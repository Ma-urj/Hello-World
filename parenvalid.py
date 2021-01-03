#To check if Parenthese sequence is valid
class parenthese:
    def is_valid(self, str1):
        pchar = {"(": ")", "{": "}", "[": "]"}
        i = 0
        while i < len(str1):
            if pchar[str1[i]] != str1[i+1]:
                return False
            i += 2
        return True

str = input("Enter parenthese sequence: ")
print(parenthese().is_valid(str))
