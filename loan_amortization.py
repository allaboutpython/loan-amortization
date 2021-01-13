"""
Python implementation of loan/amortization schedule
"""


import pandas as pd


def get_monthly_pmt(loan_amt, r, n):
    """ calculate monthly payment
    loan_amt: initial loan amount
    r: monthly interest
    n: total number of payments
    """
    return loan_amt*r*(1 + r)**n / ((1 + r)**n - 1)
    

def get_principle(loan_amt, A, r, t):
    """ calculate principle for month t
    loan_amt: intial loan amount
    A: monthly payment
    r: monthly intrest
    t: number of payments
    """
    return loan_amt*((1 + r)**t) - A*((1 + r)**t - 1)/r


def get_schedule(loan_amt, r, n):
    """ calculate the amortization schedule
    loan_amt: intial loan amount
    r: monthly intrest
    n: total number of payments
    """
    monthly = []
    A = get_monthly_pmt(loan_amt, r, n)
    last = loan_amt
    for i in range(1, n+1):
        curr = get_principle(loan_amt, A, r, i)
        p = last - curr
        monthly.append([i, p, A - p, curr])
        last = curr
    return pd.DataFrame(monthly, columns=['month', 'principle_pmt', 'interest_pmt', 'principle'])


"""
loan_amt = 500,000
r = 0.04/12
n = 300

>>> get_monthly_pmt(loan_amt=500000, r=0.04/12, n=300)

2639.1842014888507

>>> df = show_schedule(loan_amt=500000, r=0.04/12, n=300)

month	principle_pmt	interest_pmt	principle
0	1	972.517535	1666.666667	499027.482465
1	2	975.759260	1663.424942	498051.723205
2	3	979.011791	1660.172411	497072.711414
3	4	982.275163	1656.909038	496090.436251
4	5	985.549414	1653.634788	495104.886837
...	...	...	...	...
295	296	2595.634264	43.549938	10469.347082
296	297	2604.286378	34.897824	7865.060704
297	298	2612.967332	26.216869	5252.093371
298	299	2621.677224	17.506978	2630.416148
299	300	2630.416148	8.768054	0.000000
"""