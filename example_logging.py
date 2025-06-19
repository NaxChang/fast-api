# example_logging.py

import logging

logger1 = logging.getLogger("nameless")
logger2 = logging.getLogger("nameless")

print(logger1 is logger2)
