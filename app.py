from flask import Flask,render_template, request, send_file

from scripts.Regexer import regexer
app = Flask(__name__)

regexer()


@app.route('/download/sha1.csv')
def csv_return():
    return send_file('sha1.csv')


@app.route('/download/sha1.txt')
def sha1txt():
    return send_file('./Signitures/Checkpoint/sha1.csv')

@app.route('/test')
def testing():
    ##share the sha1 : ca9dcd197d0061abcf8537a9e7a8c9c64f799b53 wich is in first line sha
    return send_file('iocs_check.csv')


if __name__ == '__main__':
    app.run()
