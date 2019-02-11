from flask import Flask

app = Flask(__name__)

@app.route("/")
def http_prepost_response():
    return "<img src=" + url_for("static", filename = "1.jpg") + ">"

@app.route('/board')
def board_list():
    return "<img src=\"https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png\">"

if __name__ == "__main__":
    app.run(host = "0.0.0.0")