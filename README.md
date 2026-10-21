# Python buổi 1 — Bài 1

Lập bảng giá trị chân lý của công thức trong Đại số mệnh đề.

## Chạy chương trình

Yêu cầu Python 3.8 trở lên, không cần cài thêm thư viện.

```bash
python bai1.py
```

Nhập công thức, ví dụ:

```text
p -> q
(p & q) -> r
(p -> q) <-> (~q -> ~p)
```

## Ký hiệu

| Ký hiệu | Ý nghĩa |
| --- | --- |
| `~` | Phủ định |
| `&` | Hội (và) |
| `\|` | Tuyển (hoặc) |
| `^` | Hoặc loại trừ |
| `->` | Kéo theo |
| `<->` | Tương đương |

Mỗi biến là một chữ cái ASCII (`a`–`z`, `A`–`Z`), có phân biệt chữ hoa và chữ thường.

Thứ tự ưu tiên từ cao xuống thấp: `~`, `&`, `^`, `|`, `->`, `<->`.
Dùng ngoặc để chỉ định thứ tự tính. Phép kéo theo kết hợp phải;
các phép hai ngôi còn lại kết hợp trái.

Chương trình liệt kê đủ 2ⁿ tổ hợp của n biến, theo thứ tự FALSE trước TRUE.
Công thức được phân tích trực tiếp, không sử dụng `eval()`.

## Ví dụ kết quả

Với công thức `p -> q`:

```text
  p   |   q   | p -> q
------+-------+-------
FALSE | FALSE |  TRUE
FALSE |  TRUE |  TRUE
 TRUE | FALSE | FALSE
 TRUE |  TRUE |  TRUE
```
