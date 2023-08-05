from . import _version
from .drb_signature_magic import MagicSignature

__version__ = _version.get_versions()['version']
__all__ = ['MagicSignature']
