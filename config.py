import os


BACKUP_SERVER_HOST = os.getenv('BACKUP_SERVER_HOST')
BACKUP_SERVER_PORT = os.getenv('BACKUP_SERVER_PORT')
BACKUP_SERVER_USER = os.getenv('BACKUP_SERVER_USER')
CLIENT_USER = os.getenv('CLIENT_USER')

BACKUP_MOUNT_CLIENT_PATH = f'/home/{CLIENT_USER}/server'
BACKUP_MOUNT_SERVER_PATH = f'/home/{BACKUP_SERVER_USER}/backup'
BACKUP_NAME = os.getenv('BACKUP_NAME')

MAIL_TO = os.getenv('MAIL_TO')
MAIL_USER = os.getenv('MAIL_USER')
MAIL_SMTP = os.getenv('MAIL_SMTP')
MAIL_PORT = os.getenv('MAIL_PORT')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
MAIL_BODY = f'The {BACKUP_NAME} backup was successfully sent to the server'

DATA_DIR = os.getenv('DATA_DIR')
BACKUP_DIR = f'/home/{CLIENT_USER}/backup_script/backups'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_DIR = os.path.join(BASE_DIR, 'temp')
DAILY_DIR = os.path.join(BACKUP_DIR, 'daily')
WEEKLY_DIR = os.path.join(BACKUP_DIR, 'weekly')
MONTHLY_DIR = os.path.join(BACKUP_DIR, 'monthly')
ANNUALLY_DIR = os.path.join(BACKUP_DIR, 'annually')

DAILY_BACKUPS_COUNT = 7
WEEKLY_BACKUPS_COUNT = 4
MONTHLY_BACKUPS_COUNT = 12
ANNUALLY_BACKUPS_COUNT = 3

COMMAND_STOP = os.getenv('COMMAND_STOP')
COMMAND_START = os.getenv('COMMAND_START')

SEND_BACKUP = True
SEND_EMAIL = True
SEND_FINAL_EMAIL = False
