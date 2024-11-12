from apachelogs import LogParser
import pymysql.cursors

def connect(user, password, db):
    con =   pymysql.connect(host='localhost',
            user=user,
            password=password,
            database=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)
    return con

def write_to_db(con, filename):
    fo = open(filename, 'rt')
    parser = LogParser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")
    for line in fo:
        try:
            parser.parse(line)
            print(str(entry.request_time), entry.request_line)
            rl = entry.request_line.split(" ")
            print(rl[0].strip("/"))
            # Create a new record
            with con.cursor() as cursor:
                sql = "INSERT INTO `apache_log` (`useragent`, `time`, `method`, `page`) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (entry.headers_in["User-Agent"], entry.request_time.strftime("%Y-%m-%d %H:%M:%S"), rl[0], rl[1]))
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                con.commit()
        except Exception as e:
            print(e)