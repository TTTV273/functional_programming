def word_count_memo(document, memos):
    # TODO(human): Implement memoization function following these steps:
    # 1. Create a .copy() of the memos dictionary for immutability
    memos_copy = memos.copy()
    # 2. Check if document is already 'in' the memos dictionary (cache hit)
    #    - If yes: return (cached_count, memos_copy)
    if document in memos_copy:
        cached_count = memos_copy[document]
        return (cached_count, memos_copy)
    # 3. If not in cache (cache miss):
    #    - Use word_count(document) to compute the count
    #    - Store the result in memos_copy[document] = count
    #    - Return (count, memos_copy)
    else:
        count = word_count(document)
        memos_copy[document] = count
        return (count, memos_copy)


# Don't edit below this line


def word_count(document):
    count = len(document.split())
    return count
