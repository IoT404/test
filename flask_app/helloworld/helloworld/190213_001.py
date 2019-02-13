#!/user/bin/python
#-*-coding:utf-8-*-
from flask import Flask, Response, make_response, url_for, render_template, request, session, redirect
from bs4 import BeautifulSoup
from subprocess import PIPE, Popen 
import requests
import sys
import psutil
import RPi.GPIO as GPIO

LedPin = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(LedPin, GPIO.OUT)

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
app.debug = True

@app.route('/board', methods = ['GET'])
def board_list_get():
    return ""

@app.route('/board', methods = ['POST'])
def board_list_post():
    return ""

@app.route("/info")
def iot_sys_info():
#==============================================================================
    cpu_temp            = iot_measure_temp()
    cpu_percent         = psutil.cpu_percent() 
    cpu_count           = psutil.cpu_count()
#==============================================================================
    memory              = psutil.virtual_memory()
    mem_total           = memory.total
    mem_percent         = memory.percent
#==============================================================================
    hd_disk             = psutil.disk_usage("/")
    disk_percent        = hd_disk.percent
#==============================================================================
    iot_sys_info_dict   = {
                            "CPU 코어 갯수"       :cpu_count,
                            "디스크 사용율"       :disk_percent,
                            "메모리 사용율"       :mem_percent,
                            "전체 메모리"         :mem_total,
                            "CPU 사용율"          :cpu_percent,
                            "CPU 온도"            :cpu_temp,
                            }
    return render_template('hw_info.html', hw_info = iot_sys_info_dict)

@app.route("/led/<iot_state>")
def led_onoff(iot_state):
    if "on" == iot_state:
        GPIO.output(LedPin, GPIO.HIGH)
    if "off" == iot_state:
        GPIO.output(LedPin, GPIO.LOW)
    if "toggle" == iot_state:
        GPIO.output(LedPin, not GPIO.input(LedPin))
    return iot_sys_info()

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
	app.run(host = "192.168.0.210")