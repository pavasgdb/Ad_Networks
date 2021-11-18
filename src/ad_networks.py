from builtwith import builtwith
import sys

d = builtwith(sys.argv[1],headers=[])
print(d)