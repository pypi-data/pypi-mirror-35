import ee

# TODO: Make this a class eventually
def collection(
        variable,
        collections,
        start_date,
        end_date,
        t_interval,
        geometry,
        **kwargs
        ):
    """Generic OpenET Collection

    Parameters
    ----------
    self :
    variable : str
        Variable to compute.
    collections : list
        GEE satellite image collection IDs.
    start_date : str
        ISO format inclusive start date (i.e. YYYY-MM-DD).
    end_date : str
        ISO format exclusive end date (i.e. YYYY-MM-DD).
    t_interval : {'daily', 'monthly', 'annual', 'overpass'}
        Time interval over which to interpolate and aggregate values.
        Selecting 'overpass' will return values only for the overpass dates.
    geometry : ee.Geometry
        The geometry object will be used to filter the input collections.
    kwargs :

    Returns
    -------
    ee.ImageCollection

    """

    # CGM - Make this a global or collection property?
    landsat_c1_toa_collections = [
        'LANDSAT/LC08/C01/T1_RT_TOA',
        'LANDSAT/LE07/C01/T1_RT_TOA',
        'LANDSAT/LC08/C01/T1_TOA',
        'LANDSAT/LE07/C01/T1_TOA',
        'LANDSAT/LT05/C01/T1_TOA',
    ]
    sentinel2_toa_collections = [
        'COPERNICUS/S2',
    ]

    # TODO: Test whether the requested variable is supported

    # Build the variable image collection
    variable_coll = ee.ImageCollection([])
    for coll_id in collections:
        if coll_id in landsat_c1_toa_collections:
            def compute(image):
                model_obj = NDVI.from_landsat_c1_toa(
                    toa_image=ee.Image(image))
                return ee.Image(model_obj.get_variable(variable))
        elif coll_id in sentinel2_toa_collections:
            def compute(image):
                model_obj = NDVI.from_sentinel2_toa(
                    toa_image=ee.Image(image))
                return ee.Image(model_obj.get_variable(variable))
        else:
            raise ValueError('unsupported collection: {}'.format(coll_id))

        var_coll = ee.ImageCollection(coll_id)\
            .filterDate(start_date, end_date)\
            .filterBounds(geometry)\
            .map(compute)

        # TODO: Allow additional filter parameters (like CLOUD_COVER_LAND for Landsat)
        # .filterMetadata() \

        variable_coll = variable_coll.merge(var_coll)

    # TODO: Add interpolation component

    # Interpolate/aggregate to t_interval
    # Should this only be allowed for specific variables (ETf, ETa)?
    # We would need a daily reference collection to get to ET
    # output_coll = openet.interp.interpolate(variable_coll)

    return variable_coll


class NDVI():
    """GEE based model for computing ETf as a linear function of NDVI"""

    def __init__(
            self,
            image,
            m=1.25,
            b=0.0,
            **kwargs
            ):
        """Initialize an NDVI_ET object.

        Parameters
        ----------
        image : ee.Image
            Must have bands: "ndvi"
        m : float, optional
            Slope (the default is 1.25).
        b : float, optional
            Offset (the default is 0.0).
        kwargs :

        Notes
        -----
        ETf = m * NDVI + b

        """
        input_image = ee.Image(image)
        self.ndvi = input_image.select(['ndvi'])
        self._m = m
        self._b = b

        # Copy system properties
        self.index = input_image.get('system:index')
        self.time_start = input_image.get('system:time_start')

    def get_variable(self, variable):
        if variable == 'etf':
            return self.etf()
        # CGM - Returning ET requires ETr to be passed in (maybe via kwargs)
        # elif variable == 'et':
        #     return self.et()
        elif variable == 'ndvi':
            return self.ndvi

    def etf(self):
        """Compute ETf"""
        etf = ee.Image(self.ndvi) \
            .multiply(self._m).add(self._b) \
            .setMulti({
                'system:index': self.index,
                'system:time_start': self.time_start})
        return ee.Image(etf).rename(['etf'])

    @classmethod
    def from_landsat_c1_toa(cls, toa_image, **kwargs):
        """Constructs an NDVI_ET object from a Landsat TOA image

        Parameters
        ----------
        toa_image : ee.Image

        Returns
        -------
        NDVI_ET

        """
        # Use the SPACECRAFT_ID property identify each Landsat type
        spacecraft_id = ee.String(ee.Image(toa_image).get('SPACECRAFT_ID'))

        # Rename bands to generic names
        input_bands = ee.Dictionary({
            'LANDSAT_5': ['B1', 'B2', 'B3', 'B4', 'B5', 'B7', 'B6', 'BQA'],
            'LANDSAT_7': ['B1', 'B2', 'B3', 'B4', 'B5', 'B7', 'B6_VCID_1', 'BQA'],
            'LANDSAT_8': ['B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B10', 'BQA'],
        })
        output_bands = [
            'blue', 'green', 'red', 'nir', 'swir1', 'swir2', 'lst', 'BQA']
        prep_image = ee.Image(toa_image) \
            .select(input_bands.get(spacecraft_id), output_bands)

        # Build the input image
        # Eventually send the BQA band or a cloud mask through also
        input_image = ee.Image([
            cls._ndvi(prep_image)
        ])

        # Add properties and instantiate class
        input_image = ee.Image(input_image.setMulti({
            'system:time_start': ee.Image(toa_image).get('system:time_start')
        }))

        # Instantiate the class
        return cls(input_image, **kwargs)

    @classmethod
    def from_sentinel2_toa(cls, toa_image, **kwargs):
        """Constructs an NDVI_ET object from a Sentinel TOA image

        Parameters
        ----------
        toa_image : ee.Image

        Returns
        -------
        NDVI_ET

        """

        # Don't distinguish between Sentinel-2 A and B for now
        # Rename bands to generic names
        # Scale bands to 0-1 (from 0-10000)
        input_bands = ['B2', 'B3', 'B4', 'B8', 'B11', 'B12', 'QA60']
        output_bands = ['blue', 'green', 'red', 'nir', 'swir1', 'swir2', 'QA60']
        prep_image = ee.Image(toa_image) \
            .select(input_bands, output_bands) \
            .divide(10000.0)

        # Build the input image
        # Eventually send the BQA band or a cloud mask through also
        input_image = ee.Image([
            cls._ndvi(prep_image)
        ])

        # Add properties and instantiate class
        input_image = ee.Image(input_image.setMulti({
            'system:time_start': ee.Image(toa_image).get('system:time_start')
        }))

        # Instantiate the class
        return cls(input_image, **kwargs)

    # Why is this a staticmethod?
    @staticmethod
    def _ndvi(toa_image):
        """Compute NDVI

        Parameters
        ----------
        toa_image : ee.Image
            Renamed TOA image with 'nir' and 'red bands.

        Returns
        -------
        ee.Image

        """
        return ee.Image(toa_image).normalizedDifference(['nir', 'red']) \
            .rename(['ndvi'])
