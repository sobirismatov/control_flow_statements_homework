def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    s=a
    if a>0 and a%2==0:
        s= "musbat juft son"
    if a>0 and a%2==1:
        s= "musbat toq son"
    if a<0 and a%2==0:
        s= "manfiy juft son"
    if a<0 and a%2==1:
        s= "manfiy toq son"
    if a==0:
        s= "raqam nol"
    return s
print(main(0))