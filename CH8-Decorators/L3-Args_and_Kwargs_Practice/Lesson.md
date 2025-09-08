# Args and Kwargs Practice

Doc2Doc should be extensible to allow for third-party plugins. These plugins will be configurable.

## Assignment

Complete the `configure_plugin_decorator` function. It decorates a `func` that takes keyword arguments `**kwargs`, but the wrapper function it returns takes positional arguments `*args`. The arguments passed to the wrapper will be a series of tuples, each a key/value pair.

1. Create a wrapper function that takes positional arguments `*args`:
   1. Within the wrapper function, convert the `args` into a dictionary with the [`dict`](https://docs.python.org/3/library/stdtypes.html#dict) function.
   2. Return the result of passing this dictionary into `func` as keyword arguments unpacked with the [`**`](https://www.bitecode.dev/i/140708565/unpacking-arguments) operator.
2. Return the wrapper function.

```python
plugin_config = configure_backups(("path", "~/duplicates"), ("prefix", "duplicate_"), ("extension", ".rtf"))

# plugin_config:
# {
#   "path": "~/duplicates",
#   "prefix": "duplicate_",
#   "extension": ".rtf",
# }
```

## Gemini Translation

### Thực hành về Args và Kwargs

Mục tiêu là làm cho hệ thống Doc2Doc có thể mở rộng bằng cách cho phép các plugin của bên thứ ba. Các plugin này sẽ có thể được cấu hình.

#### Yêu cầu

Hãy hoàn thiện hàm `configure_plugin_decorator`. Hàm này sẽ "trang trí" (decorate) một hàm `func` vốn nhận các tham số có tên (`**kwargs`), nhưng hàm `wrapper` mà nó trả về sẽ nhận các tham số vị trí (`*args`). Các tham số được truyền vào `wrapper` sẽ là một chuỗi các cặp `tuple`, mỗi `tuple` là một cặp khóa/giá trị (key/value).

1. Tạo một hàm `wrapper` nhận vào các tham số vị trí `*args`:
   1. Bên trong hàm `wrapper`, hãy chuyển đổi `args` thành một dictionary bằng hàm `dict()`.
   2. Trả về kết quả của việc truyền dictionary này vào hàm `func` dưới dạng các tham số có tên bằng cách sử dụng toán tử giải nén `**`.
2. Trả về hàm `wrapper`.

```python
plugin_config = configure_backups(("path", "~/duplicates"), ("prefix", "duplicate_"), ("extension", ".rtf"))

# plugin_config sẽ là:
# {
#   "path": "~/duplicates",
#   "prefix": "duplicate_",
#   "extension": ".rtf",
# }
```

**Câu hỏi từ Gemini:** Làm thế nào trong Python để chúng ta có thể chuyển một danh sách các cặp (key, value) như `[("path", "~/duplicates"), ("prefix", "duplicate_")]` thành một dictionary?
