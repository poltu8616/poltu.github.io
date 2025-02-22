from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    return f'Name: {name}, Email: {email}'
  else:
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
