# ====== QUẢN LÝ BÀN ĂN ======

# Danh sách bàn ăn (dạng dictionary)
# Ví dụ: {1: "trong", 2: "dang su dung"}
tables = {}

# ------------------------------------
# Thêm bàn mới
# ------------------------------------
def add_table(table_number):
    if table_number in tables:
        print("❌ Bàn đã tồn tại!")
    else:
        tables[table_number] = "trong"
        print("✅ Đã thêm bàn", table_number)

# ------------------------------------
# Xóa bàn
# ------------------------------------
def remove_table(table_number):
    if table_number in tables:
        del tables[table_number]
        print("🗑️ Đã xóa bàn", table_number)
    else:
        print("❌ Không tìm thấy bàn!")

# ------------------------------------
# Đánh dấu bàn đang dùng
# ------------------------------------
def use_table(table_number):
    if table_number in tables:
        tables[table_number] = "dang su dung"
        print("🍽️ Bàn", table_number, "đã được sử dụng")
    else:
        print("❌ Bàn không tồn tại!")

# ------------------------------------
# Đánh dấu bàn trống
# ------------------------------------
def free_table(table_number):
    if table_number in tables:
        tables[table_number] = "trong"
        print("🪑 Bàn", table_number, "đã được làm trống")
    else:
        print("❌ Bàn không tồn tại!")

# ------------------------------------
# Hiển thị danh sách bàn
# ------------------------------------
def show_tables():
    print("\n=== DANH SÁCH BÀN ĂN ===")
    for table, status in tables.items():
        print(f"Bàn {table}: {status}")

# ------------------------------------
# DEMO chạy thử
# ------------------------------------
add_table(1)
add_table(2)
add_table(3)

use_table(1)
free_table(2)
remove_table(3)

show_tables()
