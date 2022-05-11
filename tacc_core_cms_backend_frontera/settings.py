from tacc_core_cms_backend.settings import *

# Application definition
INSTALLED_APPS = [
    'tacc_core_cms_backend_frontera',
] + INSTALLED_APPS

# Import local settings
try:
    from .secrets import *
except ModuleNotFoundError:
    pass

try:
    from .settings_local import *
except ModuleNotFoundError:
    pass
