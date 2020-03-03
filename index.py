from flask import Flask
from flask import render_template
from baiduspider import getBdMsg
from flask import request

# Flask(__name__).run()
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weibiaobiao")
def demo():
    return "Hello Calloway - python!"

@app.route("/s")
def search():
    keyword = request.args.get("wd")
    text = getBdMsg(keyword)
    return text

if __name__ == "__main__":
    app.run()

