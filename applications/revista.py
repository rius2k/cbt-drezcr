from flask import * #type: ignore
from settings import *
bp, app_config = Blueprint('revista', __name__), loadAppConfig() #type:ignore


@bp.route('/')
def index():
    return 'Nuestra revista'