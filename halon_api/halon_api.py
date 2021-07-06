import requests
from requests.models import HTTPError

import json


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
        return self._request("POST", "/system:reboot")

    def shut_down_system(self) -> bool:
        """Shut down the system"""
        return self._request("POST", "/system:shutdown")

    ## TIME ##

    def get_system_time(self) -> str:
        """Get the current system time"""
        return self._request("GET", "/system/time")["time"]

    def set_system_time(self, time) -> bool:
        """Set the system time"""
        payload = {"time": time}
        return self._request("PUT", "/system/time", payload=payload)

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

    def clear_dns_cache(self, name, filter="") -> bool:
        """Clear the DNS cache"""
        # params = {"filter": filter, "name": name}
        # return self._request("DELETE", "/system/dns/cache", params=params)
        raise NotImplementedError()

    ## COMMANDS ##

    ## FILES ##

    def read_file(self, path, size_offset=0, size_limit=1024) -> dict:
        """Read a file from disk"""
        params = {"path": path, "offset": size_offset, "limit": size_limit}
        return self._request("GET", "/system/files", params=params)

    def write_file(self, path, bytes) -> bool:
        """Write a file to disk"""
        encoded = base64.b64encode(bytes)
        params = {"path": path}
        payload = {"data": encoded.decode("ascii")}
        return self._request("PUT", "/system/files", params=params, payload=payload)

    def clear_file(self, path):
        """Clear a file on disk"""
        params = {"path": path}
        return self._request("DELETE", "/system/files", params=params)

    def get_file_size(self, path):
        """Get the size of a file in bytes"""
        params = {"path": path}
        return self._request("POST", "/system/files:size", params=params)

    ## REVISIONS ##

    def list_config_revisions(self, offset=0, limit=5) -> list:
        """List the config revisions"""
        params = {"offset": offset, "limit": limit}
        return self._request("GET", "/config/revisions", params=params)

    def get_config_revision(self, id="HEAD", type=-1) -> dict:
        """Get a single config revision. id must be a positive integer, or the string 'HEAD'"""
        params = {"type": type}
        return self._request("GET", f"/config/revisions/{id}", params=params)

    def create_config_revision(self, id, config, message="Created through API") -> int:
        """Add a configuration revision. Config is a list of dicts. One dict pr. parameter. Return new configuration ID"""
        payload = {"config": config, "message": message}
        return self._request("POST", f"/config/revisions/{id}", payload=payload)["id"]

    ## TESTING/LIVESTAGING ##

    ## EMAIL ##

    def get_email_history(
        self, filter=None, offset=0, limit=5, sortby="time2", total=False
    ) -> dict:
        """Get emails from history"""
        params = {
            "filter": filter,
            "offset": offset,
            "limit": limit,
            "total": str(total).lower(),
            "sortby": sortby,
        }
        return self._request("GET", "/email/history", params=params)

    def get_email(self, id) -> dict:
        """Get an email from history"""
        return self._request("GET", f"/email/history/{id}")["email"]

    ## LICENSE ##

    def get_license(self) -> dict:
        """Get license information for the system"""
        return self._request("GET", "/license")

    def refresh_license(self) -> bool:
        """Refresh the license information"""
        return self._request("POST", "/license:refresh")

    def import_license_key(self, key) -> bool:
        """Import a license key (for offline use)"""
        payload = {"key": key}
        return self._request("PUT", "/license/key", payload=payload)

    ## STATS ##

    def list_stats(
        self, name=None, namespace=None, legend=None, offset=0, limit=5
    ) -> list:
        """List the stat entries"""
        params = {
            "filter[name]": name,
            "filter[namespace]": namespace,
            "filter[legend]": legend,
            "offset": offset,
            "limit": limit,
        }
        return self._request("GET", "/stats", params=params)

    def clear_stats(self, name=None, namespace=None, legend=None) -> int:
        """Clear stat entries matched by filter. Returns number of accected stats"""
        params = {
            "filter[name]": name,
            "filter[namespace]": namespace,
            "filter[legend]": legend,
        }
        return self._request("DELETE", "/stats", params=params)["affected"]

    ## GRAPHS ##

    def list_graphs(self, offset=0, limit=5) -> list:
        """List the graph databases"""
        params = {"offset": offset, "limit": limit}
        return self._request("GET", "/graphs", params=params)

    def get_graph(self, id) -> str:
        """Export a graph databases"""
        return self._request("GET", f"/graphs/{id}")["data"]

    def clear_graph(self, id) -> bool:
        """Clear a graph databases"""
        return self._request("DELETE", f"/graphs/{id}")

    ## SCRIPTS ##
