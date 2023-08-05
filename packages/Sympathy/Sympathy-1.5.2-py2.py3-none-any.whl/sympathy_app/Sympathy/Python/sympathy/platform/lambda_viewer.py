# Copyright (c) 2013, System Engineering Software Society
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

from PySide import QtGui

from .viewerbase import ViewerBase


class LambdaViewer(ViewerBase):
    def __init__(self, data=None, console=None, parent=None):
        super(LambdaViewer, self).__init__(parent)

        self._name_label = QtGui.QLabel()
        self._identifier_label = QtGui.QLabel()
        self.update_data(data)

        layout = QtGui.QFormLayout()
        layout.addRow('Name', self._name_label)
        layout.addRow('Full UUID', self._identifier_label)
        self.setLayout(layout)

    def data(self):
        return self._data

    def update_data(self, data):
        self._data = data
        if data is not None:
            try:
                flow, ports = data.get()
                self._name_label.setText(self._data.name())
                self._identifier_label.setText(self._data.identifier())
            except ValueError:
                pass
