import logging

# IV. Advanced configration

# Programmers can configure logging in three ways:
# 1. Creating loggers, handlers, and formatters explicitly using Python code that calls the configuration methods listed above.
# 2. Creating a logging config file and reading it using the fileConfig() function.
# 3. Creating a dictionary of configuration information and passing it to the dictConfig() function.


# 1 - Programatically
# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

# 2. Using a confguration file

import logging.config

# create configuration
logging.config.fileConfig('logging.properties')

# create logger
logger = logging.getLogger('simpleExamplePROPS')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')


# 3. Usiging dictionary - it can come from file/socket/creaed_here/...

import yaml

# create configuration
logging.config.dictConfig(yaml.load(open('logging.yaml', 'r')))

# # create logger
logger = logging.getLogger('simpleExampleYAML')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
