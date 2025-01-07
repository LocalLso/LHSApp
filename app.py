from flask import Flask
from extensions import db, login_manager
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)

app.config.from_object('config.Config')
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'users.login'

from users.routes import users_bp
from assessments.routes import assessments_bp
from analytics.routes import analytics_bp

app.register_blueprint(users_bp)
app.register_blueprint(assessments_bp)
app.register_blueprint(analytics_bp)

if __name__ == '__main__':
    app.run(debug=True)

