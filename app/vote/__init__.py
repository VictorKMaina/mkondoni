from flask import Blueprint

vote = Blueprint("vote", __name__)

from . import views