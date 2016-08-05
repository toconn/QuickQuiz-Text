from ua.core.entities.appinfo import AppInfo

APP_NAME = 'FlashCards'

APP_VERSION      = '1.0.4'
APP_BUILD_DATE   = '2016-07-29'
APP_BUILD_NUMBER = '5'
APP_CREATED_DATE = '2016-05-03'

APP_INFO = AppInfo(APP_NAME, APP_VERSION, APP_BUILD_DATE, APP_BUILD_NUMBER, APP_CREATED_DATE)

HELP_USAGE = APP_INFO.name + ' [-h] [-p] [-v] deck_path [ deck_path... ]'
