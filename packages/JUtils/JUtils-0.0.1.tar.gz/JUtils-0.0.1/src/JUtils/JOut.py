#Functions for handling console output

def printn(*args):
    """Prints the given arguments, with newlines before and after
    
    Parameters:
        *args: The arguments to print.
    """
    print("\n"+" ".join(str(x) for x in args)+"\n")