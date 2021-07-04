# https://flask.palletsprojects.com/en/2.0.x/config/#configuring-from-files
# https://exploreflask.com/en/latest/configuration.html

from app import app
import os
app.run(host='0.0.0.0', port=5000, debug=True)
