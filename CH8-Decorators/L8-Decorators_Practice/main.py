def replacer(old, new):
    def decorated_func(func):
        def wrapper(text):
            new_text = text.replace(old, new)
            return func(new_text)

        return wrapper

    return decorated_func


@replacer("&", "&amp;")
@replacer("<", "&lt;")
@replacer(">", "&gt;")
@replacer('"', "&quot;")
@replacer("'", "&#x27;")
def tag_pre(text):
    return f"<pre>{text}</pre>"

