from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! My first Python website"

app.run(debug=True)














