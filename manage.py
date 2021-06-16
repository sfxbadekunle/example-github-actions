from flask_script import Manager
from app import create_app


manger = Manager(create_app())

if __name__ == "__main__":
    manger.run()