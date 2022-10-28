def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if 9<a and a<100 and a%2!=0:
        return "ikki xonali toq raqam"
    if  9<a and a<100 and a%2==0:
        return "ikki xonali juft raqam"
    if 99<a and a<1000 and a%2!=0:
       return  "uch xonali toq raqam"
    if 99<a and a<1000 and a%2==0:
       return  "uch xonali juft raqam"
print(main(103))