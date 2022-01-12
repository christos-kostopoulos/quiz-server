import datetime
from typing import Text

from flask_appbuilder import Model
from flask_appbuilder.models.decorators import renders
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Column, Text, Boolean
from sqlalchemy.orm import relation, relationship
from flask import Markup


mindate = datetime.date(datetime.MINYEAR, 1, 1)

class Quiz(Model): 
  id = Column(Integer, primary_key=True)
  name = Column(String(50), nullable=False)
  category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
  category = relationship("Category")

  def __repr__(self):
        return self.name

class Category(Model): 
  id = Column(Integer, primary_key=True)
  name = Column(String(50), unique=True, nullable=False)
  
  def __repr__(self):
      return self.name

class Question(Model): 
  id = Column(Integer, primary_key=True)
  questionTitle = Column(Text)
  quiz_id = Column(Integer, ForeignKey("quiz.id"), nullable=False)
  quiz = relationship("Quiz")
  explanation = Column(Text)
  resource =  name = Column(String(200))
  # @renders('questionTitle')
  # def latex_field(self):
  #   # will render this columns as bold on ListWidget
  #   return Markup('<b>' + self.questionTitle + '</b>')
  
  def __repr__(self):
    return self.questionTitle
  
class Choice(Model): 
  id = Column(Integer, primary_key=True)
  choice = Column(Text)
  is_right_choice =  Column(Boolean, default=False) 
  question_id = Column(Integer, ForeignKey("question.id"), nullable=False)
  question = relationship("Question")

  def __repr__(self):
    return self.choice
