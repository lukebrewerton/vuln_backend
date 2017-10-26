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

import requests
import json
import MySQLdb
import logging
import logging.handlers
from config import *


logger = logging.getLogger('vulnsets')


def update_vuln_sets(db_server, db_user, db_pwd, db_name, api_search_path):
    try:
        logging.info('Connecting to the database...')
        con = MySQLdb.connect(db_server, db_user, db_pwd, db_name)
        logging.info('Database connected!')
    except FileNotFoundError as fnf:
        logging.error(fnf)
    except MySQLdb.Error as e:
        logging.error(e)
    try:
        logging.info('Getting latest vulnerability sets from Vulners API...')
        response = requests.get(api_search_path)
        response.encoding = 'windows-1252'
        vuln_set = json.loads(response.text)
        vuln_type = vuln_set['data']['type_results']
    except Exception as e:
        logging.error(e)
    try:
        logging.info('Processing JSON response')
        for k in vuln_type:
            vuln_bulletinfamily = vuln_set['data']['type_results'][k]['bulletinFamily']
            vuln_name = vuln_set['data']['type_results'][k]['displayName']
            vuln_count = vuln_set['data']['type_results'][k]['count']
            try:
                logging.info('Inserting vulnerability type ' + k + ' into DB')
                with con:
                    cur = con.cursor()
                    cur.execute(
                            "INSERT INTO vuln_sets (vulntype, displayname, bulletinfamily, vulncount)"
                            " VALUES (%s,%s,%s,%s) ON DUPLICATE KEY"
                            " UPDATE vulncount = %s",
                            [k, vuln_name, vuln_bulletinfamily, vuln_count, vuln_count]
                    )
                    con.commit()
                logging.info('Vulnerability type ' + k + ' inserted successfully!')
            except Exception as e:
                logging.error(str(e))
        logging.info('Vulnerability sets successfully updated!')
    except Exception as e:
        logging.error(e)
