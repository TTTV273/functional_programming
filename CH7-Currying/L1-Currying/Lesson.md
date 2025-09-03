# Currying

Function [currying](https://en.wikipedia.org/wiki/Currying) is a specific *kind* of function transformation where we translate a single function that accepts multiple arguments into *multiple* functions that each accept a *single* argument.

This is a "normal" 3-argument function:

```py
box_volume(3, 4, 5)
```

This is a "curried" *series of functions* that does the same thing:

```py
box_volume(3)(4)(5)
```

Here's another example that includes the implementations:

```py
def sum(a, b):
  return a + b

print(sum(1, 2))
# prints 3
```

And the same thing curried:

```py
def sum(a):
  def inner_sum(b):
    return a + b
  return inner_sum

print(sum(1)(2))
# prints 3
```

The `sum` function only takes a *single* input, `a`. It returns a *new* function that takes a single input, `b`. This new function when called with a value for `b` will return the sum of `a` and `b`. *We'll talk later about why this is useful.*

## Assignment

In Doc2Doc, for some types of text files, we need to transform the font size of the text when rendering it onscreen.

Fix the `converted_font_size` function. We are using a 3rd party code library that expects our function to be a curried series of functions that each take a single argument.

- `converted_font_size` should just take a single argument, `font_size` and return a function that takes a single argument, `doc_type`. That function should return the `font_size` multiplied by the appropriate value for the given `doc_type`.

## Tip

You can always `Reset` the code to see the proper `font_size` multipliers if you accidentally change them.

## Gemini Translation

Được thôi anh. Em sẽ dịch toàn bộ nội dung bài học sang tiếng Việt trước nhé.

-----

### **Currying**

**Currying** một hàm là một dạng biến đổi hàm đặc biệt, nơi chúng ta chuyển một hàm duy nhất chấp nhận nhiều tham số thành **nhiều** hàm, mà mỗi hàm trong đó chỉ chấp nhận một tham số **duy nhất**.

Đây là một hàm 3 tham số "bình thường":

```python
box_volume(3, 4, 5)
```

Đây là một **chuỗi các hàm** đã được "curry hóa" và thực hiện điều tương tự:

```python
box_volume(3)(4)(5)
```

Đây là một ví dụ khác bao gồm cả phần triển khai code:

```python
# Hàm thông thường
def sum(a, b):
  return a + b

print(sum(1, 2))
# in ra 3
```

Và đây là hàm tương tự đã được curry hóa:

```python
# Hàm đã được curry hóa
def sum(a):
  def inner_sum(b):
    return a + b
  return inner_sum

print(sum(1)(2))
# in ra 3
```

Hàm `sum` ở trên chỉ nhận một đầu vào **duy nhất**, là `a`. Nó trả về một hàm **mới** (`inner_sum`), và hàm mới này cũng chỉ nhận một đầu vào duy nhất, là `b`. Khi hàm mới này được gọi với một giá trị cho `b`, nó sẽ trả về tổng của `a` và `b`. *Chúng ta sẽ bàn về lợi ích của việc này sau.*

#### **Bài tập**

Trong dự án Doc2Doc, đối với một số loại tệp văn bản, chúng ta cần thay đổi kích thước phông chữ của văn bản khi hiển thị nó trên màn hình.

Hãy sửa hàm `converted_font_size`. Chúng ta đang sử dụng một thư viện của bên thứ ba và thư viện này yêu cầu hàm của chúng ta phải là một chuỗi các hàm đã được curry hóa, mỗi hàm chỉ nhận một tham số.

  - `converted_font_size` chỉ nên nhận một tham số duy nhất là `font_size` và trả về một hàm khác.
  - Hàm trả về này cũng chỉ nhận một tham số duy nhất là `doc_type`.
  - Hàm đó sẽ trả về `font_size` nhân với giá trị phù hợp cho `doc_type` tương ứng.

#### **Mẹo**

Bạn luôn có thể nhấn `Reset` code để xem lại các hệ số nhân `font_size` chính xác nếu bạn vô tình thay đổi chúng.

-----

Đây là toàn bộ nội dung đã được dịch. Anh đọc qua một lượt nhé. Khi nào anh sẵn sàng, chúng ta có thể bắt đầu phân tích ví dụ về hàm `sum` để hiểu rõ hơn về cách nó hoạt động. Anh thấy sao?
