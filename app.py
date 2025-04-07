from signLanguageDetection.logger import logging
from signLanguageDetection.exception import AppException
import sys

try:
    a = 3/"s"
    
except Exception as e:
    raise AppException(e, sys)