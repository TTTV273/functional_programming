def get_logger(formatter):
    # STEP 1: This is the OUTER function (the factory)
    # It receives parameters that will be "remembered" by the inner function
    # formatter = the function that will format our log messages
    
    # STEP 2: Define the INNER function (the product that gets returned)
    # This inner function will be called later by whoever uses our factory
    def logger(first, second):
        # STEP 3: Use the parameters from the outer function (closure)
        # formatter was captured from the outer scope
        formatted_message = formatter(first, second)
        
        # STEP 4: Do the actual work (in this case, print the formatted message)
        print(formatted_message)
    
    # STEP 5: Return the inner function (NOT call it!)
    # This gives the caller a customized function to use later
    return logger


# Don't edit below this line


def test(first, errors, formatter):
    print("Logs:")
    logger = get_logger(formatter)
    for err in errors:
        logger(first, err)
    print("====================================")


def colon_delimit(first, second):
    return f"{first}: {second}"


def dash_delimit(first, second):
    return f"{first} - {second}"


def main():
    db_errors = [
        "out of memory",
        "cpu is pegged",
        "networking issue",
        "invalid syntax",
    ]
    test("Doc2Doc FATAL", db_errors, colon_delimit)

    mail_errors = [
        "email too large",
        "non alphanumeric symbols found",
    ]
    test("Doc2Doc WARNING", mail_errors, dash_delimit)


main()
