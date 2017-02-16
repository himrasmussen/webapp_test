from flask import Flask
application = Flask(__name__)
application.config.from_object('config')

from application import views

if __name__ == "__main__":
    application.run()
