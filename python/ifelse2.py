enter_div_test = int(input("Enter divisibility test number: "))
enter_num = int(input("Enter a number: "))

if enter_num % enter_div_test == 0:
    print(enter_num, "is divisible by", enter_div_test)
else:
    print(enter_num, "is not divisible by", enter_div_test)