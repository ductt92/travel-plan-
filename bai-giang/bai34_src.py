#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Hạ) – Bài 34 «为文物而生的人». Chạy để sinh bai34.json."""
import json
import os

TAG = "HSK 6 (Hạ) · Bài 34 · 为文物而生的人"
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
    top="Giáo trình chuẩn HSK 6 – Quyển Hạ",
    zh="为文物而生的人", py="Wèi wénwù ér shēng de rén", vi="Bài 34: Người sinh ra vì cổ vật",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Hạ.",
         "Hôm nay chúng ta học bài ba mươi tư: 为文物而生的人。 Nghĩa là: Người sinh ra vì cổ vật.",
         "Bài này thuộc Đơn vị chín, chủ đề 古今博览, tức là nhìn rộng xưa nay. Bài khóa kể về một con người có thật: nhà sưu tầm, nhà giám định gốm sứ cổ nổi tiếng 孙瀛洲, người đã hiến tặng hơn ba nghìn món cổ vật quý cho Bảo tàng Cố Cung, và dành cả đời để bảo vệ văn hóa dân tộc."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu nội dung bài khóa 为文物而生的人 – cuộc đời và nghĩa cử của 孙瀛洲",
           "Nắm vững 51 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: liên từ 尚且 và giới từ 当 (当年、当时、当代)",
           "Phân biệt hai tính từ 温和 và 温柔",
           "Kỹ năng viết: chuyển ý, nối đoạn (过渡)"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa: 孙瀛洲 là ai, ông đã làm gì, và vì sao người ta gọi ông là một bậc thầy thực thụ."),
         F(1, "Thứ hai, nắm vững năm mươi mốt từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học hai điểm ngữ pháp: liên từ 尚且, nghĩa là còn, đến cả… còn; và giới từ dāng, nghĩa là đang, ngay lúc đó, nơi đó, như trong các từ 当年，当时，当代."),
         F(3, "Thứ tư, phân biệt hai tính từ rất gần nghĩa: 温和 và 温柔."),
         F(4, "Thứ năm, một kỹ năng viết quan trọng: chuyển ý, nối đoạn, tiếng Trung gọi là 过渡, giúp bài văn liền mạch thành một khối."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Câu hỏi khởi động", size=40,
    items=["请对照图片熟悉下列物品的名称，并说一说你在哪儿见过这些东西。",
           "斗彩 (dòucǎi) – sứ đấu thái: vẽ màu lam dưới men, rồi tô màu trên men",
           "糖葫芦 (tánghúlu) – kẹo hồ lô: quả sơn tra xiên que, phủ đường",
           "陶瓷 (táocí) – gốm sứ",
           "古玩 (gǔwán) – đồ cổ để thưởng ngoạn",
           "你在哪儿见过这些东西？ – Bạn đã thấy những thứ này ở đâu?"],
    say=["Chúng ta bắt đầu bằng phần khởi động. Sách yêu cầu như sau.",
         F(0, "请对照图片熟悉下列物品的名称，并说一说你在哪儿见过这些东西。 Hãy đối chiếu với hình ảnh để làm quen với tên gọi của các đồ vật sau, và nói xem bạn đã thấy chúng ở đâu."),
         F(1, "Thứ nhất: 斗彩。 Đây là một loại đồ sứ quý. Người thợ vẽ đường viền màu lam dưới lớp men, nung lên, rồi tô thêm các màu khác trên men và nung lần nữa. Các màu sắc như đua nhau khoe sắc. Theo chú thích của sách, loại sứ này còn gọi là 逗彩, rất ít món còn lưu truyền đến nay."),
         F(2, "Thứ hai: 糖葫芦, kẹo hồ lô. Đó là những quả sơn tra xiên thành chuỗi rồi phủ một lớp đường, món ăn vặt mùa đông nổi tiếng của Bắc Kinh. Trong bài khóa, kẹo hồ lô cho con ăn ngày Tết đều do 孙瀛洲 tự làm."),
         F(3, "Thứ ba: 陶瓷, gốm sứ."),
         F(4, "Thứ tư: 古玩, đồ cổ để thưởng ngoạn, sưu tầm. 古玩店 là tiệm đồ cổ."),
         F(5, "你在哪儿见过这些东西？ Bạn đã thấy những thứ này ở đâu? Ví dụ: 我在博物馆里见过斗彩瓷器。 Tôi đã thấy đồ sứ đấu thái trong bảo tàng. Các bạn hãy tạm dừng video và thử trả lời bằng tiếng Trung nhé.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 衣 và 家", size=36,
    items=["## 衣 (y): áo, quần áo",
           "衣着 cách ăn mặc · 衣服 quần áo · 衣柜 tủ quần áo · 衣架 móc áo · 衣领 cổ áo · 衣物 quần áo, đồ dùng",
           "大衣 áo khoác dài · 衬衣 áo sơ mi · 风衣 áo gió, măng tô · 毛衣 áo len · 上衣 áo · 睡衣 đồ ngủ · 外衣 áo ngoài",
           "## 家 (gia): người chuyên về một lĩnh vực",
           "收藏家 nhà sưu tầm · 鉴定家 nhà giám định · 科学家 nhà khoa học · 艺术家 nghệ sĩ · 画家 họa sĩ · 作家 nhà văn",
           "文学家 nhà văn học · 政治家 chính trị gia · 音乐家 nhạc sĩ · 名家 danh gia · 专家 chuyên gia · 大家 bậc thầy"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo, rất có lợi cho người Việt vì hầu hết các chữ đều có âm Hán Việt quen thuộc.",
         F(0, "Nhóm thứ nhất có yếu tố y, nghĩa là áo, quần áo, như trong từ 衣服."),
         F(1, "衣着，衣服，衣柜，衣架，衣领，衣物。 Tức là: cách ăn mặc, quần áo, tủ quần áo, móc áo, cổ áo, và quần áo đồ dùng nói chung. Từ 衣着 có trong câu mở đầu bài khóa: 衣着朴素, ăn mặc giản dị. Chú ý chữ sau trong 衣着 đọc là zhuó."),
         F(2, "大衣，衬衣，风衣，毛衣，上衣，睡衣，外衣。 Tức là: áo khoác dài, áo sơ mi, áo gió, áo len, áo, đồ ngủ, và áo ngoài."),
         F(3, "Nhóm thứ hai có yếu tố gia, đứng cuối từ, chỉ người chuyên về một lĩnh vực, giống chữ nhà trong nhà văn, nhà khoa học."),
         F(4, "收藏家，鉴定家，科学家，艺术家，画家，作家。 Tức là: nhà sưu tầm, nhà giám định, nhà khoa học, nghệ sĩ, họa sĩ, nhà văn. Bài khóa giới thiệu 孙瀛洲 là 古陶瓷收藏家、鉴定家, nhà sưu tầm và nhà giám định gốm sứ cổ."),
         F(5, "文学家，政治家，音乐家，名家，专家，大家。 Tức là: nhà văn học, chính trị gia, nhạc sĩ, danh gia, chuyên gia, và bậc thầy. Chú ý từ 大家 ở đây không phải là mọi người, mà là bậc thầy lớn. Cuối bài khóa, tác giả gọi 孙瀛洲 là một 大家 như vậy.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 册 và 丰", size=36,
    items=["## 册 (sách): sổ, quyển, tập",
           "造册 lập sổ · 注册 đăng ký · 表册 sổ bảng biểu · 分册 tập (của bộ sách) · 画册 tập tranh · 名册 danh sách",
           "史册 sử sách · 手册 sổ tay · 书册 sách vở · 账册 sổ sách kế toán · 纪念册 sổ lưu niệm · 册子 cuốn sổ",
           "## 丰 (phong): nhiều, dồi dào, sung túc",
           "丰厚 dồi dào, hậu hĩnh · 丰产 năng suất cao · 丰富 phong phú · 丰满 đầy đặn · 丰茂 tươi tốt · 丰年 năm được mùa",
           "丰盛 thịnh soạn · 丰收 bội thu · 丰硕 (thành quả) to lớn · 丰足 đầy đủ · 丰裕 sung túc · 丰衣足食 cơm no áo ấm · 五谷丰登 ngũ cốc được mùa"],
    say=[F(0, "Nhóm thứ ba có chữ 册, Hán Việt là sách, nghĩa là sổ, quyển, tập."),
         F(1, "造册，注册，表册，分册，画册，名册。 Tức là: lập sổ, đăng ký, sổ bảng biểu, một tập của bộ sách, tập tranh, danh sách. Trong bài khóa có cụm 登记造册, ghi chép, lập sổ các cổ vật được hiến tặng."),
         F(2, "史册，手册，书册，账册，纪念册，册子。 Tức là: sử sách, sổ tay, sách vở, sổ sách kế toán, sổ lưu niệm, và cuốn sổ."),
         F(3, "Nhóm cuối cùng có chữ 丰, Hán Việt là phong, như trong phong phú, nghĩa là nhiều, dồi dào."),
         F(4, "丰厚，丰产，丰富，丰满，丰茂，丰年。 Tức là: dồi dào hậu hĩnh, năng suất cao, phong phú, đầy đặn, tươi tốt, năm được mùa. Bài khóa có câu 家藏竟然如此丰厚, đồ cất giữ trong nhà lại phong phú đến thế."),
         F(5, "丰盛，丰收，丰硕，丰足，丰裕，丰衣足食，五谷丰登。 Tức là: thịnh soạn, bội thu, thành quả to lớn, đầy đủ, sung túc, cơm no áo ấm, và ngũ cốc được mùa. Hai thành ngữ cuối là những lời chúc Tết rất quen thuộc."),
         "Các bạn thấy không, chỉ cần nắm nghĩa của một chữ gốc, ta có thể đoán được nghĩa của cả một nhóm từ."])

add("bullets", section="Khởi động 热身", title="Nhân vật trong bài: 孙瀛洲 (1893–1966)", size=38,
    items=["孙瀛洲 Sūn Yíngzhōu – chuyên gia giám định gốm sứ cổ nổi tiếng của Trung Quốc, quê Hà Bắc",
           "13 tuổi lên Bắc Kinh học việc ở tiệm đồ cổ · năm 1923 tự mở tiệm đồ cổ riêng",
           "Năm 1956: hiến tặng hơn 3000 món cổ vật cho Bảo tàng Cố Cung (故宫博物院)",
           "Món nổi tiếng nhất: chén 斗彩三秋杯 đời Minh, niên hiệu Thành Hóa",
           "Cùng năm vào Cố Cung làm nghiên cứu, giám định; đào tạo nhiều học trò như 耿宝昌",
           "故宫 = Tử Cấm Thành, cung điện của hoàng đế hai triều Minh, Thanh"],
    say=["Trước khi học từ mới, thầy giới thiệu đôi nét về nhân vật chính, vì đây là một người có thật.",
         F(0, "孙瀛洲, sinh năm một nghìn tám trăm chín mươi ba, mất năm một nghìn chín trăm sáu mươi sáu. Theo chú thích của sách, ông là chuyên gia giám định gốm sứ cổ nổi tiếng của Trung Quốc. Quê ông ở tỉnh Hà Bắc."),
         F(1, "Năm mười ba tuổi, ông lên Bắc Kinh học việc ở tiệm đồ cổ. Đến năm một nghìn chín trăm hai mươi ba, ông tự mở tiệm đồ cổ của riêng mình và trở thành người có uy tín trong giới buôn bán đồ cổ."),
         F(2, "Năm một nghìn chín trăm năm mươi sáu, ông hiến tặng không hơn ba nghìn món cổ vật cho Bảo tàng Cố Cung, tiếng Trung là 故宫博物院."),
         F(3, "Món nổi tiếng nhất là chiếc chén 斗彩三秋杯 đời nhà Minh, thời vua Thành Hóa. Tên chén có hai chữ tam thu, tức ba tháng mùa thu, vì trên chén vẽ cảnh bướm bay giữa hoa cỏ và đá núi mùa thu."),
         F(4, "Cũng trong năm đó, ông được mời vào Cố Cung làm công tác nghiên cứu và giám định gốm sứ cổ. Ông đào tạo nhiều học trò, trong đó có 耿宝昌, sau này trở thành bậc thầy hàng đầu trong ngành giám định gốm sứ."),
         F(5, "Còn 故宫, tức Cố Cung, chính là Tử Cấm Thành ở Bắc Kinh, cung điện của các hoàng đế hai triều Minh và Thanh, nay là một trong những bảo tàng lớn nhất thế giới.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng)
V = [
    ("霞", "xiá", "hà", "danh từ", "ráng (mây hồng lúc bình minh, hoàng hôn)", "清晨，朝霞铺满了天空。", "Sáng sớm, ráng hồng phủ kín bầu trời.",
     "Danh từ, chỉ ráng mây, những đám mây được mặt trời nhuộm đỏ lúc bình minh hay hoàng hôn. 朝霞 là ráng sáng, 晚霞 là ráng chiều. Chú ý: 朝霞 đọc là zhāoxiá, chữ đầu thanh một, nghĩa là buổi sáng."),
    ("朴素", "pǔsù", "phác tố", "tính từ", "giản dị, mộc mạc", "她穿得很朴素。", "Cô ấy ăn mặc rất giản dị.",
     "Tính từ, nghĩa là giản dị, mộc mạc, không cầu kỳ. Chữ đầu Hán Việt là phác, như trong chất phác. Trong bài: 衣着朴素, ăn mặc giản dị."),
    ("温和", "wēnhé", "ôn hòa", "tính từ", "ôn hòa, hiền hòa; (khí hậu) ôn hòa", "他性情温和，从来不发脾气。", "Ông ấy tính tình ôn hòa, chưa bao giờ nổi nóng.",
     "Tính từ, chỉ tính tình, thái độ hiền hòa, nhã nhặn; cũng chỉ khí hậu không nóng không lạnh. Trong bài: 性情温和, tính tình ôn hòa. Lát nữa ta sẽ phân biệt từ này với 温柔."),
    ("颠簸", "diānbǒ", "điên bá", "động từ", "xóc nảy, lắc lư (xe, thuyền)", "汽车在山路上颠簸了三个小时。", "Xe ô tô xóc nảy trên đường núi suốt ba tiếng.",
     "Động từ, chỉ xe cộ, tàu thuyền rung lắc, xóc nảy lên xuống. Trong bài: 一路颠簸的公共汽车, chiếc xe buýt xóc nảy suốt dọc đường. Chú ý chữ sau đọc thanh ba: bǒ."),
    ("巷", "xiàng", "hạng", "danh từ", "ngõ, hẻm", "他走过熟悉的大街小巷。", "Ông đi qua những con phố, ngõ hẻm quen thuộc.",
     "Danh từ, nghĩa là ngõ, hẻm. Cụm 大街小巷 nghĩa là phố lớn ngõ nhỏ, khắp mọi nơi. Ở Bắc Kinh, ngõ nhỏ còn gọi là 胡同."),
    ("陶瓷", "táocí", "đào từ", "danh từ", "gốm sứ", "景德镇的陶瓷闻名世界。", "Gốm sứ Cảnh Đức Trấn nổi tiếng thế giới.",
     "Danh từ, gồm hai chữ: chữ đầu là đồ gốm, chữ sau là đồ sứ, ghép lại là gốm sứ. 古陶瓷 là gốm sứ cổ."),
    ("收藏", "shōucáng", "thu tàng", "động từ", "sưu tầm, sưu tập và cất giữ", "他收藏了很多古代字画。", "Ông ấy sưu tầm rất nhiều thư họa cổ.",
     "Động từ, nghĩa là sưu tầm và cất giữ. 收藏家 là nhà sưu tầm. Chú ý chữ sau đọc là cáng, thanh hai."),
    ("鉴定", "jiàndìng", "giám định", "động từ", "giám định, thẩm định (thật giả, chất lượng)", "专家鉴定这件瓷器是真品。", "Chuyên gia giám định chiếc đồ sứ này là đồ thật.",
     "Động từ, giống hệt tiếng Việt giám định: xem xét để xác định thật giả, chất lượng. 鉴定家 là nhà giám định."),
    ("无偿", "wúcháng", "vô thường", "tính từ", "không lấy tiền, không hoàn lại, miễn phí", "他把房子无偿送给了学校。", "Ông ấy tặng không ngôi nhà cho trường học.",
     "Tính từ, nghĩa là không đòi trả công, không lấy tiền. Chữ sau là thường trong bồi thường. Cẩn thận từ dễ nhầm: vô thường trong tiếng Việt là không bền vững, như đời người vô thường, đó là một từ khác hẳn. 无偿献血 là hiến máu tình nguyện."),
    ("赠送", "zèngsòng", "tặng tống", "động từ", "tặng, biếu", "公司赠送给每位顾客一份小礼物。", "Công ty tặng mỗi khách hàng một món quà nhỏ.",
     "Động từ, nghĩa là tặng, biếu, trang trọng hơn 送."),
    ("络绎不绝", "luòyì bù jué", "lạc dịch bất tuyệt", "thành ngữ", "(người, xe) nối nhau không dứt, tấp nập", "来参观的游客络绎不绝。", "Du khách đến tham quan nối nhau không dứt.",
     "Thành ngữ, chỉ người, xe qua lại liên tục, không ngớt. Nó gần nghĩa với 川流不息 mà ta đã học ở bài hai mươi mốt."),
    ("文物", "wénwù", "văn vật", "danh từ", "cổ vật, di vật văn hóa, lịch sử", "这些文物都是国家的宝贵财富。", "Những cổ vật này đều là tài sản quý báu của quốc gia.",
     "Danh từ, chỉ các di vật văn hóa, lịch sử như đồ gốm, thư họa, đồ đồng. Chú ý: văn vật trong tiếng Việt thường chỉ nền văn hiến, như Thăng Long nghìn năm văn vật; còn 文物 là những cổ vật cụ thể. Đây là từ khóa của tên bài."),
    ("同志", "tóngzhì", "đồng chí", "danh từ", "đồng chí; (cách gọi) cán bộ, nhân viên", "故宫的同志明天来打包装箱。", "Cán bộ của Cố Cung ngày mai sẽ đến đóng gói vào thùng.",
     "Danh từ, nghĩa là đồng chí. Trong bài, 故宫的同志 là cách gọi các cán bộ, nhân viên của Bảo tàng Cố Cung, cách nói phổ biến ở Trung Quốc thời đó. Ngày nay người ta ít dùng từ này để xưng hô với người lạ."),
    ("打包", "dǎ bāo", "đả bao", "động từ", "đóng gói; gói (đồ ăn) mang về", "我们把衣服打包寄回家了。", "Chúng tôi đóng gói quần áo gửi về nhà.",
     "Động từ, nghĩa là đóng gói. Trong nhà hàng, 打包 còn là gói đồ ăn thừa mang về. Đây là từ ly hợp, có thể nói 打个包."),
    ("搭配", "dāpèi", "đáp phối", "động từ", "phối hợp, kết hợp (cho hài hòa)", "这条裙子和那双鞋搭配得很好看。", "Chiếc váy này phối với đôi giày kia rất đẹp.",
     "Động từ, nghĩa là phối hợp cho hài hòa, như phối đồ, phối màu. Trong học tiếng, 词语搭配 là cách kết hợp từ."),
    ("图案", "tú'àn", "đồ án", "danh từ", "hoa văn, họa tiết", "瓷杯上的图案是两只蝴蝶。", "Họa tiết trên chiếc chén sứ là hai con bướm.",
     "Danh từ, nghĩa là hoa văn, họa tiết trang trí. Cẩn thận từ dễ nhầm: đồ án trong tiếng Việt là bản thiết kế, bài làm lớn như đồ án tốt nghiệp; còn 图案 là hoa văn."),
    ("皇帝", "huángdì", "hoàng đế", "danh từ", "hoàng đế, vua", "这对杯子是皇帝下旨烧制的。", "Đôi chén này do hoàng đế hạ chỉ cho nung.",
     "Danh từ, giống hệt tiếng Việt hoàng đế."),
    ("皇后", "huánghòu", "hoàng hậu", "danh từ", "hoàng hậu (vợ chính của vua)", "皇后是皇帝的正妻。", "Hoàng hậu là vợ chính của hoàng đế.",
     "Danh từ, nghĩa là hoàng hậu. Theo chú thích của sách, 妃 là những người vợ khác của vua ngoài hoàng hậu, còn 爱妃 là phi tần được vua sủng ái."),
    ("销毁", "xiāohuǐ", "tiêu hủy", "động từ", "tiêu hủy (đốt, nấu chảy)", "警察把这些假货全部销毁了。", "Cảnh sát đã tiêu hủy toàn bộ chỗ hàng giả này.",
     "Động từ, nghĩa là tiêu hủy bằng cách đốt hoặc nấu chảy, giống tiếng Việt."),
    ("手艺", "shǒuyì", "thủ nghệ", "danh từ", "tay nghề, nghề thủ công", "他做菜的手艺很好。", "Tay nghề nấu ăn của anh ấy rất giỏi.",
     "Danh từ, nghĩa là tay nghề, kỹ năng làm thủ công. 手艺人 là người thợ thủ công, nghệ nhân."),
    ("凝聚", "níngjù", "ngưng tụ", "động từ", "ngưng tụ; kết tinh, chứa đựng; gắn kết", "这部作品凝聚着作者多年的心血。", "Tác phẩm này chứa đựng tâm huyết nhiều năm của tác giả.",
     "Động từ. Nghĩa gốc là ngưng tụ, như hơi nước ngưng lại. Nghĩa bóng hay gặp hơn: kết tinh, chứa đựng, hoặc gắn kết. 凝聚力 là sức gắn kết. Tiếng Việt ngưng tụ chủ yếu dùng trong vật lý, nên khi dịch nghĩa bóng hãy dùng chứa đựng, hội tụ."),
    ("结晶", "jiéjīng", "kết tinh", "danh từ", "sự kết tinh, thành quả", "这项发明是大家智慧的结晶。", "Phát minh này là kết tinh trí tuệ của mọi người.",
     "Danh từ, giống tiếng Việt kết tinh, vừa là tinh thể, vừa là thành quả quý giá. 智慧的结晶 là kết tinh của trí tuệ."),
    ("籍贯", "jíguàn", "tịch quán", "danh từ", "quê quán, nguyên quán", "他的籍贯是河北。", "Quê quán của ông ấy là Hà Bắc.",
     "Danh từ, chỉ nơi gốc gác của tổ tiên hoặc nơi sinh. Tiếng Việt nói quê quán, nguyên quán. Trên các tờ khai ở Trung Quốc thường có mục 籍贯."),
    ("采购", "cǎigòu", "thái cấu", "danh từ", "việc thu mua; người thu mua", "他在公司负责采购。", "Anh ấy phụ trách thu mua ở công ty.",
     "Sách ghi là danh từ: việc thu mua, hoặc người làm công việc thu mua. Từ này cũng dùng như động từ: 采购原料, thu mua nguyên liệu."),
    ("创业", "chuàngyè", "sáng nghiệp", "động từ", "khởi nghiệp, gây dựng sự nghiệp", "大学毕业后，他回老家创业了。", "Tốt nghiệp đại học xong, anh ấy về quê khởi nghiệp.",
     "Động từ, nghĩa là gây dựng sự nghiệp, tiếng Việt hiện đại nói là khởi nghiệp. Chú ý chữ đầu đọc thanh bốn: chuàng."),
    ("威望", "wēiwàng", "uy vọng", "danh từ", "uy tín và danh vọng", "他在业内很有威望。", "Ông ấy rất có uy tín trong ngành.",
     "Danh từ, chỉ danh tiếng và uy tín khiến người khác kính phục. Lát nữa ta sẽ gặp 威信, một từ gần nghĩa."),
    ("吝啬", "lìnsè", "lận sắc", "tính từ", "keo kiệt, bủn xỉn", "他很吝啬，连一分钱都舍不得花。", "Anh ta rất keo kiệt, đến một xu cũng không nỡ tiêu.",
     "Tính từ, nghĩa là keo kiệt, bủn xỉn, mang nghĩa xấu. Trong bài, con gái kể bố tiết kiệm đến mức 甚至有些吝啬, thậm chí hơi keo kiệt; đây là cách nói đùa đầy yêu thương."),
    ("尚且", "shàngqiě", "thượng thả", "liên từ", "còn, đến… còn (huống chi…)", "这道题老师尚且不会做，何况学生呢？", "Bài này thầy giáo còn không làm được, huống chi học sinh?",
     "Liên từ, nghĩa là còn, đến cả… còn, thường đi với 何况 ở vế sau. Đây là điểm ngữ pháp trọng tâm, ta sẽ học kỹ ở phần sau."),
    ("不惜", "bùxī", "bất tích", "động từ", "không tiếc, sẵn sàng bỏ ra", "为了治好孩子的病，他们不惜花光所有积蓄。", "Để chữa bệnh cho con, họ không tiếc tiêu hết mọi khoản tiết kiệm.",
     "Động từ, nghĩa là không tiếc, sẵn sàng bỏ ra cái giá lớn để đạt mục đích. 不惜重金 là không tiếc tiền lớn; 不惜一切代价 là bằng mọi giá."),
    ("可观", "kěguān", "khả quan", "tính từ", "đáng kể, khá lớn (số lượng)", "这家公司去年的收入相当可观。", "Thu nhập năm ngoái của công ty này khá lớn.",
     "Tính từ. Đây là từ rất dễ nhầm! Khả quan trong tiếng Việt là có triển vọng tốt; còn 可观 nghĩa là đáng kể, khá lớn, thường nói về số lượng, con số. Trong bài: 数量可观, số lượng đáng kể."),
    ("神圣", "shénshèng", "thần thánh", "tính từ", "thiêng liêng", "保卫祖国是每个公民神圣的义务。", "Bảo vệ Tổ quốc là nghĩa vụ thiêng liêng của mỗi công dân.",
     "Tính từ. Cũng là từ dễ nhầm: thần thánh trong tiếng Việt thường chỉ các vị thần; còn 神圣 là tính từ, nghĩa là thiêng liêng. 神圣的使命 là sứ mệnh thiêng liêng."),
    ("使命", "shǐmìng", "sứ mệnh", "danh từ", "sứ mệnh", "保护文物是他一生的使命。", "Bảo vệ cổ vật là sứ mệnh cả đời của ông.",
     "Danh từ, giống hệt tiếng Việt sứ mệnh."),
    ("看待", "kàndài", "khán đãi", "động từ", "nhìn nhận, đối xử, coi (như)", "你怎样看待这个问题？", "Bạn nhìn nhận vấn đề này như thế nào?",
     "Động từ, nghĩa là nhìn nhận, đánh giá, hoặc đối xử với ai đó. Trong bài: 怎样看待当年父亲捐赠的义举, nhìn nhận thế nào về nghĩa cử hiến tặng năm xưa của bố."),
    ("家属", "jiāshǔ", "gia thuộc", "danh từ", "người nhà, gia quyến", "医生正在和病人家属谈话。", "Bác sĩ đang nói chuyện với người nhà bệnh nhân.",
     "Danh từ, chỉ người nhà, thành viên gia đình của một người nào đó, như 病人家属, người nhà bệnh nhân."),
    ("拥护", "yōnghù", "ủng hộ", "động từ", "ủng hộ, tán thành", "大家都拥护这个决定。", "Mọi người đều ủng hộ quyết định này.",
     "Động từ. Âm Hán Việt giống ủng hộ, nhưng 拥护 thường dùng cho chính sách, quyết định, lãnh đạo, sắc thái trang trọng. Ủng hộ thông thường hay dịch là 支持; còn ủng hộ theo nghĩa quyên góp tiền thì tiếng Trung là 捐款."),
    ("表彰", "biǎozhāng", "biểu chương", "động từ", "biểu dương, tuyên dương", "学校表彰了一批优秀教师。", "Nhà trường đã tuyên dương một loạt giáo viên ưu tú.",
     "Động từ, nghĩa là khen ngợi công khai một cách trang trọng, tiếng Việt nói biểu dương, tuyên dương."),
    ("荣誉", "róngyù", "vinh dự", "danh từ", "vinh dự, vinh quang", "能代表国家参加比赛是我的荣誉。", "Được đại diện quốc gia thi đấu là vinh dự của tôi.",
     "Danh từ, nghĩa là vinh dự, vinh quang. 荣誉证书 là giấy khen, 荣誉称号 là danh hiệu vinh dự."),
    ("奖励", "jiǎnglì", "tưởng lệ", "động từ", "khen thưởng, thưởng", "公司奖励了表现最好的员工。", "Công ty khen thưởng những nhân viên làm việc tốt nhất.",
     "Động từ, nghĩa là thưởng để khích lệ. Cũng dùng làm danh từ: 物质奖励, phần thưởng vật chất."),
    ("称号", "chēnghào", "xưng hiệu", "danh từ", "danh hiệu", "他获得了劳动模范的称号。", "Ông ấy được tặng danh hiệu lao động gương mẫu.",
     "Danh từ, nghĩa là danh hiệu được trao tặng, thường mang tính vinh dự."),
    ("争气", "zhēng qì", "tranh khí", "động từ", "phấn đấu, không chịu thua kém, làm rạng mặt", "孩子很争气，考上了最好的大学。", "Đứa con rất biết phấn đấu, đã đỗ vào trường đại học tốt nhất.",
     "Động từ, nghĩa là phấn đấu vươn lên, làm nên chuyện để người nhà nở mày nở mặt. Ngược lại, 不争气 là không ra gì, làm người khác thất vọng. Đây là từ ly hợp: 争口气."),
    ("沾光", "zhān guāng", "triêm quang", "động từ", "hưởng lây, nhờ hơi (người khác)", "他从来不想沾父亲的光。", "Anh ấy chưa bao giờ muốn dựa hơi bố.",
     "Động từ, nghĩa là nhờ quan hệ với ai đó mà được hưởng lợi. Đây là từ ly hợp, mẫu hay gặp: 沾谁的光."),
    ("品质", "pǐnzhì", "phẩm chất", "danh từ", "phẩm chất, phẩm cách; chất lượng", "诚实是一种可贵的品质。", "Trung thực là một phẩm chất đáng quý.",
     "Danh từ, chỉ phẩm chất, nhân cách của con người; cũng chỉ chất lượng hàng hóa, như 品质优良, chất lượng tốt."),
    ("乐意", "lèyì", "lạc ý", "động từ", "sẵn lòng, vui lòng", "我很乐意帮助你。", "Tôi rất sẵn lòng giúp bạn.",
     "Động từ, nghĩa là vui lòng, sẵn lòng. Chú ý chữ đầu đọc lè, thanh bốn, nghĩa là vui, không đọc yuè."),
    ("精益求精", "jīngyìqiújīng", "tinh ích cầu tinh", "thành ngữ", "đã giỏi còn muốn giỏi hơn, không ngừng hoàn thiện", "他对工作精益求精，从不马虎。", "Anh ấy luôn cầu toàn trong công việc, chẳng bao giờ qua loa.",
     "Thành ngữ, nghĩa là đã tinh xảo rồi vẫn cầu cho tinh xảo hơn nữa, tức không ngừng hoàn thiện."),
    ("次序", "cìxù", "thứ tự", "danh từ", "thứ tự", "请按次序排队。", "Xin hãy xếp hàng theo thứ tự.",
     "Danh từ, giống tiếng Việt thứ tự. Tiếng Trung cũng hay nói 顺序."),
    ("朝代", "cháodài", "triều đại", "danh từ", "triều đại", "这件瓷器是哪个朝代的？", "Món đồ sứ này thuộc triều đại nào?",
     "Danh từ, giống tiếng Việt triều đại. Chú ý chữ đầu đọc cháo, thanh hai, khác với 朝霞 ở từ số một."),
    ("泛滥", "fànlàn", "phiếm lạm", "động từ", "(nước) tràn bờ; (điều xấu) tràn lan", "网上的假消息泛滥成灾。", "Tin giả trên mạng tràn lan thành nạn.",
     "Động từ. Nghĩa gốc là nước sông tràn bờ; nghĩa bóng là điều xấu lan tràn không kiểm soát được. Trong bài: 假货泛滥, hàng giả tràn lan."),
    ("威信", "wēixìn", "uy tín", "danh từ", "uy tín", "这位老师在学生中很有威信。", "Thầy giáo này rất có uy tín với học sinh.",
     "Danh từ, giống tiếng Việt uy tín. So với 威望: 威信 nhấn mạnh được người khác tin tưởng, còn 威望 nhấn mạnh danh vọng, tiếng tăm."),
    ("当代", "dāngdài", "đương đại", "danh từ", "đương đại, thời nay", "他是当代最有名的画家之一。", "Ông ấy là một trong những họa sĩ nổi tiếng nhất đương đại.",
     "Danh từ, giống tiếng Việt đương đại."),
    ("级别", "jíbié", "cấp biệt", "danh từ", "cấp bậc, cấp độ", "这是国家级别的比赛。", "Đây là cuộc thi cấp quốc gia.",
     "Danh từ, nghĩa là cấp bậc, cấp độ."),
    ("泰斗", "tàidǒu", "thái đẩu", "danh từ", "bậc thái đẩu, người đứng đầu một lĩnh vực", "他是中国古陶瓷鉴定的泰斗。", "Ông là bậc thái đẩu trong ngành giám định gốm sứ cổ Trung Quốc.",
     "Danh từ, rút gọn từ 泰山北斗, núi Thái Sơn và sao Bắc Đẩu, chỉ người có uy tín cao nhất trong một lĩnh vực. Tiếng Việt cũng nói bậc thái đẩu. Chú ý chữ sau đọc dǒu, thanh ba."),
]

add("bullets", chapter="Từ mới (51 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 34 có 51 từ mới, chia thành 17 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 颠簸 (bǒ) · 收藏 (cáng) · 乐意 (lè) · 朝霞 (zhāo) ≠ 朝代 (cháo) · 泰斗 (dǒu)",
           "Từ dễ nhầm: 无偿 ≠ vô thường · 图案 ≠ đồ án · 可观 ≠ khả quan · 神圣 ≠ thần thánh"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có năm mươi mốt từ, thầy chia thành mười bảy nhóm nhỏ, mỗi nhóm ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Bài này có một số chữ đa âm, thầy sẽ nhắc khi gặp."),
         F(4, "Đặc biệt, có mấy từ Hán Việt nghe quen nhưng nghĩa khác tiếng Việt, như 无偿，图案，可观，神圣. Thầy sẽ đánh dấu kỹ để các bạn không dùng nhầm. Chúng ta bắt đầu nhé.")])

for g in range(0, len(V), 3):
    group = V[g:g + 3]
    words, say = [], []
    for i, (zh, py, hv, loai, vi, ex, exvi, expl) in enumerate(group):
        n = g + i + 1
        words.append({"zh": zh, "py": py, "hv": hv.upper(), "loai": f"{n}. {loai}", "vi": vi, "ex": ex, "exvi": exvi})
        say.append(F(i, f"Từ số {n}: {zh}。 {zh}。 Hán Việt là {hv}.", zr=120))
        say.append(F(i, f"{expl} Ví dụ: {ex}{'' if ex[-1] in '。…？！，' else '，'} {exvi[0].upper() + exvi[1:]}{'' if exvi.endswith(('.', '?', '!')) else '.'}", zr=130))
    add("vocab", section="Từ mới 生词", title=f"Từ mới ({g + 1}–{g + len(group)} / {len(V)})",
        words=words, say=say)

# ======================= BÀI KHÓA =======================
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung nếu khác: số viết bằng chữ Hán])
P = [
    ("几十年前，北京街头远不及今天繁华。清晨，朝霞还没铺满天空，一位衣着朴素、性情温和的老人，坐着一路颠簸的公共汽车去上班。",
     "Mấy chục năm trước, đường phố Bắc Kinh còn kém xa sự phồn hoa của ngày nay. Sáng sớm, khi ráng hồng còn chưa phủ kín bầu trời, một ông lão ăn mặc giản dị, tính tình ôn hòa ngồi trên chiếc xe buýt xóc nảy suốt dọc đường để đi làm.",
     ["远不及 nghĩa là kém xa, không bằng được: A 远不及 B, A kém xa B. 繁华 là phồn hoa, sầm uất.",
      "衣着朴素、性情温和 là hai cụm bốn chữ song song, một tả bề ngoài, một tả tính cách. 一路颠簸 là xóc nảy suốt dọc đường."]),
    ("到站了，他慢慢地从车上走下来，走过他熟悉的大街小巷，步行到故宫博物院。他就是著名的古陶瓷收藏家、鉴定家孙瀛洲。",
     "Đến bến, ông chậm rãi bước xuống xe, đi qua những con phố, ngõ hẻm quen thuộc, đi bộ đến Bảo tàng Cố Cung. Ông chính là nhà sưu tầm, nhà giám định gốm sứ cổ nổi tiếng 孙瀛洲.",
     ["步行 là đi bộ. 故宫博物院 là Bảo tàng Cố Cung.",
      "Các bạn để ý cách mở bài: tác giả tả một ông lão bình thường trước, đến cuối mới nói 他就是…… để giới thiệu tên nhân vật. Cách này tạo sự tò mò cho người đọc."]),
    ("对于孙瀛洲和他的家人来说，1956年是个值得记忆的年头，那一年孙瀛洲将自己精心收藏的3000余件文物无偿赠送给了故宫博物院，其中的斗彩三秋杯更是格外引人注目。",
     "Đối với 孙瀛洲 và gia đình ông, năm 1956 là một năm đáng nhớ. Năm đó, 孙瀛洲 đã tặng không cho Bảo tàng Cố Cung hơn 3000 món cổ vật mà ông dày công sưu tầm, trong đó chiếc chén đấu thái tam thu càng đặc biệt thu hút sự chú ý.",
     ["对于……来说 là đối với… mà nói. 年头 ở đây là năm. Cấu trúc 将文物赠送给故宫 là cách nói văn viết của 把文物赠送给故宫, đem cổ vật tặng cho Cố Cung.",
      "余 đứng sau số nghĩa là hơn: 三千余件, hơn ba nghìn món. 格外引人注目 là đặc biệt thu hút sự chú ý."],
     "对于孙瀛洲和他的家人来说，一九五六年是个值得记忆的年头，那一年孙瀛洲将自己精心收藏的三千余件文物无偿赠送给了故宫博物院，其中的斗彩三秋杯更是格外引人注目。"),
    ("孙瀛洲的女儿孙女士至今仍记得当年的情景。那些日子，家里人来人往，络绎不绝，人们忙着对捐献的文物登记造册，之后，故宫的同志就该来打包装箱了。",
     "Con gái của 孙瀛洲 là bà Tôn đến nay vẫn còn nhớ cảnh tượng năm ấy. Những ngày đó, người ra người vào nhà tấp nập không ngớt, mọi người bận rộn ghi chép, lập sổ các cổ vật được hiến tặng; sau đó, cán bộ của Cố Cung sẽ đến đóng gói, cho vào thùng.",
     ["至今仍 là đến nay vẫn. 当年 là năm ấy, hồi đó. 人来人往 là người ra người vào, đi cùng 络绎不绝 càng nhấn mạnh sự tấp nập.",
      "对……登记造册 là ghi chép, lập sổ đối với…. Còn 就该来打包装箱了 nghĩa là sắp đến lúc đến đóng gói, cách nói giống như 该吃饭了, đến giờ ăn cơm rồi."]),
    ("那晚，父亲把全家叫到一起，从准备捐出的几百盒珍贵文物中找出一个精致的小盒子，取出两个小瓷杯给全家看。",
     "Tối hôm đó, bố gọi cả nhà lại, từ trong mấy trăm hộp cổ vật quý chuẩn bị hiến tặng, tìm ra một chiếc hộp nhỏ tinh xảo, lấy ra hai chiếc chén sứ nhỏ cho cả nhà xem.",
     ["从……中找出 là tìm ra từ trong…. 几百盒 là mấy trăm hộp, 盒 vừa là danh từ vừa là lượng từ.",
      "精致 là tinh xảo. Câu này dùng một chuỗi động từ liên tiếp: 叫到一起，找出，取出，给全家看, kể lại hành động theo đúng trình tự."]),
    ("他说这是咱家最值钱的东西，故宫里也没有，明天就捐给故宫了，今天让你们看看。父亲说话时脸上充满了自豪。",
     "Ông nói đây là thứ đáng giá nhất của nhà mình, ngay cả trong Cố Cung cũng không có, ngày mai sẽ hiến cho Cố Cung rồi, hôm nay cho các con xem một chút. Lúc nói, gương mặt bố tràn đầy niềm tự hào.",
     ["咱家 là nhà mình, khẩu ngữ, bao gồm cả người nghe. 值钱 là đáng giá. 也没有 ở đây là ngay cả… cũng không có.",
      "Câu nói của bố được thuật lại gián tiếp, nên không dùng dấu ngoặc kép. 充满了自豪 là tràn đầy tự hào."]),
    ("大家专注地看着父亲手里那对造型秀巧，杯体轻灵、洁白的斗彩瓷杯：杯体色调柔和而宁静，搭配的图案是两只在山石花草间飞舞的蝴蝶，淡雅清爽，赏心悦目。",
     "Mọi người chăm chú nhìn đôi chén sứ đấu thái trên tay bố, dáng thanh tú tinh xảo, thân chén nhẹ nhàng, trắng tinh: tông màu của chén dịu nhẹ mà tĩnh lặng, họa tiết đi kèm là hai con bướm bay lượn giữa đá núi và hoa cỏ, thanh nhã, tươi mát, nhìn mà vui mắt vui lòng.",
     ["专注地 là chăm chú. 造型秀巧 là kiểu dáng thanh tú, tinh xảo. 色调 là tông màu, chú ý chữ sau đọc diào.",
      "淡雅清爽，赏心悦目 là thanh nhã, tươi mát, đẹp mắt vui lòng. Tác giả tả chiếc chén theo trình tự: dáng chén, màu sắc, rồi đến họa tiết."]),
    ("相传这对杯子是当年皇帝专门下旨烧制的，不是烧给皇后，而是烧给一位爱妃。",
     "Tương truyền đôi chén này là do hoàng đế năm xưa đặc biệt hạ chỉ cho nung, không phải nung cho hoàng hậu, mà là nung cho một phi tần được vua sủng ái.",
     ["相传 là tương truyền, theo lời kể lại từ xưa. 下旨 là hạ chỉ, ra thánh chỉ. 烧制 là nung, chế tác bằng cách nung.",
      "不是……而是…… là không phải… mà là…. 爱妃 là phi tần được vua yêu chiều."]),
    ("当时共烧成5对，选出这一对后，其余4对全部销毁，并将烧制杯子的手艺人处死，烧制工艺就此失传，而这对凝聚着先人智慧结晶的杯子也就成了存世孤品。",
     "Khi đó tổng cộng nung được 5 đôi; sau khi chọn ra đôi này, 4 đôi còn lại đều bị tiêu hủy hết, và người thợ nung chén cũng bị xử tử, kỹ thuật nung từ đó thất truyền; còn đôi chén chứa đựng kết tinh trí tuệ của người xưa này cũng trở thành món duy nhất còn tồn tại trên đời.",
     ["共 là tổng cộng. 其余 là phần còn lại. 处死 là xử tử, chú ý chữ đầu đọc chǔ. 就此失传 là từ đó thất truyền.",
      "存世孤品 là món độc nhất còn tồn tại trên đời. Chính vì là món duy nhất nên đôi chén này vô cùng quý giá."],
     "当时共烧成五对，选出这一对后，其余四对全部销毁，并将烧制杯子的手艺人处死，烧制工艺就此失传，而这对凝聚着先人智慧结晶的杯子也就成了存世孤品。"),
    ("也许有人要问，这孙瀛洲到底什么来历？家藏竟然如此丰厚？",
     "Có lẽ có người sẽ hỏi: rốt cuộc 孙瀛洲 này có lai lịch thế nào? Đồ cất giữ trong nhà sao lại phong phú đến thế?",
     ["这 đứng trước tên riêng như 这孙瀛洲 là cách nói khẩu ngữ, nhấn mạnh đối tượng đang bàn. 到底 là rốt cuộc, 来历 là lai lịch, 竟然 thể hiện sự ngạc nhiên.",
      "Đoạn văn ngắn chỉ có hai câu hỏi này là một đoạn chuyển ý, nối phần kể chuyện hiến tặng với phần kể cuộc đời ông. Ta sẽ học kỹ ở phần kỹ năng viết."]),
    ("孙瀛洲的籍贯是河北，他13岁到北京，在古玩店做学徒、伙计，之后做过采购、副经理。1923年他自己创业，开办了古玩店。",
     "孙瀛洲 quê ở Hà Bắc. Năm 13 tuổi ông lên Bắc Kinh, làm người học việc, người làm công trong tiệm đồ cổ, sau đó từng làm người thu mua, phó giám đốc. Năm 1923, ông tự khởi nghiệp, mở tiệm đồ cổ.",
     ["学徒 là người học việc, 伙计 là người làm công trong tiệm, 副经理 là phó giám đốc.",
      "做过 là đã từng làm. 开办 là mở, thành lập. Các bạn thấy cuộc đời ông đi từ thấp lên cao: học việc, làm công, thu mua, phó giám đốc, rồi tự làm chủ."],
     "孙瀛洲的籍贯是河北，他十三岁到北京，在古玩店做学徒、伙计，之后做过采购、副经理。一九二三年他自己创业，开办了古玩店。"),
    ("由于经营有方，又收藏有大量珍贵文物，孙瀛洲在当时的古董经营者中很有威望。",
     "Nhờ kinh doanh có phương pháp, lại sưu tầm được rất nhiều cổ vật quý, 孙瀛洲 rất có uy tín trong giới kinh doanh đồ cổ thời bấy giờ.",
     ["由于……又…… là do…, lại…, nêu hai nguyên nhân. 经营有方 là kinh doanh có phương pháp. 古董 là đồ cổ, 古董经营者 là người kinh doanh đồ cổ.",
      "当时 là lúc bấy giờ, một ví dụ cho điểm ngữ pháp thứ hai mà ta sẽ học."]),
    ("孙女士感慨道，尽管当年家中私藏丰厚，但他们生活却非常简朴，甚至有些吝啬，举个例子吧，过年时孩子们吃的糖葫芦都是孙瀛洲自制的。他对孩子尚且如此，对自己的那份节俭也就不难想象了。",
     "Bà Tôn bồi hồi kể lại: tuy năm đó đồ cất giữ riêng trong nhà rất phong phú, nhưng cả nhà lại sống vô cùng giản dị, thậm chí có phần keo kiệt. Lấy ví dụ nhé, kẹo hồ lô bọn trẻ ăn dịp Tết đều do 孙瀛洲 tự làm. Đối với con cái mà ông còn như vậy, thì sự tiết kiệm của ông đối với bản thân cũng chẳng khó hình dung.",
     ["感慨道 là cảm khái nói, bồi hồi nói. 尽管……但……却…… là tuy… nhưng… lại…. 私藏 là đồ cất giữ riêng.",
      "他对孩子尚且如此，对自己……也就不难想象了 là câu mẫu cho điểm ngữ pháp 尚且. 那份节俭 là sự tiết kiệm ấy; 份 là lượng từ cho tình cảm, phẩm chất."]),
    ("可是，为了收购绝世珍品斗彩三秋杯，他却是不惜重金。正是这种对陶瓷执着的热爱，使孙瀛洲收藏了数量可观的陶瓷精品。",
     "Thế nhưng, để mua được báu vật có một không hai là chiếc chén đấu thái tam thu, ông lại không tiếc bỏ ra số tiền lớn. Chính tình yêu bền bỉ ấy đối với gốm sứ đã giúp 孙瀛洲 sưu tầm được một số lượng đáng kể những tác phẩm gốm sứ tinh phẩm.",
     ["可是 ở đầu câu là từ chuyển ý: phía trước nói ông tiết kiệm, phía sau nói ông không tiếc tiền. 绝世珍品 là báu vật có một không hai. 不惜重金 là không tiếc tiền lớn.",
      "正是……使…… là chính… đã khiến…. 执着 là kiên trì, bền bỉ, chú ý chữ sau đọc zhuó. 数量可观 là số lượng đáng kể."]),
    ("孙瀛洲的子女们说，父亲来到这个世界好像只有一个神圣的使命——保护文物。他全身心投入到文物当中，生活在文物当中。",
     "Các con của 孙瀛洲 nói, bố đến với thế giới này dường như chỉ có một sứ mệnh thiêng liêng: bảo vệ cổ vật. Ông dồn hết tâm sức vào cổ vật, sống giữa những cổ vật.",
     ["Dấu gạch ngang dài dùng để giải thích: sứ mệnh thiêng liêng ấy chính là 保护文物. Câu này cũng giải thích tên bài: 为文物而生的人.",
      "全身心投入到……当中 là dồn hết thân tâm vào…. Hai vế 投入到文物当中 và 生活在文物当中 lặp cấu trúc để nhấn mạnh."]),
    ("有人问他们怎样看待当年父亲捐赠的义举？要是在今天，你们这些做家属的会支持父亲吗？",
     "Có người hỏi họ nhìn nhận thế nào về nghĩa cử hiến tặng năm xưa của bố? Nếu là ngày nay, những người nhà như các anh chị có ủng hộ bố không?",
     ["义举 là nghĩa cử, việc làm vì nghĩa. 捐赠 là hiến tặng.",
      "要是 là nếu, khẩu ngữ. 你们这些做家属的 là các anh chị, những người làm người nhà; 做 ở đây là làm, đóng vai trò."]),
    ("他们回答：“今天我们也会拥护父亲的选择，就像父亲捐出这些文物不是为了表彰，不是为了荣誉，不是为了奖励，也没想得到什么称号一样，这些东西本就属于国家，属于全人类。”",
     "Họ trả lời: Ngày nay chúng tôi cũng sẽ ủng hộ sự lựa chọn của bố, cũng giống như việc bố hiến tặng những cổ vật này không phải để được biểu dương, không phải vì vinh dự, không phải vì phần thưởng, cũng không nghĩ tới việc nhận danh hiệu gì; những thứ này vốn thuộc về đất nước, thuộc về toàn nhân loại.",
     ["就像……一样 là cũng giống như…. Ba lần 不是为了 liên tiếp là phép điệp, tạo khí thế và nhấn mạnh động cơ trong sáng của người bố.",
      "本就 là vốn dĩ đã. 属于国家，属于全人类 lặp 属于 hai lần, ý được nâng từ đất nước lên toàn nhân loại."]),
    ("孙家后人很争气，他们不想沾父亲的光，父亲留给他们最大的财富就是高洁的品质。",
     "Con cháu nhà họ Tôn rất biết phấn đấu, họ không muốn dựa hơi bố; tài sản lớn nhất bố để lại cho họ chính là phẩm chất cao thượng, trong sạch.",
     ["后人 là con cháu đời sau. 沾父亲的光 là dựa hơi bố, ví dụ của từ ly hợp 沾光.",
      "高洁 là cao thượng và trong sạch. Câu này cho thấy món quà quý nhất không phải là tiền của, mà là nhân cách."]),
    ("1956年，孙瀛洲受聘于故宫博物院从事古陶瓷研究、鉴定工作。他很乐意接受这份工作，工作中更是精益求精。",
     "Năm 1956, 孙瀛洲 được Bảo tàng Cố Cung mời về làm công tác nghiên cứu, giám định gốm sứ cổ. Ông rất vui lòng nhận công việc này, và trong công việc lại càng không ngừng hoàn thiện.",
     ["受聘于 là được… mời làm việc, 于 ở đây chỉ nơi mời. 从事 là làm, theo đuổi một nghề.",
      "更是 là lại càng. 精益求精 là thành ngữ vừa học: đã giỏi còn muốn giỏi hơn."],
     "一九五六年，孙瀛洲受聘于故宫博物院从事古陶瓷研究、鉴定工作。他很乐意接受这份工作，工作中更是精益求精。"),
    ("孙瀛洲的弟子讲过这样一件事：一次，孙瀛洲让人们把不同时期的瓷器放在一起，其中当然有真品，也有仿品。",
     "Học trò của 孙瀛洲 từng kể một chuyện thế này: một lần, 孙瀛洲 bảo mọi người đặt đồ sứ của những thời kỳ khác nhau lại với nhau, trong đó dĩ nhiên có đồ thật, cũng có đồ giả.",
     ["弟子 là đệ tử, học trò. 讲过这样一件事 là từng kể một chuyện như thế này, dùng để dẫn vào một câu chuyện minh họa.",
      "真品 là đồ thật, 仿品 là đồ phỏng chế, đồ làm giả."]),
    ("他背过身，人们打乱摆放次序，他闭着眼睛，转过身来，只用手摸，就准确地一一说出了各件文物的朝代、名称。",
     "Ông quay lưng lại, mọi người xáo trộn thứ tự bày đặt; ông nhắm mắt, quay người lại, chỉ dùng tay sờ mà đã nói chính xác lần lượt triều đại, tên gọi của từng món cổ vật.",
     ["背过身 là quay lưng lại, 转过身来 là quay người lại. 打乱 là xáo trộn. 一一 là lần lượt từng cái một.",
      "只用手摸，就准确地一一说出 nghĩa là chỉ cần sờ bằng tay là đã nói chính xác, nhấn mạnh tài năng phi thường. Câu kể bằng chuỗi động tác ngắn, đọc lên rất có nhịp."]),
    ("在历来假货泛滥的文物界，鉴定家孙瀛洲就是一张最有威信的名片。",
     "Trong giới cổ vật, nơi từ trước đến nay hàng giả luôn tràn lan, nhà giám định 孙瀛洲 chính là một tấm danh thiếp có uy tín nhất.",
     ["历来 là từ trước đến nay. 文物界 là giới cổ vật, 界 là giới, như 教育界, giới giáo dục.",
      "一张最有威信的名片 là phép ẩn dụ: tên tuổi của ông giống như một tấm danh thiếp bảo chứng, cứ là ông giám định thì người ta tin."]),
    ("当代社会，被称为“专家”容易，称为“著名专家”也不难，但称得上“大家”的不多，孙瀛洲就是人人心服口服的国家级别的“大家”。",
     "Trong xã hội đương đại, được gọi là chuyên gia thì dễ, được gọi là chuyên gia nổi tiếng cũng không khó, nhưng người xứng đáng được gọi là bậc thầy thì không nhiều; 孙瀛洲 chính là bậc thầy cấp quốc gia mà ai ai cũng tâm phục khẩu phục.",
     ["被称为 là được gọi là; 称得上 là xứng đáng được gọi là. Ba bậc 专家，著名专家，大家 đi từ thấp lên cao, tạo thế tăng tiến.",
      "大家 ở đây là bậc thầy, không phải mọi người. 心服口服 là tâm phục khẩu phục, giống hệt thành ngữ tiếng Việt."]),
    ("孙瀛洲在故宫博物院工作期间将一生所学毫无保留地传授给学生，培养出一批文物鉴定人才，有的已成为当今古陶瓷鉴定的泰斗。",
     "Trong thời gian làm việc tại Bảo tàng Cố Cung, 孙瀛洲 đã truyền dạy cho học trò tất cả những gì ông học được cả đời mà không giữ lại chút nào, đào tạo nên một lớp nhân tài giám định cổ vật, trong đó có người đã trở thành bậc thái đẩu của ngành giám định gốm sứ cổ ngày nay.",
     ["期间 là trong thời gian. 将一生所学 là đem tất cả những gì học được cả đời; 所 cộng động từ tạo thành danh từ: 所学, điều đã học.",
      "毫无保留 là không giữ lại chút nào. 当今 là ngày nay. Bài khóa kết thúc bằng hình ảnh thầy truyền nghề cho trò, sự nghiệp bảo vệ cổ vật được tiếp nối."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 为文物而生的人",
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 为文物而生的人, dài một nghìn hai trăm chín mươi chín chữ, được cải biên từ một bài báo đăng trên 北京青年报, báo Thanh niên Bắc Kinh.",
         F(0, "Thầy chia bài thành hai mươi bốn đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 100 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi, cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Tóm tắt nội dung", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5) – phần 1", size=36,
    items=["## 1. 描述一下孙瀛洲 – Giới thiệu nhân vật",
           "衣着朴素，性情温和，坐着公共汽车到故宫上班，是古陶瓷收藏家、鉴定家",
           "## 2. 为什么说1956年是个值得记忆的年头？",
           "把3000余件文物无偿赠送给故宫 · 对文物登记造册，打包装箱 · 父亲取出斗彩三秋杯给全家看",
           "## 3. 为什么斗彩三秋杯有这么高的价值？",
           "造型秀巧，色调柔和，图案淡雅 · 相传皇帝下旨烧制，其余全部销毁，成了存世孤品"],
    say=["Chúng ta cùng nhìn lại bố cục của cả bài khóa. Bài tập năm trong sách gợi ý sáu câu hỏi, tương ứng với sáu phần của bài.",
         F(0, "Phần một: 描述一下孙瀛洲, hãy miêu tả 孙瀛洲."),
         F(1, "Ông ăn mặc giản dị, tính tình ôn hòa, ngồi xe buýt đến Cố Cung đi làm, là nhà sưu tầm và nhà giám định gốm sứ cổ."),
         F(2, "Phần hai: 为什么说一九五六年是个值得记忆的年头？ Vì sao nói năm một nghìn chín trăm năm mươi sáu là một năm đáng nhớ?"),
         F(3, "Vì năm đó ông tặng không hơn ba nghìn món cổ vật cho Cố Cung; cả nhà bận rộn lập sổ, đóng gói; và tối hôm ấy, người bố lấy đôi chén đấu thái tam thu ra cho cả nhà xem."),
         F(4, "Phần ba: 为什么斗彩三秋杯有这么高的价值？ Vì sao chiếc chén này có giá trị cao đến thế?"),
         F(5, "Vì nó có dáng đẹp, màu dịu, họa tiết thanh nhã; và tương truyền do hoàng đế hạ chỉ cho nung, những chiếc còn lại đều bị tiêu hủy, nên nó trở thành món độc nhất còn tồn tại.")])

add("bullets", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5) – phần 2", size=36,
    items=["## 4. 说说孙瀛洲的经历 – Cuộc đời",
           "籍贯河北 · 13岁到北京，在古玩店做学徒、伙计 · 1923年创业 · 在古董经营者中很有威望",
           "## 5. 孩子们怎么看待父亲和父亲的义举？",
           "生活简朴，却不惜重金收购珍品 · 支持父亲 · 不想沾父亲的光 · 最大财富是高洁的品质",
           "## 6. 孙瀛洲在工作中的贡献有哪些？",
           "从事鉴定工作，精益求精 · 闭眼摸瓷器说出朝代 · 心服口服的“大家” · 将一生所学传授给学生"],
    say=[F(0, "Phần bốn: 说说孙瀛洲的经历, kể về cuộc đời của 孙瀛洲."),
         F(1, "Quê Hà Bắc, mười ba tuổi lên Bắc Kinh học việc ở tiệm đồ cổ, năm một nghìn chín trăm hai mươi ba tự mở tiệm, và rất có uy tín trong giới kinh doanh đồ cổ."),
         F(2, "Phần năm: 孩子们怎么看待父亲和父亲的义举？ Các con nhìn nhận thế nào về người bố và nghĩa cử của ông?"),
         F(3, "Bố sống giản dị nhưng không tiếc tiền mua báu vật; các con ủng hộ lựa chọn của bố; họ không muốn dựa hơi bố; và tài sản lớn nhất bố để lại là phẩm chất cao thượng."),
         F(4, "Phần sáu: 孙瀛洲在工作中的贡献有哪些？ Những cống hiến của ông trong công việc là gì?"),
         F(5, "Ông làm công tác giám định và không ngừng hoàn thiện; nhắm mắt sờ đồ sứ cũng nói đúng triều đại; là bậc thầy được mọi người tâm phục khẩu phục; và truyền hết sở học cho học trò. Bố cục này rất có ích khi các bạn làm bài tập viết tóm tắt ở cuối bài.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 尚且", section="Ngữ pháp 注释", title="1. 尚且 shàngqiě – còn, đến… còn (huống chi…)", size=36,
    items=["Liên từ, dùng ở vế trước của câu phức: nêu một trường hợp rõ ràng để so sánh",
           "Vế sau: rút ra kết luận đương nhiên cho trường hợp cùng loại ở mức độ khác",
           "Mẫu: A 尚且……，(何况 / 更不用说 / 就更……) B……",
           "他对孩子尚且如此，对自己的那份节俭也就不难想象了。",
           "经济增长强劲时，这个企业尚且如此，经济衰退时，企业肯定会出现生存问题。",
           "“人”和“入”这么简单的两个字他尚且分不清楚，何况其他呢？"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là liên từ 尚且.",
         F(0, "尚且 dùng ở vế trước của câu phức. Vế này nêu ra một trường hợp rõ ràng, dễ thấy, để làm cơ sở so sánh."),
         F(1, "Vế sau nói về một trường hợp cùng loại nhưng ở mức độ khác, và rút ra kết luận đương nhiên. Tiếng Việt dịch là: A còn… huống chi B."),
         F(2, "Vế sau thường dùng 何况, 更不用说, hoặc 就更 để hô ứng."),
         F(3, "Ví dụ một, lấy từ bài khóa: 他对孩子尚且如此，对自己的那份节俭也就不难想象了。 Đối với con cái ông còn như vậy, thì sự tiết kiệm đối với bản thân cũng chẳng khó hình dung. Con cái là người ông thương nhất mà ông còn tiết kiệm, huống chi đối với chính mình."),
         F(4, "Ví dụ hai: 经济增长强劲时，这个企业尚且如此，经济衰退时，企业肯定会出现生存问题。 Khi kinh tế tăng trưởng mạnh, doanh nghiệp này còn như vậy, thì khi kinh tế suy thoái, chắc chắn sẽ gặp vấn đề sống còn."),
         F(5, "Ví dụ ba: 人和入这么简单的两个字他尚且分不清楚，何况其他呢？ Hai chữ đơn giản như chữ nhân và chữ nhập mà anh ta còn không phân biệt được, huống chi những chữ khác?")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: chọn vị trí thích hợp cho 尚且", reveal=True, size=38,
    items=["(1) A小学生B明白C这些D道理，何况大学生呢？",
           "Đáp án: B → 小学生尚且明白这些道理，何况大学生呢？",
           "(2) 钱钟书先生A如此B，对于一般人来说，读书D做笔记就更有必要了。",
           "Đáp án: A → 钱钟书先生尚且如此……",
           "(3) A这个字B你作为中国人C不认识，D我这个留学生就更不认识了。",
           "Đáp án: C → 这个字你作为中国人尚且不认识……"],
    say=[F(0, "Luyện tập: chọn vị trí thích hợp cho 尚且. Câu một: 小学生明白这些道理，何况大学生呢？ Học sinh tiểu học hiểu những đạo lý này, huống chi sinh viên? 尚且 nên đặt ở vị trí A, B, C hay D? Các bạn tạm dừng và suy nghĩ nhé."),
         F(1, "Đáp án: B. 小学生尚且明白这些道理，何况大学生呢？ Học sinh tiểu học còn hiểu những đạo lý này, huống chi sinh viên. 尚且 đứng sau chủ ngữ, trước động từ."),
         F(2, "Câu hai: 钱钟书先生如此，对于一般人来说，读书做笔记就更有必要了。 钱钟书 là nhà văn, học giả nổi tiếng, tác giả tiểu thuyết 围城, nổi tiếng vì đọc sách rất nhiều và ghi chép rất kỹ."),
         F(3, "Đáp án: A. 钱钟书先生尚且如此，对于一般人来说，读书做笔记就更有必要了。 Đến ông 钱钟书 còn như vậy, thì với người bình thường, đọc sách mà ghi chép lại càng cần thiết."),
         F(4, "Câu ba: 这个字你作为中国人不认识，我这个留学生就更不认识了。 Chữ này bạn là người Trung Quốc không biết, tôi là du học sinh thì lại càng không biết."),
         F(5, "Đáp án: C. 这个字你作为中国人尚且不认识，我这个留学生就更不认识了。 Chữ này bạn là người Trung Quốc còn không biết, huống chi tôi là du học sinh. Các bạn để ý: 尚且 luôn đứng ngay trước vị ngữ của vế trước.")])

add("bullets", chapter="Ngữ pháp: 当", section="Ngữ pháp 注释", title="2. 当 dāng – đang, ngay (lúc đó, nơi đó)", size=38,
    items=["Giới từ, nghĩa là 正在: đúng vào (thời điểm đó, nơi đó)",
           "Thường gặp: 当年 năm ấy · 当时 lúc ấy · 当代 thời nay · 当今 ngày nay · 当场 ngay tại chỗ · 当地 địa phương đó",
           "孙瀛洲的女儿孙女士至今仍记得当年的情景。",
           "由于经营有方，又收藏有大量珍贵文物，孙瀛洲在当时的古董经营者中很有威望。",
           "当代社会，被称为“专家”容易，称为“著名专家”也不难，但称得上“大家”的不多。"],
    say=["Điểm ngữ pháp thứ hai là giới từ đọc là dāng, thanh một, Hán Việt là đương, như trong đương thời, đương đại.",
         F(0, "Theo sách, nó có nghĩa là 正在, tức là đúng vào thời điểm đó, hoặc ở chính nơi đó."),
         F(1, "Ta hay gặp nó trong các từ: 当年，当时，当代，当今，当场，当地。 Tức là: năm ấy, lúc ấy, thời nay, ngày nay, ngay tại chỗ, và địa phương đó."),
         F(2, "Ví dụ một, lấy từ bài khóa: 孙瀛洲的女儿孙女士至今仍记得当年的情景。 Con gái ông là bà Tôn đến nay vẫn nhớ cảnh tượng năm ấy."),
         F(3, "Ví dụ hai: 由于经营有方，又收藏有大量珍贵文物，孙瀛洲在当时的古董经营者中很有威望。 Nhờ kinh doanh giỏi, lại sưu tầm nhiều cổ vật quý, ông rất có uy tín trong giới buôn đồ cổ thời bấy giờ."),
         F(4, "Ví dụ ba: 当代社会，被称为专家容易，称为著名专家也不难，但称得上大家的不多。 Trong xã hội đương đại, được gọi là chuyên gia thì dễ, gọi là chuyên gia nổi tiếng cũng không khó, nhưng xứng đáng là bậc thầy thì không nhiều.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: chọn 当今 / 当场 / 当地 điền vào chỗ trống", reveal=True, size=38,
    items=["(1) 洪水淹没了村庄，给___人民的生活造成了很大的损失。",
           "Đáp án: 当地",
           "(2) 所有这些，与___社会提倡的“可持续发展”“以人为本”的价值观显然是背道而驰的。",
           "Đáp án: 当今",
           "(3) 他刚把手伸到别人的书包里，钱包还没拿出来，就被警察___抓获。",
           "Đáp án: 当场"],
    say=[F(0, "Luyện tập: chọn một trong ba từ 当今，当场，当地 để điền vào chỗ trống. Câu một: 洪水淹没了村庄，给什么人民的生活造成了很大的损失。 Lũ lụt nhấn chìm làng mạc, gây tổn thất lớn cho đời sống của người dân nơi nào? Các bạn tạm dừng và chọn nhé."),
         F(1, "Đáp án: 当地. 给当地人民的生活造成了很大的损失。 Gây tổn thất lớn cho đời sống người dân địa phương."),
         F(2, "Câu hai: 所有这些，与什么社会提倡的可持续发展、以人为本的价值观显然是背道而驰的。 Tất cả những điều này rõ ràng đi ngược lại với giá trị phát triển bền vững, lấy con người làm gốc mà xã hội lúc nào đề xướng?"),
         F(3, "Đáp án: 当今. 与当今社会提倡的价值观背道而驰。 Đi ngược lại với giá trị mà xã hội ngày nay đề xướng. 背道而驰 là đi ngược chiều nhau."),
         F(4, "Câu ba: 他刚把手伸到别人的书包里，钱包还没拿出来，就被警察什么抓获。 Hắn vừa thò tay vào cặp người khác, còn chưa lấy được ví ra, thì đã bị cảnh sát bắt như thế nào?"),
         F(5, "Đáp án: 当场. 就被警察当场抓获。 Đã bị cảnh sát bắt quả tang ngay tại chỗ.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 温和 – 温柔", section="Phân biệt từ 词语辨析", title="Phân biệt 温和 và 温柔",
    common="Giống nhau: tính từ, (tính tình, thái độ, lời nói) không nghiêm khắc, khiến người ta thấy thân thiện. Ví dụ: 她性格温和/温柔。",
    cols=[{"head": "温和",
           "lines": ["(1) Nhấn mạnh thái độ, lời nói hòa nhã, lịch sự",
                     "Đúng: 经理温和的态度打消了我的顾虑。",
                     "(2) Còn chỉ khí hậu không lạnh không nóng",
                     "Đúng: 昆明气候温和，四季如春。"]},
          {"head": "温柔",
           "lines": ["(1) Hiền dịu, dễ chịu, có ý kiến khác vẫn chiều theo người khác; thường dùng cho nữ",
                     "Đúng: 这个女孩子很温柔。",
                     "(2) Không dùng cho khí hậu",
                     "Sai: 昆明气候温柔。"]}],
    say=["Tiếp theo là phần phân biệt từ: 温和 và 温柔. Hai từ này đều bắt đầu bằng chữ 温, ôn, nghĩa là ấm áp, nên rất dễ dùng lẫn.",
         "Điểm giống nhau: cả hai đều là tính từ, đều chỉ tính tình, thái độ, lời nói không nghiêm khắc, khiến người ta thấy thân thiện, gần gũi. Ví dụ: 她性格温和, hoặc 她性格温柔, đều đúng. Cô ấy tính tình hiền hòa.",
         F(0, "Điểm khác thứ nhất. 温和 nhấn mạnh thái độ và lời nói hòa nhã, lịch sự. Ví dụ: 经理温和的态度打消了我的顾虑。 Thái độ ôn hòa của giám đốc đã xóa tan nỗi lo lắng của tôi. 顾虑 là điều băn khoăn, lo lắng."),
         F(1, "Còn 温柔 hàm ý hiền dịu, tính nết dễ chịu, khi có ý kiến khác vẫn sẵn lòng chiều theo người khác. Từ này thường dùng cho phụ nữ. Ví dụ: 这个女孩子很温柔。 Cô gái này rất dịu dàng."),
         F(0, "Điểm khác thứ hai. 温和 còn dùng để chỉ khí hậu không lạnh không nóng. Ví dụ: 昆明气候温和，四季如春。 Khí hậu Côn Minh ôn hòa, bốn mùa đều như mùa xuân."),
         F(1, "Còn 温柔 không có cách dùng này. Nói 昆明气候温柔 là sai."),
         "Mẹo nhớ: 温和 là ôn hòa, dùng cho cả người lẫn khí hậu; 温柔 là dịu dàng, chỉ dùng cho người, đặc biệt là phụ nữ."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: Đúng hay sai?", reveal=True, size=38,
    items=["(1) 一个态度温和的办事员接待了我，仔细询问了我的情况。",
           "Đáp án: Đúng – 温和 chỉ thái độ hòa nhã.",
           "(2) 苏州地处太湖之滨，气候温柔，土地肥沃。",
           "Đáp án: Sai – khí hậu phải dùng 温和: 气候温和。",
           "(3) 她温柔地开导我，使我受伤的心灵得到一丝抚慰。",
           "Đáp án: Đúng – người phụ nữ dịu dàng an ủi.",
           "(4) 他温和的目光给了我莫大的力量，我鼓起勇气登台演出。",
           "Đáp án: Đúng – ánh mắt hiền hòa, thân thiện."],
    say=[F(0, "Bây giờ chúng ta làm thử: câu nào đúng, câu nào sai? Câu một: 一个态度温和的办事员接待了我，仔细询问了我的情况。 Một nhân viên có thái độ ôn hòa đã tiếp tôi, hỏi han kỹ tình hình của tôi. Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: đúng. 温和 dùng để chỉ thái độ hòa nhã, lịch sự."),
         F(2, "Câu hai: 苏州地处太湖之滨，气候温柔，土地肥沃。 Tô Châu nằm bên bờ Thái Hồ, khí hậu dịu dàng, đất đai màu mỡ."),
         F(3, "Đáp án: sai. Nói về khí hậu chỉ dùng được 温和, phải sửa thành 气候温和."),
         F(4, "Câu ba: 她温柔地开导我，使我受伤的心灵得到一丝抚慰。 Cô ấy dịu dàng khuyên giải tôi, khiến tâm hồn tổn thương của tôi được an ủi phần nào."),
         F(5, "Đáp án: đúng. 温柔 dùng cho người phụ nữ dịu dàng, rất phù hợp."),
         F(6, "Câu bốn: 他温和的目光给了我莫大的力量，我鼓起勇气登台演出。 Ánh mắt hiền hòa của anh ấy cho tôi sức mạnh to lớn, tôi lấy hết can đảm lên sân khấu biểu diễn."),
         F(7, "Đáp án: đúng. 温和的目光 là ánh mắt hiền hòa, thân thiện. 莫大 là vô cùng lớn.")])

# ======================= KỸ NĂNG VIẾT =======================
add("bullets", chapter="Kỹ năng viết: 过渡", section="Tu từ 篇章修辞", title="Chương pháp (5): Chuyển ý, nối đoạn (过渡)", size=38,
    items=["过渡: khi bài văn chuyển từ ý này sang ý khác, đoạn này sang đoạn khác, dùng từ, câu hoặc đoạn văn để nối cho tự nhiên",
           "Tác dụng: làm ý trên dưới liền mạch, cả bài thành một khối thống nhất",
           "## Ba hình thức",
           "过渡词 từ chuyển ý: 可是、但是、然而、此外、总之……",
           "过渡句 câu chuyển ý: thường là câu hỏi hoặc câu tóm ý trên, mở ý dưới",
           "过渡段 đoạn chuyển ý: một đoạn ngắn đứng riêng giữa hai phần lớn"],
    say=["Phần cuối cùng về lý thuyết là kỹ năng viết: chuyển ý, nối đoạn, tiếng Trung gọi là 过渡.",
         F(0, "Định nghĩa: khi bài văn chuyển từ tầng ý này sang tầng ý khác, hoặc từ đoạn này sang đoạn khác, người viết dùng một số từ, câu, hay đoạn văn để nối hai phần đó lại cho tự nhiên."),
         F(1, "Tác dụng của nó là làm cho ý văn phía trên và phía dưới liền mạch, tạo thành một chỉnh thể. Hầu hết các bài văn đều có ngôn ngữ chuyển ý."),
         F(2, "Có ba hình thức."),
         F(3, "Thứ nhất là 过渡词, từ chuyển ý, như 可是，但是，然而，此外，总之."),
         F(4, "Thứ hai là 过渡句, câu chuyển ý. Nó thường là một câu hỏi, hoặc một câu vừa tóm ý trên vừa mở ra ý dưới."),
         F(5, "Thứ ba là 过渡段, đoạn chuyển ý: một đoạn văn ngắn đứng riêng, nằm giữa hai phần lớn của bài.")])

add("bullets", section="Tu từ 篇章修辞", title="Ví dụ về 过渡: từ, câu và đoạn chuyển ý", size=34,
    items=["## 过渡词: 可是",
           "……他对孩子尚且如此，对自己的那份节俭也就不难想象了。可是，为了收购绝世珍品斗彩三秋杯，他却是不惜重金。",
           "## 过渡句: 鲸的身子这么大，它们吃什么呢？",
           "……四个人围着桌子坐在它的嘴里看书，还显得很宽敞。…… 鲸的身子这么大，它们吃什么呢？须鲸主要吃虾和小鱼……",
           "## 过渡段: 也许有人要问，这孙瀛洲到底什么来历？家藏竟然如此丰厚？",
           "Đoạn trước: chuyện hiến chén quý → đoạn chuyển ý → đoạn sau: 孙瀛洲的籍贯是河北……"],
    say=["Bây giờ ta xem ba ví dụ trong sách.",
         F(0, "Ví dụ một, từ chuyển ý: 可是."),
         F(1, "Phía trước nói ông sống rất tiết kiệm: 他对孩子尚且如此，对自己的那份节俭也就不难想象了。 Rồi bằng một từ 可是, ý văn chuyển hẳn sang hướng ngược lại: 可是，为了收购绝世珍品斗彩三秋杯，他却是不惜重金。 Từ tiết kiệm sang không tiếc tiền, chỉ cần một từ là nối được hai ý."),
         F(2, "Ví dụ hai, câu chuyển ý, lấy từ một bài văn về cá voi."),
         F(3, "Phần trước tả cá voi to đến mức bốn người ngồi quanh bàn đọc sách trong miệng nó vẫn thấy rộng rãi. Sau đó tác giả hỏi: 鲸的身子这么大，它们吃什么呢？ Thân cá voi to như vậy, chúng ăn gì? Rồi phần sau nói về thức ăn: 须鲸主要吃虾和小鱼, cá voi tấm sừng chủ yếu ăn tôm và cá nhỏ. Câu hỏi này vừa tóm ý trên, vừa mở ý dưới."),
         F(4, "Ví dụ ba, đoạn chuyển ý, chính là đoạn trong bài khóa: 也许有人要问，这孙瀛洲到底什么来历？家藏竟然如此丰厚？"),
         F(5, "Đoạn trước kể chuyện hiến đôi chén quý; đoạn này đặt câu hỏi về lai lịch của ông; rồi đoạn sau trả lời: 孙瀛洲的籍贯是河北. Nhờ đoạn ngắn này, bài văn chuyển từ chuyện hiến tặng sang chuyện cuộc đời rất tự nhiên.")])

add("bullets", section="Tu từ 篇章修辞", title="Luyện tập: đặt câu chuyển ý vào vị trí thích hợp", reveal=True, size=34,
    items=["Câu chuyển ý: 这座桥不但坚固，而且美观。",
           "……有一座世界闻名的石拱桥，叫安济桥，又叫赵州桥。A 它是隋朝的石匠李春设计和参加建造的……",
           "赵州桥非常雄伟。B 桥长五十多米……这种设计……既减轻了流水对桥身的冲击力……又减轻了桥身的重量，节省了石料。",
           "C 桥面两侧有石栏，栏板上雕刻着精美的图案……所有的龙似乎都在游动，真像活了一样。",
           "D 赵州桥表现了劳动人民的智慧和才干，是我国宝贵的历史遗产。",
           "Đáp án: C – nối ý kiên cố (thiết kế) với ý đẹp (lan can chạm rồng)"],
    say=[F(0, "Luyện tập: chọn vị trí thích hợp cho câu chuyển ý: 这座桥不但坚固，而且美观。 Cây cầu này không những kiên cố mà còn đẹp."),
         F(1, "Đoạn văn nói về 赵州桥, cầu Triệu Châu ở tỉnh Hà Bắc, một cây cầu đá vòm nổi tiếng thế giới, còn gọi là 安济桥. Vị trí A nằm ở đoạn giới thiệu chung về cây cầu và người xây dựng nó."),
         F(2, "Vị trí B ở đoạn tả cầu rất hùng vĩ, dài hơn năm mươi mét, và thiết kế đặc biệt vừa giảm sức va đập của dòng nước, vừa giảm trọng lượng thân cầu, tiết kiệm đá. Tức là nói về sự kiên cố."),
         F(3, "Vị trí C ở đầu đoạn tả lan can đá hai bên mặt cầu, chạm khắc những hình rồng tinh xảo như đang bay lượn. Tức là nói về vẻ đẹp."),
         F(4, "Vị trí D ở đoạn kết: cầu Triệu Châu thể hiện trí tuệ và tài năng của người lao động, là di sản lịch sử quý báu. Các bạn tạm dừng và chọn nhé."),
         F(5, "Đáp án: C. Phía trước nói về sự kiên cố, phía sau nói về vẻ đẹp. Câu 这座桥不但坚固，而且美观 vừa tóm ý trên bằng chữ kiên cố, vừa mở ý dưới bằng chữ đẹp, đúng là một câu chuyển ý điển hình.")])

add("bullets", section="Tu từ 篇章修辞", title="Bài tập 4: Tìm từ, câu chuyển ý trong đoạn văn", reveal=True, size=32,
    items=["(1) 我们班的同学学习都非常努力，拿小丽来说，她上课从来不迟到，每天不是在图书馆就是在宿舍学习。",
           "Đáp án: 拿小丽来说 (từ ý chung chuyển sang ví dụ cụ thể)",
           "(2) ……我们的教育工作就会取得良好效果。反之，教育工作就会迷失方向，遭受挫折，甚至失败。",
           "Đáp án: 反之 (chuyển sang mặt ngược lại)",
           "(3) ……技术和掌握高科技的人才也来自城市，总而言之，脱离了城市，农业和农村经济就无法得到发展。",
           "Đáp án: 总而言之 (chuyển sang tổng kết)",
           "(4) “三高”食品本身无罪，因为热量、脂肪、糖分也是人体必需的，但俗话说“过犹不及”……",
           "Đáp án: 但 (chuyển ý ngược lại: ăn quá nhiều thì có hại)"],
    say=[F(0, "Bài tập bốn trong sách: tìm từ hoặc câu chuyển ý. Đoạn một: 我们班的同学学习都非常努力，拿小丽来说，她上课从来不迟到，每天不是在图书馆就是在宿舍学习。 Các bạn lớp tôi đều học rất chăm, lấy Tiểu Lệ làm ví dụ, bạn ấy chưa bao giờ đi học muộn, ngày nào cũng học ở thư viện hoặc ký túc xá. Các bạn tìm thử nhé."),
         F(1, "Đáp án: 拿小丽来说, lấy Tiểu Lệ làm ví dụ. Cụm này chuyển từ nhận xét chung sang một ví dụ cụ thể."),
         F(2, "Đoạn hai: 如果我们在实践中选择和采取恰当的措施，目标一致地协调行动，我们的教育工作就会取得良好效果。反之，教育工作就会迷失方向，遭受挫折，甚至失败。 Nếu trong thực tiễn ta chọn biện pháp thích hợp, phối hợp hành động thống nhất, công tác giáo dục sẽ đạt hiệu quả tốt. Ngược lại, sẽ mất phương hướng, gặp thất bại."),
         F(3, "Đáp án: 反之, ngược lại. Từ này chuyển sang nói về mặt trái của vấn đề."),
         F(4, "Đoạn ba: 农业的市场主要在城市，资金主要来自城市，技术和掌握高科技的人才也来自城市，总而言之，脱离了城市，农业和农村经济就无法得到发展。 Thị trường, vốn, kỹ thuật và nhân tài của nông nghiệp đều đến từ thành phố; tóm lại, tách khỏi thành phố thì kinh tế nông nghiệp, nông thôn không thể phát triển."),
         F(5, "Đáp án: 总而言之, tóm lại. Từ này chuyển từ các ý cụ thể sang phần tổng kết."),
         F(6, "Đoạn bốn: 三高食品本身无罪，因为热量、脂肪、糖分也是人体必需的，但俗话说过犹不及，一个人每天摄入过量的油脂和糖分对身体危害是极大的。 Thực phẩm nhiều đường, nhiều béo, nhiều năng lượng bản thân không có tội, vì cơ thể cũng cần chúng; nhưng tục ngữ nói quá cũng như không, mỗi ngày ăn quá nhiều dầu mỡ và đường thì rất có hại."),
         F(7, "Đáp án: 但, nhưng. Từ này chuyển ý văn sang hướng ngược lại. 过犹不及 nghĩa là làm quá cũng tệ như làm chưa tới.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ được đánh dấu", size=40,
    items=["温和 (温) → 温柔 · 温顺 · 温厚 · 温情",
           "赠送 (赠) → 赠品 · 赠言 · 捐赠 · 馈赠",
           "皇帝 (皇) → 皇后 · 皇宫 · 皇室 · 皇家",
           "创业 (创) → 创新 · 创造 · 创作 · 创办",
           "荣誉 (荣) → 光荣 · 荣幸 · 荣获 · 繁荣"],
    say=["Phần luyện tập. Bài tập một: mô phỏng ví dụ, viết thêm các từ khác. Trong bài này, chữ được đánh dấu chấm đều là chữ đầu của từ.",
         F(0, "Ví dụ mẫu: 温和, có 温柔，温顺，温厚，温情. Tức là dịu dàng, ngoan ngoãn dễ bảo, hiền hậu, và tình cảm ấm áp."),
         F(1, "赠送, có 赠品，赠言，捐赠，馈赠. Tức là quà tặng kèm, lời tặng, quyên tặng, và biếu tặng."),
         F(2, "皇帝, có 皇后，皇宫，皇室，皇家. Tức là hoàng hậu, hoàng cung, hoàng thất, và hoàng gia."),
         F(3, "创业, có 创新，创造，创作，创办. Tức là đổi mới sáng tạo, sáng tạo, sáng tác, và sáng lập."),
         F(4, "荣誉, có 光荣，荣幸，荣获，繁荣. Tức là vẻ vang, vinh hạnh, vinh dự giành được, và phồn vinh.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Hoàn thành câu bằng từ cho sẵn (1)", reveal=True, size=38,
    items=["(1) 他常常____。（无偿）",
           "Đáp án: 他常常无偿帮助有困难的人。",
           "(2) 他们店的生意很好，____。（络绎不绝）",
           "Đáp án: 他们店的生意很好，顾客络绎不绝。",
           "(3) 大人____，更别说孩子了。（尚且）",
           "Đáp án: 大人尚且搬不动这块石头，更别说孩子了。"],
    say=[F(0, "Bài tập hai: dùng từ cho sẵn để hoàn thành câu. Câu một, dùng 无偿: 他常常…… Anh ấy thường thường làm gì? Các bạn tạm dừng và thử nhé."),
         F(1, "Đáp án gợi ý: 他常常无偿帮助有困难的人。 Anh ấy thường giúp đỡ không công những người gặp khó khăn. Cũng có thể nói 他常常无偿帮邻居修电脑, anh ấy thường sửa máy tính giúp hàng xóm mà không lấy tiền."),
         F(2, "Câu hai, dùng 络绎不绝: 他们店的生意很好…… Cửa hàng của họ buôn bán rất đắt, thì sao?"),
         F(3, "Đáp án gợi ý: 顾客络绎不绝。 Khách hàng ra vào nườm nượp không ngớt."),
         F(4, "Câu ba, dùng 尚且: 大人……，更别说孩子了。 Người lớn thế nào đó, huống chi là trẻ con."),
         F(5, "Đáp án gợi ý: 大人尚且搬不动这块石头，更别说孩子了。 Người lớn còn không khiêng nổi tảng đá này, huống chi trẻ con. Các bạn để ý 更别说 hô ứng với 尚且, giống như 何况.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Hoàn thành câu bằng từ cho sẵn (2)", reveal=True, size=38,
    items=["(4) 为了自己的事业，____。（不惜）",
           "Đáp án: 为了自己的事业，他不惜付出一切代价。",
           "(5) 由于采用了新技术，____。（可观）",
           "Đáp án: 由于采用了新技术，工厂的产量增长相当可观。",
           "(6) 人们对环境的破坏____。（泛滥）",
           "Đáp án: 人们对环境的破坏导致了洪水泛滥。"],
    say=[F(0, "Câu bốn, dùng 不惜: 为了自己的事业…… Vì sự nghiệp của mình thì sao?"),
         F(1, "Đáp án gợi ý: 为了自己的事业，他不惜付出一切代价。 Vì sự nghiệp của mình, anh ấy sẵn sàng trả bất cứ giá nào."),
         F(2, "Câu năm, dùng 可观: 由于采用了新技术…… Nhờ áp dụng công nghệ mới thì sao?"),
         F(3, "Đáp án gợi ý: 工厂的产量增长相当可观。 Sản lượng của nhà máy tăng lên khá đáng kể. Nhớ là 可观 nói về số lượng lớn, không phải khả quan nhé."),
         F(4, "Câu sáu, dùng 泛滥: 人们对环境的破坏…… Sự phá hoại môi trường của con người thì sao?"),
         F(5, "Đáp án gợi ý: 人们对环境的破坏导致了洪水泛滥。 Sự phá hoại môi trường của con người đã dẫn đến lũ lụt tràn lan. Ở đây 泛滥 dùng theo nghĩa gốc là nước tràn bờ.")])

add("bullets", section="Luyện tập 练习", title="Mở rộng 扩展: từ chỉ thân phận con người", size=34,
    items=["董事长 chủ tịch hội đồng quản trị · 法人 pháp nhân (công ty, đoàn thể…)",
           "顾问 cố vấn · 保姆 người giúp việc (trông trẻ, chăm người già, làm việc nhà)",
           "乞丐 người ăn xin · 渔民 ngư dân · 公民 công dân",
           "委员 ủy viên · 书记 bí thư (người phụ trách chính của tổ chức Đảng, Đoàn)",
           "元首 nguyên thủ quốc gia · 俘虏 tù binh",
           "将军 tướng quân, tướng lĩnh · 司令 tư lệnh"],
    say=["Phần mở rộng của sách giới thiệu một số từ chỉ thân phận con người.",
         F(0, "董事长, chủ tịch hội đồng quản trị, là người đại diện pháp lý của công ty, do hội đồng quản trị bầu ra. 法人, pháp nhân, là tổ chức được thành lập theo luật, có tài sản độc lập, như công ty, đoàn thể."),
         F(1, "顾问, cố vấn, là người có kiến thức chuyên môn để cá nhân hoặc cơ quan hỏi ý kiến. 保姆 là người phụ nữ được thuê để trông trẻ, chăm người già, người bệnh, hoặc làm việc nhà. Cẩn thận: bảo mẫu trong tiếng Việt thường là cô giáo trông trẻ ở nhà trẻ, còn 保姆 là người giúp việc gia đình."),
         F(2, "乞丐 là người ăn xin. 渔民 là ngư dân, người sống bằng nghề đánh cá. 公民 là công dân, người có quốc tịch một nước, được hưởng quyền lợi và có nghĩa vụ theo pháp luật nước đó."),
         F(3, "委员 là ủy viên, thành viên của một tổ chức lãnh đạo tập thể. 书记 là bí thư, người phụ trách chính trong tổ chức Đảng, Đoàn. Cẩn thận: thư ký trong tiếng Việt thì tiếng Trung là 秘书, đừng nhầm với 书记 nhé."),
         F(4, "元首 là nguyên thủ, người lãnh đạo cao nhất của một quốc gia. 俘虏 là tù binh, kẻ địch bị bắt trong chiến tranh."),
         F(5, "将军 là tướng quân, sĩ quan cấp tướng, cũng chỉ chung sĩ quan cao cấp. 司令 là tư lệnh, người chỉ huy quân sự trong quân đội một số nước.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 34", size=36,
    items=["Từ vựng trọng tâm: 朴素 · 无偿 · 络绎不绝 · 凝聚 · 吝啬 · 不惜 · 可观 · 神圣 · 争气 · 沾光 · 精益求精 · 泰斗",
           "Ngữ pháp: 尚且 (A 尚且…，何况 B) · 当 = 正在 (当年、当时、当代、当今、当场、当地)",
           "Phân biệt: 温和 (thái độ hòa nhã, cả khí hậu) ≠ 温柔 (dịu dàng, dùng cho người, nhất là nữ)",
           "Viết: 过渡 – từ chuyển ý (可是)、câu chuyển ý、đoạn chuyển ý",
           "## Bài tập về nhà",
           "Dựa vào bài tập 5, rút gọn bài khóa thành bài văn ngắn khoảng 400 chữ, nhớ dùng từ, câu chuyển ý"],
    say=["Chúng ta cùng tổng kết bài ba mươi tư.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 朴素，无偿，络绎不绝，凝聚，吝啬，不惜，可观，神圣，争气，沾光，精益求精，泰斗. Và nhớ kỹ những từ dễ nhầm: 无偿 không phải vô thường, 可观 không phải khả quan, 神圣 là thiêng liêng."),
         F(1, "Về ngữ pháp: 尚且 dùng ở vế trước, nêu một trường hợp rõ ràng, vế sau thường có 何况 hoặc 更别说, nghĩa là A còn… huống chi B. Còn giới từ đọc dāng có nghĩa là 正在, đúng vào lúc đó, nơi đó, như trong 当年，当时，当代，当今，当场，当地."),
         F(2, "Về phân biệt từ: 温和 nhấn mạnh thái độ hòa nhã, lịch sự, và còn dùng cho khí hậu; 温柔 là dịu dàng, chỉ dùng cho người, thường là phụ nữ."),
         F(3, "Về kỹ năng viết: dùng từ chuyển ý như 可是, câu chuyển ý, hoặc đoạn chuyển ý để bài văn liền mạch, chuyển từ ý này sang ý khác một cách tự nhiên."),
         F(5, "Bài tập về nhà, theo phần vận dụng của sách: bài khóa kể câu chuyện về nhà sưu tầm, nhà giám định gốm sứ 孙瀛洲, cho ta thấy phong thái của một bậc thầy thực thụ. Các bạn hãy tham khảo bài tập năm, rút gọn bài khóa thành một bài văn ngắn khoảng bốn trăm chữ. Hãy đi lần lượt sáu phần mà thầy đã tổng kết, và thử dùng 尚且 cùng ít nhất một từ chuyển ý nhé."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Hẹn gặp lại các bạn ở bài ba mươi lăm: 走近木版年画, Đến gần tranh Tết khắc gỗ, một bài tiếp tục chủ đề văn hóa truyền thống. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Hạ) – Bài 34: 为文物而生的人 (Người sinh ra vì cổ vật)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh; cụm dài trước)
    "tts_replace": {"为文物": "位文物",    # wèi (vì)
                    "朝霞": "招霞",        # zhāoxiá
                    "朝代": "潮代",        # cháodài
                    "颠簸": "颠跛",        # diānbǒ
                    "巷": "向",            # xiàng (大街小巷, chỉ có âm này trong bài)
                    "衣着": "衣酌",        # yīzhuó
                    "执着": "执酌",        # zhízhuó
                    "斗彩": "豆彩",        # dòucǎi
                    "泰斗": "泰抖",        # tàidǒu
                    "北斗": "北抖",        # běidǒu
                    "处死": "楚死",        # chǔsǐ
                    "地处": "地楚",        # dìchǔ
                    "色调": "色掉",        # sèdiào
                    "朴素": "普素",        # pǔsù
                    "简朴": "简普",        # jiǎnpǔ
                    "乐意": "勒意",        # lèyì
                    "背过身": "被过身",    # bèi guò shēn
                    "背道": "被道",        # bèidào (背道而驰)
                    "以人为本": "以人维本",  # yǐ rén wéi běn
                    "称为": "称维",        # chēngwéi
                    "强劲": "强竞",        # qiángjìng
                    "恰当": "恰荡",        # qiàdàng
                    "糖分": "糖份",        # tángfèn
                    "董事长": "董事掌"},   # dǒngshìzhǎng
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai34.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
