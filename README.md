# WEBSITE CHIA SẺ & QUẢN LÝ TÀI LIỆU

Một TRANG web cơ bản được xây dựng bằng **Flask** (Python) và **SQLAlchemy**, cho phép người dùng đăng ký, đăng nhập và quản lý danh sách tài liệu cá nhân (Thêm, Sửa, Xóa, Tìm kiếm, Tải lên và tải xuống tệp tin).

---

## Tính năng chính

* **Xác thực người dùng:** Đăng ký tài liệu mới và Đăng nhập hệ thống được bảo mật bằng Session.
* **Quản lý tài liệu:** * **Xem** danh sách toàn bộ tài liệu đã lưu.
    * **Thêm mới** tài liệu kèm theo tiêu đề, danh mục và tệp tải lên (`.pdf`, `.docx`, hình ảnh, v.v.).
    * **Cập nhật** chỉnh sửa thông tin hoặc thay đổi tệp tin đã tải lên.
    * **Xóa** tài liệu không còn sử dụng.
* **Tìm kiếm thông minh:** Tìm kiếm tài liệu nhanh chóng theo Tiêu đề (`Title`) hoặc Danh mục (`Category`).

---

## Cấu trúc thư mục dự án

```text
Website_Project/
│
├── app.py               # File mã nguồn chính
├── documents.db         # Cơ sở dữ liệu SQLite (Tự động khởi tạo khi chạy ứng dụng)
│
├── uploads/             # Thư mục lưu trữ các tệp tin người dùng tải lên
│
├── static/              # Thư mục chứa tài nguyên tĩnh
│   └── style.css        # Giao diện CSS của ứng dụng
│
└── templates/           # Thư mục chứa các giao diện giao diện HTML
    ├── login.html       # Giao diện Đăng nhập
    ├── register.html    # Giao diện Đăng ký
    ├── index.html       # Trang chủ hiển thị danh sách tài liệu
    ├── add.html         # Giao diện Thêm tài liệu mới
    ├── edit.html        # Giao diện Chỉnh sửa tài liệu
    └── search.html      # Giao diện Tìm kiếm tài liệu

```

---

## Yêu cầu hệ thống & Cài đặt

Để chạy dự án này, bạn cần cài đặt sẵn **Python** , **Git** , **VSCode** hoặc bất kì một ứng dụng có chức năng tương tự trên máy tính và thực hiện các bước sau:

### 1. Bản sao dự án (Clone/Tải về)

```bash
git clone <link-github-cua-ban>

```

### 2. Cài đặt các thư viện cần thiết

Mở terminal tại thư mục dự án và cài đặt **Flask** cùng với **Flask-SQLAlchemy**:

```bash
pip install Flask Flask-SQLAlchemy

```

### 3. Khởi chạy ứng dụng

Chạy file `app.py` bằng lệnh:

```bash
python app.py hoặc flask run

```

Sau khi chạy lệnh thành công, hệ thống sẽ tự động tạo file cơ sở dữ liệu `documents.db` và thư mục `uploads/`.

### 4. Truy cập ứng dụng

Mở trình duyệt web của bạn và truy cập đường dẫn:

```text
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

```

---

## 🔑 Tài khoản thử nghiệm

Do hệ thống sử dụng cơ sở dữ liệu trống lúc ban đầu, bạn có thể tự tạo tài khoản mới tại trang `/register` hoặc sử dụng các chức năng trực tiếp sau khi đăng ký thành công.

---

## 🛡️ Các công nghệ sử dụng

* **Python, Flask Framework**
* **Flask-SQLAlchemy (SQLite)**
* **HTML, CSS (Static files)**

```

```
