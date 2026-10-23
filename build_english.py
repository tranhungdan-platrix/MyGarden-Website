import os
import re

# Read Vietnamese index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

en_content = content

# Replace asset paths for /en/ subdirectory
en_content = re.sub(r'href="styles/', 'href="../styles/', en_content)
en_content = re.sub(r'href="\./styles/', 'href="../styles/', en_content)
en_content = re.sub(r'href="plugins/', 'href="../plugins/', en_content)
en_content = re.sub(r'src="plugins/', 'src="../plugins/', en_content)
en_content = re.sub(r'src="js/', 'src="../js/', en_content)
en_content = re.sub(r'src="\./js/', 'src="../js/', en_content)
en_content = re.sub(r'src="images/', 'src="../images/', en_content)
en_content = re.sub(r'src="\./images/', 'src="../images/', en_content)
en_content = re.sub(r'url\(images/', 'url(../images/', en_content)
en_content = re.sub(r'href="images/', 'href="../images/', en_content)
en_content = re.sub(r'data-image-src="images/', 'data-image-src="../images/', en_content)

# Language switcher in en/index.html
en_content = re.sub(
    r'<a href="index\.html" class="active">🇻🇳 VN</a>\s*<span class="lang-sep">\|</span>\s*<a href="en/index\.html">🇬🇧 EN</a>',
    '<a href="../index.html">🇻🇳 VN</a> <span class="lang-sep">|</span> <a href="index.html" class="active">🇬🇧 EN</a>',
    en_content
)

# Nav links
en_content = en_content.replace('Câu Chuyện MyGarden Villa', 'The MyGarden Story')
en_content = en_content.replace('Về Các Villa', 'Our Villas')
en_content = en_content.replace('Địa Điểm Vui Chơi', 'Attractions & Experiences')
en_content = en_content.replace('Đánh Giá', 'Guest Reviews')
en_content = en_content.replace('Liên hệ', 'Contact Us')
en_content = en_content.replace('Đặt online', 'Book Online')

# Home slider descriptions
en_content = en_content.replace('Không gian rộng rãi thoáng mát', 'Spacious, refreshing, and serene natural sanctuaries')
en_content = en_content.replace('Nội thất hiện đại, đầy đủ tiện nghi', 'Modern interiors thoughtfully appointed with premium comforts')
en_content = en_content.replace('Nơi nghỉ dưỡng yên bình giữa khu vườn xinh xắn', 'Peaceful retreat nestled amidst blooming private gardens')
en_content = en_content.replace('Mang thiên nhiên đến gần hơn với quý khách', 'Bringing pristine nature closer to you and your loved ones')

# Story section
vn_p1 = 'MyGarden Villa ra đời sau đợt dịch Covid lịch sử năm 2021, khi mà lần đầu tiên người dân Sài Gòn chứng kiến cảnh phong toả tù túng và ngột ngạt của Sài Gòn. Khi đó, những thứ tưởng như đơn giản như những bó rau, hoa quả hay hít thở khí trời trong lành lại trở nên vô cùng xa xỉ. 45 ngày đêm phong toả nghiêm ngặt của Sài Gòn năm 2021 đã thúc đẩy sự ra đời của MyGarden Villa, với cột mốc đầu tiên là MyGarden Villa Bình Châu Hotspring.'
en_p1 = 'MyGarden Villa was born in the wake of the historic 2021 Covid-19 pandemic, when residents of Saigon first experienced the stifling confinement and isolation of citywide lockdown. At that time, everyday blessings once taken for granted—fresh produce, homegrown fruits, and breathing pure, unpolluted air—suddenly became priceless luxuries. Those 45 days of strict lockdown in 2021 sparked the founding vision of MyGarden Villa, marked by our very first sanctuary: MyGarden Villa Binh Chau Hotspring.'

vn_p2 = 'Với ý tưởng ban đầu là tạo nên một chốn bình yên, gần gũi thiên nhiên để thoát khỏi bầu không khí ngột ngạt và đầy áp lực của thành thị, MyGarden Villa được thiết kế hết sức đơn giản nhưng không kém phần tiện nghi, mang phong cách hiện đại nhưng được bao bọc giữa vườn cây xanh mát đậm nét thôn quê. MyGarden Villa được gửi gắm ước mơ về một ngôi nhà vườn bình yên giữa thiên nhiên trong lành, nơi mọi người có thể tận tay hái rau quả tươi sạch trong vườn hoặc đơn giản là nhâm nhi ly cà phê ngắm nhìn mặt trời mọc qua các tán lá rì rào trong gió.'
en_p2 = 'Guided by the aspiration to build a haven of peace immersed in nature away from the suffocating pressure of city life, MyGarden Villa was designed with elegant simplicity and modern convenience, sheltered within verdant countryside gardens. MyGarden Villa embodies our dream of a peaceful garden homestead in clean, crisp nature—where guests can harvest fresh organic vegetables with their own hands, or simply savor a morning cup of coffee watching the sun rise through gentle leaves whispering in the breeze.'

vn_p3 = '''Sau khi MyGarden Villa đầu tiên được đưa vào sử dụng đầu năm 2022 gần khu suối nước nóng - rừng quốc gia Bình Châu, MyGarden Villa Bảo Lộc Lakeview (MyGarden Nam Phuong Lakeview) cũng được hoàn thành vào tháng 08/2022 tại phố núi Bảo Lộc. Tháng 4/2024, MyGarden Villa Phan Thiết Beachfront chính thức được đưa vào sử dụng tại thành phố biển Phan Thiết, hoàn tất chuỗi nhà vườn “Rừng-Núi-Biển” của MyGarden Villa. 
\t\t\t\tChuỗi MyGarden Villa là nơi gia đình và bạn bè của gia chủ tìm về để sum vầy và nghỉ dưỡng sau những ngày làm việc mỏi mệt. Tại MyGarden Villa, mọi người có thể biến ước mơ thành hiện thực: thưởng trà ngắm cá giữa vườn cây rậm bóng mát ở Bình Châu Hotspring; tận hưởng làn sương mù mát lạnh vào sáng tinh mơ ở Bảo Lộc Lakeview; hay ngắm bình minh ló dạng trên biển tại Phan Thiết Beachfront. MyGarden Villa là ngôi nhà vườn mơ ước của chúng tôi, và giờ đây cũng là của bạn.'''
en_p3 = '''Following the opening of our first villa in early 2022 near the hot springs and national forest of Binh Chau, MyGarden Villa Bao Loc Lakeview (MyGarden Nam Phuong Lakeview) was completed in August 2022 in the mountain town of Bao Loc. In April 2024, MyGarden Villa Phan Thiet Beachfront officially opened in the coastal city of Phan Thiet, completing the signature “Forest - Mountain - Sea” sanctuary collection of MyGarden Villa.
\t\t\t\tThe MyGarden Villa collection is where family and friends gather to reconnect and rejuvenate after demanding workweeks. At MyGarden Villa, cherished dreams come alive: sip tea watching koi fish swim beneath shady canopies at Binh Chau Hotspring; embrace the crisp morning mist at Bao Loc Lakeview; or marvel at dawn breaking across the ocean at Phan Thiet Beachfront. MyGarden Villa was our dream sanctuary—and now, it is warmly yours.'''

vn_p4 = 'Và trong tháng 6 năm 2025, chúng tôi hân hạnh giới thiệu thành viên mới nhất trong gia đình MyGarden Villa: Sea Sand Garden Villa. Sea Sand Garden Villa tiếp nối tinh thần của MyGarden Villa là mang trải nghiệm an yên đến với mọi người. Cùng với các villa khác của MyGarden Villa, đây cũng sẽ là là địa điểm tuyệt với cho những quý khách tìm kiếm sự thư giãn và kết nối sâu sắc với thiên nhiên.'
en_p4 = 'In June 2025, we proudly introduced the newest member of the MyGarden Villa family: Sea Sand Garden Villa. Carrying forward our founding ethos of sharing tranquility with all, Sea Sand Garden Villa, alongside our other villas, offers an idyllic setting for travelers seeking relaxation and a profound connection with nature.'

en_content = en_content.replace(vn_p1, en_p1)
en_content = en_content.replace(vn_p2, en_p2)
en_content = en_content.replace(vn_p3, en_p3)
en_content = en_content.replace(vn_p4, en_p4)

# Amenity translations
amenities_map = {
    '5 Phòng ngủ': '5 Bedrooms',
    '3 Phòng ngủ': '3 Bedrooms',
    '6 Phòng ngủ': '6 Bedrooms',
    '7 Phòng ngủ': '7 Bedrooms',
    'Lưu trú qua đêm': 'Overnight Stay',
    'Lễ tân đón tiếp': 'Host Reception & Greeting',
    'Cho phép mang theo thú cưng': 'Pet-Friendly',
    'Bếp riêng': 'Private Kitchen',
    'Phòng tắm riêng': 'Private En-suite Bathroom',
    'Nhìn ra hồ': 'Lake View',
    'Ban công': 'Private Balcony',
    'Nhìn ra vườn': 'Garden View',
    'Sân trong': 'Private Courtyard',
    'Tivi màn hình phẳng': 'Flat-Screen TV',
    'Tiện nghi BBQ': 'BBQ Facilities',
    'Sân hiên': 'Outdoor Terrace',
    'Wifi miễn phí': 'Free High-Speed Wi-Fi',
    'Gần sát suối nước nóng': 'Steps from Hot Springs',
    'Điều hòa không khí': 'Air Conditioning',
    'Lối ra bãi biển - Hướng biển': 'Direct Beach Access - Ocean View',
    'Bể bơi': 'Private Swimming Pool',
    'Bàn bi-da': 'Billiards / Pool Table',
    'Đặt Ngay': 'Book Now',
    'Xem Chi Tiết': 'View Details'
}

for vn, en in amenities_map.items():
    en_content = en_content.replace(vn, en)

# Detail links in en/index.html
en_content = en_content.replace('href="/baoloc.html"', 'href="baoloc.html"')
en_content = en_content.replace('href="/binhchau.html"', 'href="binhchau.html"')
en_content = en_content.replace('href="/seasand.html"', 'href="seasand.html"')
en_content = en_content.replace('href="/phanthiet.html"', 'href="phanthiet.html"')

# Attractions Section
en_content = en_content.replace('<h2>CÁC ĐỊA ĐIỂM VUI CHƠI</h2>', '<h2>ATTRACTIONS & LOCAL EXPERIENCES</h2>')
en_content = en_content.replace('Tham Quan Vui Chơi Giải Trí', 'Sightseeing & Attractions')
en_content = en_content.replace('Địa Điểm Ăn Uống', 'Dining & Local Cuisine')

# Attractions items Binh Chau
en_content = en_content.replace('Khu Du Lịch Suối Nước Nóng Minera Bình Châu', 'Minera Binh Chau Hot Springs Resort')
en_content = en_content.replace('Biển Sông Lô Suối Ồ Và Khu Du Lịch Hodota', 'Song Lo Suoi O Beach & Hodota Resort')
en_content = en_content.replace('Vườn Nhãn Suối Bang', 'Suoi Bang Longan Orchards')
en_content = en_content.replace('Công Viên Nước Tropicana-Novaworld Hồ Tràm', 'Tropicana Water Park - Novaworld Ho Tram')
en_content = en_content.replace('Khu Bảo Tồn Thiên Nhiên Bình Châu-Phước Bửu', 'Binh Chau - Phuoc Buu Nature Reserve')
en_content = en_content.replace('Biển Seava Hồ Tràm', 'Seava Ho Tram Beach')
en_content = en_content.replace('Hampton Pier (Cầu Ngắm Biển, Tắm Biển)', 'Hamptons Pier (Ocean Boardwalk & Beach)')
en_content = en_content.replace('Nhà Hàng Hội Ngộ', 'Hoi Ngo Restaurant')
en_content = en_content.replace('Nhà Hàng Cơm Niêu Thùy Trang', 'Thuy Trang Claypot Rice Restaurant')
en_content = en_content.replace('Nhà Hàng Hai Lộc II', 'Hai Loc II Seafood Restaurant')
en_content = en_content.replace('Chợ Bình Châu', 'Binh Chau Local Market')

# Attractions items Bao Loc
en_content = en_content.replace('Vườn Dâu Berry Bistro', 'Berry Bistro Strawberry Farm')
en_content = en_content.replace('Săn Mây Núi Đại Bình (Bình Minh Luxury)', 'Dai Binh Mountain Cloud Hunting (Binh Minh Luxury)')
en_content = en_content.replace('Tu Viện Bát Nhã', 'Bat Nha Monastery')
en_content = en_content.replace('Thác Dambri', 'Dambri Waterfall')
en_content = en_content.replace('Chùa Di Đà - Thác Tam Hợp', 'Di Da Pagoda & Tam Hop Waterfall')
en_content = en_content.replace('Linh Quy Pháp Ấn', 'Linh Quy Phap An Temple')
en_content = en_content.replace('Phở Khô Hào Ký', 'Hao Ky Dry Pho')
en_content = en_content.replace('Bún Bò Nhà Thờ', 'Church Beef Noodle Soup')
en_content = en_content.replace('Đậu Nành Nóng Nhà Thờ Bảo Lộc', 'Bao Loc Church Hot Soy Milk')
en_content = en_content.replace('Chè Thảo Uyên', 'Thao Uyen Sweet Soup')
en_content = en_content.replace('Nhà Hàng Bách Hỷ An', 'Bach Hy An Restaurant')
en_content = en_content.replace('Nhà Của Gạo', 'Nha Cua Gao Cafe')
en_content = en_content.replace('Cá Tầm Vũ Trụ', 'Vu Tru Sturgeon Specialty')

# Attractions items Phan Thiet
en_content = en_content.replace('Novadreams Adventure World', 'Novadreams Adventure World')
en_content = en_content.replace('Wonderland Water Park', 'Wonderland Water Park')
en_content = en_content.replace('Bikini Beach', 'Bikini Beach')
en_content = en_content.replace('Nhà Hàng Hải Sản Xuân Hưng', 'Xuan Hung Seafood Restaurant')
en_content = en_content.replace('Reo Beach Café', 'Reo Beach Café')
en_content = en_content.replace('Café Đồi Sim', 'Doi Sim Café')
en_content = en_content.replace('Aloha Beach Club', 'Aloha Beach Club')
en_content = en_content.replace('Cơm Niêu Cậu Khâu', 'Cau Khau Claypot Rice')
en_content = en_content.replace('Chavi Beach Coffee', 'Chavi Beach Coffee')
en_content = en_content.replace('Nhà Hàng Ốc Benz 2', 'Oc Benz 2 Seafood Restaurant')
en_content = en_content.replace('Bánh flan Mộng Cầm', 'Mong Cam Creme Caramel Flan')
en_content = en_content.replace('Bánh Căn Lân Nguyệt', 'Lan Nguyet Banh Can')
en_content = en_content.replace('Bánh canh Chả cá Gái', 'Gai Fish Cake Noodle Soup')
en_content = en_content.replace('Hyme Kaffe’', 'Hyme Kaffe’')
en_content = en_content.replace('Chả cuốn cá trích Dung', 'Dung Herring Spring Rolls')
en_content = en_content.replace('Nem Nướng Minh Hiếu', 'Minh Hieu Grilled Pork Sausage')
en_content = en_content.replace('Nhà hàng Good Morning Vietnam', 'Good Morning Vietnam Italian Restaurant')

# Testimonials
en_content = en_content.replace('<h2>ĐÁNH GIÁ CỦA KHÁCH HÀNG VỀ MYGARDEN VILLA</h2>', '<h2>WHAT GUESTS SAY ABOUT MYGARDEN VILLA</h2>')

rev1_vn = '5 sao cho sự sạch sẽ, yên tĩnh và view hồ rất đẹp. Homestay kiểu cấu trúc mở thân thiện môi trường, sân vườn rộng có khu BBQ tiện lợi. Phòng bếp đầy đủ tiện nghi, phòng ngủ thoáng mát mình quất liền 4 tiếng ngủ trưa ;)) Vị trí gần khu trung tâm ko mất thời gian di chuyển.'
rev1_en = '5 stars for cleanliness, peaceful tranquility, and stunning lake views! The eco-friendly open architecture, generous garden, and convenient BBQ area made our trip unforgettable. The kitchen is fully equipped, and the breezy bedroom gave me the deepest 4-hour nap ever ;)) Great location close to the town center.'

rev2_vn = 'Đã ở đây vào dịp Tết Tây, không gian rộng rãi, vườn rau sạch, gần chợ và trung tâm. Đặc biệt, có thể chèo thuyền trên hồ Nam Phương là 1 trải nghiệm tuyệt vời!'
rev2_en = 'Stayed here over the New Year holiday. Vast space, fresh organic vegetable garden, close to the local market and town center. Kayaking on Nam Phuong Lake was a truly wonderful and memorable experience!'

rev3_vn = 'Nhà đẹp, thoáng mát, sạch sẽ, trang bị đầy đủ. 3 phòng đều có ban công khá riêng tư. Chỉ cách suối nước nóng khoảng 2km. Ở đây có thể ra chợ Bình Châu mua hải sản về tự nấu ăn rất ngon.'
rev3_en = 'Beautiful, airy, sparkling clean home with complete amenities. All 3 bedrooms have private balconies offering great privacy. Only 2km from the hot springs. We easily bought fresh seafood at Binh Chau market to cook delicious meals together.'

rev4_vn = 'Không gian cây xanh rất thoáng mát, có cả hồ cá koi cf thư giản🥰🥰'
rev4_en = 'The lush green garden is wonderfully breezy and refreshing, with a charming koi fish pond perfect for relaxing with morning coffee 🥰🥰'

rev5_vn = 'Gia đình mình đi 12 người và 5 trẻ em ở rất thoải mái và đầy đủ tiện nghi. Villa sạch, đẹp, phòng ngủ view biển vả hồ bơi ko có gì để chê luôn.'
rev5_en = 'Our family group of 12 adults and 5 children had more than enough comfortable space with top-notch amenities. The villa is pristine, stylish, and the ocean-facing bedrooms and swimming pool are beyond compare!'

rev6_vn = 'Phòng đẹp chủ nhà thân thiện không gian thoải mái lí tưởng cho gia đình ,view hướng biển . Hướng phòng ngủ ngay biển sáng tối thì thấy trăng .chủ nhà hỗ trợ nhiệt tình siu dễ thương. 10000 điểm'
rev6_en = 'Gorgeous rooms, exceptionally friendly hosts, and an ideal setting for families with direct ocean views. The master bedroom faces straight to the sea—morning sun and moonlit waves at night. Super helpful and caring hosts. 10/10!'

en_content = en_content.replace(rev1_vn, rev1_en)
en_content = en_content.replace(rev2_vn, rev2_en)
en_content = en_content.replace(rev3_vn, rev3_en)
en_content = en_content.replace(rev4_vn, rev4_en)
en_content = en_content.replace(rev5_vn, rev5_en)
en_content = en_content.replace(rev6_vn, rev6_en)

# Footer
en_content = en_content.replace('LIÊN HỆ VỚI MYGARDEN VILLA', 'CONNECT WITH MYGARDEN VILLA')
en_content = en_content.replace('CÁC CƠ SỞ LƯU TRÚ CỦA MYGARDEN VILLA', 'MYGARDEN VILLA LOCATIONS')
en_content = en_content.replace('102/8 Lý Thái Tổ, Đam Bri, Bảo Lộc, Lâm Đồng', '102/8 Ly Thai To, Dam Bri, Bao Loc, Lam Dong')
en_content = en_content.replace('QL55, Bình Châu, Xuyên Mộc, Bà Rịa - Vũng Tàu', 'Highway 55, Binh Chau, Xuyen Moc, Ba Ria - Vung Tau')
en_content = en_content.replace('463 Lạc Long Quân, Tiến Thành, Thành phố Phan Thiết, Bình Thuận', '463 Lac Long Quan, Tien Thanh, Phan Thiet City, Binh Thuan')
en_content = en_content.replace('407 Lạc Long Quân, Tiến Thành, Thành phố Phan Thiết, Bình Thuận', '407 Lac Long Quan, Tien Thanh, Phan Thiet City, Binh Thuan')

with open('en/index.html', 'w', encoding='utf-8') as f:
    f.write(en_content)

print('en/index.html generated!')


# Helper function to generate detail pages
def translate_detail_page(filename, title_en, why_us_text_en, garden_text_en):
    with open(filename, 'r', encoding='utf-8') as f:
        c = f.read()

    # Paths
    c = re.sub(r'href="styles/', 'href="../styles/', c)
    c = re.sub(r'href="\./styles/', 'href="../styles/', c)
    c = re.sub(r'href="plugins/', 'href="../plugins/', c)
    c = re.sub(r'src="plugins/', 'src="../plugins/', c)
    c = re.sub(r'src="js/', 'src="../js/', c)
    c = re.sub(r'src="\./js/', 'src="../js/', c)
    c = re.sub(r'src="images/', 'src="../images/', c)
    c = re.sub(r'src="\./images/', 'src="../images/', c)
    c = re.sub(r'url\(images/', 'url(../images/', c)
    c = re.sub(r'href="images/', 'href="../images/', c)

    # Logo link
    c = c.replace('href="index.html"', 'href="index.html"')

    # Lang switcher
    c = re.sub(
        r'<a href="' + filename + r'" class="active">🇻🇳 VN</a>\s*<span class="lang-sep">\|</span>\s*<a href="en/' + filename + r'">🇬🇧 EN</a>',
        '<a href="../' + filename + '">🇻🇳 VN</a> <span class="lang-sep">|</span> <a href="' + filename + '" class="active">🇬🇧 EN</a>',
        c
    )

    # Common UI
    c = c.replace('Trải nghiệm MyGarden Villa', 'Experience MyGarden Villa')
    c = c.replace('Đặt Ngay', 'Book Now')
    c = c.replace('<h1>Lý do nên chọn chúng tôi</h1>', '<h1>Why Choose Us</h1>')
    c = c.replace('<h2>HÌNH ẢNH CỦA KHÁCH HÀNG</h2>', '<h2>GUEST MEMORIES & PHOTOS</h2>')

    # Common services/amenities
    for vn, en in amenities_map.items():
        c = c.replace(vn, en)

    c = c.replace('Đỗ xe trong khuôn viên miễn phí', 'Free On-Site Private Parking')
    c = c.replace('Lò nướng', 'Outdoor BBQ Grill / Oven')
    c = c.replace('WiFi miễn phí', 'Free High-Speed Wi-Fi')

    # Specific text
    c = c.replace('<title>' + filename, '<title>' + title_en)
    if why_us_text_en:
        # replace paragraph
        c = re.sub(r'<div class="split_section_text">\s*<p>(.*?)</p>\s*</div>',
                   f'<div class="split_section_text"><p>{why_us_text_en}</p></div>',
                   c, count=1, flags=re.DOTALL)
    if garden_text_en:
        # replace second paragraph
        parts = c.split('<div class="split_section_left_content">')
        if len(parts) > 1:
            p2 = re.sub(r'<div class="split_section_text">\s*<p>(.*?)</p>\s*</div>',
                        f'<div class="split_section_text"><p>{garden_text_en}</p></div>',
                        parts[1], count=1, flags=re.DOTALL)
            c = parts[0] + '<div class="split_section_left_content">' + p2

    # Footer
    c = c.replace('LIÊN HỆ VỚI MYGARDEN VILLA', 'CONNECT WITH MYGARDEN VILLA')
    c = c.replace('CÁC CƠ SỞ LƯU TRÚ CỦA MYGARDEN VILLA', 'MYGARDEN VILLA LOCATIONS')
    c = c.replace('102/8 Lý Thái Tổ, Đam Bri, Bảo Lộc, Lâm Đồng', '102/8 Ly Thai To, Dam Bri, Bao Loc, Lam Dong')
    c = c.replace('QL55, Bình Châu, Xuyên Mộc, Bà Rịa - Vũng Tàu, Việt Nam', 'Highway 55, Binh Chau, Xuyen Moc, Ba Ria - Vung Tau')
    c = c.replace('463 Lạc Long Quân, Tiến Thành, Thành phố Phan Thiết, Bình Thuận', '463 Lac Long Quan, Tien Thanh, Phan Thiet City, Binh Thuan')
    c = c.replace('407 Lạc Long Quân, Tiến Thành, Thành phố Phan Thiết, Bình Thuận', '407 Lac Long Quan, Tien Thanh, Phan Thiet City, Binh Thuan')

    with open(os.path.join('en', filename), 'w', encoding='utf-8') as out:
        out.write(c)
    print(f'en/{filename} generated!')


# Bao Loc
translate_detail_page(
    'baoloc.html',
    'MyGarden Villa Bao Loc Lakeview',
    'MyGarden Villa Bao Loc Lakeview (MyGarden Nam Phuong Lakeview) sits directly on the banks of scenic Nam Phuong Lake, Bao Loc City, Lam Dong Province. Designed in harmony with nature, this sanctuary represents the "Mountain" jewel in MyGarden Villa’s signature "Forest-Mountain-Sea" collection. Surrounded year-round by fertile orchards and blooming flowers, the villa features comprehensive modern comforts—flat-screen TVs, refrigerator, fully equipped kitchen—paired with outdoor BBQ, open-air karaoke, fishing, and kayaking on the tranquil lake.',
    'This 5-bedroom villa is enveloped by lush fruit trees, organic vegetables, and seasonal blossoms. Depending on the time of year, guests can handpick fresh garden harvests including avocados, durians, mangosteens, star apples, guavas, plums, broccoli, and carrots. All flora is cultivated naturally and organically for the health of our family and our cherished guests.'
)

# Nam Phuong
translate_detail_page(
    'namphuong.html',
    'MyGarden Villa Nam Phuong Lakeview',
    'MyGarden Villa Nam Phuong Lakeview offers an intimate mountain lakeside haven in Bao Loc. Guests enjoy sweeping vistas over Nam Phuong Lake, cool morning mist, and complete self-catering luxury surrounded by verdant orchards.',
    'Surrounded by fresh air and fruit trees, guests can enjoy quiet walks, lakeside fishing, kayaking, and open-air barbecues under starry mountain skies.'
)

# Binh Chau
translate_detail_page(
    'binhchau.html',
    'MyGarden Villa Binh Chau Hotspring',
    'MyGarden Villa Binh Chau Hotspring is situated in Binh Chau, Xuyen Moc District, Ba Ria - Vung Tau, just 2km from the renowned Minera Hot Springs and Binh Chau - Phuoc Buu Nature Reserve. Serving as the "Forest" cornerstone of our collection, the villa offers a peaceful countryside retreat surrounded by fresh coastal woodland air, featuring modern amenities, outdoor BBQ, and a serene koi fish pond.',
    'The 3-bedroom villa provides generous private balconies overlooking flowering gardens and shady trees. Guests can easily visit Binh Chau market for fresh morning seafood, unwind in the natural hot springs, or explore the ancient coastal rainforest.'
)

# Phan Thiet
translate_detail_page(
    'phanthiet.html',
    'MyGarden Villa Phan Thiet Beachfront',
    'MyGarden Villa Phan Thiet Beachfront is situated directly along the coastline at 463 Lac Long Quan, Tien Thanh, Phan Thiet City. Representing the "Sea" jewel in our collection, this expansive 7-bedroom beachfront estate features direct beach access, a private swimming pool, billiards table, full kitchen, and panoramic ocean views from every corner.',
    'Ideal for large family gatherings and retreats, guests wake up to sunrise breaking over the sea, spend days lounging by the pool or enjoying beach sports, and gather for sunset barbecues as ocean breezes roll in.'
)

# Sea Sand
translate_detail_page(
    'seasand.html',
    'Sea Sand Garden Villa',
    'Sea Sand Garden Villa is located at 407 Lac Long Quan, Tien Thanh, Phan Thiet City, directly opposite the beach. This boutique 6-bedroom villa features a private swimming pool, billiards table, full kitchen, and an airy courtyard garden crafted for relaxation and seaside entertaining.',
    'With generous living quarters, en-suite bedrooms, and full luxury amenities, Sea Sand Garden Villa is the premier coastal destination for unforgettable family holidays and group vacations.'
)

print('All English pages generated successfully!')
