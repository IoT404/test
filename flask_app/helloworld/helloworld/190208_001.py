from flask import Flask

app = Flask(__name__)

@app.route("/")
def http_prepost_response():
    return "/"

@app.before_first_request
def before_first_request():
    print ("before_first_request")

@app.before_request
def before_request():
    print ("before_request")

@app.after_request
def after_request(response):
    print ("after_request")
    return response

@app.teardown_request
def teardown_request(exception):
    print ("teardown_request")

@app.teardown_appcontext
def teardown_appcontext(exception):
    print ("teardown_appcontext")

if __name__ == "__main__":
    app.run(host = "0.0.0.0")