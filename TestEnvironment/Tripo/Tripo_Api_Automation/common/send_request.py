# -*- coding: UTF-8 -*-
import requests

class SendRequest:

    sess = requests.session()

    def send_all_request(self, **kwargs):
        res = SendRequest.sess.request(**kwargs)
        # res = SendRequest.requests.sessions().request(**kwargs)
        return res
