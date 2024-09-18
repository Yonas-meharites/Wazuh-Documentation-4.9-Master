import os
import sys
from datetime import datetime

# -- Project information -----------------------------------------------------
project = u'Wazuh'
author = u'Wazuh, Inc.'
copyright = u'© ' + str(datetime.now().year) + u' Wazuh, Inc.'

# Path setup
sys.path.insert(0, os.path.abspath('.'))

# Sphinx extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinxcontrib.images',
]

# Paths
templates_path = ['_templates']
# html_static_path = ['_static','images']
html_static_path = ['images']

html_css_files = [
    'css/wazuh-custom.css',         # Your custom HTML CSS
    'fonts/google-fonts.min.css'    # The Google Fonts CSS
]


images_config = {
    'thumbnail_size': (150, 150),  # Thumbnail size
    'default_image_width': '80%',  # Default image width
    'output_dir': '_images',       # Directory for generated thumbnails
}

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'
# Set the custom Pygments style


# html_css_files = ['css/wazuh-custom.css']  # Link to custom CSS

# The master toctree document.
master_doc = 'index'

# HTML theme
# html_theme = 'sphinx_rtd_theme'
html_theme = "furo"


# EPUB settings
epub_title = 'Wazuh-Documentation-4.9'
epub_author = 'Yohannes Iyob Tekle'
epub_publisher = 'Yohannes-Publishers-Private'
epub_copyright = '2024'
epub_identifier = 'unique-identifier'
epub_scheme = '2024-09-17-Version-4.9'
epub_language = 'en'
epub_exclude_files = ['search.html']

epub_css_files = [
    'css/epub.css',               # Your custom CSS
    'fonts/google-fonts.min.css'   # The Google Fonts CSS
]

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

latex_documents = [
    (master_doc, 'your_project_name.tex', project,
     author, 'manual'),
]

# HTML title and favicon
html_title = f'{project} Documentation-4.9'

# Path to the logo image
html_logo = 'icons/wazuh-logo-john.png'   

# Path to the favicon image
html_favicon = 'icons/favicon.ico'


# Add link anchors for each heading and description environment. Default: True.
html_permalinks = True

# HTML context
html_context = {
    "display_github": True,
    "github_user": "wazuh",
    "github_repo": "wazuh-documentation",
    'github_version': 'main',
    "conf_py_path": "/source/",
}
