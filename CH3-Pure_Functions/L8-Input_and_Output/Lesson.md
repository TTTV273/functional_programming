# Input and Output

![Comic by xkcd](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/SVpmfNV-1026x720.png)

Comic by [xkcd](https://xkcd.com/1790/).

The term "i/o" stands for input/output. In the context of writing programs, i/o refers to anything in our code that interacts with the "outside world". "Outside world" just means anything that's not stored in our application's memory (like variables).

## Examples of I/O

- Reading from or writing to a file on the hard drive
- Accessing the internet
- Reading from or writing to a database
- Even simply *printing to the console* is considered i/o!

*All i/o is a form of "side effect".*

## Assignment

In Doc2Doc, we frequently need to change the casing of some text. For example:

### TitleCase

> Every Day Once A Day Give Yourself A Present

### LowerCase

> every day once a day give yourself a present

### UpperCase

> EVERY DAY ONCE A DAY GIVE YOURSELF A PRESENT

There is an issue in the `convert_case` function, our test suite can't test its behavior because it's printing to the console (eww... a *side-effect*) instead of returning a value. Fix the function so that it returns the correct value instead of printing it.

## Gemini Translation

### **# Nhập và Xuất (Input and Output)**

*Truyện tranh của [xkcd](https://xkcd.com/1790/).*

Thuật ngữ **"I/O"** là viết tắt của **input/output** (nhập/xuất). Trong bối cảnh lập trình, I/O đề cập đến bất cứ thứ gì trong code của chúng ta tương tác với "thế giới bên ngoài". "Thế giới bên ngoài" ở đây đơn giản là mọi thứ không được lưu trữ trong bộ nhớ của ứng dụng (như các biến).

### **## Ví dụ về I/O**

* Đọc hoặc ghi vào một tập tin trên ổ cứng.
* Truy cập Internet.
* Đọc hoặc ghi vào cơ sở dữ liệu.
* Ngay cả việc đơn giản là ***in ra màn hình console*** cũng được coi là I/O!

***Tất cả các hoạt động I/O đều là một dạng "tác dụng phụ" (side effect).***

### **## Bài tập**

Trong dự án Doc2Doc, chúng ta thường xuyên cần thay đổi kiểu viết hoa/thường của một đoạn văn bản. Ví dụ:

#### **### TitleCase (Viết Hoa Chữ Cái Đầu)**

> Every Day Once A Day Give Yourself A Present

#### **### LowerCase (Viết thường)**

> every day once a day give yourself a present

#### **### UpperCase (Viết HOA)**

> EVERY DAY ONCE A DAY GIVE YOURSELF A PRESENT

Hiện có một vấn đề trong hàm `convert_case`. Bộ kiểm thử (test suite) của chúng ta không thể kiểm tra hành vi của nó vì nó đang in kết quả ra console (thật tệ... một *tác dụng phụ*) thay vì trả về một giá trị.

**Yêu cầu:** Hãy sửa lại hàm để nó trả về (return) giá trị chính xác thay vì in ra.