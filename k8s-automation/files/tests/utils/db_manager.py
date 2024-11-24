import pymysql


def create_table():
    connection = pymysql.connect(host="localhost", user="root", password="arshdeep", database="testdb")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metrics (
            id INT AUTO_INCREMENT PRIMARY KEY,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            value FLOAT
        );
    """)
    cursor.execute("INSERT INTO metrics (value) VALUES (10.5), (20.7), (30.1);")
    connection.commit()
    cursor.close()
    connection.close()

