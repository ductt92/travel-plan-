#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Hạ) – Bài 28 «高山流水遇知音». Chạy để sinh bai28.json."""
import json
import os

TAG = "HSK 6 (Hạ) · Bài 28 · 高山流水遇知音"
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
    zh="高山流水遇知音", py="Gāoshān liúshuǐ yù zhīyīn", vi="Bài 28: Núi cao nước chảy gặp tri âm",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Hạ.",
         "Hôm nay chúng ta học bài hai mươi tám: 高山流水遇知音。 Nghĩa là: Núi cao nước chảy gặp tri âm.",
         "Đây là bài cuối cùng của Đơn vị bảy, chủ đề 经典阅读, tức là Đọc tác phẩm kinh điển. Bài khóa kể lại câu chuyện tri âm nổi tiếng giữa Bá Nha và Chung Tử Kỳ, một câu chuyện mà người Việt chúng ta cũng rất quen thuộc."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bối cảnh thời Xuân Thu và câu chuyện tri âm Bá Nha – Tử Kỳ",
           "Nắm vững 51 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: các cấu trúc với 个 và phó từ 向来",
           "Phân biệt hai từ 气势 và 气魄",
           "Tu từ: phép uyển khúc (婉曲) – nói tránh, nói giảm"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu bối cảnh thời Xuân Thu, và nắm được câu chuyện tri âm giữa Bá Nha và Chung Tử Kỳ."),
         F(1, "Thứ hai, nắm vững năm mươi mốt từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học hai điểm ngữ pháp: các cấu trúc có chữ 个, và phó từ 向来."),
         F(3, "Thứ tư, phân biệt hai danh từ rất dễ nhầm: 气势 và 气魄."),
         F(4, "Thứ năm, một biện pháp tu từ rất tế nhị: phép uyển khúc, tiếng Trung gọi là 婉曲, tức là cách nói tránh, nói giảm."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Câu hỏi khởi động: 瑶琴 và 知音", size=40,
    items=["瑶琴 yáoqín: dao cầm – loại đàn cổ, có thể tấu nên những âm thanh tuyệt diệu",
           "你理解的“知音”是什么意思？ – Bạn hiểu 知音 nghĩa là gì?",
           "知音: nghĩa đen là hiểu được tiếng đàn (知 biết + 音 âm thanh)",
           "Nghĩa bóng: người bạn thật sự hiểu mình, hiểu cả tâm hồn mình",
           "你有知音吗？ – Bạn có tri âm không?"],
    say=["Chúng ta bắt đầu bằng phần khởi động. Sách cho xem bức tranh một cây đàn và hỏi mấy câu sau.",
         F(0, "Vật trong tranh gọi là 瑶琴, Hán Việt là dao cầm, một loại đàn cổ có thể tấu nên những âm thanh tuyệt diệu."),
         F(1, "Tiếng Trung có một từ là 知音. Câu hỏi là: 你理解的知音是什么意思？ Bạn hiểu từ 知音 nghĩa là gì?"),
         F(2, "知音 Hán Việt là tri âm. 知 là biết, hiểu; 音 là âm thanh. Nghĩa đen là người hiểu được tiếng đàn của mình."),
         F(3, "Nghĩa bóng là người bạn thật sự hiểu mình, hiểu cả suy nghĩ và tâm hồn mình. Tiếng Việt cũng dùng từ tri âm, tri kỷ với nghĩa này."),
         F(4, "Câu cuối: 你有知音吗？ Bạn có tri âm không? Các bạn hãy tạm dừng video, thử trả lời bằng tiếng Trung, rồi mới xem tiếp nhé.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 动 và 辨", size=38,
    items=["## 动 (động): lay động, làm xúc động",
           "动听 êm tai · 动人 cảm động · 动火 nổi nóng · 动气 · 动怒 nổi giận · 动情 xúc động · 动容 động lòng",
           "动心 động lòng · 感动 cảm động · 打动 làm cảm động · 激动 kích động · 触动 chạm đến · 生动 sinh động",
           "## 辨 (biện): phân biệt, nhận ra",
           "辨识 nhận biết · 辨别 biện biệt · 辨认 nhận ra · 辨析 phân tích phân biệt · 辨明 làm rõ",
           "分辨 phân biện · 明辨是非 phân biệt rõ đúng sai"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo, rất có lợi cho người Việt nhờ âm Hán Việt.",
         F(0, "Nhóm thứ nhất có chữ 动, Hán Việt là động. Ở đây 动 mang nghĩa lay động, làm rung động lòng người."),
         F(1, "动听，动人，动火，动气，动怒，动情，动容。 Tức là: êm tai, cảm động, nổi nóng, tức giận, nổi giận, xúc động và động lòng. Từ 动听 có ngay ở câu đầu bài khóa: tiếng đàn của Bá Nha 优美动听."),
         F(2, "动心，感动，打动，激动，触动，生动。 Tức là: động lòng, cảm động, làm cảm động, kích động, chạm đến lòng người, và sinh động. Cuối bài khóa có câu: tình bạn của hai người 感动了后人."),
         F(3, "Nhóm thứ hai có chữ 辨, Hán Việt là biện, nghĩa là phân biệt, nhận ra."),
         F(4, "辨识，辨别，辨认，辨析，辨明。 Tức là: nhận biết, phân biệt, nhận ra, phân tích để phân biệt, và làm cho rõ. Bài khóa có câu: Bá Nha 请他辨识其中之意, mời Chung Tử Kỳ nhận ra ý tứ trong tiếng đàn."),
         F(5, "分辨，明辨是非。 Tức là: phân biệt, và phân biệt rõ đúng sai.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 雄 và 清", size=38,
    items=["## 雄 (hùng): mạnh mẽ, to lớn",
           "雄壮 hùng tráng · 雄伟 hùng vĩ · 雄厚 hùng hậu · 雄大 · 雄劲 mạnh mẽ · 雄浑 hùng hồn",
           "雄兵 hùng binh · 雄心 hùng tâm · 雄威 uy hùng · 雄姿 dáng hùng dũng · 雄关 cửa ải hiểm yếu",
           "## 清 (thanh): trong, sạch, mát",
           "清澈 trong vắt · 清新 thanh tân · 清爽 mát mẻ · 清淡 thanh đạm · 清风 gió mát · 清高 thanh cao",
           "清净 thanh tịnh · 清凉 mát lạnh · 清香 hương thơm dịu · 清秀 thanh tú · 清白 trong sạch · 清汤 canh trong"],
    say=[F(0, "Nhóm thứ ba có chữ 雄, Hán Việt là hùng, nghĩa là mạnh mẽ, to lớn, như trong từ hùng vĩ, hùng tráng."),
         F(1, "雄壮，雄伟，雄厚，雄大，雄劲，雄浑。 Tức là: hùng tráng, hùng vĩ, hùng hậu, to lớn, mạnh mẽ, và hùng hồn. Bài khóa dùng 雄壮 và 雄伟 để tả tiếng đàn như núi cao."),
         F(2, "雄兵，雄心，雄威，雄姿，雄关。 Tức là: đội quân hùng mạnh, hùng tâm, uy hùng, dáng vẻ hùng dũng, và cửa ải hiểm yếu."),
         F(3, "Nhóm cuối cùng có chữ 清, Hán Việt là thanh, nghĩa là trong, sạch, mát."),
         F(4, "清澈，清新，清爽，清淡，清风，清高。 Tức là: trong vắt, trong lành, mát mẻ, thanh đạm, gió mát, và thanh cao. Bài khóa có 江水清澈, nước sông trong vắt, và 琴声变得清新流畅."),
         F(5, "清净，清凉，清香，清秀，清白，清汤。 Tức là: thanh tịnh, mát lạnh, hương thơm dịu, thanh tú, trong sạch, và canh trong."),
         "Các bạn thấy không, chỉ cần nắm nghĩa của một chữ gốc, ta có thể đoán được nghĩa của cả một nhóm từ. Hãy áp dụng cách này khi học từ mới nhé."])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng)
V = [
    ("领会", "lǐnghuì", "lĩnh hội", "động từ", "lĩnh hội, hiểu được (ý sâu xa)", "我终于领会了老师的意思。", "Cuối cùng tôi đã hiểu được ý của thầy.",
     "Động từ, nghĩa là lĩnh hội, hiểu được ý nghĩa, ý đồ sâu xa. Trong bài: không ai thật sự 领会 được nội hàm trong tiếng đàn của Bá Nha."),
    ("内涵", "nèihán", "nội hàm", "danh từ", "nội hàm, ý nghĩa sâu xa bên trong", "这首诗的内涵很丰富。", "Ý nghĩa bên trong của bài thơ này rất phong phú.",
     "Danh từ, nghĩa là nội hàm, tức ý nghĩa, giá trị sâu xa bên trong. Ngoài ra, 有内涵 còn dùng để khen một người có chiều sâu, có học thức."),
    ("港湾", "gǎngwān", "cảng loan", "danh từ", "vịnh, bến cảng (nơi thuyền neo đậu)", "风浪很大，船停在了港湾里。", "Sóng gió rất lớn, thuyền neo lại trong vịnh.",
     "Danh từ, nghĩa là vịnh, bến cảng, nơi thuyền bè neo đậu tránh sóng gió. 港 là cảng, 湾 là vịnh."),
    ("晴朗", "qínglǎng", "tình lãng", "tính từ", "(trời) quang đãng, nắng ráo, không mây", "今天天气晴朗，我们去爬山吧。", "Hôm nay trời quang đãng, chúng ta đi leo núi đi.",
     "Tính từ, nghĩa là trời quang đãng, nắng ráo, không có mây. Từ này thường dùng để tả thời tiết."),
    ("清澈", "qīngchè", "thanh triệt", "tính từ", "trong veo, trong vắt", "这里的江水清澈见底。", "Nước sông ở đây trong vắt nhìn thấy cả đáy.",
     "Tính từ, nghĩa là trong veo, trong vắt, thường tả nước. 清澈见底 là trong đến mức nhìn thấy đáy. Từ này còn dùng để tả đôi mắt trong sáng."),
    ("出神", "chū shén", "xuất thần", "động từ", "say sưa, mê mải đến ngây người", "他听音乐听得出了神。", "Anh ấy nghe nhạc say sưa đến ngây người.",
     "Động từ ly hợp, nghĩa là tập trung, say mê đến mức ngây người ra, quên cả xung quanh. Cẩn thận: xuất thần trong tiếng Việt thường là đạt tới mức tuyệt diệu, còn 出神 là ngẩn người, mê mải."),
    ("弦", "xián", "huyền", "danh từ", "dây đàn", "他弹琴时，一根琴弦断了。", "Khi anh ấy đang đàn, một sợi dây đàn bị đứt.",
     "Danh từ, nghĩa là dây đàn. Đàn bầu của Việt Nam còn gọi là độc huyền cầm, tức đàn một dây, chính là chữ 弦 này. Lượng từ đi kèm là 根."),
    ("美妙", "měimiào", "mỹ diệu", "tính từ", "tuyệt diệu, êm ái, đẹp đẽ", "她的歌声非常美妙。", "Giọng hát của cô ấy vô cùng tuyệt diệu.",
     "Tính từ, nghĩa là tuyệt diệu, đẹp đẽ, êm ái, thường tả âm nhạc, giọng hát, hoặc khoảnh khắc đẹp."),
    ("砍伐", "kǎnfá", "khảm phạt", "động từ", "chặt, đốn (cây)", "我们不能随便砍伐树木。", "Chúng ta không được tùy tiện chặt phá cây cối.",
     "Động từ, nghĩa là chặt, đốn cây. Trong bài: bên cạnh người tiều phu có đống củi 刚刚砍伐来的, vừa mới đốn về."),
    ("平凡", "píngfán", "bình phàm", "tính từ", "bình thường, tầm thường", "他是一个平凡的人。", "Anh ấy là một người bình thường.",
     "Tính từ, nghĩa là bình thường, không có gì đặc biệt. Ngược lại, 不平凡 là phi thường, khác người. Trong bài, Bá Nha ngạc nhiên vì nơi núi rừng lại có một người 不平凡 như vậy."),
    ("乐谱", "yuèpǔ", "nhạc phổ", "danh từ", "bản nhạc, nhạc phổ", "她一边看乐谱，一边弹钢琴。", "Cô ấy vừa nhìn bản nhạc vừa đánh đàn piano.",
     "Danh từ, nghĩa là bản nhạc, nhạc phổ. Chú ý: chữ 乐 ở đây đọc là yuè, thanh bốn, như trong 音乐, không đọc là lè."),
    ("赞叹", "zàntàn", "tán thán", "động từ", "khen ngợi, tấm tắc thán phục", "看了他的表演，大家都赞叹不已。", "Xem anh ấy biểu diễn, mọi người đều tấm tắc khen mãi.",
     "Động từ, nghĩa là khen ngợi với lòng thán phục. 赞叹不已 là tấm tắc khen không ngớt."),
    ("创作", "chuàngzuò", "sáng tác", "động từ", "sáng tác", "这首歌是他自己创作的。", "Bài hát này do chính anh ấy sáng tác.",
     "Động từ, nghĩa là sáng tác tác phẩm văn học, nghệ thuật, âm Hán Việt giống hệt tiếng Việt. Nó cũng có thể làm danh từ: tác phẩm, sự sáng tác."),
    ("民间", "mínjiān", "dân gian", "danh từ", "dân gian, trong dân chúng", "这是一个流传很广的民间故事。", "Đây là một câu chuyện dân gian được lưu truyền rộng rãi.",
     "Danh từ, nghĩa là dân gian, trong dân chúng, đối lập với triều đình, nhà nước. Trong bài: 民间真有精通音乐之人, trong dân gian quả thật có người tinh thông âm nhạc."),
    ("精通", "jīngtōng", "tinh thông", "động từ", "tinh thông, thông thạo", "他精通三种语言。", "Anh ấy thông thạo ba thứ tiếng.",
     "Động từ, nghĩa là tinh thông, hiểu biết sâu và thành thạo một lĩnh vực nào đó."),
    ("难能可贵", "nánnéng-kěguì", "nan năng khả quý", "thành ngữ", "làm được việc khó, thật đáng quý", "他这么年轻就这么懂事，真是难能可贵。", "Còn trẻ như vậy mà đã hiểu chuyện thế, thật đáng quý.",
     "Thành ngữ. 难能 là việc khó làm được, 可贵 là đáng quý. Nghĩa là làm được điều khó làm, nên rất đáng quý trọng."),
    ("应邀", "yìngyāo", "ứng yêu", "động từ", "nhận lời mời", "他应邀参加了朋友的婚礼。", "Anh ấy nhận lời mời đến dự đám cưới của bạn.",
     "Động từ, nghĩa là nhận lời mời, đáp lại lời mời, sắc thái trang trọng. Chú ý: chữ 应 ở đây đọc là yìng, thanh bốn."),
    ("钦佩", "qīnpèi", "khâm bội", "động từ", "khâm phục, kính phục", "我非常钦佩他的勇气。", "Tôi vô cùng khâm phục lòng dũng cảm của anh ấy.",
     "Động từ, nghĩa là khâm phục, kính phục, mức độ trang trọng hơn 佩服."),
    ("演奏", "yǎnzòu", "diễn tấu", "động từ", "biểu diễn (nhạc cụ), diễn tấu", "他为大家演奏了一首名曲。", "Anh ấy biểu diễn cho mọi người một bản nhạc nổi tiếng.",
     "Động từ, nghĩa là biểu diễn bằng nhạc cụ, diễn tấu. Chú ý: hát thì dùng 演唱, còn chơi nhạc cụ thì dùng 演奏."),
    ("豪迈", "háomài", "hào mại", "tính từ", "hào hùng, hào sảng, khoáng đạt", "他的琴声雄壮豪迈。", "Tiếng đàn của anh ấy hùng tráng, hào hùng.",
     "Tính từ, nghĩa là hào hùng, khoáng đạt, đầy khí phách, thường tả giọng nói, khí thế, hoặc tiếng nhạc."),
    ("旋律", "xuánlǜ", "toàn luật", "danh từ", "giai điệu", "这首歌的旋律很好听。", "Giai điệu của bài hát này rất hay.",
     "Danh từ, nghĩa là giai điệu của một bản nhạc. Hán Việt là toàn luật, nhưng tiếng Việt chúng ta dịch là giai điệu."),
    ("雄伟", "xióngwěi", "hùng vĩ", "tính từ", "hùng vĩ, to lớn tráng lệ", "长城非常雄伟。", "Vạn Lý Trường Thành vô cùng hùng vĩ.",
     "Tính từ, nghĩa là hùng vĩ, to lớn và tráng lệ, thường tả núi non, công trình kiến trúc."),
    ("壮观", "zhuàngguān", "tráng quan", "tính từ", "hùng tráng, ngoạn mục", "海上日出的景色十分壮观。", "Cảnh mặt trời mọc trên biển vô cùng ngoạn mục.",
     "Tính từ, nghĩa là cảnh tượng hùng tráng, ngoạn mục, khiến người xem choáng ngợp."),
    ("气势", "qìshì", "khí thế", "danh từ", "khí thế, thế mạnh", "这幅画很有气势。", "Bức tranh này rất có khí thế.",
     "Danh từ, nghĩa là khí thế, thanh thế mạnh mẽ của người hoặc sự vật. Lát nữa ta sẽ so sánh kỹ với từ 气魄."),
    ("气魄", "qìpò", "khí phách", "danh từ", "khí phách, bản lĩnh, sự quyết đoán", "他办事很有气魄。", "Anh ấy làm việc rất có khí phách.",
     "Danh từ, nghĩa là khí phách, bản lĩnh, sự gan dạ và quyết đoán khi làm việc."),
    ("曲折", "qūzhé", "khúc chiết", "tính từ", "quanh co; phức tạp, nhiều thăng trầm", "这个故事的情节很曲折。", "Tình tiết câu chuyện này rất ly kỳ, nhiều khúc ngoặt.",
     "Tính từ, nghĩa là quanh co, khúc khuỷu; nghĩa bóng là phức tạp, nhiều thăng trầm. Chú ý: ở đây 曲 đọc là qū, thanh một; còn trong 曲子 hay 一曲, chữ 曲 đọc là qǔ, thanh ba, nghĩa là bản nhạc."),
    ("节奏", "jiézòu", "tiết tấu", "danh từ", "tiết tấu, nhịp điệu", "城市生活的节奏很快。", "Nhịp sống ở thành phố rất nhanh.",
     "Danh từ, nghĩa là tiết tấu trong âm nhạc, và cũng chỉ nhịp độ của cuộc sống, công việc."),
    ("短促", "duǎncù", "đoản xúc", "tính từ", "ngắn và gấp (thời gian, âm thanh)", "跑完步，他的呼吸很短促。", "Chạy xong, hơi thở của anh ấy rất ngắn và gấp.",
     "Tính từ, nghĩa là ngắn và gấp, dùng cho âm thanh, hơi thở, hoặc thời gian."),
    ("波涛", "bōtāo", "ba đào", "danh từ", "sóng lớn, sóng cả", "海上波涛汹涌。", "Trên biển sóng cả cuồn cuộn.",
     "Danh từ, nghĩa là sóng lớn. 波涛汹涌 là sóng cả cuồn cuộn, một cụm rất hay gặp. Tiếng Việt có từ ba đào, nghĩa là sóng gió."),
    ("溅", "jiàn", "tiễn", "động từ", "bắn tóe, văng (nước, bùn)", "汽车开过，溅了我一身水。", "Xe ô tô chạy qua, làm nước bắn đầy người tôi.",
     "Động từ, nghĩa là bắn tóe, văng ra, thường nói về nước hoặc bùn. Bài khóa có 浪花飞溅, bọt sóng tung tóe."),
    ("气概", "qìgài", "khí khái", "danh từ", "khí phách hiên ngang, khí khái", "他很有英雄气概。", "Anh ấy rất có khí phách anh hùng.",
     "Danh từ, nghĩa là khí phách hiên ngang, thái độ mạnh mẽ khi đối mặt với việc lớn. 英雄气概 là khí phách anh hùng."),
    ("含义", "hányì", "hàm nghĩa", "danh từ", "hàm ý, ý nghĩa", "这句话的含义很深。", "Hàm ý của câu nói này rất sâu sắc.",
     "Danh từ, nghĩa là hàm ý, ý nghĩa ẩn chứa trong lời nói, chữ viết hay âm nhạc."),
    ("荒凉", "huāngliáng", "hoang lương", "tính từ", "hoang vắng, hoang vu", "这是一片荒凉的土地。", "Đây là một vùng đất hoang vắng.",
     "Tính từ, nghĩa là hoang vắng, ít người qua lại, cảnh vật tiêu điều."),
    ("领悟", "lǐngwù", "lĩnh ngộ", "động từ", "ngộ ra, hiểu thấu", "他终于领悟了人生的道理。", "Cuối cùng anh ấy đã ngộ ra đạo lý cuộc đời.",
     "Động từ, nghĩa là ngộ ra, hiểu thấu đến tận cùng. So với 领会, từ 领悟 nhấn mạnh sự hiểu sâu hơn, có phần giác ngộ."),
    ("侃侃而谈", "kǎnkǎn ér tán", "khản khản nhi đàm", "thành ngữ", "trò chuyện thao thao, ung dung tự tin", "他在会上侃侃而谈。", "Anh ấy nói năng thao thao, đầy tự tin trong cuộc họp.",
     "Thành ngữ. 侃侃 là dáng nói năng ung dung, thẳng thắn. Nghĩa là trò chuyện thao thao, tự tin và hào hứng."),
    ("投机", "tóujī", "đầu cơ", "tính từ", "hợp ý, hợp chuyện, ăn ý", "我们俩越谈越投机。", "Hai chúng tôi càng nói chuyện càng hợp ý.",
     "Tính từ, nghĩa là hợp ý, hợp chuyện. Cẩn thận: Hán Việt là đầu cơ, nhưng trong bài này nó không phải là đầu cơ kiếm lời, mà là nói chuyện hợp nhau. Có câu 话不投机半句多, không hợp ý thì nửa câu cũng thấy thừa."),
    ("黎明", "límíng", "lê minh", "danh từ", "bình minh, rạng đông", "黎明时分，天边出现了一道光。", "Lúc rạng đông, chân trời hiện lên một vệt sáng.",
     "Danh từ, nghĩa là bình minh, lúc trời sắp sáng. Bài khóa có 黎明将至, trời sắp sáng."),
    ("告辞", "gàocí", "cáo từ", "động từ", "cáo từ, xin phép ra về", "时间不早了，我该告辞了。", "Muộn rồi, tôi xin phép cáo từ.",
     "Động từ, nghĩa là cáo từ, chào để ra về, sắc thái lịch sự, trang trọng."),
    ("黄昏", "huánghūn", "hoàng hôn", "danh từ", "hoàng hôn, chiều tối", "黄昏时，我们在海边散步。", "Lúc hoàng hôn, chúng tôi đi dạo bên bờ biển.",
     "Danh từ, nghĩa là hoàng hôn, lúc mặt trời lặn, âm Hán Việt giống hệt tiếng Việt."),
    ("降临", "jiànglín", "giáng lâm", "động từ", "đến, buông xuống (đêm tối, may rủi)", "夜幕降临了，街上亮起了灯。", "Màn đêm buông xuống, đường phố sáng đèn.",
     "Động từ, nghĩa là đến, buông xuống, sắc thái văn viết. Hay đi với 夜幕, màn đêm, hoặc 幸福, 灾难: hạnh phúc hay tai họa ập đến."),
    ("沮丧", "jǔsàng", "tự táng", "tính từ", "chán nản, ủ rũ, nản lòng", "考试没通过，他很沮丧。", "Thi không đỗ, anh ấy rất chán nản.",
     "Tính từ, nghĩa là chán nản, ủ rũ, mất tinh thần. Chú ý: chữ 丧 ở đây đọc là sàng, thanh bốn."),
    ("变故", "biàngù", "biến cố", "danh từ", "biến cố, tai biến bất ngờ", "他家发生了变故。", "Nhà anh ấy xảy ra biến cố.",
     "Danh từ, nghĩa là biến cố, việc bất ngờ không hay xảy ra, âm Hán Việt giống hệt tiếng Việt."),
    ("逝世", "shìshì", "thệ thế", "động từ", "qua đời, tạ thế (trang trọng)", "这位著名作家去年逝世了。", "Nhà văn nổi tiếng này đã qua đời năm ngoái.",
     "Động từ, nghĩa là qua đời, tạ thế. Đây là cách nói trang trọng, tôn kính, thường dùng cho người có danh tiếng."),
    ("坟墓", "fénmù", "phần mộ", "danh từ", "phần mộ, mồ mả", "他的坟墓修在江边。", "Mộ của ông được xây bên bờ sông.",
     "Danh từ, nghĩa là phần mộ, mồ mả."),
    ("不止", "bùzhǐ", "bất chỉ", "động từ", "không ngừng, không dứt", "听到这个消息，她哭泣不止。", "Nghe tin này, cô ấy khóc mãi không thôi.",
     "Động từ, nghĩa là không ngừng, không dứt, thường đứng sau động từ: 泪流不止, nước mắt tuôn không ngớt. Ngoài ra 不止 còn có nghĩa là hơn, vượt quá, ví dụ 不止一次, không chỉ một lần."),
    ("粉碎", "fěnsuì", "phấn toái", "tính từ", "vỡ vụn, tan tành", "杯子掉在地上，摔得粉碎。", "Cái cốc rơi xuống đất, vỡ tan tành.",
     "Tính từ, nghĩa là vỡ vụn như bột, tan tành. Nó còn là động từ, nghĩa là đập tan, ví dụ 粉碎敌人的阴谋, đập tan âm mưu của kẻ thù."),
    ("向来", "xiànglái", "hướng lai", "phó từ", "xưa nay vẫn, từ trước đến nay", "他向来很守时。", "Xưa nay anh ấy luôn đúng giờ.",
     "Phó từ, nghĩa là từ trước đến nay vẫn luôn như vậy. Đây là điểm ngữ pháp thứ hai, ta sẽ học kỹ ở phần sau."),
    ("凄凉", "qīliáng", "thê lương", "tính từ", "thê lương, buồn thảm, hiu quạnh", "这首曲子听起来很凄凉。", "Bản nhạc này nghe thật thê lương.",
     "Tính từ, nghĩa là thê lương, buồn thảm, hiu quạnh, tả cảnh vật hoặc tâm trạng."),
    ("深情厚谊", "shēnqíng hòuyì", "thâm tình hậu nghị", "thành ngữ", "tình cảm sâu nặng, tình nghĩa thắm thiết", "我永远不会忘记你们的深情厚谊。", "Tôi mãi mãi không quên tình cảm sâu nặng của các bạn.",
     "Thành ngữ. 深情 là tình sâu, 厚谊 là nghĩa dày. Nghĩa là tình cảm sâu nặng, tình nghĩa thắm thiết."),
    ("真挚", "zhēnzhì", "chân chí", "tính từ", "chân thành, chân thật", "他们之间有着真挚的友谊。", "Giữa họ có một tình bạn chân thành.",
     "Tính từ, nghĩa là chân thành, xuất phát từ tấm lòng, thường đi với 感情, 友谊, 爱情."),
    ("纯洁", "chúnjié", "thuần khiết", "tính từ", "trong sáng, thuần khiết", "孩子的心灵是纯洁的。", "Tâm hồn trẻ thơ thật trong sáng.",
     "Tính từ, nghĩa là trong sáng, thuần khiết, không vẩn đục, không vụ lợi."),
]

add("bullets", chapter="Từ mới (51 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 28 có 51 từ mới, chia thành 17 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc đặc biệt: 乐谱 (yuè), 应邀 (yìng), 曲折 (qū), 沮丧 (sàng)"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có năm mươi mốt từ, thầy chia thành mười bảy nhóm nhỏ, mỗi nhóm ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số từ có âm đọc đặc biệt, thầy sẽ nhắc khi gặp. Chúng ta bắt đầu nhé.")])

for g in range(0, len(V), 3):
    group = V[g:g + 3]
    words, say = [], []
    for i, (zh, py, hv, loai, vi, ex, exvi, expl) in enumerate(group):
        n = g + i + 1
        words.append({"zh": zh, "py": py, "hv": hv.upper(), "loai": f"{n}. {loai}", "vi": vi, "ex": ex, "exvi": exvi})
        say.append(F(i, f"Từ số {n}: {zh}。 {zh}。 Hán Việt là {hv}.", zr=120))
        say.append(F(i, f"{expl} Ví dụ: {ex}{'' if ex[-1] in '。…！？' else '，'} {exvi[0].upper() + exvi[1:]}{'' if exvi[-1] in '.!?' else '.'}", zr=130))
    add("vocab", section="Từ mới 生词", title=f"Từ mới ({g + 1}–{g + len(group)} / {len(V)})",
        words=words, say=say)

# ======================= BỐI CẢNH =======================
add("bullets", chapter="Bối cảnh: Bá Nha – Tử Kỳ", section="Bài khóa 课文", title="Bối cảnh: thời Xuân Thu và hai nhân vật", size=38,
    items=["春秋 Xuân Thu (770–476 TCN): nhà Chu suy yếu, các nước chư hầu tranh hùng",
           "俞伯牙 (Du) Bá Nha: bậc thầy đánh đàn, tương truyền làm quan ở nước Tấn 晋国",
           "钟子期 Chung Tử Kỳ: người tiều phu nơi núi rừng, nghe đàn mà hiểu lòng người đàn",
           "Ghi chép sớm: 《吕氏春秋》 Lã Thị Xuân Thu · 《列子》 Liệt Tử",
           "Thời Minh: 冯梦龙 Phùng Mộng Long viết truyện 《俞伯牙摔琴谢知音》 – bài khóa dựa theo bản này"],
    say=["Trước khi đọc bài khóa, thầy kể một chút về bối cảnh, để các bạn hiểu câu chuyện sâu hơn. Câu chuyện này người Việt chúng ta rất quen, nhưng biết thêm nguồn gốc sẽ thú vị hơn nhiều.",
         F(0, "Câu chuyện xảy ra vào thời 春秋, tức thời Xuân Thu, khoảng từ năm bảy trăm bảy mươi đến năm bốn trăm bảy mươi sáu trước Công nguyên. Lúc đó nhà Chu suy yếu, các nước chư hầu tranh giành quyền bá chủ."),
         F(1, "Nhân vật thứ nhất là 俞伯牙, Bá Nha. Ông là một bậc thầy đánh đàn nổi tiếng, tương truyền làm quan ở nước Tấn. Họ Du, tức chữ 俞, là do truyện kể đời sau thêm vào, nên người Việt quen gọi là Du Bá Nha, hoặc chỉ gọi là Bá Nha."),
         F(2, "Nhân vật thứ hai là 钟子期, Chung Tử Kỳ, một người tiều phu nơi núi rừng, nhưng lại có thể nghe tiếng đàn mà hiểu được tâm tư của người đàn."),
         F(3, "Câu chuyện đã được ghi lại từ rất sớm, trong các sách cổ như 吕氏春秋, Lã Thị Xuân Thu, và 列子, Liệt Tử."),
         F(4, "Đến thời nhà Minh, nhà văn 冯梦龙, Phùng Mộng Long, viết thành truyện 俞伯牙摔琴谢知音, nghĩa là Du Bá Nha đập đàn tạ tri âm. Bài khóa hôm nay kể lại theo bản này, nên có thêm nhiều chi tiết như đêm Trung thu, hẹn ước năm sau, và bản nhạc của Khổng Tử.")])

add("bullets", section="Bài khóa 课文", title="Thành ngữ và văn hóa từ câu chuyện", size=38,
    items=["高山流水 cao sơn lưu thủy: núi cao nước chảy – tiếng đàn tri âm, âm nhạc tuyệt diệu",
           "知音 tri âm: người hiểu tiếng đàn → người bạn hiểu mình nhất · 知音难觅 tri âm khó tìm",
           "伯牙绝弦 / 伯牙摔琴: mất tri âm, Bá Nha đập đàn, cả đời không đàn nữa",
           "瑶琴 dao cầm (古琴 cổ cầm): đàn bảy dây, nhạc cụ của văn nhân thời xưa",
           "中秋 Trung thu: rằm tháng tám âm lịch (chú thích trong sách)"],
    say=["Câu chuyện này để lại cho tiếng Trung, và cả tiếng Việt, nhiều thành ngữ quen thuộc.",
         F(0, "Thứ nhất, 高山流水, cao sơn lưu thủy, núi cao nước chảy. Đó là hình ảnh trong tiếng đàn của Bá Nha mà Chung Tử Kỳ nghe ra được. Ngày nay, cụm từ này chỉ tình tri âm, hoặc chỉ âm nhạc tuyệt diệu."),
         F(1, "Thứ hai, 知音, tri âm. Từ nghĩa người hiểu tiếng đàn, nó trở thành từ chỉ người bạn hiểu mình nhất. Người ta hay nói 知音难觅, tri âm khó tìm."),
         F(2, "Thứ ba, 伯牙绝弦, hay 伯牙摔琴. Sách Lã Thị Xuân Thu chép rằng: Chung Tử Kỳ mất, Bá Nha đập đàn, cắt dây, suốt đời không đàn nữa, vì cho rằng trên đời không còn ai đáng để mình đàn cho nghe."),
         F(3, "Thứ tư, cây đàn trong truyện là 瑶琴, dao cầm, một tên gọi đẹp của 古琴, cổ cầm, loại đàn bảy dây mà các bậc văn nhân thời xưa rất yêu quý."),
         F(4, "Cuối cùng, sách có chú thích: 中秋 là Tết Trung thu, ngày rằm tháng tám âm lịch. Hai lần gặp gỡ của Bá Nha và Tử Kỳ đều vào đêm Trung thu trăng sáng. Bây giờ, chúng ta cùng đọc bài khóa nhé.")])

# ======================= BÀI KHÓA =======================
P = [
    ("俞伯牙从小酷爱音乐，他的琴声优美动听，犹如高山流水一般。虽然大家都赞美他琴弹得好，却从没有人能真正领会他琴声的内涵，他多想找到自己的知音啊！",
     "Du Bá Nha từ nhỏ đã say mê âm nhạc, tiếng đàn của ông du dương êm tai, tựa như núi cao nước chảy. Tuy mọi người đều khen ông đàn hay, nhưng chưa từng có ai thật sự hiểu được ý nghĩa sâu xa trong tiếng đàn của ông. Ông khao khát biết bao được tìm thấy tri âm của mình!",
     ["酷爱 nghĩa là cực kỳ yêu thích, say mê. 犹如……一般 nghĩa là tựa như…, là cách nói văn viết của 好像……一样.",
      "多……啊 là câu cảm thán: 他多想找到自己的知音啊, ông khao khát biết bao. Ngay câu mở đầu, tác giả đã nêu nỗi niềm của nhân vật: đàn hay mà không ai hiểu."]),
    ("一个中秋之夜，他乘船来到江边，偶遇风浪，船停在了一个类似港湾的地方。晚上，风浪渐渐平息，天气晴朗，江水清澈，景色十分迷人。",
     "Vào một đêm Trung thu, ông đi thuyền đến bờ sông, tình cờ gặp sóng gió, thuyền phải dừng lại ở một nơi giống như vịnh nhỏ. Buổi tối, sóng gió dần lặng, trời quang đãng, nước sông trong vắt, cảnh sắc vô cùng quyến rũ.",
     ["乘船 là đi thuyền. 偶遇 là tình cờ gặp. 类似 nghĩa là tương tự, giống như: 类似港湾的地方, một nơi giống như bến cảng.",
      "平息 là lặng xuống, yên lại. Tác giả tả cảnh trời quang, nước trong, trăng sáng, chuẩn bị không khí cho cuộc gặp gỡ định mệnh."]),
    ("望着空中的明月，俞伯牙来了兴致，拿出琴弹了起来，一会儿他就沉醉在了音乐之中。忽然他看到一个人雕塑一样站在岸边，似乎听得出了神。",
     "Ngắm vầng trăng sáng trên trời, Du Bá Nha nổi hứng, lấy đàn ra gảy, chẳng mấy chốc ông đã đắm chìm trong âm nhạc. Bỗng ông thấy một người đứng trên bờ như một pho tượng, dường như đang nghe say sưa đến ngây người.",
     ["来了兴致 nghĩa là nổi hứng. 弹了起来 là bắt đầu đàn; 起来 chỉ động tác bắt đầu. 沉醉在……之中 là say sưa, đắm chìm trong….",
      "雕塑一样 là giống như một pho tượng, phép so sánh cho thấy người nghe đứng im phăng phắc. 听得出了神 là nghe say đến ngây người, dùng từ 出神 vừa học."]),
    ("俞伯牙一个不留神，“啪”的一声，琴弦拨断了一根。这时，听琴的人大声说：“先生不必在意，我是个打柴的，回家晚了，走到这里听到您在弹琴，觉得琴声美妙，不由得站在这里听了起来。”",
     "Du Bá Nha chỉ sơ ý một chút, phựt một tiếng, một sợi dây đàn bị gảy đứt. Lúc đó, người nghe đàn nói to: Thưa tiên sinh, xin ngài đừng bận tâm, tôi là người đốn củi, về nhà muộn, đi đến đây nghe thấy ngài đang đánh đàn, thấy tiếng đàn tuyệt diệu, bất giác đứng lại đây nghe.",
     ["一个不留神 nghĩa là chỉ một chút sơ ý, đây chính là cấu trúc 一个 cộng cụm động từ mà ta học ở phần ngữ pháp. 啪 là từ tượng thanh, như tiếng phựt, tiếng tách.",
      "打柴的 là người đốn củi, tiều phu; cấu trúc động từ cộng 的 chỉ người làm nghề đó. 不必在意 là không cần để tâm. 不由得 nghĩa là bất giác, không kìm được."]),
    ("俞伯牙借着月光仔细打量，见那人身旁放着刚刚砍伐来的木柴，果然是个打柴的。俞伯牙心想：一个打柴的怎么能听懂我的琴呢？偏僻的山野还有这么不平凡的人？",
     "Du Bá Nha nhờ ánh trăng nhìn kỹ, thấy bên cạnh người ấy có đống củi vừa mới đốn về, quả nhiên là người đốn củi. Du Bá Nha nghĩ thầm: Một người đốn củi làm sao có thể hiểu được tiếng đàn của ta? Nơi núi rừng hẻo lánh mà lại có người phi thường như vậy sao?",
     ["借着月光 là nhờ vào ánh trăng. 打量 là quan sát, nhìn kỹ từ trên xuống dưới. 果然 là quả nhiên. 偏僻 là hẻo lánh.",
      "Hai câu hỏi 怎么能……呢 và 还有……？ thể hiện sự ngạc nhiên, nghi ngờ của Bá Nha: một người tiều phu nơi rừng núi mà lại hiểu đàn sao?"]),
    ("于是他问：“你既然懂琴，那就请说说，我弹的是什么曲子？”打柴人说：“先生刚才弹的乐谱是孔子为赞叹他的弟子而创作的，只可惜，您弹到第四句的时候琴弦断了。”",
     "Thế là ông hỏi: Anh đã hiểu đàn, vậy xin hãy nói xem, ta vừa đàn khúc gì? Người đốn củi đáp: Bản nhạc tiên sinh vừa đàn là do Khổng Tử sáng tác để ca ngợi người học trò của mình, chỉ tiếc là ngài đàn đến câu thứ tư thì dây đàn bị đứt.",
     ["既然……那就…… nghĩa là đã… thì…. 为……而…… nghĩa là vì… mà…: 为赞叹他的弟子而创作, sáng tác để ca ngợi học trò của mình.",
      "只可惜 là chỉ tiếc là. Chung Tử Kỳ không chỉ biết bản nhạc, mà còn biết chính xác dây đứt ở câu thứ tư. Theo truyện thời Minh, đó là khúc Khổng Tử than tiếc người học trò yêu là Nhan Hồi."]),
    ("俞伯牙不禁感叹，民间真有精通音乐之人，难能可贵！他迫不及待地想和打柴人好好聊聊。",
     "Du Bá Nha không khỏi cảm thán: trong dân gian quả thật có người tinh thông âm nhạc, thật hiếm có và đáng quý! Ông nóng lòng muốn trò chuyện thật kỹ với người đốn củi.",
     ["不禁 nghĩa là không nén được, bất giác. 之人 là người, cách nói văn viết: 精通音乐之人, người tinh thông âm nhạc.",
      "迫不及待 là thành ngữ, nghĩa là nóng lòng, không thể chờ thêm được nữa. 好好聊聊 là trò chuyện cho thỏa."]),
    ("打柴人应邀上了船，看到俞伯牙的琴，赞道：“真是好琴。”接着又说起瑶琴的来历，俞伯牙不禁心生钦佩。",
     "Người đốn củi nhận lời mời lên thuyền, nhìn thấy cây đàn của Du Bá Nha, khen rằng: Quả là đàn tốt. Rồi lại kể về lai lịch của cây dao cầm, khiến Du Bá Nha không khỏi kính phục trong lòng.",
     ["应邀 là nhận lời mời. 赞道 là khen rằng; 道 ở đây nghĩa là nói. 来历 là lai lịch, nguồn gốc.",
      "心生钦佩 là trong lòng nảy sinh sự kính phục. Các bạn để ý thái độ của Bá Nha thay đổi: từ nghi ngờ chuyển sang kính phục."]),
    ("接着俞伯牙又为打柴人演奏了几曲，请他辨识其中之意。当他的琴声雄壮豪迈的时候，打柴人说：“这旋律表达了高山的雄伟壮观。有气势，有气魄！”",
     "Tiếp đó, Du Bá Nha lại đàn mấy khúc cho người đốn củi nghe, mời anh nhận ra ý tứ trong đó. Khi tiếng đàn hùng tráng hào hùng, người đốn củi nói: Giai điệu này diễn tả sự hùng vĩ, tráng lệ của núi cao. Thật có khí thế, có khí phách!",
     ["辨识其中之意 là nhận ra ý tứ trong đó; 其 là trong đó, 之 là của, đều là cách nói văn ngôn. 几曲 là mấy khúc nhạc, chữ 曲 đọc là qǔ.",
      "Hàng loạt tính từ hùng tráng: 雄壮，豪迈，雄伟，壮观. Còn 有气势，有气魄 là có khí thế, có khí phách; ta sẽ phân biệt hai từ này ở phần sau."]),
    ("当琴声曲折激越、节奏短促时，打柴人说：“这旋律表达的是波涛汹涌，浪花飞溅，气概非凡！”当琴声变得清新流畅时，打柴人说：“这旋律表达的是无尽的流水。”",
     "Khi tiếng đàn trầm bổng dồn dập, tiết tấu ngắn gấp, người đốn củi nói: Giai điệu này diễn tả sóng cả cuồn cuộn, bọt sóng tung tóe, khí phách phi thường! Khi tiếng đàn trở nên trong trẻo, trôi chảy, người đốn củi nói: Giai điệu này diễn tả dòng nước chảy mãi không ngừng.",
     ["曲折激越 là trầm bổng dồn dập, 节奏短促 là tiết tấu ngắn gấp. 波涛汹涌 là sóng cả cuồn cuộn, 浪花飞溅 là bọt sóng tung tóe. 气概非凡 là khí phách phi thường.",
      "Ba lần đàn, ba lần Chung Tử Kỳ đều nghe ra: núi cao, sóng cả, và dòng nước chảy mãi. Đó chính là ý nghĩa của bốn chữ 高山流水."]),
    ("俞伯牙惊喜万分，过去没人能听懂他琴声的含义，没想到在这荒凉之地，竟觅到自己久寻不遇的知音，不仅能领会其意，还能领悟其神。",
     "Du Bá Nha vô cùng mừng rỡ. Trước đây không ai hiểu được hàm ý trong tiếng đàn của ông, không ngờ ở nơi hoang vắng này, ông lại tìm được người tri âm mà mình tìm mãi không gặp, người ấy không chỉ hiểu được ý, mà còn thấu được cái thần của tiếng đàn.",
     ["惊喜万分 là vô cùng mừng rỡ. 竟 là vậy mà, không ngờ. 觅 là tìm, văn viết. 久寻不遇 là tìm mãi không gặp.",
      "不仅能领会其意，还能领悟其神: không chỉ hiểu được ý, mà còn thấu được cái thần. Hãy chú ý cặp từ 领会 và 领悟; từ thứ hai mức độ sâu hơn."]),
    ("打柴人叫钟子期，两人在月下侃侃而谈，越谈越投机。黎明将至，钟子期告辞，并与俞伯牙约定，来年中秋还在这里相见。",
     "Người đốn củi tên là Chung Tử Kỳ. Hai người trò chuyện thao thao dưới trăng, càng nói càng hợp ý. Trời sắp sáng, Chung Tử Kỳ cáo từ, và hẹn với Du Bá Nha rằng Trung thu năm sau sẽ lại gặp nhau ở đây.",
     ["侃侃而谈 là trò chuyện thao thao. 越谈越投机 là càng nói càng hợp ý; đây là cấu trúc 越 A 越 B, càng A càng B.",
      "黎明将至 là trời sắp sáng; 将 là sắp, 至 là đến. 来年 là năm sau. 约定 là hẹn ước. Lời hẹn này mở ra phần sau của câu chuyện."]),
    ("第二年中秋这天，俞伯牙如约来到了老地方，从黄昏等到夜幕降临，一直不见钟子期到来，他有些沮丧，开始用琴声呼唤钟子期，可还是见不到钟子期的影子。该不是有了什么变故吧？俞伯牙焦急万分。",
     "Trung thu năm sau, Du Bá Nha đến chỗ cũ đúng hẹn, đợi từ lúc hoàng hôn đến khi màn đêm buông xuống, mãi không thấy Chung Tử Kỳ đến. Ông hơi chán nản, bắt đầu dùng tiếng đàn để gọi Chung Tử Kỳ, nhưng vẫn không thấy bóng dáng anh đâu. Chẳng lẽ đã xảy ra biến cố gì? Du Bá Nha vô cùng sốt ruột.",
     ["如约 là đúng hẹn. 老地方 là chỗ cũ. 从黄昏等到夜幕降临 là đợi từ hoàng hôn đến khi màn đêm buông xuống. 影子 ở đây là bóng dáng.",
      "该不是……吧 là chẳng lẽ là…, biểu thị sự phỏng đoán đầy lo lắng. 焦急万分 là vô cùng sốt ruột."]),
    ("第二天，俞伯牙向一位老人打听他的好友，老人告诉他，钟子期染病，逝世已有段时间了。临走前，他留下遗言，把坟墓修在江边，到八月十五，好听俞伯牙弹琴。",
     "Ngày hôm sau, Du Bá Nha hỏi thăm một ông lão về người bạn của mình. Ông lão nói với ông rằng Chung Tử Kỳ bị bệnh, đã qua đời được một thời gian rồi. Trước lúc ra đi, anh để lại di ngôn, xin xây mộ bên bờ sông, để đến ngày rằm tháng tám có thể nghe Du Bá Nha đánh đàn.",
     ["打听 là hỏi thăm. 染病 là nhiễm bệnh. 逝世 là qua đời, cách nói trang trọng. 遗言 là di ngôn, lời trăng trối.",
      "临走前 ở đây không phải là trước khi đi đâu, mà là trước khi qua đời. Đây là phép uyển khúc, ta học ở phần tu từ. Còn 好 trong 好听俞伯牙弹琴 nghĩa là để, để có thể."]),
    ("老人的话使俞伯牙泪流不止，他来到钟子期坟前，弹了一曲《高山流水》，曲终，他把心爱的琴摔了个粉碎，悲伤地说：“琴向来是要弹给知音听的，如今我唯一的知音已不在人世，这琴还弹给谁听呢？”",
     "Lời ông lão khiến Du Bá Nha nước mắt tuôn không ngớt. Ông đến trước mộ Chung Tử Kỳ, đàn một khúc Cao sơn lưu thủy. Khúc nhạc vừa dứt, ông đập cây đàn yêu quý tan tành, đau buồn nói: Đàn xưa nay là để đàn cho tri âm nghe, nay người tri âm duy nhất của ta đã không còn trên đời, cây đàn này còn đàn cho ai nghe nữa?",
     ["泪流不止 là nước mắt tuôn không ngớt. 曲终 là khúc nhạc kết thúc. 摔了个粉碎 là cấu trúc động từ cộng 个 cộng bổ ngữ, giống 摔得粉碎.",
      "向来 là xưa nay vẫn. Câu hỏi tu từ 这琴还弹给谁听呢: đàn này còn đàn cho ai nghe nữa, tức là không còn ai để đàn cho nghe nữa."]),
    ("故事有些凄凉，但两位知音的深情厚谊感动了后人，至今人们还用“知音”来形容朋友之间真挚而纯洁的情谊。",
     "Câu chuyện có phần thê lương, nhưng tình cảm sâu nặng giữa hai người tri âm đã làm cảm động người đời sau. Cho đến nay, người ta vẫn dùng từ tri âm để chỉ tình bạn chân thành và trong sáng giữa bạn bè.",
     ["后人 là người đời sau. 至今 là cho đến nay. 用……来形容…… là dùng… để miêu tả, để chỉ….",
      "Câu kết nêu ý nghĩa của cả câu chuyện. Trong tiếng Việt, chúng ta cũng dùng chữ tri âm, tri kỷ với nghĩa y hệt."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 高山流水遇知音",
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 高山流水遇知音, dài một nghìn không trăm bảy mươi hai chữ.",
         F(0, "Thầy chia bài thành từng đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, (zh, vi, notes) in enumerate(P, 1):
    zsize = 54 if len(zh) <= 100 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, zh, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi, cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Tóm tắt nội dung", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5)", size=36,
    items=["## 1. Hai người gặp nhau thế nào?",
           "俞: 酷爱音乐、无人领会、江边弹奏 · 钟: 打柴人、听得出了神、精通音乐",
           "## 2. Hai người nói chuyện gì?",
           "雄壮豪迈 → 高山雄伟壮观 · 曲折激越 → 波涛汹涌 · 清新流畅 → 无尽的流水",
           "## 3. Lời hẹn có thực hiện được không?",
           "来年中秋再见 → 第二年，俞等钟，钟未到 → 听说钟逝世、遗言 → 俞摔琴",
           "## 4. Ý nghĩa của tri âm: 朋友之间真挚而纯洁的情谊"],
    say=["Chúng ta cùng nhìn lại bố cục của cả bài khóa, theo gợi ý của bài tập năm trong sách.",
         F(0, "Thứ nhất, Bá Nha và Tử Kỳ gặp nhau như thế nào?"),
         F(1, "Về Bá Nha: 酷爱音乐，无人领会，江边弹奏, tức là say mê âm nhạc, không ai hiểu, đàn bên bờ sông. Về Tử Kỳ: 打柴人，听得出了神，精通音乐, tức là người đốn củi, nghe say đến ngây người, tinh thông âm nhạc."),
         F(2, "Thứ hai, hai người nói chuyện gì?"),
         F(3, "Tiếng đàn 雄壮豪迈, hùng tráng hào hùng, là núi cao hùng vĩ. Tiếng đàn 曲折激越, trầm bổng dồn dập, là sóng cả cuồn cuộn. Tiếng đàn 清新流畅, trong trẻo trôi chảy, là dòng nước chảy mãi."),
         F(4, "Thứ ba, lời hẹn của hai người có thực hiện được không?"),
         F(5, "Hai người hẹn Trung thu năm sau gặp lại. Năm sau, Bá Nha đợi mà Tử Kỳ không đến. Ông nghe tin Tử Kỳ đã mất, và nghe về di ngôn của bạn. Cuối cùng, Bá Nha đập đàn."),
         F(6, "Thứ tư, ý nghĩa của tri âm: tình bạn chân thành và trong sáng giữa bạn bè. Bố cục này rất có ích khi các bạn làm bài tập kể lại nội dung bài khóa.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: cấu trúc với 个", section="Ngữ pháp 注释", title="1. Cấu trúc với 个 (a): 一个 + danh từ / động từ", size=38,
    items=["一个 + danh từ / cụm động từ, đặt trước động từ vị ngữ",
           "Biểu thị: động tác, sự việc xảy ra rất nhanh, đột ngột",
           "他手没抓住栏杆，一个跟头栽了下来。",
           "我一个不小心，打碎了妈妈最心爱的花瓶。",
           "俞伯牙一个不留神，“啪”的一声，琴弦拨断了一根。",
           "Hay gặp: 一个不小心 · 一个不留神 · 一个失手 · 一个跟头 · 一个箭步"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là các cấu trúc có liên quan đến chữ 个. Có hai cấu trúc, chúng ta học từng cái một.",
         F(0, "Cấu trúc thứ nhất: 一个 cộng danh từ, hoặc cộng cụm động từ, đặt trước động từ vị ngữ."),
         F(1, "Cấu trúc này biểu thị động tác hay sự việc xảy ra rất nhanh, rất đột ngột. Tiếng Việt có thể dịch là: chỉ một cái…, chỉ sơ ý một chút là…."),
         F(2, "Ví dụ một: 他手没抓住栏杆，一个跟头栽了下来。 Tay anh ấy không nắm được lan can, lộn một cái ngã nhào xuống."),
         F(3, "Ví dụ hai: 我一个不小心，打碎了妈妈最心爱的花瓶。 Tôi chỉ bất cẩn một chút, đã làm vỡ chiếc bình hoa mẹ yêu quý nhất."),
         F(4, "Ví dụ ba, lấy từ bài khóa: 俞伯牙一个不留神，啪的一声，琴弦拨断了一根。 Du Bá Nha chỉ sơ ý một chút, phựt một tiếng, một sợi dây đàn đã đứt."),
         F(5, "Các cụm hay gặp: 一个不小心，一个不留神，一个失手，一个跟头，一个箭步. Tức là: bất cẩn một chút, sơ ý một chút, lỡ tay một cái, lộn một vòng, và một bước phóng tới.")])

add("bullets", section="Ngữ pháp 注释", title="1. Cấu trúc với 个 (b): động từ + (了) + 个 + tính từ / động từ", size=38,
    items=["个 có tác dụng giống 得: dẫn ra bổ ngữ chỉ kết quả, mức độ",
           "他把心爱的琴摔了个粉碎。 (= 摔得粉碎)",
           "我们都爱听张总讲话，开会的时候张总一张嘴，大家就会笑个不停。",
           "他们的武力太弱，不足以构成威胁，我们一定能够把他们打个落花流水。",
           "Hay gặp: 笑个不停 · 下个不停 · 吃个饱 · 问个明白 · 弄了个乱七八糟",
           "Sắc thái khẩu ngữ, sinh động, nhấn mạnh mức độ cao"],
    say=["Cấu trúc thứ hai: động từ, có thể thêm 了, rồi đến 个, sau đó là tính từ hoặc động từ.",
         F(0, "Trong cấu trúc này, chữ 个 có tác dụng giống chữ 得, dùng để dẫn ra bổ ngữ chỉ kết quả hoặc mức độ."),
         F(1, "Ví dụ một, lấy từ bài khóa: 他把心爱的琴摔了个粉碎。 Ông đập cây đàn yêu quý tan tành. Câu này cũng có thể nói là 摔得粉碎."),
         F(2, "Ví dụ hai: 我们都爱听张总讲话，开会的时候张总一张嘴，大家就会笑个不停。 Chúng tôi đều thích nghe giám đốc Trương nói chuyện, lúc họp hễ ông ấy mở miệng là mọi người cười không ngớt."),
         F(3, "Ví dụ ba: 他们的武力太弱，不足以构成威胁，我们一定能够把他们打个落花流水。 Lực lượng của họ quá yếu, không đủ để gây ra mối đe dọa, chúng ta nhất định sẽ đánh cho họ tan tác. 落花流水 nghĩa đen là hoa rụng nước trôi, nghĩa bóng là thua tan tác."),
         F(4, "Các cụm hay gặp: 笑个不停，下个不停，吃个饱，问个明白，弄了个乱七八糟. Tức là: cười không ngớt, mưa không ngớt, ăn cho no, hỏi cho rõ, và làm cho bừa bộn lung tung."),
         F(5, "Cấu trúc này mang sắc thái khẩu ngữ, rất sinh động, thường nhấn mạnh mức độ cao.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: ghép 6 vế thành 3 đoạn văn liền mạch", reveal=True, size=36,
    items=["A. 他一个失手，碗掉在地上 · B. 不一会儿就把屋子弄了个乱七八糟 · C. 天阴沉沉的，瓢泼大雨下个不停",
           "D. 摔了个粉碎 · E. 儿子放学，和小伙伴在家里玩儿起了捉迷藏 · F. 大家的心里都很着急",
           "Đáp án (1): A + D → 他一个失手，碗掉在地上，摔了个粉碎。",
           "Đáp án (2): E + B → 儿子放学，和小伙伴在家里玩儿起了捉迷藏，不一会儿就把屋子弄了个乱七八糟。",
           "Đáp án (3): C + F → 天阴沉沉的，瓢泼大雨下个不停，大家的心里都很着急。"],
    say=[F(0, "Luyện tập: ghép sáu vế câu thành ba đoạn văn liền mạch. A: 他一个失手，碗掉在地上。 B: 不一会儿就把屋子弄了个乱七八糟。 C: 天阴沉沉的，瓢泼大雨下个不停。"),
         F(1, "D: 摔了个粉碎。 E: 儿子放学，和小伙伴在家里玩儿起了捉迷藏。 F: 大家的心里都很着急。 Các bạn hãy tạm dừng và thử ghép nhé."),
         F(2, "Đáp án thứ nhất: A cộng D. 他一个失手，碗掉在地上，摔了个粉碎。 Anh ấy lỡ tay một cái, chiếc bát rơi xuống đất, vỡ tan tành."),
         F(3, "Đáp án thứ hai: E cộng B. 儿子放学，和小伙伴在家里玩儿起了捉迷藏，不一会儿就把屋子弄了个乱七八糟。 Con trai tan học, chơi trốn tìm với các bạn ở nhà, chẳng mấy chốc đã làm căn phòng bừa bộn lung tung."),
         F(4, "Đáp án thứ ba: C cộng F. 天阴沉沉的，瓢泼大雨下个不停，大家的心里都很着急。 Trời u ám, mưa như trút nước không ngớt, ai nấy trong lòng đều rất sốt ruột. Các bạn để ý: cả ba đoạn đều dùng cấu trúc với 个.")])

add("bullets", chapter="Ngữ pháp: 向来", section="Ngữ pháp 注释", title="2. 向来 xiànglái – xưa nay vẫn, từ trước đến nay", size=38,
    items=["Phó từ: biểu thị từ quá khứ đến hiện tại đều như vậy",
           "Cấu trúc: 向来 + động từ / tính từ (cũng có thể đứng trước chủ ngữ)",
           "他们向来忠厚、老实，为人诚恳。",
           "他教汉语向来重视识字，这样可以使留学生熟悉语素，进而掌握大量的词汇。",
           "琴向来是要弹给知音听的，如今我唯一的知音已不在人世，这琴还弹给谁听呢？",
           "Gần nghĩa: 一向 · 从来 (从来 hay đi với phủ định: 从来不 / 从来没)"],
    say=["Điểm ngữ pháp thứ hai là phó từ 向来.",
         F(0, "向来 biểu thị từ quá khứ cho đến hiện tại đều như vậy, không thay đổi. Tiếng Việt dịch là: xưa nay vẫn, từ trước đến nay vẫn."),
         F(1, "Cấu trúc: 向来 đứng trước động từ hoặc tính từ. Đôi khi nó cũng có thể đứng trước chủ ngữ."),
         F(2, "Ví dụ một: 他们向来忠厚、老实，为人诚恳。 Họ xưa nay vẫn trung hậu, thật thà, đối xử với người khác rất thành khẩn."),
         F(3, "Ví dụ hai: 他教汉语向来重视识字，这样可以使留学生熟悉语素，进而掌握大量的词汇。 Ông dạy tiếng Trung xưa nay luôn coi trọng việc biết chữ, như vậy giúp lưu học sinh quen với các yếu tố cấu tạo từ, từ đó nắm được lượng từ vựng lớn."),
         F(4, "Ví dụ ba, lấy từ bài khóa: 琴向来是要弹给知音听的，如今我唯一的知音已不在人世，这琴还弹给谁听呢？ Đàn xưa nay là để đàn cho tri âm nghe, nay tri âm duy nhất của ta không còn nữa, đàn này còn đàn cho ai nghe?"),
         F(5, "Từ gần nghĩa là 一向 và 从来. Chú ý: 从来 thường đi với phủ định, như 从来不, 从来没; còn 向来 dùng được cả khẳng định lẫn phủ định.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: chọn câu thích hợp điền vào chỗ trống", reveal=True, size=38,
    items=["A. 向来为别人考虑得少 · B. 向来他说了不算 · C. 这地方向来热闹",
           "(1) ________，买东西的、逛街的、看热闹的，人山人海。",
           "Đáp án: C – 这地方向来热闹，买东西的、逛街的、看热闹的，人山人海。",
           "(2) 他的缺点就是太自私，________，为自己想得多。",
           "Đáp án: A – ……太自私，向来为别人考虑得少，为自己想得多。",
           "(3) 他们家的事________，得问他爱人。",
           "Đáp án: B – 他们家的事向来他说了不算，得问他爱人。"],
    say=[F(0, "Luyện tập: chọn câu thích hợp điền vào chỗ trống. Có ba lựa chọn. A: 向来为别人考虑得少。 B: 向来他说了不算。 C: 这地方向来热闹。"),
         F(1, "Câu một: ……，买东西的、逛街的、看热闹的，人山人海。 Người mua sắm, người dạo phố, người xem náo nhiệt, đông nghịt. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: C. 这地方向来热闹，买东西的、逛街的、看热闹的，人山人海。 Nơi này xưa nay vẫn náo nhiệt, người đông như biển."),
         F(3, "Câu hai: 他的缺点就是太自私，……，为自己想得多。 Khuyết điểm của anh ta là quá ích kỷ."),
         F(4, "Đáp án: A. 他的缺点就是太自私，向来为别人考虑得少，为自己想得多。 Xưa nay nghĩ cho người khác thì ít, nghĩ cho mình thì nhiều."),
         F(5, "Câu ba: 他们家的事……，得问他爱人。 Việc nhà họ thì phải hỏi vợ anh ta."),
         F(6, "Đáp án: B. 他们家的事向来他说了不算，得问他爱人。 Việc nhà họ xưa nay anh ta nói không có tác dụng, phải hỏi vợ anh ta. Chú ý: ở đây 向来 đứng trước chủ ngữ 他.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 气势 – 气魄", section="Phân biệt từ 词语辨析", title="Phân biệt 气势 và 气魄",
    common="Giống nhau: đều chỉ người hoặc sự vật thể hiện một sức mạnh, khí thế nào đó. Ví dụ: 天安门城楼的气势/气魄非常雄伟。",
    cols=[{"head": "气势",
           "lines": ["(1) Thiên về thái độ, thanh thế bên ngoài (态度、声势)",
                     "Đúng: 他气势汹汹地冲过来。",
                     "(2) Hay đi với: 气势汹汹 · 气势宏大 · 气势磅礴",
                     "Đúng: 整场演出气势宏大。"]},
          {"head": "气魄",
           "lines": ["(1) Thiên về gan dạ, quyết đoán khi xử lý công việc (胆识和果断的作风)",
                     "Đúng: 他办事很有气魄。",
                     "(2) Hay đi với: 有气魄 · 大气魄 · 有魄力",
                     "Sai: 他气魄汹汹地冲过来。"]}],
    say=["Tiếp theo là phần phân biệt từ: 气势 và 气魄. Hai từ này đều có chữ 气, và đều có thể dịch là khí thế, khí phách, nên rất dễ nhầm.",
         "Điểm giống nhau: cả hai đều chỉ người hoặc sự vật thể hiện ra một sức mạnh, một khí thế nào đó. Ví dụ: 天安门城楼的气势非常雄伟， hoặc 气魄非常雄伟， đều đúng. Thành lầu Thiên An Môn vô cùng hùng vĩ.",
         F(0, "Điểm khác. 气势 thiên về thái độ, thanh thế thể hiện ra bên ngoài. Ví dụ: 他气势汹汹地冲过来。 Anh ta hung hăng xông tới. 气势汹汹 là một cụm cố định, nghĩa là hùng hổ, hung hăng."),
         F(0, "气势 còn hay đi với 宏大 và 磅礴, ví dụ 整场演出气势宏大。 Cả buổi biểu diễn có khí thế hoành tráng."),
         F(1, "Còn 气魄 thiên về phẩm chất bên trong của con người: sự gan dạ, hiểu biết, và tác phong quyết đoán khi xử lý công việc. Ví dụ: 他办事很有气魄。 Anh ấy làm việc rất có khí phách, rất quyết đoán."),
         F(1, "Vì vậy, không thể nói 他气魄汹汹地冲过来, câu này sai."),
         "Mẹo nhớ: 气势 là cái thế, cái vẻ bên ngoài, có thể dùng cho cả cảnh vật, buổi biểu diễn; 气魄 là cái bản lĩnh bên trong, chủ yếu dùng cho con người khi làm việc lớn."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: chọn 气势 hay 气魄 điền vào chỗ trống", reveal=True, size=38,
    items=["(1) 处理大事就应该像他这样果断，有大______。",
           "Đáp án: 气魄 – nói về sự quyết đoán khi xử lý việc lớn.",
           "(2) 整场演出______宏大，精彩异常，深深吸引了广大观众。",
           "Đáp án: 气势 – nói về thanh thế của buổi biểu diễn.",
           "(3) 这样一个有大______的人，如果不当领导实在太可惜了。",
           "Đáp án: 气魄 – nói về bản lĩnh của một con người.",
           "(4) 在比赛中，不管实力如何，我们首先要从______上压倒对方。",
           "Đáp án: 气势 – nói về thái độ, thanh thế bên ngoài."],
    say=[F(0, "Bây giờ chúng ta làm thử. Câu một: 处理大事就应该像他这样果断，有大……。 Xử lý việc lớn thì nên quyết đoán như anh ấy. Chọn 气势 hay 气魄? Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: 气魄. 有大气魄, có khí phách lớn, vì câu nói về sự quyết đoán khi xử lý việc lớn."),
         F(2, "Câu hai: 整场演出……宏大，精彩异常，深深吸引了广大观众。 Cả buổi biểu diễn hoành tráng, đặc sắc lạ thường, thu hút sâu sắc đông đảo khán giả."),
         F(3, "Đáp án: 气势. 气势宏大 là cụm hay gặp, nói về thanh thế của buổi biểu diễn."),
         F(4, "Câu ba: 这样一个有大……的人，如果不当领导实在太可惜了。 Một người có bản lĩnh lớn như vậy, nếu không làm lãnh đạo thì thật quá đáng tiếc."),
         F(5, "Đáp án: 气魄. Câu này nói về phẩm chất, bản lĩnh của một con người."),
         F(6, "Câu bốn: 在比赛中，不管实力如何，我们首先要从……上压倒对方。 Trong thi đấu, bất kể thực lực thế nào, trước hết chúng ta phải áp đảo đối phương về mặt gì đó."),
         F(7, "Đáp án: 气势. 从气势上压倒对方, áp đảo đối phương về khí thế, tức là thái độ, thanh thế bên ngoài.")])

# ======================= TU TỪ =======================
add("bullets", chapter="Tu từ: uyển khúc", section="Tu từ 篇章修辞", title="Tu từ (5): uyển khúc (婉曲) – nói tránh", size=36,
    items=["Cố ý không nói thẳng, mà mượn cách nói khác cùng ý nghĩa để diễn đạt uyển chuyển, vòng vo",
           "临走前，他留下遗言，把坟墓修在江边，到八月十五，好听俞伯牙弹琴。 → không nói 死, dùng 走",
           "各位先聊，我去方便一下。 → không nói 上厕所, dùng 方便",
           "您刚40岁，长得好像有点儿着急。 → không nói 老, dùng 长得着急",
           "Tác dụng: tế nhị, lịch sự, tránh điều kiêng kỵ hoặc khó nói",
           "Tiếng Việt cũng vậy: qua đời → đi xa, về với tổ tiên · đi vệ sinh → đi giải quyết"],
    say=["Phần cuối cùng về lý thuyết là một biện pháp tu từ: uyển khúc, tiếng Trung gọi là 婉曲. 婉 là uyển chuyển, nhẹ nhàng; 曲 ở đây là cong, vòng vèo.",
         F(0, "婉曲 là cố ý không nói thẳng một sự việc, mà mượn một cách nói khác có cùng ý nghĩa, để diễn đạt một cách uyển chuyển, vòng vo."),
         F(1, "Ví dụ một, lấy từ bài khóa: 临走前，他留下遗言，把坟墓修在江边，到八月十五，好听俞伯牙弹琴。 Ở đây không nói thẳng chữ 死, chết, mà dùng chữ 走, đi."),
         F(2, "Ví dụ hai: 各位先聊，我去方便一下。 Mọi người cứ nói chuyện trước, tôi đi giải quyết một chút. Không nói thẳng 上厕所, đi vệ sinh, mà dùng 方便."),
         F(3, "Ví dụ ba: 您刚四十岁，长得好像有点儿着急。 Anh mới bốn mươi tuổi, mà trông có vẻ hơi vội lớn. Không nói thẳng 老, già, mà nói 长得着急, một cách nói hài hước và tế nhị."),
         F(4, "Tác dụng của uyển khúc là giúp lời nói tế nhị, lịch sự, tránh những điều kiêng kỵ hoặc khó nói."),
         F(5, "Tiếng Việt cũng có rất nhiều cách nói tránh như vậy: thay vì nói chết, ta nói qua đời, đi xa, về với tổ tiên; thay vì nói đi vệ sinh, ta nói đi giải quyết. Trong ngữ văn Việt Nam, đây chính là phép nói giảm, nói tránh.")])

add("bullets", section="Tu từ 篇章修辞", title="Luyện tập: câu nào dùng phép uyển khúc?", reveal=True, size=38,
    items=["(1) 在那家商店，我看到了一架旧手风琴，轻巧可爱。",
           "Đáp án: Không – câu miêu tả bình thường.",
           "(2) 妈妈，我的个人问题自己解决好不好，您就别操心了！",
           "Đáp án: Có – 个人问题 thay cho chuyện yêu đương, hôn nhân.",
           "(3) 为了创造一个优美的生活环境，让我们大家共同努力吧！",
           "Đáp án: Không – lời kêu gọi nói thẳng."],
    say=[F(0, "Luyện tập: chỉ ra câu nào dùng phép uyển khúc. Câu một: 在那家商店，我看到了一架旧手风琴，轻巧可爱。 Ở cửa hàng đó, tôi thấy một chiếc đàn phong cầm cũ, nhỏ gọn đáng yêu. Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: không. Đây chỉ là một câu miêu tả bình thường."),
         F(2, "Câu hai: 妈妈，我的个人问题自己解决好不好，您就别操心了！ Mẹ ơi, vấn đề cá nhân của con để con tự giải quyết được không, mẹ đừng lo nữa!"),
         F(3, "Đáp án: có. 个人问题, vấn đề cá nhân, là cách nói tránh, thay cho chuyện yêu đương, kết hôn. Người Trung Quốc rất hay dùng cách nói này."),
         F(4, "Câu ba: 为了创造一个优美的生活环境，让我们大家共同努力吧！ Để tạo nên một môi trường sống tươi đẹp, chúng ta hãy cùng nhau cố gắng!"),
         F(5, "Đáp án: không. Đây là lời kêu gọi nói thẳng.")])

add("bullets", section="Tu từ 篇章修辞", title="Bài tập 4: uyển khúc được dùng thế nào?", reveal=True, size=36,
    items=["(1) 有的人从出生到告别人世，从来没离开过自己生活的村庄。",
           "Đáp án: 告别人世 thay cho 死 (qua đời)",
           "(2) 聂耳以二十二岁的青春年华，过早地写下了他生命的休止符。",
           "Đáp án: 写下了生命的休止符 thay cho 去世",
           "(3) 因为喝水太多，他没过多久就要去方便一下，让坐在他旁边的乘客很不耐烦。",
           "Đáp án: 方便一下 thay cho 上厕所",
           "(4) 我们家那位啊，真是懒得不成样子。",
           "Đáp án: 那位 thay cho 丈夫 / 妻子 (chồng / vợ)"],
    say=[F(0, "Bài tập bốn trong sách: hãy chỉ ra phép uyển khúc được dùng như thế nào. Câu một: 有的人从出生到告别人世，从来没离开过自己生活的村庄。 Có người từ lúc sinh ra cho đến khi từ biệt cõi đời, chưa từng rời khỏi ngôi làng mình sống."),
         F(1, "Đáp án: 告别人世, từ biệt cõi đời, thay cho chữ 死."),
         F(2, "Câu hai: 聂耳以二十二岁的青春年华，过早地写下了他生命的休止符。 Nhiếp Nhĩ ở tuổi thanh xuân hai mươi hai, đã quá sớm viết nên dấu lặng cho cuộc đời mình. Nhiếp Nhĩ là nhạc sĩ, tác giả bài quốc ca Trung Quốc."),
         F(3, "Đáp án: 写下了生命的休止符 thay cho 去世, qua đời. 休止符 là dấu lặng trong âm nhạc; vì Nhiếp Nhĩ là nhạc sĩ, nên cách nói này vừa tế nhị vừa rất hay."),
         F(4, "Câu ba: 因为喝水太多，他没过多久就要去方便一下，让坐在他旁边的乘客很不耐烦。 Vì uống quá nhiều nước, chẳng bao lâu anh ta lại phải đi giải quyết, khiến hành khách ngồi bên cạnh rất khó chịu."),
         F(5, "Đáp án: 方便一下 thay cho 上厕所, đi vệ sinh."),
         F(6, "Câu bốn: 我们家那位啊，真是懒得不成样子。 Người nhà tôi ấy à, đúng là lười không ra thể thống gì."),
         F(7, "Đáp án: 那位, vị ấy, thay cho chồng hoặc vợ. Đây là cách nói tránh khi nhắc đến bạn đời trước mặt người khác, giống như tiếng Việt nói nhà tôi, ông xã nhà tôi.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ đầu", size=40,
    items=["赞叹 → 赞扬 · 赞美 · 称赞 · 夸赞",
           "内涵 → 内容 · 内心 · 内部 · 内在",
           "晴朗 → 晴天 · 放晴 · 晴空 · 天晴",
           "美妙 → 美丽 · 美好 · 美观 · 美味",
           "豪迈 → 豪华 · 豪爽 · 豪放 · 自豪"],
    say=["Phần luyện tập. Bài tập một: dựa vào chữ có dấu chấm bên dưới, tức là chữ đầu của mỗi từ, hãy viết thêm các từ khác.",
         F(0, "Ví dụ mẫu: 赞叹, lấy chữ 赞, có 赞扬，赞美，称赞，夸赞. Tức là tán dương, ca ngợi, khen ngợi, và khen."),
         F(1, "内涵, lấy chữ 内, có 内容，内心，内部，内在. Tức là nội dung, nội tâm, nội bộ, và bên trong."),
         F(2, "晴朗, lấy chữ 晴, có 晴天，放晴，晴空，天晴. Tức là ngày nắng, trời tạnh ráo, bầu trời quang đãng, và trời hửng nắng."),
         F(3, "美妙, lấy chữ 美, có 美丽，美好，美观，美味. Tức là xinh đẹp, tốt đẹp, đẹp mắt, và món ngon."),
         F(4, "豪迈, lấy chữ 豪, có 豪华，豪爽，豪放，自豪. Tức là sang trọng, hào sảng, phóng khoáng, và tự hào.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Hoàn thành câu bằng từ cho sẵn (1–3)", reveal=True, size=38,
    items=["(1) 听了他的一席话，我__________。（领会）",
           "Đáp án: 听了他的一席话，我终于领会了这件事的意义。",
           "(2) __________，不知道在想什么。（出神）",
           "Đáp án: 他坐在窗前望着远方出了神，不知道在想什么。",
           "(3) 我们这些老百姓__________。（平凡）",
           "Đáp án: 我们这些老百姓过的都是平凡的日子。"],
    say=[F(0, "Bài tập hai: dùng từ cho sẵn để hoàn thành câu. Câu một, dùng 领会: 听了他的一席话，我……。 Nghe anh ấy nói một hồi, tôi… Các bạn tạm dừng và thử hoàn thành nhé."),
         F(1, "Đáp án gợi ý: 我终于领会了这件事的意义。 Cuối cùng tôi đã hiểu được ý nghĩa của việc này. 一席话 là một hồi nói chuyện."),
         F(2, "Câu hai, dùng 出神: ……，不知道在想什么。 …, không biết đang nghĩ gì."),
         F(3, "Đáp án gợi ý: 他坐在窗前望着远方出了神，不知道在想什么。 Anh ấy ngồi bên cửa sổ nhìn xa xăm đến ngây người, không biết đang nghĩ gì."),
         F(4, "Câu ba, dùng 平凡: 我们这些老百姓……。 Những người dân thường như chúng tôi…"),
         F(5, "Đáp án gợi ý: 我们这些老百姓过的都是平凡的日子。 Những người dân thường như chúng tôi đều sống những ngày tháng bình thường.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Hoàn thành câu bằng từ cho sẵn (4–6)", reveal=True, size=38,
    items=["(4) 昨天我们__________。（应邀）",
           "Đáp án: 昨天我们应邀参加了一个国际研讨会。",
           "(5) __________，很快就成了无话不谈的好朋友。（投机）",
           "Đáp án: 我们俩第一次见面就聊得很投机，很快就成了无话不谈的好朋友。",
           "(6) 他这个人__________。（向来）",
           "Đáp án: 他这个人向来说话算话，从不骗人。"],
    say=[F(0, "Câu bốn, dùng 应邀: 昨天我们……。 Hôm qua chúng tôi…"),
         F(1, "Đáp án gợi ý: 昨天我们应邀参加了一个国际研讨会。 Hôm qua chúng tôi nhận lời mời tham dự một hội thảo quốc tế."),
         F(2, "Câu năm, dùng 投机: ……，很快就成了无话不谈的好朋友。 …, rất nhanh đã trở thành đôi bạn thân chuyện gì cũng nói với nhau."),
         F(3, "Đáp án gợi ý: 我们俩第一次见面就聊得很投机。 Hai chúng tôi lần đầu gặp mặt đã nói chuyện rất hợp ý. Chú ý: 投机 ở đây là tính từ, làm bổ ngữ sau 聊得."),
         F(4, "Câu sáu, dùng 向来: 他这个人……。 Con người anh ấy…"),
         F(5, "Đáp án gợi ý: 他这个人向来说话算话，从不骗人。 Con người anh ấy xưa nay nói là làm, chưa bao giờ lừa ai.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ điền vào chỗ trống (đoạn 1)", reveal=True, size=36,
    items=["美妙 · 创作 · 精通 · 演奏 · 难能可贵",
           "小王酷爱音乐，____的琴声总能给他带来无尽的享受。有时他会自己____几曲，有时也自己____乐曲。虽然他并不是____音乐之人，可____的是他一直保有对音乐的热爱。",
           "Đáp án: 美妙 · 演奏 · 创作 · 精通 · 难能可贵"],
    say=[F(0, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn một có năm từ: 美妙，创作，精通，演奏，难能可贵."),
         F(1, "小王酷爱音乐，……的琴声总能给他带来无尽的享受。有时他会自己……几曲，有时也自己……乐曲。虽然他并不是……音乐之人，可……的是他一直保有对音乐的热爱。 Các bạn tạm dừng và thử điền nhé."),
         F(2, "Đáp án: 美妙的琴声，演奏几曲，创作乐曲，精通音乐之人，难能可贵. Cả đoạn là: Tiểu Vương say mê âm nhạc, tiếng đàn tuyệt diệu luôn mang lại cho anh niềm vui vô tận. Có lúc anh tự chơi vài khúc, có lúc tự sáng tác nhạc. Tuy anh không phải người tinh thông âm nhạc, nhưng điều đáng quý là anh luôn giữ được tình yêu với âm nhạc.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ điền vào chỗ trống (đoạn 2)", reveal=True, size=36,
    items=["黎明 · 真挚 · 不止 · 逝世 · 坟墓",
           "爷爷____已经有段时间了，可每当提到他，奶奶还是泪流____。从黄昏到____，奶奶整夜思念爷爷，实在忍不住了，她就到爷爷的____前，跟他说说话。爷爷奶奶____的爱情真令人感动。",
           "Đáp án: 逝世 · 不止 · 黎明 · 坟墓 · 真挚"],
    say=[F(0, "Đoạn hai có năm từ: 黎明，真挚，不止，逝世，坟墓."),
         F(1, "爷爷……已经有段时间了，可每当提到他，奶奶还是泪流……。从黄昏到……，奶奶整夜思念爷爷，实在忍不住了，她就到爷爷的……前，跟他说说话。爷爷奶奶……的爱情真令人感动。 Các bạn thử điền nhé."),
         F(2, "Đáp án: 逝世，泪流不止，从黄昏到黎明，坟墓前，真挚的爱情. Cả đoạn là: Ông đã qua đời được một thời gian, nhưng mỗi khi nhắc đến ông, bà vẫn nước mắt tuôn không ngớt. Từ hoàng hôn đến rạng sáng, bà nhớ ông suốt đêm, không kìm được nữa, bà lại ra trước mộ ông, trò chuyện với ông. Tình yêu chân thành của ông bà thật khiến người ta cảm động.")])

# ======================= MỞ RỘNG =======================
add("bullets", chapter="Mở rộng", section="Mở rộng 扩展", title="Mở rộng (1): hiểu nghĩa từng chữ (语素义)", size=34,
    items=["附件 phụ kiện: 附 kèm theo + 件 văn bản → tài liệu đính kèm · 撤销 triệt tiêu: 撤 bỏ đi + 销 hủy → hủy bỏ",
           "联盟 liên minh: 联 liên kết + 盟 đoàn thể · 溶解 dung giải: 溶 tan + 解 phân giải → hòa tan",
           "师范 sư phạm: 师 thầy + 范 khuôn mẫu → người thầy là tấm gương · 无辜 vô cô: 无 không + 辜 tội → vô tội",
           "监督 giám đốc: 监 xem xét + 督 đôn đốc → giám sát (≠ giám đốc công ty 经理)",
           "批发 phê phát: 批 hàng loạt + 发 bán ra → bán buôn, bán sỉ",
           "正 chính: tốt, tích cực (正面) · lớn hơn 0 (正数) · mất electron (正极)",
           "负 phụ: xấu, tiêu cực (负面) · nhỏ hơn 0 (负数) · nhận electron (负极)"],
    say=["Phần mở rộng của sách giúp chúng ta hiểu nghĩa của từng chữ trong một từ. Người Việt học phần này rất thuận lợi nhờ âm Hán Việt.",
         F(0, "附件: 附 là kèm theo, 件 là văn bản, giấy tờ. 附件 là tài liệu đính kèm, ví dụ tệp đính kèm trong thư điện tử. 撤销: 撤 là bỏ đi, 销 là hủy bỏ. 撤销 là hủy bỏ, thu hồi."),
         F(1, "联盟: 联 là liên kết, 盟 là đoàn thể, khối liên minh. 溶解: 溶 là tan ra, 解 là phân giải. 溶解 là hòa tan."),
         F(2, "师范: 师 là thầy, 范 là khuôn mẫu, tấm gương. 师范 là sư phạm, người thầy phải là tấm gương. 无辜: 无 là không, 辜 là tội. 无辜 là vô tội."),
         F(3, "监督: 监 là xem xét, 督 là đôn đốc. 监督 là giám sát. Cẩn thận: Hán Việt là giám đốc, nhưng trong tiếng Trung, 监督 là động từ giám sát, còn giám đốc công ty thì gọi là 经理."),
         F(4, "批发: 批 là hàng loạt, 发 là bán ra. 批发 là bán buôn, bán sỉ. Ngược lại, bán lẻ là 零售."),
         F(5, "Chữ 正 có ba nghĩa: tốt, tích cực, như 正面; lớn hơn không, như 正数, số dương; và mất electron, như 正极, cực dương."),
         F(6, "Chữ 负 cũng có ba nghĩa đối lập: xấu, tiêu cực, như 负面; nhỏ hơn không, như 负数, số âm; và nhận electron, như 负极, cực âm.")])

add("bullets", section="Mở rộng 扩展", title="Mở rộng (2): từ ngữ về đời sống động vật", size=36,
    items=["最近，母猫生育了几只小猫，小猫们发育良好，活泼好动，它们与主人一起生活在一所大别墅里。",
           "有时候，猫咪们会在花园里找青草吃，难道它们也需要植物纤维？有时候，猫咪们会在沙发旁摩擦自己的皮毛，舒服了，就在阳光下懒洋洋地睡大觉。",
           "生育 sinh đẻ · 发育 phát triển (cơ thể) · 别墅 biệt thự · 纤维 chất xơ · 摩擦 cọ xát"],
    say=["Phần mở rộng thứ hai: đọc đoạn văn và làm quen với các từ ngữ về đời sống động vật.",
         F(0, "最近，母猫生育了几只小猫，小猫们发育良好，活泼好动，它们与主人一起生活在一所大别墅里。 Gần đây, mèo mẹ sinh được mấy chú mèo con, mèo con phát triển tốt, hoạt bát hiếu động, chúng sống cùng chủ trong một căn biệt thự lớn."),
         F(1, "有时候，猫咪们会在花园里找青草吃，难道它们也需要植物纤维？有时候，猫咪们会在沙发旁摩擦自己的皮毛，舒服了，就在阳光下懒洋洋地睡大觉。 Có lúc lũ mèo tìm cỏ non trong vườn để ăn, chẳng lẽ chúng cũng cần chất xơ thực vật? Có lúc chúng cọ bộ lông vào cạnh ghế sô pha, dễ chịu rồi thì nằm ngủ một giấc dài lười biếng dưới nắng."),
         F(2, "Các từ cần nhớ: 生育, sinh đẻ. Cẩn thận, đây không phải sinh dục của tiếng Việt, mà là sinh con. 发育, sự phát triển của cơ thể. 别墅, biệt thự. 纤维, chất xơ, sợi. Và 摩擦, cọ xát, ma sát.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 28", size=36,
    items=["Từ vựng trọng tâm: 领会 · 领悟 · 出神 · 精通 · 难能可贵 · 钦佩 · 投机 · 沮丧 · 逝世 · 向来 · 深情厚谊 · 真挚",
           "Ngữ pháp: 一个 + N/V (nhanh, đột ngột) · V + (了) + 个 + bổ ngữ (giống 得) · 向来 (xưa nay vẫn)",
           "Phân biệt: 气势 (thanh thế bên ngoài) ≠ 气魄 (bản lĩnh, quyết đoán)",
           "Tu từ: uyển khúc 婉曲 (走 · 方便 · 长得着急 · 个人问题 · 那位)",
           "## Bài tập về nhà",
           "1. Kể lại câu chuyện 高山流水遇知音 theo 4 gợi ý ở bài tập 5",
           "2. Viết bài 我的知音 (≥ 400 chữ) về cuộc gặp gỡ và thấu hiểu với người tri âm của bạn"],
    say=["Chúng ta cùng tổng kết bài hai mươi tám.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 领会，领悟，出神，精通，难能可贵，钦佩，投机，沮丧，逝世，向来，深情厚谊，真挚."),
         F(1, "Về ngữ pháp: 一个 cộng danh từ hoặc động từ, biểu thị sự việc xảy ra nhanh và đột ngột. Động từ cộng 个 cộng bổ ngữ, chữ 个 giống chữ 得. Và 向来, nghĩa là xưa nay vẫn."),
         F(2, "Về phân biệt từ: 气势 thiên về thái độ, thanh thế bên ngoài; 气魄 thiên về bản lĩnh, sự quyết đoán khi làm việc."),
         F(3, "Về tu từ: phép uyển khúc, nói tránh những điều kiêng kỵ hoặc khó nói, như dùng 走 thay cho chết, 方便 thay cho đi vệ sinh."),
         F(5, "Bài tập về nhà thứ nhất: dựa vào bốn gợi ý ở bài tập năm, hãy kể lại câu chuyện núi cao nước chảy gặp tri âm bằng tiếng Trung."),
         F(6, "Bài tập thứ hai, phần vận dụng của sách: hãy lấy đề bài 我的知音, tri âm của tôi, viết khoảng bốn trăm chữ trở lên, kể lại câu chuyện bạn gặp gỡ và thấu hiểu người tri âm của mình. Nhớ dùng các từ mới, và nếu được, hãy thử dùng cả phép uyển khúc nhé."),
         "Bài học hôm nay cũng khép lại Đơn vị bảy, Đọc tác phẩm kinh điển. Cảm ơn các bạn đã theo dõi bài giảng. Hẹn gặp lại các bạn ở bài hai mươi chín, bài mở đầu Đơn vị tám: 笑的备忘录, Bản ghi nhớ về tiếng cười. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Hạ) – Bài 28: 高山流水遇知音 (Núi cao nước chảy gặp tri âm)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {
        "乐谱": "越谱",          # yuèpǔ
        "应邀": "映邀",          # yìngyāo
        "一曲": "一取",          # yì qǔ
        "几曲": "几取",          # jǐ qǔ
        "曲终": "取终",          # qǔ zhōng
        "为赞叹": "位赞叹",      # wèi
        "为打柴人": "位打柴人",  # wèi
        "为别人": "位别人",      # wèi
        "为自己": "位自己",      # wèi
        "长得": "掌得",          # zhǎngde
        "雄劲": "雄竞",          # xióngjìng
        "纤维": "先维",          # xiānwéi
        "冯梦龙": "逢梦龙",      # Féng
    },
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai28.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
