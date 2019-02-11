#!/user/bin/python
#-*-coding:utf-8-*-
from flask import Flask, Response, make_response, url_for
import sys

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)

@app.route('/board', methods = ['GET'])
def board_list_get():
    return ""

@app.route('/board', methods = ['POST'])
def board_list_post():
    return ""

@app.route("/user/<uname>")
def IoT_user_name(uname):
    return "User name : %s" %uname

@app.route("/user/<int:num_id>")
def IoT_user_number_id(num_id):
    return "ID Number : %d" %num_id

@app.route("/log")
def IoT_logging_test():
    test_value = 20190211
    app.logger.debug("디버깅 시행 중")
    app.logger.warning(str(test_value) + "=====")
    app.logger.error("에러발생")
    return "로거 끝"

@app.route("/")
def IoT_http_prepost_response():
	return "<img src=" + url_for("static", filename = "1.png") + ">"

if __name__ == "__main__":
	app.run(host = "0.0.0.0")