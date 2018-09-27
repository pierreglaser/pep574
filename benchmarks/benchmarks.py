#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author: Pierre Glaser
"""bechmarks for no-copy pickling of numpy arrays"""
import gc
import os
import sys

import numpy as np


class Benchmark:
    """base class for the different pickling benchmarks"""
    repeat = 1
    number = 1
    timeout = 30
    params = [
        (
            # (10000, 1000),
            (10000, 10000),
        ),
    ]
    param_names = ['shape']
    temp_filename = 'tmp_array.pkl'
    processes = 2

    def setup(self, shape):
        self.data = np.arange(int(1e8))


class Protocol5WithOutOfBandBuffer(Benchmark):
    def peakmem_pickle(self, shape):
        # In <3.8 pythons, the pickle module does not provide protocol 5
        # support, so we use the pickle5 backport instead
        if sys.version < '3.8':
            import pickle5 as pickle
        else:
            import pickle
        buffers = []
        try:

            with open(self.temp_filename, 'wb') as f:
                pickle.dump(
                    self.data, f, protocol=5, buffer_callback=buffers.append)

            del self.data
            gc.collect()

            with open(self.temp_filename, 'rb') as f:
                new_data = pickle.load(f, buffers=buffers)

        finally:
            os.unlink(self.temp_filename)

    peakmem_pickle.benchmark_name = (
        'peakmem_protocol_5_pickling_with_out_of_band_buffers')

    def time_pickle(self, shape):
        if sys.version < '3.8':
            import pickle5 as pickle
        else:
            import pickle
        buffers = []
        try:

            with open(self.temp_filename, 'wb') as f:
                pickle.dump(
                    self.data, f, protocol=5, buffer_callback=buffers.append)

            del self.data
            gc.collect()

            with open(self.temp_filename, 'rb') as f:
                new_data = pickle.load(f, buffers=buffers)

        finally:
            os.unlink(self.temp_filename)

    time_pickle.benchmark_name = (
        'time_protocol_5_pickling_with_out_of_band_buffers')


class Protocol4(Benchmark):
    def peakmem_pickle(self, shape):
        import pickle

        buffers = []
        try:

            with open(self.temp_filename, 'wb') as f:
                pickle.dump(self.data, f, protocol=4)

            del self.data
            gc.collect()

            with open(self.temp_filename, 'rb') as f:
                new_data = pickle.load(f)

        finally:
            os.unlink(self.temp_filename)

    peakmem_pickle.benchmark_name = 'peakmem_protocol_4_pickling'

    def time_pickle(self, shape):
        import pickle
        buffers = []
        try:

            with open(self.temp_filename, 'wb') as f:
                pickle.dump(self.data, f, protocol=4)

            del self.data
            gc.collect()

            with open(self.temp_filename, 'rb') as f:
                new_data = pickle.load(f)

        finally:
            os.unlink(self.temp_filename)

    time_pickle.benchmark_name = 'time_protocol_4_pickling'


class Protocol5NoOutOfBandBuffer(Benchmark):
    def peakmem_pickle(self, shape):
        if sys.version < '3.8':
            import pickle5 as pickle
        else:
            import pickle

        buffers = []
        try:

            with open(self.temp_filename, 'wb') as f:
                pickle.dump(self.data, f, protocol=5)

            del self.data
            gc.collect()

            with open(self.temp_filename, 'rb') as f:
                new_data = pickle.load(f)

        finally:
            os.unlink(self.temp_filename)

    peakmem_pickle.benchmark_name = (
        'peakmem_protocol_5_pickling_no_out_of_band_buffer')

    def time_pickle(self, shape):
        if sys.version < '3.8':
            import pickle5 as pickle
        else:
            import pickle
        buffers = []
        try:

            with open(self.temp_filename, 'wb') as f:
                pickle.dump(self.data, f, protocol=5)

            del self.data
            gc.collect()

            with open(self.temp_filename, 'rb') as f:
                new_data = pickle.load(f)

        finally:
            os.unlink(self.temp_filename)

    time_pickle.benchmark_name = (
        'time_protocol_5_pickling_no_out_of_band_buffer')


# class ArrayReduceEx(Benchmark):
#     def peakmem_reduce_ex(self, shape):
#         _ = self.data.__reduce_ex__(5)

#     peakmem_reduce_ex.benchmark_name = 'peakmem_reduce_ex'

#     def peakmem_reduce(self, shape):
#         _ = self.data.__reduce__()

#     peakmem_reduce.benchmark_name = 'peakmem_reduce'
