from flask import Flask,render_template, request, send_file

from scripts.Regexer import regexer
app = Flask(__name__)

regexer()


@app.route('/download/sha1.csv')
def csv_return():
    return send_file('Signitures/Checkpoint/sha1.csv')

@app.route('/download/sha256.csv')
def sha256_return():
    return send_file('Signitures/Checkpoint/sha256.csv')

@app.route('/download/ip_addresses.csv')
def ip_return():
    return send_file('Signitures/Checkpoint/ip_addresses.csv')


@app.route('/test')
def testing():
    return send_file('iocs_check.csv')


if __name__ == '__main__':
    app.run()
