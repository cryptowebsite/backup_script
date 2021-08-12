from utils.run_system_cmd import run_system_cmd
from utils import utils
import datetime
import os


def delete_old_backups(path, backup_count, required_expiration_time):
    backups_list = os.listdir(path)

    if len(backups_list) > backup_count:
        for backup_archive in backups_list:
            backup_archive_path = os.path.join(path, backup_archive)
            backup_create_time = datetime.datetime.fromtimestamp(os.path.getmtime(backup_archive_path))
            archive_age = (utils.now + datetime.timedelta(seconds=60)) - backup_create_time

            if archive_age >= required_expiration_time:
                run_system_cmd(f'rm {backup_archive_path}', 'deleting backups')
