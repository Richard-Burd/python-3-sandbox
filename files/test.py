# https://stackoverflow.com/questions/30669474/beyond-top-level-package-error-in-relative-import

import sys
sys.path.append("..") # Adds higher directory to python modules path.

from lessons.space.planet import Planet

print(Planet)
#=> <class 'lessons.space.planet.Planet'>
