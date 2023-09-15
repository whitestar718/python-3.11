def create_eg():
    eg = ExceptionGroup("Exception group message!",
                        [FileNotFoundError("'aaa.png' not found..."),
                         FileNotFoundError("'bbb.png' not found..."),
                         ValueError("Mayonnaise is not an instrument")])
    raise eg

# 1
# create_eg()

try:
    create_eg()

except* FileNotFoundError as eg:
    print(eg.exceptions)

except* ValueError as eg:
    eg.add_note("value error additional notes")
    print(eg.exceptions)