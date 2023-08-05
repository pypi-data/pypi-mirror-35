"""
Interface for the gingerfy package. Exposes one interface method fix.
"""
from .src.gingerfier import Gingerfier
from .src.gingerfied import Gingerfied

def fix(string: str) -> Gingerfied:
    """Fix the broken string / sentence and return a Gingerfied object."""

    gingerfier = Gingerfier()

    return gingerfier.fix(string)
