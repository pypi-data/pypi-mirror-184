from cvxpy.atoms.elementwise.exp import exp
from cvxpy.atoms.elementwise.log import log


def one_minus_pos_canon(expr, args):
    return log(expr._ones - exp(args[0])), []
