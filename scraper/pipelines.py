
import mysql.connector

class MySQLPipeline:
    def open_spider(self, spider):
        self.conn = mysql.connector.connect(
            host='host.docker.internal',
            user='root',
            passwd='122877',
            db='sam',
            port=3306
        )
        self.cursor = self.conn.cursor()


    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
        self.cursor.execute(
            "INSERT INTO sample_table (title, email, name) VALUES (%s, %s, %s)",
            (item['title'], item['email'], item['name'])
        )
        return item
