
# [[file:~/Research/CFEDemands/Demands/demands.org::*Top-level%20demand%20interface][demands]]

# Tangled on Sun Aug 26 11:11:21 2018
from __future__ import print_function
from . import frischian
from . import hicksian
from . import marshallian
from ._core import lambdavalue, relative_risk_aversion, excess_expenditures, excess_expenditures_derivative, excess_utility, lambdaforU, expenditures
from ._utils import derivative, check_args
from numpy import array, log

def utility(x,alpha,beta,phi):
    """
    Direct utility from consumption of x.
    """
    n,alpha,beta,phi = check_args(x,alpha,beta,phi)

    U=0
    for i in range(n):
        if beta[i]==1:
            U += alpha[i]*log(x[i]+phi[i])
        else:
            U += alpha[i]*((x[i]+phi[i])**(1-1./beta[i])-1)*beta[i]/(beta[i]-1)

    return U

def marginal_utilities(x,alpha,beta,phi):
    """
    Marginal utilities from consumption of x.
    """
    n,alpha,beta,phi = check_args(x,alpha,beta,phi)

    MU=[]
    for i in range(n):
        MU += [alpha[i]*((x[i]+phi[i])**(-1./beta[i]))]

    return MU

# demands ends here

# [[file:~/Research/CFEDemands/Demands/demands.org::*Hicksian%20demand%20interface][main]]

# Tangled on Sun Aug 26 11:11:21 2018
def main(y,p,alpha,beta,phi,NegativeDemands=True):

    n=len(p)
    print('lambda=%f' % lambdavalue(y,p,alpha,beta,phi,NegativeDemands=NegativeDemands))
    print('budget shares '+'%6.5f\t'*n % tuple(marshallian.budgetshares(y,p,alpha,beta,phi,NegativeDemands=NegativeDemands)))
    print('share income elasticities '+'%6.5f\t'*n % tuple(marshallian.share_income_elasticity(y,p,alpha,beta,phi,NegativeDemands=NegativeDemands)))
    print('indirect utility=%f' % marshallian.indirect_utility(y,p,alpha,beta,phi,NegativeDemands=NegativeDemands))
    
    # Here's a test of the connections between different demand
    # representations:
    print("Testing identity relating expenditures and indirect utility...", end=' ')
    V=marshallian.indirect_utility(y,p,alpha,beta,phi,NegativeDemands=NegativeDemands)
    X=hicksian.expenditurefunction(V,p,alpha,beta,phi,NegativeDemands=NegativeDemands)
    assert abs(y-X)<1e-6
    print("passed.")
    
    def V(xbar):
        return marshallian.indirect_utility(xbar,p,alpha,beta,phi,NegativeDemands=NegativeDemands)

    dV=derivative(V)

    tol=1e-6

    try:
        print("Evaluating lambda-V'...", end=' ')
        lbda=lambdavalue(y,p,alpha,beta,phi,NegativeDemands=NegativeDemands)
        assert abs(dV(y)-lbda)<tol
        print("within tolerance %f" % tol)
    except AssertionError:
        print("dV=%f; lambda=%f" % (dV(y),lbda))

if __name__=="__main__":
    print("Single good; negative phi")
    main(3.,[1],[1],[1],[-2.],NegativeDemands=False)

    print("Passed.")
    print()

    print("Two goods; phis of different signs; no negative demands")
    main(3,[1]*2,[1]*2,[1]*2,[2,-2.],NegativeDemands=False)

    print("Passed.")
    print()

    print("Two goods; phis of different signs; negative demands allowed")
    main(3,[1]*2,[1]*2,[1]*2,[2,-2.],NegativeDemands=True)

    print("Passed.")
    print()

    y=6
    p=array([10.0,15.0])
    alpha=array([0.25,0.75])
    beta=array([1./2,2.])
    phi=array([-.1,0.0])

    main(y,p,alpha,beta,phi)

# main ends here
