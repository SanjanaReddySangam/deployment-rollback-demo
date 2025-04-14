from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    raise Exception("Oops! Something went wrong in v2")
    return "Hello from Version 2!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

