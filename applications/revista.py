from flask import * #type: ignore
from settings import *

app_title = str(os.path.basename(__file__).replace('.py', '')).capitalize()

bp, app_config = Blueprint(app_title, __name__), loadAppConfig() #type:ignore

@bp.route('/')
def index():
    return render_template(
        'index.html',
        DefaultCSS=loadDefaultCSS(),
        DefaultMetatags=loadDefaultMetatags(),
        PageTitle=SetPageTitle(f'{app_title} ~ {app_config['site-description']['after-pagetitle']}'),
        PageDescription=SetPageDescription(app_config["site-description"]["description"]),
        JsFX=SetJSInit(),
        PageHeader=SetPageHeader(),
        PageFooter=SetPageFooter(),
        PageContentTitle=SetPageContentTitle(app_title)
    )