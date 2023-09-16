import logging


# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')



# logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
# logging.critical('This is a Warning')
# =============================================================
# logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
# logging.warning('This will get logged to a file')

# =============================================================
# logging.basicConfig(filename='foo.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
# logging.info('Admin logged in')
# =============================================================
# logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%Y %H:%M:%S', level=logging.INFO)
# logging.info('Admin logged out')

# ============================================================
# name = 'siyamak'
# logging.basicConfig(filename="foo.log", format='%(asctime)s - %(message)s', datefmt='%d-%b-%Y %H:%M:%S')

# logging.error('%s raised an error', name)
# =================================================================
# a = 5
# b = 0

# try:
#   c = a / b
# except Exception as e:
#     logging.basicConfig(filemode='a', filename='app.log', format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d')
#     logging.error("Exception occurred", exc_info=False)
# ===================================================================
# import logging

# a = 5
# b = 0
# try:
#   c = a / b
# except Exception as e:
#   logging.exception("Exception occurred")
# =======================================================================
# logger = logging.getLogger('example_logger')
# logging.basicConfig(filemode='a', filename='app.log', format='%(asctime)s - %(name)s - %(message)s', datefmt='%Y-%m-%d')
# logger.warning('This is a warning')

# =======================================================================

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')

# Create formatters and add it to handlers
c_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
f_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)


logger.warning('This is a warning')
logger.error('This is an error')

# این نامی است که پایتون به ماژولی اختصاص می‌دهد که در آن اجرا شروع شده بود
# =================================================================================

# import logging.config

# logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)

# # Get the logger specified in the file
# logger = logging.getLogger(__name__)

# logger.debug('This is a debug message')
# ==============================================================================
# import logging
# import logging.config
# import yaml

# with open('config.yaml', 'r') as f:
#     config = yaml.safe_load(f.read())
#     logging.config.dictConfig(config)

# logger = logging.getLogger(__name__)

# logger.debug('This is a debug message')
# ===================================================================
