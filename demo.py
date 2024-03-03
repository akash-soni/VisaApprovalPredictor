from us_visa.logger import logging
from us_visa.exception import USvisaException
from us_visa.constants import *
import sys
from us_visa.pipline.training_pipeline import TrainPipeline

#logging.info("Welcome to our custom log")

# try:
#     a = 1 / "10"
# except Exception as e:
#     raise USViaException(e, sys) from e


pipeline = TrainPipeline()
pipeline.run_pipeline()
