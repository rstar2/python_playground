
from os import path


# import localy develoved module
import forecaster_simple

forecaster_simple.main()

# --------------------------------
# import localy develoved package
import forecaster

forecaster.main()

# ------------------------------
# access it's attached package data:

# 1. Usging the __file__
forecaster_dir = path.dirname(forecaster.__file__)
forecaster_package_data = open(path.join(forecaster_dir, 'package_data.dat')).read()

print(forecaster_package_data)

# 2. Using the ResourceManagerAPI

# prefer resource_string and resource_stream to resource_filename
from pkg_resources import resource_string, resource_stream, resource_filename, Requirement

forecaster_package_data2 = resource_string(forecaster.__name__, 'package_data.dat')
# this will get the actual package data filename path
forecaster_package_data_filename = resource_filename(Requirement.parse("Forecaster"), "package_data.dat")

print(forecaster_package_data2)
print(forecaster_package_data_filename)


print("ok")