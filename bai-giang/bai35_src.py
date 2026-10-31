#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Hạ) – Bài 35 «走近木版年画». Chạy để sinh bai35.json."""
import json
import os

TAG = "HSK 6 (Hạ) · Bài 35 · 走近木版年画"
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
    zh="走近木版年画", py="Zǒujìn mùbǎn niánhuà", vi="Bài 35: Đến gần tranh Tết khắc gỗ",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Hạ.",
         "Hôm nay chúng ta học bài ba mươi lăm: 走近木版年画。 Nghĩa là: Đến gần tranh Tết khắc gỗ.",
         "Bài này thuộc Đơn vị chín, chủ đề 古今博览, tức là nhìn rộng chuyện xưa và nay. Bài khóa kể về nguồn gốc của tranh Tết, sự ra đời của tranh Tết in khắc gỗ, và chân dung một nghệ nhân hết lòng với nghề: ông 张光宁.",
         "Người Việt chúng ta cũng có tranh Đông Hồ, một dòng tranh Tết in khắc gỗ rất nổi tiếng. Vì vậy trong bài, thầy sẽ so sánh một chút để các bạn thấy hai dòng tranh này gần gũi nhau như thế nào."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu nội dung bài khóa 走近木版年画 – nguồn gốc, kỹ thuật và nghệ nhân tranh Tết",
           "Nắm vững 51 từ mới (và từ phụ 次品), kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: phó từ 终究 và cấu trúc 愈……愈……",
           "Phân biệt hai từ 连年 và 连续",
           "Kỹ năng viết: lặp lại từ khóa, đẩy chủ đề tiến lên (重复关键词)"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa: tranh Tết bắt nguồn từ đâu, kỹ thuật in khắc gỗ ra đời thế nào, và nghệ nhân 张光宁 đã gắn bó với tranh Tết ra sao."),
         F(1, "Thứ hai, nắm vững năm mươi mốt từ mới, cộng thêm một từ phụ là 次品. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học hai điểm ngữ pháp: phó từ 终究, nghĩa là rốt cuộc, suy cho cùng; và cấu trúc 愈……愈……, nghĩa là càng… càng…, dùng trong văn viết."),
         F(3, "Thứ tư, phân biệt hai từ đều có nghĩa liên tiếp: 连年 và 连续."),
         F(4, "Thứ năm, một kỹ năng viết rất hay: lặp lại từ khóa để làm nổi bật thông tin và đẩy chủ đề tiến lên, tiếng Trung gọi là 重复关键词，推进主题."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Khởi động 1: Đồ vật này liên quan đến gì?", size=40,
    items=["对照图片熟悉下列物品的名称，并想一想这些东西跟什么有关系？",
           "门神画 ménshén huà – tranh môn thần (thần giữ cửa)",
           "碑刻 bēikè – bia khắc chữ · 拓印 tàyìn – in rập (dập chữ từ bia)",
           "墨 mò – mực (thỏi mực) · 印章 yìnzhāng – con dấu",
           "雕版 diāobǎn – bản khắc gỗ (ván in)",
           "→ Tất cả đều liên quan đến nghề in và tranh Tết khắc gỗ"],
    say=["Chúng ta bắt đầu bằng phần khởi động.",
         F(0, "对照图片熟悉下列物品的名称，并想一想这些东西跟什么有关系？ Hãy đối chiếu với hình ảnh để làm quen tên các đồ vật sau, và nghĩ xem chúng liên quan đến điều gì."),
         F(1, "Hình thứ nhất: 门神画, tranh môn thần. 门神 là vị thần giữ cửa. Ngày Tết, người Trung Quốc dán hai bức tranh vị tướng oai phong lên hai cánh cổng để trừ tà."),
         F(2, "Hình thứ hai: 碑刻, bia đá khắc chữ. Hình thứ ba: 拓印, tức là in rập: người ta đặt giấy lên mặt bia rồi vỗ mực, để chép lại chữ khắc trên bia."),
         F(3, "Hình thứ tư: 墨, thỏi mực, Hán Việt là mặc. Hình thứ năm: 印章, con dấu, Hán Việt là ấn chương."),
         F(4, "Hình thứ sáu: 雕版, bản khắc gỗ, Hán Việt là điêu bản, tức tấm ván gỗ đã khắc hình để in."),
         F(5, "Các bạn đoán ra chưa? Tất cả những thứ này đều liên quan đến nghề in, và chính là tiền thân của tranh Tết khắc gỗ mà chúng ta học hôm nay.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 画 và 展", size=36,
    items=["## 画 (họa): tranh, vẽ",
           "门神画 tranh môn thần · 年画 tranh Tết · 版画 tranh khắc · 油画 tranh sơn dầu · 国画 tranh quốc họa",
           "漫画 truyện tranh · 书画 thư họa · 图画 tranh vẽ · 字画 tranh chữ · 动画 hoạt hình",
           "画家 họa sĩ · 画展 triển lãm tranh · 画报 họa báo · 画册 tập tranh",
           "## 展 (triển): mở ra, phát triển",
           "拓展 mở rộng · 开展 triển khai · 发展 phát triển · 进展 tiến triển · 扩展 mở rộng",
           "伸展 vươn ra · 舒展 duỗi ra · 延展 kéo dài · 展开 triển khai · 展翅 dang cánh · 愁眉不展 mặt ủ mày chau"],
    say=["Phần khởi động thứ hai: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo, rất có lợi cho người Việt vì các chữ đều có âm Hán Việt quen thuộc.",
         F(0, "Nhóm thứ nhất có chữ 画, Hán Việt là họa, nghĩa là tranh, hoặc vẽ."),
         F(1, "门神画，年画，版画，油画，国画。 Tức là: tranh môn thần, tranh Tết, tranh khắc, tranh sơn dầu, và tranh quốc họa, tức tranh thủy mặc truyền thống."),
         F(2, "漫画，书画，图画，字画，动画。 Tức là: truyện tranh, thư họa, tranh vẽ, tranh chữ, và phim hoạt hình."),
         F(3, "画家，画展，画报，画册。 Tức là: họa sĩ, triển lãm tranh, họa báo, và tập tranh."),
         F(4, "Nhóm thứ hai có chữ 展, Hán Việt là triển, nghĩa là mở ra, phát triển."),
         F(5, "拓展，开展，发展，进展，扩展。 Tức là: mở rộng, triển khai, phát triển, tiến triển, mở rộng. Từ 拓展 các bạn sẽ gặp nhiều lần trong bài khóa."),
         F(6, "伸展，舒展，延展，展开，展翅，愁眉不展。 Tức là: vươn ra, duỗi ra, kéo dài, triển khai, dang cánh, và 愁眉不展, mặt ủ mày chau, lông mày không giãn ra được.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 墨 và 花", size=36,
    items=["## 墨 (mặc): mực",
           "墨水 mực nước · 墨点 vết mực · 墨盒 hộp mực · 墨汁 mực nước (thư pháp)",
           "淡墨 mực nhạt · 浓墨 mực đậm · 磨墨 mài mực · 油墨 mực in · 水墨画 tranh thủy mặc",
           "## 花 (hoa): hoa",
           "花朵 bông hoa · 花草 hoa cỏ · 花丛 khóm hoa · 花木 hoa và cây · 花卉 hoa cảnh · 花鸟 hoa điểu",
           "花瓶 bình hoa · 花盆 chậu hoa · 花坛 bồn hoa · 花农 người trồng hoa · 花园 vườn hoa · 鲜花 hoa tươi · 种花 trồng hoa"],
    say=[F(0, "Nhóm thứ ba có chữ 墨, Hán Việt là mặc, nghĩa là mực. Tiếng Việt có từ mặc khách, tức là người làm thơ văn, gắn với nghiên bút và mực."),
         F(1, "墨水，墨点，墨盒，墨汁。 Tức là: mực nước, vết mực, hộp mực, và mực nước dùng để viết thư pháp."),
         F(2, "淡墨，浓墨，磨墨，油墨，水墨画。 Tức là: mực nhạt, mực đậm, mài mực, mực in, và tranh thủy mặc. Trong bài khóa có từ 墨水儿, mực."),
         F(3, "Nhóm cuối cùng có chữ 花, Hán Việt là hoa."),
         F(4, "花朵，花草，花丛，花木，花卉，花鸟。 Tức là: bông hoa, hoa cỏ, khóm hoa, hoa và cây, hoa cảnh, và hoa điểu, tức đề tài hoa và chim trong hội họa."),
         F(5, "花瓶，花盆，花坛，花农，花园，鲜花，种花。 Tức là: bình hoa, chậu hoa, bồn hoa, người trồng hoa, vườn hoa, hoa tươi, và trồng hoa. Bài khóa có cụm 盛开的花朵, những bông hoa nở rộ."),
         "Chỉ cần nắm nghĩa của một chữ gốc, ta có thể đoán được nghĩa của cả một nhóm từ. Hãy áp dụng cách này khi học từ mới nhé."])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng)
V = [
    ("起源", "qǐyuán", "khởi nguyên", "danh từ", "nguồn gốc, khởi nguồn", "这本书介绍了年画的起源。", "Cuốn sách này giới thiệu nguồn gốc của tranh Tết.",
     "Danh từ, nghĩa là nguồn gốc, khởi nguồn của một sự vật. Âm Hán Việt là khởi nguyên, rất gần với từ khởi nguồn của tiếng Việt. Tiêu đề phần một của bài khóa chính là 年画的起源."),
    ("文献", "wénxiàn", "văn hiến", "danh từ", "tài liệu, văn bản tư liệu", "他查阅了大量历史文献。", "Anh ấy đã tra cứu rất nhiều tài liệu lịch sử.",
     "Danh từ, nghĩa là tài liệu, văn bản có giá trị tư liệu. Đây là từ dễ nhầm: văn hiến trong tiếng Việt chỉ truyền thống văn hóa lâu đời, như nền văn hiến nghìn năm; còn 文献 trong tiếng Trung là tài liệu, sách vở để tra cứu."),
    ("凶恶", "xiōng'è", "hung ác", "tính từ", "hung ác, dữ tợn", "那条狗看起来很凶恶。", "Con chó ấy trông rất dữ tợn.",
     "Tính từ, nghĩa là hung ác, dữ tợn, âm Hán Việt giống hệt tiếng Việt."),
    ("揭露", "jiēlù", "yết lộ", "động từ", "vạch trần, phơi bày", "记者揭露了事情的真相。", "Phóng viên đã vạch trần sự thật của vụ việc.",
     "Động từ, nghĩa là vạch trần, phơi bày những điều xấu bị che giấu. Trong bài có cụm 无须揭露恶行, không cần vạch tội ác."),
    ("昌盛", "chāngshèng", "xương thịnh", "tính từ", "hưng thịnh, phồn vinh", "祝愿祖国繁荣昌盛！", "Chúc Tổ quốc phồn vinh hưng thịnh!",
     "Tính từ, nghĩa là hưng thịnh, phát triển rực rỡ, thường nói về đất nước, văn hóa. Cụm 繁荣昌盛 rất hay gặp trong các lời chúc."),
    ("题材", "tícái", "đề tài", "danh từ", "đề tài, chất liệu (của tác phẩm)", "这部电影是历史题材的。", "Bộ phim này thuộc đề tài lịch sử.",
     "Danh từ, nghĩa là đề tài, tức chất liệu, nội dung mà tác phẩm văn học nghệ thuật phản ánh. Chú ý: đề tài nghiên cứu khoa học thì tiếng Trung thường nói 课题, còn 题材 dùng cho tác phẩm."),
    ("驱逐", "qūzhú", "khu trục", "động từ", "xua đuổi, đuổi đi", "人们放鞭炮是为了驱逐邪气。", "Người ta đốt pháo là để xua đuổi tà khí.",
     "Động từ, nghĩa là xua đuổi, đuổi đi. Tiếng Việt có từ tàu khu trục, chính là loại tàu dùng để đánh đuổi tàu địch."),
    ("吉祥", "jíxiáng", "cát tường", "tính từ", "may mắn, tốt lành", "祝你新年吉祥如意！", "Chúc bạn năm mới cát tường như ý!",
     "Tính từ, nghĩa là may mắn, tốt lành. 吉祥如意 là câu chúc Tết rất quen thuộc."),
    ("里程碑", "lǐchéngbēi", "lý trình bi", "danh từ", "cột mốc (quan trọng)", "造纸术的发明是一个重要的里程碑。", "Phát minh ra nghề làm giấy là một cột mốc quan trọng.",
     "Danh từ. Nghĩa đen là cột cây số ven đường; nghĩa bóng là cột mốc quan trọng, đánh dấu một giai đoạn phát triển mới."),
    ("墨水儿", "mòshuǐr", "mặc thủy", "danh từ", "mực", "我的钢笔没墨水儿了。", "Bút máy của tôi hết mực rồi.",
     "Danh từ, nghĩa là mực. Khi đọc nhớ có âm cuốn lưỡi ở cuối."),
    ("盖章", "gài zhāng", "cái chương", "động từ", "đóng dấu", "这份合同需要盖章才有效。", "Bản hợp đồng này phải đóng dấu mới có hiệu lực.",
     "Động từ ly hợp, nghĩa là đóng dấu. Có thể tách ra, ví dụ 盖个章, đóng cái dấu."),
    ("联想", "liánxiǎng", "liên tưởng", "động từ", "liên tưởng", "看到雪，我就联想到了家乡。", "Nhìn thấy tuyết, tôi liền liên tưởng đến quê nhà.",
     "Động từ, nghĩa là liên tưởng, âm Hán Việt giống hệt tiếng Việt. Thường dùng 联想到, liên tưởng đến."),
    ("涂抹", "túmǒ", "đồ mạt", "động từ", "bôi, quét, phết", "他在面包上涂抹了一层黄油。", "Anh ấy phết một lớp bơ lên bánh mì.",
     "Động từ, nghĩa là bôi, quét, phết một lớp lên bề mặt. Ngoài ra còn có nghĩa viết vẽ nguệch ngoạc. Trong bài, người thợ quét mực lên bản khắc."),
    ("终究", "zhōngjiū", "chung cứu", "phó từ", "rốt cuộc, suy cho cùng", "他终究还是个孩子。", "Suy cho cùng nó vẫn chỉ là đứa trẻ.",
     "Phó từ, nghĩa là rốt cuộc, suy cho cùng, cuối cùng vẫn. Đây là điểm ngữ pháp thứ nhất của bài, ta sẽ học kỹ ở phần sau."),
    ("烟花爆竹", "yānhuā bàozhú", "yên hoa bộc trúc", "danh từ", "pháo hoa và pháo nổ", "很多城市春节期间禁止燃放烟花爆竹。", "Nhiều thành phố cấm đốt pháo hoa, pháo nổ dịp Tết.",
     "Nghĩa là pháo hoa và pháo nổ. 烟花 là pháo hoa; 爆竹 là pháo nổ, vì ngày xưa người ta đốt ống tre cho nổ lốp bốp, nên gọi là bộc trúc."),
    ("寄托", "jìtuō", "ký thác", "động từ", "gửi gắm (hy vọng, tình cảm)", "父母把希望寄托在孩子身上。", "Cha mẹ gửi gắm hy vọng vào con cái.",
     "Động từ, nghĩa là gửi gắm hy vọng, tình cảm vào một người hay một vật. Trong bài: 寄托着百姓美好愿望的年画, những bức tranh Tết gửi gắm ước mong tốt đẹp của người dân."),
    ("增添", "zēngtiān", "tăng thiêm", "động từ", "thêm, tăng thêm", "红灯笼为节日增添了喜庆的气氛。", "Đèn lồng đỏ tăng thêm không khí vui tươi cho ngày lễ.",
     "Động từ, nghĩa là thêm vào, tăng thêm, thường đi với những từ trừu tượng như không khí, niềm vui, vẻ đẹp."),
    ("丰收", "fēngshōu", "phong thu", "động từ", "được mùa, bội thu", "今年又是一个丰收年。", "Năm nay lại là một năm được mùa.",
     "Động từ, nghĩa là được mùa, thu hoạch dồi dào. Ước mong được mùa là một đề tài rất phổ biến của tranh Tết."),
    ("发财", "fā cái", "phát tài", "động từ", "phát tài, làm giàu", "过年时人们常说：恭喜发财！", "Dịp Tết người ta thường nói: Chúc phát tài!",
     "Động từ ly hợp, nghĩa là phát tài, giàu lên. 恭喜发财 là câu chúc Tết quen thuộc nhất của người Hoa."),
    ("连年", "liánnián", "liên niên", "động từ", "nhiều năm liền", "这个地区连年干旱。", "Vùng này hạn hán nhiều năm liền.",
     "Động từ, nghĩa là nhiều năm liền. Trong bài có câu chúc 连年有余, năm nào cũng dư dả. Tranh Tết hay vẽ hoa sen và cá, vì hoa sen đọc gần với 连, còn cá đọc giống 余. Lát nữa ta sẽ phân biệt 连年 với 连续."),
    ("寓言", "yùyán", "ngụ ngôn", "danh từ", "truyện ngụ ngôn", "我小时候最爱读寓言故事。", "Hồi nhỏ tôi thích đọc truyện ngụ ngôn nhất.",
     "Danh từ, nghĩa là truyện ngụ ngôn, âm Hán Việt giống hệt tiếng Việt."),
    ("信仰", "xìnyǎng", "tín ngưỡng", "danh từ", "tín ngưỡng, niềm tin", "我们应该尊重别人的信仰。", "Chúng ta nên tôn trọng tín ngưỡng của người khác.",
     "Danh từ, nghĩa là tín ngưỡng, niềm tin sâu sắc vào một tôn giáo hay một lý tưởng."),
    ("喜闻乐见", "xǐwén-lèjiàn", "hỉ văn lạc kiến", "thành ngữ", "được ưa chuộng, thích nghe thích xem", "年画是老百姓喜闻乐见的艺术形式。", "Tranh Tết là loại hình nghệ thuật được người dân ưa chuộng.",
     "Thành ngữ, nghĩa đen là thích nghe, vui xem, tức là được mọi người yêu thích, ưa chuộng."),
    ("神气", "shénqì", "thần khí", "tính từ", "oai vệ, có thần; vênh váo", "他穿上军装，显得特别神气。", "Mặc quân phục vào, anh ấy trông đặc biệt oai vệ.",
     "Tính từ, nghĩa là oai phong, có thần thái. Đôi khi mang nghĩa xấu là vênh váo, ra vẻ ta đây. Cẩn thận: thần khí trong tiếng Việt thường là danh từ chỉ khí chất, còn 神气 ở đây là tính từ tả dáng vẻ."),
    ("翘", "qiào", "kiều", "động từ", "vểnh lên, nhếch lên", "小狗翘着尾巴跑过来。", "Chú chó con vểnh đuôi chạy tới.",
     "Động từ, nghĩa là vểnh lên, nhếch lên, như vểnh đuôi, nhếch mép. Chú ý trong nghĩa này đọc thanh bốn: qiào."),
    ("神态", "shéntài", "thần thái", "danh từ", "thần thái, dáng vẻ", "画上的老虎神态逼真。", "Con hổ trong tranh có thần thái sống động như thật.",
     "Danh từ, nghĩa là thần thái, dáng vẻ và nét mặt. 神态逼真 là thần thái sống động như thật."),
    ("盛开", "shèngkāi", "thịnh khai", "động từ", "nở rộ", "春天到了，桃花盛开。", "Mùa xuân đến, hoa đào nở rộ.",
     "Động từ, nghĩa là nở rộ, hoa nở rực rỡ."),
    ("散发", "sànfā", "tán phát", "động từ", "tỏa ra, toát ra", "花园里散发着阵阵花香。", "Khu vườn tỏa ra từng đợt hương hoa.",
     "Động từ, nghĩa là tỏa ra, toát ra, như tỏa hương, toát lên vẻ vui tươi. Ngoài ra còn có nghĩa phân phát, ví dụ 散发传单, phát tờ rơi."),
    ("耸", "sǒng", "tủng", "động từ", "nhún (vai)", "他耸耸肩，什么也没说。", "Anh ấy nhún nhún vai, không nói gì cả.",
     "Động từ, nghĩa là nhún vai, thường gặp trong cụm 耸肩. Nghĩa gốc là cao vút, như 高耸入云, cao chọc trời."),
    ("州", "zhōu", "châu", "danh từ", "châu (đơn vị hành chính thời xưa)", "古代中国分为九州。", "Trung Quốc thời cổ chia thành chín châu.",
     "Danh từ, chỉ châu, đơn vị hành chính thời xưa. Nhiều địa danh còn giữ chữ này như 杭州，广州. Trong bài có 魏州, nay thuộc tỉnh Hà Bắc."),
    ("外行", "wàiháng", "ngoại hàng", "danh từ", "người ngoài nghề, người không thạo", "在电脑方面，我完全是个外行。", "Về máy tính, tôi hoàn toàn là người ngoài nghề.",
     "Danh từ, nghĩa là người ngoài nghề, người không thạo. Trái nghĩa là 内行, người trong nghề. Chú ý đọc là háng, giống chữ hàng trong ngân hàng; và đừng nhầm với hàng ngoại của tiếng Việt nhé."),
    ("推销", "tuīxiāo", "thôi tiêu", "động từ", "chào hàng, tiếp thị", "他在商场推销新产品。", "Anh ấy chào bán sản phẩm mới ở trung tâm thương mại.",
     "Động từ, nghĩa là chào hàng, tìm cách bán hàng. 推销员 là nhân viên tiếp thị, còn 推销术 trong bài là mánh chào hàng."),
    ("吞吞吐吐", "tūntūntǔtǔ", "thôn thôn thổ thổ", "thành ngữ", "ấp a ấp úng", "他说话吞吞吐吐的，好像有什么心事。", "Anh ấy nói năng ấp úng, hình như có tâm sự gì.",
     "Nghĩa đen là nuốt vào nhả ra; nghĩa bóng là nói năng ngập ngừng, ấp úng, muốn nói lại thôi."),
    ("残次品", "cáncì pǐn", "tàn thứ phẩm", "danh từ", "hàng lỗi, hàng hỏng", "这批货里有不少残次品。", "Lô hàng này có không ít hàng lỗi.",
     "Danh từ, nghĩa là hàng bị hư hỏng hoặc có khuyết tật. 残 là tàn, hỏng; 次 là kém, loại hai."),
    ("次品", "cìpǐn", "thứ phẩm", "danh từ", "hàng kém chất lượng, hàng loại hai", "次品不能卖给顾客。", "Hàng kém chất lượng không được bán cho khách.",
     "Danh từ, nghĩa là hàng không đạt tiêu chuẩn. Tiếng Việt cũng nói hàng thứ phẩm. Trái nghĩa là 正品, hàng chính phẩm."),
    ("现成", "xiànchéng", "hiện thành", "tính từ", "có sẵn, làm sẵn", "冰箱里有现成的饭菜。", "Trong tủ lạnh có sẵn cơm canh.",
     "Tính từ, nghĩa là có sẵn, làm sẵn, không phải chuẩn bị nữa. Trong bài có cụm 现成的理由, những lý do có sẵn."),
    ("谢绝", "xièjué", "tạ tuyệt", "động từ", "khước từ (một cách lịch sự)", "本店商品谢绝还价。", "Hàng hóa của cửa hàng xin miễn mặc cả.",
     "Động từ, nghĩa là từ chối một cách lịch sự, khéo léo. Hay thấy trên biển báo, ví dụ 谢绝参观, xin miễn tham quan."),
    ("故乡", "gùxiāng", "cố hương", "danh từ", "quê hương, quê nhà", "他离开故乡已经二十年了。", "Anh ấy rời quê hương đã hai mươi năm rồi.",
     "Danh từ, nghĩa là quê hương. Trong bài, 年画的故乡 là quê hương của tranh Tết."),
    ("扎实", "zhāshi", "trát thực", "tính từ", "vững chắc, chắc chắn", "他的汉语基础很扎实。", "Nền tảng tiếng Trung của anh ấy rất vững chắc.",
     "Tính từ, nghĩa là vững chắc, chắc chắn, thường nói về kiến thức, kỹ năng hay cách làm việc. Trong bài: 基本功扎实, kỹ năng cơ bản vững vàng."),
    ("塑造", "sùzào", "tố tạo", "động từ", "khắc họa, xây dựng (hình tượng)", "这部小说塑造了一个英雄形象。", "Cuốn tiểu thuyết này đã xây dựng một hình tượng anh hùng.",
     "Động từ. Nghĩa gốc là nặn tượng; nghĩa thường gặp là khắc họa, xây dựng hình tượng nhân vật trong văn học nghệ thuật."),
    ("手法", "shǒufǎ", "thủ pháp", "danh từ", "thủ pháp, kỹ xảo", "这幅画的表现手法很新颖。", "Thủ pháp thể hiện của bức tranh này rất mới lạ.",
     "Danh từ, nghĩa là thủ pháp, cách làm, kỹ xảo trong nghệ thuật. Trong bài có 雕版手法, thủ pháp khắc bản."),
    ("派别", "pàibié", "phái biệt", "danh từ", "trường phái, phe phái", "书法有很多不同的派别。", "Thư pháp có rất nhiều trường phái khác nhau.",
     "Danh từ, nghĩa là trường phái, phe phái."),
    ("借鉴", "jièjiàn", "tá giám", "động từ", "tham khảo, học hỏi", "我们可以借鉴别人的经验。", "Chúng ta có thể học hỏi kinh nghiệm của người khác.",
     "Động từ. Chữ 鉴 là tấm gương soi; 借鉴 là mượn gương người khác để soi mình, tức là tham khảo, học hỏi."),
    ("再接再厉", "zàijiē-zàilì", "tái tiếp tái lệ", "thành ngữ", "tiếp tục cố gắng, nỗ lực hơn nữa", "希望你再接再厉，取得更好的成绩！", "Mong em tiếp tục cố gắng, đạt thành tích tốt hơn nữa!",
     "Thành ngữ, nghĩa là tiếp tục nỗ lực, cố gắng hơn nữa, thường dùng để động viên sau khi đã đạt được thành tích."),
    ("心得", "xīndé", "tâm đắc", "danh từ", "điều thu hoạch, kinh nghiệm rút ra", "老师让我们写一篇读书心得。", "Thầy bảo chúng tôi viết một bài cảm nhận sau khi đọc sách.",
     "Danh từ, nghĩa là những điều hiểu ra, thu hoạch được qua học tập, làm việc. Đây là từ dễ nhầm: tâm đắc trong tiếng Việt là rất hài lòng, thấy đúng ý mình; còn 心得 là danh từ, chỉ kinh nghiệm, bài học rút ra."),
    ("缺席", "quē xí", "khuyết tịch", "động từ", "vắng mặt", "他今天因病缺席了会议。", "Hôm nay anh ấy vắng mặt ở cuộc họp vì ốm.",
     "Động từ, nghĩa là vắng mặt trong cuộc họp, buổi học. Tiếng Việt cũng nói xử khuyết tịch, tức là xử vắng mặt."),
    ("干劲", "gànjìn", "cán kình", "danh từ", "nhiệt huyết, sức hăng hái", "年轻人干劲十足。", "Người trẻ tràn đầy nhiệt huyết.",
     "Danh từ, nghĩa là sức hăng hái, nhiệt tình khi làm việc. 干劲十足 là hăng hái tràn đầy. Chú ý đọc gàn, thanh bốn."),
    ("占据", "zhànjù", "chiếm cứ", "động từ", "chiếm, chiếm giữ", "工作占据了他大部分时间。", "Công việc chiếm phần lớn thời gian của anh ấy.",
     "Động từ, nghĩa là chiếm, chiếm giữ một vị trí, không gian hay thời gian."),
    ("确立", "quèlì", "xác lập", "động từ", "xác lập, xác định rõ", "他很早就确立了自己的人生目标。", "Anh ấy đã xác định mục tiêu cuộc đời mình từ rất sớm.",
     "Động từ, nghĩa là xác lập, xác định một cách vững chắc, thường đi với mục tiêu, địa vị, chế độ."),
    ("信念", "xìnniàn", "tín niệm", "danh từ", "niềm tin (vững chắc)", "他有着坚定的信念。", "Anh ấy có một niềm tin vững chắc.",
     "Danh từ, nghĩa là niềm tin vững chắc vào điều mình theo đuổi. 信仰 thiên về tôn giáo, lý tưởng; còn 信念 gần gũi hơn, là niềm tin của mỗi người."),
    ("任重道远", "rènzhòng-dàoyuǎn", "nhậm trọng đạo viễn", "thành ngữ", "gánh nặng đường xa", "保护传统文化任重道远。", "Bảo vệ văn hóa truyền thống là trách nhiệm nặng nề, đường còn dài.",
     "Thành ngữ, nghĩa là gánh nặng mà đường còn xa, tức trách nhiệm lớn lao, cần kiên trì lâu dài."),
    ("一帆风顺", "yìfān-fēngshùn", "nhất phàm phong thuận", "thành ngữ", "thuận buồm xuôi gió", "人生不可能总是一帆风顺。", "Đời người không thể lúc nào cũng thuận buồm xuôi gió.",
     "Thành ngữ, nghĩa giống hệt câu thuận buồm xuôi gió của tiếng Việt. Chú ý pinyin viết là yìfān, thanh bốn, do biến điệu."),
]
# số thứ tự theo sách: 次品 là từ phụ đi kèm số 34
NUM = []
_n = 0
for _w in V:
    if _w[0] == "次品":
        NUM.append("34b")
    else:
        _n += 1
        NUM.append(str(_n))
assert _n == 51

add("bullets", chapter="Từ mới (51 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 35 có 51 từ mới (cộng từ phụ 次品), chia thành 18 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 翘 (qiào) · 外行 (háng) · 扎实 (zhā) · 干劲 (gàn)",
           "Cẩn thận từ dễ nhầm: 文献 ≠ văn hiến · 心得 ≠ tâm đắc"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có năm mươi mốt từ, cộng thêm một từ phụ là 次品. Thầy chia thành mười tám nhóm nhỏ, mỗi nhóm hai hoặc ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số từ có âm đọc đặc biệt, thầy sẽ nhắc khi gặp."),
         F(4, "Ngoài ra có vài từ Hán Việt nghe quen nhưng nghĩa khác tiếng Việt, ví dụ 文献 không phải là văn hiến, 心得 không phải là tâm đắc. Thầy sẽ giải thích kỹ. Chúng ta bắt đầu nhé.")])

sizes = [3] * 16 + [2, 2]
assert sum(sizes) == len(V)
g = 0
for gs in sizes:
    group = V[g:g + gs]
    words, say = [], []
    for i, (zh, py, hv, loai, vi, ex, exvi, expl) in enumerate(group):
        n = NUM[g + i]
        words.append({"zh": zh, "py": py, "hv": hv.upper(), "loai": f"{n}. {loai}", "vi": vi, "ex": ex, "exvi": exvi})
        if n == "34b":
            say.append(F(i, f"Đi kèm từ số 34 là từ phụ {zh}。 {zh}。 Hán Việt là {hv}.", zr=120))
        else:
            say.append(F(i, f"Từ số {n}: {zh}。 {zh}。 Hán Việt là {hv}.", zr=120))
        say.append(F(i, f"{expl} Ví dụ: {ex}{'' if ex[-1] in '。…？！，' else '，'} {exvi[0].upper() + exvi[1:]}{'' if exvi.endswith(('.', '!', '?')) else '.'}", zr=130))
    add("vocab", section="Từ mới 生词", title=f"Từ mới ({g + 1}–{g + len(group)} / {len(V)})",
        words=words, say=say)
    g += gs

# ======================= BÀI KHÓA =======================
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung nếu khác: số viết bằng chữ Hán])
P = [
    # --- 年画的起源 ---
    ("年画是中国画的一种，始于古代的门神画。",
     "Tranh Tết là một loại hình của hội họa Trung Quốc, bắt nguồn từ tranh môn thần thời cổ.",
     ["始于 nghĩa là bắt đầu từ, cách nói văn viết. 门神画 là tranh môn thần, tức tranh vẽ vị thần giữ cửa, dán trên hai cánh cổng.",
      "Câu mở bài rất ngắn, nêu ngay định nghĩa và nguồn gốc, đúng phong cách của văn thuyết minh."]),
    ("有文献记载：传说很久以前，有一对兄弟，专门监督百鬼，发现凶恶的鬼就捆绑起来，无须揭露恶行，直接去喂老虎。",
     "Có tài liệu ghi chép rằng: tương truyền từ rất lâu về trước, có hai anh em chuyên trông coi trăm loài quỷ; hễ phát hiện con quỷ nào hung ác thì trói lại, không cần vạch tội, đem thẳng cho hổ ăn.",
     ["记载 là ghi chép. 传说 là tương truyền. 监督 là giám sát, trông coi. 捆绑 là trói lại.",
      "无须 nghĩa là không cần, là cách nói văn viết của 不必. Hai anh em này về sau được coi là hai vị môn thần đầu tiên."]),
    ("于是有人在门上画上他们兄弟二人的像，用以防鬼，这就是最早的门神画。",
     "Thế là có người vẽ hình hai anh em họ lên cửa để phòng quỷ; đó chính là những bức tranh môn thần sớm nhất.",
     ["用以 nghĩa là dùng để, cách nói văn viết. 防鬼 là phòng quỷ, trừ tà.",
      "Sau này tranh môn thần thường vẽ hai vị tướng mặc giáp oai phong, giống bức tranh đầu tiên trong phần khởi động."]),
    ("随着唐宋两朝经济的发展，文化的昌盛以及民间绘画水平的提高，门神画的内容得以拓展，反映世俗生活题材的作品进入了这一领域。",
     "Cùng với sự phát triển kinh tế, sự hưng thịnh văn hóa và trình độ hội họa dân gian được nâng cao dưới hai triều Đường, Tống, nội dung của tranh môn thần được mở rộng; những tác phẩm phản ánh đề tài đời sống thế tục đã bước vào lĩnh vực này.",
     ["Sau 随着 là ba cụm danh từ song song: 经济的发展，文化的昌盛，以及民间绘画水平的提高. 以及 là và, cùng với, dùng trong văn viết.",
      "得以 là nhờ đó mà được, có thể. 世俗生活 là đời sống thế tục, cuộc sống thường ngày. Theo chú thích của sách: nhà Đường từ năm sáu trăm mười tám đến chín trăm linh bảy, nhà Tống từ năm chín trăm sáu mươi đến một nghìn hai trăm bảy mươi chín."]),
    ("之后，有清朝学者在论述这类画作时正式使用了“年画”一词，自此，以驱逐祸凶、祝福新年吉祥喜庆为内容的画儿就叫年画了。",
     "Về sau, có học giả đời Thanh khi bàn về loại tranh này đã chính thức dùng từ niên họa, tức tranh Tết; từ đó, những bức tranh lấy việc xua đuổi tai ương, chúc năm mới may mắn vui tươi làm nội dung được gọi là tranh Tết.",
     ["论述 là bàn luận, trình bày. 自此 là từ đó trở đi. 祸凶 là tai họa, điều dữ.",
      "以……为内容 nghĩa là lấy… làm nội dung. Nhà Thanh theo chú thích của sách là từ năm một nghìn sáu trăm mười sáu đến một nghìn chín trăm mười một."]),
    # --- 木版年画 ---
    ("造纸技术的发明是人类文化发展史上一个重要的里程碑。",
     "Việc phát minh ra kỹ thuật làm giấy là một cột mốc quan trọng trong lịch sử phát triển văn hóa của nhân loại.",
     ["造纸技术 là kỹ thuật làm giấy, một trong bốn phát minh lớn của Trung Quốc cổ đại. 里程碑 là cột mốc, từ vừa học.",
      "Phần hai của bài khóa đi theo trình tự thời gian: có giấy, rồi có mực, có con dấu, rồi đến in khắc bản."]),
    ("有了纸，书写就需要墨水儿，于是有人发明了墨；字画、书信上需要盖章，于是印章开始流行；碑刻、拓印技术被广泛运用，于是有人联想到：这些技术结合起来，不就能印出书来吗！",
     "Có giấy rồi thì việc viết lách cần đến mực, thế là có người phát minh ra mực; tranh chữ, thư từ cần đóng dấu, thế là con dấu bắt đầu thịnh hành; kỹ thuật khắc bia, in rập được sử dụng rộng rãi, thế là có người liên tưởng: kết hợp những kỹ thuật này lại, chẳng phải là in được sách sao!",
     ["Ba vế câu đều theo cùng một mô hình: có nhu cầu, rồi 于是, dẫn đến một phát minh. Từ 于是 và 需要 lặp lại nhiều lần, đây chính là thủ pháp lặp từ khóa mà ta sẽ học ở phần tu từ.",
      "不就能……吗 là câu hỏi tu từ: chẳng phải là có thể… sao! Tức là chắc chắn có thể."]),
    ("人们尝试把印章扩大成一张纸那么大，叫作“版”，然后把书的内容刻在版上，在版上涂抹上墨，把纸铺到上面，用刷子均匀地刷印，最后将纸揭起，印品就出来了，这就是最早的雕版印刷。",
     "Người ta thử phóng to con dấu ra bằng cả một tờ giấy, gọi là bản; sau đó khắc nội dung sách lên bản, quét mực lên bản, trải giấy lên trên, dùng bàn chải xoa in đều tay, cuối cùng bóc giấy lên là có bản in; đó chính là kỹ thuật in khắc bản sớm nhất.",
     ["Đoạn này tả quy trình in theo thứ tự, có các từ nối 然后 và 最后. 叫作 là gọi là. 铺到上面 là trải lên trên. 刷子 là bàn chải. 揭起 là bóc lên.",
      "雕版印刷 là in khắc bản. Tranh Đông Hồ của Việt Nam cũng làm theo đúng cách này: khắc ván gỗ, quét màu lên ván, đặt giấy lên rồi xoa đều."]),
    ("虽然雕版印刷中雕刻版面需要大量的人工和材料，但雕版完成后一经开印，就显示出空前的高效率和印刷量大的优越性。",
     "Tuy trong in khắc bản, việc khắc mặt bản cần rất nhiều công sức và vật liệu, nhưng một khi bản khắc đã xong và bắt đầu in, nó liền cho thấy ưu thế hiệu suất cao chưa từng có và số lượng in lớn.",
     ["虽然……但…… là tuy… nhưng…. 一经……就…… nghĩa là một khi đã… thì liền…, cách nói văn viết.",
      "空前 là chưa từng có. 优越性 là tính ưu việt, ưu thế."]),
    ("单色印品终究不能满足人们的审美需求，之后就有了彩色套印技术。人们把这种技术运用到年画制作上，木版彩色套印年画就此诞生。",
     "Bản in một màu rốt cuộc không thể thỏa mãn nhu cầu thẩm mỹ của con người, sau đó kỹ thuật in chồng màu ra đời. Người ta áp dụng kỹ thuật này vào việc làm tranh Tết, và tranh Tết in chồng màu khắc gỗ từ đó ra đời.",
     ["单色 là một màu. 终究 là rốt cuộc, suy cho cùng, điểm ngữ pháp thứ nhất. 审美需求 là nhu cầu thẩm mỹ.",
      "套印 là in chồng màu: mỗi màu một tấm ván, in lần lượt chồng lên nhau cho khớp. 就此 là từ đó, 诞生 là ra đời."]),
    ("宋明两代，木版年画从问世走向成熟，之后走进了百姓生活，以至过年贴年画成为了一种风尚，仿佛没有年画，没有烟花爆竹，没有春联就不叫过年，而寄托着百姓美好愿望的年画，也为春节增添了浓浓的年味。",
     "Qua hai đời Tống, Minh, tranh Tết khắc gỗ đi từ chỗ ra đời đến chỗ hoàn thiện, rồi đi vào đời sống người dân, đến mức dán tranh Tết khi ăn Tết trở thành một nếp chuộng; dường như không có tranh Tết, không có pháo hoa pháo nổ, không có câu đối Tết thì chẳng gọi là ăn Tết; và những bức tranh gửi gắm ước mong tốt đẹp của người dân cũng làm tăng thêm hương vị Tết đậm đà.",
     ["问世 là ra đời. 以至 là đến mức. 风尚 là nếp chuộng, phong trào được ưa thích. Nhà Minh theo chú thích là từ năm một nghìn ba trăm sáu mươi tám đến một nghìn sáu trăm bốn mươi bốn.",
      "仿佛没有……就不叫过年 : dường như không có… thì không gọi là ăn Tết. Người Việt cũng có câu: thịt mỡ, dưa hành, câu đối đỏ, cây nêu, tràng pháo, bánh chưng xanh."]),
    ("当时的另一盛况是，家族式的年画印制场所遍及全国各地。这期间，年画的内容也从威武的门神，扩展到期盼丰收、恭喜发财、连年有余的吉庆画，再到历史故事、戏曲人物、民间笑话、寓言和神话，内容无所不包。",
     "Một cảnh tượng thịnh vượng khác thời ấy là các xưởng in tranh Tết kiểu gia đình có mặt khắp cả nước. Trong thời kỳ này, nội dung tranh Tết cũng mở rộng từ những vị môn thần oai vệ đến tranh cát tường mong được mùa, chúc phát tài, năm nào cũng dư dả, rồi đến chuyện lịch sử, nhân vật hí khúc, truyện cười dân gian, ngụ ngôn và thần thoại; nội dung bao quát mọi thứ.",
     ["盛况 là cảnh tượng thịnh vượng. 家族式 là kiểu gia đình, cha truyền con nối. 遍及 là có mặt khắp, lan khắp.",
      "从……扩展到……，再到…… nghĩa là từ… mở rộng đến…, rồi đến…. 无所不包 là không gì không bao gồm."]),
    ("年画成了文化交流、道德教育、信仰传承的载体与工具，是老百姓喜闻乐见的文化艺术形式。",
     "Tranh Tết trở thành phương tiện và công cụ để giao lưu văn hóa, giáo dục đạo đức, truyền thừa tín ngưỡng, là loại hình văn hóa nghệ thuật được người dân ưa chuộng.",
     ["载体 là vật mang, phương tiện chuyên chở. 传承 là truyền thừa, lưu truyền qua các thế hệ.",
      "Câu này tổng kết vai trò của tranh Tết, khép lại phần hai của bài khóa."]),
    # --- 年画传人张光宁 ---
    ("第一次见到张光宁的木版年画，是在春节庙会上。在众多摊位中，他的两只木版彩色套印技术做成的布老虎神气极了。",
     "Lần đầu tiên tôi thấy tranh Tết khắc gỗ của Trương Quang Ninh là ở hội chùa dịp Tết. Giữa rất nhiều sạp hàng, hai con hổ vải làm bằng kỹ thuật in chồng màu khắc gỗ của anh trông oai vệ vô cùng.",
     ["Tiêu đề phần ba là 年画传人张光宁, Trương Quang Ninh, người kế thừa nghề tranh Tết. 传人 là người kế thừa, truyền nhân.",
      "庙会 là hội chùa, hội đình. 摊位 là sạp hàng. 布老虎 là con hổ vải, một món đồ chơi dân gian. 神气极了 là oai vệ hết sức."]),
    ("那虎翘着尾巴，神态逼真，身上装饰着彩绘花纹和盛开的花朵，全身散发着喜气。",
     "Con hổ ấy vểnh đuôi, thần thái sống động như thật, trên mình trang trí hoa văn vẽ màu và những bông hoa nở rộ, toàn thân toát lên vẻ vui tươi.",
     ["逼真 là giống như thật. 彩绘 là vẽ màu. 花纹 là hoa văn. 喜气 là không khí vui mừng, hân hoan.",
      "Câu văn tả con hổ theo trình tự rất rõ: cái đuôi, thần thái, thân mình, rồi toàn thân. Các động từ đều có trợ từ zhe đi sau, chỉ trạng thái đang tiếp diễn."]),
    ("我问多少钱，他耸耸肩，对我说：“这是魏州虎。”言外之意是在告诉我这个外行，这虎可是系出名门。",
     "Tôi hỏi giá bao nhiêu, anh nhún vai, nói với tôi: Đây là hổ Ngụy Châu. Ý ngoài lời là muốn nói với kẻ ngoài nghề như tôi rằng con hổ này có gốc gác danh tiếng đấy.",
     ["言外之意 là ý ngoài lời, hàm ý. Cụm 系出名门 đọc là xì chū míngmén, nghĩa là xuất thân từ dòng dõi danh tiếng. 可是 ở đây là phó từ nhấn mạnh, nghĩa là quả thật là.",
      "Theo chú thích, 魏州 nay thuộc huyện Ngụy, thành phố Hàm Đan, tỉnh Hà Bắc, nơi có nghề nhuộm dệt vải hoa truyền thống đến nay vẫn rất độc đáo."]),
    ("我心想：“魏州是哪儿？我不知道别人也未必知道，这算什么推销术？”这是他给我留下的第一印象。",
     "Tôi nghĩ bụng: Ngụy Châu là ở đâu? Tôi không biết thì người khác cũng chưa chắc biết, thế này mà gọi là cách chào hàng à? Đó là ấn tượng đầu tiên anh để lại cho tôi.",
     ["未必 là chưa chắc. 这算什么…… là thế này mà gọi là… sao, mang ý chê bai.",
      "留下……印象 là để lại ấn tượng. Tác giả kể theo trình tự: ấn tượng thứ nhất, ấn tượng thứ hai, rồi quen lâu mới hiểu."]),
    ("“这个卖年画的不像个商人”，这是他给我留下的第二印象。当你和他讨价还价的时候，他立刻就变得不好意思起来，说话吞吞吐吐。",
     "Người bán tranh Tết này chẳng giống dân buôn, đó là ấn tượng thứ hai anh để lại cho tôi. Khi bạn mặc cả với anh, anh lập tức trở nên ngượng ngùng, nói năng ấp úng.",
     ["讨价还价 là mặc cả, trả giá, đọc là tǎojià huánjià.",
      "不好意思起来 : 起来 đứng sau tính từ, chỉ trạng thái bắt đầu xuất hiện, tức là bắt đầu ngượng ngùng."]),
    ("什么“这是纯手工的”“残次品不可避免”这些现成的“谢绝”还价的理由他一条也说不出来，相反却唠唠叨叨地总想和你讨论木版年画中深厚的文化底蕴。",
     "Những lý do có sẵn để từ chối mặc cả như: đây là hàng thủ công, hàng lỗi là không tránh khỏi…, anh không nói ra được lấy một câu; ngược lại, anh cứ luyên thuyên, lúc nào cũng muốn bàn với bạn về chiều sâu văn hóa trong tranh Tết khắc gỗ.",
     ["什么 đứng đầu một loạt liệt kê mang nghĩa: nào là…, những thứ như…. 一条也说不出来 là một lý do cũng không nói ra được.",
      "唠唠叨叨 là nói lải nhải, nói mãi không thôi. 底蕴 là chiều sâu, nội hàm văn hóa."]),
    ("相识久了才知道，他在年画的故乡出生、长大，从小就画年画，基本功扎实，后来又对年画的构图创作、人物塑造、雕版手法、颜料加工等进行了广泛的研究。",
     "Quen nhau lâu rồi tôi mới biết, anh sinh ra và lớn lên ở quê hương của tranh Tết, từ nhỏ đã vẽ tranh Tết, kỹ năng cơ bản rất vững; sau này anh lại nghiên cứu rộng rãi về bố cục sáng tác, khắc họa nhân vật, thủ pháp khắc bản, chế biến màu vẽ của tranh Tết.",
     ["相识 là quen biết. 构图 là bố cục tranh. 颜料 là màu vẽ, thuốc màu. 加工 là chế biến.",
      "对……进行了研究 là tiến hành nghiên cứu về…, một cấu trúc văn viết rất hay gặp."]),
    ("当他的作品逐步被市场认可后，他又不满足了，中国年画虽不分派别，但不同地区的年画各有所长，都值得学习借鉴。",
     "Khi tác phẩm của anh dần dần được thị trường công nhận, anh lại không thỏa mãn: tranh Tết Trung Quốc tuy không chia trường phái, nhưng tranh Tết mỗi vùng đều có sở trường riêng, đều đáng để học hỏi.",
     ["逐步 là dần dần. 认可 là công nhận. 虽……但…… là tuy… nhưng…, 虽 là cách nói gọn của 虽然.",
      "各有所长 là mỗi nơi có sở trường riêng. Trung Quốc có bốn trung tâm tranh Tết nổi tiếng: 杨柳青，桃花坞，杨家埠 và 朱仙镇."]),
    ("于是，他再接再厉，数年间走遍了全国各大年画产地，与同行进行广泛的交流。不仅如此，参加民俗文化巡展，走进大学和师生就相关主题进行研讨，交流艺术心得，他从不缺席。",
     "Thế là anh tiếp tục nỗ lực, trong vài năm đã đi khắp các vùng sản xuất tranh Tết lớn trong cả nước, giao lưu rộng rãi với những người cùng nghề. Không chỉ vậy, tham gia triển lãm lưu động về văn hóa dân gian, đến các trường đại học thảo luận với thầy trò về những chủ đề liên quan, trao đổi kinh nghiệm nghệ thuật, anh chưa bao giờ vắng mặt.",
     ["数年间 là trong vài năm. 同行 ở đây đọc là tóngháng, nghĩa là người cùng nghề. 不仅如此 là không chỉ như vậy.",
      "巡展 là triển lãm lưu động. 就……进行研讨 là thảo luận về…. Chú ý câu sau rất dài, liệt kê ba hoạt động rồi mới đến chủ ngữ 他 và vị ngữ 从不缺席."]),
    ("张光宁一年到头真够忙的，可他总是干劲十足。他曾真诚地说：“年画占据了我生命的全部，我喜欢它，热爱它，靠它生活，也在努力探索它、发展它。”",
     "Trương Quang Ninh quanh năm suốt tháng thật là bận rộn, nhưng anh lúc nào cũng hăng hái tràn đầy. Anh từng chân thành nói: Tranh Tết chiếm trọn cuộc đời tôi, tôi thích nó, yêu nó, sống nhờ nó, và cũng đang nỗ lực tìm tòi nó, phát triển nó.",
     ["一年到头 là quanh năm suốt tháng. 真够……的 là thật là quá…. 干劲十足 là hăng hái tràn đầy.",
      "Trong lời nói của anh, chữ 它 lặp lại năm lần. Đây cũng là cách lặp từ khóa để nhấn mạnh tình yêu với tranh Tết."]),
    ("是啊，愈是经营年画久了，他对年画就愈是热爱。他已确立了自己的目标——传播他喜爱的这一民俗文化。",
     "Đúng vậy, càng gắn bó với nghề tranh Tết lâu, anh lại càng yêu tranh Tết. Anh đã xác định mục tiêu của mình: truyền bá nét văn hóa dân gian mà anh yêu thích này.",
     ["愈是……就愈是…… giống 越……越……, nghĩa là càng… càng…, đây là điểm ngữ pháp thứ hai.",
      "经营 ở đây là gắn bó, làm nghề. Dấu gạch ngang dài dùng để giải thích mục tiêu là gì."]),
    ("他的信念就是拓展年画的内容，使其雅俗共赏，为更多民众所喜爱，虽然任重道远，也不会一帆风顺，但他一定会坚持下去。",
     "Niềm tin của anh là mở rộng nội dung tranh Tết, làm cho nó được cả người sành lẫn người bình dân cùng thưởng thức, được nhiều người yêu thích hơn; tuy gánh nặng đường xa, cũng sẽ không thuận buồm xuôi gió, nhưng anh nhất định sẽ kiên trì đến cùng.",
     ["使其 là làm cho nó. 雅俗共赏 là người sành và người bình dân đều thưởng thức được.",
      "为……所…… là câu bị động văn viết: 为更多民众所喜爱, được nhiều người yêu thích hơn. Bài khóa kết thúc bằng hai thành ngữ vừa học: 任重道远 và 一帆风顺."]),
]

SUB = {1: "年画的起源", 6: "木版年画", 14: "年画传人张光宁"}

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 走近木版年画",
    items=["Ba phần: 年画的起源 · 木版年画 · 年画传人张光宁",
           "Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 走近木版年画, dài một nghìn bốn trăm bốn mươi bảy chữ.",
         F(0, "Bài khóa có ba phần nhỏ: 年画的起源, nguồn gốc tranh Tết; 木版年画, tranh Tết khắc gỗ; và 年画传人张光宁, nghệ nhân kế thừa tranh Tết Trương Quang Ninh."),
         F(1, "Thầy chia bài thành từng đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(2, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(3, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

cur = ""
for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    cur = SUB.get(i, cur)
    zsize = 54 if len(zh) <= 100 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)} · {cur}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi, cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Tóm tắt nội dung", section="Bài khóa 课文", title="Bố cục bài khóa (1): lịch sử tranh Tết", size=36,
    items=["## 1. 年画的起源 – Nguồn gốc tranh Tết",
           "门神画 · 兄弟二人 · 唐宋：门神画内容拓展 · 清朝：使用“年画”一词",
           "## 2. 木版年画 – Tranh Tết khắc gỗ",
           "雕版的发明：墨 → 印章 → 碑刻、拓印 → 扩大印章 → 在版上刷印",
           "彩色套印：单色印品不能满足审美需求 → 木版彩色套印年画诞生",
           "年画走进百姓生活：过年贴年画 · 年画印制场所 · 年画内容 · 年画成了……的载体与工具"],
    say=["Chúng ta cùng nhìn lại bố cục bài khóa, theo gợi ý của bài tập năm trong sách.",
         F(0, "Phần một: nguồn gốc tranh Tết."),
         F(1, "Bắt đầu từ tranh môn thần, gắn với truyền thuyết về hai anh em trông coi trăm quỷ; đến đời Đường, Tống, nội dung tranh được mở rộng; đến đời Thanh, từ 年画 chính thức được dùng."),
         F(2, "Phần hai: tranh Tết khắc gỗ."),
         F(3, "Kỹ thuật khắc bản ra đời qua một chuỗi phát minh: mực, con dấu, khắc bia và in rập, rồi phóng to con dấu thành bản khắc để in."),
         F(4, "Tiếp theo là kỹ thuật in chồng màu, vì bản in một màu không thỏa mãn nhu cầu thẩm mỹ, và tranh Tết in chồng màu khắc gỗ ra đời."),
         F(5, "Rồi tranh Tết đi vào đời sống người dân: Tết nào cũng dán tranh, xưởng in khắp nơi, nội dung phong phú, và tranh Tết trở thành phương tiện giao lưu văn hóa, giáo dục đạo đức.")])

add("bullets", section="Bài khóa 课文", title="Bố cục bài khóa (2): nghệ nhân 张光宁", size=38,
    items=["## 3. 年画传人张光宁 – Nghệ nhân Trương Quang Ninh",
           "初次认识：春节庙会 · 布老虎 · 推销",
           "第二印象：不像商人 · 讨论年画的文化底蕴",
           "相识久了：出生、长大 · 从小…… · 后来…… · 再接再厉…… · 不仅如此……",
           "目标和信念：传播民俗文化 · 拓展年画内容",
           "→ Cách kể: ấn tượng thứ nhất → ấn tượng thứ hai → quen lâu mới hiểu"],
    say=[F(0, "Phần ba của bài khóa là chân dung nghệ nhân Trương Quang Ninh."),
         F(1, "Lần đầu gặp gỡ: ở hội chùa dịp Tết, tác giả thấy con hổ vải của anh, và câu chào hàng kỳ lạ: 这是魏州虎。"),
         F(2, "Ấn tượng thứ hai: anh không giống dân buôn, không biết mặc cả, chỉ thích bàn về chiều sâu văn hóa của tranh Tết."),
         F(3, "Quen lâu rồi mới biết: anh sinh ra và lớn lên ở quê hương tranh Tết, từ nhỏ đã vẽ, sau này nghiên cứu sâu, đi khắp nơi học hỏi, tham gia mọi hoạt động giao lưu."),
         F(4, "Cuối cùng là mục tiêu và niềm tin của anh: truyền bá văn hóa dân gian, mở rộng nội dung tranh Tết."),
         F(5, "Cách kể chuyện từ ấn tượng ban đầu đến hiểu biết sâu sắc này rất đáng học, các bạn có thể dùng khi viết về một nhân vật.")])

add("bullets", section="Bài khóa 课文", title="Liên hệ: tranh Tết Trung Quốc và tranh Đông Hồ", size=36,
    items=["## Giống nhau",
           "In khắc gỗ, mỗi màu một ván, in chồng màu lần lượt (套印)",
           "Bán và dán dịp Tết, gửi gắm ước mong may mắn, sung túc, được mùa",
           "Đề tài dân gian: chúc phúc, sinh hoạt, truyện cổ, ngụ ngôn",
           "## Khác nhau",
           "Đông Hồ (Bắc Ninh): giấy dó quét điệp, màu tự nhiên · tranh Lợn đàn, Đám cưới chuột, Vinh hoa – Phú quý",
           "Trung Quốc: nhiều trung tâm – 杨柳青 (Thiên Tân), 桃花坞 (Tô Châu), 杨家埠 (Sơn Đông), 朱仙镇 (Hà Nam); môn thần, cá chép, em bé ôm cá"],
    say=["Trước khi sang ngữ pháp, thầy muốn liên hệ một chút với tranh Đông Hồ của Việt Nam.",
         F(1, "Điểm giống thứ nhất: cả hai đều là tranh in khắc gỗ, mỗi màu khắc một tấm ván riêng, in lần lượt chồng lên nhau. Đây chính là kỹ thuật 套印 trong bài khóa."),
         F(2, "Thứ hai: cả hai đều được bán và dán vào dịp Tết, gửi gắm ước mong may mắn, sung túc, được mùa."),
         F(3, "Thứ ba: đề tài đều gần gũi với dân gian: lời chúc phúc, cảnh sinh hoạt, truyện cổ và ngụ ngôn."),
         F(5, "Về điểm khác: tranh Đông Hồ ở Bắc Ninh in trên giấy dó quét điệp óng ánh, dùng màu tự nhiên như than lá tre, sỏi son, hoa hòe. Những bức nổi tiếng là Lợn đàn, Đám cưới chuột, Vinh hoa và Phú quý."),
         F(6, "Còn Trung Quốc có nhiều trung tâm tranh Tết, nổi tiếng nhất là 杨柳青 ở Thiên Tân, 桃花坞 ở Tô Châu, 杨家埠 ở Sơn Đông và 朱仙镇 ở Hà Nam. Đề tài quen thuộc là môn thần, cá chép, em bé ôm cá, mang ý nghĩa 连年有余. Các bạn thấy đấy, hai dòng tranh tuy khác nhau nhưng cùng chung một tinh thần đón Tết.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 终究", section="Ngữ pháp 注释", title="1. 终究 zhōngjiū – rốt cuộc, suy cho cùng (1)", size=40,
    items=["Phó từ. Cách dùng 1: nhấn mạnh bản chất sự vật không thay đổi, sự thật không thể phủ nhận",
           "Tăng cường ngữ khí, thường dùng trong câu trần thuật mang tính đánh giá",
           "单色印品终究不能满足人们的审美需求，之后就有了彩色套印技术。",
           "猫终究是动物，动物急了咬人也是正常的。",
           "Gần nghĩa: 毕竟 · 到底 – suy cho cùng"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là phó từ 终究.",
         F(0, "终究 có hai cách dùng. Cách dùng thứ nhất: nhấn mạnh rằng bản chất, đặc điểm của sự vật không thay đổi, sự thật không thể phủ nhận. Tiếng Việt dịch là: suy cho cùng, dù sao thì cũng."),
         F(1, "Nó có tác dụng tăng cường ngữ khí, và thường dùng trong câu trần thuật mang ý nghĩa đánh giá."),
         F(2, "Ví dụ một, lấy từ bài khóa: 单色印品终究不能满足人们的审美需求，之后就有了彩色套印技术。 Bản in một màu suy cho cùng không thể thỏa mãn nhu cầu thẩm mỹ của con người, sau đó mới có kỹ thuật in chồng màu."),
         F(3, "Ví dụ hai: 猫终究是动物，动物急了咬人也是正常的。 Mèo suy cho cùng vẫn là động vật, động vật mà cuống lên thì cắn người cũng là chuyện bình thường."),
         F(4, "Theo cách dùng này, 终究 gần nghĩa với 毕竟 và 到底, đều nghĩa là suy cho cùng.")])

add("bullets", section="Ngữ pháp 注释", title="终究 – cách dùng 2: kết quả tất yếu sẽ đến", size=38,
    items=["Thường đứng trước động từ năng nguyện (会、要…): kết quả dự đoán, mong đợi nhất định sẽ xuất hiện",
           "Cấu trúc: 终究 + 会 / 要 + động từ – dù thế nào cuối cùng cũng sẽ…",
           "胜利总是在真理一边，正义的事业终究会取得胜利。",
           "……有再好的管理和技术，产品终究要靠这些普通工人去生产。",
           "Bối cảnh ví dụ 2: một doanh nghiệp không thể thiếu nhân tài quản lý, kỹ thuật, nhưng cũng không thể thiếu công nhân tuyến đầu"],
    say=[F(0, "Cách dùng thứ hai: 终究 thường đứng trước động từ năng nguyện, như 终究会，终究要, biểu thị kết quả mà ta dự đoán hoặc mong đợi nhất định sẽ xuất hiện. Dù thế nào đi nữa, cuối cùng cũng sẽ như vậy."),
         F(1, "Cấu trúc thường gặp là 终究会 hoặc 终究要, rồi cộng động từ. Tiếng Việt dịch là: rốt cuộc sẽ, cuối cùng nhất định sẽ."),
         F(2, "Ví dụ: 胜利总是在真理一边，正义的事业终究会取得胜利。 Chiến thắng luôn đứng về phía chân lý, sự nghiệp chính nghĩa rốt cuộc sẽ giành thắng lợi."),
         F(3, "Ví dụ hai: 有再好的管理和技术，产品终究要靠这些普通工人去生产。 Dù quản lý và kỹ thuật có tốt đến đâu, sản phẩm rốt cuộc vẫn phải dựa vào những công nhân bình thường này làm ra."),
         F(4, "Câu này nằm trong một đoạn nói rằng: thành công của doanh nghiệp là kết quả nỗ lực của cả tập thể, cần nhân tài quản lý, kỹ thuật, nhưng cũng không thể thiếu những công nhân tuyến đầu.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: dùng 终究 viết lại câu", reveal=True, size=36,
    items=["(1) 如果一个人一直不愿意变老，那他就永远不会幸福，因为他最后是一定会变老的。",
           "Đáp án: ……因为他终究会变老的。",
           "(2) 借住在朋友这儿当然不是长久之计，还是应该尽快租个房子。",
           "Đáp án: 借住在朋友这儿终究不是长久之计，还是应该尽快租个房子。",
           "(3) 失败毕竟不是好事，但只要从失败中吸取经验教训，坏事也可以变成好事。",
           "Đáp án: 失败终究不是好事，但只要从失败中吸取经验教训，坏事也可以变成好事。"],
    say=[F(0, "Luyện tập: dùng 终究 viết lại câu. Câu một: 如果一个人一直不愿意变老，那他就永远不会幸福，因为他最后是一定会变老的。 Nếu một người mãi không chịu già đi, thì người đó sẽ không bao giờ hạnh phúc, vì cuối cùng nhất định họ sẽ già. Các bạn hãy tạm dừng và thử viết lại nhé."),
         F(1, "Đáp án: thay 最后是一定 bằng 终究: 因为他终究会变老的。 Đây là cách dùng thứ hai, kết quả tất yếu sẽ đến."),
         F(2, "Câu hai: 借住在朋友这儿当然不是长久之计，还是应该尽快租个房子。 Ở nhờ nhà bạn đương nhiên không phải kế lâu dài, vẫn nên sớm thuê một căn nhà."),
         F(3, "Đáp án: thay 当然 bằng 终究: 借住在朋友这儿终究不是长久之计。 Ở nhờ nhà bạn suy cho cùng không phải kế lâu dài."),
         F(4, "Câu ba: 失败毕竟不是好事，但只要从失败中吸取经验教训，坏事也可以变成好事。 Thất bại dù sao cũng không phải chuyện tốt, nhưng chỉ cần rút ra bài học từ thất bại, chuyện xấu cũng có thể thành chuyện tốt."),
         F(5, "Đáp án: thay 毕竟 bằng 终究: 失败终究不是好事。 Đây là cách dùng thứ nhất, nhấn mạnh bản chất không thay đổi.")])

add("bullets", chapter="Ngữ pháp: 愈……愈……", section="Ngữ pháp 注释", title="2. 愈……愈…… yù…yù… – càng… càng…", size=38,
    items=["Giống 越……越……, dùng trong văn viết",
           "愈是经营年画久了，他对年画就愈是热爱。",
           "机遇的特点之一是转瞬即逝，市场竞争愈激烈愈是如此。",
           "一般说来，一个人受的教育愈多、愈好，占有的人类精神文化的财富也就愈多，创造、发展文化的能力也就愈强。",
           "Biến thể: 愈是……就愈是…… · 愈……就愈…… · 愈……，……也就愈……"],
    say=["Điểm ngữ pháp thứ hai là cấu trúc 愈……愈…….",
         F(0, "愈……愈…… có nghĩa giống hệt 越……越……, tức là càng… càng…, nhưng mang sắc thái văn viết, trang trọng hơn. Chữ 愈 Hán Việt là dũ, như trong từ dũ phát."),
         F(1, "Ví dụ một, lấy từ bài khóa: 愈是经营年画久了，他对年画就愈是热爱。 Càng gắn bó với nghề tranh Tết lâu, anh lại càng yêu tranh Tết."),
         F(2, "Ví dụ hai: 机遇的特点之一是转瞬即逝，市场竞争愈激烈愈是如此。 Một trong những đặc điểm của cơ hội là thoáng qua trong chớp mắt, cạnh tranh thị trường càng khốc liệt thì càng như vậy. 转瞬即逝 là vụt qua trong nháy mắt."),
         F(3, "Ví dụ ba: 一般说来，一个人受的教育愈多、愈好，占有的人类精神文化的财富也就愈多，创造、发展文化的能力也就愈强。 Nói chung, một người được giáo dục càng nhiều, càng tốt, thì của cải tinh thần văn hóa nhân loại mà họ có được cũng càng nhiều, năng lực sáng tạo và phát triển văn hóa cũng càng mạnh."),
         F(4, "Các bạn để ý các biến thể: 愈是……就愈是……，愈……就愈……, hoặc vế sau dùng 也就愈. Chữ 就 hay 也就 ở vế sau giúp câu văn chặt chẽ hơn.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: ghép 6 vế thành 3 đoạn với 愈", size=36,
    items=["A. 一个家庭，愈重视教育，教育的投入愈多，",
           "B. 市场经济是法制经济，愈是发达的市场经济，",
           "C. 经营活动愈是会受到完备的法规约束，从而，在法制的框架内展开充分的公平竞争。",
           "D. 他生就一副挑战式性格，愈是面对成功，",
           "E. 家庭成员的文化水平就愈高，综合素质也就愈高。",
           "F. 愈要为自己设定更高的目标。"],
    say=[F(0, "Luyện tập: hãy ghép sáu vế câu sau thành ba đoạn văn liền mạch. Vế A: 一个家庭，愈重视教育，教育的投入愈多。 Một gia đình càng coi trọng giáo dục, đầu tư cho giáo dục càng nhiều."),
         F(1, "Vế B: 市场经济是法制经济，愈是发达的市场经济。 Kinh tế thị trường là kinh tế pháp chế, kinh tế thị trường càng phát triển."),
         F(2, "Vế C: 经营活动愈是会受到完备的法规约束，从而，在法制的框架内展开充分的公平竞争。 Hoạt động kinh doanh càng chịu sự ràng buộc của hệ thống pháp quy hoàn chỉnh, từ đó triển khai cạnh tranh công bằng đầy đủ trong khuôn khổ pháp luật."),
         F(3, "Vế D: 他生就一副挑战式性格，愈是面对成功。 Anh ấy bẩm sinh có tính cách thích thử thách, càng đối mặt với thành công."),
         F(4, "Vế E: 家庭成员的文化水平就愈高，综合素质也就愈高。 Trình độ văn hóa của các thành viên gia đình càng cao, tố chất tổng hợp cũng càng cao."),
         F(5, "Vế F: 愈要为自己设定更高的目标。 Càng phải đặt cho mình mục tiêu cao hơn. Các bạn hãy tạm dừng và thử ghép nhé.")])

add("bullets", section="Ngữ pháp 注释", title="Đáp án: ghép vế với 愈", reveal=True, size=36,
    items=["(1) Ghép A với vế nào?",
           "Đáp án: A + E – 一个家庭，愈重视教育，教育的投入愈多，家庭成员的文化水平就愈高，综合素质也就愈高。",
           "(2) Ghép B với vế nào?",
           "Đáp án: B + C – 市场经济是法制经济，愈是发达的市场经济，经营活动愈是会受到完备的法规约束……",
           "(3) Ghép D với vế nào?",
           "Đáp án: D + F – 他生就一副挑战式性格，愈是面对成功，愈要为自己设定更高的目标。"],
    say=[F(0, "Đoạn thứ nhất: vế A nói về gia đình và giáo dục. Vế nào nối tiếp?"),
         F(1, "Đáp án: A cộng E. 一个家庭，愈重视教育，教育的投入愈多，家庭成员的文化水平就愈高，综合素质也就愈高。 Một gia đình càng coi trọng giáo dục, đầu tư càng nhiều, thì trình độ văn hóa của các thành viên càng cao, tố chất tổng hợp cũng càng cao."),
         F(2, "Đoạn thứ hai: vế B nói về kinh tế thị trường."),
         F(3, "Đáp án: B cộng C. 市场经济是法制经济，愈是发达的市场经济，经营活动愈是会受到完备的法规约束。 Kinh tế thị trường càng phát triển, hoạt động kinh doanh càng chịu ràng buộc của pháp quy hoàn chỉnh."),
         F(4, "Đoạn thứ ba: vế D nói về tính cách của một người."),
         F(5, "Đáp án: D cộng F. 他生就一副挑战式性格，愈是面对成功，愈要为自己设定更高的目标。 Anh ấy bẩm sinh thích thử thách, càng thành công lại càng đặt cho mình mục tiêu cao hơn. Mẹo làm bài: hãy tìm vế có chữ 愈 ở nửa đầu, rồi ghép với vế có chữ 愈 ở nửa sau.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 连年 – 连续", section="Phân biệt từ 词语辨析", title="Phân biệt 连年 và 连续",
    common="Giống nhau: đều có nghĩa liên tiếp không ngừng. Ví dụ: 他们连年/连续创造了高产纪录。",
    cols=[{"head": "连年",
           "lines": ["(1) Liên tiếp nhiều năm – chỉ dùng cho thời gian tính bằng năm, không có nghĩa khác",
                     "Đúng: 连年大丰收。",
                     "(2) Phía sau không mang cụm số lượng",
                     "Sai: 他连年三年获奖。",
                     "Đúng: 他连年获奖。"]},
          {"head": "连续",
           "lines": ["(1) Cái này nối tiếp cái kia – dùng cho mọi khoảng thời gian",
                     "Đúng: 连续下了三天雨。",
                     "Đúng: 他们连续工作了15个小时。",
                     "(2) Phía sau có thể mang cụm số lượng",
                     "Đúng: 他已经连续三天没吃东西了。"]}],
    say=["Tiếp theo là phần phân biệt từ: 连年 và 连续. Hai từ này cùng có chữ 连, nên rất dễ nhầm.",
         "Điểm giống nhau: cả hai đều có nghĩa liên tiếp không ngừng. Ví dụ: 他们连年创造了高产纪录。 Hoặc: 他们连续创造了高产纪录。 Cả hai câu đều đúng. Họ liên tiếp lập kỷ lục năng suất cao.",
         F(0, "Điểm khác thứ nhất. 连年 nghĩa là liên tiếp nhiều năm, chỉ dùng cho thời gian tính bằng năm, không có nghĩa nào khác. Ví dụ: 连年大丰收。 Nhiều năm liền được mùa lớn."),
         F(1, "Còn 连续 nghĩa là cái này nối tiếp cái kia, dùng được cho bất kỳ khoảng thời gian nào: ngày, giờ, lần. Ví dụ: 连续下了三天雨。 Mưa liền ba ngày. Và 他们连续工作了十五个小时。 Họ làm việc liên tục mười lăm tiếng đồng hồ."),
         F(0, "Điểm khác thứ hai. Sau 连年 không mang cụm số lượng. Nói 他连年三年获奖 là sai, chỉ nói 他连年获奖, anh ấy đoạt giải nhiều năm liền."),
         F(1, "Còn sau 连续 có thể mang cụm số lượng. Ví dụ: 他已经连续三天没吃东西了。 Anh ấy đã liền ba ngày không ăn gì rồi."),
         "Mẹo nhớ: 连年 tự nó đã chứa chữ 年, nên không cần và cũng không thể thêm số năm phía sau; 连续 thì linh hoạt, thêm được ba ngày, năm lần, mười lăm tiếng."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: chọn 连年 hay 连续?", reveal=True, size=36,
    items=["(1) 用同样的方法___念下去，直到不看卡片，念十遍不出错为止。",
           "Đáp án: 连续 – nối tiếp nhau từng lần, không phải tính bằng năm.",
           "(2) 人民生活在社会动荡和___战乱中，苦不堪言。",
           "Đáp án: 连年 – chiến tranh kéo dài nhiều năm liền.",
           "(3) 屏幕上会___出现几个数字，你要迅速记住它们。",
           "Đáp án: 连续 – các con số hiện ra liên tiếp, phía sau có 几个.",
           "(4) 最近几年来，由于管理混乱、经营不善，导致___亏损。",
           "Đáp án: 连年 – lỗ nhiều năm liền (几年来)."],
    say=[F(0, "Bây giờ chúng ta làm thử. Câu một: 用同样的方法什么念下去，直到不看卡片，念十遍不出错为止。 Dùng cùng một cách, đọc liên tục cho đến khi không nhìn thẻ, đọc mười lần không sai mới thôi. Các bạn chọn từ nào?"),
         F(1, "Đáp án: 连续. Ở đây là đọc nối tiếp nhau từng lần, không liên quan đến năm."),
         F(2, "Câu hai: 人民生活在社会动荡和什么战乱中，苦不堪言。 Người dân sống trong cảnh xã hội rối ren và chiến loạn triền miên, khổ không kể xiết."),
         F(3, "Đáp án: 连年. 连年战乱 là chiến loạn nhiều năm liền."),
         F(4, "Câu ba: 屏幕上会什么出现几个数字，你要迅速记住它们。 Trên màn hình sẽ liên tiếp hiện ra mấy con số, bạn phải nhanh chóng ghi nhớ chúng."),
         F(5, "Đáp án: 连续. Các con số hiện ra nối tiếp nhau trong vài giây, không phải nhiều năm."),
         F(6, "Câu bốn: 最近几年来，由于管理混乱、经营不善，导致什么亏损。 Mấy năm gần đây, do quản lý lộn xộn, kinh doanh kém, dẫn đến thua lỗ nhiều năm liền."),
         F(7, "Đáp án: 连年. Câu có 几年来, nói về nhiều năm, nên dùng 连年亏损, lỗ liền mấy năm.")])

# ======================= KỸ NĂNG VIẾT =======================
add("bullets", chapter="Kỹ năng viết: lặp từ khóa", section="Tu từ 篇章修辞", title="Lặp lại từ khóa, đẩy chủ đề tiến lên", size=36,
    items=["重复关键词，推进主题",
           "Về giao tiếp: lặp từ khóa làm nổi bật một hay vài thông tin",
           "Về kết cấu: lặp đi lặp lại từ khóa quan trọng nhất giúp chủ đề không ngừng được đẩy tới",
           "→ Một trong những cách làm đoạn văn liền mạch, câu văn trôi chảy",
           "(1) 有了纸，书写就需要墨水儿，于是有人发明了墨；字画、书信上需要盖章，于是印章开始流行；碑刻、拓印技术被广泛运用，于是有人联想到……"],
    say=["Phần cuối cùng về lý thuyết là kỹ năng viết: lặp lại từ khóa, đẩy chủ đề tiến lên. Tiếng Trung gọi là 重复关键词，推进主题.",
         F(1, "Lặp từ khóa có tác dụng rất quan trọng trong văn bản. Về mặt giao tiếp, lặp lại từ khóa giúp làm nổi bật một hoặc vài thông tin."),
         F(2, "Về mặt kết cấu, việc không ngừng lặp lại từ khóa quan trọng nhất giúp chủ đề được đẩy tới liên tục."),
         F(3, "Đây là một trong những cách làm cho đoạn văn liền mạch, câu văn trôi chảy. Chú ý: lặp từ khóa là lặp có chủ ý, khác với lặp chủ ngữ thừa thãi mà ta đã học cách tỉnh lược."),
         F(4, "Ví dụ một, lấy từ bài khóa: các từ 需要 và 于是 lặp lại nhiều lần. Mỗi lần lặp, câu chuyện tiến thêm một bước: có giấy, cần mực, có mực, cần con dấu, rồi đến in khắc bản. Chủ đề về sự ra đời của nghề in cứ thế được đẩy tới.")])

add("bullets", section="Tu từ 篇章修辞", title="Lặp từ khóa: thêm hai ví dụ", size=36,
    items=["(2) 我开始每天至少写两千字。没有为“一定要换成稿费”而写，没有读者也写，自己寻找题目，把写作当成生活的一部分。有时，写不出自己想写的东西来，那就写一些无聊的消息稿或整理访问稿，我甚至还愿意接翻译稿，只求有字可写。",
           "→ Từ khóa: 写 – nhấn mạnh quyết tâm viết mỗi ngày",
           "(3) 佩珊！佩珊！我心里难过极了！想到一个人会死，而且会突然地就死，我真是难过极了！我不肯死！我一定不能死！可是我们总有一天要死。",
           "→ Từ khóa: 死 · 难过极了 – dồn nén cảm xúc"],
    say=[F(0, "Ví dụ hai: 我开始每天至少写两千字。没有为一定要换成稿费而写，没有读者也写，自己寻找题目，把写作当成生活的一部分。有时，写不出自己想写的东西来，那就写一些无聊的消息稿或整理访问稿，我甚至还愿意接翻译稿，只求有字可写。"),
         F(0, "Dịch: Tôi bắt đầu mỗi ngày viết ít nhất hai nghìn chữ. Không phải viết vì nhất định phải đổi lấy nhuận bút, không có độc giả cũng viết, tự tìm đề tài, coi viết lách là một phần cuộc sống. Có lúc không viết được điều mình muốn viết thì viết mấy bản tin nhạt nhẽo hay chỉnh lý bài phỏng vấn, tôi thậm chí còn sẵn lòng nhận bản dịch, chỉ cần có chữ để viết."),
         F(1, "Từ khóa ở đây là 写, viết. Nó lặp lại hơn mười lần, nhấn mạnh quyết tâm viết bằng mọi giá của tác giả."),
         F(2, "Ví dụ ba: 佩珊！佩珊！我心里难过极了！想到一个人会死，而且会突然地就死，我真是难过极了！我不肯死！我一定不能死！可是我们总有一天要死。 Bội San! Bội San! Lòng em buồn quá! Nghĩ đến chuyện một người sẽ chết, mà lại chết đột ngột, em thật buồn quá! Em không muốn chết! Em nhất định không được chết! Nhưng rồi sẽ có một ngày chúng ta phải chết."),
         F(3, "Từ khóa là 死 và 难过极了. Việc lặp đi lặp lại khiến cảm xúc dồn nén, ngày càng dâng cao, làm người đọc cảm nhận rõ nỗi sợ hãi và đau buồn của nhân vật.")])

add("bullets", section="Tu từ 篇章修辞", title="Luyện tập: điền từ thích hợp (lặp từ khóa)", reveal=True, size=36,
    items=["小张的花店跟别人不一样的地方是免费送花，只要是有这种需求的，路近的送，路远的___；大花篮、大花束送，一支两支___；晴天送，雨天___；即使人手不够，小李亲自骑自行车___。",
           "Đáp án: 也送 · 也送 · 也送 · 也送",
           "→ Từ khóa 送 lặp lại nhiều lần: nhấn mạnh đặc điểm giao hoa miễn phí trong mọi hoàn cảnh"],
    say=[F(0, "Luyện tập: căn cứ vào ý của đoạn văn, điền từ thích hợp. 小张的花店跟别人不一样的地方是免费送花，只要是有这种需求的，路近的送，路远的什么；大花篮、大花束送，一支两支什么；晴天送，雨天什么；即使人手不够，小李亲自骑自行车什么。"),
         F(0, "Dịch: Điểm khác biệt của tiệm hoa nhà Tiểu Trương là giao hoa miễn phí; chỉ cần có nhu cầu, đường gần thì giao, đường xa cũng giao; giỏ hoa lớn, bó hoa to thì giao, một hai cành cũng giao; trời nắng giao, trời mưa cũng giao; dù thiếu người, Tiểu Lý cũng tự đạp xe đi giao. Các bạn hãy tạm dừng và thử điền."),
         F(1, "Đáp án: cả bốn chỗ trống đều là 也送. 路远的也送，一支两支也送，雨天也送，小李亲自骑自行车也送。"),
         F(2, "Chữ 送 được lặp lại tám lần, làm nổi bật đặc điểm của tiệm hoa: giao hoa miễn phí trong mọi hoàn cảnh. Đây chính là tác dụng của việc lặp từ khóa.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Viết thêm từ theo chữ cho sẵn", size=40,
    items=["例：文献 → 文章 · 文学 · 文人 · 作文",
           "增添 → 增加 · 增长 · 增强 · 增多",
           "发财 → 发展 · 发明 · 发现 · 发达",
           "外行 → 外国 · 外地 · 外表 · 外交",
           "故乡 → 故事 · 故宫 · 故居 · 家乡"],
    say=["Phần luyện tập. Bài tập một: bắt chước ví dụ, viết thêm các từ có chứa chữ được đánh dấu.",
         F(0, "Ví dụ mẫu: 文献, có 文章，文学，文人，作文. Tức là bài văn, văn học, văn nhân, và bài tập làm văn."),
         F(1, "增添, có thể mở rộng thành 增加，增长，增强，增多. Tức là tăng thêm, tăng trưởng, tăng cường, và tăng lên."),
         F(2, "发财, có 发展，发明，发现，发达. Tức là phát triển, phát minh, phát hiện, phát đạt."),
         F(3, "外行, có 外国，外地，外表，外交. Tức là nước ngoài, nơi khác, bề ngoài, và ngoại giao."),
         F(4, "故乡, có 故事，故宫，故居，家乡. Tức là câu chuyện, Cố Cung, nhà cũ của danh nhân, và quê nhà. Các bạn có thể tìm thêm nhiều từ khác nữa.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (1)", reveal=True, size=38,
    items=["(1) 孩子们很想了解生命是怎么开始的。（起源）",
           "Đáp án: 孩子们很想了解生命的起源。",
           "(2) 看到此情此景，我的脑海里浮现出许多往事。（联想）",
           "Đáp án: 看到此情此景，我联想到了许多往事。",
           "(3) 一个人的力量毕竟是有限的，还是团结力量大。（终究）",
           "Đáp án: 一个人的力量终究是有限的，还是团结力量大。"],
    say=[F(0, "Bài tập hai: dùng từ hoặc cấu trúc cho sẵn để viết lại câu. Câu một, dùng 起源: 孩子们很想了解生命是怎么开始的。 Bọn trẻ rất muốn biết sự sống bắt đầu như thế nào."),
         F(1, "Đáp án: 孩子们很想了解生命的起源。 Bọn trẻ rất muốn tìm hiểu nguồn gốc của sự sống."),
         F(2, "Câu hai, dùng 联想: 看到此情此景，我的脑海里浮现出许多往事。 Nhìn thấy cảnh này, trong đầu tôi hiện lên bao chuyện cũ."),
         F(3, "Đáp án: 看到此情此景，我联想到了许多往事。 Nhìn thấy cảnh này, tôi liên tưởng đến bao chuyện cũ."),
         F(4, "Câu ba, dùng 终究: 一个人的力量毕竟是有限的，还是团结力量大。 Sức một người dù sao cũng có hạn, đoàn kết mới là sức mạnh."),
         F(5, "Đáp án: thay 毕竟 bằng 终究: 一个人的力量终究是有限的，还是团结力量大。")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (2)", reveal=True, size=38,
    items=["(4) 随着孩子的陆续出生，家里增加了不少人口。（增添）",
           "Đáp án: 随着孩子的陆续出生，家里增添了不少人口。",
           "(5) 由于此地涉及国家机密，所以是不允许参观的。（谢绝）",
           "Đáp án: 此地涉及国家机密，谢绝参观。",
           "(6) 老师曾教导我们：“情况越紧急，越需要沉着冷静。”（愈……愈……）",
           "Đáp án: 老师曾教导我们：“情况愈紧急，愈需要沉着冷静。”"],
    say=[F(0, "Câu bốn, dùng 增添: 随着孩子的陆续出生，家里增加了不少人口。 Con cái lần lượt ra đời, trong nhà thêm không ít người."),
         F(1, "Đáp án: thay 增加 bằng 增添: 家里增添了不少人口。"),
         F(2, "Câu năm, dùng 谢绝: 由于此地涉及国家机密，所以是不允许参观的。 Vì nơi này liên quan đến bí mật quốc gia, nên không cho phép tham quan."),
         F(3, "Đáp án: 此地涉及国家机密，谢绝参观。 Nơi này liên quan đến bí mật quốc gia, xin miễn tham quan. Cách nói 谢绝参观 vừa ngắn gọn vừa lịch sự."),
         F(4, "Câu sáu, dùng 愈……愈……: 老师曾教导我们：情况越紧急，越需要沉着冷静。 Thầy từng dạy chúng tôi: tình huống càng khẩn cấp, càng cần bình tĩnh."),
         F(5, "Đáp án: thay 越 bằng 愈: 情况愈紧急，愈需要沉着冷静。 Đây là cách nói văn viết, rất hợp với lời dạy trang trọng của thầy giáo.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống", reveal=True, size=34,
    items=["(1) 神态 · 手法 · 涂抹 · 心得 · 盛开",
           "儿子从小就爱画画儿，从开始的随便___，到现在能画出___逼真的动物，___的花朵……绘画___越来越娴熟。一路走来，经历了许多艰辛，也收获了许多幸福，他愿意与大家一起分享画画儿的___。",
           "Đáp án: 涂抹 · 神态 · 盛开 · 手法 · 心得",
           "(2) 确立 · 一帆风顺 · 借鉴 · 信念 · 扎实",
           "想要成就一番事业，无论选择哪条路，都不会___的。首先要___自己的目标，给自己打下___的基础，多___别人成功的经验，抱着必胜的___坚持下去，最后的胜利一定属于你。",
           "Đáp án: 一帆风顺 · 确立 · 扎实 · 借鉴 · 信念"],
    say=[F(1, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn một có năm từ: 神态，手法，涂抹，心得，盛开. Con trai từ nhỏ đã thích vẽ, từ lúc đầu bôi vẽ tùy tiện, đến nay đã vẽ được những con vật có thần thái sống động, những bông hoa nở rộ, thủ pháp vẽ ngày càng thành thạo. Các bạn tạm dừng và thử điền nhé."),
         F(2, "Đáp án: 从开始的随便涂抹，到现在能画出神态逼真的动物，盛开的花朵，绘画手法越来越娴熟，他愿意与大家一起分享画画儿的心得。 Cậu sẵn lòng chia sẻ với mọi người kinh nghiệm vẽ tranh."),
         F(4, "Đoạn hai có năm từ: 确立，一帆风顺，借鉴，信念，扎实. Muốn làm nên sự nghiệp, dù chọn con đường nào cũng sẽ không thuận buồm xuôi gió."),
         F(5, "Đáp án: 都不会一帆风顺的。首先要确立自己的目标，给自己打下扎实的基础，多借鉴别人成功的经验，抱着必胜的信念坚持下去。 Trước hết phải xác định mục tiêu, xây nền tảng vững chắc, học hỏi kinh nghiệm thành công của người khác, ôm niềm tin tất thắng mà kiên trì, chiến thắng cuối cùng nhất định thuộc về bạn.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 4: Tìm từ khóa được lặp lại", reveal=True, size=34,
    items=["(1) 这泪水，是激动的泪水，兴奋的泪水，喜悦的泪水，收获的泪水。",
           "Đáp án: 泪水",
           "(2) 他是代表全民族的大多数，最正确、最勇敢、最坚决、最忠实、最热忱的空前的民族英雄。",
           "Đáp án: 最",
           "(3) 一根火柴，它自己熄灭了，却把别人点燃起来，点起了比自己大十倍、百倍、千倍以至数万倍的熊熊大火。",
           "Đáp án: 倍",
           "(4) 他用心观察着，眼前飞过的一只雁，一只麻雀，一只蝴蝶，一只蜻蜓，他都不放过。",
           "Đáp án: 一只"],
    say=[F(0, "Bài tập bốn: tìm từ khóa được lặp lại trong các đoạn sau. Câu một: 这泪水，是激动的泪水，兴奋的泪水，喜悦的泪水，收获的泪水。 Giọt nước mắt này là nước mắt xúc động, nước mắt hân hoan, nước mắt vui sướng, nước mắt của thành quả."),
         F(1, "Đáp án: 泪水, nước mắt."),
         F(2, "Câu hai: 他是代表全民族的大多数，最正确、最勇敢、最坚决、最忠实、最热忱的空前的民族英雄。 Ông là người anh hùng dân tộc chưa từng có, đại diện cho đa số cả dân tộc, đúng đắn nhất, dũng cảm nhất, kiên quyết nhất, trung thành nhất, nhiệt thành nhất."),
         F(3, "Đáp án: 最, nhất."),
         F(4, "Câu ba: 一根火柴，它自己熄灭了，却把别人点燃起来，点起了比自己大十倍、百倍、千倍以至数万倍的熊熊大火。 Một que diêm, tự nó tắt đi, nhưng lại thắp sáng người khác, nhóm lên ngọn lửa hừng hực lớn hơn chính nó mười lần, trăm lần, nghìn lần, thậm chí hàng vạn lần."),
         F(5, "Đáp án: 倍, lần. Sự lặp lại khiến ngọn lửa như lớn dần lên trước mắt người đọc."),
         F(6, "Câu bốn: 他用心观察着，眼前飞过的一只雁，一只麻雀，一只蝴蝶，一只蜻蜓，他都不放过。 Anh chăm chú quan sát, con nhạn, con chim sẻ, con bướm, con chuồn chuồn bay qua trước mắt, anh đều không bỏ sót."),
         F(7, "Đáp án: 一只, một con. Từ khóa lặp lại nhấn mạnh sự quan sát tỉ mỉ của nhân vật.")])

add("bullets", section="Luyện tập 练习", title="Mở rộng 扩展: hiểu nghĩa từng yếu tố (1)", size=36,
    items=["回收 – trở về + thu về → thu hồi (để tái sử dụng)",
           "开采 – khai phá + đào lấy (khoáng sản) → khai thác",
           "开除 – tách ra + bỏ đi → đuổi việc, đuổi học",
           "划分 – chia tổng thể thành phần + tách ra → phân chia",
           "请示 – xin + chỉ thị → xin chỉ thị (cấp trên)",
           "施加 – trao cho (áp lực, ảnh hưởng) + tăng thêm → gây (áp lực)"],
    say=["Phần mở rộng của sách giúp các bạn làm quen với ý nghĩa của từng yếu tố trong từ. Hiểu từng chữ thì sẽ hiểu cả từ.",
         F(0, "回收, hồi thu: 回 là trở về, 收 là thu về để tận dụng. Cả từ nghĩa là thu hồi, tái chế, ví dụ 回收废品, thu gom phế liệu."),
         F(1, "开采, khai thác: 开 là khai phá, 采 là đào lấy khoáng sản. 开采石油 là khai thác dầu mỏ."),
         F(2, "开除, khai trừ: 开 là làm tách ra, 除 là bỏ đi. Cả từ nghĩa là đuổi việc, đuổi học. Chú ý khai trừ trong tiếng Việt thường dùng với tổ chức, đảng phái, còn 开除 dùng rộng hơn."),
         F(3, "划分, hoạch phân: chữ đầu là chia một tổng thể thành nhiều phần, chữ sau là tách ra. Cả từ nghĩa là phân chia, ví dụ 划分区域, phân chia khu vực."),
         F(4, "请示, thỉnh thị: 请 là xin, 示 là chỉ thị. Cả từ nghĩa là xin ý kiến chỉ đạo của cấp trên."),
         F(5, "施加, thi gia: 施 là trao cho, tác động lên, như áp lực hay ảnh hưởng; 加 là tăng thêm. 施加压力 là gây áp lực.")])

add("bullets", section="Luyện tập 练习", title="Mở rộng 扩展: hiểu nghĩa từng yếu tố (2)", size=36,
    items=["玩弄 – đùa bỡn, dùng thủ đoạn không chính đáng + trêu đùa → đùa giỡn, giở trò",
           "应酬 – ứng phó + giao tiếp qua lại → xã giao, tiếp khách",
           "瞻仰 – nhìn lên + tôn kính ngưỡng mộ → chiêm ngưỡng",
           "铸造 – nấu chảy kim loại đổ khuôn + chế tạo → đúc",
           "落成 – đạt kết quả + hoàn thành → khánh thành (công trình)",
           "配套 – bổ sung cái còn thiếu + gộp thành bộ → đồng bộ"],
    say=[F(0, "玩弄: chữ đầu là đùa bỡn, sử dụng bằng thủ đoạn không chính đáng; chữ sau là trêu đùa. Cả từ nghĩa là đùa giỡn, giở trò, ví dụ 玩弄手段, giở thủ đoạn."),
         F(1, "应酬, ứng thù: chữ đầu là ứng phó, chữ sau là giao tiếp qua lại. Cả từ nghĩa là xã giao, tiếp khách, ví dụ 晚上有个应酬, tối nay có buổi tiếp khách."),
         F(2, "瞻仰, chiêm ngưỡng: 瞻 là nhìn lên phía trước, 仰 là tôn kính ngưỡng mộ. Âm Hán Việt giống hệt tiếng Việt."),
         F(3, "铸造, chú tạo: 铸 là nấu chảy kim loại rồi đổ vào khuôn, 造 là chế tạo. Cả từ nghĩa là đúc, ví dụ 铸造铜像, đúc tượng đồng."),
         F(4, "落成, lạc thành: chữ đầu là đạt được một kết quả, chữ sau là hoàn thành. Cả từ nghĩa là công trình xây xong, khánh thành, ví dụ 落成典礼, lễ khánh thành."),
         F(5, "配套, phối sáo: 配 là bổ sung cái còn thiếu, 套 là gộp những thứ cùng loại thành một bộ. Cả từ nghĩa là đồng bộ, ví dụ 配套设施, cơ sở vật chất đồng bộ.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 35", size=36,
    items=["Từ vựng trọng tâm: 起源 · 驱逐 · 里程碑 · 寄托 · 增添 · 喜闻乐见 · 谢绝 · 扎实 · 借鉴 · 再接再厉 · 心得 · 任重道远 · 一帆风顺",
           "Ngữ pháp: 终究 (suy cho cùng; rốt cuộc sẽ) · 愈……愈…… (càng… càng…, văn viết)",
           "Phân biệt: 连年 (nhiều năm liền, không mang số lượng) ≠ 连续 (liên tục, mang được số lượng)",
           "Viết: lặp lại từ khóa để làm nổi bật thông tin và đẩy chủ đề tiến lên",
           "## Bài tập về nhà (运用)",
           "Viết bài 我们的……艺术 (≥ 400 chữ): giới thiệu một loại hình hội họa dân tộc và câu chuyện về một họa sĩ tiêu biểu",
           "Gợi ý: 我们的东湖画艺术 – nguồn gốc, kỹ thuật, nghệ nhân; dùng 终究, 愈……愈…… và lặp từ khóa"],
    say=["Chúng ta cùng tổng kết bài ba mươi lăm.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 起源，驱逐，里程碑，寄托，增添，喜闻乐见，谢绝，扎实，借鉴，再接再厉，心得，任重道远，一帆风顺."),
         F(1, "Về ngữ pháp: 终究 có hai cách dùng: nhấn mạnh bản chất không đổi, nghĩa là suy cho cùng; và dùng trong 终究会，终究要, nghĩa là rốt cuộc nhất định sẽ. Còn 愈……愈…… giống 越……越……, nhưng dùng trong văn viết."),
         F(2, "Về phân biệt từ: 连年 là nhiều năm liền, phía sau không mang cụm số lượng; 连续 là liên tục, dùng cho mọi khoảng thời gian, và có thể mang cụm số lượng."),
         F(3, "Về kỹ năng viết: lặp lại từ khóa một cách có chủ ý để làm nổi bật thông tin và đẩy chủ đề tiến lên, giúp đoạn văn liền mạch."),
         F(5, "Bài tập về nhà, theo phần vận dụng của sách: bài khóa đã giới thiệu tranh Tết khắc gỗ và nghệ nhân Trương Quang Ninh. Ở đất nước các bạn chắc chắn cũng có loại hình hội họa mang bản sắc dân tộc và những họa sĩ tiêu biểu. Hãy viết một bài với tiêu đề 我们的什么艺术, ít nhất bốn trăm chữ."),
         F(6, "Thầy gợi ý: các bạn có thể viết 我们的东湖画艺术, nghệ thuật tranh Đông Hồ của chúng ta: kể nguồn gốc, kỹ thuật làm tranh, và câu chuyện về một nghệ nhân. Hãy thử dùng 终究，愈……愈……, và cách lặp từ khóa trong bài viết nhé."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Hẹn gặp lại các bạn ở bài ba mươi sáu: 中国古代书院, Thư viện thời cổ đại Trung Quốc, tức những học viện nơi các bậc học giả xưa giảng dạy và đọc sách. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Hạ) – Bài 35: 走近木版年画 (Đến gần tranh Tết khắc gỗ)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (cùng pinyin, cùng thanh; cụm dài trước)
    "tts_replace": {
        "为更多民众所喜爱": "维更多民众所喜爱",  # wéi
        "吞吞吐吐": "吞吞土土",    # tǔ
        "唠唠叨叨": "劳劳刀刀",    # láoláo dāodāo
        "系出名门": "细出名门",    # xì
        "各有所长": "各有所常",    # cháng
        "任重道远": "认众道远",    # rèn zhòng
        "曾真诚": "层真诚",        # céng
        "曾教导": "层教导",        # céng
        "为内容": "维内容",        # yǐ…wéi nèiróng
        "为止": "维止",            # wéizhǐ
        "揭露": "揭路",            # jiēlù
        "拓印": "踏印",            # tàyìn
        "外行": "外航",            # wàiháng
        "内行": "内航",            # nèiháng
        "同行": "同航",            # tóngháng (người cùng nghề)
        "还价": "环价",            # huánjià
        "扎实": "渣实",            # zhā
        "干劲": "赣进",            # gànjìn
        "心得": "心德",            # xīndé
        "戏曲": "戏取",            # xìqǔ
        "载体": "在体",            # zàitǐ
        "数年": "树年",            # shù nián
        "数万": "树万",            # shù wàn
        "两朝": "两潮",            # cháo
        "清朝": "清潮",            # cháo
        "长大": "掌大",            # zhǎng
        "沉着": "沉酌",            # chénzhuó
        "当成": "荡成",            # dàngchéng
        "重复": "虫复",            # chóngfù
        "种花": "众花",            # zhòng huā
        "磨墨": "魔墨",            # mó mò
        "划分": "化分",            # huàfēn
        "应酬": "映酬",            # yìngchou
        "翘": "俏",                # qiào
    },
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai35.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
