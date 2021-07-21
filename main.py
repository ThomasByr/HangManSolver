from core.search import *

msg = "---user input---\nformat : letters or dots then tested letters\nfor eg : .a.er aeiouls\n\n_"

#! put path below
with open("assets\\fr_dict.txt", "r", encoding="utf-8") as f:
    d = f.readlines()  # list of lines
    d = [x.strip().lower() for x in d]  # lowercase w/o spaces

if __name__ == "__main__":
    user_space = input(msg).lower()
    print(find(user_space, d))
