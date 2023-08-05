[![coverage report](https://gitlab.com/nobodyinperson/hledger-utils/badges/main/coverage.svg)](https://gitlab.com/nobodyinperson/hledger-utils/-/commits/main)
[![pipeline status](https://gitlab.com/nobodyinperson/hledger-utils/badges/main/pipeline.svg)](https://gitlab.com/nobodyinperson/hledger-utils/-/commits/main)
[![Downloads](https://static.pepy.tech/badge/hledger-utils)](https://pepy.tech/project/hledger-utils)

#  🛠️ `hledger` Utilities

This Python package extends [`hledger`](https://hledger.org) the [plaintextaccounting](https://plaintextaccounting.org) tool with some utilities.
 
## ✨ Features Added to `hledger`

### `hledger edit ...`: 📝 Editing `hledger` Transactions in your `$EDITOR`

```bash
# Opens your EDITOR (or VISUAL) with only transactions in € that have a Berlin tag
# You can modify them as usual, if you save and quit the editor, the changes will be
# applied to the appropriate files
hledger edit cur:€ tag:location=Berlin

# Opens your EDITOR with all transactions
hledger edit

# If you don't have LEDGER_FILE set, you need to specify a journal file as usual:
hledger edit -f journal.hledger
```

This should work with pretty much any hledger query, just substitute `hledger balance` or `hledger register` etc. with 'hledger edit'. This is a neat way of quickly editing transactions you were just inspecting.

🎥 Check this screencast below to see `hledger edit` in action:

[![asciicast](https://asciinema.org/a/549559.svg)](https://asciinema.org/a/549559)

## 📦 Installation

```bash
# Install this package from PyPI:
pip install hledger-utils

# Install the latest development version:
pip install git+https://gitlab.com/nobodyinperson/hledger-utils

# Install from the repository root
git clone https://gitlab.com/nobodyinperson/hledger-utils
cd hledger-utils
pip install .
```

> If that fails, try `python3 -m pip install --user ...` instead of just `pip install ...`

This package is also available [in the AUR as `python-hledger-utils-git`](https://aur.archlinux.org/packages/python-hledger-utils-git).
