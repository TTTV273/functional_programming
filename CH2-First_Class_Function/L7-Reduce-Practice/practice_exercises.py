import functools


# Exercise 1: Sum Numbers (Warmup)
# Bài 1: Cộng các số (Khởi động)
def sum_numbers(numbers):
    """
    Use reduce to sum all numbers in the list.
    Dùng reduce để cộng tất cả số trong danh sách.

    Example: sum_numbers([1, 2, 3, 4]) -> 10
    """
    # TODO: Implement using functools.reduce
    # Hint: You need a function that takes (sum_so_far, next_number)
    # Gợi ý: Cần một hàm nhận (tổng_hiện_tại, số_tiếp_theo)
    return functools.reduce(add, numbers)


def add(sum_so_far, next_number):
    print(f"sum_so_far: {sum_so_far}, next_number: {next_number}")
    return sum_so_far + next_number


# Exercise 2: Find Maximum (Comparison)
# Bài 2: Tìm số lớn nhất (So sánh)
def find_maximum(numbers):
    """
    Use reduce to find the largest number in the list.
    Dùng reduce để tìm số lớn nhất trong danh sách.

    Example: find_maximum([3, 7, 2, 9, 1]) -> 9
    """
    # TODO: Implement using functools.reduce
    # Hint: You need a function that compares (max_so_far, next_number)
    # Gợi ý: Cần một hàm so sánh (max_hiện_tại, số_tiếp_theo)
    return functools.reduce(find_bigger, numbers)


def find_bigger(max_so_far, next_number):
    return max(max_so_far, next_number)


# Exercise 3: Count Words (Dictionary Accumulation)
# Bài 3: Đếm từ (Tích lũy từ điển)
def count_words(words):
    """
    Use reduce to count frequency of each word.
    Dùng reduce để đếm tần suất của mỗi từ.

    Example: count_words(["apple", "banana", "apple"]) -> {"apple": 2, "banana": 1}
    """
    # TODO: Implement using functools.reduce
    # Hint: Start with empty dict {}, accumulate word counts
    # Gợi ý: Bắt đầu với từ điển rỗng {}, tích lũy số lần đếm
    return functools.reduce(count_helper, words, {})


def count_helper(word_counts, next_word):
    if next_word in word_counts:
        word_counts[next_word] += 1
    else:
        word_counts[next_word] = 1
    return word_counts


# Exercise 4: Flatten Lists (List Accumulation)
# Bài 4: Làm phẳng danh sách (Tích lũy danh sách)
def flatten_lists(list_of_lists):
    """
    Use reduce to flatten a list of lists into a single list.
    Dùng reduce để làm phẳng danh sách các danh sách thành một danh sách duy nhất.

    Example: flatten_lists([[1, 2], [3, 4], [5]]) -> [1, 2, 3, 4, 5]
    """
    # TODO: Implement using functools.reduce
    # Hint: Start with empty list [], extend with each sublist
    # Gợi ý: Bắt đầu với danh sách rỗng [], mở rộng với mỗi danh sách con
    return functools.reduce(flatten_helper, list_of_lists, [])


def flatten_helper(combined_list, next_sublist):
    print(f"combined_list: {combined_list}, next_sublist: {next_sublist}")
    return combined_list + next_sublist


# Exercise 5: Build URL (Complex String Building)
# Bài 5: Xây dựng URL (Xây dựng chuỗi phức tạp)
def build_url(parts):
    """
    Use reduce to build a URL from parts, handling slashes correctly.
    Dùng reduce để xây dựng URL từ các phần, xử lý dấu gạch chéo đúng cách.

    Example: build_url(["https://api.example.com", "users", "123", "posts"])
             -> "https://api.example.com/users/123/posts"
    """
    # TODO: Implement using functools.reduce
    # Hint: First part is base, others are joined with "/"
    # Handle case where base might already end with "/"
    # Gợi ý: Phần đầu là base, các phần khác nối với "/"
    # Xử lý trường hợp base đã kết thúc bằng "/"
    return functools.reduce(url_helper, parts)


def url_helper(base_url, next_part):
    print(f"base_url: {base_url}, next_part: {next_part}")
    clean_right_part = next_part.rstrip("/")
    clean_part = clean_right_part.lstrip("/")
    if base_url.endswith("/"):
        return base_url + next_part
    else:
        return base_url + "/" + clean_part

