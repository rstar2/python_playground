import logging

# By default, informational and debugging messages are suppressed
# and the output is sent to standard error.
# Other output options include routing messages through email,
# datagrams, sockets, or to an HTTP Server.
# New filters can select different routing based on
# message priority: DEBUG, INFO, WARNING, ERROR, and CRITICAL.

logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')

# The logging system can be configured directly from Python
# or can be loaded from a user editable configuration file
# for customized logging without altering the application