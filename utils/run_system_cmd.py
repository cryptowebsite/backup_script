import subprocess
import config
from utils.utils import write_log
from utils.send_mail import send_mail


def run_system_cmd(cmd, desc):
    if subprocess.call(cmd, shell=True) != 0:
        subprocess.call(config.COMMAND_START, shell=True)
        msg = f'An error occurred while {desc}'
        send_mail(msg, 'error')
        write_log(msg)
        raise SystemExit(1)
