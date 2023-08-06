#
# Copyright (c) 2017 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import List

import tensorflow as tf

from rl_coach.architectures.tensorflow_components.architecture import Dense
from rl_coach.architectures.tensorflow_components.embedders.embedder import InputEmbedder
from rl_coach.base_parameters import EmbedderScheme
from rl_coach.core_types import InputVectorEmbedding


class VectorEmbedder(InputEmbedder):
    """
    An input embedder that is intended for inputs that can be represented as vectors.
    The embedder flattens the input, applies several dense layers to it and returns the output.
    """
    schemes = {
        EmbedderScheme.Empty:
            [],

        EmbedderScheme.Shallow:
            [
                Dense([128])
            ],

        # dqn
        EmbedderScheme.Medium:
            [
                Dense([256])
            ],

        # carla
        EmbedderScheme.Deep: \
            [
                Dense([128]),
                Dense([128]),
                Dense([128])
            ]
    }

    def __init__(self, input_size: List[int], activation_function=tf.nn.relu,
                 scheme: EmbedderScheme=EmbedderScheme.Medium, batchnorm: bool=False, dropout: bool=False,
                 name: str= "embedder", input_rescaling: float=1.0, input_offset:float=0.0, input_clipping=None):
        super().__init__(input_size, activation_function, scheme, batchnorm, dropout, name,
                         input_rescaling, input_offset, input_clipping)

        self.return_type = InputVectorEmbedding
        if len(self.input_size) != 1 and scheme != EmbedderScheme.Empty:
            raise ValueError("The input size of a vector embedder must contain only a single dimension")
