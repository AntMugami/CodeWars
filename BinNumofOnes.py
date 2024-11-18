def count_bits(n):
    str_bin_num = str(bin(n))
    return str_bin_num.count('1',2,)


# def countBits(n):
#     return bin(n).count("1")


print(count_bits(4))
print(count_bits(7))
print(count_bits(9))
print(count_bits(10)) 