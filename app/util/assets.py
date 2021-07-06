from flask_assets import Bundle, Environment
from .. import app

# https://exploreflask.com/en/latest/static.html
bundles = {
    'css': Bundle('style.css'),
    'htmx': Bundle('htmx.1.4.1.min.js.gz')
}

assets = Environment(app)
assets.register(bundles)
