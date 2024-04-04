# Hadi Serag Eldin
import argparse
import sys

def calculate_tuition(credits=12, resident=True, dt=False):
    """Calculates tuition and mandatory fees for one semester at UMD.

    Takes into consideration the number of credits the student is taking,
    whether they are a resident of Maryland, and whether they pay
    differential tuition.

    Args:
        credits (integer): the number of credits the student is taking
            (default: 12).
        resident (boolean): whether the student is considered a
            Maryland state resident for tuition purposes (default: True).
        dt (boolean): whether or not the student pays
            differential tuition (default: False).

    Raises:
        ValueError: credits must be non-negative.

    Returns:
        float: the student's combined tuition and mandatory fees.
    """
    if credits < 0:
        raise ValueError("Credits must be non-negative.")
    
    flat_tuition_md = 4412.00
    flat_tuition_non_md = 17468.00
    per_credit_md = 367.00
    per_credit_non_md = 1456.00
    differential_tuition_flat = 1428.00
    differential_tuition_per_credit = 118.00
    fee_9_or_more_credits = 977.50
    fee_1_to_8_credits = 455.00

    tuition = 0.0
    fees = 0.0

    if credits >= 12:
        if resident:
            tuition = flat_tuition_md
        else:
            tuition = flat_tuition_non_md
        if dt:
            tuition += differential_tuition_flat
    elif credits > 0:
        if resident:
            tuition = credits * per_credit_md
        else:
            tuition = credits * per_credit_non_md
        if dt:
            tuition += credits * differential_tuition_per_credit
    
    if credits >= 9:
        fees = fee_9_or_more_credits
    elif credits >= 1:
        fees = fee_1_to_8_credits

    return tuition + fees

def parse_args(arglist):
    """Parses command-line arguments.

    The following optional command-line arguments are defined:

    -c / --credits: the number of credits the student is taking
        (type: int, default: 12)
    -nr / --nonresident: indicates the student is not a Maryland
        resident (action: 'store_true')
    -dt / --differentialtuition: indicates the student pays differential
        tuition (action: 'store_true')

    Args:
        arglist (list of str): a list of command-line arguments.

    Returns:
        namespace: a namespace with variables credits, nonresident, and
        differentialtuition.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--credits', type=int, default=12)
    parser.add_argument('-nr', '--nonresident', action='store_true')
    parser.add_argument('-dt', '--differentialtuition', action='store_true')
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    resident = not args.nonresident  # Negate nonresident to get resident status
    total_cost = calculate_tuition(args.credits, resident, args.differentialtuition)
    print(f"Your tuition and fees total ${total_cost:.2f}.")

#I tested it by running this script from the command line. I did "HSeragEldin_TuitionCalculator.py -c 15 -nr -dt"
#My result for that was "Your tuition and fees total $19873.50." to show it worked. 