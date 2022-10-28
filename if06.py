def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    if a>0 and b>0 and c>0:
        return  3 , "there are a lot of positive numbers"
    if a<0 and b>0 and c>0 or a<0 and b<0 and c>0 or a>0 and b>0 and c<0:
        return 2, "there are a lot of positive numbers"
    if a<0 and b<0 and c>0 or a<0 and b>0 and c<0 or a>0 and b<0 and c<0:
        return 2 , "there are a lot of negative numbers"
    else:
        return 3, "there are a lot of negative numbers"