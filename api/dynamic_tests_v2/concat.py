#   Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from common_import import *


class PaddleConcat(PaddleDynamicAPIBenchmarkBase):
    def build_graph(self, config):
        xs = []
        for i in range(len(config.x_shape)):
            x_i = self.variable(
                name='x_' + str(i),
                shape=config.x_shape[i],
                dtype=config.x_dtype[i])
            xs.append(x_i)
        self.feed_list = xs

    def run_graph(self, config):
        result = paddle.concat(x=self.feed_list, axis=config.axis)
        self.fetch_list = [result]
        if config.backward:
            self.append_gradients(result, self.feed_list)


class TorchConcat(PytorchAPIBenchmarkBase):
    def build_graph(self, config):
        xs = []
        for i in range(len(config.x_shape)):
            x_i = self.variable(
                name='x_' + str(i),
                shape=config.x_shape[i],
                dtype=config.x_dtype[i])
            xs.append(x_i)
        self.feed_list = xs

    def run_graph(self, config):
        result = torch.cat(tensors=self.feed_list, dim=config.axis)
        self.fetch_list = [result]
        if config.backward:
            self.append_gradients(result, self.feed_list)


if __name__ == '__main__':
    test_main(
        pd_dy_obj=PaddleConcat(),
        torch_obj=TorchConcat(),
        config=APIConfig("concat"))
