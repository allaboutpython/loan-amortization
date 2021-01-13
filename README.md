# loan-amortization
This is an Python implementation of [loan and mortgage amortization](https://www.allaboutpython.com/2021/01/loan-or-mortgage-amortization-function.html). It can be used to solve the [buy vs rent problem](https://www.allaboutpython.com/2021/01/the-buy-vs-rent-decision-value-of-money.html).

The loan or mortgage amortization schedule usually achieved with the excel template in the financial world. One can simply use the formula to compute the monthly payment and the template to work on the schedule. There are more complex tasks that are not easily to refer to the excel sheet. For instance, we might want to perform a task to look up the balance on the amortization schedule to make the decision when to pay off the balance. This could be simply implemented in Python and it's a nice illustration of how to use Python in Finance. I decided to take a shot to the loan amortization function as the start of a financial calculator. The results has been cross checked with the financial calculators. 

There are generally tree steps. 

1. Calculate the monthly payment for the loan
2. Calculate the principle for amortization schedule
3. Calculate the payment schedule

The monthly payment can be easily calculated with the amortizatoin formula. The detailed loan amortization derivation can be found on wikipedia.

The first step is to calculate the monthly payment with the loan amortization formula. The input is the initial loan amount, the month interest and the total length of loan in months. The interest published is usually the nominal annual interest. The monthly interest can be simply derived by nominal interest/12. The second step is to calculate the principle of any month t. The final step is to iterate thought the period of month to compute the schedule.

    
