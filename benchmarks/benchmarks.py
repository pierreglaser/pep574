#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author: Pierre Glaser
"""bechmarks for no-copy pickling of numpy arrays"""
import pickle

import numpy as np


class Benchmark:
    """base class for the different pickling benchmarks"""
    repeat = 1
    number = 1
    timeout = 30
    params = [
        ((100, 100), (1000, 100), (1000, 1000), (10000, 1000)),
    ]
    param_names = ['shape']

    def setup(self, shape):
        self.data = np.random.randn(*shape)


class Protocol5WithBuffer(Benchmark):
    def peakmem_pickle(self, shape):
        buffers = []
        stream = pickle.dumps(
            self.data, protocol=5, buffer_callback=buffers.append)
        b = pickle.loads(stream, buffers=buffers)
    peakmem_pickle.benchmark_name = 'peakmem_protocol_5_pickling_with_buffers'


class Protocol4(Benchmark):
    def setup(self, shape):
        self.data = np.random.randn(*shape)

    def peakmem_pickle(self, shape):
        buffers = []
        stream = pickle.dumps(self.data, protocol=4)
        b = pickle.loads(stream)
    peakmem_pickle.benchmark_name = 'peakmem_protocol_4_pickling'


class Protocol5(Benchmark):
    def peakmem_pickle(self, shape):
        buffers = []
        stream = pickle.dumps(self.data, protocol=5)
        b = pickle.loads(stream)
    peakmem_pickle.benchmark_name = 'peakmem_protocol_5_pickling'
