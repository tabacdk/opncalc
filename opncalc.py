import doctest

def separate(text):
    """Separates tokens in string

    Args:
        text (str): The untokenized string

    Returns:
        list[str]: The tokens

    >>> separate("123 456 +")
    ['123', '456', '+']
    >>> separate("")
    []
    """
    tokens = text.split()
    return tokens

def calculate(tokens, stack, storage):
    done = False
    for t in tokens:
        n = safe_int(t)
        if n is not None:
            stack.append(n)
        elif t == "+":
            b = stack.pop()
            a = stack.pop()
            result = a + b
            stack.append(result)
        elif t == "-":
            a = stack.pop()
            b = stack.pop()
            result = a - b
            stack.append(result)
        elif t == "*":
            b = stack.pop()
            a = stack.pop()
            result = a * b
            stack.append(result)
        elif t == "/":
            b = stack.pop()
            a = stack.pop()
            result = a / b
            stack.append(result)
        elif t == "quit":
            done = True
        elif t == "store": # "23 4 store ... 4 recall"
            b = stack.pop()
            a = stack.pop()
            storage[b] = a
        elif t == "recall":
            a = stack.pop()
            b = storage[a]
            stack.append(b)
        elif t == "drop":
            stack.pop()
        elif t == "dup":
            a = stack.pop()
            stack.append(a)
            stack.append(a)            
        else:
            print("Unknown token :", t)
    return done

def safe_int(s):
    """returns an int or None if not parsable as int

    >>> safe_int("123")
    123
    >>> type(safe_int("!23"))
    <class 'NoneType'>
    """
    try:
        n = int(s)
    except ValueError:
        return None
    else:
        return n

stack = []
storage = {}
done = False
while True:
    text = input("> ")      # "23 24 +"
    tokens = separate(text) # ["2", "23", "24", "+", "*"]
    done = calculate(tokens, stack, storage)
    print(stack)            # [94]
    if done:
        break

# doctest.testmod()
