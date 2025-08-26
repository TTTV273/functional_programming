# Recursion Review

![xkcd comic](https://imgs.xkcd.com/comics/tabletop_roleplaying.png)

-- [xkcd](https://xkcd.com/244/)

*I hate explaining jokes, but in case you don't get the comic:* The joke is that the characters within the Dungeons and Dragons game are *also* playing their own Dungeons and Dragons game. Maybe *their* character's game of DnD also has characters playing DnD, and so on, recursively forever.

## Another Example

```python
def print_chars(word, i):
    # Base case: if index i equals word length, stop
    if i == len(word):
        return
    # Print character at position i
    print(word[i])
    # Recursive step: call function with i + 1
    print_chars(word, i + 1)

print_chars("Hello", 0)
# H
# e
# l
# l
# o
```

The `print_chars` example demonstrates the two core components of recursion clearly:

1. **Base case**: `if i == len(word): return` - this is where the function stops
2. **Recursive step**: `print_chars(word, i + 1)` - the function calls itself with a smaller problem (processing from the next position)

---

## Gemini Translation

**Ôn tập về Đệ quy**

-- [xkcd](https://xkcd.com/244/)

*Tôi ghét phải giải thích mấy trò đùa, nhưng phòng khi bạn không hiểu mẩu truyện này:* Trò đùa ở đây là các nhân vật trong trò chơi Dungeons and Dragons lại đang *chơi* một ván Dungeons and Dragons của riêng họ. Có lẽ các nhân vật trong ván DnD *của họ* cũng có những nhân vật đang chơi DnD, và cứ thế, đệ quy mãi mãi.

## Một ví dụ khác

```python
def print_chars(word, i):
    # Trường hợp cơ sở: nếu chỉ số i bằng độ dài của từ, thì dừng lại.
    if i == len(word):
        return
    # In ra ký tự tại vị trí i
    print(word[i])
    # Bước đệ quy: gọi lại hàm với chỉ số i + 1
    print_chars(word, i + 1)

print_chars("Hello", 0)
# Kết quả:
# H
# e
# l
# l
# o
```

Ví dụ `print_chars` này cũng thể hiện rất rõ hai phần cốt lõi của đệ quy:

1. **Trường hợp cơ sở**: `if i == len(word): return`, đây là lúc hàm dừng lại.
2. **Bước đệ quy**: `print_chars(word, i + 1)`, hàm gọi lại chính nó với bài toán nhỏ hơn (xét từ vị trí tiếp theo).

Tiếp theo, chúng ta nên xem các tệp bài tập trong thư mục này để biết nhiệm vụ là gì nhé!
