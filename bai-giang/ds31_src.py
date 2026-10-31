#!/usr/bin/env python3
"""Kịch bản bài giảng 顶石中文 – Bài 3.1 «碳排放的“蛋糕”怎么切？». Chạy để sinh ds31.json."""
import json
import os

TAG = "顶石中文 · Bài 3.1 · 碳排放的“蛋糕”怎么切？"
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
    zh="碳排放的“蛋糕”怎么切？", py="Tàn páifàng de “dàngāo” zěnme qiē?",
    vi="Bài 3.1: Chia “chiếc bánh” phát thải carbon thế nào?",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng giáo trình 顶石中文, Đỉnh cao tiếng Trung.",
         "Hôm nay chúng ta bước sang Đơn vị ba: 环保篇, chủ đề Bảo vệ môi trường. Bài đầu tiên của đơn vị là bài ba chấm một: 碳排放的蛋糕怎么切？ Nghĩa là: Chia chiếc bánh phát thải carbon thế nào?",
         "Bài khóa trích từ một cuộc phỏng vấn của Đài truyền hình Trung ương Trung Quốc năm 2010, sau Hội nghị thượng đỉnh về biến đổi khí hậu ở Copenhagen. Người trả lời phỏng vấn là viện sĩ 丁仲礼, Đinh Trọng Lễ. Ông ví tổng lượng khí cacbonic mà cả thế giới còn được phép thải ra như một chiếc bánh ngọt có hạn: chia thế nào mới là công bằng?",
         "Đây là một bài nghị luận dưới dạng đối thoại, có rất nhiều từ ngữ chính luận như 减排，共识，配额，公允. Học xong bài này, các bạn sẽ có đủ vốn từ để bàn về biến đổi khí hậu bằng tiếng Trung."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học", size=40,
    items=["Hiểu bài phỏng vấn: vì sao quyền phát thải là quyền phát triển, thế nào là chia “chiếc bánh” công bằng",
           "Nắm vững 45 từ mới (có 5 thành ngữ), kèm âm Hán Việt và ví dụ",
           "8 mẫu câu: 就…… · 简单一句话 · 进一步 · 也就是说 · 有失…… · 把……视为…… · 有的是 · 取决于",
           "Kết hợp từ: 应对 · 尾声 · 共识 · 尖锐 · 实质 · 落实",
           "Làm bài tập của sách; thảo luận: Việt Nam và mục tiêu trung hòa carbon"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài phỏng vấn: vì sao ông Đinh Trọng Lễ cho rằng quyền phát thải chính là quyền phát triển, và theo ông, chia chiếc bánh phát thải thế nào mới công bằng."),
         F(1, "Thứ hai, nắm vững bốn mươi lăm từ mới, trong đó có năm thành ngữ. Với mỗi từ, thầy sẽ đọc mẫu, cho âm Hán Việt, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học tám mẫu câu trọng điểm của sách: 就, 简单一句话，进一步，也就是说，有失公允，把什么视为什么，有的是, và 取决于."),
         F(3, "Thứ tư, học cách kết hợp của sáu từ quan trọng: 应对，尾声，共识，尖锐，实质，落实."),
         F(4, "Thứ năm, làm các bài tập của sách, và cùng thảo luận: Việt Nam đang ứng phó với biến đổi khí hậu như thế nào."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= CÂU HỎI KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 课前思考", title="Câu hỏi khởi động 课前思考", size=36,
    items=["1．你了解碳排放吗？",
           "Phát thải carbon: khí CO2 thải ra khi đốt than, dầu, khí đốt… → gây hiệu ứng nhà kính",
           "2．全球气候变暖真的有那么大危害吗？人类对此是否反应过度了？",
           "Việt Nam: một trong những nước chịu ảnh hưởng nặng nhất (nước biển dâng, xâm nhập mặn ở đồng bằng sông Cửu Long)",
           "3．你认为全面禁止燃油车生产可行吗？",
           "Nhiều nước đặt lộ trình dừng bán xe chạy xăng; Hà Nội có lộ trình hạn chế xe máy chạy xăng ở nội đô"],
    say=["Trước khi vào bài, sách đưa ra ba câu hỏi để chúng ta suy nghĩ. Các bạn hãy tạm dừng video và thử trả lời bằng tiếng Trung nhé.",
         F(0, "Câu một: 你了解碳排放吗？ Bạn có hiểu về phát thải carbon không?"),
         F(1, "碳排放 là phát thải carbon, chủ yếu là khí cacbonic thải ra khi con người đốt than, dầu mỏ, khí đốt để sản xuất điện, chạy xe, vận hành nhà máy. Khí này giữ nhiệt trong khí quyển, gây ra hiệu ứng nhà kính."),
         F(2, "Câu hai: 全球气候变暖真的有那么大危害吗？人类对此是否反应过度了？ Trái đất nóng lên có thật sự nguy hại đến thế không? Liệu loài người có đang phản ứng thái quá không?"),
         F(3, "Với người Việt Nam, câu trả lời khá rõ: nước ta là một trong những quốc gia chịu ảnh hưởng nặng nề nhất của biến đổi khí hậu, với bão lũ thất thường, nước biển dâng, xâm nhập mặn ở đồng bằng sông Cửu Long. Các bạn có thể nói: 越南是受气候变化影响最严重的国家之一。"),
         F(4, "Câu ba: 你认为全面禁止燃油车生产可行吗？ Bạn có cho rằng cấm hoàn toàn việc sản xuất xe chạy bằng nhiên liệu xăng dầu là khả thi không? 燃油车 là xe chạy xăng dầu, đối lập với 电动车, xe điện."),
         F(5, "Nhiều nước đã đặt lộ trình dừng bán ô tô chạy xăng. Ở Việt Nam, Hà Nội cũng đã có lộ trình hạn chế xe máy chạy xăng trong khu vực nội đô. Theo các bạn, việc này khó ở chỗ nào? Hãy giữ câu trả lời của mình, cuối bài chúng ta sẽ quay lại thảo luận.")])

add("bullets", section="Khởi động 课前思考", title="Bối cảnh bài khóa (theo phần 注释)", size=34,
    items=["## 联合国气候变化大会 – Hội nghị Liên Hợp Quốc về biến đổi khí hậu (COP)",
           "Họp mỗi năm từ 1995 · 1997: 《京都议定书》 Nghị định thư Kyoto · 2007: 《巴厘岛路线图》",
           "2009 Copenhagen: kết quả ít ỏi, chỉ có 《哥本哈根协议》 không ràng buộc pháp lý · 2015: 《巴黎协定》 Thỏa thuận Paris",
           "## 丁仲礼 Dīng Zhònglǐ – Đinh Trọng Lễ",
           "Chuyên gia cổ sinh vật học và địa tầng học, viện sĩ Viện Khoa học Trung Quốc",
           "## G8 – Nhóm tám nước công nghiệp: Mỹ, Anh, Pháp, Đức, Nhật, Ý, Canada, Nga (Nga bị đình chỉ năm 2014)"],
    say=["Để hiểu bài khóa, chúng ta cần biết một chút bối cảnh, theo phần chú thích của sách.",
         F(0, "联合国气候变化大会, Hội nghị Liên Hợp Quốc về biến đổi khí hậu, thường gọi tắt là COP. Bài khóa gọi nó là 联合国气候变化峰会, hội nghị thượng đỉnh."),
         F(1, "Hội nghị họp mỗi năm một lần từ năm 1995, luân phiên ở các nơi trên thế giới. Năm 1997 ở Kyoto, Nhật Bản, thông qua 京都议定书, Nghị định thư Kyoto. Năm 2007 ở Bali, Indonesia, thông qua 巴厘岛路线图, Lộ trình Bali."),
         F(2, "Năm 2009, hội nghị ở Copenhagen đạt rất ít kết quả, cuối cùng chỉ có 哥本哈根协议, Hiệp định Copenhagen, không có tính ràng buộc pháp lý. Đến năm 2015, gần hai trăm bên tham gia đã thông qua 巴黎协定, Thỏa thuận Paris, sắp xếp hành động chung của thế giới sau năm 2020."),
         F(3, "Nhân vật chính của bài là 丁仲礼, Đinh Trọng Lễ."),
         F(4, "Ông là chuyên gia cổ sinh vật học và địa tầng học của Viện Địa chất, Viện Khoa học Trung Quốc, là viện sĩ của viện này. Vì nghiên cứu khí hậu trái đất suốt hàng trăm triệu năm, ông có cái nhìn rất khác về chuyện trái đất nóng lên."),
         F(5, "Cuối cùng là G8, nhóm tám nước công nghiệp lớn: Mỹ, Anh, Pháp, Đức, Nhật Bản, Ý, Canada và Nga. Năm 2014, tư cách thành viên của Nga bị đình chỉ, nhóm trở lại là G7.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("举世瞩目", "jǔshì-zhǔmù", "cử thế chúc mục", "thành ngữ", "được cả thế giới chú ý", "人类登月是一个举世瞩目的成就。", "Con người đặt chân lên Mặt Trăng là một thành tựu cả thế giới dõi theo.",
     "Thành ngữ. 举世 là cả thế gian, 瞩目 là dõi mắt nhìn: cả thế giới đều dõi theo. Câu mở đầu bài khóa: 举世瞩目的联合国气候变化峰会, hội nghị thượng đỉnh về biến đổi khí hậu được cả thế giới chú ý. Chữ 瞩 đọc thanh ba, đừng nhầm với chữ 嘱 trong 嘱咐."),
    ("峰会", "fēnghuì", "phong hội", "danh từ", "hội nghị thượng đỉnh", "各国领导人出席了这次峰会。", "Lãnh đạo các nước đã tham dự hội nghị thượng đỉnh lần này.",
     "Danh từ, nghĩa là hội nghị thượng đỉnh, hội nghị cấp cao nhất. Chữ 峰 là đỉnh núi, như trong 高峰. Đây là từ thầy bổ sung, không có trong bảng từ của sách, nhưng xuất hiện ngay câu đầu bài khóa."),
    ("商定", "shāngdìng", "thương định", "động từ", "bàn bạc và quyết định, thỏa thuận", "我们应当共同商定处理办法。", "Chúng ta nên cùng nhau bàn bạc quyết định cách xử lý.",
     "Động từ, nghĩa là bàn bạc rồi đi đến quyết định. 商 là bàn bạc, như trong 商量; 定 là quyết định. Khác với 商量 chỉ là bàn bạc, 商定 nhấn mạnh đã có kết quả. Trong bài: 商定下一步温室气体减排的方案, thống nhất phương án giảm phát thải khí nhà kính cho bước tiếp theo."),
    ("温室", "wēnshì", "ôn thất", "danh từ", "nhà kính", "二氧化碳是一种温室气体。", "Khí cacbonic là một loại khí nhà kính.",
     "Danh từ, nghĩa gốc là căn phòng ấm, nhà kính trồng cây; nay hay dùng khi nói về trái đất nóng lên: 温室气体, khí nhà kính; 温室效应, hiệu ứng nhà kính. Nghĩa bóng: 温室里的花朵, bông hoa trong nhà kính, chỉ đứa trẻ được nuông chiều."),
    ("减排", "jiǎnpái", "giảm bài", "động từ", "giảm phát thải", "节能减排是每个人的责任。", "Tiết kiệm năng lượng, giảm phát thải là trách nhiệm của mỗi người.",
     "Động từ, nói gọn của 减少排放, tức là giảm lượng chất độc hại thải ra, đặc biệt là giảm phát thải khí cacbonic. Cụm cố định rất hay gặp: 节能减排, tiết kiệm năng lượng và giảm phát thải."),
    ("应对", "yìngduì", "ứng đối", "động từ", "ứng phó, đối phó", "我们要制定应对危机的措施。", "Chúng ta phải đề ra biện pháp ứng phó với khủng hoảng.",
     "Động từ, nghĩa là áp dụng biện pháp để ứng phó với tình huống xảy ra. Chữ đầu đọc thanh bốn. Trong bài: 应对气候变化, ứng phó với biến đổi khí hậu. Lát nữa chúng ta sẽ học các kết hợp của nó: 应对问题，应对挑战，应对风险."),
    ("协议", "xiéyì", "hiệp nghị", "danh từ", "hiệp định, thỏa thuận", "双方终于签订了合作协议。", "Hai bên cuối cùng đã ký thỏa thuận hợp tác.",
     "Danh từ, nghĩa là bản thỏa thuận, hiệp định giữa các bên. Động từ hay đi kèm là 达成 và 签订: 达成协议, đạt được thỏa thuận; 签订协议, ký kết hiệp định. Trong bài: 达成一项新协议, đạt được một hiệp định mới. Đây cũng là từ bổ sung."),
    ("历时", "lìshí", "lịch thời", "động từ", "kéo dài, trải qua (bao lâu)", "这场战争历时三年。", "Cuộc chiến tranh này kéo dài ba năm.",
     "Động từ, nghĩa là sự việc kéo dài, trải qua bao nhiêu thời gian, văn viết. Phía sau thường là một khoảng thời gian. Trong bài: 历时近两周的会议, hội nghị kéo dài gần hai tuần."),
    ("硝烟四起", "xiāoyān sìqǐ", "tiêu yên tứ khởi", "thành ngữ", "khói súng nổi khắp nơi; căng thẳng như chiến trận", "法庭上，双方唇枪舌剑，可谓硝烟四起。", "Tại phiên tòa, hai bên đấu khẩu gay gắt, có thể nói là khói lửa mịt mù.",
     "Thành ngữ. 硝烟 là khói thuốc súng, 四起 là nổi lên bốn phía: chỉ bầu không khí căng thẳng khi chiến tranh nổ ra hoặc sắp nổ ra. Trong bài dùng theo nghĩa bóng: hội nghị tranh cãi rất kịch liệt, không khí như chiến trường."),
    ("喧嚣", "xuānxiāo", "huyên hiêu", "tính từ", "ồn ào, náo động, huyên náo", "他想远离城市的喧嚣。", "Anh ấy muốn tránh xa sự ồn ào của thành phố.",
     "Tính từ, nghĩa là âm thanh hỗn tạp, ồn ào, không yên tĩnh; cũng dùng như danh từ: 城市的喧嚣, sự ồn ào của đô thị. Trong bài: 一片喧嚣, cả một vùng ồn ào náo động."),
    ("尾声", "wěishēng", "vĩ thanh", "danh từ", "phần cuối, giai đoạn kết thúc", "比赛已经接近尾声。", "Trận đấu đã gần đến hồi kết.",
     "Danh từ, nghĩa là phần cuối cùng của một sự việc. Âm Hán Việt vĩ thanh, giống tiếng Việt gọi phần kết của một tác phẩm. Hay đi với 接近，进入，临近: 接近尾声, gần đến hồi kết."),
    ("共识", "gòngshí", "cộng thức", "danh từ", "nhận thức chung, sự đồng thuận", "经过多次讨论，双方达成了共识。", "Sau nhiều lần thảo luận, hai bên đã đạt được sự đồng thuận.",
     "Danh từ, nghĩa là nhận thức chung, ý kiến thống nhất. Kết hợp quan trọng nhất là 达成共识, đạt được đồng thuận. Trong bài, đến tận cuối hội nghị, các đại biểu vẫn 没能达成共识."),
    ("尖锐", "jiānruì", "tiêm nhuệ", "tính từ", "gay gắt; chói tai; sắc bén", "他们之间的矛盾越来越尖锐。", "Mâu thuẫn giữa họ ngày càng gay gắt.",
     "Tính từ, nghĩa gốc là nhọn, sắc. Trong bài dùng theo nghĩa đối lập gay gắt: 尖锐激烈的争吵, cuộc tranh cãi gay gắt, kịch liệt. Ngoài ra còn chỉ âm thanh chói tai, 尖锐的响声; hoặc lời phê bình sắc bén, 尖锐的批评."),
    ("争吵", "zhēngchǎo", "tranh sảo", "động từ", "cãi nhau, tranh cãi", "他们为了一点小事争吵起来。", "Họ cãi nhau chỉ vì một chuyện nhỏ.",
     "Động từ, nghĩa là cãi vã vì ý kiến khác nhau; cũng dùng như danh từ: 引发争吵, gây ra tranh cãi. Trong bài, phóng viên hỏi: 到底在吵什么, rốt cuộc là cãi nhau về cái gì."),
    ("排放", "páifàng", "bài phóng", "động từ", "thải ra, xả ra (khí thải, nước thải)", "工厂不能随便排放污水。", "Nhà máy không được tùy tiện xả nước thải.",
     "Động từ, nghĩa là thải khí thải, nước thải ra môi trường. Hay gặp: 排放污水, xả nước thải; 尾气排放, khí thải xe cộ; 碳排放, phát thải carbon. Đây là từ khóa của cả bài."),
    ("二氧化碳", "èryǎnghuàtàn", "nhị dưỡng hóa thán", "danh từ", "khí CO2, khí cacbonic", "植物吸收二氧化碳，放出氧气。", "Thực vật hấp thụ khí cacbonic, nhả ra khí oxy.",
     "Danh từ, chính là khí CO2, loại khí nhà kính phổ biến nhất. Phân tích từng chữ: 二 là hai, 氧 là oxy, 化 là hóa hợp, 碳 là carbon: hai nguyên tử oxy hóa hợp với carbon."),
    ("实质", "shízhì", "thực chất", "danh từ", "thực chất, bản chất", "我们要看清问题的实质。", "Chúng ta phải nhìn rõ bản chất của vấn đề.",
     "Danh từ, nghĩa là bản chất, cốt lõi. Hay gặp: 问题的实质，实质上，实质性. Trong bài: 这个排放多少，实质又是什么, vậy thực chất của chuyện thải bao nhiêu là gì?"),
    ("能源", "néngyuán", "năng nguyên", "danh từ", "năng lượng, nguồn năng lượng", "我们应该大力发展新能源。", "Chúng ta nên ra sức phát triển năng lượng mới.",
     "Danh từ, chỉ các nguồn có thể sinh ra năng lượng, như than, dầu mỏ, gió, mặt trời. Hay gặp: 化石能源, năng lượng hóa thạch; 新能源, năng lượng mới; 节约能源, tiết kiệm năng lượng. Chú ý: 能源 là nguồn năng lượng, còn 能量 là năng lượng nói chung."),
    ("休戚相关", "xiūqī-xiāngguān", "hưu thích tương quan", "thành ngữ", "vui buồn có nhau, gắn bó mật thiết", "人类身体的健康与环境质量休戚相关。", "Sức khỏe con người gắn bó mật thiết với chất lượng môi trường.",
     "Thành ngữ. 休 là niềm vui, 戚 là nỗi buồn: vui buồn, họa phúc đều liên quan đến nhau, chỉ mối quan hệ cực kỳ mật thiết, cùng chung lợi hại. Trong bài: 和发展问题是休戚相关的, gắn chặt với vấn đề phát triển."),
    ("意味着", "yìwèizhe", "ý vị (trước)", "động từ", "có nghĩa là, đồng nghĩa với", "放弃就意味着失败。", "Bỏ cuộc đồng nghĩa với thất bại.",
     "Động từ, nghĩa là có nghĩa là, hàm ý là, luôn có chữ 着 ở cuối. Trong bài, từ này lặp đi lặp lại: 意味着生活的改善，意味着国家的发展, có nghĩa là cuộc sống được cải thiện, đất nước được phát triển. Từ bổ sung, rất cần cho văn nghị luận."),
    ("设定", "shèdìng", "thiết định", "động từ", "đặt ra, thiết lập", "请你先设定一个密码。", "Bạn hãy đặt một mật khẩu trước đã.",
     "Động từ, nghĩa là thiết lập, xác định: 设定目标, đặt mục tiêu; 设定密码, đặt mật khẩu. Trong bài: 对发达国家设定了减排标准, đặt ra tiêu chuẩn giảm phát thải cho các nước phát triển."),
    ("统统", "tǒngtǒng", "thống thống", "phó từ", "tất cả, toàn bộ, hết thảy", "把这些不愉快的经历统统忘掉吧。", "Hãy quên sạch những trải nghiệm không vui này đi.",
     "Phó từ, nghĩa là toàn bộ, tất cả, giống 全部 và 都, nhấn mạnh không sót cái nào, mang màu sắc khẩu ngữ. Trong bài: 排放总量统统放在八千亿吨这个大盘子里, toàn bộ tổng lượng phát thải đều nằm trong cái đĩa lớn tám trăm tỷ tấn."),
    ("人均", "rénjūn", "nhân quân", "động từ", "bình quân đầu người", "这个城市的人均收入很高。", "Thu nhập bình quân đầu người của thành phố này rất cao.",
     "Động từ, nghĩa là tính bình quân theo đầu người, thường đứng trước danh từ: 人均消费，人均收入，人均排放权. Đây là khái niệm then chốt trong lập luận về công bằng của ông Đinh."),
    ("基数", "jīshù", "cơ số", "danh từ", "con số gốc, mức cơ sở", "中国人口基数大，就业压力也大。", "Trung Quốc có quy mô dân số lớn, áp lực việc làm cũng lớn.",
     "Danh từ, nghĩa là con số dùng làm chuẩn hoặc điểm xuất phát để tính toán. Cẩn thận: tiếng Việt cơ số thường là thuật ngữ toán học; còn 基数 trong báo chí là mức gốc, quy mô ban đầu. Trong bài: 发达国家基数大, mức phát thải gốc của các nước phát triển lớn, nên dù giảm nhiều vẫn còn cao."),
    ("限定", "xiàndìng", "hạn định", "động từ", "hạn chế, quy định giới hạn", "每人限定只能买两张票。", "Mỗi người chỉ được mua tối đa hai vé.",
     "Động từ, nghĩa là quy định phạm vi về thời gian, không gian, số lượng. Trong bài: 对今后的排放进行严格的限定, hạn chế nghiêm ngặt lượng phát thải sau này."),
    ("稀缺", "xīquē", "hi khuyết", "tính từ", "khan hiếm", "水是一种稀缺资源。", "Nước là một loại tài nguyên khan hiếm.",
     "Tính từ, nghĩa là thiếu thốn, hiếm hoi. Hay gặp: 稀缺资源, tài nguyên khan hiếm; 稀缺商品, hàng hóa khan hiếm. Theo bài, khi phát thải bị hạn chế, quyền phát thải sẽ trở thành một thứ hàng hóa khan hiếm."),
    ("不可多得", "bùkě-duōdé", "bất khả đa đắc", "thành ngữ", "hiếm có, khó mà có được", "这是一次不可多得的好机会。", "Đây là một cơ hội tốt hiếm có.",
     "Thành ngữ, nghĩa là rất hiếm, khó có được, thường nói về nhân tài, vật quý hay cơ hội. Trong bài: 非常稀缺的、不可多得的商品, một thứ hàng cực kỳ khan hiếm, khó mà có được."),
    ("配额", "pèi'é", "phối ngạch", "danh từ", "hạn ngạch, định mức được phân", "每个国家都有一定的进口配额。", "Mỗi nước đều có một hạn ngạch nhập khẩu nhất định.",
     "Danh từ, nghĩa là số lượng được phân chia, hạn ngạch. Hay gặp: 进口配额，配额限制. Trong bài: 二氧化碳排放配额, hạn ngạch phát thải khí cacbonic."),
    ("真金白银", "zhēnjīn-báiyín", "chân kim bạch ngân", "thành ngữ", "tiền thật, của thật", "排放指标需要用真金白银来购买。", "Chỉ tiêu phát thải phải bỏ tiền thật ra mà mua.",
     "Thành ngữ gốc khẩu ngữ, nghĩa đen là vàng thật bạc trắng, chỉ tiền bạc, tài sản thật sự. Trong bài, phóng viên chen vào một câu ngắn: 真金白银, tức là phải trả bằng tiền thật đấy."),
    ("余下", "yúxià", "dư hạ", "động từ", "còn lại, còn thừa", "一千元，用去六百，还余下四百。", "Một nghìn tệ, tiêu mất sáu trăm, còn lại bốn trăm.",
     "Động từ, nghĩa là còn lại, thừa ra, giống 剩下 nhưng văn viết hơn. Trong bài: 余下的五十五亿人, năm tỷ rưỡi người còn lại."),
    ("算账", "suànzhàng", "toán trướng", "động từ", "tính toán sổ sách; tính sổ", "我们来算算账，看看这个月花了多少钱。", "Chúng ta tính xem tháng này đã tiêu hết bao nhiêu tiền.",
     "Động từ ly hợp, nghĩa là tính toán sổ sách. Vì là từ ly hợp nên có thể lặp thành 算算账, hoặc tách ra: 算一笔账. Nghĩa bóng là tính sổ, trả đũa ai. Trong bài: 那你算算账, vậy anh thử tính xem."),
    ("公允", "gōngyǔn", "công doãn", "tính từ", "công bằng, thỏa đáng", "这样的评价有失公允。", "Đánh giá như vậy là thiếu công bằng.",
     "Tính từ, nghĩa là công bằng, thỏa đáng, văn viết. Hầu như luôn gặp trong cụm 有失公允 hoặc 欠公允, nghĩa là thiếu công bằng. Trong bài: 是不是有失公允, như thế có phải là thiếu công bằng không?"),
    ("保障", "bǎozhàng", "bảo chướng", "động từ", "bảo đảm, bảo vệ (quyền lợi, an toàn)", "法律保障公民的基本权利。", "Pháp luật bảo đảm các quyền cơ bản của công dân.",
     "Động từ, nghĩa là bảo vệ tính mạng, tài sản, quyền lợi không bị xâm phạm; cũng làm danh từ: 社会保障, an sinh xã hội. Trong bài: 保障发展中国家的发展权利, bảo đảm quyền phát triển của các nước đang phát triển. Phân biệt với 保证, cam đoan, bảo đảm sẽ làm được."),
    ("落实", "luòshí", "lạc thực", "động từ", "thực hiện, triển khai, đưa vào thực tế", "这项计划一定要落实到位。", "Kế hoạch này nhất định phải thực hiện đến nơi đến chốn.",
     "Động từ, nghĩa là làm cho kế hoạch, biện pháp, chính sách được thực hiện thật sự. Hay gặp: 落实计划，落实任务，落实政策. Trong bài: 落实联合国千年发展计划, thực hiện kế hoạch phát triển thiên niên kỷ của Liên Hợp Quốc."),
    ("效应", "xiàoyìng", "hiệu ứng", "danh từ", "hiệu ứng", "温室效应导致全球变暖。", "Hiệu ứng nhà kính dẫn đến trái đất nóng lên.",
     "Danh từ, nghĩa là hiện tượng, kết quả do tác dụng vật lý hay hóa học sinh ra; nay dùng rộng hơn, như 名人效应, hiệu ứng người nổi tiếng. Âm Hán Việt hiệu ứng giống tiếng Việt. Chữ sau đọc thanh bốn."),
    ("演化", "yǎnhuà", "diễn hóa", "động từ", "biến đổi dần, tiến hóa", "地球的气候一直在演化。", "Khí hậu trái đất luôn luôn biến đổi.",
     "Động từ, nghĩa là phát triển, biến đổi qua thời gian dài, thường nói về giới tự nhiên. Gần nghĩa với 进化, tiến hóa, nhưng 演化 trung tính hơn, không nhất thiết là theo hướng tốt lên. Trong bài: 环境气候演化, sự biến đổi của môi trường khí hậu."),
    ("拯救", "zhěngjiù", "chửng cứu", "động từ", "cứu vớt, giải cứu", "朋友们合力把他从破产的边缘拯救过来。", "Bạn bè hợp sức cứu anh ấy khỏi bờ vực phá sản.",
     "Động từ, nghĩa là cứu giúp để thoát khỏi nguy nan, sắc thái trang trọng. Câu nổi tiếng của bài: 这不是人类拯救地球的问题，是人类拯救自己的问题, đây không phải chuyện con người cứu trái đất, mà là chuyện con người tự cứu mình."),
    ("浓度", "nóngdù", "nùng độ", "danh từ", "nồng độ", "空气中二氧化碳的浓度越来越高。", "Nồng độ khí cacbonic trong không khí ngày càng cao.",
     "Danh từ, nghĩa là hàm lượng tương đối của một thành phần, giống tiếng Việt nồng độ. Hay gặp: 高浓度, nồng độ cao; 血糖浓度, nồng độ đường huyết."),
    ("毁灭", "huǐmiè", "hủy diệt", "động từ", "hủy diệt, tiêu diệt hoàn toàn", "战争毁灭了这座古城。", "Chiến tranh đã hủy diệt tòa thành cổ này.",
     "Động từ, nghĩa là tiêu diệt hoàn toàn, giống hệt tiếng Việt hủy diệt. Trong bài: 毁灭的只是物种，毁灭的是人类自己, cái bị hủy diệt chỉ là các loài sinh vật, là chính loài người."),
    ("物种", "wùzhǒng", "vật chủng", "danh từ", "loài (sinh vật)", "大熊猫是珍贵的濒危物种。", "Gấu trúc lớn là loài quý hiếm có nguy cơ tuyệt chủng.",
     "Danh từ, đơn vị cơ bản trong phân loại sinh vật, tức là loài. Chữ sau đọc thanh ba, như trong 种类. Hay gặp: 濒危物种, loài có nguy cơ tuyệt chủng."),
    ("取决", "qǔjué", "thủ quyết", "động từ", "do… quyết định, tùy thuộc vào", "成功与否取决于你自己。", "Thành công hay không là tùy vào chính bạn.",
     "Động từ, nghĩa là do một mặt nào đó quyết định, hầu như luôn đi với 于: A取决于B, A phụ thuộc vào B. Đây là mẫu câu thứ tám của bài."),
    ("包容", "bāoróng", "bao dung", "động từ", "bao dung, khoan dung; dung nạp", "夫妻之间要相互包容。", "Vợ chồng phải bao dung cho nhau.",
     "Động từ, nghĩa là khoan dung, rộng lượng; cũng có nghĩa là chứa đựng, dung nạp. Trong bài: 更具包容性的文明, một nền văn minh có tính bao dung hơn."),
    ("弹性", "tánxìng", "đàn tính", "danh từ", "tính đàn hồi; tính linh hoạt", "很多公司实行弹性工作制。", "Nhiều công ty áp dụng chế độ giờ làm linh hoạt.",
     "Danh từ, nghĩa gốc là tính đàn hồi; nghĩa bóng là tính linh hoạt, có thể điều chỉnh theo thực tế: 弹性工作制, chế độ làm việc linh hoạt. Chữ đầu ở đây đọc tán, khác với cách đọc dàn trong 子弹, viên đạn."),
    ("碳达峰", "tàn dáfēng", "thán đạt phong", "danh từ", "đạt đỉnh phát thải carbon", "很多国家都提出了碳达峰的目标。", "Nhiều nước đã đề ra mục tiêu đạt đỉnh phát thải carbon.",
     "Danh từ, từ bổ sung lấy từ chú thích của bài tập. Nghĩa là đến một thời điểm nào đó, lượng khí cacbonic thải ra không tăng nữa, đạt đỉnh, rồi sau đó giảm dần. 达峰 là đạt đỉnh."),
    ("碳中和", "tàn zhōnghé", "thán trung hòa", "danh từ", "trung hòa carbon, phát thải ròng bằng 0", "实现碳中和需要全社会的共同努力。", "Đạt trung hòa carbon cần sự nỗ lực chung của toàn xã hội.",
     "Danh từ, nghĩa là lượng khí thải do một quốc gia, doanh nghiệp hay cá nhân tạo ra được bù trừ hoàn toàn bằng trồng rừng, tiết kiệm năng lượng, giảm phát thải, đạt mức phát thải ròng bằng không. Việt Nam đã cam kết đạt mục tiêu này vào năm 2050."),
]

add("bullets", chapter="Từ mới (45 từ)", section="Từ mới 生词", title="Phần 1: Từ mới", size=40,
    items=["Bài 3.1 có 35 từ trong bảng từ + 5 thành ngữ (成语) + 5 từ bổ sung = 45 từ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Từ có dấu * trong sách là từ mở rộng, chỉ cần hiểu",
           "Chú ý âm đọc: 应对 / 效应 (yìng) · 物种 (zhǒng) · 弹性 (tán) · 配额 (pèi'é)",
           "Từ dễ nhầm: 基数 · 能源 / 能量 · 保障 / 保证"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bảng từ của sách có ba mươi lăm từ; thầy thêm năm thành ngữ trong phần 成语和惯用语, và năm từ bổ sung rất hay gặp trong bài như 峰会，协议，意味着, cùng hai thuật ngữ 碳达峰，碳中和. Tổng cộng bốn mươi lăm từ, chia thành mười lăm nhóm.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Trong sách, các từ có dấu sao là từ mở rộng, chỉ cần hiểu khi đọc. Tuy vậy, nhiều từ có dấu sao như 减排，稀缺，配额 lại là từ khóa của đề tài môi trường, nên các bạn cố gắng nhớ nhé."),
         F(3, "Chú ý cách đọc của mấy từ có chữ đa âm: 应对，效应，物种，弹性, và 配额. Thầy sẽ nhắc khi gặp từng từ."),
         F(4, "Ngoài ra có mấy từ dễ hiểu nhầm hoặc dễ lẫn, như 基数, phân biệt 能源 với 能量, 保障 với 保证. Các bạn nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

sizes = [3] * 15
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
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung: số viết bằng chữ, bỏ ngoặc kép])
P = [
    ("2009年12月7日，举世瞩目的联合国气候变化峰会在丹麦首都哥本哈根召开，来自192个国家和地区的代表参加了这次大会。国际社会希望在本次大会上商定下一步温室气体减排的方案，就2012到2020年全球应对气候变化问题达成一项新协议。",
     "Ngày 7 tháng 12 năm 2009, Hội nghị thượng đỉnh về biến đổi khí hậu của Liên Hợp Quốc, sự kiện được cả thế giới chú ý, khai mạc tại Copenhagen, thủ đô Đan Mạch, với đại biểu đến từ 192 quốc gia và vùng lãnh thổ. Cộng đồng quốc tế hy vọng hội nghị lần này sẽ thống nhất được phương án giảm phát thải khí nhà kính cho bước tiếp theo, đạt được một hiệp định mới về việc toàn cầu ứng phó với biến đổi khí hậu giai đoạn 2012 đến 2020.",
     ["举世瞩目的 làm định ngữ cho 峰会. 在丹麦首都哥本哈根召开 là khai mạc tại Copenhagen, thủ đô Đan Mạch; 召开 là triệu tập, khai mạc một hội nghị. 来自 là đến từ.",
      "商定方案 là thống nhất phương án. 就……达成一项新协议: giới từ 就 dẫn ra đối tượng, phạm vi của hành động, nghĩa là về vấn đề gì đó mà đạt được một hiệp định mới. Đây là mẫu câu thứ nhất của bài."],
     "二零零九年十二月七日，举世瞩目的联合国气候变化峰会在丹麦首都哥本哈根召开，来自一百九十二个国家和地区的代表参加了这次大会。国际社会希望在本次大会上商定下一步温室气体减排的方案，就二零一二到二零二零年全球应对气候变化问题达成一项新协议。"),
    ("然而在历时近两周的会议中，参会人数已经远远超过了官方注册的一万五千人，会场内外硝烟四起，一片喧嚣，直到接近尾声代表们仍然没能达成共识。",
     "Thế nhưng, trong suốt hội nghị kéo dài gần hai tuần, số người dự họp đã vượt xa con số mười lăm nghìn người đăng ký chính thức; trong và ngoài hội trường không khí căng thẳng như chiến trận, ồn ào náo động, mãi đến khi hội nghị sắp kết thúc, các đại biểu vẫn không đạt được sự đồng thuận.",
     ["历时近两周 là kéo dài gần hai tuần, chữ 近 ở đây là gần, xấp xỉ. 远远超过 là vượt xa. 官方注册 là đăng ký chính thức.",
      "硝烟四起，一片喧嚣 là hai cụm bốn chữ miêu tả không khí: căng thẳng như chiến trường, ồn ào náo loạn. 直到接近尾声，仍然没能达成共识 là mãi đến lúc gần kết thúc vẫn không đạt được đồng thuận. Các từ 接近尾声 và 达成共识 nên học thuộc cả cụm."]),
    ("记者：这次哥本哈根给人的感觉一直是尖锐激烈的争吵，到底在吵什么？\n丁仲礼：其实吵的问题很简单，就是今后不同的国家，还能排放多少二氧化碳。\n记者：这个排放多少，实质又是什么？",
     "Phóng viên: Hội nghị Copenhagen lần này luôn cho người ta cảm giác toàn là những cuộc tranh cãi gay gắt, kịch liệt, rốt cuộc là cãi nhau về điều gì? Đinh Trọng Lễ: Thật ra vấn đề tranh cãi rất đơn giản, đó là từ nay về sau các quốc gia khác nhau còn được thải ra bao nhiêu khí cacbonic. Phóng viên: Vậy chuyện thải bao nhiêu này, thực chất là gì?",
     ["给人的感觉 là cảm giác mang lại cho người ta. 尖锐激烈的争吵 là cuộc tranh cãi gay gắt, kịch liệt. 到底 là rốt cuộc, dùng trong câu hỏi để truy hỏi đến cùng.",
      "Câu trả lời của ông Đinh rất ngắn gọn: cãi nhau chỉ vì một chuyện, 还能排放多少二氧化碳, còn được thải bao nhiêu khí cacbonic. Phóng viên hỏi tiếp: 实质又是什么; chữ 又 làm câu hỏi đi sâu thêm, truy đến bản chất."]),
    ("丁仲礼：简单一句话，就是说这个问题是和能源问题联系在一起的，和发展问题是休戚相关的，所以说争论半天就是我还能排放多少，我还能使用多少能源。\n记者：您的意思就是这个排放就意味着未来的发展权？\n丁仲礼：这个是肯定的。",
     "Đinh Trọng Lễ: Nói gọn một câu, vấn đề này gắn liền với vấn đề năng lượng, gắn bó mật thiết với vấn đề phát triển, cho nên tranh cãi mãi cũng chỉ là: tôi còn được thải bao nhiêu, tôi còn được dùng bao nhiêu năng lượng. Phóng viên: Ý ông là quyền phát thải này đồng nghĩa với quyền phát triển trong tương lai? Đinh Trọng Lễ: Điều đó là chắc chắn.",
     ["简单一句话 là nói gọn một câu, dùng để tóm tắt, rút ra điểm cốt lõi; đây là mẫu câu thứ hai. 和……联系在一起 là gắn liền với; 和……是休戚相关的 là gắn bó mật thiết với.",
      "争论半天 là tranh luận mãi; 半天 ở đây là khẩu ngữ, chỉ thời gian rất lâu chứ không phải đúng nửa ngày. Logic của ông Đinh: phát thải gắn với năng lượng, năng lượng gắn với phát triển, nên 排放就意味着未来的发展权."]),
    ("记者：这个排放权对于普通国民又意味着什么？\n丁仲礼：意味着生活的改善，意味着国家的发展，你的福利能不能进一步地增加，也意味着你有没有工作。",
     "Phóng viên: Vậy quyền phát thải này có ý nghĩa gì đối với người dân bình thường? Đinh Trọng Lễ: Nó có nghĩa là cuộc sống được cải thiện, đất nước được phát triển, phúc lợi của bạn có thể tăng thêm nữa hay không, và cũng có nghĩa là bạn có việc làm hay không.",
     ["对于普通国民 là đối với người dân bình thường. Câu trả lời dùng phép điệp: 意味着 lặp lại ba lần, làm lập luận thêm mạnh mẽ.",
      "福利 là phúc lợi. 进一步地增加 là tăng thêm một bước nữa; 进一步 là mẫu câu thứ ba. 有没有工作 là có việc làm hay không: quyền phát thải gắn với công ăn việc làm của từng người."]),
    ("记者：您理解的公平是什么？\n丁仲礼：人与人之间应该有个大致相等的排放空间。\n记者：不过，这次的方案并没有对发展中国家提出要求，也没有要求你减多少，不是吗？",
     "Phóng viên: Theo ông hiểu, công bằng là gì? Đinh Trọng Lễ: Giữa người với người nên có một không gian phát thải gần như ngang nhau. Phóng viên: Nhưng phương án lần này đâu có đặt ra yêu cầu đối với các nước đang phát triển, cũng không yêu cầu các ông phải giảm bao nhiêu, chẳng phải vậy sao?",
     ["大致相等 là gần như ngang bằng, 大致 là đại khái, xấp xỉ. Đây là quan điểm cốt lõi của ông Đinh: công bằng là tính theo đầu người, mỗi người có không gian phát thải gần như nhau.",
      "发展中国家 là các nước đang phát triển, còn 发达国家 là các nước phát triển. 不是吗 ở cuối câu là câu hỏi tu từ, nghĩa là chẳng phải vậy sao, dùng để khẳng định ý của mình."]),
    ("丁仲礼：它确实是没有对发展中国家减排设定绝对量，但是它对发达国家设定了减排标准。中期，2020年有25%到40%的减排，到2050年要有80%到95%的减排。但是，它有一个总量，就是全世界二氧化碳的排放总量统统放在8000亿吨这个大盘子里。",
     "Đinh Trọng Lễ: Đúng là nó không đặt ra lượng giảm phát thải tuyệt đối cho các nước đang phát triển, nhưng nó đặt ra tiêu chuẩn giảm phát thải cho các nước phát triển. Trung hạn, đến năm 2020 giảm từ 25% đến 40%, đến năm 2050 phải giảm từ 80% đến 95%. Nhưng nó có một tổng lượng, tức là toàn bộ lượng khí cacbonic thải ra của cả thế giới đều nằm trong cái đĩa lớn 800 tỷ tấn này.",
     ["确实 là đúng là, quả thật: ông Đinh thừa nhận ý của phóng viên trước, rồi dùng 但是 để chuyển ý. 绝对量 là lượng tuyệt đối. 对……设定标准 là đặt ra tiêu chuẩn cho ai.",
      "Điểm mấu chốt nằm ở câu cuối: 统统放在八千亿吨这个大盘子里. Cái đĩa lớn tám trăm tỷ tấn chính là chiếc bánh trong tên bài: tổng lượng phát thải của cả thế giới đã bị giới hạn, nước này dùng nhiều thì nước kia còn ít."],
     "丁仲礼：它确实是没有对发展中国家减排设定绝对量，但是它对发达国家设定了减排标准。中期，二零二零年有百分之二十五到百分之四十的减排，到二零五零年要有百分之八十到百分之九十五的减排。但是，它有一个总量，就是全世界二氧化碳的排放总量统统放在八千亿吨这个大盘子里。"),
    ("丁仲礼：那么等于这个蛋糕的数量是确定下来了，也就是说，今后发达国家的人均排放权是发展中国家的2.3倍。尽管减80%，一步一步往下减，但是发达国家基数大，是发展中国家的4.8倍。如果国际上对今后的排放进行严格的限定的话，那么二氧化碳的排放权就会变成一种非常稀缺的、不可多得的商品。",
     "Đinh Trọng Lễ: Như vậy là số lượng của chiếc bánh đã được xác định, nói cách khác, từ nay về sau quyền phát thải bình quân đầu người của các nước phát triển gấp 2,3 lần các nước đang phát triển. Dù họ giảm 80%, giảm dần từng bước, nhưng mức gốc của các nước phát triển lớn, gấp 4,8 lần các nước đang phát triển. Nếu quốc tế hạn chế nghiêm ngặt lượng phát thải sau này, thì quyền phát thải khí cacbonic sẽ trở thành một thứ hàng hóa cực kỳ khan hiếm, khó mà có được.",
     ["等于 là bằng với, tức là. 也就是说 là nói cách khác, tức là, dùng để giải thích rõ hơn ý trước; đây là mẫu câu thứ tư. 人均排放权 là quyền phát thải bình quân đầu người.",
      "尽管……但是…… là mặc dù… nhưng…. 一步一步往下减 là giảm dần từng bước. 基数大 là mức gốc lớn. 如果……的话，那么…… là nếu… thì…. Khi đó quyền phát thải trở thành thứ hàng hóa khan hiếm, phải mua bằng tiền."],
     "丁仲礼：那么等于这个蛋糕的数量是确定下来了，也就是说，今后发达国家的人均排放权是发展中国家的二点三倍。尽管减百分之八十，一步一步往下减，但是发达国家基数大，是发展中国家的四点八倍。如果国际上对今后的排放进行严格的限定的话，那么二氧化碳的排放权就会变成一种非常稀缺的、不可多得的商品。"),
    ("记者：就是你想要排有可能……\n丁仲礼：你不够排你就得买，前提是你承认二氧化碳排放配额是一种稀缺商品。\n记者：真金白银。\n丁仲礼：那么这个8000亿吨分配的过程当中，多分一点，少分一点是多大的利益。",
     "Phóng viên: Tức là nếu muốn thải thì có thể… Đinh Trọng Lễ: Không đủ để thải thì anh phải mua, với điều kiện anh thừa nhận hạn ngạch phát thải khí cacbonic là một thứ hàng hóa khan hiếm. Phóng viên: Tiền thật bạc thật đấy. Đinh Trọng Lễ: Vậy thì trong quá trình phân chia 800 tỷ tấn này, được chia nhiều hơn một chút hay ít hơn một chút là cả một khoản lợi ích lớn biết bao.",
     ["你不够排你就得买: động từ năng nguyện ở đây đọc là děi, nghĩa là phải, khẩu ngữ. 前提是 là với điều kiện là, tiền đề là. 排放配额 là hạn ngạch phát thải.",
      "真金白银 là câu chen ngắn của phóng viên: phải trả bằng tiền thật. 多分一点，少分一点是多大的利益 là câu cảm thán: chia nhiều một chút hay ít một chút là cả một khoản lợi ích lớn biết bao; 多大 ở đây nghĩa là lớn biết bao."],
     "记者：就是你想要排有可能。丁仲礼：你不够排你就得买，前提是你承认二氧化碳排放配额是一种稀缺商品。记者：真金白银。丁仲礼：那么这个八千亿吨分配的过程当中，多分一点，少分一点是多大的利益。"),
    ("记者：它现在提出的一个概念，就是说我不管你是人均，还是说贫富，现在只以碳排放大国来算。\n丁仲礼：根据G8的方案，27个发达国家取走的是多少蛋糕，取走的是44%。发达国家多少人口，11亿人口，余下的55亿人分56%的蛋糕，那么你说公平不公平？",
     "Phóng viên: Khái niệm mà họ đưa ra bây giờ là: không cần biết tính theo đầu người hay theo giàu nghèo, giờ chỉ tính theo các nước phát thải lớn. Đinh Trọng Lễ: Theo phương án của G8, 27 nước phát triển lấy đi bao nhiêu phần bánh? Lấy đi 44%. Các nước phát triển có bao nhiêu dân? 1,1 tỷ người; còn 5,5 tỷ người còn lại chia nhau 56% chiếc bánh. Vậy anh nói xem, có công bằng không?",
     ["不管……还是…… là bất kể… hay…. 只以碳排放大国来算 là chỉ tính theo các nước phát thải lớn; 以……来算 là lấy cái gì làm căn cứ để tính.",
      "Ông Đinh dùng lối tự hỏi tự đáp: 取走的是多少蛋糕，取走的是百分之四十四. Hai con số đặt cạnh nhau: một tỷ một trăm triệu người lấy bốn mươi bốn phần trăm, còn năm tỷ rưỡi người chia nhau năm mươi sáu phần trăm. 你说公平不公平 là câu hỏi để người nghe tự rút ra kết luận."],
     "记者：它现在提出的一个概念，就是说我不管你是人均，还是说贫富，现在只以碳排放大国来算。丁仲礼：根据八国集团的方案，二十七个发达国家取走的是多少蛋糕，取走的是百分之四十四。发达国家多少人口，十一亿人口，余下的五十五亿人分百分之五十六的蛋糕，那么你说公平不公平？"),
    ("记者：它这个方案本身就没有按人口计算。\n丁仲礼：那你算算账。假如告诉你，中国从2020年以后，每年花一万亿人民币去购买二氧化碳排放权，你会怎么想，是不是有失公允？",
     "Phóng viên: Bản thân phương án này đã không tính theo dân số. Đinh Trọng Lễ: Vậy anh thử tính xem. Giả sử có người nói với anh rằng, từ sau năm 2020, mỗi năm Trung Quốc phải bỏ ra một nghìn tỷ nhân dân tệ để mua quyền phát thải khí cacbonic, anh sẽ nghĩ sao, như thế có phải là thiếu công bằng không?",
     ["本身 là bản thân, tự nó. 按人口计算 là tính theo dân số. 算算账 là động từ ly hợp lặp lại, mang giọng khẩu ngữ: anh tính thử xem.",
      "假如 là giả sử. 有失公允 là thiếu công bằng: 有 cộng một động từ đơn âm tiết như 失, tạo giọng điệu uyển chuyển, nhẹ nhàng; đây là mẫu câu thứ năm."],
     "记者：它这个方案本身就没有按人口计算。丁仲礼：那你算算账。假如告诉你，中国从二零二零年以后，每年花一万亿人民币去购买二氧化碳排放权，你会怎么想，是不是有失公允？"),
    ("换句话说，我对公平的理解，我把排放权视为发展权，视为基本人权，所以，人与人之间应该有个大致相等的排放空间。维护发展中国家的利益，保障发展中国家的发展权利，落实联合国千年发展计划，这难道不是人类的利益吗？",
     "Nói cách khác, theo cách hiểu của tôi về công bằng, tôi coi quyền phát thải là quyền phát triển, là quyền cơ bản của con người, vì vậy giữa người với người nên có một không gian phát thải gần như ngang nhau. Bảo vệ lợi ích của các nước đang phát triển, bảo đảm quyền phát triển của các nước đang phát triển, thực hiện Kế hoạch Phát triển Thiên niên kỷ của Liên Hợp Quốc, chẳng lẽ đó không phải là lợi ích của nhân loại sao?",
     ["换句话说 là nói cách khác. 把……视为…… là coi cái gì là cái gì, văn viết, giống 把……看作……; đây là mẫu câu thứ sáu. 视为基本人权 là coi là quyền cơ bản của con người.",
      "Câu cuối dùng ba cụm động từ song song: 维护利益，保障权利，落实计划, rồi kết bằng câu phản vấn 这难道不是人类的利益吗, chẳng lẽ đó không phải là lợi ích của nhân loại sao? Câu phản vấn làm sự khẳng định mạnh hơn."]),
    ("记者：假如像您所说的，现在这个方案，发达国家又不接受的话，如果它就这么拖下去，这几年下去，会不会温室效应导致的全球变暖的状况变得更糟糕了？",
     "Phóng viên: Giả sử như ông nói, phương án hiện nay các nước phát triển lại không chấp nhận, nếu cứ kéo dài mãi như vậy, vài năm nữa trôi qua, liệu tình trạng trái đất nóng lên do hiệu ứng nhà kính có trở nên tồi tệ hơn không?",
     ["像您所说的 là như ông đã nói; 所 cộng động từ là cách nói trang trọng. 又不接受 là lại không chấp nhận. 拖下去 là kéo dài mãi; 下去 chỉ sự tiếp diễn.",
      "温室效应导致的全球变暖 là sự nóng lên toàn cầu do hiệu ứng nhà kính gây ra; cả cụm dài này làm định ngữ cho 状况. 会不会变得更糟糕 là liệu có trở nên tồi tệ hơn không."]),
    ("丁仲礼：我很乐观。我研究几亿年以来的环境气候演化，这不是人类拯救地球的问题，是人类拯救自己的问题，跟拯救地球是没有关系的，地球用不着你拯救，地球比现在再高十几度的时候有的是，地球二氧化碳的浓度比现在高10倍的时候也有的是，地球不都是这么演化过来的？都好好的。",
     "Đinh Trọng Lễ: Tôi rất lạc quan. Tôi nghiên cứu sự biến đổi của môi trường khí hậu suốt mấy trăm triệu năm qua. Đây không phải chuyện con người cứu trái đất, mà là chuyện con người tự cứu mình, chẳng liên quan gì đến việc cứu trái đất cả. Trái đất không cần anh cứu. Những thời kỳ trái đất nóng hơn bây giờ hơn chục độ có đầy, những thời kỳ nồng độ khí cacbonic cao gấp 10 lần bây giờ cũng có đầy, chẳng phải trái đất đều đã biến đổi như thế mà đi tới hôm nay sao? Vẫn ổn cả.",
     ["用不着 là không cần, khẩu ngữ. 比现在再高十几度 là còn cao hơn bây giờ hơn chục độ. 的时候有的是 là những lúc như thế có đầy, không thiếu: 有的是 nhấn mạnh rất nhiều; đây là mẫu câu thứ bảy.",
      "地球不都是这么演化过来的 là câu phản vấn: chẳng phải trái đất đều biến đổi như vậy mà đi qua sao? 都好好的 là đều ổn cả. Ý của ông Đinh: khí hậu thay đổi không hủy diệt được trái đất, nó chỉ đe dọa chính con người."],
     "丁仲礼：我很乐观。我研究几亿年以来的环境气候演化，这不是人类拯救地球的问题，是人类拯救自己的问题，跟拯救地球是没有关系的，地球用不着你拯救，地球比现在再高十几度的时候有的是，地球二氧化碳的浓度比现在高十倍的时候也有的是，地球不都是这么演化过来的？都好好的。"),
    ("记者：毁灭的只是物种？\n丁仲礼：毁灭的只是物种，毁灭的是人类自己。所以是人类如何拯救人类，不是人类如何拯救地球。\n记者：到底能不能拯救自己，最核心的东西，最终取决于什么？",
     "Phóng viên: Cái bị hủy diệt chỉ là các loài sinh vật? Đinh Trọng Lễ: Cái bị hủy diệt chỉ là các loài sinh vật, cái bị hủy diệt là chính loài người. Vì vậy vấn đề là con người cứu lấy con người thế nào, chứ không phải con người cứu trái đất thế nào. Phóng viên: Rốt cuộc có tự cứu được mình hay không, điều cốt lõi nhất, cuối cùng phụ thuộc vào cái gì?",
     ["毁灭的只是物种 là cấu trúc chữ 的: 毁灭的 là cái bị hủy diệt. Ông Đinh lặp lại câu của phóng viên rồi đẩy ý lên cao hơn: 毁灭的是人类自己.",
      "是A，不是B là phép đối để nhấn mạnh: 是人类如何拯救人类，不是人类如何拯救地球. 最终取决于什么 là cuối cùng phụ thuộc vào cái gì; 取决于 là mẫu câu thứ tám."]),
    ("丁仲礼：取决于文化、文明。人类应对各种挑战的时候，人们有一种更具包容性的、更有弹性的一种文明的产生，或者是我们现有文明有很好的发展。",
     "Đinh Trọng Lễ: Phụ thuộc vào văn hóa, văn minh. Khi loài người ứng phó với đủ loại thách thức, cần có một nền văn minh bao dung hơn, linh hoạt hơn ra đời, hoặc là nền văn minh hiện có của chúng ta phát triển thật tốt.",
     ["应对各种挑战 là ứng phó với đủ loại thách thức. 更具包容性的 là có tính bao dung hơn; 具 là có, văn viết. 更有弹性的 là linh hoạt hơn. Đây là lời nói trong phỏng vấn nên hơi lặp: 一种……的一种文明.",
      "Kết thúc cuộc phỏng vấn, ông Đinh đưa câu chuyện từ những con số và lợi ích lên tầm văn minh: con người có tự cứu được mình hay không, rốt cuộc tùy vào việc ta có xây dựng được một nền văn minh bao dung và linh hoạt hơn hay không."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 碳排放的“蛋糕”怎么切？", size=42,
    items=["Bài phỏng vấn: 记者 (phóng viên) hỏi – 丁仲礼 (Đinh Trọng Lễ) đáp",
           "Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa. Bài được trích từ chương trình 面对面, Đối mặt, của Đài truyền hình Trung ương Trung Quốc, phát sóng ngày hai mươi mốt tháng ba năm 2010, với tiêu đề: 什么是公平的减排方案, thế nào là một phương án giảm phát thải công bằng.",
         F(0, "Sau một đoạn mở đầu giới thiệu bối cảnh, phần còn lại là hỏi đáp: 记者 là phóng viên, còn 丁仲礼 là người trả lời. Văn phỏng vấn mang đậm màu sắc khẩu ngữ, có chỗ lặp từ, có câu bỏ lửng, các bạn đừng ngạc nhiên nhé."),
         F(1, "Thầy chia bài thành mười sáu đoạn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(2, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(3, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

ZS = {3: 50, 4: 46, 9: 44, 10: 46}
for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    n = len(zh)
    # đoạn hỏi đáp xuống dòng nhiều: chọn cỡ chữ nhỏ hơn cho vừa khung
    zsize = ZS.get(i) or (54 if n <= 100 else 50 if n <= 125 else 46)
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Bố cục & hiểu bài", section="Bài khóa 课文", title="Bố cục bài khóa", size=34,
    items=["## Mở đầu (đoạn 1–2): Hội nghị Copenhagen 2009 – tranh cãi gay gắt, không đạt đồng thuận",
           "## Cãi nhau vì cái gì? (đoạn 3–5)",
           "排放 → 能源 → 发展权：意味着生活的改善、国家的发展、福利和工作",
           "## Thế nào là công bằng? (đoạn 6–12)",
           "人均 · 蛋糕 = 8000亿吨 · 27国取走44%，55亿人分56% · 有失公允 · 把排放权视为发展权",
           "## Lạc quan (đoạn 13–16): 人类拯救自己，不是拯救地球 → 取决于文化、文明"],
    say=["Trước khi sang phần ngữ pháp, chúng ta cùng nhìn lại bố cục của bài khóa.",
         F(0, "Phần mở đầu, đoạn một và hai: Hội nghị Copenhagen năm 2009, đại biểu đến từ một trăm chín mươi hai quốc gia và vùng lãnh thổ, tranh cãi gay gắt, đến cuối vẫn không đạt được đồng thuận."),
         F(1, "Phần hai, đoạn ba đến năm: các nước cãi nhau vì cái gì?"),
         F(2, "Câu trả lời là một chuỗi logic: 排放 gắn với 能源, năng lượng gắn với 发展权, quyền phát triển. Với người dân bình thường, nó có nghĩa là cuộc sống, phúc lợi và việc làm."),
         F(3, "Phần ba, đoạn sáu đến mười hai, là trọng tâm: thế nào là công bằng?"),
         F(4, "Ông Đinh cho rằng phải tính theo đầu người. Tổng lượng phát thải, tức chiếc bánh, chỉ có tám trăm tỷ tấn; theo phương án của G8, hai mươi bảy nước phát triển lấy đi bốn mươi bốn phần trăm, năm tỷ rưỡi người còn lại chia năm mươi sáu phần trăm. Như thế là 有失公允. Ông 把排放权视为发展权, coi quyền phát thải là quyền phát triển, là quyền cơ bản của con người."),
         F(5, "Phần cuối, đoạn mười ba đến mười sáu: ông Đinh lạc quan. Trái đất không cần con người cứu; điều con người cần làm là tự cứu mình, và điều đó rốt cuộc phụ thuộc vào văn hóa, văn minh.")])

add("bullets", section="Bài khóa 课文", title="Kiểm tra hiểu bài: đúng hay sai?", reveal=True, size=34,
    items=["(1) 哥本哈根会议最后达成了共识。",
           "Đáp án: Sai – 直到接近尾声代表们仍然没能达成共识。",
           "(2) 方案对发达国家设定了减排标准，对发展中国家没有设定减排的绝对量。",
           "Đáp án: Đúng – 它确实是没有对发展中国家减排设定绝对量，但是它对发达国家设定了减排标准。",
           "(3) 丁仲礼认为，公平就是只以碳排放大国来计算排放量。",
           "Đáp án: Sai – 他认为人与人之间应该有个大致相等的排放空间（按人均计算）。",
           "(4) 丁仲礼认为，全球变暖会毁灭地球，所以人类要拯救地球。",
           "Đáp án: Sai – 地球用不着你拯救，毁灭的是人类自己。"],
    say=["Bây giờ chúng ta kiểm tra xem mình đã hiểu bài chưa. Thầy đọc từng câu, các bạn cho biết đúng hay sai nhé.",
         F(0, "Câu một: 哥本哈根会议最后达成了共识。 Hội nghị Copenhagen cuối cùng đã đạt được đồng thuận. Đúng hay sai?"),
         F(1, "Đáp án: sai. Bài khóa nói rõ: 直到接近尾声代表们仍然没能达成共识。 Mãi đến lúc gần kết thúc, các đại biểu vẫn không đạt được đồng thuận."),
         F(2, "Câu hai: 方案对发达国家设定了减排标准，对发展中国家没有设定减排的绝对量。 Phương án đặt ra tiêu chuẩn giảm phát thải cho các nước phát triển, không đặt lượng giảm tuyệt đối cho các nước đang phát triển."),
         F(3, "Đáp án: đúng. Ông Đinh thừa nhận: 它确实是没有对发展中国家减排设定绝对量，但是它对发达国家设定了减排标准。 Nhưng ông chỉ ra vấn đề nằm ở tổng lượng."),
         F(4, "Câu ba: 丁仲礼认为，公平就是只以碳排放大国来计算排放量。 Ông Đinh cho rằng công bằng là chỉ tính theo các nước phát thải lớn."),
         F(5, "Đáp án: sai. Đó là khái niệm mà phương án kia đưa ra, còn ông Đinh phản đối. Ông cho rằng 人与人之间应该有个大致相等的排放空间, tức là phải tính theo đầu người."),
         F(6, "Câu bốn: 丁仲礼认为，全球变暖会毁灭地球，所以人类要拯救地球。 Ông Đinh cho rằng trái đất nóng lên sẽ hủy diệt trái đất, nên con người phải cứu trái đất."),
         F(7, "Đáp án: sai. Ông nói: 地球用不着你拯救, trái đất không cần anh cứu; 毁灭的是人类自己, cái bị hủy diệt là chính loài người. Đây là quan điểm rất độc đáo của bài.")])

# ======================= MẪU CÂU =======================
add("bullets", chapter="Mẫu câu: 就 · 简单一句话 · 进一步", section="Mẫu câu 重点句型", title="1. 就……+ V. – về (vấn đề…) mà làm gì", size=33,
    items=["Giới từ 就 dẫn ra đối tượng, phạm vi đề tài của hành động; văn viết",
           "Hay gặp: 就……达成协议 / 发表意见 / 接受采访 / 征求意见 / 进行讨论",
           "国际社会希望……就2012到2020年全球应对气候变化问题达成一项新协议。",
           "《纽约时报》曾致电他，要求他就此事发表意见。",
           "公司的诉讼代理人拒绝就此事接受电视台的采访。",
           "记者获悉，今年该市将就文明行为立法征求市民的意见和建议。"],
    say=["Bây giờ chúng ta sang phần mẫu câu trọng điểm, 重点句型. Bài này có tám mẫu. Mẫu thứ nhất là giới từ 就 đứng trước một cụm danh từ, rồi mới đến động từ.",
         F(0, "Ở đây 就 không phải là phó từ nghĩa là liền, mà là giới từ, dẫn ra đối tượng hoặc phạm vi đề tài của hành động. Tiếng Việt dịch là về, đối với, xoay quanh vấn đề gì đó. Cách dùng này mang màu sắc văn viết, rất hay gặp trong tin tức."),
         F(1, "Những kết hợp hay gặp: 就什么达成协议, đạt được thỏa thuận về việc gì; 就什么发表意见, phát biểu ý kiến về việc gì; 接受采访，征求意见，进行讨论."),
         F(2, "Ví dụ một, từ bài khóa: 国际社会希望在本次大会上商定下一步温室气体减排的方案，就二零一二到二零二零年全球应对气候变化问题达成一项新协议。 Đạt được một hiệp định mới về vấn đề toàn cầu ứng phó với biến đổi khí hậu giai đoạn 2012 đến 2020."),
         F(3, "Ví dụ hai: 纽约时报曾致电他，要求他就此事发表意见。 Tờ Thời báo New York từng gọi điện cho ông, đề nghị ông phát biểu ý kiến về việc này. 致电 là gọi điện, văn viết."),
         F(4, "Ví dụ ba: 公司的诉讼代理人拒绝就此事接受电视台的采访。 Người đại diện tố tụng của công ty từ chối trả lời phỏng vấn của đài truyền hình về việc này."),
         F(5, "Ví dụ bốn: 记者获悉，今年该市将就文明行为立法征求市民的意见和建议。 Phóng viên được biết, năm nay thành phố này sẽ lấy ý kiến và kiến nghị của người dân về việc lập pháp cho hành vi văn minh. 获悉 là được biết, 该市 là thành phố này.")])

add("bullets", section="Mẫu câu 重点句型", title="2. 简单一句话，…… – nói gọn một câu, tóm lại", size=34,
    items=["Đứng đầu câu, rút ra ý cốt lõi, kết luận ngắn gọn; khẩu ngữ (văn viết: 简言之 · 一言以蔽之)",
           "简单一句话，就是说这个问题是和能源问题联系在一起的，和发展问题是休戚相关的……",
           "简单一句话，连日常琐事都处理不好的人，还谈什么事业抱负呢？",
           "简单一句话，种瓜得瓜，种豆得豆，没有付出就没有收获！"],
    say=["Mẫu thứ hai: 简单一句话, nói gọn một câu.",
         F(0, "Cụm này đứng đầu câu, dùng khi người nói muốn rút ra ý cốt lõi, đưa ra kết luận ngắn gọn sau một vấn đề phức tạp. Tiếng Việt nói là: nói gọn một câu, tóm lại là. Đây là cách nói khẩu ngữ; trong văn viết có thể dùng 简言之 hoặc 一言以蔽之."),
         F(1, "Ví dụ một, từ bài khóa: 简单一句话，就是说这个问题是和能源问题联系在一起的，和发展问题是休戚相关的。 Nói gọn một câu, vấn đề này gắn liền với năng lượng, gắn bó mật thiết với phát triển."),
         F(2, "Ví dụ hai: 简单一句话，连日常琐事都处理不好的人，还谈什么事业抱负呢？ Nói gọn một câu, người ngay cả việc vặt hằng ngày cũng không xử lý nổi, thì còn nói gì đến sự nghiệp, hoài bão? 琐事 là việc vặt, 抱负 là hoài bão."),
         F(3, "Ví dụ ba: 简单一句话，种瓜得瓜，种豆得豆，没有付出就没有收获！ Tóm lại, trồng dưa được dưa, trồng đậu được đậu, không bỏ công sức thì không có thu hoạch. Giống câu gieo gió gặt bão, hay có làm thì mới có ăn của tiếng Việt.")])

add("bullets", section="Mẫu câu 重点句型", title="3. 进一步（地）…… – tiến thêm một bước, sâu hơn", size=34,
    items=["Phó từ, đứng trước động từ (thường song âm tiết): làm sâu hơn, nhiều hơn so với hiện tại",
           "Hay gặp: 进一步了解 · 进一步发展 · 进一步加强 · 进一步提高",
           "排放权对于普通的国民来说，……你的福利能不能进一步地增加，也意味着你有没有工作。",
           "最近他的表现实在让人捉摸不透，我想进一步了解他来这儿的动机。",
           "他们俩的关系有进一步往前发展的可能吗？"],
    say=["Mẫu thứ ba: 进一步, có thể thêm 地 thành 进一步地.",
         F(0, "进一步 là phó từ, nghĩa đen là tiến thêm một bước, đứng trước động từ, biểu thị làm sâu hơn, nhiều hơn so với mức hiện tại. Động từ phía sau thường là từ hai âm tiết."),
         F(1, "Những kết hợp hay gặp: 进一步了解, tìm hiểu sâu hơn; 进一步发展, phát triển hơn nữa; 进一步加强, tăng cường hơn nữa; 进一步提高, nâng cao hơn nữa."),
         F(2, "Ví dụ một, từ bài khóa: 你的福利能不能进一步地增加，也意味着你有没有工作。 Phúc lợi của bạn có thể tăng thêm nữa hay không, cũng có nghĩa là bạn có việc làm hay không."),
         F(3, "Ví dụ hai: 最近他的表现实在让人捉摸不透，我想进一步了解他来这儿的动机。 Gần đây biểu hiện của anh ta thật khó đoán, tôi muốn tìm hiểu kỹ hơn động cơ anh ta đến đây. 捉摸不透 là không đoán ra được."),
         F(4, "Ví dụ ba: 他们俩的关系有进一步往前发展的可能吗？ Quan hệ của hai người họ có khả năng tiến thêm một bước nữa không?")])

add("bullets", chapter="Mẫu câu: 也就是说 · 有失 · 视为", section="Mẫu câu 重点句型", title="4. 也就是说…… – tức là, nói cách khác", size=33,
    items=["Dẫn ra lời giải thích, nói rõ hơn hoặc rút ra hệ quả của ý trước (≈ 换句话说)",
           "那么等于这个蛋糕的数量是确定下来了，也就是说，今后发达国家的人均排放权是发展中国家的2.3倍。",
           "很多人相信字如其人，也就是说，一个人的品行、性格可以从其书写中显现出来。",
           "有一家公司的招聘要求是：男生，本科、硕士均可。也就是说，他们宁愿要本科男生，也不要硕士女生。"],
    say=["Mẫu thứ tư: 也就是说, tức là, nói cách khác.",
         F(0, "也就是说 đứng giữa hai vế hoặc đầu câu sau, dẫn ra lời giải thích, nói rõ hơn ý trước, hoặc rút ra hệ quả ngầm ẩn trong ý trước. Nghĩa gần giống 换句话说, mà chúng ta gặp ở đoạn mười hai."),
         F(1, "Ví dụ một, từ bài khóa: 那么等于这个蛋糕的数量是确定下来了，也就是说，今后发达国家的人均排放权是发展中国家的二点三倍。 Số lượng chiếc bánh đã được xác định, tức là quyền phát thải bình quân đầu người của nước phát triển gấp hai phẩy ba lần nước đang phát triển."),
         F(2, "Ví dụ hai: 很多人相信字如其人，也就是说，一个人的品行、性格可以从其书写中显现出来。 Nhiều người tin rằng nét chữ nết người, tức là phẩm hạnh, tính cách của một người có thể thể hiện qua chữ viết của họ. Giống hệt câu nét chữ nết người của tiếng Việt."),
         F(3, "Ví dụ ba: 有一家公司的招聘要求是：男生，本科、硕士均可。也就是说，他们宁愿要本科男生，也不要硕士女生。 Một công ty ghi yêu cầu tuyển dụng: nam, cử nhân hay thạc sĩ đều được. Nói cách khác, họ thà nhận nam cử nhân chứ không nhận nữ thạc sĩ. Ở đây 也就是说 rút ra hàm ý phân biệt đối xử ẩn sau câu chữ.")])

add("bullets", section="Mẫu câu 重点句型", title="5. 有 + động từ đơn âm tiết – giọng điệu uyển chuyển", size=34,
    items=["有 + động từ một âm tiết: nói giảm, lịch sự, văn viết",
           "Hay gặp: 有失公允 (thiếu công bằng) · 有失身份 (mất thể diện) · 有待改善 / 有待提高 (còn chờ cải thiện / nâng cao)",
           "假如告诉你，中国……每年花一万亿人民币去购买二氧化碳排放权，你会怎么想，是不是有失公允？",
           "也许有人要问了：一个老作家还要去学习，接受批评，难道不有失身份么？",
           "农村受教育程度普遍偏低，中小学基本办学条件有待改善，教师素质有待提高。"],
    say=["Mẫu thứ năm: 有 cộng một động từ đơn âm tiết.",
         F(0, "Cấu trúc này tạo giọng điệu uyển chuyển, nói giảm nói tránh, lịch sự hơn, thường gặp trong văn viết. Ví dụ, thay vì nói thẳng 不公平, không công bằng, người ta nói 有失公允."),
         F(1, "Những cụm hay gặp: 有失公允, thiếu công bằng; 有失身份, làm mất thân phận, mất thể diện; 有待改善 và 有待提高, còn cần được cải thiện, nâng cao. Chữ 待 là chờ đợi: 有待 tức là vẫn còn đang chờ, chưa đạt."),
         F(2, "Ví dụ một, từ bài khóa: 假如告诉你，中国从二零二零年以后，每年花一万亿人民币去购买二氧化碳排放权，你会怎么想，是不是有失公允？ Như thế có phải là thiếu công bằng không?"),
         F(3, "Ví dụ hai: 也许有人要问了：一个老作家还要去学习，接受批评，难道不有失身份么？ Có lẽ sẽ có người hỏi: một nhà văn lão thành mà còn phải đi học, chịu phê bình, chẳng phải là mất thể diện sao?"),
         F(4, "Ví dụ ba: 农村受教育程度普遍偏低，中小学基本办学条件有待改善，教师素质有待提高。 Trình độ học vấn ở nông thôn nhìn chung còn thấp, điều kiện cơ bản của các trường tiểu học, trung học còn cần cải thiện, chất lượng giáo viên còn cần nâng cao.")])

add("bullets", section="Mẫu câu 重点句型", title="6. 把……视为…… – coi… là…, xem… như…", size=34,
    items=["Văn viết, ≈ 把……看作 / 当作……; bị động: ……被视为……",
           "我对公平的理解，我把排放权视为发展权，视为基本人权……",
           "众所周知，中国人把孝顺父母视为天经地义的事情。",
           "短暂的一生会有许多困难和挫折，我们应该把它们视为前进的阶梯。"],
    say=["Mẫu thứ sáu: 把什么视为什么, coi cái gì là cái gì.",
         F(0, "视 là nhìn, xem; 视为 là xem là, coi là, văn viết. Nghĩa giống 把什么看作什么 hay 把什么当作什么 trong khẩu ngữ. Dạng bị động là 被视为: 他被视为天才, anh ấy được coi là thiên tài."),
         F(1, "Ví dụ một, từ bài khóa: 我对公平的理解，我把排放权视为发展权，视为基本人权。 Tôi coi quyền phát thải là quyền phát triển, là quyền cơ bản của con người."),
         F(2, "Ví dụ hai: 众所周知，中国人把孝顺父母视为天经地义的事情。 Ai cũng biết, người Trung Quốc coi hiếu thảo với cha mẹ là chuyện hiển nhiên, đạo lý trời đất. 天经地义 là lẽ đương nhiên, không thể bàn cãi."),
         F(3, "Ví dụ ba: 短暂的一生会有许多困难和挫折，我们应该把它们视为前进的阶梯。 Cuộc đời ngắn ngủi sẽ có nhiều khó khăn, trắc trở, chúng ta nên coi chúng là những bậc thang để tiến lên.")])

add("bullets", chapter="Mẫu câu: 有的是 · 取决于", section="Mẫu câu 重点句型", title="7. ……有的是 / 有的是 + N – có đầy, có thừa", size=33,
    items=["Nhấn mạnh rất nhiều, không sợ thiếu; khẩu ngữ. Đọc yǒudeshì (khác 有的 “có cái”)",
           "地球比现在再高十几度的时候有的是，地球二氧化碳的浓度比现在高10倍的时候也有的是……",
           "你们那里能解决这类问题的高水平的人有的是，就不必来这儿求援了吧！",
           "你先撞了我还如此不讲理，如果你非要和我争的话，我有的是时间和你吵。"],
    say=["Mẫu thứ bảy: 有的是. Có hai vị trí: đặt sau danh từ, như 时间有的是; hoặc đặt trước danh từ, như 有的是时间.",
         F(0, "有的是 nhấn mạnh rằng có rất nhiều, có thừa, không sợ thiếu. Đây là cách nói khẩu ngữ. Cẩn thận: đừng nhầm với 有的 trong 有的人, nghĩa là có người."),
         F(1, "Ví dụ một, từ bài khóa: 地球比现在再高十几度的时候有的是，地球二氧化碳的浓度比现在高十倍的时候也有的是。 Những lúc trái đất nóng hơn bây giờ hơn chục độ có đầy, những lúc nồng độ khí cacbonic cao gấp mười lần cũng có đầy."),
         F(2, "Ví dụ hai: 你们那里能解决这类问题的高水平的人有的是，就不必来这儿求援了吧！ Chỗ các anh thiếu gì người giỏi giải quyết được loại vấn đề này, khỏi cần đến đây cầu cứu nhé!"),
         F(3, "Ví dụ ba: 你先撞了我还如此不讲理，如果你非要和我争的话，我有的是时间和你吵。 Anh đâm vào tôi trước mà còn ngang ngược như vậy, nếu anh nhất định muốn cãi thì tôi thừa thời gian cãi với anh. Ở đây 有的是 đứng trước danh từ 时间.")])

add("bullets", section="Mẫu câu 重点句型", title="8. ……取决于…… – do… quyết định, tùy thuộc vào…", size=34,
    items=["A 取决于 B: B là yếu tố quyết định A; A thường có dạng hai mặt: 能不能 / 能否 / 是否 / 高低…",
           "人类到底能不能拯救自己，最核心的东西，最终取决于什么？",
           "一个国家的教育水平从本质上来说取决于全社会对于教育的重视程度。",
           "一个人能否成功取决于个人的心理素质、人生态度和才能资质。"],
    say=["Mẫu thứ tám: 取决于, do cái gì quyết định.",
         F(0, "Trong mẫu A取决于B, B là yếu tố quyết định A. Vế A thường mang ý hai mặt, như 能不能，能否，是否, hoặc 高低, 好坏. Tiếng Việt dịch là: A phụ thuộc vào B, A tùy thuộc vào B."),
         F(1, "Ví dụ một, từ bài khóa: 人类到底能不能拯救自己，最核心的东西，最终取决于什么？ Loài người rốt cuộc có tự cứu được mình không, điều cốt lõi nhất, cuối cùng phụ thuộc vào cái gì?"),
         F(2, "Ví dụ hai: 一个国家的教育水平从本质上来说取决于全社会对于教育的重视程度。 Về bản chất, trình độ giáo dục của một quốc gia phụ thuộc vào mức độ coi trọng giáo dục của toàn xã hội."),
         F(3, "Ví dụ ba: 一个人能否成功取决于个人的心理素质、人生态度和才能资质。 Một người có thành công hay không tùy thuộc vào bản lĩnh tâm lý, thái độ sống và tài năng tư chất của người đó.")])

# ======================= KẾT HỢP TỪ & THÀNH NGỮ =======================
add("bullets", chapter="Kết hợp từ & thành ngữ", section="Kết hợp từ 词语搭配", title="Kết hợp từ (1): 应对 · 尾声 · 共识", size=33,
    items=["## 应对：～问题 · ～挑战 · ～风险 · ～挫折",
           "我们应该有过硬的心理素质，这样才能应对各种风险，战胜各种挑战。",
           "## 尾声：接近～ · 进入～ · 临近～",
           "十一黄金周临近尾声，出行者开始有序踏上返程的路。",
           "## 共识：达成～ · 取得～ · 扩大～ · 增进～",
           "要加强双方领导人和各界人士之间的交往，增进互信，扩大共识。"],
    say=["Tiếp theo là phần kết hợp từ, 词语搭配. Học từ theo cụm sẽ giúp các bạn dùng từ tự nhiên như người bản ngữ.",
         F(0, "应对 đi với 问题，挑战，风险，挫折: ứng phó với vấn đề, thách thức, rủi ro, trắc trở."),
         F(1, "Ví dụ: 我们应该有过硬的心理素质，这样才能应对各种风险，战胜各种挑战。 Chúng ta nên có bản lĩnh tâm lý vững vàng, như vậy mới ứng phó được với mọi rủi ro, chiến thắng mọi thách thức. 过硬 là vững vàng, cứng cựa."),
         F(2, "尾声 đi với 接近，进入，临近: gần đến hồi kết, bước vào giai đoạn cuối, sắp kết thúc."),
         F(3, "Ví dụ: 十一黄金周临近尾声，出行者开始有序踏上返程的路。 Tuần lễ vàng Quốc khánh mùng một tháng mười sắp kết thúc, người đi chơi bắt đầu lần lượt lên đường trở về."),
         F(4, "共识 đi với 达成，取得，扩大，增进: đạt được, giành được, mở rộng, tăng cường sự đồng thuận."),
         F(5, "Ví dụ: 要加强双方领导人和各界人士之间的交往，增进互信，扩大共识。 Cần tăng cường giao lưu giữa lãnh đạo và nhân sĩ các giới của hai bên, tăng cường tin cậy lẫn nhau, mở rộng đồng thuận.")])

add("bullets", section="Kết hợp từ 词语搭配", title="Kết hợp từ (2): 尖锐 · 实质 · 落实", size=33,
    items=["## 尖锐：～的争吵 · ～的响声 · ～的批评",
           "这篇文章提出的批评十分尖锐、发人深省。",
           "## 实质：问题的～ · ～变化 · ～上",
           "区域之间经济发展的竞争，实质上体现为发展环境的竞争。",
           "## 落实：～计划 · ～任务 · ～政策",
           "目标已明确，基本思路也已确定，接下来要尽快落实该项政策。"],
    say=[F(0, "尖锐 đi với 争吵，响声，批评: cuộc cãi vã gay gắt, tiếng động chói tai, lời phê bình sắc bén."),
         F(1, "Ví dụ: 这篇文章提出的批评十分尖锐、发人深省。 Lời phê bình mà bài viết này đưa ra rất sắc bén, khiến người ta phải suy ngẫm sâu xa. 发人深省 là gợi cho người ta suy nghĩ sâu sắc."),
         F(2, "实质 đi với 问题的实质, bản chất của vấn đề; 实质变化, thay đổi thực chất; và 实质上, về thực chất."),
         F(3, "Ví dụ: 区域之间经济发展的竞争，实质上体现为发展环境的竞争。 Cạnh tranh phát triển kinh tế giữa các vùng, về thực chất là cạnh tranh về môi trường phát triển."),
         F(4, "落实 đi với 计划，任务，政策: thực hiện kế hoạch, nhiệm vụ, chính sách."),
         F(5, "Ví dụ: 目标已明确，基本思路也已确定，接下来要尽快落实该项政策。 Mục tiêu đã rõ ràng, hướng đi cơ bản cũng đã xác định, tiếp theo phải nhanh chóng triển khai chính sách này.")])

add("bullets", section="Thành ngữ 成语和惯用语", title="Thành ngữ trong bài: thêm ví dụ của sách", size=33,
    items=["举世瞩目：2008年夏天，举世瞩目的北京奥运会取得了圆满成功。",
           "硝烟四起：目前，全球争夺第N代移动通信经营权的战场已硝烟四起。",
           "休戚相关：世界经济现在比以往任何时候都和各国紧密相连，休戚相关。",
           "不可多得：对于中国女足来说，这次比赛是一次不可多得的与强队热身锻炼的机会。",
           "真金白银：用真金白银而不是空口白话去吸引人才。"],
    say=["Năm thành ngữ của bài, chúng ta đã học trong phần từ mới. Bây giờ cùng nghe thêm một ví dụ của sách cho mỗi thành ngữ.",
         F(0, "举世瞩目: 二零零八年夏天，举世瞩目的北京奥运会取得了圆满成功。 Mùa hè năm 2008, Thế vận hội Bắc Kinh được cả thế giới chú ý đã thành công tốt đẹp."),
         F(1, "硝烟四起: 目前，全球争夺第N代移动通信经营权的战场已硝烟四起。 Hiện nay, cuộc chiến giành quyền kinh doanh mạng di động thế hệ mới trên toàn cầu đã nổ ra khắp nơi. Ở đây thành ngữ dùng cho cạnh tranh thương mại."),
         F(2, "休戚相关: 世界经济现在比以往任何时候都和各国紧密相连，休戚相关。 Kinh tế thế giới hiện nay gắn bó chặt chẽ với các nước hơn bất cứ lúc nào, vui buồn có nhau."),
         F(3, "不可多得: 对于中国女足来说，这次比赛是一次不可多得的与强队热身锻炼的机会。 Với đội tuyển bóng đá nữ Trung Quốc, trận đấu này là một cơ hội hiếm có để khởi động, rèn luyện với đội mạnh."),
         F(4, "真金白银: 用真金白银而不是空口白话去吸引人才。 Dùng tiền thật, chứ không phải lời nói suông, để thu hút nhân tài. 空口白话 là nói suông, hứa hão. Hai cụm này đối nhau rất đẹp.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 课后练习", title="Bài tập 1: Chọn từ điền vào chỗ trống (1)", reveal=True, size=34,
    items=["## Từ cho sẵn: 喧嚣 · 休戚相关 · 尖锐 · 不可多得 · 实质 · 落实",
           "(1) ___国家乡村振兴政策，让老百姓的生活幸福感倍增。",
           "Đáp án: 落实",
           "(2) 教育孩子的___在于教育自己，以身作则是父母影响孩子的最有效的方法。",
           "Đáp án: 实质",
           "(3) 这篇文章重点突出、条理分明、语言生动，是___的佳作。",
           "Đáp án: 不可多得"],
    say=["Bây giờ chúng ta sang phần luyện tập của sách, 课后练习. Bài tập một: chọn từ thích hợp điền vào chỗ trống. Có sáu từ: 喧嚣，休戚相关，尖锐，不可多得，实质，落实.",
         F(1, "Câu một: 什么国家乡村振兴政策，让老百姓的生活幸福感倍增。 Cái gì chính sách chấn hưng nông thôn của nhà nước, khiến cảm giác hạnh phúc của người dân tăng gấp bội. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 落实. 落实政策, thực hiện chính sách, là kết hợp chúng ta vừa học."),
         F(3, "Câu hai: 教育孩子的什么在于教育自己，以身作则是父母影响孩子的最有效的方法。 Cái gì của việc dạy con nằm ở việc dạy chính mình; lấy mình làm gương là cách cha mẹ ảnh hưởng đến con hiệu quả nhất."),
         F(4, "Đáp án: 实质. 教育孩子的实质在于教育自己, bản chất của việc dạy con là dạy chính mình."),
         F(5, "Câu ba: 这篇文章重点突出、条理分明、语言生动，是什么的佳作。 Bài viết này trọng tâm nổi bật, mạch lạc, ngôn ngữ sinh động, là một tác phẩm hay thế nào?"),
         F(6, "Đáp án: 不可多得. 不可多得的佳作, một tác phẩm hay hiếm có.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 1: Chọn từ điền vào chỗ trống (2)", reveal=True, size=34,
    items=["(4) 个人命运与国家命运是___的，我们应该在实现个人抱负的同时，也为国家的发展贡献一份力量。",
           "Đáp án: 休戚相关",
           "(5) 辞职后远离城市的___，来到遥远的山村，他感到无比轻松。",
           "Đáp án: 喧嚣",
           "(6) 这位记者提出的问题十分___，他一时间不知道该如何回答。",
           "Đáp án: 尖锐"],
    say=[F(0, "Câu bốn: 个人命运与国家命运是什么的，我们应该在实现个人抱负的同时，也为国家的发展贡献一份力量。 Vận mệnh cá nhân và vận mệnh đất nước như thế nào với nhau; chúng ta nên vừa thực hiện hoài bão cá nhân, vừa góp một phần sức lực cho sự phát triển của đất nước."),
         F(1, "Đáp án: 休戚相关. Vận mệnh cá nhân và đất nước gắn bó mật thiết với nhau."),
         F(2, "Câu năm: 辞职后远离城市的什么，来到遥远的山村，他感到无比轻松。 Sau khi nghỉ việc, rời xa cái gì của thành phố, đến một làng núi xa xôi, anh ấy cảm thấy nhẹ nhõm vô cùng."),
         F(3, "Đáp án: 喧嚣. 城市的喧嚣, sự ồn ào của thành phố."),
         F(4, "Câu sáu: 这位记者提出的问题十分什么，他一时间不知道该如何回答。 Câu hỏi mà phóng viên này đưa ra rất thế nào, khiến anh ta nhất thời không biết trả lời ra sao."),
         F(5, "Đáp án: 尖锐. 问题十分尖锐, câu hỏi rất sắc bén, rất gai góc.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn đáp án đúng (1)", reveal=True, size=34,
    items=["(1) ……机遇应该各国共享，风险也需要各国联手（ ）。 A.负担 B.对付 C.应对 D.应付",
           "Đáp án: C. 应对 – 应对风险 (ứng phó rủi ro); 应付 = đối phó qua loa, 对付 = đối phó với đối thủ",
           "(2) 由于两国会谈未能取得任何进展，双方（ ）下周日再举行新一轮会谈。 A.商量 B.商定 C.制定 D.协商",
           "Đáp án: B. 商定 – đã bàn và quyết định; 商量 / 协商 chỉ là bàn bạc, 制定 dùng cho kế hoạch, luật",
           "(3) 当地方冲突（ ）为世界冲突，每个国家、每个人都不能幸免。 A.推演 B.进化 C.演算 D.演化",
           "Đáp án: D. 演化 – 演化为: biến thành, phát triển thành"],
    say=["Bài tập hai: chọn đáp án đúng.",
         F(0, "Câu một: 经济全球化是当今世界发展的趋势，机遇与风险并存，机遇应该各国共享，风险也需要各国联手什么。 Toàn cầu hóa kinh tế là xu thế của thế giới ngày nay, cơ hội và rủi ro cùng tồn tại; cơ hội thì các nước cùng hưởng, rủi ro cũng cần các nước chung tay làm gì. A, 负担; B, 对付; C, 应对; D, 应付."),
         F(1, "Đáp án: C, 应对. 应对风险 là ứng phó với rủi ro. 应付 thường mang nghĩa đối phó qua loa, chiếu lệ; 对付 là đối phó với đối thủ, kẻ địch; 负担 là gánh vác chi phí, trách nhiệm."),
         F(2, "Câu hai: 由于两国会谈未能取得任何进展，双方什么下周日再举行新一轮会谈。 Vì cuộc hội đàm giữa hai nước không đạt được tiến triển nào, hai bên làm gì là chủ nhật tuần sau sẽ tổ chức vòng hội đàm mới. A, 商量; B, 商定; C, 制定; D, 协商."),
         F(3, "Đáp án: B, 商定. Hai bên đã bàn bạc và thống nhất thời gian, tức là đã có kết quả. 商量 và 协商 chỉ là quá trình bàn bạc; 制定 dùng cho kế hoạch, pháp luật."),
         F(4, "Câu ba: 当地方冲突什么为世界冲突，每个国家、每个人都不能幸免。 Khi xung đột cục bộ làm sao thành xung đột thế giới, không quốc gia nào, không ai có thể thoát khỏi. A, 推演; B, 进化; C, 演算; D, 演化."),
         F(5, "Đáp án: D, 演化. 演化为 là biến đổi thành, phát triển thành. 进化 là tiến hóa của sinh vật; 推演 là suy diễn; 演算 là tính toán.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn đáp án đúng (2)", reveal=True, size=34,
    items=["(4) 唯有（ ）顾客至上的理念，才能使服务的品质日渐提升…… A.落实 B.达成 C.成为 D.作为",
           "Đáp án: A. 落实 – 落实理念 (thực hiện triết lý); 达成 đi với 协议 / 共识 / 目标",
           "(5) 地球是我们的家园，（ ）地球就是（ ）我们的未来。 A.拯救 B.抢救 C.挽救 D.挽留",
           "Đáp án: A. 拯救 – cứu vớt điều lớn lao; 抢救 = cấp cứu, 挽救 = cứu vãn, 挽留 = níu giữ"],
    say=[F(0, "Câu bốn: 唯有什么顾客至上的理念，才能使服务的品质日渐提升，客户方能真正成为我们的永久支持者。 Chỉ có làm gì với triết lý khách hàng là trên hết, thì chất lượng dịch vụ mới ngày càng nâng cao, khách hàng mới thật sự trở thành người ủng hộ lâu dài của chúng ta. A, 落实; B, 达成; C, 成为; D, 作为."),
         F(1, "Đáp án: A, 落实. Thực hiện triết lý khách hàng là trên hết. 达成 đi với 协议，共识，目标; còn 成为 và 作为 không đi với tân ngữ này."),
         F(2, "Câu năm: 地球是我们的家园，什么地球就是什么我们的未来。 Trái đất là ngôi nhà của chúng ta, làm gì trái đất chính là làm gì tương lai của chúng ta. A, 拯救; B, 抢救; C, 挽救; D, 挽留."),
         F(3, "Đáp án: A, 拯救. 拯救地球就是拯救我们的未来, cứu trái đất chính là cứu tương lai của chúng ta. 抢救 là cấp cứu, cứu gấp như 抢救病人; 挽救 là cứu vãn một tình thế sắp hỏng, như 挽救生命; 挽留 là níu kéo ai ở lại.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ, mẫu câu cho sẵn để trả lời (1)", reveal=True, size=33,
    items=["(1) 哥本哈根这次会议，各个国家在争吵什么？（简单一句话）",
           "Đáp án gợi ý: 简单一句话，各国争吵的就是今后自己还能排放多少二氧化碳，也就是还能使用多少能源、还有多大的发展空间。",
           "(2) 二氧化碳排放权对普通国民来讲意味着什么？（进一步地）",
           "Đáp án gợi ý: 意味着生活的改善和国家的发展，意味着自己的福利能不能进一步地增加，也意味着有没有工作。"],
    say=["Bài tập ba: dùng từ và mẫu câu cho sẵn để trả lời câu hỏi. Đây là câu hỏi mở, thầy đưa ra đáp án gợi ý.",
         F(0, "Câu một, dùng 简单一句话: 哥本哈根这次会议，各个国家在争吵什么？ Tại hội nghị Copenhagen lần này, các nước tranh cãi về điều gì? Các bạn tạm dừng và thử trả lời nhé."),
         F(1, "Đáp án gợi ý: 简单一句话，各国争吵的就是今后自己还能排放多少二氧化碳，也就是还能使用多少能源、还有多大的发展空间。 Nói gọn một câu, các nước tranh cãi về việc sau này mình còn được thải bao nhiêu khí cacbonic, tức là còn được dùng bao nhiêu năng lượng, còn bao nhiêu không gian phát triển."),
         F(2, "Câu hai, dùng 进一步地: 二氧化碳排放权对普通国民来讲意味着什么？ Quyền phát thải khí cacbonic có ý nghĩa gì với người dân bình thường?"),
         F(3, "Đáp án gợi ý: 意味着生活的改善和国家的发展，意味着自己的福利能不能进一步地增加，也意味着有没有工作。 Có nghĩa là cuộc sống được cải thiện, đất nước phát triển, phúc lợi của mình có tăng thêm được không, và có việc làm hay không.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ, mẫu câu cho sẵn để trả lời (2)", reveal=True, size=33,
    items=["(3) 丁仲礼如何看待二氧化碳的公平排放？（把……视为……）",
           "Đáp án gợi ý: 丁仲礼把排放权视为发展权，视为基本人权，所以他认为人与人之间应该有个大致相等的排放空间。",
           "(4) 人类是否能够拯救自己，最核心的问题是什么？（取决于……）",
           "Đáp án gợi ý: 人类能否拯救自己，最终取决于文化和文明，取决于能否产生一种更具包容性、更有弹性的文明。"],
    say=[F(0, "Câu ba, dùng 把什么视为什么: 丁仲礼如何看待二氧化碳的公平排放？ Ông Đinh Trọng Lễ nhìn nhận thế nào về việc phát thải khí cacbonic một cách công bằng?"),
         F(1, "Đáp án gợi ý: 丁仲礼把排放权视为发展权，视为基本人权，所以他认为人与人之间应该有个大致相等的排放空间。 Ông coi quyền phát thải là quyền phát triển, là quyền cơ bản của con người, vì vậy giữa người với người nên có không gian phát thải gần như ngang nhau."),
         F(2, "Câu bốn, dùng 取决于: 人类是否能够拯救自己，最核心的问题是什么？ Loài người có tự cứu được mình không, vấn đề cốt lõi nhất là gì?"),
         F(3, "Đáp án gợi ý: 人类能否拯救自己，最终取决于文化和文明，取决于能否产生一种更具包容性、更有弹性的文明。 Con người có tự cứu được mình hay không, cuối cùng phụ thuộc vào văn hóa và văn minh, vào việc có ra đời được một nền văn minh bao dung hơn, linh hoạt hơn hay không.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Điền từ vào đoạn văn (1)", reveal=True, size=34,
    items=["## Từ cho sẵn: 拯救 · 落实 · 排放 · 共识 · 毁灭 · 实质 · 休戚相关 · 举世瞩目",
           "人类与自然___，气候变化是人类面临的全球性问题。目前公众基本上就环保问题达成了___：全球变暖会对世界造成___性的后果，要___人类自身，减排势在必行。",
           "Đáp án: 休戚相关 · 共识 · 毁灭 · 拯救"],
    say=["Bài tập bốn: chọn từ cho sẵn điền vào đoạn văn. Có tám từ: 拯救，落实，排放，共识，毁灭，实质，休戚相关，举世瞩目. Đoạn văn chia làm hai phần.",
         F(1, "Phần một: 人类与自然什么，气候变化是人类面临的全球性问题。目前公众基本上就环保问题达成了什么：全球变暖会对世界造成什么性的后果，要什么人类自身，减排势在必行。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 人类与自然休戚相关，……公众基本上就环保问题达成了共识：全球变暖会对世界造成毁灭性的后果，要拯救人类自身，减排势在必行。 Con người và tự nhiên gắn bó mật thiết; công chúng về cơ bản đã đạt được đồng thuận về vấn đề môi trường: trái đất nóng lên sẽ gây ra hậu quả mang tính hủy diệt, muốn cứu lấy chính loài người thì giảm phát thải là việc bắt buộc phải làm. Các bạn để ý, ở đây lại gặp mẫu câu 就……达成共识, và ý tưởng 拯救人类自身 của ông Đinh.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Điền từ vào đoạn văn (2)", reveal=True, size=32,
    items=["在___的第26届联合国气候变化大会上，中国提出：二氧化碳___力争2030年前达到峰值，2060年实现碳中和。___这样的计划，对于中国这个最大的发展中国家来说，绝非易事。……碳达峰、碳中和立足于国家利益和人类共同利益的平衡，___上是一个倒逼机制……",
           "Đáp án: 举世瞩目 · 排放 · 落实 · 实质",
           "Chú thích: 碳达峰 = đạt đỉnh phát thải · 碳中和 = trung hòa carbon · 倒逼机制 = cơ chế tạo sức ép buộc phải thay đổi"],
    say=[F(0, "Phần hai: 在什么的第二十六届联合国气候变化大会上，中国提出：二氧化碳什么力争二零三零年前达到峰值，二零六零年实现碳中和。什么这样的计划，对于中国这个最大的发展中国家来说，绝非易事。 Tiếp theo: 国家气候战略中心战略规划部主任柴麒敏认为，碳达峰、碳中和立足于国家利益和人类共同利益的平衡，什么上是一个倒逼机制。"),
         F(1, "Đáp án: 举世瞩目的第二十六届联合国气候变化大会, hội nghị COP hai mươi sáu được cả thế giới chú ý; 二氧化碳排放力争二零三零年前达到峰值, phát thải khí cacbonic phấn đấu đạt đỉnh trước năm 2030; 落实这样的计划, thực hiện kế hoạch như vậy; và 实质上是一个倒逼机制, về thực chất là một cơ chế tạo sức ép."),
         F(2, "Hai thuật ngữ trong chú thích, chúng ta đã học trong phần từ mới: 碳达峰, đạt đỉnh phát thải, và 碳中和, trung hòa carbon. Còn 倒逼机制 là cơ chế dùng áp lực từ mục tiêu để buộc nền kinh tế phải chuyển đổi, phát triển chất lượng cao hơn.")])

# ======================= THẢO LUẬN =======================
add("bullets", chapter="Thảo luận", section="Thảo luận 讨论", title="Thảo luận: chiếc bánh nên chia thế nào?", reveal=True, size=33,
    items=["你同意丁仲礼“按人均分配排放权”的公平观吗？为什么？",
           "Đáp án gợi ý: 我基本同意。发达国家在工业化过程中已经排放了大量二氧化碳，人均排放也远远高于发展中国家，所以应该承担更多的减排责任。不过，发展中国家也不能走“先污染，后治理”的老路。",
           "## Liên hệ Việt Nam",
           "Cam kết tại COP26 (2021): phát thải ròng bằng 0 vào năm 2050 · phát triển điện mặt trời, điện gió",
           "Thử nói: 越南提出到2050年实现净零排放。在发展经济的同时减少排放，越南面临哪些挑战？"],
    say=["Bây giờ chúng ta cùng thảo luận. Câu hỏi: 你同意丁仲礼按人均分配排放权的公平观吗？为什么？ Bạn có đồng ý với quan điểm công bằng của ông Đinh, tức là phân chia quyền phát thải theo đầu người không? Vì sao?",
         F(0, "Các bạn tạm dừng video, thử nói vài câu bằng tiếng Trung, dùng các từ vừa học như 人均，公允，把什么视为什么，取决于."),
         F(1, "Đáp án gợi ý: 我基本同意。发达国家在工业化过程中已经排放了大量二氧化碳，人均排放也远远高于发展中国家，所以应该承担更多的减排责任。不过，发展中国家也不能走先污染，后治理的老路。 Tôi về cơ bản đồng ý. Các nước phát triển đã thải ra lượng lớn khí cacbonic trong quá trình công nghiệp hóa, phát thải bình quân đầu người cũng cao hơn nhiều, nên phải gánh nhiều trách nhiệm giảm phát thải hơn. Tuy vậy, các nước đang phát triển cũng không thể đi lại con đường cũ: ô nhiễm trước, xử lý sau."),
         F(2, "Còn Việt Nam thì sao?"),
         F(3, "Tại hội nghị COP hai mươi sáu năm 2021, Việt Nam đã cam kết đạt mức phát thải ròng bằng không vào năm 2050, tức là 碳中和. Điện mặt trời và điện gió ở nước ta đã phát triển rất nhanh trong những năm gần đây."),
         F(4, "Các bạn thử nói: 越南提出到二零五零年实现净零排放。在发展经济的同时减少排放，越南面临哪些挑战？ Việt Nam đặt mục tiêu phát thải ròng bằng không vào năm 2050. Vừa phát triển kinh tế vừa giảm phát thải, Việt Nam đối mặt với những thách thức nào? 净零排放 là phát thải ròng bằng không. Đây cũng là một đề tài rất hay để viết bài luận.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết", section="Tổng kết", title="Tổng kết bài 3.1", size=34,
    items=["Từ vựng trọng tâm: 减排 · 排放 · 应对 · 共识 · 尾声 · 实质 · 能源 · 人均 · 基数 · 稀缺 · 配额 · 公允 · 落实 · 拯救 · 取决",
           "Thành ngữ: 举世瞩目 · 硝烟四起 · 休戚相关 · 不可多得 · 真金白银",
           "Mẫu câu: 就……+V · 简单一句话 · 进一步 · 也就是说 · 有失/有待 · 把……视为…… · 有的是 · 取决于",
           "Ý chính: 排放权 = 发展权 → công bằng là 人与人之间大致相等的排放空间",
           "## Bài tập về nhà",
           "Viết đoạn văn 300 chữ: 你怎么看“碳排放的蛋糕”？ (dùng ít nhất 3 mẫu câu của bài)"],
    say=["Chúng ta cùng tổng kết bài ba chấm một.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ những từ chính luận về môi trường: 减排，排放，应对，共识，尾声，实质，能源，人均，基数，稀缺，配额，公允，落实，拯救，取决."),
         F(1, "Năm thành ngữ: 举世瞩目，硝烟四起，休戚相关，不可多得，真金白银."),
         F(2, "Tám mẫu câu: giới từ 就 dẫn ra đề tài; 简单一句话 để tóm lại; 进一步 tiến thêm một bước; 也就是说 để giải thích; 有 cộng động từ đơn âm tiết như 有失，有待; 把什么视为什么; 有的是 nhấn mạnh rất nhiều; và 取决于."),
         F(3, "Về nội dung: ông Đinh Trọng Lễ coi quyền phát thải là quyền phát triển, nên công bằng nghĩa là mỗi người có một không gian phát thải gần như ngang nhau; và con người không cần cứu trái đất, mà cần tự cứu mình."),
         F(5, "Bài tập về nhà: hãy viết một đoạn văn khoảng ba trăm chữ với đề 你怎么看碳排放的蛋糕, bạn nghĩ gì về chiếc bánh phát thải carbon. Cố gắng dùng ít nhất ba mẫu câu của bài, như 简单一句话，把什么视为什么，取决于."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Bài sau, bài ba chấm hai, chúng ta sẽ chuyển từ chuyện toàn cầu về chuyện rất đời thường: phân loại rác. Tên bài là: 随手扔还是随手分，你拎得清吗？ Tiện tay vứt hay tiện tay phân loại, bạn có rõ không? Chúng ta sẽ đến Thượng Hải, nơi phân loại rác trở thành chuyện ai cũng bàn tán. Hẹn gặp lại các bạn. Chúc các bạn học tốt!"])

lesson = {
    "title": "顶石中文 – Bài 3.1: 碳排放的“蛋糕”怎么切？ (Chia “chiếc bánh” phát thải carbon thế nào?)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"应对": "映对",            # yìngduì
                    "效应": "效映",            # xiàoyìng
                    "落实": "洛实",            # luòshí
                    "基数": "基树",            # jīshù
                    "物种": "物肿",            # wùzhǒng
                    "弹性": "谈性",            # tánxìng
                    "种瓜得瓜": "众瓜得瓜",    # zhòng guā
                    "种豆得豆": "众豆得豆",    # zhòng dòu
                    "视为": "视维",            # shìwéi
                    "演化为": "演化维",        # yǎnhuà wéi
                    "为世界冲突": "维世界冲突",  # wéi
                    "体现为": "体现维",        # tǐxiàn wéi
                    "称为": "称维",            # chēngwéi
                    "为国家的发展": "位国家的发展",  # wèi
                    "相等": "相等",
                    "处理": "楚理",            # chǔlǐ
                    "琐事": "琐事",
                    "调整": "条整",            # tiáozhěng
                    "角色": "决色",            # juésè
                    "强队": "强队",
                    "规划": "规话",            # guīhuà
                    "倒逼": "到逼",            # dàobī
                    "过硬": "过硬",
                    "发人深省": "发人深醒",    # fā rén shēn xǐng
                    "好好的": "好好的",
                    "得买": "得买",
                    "空口白话": "空口白话",
                    "一时间": "一时间"},
    "slides": slides,
}
# bỏ các cặp giữ nguyên (chỉ để ghi nhớ đã kiểm tra)
lesson["tts_replace"] = {k: v for k, v in lesson["tts_replace"].items() if k != v}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds31.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
