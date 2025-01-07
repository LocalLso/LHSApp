import logging
from flask import Flask
from extensions import db, login_manager
from flask_migrate import Migrate
from users.routes import users_bp
from assessments.routes import assessments_bp
from analytics.routes import analytics_bp

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'users.login'
migrate = Migrate(app, db)  # Initialize Flask-Migrate

app.register_blueprint(users_bp)
app.register_blueprint(assessments_bp)
app.register_blueprint(analytics_bp)

if __name__ == '__main__':
    app.run(debug=True)

