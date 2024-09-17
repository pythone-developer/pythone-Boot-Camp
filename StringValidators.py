def string_validators(s):
    flag_alnum = any(ch.isalnum() for ch in s)
    alphabetical = any(ch.isalpha() for ch in s)
    digits = any(ch.isdigit() for ch in s)
    lowercase = any(ch.islower() for ch in s)
    uppercase = any(ch.isupper() for ch in s)
    
    return flag_alnum, alphabetical, digits, lowercase, uppercase

if __name__ == '__main__':
    s = input()
    
    flag_alnum, alphabetical, digits, lowercase, uppercase = string_validators(s)
    print(flag_alnum)
    print(alphabetical)
    print(digits)
    print(lowercase)
    print(uppercase)
