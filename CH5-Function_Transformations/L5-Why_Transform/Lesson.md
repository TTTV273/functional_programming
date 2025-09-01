# Why Transform?

You might be wondering:

- "When would I use function transformations in the real world?"
- "Isn't it simpler to just define functions at the top level of the code, and call them as needed?"

Good questions. To be clear, we don't just transform functions at [runtime](https://en.wikipedia.org/wiki/Execution_(computing)#Runtime) for the fun of it! We only use advanced techniques like function transformations when they make our code *simpler than it would otherwise be*.

## Code Reusability

Creating variations of the same function dynamically can make it a lot easier to share common functionality. Take a look at this `formatter` function. It accepts a "pattern" and returns a new function that formats text according to that pattern:

```python
def formatter(pattern):
    def inner_func(text):
        result = ""
        i = 0
        while i < len(pattern):
            if pattern[i:i+2] == '{}':
                result += text
                i += 2
            else:
                result += pattern[i]
                i += 1
        return result
    return inner_func
```

Now we can create new formatters easily:

```python
bold_formatter = formatter("**{}**")
italic_formatter = formatter("*{}*")
bullet_point_formatter = formatter("* {}")
```

And use them like this:

```python
print(bold_formatter("Hello"))
# **Hello**
print(italic_formatter("Hello"))
# *Hello*
print(bullet_point_formatter("Hello"))
# * Hello
```

## Closures

90% of the time, when I use function transformations, it's because I want to create a closure. We'll talk about closures in the next chapter!

## Gemini Translation

# Tại sao cần biến đổi hàm?

Có thể bạn đang tự hỏi:

- "Khi nào thì tôi nên sử dụng kỹ thuật biến đổi hàm trong thực tế?"
- "Chẳng phải sẽ đơn giản hơn nếu chỉ cần định nghĩa các hàm ở cấp cao nhất của code, rồi gọi chúng khi cần hay sao?"

Đây là những câu hỏi rất hay. Cần phải làm rõ rằng, chúng ta không biến đổi hàm lúc **runtime** (khi chương trình đang chạy) chỉ để cho vui! Chúng ta chỉ sử dụng các kỹ thuật nâng cao như biến đổi hàm khi chúng thực sự làm cho code của chúng ta trở nên *đơn giản hơn so với khi không dùng chúng*.

## Tái sử dụng code

Việc tự động tạo ra các biến thể của cùng một hàm có thể giúp chia sẻ các chức năng chung một cách dễ dàng hơn rất nhiều. Hãy xem hàm `formatter` dưới đây. Nó nhận vào một "mẫu" (pattern) và trả về một hàm mới dùng để định dạng văn bản theo mẫu đó:

```python
def formatter(pattern):
    def inner_func(text):
        result = ""
        i = 0
        while i < len(pattern):
            if pattern[i:i+2] == '{}':
                result += text
                i += 2
            else:
                result += pattern[i]
                i += 1
        return result
    return inner_func
```

Bây giờ, chúng ta có thể tạo ra các hàm định dạng mới một cách dễ dàng:

```python
bold_formatter = formatter("**{}**")
italic_formatter = formatter("*{}*")
bullet_point_formatter = formatter("* {}")
```

Và sử dụng chúng như sau:

```python
print(bold_formatter("Hello"))
# **Hello**
print(italic_formatter("Hello"))
# *Hello*
print(bullet_point_formatter("Hello"))
# * Hello
```

## Closure

Trong 90% trường hợp, khi tôi sử dụng kỹ thuật biến đổi hàm, đó là vì tôi muốn tạo ra một **closure**. Chúng ta sẽ tìm hiểu về closure trong chương tiếp theo!