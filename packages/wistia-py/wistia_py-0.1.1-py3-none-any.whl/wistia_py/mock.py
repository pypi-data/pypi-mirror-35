from .wrapper import WistiaAPI as ActualWistiaAPI


def request_mock(*a, **kw):
    return dict(mock=True, args=a, kwargs=kw)


class WistiaAPI(ActualWistiaAPI):
    """Simple mock WistiaAPI object

    This doesn't make network requests, so it's great for unit testing.

    Accepts all the params the WistiaAPI accepts, plus request_mock.
    Logs responses to self.calls and calls request_mock for every request.

    By default, request_mock creates a dictionary with args and kwargs
    as if it was the requests.method() call.

    :param request_mock: function that can be called with this signature:
        example(method, url, data=data)

    :Example:

    from mock import patch
    from wistia_py.mock import WistiaAPI

    @patch('wistia_py.WistiaAPI')
    def test_example(WistiaAPIMock):

        responses = [
            dict(data=dict(id='sample_token')),  # mock expiring token response
        ]

        def wistia_api_call(instance, method, url, data=None):
            response = responses[len(instance.calls) - 1]
            return response

        WistiaAPIMock.return_value = WistiaAPI('mock_api_password', request_mock=wistia_api_call)

        # real code calls wistia.get_upload_expiring_token(...)
        # and receives the response from above
    """

    def __init__(self, *args, **kwargs):
        self.request_mock = kwargs.pop('request_mock', request_mock)
        super().__init__(*args, **kwargs)
        self.calls = []

    def call(self, rel_path, data=None, method='GET'):
        url = self.build_url(rel_path)
        self.calls.append(dict(
            method=method,
            url=url,
            data=data))

        return self.request_mock(self, method, url, data=data)


def get_mock(responses=None, api_password='mock_api_password'):
    """Quick convenience function for unit tests.

    :Example:
    from mock import patch
    from wistia_py.mock import get_mock


    @patch('wistia_py.WistiaAPI')
    def test_example(WistiaAPIMock):
        responses = [
            dict(data=dict(id='sample_token')),  # mock expiring token response
        ]
        WistiaAPIMock.return_value = get_mock(responses)

        # real code calls wistia.get_upload_expiring_token(...)
        # and receives the response from above
    """
    def wistia_api_call(instance, method, url, data=None):
        response = responses[len(instance.calls) - 1]
        return response

    kwargs = dict(request_mock=wistia_api_call) if responses else dict()

    return WistiaAPI(api_password, **kwargs)
