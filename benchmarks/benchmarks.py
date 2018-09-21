#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author: Pierre Glaser
"""bechmarks for no-copy pickling of numpy arrays"""
import gc
import os
import pickle

import numpy as np


class Benchmark:
    """base class for the different pickling benchmarks"""
    repeat = 1
    number = 1
    timeout = 30
    params = [
        ((10000, 1000), (10000, 10000)),
    ]
    param_names = ['shape']
    temp_filename = 'tmp_array.pkl'

    def setup(self, shape):
        self.data = np.random.randn(*shape)


class Protocol5WithOutOfBandBuffer(Benchmark):
    def peakmem_pickle(self, shape):
        buffers = []
        try:

            with open(self.temp_filename, 'wb') as f:
                pickle.dump(
                    self.data, f, protocol=5, buffer_callback=buffers.append)

            with open(self.temp_filename, 'rb') as f:
                self.data = pickle.load(f, buffers=buffers)

        finally:
            os.unlink(self.temp_filename)

    peakmem_pickle.benchmark_name = 'peakmem_protocol_5_pickling_with_buffers'

    def time_pickle(self, shape):
        buffers = []
        try:

            with open(self.temp_filename, 'wb') as f:
                pickle.dump(
                    self.data, f, protocol=5, buffer_callback=buffers.append)

            with open(self.temp_filename, 'rb') as f:
                self.data = pickle.load(f, buffers=buffers)

        finally:
            os.unlink(self.temp_filename)

    time_pickle.benchmark_name = 'time_protocol_5_pickling_with_buffers'


class Protocol4(Benchmark):
    def peakmem_pickle(self, shape):
        buffers = []
        try:

            with open(self.temp_filename, 'wb') as f:
                pickle.dump(
                    self.data, f, protocol=4)

            with open(self.temp_filename, 'rb') as f:
                self.data = pickle.load(f)

        finally:
            os.unlink(self.temp_filename)

    peakmem_pickle.benchmark_name = 'peakmem_protocol_4_pickling'

    def time_pickle(self, shape):
        buffers = []
        try:

            with open(self.temp_filename, 'wb') as f:
                pickle.dump(
                    self.data, f, protocol=4)

            with open(self.temp_filename, 'rb') as f:
                self.data = pickle.load(f)

        finally:
            os.unlink(self.temp_filename)

    time_pickle.benchmark_name = 'time_protocol_4_pickling'


class Protocol5(Benchmark):
    def peakmem_pickle(self, shape):
        buffers = []
        try:

            with open(self.temp_filename, 'wb') as f:
                pickle.dump(
                    self.data, f, protocol=5)

            with open(self.temp_filename, 'rb') as f:
                self.data = pickle.load(f)

        finally:
            os.unlink(self.temp_filename)

    peakmem_pickle.benchmark_name = 'peakmem_protocol_5_pickling'

    def time_pickle(self, shape):
        buffers = []
        try:

            with open(self.temp_filename, 'wb') as f:
                pickle.dump(
                    self.data, f, protocol=5)

            with open(self.temp_filename, 'rb') as f:
                self.data = pickle.load(f)

        finally:
            os.unlink(self.temp_filename)
    time_pickle.benchmark_name = 'time_protocol_5_pickling'
