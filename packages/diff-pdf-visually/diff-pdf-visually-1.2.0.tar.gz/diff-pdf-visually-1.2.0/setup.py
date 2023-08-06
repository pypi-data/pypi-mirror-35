# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['diff_pdf_visually']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['diff-pdf-visually = diff_pdf_visually:__main__.main']}

setup_kwargs = {
    'name': 'diff-pdf-visually',
    'version': '1.2.0',
    'description': 'A simple script to test whether there is a significant difference between two PDFs using ImageMagick and pdftocairo.',
    'long_description': '\n***************************************************************\n``diff-pdf-visually``: Find visual differences between two PDFs\n***************************************************************\n\nThis script checks whether two PDFs are visually the same. So:\n\n- White text on a white background will be **ignored**.\n- Subtle changes in position, size, or color of text will be **detected**.\n- This program will ignore changes caused by a different version of the PDF generator, or by invisible changes in the source document.\n\nThis is in contrast to most other tools, which tend to extract the text stream out of a PDF, and then diff those texts. Such tools include:\n\n- `pdf-diff <https://github.com/JoshData/pdf-diff>`_ by Joshua Tauberer\n\nThere seem to be some tools similar to the one you\'re looking at now, although I have experience with none of these:\n\n- Václav Slavík seems to have `an open source one <https://github.com/vslavik/diff-pdf>`_\n- There might be more useful ones mentioned on `this SuperUser thread <https://superuser.com/questions/46123/how-to-compare-the-differences-between-two-pdf-files-on-windows>`_\n\nThe strength of this script is that it\'s simple to use on the command line, and it\'s easy to reuse in scripts:\n\n.. code-block:: python\n\n    from diff_pdf_visually import pdfdiff\n\n    # Returns True or False\n    pdfdiff("a.pdf", "b.pdf")\n\nOr use it from the command line:\n\n.. code-block:: shell\n\n    $ pip3 install --user diff-pdf-visually\n    $ diff-pdf-visually a.pdf b.pdf\n\nHow it works\n============\n\nWe use ``pdftocairo`` to convert both PDFs to a series of PNG images in a temporary directory. The number of pages and the dimensions of the page must be exactly the same. Then we call ``compare`` from ImageMagick to check how similar they are; if one of the pages compares different above a certain threshold, then the PDFs are reported as different, otherwise they are reported the same.\n\n**You must have ImageMagick and pdftocairo already installed**.\n\nCall ``diff-pdf-visually`` without parameters (or run ``python3 -m diff_pdf_visually``) to see its command line arguments. Import it as ``diff_pdf_visually`` to use its functions from Python.\n\nSo what do you use this for?\n============================\n\nPersonally, I\'ve used this a couple of times to refactor my LaTeX documents: I just simplify or remove some macro definitions, and if nothing changes, apparently it\'s safe to make that change.\n\nHow to install this\n===================\n\n``pip3 install diff-pdf-visually``\n\nStatus\n======\n\nAt the moment, this program/module works best for finding *whether* two PDFs are visually different.\n\nThis project is licenced under the MIT licence.\n\nDoes it work on Python 2?\n=========================\n\nI don\'t know! You tell me :D',
    'author': 'Bram Geron',
    'author_email': 'bram@bram.xyz',
    'url': 'https://github.com/bgeron/diff-pdf-visually',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.0,<4.0',
}


setup(**setup_kwargs)
