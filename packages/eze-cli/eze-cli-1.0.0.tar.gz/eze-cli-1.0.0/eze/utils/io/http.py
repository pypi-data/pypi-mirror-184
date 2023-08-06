"""Networking helpers
"""
import json
import urllib.request
import urllib.error
from json import JSONDecodeError

import re

from eze.utils.error import EzeNetworkingError
from eze.utils.log import log_debug


def request_json(url: str, data=None, headers=None, method=None) -> dict:
    """
    requests a url and convert return into json

    :raises EzeNetworkingError: on networking error or json decoding error"""
    log_debug(f"calling url '{url}'")
    if not headers:
        headers = {}
    contents = request(url, data=data, headers=headers, method=method)
    try:
        return json.loads(contents)
    except JSONDecodeError as error:
        raise EzeNetworkingError(f"Error in JSON response '{url}', {contents} ({error})")


def request(url: str, data=None, headers=None, method=None) -> str:
    """
    requests a url and returns string

    :raises EzeNetworkingError: on networking error
    """
    if not headers:
        headers = {}
    try:
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        # nosec: Request is being built directly above as a explicit http request
        # hence no risk of unexpected scheme
        with urllib.request.urlopen(req) as stream:  # nosec # nosemgrep
            return stream.read()

    except urllib.error.HTTPError as error:
        error_text = error.read().decode()
        error_message = f"{error.code} ({error.reason} [{error_text}]"

        raise EzeNetworkingError(f"Error accessing url '{url}', Error: {error_message}")
    except urllib.error.URLError as error:
        raise EzeNetworkingError(f"Error accessing url '{url}', Error: {error}")


def spine_case_url(url: str) -> str:
    """convert url into spine case, file name safe version"""
    cleaned_url = re.sub("^https?:?[/][/]", "", url)
    cleaned_url = re.sub("^[a-zA-Z0-9.]+@[a-zA-Z0-9.]+:", "", cleaned_url)
    cleaned_url = re.sub("\\.[a-z]{,4}$", "", cleaned_url)
    cleaned_url = re.sub("[^a-zA-Z0-9]+", "-", cleaned_url)
    cleaned_url = re.sub("[-]+", "-", cleaned_url)
    return cleaned_url
