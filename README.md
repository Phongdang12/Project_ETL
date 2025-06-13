# Stock Data ETL with Python, Pandas, and MySQL

## Mô tả
Dự án này thực hiện quy trình **ETL (Extract - Transform - Load)**:
- **Extract:** Lấy dữ liệu chứng khoán (ví dụ: IBM) từ API của Alpha Vantage.
- **Transform:** Xử lý, chuyển đổi dữ liệu sang dạng bảng, tách ngày và giờ, làm sạch dữ liệu.
- **Load:** Lưu dữ liệu đã xử lý vào cơ sở dữ liệu MySQL.

## Yêu cầu
- Python 3.x
- MySQL server (đã tạo sẵn database, ví dụ: `test`)
- Các thư viện Python:
  - pandas
  - requests
  - sqlalchemy
  - pymysql

## Cài đặt thư viện
Chạy lệnh sau trong terminal:
```
python -m pip install pandas requests sqlalchemy pymysql
```

## Cấu hình MySQL
- Tạo database (nếu chưa có):
```sql
CREATE DATABASE test;
```

## Kết quả
- Dữ liệu chứng khoán sẽ được lưu vào bảng `stock_price` trong database MySQL.
- Bạn có thể kiểm tra dữ liệu bằng MySQL Workbench hoặc lệnh SQL:
```sql
SELECT * FROM stock_price LIMIT 10;
```

## Liên hệ
Nếu có thắc mắc, vui lòng liên hệ: phong.danghandsomek@hcmut.edu.vn
