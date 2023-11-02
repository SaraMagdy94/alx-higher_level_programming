#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    addi = add(a, b)
    subi = sub(a, b)
    multi = mul(a, b)
    divi = div(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, addi))
    print("{:d} - {:d} = {:d}".format(a, b, subi))
    print("{:d} * {:d} = {:d}".format(a, b, multi))
    print("{:d} / {:d} = {:d}".format(a, b, divi))
