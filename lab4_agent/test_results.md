# BÁO CÁO KẾT QUẢ TEST - LAB 4

## Test 1: Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.
### Diễn giải:
#### Các bước xử lý:
#### Phản hồi cuối cùng:
> Chào bạn! Rất vui được đồng hành cùng bạn trong chuyến đi sắp tới. Để mình gợi ý điểm đến và lên phương án chi tiêu hợp lý nhất, bạn cho mình biết thêm vài thông tin nhỏ nhé:

- 🛫 Bạn sẽ xuất phát từ thành phố nào?
- 🏖 Bạn thích phong cách du lịch nào: nghỉ dưỡng biển, leo núi/trekking, khám phá phố cổ/ẩm thực, hay chill tại homestay giữa thiên nhiên?
- 💰 Ngân sách dự kiến cho chuyến đi khoảng bao nhiêu? (Có thể ghi rõ cho 1 người hay cả nhóm)
- 📅 Bạn định đi mấy ngày?

Ví dụ: Bay từ Hà Nội/HCM đến Đà Nẵng – Hội An rất tiện cho kỳ nghỉ 3-4 ngày, hay Phú Quốc/Đà Lạt nếu bạn muốn không khí mát mẻ + check-in sống ảo. Cứ chia sẻ thoải mái, mình sẽ tìm chuyến bay & khách sạn tối ưu chi phí, đồng thời báo bạn rõ số tiền còn lại để ăn chơi nhé! ✈️🌴

---

## Test 2: Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng
### Diễn giải:
#### Các bước xử lý:
- Gọi tool: `search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})`
- Kết quả tool `search_flights`: Chuyến bay từ Hà Nội đến Đà Nẵng:
- Vietnam Airlines (economy): 06:00 -> 07:20 | Giá: 1.450.000đ
- Vietnam Airlines (business): 14:00 -> 15:20 | Giá: 2.800.000đ
- VietJet Air (economy): 08:30 -> 09:50...
#### Phản hồi cuối cùng:
> Chào bạn! Dưới đây là các chuyến bay hiện có từ Hà Nội đi Đà Nẵng để bạn tham khảo nhé:

**Chuyến bay:**
- VietJet Air (Economy): 08:30 → 09:50 | Giá: 890.000đ 💡 *Giá tốt nhất*
- Bamboo Airways (Economy): 11:00 → 12:20 | Giá: 1.200.000đ
- Vietnam Airlines (Economy): 06:00 → 07:20 | Giá: 1.450.000đ
- Vietnam Airlines (Business): 14:00 → 15:20 | Giá: 2.800.000đ

**Khách sạn:** Mình chưa gợi ý vội vì còn tuỳ vào số đêm bạn lưu trú và khu vực bạn muốn ở (sát biển Mỹ Khê, trung tâm thành phố, hay gần sân bay). Bạn thích phong cách nghỉ dưỡng hay tiện đi lại ăn chơi nhỉ?

**Tổng chi phí ước tính:** Bạn vui lòng cho mình biết **tổng ngân sách dự kiến** cho chuyến đi này là bao nhiêu nhé? Mình sẽ cộng vé máy bay, khách sạn, và các khoản phát sinh để tính ra số tiền còn lại, giúp bạn chi tiêu thoải mái mà không lo "cháy túi".

**Gợi ý thêm:** 
- Đà Nẵng sáng sớm thường mát và ít mưa, nên nếu chọn chuyến bay 6h hoặc 8h30, bạn sẽ có hẳn 1 ngày dài để khám phá Cầu Vàng, biển Mỹ Khê hoặc ăn bún mắm, mì Quảng ngay khi đáp xuống.
- Nếu đi nhóm hoặc gia đình, đặt vé trước 3-4 tuần thường săn được giá tốt hơn khoảng 10-15% đó.

Bạn dự định đi mấy ngày và ngân sách khoảng bao nhiêu? Mình sẽ lên phương án khách sạn + tính toán chi phí chi tiết cho bạn ngay! 🌴✈️

---

## Test 3: Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!
### Diễn giải:
#### Các bước xử lý:
- Gọi tool: `search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})`
- Kết quả tool `search_flights`: Chuyến bay từ Hà Nội đến Phú Quốc:
- Vietnam Airlines (economy): 07:00 -> 09:15 | Giá: 2.100.000đ
- VietJet Air (economy): 10:00 -> 12:15 | Giá: 1.350.000đ
- VietJet Air (economy): 16:00 -> 18:15 | Gi...
- Gọi tool: `search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 1500000})`
- Kết quả tool `search_hotels`: Khách sạn tại Phú Quốc (trong tầm giá 1.500.000đ): 
- 9Station Hostel (2*): Dương Đông | Rating: 4.5 | Giá: 200.000đ/đêm
- Sol by Meliá (4*): Bãi Trường | Rating: 4.2 | Giá: 1.500.000đ/đêm
- Lahana Re...
- Gọi tool: `calculate_budget({'expenses': 'vé_máy_bay:2200000,khách_sạn:1600000', 'total_budget': 5000000})`
- Kết quả tool `calculate_budget`: Bảng chi phí:
- vé_máy_bay: 2.200.000đ
- khách_sạn: 1.600.000đ
---
Tổng chi: 3.800.000đ
Ngân sách: 5.000.000đ
Còn lại: 1.200.000đ
...
#### Phản hồi cuối cùng:
> Chào bạn! Phú Quốc 2 đêm với budget 5 triệu là hoàn toàn khả thi và vẫn đủ dư dả để ăn uống, vui chơi nè. Mình đã tìm giúp bạn các lựa chọn tối ưu nhất đây:

**Chuyến bay (khứ hồi):**
- VietJet Air: 16:00 -> 18:15 | Giá: 1.100.000đ/chiều (~2.200.000đ khứ hồi)

**Khách sạn (2 đêm):**
- Lahana Resort (3*): Dương Đông | Rating: 4.0 | Giá: 800.000đ/đêm → 1.600.000đ/2 đêm
*(Hoặc nếu muốn cực tiết kiệm: 9Station Hostel 2* chỉ 200k/đêm → 400k/2 đêm, còn dư tiền ăn hải sản thoải mái luôn!)*

**Tổng chi phí ước tính:**
| Khoản chi | Số tiền |
|-----------|---------|
| Vé máy bay (khứ hồi) | 2.200.000đ |
| Khách sạn (2 đêm) | 1.600.000đ |
| **Tổng** | **3.800.000đ** |
| **Còn lại** | **1.200.000đ** |

**Gợi ý thêm:** 
- Với 1.2 triệu còn lại, bạn có thể thuê xe máy (~150k/ngày), ăn bún quậy, ghẹ, hàu ở Dương Đông, và đi tour 3 đảo (Hòn Mây Rút, Hòn Dăm, Hòn Một) khoảng 300-400k/người.
- Nếu chọn hostel thay vì khách sạn 3 sao, bạn sẽ dư khoảng 2.4 triệu — tha hồ nâng cấp bữa ăn hoặc trải nghiệm lặn ngắm san hô!
- Thời tiết Phú Quốc mùa này khá đẹp, nhớ mang kem chống nắng và áo mỏng đề phòng gió biển buổi tối nhé.

Bạn muốn mình chốt phương án nào, hay cần mình tìm thêm lựa chọn khác? 😊

---

## Test 4: Tôi muốn đặt khách sạn
#### Các bước xử lý:
-(Trao đổi trực tiếp để lấy thêm thông tin khách hàng)
#### Phản hồi cuối cùng:
> Chào bạn! Mình sẵn sàng giúp bạn tìm khách sạn ưng ý rồi 🌴 Để mình gợi ý được chỗ ở vừa ý và phù hợp với túi tiền, bạn cho mình biết thêm 2 thông tin này nha:
> - Bạn định du lịch thành phố nào? (VD: Đà Nẵng, Phú Quốc, Hà Nội, TP.HCM...)
> - Bạn có mức ngân sách tối đa cho mỗi đêm khoảng bao nhiêu không? (Nếu chưa xác định rõ, mình cứ tìm các mức giá phổ biến để bạn dễ so sánh nha)
> 
> Cứ nhắn mình, mình sẽ lọc ngay những khách sạn có rating tốt nhất trong tầm giá cho bạn! 😊

---

## Test 5: Giải giúp tôi bài tập lập trình Python về linked list
#### Các bước xử lý:
-(Từ chối do vi phạm Guardrail về phạm vi dịch vụ)
#### Phản hồi cuối cùng:
> Chào bạn, khoản này thì mình chịu thua rồi 🙈. Mình là trợ lý ảo của **TravelBuddy**, chuyên hỗ trợ tìm chuyến bay, đặt khách sạn và tư vấn lịch trình du lịch Việt Nam chứ không rành về lập trình Python lắm.
> 
> Nhưng nếu bạn đang cần "xả hơi" khỏi mớ code rắc rối để lên kế hoạch đi đâu đó cho thư giãn (ví dụ như một trip lên Đà Lạt ngắm sương mờ hay ra Phú Quốc tắm biển), thì nhắn mình ngay nhé! Mình hứa sẽ "cân" hết mọi yêu cầu du lịch cho bạn 😉

---

