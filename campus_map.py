from flask import Flask, render_template, url_for, send_from_directory
from flaskext.mysql import MySQL
app = Flask(__name__, static_url_path='')

mysql = MySQL()
# MySQL config
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'wwu1892'
app.config['MYSQL_DATABASE_DB'] = 'wwu'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/node_modules/leaflet/dist/<path:path>')
def send_module(path):
    return send_from_directory('node_modules/leaflet/dist/', path)

@app.route('/search', methods=['GET'])
def search():
    request.GET.get('q')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM schedule")
    data = cursor.fetchall()
    return render_template('index.html', results = data)

if __name__ == '__main__':
    app.run(debug=True)