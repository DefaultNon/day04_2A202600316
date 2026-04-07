from tools import search_flights, search_hotels, calculate_budget

print("--- Testing search_flights ---")
# StructuredTool objects are called via .invoke()
print(search_flights.invoke({"origin": "Hà Nội", "destination": "Đà Nẵng"}))

print("\n--- Testing search_hotels ---")
print(search_hotels.invoke({"city": "Đà Nẵng", "max_price_per_night": 1000000}))

print("\n--- Testing calculate_budget ---")
print(calculate_budget.invoke({"total_budget": 5000000, "expenses": "vé_máy_bay:1450000,khách_sạn:800000"}))
