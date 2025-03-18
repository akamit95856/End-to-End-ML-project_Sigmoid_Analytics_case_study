from ML_Project_Sigmoid_Analytics.logger import logging
from ML_Project_Sigmoid_Analytics.exception import CustomException
import sys


logging.info("welcome to our custom log")

try:
    a=2/0
except Exception as e:
    raise CustomException(e,sys)