# Recursion

[Recursion](https://en.wikipedia.org/wiki/Recursion_(computer_science)) is a famously tricky concept to grasp, but it's honestly quite simple - don't let it intimidate you! A recursive function is just a function that calls itself!

Recursion is the process of defining something in terms of itself.

[Link to Video: Recursion Explained](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/Recursion-explained.mp4)

## Example of Recursion

If you thought loops were the only way to iterate over a list, you were wrong! Recursion is fundamental to functional programming because it's how we iterate over lists while avoiding stateful loops. Take a look at this function that sums the numbers in a list:

```python
def sum_nums(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sum_nums(nums[1:])

print(sum_nums([1, 2, 3, 4, 5]))
# 15
```

Don't break your brain on the example above! Let's break it down step by step:

### 1. Solve a Small Problem

Our goal is to sum all the numbers in a list, but we're not allowed to loop. So, we start by solving the smallest possible problem: summing the first number in the list with the rest of the list:

```python
return nums[0] + sum_nums(nums[1:])
```

### 2. Recurse

So, what actually happens when we call `sum_nums(nums[1:])`? Well, we're just calling `sum_nums` with a smaller list! In the first call, the `nums` input was `[1, 2, 3, 4, 5]`, but in the next call it's just `[2, 3, 4, 5]`. We just keep calling `sum_nums` with smaller and smaller lists.

### 3. The Base Case

So what happens when we get to the "end"? `sum_nums(nums[1:])` is called, but `nums[1:]` is an empty list because we ran out of numbers. We need to write a base case to stop the madness.

```python
if len(nums) == 0:
    return 0
```

The "base case" of a recursive function is the part of the function that does *not* call itself.

## Assignment

Doc2Doc can automatically generate various layouts for a page. There are a *lot* of possible layouts, so we need a [factorial](https://en.wikipedia.org/wiki/Factorial) function to calculate the total number of possible layouts.

Complete the `factorial_r` function. It should recursively calculate the factorial of a number.

A factorial is the product of all positive integers less than or equal to a number. For example, 5! (read: "five factorial") is `5 * 4 * 3 * 2 * 1`, which is 120.

## Tips

1.  What's a small problem you can solve first?
2.  How can you go from the "first" value of x to the "next" value of x, all the way down to the "last" value of x?
3.  What's the base case that should stop the recursion?
4.  Since 0! is an [empty product](https://en.wikipedia.org/wiki/Empty_product), what should an input of 0 return?

---
## Gemini translations

# Đệ quy

[Đệ quy (Recursion)](https://en.wikipedia.org/wiki/Recursion_(computer_science)) là một khái niệm nổi tiếng khó nắm bắt, nhưng thực sự nó khá đơn giản - đừng để nó làm bạn sợ! Một hàm đệ quy chỉ là một hàm tự gọi chính nó!

Đệ quy là quá trình định nghĩa một cái gì đó bằng chính nó.

[Link tới Video: Giải thích về Đệ quy](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/Recursion-explained.mp4)

## Ví dụ về Đệ quy

Nếu bạn nghĩ rằng vòng lặp là cách duy nhất để duyệt qua một danh sách, bạn đã nhầm! Đệ quy là nền tảng của lập trình hàm vì đó là cách chúng ta duyệt qua các danh sách trong khi tránh các vòng lặp có trạng thái. Hãy xem hàm tính tổng các số trong một danh sách sau:

```python
def sum_nums(nums):
    # Trường hợp cơ sở: nếu danh sách rỗng, trả về 0
    if len(nums) == 0:
        return 0
    # Bước đệ quy: trả về phần tử đầu tiên cộng với tổng của phần còn lại
    return nums[0] + sum_nums(nums[1:])

print(sum_nums([1, 2, 3, 4, 5]))
# 15
```

Đừng làm mình rối não với ví dụ trên! Chúng ta hãy phân tích nó từng bước một:

### 1. Giải quyết một bài toán nhỏ

Mục tiêu của chúng ta là tính tổng tất cả các số trong một danh sách, nhưng không được phép dùng vòng lặp. Vì vậy, chúng ta bắt đầu bằng cách giải quyết bài toán nhỏ nhất có thể: tính tổng số đầu tiên trong danh sách với phần còn lại của danh sách:

```python
return nums[0] + sum_nums(nums[1:])
```

### 2. Đệ quy

Vậy, điều gì thực sự xảy ra khi chúng ta gọi `sum_nums(nums[1:])`? Chà, chúng ta chỉ đang gọi `sum_nums` với một danh sách nhỏ hơn! Trong lần gọi đầu tiên, đầu vào `nums` là `[1, 2, 3, 4, 5]`, nhưng trong lần gọi tiếp theo, nó chỉ còn là `[2, 3, 4, 5]`. Chúng ta tiếp tục gọi `sum_nums` với các danh sách ngày càng nhỏ hơn.

### 3. Trường hợp cơ sở (Base Case)

Vậy điều gì xảy ra khi chúng ta đến "cuối cùng"? `sum_nums(nums[1:])` được gọi, nhưng `nums[1:]` là một danh sách rỗng vì chúng ta đã hết số. Chúng ta cần viết một trường hợp cơ sở để dừng lại.

```python
if len(nums) == 0:
    return 0
```

"Trường hợp cơ sở" của một hàm đệ quy là phần của hàm mà *không* tự gọi chính nó.

## Bài tập

Doc2Doc có thể tự động tạo ra các bố cục khác nhau cho một trang. Có *rất nhiều* bố cục khả thi, vì vậy chúng ta cần một hàm [giai thừa (factorial)](https://en.wikipedia.org/wiki/Factorial) để tính tổng số bố cục có thể có.

Hoàn thành hàm `factorial_r`. Nó phải tính giai thừa của một số bằng phương pháp đệ quy.

Giai thừa là tích của tất cả các số nguyên dương nhỏ hơn hoặc bằng một số. Ví dụ, 5! (đọc là "năm giai thừa") là `5 * 4 * 3 * 2 * 1`, bằng 120.

## Gợi ý

1.  Bài toán nhỏ nào bạn có thể giải quyết trước?
2.  Làm thế nào bạn có thể đi từ giá trị "đầu tiên" của x đến giá trị "tiếp theo" của x, cho đến giá trị "cuối cùng" của x?
3.  Trường hợp cơ sở nào sẽ dừng đệ quy?
4.  Vì 0! là một [tích rỗng (empty product)](https://en.wikipedia.org/wiki/Empty_product), đầu vào là 0 nên trả về giá trị nào?

## ChatGPT Explanation
Anh ơi, em đã đọc được toàn bộ nội dung của bài học này. Em tóm gọn và giải thích lại để anh dễ hình dung nhé:

---

## 1. Khái niệm chính

* **Đệ quy (Recursion)**: Một hàm tự gọi lại chính nó.
* Ý tưởng: giải quyết một bài toán lớn bằng cách chia nó thành **bài toán nhỏ hơn cùng dạng** + **trường hợp cơ sở (base case)** để dừng.

---

## 2. Ví dụ minh họa: `sum_nums`

```python
def sum_nums(nums):
    if len(nums) == 0:   # Base case: danh sách rỗng
        return 0
    return nums[0] + sum_nums(nums[1:])  # Recursive case
```

* Nếu `nums = [1, 2, 3, 4, 5]`:

  * Bước 1: `1 + sum_nums([2,3,4,5])`
  * Bước 2: `1 + (2 + sum_nums([3,4,5]))`
  * Bước 3: `1 + (2 + (3 + sum_nums([4,5])))`
  * … cuối cùng khi list rỗng → trả về 0.

 Kết quả: 15.

---

## 3. Các bước cần nhớ khi viết hàm đệ quy

1. **Xác định bài toán nhỏ nhất** có thể giải (base case).
2. **Giảm bài toán lớn** thành bài toán nhỏ hơn (recursive step).
3. Đảm bảo mỗi lần gọi thì **tiến dần về base case**.

---

## 4. Bài tập trong bài học

Viết hàm **giai thừa** bằng đệ quy:

* Định nghĩa:

  * `n! = n * (n-1) * (n-2) ... * 1`
  * Ví dụ: `5! = 120`
* Đặc biệt: `0! = 1` (theo định nghĩa tích rỗng).

 Hàm cần viết: `factorial_r(n)` với 2 phần:

* Base case: khi `n == 0` → trả về 1.
* Recursive case: `n * factorial_r(n-1)`.

---

### Tóm lại

Đệ quy = **bài toán lớn → bài toán nhỏ hơn cùng loại → dừng ở base case**.
Trong bài này anh học:

* Cộng dãy số bằng đệ quy.
* Giai thừa là bài tập thực hành.

---

Anh có muốn em cùng anh code thử hàm `factorial_r(n)` rồi chạy với vài giá trị (ví dụ 5, 0, 1) để kiểm chứng không?

