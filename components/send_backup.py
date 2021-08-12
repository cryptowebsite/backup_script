import config
from utils.send_mail import send_mail
from utils import utils
from utils.run_system_cmd import run_system_cmd


def send_backup(backup_path, backup_name):
    server_confidential_data = f'-p {config.BACKUP_SERVER_PORT} {config.BACKUP_SERVER_USER}@{config.BACKUP_SERVER_HOST}'
    server_path = config.BACKUP_MOUNT_SERVER_PATH
    mount_path = config.BACKUP_MOUNT_CLIENT_PATH
    mount_cmd = f'sshfs {server_confidential_data}:/{server_path} {mount_path}'
    copy_cmd = f'cp {backup_path} {mount_path}/{backup_name}'

    original_md5 = utils.get_md5_from_file(backup_path)
    run_system_cmd(f'su - {config.CLIENT_USER} -c "{mount_cmd}"', 'mounting the SSHFS')
    run_system_cmd(f'su - {config.CLIENT_USER} -c "{copy_cmd}"', 'coping the backup to the server')
    returned_md5 = utils.get_md5_from_file(f'{mount_path}/{backup_name}')
    run_system_cmd(f'umount {mount_path}', 'unmounting the SSHFS')

    if original_md5 == returned_md5:
        if config.SEND_FINAL_EMAIL:
            send_mail(config.MAIL_BODY, 'success')
    else:
        error_text = 'The checksums of the backups do not match'
        utils.write_log(error_text)
        send_mail(error_text, 'error')
