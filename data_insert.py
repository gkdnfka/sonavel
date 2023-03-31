import config
import pymysql
import csv

from sshtunnel import SSHTunnelForwarder

with SSHTunnelForwarder((config.SERVER_IP, config.SERVER_PORT),
                            ssh_username=config.SSH_USERNAME,
                            ssh_pkey=config.KEY_NAME,
                            remote_bind_address=('127.0.0.1', 3306)) as tunnel:
    with pymysql.connect(
            host='127.0.0.1',  # (local_host)
            user=config.DB_USERNAME,
            passwd=config.DB_PWD,
            db=config.DB_NAME,
            charset='utf8',
            port=tunnel.local_bind_port,
            cursorclass=pymysql.cursors.DictCursor) as conn:
        with conn.cursor() as cur:
            # Class 데이터 우선 삽입.

            for key, value in config.CLASS_CODE.items():
                sql = 'INSERT INTO class (class_code, class_name) VALUES (%s, %s)'
                values = (value, key)
                cur.execute(sql, values)


            #clear_record 삽입.
            with open(config.DATA_FILEPATH, 'r') as file:
                reader = csv.reader(file)
                next(reader)

                for cnt, row in enumerate(reader):
                    sql = 'INSERT INTO clear_records (user1_class, user1_level, user2_class, user2_level, user3_class, user3_level, user4_class, user4_level, clear_time) ' \
                          'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
                    values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    cur.execute(sql, values)
        conn.commit()

