'''PAYING OFF CREDIT CARD DEBT

Each month, a credit card statement will come with the option for you to pay a minimum amount of your charge, usually 2% of the balance due. However, the credit card company earns money by charging interest on the balance that you don't pay. So even if you pay credit card payments on time, interest is still accruing on the outstanding balance.

Say you've made a $5,000 purchase on a credit card with an 18% annual interest rate and a 2% minimum monthly payment rate. If you only pay the minimum monthly amount for a year, how much is the remaining balance?

You can think about this in the following way.

At the beginning of month 0 (when the credit card statement arrives), assume you owe an amount we will call b0 (b for balance; subscript 0 to indicate this is the balance at month 0).

Any payment you make during that month is deducted from the balance. Let's call the payment you make in month 0, p0. Thus, your unpaid balance for month 0, ub0, is equal to b0−p0.

ub0=b0−p0

At the beginning of month 1, the credit card company will charge you interest on your unpaid balance. So if your annual interest rate is r, then at the beginning of month 1, your new balance is your previous unpaid balance ub0, plus the interest on this unpaid balance for the month. In algebra, this new balance would be

b1=ub0+r12.0⋅ub0

In month 1, we will make another payment, p1. That payment has to cover some of the interest costs, so it does not completely go towards paying off the original charge. The balance at the beginning of month 2, b2, can be calculated by first calculating the unpaid balance after paying p1, then by adding the interest accrued:

ub1=b1−p1
b2=ub1+r12.0⋅ub1

If you choose just to pay off the minimum monthly payment each month, you will see that the compound interest will dramatically reduce your ability to lower your debt.

Let's look at an example. If you've got a $5,000 balance on a credit card with 18% annual interest rate, and the minimum monthly payment is 2% of the current balance, we would have the following repayment schedule if you only pay the minimum payment each month:

Month	Balance	Minimum Payment	Unpaid Balance	Interest
0	5000.00	100 (= 5000 * 0.02)	4900 (= 5000 - 100)	73.50 (= 0.18/12.0 * 4900)
1	4973.50 (= 4900 + 73.50)	99.47 (= 4973.50 * 0.02)	4874.03 (= 4973.50 - 99.47)	73.11 (= 0.18/12.0 * 4874.03)
2	4947.14 (= 4874.03 + 73.11)	98.94 (= 4947.14 * 0.02)	4848.20 (= 4947.14 - 98.94)	72.72 (= 0.18/12.0 * 4848.20)

You can see that a lot of your payment is going to cover interest, and if you work this through month 12, you will see that after a year, you will have paid $1165.63 and yet you will still owe $4691.11 on what was originally a $5000.00 debt. Pretty depressing!

PROBLEM 1: PAYING THE MINIMUM  (10/10 points)
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance, and print to screen something of the format:

Month: 1
Minimum monthly payment: 96.0
Remaining balance: 4784.0
Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41
instead of

Remaining balance: 813.4141998135 
Finally, print out the total amount paid that year and the remaining balance at the end of the year in the format:

Total paid: 96.0
Remaining balance: 4784.0
A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

Note that the grading script looks for the order in which each value is printed out. We provide sample test cases below; we suggest you develop your code on your own machine, and make sure your code passes the sample test cases, before you paste it into the box below.

Test Cases to Test Your Code With. Be sure to test these on your own machine - and that you get the same output! - before running your code on this webpage!
Click to See Problem 1 Test Cases

The code you paste into the following box should not specify the values for the variables balance, annualInterestRate, or monthlyPaymentRate - our test code will define those values before testing your submission.
'''

# Paste your code into this box
minpay = 0
unpaid = 0
total = 0
for i in range(1,13):
    monthinterest = annualInterestRate/12
    minpay = monthlyPaymentRate*balance
    unpaid = balance - minpay
    balance = unpaid*   (1+monthinterest)
    total = total + minpay
    print ("Month: %d"%i)
    print ("Minimum monthly payment: %.2f" % minpay)
    print ("Remaining balance: %.2f" % balance)


print "Total paid: %.2f" % total
print ("Remaining balance: %.2f" % balance)