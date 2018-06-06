import os

# *****************************
# Environment specific settings
# *****************************

# DO NOT use "DEBUG = True" in production environments
DEBUG = False
# DO NOT use Unsecure Secrets in production environments
# Generate a safe one with:
#     python -c "import os; print repr(os.urandom(24));"
SECRET_KEY = '...'

# SQLAlchemy settings
# SQLALCHEMY_DATABASE_URI = '' EX:sqlite:///../app.sqlite