
from __future__ import absolute_import, division, print_function, unicode_literals

import os.path

import pytest
import numpy as np

from cfgrib import cfmessage
from cfgrib import messages
from cfgrib import dataset

SAMPLE_DATA_FOLDER = os.path.join(os.path.dirname(__file__), 'sample-data')
TEST_DATA = os.path.join(SAMPLE_DATA_FOLDER, 'era5-levels-members.grib')


def test_dict_merge():
    master = {'one': 1}
    dataset.dict_merge(master, {'two': 2})
    assert master == {'one': 1, 'two': 2}
    dataset.dict_merge(master, {'two': 2})
    assert master == {'one': 1, 'two': 2}

    with pytest.raises(ValueError):
        dataset.dict_merge(master, {'two': 3})


def test_build_data_var_components_no_encode():
    index = messages.Stream(path=TEST_DATA).index(dataset.ALL_KEYS).subindex(paramId=130)
    dims, data_var, coord_vars = dataset.build_data_var_components(index=index)
    assert dims == {'number': 10, 'dataDate': 2, 'dataTime': 2, 'topLevel': 2, 'i': 7320}
    assert data_var.data.shape == (10, 2, 2, 2, 7320)

    # equivalent to not np.isnan without importing numpy
    assert data_var.data[:, :, :, :, :].mean() > 0.


def test_build_data_var_components_encode_geography():
    stream = messages.Stream(path=TEST_DATA, message_class=cfmessage.CfMessage)
    index = stream.index(dataset.ALL_KEYS).subindex(paramId=130)
    dims, data_var, coord_vars = dataset.build_data_var_components(
        index=index, encode_geography=True,
    )
    assert dims == {
        'number': 10, 'dataDate': 2, 'dataTime': 2,
        'topLevel': 2, 'latitude': 61, 'longitude': 120,
    }
    assert data_var.data.shape == (10, 2, 2, 2, 61, 120)

    # equivalent to not np.isnan without importing numpy
    assert data_var.data[:, :, :, :, :, :].mean() > 0.


def test_Dataset():
    res = dataset.Dataset.frompath(TEST_DATA)
    assert 'history' in res.attributes
    assert res.attributes['GRIB_edition'] == 1
    assert tuple(res.dimensions.keys()) == \
        ('number', 'time', 'air_pressure', 'latitude', 'longitude')
    assert len(res.variables) == 9


def test_Dataset_no_encode():
    res = dataset.Dataset.frompath(
        TEST_DATA, encode_time=False, encode_vertical=False, encode_geography=False,
    )
    assert 'history' in res.attributes
    assert res.attributes['GRIB_edition'] == 1
    assert tuple(res.dimensions.keys()) == ('number', 'dataDate', 'dataTime', 'topLevel', 'i')
    assert len(res.variables) == 9


def test_Dataset_encode_time():
    res = dataset.Dataset.frompath(TEST_DATA, encode_vertical=False, encode_geography=False)
    assert 'history' in res.attributes
    assert res.attributes['GRIB_edition'] == 1
    assert tuple(res.dimensions.keys()) == ('number', 'time', 'topLevel', 'i')
    assert len(res.variables) == 9

    # equivalent to not np.isnan without importing numpy
    assert res.variables['t'].data[:, :, :, :].mean() > 0.


def test_Dataset_encode_geography():
    res = dataset.Dataset.frompath(TEST_DATA, encode_time=False, encode_vertical=False)
    assert 'history' in res.attributes
    assert res.attributes['GRIB_edition'] == 1
    assert tuple(res.dimensions.keys()) == \
        ('number', 'dataDate', 'dataTime', 'topLevel', 'latitude', 'longitude')
    assert len(res.variables) == 9

    # equivalent to not np.isnan without importing numpy
    assert res.variables['t'].data[:, :, :, :, :, :].mean() > 0.


def test_Dataset_encode_vertical():
    res = dataset.Dataset.frompath(TEST_DATA, encode_time=False, encode_geography=False)
    assert 'history' in res.attributes
    assert res.attributes['GRIB_edition'] == 1
    assert tuple(res.dimensions.keys()) == ('number', 'dataDate', 'dataTime', 'air_pressure', 'i')
    assert len(res.variables) == 9

    # equivalent to not np.isnan without importing numpy
    assert res.variables['t'].data[:, :, :, :, :].mean() > 0.


def test_Dataset_reguler_gg_surface():
    path = os.path.join(SAMPLE_DATA_FOLDER, 'regular_gg_sfc.grib')
    res = dataset.Dataset.frompath(path)

    assert res.dimensions == {'latitude': 96, 'longitude': 192}
    assert np.allclose(res.variables['latitude'].data[:2], [88.57216851, 86.72253095])


def test_build_valid_time():
    forecast_reference_time = np.array(0)
    forecast_period = np.array(0)

    dims, data, attrs = dataset.build_valid_time(forecast_reference_time, forecast_period)

    assert dims == ()
    assert data.shape == ()

    forecast_reference_time = np.array([0, 31536000])
    forecast_period = np.array(0)

    dims, data, attrs = dataset.build_valid_time(forecast_reference_time, forecast_period)

    assert dims == ('time',)
    assert data.shape == forecast_reference_time.shape + forecast_period.shape

    forecast_reference_time = np.array(0)
    forecast_period = np.array([0, 12, 24, 36])

    dims, data, attrs = dataset.build_valid_time(forecast_reference_time, forecast_period)

    assert dims == ('step',)
    assert data.shape == (4,)
    assert np.allclose((data - data[..., :1]) / 3600, forecast_period)

    forecast_reference_time = np.array([0, 31536000])
    forecast_period = np.array([0, 12, 24, 36])

    dims, data, attrs = dataset.build_valid_time(forecast_reference_time, forecast_period)

    assert dims == ('time', 'step')
    assert data.shape == (2, 4)
    assert np.allclose((data - data[..., :1]) / 3600, forecast_period)
