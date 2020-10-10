import time

from mysql.connector import connect, Error

# Please fill correct Database Credentials

database_credentials = {
    "host": "",
    "user": "",
    "passwd": "",
    "database": ""
}

# Database Table Field/Column Names

table_fields = [
    "COMPANY_NAME", "ADDRESS", "ADDRESS_2", "CITY", "STATE_ABR", "STATE_NAME", "ZIP_CODE",
    "PHONE", "FAX", "TOLL_FREE_NUMBER", "BRANCH_MANAGER", "BM_NMLS_ID", "BM_EMAIL",
    "REGIONAL_MANAGER", "RM_NMLS_ID", "RM_EMAIL", "MAP_LINK", "POSITION",
    "VISIBLE", "BRANCH_NMLS_ID", "DAYS_OF_OPERATION", "HOURS_OF_OPERATION", "BRANCH_IMAGE",
    "BRANCH_POSITION", "BRANCH", "ORIGINATION_TYPE_SERVICE", "WEBSITE_NAME", "WEBSITE_LINK",
]

# Input Fields, Please inside double quotes ""  you can fill/modify input fields information

COMPANY_NAME = ""
ADDRESS = ""
ADDRESS_2 = ""
CITY = ""
STATE_ABR = ""
STATE_NAME = ""
ZIP_CODE = ""
PHONE = ""
FAX = ""
TOLL_FREE_NUMBER = ""
BRANCH_MANAGER = ""
BM_NMLS_ID = ""
BM_EMAIL = ""
REGIONAL_MANAGER = ""
RM_NMLS_ID = ""
RM_EMAIL = ""
MAP_LINK = ""
POSITION = ""
VISIBLE = ""
BRANCH_NMLS_ID = ""
DAYS_OF_OPERATION = ""
HOURS_OF_OPERATION = ""
BRANCH_IMAGE = ""
BRANCH_POSITION = ""
BRANCH = ""
ORIGINATION_TYPE_SERVICE = ""
WEBSITE_NAME = ""
WEBSITE_LINK = ""


class UpdateMysqlDatabase:

    def __init__(self):
        self.open_sql_connection()
        self.insert_record()

    def insert_record(self, retry_times=0):
        table_name = "SWMC_BRANCHES"
        place_holders = ', '.join(['%s'] * len(table_fields))
        query = f"INSERT INTO `{table_name}` ({', '.join(f'`{c}`' for c in table_fields)}) VALUES({place_holders})"

        values = (
            COMPANY_NAME, ADDRESS, ADDRESS_2, CITY, STATE_ABR, STATE_NAME, ZIP_CODE,
            PHONE, FAX, TOLL_FREE_NUMBER, BRANCH_MANAGER, BM_NMLS_ID, BM_EMAIL,
            REGIONAL_MANAGER, RM_NMLS_ID, RM_EMAIL, MAP_LINK, POSITION,
            VISIBLE, BRANCH_NMLS_ID, DAYS_OF_OPERATION, HOURS_OF_OPERATION, BRANCH_IMAGE,
            BRANCH_POSITION, BRANCH, ORIGINATION_TYPE_SERVICE, WEBSITE_NAME, WEBSITE_LINK,
        )

        try:
            self.update_mysql_connection()
            self.sql_conn_cursor.execute(query, values)
            self.sql_connection.commit()
            print(f"{self.sql_conn_cursor.rowcount} rows inserted in {table_name}")

        except Exception as e:
            if self.can_retry(f"Exception while inserting record in "
                              f"{table_name}\n{e}", retry_times):
                self.insert_record(retry_times + 1)
                return

    def can_retry(self, log, retry_times):
        if retry_times == 2:
            return

        time.sleep(5)
        self.update_mysql_connection()
        print(log)
        return True

    def open_sql_connection(self):
        connection_tries = 0
        while connection_tries < 5:
            try:
                self.sql_connection = connect(**database_credentials)
                self.sql_conn_cursor = self.sql_connection.cursor()
                break
            except Error as err:
                print("Exception while making SQL Database Connection: {}".format(err))
                connection_tries += 1
                time.sleep(30)

        if connection_tries == 5:
            print("Failed 5 tries to establish connection")
            raise StopIteration()

    def update_mysql_connection(self):
        if self.sql_connection.is_connected():
            return
        self.open_sql_connection()


if __name__ == "__main__":
    UpdateMysqlDatabase()
