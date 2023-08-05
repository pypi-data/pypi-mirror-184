"""Setup ScanHub."""

import sys

import os
import os.path as op

from setuptools import setup

# Give setuptools a hint to complain if it's too old a version
# 30.3.0 allows us to put most metadata in setup.cfg
# 38.3.0 contains most setup.cfg bugfixes
# Should match pyproject.toml
SETUP_REQUIRES = ["setuptools >= 38.3.0"]
# This enables setuptools to install wheel on-the-fly
SETUP_REQUIRES += ["wheel"] if "bdist_wheel" in sys.argv else []

# get the version (don't import mne here, so dependencies are not needed)
version = None
with open(op.join('scanhub', '_version.py'), 'r') as fid:
    for line in (line.strip() for line in fid):
        if line.startswith('__version__'):
            version = line.split('=')[1].strip().strip('\'')
            break
if version is None:
    raise RuntimeError('Could not determine version')


descr = """ScanHub Tools"""

DISTNAME = 'scanhub'
DESCRIPTION = descr
MAINTAINER = 'Christoph Dinh'
MAINTAINER_EMAIL = 'christoph.dinh@brain-link.de'
URL = 'https://github.com/brain-link/scanhub_tools'
LICENSE = 'BSD-licenced (3 clause)'
DOWNLOAD_URL = 'https://github.com/brain-link/scanhub_tools'
VERSION = version


def package_tree(pkgroot):
    """Get the submodule list."""
    # Adapted from VisPy
    path = op.dirname(__file__)
    subdirs = [op.relpath(i[0], path).replace(op.sep, '.')
               for i in os.walk(op.join(path, pkgroot))
               if '__init__.py' in i[2]]
    return sorted(subdirs)


if __name__ == "__main__":
    if op.exists('MANIFEST'):
        os.remove('MANIFEST')

    with open('README.rst', 'r') as fid:
        long_description = fid.read()

    install_requires = list()
    with open('requirements.txt', 'r') as fid:
        for line in fid:
            req = line.strip()
            install_requires.append(req)
            
    setup(name=DISTNAME,
          maintainer=MAINTAINER,
          include_package_data=True,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          long_description=long_description,
          long_description_content_type='text/x-rst',
          zip_safe=False,  # the package can run out of an .egg file
          classifiers=['Intended Audience :: Science/Research',
                       'Intended Audience :: Developers',
                       'License :: OSI Approved :: BSD License',
                       'Topic :: Scientific/Engineering',
                       'Programming Language :: Python :: 3',
                       'Development Status :: 1 - Planning',
                       'Operating System :: OS Independent',
                       ],
        keywords='ScanHub MRI MEG EEG',
        project_urls={
        'Source': 'https://github.com/brain-link/scanhub_tools/',
        'Tracker': 'https://github.com/brain-link/scanhub_tools/issues/',
        },
        platforms='any',
        python_requires='>=3.7',
        install_requires=install_requires,
        setup_requires=SETUP_REQUIRES,
        packages=package_tree('scanhub'))