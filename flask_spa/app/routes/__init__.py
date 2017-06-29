from flask import Blueprint
routes = Blueprint('routes', __name__, url_prefix="/routes")

# 1. One way to import all routes is:
# from .adder import *
# from .github import *

# 2. Second way is:
# using __all__  - it is taken to be the list of module names
# that should be imported when from package import * is encountered
# BUT then this "routes" module should not be imported  with
# from routes import *, outside
__all__ = ["adder", "github"]
from . import *
