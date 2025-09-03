def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length

        def with_length(doc):
            split_doc = doc.split("\n")
            # count = 0
            # for line in split_doc:
            #     if sequence in line:
            #         count += 1
            # return count
            return len(list(filter(lambda line: sequence in line, split_doc)))

        return with_length

    return with_char
