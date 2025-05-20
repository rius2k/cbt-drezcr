from flask import * #type: ignore
from settings import *
bp, app_config = Blueprint('nosotros', __name__), loadAppConfig() #type:ignore

@bp.route('/')
def index():
    return 'Sobre nosotros'