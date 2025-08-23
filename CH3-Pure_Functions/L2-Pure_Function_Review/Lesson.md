# Pure Function Review

Pure functions have a *lot* of benefits. Whenever possible, good developers try to use pure functions instead of impure functions. Remember, pure functions:

- Return the same result if given the same arguments. They are [deterministic](https://en.wikipedia.org/wiki/Deterministic_system).
- Do not change the external state of the program. For example, they do not change any variables outside of their scope.
- Do not perform any [I/O operations](https://en.wikipedia.org/wiki/Input/output) (like reading from disk, accessing the internet, or writing to the console).

These properties result in pure functions being easier to test, debug, and think about.

Refer to the following examples and answer the questions.

## Example 1

```python
def multiply_by2(nums):
    products = []
    for num in nums:
        products.append(num*2)
    return products
```

## Example 2

```python
balance = 1000
cars = []

def buy_car(new_car):
    global balance
    cars.append(new_car)
    balance -= 69
```

## Example 3

```python
import random

def roll_die(num_sides):
    return random.randint(1, num_sides)
```

## Gemini Translation

### **Ôn Tập Về Hàm Thuần Khiết (Pure Function)**

Hàm thuần khiết có *rất nhiều* lợi ích. Bất cứ khi nào có thể, các lập trình viên giỏi luôn cố gắng sử dụng hàm thuần khiết thay vì hàm không thuần khiết. Hãy nhớ rằng, hàm thuần khiết có các đặc điểm sau:

* **Có thể dự đoán (Deterministic):** Luôn trả về cùng một kết quả nếu được cung cấp cùng một đối số đầu vào.
* **Không có tác dụng phụ (No Side Effects):**
    * Không làm thay đổi trạng thái bên ngoài của chương trình (ví dụ: không thay đổi bất kỳ biến nào nằm ngoài phạm vi của nó).
    * Không thực hiện bất kỳ hoạt động **I/O** nào (viết tắt của Input/Output - Nhập/Xuất), ví dụ như đọc file từ ổ đĩa, truy cập internet, hay in ra màn hình console.

Những đặc tính này giúp cho hàm thuần khiết trở nên **dễ kiểm thử (test), dễ gỡ lỗi (debug), và dễ suy luận hơn**.

Bây giờ, chúng ta sẽ xem qua 3 ví dụ dưới đây.

-----

#### **Ví dụ 1**

```python
def multiply_by2(nums):
    products = []
    for num in nums:
        products.append(num*2)
    return products
```

#### **Ví dụ 2**

```python
balance = 1000
cars = []

def buy_car(new_car):
    global balance
    cars.append(new_car)
    balance -= 69
```

#### **Ví dụ 3**

```python
import random

def roll_die(num_sides):
    return random.randint(1, num_sides)
```

-----

Bây giờ, hãy bắt đầu với **Ví dụ 1**. Dựa vào các định nghĩa ở trên, theo anh, hàm `multiply_by2` có phải là một hàm thuần khiết không? Tại sao?
