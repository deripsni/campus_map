from flask import Flask, render_template, url_for, send_from_directory, request, jsonify
from flaskext.mysql import MySQL
from flask_cors import CORS
app = Flask(__name__, static_url_path='')
CORS(app)

mysql = MySQL()
# MySQL config
app.config['MYSQL_DATABASE_USER'] = 'dbuser'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Test1234'
app.config['MYSQL_DATABASE_DB'] = 'WWU'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT ROOM FROM schedule WHERE ROOM LIKE '%{0}%'".format(query)) # STRM LIKE %{0}% OR CLASS_NBR LIKE %{0}% OR ACAD_ORG LIKE %{0}% OR WWU_ACAD_ORG_DESCR LIKE %{0}% OR SUBJECT LIKE %{0}% OR CATALOG_NBR LIKE %{0}% OR CLASS_SECTION LIKE %{0}% OR CLASS_TITLE LIKE %{0}% OR UNITS LIKE %{0}% OR ENRL_TOT LIKE %{0}% OR MTG_TIME LIKE %{0}% OR MTG_DAYS LIKE %{0}%".format(query))
    data = cursor.fetchall()
    return jsonify(data)

@app.route('/locate', methods=['GET'])
def locate():
    query = request.args.get('q')
    cursor = conn.cursor()
    cursor.execute("SELECT X_COORD, Y_COORD FROM classrooms WHERE ROOM LIKE '%{0}%'".format(query)) # STRM LIKE %{0}% OR CLASS_NBR LIKE %{0}% OR ACAD_ORG LIKE %{0}% OR WWU_ACAD_ORG_DESCR LIKE %{0}% OR SUBJECT LIKE %{0}% OR CATALOG_NBR LIKE %{0}% OR CLASS_SECTION LIKE %{0}% OR CLASS_TITLE LIKE %{0}% OR UNITS LIKE %{0}% OR ENRL_TOT LIKE %{0}% OR MTG_TIME LIKE %{0}% OR MTG_DAYS LIKE %{0}%".format(query))
    data = cursor.fetchall()
    return jsonify(data)

@app.route('/node_modules/leaflet/dist/<path:path>')
def send_module(path):
    return send_from_directory('node_modules/leaflet/dist/', path)

if __name__ == '__main__':
    app.run(debug=True)
