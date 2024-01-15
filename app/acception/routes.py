from flask import request, Blueprint,jsonify
from app import db  
from sqlalchemy import text
import random;


acception_bp = Blueprint('acception',__name__)



