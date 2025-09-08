def args_logger(*args, **kwargs):
    for count, item in enumerate(args, 1):
        print(f"{count}. {item}")

    for key, value in sorted(kwargs.items()):
        print(f"* {key}: {value}")

    pass
