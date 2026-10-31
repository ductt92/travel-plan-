#!/usr/bin/env python3
"""Kịch bản bài giảng 顶石中文 – Bài 7.1 «闲置经济是真正的共享经济». Chạy để sinh ds71.json."""
import json
import os

TAG = "顶石中文 · Bài 7.1 · 闲置经济是真正的共享经济"
slides = []


def add(type_, chapter=None, section="", **kw):
    s = {"type": type_, "section": section, **kw}
    if chapter:
        s["chapter"] = chapter
    slides.append(s)


def F(i, t, **kw):
    return {"t": t, "f": i, **kw}


# ======================= MỞ ĐẦU =======================
add("title", chapter="Mở đầu",
    top="顶石中文 – Đỉnh cao tiếng Trung",
    zh="闲置经济是\n真正的共享经济", py="Xiánzhì jīngjì shì zhēnzhèng de gòngxiǎng jīngjì",
    vi="Bài 7.1: Kinh tế đồ cũ mới là kinh tế chia sẻ thực sự",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng giáo trình 顶石中文, Đỉnh cao tiếng Trung.",
         {"t": "Hôm nay chúng ta bước sang Đơn vị bảy, 经济篇, chủ đề Kinh tế, với bài bảy chấm một: 闲置经济是真正的共享经济。 Nghĩa là: Kinh tế đồ cũ, đồ để không, mới là kinh tế chia sẻ thực sự.",
          "cap": "Hôm nay chúng ta bước sang Đơn vị 7, 经济篇, chủ đề Kinh tế, với bài 7.1: 闲置经济是真正的共享经济。 Nghĩa là: Kinh tế đồ cũ, đồ để không, mới là kinh tế chia sẻ thực sự."},
         "Bài khóa là một bài báo của Tân Hoa Xã. Bài mở đầu bằng chiếc điện thoại cũ: ở Trung Quốc, hàng tỷ chiếc điện thoại cũ đang nằm im trong ngăn kéo, còn Nhật Bản thì chiết xuất vàng từ điện thoại cũ để làm huy chương Olympic. Từ đó, tác giả bàn về thị trường đồ cũ nghìn tỷ tệ, về lòng tin trong giao dịch, và về giá trị xã hội của việc biến lãng phí thành tiêu dùng.",
         "Ở Việt Nam, chắc các bạn cũng quen với chuyện pass đồ, thanh lý đồ cũ trên Chợ Tốt hay các hội nhóm Facebook. Trong lúc học, các bạn hãy so sánh xem người trẻ hai nước mua bán đồ cũ giống và khác nhau thế nào nhé."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài báo về kinh tế đồ cũ: quy mô thị trường, lòng tin, giá trị xã hội",
           "Nắm vững 48 từ mới, kèm âm Hán Việt và ví dụ (có nhiều từ lóng mạng: 吃土 · 回血 · 剁手)",
           "6 mẫu câu: 尚属 · 趋于 · 向来 · 严把……关 · 换言之 · 一连",
           "Kết hợp từ: 超乎 · 放眼 · 缔造 và 6 thành ngữ, quán ngữ",
           "Luyện tập theo sách; liên hệ: “pass đồ”, chợ đồ cũ ở Việt Nam"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu bài báo về kinh tế đồ cũ: thị trường này lớn đến mức nào, vì sao lòng tin là chìa khóa, và mua bán đồ cũ có giá trị gì cho xã hội."),
         F(1, "Thứ hai, nắm vững bốn mươi tám từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ. Bài này có khá nhiều từ lóng trên mạng, như 吃土，回血，剁手, rất thú vị."),
         F(2, "Thứ ba, học sáu mẫu câu trọng điểm: 尚属，趋于，向来，严把关，换言之, và 一连."),
         F(3, "Thứ tư, học các kết hợp từ 超乎，放眼，缔造, cùng sáu thành ngữ, quán ngữ như 何去何从，囊中羞涩，喜新厌旧."),
         F(4, "Thứ năm, làm bài luyện tập của sách, và liên hệ với chuyện pass đồ, chợ đồ cũ ở Việt Nam."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 课前思考", title="Câu hỏi trước bài học 课前思考", reveal=True, size=34,
    items=["(1) 你购买过二手物品吗？如果有，购买过哪类的二手物品呢？",
           "Đáp án gợi ý: 我买过二手物品，比如二手书、二手自行车，还在网上买过一部二手手机。",
           "(2) 你的闲置物品一般会怎么处理？",
           "Đáp án gợi ý: 我一般会把闲置物品放到网上转卖，或者送给朋友，旧衣服会捐给需要的人。",
           "(3) 你们国家有哪些受欢迎的闲置物品交易平台？",
           "Đáp án gợi ý: 在越南，Chợ Tốt很受欢迎，很多人也在脸书（Facebook）的二手群组里买卖闲置物品。"],
    say=["Chúng ta bắt đầu bằng ba câu hỏi trước bài học, 课前思考. Thầy đọc câu hỏi, các bạn tạm dừng để tự trả lời bằng tiếng Trung, rồi nghe câu trả lời gợi ý nhé.",
         F(0, "Câu một: 你购买过二手物品吗？如果有，购买过哪类的二手物品呢？ Bạn đã từng mua đồ cũ chưa? Nếu có, bạn đã mua loại đồ cũ nào? 二手 là đồ đã qua tay một người, tức là đồ cũ, hàng second-hand."),
         F(1, "Gợi ý: 我买过二手物品，比如二手书、二手自行车，还在网上买过一部二手手机。 Tôi từng mua đồ cũ, ví dụ sách cũ, xe đạp cũ, còn mua một chiếc điện thoại cũ trên mạng."),
         F(2, "Câu hai: 你的闲置物品一般会怎么处理？ Đồ để không của bạn thường được xử lý thế nào? 闲置物品 là đồ không dùng đến, từ khóa của cả bài."),
         F(3, "Gợi ý: 我一般会把闲置物品放到网上转卖，或者送给朋友，旧衣服会捐给需要的人。 Tôi thường đăng đồ không dùng lên mạng để bán lại, hoặc tặng bạn bè; quần áo cũ thì quyên góp cho người cần."),
         F(4, "Câu ba: 你们国家有哪些受欢迎的闲置物品交易平台？ Ở nước bạn có những nền tảng mua bán đồ cũ nào được ưa chuộng?"),
         F(5, "Gợi ý: 在越南，Chợ Tốt很受欢迎，很多人也在脸书的二手群组里买卖闲置物品。 Ở Việt Nam, Chợ Tốt rất được ưa chuộng, nhiều người cũng mua bán đồ cũ trong các hội nhóm đồ cũ trên Facebook. 脸书 là cách người Trung Quốc gọi Facebook.")])

add("bullets", section="Khởi động 课前思考", title="Khởi động: 共享经济 và 闲置经济", size=34,
    items=["## 共享经济 kinh tế chia sẻ: dùng chung tài sản, “dùng” thay vì “sở hữu”",
           "共享单车 xe đạp công cộng · 共享充电宝 sạc dự phòng cho thuê · 共享汽车 ô tô thuê theo giờ",
           "## 闲置经济 kinh tế đồ cũ: đưa đồ để không trở lại lưu thông",
           "二手 đồ cũ · 闲置物品 đồ không dùng đến · 转卖 bán lại (“pass”) · 回收 thu hồi, tái chế",
           "以旧换新 thu cũ đổi mới · 闲鱼 Xianyu, 转转 Zhuanzhuan: ứng dụng đồ cũ lớn nhất Trung Quốc",
           "## Câu hỏi của tên bài: vì sao 闲置经济 mới là “真正的”共享经济？"],
    say=["Trước khi học từ mới, chúng ta làm quen với hai khái niệm then chốt của bài: 共享经济 và 闲置经济.",
         F(0, "共享经济 là kinh tế chia sẻ: nhiều người dùng chung một tài sản, tức là chỉ cần được dùng chứ không cần sở hữu."),
         F(1, "Ở Trung Quốc, nổi tiếng nhất là 共享单车, xe đạp chia sẻ, quét mã là đi; 共享充电宝, sạc dự phòng cho thuê; và 共享汽车, ô tô thuê theo giờ. Khoảng năm hai nghìn không trăm mười bảy, xe đạp chia sẻ bùng nổ đến mức có những bãi xe bỏ hoang chất cao như núi."),
         F(2, "Còn 闲置经济 là kinh tế đồ cũ: đưa những món đồ để không trở lại lưu thông, đến tay người cần."),
         F(3, "Các từ hay gặp: 二手, đồ cũ; 闲置物品, đồ không dùng đến; 转卖, bán lại, giới trẻ Việt Nam gọi là pass đồ; 回收, thu hồi, tái chế."),
         F(4, "以旧换新 là thu cũ đổi mới, giống chương trình thu cũ đổi mới ở các chuỗi điện thoại Việt Nam. 闲鱼 và 转转 là hai ứng dụng mua bán đồ cũ lớn nhất Trung Quốc."),
         F(5, "Tên bài đặt ra một câu hỏi: vì sao kinh tế đồ cũ mới là kinh tế chia sẻ thực sự? Các bạn hãy giữ câu hỏi này trong đầu; đến đoạn chín của bài khóa, tác giả sẽ trả lời.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("闲置", "xiánzhì", "nhàn trí", "tính từ", "để không, bỏ không, không dùng đến", "我把闲置的自行车卖掉了。", "Tôi đã bán chiếc xe đạp để không của mình.",
     "Tính từ, cũng dùng như động từ, nghĩa là để sang một bên, không dùng tới. 闲 là nhàn, rảnh rỗi; 置 là đặt, để. 闲置物品 là đồ không dùng đến; 闲置经济 trong tên bài là nền kinh tế mua bán lại những món đồ ấy. Tiếng Việt hay nói đồ thanh lý, đồ pass lại."),
    ("零部件", "língbùjiàn", "linh bộ kiện", "danh từ", "linh kiện, phụ tùng", "这家工厂生产汽车零部件。", "Nhà máy này sản xuất linh kiện ô tô.",
     "Danh từ, là cách gọi chung của 零件, chi tiết nhỏ, và 部件, bộ phận lớn hơn. Âm Hán Việt linh kiện chính là 零件. Trong bài: 将旧手机零部件拆下, tháo linh kiện của điện thoại cũ ra."),
    ("装裱", "zhuāngbiǎo", "trang biểu", "động từ", "bồi tranh, lên khung (tranh, chữ)", "这幅画装裱好以后挂在客厅里。", "Bức tranh này lên khung xong sẽ treo ở phòng khách.",
     "Động từ, nghĩa gốc là bồi giấy vào mặt sau tranh, thư pháp để làm đẹp và bảo quản. Trong bài là tháo linh kiện điện thoại cũ ra, gắn vào khung thành một món đồ trang trí nghệ thuật. 裱好的iPhone 5 là chiếc iPhone 5 đã được đóng khung."),
    ("风尚", "fēngshàng", "phong thượng", "danh từ", "trào lưu, nếp sống thịnh hành", "节约用水已成为一种社会风尚。", "Tiết kiệm nước đã trở thành một nếp sống của xã hội.",
     "Danh từ, chỉ phong khí, thói quen thịnh hành trong xã hội ở một thời kỳ, thường mang nghĩa tốt. Gần nghĩa với 风气 và 时尚. Trong bài: 成为许多年轻人的风尚, trở thành trào lưu của nhiều người trẻ."),
    ("抽屉", "chōuti", "trừu thế", "danh từ", "ngăn kéo", "钥匙放在桌子的抽屉里。", "Chìa khóa để trong ngăn kéo bàn.",
     "Danh từ, nghĩa là ngăn kéo của bàn, tủ. 抽 là kéo ra, rút ra. Chữ thứ hai đọc thanh nhẹ. Trong bài: 大量的旧手机闲置在人们的抽屉里, rất nhiều điện thoại cũ nằm im trong ngăn kéo."),
    ("放眼", "fàngyǎn", "phóng nhãn", "động từ", "phóng tầm mắt, nhìn ra (rộng, xa)", "放眼望去，到处都是绿色的田野。", "Phóng tầm mắt nhìn ra, đâu đâu cũng là cánh đồng xanh.",
     "Động từ, nghĩa là mở rộng tầm mắt mà nhìn, giống phóng tầm mắt trong tiếng Việt. Nghĩa bóng là nhìn rộng, nhìn xa: 放眼世界，放眼未来. Đây là một kết hợp từ trọng điểm của bài."),
    ("邻国", "línguó", "lân quốc", "danh từ", "nước láng giềng, nước lân cận", "越南和中国是邻国。", "Việt Nam và Trung Quốc là hai nước láng giềng.",
     "Danh từ, nghĩa là nước có lãnh thổ kề bên. 邻 là lân, như trong lân cận. Trong bài: 放眼邻国日本, nhìn sang nước láng giềng Nhật Bản. Trung Quốc và Nhật Bản cách nhau một vùng biển, nên ở đây hiểu là nước lân cận."),
    ("电信", "diànxìn", "điện tín", "danh từ", "viễn thông", "他在一家电信公司工作。", "Anh ấy làm việc ở một công ty viễn thông.",
     "Danh từ, chỉ việc truyền tin bằng điện thoại, điện báo, vô tuyến, tức là ngành viễn thông. Cẩn thận: tiếng Việt điện tín thường là bức điện báo; còn 电信 là cả ngành viễn thông, như 中国电信, China Telecom."),
    ("运营商", "yùnyíngshāng", "vận doanh thương", "danh từ", "nhà mạng, nhà cung cấp dịch vụ", "你的手机用的是哪个运营商？", "Điện thoại của bạn dùng nhà mạng nào?",
     "Danh từ, chỉ nhà cung cấp dịch vụ mạng, như 中国移动，中国联通，中国电信. Ở Việt Nam là Viettel, Vinaphone, MobiFone. 运营 là vận hành, kinh doanh; 商 là doanh nghiệp."),
    ("奖牌", "jiǎngpái", "tưởng bài", "danh từ", "huy chương", "这次运动会中国队获得了很多奖牌。", "Kỳ đại hội thể thao này đội Trung Quốc giành được rất nhiều huy chương.",
     "Danh từ, nghĩa là huy chương trao cho người thắng cuộc, thường gồm 金牌，银牌，铜牌, huy chương vàng, bạc, đồng. Lượng từ là 枚: 一枚奖牌."),
    ("提纯", "tíchún", "đề thuần", "động từ", "tinh chế, lọc cho tinh khiết", "这种金属需要经过提纯才能使用。", "Loại kim loại này phải qua tinh chế mới dùng được.",
     "Động từ, nghĩa là loại bỏ tạp chất cho tinh khiết. 提 là rút ra, 纯 là thuần, tinh khiết. Trong bài: 从中提纯了三十二公斤黄金, từ đó tinh chế được ba mươi hai ki-lô-gam vàng."),
    ("提炼", "tíliàn", "đề luyện", "động từ", "chiết xuất, tinh luyện; đúc kết", "这篇文章的观点是从大量调查中提炼出来的。", "Quan điểm của bài viết này được đúc kết từ rất nhiều cuộc khảo sát.",
     "Động từ, nghĩa gốc là dùng phương pháp hóa học, vật lý để lấy ra thứ cần thiết, như 提炼石油, lọc dầu; nghĩa bóng là đúc kết, khái quát. Trong bài: 从旧手机里提炼真金, chiết xuất vàng thật từ điện thoại cũ."),
    ("尚属", "shàngshǔ", "thượng thuộc", "động từ", "vẫn còn là, vẫn thuộc", "这种做法在国内尚属首次。", "Cách làm này ở trong nước vẫn còn là lần đầu tiên.",
     "Động từ, văn viết, nghĩa là vẫn còn thuộc về, vẫn còn là. 尚 là còn, 属 là thuộc. Cụm hay gặp nhất: 尚属首次, vẫn là lần đầu tiên. Đây là mẫu câu thứ nhất của bài."),
    ("视角", "shìjiǎo", "thị giác", "danh từ", "góc nhìn, góc độ", "这部电影从孩子的视角讲故事。", "Bộ phim này kể chuyện từ góc nhìn của một đứa trẻ.",
     "Danh từ, nghĩa là góc độ quan sát sự vật, nhìn nhận vấn đề. Cẩn thận, từ dễ nhầm: tiếng Việt thị giác là khả năng nhìn của mắt, tiếng Trung gọi là 视觉; còn 视角 là góc nhìn. Chữ cuối đọc là jiǎo."),
    ("挖掘", "wājué", "oạt quật", "động từ", "đào; khai thác, tìm tòi", "我们要挖掘每个学生的潜力。", "Chúng ta phải khai thác tiềm năng của mỗi học sinh.",
     "Động từ, nghĩa gốc là đào sâu xuống, nghĩa bóng là khai thác, phát hiện những tầng sâu hơn. Trong bài: 闲置物品的价值尚有很大的挖掘空间, giá trị của đồ để không vẫn còn nhiều dư địa để khai thác."),
    ("转卖", "zhuǎnmài", "chuyển mại", "động từ", "bán lại", "他把买来的票加价转卖了。", "Anh ta nâng giá bán lại số vé đã mua.",
     "Động từ, nghĩa là mua vào rồi bán lại cho người khác. Giới trẻ Việt Nam hay nói pass lại. Trong bài: 允许客户在平台转卖用过的宜家产品, cho phép khách hàng bán lại sản phẩm IKEA đã dùng ngay trên nền tảng."),
    ("匮乏", "kuìfá", "quỹ phạp", "tính từ", "thiếu thốn, khan hiếm", "那个年代，物质非常匮乏。", "Thời ấy, vật chất vô cùng thiếu thốn.",
     "Tính từ, văn viết, nghĩa là thiếu thốn. Từ này không có trong bảng từ của sách, nhưng xuất hiện trong bài khóa và bài tập bốn: 从当初物质的极度匮乏到如今商品的极大丰富, từ chỗ vật chất cực kỳ thiếu thốn đến chỗ hàng hóa vô cùng dồi dào."),
    ("变迁", "biànqiān", "biến thiên", "động từ", "đổi thay, biến đổi (qua thời gian dài)", "几十年来，这座城市发生了巨大的变迁。", "Mấy chục năm qua, thành phố này đã có những đổi thay to lớn.",
     "Động từ, cũng dùng như danh từ, chỉ sự thay đổi của sự vật qua thời gian dài. Tiếng Việt có câu bể dâu biến thiên. Chú ý: 变迁 khác 迁移, di dời chỗ ở; lát nữa trong bài tập ta sẽ gặp cặp từ này."),
    ("世代", "shìdài", "thế đại", "danh từ", "thế hệ; nhiều đời", "他们家世代都是农民。", "Nhà họ đời đời đều là nông dân.",
     "Danh từ, nghĩa là nhiều năm tháng, nhiều đời. Trong bài, Z世代 là thế hệ Z, những người sinh khoảng từ giữa thập niên chín mươi đến cuối thập niên hai nghìn, lớn lên cùng internet."),
    ("盲盒", "mánghé", "manh hạp", "danh từ", "hộp mù (blind box)", "很多年轻人喜欢买盲盒。", "Nhiều bạn trẻ thích mua hộp mù.",
     "Danh từ, chỉ loại hộp đồ chơi bên ngoài không ghi gì, phải mở ra mới biết mình bốc được món nào. 盲 là mù, 盒 là hộp. Ở Việt Nam, hộp mù Labubu cũng từng gây sốt."),
    ("廉价", "liánjià", "liêm giá", "tính từ", "giá rẻ, rẻ tiền", "这家超市的东西很廉价。", "Đồ ở siêu thị này rất rẻ.",
     "Tính từ, nghĩa là giá rẻ. Chữ 廉 vừa có nghĩa là liêm khiết, như 廉洁, vừa có nghĩa là rẻ. Đôi khi 廉价 mang sắc thái rẻ tiền, như 廉价劳动力, lao động giá rẻ."),
    ("囤", "tún", "độn", "động từ", "tích trữ, trữ (hàng)", "疫情期间很多人在家里囤了大米。", "Trong mùa dịch, nhiều người tích trữ gạo ở nhà.",
     "Động từ, ở đây đọc là tún, nghĩa là tích trữ. Cụm hay gặp: 囤货, trữ hàng. Trong bài: 转卖囤多了的纸尿裤, bán lại số bỉm đã tích trữ quá nhiều.", "屯"),
    ("财报", "cáibào", "tài báo", "danh từ", "báo cáo tài chính", "公司下周公布第三季度财报。", "Tuần sau công ty công bố báo cáo tài chính quý ba.",
     "Danh từ, là dạng nói tắt của 财务报表, báo cáo tài chính. Rất hay gặp trong tin kinh tế: 公布财报, công bố báo cáo tài chính."),
    ("吃土", "chītǔ", "ngật thổ", "động từ", "(từ lóng) “ăn đất”, cháy túi, hết sạch tiền", "这个月买了太多东西，只能吃土了。", "Tháng này mua nhiều đồ quá, chỉ còn nước ăn đất thôi.",
     "Động từ, từ lóng trên mạng: nghèo đến mức không có tiền ăn cơm, phải ăn đất. Thường dùng để đùa sau khi mua sắm quá tay, giống tiếng Việt nói cháy túi, ăn mì tôm cả tháng. 吃土少年 là cậu thiếu niên phải ăn đất."),
    ("回血", "huíxuè", "hồi huyết", "động từ", "(từ lóng) hồi máu; gỡ lại tiền, lấy lại sức", "把不用的东西卖掉，也能回点儿血。", "Bán bớt đồ không dùng cũng gỡ lại được chút tiền.",
     "Động từ, vốn là từ trong trò chơi điện tử: nhân vật hồi máu. Nghĩa mở rộng là hồi phục trạng thái, gỡ lại tiền. Trong bài, 回血青年 là bạn trẻ bán đồ cũ để gỡ lại số tiền đã tiêu."),
    ("剁手", "duòshǒu", "đóa thủ", "động từ", "(từ lóng) “chặt tay”, nghiện mua sắm online", "一到“双十一”，她就忍不住剁手。", "Cứ đến ngày hội mua sắm Song Thập Nhất là cô ấy lại không nhịn được mà mua quá tay.",
     "Động từ, nghĩa đen là chặt tay. Người mua sắm online quá tay hay tự nhận muốn chặt tay để khỏi bấm mua nữa, nên 剁手 chỉ việc nghiện mua sắm, tiêu tiền như nước. 剁手党 là hội nghiện mua sắm."),
    ("寿命", "shòumìng", "thọ mệnh", "danh từ", "tuổi thọ", "这种电池的使用寿命是五年。", "Tuổi thọ sử dụng của loại pin này là năm năm.",
     "Danh từ, nghĩa là số năm sống được, dùng cho cả người lẫn đồ vật. Trong bài có hai cụm: 使用寿命, tuổi thọ sử dụng, và 设计寿命, tuổi thọ thiết kế."),
    ("趋于", "qūyú", "xu vu", "động từ", "có xu hướng, dần dần đi đến", "病人的情况已经趋于稳定。", "Tình trạng bệnh nhân đã dần ổn định.",
     "Động từ, văn viết, nghĩa là hướng tới, dần đi đến một trạng thái. Sau 趋于 thường là tính từ hai âm tiết: 趋于稳定，趋于平静，趋于理性. Đây là mẫu câu thứ hai."),
    ("刻意", "kèyì", "khắc ý", "tính từ", "cố ý, cố tình, dụng công", "她并没有刻意打扮，却很漂亮。", "Cô ấy không hề cố tình trang điểm, vậy mà vẫn rất đẹp.",
     "Tính từ, hay dùng như phó từ, nghĩa là cố ý, dồn hết tâm tư vào. Trong bài: 共享的本质，不是刻意创造闲置, bản chất của chia sẻ không phải là cố tình tạo ra đồ để không. So với 故意, 刻意 nhấn mạnh sự dụng công, cố làm cho bằng được."),
    ("向来", "xiànglái", "hướng lai", "phó từ", "từ trước đến nay, xưa nay", "他向来不喝酒。", "Anh ấy xưa nay không uống rượu.",
     "Phó từ, nghĩa là từ trước tới nay vẫn luôn như vậy, giống 一向 và 从来. Đây là mẫu câu thứ ba của bài."),
    ("命门", "mìngmén", "mệnh môn", "danh từ", "chỗ hiểm yếu, tử huyệt", "价格是这家公司的命门。", "Giá cả là tử huyệt của công ty này.",
     "Danh từ, vốn là tên một huyệt đạo trong Đông y; nghĩa bóng là chỗ hiểm yếu nhất, nơi quyết định sống còn. Trong bài: 信任，向来是闲置交易的命门, lòng tin xưa nay là tử huyệt của giao dịch đồ cũ."),
    ("换言之", "huànyánzhī", "hoán ngôn chi", "cụm từ", "nói cách khác", "他没有回答，换言之，他不同意。", "Anh ấy không trả lời, nói cách khác, anh ấy không đồng ý.",
     "Cụm từ văn viết, dùng như liên từ, nghĩa là nói cách khác, giống 换句话说. 换 là đổi, 言 là lời, 之 là nó: đổi lời mà nói. Đây là mẫu câu thứ năm."),
    ("撮合", "cuōhe", "toát hợp", "động từ", "làm mai, se duyên; môi giới, kết nối", "朋友们想撮合他们俩。", "Bạn bè muốn se duyên cho hai người họ.",
     "Động từ, nghĩa là kéo hai bên lại với nhau cho thành chuyện, thường nói về hôn nhân, giao dịch. Chữ thứ hai đọc thanh nhẹ. Trong bài: 不仅要平台来撮合交易, không chỉ cần nền tảng kết nối giao dịch."),
    ("拓展", "tuòzhǎn", "thác triển", "động từ", "mở rộng, phát triển", "公司正在拓展海外市场。", "Công ty đang mở rộng thị trường nước ngoài.",
     "Động từ, nghĩa là khai phá và mở rộng. Chữ 拓 là khai mở, như trong 开拓. Trong bài: 闲鱼还将拓展新线下, Xianyu còn sẽ mở rộng mảng giao dịch trực tiếp kiểu mới."),
    ("触", "chù", "xúc", "động từ", "chạm, sờ, tiếp xúc", "展品请勿用手触摸。", "Xin đừng dùng tay sờ vào hiện vật trưng bày.",
     "Động từ, nghĩa là chạm vào, tiếp xúc. Hán Việt là xúc, như trong tiếp xúc, xúc giác. Trong bài: 线下交易最大的特征是可感可触, đặc điểm lớn nhất của giao dịch trực tiếp là cảm nhận được, sờ chạm được."),
    ("履约", "lǚyuē", "lý ước", "động từ", "thực hiện hợp đồng, giữ đúng giao ước", "双方都应该按时履约。", "Hai bên đều phải thực hiện hợp đồng đúng hạn.",
     "Động từ, văn viết, nghĩa là thực hiện điều đã giao ước. 履 là thực hiện, như trong 履行; 约 là ước hẹn, hợp đồng. Trong bài: 促进交易顺利履约, giúp giao dịch được thực hiện suôn sẻ."),
    ("缔造", "dìzào", "đế tạo", "động từ", "sáng lập, tạo dựng, kiến tạo", "他们缔造了一个商业奇迹。", "Họ đã tạo nên một kỳ tích kinh doanh.",
     "Động từ, văn viết, nghĩa là sáng lập, tạo dựng nên những điều lớn lao. Chữ đầu cũng có trong 缔结, ký kết. Đây là một kết hợp từ trọng điểm của bài."),
    ("专项", "zhuānxiàng", "chuyên hạng", "danh từ", "chuyên đề, hạng mục riêng", "政府拨出专项资金修建学校。", "Chính phủ cấp kinh phí riêng để xây trường học.",
     "Danh từ, chỉ một hạng mục riêng biệt. Hay gặp: 专项资金, kinh phí chuyên dùng; 专项治理, chấn chỉnh theo chuyên đề; 专项检查, kiểm tra chuyên đề."),
    ("坍塌", "tāntā", "than tháp", "động từ", "sụp đổ, đổ sập", "大雨过后，那座老房子坍塌了。", "Sau trận mưa lớn, căn nhà cũ ấy đã đổ sập.",
     "Động từ, nghĩa là sụp đổ, thường nói về nhà cửa, cầu cống, đất đá. Trong bài dùng nghĩa bóng: 信任坍塌, lòng tin sụp đổ."),
    ("追溯", "zhuīsù", "truy tố", "động từ", "truy nguyên, truy xuất (nguồn gốc)", "这个传统可以追溯到唐朝。", "Truyền thống này có thể truy ngược về đời Đường.",
     "Động từ, nghĩa là lần ngược về nguồn gốc. Cẩn thận, từ dễ nhầm: tiếng Việt truy tố là khởi tố ra tòa; còn 追溯 là truy nguyên. Trong bài: 物品可追溯性, khả năng truy xuất nguồn gốc của hàng hóa."),
    ("一连", "yīlián", "nhất liên", "phó từ", "liền, liên tiếp, một mạch", "他一连工作了十个小时。", "Anh ấy làm việc liền một mạch mười tiếng.",
     "Phó từ, chỉ động tác hay tình huống xảy ra liên tục, nhấn mạnh số lượng nhiều hoặc thời gian dài. Sau 一连 thường là động từ hoặc cụm số lượng. Đây là mẫu câu thứ sáu."),
    ("普罗大众", "pǔluó dàzhòng", "phổ la đại chúng", "danh từ", "quần chúng bình dân, người dân thường", "这项政策关系到普罗大众的生活。", "Chính sách này liên quan đến đời sống của người dân bình thường.",
     "Danh từ, nghĩa là dân chúng bình thường. 普罗 là phiên âm rút gọn của chữ prolétariat trong tiếng Pháp, giai cấp vô sản. Trong bài: 聚焦普罗大众, tập trung vào người dân bình thường."),
    ("换算", "huànsuàn", "hoán toán", "động từ", "quy đổi", "一美元换算成人民币大约是七元。", "Một đô la Mỹ quy đổi ra Nhân dân tệ khoảng bảy tệ.",
     "Động từ, nghĩa là quy đổi số lượng từ đơn vị này sang đơn vị khác. Trong bài: 换算成蚂蚁森林能量, quy đổi thành năng lượng của Rừng Kiến."),
    ("亩", "mǔ", "mẫu", "lượng từ", "mẫu (đơn vị diện tích ruộng đất)", "他家有十亩地。", "Nhà anh ấy có mười mẫu ruộng.",
     "Lượng từ, đơn vị đo diện tích ruộng đất của Trung Quốc. Chú ý: một mẫu Trung Quốc khoảng sáu trăm sáu mươi bảy mét vuông, mười lăm mẫu bằng một héc-ta; còn một mẫu Bắc Bộ của Việt Nam là ba nghìn sáu trăm mét vuông. Cùng tên nhưng khác hẳn nhau."),
    ("荒漠", "huāngmò", "hoang mạc", "danh từ", "hoang mạc", "这里曾经是一片荒漠。", "Nơi đây từng là một vùng hoang mạc.",
     "Danh từ, chỉ vùng đất hoang vắng mênh mông, âm Hán Việt và nghĩa giống hệt tiếng Việt. 荒漠化 là hoang mạc hóa, sa mạc hóa. Trong bài: 荒漠化土地, đất bị hoang mạc hóa."),
    ("庆幸", "qìngxìng", "khánh hạnh", "động từ", "mừng vì may mắn", "我很庆幸当时没有上那班飞机。", "Tôi rất mừng vì lúc đó đã không lên chuyến bay ấy.",
     "Động từ, nghĩa là vui mừng vì sự việc bất ngờ có kết cục tốt. Mẫu hay gặp ở đầu câu: 值得庆幸的是, điều đáng mừng là, như câu cuối bài khóa."),
    ("沉睡", "chénshuì", "trầm thụy", "động từ", "ngủ say; nằm im, chưa được đánh thức", "孩子在妈妈怀里沉睡着。", "Đứa bé đang ngủ say trong lòng mẹ.",
     "Động từ, nghĩa đen là ngủ say; nghĩa bóng là nằm im, chưa được khai thác. Trong bài: 物品的可贵不在沉睡而在流通, cái quý của đồ vật không nằm ở chỗ ngủ yên mà ở chỗ được lưu thông."),
    ("可贵", "kěguì", "khả quý", "tính từ", "đáng quý, quý báu", "诚实是一种可贵的品质。", "Trung thực là một phẩm chất đáng quý.",
     "Tính từ, nghĩa là đáng trân trọng, đáng coi trọng. Hay gặp: 难能可贵, hiếm có, đáng quý."),
]

add("bullets", chapter="Từ mới (48 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 7.1 có 48 từ mới, chia thành 16 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 囤 (tún) · 抽屉 (chōuti) · 撮合 (cuōhe) · 视角 (jiǎo) · 拓展 (tuò)",
           "Từ lóng mạng: 吃土 · 回血 · 剁手 · Từ dễ nhầm: 电信 · 视角 · 追溯 · 亩"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bảng từ của sách có bốn mươi bảy từ; thầy thêm từ 匮乏, có trong bài khóa và bài tập, thành bốn mươi tám từ, chia thành mười sáu nhóm nhỏ, mỗi nhóm ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Chú ý cách đọc của một số chữ: 囤 đọc là tún; 抽屉 và 撮合 có chữ thứ hai đọc thanh nhẹ; 视角 đọc là shìjiǎo; và 拓展 đọc là tuòzhǎn."),
         F(4, "Bài này có mấy từ lóng mạng rất thú vị: 吃土，回血，剁手. Còn những từ Hán Việt dễ hiểu nhầm như 电信，视角，追溯, và đơn vị 亩, các bạn nhớ nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

sizes = [3] * 16
assert sum(sizes) == len(V)
g = 0
for gs in sizes:
    group = V[g:g + gs]
    words, say = [], []
    for i, item in enumerate(group):
        assert len(item) in (8, 9), item[0]
        zh, py, hv, loai, vi, ex, exvi, expl = item[:8]
        spoken = item[8] if len(item) > 8 else zh
        n = g + i + 1
        words.append({"zh": zh, "py": py, "hv": hv.upper(), "loai": f"{n}. {loai}", "vi": vi, "ex": ex, "exvi": exvi})
        head = f"Từ số {n}: {zh}。 {zh}。 Hán Việt là {hv}."
        if spoken != zh:
            say.append(F(i, f"Từ số {n}: {spoken}。 {spoken}。 Hán Việt là {hv}.", zr=120, cap=head))
        else:
            say.append(F(i, head, zr=120))
        say.append(F(i, f"{expl} Ví dụ: {ex}{'' if ex[-1] in '。…？！，' else '，'} {exvi[0].upper() + exvi[1:]}{'' if exvi[-1] in '.!?' else '.'}", zr=130))
    add("vocab", section="Từ mới 生词", title=f"Từ mới ({g + 1}–{g + len(group)} / {len(V)})",
        words=words, say=say)
    g += gs

# ======================= BÀI KHÓA =======================
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung: số viết bằng chữ Hán, bỏ ngoặc kép])
P = [
    ("95后小林将一只裱好的iPhone5挂上闲鱼，定价120元。将旧手机零部件拆下，装裱好后再出售，成为许多年轻人的风尚。",
     "Tiểu Lâm, một bạn trẻ thế hệ sau 95, đăng lên Xianyu một chiếc iPhone 5 đã được đóng khung, giá 120 tệ. Tháo rời linh kiện của điện thoại cũ, đóng khung lại rồi đem bán đã trở thành trào lưu của nhiều người trẻ.",
     ["九五后 là thế hệ sinh từ năm 1995 đến 1999. 小林 là cậu Lâm, chữ 小 đặt trước họ để gọi thân mật người trẻ. 闲鱼, Xianyu, nghĩa đen là con cá nhàn rỗi, là ứng dụng mua bán đồ cũ lớn nhất Trung Quốc của tập đoàn Alibaba. 挂上闲鱼 là đăng bán lên Xianyu.",
      "将旧手机零部件拆下 là câu chữ 将, giống câu chữ 把 nhưng mang màu sắc văn viết: tháo linh kiện điện thoại cũ ra. 装裱好后再出售: đóng khung xong rồi mới bán. Bài báo mở đầu bằng một câu chuyện nhỏ rất cụ thể để dẫn vào vấn đề lớn."],
     "九五后小林将一只裱好的iPhone 5挂上闲鱼，定价一百二十元。将旧手机零部件拆下，装裱好后再出售，成为许多年轻人的风尚。"),
    ("旧手机何去何从，是一个问题。有数据显示，2015年至2019年，中国总共生产了94亿部手机。大量的旧手机闲置在人们的抽屉里。",
     "Điện thoại cũ đi đâu về đâu, đó là một vấn đề. Có số liệu cho thấy, từ năm 2015 đến năm 2019, Trung Quốc đã sản xuất tổng cộng 9,4 tỷ chiếc điện thoại. Rất nhiều điện thoại cũ đang nằm im trong ngăn kéo của mọi người.",
     ["何去何从 là thành ngữ: đi đâu, theo đâu, chỉ việc phải lựa chọn hướng đi. Lát nữa ta sẽ học kỹ. 有数据显示 là có số liệu cho thấy, cách mở đầu rất hay gặp trong văn báo chí.",
      "九十四亿部 là chín tỷ bốn trăm triệu chiếc: người Trung Quốc đếm theo vạn và ức, một 亿 là một trăm triệu. 部 là lượng từ của điện thoại, máy móc. 闲置在抽屉里: nằm không trong ngăn kéo."],
     "旧手机何去何从，是一个问题。有数据显示，二零一五年至二零一九年，中国总共生产了九十四亿部手机。大量的旧手机闲置在人们的抽屉里。"),
    ("放眼邻国日本，闲置手机也有新故事。为了迎接东京奥运会，日本最大的电信运营商都科摩公司（NTT Docomo）回收了621万部手机，日本奖牌制作团队从中提纯了32公斤黄金，3.5吨银和2.2吨铜。从旧手机里提炼真金做奖牌，这在奥运史上尚属首次。",
     "Nhìn sang nước láng giềng Nhật Bản, điện thoại để không cũng có câu chuyện mới. Để đón Thế vận hội Tokyo, nhà mạng lớn nhất Nhật Bản là NTT Docomo đã thu hồi 6,21 triệu chiếc điện thoại, đội chế tác huy chương của Nhật Bản đã tinh chế từ đó được 32 kg vàng, 3,5 tấn bạc và 2,2 tấn đồng. Chiết xuất vàng thật từ điện thoại cũ để làm huy chương, đây vẫn là lần đầu tiên trong lịch sử Olympic.",
     ["放眼邻国日本 là phóng tầm mắt sang nước láng giềng Nhật Bản. 奥运会 là Thế vận hội Olympic, nói tắt của 奥林匹克运动会. 都科摩 là tên phiên âm của Docomo. 回收 là thu hồi, tái chế.",
      "从中提纯 là tinh chế từ trong đó. 提炼真金做奖牌: chiết xuất vàng thật làm huy chương. 尚属首次 là vẫn còn là lần đầu, mẫu câu thứ nhất của bài. Thế vận hội Tokyo vốn dự kiến năm 2020, do dịch bệnh lùi sang năm 2021."],
     "放眼邻国日本，闲置手机也有新故事。为了迎接东京奥运会，日本最大的电信运营商都科摩公司回收了六百二十一万部手机，日本奖牌制作团队从中提纯了三十二公斤黄金，三点五吨银和二点二吨铜。从旧手机里提炼真金做奖牌，这在奥运史上尚属首次。"),
    ("旧手机的去向提供了两个视角：向左看，还有巨量的闲置物品没有进入流通；向右看，闲置物品的价值尚有很大的挖掘空间。",
     "Đích đến của điện thoại cũ mở ra hai góc nhìn: nhìn sang trái, vẫn còn một lượng khổng lồ đồ để không chưa đi vào lưu thông; nhìn sang phải, giá trị của đồ để không vẫn còn rất nhiều dư địa để khai thác.",
     ["去向 là nơi đi tới, hướng đi. 巨量 là lượng khổng lồ. 进入流通 là đi vào lưu thông, tức là được mua bán, sử dụng lại.",
      "尚有 là vẫn còn có, chữ 尚 giống trong 尚属. 挖掘空间 là dư địa khai thác. Hai vế 向左看，向右看 đối nhau rất cân, khép lại phần mở đầu: một mặt là vấn đề, một mặt là cơ hội."]),
    ("十年前，宜家在瑞典推出共享模式的网络平台，允许客户在平台转卖用过的宜家产品，这给那些爱宜家但囊中羞涩的人一种新的选择。",
     "Mười năm trước, IKEA đã cho ra mắt ở Thụy Điển một nền tảng trực tuyến theo mô hình chia sẻ, cho phép khách hàng bán lại sản phẩm IKEA đã qua sử dụng ngay trên nền tảng. Điều này mang lại một lựa chọn mới cho những người yêu thích IKEA nhưng lại eo hẹp về tiền bạc.",
     ["Đây là đoạn đầu của tiêu đề nhỏ thứ nhất: 闲置经济是真正的共享经济, trùng với tên bài. 宜家 là IKEA, hãng nội thất nổi tiếng của Thụy Điển; 瑞典 là Thụy Điển. 推出 là cho ra mắt.",
      "允许客户在平台转卖: cho phép khách bán lại trên nền tảng. 囊中羞涩 là thành ngữ: trong túi ngại ngùng, tức là cách nói khéo của việc túi tiền eo hẹp. Câu trúc 给某人一种新的选择 là mang lại cho ai một lựa chọn mới."]),
    ("改革开放四十多年来，从当初物质的极度匮乏到如今商品的极大丰富，公众消费理念的变迁显而易见。同样的东西，你视为垃圾，别人可能视为宝贝。",
     "Hơn bốn mươi năm cải cách mở cửa, từ chỗ vật chất cực kỳ thiếu thốn ngày trước đến chỗ hàng hóa vô cùng dồi dào ngày nay, sự đổi thay trong quan niệm tiêu dùng của công chúng là điều ai cũng thấy rõ. Cùng một món đồ, bạn coi là rác, người khác có thể coi là báu vật.",
     ["改革开放 là cải cách mở cửa, bắt đầu từ năm 1978. Cấu trúc 从……到…… là từ… đến…, ở đây đối lập 极度匮乏 với 极大丰富, cực kỳ thiếu thốn và vô cùng dồi dào.",
      "消费理念 là quan niệm tiêu dùng. 显而易见 là thành ngữ: rõ ràng, dễ thấy. 你视为垃圾，别人可能视为宝贝: 视为 là coi là, văn viết. Câu này giống tục ngữ tiếng Anh: rác của người này là kho báu của người kia."]),
    ("Z世代买二手球鞋、盲盒，旧物成了宝贝；白领阶层买廉价婴儿床，转卖囤多了的纸尿裤；二手母婴产品、二手车、二手手机都是千亿元以上的市场。",
     "Thế hệ Z mua giày thể thao cũ, hộp mù, đồ cũ thành báu vật; giới văn phòng mua cũi trẻ em giá rẻ, bán lại số bỉm tích trữ quá nhiều; đồ mẹ và bé cũ, ô tô cũ, điện thoại cũ đều là những thị trường trên trăm tỷ tệ.",
     ["Ba vế câu cách nhau bằng dấu chấm phẩy, liệt kê ba nhóm người và thị trường: Z世代 là thế hệ Z; 白领阶层 là tầng lớp cổ cồn trắng, dân văn phòng; 二手球鞋 là giày thể thao cũ, nhiều đôi giày hiếm còn đắt hơn giày mới.",
      "婴儿床 là cũi trẻ em; 纸尿裤 là bỉm, tã giấy; 囤多了 là tích trữ quá nhiều. 母婴产品 là đồ dùng mẹ và bé. 千亿元以上 là trên một trăm tỷ tệ: 千亿 là nghìn ức, tức một trăm tỷ."],
     "Z世代买二手球鞋、盲盒，旧物成了宝贝；白领阶层买廉价婴儿床，转卖囤多了的纸尿裤；二手母婴产品、二手车、二手手机都是千亿元以上的市场。"),
    ("今年5月，阿里巴巴公布的2020年财报中，闲鱼年成交额已突破2000亿元。从阿里内部视角看，新与旧，也没有天然鸿沟。在平台上，天猫、淘宝、闲鱼互相打通。",
     "Tháng 5 năm nay, trong báo cáo tài chính năm 2020 mà Alibaba công bố, doanh số giao dịch hằng năm của Xianyu đã vượt 200 tỷ tệ. Nhìn từ góc độ nội bộ Alibaba, giữa mới và cũ cũng chẳng có hố sâu ngăn cách tự nhiên nào. Trên nền tảng, Tmall, Taobao và Xianyu được kết nối thông suốt với nhau.",
     ["今年 ở đây là năm 2020, năm bài báo ra đời. 成交额 là doanh số giao dịch; 突破 là vượt qua mốc. 两千亿元 là hai nghìn ức, tức hai trăm tỷ tệ.",
      "鸿沟 là hố sâu ngăn cách. 天猫 là Tmall, sàn bán hàng mới chính hãng; 淘宝 là Taobao, chợ online; 闲鱼 bán đồ cũ: cả ba đều của Alibaba. 互相打通 là kết nối thông suốt, ví dụ dùng chung tài khoản, đồ mua trên Taobao có thể bán lại ngay trên Xianyu."],
     "今年五月，阿里巴巴公布的二零二零年财报中，闲鱼年成交额已突破两千亿元。从阿里内部视角看，新与旧，也没有天然鸿沟。在平台上，天猫、淘宝、闲鱼互相打通。"),
    ("越来越多年轻人拥抱新品也不拒绝二手。“双11”之前，他们自称“吃土少年”；“双11”之后，则出掉闲置物成为“回血青年”。剁手时“说买就买”，闲置不用时出手依然迅速。",
     "Ngày càng nhiều người trẻ vừa đón nhận hàng mới vừa không từ chối đồ cũ. Trước ngày 11 tháng 11, họ tự gọi mình là thiếu niên ăn đất; sau ngày 11 tháng 11, họ lại bán bớt đồ không dùng để thành thanh niên hồi máu. Lúc mua sắm thì muốn mua là mua, lúc đồ để không thì bán đi cũng nhanh không kém.",
     ["拥抱新品 là ôm lấy, đón nhận hàng mới. 双十一 là ngày 11 tháng 11, vốn là Ngày Độc thân, nay là lễ hội mua sắm online lớn nhất Trung Quốc. 吃土少年 là cháy túi vì mua sắm; 回血青年 là bán đồ cũ để gỡ lại tiền.",
      "则 là thì, lại, văn viết, chỉ sự đối lập với vế trước. 出掉闲置物 là bán đi đồ không dùng; 出手 là bán ra, ra tay. 说买就买 là nói mua là mua ngay, mẫu 说A就A chỉ sự quyết đoán, nhanh gọn."],
     "越来越多年轻人拥抱新品也不拒绝二手。双十一之前，他们自称吃土少年；双十一之后，则出掉闲置物成为回血青年。剁手时说买就买，闲置不用时出手依然迅速。"),
    ("有报告显示，预计2020年中国闲置市场规模可达到1万亿元。",
     "Có báo cáo cho thấy, dự kiến năm 2020 quy mô thị trường đồ cũ của Trung Quốc có thể đạt 1 nghìn tỷ tệ.",
     ["Đoạn chỉ có một câu, nhưng con số rất ấn tượng: 一万亿元 là một vạn ức, tức một nghìn tỷ tệ. Đây cũng là con số trong tên gốc của bài báo: 市场规模达一万亿元.",
      "有报告显示 giống 有数据显示 ở đoạn hai: cách dẫn số liệu khách quan của văn báo chí. 预计 là dự kiến, ước tính; 可达到 là có thể đạt tới."],
     "有报告显示，预计二零二零年中国闲置市场规模可达到一万亿元。"),
    ("今天消费品的平均使用寿命远远低于其设计寿命，而“喜新厌旧”造就了闲置物品的庞大市场，其本质是形成不同消费层次对物品各个生命阶段的共享。",
     "Ngày nay, tuổi thọ sử dụng trung bình của hàng tiêu dùng thấp hơn rất nhiều so với tuổi thọ thiết kế của chúng, và thói có mới nới cũ đã tạo nên thị trường đồ cũ khổng lồ, bản chất của nó là hình thành sự chia sẻ giữa các tầng lớp tiêu dùng khác nhau đối với từng giai đoạn trong vòng đời của món đồ.",
     ["远远低于其设计寿命: thấp hơn xa tuổi thọ thiết kế của nó; 其 là của nó, văn viết. Ví dụ một chiếc điện thoại thiết kế để dùng năm năm, nhưng người ta hai năm đã đổi máy mới.",
      "喜新厌旧 là thành ngữ: thích mới chán cũ, giống có mới nới cũ. 造就 là tạo nên. 其本质是 là bản chất của nó là. Đây chính là câu trả lời cho tên bài: đồ cũ được chuyển từ người dùng ở tầng tiêu dùng này sang người ở tầng khác, đó mới là chia sẻ thật sự."]),
    ("在国内共享经济从涨潮、退潮再到趋于理性的过程中，全社会也在形成一种共识：共享的本质，不是刻意创造闲置，而是合理消化闲置，是将有限资源服务于更多群体。",
     "Trong quá trình kinh tế chia sẻ ở trong nước đi từ lúc thủy triều dâng, đến lúc thủy triều rút, rồi dần trở nên lý trí, toàn xã hội cũng đang hình thành một nhận thức chung: bản chất của chia sẻ không phải là cố tình tạo ra đồ để không, mà là tiêu hóa đồ để không một cách hợp lý, là đem nguồn tài nguyên có hạn phục vụ cho nhiều nhóm người hơn.",
     ["涨潮，退潮 là thủy triều lên, thủy triều xuống, ví với sự bùng nổ rồi thoái trào của kinh tế chia sẻ, như cơn sốt xe đạp chia sẻ rồi hàng loạt công ty phá sản. 趋于理性 là dần trở nên lý trí, mẫu câu thứ hai của bài.",
      "共识 là nhận thức chung. 不是A，而是B là không phải A mà là B. 刻意创造闲置 là cố tình tạo ra đồ thừa, ví dụ tung ra hàng triệu chiếc xe đạp chia sẻ không ai dùng. 将有限资源服务于更多群体: đem tài nguyên có hạn phục vụ nhiều người hơn."]),
    ("当然，闲置交易并非没有门槛，信任，向来是闲置交易的命门。闲鱼在交易领域推出“无忧购”，具体来说，“无忧购”是一套由服务商提供回收、鉴定服务，平台严把质量关、客服关的全方位服务体系。",
     "Tất nhiên, giao dịch đồ cũ không phải là không có rào cản; lòng tin xưa nay vẫn là tử huyệt của giao dịch đồ cũ. Xianyu đã cho ra mắt dịch vụ Mua không lo trong lĩnh vực giao dịch. Cụ thể, Mua không lo là một hệ thống dịch vụ toàn diện, trong đó nhà cung cấp dịch vụ lo việc thu mua, giám định, còn nền tảng kiểm soát chặt chẽ khâu chất lượng và khâu chăm sóc khách hàng.",
     ["Đây là tiêu đề nhỏ thứ hai: 信任是打开闲置交易的钥匙, lòng tin là chìa khóa mở ra giao dịch đồ cũ. 并非 là hoàn toàn không phải, văn viết. 门槛 là ngưỡng cửa, rào cản. 向来是……的命门: xưa nay là tử huyệt của…, mẫu câu thứ ba.",
      "无忧购 là Mua không lo. 具体来说 là nói cụ thể. 由服务商提供回收、鉴定服务: chữ 由 giới thiệu người thực hiện. 严把质量关、客服关 là giữ chặt cửa ải chất lượng và chăm sóc khách hàng, mẫu câu thứ tư 严把关."]),
    ("换言之，用户既要一个自由的市场，更要一个规范的市场，不仅要平台来撮合交易，更要平台来担保交易。",
     "Nói cách khác, người dùng vừa cần một thị trường tự do, lại càng cần một thị trường có quy chuẩn; không chỉ cần nền tảng đứng ra kết nối giao dịch, mà càng cần nền tảng đứng ra bảo đảm cho giao dịch.",
     ["换言之 là nói cách khác, mẫu câu thứ năm. Đoạn này dùng hai cặp liên từ song song: 既要……更要…… là vừa cần… càng cần…; 不仅要……更要…… là không chỉ cần… mà càng cần…. Chữ 更 nhấn mạnh vế sau quan trọng hơn.",
      "规范 là có quy chuẩn, có phép tắc. 撮合交易 là kết nối, làm cầu nối cho giao dịch. 担保 là bảo lãnh, bảo đảm: nếu hàng giả, hàng kém chất lượng thì nền tảng chịu trách nhiệm."]),
    ("与此同时，闲鱼还将拓展“新线下”。比起线上交易，线下交易最大的特征是可感可触、就近直接。做好线下这个信任场，可以促进交易顺利履约。",
     "Đồng thời, Xianyu còn sẽ mở rộng mảng giao dịch trực tiếp kiểu mới. So với giao dịch trực tuyến, đặc điểm lớn nhất của giao dịch trực tiếp là cảm nhận được, sờ chạm được, gần gũi và trực tiếp. Làm tốt không gian tạo lòng tin trực tiếp này có thể giúp giao dịch được thực hiện suôn sẻ.",
     ["与此同时 là cùng lúc đó, đồng thời. 线上 là online, trực tuyến; 线下 là offline, trực tiếp. 新线下 là mô hình offline kiểu mới, ví dụ các điểm thu mua, cửa hàng đồ cũ của nền tảng.",
      "比起A，B…… là so với A thì B…. 可感可触 là cảm được, chạm được. 就近直接 là ở gần, trực tiếp. 信任场 là không gian tạo dựng lòng tin. 履约 là thực hiện giao dịch đã thỏa thuận."]),
    ("缔造信任空间是多方面的。除了物品真实性、物品质量、安全风险，还涉及个人隐私等问题。今年，闲鱼展开了专项治理行动，看来是铁了心要治理平台问题，说白了也是要防止交易中的信任坍塌。",
     "Tạo dựng không gian lòng tin là việc của nhiều phương diện. Ngoài tính xác thực của món đồ, chất lượng món đồ và rủi ro an toàn, còn liên quan đến các vấn đề như quyền riêng tư cá nhân. Năm nay, Xianyu đã triển khai chiến dịch chấn chỉnh chuyên đề, xem ra là đã quyết tâm sắt đá giải quyết các vấn đề của nền tảng; nói thẳng ra, cũng là để ngăn lòng tin trong giao dịch sụp đổ.",
     ["缔造信任空间 là tạo dựng không gian lòng tin. 除了……，还涉及…… là ngoài… còn liên quan đến…. 个人隐私 là quyền riêng tư cá nhân, ví dụ lộ số điện thoại, địa chỉ khi gửi hàng.",
      "专项治理行动 là chiến dịch chấn chỉnh theo chuyên đề. 铁了心 là quán ngữ: lòng đã hóa sắt, tức là quyết tâm không lay chuyển. 说白了 là nói trắng ra, nói thẳng ra, khẩu ngữ. 信任坍塌 là lòng tin sụp đổ."]),
    ("从长远来看，信任提升依赖技术提升。随着大数据、人工智能等技术手段的落地，物品可追溯性将大大提升，做到有案可稽。",
     "Về lâu dài, nâng cao lòng tin phải dựa vào nâng cao công nghệ. Cùng với việc các phương tiện kỹ thuật như dữ liệu lớn, trí tuệ nhân tạo được đưa vào ứng dụng thực tế, khả năng truy xuất nguồn gốc của hàng hóa sẽ được nâng cao rất nhiều, đạt tới mức có hồ sơ để tra cứu.",
     ["从长远来看 là xét về lâu dài. 依赖 là dựa vào, phụ thuộc vào. 大数据 là dữ liệu lớn, big data; 人工智能 là trí tuệ nhân tạo, AI. 落地 là hạ cánh, nghĩa bóng là được đưa vào thực tế.",
      "可追溯性 là khả năng truy xuất nguồn gốc. 有案可稽 là thành ngữ: có hồ sơ để tra, chứng cứ rõ ràng; chữ cuối đọc là jī, nghĩa là tra xét. Ý nói mỗi món đồ đều có lý lịch rõ ràng, không thể gian lận."]),
    ("这几年来，国内循环经济发展，一连出台了多项政策措施。有几个很醒目的政策：支持共享经济，提倡垃圾分类，倡导光盘行动。它们的一个共同特点，是围绕衣食住行，聚焦普罗大众。",
     "Mấy năm nay, để phát triển kinh tế tuần hoàn trong nước, nhà nước đã liên tiếp ban hành nhiều chính sách, biện pháp. Có mấy chính sách rất nổi bật: ủng hộ kinh tế chia sẻ, khuyến khích phân loại rác, kêu gọi phong trào ăn sạch đĩa. Điểm chung của chúng là xoay quanh chuyện ăn mặc ở đi lại, tập trung vào người dân bình thường.",
     ["Đây là tiêu đề nhỏ thứ ba: 深挖浪费变消费的社会价值, đào sâu giá trị xã hội của việc biến lãng phí thành tiêu dùng. 循环经济 là kinh tế tuần hoàn. 一连出台 là liên tiếp ban hành, mẫu câu thứ sáu. 醒目 là bắt mắt, nổi bật.",
      "提倡，倡导 đều là đề xướng, kêu gọi. 光盘行动 là phong trào ăn sạch đĩa, chống lãng phí thức ăn. 衣食住行 là ăn, mặc, ở, đi lại, tức mọi nhu cầu cơ bản. 普罗大众 là người dân bình thường."]),
    ("闲鱼团队自认为闲置交易“离钱比较近，离赚钱比较远”。从2018年起，除了闲置交易，团队促进了超过325万用户回收家中的闲置旧衣，超过70万用户回收了图书，大约150万部手机和60万件大家电也得到了环保回收。换算成蚂蚁森林能量，大约能解决16736亩荒漠化土地。",
     "Đội ngũ Xianyu tự nhận rằng giao dịch đồ cũ thì gần tiền nhưng xa chuyện kiếm tiền. Từ năm 2018, ngoài giao dịch đồ cũ, đội ngũ còn thúc đẩy hơn 3,25 triệu người dùng thu gom quần áo cũ không dùng trong nhà, hơn 700 nghìn người dùng thu gom sách, khoảng 1,5 triệu chiếc điện thoại và 600 nghìn món đồ điện gia dụng lớn cũng được thu hồi theo cách thân thiện với môi trường. Quy đổi thành năng lượng Rừng Kiến, có thể cải tạo khoảng 16.736 mẫu đất bị hoang mạc hóa.",
     ["离钱比较近，离赚钱比较远: tiền đi qua tay rất nhiều, nhưng lợi nhuận thu về không bao nhiêu, vì phí giao dịch đồ cũ rất thấp. 自认为 là tự cho rằng. 促进 là thúc đẩy. 大家电 là đồ điện gia dụng lớn như tủ lạnh, máy giặt.",
      "蚂蚁森林 là Rừng Kiến, chương trình của Alipay: hành vi sống xanh được tính thành năng lượng xanh, tích đủ thì được trồng một cây thật. 换算成 là quy đổi thành. 一万六千七百三十六亩 là khoảng một nghìn một trăm héc-ta."],
     "闲鱼团队自认为闲置交易离钱比较近，离赚钱比较远。从二零一八年起，除了闲置交易，团队促进了超过三百二十五万用户回收家中的闲置旧衣，超过七十万用户回收了图书，大约一百五十万部手机和六十万件大家电也得到了环保回收。换算成蚂蚁森林能量，大约能解决一万六千七百三十六亩荒漠化土地。"),
    ("经历了几十年经济的高增长，伴随物质财富的迅速积累，人们习惯了在消费上“追新”，造成国内闲置产品规模巨大，由此带来的浪费超乎想象。",
     "Trải qua mấy chục năm kinh tế tăng trưởng cao, cùng với sự tích lũy nhanh chóng của của cải vật chất, người ta đã quen chạy theo cái mới trong tiêu dùng, khiến quy mô đồ để không trong nước rất lớn, sự lãng phí do đó gây ra vượt xa sức tưởng tượng.",
     ["高增长 là tăng trưởng cao. 伴随 là đi kèm, cùng với. 财富的迅速积累 là của cải tích lũy nhanh. 追新 là chạy theo cái mới, ví dụ điện thoại vừa ra mẫu mới là đổi ngay.",
      "造成 là gây ra, thường đi với kết quả xấu. 由此带来的浪费 là sự lãng phí do đó mà ra; 由此 là từ đó, do đó. 超乎想象 là vượt ngoài tưởng tượng, kết hợp từ trọng điểm của bài."]),
    ("值得庆幸的是，随着绿色发展理念深入人心，“物品的可贵不在沉睡而在流通；物品的使用比占有更具价值”的消费观正在闲置交易中得以践行。",
     "Điều đáng mừng là, cùng với việc lý niệm phát triển xanh ngày càng thấm sâu vào lòng người, quan niệm tiêu dùng cái quý của đồ vật không nằm ở chỗ ngủ yên mà ở chỗ được lưu thông; sử dụng đồ vật có giá trị hơn sở hữu nó đang được hiện thực hóa trong giao dịch đồ cũ.",
     ["值得庆幸的是 là điều đáng mừng là. 深入人心 là thấm sâu vào lòng người. 不在A而在B là không nằm ở A mà nằm ở B. 使用比占有更具价值: dùng có giá trị hơn sở hữu; 更具 là càng có, văn viết.",
      "得以践行 là được thực hiện, được đưa vào thực tiễn; 得以 là nhờ đó mà có thể. Câu kết trả lời trọn vẹn tên bài: dùng chứ không cần sở hữu, đó chính là tinh thần của kinh tế chia sẻ, và giao dịch đồ cũ đang làm được điều đó."],
     "值得庆幸的是，随着绿色发展理念深入人心，物品的可贵不在沉睡而在流通；物品的使用比占有更具价值的消费观正在闲置交易中得以践行。"),
]

# tiêu đề nhỏ của bài khóa: đoạn bắt đầu phần đó
HEAD = {5: "闲置经济是真正的共享经济", 13: "“信任”是打开闲置交易的钥匙", 18: "深挖“浪费变消费”的社会价值"}

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 闲置经济是真正的共享经济", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa. Bài được cải biên từ bài báo 市场规模达一万亿元，闲置经济是真正的共享经济, Quy mô thị trường đạt một nghìn tỷ tệ, kinh tế đồ cũ mới là kinh tế chia sẻ thực sự, của tác giả 周蕊, đăng trên 新华每日电讯, Tân Hoa Mỗi Nhật Điện Tấn, ngày hai tháng mười hai năm hai nghìn không trăm hai mươi. Bài có một phần mở đầu và ba tiêu đề nhỏ.",
         F(0, "Thầy chia bài thành hai mươi mốt đoạn ngắn; những đoạn dài trong sách được tách làm hai. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 90 else 50 if len(zh) <= 115 else 46
    title = f"Bài khóa – đoạn {i}/{len(P)}" + (f" · {HEAD[i]}" if i in HEAD else "")
    add("passage", section="Bài khóa 课文", title=title, zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Bố cục & ghi chú", section="Bài khóa 课文", title="Bố cục bài khóa", size=33,
    items=["## 1. Mở đầu: điện thoại cũ đi đâu về đâu? (đoạn 1–4)",
           "iPhone đóng khung · 94 亿部 điện thoại nằm trong ngăn kéo · Nhật lấy vàng làm huy chương → 两个视角",
           "## 2. 闲置经济是真正的共享经济 (đoạn 5–12)",
           "IKEA · 消费理念的变迁 · 闲鱼 2000 亿元 · 吃土少年→回血青年 · 1 万亿元 · 共享的本质",
           "## 3. “信任”是打开闲置交易的钥匙 (đoạn 13–17)",
           "无忧购 · 新线下 · 专项治理 · 大数据、人工智能 → 有案可稽",
           "## 4. 深挖“浪费变消费”的社会价值 (đoạn 18–21)",
           "政策: 共享经济、垃圾分类、光盘行动 · 回收旧衣、图书、手机 · 物品的使用比占有更具价值"],
    say=["Trước khi sang phần mẫu câu, chúng ta cùng nhìn lại bố cục bài khóa. Đây là một bài báo bình luận kinh tế, có bốn phần.",
         F(1, "Phần một, mở đầu: từ chiếc iPhone đóng khung của Tiểu Lâm, tác giả đặt câu hỏi điện thoại cũ đi đâu về đâu. Chín tỷ bốn trăm triệu chiếc điện thoại nằm trong ngăn kéo, trong khi Nhật Bản lấy vàng từ điện thoại cũ làm huy chương. Từ đó mở ra hai góc nhìn: vấn đề lãng phí và cơ hội khai thác giá trị."),
         F(3, "Phần hai, tiêu đề 闲置经济是真正的共享经济: quan niệm tiêu dùng đã thay đổi, thị trường đồ cũ lên tới nghìn tỷ tệ, người trẻ vừa mua mới vừa bán cũ. Bản chất của chia sẻ là tiêu hóa hợp lý đồ để không, chứ không phải cố tình tạo ra nó."),
         F(5, "Phần ba, tiêu đề 信任是打开闲置交易的钥匙: lòng tin là tử huyệt. Xianyu xây dựng lòng tin bằng dịch vụ Mua không lo, mảng giao dịch trực tiếp, chiến dịch chấn chỉnh, và về lâu dài là bằng công nghệ."),
         F(7, "Phần bốn, tiêu đề 深挖浪费变消费的社会价值: nhà nước khuyến khích kinh tế tuần hoàn, Xianyu thu gom quần áo, sách, điện thoại cũ. Kết luận: cái quý của đồ vật nằm ở lưu thông, dùng có giá trị hơn sở hữu.")])

add("bullets", section="Bài khóa 课文", title="Ghi chú 注释: hiểu thêm về bối cảnh", size=32,
    items=["装裱（流行装置）: vốn là bồi tranh; ở đây là tháo linh kiện điện thoại cũ, đóng khung thành tác phẩm trang trí",
           "光盘行动 (2013): “光盘” = ăn sạch đĩa; phong trào trân trọng lương thực, chống lãng phí; lọt top 10 từ thịnh hành năm 2020",
           "蚂蚁森林 (Alipay, 27/8/2016): hành vi sống xanh → “绿色能量” → trồng cây thật ở vùng cần phục hồi sinh thái; giải 地球卫士奖 của LHQ (2019)",
           "闲鱼 Xianyu: app đồ cũ của Alibaba · 天猫 Tmall · 淘宝 Taobao · 双11: lễ hội mua sắm 11/11"],
    say=["Sách có ba ghi chú giúp hiểu thêm bối cảnh bài khóa; thầy bổ sung thêm một ghi chú về các nền tảng của Alibaba.",
         F(0, "Một: 装裱, ở đây sách gọi là 流行装置, món đồ trang trí thịnh hành. Nghĩa gốc là bồi giấy vào mặt sau tranh, thư pháp để làm đẹp và bảo quản. Trong bài là tháo rời linh kiện điện thoại cũ, sắp xếp đẹp mắt trong khung, thành một tác phẩm sắp đặt nghệ thuật."),
         F(1, "Hai: 光盘行动. Năm hai nghìn không trăm mười ba, Trung Quốc phát động phong trào ăn sạch đĩa: 光盘 ở đây không phải đĩa CD, mà là ăn sạch thức ăn trong đĩa. Mục đích là tạo thói quen trân trọng lương thực, chống lãng phí. Ngày bốn tháng mười hai năm hai nghìn không trăm hai mươi, 光盘行动 lọt vào mười từ thịnh hành nhất của năm."),
         F(2, "Ba: 蚂蚁森林, Rừng Kiến, ra mắt ngày hai mươi bảy tháng tám năm hai nghìn không trăm mười sáu, do tập đoàn Alibaba khởi xướng trên ứng dụng Alipay. Mỗi hành vi giảm phát thải, như đi bộ, thanh toán điện tử, được tính thành năng lượng xanh; tích đủ năng lượng thì có thể đăng ký trồng một cây thật ở vùng cần phục hồi sinh thái. Năm hai nghìn không trăm mười chín, dự án được Liên Hợp Quốc trao giải Nhà vô địch Trái Đất, 地球卫士奖."),
         F(3, "Bốn: 闲鱼, 天猫, 淘宝 đều là nền tảng của Alibaba; còn 双十一, ngày mười một tháng mười một, là lễ hội mua sắm trực tuyến lớn nhất Trung Quốc, cũng rất quen thuộc với người dùng Shopee, Lazada ở Việt Nam.")])

# ======================= MẪU CÂU =======================
add("bullets", chapter="Mẫu câu: 尚属 · 趋于 · 向来", section="Mẫu câu 重点句型", title="1. 尚属…… · 2. 趋于……", size=33,
    items=["## 尚属: vẫn còn thuộc về, vẫn còn là (văn viết; hay gặp: 尚属首次)",
           "从旧手机里提炼真金做奖牌，这在奥运史上尚属首次。",
           "我国尚属发展中国家，经济发展还不平衡。",
           "本周四，深圳航空公司成立了外籍飞行员分部，这在中国民航业中尚属首次。",
           "## 趋于 + tính từ (2 âm tiết): dần hướng tới, có xu hướng",
           "在国内共享经济从涨潮、退潮再到趋于理性的过程中，全社会也在形成一种共识。",
           "时间，让一些东西更清晰，让一些感情更明白，让一切都趋于平静。",
           "自从来到了这个城市工作，他的生活便趋于稳定，日子过得波澜不惊。"],
    say=["Bây giờ chúng ta sang phần mẫu câu trọng điểm. Bài có sáu mẫu, thầy chia thành ba slide.",
         F(0, "Mẫu thứ nhất: 尚属, nghĩa là vẫn còn thuộc về, vẫn còn là. Đây là cách nói văn viết; cụm hay gặp nhất là 尚属首次, vẫn còn là lần đầu tiên, và 尚属正常, vẫn còn trong mức bình thường."),
         F(1, "Ví dụ một, lấy từ bài khóa: 从旧手机里提炼真金做奖牌，这在奥运史上尚属首次。 Chiết xuất vàng thật từ điện thoại cũ làm huy chương, đây vẫn là lần đầu tiên trong lịch sử Olympic."),
         F(2, "Ví dụ hai: 我国尚属发展中国家，经济发展还不平衡。 Nước ta vẫn còn là nước đang phát triển, kinh tế phát triển chưa đồng đều."),
         F(3, "Ví dụ ba: 本周四，深圳航空公司成立了外籍飞行员分部，这在中国民航业中尚属首次。 Thứ năm tuần này, hãng hàng không Thâm Quyến thành lập bộ phận phi công nước ngoài, điều này trong ngành hàng không dân dụng Trung Quốc vẫn là lần đầu."),
         F(4, "Mẫu thứ hai: 趋于, nghĩa là dần hướng tới. Sau 趋于 thường là một tính từ hai âm tiết chỉ trạng thái: 趋于稳定，趋于平静，趋于成熟，趋于理性."),
         F(5, "Ví dụ một, lấy từ bài khóa: 在国内共享经济从涨潮、退潮再到趋于理性的过程中，全社会也在形成一种共识。 Kinh tế chia sẻ đi từ lúc thủy triều dâng, thủy triều rút, rồi dần trở nên lý trí."),
         F(6, "Ví dụ hai: 时间，让一些东西更清晰，让一些感情更明白，让一切都趋于平静。 Thời gian khiến một số điều rõ ràng hơn, một số tình cảm minh bạch hơn, khiến mọi thứ dần lắng lại."),
         F(7, "Ví dụ ba: 自从来到了这个城市工作，他的生活便趋于稳定，日子过得波澜不惊。 Từ khi đến thành phố này làm việc, cuộc sống của anh ấy dần ổn định, ngày tháng trôi qua êm đềm. 波澜不惊 là mặt nước không gợn sóng, chỉ cuộc sống yên bình.")])

add("bullets", section="Mẫu câu 重点句型", title="3. 向来…… · 4. 严把……关", size=33,
    items=["## 向来: từ trước đến nay, xưa nay (= 从来、一向)",
           "当然，闲置交易并非没有门槛，信任，向来是闲置交易的命门。",
           "这位老师对学生向来一视同仁。",
           "老王处事向来坚毅、果敢，在原则问题上，他总是毫不含糊。",
           "## 严把……关: theo tiêu chuẩn đã định, kiểm tra nghiêm ngặt (giữ chặt cửa ải…)",
           "“无忧购”是一套由服务商提供回收、鉴定服务，平台严把质量关、客服关的全方位服务体系。",
           "这次选购材料一定要严把质量关，宁缺毋滥。",
           "市场负责人说他们按照规定严把进货关，对于活禽和禽类产品严格实行进货查验制度。"],
    say=[F(0, "Mẫu thứ ba: 向来, nghĩa là từ trước đến nay vẫn luôn như thế, giống 从来 và 一向. Thường đứng sau chủ ngữ, trước động từ hoặc tính từ."),
         F(1, "Ví dụ một, lấy từ bài khóa: 当然，闲置交易并非没有门槛，信任，向来是闲置交易的命门。 Lòng tin xưa nay vẫn là tử huyệt của giao dịch đồ cũ."),
         F(2, "Ví dụ hai: 这位老师对学生向来一视同仁。 Thầy giáo này xưa nay luôn đối xử công bằng với mọi học sinh. 一视同仁 là thành ngữ: nhìn ai cũng như nhau, nhất thị đồng nhân."),
         F(3, "Ví dụ ba: 老王处事向来坚毅、果敢，在原则问题上，他总是毫不含糊。 Ông Vương xưa nay làm việc kiên định, quả cảm; trong những vấn đề nguyên tắc, ông luôn dứt khoát rõ ràng. 毫不含糊 là không chút mập mờ."),
         F(4, "Mẫu thứ tư: 严把关. Chữ 关 vốn là cửa ải; 把关 là canh giữ cửa ải, nghĩa bóng là kiểm tra theo tiêu chuẩn. 严把质量关 là kiểm soát chặt chẽ chất lượng. Ở giữa có thể chèn 质量，进货，入口，招生, v.v."),
         F(5, "Ví dụ một, lấy từ bài khóa: 无忧购是一套由服务商提供回收、鉴定服务，平台严把质量关、客服关的全方位服务体系。 Nền tảng kiểm soát chặt khâu chất lượng và khâu chăm sóc khách hàng."),
         F(6, "Ví dụ hai: 这次选购材料一定要严把质量关，宁缺毋滥。 Lần chọn mua vật liệu này nhất định phải kiểm soát chặt chất lượng, thà thiếu chứ không lấy bừa. 宁缺毋滥 là thà thiếu còn hơn lạm, chữ đầu đọc là nìng."),
         F(7, "Ví dụ ba: 市场负责人说他们按照规定严把进货关，对于活禽和禽类产品严格实行进货查验制度。 Người phụ trách chợ nói họ làm đúng quy định, kiểm soát chặt khâu nhập hàng, áp dụng nghiêm chế độ kiểm tra khi nhập gia cầm sống và sản phẩm gia cầm.")])

add("bullets", chapter="Mẫu câu: 换言之 · 一连", section="Mẫu câu 重点句型", title="5. 换言之，…… · 6. 一连……", size=33,
    items=["## 换言之: nói cách khác (= 换句话说), văn viết; đứng đầu vế sau, diễn đạt lại rõ hơn",
           "……平台严把质量关、客服关的全方位服务体系。换言之，用户既要一个自由的市场，更要一个规范的市场……",
           "旅馆出售的是服务而不是产品，换言之，服务就是旅馆的产品。",
           "沉默是金，换言之，谨言慎行总是没错的。",
           "## 一连 + động từ / số lượng: liên tiếp, liền một mạch (nhấn mạnh nhiều, lâu)",
           "这几年来，国内循环经济发展，一连出台了多项政策措施。",
           "南京进入了梅雨季节，一连下了十几天的雨。",
           "我最近课业压力特别大，一连三天都失眠。"],
    say=[F(0, "Mẫu thứ năm: 换言之, nghĩa là nói cách khác, giống 换句话说 nhưng trang trọng hơn. Nó đứng đầu vế sau, diễn đạt lại ý vế trước một cách rõ ràng, cụ thể hoặc khái quát hơn."),
         F(1, "Ví dụ một, lấy từ bài khóa: sau khi giới thiệu dịch vụ Mua không lo, tác giả viết: 换言之，用户既要一个自由的市场，更要一个规范的市场，不仅要平台来撮合交易，更要平台来担保交易。 Câu sau giải thích lại câu trước theo góc nhìn của người dùng."),
         F(2, "Ví dụ hai: 旅馆出售的是服务而不是产品，换言之，服务就是旅馆的产品。 Khách sạn bán dịch vụ chứ không bán sản phẩm, nói cách khác, dịch vụ chính là sản phẩm của khách sạn."),
         F(3, "Ví dụ ba: 沉默是金，换言之，谨言慎行总是没错的。 Im lặng là vàng, nói cách khác, cẩn trọng lời nói việc làm thì không bao giờ sai."),
         F(4, "Mẫu thứ sáu: 一连, nghĩa là liên tiếp, liền một mạch. Sau 一连 là động từ hoặc cụm số lượng, nhấn mạnh số lượng nhiều hoặc thời gian dài. Khác với 一直, sau 一连 thường có con số cụ thể: 一连三天, 一连五次."),
         F(5, "Ví dụ một, lấy từ bài khóa: 这几年来，国内循环经济发展，一连出台了多项政策措施。 Mấy năm nay nhà nước liên tiếp ban hành nhiều chính sách."),
         F(6, "Ví dụ hai: 南京进入了梅雨季节，一连下了十几天的雨。 Nam Kinh bước vào mùa mưa dầm, mưa liền mười mấy ngày. 梅雨 là mưa mùa mận chín, mùa mưa dầm đầu hè ở miền nam Trung Quốc."),
         F(7, "Ví dụ ba: 我最近课业压力特别大，一连三天都失眠。 Dạo này áp lực học hành của tôi rất lớn, mất ngủ liền ba đêm.")])

add("bullets", section="Mẫu câu 重点句型", title="Luyện tập: điền 尚属 · 趋于 · 向来 · 严把 · 换言之 · 一连", reveal=True, size=34,
    items=["(1) 他___准时，今天怎么迟到了？",
           "Đáp án: 向来",
           "(2) 经过治疗，病人的情况已___稳定。",
           "Đáp án: 趋于",
           "(3) 用无人机送快递，这在我们县___首次。",
           "Đáp án: 尚属",
           "(4) 他___给她打了五个电话，她都没接。",
           "Đáp án: 一连",
           "(5) 学校招生一定要___入口关。",
           "Đáp án: 严把",
           "(6) 他从来不说谎，___，他是个诚实的人。",
           "Đáp án: 换言之"],
    say=["Bây giờ chúng ta luyện tập nhanh sáu mẫu câu vừa học. Thầy đọc câu, các bạn tạm dừng chọn từ, rồi nghe đáp án nhé.",
         F(0, "Câu một: 他什么准时，今天怎么迟到了？ Anh ấy xưa nay luôn đúng giờ, sao hôm nay lại đến muộn?"),
         F(1, "Đáp án: 向来. 他向来准时. Từ chỉ thói quen từ trước tới nay."),
         F(2, "Câu hai: 经过治疗，病人的情况已什么稳定。 Sau khi điều trị, tình trạng bệnh nhân đã dần ổn định."),
         F(3, "Đáp án: 趋于. 趋于稳定, sau 趋于 là tính từ hai âm tiết."),
         F(4, "Câu ba: 用无人机送快递，这在我们县什么首次。 Dùng máy bay không người lái giao hàng, ở huyện chúng tôi vẫn là lần đầu."),
         F(5, "Đáp án: 尚属. 尚属首次, cụm cố định."),
         F(6, "Câu bốn: 他什么给她打了五个电话，她都没接。 Anh ấy gọi cho cô ấy liền năm cuộc, cô ấy đều không nghe máy."),
         F(7, "Đáp án: 一连. Sau 一连 là cụm số lượng 五个电话."),
         F(8, "Câu năm: 学校招生一定要什么入口关。 Nhà trường tuyển sinh nhất định phải kiểm soát chặt khâu đầu vào."),
         F(9, "Đáp án: 严把. 严把入口关, theo mẫu 严把关."),
         F(10, "Câu sáu: 他从来不说谎，什么，他是个诚实的人。 Anh ấy chưa bao giờ nói dối, nói cách khác, anh ấy là người trung thực."),
         F(11, "Đáp án: 换言之. Vế sau khái quát lại vế trước.")])

# ======================= KẾT HỢP TỪ & THÀNH NGỮ =======================
add("bullets", chapter="Kết hợp từ & thành ngữ", section="Kết hợp từ 词语搭配", title="Kết hợp từ: 超乎 · 放眼 · 缔造", size=32,
    items=["## 超乎 vượt quá: ～想象 · ～寻常 · ～预期 · ～意料",
           "……造成国内闲置产品规模巨大，由此带来的浪费超乎想象。",
           "他从小到大都在森林里待着，所以对大自然有着超乎寻常的亲近感。",
           "## 放眼 phóng tầm mắt: ～未来 · ～世界 · ～四周",
           "放眼未来，华语电影一定会在世界电影领域占领一席之地。 · 现代人就是要放眼世界，不能闭关自守，坐井观天。",
           "## 缔造 tạo dựng: ～者 · ～传奇 · ～国家 · ～伟业",
           "经过不懈的努力，中国乒乓球队缔造了一个又一个的传奇。 · 历史是人民缔造的。"],
    say=["Tiếp theo là phần kết hợp từ, 词语搭配. Bài này có ba từ trọng điểm.",
         F(0, "Từ thứ nhất: 超乎, nghĩa là vượt ra ngoài. Hay đi với 想象，寻常，预期，意料: 超乎想象, vượt ngoài tưởng tượng; 超乎寻常, khác thường; 超乎预期, vượt mong đợi; 超乎意料, ngoài dự liệu."),
         F(1, "Ví dụ lấy từ bài khóa: 造成国内闲置产品规模巨大，由此带来的浪费超乎想象。 Sự lãng phí do đó gây ra vượt xa sức tưởng tượng."),
         F(2, "Ví dụ khác: 他从小到大都在森林里待着，所以对大自然有着超乎寻常的亲近感。 Anh ấy từ nhỏ đến lớn sống trong rừng, nên có sự gần gũi khác thường với thiên nhiên. Sách còn có câu: 结果往往是超乎预期的, kết quả thường vượt ngoài mong đợi."),
         F(3, "Từ thứ hai: 放眼, phóng tầm mắt. Hay đi với 未来，世界，四周: 放眼未来, nhìn về tương lai; 放眼世界, nhìn ra thế giới; 放眼四周, nhìn quanh bốn phía. Trong bài: 放眼邻国日本."),
         F(4, "Ví dụ: 放眼未来，华语电影一定会在世界电影领域占领一席之地。 Nhìn về tương lai, điện ảnh Hoa ngữ nhất định sẽ chiếm được một chỗ đứng trong làng điện ảnh thế giới. Và: 现代人就是要放眼世界，不能闭关自守，坐井观天。 Người hiện đại phải nhìn ra thế giới, không thể đóng cửa tự thủ, ếch ngồi đáy giếng. 坐井观天 chính là ếch ngồi đáy giếng của tiếng Việt."),
         F(5, "Từ thứ ba: 缔造, tạo dựng. Hay đi với 者，传奇，国家，伟业: 缔造者, người sáng lập; 缔造传奇, làm nên huyền thoại; 缔造国家, dựng nước; 缔造伟业, dựng nên nghiệp lớn. Trong bài: 缔造信任空间是多方面的."),
         F(6, "Ví dụ: 经过不懈的努力，中国乒乓球队缔造了一个又一个的传奇。 Sau những nỗ lực không ngừng, đội bóng bàn Trung Quốc đã làm nên hết huyền thoại này đến huyền thoại khác. Và: 历史是人民缔造的。 Lịch sử là do nhân dân tạo nên.")])

add("bullets", section="Thành ngữ 成语和惯用语", title="Thành ngữ (1): 何去何从 · 囊中羞涩 · 显而易见", size=32,
    items=["## 何去何从 héqù-hécóng: đi đâu theo đâu – chọn hướng nào trong việc hệ trọng",
           "旧手机何去何从，是一个问题。 · 现在是人生的重要关头，何去何从，你要考虑清楚。",
           "## 囊中羞涩 nángzhōng-xiūsè: túi tiền eo hẹp (cách nói khéo của “không có tiền”)",
           "这给那些爱宜家但囊中羞涩的人一种新的选择。 · 她看中了一件漂亮衣服，可是囊中羞涩，买不起。",
           "## 显而易见 xiǎn'éryìjiàn: rõ ràng, dễ thấy",
           "……公众消费理念的变迁显而易见。 · 这道理显而易见，谁都能看明白。"],
    say=["Bây giờ là phần thành ngữ và quán ngữ, 成语和惯用语. Bài có sáu cụm, thầy chia thành hai slide.",
         F(0, "Thành ngữ thứ nhất: 何去何从. 何 là đâu, gì; 去 là rời đi, 从 là đi theo. Đi đâu, theo đâu: chỉ việc phải lựa chọn phương hướng trong một vấn đề hệ trọng, nhiều khi là còn lưỡng lự chưa quyết."),
         F(1, "Ví dụ trong bài: 旧手机何去何从，是一个问题。 Điện thoại cũ đi đâu về đâu là một vấn đề. Ví dụ khác: 现在是人生的重要关头，何去何从，你要考虑清楚。 Bây giờ là bước ngoặt quan trọng của đời người, đi theo hướng nào, cậu phải suy nghĩ cho kỹ."),
         F(2, "Thành ngữ thứ hai: 囊中羞涩. 囊 là cái túi, 羞涩 là ngượng ngùng: cái túi thấy ngượng vì trống rỗng. Đây là cách nói khéo, nói giảm của việc không có tiền, túi tiền eo hẹp."),
         F(3, "Ví dụ trong bài: 这给那些爱宜家但囊中羞涩的人一种新的选择。 Ví dụ khác: 她看中了一件漂亮衣服，可是囊中羞涩，买不起。 Cô ấy ưng một bộ quần áo đẹp, nhưng túi tiền eo hẹp, không mua nổi."),
         F(4, "Thành ngữ thứ ba: 显而易见, rõ ràng và dễ thấy. 显 là hiển hiện, 易 là dễ: sự việc hay đạo lý rất rõ ràng, ai cũng nhìn ra."),
         F(5, "Ví dụ trong bài: 公众消费理念的变迁显而易见。 Ví dụ khác: 这道理显而易见，谁都能看明白。 Đạo lý này rõ như ban ngày, ai cũng hiểu. Chú ý: chữ 而 ở giữa đọc là ér, nối hai tính từ.")])

add("bullets", section="Thành ngữ 成语和惯用语", title="Thành ngữ (2): 喜新厌旧 · 铁了心 · 有案可稽", size=32,
    items=["## 喜新厌旧 xǐxīn-yànjiù: thích mới chán cũ, có mới nới cũ",
           "而“喜新厌旧”造就了闲置物品的庞大市场…… · 有人喜新厌旧，还美其名曰：旧的不去，新的不来。",
           "## 铁了心 tiělexīn: đã quyết tâm sắt đá, không đổi ý",
           "……看来是铁了心要治理平台问题…… · 日子实在过不下去了，她铁了心要跟自己的丈夫离婚。",
           "## 有案可稽 yǒu'ànkějī: có hồ sơ để tra – chứng cứ xác thực, khó chối cãi",
           "……物品可追溯性大大提升，做到有案可稽。 · 白纸黑字，有案可稽，你怎么还能睁着眼睛说瞎话呢？"],
    say=[F(0, "Thành ngữ thứ tư: 喜新厌旧, thích cái mới, chán cái cũ, giống hệt câu có mới nới cũ của tiếng Việt. Có thể nói về đồ vật, cũng có thể chê người thay lòng đổi dạ trong tình cảm."),
         F(1, "Ví dụ trong bài: 而喜新厌旧造就了闲置物品的庞大市场。 Ví dụ khác: 有人喜新厌旧，还美其名曰：旧的不去，新的不来。 Có người có mới nới cũ, lại còn nói cho đẹp rằng: cái cũ không đi, cái mới không đến. 美其名曰 là gọi bằng một cái tên đẹp đẽ, mang ý mỉa mai."),
         F(2, "Quán ngữ thứ năm: 铁了心, nghĩa đen là trái tim đã hóa sắt, tức là đã hạ quyết tâm, không thay đổi ý định. Phía sau thường là 要 cộng động từ: 铁了心要……."),
         F(3, "Ví dụ trong bài: 看来是铁了心要治理平台问题. Ví dụ khác: 日子实在过不下去了，她铁了心要跟自己的丈夫离婚。 Cuộc sống thật sự không thể chịu nổi nữa, cô ấy đã quyết tâm ly hôn với chồng. Sách còn có câu: 他铁了心要在中国发展, anh ấy quyết tâm phát triển sự nghiệp ở Trung Quốc."),
         F(4, "Thành ngữ thứ sáu: 有案可稽. 案 là hồ sơ, văn bản; 稽 đọc là jī, nghĩa là tra xét. Có hồ sơ để tra cứu, tức là chứng cứ xác thực, khó mà chối cãi."),
         F(5, "Ví dụ trong bài: 物品可追溯性大大提升，做到有案可稽。 Ví dụ khác: 白纸黑字，有案可稽，你怎么还能睁着眼睛说瞎话呢？ Giấy trắng mực đen, có hồ sơ rành rành, sao anh còn có thể trợn mắt nói dối được? 睁着眼睛说瞎话 là mở mắt nói điều mù quáng, tức là nói dối trắng trợn.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 课后练习", title="Bài tập 1: Chọn từ điền vào chỗ trống", reveal=True, size=32,
    items=["## Từ cho sẵn: 变迁 · 放眼 · 何去何从 · 显而易见 · 换言之",
           "(1) 亚洲国家对双边协定的热情是___的，他们有理由支持亚洲内部的贸易。",
           "Đáp án: 显而易见",
           "(2) 哲学的乐趣并不在于知识，而在于思索，___，哲学就是让人们习惯于思考。",
           "Đáp án: 换言之",
           "(3) 不管岁月如何___，这块巨石依然坚强地矗立在那里。",
           "Đáp án: 变迁",
           "(4) 没有梦想的人，就像是飘散在天空中的蒲公英，不知___。",
           "Đáp án: 何去何从",
           "(5) 各高等院校应___未来，在现代教育技术方面加大投入。",
           "Đáp án: 放眼"],
    say=["Phần luyện tập của sách mang tên 趁热打铁, rèn sắt khi còn nóng. Bài tập một: chọn từ điền vào chỗ trống. Có năm từ: 变迁，放眼，何去何从，显而易见，换言之.",
         F(1, "Câu một: 亚洲国家对双边协定的热情是什么的，他们有理由支持亚洲内部的贸易。 Sự nhiệt tình của các nước châu Á đối với hiệp định song phương là điều thế nào? Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 显而易见. 热情是显而易见的, sự nhiệt tình là điều ai cũng thấy rõ. Cấu trúc 是……的 rất hay đi với 显而易见."),
         F(3, "Câu hai: 哲学的乐趣并不在于知识，而在于思索，什么，哲学就是让人们习惯于思考。 Niềm vui của triết học không nằm ở tri thức, mà ở sự suy ngẫm."),
         F(4, "Đáp án: 换言之. Vế sau diễn đạt lại vế trước: nói cách khác, triết học là giúp con người quen với việc suy nghĩ."),
         F(5, "Câu ba: 不管岁月如何什么，这块巨石依然坚强地矗立在那里。 Dù năm tháng đổi thay thế nào, tảng đá lớn này vẫn sừng sững ở đó."),
         F(6, "Đáp án: 变迁. 岁月变迁, năm tháng đổi thay, sự thay đổi qua thời gian dài."),
         F(7, "Câu bốn: 没有梦想的人，就像是飘散在天空中的蒲公英，不知什么。 Người không có ước mơ giống như hạt bồ công anh bay tản mác trên trời, không biết đi đâu về đâu."),
         F(8, "Đáp án: 何去何从. 不知何去何从, không biết nên đi đâu về đâu."),
         F(9, "Câu năm: 各高等院校应什么未来，在现代教育技术方面加大投入。 Các trường đại học nên nhìn về tương lai, tăng cường đầu tư vào công nghệ giáo dục hiện đại."),
         F(10, "Đáp án: 放眼. 放眼未来, đúng như kết hợp từ vừa học.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn đáp án đúng", reveal=True, size=33,
    items=["(1) 如果你（  ）强求一些东西，往往不能达到预期的目的。 A.刻意 B.故意 C.专门 D.特意",
           "Đáp án: A 刻意 – cố công, cố ép cho bằng được (故意 thường là cố ý làm điều xấu)",
           "(2) 人的一生应该多出去走一走……感受不同的文化风情，（  ）自己的视野。 A.展开 B.广阔 C.扩大 D.拓展",
           "Đáp án: D 拓展 – 拓展视野 mở rộng tầm nhìn (广阔 là tính từ; 展开 là triển khai, mở ra)",
           "(3) 他感冒了，（  ）几天没来上课。 A.一连 B.一直 C.不停 D.不断",
           "Đáp án: A 一连 – sau 一连 có cụm số lượng 几天",
           "(4) 为了长江水利工程的建设，三峡库区的居民进行了史无前例的大（  ）。 A.变化 B.变迁 C.迁移 D.变动",
           "Đáp án: C 迁移 – di dời chỗ ở (变迁 là đổi thay theo thời gian)"],
    say=["Bài tập hai: chọn đáp án đúng. Bài này giúp phân biệt các từ gần nghĩa.",
         F(0, "Câu một: 如果你什么强求一些东西，往往不能达到预期的目的。 Nếu bạn cố ép cho bằng được một số thứ, thường sẽ không đạt được mục đích mong muốn. Bốn lựa chọn: 刻意，故意，专门，特意."),
         F(1, "Đáp án: A, 刻意. 刻意强求 là cố công ép buộc. 故意 thường là cố tình làm điều không tốt, như 故意捣乱; 专门 và 特意 là chuyên để, cốt để làm một việc, không đi với 强求."),
         F(2, "Câu hai: 人的一生应该多出去走一走，看一看，感受不同的文化风情，什么自己的视野。 Đời người nên đi đây đi đó nhiều, cảm nhận những phong tục văn hóa khác nhau, để làm gì với tầm nhìn của mình. Bốn lựa chọn: 展开，广阔，扩大，拓展."),
         F(3, "Đáp án: D, 拓展, từ mới của bài: 拓展视野, mở rộng tầm nhìn. 广阔 là tính từ, rộng lớn, không mang tân ngữ; 展开 là mở ra, triển khai, như 展开讨论. 扩大视野 cũng có người nói, nhưng 拓展 là đáp án sách muốn luyện."),
         F(4, "Câu ba: 他感冒了，什么几天没来上课。 Anh ấy bị cảm, mấy ngày liền không đến lớp. Bốn lựa chọn: 一连，一直，不停，不断."),
         F(5, "Đáp án: A, 一连. Phía sau có cụm số lượng 几天, nên dùng 一连. 一直 không đi trực tiếp với số lượng; 不停 và 不断 chỉ hành động không ngừng, không hợp với 没来上课."),
         F(6, "Câu bốn: 为了长江水利工程的建设，三峡库区的居民进行了史无前例的大什么。 Để xây dựng công trình thủy lợi trên sông Trường Giang, cư dân vùng lòng hồ Tam Hiệp đã tiến hành một cuộc đại gì đó chưa từng có trong lịch sử. Bốn lựa chọn: 变化，变迁，迁移，变动."),
         F(7, "Đáp án: C, 迁移, di dời chỗ ở. Hơn một triệu người dân đã phải chuyển nhà để nhường chỗ cho đập Tam Hiệp. Chú ý: 变迁 trông giống nhưng nghĩa là đổi thay theo thời gian, như 时代变迁, không phải chuyển chỗ ở.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ ngữ, mẫu câu cho sẵn trả lời câu hỏi", reveal=True, size=31,
    items=["(1) 什么是“无忧购”？（换言之）",
           "Đáp án gợi ý: “无忧购”是闲鱼推出的一套由服务商提供回收、鉴定服务，平台严把质量关、客服关的全方位服务体系。换言之，平台不仅撮合交易，还担保交易。",
           "(2) 中国的共享经济在怎样的过程中形成了什么样的共识？（趋于）",
           "Đáp án gợi ý: 在共享经济从涨潮、退潮再到趋于理性的过程中，全社会形成了一种共识：共享的本质不是刻意创造闲置，而是合理消化闲置。",
           "(3) 闲置交易的门槛是什么？（向来）",
           "Đáp án gợi ý: 闲置交易的门槛是信任，信任向来是闲置交易的命门。",
           "(4) 从旧手机里提炼真金做奖牌是什么样的举措？（尚属）",
           "Đáp án gợi ý: 这是日本为迎接东京奥运会采取的环保举措，从旧手机里提炼真金做奖牌，这在奥运史上尚属首次。"],
    say=["Bài tập ba: dùng từ ngữ và mẫu câu cho sẵn để trả lời câu hỏi về bài khóa. Đây là câu hỏi mở, thầy đưa ra đáp án gợi ý.",
         F(0, "Câu một: 什么是无忧购？ Mua không lo là gì? Dùng 换言之."),
         F(1, "Gợi ý: 无忧购是闲鱼推出的一套由服务商提供回收、鉴定服务，平台严把质量关、客服关的全方位服务体系。换言之，平台不仅撮合交易，还担保交易。 Mua không lo là hệ thống dịch vụ toàn diện của Xianyu; nói cách khác, nền tảng không chỉ kết nối mà còn bảo đảm giao dịch."),
         F(2, "Câu hai: 中国的共享经济在怎样的过程中形成了什么样的共识？ Kinh tế chia sẻ Trung Quốc đã hình thành nhận thức chung nào, trong quá trình ra sao? Dùng 趋于."),
         F(3, "Gợi ý: 在共享经济从涨潮、退潮再到趋于理性的过程中，全社会形成了一种共识：共享的本质不是刻意创造闲置，而是合理消化闲置。"),
         F(4, "Câu ba: 闲置交易的门槛是什么？ Rào cản của giao dịch đồ cũ là gì? Dùng 向来."),
         F(5, "Gợi ý: 闲置交易的门槛是信任，信任向来是闲置交易的命门。 Rào cản là lòng tin, lòng tin xưa nay là tử huyệt của giao dịch đồ cũ."),
         F(6, "Câu bốn: 从旧手机里提炼真金做奖牌是什么样的举措？ Chiết xuất vàng từ điện thoại cũ làm huy chương là một biện pháp như thế nào? Dùng 尚属. 举措 là biện pháp, động thái."),
         F(7, "Gợi ý: 这是日本为迎接东京奥运会采取的环保举措，从旧手机里提炼真金做奖牌，这在奥运史上尚属首次。 Đây là biện pháp bảo vệ môi trường Nhật Bản áp dụng để đón Olympic Tokyo, và là lần đầu tiên trong lịch sử Olympic.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Chọn từ điền vào đoạn văn", reveal=True, size=32,
    items=["## Từ cho sẵn: 匮乏 · 盲盒 · 显而易见 · 囤 · 廉价 · 换言之",
           "改革开放四十多年来，从当初物质的极度___到如今商品的极大丰富，公众消费理念的变迁___。“汝之闲置，彼之珍藏”，___，同样的东西，你视为垃圾，别人可能视为宝贝。Z世代买二手球鞋、___，旧物成了宝贝；白领阶层买___婴儿床，转卖___多了的纸尿裤；二手母婴产品、二手车、二手手机都是千亿元以上的市场。",
           "Đáp án: 匮乏 · 显而易见 · 换言之 · 盲盒 · 廉价 · 囤"],
    say=["Bài tập bốn: chọn từ điền vào đoạn văn. Có sáu từ: 匮乏，盲盒，显而易见，囤，廉价，换言之.",
         F(1, "改革开放四十多年来，从当初物质的极度什么到如今商品的极大丰富，公众消费理念的变迁什么。汝之闲置，彼之珍藏，什么，同样的东西，你视为垃圾，别人可能视为宝贝。Z世代买二手球鞋、什么，旧物成了宝贝；白领阶层买什么婴儿床，转卖什么多了的纸尿裤。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 极度匮乏；变迁显而易见；换言之；二手球鞋、盲盒；廉价婴儿床；转卖囤多了的纸尿裤。"),
         F(2, "Đoạn văn này gần như chính là đoạn sáu và đoạn bảy của bài khóa, chỉ thêm một câu văn ngôn: 汝之闲置，彼之珍藏. 汝 là anh, bạn; 彼 là người kia: đồ để không của bạn là báu vật của người khác. Vế sau giải thích lại câu văn ngôn ấy bằng tiếng hiện đại, nên đặt 换言之 vào giữa là rất hợp.")])

# ======================= LIÊN HỆ =======================
add("bullets", chapter="Liên hệ: chợ đồ cũ ở Việt Nam", section="Thảo luận 讨论", title="Liên hệ Việt Nam: “pass đồ” và kinh tế đồ cũ", size=33,
    items=["“Pass đồ” = 转卖闲置 · “thanh lý” = 清仓/出闲置 · Chợ Tốt, hội nhóm Facebook ≈ 闲鱼、转转",
           "Đồ “si” (quần áo second-hand nhập khẩu) ≈ 二手衣服 · thu cũ đổi mới ≈ 以旧换新",
           "Ngại mua đồ cũ vì sợ hàng giả, hàng lỗi → đúng như bài khóa: 信任是打开闲置交易的钥匙",
           "汝之闲置，彼之珍藏 · 物品的使用比占有更具价值",
           "Câu hỏi: 你愿意买二手货吗？为什么？"],
    say=["Trước khi tổng kết, chúng ta cùng liên hệ với Việt Nam.",
         F(0, "Giới trẻ Việt Nam hay nói pass đồ, chính là 转卖闲置 trong bài; còn thanh lý đồ cũng gần với 出闲置. Chợ Tốt và các hội nhóm pass đồ trên Facebook đóng vai trò giống 闲鱼 và 转转 ở Trung Quốc."),
         F(1, "Quần áo si, tức là quần áo second-hand nhập từ Nhật, Hàn, rất được các bạn trẻ yêu thích, vừa rẻ vừa độc. Còn các chuỗi điện thoại thì có chương trình thu cũ đổi mới, chính là 以旧换新."),
         F(2, "Nhưng nhiều người vẫn ngại mua đồ cũ trên mạng vì sợ hàng giả, hàng lỗi, sợ bị lừa chuyển khoản. Điều này đúng như bài khóa nói: lòng tin là chìa khóa mở ra giao dịch đồ cũ."),
         F(3, "Hãy nhớ hai câu đẹp của bài: 汝之闲置，彼之珍藏, đồ để không của bạn là báu vật của người khác; và 物品的使用比占有更具价值, dùng có giá trị hơn sở hữu."),
         F(4, "Câu hỏi cho các bạn: 你愿意买二手货吗？为什么？ Bạn có sẵn lòng mua đồ cũ không? Vì sao? Câu mẫu: 我愿意买二手货，因为价格实惠，也比较环保；不过我只在信得过的平台上买。 Tôi sẵn lòng mua đồ cũ vì giá phải chăng, lại thân thiện với môi trường; nhưng tôi chỉ mua trên nền tảng đáng tin cậy. Các bạn hãy tạm dừng và tự trả lời bằng tiếng Trung nhé.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 7.1", size=33,
    items=["Từ vựng trọng tâm: 闲置 · 风尚 · 提炼 · 视角 · 挖掘 · 转卖 · 变迁 · 囤 · 寿命 · 趋于 · 刻意 · 命门 · 撮合 · 拓展 · 缔造 · 坍塌 · 追溯 · 庆幸",
           "Từ lóng mạng: 吃土 · 回血 · 剁手",
           "Mẫu câu: 尚属 · 趋于 · 向来 · 严把……关 · 换言之 · 一连",
           "Kết hợp từ: 超乎想象 · 放眼世界 · 缔造传奇 · Thành ngữ: 何去何从 · 囊中羞涩 · 显而易见 · 喜新厌旧 · 铁了心 · 有案可稽",
           "## Bài tập về nhà",
           "Viết đoạn văn khoảng 300 chữ: 二手货，你愿意买单吗？ (dùng ít nhất 3 mẫu câu của bài)"],
    say=["Chúng ta cùng tổng kết bài bảy chấm một.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 闲置，风尚，提炼，视角，挖掘，转卖，变迁，囤，寿命，趋于，刻意，命门，撮合，拓展，缔造，坍塌，追溯，庆幸. Nhớ những từ dễ nhầm như 视角, 追溯, và đơn vị 亩 nhé."),
         F(1, "Ba từ lóng mạng: 吃土, cháy túi; 回血, gỡ lại tiền; 剁手, nghiện mua sắm online."),
         F(2, "Về mẫu câu: 尚属 là vẫn còn là, hay gặp 尚属首次; 趋于 là dần hướng tới, cộng tính từ hai âm tiết; 向来 là xưa nay; 严把关 là kiểm soát chặt một khâu; 换言之 là nói cách khác; và 一连 là liên tiếp, thường cộng số lượng."),
         F(3, "Về kết hợp từ và thành ngữ: 超乎想象，放眼世界，缔造传奇; 何去何从，囊中羞涩，显而易见，喜新厌旧，铁了心, và 有案可稽."),
         F(5, "Bài tập về nhà: hãy viết một đoạn văn khoảng ba trăm chữ với đề 二手货，你愿意买单吗？ Đồ cũ, bạn có sẵn lòng xuống tiền không? Đây cũng là một đề trong phần ôn tập đơn vị của sách. Hãy dùng ít nhất ba mẫu câu của bài, như 向来，换言之，趋于."),
         {"t": "Cảm ơn các bạn đã theo dõi bài giảng. Bài sau, bài bảy chấm hai, có tên 天下没有永远免费的午餐, Trên đời không có bữa trưa nào miễn phí mãi. Chúng ta sẽ bàn về chuyện năm hào tiền phí gửi đồ ở tủ nhận hàng Phong Sào, và vì sao thời đại internet miễn phí đã đến hồi kết thúc. Hẹn gặp lại các bạn. Chúc các bạn học tốt!",
          "cap": "Cảm ơn các bạn đã theo dõi bài giảng. Bài sau, bài 7.2: 天下没有永远免费的午餐, Trên đời không có bữa trưa nào miễn phí mãi. Hẹn gặp lại các bạn. Chúc các bạn học tốt!"}])

lesson = {
    "title": "顶石中文 – Bài 7.1: 闲置经济是真正的共享经济 (Kinh tế đồ cũ mới là kinh tế chia sẻ thực sự)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"囤": "屯",                  # tún
                    "都科摩": "督科摩",          # Dūkēmó (Docomo)
                    "视角": "视脚",              # shìjiǎo
                    "视为": "视维",              # shìwéi
                    "长远": "常远",              # chángyuǎn
                    "增长": "增涨",              # zēngzhǎng
                    "调查": "掉查",              # diàochá
                    "强求": "抢求",              # qiǎngqiú
                    "宁缺": "佞缺",              # nìngquē
                    "处事": "楚事",              # chǔshì
                    "处理": "楚理",              # chǔlǐ
                    "说白了": "说白啦",          # shuōbái le
                    "铁了心": "铁啦心",          # tiě le xīn
                    "有案可稽": "有案可机",      # yǒu'àn kě jī
                    "撮合": "搓合",              # cuōhe
                    "拓展": "唾展",              # tuòzhǎn
                    "露": "露"},
    "slides": slides,
}
lesson["tts_replace"].pop("露")
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds71.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
