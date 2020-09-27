from os import getenv

DEBUG = getenv('DEBUG', '').lower() == 'true'

ENVIRONMENT_PRODUCTION = 'production'
ENVIRONMENT_STAGING = 'staging'
ENVIRONMENT_LOCAL = 'local'
ENVIRONMENT_CI = 'ci'
ENVIRONMENT = getenv('ENVIRONMENT', ENVIRONMENT_LOCAL)
