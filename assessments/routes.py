from flask import Blueprint, render_template, request, redirect, url_for, session
from extensions import db
from assessments.models import Assessment, Grade
from assessments.forms import AssessmentForm, AnswerForm
from assessments.grading import grade_assessment
from flask_login import current_user, login_required

assessments_bp = Blueprint('assessments', __name__)

@assessments_bp.route('/dashboard')
@login_required
def dashboard():
    assessments = Assessment.query.all()
    return render_template('dashboard.html', assessments=assessments)

@assessments_bp.route('/add_assessment', methods=['GET', 'POST'])
@login_required
def add_assessment():
    if current_user.role != 'teacher':
        return redirect(url_for('assessments.dashboard'))
    
    form = AssessmentForm()
    if form.validate_on_submit():
        new_assessment = Assessment(question=form.question.data, answer=form.answer.data)
        db.session.add(new_assessment)
        db.session.commit()
        return redirect(url_for('assessments.dashboard'))
    return render_template('add_assessment.html', form=form)

@assessments_bp.route('/delete_assessment/<int:assessment_id>')
@login_required
def delete_assessment(assessment_id):
    if current_user.role != 'teacher':
        return redirect(url_for('assessments.dashboard'))
    
    assessment = Assessment.query.get_or_404(assessment_id)
    db.session.delete(assessment)
    db.session.commit()
    return redirect(url_for('assessments.dashboard'))

@assessments_bp.route('/take_assessment/<int:assessment_id>', methods=['GET', 'POST'])
@login_required
def take_assessment(assessment_id):
    if current_user.role != 'student':
        return redirect(url_for('assessments.dashboard'))
    
    assessment = Assessment.query.get_or_404(assessment_id)
    form = AnswerForm()
    if form.validate_on_submit():
        score = grade_assessment(form.answer.data, assessment.answer)
        new_grade = Grade(username=current_user.username, assessment_id=assessment.id, score=score)
        db.session.add(new_grade)
        db.session.commit()
        return redirect(url_for('assessments.grades'))
    return render_template('take_assessment.html', assessment=assessment, form=form)

@assessments_bp.route('/grades')
@login_required
def grades():
    if current_user.role != 'student':
        return redirect(url_for('assessments.dashboard'))
    
    user_grades = Grade.query.filter_by(username=current_user.username).all()
    return render_template('grades.html', grades=user_grades)

@assessments_bp.route('/view_assessment/<int:assessment_id>')
@login_required
def view_assessment(assessment_id):
    assessment = Assessment.query.get_or_404(assessment_id)
    return render_template('view_assessment.html', assessment=assessment)

