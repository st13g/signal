from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def save_value():
    value = request.form['value']
    with open('value.txt', 'w') as f:
        f.write(value)
    return render_template('index.html', message='Value saved')

if __name__ == '__main__':
    app.run(debug=False)
