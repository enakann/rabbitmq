import sys

import inspect


mod=sys.argv[1]
mod="pika."+mod
print(inspect.getsourcefile(mod))
