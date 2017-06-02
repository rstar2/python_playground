import logging

# By default, informational and debugging messages are suppressed
# and the output is sent to standard error.
# Other output options include routing messages through email,
# datagrams, sockets, or to an HTTP Server.
# New filters can select different routing based on
# message priority: DEBUG, INFO, WARNING, ERROR, and CRITICAL.


# I. Configure the logging - basic configuration
#  filemode='w' will replace the existing 'example.log'on each start
logging.basicConfig(filename='example.log',
                    filemode='w', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# II. using the ROOT logger
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')

# The logging system can be configured directly from Python
# or can be loaded from a user editable configuration file
# for customized logging without altering the application

# ---------------
# III. Using different loggers

log = logging.getLogger("foo.bar.baz")

#  so it good to create loggers with module's name in the Python package namespace.
log = logging.getLogger(__name__)

log.warning('%s before you %s', 'Look', 'leap!')
