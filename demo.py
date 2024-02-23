from us_visa.logger import logging
from us_visa.exception import USViaException
import sys

#logging.info("Welcome to our custom log")

try:
    a = 1 / "10"
except Exception as e:
    raise USViaException(e, sys) from e

