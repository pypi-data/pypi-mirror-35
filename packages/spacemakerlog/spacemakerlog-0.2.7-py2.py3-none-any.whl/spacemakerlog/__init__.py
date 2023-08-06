import os
import log
import logging

log.set_level(os.getenv('LOG_LEVEL', 'debug'))
log.set_format(os.getenv('LOG_FORMAT', 'json'))

# for "known" external loggers set a default log level of warn
# we do this because we want our default application log level to be "debug"
# but if we set this - then external libs will write a lot of lines and create clutter.
# this was found to be the most pragmatic way for now

known_external_loggers = [
    'boto',
    'boto3',
    'requests',
    'urllib',
    'urllib3',
    'rasterio',
    'gdal',
    'shapely',
    'pymunk',
    'numpy',
    'scipy',
    'flask',
    'marshmallow',
    'pandas',
    'matplotlib',
    'nose',
    'gunicorn',
    'jsonschema',
    'ortools',
    'triangle',
    'enum',
    'enum34',
    'python-jose',
    'pyasn1',
    'h5py',
    'future',
    'pyproj',
    's3transfer',
    'networkx',
    'cython',
    'overpy',
    'opencv-python'
]

for kel in known_external_loggers:
    logging.getLogger(kel).setLevel(logging.WARN)

log.set_level_external('warn')
