import config
import datetime
from components.delete_old_backups import delete_old_backups
from utils import utils
from utils.run_system_cmd import run_system_cmd


def sort_backups(path):
    # Weekly sort
    if utils.current_weekday == 0:
        run_system_cmd(f'cp {path} {config.WEEKLY_DIR}', 'copying the weekly backup')

    # Monthly sort
    if utils.current_day == 1:
        run_system_cmd(f'cp {path} {config.MONTHLY_DIR}', 'copying the monthly backup')

    # Annually sort
    if utils.current_day == 1 and utils.current_month == 1:
        run_system_cmd(f'cp {path} {config.ANNUALLY_DIR}', 'copying the annually backup')

    delete_old_backups(config.DAILY_DIR, config.DAILY_BACKUPS_COUNT, datetime.timedelta(days=7))
    delete_old_backups(config.WEEKLY_DIR, config.WEEKLY_BACKUPS_COUNT, datetime.timedelta(days=30))
    delete_old_backups(config.MONTHLY_DIR, config.MONTHLY_BACKUPS_COUNT, datetime.timedelta(days=365))
    delete_old_backups(config.ANNUALLY_DIR, config.ANNUALLY_BACKUPS_COUNT, datetime.timedelta(days=365 * 3))
