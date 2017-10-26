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
import os
import MySQLdb
from hurry.filesize import size, si
import logging
import logging.handlers
from zipfile import ZipFile

logger = logging.getLogger(__name__)

def get_active_vuln_sets(db_server, db_user, db_pwd, db_name):


    try:
        global active_vuln_type
        logging.info('Connecting to the database...')
        active_vuln_type = con = MySQLdb.connect(db_server, db_user, db_pwd, db_name)
        logging.info('Database connected!')
    except FileNotFoundError as fnf:
        logging.error(fnf)
    except MySQLdb.Error as e:
        logging.error(e)
    try:
        logging.info('Getting active vulnerability sets...')
        cur = con.cursor()
        active = "1"
        cur.execute("""SELECT vulntype FROM vuln_sets WHERE active = %s""", active)
        active_vuln_type = cur.fetchall()
    except MySQLdb.Error as e:
        logging.exception(e)


def download(api_path, vuln_folder):
    try:
        logging.info('Downloading vulnerability set files...')
        for db_row in active_vuln_type:
            x = db_row[0]
            basepath = os.path.dirname(__file__)
            filepath = os.path.abspath(os.path.join(basepath, ".."))
            response = requests.get(api_path + x)
            with open(filepath + vuln_folder + x + '.zip', 'wb') as f:
                f.write(response.content)
            filesize = size(os.path.getsize
                            (filepath + vuln_folder
                             + x + '.zip'), system=si)
            files = x + ".zip - " + str(filesize)
            logging.info('Downloaded ' + x + '.zip Successfully')
            logging.info('File details: ' + files)
    except Exception as e:
        logging.exception(e)


def processfiles(vuln_folder):
    try:
        logging.info('Processing downloaded files')
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, ".."))
        archive_filepath = filepath + vuln_folder
        filedir = os.chdir(archive_filepath)
        for item in os.listdir(filedir):
            if item.endswith('.zip'):
                file_name = os.path.abspath(item)
                zip_ref = ZipFile(file_name)
                zip_ref.extractall(filedir)
                zip_ref.close()
                logging.info(item + ' extracted successfully!')
                os.remove(file_name)
    except Exception as e:
        logging.exception(e)
        logging.error(e)


