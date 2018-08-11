from flask import Flask, render_template, Blueprint
from blueprints.bdocker import bdocker
from blueprints.bjenkis import jenkins

app = Flask(__name__)
app.register_blueprint(bdocker)
app.register_blueprint(jenkins)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)