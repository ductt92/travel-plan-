#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Hạ) – Bài 29 «“笑”的备忘录». Chạy để sinh bai29.json."""
import json
import os

TAG = "HSK 6 (Hạ) · Bài 29 · “笑”的备忘录"
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
    zh="“笑”的备忘录", py="“Xiào” de bèiwànglù", vi="Bài 29: Bản ghi nhớ về tiếng cười",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Hạ.",
         "Hôm nay chúng ta học bài hai mươi chín: 笑的备忘录。 Nghĩa là: Bản ghi nhớ về tiếng cười.",
         "Đây là bài mở đầu của Đơn vị tám, chủ đề 人体探秘, Khám phá cơ thể người. Bài khóa gồm hai bài văn ngắn: bài thứ nhất kể về việc bộ não của chúng ta nghe ra được tiếng cười thật hay giả; bài thứ hai bàn xem cười có thật sự là liều thuốc tốt nhất hay không."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu nội dung hai bài văn ngắn về tiếng cười: thật – giả, lợi – hại",
           "Nắm vững 52 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: phó từ 预先 và cấu trúc ……也好，……也罢",
           "Phân biệt hai chữ 诸 và 各",
           "Tu từ: thủ pháp 设问 – tự hỏi tự đáp"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung hai bài văn ngắn về tiếng cười: làm sao phân biệt cười thật với cười giả, và cười có lợi hay có hại cho sức khỏe."),
         F(1, "Thứ hai, nắm vững năm mươi hai từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học hai điểm ngữ pháp: phó từ 预先, và cấu trúc liệt kê 也好，也罢."),
         F(3, "Thứ tư, phân biệt hai chữ rất hay gặp trong cách xưng hô trang trọng: 诸 và 各."),
         F(4, "Thứ năm, một thủ pháp tu từ rất hữu ích khi viết văn: 设问, tức là tự đặt câu hỏi rồi tự trả lời."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Câu hỏi khởi động", size=40,
    items=["你爱笑吗？ – Bạn có hay cười không?",
           "你能听出别人是真笑还是假笑吗？ – Bạn có nghe ra người khác cười thật hay cười giả không?",
           "怎么分辨出来的？ – Dựa vào đâu: 表情 (nét mặt) · 声音 (giọng) · 其他 (cái khác)",
           "对健康来说，笑是有益的还是有害的？ – Với sức khỏe, cười có lợi hay có hại?",
           "有哪些益处或害处？ – Có những lợi ích (益处) hay tác hại (害处) nào?"],
    say=["Chúng ta bắt đầu bằng phần khởi động. Sách đưa ra một chuỗi câu hỏi về tiếng cười.",
         F(0, "你爱笑吗？ Bạn có hay cười không? 爱笑 là hay cười, thích cười."),
         F(1, "你能听出别人是真笑还是假笑吗？ Bạn có nghe ra người khác đang cười thật hay cười giả không? 真笑 là cười thật, 假笑 là cười giả."),
         F(2, "怎么分辨出来的？ Bạn phân biệt bằng cách nào? Sách gợi ý ba hướng: 表情, nét mặt; 声音, giọng nói; và 其他, những yếu tố khác."),
         F(3, "对健康来说，笑是有益的还是有害的？ Đối với sức khỏe, cười là có lợi hay có hại?"),
         F(4, "有哪些益处或害处？ Có những lợi ích hay tác hại nào? 益处 là lợi ích, 害处 là tác hại."),
         "Các bạn hãy tạm dừng video, thử trả lời những câu hỏi này bằng tiếng Trung, rồi mới xem tiếp nhé. Hai bài văn trong bài khóa sẽ trả lời đúng hai câu hỏi lớn này."])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 表 và 违", size=38,
    items=["## 表 (biểu): bày ra, thể hiện ra ngoài",
           "表态 tỏ thái độ · 表示 biểu thị · 表达 biểu đạt · 表决 biểu quyết · 表白 bày tỏ lòng mình",
           "表明 nói rõ, chứng tỏ · 表情 nét mặt · 表现 biểu hiện · 表演 biểu diễn · 表露 bộc lộ",
           "## 违 (vi): làm trái, đi ngược",
           "违心 trái lòng · 违反 vi phạm · 违背 làm trái · 违法 phạm pháp · 违抗 kháng lệnh · 违禁 phạm điều cấm",
           "违例 phạm quy · 违约 vi phạm hợp đồng · 违章 vi phạm quy định · 违法乱纪 · 事与愿违"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo, rất có lợi cho người Việt vì hầu hết các chữ đều có âm Hán Việt quen thuộc.",
         F(0, "Nhóm thứ nhất có chữ 表, Hán Việt là biểu, nghĩa là bày ra, thể hiện ra bên ngoài."),
         F(1, "表态，表示，表达，表决，表白。 Tức là: tỏ thái độ, biểu thị, biểu đạt, biểu quyết, và bày tỏ lòng mình. Trong bài khóa có cụm 可以不表态, có thể không tỏ thái độ."),
         F(2, "表明，表情，表现，表演，表露。 Tức là: nói rõ hay chứng tỏ, nét mặt, biểu hiện, biểu diễn, và bộc lộ."),
         F(3, "Nhóm thứ hai có chữ 违, Hán Việt là vi, như trong vi phạm, nghĩa là làm trái, đi ngược lại."),
         F(4, "违心，违反，违背，违法，违抗，违禁。 Tức là: trái lòng, vi phạm, làm trái, phạm pháp, kháng lệnh, phạm điều cấm. Bài khóa có hai từ 违背 và 违心: 违背心意的笑声, tiếng cười trái với lòng mình, và 违心地笑, cười một cách trái lòng."),
         F(5, "违例，违约，违章，违法乱纪，事与愿违。 Tức là: phạm quy, vi phạm hợp đồng, vi phạm quy định, phạm pháp loạn kỷ, và 事与愿违, sự việc diễn ra trái với mong muốn.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 活 và 隐", size=38,
    items=["## 活 (hoạt): sống, linh động, lưu thông",
           "激活 kích hoạt · 灵活 linh hoạt · 活动 hoạt động · 活络 lưu thông, linh hoạt · 活水 nước chảy",
           "活血 hoạt huyết · 活扣 nút thắt dễ gỡ · 活期 không kỳ hạn · 活性 hoạt tính",
           "## 隐 (ẩn): giấu kín, không lộ ra",
           "隐含 hàm ẩn · 隐藏 ẩn giấu · 隐蔽 che khuất · 隐居 ở ẩn · 隐瞒 giấu giếm · 隐秘 bí mật · 隐情 nỗi niềm kín",
           "隐忍 nén nhịn · 隐士 ẩn sĩ · 隐私 riêng tư · 隐退 rút lui · 隐姓埋名 mai danh ẩn tích"],
    say=[F(0, "Nhóm thứ ba có chữ 活, Hán Việt là hoạt, nghĩa là sống, linh động, lưu thông."),
         F(1, "激活，灵活，活动，活络，活水。 Tức là: kích hoạt, linh hoạt, hoạt động, lưu thông hay linh hoạt, và nước chảy. Từ 激活 xuất hiện nhiều lần trong bài khóa: 激活大脑中的特定区域, kích hoạt một vùng đặc thù trong não."),
         F(2, "活血，活扣，活期，活性。 Tức là: hoạt huyết, nút thắt dễ gỡ, không kỳ hạn như tiền gửi không kỳ hạn, và hoạt tính."),
         F(3, "Nhóm cuối cùng có chữ 隐, Hán Việt là ẩn, nghĩa là giấu kín, không để lộ ra."),
         F(4, "隐含，隐藏，隐蔽，隐居，隐瞒，隐秘，隐情。 Tức là: hàm ẩn, ẩn giấu, che khuất, ở ẩn, giấu giếm, bí mật, và nỗi niềm thầm kín. Bài khóa có 隐瞒, giấu giếm, và 隐含, ẩn chứa."),
         F(5, "隐忍，隐士，隐私，隐退，隐姓埋名。 Tức là: nén nhịn, ẩn sĩ, sự riêng tư, rút lui, và 隐姓埋名, giấu tên giấu họ, giống thành ngữ mai danh ẩn tích của tiếng Việt."),
         "Chỉ cần nắm nghĩa của một chữ gốc, ta có thể đoán được nghĩa của cả một nhóm từ. Các bạn hãy áp dụng cách này khi học từ mới nhé."])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, nhãn nếu là từ kèm theo])
V = [
    ("备忘录", "bèiwànglù", "bị vong lục", "danh từ", "bản ghi nhớ, sổ ghi nhớ", "他把明天要做的事写进了备忘录。", "Anh ấy ghi những việc cần làm ngày mai vào sổ ghi nhớ.",
     "Danh từ, nghĩa là bản ghi nhớ, sổ ghi nhớ. 备 là chuẩn bị, 忘 là quên, 录 là ghi chép: ghi lại để phòng khi quên. Tên bài 笑的备忘录 nghĩa là bản ghi nhớ về tiếng cười, tức là những điều cần ghi nhớ về cười."),
    ("岂有此理", "qǐyǒucǐlǐ", "khởi hữu thử lý", "thành ngữ", "làm gì có lý ấy, thật là vô lý", "拿了钱不办事，真是岂有此理！", "Nhận tiền mà không làm việc, thật là vô lý hết sức!",
     "Thành ngữ. 岂 là lẽ nào, 此 là này, 理 là lý lẽ. Nghĩa đen: lẽ nào lại có lý lẽ như thế; dùng để bày tỏ sự bất bình trước một việc vô lý. Bài khóa mở đầu ngay bằng câu 真是岂有此理."),
    ("庸俗", "yōngsú", "dung tục", "tính từ", "tầm thường, dung tục, thiếu tinh tế", "这部电影的内容太庸俗了。", "Nội dung bộ phim này quá dung tục.",
     "Tính từ, nghĩa là tầm thường, thấp kém, thiếu tinh tế. Âm Hán Việt dung tục cũng có trong tiếng Việt với nghĩa tương tự."),
    ("档次", "dàngcì", "đáng thứ", "danh từ", "đẳng cấp, mức (chất lượng)", "这家饭店的档次很高。", "Nhà hàng này rất cao cấp.",
     "Danh từ, nghĩa là cấp bậc, đẳng cấp về chất lượng. 高档 là cao cấp; còn 不上档次 là không đạt đẳng cấp, kém sang, như trong bài khóa: 不上档次的笑话, câu chuyện cười nhạt nhẽo, kém sang."),
    ("诸位", "zhūwèi", "chư vị", "đại từ", "các vị, quý vị", "诸位，请安静一下。", "Thưa quý vị, xin hãy trật tự một chút.",
     "Đại từ, nghĩa là các vị, quý vị, dùng để gọi nhiều người một cách trang trọng. Lát nữa chúng ta sẽ phân biệt kỹ chữ 诸 với chữ 各."),
    ("难堪", "nánkān", "nan kham", "tính từ", "khó xử, ngượng ngùng, bẽ mặt", "他当众批评我，让我很难堪。", "Anh ta phê bình tôi trước mặt mọi người, khiến tôi rất khó xử.",
     "Tính từ, nghĩa là khó xử, ngượng ngùng, bẽ mặt. 堪 là chịu nổi, nên 难堪 nghĩa gốc là khó mà chịu nổi."),
    ("虚伪", "xūwěi", "hư ngụy", "tính từ", "giả dối, đạo đức giả", "我不喜欢虚伪的人。", "Tôi không thích người giả dối.",
     "Tính từ, nghĩa là giả dối, không thật lòng, thường dùng để nói về con người, thái độ hay lời nói."),
    ("违背", "wéibèi", "vi bội", "động từ", "làm trái, đi ngược lại", "我们不能违背自己的良心。", "Chúng ta không thể làm trái lương tâm của mình.",
     "Động từ, nghĩa là làm trái, đi ngược lại, như 违背良心, làm trái lương tâm, 违背规律, đi ngược quy luật. Bài khóa có cụm 违背心意的笑声, tiếng cười trái với lòng mình."),
    ("回避", "huíbì", "hồi tị", "động từ", "né tránh, lảng tránh", "他总是回避这个问题。", "Anh ấy luôn né tránh vấn đề này.",
     "Động từ, nghĩa là né tránh, lảng tránh, không muốn đối mặt với một người hay một vấn đề."),
    ("岔", "chà", "xá", "động từ", "rẽ sang hướng khác; lảng (chuyện)", "他赶紧把话题岔开了。", "Anh ấy vội vàng lảng sang chuyện khác.",
     "Động từ, nghĩa gốc là rẽ sang một hướng khác. 把话题岔开 là lảng sang chuyện khác, đánh trống lảng. Danh từ 岔路 là đường rẽ. Ở phần hai bài khóa còn có từ 岔气, bị sóc hông."),
    ("装聋装哑", "zhuānglóng zhuāngyǎ", "trang lung trang á", "thành ngữ", "giả câm giả điếc, làm như không biết", "有人问起这件事，他就装聋装哑。", "Hễ có người hỏi đến chuyện này, anh ấy liền giả câm giả điếc.",
     "Cụm thành ngữ. 装 là giả vờ, 聋 là điếc, 哑 là câm. Nghĩa là giả câm giả điếc, cố tình làm như không nghe, không biết gì."),
    ("聋哑", "lóngyǎ", "lung á", "tính từ", "câm điếc", "这所学校专门教聋哑儿童。", "Ngôi trường này chuyên dạy trẻ em câm điếc.",
     "Đây là từ kèm theo trong mục mười một của sách. Tính từ, nghĩa là câm điếc. 聋哑人 là người câm điếc.", "kèm 11"),
    ("画蛇添足", "huàshé-tiānzú", "họa xà thiêm túc", "thành ngữ", "vẽ rắn thêm chân, làm thừa hóa hỏng", "文章已经很好了，再加这段就是画蛇添足。", "Bài văn đã rất hay rồi, thêm đoạn này là vẽ rắn thêm chân.",
     "Thành ngữ có điển tích: mấy người thi vẽ rắn, ai vẽ xong trước được uống rượu. Một người vẽ xong trước, lại vẽ thêm chân cho rắn, thế là thua. Nghĩa là làm thêm việc thừa, hóa ra hỏng việc."),
    ("机灵", "jīling", "cơ linh", "tính từ", "lanh lợi, nhanh nhẹn", "这个孩子又聪明又机灵。", "Đứa bé này vừa thông minh vừa lanh lợi.",
     "Tính từ, nghĩa là lanh lợi, nhanh trí. Chữ 灵 ở đây đọc thanh nhẹ."),
    ("周密", "zhōumì", "chu mật", "tính từ", "chu đáo, kín kẽ, tỉ mỉ", "这次活动计划得很周密。", "Hoạt động lần này được lên kế hoạch rất chu đáo.",
     "Tính từ, nghĩa là chu đáo, kín kẽ, tính toán đầy đủ mọi mặt. 周 là khắp, đủ; 密 là kín, dày."),
    ("途径", "tújìng", "đồ kính", "danh từ", "con đường, cách thức", "读书是获得知识的重要途径。", "Đọc sách là con đường quan trọng để thu nhận tri thức.",
     "Danh từ, nghĩa đen là con đường, nghĩa bóng là cách thức, phương pháp để đạt được điều gì đó."),
    ("虚假", "xūjiǎ", "hư giả", "tính từ", "không thật, giả tạo", "这则广告的内容很虚假。", "Nội dung của quảng cáo này rất giả tạo.",
     "Tính từ, nghĩa là không thật, giả tạo. So với 虚伪 thường nói về tính cách con người, thì 虚假 hay dùng cho thông tin, tình cảm, hiện tượng, như 虚假广告, quảng cáo sai sự thật."),
    ("特定", "tèdìng", "đặc định", "tính từ", "riêng biệt, nhất định, đặc thù", "这种药只在特定情况下使用。", "Loại thuốc này chỉ dùng trong những trường hợp nhất định.",
     "Tính từ, nghĩa là được chỉ định riêng, nhất định, đặc thù. Bài khóa có cụm 特定区域, vùng đặc thù trong não."),
    ("缘故", "yuángù", "duyên cố", "danh từ", "nguyên do, lý do", "他今天没来，不知是什么缘故。", "Hôm nay anh ấy không đến, không biết vì nguyên do gì.",
     "Danh từ, nghĩa là nguyên do, lý do, giống 原因."),
    ("意向", "yìxiàng", "ý hướng", "danh từ", "ý định, ý đồ", "双方都有合作的意向。", "Cả hai bên đều có ý định hợp tác.",
     "Danh từ, nghĩa là ý định, ý muốn, hướng mà người ta định làm. 合作意向 là ý định hợp tác."),
    ("诚挚", "chéngzhì", "thành chí", "tính từ", "chân thành, thành khẩn", "向您表示诚挚的感谢！", "Xin gửi tới ngài lời cảm ơn chân thành!",
     "Tính từ, nghĩa là chân thành, tha thiết, sắc thái trang trọng, hay dùng trong văn viết, thư từ."),
    ("一丝不苟", "yìsī-bùgǒu", "nhất ti bất cẩu", "thành ngữ", "cẩn thận tỉ mỉ, không qua loa chút nào", "他工作起来一丝不苟。", "Anh ấy làm việc vô cùng cẩn thận tỉ mỉ.",
     "Thành ngữ. 丝 là sợi tơ, chỉ một chút xíu; 苟 là cẩu thả. Nghĩa là không cẩu thả dù chỉ một chút, tức là cẩn thận tỉ mỉ."),
    ("倾听", "qīngtīng", "khuynh thính", "động từ", "lắng nghe", "我们要学会倾听别人的意见。", "Chúng ta phải học cách lắng nghe ý kiến của người khác.",
     "Động từ, nghĩa là lắng nghe. 倾 là nghiêng, hình ảnh nghiêng người về phía trước để nghe cho kỹ."),
    ("视频", "shìpín", "thị tần", "danh từ", "video", "我每天晚上都看学汉语的视频。", "Tối nào tôi cũng xem video học tiếng Trung.",
     "Danh từ, nghĩa là video. 网站视频 là video trên trang mạng."),
    ("一目了然", "yímù-liǎorán", "nhất mục liễu nhiên", "thành ngữ", "nhìn qua là rõ ngay", "这张图表让人一目了然。", "Biểu đồ này giúp người xem nhìn qua là hiểu ngay.",
     "Thành ngữ. 一目 là một cái nhìn, 了然 là rõ ràng. Nghĩa là chỉ cần nhìn qua một lần là rõ ngay."),
    ("预先", "yùxiān", "dự tiên", "phó từ", "trước, sẵn từ trước", "出发前要预先订好车票。", "Trước khi xuất phát phải đặt vé xe từ trước.",
     "Phó từ, nghĩa là làm trước khi sự việc xảy ra. Đây là điểm ngữ pháp thứ nhất, ta sẽ học kỹ ở phần sau."),
    ("直觉", "zhíjué", "trực giác", "danh từ", "trực giác", "我的直觉告诉我，他在说谎。", "Trực giác mách bảo tôi rằng anh ta đang nói dối.",
     "Danh từ, nghĩa là trực giác, âm Hán Việt giống hệt tiếng Việt. 凭直觉 là dựa vào trực giác."),
    ("探测", "tàncè", "thám trắc", "động từ", "dò, thăm dò (bằng thiết bị)", "科学家用仪器探测海底的情况。", "Các nhà khoa học dùng thiết bị để thăm dò tình hình đáy biển.",
     "Động từ, nghĩa là dò tìm, thăm dò, thường bằng máy móc. Trong bài, tác giả nói não người như một đôi mắt có thể 探测 niềm vui của người khác là thật hay giả."),
    ("智商", "zhìshāng", "trí thương", "danh từ", "chỉ số thông minh (IQ)", "智商高不一定就能成功。", "Chỉ số thông minh cao chưa chắc đã thành công.",
     "Danh từ, nghĩa là chỉ số thông minh, tức IQ. Người ta còn nói 情商, chỉ số cảm xúc, tức EQ."),
    ("提炼", "tíliàn", "đề luyện", "động từ", "tinh luyện; chắt lọc, đúc kết", "请从文章中提炼出主要观点。", "Hãy chắt lọc ra các quan điểm chính từ bài văn.",
     "Động từ. Nghĩa gốc là tinh luyện, lọc lấy phần tinh chất, ví dụ từ quặng hay dầu mỏ. Nghĩa bóng là chắt lọc, đúc kết thông tin, ý tưởng."),
    ("相声", "xiàngsheng", "tướng thanh", "danh từ", "tấu nói (loại hình nói hài)", "中国人很喜欢听相声。", "Người Trung Quốc rất thích nghe tấu nói.",
     "Danh từ, chỉ một loại hình nghệ thuật nói hài của Trung Quốc, thường do hai người đối đáp với nhau để gây cười. Chú ý đọc là xiàngsheng: chữ 相 thanh bốn, chữ 声 thanh nhẹ."),
    ("座右铭", "zuòyòumíng", "tọa hữu minh", "danh từ", "châm ngôn (để răn mình)", "活到老，学到老是我的座右铭。", "Sống đến già, học đến già là châm ngôn của tôi.",
     "Danh từ. Người xưa viết lời răn mình rồi đặt ở bên phải chỗ ngồi, 座 là chỗ ngồi, 右 là bên phải, 铭 là lời khắc ghi. Nghĩa là câu châm ngôn sống của một người."),
    ("通用", "tōngyòng", "thông dụng", "động từ", "dùng chung, dùng rộng rãi", "英语是国际上通用的语言。", "Tiếng Anh là ngôn ngữ được dùng rộng rãi trên thế giới.",
     "Động từ, nghĩa là được dùng chung, dùng phổ biến ở nhiều nơi. Âm Hán Việt là thông dụng."),
    ("调节", "tiáojié", "điều tiết", "động từ", "điều tiết, điều chỉnh", "运动可以调节心情。", "Vận động có thể điều tiết tâm trạng.",
     "Động từ, nghĩa là điều tiết, điều chỉnh cho vừa phải. Chú ý chữ 调 ở đây đọc là tiáo, thanh hai."),
    ("循环", "xúnhuán", "tuần hoàn", "động từ", "tuần hoàn, quay vòng", "多运动能促进血液循环。", "Vận động nhiều có thể thúc đẩy tuần hoàn máu.",
     "Động từ, nghĩa là tuần hoàn, chuyển động quay vòng rồi lại trở về chỗ cũ. 血液循环 là tuần hoàn máu."),
    ("收缩", "shōusuō", "thu súc", "động từ", "co lại, thu nhỏ lại", "天冷的时候，血管会收缩。", "Khi trời lạnh, mạch máu sẽ co lại.",
     "Động từ, nghĩa là co lại, thu nhỏ lại, trái nghĩa với 舒张 hay 扩张, giãn ra."),
    ("氧气", "yǎngqì", "dưỡng khí", "danh từ", "khí oxy", "高原上的氧气比较少。", "Trên cao nguyên, khí oxy tương đối ít.",
     "Danh từ, nghĩa là khí oxy, Hán Việt là dưỡng khí. 吸氧量 là lượng oxy hít vào."),
    ("桨", "jiǎng", "tưởng", "danh từ", "mái chèo", "他拿起桨，慢慢地划船。", "Anh ấy cầm mái chèo lên, chậm rãi chèo thuyền.",
     "Danh từ, nghĩa là mái chèo. 用桨划船 là dùng mái chèo để chèo thuyền."),
    ("试验", "shìyàn", "thí nghiệm", "động từ", "thử nghiệm, làm thí nghiệm", "这种新药还在试验阶段。", "Loại thuốc mới này vẫn đang trong giai đoạn thử nghiệm.",
     "Động từ, nghĩa là thử nghiệm, làm thí nghiệm để xem kết quả. Cũng dùng như danh từ: 做试验, làm thí nghiệm."),
    ("脂肪", "zhīfáng", "chi phương", "danh từ", "mỡ, chất béo", "少吃脂肪多的食物对身体好。", "Ăn ít thức ăn nhiều mỡ thì tốt cho cơ thể.",
     "Danh từ, nghĩa là mỡ, chất béo. 消耗脂肪 là tiêu hao mỡ."),
    ("动脉", "dòngmài", "động mạch", "danh từ", "động mạch", "动脉硬化是一种常见的老年病。", "Xơ cứng động mạch là một bệnh thường gặp ở người già.",
     "Danh từ, nghĩa là động mạch, âm Hán Việt giống hệt tiếng Việt. Ngược lại là 静脉, tĩnh mạch."),
    ("实质", "shízhì", "thực chất", "danh từ", "thực chất, bản chất", "这两个问题的实质是一样的。", "Thực chất của hai vấn đề này là như nhau.",
     "Danh từ, nghĩa là thực chất, bản chất bên trong. 实质性 là có tính thực chất; bài khóa có cụm 实质性的证据, bằng chứng thực chất."),
    ("肆无忌惮", "sìwú-jìdàn", "tứ vô kỵ đạn", "thành ngữ", "không kiêng nể gì, ngang nhiên", "他在图书馆里肆无忌惮地大声说话。", "Anh ta ngang nhiên nói to trong thư viện, chẳng kiêng nể gì.",
     "Thành ngữ. 肆 là phóng túng, 忌惮 là kiêng sợ. Nghĩa là làm càn, không kiêng nể gì cả, thường mang nghĩa xấu. Trong bài, 肆无忌惮地笑 là cười thả cửa, không chút kiềm chế."),
    ("损坏", "sǔnhuài", "tổn hoại", "động từ", "làm hỏng, làm tổn hại", "请不要损坏公共财物。", "Xin đừng làm hư hại tài sản công.",
     "Động từ, nghĩa là làm hỏng, làm tổn hại. 损坏健康 là làm tổn hại sức khỏe."),
    ("倾向", "qīngxiàng", "khuynh hướng", "động từ", "nghiêng về, thiên về", "我倾向于第二个方案。", "Tôi nghiêng về phương án thứ hai.",
     "Động từ, thường dùng 倾向于, nghĩa là nghiêng về, thiên về một ý kiến. Nó cũng là danh từ, nghĩa là khuynh hướng."),
    ("分寸", "fēncun", "phân thốn", "danh từ", "chừng mực (trong lời nói, việc làm)", "说话要注意分寸。", "Nói năng phải chú ý chừng mực.",
     "Danh từ. 分 và 寸 là những đơn vị đo chiều dài rất nhỏ, nên 分寸 chỉ mức độ vừa phải, chừng mực trong lời nói và việc làm. Chú ý chữ 寸 ở đây đọc thanh nhẹ."),
    ("恰到好处", "qiàdào-hǎochù", "kháp đáo hảo xứ", "thành ngữ", "vừa đúng mức, vừa khéo", "菜里的盐放得恰到好处。", "Muối trong món ăn nêm vừa đúng độ.",
     "Thành ngữ. 恰 là vừa vặn, 好处 ở đây là chỗ tốt nhất. Nghĩa là làm vừa đúng mức, không thừa không thiếu."),
    ("是非", "shìfēi", "thị phi", "danh từ", "đúng và sai, phải trái", "他是一个不分是非的人。", "Anh ta là người không phân biệt phải trái.",
     "Danh từ, nghĩa là đúng và sai, phải và trái. Ngoài ra còn có nghĩa là chuyện thị phi, điều tiếng, như 搬弄是非, gây chuyện thị phi."),
    ("探讨", "tàntǎo", "thám thảo", "động từ", "nghiên cứu thảo luận, bàn bạc", "我们一起来探讨这个问题。", "Chúng ta cùng nghiên cứu thảo luận vấn đề này.",
     "Động từ, nghĩa là nghiên cứu và thảo luận để tìm hiểu sâu một vấn đề."),
    ("收益", "shōuyì", "thu ích", "danh từ", "lợi ích, thu nhập", "读书的收益是一辈子的。", "Lợi ích của việc đọc sách theo ta cả đời.",
     "Danh từ, nghĩa là lợi ích hay thu nhập có được. Trong bài, tác giả so sánh 风险, rủi ro, với 收益, lợi ích, của sự hài hước."),
    ("起哄", "qǐ hòng", "khởi hống", "động từ", "(nhiều người) làm ồn, la ó, trêu chọc", "大家在一旁起哄，他的脸一下子红了。", "Mọi người bên cạnh ồ lên trêu chọc, mặt anh ấy đỏ bừng.",
     "Động từ, nghĩa là nhiều người cùng làm ồn, la ó, hoặc trêu chọc ai đó cho vui. Chú ý chữ 哄 ở đây đọc là hòng, thanh bốn."),
    ("斟酌", "zhēnzhuó", "châm chước", "động từ", "cân nhắc kỹ", "这个词用得不太合适，请再斟酌一下。", "Từ này dùng chưa hợp lắm, xin hãy cân nhắc lại.",
     "Động từ, nghĩa là cân nhắc kỹ lưỡng. Cẩn thận: châm chước trong tiếng Việt nghĩa là nới tay, thông cảm, còn 斟酌 trong tiếng Trung là cân nhắc, suy tính kỹ, nghĩa khác hẳn."),
    ("恰当", "qiàdàng", "kháp đáng", "tính từ", "thích đáng, thích hợp", "你这个词用得很恰当。", "Từ này bạn dùng rất thích hợp.",
     "Tính từ, nghĩa là thích đáng, thích hợp. Chú ý chữ 当 ở đây đọc là dàng, thanh bốn."),
]

NV = sum(1 for v in V if len(v) == 8)  # số từ theo sách (không tính từ kèm theo)
add("bullets", chapter=f"Từ mới ({NV} từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=[f"Bài 29 có {NV} từ mới (thêm từ kèm theo 聋哑), chia thành {(len(V) + 2) // 3} nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 相声 (xiàngsheng), 调节 (tiáo), 起哄 (hòng), 恰当 (dàng)"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có năm mươi hai từ, cộng thêm một từ kèm theo là 聋哑. Thầy chia thành mười tám nhóm nhỏ, mỗi nhóm ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số từ có âm đọc đặc biệt, thầy sẽ nhắc khi gặp. Chúng ta bắt đầu nhé.")])

n = 0
for g in range(0, len(V), 3):
    group = V[g:g + 3]
    words, say = [], []
    for i, item in enumerate(group):
        zh, py, hv, loai, vi, ex, exvi, expl = item[:8]
        if len(item) > 8:
            label = item[8]
            intro = f"Từ kèm theo: {zh}。 {zh}。 Hán Việt là {hv}."
        else:
            n += 1
            label = str(n)
            intro = f"Từ số {n}: {zh}。 {zh}。 Hán Việt là {hv}."
        words.append({"zh": zh, "py": py, "hv": hv.upper(), "loai": f"{label}. {loai}", "vi": vi, "ex": ex, "exvi": exvi})
        say.append(F(i, intro, zr=120))
        say.append(F(i, f"{expl} Ví dụ: {ex}{'' if ex[-1] in '。…？！，' else '，'} {exvi[0].upper() + exvi[1:]}{'' if exvi.endswith(('.', '!', '?')) else '.'}", zr=130))
    add("vocab", section="Từ mới 生词", title=f"Từ mới ({g + 1}–{g + len(group)} / {len(V)})",
        words=words, say=say)

# ======================= BÀI KHÓA =======================
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung nếu khác: số viết bằng chữ Hán, bỏ ngoặc kép])
P = [
    ("（一）大脑能“听”出笑声的真假\n真是岂有此理，难道我们听到庸俗、不上档次的笑话假笑两声、敷衍一下也不可以吗？可是，好像确实不行。",
     "Phần một: Não bộ có thể nghe ra tiếng cười thật hay giả. — Thật là vô lý hết sức! Lẽ nào khi nghe một câu chuyện cười dung tục, kém sang, chúng ta cười giả vài tiếng cho qua chuyện cũng không được sao? Thế nhưng, hình như đúng là không được thật.",
     ["Bài văn mở đầu bằng 岂有此理, giọng như đang bất bình. Tiếp theo là câu hỏi 难道……也不可以吗？, nghĩa là lẽ nào… cũng không được sao? 敷衍 là làm qua loa, đối phó cho xong.",
      "Tác giả đặt câu hỏi rồi tự trả lời ngay: 可是，好像确实不行. Đây chính là thủ pháp 设问 mà ta sẽ học ở cuối bài."],
     "一，大脑能听出笑声的真假。真是岂有此理，难道我们听到庸俗、不上档次的笑话假笑两声、敷衍一下也不可以吗？可是，好像确实不行。"),
    ("诸位，如果你不想难堪，不想让别人发现你发出的是虚伪、违背心意的笑声，你可以回避，可以不表态，可以把话题岔开，可以装聋装哑，但不要画蛇添足，违心地笑。",
     "Thưa quý vị, nếu bạn không muốn khó xử, không muốn người khác phát hiện ra tiếng cười của mình là giả dối, trái với lòng mình, thì bạn có thể né tránh, có thể không tỏ thái độ, có thể lảng sang chuyện khác, có thể giả câm giả điếc, nhưng đừng vẽ rắn thêm chân mà cười một cách trái lòng.",
     ["Tác giả dùng bốn vế 可以 liên tiếp: 可以回避，可以不表态，可以把话题岔开，可以装聋装哑. Cách liệt kê này tạo nhịp điệu mạnh, rồi chuyển ý bằng 但不要, nhưng đừng.",
      "Các bạn để ý: các vế sau đều lược bỏ chủ ngữ 你. 违心地笑 là cười trái với lòng mình; 违心 là từ trong nhóm chữ 违 ở phần khởi động."]),
    ("因为只要你笑，不管你多机灵，不管你掩饰得多么周密，别人都能看出你的笑是真心实意，还是虚情假意、装模作样。",
     "Bởi vì chỉ cần bạn cười, thì dù bạn lanh lợi đến đâu, dù bạn che đậy kín kẽ đến mức nào, người khác cũng đều nhìn ra được nụ cười của bạn là thật lòng thật dạ, hay là giả tình giả ý, làm bộ làm tịch.",
     ["Cấu trúc: 只要……，不管……，不管……，都……, nghĩa là: chỉ cần…, bất kể…, bất kể…, đều…. 掩饰 là che đậy.",
      "Hai thành ngữ đối lập: 真心实意, thật lòng thật dạ, và 虚情假意, giả tình giả ý. Còn 装模作样 là làm bộ làm tịch."]),
    ("有人不禁要问，人是通过什么途径识别“笑”背后的真实情感呢？研究者发现，我们在听到发自内心的笑声和虚假的笑声时，大脑会呈现出完全不同的反应。",
     "Có người không khỏi hỏi: con người dựa vào con đường nào để nhận ra tình cảm thật đằng sau nụ cười? Các nhà nghiên cứu phát hiện rằng, khi chúng ta nghe tiếng cười xuất phát từ đáy lòng và tiếng cười giả tạo, não bộ sẽ có những phản ứng hoàn toàn khác nhau.",
     ["不禁 là không kìm được, không khỏi. 通过什么途径 là thông qua con đường nào. 识别 là nhận biết, phân biệt.",
      "发自内心 là xuất phát từ đáy lòng. 呈现出 là hiện ra, thể hiện ra."]),
    ("假笑声会激活大脑中用于破译情感信息的特定区域，同时大脑会自动分析假笑的缘故，假笑者想隐瞒什么，以及假笑者的意向；诚挚的笑声则会激活大脑中与快乐和积极情绪相关的区域。",
     "Tiếng cười giả sẽ kích hoạt một vùng đặc thù trong não dùng để giải mã thông tin cảm xúc; đồng thời não sẽ tự động phân tích nguyên do của nụ cười giả, người cười giả muốn che giấu điều gì, và ý đồ của người cười giả. Còn tiếng cười chân thành thì kích hoạt những vùng não liên quan đến niềm vui và cảm xúc tích cực.",
     ["激活 là kích hoạt, từ trong nhóm chữ 活 ở phần khởi động. 破译 là giải mã. 隐瞒 là giấu giếm.",
      "Câu dùng dấu chấm phẩy để đối chiếu hai vế: 假笑声会…… với 诚挚的笑声则会……. Chữ 则 ở đây nghĩa là còn, thì, dùng để nêu sự đối lập."]),
    ("为了证实这一理论，一丝不苟的研究者让志愿者倾听网站视频中的笑声，同时记录他们大脑的反应，并将志愿者听到真笑与假笑时大脑的反应做对比。",
     "Để chứng thực lý thuyết này, các nhà nghiên cứu làm việc cẩn thận tỉ mỉ đã cho các tình nguyện viên lắng nghe tiếng cười trong video trên mạng, đồng thời ghi lại phản ứng của não họ, rồi đem phản ứng của não khi nghe tiếng cười thật và khi nghe tiếng cười giả ra so sánh.",
     ["证实 là chứng thực, chứng minh là đúng. 志愿者 là tình nguyện viên.",
      "将……做对比 là đem… ra so sánh; chữ 将 ở đây bằng chữ 把, dùng trong văn viết."]),
    ("测试结果一目了然，志愿者在预先未被告知测试目的的情况下，仅凭直觉就能准确地分辨出假笑声。天呀，人的大脑中竟然深藏着一双能够探测他人喜悦之情真伪的眼睛！",
     "Kết quả thử nghiệm nhìn qua là rõ: trong tình huống không được cho biết trước mục đích thử nghiệm, các tình nguyện viên chỉ dựa vào trực giác đã có thể phân biệt chính xác tiếng cười giả. Trời ơi, trong não người lại ẩn giấu sâu một đôi mắt có thể dò ra niềm vui của người khác là thật hay giả!",
     ["在……的情况下 là trong tình huống…. 预先未被告知 là chưa được cho biết trước; 未 bằng 没有, 被 là bị động. 预先 chính là điểm ngữ pháp thứ nhất.",
      "仅凭 là chỉ dựa vào. 竟然 là vậy mà, không ngờ. Câu cảm thán 天呀 thể hiện sự kinh ngạc, còn 一双眼睛 là cách nói hình ảnh, ví khả năng của não như một đôi mắt."]),
    ("研究者指出：“人类大脑对于笑声中所隐含的社会和情感信息非常敏感，这不完全是智商问题。",
     "Các nhà nghiên cứu chỉ ra: Bộ não con người rất nhạy cảm với những thông tin xã hội và cảm xúc ẩn chứa trong tiếng cười, điều này không hoàn toàn là vấn đề chỉ số thông minh.",
     ["对于……非常敏感 là rất nhạy cảm đối với…. 所隐含的 là được ẩn chứa; 所 cộng động từ cộng 的 là cấu trúc văn viết.",
      "隐含 là hàm ẩn, ẩn chứa, một từ trong nhóm chữ 隐 ở phần khởi động. Ý câu này: nhận ra tiếng cười giả không phụ thuộc vào việc ai thông minh hơn."]),
    ("当志愿者听到笑声时，会开启大脑中与心智相关的区域，从而获知他人的情感或精神状态，有些志愿者还动用了大脑中控制运动和感知的部分，进而更精准地提炼出真假笑声背后的信息。”",
     "Khi tình nguyện viên nghe thấy tiếng cười, họ sẽ mở ra những vùng não liên quan đến tâm trí, nhờ đó biết được trạng thái cảm xúc hoặc tinh thần của người khác; một số tình nguyện viên còn huy động cả những bộ phận của não điều khiển vận động và cảm giác, từ đó chắt lọc ra chính xác hơn thông tin đằng sau tiếng cười thật hay giả.",
     ["从而 là từ đó, nhờ đó; 进而 là rồi tiến thêm một bước. Hai liên từ này giúp lập luận chặt chẽ, nối tiếp nhau.",
      "获知 là biết được. 动用 là huy động, sử dụng. 提炼出……信息 là chắt lọc ra thông tin, đúng nghĩa bóng của từ 提炼 ta vừa học."]),
    ("（二）笑未必是最佳良药\n中国人喜欢听相声，因为它逗笑。“笑有益于健康”几乎得到了全世界的认可，“笑一笑十年少”“一笑解千愁”不仅被大家认可，甚至被一些人当作生活的座右铭。",
     "Phần hai: Cười chưa chắc đã là liều thuốc tốt nhất. — Người Trung Quốc thích nghe tấu nói vì nó gây cười. Quan niệm cười có lợi cho sức khỏe gần như được cả thế giới công nhận; những câu như cười một cái trẻ ra mười tuổi, một nụ cười giải nghìn nỗi sầu không những được mọi người tán đồng, mà thậm chí còn được một số người coi là châm ngôn sống.",
     ["未必 là chưa chắc. 逗笑 là chọc cười. Cấu trúc 不仅……甚至…… là không những… mà thậm chí….",
      "笑一笑十年少 là cười một cái trẻ ra mười tuổi, chữ 少 ở đây đọc là shào, nghĩa là trẻ. 一笑解千愁 là một nụ cười xua tan nghìn nỗi sầu."],
     "二，笑未必是最佳良药。中国人喜欢听相声，因为它逗笑。笑有益于健康，几乎得到了全世界的认可，笑一笑十年少，一笑解千愁，不仅被大家认可，甚至被一些人当作生活的座右铭。"),
    ("中国人深信开怀大笑也好，哈哈傻笑也罢，哪怕是私下里偷偷地笑，都会是生活中最通用，而且管用的治病良方。",
     "Người Trung Quốc tin chắc rằng, cười sảng khoái cũng được, cười ngây ngô ha ha cũng được, thậm chí là lén lút cười một mình, thì đều là phương thuốc chữa bệnh thông dụng nhất, mà lại hiệu nghiệm trong cuộc sống.",
     ["Đây là điểm ngữ pháp thứ hai: 也好，也罢, nghĩa là dù cười kiểu nào thì kết quả cũng vậy. Vế sau có chữ 都 đi kèm.",
      "开怀大笑 là cười sảng khoái. 哪怕 là dù cho, thậm chí. 管用 là hiệu nghiệm, có tác dụng, là khẩu ngữ. 良方 là phương thuốc hay."]),
    ("有研究证实，笑可以调节情绪，可以促进血液循环和腹肌收缩，100次捧腹大笑所吸收的氧气相当于用桨划船10分钟的吸氧量。",
     "Có nghiên cứu chứng thực rằng, cười có thể điều tiết cảm xúc, có thể thúc đẩy tuần hoàn máu và sự co bóp của cơ bụng; lượng oxy hấp thụ khi cười ôm bụng một trăm lần tương đương với lượng oxy hấp thụ khi dùng mái chèo chèo thuyền mười phút.",
     ["Ba từ mới liền nhau: 调节, điều tiết; 循环, tuần hoàn; 收缩, co lại. 腹肌 là cơ bụng.",
      "捧腹大笑 là cười ôm bụng. 相当于 là tương đương với. 吸氧量 là lượng oxy hấp thụ."],
     "有研究证实，笑可以调节情绪，可以促进血液循环和腹肌收缩，一百次捧腹大笑所吸收的氧气相当于用桨划船十分钟的吸氧量。"),
    ("有人做过这样的试验，开怀大笑一整天，可以燃烧掉2000卡路里，从而帮助消耗脂肪，减轻体重，同时，笑有助于缓解动脉硬化，有助于消除紧张感，这就是笑有利于健康的实质性的证据。",
     "Có người từng làm thử nghiệm thế này: cười sảng khoái suốt một ngày có thể đốt cháy hai nghìn ca-lo, từ đó giúp tiêu hao mỡ, giảm cân; đồng thời, cười giúp làm dịu chứng xơ cứng động mạch, giúp xóa tan cảm giác căng thẳng. Đây chính là bằng chứng thực chất cho thấy cười có lợi cho sức khỏe.",
     ["卡路里 là ca-lo, đơn vị đo nhiệt lượng; sách có chú thích cuối trang, gọi tắt là 卡. 燃烧掉 là đốt cháy hết.",
      "有助于 là có ích cho, giúp. 有利于 là có lợi cho. 缓解 là làm dịu, giảm nhẹ. 动脉硬化 là xơ cứng động mạch."],
     "有人做过这样的试验，开怀大笑一整天，可以燃烧掉两千卡路里，从而帮助消耗脂肪，减轻体重，同时，笑有助于缓解动脉硬化，有助于消除紧张感，这就是笑有利于健康的实质性的证据。"),
    ("然而，笑，真的是人生旅途中的最佳良药吗？答案似乎不是那么肯定。有研究人员表示，笑也不是有百益而无一害的，有时它还会产生副作用。",
     "Thế nhưng, cười có thật sự là liều thuốc tốt nhất trên hành trình cuộc đời không? Câu trả lời dường như không chắc chắn đến thế. Có nhà nghiên cứu cho biết, cười cũng không phải là trăm điều lợi mà không một điều hại, đôi khi nó còn gây ra tác dụng phụ.",
     ["Một lần nữa tác giả dùng 设问: tự đặt câu hỏi rồi tự trả lời, để chuyển từ mặt lợi sang mặt hại của tiếng cười một cách tự nhiên.",
      "然而 là thế nhưng. 有百益而无一害 là trăm lợi mà không một hại. 副作用 là tác dụng phụ."]),
    ("有医生就碰到过这样的案例：有人在肆无忌惮地笑过后因心跳加速而昏迷，而大笑到“几乎笑破肚皮”可能会导致岔气，心脏不舒服，甚至损坏人体健康。",
     "Có bác sĩ đã gặp trường hợp như thế này: có người sau khi cười thả cửa không kiêng nể gì đã bị hôn mê vì tim đập nhanh; còn cười đến mức gần như vỡ bụng có thể dẫn đến sóc hông, tim khó chịu, thậm chí làm tổn hại sức khỏe.",
     ["因……而…… là vì… mà…: 因心跳加速而昏迷, vì tim đập nhanh mà hôn mê. 案例 là trường hợp, ca bệnh.",
      "笑破肚皮 là cười vỡ bụng, một cách nói phóng đại. 岔气 là sóc hông, đau nhói ở mạn sườn khi thở."]),
    ("新的研究结果对笑“有百益而无一害”的观点提出了挑战，似乎更倾向于笑不是坏事，但分寸要掌握得恰到好处。",
     "Kết quả nghiên cứu mới đã đặt ra thách thức đối với quan điểm cười trăm lợi không một hại; dường như nó nghiêng về ý kiến cho rằng cười không phải chuyện xấu, nhưng phải giữ chừng mực cho thật vừa phải.",
     ["对……提出了挑战 là đặt ra thách thức đối với…. 倾向于 là nghiêng về.",
      "分寸要掌握得恰到好处 là phải nắm chừng mực cho thật vừa đúng, đây là câu chốt của phần hai và trả lời câu hỏi: cười thế nào mới tốt cho sức khỏe."]),
    ("可是多数人还是深信，笑的是非无须探讨，任何形式的幽默，伤害风险都不高，其收益则是显而易见的，况且，真是好朋友在一起，高兴了，起起哄，或是遇到了开心事，哪里还顾得上斟酌分寸掌握得恰当不恰当呢？",
     "Thế nhưng phần lớn mọi người vẫn tin chắc rằng, chuyện đúng sai của tiếng cười không cần bàn, mọi hình thức hài hước đều có rủi ro gây hại không cao, còn lợi ích thì rõ ràng dễ thấy. Huống hồ, khi bạn thân ở bên nhau, vui lên thì trêu đùa ồn ào, hoặc gặp chuyện vui, thì còn hơi đâu mà cân nhắc chừng mực có vừa phải hay không?",
     ["无须 là không cần. 其收益 là lợi ích của nó; 其 là đại từ văn viết. 显而易见 là rõ ràng dễ thấy. 况且 là huống hồ, hơn nữa.",
      "哪里还顾得上……呢 là câu hỏi tu từ: còn hơi đâu mà…, tức là chẳng ai để ý được. Bài văn kết thúc bằng một câu hỏi để người đọc tự suy ngẫm."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa “笑”的备忘录",
    items=["Gồm hai bài văn ngắn: (一) 大脑能“听”出笑声的真假 · (二) 笑未必是最佳良药",
           "Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 笑的备忘录, dài một nghìn một trăm năm mươi tư chữ.",
         F(0, "Bài khóa gồm hai bài văn ngắn. Bài thứ nhất: 大脑能听出笑声的真假, não bộ có thể nghe ra tiếng cười thật hay giả. Bài thứ hai: 笑未必是最佳良药, cười chưa chắc đã là liều thuốc tốt nhất."),
         F(1, "Thầy chia bài thành từng đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(2, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(3, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 100 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi, cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Tóm tắt nội dung", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5)", size=36,
    items=["## (一) 大脑能“听”出笑声的真假",
           "Đừng cười giả cho qua: dù che đậy kỹ đến đâu, người khác vẫn nhận ra",
           "Cười giả kích hoạt vùng giải mã cảm xúc · cười thật kích hoạt vùng niềm vui",
           "Thí nghiệm: chỉ bằng trực giác vẫn phân biệt được cười giả – não rất nhạy cảm",
           "## (二) 笑未必是最佳良药",
           "Lợi: điều tiết cảm xúc, tuần hoàn máu, đốt 2000 ca-lo, giảm căng thẳng",
           "Hại: hôn mê vì tim đập nhanh, sóc hông, tim khó chịu",
           "Kết: cười cần có chừng mực – nhưng bạn bè vui vẻ thì ai còn cân nhắc?"],
    say=["Chúng ta cùng nhìn lại bố cục của cả bài khóa, theo gợi ý ở bài tập năm trong sách.",
         F(0, "Bài văn thứ nhất: 大脑能听出笑声的真假, não bộ có thể nghe ra tiếng cười thật hay giả."),
         F(1, "Ý một: đừng cười giả để đối phó, vì dù bạn lanh lợi, che đậy kỹ đến đâu, người khác vẫn nhận ra."),
         F(2, "Ý hai: tiếng cười giả kích hoạt vùng não giải mã cảm xúc, còn tiếng cười thật kích hoạt vùng não liên quan đến niềm vui."),
         F(3, "Ý ba: thí nghiệm cho thấy tình nguyện viên chỉ dựa vào trực giác cũng phân biệt được cười giả, vì não người rất nhạy cảm với thông tin ẩn trong tiếng cười."),
         F(4, "Bài văn thứ hai: 笑未必是最佳良药, cười chưa chắc đã là liều thuốc tốt nhất."),
         F(5, "Mặt lợi: cười điều tiết cảm xúc, thúc đẩy tuần hoàn máu, cười cả ngày đốt được hai nghìn ca-lo, giúp giảm căng thẳng."),
         F(6, "Mặt hại: có người cười thả cửa rồi hôn mê vì tim đập nhanh, cười quá có thể bị sóc hông, tim khó chịu."),
         F(7, "Kết luận: cười cần giữ chừng mực cho vừa phải; nhưng khi bạn bè vui vẻ bên nhau, ai còn để ý đến điều đó? Bố cục này rất có ích khi các bạn làm bài tập viết tóm tắt ở cuối bài.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 预先", section="Ngữ pháp 注释", title="1. 预先 yùxiān – trước, sẵn từ trước", size=38,
    items=["Phó từ: hành động được làm trước khi sự việc xảy ra hoặc động tác tiến hành",
           "Cấu trúc: 预先 + động từ · phủ định: 预先没(有)… / 预先未…",
           "(1) 那里一年四季都是旅游旺季，到那里去旅行，一定要预先订好旅馆。",
           "(2) 大家预先都没有想到，本届绘画展览竟然这么受欢迎。",
           "(3) 志愿者在预先未被告知测试目的的情况下，仅凭直觉就能准确地分辨出假笑声。",
           "Gần nghĩa: 事先 · 提前"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là phó từ 预先.",
         F(0, "预先 là phó từ, có nghĩa là một hành động nào đó đã được làm trước khi sự việc xảy ra, hoặc trước khi động tác tiến hành. Tiếng Việt dịch là trước, sẵn từ trước."),
         F(1, "Cấu trúc: 预先 đứng trước động từ. Dạng phủ định là 预先没有, hoặc trong văn viết là 预先未."),
         F(2, "Ví dụ một: 那里一年四季都是旅游旺季，到那里去旅行，一定要预先订好旅馆。 Ở đó quanh năm đều là mùa du lịch cao điểm, đến đó du lịch nhất định phải đặt khách sạn trước."),
         F(3, "Ví dụ hai: 大家预先都没有想到，本届绘画展览竟然这么受欢迎。 Trước đó không ai ngờ rằng triển lãm hội họa lần này lại được hoan nghênh đến thế."),
         F(4, "Ví dụ ba, lấy từ bài khóa: 志愿者在预先未被告知测试目的的情况下，仅凭直觉就能准确地分辨出假笑声。 Các tình nguyện viên, dù không được cho biết trước mục đích thử nghiệm, chỉ dựa vào trực giác đã phân biệt chính xác được tiếng cười giả."),
         F(5, "预先 gần nghĩa với 事先 và 提前. Các bạn có thể thay qua lại trong nhiều trường hợp, ví dụ 预先订好旅馆, 事先订好旅馆, hay 提前订好旅馆 đều được.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: dùng 预先 hoàn thành câu", reveal=True, size=36,
    items=["(1) 这事她________，我最近都忙糊涂了，忘了告诉你了。",
           "Đáp án: 这事她预先跟我打过招呼……",
           "(2) 他________的是，居然有那么多朋友，在他最困难的时候向他伸出了援手。",
           "Đáp án: 他预先没有想到的是……",
           "(3) ……送公文的到了，吃饱喝足，稍稍休息一下，换一匹________，继续赶路。",
           "Đáp án: ……换一匹预先准备好的马，继续赶路。"],
    say=[F(0, "Luyện tập. Câu một: 这事她，chỗ trống，我最近都忙糊涂了，忘了告诉你了。 Chuyện này cô ấy đã làm gì đó từ trước, dạo này tôi bận đến lú lẫn, quên mất không nói với bạn. Các bạn hãy tạm dừng và thử hoàn thành câu."),
         F(1, "Đáp án gợi ý: 这事她预先跟我打过招呼。 Chuyện này cô ấy đã báo trước với tôi rồi."),
         F(2, "Câu hai: 他，chỗ trống，的是，居然有那么多朋友，在他最困难的时候向他伸出了援手。 Điều mà anh ấy không ngờ tới là có nhiều bạn bè đến thế đã chìa tay giúp đỡ lúc anh khó khăn nhất."),
         F(3, "Đáp án gợi ý: 他预先没有想到的是。 Điều anh ấy không hề lường trước được là…"),
         F(4, "Câu ba kể chuyện người đưa công văn thời xưa cưỡi ngựa, đến mỗi trạm thì ăn uống no nê, nghỉ một chút, rồi 换一匹，chỗ trống，继续赶路。 Đổi một con ngựa như thế nào để tiếp tục lên đường?"),
         F(5, "Đáp án gợi ý: 换一匹预先准备好的马，继续赶路。 Đổi một con ngựa đã chuẩn bị sẵn từ trước rồi tiếp tục lên đường.")])

add("bullets", chapter="Ngữ pháp: ……也好，……也罢", section="Ngữ pháp 注释", title="2. ……也好，……也罢 – … cũng được, … cũng vậy", size=36,
    items=["Dùng để liệt kê: trong bất kỳ trường hợp nào cũng đều như vậy",
           "Các dạng: A也好，B也罢 · A也好，B也好 · A也罢，B也罢 – vế sau thường có 都 / 也",
           "(1) 中国人深信开怀大笑也好，哈哈傻笑也罢，哪怕是私下里偷偷地笑，都会是生活中最通用，而且管用的治病良方。",
           "(2) 退休以后别人都养养花，喂喂鸟，可是花也好，鸟也好，都引不起他的兴趣。",
           "(3) 开汽车也罢，骑自行车也罢，行进中打电话都会影响注意力与反应能力。"],
    say=["Điểm ngữ pháp thứ hai là cấu trúc 也好，也罢.",
         F(0, "Cấu trúc này dùng để liệt kê các trường hợp, và nhấn mạnh rằng trong bất kỳ trường hợp nào thì kết quả cũng đều như vậy. Tiếng Việt có thể dịch là: A cũng được, B cũng được, đều…."),
         F(1, "Có ba dạng: 也好 đi với 也罢; 也好 đi với 也好; hoặc 也罢 đi với 也罢. Vế sau thường có chữ 都 hoặc 也 đi kèm."),
         F(2, "Ví dụ một, lấy từ bài khóa: 中国人深信开怀大笑也好，哈哈傻笑也罢，哪怕是私下里偷偷地笑，都会是生活中最通用，而且管用的治病良方。 Cười sảng khoái hay cười ngây ngô, kể cả cười lén, đều là phương thuốc hay."),
         F(3, "Ví dụ hai: 退休以后别人都养养花，喂喂鸟，可是花也好，鸟也好，都引不起他的兴趣。 Nghỉ hưu rồi người khác đều trồng hoa, nuôi chim, nhưng hoa cũng thế, chim cũng thế, đều không khơi được hứng thú của ông ấy."),
         F(4, "Ví dụ ba: 开汽车也罢，骑自行车也罢，行进中打电话都会影响注意力与反应能力。 Lái ô tô cũng vậy, đi xe đạp cũng vậy, vừa đi vừa gọi điện thoại đều ảnh hưởng đến sự tập trung và khả năng phản ứng.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: viết lại câu với ……也好，……也罢", reveal=True, size=36,
    items=["(1) 是上学还是工作，只要你自己愿意就行。",
           "Đáp án: 上学也好，工作也罢，只要你自己愿意就行。",
           "(2) 考试已经完了，考得好不好，再想也没用了。",
           "Đáp án: 考试已经完了，考得好也罢，考得不好也罢，再想也没用了。",
           "(3) 不管明天是什么天气，刮风或者下雨，都不能影响我们六点准时出发。",
           "Đáp án: 明天刮风也好，下雨也好，都不能影响我们六点准时出发。"],
    say=[F(0, "Luyện tập: viết lại câu bằng cấu trúc 也好，也罢. Câu một: 是上学还是工作，只要你自己愿意就行。 Đi học hay đi làm, chỉ cần bản thân con muốn là được. Các bạn tạm dừng và thử viết lại nhé."),
         F(1, "Đáp án: 上学也好，工作也罢，只要你自己愿意就行。 Đi học cũng được, đi làm cũng được, miễn là con muốn."),
         F(2, "Câu hai: 考试已经完了，考得好不好，再想也没用了。 Thi xong rồi, làm bài tốt hay không, nghĩ nữa cũng vô ích."),
         F(3, "Đáp án: 考得好也罢，考得不好也罢，再想也没用了。 Thi tốt cũng thế, thi không tốt cũng thế, nghĩ nữa cũng chẳng ích gì."),
         F(4, "Câu ba: 不管明天是什么天气，刮风或者下雨，都不能影响我们六点准时出发。 Dù ngày mai thời tiết thế nào, gió hay mưa, cũng không ảnh hưởng đến việc chúng ta xuất phát đúng sáu giờ."),
         F(5, "Đáp án: 明天刮风也好，下雨也好，都不能影响我们六点准时出发。 Mai gió cũng được, mưa cũng được, đều không cản được chúng ta xuất phát đúng giờ.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 诸 – 各", section="Phân biệt từ 词语辨析", title="Phân biệt 诸 và 各 (1)",
    common="Giống nhau: trong 诸位 và 各位, nghĩa và cách dùng như nhau. Ví dụ: 诸位/各位有何意见，请尽量发表。",
    cols=[{"head": "诸",
           "lines": ["(1) Văn viết, nghĩa là nhiều, các; danh từ hoặc lượng từ theo sau thường chỉ người; thường là kết cấu cố định",
                     "Ví dụ: 诸位 · 诸君 · 诸侯 · 诸子百家"]},
          {"head": "各",
           "lines": ["(1) Chỉ mọi cá thể trong một phạm vi, không chỉ người mà còn chỉ cả sự vật",
                     "Ví dụ: 各位 · 各方 · 各界 · 各国"]}],
    say=["Tiếp theo là phần phân biệt từ: 诸 và 各. Hai chữ này đều có nghĩa là các, nên người học hay dùng lẫn.",
         "Điểm giống nhau: trong hai từ xưng hô 诸位 và 各位, nghĩa và cách dùng hoàn toàn như nhau. Ví dụ: 诸位有何意见，请尽量发表, hoặc 各位有何意见，请尽量发表。 Quý vị có ý kiến gì, xin cứ phát biểu.",
         F(0, "Điểm khác thứ nhất. 诸 là văn viết, nghĩa là nhiều, các. Danh từ hay lượng từ theo sau nó thường chỉ người, và thường là những kết cấu cố định."),
         F(0, "Ví dụ: 诸位, các vị; 诸君, các ông; 诸侯, chư hầu; 诸子百家, bách gia chư tử, tức các trường phái tư tưởng thời Tiên Tần."),
         F(1, "Còn 各 chỉ mọi cá thể trong một phạm vi nào đó, không chỉ người mà còn có thể chỉ cả sự vật."),
         F(1, "Ví dụ: 各位, các vị; 各方, các bên; 各界, các giới; 各国, các nước.")])

add("compare", section="Phân biệt từ 词语辨析", title="Phân biệt 诸 và 各 (2)",
    cols=[{"head": "诸",
           "lines": ["(2) Không có cách dùng này",
                     "Sai: 双方诸执一词。",
                     "(3) Không đứng trước động từ",
                     "Sai: 他们诸想了一个办法。"]},
          {"head": "各",
           "lines": ["(2) Chỉ mỗi người làm việc gì, mỗi vật có thuộc tính gì",
                     "Đúng: 双方各执一词。",
                     "Đúng: 院子前后各有一门。",
                     "(3) Làm phó từ trước động từ: riêng từng, mỗi",
                     "Đúng: 几种水果他各买了一斤。",
                     "Đúng: 他们各想了一个办法。"]}],
    say=[F(1, "Điểm khác thứ hai. 各 có thể biểu thị không chỉ một người làm việc gì đó, hoặc không chỉ một vật có thuộc tính nào đó, tức là mỗi người, mỗi vật đều như vậy."),
         F(1, "Ví dụ: 双方各执一词。 Hai bên mỗi bên giữ một ý. Và 院子前后各有一门。 Trước và sau sân mỗi bên có một cái cổng."),
         F(0, "诸 không có cách dùng này. Không thể nói 双方诸执一词."),
         F(1, "Điểm khác thứ ba. 各 có thể làm phó từ, đứng trước động từ, nghĩa là riêng từng, mỗi. Ví dụ: 几种水果他各买了一斤。 Mấy loại hoa quả, mỗi loại anh ấy mua một cân. Và 他们各想了一个办法。 Mỗi người bọn họ nghĩ ra một cách."),
         F(0, "Còn 诸 không thể đứng trước động từ. Câu 他们诸想了一个办法 là sai."),
         "Mẹo nhớ: 诸 gần như chỉ còn sống trong mấy từ cố định, trang trọng như 诸位，诸君，诸侯，诸子百家; còn 各 dùng rộng rãi hơn rất nhiều, đi với người, với vật, và cả trước động từ."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: Đúng hay sai?", reveal=True, size=38,
    items=["(1) 亚洲各国首脑都参加了此次会议。",
           "Đáp án: Đúng – 各 đi với sự vật (国): các nước.",
           "(2) 经过诸方的共同努力，事情终于圆满解决了。",
           "Đáp án: Sai – 诸 chỉ dùng trong kết cấu cố định. Sửa: 经过各方的共同努力……",
           "(3) 三种办法各有优点和缺点，实在难以抉择。",
           "Đáp án: Đúng – 各 chỉ mỗi vật có thuộc tính gì.",
           "(4) 他喜欢读古代诸子百家的著作。",
           "Đáp án: Đúng – 诸子百家 là kết cấu cố định."],
    say=[F(0, "Bây giờ chúng ta làm thử: đúng hay sai? Câu một: 亚洲各国首脑都参加了此次会议。 Người đứng đầu các nước châu Á đều tham dự hội nghị lần này. Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: đúng. 各 có thể đi với sự vật, 各国 là các nước."),
         F(2, "Câu hai: 经过诸方的共同努力，事情终于圆满解决了。 Nhờ sự nỗ lực chung của các bên, sự việc cuối cùng đã được giải quyết trọn vẹn."),
         F(3, "Đáp án: sai. 诸 chỉ dùng trong một số kết cấu cố định, không nói 诸方. Phải sửa thành 经过各方的共同努力."),
         F(4, "Câu ba: 三种办法各有优点和缺点，实在难以抉择。 Ba cách, mỗi cách đều có ưu điểm và nhược điểm, thật khó mà lựa chọn."),
         F(5, "Đáp án: đúng. Đây là cách dùng thứ hai của 各: mỗi vật đều có thuộc tính nào đó."),
         F(6, "Câu bốn: 他喜欢读古代诸子百家的著作。 Anh ấy thích đọc tác phẩm của bách gia chư tử thời cổ đại."),
         F(7, "Đáp án: đúng. 诸子百家 là kết cấu cố định, dùng 诸 là chuẩn.")])

# ======================= TU TỪ =======================
add("bullets", chapter="Tu từ: 设问", section="Tu từ 篇章修辞", title="Tu từ (6): 设问 – tự hỏi tự đáp", size=36,
    items=["Không có gì nghi ngờ mà vẫn hỏi, rồi tự mình trả lời",
           "Tác dụng 1: gây chú ý, gợi cho người đọc suy nghĩ",
           "Tác dụng 2: tiện tổ chức bài văn, giúp chuyển ý tự nhiên, gọn gàng",
           "(1) 难道我们听到庸俗、不上档次的笑话假笑两声、敷衍一下也不可以吗？可是，好像确实不行。",
           "(2) 笑，真的是人生旅途中的最佳良药吗？答案似乎不是那么肯定。",
           "(3) 离开了手机，难道会死吗？何不尝试一下一周关机一天？说干就干，索性这礼拜就开始。",
           "Phân biệt: 设问 có câu trả lời ngay sau · 反问 không cần trả lời"],
    say=["Phần cuối cùng về lý thuyết là thủ pháp tu từ số sáu: 设问.",
         F(0, "设问 là không có gì nghi ngờ mà vẫn đặt câu hỏi, rồi tự mình trả lời. Nói gọn là tự hỏi tự đáp."),
         F(1, "Tác dụng thứ nhất: gây sự chú ý của người đọc, gợi cho họ suy nghĩ."),
         F(2, "Tác dụng thứ hai: tiện cho việc tổ chức bài văn, giúp chuyển ý một cách tự nhiên và gọn gàng."),
         F(3, "Ví dụ một, câu mở đầu bài khóa: 难道我们听到庸俗、不上档次的笑话假笑两声、敷衍一下也不可以吗？可是，好像确实不行。 Tác giả hỏi, rồi tự trả lời ngay: hình như đúng là không được."),
         F(4, "Ví dụ hai: 笑，真的是人生旅途中的最佳良药吗？答案似乎不是那么肯定。 Câu này nằm ở giữa bài văn thứ hai. Nhờ nó, bài văn chuyển từ mặt lợi sang mặt hại của tiếng cười rất tự nhiên, gọn gàng."),
         F(5, "Ví dụ ba: 离开了手机，难道会死吗？何不尝试一下一周关机一天？说干就干，索性这礼拜就开始。 Rời xa điện thoại thì chết được sao? Sao không thử mỗi tuần tắt máy một ngày? Nói là làm, tuần này bắt đầu luôn."),
         F(6, "Các bạn chú ý phân biệt: 设问 là hỏi rồi có câu trả lời ngay sau đó; còn 反问, câu hỏi tu từ, thì đáp án đã nằm sẵn trong câu hỏi, không cần trả lời.")])

add("bullets", section="Tu từ 篇章修辞", title="Luyện tập: viết lại thành câu 设问", reveal=True, size=38,
    items=["(1) 有钱不一定幸福，有朋友，有健康，有自己的事业才会幸福。",
           "Đáp án: 有钱就一定幸福吗？不一定。有朋友，有健康，有自己的事业才会幸福。",
           "(2) 气候真的变暖了，没错，我们的地球每一天都在变化。",
           "Đáp án: 气候真的变暖了吗？没错，我们的地球每一天都在变化。",
           "(3) 奋斗的人生是最美好的，因为奋斗之中快乐无穷。",
           "Đáp án: 什么样的人生是最美好的？是奋斗的人生，因为奋斗之中快乐无穷。"],
    say=[F(0, "Luyện tập: viết lại các câu sau thành câu 设问. Câu một: 有钱不一定幸福，有朋友，有健康，有自己的事业才会幸福。 Có tiền chưa chắc đã hạnh phúc, có bạn bè, có sức khỏe, có sự nghiệp riêng mới hạnh phúc. Các bạn thử nhé."),
         F(1, "Đáp án gợi ý: 有钱就一定幸福吗？不一定。 Có tiền thì nhất định hạnh phúc sao? Chưa chắc. Rồi tiếp: 有朋友，有健康，有自己的事业才会幸福。"),
         F(2, "Câu hai: 气候真的变暖了，没错，我们的地球每一天都在变化。 Khí hậu thật sự đã ấm lên, đúng vậy, trái đất của chúng ta mỗi ngày đều đang thay đổi."),
         F(3, "Đáp án: chỉ cần biến vế đầu thành câu hỏi: 气候真的变暖了吗？没错，我们的地球每一天都在变化。 Khí hậu thật sự đã ấm lên rồi sao? Đúng vậy."),
         F(4, "Câu ba: 奋斗的人生是最美好的，因为奋斗之中快乐无穷。 Cuộc đời phấn đấu là đẹp nhất, vì trong phấn đấu có niềm vui vô tận."),
         F(5, "Đáp án gợi ý: 什么样的人生是最美好的？是奋斗的人生，因为奋斗之中快乐无穷。 Cuộc đời như thế nào là đẹp nhất? Là cuộc đời phấn đấu.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ gốc", size=40,
    items=["实质 → 本质 · 性质 · 品质 · 素质",
           "档次 → 档案 · 高档 · 存档 · 搭档",
           "回避 → 避免 · 躲避 · 逃避 · 避难",
           "周密 → 周到 · 周全 · 周围 · 四周",
           "提炼 → 提高 · 提取 · 提升 · 提倡"],
    say=["Phần luyện tập. Bài tập một: bắt chước ví dụ, dựa vào chữ được đánh dấu chấm, hãy viết thêm các từ khác.",
         F(0, "Ví dụ mẫu: 实质, lấy chữ 质, có 本质，性质，品质，素质. Tức là bản chất, tính chất, phẩm chất, và tố chất."),
         F(1, "档次, lấy chữ 档, có 档案，高档，存档，搭档. Tức là hồ sơ, cao cấp, lưu trữ, và bạn cùng cặp, đối tác."),
         F(2, "回避, lấy chữ 避, có 避免，躲避，逃避，避难. Tức là tránh, trốn tránh, chạy trốn, và lánh nạn."),
         F(3, "周密, lấy chữ 周, có 周到，周全，周围，四周. Tức là chu đáo, chu toàn, xung quanh, và bốn phía."),
         F(4, "提炼, lấy chữ 提, có 提高，提取，提升，提倡. Tức là nâng cao, rút ra, đề bạt hay nâng lên, và đề xướng. Các bạn có thể tìm thêm nhiều từ khác nữa nhé.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (1)", reveal=True, size=36,
    items=["(1) 付出艰苦努力的人什么都没得到，哪有这样的道理啊？（岂有此理）",
           "Đáp án: 付出艰苦努力的人什么都没得到，真是岂有此理！",
           "(2) 我已经提前做好了计划，所以实施起来很顺利。（预先）",
           "Đáp án: 我已经预先做好了计划，所以实施起来很顺利。",
           "(3) 无论富贵还是贫穷，我对他的爱不会改变。（……也好，……也罢）",
           "Đáp án: 富贵也好，贫穷也罢，我对他的爱都不会改变。"],
    say=[F(0, "Bài tập hai: viết lại câu bằng từ hoặc cấu trúc cho sẵn. Câu một, dùng 岂有此理: 付出艰苦努力的人什么都没得到，哪有这样的道理啊？"),
         F(1, "Đáp án: thay câu hỏi 哪有这样的道理啊 bằng 真是岂有此理: 付出艰苦努力的人什么都没得到，真是岂有此理！ Người bỏ ra bao công sức mà chẳng được gì, thật là vô lý hết sức!"),
         F(2, "Câu hai, dùng 预先: 我已经提前做好了计划，所以实施起来很顺利。"),
         F(3, "Đáp án: thay 提前 bằng 预先: 我已经预先做好了计划，所以实施起来很顺利。 Tôi đã lập sẵn kế hoạch từ trước, nên thực hiện rất suôn sẻ."),
         F(4, "Câu ba, dùng 也好，也罢: 无论富贵还是贫穷，我对他的爱不会改变。"),
         F(5, "Đáp án: 富贵也好，贫穷也罢，我对他的爱都不会改变。 Giàu sang cũng thế, nghèo khó cũng thế, tình yêu của tôi dành cho anh ấy đều không thay đổi. Nhớ thêm chữ 都 ở vế sau nhé.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (2)", reveal=True, size=36,
    items=["(4) “米”是国际上普遍使用的基本长度单位。（通用）",
           "Đáp án: “米”是国际上通用的基本长度单位。",
           "(5) 问题的本质在于某些人缺乏责任心。（实质）",
           "Đáp án: 问题的实质在于某些人缺乏责任心。",
           "(6) 明天的会议很重要，发言稿你好好考虑考虑。（斟酌）",
           "Đáp án: 明天的会议很重要，发言稿你好好斟酌斟酌。"],
    say=[F(0, "Câu bốn, dùng 通用: 米是国际上普遍使用的基本长度单位。"),
         F(1, "Đáp án: thay 普遍使用 bằng 通用: 米是国际上通用的基本长度单位。 Mét là đơn vị đo chiều dài cơ bản được dùng chung trên thế giới."),
         F(2, "Câu năm, dùng 实质: 问题的本质在于某些人缺乏责任心。"),
         F(3, "Đáp án: thay 本质 bằng 实质: 问题的实质在于某些人缺乏责任心。 Thực chất của vấn đề nằm ở chỗ một số người thiếu tinh thần trách nhiệm."),
         F(4, "Câu sáu, dùng 斟酌: 明天的会议很重要，发言稿你好好考虑考虑。"),
         F(5, "Đáp án: thay 考虑考虑 bằng 斟酌斟酌: 发言稿你好好斟酌斟酌。 Bài phát biểu, anh hãy cân nhắc thật kỹ. Động từ hai âm tiết lặp lại theo kiểu ABAB, giống 考虑考虑.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ điền vào chỗ trống (1)", reveal=True, size=36,
    items=["Từ cho sẵn: 损坏 · 循环 · 脂肪 · 收缩 · 动脉",
           "心脏每时每刻都在跳动，有规律地(1)____和舒张，这可以使血液在体内不断(2)____，因此心脏的重要性不言而喻。而肥胖会导致(3)____硬化，(4)____心脏机能。所以减轻体重，减少(5)____含量是保护心脏重要的一步。",
           "Đáp án: (1) 收缩 · (2) 循环 · (3) 动脉 · (4) 损坏 · (5) 脂肪"],
    say=[F(0, "Thầy làm thêm bài tập ba để ôn từ mới: chọn từ thích hợp điền vào chỗ trống. Đoạn thứ nhất dùng các từ: 损坏，循环，脂肪，收缩，动脉."),
         F(1, "Đoạn văn nói về tim: tim đập từng giây từng phút, co và giãn có quy luật, làm cho máu lưu thông liên tục trong cơ thể. Còn béo phì sẽ gây xơ cứng động mạch, làm tổn hại chức năng tim. Vì vậy giảm cân, giảm lượng mỡ là bước quan trọng để bảo vệ tim. Các bạn tạm dừng và thử điền nhé."),
         F(2, "Đáp án: chỗ một là 收缩, vì đi đôi với 舒张; chỗ hai là 循环, 血液循环; chỗ ba là 动脉, 动脉硬化; chỗ bốn là 损坏, 损坏心脏机能; chỗ năm là 脂肪, 脂肪含量.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ điền vào chỗ trống (2)", reveal=True, size=36,
    items=["Từ cho sẵn: 恰当 · 周密 · 意向 · 收益 · 一丝不苟",
           "新产品面世以前，一般要先调查消费者的购买(1)____，然后经过(2)____的设计，(3)____的生产过程，再找一个(4)____的时机投放到市场，才能获得可观的(5)____。",
           "Đáp án: (1) 意向 · (2) 周密 · (3) 一丝不苟 · (4) 恰当 · (5) 收益"],
    say=[F(0, "Đoạn thứ hai dùng các từ: 恰当，周密，意向，收益，一丝不苟."),
         F(1, "Đoạn văn nói: trước khi sản phẩm mới ra mắt, thường phải điều tra nhu cầu mua của người tiêu dùng, rồi qua khâu thiết kế, khâu sản xuất, tìm thời điểm đưa ra thị trường, mới thu được lợi nhuận đáng kể. Các bạn thử điền nhé."),
         F(2, "Đáp án: chỗ một là 意向, 购买意向, ý định mua; chỗ hai là 周密, thiết kế chu đáo; chỗ ba là 一丝不苟, quá trình sản xuất cẩn thận tỉ mỉ; chỗ bốn là 恰当, thời cơ thích hợp; chỗ năm là 收益, 可观的收益, lợi nhuận đáng kể.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 29", size=36,
    items=["Từ vựng trọng tâm: 岂有此理 · 画蛇添足 · 一丝不苟 · 一目了然 · 肆无忌惮 · 恰到好处 · 分寸 · 斟酌",
           "Ngữ pháp: 预先 (làm sẵn từ trước) · ……也好，……也罢 (… cũng được, … cũng vậy, đều…)",
           "Phân biệt: 诸 (văn viết, kết cấu cố định, chỉ người) ≠ 各 (người và vật, đứng trước động từ được)",
           "Tu từ: 设问 – tự hỏi tự đáp, gây chú ý và chuyển ý tự nhiên",
           "## Bài tập về nhà",
           "Viết tóm tắt mỗi bài văn khoảng 200 chữ, dựa vào gợi ý của bài tập 5, dùng ít nhất một câu 设问",
           "Ôn các cặp từ gần nghĩa ở phần 扩展: 腐朽–腐败 · 烘–烤 · 焦点–中心 · 内幕–内情…"],
    say=["Chúng ta cùng tổng kết bài hai mươi chín.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ các thành ngữ: 岂有此理，画蛇添足，一丝不苟，一目了然，肆无忌惮，恰到好处, cùng hai từ 分寸 và 斟酌."),
         F(1, "Về ngữ pháp: 预先 nghĩa là làm sẵn từ trước, đứng trước động từ. Cấu trúc 也好，也罢 dùng để liệt kê, nhấn mạnh trường hợp nào cũng vậy, vế sau thường có 都."),
         F(2, "Về phân biệt từ: 诸 là văn viết, chủ yếu trong kết cấu cố định chỉ người; 各 dùng cho cả người lẫn vật, và có thể đứng trước động từ."),
         F(3, "Về tu từ: 设问 là tự hỏi tự đáp, giúp gây chú ý và chuyển ý tự nhiên."),
         F(5, "Bài tập về nhà: theo phần vận dụng trong sách, các bạn hãy viết tóm tắt mỗi bài văn thành một đoạn khoảng hai trăm chữ, dựa vào gợi ý của bài tập năm. Hãy thử dùng ít nhất một câu 设问 nhé."),
         F(6, "Ngoài ra, hãy ôn các cặp từ gần nghĩa ở phần mở rộng, như 腐朽 và 腐败, 烘 và 烤, 焦点 và 中心, 内幕 và 内情."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Hẹn gặp lại các bạn ở bài ba mươi: 你睡好了吗, Bạn ngủ có ngon không? Chúc các bạn học tốt, và nhớ cười thật nhiều, nhưng cười cho có chừng mực nhé!"])

lesson = {
    "title": "HSK 6 (Hạ) – Bài 29: “笑”的备忘录 (Bản ghi nhớ về tiếng cười)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thứ tự quan trọng: cụm dài trước)
    "tts_replace": {
        "相声": "象声",          # xiàngsheng, tránh đọc xiāng
        "起哄": "起讧",          # qǐhòng, tránh đọc hǒng/hōng
        "十年少": "十年绍",      # shào (trẻ), tránh đọc shǎo
        "当作": "荡作",          # dàngzuò
        "恰当": "恰荡",          # qiàdàng
        "尽量": "紧量",          # jǐnliàng
        "说干就干": "说赣就赣",  # gàn
    },
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai29.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
