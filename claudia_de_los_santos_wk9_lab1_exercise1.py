from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = b'0\x1b\xc8\x12\xa8\x9e\x8b\x0f{X,LEx\x97mE5S\xcf\xfc\xefI\xf1'

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)