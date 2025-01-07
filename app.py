from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'

from users.routes import users_bp
from assessments.routes import assessments_bp
from analytics.routes import analytics_bp

app.register_blueprint(users_bp)
app.register_blueprint(assessments_bp)
app.register_blueprint(analytics_bp)

if __name__ == '__main__':
    app.run(debug=True)

