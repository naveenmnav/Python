from flask import Flask, render_template, request, jsonify
import mysql.connector as connection

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'INeuron'


@app.route('/', methods=['GET', 'POST'])  # To render Homepage
def home_page():
    return render_template('index.html')


# Testing Connection


def dbConnectionCheck():
    mydb = connection.connect(host=app.config['MYSQL_HOST'], user =app.config['MYSQL_USER'], passwd = app.config['MYSQL_PASSWORD'] )

    cursor = mydb.cursor()
    cursor.execute("SHOW DATABASES")

    res = cursor.fetchall()
    print(res)

@app.route('/create_database', methods=['POST'])
def createDatabase():
    if (request.method == 'POST'):
        DBName =request.json['DBName']
        try:
            mydb = connection.connect(host=app.config['MYSQL_HOST'], user=app.config['MYSQL_USER'],
                                      passwd=app.config['MYSQL_PASSWORD'])
            print("Connection: " + str(mydb.is_connected()))
            cursor = mydb.cursor()
            show_query = 'SHOW DATABASES '
            cursor.execute(show_query)
            res = cursor.fetchall()
            print(res)


            createQuery = 'CREATE DATABASE '+ DBName
            cursor.execute(createQuery)
            result = "Database " + DBName + "is created Successfully"

        except Exception as e:
            mydb.close()
            print("Error: "+str(e))
        return jsonify(result)

@app.route('/create_table', methods=['POST'])
def create_table():
    if (request.method == 'POST'):
        DBName = request.json['DBName']
        table_name = request.json['table_name']
        contents = request.json['column_types']
        try:
            mydb = connection.connect(host=app.config['MYSQL_HOST'], user=app.config['MYSQL_USER'],
                                      passwd=app.config['MYSQL_PASSWORD'])
            cursor = mydb.cursor()
            select_db_query = 'USE '+DBName
            cursor.execute(select_db_query)
            print(f"DB {DBName} selected")
            create_tbl_query = ''
            create_tbl_query = create_tbl_query+str(contents)
            create_table_query = "CREATE TABLE "+table_name+" ( "+ create_tbl_query+" )"

            cursor.execute(create_table_query)
            #print(f"Table {table_name} created successfully")
            result = "Table "+table_name+" created successfully"
            mydb.close()
        except Exception as e:
            mydb.close()
            print(str(e))

        return jsonify(result)




@app.route('/insert_data', methods=['POST'])
def insert_data():
    if (request.method == 'POST'):
        DBName = request.json['DBName']
        table_name = request.json['table_name']
        contents = request.json['query_string']
        try:
            mydb = connection.connect(host=app.config['MYSQL_HOST'], user=app.config['MYSQL_USER'],
                                      passwd=app.config['MYSQL_PASSWORD'])
            cursor = mydb.cursor()
            select_db_query = 'USE '+DBName
            cursor.execute(select_db_query)
            print(f"DB {DBName} selected")
            insert_data_tbl =contents
            print(insert_data_tbl)
            cursor.execute(insert_data_tbl)
            print(f'Data inserted successfully')
            mydb.commit()
            mydb.close()
        except Exception as e:
            mydb.close()
            print(str(e))
        return jsonify('Data inserted successfully')


@app.route('/show_data', methods=['POST'])
def show_data():
    if (request.method == 'POST'):
        DBName = request.json['DBName']
        table_name = request.json['table_name']
        contents = request.json['query_string']
        try:
            mydb = connection.connect(host=app.config['MYSQL_HOST'], user=app.config['MYSQL_USER'],
                                      passwd=app.config['MYSQL_PASSWORD'])
            cursor = mydb.cursor()
            select_db_query = 'USE '+DBName
            cursor.execute(select_db_query)
            print(f"DB {DBName} selected")
            cursor.execute(contents)
            res = []
            for result in cursor.fetchall():
                res.append(result)
            print(f'Data Got successfully')
            mydb.close()

        except Exception as e:
            mydb.close()
            print(str(e))

    return jsonify(res )


@app.route('/show_DB_data', methods=['POST'])
def show_datas():
    if request.method == 'POST':
        DBName = str(request.form['Database'])
        table_name = str(request.form['TableName'])
        contents = str(request.form['Query'])
        try:
            mydb = connection.connect(host=app.config['MYSQL_HOST'], user=app.config['MYSQL_USER'],
                                      passwd=app.config['MYSQL_PASSWORD'])
            cursor = mydb.cursor()
            select_db_query = 'USE '+DBName
            cursor.execute(select_db_query)
            print(f"DB {DBName} selected")
            cursor.execute(contents)
            res = []
            for result in cursor.fetchall():
                res.append(result)
            print(f'Data Got successfully')
            mydb.close()

        except Exception as e:
            mydb.close()
            print(str(e))

        return render_template('result.html', res=res)


if __name__ == '__main__':
    app.run()


#createDatabase('MYSQLDatabase')
#create_table('MYSQLDatabase','TestTable',query_f = 'ID int(10) AUTO_INCREMENT PRIMARY KEY, FirstName varchar(50) , Lastname varchar(50) , email_id varchar(50)')
#insert_data('MYSQLDatabase','TestTable',query_f = "0001, 'Naveen' , 'Kumar', 'test@gmail.com'")