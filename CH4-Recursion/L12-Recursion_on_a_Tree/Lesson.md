# Recursion on a Tree

Recursion is often used in "tree-like" structures. For example:

- Nested dictionaries
- File systems
- HTML documents
- JSON objects

That's because trees can have *unknown* depth. It's hard to write a series of loops because you don't know how many levels deep the tree goes.

```python
for entry_i in directory:
    if entry_i.is_dir:
        for entry_j in entry_i:
            if entry_j.is_dir:
                for entry_k in entry_j:
                    ...
```

## Assignment

You're responsible for a module in Doc2Doc that can scan a file system (represented in our code as nested dictionaries) and create a list of the filenames.

Complete the recursive `list_files` function. It accepts two arguments:

- `parent_directory`: A dictionary of dictionaries representing the current directory. A child directory's value is a dictionary and a file's value is `None`.
- `current_filepath`: A string representing the current path (e.g. `/dir1/dir2/filename.txt`)

It should return a list of all filepaths in the `parent_directory`.

## Steps

1.  Create an empty list to store the file paths.
2.  Use a `for-loop` to iterate through the keys of the `parent_directory` dictionary:
   1.  Use the key to create a new file path by concatenating a slash `/` and the key to the end of the `current_filepath`.
   2.  If the value is `None`, the key is a filename. `.append()` the new file path to the list of file paths.
   3.  Otherwise, the value is a child directory dictionary. Recursively call `list_files` with the child directory dictionary and the new file path.
   4.  Use [`.extend()`](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) to add the results of the recursive call to the list of file paths.
3.  Return the list of file paths.

Example `parent_directory`:

```python
{
    "Documents": {
        "Proposal.docx": None,
        "Receipts": {
            "January": {
                "receipt1.txt": None,
                "receipt2.txt": None
            },
            "February": {
                "receipt3.txt": None
            }
        }
    },
}
```

Resulting list of file paths:

```python
[
    "/Documents/Proposal.docx",
    "/Documents/Receipts/January/receipt1.txt",
    "/Documents/Receipts/January/receipt2.txt",
    "/Documents/Receipts/February/receipt3.txt"
]
```

## Tips

- What's the base case? It looks a bit different than before, but it's just when a nested node's value is `None` because in that case we don't have any more directories to explore.
- You might be wondering why we used a loop! Loops are nice when we know how many times we need to iterate (the number of keys in the dictionary). Recursion is nice when we don't know how many times we need to iterate (the number of nested dictionaries).
- Use `.extend()` to add a list's items to another list:

```python
items = ["six-string lute", "petrified dragon egg", "the only ring"]
items.extend(["philospher's stone", "invisibility cloak", "moistened scimitar"])
# ["six-string lute", "petrified dragon egg", "the only ring", "philospher's stone", "invisibility cloak", "moistened scimitar"]
```

## Gemini Translation

# **Đệ quy trên một Cấu trúc Cây**

Đệ quy thường được sử dụng trong các cấu trúc "dạng cây". Ví dụ:

- Từ điển lồng nhau (Nested dictionaries)
- Hệ thống tệp (File systems)
- Tài liệu HTML
- Đối tượng JSON

Đó là bởi vì các cây có thể có độ sâu ***không xác định***. Rất khó để viết một loạt các vòng lặp vì bạn không biết cây đó đi sâu bao nhiêu cấp.

```python
for entry_i in directory:
    if entry_i.is_dir:
        for entry_j in entry_i:
            if entry_j.is_dir:
                for entry_k in entry_j:
                    ... # Biết bao giờ mới hết?
```

# **Nhiệm vụ**

Anh đang chịu trách nhiệm cho một module trong Doc2Doc có thể quét một hệ thống tệp (được biểu diễn trong code của chúng ta dưới dạng các từ điển lồng nhau) và tạo ra một danh sách các tên tệp.

Hãy hoàn thành hàm đệ quy `list_files`. Hàm này chấp nhận hai đối số:

- `parent_directory`: Một từ điển của các từ điển, đại diện cho thư mục hiện tại. Giá trị của một thư mục con là một từ điển, và giá trị của một tệp là `None`.
- `current_filepath`: Một chuỗi đại diện cho đường dẫn hiện tại (ví dụ: `/dir1/dir2/filename.txt`)

Hàm này phải trả về một danh sách tất cả các đường dẫn tệp trong `parent_directory`.

Bài toán này rất giống với ví dụ "tìm kho báu trong rương" của chúng ta, nhưng lần này mục tiêu là **liệt kê tất cả các tệp** thay vì chỉ tìm một thứ.

Dựa vào kinh nghiệm từ ví dụ trước, khi bắt đầu viết hàm `list_files`, bước đầu tiên anh nghĩ chúng ta nên làm là gì?