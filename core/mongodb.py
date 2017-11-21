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

import json
import logging
import logging.handlers
import os
import pymongo
from datetime import timedelta, datetime
from pymongo import MongoClient


def import_json(mongo_server,mongo_port, vuln_folder):
    try:
        logging.info('Connecting to MongoDB')
        client = MongoClient(mongo_server, mongo_port)
        db = client['vuln_sets']
        coll = db['vulnerabilities']
        logging.info('Connected to MongoDB')
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, ".."))
        archive_filepath = filepath + vuln_folder
        filedir = os.chdir(archive_filepath)
        file_count = 0
        for item in os.listdir(filedir):
            if item.endswith('.json'):
                file_name = os.path.abspath(item)
                with open(item, 'r') as currentfile:
                    vuln_counter = 0
                    duplicate_count = 0
                    logging.info('Currently processing ' + item)
                    file_count +=1
                    json_data = currentfile.read()
                    vuln_content = json.loads(json_data)
                    today = datetime.now()
                    last_month = today - timedelta(days=30)
                    for vuln in vuln_content:
                        try:
                            del vuln['_type']
                            new_vuln = {key: vuln[key] for key in vuln if key != '_source'}
                            new_vuln.update(vuln['_source'])
                            if new_vuln['published'] >= str(last_month):
                                coll.insert(new_vuln, continue_on_error=True)
                                vuln_counter += 1
                            else:
                                pass
                        except pymongo.errors.DuplicateKeyError:
                            duplicate_count +=1

                logging.info('Added ' + str(vuln_counter) + ' vulnerabilities for ' + item)
                logging.info('Found ' + str(duplicate_count) + ' duplicate records!')
                os.remove(file_name)
        logging.info('Processed ' + str(file_count) + ' files')
    except Exception as e:
        logging.exception(e)
