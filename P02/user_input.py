"""-------------------------------------------------------------------------
User Input Module - Robust numeric input validation

two functions: get_integer and get_float
they prompt the user to input a number
   if the input does not meet specified criteria,
   then the user is scolded and prompted again
   after three unsuccessful tries, None is returned
There are four possible calls for either function,
   illustrated here for get_integer
    get_integer() - any integer input by the user is returned
                    generic prompt is used
    get_integer(prompt) - any integer input by the user is returned
                          user supplied prompt is used prompt is used
    get_integer(prompt, max) - integer input by the user is returned
                               provided it is no larger than max
                               user supplied prompt is used
     get_integer(prompt, maxn, min) - integer input by the user is returned
                                provided it is between min and max
                                user supplied prompt is used
-------------------------------------------------------------------------"""

INTEGER = 4         # asking for integer input
FLOAT = 8           # asking for float input
MAX_NR_ATTEMPTS = 3 # before giving up
NO_BOUND = 0    # no bounds on the solicited numeric input
LOWER_BOUND = 1   # only min bound on the solicited numeric input provided
UPPER_BOUND = 2   # only max bound on the solicited numeric input provided
BOTH_BOUNDS = 3   # upper and lower limit on the numeric input provided


def get_integer(prompt=None, upper=None, lower=None):
    return get_number(INTEGER, prompt, upper, lower)


def get_float(prompt=None, upper=None, lower=None):
    return get_number(FLOAT, prompt, upper, lower)


def get_number(number_type, prompt=None, upper=None, lower=None):

    case, new_prompt = build_prompt(number_type, prompt, upper, lower)

    all_done = False
    nr_of_attempts = 0
    while not all_done and nr_of_attempts < MAX_NR_ATTEMPTS:
        try:
            if number_type == INTEGER:
                inp = int(input(new_prompt))
            else:  # number_type must be FLOAT
                inp = float(input(new_prompt))

            if case == NO_BOUND:
                all_done = True
            elif case == UPPER_BOUND:
                if inp <= upper:
                    all_done = True
                else:
                    print("This value is too large")
                    nr_of_attempts += 1
            elif case == LOWER_BOUND:
                if inp >= lower:
                    all_done = True
                else:
                    print("This value is too small")
                    nr_of_attempts += 1
            else:  # case must == BOTH_BOUNDS
                if lower <= inp <= upper:
                    all_done = True
                else:
                    print("This value is not between " + str(lower) + " and " + str(upper))
                    nr_of_attempts += 1
        except:
            print("this is not a valid input")
            nr_of_attempts += 1

    if all_done:
        return inp
    else:
        return None


def build_prompt(type, prompt, upper, lower):
    if prompt is None:
        prompt = "Please enter " + ("an integer " if type == INTEGER else "a float ")

    if upper is None and lower is None:
        case = NO_BOUND
    elif upper is None: # lower had to be given
        case = LOWER_BOUND
        prompt += ("no smaller than " + str(lower) + " ")
    elif lower is None:  # lower had to be given
        case = UPPER_BOUND
        prompt += (" not higher than " + str(upper) + " ")
    else:
        case = BOTH_BOUNDS
        prompt += (" between " + str(lower) + " and " + str(upper) + " ")
    return case, prompt


if __name__ == "__main__":
    # test code: 8 possible calling patterns  covering:
    # * with / without a prompt
    # * with / without a lower bound
    # * with / without an upper bound
    # * any order of keyword arguments

    # because the function signature is: get_integer(prompt=None, upper=None, lower=None),
    # the keyword names must be: **prompt**, **upper**, **lower**.

    # **1. No arguments at all**
    x = get_integer()
    print(f"called without a prompt integer: {x}")

    # **2. Only prompt**
    x = get_integer(prompt="Please enter an int: ")
    print(f"called with a prompt integer: {x}")

    # **3. Only upper bound**
    x = get_integer(upper=20)
    print(f"called without a prompt  but <= 20.  Integer: {x}")

    # **4. Only lower bound**
    x = get_integer(lower=10)
    print(f"called without a prompt  but >= 20.  Integer: {x}")

    # **5. Prompt + upper**
    x = get_integer(prompt="Please enter an int: ", upper=20)
    print(f"called with a prompt  and <= 20.  Integer: {x}")

    # **6. Prompt + lower**
    x = get_integer(prompt="Please enter an int: ", lower=10)
    print(f"called with a prompt  and >= 20.  Integer: {x}")

    # **7. Upper + lower**
    x = get_integer(upper=20, lower=10)
    print(f"called without a prompt  10 <= x <= 20.  Integer: {x}")

    # **8. Prompt + upper + lower**
    x = get_integer(prompt="Please enter an int: ", upper=20, lower=10)
    print(f"called with a prompt  10 <= x <= 20.  Integer: {x}")

    # IMPORTANT  keyword arguments may be given in any order, for example:
    x = get_integer(lower=10, prompt="Please enter an int: ")
    print(f'called: "lower=10, prompt=Please enter an int: {x}')
