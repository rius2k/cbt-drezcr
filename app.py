from settings import *
from flask import * #type:ignore

app, app_config = Flask(__name__), loadAppConfig() #type:ignore

@app.route('/', methods=["GET"])
def index():
    return render_template(
        'index.html',
        DefaultCSS=loadDefaultCSS(),
        DefaultMetatags=loadDefaultMetatags(),
        PageTitle=SetPageTitle(f'Inicio ~ {app_config['site-description']['after-pagetitle']}'),
        PageDescription=SetPageDescription(app_config["site-description"]["description"]),
        JsFX=SetJSInit(),
        PageHeader=SetPageHeader(),
        PageFooter=SetPageFooter(),
        PageContentTitle=SetPageContentTitle('Inicio')
    )

"""@app.route('/getTheme', methods=["POST"])
def getTheme():
    data = request.get_json()
    return str(SetTheme(data))
def SetTheme(data):
    zona = data.get("timezone", "UTC")  # fallback por si acaso. Se puede usar para opciones de fingerprint
    dt = datetime.now(ZoneInfo(zona))
    hora = dt.hour
    print(f"La hora local del cliente, es {hora}")
    if 6 <= hora < 18:data_theme = "white"
    else:data_theme = "dark"
    return data_theme
"""

if __name__:
    mapApplications(app)
    app.run(debug=True, host=app_config['host'], port=app_config['port']) 