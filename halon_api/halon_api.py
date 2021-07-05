import requests
from requests.models import HTTPError


class HalonAPI:
    def __init__(
        self,
        url,
        user,
        password,
        version="5.6.0",
        cert=None,
        verify_cert=True,
    ) -> None:
        self.base_url = f"{url}/api/{version}"
        self.auth = requests.auth.HTTPBasicAuth(user, password)
        self.cert = cert
        self.verify_cert = verify_cert
        # The session to use for all requests (HTTP pooling)
        # self.session = requests.Session()
        self.headers = {}

        # Don't warn about cert not being verified if user disabled verification
        if not verify_cert:
            requests.urllib3.disable_warnings(
                requests.urllib3.exceptions.InsecureRequestWarning
            )

    def _request(self, method, path, payload={}, params={}) -> dict:
        """Perform a get request"""

        try:
            r = requests.request(
                method=method,
                url=self.base_url + path,
                auth=self.auth,
                json=payload,
                params=params,
                headers=self.headers,
                verify=self.verify_cert,
            )

            # Raise exception on HTTP error codes
            r.raise_for_status()

        except HTTPError as e:
            m = r.json().get("message")
            raise ValueError(f"{e}: {m}")

        # Return True on "no content" response
        if r.status_code == 204:
            return True

        return r.json()

    ## HARDWARE ##

    def reboot_system(self) -> bool:
        """Reboot the system"""
        raise NotImplementedError()

    def shut_down_system(self) -> bool:
        """Shut down the system"""
        raise NotImplementedError()

    ## TIME ##

    def get_system_time(self) -> str:
        """Get the current system time"""
        # FIXME: Return datetime object
        return self._request("GET", "/system/time")["time"]

    def set_system_time(self, time) -> bool:
        """Set the system time from a datetime object"""
        # datetime
        raise NotImplementedError()

    def get_system_uptime(self) -> int:
        """Get the current system uptime in seconds"""
        return self._request("GET", "/system/uptime")["uptime"]

    ## UPDATE ##

    def get_software_version(self) -> str:
        """Get the current Halon version"""
        return self._request("GET", "/system/versions/current")["version"]

    def get_latest_software_version(self) -> list:
        """Get the latest Halon version"""
        return self._request("GET", "/system/versions/latest")

    def get_update_status(self) -> dict:
        """Get update status. Error code 500 if no update in progress"""
        return self._request("GET", "/system/update")

    def cancel_pending_update(self) -> bool:
        """Cancel a pending update"""
        return self._request("DELETE", "/system/update")

    def download_update(self, version) -> bool:
        """Begin downloading (prefetching) an update"""
        payload = {"version": version}
        return self._request("POST", "/system/update:download", payload=payload)

    def install_update(self, version) -> bool:
        """Install an update"""
        payload = {"version": version}
        return self._request("POST", "/system/update:install", payload=payload)

    ## DNS ##

    def clear_dns_cache(self) -> bool:
        """Clear the DNS cache"""
        raise NotImplementedError()

    ## COMMANDS ##

    ## FILES ##

    ## CONFIG ##

    ## EMAIL ##

    def get_email_history(self, params) -> list:
        """Get emails from history"""
        raise NotImplementedError()

    def get_email(self, id) -> dict:
        """Get an email from history"""
        raise NotImplementedError()

    ## REPORTING ##

    def get_license(self) -> dict:
        """Get license information for the system"""
        return self._request("GET", "/license")

    def refresh_license(self) -> bool:
        """Refresh the license information"""
        raise NotImplementedError()

    def import_license_key(self, key) -> bool:
        """Import a license key (for offline use)"""
        raise NotImplementedError()

    ## STATS ##

    def get_stats(self, filter="", offset=0, limit=5) -> list:
        """List the stat entries"""
        params = {filter: filter, "offset": offset, "limit": limit}
        return self._request("GET", "/stats", params=params)

    def clear_stats(self) -> bool:
        """Clear the stat entries"""
        raise NotImplementedError()

    ## GRAPHS ##

    def get_graphs(self, offset=0, limit=5) -> list:
        """List the graph databases"""
        params = {"offset": offset, "limit": limit}
        return self._request("GET", "/graphs", params=params)