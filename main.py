if __name__ == '__main__':
    import os
    import config
    from components.send_backup import send_backup
    from components.sort_backups import sort_backups
    from utils import utils
    from utils.run_system_cmd import run_system_cmd
    from utils.send_mail import send_mail

    utils.create_folders()
    run_system_cmd(config.COMMAND_STOP, 'stopping the application and the DBMS')
    run_system_cmd(f'cp -r {config.DATA_DIR} {config.TEMP_DIR}', 'copying the file')
    run_system_cmd(config.COMMAND_START, 'starting the application and the DBMS')

    archive_name = f'{utils.current_day}_{utils.current_month}_{utils.current_year}_{config.BACKUP_NAME}.tar.gz'
    backup_path = os.path.join(config.BACKUP_DIR, 'daily', f'{archive_name}.gpg')
    change_owner_cmd = f'chown -R {config.CLIENT_USER}:{config.CLIENT_USER} {config.TEMP_DIR}'
    make_archive_cmd = f'su - {config.CLIENT_USER} -c "cd {config.TEMP_DIR} && tar -zcvf {archive_name} *"'
    make_pgp_cmd = f'gpg -e -r {config.CLIENT_USER} {archive_name}'
    copy_cmd = f'cp {config.TEMP_DIR}/{archive_name}.gpg {backup_path}'
    clean_cmd = f'rm -rf {config.TEMP_DIR}/*'
    create_gpg_cmd = f'su - {config.CLIENT_USER} -c "cd {config.TEMP_DIR} && {make_pgp_cmd} && {copy_cmd}" && {clean_cmd}'

    run_system_cmd(change_owner_cmd, 'changing the owner of the temp directory')
    run_system_cmd(make_archive_cmd, 'creating the archive')
    run_system_cmd(create_gpg_cmd, 'encrypting the archive')

    if config.SEND_BACKUP:
        send_backup(backup_path, f'{archive_name}.gpg')
    elif config.SEND_FINAL_EMAIL:
        send_mail(config.MAIL_BODY, 'success')

    sort_backups(backup_path)
