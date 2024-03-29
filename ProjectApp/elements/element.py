class Element:
    def __init__(self, element_id, element_order, element, element_criteria, competency_id):
        if not isinstance (element_id, int) and element_id != None:
            raise Exception ("element id must be an int")
        if not isinstance (element_order, int):
            raise Exception ("element_order not int")
        if not isinstance (element, str):
            raise Exception ("element not str")
        if not isinstance (element_criteria, str):
            raise Exception ("element_criteria not str")
        if not isinstance (competency_id, str):
            raise Exception ("competency_id not str")
        self.element_id = element_id
        self.element_order = element_order
        self.element = element
        self.element_criteria = element_criteria
        self.competency_id = competency_id
        
    def __repr__(self):
        return f'Element({self.element_id}, {self.element_order}, {self.element}, {self.element_criteria}, {self.competency_id})'
    
    def __str__(self):
        return f'{self.element_id} {self.element_order} {self.element_order} {self.element} {self.element_criteria} {self.competency_id}'
    
    def to_json(self):
        return self.__dict__
    
    def from_json(element_str):
        if not isinstance (element_str, dict):
            raise Exception ("Expected type dict")
        return Element(element_str['element_id'], element_str['element_order'], element_str['element'], element_str['element_criteria'], element_str['competency_id'])
        
from flask_wtf import FlaskForm 
from wtforms import StringField
from wtforms.validators import DataRequired, Length
class ElementForm(FlaskForm):
    element = StringField('Element', validators=[DataRequired(), Length(min=5, max=250)])
    element_criteria = StringField('Element criteria', validators=[DataRequired(), Length(min=5, max=250)])
        
