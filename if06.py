from re import S


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
    s=a,b,c
    if a>0 and b>0 and c>0:
        s="musbat raqamlar ko'p"
    if a<0 and b>0 and c>0 or a<0 and b<0 and c>0 or a>0 and b>0 and c<0:
        s= "musbat raqamlar ko'p"
    if a<0 and b<0 and c>0 or a<0 and b>0 and c<0 or a>0 and b<0 and c<0:
        s= "manfiy raqamlar kop"
    else:
        s= "manfiy raqamlar kop"
    return s
print(main(2,3,4))
