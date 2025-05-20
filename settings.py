import json, importlib

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
