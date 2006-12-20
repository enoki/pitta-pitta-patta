#
# Bandleader
# Licensed under the GPL
#

from distutils.core import setup
import py2exe

setup(windows=[{'script' : 'pitta-pitta-patta.py',
                'icon_resources' : [(1, 'icons/icon.ico')]
               }],
               name="Pitta Pitta Patta",
               version="0.1",
     )
