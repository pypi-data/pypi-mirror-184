from lamindb import __version__ as lamindb_v
from packaging import version

if version.parse(lamindb_v) != version.parse("0.19.4"):
    raise RuntimeError("lndb_rest needs lamindb==0.19.4")
