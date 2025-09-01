def new_collection(initial_docs):
    # TODO: Step 1 - Create a COPY of initial_docs to avoid modifying the original
    # Hint: Use .copy() method to create a separate list that we can modify
    doc_copy = initial_docs.copy()

    # TODO: Step 2 - Define the inner function that will be returned
    # This function should:
    # - Take one parameter (new_doc) which is a string
    # - Append the new_doc to the copied list (NO nonlocal needed!)
    # - Return the updated list
    def inner_func(new_doc):
        doc_copy.append(new_doc)
        return doc_copy

    # TODO: Step 3 - Return the inner function (not called, just the function itself)
    return inner_func
