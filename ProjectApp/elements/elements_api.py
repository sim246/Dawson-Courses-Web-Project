from flask import Blueprint, abort, request, jsonify, flash
from .element import Element
from ..dbmanager import get_db
bp = Blueprint("element-api", __name__, url_prefix="/api/elements")

@bp.route("/", methods = ["GET", "POST"])
def post_elements():
    page_num = 1
    if request.method == "POST":
        json_element = request.json
        if json_element:
            try:
                element = Element.from_json(json_element)
                get_db().add_element(element), 201 
                flash("element added succesfully!")
                # display the added element
            except Exception as e:
                flash("could not add element")
                abort(409)
    elif request.method == "GET":
        if request.args:
            page = request.args.get("page")
            try:
                if page:
                    page_num = int(page)
            except:
                flash("element with that id not found")
                abort(404)
    try:            
        elements, prev_page, next_page = get_db().get_elements(page_num = page_num, page_size = 10)            
        json_elements = {
            "previous_page" : prev_page,
            "next_page": next_page,
            "results:" : [element.to_json() for element in elements]}
        return jsonify(json_elements)
    except:
        flash("could not fetch elements")
        abort(404)
        
@bp.route("/<int:element_id>", methods = [ "DELETE", "PUT", "GET"])
def modify_element(element_id):
    if request.method == "PUT":
        json_element = request.json
        if json_element:
            try:
                element = Element.from_json(json_element)
                get_db().add_element(element), 201 
                flash("element added succesfully!")
                # display the added element
            except Exception as e:
                flash("could not add element")
                abort(409)
    elif request.method == "GET":    
        try:
            element = get_db().get_element(int(element_id))
            return element.to_json(), 200
        except:
            flash("Invalid ID, make sure url is correct")
            abort(404)
   