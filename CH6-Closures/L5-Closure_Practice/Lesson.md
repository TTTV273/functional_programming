# Closure Practice

Doc2Doc should be able to add CSS styling to an HTML file. CSS uses selectors to identify the HTML element to add the style property. Essentially, styles are a chain of keys and values.

Complete the `css_styles` function. It accepts a nested dictionary as input, `initial_styles`, and returns a function, `add_style`.

1. Copies `initial_styles` to avoid modifying the original dictionary.

> **Warning**
> 
> Because we're dealing with nested dictionaries here, the `.copy()` method will produce a *shallow copy*: the outer dict is a new object, but mutating inner dicts will still affect the original one. So, you should use [`copy.deepcopy()`](https://docs.python.org/3/library/copy.html) instead.

2. Returns an `add_style` function that:
   1. Takes three string arguments: `selector`, `property`, and `value`. `selector` is a key in the `initial_styles` dictionary and its value should be a dictionary.
   2. Checks if the `selector` exists in the dictionary. If not, creates a new dictionary for the `selector` value.
   3. Then adds or updates the `property` with the given `value` for the selector.
   4. Returns the updated dictionary.

For example:

```python
initial_styles = {
    "body": {
        "background-color": "white",
        "color": "black"
    },
    "h1": {
        "font-size": "16px",
        "padding": "10px"
    }
}

add_style = css_styles(initial_styles)

new_styles = add_style("p", "color", "grey")
# {
#    "body": {
#        "background-color": "white",
#        "color": "black"
#    },
#    "h1": {
#        "font-size": "16px",
#        "padding": "10px"
#    },
#    "p": {
#        "color": "grey",
#    }
# }
```

## Gemini Translation

### Thực hành về Closure

Doc2Doc cần có khả năng thêm các định dạng CSS vào một file HTML. CSS sử dụng các "selector" (bộ chọn) để xác định phần tử HTML cần thêm thuộc tính định dạng. Về cơ bản, các định dạng này là một chuỗi các cặp key-value.

Hoàn thành hàm `css_styles`. Nó nhận đầu vào là một dictionary lồng nhau (nested dictionary), `initial_styles`, và trả về một hàm, `add_style`.

1. Sao chép `initial_styles` để tránh sửa đổi dictionary gốc.

   > **⚠️ Cảnh báo**
   >
   > Vì chúng ta đang làm việc với dictionary lồng nhau ở đây, phương thức `.copy()` sẽ tạo ra một *bản sao nông (shallow copy)*: dictionary bên ngoài là một đối tượng mới, nhưng việc thay đổi các dictionary bên trong vẫn sẽ ảnh hưởng đến cái gốc. Vì vậy, bạn nên sử dụng [`copy.deepcopy()`](https://docs.python.org/3/library/copy.html) thay thế.

2. Trả về một hàm `add_style` mà hàm đó:
   1. Nhận ba tham số chuỗi: `selector`, `property`, và `value`. `selector` là một key trong dictionary `initial_styles` và giá trị của nó nên là một dictionary.
   2. Kiểm tra xem `selector` có tồn tại trong dictionary không. Nếu không, tạo một dictionary mới cho giá trị của `selector`.
   3. Sau đó thêm hoặc cập nhật `property` với `value` đã cho của `selector`.
   4. Trả về dictionary đã được cập nhật.

Ví dụ:

```python
initial_styles = {
    "body": {
        "background-color": "white",
        "color": "black"
    },
    "h1": {
        "font-size": "16px",
        "padding": "10px"
    }
}

add_style = css_styles(initial_styles)

new_styles = add_style("p", "color", "grey")
# {
#    "body": {
#        "background-color": "white",
#        "color": "black"
#    },
#    "h1": {
#        "font-size": "16px",
#        "padding": "10px"
#    },
#    "p": {
#        "color": "grey",
#    }
# }
```

---

Bài học này giới thiệu một khái niệm mới rất quan trọng: sự khác biệt giữa **"sao chép nông" (`.copy()`)** và **"sao chép sâu" (`deepcopy`)**. Dựa vào phần "Cảnh báo" trong bài, anh có thể giải thích tại sao việc dùng `.copy()` thông thường sẽ không đủ an toàn trong trường hợp này không ạ?
```