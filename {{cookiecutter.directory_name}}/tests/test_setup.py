import re

from specimen import __version__ as version


def test_version():
    assert re.match(r"^\d+\.\d+\.\d+$", version)
