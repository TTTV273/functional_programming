def make_counter(start=0, step=1):
    # Shared state
    current = start
    original_start = start

    def next_count():
        # Return current, then advance by step
        nonlocal current
        value = current
        current += step
        return value

    def reset(new_start=None):
        nonlocal current
        if new_start is None:
            current = original_start
        else:
            current = new_start
        return current

    def peek():
        # Return the current value without changing it
        return current

    return next_count, reset, peek


def make_prefixer(prefix):
    def add_prefix(message):
        return f"{prefix} {message}"

    return add_prefix
