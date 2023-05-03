from flask import Blueprint, abort, render_template, redirect, url_for, flash, request
from .courses_element import CourseElement, CourseElementForm
from ..dbmanager import get_db

bp = Blueprint("courses_elements", __name__, url_prefix="/courses-elements")

@bp.route("/", methods = ["GET", "POST"])
def list_courses_elements():
    form = CourseElementForm()
    if request.method == "POST" and form.validate_on_submit():
        new_course_element = CourseElement(form.course_id.data, int(form.element_id.data), float(form.hours.data))
        try:
            get_db().add_courses_element(new_course_element)
        except ValueError as e:
            flash(str(e))
    return render_template("courses_elements.html", courses_elements = get_db().get_elements_and_course_ids_as_tuples(), form = form, courses = get_db().get_courses_with_sum_hours_from_elements())
    
#display all elements for a given course
@bp.route("course/<element_id>/")
def get_course_element_id(element_id):
    pass
    
#display a course for a given element_id
@bp.route("elements/<course_id>/")
def get_course_course_id(course_id):
    pass