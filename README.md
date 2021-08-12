<h1 align="center">Linux backup script</h1>

## Description

**This script is used to create backups and send them to a remote server. Locally, the script stores daily, weekly, monthly and annual copies. All data is archived and encrypted. In case of an error, it will be written to the `logs` file and sent a letter to the email. The script is far from perfect, and is constantly improving.**


## Project setup

### 1. Linux machine preparation

**1.1. The `gpg` utility is used for encryption. First you need to create private and public keys to encrypt and decrypt the archive.**
```shell
gpg --full-generate-key
gpg --list-keys
```
**1.1.1. If you need to decrypt the archive on another machine, then you need to export the private key.**

***public key***
```shell
gpg --export -a your_user
```

***private key***
```shell
gpg --export-secret-key -a your_user
```

**1.1.2. On the machine where decryption will take place, you need to import the private key.**
```shell
gpg --import private.key
```

**1.2. Decrypt the archive.**
```shell
gpg -d your_file.tar.gz.gpg | tar -xvz
```

**1.3. Sending backups to a remote server.**

**1.3.1. To send backups to a remote server, `ssshfs` is used, then you need to install `sshfs` package.**
```shell
sudo apt install sshfs
```

**1.3.2. You need to create SSH keys.**
```shell
ssh-keygen
ssh-copy-id username@remote_host
```

**1.3.3. On the remote server, you need to configure access using the SSH key, create a directory and assign write rights.**

**1.3.4. On the local machine, you need to create a directory to mount the server directory (`sshfs`).**
```shell
mkdir ~/server
```

### 2. Creating virtual environment variables.

**First you need to go to the project folder and create `setenv.sh` file. Next you need to create the following variables in the file.**
```shell
cd backup_script
nano setenv.sh
```

```shell
export MAIL_TO= # Mail recipient
export MAIL_SMTP= # Mail sender server smtp URL
export MAIL_PORT= # Mail sender server smtp port
export MAIL_USER= # Mail sender server username
export MAIL_PASSWORD= # Mail sender server password

export BACKUP_SERVER_HOST= # Remoute backup server host
export BACKUP_SERVER_PORT= # Remoute backup server port
export BACKUP_SERVER_USER= # Remoute backup server username

export CLIENT_USER= # Client user
export DATA_DIR= # Directory to save
export BACKUP_NAME= # Backup name

export COMMAND_STOP= # Command for stop the application and the DBMS
export COMMAND_START= # Command for start the DBMS and the application
```

```shell
sudo chmod +x setenv.sh
```

### 3. Application configuration.

**Next you need to edit the `config.py` file. In this file, change the following variables.**

* MAIL_BODY = Body of the email
* BACKUP_MOUNT_CLIENT_PATH = The path to where the backups are stored on the server
* BACKUP_MOUNT_SERVER_PATH = Path to local mount point
* BASE_DIR = Backup storage directory
* TEMP_DIR = Temp directory
* DAILY_DIR = Directory for storing daily backups
* WEEKLY_DIR = Directory for storing weekly backups
* MONTHLY_DIR = Directory for storing monthly backups
* ANNUALLY_DIR = Directory for storing annually backups
* DAILY_BACKUPS_COUNT = The number of daily backups stored
* WEEKLY_BACKUPS_COUNT = The number of weekly backups stored
* MONTHLY_BACKUPS_COUNT = The number of monthly backups stored
* ANNUALLY_BACKUPS_COUNT = The number of annually backups stored
* SEND_BACKUP = If you want to send backups to a remote server set the value to `True` otherwise `False`
* SEND_EMAIL = If you want to send an email set the value to `True` otherwise `False`
* SEND_FINALY_EMAIL = If you want to send an success email set the value to `True` otherwise `False`

### 4. Run the application.

**4.1. If your command to stop the application requires permissions then the script must be run from the `root` user.**
```shell
sudo ./run.sh
```

**4.2. For autorun you need to use the cron.**
```shell
sudo crontab -e
```

**For example, the following command will run the script every day at 00:10 am.**
```shell
10 0 * * * . /your_path/backup_script/setenv.sh && /usr/bin/python3 /your_path/backup_script/main.py
```
