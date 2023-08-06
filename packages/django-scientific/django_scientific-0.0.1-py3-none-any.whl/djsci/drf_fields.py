# -*- coding:utf-8 -*-
# Django RestFramework (DRF) serializer fields

from rest_framework.fields import Field as DRFField
import numpy as np
try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False


class DRFNumpyArrayField(DRFField):
    def to_representation(self, value):
        result = {
            "type": "NumpyArray",
            "dtype": value.dtype.str,
            "shape": list(value.shape),
            "data": value.tolist()
        }
        return result

    def to_internal_value(self, data):
        if isinstance(data, list):
            return np.array(data)
        elif isinstance(data, dict):
            return np.array(data['data'], dtype=data.get('dtype'))
        else:
            raise NotImplementedError(u'Data type {} is not supported by DRFNumpyArrayField.'.format(type(data)))


class DRFPandasDataFrameField(DRFField):
    def to_representation(self, value):
        if not HAS_PANDAS:
            raise RuntimeError("Pandas not installed!")

    def to_internal_value(self, data):
        if not HAS_PANDAS:
            raise RuntimeError("Pandas not installed!")


class DRFPandasSeriesField(DRFField):
    def to_representation(self, value):
        if not HAS_PANDAS:
            raise RuntimeError("Pandas not installed!")

    def to_internal_value(self, data):
        if not HAS_PANDAS:
            raise RuntimeError("Pandas not installed!")

