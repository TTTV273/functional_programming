# Recursion Practice

In Doc2Doc, we have a search function to find the longest word in a document.

## Assignment

Complete the `find_longest_word` function without a loop. It accepts string inputs, `document`, and optional `longest_word`, which is the current longest word and defaults to an empty string.

1.  Check if the first word is longer than the current `longest_word`, then recur for the rest of the document.
   - Words with equal length to `longest_word` should be skipped.

2.  Ensure there are no potential [index errors](https://docs.python.org/3/library/exceptions.html#IndexError).

Assume that a "word" means a series of any consecutive non-whitespace characters. For example, `find_longest_word("How are you?")` should return the string `"you?"`.

> **Tip**: You can use [`.split`](https://docs.python.org/3/library/stdtypes.html#str.split) with `maxsplit=1`.  
> That will split a string into a list of `[first_word, rest_of_string]`

## Gemini Translation

## **Bài thực hành về Đệ quy**

Nhiệm vụ của chúng ta là hoàn thành hàm `find_longest_word` để tìm từ dài nhất trong một văn bản.

### **Yêu cầu**

Hoàn thành hàm `find_longest_word` **mà không sử dụng vòng lặp**. Hàm này nhận vào:
* `document`: một chuỗi ký tự.
* `longest_word`: một tham số tùy chọn, là từ dài nhất tìm thấy được cho đến hiện tại (mặc định là một chuỗi rỗng `""`).

**Luật xử lý:**
1. Kiểm tra xem từ đầu tiên có dài hơn `longest_word` hiện tại không.
   * Nếu một từ có độ dài bằng với `longest_word`, hãy bỏ qua nó.
2. Thực hiện gọi đệ quy cho phần còn lại của văn bản.
3. Phải đảm bảo không xảy ra lỗi chỉ mục (`IndexError`), ví dụ như khi văn bản trống.

> **Mẹo**: Bạn có thể dùng phương thức `.split()` với tham số `maxsplit=1`. Nó sẽ tách một chuỗi thành một danh sách gồm `[từ_đầu_tiên, phần_còn_lại_của_chuỗi]`.

Để giải quyết bất kỳ bài toán đệ quy nào, chúng ta luôn cần xác định hai yếu tố cốt lõi:

1. **Trường hợp cơ sở (Base Case) 🛑:** Đây là điều kiện dừng, là trường hợp đơn giản nhất mà hàm có thể trả về kết quả ngay lập tức mà không cần gọi lại chính nó.
2. **Bước đệ quy (Recursive Step) 🔄:** Đây là cách chúng ta giải quyết một phần nhỏ của bài toán và sau đó gọi lại chính hàm đó để giải quyết phần còn lại, nhỏ hơn.

Chúng ta hãy bắt đầu với phần đầu tiên nhé. Theo bạn, **trường hợp cơ sở** cho hàm `find_longest_word` này là gì? Tức là, khi nào thì hàm nên dừng lại?