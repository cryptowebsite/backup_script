import os
import config
import datetime
import subprocess
from utils.send_mail import send_mail

now = datetime.datetime.now()
current_time = now.strftime('%Y-%m-%d %H:%M:%S')
current_day = now.day
current_weekday = now.weekday()
current_month = now.month
current_year = now.year


def write_log(log):
    logs = os.path.join(config.BASE_DIR, 'logs')
    cmd = f'echo {current_time} {log} >> {logs}'
    subprocess.call(f'su - {config.CLIENT_USER} -c "{cmd}"', shell=True)


def create_folders():
    dirs = [
        config.TEMP_DIR,
        config.BACKUP_DIR,
        config.DAILY_DIR,
        config.WEEKLY_DIR,
        config.MONTHLY_DIR,
        config.ANNUALLY_DIR
    ]

    def make_error(err):
        message = f'An error occurred while {err}'
        write_log(message)
        send_mail(message, 'error')

    for directory in dirs:
        if subprocess.call(f'mkdir -p {directory}', shell=True) != 0:
            make_error('creating directories')

        if subprocess.call(f'chmod 700 {directory}', shell=True) != 0:
            make_error('changing the permissions of directories')

        if subprocess.call(f'chown -R {config.CLIENT_USER}:{config.CLIENT_USER} {directory}', shell=True) != 0:
            make_error('changing the owner of directories')


def get_md5_from_file(file):
    cmd = f'su - {config.CLIENT_USER} -c "md5sum {file}"'
    if subprocess.call(cmd, shell=True) == 0:
        res = str(subprocess.check_output(cmd, shell=True))
        return res.split(' ')[0]
    else:
        msg = 'An error occurred while getting the MD5'
        write_log(msg)
        send_mail(msg, 'error')
