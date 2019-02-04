from flask import Flask, render_template, url_for, send_from_directory
app = Flask(__name__, static_url_path='')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/node_modules/leaflet/dist/<path:path>')
def send_module(path):
    return send_from_directory('node_modules/leaflet/dist/', path)

@app.route('/assets/<path:path>')
def send_asset(path):
    return send_from_directory('assets/', path)

if __name__ == '__main__':
    app.run(debug=True)