from flask import Blueprint, render_template
from assessments.models import Assessment, Grade
from flask_login import current_user, login_required

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/analytics')
@login_required
def analytics():
    if current_user.role != 'teacher':
        return redirect(url_for('assessments.dashboard'))
    
    assessments = Assessment.query.all()
    grades = Grade.query.all()
    return render_template('analytics.html', assessments=assessments, grades=grades)

