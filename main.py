from flask import Flask,render_template
from get_api import get_data
app = Flask('app')

@app.route('/')
def hello_world():
  data,burgerdata = get_data() # calling the get_data()
  return render_template('index.html',data = data, burgerdata = burgerdata ) #send burger data to index.html

app.run(host='0.0.0.0', port=8080)