import tensorflow as tf
from . import Module
from .. import Activation
from .. import BatchNormalization
from .. import Conv2D
from .. import Dense
from .. import GlobalAveragePooling2D


class ResNet(Module):
    def __init__(self):
        pass

    def v1(self, x):
        '''
        # Arguments
            x: placeholder
        '''
        layers = [
            Conv2D(kernel_size=(7, 7, 64),
                   input_dim=x.get_shape()),
            BatchNormalization(),
            Activation('relu'),
            MaxPooling2D()
        ]
        for layer in layers:
            x = self._forward(x, layer)
        x = self._base_block(x)
        x = self._base_block(x)
        x = self._base_block(x)
        x = self._forward(x, GlobalAveragePooling2D())

        layers = [
            De
        ]

        pass

    def _base_block(self, x, channel_out=64):
        '''
        # Arguments
            x: placeholder
        '''
        layers = [
            Conv2D(kernel_size=(3, 3, channel_out),
                   input_dim=x.get_shape()),
            BatchNormalization(),
            Activation('relu'),
            Conv2D(kernel_size=(3, 3, channel_out))
            BatchNormalization()
        ]
        for layer in layers:
            h = layer(x)
        shortcut = self._shortcut(x, output_dim=h.get_shape())

        return Activation('relu')(h + shortcut)

    def _bottleneck(self, x, channel_out=256):
        '''
        # Arguments
            x: placeholder
        '''
        channel = channel_out // 4
        layers = [
            Conv2D(kernel_size=(1, 1, channel),
                   input_dim=x.get_shape()),
            BatchNormalization(),
            Activation('relu'),
            Conv2D(kernel_size=(3, 3, channel)),
            BatchNormalization(),
            Activation('relu'),
            Conv2D(kernel_size=(1, 1, channel)),
            BatchNormalization()
        ]
        for layer in layers:
            h = layer(x)
        shortcut = self._shortcut(x, output_dim=h.get_shape())

        return Activation('relu')(h + shortcut)

    def _projection(self, x, channel_out):
        layer = Conv2D(kernel_size=(1, 1, channel_out))
        return layer(x)

    def _shortcut(self, x, output_dim):
        input_dim = x.get_shape()
        input_channel = input_dim[2]
        output_channel = output_dim[2]

        if input_channel != output_channel:
            return self._projection(x, output_channel)
        else:
            return Activation('linear')(x)
