#Functions for string analysing and modification

nl = "\n" #newline constant to keep code clean

def locBrac(string: str, brac: str, ix: int) -> int:
    """
    Finds the index of the closing bracket that matches the opening bracket at the given index in the given string.

    Parameters:
        string (str): The input string.
        brac (str): The bracket character | Possible are ( [ { <
        ix (int): The index of the opening bracket in the input string.

    Returns:
        int: The index of the closing bracket in the input string, or -1 if no matching closing bracket was found.

    Example:
        >>> locBrac('[hello[world]]', 0)
        13
        >>> locBrac('[hello[world]]', 6)
        12
        >>> locBrac('[hello]world]', 0)
        -1
    """
    fil = {"(":")", "[":"]", "{":"}", "<":">"}
    if not brac in fil:
        return -1
    if not brac in string:
        return -1
    st = []
    for i, ch in enumerate(string):
        if ch == brac:
            st.append(i)
        elif ch == fil[brac]:
            st.pop()
        if st == [] and i >= ix:
            return i
    return -1