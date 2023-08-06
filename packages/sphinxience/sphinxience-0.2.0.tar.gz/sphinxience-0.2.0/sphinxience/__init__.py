__version__ = '0.1.2'

__all__ = []

import os.path

SUBMODULES = ["skip"]

def update_context(app, pagename, templatename, context, doctree):
    context["sphinxience_version"] = __version__

def setup(app):
    app.require_sphinx('1.7')

    app.add_html_theme('sphinxience',
        os.path.abspath(os.path.dirname(__file__)))

    app.connect("html-page-context", update_context)

    for submodule in SUBMODULES:
        app.setup_extension("sphinxience.{}".format(submodule))

    return {'version': '0.1.2', "parallel_read_safe": True}