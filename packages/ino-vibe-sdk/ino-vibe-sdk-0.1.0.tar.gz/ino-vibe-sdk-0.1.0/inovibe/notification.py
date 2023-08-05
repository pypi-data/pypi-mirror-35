import abc

import grpc

import mgi_pb2
import mgi_pb2_grpc


channel = grpc.insecure_channel('localhost:50051')
stub = mgi_pb2_grpc.FCMNotificationStub(channel)


class MessageBase(metaclass=abc.ABCMeta):
    def __init__(self, devid, alias):
        self._devid = devid
        self._alias = alias

    @abc.abstractproperty
    def msg_type(self):
        return ''

    @property
    def devid(self):
        return self._devid

    @property
    def alias(self):
        return self._alias


class PowerUpMessage(MessageBase):
    def __init__(self, devid, alias):
        super(self.__class__, self).__init__(devid, alias)

    @property
    def msg_type(self):
        return 'power_up'


class PowerOffMessage(MessageBase):
    def __init__(self, devid, alias):
        super(self.__class__, self).__init__(devid, alias)

    @property
    def msg_type(self):
        return 'power_off'


class InstallCompleteMessage(MessageBase):
    def __init__(self, devid, alias):
        super(self.__class__, self).__init__(devid, alias)

    @property
    def msg_type(self):
        return 'complete'


class ExcavationMessage(MessageBase):
    def __init__(self, devid, alias):
        super(self.__class__, self).__init__(devid, alias)

    @property
    def msg_type(self):
        return 'alert'


class InclinationMessage(MessageBase):
    def __init__(self, devid, alias):
        super(self.__class__, self).__init__(devid, alias)

    @property
    def msg_type(self):
        return 'inclination'


def send_by_tokens(message, tokens):
    """Send notification message by user's device token.
    This API function should be decrecated near future because this function is
    only for backward compatibility.
    """

    req = mgi_pb2.FCMByTokenRequest(device_tokens=tokens,
                                    data={
                                        'type': message.msg_type,
                                        'ltid': message.devid,
                                        'alias': message.alias
                                    })

    stub.SendByTokens(req)


def register_token(email, token):
    # TODO:
    pass


def send_notification(message):
    # TODO:
    pass
