import ee
import pytest

import openet.ndvi as ndvi

test_geom = ee.Geometry.Rectangle([0, 0, 10, 10], 'EPSG:32613', False)


def test_NDVI_init():
    """Test that the class can be initialized from an NDVI image"""
    ndvi_img = ee.Image.constant([0.5]).rename(['ndvi']).setMulti({
        'system:time_start': ee.Date('2017-07-01').millis(),
        'system:index': 'test',
    })
    output = ndvi.NDVI(ndvi_img)
    assert output


# def test_NDVI_properties():
#     """Test that the class properties"""


# def test_NDVI_from_landsat_toa():
#     assert False


# def test_NDVI_from_sentinel2_toa():
#     assert False


# def test_NDVI_etf():
#     assert False


# Intentionally using the parameterize decorator to demonstrate the approach
# @pytest.mark.parametrize(
#     'red,nir,expected',
#     [
#         [0.2, 0.7, 0.5 / 0.9]
#     ]
# )
# def test_NDVI_ndvi(red, nir, expected):
#     """Test that NDVI is being computed correctly using constant images"""
#     toa_image = ee.Image.constant([red, nir]).rename(['red', 'nir'])
#     output = ndviee.ndviee.NDVI()\
#         ._ndvi(toa_image)\
#         .reduceRegion(ee.Reducer.first(), geometry=test_geom, scale=1)\
#         .getInfo()['ndvi']
#     assert float(output) == pytest.approx(expected, abs=diff)
