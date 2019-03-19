from flask import Flask, render_template, url_for, send_from_directory, request
from flaskext.mysql import MySQL
app = Flask(__name__, static_url_path='')

mysql = MySQL()
# MySQL config
app.config['MYSQL_DATABASE_USER'] = 'dbuser'
app.config['MYSQL_DATABASE_PASSWORD'] = 'wwu1892'
app.config['MYSQL_DATABASE_DB'] = 'wwu'
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
    cursor.execute("SELECT * FROM schedule WHERE (STRM LIKE %{0}% OR CLASS_NBR LIKE %{0}% OR ACAD_ORG LIKE %{0}% OR WWU_ACAD_ORG_DESCR LIKE %{0}% OR SUBJECT LIKE %{0}% OR CATALOG_NBR LIKE %{0}% OR CLASS_SECTION LIKE %{0}% OR CLASS_TITLE LIKE %{0}% OR UNITS LIKE %{0}% OR ENRL_TOT LIKE %{0}% OR ROOM LIKE %{0}% OR MTG_TIME LIKE %{0}% OR MTG_DAYS LIKE %{0}%)".format(query))
    data = cursor.fetchall()
    return jsonify(data)
    #return render_template('index.html', results = data)

@app.route('/node_modules/leaflet/dist/<path:path>')
def send_module(path):
    return send_from_directory('node_modules/leaflet/dist/', path)

if __name__ == '__main__':
    app.run(debug=True)