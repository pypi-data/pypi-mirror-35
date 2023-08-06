# -*- coding: utf-8 -*-
import json
from hashlib import md5

from ...util.protocol import WsClientFactory, WsClientProtocol


def get_unsigned_str(param, secret_key):
    unsigned_params = sorted(param.items())
    unsigned_params.append(('secret_key', secret_key))
    return '&'.join([
        '='.join([str(param[0]), str(param[1])]) for param in unsigned_params
    ])


def sign(unsigned_str):
    m = md5()
    m.update(unsigned_str.encode('utf-8'))
    return m.hexdigest().upper()


def signed_rest_str(param, secret_key):
    """ sign rest params and return signed param str

    :param params: {key: value}
    :returns: signed params str

    """
    unsigned_str = get_unsigned_str(param, secret_key)
    sig = sign(unsigned_str)
    return unsigned_str + '&sign={}'.format(sig)


def signed_ws_param(param, secret_key):
    unsigned_str = get_unsigned_str(param, secret_key)
    sig = sign(unsigned_str)
    param['sign'] = sig
    return param


class OKEXWsClientFactory(WsClientFactory):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.proto_inst = None
        self.connected_channels = set()


class OKEXWsClientProtocol(WsClientProtocol):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.autoPingInterval = 30
        self.autoPingTimeout = 30
        self._channel_handlers = {}

    def _on_text(self, payload):
        msgs = json.loads(payload)
        for msg in msgs:
            self._on_msg(msg)

    def _on_msg(self, msg):
        try:
            channel_suffix = msg['channel'].split('_')[-1]
            if channel_suffix in self._channel_handlers:
                self._channel_handlers[channel_suffix](msg['channel'], msg)
            else:
                self.log.warn('receive unexpected msg {}'.format(msg))
        except KeyError:
            self.log.warn('receive unexpected msg {}'.format(msg))

    def _parse_symbol(self, channel):
        return '_'.join(channel.split('_')[3:5])


if __name__ == '__main__':
    params = {
        'api_key': 'c821db84-6fbd-11e4-a9e3-c86000d26d7c',
        'symbol': 'btc_usdt',
        'type': 'buy',
        'price': 680,
        'amount': 1.0,
        'symbol': 'btc_usdt',
    }
    print(signed_rest_str(params, 'ffwerjhiewuroi'))
