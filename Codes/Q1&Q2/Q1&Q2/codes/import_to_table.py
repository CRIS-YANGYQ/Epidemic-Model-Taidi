import pymysql


def each_file():
    sql = '''LOAD DATA INFILE 'person_info.csv' 
            INTO TABLE person_info
            FIELDS TERMINATED BY ','
            ENCLOSED BY ','
            LINES TERMINATED BY '\n'
            IGNORE 1 ROWS;
            '''
    db.cursor().execute(sql)

    sql = '''LOAD DATA INFILE 'venue_info.csv' 
                INTO TABLE venue_info
                FIELDS TERMINATED BY ','
                ENCLOSED BY ','
                LINES TERMINATED BY '\n'
                IGNORE 1 ROWS;
                '''
    db.cursor().execute(sql)

    sql = '''LOAD DATA INFILE 'personal_report_info.csv' 
            INTO TABLE personal_report_info
            FIELDS TERMINATED BY ','
            ENCLOSED BY ','
            LINES TERMINATED BY '\n'
            IGNORE 1 ROWS;
            '''
    db.cursor().execute(sql)

    sql = '''LOAD DATA INFILE 'acid_sample_info.csv'
            INTO TABLE na_sample_info
            FIELDS TERMINATED BY ','
            ENCLOSED BY ','
            LINES TERMINATED BY '\n'
            IGNORE 1 ROWS;
            '''
    db.cursor().execute(sql)

    sql = '''LOAD DATA INFILE 'vaccination_info.csv' 
            INTO TABLE vaccination_info
            FIELDS TERMINATED BY ','
            ENCLOSED BY ','
            LINES TERMINATED BY '\n'
            IGNORE 1 ROWS;
            '''
    db.cursor().execute(sql)


if __name__ == '__main__':
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='ff2017',
        charset='utf8',
        database='tedi_data'
    )
    each_file()
    db.close()
