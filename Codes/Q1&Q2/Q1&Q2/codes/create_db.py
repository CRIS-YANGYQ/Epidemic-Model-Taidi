import pymysql
import cryptography


def create_base():
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='ff2017',
        charset='utf8'
    )
    cursor = db.cursor()
    try:
        cursor.execute("CREATE DATABASE tedi_data")
    except ValueError:
        print("database desired already exists!")

    print("connected !")


def main():
    create_base()


if __name__ == '__main__':
    main()
