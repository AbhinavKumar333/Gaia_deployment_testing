from flask import Flask
from Controller.view import utility

app = Flask(__name__)
app.register_blueprint(utility)

if __name__ == "__main__":
    app.run(debug=True)