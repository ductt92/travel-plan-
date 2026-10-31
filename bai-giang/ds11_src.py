#!/usr/bin/env python3
"""Kịch bản bài giảng 顶石中文 – Bài 1.1 «没有高考，你怎么拼得过富二代？». Chạy để sinh ds11.json."""
import json
import os

TAG = "顶石中文 · Bài 1.1 · 没有高考，你怎么拼得过富二代？"
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
    zh="没有高考", py="你怎么拼得过富二代？",
    vi="Bài 1.1: Không thi đại học, sao đua nổi con nhà giàu?",
    sub="Méiyǒu gāokǎo, nǐ zěnme pīn de guò fù'èrdài?\nBài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng giáo trình 顶石中文, Đỉnh cao tiếng Trung, một giáo trình tổng hợp tiếng Hán cao cấp.",
         "Hôm nay chúng ta bắt đầu Đơn vị một, 教育篇, chủ đề Giáo dục, với bài một chấm một: 没有高考，你怎么拼得过富二代？ Nghĩa là: Không có thi đại học, bạn làm sao đua nổi con nhà giàu?",
         "Bài khóa được cải biên từ chương trình phỏng vấn 我们, tác giả là 白岩松, nhà báo và người dẫn chương trình nổi tiếng của Đài truyền hình Trung ương Trung Quốc. Ông kể về kỳ thi đại học của chính mình, về chuyến làm phim ở ngôi trường được gọi là công xưởng luyện thi lớn nhất châu Á, và vì sao ông tin rằng thi đại học vẫn có thể thay đổi số phận của con nhà nghèo.",
         "Khác với giáo trình HSK, các bài khóa của 顶石中文 là những bài nghị luận, bình luận về các vấn đề xã hội. Ngoài từ vựng, chúng ta sẽ học cách lập luận và bày tỏ quan điểm bằng tiếng Trung."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài khóa: ý nghĩa của kỳ thi đại học (高考) đối với con nhà nghèo",
           "Nắm vững 45 từ mới (41 từ trong sách + 4 từ bổ sung), kèm âm Hán Việt và ví dụ",
           "11 mẫu câu trọng điểm: 按说 · 未免 · 换一个角度 · 不只是……更是…… · 历来 · 稍稍 · 偏偏 · 反倒 · 并非 · 无论如何……都 · 相反的是",
           "Kết hợp từ (词语搭配) và 3 thành ngữ",
           "Luyện tập, thảo luận và liên hệ với kỳ thi tốt nghiệp THPT ở Việt Nam"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa: vì sao tác giả nói thi đại học là con đường quan trọng để con nhà nghèo thay đổi số phận."),
         F(1, "Thứ hai, nắm vững bốn mươi lăm từ mới: bốn mươi mốt từ trong sách và bốn từ thầy bổ sung từ bài khóa. Với mỗi từ, thầy sẽ đọc mẫu, cho âm Hán Việt, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học mười một mẫu câu trọng điểm, như 按说, theo lẽ thường mà nói; 未免, thật là hơi quá; 偏偏, lại cứ; 反倒, trái lại; và 无论如何……都, dù thế nào cũng."),
         F(3, "Thứ tư, học các kết hợp từ thường gặp và ba thành ngữ của bài."),
         F(4, "Cuối cùng, chúng ta làm bài tập, thảo luận, và liên hệ với kỳ thi tốt nghiệp trung học phổ thông ở Việt Nam. Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé.")])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 课前思考", title="Khởi động: Suy nghĩ trước khi học (课前思考)", reveal=True, size=34,
    items=["(1) 你觉得考生选择大学、报考志愿时，会考虑哪些因素？",
           "Đáp án gợi ý: 学校的名气和排名、专业、地区、学费、就业前景，还有自己的兴趣。",
           "(2) 在你们国家，进入大学的途径有哪些？",
           "Đáp án gợi ý: 在越南，可以用高中毕业考试的成绩、高中的学习成绩、能力评估考试的成绩申请大学，优秀学生还可以被保送。",
           "(3) 你知道中国的大学考试曾中断过吗？原因是什么？后来又为什么恢复？",
           "Đáp án gợi ý: 中断过。1966年因为“文化大革命”停止了十余年；1977年恢复，让人人都能凭考试公平竞争，国家也需要选拔人才。"],
    say=["Chúng ta bắt đầu bằng phần 课前思考, suy nghĩ trước khi học. Sách đưa ra ba câu hỏi. Các bạn hãy tạm dừng video, tự trả lời bằng tiếng Trung trước, rồi nghe đáp án gợi ý nhé.",
         F(0, "Câu một: 你觉得考生选择大学、报考志愿时，会考虑哪些因素？ Theo bạn, khi chọn trường đại học và đăng ký nguyện vọng, thí sinh sẽ cân nhắc những yếu tố nào?"),
         F(1, "Đáp án gợi ý: 学校的名气和排名、专业、地区、学费、就业前景，还有自己的兴趣。 Danh tiếng và thứ hạng của trường, ngành học, khu vực, học phí, triển vọng việc làm, và sở thích của bản thân. Từ 志愿 ở đây là nguyện vọng đăng ký, lát nữa chúng ta sẽ gặp trong bài khóa."),
         F(2, "Câu hai: 在你们国家，进入大学的途径有哪些？ Ở nước bạn, có những con đường nào để vào đại học?"),
         F(3, "Đáp án gợi ý: 在越南，可以用高中毕业考试的成绩、高中的学习成绩、能力评估考试的成绩申请大学，优秀学生还可以被保送。 Ở Việt Nam có thể xét tuyển bằng điểm thi tốt nghiệp trung học phổ thông, bằng học bạ, bằng điểm thi đánh giá năng lực; học sinh xuất sắc còn được tuyển thẳng, tiếng Trung gọi là 保送."),
         F(4, "Câu ba: 你知道中国的大学考试曾中断过吗？原因是什么？后来又为什么恢复？ Bạn có biết kỳ thi đại học của Trung Quốc từng bị gián đoạn không? Vì sao? Sau đó vì sao lại được khôi phục?"),
         F(5, "Đáp án gợi ý: có. Từ năm một chín sáu sáu, do Cách mạng Văn hóa, kỳ thi đại học bị bãi bỏ hơn mười năm; năm một chín bảy bảy, kỳ thi được khôi phục, để mọi người đều có thể cạnh tranh công bằng bằng thi cử, và đất nước cũng cần tuyển chọn nhân tài. Sự kiện này chính là câu chuyện mở đầu của bài khóa.")])

add("bullets", section="Khởi động 课前思考", title="Bối cảnh: tác giả và các khái niệm (注释)", size=33,
    items=["白岩松 (1968–): nhà báo, MC của Đài truyền hình Trung ương; năm 1985 thi đỗ Học viện Phát thanh Bắc Kinh (nay là 中国传媒大学)",
           "毛坦厂中学 (An Huy): trường cấp ba quy mô cực lớn, quản lý kiểu quân đội, tỷ lệ đỗ cao – “亚洲最大高考工厂”",
           "Phụ huynh coi cây liễu trăm tuổi trước trường là “老神树”, thắp hương khấn vái trước kỳ thi",
           "高考名校: trường cấp ba có tỷ lệ đỗ đại học cao, nhiều học sinh vào trường danh tiếng",
           "富一代 → 富二代 (富家子弟): con cái thế hệ doanh nhân giàu lên sau cải cách mở cửa",
           "官二代 (官家子弟): con cái của người làm quan to, nhiều quyền lực"],
    say=["Trước khi học từ mới, chúng ta tìm hiểu bối cảnh qua phần chú thích, 注释, của sách.",
         F(0, "Tác giả 白岩松 sinh năm một chín sáu tám ở Nội Mông, là nhà báo, người dẫn chương trình và nhà văn. Năm một chín tám lăm, ông thi đỗ với thành tích xuất sắc vào khoa Báo chí của Học viện Phát thanh Bắc Kinh, nay là Đại học Truyền thông Trung Quốc, 中国传媒大学. Ông từng tham gia truyền hình trực tiếp sự kiện Hồng Kông trở về Trung Quốc năm một chín chín bảy."),
         F(1, "毛坦厂中学 là trường trung học Mao Thản Xưởng, nằm sâu trong vùng núi Đại Biệt, tỉnh An Huy. Trường có quy mô khổng lồ, quản lý kiểu quân đội, tỷ lệ đỗ đại học cao, nên được gọi là 亚洲最大高考工厂, công xưởng luyện thi đại học lớn nhất châu Á. Mỗi mùa thi, hàng vạn phụ huynh tiễn con đi thi."),
         F(2, "Trường có một cây liễu hơn trăm tuổi, phụ huynh gọi là 老神树, cây thần. Mỗi năm trước kỳ thi, họ đứng cách tường rào thắp hương khấn vái, mong con thi cử thuận lợi, 金榜题名, đỗ đạt cao."),
         F(3, "高考名校 là những trường cấp ba có tỷ lệ đỗ đại học cao, nhiều học sinh vào trường danh tiếng, thường là trường trọng điểm của tỉnh, thành phố, được chính sách địa phương ưu ái."),
         F(4, "Lớp doanh nhân tư nhân đầu tiên giàu lên sau cải cách mở cửa được gọi là 富一代, thế hệ giàu thứ nhất. Con cái họ thừa kế tài sản nên được gọi là 富二代, còn gọi là 富家子弟, con nhà giàu."),
         F(5, "Còn con cái của những người làm quan to, nhiều quyền lực, thì gọi là 官家子弟 hoặc 官二代. Nắm được mấy khái niệm này, các bạn sẽ hiểu bài khóa dễ hơn nhiều.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("富二代", "fù'èrdài", "phú nhị đại", "danh từ", "con nhà giàu (thế hệ thứ hai của nhà giàu)", "他是个富二代，从来不用为钱发愁。", "Anh ta là con nhà giàu, chưa bao giờ phải lo chuyện tiền bạc.",
     "Danh từ, chỉ con cái của những người có rất nhiều của cải. 富 là giàu, 二代 là thế hệ thứ hai. Tên bài là 没有高考，你怎么拼得过富二代."),
    ("按说", "ànshuō", "án thuyết", "phó từ", "theo lẽ thường mà nói, lẽ ra", "按说他早该到了，怎么还没来？", "Theo lẽ thì anh ấy phải đến từ lâu rồi, sao vẫn chưa tới?",
     "Phó từ, nghĩa là dựa theo sự thật và lẽ thường mà nói. Vế sau thường có 可是 hoặc 却, nêu thực tế trái ngược. Gần nghĩa với 按理说. Đây là mẫu câu trọng điểm đầu tiên của bài."),
    ("未免", "wèimiǎn", "vị miễn", "phó từ", "thật là, không thể không nói là (hơi quá)", "你这样说未免太过分了。", "Cậu nói như vậy thì thật là quá đáng.",
     "Phó từ, dùng khi người nói thấy việc gì đó hơi quá mức, mang ý không tán thành một cách nhẹ nhàng. Thường đi với 太，过于，有点儿. Trong bài: 这样的说法未免过于绝对."),
    ("尊严", "zūnyán", "tôn nghiêm", "danh từ", "phẩm giá, lòng tự trọng", "每个人都有自己的尊严。", "Mỗi người đều có phẩm giá của riêng mình.",
     "Danh từ, chỉ địa vị và thân phận đáng được tôn trọng. Hay gặp 国家尊严，人格尊严. Chú ý: tiếng Việt tôn nghiêm thường chỉ vẻ trang nghiêm, như chốn tôn nghiêm; còn 尊严 chủ yếu là phẩm giá. Trong bài: 对于公平、尊严的梦想."),
    ("历来", "lìlái", "lịch lai", "phó từ", "từ trước đến nay, xưa nay", "中国人历来重视教育。", "Người Trung Quốc xưa nay luôn coi trọng giáo dục.",
     "Phó từ thời gian, nghĩa là suốt nhiều năm qua, từ trước đến nay, gần nghĩa với 从来 nhưng mang màu sắc văn viết hơn. Hay gặp 历来如此, xưa nay vẫn vậy."),
    ("流传", "liúchuán", "lưu truyền", "động từ", "lưu truyền, truyền lại", "这个故事在民间流传很广。", "Câu chuyện này được lưu truyền rộng rãi trong dân gian.",
     "Động từ, nghĩa là truyền lại hoặc truyền đi rộng rãi, âm Hán Việt và nghĩa giống tiếng Việt. Trong bài: 中国历来流传着一句话."),
    ("稍稍", "shāoshāo", "sảo sảo", "phó từ", "hơi, một chút", "请稍稍等一下。", "Xin vui lòng chờ một chút.",
     "Phó từ mức độ, nghĩa là hơi, một chút, giống 稍微. Trong bài: 应该稍稍对前面的话加以改动, nên sửa câu nói ở trên một chút."),
    ("改动", "gǎidòng", "cải động", "động từ", "sửa đổi, thay đổi (câu chữ, hạng mục, thứ tự)", "这篇文章我只改动了几个字。", "Bài văn này tôi chỉ sửa vài chữ.",
     "Động từ, nghĩa là sửa đổi một phần câu chữ, hạng mục hay thứ tự. Mẫu trong bài: 对……加以改动, tiến hành sửa đổi cái gì, mang màu sắc văn viết."),
    ("学子", "xuézǐ", "học tử", "danh từ", "học trò, người đi học (văn viết)", "每年都有上千万学子参加高考。", "Mỗi năm có hơn chục triệu sĩ tử tham gia thi đại học.",
     "Danh từ văn viết, chỉ học sinh, sinh viên. Thành ngữ 莘莘学子 nghĩa là đông đảo học trò. Trong bài, tác giả sửa câu nổi tiếng thành 国家兴亡，学子有路，匹夫有责."),
    ("科目", "kēmù", "khoa mục", "danh từ", "môn học, môn thi", "高考一共考几个科目？", "Thi đại học thi tất cả mấy môn?",
     "Danh từ, chỉ tên các môn học, môn thi trong nhà trường. Hay gặp 考试科目. Trong bài: 当年我所有的科目都是满分."),
    ("满分", "mǎnfēn", "mãn phân", "danh từ", "điểm tối đa", "这次数学考试他得了满分。", "Bài thi toán lần này cậu ấy được điểm tối đa.",
     "Danh từ, nghĩa là điểm cao nhất theo quy định, như điểm mười ở Việt Nam. Hay gặp 得满分，打满分."),
    ("文科", "wénkē", "văn khoa", "danh từ", "khối khoa học xã hội, ban xã hội", "我上高中时选的是文科。", "Hồi cấp ba tôi chọn ban xã hội.",
     "Danh từ, chỉ chung các ngành văn học, lịch sử, triết học, kinh tế. Đối lập là 理科, khối tự nhiên. Trước đây, học sinh cấp ba ở Trung Quốc chia ban văn và ban lý để thi đại học."),
    ("状元", "zhuàngyuán", "trạng nguyên", "danh từ", "trạng nguyên; thủ khoa", "她是我们省的高考状元。", "Cô ấy là thủ khoa thi đại học của tỉnh chúng tôi.",
     "Danh từ. Thời khoa cử là người đỗ đầu kỳ thi Đình, giống trạng nguyên của Việt Nam; ngày nay chỉ người đứng đầu một kỳ thi: 高考状元，文科状元. Trong bài, vợ tác giả là 镇江文科状元, thủ khoa khối xã hội của Trấn Giang."),
    ("偏偏", "piānpiān", "thiên thiên", "phó từ", "lại cứ, cố tình, khăng khăng", "别人都同意，他偏偏反对。", "Ai cũng đồng ý, anh ta lại cứ phản đối.",
     "Phó từ, biểu thị cố ý làm trái với yêu cầu khách quan hoặc tình hình thực tế. Hay đi với 明明 ở vế trước. Đây là một mẫu câu trọng điểm của bài."),
    ("反倒", "fǎndào", "phản đảo", "phó từ", "trái lại, ngược lại", "雨没停，反倒越下越大了。", "Mưa không tạnh, trái lại càng lúc càng to.",
     "Phó từ ngữ khí, nghĩa là trái lại, giống 反而: kết quả ngược với lẽ thường hay điều dự đoán. Chữ thứ hai đọc thanh bốn. Trong bài: 这反倒说明……"),
    ("持", "chí", "trì", "động từ", "giữ, mang (quan điểm, thái độ)", "我对这件事持反对态度。", "Tôi giữ thái độ phản đối đối với việc này.",
     "Động từ văn viết, nghĩa là giữ, có một quan điểm hay thái độ nào đó. Mẫu: 持……态度，持……观点. Hán Việt là trì, như trong duy trì, kiên trì. Trong bài: 我持中立态度."),
    ("中立", "zhōnglì", "trung lập", "tính từ", "trung lập", "在这个问题上，我保持中立。", "Về vấn đề này, tôi giữ trung lập.",
     "Tính từ, nghĩa là đứng giữa hai bên đối lập, không nghiêng về bên nào. Hay gặp 中立国，中立态度."),
    ("赞赏", "zànshǎng", "tán thưởng", "động từ", "khen ngợi, đánh giá cao", "他的想法得到了老师的赞赏。", "Ý tưởng của cậu ấy được thầy giáo khen ngợi.",
     "Động từ, nghĩa là ca ngợi và thưởng thức, đánh giá cao. Hay gặp 得到赞赏，赞赏的目光, ánh mắt tán thưởng."),
    ("官家子弟", "guānjiā zǐdì", "quan gia tử đệ", "cụm danh từ", "con nhà quan", "他是官家子弟，从小生活条件很好。", "Anh ta là con nhà quan, từ nhỏ đã có điều kiện sống rất tốt.",
     "Cụm danh từ, chỉ con cái của những người làm quan to, có nhiều quyền lực, còn gọi là 官二代."),
    ("富家子弟", "fùjiā zǐdì", "phú gia tử đệ", "cụm danh từ", "con nhà giàu", "这所学校有不少富家子弟。", "Ngôi trường này có không ít con nhà giàu.",
     "Cụm danh từ, chỉ con cái của những gia đình có nhiều của cải, tức là 富二代."),
    ("子弟", "zǐdì", "tử đệ", "danh từ", "con em, lớp hậu bối", "这是一所职工子弟学校。", "Đây là trường dành cho con em công nhân viên chức.",
     "Danh từ, chỉ lớp con em, thế hệ trẻ. Hay gặp 职工子弟，干部子弟. Tiếng Việt cũng nói con em, tử đệ."),
    ("门槛", "ménkǎn", "môn hạm", "danh từ", "ngưỡng cửa; tiêu chuẩn, điều kiện vào", "这家公司招聘的门槛很高。", "Ngưỡng tuyển dụng của công ty này rất cao.",
     "Danh từ, nghĩa gốc là bậc cửa, nghĩa bóng là tiêu chuẩn, điều kiện để bước vào một phạm vi nào đó. Hay gặp 门槛高，降低门槛. Tiếng Việt cũng nói ngưỡng cửa."),
    ("并非", "bìngfēi", "tịnh phi", "động từ", "hoàn toàn không phải", "事情并非你想的那样。", "Sự việc hoàn toàn không phải như cậu nghĩ.",
     "Động từ, nghĩa là hoàn toàn không phải, bằng 并不是, văn viết, phủ định mạnh điều người ta tưởng. Trong bài: 然而毛坦厂中学并非如此."),
    ("柳树", "liǔshù", "liễu thụ", "danh từ", "cây liễu", "河边种着一排柳树。", "Bên bờ sông trồng một hàng liễu.",
     "Danh từ, cây liễu. Trước cổng trường Mao Thản Xưởng có một cây liễu hơn trăm tuổi mà phụ huynh coi là cây thần."),
    ("祭拜", "jìbài", "tế bái", "động từ", "cúng bái, khấn vái", "清明节人们去祭拜祖先。", "Tiết Thanh minh mọi người đi cúng bái tổ tiên.",
     "Động từ, nghĩa là cúng tế và lễ bái. Trong bài: 把院墙外柳树当神树祭拜, coi cây liễu ngoài tường trường như cây thần mà khấn vái."),
    ("富裕", "fùyù", "phú dụ", "tính từ", "giàu có, sung túc", "他家的生活很富裕。", "Cuộc sống nhà anh ấy rất sung túc.",
     "Tính từ, nghĩa là điều kiện kinh tế tốt, tiền bạc đầy đủ. Hay gặp 富裕人家，生活富裕. Trong bài: 都不是富裕的父母."),
    ("卑微", "bēiwēi", "ti vi", "tính từ", "thấp kém, nhỏ bé (địa vị)", "他出身卑微，却很有志气。", "Anh ấy xuất thân thấp kém nhưng rất có chí khí.",
     "Tính từ, nghĩa là địa vị thấp kém, nhỏ bé. Hay gặp 身份卑微，卑微的态度. Trong bài, phía sau trường Mao Thản Xưởng là 非常卑微的家庭."),
    ("轮流", "lúnliú", "luân lưu", "động từ", "lần lượt, thay phiên nhau", "我们轮流打扫教室。", "Chúng tôi thay phiên nhau quét dọn lớp học.",
     "Động từ, nghĩa là theo thứ tự người này tiếp người kia, thay phiên nhau. Mẫu: 轮流 cộng động từ, như 轮流休息，轮流开车. Trong bài: 母亲轮流给三四个孩子做饭."),
    ("寄托", "jìtuō", "ký thác", "động từ", "gửi gắm, đặt (hy vọng, tình cảm) vào", "父母把希望寄托在孩子身上。", "Cha mẹ đặt hết hy vọng vào con cái.",
     "Động từ, nghĩa là gửi gắm lý tưởng, hy vọng, tình cảm vào ai hay vào điều gì. Mẫu: 把……寄托在……身上. Trong bài: 孩子身上寄托着……家庭梦想."),
    ("可喜", "kěxǐ", "khả hỉ", "tính từ", "đáng mừng", "这是一个可喜的变化。", "Đây là một sự thay đổi đáng mừng.",
     "Tính từ, nghĩa là khiến người ta vui mừng. Hay gặp 可喜的成绩，可喜的变化. Chữ 可 cộng động từ tâm lý tạo thành tính từ, như 可爱，可怕，可惜."),
    ("嘲讽", "cháofěng", "trào phúng", "động từ", "chế giễu, mỉa mai", "不要嘲讽别人的缺点。", "Đừng chế giễu khuyết điểm của người khác.",
     "Động từ, nghĩa là cười nhạo và châm biếm. Chú ý: tiếng Việt trào phúng thường chỉ lối văn châm biếm, như thơ trào phúng; còn 嘲讽 là hành động chế giễu ai đó. Hay gặp 受到嘲讽，嘲讽的语气."),
    ("体制", "tǐzhì", "thể chế", "danh từ", "thể chế, cơ chế tổ chức", "中国的教育体制一直在改革。", "Thể chế giáo dục của Trung Quốc vẫn luôn được cải cách.",
     "Danh từ, chỉ chế độ tổ chức của nhà nước, cơ quan, doanh nghiệp. Hay gặp 政治体制，教育体制."),
    ("应试教育", "yìngshì jiàoyù", "ứng thí giáo dục", "cụm danh từ", "giáo dục chạy theo thi cử", "很多人批评应试教育。", "Nhiều người phê phán lối giáo dục chạy theo thi cử.",
     "Cụm danh từ, chỉ lối giáo dục lấy việc luyện khả năng làm bài thi làm mục đích chính. Chữ 应 đọc thanh bốn. Đối lập là 素质教育, giáo dục toàn diện, chúng ta sẽ gặp lại ở phần ôn tập đơn vị."),
    ("温情", "wēnqíng", "ôn tình", "danh từ", "sự ấm áp, tình cảm dịu dàng", "这部电影充满了温情。", "Bộ phim này tràn đầy tình cảm ấm áp.",
     "Danh từ, nghĩa là thái độ ôn hòa, tình cảm ấm áp. Hay gặp 充满温情. Trong bài: 我愿意用温情去面对这样的事情."),
    ("回想", "huíxiǎng", "hồi tưởng", "động từ", "nhớ lại, hồi tưởng", "回想起小时候的事，他笑了。", "Nhớ lại chuyện hồi nhỏ, anh ấy bật cười.",
     "Động từ, nghĩa là nghĩ lại chuyện đã qua. Hay gặp 回想起，回想不起来. Trong bài: 回想一九八五年的时候."),
    ("少之又少", "shǎozhīyòushǎo", "thiểu chi hựu thiểu", "cụm cố định", "rất ít, hầu như không có", "能考满分的学生少之又少。", "Học sinh thi được điểm tối đa thì cực kỳ hiếm.",
     "Cụm cố định, nghĩa là ít lại càng ít, hầu như không có. Trong bài: 谈发财、物质只有一两个，少之又少."),
    ("门路", "ménlù", "môn lộ", "danh từ", "đường dây, quan hệ, cửa sau (để đạt mục đích)", "他想找门路进这家公司。", "Anh ta muốn tìm đường dây để vào công ty này.",
     "Danh từ, đặc biệt chỉ con đường, mối quan hệ giúp đạt được mục đích cá nhân. Hay gặp 找门路，走门路，门路多. Trong bài: 我们没有任何的门路."),
    ("人脉", "rénmài", "nhân mạch", "danh từ", "các mối quan hệ, mạng lưới quan hệ", "做生意需要广泛的人脉。", "Làm ăn cần có mạng lưới quan hệ rộng.",
     "Danh từ, chỉ các mối quan hệ xã hội của một người. Hay gặp 人脉资源，拓展人脉, mở rộng quan hệ."),
    ("调转", "diàozhuǎn", "điệu chuyển", "động từ", "điều chuyển (công tác, vị trí)", "他最近调转到北京工作了。", "Gần đây anh ấy được điều chuyển lên Bắc Kinh làm việc.",
     "Động từ, nghĩa là điều động, chuyển đổi công tác hay vị trí. Chữ 调 ở đây đọc là diào, như trong 调动, chứ không đọc tiáo. Trong bài: 没有为找工作、调转岗位送过一次礼."),
    ("渺茫", "miǎománg", "miểu mang", "tính từ", "mờ mịt, mong manh", "他觉得考上名校的希望很渺茫。", "Cậu ấy thấy hy vọng thi đỗ trường danh tiếng rất mong manh.",
     "Tính từ, nghĩa là mờ mịt, khó đoán trước vì không nắm chắc. Hay gặp 希望渺茫，前途渺茫."),
    ("寒门", "hánmén", "hàn môn", "danh từ", "nhà nghèo, gia đình nghèo khó", "他出身寒门，靠读书改变了命运。", "Anh ấy xuất thân nhà nghèo, nhờ học hành mà đổi đời.",
     "Danh từ, nghĩa là gia đình nghèo khó. Tiếng Việt cũng có hàn môn. Hay gặp 出身寒门，寒门子弟，寒门出贵子, nhà nghèo sinh con quý."),
    # bốn từ bổ sung lấy từ bài khóa
    ("招生", "zhāoshēng", "chiêu sinh", "động từ (bổ sung)", "tuyển sinh", "这所大学今年招生三千人。", "Năm nay trường đại học này tuyển ba nghìn sinh viên.",
     "Động từ, nghĩa là tuyển sinh. Trong bài: 大学招生考试, kỳ thi tuyển sinh đại học, chính là 高考. Hay gặp 招生名额, chỉ tiêu tuyển sinh, sẽ gặp lại ở bài một chấm ba."),
    ("志愿", "zhìyuàn", "chí nguyện", "danh từ (bổ sung)", "nguyện vọng (đăng ký trường)", "他的第一志愿是北京大学。", "Nguyện vọng một của cậu ấy là Đại học Bắc Kinh.",
     "Danh từ, nghĩa là ý nguyện, chí hướng; trong thi cử là nguyện vọng đăng ký trường. Hay gặp 填报志愿，第一志愿. Ngoài ra, 志愿者 là tình nguyện viên."),
    ("涉及", "shèjí", "thiệp cập", "động từ (bổ sung)", "liên quan đến, đụng chạm đến", "这个问题涉及很多人的利益。", "Vấn đề này liên quan đến lợi ích của rất nhiều người.",
     "Động từ, nghĩa là liên quan, dính dáng đến. Trong bài: 涉及到教育体制、应试教育的东西. Từ này còn xuất hiện trong bài tập bốn."),
    ("命运", "mìngyùn", "mệnh vận", "danh từ (bổ sung)", "số phận, vận mệnh", "知识可以改变命运。", "Tri thức có thể thay đổi số phận.",
     "Danh từ, nghĩa là số phận. Cụm 改变命运, thay đổi số phận, xuất hiện nhiều lần trong bài, như 希望高考能改变他们的命运."),
]

add("bullets", chapter="Từ mới (45 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 1.1 có 41 từ trong sách + 4 từ bổ sung, chia thành 15 nhóm",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 反倒 (dào) · 调转 (diào) · 应试 (yìng)",
           "Từ dễ nhầm: 尊严 · 嘲讽 · 门路"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bảng từ của sách có bốn mươi mốt từ; thầy bổ sung thêm bốn từ quan trọng trong bài khóa, tổng cộng bốn mươi lăm từ, chia thành mười lăm nhóm, mỗi nhóm ba từ. Những từ có dấu sao trong sách là từ siêu cương, ít gặp hơn, các bạn chỉ cần hiểu nghĩa.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số chữ có nhiều cách đọc, như chữ thứ hai trong 反倒, chữ đầu trong 调转 và 应试. Thầy sẽ nhắc khi gặp."),
         F(4, "Ngoài ra, có mấy từ Hán Việt dễ hiểu nhầm, như 尊严，嘲讽，门路. Nghĩa của chúng trong tiếng Trung khác với tiếng Việt, các bạn nhớ nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

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
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung nếu khác: số viết bằng chữ, bỏ ngoặc kép])
P = [
    ("没有高考你拼得过富二代吗？按说这样的说法未免过于绝对，却是非常现实的话题，可换一个角度，你说我能不知道高考有多少毛病和问题吗？",
     "Không có thi đại học, bạn có đua nổi con nhà giàu không? Theo lẽ thường mà nói, cách nói này thật có phần quá tuyệt đối, nhưng lại là một đề tài vô cùng thực tế. Có điều, nhìn từ một góc độ khác, bạn nghĩ tôi lại không biết thi đại học có bao nhiêu khuyết điểm và vấn đề hay sao?",
     ["拼得过 là đua nổi, cạnh tranh nổi: 拼 là dốc sức cạnh tranh, 得过 là bổ ngữ khả năng, phủ định là 拼不过. Câu mở đầu chính là tên bài.",
      "按说 là theo lẽ thường mà nói; 未免过于绝对 là thật có phần quá tuyệt đối. 可换一个角度 là nhưng nhìn từ góc khác. 你说我能不知道……吗 là câu hỏi tu từ: tôi đâu phải không biết thi đại học có nhiều vấn đề. Ba mẫu 按说，未免，换一个角度 đều là mẫu câu trọng điểm."]),
    ("1977年9月，中国教育部决定恢复停止了十余年的大学招生考试，这恢复的不只是高考，更是几代中国人对于公平、尊严的梦想。",
     "Tháng 9 năm 1977, Bộ Giáo dục Trung Quốc quyết định khôi phục kỳ thi tuyển sinh đại học đã bị ngừng hơn mười năm. Thứ được khôi phục không chỉ là kỳ thi đại học, mà còn là giấc mơ về công bằng và phẩm giá của mấy thế hệ người Trung Quốc.",
     ["恢复 là khôi phục. 停止了十余年 là đã ngừng hơn mười năm: từ năm một chín sáu sáu, do Cách mạng Văn hóa, kỳ thi đại học bị bãi bỏ. 大学招生考试 là kỳ thi tuyển sinh đại học, chính là 高考.",
      "这恢复的不只是高考，更是……梦想: mẫu 不只是……，更是…… nghĩa là không chỉ là…, mà còn là…, vế sau quan trọng hơn. 对于公平、尊严的梦想 là giấc mơ về công bằng và phẩm giá."],
     "一九七七年九月，中国教育部决定恢复停止了十余年的大学招生考试，这恢复的不只是高考，更是几代中国人对于公平、尊严的梦想。"),
    ("中国历来流传着一句话：“国家兴亡，匹夫有责。”我觉得有了“恢复高考”这事，应该稍稍对前面的话加以改动：“国家兴亡，学子有路，匹夫有责”。",
     "Ở Trung Quốc xưa nay vẫn lưu truyền một câu: “Nước nhà hưng vong, kẻ thất phu cũng có trách nhiệm.” Tôi cho rằng có chuyện “khôi phục thi đại học” rồi, thì nên sửa câu ấy đi một chút: “Nước nhà hưng vong, người đi học có đường tiến thân, kẻ thất phu có trách nhiệm.”",
     ["历来流传着 là xưa nay vẫn lưu truyền. 国家兴亡，匹夫有责 là thành ngữ: đất nước hưng thịnh hay suy vong, mỗi người dân thường đều có trách nhiệm; 匹夫 là người đàn ông bình thường. Tiếng Việt cũng có câu quốc gia hưng vong, thất phu hữu trách.",
      "稍稍对前面的话加以改动 là sửa câu nói trên một chút; mẫu 对……加以改动 là tiến hành sửa đổi cái gì. 学子有路 là người đi học có đường đi: nhờ thi đại học, con nhà bình thường cũng có lối tiến thân."]),
    ("80年代的高考和当代高考概念是不一样的，当年我所有的科目都是满分，我报考学校的第一志愿就是北京广播学院，第二志愿是武汉大学，第三志愿是北京大学。",
     "Kỳ thi đại học những năm 80 và kỳ thi đại học ngày nay là hai khái niệm khác nhau. Năm ấy, môn nào của tôi cũng đạt điểm tối đa; khi đăng ký trường, nguyện vọng một của tôi là Học viện Phát thanh Bắc Kinh, nguyện vọng hai là Đại học Vũ Hán, nguyện vọng ba là Đại học Bắc Kinh.",
     ["80年代 là những năm tám mươi. 当代 là thời nay. 当年 là năm ấy, hồi đó. 科目 là môn thi; 满分 là điểm tối đa.",
      "报考 là đăng ký dự thi. 第一志愿 là nguyện vọng một. Điều thú vị là tác giả xếp Đại học Bắc Kinh danh tiếng chỉ ở nguyện vọng ba, sau Học viện Phát thanh Bắc Kinh, ngôi trường đào tạo phát thanh viên mà ông yêu thích."],
     "八十年代的高考和当代高考概念是不一样的，当年我所有的科目都是满分，我报考学校的第一志愿就是北京广播学院，第二志愿是武汉大学，第三志愿是北京大学。"),
    ("后来我经常和我爱人开玩笑，她是镇江文科状元，明明能够去中国所有的名牌学校，但是偏偏莫名其妙地报考了北京广播学院。",
     "Sau này tôi thường đùa với vợ mình: cô ấy là thủ khoa khối xã hội của Trấn Giang, rõ ràng có thể vào bất kỳ trường danh tiếng nào của Trung Quốc, vậy mà lại cứ chẳng hiểu vì sao đi đăng ký vào Học viện Phát thanh Bắc Kinh.",
     ["爱人 là vợ hoặc chồng, cách gọi phổ biến ở Trung Quốc đại lục. 镇江 là thành phố Trấn Giang, tỉnh Giang Tô. 文科状元 là thủ khoa khối xã hội. 名牌学校 là trường danh tiếng.",
      "明明……，但是偏偏……: rõ ràng là…, vậy mà lại cứ…. 偏偏 diễn tả việc làm trái với lẽ thường. 莫名其妙 là chẳng hiểu vì sao, không giải thích nổi. Đây là lời nói đùa: nhờ vợ chọn ngôi trường này mà hai người mới gặp nhau."]),
    ("这反倒说明，那个时候大家更多的是挑选自己想去的学校和专业，不像今天已经变成了不管学生喜不喜欢，必须要去某所高校的现象。",
     "Điều này trái lại cho thấy, thời ấy mọi người chủ yếu chọn trường và ngành mình muốn học, không giống như ngày nay, đã thành hiện tượng bất kể học sinh có thích hay không, cũng nhất định phải vào cho được một trường đại học nào đó.",
     ["反倒说明 là trái lại cho thấy: tưởng như chọn trường kỳ lạ là điều dở, nhưng nó lại chứng tỏ thời đó học sinh được tự do chọn theo sở thích. 挑选 là lựa chọn kỹ.",
      "不像今天…… là không giống ngày nay. 不管……喜不喜欢 là bất kể có thích hay không. 某所高校 là một trường đại học nào đó; 所 là lượng từ của trường học, 高校 là trường đại học, cao đẳng. Tác giả phê phán việc ngày nay chỉ chạy theo danh tiếng của trường."]),
    ("对于部分高考名校，我持中立态度，不一定赞赏，但是也不便于直接批评。毛坦厂（Máotǎnchǎng）我们做了两期的节目，回来改变了我的态度。",
     "Đối với một số trường cấp ba nổi tiếng về luyện thi đại học, tôi giữ thái độ trung lập: không hẳn tán thưởng, nhưng cũng không tiện phê phán thẳng. Chúng tôi đã làm hai số chương trình ở Mao Thản Xưởng, trở về thì thái độ của tôi đã thay đổi.",
     ["高考名校 là trường cấp ba có tỷ lệ đỗ đại học cao. 持中立态度 là giữ thái độ trung lập. 不一定赞赏 là không hẳn tán thưởng. 不便于 là không tiện.",
      "毛坦厂 là trường Mao Thản Xưởng ở An Huy, công xưởng luyện thi mà chúng ta đã nói ở phần bối cảnh. 两期的节目 là hai số, hai kỳ của chương trình; 期 là lượng từ cho số báo, số chương trình."],
     "对于部分高考名校，我持中立态度，不一定赞赏，但是也不便于直接批评。毛坦厂我们做了两期的节目，回来改变了我的态度。"),
    ("很多官家子弟、富家子弟费尽心机找人把孩子送到竞争门槛较高的高考名校，而那些没有一定的财富、权力的家庭根本进不去这些学校的大门。",
     "Rất nhiều con nhà quan, con nhà giàu tìm đủ mọi cách nhờ vả người quen để đưa con vào những trường luyện thi danh tiếng có ngưỡng cạnh tranh khá cao, còn những gia đình không có của cải, quyền lực nhất định thì hoàn toàn không thể bước qua cổng những ngôi trường này.",
     ["官家子弟 là con nhà quan; 富家子弟 là con nhà giàu. 费尽心机 là thành ngữ, nghĩa là vắt óc, tìm đủ mọi cách. 找人 là tìm người nhờ vả, đi cửa sau.",
      "门槛较高 là ngưỡng cửa khá cao. 根本进不去 là hoàn toàn không vào được; 根本 đứng trước từ phủ định để nhấn mạnh. Hình ảnh này trái ngược với trường Mao Thản Xưởng ở đoạn sau."]),
    ("然而毛坦厂中学并非如此，毛坦厂相当多的学生是打工者的孩子，把院墙外柳树当神树祭拜的，都不是富裕的父母。",
     "Thế nhưng trường Mao Thản Xưởng hoàn toàn không phải như vậy. Khá nhiều học sinh ở đây là con của những người lao động làm thuê; những người coi cây liễu ngoài tường trường như cây thần mà khấn vái đều không phải là những bậc cha mẹ giàu có.",
     ["并非如此 là hoàn toàn không phải như vậy. 相当多 là khá nhiều. 打工者 là người lao động làm thuê, thường là nông dân lên thành phố kiếm sống.",
      "把院墙外柳树当神树祭拜的: cấu trúc 把A当B là coi A như B, chữ 当 đọc thanh bốn. Cụm có chữ 的 ở cuối thay cho danh từ chỉ người: những người khấn vái."]),
    ("毛坦厂中学的背后是非常卑微的家庭，父亲在外打工，母亲轮流给三四个孩子做饭。孩子出发去参加高考时，上万人守着大客车，这些孩子身上寄托着一个又一个非常普通甚至卑微的家庭梦想。",
     "Phía sau trường Mao Thản Xưởng là những gia đình vô cùng nhỏ bé: người cha đi làm thuê xa nhà, các bà mẹ thay phiên nhau nấu cơm cho ba bốn đứa trẻ. Khi bọn trẻ lên đường đi thi, hàng vạn người đứng chờ quanh những chiếc xe khách lớn; những đứa trẻ ấy mang trên mình giấc mơ của biết bao gia đình rất đỗi bình thường, thậm chí nhỏ bé.",
     ["卑微 là nhỏ bé, thấp kém. 在外打工 là đi làm thuê xa nhà. 轮流给三四个孩子做饭 là thay phiên nhau nấu cơm cho ba bốn đứa trẻ: nhiều phụ huynh thuê nhà gần trường để ở cùng con, gọi là 陪读.",
      "上万人守着大客车 là hàng vạn người vây quanh xe khách; 上万 là lên tới hàng vạn. 寄托着……梦想 là gửi gắm giấc mơ. 一个又一个 là hết cái này đến cái khác, biết bao nhiêu."]),
    ("把高考作为人生梦想是可喜和值得鼓励的，无论如何我都做不出任何嘲讽毛坦厂中学的事情。",
     "Coi thi đại học là ước mơ của đời mình là điều đáng mừng và đáng được khích lệ; dù thế nào đi nữa, tôi cũng không thể làm bất cứ điều gì chế giễu trường Mao Thản Xưởng.",
     ["把A作为B là coi A là B. 可喜 là đáng mừng; 值得鼓励 là đáng được khích lệ.",
      "无论如何我都做不出…… là dù thế nào tôi cũng không làm nổi…; 做不出 là bổ ngữ khả năng, ý là lương tâm không cho phép. 嘲讽 là chế giễu. Đây là mẫu câu 无论如何……都."]),
    ("可能这里有很多我们不一定认同的涉及到教育体制、应试教育的东西，但是我愿意用温情去面对这样的事情。更重要的是，我祝福这些普通的家庭，希望高考能改变他们的命运。",
     "Có thể ở đây có nhiều điều liên quan đến thể chế giáo dục, đến lối giáo dục chạy theo thi cử mà chúng ta chưa chắc đã đồng tình, nhưng tôi sẵn lòng nhìn những chuyện như thế bằng sự cảm thông ấm áp. Quan trọng hơn, tôi chúc phúc cho những gia đình bình thường này, mong rằng thi đại học có thể thay đổi số phận của họ.",
     ["Câu này có định ngữ rất dài: 我们不一定认同的涉及到教育体制、应试教育的东西, những thứ liên quan đến thể chế giáo dục và giáo dục thi cử mà chúng ta chưa chắc đồng tình. 认同 là đồng tình, tán thành.",
      "用温情去面对 là đối diện bằng sự ấm áp, cảm thông. 更重要的是 là quan trọng hơn là, dùng để đưa ra ý chính. 祝福 là chúc phúc."]),
    ("回想1985年的时候，我们班同学在高考留言板上的留言，如果按现在的话来说，更多应该是谈高考、谈梦想，相反的是，那个时候更多谈人生，其中谈发财、物质只有一两个，少之又少。",
     "Nhớ lại năm 1985, những lời nhắn của bạn bè lớp tôi trên bảng lưu bút mùa thi, nếu nói theo cách ngày nay, lẽ ra phần nhiều phải bàn về thi cử, về ước mơ; thế nhưng ngược lại, hồi ấy mọi người bàn về lẽ sống nhiều hơn, trong đó nói đến chuyện làm giàu, chuyện vật chất chỉ có một hai người, ít lại càng ít.",
     ["回想 là nhớ lại. 留言板 là bảng lưu bút, bảng để lại lời nhắn. 按现在的话来说 là nói theo cách nói ngày nay.",
      "相反的是 là ngược lại, dùng để nêu sự thật trái với điều vừa nói. 谈人生 là bàn về lẽ sống, về cuộc đời. 发财 là phát tài, làm giàu. 少之又少 là ít lại càng ít. Tác giả muốn nói: thế hệ của ông sống có lý tưởng, ít thực dụng."],
     "回想一九八五年的时候，我们班同学在高考留言板上的留言，如果按现在的话来说，更多应该是谈高考、谈梦想，相反的是，那个时候更多谈人生，其中谈发财、物质只有一两个，少之又少。"),
    ("我们没有任何的门路，我母亲就是一名普通的老师，父亲在76年就去世了。当年在北京我没有亲戚和熟悉的人脉，但我走到今天，却没有为找工作、调转岗位送过一次礼，不也走到今天了吗？",
     "Chúng tôi chẳng có đường dây quan hệ nào cả: mẹ tôi chỉ là một giáo viên bình thường, bố tôi mất từ năm 76. Hồi đó ở Bắc Kinh tôi không có họ hàng, cũng chẳng có mối quan hệ quen biết nào, vậy mà tôi đi được đến hôm nay mà chưa từng biếu xén lấy một lần vì chuyện tìm việc hay điều chuyển công tác. Chẳng phải tôi vẫn đi được đến hôm nay đó sao?",
     ["门路 là đường dây, cửa sau. 在七六年 là năm một chín bảy sáu, nói tắt. 亲戚 là họ hàng. 人脉 là các mối quan hệ.",
      "调转岗位 là điều chuyển vị trí công tác, chữ 调 đọc là diào. 送礼 là biếu quà, đút lót; ở đây tách ra thành 送过一次礼. 不也走到今天了吗 là câu hỏi tu từ: chẳng phải tôi cũng đã đi đến ngày hôm nay sao? Ý là không cần đi cửa sau vẫn có thể thành công."],
     "我们没有任何的门路，我母亲就是一名普通的老师，父亲在七六年就去世了。当年在北京我没有亲戚和熟悉的人脉，但我走到今天，却没有为找工作、调转岗位送过一次礼，不也走到今天了吗？"),
    ("如果现在的年轻人说生活中有很多糟糕的东西，当然有。但是要去相信还有另外一种方式能够改变命运，那就是高考。如果你不用分数考出去，家里头帮助你进入名校的机会真的很渺茫。",
     "Nếu các bạn trẻ bây giờ nói cuộc sống có nhiều điều tồi tệ, thì đương nhiên là có. Nhưng phải tin rằng vẫn còn một cách khác có thể thay đổi số phận, đó chính là thi đại học. Nếu bạn không dùng điểm số để thi thoát ra, thì cơ hội gia đình giúp bạn vào trường danh tiếng thật sự rất mong manh.",
     ["糟糕 là tồi tệ. 当然有 là đương nhiên là có: tác giả thừa nhận mặt trái của xã hội trước, rồi mới chuyển ý bằng 但是.",
      "用分数考出去 là dùng điểm số thi để thoát ra, rời khỏi quê nghèo. 家里头 là gia đình, cách nói khẩu ngữ. 渺茫 là mong manh, mờ mịt."]),
    ("我希望高考能使很多寒门孩子有成为富一代的可能，一个人上了大学，改变了这个家庭。也许最终你依然拼不过富二代，但是你可能改变自己家庭的生活。",
     "Tôi mong thi đại học có thể giúp nhiều đứa trẻ nhà nghèo có cơ hội trở thành thế hệ giàu có đầu tiên: một người vào đại học, thay đổi cả một gia đình. Có lẽ cuối cùng bạn vẫn không đua nổi con nhà giàu, nhưng bạn có thể thay đổi cuộc sống của gia đình mình.",
     ["寒门孩子 là con nhà nghèo. 富一代 là thế hệ giàu có đầu tiên, tức là người tự mình làm nên. 使 là khiến cho, làm cho, văn viết.",
      "依然拼不过富二代 là vẫn không đua nổi con nhà giàu, quay lại câu hỏi ở đầu bài. Kết luận rất thực tế: thi đại học không phải phép màu, nhưng là cơ hội công bằng để con nhà nghèo thay đổi cuộc sống gia đình."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 没有高考，你怎么拼得过富二代？", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa. Bài được cải biên từ chương trình phỏng vấn 我们 của 白岩松. Đây là lời kể ở ngôi thứ nhất, giọng văn gần với văn nói, có nhiều câu hỏi tu từ và cách nói khẩu ngữ.",
         F(0, "Bài có bảy đoạn, thầy chia thành mười sáu phần ngắn. Với mỗi phần, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    assert len(item) in (3, 4), item[0][:10]
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 70 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", ""), cap="")] + [F(1, n) for n in notes])

# ======================= ĐỌC HIỂU =======================
add("bullets", chapter="Đọc hiểu", section="Đọc hiểu 课文理解", title="Bố cục bài khóa", size=36,
    items=["Đoạn 1: Ý nghĩa của việc khôi phục thi đại học năm 1977 – công bằng và phẩm giá",
           "Đoạn 2: Thi đại học những năm 80 – học sinh được tự do chọn trường, chọn ngành",
           "Đoạn 3–5: Trường Mao Thản Xưởng – thái độ của tác giả từ trung lập chuyển sang cảm thông",
           "Đoạn 6: Lưu bút năm 1985 – bàn về lẽ sống, ít bàn chuyện làm giàu",
           "Đoạn 7: Không có quan hệ vẫn thành công – thi đại học là cơ hội đổi đời của con nhà nghèo"],
    say=["Chúng ta cùng nhìn lại bố cục của bài khóa. Bài có bảy đoạn, đi từ lịch sử, qua trải nghiệm của tác giả, đến quan điểm của ông.",
         F(0, "Đoạn một: thừa nhận thi đại học có nhiều vấn đề, nhưng việc khôi phục nó năm một chín bảy bảy mang lại giấc mơ về công bằng và phẩm giá."),
         F(1, "Đoạn hai: kỳ thi đại học những năm tám mươi khác ngày nay: học sinh chọn trường, chọn ngành theo sở thích, như chính tác giả và vợ ông."),
         F(2, "Đoạn ba đến đoạn năm: trường Mao Thản Xưởng. Ban đầu tác giả giữ thái độ trung lập với các trường luyện thi, nhưng khi thấy phía sau là những gia đình lao động nghèo, ông chuyển sang cảm thông và chúc phúc."),
         F(3, "Đoạn sáu: lưu bút của bạn học năm một chín tám lăm chủ yếu bàn về lẽ sống, rất ít người nói chuyện làm giàu."),
         F(4, "Đoạn bảy: kết luận. Tác giả không có quan hệ, không đi cửa sau, vẫn thành công. Ông tin thi đại học là cách để con nhà nghèo thay đổi số phận, dù có thể vẫn không đua nổi con nhà giàu.")])

add("bullets", section="Đọc hiểu 课文理解", title="Câu hỏi đọc hiểu (1)", reveal=True, size=34,
    items=["(1) 作者为什么说恢复的“不只是高考”？",
           "Đáp án: 因为恢复的更是几代中国人对于公平、尊严的梦想。",
           "(2) 作者把“国家兴亡，匹夫有责”改成了什么？为什么？",
           "Đáp án: 改成“国家兴亡，学子有路，匹夫有责”，因为有了高考，读书人就有了出路。",
           "(3) 80年代的高考和今天的高考有什么不同？",
           "Đáp án: 那时候大家更多是挑选自己想去的学校和专业；今天不管学生喜不喜欢，都必须要去某所高校。"],
    say=["Bây giờ chúng ta kiểm tra mức độ hiểu bài. Thầy đọc câu hỏi, các bạn tạm dừng, trả lời bằng tiếng Trung, rồi nghe đáp án.",
         F(0, "Câu một: 作者为什么说恢复的不只是高考？ Vì sao tác giả nói thứ được khôi phục không chỉ là kỳ thi đại học?"),
         F(1, "Đáp án: 因为恢复的更是几代中国人对于公平、尊严的梦想。 Vì thứ được khôi phục còn là giấc mơ về công bằng và phẩm giá của mấy thế hệ người Trung Quốc."),
         F(2, "Câu hai: 作者把国家兴亡，匹夫有责改成了什么？为什么？ Tác giả đã sửa câu nói ấy thành gì? Vì sao?"),
         F(3, "Đáp án: 改成国家兴亡，学子有路，匹夫有责，因为有了高考，读书人就有了出路。 Vì có thi đại học thì người đi học có lối thoát, có đường tiến thân."),
         F(4, "Câu ba: 八十年代的高考和今天的高考有什么不同？ Kỳ thi đại học những năm tám mươi khác ngày nay ở điểm nào?"),
         F(5, "Đáp án: 那时候大家更多是挑选自己想去的学校和专业；今天不管学生喜不喜欢，都必须要去某所高校。 Hồi đó mọi người chọn trường và ngành mình thích; ngày nay bất kể thích hay không, đều phải vào cho được một trường nào đó.")])

add("bullets", section="Đọc hiểu 课文理解", title="Câu hỏi đọc hiểu (2)", reveal=True, size=34,
    items=["(4) 去毛坦厂做节目以后，作者的态度有什么变化？为什么？",
           "Đáp án: 从“中立”变成了理解和祝福，因为那里的学生多是打工者的孩子，身上寄托着普通家庭的梦想。",
           "(5) 1985年作者的同学在留言板上多谈什么？",
           "Đáp án: 更多谈人生，谈发财、物质的只有一两个，少之又少。",
           "(6) 作者认为高考对寒门孩子意味着什么？",
           "Đáp án: 高考是改变命运的另一种方式；也许拼不过富二代，但能改变自己家庭的生活。"],
    say=[F(0, "Câu bốn: 去毛坦厂做节目以后，作者的态度有什么变化？为什么？ Sau khi làm chương trình ở Mao Thản Xưởng, thái độ của tác giả thay đổi thế nào? Vì sao?"),
         F(1, "Đáp án: 从中立变成了理解和祝福，因为那里的学生多是打工者的孩子，身上寄托着普通家庭的梦想。 Từ trung lập chuyển sang thấu hiểu và chúc phúc, vì học sinh ở đó phần lớn là con người lao động, mang trên mình giấc mơ của những gia đình bình thường."),
         F(2, "Câu năm: 一九八五年作者的同学在留言板上多谈什么？ Năm một chín tám lăm, bạn học của tác giả viết gì trên bảng lưu bút?"),
         F(3, "Đáp án: 更多谈人生，谈发财、物质的只有一两个，少之又少。 Phần lớn bàn về lẽ sống, nói chuyện làm giàu và vật chất chỉ có một hai người."),
         F(4, "Câu sáu: 作者认为高考对寒门孩子意味着什么？ Theo tác giả, thi đại học có ý nghĩa gì với con nhà nghèo?"),
         F(5, "Đáp án: 高考是改变命运的另一种方式；也许拼不过富二代，但能改变自己家庭的生活。 Đó là một cách khác để thay đổi số phận: có thể không đua nổi con nhà giàu, nhưng có thể thay đổi cuộc sống gia đình mình.")])

# ======================= MẪU CÂU TRỌNG ĐIỂM =======================
add("bullets", chapter="Mẫu câu: 按说 · 未免 · 换一个角度", section="Mẫu câu 重点句型", title="1. 按说 ànshuō – theo lẽ thường mà nói", size=34,
    items=["Phó từ: dựa theo sự thật, lẽ thường mà nói (lẽ ra…); vế sau thường có 可是 · 却 · 可 nêu thực tế trái ngược",
           "Từ gần nghĩa: 按理 · 按理说",
           "没有高考你拼得过富二代吗？按说这样的说法未免过于绝对，却是非常现实的话题……",
           "按说现在是蔬菜供应淡季，可是这里的蔬菜种类还是不少。",
           "按说这个时候应该下雪了，可今年一场雪都没下。"],
    say=["Bây giờ chúng ta sang phần mẫu câu và từ trọng điểm, 重点句型与词汇. Sách đưa ra mười một điểm, thầy sẽ giảng lần lượt, mỗi điểm kèm ba ví dụ của sách.",
         F(0, "Điểm thứ nhất: 按说. Đây là phó từ, nghĩa là dựa theo sự thật hoặc lẽ thường mà nói, tiếng Việt là theo lẽ thường, lẽ ra. Vế sau thường có 可是，却 hoặc 可, nêu ra thực tế trái ngược với lẽ thường."),
         F(1, "Những từ gần nghĩa là 按理 và 按理说."),
         F(2, "Ví dụ một, câu mở đầu bài khóa: 没有高考你拼得过富二代吗？按说这样的说法未免过于绝对，却是非常现实的话题。 Theo lẽ mà nói, cách nói này hơi tuyệt đối, nhưng lại là đề tài rất thực tế."),
         F(3, "Ví dụ hai: 按说现在是蔬菜供应淡季，可是这里的蔬菜种类还是不少。 Theo lẽ thường thì bây giờ đang là mùa ít rau, nhưng ở đây vẫn có khá nhiều loại rau. 淡季 là mùa thấp điểm."),
         F(4, "Ví dụ ba: 按说这个时候应该下雪了，可今年一场雪都没下。 Lẽ ra giờ này phải có tuyết rồi, vậy mà năm nay chưa có lấy một trận tuyết.")])

add("bullets", section="Mẫu câu 重点句型", title="2. 未免 wèimiǎn – thật là (hơi quá)", size=34,
    items=["Phó từ: thật là, không thể không nói là… – nhận xét việc gì đó quá mức, giọng phê bình nhẹ nhàng",
           "Thường đi với 太 · 过于 · 有点儿 · 过分: 未免太……了 / 未免过于……",
           "按说这样的说法未免过于绝对，却是非常现实的话题。",
           "你这样当众指责他，未免也太过分了。",
           "单纯用一次考试来判断人的能力，未免也太绝对化、片面化了。"],
    say=["Điểm thứ hai: 未免.",
         F(0, "未免 là phó từ, nghĩa là thật là, không thể không nói là. Người nói dùng nó để nhận xét một việc gì đó vượt quá mức hợp lý, giọng phê bình nhưng nhẹ nhàng, lịch sự."),
         F(1, "未免 thường đi với 太，过于，有点儿，过分, tạo thành 未免太……了, hoặc 未免过于……."),
         F(2, "Ví dụ một, trong bài khóa: 按说这样的说法未免过于绝对。 Cách nói này thật có phần quá tuyệt đối."),
         F(3, "Ví dụ hai: 你这样当众指责他，未免也太过分了。 Cậu trách mắng anh ấy trước mặt mọi người như thế thì thật là quá đáng. 当众 là trước mặt mọi người."),
         F(4, "Ví dụ ba: 单纯用一次考试来判断人的能力，未免也太绝对化、片面化了。 Chỉ dùng một kỳ thi để đánh giá năng lực con người thì thật là quá tuyệt đối, quá phiến diện. Câu này cũng chính là lời phê bình hay gặp đối với thi đại học.")])

add("bullets", section="Mẫu câu 重点句型", title="3. 换一个角度（来看）– nhìn từ góc độ khác", size=34,
    items=["Đưa ra một cách nhìn khác, thường trái với ý vừa nói; hay đứng sau 可 · 可是 · 但",
           "……却是非常现实的话题，可换一个角度，你说我能不知道高考有多少毛病和问题吗？",
           "他一直觉得没考上大学是自己的劣势，可换一个角度，正是因为没上过大学，他才会更努力。",
           "大量的作业有助于学生掌握知识，可换一个角度来看，为了让学生能够有好成绩，就非得采取这样的方式吗？"],
    say=["Điểm thứ ba: 换一个角度, hoặc đầy đủ là 换一个角度来看, nghĩa là đổi sang một góc độ khác mà nhìn.",
         F(0, "Cụm này dùng để đưa ra một cách nhìn khác, thường trái với ý vừa nói. Nó hay đứng sau 可，可是 hoặc 但. Đây là cụm rất hữu ích khi viết văn nghị luận, để xem xét vấn đề từ hai phía."),
         F(1, "Ví dụ một, trong bài khóa: 却是非常现实的话题，可换一个角度，你说我能不知道高考有多少毛病和问题吗？ Nhưng nhìn từ góc khác, tôi đâu phải không biết thi đại học có bao nhiêu vấn đề."),
         F(2, "Ví dụ hai: 他一直觉得没考上大学是自己的劣势，可换一个角度，正是因为没上过大学，他才会更努力。 Anh ấy luôn cho rằng không đỗ đại học là điểm yếu của mình, nhưng nhìn từ góc khác, chính vì chưa học đại học nên anh ấy mới nỗ lực hơn. 劣势 là thế yếu."),
         F(3, "Ví dụ ba: 大量的作业有助于学生掌握知识，可换一个角度来看，为了让学生能够有好成绩，就非得采取这样的方式吗？ Nhiều bài tập giúp học sinh nắm vững kiến thức, nhưng nhìn từ góc khác, để học sinh có thành tích tốt, cứ nhất thiết phải dùng cách này sao? 非得 là nhất thiết phải.")])

add("bullets", chapter="Mẫu câu: 不只是…更是 · 历来 · 稍稍", section="Mẫu câu 重点句型", title="4. 不只是……，更是…… – không chỉ là…, mà còn là…", size=36,
    items=["Vế sau có ý nghĩa sâu hơn, quan trọng hơn vế trước (tăng tiến)",
           "1977年9月……这恢复的不只是高考，更是几代中国人对于公平、尊严的梦想。",
           "结婚不只是两个人的事，更是两个家庭的事。",
           "互联网不只是一种技术，更是一种思想、一种理念。"],
    say=["Điểm thứ tư: mẫu câu 不只是……，更是…….",
         F(0, "Mẫu này nghĩa là không chỉ là…, mà còn là…. Vế sau có ý nghĩa sâu sắc hơn, quan trọng hơn vế trước, đây là quan hệ tăng tiến. Chữ 更 nhấn mạnh vế sau."),
         F(1, "Ví dụ một, trong bài khóa: 这恢复的不只是高考，更是几代中国人对于公平、尊严的梦想。 Thứ được khôi phục không chỉ là kỳ thi, mà còn là giấc mơ về công bằng và phẩm giá."),
         F(2, "Ví dụ hai: 结婚不只是两个人的事，更是两个家庭的事。 Kết hôn không chỉ là chuyện của hai người, mà còn là chuyện của hai gia đình. Câu này người Việt nghe chắc thấy rất quen."),
         F(3, "Ví dụ ba: 互联网不只是一种技术，更是一种思想、一种理念。 Internet không chỉ là một công nghệ, mà còn là một tư tưởng, một quan niệm.")])

add("bullets", section="Mẫu câu 重点句型", title="5. 历来 lìlái – từ trước đến nay", size=36,
    items=["Phó từ thời gian: suốt nhiều năm (nhiều lần) qua, từ trước đến nay (≈ 从来, văn viết hơn)",
           "Hay gặp: 历来如此 · 历来重视 · 历来是……",
           "中国历来流传着一句话：“国家兴亡，匹夫有责。”",
           "王老师历来重视培养学生的动手能力。",
           "他做人做事历来是快人快语，从不拖泥带水。"],
    say=["Điểm thứ năm: phó từ 历来.",
         F(0, "历来 là phó từ thời gian, nghĩa là suốt nhiều năm, nhiều lần qua, từ trước đến nay. Nó gần với 从来, nhưng mang màu sắc văn viết hơn, và thường dùng trong câu khẳng định."),
         F(1, "Những cụm hay gặp: 历来如此, xưa nay vẫn thế; 历来重视, xưa nay luôn coi trọng."),
         F(2, "Ví dụ một, trong bài khóa: 中国历来流传着一句话：国家兴亡，匹夫有责。 Ở Trung Quốc xưa nay vẫn lưu truyền một câu nói."),
         F(3, "Ví dụ hai: 王老师历来重视培养学生的动手能力。 Thầy Vương xưa nay luôn coi trọng việc rèn luyện kỹ năng thực hành cho học sinh. 动手能力 là khả năng tự tay làm."),
         F(4, "Ví dụ ba: 他做人做事历来是快人快语，从不拖泥带水。 Anh ấy làm người làm việc xưa nay luôn thẳng thắn, nhanh gọn, chưa bao giờ dây dưa. 快人快语 là người thẳng tính nói thẳng; 拖泥带水 là lề mề, dây dưa.")])

add("bullets", section="Mẫu câu 重点句型", title="6. 稍稍 shāoshāo – hơi, một chút", size=36,
    items=["Phó từ mức độ: hơi, một chút (= 稍微 · 略微), chỉ số lượng ít hoặc mức độ nhẹ",
           "我觉得有了“恢复高考”这事，应该稍稍对前面的话加以改动……",
           "事情终于真相大白了，大家都稍稍松了一口气。",
           "上海的夏天又闷又热，稍稍一动就会满头大汗。"],
    say=["Điểm thứ sáu: 稍稍.",
         F(0, "稍稍 là phó từ mức độ, nghĩa là hơi, một chút, giống 稍微 và 略微. Nó chỉ số lượng ít hoặc mức độ nhẹ."),
         F(1, "Ví dụ một, trong bài khóa: 我觉得有了恢复高考这事，应该稍稍对前面的话加以改动。 Tôi nghĩ có chuyện khôi phục thi đại học rồi, thì nên sửa câu nói ở trên một chút."),
         F(2, "Ví dụ hai: 事情终于真相大白了，大家都稍稍松了一口气。 Sự việc cuối cùng cũng sáng tỏ, mọi người đều thở phào nhẹ nhõm một chút. 真相大白 là sự thật được phơi bày."),
         F(3, "Ví dụ ba: 上海的夏天又闷又热，稍稍一动就会满头大汗。 Mùa hè Thượng Hải vừa oi vừa nóng, chỉ hơi cử động một chút là mồ hôi đầm đìa. Mẫu 稍稍一 cộng động từ nghĩa là chỉ cần hơi… một chút là….")])

add("bullets", chapter="Mẫu câu: 偏偏 · 反倒", section="Mẫu câu 重点句型", title="7. 偏偏 piānpiān – lại cứ, cố tình", size=34,
    items=["Phó từ: cố ý làm trái với yêu cầu khách quan hoặc tình hình thực tế",
           "Hay dùng mẫu: 明明……，（但是/却）偏偏……",
           "她是镇江文科状元，明明能够去中国所有的名牌学校，但是偏偏莫名其妙地报考了北京广播学院。",
           "周围这么多漂亮的女生，你怎么偏偏喜欢她？",
           "明明可以靠脸吃饭，却偏偏要靠实力去奋斗。"],
    say=["Điểm thứ bảy: phó từ 偏偏.",
         F(0, "偏偏 biểu thị cố ý làm trái với yêu cầu khách quan hoặc với tình hình thực tế. Tiếng Việt dịch là lại cứ, cố tình, khăng khăng."),
         F(1, "偏偏 rất hay đi với 明明 ở vế trước: 明明……，但是偏偏……, rõ ràng là…, vậy mà lại cứ…."),
         F(2, "Ví dụ một, trong bài khóa: 她是镇江文科状元，明明能够去中国所有的名牌学校，但是偏偏莫名其妙地报考了北京广播学院。 Rõ ràng có thể vào mọi trường danh tiếng, vậy mà lại cứ chọn Học viện Phát thanh."),
         F(3, "Ví dụ hai: 周围这么多漂亮的女生，你怎么偏偏喜欢她？ Xung quanh bao nhiêu cô gái xinh đẹp, sao cậu lại cứ thích cô ấy?"),
         F(4, "Ví dụ ba: 明明可以靠脸吃饭，却偏偏要靠实力去奋斗。 Rõ ràng có thể sống nhờ nhan sắc, vậy mà lại cứ muốn phấn đấu bằng thực lực. 靠脸吃饭 là sống nhờ khuôn mặt, một câu nói đùa trên mạng.")])

add("bullets", section="Mẫu câu 重点句型", title="8. 反倒 fǎndào – trái lại, ngược lại", size=34,
    items=["Phó từ ngữ khí: trái lại (= 反而) – kết quả ngược với lẽ thường hoặc điều dự đoán",
           "Mẫu thường gặp: （不但不/没）……，反倒……",
           "这反倒说明，那个时候大家更多的是挑选自己想去的学校和专业……",
           "爸妈都很担心他走不出高考失利阴影，他自己反倒很想得开，决定复读明年再考。",
           "爷爷用钢笔写字不顺手，用毛笔反倒得心应手。"],
    say=["Điểm thứ tám: 反倒. Chữ thứ hai đọc thanh bốn.",
         F(0, "反倒 là phó từ ngữ khí, nghĩa là trái lại, ngược lại, giống 反而. Nó cho biết kết quả trái với lẽ thường hoặc với điều người ta dự đoán."),
         F(1, "Mẫu thường gặp: 不但不……，反倒……, không những không…, trái lại còn…."),
         F(2, "Ví dụ một, trong bài khóa: 这反倒说明，那个时候大家更多的是挑选自己想去的学校和专业。 Việc chọn trường kỳ lạ ấy, trái lại, cho thấy thời đó mọi người được tự do chọn."),
         F(3, "Ví dụ hai: 爸妈都很担心他走不出高考失利阴影，他自己反倒很想得开，决定复读明年再考。 Bố mẹ rất lo cậu ấy không vượt qua được cú sốc thi trượt, bản thân cậu ấy trái lại rất thoải mái, quyết định ôn lại để sang năm thi tiếp. 复读 là học lại một năm để thi lại, rất phổ biến ở Trung Quốc."),
         F(4, "Ví dụ ba: 爷爷用钢笔写字不顺手，用毛笔反倒得心应手。 Ông nội viết bút máy không quen tay, viết bút lông thì trái lại rất thuần thục. 得心应手 là thành ngữ, nghĩa là làm việc gì đó rất thuận tay, thành thạo.")])

add("compare", section="Mẫu câu 重点句型", title="Phân biệt 偏偏 và 明明",
    common="Hai phó từ hay đi cùng nhau: 明明……，却/但是偏偏…… (rõ ràng là…, vậy mà lại cứ…)",
    cols=[{"head": "偏偏",
           "lines": ["Cố ý làm trái lẽ thường; hoặc sự việc xảy ra trái ý muốn",
                     "Đúng: 别人都同意，他偏偏反对。",
                     "Đúng: 我去找他，他偏偏不在家。"]},
          {"head": "明明",
           "lines": ["Rõ ràng là (sự thật hiển nhiên), vế sau thường chuyển ý, trách móc",
                     "Đúng: 这个观点明明是错误的，为什么还有那么多支持者？",
                     "Sai: 这个观点偏偏是错误的……"]}],
    say=["Vì 偏偏 và 明明 hay đứng cạnh nhau, nhiều bạn dễ nhầm. Bài tập hai của sách cũng có một câu kiểm tra điểm này, nên chúng ta phân biệt luôn.",
         F(0, "偏偏 diễn tả cố ý làm trái với lẽ thường, như 别人都同意，他偏偏反对, ai cũng đồng ý, anh ta lại cứ phản đối. Nó còn diễn tả sự việc xảy ra trái với mong muốn, như 我去找他，他偏偏不在家, tôi đi tìm anh ấy, thì anh ấy lại không có nhà."),
         F(1, "Còn 明明 nghĩa là rõ ràng là, nhấn mạnh một sự thật hiển nhiên, vế sau thường chuyển ý hoặc trách móc. Ví dụ: 这个观点明明是错误的，为什么还有那么多支持者？ Quan điểm này rõ ràng là sai, sao vẫn có nhiều người ủng hộ thế?"),
         F(1, "Câu này không thể dùng 偏偏, vì ở đây không có ai cố ý làm trái điều gì, chỉ nêu một sự thật hiển nhiên. Mẹo nhớ: 明 là sáng, rõ, nên 明明 là rõ ràng; 偏 là lệch, nên 偏偏 là cố tình lệch khỏi lẽ thường.")])

add("bullets", chapter="Mẫu câu: 并非 · 无论如何 · 相反的是", section="Mẫu câu 重点句型", title="9. 并非 bìngfēi – hoàn toàn không phải", size=36,
    items=["Động từ: hoàn toàn không phải (= 并不是); văn viết, phủ định mạnh điều người ta tưởng",
           "然而毛坦厂中学并非如此，毛坦厂相当多的学生是打工者的孩子……",
           "他这样做并非发自内心。",
           "生活中并非件件事都能称心如意。"],
    say=["Điểm thứ chín: 并非.",
         F(0, "并非 nghĩa là hoàn toàn không phải, bằng 并不是. Đây là cách nói văn viết, dùng để phủ định mạnh điều người ta tưởng hoặc điều vừa nói. Chữ 非 Hán Việt là phi, nghĩa là không phải, như trong phi pháp."),
         F(1, "Ví dụ một, trong bài khóa: 然而毛坦厂中学并非如此，毛坦厂相当多的学生是打工者的孩子。 Người ta tưởng trường luyện thi nào cũng toàn con nhà giàu, nhưng Mao Thản Xưởng hoàn toàn không phải vậy."),
         F(2, "Ví dụ hai: 他这样做并非发自内心。 Anh ấy làm như vậy hoàn toàn không phải xuất phát từ đáy lòng."),
         F(3, "Ví dụ ba: 生活中并非件件事都能称心如意。 Trong cuộc sống không phải việc gì cũng được như ý. 称心如意 là vừa lòng như ý.")])

add("bullets", section="Mẫu câu 重点句型", title="10. 无论如何……都 – dù thế nào… cũng…", size=34,
    items=["Bất kể điều kiện ra sao, kết quả vẫn không thay đổi",
           "Phía sau thường là phủ định hoặc quyết tâm: 无论如何都不肯…… / 无论如何都要……",
           "把高考作为人生梦想是可喜和值得鼓励的，无论如何我都做不出任何嘲讽毛坦厂中学的事情。",
           "她知道你今天也出席这个会议，便找借口说身体不舒服，无论如何都不肯来了。",
           "要成就一番事业，就必须抱有“无论如何都要干到底”的决心。"],
    say=["Điểm thứ mười: 无论如何……都.",
         F(0, "Mẫu này nghĩa là dù thế nào đi nữa… cũng…, biểu thị bất kể điều kiện ra sao, kết quả vẫn không thay đổi."),
         F(1, "Phía sau thường là một câu phủ định hoặc một quyết tâm: 无论如何都不肯, nhất định không chịu; 无论如何都要, bằng mọi giá phải."),
         F(2, "Ví dụ một, trong bài khóa: 把高考作为人生梦想是可喜和值得鼓励的，无论如何我都做不出任何嘲讽毛坦厂中学的事情。 Dù thế nào tôi cũng không thể làm điều gì chế giễu trường Mao Thản Xưởng."),
         F(3, "Ví dụ hai: 她知道你今天也出席这个会议，便找借口说身体不舒服，无论如何都不肯来了。 Cô ấy biết hôm nay cậu cũng dự cuộc họp này, liền lấy cớ không khỏe, nhất định không chịu đến. 找借口 là kiếm cớ."),
         F(4, "Ví dụ ba: 要成就一番事业，就必须抱有无论如何都要干到底的决心。 Muốn làm nên sự nghiệp, phải có quyết tâm dù thế nào cũng làm đến cùng.")])

add("bullets", section="Mẫu câu 重点句型", title="11. 相反的是 – ngược lại là…", size=34,
    items=["Nêu ra sự thật trái với điều vừa nói hoặc điều người ta tưởng",
           "……更多应该是谈高考、谈梦想，相反的是，那个时候更多谈人生，其中谈发财、物质只有一两个，少之又少。",
           "他从没有抱怨过任务多，相反的是一直在努力完成工作。",
           "很多人觉得过度节食可以快速减肥，相反的是，它可能会导致身体虚弱。"],
    say=["Điểm cuối cùng: 相反的是.",
         F(0, "相反的是 nghĩa là ngược lại là, dùng để nêu ra một sự thật trái với điều vừa nói, hoặc trái với điều người ta thường tưởng. Đây cũng là một từ nối rất hay dùng trong văn nghị luận."),
         F(1, "Ví dụ một, trong bài khóa: 更多应该是谈高考、谈梦想，相反的是，那个时候更多谈人生。 Lẽ ra phải bàn về thi cử, về ước mơ, nhưng ngược lại, hồi đó mọi người bàn về lẽ sống nhiều hơn."),
         F(2, "Ví dụ hai: 他从没有抱怨过任务多，相反的是一直在努力完成工作。 Anh ấy chưa bao giờ than phiền nhiều việc, ngược lại luôn cố gắng hoàn thành công việc."),
         F(3, "Ví dụ ba: 很多人觉得过度节食可以快速减肥，相反的是，它可能会导致身体虚弱。 Nhiều người nghĩ nhịn ăn quá mức có thể giảm cân nhanh, nhưng ngược lại, nó có thể khiến cơ thể suy nhược. 节食 là ăn kiêng.")])

# ======================= KẾT HỢP TỪ & THÀNH NGỮ =======================
add("bullets", chapter="Kết hợp từ & thành ngữ", section="Kết hợp từ 词语搭配", title="Kết hợp từ (1): 改动 · 持 · 门槛 · 轮流", size=33,
    items=["## 改动 + N: ～内容 · ～词句 · ～文字 · ～顺序",
           "你的这篇文章我只改动了个别词句。",
           "## 持 + thái độ, quan điểm: ～反对态度 · ～相反观点 · ～一致立场",
           "调查显示，44%的受访者认为数字货币利大于弊，其他人持相反观点。",
           "## 门槛: ～高 · ～低 · 没有～ · 降低～",
           "政府为了鼓励毕业生创业，降低了中小企业注册的门槛。",
           "## 轮流 + V: ～做饭 · ～休息 · ～开车 · ～值班 · ～发言",
           "我们总行程约有近一千公里，四个人轮流开车。"],
    say=["Tiếp theo là phần 词语搭配, kết hợp từ. Học từ theo cụm sẽ giúp các bạn dùng từ tự nhiên như người bản ngữ.",
         F(0, "改动 đi với tân ngữ chỉ văn bản, thứ tự: 改动内容，改动词句，改动文字，改动顺序."),
         F(1, "Ví dụ: 你的这篇文章我只改动了个别词句。 Bài văn này của cậu, tôi chỉ sửa một vài câu chữ."),
         F(2, "持 đi với thái độ, quan điểm, lập trường: 持反对态度，持相反观点，持一致立场. Ngoài ra còn có 持不同政见者, người có chính kiến khác."),
         F(3, "Ví dụ: 调查显示，百分之四十四的受访者认为数字货币利大于弊，其他人持相反观点。 Khảo sát cho thấy bốn mươi bốn phần trăm người được hỏi cho rằng tiền kỹ thuật số lợi nhiều hơn hại, những người khác giữ quan điểm ngược lại."),
         F(4, "门槛 đi với cao, thấp: 门槛高，门槛低，没有门槛，降低门槛."),
         F(5, "Ví dụ: 政府为了鼓励毕业生创业，降低了中小企业注册的门槛。 Để khuyến khích sinh viên tốt nghiệp khởi nghiệp, chính phủ đã hạ thấp ngưỡng đăng ký doanh nghiệp vừa và nhỏ."),
         F(6, "轮流 đứng trước động từ: 轮流做饭，轮流休息，轮流开车，轮流值班，轮流发言."),
         F(7, "Ví dụ: 我们总行程约有近一千公里，四个人轮流开车。 Tổng hành trình của chúng tôi gần một nghìn cây số, bốn người thay phiên nhau lái xe.")])

add("bullets", section="Kết hợp từ 词语搭配", title="Kết hợp từ (2): 寄托 · 门路 · 渺茫 · 寒门", size=33,
    items=["## 寄托 + N: ～梦想 · ～哀思 · ～希望 · ～感情",
           "赏月是中国自古以来的中秋节习俗，寄托着人们对“天上月儿圆，世间人团圆”的美好心愿。",
           "## 门路: 走～ · 跑～ · 找～ · ～多 · ～广",
           "大山里的孩子没有别的门路，高考几乎是改变命运的唯一机会。",
           "## 渺茫: 希望～ · 前途～ · 机会～ · 感觉很～",
           "马上就要毕业了，我还没有找到合适的工作，难免会觉得前途渺茫。",
           "## 寒门: 出身～ · ～学子 · ～出贵子",
           "很多优秀的运动员出身寒门，他们通过努力成为世界冠军。"],
    say=[F(0, "寄托 đi với những thứ trừu tượng: 寄托梦想，寄托希望，寄托感情, và 寄托哀思, gửi gắm nỗi tiếc thương người đã khuất."),
         F(1, "Ví dụ: 赏月是中国自古以来的中秋节习俗，寄托着人们对天上月儿圆，世间人团圆的美好心愿。 Ngắm trăng là phong tục Trung thu từ xưa của Trung Quốc, gửi gắm mong ước tốt đẹp: trên trời trăng tròn, dưới đất người đoàn viên."),
         F(2, "门路 đi với 走，跑，找: 走门路，跑门路，找门路, đều là chạy chọt, tìm đường dây. Ngoài ra còn có 门路多，门路广, nhiều đường dây, quan hệ rộng."),
         F(3, "Ví dụ: 大山里的孩子没有别的门路，高考几乎是改变命运的唯一机会。 Trẻ em vùng núi không có con đường nào khác, thi đại học gần như là cơ hội duy nhất để thay đổi số phận."),
         F(4, "渺茫 đi với 希望，前途，机会: 希望渺茫，前途渺茫，机会渺茫."),
         F(5, "Ví dụ: 马上就要毕业了，我还没有找到合适的工作，难免会觉得前途渺茫。 Sắp tốt nghiệp rồi mà tôi vẫn chưa tìm được việc phù hợp, khó tránh khỏi cảm thấy tương lai mờ mịt."),
         F(6, "寒门: 出身寒门, xuất thân nhà nghèo; 寒门学子, học trò nhà nghèo; và câu 寒门出贵子, nhà nghèo sinh con quý."),
         F(7, "Ví dụ: 很多优秀的运动员出身寒门，他们通过努力成为世界冠军。 Nhiều vận động viên xuất sắc xuất thân nhà nghèo, nhờ nỗ lực mà trở thành nhà vô địch thế giới.")])

add("bullets", section="Thành ngữ 成语", title="Thành ngữ (成语)", size=34,
    items=["## 国家兴亡，匹夫有责 – đất nước hưng vong, mỗi người dân đều có trách nhiệm",
           "在战争年代，许多年轻人都抱着“国家兴亡，匹夫有责”的信念，扛起枪上了前线。",
           "## 莫名其妙 – chuyện kỳ lạ, không giải thích nổi (名: nói ra)",
           "比赛即将开始，一名运动员突然离开赛场，他这一举动让在场所有观众都感到莫名其妙。",
           "## 费尽心机 – vắt óc nghĩ mọi cách (心机: mưu kế)",
           "为了得到这份好工作，他费尽心机，到处托关系找人帮忙。"],
    say=["Bài này có ba thành ngữ.",
         F(0, "Thứ nhất: 国家兴亡，匹夫有责. Nghĩa là việc lớn hưng vong của đất nước, mỗi người dân thường đều có trách nhiệm. 匹夫 là người đàn ông bình thường. Câu này xuất phát từ tư tưởng của học giả 顾炎武 đời Minh Thanh."),
         F(1, "Ví dụ: 在战争年代，许多年轻人都抱着国家兴亡，匹夫有责的信念，扛起枪上了前线。 Trong những năm chiến tranh, rất nhiều thanh niên mang niềm tin ấy, vác súng ra tiền tuyến."),
         F(2, "Thứ hai: 莫名其妙. Chữ 名 ở đây nghĩa là nói ra: không ai nói ra được cái lẽ của nó, tức là chuyện kỳ lạ, không giải thích nổi. Tiếng Việt hay dịch là chẳng hiểu ra sao, khó hiểu."),
         F(3, "Ví dụ: 比赛即将开始，一名运动员突然离开赛场，他这一举动让在场所有观众都感到莫名其妙。 Trận đấu sắp bắt đầu, một vận động viên bỗng rời sân, hành động này khiến toàn bộ khán giả cảm thấy khó hiểu."),
         F(4, "Thứ ba: 费尽心机. 费尽 là dùng hết, 心机 là mưu kế, tâm cơ: vắt óc nghĩ đủ mọi cách. Thành ngữ này thường hơi mang ý chê."),
         F(5, "Ví dụ: 为了得到这份好工作，他费尽心机，到处托关系找人帮忙。 Để có được công việc tốt này, anh ta vắt óc đủ mọi cách, khắp nơi nhờ vả quan hệ. 托关系 là nhờ cậy quan hệ.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 趁热打铁", title="Bài tập 1: Chọn từ điền vào chỗ trống (1)", reveal=True, size=36,
    items=["## Từ cho sẵn: 赞赏 · 人脉 · 莫名其妙 · 费尽心机 · 改动 · 嘲讽",
           "(1) 为了劝说客户在这个项目上投资，他真的是___。",
           "Đáp án: 费尽心机",
           "(2) 我们只在文章的结尾处做了___，其他部分仍然保持原样。",
           "Đáp án: 改动",
           "(3) 对犯错误的人，我们不应该___他们。",
           "Đáp án: 嘲讽"],
    say=["Bây giờ là phần luyện tập của sách, 趁热打铁, nghĩa đen là rèn sắt khi còn nóng. Bài tập một: chọn từ cho sẵn điền vào chỗ trống.",
         F(0, "Có sáu từ: 赞赏，人脉，莫名其妙，费尽心机，改动，嘲讽."),
         F(1, "Câu một: 为了劝说客户在这个项目上投资，他真的是什么。 Để thuyết phục khách hàng đầu tư vào dự án này, anh ấy thật là…. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 费尽心机. 他真的是费尽心机, anh ấy thật đã vắt óc nghĩ đủ mọi cách."),
         F(3, "Câu hai: 我们只在文章的结尾处做了什么，其他部分仍然保持原样。 Chúng tôi chỉ… ở phần cuối bài, các phần khác vẫn giữ nguyên."),
         F(4, "Đáp án: 改动. 做了改动, đã sửa đổi. Vế sau 保持原样, giữ nguyên, là gợi ý."),
         F(5, "Câu ba: 对犯错误的人，我们不应该什么他们。 Đối với người phạm lỗi, chúng ta không nên… họ."),
         F(6, "Đáp án: 嘲讽. 不应该嘲讽他们, không nên chế giễu họ.")])

add("bullets", section="Luyện tập 趁热打铁", title="Bài tập 1: Chọn từ điền vào chỗ trống (2)", reveal=True, size=36,
    items=["## Từ cho sẵn: 赞赏 · 人脉 · 莫名其妙 · 费尽心机 · 改动 · 嘲讽",
           "(4) 中国人常说“一个好汉三个帮”，也就是说，人要想做成大事，背后的___关系非常重要。",
           "Đáp án: 人脉",
           "(5) 在学校举办的英语竞赛中，李明的演讲赢得现场评委和观众的一致___。",
           "Đáp án: 赞赏",
           "(6) 今天我刚一到家，妈妈就把我大骂一顿，真是___。",
           "Đáp án: 莫名其妙"],
    say=[F(1, "Câu bốn: 中国人常说一个好汉三个帮，也就是说，人要想做成大事，背后的什么关系非常重要。 Người Trung Quốc thường nói một người hảo hán cần ba người giúp, nghĩa là muốn làm nên việc lớn, mối quan hệ… phía sau rất quan trọng."),
         F(2, "Đáp án: 人脉. 人脉关系, các mối quan hệ. Câu 一个好汉三个帮 giống câu một cây làm chẳng nên non của tiếng Việt."),
         F(3, "Câu năm: 在学校举办的英语竞赛中，李明的演讲赢得现场评委和观众的一致什么。 Trong cuộc thi tiếng Anh do trường tổ chức, bài hùng biện của Lý Minh giành được sự… nhất trí của ban giám khảo và khán giả."),
         F(4, "Đáp án: 赞赏. 赢得一致赞赏, giành được sự khen ngợi nhất trí."),
         F(5, "Câu sáu: 今天我刚一到家，妈妈就把我大骂一顿，真是什么。 Hôm nay tôi vừa về đến nhà, mẹ đã mắng cho một trận, thật là…."),
         F(6, "Đáp án: 莫名其妙. Bị mắng mà không hiểu vì sao, thật là khó hiểu.")])

add("bullets", section="Luyện tập 趁热打铁", title="Bài tập 2: Chọn đáp án đúng (1)", reveal=True, size=33,
    items=["(1) 改变（ ）教育的体制不等于放弃考试，而是老师要更多地开发学生的潜能。  A.应考  B.笔试  C.面试  D.应试",
           "Đáp án: D – 应试教育: giáo dục chạy theo thi cử",
           "(2) 并不是每个人都能自由（ ）自己未来要走的路，许多孩子都因为家庭太贫穷而放弃了自己的梦想。  A.挑选  B.采取  C.抉择  D.判断",
           "Đáp án: C – 抉择: lựa chọn hệ trọng (con đường đời); 挑选 dùng khi chọn đồ vật, người trong nhiều thứ",
           "(3) 世界上有很多（ ）的事，我们还很难用科学的观点解释。  A.莫名其妙  B.岂有此理  C.稀里糊涂  D.恍然大悟",
           "Đáp án: A – 莫名其妙: kỳ lạ, không giải thích nổi"],
    say=["Bài tập hai: chọn một đáp án đúng.",
         F(0, "Câu một: 改变什么教育的体制不等于放弃考试，而是老师要更多地开发学生的潜能。 Thay đổi thể chế giáo dục… không có nghĩa là bỏ thi cử, mà là giáo viên phải khai thác tiềm năng của học sinh nhiều hơn. Bốn lựa chọn: 应考，笔试，面试，应试."),
         F(1, "Đáp án: D, 应试. 应试教育 là cụm cố định, giáo dục chạy theo thi cử. 应考 là động từ, đi thi; 笔试 là thi viết; 面试 là phỏng vấn."),
         F(2, "Câu hai: 并不是每个人都能自由什么自己未来要走的路，许多孩子都因为家庭太贫穷而放弃了自己的梦想。 Không phải ai cũng có thể tự do… con đường tương lai của mình, nhiều đứa trẻ đã từ bỏ ước mơ vì gia đình quá nghèo. Lựa chọn: 挑选，采取，抉择，判断."),
         F(3, "Đáp án: C, 抉择. 抉择 là lựa chọn hệ trọng, như chọn con đường đời. 挑选 thường dùng khi chọn đồ vật hay người trong nhiều thứ; 采取 đi với biện pháp; 判断 là phán đoán."),
         F(4, "Câu ba: 世界上有很多什么的事，我们还很难用科学的观点解释。 Trên đời có rất nhiều chuyện…, chúng ta vẫn khó giải thích bằng khoa học. Lựa chọn: 莫名其妙，岂有此理，稀里糊涂，恍然大悟."),
         F(5, "Đáp án: A, 莫名其妙, kỳ lạ không giải thích nổi. 岂有此理 là vô lý hết sức, dùng khi tức giận; 稀里糊涂 là mơ mơ hồ hồ; 恍然大悟 là bừng tỉnh hiểu ra.")])

add("bullets", section="Luyện tập 趁热打铁", title="Bài tập 2: Chọn đáp án đúng (2)", reveal=True, size=33,
    items=["(4) 这个观点（ ）是错误的，真不明白为什么还有那么多支持者？  A.渐渐  B.稍稍  C.偏偏  D.明明",
           "Đáp án: D – 明明: rõ ràng là",
           "(5) 编辑帮他把已经写好的文章（ ）作了修改，没过多久文章就发表了。  A.悄悄  B.偷偷  C.渐渐  D.稍稍",
           "Đáp án: D – 稍稍作了修改: sửa đổi một chút",
           "(6) “别让孩子输在起跑线上”是家长们挂在嘴边的一句话，孩子是家庭的未来，（ ）了全家人的期望。  A.期待  B.托付  C.寄托  D.依靠",
           "Đáp án: C – 寄托了全家人的期望: gửi gắm kỳ vọng của cả nhà"],
    say=[F(0, "Câu bốn: 这个观点什么是错误的，真不明白为什么还有那么多支持者？ Quan điểm này… là sai, thật không hiểu sao vẫn có nhiều người ủng hộ đến vậy. Lựa chọn: 渐渐，稍稍，偏偏，明明."),
         F(1, "Đáp án: D, 明明, rõ ràng là. Đây chính là câu chúng ta vừa phân biệt với 偏偏."),
         F(2, "Câu năm: 编辑帮他把已经写好的文章什么作了修改，没过多久文章就发表了。 Biên tập viên giúp anh ấy… sửa bài viết đã hoàn thành, chẳng bao lâu bài đã được đăng. Lựa chọn: 悄悄，偷偷，渐渐，稍稍."),
         F(3, "Đáp án: D, 稍稍, một chút. Biên tập viên chỉ sửa một chút. 悄悄 và 偷偷 là lặng lẽ, lén lút, không hợp vì biên tập viên giúp sửa một cách công khai; 渐渐 là dần dần."),
         F(4, "Câu sáu: 别让孩子输在起跑线上是家长们挂在嘴边的一句话，孩子是家庭的未来，什么了全家人的期望。 Đừng để con thua ngay từ vạch xuất phát là câu cửa miệng của các bậc phụ huynh; con cái là tương lai của gia đình, … kỳ vọng của cả nhà. Lựa chọn: 期待，托付，寄托，依靠."),
         F(5, "Đáp án: C, 寄托. 寄托了全家人的期望, mang trên mình kỳ vọng của cả nhà. 托付 là giao phó việc cho người khác làm; 依靠 là dựa vào.")])

add("bullets", section="Luyện tập 趁热打铁", title="Bài tập 3: Dùng từ cho sẵn trả lời câu hỏi (1)", reveal=True, size=34,
    items=["(1) 学生在选择专业时要考虑哪些因素？（不只是……更是）",
           "Đáp án gợi ý: 选择专业不只是选择几年的课程，更是选择自己未来的职业和生活，所以要考虑兴趣、能力和就业前景。",
           "(2) 80年代高考和当今高考有哪些异同点？（反倒）",
           "Đáp án gợi ý: 相同的是都要凭分数上大学。不同的是，80年代条件差，大家反倒更自由，能挑选自己喜欢的学校和专业；今天条件好了，很多人却只看学校的名气。"],
    say=["Bài tập ba: dùng từ và mẫu câu cho sẵn để trả lời câu hỏi. Đây là câu hỏi mở, thầy đưa ra đáp án gợi ý; các bạn hãy tự trả lời trước theo ý mình.",
         F(0, "Câu một, dùng 不只是……更是: 学生在选择专业时要考虑哪些因素？ Khi chọn ngành, học sinh cần cân nhắc những yếu tố nào?"),
         F(1, "Đáp án gợi ý: 选择专业不只是选择几年的课程，更是选择自己未来的职业和生活，所以要考虑兴趣、能力和就业前景。 Chọn ngành không chỉ là chọn mấy năm học, mà còn là chọn nghề nghiệp và cuộc sống tương lai, vì vậy cần cân nhắc sở thích, năng lực và triển vọng việc làm."),
         F(2, "Câu hai, dùng 反倒: 八十年代高考和当今高考有哪些异同点？ Thi đại học những năm tám mươi và ngày nay giống và khác nhau thế nào?"),
         F(3, "Đáp án gợi ý: 相同的是都要凭分数上大学。不同的是，八十年代条件差，大家反倒更自由，能挑选自己喜欢的学校和专业；今天条件好了，很多人却只看学校的名气。 Giống nhau là đều dựa vào điểm số để vào đại học. Khác nhau là: những năm tám mươi điều kiện kém, nhưng trái lại mọi người tự do hơn; ngày nay điều kiện tốt hơn, nhiều người lại chỉ nhìn vào danh tiếng của trường.")])

add("bullets", section="Luyện tập 趁热打铁", title="Bài tập 3: Dùng từ cho sẵn trả lời câu hỏi (2)", reveal=True, size=34,
    items=["(3) 有人说：“高考可以改变命运。”对此，你怎么看？（持）",
           "Đáp án gợi ý: 我对这个说法持赞同态度。对寒门孩子来说，高考是最公平的机会之一，虽然不一定拼得过富二代，但能改变自己和家庭的生活。",
           "(4) 对于出身寒门的学生，高考究竟能带给他们什么？（历来）",
           "Đáp án gợi ý: 中国人历来重视读书。对寒门学生来说，高考能带给他们公平竞争的机会、走出大山的道路和改变命运的希望。"],
    say=[F(0, "Câu ba, dùng 持: 有人说：高考可以改变命运。对此，你怎么看？ Có người nói thi đại học có thể thay đổi số phận. Bạn nghĩ sao về điều này?"),
         F(1, "Đáp án gợi ý: 我对这个说法持赞同态度。对寒门孩子来说，高考是最公平的机会之一，虽然不一定拼得过富二代，但能改变自己和家庭的生活。 Tôi tán thành cách nói này. Với con nhà nghèo, thi đại học là một trong những cơ hội công bằng nhất; tuy chưa chắc đua nổi con nhà giàu, nhưng có thể thay đổi cuộc sống của bản thân và gia đình. Nếu không đồng ý, các bạn có thể nói 我对这个说法持怀疑态度."),
         F(2, "Câu bốn, dùng 历来: 对于出身寒门的学生，高考究竟能带给他们什么？ Đối với học sinh xuất thân nhà nghèo, thi đại học rốt cuộc mang lại cho các em điều gì?"),
         F(3, "Đáp án gợi ý: 中国人历来重视读书。对寒门学生来说，高考能带给他们公平竞争的机会、走出大山的道路和改变命运的希望。 Người Trung Quốc xưa nay coi trọng việc học. Với học sinh nhà nghèo, thi đại học mang lại cơ hội cạnh tranh công bằng, con đường ra khỏi núi rừng, và hy vọng thay đổi số phận.")])

add("bullets", section="Luyện tập 趁热打铁", title="Bài tập 4: Chọn từ điền vào đoạn văn", reveal=True, size=33,
    items=["## Từ cho sẵn: 换一个角度 · 涉及 · 持 · 可喜 · 门槛 · 渺茫",
           "据报道，近日江苏省某高中一个班有20多名学生考取北大清华等著名高校，对此多数网友都___积极态度，网络上一片惊叹之声。这样的成绩当然是___的，可___来说，中国的求学者多，名校少，大学的___高，因此，每年高考，依然有不少的学子觉得希望___。要让“残酷”的高考变成“温柔”的高考，需要国家增加对教育事业的投入，合理分配教育资源，这就___到教育体制的改革，在这个方面，中国还有很长的路要走。",
           "Đáp án: 持 · 可喜 · 换一个角度 · 门槛 · 渺茫 · 涉及"],
    say=["Bài tập bốn: chọn từ cho sẵn điền vào đoạn văn.",
         F(0, "Có sáu từ: 换一个角度，涉及，持，可喜，门槛，渺茫."),
         F(1, "Đoạn văn như sau: 据报道，近日江苏省某高中一个班有二十多名学生考取北大清华等著名高校，对此多数网友都什么积极态度，网络上一片惊叹之声。这样的成绩当然是什么的，可什么来说，中国的求学者多，名校少，大学的什么高，因此，每年高考，依然有不少的学子觉得希望什么。要让残酷的高考变成温柔的高考，需要国家增加对教育事业的投入，合理分配教育资源，这就什么到教育体制的改革，在这个方面，中国还有很长的路要走。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 持积极态度，可喜的，可换一个角度来说，大学的门槛高，希望渺茫，涉及到教育体制的改革. Cả đoạn nghĩa là: Theo tin tức, một lớp của một trường cấp ba ở Giang Tô có hơn hai mươi học sinh đỗ Bắc Đại, Thanh Hoa; đa số cư dân mạng có thái độ tích cực. Thành tích như vậy đương nhiên đáng mừng, nhưng nhìn từ góc khác, Trung Quốc người muốn học nhiều mà trường danh tiếng ít, ngưỡng vào đại học cao, nên mỗi mùa thi vẫn có nhiều sĩ tử thấy hy vọng mong manh. Muốn kỳ thi tàn khốc trở nên dịu dàng, nhà nước cần đầu tư nhiều hơn cho giáo dục, phân bổ hợp lý tài nguyên giáo dục, và điều này liên quan đến cải cách thể chế giáo dục.")])

# ======================= THẢO LUẬN =======================
add("bullets", chapter="Thảo luận", section="Thảo luận 讨论", title="Thảo luận: Không thi đại học, có đua nổi con nhà giàu?", reveal=True, size=34,
    items=["(1) 你同意“没有高考，你怎么拼得过富二代”这个说法吗？",
           "Đáp án gợi ý: 按说这样的说法未免过于绝对，可换一个角度，对寒门孩子来说，高考确实是最公平的机会：分数面前人人平等。",
           "(2) 除了高考，年轻人还有哪些改变命运的道路？",
           "Đáp án gợi ý: 职业教育、学一门技术、创业、出国留学……高考并非唯一的出路，但它是成本最低、最公平的一条路。"],
    say=["Bây giờ chúng ta cùng thảo luận. Các bạn hãy thử nói quan điểm của mình bằng tiếng Trung, dùng càng nhiều mẫu câu vừa học càng tốt.",
         F(0, "Câu hỏi một: 你同意没有高考，你怎么拼得过富二代这个说法吗？ Bạn có đồng ý với câu nói: không có thi đại học, bạn làm sao đua nổi con nhà giàu?"),
         F(1, "Gợi ý: 按说这样的说法未免过于绝对，可换一个角度，对寒门孩子来说，高考确实是最公平的机会：分数面前人人平等。 Cách nói này hơi tuyệt đối, nhưng nhìn từ góc khác, với con nhà nghèo, thi đại học đúng là cơ hội công bằng nhất: trước điểm số, mọi người đều bình đẳng. Các bạn để ý, câu trả lời này dùng lại đúng ba mẫu câu đầu tiên của bài."),
         F(2, "Câu hỏi hai: 除了高考，年轻人还有哪些改变命运的道路？ Ngoài thi đại học, người trẻ còn có những con đường nào để thay đổi số phận?"),
         F(3, "Gợi ý: 职业教育、学一门技术、创业、出国留学……高考并非唯一的出路，但它是成本最低、最公平的一条路。 Giáo dục nghề nghiệp, học một nghề, khởi nghiệp, du học…. Thi đại học hoàn toàn không phải lối thoát duy nhất, nhưng là con đường ít tốn kém và công bằng nhất.")])

add("bullets", section="Thảo luận 讨论", title="Liên hệ Việt Nam: kỳ thi tốt nghiệp THPT", size=36,
    items=["Việt Nam: 高中毕业考试 (thi tốt nghiệp THPT) dùng để xét tuyển đại học – “cuộc chiến” của cả gia đình",
           "寒门出贵子: nhiều thủ khoa xuất thân nông thôn, nhà nghèo – “học để đổi đời”",
           "Lò luyện thi, trường chuyên lớp chọn, học thêm – rất giống 应试教育 và 高考名校",
           "Thử nói: 在越南，人们历来……；高考不只是……，更是……"],
    say=["Chúng ta liên hệ với Việt Nam.",
         F(0, "Ở Việt Nam, kỳ thi tốt nghiệp trung học phổ thông, tiếng Trung có thể gọi là 越南的高中毕业考试, được dùng để xét tuyển đại học. Mỗi mùa thi, cả gia đình cùng lo lắng, giống hệt cảnh 上万人守着大客车 ở Mao Thản Xưởng."),
         F(1, "Ở Việt Nam cũng có rất nhiều câu chuyện thủ khoa xuất thân từ nông thôn, nhà nghèo, học để đổi đời. Đó chính là tinh thần 寒门出贵子 trong bài."),
         F(2, "Bên cạnh đó, lò luyện thi, trường chuyên lớp chọn, học thêm tràn lan cũng khiến nhiều người lo ngại, rất giống những vấn đề của 应试教育 và 高考名校 mà tác giả nhắc đến."),
         F(3, "Các bạn hãy thử nói vài câu về Việt Nam, ví dụ: 在越南，人们历来重视读书；高中毕业考试不只是一场考试，更是很多家庭改变命运的希望。 Ở Việt Nam, người ta xưa nay coi trọng việc học; kỳ thi tốt nghiệp không chỉ là một kỳ thi, mà còn là hy vọng đổi đời của nhiều gia đình.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 1.1", size=34,
    items=["Từ vựng trọng tâm: 按说 · 未免 · 尊严 · 历来 · 稍稍 · 偏偏 · 反倒 · 持 · 门槛 · 并非 · 卑微 · 寄托 · 嘲讽 · 门路 · 人脉 · 渺茫 · 寒门",
           "Mẫu câu (1): 按说……可…… · 未免太…… · 换一个角度（来看） · 不只是……，更是……",
           "Mẫu câu (2): 历来 · 稍稍 · 明明……偏偏…… · 反倒 · 并非 · 无论如何……都 · 相反的是",
           "Thành ngữ: 国家兴亡，匹夫有责 · 莫名其妙 · 费尽心机",
           "## Bài tập về nhà",
           "Viết đoạn văn khoảng 300 chữ: 高考（或越南的高中毕业考试）能改变命运吗？ – dùng ít nhất 5 mẫu câu của bài"],
    say=["Chúng ta cùng tổng kết bài một chấm một.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 按说，未免，尊严，历来，稍稍，偏偏，反倒，持，门槛，并非，卑微，寄托，嘲讽，门路，人脉，渺茫，寒门. Và đừng quên những từ dễ nhầm như 尊严，嘲讽，门路."),
         F(1, "Về mẫu câu, nhóm một: 按说 nêu lẽ thường, vế sau chuyển ý; 未免 phê bình nhẹ nhàng việc quá mức; 换一个角度 đưa ra góc nhìn khác; 不只是……，更是…… nhấn mạnh vế sau quan trọng hơn."),
         F(2, "Nhóm hai: 历来, từ trước đến nay; 稍稍, một chút; 明明……偏偏……, rõ ràng là… vậy mà lại cứ…; 反倒, trái lại; 并非, hoàn toàn không phải; 无论如何……都, dù thế nào cũng; và 相反的是, ngược lại là."),
         F(3, "Ba thành ngữ: 国家兴亡，匹夫有责，莫名其妙，费尽心机."),
         F(5, "Bài tập về nhà: hãy viết một đoạn văn khoảng ba trăm chữ với đề 高考能改变命运吗, hoặc viết về kỳ thi tốt nghiệp trung học phổ thông ở Việt Nam. Hãy dùng ít nhất năm mẫu câu của bài, ví dụ mở đầu bằng 按说, chuyển ý bằng 换一个角度来看, và bày tỏ quan điểm bằng 我持……态度."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Bài sau, bài một chấm hai, vẫn thuộc chủ đề Giáo dục: 学区房情结怎么破？ Làm sao phá bỏ cơn sốt nhà gần trường điểm? Chúng ta sẽ tìm hiểu vì sao phụ huynh Trung Quốc chấp nhận bỏ ra rất nhiều tiền để mua một căn nhà cũ nát gần trường tốt, và nhà gần trường ở nước ngoài có gì khác. Hẹn gặp lại các bạn. Chúc các bạn học tốt!"])

lesson = {
    "title": "顶石中文 – Bài 1.1: 没有高考，你怎么拼得过富二代？ (Không thi đại học, sao đua nổi con nhà giàu?)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"反倒": "反到",            # fǎndào
                    "调转": "掉转",            # diàozhuǎn
                    "调动": "掉动",            # diàodòng
                    "应试": "硬试",            # yìngshì
                    "应考": "硬考",            # yìngkǎo
                    "当神树": "荡神树",        # dàng
                    "为找工作": "位找工作",    # wèi
                    "莘莘": "深深",            # shēnshēn
                    "朝他": "潮他",            # cháo
                    "称心": "趁心",            # chènxīn
                    "复读": "富读",            # fùdú (phòng đọc nhầm)
                    "得心应手": "得心硬手",    # yìng
                    "便找借口": "变找借口",    # biàn
                    "拖泥带水": "拖泥带水"},
    "slides": slides,
}
lesson["tts_replace"].pop("拖泥带水")
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds11.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
