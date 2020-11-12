import json
from chalice import Chalice
from chalicelib import sql_service
from chalicelib import boto_rds_conn
from chalicelib import SqlQueries

app = Chalice(app_name='my_app_aurora')

columns = ["shoetype", "color"]

@app.route('/psycopg')
def index():
    return sql_service.select_all()


@app.route('/boto')
def boto_conn():

    cnx = boto_rds_conn.BotoPostgresqlDB()
    response = cnx.execute_query(SqlQueries.SELECT_ALL)
    f_res = []
    for record in response['records']:
        res = []
        for rec in record:
            for k, v in rec.items():
                res.append(v)
        values = {columns[i]: res[i] for i in range(len(columns))}
        
        f_res.append(values)

    print("Final Response: %s", response)
    return json.dumps(f_res)
