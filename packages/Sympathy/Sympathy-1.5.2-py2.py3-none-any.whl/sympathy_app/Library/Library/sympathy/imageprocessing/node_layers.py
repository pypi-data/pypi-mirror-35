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

from __future__ import (print_function, division, unicode_literals,
                        absolute_import)
from sympathy.api import node
from sympathy.api.nodeconfig import Port, Ports, Tag, Tags

import numpy as np
from sylib.imageprocessing.image import Image
from sylib.imageprocessing.algorithm_selector import ImageFiltering_abstract


class OverlayImages(ImageFiltering_abstract, node.Node):
    name = 'Overlay Images'
    author = 'Mathias Broxvall'
    copyright = '(C) 2017 System Engineering Software Society'
    version = '0.1'
    icon = 'image_overlay.svg'
    description = (
        'Combines two images by layering the first (top port) image on top of '
        'the other (bottom port) image\n, with choice for combining operator. '
        'Images must have the same number of channels')
    nodeid = 'syip.overlay'
    tags = Tags(Tag.ImageProcessing.Layers)

    default_parameters = {
        'use alpha channel': 'Use last channel of source images as alpha channel',
        'alpha': 'Alpha value used when no alpha channel is given'
    }
    algorithms = {
        'additive': dict({
            'description': 'Adds the two images together where they overlap.',
            'unity': 0.0,
            'expr': lambda result, im: result + im,
            'multichromatic': True
        }, **default_parameters),
        'multiplicative': dict({
            'description': 'Multiplies images where they overlap.',
            'unity': 1.0,
            'expr': lambda result, im: result * im,
            'multichromatic': True
        }, **default_parameters),
        'divide': dict({
            'description': 'Divides bottom image by all other images.',
            'unity': 1.0,
            'expr': lambda result, im: result / im,
            'multichromatic': True
        }, **default_parameters),
        'subtract': dict({
            'description': 'Subtracts top image from bottom.',
            'unity': 0.0,
            'expr': lambda result, im: result - im,
            'multichromatic': True
        }, **default_parameters),
        'max': dict({
            'description': 'Takes the maximum value of the images.',
            'unity': 0.0,
            'expr': lambda result, im: np.maximum(result, im),
            'multichromatic': True
        }, **default_parameters),
        'min': dict({
            'description': 'Takes the minimum value of the images.',
            'unity': 0.0,
            'expr': lambda result, im: np.minimum(result, im),
            'multichromatic': True
        }, **default_parameters),
        'layer': dict({
            'description': (
                'Layers on image on top of the other, alpha channel (if any) '
                'determines transparency. Otherwise alpha value below'),
            'unity': 0.0,
            'expr': lambda result, im: im,
            'multichromatic': True
        }, **default_parameters),
    }

    options_list  = [
        'use alpha channel', 'alpha'
    ]
    options_types = {
        'use alpha channel': bool, 'alpha': float
    }
    options_default = {
        'use alpha channel': False, 'alpha': 1.0
    }

    parameters = node.parameters()
    parameters.set_string(
        'algorithm', value=next(iter(algorithms)), description='',
        label='Algorithm')
    ImageFiltering_abstract.generate_parameters(
        parameters, options_types, options_default)

    inputs = Ports([
        Port.Custom('image', 'Input images', name='images', n=(2,))
    ])
    outputs = Ports([
        Image('result after filtering', name='result'),
    ])
    __doc__ = ImageFiltering_abstract.generate_docstring(
        description, algorithms, options_list, inputs, outputs)

    def execute(self, node_context):
        images = [
            obj.get_image() for obj in node_context.input.group('images')]

        params   = node_context.parameters
        alg_name = params['algorithm'].value
        use_alpha = params['use alpha channel'].value

        # Reshape so all images guaranteed to have 3 dimensions
        images = [
            (im.reshape(im.shape + (1,)) if len(im.shape) < 3 else im)
            for im in images]

        # Compute max size
        max_y = max([im.shape[0] for im in images])
        max_x = max([im.shape[1] for im in images])
        max_c = max([im.shape[2] for im in images])

        if alg_name == 'multiplicative':
            unity = 1.0
        elif alg_name == 'divide':
            unity = 1.0
        else:
            unity = 0.0

        result = np.full((max_y, max_x, max_c), unity)
        if any([im.dtype.kind == 'c' for im in images]):
            result = result.astype(np.complex)

        bot = images[-1]
        result[:bot.shape[0], :bot.shape[1], :bot.shape[2]] = bot
        rest = images[:-1]

        alpha = params['alpha'].value
        for im in rest[::-1]:
            for c in range(im.shape[2]):
                expr    = OverlayImages.algorithms[alg_name]['expr']
                y, x, _ = im.shape
                if use_alpha:
                    result[:y, :x, c] = (
                        result[:y, :x, c] * (1-im[:, :, -1]) +
                        im[:, :, -1] * expr(result[:y, :x, c], im[:, :, c]))
                else:
                    result[:y, :x, c] = (
                        result[:y, :x, c] * (1-alpha) +
                        alpha * expr(result[:y, :x, c], im[:, :, c]))
        node_context.output['result'].set_image(result)
