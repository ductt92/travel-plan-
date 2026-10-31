#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Thượng) – Bài 2 «父母之爱». Chạy để sinh bai02.json."""
import json
import os

TAG = "HSK 6 (Thượng) · Bài 2 · 父母之爱"
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
    zh="父母之爱", py="Fùmǔ zhī ài", vi="Bài 2: Tình yêu của ba mẹ",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Thượng.",
         "Hôm nay chúng ta học bài hai: 父母之爱。 Nghĩa là: Tình yêu của ba mẹ.",
         "Đây là bài thứ hai của Chủ đề một, 生活点滴, những giọt nhỏ của cuộc sống. Bài khóa kể về một cô sinh viên lần đầu xa nhà. Kỳ nghỉ đến, ba mẹ lại bảo cô đừng về, khiến cô rất buồn và trách ba mẹ. Mãi đến năm thứ ba đại học, cô mới hiểu ra tình yêu thầm lặng ẩn sau quyết định ấy."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu nội dung bài khóa 父母之爱 – tình yêu thầm lặng của ba mẹ",
           "Nắm vững 44 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: 恨不得 · 顿时 · 不由得",
           "Phân biệt hai động từ 体谅 và 原谅",
           "Kỹ năng viết: cách kể chuyện có nút thắt, mô phỏng đoạn văn",
           "Mở rộng: 10 động từ chỉ động tác của tay, thân người"],
    say=["Bài học hôm nay có sáu mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa, và cảm nhận tình yêu thầm lặng mà ba mẹ dành cho con cái."),
         F(1, "Thứ hai, nắm vững bốn mươi bốn từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học ba điểm ngữ pháp: 恨不得，顿时 và 不由得. Cả ba đều xuất hiện trong bài khóa."),
         F(3, "Thứ tư, phân biệt hai động từ đều liên quan đến sự cảm thông: 体谅 và 原谅."),
         F(4, "Thứ năm, kỹ năng viết: học cách kể một câu chuyện có nút thắt và mở nút như bài khóa, rồi tập mô phỏng các đoạn văn mẫu."),
         F(5, "Thứ sáu, phần mở rộng: mười động từ chỉ động tác, như bẻ, dìu, vác, gặm, phơi."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Câu hỏi khởi động", size=38,
    items=["中国有句俗话：“打是亲，骂是爱”，你能理解吗？",
           "下面这些事情中，你觉得父母做得对不对？为什么？",
           "(1) 帮孩子做所有的事情。 (2) 为了了解孩子，偷看孩子的日记。",
           "(3) 让孩子分担家务。 (4) 假期让孩子去打工赚自己的零花钱。",
           "(5) 对孩子的事情不闻不问。 (6) 孩子做错了事情，打骂孩子。"],
    say=["Chúng ta bắt đầu bằng phần khởi động.",
         F(0, "中国有句俗话：打是亲，骂是爱，你能理解吗？ Trung Quốc có câu tục ngữ: đánh là thương, mắng là yêu. Bạn có hiểu được không? Câu này giống câu thương cho roi cho vọt của tiếng Việt."),
         F(1, "下面这些事情中，你觉得父母做得对不对？为什么？ Trong những việc dưới đây, bạn thấy ba mẹ làm đúng hay sai? Tại sao?"),
         F(2, "Việc thứ nhất: 帮孩子做所有的事情。 Làm giúp con mọi việc. Việc thứ hai: 为了了解孩子，偷看孩子的日记。 Để hiểu con, lén đọc nhật ký của con. 偷看 là xem trộm."),
         F(3, "Việc thứ ba: 让孩子分担家务。 Cho con chia sẻ việc nhà. Việc thứ tư: 假期让孩子去打工赚自己的零花钱。 Kỳ nghỉ cho con đi làm thêm kiếm tiền tiêu vặt. 零花钱 là tiền tiêu vặt."),
         F(4, "Việc thứ năm: 对孩子的事情不闻不问。 Không đoái hoài gì đến chuyện của con. 不闻不问 nghĩa đen là không nghe không hỏi. Việc thứ sáu: 孩子做错了事情，打骂孩子。 Con làm sai thì đánh mắng con."),
         "Các bạn hãy tạm dừng video, chọn một việc và nói ý kiến của mình bằng tiếng Trung, ví dụ: 我觉得让孩子分担家务是对的，因为这样可以培养孩子的独立能力。 Sau đó hãy xem tiếp nhé."])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 光 và 爱", size=36,
    items=["## 光 (quang): ánh sáng",
           "阳光 ánh nắng · 月光 ánh trăng · 星光 ánh sao · 灯光 ánh đèn · 火光 ánh lửa",
           "发光 phát sáng · 放光 tỏa sáng · 光明 ánh sáng, tươi sáng · 光亮 sáng sủa",
           "## 爱 (ái): yêu",
           "亲爱 thân yêu · 可爱 đáng yêu · 热爱 yêu tha thiết · 疼爱 thương yêu · 友爱 thân ái · 恋爱 yêu đương · 关爱 quan tâm yêu thương",
           "求爱 tỏ tình · 相爱 yêu nhau · 爱情 tình yêu · 爱心 lòng nhân ái · 爱护 yêu quý giữ gìn · 爱惜 quý trọng · 爱好 sở thích"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo, rất có lợi cho người Việt vì hầu hết các chữ đều có âm Hán Việt quen thuộc.",
         F(0, "Nhóm thứ nhất có chữ 光, Hán Việt là quang, nghĩa là ánh sáng, như trong quang minh, quang cảnh."),
         F(1, "阳光，月光，星光，灯光，火光。 Tức là: ánh nắng, ánh trăng, ánh sao, ánh đèn, ánh lửa. Trong bài khóa có cụm 灯光下, dưới ánh đèn."),
         F(2, "发光，放光，光明，光亮。 Tức là: phát sáng, tỏa sáng, ánh sáng tươi sáng, và sáng sủa."),
         F(3, "Nhóm thứ hai có chữ 爱, Hán Việt là ái, nghĩa là yêu, như trong ái tình, ái quốc. Tên bài hôm nay cũng có chữ này: 父母之爱."),
         F(4, "亲爱，可爱，热爱，疼爱，友爱，恋爱，关爱。 Tức là: thân yêu, đáng yêu, yêu tha thiết, thương yêu, thân ái, yêu đương, quan tâm yêu thương."),
         F(5, "求爱，相爱，爱情，爱心，爱护，爱惜，爱好。 Tức là: tỏ tình, yêu nhau, tình yêu, lòng nhân ái, yêu quý giữ gìn, quý trọng, và sở thích. Bài khóa có cụm 有爱的家庭, gia đình đầy tình yêu thương.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 自 và 心", size=36,
    items=["## 自 (tự): tự mình, bản thân",
           "自动 tự động · 自豪 tự hào · 自觉 tự giác · 自私 ích kỷ · 自由 tự do · 自愿 tự nguyện",
           "自信 tự tin · 自责 tự trách · 自夸 tự khoe · 自救 tự cứu · 亲自 đích thân · 各自 mỗi người, riêng",
           "## 心 (tâm): lòng, tim",
           "放心 yên tâm · 关心 quan tâm · 小心 cẩn thận · 粗心 cẩu thả · 开心 vui vẻ · 耐心 kiên nhẫn · 伤心 đau lòng · 专心 chuyên tâm",
           "信心 niềm tin · 爱心 lòng nhân ái · 决心 quyết tâm · 热心 nhiệt tình · 心情 tâm trạng · 心理 tâm lý · 心脏 quả tim"],
    say=[F(0, "Nhóm thứ ba có chữ 自, Hán Việt là tự, nghĩa là tự mình, bản thân."),
         F(1, "自动，自豪，自觉，自私，自由，自愿。 Tức là: tự động, tự hào, tự giác, ích kỷ, tự do, tự nguyện. Chú ý 自私 Hán Việt là tự tư, nhưng nghĩa là ích kỷ, chỉ nghĩ cho riêng mình."),
         F(2, "自信，自责，自夸，自救，亲自，各自。 Tức là: tự tin, tự trách, tự khoe, tự cứu, đích thân, và mỗi người. Bài khóa có cụm 独立自主, độc lập tự chủ."),
         F(3, "Nhóm cuối cùng có chữ 心, Hán Việt là tâm, nghĩa là lòng, trái tim."),
         F(4, "放心，关心，小心，粗心，开心，耐心，伤心，专心。 Tức là: yên tâm, quan tâm, cẩn thận, cẩu thả, vui vẻ, kiên nhẫn, đau lòng, chuyên tâm. Chú ý 小心 không phải tiểu tâm theo nghĩa hẹp hòi, mà là cẩn thận."),
         F(5, "信心，爱心，决心，热心，心情，心理，心脏。 Tức là: niềm tin, lòng nhân ái, quyết tâm, nhiệt tình, tâm trạng, tâm lý, và quả tim. Trong bài khóa còn có 心疼, xót xa, thương xót."),
         "Các bạn thấy không, chỉ cần nắm nghĩa của một chữ gốc, ta có thể đoán được nghĩa của cả một nhóm từ. Hãy áp dụng cách này khi học từ mới nhé."])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng)
V = [
    ("和蔼", "hé'ǎi", "hòa ái", "tính từ", "hòa nhã, ôn hòa, dễ gần", "老师对学生态度和蔼。", "Thầy giáo có thái độ ôn hòa với học sinh.",
     "Tính từ, nghĩa là hòa nhã, ôn hòa, dễ gần. Thường dùng để tả thái độ của người lớn tuổi, người bề trên đối với người dưới. Hay gặp trong cụm 态度和蔼 và 和蔼可亲."),
    ("和气", "héqi", "hòa khí", "tính từ", "nhã nhặn, ôn tồn; hòa thuận", "他说话总是很和气。", "Anh ấy nói chuyện lúc nào cũng nhã nhặn.",
     "Tính từ, nghĩa là nhã nhặn, ôn tồn, hòa thuận. Chú ý chữ thứ hai đọc thanh nhẹ. Trong tiếng Việt, hòa khí là bầu không khí hòa thuận; tiếng Trung cũng có nghĩa đó, nhưng hay dùng nhất là tả cách nói năng nhã nhặn: 说话和气."),
    ("目光", "mùguāng", "mục quang", "danh từ", "ánh mắt", "她的目光中充满了期待。", "Ánh mắt cô ấy tràn đầy mong đợi.",
     "Danh từ, nghĩa là ánh mắt. Ngoài ra còn có nghĩa bóng là tầm nhìn, ví dụ 目光远大, tầm nhìn xa trông rộng."),
    ("慈祥", "cíxiáng", "từ tường", "tính từ", "hiền từ, hiền hậu (người lớn tuổi)", "奶奶慈祥地笑了。", "Bà nội mỉm cười hiền từ.",
     "Tính từ, nghĩa là hiền từ, hiền hậu. Chỉ dùng cho người lớn tuổi như ông bà, cha mẹ, không dùng cho người trẻ."),
    ("跨", "kuà", "khóa", "động từ", "bước (dài) qua, bước vào; vượt qua", "他跨进了大学的校门。", "Cậu ấy đã bước chân vào cổng trường đại học.",
     "Động từ, nghĩa là bước một bước dài qua, bước vào. Nghĩa mở rộng là vượt qua ranh giới, ví dụ 跨国公司, công ty đa quốc gia."),
    ("自主", "zìzhǔ", "tự chủ", "động từ", "tự chủ, tự quyết định", "孩子要学会独立自主。", "Trẻ con phải học cách độc lập tự chủ.",
     "Động từ, nghĩa là tự chủ, tự mình quyết định, không phụ thuộc người khác. Âm Hán Việt giống hệt tiếng Việt. Hay đi thành cụm 独立自主."),
    ("甭", "béng", "bằng", "phó từ", "khỏi, không cần (khẩu ngữ)", "你甭担心，我自己能行。", "Bạn khỏi lo, mình tự làm được.",
     "Phó từ khẩu ngữ, hay dùng ở miền Bắc Trung Quốc. Chữ này được ghép từ hai chữ 不 và 用, đọc liền lại thành béng, nghĩa là không cần, khỏi. Trong bài có cụm 更甭提了, càng khỏi phải nói."),
    ("脱离", "tuōlí", "thoát ly", "động từ", "thoát khỏi, rời khỏi", "病人已经脱离了危险。", "Bệnh nhân đã qua cơn nguy hiểm.",
     "Động từ, nghĩa là thoát khỏi, rời khỏi một hoàn cảnh hay một chỗ dựa. Trong bài: 脱离父母, rời xa vòng tay ba mẹ."),
    ("诱惑", "yòuhuò", "dụ hoặc", "động từ", "cám dỗ; sức hấp dẫn, lôi cuốn", "美食的诱惑很难抵挡。", "Sự cám dỗ của món ngon rất khó cưỡng lại.",
     "Động từ, nghĩa là cám dỗ, lôi cuốn. Cẩn thận: tiếng Việt thường hiểu cám dỗ theo nghĩa xấu, nhưng trong bài, 诱惑 mang nghĩa tích cực là sức hấp dẫn: cuộc sống tự lập có sức hấp dẫn rất lớn."),
    ("无比", "wúbǐ", "vô tỷ", "động từ", "vô cùng, không gì sánh bằng", "听到这个好消息，大家无比高兴。", "Nghe tin vui này, mọi người vô cùng vui mừng.",
     "Nghĩa là không gì sánh được, tức là vô cùng. Thường đứng trước tính từ hoặc động từ tâm lý, mang sắc thái văn viết, mạnh hơn 非常."),
    ("向往", "xiàngwǎng", "hướng vãng", "động từ", "mong mỏi, khao khát, hướng tới", "我一直向往大城市的生活。", "Tôi luôn khao khát cuộc sống ở thành phố lớn.",
     "Động từ, nghĩa là mong mỏi, khao khát, lòng luôn hướng tới một điều tốt đẹp."),
    ("孤独", "gūdú", "cô độc", "tính từ", "cô đơn, cô độc", "一个人在国外，难免感到孤独。", "Một mình ở nước ngoài, khó tránh khỏi cảm thấy cô đơn.",
     "Tính từ, nghĩa là cô đơn, cô độc. Trong bài có cụm 孤独感, cảm giác cô đơn."),
    ("哭鼻子", "kū bízi", "khốc tỵ tử", "động từ", "khóc nhè, khóc mếu máo (khẩu ngữ)", "这么大了还哭鼻子！", "Lớn thế này rồi mà còn khóc nhè!",
     "Cách nói khẩu ngữ, nghĩa là khóc nhè, khóc mếu máo, có chút trêu đùa. Đừng dịch từng chữ thành khóc mũi nhé."),
    ("片刻", "piànkè", "phiến khắc", "danh từ", "chốc lát, một lát", "请您稍等片刻。", "Xin quý khách vui lòng đợi một lát.",
     "Danh từ, nghĩa là chốc lát, một thời gian rất ngắn. Trong bài: 片刻不停, không dừng lại phút nào."),
    ("步伐", "bùfá", "bộ phạt", "danh từ", "bước chân, nhịp bước", "我们要加快改革的步伐。", "Chúng ta phải đẩy nhanh bước tiến cải cách.",
     "Danh từ, nghĩa là bước chân, nhịp bước. Nghĩa bóng là tiến độ, bước tiến của một sự việc."),
    ("包围", "bāowéi", "bao vi", "động từ", "bao quanh, vây quanh", "这个小村子被大山包围着。", "Ngôi làng nhỏ này được núi non bao quanh.",
     "Động từ, nghĩa là bao quanh, vây quanh. Trong bài dùng nghĩa bóng: 被亲情包围, được tình thân bao bọc."),
    ("感染", "gǎnrǎn", "cảm nhiễm", "động từ", "lây nhiễm; truyền (cảm xúc) sang", "他的笑声感染了每一个人。", "Tiếng cười của anh ấy lan sang mọi người.",
     "Động từ. Nghĩa thứ nhất là lây nhiễm bệnh, giống cảm nhiễm trong tiếng Việt. Nhưng chú ý: nghĩa thứ hai, cũng là nghĩa trong bài, là làm cho cảm xúc của mình lan sang người khác."),
    ("恨不得", "hènbude", "hận bất đắc", "động từ", "nóng lòng muốn, chỉ mong sao", "我恨不得马上见到你。", "Tôi chỉ mong được gặp bạn ngay lập tức.",
     "Động từ, nghĩa là nóng lòng muốn, chỉ mong sao được làm ngay. Cẩn thận: dù có chữ hận, từ này không hề mang nghĩa căm ghét. Đây là điểm ngữ pháp thứ nhất của bài."),
    ("跟前", "gēnqián", "cân tiền", "danh từ", "bên cạnh, trước mặt (gần sát)", "孩子跑到妈妈跟前。", "Đứa bé chạy đến bên mẹ.",
     "Danh từ, nghĩa là ngay bên cạnh, ngay trước mặt, chỉ vị trí rất gần một người."),
    ("团圆", "tuányuán", "đoàn viên", "động từ", "đoàn tụ, sum họp", "春节是全家团圆的日子。", "Tết là ngày cả nhà đoàn tụ.",
     "Động từ, nghĩa là đoàn tụ, sum họp gia đình. Cẩn thận: đoàn viên theo nghĩa thành viên của Đoàn thanh niên là một từ khác, viết là 团员."),
    ("近来", "jìnlái", "cận lai", "danh từ", "dạo này, gần đây", "你近来身体怎么样？", "Dạo này sức khỏe bạn thế nào?",
     "Danh từ, nghĩa là dạo này, khoảng thời gian gần đây cho đến hiện tại."),
    ("酝酿", "yùnniàng", "uấn nhưỡng", "động từ", "ấp ủ, nung nấu, chuẩn bị (từ lâu)", "这个计划已经酝酿了很久。", "Kế hoạch này đã được ấp ủ từ lâu.",
     "Động từ. Nghĩa gốc là ủ rượu; nghĩa bóng là ấp ủ, nung nấu, chuẩn bị dần dần một ý định hay một cảm xúc. Trong bài: 酝酿已久的恋家情绪, tâm trạng nhớ nhà ấp ủ đã lâu."),
    ("刹那", "chànà", "sát na", "danh từ", "khoảnh khắc, chốc lát", "那一刹那，我明白了一切。", "Trong khoảnh khắc ấy, tôi hiểu ra tất cả.",
     "Danh từ, nghĩa là khoảnh khắc. Từ này vốn là thuật ngữ nhà Phật, tiếng Việt cũng có từ sát na. Chú ý chữ đầu đọc là chà, thanh bốn, khác với cách đọc trong từ phanh xe."),
    ("反常", "fǎncháng", "phản thường", "tính từ", "khác thường, bất thường", "最近的天气有点儿反常。", "Thời tiết dạo này hơi bất thường.",
     "Tính từ, nghĩa là khác thường, trái với bình thường."),
    ("埋怨", "mányuàn", "mai oán", "động từ", "oán trách, phàn nàn, trách móc", "他总是埋怨别人。", "Anh ta lúc nào cũng trách móc người khác.",
     "Động từ, nghĩa là oán trách, phàn nàn. Chú ý: chữ đầu ở đây đọc là mán, thanh hai, chứ không đọc mái như khi mang nghĩa chôn, vùi."),
    ("体谅", "tǐliàng", "thể lượng", "động từ", "thông cảm, cảm thông", "父母很体谅孩子的辛苦。", "Ba mẹ rất thông cảm với sự vất vả của con.",
     "Động từ, nghĩa là thông cảm, đặt mình vào hoàn cảnh người khác để hiểu cho họ. Lát nữa ta sẽ so sánh từ này với 原谅."),
    ("无精打采", "wújīng-dǎcǎi", "vô tinh đả thải", "thành ngữ", "ủ rũ, phờ phạc, thiếu sức sống", "他今天看起来无精打采的。", "Hôm nay trông anh ấy ủ rũ thế nào ấy.",
     "Thành ngữ, nghĩa là ủ rũ, phờ phạc, không có chút tinh thần nào."),
    ("规划", "guīhuà", "quy hoạch", "động từ", "lên kế hoạch, hoạch định", "你应该好好规划一下自己的未来。", "Bạn nên lên kế hoạch kỹ cho tương lai của mình.",
     "Động từ, nghĩa là lên kế hoạch. Cẩn thận: trong tiếng Việt, quy hoạch thường dùng cho đất đai, đô thị; còn tiếng Trung dùng rộng hơn, kể cả việc lên kế hoạch cho kỳ nghỉ hay tương lai."),
    ("熬", "áo", "ngao", "động từ", "chịu đựng, cố vượt qua; ninh, sắc", "他熬过了最困难的日子。", "Anh ấy đã vượt qua những ngày khó khăn nhất.",
     "Động từ. Nghĩa gốc là ninh, sắc, ví dụ 熬汤, ninh canh. Nghĩa bóng là cố chịu đựng cho qua, ví dụ 熬夜, thức khuya. Trong bài: 熬过漫长的假期."),
    ("漫长", "màncháng", "mạn trường", "tính từ", "dài đằng đẵng", "漫长的冬天终于过去了。", "Mùa đông dài đằng đẵng cuối cùng cũng qua.",
     "Tính từ, nghĩa là dài đằng đẵng, dùng cho thời gian hoặc con đường."),
    ("寂静", "jìjìng", "tịch tĩnh", "tính từ", "vắng lặng, yên ắng", "夜深了，四周一片寂静。", "Đêm đã khuya, xung quanh vắng lặng.",
     "Tính từ, nghĩa là vắng lặng, không có một tiếng động nào, mang sắc thái văn viết, hay dùng để tả cảnh."),
    ("稿件", "gǎojiàn", "cảo kiện", "danh từ", "bài viết, bản thảo (gửi đăng)", "编辑每天要看很多稿件。", "Biên tập viên mỗi ngày phải đọc rất nhiều bản thảo.",
     "Danh từ, nghĩa là bài viết, bản thảo gửi cho báo, tạp chí hoặc nhà xuất bản."),
    ("难得", "nándé", "nan đắc", "tính từ", "hiếm có, khó có được", "这是一个难得的机会。", "Đây là một cơ hội hiếm có.",
     "Tính từ, nghĩa là hiếm có, khó có được, vì vậy rất đáng quý."),
    ("心疼", "xīnténg", "tâm đông", "động từ", "thương xót, xót xa; tiếc (của)", "看到孩子受伤，妈妈很心疼。", "Thấy con bị thương, mẹ rất xót xa.",
     "Động từ. Cẩn thận: từ này không có nghĩa là đau tim. Nghĩa là thương xót, xót xa cho người mình yêu; ngoài ra còn có nghĩa là tiếc của, ví dụ 心疼钱."),
    ("掩饰", "yǎnshì", "yểm sức", "động từ", "che đậy, che giấu (cảm xúc, khuyết điểm)", "她努力掩饰自己的紧张。", "Cô ấy cố gắng che giấu sự căng thẳng của mình.",
     "Động từ, nghĩa là che đậy, che giấu, thường dùng với cảm xúc, khuyết điểm, sai lầm."),
    ("隐瞒", "yǐnmán", "ẩn man", "động từ", "giấu giếm, giấu kín (sự thật)", "你不应该向父母隐瞒真相。", "Bạn không nên giấu ba mẹ sự thật.",
     "Động từ, nghĩa là giấu giếm. Khác với 掩饰: 掩饰 là che đi cảm xúc, khuyết điểm; còn 隐瞒 là giấu sự thật, thông tin, không cho người khác biết."),
    ("唠叨", "láodao", "lao thao", "động từ", "càm ràm, nói đi nói lại, lải nhải", "妈妈又在唠叨了。", "Mẹ lại đang càm ràm rồi.",
     "Động từ, nghĩa là nói đi nói lại mãi, càm ràm. Chữ thứ hai đọc thanh nhẹ. Trong bài, từ này không mang nghĩa xấu, mà cho thấy mẹ cứ nhắc mãi vì thương con."),
    ("吃苦", "chī kǔ", "cật khổ", "động từ", "chịu khổ, chịu cực", "年轻人要能吃苦。", "Người trẻ phải chịu được khổ.",
     "Động từ ly hợp, nghĩa là chịu khổ, chịu cực, đừng dịch từng chữ thành ăn đắng nhé. Ngược nghĩa với 享福, hưởng phúc."),
    ("欣慰", "xīnwèi", "hân úy", "tính từ", "vui mừng và yên lòng, mãn nguyện", "看到孩子这么懂事，父母很欣慰。", "Thấy con hiểu chuyện như vậy, ba mẹ rất mãn nguyện.",
     "Tính từ, nghĩa là vui mừng và yên lòng, mãn nguyện, thường là cảm xúc của bề trên khi thấy người dưới tiến bộ."),
    ("本事", "běnshi", "bản sự", "danh từ", "bản lĩnh, năng lực, tài cán", "他很有本事，什么都会做。", "Anh ấy rất giỏi, việc gì cũng làm được.",
     "Danh từ, nghĩa là bản lĩnh, năng lực, tài cán, chữ thứ hai đọc thanh nhẹ. Trong bài có câu 不吃苦，怎么长本事, không chịu khổ thì làm sao có bản lĩnh."),
    ("皱纹", "zhòuwén", "trứu văn", "danh từ", "nếp nhăn", "爷爷的脸上布满了皱纹。", "Gương mặt ông nội đầy những nếp nhăn.",
     "Danh từ, nghĩa là nếp nhăn trên da."),
    ("顿时", "dùnshí", "đốn thời", "phó từ", "ngay lập tức, bỗng chốc", "听到这个消息，他顿时愣住了。", "Nghe tin này, anh ấy lập tức sững người.",
     "Phó từ, nghĩa là ngay lập tức, bỗng chốc. Đây là điểm ngữ pháp thứ hai."),
    ("不由得", "bùyóude", "bất do đắc", "phó từ", "bất giác, không kìm được", "想起家乡，我不由得流下了眼泪。", "Nhớ về quê hương, tôi bất giác rơi nước mắt.",
     "Phó từ, nghĩa là bất giác, không kìm được. Đây là điểm ngữ pháp thứ ba."),
    ("热泪盈眶", "rèlèi yíng kuàng", "nhiệt lệ doanh khuông", "thành ngữ", "nước mắt lưng tròng, rưng rưng", "听完他的故事，大家都热泪盈眶。", "Nghe xong câu chuyện của anh ấy, ai nấy đều rưng rưng nước mắt.",
     "Thành ngữ. 热泪 là nước mắt nóng, 盈 là đầy, 眶 là hốc mắt. Cả câu nghĩa là nước mắt lưng tròng vì xúc động."),
]

add("bullets", chapter="Từ mới (44 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 2 có 44 từ mới, chia thành 15 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 甭 (béng) · 刹那 (chà) · 埋怨 (mán) · 熬 (áo) · 和气, 唠叨, 本事 (thanh nhẹ)"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có bốn mươi bốn từ, thầy chia thành mười lăm nhóm nhỏ, mỗi nhóm hai hoặc ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số từ có âm đọc đặc biệt, thầy sẽ nhắc khi gặp. Bài này cũng có nhiều từ Hán Việt giống hệt tiếng Việt như 自主，孤独，团圆, nhưng cũng có những từ dễ hiểu nhầm như 心疼，感染，规划. Chúng ta bắt đầu nhé.")])

sizes = [3] * 14 + [2]
assert sum(sizes) == len(V)
g = 0
for gs in sizes:
    group = V[g:g + gs]
    words, say = [], []
    for i, (zh, py, hv, loai, vi, ex, exvi, expl) in enumerate(group):
        n = g + i + 1
        words.append({"zh": zh, "py": py, "hv": hv.upper(), "loai": f"{n}. {loai}", "vi": vi, "ex": ex, "exvi": exvi})
        say.append(F(i, f"Từ số {n}: {zh}。 {zh}。 Hán Việt là {hv}.", zr=120))
        say.append(F(i, f"{expl} Ví dụ: {ex}{'' if ex[-1] in '。…？！，' else '，'} {exvi[0].upper() + exvi[1:]}{'' if exvi.endswith(('.', '!', '?')) else '.'}", zr=130))
    add("vocab", section="Từ mới 生词", title=f"Từ mới ({g + 1}–{g + len(group)} / {len(V)})",
        words=words, say=say)
    g += gs

# ======================= BÀI KHÓA =======================
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung nếu khác])
P = [
    ("我从小生活在一个有爱的家庭，父母感情和睦，很少吵架，他们对我态度和蔼，说话和气，目光中都充满着慈祥。",
     "Tôi lớn lên trong một gia đình đầy tình yêu thương. Ba mẹ tôi tình cảm hòa thuận, rất ít khi cãi nhau. Với tôi, ba mẹ luôn ôn hòa, nói năng nhã nhặn, trong ánh mắt lúc nào cũng tràn đầy sự hiền từ.",
     ["从小 là từ nhỏ. 和睦 là hòa thuận, hay dùng cho quan hệ trong gia đình. 吵架 là cãi nhau.",
      "Mẫu câu 对 cộng người cộng 态度 cộng tính từ: 对我态度和蔼, có thái độ ôn hòa với tôi. Tác giả dùng liền ba từ 和蔼，和气，慈祥 để vẽ nên hình ảnh ba mẹ hiền hậu."]),
    ("他们和我身边所有父母一样，给我很多宠爱，我也和身边所有的孩子一样，在跨进大学校门之前，从没有离开过家，独立自主的能力就更甭提了。",
     "Cũng như mọi ông bố bà mẹ xung quanh tôi, ba mẹ dành cho tôi rất nhiều sự cưng chiều; còn tôi cũng giống như mọi đứa trẻ xung quanh, trước khi bước chân vào cổng trường đại học chưa từng rời xa nhà, còn khả năng độc lập tự chủ thì càng khỏi phải nói.",
     ["和身边所有的孩子一样 nghĩa là giống như mọi đứa trẻ xung quanh. Cấu trúc giống như… được dùng hai lần để tạo sự cân đối. 宠爱 là cưng chiều.",
      "在……之前 là trước khi…. 更甭提了 nghĩa là càng khỏi phải nói, ý là khả năng tự lập gần như bằng không."]),
    ("脱离父母，独立生活对我具有巨大的诱惑，让我无比向往。",
     "Rời xa ba mẹ, sống tự lập có sức hấp dẫn vô cùng lớn đối với tôi, khiến tôi hết sức khao khát.",
     ["对……具有……的诱惑 nghĩa là có sức hấp dẫn đối với…. Ở đây 诱惑 mang nghĩa tích cực, là sức hấp dẫn, chứ không phải sự cám dỗ xấu.",
      "无比 đứng trước động từ tâm lý: 无比向往, vô cùng khao khát."]),
    ("几年以后，我终于在别的城市上了大学。第一次离开家，心里的孤独感一下子跑了出来。",
     "Mấy năm sau, cuối cùng tôi cũng vào đại học ở một thành phố khác. Lần đầu tiên rời nhà, cảm giác cô đơn trong lòng bỗng chốc ùa ra.",
     ["上了大学 là vào đại học. 孤独感 là cảm giác cô đơn. Hậu tố 感 giống chữ cảm trong tiếng Việt: 幸福感 là cảm giác hạnh phúc.",
      "一下子跑了出来, nghĩa đen là bỗng chốc chạy vụt ra. Đây là cách nhân hóa: cảm giác cô đơn như đang trốn trong lòng, rồi bỗng ùa ra."]),
    ("记得刚开学的时候，宿舍里的同学一给家里打电话就哭鼻子，每到节假日，大家更是片刻不停地往家赶。有同学回趟家要坐一夜的火车，这也阻挡不了大家回家的步伐。",
     "Còn nhớ hồi mới nhập học, các bạn trong ký túc xá hễ gọi điện về nhà là khóc nhè; mỗi khi đến ngày lễ, ngày nghỉ, mọi người lại càng hối hả về nhà không ngơi phút nào. Có bạn về nhà một chuyến phải ngồi tàu suốt một đêm, nhưng điều đó cũng không cản được bước chân về nhà của mọi người.",
     ["一……就…… là hễ… là…. 每到……更是…… là mỗi khi đến… thì càng…. Đây là những mẫu câu ta sẽ mô phỏng trong bài tập bốn.",
      "片刻不停 là không dừng lại chút nào. 往家赶 là vội vã về nhà. 回趟家 là về nhà một chuyến, tức là 回一趟家. 阻挡不了 là không ngăn cản được."]),
    ("回家的快乐和被亲情包围的幸福感染了我，我也恨不得马上飞到父母跟前，与他们团圆。",
     "Niềm vui được về nhà và hạnh phúc được tình thân bao bọc đã lan sang tôi, tôi cũng chỉ mong sao bay ngay đến bên ba mẹ, đoàn tụ cùng ba mẹ.",
     ["Chủ ngữ của câu rất dài: 回家的快乐和被亲情包围的幸福, động từ là 感染, tân ngữ là 我. 感染 ở đây là cảm xúc lan sang người khác.",
      "恨不得马上飞到父母跟前: chỉ mong được bay ngay đến bên ba mẹ, một điều không thể làm thật. Đây là điểm ngữ pháp thứ nhất. 与他们团圆 là cách nói văn viết của 和他们团圆, đoàn tụ cùng ba mẹ."]),
    ("假期终于要到了，我给父母打电话，告诉他们我准备回家。母亲却说，近来他们比较忙，要没什么事，就甭回来了，在学校看看书，或找份兼职做做。",
     "Cuối cùng kỳ nghỉ cũng sắp đến, tôi gọi điện cho ba mẹ, báo rằng tôi chuẩn bị về nhà. Nhưng mẹ lại nói, dạo này ba mẹ khá bận, nếu không có việc gì thì đừng về, cứ ở trường đọc sách, hoặc tìm một việc làm thêm mà làm.",
     ["却 là lại, nhưng lại, biểu thị điều trái với mong đợi. 要没什么事 cũng giống 要是没什么事, nghĩa là nếu không có việc gì, cách nói khẩu ngữ.",
      "兼职 là việc làm thêm, bán thời gian. 份 là lượng từ cho công việc. Động từ lặp lại 看看书，做做 làm cho giọng nói nhẹ nhàng, thoải mái."]),
    ("母亲的话使我酝酿已久的恋家情绪刹那间就没有了，我无法理解父母的反常，心中暗暗埋怨父母不体谅我。",
     "Lời của mẹ khiến tâm trạng nhớ nhà mà tôi ấp ủ đã lâu tan biến ngay trong khoảnh khắc. Tôi không thể hiểu nổi sự khác thường của ba mẹ, trong lòng thầm trách ba mẹ không thông cảm cho mình.",
     ["使 là khiến, làm cho, văn viết. 酝酿已久 là ấp ủ đã lâu. 恋家情绪 là tâm trạng quyến luyến gia đình. 刹那间 là trong khoảnh khắc.",
      "暗暗 là thầm, ngấm ngầm. Ở đây nhân vật hiểu lầm ba mẹ, tạo nên nút thắt của câu chuyện."]),
    ("无精打采了几天之后，我不得不开始规划怎样熬过漫长的假期。假期的校园寂静得很，我在图书馆看书，给杂志社写稿件，发现在难得的寂静中工作是那么美好。",
     "Sau mấy ngày ủ rũ, tôi đành phải bắt đầu tính xem làm sao vượt qua kỳ nghỉ dài đằng đẵng. Trong kỳ nghỉ, sân trường vắng lặng vô cùng, tôi đọc sách trong thư viện, viết bài cho tòa soạn tạp chí, và nhận ra làm việc trong sự yên tĩnh hiếm có ấy thật tuyệt vời biết bao.",
     ["不得不 là đành phải, buộc phải. 熬过 là cố chịu cho qua, cho thấy kỳ nghỉ này với nhân vật rất khó khăn. Cụm 无精打采了几天 cho thấy thành ngữ này ở đây được dùng như động từ.",
      "寂静得很 nghĩa là vắng lặng vô cùng. 杂志社 là tòa soạn tạp chí. Chú ý tâm trạng thay đổi: từ buồn chán đến thấy công việc thật đẹp."]),
    ("大学三年级，我回了趟家。母亲第一眼看到我时，脸上满是心疼，但瞬间那情绪就被她掩饰起来，我心中飞快地闪过一丝疑惑：他们在隐瞒什么呢？",
     "Năm thứ ba đại học, tôi về nhà một chuyến. Khi mẹ vừa nhìn thấy tôi, trên mặt mẹ đầy vẻ xót xa, nhưng trong chớp mắt cảm xúc đó đã bị mẹ che giấu đi. Trong lòng tôi thoáng qua một tia nghi ngờ: ba mẹ đang giấu giếm điều gì vậy?",
     ["满是 là đầy, toàn là. 瞬间 là trong nháy mắt. 被她掩饰起来 là câu bị động với 被.",
      "一丝 là một chút, một tia, nhỏ như sợi tơ: 一丝疑惑, một tia nghi ngờ. Câu hỏi 他们在隐瞒什么呢 khơi gợi sự tò mò của người đọc."]),
    ("那晚，我躺下怎么也睡不着，半夜听到母亲还在跟父亲唠叨：“孩子比在家时瘦多了，肯定是吃苦了，可她的变化还是挺让咱们欣慰的。”",
     "Đêm đó, tôi nằm xuống mà thế nào cũng không ngủ được. Nửa đêm, tôi nghe thấy mẹ vẫn đang thủ thỉ mãi với ba: Con bé gầy đi nhiều so với hồi ở nhà, chắc chắn là chịu khổ rồi, nhưng sự thay đổi của nó vẫn khiến chúng ta thật mãn nguyện.",
     ["怎么也 cộng phủ định là thế nào cũng không: 怎么也睡不着, thế nào cũng không ngủ được. 唠叨 ở đây không mang nghĩa xấu, mà là mẹ cứ nói mãi vì lo cho con.",
      "比在家时瘦多了 là câu so sánh: gầy hơn nhiều so với lúc ở nhà. 肯定是……可…… là chắc chắn là…, nhưng…, cũng là mẫu câu trong bài tập bốn. 咱们 là chúng ta, gồm cả người nghe."]),
    ("接着是父亲的声音：“总有一天她会明白的，不吃苦，怎么长本事？社会不需要只会享福的人。”",
     "Tiếp đó là giọng của ba: Rồi sẽ có một ngày con hiểu ra thôi. Không chịu khổ thì làm sao mà có bản lĩnh? Xã hội không cần những người chỉ biết hưởng phúc.",
     ["总有一天 là rồi sẽ có một ngày. 不吃苦，怎么长本事 là câu hỏi tu từ, ý là phải chịu khổ thì mới có bản lĩnh.",
      "Trong cụm 长本事, chữ đầu đọc là zhǎng, thanh ba, nghĩa là tăng thêm. 享福 là hưởng phúc, sống sung sướng. Đây chính là lý do thật sự khiến ba mẹ không cho con về nhà."]),
    ("我悄悄走出卧室，看到灯光下父母不舍的目光、头上新增的白发和眼角越来越深的皱纹，顿时什么都明白了，不由得热泪盈眶。",
     "Tôi lặng lẽ bước ra khỏi phòng ngủ, nhìn thấy dưới ánh đèn ánh mắt lưu luyến của ba mẹ, những sợi tóc bạc mới thêm trên đầu và những nếp nhăn nơi khóe mắt ngày một sâu, tôi lập tức hiểu ra tất cả, bất giác nước mắt lưng tròng.",
     ["Ba cụm danh từ song song: 不舍的目光，新增的白发，越来越深的皱纹, cho thấy ba mẹ đã già đi và thương con biết bao. 不舍 là không nỡ xa.",
      "Câu kết dùng liền hai điểm ngữ pháp: 顿时什么都明白了，不由得热泪盈眶. Lập tức hiểu ra tất cả, bất giác nước mắt lưng tròng. Tình yêu của ba mẹ thật thầm lặng."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 父母之爱",
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 父母之爱, dài bảy trăm linh một chữ, được cải biên từ một bài báo trên Bắc Kinh Thanh niên báo.",
         F(0, "Thầy chia bài thành mười ba đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 100 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi, cap="")] + [F(1, n) for n in notes])

# ----- Tóm tắt (bài tập 5) -----
add("bullets", chapter="Tóm tắt nội dung", section="Bài khóa 课文", title="Bài tập 5: Tóm tắt bài khóa (1/2)", reveal=True, size=36,
    items=["(1) “我”的家庭是什么样的家庭？",
           "Đáp án: 父母感情和睦，很少吵架；他们对我态度和蔼，给我很多宠爱；我独立自主的能力很差。",
           "(2) 上大学后，“我”想家的感受是什么样的？",
           "Đáp án: 心里的孤独感一下子跑了出来；别的同学一给家里打电话就哭鼻子；我也恨不得马上飞到父母跟前。",
           "(3) 假期到来时，父母给“我”什么建议？“我”能理解吗？",
           "Đáp án: 要没什么事，就甭回来了，在学校看看书，或找份兼职；我无法理解，心中暗暗埋怨父母不体谅我。"],
    say=["Bây giờ chúng ta cùng tóm tắt bài khóa theo bài tập năm của sách. Sách đưa ra năm câu hỏi kèm gợi ý.",
         F(0, "Câu một: 我的家庭是什么样的家庭？ Gia đình của nhân vật tôi là một gia đình như thế nào? Gợi ý: tình cảm của ba mẹ, thái độ của ba mẹ với tôi, và khả năng tự lập của tôi."),
         F(1, "Đáp án: 父母感情和睦，很少吵架；他们对我态度和蔼，给我很多宠爱；我独立自主的能力很差。 Ba mẹ hòa thuận, ít cãi nhau, rất hiền với tôi và cưng chiều tôi, còn khả năng tự lập của tôi rất kém."),
         F(2, "Câu hai: 上大学后，我想家的感受是什么样的？ Sau khi vào đại học, cảm giác nhớ nhà của tôi ra sao?"),
         F(3, "Đáp án: 心里的孤独感一下子跑了出来；别的同学一给家里打电话就哭鼻子；我也恨不得马上飞到父母跟前。 Nỗi cô đơn bỗng chốc ùa ra, các bạn khác gọi điện về nhà là khóc, còn tôi chỉ mong bay ngay về bên ba mẹ."),
         F(4, "Câu ba: 假期到来时，父母给我什么建议？我能理解吗？ Khi kỳ nghỉ đến, ba mẹ khuyên tôi điều gì? Tôi có hiểu không?"),
         F(5, "Đáp án: 要没什么事，就甭回来了，在学校看看书，或找份兼职；我无法理解，心中暗暗埋怨父母不体谅我。 Ba mẹ bảo không có việc gì thì đừng về, ở trường đọc sách hoặc làm thêm; tôi không hiểu nổi, trong lòng thầm trách ba mẹ.")])

add("bullets", section="Bài khóa 课文", title="Bài tập 5: Tóm tắt bài khóa (2/2)", reveal=True, size=36,
    items=["(4) “我”的假期是怎么度过的？",
           "Đáp án: 我在图书馆看书，给杂志社写稿件，发现在难得的寂静中工作是那么美好。",
           "(5) “我”回家后，知道了什么真相？",
           "Đáp án: 父母不让我回家，不是不爱我，而是想让我吃苦、长本事，学会独立生活。",
           "## Mạch cảm xúc: 向往 → 孤独 → 埋怨 → 疑惑 → 明白、热泪盈眶"],
    say=[F(0, "Câu bốn: 我的假期是怎么度过的？ Kỳ nghỉ của tôi trôi qua như thế nào?"),
         F(1, "Đáp án: 我在图书馆看书，给杂志社写稿件，发现在难得的寂静中工作是那么美好。 Tôi đọc sách ở thư viện, viết bài cho tạp chí, và nhận ra làm việc trong yên tĩnh thật tuyệt."),
         F(2, "Câu năm: 我回家后，知道了什么真相？ Sau khi về nhà, tôi biết được sự thật gì? Ô trống này sách để cho các bạn tự trả lời."),
         F(3, "Đáp án gợi ý: 父母不让我回家，不是不爱我，而是想让我吃苦、长本事，学会独立生活。 Ba mẹ không cho tôi về, không phải vì không thương tôi, mà là muốn tôi chịu khổ, có bản lĩnh, học cách sống tự lập."),
         F(4, "Các bạn hãy để ý mạch cảm xúc của nhân vật: từ 向往, khao khát tự lập, đến 孤独, cô đơn, rồi 埋怨, trách móc, sang 疑惑, nghi ngờ, và cuối cùng là 明白, hiểu ra, 热泪盈眶, rưng rưng nước mắt.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 恨不得", section="Ngữ pháp 注释", title="1. 恨不得 hènbude – chỉ mong sao, nóng lòng muốn", size=38,
    items=["Động từ: biểu thị mong mỏi tha thiết được làm ngay một việc",
           "Thường dùng cho việc trên thực tế không làm được · hay đi với 马上 / 一下子",
           "工作忙的时候，她恨不得一个人干两个人的活儿。",
           "他累坏了，恨不得一下子倒在床上，睡上三天三夜。",
           "回家的快乐和被亲情包围的幸福感染了我，我也恨不得马上飞到父母跟前，与他们团圆。",
           "Chú ý: 恨 ở đây không mang nghĩa căm ghét"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là 恨不得.",
         F(0, "恨不得 là động từ, biểu thị sự mong mỏi tha thiết, nóng lòng muốn làm ngay một việc gì đó. Tiếng Việt dịch là chỉ mong sao, hận không thể."),
         F(1, "Từ này thường dùng cho những việc trên thực tế không làm được, mang tính phóng đại. Phía sau là một cụm động từ, hay đi với 马上 hoặc 一下子."),
         F(2, "Ví dụ một: 工作忙的时候，她恨不得一个人干两个人的活儿。 Lúc công việc bận rộn, cô ấy chỉ mong một mình làm được việc của hai người."),
         F(3, "Ví dụ hai: 他累坏了，恨不得一下子倒在床上，睡上三天三夜。 Anh ấy mệt rã rời, chỉ muốn lập tức ngã ra giường ngủ liền ba ngày ba đêm. Rõ ràng không ai ngủ được ba ngày ba đêm, đây là cách nói phóng đại."),
         F(4, "Ví dụ ba, lấy từ bài khóa: 我也恨不得马上飞到父母跟前，与他们团圆。 Tôi cũng chỉ mong bay ngay đến bên ba mẹ, đoàn tụ cùng ba mẹ. Người thì không thể bay, nên đây cũng là việc không làm được."),
         F(5, "Chú ý: dù có chữ hận, 恨不得 không mang nghĩa căm ghét chút nào, mà là mong muốn rất mạnh mẽ.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: hoàn thành câu với 恨不得", reveal=True, size=40,
    items=["(1) 听到这个消息，他难受得不得了，恨不得……",
           "Đáp án: ……恨不得大哭一场。",
           "(2) 他饿极了，恨不得……",
           "Đáp án: ……恨不得一口吃下一整个西瓜。",
           "(3) 我又看了看表，它好像根本就没往前走，我真恨不得把表……",
           "Đáp án: ……恨不得把表往前拨一个小时。"],
    say=[F(0, "Luyện tập. Câu một: 听到这个消息，他难受得不得了，恨不得…… Nghe tin này, anh ấy khó chịu vô cùng, chỉ muốn làm gì? Các bạn hãy tạm dừng và thử hoàn thành câu."),
         F(1, "Đáp án gợi ý: 恨不得大哭一场。 Chỉ muốn khóc một trận thật to."),
         F(2, "Câu hai: 他饿极了，恨不得…… Anh ấy đói lắm rồi, chỉ muốn làm gì?"),
         F(3, "Đáp án gợi ý: 恨不得一口吃下一整个西瓜。 Chỉ muốn ăn một miếng hết cả quả dưa hấu. Đây là cách nói phóng đại, đúng tinh thần của 恨不得."),
         F(4, "Câu ba: 我又看了看表，它好像根本就没往前走，我真恨不得把表…… Tôi lại nhìn đồng hồ, nó dường như chẳng chạy chút nào, tôi thật chỉ muốn làm gì với cái đồng hồ?"),
         F(5, "Đáp án gợi ý: 恨不得把表往前拨一个小时。 Chỉ muốn vặn kim đồng hồ lên trước một tiếng. Các bạn có thể có đáp án khác, miễn là thể hiện mong muốn rất mạnh mẽ.")])

add("bullets", chapter="Ngữ pháp: 顿时", section="Ngữ pháp 注释", title="2. 顿时 dùnshí – ngay lập tức, bỗng chốc", size=36,
    items=["Phó từ: hành động, sự việc xảy ra ngay trong tình huống đó hoặc liền sau một việc khác",
           "Thường dùng trong văn viết · chỉ dùng để kể việc đã xảy ra",
           "傍晚，我们在大山里迷路了……大家拿出手机看了看，居然都快没电了，两个女生顿时急得哭了起来。",
           "我悄悄走出卧室，看到灯光下父母不舍的目光……顿时什么都明白了。",
           "听了医生的话，顿时，他的心里又燃起了希望。",
           "Sai: 你顿时来我家。 → Đúng: 你马上来我家。"],
    say=["Điểm ngữ pháp thứ hai là phó từ 顿时.",
         F(0, "顿时 biểu thị một hành động, một sự việc xảy ra ngay trong một tình huống nào đó, hoặc xảy ra liền ngay sau một việc khác. Tiếng Việt dịch là ngay lập tức, bỗng chốc."),
         F(1, "顿时 thường dùng trong văn viết, và chỉ dùng để kể lại việc đã xảy ra."),
         F(2, "Ví dụ một: 傍晚，我们在大山里迷路了，能够和外面联系的手机成了唯一救命的工具。大家拿出手机看了看，居然都快没电了，两个女生顿时急得哭了起来。 Chiều tối, chúng tôi bị lạc trong núi, chiếc điện thoại là công cụ cứu mạng duy nhất. Mọi người lấy điện thoại ra xem, không ngờ đều sắp hết pin, hai bạn nữ lập tức cuống lên khóc òa."),
         F(3, "Ví dụ hai, lấy từ bài khóa: 看到灯光下父母不舍的目光，顿时什么都明白了。 Nhìn thấy ánh mắt lưu luyến của ba mẹ dưới ánh đèn, tôi lập tức hiểu ra tất cả."),
         F(4, "Ví dụ ba: 听了医生的话，顿时，他的心里又燃起了希望。 Nghe lời bác sĩ, ngay lập tức, trong lòng anh ấy lại nhen nhóm hy vọng. Các bạn thấy 顿时 có thể đứng đầu vế câu, tách ra bằng dấu phẩy."),
         F(5, "Chú ý: 顿时 không dùng cho mệnh lệnh hay việc trong tương lai. Không nói 你顿时来我家, mà phải nói 你马上来我家。 Anh đến nhà tôi ngay đi.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: dùng 顿时 viết lại câu", reveal=True, size=36,
    items=["(1) 听她这么一说，我立刻没了主意。",
           "Đáp án: 听她这么一说，我顿时没了主意。",
           "(2) 一场大雨过后，我们要经过的那条公路断路了，计划好的旅行不能成行，孩子立刻急哭了。",
           "Đáp án: ……计划好的旅行不能成行，孩子顿时急哭了。",
           "(3) 专题讲座就要开始了，深受大家喜爱的老教授走上了讲台，马上，会场变得鸦雀无声。",
           "Đáp án: ……老教授走上了讲台，会场顿时变得鸦雀无声。"],
    say=[F(0, "Luyện tập: dùng 顿时 viết lại câu. Câu một: 听她这么一说，我立刻没了主意。 Nghe cô ấy nói vậy, tôi lập tức không biết tính sao. Các bạn tạm dừng và thử viết lại nhé."),
         F(1, "Đáp án: thay 立刻 bằng 顿时: 听她这么一说，我顿时没了主意。"),
         F(2, "Câu hai: 一场大雨过后，我们要经过的那条公路断路了，计划好的旅行不能成行，孩子立刻急哭了。 Sau trận mưa lớn, con đường chúng tôi định đi bị đứt, chuyến du lịch đã lên kế hoạch không thể thực hiện, đứa trẻ lập tức khóc òa."),
         F(3, "Đáp án: 孩子顿时急哭了。"),
         F(4, "Câu ba: 专题讲座就要开始了，深受大家喜爱的老教授走上了讲台，马上，会场变得鸦雀无声。 Buổi tọa đàm chuyên đề sắp bắt đầu, vị giáo sư già được mọi người yêu mến bước lên bục giảng, ngay lập tức, hội trường im phăng phắc."),
         F(5, "Đáp án: 会场顿时变得鸦雀无声。 Thành ngữ 鸦雀无声 nghĩa đen là quạ và chim sẻ không kêu, tức là im phăng phắc.")])

add("bullets", chapter="Ngữ pháp: 不由得", section="Ngữ pháp 注释", title="3. 不由得 bùyóude – bất giác, không kìm được", size=36,
    items=["Phó từ: không kiềm chế được bản thân · thường có nguyên nhân khiến mình không kìm được",
           "Cấu trúc: 不由得 + cụm động từ / cụm chủ vị",
           "李朋带病上场参加比赛了，我不由得有些担心。",
           "书中描写的情景，让我不由得回想起和圆圆谈恋爱时的幸福和快乐。",
           "……顿时什么都明白了，不由得热泪盈眶。",
           "Cụm chủ vị: 他说得这么认真，不由得我不信。"],
    say=["Điểm ngữ pháp thứ ba là phó từ 不由得.",
         F(0, "不由得 biểu thị không kiềm chế được bản thân, không nhịn được. Trong câu thường có một nguyên nhân khiến mình không kìm được. Tiếng Việt dịch là bất giác, không kìm được, không khỏi."),
         F(1, "Cấu trúc thường gặp: 不由得 cộng cụm động từ, hoặc cộng cụm chủ vị."),
         F(2, "Ví dụ một: 李朋带病上场参加比赛了，我不由得有些担心。 Lý Bằng mang bệnh vẫn ra sân thi đấu, tôi không khỏi có chút lo lắng. Nguyên nhân là anh ấy đang bị bệnh."),
         F(3, "Ví dụ hai: 书中描写的情景，让我不由得回想起和圆圆谈恋爱时的幸福和快乐。 Cảnh tượng miêu tả trong sách khiến tôi bất giác nhớ lại niềm hạnh phúc hồi yêu Viên Viên."),
         F(4, "Ví dụ ba, câu kết của bài khóa: 顿时什么都明白了，不由得热泪盈眶。 Lập tức hiểu ra tất cả, bất giác nước mắt lưng tròng."),
         F(5, "Còn đây là ví dụ với cụm chủ vị: 他说得这么认真，不由得我不信。 Anh ấy nói nghiêm túc như vậy, khiến tôi không thể không tin.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: dùng 不由得 viết lại câu", reveal=True, size=38,
    items=["(1) 山路窄窄的，还不平，车开得飞快，我们坐在车上难免有些担心。",
           "Đáp án: ……我们坐在车上不由得有些担心。",
           "(2) 第一次上台，我的心里不免有些发慌。",
           "Đáp án: 第一次上台，我的心里不由得有些发慌。",
           "(3) 表演太精彩了，大家情不自禁地鼓起掌来。",
           "Đáp án: 表演太精彩了，大家不由得鼓起掌来。"],
    say=[F(0, "Luyện tập: dùng 不由得 viết lại câu. Câu một: 山路窄窄的，还不平，车开得飞快，我们坐在车上难免有些担心。 Đường núi hẹp lại gồ ghề, xe chạy rất nhanh, ngồi trên xe chúng tôi khó tránh khỏi lo lắng."),
         F(1, "Đáp án: thay 难免 bằng 不由得: 我们坐在车上不由得有些担心。"),
         F(2, "Câu hai: 第一次上台，我的心里不免有些发慌。 Lần đầu lên sân khấu, trong lòng tôi không khỏi có chút hoảng hốt."),
         F(3, "Đáp án: 我的心里不由得有些发慌。"),
         F(4, "Câu ba: 表演太精彩了，大家情不自禁地鼓起掌来。 Màn biểu diễn quá đặc sắc, mọi người không kìm được mà vỗ tay."),
         F(5, "Đáp án: 大家不由得鼓起掌来。 Qua bài này, các bạn thấy 不由得 có nghĩa gần với 难免，不免 và 情不自禁, đều là không tránh được, không kìm được.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 体谅 – 原谅", section="Phân biệt từ 词语辨析", title="Phân biệt 体谅 và 原谅",
    common="Giống nhau: đều là động từ, đều mang nghĩa cảm thông; nhưng thường không thay thế cho nhau.",
    cols=[{"head": "体谅",
           "lines": ["(1) Đặt mình vào vị trí người khác để hiểu và cảm thông; trước có thể thêm 很、非常",
                     "Đúng: 我的家离公司很远，孩子又小，老板很体谅我，允许我晚半个小时上班。",
                     "(2) Có thể lặp lại",
                     "Đúng: 他家确实有特殊情况，你就体谅体谅他吧。"]},
          {"head": "原谅",
           "lines": ["(1) Tha thứ sơ suất, lỗi lầm, không trách phạt; trước thường không thêm phó từ",
                     "Đúng: 昨天我没写完作业，是因为我病了，所以老师原谅了我。",
                     "(2) Thường không lặp lại",
                     "Sai: 你就原谅原谅他吧。"]}],
    say=["Tiếp theo là phần phân biệt từ: 体谅 và 原谅. Hai từ có chung chữ lượng, nên học sinh hay nhầm.",
         "Điểm giống nhau: cả hai đều là động từ, đều có nghĩa thông cảm, bỏ qua cho người khác. Nhưng thông thường không thể thay thế cho nhau.",
         F(0, "Điểm khác thứ nhất. 体谅 có nghĩa là đặt mình vào vị trí của người khác mà suy nghĩ, để hiểu và cảm thông cho họ. Phía trước có thể thêm phó từ như 很，非常."),
         F(0, "Ví dụ: 我的家离公司很远，孩子又小，老板很体谅我，允许我晚半个小时上班。 Nhà tôi cách công ty rất xa, con lại còn nhỏ, sếp rất thông cảm cho tôi, cho phép tôi đi làm muộn nửa tiếng. Ở đây không ai có lỗi cả, chỉ là hoàn cảnh khó khăn."),
         F(1, "Còn 原谅 nhấn mạnh việc bỏ qua sơ suất, lỗi lầm của người khác, không trách mắng hay trừng phạt. Tiếng Việt dịch là tha thứ. Phía trước thường không thêm phó từ."),
         F(1, "Ví dụ: 昨天我没写完作业，是因为我病了，所以老师原谅了我。 Hôm qua em không làm xong bài tập là vì em bị ốm, nên thầy đã tha thứ cho em. Ở đây có một lỗi là không làm bài tập."),
         F(0, "Điểm khác thứ hai. 体谅 có thể lặp lại thành 体谅体谅. Ví dụ: 他家确实有特殊情况，你就体谅体谅他吧。 Nhà anh ấy quả thật có hoàn cảnh đặc biệt, anh thông cảm cho anh ấy chút đi."),
         F(1, "Còn 原谅 thường không lặp lại như vậy."),
         "Mẹo nhớ: có lỗi lầm cần bỏ qua thì dùng 原谅, tha thứ; có hoàn cảnh khó khăn cần hiểu cho thì dùng 体谅, thông cảm."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: chọn 体谅 hay 原谅?", reveal=True, size=38,
    items=["(1) 妈妈，____我吧，我不是故意的，下次一定不这样了。",
           "Đáp án: 原谅 – xin tha thứ cho một lỗi lầm.",
           "(2) 他太不____我了，我又要工作又要做家务，他还批评我干得慢。",
           "Đáp án: 体谅 – có 太 phía trước, nói về hoàn cảnh vất vả.",
           "(3) 小丽是个善良的女孩，很能____别人。",
           "Đáp án: 体谅 – có 很能 phía trước, cảm thông với người khác.",
           "(4) 虽然这次我____了他，但他并没有就此改正自己的错误。",
           "Đáp án: 原谅 – bỏ qua lỗi lầm (错误)."],
    say=[F(0, "Bây giờ chúng ta làm thử bài tập của sách: chọn 体谅 hoặc 原谅 để điền vào chỗ trống. Câu một: 妈妈，……我吧，我不是故意的，下次一定不这样了。 Mẹ ơi, hãy thế nào con đi, con không cố ý đâu, lần sau nhất định không thế nữa. Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: 原谅. 妈妈，原谅我吧。 Con đã phạm lỗi và xin mẹ tha thứ."),
         F(2, "Câu hai: 他太不……我了，我又要工作又要做家务，他还批评我干得慢。 Anh ấy thật quá không thế nào với tôi, tôi vừa phải đi làm vừa phải làm việc nhà, anh ấy còn chê tôi làm chậm."),
         F(3, "Đáp án: 体谅. 他太不体谅我了。 Phía trước có phó từ 太, và câu nói về hoàn cảnh vất vả, không phải lỗi lầm."),
         F(4, "Câu ba: 小丽是个善良的女孩，很能……别人。 Tiểu Lệ là một cô gái lương thiện, rất biết thế nào với người khác."),
         F(5, "Đáp án: 体谅. 很能体谅别人, rất biết cảm thông cho người khác."),
         F(6, "Câu bốn: 虽然这次我……了他，但他并没有就此改正自己的错误。 Tuy lần này tôi đã thế nào anh ta, nhưng anh ta không vì thế mà sửa sai."),
         F(7, "Đáp án: 原谅. 虽然这次我原谅了他。 Câu nói rõ anh ta có 错误, tức là có lỗi, nên dùng 原谅, tha thứ.")])

# ======================= KỸ NĂNG VIẾT =======================
add("bullets", chapter="Kỹ năng viết: kể chuyện & mô phỏng", section="Kỹ năng viết 写作", title="Cách kể chuyện: thắt nút – mở nút", size=36,
    items=["## Bài khóa kể theo trình tự thời gian, có nút thắt và mở nút",
           "Mở đầu: gia đình yêu thương, nhân vật khao khát tự lập (向往)",
           "Thắt nút: mẹ bảo 甭回来了 → nhân vật hiểu lầm, trách ba mẹ (埋怨)",
           "Gợi tò mò: 脸上满是心疼……他们在隐瞒什么呢？ (疑惑)",
           "Mở nút: nghe lời ba mẹ nói nửa đêm → biết sự thật",
           "Kết: 顿时什么都明白了，不由得热泪盈眶。 – cảm xúc dâng trào",
           "Bí quyết: đừng nói thẳng ba mẹ rất yêu tôi – hãy để người đọc tự cảm nhận qua chi tiết"],
    say=["Bây giờ chúng ta sang kỹ năng viết. Trước tiên, hãy học cách kể chuyện của bài khóa.",
         F(0, "Bài khóa kể theo trình tự thời gian, nhưng có nút thắt và mở nút, nên rất cuốn hút."),
         F(1, "Mở đầu: nhân vật lớn lên trong một gia đình yêu thương, khao khát được tự lập."),
         F(2, "Thắt nút: kỳ nghỉ đến, mẹ lại bảo 甭回来了, đừng về. Nhân vật hiểu lầm, thầm trách ba mẹ."),
         F(3, "Gợi tò mò: năm thứ ba về nhà, thấy mẹ đầy vẻ xót xa nhưng lại che giấu, nhân vật tự hỏi 他们在隐瞒什么呢？ Người đọc cũng tò mò theo."),
         F(4, "Mở nút: nửa đêm nghe được cuộc trò chuyện của ba mẹ, nhân vật mới biết sự thật."),
         F(5, "Kết: 顿时什么都明白了，不由得热泪盈眶。 Cảm xúc dâng trào ở câu cuối cùng."),
         F(6, "Bí quyết: tác giả không hề nói thẳng ba mẹ rất yêu tôi, mà để người đọc tự cảm nhận qua những chi tiết như ánh mắt, tóc bạc, nếp nhăn. Khi làm bài viết ở phần vận dụng, các bạn hãy thử áp dụng cách này.")])

add("bullets", section="Kỹ năng viết 写作", title="Bài tập 4: Mô phỏng đoạn văn (1)", reveal=True, size=36,
    items=["Mẫu: 记得刚开学的时候，宿舍里的同学一给家里打电话就哭鼻子，每到节假日，大家更是片刻不停地往家赶……我也恨不得马上飞到父母跟前，与他们团圆。",
           "Khung: 记得____的时候，我一____就____，每到____，我更是____。那些下班后急忙忙赶回家的人们感染了我，我也恨不得____。",
           "Đáp án: 记得刚参加工作的时候，我一想起家人就特别难过，每到周末，我更是想家想得厉害。那些下班后急忙忙赶回家的人们感染了我，我也恨不得马上飞回家，和家人一起吃顿饭。"],
    say=[F(0, "Bài tập bốn của sách: đọc đoạn văn rồi mô phỏng đặt câu. Đoạn mẫu thứ nhất lấy từ bài khóa, có bốn điểm cần chú ý: 记得……的时候, còn nhớ hồi…; 一……就……, hễ… là…; 每到……更是……, mỗi khi đến… thì càng…; và 恨不得, chỉ mong sao."),
         F(1, "Khung câu cần hoàn thành: 记得……的时候，我一……就……，每到……，我更是……。那些下班后急忙忙赶回家的人们感染了我，我也恨不得……。 Các bạn hãy tạm dừng và thử viết."),
         F(2, "Đáp án gợi ý: 记得刚参加工作的时候，我一想起家人就特别难过，每到周末，我更是想家想得厉害。那些下班后急忙忙赶回家的人们感染了我，我也恨不得马上飞回家，和家人一起吃顿饭。 Còn nhớ hồi mới đi làm, hễ nghĩ đến gia đình là tôi buồn vô cùng, mỗi khi đến cuối tuần lại càng nhớ nhà da diết. Những người tan làm vội vã về nhà khiến tôi cũng chỉ mong bay ngay về nhà, ăn một bữa cơm cùng gia đình.")])

add("bullets", section="Kỹ năng viết 写作", title="Bài tập 4: Mô phỏng đoạn văn (2)", reveal=True, size=38,
    items=["Mẫu: 孩子比在家时瘦多了，肯定是吃苦了，可她的变化还是挺让咱们欣慰的。",
           "Cấu trúc: 肯定是 + suy đoán，可 + ý trái ngược",
           "Khung: 他现在开着豪华汽车，全身上下都是名牌，肯定是____，可____。",
           "Đáp án: ……肯定是赚了不少钱，可他对老朋友还是跟以前一样热情。"],
    say=[F(0, "Đoạn mẫu thứ hai là lời của mẹ: 孩子比在家时瘦多了，肯定是吃苦了，可她的变化还是挺让咱们欣慰的。"),
         F(1, "Cấu trúc ở đây là 肯定是 cộng một suy đoán, sau đó 可 cộng một ý trái ngược. Chắc chắn là…, nhưng mà…."),
         F(2, "Khung câu: 他现在开着豪华汽车，全身上下都是名牌，肯定是……，可……。 Bây giờ anh ta lái xe sang, từ đầu đến chân toàn đồ hàng hiệu, chắc chắn là…, nhưng…. Các bạn thử viết nhé."),
         F(3, "Đáp án gợi ý: 肯定是赚了不少钱，可他对老朋友还是跟以前一样热情。 Chắc chắn là kiếm được nhiều tiền, nhưng anh ấy vẫn nhiệt tình với bạn cũ như trước đây.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Viết thêm từ theo chữ được đánh dấu", size=38,
    items=["Mẫu: 和蔼 (和) → 和睦 · 和气 · 和平 · 心平气和",
           "脱离 (离) → 离开 · 离别 · 分离 · 距离 · 远离",
           "无比 (无) → 无聊 · 无法 · 无数 · 无限 · 无奈",
           "吃苦 (苦) → 辛苦 · 痛苦 · 艰苦 · 刻苦 · 苦恼",
           "顿时 (时) → 时间 · 时代 · 及时 · 准时 · 同时"],
    say=["Phần luyện tập. Bài tập một: mô phỏng ví dụ, viết thêm các từ có chứa chữ được đánh dấu chấm bên dưới.",
         F(0, "Ví dụ mẫu: 和蔼, chữ được đánh dấu là chữ đầu. Ta có 和睦，和气，和平，心平气和. Tức là hòa thuận, nhã nhặn, hòa bình, và bình tĩnh ôn hòa."),
         F(1, "脱离, chữ được đánh dấu là chữ thứ hai, ly. Ta có 离开，离别，分离，距离，远离. Tức là rời khỏi, ly biệt, chia lìa, khoảng cách, tránh xa."),
         F(2, "无比, chữ được đánh dấu là chữ đầu, vô. Ta có 无聊，无法，无数，无限，无奈. Tức là buồn chán, không thể, vô số, vô hạn, bất đắc dĩ."),
         F(3, "吃苦, chữ được đánh dấu là chữ thứ hai, khổ. Ta có 辛苦，痛苦，艰苦，刻苦，苦恼. Tức là vất vả, đau khổ, gian khổ, chăm chỉ khắc khổ, phiền não."),
         F(4, "顿时, chữ được đánh dấu là chữ thứ hai, thời. Ta có 时间，时代，及时，准时，同时. Tức là thời gian, thời đại, kịp thời, đúng giờ, đồng thời.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Hoàn thành câu với từ cho sẵn (1/2)", reveal=True, size=38,
    items=["(1) 我喜欢旅行，____。（向往）",
           "Đáp án: 我喜欢旅行，一直向往着到世界各地去看看。",
           "(2) 那家饭馆的环境很不好，顾客们____。（埋怨）",
           "Đáp án: ……顾客们经常埋怨那里又吵又乱。",
           "(3) 看到这么精彩的表演，大家____。（不由得）",
           "Đáp án: ……大家不由得鼓起掌来。"],
    say=[F(0, "Bài tập hai: dùng từ cho sẵn để hoàn thành câu. Câu một, dùng 向往: 我喜欢旅行，…… Tôi thích du lịch, …. Các bạn tạm dừng và thử hoàn thành nhé."),
         F(1, "Đáp án gợi ý: 我喜欢旅行，一直向往着到世界各地去看看。 Tôi thích du lịch, luôn khao khát được đi khắp thế giới."),
         F(2, "Câu hai, dùng 埋怨: 那家饭馆的环境很不好，顾客们…… Môi trường của quán ăn đó rất tệ, khách hàng…."),
         F(3, "Đáp án gợi ý: 顾客们经常埋怨那里又吵又乱。 Khách hàng thường phàn nàn ở đó vừa ồn vừa lộn xộn."),
         F(4, "Câu ba, dùng 不由得: 看到这么精彩的表演，大家…… Xem màn biểu diễn đặc sắc như vậy, mọi người…."),
         F(5, "Đáp án gợi ý: 大家不由得鼓起掌来。 Mọi người không kìm được mà vỗ tay.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Hoàn thành câu với từ cho sẵn (2/2)", reveal=True, size=38,
    items=["(4) 中秋节，全家团圆在一起，妈妈____。（无比）",
           "Đáp án: ……妈妈感到无比幸福。",
           "(5) 一天没吃饭，我饿坏了，____。（恨不得）",
           "Đáp án: ……恨不得马上吃下一大碗面条。",
           "(6) 他丢了工作，但怕妈妈担心，所以____。（隐瞒）",
           "Đáp án: ……所以一直向妈妈隐瞒了这件事。"],
    say=[F(0, "Câu bốn, dùng 无比: 中秋节，全家团圆在一起，妈妈…… Tết Trung thu, cả nhà đoàn tụ bên nhau, mẹ…."),
         F(1, "Đáp án gợi ý: 妈妈感到无比幸福。 Mẹ cảm thấy hạnh phúc vô cùng."),
         F(2, "Câu năm, dùng 恨不得: 一天没吃饭，我饿坏了，…… Cả ngày không ăn gì, tôi đói lả rồi, …."),
         F(3, "Đáp án gợi ý: 恨不得马上吃下一大碗面条。 Chỉ muốn ăn ngay một bát mì thật to."),
         F(4, "Câu sáu, dùng 隐瞒: 他丢了工作，但怕妈妈担心，所以…… Anh ấy bị mất việc, nhưng sợ mẹ lo, nên…."),
         F(5, "Đáp án gợi ý: 所以一直向妈妈隐瞒了这件事。 Nên vẫn luôn giấu mẹ chuyện này. Chú ý cấu trúc 向 cộng người cộng 隐瞒, giấu ai đó.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ điền vào chỗ trống (1)", reveal=True, size=36,
    items=["Từ cho sẵn: 无精打采 · 隐瞒 · 反常 · 热泪盈眶 · 不由得",
           "最近我的朋友小李有些__(1)__，每天都__(2)__的，他以前可是非常开朗的啊。我__(3)__担心起他来。于是我找了个机会跟他说：“如果你遇到了什么困难，千万别__(4)__，告诉我，我们一起想办法解决吧！”听了我的话，小李感动得__(5)__。",
           "Đáp án: (1) 反常 · (2) 无精打采 · (3) 不由得 · (4) 隐瞒 · (5) 热泪盈眶"],
    say=[F(0, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn thứ nhất có năm từ: 无精打采，隐瞒，反常，热泪盈眶，不由得."),
         F(1, "Đoạn văn kể về người bạn tên Tiểu Lý dạo này có gì đó khác thường, ngày nào cũng ủ rũ, trong khi trước đây rất vui vẻ. Tôi bắt đầu lo cho cậu ấy và khuyên cậu ấy đừng giấu chuyện gì. Các bạn hãy tạm dừng và điền thử năm chỗ trống."),
         F(2, "Đáp án: 最近我的朋友小李有些反常，每天都无精打采的，他以前可是非常开朗的啊。我不由得担心起他来。"),
         F(2, "于是我找了个机会跟他说：如果你遇到了什么困难，千万别隐瞒，告诉我，我们一起想办法解决吧！听了我的话，小李感动得热泪盈眶。 Nghe tôi nói vậy, Tiểu Lý cảm động đến rưng rưng nước mắt.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ điền vào chỗ trống (2)", reveal=True, size=36,
    items=["Từ cho sẵn: 酝酿 · 埋怨 · 近来 · 顿时 · 体谅",
           "__(1)__公司的事情比较多，我__(2)__已久的旅行也只能放弃了。心中暗暗__(3)__老板太不__(4)__员工了。但反过来一想，只有公司发展好了，我们才会有更好的未来。于是，那些不满的情绪__(5)__消失了。",
           "Đáp án: (1) 近来 · (2) 酝酿 · (3) 埋怨 · (4) 体谅 · (5) 顿时"],
    say=[F(0, "Đoạn thứ hai có năm từ: 酝酿，埋怨，近来，顿时，体谅."),
         F(1, "Đoạn văn kể: dạo này công ty nhiều việc, chuyến du lịch ấp ủ đã lâu đành phải hủy, tôi thầm trách sếp không thông cảm cho nhân viên. Nhưng nghĩ lại thì công ty phát triển tốt, tương lai của chúng tôi mới tốt hơn. Các bạn tạm dừng và thử điền nhé."),
         F(2, "Đáp án: 近来公司的事情比较多，我酝酿已久的旅行也只能放弃了。心中暗暗埋怨老板太不体谅员工了。"),
         F(2, "但反过来一想，只有公司发展好了，我们才会有更好的未来。于是，那些不满的情绪顿时消失了。 Thế là những cảm xúc bất mãn ấy lập tức tan biến. Các bạn để ý: đoạn này dùng lại rất nhiều cụm trong bài khóa, như 酝酿已久，心中暗暗埋怨，太不体谅.")])

# ======================= MỞ RỘNG =======================
add("bullets", chapter="Mở rộng: động từ chỉ động tác", section="Mở rộng 扩展", title="Từ vựng mở rộng: động từ chỉ động tác (1)", size=38,
    items=["掰 bāi – bẻ (bằng tay): 把面包掰开。",
           "鞠躬 jūgōng – cúi chào: 孩子给父母鞠躬。",
           "搀 chān – dìu, đỡ: 搀着老人过马路。",
           "扛 káng – vác (trên vai): 他扛着一个箱子。",
           "飞翔 fēixiáng – bay lượn: 天空中有一只飞翔的鸟儿。"],
    say=["Phần mở rộng: sách giới thiệu mười động từ chỉ động tác, kèm hình minh họa. Các từ này rất hay gặp trong văn miêu tả.",
         F(0, "Từ thứ nhất: 掰开, bẻ ra bằng tay. Ví dụ: 把面包掰开。 Bẻ đôi chiếc bánh mì."),
         F(1, "鞠躬, cúi chào. Ví dụ: 孩子给父母鞠躬。 Đứa con cúi chào ba mẹ."),
         F(2, "搀着, dìu, đỡ người khác đi. Ví dụ: 搀着老人过马路。 Dìu người già qua đường."),
         F(3, "Vác trên vai. Ví dụ: 他扛着一个箱子。 Anh ấy đang vác một chiếc thùng."),
         F(4, "飞翔, bay lượn. Ví dụ: 天空中有一只飞翔的鸟儿。 Trên bầu trời có một chú chim đang bay lượn.")])

add("bullets", section="Mở rộng 扩展", title="Từ vựng mở rộng: động từ chỉ động tác (2)", size=38,
    items=["啃 kěn – gặm, cắn: 孩子在啃苹果。",
           "搅拌 jiǎobàn – khuấy, đánh trộn: 把碗里的鸡蛋搅拌一下。",
           "挎 kuà – khoác, đeo (trên cánh tay, vai): 她胳膊上挎着很多包。",
           "敬礼 jìnglǐ – chào (giơ tay chào): 他们在给领导敬礼。",
           "晾 liàng – phơi: 外面晾着几件衣服。"],
    say=[F(0, "Gặm, cắn. Ví dụ: 孩子在啃苹果。 Đứa bé đang gặm quả táo."),
         F(1, "搅拌, khuấy, đánh trộn. Ví dụ: 把碗里的鸡蛋搅拌一下。 Đánh trứng trong bát lên một chút."),
         F(2, "Khoác, đeo trên cánh tay. Ví dụ: 她胳膊上挎着很多包。 Trên cánh tay cô ấy khoác rất nhiều túi."),
         F(3, "敬礼, giơ tay chào. Ví dụ: 他们在给领导敬礼。 Họ đang giơ tay chào lãnh đạo."),
         F(4, "Phơi. Ví dụ: 外面晾着几件衣服。 Bên ngoài đang phơi mấy bộ quần áo. Các bạn hãy thử làm động tác khi đọc từng từ, sẽ nhớ rất nhanh.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 2", size=36,
    items=["Từ vựng trọng tâm: 和蔼 · 慈祥 · 向往 · 酝酿 · 埋怨 · 体谅 · 无精打采 · 熬 · 心疼 · 隐瞒 · 欣慰",
           "Ngữ pháp: 恨不得 (chỉ mong sao) · 顿时 (ngay lập tức) · 不由得 (bất giác)",
           "Phân biệt: 体谅 (thông cảm hoàn cảnh) ≠ 原谅 (tha thứ lỗi lầm)",
           "Viết: kể chuyện có nút thắt – mở nút, để chi tiết nói thay cảm xúc",
           "## Bài tập về nhà",
           "Viết bài văn ≥ 300 chữ với đề 父母给我的爱: nêu rõ nguyên nhân, diễn biến, kết quả; dùng 恨不得 · 顿时 · 不由得"],
    say=["Chúng ta cùng tổng kết bài hai.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 和蔼，慈祥，向往，酝酿，埋怨，体谅，无精打采，熬，心疼，隐瞒，欣慰."),
         F(1, "Về ngữ pháp: 恨不得 nghĩa là chỉ mong sao, thường dùng cho việc không làm được. 顿时 nghĩa là ngay lập tức, chỉ dùng kể việc đã xảy ra. 不由得 nghĩa là bất giác, không kìm được."),
         F(2, "Về phân biệt từ: 体谅 là thông cảm cho hoàn cảnh của người khác, có thể thêm 很 và có thể lặp lại. 原谅 là tha thứ cho lỗi lầm."),
         F(3, "Về kỹ năng viết: hãy kể chuyện có nút thắt và mở nút, và để các chi tiết nói thay cảm xúc."),
         F(5, "Bài tập về nhà, theo phần vận dụng của sách: 以父母给我的爱为题，写一篇不少于三百字的文章。 Hãy viết một bài văn ít nhất ba trăm chữ với đề bài Tình yêu ba mẹ dành cho tôi. Nêu rõ nguyên nhân, diễn biến, kết quả của câu chuyện, và qua chuyện đó bạn đã cảm nhận được tình yêu của ba mẹ như thế nào. Hãy cố gắng dùng 恨不得，顿时，不由得 trong bài viết."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Hẹn gặp lại các bạn ở bài ba: 一盒月饼, Một hộp bánh Trung thu. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Thượng) – Bài 2: 父母之爱 (Tình yêu của ba mẹ)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thứ tự quan trọng: cụm dài trước)
    "tts_replace": {"刹那": "岔那", "埋怨": "蛮怨", "长本事": "涨本事", "白发": "白珐",
                    "规划": "规话", "熬": "敖", "为题": "围题",
                    "人干两个": "人赣两个", "我干得慢": "我赣得慢", "倒在床上": "导在床上",
                    "心脏": "心葬"},
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai02.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
