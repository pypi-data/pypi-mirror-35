# Copyright (c) 2016, System Engineering Software Society
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the System Engineering Software Society nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.
# IN NO EVENT SHALL SYSTEM ENGINEERING SOFTWARE SOCIETY BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
from __future__ import (print_function, division, unicode_literals,
                        absolute_import)


class Message(object):
    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        return self._data

    @property
    def type(self):
        return self.__class__

    def to_dict(self):
        return {'type': self.__class__.__name__, 'data': self._data}


class DataBlockedMessage(Message):
    def __init__(self, uuid):
        super(DataBlockedMessage, self).__init__(uuid)

class DataReadyMessage(Message):
    def __init__(self, uuid):
        super(DataReadyMessage, self).__init__(uuid)


class DataRequestMessage(Message):
    def __init__(self, uuid):
        super(DataRequestMessage, self).__init__(uuid)


class StatusDataRequestMessage(Message):
    def __init__(self, uuid):
        super(StatusDataRequestMessage, self).__init__(uuid)


class AggConfigUpdateMessage(Message):
    def __init__(self, dict_data):
        super(AggConfigUpdateMessage, self).__init__(dict_data)


class RaiseWindowMessage(Message):
    def __init__(self, uuid):
        super(RaiseWindowMessage, self).__init__(uuid)


class ProgressMessage(Message):
    def __init__(self, value):
        super(ProgressMessage, self).__init__(value)


class StatusMessage(Message):
    def __init__(self, value):
        super(StatusMessage, self).__init__(value)


class PortDataReadyMessage(Message):
    def __init__(self, value):
        super(PortDataReadyMessage, self).__init__(value)

    @classmethod
    def init_args(cls, uuid, filename, dtype):
        return cls({'uuid': uuid, 'file': filename, 'type': dtype})

    @property
    def filename(self):
        return self._data['file']

    @property
    def dtype(self):
        # Warning! do not confuse with property named type.
        return self._data['type']

    @property
    def uuid(self):
        return self._data['uuid']


def from_dict(msg_dict):
    cls = globals()[msg_dict['type']]
    return cls(msg_dict['data'])
