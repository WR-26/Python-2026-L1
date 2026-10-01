import os
import json
import zipfile
from domains import Student, Course

DATA_FILE = "students.dat"        # Tên file nén tổng hợp[cite: 4]
STUDENTS_TXT = "students.txt"     # File tạm chứa thông tin sinh viên
COURSES_TXT = "courses.txt"       # File tạm chứa thông tin môn học

def save_data(students, courses):
    """
    YÊU CẦU PW5: Lưu dữ liệu ra các file văn bản, sau đó nén lại thành file students.dat[cite: 4]
    """
    # 1. Chuyển đổi dữ liệu đối tượng thành dạng từ điển (Dictionary/JSON)
    students_data = [s.to_dict() for s in students.values()]
    courses_data = [c.to_dict() for c in courses.values()]

    # 2. Ghi ra các file văn bản tạm thời
    with open(STUDENTS_TXT, "w", encoding="utf-8") as f:
        json.dump(students_data, f, ensure_ascii=False, indent=4)

    with open(COURSES_TXT, "w", encoding="utf-8") as f:
        json.dump(courses_data, f, ensure_ascii=False, indent=4)

    # 3. Tiến hành nén các file văn bản vào students.dat sử dụng chuẩn zipfile.ZIP_DEFLATED[cite: 4]
    with zipfile.ZipFile(DATA_FILE, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(STUDENTS_TXT)
        zipf.write(COURSES_TXT)

    # 4. Xóa các file văn bản tạm thời sau khi nén thành công
    if os.path.exists(STUDENTS_TXT):
        os.remove(STUDENTS_TXT)
    if os.path.exists(COURSES_TXT):
        os.remove(COURSES_TXT)


def load_data():
    """
    YÊU CẦU PW5: Kiểm tra nếu students.dat tồn tại -> giải nén và tải dữ liệu lên bộ nhớ[cite: 4]
    """
    students = {}
    courses = {}

    # Kiểm tra sự tồn tại của file students.dat[cite: 4]
    if not os.path.exists(DATA_FILE):
        return students, courses

    try:
        # Mở và đọc nội dung trực tiếp từ file nén students.dat[cite: 4]
        with zipfile.ZipFile(DATA_FILE, "r") as zipf:
            # Tải danh sách khóa học
            if COURSES_TXT in zipf.namelist():
                with zipf.open(COURSES_TXT) as f:
                    courses_raw = json.load(f)
                    for item in courses_raw:
                        c = Course(item["id"], item["name"], item["credits"])
                        courses[c.id] = c

            # Tải danh sách sinh viên và bảng điểm
            if STUDENTS_TXT in zipf.namelist():
                with zipf.open(STUDENTS_TXT) as f:
                    students_raw = json.load(f)
                    for item in students_raw:
                        s = Student(item["id"], item["name"], item["dob"])
                        s.marks = item.get("marks", {})
                        students[s.id] = s

        # Tính toán lại GPA cho toàn bộ sinh viên vừa khôi phục
        for s in students.values():
            s.calculate_gpa(courses)

    except Exception as e:
        pass

    return students, courses