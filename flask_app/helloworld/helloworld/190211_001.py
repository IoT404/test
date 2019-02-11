from flask import Flask, Response, make_response, url_for

app = Flask(__name__)

@app.route('/board', methods = ['GET'])
def board_list_get():
    return""

@app.route('/board', methods = ['POST'])
def board_list_post():
    return""

@app.route("/")
def IoT_http_prepost_response():
	return "<img src=" + url_for("static", filename = "1.png") + ">"

if __name__ == "__main__":
	app.run(host = "0.0.0.0")