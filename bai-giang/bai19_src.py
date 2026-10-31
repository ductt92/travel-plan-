#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Thượng) – Bài 19 «无阳光的深海世界». Chạy để sinh bai19.json."""
import json
import os

TAG = "HSK 6 (Thượng) · Bài 19 · 无阳光的深海世界"
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
    top="Giáo trình chuẩn HSK 6 – Quyển Thượng",
    zh="无阳光的深海世界", py="Wú yángguāng de shēnhǎi shìjiè",
    vi="Bài 19: Thế giới biển sâu không ánh mặt trời",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Thượng.",
         "Hôm nay chúng ta học bài mười chín: 无阳光的深海世界。 Nghĩa là: Thế giới biển sâu không có ánh mặt trời.",
         "Bài này thuộc Chủ đề năm, 美丽家园, Quê hương xinh đẹp. Ngôi nhà chung của chúng ta không chỉ có núi rừng, sông hồ, mà còn có cả đáy biển sâu hàng nghìn mét, nơi ánh mặt trời không bao giờ chiếu tới.",
         "Người ta vẫn nói vạn vật sinh trưởng nhờ mặt trời. Thế nhưng các nhà khoa học lại phát hiện ra cả một thế giới sinh vật sống dưới đáy biển tối đen, nóng bỏng và áp suất cực lớn. Chúng sống bằng cách nào? Chúng ta cùng tìm hiểu nhé."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài khóa: thế giới sinh vật dưới đáy biển sâu sống nhờ đâu khi không có ánh mặt trời",
           "Nắm vững 46 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: liên từ 进而, động từ 得以, phó từ 偏偏",
           "Phân biệt hai phó từ 历来 và 从来",
           "Mở rộng: câu sai do mơ hồ về nghĩa (歧义句) và các kết hợp từ thường gặp"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa: các nhà khoa học đã phát hiện gì dưới đáy biển sâu, và những sinh vật ở đó sống nhờ vào đâu khi không có ánh mặt trời."),
         F(1, "Thứ hai, nắm vững bốn mươi sáu từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học ba điểm ngữ pháp: liên từ 进而, nghĩa là rồi tiến thêm một bước; động từ 得以, nghĩa là nhờ đó mà có thể; và phó từ 偏偏, nghĩa là lại cứ, cố tình."),
         F(3, "Thứ tư, phân biệt hai phó từ rất dễ nhầm: 历来 và 从来, đều có nghĩa là xưa nay, từ trước đến giờ."),
         F(4, "Thứ năm, phần mở rộng: nhận biết câu sai do mơ hồ về nghĩa, tiếng Trung gọi là 歧义句, và làm quen với mười hai từ cùng các kết hợp thường gặp."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Khởi động: Làm quen tên các sinh vật biển", size=40,
    items=["蛤蜊 gélí – con nghêu, con ngao",
           "蚌 bàng – con trai (loài nhuyễn thể hai mảnh vỏ)",
           "蟹 xiè – con cua",
           "贝壳 bèiké – vỏ sò, vỏ ốc",
           "红冠蠕虫 hóngguān rúchóng – giun ống mào đỏ (sống ở miệng phun nhiệt dưới đáy biển)"],
    say=["Chúng ta bắt đầu bằng phần khởi động. Sách yêu cầu các bạn nhìn tranh và làm quen với tên của một số sinh vật. Những sinh vật này đều sẽ xuất hiện trong bài khóa.",
         F(0, "蛤蜊。 Đây là con nghêu, hay con ngao, loài có hai mảnh vỏ cứng, rất quen thuộc trong các món hải sản."),
         F(1, "蚌。 Đây là con trai, cũng là loài nhuyễn thể có hai mảnh vỏ, có loài còn tạo ra ngọc trai. Trong bài khóa có cụm 白蚌, con trai trắng."),
         F(2, "蟹。 Đây là con cua. Trong khẩu ngữ, người Trung Quốc hay nói 螃蟹."),
         F(3, "贝壳。 Đây là vỏ sò, vỏ ốc. Từ này là từ mới của bài, lát nữa thầy sẽ giảng kỹ hơn."),
         F(4, "红冠蠕虫。 Đây là một loài giun ống có phần đầu màu đỏ như chiếc mào, sống thành từng cụm quanh các miệng phun nhiệt dưới đáy biển sâu. 红 là màu đỏ, 冠 ở đây là cái mào, 蠕虫 là loài giun. Loài này chính là nhân vật nổi bật ở cuối bài khóa.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 疑 và 地", size=38,
    items=["## 疑 (nghi): ngờ, không tin, chưa rõ",
           "质疑 chất vấn · 怀疑 hoài nghi · 多疑 đa nghi · 生疑 sinh nghi · 可疑 khả nghi · 无疑 chắc chắn · 猜疑 ngờ vực",
           "疑惑 nghi hoặc · 疑心 lòng ngờ vực · 疑点 điểm đáng ngờ · 疑难 khó giải quyết · 疑问 câu hỏi · 半信半疑 bán tín bán nghi",
           "## 地 (địa): đất, mặt đất, nơi chốn",
           "地壳 vỏ trái đất · 地方 nơi, địa phương · 地图 bản đồ · 地点 địa điểm · 地球 trái đất · 地址 địa chỉ · 地理 địa lý",
           "地区 khu vực · 地震 động đất · 当地 địa phương đó · 陆地 lục địa · 土地 đất đai · 耕地 đất canh tác"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo, rất có lợi cho người Việt vì hầu hết các chữ đều có âm Hán Việt quen thuộc.",
         F(0, "Nhóm thứ nhất có chữ nghi, nghĩa là ngờ vực, không tin, hoặc chưa rõ ràng."),
         F(1, "质疑，怀疑，多疑，生疑，可疑，无疑，猜疑。 Tức là: chất vấn, hoài nghi, đa nghi, sinh nghi, khả nghi, không còn nghi ngờ gì nữa, và ngờ vực. Từ 质疑 có trong bài khóa: các nhà khoa học 提出了质疑, đặt ra nghi vấn với một chân lý cũ."),
         F(2, "疑惑，疑心，疑点，疑难，疑问，半信半疑。 Tức là: nghi hoặc, lòng ngờ vực, điểm đáng ngờ, khó khăn chưa giải quyết được, câu hỏi, và bán tín bán nghi."),
         F(3, "Nhóm thứ hai có chữ địa, nghĩa là đất, mặt đất, hoặc nơi chốn."),
         F(4, "地壳，地方，地图，地点，地球，地址，地理。 Tức là: vỏ trái đất, nơi chốn hay địa phương, bản đồ, địa điểm, trái đất, địa chỉ, và địa lý. Chú ý: trong từ 地壳, chữ thứ hai đọc như chữ đầu của 窍门, thanh bốn, khác với cách đọc trong 贝壳. Từ 地壳 cũng có trong bài khóa."),
         F(5, "地区，地震，当地，陆地，土地，耕地。 Tức là: khu vực, động đất, địa phương đó, lục địa, đất đai, và đất canh tác.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 裂 và 探", size=38,
    items=["## 裂 (liệt): nứt, nẻ, tách ra",
           "裂缝 khe nứt · 裂开 nứt ra · 裂口 vết nứt · 裂片 mảnh vỡ · 分裂 phân liệt, chia rẽ",
           "干裂 khô nứt nẻ · 破裂 vỡ, tan vỡ · 四分五裂 chia năm xẻ bảy",
           "## 探 (thám): dò, tìm hiểu, thăm dò",
           "探究 tìm tòi nghiên cứu · 探求 tìm kiếm · 探路 dò đường · 探索 thăm dò, khám phá · 探明 dò rõ",
           "探讨 thảo luận · 探险 thám hiểm · 探听 nghe ngóng · 试探 thăm dò thử"],
    say=[F(0, "Nhóm thứ ba có chữ liệt, nghĩa là nứt, nẻ, tách ra, như trong từ phân liệt."),
         F(1, "裂缝，裂开，裂口，裂片，分裂。 Tức là: khe nứt, nứt ra, vết nứt, mảnh vỡ, và phân liệt, chia rẽ. Bài khóa có câu 海水从地壳分裂而成的裂缝渗透到地下, nước biển thấm xuống lòng đất qua những khe nứt do vỏ trái đất tách ra."),
         F(2, "干裂，破裂，四分五裂。 Tức là: khô nứt nẻ, tan vỡ, và chia năm xẻ bảy."),
         F(3, "Nhóm cuối cùng có chữ thám, như trong thám hiểm, nghĩa là dò, tìm hiểu."),
         F(4, "探究，探求，探路，探索，探明。 Tức là: tìm tòi nghiên cứu, tìm kiếm, dò đường, thăm dò khám phá, và dò cho rõ. Từ 探索 và 探究 đều có trong bài khóa."),
         F(5, "探讨，探险，探听，试探。 Tức là: thảo luận, thám hiểm, nghe ngóng, và thăm dò thử."),
         "Các bạn thấy không, chỉ cần nắm nghĩa của một chữ gốc, ta có thể đoán được nghĩa của cả một nhóm từ. Hãy áp dụng cách này khi học từ mới nhé."])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đồng âm để đọc từ một chữ])
V = [
    ("俗话", "súhuà", "tục thoại", "danh từ", "tục ngữ, câu nói dân gian", "俗话说，好的开始是成功的一半。", "Tục ngữ có câu: khởi đầu tốt là thành công một nửa.",
     "Danh từ, nghĩa là tục ngữ, câu nói lưu truyền trong dân gian. Mẫu quen thuộc nhất là 俗话说, tục ngữ có câu. Bài khóa mở đầu bằng câu 俗话说万物生长靠太阳."),
    ("历来", "lìlái", "lịch lai", "phó từ", "xưa nay, từ trước đến nay", "这里历来是重要的交通中心。", "Nơi đây xưa nay vẫn là trung tâm giao thông quan trọng.",
     "Phó từ, nghĩa là xưa nay, từ trước đến nay vẫn thế. Từ này mang màu sắc văn viết. Lát nữa chúng ta sẽ so sánh kỹ 历来 với 从来."),
    ("维持", "wéichí", "duy trì", "động từ", "duy trì, giữ gìn", "他靠打工维持生活。", "Anh ấy sống qua ngày nhờ đi làm thêm.",
     "Động từ, nghĩa là duy trì, giữ cho một trạng thái tiếp tục tồn tại. Hay gặp: 维持生命, duy trì sự sống; 维持秩序, giữ trật tự; 维持生活, sống qua ngày."),
    ("众所周知", "zhòngsuǒzhōuzhī", "chúng sở chu tri", "thành ngữ", "mọi người đều biết", "众所周知，吸烟有害健康。", "Ai cũng biết hút thuốc có hại cho sức khỏe.",
     "Thành ngữ, nghĩa là điều mà mọi người đều biết. 众 là mọi người, 周 là khắp, 知 là biết. Thường đứng đầu câu, sau đó là dấu phẩy, hoặc làm định ngữ như 众所周知的真理."),
    ("真理", "zhēnlǐ", "chân lý", "danh từ", "chân lý", "实践是检验真理的唯一标准。", "Thực tiễn là tiêu chuẩn duy nhất để kiểm nghiệm chân lý.",
     "Danh từ, nghĩa là chân lý, âm Hán Việt và nghĩa giống hệt tiếng Việt."),
    ("认定", "rèndìng", "nhận định", "động từ", "cho rằng (chắc chắn), xác nhận", "我认定他是个可靠的人。", "Tôi tin chắc anh ấy là người đáng tin cậy.",
     "Động từ, nghĩa là tin chắc, khẳng định là như vậy, hoặc chính thức xác nhận. Cẩn thận, đây là từ dễ nhầm: nhận định trong tiếng Việt là đưa ra nhận xét, đánh giá; còn 认定 là đã kết luận chắc chắn, khó thay đổi. Trong bài, 早已认定为准则 là từ lâu đã coi là nguyên tắc."),
    ("准则", "zhǔnzé", "chuẩn tắc", "danh từ", "nguyên tắc, chuẩn mực", "诚实是做人的基本准则。", "Trung thực là chuẩn mực cơ bản để làm người.",
     "Danh từ, nghĩa là nguyên tắc, chuẩn mực để làm theo. Hay gặp: 行为准则, chuẩn mực hành vi."),
    ("定义", "dìngyì", "định nghĩa", "danh từ", "định nghĩa", "你能给幸福下个定义吗？", "Bạn có thể đưa ra định nghĩa về hạnh phúc không?",
     "Danh từ, nghĩa là định nghĩa. Chú ý cách kết hợp: đưa ra định nghĩa là 下定义, cho cái gì đó một định nghĩa là 给什么下定义."),
    ("潜水", "qiánshuǐ", "tiềm thủy", "động từ", "lặn", "我们夏天去海边潜水吧。", "Mùa hè chúng ta ra biển lặn nhé.",
     "Động từ, nghĩa là lặn xuống nước. 潜 là chìm, ẩn dưới mặt nước, như tiềm trong tàu tiềm thủy, tức tàu ngầm."),
    ("繁殖", "fánzhí", "phồn thực", "động từ", "sinh sôi, sinh sản", "春天是很多动物繁殖的季节。", "Mùa xuân là mùa sinh sản của nhiều loài động vật.",
     "Động từ, nghĩa là sinh sôi nảy nở, sinh sản. Dùng cho động vật, thực vật, vi khuẩn, không dùng cho con người."),
    ("场所", "chǎngsuǒ", "trường sở", "danh từ", "nơi, nơi chốn", "公共场所禁止吸烟。", "Cấm hút thuốc ở nơi công cộng.",
     "Danh từ, nghĩa là nơi, chỗ diễn ra một hoạt động nào đó. Hay gặp nhất là 公共场所, nơi công cộng. Chữ đầu đọc thanh ba."),
    ("古怪", "gǔguài", "cổ quái", "tính từ", "kỳ quặc, kỳ dị", "这个老人的脾气很古怪。", "Tính tình ông cụ này rất kỳ quặc.",
     "Tính từ, nghĩa là kỳ quặc, khác thường, ít thấy. Trong bài, 长相古怪 là hình dạng kỳ dị."),
    ("贝壳", "bèiké", "bối xác", "danh từ", "vỏ sò, vỏ ốc", "孩子们在海边捡贝壳。", "Bọn trẻ nhặt vỏ sò trên bãi biển.",
     "Danh từ, nghĩa là vỏ sò, vỏ ốc. Lưu ý: chữ cuối của từ này đọc thanh hai; nhưng trong từ 地壳, vỏ trái đất, nó lại đọc như chữ đầu của 窍门, thanh bốn."),
    ("诧异", "chàyì", "sá dị", "tính từ", "kinh ngạc, lấy làm lạ", "听到这个消息，大家都很诧异。", "Nghe tin này, mọi người đều rất kinh ngạc.",
     "Tính từ, nghĩa là kinh ngạc, lấy làm lạ vì điều gì đó khác thường. Trong bài, 科学家深感诧异 là các nhà khoa học vô cùng kinh ngạc."),
    ("样品", "yàngpǐn", "dạng phẩm", "danh từ", "hàng mẫu, mẫu vật", "请先给我们寄一些样品。", "Xin hãy gửi trước cho chúng tôi một ít hàng mẫu.",
     "Danh từ, nghĩa là hàng mẫu trong buôn bán, hoặc mẫu vật trong nghiên cứu khoa học. Trong bài là mẫu vật mang lên từ đáy biển."),
    ("刺", "cì", "thứ, thích", "động từ", "đâm, chọc; kích thích (giác quan)", "阳光刺得我睁不开眼睛。", "Ánh nắng chói đến mức tôi không mở mắt ra được.",
     "Động từ, nghĩa gốc là đâm, chọc bằng vật nhọn; nghĩa mở rộng là kích thích mạnh vào giác quan. Hay gặp: 刺鼻, xộc vào mũi; 刺眼, chói mắt; 刺耳, chói tai. Trong bài, 刺鼻臭蛋气味 là mùi trứng thối xộc lên mũi.", "次"),
    ("气味", "qìwèi", "khí vị", "danh từ", "mùi", "厨房里有一股奇怪的气味。", "Trong bếp có một mùi lạ.",
     "Danh từ, nghĩa là mùi. Lượng từ thường dùng là 股: 一股气味, một luồng mùi."),
    ("恍然大悟", "huǎngrán dà wù", "hoảng nhiên đại ngộ", "thành ngữ", "bỗng nhiên tỉnh ngộ, chợt hiểu ra", "听了老师的解释，我才恍然大悟。", "Nghe thầy giải thích, tôi mới chợt hiểu ra.",
     "Thành ngữ, nghĩa là bỗng nhiên hiểu ra, vỡ lẽ. 恍然 là bỗng chốc, 悟 là hiểu ra, như giác ngộ."),
    ("进而", "jìn'ér", "tiến nhi", "liên từ", "rồi tiến thêm, từ đó tiến tới", "先学好拼音，进而学习汉字。", "Trước hết học tốt phiên âm, rồi từ đó tiến tới học chữ Hán.",
     "Liên từ, đặt ở đầu vế sau, nghĩa là trên cơ sở đã có thì tiến thêm một bước. Đây là điểm ngữ pháp thứ nhất của bài."),
    ("分裂", "fēnliè", "phân liệt", "động từ", "tách ra, chia ra; chia rẽ", "细胞分裂是生命的基本现象。", "Phân bào là hiện tượng cơ bản của sự sống.",
     "Động từ, nghĩa là một chỉnh thể tách ra thành nhiều phần. Dùng cho vật chất như 细胞分裂, phân bào; và cho tổ chức, quốc gia, nghĩa là chia rẽ."),
    ("渗透", "shèntòu", "thẩm thấu", "động từ", "thẩm thấu, ngấm vào, thấm", "雨水慢慢渗透到土里。", "Nước mưa từ từ ngấm vào đất.",
     "Động từ, nghĩa là chất lỏng ngấm dần qua một vật. Nghĩa bóng là một ảnh hưởng nào đó dần dần thâm nhập vào."),
    ("细菌", "xìjūn", "tế khuẩn", "danh từ", "vi khuẩn", "有些细菌对人体是有益的。", "Có những loại vi khuẩn có lợi cho cơ thể người.",
     "Danh từ, nghĩa là vi khuẩn. 细 là nhỏ, 菌 là nấm, khuẩn. Chữ thứ hai đọc thanh một."),
    ("过滤", "guòlǜ", "quá lự", "động từ", "lọc", "这种水要过滤以后才能喝。", "Loại nước này phải lọc rồi mới uống được.",
     "Động từ, nghĩa là lọc, cho chất lỏng hay khí đi qua để giữ lại tạp chất. Trong bài, 过滤海水中的食物 là lọc thức ăn trong nước biển."),
    ("来源", "láiyuán", "lai nguyên", "danh từ", "nguồn, nguồn gốc", "工资是他唯一的收入来源。", "Tiền lương là nguồn thu nhập duy nhất của anh ấy.",
     "Danh từ, nghĩa là nguồn, nơi sự vật bắt nguồn. Hay gặp: 收入来源, nguồn thu nhập; 食物来源, nguồn thức ăn."),
    ("合成", "héchéng", "hợp thành", "động từ", "tổng hợp, hợp thành", "这张照片是用电脑合成的。", "Bức ảnh này được ghép bằng máy tính.",
     "Động từ, nghĩa là ghép nhiều phần thành một chỉnh thể; trong hóa học là tổng hợp. Chú ý: tiếng Việt nói tổng hợp, còn tiếng Trung nói 合成. Trong bài có thuật ngữ 化学合成, hóa tổng hợp."),
    ("解放", "jiěfàng", "giải phóng", "động từ", "giải phóng, phóng thích", "我们要解放思想，大胆创新。", "Chúng ta phải giải phóng tư tưởng, mạnh dạn đổi mới.",
     "Động từ, nghĩa là giải phóng. 解放思想 là giải phóng tư tưởng, tức là thoát khỏi lối nghĩ cũ."),
    ("迈", "mài", "mại", "động từ", "bước, sải bước", "他迈出了人生的第一步。", "Anh ấy đã bước bước đầu tiên của cuộc đời.",
     "Động từ, nghĩa là bước, sải bước dài. Thường dùng theo nghĩa bóng: 迈向未来, tiến về tương lai. Trong bài, 迈向地球以外 là tiến ra ngoài trái đất."),
    ("探索", "tànsuǒ", "thám sách", "động từ", "thăm dò, tìm tòi, khám phá", "人类从未停止探索宇宙的奥秘。", "Loài người chưa bao giờ ngừng khám phá bí ẩn vũ trụ.",
     "Động từ, nghĩa là tìm tòi, khám phá những điều chưa biết. Tân ngữ thường là 奥秘, bí ẩn; 秘密, bí mật; 道路, con đường."),
    ("据悉", "jùxī", "cứ tất", "động từ", "theo nguồn tin, được biết", "据悉，这座大桥将于明年完工。", "Được biết, cây cầu này sẽ hoàn thành vào năm sau.",
     "Động từ, nghĩa là theo những gì được biết. Từ này dùng trong văn viết, nhất là tin tức báo chí, và thường đứng đầu câu."),
    ("忍受", "rěnshòu", "nhẫn thụ", "động từ", "chịu đựng", "我再也忍受不了这里的噪音了。", "Tôi không chịu nổi tiếng ồn ở đây nữa rồi.",
     "Động từ, nghĩa là chịu đựng đau đớn, khó khăn, hay những điều không vui. Trong bài, 忍受高温 là chịu được nhiệt độ cao."),
    ("超越", "chāoyuè", "siêu việt", "động từ", "vượt qua, hơn hẳn", "他超越了自己的最好成绩。", "Anh ấy đã vượt qua thành tích tốt nhất của chính mình.",
     "Động từ, nghĩa là vượt qua. Cẩn thận: siêu việt trong tiếng Việt là tính từ, nghĩa là xuất chúng; còn 超越 là động từ, phía sau có tân ngữ: 超越想象, vượt ngoài sức tưởng tượng."),
    ("摄氏度", "shèshìdù", "nhiếp thị độ", "lượng từ", "độ C", "今天最高气温三十五摄氏度。", "Hôm nay nhiệt độ cao nhất là ba mươi lăm độ C.",
     "Lượng từ, nghĩa là độ C, đơn vị đo nhiệt độ. Ký hiệu viết là chữ C có vòng tròn nhỏ phía trước, đọc là 摄氏度."),
    ("丧失", "sàngshī", "táng thất", "động từ", "mất đi, mất mát", "失败了几次，他也没有丧失信心。", "Thất bại mấy lần, anh ấy vẫn không mất niềm tin.",
     "Động từ, nghĩa là mất đi, thường là những thứ trừu tượng hoặc quan trọng: 丧失信心, mất niềm tin; 丧失生命, mất mạng. Chữ đầu đọc thanh bốn."),
    ("偏偏", "piānpiān", "thiên thiên", "phó từ", "lại cứ, cố tình; trái lại", "我让他别去，他偏偏要去。", "Tôi bảo anh ấy đừng đi, anh ấy lại cứ muốn đi.",
     "Phó từ, nghĩa là lại cứ, cố tình làm trái; hoặc sự thật lại trái với mong muốn. Đây là điểm ngữ pháp thứ ba của bài."),
    ("真相", "zhēnxiàng", "chân tướng", "danh từ", "sự thật, chân tướng", "警察终于查明了事情的真相。", "Cảnh sát cuối cùng đã điều tra rõ sự thật của vụ việc.",
     "Danh từ, nghĩa là sự thật, bộ mặt thật của sự việc. Hay gặp: 查明真相, điều tra rõ sự thật; 真相大白, sự thật được phơi bày."),
    ("华丽", "huálì", "hoa lệ", "tính từ", "lộng lẫy, tráng lệ", "她穿着一件华丽的礼服。", "Cô ấy mặc một bộ lễ phục lộng lẫy.",
     "Tính từ, nghĩa là đẹp đẽ, lộng lẫy, rực rỡ. Hán Việt hoa lệ, như trong cụm từ thành phố hoa lệ."),
    ("阵容", "zhènróng", "trận dung", "danh từ", "đội hình, lực lượng", "这部电影的演员阵容非常强大。", "Dàn diễn viên của bộ phim này vô cùng hùng hậu.",
     "Danh từ, nghĩa gốc là thế trận, đội hình quân đội; nay hay dùng chỉ lực lượng, đội hình của một tập thể: 演员阵容, dàn diễn viên. Trong bài, 强大而华丽的阵容 là đội hình hùng hậu và lộng lẫy."),
    ("有条不紊", "yǒutiáo-bùwěn", "hữu điều bất vặn", "thành ngữ", "ngăn nắp, có trật tự", "她把家务安排得有条不紊。", "Cô ấy sắp xếp việc nhà đâu ra đấy.",
     "Thành ngữ, nghĩa là có thứ tự, ngăn nắp, không rối loạn. 条 là thứ tự, 紊 là rối loạn. Thường làm trạng ngữ, như 有条不紊地进行, tiến hành một cách có trật tự."),
    ("展现", "zhǎnxiàn", "triển hiện", "động từ", "bày ra, thể hiện", "这部电影展现了农村的新面貌。", "Bộ phim này thể hiện diện mạo mới của nông thôn.",
     "Động từ, nghĩa là bày ra trước mắt, thể hiện rõ ra. Ví dụ 展现才华, thể hiện tài năng."),
    ("丛", "cóng", "tùng", "lượng từ", "bụi, khóm, chùm", "路边开着一丛丛野花。", "Ven đường nở những khóm hoa dại.",
     "Lượng từ, dùng cho cây cỏ, hoa mọc thành bụi, thành khóm. Lặp lại thành 一丛丛 để chỉ số nhiều, từng khóm từng khóm."),
    ("体积", "tǐjī", "thể tích", "danh từ", "thể tích, kích thước", "这个箱子体积太大，放不进车里。", "Cái thùng này kích thước quá to, không cho vào xe được.",
     "Danh từ, nghĩa là thể tích. Trong khẩu ngữ, 体积大 thường hiểu đơn giản là to, cồng kềnh."),
    ("造型", "zàoxíng", "tạo hình", "danh từ", "kiểu dáng, hình dáng", "这座建筑的造型很独特。", "Kiểu dáng của tòa nhà này rất độc đáo.",
     "Danh từ, nghĩa là hình dáng, kiểu dáng của một vật. Trong bài, 造型奇特的白蚌 là con trai trắng có hình dáng kỳ lạ."),
    ("迷惑", "míhuò", "mê hoặc", "tính từ", "mơ hồ, khó hiểu, hoang mang", "他的话让我感到很迷惑。", "Lời anh ấy nói làm tôi thấy rất khó hiểu.",
     "Tính từ, nghĩa là không hiểu rõ, mơ hồ, hoang mang. Cẩn thận: mê hoặc trong tiếng Việt là quyến rũ, làm say mê; còn 迷惑 chủ yếu là thấy khó hiểu. Trong bài, 迷惑不解 là khó hiểu, không lý giải được."),
    ("广阔", "guǎngkuò", "quảng khoát", "tính từ", "bao la, rộng lớn", "年轻人在这里有广阔的发展空间。", "Người trẻ ở đây có không gian phát triển rộng lớn.",
     "Tính từ, nghĩa là rộng lớn, bao la. Dùng cho không gian thật như biển, thảo nguyên, hoặc nghĩa bóng như 广阔的前景, triển vọng rộng mở."),
    ("奇妙", "qímiào", "kỳ diệu", "tính từ", "kỳ diệu, tuyệt diệu", "大自然真是太奇妙了！", "Thiên nhiên thật là kỳ diệu!",
     "Tính từ, nghĩa là kỳ diệu, hay đến mức khiến người ta ngạc nhiên thích thú. Âm Hán Việt giống hệt tiếng Việt."),
    ("基地", "jīdì", "cơ địa", "danh từ", "căn cứ, cơ sở", "这里是全国最大的蔬菜生产基地。", "Đây là cơ sở sản xuất rau lớn nhất cả nước.",
     "Danh từ, nghĩa là căn cứ, cơ sở để tiến hành một hoạt động: 军事基地, căn cứ quân sự; 研究基地, cơ sở nghiên cứu. Tiếng Việt không nói cơ địa theo nghĩa này, mà nói căn cứ hoặc cơ sở."),
]

add("bullets", chapter="Từ mới (46 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 19 có 46 từ mới, chia thành 16 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 场所 (chǎng) · 贝壳 (ké) · 细菌 (jūn) · 丧失 (sàng)",
           "Từ dễ nhầm: 认定 · 合成 · 超越 · 迷惑 · 基地"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có bốn mươi sáu từ, thầy chia thành mười sáu nhóm nhỏ, mỗi nhóm hai hoặc ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số từ có âm đọc cần chú ý, như 场所，贝壳，细菌，丧失. Thầy sẽ nhắc khi gặp."),
         F(4, "Ngoài ra, có mấy từ Hán Việt rất dễ hiểu nhầm, như 认定，合成，超越，迷惑，基地. Nghĩa của chúng trong tiếng Trung khác với tiếng Việt, các bạn nhớ nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

sizes = [3] * 14 + [2, 2]
assert sum(sizes) == len(V)
g = 0
for gs in sizes:
    group = V[g:g + gs]
    words, say = [], []
    for i, item in enumerate(group):
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
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung nếu khác])
P = [
    ("俗话说万物生长靠太阳。人们之所以这样说，是因为历来植物生长离不开阳光，而动物又靠植物维持生命，所以没有阳光，就没有万物，这是众所周知的真理。",
     "Tục ngữ nói vạn vật sinh trưởng nhờ mặt trời. Người ta sở dĩ nói như vậy là vì xưa nay thực vật sinh trưởng không thể thiếu ánh nắng, còn động vật lại dựa vào thực vật để duy trì sự sống, cho nên không có ánh nắng thì không có vạn vật, đây là chân lý mà ai cũng biết.",
     ["之所以……是因为…… nghĩa là sở dĩ… là vì…: nêu kết quả trước, rồi mới giải thích nguyên nhân. Đây là mẫu câu văn viết rất hay gặp.",
      "离不开 là không thể tách rời, không thể thiếu. 而 ở đây nối hai vế, nghĩa là còn, mà."]),
    ("然而科学家们的深海考察，却向人类早已认定为准则的定义提出了质疑。",
     "Thế nhưng, cuộc khảo sát biển sâu của các nhà khoa học lại đặt ra nghi vấn đối với định nghĩa mà loài người từ lâu đã coi là nguyên tắc.",
     ["然而……却…… là thế nhưng… lại…, báo hiệu một bước ngoặt. 考察 là khảo sát thực địa.",
      "向……提出质疑 là đặt ra nghi vấn với cái gì. 认定为准则 là coi là nguyên tắc, tin chắc là đúng."]),
    ("潜水到几千米深海底的科学家发现了一个繁殖生命的场所，那里的生物长相古怪，蛤、蚌、蟹、贝壳、红冠蠕虫等等，什么都有。",
     "Các nhà khoa học lặn xuống đáy biển sâu mấy nghìn mét đã phát hiện ra một nơi sự sống sinh sôi. Sinh vật ở đó có hình dạng kỳ dị: nghêu, trai, cua, sò ốc, giun ống mào đỏ, vân vân, cái gì cũng có.",
     ["Chủ ngữ của câu khá dài: 潜水到几千米深海底的科学家, các nhà khoa học lặn xuống đáy biển sâu mấy nghìn mét. Khi đọc câu dài, hãy tìm danh từ trung tâm trước.",
      "长相 là tướng mạo, hình dạng bên ngoài. 什么都有 là cái gì cũng có, nhấn mạnh sự phong phú."]),
    ("科学家深感诧异：在没有阳光，没有食物，压力又很大的海底，怎么会有这么多生物？它们靠什么生存呢？",
     "Các nhà khoa học vô cùng kinh ngạc: ở đáy biển không có ánh nắng, không có thức ăn, áp suất lại rất lớn, sao lại có nhiều sinh vật như vậy? Chúng dựa vào đâu để sinh tồn?",
     ["深感 là cảm thấy sâu sắc, vô cùng, thường đi với tính từ chỉ cảm xúc: 深感诧异，深感遗憾.",
      "Ba điều kiện khắc nghiệt được liệt kê liền nhau: không ánh nắng, không thức ăn, áp suất lớn. Hai câu hỏi cuối chính là vấn đề mà cả bài khóa sẽ trả lời."]),
    ("回到地面后，科学家取出从深海带回的样品，一股带有刺鼻臭蛋气味的硫化氢气体立即冲了出来，科学家恍然大悟，进而提出了这样的假说——",
     "Trở lại mặt đất, các nhà khoa học lấy mẫu vật mang về từ biển sâu ra, một luồng khí hydro sunfua có mùi trứng thối xộc vào mũi lập tức xông ra. Các nhà khoa học chợt hiểu ra, rồi từ đó đưa ra giả thuyết như sau:",
     ["硫化氢 là khí hydro sunfua, một loại khí không màu, dễ cháy, rất độc, có mùi trứng thối. 一股 là lượng từ cho mùi, luồng khí.",
      "进而提出了这样的假说 là rồi từ đó tiến tới đưa ra giả thuyết. Đây là điểm ngữ pháp 进而: trên cơ sở đã hiểu ra, tiến thêm một bước. 假说 là giả thuyết."],
     "回到地面后，科学家取出从深海带回的样品，一股带有刺鼻臭蛋气味的硫化氢气体立即冲了出来，科学家恍然大悟，进而提出了这样的假说。"),
    ("当海水从地壳分裂而成的裂缝渗透到地下时，在高温和高压的作用下，水里所含的硫酸盐转化成了硫化氢，某些细菌借硫化氢代谢变化，吸收温泉的热量得以繁殖。",
     "Khi nước biển thấm xuống lòng đất qua những khe nứt do vỏ trái đất tách ra, dưới tác dụng của nhiệt độ cao và áp suất cao, muối sunfat có trong nước chuyển hóa thành hydro sunfua; một số vi khuẩn nhờ quá trình trao đổi chất với hydro sunfua, hấp thụ nhiệt lượng của suối nước nóng mà có thể sinh sôi.",
     ["当……时 là khi…; 在……的作用下 là dưới tác dụng của…. 硫酸盐 là muối sunfat. 代谢 là trao đổi chất.",
      "借……得以繁殖 là nhờ vào… mà có thể sinh sôi. Đây là điểm ngữ pháp 得以: phía trước nêu điều kiện, phía sau là kết quả đạt được."]),
    ("一些小动物靠过滤细菌维持生命，而小动物又成了大动物的食物来源，这样，就构成了一个新的“食物链”。",
     "Một số động vật nhỏ sống nhờ lọc vi khuẩn, còn động vật nhỏ lại trở thành nguồn thức ăn của động vật lớn. Như vậy đã tạo thành một chuỗi thức ăn mới.",
     ["食物链 là chuỗi thức ăn. 构成 là cấu thành, tạo thành.",
      "Chuỗi thức ăn ở đây là: vi khuẩn, rồi động vật nhỏ, rồi động vật lớn. Khác với trên mặt đất, mắt xích đầu tiên không phải là thực vật cần ánh nắng."],
     "一些小动物靠过滤细菌维持生命，而小动物又成了大动物的食物来源，这样，就构成了一个新的食物链。"),
    ("它们靠来自地球内部的热能维持生命，这种程序叫“化学合成”，是生物科学史上的第一次发现。",
     "Chúng duy trì sự sống nhờ nhiệt năng đến từ lòng trái đất. Quá trình này gọi là hóa tổng hợp, là phát hiện đầu tiên trong lịch sử khoa học sinh vật.",
     ["来自 là đến từ, văn viết. 热能 là nhiệt năng. 程序 ở đây là quá trình, trình tự.",
      "化学合成 là hóa tổng hợp, ngược với 光合作用, quang hợp, của thực vật cần ánh sáng mặt trời."],
     "它们靠来自地球内部的热能维持生命，这种程序叫化学合成，是生物科学史上的第一次发现。"),
    ("它告诉人类，在没有阳光的条件下，也可能有生命；它启发人们，要解放思想，迈向地球以外，探索生命存在的新路。",
     "Nó cho loài người biết rằng, trong điều kiện không có ánh nắng cũng có thể có sự sống; nó gợi mở cho con người phải giải phóng tư tưởng, tiến ra ngoài trái đất, tìm tòi con đường mới cho sự tồn tại của sự sống.",
     ["Hai vế song song: 它告诉人类…… và 它启发人们……, nối bằng dấu chấm phẩy. 启发 là gợi mở, khơi gợi.",
      "解放思想 là giải phóng tư tưởng, không bó buộc vào chân lý cũ. 迈向地球以外 là tiến ra ngoài trái đất."]),
    ("据悉，这种细菌忍受高温的本领远远超越了我们的想象，它们能在250摄氏度（250℃）的环境下生存。",
     "Được biết, khả năng chịu nhiệt độ cao của loại vi khuẩn này vượt xa sức tưởng tượng của chúng ta, chúng có thể sống trong môi trường hai trăm năm mươi độ C.",
     ["据悉 đứng đầu câu, nghĩa là theo nguồn tin được biết. 本领 là bản lĩnh, khả năng.",
      "远远超越了我们的想象 là vượt xa sức tưởng tượng của chúng ta. 远远 nhấn mạnh mức độ chênh lệch rất lớn."],
     "据悉，这种细菌忍受高温的本领远远超越了我们的想象，它们能在二百五十摄氏度的环境下生存。"),
    ("一般情况下，高于40℃，大部分植物和动物就无法成活；高于65℃，多数细菌会丧失生命，可是，为什么偏偏这种细菌能够存活下来？其中的奥秘到底是什么呢？",
     "Trong tình huống bình thường, trên bốn mươi độ C, phần lớn thực vật và động vật không thể sống được; trên sáu mươi lăm độ C, đa số vi khuẩn sẽ chết. Thế nhưng, vì sao riêng loại vi khuẩn này lại sống sót được? Bí ẩn trong đó rốt cuộc là gì?",
     ["高于 là cao hơn, văn viết. 成活 là sống được, sống sót. 存活下来 là sống sót lại.",
      "偏偏 ở đây là sự thật trái với lẽ thường: các loài khác đều chết, riêng loại vi khuẩn này lại sống. Đây là điểm ngữ pháp 偏偏. 奥秘 là bí ẩn sâu xa."],
     "一般情况下，高于四十摄氏度，大部分植物和动物就无法成活；高于六十五摄氏度，多数细菌会丧失生命，可是，为什么偏偏这种细菌能够存活下来？其中的奥秘到底是什么呢？"),
    ("有人迫不及待地想探究其真相，有人却说，与其把精力用来探索耐高温细菌生命存在的秘密，不如去探索高温和高压下的金星或其他星球上，是否也有生物存在。",
     "Có người nóng lòng muốn tìm hiểu sự thật, nhưng có người lại nói, thay vì dồn sức khám phá bí mật tồn tại của vi khuẩn chịu nhiệt, chi bằng đi khám phá xem trên sao Kim với nhiệt độ cao và áp suất cao, hay trên các hành tinh khác, có sinh vật tồn tại hay không.",
     ["其 là đại từ văn viết, nghĩa là của nó: 探究其真相, tìm hiểu sự thật của nó. 迫不及待 là nóng lòng, các bạn đã học ở bài năm.",
      "与其……不如…… nghĩa là thay vì… chi bằng…. 金星 là sao Kim, hành tinh thứ hai tính từ mặt trời. 是否 là có… hay không."]),
    ("不管人类怎么想，这些深海生物依然保持着它们强大而华丽的阵容，有条不紊地过着自己的日子，展现着他们独特的精彩：",
     "Dù con người nghĩ thế nào, những sinh vật biển sâu này vẫn giữ đội hình hùng hậu và lộng lẫy của chúng, ngăn nắp sống cuộc sống của riêng mình, phô bày vẻ đặc sắc độc đáo của chúng:",
     ["不管……都/依然…… là dù… thì vẫn…. 依然 là vẫn, vẫn như cũ.",
      "Tác giả dùng phép nhân hóa: 过着自己的日子, sống cuộc sống của mình, như thể sinh vật biển sâu cũng là con người. 有条不紊地 làm trạng ngữ."]),
    ("一丛丛红冠蠕虫，把白色外套管固定在岩石上，保护着自己柔软的身体。",
     "Từng cụm giun ống mào đỏ gắn chặt lớp ống bọc màu trắng bên ngoài lên vách đá, bảo vệ cơ thể mềm mại của mình.",
     ["一丛丛 là từng cụm từng cụm. 外套管 là lớp ống bọc bên ngoài, giống như chiếc áo khoác của loài giun.",
      "把……固定在…… là câu chữ 把: gắn chặt cái gì vào đâu. 柔软 là mềm mại."]),
    ("它们没有嘴，没有眼，甚至消化系统也不存在，仅靠伸出套管顶端的身体过滤海水中的食物，它们是怎么繁殖后代的呢？",
     "Chúng không có miệng, không có mắt, thậm chí cả hệ tiêu hóa cũng không có, chỉ dựa vào phần cơ thể thò ra ở đầu ống để lọc thức ăn trong nước biển. Vậy chúng sinh sản đời sau bằng cách nào?",
     ["甚至……也…… là thậm chí… cũng…, đẩy mức độ lên cao nhất. 仅靠 là chỉ dựa vào, văn viết.",
      "伸出套管顶端的身体 là phần cơ thể thò ra khỏi đầu ống. 后代 là đời sau, con cháu."]),
    ("体积庞大的巨蛤，造型奇特的白蚌，它们的生理结构，食物基础，甚至它们的门类归属，都使人迷惑不解。",
     "Loài nghêu khổng lồ có kích thước to lớn, loài trai trắng có hình dáng kỳ lạ, cấu tạo sinh lý, nguồn thức ăn, thậm chí cả việc chúng thuộc ngành loài nào, đều khiến người ta không sao hiểu nổi.",
     ["庞大 là to lớn, đồ sộ. 门类归属 là thuộc về ngành, loại nào trong phân loại sinh vật.",
      "使人迷惑不解 là khiến người ta khó hiểu, không lý giải được. 使 cộng người cộng trạng thái là làm cho ai đó thế nào."]),
    ("这片神秘而广阔的深海世界能为我们提供新的食物资源，成为奇妙的科学研究基地吗？",
     "Thế giới biển sâu bí ẩn và bao la này liệu có thể cung cấp cho chúng ta nguồn thực phẩm mới, trở thành một căn cứ nghiên cứu khoa học kỳ diệu không?",
     ["片 là lượng từ cho vùng rộng lớn: 一片海，这片世界. 神秘而广阔 là bí ẩn mà bao la, 而 nối hai tính từ.",
      "Bài kết thúc bằng một câu hỏi mở, để lại cho người đọc sự tò mò về thế giới chưa được khám phá."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 无阳光的深海世界", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 无阳光的深海世界, dài tám trăm chín mươi hai chữ. Bài được cải biên từ bài viết 无阳光世界的深海生命 trong cuốn sách 神奇动植物之谜, Bí ẩn của động thực vật kỳ diệu.",
         F(0, "Thầy chia bài thành mười bảy đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng. Bài này có khá nhiều thuật ngữ khoa học, các bạn đừng lo, thầy sẽ giải thích từng từ."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 100 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Tóm tắt nội dung", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5) – phần 1", size=34,
    items=["## 1. 为什么说万物生长靠太阳？",
           "植物生长离不开阳光 · 动物又靠植物维持生命",
           "## 2. 几千米深的海底有生物吗？",
           "科学家发现了一个繁殖生命的场所 · 那里的生物长相古怪，蛤、蚌、蟹、贝壳、红冠蠕虫等等，什么都有",
           "## 3. 深海的生物靠什么生存？",
           "假说：当海水渗透到地下时，在高温和高压的作用下，硫酸盐转化成了硫化氢，某些细菌借硫化氢代谢变化，吸收温泉的热量得以繁殖"],
    say=["Bài tập năm của sách yêu cầu dựa vào gợi ý để tóm tắt nội dung chính của bài khóa. Chúng ta cùng làm luôn nhé.",
         F(0, "Câu hỏi một: vì sao nói vạn vật sinh trưởng nhờ mặt trời?"),
         F(1, "Vì 植物生长离不开阳光, thực vật sinh trưởng không thể thiếu ánh nắng; và 动物又靠植物维持生命, động vật lại dựa vào thực vật để duy trì sự sống."),
         F(2, "Câu hỏi hai: dưới đáy biển sâu mấy nghìn mét có sinh vật không?"),
         F(3, "Có. Các nhà khoa học đã phát hiện một nơi sự sống sinh sôi, sinh vật ở đó có hình dạng kỳ dị: nghêu, trai, cua, sò ốc, giun ống mào đỏ, cái gì cũng có."),
         F(4, "Câu hỏi ba: sinh vật biển sâu sống nhờ vào đâu?"),
         F(5, "Theo giả thuyết: khi nước biển thấm xuống lòng đất, dưới tác dụng của nhiệt độ cao và áp suất cao, muối sunfat chuyển hóa thành hydro sunfua; một số vi khuẩn nhờ trao đổi chất với hydro sunfua, hấp thụ nhiệt của suối nước nóng mà sinh sôi. Sau đó động vật nhỏ ăn vi khuẩn, động vật lớn ăn động vật nhỏ.")])

add("bullets", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5) – phần 2", size=34,
    items=["## 4. 描述一下深海耐高温细菌忍受高温的本领",
           "这种细菌能在250℃的环境下生存 · 大部分植物和动物：高于40℃就无法成活 · 多数细菌：高于65℃会丧失生命",
           "## 5. 深海中的生物还有什么使人迷惑不解的问题？",
           "红冠蠕虫：没有嘴，没有眼，没有消化系统，它们是怎么繁殖后代的？",
           "巨蛤、白蚌：它们的生理结构、食物基础、门类归属，都使人迷惑不解"],
    say=[F(0, "Câu hỏi bốn: hãy miêu tả khả năng chịu nhiệt của loại vi khuẩn biển sâu."),
         F(1, "Loại vi khuẩn này có thể sống trong môi trường hai trăm năm mươi độ C. Trong khi đó, trên bốn mươi độ C, phần lớn thực vật và động vật không sống được; trên sáu mươi lăm độ C, đa số vi khuẩn sẽ chết."),
         F(2, "Câu hỏi năm: sinh vật biển sâu còn những vấn đề gì khiến người ta khó hiểu?"),
         F(3, "Thứ nhất là loài giun ống mào đỏ: không có miệng, không có mắt, không có hệ tiêu hóa, vậy chúng sinh sản bằng cách nào?"),
         F(4, "Thứ hai là loài nghêu khổng lồ và trai trắng: cấu tạo sinh lý, nguồn thức ăn, và chúng thuộc ngành loài nào, đều còn là bí ẩn. Bố cục này rất có ích khi các bạn làm bài tập viết ở cuối bài.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 进而", section="Ngữ pháp 注释", title="1. 进而 jìn'ér – rồi tiến thêm, từ đó tiến tới", size=36,
    items=["Liên từ, dùng ở vế sau: trên cơ sở đã có, tiến thêm một bước · dùng trong văn viết",
           "人是在改造环境的实践中认识环境并接受环境的影响，进而改造自己的。",
           "想象有减轻心理压力，维持心理平衡，进而促进心理健康的作用。",
           "……科学家恍然大悟，进而提出了这样的假说——当海水从地壳分裂而成的裂缝渗透到地下时……"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là liên từ 进而.",
         F(0, "进而 là liên từ, dùng ở đầu vế câu phía sau, biểu thị trên cơ sở điều đã có ở vế trước, tiến thêm một bước nữa. Tiếng Việt dịch là rồi tiến tới, rồi từ đó. Từ này dùng trong văn viết."),
         F(1, "Ví dụ một: 人是在改造环境的实践中认识环境并接受环境的影响，进而改造自己的。 Con người nhận thức môi trường và chịu ảnh hưởng của môi trường trong thực tiễn cải tạo môi trường, rồi từ đó cải tạo chính mình."),
         F(2, "Ví dụ hai: 想象是维持儿童心理健康的重要手段。想象有减轻心理压力，维持心理平衡，进而促进心理健康的作用。 Trí tưởng tượng là phương tiện quan trọng giúp duy trì sức khỏe tâm lý của trẻ. Nó có tác dụng giảm áp lực tâm lý, duy trì cân bằng tâm lý, rồi từ đó thúc đẩy sức khỏe tâm lý."),
         F(3, "Ví dụ ba, lấy từ bài khóa: 科学家恍然大悟，进而提出了这样的假说。 Các nhà khoa học chợt hiểu ra, rồi từ đó đưa ra giả thuyết. Các bạn thấy đấy: bước một là hiểu ra, bước hai cao hơn là đưa ra giả thuyết. Hai bước có quan hệ tăng tiến, bước sau dựa trên bước trước.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: dùng 进而 viết lại câu", reveal=True, size=36,
    items=["(1) 新的教学方法要先在个别班级进行实验，之后在全校推广。",
           "Đáp án: 新的教学方法要先在个别班级进行实验，进而在全校推广。",
           "(2) 要先把原著表达的思想弄清楚，在此基础上，很好地去理解原著。",
           "Đáp án: 要先把原著表达的思想弄清楚，进而很好地去理解原著。",
           "(3) 据说，著名画家齐白石画虾数十年，到了七十岁时赶上了古人的水平，后来继续努力，超越了古人。",
           "Đáp án: ……到了七十岁时赶上了古人的水平，进而超越了古人。"],
    say=[F(0, "Luyện tập: dùng 进而 viết lại câu. Câu một: 新的教学方法要先在个别班级进行实验，之后在全校推广。 Phương pháp dạy học mới phải thử nghiệm trước ở một vài lớp, sau đó mới mở rộng ra toàn trường. Các bạn tạm dừng và thử viết lại nhé."),
         F(1, "Đáp án: thay 之后 bằng 进而: 新的教学方法要先在个别班级进行实验，进而在全校推广。 Thử nghiệm ở vài lớp trước, rồi từ đó mở rộng ra toàn trường."),
         F(2, "Câu hai: 要先把原著表达的思想弄清楚，在此基础上，很好地去理解原著。 Trước hết phải làm rõ tư tưởng mà nguyên tác thể hiện, trên cơ sở đó mới hiểu thấu nguyên tác."),
         F(3, "Đáp án: cụm 在此基础上, trên cơ sở đó, chính là nghĩa của 进而. Viết lại: 要先把原著表达的思想弄清楚，进而很好地去理解原著。"),
         F(4, "Câu ba: 据说，著名画家齐白石画虾数十年，到了七十岁时赶上了古人的水平，后来继续努力，超越了古人。 Nghe nói, danh họa Tề Bạch Thạch vẽ tôm mấy chục năm, đến bảy mươi tuổi thì đuổi kịp trình độ của người xưa, sau đó tiếp tục cố gắng, vượt qua cả người xưa."),
         F(5, "Đáp án: 到了七十岁时赶上了古人的水平，进而超越了古人。 Đuổi kịp người xưa, rồi tiến thêm một bước là vượt qua người xưa. Đây là ví dụ rất rõ về quan hệ tăng tiến của 进而.")])

add("bullets", chapter="Ngữ pháp: 得以", section="Ngữ pháp 注释", title="2. 得以 déyǐ – nhờ đó mà có thể", size=36,
    items=["Động từ: nhờ đó mà đạt được, nhờ đó mà có thể; có thể · dùng trong văn viết",
           "Phía trước thường nêu điều kiện; phía sau là kết quả đã thực hiện hoặc kết quả mong đợi",
           "Thường đi với động từ, cụm động từ; ít đi với cụm tính từ",
           "……某些细菌借硫化氢代谢变化，吸收温泉的热量得以繁殖。",
           "……使他明白，只有自首，才是他和家人得以解脱的唯一途径。",
           "幸亏列车上有位经验丰富的医生，使他得以清醒过来。"],
    say=["Điểm ngữ pháp thứ hai là động từ 得以.",
         F(0, "得以 là động từ, nghĩa là nhờ vào đó mà đạt được, nhờ đó mà có thể. Từ này dùng trong văn viết."),
         F(1, "Ở phía trước, ngữ cảnh thường nêu ra điều kiện giúp sự việc xảy ra. Phía sau 得以 thường là kết quả đã thực hiện được, cũng có thể là kết quả mong đợi."),
         F(2, "得以 thường bổ nghĩa cho động từ hoặc cụm động từ, rất ít khi đi với cụm tính từ."),
         F(3, "Ví dụ một, lấy từ bài khóa: 在高温和高压的作用下，水里所含的硫酸盐转化成了硫化氢，某些细菌借硫化氢代谢变化，吸收温泉的热量得以繁殖。 Điều kiện là trao đổi chất và hấp thụ nhiệt, kết quả là vi khuẩn sinh sôi được."),
         F(4, "Ví dụ hai: 警察用最简单易懂的语言，把自首和逃跑的两种结果分析给他听，使他明白，只有自首，才是他和家人得以解脱的唯一途径。 Cảnh sát dùng lời lẽ đơn giản dễ hiểu nhất, phân tích cho anh ta nghe hai kết quả của tự thú và bỏ trốn, làm anh ta hiểu rằng chỉ có tự thú mới là con đường duy nhất để anh ta và gia đình được giải thoát."),
         F(5, "Ví dụ ba: 幸亏列车上有位经验丰富的医生，使他得以清醒过来。 May mà trên tàu có một bác sĩ giàu kinh nghiệm, nhờ đó anh ấy mới tỉnh lại được.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: dùng 得以 viết lại câu", reveal=True, size=36,
    items=["(1) 长寿的一生使他有机会见证中国历史上的伟大年代。",
           "Đáp án: 长寿的一生使他得以见证中国历史上的伟大年代。",
           "(2) 大机器代替了手工工场，科学技术在生产上才能广泛运用。",
           "Đáp án: 大机器代替了手工工场，科学技术在生产上才得以广泛运用。",
           "(3) 这个联欢会，希望孩子们能唱的唱，能跳的跳，能写的写，能画的画，就是要让所有孩子的特长都能够发挥出来。",
           "Đáp án: ……就是要让所有孩子的特长都得以发挥出来。"],
    say=[F(0, "Luyện tập: dùng 得以 viết lại câu. Câu một: 长寿的一生使他有机会见证中国历史上的伟大年代。 Cuộc đời trường thọ giúp ông có cơ hội chứng kiến thời đại vĩ đại trong lịch sử Trung Quốc. Các bạn tạm dừng và thử viết lại nhé."),
         F(1, "Đáp án: thay 有机会 bằng 得以: 长寿的一生使他得以见证中国历史上的伟大年代。 Nhờ sống lâu mà ông được chứng kiến thời đại vĩ đại ấy."),
         F(2, "Câu hai: 大机器代替了手工工场，科学技术在生产上才能广泛运用。 Máy móc lớn thay thế công trường thủ công, khoa học kỹ thuật mới có thể được ứng dụng rộng rãi trong sản xuất."),
         F(3, "Đáp án: thay 才能 bằng 才得以: 科学技术在生产上才得以广泛运用。 Điều kiện là máy móc thay thế lao động thủ công, kết quả là khoa học kỹ thuật được ứng dụng rộng rãi."),
         F(4, "Câu ba: 这个联欢会，希望孩子们能唱的唱，能跳的跳，能写的写，能画的画，就是要让所有孩子的特长都能够发挥出来。 Buổi liên hoan này mong các em, ai hát được thì hát, ai múa được thì múa, ai viết được thì viết, ai vẽ được thì vẽ, chính là để năng khiếu của mọi em đều được phát huy."),
         F(5, "Đáp án: thay 能够 bằng 得以: 就是要让所有孩子的特长都得以发挥出来。 Đây là kết quả mong đợi, đúng như sách nói: sau 得以 cũng có thể là kết quả mong muốn đạt được.")])

add("bullets", chapter="Ngữ pháp: 偏偏", section="Ngữ pháp 注释", title="3. 偏偏 piānpiān – lại cứ, cố tình; trái lại", size=34,
    items=["## (1) Chủ quan cố tình làm trái yêu cầu hay tình hình khách quan – hay đi với 要、不",
           "那里太危险了，大家都劝他不要去，他偏偏要去。",
           "我爱做的事，偏偏不让我做；我不爱做的事，倒非做不可，真让人生气！",
           "## (2) Sự thật trái ngược hẳn với mong muốn, yêu cầu hay lẽ thường",
           "30年前我们班那个最不爱说话、最不起眼儿的女生，今天偏偏最成功。",
           "高于40℃，大部分植物和动物就无法成活；高于65℃，多数细菌会丧失生命，可是，为什么偏偏这种细菌能够存活下来？"],
    say=["Điểm ngữ pháp thứ ba là phó từ 偏偏. Từ này có hai cách dùng chính.",
         F(0, "Cách dùng thứ nhất: biểu thị về mặt chủ quan, người ta cố tình làm ngược lại với yêu cầu hay tình hình khách quan. Tiếng Việt dịch là cứ nhất định, lại cứ. Thường đi cùng 要 hoặc 不."),
         F(1, "Ví dụ một: 那里太危险了，大家都劝他不要去，他偏偏要去。 Chỗ đó nguy hiểm quá, mọi người đều khuyên anh ấy đừng đi, vậy mà anh ấy cứ nhất định muốn đi."),
         F(2, "Ví dụ hai: 我爱做的事，偏偏不让我做；我不爱做的事，倒非做不可，真让人生气！ Việc tôi thích làm thì cứ không cho tôi làm; việc tôi không thích thì lại bắt buộc phải làm, thật là bực mình!"),
         F(3, "Cách dùng thứ hai: biểu thị sự thật trái ngược hẳn với một mong muốn, yêu cầu, hay lẽ thường nào đó. Tiếng Việt dịch là lại, trái lại, riêng."),
         F(4, "Ví dụ ba: 三十年前我们班那个最不爱说话、最不起眼儿的女生，今天偏偏最成功。 Ba mươi năm trước, cô bạn ít nói nhất, mờ nhạt nhất lớp tôi, thì nay lại là người thành công nhất. Theo lẽ thường thì khó ai nghĩ cô ấy sẽ thành công nhất."),
         F(5, "Ví dụ bốn, lấy từ bài khóa: 高于四十摄氏度，大部分植物和动物就无法成活；高于六十五摄氏度，多数细菌会丧失生命，可是，为什么偏偏这种细菌能够存活下来？ Các loài khác đều chết, riêng loại vi khuẩn này lại sống được, trái với lẽ thường.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: hoàn thành câu với 偏偏", reveal=True, size=38,
    items=["(1) 他从小就喜欢画画儿，也有绘画的天赋，没想到……",
           "Đáp án: ……没想到父母偏偏让他学医。",
           "(2) 去南方旅游的火车票也买了，旅馆也订了，……",
           "Đáp án: ……偏偏这时候公司让我去出差。",
           "(3) 跟他说好有急事要联系，可他……",
           "Đáp án: ……可他偏偏把手机关了。"],
    say=[F(0, "Luyện tập: hoàn thành câu với 偏偏. Câu một: 他从小就喜欢画画儿，也有绘画的天赋，没想到…… Từ nhỏ cậu ấy đã thích vẽ, lại có năng khiếu hội họa, không ngờ thế nào? Các bạn tạm dừng và thử hoàn thành câu nhé."),
         F(1, "Đáp án gợi ý: 没想到父母偏偏让他学医。 Không ngờ bố mẹ lại cứ bắt cậu ấy học y. Đây là cách dùng thứ nhất: người khác cố tình làm trái với mong muốn của cậu ấy."),
         F(2, "Câu hai: 去南方旅游的火车票也买了，旅馆也订了，…… Vé tàu đi du lịch phương Nam đã mua, khách sạn cũng đặt rồi, thì sao?"),
         F(3, "Đáp án gợi ý: 偏偏这时候公司让我去出差。 Đúng lúc này công ty lại bắt tôi đi công tác. Đây là cách dùng thứ hai: sự thật trái với mong muốn."),
         F(4, "Câu ba: 跟他说好有急事要联系，可他…… Đã hẹn với anh ấy là có việc gấp thì liên lạc, vậy mà anh ấy thì sao?"),
         F(5, "Đáp án gợi ý: 可他偏偏把手机关了。 Vậy mà anh ấy lại tắt điện thoại. Các bạn để ý, 偏偏 luôn mang chút cảm giác bất mãn, không vừa ý của người nói.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 历来 – 从来", section="Phân biệt từ 词语辨析", title="Phân biệt 历来 và 从来 (1): câu phủ định",
    common="Giống nhau: đều là phó từ, chỉ từ xưa đến nay đều như vậy. Ví dụ: 我跟他下棋历来/从来都要输的。",
    cols=[{"head": "历来",
           "lines": ["Chủ yếu dùng trong văn viết, không dùng trong câu phủ định",
                     "Đúng: 我们历来提倡艰苦朴素，反对铺张浪费。"]},
          {"head": "从来",
           "lines": ["Chủ yếu dùng trong câu phủ định",
                     "Đúng: 我从来不隐瞒自己的观点。",
                     "Sai: 我历来不隐瞒自己的观点。"]}],
    say=["Tiếp theo là phần phân biệt từ: 历来 và 从来. Hai từ này đều dịch là xưa nay, từ trước đến giờ, nên người học rất hay dùng lẫn lộn.",
         "Điểm giống nhau: cả hai đều là phó từ, biểu thị từ quá khứ đến hiện tại đều như vậy. Ví dụ: 我跟他下棋历来都要输的, hoặc 从来都要输的, đều đúng. Tôi chơi cờ với anh ấy xưa nay toàn thua.",
         F(0, "Điểm khác thứ nhất. 历来 chủ yếu dùng trong văn viết, và không dùng trong câu phủ định. Ví dụ: 我们历来提倡艰苦朴素，反对铺张浪费。 Chúng tôi xưa nay luôn đề cao lối sống giản dị chịu khó, phản đối phô trương lãng phí."),
         F(1, "Còn 从来 thì chủ yếu dùng trong câu phủ định, như 从来不，从来没. Ví dụ: 我从来不隐瞒自己的观点。 Tôi trước giờ chưa bao giờ giấu quan điểm của mình."),
         F(1, "Vì vậy, câu 我历来不隐瞒自己的观点 là không tự nhiên. Khi câu có 不 hoặc 没, các bạn hãy dùng 从来."),
         "Mẹo nhớ: 从来不，从来没 là cụm rất quen thuộc trong khẩu ngữ; còn 历来 thì mang màu sắc trang trọng, hay gặp trong văn bản, báo chí."])

add("compare", section="Phân biệt từ 词语辨析", title="Phân biệt 历来 và 从来 (2): câu khẳng định",
    cols=[{"head": "历来",
           "lines": ["Có thể bổ nghĩa cho một động từ hay tính từ hai âm tiết đứng một mình",
                     "Đúng: 这个人历来忠厚老实，可以信赖。"]},
          {"head": "从来",
           "lines": ["Trong câu khẳng định: bổ nghĩa cho cụm động từ, cụm tính từ hoặc phân câu; thường không đi với một động từ, tính từ đứng một mình",
                     "Đúng: 川西平原从来就是物产丰富。"]}],
    say=[F(0, "Điểm khác thứ hai. 历来 có thể bổ nghĩa cho một động từ hoặc tính từ hai âm tiết đứng một mình. Ví dụ: 这个人历来忠厚老实，可以信赖。 Người này xưa nay vốn trung hậu thật thà, có thể tin cậy được."),
         F(1, "Còn 从来, khi dùng trong câu khẳng định, thì bổ nghĩa cho cụm động từ, cụm tính từ hoặc cả một phân câu, thường không bổ nghĩa cho một động từ hay tính từ đứng trơ trọi. Ví dụ: 川西平原从来就是物产丰富。 Đồng bằng phía tây Tứ Xuyên xưa nay vốn sản vật phong phú."),
         F(1, "Các bạn để ý: trong câu khẳng định, 从来 thường đi kèm 就 hoặc 都, như 从来就是，从来都是, để câu tự nhiên hơn."),
         "Tóm lại: câu phủ định thì dùng 从来; văn viết, câu khẳng định với một từ hai âm tiết đứng một mình thì dùng 历来."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: chọn 历来 hay 从来 điền vào chỗ trống", reveal=True, size=38,
    items=["(1) 爷爷___没有浪费过一点儿粮食。",
           "Đáp án: 从来 – câu phủ định (没有)",
           "(2) 中国西北地区雨量___稀少。",
           "Đáp án: 历来 – bổ nghĩa cho tính từ hai âm tiết 稀少",
           "(3) 他___心直口快，有什么说什么。",
           "Đáp án: 历来 – câu khẳng định (cũng có thể nói 从来就)",
           "(4) 她总是无忧无虑，好像___不知道什么叫烦恼。",
           "Đáp án: 从来 – câu phủ định (不知道)"],
    say=[F(0, "Bây giờ chúng ta làm thử: chọn 历来 hoặc 从来 điền vào chỗ trống. Câu một: 爷爷什么没有浪费过一点儿粮食。 Ông nội chưa từng lãng phí một chút lương thực nào. Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: 从来. Câu có 没有, là câu phủ định, nên dùng 从来: 爷爷从来没有浪费过一点儿粮食。"),
         F(2, "Câu hai: 中国西北地区雨量什么稀少。 Vùng tây bắc Trung Quốc lượng mưa xưa nay vẫn ít."),
         F(3, "Đáp án: 历来. 稀少 là tính từ hai âm tiết đứng một mình, nên dùng 历来: 中国西北地区雨量历来稀少。"),
         F(4, "Câu ba: 他什么心直口快，有什么说什么。 Anh ấy xưa nay tính thẳng thắn, có gì nói nấy."),
         F(5, "Đáp án: 历来: 他历来心直口快。 Đây là câu khẳng định, mang màu sắc nhận xét trang trọng. Nếu muốn dùng 从来, nên thêm 就: 他从来就心直口快。"),
         F(6, "Câu bốn: 她总是无忧无虑，好像什么不知道什么叫烦恼。 Cô ấy lúc nào cũng vô tư, dường như chưa bao giờ biết phiền não là gì."),
         F(7, "Đáp án: 从来. Câu có 不知道, là câu phủ định: 好像从来不知道什么叫烦恼。")])

# ======================= MỞ RỘNG: CÂU MƠ HỒ =======================
add("bullets", chapter="Mở rộng: câu mơ hồ (歧义句)", section="Mở rộng 扩展", title="Câu sai: câu mơ hồ về nghĩa (歧义句)", size=34,
    items=["Một câu bình thường chỉ diễn đạt một ý; nếu hiểu được theo hai cách trở lên → 歧义句",
           "## (1) Từ có hai từ loại: 前 là phương vị từ hay động từ?",
           "Sai: 上面通知说，让您本周五前去汇报。",
           "Cách hiểu 1: trước thứ Sáu (前 = 之前) · Cách hiểu 2: thứ Sáu đi đến (前去 = 前往)",
           "Sửa: ……让您本周五以前去汇报。/ ……让您本周五去汇报。"],
    say=["Bây giờ chúng ta sang phần mở rộng của sách. Quyển Thượng không có mục tu từ riêng, thay vào đó là kỹ năng nhận biết câu sai. Hôm nay là loại câu sai do mơ hồ về nghĩa, tiếng Trung gọi là 歧义句. Hán Việt là kỳ nghĩa, tức là nghĩa rẽ thành nhiều nhánh.",
         F(0, "Trong tình huống bình thường, một câu chỉ diễn đạt một ý. Nếu một câu có thể hiểu theo hai cách hoặc nhiều hơn, thì đó là câu mơ hồ, 歧义句. Sách đưa ra năm ví dụ."),
         F(1, "Ví dụ một: một từ có thể thuộc hai từ loại khác nhau."),
         F(2, "Câu sai: 上面通知说，让您本周五前去汇报。 Cấp trên thông báo, mời anh thứ Sáu tuần này đi báo cáo."),
         F(3, "Nếu 前 là phương vị từ, nghĩa là trước thứ Sáu. Nếu 前 là động từ, đi cùng 去 thành 前去, nghĩa là đi đến, tức là đúng ngày thứ Sáu thì đi báo cáo. Hai cách hiểu khác hẳn nhau về thời gian."),
         F(4, "Cách sửa: nếu muốn nói trước thứ Sáu thì viết 让您本周五以前去汇报。 Nếu muốn nói đúng thứ Sáu thì viết 让您本周五去汇报。")])

add("bullets", section="Mở rộng 扩展", title="Ví dụ câu mơ hồ (2)", size=34,
    items=["## (2) Động từ có hai chiều: 租 là thuê hay cho thuê?",
           "Sai: 那时候我们同在一个城市，我还租了他一套房子呢。",
           "Sửa: ……我还跟他租了一套房子呢。/ ……我还租给了他一套房子呢。",
           "## (3) Phạm vi bổ nghĩa của định ngữ: 几个 bổ nghĩa cho ai?",
           "Sai: 几个海归投资的垃圾发电厂很快将要建成投产。",
           "Sửa: 几个海归投资的一座垃圾发电厂…… / 海归投资的几个垃圾发电厂……"],
    say=[F(0, "Ví dụ hai: động từ mang hai chiều nghĩa, vừa là nhận vào, vừa là cho đi."),
         F(1, "Câu sai: 那时候我们同在一个城市，我还租了他一套房子呢。 Hồi đó chúng tôi cùng ở một thành phố, tôi còn thuê một căn nhà của anh ấy nữa cơ."),
         F(2, "Động từ 租 vừa có nghĩa là thuê, vừa có nghĩa là cho thuê. Nên câu này có thể hiểu là tôi thuê nhà của anh ấy, hoặc tôi cho anh ấy thuê nhà. Cách sửa: 我还跟他租了一套房子呢, tôi thuê nhà của anh ấy; hoặc 我还租给了他一套房子呢, tôi cho anh ấy thuê nhà."),
         F(3, "Ví dụ ba: phạm vi bổ nghĩa của định ngữ không rõ ràng."),
         F(4, "Câu sai: 几个海归投资的垃圾发电厂很快将要建成投产。 Nhà máy điện rác do mấy người du học về nước đầu tư sắp xây xong và đi vào sản xuất. 海归 là người đi du học về nước."),
         F(5, "Định ngữ 几个 có thể bổ nghĩa cho 海归, tức là mấy người đầu tư; cũng có thể bổ nghĩa cho 垃圾发电厂, tức là có mấy nhà máy. Cách sửa: 几个海归投资的一座垃圾发电厂, một nhà máy do mấy người đầu tư; hoặc 海归投资的几个垃圾发电厂, mấy nhà máy.")])

add("bullets", section="Mở rộng 扩展", title="Ví dụ câu mơ hồ (3): ngắt nhịp khác nhau", size=34,
    items=["## (4) 医生看到我们非常焦急，连忙把病人的病情告诉我们。",
           "医生看到 / 我们非常焦急 (chúng tôi lo) · 医生看到我们 / 非常焦急 (bác sĩ lo)",
           "Sửa: 医生看到我们非常焦急的样子，…… / 医生非常焦急，看到我们，……",
           "## (5) 我们打败了师大女篮得到了冠军。",
           "我们打败了师大女篮 / 得到了冠军 · 我们打败了 / 师大女篮得到了冠军",
           "Sửa: 我们打败了师大女篮，得到了冠军。/ 我们打败了，师大女篮得到了冠军。"],
    say=[F(0, "Ví dụ bốn và năm: câu mơ hồ do cách ngắt nhịp khác nhau. Câu sai thứ tư: 医生看到我们非常焦急，连忙把病人的病情告诉我们。 Bác sĩ thấy chúng tôi rất lo lắng, vội nói cho chúng tôi biết bệnh tình của bệnh nhân."),
         F(1, "Nếu ngắt sau 看到, thì người lo lắng là chúng tôi. Nếu ngắt sau 我们, thì người lo lắng là bác sĩ."),
         F(2, "Cách sửa: 医生看到我们非常焦急的样子，连忙把病人的病情告诉我们, thêm 的样子 để rõ là chúng tôi lo. Hoặc 医生非常焦急，看到我们，连忙把病人的病情告诉我们, để rõ là bác sĩ lo."),
         F(3, "Câu sai thứ năm: 我们打败了师大女篮得到了冠军。 Câu này cũng có hai cách ngắt nhịp."),
         F(4, "Ngắt sau 师大女篮, nghĩa là chúng tôi đánh bại đội bóng rổ nữ Đại học Sư phạm và giành chức vô địch. Ngắt sau 打败了, nghĩa là chúng tôi bị thua, còn đội bóng rổ nữ Đại học Sư phạm giành chức vô địch. Hai nghĩa ngược hẳn nhau!"),
         F(5, "Cách sửa rất đơn giản: thêm dấu phẩy vào đúng chỗ. 我们打败了师大女篮，得到了冠军。 hoặc 我们打败了，师大女篮得到了冠军。 Các bạn thấy đấy, khi viết, một dấu phẩy cũng có thể thay đổi hoàn toàn ý nghĩa.")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chỉ ra lỗi và sửa lại (1)", reveal=True, size=34,
    items=["(1) 他背着爸爸和我买下了那栋房子。",
           "Đáp án: 背着 có hai nghĩa: cõng hoặc giấu → 他瞒着爸爸和我买下了那栋房子。/ 他背着爸爸，和我一起买下了那栋房子。",
           "(2) 这个精致的玩具将作为今晚最受欢迎的客人的礼品送给他。",
           "Đáp án: 最受欢迎的 bổ nghĩa cho 客人 hay 礼品? → 这个精致的玩具将作为礼品，送给今晚最受欢迎的客人。",
           "(3) 我的车没有锁，在教室门口放着呢，你去骑吧。",
           "Đáp án: 锁 là danh từ hay động từ? → 我的车没上锁，…… / 我的车没有车锁，……"],
    say=[F(0, "Luyện tập: chỉ ra lỗi của các câu sau và đề xuất cách sửa. Câu một: 他背着爸爸和我买下了那栋房子。 Câu này có thể hiểu theo những cách nào? Các bạn tạm dừng và suy nghĩ nhé."),
         F(1, "Đáp án: chữ đầu của 背着 có hai cách đọc và hai nghĩa. Đọc thanh một là cõng trên lưng; đọc thanh bốn là giấu, làm sau lưng ai đó. Nếu nghĩa là giấu, sửa thành 他瞒着爸爸和我买下了那栋房子。 Anh ấy giấu bố và tôi để mua căn nhà. Nếu nghĩa là cõng, sửa thành 他背着爸爸，和我一起买下了那栋房子。"),
         F(2, "Câu hai: 这个精致的玩具将作为今晚最受欢迎的客人的礼品送给他。 Món đồ chơi tinh xảo này sẽ được làm quà tặng cho vị khách được yêu thích nhất tối nay."),
         F(3, "Đáp án: cụm 最受欢迎的 có thể bổ nghĩa cho 客人, vị khách được yêu thích nhất; cũng có thể bổ nghĩa cho 礼品, món quà được yêu thích nhất. Sửa: 这个精致的玩具将作为礼品，送给今晚最受欢迎的客人。"),
         F(4, "Câu ba: 我的车没有锁，在教室门口放着呢，你去骑吧。 Xe của tôi để ở cửa lớp, bạn đi lấy mà đi."),
         F(5, "Đáp án: 锁 có thể là động từ, nghĩa là chưa khóa xe; cũng có thể là danh từ, nghĩa là xe không có ổ khóa. Sửa: 我的车没上锁, xe tôi chưa khóa; hoặc 我的车没有车锁, xe tôi không có khóa.")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chỉ ra lỗi và sửa lại (2)", reveal=True, size=34,
    items=["(4) 我看见她很高兴，就和她聊了起来。",
           "Đáp án: Ai vui, tôi hay cô ấy? → 我看见她很高兴的样子，就…… / 看见她，我很高兴，就……",
           "(5) 他借了我两本书还没还呢。",
           "Đáp án: 借 là mượn hay cho mượn? → 他向我借了两本书，还没还呢。/ 他借给我两本书，我还没还呢。"],
    say=[F(0, "Câu bốn: 我看见她很高兴，就和她聊了起来。 Tôi thấy cô ấy rất vui, liền trò chuyện với cô ấy. Câu này mơ hồ ở đâu?"),
         F(1, "Đáp án: giống ví dụ về bác sĩ, câu này ngắt nhịp khác nhau thì nghĩa khác nhau. Người vui có thể là cô ấy, cũng có thể là tôi. Sửa: 我看见她很高兴的样子，就和她聊了起来, cô ấy vui. Hoặc 看见她，我很高兴，就和她聊了起来, tôi vui."),
         F(2, "Câu năm: 他借了我两本书还没还呢。 Câu này nói ai mượn sách của ai?"),
         F(3, "Đáp án: giống động từ 租, động từ 借 cũng có hai chiều: mượn và cho mượn. Sửa: 他向我借了两本书，还没还呢, anh ấy mượn sách của tôi mà chưa trả. Hoặc 他借给我两本书，我还没还呢, anh ấy cho tôi mượn sách mà tôi chưa trả. Mẹo: khi gặp động từ hai chiều như 租，借, hãy dùng 向 hoặc 跟 để chỉ nhận vào, dùng 给 để chỉ cho đi.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ có dấu chấm", size=40,
    items=["历来 (来) → 从来 · 本来 · 原来 · 后来",
           "维持 (持) → 坚持 · 支持 · 保持 · 主持",
           "准则 (则) → 规则 · 原则 · 法则 · 守则",
           "场所 (场) → 广场 · 市场 · 操场 · 机场",
           "广阔 (广) → 广大 · 广泛 · 广告 · 推广"],
    say=["Phần luyện tập. Bài tập một: mô phỏng ví dụ, viết thêm các từ có chứa chữ được đánh dấu chấm.",
         F(0, "Ví dụ mẫu: 历来, chữ được đánh dấu là chữ thứ hai, chữ lai. Ta có 从来，本来，原来，后来. Tức là xưa nay, vốn dĩ, hóa ra, và sau này."),
         F(1, "维持, chữ được đánh dấu là chữ thứ hai, chữ trì, nghĩa là giữ. Ta có 坚持，支持，保持，主持. Tức là kiên trì, ủng hộ, giữ gìn, và chủ trì."),
         F(2, "准则, chữ được đánh dấu là chữ thứ hai, chữ tắc, nghĩa là quy tắc. Ta có 规则，原则，法则，守则. Tức là quy tắc, nguyên tắc, phép tắc, và nội quy."),
         F(3, "场所, chữ được đánh dấu là chữ đầu, chữ trường, nghĩa là nơi chốn, bãi rộng. Ta có 广场，市场，操场，机场. Tức là quảng trường, chợ, sân tập, và sân bay."),
         F(4, "广阔, chữ được đánh dấu là chữ đầu, chữ quảng, nghĩa là rộng. Ta có 广大，广泛，广告，推广. Tức là rộng lớn, rộng rãi, quảng cáo, và mở rộng phổ biến.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Dùng từ cho sẵn hoàn thành câu (1)", reveal=True, size=38,
    items=["(1) 先提出计划，……（进而）",
           "Đáp án: 先提出计划，进而制定具体的实施方案。",
           "(2) 几十年来，……（忍受）",
           "Đáp án: 几十年来，他一直忍受着病痛，坚持工作。",
           "(3) 星期天他来找我，……（偏偏）",
           "Đáp án: 星期天他来找我，偏偏我不在家。"],
    say=[F(0, "Bài tập hai: dùng từ cho sẵn để hoàn thành câu. Câu một, dùng 进而: 先提出计划，…… Trước hết đưa ra kế hoạch, rồi sao? Các bạn tạm dừng và thử viết nhé."),
         F(1, "Đáp án gợi ý: 先提出计划，进而制定具体的实施方案。 Trước hết đưa ra kế hoạch, rồi từ đó xây dựng phương án thực hiện cụ thể."),
         F(2, "Câu hai, dùng 忍受: 几十年来，…… Mấy chục năm nay, thế nào?"),
         F(3, "Đáp án gợi ý: 几十年来，他一直忍受着病痛，坚持工作。 Mấy chục năm nay, ông ấy luôn chịu đựng bệnh tật, kiên trì làm việc."),
         F(4, "Câu ba, dùng 偏偏: 星期天他来找我，…… Chủ nhật anh ấy đến tìm tôi, thì sao?"),
         F(5, "Đáp án gợi ý: 星期天他来找我，偏偏我不在家。 Chủ nhật anh ấy đến tìm tôi, lại đúng lúc tôi không có nhà. Đây là cách dùng thứ hai: sự thật trái với mong muốn.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Dùng từ cho sẵn hoàn thành câu (2)", reveal=True, size=38,
    items=["(4) 这个地方……（广阔）",
           "Đáp án: 这个地方土地广阔，物产丰富。",
           "(5) ……闻名世界。（众所周知）",
           "Đáp án: 众所周知，中国的长城闻名世界。",
           "(6) 各项工作……（有条不紊）",
           "Đáp án: 各项工作都在有条不紊地进行着。"],
    say=[F(0, "Câu bốn, dùng 广阔: 这个地方…… Nơi này thế nào?"),
         F(1, "Đáp án gợi ý: 这个地方土地广阔，物产丰富。 Nơi này đất đai rộng lớn, sản vật phong phú."),
         F(2, "Câu năm, dùng 众所周知: 什么闻名世界。 Cái gì nổi tiếng thế giới?"),
         F(3, "Đáp án gợi ý: 众所周知，中国的长城闻名世界。 Ai cũng biết, Vạn Lý Trường Thành của Trung Quốc nổi tiếng thế giới. 众所周知 thường đứng đầu câu, sau là dấu phẩy."),
         F(4, "Câu sáu, dùng 有条不紊: 各项工作…… Các công việc thế nào?"),
         F(5, "Đáp án gợi ý: 各项工作都在有条不紊地进行着。 Mọi công việc đều đang được tiến hành đâu ra đấy. 有条不紊地 làm trạng ngữ, giống câu trong bài khóa: 有条不紊地过着自己的日子.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (1)", reveal=True, size=34,
    items=["## Từ cho sẵn: 俗话 · 历来 · 超越 · 真理 · 众所周知",
           "___说：“独木不成林”，这句话告诉我们团结的重要性。___，一根筷子很容易折断，可一把筷子就很难折断了，团结能使我们___自身的局限，产生巨大的力量，所以“团结力量大”成为___人们都认可的___。",
           "Đáp án: 俗话 · 众所周知 · 超越 · 历来 · 真理"],
    say=[F(0, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn một có năm từ: 俗话，历来，超越，真理，众所周知."),
         F(1, "什么说：独木不成林，这句话告诉我们团结的重要性。什么，一根筷子很容易折断，可一把筷子就很难折断了，团结能使我们什么自身的局限，产生巨大的力量，所以团结力量大成为什么人们都认可的什么。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 俗话说，独木不成林；众所周知，一根筷子很容易折断；团结能使我们超越自身的局限；所以团结力量大成为历来人们都认可的真理。 Tục ngữ nói: một cây làm chẳng nên non. Ai cũng biết, một chiếc đũa thì dễ bẻ gãy, nhưng cả bó đũa thì rất khó bẻ. Đoàn kết giúp chúng ta vượt qua giới hạn của bản thân, tạo ra sức mạnh to lớn, cho nên đoàn kết là sức mạnh trở thành chân lý mà xưa nay mọi người đều công nhận.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (2)", reveal=True, size=34,
    items=["## Từ cho sẵn: 诧异 · 偏偏 · 展现 · 古怪 · 恍然大悟",
           "今天是周末，可经理___让我去加班，我满肚子不乐意，却也没有办法。在公司门口，居然遇到了几个同事，我很___，问：“周末怎么还有这么多人来上班？”而他们看到我，神情都有些___。直到走进办公室，鲜花和蛋糕___在我眼前，经理和同事们唱起了生日歌，我才___，原来今天是我的生日……",
           "Đáp án: 偏偏 · 诧异 · 古怪 · 展现 · 恍然大悟"],
    say=[F(0, "Đoạn hai có năm từ: 诧异，偏偏，展现，古怪，恍然大悟."),
         F(1, "今天是周末，可经理什么让我去加班，我满肚子不乐意，却也没有办法。在公司门口，居然遇到了几个同事，我很什么，问：周末怎么还有这么多人来上班？而他们看到我，神情都有些什么。直到走进办公室，鲜花和蛋糕什么在我眼前，经理和同事们唱起了生日歌，我才什么，原来今天是我的生日，他们为我准备了一个特别的生日晚会。 Các bạn điền thử nhé."),
         F(2, "Đáp án: 经理偏偏让我去加班，我很诧异，神情都有些古怪，鲜花和蛋糕展现在我眼前，我才恍然大悟。 Hôm nay là cuối tuần, vậy mà giám đốc lại cứ bắt tôi đi làm thêm, tôi bực cả bụng mà cũng chẳng biết làm sao. Ở cổng công ty, tôi lại gặp mấy đồng nghiệp, tôi rất ngạc nhiên. Còn họ nhìn thấy tôi, vẻ mặt ai cũng hơi kỳ lạ. Đến khi bước vào văn phòng, hoa tươi và bánh kem hiện ra trước mắt, mọi người hát vang bài chúc mừng sinh nhật, tôi mới vỡ lẽ: hôm nay là sinh nhật tôi, họ đã chuẩn bị cho tôi một bữa tiệc đặc biệt."),
         "Các bạn thấy không, đoạn văn này dùng cả 偏偏 lẫn 恍然大悟, đúng là những từ trọng tâm của bài. Hãy đọc to lại đoạn văn này vài lần nhé."])

add("bullets", section="Luyện tập 练习", title="Bài tập 4: Chọn vị trí thích hợp cho từ trong ngoặc", reveal=True, size=34,
    items=["(1) A只有B不断努力，C梦想才能D实现。（得以）",
           "Đáp án: D – 梦想才能得以实现。",
           "(2) 通过A调查研究B发现问题，C找到D解决问题的方法。（进而）",
           "Đáp án: C – ……发现问题，进而找到解决问题的方法。",
           "(3) 经过讨论，A大家的意见B都统一了，C可D他不同意。（偏偏）",
           "Đáp án: D – ……可他偏偏不同意。",
           "(4) A老校长B重视C学生们的D素质教育。（历来）",
           "Đáp án: B – 老校长历来重视学生们的素质教育。",
           "(5) A今年B入境旅游观光的C人数已超过D千万。（据悉）",
           "Đáp án: A – 据悉，今年入境旅游观光的人数已超过千万。"],
    say=[F(0, "Bài tập bốn: chọn vị trí thích hợp cho từ trong ngoặc. Câu một, từ 得以: 只有不断努力，梦想才能实现。 Chỉ có không ngừng cố gắng, ước mơ mới có thể thành hiện thực. Các bạn chọn A, B, C hay D?"),
         F(1, "Đáp án: D. 梦想才能得以实现。 得以 đứng ngay trước động từ chỉ kết quả 实现."),
         F(2, "Câu hai, từ 进而: 通过调查研究发现问题，找到解决问题的方法。 Thông qua điều tra nghiên cứu để phát hiện vấn đề, tìm ra cách giải quyết."),
         F(3, "Đáp án: C. 进而 đứng đầu vế sau: 发现问题，进而找到解决问题的方法。 Phát hiện vấn đề, rồi từ đó tìm ra cách giải quyết."),
         F(4, "Câu ba, từ 偏偏: 经过讨论，大家的意见都统一了，可他不同意。 Qua thảo luận, ý kiến mọi người đã thống nhất, nhưng anh ấy không đồng ý."),
         F(5, "Đáp án: D. 偏偏 là phó từ, đứng sau chủ ngữ 他, trước 不同意: 可他偏偏不同意。 Vậy mà anh ấy cứ nhất định không đồng ý."),
         F(6, "Câu bốn, từ 历来: 老校长重视学生们的素质教育。 Thầy hiệu trưởng già coi trọng giáo dục tố chất của học sinh."),
         F(7, "Đáp án: B. 历来 là phó từ, đứng sau chủ ngữ, trước động từ 重视: 老校长历来重视学生们的素质教育。 Thầy hiệu trưởng xưa nay luôn coi trọng giáo dục toàn diện cho học sinh."),
         F(8, "Câu năm, từ 据悉: 今年入境旅游观光的人数已超过千万。 Năm nay số du khách nhập cảnh tham quan đã vượt quá mười triệu."),
         F(9, "Đáp án: A. 据悉 đứng đầu câu, sau là dấu phẩy: 据悉，今年入境旅游观光的人数已超过千万。 Được biết, năm nay số du khách quốc tế đã vượt mười triệu.")])

add("bullets", section="Luyện tập 练习", title="Mở rộng 扩展: từ vựng và kết hợp từ (1)", size=34,
    items=["附属 phụ thuộc, trực thuộc: 附属中学 · 这所医院附属于医科大学。",
           "杠杆 đòn bẩy: 杠杆作用、经济杠杆 · 应充分发挥金融机构在经济发展中的杠杆作用。",
           "疙瘩 cục u, nút thắt: 面疙瘩、线疙瘩 · 他的眉头皱成了一个大疙瘩。",
           "勾结 câu kết: 暗中勾结 · 他们勾结在一起，做了不少坏事。",
           "贯彻 quán triệt, thực hiện: 贯彻始终 · 我们公司一直贯彻公平、公正的原则。",
           "混淆 lẫn lộn: 混淆黑白、混淆是非 · 对和错是不容混淆的。"],
    say=["Phần mở rộng thứ hai của sách giới thiệu mười hai từ cùng cách kết hợp thường gặp. Thầy đọc qua để các bạn làm quen.",
         F(0, "附属, phụ thuộc, trực thuộc. Kết hợp: 附属中学, trường trung học trực thuộc. Ví dụ: 这所医院附属于医科大学。 Bệnh viện này trực thuộc trường đại học y."),
         F(1, "杠杆, đòn bẩy. Kết hợp: 杠杆作用，经济杠杆, tác dụng đòn bẩy, đòn bẩy kinh tế. Ví dụ: 应充分发挥金融机构在经济发展中的杠杆作用。 Cần phát huy đầy đủ vai trò đòn bẩy của các tổ chức tài chính trong phát triển kinh tế."),
         F(2, "疙瘩, cục u, nút thắt. Kết hợp: 面疙瘩，线疙瘩, viên bột, nút chỉ. Ví dụ: 他的眉头皱成了一个大疙瘩。 Lông mày anh ấy nhíu chặt lại thành một nút."),
         F(3, "勾结, câu kết, mang nghĩa xấu. Kết hợp: 暗中勾结, ngấm ngầm câu kết. Ví dụ: 他们勾结在一起，做了不少坏事。 Bọn họ câu kết với nhau, làm không ít chuyện xấu."),
         F(4, "贯彻, quán triệt, thực hiện triệt để. Kết hợp: 贯彻始终, thực hiện từ đầu đến cuối. Ví dụ: 我们公司一直贯彻公平、公正的原则。 Công ty chúng tôi luôn thực hiện nguyên tắc công bằng, công chính."),
         F(5, "混淆, lẫn lộn, làm lẫn lộn. Kết hợp: 混淆黑白，混淆是非, đổi trắng thay đen, lẫn lộn phải trái. Ví dụ: 对和错是不容混淆的。 Đúng và sai không thể lẫn lộn được.")])

add("bullets", section="Luyện tập 练习", title="Mở rộng 扩展: từ vựng và kết hợp từ (2)", size=34,
    items=["机械 máy móc; cứng nhắc: 机械化 · 这个人做事太机械了，一点儿灵活性都没有。",
           "冷却 làm nguội: 自然冷却、冷却剂 · 岩浆冷却后就成了岩石。",
           "媒介 môi giới, trung gian: 传播媒介 · 苍蝇是传染疾病的媒介。",
           "谜语 câu đố: 猜谜语 · 这个谜语我怎么也猜不出来，你快告诉我吧。",
           "母语 tiếng mẹ đẻ: 母语教学 · 我的母语是汉语，你的母语呢？",
           "排练 diễn tập: 排练节目 · 为了这次演出，我们天天认真排练。"],
    say=[F(0, "机械, máy móc, và nghĩa bóng là cứng nhắc. Kết hợp: 机械化, cơ giới hóa. Ví dụ: 这个人做事太机械了，一点儿灵活性都没有。 Người này làm việc máy móc quá, chẳng linh hoạt chút nào."),
         F(1, "冷却, làm nguội. Kết hợp: 自然冷却，冷却剂, làm nguội tự nhiên, chất làm mát. Ví dụ: 岩浆冷却后就成了岩石。 Dung nham nguội đi thì thành đá."),
         F(2, "媒介, môi giới, trung gian. Kết hợp: 传播媒介, phương tiện truyền thông. Ví dụ: 苍蝇是传染疾病的媒介。 Ruồi là vật trung gian truyền bệnh."),
         F(3, "谜语, câu đố. Kết hợp: 猜谜语, đoán câu đố. Ví dụ: 这个谜语我怎么也猜不出来，你快告诉我吧。 Câu đố này tôi đoán mãi không ra, bạn mau nói cho tôi đi."),
         F(4, "母语, tiếng mẹ đẻ. Kết hợp: 母语教学, dạy học bằng tiếng mẹ đẻ. Ví dụ: 我的母语是汉语，你的母语呢？ Tiếng mẹ đẻ của tôi là tiếng Hán, còn của bạn?"),
         F(5, "排练, diễn tập, tập dượt. Kết hợp: 排练节目, tập tiết mục. Ví dụ: 为了这次演出，我们天天认真排练。 Để chuẩn bị cho buổi biểu diễn này, ngày nào chúng tôi cũng tập luyện nghiêm túc. Các bạn hãy tự đặt thêm câu với mỗi từ nhé.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 19", size=36,
    items=["Từ vựng trọng tâm: 众所周知 · 认定 · 繁殖 · 诧异 · 恍然大悟 · 探索 · 据悉 · 超越 · 丧失 · 有条不紊 · 迷惑",
           "Ngữ pháp: 进而 (rồi tiến thêm) · 得以 (nhờ đó mà có thể) · 偏偏 (lại cứ; trái lại)",
           "Phân biệt: 历来 (văn viết, không dùng trong câu phủ định) ≠ 从来 (chủ yếu trong câu phủ định)",
           "Mở rộng: câu mơ hồ do từ loại, động từ hai chiều, phạm vi định ngữ, ngắt nhịp",
           "## Bài tập về nhà (运用)",
           "Dựa vào bài tập 5, viết lại bài khóa thành bài văn ngắn khoảng 400 chữ"],
    say=["Chúng ta cùng tổng kết bài mười chín.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 众所周知，认定，繁殖，诧异，恍然大悟，探索，据悉，超越，丧失，有条不紊，迷惑. Và đừng quên những từ dễ nhầm như 认定，超越，迷惑, nghĩa của chúng khác với âm Hán Việt trong tiếng Việt."),
         F(1, "Về ngữ pháp: 进而 đứng đầu vế sau, chỉ tiến thêm một bước trên cơ sở đã có. 得以 nghĩa là nhờ điều kiện nào đó mà có thể, phía sau là kết quả. 偏偏 có hai nghĩa: cố tình làm trái, và sự thật trái với mong muốn."),
         F(2, "Về phân biệt từ: 历来 mang màu sắc văn viết, không dùng trong câu phủ định, có thể đi với một từ hai âm tiết đứng một mình; còn 从来 chủ yếu dùng trong câu phủ định."),
         F(3, "Về phần mở rộng: câu mơ hồ thường do một từ có hai từ loại, động từ có hai chiều như 租，借, phạm vi định ngữ không rõ, hoặc ngắt nhịp khác nhau. Khi viết, hãy đọc lại câu của mình xem có thể hiểu theo hai cách không nhé."),
         F(5, "Bài tập về nhà, theo phần vận dụng của sách: bài khóa miêu tả một thế giới biển sâu kỳ diệu, nơi không có ánh nắng, áp suất rất lớn, nhưng vẫn có những sinh vật kỳ lạ. Chúng sống nhờ đâu, có bản lĩnh gì, còn những lĩnh vực nào con người chưa biết? Hãy dựa vào bài tập năm, viết lại bài khóa thành một bài văn ngắn khoảng bốn trăm chữ. Nhớ thử dùng 进而，得以，偏偏 trong bài viết nhé."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Thế giới quanh ta vẫn còn biết bao điều kỳ diệu đang chờ được khám phá. Hẹn gặp lại các bạn ở bài hai mươi: 金鸡窝, Ổ gà vàng. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Thượng) – Bài 19: 无阳光的深海世界 (Thế giới biển sâu không ánh mặt trời)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"蛤": "格",                # gé (蛤蜊、巨蛤 – trong bài luôn đọc gé)
                    "蚌": "棒",                # bàng
                    "红冠": "红官",            # hóngguān
                    "地壳": "地窍",            # dìqiào
                    "干裂": "甘裂",            # gānliè
                    "裂缝": "裂凤",            # lièfèng
                    "生长": "生涨",            # shēngzhǎng
                    "长相": "涨相",            # zhǎngxiàng
                    "校长": "校涨",            # xiàozhǎng
                    "认定为": "认定维",        # wéi
                    "能为我们": "能位我们",    # wèi
                    "为我准备": "位我准备",    # wèi
                    "真相": "真象",            # zhēnxiàng
                    "数十年": "树十年",        # shù
                    "倒非": "到非",            # dào
                    "朴素": "普素",            # pǔsù
                    "铺张": "扑张",            # pūzhāng
                    "杠杆": "杠敢",            # gànggǎn
                    "还没还呢": "还没环呢",    # huán
                    "背着爸爸，和我一起": "杯着爸爸，和我一起"},  # bēi (nghĩa cõng)
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai19.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
