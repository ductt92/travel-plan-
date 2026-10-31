#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Thượng) – Bài 10 «全球化视野中的中国饮食». Chạy để sinh bai10.json."""
import json
import os

TAG = "HSK 6 (Thượng) · Bài 10 · 全球化视野中的中国饮食"
slides = []


def add(type_, chapter=None, section="", **kw):
    s = {"type": type_, "section": section, **kw}
    if chapter:
        s["chapter"] = chapter
    slides.append(s)


def F(i, t, **kw):
    return {"t": t, "f": i, **kw}


# ======================= MỞ ĐẦU =======================
# Tên bài có 11 chữ, vừa khít một dòng chữ cỡ lớn (170px) nên giữ nguyên.
add("title", chapter="Mở đầu",
    top="Giáo trình chuẩn HSK 6 – Quyển Thượng",
    zh="全球化视野中的中国饮食", py="Quánqiúhuà shìyě zhōng de Zhōngguó yǐnshí",
    vi="Bài 10: Thức ăn Trung Quốc trong xu thế toàn cầu hóa",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Thượng.",
         "Hôm nay chúng ta học bài mười: 全球化视野中的中国饮食。 Nghĩa là: Thức ăn Trung Quốc trong xu thế toàn cầu hóa, hay nói sát hơn là: ẩm thực Trung Quốc dưới tầm nhìn toàn cầu hóa.",
         "Bài này thuộc Chủ đề ba, 多彩社会, Xã hội muôn màu. Khác với những câu chuyện kể ở các bài trước, bài khóa hôm nay là một bài văn nghị luận. Tác giả giải thích vì sao văn hóa ẩm thực Trung Quốc trải qua mấy nghìn năm mà vẫn hấp dẫn: vì nó luôn biết tiếp thu cái hay của thế giới, từ nguyên liệu, cách chế biến cho đến cách ngồi ăn.",
         "Người Việt chúng ta cũng có một nền ẩm thực rất phong phú, nên trong lúc học, các bạn hãy thử so sánh với món ăn quê mình nhé."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài khóa: vì sao ẩm thực Trung Hoa luôn hấp dẫn và tràn đầy sức sống",
           "Nắm vững 51 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: liên từ 以至, liên từ 即便, danh từ 所在",
           "Phân biệt 凡是 và 所有",
           "Mở rộng: từ vựng về địa lý (地理)"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa: vì sao văn hóa ẩm thực Trung Hoa luôn hấp dẫn, và bí quyết nào khiến nó tràn đầy sức sống."),
         F(1, "Thứ hai, nắm vững năm mươi mốt từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học ba điểm ngữ pháp: liên từ 以至, nghĩa là đến nỗi, đến mức; liên từ 即便, nghĩa là cho dù; và danh từ 所在, nghĩa là chỗ, nơi tồn tại."),
         F(3, "Thứ tư, phân biệt hai từ rất dễ dùng lẫn: 凡是 và 所有."),
         F(4, "Thứ năm, phần mở rộng của sách: làm quen với một nhóm từ vựng về địa lý, như 盆地，沼泽，温带，省会."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Khởi động: Bạn có biết các loại thực phẩm này?", size=38,
    items=["柠檬 chanh · 蒜 tỏi · 鸡 gà · 葱 hành · 芒果 xoài · 鱼 cá · 西红柿 cà chua · 姜 gừng · 土豆 khoai tây",
           "水果 trái cây: 柠檬、芒果",
           "蔬菜 rau củ: 西红柿、土豆",
           "禽肉 thịt (gia cầm, cá): 鸡、鱼",
           "调料 gia vị: 葱、姜、蒜"],
    say=["Chúng ta bắt đầu bằng phần khởi động. Sách cho chín bức ảnh thực phẩm và hỏi: 下面各种食材你认识吗？ Bạn có nhận ra các loại nguyên liệu dưới đây không? Hãy chọn tên đúng cho từng ảnh, rồi xếp chúng vào các nhóm.",
         F(0, "Chín từ đó là: 柠檬, quả chanh. 蒜, tỏi. 鸡, con gà. 葱, hành lá. 芒果, quả xoài. 鱼, con cá. 西红柿, cà chua. 姜, gừng. Và 土豆, khoai tây."),
         F(1, "Bây giờ xếp nhóm. Nhóm 水果, trái cây, có 柠檬 và 芒果. Hai thứ này đều là trái cây từ nước ngoài vào Trung Quốc, lát nữa bài khóa sẽ nhắc đến."),
         F(2, "Nhóm 蔬菜, rau củ, có 西红柿 và 土豆. Cà chua đôi khi cũng được ăn như trái cây, nên nếu các bạn xếp nó vào nhóm trái cây thì cũng không sai."),
         F(3, "Nhóm 禽肉, thịt gia cầm và các loại thịt, có 鸡 và 鱼."),
         F(4, "Và nhóm 调料, gia vị, có 葱，姜，蒜, tức là hành, gừng, tỏi. Bài khóa nói rằng ba thứ gia vị này vào Trung Quốc từ rất lâu, đến mức nhiều người Trung Quốc tưởng chúng là nguyên liệu bản địa. Thú vị không nào?")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 食 và 明", size=38,
    items=["## 食 (thực): ăn, đồ ăn",
           "饮食 ẩm thực · 零食 đồ ăn vặt · 面食 đồ làm từ bột mì · 肉食 đồ mặn, thịt · 甜食 đồ ngọt · 素食 đồ chay",
           "进食 ăn uống · 食物 thức ăn · 食品 thực phẩm · 食堂 nhà ăn · 食用 dùng để ăn · 丰衣足食 cơm no áo ấm",
           "## 明 (minh): rõ ràng, sáng",
           "明确 rõ ràng · 明显 rõ rệt · 明白 hiểu rõ · 明明 rõ ràng là · 明知 biết rõ · 说明 giải thích · 证明 chứng minh",
           "表明 tỏ rõ · 指明 chỉ rõ · 查明 điều tra rõ · 问明 hỏi rõ · 简明 ngắn gọn rõ ràng · 鲜明 rõ nét"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo, rất có lợi cho người Việt vì hầu hết các chữ đều có âm Hán Việt quen thuộc.",
         F(0, "Nhóm thứ nhất là chữ thực, như trong 饮食, nghĩa là ăn, đồ ăn."),
         F(1, "饮食，零食，面食，肉食，甜食，素食。 Tức là: ẩm thực, đồ ăn vặt, đồ làm từ bột mì, đồ mặn, đồ ngọt, và đồ chay. Từ 饮食 và 素食 đều là từ mới của bài hôm nay."),
         F(2, "进食，食物，食品，食堂，食用，丰衣足食。 Tức là: ăn uống, thức ăn, thực phẩm, nhà ăn, dùng để ăn, và thành ngữ 丰衣足食, áo mặc đủ đầy, cơm ăn no đủ, giống cơm no áo ấm của tiếng Việt."),
         F(3, "Nhóm thứ hai là chữ minh, như trong 明白, nghĩa là rõ ràng, sáng sủa."),
         F(4, "明确，明显，明白，明明，明知，说明，证明。 Tức là: rõ ràng, rõ rệt, hiểu rõ, rõ ràng là, biết rõ, giải thích, và chứng minh."),
         F(5, "表明，指明，查明，问明，简明，鲜明。 Tức là: tỏ rõ, chỉ rõ, điều tra rõ, hỏi rõ, ngắn gọn rõ ràng, và rõ nét. Từ 鲜明 có trong bài khóa: 民族特性鲜明, đặc tính dân tộc rõ nét.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 系 và 品", size=38,
    items=["## 系 (hệ): hệ thống, dòng dõi",
           "父系 dòng cha · 母系 dòng mẹ · 体系 hệ thống · 派系 phe phái · 太阳系 hệ Mặt Trời",
           "水系 hệ thống sông ngòi · 星系 thiên hà · 系列 loạt, dãy · 系统 hệ thống",
           "## 品 (phẩm): vật phẩm, đồ vật",
           "食品 thực phẩm · 产品 sản phẩm · 药品 dược phẩm · 物品 vật phẩm · 奖品 phần thưởng · 礼品 quà tặng · 商品 hàng hóa",
           "甜品 đồ tráng miệng · 用品 đồ dùng · 纪念品 quà lưu niệm · 农产品 nông sản · 日用品 đồ dùng hằng ngày · 消费品 hàng tiêu dùng"],
    say=[F(0, "Nhóm thứ ba là chữ hệ, như trong 系统, nghĩa là hệ thống, hoặc dòng dõi, nhánh."),
         F(1, "父系，母系，体系，派系，太阳系。 Tức là: dòng cha, dòng mẹ, hệ thống, phe phái, và hệ Mặt Trời. Bài khóa có cụm 中华饮食体系, hệ thống ẩm thực Trung Hoa."),
         F(2, "水系，星系，系列，系统。 Tức là: hệ thống sông ngòi, thiên hà, loạt, và hệ thống."),
         F(3, "Nhóm cuối cùng là chữ phẩm, như trong 产品, nghĩa là vật phẩm, đồ vật."),
         F(4, "食品，产品，药品，物品，奖品，礼品，商品。 Tức là: thực phẩm, sản phẩm, dược phẩm, vật phẩm, phần thưởng, quà tặng, và hàng hóa."),
         F(5, "甜品，用品，纪念品，农产品，日用品，消费品。 Tức là: đồ tráng miệng, đồ dùng, quà lưu niệm, nông sản, đồ dùng hằng ngày, và hàng tiêu dùng. Từ mới 品种 trong bài cũng có chữ phẩm này."),
         "Các bạn thấy không, chỉ cần nắm nghĩa của một chữ gốc, ta có thể đoán được nghĩa của cả một nhóm từ. Hãy áp dụng cách này khi học từ mới nhé."])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng)
V = [
    ("视野", "shìyě", "thị dã", "danh từ", "tầm nhìn, tầm mắt", "站在山顶上，视野非常开阔。", "Đứng trên đỉnh núi, tầm nhìn vô cùng rộng mở.",
     "Danh từ. Nghĩa gốc là phạm vi mắt nhìn thấy được; nghĩa bóng là tầm nhìn, tầm hiểu biết. 开阔视野 là mở rộng tầm nhìn, còn 全球化视野 trong tên bài là tầm nhìn toàn cầu hóa."),
    ("饮食", "yǐnshí", "ẩm thực", "danh từ", "đồ ăn thức uống; ăn uống", "中国的饮食文化历史悠久。", "Văn hóa ẩm thực Trung Quốc có lịch sử lâu đời.",
     "Danh từ. Chữ đầu là uống, chữ sau là ăn, nên 饮食 là chuyện ăn uống, giống hệt ẩm thực trong tiếng Việt. Hay gặp: 饮食文化，饮食习惯."),
    ("蕴藏", "yùncáng", "uẩn tàng", "động từ", "chứa đựng, tiềm ẩn", "这片土地下蕴藏着丰富的石油。", "Dưới vùng đất này chứa đựng trữ lượng dầu mỏ phong phú.",
     "Động từ, nghĩa là chứa đựng bên trong, chưa lộ ra ngoài. Dùng cho tài nguyên, sức mạnh, tình cảm hay ý nghĩa, thường đi với 着: 蕴藏着. Âm tiết thứ hai đọc là cáng, thanh hai."),
    ("传达", "chuándá", "truyền đạt", "động từ", "truyền đạt, truyền tải", "这幅画传达了画家对家乡的思念。", "Bức tranh này truyền tải nỗi nhớ quê hương của họa sĩ.",
     "Động từ, nghĩa là truyền đạt, truyền tải một tin tức, một tư tưởng hay một tình cảm. Âm Hán Việt và nghĩa giống tiếng Việt."),
    ("鲜明", "xiānmíng", "tiên minh", "tính từ", "rõ ràng, rõ nét, nổi bật", "这两种观点形成了鲜明的对比。", "Hai quan điểm này tạo thành sự đối lập rõ nét.",
     "Tính từ, nghĩa là rõ ràng, rõ nét, khác biệt hẳn. Cẩn thận: chữ đầu thường gặp với nghĩa tươi, như 新鲜, nhưng 鲜明 không phải là tươi sáng, mà là rõ nét, nổi bật. Hay gặp: 特点鲜明，立场鲜明，鲜明的对比."),
    ("区域", "qūyù", "khu vực", "danh từ", "khu vực, vùng", "这个区域禁止停车。", "Khu vực này cấm đỗ xe.",
     "Danh từ, nghĩa là khu vực, vùng, giống hệt tiếng Việt. Trong bài có cụm 不同国家、不同区域、不同民族."),
    ("优异", "yōuyì", "ưu dị", "tính từ", "xuất sắc, nổi bật", "她以优异的成绩考上了北京大学。", "Cô ấy thi đỗ Đại học Bắc Kinh với thành tích xuất sắc.",
     "Tính từ, nghĩa là xuất sắc, vượt trội hẳn. Đừng hiểu chữ dị là kỳ dị: ở đây nó là khác hẳn người thường, theo hướng tốt. Trong bài, 优异之处 là những điểm ưu tú."),
    ("以至", "yǐzhì", "dĩ chí", "liên từ", "đến nỗi, đến mức; cho đến", "他太紧张了，以至说不出话来。", "Anh ấy căng thẳng quá, đến nỗi không nói nên lời.",
     "Liên từ, đứng đầu vế sau, nghĩa là đến nỗi, đến mức. Đây là điểm ngữ pháp thứ nhất của bài. Ngoài ra nó còn có nghĩa là cho đến, như 从小学以至大学, từ tiểu học cho đến đại học."),
    ("辉煌", "huīhuáng", "huy hoàng", "tính từ", "huy hoàng, rực rỡ", "中国古代曾经创造了辉煌的文化。", "Trung Quốc cổ đại từng tạo nên một nền văn hóa rực rỡ.",
     "Tính từ, nghĩa là huy hoàng, rực rỡ, thường nói về thành tựu, lịch sử, văn hóa. Âm Hán Việt và nghĩa giống tiếng Việt."),
    ("和谐", "héxié", "hòa hài", "tính từ", "hài hòa, hòa hợp", "我们家的气氛非常和谐。", "Bầu không khí gia đình tôi vô cùng hòa thuận.",
     "Tính từ, nghĩa là hài hòa, hòa hợp. Hán Việt là hòa hài, nhưng chữ hài ở đây là ăn khớp với nhau, chứ không phải hài hước. Hay gặp: 和谐社会，家庭和谐."),
    ("调和", "tiáohé", "điều hòa", "động từ", "điều hòa, dung hòa; pha trộn", "他在两个人之间调和矛盾。", "Anh ấy đứng giữa dung hòa mâu thuẫn của hai người.",
     "Động từ, nghĩa là phối hợp cho cân đối, làm dịu mâu thuẫn, hoặc pha trộn cho đều. Âm tiết đầu đọc là tiáo, thanh hai. Chú ý: cái máy điều hòa trong tiếng Trung lại là 空调."),
    ("辽阔", "liáokuò", "liêu khoát", "tính từ", "bao la, rộng lớn", "中国有辽阔的土地和丰富的物产。", "Trung Quốc có đất đai rộng lớn và sản vật phong phú.",
     "Tính từ, nghĩa là bao la, rộng lớn, thường tả đất đai, thảo nguyên, biển cả, bầu trời."),
    ("飞禽走兽", "fēiqín zǒushòu", "phi cầm tẩu thú", "thành ngữ", "chim muông, cầm thú", "森林里生活着各种飞禽走兽。", "Trong rừng có đủ loại chim muông thú vật sinh sống.",
     "Thành ngữ. Chữ cầm là loài chim, chữ thú là loài thú; loài biết bay và loài chạy trên mặt đất. Cả cụm chỉ chung các loài chim thú."),
    ("湖泊", "húpō", "hồ bạc", "danh từ", "hồ, ao hồ", "这个地区有很多湖泊。", "Vùng này có rất nhiều hồ.",
     "Danh từ, chỉ chung các hồ nước. Chú ý âm đọc: âm tiết thứ hai đọc là pō, thanh một, không đọc là bó."),
    ("溪", "xī", "khê", "danh từ", "suối, khe suối", "村子前面有一条小溪。", "Trước làng có một con suối nhỏ.",
     "Danh từ, nghĩa là suối, dòng nước nhỏ chảy từ trên núi xuống. Thường nói 小溪，溪水."),
    ("丘陵", "qiūlíng", "khâu lăng", "danh từ", "đồi, vùng đồi thấp", "这一带都是丘陵，很适合种植茶树。", "Vùng này toàn đồi thấp, rất hợp trồng chè.",
     "Danh từ, chỉ vùng đồi thấp nhấp nhô, thấp hơn núi. Hán Việt là khâu lăng, có sách đọc là khưu lăng."),
    ("种植", "zhòngzhí", "chủng thực", "động từ", "trồng, trồng trọt", "农民在山坡上种植了很多果树。", "Nông dân trồng rất nhiều cây ăn quả trên sườn đồi.",
     "Động từ, nghĩa là trồng cây. Chú ý: âm tiết đầu đọc là zhòng, thanh bốn, vì đây là động từ trồng; khi mang nghĩa giống, loại thì đọc zhǒng, thanh ba, như trong 品种."),
    ("精心", "jīngxīn", "tinh tâm", "tính từ", "tỉ mỉ, dày công, chu đáo", "这是我为你精心准备的礼物。", "Đây là món quà tôi dày công chuẩn bị cho bạn.",
     "Tính từ, nghĩa là tỉ mỉ, dày công, rất để tâm. Thường làm trạng ngữ: 精心设计，精心照顾，精心构思. Đừng nhầm với tinh tâm trong tiếng Việt."),
    ("构思", "gòusī", "cấu tứ", "động từ", "cấu tứ, lên ý tưởng, sắp đặt", "这部小说他构思了整整三年。", "Cuốn tiểu thuyết này anh ấy cấu tứ suốt ba năm ròng.",
     "Động từ, nghĩa là suy nghĩ, sắp đặt trước nội dung và bố cục, khi viết văn, vẽ tranh hay làm một món ăn. Trong bài, 经过精心构思 là qua sự cấu tứ dày công."),
    ("烹饪", "pēngrèn", "phanh nhẫm", "động từ", "nấu nướng", "她的烹饪技术非常高。", "Tay nghề nấu nướng của cô ấy rất cao.",
     "Động từ, nghĩa là nấu nướng, mang màu sắc văn viết; khẩu ngữ thường nói 做饭，做菜. Hay gặp: 烹饪技术，烹饪学校."),
    ("即便", "jíbiàn", "tức tiện", "liên từ", "cho dù, dù cho", "即便下雨，比赛也照常进行。", "Cho dù trời mưa, trận đấu vẫn diễn ra như thường.",
     "Liên từ, nghĩa là cho dù, giống 即使. Vế sau thường có 也. Đây là điểm ngữ pháp thứ hai của bài."),
    ("素食", "sùshí", "tố thực", "danh từ", "đồ chay, thức ăn chay", "他已经吃了十年素食。", "Anh ấy đã ăn chay mười năm rồi.",
     "Danh từ, nghĩa là đồ chay. Chữ tố ở đây là chay, ngược với 荤, đồ mặn. Người ăn chay gọi là 素食者."),
    ("人间", "rénjiān", "nhân gian", "danh từ", "nhân gian, cõi đời", "苏州和杭州被称为人间天堂。", "Tô Châu và Hàng Châu được mệnh danh là thiên đường nơi trần gian.",
     "Danh từ, nghĩa là nhân gian, thế gian, cõi đời. Trong bài, 尽享人间美味 là tận hưởng mỹ vị nhân gian."),
    ("体系", "tǐxì", "thể hệ", "danh từ", "hệ thống", "这所大学有完整的教学体系。", "Trường đại học này có một hệ thống giảng dạy hoàn chỉnh.",
     "Danh từ, nghĩa là hệ thống, một chỉnh thể gồm nhiều bộ phận liên kết với nhau. So với 系统, từ 体系 hay dùng cho tư tưởng, lý luận, tổ chức, như 中华饮食体系."),
    ("品种", "pǐnzhǒng", "phẩm chủng", "danh từ", "giống, chủng loại, mặt hàng", "这家超市的水果品种很多。", "Siêu thị này có rất nhiều loại trái cây.",
     "Danh từ, chỉ giống cây trồng, giống vật nuôi, hoặc chủng loại hàng hóa. Âm tiết thứ hai đọc zhǒng, thanh ba."),
    ("认可", "rènkě", "nhận khả", "động từ", "công nhận, chấp nhận, tán thành", "他的能力得到了大家的认可。", "Năng lực của anh ấy đã được mọi người công nhận.",
     "Động từ, nghĩa là công nhận, chấp nhận. Mẫu rất hay gặp là 得到认可, được công nhận, như trong bài: 西方饮食思想与方式得到认可."),
    ("形态", "xíngtài", "hình thái", "danh từ", "hình thái, hình dạng", "水有三种形态：液态、固态和气态。", "Nước có ba trạng thái: lỏng, rắn và khí.",
     "Danh từ, nghĩa là hình thái, hình dạng biểu hiện ra bên ngoài của sự vật. Trong bài, 中华饮食形态 là diện mạo của ẩm thực Trung Hoa."),
    ("栽培", "zāipéi", "tài bồi", "động từ", "trồng trọt, vun trồng; bồi dưỡng", "这种花很难栽培。", "Loài hoa này rất khó trồng.",
     "Động từ. Nghĩa gốc là trồng và chăm sóc cây cối; nghĩa bóng là bồi dưỡng, nâng đỡ nhân tài, như 感谢老师的栽培, cảm ơn thầy đã dìu dắt. Tiếng Việt tài bồi chỉ còn nghĩa vun đắp."),
    ("培育", "péiyù", "bồi dục", "động từ", "nuôi trồng, chăm bón; lai tạo giống", "科学家培育出了一种新的水稻。", "Các nhà khoa học đã lai tạo ra một giống lúa mới.",
     "Động từ, nghĩa là nuôi trồng, chăm bón cho lớn lên, hoặc lai tạo ra giống mới. Trong bài, 培育外来品种 là lai tạo, nuôi trồng giống từ nước ngoài."),
    ("凡是", "fánshì", "phàm thị", "phó từ", "phàm là, hễ là", "凡是认识他的人都说他好。", "Hễ là người quen anh ấy thì đều khen anh ấy tốt.",
     "Phó từ, nghĩa là phàm là, hễ là, chỉ tất cả những gì nằm trong một phạm vi, không có ngoại lệ. Vế sau thường có 都. Lát nữa chúng ta sẽ phân biệt từ này với 所有."),
    ("清晰", "qīngxī", "thanh tích", "tính từ", "rõ ràng, rõ nét", "这张照片拍得非常清晰。", "Bức ảnh này chụp rất rõ nét.",
     "Tính từ, nghĩa là rõ ràng, rõ nét, dùng cho hình ảnh, âm thanh, hoặc suy nghĩ: 声音清晰，思路清晰."),
    ("分辨", "fēnbiàn", "phân biện", "động từ", "phân biệt, phân rõ", "这对双胞胎长得太像了，我分辨不出来。", "Cặp song sinh này giống nhau quá, tôi không phân biệt được.",
     "Động từ, nghĩa là phân biệt, nhận ra chỗ khác nhau. Cẩn thận: đừng nhầm với 分辩, có bộ ngôn, nghĩa là biện bạch, cãi lại."),
    ("频率", "pínlǜ", "tần suất", "danh từ", "tần suất; tần số", "这个词在口语中使用频率很高。", "Từ này có tần suất sử dụng rất cao trong khẩu ngữ.",
     "Danh từ, nghĩa là tần suất, số lần xảy ra trong một khoảng thời gian; trong vật lý là tần số. Âm tiết thứ hai đọc lǜ, thanh bốn."),
    ("调料", "tiáoliào", "điều liệu", "danh từ", "gia vị", "做这道菜需要很多调料。", "Làm món này cần rất nhiều gia vị.",
     "Danh từ, nghĩa là gia vị, như hành, gừng, tỏi, muối, nước tương. Âm tiết đầu đọc tiáo, thanh hai, giống trong 调和."),
    ("正宗", "zhèngzōng", "chính tông", "tính từ", "chính gốc, chính cống", "这家饭馆的川菜很正宗。", "Món Tứ Xuyên của quán này rất chính gốc.",
     "Tính từ, nghĩa là chính gốc, chính cống, đúng hương vị truyền thống. Rất hay dùng khi nói về món ăn: 正宗的北京烤鸭."),
    ("加工", "jiāgōng", "gia công", "động từ", "chế biến, gia công", "这些水果可以加工成果汁。", "Những loại trái cây này có thể chế biến thành nước ép.",
     "Động từ, nghĩa là chế biến nguyên liệu thành sản phẩm, như 食品加工，加工厂; hoặc sửa sang cho hoàn thiện, như 这篇文章还需要加工. Chú ý: tiếng Việt gia công hay chỉ việc nhận làm hàng theo đơn đặt hàng; còn 加工 thiên về chế biến."),
    ("照样", "zhàoyàng", "chiếu dạng", "phó từ", "vẫn như thường, vẫn cứ", "他病了，可是照样去上班。", "Anh ấy bị ốm, nhưng vẫn đi làm như thường.",
     "Phó từ, nghĩa là điều kiện đã thay đổi, nhưng sự việc vẫn như cũ. Trong bài: nguyên liệu từ nước ngoài, nhưng người Trung Quốc 照样 nấu theo kiểu Trung Quốc."),
    ("得力", "délì", "đắc lực", "động từ", "nhờ vào, được lợi từ", "他的成功得力于家人的支持。", "Thành công của anh ấy là nhờ sự ủng hộ của gia đình.",
     "Động từ, thường dùng theo mẫu 得力于, nghĩa là nhờ vào. Cẩn thận: tiếng Việt đắc lực là giỏi giang, giúp được việc. Tiếng Trung cũng có nghĩa tính từ đó, như 得力助手, trợ thủ đắc lực; nhưng trong bài thì là động từ, nhờ vào."),
    ("内在", "nèizài", "nội tại", "tính từ", "bên trong, nội tại", "我们不能只看外表，更要看内在。", "Chúng ta không thể chỉ nhìn vẻ ngoài, mà càng phải nhìn bên trong.",
     "Tính từ, nghĩa là bên trong, vốn có trong sự vật, trái nghĩa với 外在. Trong bài, 内在价值 là giá trị bên trong."),
    ("灵感", "línggǎn", "linh cảm", "danh từ", "cảm hứng, nguồn cảm hứng", "这首歌的灵感来自一次旅行。", "Cảm hứng của bài hát này đến từ một chuyến du lịch.",
     "Danh từ. Đây là từ rất dễ nhầm! Tiếng Việt linh cảm là cảm giác báo trước một chuyện sắp xảy ra, tiếng Trung gọi là 预感. Còn 灵感 là cảm hứng sáng tạo, ý tưởng chợt đến."),
    ("创新", "chuàngxīn", "sáng tân", "động từ", "đổi mới, sáng tạo cái mới", "企业要发展，就必须不断创新。", "Doanh nghiệp muốn phát triển thì phải không ngừng đổi mới.",
     "Động từ, nghĩa là bỏ cái cũ, tạo ra cái mới. Cũng dùng như danh từ: 技术创新. Trong bài có 创新式地, theo cách sáng tạo."),
    ("就餐", "jiùcān", "tựu xan", "động từ", "ăn cơm, dùng bữa", "请各位客人到二楼就餐。", "Mời quý khách lên tầng hai dùng bữa.",
     "Động từ, nghĩa là ăn cơm, dùng bữa, mang màu sắc trang trọng, văn viết. Trong sách, từ này có dấu sao, tức là từ nằm ngoài đề cương HSK. Ví dụ ở bài tập một: 合餐，分餐，餐桌，餐厅."),
    ("排斥", "páichì", "bài xích", "động từ", "bài xích, loại trừ", "我们不应该排斥不同的文化。", "Chúng ta không nên bài xích những nền văn hóa khác.",
     "Động từ, nghĩa là bài xích, gạt bỏ, không chấp nhận. Trong bài, 不排斥异域文化 là không bài xích văn hóa nước ngoài."),
    ("折", "zhé", "chiết", "động từ", "gấp, xếp", "她把信折好放进了信封。", "Cô ấy gấp lá thư lại rồi bỏ vào phong bì.",
     "Động từ, nghĩa là gấp, xếp, như 折纸, gấp giấy. Trong bài, 可随意折起来 là có thể tùy ý gấp lại. Ngoài ra, khi mua sắm, 打八折 là giảm giá còn tám mươi phần trăm."),
    ("跪", "guì", "quỵ", "động từ", "quỳ, quỳ gối", "古人见到皇帝要跪下。", "Người xưa gặp hoàng đế thì phải quỳ xuống.",
     "Động từ, nghĩa là quỳ gối. Cẩn thận: Hán Việt là quỵ, nhưng không phải ngã quỵ, mà là quỳ. Trong bài, 跪坐而食 là ngồi quỳ mà ăn."),
    ("局限", "júxiàn", "cục hạn", "động từ", "hạn chế, giới hạn, bó hẹp", "我们不能只局限在书本知识上。", "Chúng ta không thể chỉ bó hẹp trong kiến thức sách vở.",
     "Động từ, nghĩa là giới hạn trong một phạm vi hẹp. Cũng dùng như danh từ, như trong bài: 打破了跪坐而食的局限, phá vỡ giới hạn của lối ngồi quỳ mà ăn. Còn 局限性 là tính hạn chế."),
    ("诞生", "dànshēng", "đản sinh", "động từ", "ra đời, chào đời", "电脑的诞生改变了人们的生活。", "Sự ra đời của máy tính đã thay đổi cuộc sống con người.",
     "Động từ, nghĩa là ra đời, mang sắc thái trang trọng. Dùng cho vĩ nhân, quốc gia, hoặc một sự vật mới; người bình thường thì nói 出生."),
    ("继承", "jìchéng", "kế thừa", "động từ", "kế thừa, thừa kế", "我们要继承和发扬优秀的传统文化。", "Chúng ta phải kế thừa và phát huy văn hóa truyền thống ưu tú.",
     "Động từ, nghĩa là kế thừa truyền thống, sự nghiệp, hoặc thừa kế tài sản. Âm Hán Việt và nghĩa giống tiếng Việt."),
    ("元素", "yuánsù", "nguyên tố", "danh từ", "yếu tố, nhân tố; nguyên tố", "这件衣服加入了很多中国元素。", "Bộ quần áo này đưa vào rất nhiều yếu tố Trung Hoa.",
     "Danh từ. Trong hóa học là nguyên tố, như 化学元素; nghĩa rộng là yếu tố, chất liệu, như 中国元素，时尚元素. Trong bài, 新元素 là những yếu tố mới."),
    ("活力", "huólì", "hoạt lực", "danh từ", "sức sống, sinh lực", "年轻人总是充满活力。", "Người trẻ luôn tràn đầy sức sống.",
     "Danh từ, nghĩa là sức sống, sinh khí. Hay gặp: 充满活力，富有活力."),
    ("奥秘", "àomì", "áo bí", "danh từ", "điều bí ẩn, điều huyền bí", "科学家们一直在探索宇宙的奥秘。", "Các nhà khoa học luôn khám phá những điều bí ẩn của vũ trụ.",
     "Danh từ, nghĩa là điều bí ẩn sâu xa, chưa được biết đến. Trong bài, 奥秘所在 là chỗ bí ẩn nằm ở đó, tức là bí quyết."),
]

add("bullets", chapter="Từ mới (51 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 10 có 51 từ mới, chia thành 17 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 调和 · 调料 (tiáo) · 湖泊 (pō) · 种植 (zhòng) · 品种 (zhǒng)",
           "Từ dễ nhầm: 灵感 · 鲜明 · 得力 · 加工 · 跪 · 精心"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có năm mươi mốt từ, thầy chia thành mười bảy nhóm nhỏ, mỗi nhóm ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số từ có âm đọc cần chú ý, như 调和 và 调料, âm tiết đầu đọc tiáo; 湖泊, âm tiết sau đọc pō; và 种植 với 品种, một từ đọc zhòng, một từ đọc zhǒng. Thầy sẽ nhắc khi gặp."),
         F(4, "Ngoài ra, có mấy từ Hán Việt rất dễ hiểu nhầm, như 灵感，鲜明，得力，加工，跪，精心. Nghĩa của chúng trong tiếng Trung khác với tiếng Việt, các bạn nhớ nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

sizes = [3] * 17
assert sum(sizes) == len(V)
g = 0
for gs in sizes:
    group = V[g:g + gs]
    words, say = [], []
    for i, (zh, py, hv, loai, vi, ex, exvi, expl) in enumerate(group):
        n = g + i + 1
        words.append({"zh": zh, "py": py, "hv": hv.upper(), "loai": f"{n}. {loai}", "vi": vi, "ex": ex, "exvi": exvi})
        say.append(F(i, f"Từ số {n}: {zh}。 {zh}。 Hán Việt là {hv}.", zr=120))
        say.append(F(i, f"{expl} Ví dụ: {ex}{'' if ex[-1] in '。…？！，' else '，'} {exvi[0].upper() + exvi[1:]}{'' if exvi.endswith('.') else '.'}", zr=130))
    add("vocab", section="Từ mới 生词", title=f"Từ mới ({g + 1}–{g + len(group)} / {len(V)})",
        words=words, say=say)
    g += gs

# ======================= BÀI KHÓA =======================
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung nếu khác])
P = [
    ("任何一个民族的饮食都不仅仅为饮食，它蕴藏着这个民族的精神与特征，传达着这个民族的文化传统。",
     "Ẩm thực của bất kỳ dân tộc nào cũng không chỉ đơn thuần là chuyện ăn uống; nó chứa đựng tinh thần và đặc trưng của dân tộc ấy, truyền tải truyền thống văn hóa của dân tộc ấy.",
     ["不仅仅为饮食 nghĩa là không chỉ đơn thuần là ăn uống. Ở đây 仅仅为 tương đương 仅仅是, mang màu sắc văn viết.",
      "蕴藏着 và 传达着 là hai động từ có 着 đi song song, tạo nhịp câu cân đối. Từ 与 nghĩa là và, văn viết, giống 和. Câu mở đầu nêu luận điểm chung của cả bài."]),
    ("中国的饮食文化历经数千年，始终具有魅力，是因为它不仅民族特性鲜明，而且善于吸收不同国家、不同区域、不同民族的优异之处，以至辉煌至今。",
     "Văn hóa ẩm thực Trung Quốc đã trải qua mấy nghìn năm mà luôn có sức hấp dẫn, là vì nó không những mang đặc tính dân tộc rõ nét, mà còn giỏi hấp thu những điểm ưu tú của các quốc gia, các khu vực, các dân tộc khác nhau, đến mức rực rỡ cho đến tận ngày nay.",
     ["历经 là trải qua, 数千年 là mấy nghìn năm. 是因为 nghĩa là là bởi vì: nói kết quả trước, rồi mới nêu nguyên nhân.",
      "不仅……而且……，以至…… nghĩa là không những…, mà còn…, đến mức…. 以至 là điểm ngữ pháp thứ nhất. 善于 là giỏi về, 至今 là cho đến nay. Câu này có trong bài tập bốn, các bạn nhớ cấu trúc nhé."]),
    ("中国文化的核心是一个“和”字。“和”包含“中和”“和谐”之意。“中和”的意思就是折中、调和性质不同的事物。",
     "Cốt lõi của văn hóa Trung Quốc là một chữ Hòa. Hòa bao hàm ý nghĩa trung hòa và hài hòa. Trung hòa nghĩa là dung hòa, điều hòa những sự vật có tính chất khác nhau.",
     ["核心 là hạt nhân, cốt lõi. 之意 là ý nghĩa của…, văn viết: 包含中和、和谐之意, bao hàm ý trung hòa và hài hòa.",
      "折中 là chiết trung, dung hòa các bên, không thiên lệch. 调和 ở đây đọc tiáohé. Đoạn này rất ngắn nhưng quan trọng, vì cuối bài tác giả sẽ quay lại chữ Hòa."],
     "中国文化的核心是一个和字。和包含中和、和谐之意。中和的意思就是折中、调和性质不同的事物。"),
    ("原本中华饮食中的大量食物来自辽阔的土地，高山上的飞禽走兽，湖泊、小溪中的一条鱼，丘陵上种植的一棵菜，经过精心构思，巧妙烹饪，即便仅为一餐素食，也可以让你尽享人间美味。",
     "Vốn dĩ, rất nhiều thực phẩm trong ẩm thực Trung Hoa đến từ đất đai bao la: chim muông thú rừng trên núi cao, một con cá trong hồ, trong suối, một cây rau trồng trên đồi; qua sự cấu tứ dày công và cách nấu khéo léo, cho dù chỉ là một bữa cơm chay, cũng có thể cho bạn tận hưởng mỹ vị nhân gian.",
     ["中华, theo chú thích của sách: thời cổ gọi vùng lưu vực sông Hoàng Hà là Trung Hoa, đó là cái nôi của người Hán; về sau dùng để chỉ Trung Quốc. 原本 là vốn dĩ, lúc đầu.",
      "即便仅为一餐素食，也…… nghĩa là cho dù chỉ là một bữa chay, cũng…. Đây là điểm ngữ pháp 即便. 尽享 là tận hưởng trọn vẹn. Chú ý các lượng từ: 一条鱼，一棵菜，一餐素食."]),
    ("汉唐以后，中亚及东南亚的食物进入了中华饮食体系，极大地丰富了中国食物的品种；近代，西方饮食思想与方式得到认可，具有现代特征的中华饮食形态逐渐形成。",
     "Từ sau đời Hán, đời Đường, thực phẩm của Trung Á và Đông Nam Á đã đi vào hệ thống ẩm thực Trung Hoa, làm phong phú thêm rất nhiều chủng loại thực phẩm của Trung Quốc; đến thời cận đại, tư tưởng và phương thức ẩm thực phương Tây được chấp nhận, hình thái ẩm thực Trung Hoa mang đặc trưng hiện đại dần dần hình thành.",
     ["汉唐 là nhà Hán và nhà Đường. Theo chú thích, nhà Hán từ năm hai trăm linh sáu trước Công nguyên đến năm hai trăm hai mươi, nhà Đường từ năm sáu trăm mười tám đến năm chín trăm linh bảy. 中亚 là Trung Á, gồm năm nước Kazakhstan, Uzbekistan, Kyrgyzstan, Tajikistan và Turkmenistan. 东南亚 là Đông Nam Á, trong đó có cả Việt Nam chúng ta.",
      "极大地丰富了 là làm phong phú lên rất nhiều, ở đây 丰富 là động từ. 得到认可 là được chấp nhận. Dấu chấm phẩy chia câu thành hai giai đoạn: sau Hán Đường, và thời cận đại."]),
    ("在食材栽培方面，中华饮食坚持以本国物产为基本原料，同时合理引进、培育外来品种，比如咖啡、柠檬、芒果等，凡是历史不够悠久的外来食品，人们一般从食物名称上就能立即清晰地分辨出它的洋身份。",
     "Về mặt trồng trọt nguyên liệu, ẩm thực Trung Hoa kiên trì lấy sản vật trong nước làm nguyên liệu cơ bản, đồng thời du nhập và nuôi trồng một cách hợp lý các giống ngoại lai, ví dụ cà phê, chanh, xoài…; phàm là thực phẩm ngoại lai có lịch sử chưa đủ lâu đời, người ta thường chỉ nhìn tên gọi là có thể lập tức nhận ra rõ ràng thân phận nước ngoài của nó.",
     ["以本国物产为基本原料 nghĩa là lấy sản vật trong nước làm nguyên liệu cơ bản, theo mẫu câu văn viết lấy cái này làm cái kia, rất hay gặp. 引进 là du nhập, đưa từ nước ngoài vào.",
      "凡是……，人们一般……就能…… nghĩa là phàm là…, người ta thường… là có thể…. 洋身份 là thân phận ngoại quốc; chữ dương ở đây chỉ những thứ đến từ nước ngoài, như 洋葱, hành tây. Câu này cũng là mẫu của bài tập bốn."]),
    ("至于中餐中使用频率最高的葱、姜、蒜等调料，因其进入中华饮食年代久远，许多中国人甚至把它当成了正宗的中国食材。",
     "Còn những loại gia vị được dùng nhiều nhất trong món ăn Trung Quốc như hành, gừng, tỏi, vì chúng đã đi vào ẩm thực Trung Hoa từ rất lâu đời, nhiều người Trung Quốc thậm chí còn coi chúng là nguyên liệu Trung Quốc chính gốc.",
     ["至于 nghĩa là còn như, còn về, dùng để chuyển sang một đối tượng mới. 因其 là bởi vì nó, trong đó 其 là đại từ văn viết, bằng 它.",
      "把它当成了 nghĩa là coi nó là; 当成 đọc là dàngchéng, thanh bốn. 年代久远 là niên đại xa xưa. Còn nhớ phần khởi động không? Hành, gừng, tỏi chính là nhóm gia vị đấy."]),
    ("在加工过程中，中国人照样可以用中国方式烹饪外来食材，使它美味诱人。而这一切得力于中国人能够充分认识异域食物的内在价值，以开放性的思维和灵感，创新式地把外来食物改变为中国饮食成分。",
     "Trong quá trình chế biến, người Trung Quốc vẫn có thể dùng cách của Trung Quốc để nấu nguyên liệu ngoại lai, khiến chúng thơm ngon hấp dẫn. Mà tất cả những điều này là nhờ người Trung Quốc biết nhận thức đầy đủ giá trị bên trong của thực phẩm từ vùng đất khác, dùng tư duy cởi mở và cảm hứng, sáng tạo biến thực phẩm ngoại lai thành một phần của ẩm thực Trung Quốc.",
     ["照样 là vẫn như thường: nguyên liệu là của nước ngoài, nhưng vẫn nấu theo kiểu Trung Quốc. 美味诱人 là ngon lành hấp dẫn. 使它 là làm cho nó.",
      "得力于 là nhờ vào. 异域 là vùng đất khác, nước ngoài. 以开放性的思维和灵感 là dựa vào tư duy cởi mở và cảm hứng. 创新式地 là một cách sáng tạo, làm trạng ngữ cho động từ 改变."]),
    ("在就餐方式上，中华饮食文化同样显示着不排斥异域文化的态度，比如中餐“合餐制”的形成。先秦至唐代，中国采用分餐式方式就餐。",
     "Về phương thức dùng bữa, văn hóa ẩm thực Trung Hoa cũng thể hiện thái độ không bài xích văn hóa nước ngoài, ví dụ như sự hình thành chế độ ăn chung của người Trung Quốc. Từ thời Tiên Tần đến đời Đường, Trung Quốc ăn theo kiểu chia phần riêng.",
     ["合餐制 là chế độ ăn chung: mọi người ngồi quanh một bàn, cùng gắp từ những đĩa chung. 分餐式 là mỗi người một phần riêng.",
      "先秦, theo chú thích của sách, thường chỉ thời kỳ trước khi nhà Tần thống nhất Trung Quốc, tức thời Xuân Thu Chiến Quốc. 至 ở đây là đến, văn viết."],
     "在就餐方式上，中华饮食文化同样显示着不排斥异域文化的态度，比如中餐合餐制的形成。先秦至唐代，中国采用分餐式方式就餐。"),
    ("南北朝时期，一种可随意折起来、称作胡床的坐具和一种较大的餐桌开始在中原地区流行，这些器具的推广，打破了跪坐而食的局限，形成了围坐合餐的形式。",
     "Thời Nam Bắc triều, một loại đồ ngồi có thể tùy ý gấp lại, gọi là hồ sàng, cùng một loại bàn ăn khá lớn bắt đầu thịnh hành ở vùng Trung Nguyên; việc phổ biến những vật dụng này đã phá vỡ giới hạn của lối ngồi quỳ mà ăn, hình thành nên hình thức ngồi quây quần ăn chung.",
     ["南北朝 là thời Nam Bắc triều, từ năm bốn trăm hai mươi đến năm năm trăm tám mươi chín. 中原 là vùng trung và hạ lưu sông Hoàng Hà. 胡床 là một loại ghế xếp du nhập từ các dân tộc phương Bắc và phương Tây, nên mới gọi là hồ sàng.",
      "跪坐而食 là ngồi quỳ mà ăn. 打破局限 là phá vỡ giới hạn, ở đây 局限 dùng như danh từ. 围坐合餐 là ngồi quây quanh bàn ăn chung."]),
    ("当然，对“合餐制”的全面接受与文化认同，根本上与“和”文化是相通的。",
     "Đương nhiên, việc hoàn toàn tiếp nhận và đồng thuận về văn hóa đối với chế độ ăn chung, về căn bản là tương thông với văn hóa chữ Hòa.",
     ["对合餐制的全面接受与文化认同 là một cụm danh từ dài làm chủ ngữ. 认同 là đồng tình, thừa nhận.",
      "相通 là tương thông, có điểm chung. Tác giả quay lại ý chữ Hòa ở đoạn hai: ngồi quây quần ăn chung chính là biểu hiện của sự hòa hợp."],
     "当然，对合餐制的全面接受与文化认同，根本上与和文化是相通的。"),
    ("可以说，中华饮食文化自诞生之日起，就面向世界，边继承，边改革，不断引进新元素，这也是其充满活力的奥秘所在。",
     "Có thể nói, văn hóa ẩm thực Trung Hoa ngay từ ngày ra đời đã hướng ra thế giới, vừa kế thừa vừa cải cách, không ngừng du nhập những yếu tố mới; đây cũng chính là bí quyết khiến nó tràn đầy sức sống.",
     ["自……之日起 nghĩa là kể từ ngày…. 面向世界 là hướng ra thế giới. 边继承，边改革 là vừa kế thừa, vừa cải cách.",
      "奥秘所在 là chỗ bí ẩn nằm ở đó, tức là bí quyết; 所在 là điểm ngữ pháp thứ ba. Câu kết tổng kết cả bài: ẩm thực Trung Hoa sống mãi nhờ vừa giữ gốc vừa đổi mới."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 全球化视野中的中国饮食", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 全球化视野中的中国饮食, dài bảy trăm bảy mươi mốt chữ. Bài được cải biên từ bài viết 论全球化视野中的中国饮食 của tác giả 肖向东.",
         F(0, "Thầy chia bài thành mười hai đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng. Đây là văn nghị luận, câu khá dài, nên các bạn chú ý các cặp liên từ nhé."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 90 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Tóm tắt nội dung", section="Bài khóa 课文", title="Tóm tắt bài khóa (theo bài tập 5) – phần 1", size=34,
    items=["## 1. 中国饮食文化为什么具有魅力？",
           "不仅民族特性鲜明，而且善于吸收……优异之处，以至辉煌至今",
           "## 2. 中国文化的核心",
           "“和”：包含“中和”“和谐”之意",
           "## 3. 发展历程 – 食物",
           "原本：来自辽阔的土地 · 汉唐以后：中亚及东南亚的食物进入 · 近代：西方饮食思想与方式得到认可"],
    say=["Bài tập năm của sách yêu cầu dựa vào gợi ý để tóm tắt nội dung chính của bài khóa. Chúng ta cùng làm luôn nhé.",
         F(0, "Câu hỏi một: vì sao văn hóa ẩm thực Trung Quốc có sức hấp dẫn?"),
         F(1, "Dùng khung 不仅，而且，以至: 不仅民族特性鲜明，而且善于吸收不同国家、不同区域、不同民族的优异之处，以至辉煌至今。"),
         F(2, "Câu hỏi hai: cốt lõi của văn hóa Trung Quốc là gì?"),
         F(3, "Là chữ Hòa, bao hàm hai ý: 中和 và 和谐."),
         F(4, "Câu hỏi ba: quá trình phát triển của ẩm thực Trung Hoa, trước hết là về thực phẩm."),
         F(5, "原本，食物来自辽阔的土地。 Lúc đầu, thực phẩm đến từ đất đai bao la của Trung Quốc. 汉唐以后，中亚及东南亚的食物进入中华饮食体系。 Sau Hán Đường, thực phẩm Trung Á và Đông Nam Á đi vào. 近代，西方饮食思想与方式得到认可。 Thời cận đại, tư tưởng ẩm thực phương Tây được chấp nhận.")])

add("bullets", section="Bài khóa 课文", title="Tóm tắt bài khóa (theo bài tập 5) – phần 2", size=34,
    items=["## 4. 食材",
           "以本国物产为基本原料 · 同时合理引进外来品种 · 凡是……就能分辨出它的洋身份 · 至于葱、姜、蒜……因其……甚至……",
           "## 5. 加工过程",
           "照样可以用中国方式烹饪外来食材 · 得力于开放性的思维和灵感",
           "## 6. 就餐方式",
           "先秦至唐代：分餐 · 南北朝时期：胡床、大餐桌 → 围坐合餐",
           "## 7. 总结",
           "面向世界，边继承，边改革，不断引进新元素"],
    say=[F(0, "Tiếp theo là về nguyên liệu."),
         F(1, "Ẩm thực Trung Hoa 以本国物产为基本原料, đồng thời 合理引进外来品种. 凡是历史不够悠久的外来食品，一看名称就能分辨出它的洋身份。 Còn 葱、姜、蒜, vì vào Trung Quốc từ lâu, nên nhiều người thậm chí coi là nguyên liệu chính gốc."),
         F(2, "Về quá trình chế biến."),
         F(3, "中国人照样可以用中国方式烹饪外来食材, và điều này 得力于 tư duy cởi mở và cảm hứng sáng tạo."),
         F(4, "Về cách dùng bữa."),
         F(5, "Từ thời Tiên Tần đến đời Đường là ăn chia phần. Đến thời Nam Bắc triều, ghế xếp 胡床 và bàn ăn lớn được phổ biến, hình thành kiểu 围坐合餐, ngồi quây quần ăn chung."),
         F(6, "Cuối cùng là phần tổng kết."),
         F(7, "中华饮食文化面向世界，边继承，边改革，不断引进新元素。 Đó là bí quyết của sức sống. Bố cục này rất có ích cho bài tập về nhà: viết tóm tắt bài khóa khoảng ba trăm chữ.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 以至", section="Ngữ pháp 注释", title="1. 以至 yǐzhì – đến nỗi, đến mức", size=36,
    items=["Liên từ, đứng đầu vế sau: mức độ ở vế trước rất sâu → dẫn đến một kết quả",
           "Cũng nói 以至于",
           "中国的饮食文化历经数千年，始终具有魅力，是因为它不仅民族特性鲜明，而且善于吸收不同国家、不同区域、不同民族的优异之处，以至辉煌至今。",
           "那个电影她看了十来遍，以至许多台词都能背诵下来。",
           "著名作家纪伯伦曾说：“我们已经走得太远，以至于忘了为什么出发。”"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là liên từ 以至.",
         F(0, "以至 là liên từ, đứng ở đầu vế câu phía sau. Nó biểu thị: vì tình huống ở vế trước có mức độ rất sâu, nên dẫn đến một kết quả nào đó. Tiếng Việt dịch là đến nỗi, đến mức."),
         F(1, "Cũng có thể nói 以至于, nghĩa hoàn toàn giống nhau."),
         F(2, "Ví dụ một, lấy từ bài khóa: 中国的饮食文化历经数千年，始终具有魅力，是因为它不仅民族特性鲜明，而且善于吸收不同国家、不同区域、不同民族的优异之处，以至辉煌至今。 Vì nó giỏi hấp thu cái hay của người khác, đến mức rực rỡ cho đến ngày nay."),
         F(3, "Ví dụ hai: 那个电影她看了十来遍，以至许多台词都能背诵下来。 Bộ phim đó cô ấy xem đến mười mấy lần, đến mức thuộc lòng được nhiều câu thoại. 十来遍 là khoảng mười lần."),
         F(4, "Ví dụ ba: 著名作家纪伯伦曾说：我们已经走得太远，以至于忘了为什么出发。 Nhà văn nổi tiếng Kahlil Gibran từng nói: Chúng ta đã đi quá xa, đến nỗi quên mất vì sao mình xuất phát.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: dùng 以至 hoàn thành câu", reveal=True, size=36,
    items=["(1) 朋友告诉我，这所商学院在北美有相当的知名度，……",
           "Đáp án: ……，以至很多中国学生都想去那儿留学。",
           "(2) 科学技术的发展实在是太快了，……如今变为了现实。",
           "Đáp án: ……，以至许多过去只在科幻电影里出现的东西，如今变为了现实。",
           "(3) 走在路上，他脑子里一直在想别的事，……",
           "Đáp án: ……，以至走过了家门都没发现。"],
    say=[F(0, "Luyện tập: dùng 以至 hoàn thành câu. Câu một: 朋友告诉我，这所商学院在北美有相当的知名度，以至什么? Bạn tôi nói với tôi, trường kinh doanh này khá nổi tiếng ở Bắc Mỹ, đến mức sao? Các bạn tạm dừng và thử hoàn thành câu nhé."),
         F(1, "Đáp án gợi ý: 以至很多中国学生都想去那儿留学。 Đến mức rất nhiều sinh viên Trung Quốc đều muốn đến đó du học."),
         F(2, "Câu hai: 科学技术的发展实在是太快了，以至什么如今变为了现实。 Khoa học kỹ thuật phát triển thật sự quá nhanh, đến mức cái gì đó nay đã thành hiện thực?"),
         F(3, "Đáp án gợi ý: 以至许多过去只在科幻电影里出现的东西，如今变为了现实。 Đến mức nhiều thứ trước kia chỉ xuất hiện trong phim khoa học viễn tưởng, nay đã trở thành hiện thực."),
         F(4, "Câu ba: 走在路上，他脑子里一直在想别的事，以至什么。 Đi trên đường, đầu óc anh ấy cứ nghĩ chuyện khác, đến nỗi sao?"),
         F(5, "Đáp án gợi ý: 以至走过了家门都没发现。 Đến nỗi đi quá cửa nhà mà cũng không biết. Chú ý: vế sau 以至 luôn là kết quả của mức độ ở vế trước.")])

add("bullets", chapter="Ngữ pháp: 即便", section="Ngữ pháp 注释", title="2. 即便 jíbiàn – cho dù, dù cho", size=36,
    items=["Liên từ, biểu thị giả thiết kiêm nhượng bộ, nghĩa là 就是、即使",
           "Mẫu: 即便……，也/还……",
           "她最近心情不好，即便有些不讲理，你也要原谅她。",
           "我喜欢那个工作，即便薪水低，我还是要去。",
           "……经过精心构思，巧妙烹饪，即便仅为一餐素食，也可以让你尽享人间美味。"],
    say=["Điểm ngữ pháp thứ hai là liên từ 即便.",
         F(0, "即便 biểu thị giả thiết kiêm nhượng bộ: tạm giả sử có một tình huống, rồi nói rằng kết quả vẫn không thay đổi. Nghĩa giống 就是 và 即使, tiếng Việt dịch là cho dù, dù cho."),
         F(1, "Vế sau thường dùng 也, hoặc 还, 还是."),
         F(2, "Ví dụ một: 她最近心情不好，即便有些不讲理，你也要原谅她。 Dạo này tâm trạng cô ấy không tốt, cho dù có hơi vô lý, cậu cũng phải tha thứ cho cô ấy."),
         F(3, "Ví dụ hai: 我喜欢那个工作，即便薪水低，我还是要去。 Tôi thích công việc đó, cho dù lương thấp, tôi vẫn muốn đi."),
         F(4, "Ví dụ ba, lấy từ bài khóa: 经过精心构思，巧妙烹饪，即便仅为一餐素食，也可以让你尽享人间美味。 Qua cấu tứ dày công, nấu nướng khéo léo, cho dù chỉ là một bữa chay, cũng cho bạn tận hưởng mỹ vị nhân gian.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: hoàn thành câu với 即便", reveal=True, size=36,
    items=["(1) 即便我们拿了冠军，……",
           "Đáp án: ……，也不能骄傲。",
           "(2) 大家……，即便说错了也没关系。",
           "Đáp án: 大家有什么想法都可以大胆地说出来，……",
           "(3) 即便……，你也应该严格要求自己。",
           "Đáp án: 即便没有人监督你，……"],
    say=[F(0, "Luyện tập: hoàn thành câu. Câu một: 即便我们拿了冠军，…… Cho dù chúng ta giành chức vô địch, thì sao? Các bạn tạm dừng và thử hoàn thành câu nhé."),
         F(1, "Đáp án gợi ý: 即便我们拿了冠军，也不能骄傲。 Cho dù chúng ta giành chức vô địch, cũng không được kiêu ngạo."),
         F(2, "Câu hai: 大家，什么什么，即便说错了也没关系。 Mọi người làm sao đó, cho dù nói sai cũng không sao."),
         F(3, "Đáp án gợi ý: 大家有什么想法都可以大胆地说出来，即便说错了也没关系。 Mọi người có ý kiến gì cứ mạnh dạn nói ra, cho dù nói sai cũng không sao."),
         F(4, "Câu ba: 即便什么什么，你也应该严格要求自己。 Cho dù thế nào, bạn cũng nên nghiêm khắc với bản thân."),
         F(5, "Đáp án gợi ý: 即便没有人监督你，你也应该严格要求自己。 Cho dù không có ai giám sát, bạn cũng nên nghiêm khắc với chính mình. Các bạn thấy đấy, vế sau luôn có 也.")])

add("bullets", chapter="Ngữ pháp: 所在", section="Ngữ pháp 注释", title="3. 所在 suǒzài – chỗ, nơi tồn tại", size=36,
    items=["Danh từ: nơi chốn, chỗ tồn tại; dùng trong văn viết",
           "Hay gặp: 问题所在 · 原因所在 · 关键所在 · 力量所在 · 希望所在 · 奥秘所在",
           "他选择了风景秀美、气候宜人的所在，盖了房子，安下了家。",
           "培养人是教育的立足点，是教育价值的根本所在，是教育的本体功能。",
           "可以说，中华饮食文化自诞生之日起，就面向世界，边继承，边改革，不断引进新元素，这也是其充满活力的奥秘所在。"],
    say=["Điểm ngữ pháp thứ ba là danh từ 所在.",
         F(0, "所在 là danh từ, chỉ nơi chốn, chỗ mà sự vật tồn tại. Từ này dùng trong văn viết."),
         F(1, "所在 thường đứng sau một danh từ trừu tượng, chỉ cái cốt lõi nằm ở đâu: 问题所在, chỗ mấu chốt của vấn đề; 原因所在, nguyên nhân nằm ở đó; 关键所在, then chốt; 力量所在, sức mạnh; 希望所在, niềm hy vọng; 奥秘所在, bí quyết."),
         F(2, "Ví dụ một: 他选择了风景秀美、气候宜人的所在，盖了房子，安下了家。 Ông ấy chọn một nơi phong cảnh đẹp, khí hậu dễ chịu, cất nhà và an cư ở đó. Ở đây 所在 mang nghĩa cụ thể là một nơi chốn."),
         F(3, "Ví dụ hai: 培养人是教育的立足点，是教育价值的根本所在，是教育的本体功能。 Bồi dưỡng con người là chỗ đứng của giáo dục, là cái gốc của giá trị giáo dục, là chức năng bản thể của giáo dục."),
         F(4, "Ví dụ ba, lấy từ câu kết của bài khóa: 这也是其充满活力的奥秘所在。 Đây cũng chính là bí quyết khiến nó tràn đầy sức sống.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: chọn vị trí thích hợp cho 所在", reveal=True, size=36,
    items=["(1) 大家的支持A是我们的力量B，我们一定会尽心尽力做好C工作，不辜负大家的期望D。",
           "Đáp án: B – 大家的支持是我们的力量所在。",
           "(2) 找不到问题A在哪儿，解决问题B就无从谈起，只有找到问题C，才谈得上解决问题D。",
           "Đáp án: C – 只有找到问题所在，才谈得上解决问题。",
           "(3) 给A孩子们B创造幸福美好的生活C，是父亲一生为之奋斗的动力D。",
           "Đáp án: D – ……是父亲一生为之奋斗的动力所在。"],
    say=[F(0, "Luyện tập: chọn vị trí thích hợp cho 所在. Câu một: 大家的支持是我们的力量，我们一定会尽心尽力做好工作，不辜负大家的期望。 Sự ủng hộ của mọi người là sức mạnh của chúng tôi, chúng tôi nhất định sẽ dốc hết sức làm tốt công việc, không phụ kỳ vọng của mọi người. Có bốn vị trí A, B, C, D. Các bạn chọn thử nhé."),
         F(1, "Đáp án: B. 大家的支持是我们的力量所在。 Nhớ cụm 力量所在, sức mạnh nằm ở đó."),
         F(2, "Câu hai: 找不到问题在哪儿，解决问题就无从谈起，只有找到问题，才谈得上解决问题。 Không tìm ra vấn đề ở đâu thì chẳng thể nói đến chuyện giải quyết; chỉ khi tìm ra vấn đề, mới nói được đến chuyện giải quyết."),
         F(3, "Đáp án: C. 只有找到问题所在，才谈得上解决问题。 Cụm 问题所在 là chỗ mấu chốt của vấn đề. Vị trí A sai, vì sau đó đã có 在哪儿 rồi."),
         F(4, "Câu ba: 给孩子们创造幸福美好的生活，是父亲一生为之奋斗的动力。 Tạo cho các con một cuộc sống hạnh phúc tươi đẹp, là động lực mà người cha phấn đấu cả đời."),
         F(5, "Đáp án: D. 是父亲一生为之奋斗的动力所在。 Mẹo: 所在 luôn đứng sau danh từ mà nó bổ sung, như 力量，问题，动力.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 凡是 – 所有", section="Phân biệt từ 词语辨析", title="Phân biệt 凡是 và 所有",
    common="Giống nhau: đều chỉ toàn bộ, không có ngoại lệ. Ví dụ: 凡是/所有参加会议的人，都要自带笔记本电脑。",
    cols=[{"head": "凡是",
           "lines": ["(1) Nhấn mạnh một phạm vi đặc định; chỉ đứng trước danh từ có tính chất riêng",
                     "Đúng: 凡是教师，都有国家认定的资格证书。",
                     "Sai: 凡是东西都放在这里。",
                     "(2) Phó từ, đứng được trước động từ",
                     "Đúng: 市里凡是有画展，再远他也要去参观学习。"]},
          {"head": "所有",
           "lines": ["(1) Đứng trực tiếp trước danh từ chung chung",
                     "Đúng: 所有东西都放在这里。",
                     "(2) Tính từ, chỉ bổ nghĩa cho danh từ, không đứng trước động từ",
                     "Đúng: 所有问题都解决了。"]}],
    say=["Tiếp theo là phần phân biệt từ: 凡是 và 所有. Tiếng Việt có thể dịch cả hai là tất cả, mọi, nên rất dễ dùng lẫn.",
         "Điểm giống nhau: cả hai đều chỉ toàn bộ, không có một ngoại lệ nào. Ví dụ: 凡是参加会议的人，都要自带笔记本电脑, hoặc 所有参加会议的人，都要自带笔记本电脑, đều đúng. Tất cả những người dự họp đều phải tự mang theo máy tính xách tay.",
         F(0, "Điểm khác thứ nhất. 凡是 nhấn mạnh một phạm vi đặc định, nên không thể đứng ngay trước một danh từ chung chung, mà chỉ đứng trước danh từ mang một tính chất riêng. Ví dụ: 凡是教师，都有国家认定的资格证书。 Phàm là giáo viên, đều có chứng chỉ do nhà nước công nhận. 教师 là một nhóm người có tính chất riêng, nên đúng."),
         F(0, "Nhưng câu 凡是东西都放在这里 thì sai, vì 东西 là danh từ quá chung chung, không có tính chất đặc định nào."),
         F(1, "Ngược lại, 所有 đứng trực tiếp trước danh từ chung chung được. Ví dụ: 所有东西都放在这里。 Tất cả đồ đạc đều để ở đây."),
         F(0, "Điểm khác thứ hai. 凡是 là phó từ, nên đứng được trước động từ. Ví dụ: 小王酷爱美术，市里凡是有画展，再远他也要去参观学习。 Tiểu Vương rất mê mỹ thuật, hễ trong thành phố có triển lãm tranh, dù xa mấy anh ấy cũng đi xem để học hỏi. Ở đây 凡是 đứng trước động từ 有."),
         F(1, "Còn 所有 là tính từ, chỉ bổ nghĩa cho danh từ, không đứng trước động từ. Ví dụ: 所有问题都解决了。 Tất cả vấn đề đều đã được giải quyết."),
         "Mẹo nhớ: 所有 giống chữ tất cả, chỉ đi với danh từ. Còn 凡是 giống chữ phàm là, hễ là: nhấn mạnh hễ thuộc phạm vi đó, có tính chất đó, thì đều như vậy, và đứng được trước động từ."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: Đúng hay sai?", reveal=True, size=34,
    items=["(1) 凡是建筑工人，一律都要穿工作服上班。",
           "Đáp án: Đúng – 建筑工人 là nhóm người có tính chất riêng.",
           "(2) 凡是人才，都要让他们有发挥自己才能的机会。",
           "Đáp án: Đúng – 人才 là người có tài, mang tính chất riêng.",
           "(3) 所有从那个地区来的人，都要接受检查。",
           "Đáp án: Đúng – 所有 bổ nghĩa cho danh từ 人.",
           "(4) 所有收到这个标题的邮件，请不要打开，已经证实这是个病毒。",
           "Đáp án: Sai – hễ nhận được thư có tiêu đề này: 凡是收到这个标题的邮件……"],
    say=[F(0, "Bây giờ chúng ta làm thử: phán đoán đúng sai. Câu một: 凡是建筑工人，一律都要穿工作服上班。 Phàm là công nhân xây dựng, đều phải mặc đồ bảo hộ đi làm. Đúng hay sai? Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: đúng. 建筑工人 là một nhóm người có tính chất riêng, nên dùng 凡是 được."),
         F(2, "Câu hai: 凡是人才，都要让他们有发挥自己才能的机会。 Phàm là nhân tài, đều phải cho họ cơ hội phát huy tài năng."),
         F(3, "Đáp án: đúng. 人才 là người có tài, mang tính chất riêng, không phải danh từ chung chung như 东西."),
         F(4, "Câu ba: 所有从那个地区来的人，都要接受检查。 Tất cả những người đến từ khu vực đó đều phải chịu kiểm tra."),
         F(5, "Đáp án: đúng. 所有 bổ nghĩa cho danh từ 人, phía trước có định ngữ 从那个地区来的."),
         F(6, "Câu bốn: 所有收到这个标题的邮件，请不要打开，已经证实这是个病毒。 Tất cả thư điện tử nhận được có tiêu đề này, xin đừng mở, đã xác thực đây là virus."),
         F(7, "Đáp án: sai. Câu này là lời dặn cho bất cứ lá thư nào có tiêu đề đó, kể cả những thư sẽ nhận sau này, tức là nghĩa hễ là, phàm là. Vì vậy nên dùng 凡是: 凡是收到这个标题的邮件，请不要打开。 Còn 所有 chỉ một tập hợp đã xác định, đã có sẵn.")])

# ======================= MỞ RỘNG: TỪ VỰNG ĐỊA LÝ =======================
add("bullets", chapter="Mở rộng: từ vựng địa lý", section="Mở rộng 扩展", title="Mở rộng 扩展: Từ vựng về địa lý (地理)", size=34,
    items=["## (1) 术语 – thuật ngữ",
           "边界 biên giới, ranh giới · 地势 địa thế, thế đất · 地质 địa chất · 经纬 kinh tuyến và vĩ tuyến",
           "## (2) 地貌 – địa mạo, dạng địa hình",
           "盆地 bồn địa, lòng chảo · 沼泽 đầm lầy · 海滨 bờ biển, miền duyên hải · 支流 nhánh sông, chi lưu · 坡 sườn dốc",
           "## (3) 分区 – phân vùng",
           "温带 ôn đới · 省会 thủ phủ tỉnh, tỉnh lỵ · 边疆 biên cương, vùng biên giới"],
    say=["Bây giờ chúng ta sang phần mở rộng của sách. Quyển Thượng không có mục tu từ riêng; bài này mở rộng một nhóm từ vựng về địa lý, tiếng Trung là 地理. Nhóm từ này rất hợp với bài khóa, vì bài khóa nhắc đến đất đai bao la, núi cao, hồ, suối, đồi.",
         F(0, "Sách chia các từ thành ba nhánh. Nhánh thứ nhất là 术语, tức là thuật ngữ."),
         F(1, "边界, biên giới, ranh giới giữa hai vùng. 地势, địa thế, tức là thế đất cao thấp. 地质, địa chất. Và 经纬, kinh vĩ, tức là kinh tuyến và vĩ tuyến trên bản đồ."),
         F(2, "Nhánh thứ hai là 地貌, địa mạo, tức là các dạng địa hình bề mặt."),
         F(3, "盆地, bồn địa, tức là vùng lòng chảo, xung quanh cao, ở giữa thấp. 沼泽, Hán Việt là chiểu trạch, tức là đầm lầy. 海滨, hải tân, bờ biển. 支流, chi lưu, nhánh sông đổ vào sông chính. Và 坡, sườn dốc, như 山坡, sườn núi."),
         F(4, "Nhánh thứ ba là 分区, phân vùng."),
         F(5, "温带, ôn đới. 省会, Hán Việt là tỉnh hội, tức là thủ phủ của một tỉnh, nơi đặt cơ quan chính quyền tỉnh. Và 边疆, biên cương, vùng đất xa ở biên giới.")])

add("bullets", section="Mở rộng 扩展", title="Từ địa lý trong bài khóa và một số lưu ý", size=36,
    items=["Trong bài: 辽阔的土地 · 高山 · 湖泊 · 小溪 · 丘陵 · 区域 · 中原 · 中亚 · 东南亚",
           "地势 (thế đất cao thấp) ≠ 地形 (hình dạng địa hình nói chung)",
           "盆地: 四川盆地 · 塔里木盆地 — 坡: 山坡 · 上坡 · 下坡",
           "省会: 成都是四川的省会 — tương đương thủ phủ tỉnh",
           "经纬: 经度 kinh độ + 纬度 vĩ độ"],
    say=[F(0, "Trước hết, hãy nhìn lại các từ địa lý trong bài khóa: 辽阔的土地，高山，湖泊，小溪，丘陵，区域，中原，中亚，东南亚. Chúng giúp tác giả vẽ ra bức tranh về nguồn nguyên liệu phong phú của ẩm thực Trung Hoa."),
         F(1, "Một lưu ý nhỏ: 地势 nhấn mạnh thế đất cao hay thấp, như 地势西高东低, địa thế phía tây cao, phía đông thấp. Còn 地形 là hình dạng địa hình nói chung."),
         F(2, "Với 盆地, Trung Quốc có những bồn địa nổi tiếng như 四川盆地 và 塔里木盆地. Với 坡, ta có 山坡, sườn núi; 上坡, lên dốc; và 下坡, xuống dốc."),
         F(3, "Với 省会, ví dụ: 成都是四川的省会。 Thành Đô là thủ phủ của tỉnh Tứ Xuyên."),
         F(4, "Còn 经纬 là gộp của 经度, kinh độ, và 纬度, vĩ độ. Bây giờ chúng ta luyện tập một chút nhé.")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chọn từ địa lý điền vào chỗ trống (1)", reveal=True, size=36,
    items=["## Từ cho sẵn: 盆地 · 省会 · 支流 · 温带 · 坡 · 经纬",
           "(1) 四川___四周是山，中间低平，物产非常丰富。",
           "Đáp án: 盆地",
           "(2) 成都是四川省的___，也是有名的美食之都。",
           "Đáp án: 省会",
           "(3) 长江有很多条___，汉江就是其中最长的一条。",
           "Đáp án: 支流"],
    say=[F(0, "Luyện tập: chọn từ thích hợp điền vào chỗ trống. Các từ cho sẵn là 盆地，省会，支流，温带，坡，经纬."),
         F(1, "Câu một: 四川什么四周是山，中间低平，物产非常丰富。 Xung quanh là núi, ở giữa thấp và bằng phẳng, sản vật rất phong phú. Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 盆地. 四川盆地四周是山，中间低平。 Xung quanh cao, ở giữa thấp, đó chính là đặc điểm của bồn địa."),
         F(3, "Câu hai: 成都是四川省的什么，也是有名的美食之都。 Thành Đô là cái gì của tỉnh Tứ Xuyên, và cũng là kinh đô ẩm thực nổi tiếng."),
         F(4, "Đáp án: 省会. 成都是四川省的省会。 Thành Đô là thủ phủ của tỉnh Tứ Xuyên."),
         F(5, "Câu ba: 长江有很多条什么，汉江就是其中最长的一条。 Trường Giang có rất nhiều cái gì, sông Hán là dài nhất trong số đó."),
         F(6, "Đáp án: 支流. 长江有很多条支流。 Trường Giang có rất nhiều nhánh sông. Chú ý lượng từ 条 đi với sông.")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chọn từ địa lý điền vào chỗ trống (2)", reveal=True, size=36,
    items=["(4) 中国大部分地区属于___，四季分明。",
           "Đáp án: 温带",
           "(5) 这条山路的___很陡，骑自行车上去非常吃力。",
           "Đáp án: 坡",
           "(6) 在地图上，用___线可以准确地确定一个地方的位置。",
           "Đáp án: 经纬"],
    say=[F(0, "Câu bốn: 中国大部分地区属于什么，四季分明。 Phần lớn lãnh thổ Trung Quốc thuộc vùng gì, bốn mùa rõ rệt."),
         F(1, "Đáp án: 温带. 中国大部分地区属于温带。 Phần lớn Trung Quốc thuộc vùng ôn đới."),
         F(2, "Câu năm: 这条山路的什么很陡，骑自行车上去非常吃力。 Cái gì của con đường núi này rất dốc, đạp xe lên rất vất vả."),
         F(3, "Đáp án: 坡. 这条山路的坡很陡。 Con dốc của đường núi này rất đứng. 陡 là dốc đứng."),
         F(4, "Câu sáu: 在地图上，用什么线可以准确地确定一个地方的位置。 Trên bản đồ, dùng đường gì có thể xác định chính xác vị trí của một nơi."),
         F(5, "Đáp án: 经纬. 用经纬线可以准确地确定一个地方的位置。 Dùng kinh tuyến và vĩ tuyến để xác định vị trí. Các bạn hãy thử dùng những từ này để giới thiệu địa lý quê hương mình bằng tiếng Trung nhé.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ có dấu chấm", size=40,
    items=["就餐 (餐) → 合餐 · 分餐 · 餐桌 · 餐厅",
           "优异 (优) → 优秀 · 优点 · 优势 · 优美",
           "品种 (种) → 种类 · 各种 · 物种 · 人种",
           "形态 (态) → 态度 · 状态 · 心态 · 姿态",
           "调料 (料) → 原料 · 材料 · 饮料 · 香料"],
    say=["Phần luyện tập. Bài tập một: mô phỏng ví dụ, viết thêm các từ có chứa chữ được đánh dấu chấm.",
         F(0, "Ví dụ mẫu: 就餐, chữ được đánh dấu là chữ thứ hai, chữ xan, nghĩa là bữa ăn. Ta có 合餐，分餐，餐桌，餐厅. Tức là ăn chung, ăn riêng, bàn ăn, và nhà hàng."),
         F(1, "优异, chữ được đánh dấu là chữ đầu, chữ ưu, nghĩa là tốt. Ta có 优秀，优点，优势，优美. Tức là ưu tú, ưu điểm, ưu thế, và đẹp đẽ."),
         F(2, "品种, chữ được đánh dấu là chữ thứ hai, đọc zhǒng, nghĩa là loại, giống. Ta có 种类，各种，物种，人种. Tức là chủng loại, các loại, giống loài, và chủng tộc."),
         F(3, "形态, chữ được đánh dấu là chữ thứ hai, chữ thái, nghĩa là dáng vẻ, trạng thái. Ta có 态度，状态，心态，姿态. Tức là thái độ, trạng thái, tâm thái, và tư thế."),
         F(4, "调料, chữ được đánh dấu là chữ thứ hai, chữ liệu, nghĩa là vật liệu. Ta có 原料，材料，饮料，香料. Tức là nguyên liệu, vật liệu, đồ uống, và hương liệu.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (1)", reveal=True, size=36,
    items=["(1) 她的变化太大了，我跟她面对面都没认出来。（以至）",
           "Đáp án: 她的变化太大了，以至我跟她面对面都没认出来。",
           "(2) 就是我们的工作取得了很大的成绩，也不能骄傲。（即便……也……）",
           "Đáp án: 即便我们的工作取得了很大的成绩，也不能骄傲。",
           "(3) 所有见过她的人，没有不称赞她漂亮的。（凡是）",
           "Đáp án: 凡是见过她的人，没有不称赞她漂亮的。"],
    say=[F(0, "Bài tập hai: dùng từ hoặc cấu trúc cho sẵn để viết lại câu. Câu một, dùng 以至: 她的变化太大了，我跟她面对面都没认出来。 Cô ấy thay đổi nhiều quá, tôi đứng đối diện mà cũng không nhận ra. Các bạn tạm dừng và thử viết lại nhé."),
         F(1, "Đáp án: 她的变化太大了，以至我跟她面对面都没认出来。 Cô ấy thay đổi nhiều đến nỗi tôi đứng đối diện mà không nhận ra."),
         F(2, "Câu hai, dùng 即便，也: 就是我们的工作取得了很大的成绩，也不能骄傲。 Cho dù công việc của chúng ta đạt được thành tích lớn, cũng không được kiêu ngạo."),
         F(3, "Đáp án: thay 就是 bằng 即便: 即便我们的工作取得了很大的成绩，也不能骄傲。 Ở đây 就是 là liên từ, nghĩa là cho dù, giống 即便."),
         F(4, "Câu ba, dùng 凡是: 所有见过她的人，没有不称赞她漂亮的。 Tất cả những người từng gặp cô ấy, không ai không khen cô ấy xinh đẹp."),
         F(5, "Đáp án: 凡是见过她的人，没有不称赞她漂亮的。 Hễ ai đã gặp cô ấy, không ai không khen cô ấy xinh. Câu phủ định hai lần 没有不 nghĩa là ai cũng.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (2)", reveal=True, size=36,
    items=["(4) 一个国家的希望都在青少年身上。（所在）",
           "Đáp án: 青少年是一个国家的希望所在。",
           "(5) 虽然不是上下班高峰期，这里还是堵车。（照样）",
           "Đáp án: 虽然不是上下班高峰期，这里照样堵车。",
           "(6) 他能取得这么好的成绩，是因为平时的勤学苦练。（得力于）",
           "Đáp án: 他能取得这么好的成绩，得力于平时的勤学苦练。"],
    say=[F(0, "Câu bốn, dùng 所在: 一个国家的希望都在青少年身上。 Hy vọng của một đất nước đều đặt ở thế hệ thanh thiếu niên."),
         F(1, "Đáp án: 青少年是一个国家的希望所在。 Thanh thiếu niên là niềm hy vọng của một đất nước. Nhớ cụm 希望所在."),
         F(2, "Câu năm, dùng 照样: 虽然不是上下班高峰期，这里还是堵车。 Tuy không phải giờ cao điểm, chỗ này vẫn tắc đường."),
         F(3, "Đáp án: 虽然不是上下班高峰期，这里照样堵车。 Tuy không phải giờ cao điểm, chỗ này vẫn tắc đường như thường. 照样 thay cho 还是."),
         F(4, "Câu sáu, dùng 得力于: 他能取得这么好的成绩，是因为平时的勤学苦练。 Anh ấy đạt được thành tích tốt như vậy, là vì ngày thường chăm chỉ học và khổ luyện."),
         F(5, "Đáp án: 他能取得这么好的成绩，得力于平时的勤学苦练。 Thành tích tốt như vậy là nhờ ngày thường chăm học khổ luyện. 得力于 thay cho 是因为, mang sắc thái tích cực: nhờ có điều tốt đó.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (1)", reveal=True, size=34,
    items=["## Từ cho sẵn: 正宗 · 凡是 · 烹饪 · 就餐 · 创新",
           "妈妈是个___高手，能做出各种各样的美味佳肴。不管多么普通的食材，只要经过妈妈的手，都能变成人间美味，___吃过的人没有不称赞的。妈妈是山东人，不但能做出___的传统鲁菜，更能___式地发明新的吃法，让我们全家人在___时，常常充满了惊喜。",
           "Đáp án: 烹饪 · 凡是 · 正宗 · 创新 · 就餐"],
    say=[F(0, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn một có năm từ: 正宗，凡是，烹饪，就餐，创新."),
         F(1, "妈妈是个什么高手，能做出各种各样的美味佳肴。不管多么普通的食材，只要经过妈妈的手，都能变成人间美味，什么吃过的人没有不称赞的。妈妈是山东人，不但能做出什么的传统鲁菜，更能什么式地发明新的吃法，让我们全家人在什么时，常常充满了惊喜。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 烹饪高手，凡是吃过的人，正宗的传统鲁菜，创新式地发明新的吃法，在就餐时。 Mẹ tôi là cao thủ nấu nướng, làm được đủ món ngon. Nguyên liệu bình thường đến mấy, qua tay mẹ cũng thành mỹ vị nhân gian, hễ ai ăn rồi cũng đều khen. Mẹ là người Sơn Đông, không những nấu được món Lỗ chính gốc, mà còn sáng tạo ra cách ăn mới, khiến cả nhà tôi mỗi bữa ăn đều đầy bất ngờ. 鲁菜 là ẩm thực Sơn Đông, một trong tám trường phái ẩm thực lớn của Trung Quốc.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (2)", reveal=True, size=34,
    items=["## Từ cho sẵn: 区域 · 局限 · 品种 · 辽阔 · 鲜明",
           "中国历史悠久，土地___，不同___、不同民族的饮食不但特色___，而且___丰富。比如：南方人爱吃米饭，北方人爱吃面食；山西人喜欢吃醋，四川人喜欢辣椒，等等。不过，随着各地人员流动的增加，这种___逐渐被打破了。在全国各地的大小城市，你都能吃到来自各处的各种美食。",
           "Đáp án: 辽阔 · 区域 · 鲜明 · 品种 · 局限"],
    say=[F(0, "Đoạn hai có năm từ: 区域，局限，品种，辽阔，鲜明."),
         F(1, "中国历史悠久，土地什么，不同什么、不同民族的饮食不但特色什么，而且什么丰富。比如：南方人爱吃米饭，北方人爱吃面食；山西人喜欢吃醋，四川人喜欢辣椒，等等。不过，随着各地人员流动的增加，这种什么逐渐被打破了。在全国各地的大小城市，你都能吃到来自各处的各种美食。 Các bạn điền thử nhé."),
         F(2, "Đáp án: 土地辽阔，不同区域，特色鲜明，品种丰富，这种局限逐渐被打破了。 Trung Quốc lịch sử lâu đời, đất đai bao la, ẩm thực của các vùng, các dân tộc khác nhau không những đặc sắc rõ nét mà còn phong phú về chủng loại. Người miền Nam thích cơm, người miền Bắc thích đồ bột mì; người Sơn Tây thích giấm, người Tứ Xuyên thích ớt. Nhưng khi người dân di chuyển giữa các vùng nhiều hơn, giới hạn ấy dần bị phá vỡ. Chú ý: 打破局限 là một kết hợp từ chúng ta đã gặp trong bài khóa.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 4: Đọc đoạn văn, mô phỏng đặt câu", reveal=True, size=32,
    items=["中国的饮食文化历经数千年，始终具有魅力，是因为它不仅民族特性鲜明，而且善于吸收……的优异之处，以至辉煌至今。",
           "Đáp án: 他们两个人结婚三十多年，始终相亲相爱，是因为他们不仅性格互补，而且懂得互相理解、互相包容，以至感情越来越深。",
           "在食材栽培方面，中华饮食坚持以本国物产为基本原料，同时合理引进、培育外来品种，比如咖啡、柠檬、芒果等，凡是……",
           "Đáp án: 在学习汉语方面，我坚持每天读课文、记生词，同时多跟中国朋友交流，比如一起聊天、看电影等，凡是学过的词语，我都尽量在生活中用起来。"],
    say=[F(0, "Bài tập bốn: đọc đoạn văn, rồi mô phỏng để đặt câu. Câu mẫu một lấy từ bài khóa, với khung 始终，是因为，不仅，而且，以至. Đề bài cho sẵn phần đầu: 他们两个人结婚三十多年，始终相亲相爱，是因为他们不仅…… Hai người họ kết hôn hơn ba mươi năm, luôn yêu thương nhau, là vì họ không những… Các bạn thử viết tiếp nhé."),
         F(1, "Đáp án gợi ý: 是因为他们不仅性格互补，而且懂得互相理解、互相包容，以至感情越来越深。 Là vì họ không những tính cách bổ sung cho nhau, mà còn biết thông cảm và bao dung lẫn nhau, đến mức tình cảm ngày càng sâu đậm."),
         F(2, "Câu mẫu hai, với khung 坚持，同时，比如，凡是. Đề bài: 在学习汉语方面，我坚持…… Về mặt học tiếng Trung, tôi kiên trì…"),
         F(3, "Đáp án gợi ý: 在学习汉语方面，我坚持每天读课文、记生词，同时多跟中国朋友交流，比如一起聊天、看电影等，凡是学过的词语，我都尽量在生活中用起来。 Về mặt học tiếng Trung, tôi kiên trì mỗi ngày đọc bài khóa, nhớ từ mới, đồng thời giao lưu nhiều với bạn Trung Quốc, ví dụ cùng trò chuyện, xem phim; phàm là từ đã học, tôi đều cố gắng dùng trong cuộc sống. Các bạn hãy viết câu của riêng mình nhé.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 10", size=34,
    items=["Từ vựng trọng tâm: 视野 · 蕴藏 · 鲜明 · 辉煌 · 和谐 · 精心 · 烹饪 · 认可 · 照样 · 得力 · 灵感 · 排斥 · 局限 · 奥秘",
           "Ngữ pháp: 以至 (đến nỗi, đến mức) · 即便 (cho dù) · 所在 (chỗ, nơi tồn tại)",
           "Phân biệt: 凡是 (phạm vi đặc định; đứng được trước động từ) ≠ 所有 (trước danh từ chung chung; không đứng trước động từ)",
           "Mở rộng: từ vựng địa lý – 边界 · 地势 · 盆地 · 沼泽 · 支流 · 温带 · 省会 · 边疆",
           "## Bài tập về nhà (运用)",
           "Dựa vào bài tập 5, viết tóm tắt bài khóa khoảng 300 chữ: lịch sử phát triển, nguyên liệu, cách dùng bữa"],
    say=["Chúng ta cùng tổng kết bài mười.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 视野，蕴藏，鲜明，辉煌，和谐，精心，烹饪，认可，照样，得力，灵感，排斥，局限，奥秘. Và đừng quên những từ dễ nhầm như 灵感 là cảm hứng chứ không phải linh cảm, 得力于 là nhờ vào."),
         F(1, "Về ngữ pháp: 以至 đứng đầu vế sau, nghĩa là đến nỗi, đến mức. 即便 nghĩa là cho dù, vế sau thường có 也. 所在 là danh từ văn viết, chỉ chỗ, nơi tồn tại, như 问题所在，奥秘所在."),
         F(2, "Về phân biệt từ: 凡是 nhấn mạnh một phạm vi đặc định, chỉ đứng trước danh từ có tính chất riêng, và đứng được trước động từ; còn 所有 đứng thẳng trước danh từ chung chung, nhưng không đứng trước động từ."),
         F(3, "Về phần mở rộng: các bạn đã làm quen với những từ địa lý như 边界，地势，盆地，沼泽，支流，温带，省会，边疆."),
         F(5, "Bài tập về nhà, theo phần vận dụng của sách: bài khóa giới thiệu văn hóa ẩm thực Trung Hoa từ lịch sử phát triển, việc trồng trọt và lựa chọn nguyên liệu, đến cách dùng bữa. Hãy dựa vào bài tập năm, viết tóm tắt bài khóa thành một đoạn văn khoảng ba trăm chữ. Nhớ thử dùng 以至，即便，所在，凡是 trong bài viết nhé."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Lần tới khi ăn một món Trung Hoa, các bạn hãy thử đoán xem nguyên liệu nào là bản địa, nguyên liệu nào mang thân phận ngoại quốc nhé. Hẹn gặp lại các bạn ở bài mười một: 我不在时，猫在干什么, Các chú mèo làm gì khi tôi đi vắng? Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Thượng) – Bài 10: 全球化视野中的中国饮食 (Thức ăn Trung Quốc trong xu thế toàn cầu hóa)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"调和": "条和",            # tiáohé
                    "调料": "条料",            # tiáoliào
                    "种植": "众植",            # zhòngzhí
                    "湖泊": "湖坡",            # húpō
                    "尽享": "进享",            # jìnxiǎng
                    "尽心尽力": "进心进力",    # jìnxīn jìnlì
                    "仅为": "仅维",            # jǐn wéi (仅仅为饮食, 仅为一餐)
                    "为基本原料": "维基本原料",  # wéi
                    "变为": "变维",            # biànwéi
                    "为之": "位之",            # wèizhī
                    "当成": "荡成",            # dàngchéng
                    "南北朝": "南北潮",        # cháo
                    "纪伯伦": "记伯伦",        # Jìbólún
                    "长得": "掌得",            # zhǎng de
                    "折": "哲",                # zhé (mọi chữ 折 trong bài đều đọc zhé)
                    "干什么": "赣什么"},       # gàn shénme
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai10.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
