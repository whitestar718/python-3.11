def create_eg():
    eg = ExceptionGroup("Exception group message!",
                        [FileNotFoundError("'aaa.png' not found..."),
                         FileNotFoundError("'bbb.png' not found..."),
                         ValueError("Mayonnaise is not an instrument")])
    raise eg

def add3(a, b, c):
    try:
        assert type(a) == int
    except AssertionError as e:
        e.add_note("a is not an integer...")
        # raise

    try:
        assert type(b) == int
    except AssertionError as e:
        e.add_note("b is not an integer...")
        raise
    
    try:
        assert type(c) == str
        print(c, "is string... ok")
    except AssertionError as e:
        e.add_note("c must be string")
        raise

    return a + b

#-----------------------------------------------

add3('1', '2', 3)