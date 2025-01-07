def grade_assessment(student_answer, correct_answer):
    """
    Compares the student's answer with the correct answer and returns the score.
    The scoring mechanism can be customized as needed.
    """
    # Simple case-insensitive comparison
    if student_answer.strip().lower() == correct_answer.strip().lower():
        return 1.0
    return 0.0

