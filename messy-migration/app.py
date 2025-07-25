from flask import Flask
from routes.user_routes import user_routes

app = Flask(__name__)
app.register_blueprint(user_routes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009, debug=True)
