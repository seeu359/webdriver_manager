from webdriver_manager.core.constants import GH_TOKEN
from webdriver_manager.core.logger import log


class Driver(object):
    def __init__(
            self,
            name,
            version,
            os_type,
            url,
            latest_release_url,
            http_client):
        self._name = name
        self._url = url
        self._version = version
        self._os_type = os_type
        self._latest_release_url = latest_release_url
        self._http_client = http_client

    @property
    def auth_header(self):
        gh_token = GH_TOKEN
        if gh_token:
            log("GH_TOKEN will be used to perform requests")
            return {"Authorization": f"token {gh_token}"}

    def get_name(self):
        return self._name

    def get_os_type(self):
        return self._os_type

    def get_url(self):
        return f"{self._url}/{self.get_version()}/{self.get_name()}_{self.get_os_type()}.zip"

    def get_version(self):
        self._version = (
            self.get_latest_release_version()
            if self._version == "latest"
            else self._version
        )
        return self._version

    def get_latest_release_version(self):
        # type: () -> str
        raise NotImplementedError("Please implement this method")