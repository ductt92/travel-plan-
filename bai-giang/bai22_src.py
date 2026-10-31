#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Hạ) – Bài 22 «2050年的汽车什么样». Chạy để sinh bai22.json."""
import json
import os

TAG = "HSK 6 (Hạ) · Bài 22 · 2050年的汽车什么样"
slides = []


def add(type_, chapter=None, section="", **kw):
    s = {"type": type_, "section": section, **kw}
    if chapter:
        s["chapter"] = chapter
    slides.append(s)


def F(i, t, **kw):
    return {"t": t, "f": i, **kw}


def zh_num(s):
    """Đổi số năm trong câu tiếng Trung sang chữ Hán để giọng Trung đọc liền mạch."""
    return s.replace("2050", "二零五零")


# ======================= MỞ ĐẦU =======================
add("title", chapter="Mở đầu",
    top="Giáo trình chuẩn HSK 6 – Quyển Hạ",
    zh="2050年的汽车什么样", py="Èr líng wǔ líng nián de qìchē shénme yàng",
    vi="Bài 22: Ô tô năm 2050 sẽ như thế nào?",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Hạ.",
         "Hôm nay chúng ta học bài hai mươi hai: 二零五零年的汽车什么样？ Nghĩa là: Ô tô năm hai nghìn không trăm năm mươi sẽ như thế nào?",
         "Bài này tiếp nối chủ đề tưởng tượng về cuộc sống tương lai của bài trước. Bài khóa là một bài báo thuyết minh, phác họa bốn đặc điểm của chiếc ô tô trong tương lai: sạch và an toàn hơn, tự động lái, hòa nhập với lối sống số, và vấn đề nhiên liệu."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu nội dung bài khóa 2050年的汽车什么样 – 4 đặc điểm của ô tô tương lai",
           "Nắm vững 52 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: 动不动 và cách dùng 甲乙丙丁……",
           "Phân biệt hai từ 担保 và 保证",
           "Kỹ năng viết: liên kết từ vựng (词汇衔接)"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa, xem ô tô năm hai nghìn không trăm năm mươi có bốn đặc điểm gì."),
         F(1, "Thứ hai, nắm vững năm mươi hai từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học hai điểm ngữ pháp: cụm từ 动不动, và cách dùng 甲，乙，丙，丁 để sắp xếp thứ tự."),
         F(3, "Thứ tư, phân biệt hai từ rất dễ nhầm: 担保 và 保证."),
         F(4, "Thứ năm, một kỹ năng viết rất hữu ích: liên kết từ vựng, tiếng Trung gọi là 词汇衔接."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Câu hỏi khởi động",
    items=["关于未来的汽车，你认为会具有什么样的功能？",
           "1. 能够自动驾驶。 – Có thể tự động lái",
           "2. 节能环保。 – Tiết kiệm năng lượng, bảo vệ môi trường",
           "3. 水上、陆地、空中都能行驶。 – Chạy được trên nước, trên bộ và trên không",
           "4. 具有更多数字生活功能。 – Có nhiều chức năng của đời sống số hơn",
           "其他： – Chức năng khác?"],
    say=["Chúng ta bắt đầu bằng phần khởi động. Câu hỏi thứ nhất của sách là:",
         F(0, "关于未来的汽车，你认为会具有什么样的功能？ Về ô tô của tương lai, bạn cho rằng nó sẽ có những chức năng gì? Sách gợi ý bốn lựa chọn."),
         F(1, "Một: 能够自动驾驶。 Có thể tự động lái. 驾驶 là lái xe."),
         F(2, "Hai: 节能环保。 Tiết kiệm năng lượng và bảo vệ môi trường. 节能 là tiết kiệm năng lượng, 环保 là bảo vệ môi trường."),
         F(3, "Ba: 水上、陆地、空中都能行驶。 Chạy được cả trên mặt nước, trên đất liền và trên không trung. 行驶 là chạy, dùng cho xe cộ, tàu thuyền."),
         F(4, "Bốn: 具有更多数字生活功能。 Có nhiều chức năng của đời sống số hơn."),
         F(5, "Và 其他, những chức năng khác. Các bạn hãy tạm dừng video, chọn đáp án của mình và thử nói thêm một chức năng khác bằng tiếng Trung nhé.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 油 và 缺", size=36,
    items=["## 油 (du): dầu, mỡ",
           "石油 dầu mỏ · 汽油 xăng · 柴油 dầu diesel · 花生油 dầu lạc · 豆油 dầu đậu nành · 橄榄油 dầu ô liu · 奶油 kem sữa",
           "黄油 bơ · 鱼油 dầu cá · 菜籽油 dầu hạt cải · 鞋油 xi đánh giày · 加油 đổ xăng; cố lên · 油炸 chiên ngập dầu · 油田 mỏ dầu",
           "## 缺 (khuyết): thiếu",
           "紧缺 khan hiếm · 缺少 thiếu · 缺乏 thiếu hụt · 缺口 chỗ hổng, chỗ thiếu hụt",
           "缺课 nghỉ học · 缺水 thiếu nước · 缺觉 thiếu ngủ · 缺勤 vắng mặt (không đi làm)"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo, rất có lợi cho người Việt vì hầu hết các chữ đều có âm Hán Việt quen thuộc.",
         F(0, "Nhóm thứ nhất có chữ 油, Hán Việt là du, nghĩa là dầu, mỡ."),
         F(1, "石油，汽油，柴油，花生油，豆油，橄榄油，奶油。 Tức là: dầu mỏ, xăng, dầu diesel, dầu lạc, dầu đậu nành, dầu ô liu và kem sữa. Trong bài khóa, các bạn sẽ gặp 石油，汽油 và 柴油."),
         F(2, "黄油，鱼油，菜籽油，鞋油，加油，油炸，油田。 Tức là: bơ, dầu cá, dầu hạt cải, xi đánh giày, đổ xăng, chiên ngập dầu, và mỏ dầu. Từ 加油 vừa là đổ xăng, vừa là cố lên, chắc các bạn rất quen."),
         F(3, "Nhóm thứ hai có chữ 缺, Hán Việt là khuyết, nghĩa là thiếu, như trong từ khuyết điểm của tiếng Việt."),
         F(4, "紧缺，缺少，缺乏，缺口。 Tức là: khan hiếm, thiếu, thiếu hụt, và chỗ hổng. Bài khóa có câu 石油资源日益紧缺, tài nguyên dầu mỏ ngày càng khan hiếm."),
         F(5, "缺课，缺水，缺觉，缺勤。 Tức là: nghỉ học, thiếu nước, thiếu ngủ, và vắng mặt không đi làm. Chú ý từ 缺觉, chữ 觉 ở đây đọc là jiào, nghĩa là giấc ngủ.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 迹 và 导", size=36,
    items=["## 迹 (tích): dấu vết",
           "劣迹 vết nhơ, hành vi xấu · 事迹 sự tích · 奇迹 kỳ tích · 名胜古迹 danh lam cổ tích · 足迹 dấu chân",
           "笔迹 bút tích · 痕迹 dấu vết · 污迹 vết bẩn · 血迹 vết máu · 迹象 dấu hiệu",
           "## 导 (đạo): dẫn dắt",
           "引导 dẫn dắt · 指导 chỉ đạo · 领导 lãnh đạo · 向导 người dẫn đường · 主导 chủ đạo · 倡导 đề xướng",
           "先导 người đi đầu · 导游 hướng dẫn viên du lịch · 导演 đạo diễn · 导师 người hướng dẫn · 导航 dẫn đường"],
    say=[F(0, "Nhóm thứ ba có chữ 迹, Hán Việt là tích, nghĩa là dấu vết, như trong từ di tích, bút tích."),
         F(1, "劣迹，事迹，奇迹，名胜古迹，足迹。 Tức là: vết nhơ hay hành vi xấu, sự tích, kỳ tích, danh lam cổ tích, và dấu chân. Từ 劣迹 có trong bài khóa: 鉴于以上劣迹, xét đến những tội trạng kể trên."),
         F(2, "笔迹，痕迹，污迹，血迹，迹象。 Tức là: bút tích, dấu vết, vết bẩn, vết máu, và dấu hiệu."),
         F(3, "Nhóm cuối cùng có chữ 导, Hán Việt là đạo, nghĩa là dẫn dắt, như trong từ lãnh đạo, hướng đạo."),
         F(4, "引导，指导，领导，向导，主导，倡导。 Tức là: dẫn dắt, chỉ đạo, lãnh đạo, người dẫn đường, chủ đạo, và đề xướng. Bài khóa có cụm 引导一长串汽车前行, dẫn một chuỗi dài ô tô tiến lên."),
         F(5, "先导，导游，导演，导师，导航。 Tức là: người đi đầu, hướng dẫn viên du lịch, đạo diễn, người hướng dẫn, và dẫn đường hay định vị. 导航 chính là chức năng chỉ đường trên ô tô và điện thoại."),
         "Các bạn thấy không, chỉ cần nắm nghĩa của một chữ gốc, ta có thể đoán được nghĩa của cả một nhóm từ. Hãy áp dụng cách này khi học từ mới nhé."])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng)
V = [
    ("堵塞", "dǔsè", "đổ tắc", "động từ", "tắc nghẽn, bị chặn lại", "每次遇到交通堵塞，人们就会心烦意乱。", "Mỗi lần gặp tắc đường, mọi người lại bực bội rối bời.",
     "Động từ, nghĩa là tắc nghẽn, bị chặn lại. 交通堵塞 là tắc nghẽn giao thông, trong khẩu ngữ hay nói 堵车. Chú ý: chữ 塞 ở đây đọc là sè, thanh bốn."),
    ("滞留", "zhìliú", "trệ lưu", "động từ", "bị kẹt lại, lưu lại (không đi được)", "滞留在路上", "bị kẹt lại trên đường",
     "Động từ, nghĩa là bị kẹt lại, phải ở lại một chỗ không đi tiếp được, thường do thời tiết hay giao thông."),
    ("折磨", "zhémó", "chiết ma", "động từ", "dày vò, hành hạ", "被堵车折磨得心烦意乱", "bị tắc đường dày vò đến bực bội rối bời",
     "Động từ, nghĩa là dày vò, hành hạ cả về thể xác lẫn tinh thần. Hay dùng trong câu bị động: 被 cộng tác nhân cộng 折磨."),
    ("翼", "yì", "dực", "danh từ", "cánh", "汽车要是也有双翼就好了。", "Giá mà ô tô cũng có đôi cánh thì hay biết mấy.",
     "Danh từ, nghĩa là cánh, là cách nói văn viết của 翅膀. 双翼 là đôi cánh."),
    ("担保", "dānbǎo", "đảm bảo", "động từ", "bảo đảm, cam đoan (chịu trách nhiệm)", "别的不敢担保", "những chuyện khác thì không dám đảm bảo",
     "Động từ, nghĩa là bảo đảm, cam đoan và chịu trách nhiệm. Đây là từ trong phần phân biệt với 保证, các bạn chú ý nhé."),
    ("大体", "dàtǐ", "đại thể", "phó từ", "về đại thể, nhìn chung", "大体为我们勾画出了汽车的轮廓", "về đại thể đã phác họa cho chúng ta hình dáng ô tô",
     "Phó từ, nghĩa là về đại thể, nhìn chung, gần như. Âm Hán Việt giống hệt từ đại thể của tiếng Việt."),
    ("勾画", "gōuhuà", "câu họa", "động từ", "phác họa, vẽ phác", "勾画出未来汽车的轮廓", "phác họa ra hình dáng ô tô tương lai",
     "Động từ, nghĩa là phác họa, vẽ ra những đường nét chính; nghĩa bóng là miêu tả một cách khái quát."),
    ("轮廓", "lúnkuò", "luân khuếch", "danh từ", "đường nét, hình dáng bên ngoài", "远处山的轮廓", "đường nét của dãy núi phía xa",
     "Danh từ, nghĩa là đường viền, hình dáng bên ngoài; cũng chỉ nét khái quát của một sự việc."),
    ("指责", "zhǐzé", "chỉ trách", "động từ", "chỉ trích, trách móc", "我们常常听到这样的指责。", "Chúng ta thường nghe những lời chỉ trích như thế này.",
     "Động từ, nghĩa là chỉ trích, trách móc. Cũng dùng như danh từ: 这样的指责, những lời chỉ trích như vậy."),
    ("融化", "rónghuà", "dung hóa", "động từ", "tan chảy (băng, tuyết)", "北极冰川在融化。", "Băng ở Bắc Cực đang tan chảy.",
     "Động từ, nghĩa là tan chảy, thường dùng cho băng, tuyết."),
    ("石油", "shíyóu", "thạch du", "danh từ", "dầu mỏ", "石油资源日益紧缺。", "Tài nguyên dầu mỏ ngày càng khan hiếm.",
     "Danh từ, nghĩa là dầu mỏ. Chữ 油 ta vừa học trong phần khởi động."),
    ("事故", "shìgù", "sự cố", "danh từ", "tai nạn, sự cố", "死于交通事故", "chết vì tai nạn giao thông",
     "Danh từ, nghĩa là tai nạn, sự cố. 交通事故 là tai nạn giao thông."),
    ("割", "gē", "cát", "động từ", "cắt; từ bỏ", "忍痛割爱", "nén đau từ bỏ thứ mình yêu quý",
     "Động từ, nghĩa gốc là cắt, như 割草, cắt cỏ; nghĩa bóng là từ bỏ. Thành ngữ 忍痛割爱 nghĩa là nén đau mà từ bỏ thứ mình yêu quý."),
    ("优胜劣汰", "yōushèng-liètài", "ưu thắng liệt thải", "thành ngữ", "mạnh được yếu thua, chọn lọc đào thải", "根据优胜劣汰的原则", "theo nguyên tắc mạnh được yếu thua",
     "Thành ngữ, nghĩa là cái tốt thì thắng, cái kém thì bị đào thải, giống câu mạnh được yếu thua, hay quy luật chọn lọc tự nhiên."),
    ("皆", "jiē", "giai", "phó từ", "đều, tất cả", "一切皆有可能。", "Mọi thứ đều có thể xảy ra.",
     "Phó từ, nghĩa là đều, tất cả, là cách nói văn viết của 都."),
    ("明智", "míngzhì", "minh trí", "tính từ", "sáng suốt, khôn ngoan", "似乎不是明智之举。", "Dường như không phải là hành động sáng suốt.",
     "Tính từ, nghĩa là sáng suốt, khôn ngoan. 明智之举 là một hành động sáng suốt."),
    ("出路", "chūlù", "xuất lộ", "danh từ", "lối ra; lối thoát, hướng giải quyết", "根本出路", "lối thoát căn bản",
     "Danh từ. Nghĩa đen là lối ra; nghĩa bóng là lối thoát, hướng giải quyết vấn đề."),
    ("规范", "guīfàn", "quy phạm", "tính từ", "đúng chuẩn mực, đúng quy tắc", "规范驾车出行", "lái xe đi lại đúng quy tắc",
     "Tính từ, nghĩa là đúng chuẩn mực, đúng quy tắc. Cũng có thể làm danh từ, nghĩa là quy phạm, chuẩn mực."),
    ("谋求", "móuqiú", "mưu cầu", "động từ", "mưu cầu, tìm cách đạt được", "谋求发展", "mưu cầu phát triển",
     "Động từ, nghĩa là mưu cầu, tìm cách đạt được, thường đi với 发展，利益，合作."),
    ("干预", "gānyù", "can dự", "động từ", "can thiệp", "无人干预", "không có người can thiệp",
     "Động từ, nghĩa là can thiệp, can dự vào việc gì đó."),
    ("平坦", "píngtǎn", "bình thản", "tính từ", "bằng phẳng", "平坦的高速路", "đường cao tốc bằng phẳng",
     "Tính từ, nghĩa là bằng phẳng, dùng cho đường sá, mặt đất. Cẩn thận: bình thản trong tiếng Việt là điềm tĩnh, còn 平坦 trong tiếng Trung là bằng phẳng."),
    ("奔驰", "bēnchí", "bôn trì", "động từ", "chạy nhanh, phóng nhanh", "车辆在高速路上奔驰。", "Xe cộ phóng nhanh trên đường cao tốc.",
     "Động từ, nghĩa là chạy rất nhanh, phi nhanh, dùng cho ngựa hay xe cộ. Hãng xe Mercedes trong tiếng Trung cũng tên là 奔驰."),
    ("试图", "shìtú", "thí đồ", "động từ", "thử, định, cố tìm cách", "欧洲正试图实现自动行驶。", "Châu Âu đang thử thực hiện việc tự động lái.",
     "Động từ, nghĩa là thử, định, cố tìm cách làm việc gì, mang sắc thái văn viết. Phía sau 试图 là một động từ."),
    ("引导", "yǐndǎo", "dẫn đạo", "động từ", "dẫn đường, dẫn dắt", "由一名职业司机引导一长串汽车前行", "một tài xế chuyên nghiệp dẫn một chuỗi dài ô tô tiến lên",
     "Động từ, nghĩa là dẫn đường, dẫn dắt, hướng dẫn. Chữ 导 ta đã gặp trong phần khởi động."),
    ("串", "chuàn", "xuyến", "lượng từ", "chuỗi, xâu, chùm", "一长串汽车、一串钥匙", "một chuỗi dài ô tô, một chùm chìa khóa",
     "Lượng từ, dùng cho những vật nối thành chuỗi, như chuỗi hạt, chùm chìa khóa, chùm nho."),
    ("珍珠", "zhēnzhū", "trân châu", "danh từ", "ngọc trai, trân châu", "一条线上的珍珠", "những hạt ngọc trai trên một sợi dây",
     "Danh từ, nghĩa là ngọc trai, trân châu. 珍珠奶茶 là trà sữa trân châu, chắc các bạn rất quen."),
    ("效益", "xiàoyì", "hiệu ích", "danh từ", "hiệu quả và lợi ích", "工作效益大大提高。", "Hiệu quả công việc được nâng cao rất nhiều.",
     "Danh từ, nghĩa là hiệu quả và lợi ích. 经济效益 là hiệu quả kinh tế."),
    ("抵达", "dǐdá", "để đạt", "động từ", "đến nơi, tới", "汽车抵达终点。", "Ô tô đến đích.",
     "Động từ, nghĩa là đến nơi, là cách nói văn viết của 到达."),
    ("终点", "zhōngdiǎn", "chung điểm", "danh từ", "điểm cuối, đích", "到达终点", "về đến đích",
     "Danh từ, nghĩa là điểm cuối, đích đến; trái nghĩa với 起点, điểm xuất phát."),
    ("配备", "pèibèi", "phối bị", "động từ", "trang bị", "车上配备的高科技系统", "hệ thống công nghệ cao được trang bị trên xe",
     "Động từ, nghĩa là trang bị, bố trí đầy đủ người hoặc thiết bị."),
    ("停泊", "tíngbó", "đình bạc", "động từ", "neo đậu; đỗ (xe)", "自动停泊入位", "tự động đỗ vào chỗ",
     "Động từ, nghĩa là neo đậu, vốn dùng cho tàu thuyền; trong bài dùng cho ô tô, nghĩa là đỗ xe. Chú ý: chữ 泊 ở đây đọc là bó, thanh hai."),
    ("力求", "lìqiú", "lực cầu", "động từ", "cố gắng hết sức để", "力求做到最好", "cố gắng hết sức làm tốt nhất",
     "Động từ, nghĩa là cố gắng hết sức để đạt được điều gì, phía sau là động từ hoặc cụm động từ."),
    ("丙", "bǐng", "bính", "danh từ", "thứ ba (chữ thứ ba trong thiên can)", "甲、乙、丙、丁", "thứ nhất, thứ hai, thứ ba, thứ tư",
     "Danh từ, chữ thứ ba trong thiên can, Hán Việt là Bính, thường dùng để chỉ thứ ba."),
    ("融合", "rónghé", "dung hợp", "động từ", "dung hợp, hòa nhập", "融合数字生活方式", "hòa nhập lối sống số",
     "Động từ, nghĩa là dung hợp, hòa quyện nhiều thứ làm một."),
    ("引擎", "yǐnqíng", "dẫn kình", "danh từ", "động cơ", "搜索引擎公司", "công ty công cụ tìm kiếm",
     "Danh từ, nghĩa là động cơ, phiên âm từ tiếng Anh engine. 搜索引擎 là công cụ tìm kiếm."),
    ("行列", "hángliè", "hàng liệt", "danh từ", "hàng ngũ", "加入到汽车研发的行列", "gia nhập hàng ngũ nghiên cứu phát triển ô tô",
     "Danh từ, nghĩa là hàng ngũ. Chú ý: chữ 行 ở đây đọc là háng, thanh hai."),
    ("潮流", "cháoliú", "triều lưu", "danh từ", "trào lưu, xu thế", "无法阻挡的潮流", "trào lưu không thể ngăn cản",
     "Danh từ, nghĩa là trào lưu, xu thế, dòng chảy của thời đại."),
    ("助理", "zhùlǐ", "trợ lý", "danh từ", "trợ lý", "虚拟个人助理", "trợ lý cá nhân ảo",
     "Danh từ, nghĩa là trợ lý, âm Hán Việt giống hệt tiếng Việt."),
    ("锦上添花", "jǐnshàng-tiānhuā", "cẩm thượng thiêm hoa", "thành ngữ", "thêu hoa trên gấm (đã đẹp lại thêm đẹp)", "必然的服务，而非锦上添花", "dịch vụ tất yếu, chứ không phải thêu hoa trên gấm",
     "Thành ngữ, nghĩa là thêu hoa trên gấm, tức là đã đẹp lại càng thêm đẹp, có cũng được mà không có cũng không sao. Ngược lại là 雪中送炭, đưa than sưởi ngày tuyết, tức là giúp đỡ lúc khó khăn."),
    ("保障", "bǎozhàng", "bảo chướng", "động từ", "bảo đảm, bảo vệ (an toàn, quyền lợi)", "为汽车的安全使用提供保障", "đảm bảo cho việc sử dụng ô tô an toàn",
     "Động từ, nghĩa là bảo đảm, bảo vệ cho an toàn, quyền lợi không bị tổn hại. Cũng dùng như danh từ: 提供保障, cung cấp sự bảo đảm."),
    ("丁", "dīng", "đinh", "danh từ", "thứ tư (chữ thứ tư trong thiên can)", "丁：长途行车仍靠汽油。", "Phần bốn: đi đường dài vẫn dựa vào xăng.",
     "Danh từ, chữ thứ tư trong thiên can, Hán Việt là Đinh, dùng để chỉ thứ tư."),
    ("柴油", "cháiyóu", "sài du", "danh từ", "dầu diesel", "汽油和柴油", "xăng và dầu diesel",
     "Danh từ, nghĩa là dầu diesel. Chữ 柴 nghĩa gốc là củi."),
    ("遏制", "èzhì", "át chế", "động từ", "kiềm chế, ngăn chặn", "遏制汽油、柴油的使用", "kiềm chế việc sử dụng xăng, dầu diesel",
     "Động từ, nghĩa là kiềm chế, ngăn chặn, thường dùng với những điều tiêu cực."),
    ("比重", "bǐzhòng", "tỷ trọng", "danh từ", "tỷ trọng", "电动汽车的比重一定会提高。", "Tỷ trọng ô tô điện chắc chắn sẽ tăng lên.",
     "Danh từ, nghĩa là tỷ trọng, tức phần chiếm trong tổng thể."),
    ("昂贵", "ángguì", "ngang quý", "tính từ", "đắt đỏ", "造价可能很昂贵。", "Giá thành có thể rất đắt.",
     "Tính từ, nghĩa là đắt đỏ, là cách nói văn viết của 贵."),
    ("阻碍", "zǔ'ài", "trở ngại", "động từ", "cản trở, gây trở ngại", "阻碍人们选择电动汽车", "cản trở người ta chọn ô tô điện",
     "Động từ, nghĩa là cản trở, gây trở ngại. Cũng có thể dùng như danh từ."),
    ("排除", "páichú", "bài trừ", "động từ", "loại trừ, gạt bỏ", "不排除这种可能。", "Không loại trừ khả năng này.",
     "Động từ, nghĩa là loại trừ, gạt bỏ. 不排除 là không loại trừ, tức là vẫn có khả năng xảy ra."),
    ("确保", "quèbǎo", "xác bảo", "động từ", "đảm bảo chắc chắn", "确保减少污染", "đảm bảo chắc chắn giảm ô nhiễm",
     "Động từ, nghĩa là đảm bảo chắc chắn, mức độ khẳng định rất cao."),
    ("排放", "páifàng", "bài phóng", "động từ", "thải ra, xả ra", "废气的排放必须减少。", "Lượng khí thải phải được giảm bớt.",
     "Động từ, nghĩa là thải ra, xả ra, dùng cho khí thải, nước thải."),
    ("代价", "dàijià", "đại giá", "danh từ", "cái giá (phải trả)", "付出了巨大的代价", "đã trả một cái giá rất lớn",
     "Danh từ, nghĩa là cái giá phải trả. 付出代价 là trả giá."),
    ("伴侣", "bànlǚ", "bạn lữ", "danh từ", "bạn đồng hành, bạn đời", "生活中不可缺少的伴侣", "người bạn đồng hành không thể thiếu trong cuộc sống",
     "Danh từ, nghĩa là bạn đồng hành, bạn đời. Trong bài, ô tô được ví như người bạn đồng hành của con người."),
    ("支柱", "zhīzhù", "chi trụ", "danh từ", "cột chống; trụ cột", "支柱产业", "ngành công nghiệp trụ cột",
     "Danh từ. Nghĩa đen là cột chống; nghĩa bóng là trụ cột. 支柱产业 là ngành công nghiệp trụ cột."),
]

GROUPS = [3] * 16 + [2, 2]  # 52 từ → 18 nhóm
assert sum(GROUPS) == len(V)

add("bullets", chapter="Từ mới (52 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 22 có 52 từ mới, chia thành 18 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý các từ có âm đọc đặc biệt: 堵塞 (sè), 停泊 (bó), 行列 (háng)"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có năm mươi hai từ, thầy chia thành mười tám nhóm nhỏ, mỗi nhóm hai hoặc ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ, phần lớn lấy từ chính bài khóa."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số từ có âm đọc đặc biệt, như 堵塞，停泊 và 行列, thầy sẽ nhắc khi gặp. Chúng ta bắt đầu nhé.")])

g = 0
for size in GROUPS:
    group = V[g:g + size]
    words, say = [], []
    for i, (zh, py, hv, loai, vi, ex, exvi, expl) in enumerate(group):
        n = g + i + 1
        words.append({"zh": zh, "py": py, "hv": hv.upper(), "loai": f"{n}. {loai}", "vi": vi, "ex": ex, "exvi": exvi})
        say.append(F(i, f"Từ số {n}: {zh}。 {zh}。 Hán Việt là {hv}.", zr=120))
        say.append(F(i, f"{expl} Ví dụ: {ex}{'' if ex[-1] in '。…？！' else '，'} {exvi[0].upper() + exvi[1:]}{'' if exvi.endswith('.') else '.'}", zr=130))
    add("vocab", section="Từ mới 生词", title=f"Từ mới ({g + 1}–{g + len(group)} / {len(V)})",
        words=words, say=say)
    g += size

# ======================= BÀI KHÓA =======================
P = [
    ("每次遇到交通堵塞，那些滞留在路上，被堵车折磨得心烦意乱的人们就会想：汽车要是也有双翼，能飞起来就好了。人们的期盼，有可能变为现实吗？",
     "Mỗi lần gặp tắc đường, những người bị kẹt lại trên đường, bị cảnh tắc xe dày vò đến mức bực bội rối bời, đều sẽ nghĩ: giá mà ô tô cũng có đôi cánh, bay lên được thì hay biết mấy. Mong ước ấy của con người liệu có thể trở thành hiện thực không?",
     ["被堵车折磨得心烦意乱 là câu bị động với 被, sau đó là bổ ngữ trình độ 得. Nghĩa là bị tắc đường dày vò đến mức bực bội. 心烦意乱 là thành ngữ chỉ tâm trạng bực bội, rối như tơ vò.",
      "要是……就好了 nghĩa là giá mà… thì tốt biết mấy, dùng để nói một mong ước. 期盼 là sự mong đợi, 变为现实 là trở thành hiện thực."]),
    ("2050年，汽车会是什么样？别的不敢担保，以下四点大体为我们勾画出了2050年汽车的轮廓。",
     "Năm 2050, ô tô sẽ như thế nào? Những chuyện khác thì không dám đảm bảo, nhưng bốn điểm dưới đây về đại thể đã phác họa cho chúng ta hình dáng của ô tô năm 2050.",
     ["别的不敢担保 nghĩa là những chuyện khác thì không dám đảm bảo. Từ 担保 lát nữa ta sẽ phân biệt với 保证.",
      "勾画出……的轮廓 là phác họa ra đường nét của…. Câu này mở ra bốn phần của bài, được đánh số bằng 甲，乙，丙，丁, chứ không phải bằng một, hai, ba, bốn."]),
    ("甲：更加清洁、安全。我们首先要问的是，2050年汽车还会存在吗？我们常常听到这样的指责：北极冰川在融化；空气质量在下降；石油资源日益紧缺；每年全球一百多万人死于交通事故，都是汽车惹的祸。",
     "Phần một (甲): Sạch hơn, an toàn hơn. Câu hỏi đầu tiên chúng ta phải đặt ra là: năm 2050 ô tô có còn tồn tại không? Chúng ta thường nghe những lời chỉ trích như thế này: băng ở Bắc Cực đang tan chảy; chất lượng không khí đang đi xuống; tài nguyên dầu mỏ ngày càng khan hiếm; mỗi năm trên toàn cầu có hơn một triệu người chết vì tai nạn giao thông – tất cả đều là tai họa do ô tô gây ra.",
     ["日益 nghĩa là ngày càng, văn viết: 日益紧缺, ngày càng khan hiếm. 死于 nghĩa là chết vì; chữ 于 trong văn viết có thể mang nghĩa ở, vì, từ.",
      "惹祸 là gây ra tai họa; 都是汽车惹的祸 là tất cả đều là tai họa do ô tô gây ra. Các bạn chú ý cách dùng dấu chấm phẩy để liệt kê một loạt lời chỉ trích."]),
    ("鉴于以上劣迹，人类会不会忍痛割爱？根据优胜劣汰的原则，汽车会不会被取代？",
     "Xét đến những tội trạng kể trên, liệu loài người có nén đau từ bỏ thứ mình yêu thích không? Theo nguyên tắc mạnh được yếu thua, liệu ô tô có bị thay thế không?",
     ["鉴于 nghĩa là xét thấy, căn cứ vào, văn viết. 劣迹 là hành vi xấu, vết nhơ, chính là từ có chữ 迹 trong phần khởi động.",
      "忍痛割爱 là thành ngữ: nén đau mà từ bỏ thứ mình yêu quý. Hai câu hỏi liên tiếp 会不会 tạo cảm giác băn khoăn, thu hút người đọc."]),
    ("一切皆有可能，但作为一种将人解放出来的灵活的交通工具，动不动就要将其淘汰，似乎不是明智之举，根本出路还是要在清洁环保、规范驾车出行上下功夫。谋求这一交通工具的清洁、安全，是2050年对汽车最起码的要求。",
     "Mọi thứ đều có thể xảy ra, nhưng ô tô là một phương tiện giao thông linh hoạt đã giải phóng con người, hơi một chút là đòi loại bỏ nó thì dường như không phải là việc làm sáng suốt. Lối thoát căn bản vẫn là phải dồn sức vào việc làm cho xe sạch, thân thiện với môi trường và lái xe đi lại đúng quy tắc. Mưu cầu sự sạch sẽ, an toàn cho phương tiện giao thông này là yêu cầu tối thiểu đối với ô tô năm 2050.",
     ["动不动就要将其淘汰 nghĩa là hơi một tí là đòi loại bỏ nó. 动不动 chính là điểm ngữ pháp thứ nhất của bài. 将其 là cách nói văn viết của 把它.",
      "明智之举 là việc làm sáng suốt. 在……上下功夫 nghĩa là dồn công sức vào việc gì. 最起码 nghĩa là tối thiểu, ít nhất."]),
    ("乙：能自动行驶。2050年，无人干预，能够自动在平坦的高速路上奔驰的车辆将会走进家庭。",
     "Phần hai (乙): Có thể tự động lái. Năm 2050, những chiếc xe không cần người can thiệp, có thể tự động phóng nhanh trên đường cao tốc bằng phẳng sẽ đi vào các gia đình.",
     ["Chủ ngữ của câu rất dài: 无人干预，能够自动在平坦的高速路上奔驰的车辆, những chiếc xe không cần người can thiệp, tự chạy trên đường cao tốc. Vị ngữ chỉ là 将会走进家庭, sẽ đi vào gia đình, tức là trở nên phổ biến.",
      "无人 là không có người. Ví dụ 无人驾驶 là lái xe không người, tức xe tự lái."]),
    ("欧洲正试图实现由一名职业司机驾车引导一长串汽车前行，它们像是一条线上的珍珠，在路上移动。被引导车辆上的驾驶者可以工作，也可以休息，职业司机的工作效益也将大大提高。",
     "Châu Âu đang thử thực hiện việc để một tài xế chuyên nghiệp lái xe dẫn đầu một chuỗi dài ô tô cùng tiến lên, chúng giống như những hạt ngọc trai trên một sợi dây, di chuyển trên đường. Người lái trên các xe được dẫn đường có thể làm việc, cũng có thể nghỉ ngơi, hiệu quả làm việc của tài xế chuyên nghiệp cũng sẽ được nâng cao rất nhiều.",
     ["由……引导…… nghĩa là do ai đó dẫn dắt. 一长串汽车 là một chuỗi dài ô tô, 串 là lượng từ chỉ chuỗi, xâu.",
      "像是一条线上的珍珠 là phép so sánh rất hình ảnh: đoàn xe nối đuôi nhau như chuỗi ngọc trai. Chú ý cặp từ trái nghĩa 工作 và 休息, lát nữa ta sẽ gặp lại trong phần liên kết từ vựng."]),
    ("汽车抵达终点后，车上配备的高科技系统能使车辆自动停泊入位。这就是人类力求实现的汽车自动行驶。",
     "Sau khi ô tô đến đích, hệ thống công nghệ cao được trang bị trên xe có thể giúp xe tự động đỗ vào chỗ. Đây chính là việc ô tô tự động lái mà con người đang ra sức thực hiện.",
     ["能使车辆自动停泊入位: chữ 使 nghĩa là làm cho, khiến cho. 停泊 vốn dùng cho tàu thuyền neo đậu, ở đây dùng cho xe đỗ. 入位 là vào đúng chỗ.",
      "力求实现 nghĩa là ra sức thực hiện, cố gắng hết mức để đạt được."]),
    ("丙：融合数字生活方式。某家著名的搜索引擎公司意识到，为个人驾驶提供服务蕴藏着巨大的商机，于是，他们迫不及待地加入到汽车研发的行列，车企与电脑公司合作几乎成了无法阻挡的潮流。",
     "Phần ba (丙): Hòa nhập lối sống số. Một công ty công cụ tìm kiếm nổi tiếng nhận ra rằng việc cung cấp dịch vụ cho người lái xe cá nhân ẩn chứa cơ hội kinh doanh rất lớn, vì vậy họ nóng lòng gia nhập hàng ngũ nghiên cứu phát triển ô tô; việc các hãng xe hợp tác với các công ty máy tính gần như đã trở thành một trào lưu không gì ngăn cản được.",
     ["蕴藏着巨大的商机 là ẩn chứa cơ hội kinh doanh to lớn; 商机 là cơ hội kinh doanh. 迫不及待 là thành ngữ: nóng lòng, không chờ đợi được nữa.",
      "加入到……的行列 là gia nhập hàng ngũ…. 车企 là viết tắt của 汽车企业, doanh nghiệp ô tô. 无法阻挡 là không thể ngăn cản."]),
    ("创造虚拟个人助理，为汽车用户提供路线、交通信息和日程安排等方面的帮助，在2050年将会是必然的服务，而非锦上添花。数字生活方式将完全与汽车融为一体，为汽车的方便、安全使用提供保障。",
     "Tạo ra trợ lý cá nhân ảo, giúp người dùng ô tô về lộ trình, thông tin giao thông, sắp xếp lịch trình…, vào năm 2050 sẽ là dịch vụ tất yếu, chứ không phải là thêu hoa trên gấm. Lối sống số sẽ hoàn toàn hòa làm một với ô tô, đảm bảo cho việc sử dụng ô tô thuận tiện và an toàn.",
     ["而非 nghĩa là chứ không phải, văn viết của 而不是. Ý tác giả là trợ lý ảo sẽ là thứ bắt buộc phải có, chứ không chỉ là thứ thêm vào cho đẹp.",
      "融为一体 là hòa làm một. 为……提供保障 là cung cấp sự bảo đảm cho…."]),
    ("丁：长途行车仍靠汽油。2050年的汽车动力是什么？电力？风力？还是依然用汽油和柴油？有人会说，清洁能源的开发就是要遏制汽油、柴油的使用。",
     "Phần bốn (丁): Đi đường dài vẫn dựa vào xăng. Động lực của ô tô năm 2050 là gì? Điện? Sức gió? Hay vẫn dùng xăng và dầu diesel? Có người sẽ nói, phát triển năng lượng sạch chính là để kiềm chế việc sử dụng xăng và dầu diesel.",
     ["长途行车 là lái xe đường dài. 仍靠 nghĩa là vẫn dựa vào. 依然 nghĩa là vẫn như cũ.",
      "Tác giả dùng một loạt câu hỏi ngắn: 电力？风力？ để gợi suy nghĩ cho người đọc. 遏制 thường đi với những điều tiêu cực, như 遏制污染."]),
    ("没错，作为日常交通工具，电动汽车的比重一定会提高，可是跑长途呢？电动汽车也许能承受超远距离行驶，但电池可能很重，造价可能很昂贵，充电的时间可能很长，这些都可能成为阻碍人们选择电动汽车的理由。",
     "Đúng vậy, là phương tiện đi lại hàng ngày, tỷ trọng ô tô điện chắc chắn sẽ tăng lên, nhưng còn chạy đường dài thì sao? Ô tô điện có lẽ chịu được việc chạy quãng đường siêu xa, nhưng pin có thể rất nặng, giá thành có thể rất đắt, thời gian sạc có thể rất lâu; tất cả những điều này đều có thể trở thành lý do cản trở người ta chọn ô tô điện.",
     ["可是跑长途呢: câu hỏi với 呢 nghĩa là còn… thì sao. 承受 là chịu đựng được. 造价 là giá thành chế tạo.",
      "Các bạn chú ý ba tính từ 重，昂贵，长 cùng miêu tả cục pin: nặng, đắt, sạc lâu. Đây chính là ví dụ về liên kết từ vựng mà ta học ở cuối bài."]),
    ("所以，不排除长距离行车还用汽油或柴油，因此为了确保减少污染，燃料的使用效率必须提高，废气的排放必须减少。",
     "Vì vậy, không loại trừ khả năng xe chạy đường dài vẫn dùng xăng hoặc dầu diesel; do đó, để đảm bảo chắc chắn giảm ô nhiễm, hiệu suất sử dụng nhiên liệu phải được nâng cao, khí thải phải được giảm bớt.",
     ["不排除 nghĩa là không loại trừ, tức là vẫn có khả năng. 为了确保…… là để đảm bảo chắc chắn….",
      "Hai vế 必须提高 và 必须减少 đặt song song, tạo nhịp điệu cân đối. 燃料 là nhiên liệu, 废气 là khí thải."]),
    ("长久以来，汽车作为人类重要的交通工具与我们相伴相随，人类也为此付出了巨大的代价。",
     "Từ lâu nay, ô tô với tư cách là phương tiện giao thông quan trọng của loài người đã luôn đồng hành cùng chúng ta, và loài người cũng vì thế mà phải trả một cái giá rất lớn.",
     ["长久以来 là từ lâu nay. 作为 là với tư cách là. 相伴相随 là luôn đi cùng, gắn bó bên nhau.",
      "为此 nghĩa là vì việc này. 付出了巨大的代价 là đã phải trả một cái giá rất đắt."]),
    ("2050年，如果汽车还是我们生活中不可缺少的伴侣，它在我们的经济生活中还扮演支柱产业的角色，它必须是清洁的、安全的，它必须符合可持续发展的原则。",
     "Năm 2050, nếu ô tô vẫn là người bạn đồng hành không thể thiếu trong cuộc sống của chúng ta, nếu trong đời sống kinh tế nó vẫn đóng vai trò ngành công nghiệp trụ cột, thì nó phải sạch, phải an toàn, phải phù hợp với nguyên tắc phát triển bền vững.",
     ["扮演……的角色 là đóng vai trò…. 支柱产业 là ngành công nghiệp trụ cột. 可持续发展 là phát triển bền vững.",
      "Tác giả lặp lại chữ 它 và hai lần 它必须 để kết bài thật mạnh mẽ, nhấn mạnh lại yêu cầu sạch và an toàn đã nêu ở phần đầu. Mở bài và kết bài hô ứng với nhau."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 2050年的汽车什么样",
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 二零五零年的汽车什么样, dài chín trăm tám mươi sáu chữ, được cải biên từ một bài báo cùng tên trên tờ 参考消息.",
         F(0, "Thầy chia bài thành mười lăm đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, (zh, vi, notes) in enumerate(P, 1):
    zsize = 54 if len(zh) <= 100 else 50 if len(zh) <= 115 else 46
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, zh_num(zh), cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi, cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Tóm tắt nội dung", section="Bài khóa 课文", title="Bố cục bài khóa", size=36,
    items=["## Mở bài: tắc đường → mơ ô tô biết bay · 4 điểm phác họa ô tô năm 2050",
           "甲 Sạch hơn, an toàn hơn: tội trạng của ô tô hiện nay → lối thoát căn bản",
           "乙 Tự động lái: tài xế chuyên nghiệp dẫn đoàn xe · tự động đỗ xe vào chỗ",
           "丙 Hòa nhập lối sống số: hãng xe hợp tác với công ty tìm kiếm · trợ lý cá nhân ảo",
           "丁 Nhiên liệu: ưu, nhược điểm của ô tô điện · xe xăng, dầu vẫn dùng nhưng phải hiệu quả hơn",
           "## Kết bài: ô tô năm 2050 phải sạch, an toàn, phát triển bền vững"],
    say=["Chúng ta cùng nhìn lại bố cục của cả bài khóa, theo đúng gợi ý ở bài tập năm trong sách.",
         F(0, "Mở bài: bị tắc đường, người ta mơ ô tô có cánh để bay. Tác giả đặt câu hỏi ô tô năm hai nghìn không trăm năm mươi sẽ ra sao, rồi nêu bốn điểm."),
         F(1, "Phần 甲: sạch hơn, an toàn hơn. Tác giả nêu những tội trạng của ô tô hiện nay, như ô nhiễm, tai nạn, rồi chỉ ra lối thoát căn bản là làm cho xe sạch và lái xe đúng quy tắc."),
         F(2, "Phần 乙: tự động lái. Một tài xế chuyên nghiệp dẫn cả đoàn xe, đến nơi thì xe tự đỗ vào chỗ."),
         F(3, "Phần 丙: hòa nhập lối sống số. Hãng xe hợp tác với công ty công cụ tìm kiếm, tạo ra trợ lý cá nhân ảo."),
         F(4, "Phần 丁: nhiên liệu. Ô tô điện có ưu điểm nhưng cũng có nhược điểm khi đi đường dài, nên xe xăng, dầu vẫn được dùng, nhưng phải tiết kiệm nhiên liệu và giảm khí thải."),
         F(5, "Kết bài: nếu ô tô vẫn là người bạn đồng hành của con người, thì nó phải sạch, an toàn và phù hợp với phát triển bền vững. Bố cục này rất có ích khi các bạn làm bài tập viết tóm tắt ở cuối bài.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 动不动", section="Ngữ pháp 注释", title="1. 动不动 dòngbudòng – hơi một tí là…",
    items=["Biểu thị rất dễ xảy ra một phản ứng hay hành động nào đó",
           "Thường dùng cho việc không mong muốn · Cấu trúc: 动不动 + 就 + động từ",
           "他最近工作忙、压力大，动不动就着急、发脾气。",
           "作为一种将人解放出来的灵活的交通工具，动不动就要将其淘汰，似乎不是明智之举……",
           "父母要多与孩子交流，不要动不动就呵斥压服，以「住嘴」来强行制止孩子发表意见。"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là 动不动.",
         F(0, "动不动 biểu thị việc rất dễ xảy ra một phản ứng hay hành động nào đó. Tiếng Việt dịch là: hơi một tí là, động một chút là, hở ra là."),
         F(1, "Nó thường dùng cho những việc không mong muốn, mang sắc thái phàn nàn, chê trách. Cấu trúc: 动不动 cộng 就 cộng động từ."),
         F(2, "Ví dụ một: 他最近工作忙、压力大，动不动就着急、发脾气。 Dạo này anh ấy công việc bận rộn, áp lực lớn, hơi một tí là sốt ruột, nổi cáu."),
         F(3, "Ví dụ hai, lấy từ bài khóa: 作为一种将人解放出来的灵活的交通工具，动不动就要将其淘汰，似乎不是明智之举。 Ô tô là phương tiện linh hoạt đã giải phóng con người, hơi một chút là đòi loại bỏ nó thì dường như không sáng suốt."),
         F(4, "Ví dụ ba: 父母要多与孩子交流，不要动不动就呵斥压服，以住嘴来强行制止孩子发表意见。 Cha mẹ nên trò chuyện nhiều với con, đừng hơi một tí là quát mắng, dùng câu im miệng để ép con không được nói lên ý kiến.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: dùng 动不动 hoàn thành câu", reveal=True, size=40,
    items=["(1) 他身体很弱，……",
           "Đáp án: ……动不动就感冒发烧。",
           "(2) 你的电脑该换了，……，多耽误事啊。",
           "Đáp án: ……动不动就死机……",
           "(3) 对孩子要耐心，……",
           "Đáp án: ……不要动不动就发火、打骂孩子。"],
    say=[F(0, "Luyện tập. Câu một: 他身体很弱，…… Sức khỏe anh ấy rất yếu, hơi một tí là sao? Các bạn hãy tạm dừng và thử hoàn thành câu."),
         F(1, "Đáp án gợi ý: 他身体很弱，动不动就感冒发烧。 Anh ấy sức khỏe rất yếu, hơi một tí là cảm sốt."),
         F(2, "Câu hai: 你的电脑该换了，……，多耽误事啊。 Máy tính của bạn nên thay rồi, như thế thì lỡ việc biết bao nhiêu."),
         F(3, "Đáp án gợi ý: 你的电脑该换了，动不动就死机，多耽误事啊。 Máy tính của bạn nên thay đi, hơi một tí là treo máy, lỡ việc biết bao."),
         F(4, "Câu ba: 对孩子要耐心，…… Với trẻ con phải kiên nhẫn."),
         F(5, "Đáp án gợi ý: 对孩子要耐心，不要动不动就发火、打骂孩子。 Với trẻ con phải kiên nhẫn, đừng hơi một tí là nổi nóng, đánh mắng con. Các bạn để ý, cả ba câu đều nói về việc không mong muốn.")])

add("bullets", chapter="Ngữ pháp: 甲乙丙丁", section="Ngữ pháp 注释", title="2. 甲乙丙丁…… – dùng để sắp xếp thứ tự",
    items=["Dùng để đánh số thứ tự sự vật, giống 1, 2, 3, 4 hoặc A, B, C, D",
           "甲：更加清洁、安全　乙：能自动行驶　丙：融合数字生活方式",
           "Thường gặp trong văn bản, đề thi, câu đố: 甲方 bên A · 乙方 bên B (hợp đồng)",
           "甲乙丙丁四人的车分别为白色、银色、蓝色和红色。"],
    say=["Điểm ngữ pháp thứ hai là cách dùng 甲，乙，丙，丁.",
         F(0, "Bốn chữ này được dùng để đánh số thứ tự cho sự vật, giống như một, hai, ba, bốn, hoặc A, B, C, D."),
         F(1, "Ví dụ chính là bố cục bài khóa: 甲：更加清洁、安全。乙：能自动行驶。丙：融合数字生活方式。 Phần một, phần hai, phần ba."),
         F(2, "Cách đánh số này rất hay gặp trong văn bản, đề thi và câu đố. Ví dụ trong hợp đồng, 甲方 là bên A, 乙方 là bên B."),
         F(3, "Hay trong câu đố: 甲乙丙丁四人的车分别为白色、银色、蓝色和红色。 Xe của bốn người Giáp, Ất, Bính, Đinh lần lượt là màu trắng, bạc, xanh lam và đỏ. Lát nữa chúng ta sẽ giải câu đố này.")])

add("bullets", section="Ngữ pháp 注释", title="Thiên can, địa chi (天干地支)", size=38,
    items=["天干 (10 chữ): 甲 乙 丙 丁 戊 己 庚 辛 壬 癸",
           "地支 (12 chữ): 子 丑 寅 卯 辰 巳 午 未 申 酉 戌 亥",
           "Ghép lần lượt → 60 tổ hợp, tuần hoàn → ghi ngày, năm (nông lịch)",
           "2015年，农历乙未。",
           "甲午战争发生在1894年。",
           "甲申年来临之际，祝您健康幸福，心想事成。"],
    say=["Ngoài ra, sách còn giới thiệu một kiến thức văn hóa rất gần gũi với người Việt: thiên can và địa chi, tiếng Trung gọi tắt là 干支.",
         F(0, "天干 có mười chữ: 甲，乙，丙，丁，戊，己，庚，辛，壬，癸。 Tiếng Việt chúng ta đọc là: Giáp, Ất, Bính, Đinh, Mậu, Kỷ, Canh, Tân, Nhâm, Quý."),
         F(1, "地支 có mười hai chữ: 子，丑，寅，卯，辰，巳，午，未，申，酉，戌，亥。 Tức là: Tý, Sửu, Dần, Mão, Thìn, Tỵ, Ngọ, Mùi, Thân, Dậu, Tuất, Hợi."),
         F(2, "Người xưa ghép lần lượt mười chữ thiên can với mười hai chữ địa chi, được sáu mươi tổ hợp, cứ thế tuần hoàn, dùng để ghi ngày và ghi năm. Ngày nay nông lịch Trung Quốc, cũng như âm lịch Việt Nam, vẫn dùng cách này."),
         F(3, "Ví dụ: 二零一五年，农历乙未。 Năm hai nghìn không trăm mười lăm là năm Ất Mùi."),
         F(4, "甲午战争发生在一八九四年。 Chiến tranh Giáp Ngọ xảy ra năm một nghìn tám trăm chín mươi tư."),
         F(5, "甲申年来临之际，祝您健康幸福，心想事成。 Nhân dịp năm Giáp Thân đến, chúc bạn mạnh khỏe hạnh phúc, cầu được ước thấy. 心想事成 là câu chúc Tết rất phổ biến.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập 1: giải câu đố 甲乙丙丁", reveal=True, size=34,
    items=["甲乙丙丁四人的车分别为白色、银色、蓝色和红色。",
           "甲说：乙的车不是白色。乙说：丙的车是红色的。丙说：丁的车不是蓝色的。",
           "丁说：甲、乙、丙三人中有一个人的车是红色的，而且只有这个人说的是实话。",
           "假如丁说的是实话，正确的是：A. 甲白乙银　B. 乙蓝丙红　C. 丙白丁蓝　D. 丙银甲红",
           "Đáp án: C – 甲 đỏ (người nói thật) · 乙 bạc · 丙 trắng · 丁 xanh lam"],
    say=[F(0, "Luyện tập một: câu đố trong sách. 甲乙丙丁四人的车分别为白色、银色、蓝色和红色。 Xe của bốn người lần lượt có màu trắng, bạc, xanh lam và đỏ."),
         F(1, "Khi được hỏi màu xe, 甲说：乙的车不是白色。 Giáp nói: xe của Ất không phải màu trắng. 乙说：丙的车是红色的。 Ất nói: xe của Bính màu đỏ. 丙说：丁的车不是蓝色的。 Bính nói: xe của Đinh không phải màu xanh."),
         F(2, "丁说：甲、乙、丙三人中有一个人的车是红色的，而且只有这个人说的是实话。 Đinh nói: trong ba người Giáp, Ất, Bính có một người có xe màu đỏ, và chỉ người đó nói thật."),
         F(3, "假如丁说的是实话，那么以下说法正确的是哪一个？ Nếu Đinh nói thật, thì câu nào đúng? Các bạn tạm dừng video và suy luận nhé."),
         F(4, "Đáp án là C. Nếu Bính có xe đỏ thì câu của Ất cũng đúng, vô lý; nếu Ất có xe đỏ thì Ất nói thật, xe Bính cũng đỏ, cũng vô lý. Vậy Giáp có xe đỏ và nói thật, nên xe Ất không phải màu trắng; Bính nói sai, nên xe Đinh màu xanh lam. Còn lại Ất màu bạc, Bính màu trắng.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập 2: câu nào có 甲乙丙丁 mang nghĩa khác?", reveal=True, size=38,
    items=["(1) 她姓甲，叫甲吉。",
           "(2) 他叫李甲申，肯定是1944年出生的，那一年是甲申年。",
           "(3) 这篇文章分为甲、乙、丙三部分，我最喜欢的是第三部分。",
           "Đáp án: câu (1) – 甲 là họ người, không phải thứ tự hay thiên can",
           "(2) 甲申 là năm can chi · (3) 甲、乙、丙 là thứ tự – giống cách dùng đã học"],
    say=["Luyện tập hai: trong các câu sau, câu nào có 甲乙丙丁 mang nghĩa khác với cách dùng vừa học?",
         F(0, "Câu một: 她姓甲，叫甲吉。 Cô ấy họ Giáp, tên là Giáp Cát."),
         F(1, "Câu hai: 他叫李甲申，肯定是一九四四年出生的，那一年是甲申年。 Anh ấy tên là Lý Giáp Thân, chắc chắn sinh năm một nghìn chín trăm bốn mươi tư, năm đó là năm Giáp Thân."),
         F(2, "Câu ba: 这篇文章分为甲、乙、丙三部分，我最喜欢的是第三部分。 Bài văn này chia làm ba phần Giáp, Ất, Bính, tôi thích nhất phần thứ ba."),
         F(3, "Đáp án: câu một. Ở đây 甲 chỉ là một họ người, không phải thứ tự, cũng không phải thiên can."),
         F(4, "Câu hai, 甲申 là tên năm theo can chi; câu ba, 甲、乙、丙 dùng để đánh số các phần. Cả hai đều giống cách dùng đã học.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 担保 – 保证", section="Phân biệt từ 词语辨析", title="Phân biệt 担保 và 保证",
    common="Giống nhau: biểu thị chịu trách nhiệm, khẳng định không xảy ra vấn đề hoặc nhất định làm được. Ví dụ: 出不了事，我敢担保/保证。",
    cols=[{"head": "担保",
           "lines": ["(1) Phía sau không mang danh từ, chỉ mang động từ hoặc mệnh đề",
                     "Sai: 我们要担保产品质量。",
                     "Đúng: 我敢担保，产品质量没有问题。",
                     "(2) Không có tính danh từ"]},
          {"head": "保证",
           "lines": ["(1) Phía sau mang được danh từ: đảm bảo yêu cầu, tiêu chuẩn đã định, không giảm bớt",
                     "Đúng: 我们要保证产品质量。",
                     "(2) Làm được danh từ: điều bảo đảm, sự bảo đảm",
                     "Đúng: 安定团结是我们取得胜利的保证。"]}],
    say=["Tiếp theo là phần phân biệt từ: 担保 và 保证. Tiếng Việt đều có thể dịch là đảm bảo, nên học sinh rất hay nhầm.",
         "Điểm giống nhau: cả hai đều biểu thị chịu trách nhiệm, khẳng định chắc chắn không có vấn đề hoặc nhất định làm được. Ví dụ: 出不了事，我敢担保, hoặc 我敢保证, đều đúng. Không xảy ra chuyện gì đâu, tôi dám đảm bảo.",
         F(0, "Điểm khác thứ nhất. Phía sau 担保 không thể mang danh từ, chỉ có thể mang động từ hoặc một mệnh đề nhỏ."),
         F(0, "Ví dụ: 我们要担保产品质量 là sai, vì 产品质量 là danh từ. Phải nói: 我敢担保，产品质量没有问题。 Tôi dám đảm bảo, chất lượng sản phẩm không có vấn đề."),
         F(1, "Còn phía sau 保证 thì mang được danh từ, biểu thị đảm bảo đạt được yêu cầu, tiêu chuẩn đã định, không giảm bớt. Ví dụ: 我们要保证产品质量。 Chúng ta phải đảm bảo chất lượng sản phẩm."),
         F(0, "Điểm khác thứ hai. 担保 không có cách dùng danh từ."),
         F(1, "Còn 保证 làm được danh từ, chỉ điều bảo đảm. Ví dụ: 安定团结是我们取得胜利的保证。 Ổn định và đoàn kết là điều bảo đảm cho thắng lợi của chúng ta."),
         "Mẹo nhớ: 担保 có chữ 担, là gánh vác, nhấn mạnh người nói đứng ra gánh trách nhiệm, phía sau là cả một câu. 保证 linh hoạt hơn, vừa mang được danh từ, vừa làm được danh từ."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: Đúng hay sai?", reveal=True, size=38,
    items=["(1) 他的能力很强，这件棘手的事交给他办，保证错不了。",
           "Đáp án: ĐÚNG – 保证 + mệnh đề 错不了.",
           "(2) 由于任务异常繁重，请给他们担保科研时间。",
           "Đáp án: SAI – 担保 không mang danh từ. Sửa: 请给他们保证科研时间。",
           "(3) 反复练习和精益求精是取得成功的担保。",
           "Đáp án: SAI – 担保 không làm danh từ. Sửa: ……是取得成功的保证。",
           "(4) 他语气坚定地对将军说：保证圆满完成任务！",
           "Đáp án: ĐÚNG – 保证 + cụm động từ 圆满完成任务."],
    say=[F(0, "Bây giờ chúng ta làm thử. Câu một: 他的能力很强，这件棘手的事交给他办，保证错不了。 Năng lực anh ấy rất tốt, việc khó nhằn này giao cho anh ấy, đảm bảo không sai được. Đúng hay sai? Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: đúng. Phía sau 保证 là mệnh đề 错不了, hoàn toàn hợp lý."),
         F(2, "Câu hai: 由于任务异常繁重，请给他们担保科研时间。 Vì nhiệm vụ vô cùng nặng nề, xin hãy đảm bảo thời gian nghiên cứu khoa học cho họ."),
         F(3, "Đáp án: sai. 科研时间 là danh từ, mà 担保 không mang danh từ. Phải sửa thành 请给他们保证科研时间。"),
         F(4, "Câu ba: 反复练习和精益求精是取得成功的担保。 Luyện tập nhiều lần và không ngừng hoàn thiện là sự bảo đảm cho thành công."),
         F(5, "Đáp án: sai. Ở đây cần một danh từ, mà 担保 không có cách dùng danh từ. Phải sửa thành 是取得成功的保证。"),
         F(6, "Câu bốn: 他语气坚定地对将军说：保证圆满完成任务！ Anh ấy nói với tướng quân bằng giọng kiên định: đảm bảo hoàn thành xuất sắc nhiệm vụ!"),
         F(7, "Đáp án: đúng. 保证 cộng cụm động từ 圆满完成任务 là cách nói rất tự nhiên.")])

# ======================= KỸ NĂNG VIẾT =======================
add("bullets", chapter="Kỹ năng viết: liên kết từ vựng", section="Tu từ 篇章修辞", title="Liên kết từ vựng (词汇衔接)", size=36,
    items=["Khi thuyết minh, miêu tả một sự vật hay một bối cảnh, các từ ngữ có liên hệ về nghĩa với nhau → giúp đoạn văn mạch lạc",
           "(1) 电动汽车也许能承受超远距离行驶，但电池可能很重，造价可能很昂贵，充电的时间可能很长。",
           "→ 重、昂贵、长: cùng miêu tả pin (trọng lượng, giá thành, thời gian sạc) vượt quá mức vừa phải",
           "(2) 被引导车辆上的驾驶者可以工作，也可以休息，职业司机的工作效益也将大大提高。",
           "→ 工作 – 休息: cặp từ trái nghĩa tạo liên hệ về nghĩa",
           "(3) 我的房间靠近大海，宽敞明亮，有室内卫生间和淋浴设备，还有一个小阳台可以观赏窗外的大海。",
           "→ 卫生间、淋浴设备、小阳台: cùng là tiện nghi trong phòng"],
    say=["Phần cuối cùng về lý thuyết là kỹ năng viết: liên kết từ vựng, tiếng Trung gọi là 词汇衔接.",
         F(0, "Khi thuyết minh hay miêu tả một sự vật, một bối cảnh, một số từ ngữ trong đoạn văn có liên hệ với nhau về nghĩa. Mối liên hệ về nghĩa giữa các từ ấy gọi là liên kết từ vựng, nó có vai trò quan trọng giúp đoạn văn liền mạch."),
         F(1, "Ví dụ một, lấy từ bài khóa: 电池可能很重，造价可能很昂贵，充电的时间可能很长。 Pin có thể rất nặng, giá thành rất đắt, thời gian sạc rất lâu."),
         F(2, "Ba từ 重，昂贵，长 cùng miêu tả cục pin, về trọng lượng, giá thành và thời gian sạc, đều vượt quá mức vừa phải. Nhờ vậy ba vế câu gắn chặt với nhau."),
         F(3, "Ví dụ hai, cũng từ bài khóa: 被引导车辆上的驾驶者可以工作，也可以休息。 Người lái có thể làm việc, cũng có thể nghỉ ngơi."),
         F(4, "Cặp từ trái nghĩa 工作 và 休息 tạo thành một mối liên hệ về nghĩa."),
         F(5, "Ví dụ ba: 我的房间靠近大海，宽敞明亮，有室内卫生间和淋浴设备，还有一个小阳台可以观赏窗外的大海。 Phòng tôi gần biển, rộng rãi sáng sủa, có nhà vệ sinh và vòi sen trong phòng, lại có một ban công nhỏ để ngắm biển."),
         F(6, "Các từ 卫生间，淋浴设备，小阳台 đều là tiện nghi trong phòng, cùng nhau tạo thành liên kết về nghĩa. Khi viết, các bạn hãy chọn những từ cùng một trường nghĩa để đoạn văn chặt chẽ.")])

add("bullets", section="Tu từ 篇章修辞", title="Luyện tập: ghép 6 vế thành 3 đoạn liền mạch", reveal=True, size=32,
    items=["A. 下了火车，我做的第一件事就是买一份当地的报纸，迫不及待地在路边翻看起来",
           "B. 我们结婚十年了，大女儿七岁，小女儿四岁",
           "C. 我一向对做家事十分痛恨，但对做菜却是十分有兴趣",
           "D. 几只洋葱，几片肉，一把粉丝，一会儿就变出一个菜来，我很欣赏这种艺术",
           "E. 翻着翻着，竟然发现满满一版的招聘启事，我高兴得眉飞色舞",
           "F. 十年来我的一个突出感觉就是我的妻子从来不认错",
           "Đáp án: (1) A + E – 报纸 · 翻看 · 翻着翻着 · 一版 · 招聘启事",
           "(2) B + F – 结婚十年 · 十年来 · 妻子",
           "(3) C + D – 做菜 · 洋葱、肉、粉丝 · 变出一个菜"],
    say=["Luyện tập: dựa vào liên hệ về nghĩa giữa các từ, hãy ghép sáu vế câu sau thành ba đoạn liền mạch.",
         F(0, "A: 下了火车，我做的第一件事就是买一份当地的报纸，迫不及待地在路边翻看起来。 Xuống tàu, việc đầu tiên tôi làm là mua một tờ báo địa phương, nóng lòng đứng ngay bên đường lật xem."),
         F(1, "B: 我们结婚十年了，大女儿七岁，小女儿四岁。 Chúng tôi cưới nhau đã mười năm, con gái lớn bảy tuổi, con gái nhỏ bốn tuổi."),
         F(2, "C: 我一向对做家事十分痛恨，但对做菜却是十分有兴趣。 Tôi xưa nay rất ghét làm việc nhà, nhưng lại rất hứng thú với nấu ăn."),
         F(3, "D: 几只洋葱，几片肉，一把粉丝，一会儿就变出一个菜来，我很欣赏这种艺术。 Vài củ hành tây, mấy lát thịt, một nắm miến, loáng cái đã biến ra một món ăn, tôi rất thích nghệ thuật này."),
         F(4, "E: 翻着翻着，竟然发现满满一版的招聘启事，我高兴得眉飞色舞。 Lật mãi lật mãi, bỗng phát hiện cả một trang đầy thông báo tuyển dụng, tôi vui đến mức mặt mày hớn hở."),
         F(5, "F: 十年来我的一个突出感觉就是我的妻子从来不认错。 Mười năm qua, cảm nhận rõ nhất của tôi là vợ tôi chưa bao giờ nhận lỗi. Các bạn tạm dừng và thử ghép nhé."),
         F(6, "Đáp án. Đoạn một là A và E: 报纸，翻看，翻着翻着，一版，招聘启事 đều liên quan đến việc đọc báo."),
         F(7, "Đoạn hai là B và F: 结婚十年 nối với 十年来 và 妻子."),
         F(8, "Đoạn ba là C và D: 做菜 nối với 洋葱，肉，粉丝 và 变出一个菜. Các bạn thấy đấy, chính các từ cùng trường nghĩa là sợi dây nối các câu lại với nhau.")])

add("bullets", section="Tu từ 篇章修辞", title="Bài tập 4: sắp xếp câu theo liên kết từ vựng", reveal=True, size=34,
    items=["(1) A 是爸爸一手把我抚养大的 · B 我很不忍心 · C 我从小就没有了妈妈 · D 又要离开他 · E 好不容易等我长大了",
           "Đáp án: C – A – E – D – B",
           "(2) A 整个房间除了基本生活用品以外，其他全部被书占据 · B 就是把书籍资料剪切成卡片 · C 李先生的书房称得上是真正的书房 · D 分类做成小小的集子 · E 所谓自建资料册子 · F 他的书房中有一种非常有特色的自建资料册子 · G 方便日后取用",
           "Đáp án: C – A – F – E – B – D – G"],
    say=[F(0, "Bài tập bốn trong sách: dựa vào liên hệ về nghĩa của từ ngữ, sắp xếp lại thứ tự các câu. Câu một có năm vế: 是爸爸一手把我抚养大的，我很不忍心，我从小就没有了妈妈，又要离开他，好不容易等我长大了。 Các bạn thử sắp xếp nhé."),
         F(1, "Đáp án: C, A, E, D, B. 我从小就没有了妈妈，是爸爸一手把我抚养大的，好不容易等我长大了，又要离开他，我很不忍心。 Tôi mất mẹ từ nhỏ, một tay bố nuôi tôi khôn lớn, khó khăn lắm tôi mới lớn lên, lại phải rời xa bố, tôi thật không nỡ. Các từ 妈妈，爸爸，抚养大，长大，离开他 nối các vế lại với nhau."),
         F(2, "Câu hai có bảy vế, nói về thư phòng của ông Lý và cuốn sổ tư liệu tự làm của ông. Các bạn tạm dừng và thử sắp xếp."),
         F(3, "Đáp án: C, A, F, E, B, D, G. 李先生的书房称得上是真正的书房，整个房间除了基本生活用品以外，其他全部被书占据。他的书房中有一种非常有特色的自建资料册子，所谓自建资料册子，就是把书籍资料剪切成卡片，分类做成小小的集子，方便日后取用。 Từ 书房 nối câu C với A và F; cụm 自建资料册子 nối F với E; còn 卡片，集子，取用 nối các bước làm sổ.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ được đánh dấu", size=40,
    items=["担保 (保) → 保证 · 保险 · 确保 · 准保",
           "指责 (责) → 责任 · 负责 · 责备 · 职责",
           "平坦 (平) → 平等 · 平静 · 平安 · 和平",
           "抵达 (达) → 到达 · 发达 · 表达 · 传达",
           "停泊 (停) → 停止 · 停车 · 停留 · 暂停"],
    say=["Phần luyện tập. Bài tập một: bắt chước ví dụ, dựa vào chữ có dấu chấm bên dưới, hãy viết thêm các từ khác.",
         F(0, "Ví dụ mẫu: 担保, chữ được đánh dấu là 保. Ta có 保证，保险，确保，准保. Tức là bảo đảm, bảo hiểm, đảm bảo chắc chắn, và chắc chắn."),
         F(1, "指责, chữ được đánh dấu là 责. Có thể mở rộng thành 责任，负责，责备，职责. Tức là trách nhiệm, phụ trách, trách mắng, và chức trách."),
         F(2, "平坦, chữ được đánh dấu là 平. Có 平等，平静，平安，和平. Tức là bình đẳng, bình tĩnh, bình an, hòa bình."),
         F(3, "抵达, chữ được đánh dấu là 达. Có 到达，发达，表达，传达. Tức là đến nơi, phát triển, biểu đạt, truyền đạt."),
         F(4, "停泊, chữ được đánh dấu là 停. Có 停止，停车，停留，暂停. Tức là dừng lại, đỗ xe, lưu lại, và tạm dừng.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Hoàn thành câu bằng từ cho sẵn (1)", reveal=True, size=38,
    items=["(1) 因为恶劣的天气，机场……（滞留）",
           "Đáp án: 因为恶劣的天气，机场滞留了大量旅客。",
           "(2) 对于这个高精尖的专业，我……（大体）",
           "Đáp án: 对于这个高精尖的专业，我只是大体了解一些。",
           "(3) 看到她伤心欲绝的样子，我……（试图）",
           "Đáp án: 看到她伤心欲绝的样子，我试图安慰她，可她什么也听不进去。"],
    say=[F(0, "Bài tập hai: dùng từ cho sẵn để hoàn thành câu. Câu một, dùng từ 滞留: 因为恶劣的天气，机场…… Vì thời tiết xấu, sân bay thế nào? Các bạn tạm dừng và thử làm nhé."),
         F(1, "Đáp án gợi ý: 因为恶劣的天气，机场滞留了大量旅客。 Vì thời tiết xấu, rất nhiều hành khách bị kẹt lại ở sân bay."),
         F(2, "Câu hai, dùng 大体: 对于这个高精尖的专业，我…… Đối với chuyên ngành công nghệ cao, tinh vi này, tôi thế nào?"),
         F(3, "Đáp án gợi ý: 对于这个高精尖的专业，我只是大体了解一些。 Đối với chuyên ngành này, tôi chỉ hiểu đại khái một chút."),
         F(4, "Câu ba, dùng 试图: 看到她伤心欲绝的样子，我…… Thấy cô ấy đau lòng muốn chết, tôi thế nào?"),
         F(5, "Đáp án gợi ý: 我试图安慰她，可她什么也听不进去。 Tôi định an ủi cô ấy, nhưng cô ấy chẳng nghe lọt tai điều gì.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Hoàn thành câu bằng từ cho sẵn (2)", reveal=True, size=38,
    items=["(4) 经过十几个小时的漫长飞行，……（抵达）",
           "Đáp án: ……我们终于抵达了目的地。",
           "(5) 为了提高工作效率，公司……（配备）",
           "Đáp án: ……公司为每位员工配备了一台新电脑。",
           "(6) 演出前我们认真排练，……（力求）",
           "Đáp án: ……力求在舞台上表现得完美。"],
    say=[F(0, "Câu bốn, dùng 抵达: 经过十几个小时的漫长飞行，…… Sau hơn mười tiếng bay dài đằng đẵng, thì sao?"),
         F(1, "Đáp án gợi ý: 经过十几个小时的漫长飞行，我们终于抵达了目的地。 Sau hơn mười tiếng bay, cuối cùng chúng tôi đã đến nơi."),
         F(2, "Câu năm, dùng 配备: 为了提高工作效率，公司…… Để nâng cao hiệu suất làm việc, công ty đã làm gì?"),
         F(3, "Đáp án gợi ý: 为了提高工作效率，公司为每位员工配备了一台新电脑。 Để nâng cao hiệu suất làm việc, công ty đã trang bị cho mỗi nhân viên một máy tính mới."),
         F(4, "Câu sáu, dùng 力求: 演出前我们认真排练，…… Trước buổi biểu diễn, chúng tôi tập luyện nghiêm túc, để làm gì?"),
         F(5, "Đáp án gợi ý: 演出前我们认真排练，力求在舞台上表现得完美。 Trước buổi diễn chúng tôi tập luyện nghiêm túc, cố gắng hết sức để thể hiện hoàn hảo trên sân khấu.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 22", size=36,
    items=["Từ vựng trọng tâm: 堵塞 · 担保 · 优胜劣汰 · 引导 · 力求 · 锦上添花 · 遏制 · 确保 · 代价",
           "Ngữ pháp: 动不动 (hơi một tí là…) · 甲乙丙丁 (đánh số thứ tự; thiên can địa chi)",
           "Phân biệt: 担保 (+ động từ/mệnh đề, không làm danh từ) ≠ 保证 (+ danh từ, làm được danh từ)",
           "Viết: liên kết từ vựng – các từ cùng trường nghĩa giúp đoạn văn mạch lạc",
           "## Bài tập về nhà",
           "Rút gọn bài khóa thành đoạn văn khoảng 350 chữ theo 4 phần 甲乙丙丁, chú ý dùng liên kết từ vựng"],
    say=["Chúng ta cùng tổng kết bài hai mươi hai.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 堵塞，担保，优胜劣汰，引导，力求，锦上添花，遏制，确保，代价."),
         F(1, "Về ngữ pháp: 动不动 nghĩa là hơi một tí là, thường dùng cho việc không mong muốn. 甲，乙，丙，丁 dùng để đánh số thứ tự, và cũng là bốn chữ đầu của thiên can."),
         F(2, "Về phân biệt từ: phía sau 担保 chỉ mang động từ hoặc mệnh đề, và không làm danh từ. 保证 thì mang được danh từ, và làm được danh từ."),
         F(3, "Về kỹ năng viết: hãy dùng những từ cùng trường nghĩa, gần nghĩa hoặc trái nghĩa để các câu văn liên kết chặt chẽ với nhau."),
         F(5, "Bài tập về nhà: các bạn hãy rút gọn bài khóa thành một đoạn văn khoảng ba trăm năm mươi chữ. Hãy dựa vào bố cục bốn phần mà thầy đã tổng kết: sạch và an toàn, tự động lái, hòa nhập lối sống số, và nhiên liệu; đồng thời chú ý dùng liên kết từ vựng."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Hẹn gặp lại các bạn ở bài hai mươi ba: 大数据时代, Thời đại dữ liệu lớn. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Hạ) – Bài 22: 2050年的汽车什么样 (Ô tô năm 2050 sẽ như thế nào?)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm
    "tts_replace": {"堵塞": "堵色", "停泊": "停博", "行列": "航列", "角色": "决色", "缺觉": "缺叫"},
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai22.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
