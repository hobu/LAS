# -*- coding: utf-8 -*-
#
# LAS documentation build configuration file, created by
# sphinx-quickstart on Tue Feb  7 14:10:03 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.mathjax', 'sphinxcontrib.spelling']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.txt'

# The master toctree document.
master_doc = '00_index'

# General information about the project.
project = u'LAS'
copyright = u'2019, ASPRS'
author = u'ASPRS'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
#version = u'1.4'
# Custom non-keyword version tag for header
myversion = u'1.4 - R15'
# The full version, including alpha/beta/rc tags.
release = u'VERSION ' + myversion
releasename = release
version=''

# Publication info (approval date, release date, and GitHub SHA)
today='09 July 2019'
releasedate='09 July 2019'
approvaldate = 'November 2011'

import subprocess

def get_git_revision_short_hash():
    import os
    return os.environ['GITHUB_SHA']
gitsha = get_git_revision_short_hash()

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'LASdoc'


# -- Options for LaTeX output ---------------------------------------------

preamble = r'''

% Ensures arabic numerals (1, 2, 3) as section numbering style
\renewcommand\thesection{\arabic{section}}

% Apply fancyhdr overrides to Sphinx default styles. More info:
% https://stackoverflow.com/questions/4839105/sphinx-customization-of-latexpdf-output
% bug: this still doesn't apply to the TOC and title page. not sure what style's there.

\usepackage{titling}
\usepackage{fancyhdr}
\makeatletter
\fancypagestyle{normal}{
    \fancyhf{}
    \fancyhead[R]{American Society for Photogrammetry \& Remote Sensing}
    \fancyhead[L]{LAS Specification VVVV}
    \fancyfoot[L]{\rightmark}
    \fancyfoot[R]{Page \thepage}

    \renewcommand{\headrulewidth}{1pt}
    \renewcommand{\footrulewidth}{1pt}
}

% Override Sphinx defaults for table heading (bold instead of sans serif)
% note: won't work in newer versions of Sphinx 1.7+
\protected\def\sphinxstyletheadfamily{\textbf}

\makeatother

% Override Sphinx defaults for list item spacing and bolding. More info:
% https://tex.stackexchange.com/questions/10684/vertical-space-in-lists
% https://texblog.org/2008/10/16/lists-enumerate-itemize-description-and-how-to-change-them/
\usepackage{enumitem}
\setlist{noitemsep}

'''.replace("VVVV", u'v.' + myversion)

# Build PDF title page
args = {}
args['author'] = author
args['releasedate'] = releasedate
args['releasename'] = releasename
args['approvaldate'] = approvaldate
args['gitsha'] = gitsha
import datetime
now = datetime.datetime.now()
args['thisyear'] = now.year
now = now.strftime("%d %B %Y")
args['now'] = now

title = r"""
\begin{titlingpage}

{\sphinxlogo}


\vspace{0.25in}

{\huge
\thetitle\\
}

\release{%(releasename)s}
\author{%(author)s}

{\Large \bf
\noindent
Release Information:\\
}
\noindent {\bf Version Approved -- %(approvaldate)s}\\
Revision date -- %(releasedate)s\\
\\
PDF build date -- %(now)s\\
GitHub commit -- %(gitsha)s\\
GitHub repo -- https://github.com/ASPRSorg/LAS


\vspace{0.25in}

{\Large \bf
\noindent Published by:\\
}
The American Society for Photogrammetry \& Remote Sensing\\
425 Barlow Place, Suite 210\\
Bethesda, Maryland 20814-2160\\
Voice: 301-493-0290\\
Fax: 225-408-4422\\
Web: \underline{www.asprs.org}\\


\noindent
Copyright \copyright~2002-%(thisyear)d American Society for Photogrammetry and Remote Sensing (ASPRS). All rights reserved.\\
\\
\\
{\bf Permission to Use:} The copyright owner hereby consents to unlimited use and
distribution of this document, or parts thereof, \underline{as a specification} provided such use references
ASPRS as the publisher. This consent does not extend to other uses such as general distribution
in any form, including electronic, by any individual or organization whether for advertising or
promotional purposes, for creating new collective works, or for resale. For these and all other
purposes, reproduction of this publication or any part thereof (excluding short quotations for use
in the preparation of reviews and technical and scientific papers) may be made only after
obtaining the specific approval of the publisher.\\
\\
Printed in the United States of America.

\end{titlingpage}

""" % args

# Assign 'report' to 'manual' documentclass. Override as needed.
#latex_docclass = {
#    'manual': 'report'
#}

# Final PDF page setup for LaTeX
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '12pt',

    # Other document class options - ensure uniform header/footer
    'classoptions': ',oneside,openany',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': preamble,

    # Latex figure (float) alignment
    #
    'figure_align': 'htbp',
    'releasename': ' ',# defined above. blank to prevent duplicate usage in title page
    'maketitle': title,

    # Don't use atendofbody. Use fancyhdr calls in preamble instead (above).
#    'atendofbody': """American Society for Photogrammetry \& Remote Sensing \\ LAS SPECIFICATION \\""" + releasename
}

latex_toplevel_sectioning='section'
latex_show_urls='footnote'
latex_logo = './_static/asprslogo45.png'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'LAS.tex', u'LAS Specification %s' % myversion,
     u'ASPRS', 'manual'),
]


