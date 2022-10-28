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
    if a>0 and a%2==0:
        return "musbat juft son"
    if a>0 and a%2!=0:
        return "musbat toq son"
    if a<0 and a%2==0:
        return "manfiy juft son"
    if a<0 and a%2!=0:
        return "manfiy toq son"
    if a==0:
        return "raqam nol"
print(main(-3))