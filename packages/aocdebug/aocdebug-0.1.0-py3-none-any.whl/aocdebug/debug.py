import traceback

BOLD = "\033[1m"
GREEN = "\033[92m"
CYAN = "\033[96m"
CLEAR = "\033[0m"


def debug(*arg_values):
    path, lno, _, loc = traceback.extract_stack()[-2]
    filename = path[len(path) - path[::-1].index("/") :]
    arg_names = loc[loc.index("(") + 1 : -1].split(", ")
    print(f"<{filename}+{CYAN}{lno}{CLEAR}>", end=" ")
    for (arg_value, arg_name) in zip(arg_values, arg_names):
        print(f"{BOLD+GREEN}{arg_name}{CLEAR}={repr(arg_value)}", end=", ")
    print()
