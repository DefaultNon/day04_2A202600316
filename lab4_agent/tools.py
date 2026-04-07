from langchain_core.tools import tool

# ============================================================
# MOCK DATA — Dữ liệu giả lập hệ thống du lịch
# ============================================================

FLIGHTS_DB = {
    ("Hà Nội", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "07:20", "price": 1450000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "14:00", "arrival": "15:20", "price": 2800000, "class": "business"},
        {"airline": "VietJet Air", "departure": "08:30", "arrival": "09:50", "price": 890000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "11:00", "arrival": "12:20", "price": 1200000, "class": "economy"},
    ],
    ("Hà Nội", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "07:00", "arrival": "09:15", "price": 2100000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "10:00", "arrival": "12:15", "price": 1350000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "16:00", "arrival": "18:15", "price": 1100000, "class": "economy"},
    ],
    ("Hà Nội", "Hồ Chí Minh"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "08:10", "price": 1600000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "07:30", "arrival": "09:40", "price": 950000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "12:00", "arrival": "14:10", "price": 1300000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "18:00", "arrival": "20:10", "price": 3200000, "class": "business"},
    ],
    ("Hồ Chí Minh", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "09:00", "arrival": "10:20", "price": 1300000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "13:00", "arrival": "14:20", "price": 780000, "class": "economy"},
    ],
    ("Hồ Chí Minh", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "08:00", "arrival": "09:00", "price": 1100000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "15:00", "arrival": "16:00", "price": 650000, "class": "economy"},
    ],
}

HOTELS_DB = {
    "Đà Nẵng": [
        {"name": "Mường Thanh Luxury", "stars": 5, "price_per_night": 1800000, "area": "Mỹ Khê", "rating": 4.5},
        {"name": "Sala Danang Beach", "stars": 4, "price_per_night": 1200000, "area": "Mỹ Khê", "rating": 4.3},
        {"name": "Fivitel Danang", "stars": 3, "price_per_night": 650000, "area": "Sơn Trà", "rating": 4.1},
        {"name": "Memory Hostel", "stars": 2, "price_per_night": 250000, "area": "Hải Châu", "rating": 4.6},
        {"name": "Christina's Homestay", "stars": 2, "price_per_night": 350000, "area": "An Thượng", "rating": 4.7},
    ],
    "Phú Quốc": [
        {"name": "Vinpearl Resort", "stars": 5, "price_per_night": 3500000, "area": "Bãi Dài", "rating": 4.4},
        {"name": "Sol by Meliá", "stars": 4, "price_per_night": 1500000, "area": "Bãi Trường", "rating": 4.2},
        {"name": "Lahana Resort", "stars": 3, "price_per_night": 800000, "area": "Dương Đông", "rating": 4.0},
        {"name": "9Station Hostel", "stars": 2, "price_per_night": 200000, "area": "Dương Đông", "rating": 4.5},
    ],
    "Hồ Chí Minh": [
        {"name": "Rex Hotel", "stars": 5, "price_per_night": 2800000, "area": "Quận 1", "rating": 4.3},
        {"name": "Liberty Central", "stars": 4, "price_per_night": 1400000, "area": "Quận 1", "rating": 4.1},
        {"name": "Cochin Zen Hotel", "stars": 3, "price_per_night": 550000, "area": "Quận 3", "rating": 4.4},
        {"name": "The Common Room", "stars": 2, "price_per_night": 180000, "area": "Quận 1", "rating": 4.6},
    ],
}


@tool
def search_flights(origin: str, destination: str) -> str:
    """
    Tìm kiếm các chuyến bay giữa hai thành phố.
    Tham số:
    - origin: thành phố khởi hành (VD: 'Hà Nội', 'Hồ Chí Minh')
    - destination: thành phố đến (VD: 'Đà Nẵng', 'Phú Quốc')
    Trả về danh sách chuyến bay với hãng, giờ bay, giá vé.
    """
    flights = FLIGHTS_DB.get((origin, destination))
    if not flights:
        # Thử tra ngược
        flights = FLIGHTS_DB.get((destination, origin))
        if not flights:
            return f"Không tìm thấy chuyến bay từ {origin} đến {destination}."

    result = f"Chuyến bay từ {origin} đến {destination}:\n"
    for f in flights:
        price_fmt = "{:,.0f}đ".format(f['price']).replace(",", ".")
        result += f"- {f['airline']} ({f['class']}): {f['departure']} -> {f['arrival']} | Giá: {price_fmt}\n"
    return result


@tool
def search_hotels(city: str, max_price_per_night: int = 999999999) -> str:
    """
    Tìm kiếm khách sạn tại một thành phố, có thể lọc theo giá tối đa mỗi đêm.
    Tham số:
    - city: tên thành phố (VD: 'Đà Nẵng', 'Phú Quốc', 'Hồ Chí Minh')
    - max_price_per_night: giá tối đa mỗi đêm (VNĐ)
    """
    hotels = HOTELS_DB.get(city, [])
    if not hotels:
        return f"Không tìm thấy khách sạn tại {city}."

    filtered_hotels = [h for h in hotels if h['price_per_night'] <= max_price_per_night]
    if not filtered_hotels:
        return f"Không tìm thấy khách sạn tại {city} với giá dưới {max_price_per_night:,.0f}đ/đêm. Hãy thử tăng ngân sách.".replace(",", ".")

    # Sắp xếp theo rating giảm dần
    sorted_hotels = sorted(filtered_hotels, key=lambda x: x['rating'], reverse=True)

    result = f"Khách sạn tại {city} (trong tầm giá {max_price_per_night:,.0f}đ): \n".replace(",", ".")
    for h in sorted_hotels:
        price_fmt = "{:,.0f}đ".format(h['price_per_night']).replace(",", ".")
        result += f"- {h['name']} ({h['stars']}*): {h['area']} | Rating: {h['rating']} | Giá: {price_fmt}/đêm\n"
    return result


@tool
def calculate_budget(total_budget: int, expenses: str) -> str:
    """
    Tính toán ngân sách còn lại sau khi trừ các khoản chi phí.
    Tham số:
    - total_budget: tổng ngân sách ban đầu (VNĐ)
    - expenses: chuỗi định dạng 'tên_khoản:số_tiền' cách nhau bởi dấu phẩy (VD: 'vé_máy_bay:890000,khách_sạn:650000')
    """
    try:
        expense_list = expenses.split(",")
        parsed_expenses = {}
        total_expense = 0
        
        detail_lines = []
        for item in expense_list:
            if ":" not in item:
                continue
            name, price = item.split(":")
            price_val = int(price.strip())
            parsed_expenses[name.strip()] = price_val
            total_expense += price_val
            detail_lines.append(f"- {name.strip()}: {'{:,.0f}đ'.format(price_val).replace(',', '.')}")
        
        remaining = total_budget - total_expense
        
        result = "Bảng chi phí:\n"
        result += "\n".join(detail_lines) + "\n"
        result += "---\n"
        result += f"Tổng chi: {'{:,.0f}đ'.format(total_expense).replace(',', '.')}\n"
        result += f"Ngân sách: {'{:,.0f}đ'.format(total_budget).replace(',', '.')}\n"
        result += f"Còn lại: {'{:,.0f}đ'.format(remaining).replace(',', '.')}\n"
        
        if remaining < 0:
            result += f"CẢNH BÁO: Vượt ngân sách {'{:,.0f}đ'.format(abs(remaining)).replace(',', '.')}! Cần điều chỉnh."
            
        return result
    except Exception as e:
        return f"Lỗi định dạng expenses: {str(e)}. Hãy sử dụng định dạng 'tên_khoản:số_tiền,tên_khoản2:số_tiền2'."
