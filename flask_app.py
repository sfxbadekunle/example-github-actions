# This file is used for hosting at PythonAnywhere.com
# 'app' must point to a Flask Application object.

from app import boot_application

app=boot_application()

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port=3000)