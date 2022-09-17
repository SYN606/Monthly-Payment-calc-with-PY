from sys import flags


def main():
    print("This is monthaly loan calculator.")


    principal = float(input("Input the loan amout : "))
    apr = float(input("Input the annual intrest rate : "))
    years = int(input("Input amount of years : "))


    monthly_intrest_rate = apr / 1200
    months = years * 12
    monthly_payment = principal * monthly_intrest_rate / (1 - (1 + monthly_intrest_rate)**(-months))


    print("The monthly payment for this loan is: %.2f" % monthly_payment) # the %.2f is used for counting float value 2 digits only.

main()