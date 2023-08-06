from clapton.base import get_input_type
from clapton.templates import get_template

import connexion
from flask import redirect
import os
cwd = os.getcwd()


class App():

    def __init__(self, name):
        app = connexion.FlaskApp(name, specification_dir= cwd)
        template_type = get_input_type()
        template_file = '{}.yml'.format(template_type)
        with open(template_file, 'w') as f:
            template = get_template(template_type)
            f.write(template())

        app.add_api(template_file)

        @app.route('/')
        def redirect_to_ui():
            return redirect('./ui', code=302)

        self.app = app

    def run(self):
        self.app.run()