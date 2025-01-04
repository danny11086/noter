## APPlication settings
APP_NAME = "Noter"
APP_VERSION = "0.1.0"
APP_DESCRIPTION = "Noter - 现代化的笔记应用"

## Database settings
DB_NAME = "noter.db"
DB_PATH = "db"

## API settings
API_HOST = "0.0.0.0"
API_PORT = 5000
API_DEBUG = True

## Logging settings
LOG_LEVEL = "INFO"
LOG_PATH = "logs"
LOG_FILE = "noter.log"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
LOG_MAX_BYTES = 1024 * 1024 * 5  # 5MB
LOG_BACKUP_COUNT = 5
LOG_FILE_MODE = "a"  # append mode
LOG_FILE_ENCODING = "utf-8"
LOG_FILE_DELAY = False

## Security settings
SECRET_KEY = "noter_secret_key"
SECURITY_PASSWORD_SALT = "noter_password_salt"
SECURITY_PASSWORD_HASH = "bcrypt"
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = True
SECURITY_TRACKABLE = True
SECURITY_CHANGEABLE = True
SECURITY_SEND_REGISTER_EMAIL = True
SECURITY_SEND_PASSWORD_CHANGE_EMAIL = True


