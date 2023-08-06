from connectiontypes.postgres_handler import Postgres_Handler as pg_handler

class Database_Handler:
    def __init__(self, db_type):
        self.db_type = db_type
        self.__build_connection()

    def __build_connection(self):
        self.handler = pg_handler()
    
    def add_sql_props(self, columns, keywords, base_query):
        self.handler.define_columns(columns)
        self.handler.set_base_query(base_query)
        self.handler.set_keywords(keywords)
    
    def search_records(self):
        return self.handler.search_for_records()