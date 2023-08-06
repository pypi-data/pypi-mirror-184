# Raiseup

Raiseup is a small Python library(a fork of [elevate](https://github.com/barneygale/elevate)) that re-launches the current process with root/admin privileges using one of the following mechanisms:

- UAC (Windows)
- AppleScript (macOS)
- `pkexec`, `gksudo`, `kdesudo` or `doas` (Linux and FreeBSD)
- `sudo` (Linux, macOS)

### Usage

To use, call `raiseup.elevate(file_path)` early in your script(where `file_path` is the absolute path of the script that needs to be elevated). When run as root this
function does nothing. When not run as root, this function replaces the current
process (Linux, macOS) or creates a new process, waits, and exits (Windows).

Consider the following example(Note: `os.getuid()` only works on POSIX based systems. For windows, you might need to find other ways to check which user this script is currently running as):

```python
import os
def is_root():
    return os.getuid() == 0
if not is_root():
    from raiseup import elevate
    print("Not root")
    elevate(__file__)
else:
    print("This script is running as root")
```

This prints:

```
Not root
This script is running as root
```

On Windows, the new process's standard streams are not attached to the parent,
which is an inherent limitation of UAC. By default the new process runs in a
new console window. To suppress this window, use
`elevate(file_path,show_console=False)`.

On Linux and macOS, graphical prompts are tried before `sudo` and `doas`, by default. To prevent graphical prompts, use `elevate(file_path,graphical=False)`.

### Improvements over [Elevate](https://github.com/barneygale/elevate):

- Graphical environment variables `$DISPLAY` and `$XAUTHORITY` are automatically passed on to the elevated process (useful for GUI applications) on Linux and FreeBSD
- Added support for `doas` and the FreeBSD operating system
- Older code has been cleaned up
- Broken code has been fixed

### PyPI Package:

Raiseup is available to be installed from PyPI [here]()

`pip install raiseup`

### A common mistake:

Avoid importing `raiseup` unconditionally in your scripts if the `raiseup` package is not installed for the root/administrator user. Otherwise, the `raiseup` package will be imported regradless of which user is running the script. If the root user is running the script, it will fail to find `raiseup` resulting in a `ModuleNotFoundError` and script termination.

(c) 2018 [Barney Gale](https://github.com/barneygale/) and (c) 2021 [Xploreinfinity](https://github.com/xploreinfinity)