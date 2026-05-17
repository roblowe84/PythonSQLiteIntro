# Load the sqlite database
import sqlite3
# Creates a sqlite database called 'store'.  
conn = sqlite3.connect('store')
# Creates the table within the database
conn.execute("CREATE TABLE 'pet' (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), checkups SMALLINT UNSIGNED, birth DATE, death DATE)")
