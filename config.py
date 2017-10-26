# Vulnerabilities Tool
# Copyright (C) 2017  Luke Brewerton
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import configparser
import logging.handlers
from logging.config import fileConfig

# Logging Settings
logging.handlers = logging.handlers
fileConfig('config.ini')


# Config settings
config = configparser.ConfigParser()
config.read('config.ini')

# Config variables
db_server = config['DB']['DB_SERVER']
db_user = config['DB']['DB_USER']
db_pwd = config['DB']['DB_PWD']
db_name = config['DB']['DB_NAME']
api_search_path = config['API']['API_SEARCH_PATH']
api_path = config['API']['API_PATH']
vuln_folder = config['FILES']['VULN_FOLDER']
mongo_server = config['MONGO']['MONGO_SERVER']
mongo_port = int(config['MONGO']['MONGO_PORT'])

