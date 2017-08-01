# The configuration files themselves are actual Python files.
# Only values in uppercase are actually stored in the config object later on.
# So make sure to use uppercase letters for your config keys.

import os

class BaseConfig:
    DEBUG = True

    # Define the application directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

    DATABASE = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    DATABASE_CONNECT_OPTIONS = {}

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = "secret"

    # Secret key for signing cookies
    SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

    # Good way to generate a secret key - Copy/Paste the generated string
    # $ import os
    # $ os.urandom(24)

    # Flask Debug Toolbar configuration
    # https://flask-debugtoolbar.readthedocs.io/en/latest/#configuration
    # Enable the toolbar? (app.debug)
    DEBUG_TB_ENABLED = True
    # Whitelist of hosts to display toolbar (any host)
    # Should intercept redirects? (True)
    # DEBUG_TB_INTERCEPT_REDIRECTS =
    # List of module/class names of panels (enable all built-in panels)
    # DEBUG_TB_PANELS =
    # Enable the profiler on all requests (False, user-enabled)
    # DEBUG_TB_PROFILER_ENABLED =
    # Enable the template editor (False)
    # DEBUG_TB_TEMPLATE_EDITOR_ENABLED = 


class VSCDebugConfig(BaseConfig):
    # Keep it False if debugging in VSC is needed
    DEBUG = False
