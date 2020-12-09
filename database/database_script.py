import time

from mysql.connector import connect, Error

# Please fill correct database credentials

database_credentials = {
    "host": "localhost",
    "user": "root",
    "passwd": "toor",
    "database": "demodb"
}

# Database Table Column Names
columns = [
    "ticker", "company_name"
]

table_name = "tbl_companies"


class DatabaseScript:

    def __init__(self):
        self.open_sql_connection()
        self.create_table()
        self.insert_companies()

    def get_companies(self):
        companies = []
        with open('alllisted.txt') as file:
            for index, line in enumerate(file):
                results = line.split(',')
                companies.append((results[0], ','.join(results[1:]).strip()))
        return companies

    def insert_companies(self, retry_times=0):
        place_holders = ', '.join(['%s'] * len(columns))
        query = f"INSERT INTO `{table_name}` ({', '.join(f'`{c}`' for c in columns)}) VALUES({place_holders})"

        try:
            self.update_mysql_connection()
            self.sql_conn_cursor.executemany(query, self.get_companies())
            self.sql_connection.commit()
            print(f"{self.sql_conn_cursor.rowcount} rows inserted in {table_name}")

        except Exception as e:
            if self.can_retry(f"Exception while inserting record in " f"{table_name}\n{e}", retry_times):
                self.insert_companies(retry_times + 1)
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

    def create_table(self):
        query = "SHOW TABLES"
        self.sql_conn_cursor.execute(query)
        tables = [r[0] for r in self.sql_conn_cursor.fetchall()]

        if table_name in tables:
            return

        create_query = f"""
        CREATE TABLE `{table_name}` (
        `id` int(11) NOT NULL auto_increment,
        `ticker` varchar(48),
        `company_name` varchar(500),
        PRIMARY KEY (`id`)
        );
        """
        self.sql_conn_cursor.execute(create_query)
        self.sql_connection.commit()
        print(f"Table {table_name} created successfully.")


if __name__ == "__main__":
    DatabaseScript()
    pass
