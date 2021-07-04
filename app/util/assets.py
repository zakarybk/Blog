from flask_assets import Bundle, Environment
from .. import app

# https://exploreflask.com/en/latest/static.html
bundles = {
    'css': Bundle('styles.css')
}

assets = Environment(app)
assets.register(bundles)
