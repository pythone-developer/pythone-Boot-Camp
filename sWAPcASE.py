def swap_case(s):
    strtin=""
    for i in s:
        if i.isupper()== True:
            strtin+= i.lower()
        else:
            strtin+= i.upper()
         
    return strtin

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)