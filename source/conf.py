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
html_static_path = ['_static','images']

images_config = {
    'thumbnail_size': (150, 150),  # Thumbnail size
    'default_image_width': '80%',  # Default image width
    'output_dir': '_images',       # Directory for generated thumbnails
}

html_css_files = [
    'css/wazuh-custom.css',  # Link to custom CSS
]

# The master toctree document.
master_doc = 'index'

# HTML theme
html_theme = 'sphinx_rtd_theme'

# EPUB settings
epub_title = 'Wazuh-Documentation-5.0'
epub_author = 'Yohannes Iyob Tekle'
epub_publisher = 'Yohannes-Publishers-Private'
epub_copyright = '2024'
epub_identifier = 'unique-identifier'
epub_scheme = '2024-09-12-Version-5.0'
epub_language = 'en'
epub_exclude_files = ['search.html']

# Add your custom CSS file to the EPUB CSS list
epub_css = ['_static/css/epub.css']

# LaTeX settings for PDF
latex_engine = 'xelatex'
latex_elements = {
    'papersize': 'letterpaper',
    'fontpkg': r'\usepackage{fontspec}',  # For xelatex or lualatex
    'fncychap': r'\usepackage[Bjarne]{fncychap}',
    'pointsize': '10pt',
    'preamble': r'\usepackage{lipsum}',
    'figure_align': 'htbp',
}

latex_documents = [
    (master_doc, 'your_project_name.tex', project,
     author, 'manual'),
]

# HTML title and favicon
html_title = f'{project} Documentation-5.0'

# Path to the logo image
html_logo = 'icons/wazuh-logo-john.png'   

# Path to the favicon image
html_favicon = 'icons/favicon.ico'

# HTML context
html_context = {
    "display_github": True,
    "github_user": "wazuh",
    "github_repo": "wazuh-documentation",
    'github_version': 'main',
    "conf_py_path": "/source/",
}
