import numpy as np
import tensorflow as tf
from .Layer import Layer


class BatchNormalization(Layer):
    def __init__(self,
                 gamma_initializer='ones',
                 beta_initializer='zeros',
                 eps=np.float32(1e-5)):
        super().__init__()
        self.gamma_initializer = gamma_initializer
        self.beta_initializer = beta_initializer
        self.eps = eps

    def compile(self):
        self.gamma = \
            self.kernel_initializer(self.gamma_initializer,
                                    shape=(self.input_dim),
                                    name='gamma')
        self.beta = \
            self.kernel_initializer(self.beta_initializer,
                                    shape=(self.input_dim),
                                    name='beta')

    def forward(self, x):
        axes = 0
        if len(x.get_shape()) == 4:
            axes = (0, 1, 2)
        mean, var = tf.nn.moments(x, axes, keep_dims=True)
        std = tf.sqrt(var + self.eps)
        return self.gamma * (x - mean) / std + self.beta

    def initialize_output_dim(self):
        super().initialize_output_dim()
        self.output_dim = self.input_dim
        return self.output_dim
