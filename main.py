from core.user_space import *

msg = u"---user input---\nformat : letters or dots then tested letters\nfor eg : .a.er aeiouls\n\n_"

#! put path below
with open("assets\\fr_dict.txt", "r", encoding="utf-8") as f:
    d = f.readlines()  # list of lines
    d = [x.strip().lower() for x in d]  # lowercase w/o spaces

if __name__ == "__main__":  # main
    user_space = input(msg).lower()  # first time input
    prev = user_space  # save the previous input
    prettyprint(user_space, d)  # pretty print

    # type "quit()" to exit
    while user_space != "quit()":
        user_space = input("\n_").lower()  # next time input
        if user_space[0] == "+":  # if + then add
            # look for space in previous input then add it
            user_space = f"{prev} {user_space[1:]}" if " " not in prev else f"{prev}{user_space[1:]}"
        try:
            if (i := int(user_space[0])) in range(100):  # if int then add
                n = len(user_space) - 1
                # look for position in previous input then replace it
                user_space = f"{prev[:i]}{user_space[1:]}{prev[i+n:]}"
        except ValueError:
            pass  # do nothing
        prettyprint(user_space, d)
