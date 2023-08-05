# Copyright (c) 2017, System Engineering Software Society
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
"""
Some of the docstrings for this module have been automatically
extracted from the `scikit-learn <http://scikit-learn.org/>`_ library
and are covered by their respective licenses.
"""

from __future__ import (print_function, division, unicode_literals,
                        absolute_import)
import sklearn
import sklearn.svm

from sympathy.api import node
from sympathy.api.nodeconfig import Ports, Tag, Tags

from sylib.machinelearning.model import ModelPort
from sylib.machinelearning.abstract_nodes import SyML_abstract
from sylib.machinelearning.utility import names_from_x
from sylib.machinelearning.descriptors import Descriptor

from sylib.machinelearning.descriptors import BoolType
from sylib.machinelearning.descriptors import FloatType
from sylib.machinelearning.descriptors import IntType
from sylib.machinelearning.descriptors import NoneType
from sylib.machinelearning.descriptors import StringSelectionType
from sylib.machinelearning.descriptors import UnionType


class SupportVectorClassifier(SyML_abstract, node.Node):
    name = 'Support Vector Classifier'
    author = 'Mathias Broxvall'
    copyright = '(C) 2017 System Engineering Software Society'
    version = '0.1'
    icon = 'svm.svg'
    description = 'Support vector machine (SVM) based classifier'
    nodeid = 'org.sysess.sympathy.machinelearning.svc'
    tags = Tags(Tag.MachineLearning.Supervised)

    descriptor = Descriptor()
    descriptor.name = name
    descriptor.set_info([
        {'name': 'C',
         'type': FloatType(min_value=0.0, default=1.0)},
        {'name': 'kernel',
         'type': StringSelectionType([
              'rbf', 'linear', 'poly', 'sigmoid', 'precomputed'],
            default='rbf')},
        {'name': 'degree',
         'type': IntType(min_value=1, default=3)},
        {'name': 'gamma',
         'type': UnionType([
             FloatType(), StringSelectionType(['auto'])],
            default='auto')},
        {'name': 'coef0',
         'type': FloatType(default=0.0)},
        {'name': 'probability',
         'type': BoolType(default=False)},
        {'name': 'shrinking',
         'type': BoolType(default=True)},
        {'name': 'tol',
         'type': FloatType(default=1e-3)},
        {
            'name': 'class_weight',
            'type': UnionType([
                NoneType(),
                StringSelectionType(['balanced'])
            ], default=None
            )
        },
        {'name': 'max_iter',
         'type': IntType(min_value=-1)},
        {'name': 'random_state',
         'type': UnionType([
             IntType(), NoneType()], default=None)},
    ], doc_class=sklearn.svm.SVC)

    descriptor.set_attributes([
        {'name': 'support_', },
        {'name': 'support_vectors_', 'cnames': names_from_x},
        {'name': 'n_support_'},
        {'name': 'dual_coef_'},
        {'name': 'coef_', 'cnames': names_from_x},
        {'name': 'intercept_'},
    ], doc_class=sklearn.svm.SVC)

    parameters = node.parameters()
    SyML_abstract.generate_parameters(parameters, descriptor)

    inputs = Ports([])
    outputs = Ports([ModelPort('Model', 'model')])
    __doc__ = SyML_abstract.generate_docstring(
        description, descriptor.info, descriptor.attributes, inputs, outputs)

    def execute(self, node_context):
        model = node_context.output['model']
        desc = self.__class__.descriptor
        model.set_desc(desc)

        kwargs = self.__class__.descriptor.get_parameters(
            node_context.parameters)
        skl = sklearn.svm.SVC(**kwargs)

        model.set_skl(skl)
        model.save()


class OneClassSVM(SyML_abstract, node.Node):
    name = 'One Class SVM'
    author = 'Mathias Broxvall'
    copyright = '(C) 2017 System Engineering Software Society'
    version = '0.1'
    icon = 'outliers.svg'
    description = (
        'Unsupervised outlier detection based on support vector machines'
    )
    nodeid = 'org.sysess.sympathy.machinelearning.one_class_svm'
    tags = Tags(Tag.MachineLearning.Unsupervised)

    descriptor = Descriptor()
    descriptor.name = name
    descriptor.set_info([
        {'name': 'kernel',
         'type': StringSelectionType([
              'rbf', 'linear', 'poly', 'sigmoid', 'precomputed'],
            default='rbf')},
        {'name': 'nu',
         'type': FloatType(min_value=0, max_value=1, default=0.5)},
        {'name': 'degree',
         'type': IntType(min_value=1, default=3)},
        {'name': 'gamma',
         'type': UnionType([
             FloatType(), StringSelectionType(['auto'])],
            default='auto')},
        {'name': 'coef0',
         'type': FloatType(default=0.0)},
        {'name': 'shrinking',
         'type': BoolType(default=True)},
        {'name': 'tol',
         'type': FloatType(default=1e-3)},
        {'name': 'max_iter',
         'type': IntType(min_value=-1)},
        {'name': 'random_state',
         'type': UnionType([
             IntType(), NoneType()], default=None)},
    ], doc_class=sklearn.svm.OneClassSVM)

    descriptor.set_attributes([
        {'name': 'support_', },
        {'name': 'support_vectors_', 'cnames': names_from_x},
        {'name': 'dual_coef_'},
        {'name': 'coef_', 'cnames': names_from_x},
        {'name': 'intercept_'},
    ], doc_class=sklearn.svm.OneClassSVM)

    parameters = node.parameters()
    SyML_abstract.generate_parameters(parameters, descriptor)

    inputs = Ports([])
    outputs = Ports([ModelPort('Model', 'model')])
    __doc__ = SyML_abstract.generate_docstring(
        description, descriptor.info, descriptor.attributes, inputs, outputs)

    def execute(self, node_context):
        model = node_context.output['model']
        desc = self.__class__.descriptor
        model.set_desc(desc)

        kwargs = self.__class__.descriptor.get_parameters(
            node_context.parameters)
        skl = sklearn.svm.OneClassSVM(**kwargs)

        model.set_skl(skl)
        model.save()
