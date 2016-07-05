import sys

sys.path.append('/opt/moose/seacas/lib')

from exodus import exodus

e = exodus('xyz.e', mode='r', array_type='numpy')

print e.num_elems()
