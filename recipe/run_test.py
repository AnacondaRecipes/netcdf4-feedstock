import netCDF4
import os
import tempfile
import urllib.request

# libnetcdf needs to be able to write a cookie file to $TEMP so set it to $PREFIX
os.environ['TEMP'] = os.environ['PREFIX']

# (tkoch) we don't have OPeNDAP support enabled, which is needed for working
#         with URLs directly.
#
#url = 'http://geoport-dev.whoi.edu/thredds/dodsC/estofs/atlantic'
#with netCDF4.Dataset(url) as nc:
#    # Compiled with cython.
#    assert nc.filepath() == url

url = 'https://geoport.whoi.edu/thredds/fileServer/usgs/vault0/models/tides/vdatum_gulf_of_maine/adcirc54_38_orig.nc'

with tempfile.TemporaryDirectory() as tmpdir:
    ncfile = os.path.join(tmpdir, url.rsplit('/', 1)[-1])

    with open(ncfile, "wb+") as f, urllib.request.urlopen(url) as response:
        for chunk in iter(lambda: response.read(8192), b""):
            f.write(chunk)

    with netCDF4.Dataset(ncfile) as nc:
        nc['tidenames'][:]
