# -*- coding: utf-8 -*-
import json

from autobahn.twisted.websocket import (WebSocketClientFactory,
                                        WebSocketClientProtocol)
from twisted.internet.protocol import ReconnectingClientFactory


class WsClientProtocol(WebSocketClientProtocol):
    def __init__(self, *args, **kwargs):
        self.factory = None
        super().__init__(*args, **kwargs)

    def onConnect(self, response):
        self.log.info('server connected: {0}'.format(response.peer))
        self.factory.resetDelay()

    def onOpen(self):
        self.log.info('websocket connection open')
        # TODO: may not be managed here
        self.factory.proto_inst = self
        self._on_open()

    def _on_open(self):
        pass

    def send_text(self, msg):
        self.sendMessage(json.dumps(msg, ensure_ascii=False).encode('utf8'))

    def onMessage(self, payload, isBinary):
        if isBinary:
            self.log.debug('binary message received: {0} bytes'.format(
                len(payload)))
            self._on_binary(payload)
        else:
            self.log.debug('text message received: {0} bytes'.format(
                len(payload)))
            self._on_text(payload.decode('utf8'))

    def _on_text(self, payload):
        pass

    def _on_binary(self, payload):
        pass

    def onClose(self, wasClean, code, reason):
        self.log.warn('webSocket connection closed: {}'.format(reason))
        self._on_close(reason)

    def _on_close(self, reason):
        self.factory.proto_inst = None  # TODO: may use weakref


class WsClientFactory(WebSocketClientFactory, ReconnectingClientFactory):
    protocol = WsClientProtocol

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tcpNoDelay = True
        self.openHandshakeTimeout = 30
        self.closeHandshakeTimeout = 30

    def clientConnectionFailed(self, connector, reason):
        self.log.error('connect ws server failed, reason: {}'.format(reason))
        self.retry(connector)

    def clientConnectionLost(self, connector, reason):
        self.log.warn(
            'lost connection to ws server, reason: {}'.format(reason))
        self.retry(connector)
