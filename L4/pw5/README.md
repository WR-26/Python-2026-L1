# Student Mark Management System - PW5 (Persistent Information)

Dự án Quản lý Điểm Sinh viên được xây dựng theo mô hình **Lập trình Hướng đối tượng (OOP)**, cấu trúc **Phân chia Mô-đun (Modularization)** và tích hợp **Lưu trữ dữ liệu tự động dưới dạng file nén** dành cho bài tập thực hành môn Python tại USTH[cite: 1, 3, 4].

---

## 📌 Giới thiệu (Overview)

Chương trình được nâng cấp từ bài tập PW4[cite: 3, 4], bổ sung cơ chế nén/giải nén dữ liệu tự động bằng thư viện `zipfile`[cite: 4]. Khi khởi chạy, ứng dụng tự động kiểm tra và giải nén file `students.dat` để tải dữ liệu cũ[cite: 4]. Khi thoát, toàn bộ dữ liệu sinh viên, môn học và điểm số sẽ được ghi ra file văn bản rồi nén đóng gói lại thành file `students.dat`[cite: 4].

---

## 🏗️ Cấu trúc thư mục (Project Structure)

```text
pw5/
├── domains/                # Package chứa các lớp đối tượng chính (Domain models)
│   ├── __init__.py         # Khởi tạo package domains
│   ├── student.py          # Lớp Student & Logic tính GPA bằng NumPy
│   └── course.py           # Lớp Course quản lý thông tin môn học
├── persistence.py          # Module xử lý ghi/đọc file và nén/giải nén students.dat
├── input.py                # Module quản lý các chức năng nhập dữ liệu Curses UI
├── output.py               # Module quản lý các chức năng hiển thị Curses UI
├── main.py                 # File điều phối chính (Entry Point)
└── README.md               # Tài liệu hướng dẫn dự án
```

---

## ✨ Tính năng chính (Key Features)

* **Lưu trữ dữ liệu nén (Persistent Info)**: Tự động tải lại dữ liệu từ `students.dat` khi khởi động và tự động đóng gói nén toàn bộ dữ liệu thành file `students.dat` trước khi đóng chương trình[cite: 4].
* **Hướng đối tượng (OOP)**: Đóng gói toàn bộ logic và thuộc tính của `Student` và `Course` trong package `domains`[cite: 3].
* **Làm tròn điểm chuẩn**: Sử dụng module `math.floor()` làm tròn xuống 1 chữ số thập phân khi nhập điểm[cite: 2].
* **Tính GPA có trọng số**: Sử dụng mảng NumPy (`np.array`) tính tổng tích điểm và tín chỉ[cite: 2]:
  $$\text{GPA} = \frac{\sum (\text{Điểm môn} \times \text{Tín chỉ})}{\sum \text{Tín chỉ}}$$
* **Giao diện Curses UI**: Giao diện khung viền bảng biểu trực quan trên dòng lệnh Terminal[cite: 2].

---

## 🛠️ Yêu cầu & Cài đặt (Requirements & Setup)

### 1. Yêu cầu hệ thống
* Python 3.8 trở lên.
* Thư viện `numpy`[cite: 2].
* Thư viện `windows-curses` (dành cho hệ điều hành Windows)[cite: 2].

### 2. Cài đặt các thư viện cần thiết

```bash
pip install numpy
```

> **Lưu ý với hệ điều hành Windows:**
> ```bash
> pip install windows-curses
> ```

---

## 🚀 Hướng dẫn chạy chương trình (How to Run)

1. Mở Terminal và di chuyển vào thư mục dự án `pw5`[cite: 4]:
   ```bash
   cd pw5
   ```

2. Thực thi file script chính `main.py`[cite: 4]:
   ```bash
   python main.py
   ```

---

## 📋 Hướng dẫn sử dụng Menu

1. **1. Nhap thong tin Sinh vien**: Thêm sinh viên (Mã SV, Họ tên, Ngày sinh).
2. **2. Nhap thong tin Khoa hoc**: Thêm môn học mới (Mã môn, Tên môn, Số tín chỉ).
3. **3. Nhap diem mon hoc**: Chọn môn học và nhập điểm cho từng sinh viên (tự động làm tròn down 1 chữ số thập phân).
4. **4. Hien thi danh sach Sinh vien**: Bảng xếp hạng sinh viên sắp xếp giảm dần theo GPA.
5. **5. Hien thi danh sach Khoa hoc**: Xem danh sách môn học và số tín chỉ.
6. **6. Hien thi Bang diem theo mon hoc**: Tra cứu điểm thi từng môn học.
7. **0. Luu du lieu va Thoat chuong trinh**: Lưu và nén toàn bộ dữ liệu vào `students.dat` rồi thoát[cite: 4].

---

## 📤 Hướng dẫn đưa dự án lên GitHub (Push to GitHub)

1. Mở Terminal tại thư mục `pw5`:
   ```bash
   cd pw5
   ```

2. Thực hiện các thao tác Git:
   ```bash
   git init
   git add .
   git commit -m "Complete PW5: Persistent Info with students.dat compression"
   git branch -M main
   git remote add origin [https://github.com/USERNAME/REPOSITORY_NAME.git](https://github.com/USERNAME/REPOSITORY_NAME.git)
   git push -u origin main
   ```

---

## 👤 Thông tin Tác giả

* **Họ và tên**: Nguyễn Hữu Dũng
* **Mã sinh viên**: 2410234
* **Lớp**: 261ICT2013.L2
* **Trường**: Đại học Khoa học và Công nghệ Hà Nội (USTH)