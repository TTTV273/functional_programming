def file_type_aggregator(func_to_decorate):
    # dict of file_type -&gt; count
    counts = {}

    def wrapper(doc, file_type):
        nonlocal counts

        if file_type not in counts:
            counts[file_type] = 0
        counts[file_type] += 1
        result = func_to_decorate(doc, file_type)

        return result, counts

    return wrapper


# don't touch above this line

# Nhiệm vụ của bạn:
# 1. "Trang trí" hàm của bạn với @file_type_aggregator
# 2. Định nghĩa một hàm tên là `process_doc`
# 3. Hàm đó nhận 2 tham số: `doc` và `file_type`
# 4. Bên trong hàm, trả về chuỗi f-string theo yêu cầu: f"Processing doc: '{doc}'. File Type: {file_type}"


@file_type_aggregator
def process_doc(doc, file_type):
    return f"Processing doc: '{doc}'. File Type: {file_type}"

