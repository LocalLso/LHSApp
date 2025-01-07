from flask import Blueprint, render_template
from assessments.models import Assessment, Grade

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/analytics')
def analytics():
    assessments = Assessment.query.all()
    grades = Grade.query.all()
    # Implement your analytics logic here
    return render_template('analytics.html', assessments=assessments, grades=grades)

