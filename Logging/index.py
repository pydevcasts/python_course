import logging



logging.basicConfig(format="%(process)d-%(levelname)$-%(message)s")
logging.basicConfig(level=logging.WARNING, filemode="a", filename="./Logging/app.log")
 
logging.warning("this is a warning")