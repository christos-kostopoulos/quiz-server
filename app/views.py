import calendar

from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from . import appbuilder, db
from .models import Category, Choice, Quiz, Question
from flask_appbuilder.widgets import (
    ListBlock, ListItem, ListLinkWidget, ListThumbnail, ShowBlockWidget
)


def fill_category():
    try:
        db.session.add(Category(name="Διακριτά μαθηματικά"))
        db.session.add(Category(name="Τεχνολογία λογισμικου"))
        Question.__table__.drop()
        Quiz.__table__.drop()
        db.session.commit()
    except Exception:
        db.session.rollback()

def pretty_month_year(value):
    return calendar.month_name[value.month] + " " + str(value.year)


def pretty_year(value):
    return str(value.year)

class CategoryModelView(ModelView): 
    datamodel = SQLAInterface(Category)
    list_columns = ['id', 'name']

class ChoiceModelView(ModelView): 
    datamodel = SQLAInterface(Choice)
    list_columns = ["id", "choice", "is_right_choice"]

class QuestionModelView(ModelView): 
    datamodel = SQLAInterface(Question)
    list_columns = ["id", "latex_field", 'explanation', 'resource']
    related_views = [ChoiceModelView]
    
    show_template = 'appbuilder/general/model/show_cascade.html'
    edit_template = 'appbuilder/general/model/edit_cascade.html'

class QuizModelView(ModelView):
    datamodel = SQLAInterface(Quiz)
    list_columns = ["category.name", "name" ]
    related_views = [QuestionModelView]
    list_widget = ListBlock
    
    
    

db.create_all()
fill_category()

appbuilder.add_view(
    QuizModelView,
    "Quiz",
    icon="fa-folder-open-o",
    category="Quiz",
    category_icon="fa-envelope",
)

appbuilder.add_view_no_menu(
    QuestionModelView
)

appbuilder.add_view_no_menu(
    ChoiceModelView
)

appbuilder.add_view(CategoryModelView, "Categories", category="Quiz")