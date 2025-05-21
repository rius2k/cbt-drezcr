from flask import * #type: ignore
from settings import *

bp, app_config = Blueprint(str(os.path.basename(__file__).replace('.py', '')).capitalize(), __name__), loadAppConfig() #type:ignore

@bp.route('/')
def index():
    return render_template(
        'index.html',
        DefaultCSS=loadDefaultCSS(),
        DefaultMetatags=loadDefaultMetatags(),
        PageTitle=SetPageTitle(f'{str(os.path.basename(__file__).replace('.py', '')).capitalize()} ~ {app_config['site-description']['after-pagetitle']}'),
        PageDescription=SetPageDescription(app_config["site-description"]["description"]),
        JsFX=SetJSInit(),
        PageHeader=SetPageHeader()
    )