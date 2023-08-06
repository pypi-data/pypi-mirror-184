# 📂 MPBridge ![Python Version](https://img.shields.io/badge/Python-3.7%20or%20later-blue?style=flat-square) ![PyPI Version](https://img.shields.io/pypi/v/mpbridge?label=PyPI%20Version&style=flat-square) ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/AmirHmZz/mpbridge/python-publish.yml?label=Builds&style=flat-square) ![PyPI - Downloads](https://img.shields.io/pypi/dm/MPbridge?label=Downloads&style=flat-square)

A file system bridge to synchronise and manage files on a [MicroPython](https://github.com/micropython/micropython)
running device

## Supported platforms

- Windows
- MacOS
- Linux
- FreeBSD/BSD

## Dependencies

- Python 3.7 or above.
- [mpremote](https://pypi.org/project/mpremote/) >= 0.4.0
- [watchdog](https://pypi.org/project/watchdog/) >= 2.2.0
- [click](https://pypi.org/project/click/) >= 7.0
- [colorama](https://pypi.org/project/colorama/) >= 4.0

## Installation

`mpbridge` must be installed with `sudo` or `administrator` level of permission in order to be accessible in terminal:

### Windows

* Open `cmd.exe` as administrator and run `pip install -U mpbridge`

### Linux / MacOS

* Run `sudo pip install -U mpbridge`

## How to use

You can use `mpbridge` shell utility in several ways based on your needs:

### Bridge Mode

* This mode copies all files and folders from your `MicroPython` board into a temporary directory on your local device
  and listens for any filesystem events on local directory to apply them on your board.

1. Connect your `MicroPython` device
2. Run `mpbridge bridge <PORT>`

### Sync Directory

* This command syncs a specified local directory with a `MicroPython` board. The sync process will push 
all modified files and folders into board and also pull changes from board and exits.
* If a conflict occurs, `mpbridge` will choose the **local version** of file automatically and
overwrites it on connected board.
1. Connect your `MicroPython` device
2. Run `mpbridge sync <PORT> <DIR_PATH>`

**Note** : `<PORT>` can be the **full port path** or one of the **short forms** below :

* `c[n]` for `COM[n]` (`c3` is equal to `COM3`)
* `u[n]` for `/dev/ttyUSB[n]` (`u3` is equal to `/dev/ttyUSB3`)
* `a[n]` for `/dev/ttyACM[n]` (`a3` is equal to `/dev/ttyACM3`)
