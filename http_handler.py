'''
Created on 10 Dec 2011

@author: v0mit
'''

import urllib.request
import urllib.parse


class http_handler():
    def __init__(self):
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())

        self.user_agent = 'http_handler.Py3.v0.1 v0mit@darkpy.net'
        self.opener.addheaders = [('User-agent', self.user_agent)]

        urllib.request.install_opener(self.opener)

    def request(self, url, data=None):
        req = urllib.request.Request(url)

        if data:
            try:
                data = urllib.parse.urlencode(data)
            except TypeError as errno:
                raise HTTPError("Invalid data: {0}".format(errno))

            try:
                response = self.opener.open(req, data)
            except urllib.error as errno:
                raise HTTPError("[!]urllib.error({0})\n[URL:{1}][Data:{2}".format(errno, url, data))

            return response.read()

        else:
            try:
                response = self.opener.open(req)
            except urllib.error as errno:
                raise HTTPError("[!]urllib.error({0})\n[URL:{1}]".format(errno, url))

            except ValueError as errno:
                raise HTTPError("[!]ValueError({0}\n".format(errno))

            return response.read()


class HTTPError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
