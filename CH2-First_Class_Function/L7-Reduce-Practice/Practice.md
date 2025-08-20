# Reduce Practice Exercises

Five progressive exercises to master the reduce function and accumulator pattern.

## Exercise 1: Sum Numbers (Warmup)
**Goal**: Understand basic accumulator pattern with numbers
**Task**: Use reduce to sum a list of numbers
**Concepts**: Basic accumulation, numerical operations

## Exercise 2: Find Maximum (Comparison)
**Goal**: Use reduce for comparison operations
**Task**: Find the largest number in a list using reduce
**Concepts**: Comparison logic, conditional accumulation

## Exercise 3: Count Words (String Processing)
**Goal**: Accumulate counts using dictionaries
**Task**: Count word frequency in a list of words
**Concepts**: Dictionary accumulation, conditional updates

## Exercise 4: Flatten Lists (Data Structure)
**Goal**: Combine nested structures
**Task**: Flatten a list of lists into a single list
**Concepts**: List accumulation, extending collections

## Exercise 5: Build URL (String Building)
**Goal**: Complex string construction with rules
**Task**: Build a URL from parts with proper formatting
**Concepts**: Conditional string building, format validation

---

## Vietnamese Explanation / Giải thích bằng tiếng Việt

### Tại sao cần luyện tập reduce?

`reduce` khác với `map` và `filter` ở chỗ nó **gộp nhiều thành một**. Hãy tưởng tượng:

- **map**: Máy photocopy - mỗi trang vào ra một trang mới
- **filter**: Cái rây - lọc ra những cái cần giữ  
- **reduce**: Máy ép - gộp tất cả thành một khối duy nhất

### Pattern cơ bản của reduce:

```python
def my_reducer(accumulator, current_item):
    # accumulator = kết quả tích lũy từ các bước trước
    # current_item = phần tử hiện tại đang xử lý
    # return = kết quả mới sẽ trở thành accumulator cho bước tiếp theo
    return new_accumulator
```

Giống như lăn quả cầu tuyết: quả cầu (accumulator) ngày càng lớn khi lăn qua từng lớp tuyết mới (current_item).

### 5 bài tập từ dễ đến khó:

1. **Cộng số**: Quả cầu tuyết = tổng, lớp tuyết = số mới
2. **Tìm max**: Quả cầu = số lớn nhất, so sánh với số mới
3. **Đếm từ**: Quả cầu = từ điển đếm, cập nhật số lần xuất hiện
4. **Gộp danh sách**: Quả cầu = danh sách tổng, thêm danh sách con
5. **Xây URL**: Quả cầu = URL, thêm từng phần với quy tắc

Mỗi bài sẽ giúp anh hiểu sâu hơn về cách "quả cầu tuyết" có thể là số, chuỗi, danh sách, hay từ điển!