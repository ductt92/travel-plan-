#!/usr/bin/env python3
"""Kịch bản bài giảng 顶石中文 – Bài 6.2 «谁能站在新职业风口？». Chạy để sinh ds62.json."""
import json
import os

TAG = "顶石中文 · Bài 6.2 · 谁能站在新职业风口？"
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
    zh="谁能站在新职业风口？", py="Shéi néng zhàn zài xīn zhíyè fēngkǒu?",
    vi="Bài 6.2: Ai đứng được ở đầu ngọn gió nghề nghiệp mới?",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng giáo trình 顶石中文, Đỉnh cao tiếng Trung.",
         {"t": "Hôm nay chúng ta học bài thứ hai của Đơn vị sáu, chủ đề Nơi làm việc: bài sáu chấm hai, 谁能站在新职业风口？ Nghĩa là: Ai có thể đứng ở đầu ngọn gió của nghề nghiệp mới?",
          "cap": "Hôm nay chúng ta học bài thứ hai của Đơn vị 6, chủ đề Nơi làm việc: bài 6.2, 谁能站在新职业风口？ Nghĩa là: Ai có thể đứng ở đầu ngọn gió của nghề nghiệp mới?"},
         "Bài trước nói về mặt tối của công việc: chế độ 九九六. Bài này lại mang một không khí rất tươi mới: internet đã sinh ra hàng loạt nghề nghiệp chưa từng có, như tuyển thủ thể thao điện tử, người livestream bán hàng, người thiết kế lịch trình du lịch riêng. Giới trẻ Trung Quốc chọn nghề theo sở thích, còn bố mẹ thì vẫn mong con có một cái bát cơm sắt.",
         "Ở Việt Nam, chắc các bạn cũng thấy rất nhiều nghề mới như TikToker, người livestream bán hàng, hay tài xế công nghệ. Trong lúc học, các bạn hãy so sánh xem giới trẻ hai nước chọn nghề giống và khác nhau thế nào nhé."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài báo về các nghề mới: vì sao xuất hiện, thu nhập ra sao, giới trẻ chọn nghề thế nào",
           "Nắm vững 48 từ mới, kèm âm Hán Việt và ví dụ",
           "10 mẫu câu: 一时间 · 所谓的……只是……而已 · 顺着 · 渐成风气 · 呈现……态势 · 过一道难关 · 相去甚远 · 尤以……为最 · 以……为导向 · 必将",
           "Kết hợp từ: 争相 · 轮番 · 走高/走低/走红 và 7 thành ngữ",
           "Luyện tập theo sách; liên hệ: “bát cơm sắt” và chuyện chọn nghề ở Việt Nam"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu bài báo về các nghề mới: vì sao chúng xuất hiện, thu nhập ra sao, và giới trẻ Trung Quốc chọn nghề theo những tiêu chí nào."),
         F(1, "Thứ hai, nắm vững bốn mươi tám từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học mười mẫu câu trọng điểm, như 一时间，顺着，渐成风气，呈现态势，相去甚远，尤以为最, và 以为导向."),
         F(3, "Thứ tư, học các kết hợp từ 争相，轮番，走高, cùng bảy thành ngữ như 应运而生，五花八门，朝不保夕."),
         F(4, "Thứ năm, làm bài luyện tập của sách, và liên hệ với chuyện chọn nghề ở Việt Nam: bát cơm sắt của Trung Quốc rất giống chuyện vào biên chế của chúng ta."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 课前思考", title="Câu hỏi trước bài học 课前思考", reveal=True, size=36,
    items=["(1) 你们国家最近出现了哪些新兴职业？",
           "Đáp án gợi ý: 越南最近出现了很多新兴职业，比如短视频博主、直播带货主播、网约车司机、外卖骑手等。",
           "(2) 你们国家大学生找工作时，哪些是优先考虑的因素？",
           "Đáp án gợi ý: 收入、发展前景和工作地点是优先考虑的因素，也有不少人更看重兴趣。",
           "(3) 你们国家哪一些行业属于所谓的“铁饭碗”？",
           "Đáp án gợi ý: 在越南，公务员、公立学校的老师、公立医院的医生等被认为是“铁饭碗”。"],
    say=["Chúng ta bắt đầu bằng ba câu hỏi trước bài học, 课前思考. Thầy đọc câu hỏi, các bạn tạm dừng để tự trả lời bằng tiếng Trung, rồi nghe câu trả lời gợi ý nhé.",
         F(0, "Câu một: 你们国家最近出现了哪些新兴职业？ Ở nước bạn gần đây xuất hiện những nghề mới nổi nào? 新兴 là mới nổi."),
         F(1, "Gợi ý: 越南最近出现了很多新兴职业，比如短视频博主、直播带货主播、网约车司机、外卖骑手等。 Gần đây Việt Nam xuất hiện rất nhiều nghề mới, như người làm video ngắn, người livestream bán hàng, tài xế xe công nghệ, shipper giao đồ ăn."),
         F(2, "Câu hai: 你们国家大学生找工作时，哪些是优先考虑的因素？ Sinh viên nước bạn khi tìm việc ưu tiên cân nhắc những yếu tố nào?"),
         F(3, "Gợi ý: 收入、发展前景和工作地点是优先考虑的因素，也有不少人更看重兴趣。 Thu nhập, triển vọng phát triển và nơi làm việc là những yếu tố được ưu tiên; cũng có không ít người coi trọng sở thích hơn."),
         F(4, "Câu ba: 你们国家哪一些行业属于所谓的铁饭碗？ Ở nước bạn, những ngành nào thuộc loại bát cơm sắt? 铁饭碗 là bát cơm sắt, chỉ công việc ổn định suốt đời, rơi xuống đất cũng không vỡ."),
         F(5, "Gợi ý: 在越南，公务员、公立学校的老师、公立医院的医生等被认为是铁饭碗。 Ở Việt Nam, công chức, giáo viên trường công, bác sĩ bệnh viện công được coi là bát cơm sắt. Người Việt hay gọi là vào biên chế.")])

add("bullets", section="Khởi động 课前思考", title="Khởi động: tên các nghề mới trong tiếng Trung", size=35,
    items=["网红 người nổi tiếng trên mạng (KOL) · 博主 blogger · 短视频博主 TikToker, YouTuber",
           "主播 streamer · 带货主播 người livestream bán hàng · 电竞选手 tuyển thủ thể thao điện tử",
           "外卖骑手 shipper giao đồ ăn · 网约车司机 tài xế xe công nghệ",
           "配音员 diễn viên lồng tiếng · 化妆师 chuyên viên trang điểm · 游戏测评师 người review game",
           "旅游定制师 người thiết kế tour riêng · 海外买手 người mua hàng ở nước ngoài"],
    say=["Trước khi vào bài, chúng ta làm quen với tên tiếng Trung của một số nghề mới. Nhiều từ trong số này sẽ xuất hiện trong bài khóa.",
         F(0, "网红, người nổi tiếng trên mạng, gần giống KOL. 博主 là blogger, người viết blog hay làm kênh riêng; 短视频博主 là người làm video ngắn, như TikToker, YouTuber."),
         F(1, "主播 là streamer, người livestream. 带货主播 là người livestream bán hàng; 带货 nghĩa đen là mang hàng, tức là giúp bán hàng. 电竞选手 là tuyển thủ thể thao điện tử."),
         F(2, "外卖骑手, người giao đồ ăn, chính là shipper. 网约车司机 là tài xế xe đặt qua mạng, tức tài xế xe công nghệ như Grab."),
         F(3, "配音员, diễn viên lồng tiếng. 化妆师, chuyên viên trang điểm. 游戏测评师, người đánh giá, review game."),
         F(4, "旅游定制师, người thiết kế tour du lịch riêng theo yêu cầu. 海外买手, người chuyên mua hàng ở nước ngoài về bán, gần giống người order hàng xách tay ở Việt Nam.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("风口", "fēngkǒu", "phong khẩu", "danh từ", "chỗ đầu gió; đầu ngọn gió, nơi nhiều cơ hội nhất", "站在风口上，猪也能飞起来。", "Đứng đúng đầu ngọn gió, đến con lợn cũng bay lên được.",
     "Danh từ, nghĩa gốc là chỗ gió thổi mạnh, như 别站在风口, đừng đứng chỗ đầu gió. Nay hay dùng nghĩa bóng: lĩnh vực đang bùng nổ, nhiều cơ hội nhất, hoặc nơi cạnh tranh gay gắt nhất. Câu ví dụ là câu nói nổi tiếng của Lôi Quân, nhà sáng lập Xiaomi."),
    ("战队", "zhànduì", "chiến đội", "danh từ", "đội tuyển (thể thao điện tử)", "他们的战队获得了冠军。", "Đội tuyển của họ đã giành chức vô địch.",
     "Danh từ, nghĩa gốc là đội quân chiến đấu, nay chủ yếu chỉ đội tuyển thể thao điện tử. Trong bài: IG战队, đội tuyển IG của Trung Quốc."),
    ("电竞", "diànjìng", "điện cạnh", "danh từ", "thể thao điện tử (eSports)", "电竞已经成为亚运会的正式比赛项目。", "Thể thao điện tử đã trở thành môn thi đấu chính thức của Á vận hội.",
     "Danh từ, nói gọn của 电子竞技, thể thao điện tử. 电竞选手 là tuyển thủ thể thao điện tử. Tại Á vận hội Hàng Châu, thể thao điện tử lần đầu là môn thi đấu chính thức có tranh huy chương."),
    ("争相", "zhēngxiāng", "tranh tương", "phó từ", "tranh nhau, đua nhau", "媒体争相报道这条新闻。", "Báo chí đua nhau đưa tin này.",
     "Phó từ, nghĩa là tranh nhau, đua nhau làm việc gì, đứng trước động từ: 争相报道，争相购买，争相观看. Lát nữa ở phần kết hợp từ chúng ta sẽ gặp lại."),
    ("伴随", "bànsuí", "bạn tùy", "động từ", "đi kèm, đi theo, cùng với", "伴随着经济发展，生活越来越好。", "Cùng với sự phát triển kinh tế, cuộc sống ngày càng tốt hơn.",
     "Động từ, nghĩa là đi theo, đi cùng. Hay dùng dạng 伴随着, cùng với, theo đà. Trong bài: 伴随着改革开放的浪潮, cùng với làn sóng cải cách mở cửa."),
    ("浪潮", "làngcháo", "lãng triều", "danh từ", "làn sóng, trào lưu", "互联网浪潮改变了我们的生活。", "Làn sóng internet đã thay đổi cuộc sống của chúng ta.",
     "Danh từ, nghĩa gốc là sóng lớn, nghĩa bóng là trào lưu xã hội trên quy mô lớn, như 改革开放的浪潮, làn sóng cải cách mở cửa."),
    ("飞速", "fēisù", "phi tốc", "phó từ", "cực nhanh, nhanh như bay", "中国经济飞速发展。", "Kinh tế Trung Quốc phát triển cực nhanh.",
     "Phó từ, nghĩa là với tốc độ rất nhanh, như bay. Thường đi với 发展: 飞速发展. Gần nghĩa với 迅速，高速."),
    ("催生", "cuīshēng", "thôi sinh", "động từ", "thúc đẩy ra đời, làm nảy sinh", "网购催生了快递行业。", "Mua sắm trực tuyến đã thúc đẩy ngành chuyển phát nhanh ra đời.",
     "Động từ, nghĩa gốc là giục sinh, thúc đẻ; nghĩa bóng là thúc đẩy sự vật mới ra đời và phát triển. Chữ 催 là thúc giục, như 催促. Trong bài: 催生了一大批新职业群体."),
    ("顶级", "dǐngjí", "đỉnh cấp", "tính từ", "hàng đầu, đẳng cấp cao nhất", "他是世界顶级的设计师。", "Anh ấy là nhà thiết kế hàng đầu thế giới.",
     "Tính từ thuộc tính, nghĩa là cấp cao nhất, trình độ cao nhất, chỉ đứng trước danh từ: 顶级专家，顶级酒店. Chữ 顶 là đỉnh, nóc."),
    ("流量", "liúliàng", "lưu lượng", "danh từ", "lưu lượng (mạng); lượt xem, độ “hot”", "这个视频的流量很大。", "Video này có lượt xem rất lớn.",
     "Danh từ, nghĩa gốc là lưu lượng nước, xe, dữ liệu. Ngày nay trên mạng, 流量 là lượt truy cập, lượt xem, độ nổi tiếng. 流量明星 là ngôi sao hot; 顶级流量主播 là người livestream hot nhất."),
    ("主播", "zhǔbō", "chủ bá", "danh từ", "người dẫn chương trình; streamer", "她是一名直播带货主播。", "Cô ấy là một người livestream bán hàng.",
     "Danh từ, nghĩa gốc là phát thanh viên chính của chương trình; nay hay chỉ người livestream trên mạng. Chữ 播 là phát sóng, như 直播, phát trực tiếp."),
    ("轮番", "lúnfān", "luân phiên", "phó từ", "lần lượt, thay phiên nhau", "几位专家轮番上台发言。", "Mấy vị chuyên gia lần lượt lên phát biểu.",
     "Phó từ, nghĩa là thay phiên nhau, lần lượt làm một việc. Kết hợp: 轮番上场，轮番上阵. Trong bài: 李佳琦、薇娅轮番登上热搜, hai người thay nhau lên bảng tìm kiếm nóng."),
    ("吸金", "xījīn", "hấp kim", "động từ", "hút tiền, kiếm tiền nhanh", "这部电影上映三天就吸金十亿。", "Bộ phim này ra rạp ba ngày đã hút về một tỉ tệ.",
     "Động từ, từ mới trên báo chí, nghĩa là thu hút tiền, kiếm tiền rất nhanh. 吸 là hút, 金 là tiền. 吸金能力 là khả năng hút tiền."),
    ("经纪人", "jīngjìrén", "kinh kỷ nhân", "danh từ", "người quản lý (nghệ sĩ); người môi giới", "明星的经纪人负责安排演出。", "Người quản lý của ngôi sao phụ trách sắp xếp lịch diễn.",
     "Danh từ, chỉ người lo ký hợp đồng, sắp xếp lịch diễn, phát ngôn thay cho ngôi sao hay vận động viên, tức là người quản lý. Còn 房产经纪人 là người môi giới bất động sản."),
    ("买手", "mǎishǒu", "mãi thủ", "danh từ", "người thu mua, chuyên viên mua hàng (buyer)", "她是一名海外买手。", "Cô ấy là một người chuyên mua hàng ở nước ngoài.",
     "Danh từ, chỉ người nắm bắt xu hướng, dựa vào nhu cầu thị trường để chọn và mua hàng, tức là buyer. 海外买手 là người chuyên mua hàng ở nước ngoài về bán, gần giống người order hàng xách tay ở Việt Nam."),
    ("分众", "fēnzhòng", "phân chúng", "động từ", "phân nhóm người dùng theo nhu cầu", "现在的广告越来越分众化。", "Quảng cáo ngày nay ngày càng nhắm vào từng nhóm khách riêng.",
     "Động từ, nghĩa là chia người dùng thành các nhóm theo nhu cầu khác nhau, thường dùng dạng 分众化. Trong bài: 需求高度分众化、个性化的时代."),
    ("细分", "xìfēn", "tế phân", "động từ", "chia nhỏ, phân chia chi tiết", "我们要细分市场。", "Chúng ta phải phân khúc thị trường.",
     "Động từ, nghĩa là phân chia tỉ mỉ. 细分市场 là phân khúc thị trường. Trong bài: 将人们的各种诉求细分出来, tách nhỏ các nhu cầu khác nhau của con người."),
    ("顺着", "shùnzhe", "thuận trước", "giới từ", "dọc theo, men theo; theo", "顺着这条路一直走。", "Cứ đi thẳng theo con đường này.",
     "Giới từ, nghĩa là dọc theo, men theo một con đường; hoặc theo một hướng suy nghĩ. Trong bài: 顺着这个思路, theo hướng suy nghĩ này. Đây cũng là một mẫu câu trọng điểm."),
    ("攻略", "gōnglüè", "công lược", "danh từ", "cẩm nang, bí kíp, hướng dẫn chi tiết", "出发前我看了很多旅游攻略。", "Trước khi đi tôi đã đọc rất nhiều cẩm nang du lịch.",
     "Danh từ, nghĩa gốc là đánh chiếm, nay chỉ hướng dẫn chi tiết từng bước: 旅游攻略, cẩm nang du lịch; 游戏攻略, bí kíp chơi game. Giới trẻ Việt hay nói xin review, xin tips, khá giống nghĩa này."),
    ("囊括", "nángkuò", "nang quát", "động từ", "bao gồm tất cả; giành trọn", "中国队囊括了全部金牌。", "Đội Trung Quốc giành trọn tất cả huy chương vàng.",
     "Động từ, nghĩa là bao gồm tất cả, gom hết vào. 囊 là cái túi, 括 là bao quát. Trong thể thao, 囊括 là giành trọn. Trong bài: 从路线规划到酒店预订全部囊括."),
    ("定制", "dìngzhì", "định chế", "động từ", "đặt làm riêng, thiết kế theo yêu cầu", "这套西装是专门定制的。", "Bộ vest này được may đo riêng.",
     "Động từ, nghĩa là làm theo yêu cầu riêng của từng khách hàng: 定制西装, may đo vest; 私人定制, dịch vụ thiết kế riêng cho từng người."),
    ("风气", "fēngqì", "phong khí", "danh từ", "nếp, thói quen, phong trào xã hội", "学校形成了良好的学习风气。", "Trường đã hình thành nếp học tập tốt.",
     "Danh từ, chỉ sở thích hay thói quen thịnh hành trong xã hội hoặc một tập thể: 社会风气，学习风气. Trong bài có mẫu 渐成风气, dần thành phong trào."),
    ("适龄", "shìlíng", "thích linh", "tính từ", "đúng độ tuổi, trong độ tuổi phù hợp", "适龄儿童都应该上学。", "Trẻ em trong độ tuổi đi học đều nên được đến trường.",
     "Tính từ, nghĩa là có độ tuổi phù hợp với một yêu cầu nào đó: 适龄儿童, trẻ đúng tuổi đi học; 适龄劳动力, lao động trong độ tuổi lao động."),
    ("日趋", "rìqū", "nhật xu", "phó từ", "ngày càng", "两国关系日趋紧密。", "Quan hệ hai nước ngày càng khăng khít.",
     "Phó từ văn viết, nghĩa là ngày càng, giống 日益 và 越来越. Thường đi với tính từ hai âm tiết: 日趋成熟，日趋多样化."),
    ("呈现", "chéngxiàn", "trình hiện", "động từ", "hiện ra, thể hiện, cho thấy", "市场呈现出良好的发展态势。", "Thị trường cho thấy xu thế phát triển tốt.",
     "Động từ, nghĩa là hiện ra, bày ra trước mắt. Mẫu hay gặp trong tin tức: 呈现什么态势, cho thấy xu thế gì đó; chúng ta sẽ học ở phần mẫu câu."),
    ("稳步", "wěnbù", "ổn bộ", "tính từ", "vững bước, đều đặn, chắc chắn", "公司收入稳步增长。", "Doanh thu công ty tăng trưởng đều đặn.",
     "Tính từ, nghĩa đen là bước đi vững vàng, nghĩa bóng là tiến hành chắc chắn theo từng bước. Hầu như luôn làm trạng ngữ: 稳步上涨，稳步提升，稳步发展."),
    ("态势", "tàishì", "thái thế", "danh từ", "xu thế, tình hình", "疫情呈现下降态势。", "Dịch bệnh cho thấy xu thế giảm.",
     "Danh từ, chỉ tình hình và trạng thái phát triển của sự vật. Thường đi với 呈现 hay 保持: 呈现上升态势，保持良好态势."),
    ("赶超", "gǎnchāo", "cản siêu", "động từ", "đuổi kịp và vượt qua", "我们要赶超世界先进水平。", "Chúng ta phải đuổi kịp và vượt trình độ tiên tiến thế giới.",
     "Động từ, ghép từ 赶 là đuổi theo và 超 là vượt qua. Trong bài: 已经赶超普通白领收入水平, đã đuổi kịp và vượt mức thu nhập của nhân viên văn phòng bình thường."),
    ("抉择", "juézé", "quyết trạch", "danh từ", "sự lựa chọn (quan trọng, khó khăn)", "这是人生中一个重要的抉择。", "Đây là một lựa chọn quan trọng trong đời.",
     "Danh từ, cũng làm động từ, nghĩa là lựa chọn, nhưng trang trọng hơn 选择, thường dùng cho những lựa chọn khó khăn, hệ trọng. Tiêu đề nhỏ trong bài: 在传统和新兴之间抉择."),
    ("当下", "dāngxià", "đương hạ", "danh từ", "hiện nay, lúc này", "我们要珍惜当下。", "Chúng ta phải trân trọng hiện tại.",
     "Danh từ, nghĩa là hiện nay, ngay lúc này; cũng có nghĩa là ngay lúc ấy. Trong bài: 对于当下年轻人来说, đối với giới trẻ hiện nay."),
    ("考量", "kǎoliáng", "khảo lượng", "động từ", "cân nhắc, xem xét", "价格是我们考量的重要因素。", "Giá cả là yếu tố quan trọng chúng tôi cân nhắc.",
     "Động từ, nghĩa là suy nghĩ và cân đo. Chú ý chữ thứ hai đọc thanh hai, liáng, như trong 测量. Trong bài, 考量点 là điểm cân nhắc, tiêu chí cân nhắc."),
    ("难关", "nánguān", "nan quan", "danh từ", "cửa ải khó khăn, khó khăn lớn", "我们一起渡过了难关。", "Chúng ta đã cùng nhau vượt qua khó khăn.",
     "Danh từ, nghĩa đen là cửa ải khó qua, nghĩa bóng là khó khăn khó vượt qua. Kết hợp: 渡过难关，闯过难关，过一道难关. Chữ 关 Hán Việt là quan, cửa ải."),
    ("私企", "sīqǐ", "tư xí", "danh từ", "doanh nghiệp tư nhân", "他在一家私企工作。", "Anh ấy làm việc ở một doanh nghiệp tư nhân.",
     "Danh từ, nói gọn của 私营企业, doanh nghiệp tư nhân; đối lập với 国企, doanh nghiệp nhà nước."),
    ("从业", "cóngyè", "tòng nghiệp", "động từ", "làm nghề, hành nghề", "他在金融业从业多年。", "Anh ấy đã làm trong ngành tài chính nhiều năm.",
     "Động từ, nghĩa là làm một nghề, một ngành nào đó. 从业者 hay 从业人员 là người làm nghề, người trong ngành. Trong bài: 新媒体从业者, người làm truyền thông mới."),
    ("折射", "zhéshè", "chiết xạ", "động từ", "khúc xạ; phản ánh", "这件小事折射出社会的变化。", "Chuyện nhỏ này phản ánh sự thay đổi của xã hội.",
     "Động từ, nghĩa vật lý là khúc xạ ánh sáng; nghĩa bóng là phản ánh bản chất hay hiện tượng của sự vật. Trong bài: 折射出全新的时代心态."),
    ("测评", "cèpíng", "trắc bình", "động từ", "đo lường và đánh giá, review", "他专门做手机测评。", "Anh ấy chuyên làm review điện thoại.",
     "Động từ, nghĩa là đo lường theo các tiêu chí rồi đánh giá, chính là review sản phẩm. 游戏测评师 là người chuyên đánh giá game."),
    ("玩家", "wánjiā", "ngoạn gia", "danh từ", "người chơi; người sành chơi", "这款游戏有上亿玩家。", "Trò chơi này có hơn một trăm triệu người chơi.",
     "Danh từ, chỉ người yêu thích, thành thạo và say mê một hoạt động như sưu tầm, chơi game. Trong bài: 游戏角色扮演玩家, người hóa trang nhập vai nhân vật game, tức là cosplayer."),
    ("国企", "guóqǐ", "quốc xí", "danh từ", "doanh nghiệp nhà nước", "很多父母希望孩子进国企。", "Nhiều bố mẹ mong con vào doanh nghiệp nhà nước.",
     "Danh từ, nói gọn của 国有企业, doanh nghiệp nhà nước. Ở Trung Quốc, làm công chức hay vào 国企 được coi là 铁饭碗, bát cơm sắt."),
    ("清晰", "qīngxī", "thanh tích", "tính từ", "rõ ràng, rõ nét", "他对未来有清晰的规划。", "Anh ấy có kế hoạch rõ ràng cho tương lai.",
     "Tính từ, nghĩa là rõ ràng, rõ nét: 图像清晰, hình ảnh sắc nét; 思路清晰, mạch suy nghĩ mạch lạc. Chữ thứ hai đọc thanh một."),
    ("顶尖", "dǐngjiān", "đỉnh tiêm", "tính từ", "xuất sắc nhất, hàng đầu", "这是一所顶尖大学。", "Đây là một trường đại học hàng đầu.",
     "Tính từ, nghĩa là tốt nhất, giỏi nhất, giống 顶级. Chữ 尖 là đầu nhọn, mũi nhọn. Trong bài: 成为行业顶尖, trở thành người giỏi nhất trong ngành."),
    ("转行", "zhuǎnháng", "chuyển hàng", "động từ", "chuyển nghề, đổi ngành", "他当了十年老师，后来转行了。", "Anh ấy làm giáo viên mười năm, sau đó chuyển nghề.",
     "Động từ li hợp, nghĩa là đổi sang ngành nghề khác. Chú ý chữ thứ hai đọc háng, như trong 行业, ngành nghề. Có thể tách ra: 转了行."),
    ("导向", "dǎoxiàng", "đạo hướng", "danh từ", "định hướng, hướng dẫn dắt", "企业要以市场为导向。", "Doanh nghiệp phải lấy thị trường làm định hướng.",
     "Danh từ, nghĩa là phương hướng dẫn dắt. Mẫu hay gặp: 以什么为导向, lấy gì làm định hướng; như 以兴趣为导向, lấy sở thích làm định hướng."),
    ("颠覆", "diānfù", "điên phúc", "động từ", "lật đổ; đảo lộn hoàn toàn", "智能手机颠覆了人们的生活方式。", "Điện thoại thông minh đã làm đảo lộn lối sống của con người.",
     "Động từ, nghĩa gốc là lật úp, lật đổ; nay hay dùng nghĩa phá vỡ hoàn toàn cái truyền thống, cũ kỹ. 颠覆性创新 là đổi mới mang tính đột phá. Trong bài: 颠覆职业性别传统."),
    ("主力", "zhǔlì", "chủ lực", "danh từ", "lực lượng chủ yếu, chủ lực", "年轻人是消费的主力。", "Giới trẻ là lực lượng tiêu dùng chủ yếu.",
     "Danh từ, âm Hán Việt là chủ lực, chỉ lực lượng chính. Trong thể thao, 主力队员 là cầu thủ đá chính."),
    ("产业链", "chǎnyèliàn", "sản nghiệp liên", "danh từ", "chuỗi ngành, chuỗi sản xuất", "这里形成了完整的汽车产业链。", "Nơi đây đã hình thành chuỗi ngành ô tô hoàn chỉnh.",
     "Danh từ, chỉ chuỗi liên kết hoàn chỉnh giữa các khâu sản xuất, từ nguyên liệu đến sản phẩm và dịch vụ. Chữ 链 là cái xích, dây chuyền."),
    ("逐年", "zhúnián", "trục niên", "phó từ", "từng năm, qua từng năm", "游客人数逐年增加。", "Số lượng du khách tăng lên qua từng năm.",
     "Phó từ, nghĩa là năm này qua năm khác. Chữ 逐 là lần lượt; tương tự có 逐步, từng bước; 逐渐, dần dần."),
    ("走高", "zǒugāo", "tẩu cao", "động từ", "đi lên, tăng lên (giá cả, chỉ số)", "最近房价持续走高。", "Gần đây giá nhà liên tục tăng.",
     "Động từ, nghĩa là giá cả, chỉ số đi lên, rất hay gặp trong tin kinh tế. Trái nghĩa là 走低. Tương tự còn có 走红, trở nên nổi tiếng."),
    ("土壤", "tǔrǎng", "thổ nhưỡng", "danh từ", "đất trồng; mảnh đất, môi trường phát triển", "这里的土壤很适合种茶。", "Đất ở đây rất thích hợp để trồng chè.",
     "Danh từ, nghĩa gốc là đất đai, đất trồng; nghĩa bóng là môi trường thích hợp để sự vật nảy sinh và phát triển. Trong bài: 互联网领域必将成为催生新职业的土壤."),
]

add("bullets", chapter="Từ mới (48 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 6.2 có 48 từ mới, chia thành 16 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 考量 (liáng) · 转行 (háng) · 争相 (xiāng) · 清晰 (xī)",
           "Nhiều từ mới của thời internet: 电竞 · 流量 · 主播 · 吸金 · 买手 · 攻略 · 测评"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bảng từ của sách có bốn mươi chín từ; thầy chọn bốn mươi tám từ, còn chữ 淘 sẽ được giảng trong bài khóa, ở từ 海淘. Thầy chia thành mười sáu nhóm nhỏ, mỗi nhóm ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Chú ý cách đọc của một số chữ: 考量 đọc là kǎoliáng, 转行 đọc là zhuǎnháng, 争相 đọc là zhēngxiāng, và 清晰 đọc là qīngxī."),
         F(4, "Bài này có rất nhiều từ mới của thời internet, như 电竞，流量，主播，吸金，买手，攻略，测评. Đây đều là những từ người Trung Quốc dùng hằng ngày trên mạng, rất đáng học. Chúng ta bắt đầu.")])

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
    ("11月3日，来自中国的IG战队站在舞台中央，共同举起2018英雄联盟全球总决赛的世界冠军奖杯。一时间，电竞职业选手也成为了媒体争相报道的热点——打游戏原来也是职业！",
     "Ngày 3 tháng 11, đội tuyển IG đến từ Trung Quốc đứng giữa sân khấu, cùng nhau nâng cao chiếc cúp vô địch thế giới của Vòng chung kết toàn cầu Liên Minh Huyền Thoại 2018. Trong chốc lát, tuyển thủ thể thao điện tử chuyên nghiệp cũng trở thành tâm điểm được báo chí đua nhau đưa tin: thì ra chơi game cũng là một nghề!",
     ["IG là câu lạc bộ thể thao điện tử Invictus Gaming của Trung Quốc, do Vương Tư Thông, con trai tỷ phú Vương Kiện Lâm, thành lập năm hai nghìn không trăm mười một. 英雄联盟 là game Liên Minh Huyền Thoại; 全球总决赛 là vòng chung kết thế giới.",
      "一时间 là trong chốc lát, nhất thời, một mẫu câu trọng điểm. 争相报道 là đua nhau đưa tin. 原来 ở đây là thì ra, chỉ sự vỡ lẽ."],
     "十一月三日，来自中国的IG战队站在舞台中央，共同举起二零一八英雄联盟全球总决赛的世界冠军奖杯。一时间，电竞职业选手也成为了媒体争相报道的热点——打游戏原来也是职业！"),
    ("事实上，伴随着改革开放的浪潮，各种全新的职业种类应运而生。特别是近年来，得益于全球互联网的飞速发展，都市人消费需求日益多元化，对于服务的专业化需求也不断增多，催生了一大批新职业群体。",
     "Trên thực tế, cùng với làn sóng cải cách mở cửa, đủ loại nghề nghiệp hoàn toàn mới đã thuận theo thời thế mà ra đời. Đặc biệt là những năm gần đây, nhờ internet toàn cầu phát triển nhanh chóng, nhu cầu tiêu dùng của người thành thị ngày càng đa dạng, nhu cầu về dịch vụ chuyên nghiệp cũng không ngừng tăng, làm nảy sinh cả một lớp đông đảo những người làm nghề mới.",
     ["改革开放 là cải cách mở cửa, bắt đầu từ năm một nghìn chín trăm bảy mươi tám. 应运而生 là thành ngữ: thuận theo thời vận mà ra đời, tức là xuất hiện đúng lúc để đáp ứng nhu cầu của thời đại.",
      "得益于 là nhờ vào, được lợi từ. 都市人 là người thành thị. 多元化 là đa dạng hóa. 催生 là thúc đẩy ra đời. 一大批 là cả một lượng lớn."]),
    ("直播界两大顶级流量主播李佳琦、薇娅轮番登上热搜，“吸金”能力超强引人瞩目，而这些带货网红的一场直播背后，有来自五湖四海的专业人士——直播间的灯光师、试吃官、经纪人、客服、海外买手……",
     "Hai streamer hot nhất giới livestream là Lý Giai Kỳ và Vi Á thay nhau lên bảng tìm kiếm nóng, khả năng “hút tiền” cực mạnh khiến ai cũng chú ý; mà đằng sau một buổi livestream của những người nổi tiếng bán hàng này là các chuyên gia đến từ khắp nơi: thợ ánh sáng phòng livestream, người nếm thử, người quản lý, nhân viên chăm sóc khách hàng, người mua hàng ở nước ngoài…",
     ["Tiêu đề nhỏ của phần này là 没有找不到，只有想不到: không có nghề gì là không tìm thấy, chỉ có điều bạn chưa nghĩ tới. 直播界 là giới livestream. 热搜 là bảng tìm kiếm nóng trên Weibo.",
      "李佳琦 được gọi là ông hoàng son môi, từng bán mười lăm nghìn thỏi son trong năm phút. 带货网红 là người nổi tiếng trên mạng chuyên livestream bán hàng. 引人瞩目 là thu hút sự chú ý. 五湖四海 là năm hồ bốn biển, tức là khắp mọi miền."]),
    ("五花八门的职业名称很多都是最近两三年才开始进入人们的生活的，而所谓的“新”职业，也只是在这个需求高度分众化、个性化的时代，将人们的各种诉求细分出来的结果而已。",
     "Những tên gọi nghề nghiệp muôn hình muôn vẻ ấy, nhiều cái chỉ mới đi vào đời sống trong hai ba năm gần đây; mà cái gọi là nghề “mới”, cũng chỉ là kết quả của việc tách nhỏ các nhu cầu khác nhau của con người, trong thời đại mà nhu cầu được phân nhóm và cá nhân hóa cao độ mà thôi.",
     ["五花八门 là thành ngữ, vốn là tên hai thế trận cổ, 五花阵 và 八门阵, nay chỉ muôn hình muôn vẻ, đủ loại. Cấu trúc 是，的 trong vế đầu nhấn mạnh thời gian: chỉ mới hai ba năm gần đây.",
      "所谓的，只是，而已 là cái gọi là, chẳng qua chỉ là, mà thôi: mẫu câu trọng điểm, mang ý cho rằng khái niệm đó không có gì to tát. 诉求 là yêu cầu, mong muốn."]),
    ("顺着这个思路，作为一名“旅行发烧友”，四川姑娘韩小清选择在网络上向游客出售旅游攻略，从路线规划到酒店预订全部囊括，应有尽有。这样的私人定制服务近来渐成风气，韩小清对自己从事这份工作的未来收入也很有信心。",
     "Theo hướng suy nghĩ này, là một “tín đồ du lịch”, cô gái Tứ Xuyên Hàn Tiểu Thanh chọn bán cẩm nang du lịch cho du khách trên mạng, từ lên lộ trình đến đặt khách sạn đều bao trọn, cần gì có nấy. Dịch vụ thiết kế riêng như vậy gần đây dần thành phong trào, Hàn Tiểu Thanh cũng rất tự tin vào thu nhập tương lai của công việc này.",
     ["顺着这个思路 là theo hướng suy nghĩ này. 发烧友 là người mê một thứ gì đó như lên cơn sốt; từ này vốn ở Hồng Kông chỉ người mê thiết bị âm thanh, nay dùng rộng rãi: 电影发烧友，手机发烧友.",
      "囊括 là bao gồm tất cả. 应有尽有 là thành ngữ: cái gì cần có đều có. 私人定制 là dịch vụ đặt làm riêng cho từng người. 渐成风气 là dần dần trở thành phong trào, một mẫu câu trọng điểm."]),
    ("用老眼光来看，新职业不是“铁饭碗”，而且收入普遍处于中低水平，“朝不保夕”随时可能失业。",
     "Nếu nhìn bằng con mắt cũ, nghề mới không phải là “bát cơm sắt”, hơn nữa thu nhập nhìn chung ở mức trung bình và thấp, “sớm không giữ được tối”, có thể thất nghiệp bất cứ lúc nào.",
     ["老眼光 là cách nhìn cũ, quan niệm cũ. 铁饭碗 là bát cơm sắt: công việc ổn định suốt đời, rơi xuống đất cũng không vỡ, như làm công chức hay doanh nghiệp nhà nước. 处于中低水平 là ở mức trung bình và thấp.",
      "朝不保夕 là thành ngữ: buổi sáng không biết buổi tối sẽ ra sao, chỉ tình thế bấp bênh, khó lường. Chữ đầu ở đây đọc zhāo, nghĩa là buổi sáng."]),
    ("然而随着我国大量适龄劳动力从制造业向生活服务业转移，以及在消费升级背景下消费者的需求日趋个性化、多样化，新职业人群的收入也在水涨船高。",
     "Thế nhưng, cùng với việc một lượng lớn lao động trong độ tuổi lao động ở nước ta chuyển từ ngành chế tạo sang ngành dịch vụ đời sống, và nhu cầu của người tiêu dùng ngày càng cá nhân hóa, đa dạng hóa trong bối cảnh nâng cấp tiêu dùng, thu nhập của những người làm nghề mới cũng nước lên thuyền lên.",
     ["我国 là nước ta, cách người Trung Quốc gọi đất nước mình trong văn viết. 适龄劳动力 là lao động trong độ tuổi lao động. 制造业 là ngành chế tạo; 生活服务业 là ngành dịch vụ đời sống như ăn uống, giao hàng, làm đẹp.",
      "消费升级 là nâng cấp tiêu dùng: người dân chuyển từ mua thứ cần thiết sang mua thứ chất lượng, hợp gu. 日趋 là ngày càng. 水涨船高 là thành ngữ: nước lên thì thuyền lên, ý nói cái này tăng thì cái kia cũng tăng theo."]),
    ("《2018年新职业人群工作生活现状调研报告》（以下简称为《报告》）显示，新职业人群目前已是市场需求量较大的群体，收入呈现出稳步上涨的态势，已经赶超普通白领收入水平。",
     "“Báo cáo khảo sát thực trạng công việc và cuộc sống của những người làm nghề mới năm 2018” (dưới đây gọi tắt là “Báo cáo”) cho thấy, người làm nghề mới hiện đã là nhóm có nhu cầu thị trường khá lớn, thu nhập có xu thế tăng đều đặn, đã đuổi kịp và vượt mức thu nhập của nhân viên văn phòng bình thường.",
     ["调研报告 là báo cáo điều tra nghiên cứu. 以下简称为 là dưới đây gọi tắt là, cụm cố định trong văn bản. 需求量 là lượng cầu.",
      "呈现出稳步上涨的态势 là cho thấy xu thế tăng đều đặn; mẫu câu 呈现，态势 rất hay gặp trong tin kinh tế. 赶超 là đuổi kịp và vượt qua. 白领 là nhân viên văn phòng."],
     "《二零一八年新职业人群工作生活现状调研报告》（以下简称为《报告》）显示，新职业人群目前已是市场需求量较大的群体，收入呈现出稳步上涨的态势，已经赶超普通白领收入水平。"),
    ("尽管对于当下年轻人来说，薪水、稳定性早已不是求职中最主要的考量点，但是传统的就业观仍然会对他们产生影响。选择从事新职业，能得到父母理解是很多人必须要过的一道难关。",
     "Tuy đối với giới trẻ hiện nay, lương bổng và sự ổn định từ lâu đã không còn là tiêu chí cân nhắc quan trọng nhất khi tìm việc, nhưng quan niệm việc làm truyền thống vẫn ảnh hưởng đến họ. Khi chọn làm nghề mới, được bố mẹ thấu hiểu là cửa ải khó khăn mà nhiều người phải vượt qua.",
     ["Tiêu đề nhỏ của phần này là 在传统和新兴之间抉择, lựa chọn giữa nghề truyền thống và nghề mới nổi. 尽管，但是 là tuy, nhưng. 薪水 là tiền lương. 考量点 là điểm cân nhắc.",
      "就业观 là quan niệm về việc làm. 过一道难关 là vượt qua một cửa ải khó khăn; chữ 道 là lượng từ của cửa ải, đề bài. Đây là mẫu câu trọng điểm."]),
    ("“我家里不同意我去弄短视频，说私企没几天就会失业，非让我考公务员和事业单位。”新媒体从业者刘轩，实习期间就轻松月入过万，但还是遭到了家人的强烈反对。",
     "“Nhà tôi không đồng ý cho tôi làm video ngắn, bảo làm doanh nghiệp tư nhân chẳng mấy hôm là thất nghiệp, nhất định bắt tôi thi công chức và vào đơn vị sự nghiệp nhà nước.” Lưu Hiên, người làm truyền thông mới, ngay khi còn thực tập đã dễ dàng kiếm được hơn mười nghìn tệ mỗi tháng, nhưng vẫn bị gia đình phản đối kịch liệt.",
     ["弄短视频 là làm video ngắn; 弄 là khẩu ngữ, nghĩa là làm, xoay xở. 没几天 là chẳng được mấy ngày. 非让我 là nhất định bắt tôi; chữ 非 ở đây nghĩa là cứ đòi, nhất định phải.",
      "事业单位 là đơn vị sự nghiệp như trường học, bệnh viện công. 月入过万 là thu nhập tháng hơn một vạn, tức hơn mười nghìn tệ. 遭到 là gặp phải, bị, thường đi với điều không hay: 遭到反对."]),
    ("如今，“95后”作为职场新力量，其就业观的变化，折射出全新的时代心态。有调查显示，“95后”最向往的职业排名是：网红、配音员、化妆师、游戏测评师和游戏角色扮演玩家，已经和父母传统观念中的公务员、教师、国企职员等“好工作”相去甚远。",
     "Ngày nay, thế hệ “sau 95” là lực lượng mới nơi công sở; sự thay đổi trong quan niệm việc làm của họ phản ánh tâm thế mới của thời đại. Khảo sát cho thấy, nghề họ mơ ước nhất là: người nổi tiếng trên mạng, diễn viên lồng tiếng, chuyên viên trang điểm, người review game và cosplayer, đã khác rất xa những “công việc tốt” trong quan niệm của bố mẹ như công chức, giáo viên, nhân viên doanh nghiệp nhà nước.",
     ["95后 là thế hệ sinh từ năm một nghìn chín trăm chín mươi lăm đến chín mươi chín. 作为 là với tư cách là. 其 là của họ. 折射出 là phản ánh ra. 向往 là mơ ước, hướng tới.",
      "网红 là người nổi tiếng trên mạng; 配音员 là diễn viên lồng tiếng; 游戏角色扮演玩家 là người hóa trang nhập vai nhân vật game, tức cosplayer. 和，相去甚远 là khác rất xa so với: một mẫu câu trọng điểm."],
     "如今，九五后作为职场新力量，其就业观的变化，折射出全新的时代心态。有调查显示，九五后最向往的职业排名是：网红、配音员、化妆师、游戏测评师和游戏角色扮演玩家，已经和父母传统观念中的公务员、教师、国企职员等好工作相去甚远。"),
    ("“95后”选择创业的人群中，46%的人会选择海淘、自媒体、直播带货等新兴互联网创业项目，尤以北、深、广三地的毕业生为最。",
     "Trong số những người sau 95 chọn khởi nghiệp, 46% chọn các dự án khởi nghiệp internet mới nổi như mua hàng nước ngoài qua mạng, truyền thông cá nhân, livestream bán hàng; nổi bật nhất là sinh viên tốt nghiệp ở ba nơi Bắc Kinh, Thâm Quyến, Quảng Châu.",
     ["海淘 là mua hàng nước ngoài qua mạng; chữ 淘 nghĩa là đi khắp nơi tìm mua, như trong tên trang Taobao, 淘宝. 自媒体 là truyền thông cá nhân, như kênh YouTube, TikTok của một người. 直播带货 là livestream bán hàng.",
      "尤以，为最 là nổi bật nhất là, nhiều nhất là: mẫu câu trọng điểm. 北、深、广 là ba thành phố Bắc Kinh, Thâm Quyến, Quảng Châu."],
     "九五后选择创业的人群中，百分之四十六的人会选择海淘、自媒体、直播带货等新兴互联网创业项目，尤以北、深、广三地的毕业生为最。"),
    ("基于对自身所在行业和职业的强烈认同感，新职业人群对未来职业发展有着清晰的规划。《报告》也显示，相比传统就业市场的人群，面对未来发展，65.70%的新职业人群希望“成为行业顶尖，继续在这一行做成资深”，打算转行的仅占比1.13%。“热爱”“有趣”“自由”成为他们选择新职业的标签。",
     "Nhờ gắn bó mạnh mẽ với ngành nghề của mình, người làm nghề mới có kế hoạch rõ ràng cho tương lai. “Báo cáo” cũng cho thấy, so với người làm nghề truyền thống, 65,70% người làm nghề mới muốn “trở thành người giỏi nhất ngành, tiếp tục làm đến mức lão luyện”, chỉ 1,13% định chuyển nghề. “Đam mê”, “thú vị”, “tự do” trở thành những nhãn dán của họ khi chọn nghề mới.",
     ["基于 là dựa trên. 认同感 là cảm giác thừa nhận, gắn bó với giá trị của một điều gì đó. 规划 là kế hoạch dài hạn. 相比 là so với.",
      "顶尖 là giỏi nhất. 资深 là lâu năm, giàu kinh nghiệm, như 资深记者, phóng viên kỳ cựu. 这一行 là ngành này, chữ cuối đọc háng. 转行 là chuyển nghề. 标签 là nhãn dán, từ khóa đặc trưng."],
     "基于对自身所在行业和职业的强烈认同感，新职业人群对未来职业发展有着清晰的规划。《报告》也显示，相比传统就业市场的人群，面对未来发展，百分之六十五点七零的新职业人群希望成为行业顶尖，继续在这一行做成资深，打算转行的仅占比百分之一点一三。热爱、有趣、自由成为他们选择新职业的标签。"),
    ("随着社会观念的发展进步和就业群体的年轻化，越来越多的年轻人以兴趣为导向，坚持自我，“初生牛犊不怕虎”，甚至颠覆职业性别传统，成为新兴职业的主力。",
     "Cùng với sự tiến bộ của quan niệm xã hội và việc lực lượng lao động ngày càng trẻ hóa, ngày càng nhiều người trẻ lấy sở thích làm định hướng, kiên trì là chính mình, “nghé con mới đẻ không sợ hổ”, thậm chí phá vỡ truyền thống phân chia nghề theo giới tính, trở thành lực lượng chủ lực của các nghề mới nổi.",
     ["以兴趣为导向 là lấy sở thích làm định hướng; mẫu 以，为导向 rất hay gặp. 坚持自我 là kiên trì là chính mình. 年轻化 là trẻ hóa.",
      "初生牛犊不怕虎 là tục ngữ: nghé con mới sinh không sợ hổ, vì chưa biết hổ đáng sợ thế nào; ý khen người trẻ dám nghĩ dám làm. 颠覆职业性别传统 là phá vỡ truyền thống nghề phân theo giới, ví dụ con trai làm chuyên viên trang điểm, con gái làm tuyển thủ game."]),
    ("随着数字经济产业链结构的深刻变化，经济规模逐年走高，质量更好，组织更优，增长动力更为多元，互联网领域必将成为催生新职业的土壤。",
     "Cùng với những thay đổi sâu sắc trong cơ cấu chuỗi ngành của kinh tế số, quy mô kinh tế tăng lên qua từng năm, chất lượng tốt hơn, tổ chức tối ưu hơn, động lực tăng trưởng đa dạng hơn, lĩnh vực internet nhất định sẽ trở thành mảnh đất thúc đẩy các nghề mới ra đời.",
     ["数字经济 là kinh tế số. 逐年走高 là tăng lên từng năm. 更为多元 là đa dạng hơn; 更为 là cách nói văn viết của 更.",
      "必将 là nhất định sẽ, một mẫu câu trọng điểm. 土壤 nghĩa bóng là mảnh đất, môi trường để sự vật phát triển. Câu kết khẳng định: internet sẽ còn sinh ra rất nhiều nghề mới, và ai nắm bắt được sẽ đứng ở đầu ngọn gió."]),
]
# tiêu đề nhỏ của bài khóa: đoạn bắt đầu phần đó
HEAD = {3: "没有找不到，只有想不到", 9: "在传统和新兴之间抉择"}

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 谁能站在新职业风口？", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa. Bài được cải biên từ bài báo 新职业兴起，你准备好了吗？ Nghề mới nổi lên, bạn đã sẵn sàng chưa? của tác giả 张岩, đăng trên trang 中国报道网 ngày mười chín tháng mười hai năm hai nghìn không trăm mười tám. Bài dài gần một nghìn ba trăm chữ, có hai tiêu đề nhỏ.",
         F(0, "Thầy chia bài thành mười lăm đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
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

add("bullets", chapter="Bố cục & ghi chú", section="Bài khóa 课文", title="Bố cục bài khóa", size=34,
    items=["## 1. Mở đầu: nghề mới ra đời (đoạn 1–2)",
           "IG vô địch thế giới → 打游戏原来也是职业 · 伴随改革开放、互联网飞速发展 → 新职业应运而生",
           "## 2. 没有找不到，只有想不到 (đoạn 3–8)",
           "Sau một buổi livestream: 灯光师、试吃官、经纪人…… · 旅游定制 · thu nhập 水涨船高、赶超白领",
           "## 3. 在传统和新兴之间抉择 (đoạn 9–14)",
           "Bố mẹ muốn “铁饭碗” · 95后 mơ làm 网红、配音员…… · 65.70% muốn thành 行业顶尖, chỉ 1.13% muốn 转行",
           "## 4. Kết luận (đoạn 15)",
           "互联网领域必将成为催生新职业的土壤"],
    say=["Trước khi sang phần mẫu câu, chúng ta cùng nhìn lại bố cục bài khóa. Đây là một bài báo tin tức kết hợp bình luận, có bốn phần.",
         F(1, "Phần một, mở đầu: đội IG vô địch thế giới khiến mọi người vỡ lẽ chơi game cũng là một nghề. Cùng với cải cách mở cửa và sự phát triển của internet, nghề mới đã thuận thời mà ra đời."),
         F(3, "Phần hai, với tiêu đề 没有找不到，只有想不到: đằng sau mỗi buổi livestream là cả một đội ngũ nghề mới; có người bán cẩm nang du lịch; và thu nhập của người làm nghề mới đã vượt cả dân văn phòng."),
         F(5, "Phần ba, với tiêu đề 在传统和新兴之间抉择: bố mẹ vẫn muốn con có bát cơm sắt, nhưng thế hệ sau chín mươi lăm lại mơ làm người nổi tiếng trên mạng, diễn viên lồng tiếng; phần lớn họ muốn gắn bó lâu dài với nghề mới, rất ít người muốn chuyển nghề."),
         F(7, "Phần bốn, kết luận: lĩnh vực internet nhất định sẽ trở thành mảnh đất sinh ra những nghề mới. Đây chính là câu trả lời cho tên bài: ai dám theo sở thích và nắm bắt cơ hội, người đó sẽ đứng ở đầu ngọn gió.")])

add("bullets", section="Bài khóa 课文", title="Ghi chú 注释: hiểu thêm về bối cảnh", size=33,
    items=["IG战队: CLB thể thao điện tử Invictus Gaming, do 王思聪 (con trai 王健林, chủ tịch Wanda) lập năm 2011; vô địch LMHT thế giới 2018",
           "发烧友: vốn là cách gọi người mê thiết bị âm thanh ở Hồng Kông, nay chỉ người mê một thứ gì đó: 电影发烧友 · 手机发烧友",
           "自媒体 (We Media): cá nhân tự đăng nội dung qua internet; từ 2015 livestream, video ngắn bùng nổ – cũng có nhiều thông tin thật giả lẫn lộn",
           "直播带货: livestream bán hàng trên Taobao, JD, Douyin…; 李佳琦 “口红一哥”: 5 phút bán 15.000 thỏi son; 薇娅 doanh số 29 tỷ tệ năm 2019, cuối 2021 bị phạt vì trốn thuế"],
    say=["Sách có bốn ghi chú giúp hiểu thêm bối cảnh bài khóa.",
         F(0, "Một: IG战队, câu lạc bộ thể thao điện tử Invictus Gaming. Năm hai nghìn không trăm mười một, 王思聪, con trai của 王健林, chủ tịch tập đoàn Vạn Đạt, tuyên bố bước vào lĩnh vực thể thao điện tử và lập ra câu lạc bộ này. Năm hai nghìn không trăm mười tám, IG vô địch thế giới Liên Minh Huyền Thoại."),
         F(1, "Hai: 发烧友. Từ này bắt nguồn từ Hồng Kông, vốn để gọi những người mê thiết bị âm thanh, sau mở rộng chỉ những người đặc biệt say mê một thứ gì đó, như 电影发烧友, người mê phim; 手机发烧友, người mê điện thoại."),
         F(2, "Ba: 自媒体, truyền thông cá nhân, tiếng Anh là We Media: cá nhân dùng nền tảng internet để đăng ý kiến, quan điểm của mình. Từ năm hai nghìn không trăm mười lăm, livestream và video ngắn trở thành điểm nóng. Truyền thông cá nhân rất có sức ảnh hưởng, nhưng cũng có vấn đề thông tin thật giả lẫn lộn, nên chính phủ Trung Quốc đã nhiều lần chấn chỉnh."),
         F(3, "Bốn: 直播带货, livestream bán hàng trên các sàn như Taobao, JD, hay các nền tảng như Douyin. 李佳琦 được gọi là 口红一哥, ông hoàng son môi, từng bán mười lăm nghìn thỏi son trong năm phút. 薇娅 đạt doanh số hai mươi chín tỷ tệ năm hai nghìn không trăm mười chín, nhưng cuối năm hai nghìn không trăm hai mươi mốt bị truy thu và phạt tổng cộng hơn mười ba tỷ tệ vì trốn thuế.")])

# ======================= MẪU CÂU =======================
add("bullets", chapter="Mẫu câu: 一时间 · 所谓的 · 顺着 · 渐成风气", section="Mẫu câu 重点句型", title="1. 一时间…… · 3. 顺着……", size=33,
    items=["## 一时间: trong chốc lát, nhất thời, bỗng chốc",
           "一时间，电竞职业选手也成为了媒体争相报道的话题——打游戏原来也是职业!",
           "几个孩子打篮球不小心打碎了邻居家玻璃，一时间他们面面相觑不知该怎么办。",
           "这件事情真是复杂，千头万绪的，一时间我也说不清楚。",
           "## 顺着: giới từ – dọc theo (đường đi); theo, dựa theo (hướng suy nghĩ)",
           "顺着这个思路，四川姑娘韩小清选择在网络上向游客出售旅游攻略。",
           "我们就顺着这条路走，走到哪儿算哪儿。",
           "孩子不可能一直顺着父母规划好的路线成长，他们也需要自由的发展空间。"],
    say=["Bây giờ chúng ta sang phần mẫu câu và từ ngữ trọng điểm. Bài này có mười điểm, thầy gộp mỗi slide hai điểm. Đầu tiên là 一时间 và 顺着.",
         F(0, "一时间 nghĩa là trong một thời gian rất ngắn, trong chốc lát, bỗng chốc. Nó thường đứng đầu câu, diễn tả một sự thay đổi xảy ra rất nhanh, hoặc một trạng thái nhất thời."),
         F(1, "Ví dụ từ bài khóa: 一时间，电竞职业选手也成为了媒体争相报道的话题。 Bỗng chốc, tuyển thủ thể thao điện tử trở thành đề tài báo chí đua nhau đưa tin."),
         F(2, "几个孩子打篮球不小心打碎了邻居家玻璃，一时间他们面面相觑不知该怎么办。 Mấy đứa trẻ chơi bóng rổ lỡ làm vỡ kính nhà hàng xóm, nhất thời chúng nhìn nhau không biết phải làm sao. 面面相觑 là nhìn nhau ngơ ngác."),
         F(3, "这件事情真是复杂，千头万绪的，一时间我也说不清楚。 Chuyện này thật phức tạp, rối như tơ vò, nhất thời tôi cũng không nói rõ được. 千头万绪 là nghìn đầu vạn mối."),
         F(4, "顺着 là giới từ, có hai nghĩa: dọc theo, men theo một con đường; và theo, dựa theo một hướng, một ý muốn nào đó."),
         F(5, "Ví dụ từ bài khóa: 顺着这个思路，四川姑娘韩小清选择在网络上向游客出售旅游攻略。 Theo hướng suy nghĩ này, cô gái Tứ Xuyên Hàn Tiểu Thanh chọn bán cẩm nang du lịch trên mạng."),
         F(6, "我们就顺着这条路走，走到哪儿算哪儿。 Chúng ta cứ đi dọc con đường này, đi tới đâu hay tới đó."),
         F(7, "孩子不可能一直顺着父母规划好的路线成长，他们也需要自由的发展空间。 Con cái không thể mãi lớn lên theo con đường bố mẹ vạch sẵn, chúng cũng cần không gian phát triển tự do.")])

add("bullets", section="Mẫu câu 重点句型", title="2. 所谓的……，只是……而已 · 4. ……渐成风气", size=33,
    items=["## 所谓的……，只是……而已: cái gọi là… chẳng qua chỉ là… mà thôi (hạ thấp, cho là không có gì to tát)",
           "所谓的“新”职业，也只是……将人们的各种诉求细分出来的结果而已。",
           "哪有什么仙人仙境，所谓的“海市蜃楼”，只是一种光学现象而已。",
           "所谓的“不能让孩子输在起跑线上”，很多时候只是家长们的焦虑而已。",
           "## ……渐成风气: dần dần thịnh hành, dần thành phong trào (làm vị ngữ)",
           "这样的私人定制服务近来渐成风气。",
           "本世纪以来，年轻人的择业观念发生了很大的变化，自主创业渐成风气。",
           "近年来，由于垃圾分类投放渐成风气，古城拉萨的环境有了明显的改善。"],
    say=["Tiếp theo là 所谓的，只是，而已, và 渐成风气.",
         F(0, "Ở bài sáu chấm một, chúng ta đã học 所谓是指 để định nghĩa một khái niệm. Còn 所谓的, chẳng qua chỉ là, mà thôi, lại mang ý hạ thấp: người nói cho rằng khái niệm ấy nghe thì to tát, thực ra chẳng có gì đặc biệt.",
           cap="Ở bài 6.1, chúng ta đã học 所谓……是指…… để định nghĩa một khái niệm. Còn 所谓的……，只是……而已 lại mang ý hạ thấp: người nói cho rằng khái niệm ấy nghe thì to tát, thực ra chẳng có gì đặc biệt."),
         F(1, "Ví dụ từ bài khóa: 所谓的新职业，也只是在这个需求高度分众化、个性化的时代，将人们的各种诉求细分出来的结果而已。 Nghề mới chẳng qua chỉ là kết quả của việc tách nhỏ nhu cầu mà thôi."),
         F(2, "哪有什么仙人仙境，所谓的海市蜃楼，只是一种光学现象而已。 Làm gì có tiên nhân tiên cảnh, cái gọi là ảo ảnh lâu đài trên biển chẳng qua chỉ là một hiện tượng quang học mà thôi."),
         F(3, "所谓的不能让孩子输在起跑线上，很多时候只是家长们的焦虑而已。 Cái gọi là không để con thua ngay từ vạch xuất phát, nhiều khi chẳng qua chỉ là nỗi lo của phụ huynh mà thôi."),
         F(4, "渐成风气 nghĩa là dần dần trở thành phong trào, trở nên thịnh hành. Cụm này thường làm vị ngữ, đứng sau chủ ngữ là một hiện tượng, một việc làm."),
         F(5, "Ví dụ từ bài khóa: 这样的私人定制服务近来渐成风气。 Dịch vụ thiết kế riêng như vậy gần đây dần thành phong trào."),
         F(6, "本世纪以来，年轻人的择业观念发生了很大的变化，自主创业渐成风气。 Từ đầu thế kỷ này, quan niệm chọn nghề của giới trẻ đã thay đổi rất nhiều, tự khởi nghiệp dần thành phong trào."),
         F(7, "近年来，由于垃圾分类投放渐成风气，古城拉萨的环境有了明显的改善。 Những năm gần đây, nhờ việc phân loại rác dần thành nếp, môi trường cố đô Lhasa đã cải thiện rõ rệt.")])

add("bullets", chapter="Mẫu câu: 呈现…态势 · 难关 · 相去甚远 · 尤以…为最", section="Mẫu câu 重点句型", title="5. 呈现……态势 · 6. 过一道难关 / 渡过……", size=33,
    items=["## 呈现……态势: cho thấy xu thế… (稳定发展 · 上涨 · 加速发展 · 下降…)",
           "《报告》显示，新职业人群……收入呈现出稳步上涨的态势，已经赶超普通白领收入水平。",
           "当地经济增长呈现加速发展态势，2025年国民生产总值有望翻一番。",
           "报道指出，2010年至今，上海的房地产业一直呈现健康稳定发展的态势。",
           "## 过一道难关 / 渡过……: vượt qua khó khăn như qua một cửa ải; 渡 = vượt qua",
           "选择从事新职业，能得到父母理解是很多人必须要过的一道难关。",
           "我们一家人相互扶持，渡过了一个又一个难关。",
           "真正的朋友……会坚强的陪你闯过一道又一道难关。"],
    say=["Tiếp theo là 呈现态势 và 过一道难关.",
         F(0, "呈现什么态势 nghĩa là cho thấy, thể hiện xu thế nào đó, như ổn định, tăng lên, phát triển nhanh, giảm xuống. Đây là mẫu câu rất hay gặp trong tin tức kinh tế, xã hội."),
         F(1, "Ví dụ từ bài khóa: 报告显示，新职业人群收入呈现出稳步上涨的态势，已经赶超普通白领收入水平。 Thu nhập cho thấy xu thế tăng đều đặn."),
         F(2, "当地经济增长呈现加速发展态势，二零二五年国民生产总值有望翻一番。 Tăng trưởng kinh tế địa phương cho thấy xu thế tăng tốc, năm hai nghìn không trăm hai mươi lăm tổng sản phẩm quốc dân có triển vọng tăng gấp đôi. 翻一番 là tăng gấp đôi."),
         F(3, "报道指出，二零一零年至今，上海的房地产业一直呈现健康稳定发展的态势。 Bài báo chỉ ra, từ năm hai nghìn không trăm mười đến nay, ngành bất động sản Thượng Hải luôn cho thấy xu thế phát triển lành mạnh, ổn định."),
         F(4, "过一道难关 là vượt qua một cửa ải khó khăn; 道 là lượng từ. Chữ 关 là cửa ải, nên khắc phục khó khăn được ví như đi qua một cửa ải. Ngoài 过, còn dùng 渡过, nghĩa là vượt qua, và 闯过, nghĩa là xông qua."),
         F(5, "Ví dụ từ bài khóa: 选择从事新职业，能得到父母理解是很多人必须要过的一道难关。"),
         F(6, "我们一家人相互扶持，渡过了一个又一个难关。 Cả nhà chúng tôi nương tựa vào nhau, vượt qua hết khó khăn này đến khó khăn khác."),
         F(7, "真正的朋友绝对不会在你困难的时候离你而去，会坚强的陪你闯过一道又一道难关。 Người bạn thật sự không bao giờ bỏ bạn lúc khó khăn, mà sẽ kiên cường cùng bạn vượt qua hết cửa ải này đến cửa ải khác. Câu này sách viết 坚强的, theo chuẩn thì nên viết 坚强地 vì làm trạng ngữ.")])

add("bullets", section="Mẫu câu 重点句型", title="7. 和……相去甚远 / 相去不远 · 8. 尤以……为最", size=33,
    items=["## 和……相去甚远 / 相去不远: cách rất xa, khác rất xa / không cách xa mấy",
           "“95后”最向往的职业……已经和父母传统观念中的公务员、教师、国企职员等“好工作”相去甚远。",
           "公司今年最终的营业收入约为35亿元，这一数据与我们100亿元目标相去甚远。",
           "虽然是初次见面，但是两人一见如故，都觉得眼前的人和自己的想象相去不远。",
           "## 尤以……为最: trong số đó, nổi bật nhất / nhiều nhất là…",
           "“95后”选择创业的人群中，……尤以北、深、广三地的毕业生为最。",
           "今年以来，各地日用消费品纷纷降价，其中尤以家电为最。"],
    say=["Tiếp theo là 相去甚远 và 尤以为最.",
         F(0, "和什么相去甚远 nghĩa là cách rất xa, khác rất xa so với cái gì; 相去 là cách nhau, 甚 là rất. Ngược lại, 相去不远 là không cách xa mấy, gần giống. Có thể dùng 和 hoặc 与."),
         F(1, "Ví dụ từ bài khóa: 九五后最向往的职业已经和父母传统观念中的公务员、教师、国企职员等好工作相去甚远。"),
         F(2, "按照已完成的销售情况预估，公司今年最终的营业收入约为三十五亿元，这一数据与我们一百亿元目标相去甚远。 Doanh thu năm nay của công ty khoảng ba tỉ rưỡi tệ, còn cách rất xa mục tiêu mười tỉ tệ."),
         F(3, "虽然是初次见面，但是两人一见如故，都觉得眼前的人和自己的想象相去不远。 Tuy là lần đầu gặp, nhưng hai người như quen từ lâu, đều thấy người trước mặt không khác mấy so với tưởng tượng của mình. 一见如故 là mới gặp mà như quen đã lâu."),
         F(4, "尤以什么为最 nghĩa là trong nhiều trường hợp, nổi bật nhất, rõ rệt nhất là cái gì. 尤 là đặc biệt, 最 là nhất. Chữ 为 ở đây đọc wéi."),
         F(5, "Ví dụ từ bài khóa: 九五后选择创业的人群中，百分之四十六的人会选择海淘、自媒体等新兴互联网创业项目，尤以北、深、广三地的毕业生为最。"),
         F(6, "今年以来，各地日用消费品纷纷降价，其中尤以家电为最。 Từ đầu năm đến nay, hàng tiêu dùng ở các nơi đua nhau giảm giá, trong đó nổi bật nhất là đồ điện gia dụng.")])

add("bullets", chapter="Mẫu câu: 以…为导向 · 必将", section="Mẫu câu 重点句型", title="9. 以……为导向/目标/基础/中心 · 10. 必将……", size=33,
    items=["## 以A为B: lấy A làm B (导向 định hướng · 目标 mục tiêu · 基础 nền tảng · 中心 trung tâm)",
           "越来越多的年轻人以兴趣为导向，坚持自我，“初生牛犊不怕虎”。",
           "只有以爱情为基础的婚姻才是合乎道德的。",
           "我们不能以自己为中心，要考虑别人的感受。",
           "## 必将: phó từ – nhất định sẽ, chắc chắn sẽ (văn viết)",
           "……互联网领域必将成为滋生新职业的土壤。",
           "艰苦的时光终将过去，坚强的人必将苦尽甘来。",
           "有些人不求上进，浪费时间，最后必将一事无成。"],
    say=["Hai điểm cuối là mẫu 以为 và phó từ 必将.",
         F(0, "以 A 为 B nghĩa là lấy A làm B. B thường là 导向, định hướng; 目标, mục tiêu; 基础, nền tảng; 中心, trung tâm. Chữ 为 ở đây đọc wéi. Đây là mẫu câu văn viết rất quan trọng."),
         F(1, "Ví dụ từ bài khóa: 越来越多的年轻人以兴趣为导向，坚持自我，初生牛犊不怕虎。 Ngày càng nhiều người trẻ lấy sở thích làm định hướng."),
         F(2, "只有以爱情为基础的婚姻才是合乎道德的。 Chỉ có hôn nhân lấy tình yêu làm nền tảng mới là hợp đạo đức."),
         F(3, "我们不能以自己为中心，要考虑别人的感受。 Chúng ta không thể lấy bản thân làm trung tâm, phải nghĩ đến cảm nhận của người khác."),
         F(4, "必将 là phó từ văn viết, nghĩa là nhất định sẽ, nhấn mạnh một tình huống chắc chắn sẽ xảy ra trong tương lai."),
         F(5, "Ví dụ: 互联网领域必将成为滋生新职业的土壤。 Lĩnh vực internet nhất định sẽ trở thành mảnh đất sinh ra nghề mới. Câu trong sách dùng 滋生, còn bài khóa dùng 催生."),
         F(6, "艰苦的时光终将过去，坚强的人必将苦尽甘来。 Những tháng ngày gian khổ rồi sẽ qua, người kiên cường nhất định sẽ khổ tận cam lai. 苦尽甘来 là hết đắng đến ngọt."),
         F(7, "有些人不求上进，浪费时间，最后必将一事无成。 Có những người không cầu tiến, lãng phí thời gian, cuối cùng nhất định sẽ chẳng làm nên trò trống gì. 一事无成 là chẳng nên việc gì.")])

# ======================= KẾT HỢP TỪ & THÀNH NGỮ =======================
add("bullets", chapter="Kết hợp từ & thành ngữ", section="Kết hợp từ 词语搭配", title="Kết hợp từ: 争相 · 轮番 · 走……", size=34,
    items=["## 争相 + V: ～报道 · ～开放 · ～观看",
           "双十一期间，各电商平台争相降价促销。",
           "## 轮番: ～出动 · ～上场 · ～上阵 · ～上涨",
           "中场过后，我们队的几员大将轮番上阵，比分很快反超。",
           "## 走 + tính từ: ～高 · ～低 · ～红",
           "三季度，……国内物价涨幅持续走低。",
           "张学友的第一张个人专辑……让他的名字在香港歌坛一夜走红。"],
    say=["Tiếp theo là phần kết hợp từ.",
         F(0, "争相 đứng trước động từ: 争相报道, đua nhau đưa tin; 争相开放, đua nhau nở, nói về hoa; 争相观看, đua nhau xem."),
         F(1, "Ví dụ: 双十一期间，各电商平台争相降价促销。 Dịp mười một tháng mười một, các sàn thương mại điện tử đua nhau giảm giá khuyến mãi. 双十一 là ngày độc thân, ngày mua sắm lớn nhất Trung Quốc."),
         F(2, "轮番 đi với 出动, xuất quân; 上场, ra sân; 上阵, ra trận; và 上涨, tăng giá: 轮番上涨, thay nhau tăng giá."),
         F(3, "Ví dụ: 中场过后，我们队的几员大将轮番上阵，比分很快反超。 Sau giờ nghỉ giữa trận, mấy cầu thủ trụ cột của đội ta lần lượt vào sân, tỉ số nhanh chóng bị lật ngược. 大将 ở đây là cầu thủ trụ cột; 反超 là vượt lên dẫn trước."),
         F(4, "走 cộng tính từ chỉ xu hướng: 走高, đi lên; 走低, đi xuống; 走红, trở nên nổi tiếng."),
         F(5, "Ví dụ: 三季度，国民经济继续快速增长，市场物价基本稳定，国内物价涨幅持续走低。 Quý ba, kinh tế tiếp tục tăng nhanh, giá cả cơ bản ổn định, mức tăng giá trong nước liên tục giảm."),
         F(6, "Và: 张学友的第一张个人专辑让他的名字在香港歌坛一夜走红。 Album cá nhân đầu tiên đã giúp Trương Học Hữu nổi tiếng chỉ sau một đêm trên làng nhạc Hồng Kông.")])

add("bullets", section="Thành ngữ 成语和惯用语", title="Thành ngữ (1): 应运而生 · 引人瞩目 · 五湖四海 · 五花八门", size=33,
    items=["## 应运而生 yìngyùn'érshēng – thuận thời mà ra đời, xuất hiện đúng lúc",
           "随着互联网技术的广泛运用，远程诊断治疗应运而生。",
           "## 引人瞩目 yǐnrén-zhǔmù – thu hút sự chú ý của mọi người",
           "宴会上，姐姐一身红色的旗袍十分引人瞩目。",
           "## 五湖四海 wǔhú-sìhǎi – năm hồ bốn biển: khắp mọi miền, khắp thế giới",
           "我们来自五湖四海，为了同一个梦想走到了一起。",
           "## 五花八门 wǔhuā-bāmén – muôn hình muôn vẻ, đủ loại",
           "老师出了一道试题：“诗是什么？”，结果学生的答案五花八门，极为有趣。"],
    say=["Bài này có bảy thành ngữ và quán dụng ngữ. Chúng ta học bốn thành ngữ đầu.",
         F(0, "应运而生: 应 đọc thanh bốn, là thuận theo; 运 là thời vận. Nghĩa gốc là ứng mệnh trời mà sinh ra, nay chỉ thuận theo thời cơ mà ra đời."),
         F(1, "Ví dụ: 随着互联网技术的广泛运用，远程诊断治疗应运而生。 Cùng với việc ứng dụng rộng rãi công nghệ internet, khám chữa bệnh từ xa đã ra đời."),
         F(2, "引人瞩目: 瞩目 là chăm chú nhìn. Nghĩa là thu hút ánh nhìn, sự chú ý của mọi người."),
         F(3, "Ví dụ: 宴会上，姐姐一身红色的旗袍十分引人瞩目。 Trong bữa tiệc, chị tôi mặc bộ sườn xám đỏ rất nổi bật."),
         F(4, "五湖四海: năm hồ bốn biển, chỉ khắp bốn phương, khắp cả nước, có khi là khắp thế giới."),
         F(5, "Ví dụ: 我们来自五湖四海，为了同一个梦想走到了一起。 Chúng ta đến từ khắp mọi miền, vì cùng một ước mơ mà đến với nhau."),
         F(6, "五花八门: vốn là tên hai thế trận cổ có nhiều biến hóa, là 五花阵 và 八门阵; nay ví với muôn hình muôn vẻ, đủ loại."),
         F(7, "Ví dụ: 老师给学生出了一道试题：诗是什么？结果学生的答案五花八门，极为有趣。 Thầy giáo ra một câu hỏi: thơ là gì? Kết quả, câu trả lời của học sinh muôn hình muôn vẻ, cực kỳ thú vị.")])

add("bullets", section="Thành ngữ 成语和惯用语", title="Thành ngữ (2): 应有尽有 · 朝不保夕 · 初生牛犊不怕虎", size=33,
    items=["## 应有尽有 yīngyǒu-jìnyǒu – cái gì cần có đều có, rất đầy đủ",
           "宽阔的大街上车水马龙、百货商店的货物应有尽有……",
           "## 朝不保夕 zhāobùbǎoxī – sớm không biết chiều: tình thế nguy cấp, bấp bênh",
           "我自己现在都朝不保夕，哪有余力来帮助你。",
           "## 初生牛犊不怕虎 – nghé con mới đẻ không sợ hổ: người trẻ dám nghĩ dám làm",
           "他是“初生牛犊不怕虎”，什么事情都想试一试。",
           "中国选手多半是新手，但……又有一股“初生牛犊不怕虎”的劲头，反而取得了很好的成绩。"],
    say=[F(0, "应有尽有: chữ 应 ở đây đọc thanh một, nghĩa là nên, cần. Cái gì cần có đều có cả, chỉ sự đầy đủ, phong phú. Các bạn chú ý: 应运而生 đọc yìng, còn 应有尽有 đọc yīng."),
         F(1, "Ví dụ: 宽阔的大街上车水马龙、百货商店的货物应有尽有。 Trên đại lộ rộng, xe cộ tấp nập như nước chảy, hàng hóa trong cửa hàng bách hóa thì cái gì cũng có."),
         F(2, "朝不保夕: chữ đầu đọc zhāo, là buổi sáng; 夕 là buổi tối. Buổi sáng không dám chắc buổi tối sẽ ra sao, chỉ tình thế nguy cấp, khó lường, bấp bênh."),
         F(3, "Ví dụ: 我自己现在都朝不保夕，哪有余力来帮助你。 Bản thân tôi bây giờ còn sớm không lo được tối, lấy đâu ra sức mà giúp cậu."),
         F(4, "初生牛犊不怕虎: nghé con mới sinh không sợ hổ, vì chưa biết sự lợi hại của hổ. Thường dùng để nói người trẻ ít đắn đo, dám nghĩ dám làm, có khi khen, có khi hàm ý liều lĩnh."),
         F(5, "Ví dụ: 他是初生牛犊不怕虎，什么事情都想试一试。 Cậu ấy đúng là nghé con không sợ hổ, việc gì cũng muốn thử."),
         F(6, "Và: 中国选手多半是新手，但他们训练水平高，又有一股初生牛犊不怕虎的劲头，反而取得了很好的成绩。 Các tuyển thủ Trung Quốc phần lớn là người mới, nhưng tập luyện tốt, lại có khí thế của nghé con không sợ hổ, nên lại đạt thành tích rất tốt.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 课后练习", title="Bài tập 1: Chọn từ điền vào chỗ trống (1)", reveal=True, size=34,
    items=["## 催生 · 规划 · 稳步 · 抉择 · 测评 · 认同 · 顶级",
           "(1) 面对危机，总经理果断的___，给企业带来了发展的新契机。",
           "Đáp án: 抉择",
           "(2) 跨境电商发展迅速，这___了企业对高端电子商务人才的需求。",
           "Đáp án: 催生",
           "(3) 工厂引进新技术和新的管理方法之后，近几个月产品产量___提升。",
           "Đáp án: 稳步",
           "(4) 小米品牌赢得了国内外客户的广泛___，在市场上拥有了相当高的知名度。",
           "Đáp án: 认同"],
    say=["Bây giờ chúng ta sang phần luyện tập của sách. Bài tập một: chọn từ thích hợp điền vào chỗ trống. Có bảy từ: 催生，规划，稳步，抉择，测评，认同，顶级.",
         F(1, "Câu một: 面对危机，总经理果断的什么，给企业带来了发展的新契机。 Trước khủng hoảng, cái gì quả quyết của tổng giám đốc đã mang lại thời cơ phát triển mới cho doanh nghiệp? Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 抉择. 果断的抉择, lựa chọn quả quyết. Ở đây 抉择 là danh từ, đứng sau 的."),
         F(3, "Câu hai: 跨境电商发展迅速，这什么了企业对高端电子商务人才的需求。 Thương mại điện tử xuyên biên giới phát triển nhanh, điều này đã làm gì nhu cầu của doanh nghiệp về nhân tài thương mại điện tử cao cấp?"),
         F(4, "Đáp án: 催生. 催生了需求, làm nảy sinh nhu cầu."),
         F(5, "Câu ba: 工厂引进新技术和新的管理方法之后，近几个月产品产量什么提升。 Sau khi nhà máy áp dụng công nghệ và cách quản lý mới, mấy tháng gần đây sản lượng tăng lên thế nào?"),
         F(6, "Đáp án: 稳步. 稳步提升, tăng đều đặn, 稳步 làm trạng ngữ."),
         F(7, "Câu bốn: 小米品牌赢得了国内外客户的广泛什么，在市场上拥有了相当高的知名度。 Thương hiệu Xiaomi đã giành được sự gì rộng rãi của khách hàng trong và ngoài nước?"),
         F(8, "Đáp án: 认同. 赢得认同, giành được sự công nhận, tán thành. Từ 认同 các bạn đã gặp trong bài khóa, ở cụm 认同感.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 1: Chọn từ điền vào chỗ trống (2)", reveal=True, size=34,
    items=["(5) 在这次鉴定中，多国___专家辛苦工作了一周的时间才下定论，从中我们可以看出专家们的慎重态度。",
           "Đáp án: 顶级",
           "(6) 尽管苹果iPhone新机10月23日才正式开售，但许多媒体已经抢先拿到样机，并对它们进行了___。",
           "Đáp án: 测评",
           "(7) 我们不要把精力全放在微不足道的小事上，而要从大局出发，大处着眼，要有长远___。",
           "Đáp án: 规划"],
    say=[F(0, "Câu năm: 在这次鉴定中，多国什么专家辛苦工作了一周的时间才下定论，从中我们可以看出专家们的慎重态度。 Trong lần giám định này, các chuyên gia thế nào của nhiều nước đã làm việc vất vả suốt một tuần mới đưa ra kết luận."),
         F(1, "Đáp án: 顶级. 顶级专家, chuyên gia hàng đầu. 顶级 là tính từ thuộc tính, đứng ngay trước danh từ."),
         F(2, "Câu sáu: 尽管苹果iPhone新机十月二十三日才正式开售，但许多媒体已经抢先拿到样机，并对它们进行了什么。 Tuy iPhone mới đến ngày hai mươi ba tháng mười mới chính thức mở bán, nhưng nhiều báo chí đã có máy mẫu trước và tiến hành gì?",
           cap="Câu sáu: 尽管苹果iPhone新机10月23日才正式开售，但许多媒体已经抢先拿到样机，并对它们进行了___。 Tuy iPhone mới đến 23/10 mới chính thức mở bán, nhưng nhiều báo chí đã có máy mẫu trước và tiến hành gì?"),
         F(3, "Đáp án: 测评. 进行测评, tiến hành đánh giá, review sản phẩm."),
         F(4, "Câu bảy: 我们不要把精力全放在微不足道的小事上，而要从大局出发，大处着眼，要有长远什么。 Chúng ta đừng dồn hết sức vào những việc nhỏ nhặt, mà phải xuất phát từ đại cục, nhìn vào cái lớn, phải có cái gì lâu dài."),
         F(5, "Đáp án: 规划. 长远规划, kế hoạch lâu dài. 规划 có trong bài khóa: 从路线规划到酒店预订.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn từ thích hợp nhất (1)", reveal=True, size=34,
    items=["(1) 根据客户的“信誉”不同，银行可提供不同额度的信用卡，从千余元的普通卡到数万元的“金卡”，（  ）、品种繁多。 A.应有尽有 B.朝不保夕 C.五湖四海 D.五花八门",
           "Đáp án: D 五花八门 – nhấn mạnh muôn hình muôn vẻ, nhiều loại",
           "(2) 未来一周，大雾、雨雪天气将在我国东部（  ）登场，给公路、民航、铁路等运输行业带来巨大的压力。 A.轮番 B.争相 C.争先 D.顶尖",
           "Đáp án: A 轮番 – thay phiên nhau xuất hiện",
           "(3) 此种创新疗法，可说是完全（  ）了传统的药物治疗，其优势不言而喻。 A.囊括 B.规划 C.海淘 D.颠覆",
           "Đáp án: D 颠覆 – phá vỡ hoàn toàn cái truyền thống"],
    say=["Bài tập hai: chọn từ thích hợp nhất.",
         F(0, "Câu một: 根据客户的信誉不同，银行可提供不同额度的信用卡，从千余元的普通卡到数万元的金卡，什么、品种繁多。 Tùy uy tín của khách hàng, ngân hàng cấp thẻ tín dụng với hạn mức khác nhau, từ thẻ thường hơn một nghìn tệ đến thẻ vàng mấy vạn tệ. A, 应有尽有; B, 朝不保夕; C, 五湖四海; D, 五花八门."),
         F(1, "Đáp án: D, 五花八门. Câu này nhấn mạnh có rất nhiều loại thẻ khác nhau, nên dùng 五花八门, muôn hình muôn vẻ, đi cùng 品种繁多. 应有尽有 nhấn mạnh sự đầy đủ, cần gì có nấy, không hợp bằng."),
         F(2, "Câu hai: 未来一周，大雾、雨雪天气将在我国东部什么登场，给公路、民航、铁路等运输行业带来巨大的压力。 Trong tuần tới, sương mù, mưa tuyết sẽ thế nào xuất hiện ở miền đông. A, 轮番; B, 争相; C, 争先; D, 顶尖."),
         F(3, "Đáp án: A, 轮番. 轮番登场, thay phiên nhau xuất hiện: hết sương mù đến mưa tuyết. 争相 và 争先 đều chỉ người tranh nhau, không dùng cho thời tiết."),
         F(4, "Câu ba: 此种创新疗法，可说是完全什么了传统的药物治疗，其优势不言而喻。 Phương pháp điều trị mới này có thể nói đã hoàn toàn làm gì cách điều trị bằng thuốc truyền thống. A, 囊括; B, 规划; C, 海淘; D, 颠覆."),
         F(5, "Đáp án: D, 颠覆. 颠覆传统, phá vỡ hoàn toàn cái truyền thống. 不言而喻 là không cần nói cũng hiểu.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn từ thích hợp nhất (2)", reveal=True, size=34,
    items=["(4) 热情是强大的动力，能（  ）我们乐观的斗志和顽强的毅力。 A.滋生 B.催生 C.日趋 D.细分",
           "Đáp án: B 催生 – 滋生 thường đi với điều xấu (滋生细菌 · 滋生腐败)",
           "(5) 他知识丰富，能言善辩，是我们班这次辩论比赛的（  ）。 A.主角 B.主力 C.主张 D.主导",
           "Đáp án: B 主力 – lực lượng chủ lực của đội"],
    say=[F(0, "Câu bốn: 热情是强大的动力，能什么我们乐观的斗志和顽强的毅力。 Nhiệt huyết là động lực mạnh mẽ, có thể làm gì ý chí lạc quan và nghị lực bền bỉ của chúng ta. A, 滋生; B, 催生; C, 日趋; D, 细分."),
         F(1, "Đáp án: B, 催生, thúc đẩy nảy sinh. 滋生 cũng là nảy sinh, nhưng thường đi với điều xấu, như 滋生细菌, sinh sôi vi khuẩn; 滋生腐败, nảy sinh tham nhũng. Còn 日趋 là phó từ, 细分 là chia nhỏ, đều không hợp."),
         F(2, "Câu năm: 他知识丰富，能言善辩，是我们班这次辩论比赛的什么。 Cậu ấy kiến thức phong phú, ăn nói giỏi, là gì của lớp chúng tôi trong cuộc thi hùng biện lần này. A, 主角; B, 主力; C, 主张; D, 主导."),
         F(3, "Đáp án: B, 主力, lực lượng chủ lực. 主角 là vai chính trong phim, kịch; 主张 là chủ trương; 主导 là chủ đạo, dẫn dắt.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ ngữ, mẫu câu cho sẵn trả lời câu hỏi", reveal=True, size=32,
    items=["(1) 在你看来，数字经济发展给大学生就业创造了哪些机会？（一时间……）",
           "Đáp án gợi ý: 数字经济催生了主播、短视频博主、游戏测评师等新职业。一时间，这些职业成了很多大学生的热门选择。",
           "(2) 收入是不是左右新职业从业者职业选择的主要因素？（以……为……）",
           "Đáp án gợi ý: 不是。很多新职业从业者以兴趣为导向，“热爱”“有趣”“自由”比收入更重要。",
           "(3) 你们国家的年轻人和上一辈人的就业观一样吗？（和……相去甚远/相去不远）",
           "Đáp án gợi ý: 不一样。很多越南父母希望孩子端“铁饭碗”，而年轻人更喜欢自由的工作，两代人的就业观相去甚远。",
           "(4) 现在大学生选择职业可能会考虑哪些因素？（尤以……为最）",
           "Đáp án gợi ý: 收入、兴趣、发展前景、工作地点等都会考虑，其中尤以发展前景为最。"],
    say=["Bài tập ba: dùng từ ngữ và mẫu câu cho sẵn để trả lời câu hỏi. Đây là câu hỏi mở, cũng là câu hỏi thảo luận; thầy đưa ra đáp án gợi ý, có liên hệ với Việt Nam.",
         F(0, "Câu một: 在你看来，数字经济发展给大学生就业创造了哪些机会？ Theo bạn, sự phát triển của kinh tế số đã tạo ra những cơ hội việc làm nào cho sinh viên? Dùng 一时间."),
         F(1, "Gợi ý: 数字经济催生了主播、短视频博主、游戏测评师等新职业。一时间，这些职业成了很多大学生的热门选择。 Kinh tế số làm nảy sinh những nghề mới như streamer, người làm video ngắn, người review game. Bỗng chốc, những nghề này trở thành lựa chọn hot của nhiều sinh viên."),
         F(2, "Câu hai: 收入是不是左右新职业从业者职业选择的主要因素？ Thu nhập có phải là yếu tố chính chi phối việc chọn nghề của người làm nghề mới không? Dùng 以为. 左右 ở đây là động từ, nghĩa là chi phối."),
         F(3, "Gợi ý: 不是。很多新职业从业者以兴趣为导向，热爱、有趣、自由比收入更重要。 Không phải. Nhiều người làm nghề mới lấy sở thích làm định hướng; đam mê, thú vị, tự do quan trọng hơn thu nhập."),
         F(4, "Câu ba: 你们国家的年轻人和上一辈人的就业观一样吗？ Quan niệm việc làm của giới trẻ nước bạn và thế hệ trước có giống nhau không? Dùng 相去甚远 hoặc 相去不远."),
         F(5, "Gợi ý: 不一样。很多越南父母希望孩子端铁饭碗，而年轻人更喜欢自由的工作，两代人的就业观相去甚远。 Không giống. Nhiều bố mẹ Việt Nam mong con có bát cơm sắt, còn người trẻ thích công việc tự do hơn; quan niệm của hai thế hệ khác nhau rất xa. 端铁饭碗 là bưng bát cơm sắt, tức có việc làm ổn định."),
         F(6, "Câu bốn: 现在大学生选择职业可能会考虑哪些因素？ Sinh viên ngày nay chọn nghề có thể cân nhắc những yếu tố nào? Dùng 尤以为最."),
         F(7, "Gợi ý: 收入、兴趣、发展前景、工作地点等都会考虑，其中尤以发展前景为最。 Thu nhập, sở thích, triển vọng phát triển, nơi làm việc đều được cân nhắc, trong đó nổi bật nhất là triển vọng phát triển.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Chọn từ ngữ, thành ngữ điền vào đoạn văn", reveal=True, size=33,
    items=["## 应运而生 · 飞速 · 朝不保夕 · 颠覆 · 初生牛犊不怕虎 · 导向",
           "近年来，得益于互联网的___发展，都市人消费需求日益多元化，五花八门的新职业___。用老眼光来看，新职业不是“铁饭碗”，而且收入普遍处于中低水平，此类职业___，随时可能失业。然而，……新职业人群的收入也在水涨船高。越来越多的年轻人以兴趣为___，坚持自我，甚至___了职业性别传统，成为新兴职业的主力，可谓是“___”。",
           "Đáp án: 飞速 · 应运而生 · 朝不保夕 · 导向 · 颠覆 · 初生牛犊不怕虎"],
    say=["Bài tập bốn: chọn từ ngữ, thành ngữ điền vào đoạn văn. Có sáu lựa chọn: 应运而生，飞速，朝不保夕，颠覆，初生牛犊不怕虎，导向.",
         F(1, "近年来，得益于互联网的什么发展，都市人消费需求日益多元化，五花八门的新职业什么。用老眼光来看，新职业不是铁饭碗，而且收入普遍处于中低水平，此类职业什么，随时可能失业。然而，新职业人群的收入也在水涨船高。越来越多的年轻人以兴趣为什么，坚持自我，甚至什么了职业性别传统，成为新兴职业的主力，可谓是什么。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 飞速发展；新职业应运而生；此类职业朝不保夕；以兴趣为导向；颠覆了职业性别传统；可谓是初生牛犊不怕虎。"),
         F(2, "Các bạn thấy không, đoạn văn này chính là bản tóm tắt của bài khóa. Gợi ý ngữ pháp: trước 发展 cần một phó từ, nên chọn 飞速; sau 以兴趣为 là 导向; còn 可谓是 thường dẫn ra một câu thành ngữ, tục ngữ để kết luận. Hãy đọc to cả đoạn vài lần nhé.")])

add("bullets", chapter="Liên hệ: “bát cơm sắt” ở Việt Nam", section="Thảo luận 讨论", title="Liên hệ Việt Nam: 铁饭碗 và “vào biên chế”", size=34,
    items=["铁饭碗 bát cơm sắt ≈ “vào biên chế”: công chức, giáo viên, bác sĩ trường công / bệnh viện công",
           "金饭碗 bát cơm vàng: việc vừa ổn định vừa lương cao · 泥饭碗 bát cơm đất: việc bấp bênh, dễ “vỡ”",
           "Nghề mới ở Việt Nam: TikToker · livestream bán hàng · tài xế công nghệ · người review · game thủ chuyên nghiệp",
           "行行出状元: nghề nào cũng có trạng nguyên – làm nghề gì giỏi cũng thành công",
           "Câu hỏi: 兴趣和稳定，你更看重哪一个？为什么？"],
    say=["Trước khi tổng kết, chúng ta cùng liên hệ với Việt Nam.",
         F(0, "铁饭碗 của Trung Quốc rất giống khái niệm vào biên chế của Việt Nam: làm công chức, giáo viên trường công, bác sĩ bệnh viện công, công việc ổn định suốt đời. Nhiều bố mẹ Việt Nam cũng giống bố mẹ của Lưu Hiên trong bài, mong con có một chỗ trong biên chế."),
         F(1, "Người Trung Quốc còn nói 金饭碗, bát cơm vàng, là công việc vừa ổn định vừa lương cao; và 泥饭碗, bát cơm bằng đất, là việc bấp bênh, rơi xuống là vỡ, tức là 朝不保夕."),
         F(2, "Ở Việt Nam, những nghề mới như TikToker, livestream bán hàng, tài xế công nghệ, người review sản phẩm, game thủ chuyên nghiệp cũng đang thu hút rất nhiều người trẻ. Đội tuyển thể thao điện tử Việt Nam cũng đã có những thành tích đáng nể ở đấu trường khu vực."),
         F(3, "Có một câu tục ngữ rất hay: 行行出状元, nghề nào cũng có trạng nguyên. Ý nói làm nghề gì, chỉ cần chăm chỉ và giỏi giang, cũng có thể thành công. Phần ôn tập đơn vị ở bài sau cũng nhắc đến câu này."),
         F(4, "Câu hỏi cho các bạn: 兴趣和稳定，你更看重哪一个？为什么？ Giữa sở thích và sự ổn định, bạn coi trọng điều nào hơn? Vì sao? Hãy thử trả lời bằng tiếng Trung, dùng 以兴趣为导向 hoặc 相去甚远 nhé.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 6.2", size=34,
    items=["Từ vựng trọng tâm: 风口 · 催生 · 顶级 · 流量 · 轮番 · 囊括 · 定制 · 日趋 · 呈现 · 稳步 · 态势 · 抉择 · 考量 · 难关 · 折射 · 转行 · 导向 · 颠覆",
           "Mẫu câu: 一时间 · 所谓的……只是……而已 · 顺着 · 渐成风气 · 呈现……态势 · 过一道难关 · 和……相去甚远 · 尤以……为最 · 以……为导向 · 必将",
           "Thành ngữ: 应运而生 · 引人瞩目 · 五湖四海 · 五花八门 · 应有尽有 · 朝不保夕 · 初生牛犊不怕虎",
           "## Bài tập về nhà",
           "Viết đoạn văn khoảng 300 chữ: 越南的新职业 – nghề mới nào bạn thấy hấp dẫn nhất? Vì sao?"],
    say=["Chúng ta cùng tổng kết bài sáu chấm hai.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 风口，催生，顶级，流量，轮番，囊括，定制，日趋，呈现，稳步，态势，抉择，考量，难关，折射，转行，导向，颠覆. Nhớ cách đọc 考量 và 转行 nhé."),
         F(1, "Về mẫu câu: 一时间 là bỗng chốc; 所谓的只是而已 để hạ thấp một khái niệm; 顺着 là dọc theo, theo; 渐成风气 là dần thành phong trào; 呈现态势 là cho thấy xu thế; 过一道难关 là vượt qua khó khăn; 相去甚远 là khác rất xa; 尤以为最 là nổi bật nhất là; 以为导向 là lấy làm định hướng; và 必将 là nhất định sẽ."),
         F(2, "Về thành ngữ: 应运而生，引人瞩目，五湖四海，五花八门，应有尽有，朝不保夕，初生牛犊不怕虎. Đặc biệt chú ý cách đọc khác nhau của chữ 应 trong 应运而生 và 应有尽有."),
         F(4, "Bài tập về nhà: hãy viết một đoạn văn khoảng ba trăm chữ về chủ đề 越南的新职业, nghề mới ở Việt Nam: nghề mới nào bạn thấy hấp dẫn nhất, vì sao. Hãy dùng ít nhất ba mẫu câu của bài, như 应运而生，以兴趣为导向，和相去甚远."),
         {"t": "Cảm ơn các bạn đã theo dõi bài giảng. Bài sau, bài sáu chấm ba, là bài cuối của Đơn vị sáu: 三十岁的职场姐姐如何乘风破浪？ Các chị ba mươi tuổi nơi công sở vượt sóng thế nào? Chúng ta sẽ bàn về những khó khăn của phụ nữ đi làm: kết hôn, sinh con, phân biệt giới tính khi tuyển dụng, và cân bằng giữa gia đình với sự nghiệp. Hẹn gặp lại các bạn. Chúc các bạn học tốt!",
          "cap": "Cảm ơn các bạn đã theo dõi bài giảng. Bài sau, bài 6.3, là bài cuối của Đơn vị 6: 30 岁的职场姐姐如何乘风破浪？ Các chị 30 tuổi nơi công sở vượt sóng thế nào? Hẹn gặp lại các bạn. Chúc các bạn học tốt!"}])

lesson = {
    "title": "顶石中文 – Bài 6.2: 谁能站在新职业风口？ (Ai đứng được ở đầu ngọn gió nghề nghiệp mới?)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {},
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds62.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
