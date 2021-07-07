from flask_assets import Bundle, Environment
from .. import app

# https://exploreflask.com/en/latest/static.html
bundles = {
    'css': Bundle(
        'css/style.css',
        filters='cssmin',
        output='style.minpkt.css'
    ),
    'htmx': Bundle('js/lib/htmx.1.4.1.min.js.gz')
}

assets = Environment(app)
assets.register(bundles)
