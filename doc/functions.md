<a name="halon_api"></a>
# `halon_api`

<a name="halon_api.HalonAPI"></a>
## `HalonAPI` Objects

```python
class HalonAPI()
```

<a name="halon_api.HalonAPI.__init__"></a>
#### `__init__`

```python
 | HalonAPI.__init__(host: str, user: str, password: str, version: str = "5.6.0", secure: bool = True, verify: bool = True, port: int = None) -> None
```

Initialize a HalonAPI object.

**Arguments**:

- `host` - The fqdn of the Halon server
- `user` - The user to access Halon as
- `password` - The password for the Halon user
- `version` - The version of the Halon API to use
- `secure` - Control the use of HTTPS
- `verify` - Verify certificate on host (Bool) or full chain CA_BUNDLE .pem file
- `port` - The port to use. Will override 443 for https and 80 for http

<a name="halon_api.HalonAPI.reboot_system"></a>
#### `reboot_system`

```python
 | HalonAPI.reboot_system() -> bool
```

Reboot the system.

<a name="halon_api.HalonAPI.shut_down_system"></a>
#### `shut_down_system`

```python
 | HalonAPI.shut_down_system() -> bool
```

Shut down the system.

<a name="halon_api.HalonAPI.get_system_time"></a>
#### `get_system_time`

```python
 | HalonAPI.get_system_time() -> str
```

Get the current system time as string in format 'YYYY-MM-DDTHH:MM:SSZ'.

<a name="halon_api.HalonAPI.set_system_time"></a>
#### `set_system_time`

```python
 | HalonAPI.set_system_time(time: str) -> bool
```

Set the system time

**Arguments**:

- `time` - Time in format 'YYYY-MM-DDTHH:MM:SSZ'

<a name="halon_api.HalonAPI.get_system_uptime"></a>
#### `get_system_uptime`

```python
 | HalonAPI.get_system_uptime() -> int
```

Get the current system uptime in seconds.

<a name="halon_api.HalonAPI.get_software_version"></a>
#### `get_software_version`

```python
 | HalonAPI.get_software_version() -> str
```

Get the current Halon version.

<a name="halon_api.HalonAPI.list_latest_software_versions"></a>
#### `list_latest_software_versions`

```python
 | HalonAPI.list_latest_software_versions() -> list
```

Get the latest Halon versions. This includes the current version

<a name="halon_api.HalonAPI.get_update_status"></a>
#### `get_update_status`

```python
 | HalonAPI.get_update_status() -> dict
```

Get update status. Error code 500 if no update in progress

<a name="halon_api.HalonAPI.cancel_pending_update"></a>
#### `cancel_pending_update`

```python
 | HalonAPI.cancel_pending_update() -> bool
```

Cancel a pending update

<a name="halon_api.HalonAPI.download_update"></a>
#### `download_update`

```python
 | HalonAPI.download_update(version: str) -> bool
```

Begin downloading (prefetching) an update

<a name="halon_api.HalonAPI.install_update"></a>
#### `install_update`

```python
 | HalonAPI.install_update(version: str) -> bool
```

Install an update. If on system, it will be downloaded.

<a name="halon_api.HalonAPI.clear_dns_cache"></a>
#### `clear_dns_cache`

```python
 | HalonAPI.clear_dns_cache(filter: str) -> bool
```

Clear the DNS cache

**Arguments**:

- `filter` - A filter matching the DNS records to clear

<a name="halon_api.HalonAPI.read_file"></a>
#### `read_file`

```python
 | HalonAPI.read_file(path: str, size_offset: int = 0, size_limit: int = 1024) -> dict
```

Read a file from disk

<a name="halon_api.HalonAPI.write_file"></a>
#### `write_file`

```python
 | HalonAPI.write_file(path: str, data: bytes) -> bool
```

Write a file to disk

<a name="halon_api.HalonAPI.clear_file"></a>
#### `clear_file`

```python
 | HalonAPI.clear_file(path: str)
```

Clear a file on disk

<a name="halon_api.HalonAPI.get_file_size"></a>
#### `get_file_size`

```python
 | HalonAPI.get_file_size(path: str)
```

Get the size of a file in bytes

<a name="halon_api.HalonAPI.list_config_revisions"></a>
#### `list_config_revisions`

```python
 | HalonAPI.list_config_revisions(offset: int = 0, limit: int = 5) -> list
```

List the config revisions.

**Arguments**:

- `offset` - The offset, in pages, to use (>= 0).
- `limit` - Maximum number of items to return (1 .. 10000).

<a name="halon_api.HalonAPI.get_config_revision"></a>
#### `get_config_revision`

```python
 | HalonAPI.get_config_revision(id: str = "HEAD", type: int = None) -> dict
```

Get a single config revision.

**Arguments**:

- `id` - A positive integer or the string 'HEAD'
- `type` - The config type. Can only be used with HEAD or a test config (-1 .. 5).

<a name="halon_api.HalonAPI.create_config_revision"></a>
#### `create_config_revision`

```python
 | HalonAPI.create_config_revision(id: str, config: list, message: str = "Created through API") -> int
```

Add a configuration revision. Config is a list of dicts.
One dict pr. parameter. Return new configuration ID

<a name="halon_api.HalonAPI.start_config_test"></a>
#### `start_config_test`

```python
 | HalonAPI.start_config_test(config: list, id: str = None, conditions: dict = None) -> bool
```

Start a new configuration test

<a name="halon_api.HalonAPI.get_config_test_status"></a>
#### `get_config_test_status`

```python
 | HalonAPI.get_config_test_status() -> dict
```

Get the status of the running config test

<a name="halon_api.HalonAPI.get_test_config"></a>
#### `get_test_config`

```python
 | HalonAPI.get_test_config(id: str, type: int = None) -> dict
```

Get the test configuration

<a name="halon_api.HalonAPI.cancel_config_test"></a>
#### `cancel_config_test`

```python
 | HalonAPI.cancel_config_test(id: str) -> bool
```

Cancel the running configuration test

<a name="halon_api.HalonAPI.debug_config_test"></a>
#### `debug_config_test`

```python
 | HalonAPI.debug_config_test(id: str) -> dict
```

Debug the running config test

<a name="halon_api.HalonAPI.check_config"></a>
#### `check_config`

```python
 | HalonAPI.check_config(config: list) -> bool
```

Check a configuration for errors

<a name="halon_api.HalonAPI.list_email_history"></a>
#### `list_email_history`

```python
 | HalonAPI.list_email_history(filter: str = None, offset: int = 0, limit: int = 5, sortby: str = None, total: bool = False) -> dict
```

Get emails from history

<a name="halon_api.HalonAPI.get_email"></a>
#### `get_email`

```python
 | HalonAPI.get_email(id: int) -> dict
```

Get an email from history

<a name="halon_api.HalonAPI.get_license"></a>
#### `get_license`

```python
 | HalonAPI.get_license() -> dict
```

Get license information for the system

<a name="halon_api.HalonAPI.refresh_license"></a>
#### `refresh_license`

```python
 | HalonAPI.refresh_license() -> bool
```

Refresh the license information

<a name="halon_api.HalonAPI.import_license_key"></a>
#### `import_license_key`

```python
 | HalonAPI.import_license_key(key: str) -> bool
```

Import a license key (for offline use)

<a name="halon_api.HalonAPI.list_stats"></a>
#### `list_stats`

```python
 | HalonAPI.list_stats(name: str = None, namespace: str = None, legend: str = None, offset: int = 0, limit: int = 5) -> list
```

List the stat entries

<a name="halon_api.HalonAPI.clear_stats"></a>
#### `clear_stats`

```python
 | HalonAPI.clear_stats(name: str = None, namespace: str = None, legend: str = None) -> int
```

Clear stat entries matched by filter. Returns number of accected stats

<a name="halon_api.HalonAPI.list_graphs"></a>
#### `list_graphs`

```python
 | HalonAPI.list_graphs(offset: str = 0, limit: str = 5) -> list
```

List the graph databases

<a name="halon_api.HalonAPI.export_graph"></a>
#### `export_graph`

```python
 | HalonAPI.export_graph(id: str) -> str
```

Export a graph databases

<a name="halon_api.HalonAPI.clear_graph"></a>
#### `clear_graph`

```python
 | HalonAPI.clear_graph(id: str) -> bool
```

Clear a graph databases

<a name="__init__"></a>
# `__init__`
