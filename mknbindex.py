#!/usr/bin/env python
"""Simple script to auto-generate the index of notebooks in a given directory.
"""

## Config here
repo = 'fperez/cit2013/master'

heading = """\
# An introduction to Scientific Python and IPython.

Most of these materials exist in other repositories used for teaching, they are
gathered here for convenient presentation during CIT'2013.
"""

## No further config should be needed

import glob
import urllib

notebooks = sorted(glob.glob('*.ipynb'))

tpl =  '* [{0}](http://nbviewer.ipython.org/url/raw.github.com/' + repo +'/{1})'

idx = [ heading ]

idx.extend(tpl.format(nb.replace('.ipynb',''), urllib.quote(nb))
           for nb in notebooks)

with open('README.md', 'w') as f:
    f.write('\n'.join(idx))
    f.write('\n')
