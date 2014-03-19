#!/usr/bin/env python
from distutils.core import setup

DISTNAME = 'tract_querier'
DESCRIPTION = \
    'WMQL: Query language for automatic tract extraction from '\
    'full-brain tractographies with '\
    'a registered template on top of them'
LONG_DESCRIPTION = open('README.md').read()
MAINTAINER = 'Demian Wassermann'
MAINTAINER_EMAIL = 'demian@bwh.harvard.edu'
URL = 'http://demianw.github.io/tract_querier'
LICENSE = open('license.rst').read()
DOWNLOAD_URL = 'https://github.com/demianw/tract_querier'
VERSION = '0.1'


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)
    config.set_options(quiet=True)
    config.add_subpackage('tract_querier')
    return config


if __name__ == "__main__":
    requires_base = open('requirements.txt').readlines()
    requires = []
    for i, req in enumerate(requires_base):
        if req.strip().startswith('#') or req.strip().startswith('-'):
            continue
        req = req.strip()
        if '>' in req:
            req = req.replace('>', '(>')
            req += ')'
        requires.append(req)

    setup(
        name=DISTNAME,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        license=LICENSE,
        url=URL,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        long_description=LONG_DESCRIPTION,
        requires=requires,
        classifiers=[
            'Intended Audience :: Science/Research',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'Operating System :: Unix',
            'Operating System :: MacOS'
        ],
        scripts=[
            'scripts/tract_querier',
            'scripts/tract_math',
            'scripts/sliced_probmap_viz',
        ],
        **(configuration().todict())
    )
