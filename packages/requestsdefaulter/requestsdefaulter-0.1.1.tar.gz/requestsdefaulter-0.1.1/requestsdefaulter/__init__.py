import requests

name = "requestsdefaulter"


def default_headers(default_functions):
    original_prepare_headers = requests.models.PreparedRequest.prepare_headers

    def new_prepare_headers(self, headers):
        defaults = default_functions()

        if headers is not None:
            defaults.update(headers)

        original_prepare_headers(self, defaults)

    requests.models.PreparedRequest.prepare_headers = new_prepare_headers
