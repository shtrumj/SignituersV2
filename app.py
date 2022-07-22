from flask import Flask,render_template, request

from scripts.Regexer import regexer
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    ipv4,sha1_hashes,sha256_hashes,domains = regexer()
    return render_template('home.html', ipv4 = ipv4)





if __name__ == '__main__':
    app.run()
