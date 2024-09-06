def _uppercase_(s):
    return s.upper()

def _reverse_(s):
    return s[::-1]

def _capitalize(s):
    return s.capitalize()

def format_string(s, operations):
    for i in range(len(operations)):
        if operations[i]=="uppercase":
            s=_uppercase_(s)
        elif operations[i]=="reverse":
            s=_reverse_(s)
        elif operations[i]=="capatlize":
            s=_capitalize(s)

    return s          

def main():
    s="hello world"
    operations=['uppercase' ,'reverse']
    print(format_string(s,operations))            



if __name__ == "__main__":
    main()    