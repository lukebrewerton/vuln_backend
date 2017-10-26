# Vulnerability check backend

[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)

[![Build Status](https://travis-ci.org/lukebrewerton/vuln_backend.svg?branch=master)](https://travis-ci.org/lukebrewerton/vuln_backend)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=shields)](http://makeapullrequest.com)

A python script that connects to the [vulners.com](https://gist.github.com/athityakumar/1bd5e9e24cd2a1891565573a893993eb) API to pull in all security vulnerabilities that apply to your setup.
\
This is the backend responsible for the following:-

- Connecting to the API to get a list of all the types of vulnerabilities i.e. Cisco, Linux, Windows etc.
- Putting these into a SQLite DB so that they can be selected or deselected from the frontend
- Downloading the relevant .zip files from vulners and storing them in a folder to be accessed by the front end.



# Table of contents

- [Usage](#usage)
- [Installation](#installation)
- [Recommended configurations](#recommended-configurations)
- [Updating](#updating)
- [Uninstallation](#uninstallation)
- [Contributing](#contributing)
- [License](#license)

# Usage
To use the backend run `python3 main.py` from within the main directory of the script or setup a crontab job to do this, \
i.e. `0 1 * * 0-6 python3 /root/bin/vuln_backend/main.py >/dev/null 2>&1` 

[(Back to top)](#table-of-contents)



# Installation

Download the Zip of the script and extract to an easily accessible folder i.e. `/root/bin/vuln_backend`

[(Back to top)](#table-of-contents)



# Updating

To update, check the project homepage [here](#) to check the latest release.

[(Back to top)](#table-of-contents)



# Uninstallation

To uninstall, just delete the files and the crontab if you have set one up.

[(Back to top)](#table-of-contents)



# Contributing

[(Back to top)](#table-of-contents)

Your contributions are always welcome! Please have a look at the [contribution guidelines](CONTRIBUTING.md) first. :tada:

# License

[(Back to top)](#table-of-contents)


GPLv3 2017 - [LukeBrewerton](https://github.com/lukebrewerton/). Please have a look at the [LICENSE.md](LICENSE.md) for more details.
