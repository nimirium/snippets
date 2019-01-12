__all__ = ['Request', 'send_parallel_http_requests']

from requests_futures.sessions import FuturesSession
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Request:
    def __init__(self, url, method='GET', headers=None, data=None, return_response=True):
        """
        Describes a http request.
        :param str url:
        :param str method:
        :param dict headers:
        :param data:
        :param bool return_response: Will wait for and return the response for this request only if return_response
            is True. Default is True.
        """
        self.url = url
        self.method = method
        self.headers = headers
        self.data = data
        self.return_response = return_response


def send_parallel_http_requests(requests_list):
    """
    Send a list of parallel HTTP requests.

    :param list requests_list: list of RequestInfo objects
    :return: a list of `requests.models.Response`.
    """

    assert type(requests_list) is list, "requests_list must be a list"
    for r in requests_list:
        assert type(r) is Request, "Each item in requests_list must be a Request."

    with FuturesSession(max_workers=10) as session:
        requests_waiting_for_response = []
        for r in requests_list:
            req_kwargs = {
                'method': r.method,
                'url': r.url,
            }
            if r.headers:
                req_kwargs['headers'] = r.headers
            if r.data:
                req_kwargs['data'] = r.data
            if r.data:
                req_kwargs['data'] = r.data
            try:
                sr = session.request(**req_kwargs)
                if r.return_response:
                    requests_waiting_for_response.append(sr)
            except:
                logger.exception("Sending request failed")

        responses = []
        for x in requests_waiting_for_response:
            try:
                responses.append(x.result())
            except:
                logger.exception("Getting response failed")

        return responses
