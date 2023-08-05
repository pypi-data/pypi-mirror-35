# -*- coding: utf-8 -*-
import logging
import traceback

from time import gmtime, strftime
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core.models.entity import http
from aws_xray_sdk.ext.util import calculate_sampling_decision, \
    calculate_segment_name, construct_xray_header


log = logging
log.basicConfig(
                format='%(asctime)s [%(levelname)s] - %(name)s - %(message)s',
                datefmt='[%Y/%m/%d %I:%M:%S %p]'
               )


class XRay(object):
    _recorder = None

    def process_request(self, req, resp):
        try:
            logging.info('initializing xray middleware')
            self._recorder = xray_recorder
            self._recorder.configure(plugins=('EC2Plugin', 'ECSPlugin'), daemon_address='localhost:2000')

            headers = req.headers
            xray_header = construct_xray_header(headers)

            name = calculate_segment_name(req.host, self._recorder)

            sampling_decision = calculate_sampling_decision(
                trace_header=xray_header,
                recorder=self._recorder,
                service_name=req.host,
                method=req.method,
                path=req.path,
            )

            segment = self._recorder.begin_segment(
                name=name,
                traceid=xray_header.root,
                parent_id=xray_header.parent,
                sampling=sampling_decision,
            )

            segment.save_origin_trace_header(xray_header)
            segment.put_http_meta(http.URL, req.uri)
            segment.put_http_meta(http.METHOD, req.method)
            segment.put_http_meta(http.USER_AGENT, headers.get('User-Agent'))
            segment.put_metadata('x-ray_middleware', {'uri': req.uri, 'method': req.method,
                                                      'request': req.media},  __name__)
            segment.put_annotation('dateTime', strftime("%Y-%m-%d %H:%M:%S", gmtime()))

            client_ip = headers.get('X-Forwarded-For') or headers.get('HTTP_X_FORWARDED_FOR')
            if client_ip:
                segment.put_http_meta(http.CLIENT_IP, client_ip)
                segment.put_http_meta(http.X_FORWARDED_FOR, True)
            else:
                segment.put_http_meta(http.CLIENT_IP, req.remote_addr)

        except Exception as e:
            log.debug(str(e))
            self._handler_exception(e)

    def process_response(self, req, resp, resource, req_succeeded):
        try:
            if not req_succeeded:
                raise Exception('response error on resource: %s with message: %s' % (resource, resp.media))

            segment = self._recorder.current_segment()
            status_code = resp.status.split()
            segment.put_http_meta(http.STATUS, int(status_code[0]))

            cont_len = resp.get_header('Content-Length')
            if cont_len:
                segment.put_http_meta(http.CONTENT_LENGTH, int(cont_len))

            self._recorder.end_segment()
        except Exception as e:
            log.debug(str(e))
            self._handler_exception(e)

    def _handler_exception(self, exception):
        try:
            if not exception:
                return
            segment = self._recorder.current_segment()
            segment.put_http_meta(http.STATUS, 500)
            stack = traceback.extract_stack(limit=self._recorder._max_trace_back)
            segment.add_exception(exception, stack)
            self._recorder.end_segment()
        except Exception as e:
            log.debug(str(e))
