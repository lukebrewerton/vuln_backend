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

from config import *
from core import *

logger = logging.getLogger()


def main():
    logger.info('Running Vulnerability check updater...')
    try:
        vuln_sets.update_vuln_sets(db_server, db_user, db_pwd, db_name, api_search_path)
        download.get_active_vuln_sets(db_server, db_user, db_pwd, db_name)
        download.download(api_path, vuln_folder)
        download.processfiles(vuln_folder)
        mongodb.import_json(mongo_server, mongo_port, vuln_folder)
        logger.info('Successfully updated!')
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    main()