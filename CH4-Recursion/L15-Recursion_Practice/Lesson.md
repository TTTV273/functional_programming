# Recursion Practice
In Doc2Doc, we might have documents nested inside other documents, forming a kind of tree. You know how crazy `.docx` files can get...

Anyways, we want to find out how deeply nested a given document is.

## Assignment
Complete the `count_nested_levels` function.
1. [ ] Loop over `document_id`s in the `nested_documents` dictionary
    1. [ ] If the current `document_id` matches the `target_document_id`, return its `level` of nesting
    2. [ ] If the `target_document_id` is not found, recursively call `count_nested_levels` on the current `document_id` and increment the `level`
    3. [ ] If the recursive call found the `target_document_id`'s level, return it
2. [ ] If the `target_document_id` doesn't exist, the function should return `-1`

## Example
In this dictionary, the document with id `3` is nested 2 levels deep. Document `2` is nested 1 level deep.
```py
{
    1: {
        3: {}
    },
    2: {}
}
```

## Gemini Translation
# Thực hành Đệ quy
Trong Doc2Doc, chúng ta có thể có các tài liệu được lồng bên trong các tài liệu khác, tạo thành một dạng cây. Bạn biết các tệp `.docx` có thể trở nên phức tạp như thế nào rồi đấy...

Dù sao đi nữa, chúng ta muốn tìm ra một tài liệu nhất định được lồng sâu đến mức nào.

## Bài tập
Hoàn thành hàm `count_nested_levels`.
1. [ ] Lặp qua các `document_id` trong từ điển `nested_documents`
    1. [ ] Nếu `document_id` hiện tại khớp với `target_document_id`, trả về `level` (mức độ) lồng của nó
    2. [ ] Nếu không tìm thấy `target_document_id`, hãy gọi đệ quy `count_nested_levels` trên `document_id` hiện tại và tăng `level` lên
    3. [ ] Nếu lệnh gọi đệ quy tìm thấy level của `target_document_id`, hãy trả về nó
2. [ ] Nếu `target_document_id` không tồn tại, hàm sẽ trả về `-1`

## Ví dụ
Trong từ điển này, tài liệu có id `3` được lồng sâu 2 cấp. Tài liệu `2` được lồng sâu 1 cấp.
```py
{
    1: {
        3: {}
    },
    2: {}
}
```
