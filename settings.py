import json, importlib, os
from datetime import datetime
from zoneinfo import ZoneInfo 
def mapApplications(app):
    with open('config.json', 'r') as f:_config = json.load(f)
    endpoint_map = _config.get('endpoint-map', {})
    for url_prefix, import_path in endpoint_map.items():
        import_path = import_path[0]
        *module_parts, bp_var = import_path.split('.')
        module_str = '.'.join(module_parts)
        try:
            module = importlib.import_module(module_str)
            blueprint = getattr(module, bp_var)
            app.register_blueprint(blueprint, url_prefix=f'/{url_prefix}')
            print(f"cargado correctamente {url_prefix} ← {import_path}")
        except Exception as e:print(f"error en {import_path}: {e}")

def loadAppConfig():
    with open('config.json', 'r') as jsonfile:return json.load(jsonfile)
def loadDefaultCSS():return """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/static/global.css">
<link rel="stylesheet" href="/static/globalresponsive.css">
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" href="/static/favicon.png" type="image/x-png">"""
def SetPageTitle(v):return f"<title>{v}</title>"
def SetPageDescription(v): return f"<meta name='description' content='{v}'/>"
def loadDefaultMetatags():
    cfx = loadAppConfig()
    return f"""<link rel="icon" href="{cfx['site-description']['favicon']}" type="image/x-png"><meta name="robots" content="index, follow"><meta name="author" content="{cfx["site-description"]["author"]}"><meta property="og:type" content="website"><meta property="og:url" content="{cfx["site-description"]["url"]}"><meta property="og:image" content="{cfx["site-description"]["socialmedia-preview"]}">"""
def SetJSInit():
    with open('static/global.js', 'r') as jsreadable:content = jsreadable.read()
    return f"""<script>{content}</script><script src="/static/settings.js"></script>"""
def SetPageHeader():
    with open('templates/header.html', 'r') as htmlheader:content=htmlheader.read()
    #aquí quiero cargar un diccionario, por ejemplo de apartados, hacer el for del diccionario y añadirlos al htmlcontent
    cfx, els = loadAppConfig(), ""
    for key in cfx['endpoint-map']:
        if key == 'solesmetepec':el = f'<a href="/{key}"><button>Soles de Metepec</button></a>'
        else:
            el = f'<a href="/{key}"><button>{key.capitalize()}</button></a>'
        els += el
    content = content.replace("<!--NAVITEMS-->", els)
    return str(content)
def SetPageFooter():
    with open('templates/footer.html', 'r') as htmlfooter:content=htmlfooter.read()
    return str(content)
def SetPageContentTitle(v):
    return f"""<div id="title"><label class="h1">{v}</label></div>"""