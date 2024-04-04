from argparse import ArgumentParser
import math
import sys


def get_min_payment(principal, annual_interest_rate, years=30, num_annual_payments=12):
    """Calculate the minimum mortgage payment."""
    r = annual_interest_rate / num_annual_payments
    n = years * num_annual_payments
    minimum_payment = principal * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
    return math.ceil(minimum_payment)


def interest_due(balance, annual_interest_rate, num_annual_payments=12):
    """Calculate the amount of interest due in the next payment."""
    r = annual_interest_rate / num_annual_payments
    return balance * r


def remaining_payments(balance, annual_interest_rate, target_payment, num_annual_payments=12):
    """Calculate the number of payments required to pay off the mortgage."""
    counter = 0
    while balance > 0:
        interest_payment = interest_due(balance, annual_interest_rate, num_annual_payments)
        balance -= (target_payment - interest_payment)
        counter += 1
    return counter


def main(mortgage_amount, annual_interest_rate, years=30, num_annual_payments=12, target_payment=None):
    """Perform fixed-rate mortgage calculations and display results."""
    minimum_payment = get_min_payment(mortgage_amount, annual_interest_rate, years, num_annual_payments)
    print(f"Minimum Payment: ${minimum_payment}")

    if target_payment is None:
        target_payment = minimum_payment

    if target_payment < minimum_payment:
        print("Your target payment is less than the minimum payment for this mortgage")
    else:
        total_payments = remaining_payments(mortgage_amount, annual_interest_rate, target_payment, num_annual_payments)
        print(f"If you make payments of ${target_payment}, you will pay off the mortgage in {total_payments} payments.")


def parse_args(arglist):
    """Parse and validate command-line arguments."""
    parser = ArgumentParser()
    parser.add_argument("mortgage_amount", type=float,
                        help="the total amount of the mortgage")
    parser.add_argument("annual_interest_rate", type=float,
                        help="the annual interest rate, as a float"
                             " between 0 and 1")
    parser.add_argument("-y", "--years", type=int, default=30,
                        help="the term of the mortgage in years (default: 30)")
    parser.add_argument("-n", "--num_annual_payments", type=int, default=12,
                        help="the number of payments per year (default: 12)")
    parser.add_argument("-p", "--target_payment", type=float,
                        help="the amount you want to pay per payment"
                        " (default: the minimum payment)")

    # parse and validate arguments
    args = parser.parse_args(arglist)
    if args.mortgage_amount < 0:
        raise ValueError("mortgage amount must be positive")
    if not 0 <= args.annual_interest_rate <= 1:
        raise ValueError("annual interest rate must be between 0 and 1")
    if args.years < 1:
        raise ValueError("years must be positive")
    if args.num_annual_payments < 0:
        raise ValueError("number of payments per year must be positive")
    if args.target_payment and args.target_payment < 0:
        raise ValueError("target payment must be positive")

    return args


if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
    main(args.mortgage_amount, args.annual_interest_rate, args.years,
         args.num_annual_payments, args.target_payment)
