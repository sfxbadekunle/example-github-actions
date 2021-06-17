from flask_script import Manager
from app import boot_application


manger = Manager(boot_application())

if __name__ == "__main__":
    manger.run()