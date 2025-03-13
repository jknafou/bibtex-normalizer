__version__ = "1.0.0"
__all__ = ['process_bibtex_file']

from .processor import process_bibtex_file
from .capitalizer import DEFAULT_EXCLUDED_WORDS

import logging
logging.basicConfig(format='%(levelname)s: %(message)s')