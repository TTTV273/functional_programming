# Recursion Review

Recursion is *so dang useful* with tree-like structures because we don't always know how deep they're nested. Stop and think about how you would write nested loops to traverse a tree of arbitrary depth... it's not easy, is it?

```python
for item in tree:
    for nested_item in item:
        for nested_nested_item in nested_item:
            for nested_nested_nested_item in nested_nested_item:
                # ... WHEN DOES IT END???
```

I most often use recursion on tree-like problems (file systems, nested dictionaries, etc). If I'm just iterating over a one-dimensional list then a loop (*gasp...*) is typically simpler, even if it's not as "pure" in the academic sense.

*Remember: The rules of functional programming are just philosophies to help you write better code, but it's not always the right tool for the job.* The same goes for any programming paradigm.

## Gemini Translation

# **Ôn tập về Đệ quy**

Đệ quy ***cực kỳ hữu ích*** với các cấu trúc dạng cây vì chúng ta không phải lúc nào cũng biết chúng được lồng vào nhau sâu đến mức nào. Anh hãy thử dừng lại và suy nghĩ xem mình sẽ viết các vòng lặp lồng nhau để duyệt qua một cây có độ sâu tùy ý như thế nào... không hề dễ, phải không?

```python
for item in tree:
    for nested_item in item:
        for nested_nested_item in nested_item:
            for nested_nested_nested_item in nested_nested_item:
                # ... KHI NÀO NÓ MỚI KẾT THÚC???
```

Bản thân em thường sử dụng đệ quy nhất cho các bài toán dạng cây (ví dụ: duyệt hệ thống tệp, từ điển lồng nhau, v.v.). Nếu chỉ cần lặp qua một danh sách một chiều (one-dimensional list) thì một vòng lặp (*gasp...*) thường sẽ đơn giản hơn, ngay cả khi nó không được coi là "thuần túy" (pure) theo nghĩa học thuật.

***Hãy nhớ rằng: Các quy tắc của lập trình hàm chỉ là những triết lý giúp anh viết code tốt hơn, nhưng chúng không phải lúc nào cũng là công cụ phù hợp cho mọi công việc.*** Điều này cũng đúng với bất kỳ hệ quy chiếu lập trình (programming paradigm) nào.