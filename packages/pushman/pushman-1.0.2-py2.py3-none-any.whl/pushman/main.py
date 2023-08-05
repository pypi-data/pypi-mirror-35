# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

import json
import urllib

import requests
from pywe_sign import fill_signature


class Pushman(object):
    def send_tplmsg(self, push_id, push_secret, push_url, first='', keywords=None, remark='', color='', openid=None, openids=None):
        tpldata = {
            'push_id': push_id,
            'first': first,
            'remark': remark,
            'color': color,
            'openids': json.dumps([openid] if openid else (openids or [])),
        }

        for idx, item in enumerate(keywords or [], start=1):
            tpldata['keyword{0}'.format(idx)] = item

        tpldata = fill_signature(tpldata, push_secret)

        try:
            retmsg = requests.get(push_url.format(urllib.quote_plus(json.dumps(tpldata)))).json()
        except Exception as e:
            retmsg = e.message

        return retmsg


_global_instance = Pushman()
send_tplmsg = _global_instance.send_tplmsg
