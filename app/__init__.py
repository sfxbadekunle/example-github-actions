from flask import Flask

def boot_application():
    app = Flask(__name__)


    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    return app