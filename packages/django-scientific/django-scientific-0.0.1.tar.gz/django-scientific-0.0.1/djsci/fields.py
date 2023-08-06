# -*- coding:utf-8 -*-

from picklefield.fields import PickledObjectField


class NumpyArrayField(PickledObjectField):
    # TODO: customize value_to_string(), etc
    pass


class PandasSeriesField(PickledObjectField):
    # TODO: customize value_to_string(), etc
    pass


class PandasDataFrameField(PickledObjectField):
    # TODO: customize value_to_string(), etc
    pass