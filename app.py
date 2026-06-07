from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/artistas')
def artistas():
    return render_template('artistas.html')

if __name__ == '__main__':
    app.run(debug=True)
