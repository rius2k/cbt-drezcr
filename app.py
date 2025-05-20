from settings import *
from flask import * #type:ignore

app, app_config = Flask(__name__), loadAppConfig() #type:ignore

@app.route('/')
def index():
    return render_template('index.html', navcontent=str(getNav())) #type:ignore


#lógica

def getNav():
    return ''.join(
        f'<a href="/{key}"><button>{key}</button></a>'
        for key in app_config.get('endpoint-map', {})
    )

if __name__:
    mapApplications(app)
    app.run(debug=True, host='127.0.0.1', port=5000) 