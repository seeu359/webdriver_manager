import os
import shutil

import pytest

from webdriver_manager.core.constants import DEFAULT_PROJECT_ROOT_CACHE_PATH, DEFAULT_USER_HOME_CACHE_PATH
from webdriver_manager.core.logger import log


@pytest.fixture()
def delete_drivers_dir():
    if os.path.exists(DEFAULT_USER_HOME_CACHE_PATH):
        log(f"Delete {DEFAULT_USER_HOME_CACHE_PATH} folder")
        shutil.rmtree(DEFAULT_USER_HOME_CACHE_PATH)
    if os.path.exists(DEFAULT_PROJECT_ROOT_CACHE_PATH):
        log(f"Delete {DEFAULT_PROJECT_ROOT_CACHE_PATH} folder")
        shutil.rmtree(DEFAULT_PROJECT_ROOT_CACHE_PATH)


@pytest.fixture(scope='function')
def ssl_verify_enable():
    yield
    os.environ['WDM_SSL_VERIFY'] = ''