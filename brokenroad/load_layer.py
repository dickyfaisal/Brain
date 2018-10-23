import os
from django.contrib.gis.utils import LayerMapping
from .models import Desa

desa_mapping = {
    'desa' : 'DESA',
    'kecamatan' : 'KECAMATAN',
    'kabupaten' : 'KABUPATEN',
    'propinsi' : 'PROPINSI',
    'geom' : 'MULTIPOLYGON25D',
}

desa_shp = os.path .abspath(os.path.join(os.path.dirname(__file__),'spatial_data/spatial_data.shp'))

def run(verbose=True):
    lm = LayerMapping(Desa, desa_shp, desa_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)
