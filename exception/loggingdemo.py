import logging


logging.basicConfig(filename="mylog.log",level=logging.CRITICAL)
logging.critical("Critical")
logging.error("Error")
logging.warn("Warinig")
logging.info("Info")
logging.debug("Debug")