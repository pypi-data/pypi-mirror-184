####
##
#
#

import os
import sys
import csv
import deta
import fire
import src.cli as this

DETA_PROJECT_KEY = os.getenv("DETA_PROJECT_KEY", None)


class DetaCsv:
    def __init__(self):
        scriptname = os.path.basename(sys.argv[0]).rsplit(".", 1)[0]
        print(scriptname, "version", this.__version__)
        if len(sys.argv) == 1:
            print(f"type `{scriptname} --help` for more info")
            sys.exit()
        pass

    def upload(
        self,
        path: str,
        dbname: str = None,
        project: str = DETA_PROJECT_KEY,
        key: str = "key",
        encoding: str = "UTF-8",
        asynct: bool = False,
        verbose: bool = False,
    ):
        """
        Read csv file and upload data to your deta project database

        PATH_TO_CSV_FILE : str
        DETA_DB_NAME : str
        DETA_PROJECT_KEY : str
        CSV_FILE_ENCODING : str
        ASYNCHRONOUS_TRANSFER_FLAG : any

        :param str path: The path (absolute or relative) to the source CSV data file
        :param str dbname: The name of your Deta Base, default filename(PATH_TO_CSV_FILE)
        :param str project: The `project key` of your Deta Base instance, default DETA_PROJECT_KEY environment variable
        :param str key: - unused yet - The name for `key` field (like ID field in RDB) to store the data under
        :param str encoding: CSV file encoding, default UTF-8
        :param str asynct: unused
        :return: None
        """

        dbname = dbname or os.path.basename(path).rsplit(".", 1)[0]

        print(f"* Open detabase `{dbname}`")
        db = (deta.Deta(key)).Base(dbname)

        print(f"* Reading CSV from `{path}`")
        with open(path, mode="r", encoding=encoding) as csv_file:
            count = 0
            csv_reader = csv.DictReader(csv_file)
            for csv_row in csv_reader:
                db.put(csv_row)
                not verbose or print(f"Uploaded\t# {count}\t {csv_row}")
                count += 1

            print(f"Succesfully uploaded {count} rows to `{dbname}` Deta Base")

        return

    def download(
        self,
        dbname: str,
        path: str = None,
        project: str = DETA_PROJECT_KEY,
        key: str = "key",
        encoding: str = "UTF-8",
        asynct: bool = False,
        verbose: bool = False,
    ):
        """
        Read your Deta Base and save content to CSV file

        DETA_DB_NAME : str
        PATH_TO_CSV_FILE : str
        DETA_PROJECT_KEY : str
        CSV_FILE_ENCODING : str
        ASYNCHRONOUS_TRANSFER_FLAG : any

        :param str dbname: The name of your Deta Base
        :param str path: The path to the target CSV file, default `DETA_DB_NAME.csv`
        :param str project: The `project key` of your Deta Base instance, default DETA_PROJECT_KEY environment variable
        :param str key: - unused yet - The name for `key` field (like ID field in RDB) to store the data under
        :param str encoding: CSV file encoding, default UTF-8
        :param str asynct: unused
        :return: None
        """
        pass
