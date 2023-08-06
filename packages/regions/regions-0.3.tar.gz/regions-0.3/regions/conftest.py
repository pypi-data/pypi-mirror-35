# this contains imports plugins that configure py.test for astropy tests.
# by importing them here in conftest.py they are discoverable by py.test
# no matter how it is invoked within the source tree.

try:
    import pytest_arraydiff
except ImportError:
    raise ImportError("The pytest-arraydiff package is required for the tests. "
                      "You can install it with: pip install pytest-arraydiff")
else:
    # We need to remove pytest_arraydiff from the namespace otherwise pytest
    # gets confused, because it tries to interpret pytest_* as a special
    # function name.
    del pytest_arraydiff

from astropy.tests.pytest_plugins import *    # noqa

# Uncomment the following line to treat all DeprecationWarnings as
# exceptions
# enable_deprecations_as_exceptions()    # noqa

# Uncomment and customize the following lines to add/remove entries from
# the list of packages for which version numbers are displayed when running
# the tests. Making it pass for KeyError is essential in some cases when
# the package uses other astropy affiliated packages.
try:
    PYTEST_HEADER_MODULES['Cython'] = 'Cython'    # noqa
    PYTEST_HEADER_MODULES['Astropy'] = 'astropy'    # noqa
    PYTEST_HEADER_MODULES['Astropy-healpix'] = 'astropy_healpix'    # noqa
    del PYTEST_HEADER_MODULES['h5py']    # noqa
    del PYTEST_HEADER_MODULES['Pandas']    # noqa
except (NameError, KeyError):  # NameError is needed to support Astropy < 1.0
    pass

# Uncomment the following lines to display the version number of the
# package rather than the version number of Astropy in the top line when
# running the tests.
import os

# This is to figure out the affiliated package version, rather than
# using Astropy's
try:
    from .version import version
except ImportError:
    version = 'dev'

try:
    packagename = os.path.basename(os.path.dirname(__file__))
    TESTED_VERSIONS[packagename] = version    # noqa
except NameError:   # Needed to support Astropy <= 1.0.0
    pass
