import unittest
from parallel_http_requests import Request, send_parallel_http_requests


class ParallelHttpRequestTestCase(unittest.TestCase):
    def test_send_parallel_http_requests(self):
        responses = send_parallel_http_requests([
            Request('https://jsonplaceholder.typicode.com/posts', return_response=False),
            Request('https://jsonplaceholder.typicode.com/posts', method='GET'),
            Request('https://jsonplaceholder.typicode.com/posts', headers={'test': 'test1'}, return_response=False),
            Request('https://jsonplaceholder.typicode.com/posts', method='POST', data={
              'title': 'foo',
              'body': 'bar',
              'userId': 1
            }, return_response=True),
        ])

        print(f"RESPONSES!")
        print(f"{responses}")

        for r in responses:
            print(f"url: {r.url}")
            print(f"status code: {r.status_code}")
            print(f"data: {r.content}")
            print(f"headers: {r.headers}")
            print("")

        self.assertEqual(len(responses), 2)
