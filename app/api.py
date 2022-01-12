from flask_appbuilder import ModelRestApi, BaseView, has_access, expose
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.api import BaseApi, expose
from flask_appbuilder.models.sqla.filters import FilterStartsWith, FilterEqual
from flask_appbuilder.models.filters import BaseFilter
from sqlalchemy import or_
from . import appbuilder
from .models import Choice, Quiz, Question


class QuizModelApi(ModelRestApi):
    
    resource_name = "quiz"
    datamodel = SQLAInterface(Quiz)
    allow_browser_login = True
    list_columns = [ "id", "name", "category.name"]
    show_columns = ["id", "name", "category.name"]


appbuilder.add_api(QuizModelApi)

class Questionfilter(BaseFilter): 
    name = "Question filter"
    arg_name = "qbq"

    def apply(self, query, value):
        return query.filter(
            or_(
                Question.quiz_id == value,
            )
        )

class QuestionModelApi(ModelRestApi):
   resource_name = "questions"
   datamodel = SQLAInterface(Question)
   allow_browser_login = True
   list_columns = ["id", "questionTitle", "explanation", "quiz.id", "resource"]
   search_filters = {"questionTitle": [Questionfilter]}
   openapi_spec_methods = {
        "get_list": {
            "get": {
                "description": "Get all questions by quiz id, filter and pagination",
            }
        }
    }



class ChoiceFilter(BaseFilter):
    name = "Custom Filter"
    arg_name = "cbq"

    def apply(self, query, value):
        return query.filter(
            or_(
                Choice.question_id == value,
            )
        )
class ChoiceModelApi(ModelRestApi): 
    resource_name = "choices"
    datamodel = SQLAInterface(Choice)
    allow_browser_login = True
    search_filters = {"choice": [ChoiceFilter]}
    list_columns = ["id", "choice", "is_right_choice"]
    openapi_spec_methods = {
        "get_list": {
            "get": {
                "description": "Get all choices by question id, filter and pagination",
            }
        }
    }


appbuilder.add_api(QuestionModelApi)
appbuilder.add_api(ChoiceModelApi)

class AdminAppView(BaseView):
    @expose('/<string:param1>')
    @has_access
    def render_react(self, param1):
        self.update_redirect()
        return self.render_template('admin.html',
                                    param1 = param1)


appbuilder.add_view_no_menu(AdminAppView)
appbuilder.add_link("Admin", href='/adminappview/home', category='Quiz')

