# Python buổi 1 — 3 bài thực hành

## Cài đặt và chạy

Yêu cầu Python 3.9 trở lên. Bài 1 và Bài 2 dùng thư viện chuẩn;
Bài 3 cần SymPy.

```bash
python -m pip install -r requirements.txt
python bai1.py
python bai2.py
python bai3.py
```

Chạy từng lệnh tương ứng với bài muốn làm.

## Bài 1 — Bảng giá trị chân lý

Nhập công thức với mỗi biến là một chữ cái ASCII, có phân biệt hoa thường.

| Ký hiệu | Phép toán |
| --- | --- |
| `~` | Phủ định |
| `&` | Hội |
| `\|` | Tuyển |
| `^` | Hoặc loại trừ |
| `->` | Kéo theo |
| `<->` | Tương đương |

Ưu tiên từ cao xuống thấp: `~`, `&`, `^`, `|`, `->`, `<->`.
Dùng ngoặc để chỉ định thứ tự. Kéo theo kết hợp phải, các phép hai ngôi
còn lại kết hợp trái. Chương trình không dùng `eval()`.

Ví dụ: `(p -> q) <-> (~q -> ~p)` cho kết quả TRUE ở mọi dòng.
Với `p -> q`, chỉ dòng p = TRUE, q = FALSE cho kết quả FALSE.

## Bài 2 — Tập hợp và xâu bit

Tập vũ trụ theo tài liệu:

```text
a b c d e f g h l m o p q r s t
```

Chương trình hoán vị U mỗi lần chạy. Vị trí bit được xác định theo **thứ tự U
sau hoán vị**: bit 1 khi phần tử thuộc tập, bit 0 khi không thuộc tập.
A, B và mọi kết quả đều dùng cùng thứ tự này.

Nhập A, B bằng các phần tử cách nhau bằng khoảng trắng, ví dụ:

```text
A: a c e m
B: c d m t
```

Kết quả gồm A, B, hai tập bù trong U, hợp, giao, hai hiệu và hiệu đối xứng;
mỗi tập có danh sách phần tử, xâu bit và số phần tử. Enter biểu diễn tập rỗng.
Phần tử nhập trùng được gộp; phần tử ngoài U bị báo lỗi.

## Bài 3 — Hệ thức truy hồi

Giải dạng tuyến tính thuần nhất hệ số hằng:

```text
a_n = c1*a_(n-1) + ... + ck*a_(n-k), n >= k
```

Nhập k hệ số rồi đúng k điều kiện đầu, bắt đầu từ a0. Hỗ trợ số nguyên,
phân số (`1/2`) và thập phân (`0.25`), tính toán bằng số hữu tỷ chính xác.

| Ví dụ | Hệ số | Điều kiện đầu | Kết quả |
| --- | --- | --- | --- |
| Fibonacci | `1 1` | `0 1` | 0, 1, 1, 2, 3, 5, ... |
| Nghiệm kép | `4 -4` | `1 4` | a_n = (n + 1) × 2^n |
| Nghiệm phức | `0 -1` | `1 0` | a_n = cos(n × pi/2) |

Chương trình in phương trình đặc trưng, nghiệm và bội, nghiệm tổng quát,
hằng số theo điều kiện đầu, công thức cuối và 10 số hạng đầu.
Nghiệm phức liên hợp được viết bằng sin/cos, giữ góc chính xác.
Nghiệm 0 dùng KroneckerDelta(n, j), bằng 1 khi n = j và bằng 0 khi n khác j.
Với đa thức bậc cao, SymPy có thể dùng CRootOf để biểu diễn nghiệm đại số;
việc tìm và rút gọn công thức có thể chậm.

## Kiểm tra

```bash
python -m unittest discover -s tests -v
```
