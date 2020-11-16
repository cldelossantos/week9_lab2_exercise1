from flask import Flask, render_template, request

# from flask import request

app = Flask(__name__)

app.config['SECRET_KEY'] = b'\xca\x8e7\xb57\x94\xc3\x07\x13\xfa\xf5\xf8\xe0=6\x02<*gDRZ\xbfD'
@app.route('/sqrt/<number>')
def sqrt(number):
    if number.isnumeric():
        sqrt = int(number) ** 0.5
        return render_template('sqrt.html', sqrt=sqrt)

@app.route('/user/<username>')
def show_message(username):
    return render_template('user.html', user=username)

@app.route('/info')
def info():
    method = request.method
    return render_template('info.html', method=method)

if __name__ == '__main__':
    app.run(debug=True)