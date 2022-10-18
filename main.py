from flask import Flask, render_template, Request, Response, jsonify
# AKIAVFEYRXZ5EOZ5KTFQ 
# PwUlJB2/Q1Qcx2SyLNuYsSt4xIBKY6EIYuJb0TVk
# https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html

app = Flask(__name__)

## TO DO -- TWITTER CREDENTIALS (AUSTIN BELCAK), CSS FRAMEWORK

@app.route("/")
def index():
    return render_template("index.html")



if __name__ == '__main__':
   app.run()