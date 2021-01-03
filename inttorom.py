class roman:
    def int_to_Roman(self,num):
        val = [
        1000,900,500,400,
        100,90,50,40,
        10,9,5,4,
        1
        ]
        syb = [
        "M","CM","D","CD",
        "C","XC","L","XL",
        "X","IX","V","IV",
        "I"
        ]
        roman_num = ""
        i = 0
        while num > 0:
            for _ in range(num//val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


num = int(input("Please enter integer that needs to be converted to Roman: "))
print(roman().int_to_Roman(num))