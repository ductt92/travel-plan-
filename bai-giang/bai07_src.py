#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Thượng) – Bài 7 «我的人生我做主». Chạy để sinh bai07.json."""
import json
import os

TAG = "HSK 6 (Thượng) · Bài 7 · 我的人生我做主"
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
    zh="我的人生我做主", py="Wǒ de rénshēng wǒ zuò zhǔ",
    vi="Bài 7: Tôi làm chủ cuộc đời tôi",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Thượng.",
         "Hôm nay chúng ta học bài bảy: 我的人生我做主。 Nghĩa là: Tôi làm chủ cuộc đời tôi.",
         "Bài này thuộc Chủ đề hai, 不甘平庸, Không cam chịu tầm thường. Bài khóa kể về anh Tiểu Vương, một nhân viên kế toán chán công việc nhưng không dám đổi nghề, vì sợ chọn sai. Từ đó, tác giả bàn về một câu hỏi rất thiết thực: khả năng ra quyết định từ đâu mà có?",
         "Câu trả lời của bài rất đáng suy ngẫm: phán đoán chính xác đến từ kinh nghiệm, còn kinh nghiệm lại đến từ vô số lần phán đoán sai. Vậy nên, đừng sợ mắc lỗi, đừng sợ đi đường vòng."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài khóa: vì sao Tiểu Vương sợ chọn nghề, và khả năng ra quyết định từ đâu mà có",
           "Nắm vững 45 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: giới từ 于, động từ – liên từ 致使, động từ 并非",
           "Phân biệt 日益 và 越来越",
           "Mở rộng: câu sai do trật tự từ không đúng (语序不当) và các cặp từ gần nghĩa"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa: vì sao Tiểu Vương lo lắng, sợ chọn sai nghề, và theo tác giả, khả năng ra quyết định được hình thành như thế nào."),
         F(1, "Thứ hai, nắm vững bốn mươi lăm từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học ba điểm ngữ pháp: giới từ 于 trong văn viết; từ 致使, vừa là động từ vừa là liên từ, nghĩa là khiến cho, đến nỗi; và động từ 并非, nghĩa là hoàn toàn không phải."),
         F(3, "Thứ tư, phân biệt hai từ cùng nghĩa ngày càng: 日益 và 越来越."),
         F(4, "Thứ năm, phần mở rộng: nhận biết câu sai do trật tự từ không đúng, tiếng Trung gọi là 语序不当, và làm quen với mười bốn cặp từ gần nghĩa."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Câu hỏi khởi động: Khả năng ra quyết định từ đâu mà có?", size=38,
    items=["当你在为一件事情犹豫不决时，有的人却能很快就做出正确的决定。这种做决定的能力是怎么得来的呢？",
           "生下来就有的 – sinh ra đã có · 在学校里学习的 – học ở trường",
           "通过不断实践得到的 – có được nhờ không ngừng thực hành",
           "在不断失败中学习到的 – học được từ những lần thất bại",
           "在不确定中提升了决策能力 – nâng cao khả năng quyết định trong sự bất định",
           "性格不同造成的 – do tính cách khác nhau · 补充 – bổ sung: ……"],
    say=["Chúng ta bắt đầu bằng phần khởi động.",
         F(0, "当你在为一件事情犹豫不决时，有的人却能很快就做出正确的决定。这种做决定的能力是怎么得来的呢？ Khi bạn còn đang do dự chưa quyết được một việc, thì có người lại có thể nhanh chóng đưa ra quyết định đúng. Khả năng ra quyết định ấy từ đâu mà có? Sách yêu cầu các bạn chọn đáp án mình cho là đúng, hoặc tự bổ sung thêm."),
         F(1, "生下来就有的。 Sinh ra đã có. 在学校里学习的。 Học được ở trường."),
         F(2, "通过不断实践得到的。 Có được nhờ không ngừng thực hành."),
         F(3, "在不断失败中学习到的。 Học được từ những lần thất bại liên tiếp."),
         F(4, "在不确定中提升了决策能力。 Nâng cao khả năng quyết định trong những tình huống không chắc chắn. Từ 决策 là từ mới của bài hôm nay."),
         F(5, "性格不同造成的。 Do tính cách mỗi người khác nhau. Còn các bạn nghĩ sao? Hãy tạm dừng video và trả lời bằng tiếng Trung. Đọc xong bài khóa, các bạn sẽ thấy câu trả lời của tác giả.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 做 và 观", size=38,
    items=["## 做 (tố): làm, đảm nhận một vai trò",
           "做主 làm chủ · 做伴 làm bạn · 做客 làm khách · 做官 làm quan",
           "做人 cách làm người · 做东 làm chủ chi, đãi khách · 做演员 làm diễn viên",
           "## 观 (quan): cách nhìn, quan niệm",
           "悲观 bi quan · 乐观 lạc quan · 主观 chủ quan · 客观 khách quan",
           "人生观 nhân sinh quan · 世界观 thế giới quan · 历史观 sử quan · 观点 quan điểm · 观念 quan niệm"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo.",
         F(0, "Nhóm thứ nhất có chữ 做, Hán Việt là tố, nghĩa là làm, hoặc đảm nhận một vai trò nào đó."),
         F(1, "做主，做伴，做客，做官。 Tức là: làm chủ, làm bạn đồng hành, làm khách, làm quan. Từ 做主 chính là từ trong tên bài."),
         F(2, "做人，做东，做演员。 Tức là: cách làm người, làm chủ chi để mời khách, và làm diễn viên. 做东 là đứng ra đãi khách, ví dụ: 今天我做东, hôm nay tôi mời."),
         F(3, "Nhóm thứ hai có chữ Hán Việt là quan, như trong từ 观点, nghĩa là cách nhìn, quan niệm."),
         F(4, "悲观，乐观，主观，客观。 Tức là: bi quan, lạc quan, chủ quan, khách quan. Từ 悲观 xuất hiện nhiều lần trong bài khóa."),
         F(5, "人生观，世界观，历史观，观点，观念。 Tức là: nhân sinh quan, thế giới quan, quan điểm lịch sử, quan điểm, và quan niệm. Các bạn thấy đấy, âm Hán Việt gần như trùng khớp với tiếng Việt.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 悔 và 于", size=38,
    items=["## 悔 (hối): hối hận, ăn năn",
           "悔恨 hối hận · 悔改 hối cải · 悔过 hối lỗi · 悔婚 hủy hôn · 反悔 nuốt lời",
           "后悔 hối hận · 追悔 ân hận việc đã qua · 悔不当初 hối không kịp · 悔过自新 hối cải làm lại",
           "## 于 (vu): giới từ văn viết, gắn sau động từ / tính từ",
           "勇于 dám · 急于 vội · 长于 giỏi về · 乐于 vui lòng · 苦于 khổ vì · 难于 khó mà",
           "善于 giỏi về · 安于 yên với · 敢于 dám · 属于 thuộc về · 在于 nằm ở"],
    say=[F(0, "Nhóm thứ ba có chữ 悔, Hán Việt là hối, nghĩa là hối hận, ăn năn."),
         F(1, "悔恨，悔改，悔过，悔婚，反悔。 Tức là: hối hận, hối cải, hối lỗi, hủy hôn ước, và nuốt lời. Từ 悔恨 là từ mới của bài."),
         F(2, "后悔，追悔，悔不当初，悔过自新。 Tức là: hối hận, ân hận về việc đã qua, hối hận vì lúc trước đã làm như vậy, và hối cải để làm lại cuộc đời."),
         F(3, "Nhóm cuối cùng có chữ 于, Hán Việt là vu. Đây là giới từ dùng trong văn viết, thường gắn sau động từ hoặc tính từ để tạo thành một từ mới. Lát nữa đây cũng là điểm ngữ pháp đầu tiên."),
         F(4, "勇于，急于，长于，乐于，苦于，难于。 Tức là: dám, vội làm, giỏi về, vui lòng làm, khổ vì, khó mà. Từ 勇于 có trong bài khóa: 勇于承担责任, dám gánh vác trách nhiệm."),
         F(5, "善于，安于，敢于，属于，在于。 Tức là: giỏi về, bằng lòng với, dám, thuộc về, và nằm ở. Hãy chú ý: sau những từ này thường là một động từ hoặc một danh từ, ví dụ 善于学习, giỏi học hỏi.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng)
V = [
    ("做主", "zuò zhǔ", "tố chủ", "động từ", "làm chủ, quyết định", "这件事你自己做主吧。", "Việc này bạn tự quyết định đi.",
     "Động từ, nghĩa là làm chủ, tự mình quyết định. Tên bài 我的人生我做主 nghĩa là cuộc đời tôi, tôi làm chủ. Cụm hay gặp: 为自己做主, tự quyết định cho mình."),
    ("伤脑筋", "shāng nǎojīn", "thương não cân", "quán ngữ", "hao tổn tâm trí, đau đầu", "孩子不爱学习，真让父母伤脑筋。", "Con không thích học, thật khiến bố mẹ đau đầu.",
     "Quán ngữ, nghĩa đen là làm tổn thương gân não, tức là phải suy nghĩ đau đầu vì một chuyện khó giải quyết. Hay dùng: 为某事伤脑筋, 让人伤脑筋."),
    ("枯燥", "kūzào", "khô táo", "tính từ", "nhàm chán, đơn điệu, khô khan", "这本书内容很枯燥，我看不下去。", "Nội dung cuốn sách này rất khô khan, tôi đọc không nổi.",
     "Tính từ. Nghĩa gốc là khô ráo; nghĩa thường dùng là nhàm chán, đơn điệu, khô khan, không có gì thú vị. Thường nói 枯燥无味, khô khan vô vị."),
    ("擅长", "shàncháng", "thiện trường", "động từ", "thông thạo, giỏi về", "她擅长唱歌，也擅长跳舞。", "Cô ấy giỏi hát, cũng giỏi múa.",
     "Động từ, nghĩa là giỏi về, sở trường về một lĩnh vực nào đó, phía sau thường là động từ hoặc danh từ. Âm tiết thứ hai đọc là cháng, thanh hai."),
    ("成本", "chéngběn", "thành bản", "danh từ", "giá thành, chi phí", "今年的生产成本提高了不少。", "Năm nay chi phí sản xuất tăng lên không ít.",
     "Danh từ, nghĩa là giá thành, chi phí. Âm Hán Việt thành bản không dùng trong tiếng Việt, các bạn nhớ nghĩa là chi phí. Trong bài có 时间成本 và 经济成本, tức là chi phí thời gian và chi phí kinh tế."),
    ("急躁", "jízào", "cấp táo", "tính từ", "nôn nóng, nóng nảy, luống cuống", "遇到问题不要急躁，慢慢想办法。", "Gặp vấn đề đừng nóng vội, từ từ nghĩ cách.",
     "Tính từ, nghĩa là nôn nóng, nóng nảy, sốt ruột đến mức luống cuống. Nó gần nghĩa với 着急, nhưng mang sắc thái tiêu cực hơn."),
    ("顾虑", "gùlǜ", "cố lự", "danh từ", "nỗi lo âu, sự lo lắng", "你有什么顾虑，可以告诉我。", "Bạn có điều gì lo lắng thì có thể nói với tôi.",
     "Danh từ, nghĩa là nỗi lo lắng, sự e ngại khiến người ta không dám làm. Trong bài có thành ngữ 顾虑重重, đầy lo lắng, băn khoăn đủ đường."),
    ("过度", "guòdù", "quá độ", "tính từ", "quá mức, quá", "过度使用手机对眼睛不好。", "Dùng điện thoại quá mức không tốt cho mắt.",
     "Tính từ, nghĩa là quá mức, vượt quá giới hạn. Cẩn thận, đây là từ dễ nhầm: quá độ trong tiếng Việt thường nghĩa là chuyển tiếp, như thời kỳ quá độ, tiếng Trung viết là 过渡. Còn 过度 là quá mức, như 过度悲观, bi quan quá mức."),
    ("致使", "zhìshǐ", "trí sử", "động từ / liên từ", "làm cho, khiến cho; đến nỗi, cho nên", "大雨致使很多航班延误。", "Mưa lớn khiến nhiều chuyến bay bị chậm.",
     "Vừa là động từ, vừa là liên từ, nghĩa là khiến cho, đến nỗi; kết quả phía sau thường là điều không tốt. Đây là điểm ngữ pháp thứ hai của bài."),
    ("终身", "zhōngshēn", "chung thân", "danh từ", "cả đời, suốt đời", "这次经历让我终身难忘。", "Trải nghiệm này khiến tôi nhớ suốt đời.",
     "Danh từ, nghĩa là cả đời, suốt đời. Âm Hán Việt chung thân giống tiếng Việt, nhưng tiếng Việt hay dùng trong án chung thân; còn tiếng Trung dùng rộng hơn, như 终身难忘, nhớ suốt đời, 终身学习, học tập suốt đời."),
    ("悔恨", "huǐhèn", "hối hận", "động từ", "hối hận, ân hận", "他对自己做过的事感到非常悔恨。", "Anh ấy vô cùng hối hận về những việc mình đã làm.",
     "Động từ, nghĩa là hối hận, ân hận. So với 后悔, từ 悔恨 nặng hơn, có cả sự đau khổ, tự trách mình."),
    ("类似", "lèisì", "loại tự", "động từ", "tương tự, giống", "我也遇到过类似的问题。", "Tôi cũng từng gặp vấn đề tương tự.",
     "Động từ, nghĩa là tương tự, gần giống. Hay dùng làm định ngữ: 类似的问题, 类似的情况. Trong bài có 类似小王这样的年轻人, những người trẻ giống như Tiểu Vương."),
    ("并非", "bìngfēi", "tịnh phi", "động từ", "không phải", "成功并非一件容易的事。", "Thành công không phải là chuyện dễ dàng.",
     "Động từ, nghĩa là hoàn toàn không phải, giống 并不是, mang màu sắc văn viết. Đây là điểm ngữ pháp thứ ba của bài."),
    ("精确", "jīngquè", "tinh xác", "tính từ", "chính xác", "这个数字必须非常精确。", "Con số này phải hết sức chính xác.",
     "Tính từ, nghĩa là chính xác đến từng chi tiết, mức độ cao hơn 准确. Trong bài có 精确的判断力, khả năng phán đoán chính xác."),
    ("天生", "tiānshēng", "thiên sinh", "tính từ", "trời sinh, bẩm sinh", "她天生一副好嗓子。", "Cô ấy bẩm sinh đã có giọng hát hay.",
     "Tính từ, nghĩa là trời sinh, bẩm sinh, sinh ra đã có. Bài khóa khẳng định: 能力不是天生的, năng lực không phải bẩm sinh."),
    ("挫折", "cuòzhé", "tỏa chiết", "động từ", "thất bại, vấp ngã", "遇到挫折时，千万不要放弃。", "Khi gặp thất bại, nhất định đừng bỏ cuộc.",
     "Sách ghi là động từ, nghĩa là thất bại, vấp ngã; nhưng thường dùng như danh từ: 遇到挫折, gặp trắc trở, 经历挫折, trải qua vấp ngã."),
    ("意志", "yìzhì", "ý chí", "danh từ", "ý chí", "他是一个意志坚强的人。", "Anh ấy là người có ý chí kiên cường.",
     "Danh từ, nghĩa là ý chí, giống hệt tiếng Việt. Trong bài có 坚定的意志力, ý chí kiên định."),
    ("敏锐", "mǐnruì", "mẫn duệ", "tính từ", "nhạy bén, nhanh nhạy", "记者需要有敏锐的观察力。", "Phóng viên cần có óc quan sát nhạy bén.",
     "Tính từ, nghĩa là nhạy bén, sắc sảo, thường đi với 观察力, khả năng quan sát, và 判断力, khả năng phán đoán."),
    ("畏惧", "wèijù", "úy cụ", "động từ", "sợ, khiếp sợ", "面对困难，他毫不畏惧。", "Đối mặt khó khăn, anh ấy không chút sợ hãi.",
     "Động từ, nghĩa là sợ hãi, e sợ, mang màu sắc văn viết. Hay gặp: 毫不畏惧, không chút sợ hãi."),
    ("勇于", "yǒngyú", "dũng vu", "động từ", "can đảm, dũng cảm, mạnh dạn", "年轻人要勇于尝试新事物。", "Người trẻ phải dám thử những điều mới.",
     "Động từ, nghĩa là dám, mạnh dạn làm việc gì đó, phía sau luôn có một động từ. Bài khóa có 勇于承担责任, dám gánh vác trách nhiệm."),
    ("伴随", "bànsuí", "bạn tùy", "động từ", "đi đôi với, đi kèm", "音乐伴随我度过了童年。", "Âm nhạc đã đi cùng tôi suốt tuổi thơ.",
     "Động từ, nghĩa là đi kèm, đi cùng. Mẫu hay gặp là 伴随着, gần nghĩa với 随着, như trong bài: 伴随着经济全球化, cùng với toàn cầu hóa kinh tế."),
    ("日益", "rìyì", "nhật ích", "phó từ", "ngày càng", "两国的交流日益增多。", "Giao lưu giữa hai nước ngày càng nhiều.",
     "Phó từ, nghĩa là ngày càng, mang màu sắc văn viết. Lát nữa chúng ta sẽ phân biệt kỹ 日益 với 越来越."),
    ("昔日", "xīrì", "tích nhật", "danh từ", "ngày xưa, thời trước", "昔日的小渔村变成了大城市。", "Làng chài nhỏ ngày xưa đã biến thành thành phố lớn.",
     "Danh từ, nghĩa là ngày xưa, ngày trước, dùng trong văn viết, giống 以前 hay 过去 trong khẩu ngữ."),
    ("风光", "fēngguāng", "phong quang", "tính từ", "vẻ vang, huy hoàng", "他当年在公司里很风光。", "Năm đó anh ấy rất vẻ vang ở công ty.",
     "Ở bài này là tính từ, nghĩa là vẻ vang, huy hoàng, được nhiều người ngưỡng mộ. Chú ý: 风光 còn là danh từ nghĩa là phong cảnh, như 风光美丽. Trong bài, 昔日风光无限 là ngày xưa vô cùng huy hoàng."),
    ("亏损", "kuīsǔn", "khuy tổn", "động từ", "hao hụt, lỗ vốn", "这家公司去年亏损了几百万。", "Công ty này năm ngoái lỗ mấy triệu.",
     "Động từ, nghĩa là thua lỗ, lỗ vốn, thường nói về doanh nghiệp. Trái nghĩa là 盈利, có lãi."),
    ("倒闭", "dǎobì", "đảo bế", "động từ", "phá sản, sập tiệm", "由于经营不善，那家工厂倒闭了。", "Do kinh doanh kém, nhà máy đó đã phá sản.",
     "Động từ, nghĩa là phá sản, đóng cửa, dẹp tiệm. Chú ý cách đọc: âm tiết đầu đọc thanh ba, dǎo."),
    ("金融", "jīnróng", "kim dung", "danh từ", "tài chính", "他在一家金融公司工作。", "Anh ấy làm việc ở một công ty tài chính.",
     "Danh từ, nghĩa là tài chính, tiền tệ. Âm Hán Việt kim dung không dùng trong tiếng Việt, các bạn nhớ nghĩa là tài chính. Ví dụ 金融危机, khủng hoảng tài chính."),
    ("危机", "wēijī", "nguy cơ", "danh từ", "khủng hoảng", "公司正面临一场严重的危机。", "Công ty đang đối mặt với một cuộc khủng hoảng nghiêm trọng.",
     "Danh từ, nghĩa là khủng hoảng. Đây là từ rất dễ nhầm: nguy cơ trong tiếng Việt là khả năng xảy ra điều xấu, tiếng Trung nói là 风险; còn 危机 là cuộc khủng hoảng đã xảy ra."),
    ("盈利", "yínglì", "doanh lợi", "động từ", "thu lợi, có lãi", "这家饭店开业第一年就盈利了。", "Nhà hàng này năm đầu khai trương đã có lãi.",
     "Động từ, nghĩa là có lãi, thu được lợi nhuận. Trong bài có 连年盈利, có lãi nhiều năm liền."),
    ("运行", "yùnxíng", "vận hành", "động từ", "vận hành", "新地铁线路已经正式运行。", "Tuyến tàu điện ngầm mới đã chính thức vận hành.",
     "Động từ, nghĩa là vận hành, hoạt động, dùng cho máy móc, tàu xe, và cả doanh nghiệp. Âm Hán Việt giống tiếng Việt."),
    ("裁员", "cáiyuán", "tài viên", "động từ", "cắt giảm nhân sự", "因为经济不景气，很多公司开始裁员。", "Vì kinh tế suy thoái, nhiều công ty bắt đầu cắt giảm nhân sự.",
     "Động từ, nghĩa là cắt giảm nhân viên. 裁 là cắt, như 裁缝, thợ may; 员 là nhân viên, các bạn đã gặp ở bài trước."),
    ("意味着", "yìwèizhe", "ý vị trước", "động từ", "có nghĩa là, ngụ ý", "毕业意味着新生活的开始。", "Tốt nghiệp có nghĩa là sự khởi đầu của cuộc sống mới.",
     "Động từ, nghĩa là có nghĩa là, đồng nghĩa với. Phía sau thường là một mệnh đề. Trong bài: 这意味着，原本英明的决定今天看来可能并非如此了。"),
    ("英明", "yīngmíng", "anh minh", "tính từ", "sáng suốt, minh mẫn", "事实证明，这是一个英明的决定。", "Thực tế chứng minh, đây là một quyết định sáng suốt.",
     "Tính từ, nghĩa là sáng suốt, anh minh, thường đi với 决定, quyết định, hoặc 领导, lãnh đạo."),
    ("称心如意", "chènxīn rúyì", "xứng tâm như ý", "thành ngữ", "như ý muốn, hợp ý", "他终于找到了一份称心如意的工作。", "Cuối cùng anh ấy đã tìm được một công việc như ý.",
     "Thành ngữ, nghĩa là vừa lòng, như ý muốn. Chú ý cách đọc: âm tiết đầu đọc chèn, thanh bốn, không đọc chēng."),
    ("除", "chú", "trừ", "giới từ", "ngoài… ra, trừ… ra", "除他以外，大家都同意了。", "Ngoài anh ấy ra, mọi người đều đồng ý.",
     "Giới từ, nghĩa là ngoài ra, trừ ra, giống 除了, thường dùng theo mẫu 除……以外 hoặc 除……之外. Trong bài có 除此以外, ngoài điều này ra."),
    ("争先恐后", "zhēngxiān-kǒnghòu", "tranh tiên khủng hậu", "thành ngữ", "tranh lên trước, sợ rớt lại sau", "孩子们争先恐后地回答问题。", "Bọn trẻ tranh nhau trả lời câu hỏi.",
     "Thành ngữ. Nghĩa đen là tranh lên trước, sợ bị tụt lại phía sau; tức là chen nhau, tranh nhau làm một việc."),
    ("热门", "rèmén", "nhiệt môn", "danh từ", "sự phổ biến, được nhiều người ưa chuộng", "计算机是现在的热门专业。", "Công nghệ thông tin là ngành học được ưa chuộng hiện nay.",
     "Danh từ, chỉ thứ đang hot, được nhiều người quan tâm, theo đuổi. Hay gặp: 热门专业, ngành học hot; 热门话题, chủ đề nóng. Trái nghĩa là 冷门."),
    ("以致", "yǐzhì", "dĩ trí", "liên từ", "cho nên, vì vậy, đến nỗi", "他平时不努力，以致考试没及格。", "Bình thường anh ấy không chăm chỉ, đến nỗi thi trượt.",
     "Liên từ, đứng đầu vế sau, nghĩa là đến nỗi, dẫn đến; kết quả thường là điều không mong muốn, giống liên từ 致使."),
    ("饱和", "bǎohé", "bão hòa", "động từ", "bão hòa", "这个城市的出租车市场已经饱和了。", "Thị trường taxi của thành phố này đã bão hòa.",
     "Động từ, nghĩa là bão hòa, đã đầy, không chứa thêm được nữa. Trong bài có 人才饱和, nhân lực đã quá thừa."),
    ("就业", "jiù yè", "tựu nghiệp", "động từ", "tìm việc, có việc làm", "大学生就业越来越难了。", "Sinh viên tìm được việc làm ngày càng khó.",
     "Động từ, nghĩa là có việc làm, đi làm. Đây là từ ly hợp. Hay gặp: 就业困难, khó tìm việc; 就业机会, cơ hội việc làm."),
    ("及早", "jízǎo", "cập tảo", "phó từ", "nhanh chóng, sớm", "有病要及早治疗。", "Có bệnh phải sớm chữa trị.",
     "Phó từ, nghĩa là sớm, kịp thời, trước khi quá muộn, đứng trước động từ."),
    ("机遇", "jīyù", "cơ ngộ", "danh từ", "cơ hội, thời cơ", "机遇总是留给有准备的人。", "Cơ hội luôn dành cho người có chuẩn bị.",
     "Danh từ, nghĩa là cơ hội, thời cơ tốt. Cẩn thận: cơ ngộ trong tiếng Việt là cuộc gặp gỡ tình cờ; còn 机遇 là cơ hội, gần nghĩa với 机会 nhưng trang trọng hơn."),
    ("心灵", "xīnlíng", "tâm linh", "danh từ", "tâm hồn", "音乐可以净化人的心灵。", "Âm nhạc có thể thanh lọc tâm hồn con người.",
     "Danh từ, nghĩa là tâm hồn, nội tâm. Đây là từ dễ nhầm nhất bài: tâm linh trong tiếng Việt chỉ thế giới thần linh, tín ngưỡng; còn 心灵 chỉ là tâm hồn, như 心灵美, tâm hồn đẹp."),
    ("免疫", "miǎnyì", "miễn dịch", "động từ", "miễn dịch", "多运动可以提高身体的免疫力。", "Vận động nhiều có thể nâng cao sức đề kháng.",
     "Động từ, nghĩa là miễn dịch, giống tiếng Việt. Thường gặp 免疫力, sức miễn dịch. Bài khóa dùng hình ảnh 心灵免疫力, sức đề kháng của tâm hồn."),
    ("决策", "juécè", "quyết sách", "động từ", "ra quyết định chiến lược", "这个问题需要领导及时决策。", "Vấn đề này cần lãnh đạo kịp thời đưa ra quyết định.",
     "Động từ, nghĩa là quyết định những việc quan trọng; cũng dùng như danh từ, như 决策能力, khả năng ra quyết định. Tiếng Việt quyết sách thường chỉ chính sách lớn của nhà nước, còn 决策 dùng rộng hơn, cả cho cá nhân."),
]

add("bullets", chapter="Từ mới (45 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 7 có 45 từ mới, chia thành 15 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 擅长 (cháng) · 倒闭 (dǎo) · 称心如意 (chèn)",
           "Từ dễ nhầm: 过度 · 危机 · 机遇 · 心灵 · 成本 · 金融"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có bốn mươi lăm từ, thầy chia thành mười lăm nhóm, mỗi nhóm ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số từ có âm đọc cần chú ý, như 擅长，倒闭，称心如意. Thầy sẽ nhắc khi gặp."),
         F(4, "Ngoài ra, có mấy từ Hán Việt rất dễ hiểu nhầm, như 过度，危机，机遇，心灵. Nghĩa của chúng trong tiếng Trung khác với tiếng Việt, các bạn nhớ nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

sizes = [3] * 15
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
    ("最近，小王正为工作的事伤脑筋。毕业于3年前的他，一直做会计，成天和数字打交道，枯燥而且压力大，他做梦都想换一份工作。",
     "Gần đây, Tiểu Vương đang đau đầu vì chuyện công việc. Anh tốt nghiệp ba năm trước, từ đó đến nay luôn làm kế toán, suốt ngày tiếp xúc với những con số, vừa khô khan lại vừa áp lực, đến nằm mơ anh cũng muốn đổi một công việc khác.",
     ["正为……伤脑筋 là đang đau đầu vì chuyện gì. 毕业于三年前 là tốt nghiệp vào ba năm trước, 于 ở đây chỉ thời gian; đây chính là điểm ngữ pháp 于.",
      "成天 là suốt ngày. 和数字打交道 là tiếp xúc với những con số; mẫu 和某人打交道 là giao tiếp, làm việc với ai đó. 做梦都想 là đến nằm mơ cũng muốn, ý nói khao khát vô cùng."],
     "最近，小王正为工作的事伤脑筋。毕业于三年前的他，一直做会计，成天和数字打交道，枯燥而且压力大，他做梦都想换一份工作。"),
    ("小王对艺术、心理学都感兴趣，觉得当老师也不错，可他不确定自己真正擅长什么，怕万一选错了，要付出很大的时间成本和经济成本，为此他变得急躁、紧张、顾虑重重。",
     "Tiểu Vương đều có hứng thú với nghệ thuật và tâm lý học, cũng thấy làm giáo viên không tồi, nhưng anh không chắc mình thật sự giỏi cái gì, sợ lỡ chọn sai thì phải trả giá rất lớn về thời gian và tiền bạc, vì thế anh trở nên nôn nóng, căng thẳng, lo lắng đủ điều.",
     ["万一 là lỡ như, nhỡ đâu, dùng cho khả năng không mong muốn. 付出……成本 là phải trả cái giá, tức là bỏ ra chi phí.",
      "为此 là vì thế, vì việc này. 顾虑重重 là lo lắng chồng chất, băn khoăn đủ đường; 重重 ở đây nghĩa là nhiều lớp."]),
    ("心理专家认为，对自己缺乏信心，对未来过度悲观致使小王出现以上现象。",
     "Chuyên gia tâm lý cho rằng, thiếu tự tin vào bản thân và bi quan quá mức về tương lai đã khiến Tiểu Vương xuất hiện những biểu hiện trên.",
     ["Chủ ngữ của 致使 ở đây là hai cụm động từ: 对自己缺乏信心 và 对未来过度悲观. 致使 nghĩa là khiến cho, kết quả phía sau là điều không tốt.",
      "以上现象 là những hiện tượng nói ở trên, tức là nôn nóng, căng thẳng, lo lắng. 以上 là ở trên, trái nghĩa là 以下."]),
    ("悲观主要包括：我不敢想最坏的结果是什么；我无法承受这个结果；一旦选错，终身悔恨，甚至会觉得人生都没有希望了。",
     "Sự bi quan chủ yếu gồm: tôi không dám nghĩ kết quả tệ nhất là gì; tôi không thể chịu đựng được kết quả ấy; một khi chọn sai sẽ hối hận cả đời, thậm chí còn cảm thấy cuộc đời chẳng còn hy vọng gì nữa.",
     ["Câu dùng dấu hai chấm để liệt kê, các ý ngăn cách bằng dấu chấm phẩy. 无法承受 là không thể chịu đựng nổi.",
      "一旦……，…… là một khi đã…, thì…. 终身悔恨 là hối hận suốt đời, kết hợp hai từ mới 终身 và 悔恨."]),
    ("其实，类似小王这样的年轻人并非少数，不知道小王们是否读过下面这段对话：",
     "Thật ra, những người trẻ giống như Tiểu Vương không phải là số ít, không biết các Tiểu Vương đã từng đọc đoạn đối thoại dưới đây chưa:",
     ["类似……这样的 là giống như… thế này. 并非少数 là không hề ít, tức là rất nhiều; đây là điểm ngữ pháp 并非.",
      "小王们 là cách nói thú vị: thêm 们 vào tên riêng để chỉ tất cả những người giống Tiểu Vương. 是否 là có… hay không, văn viết."]),
    ("年轻人：你的智慧从哪里来？\n乔布斯：来自精确的判断力。\n年轻人：精确的判断力从哪里来？\n乔布斯：来自经验的积累。",
     "Người trẻ: Trí tuệ của ông từ đâu mà có? – Steve Jobs: Từ khả năng phán đoán chính xác. – Người trẻ: Khả năng phán đoán chính xác từ đâu mà có? – Steve Jobs: Từ sự tích lũy kinh nghiệm.",
     ["乔布斯 là cách phiên âm tên Steve Jobs, người sáng lập công ty Apple. 来自 là đến từ, dùng nhiều trong văn viết.",
      "积累 là tích lũy. Các bạn để ý, câu trả lời sau lấy lại từ khóa của câu trước, như một chuỗi mắt xích: trí tuệ, phán đoán, kinh nghiệm."]),
    ("年轻人：那你的经验又从哪里来？\n乔布斯：来自无数错误的判断。",
     "Người trẻ: Vậy kinh nghiệm của ông lại từ đâu mà có? – Steve Jobs: Từ vô số lần phán đoán sai lầm.",
     ["Đây là câu then chốt của cả bài: kinh nghiệm đến từ vô số lần phán đoán sai. Nói cách khác, sai lầm là con đường dẫn đến trí tuệ.",
      "无数 là vô số, không đếm xuể. 又 trong 又从哪里来 biểu thị câu hỏi tiếp nối, lại hỏi thêm một bước nữa."]),
    ("做决定是一种能力，而能力不是天生的，是通过实践和挫折得来的，在这个过程中，人同时具有了坚定的意志力和敏锐的判断力，不畏惧付出和失败，勇于承担责任，这就是成长。",
     "Ra quyết định là một năng lực, mà năng lực thì không phải bẩm sinh, nó có được nhờ thực tiễn và những lần vấp ngã. Trong quá trình ấy, con người đồng thời có được ý chí kiên định và khả năng phán đoán nhạy bén, không sợ bỏ công sức và thất bại, dám gánh vác trách nhiệm, đó chính là trưởng thành.",
     ["不是……，是…… là không phải…, mà là…. 通过……得来的 là có được thông qua…. 而 ở đầu vế thứ hai nối tiếp ý, nghĩa là mà.",
      "不畏惧 là không sợ, 勇于承担责任 là dám gánh vác trách nhiệm. Câu này là ví dụ của điểm ngữ pháp 于, chỉ phương diện."]),
    ("事实上，伴随着经济全球化，生活中的不确定因素日益增多。昔日风光无限的世界一流企业也会亏损，也会倒闭；",
     "Trên thực tế, cùng với toàn cầu hóa kinh tế, những yếu tố bất định trong cuộc sống ngày càng nhiều. Những doanh nghiệp hàng đầu thế giới từng vô cùng huy hoàng cũng có thể thua lỗ, cũng có thể phá sản;",
     ["伴随着 gần nghĩa với 随着, là cùng với. 日益增多 là ngày càng nhiều; chú ý 日益 đi với động từ hai âm tiết 增多.",
      "风光无限 là vô cùng vẻ vang. 一流企业 là doanh nghiệp hàng đầu. Hai lần 也会 nhấn mạnh: ngay cả họ cũng không tránh khỏi."]),
    ("一次金融危机，就会使一些连年盈利、运行很好的企业不得不裁员。这意味着，原本英明的决定今天看来可能并非如此了。",
     "Chỉ một cuộc khủng hoảng tài chính cũng đủ khiến một số doanh nghiệp có lãi nhiều năm liền, vận hành rất tốt buộc phải cắt giảm nhân sự. Điều này có nghĩa là, quyết định vốn dĩ rất sáng suốt, nhìn từ hôm nay có thể không còn như vậy nữa.",
     ["一次……就会…… là chỉ một lần… là đã có thể…. 连年 là nhiều năm liền. 不得不 là buộc phải, không thể không.",
      "原本 là vốn dĩ. 今天看来 là nhìn từ hôm nay. 并非如此 là hoàn toàn không phải như vậy, một cụm rất hay dùng với 并非."]),
    ("依我看，无论你怎么选择，都不太可能选一份称心如意的工作安安稳稳一辈子，由于经济环境的不确定，企业的寿命越来越短，现在，人们要经历更多次的职业选择。",
     "Theo tôi thấy, dù bạn chọn thế nào, cũng khó có thể chọn được một công việc như ý rồi yên ổn cả đời. Do môi trường kinh tế bất định, tuổi thọ của doanh nghiệp ngày càng ngắn, hiện nay con người phải trải qua nhiều lần chọn nghề hơn.",
     ["依我看 là theo tôi thấy, dùng để nêu ý kiến cá nhân. 无论你怎么选择，都不太可能 là dù bạn chọn thế nào, cũng khó có thể; mẫu này nghĩa là bất kể… đều….",
      "安安稳稳 là dạng lặp của 安稳, yên ổn, làm trạng ngữ. 一辈子 là cả đời, khẩu ngữ, gần nghĩa với 终身. 寿命 là tuổi thọ."]),
    ("除此以外，由于人们争先恐后报考热门专业，以致人才饱和，就业困难。",
     "Ngoài ra, do mọi người tranh nhau đăng ký thi vào các ngành hot, đến nỗi nhân lực bão hòa, khó tìm việc làm.",
     ["除此以外 là ngoài điều này ra, 此 là điều này, văn viết. 报考 là đăng ký dự thi.",
      "由于……，以致…… là do…, đến nỗi…: vế sau là kết quả không mong muốn. 以致 có cách dùng giống 致使 khi làm liên từ."]),
    ("而一些新职业的出现，需要新型人才的加入，谁能够及早抓住机会，谁就赢得了机遇。",
     "Còn sự xuất hiện của một số nghề mới cần có những nhân tài kiểu mới tham gia, ai sớm nắm bắt được cơ hội, người đó sẽ giành được thời cơ.",
     ["而 ở đầu câu biểu thị chuyển ý nhẹ, nghĩa là còn, nhưng. 新型 là kiểu mới.",
      "谁能够……，谁就…… là ai có thể…, người đó sẽ…; hai đại từ nghi vấn ở hai vế chỉ cùng một người. 抓住机会 là nắm bắt cơ hội, 赢得机遇 là giành được thời cơ."]),
    ("不要怕犯错，不要害怕走弯路，犯些小错并非坏事，它会增加我们的心灵免疫力。",
     "Đừng sợ mắc lỗi, đừng sợ đi đường vòng, mắc vài lỗi nhỏ không phải là chuyện xấu, nó sẽ tăng sức đề kháng cho tâm hồn chúng ta.",
     ["走弯路 là đi đường vòng, nghĩa bóng là làm việc theo cách tốn công, mắc sai lầm rồi mới đến đích. Bài tập bốn sẽ nói về cách nói ví von này.",
      "心灵免疫力 là sức miễn dịch của tâm hồn: mắc lỗi nhỏ giống như tiêm vắc xin, giúp ta vững vàng hơn trước thất bại lớn."]),
    ("不确定中充满成长的机会，只有不断提升自己的决策能力，才能真正为自己的人生做主。",
     "Trong sự bất định chứa đầy cơ hội trưởng thành, chỉ có không ngừng nâng cao khả năng ra quyết định của mình, mới có thể thật sự làm chủ cuộc đời mình.",
     ["只有……才…… là chỉ có… mới…, nhấn mạnh điều kiện duy nhất. 提升 là nâng cao.",
      "为自己的人生做主 là làm chủ cuộc đời mình, quay lại đúng tên bài. Bài được cải biên từ một bài báo trên báo Thanh niên Bắc Kinh, bàn về chứng lo âu khi lựa chọn nghề nghiệp."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 我的人生我做主", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 我的人生我做主, dài bảy trăm ba mươi chín chữ. Bài được cải biên từ bài báo Làm sao tránh xa chứng lo âu khi chọn nghề, đăng trên báo Thanh niên Bắc Kinh.",
         F(0, "Thầy chia bài thành mười lăm đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 100 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Tóm tắt nội dung", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5) – phần 1", size=34,
    items=["## 1. 为什么小王最近为工作的事伤脑筋？",
           "目前的工作枯燥而且压力大 · 对艺术、心理学都感兴趣，可不确定自己擅长什么，怕选错",
           "## 2. 什么原因使小王出现急躁、紧张、顾虑重重的现象？",
           "对自己缺乏信心 · 对未来过度悲观：不敢想最坏的结果，无法承受，一旦选错，终身悔恨",
           "## 3. 乔布斯的智慧从哪里来？",
           "智慧 ← 精确的判断力 ← 经验的积累 ← 无数错误的判断"],
    say=["Bài tập năm của sách yêu cầu dựa vào gợi ý để tóm tắt nội dung chính của bài khóa. Chúng ta cùng làm luôn nhé.",
         F(0, "Câu hỏi một: vì sao gần đây Tiểu Vương đau đầu vì chuyện công việc?"),
         F(1, "Vì 目前的工作枯燥而且压力大, công việc hiện tại khô khan lại áp lực. Anh 对艺术、心理学都感兴趣，可不确定自己擅长什么, có hứng thú với nghệ thuật và tâm lý học, nhưng không chắc mình giỏi gì, nên sợ chọn sai."),
         F(2, "Câu hỏi hai: nguyên nhân nào khiến Tiểu Vương nôn nóng, căng thẳng, lo lắng đủ đường?"),
         F(3, "Một là 对自己缺乏信心, thiếu tự tin vào bản thân. Hai là 对未来过度悲观, bi quan quá mức về tương lai: không dám nghĩ kết quả xấu nhất, không chịu đựng nổi, một khi chọn sai sẽ hối hận cả đời."),
         F(4, "Câu hỏi ba: trí tuệ của Steve Jobs từ đâu mà có?"),
         F(5, "Trí tuệ đến từ phán đoán chính xác, phán đoán chính xác đến từ tích lũy kinh nghiệm, và kinh nghiệm đến từ vô số lần phán đoán sai.")])

add("bullets", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5) – phần 2", size=34,
    items=["## 4. 做决定的能力是怎么得来的？",
           "通过实践和挫折得来的 · 具有了坚定的意志力和敏锐的判断力，不畏惧付出和失败，勇于承担责任",
           "## 5. 为什么说生活中的不确定因素日益增多？",
           "世界一流企业也会亏损、倒闭 · 金融危机使连年盈利的企业不得不裁员",
           "## 6. 为什么说不太可能选一份称心如意的工作安安稳稳一辈子？",
           "企业寿命越来越短 · 报考热门专业，以致人才饱和 · 新职业的出现，需要新型人才"],
    say=[F(0, "Câu hỏi bốn: khả năng ra quyết định từ đâu mà có?"),
         F(1, "Nó có được nhờ thực tiễn và vấp ngã. Trong quá trình đó, con người có ý chí kiên định, phán đoán nhạy bén, không sợ bỏ công sức và thất bại, dám gánh vác trách nhiệm."),
         F(2, "Câu hỏi năm: vì sao nói các yếu tố bất định trong cuộc sống ngày càng nhiều?"),
         F(3, "Vì ngay cả doanh nghiệp hàng đầu thế giới cũng có thể thua lỗ, phá sản; chỉ một cuộc khủng hoảng tài chính cũng khiến các doanh nghiệp có lãi nhiều năm phải cắt giảm nhân sự."),
         F(4, "Câu hỏi sáu: vì sao nói khó có thể chọn được một công việc như ý rồi yên ổn cả đời?"),
         F(5, "Thứ nhất, tuổi thọ doanh nghiệp ngày càng ngắn, người ta phải đổi nghề nhiều lần. Thứ hai, mọi người tranh nhau thi vào ngành hot, đến nỗi nhân lực bão hòa. Thứ ba, các nghề mới xuất hiện, cần nhân tài kiểu mới, ai nắm bắt sớm sẽ thắng. Bố cục này rất có ích khi các bạn tự kể lại bài khóa.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 于", section="Ngữ pháp 注释", title="1. 于 yú – giới từ văn viết", size=36,
    items=["## (1) Chỉ thời gian, nơi chốn – tương đương 在",
           "毕业于3年前的他，一直做会计，成天和数字打交道，枯燥而且压力大。",
           "著名的西湖龙井茶产于浙江省的西湖一带。",
           "## (2) Chỉ phương diện, nguyên nhân, mục đích",
           "我一直想和他一起去旅行，只是苦于没有时间。",
           "……不畏惧付出和失败，勇于承担责任，这就是成长。"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là giới từ 于. Đây là giới từ dùng trong văn viết.",
         F(0, "Cách dùng thứ nhất: chỉ thời gian hoặc nơi chốn, nghĩa tương đương với 在. Chú ý: 于 thường đứng sau động từ."),
         F(1, "Ví dụ một, lấy từ bài khóa: 毕业于三年前的他，一直做会计，成天和数字打交道，枯燥而且压力大。 Anh ấy, người tốt nghiệp ba năm trước, luôn làm kế toán, suốt ngày tiếp xúc với con số, vừa khô khan lại áp lực. 毕业于三年前 bằng với 在三年前毕业."),
         F(2, "Ví dụ hai: 著名的西湖龙井茶产于浙江省的西湖一带。 Trà Long Tỉnh Tây Hồ nổi tiếng được sản xuất ở vùng Tây Hồ, tỉnh Chiết Giang. 产于 là được sản xuất tại."),
         F(3, "Cách dùng thứ hai: chỉ phương diện, nguyên nhân, hoặc mục đích. Lúc này 于 gắn chặt sau một động từ hay tính từ, như 苦于，勇于，善于，急于 mà các bạn đã gặp ở phần khởi động."),
         F(4, "Ví dụ ba: 我一直想和他一起去旅行，只是苦于没有时间。 Tôi luôn muốn đi du lịch cùng anh ấy, chỉ khổ nỗi là không có thời gian. 苦于 chỉ nguyên nhân gây khổ."),
         F(5, "Ví dụ bốn, lấy từ bài khóa: 不畏惧付出和失败，勇于承担责任，这就是成长。 Không sợ bỏ công sức và thất bại, dám gánh vác trách nhiệm, đó chính là trưởng thành. 勇于 chỉ phương diện mà người đó dũng cảm.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: chọn vị trí thích hợp cho 于", reveal=True, size=36,
    items=["(1) 我已经A开始B写论文了，C最近正忙D收集资料。",
           "Đáp án: D → 最近正忙于收集资料。",
           "(2) A那时候，人们苦B长期C战乱，渴望D政治统一。",
           "Đáp án: B → 人们苦于长期战乱，渴望政治统一。",
           "(3) A第三届茅盾文学奖B获奖小说C《平凡的世界》出版D1986年。",
           "Đáp án: D → 《平凡的世界》出版于1986年。"],
    say=[F(0, "Luyện tập: chọn vị trí thích hợp cho 于. Câu một: 我已经开始写论文了，最近正忙收集资料。 Bốn vị trí A, B, C, D lần lượt là trước 开始, trước 写, trước 最近, và sau 忙. Các bạn tạm dừng và chọn nhé."),
         F(1, "Đáp án: D. 最近正忙于收集资料。 Dạo này tôi đang bận thu thập tư liệu. 忙于 là bận rộn với việc gì, chỉ phương diện."),
         F(2, "Câu hai: 那时候，人们苦长期战乱，渴望政治统一。 Vị trí A ở đầu câu, B sau 苦, C trước 战乱, D trước 政治."),
         F(3, "Đáp án: B. 人们苦于长期战乱，渴望政治统一。 Thời đó, người dân khổ vì chiến loạn kéo dài, khao khát đất nước thống nhất. 苦于 chỉ nguyên nhân."),
         F(4, "Câu ba: 第三届茅盾文学奖获奖小说平凡的世界出版一九八六年。 Vị trí D nằm giữa 出版 và năm một chín tám sáu."),
         F(5, "Đáp án: D. 平凡的世界出版于一九八六年。 Tiểu thuyết Thế giới bình thường, tác phẩm đoạt giải Mao Thuẫn lần thứ ba, được xuất bản năm một chín tám sáu. Ở đây 于 chỉ thời gian, giống 在.")])

add("bullets", chapter="Ngữ pháp: 致使", section="Ngữ pháp 注释", title="2. 致使 zhìshǐ – khiến cho, đến nỗi", size=36,
    items=["## (1) Động từ: do một nguyên nhân nào đó mà khiến cho",
           "他的粗心致使试验失败。",
           "对自己缺乏信心，对未来过度悲观致使小王出现以上现象。",
           "## (2) Liên từ: đầu vế sau, chỉ kết quả (thường tiêu cực, không mong muốn)",
           "因为人类对木材的需求与日俱增，致使森林面积大幅度减少。",
           "由于新产品研发能力有限，致使企业逐渐失去竞争力。"],
    say=["Điểm ngữ pháp thứ hai là 致使.",
         F(0, "Cách dùng thứ nhất: 致使 là động từ, biểu thị do một nguyên nhân nào đó mà khiến cho một kết quả xảy ra. Chủ ngữ chính là nguyên nhân."),
         F(1, "Ví dụ một: 他的粗心致使试验失败。 Sự cẩu thả của anh ấy đã khiến thí nghiệm thất bại."),
         F(2, "Ví dụ hai, lấy từ bài khóa: 对自己缺乏信心，对未来过度悲观致使小王出现以上现象。 Thiếu tự tin vào bản thân và bi quan quá mức về tương lai đã khiến Tiểu Vương có những biểu hiện trên."),
         F(3, "Cách dùng thứ hai: 致使 là liên từ, đứng đầu vế câu sau, biểu thị kết quả do nguyên nhân ở vế trước gây ra. Kết quả thường là điều tiêu cực, hoặc người nói không mong muốn. Vế trước hay có 因为 hoặc 由于."),
         F(4, "Ví dụ ba: 因为人类对木材的需求与日俱增，致使森林面积大幅度减少。 Vì nhu cầu gỗ của con người tăng lên từng ngày, đến nỗi diện tích rừng giảm mạnh."),
         F(5, "Ví dụ bốn: 由于新产品研发能力有限，致使企业逐渐失去竞争力。 Do năng lực nghiên cứu phát triển sản phẩm mới có hạn, đến nỗi doanh nghiệp dần dần mất đi sức cạnh tranh. Mẹo nhớ: 致使 gần nghĩa với 以致 trong bài, và trang trọng hơn 使 hay 让.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: hoàn thành câu với 致使", reveal=True, size=36,
    items=["(1) 暖冬致使流感病人______。",
           "Đáp án: 暖冬致使流感病人大量增加。",
           "(2) 由于连日暴风雪，致使______，几千名乘客滞留机场。",
           "Đáp án: ……致使航班全部取消，几千名乘客滞留机场。",
           "(3) 由于经营管理不善，致使______。",
           "Đáp án: ……致使公司连年亏损，最后不得不倒闭。"],
    say=[F(0, "Luyện tập: hoàn thành câu. Câu một: 暖冬致使流感病人什么？ Mùa đông ấm khiến cho bệnh nhân cúm thế nào? Các bạn tạm dừng và thử hoàn thành nhé."),
         F(1, "Đáp án gợi ý: 暖冬致使流感病人大量增加。 Mùa đông ấm khiến số bệnh nhân cúm tăng mạnh. Ở đây 致使 là động từ."),
         F(2, "Câu hai: 由于连日暴风雪，致使什么，几千名乘客滞留机场。 Do bão tuyết nhiều ngày liền, đến nỗi chuyện gì xảy ra, khiến mấy nghìn hành khách bị kẹt lại ở sân bay?"),
         F(3, "Đáp án gợi ý: 致使航班全部取消，几千名乘客滞留机场。 Đến nỗi toàn bộ chuyến bay bị hủy, mấy nghìn hành khách bị kẹt lại sân bay."),
         F(4, "Câu ba: 由于经营管理不善，致使什么。 Do kinh doanh và quản lý kém, đến nỗi thế nào?"),
         F(5, "Đáp án gợi ý: 致使公司连年亏损，最后不得不倒闭。 Đến nỗi công ty thua lỗ nhiều năm liền, cuối cùng buộc phải phá sản. Các bạn thấy đấy, kết quả sau 致使 đều là điều không tốt.")])

add("bullets", chapter="Ngữ pháp: 并非", section="Ngữ pháp 注释", title="3. 并非 bìngfēi – hoàn toàn không phải", size=36,
    items=["Động từ, nghĩa là 并不是; 并 đứng trước từ phủ định 非 để tăng cường ngữ khí phủ định",
           "Thường dùng để phủ định một suy nghĩ, một nhận định có sẵn · văn viết",
           "类似小王这样的年轻人并非少数。",
           "昔日风光无限的世界一流企业也会亏损……这意味着，原本英明的决定今天看来可能并非如此了。",
           "不要怕犯错，不要害怕走弯路，犯些小错并非坏事，它会增加我们的心灵免疫力。"],
    say=["Điểm ngữ pháp thứ ba là 并非.",
         F(0, "并非 là động từ, nghĩa là 并不是, hoàn toàn không phải. Chữ 并 đứng trước từ phủ định 非 để làm cho ngữ khí phủ định mạnh hơn. Chữ 非 tương đương 不是."),
         F(1, "并非 thường dùng để phủ định một suy nghĩ hay nhận định mà người khác cho là đúng, mang màu sắc văn viết. Cả ba ví dụ sau đều lấy từ bài khóa."),
         F(2, "Ví dụ một: 类似小王这样的年轻人并非少数。 Những người trẻ giống như Tiểu Vương không hề ít. Người ta có thể nghĩ đó chỉ là số ít, tác giả phủ định điều đó."),
         F(3, "Ví dụ hai: 昔日风光无限的世界一流企业也会亏损，这意味着，原本英明的决定今天看来可能并非如此了。 Doanh nghiệp hàng đầu ngày xưa cũng có thể thua lỗ, điều này có nghĩa là quyết định vốn sáng suốt, nhìn từ hôm nay có thể không còn như vậy. 并非如此 là cụm rất hay gặp."),
         F(4, "Ví dụ ba: 不要怕犯错，不要害怕走弯路，犯些小错并非坏事，它会增加我们的心灵免疫力。 Mắc lỗi nhỏ không hề là chuyện xấu, nó sẽ tăng sức đề kháng cho tâm hồn chúng ta.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: dùng 并非 hoàn thành câu", reveal=True, size=36,
    items=["(1) 城里人心里的农村特别美，而农民眼中的农村却______。",
           "Đáp án: ……而农民眼中的农村却并非如此。",
           "(2) 原本以为他结婚了，就会安心过日子，可事实并非______，他还像个孩子似的，天天心里想的就是玩儿。",
           "Đáp án: ……可事实并非如此，……",
           "(3) 你以为我只是教训你吗？其实______，我是希望你______。",
           "Đáp án: 其实我并非只想教训你，我是希望你以后少犯错误。"],
    say=[F(0, "Luyện tập: dùng 并非 hoàn thành câu. Câu một: 城里人心里的农村特别美，而农民眼中的农村却什么。 Nông thôn trong lòng người thành phố đặc biệt đẹp, còn nông thôn trong mắt người nông dân thì sao? Các bạn tạm dừng và thử nhé."),
         F(1, "Đáp án gợi ý: 而农民眼中的农村却并非如此。 Còn nông thôn trong mắt người nông dân lại hoàn toàn không phải như vậy."),
         F(2, "Câu hai: 原本以为他结婚了，就会安心过日子，可事实并非什么，他还像个孩子似的，天天心里想的就是玩儿。 Vốn tưởng anh ta lấy vợ rồi sẽ yên tâm sống ổn định, nhưng sự thật lại không phải vậy, anh ta vẫn như một đứa trẻ, ngày nào cũng chỉ nghĩ đến chơi."),
         F(3, "Đáp án gợi ý: 可事实并非如此。 Nhưng sự thật hoàn toàn không phải như thế. Lại là cụm 并非如此."),
         F(4, "Câu ba: 你以为我只是教训你吗？其实什么，我是希望你什么。 Bạn tưởng tôi chỉ muốn dạy dỗ bạn sao? Thật ra thì sao, tôi mong bạn thế nào?"),
         F(5, "Đáp án gợi ý: 其实我并非只想教训你，我是希望你以后少犯错误。 Thật ra tôi hoàn toàn không phải chỉ muốn dạy dỗ bạn, tôi mong sau này bạn ít mắc lỗi hơn.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 日益 – 越来越", section="Phân biệt từ 词语辨析", title="Phân biệt 日益 và 越来越 (1): đi với động từ",
    common="Giống nhau: mức độ tăng dần theo thời gian, ngày một hơn. Ví dụ: 建立外交关系后，两国的往来日益/越来越密切。",
    cols=[{"head": "日益",
           "lines": ["Mang động từ hai âm tiết, không mang động từ một âm tiết",
                     "Đúng: 改革开放后，人们的生活状况日益改善。"]},
          {"head": "越来越",
           "lines": ["Mang rất ít động từ, đa số là động từ tâm lý: 喜欢、想、希望、盼望",
                     "Đúng: 我越来越喜欢周末去郊区玩儿了。",
                     "Sai: 人们的生活状况越来越改善。"]}],
    say=["Tiếp theo là phần phân biệt từ: 日益 và 越来越. Cả hai đều dịch là ngày càng, nên người học rất hay dùng lẫn lộn.",
         "Điểm giống nhau: cả hai đều biểu thị mức độ tăng dần theo thời gian, ngày sau hơn ngày trước. Ví dụ: 建立外交关系后，两国的往来日益密切, hoặc 越来越密切, đều đúng. Sau khi thiết lập quan hệ ngoại giao, quan hệ qua lại giữa hai nước ngày càng mật thiết.",
         F(0, "Điểm khác thứ nhất là về động từ. Sau 日益 có thể là động từ hai âm tiết, nhưng không dùng động từ một âm tiết. Ví dụ: 改革开放后，人们的生活状况日益改善。 Sau cải cách mở cửa, đời sống của người dân ngày càng được cải thiện."),
         F(1, "Còn sau 越来越, rất ít động từ đi được, đa số là động từ tâm lý như 喜欢，想，希望，盼望. Ví dụ: 我越来越喜欢周末去郊区玩儿了。 Tôi ngày càng thích cuối tuần ra ngoại ô chơi."),
         F(1, "Vì vậy câu 人们的生活状况越来越改善 là sai, vì 改善 không phải động từ tâm lý. Phải nói 日益改善, hoặc đổi thành 越来越好."),
         "Mẹo nhớ: 日益 là từ văn viết, thích đi với từ hai âm tiết; còn 越来越 là từ khẩu ngữ, chủ yếu đi với tính từ, chỉ đi với một số ít động từ tâm lý."])

add("compare", section="Phân biệt từ 词语辨析", title="Phân biệt 日益 và 越来越 (2): đi với tính từ",
    cols=[{"head": "日益",
           "lines": ["Mang tính từ hai âm tiết, không mang tính từ một âm tiết",
                     "Đúng: 最近几十年，人口问题日益严重。",
                     "Sai: 我的汉语水平日益高了。"]},
          {"head": "越来越",
           "lines": ["Mang tính từ với bất kỳ số âm tiết nào",
                     "Đúng: 天气越来越寒冷了。",
                     "Đúng: 天气越来越冷了。"]}],
    say=[F(0, "Điểm khác thứ hai là về tính từ. Sau 日益 có thể là tính từ hai âm tiết, nhưng không dùng tính từ một âm tiết. Ví dụ: 最近几十年，人口问题日益严重。 Mấy chục năm gần đây, vấn đề dân số ngày càng nghiêm trọng."),
         F(0, "Còn câu 我的汉语水平日益高了 là sai, vì 高 là tính từ một âm tiết. Phải nói 我的汉语水平日益提高, hoặc 我的汉语水平越来越高了."),
         F(1, "Sau 越来越 thì tính từ bao nhiêu âm tiết cũng được. Ví dụ: 天气越来越寒冷了。 và 天气越来越冷了。 Cả hai đều đúng: trời ngày càng lạnh."),
         "Tóm lại, khi phân vân, các bạn hãy đếm số âm tiết của từ phía sau. Từ một âm tiết thì chỉ dùng 越来越; động từ không phải động từ tâm lý thì dùng 日益."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: Đúng hay sai?", reveal=True, size=36,
    items=["(1) 城乡人民的消费水平日益提高，消费结构也发生了变化。",
           "Đáp án: Đúng – 日益 + động từ hai âm tiết 提高.",
           "(2) 大家普遍认为市场上销售的产品种类越来越增加了。",
           "Đáp án: Sai – 增加 không phải động từ tâm lý. Sửa: ……产品种类日益增加了 / 越来越多了。",
           "(3) 最近的一项调查显示世界各国的经济形势日益好了。",
           "Đáp án: Sai – 好 là tính từ một âm tiết. Sửa: ……经济形势越来越好了。",
           "(4) 受中国朋友的影响，我越来越喜欢东方文化了。",
           "Đáp án: Đúng – 越来越 + động từ tâm lý 喜欢."],
    say=[F(0, "Bây giờ chúng ta làm thử: phán đoán đúng sai. Câu một: 城乡人民的消费水平日益提高，消费结构也发生了变化。 Mức tiêu dùng của người dân thành thị và nông thôn ngày càng nâng cao, cơ cấu tiêu dùng cũng thay đổi. Đúng hay sai? Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: đúng. 提高 là động từ hai âm tiết, đi sau 日益 rất tự nhiên."),
         F(2, "Câu hai: 大家普遍认为市场上销售的产品种类越来越增加了。 Mọi người đều cho rằng chủng loại sản phẩm bán trên thị trường ngày càng tăng."),
         F(3, "Đáp án: sai. 增加 không phải là động từ tâm lý, nên không đi sau 越来越. Sửa thành 日益增加, hoặc 越来越多了."),
         F(4, "Câu ba: 最近的一项调查显示世界各国的经济形势日益好了。 Một cuộc điều tra gần đây cho thấy tình hình kinh tế các nước trên thế giới ngày càng tốt."),
         F(5, "Đáp án: sai. Trong 日益好了, tính từ chỉ có một âm tiết, nên không đi sau 日益. Sửa thành 越来越好了."),
         F(6, "Câu bốn: 受中国朋友的影响，我越来越喜欢东方文化了。 Chịu ảnh hưởng của bạn bè người Trung Quốc, tôi ngày càng thích văn hóa phương Đông."),
         F(7, "Đáp án: đúng. 喜欢 là động từ tâm lý, đi sau 越来越 hoàn toàn được.")])

# ======================= MỞ RỘNG: CÂU SAI TRẬT TỰ TỪ =======================
add("bullets", chapter="Mở rộng: trật tự từ sai", section="Mở rộng 扩展", title="Câu sai: trật tự từ không đúng (语序不当)", size=36,
    items=["Trật tự từ trong câu không đúng quy tắc ngữ pháp, hoặc không hợp thói quen tiếng Hán",
           "## Nguyên nhân thường gặp",
           "Định ngữ, trạng ngữ, tân ngữ đặt sai vị trí",
           "Định ngữ nhiều tầng, trạng ngữ nhiều tầng sắp xếp sai thứ tự",
           "Hư từ (phó từ, giới từ…) đặt sai vị trí",
           "Câu đặc biệt dễ sai: câu 是, câu 把, câu kiêm ngữ, câu 被, câu so sánh, từ ly hợp"],
    say=["Bây giờ chúng ta sang phần mở rộng của sách. Quyển Thượng không có mục tu từ riêng, thay vào đó là kỹ năng nhận biết câu sai. Bài trước các bạn đã học câu thiếu thành phần; hôm nay là câu sai do trật tự từ không đúng, tiếng Trung gọi là 语序不当.",
         F(0, "语序不当 là khi thứ tự các từ trong câu không đúng quy tắc ngữ pháp, hoặc không phù hợp với thói quen diễn đạt của tiếng Hán. Đây là lỗi người Việt rất hay mắc, vì trật tự từ tiếng Việt khác tiếng Trung khá nhiều."),
         F(1, "Sách nêu các nguyên nhân chính gây ra lỗi này."),
         F(2, "Thứ nhất, định ngữ, trạng ngữ, hoặc tân ngữ đặt sai vị trí."),
         F(3, "Thứ hai, khi có nhiều tầng định ngữ hay nhiều tầng trạng ngữ, sắp xếp sai thứ tự giữa chúng."),
         F(4, "Thứ ba, hư từ như phó từ, giới từ đặt sai vị trí."),
         F(5, "Thứ tư, khi dùng các câu đặc biệt như câu chữ 是, câu chữ 把, câu kiêm ngữ, câu chữ 被, câu so sánh, và khi dùng từ ly hợp, cũng rất dễ sai trật tự từ. Chúng ta cùng xem năm ví dụ của sách.")])

add("bullets", section="Mở rộng 扩展", title="Ví dụ câu sai trật tự từ (1)", size=34,
    items=["## (1) Trạng ngữ đặt sai vị trí",
           "Sai: 你不必给我打电话，已经别人给我打了。",
           "Sửa: ……别人已经给我打了。 (phó từ 已经 → giới từ 给我)",
           "## (2) Tân ngữ đặt sai vị trí",
           "Sai: 地形图上的川藏线弯弯曲曲，像极了高原反应时极速抖动的心电图谱。",
           "Sửa: ……和高原反应时极速抖动的心电图谱像极了。"],
    say=[F(0, "Ví dụ một: trạng ngữ đặt sai vị trí."),
         F(1, "Câu sai: 你不必给我打电话，已经别人给我打了。 Bạn không cần gọi điện cho tôi, đã có người khác gọi cho tôi rồi."),
         F(2, "Ở vế sau, 已经 và 给我 đều là trạng ngữ, phải đặt sau chủ ngữ và trước động từ. Thứ tự đúng là: chủ ngữ, rồi phó từ, rồi giới từ chỉ đối tượng: 别人已经给我打了。"),
         F(3, "Ví dụ hai: tân ngữ đặt sai vị trí."),
         F(4, "Câu sai: 地形图上的川藏线弯弯曲曲，像极了高原反应时极速抖动的心电图谱。 Tuyến đường Tứ Xuyên – Tây Tạng trên bản đồ địa hình ngoằn ngoèo, giống hệt điện tâm đồ rung giật dữ dội khi bị sốc độ cao."),
         F(5, "Cụm 像极了 có bổ ngữ 极了 nên không thể mang tân ngữ phía sau. Phải sửa thành 和高原反应时极速抖动的心电图谱像极了, tức là dùng 和心电图谱 để đưa đối tượng so sánh lên trước.")])

add("bullets", section="Mở rộng 扩展", title="Ví dụ câu sai trật tự từ (2)", size=36,
    items=["## (3) Chủ ngữ đặt sai vị trí",
           "Sai: 郑晓龙执导的很多电视剧，对中国人是不陌生的。",
           "Sửa: 中国人对郑晓龙执导的很多电视剧是不陌生的。",
           "## (4) Câu chữ 把 dạng phủ định",
           "Sai: 这事对她打击一定很大，她肯定会受不了，我把这事没告诉她。",
           "Sửa: ……我没把这事告诉她。 (từ phủ định đặt trước 把)"],
    say=[F(0, "Ví dụ ba: chủ ngữ đặt sai vị trí."),
         F(1, "Câu sai: 郑晓龙执导的很多电视剧，对中国人是不陌生的。 Nhiều bộ phim truyền hình do Trịnh Hiểu Long đạo diễn, đối với người Trung Quốc là không xa lạ."),
         F(2, "Nòng cốt câu là: người Trung Quốc không xa lạ với cái gì. Đối tượng của 不陌生 là các bộ phim. Vậy phải sửa: 中国人对郑晓龙执导的很多电视剧是不陌生的。"),
         F(3, "Ví dụ bốn: câu chữ 把 ở dạng phủ định."),
         F(4, "Câu sai: 这事对她打击一定很大，她肯定会受不了，我把这事没告诉她。 Chuyện này chắc chắn là cú sốc lớn với cô ấy, cô ấy nhất định không chịu nổi, nên tôi không nói chuyện này cho cô ấy."),
         F(5, "Trong câu chữ 把, từ phủ định phải đặt trước 把, không đặt trước động từ. Sửa: 我没把这事告诉她。 Đây là lỗi người Việt rất hay mắc, vì tiếng Việt nói tôi đem chuyện này không nói.")])

add("bullets", section="Mở rộng 扩展", title="Ví dụ câu sai trật tự từ (3)", size=36,
    items=["## (5) Từ ly hợp đi với số lượng từ",
           "Sai: 我们公司管理比较严格，没有特殊情况不准迟到早退，每两个星期一次开会。",
           "Sửa: ……每两个星期开一次会。 (开会 là từ ly hợp: 开 + 一次 + 会)"],
    say=[F(0, "Ví dụ năm: từ ly hợp đi với số lượng từ."),
         F(1, "Câu sai: 我们公司管理比较严格，没有特殊情况不准迟到早退，每两个星期一次开会。 Công ty chúng tôi quản lý khá nghiêm, không có trường hợp đặc biệt thì không được đi muộn về sớm, cứ hai tuần họp một lần."),
         F(2, "开会 là từ ly hợp, gồm động từ 开 và tân ngữ chỉ cuộc họp. Số lượng từ thường chen vào giữa động từ và tân ngữ. Sửa: 每两个星期开一次会。 Tương tự: 见一次面，洗个澡，帮个忙.")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chỉ ra lỗi và sửa lại (1)", reveal=True, size=36,
    items=["(1) 想着想着，他发怒起来。",
           "Đáp án: Từ ly hợp + 起来 → 想着想着，他发起怒来。",
           "(2) 她不但说了那样，而且也做了那样。",
           "Đáp án: Trạng ngữ sai vị trí → 她不但那样说了，而且也那样做了。",
           "(3) 她不是看书就是写文章，每天到深夜都忙。",
           "Đáp án: Trạng ngữ, bổ ngữ sai vị trí → ……每天都忙到深夜。"],
    say=[F(0, "Luyện tập: chỉ ra lỗi của các câu sau và đề xuất cách sửa. Câu một: 想着想着，他发怒起来。 Nghĩ mãi nghĩ mãi, anh ấy nổi giận lên. Câu này sai ở đâu? Các bạn tạm dừng và suy nghĩ nhé."),
         F(1, "Đáp án: 发怒 là từ ly hợp. Khi đi với bổ ngữ xu hướng 起来, tân ngữ 怒 phải chen vào giữa 起 và 来. Sửa: 想着想着，他发起怒来。 Giống như 唱起歌来，下起雨来."),
         F(2, "Câu hai: 她不但说了那样，而且也做了那样。 Cô ấy không những nói như vậy, mà còn làm như vậy."),
         F(3, "Đáp án: 那样 ở đây là trạng ngữ chỉ cách thức, phải đứng trước động từ. Sửa: 她不但那样说了，而且也那样做了。"),
         F(4, "Câu ba: 她不是看书就是写文章，每天到深夜都忙。 Cô ấy không đọc sách thì viết văn, ngày nào cũng bận đến đêm khuya."),
         F(5, "Đáp án: 每天都 phải đứng trước động từ 忙, còn 到深夜 là bổ ngữ, phải đứng sau động từ. Sửa: 每天都忙到深夜。")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chỉ ra lỗi và sửa lại (2)", reveal=True, size=36,
    items=["(4) 我想去一起喝茶和我的朋友。",
           "Đáp án: Trạng ngữ giới từ sai vị trí → 我想和我的朋友一起去喝茶。",
           "(5) 她很有绘画天赋，不光油画画得好，中国画也并比别人画得不差。",
           "Đáp án: Câu so sánh, phủ định sai vị trí → ……中国画也并不比别人画得差。"],
    say=[F(0, "Câu bốn: 我想去一起喝茶和我的朋友。 Tôi muốn đi uống trà cùng với bạn của tôi. Câu này sai ở đâu?"),
         F(1, "Đáp án: đây là lỗi điển hình của người Việt, vì tiếng Việt đặt cùng với bạn tôi ở cuối câu. Trong tiếng Trung, cụm giới từ 和我的朋友 cùng 一起 là trạng ngữ, phải đứng trước động từ. Sửa: 我想和我的朋友一起去喝茶。"),
         F(2, "Câu năm: 她很有绘画天赋，不光油画画得好，中国画也并比别人画得不差。 Cô ấy rất có năng khiếu hội họa, không chỉ vẽ tranh sơn dầu đẹp, mà tranh Trung Quốc cũng không vẽ kém hơn người khác."),
         F(3, "Đáp án: trong câu so sánh với 比, từ phủ định phải đặt trước 比. Sửa: 中国画也并不比别人画得差。 Mẹo: khi sửa câu sai trật tự từ, hãy tìm nòng cốt chủ ngữ, vị ngữ, tân ngữ trước, rồi đặt trạng ngữ vào trước động từ, bổ ngữ vào sau động từ.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ có dấu chấm", size=40,
    items=["热门 (门) → 冷门 · 专门 · 部门 · 门类",
           "伤脑筋 (伤) → 伤心 · 伤害 · 受伤 · 伤口",
           "致使 (致) → 导致 · 以致 · 致命 · 致富",
           "类似 (似) → 相似 · 似乎 · 近似 · 好似",
           "精确 (确) → 准确 · 正确 · 明确 · 确实"],
    say=["Phần luyện tập. Bài tập một: mô phỏng ví dụ, viết thêm các từ có chứa chữ được đánh dấu chấm.",
         F(0, "Ví dụ mẫu: 热门, chữ được đánh dấu là chữ thứ hai, nghĩa là cửa, hoặc ngành, loại. Ta có 冷门，专门，部门，门类. Tức là ngành ít người theo, chuyên môn, bộ phận, và chủng loại."),
         F(1, "伤脑筋, chữ được đánh dấu là chữ đầu, nghĩa là tổn thương. Ta có 伤心，伤害，受伤，伤口. Tức là đau lòng, làm tổn thương, bị thương, và vết thương."),
         F(2, "致使, chữ được đánh dấu là chữ đầu, nghĩa là dẫn đến. Ta có 导致，以致，致命，致富. Tức là dẫn đến, đến nỗi, chí mạng, và làm giàu."),
         F(3, "类似, chữ được đánh dấu là chữ thứ hai, nghĩa là giống. Ta có 相似，似乎，近似，好似. Tức là tương tự, dường như, gần giống, và giống như."),
         F(4, "精确, chữ được đánh dấu là chữ thứ hai, nghĩa là chắc chắn, đúng. Ta có 准确，正确，明确，确实. Tức là chuẩn xác, đúng đắn, rõ ràng, và quả thực.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (1)", reveal=True, size=36,
    items=["(1) 因为地址不清楚，所以信件无法送达。（致使）",
           "Đáp án: 由于地址不清楚，致使信件无法送达。",
           "(2) 满18岁就代表着成人了，要承担起成年人的义务和责任。（意味着）",
           "Đáp án: 满18岁就意味着成人了，要承担起成年人的义务和责任。",
           "(3) 真相其实跟你想象的完全不同。（并非）",
           "Đáp án: 真相并非你想象的那样。"],
    say=[F(0, "Bài tập hai: dùng từ cho sẵn để viết lại câu. Câu một, dùng 致使: 因为地址不清楚，所以信件无法送达。 Vì địa chỉ không rõ ràng, nên thư không thể gửi đến nơi. Các bạn tạm dừng và thử viết lại nhé."),
         F(1, "Đáp án: 由于地址不清楚，致使信件无法送达。 Do địa chỉ không rõ ràng, đến nỗi thư không gửi đến được. 致使 thay cho 所以, và kết quả là điều không mong muốn."),
         F(2, "Câu hai, dùng 意味着: 满十八岁就代表着成人了，要承担起成年人的义务和责任。 Đủ mười tám tuổi là đã thành người lớn, phải gánh vác nghĩa vụ và trách nhiệm của người trưởng thành."),
         F(3, "Đáp án: thay 代表着 bằng 意味着: 满十八岁就意味着成人了。 Đủ mười tám tuổi có nghĩa là đã trưởng thành."),
         F(4, "Câu ba, dùng 并非: 真相其实跟你想象的完全不同。 Sự thật thật ra hoàn toàn khác với những gì bạn tưởng tượng."),
         F(5, "Đáp án: 真相并非你想象的那样。 Sự thật hoàn toàn không phải như bạn tưởng tượng.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (2)", reveal=True, size=36,
    items=["(4) 我们应该勇敢地承认自己的错误。（勇于）",
           "Đáp án: 我们应该勇于承认自己的错误。",
           "(5) 随着他的压力越来越大，他的精神越来越紧张。（伴随）",
           "Đáp án: 伴随着压力越来越大，他的精神越来越紧张。",
           "(6) 随着经济的发展，城市里汽车的数量越来越多。（日益）",
           "Đáp án: 随着经济的发展，城市里汽车的数量日益增多。"],
    say=[F(0, "Câu bốn, dùng 勇于: 我们应该勇敢地承认自己的错误。 Chúng ta nên dũng cảm thừa nhận sai lầm của mình."),
         F(1, "Đáp án: 我们应该勇于承认自己的错误。 勇于 thay cho 勇敢地, phía sau là động từ 承认."),
         F(2, "Câu năm, dùng 伴随: 随着他的压力越来越大，他的精神越来越紧张。 Cùng với áp lực ngày càng lớn, tinh thần anh ấy ngày càng căng thẳng."),
         F(3, "Đáp án: 伴随着压力越来越大，他的精神越来越紧张。 伴随着 thay cho 随着, giống câu trong bài: 伴随着经济全球化."),
         F(4, "Câu sáu, dùng 日益: 随着经济的发展，城市里汽车的数量越来越多。 Cùng với sự phát triển kinh tế, số lượng ô tô trong thành phố ngày càng nhiều."),
         F(5, "Đáp án: 城市里汽车的数量日益增多。 Chú ý: không nói 日益多, vì 多 là tính từ một âm tiết; phải dùng động từ hai âm tiết 增多, đúng như quy tắc chúng ta vừa học.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (1)", reveal=True, size=34,
    items=["## Từ cho sẵn: 成本 · 及早 · 顾虑 · 伤脑筋 · 称心如意",
           "最近，我在为租房子的事情___，离单位近的吧，太贵了；便宜的吧，每天花在路上的时间要三四个小时，时间___太高了。……朋友劝我：“现在想找一个___的房子本来就很难，如果你再___重重，就更找不到房子了。……我看你还是___决定吧，省得将来后悔。”",
           "Đáp án: 伤脑筋 · 成本 · 称心如意 · 顾虑 · 及早"],
    say=[F(0, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn một có năm từ: 成本，及早，顾虑，伤脑筋，称心如意."),
         F(1, "最近，我在为租房子的事情什么，离单位近的吧，太贵了；便宜的吧，每天花在路上的时间要三四个小时，时间什么太高了。一个人住吧，不安全；跟别人合租吧，又怕有矛盾。见此情形，朋友劝我：现在想找一个什么的房子本来就很难，如果你再什么重重，就更找不到房子了。你前两天看的那个房子就不错，我看你还是什么决定吧，省得将来后悔。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 为租房子的事情伤脑筋，时间成本太高了，一个称心如意的房子，再顾虑重重，还是及早决定吧。 Dạo này tôi đau đầu chuyện thuê nhà: gần cơ quan thì đắt quá; rẻ thì mỗi ngày mất ba bốn tiếng đi đường, chi phí thời gian quá cao. Bạn tôi khuyên: tìm được căn nhà như ý vốn đã khó, nếu cậu còn lo lắng đủ đường thì càng không tìm được. Tớ thấy cậu nên sớm quyết định đi, kẻo sau này hối hận.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (2)", reveal=True, size=36,
    items=["## Từ cho sẵn: 畏惧 · 意志 · 挫折 · 机遇 · 勇于",
           "人们常说：“失败是成功之母”。人的一生中总会遇到一些___，只有不___失败，___面对困难，才会在实践中获得经验，增强___力，进而抓住___，获得成功。",
           "Đáp án: 挫折 · 畏惧 · 勇于 · 意志 · 机遇"],
    say=[F(0, "Đoạn hai có năm từ: 畏惧，意志，挫折，机遇，勇于."),
         F(1, "人们常说：失败是成功之母。人的一生中总会遇到一些什么，只有不什么失败，什么面对困难，才会在实践中获得经验，增强什么力，进而抓住什么，获得成功。 Các bạn điền thử nhé."),
         F(2, "Đáp án: 遇到一些挫折，只有不畏惧失败，勇于面对困难，增强意志力，进而抓住机遇。 Người ta thường nói thất bại là mẹ thành công. Đời người luôn gặp những vấp ngã, chỉ có không sợ thất bại, dám đối mặt khó khăn, mới có thể tích lũy kinh nghiệm trong thực tiễn, tăng cường ý chí, từ đó nắm bắt thời cơ và thành công."),
         "Các bạn thấy không, đoạn văn này chính là tóm tắt tinh thần của bài khóa: đừng sợ thất bại, vì thất bại giúp chúng ta trưởng thành."])

add("bullets", section="Luyện tập 练习", title="Bài tập 4: Câu ví von (比喻) – mô phỏng đặt câu", reveal=True, size=34,
    items=["(1) 男人是山，女人是水。 → Đáp án: 男人是大树，女人是阳光。",
           "(2) 漂亮的姑娘像花儿一样。 → Đáp án: 漂亮的姑娘像一幅美丽的画。",
           "(3) 月亮像一个银色的盘子挂在天空上。 → Đáp án: 月亮像一只弯弯的小船。",
           "(4) 一闪一闪的星星像调皮的孩子眨着眼睛。 → Đáp án: 星星像一颗颗宝石在夜空中闪光。",
           "(5) 他急得像热锅上的蚂蚁。 → Đáp án: 他急得像被困在笼子里的狮子。"],
    say=[F(0, "Bài tập bốn. Trong bài khóa có câu 不要害怕走弯路, đừng sợ đi đường vòng. Đây là một cách nói ví von, tiếng Trung gọi là 比喻. Sách yêu cầu đọc các câu ví von sau và mô phỏng đặt câu. Câu một: 男人是山，女人是水。 Đàn ông là núi, phụ nữ là nước. Đây là ẩn dụ, dùng chữ 是. Gợi ý: 男人是大树，女人是阳光。 Đàn ông là cây lớn, phụ nữ là ánh nắng."),
         F(1, "Câu hai: 漂亮的姑娘像花儿一样。 Cô gái xinh đẹp như một bông hoa. Đây là so sánh, dùng mẫu 像……一样. Gợi ý: 漂亮的姑娘像一幅美丽的画。 Cô gái xinh đẹp như một bức tranh tuyệt đẹp."),
         F(2, "Câu ba: 月亮像一个银色的盘子挂在天空上。 Mặt trăng như một chiếc đĩa bạc treo trên bầu trời. Đó là trăng tròn. Gợi ý cho trăng khuyết: 月亮像一只弯弯的小船。 Mặt trăng như một chiếc thuyền nhỏ cong cong."),
         F(3, "Câu bốn: 一闪一闪的星星像调皮的孩子眨着眼睛。 Những ngôi sao lấp lánh như những đứa trẻ tinh nghịch đang chớp mắt. Gợi ý: 星星像一颗颗宝石在夜空中闪光。 Các vì sao như từng viên đá quý lấp lánh trên bầu trời đêm."),
         F(4, "Câu năm: 他急得像热锅上的蚂蚁。 Anh ấy cuống như kiến bò chảo nóng. Gợi ý: 他急得像被困在笼子里的狮子。 Anh ấy sốt ruột như con sư tử bị nhốt trong lồng. Các bạn hãy tự đặt thêm câu của mình nhé.")])

add("bullets", section="Luyện tập 练习", title="Mở rộng 扩展: các cặp từ gần nghĩa", size=36,
    items=["取缔 – 取消 hủy bỏ, cấm · 生疏 – 疏远 xa lạ, lạnh nhạt · 惋惜 – 可惜 tiếc",
           "诬陷 – 陷害 vu hãm, hãm hại · 羞耻 – 耻辱 xấu hổ, nhục nhã",
           "削弱 – 减弱 suy yếu, làm yếu đi · 遗失 – 丢失 đánh mất",
           "遭殃 – 倒霉 gặp tai họa, xui xẻo · 镇定 – 冷静 bình tĩnh",
           "自满 – 骄傲 tự mãn, kiêu ngạo · 宰 – 杀 giết (gia súc) · 请柬 – 请帖 thiệp mời",
           "公正 – 公平 công bằng · 揍 – 打 đánh"],
    say=["Phần mở rộng thứ hai của sách giới thiệu mười bốn cặp từ gần nghĩa. Thầy đọc qua để các bạn làm quen; khi gặp trong bài đọc, các bạn sẽ nhận ra ngay.",
         F(0, "取缔，取消: hủy bỏ; trong đó 取缔 là cấm hẳn, xóa bỏ một hoạt động trái phép. 生疏，疏远: xa lạ, lạnh nhạt. 惋惜，可惜: tiếc nuối."),
         F(1, "诬陷，陷害: vu oan, hãm hại. 羞耻，耻辱: xấu hổ, nhục nhã."),
         F(2, "削弱，减弱: làm suy yếu, yếu đi. 遗失，丢失: đánh mất, làm mất."),
         F(3, "遭殃，倒霉: gặp tai họa, xui xẻo. 镇定，冷静: bình tĩnh."),
         F(4, "自满，骄傲: tự mãn, kiêu ngạo. 宰，杀: giết, thường nói về gia súc, gia cầm. 请柬，请帖: thiệp mời."),
         F(5, "公正，公平: công bằng, công tâm. 揍，打: đánh; 揍 là khẩu ngữ. Các cặp từ này nghĩa gần nhau nhưng sắc thái và cách kết hợp có khác biệt, các bạn hãy tra từ điển và đặt câu với từng từ nhé.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 7", size=36,
    items=["Từ vựng trọng tâm: 伤脑筋 · 擅长 · 顾虑 · 过度 · 悔恨 · 挫折 · 勇于 · 日益 · 意味着 · 称心如意 · 争先恐后 · 机遇",
           "Ngữ pháp: 于 (thời gian, nơi chốn; phương diện, nguyên nhân) · 致使 (khiến cho, đến nỗi) · 并非 (hoàn toàn không phải)",
           "Phân biệt: 日益 (từ hai âm tiết) ≠ 越来越 (tính từ bất kỳ; động từ tâm lý)",
           "Mở rộng: câu sai do trật tự từ không đúng (语序不当)",
           "## Bài tập về nhà (运用)",
           "Viết bài ít nhất 300 chữ với đề 判断力来自哪里, kể một lần bạn phải ra quyết định"],
    say=["Chúng ta cùng tổng kết bài bảy.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 伤脑筋，擅长，顾虑，过度，悔恨，挫折，勇于，日益，意味着，称心如意，争先恐后，机遇. Và đừng quên những từ dễ nhầm như 过度，危机，机遇，心灵."),
         F(1, "Về ngữ pháp: 于 là giới từ văn viết, chỉ thời gian, nơi chốn, hoặc phương diện, nguyên nhân, mục đích. 致使 là động từ hoặc liên từ, nghĩa là khiến cho, đến nỗi, kết quả thường không tốt. 并非 nghĩa là hoàn toàn không phải, tăng cường ngữ khí phủ định."),
         F(2, "Về phân biệt từ: 日益 đi với động từ hoặc tính từ hai âm tiết; còn 越来越 đi với tính từ bao nhiêu âm tiết cũng được, nhưng chỉ đi với một số ít động từ tâm lý."),
         F(3, "Về phần mở rộng: câu sai do trật tự từ không đúng, như trạng ngữ, tân ngữ, chủ ngữ đặt sai chỗ, phủ định trong câu chữ 把 và câu so sánh, và từ ly hợp đi với số lượng từ."),
         F(5, "Bài tập về nhà, theo phần vận dụng của sách: bài khóa cho chúng ta biết, phán đoán nhạy bén đến từ thực tiễn và vấp ngã. Hãy viết một bài ít nhất ba trăm chữ với đề 判断力来自哪里, phán đoán đến từ đâu. Gợi ý: bạn từng do dự khi làm việc gì? Điều gì giúp bạn quyết định? Sự thật chứng minh quyết định ấy đúng hay sai? Bạn hiểu ra đạo lý gì? Nhớ thử dùng 于，致使，并非 trong bài viết nhé."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Đừng sợ sai, vì mỗi lần sai là một lần các bạn trưởng thành hơn. Hẹn gặp lại các bạn ở bài tám: 遇见原来的我, Gặp lại tôi của ngày xưa. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Thượng) – Bài 7: 我的人生我做主 (Tôi làm chủ cuộc đời tôi)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"正为工作": "正位工作",      # wèi
                    "为此": "位此",              # wèicǐ
                    "为自己": "位自己",          # wèi
                    "为一件事情": "位一件事情",  # wèi
                    "为租房子": "位租房子",      # wèi
                    "为某事": "位某事",          # wèi
                    "会计": "快计",              # kuàijì
                    "擅长": "擅常",              # shàncháng
                    "长于": "常于",              # chángyú
                    "顾虑重重": "顾虑虫虫",      # chóngchóng
                    "成长": "成涨",              # chéngzhǎng
                    "积累": "积垒",              # jīlěi
                    "称心": "趁心",              # chènxīn
                    "倒闭": "岛闭",              # dǎobì
                    "削弱": "薛弱",              # xuēruò
                    "请帖": "请铁",              # qǐngtiě
                    "调皮": "条皮",              # tiáopí
                    "川藏": "川葬",              # Chuān-Zàng
                    "孩子似的": "孩子是的",      # shìde
                    "得不差": "得不岔",          # bù chà
                    "画得差": "画得岔",          # chà
                    "语序不当": "语序不荡"},      # bùdàng
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai07.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
