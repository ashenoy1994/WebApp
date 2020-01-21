from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('Login_v17/index.html')

@app.route('/search')
def search():
    return render_template('Login_v17/search.html')

if __name__ == '__main__':
    app.run(debug=True)
