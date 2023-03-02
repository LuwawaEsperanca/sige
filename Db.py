import psycopg2
import psycopg2.extras
class Con:
   DB_HOST = "localhost"
   DB_NAME = "sige_db"
   DB_USER = "postgres"
   DB_PASS = "postgres"
 
   def inic(self):
       return psycopg2.connect(dbname= self.DB_NAME,
        user= self.DB_USER, password= self.DB_PASS, 
        host= self.DB_HOST)
