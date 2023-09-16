
import logging



class Pesrson():
    def __init__(self, name):
        self.name = name
    
    def delete_name(self):
        logger = logging.getLogger(__name__)
        logger.warning(f"I want to delete {self.name}")
    