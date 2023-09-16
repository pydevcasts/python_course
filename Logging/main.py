
import logging.config
from project.index import Pesrson

logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)

class Main():
    pesron = Pesrson("siyamak")
    pesron.delete_name()
    

if __name__=="__main__":
    logger = logging.getLogger(__name__)
    logger.info("hello")
    Main()