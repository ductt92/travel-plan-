#!/usr/bin/env python3
"""Kịch bản bài giảng 顶石中文 – Bài 5.2 «“养儿防老”变“养子啃老”？». Chạy để sinh ds52.json."""
import json
import os

TAG = "顶石中文 · Bài 5.2 · “养儿防老”变“养子啃老”？"
slides = []


def add(type_, chapter=None, section="", **kw):
    s = {"type": type_, "section": section, **kw}
    if chapter:
        s["chapter"] = chapter
    slides.append(s)


def F(i, t, **kw):
    return {"t": t, "f": i, **kw}


# ======================= MỞ ĐẦU =======================
# Tên bài quá dài cho một dòng chữ cỡ lớn, nên tách làm hai dòng: zh + py (như Bài 40)
add("title", chapter="Mở đầu",
    top="顶石中文 – Đỉnh cao tiếng Trung",
    zh="“养儿防老”", py="变“养子啃老”？",
    vi="Bài 5.2: “Nuôi con phòng già” thành “nuôi con ăn bám”?",
    sub="“Yǎng ér fáng lǎo” biàn “yǎng zǐ kěn lǎo”?\nBài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn trở lại với bài giảng giáo trình 顶石中文, Đỉnh cao tiếng Trung.",
         "Hôm nay chúng ta học bài thứ hai của Đơn vị năm, chủ đề Gia đình: bài năm chấm hai, 养儿防老变养子啃老？ Nghĩa là: Nuôi con phòng già, hay thành nuôi con để con ăn bám?",
         "Người Trung Quốc xưa nay tin rằng nuôi con là để về già có chỗ dựa. Thế nhưng ngày nay, ngày càng nhiều người trưởng thành vẫn sống dựa vào bố mẹ, gọi là 啃老族, đúng nghĩa đen là bộ tộc gặm người già.",
         "Bài khóa, cải biên từ 人民日报海外版, báo Nhân dân bản hải ngoại, phân tích hiện tượng này từ nhiều phía: người trẻ, cha mẹ, pháp luật và xã hội. Người Việt chúng ta cũng có câu trẻ cậy cha, già cậy con, nên chắc chắn các bạn sẽ thấy chủ đề này rất gần gũi."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài bình luận: “啃老族” là ai, vì sao xuất hiện và giải quyết thế nào",
           "Nắm vững 43 từ mới, kèm âm Hán Việt và ví dụ",
           "Câu mẫu: 频频 · 不仅……连……甚至…… · 不免令人…… · 之所以……是因为…… · ……，以…… · 所谓 · 自A自B",
           "Kết hợp từ: 步入 · 索取 · 频繁 · 蔓延 · 变相 · 营造",
           "8 thành ngữ: 养儿防老 · 理所当然 · 天经地义 · 心安理得 · 一厢情愿 · 慷慨解囊 · 水深火热 · 自食其力"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu bài bình luận: 啃老族 là những ai, vì sao hiện tượng này xuất hiện, và gia đình, pháp luật, xã hội nên làm gì."),
         F(1, "Thứ hai, nắm vững bốn mươi ba từ mới, kèm âm Hán Việt, nghĩa và ví dụ."),
         F(2, "Thứ ba, bảy câu mẫu: phó từ 频频; câu tăng tiến 不仅……连……甚至……; cấu trúc 不免令人; câu nhân quả 之所以……是因为……; câu mục đích với 以; từ 所谓; và cấu trúc cố định 自A自B."),
         F(3, "Thứ tư, sáu nhóm kết hợp từ: 步入，索取，频繁，蔓延，变相，营造."),
         F(4, "Thứ năm, tám thành ngữ rất hay dùng khi nói về quan hệ cha mẹ, con cái, như 理所当然，天经地义，心安理得，自食其力."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Suy nghĩ trước bài 课前思考", title="Suy nghĩ trước bài học 课前思考", reveal=True, size=32,
    items=["(1) 你周围有没有成年人还在依赖父母生活？",
           "Đáp án gợi ý: 有。我的一个朋友已经三十岁了，还住在父母家，生活费都是父母给的。",
           "(2) 你觉得成年后花父母的钱是天经地义的吗？",
           "Đáp án gợi ý: 不是。成年人应该自食其力；父母愿意帮助是情分，不是本分。",
           "(3) 成年人在经济上无法独立有没有社会因素的影响？",
           "Đáp án gợi ý: 有。就业难、工资偏低、房价太高，都让年轻人很难独立。",
           "(4) 你觉得什么才意味着成年人的独立？",
           "Đáp án gợi ý: 经济上能养活自己，生活上能照顾自己，遇到问题能自己做决定、承担责任。"],
    say=["Trước khi vào bài, sách đưa ra bốn câu hỏi để chúng ta suy nghĩ. Các bạn hãy tạm dừng video và thử trả lời bằng tiếng Trung trước nhé.",
         F(0, "Câu một: 你周围有没有成年人还在依赖父母生活？ Xung quanh bạn có người trưởng thành nào vẫn sống dựa vào bố mẹ không?"),
         F(1, "Đáp án gợi ý: 有。我的一个朋友已经三十岁了，还住在父母家，生活费都是父母给的。 Có. Một người bạn của tôi đã ba mươi tuổi rồi, vẫn ở nhà bố mẹ, tiền sinh hoạt đều do bố mẹ cho."),
         F(2, "Câu hai: 你觉得成年后花父母的钱是天经地义的吗？ Bạn có cho rằng trưởng thành rồi mà tiêu tiền của bố mẹ là lẽ đương nhiên không? 天经地义 là thành ngữ của bài, nghĩa là lẽ trời đất, đương nhiên đúng."),
         F(3, "Đáp án gợi ý: 不是。成年人应该自食其力；父母愿意帮助是情分，不是本分。 Không. Người trưởng thành nên tự nuôi sống mình; bố mẹ sẵn lòng giúp là vì tình nghĩa, chứ không phải bổn phận. Câu này dùng hai từ mới 情分 và 本分, các bạn sẽ gặp lại trong bài khóa."),
         F(4, "Câu ba: 成年人在经济上无法独立有没有社会因素的影响？ Người trưởng thành không thể độc lập về kinh tế, có phải do ảnh hưởng của yếu tố xã hội không?"),
         F(5, "Đáp án gợi ý: 有。就业难、工资偏低、房价太高，都让年轻人很难独立。 Có. Khó tìm việc, lương thấp, giá nhà quá cao, đều khiến người trẻ khó độc lập."),
         F(6, "Câu bốn: 你觉得什么才意味着成年人的独立？ Theo bạn, thế nào mới là sự độc lập của người trưởng thành?"),
         F(7, "Đáp án gợi ý: 经济上能养活自己，生活上能照顾自己，遇到问题能自己做决定、承担责任。 Về kinh tế tự nuôi được mình, về sinh hoạt tự chăm sóc được mình, gặp chuyện thì tự quyết định và chịu trách nhiệm.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("啃", "kěn", "khẳng", "động từ", "gặm, cắn từng chút một", "小狗正在啃骨头。", "Chú chó nhỏ đang gặm xương.",
     "Động từ, nghĩa là cắn từng chút một, gặm. Từ đây có 啃老, gặm người già, tức là ăn bám bố mẹ; và 啃老族, chỉ những người trưởng thành đã có khả năng tự kiếm sống nhưng vẫn chủ yếu dựa vào bố mẹ nuôi. Khẩu ngữ còn có 啃书本, cặm cụi gặm sách."),
    ("俗话", "súhuà", "tục thoại", "danh từ", "tục ngữ, câu nói dân gian", "俗话说：活到老，学到老。", "Tục ngữ nói: sống đến già, học đến già.",
     "Danh từ, chỉ những câu nói thông tục lưu truyền trong dân gian. Mẫu cố định: 俗话说, tục ngữ có câu. Bài khóa mở đầu bằng 俗话说养儿防老."),
    ("频频", "pínpín", "tần tần", "phó từ", "liên tiếp, nhiều lần liền", "他在台上频频向观众挥手。", "Trên sân khấu, anh ấy liên tục vẫy tay chào khán giả.",
     "Phó từ, nghĩa là liên tục, nhiều lần, đứng trước động từ. Đây là câu mẫu thứ nhất của bài. Chữ 频 cũng có trong 频繁, thường xuyên; 频率, tần suất."),
    ("殷实", "yīnshí", "ân thực", "tính từ", "giàu có, sung túc, khá giả", "他出生在一个殷实的家庭。", "Anh ấy sinh ra trong một gia đình khá giả.",
     "Tính từ, nghĩa là đầy đủ, giàu có, thường nói về gia cảnh: 殷实的家庭, 家境殷实. Văn viết, giống 富裕."),
    ("断奶", "duànnǎi", "đoạn nãi", "động từ", "cai sữa; (bóng) thôi dựa dẫm, tự lập", "孩子一岁多就断奶了。", "Đứa bé hơn một tuổi đã cai sữa.",
     "Động từ ly hợp, nghĩa gốc là cai sữa. Trong bài dùng nghĩa bóng: người lớn mà không chịu cai sữa, tức là vẫn bám lấy bố mẹ. Câu kết của bài: 给巨婴断奶, cai sữa cho những em bé khổng lồ."),
    ("个例", "gèlì", "cá lệ", "danh từ", "trường hợp cá biệt", "这种情况并不是个例。", "Tình huống này không phải là trường hợp cá biệt.",
     "Danh từ, nghĩa là trường hợp riêng lẻ, đặc biệt. Cụm hay gặp: 并非个例, chẳng phải cá biệt, tức là khá phổ biến."),
    ("步入", "bùrù", "bộ nhập", "động từ", "bước vào", "我们已经步入了网络时代。", "Chúng ta đã bước vào thời đại Internet.",
     "Động từ, nghĩa là bước vào, văn viết. Dùng cả cho không gian lẫn giai đoạn: 步入会场, 步入社会, 步入而立之年. Đây là một nhóm kết hợp từ."),
    ("控告", "kònggào", "khống cáo", "động từ", "tố cáo, kiện (lên cơ quan tư pháp)", "她向法院控告了那家公司。", "Cô ấy đã kiện công ty đó lên tòa án.",
     "Động từ, nghĩa là tố cáo, kiện lên cơ quan tư pháp hay cơ quan nhà nước. Sách ghi là danh từ, nhưng trong bài nó làm động từ: 向法院控告父母, kiện bố mẹ lên tòa."),
    ("谋生", "móushēng", "mưu sinh", "động từ", "kiếm sống, mưu sinh", "他年轻时靠卖菜谋生。", "Hồi trẻ ông ấy kiếm sống bằng nghề bán rau.",
     "Động từ, nghĩa là tìm cách kiếm sống. Âm Hán Việt mưu sinh, nghĩa giống hệt. Trong bài: 谋生能力, khả năng tự kiếm sống."),
    ("畸形", "jīxíng", "cơ hình", "tính từ", "dị dạng; méo mó, phát triển lệch lạc", "这种畸形的消费观念必须改变。", "Quan niệm tiêu dùng méo mó này phải thay đổi.",
     "Tính từ, nghĩa gốc là dị dạng, nghĩa rộng là phát triển không bình thường, lệch về một phía: 畸形繁荣, phồn vinh lệch lạc. Trong bài: 畸形的亲情关系, quan hệ tình thân méo mó."),
    ("叹息", "tànxī", "thán tức", "động từ", "thở dài, than thở", "听到这个消息，他不禁叹息了一声。", "Nghe tin này, anh ấy bất giác thở dài một tiếng.",
     "Động từ, nghĩa là thở dài, thể hiện sự thất vọng, bất lực. Trong bài: 不免令人叹息, khó tránh khiến người ta thở dài."),
    ("扶持", "fúchí", "phù trì", "động từ", "nâng đỡ, giúp đỡ", "政府大力扶持小微企业。", "Chính phủ ra sức hỗ trợ các doanh nghiệp nhỏ và siêu nhỏ.",
     "Động từ, nghĩa là dìu dắt, nâng đỡ, giúp đỡ. Trong bài: 需要得到父母的扶持和帮助, cần được bố mẹ nâng đỡ và giúp đỡ."),
    ("孝", "xiào", "hiếu", "động từ", "hiếu thảo, có hiếu với cha mẹ", "中国人常说：百善孝为先。", "Người Trung Quốc thường nói: trăm điều thiện, chữ hiếu đứng đầu.",
     "Động từ, nghĩa là hết lòng phụng dưỡng, kính trọng và vâng lời cha mẹ. Hay gặp 孝顺, hiếu thuận; 孝心, lòng hiếu. Trong bài: 敬老孝老, kính già, hiếu với người già."),
    ("感恩", "gǎn'ēn", "cảm ân", "động từ", "biết ơn, mang ơn", "我们要有一颗感恩的心。", "Chúng ta phải có một trái tim biết ơn.",
     "Động từ, nghĩa là biết ơn ân huệ người khác dành cho mình. Ngày Lễ Tạ ơn gọi là 感恩节. Trong bài: 毫无感恩, chẳng hề biết ơn."),
    ("负疚", "fùjiù", "phụ cứu", "động từ", "áy náy, thấy có lỗi", "他对父母一直心怀负疚。", "Anh ấy luôn cảm thấy áy náy với bố mẹ.",
     "Động từ, nghĩa là tự thấy có lỗi, thấy mình mắc nợ người khác. Chữ 疚 cũng có trong 内疚, áy náy. Trong bài: 没有任何负疚感, chẳng có chút cảm giác áy náy nào."),
    ("困扰", "kùnrǎo", "khốn nhiễu", "động từ", "làm phiền muộn, gây khó khăn", "失眠问题一直困扰着他。", "Chứng mất ngủ cứ hành hạ anh ấy mãi.",
     "Động từ, nghĩa là khiến người ta lo lắng, phiền muộn không yên. Cũng làm danh từ: 成为中国家庭的一大困扰, trở thành một nỗi phiền muộn lớn của các gia đình Trung Quốc."),
    ("急剧", "jíjù", "cấp kịch", "tính từ", "nhanh chóng và dữ dội, đột ngột", "近年来，城市人口急剧增加。", "Những năm gần đây, dân số thành thị tăng vọt.",
     "Tính từ, nghĩa là nhanh mà mạnh. Hay đứng trước động từ chỉ thay đổi: 急剧增加，急剧下降，急剧变化. Trong bài: 急剧转型, chuyển đổi nhanh chóng và mạnh mẽ."),
    ("转型", "zhuǎnxíng", "chuyển hình", "động từ", "chuyển đổi (mô hình, cơ cấu)", "这家工厂正在向高科技企业转型。", "Nhà máy này đang chuyển đổi thành doanh nghiệp công nghệ cao.",
     "Động từ, chỉ sự chuyển biến của cơ cấu kinh tế xã hội, hình thái văn hóa, giá trị quan. Ví dụ trong sách: 由计划经济向市场经济转型, chuyển từ kinh tế kế hoạch sang kinh tế thị trường."),
    ("索取", "suǒqǔ", "sách thủ", "động từ", "đòi, đòi hỏi (tiền, đồ vật)", "他帮助别人从不索取报酬。", "Anh ấy giúp người khác chưa bao giờ đòi thù lao.",
     "Động từ, nghĩa là đòi người khác đưa tiền hay đồ vật cho mình. Trong bài: 从父辈那里索取资源, đòi hỏi nguồn lực từ thế hệ cha mẹ. Đây là một nhóm kết hợp từ."),
    ("应届", "yīngjiè", "ứng giới", "tính từ", "(khóa tốt nghiệp) năm nay", "今年应届毕业生的人数又创新高。", "Số sinh viên tốt nghiệp năm nay lại lập kỷ lục mới.",
     "Tính từ thuộc tính, nghĩa là thuộc khóa này, chỉ dùng cho người tốt nghiệp: 应届毕业生, sinh viên vừa tốt nghiệp khóa năm nay. Chữ đầu đọc thanh một."),
    ("偏", "piān", "thiên", "động từ", "lệch, (cao, thấp) hơn mức chuẩn", "他的体温有点儿偏高。", "Thân nhiệt của anh ấy hơi cao.",
     "Ở đây 偏 là động từ, nghĩa là chênh lệch so với một tiêu chuẩn, thường đi với tính từ: 偏高, hơi cao; 偏低, hơi thấp. Trong bài: 工资偏低，房价、生活成本偏高, lương thì thấp, giá nhà và chi phí sinh hoạt thì cao."),
    ("情分", "qíngfèn", "tình phận", "danh từ", "tình nghĩa, tình cảm", "看在多年朋友的情分上，我帮你一次。", "Nể tình bạn bè bao năm, tôi giúp cậu một lần.",
     "Danh từ, nghĩa là tình cảm, tình nghĩa giữa người với người. Chú ý chữ thứ hai đọc thanh bốn. Câu rất hay trong bài: 帮你是情分而不是本分, giúp con là tình nghĩa chứ không phải bổn phận."),
    ("本分", "běnfèn", "bổn phận", "danh từ", "bổn phận, trách nhiệm vốn có", "照顾孩子是父母的本分。", "Chăm sóc con cái là bổn phận của cha mẹ.",
     "Danh từ, nghĩa là trách nhiệm, nghĩa vụ vốn phải làm. Âm Hán Việt bổn phận, nghĩa giống tiếng Việt. Chữ thứ hai cũng đọc thanh bốn. Nó còn làm tính từ, nghĩa là an phận, đúng mực: 他是个本分人."),
    ("再者", "zàizhě", "tái giả", "liên từ", "hơn nữa, vả lại", "这件衣服太贵了，再者颜色也不好看。", "Cái áo này đắt quá, vả lại màu cũng không đẹp.",
     "Liên từ, biểu thị nói thêm một tầng ý, hay đưa thêm một lý do. Giống 况且, 而且. Trong bài, 首先 rồi 再者, tác giả lần lượt đưa ra các lập luận."),
    ("反思", "fǎnsī", "phản tư", "động từ", "suy ngẫm lại, tự nhìn lại", "失败以后，我们要认真反思。", "Sau thất bại, chúng ta phải nghiêm túc nhìn lại.",
     "Động từ, nghĩa là suy nghĩ lại chuyện đã qua để rút ra bài học. Trong bài: 父母也要反思，是不是教育出了问题？ Cha mẹ cũng phải tự nhìn lại, phải chăng việc giáo dục có vấn đề?"),
    ("溺爱", "nì'ài", "nịch ái", "động từ", "nuông chiều quá mức", "爷爷奶奶太溺爱孙子了。", "Ông bà nội nuông chiều cháu trai quá mức.",
     "Động từ, nghĩa là yêu chiều con cái quá mức. Chữ 溺 là chìm đắm, như 溺水, đuối nước: yêu đến mức chìm đắm. Theo chuyên gia trong bài, đây là nguyên nhân chính sinh ra 啃老族."),
    ("体系", "tǐxì", "thể hệ", "danh từ", "hệ thống, thể chế", "这所大学建立了完整的教学体系。", "Trường đại học này đã xây dựng một hệ thống giảng dạy hoàn chỉnh.",
     "Danh từ, chỉ một chỉnh thể gồm nhiều sự vật hay ý thức liên hệ với nhau. Trong bài: 家族制的传统体系, hệ thống truyền thống của chế độ gia tộc."),
    ("抚养", "fǔyǎng", "phủ dưỡng", "động từ", "nuôi nấng, nuôi dạy (con cái)", "她一个人把三个孩子抚养成人。", "Một mình bà ấy nuôi ba đứa con khôn lớn.",
     "Động từ, nghĩa là yêu thương và nuôi dạy, người trên với người dưới: 抚养子女. Nhớ cặp từ trong bài: 父辈对子辈的抚养责任 và 子辈对父辈的赡养义务. Cha mẹ nuôi con là 抚养, con nuôi cha mẹ là 赡养."),
    ("权益", "quányì", "quyền ích", "danh từ", "quyền lợi", "我们要保护消费者的合法权益。", "Chúng ta phải bảo vệ quyền lợi hợp pháp của người tiêu dùng.",
     "Danh từ, nghĩa là quyền lợi đáng được hưởng, không được xâm phạm. Hay gặp 合法权益. Trong bài: 老年人权益保障条例, Điều lệ bảo đảm quyền lợi người cao tuổi."),
    ("根除", "gēnchú", "căn trừ", "động từ", "trừ tận gốc, xóa bỏ hoàn toàn", "这种疾病已经被彻底根除了。", "Căn bệnh này đã bị xóa sổ hoàn toàn.",
     "Động từ, nghĩa là nhổ tận gốc, xóa bỏ triệt để. Sách cho ví dụ 根除陋习, xóa bỏ hủ tục. Trong bài: 并不能根除啃老现象."),
    ("立法", "lìfǎ", "lập pháp", "động từ", "lập pháp, ban hành luật", "国家正在为保护个人信息立法。", "Nhà nước đang làm luật để bảo vệ thông tin cá nhân.",
     "Động từ, nghĩa là xây dựng, ban hành pháp luật. Âm Hán Việt lập pháp. Trong bài: 通过立法的形式, thông qua hình thức lập pháp."),
    ("蔓延", "mànyán", "mạn diên", "động từ", "lan tràn, lan rộng", "火势迅速向四周蔓延。", "Ngọn lửa nhanh chóng lan ra xung quanh.",
     "Động từ, nghĩa là lan rộng ra xung quanh như dây leo, chữ 蔓 là dây leo. Hay dùng cho lửa, dịch bệnh, và cả hiện tượng xấu: 控制啃老现象的蔓延."),
    ("以", "yǐ", "dĩ", "liên từ", "để, nhằm (biểu thị mục đích)", "我们要多锻炼身体，以增强体质。", "Chúng ta phải tập luyện nhiều, để tăng cường thể chất.",
     "Ở bài này, 以 là liên từ, đứng đầu vế sau, biểu thị mục đích, nghĩa là để, nhằm. Văn viết. Đây là câu mẫu thứ năm."),
    ("所谓", "suǒwèi", "sở vị", "tính từ", "cái gọi là, điều được nói đến", "所谓“啃老族”，是指靠父母生活的成年人。", "Cái gọi là “tộc ăn bám” là chỉ những người trưởng thành sống nhờ bố mẹ.",
     "Tính từ, nghĩa là cái được nói đến, dùng để giải thích một khái niệm. Còn có nghĩa mỉa mai: cái gọi là, tưởng là thế nhưng không phải. Đây là câu mẫu thứ sáu."),
    ("变相", "biànxiàng", "biến tướng", "tính từ", "trá hình, đội lốt", "这种收费其实是变相涨价。", "Khoản thu phí này thực chất là tăng giá trá hình.",
     "Tính từ thuộc tính, nghĩa là nội dung không đổi, chỉ đổi hình thức, thường nói về việc xấu: 变相剥削, bóc lột trá hình. Tiếng Việt biến tướng nghĩa gần giống. Trong bài: 变相的纵容, sự dung túng trá hình."),
    ("隐藏", "yǐncáng", "ẩn tàng", "động từ", "che giấu, ẩn náu", "他把真实的想法隐藏在心里。", "Anh ấy giấu kín suy nghĩ thật trong lòng.",
     "Động từ, nghĩa là giấu đi không để người khác phát hiện. Chữ thứ hai đọc là cáng. Trong bài: 内心也隐藏着无奈与痛苦, trong lòng cũng giấu nỗi bất lực và đau khổ."),
    ("操纵", "cāozòng", "thao túng", "động từ", "thao túng, điều khiển", "这件事背后有人在操纵。", "Đằng sau chuyện này có người đang giật dây.",
     "Động từ, nghĩa là đứng sau điều khiển, sai khiến. Âm Hán Việt thao túng, nghĩa giống tiếng Việt. Trong bài: 被父母强大控制欲所操纵, bị ham muốn kiểm soát mạnh mẽ của bố mẹ thao túng."),
    ("焦灼", "jiāozhuó", "tiêu chước", "tính từ", "nóng ruột, sốt ruột, lo cuống", "他焦灼地等待着考试结果。", "Anh ấy nóng ruột chờ đợi kết quả thi.",
     "Tính từ, nghĩa là cực kỳ sốt ruột, lo lắng như bị lửa đốt. 焦 là cháy sém, 灼 là đốt nóng. Trong bài: 内心焦灼不安, trong lòng bồn chồn bất an."),
    ("无异于", "wúyìyú", "vô dị ư", "động từ", "không khác gì, chẳng khác nào", "酒后开车无异于拿生命开玩笑。", "Lái xe sau khi uống rượu chẳng khác nào đùa với tính mạng.",
     "Động từ, nghĩa là không khác gì. Sách cho ví dụ: 一个人如果没有梦想，无异于死掉, một người nếu không có ước mơ thì chẳng khác gì đã chết. Trong bài: 无异于陷入另一种水深火热之中."),
    ("信赖", "xìnlài", "tín lại", "động từ", "tin cậy, tin tưởng và dựa vào", "他是一个值得信赖的朋友。", "Anh ấy là một người bạn đáng tin cậy.",
     "Động từ, nghĩa là tin tưởng và dựa vào. Mạnh hơn 信任 một chút vì có ý dựa vào. Trong bài: 两代人过着既彼此信赖又各自独立的生活."),
    ("人格", "réngé", "nhân cách", "danh từ", "nhân cách, phẩm cách", "父母要尊重孩子的人格。", "Cha mẹ phải tôn trọng nhân cách của con cái.",
     "Danh từ, chỉ tổng thể tính cách, khí chất, năng lực của một người, cũng chỉ phẩm chất đạo đức. Trong bài: 健全的人格, nhân cách lành mạnh."),
    ("营造", "yíngzào", "doanh tạo", "động từ", "tạo nên, xây dựng (bầu không khí)", "学校为学生营造了良好的学习环境。", "Nhà trường đã tạo dựng một môi trường học tập tốt cho học sinh.",
     "Động từ, nghĩa gốc là xây dựng nhà cửa; nay hay dùng nghĩa tạo ra một cách có kế hoạch: 营造气氛，营造环境. Đây là một nhóm kết hợp từ."),
    ("绝迹", "juéjì", "tuyệt tích", "động từ", "biến mất hoàn toàn, tuyệt tích", "由于乱伐森林，这里的野生动物已经绝迹了。", "Vì nạn phá rừng, động vật hoang dã ở đây đã biến mất hoàn toàn.",
     "Động từ, nghĩa là mất hết dấu vết, hoàn toàn không còn xuất hiện. Câu kết của bài: 让啃老绝迹, khiến hiện tượng ăn bám bố mẹ không còn nữa."),
]

add("bullets", chapter="Từ mới (43 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 5.2 có 43 từ mới, chia thành 15 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 情分 · 本分 (fèn) · 应届 (yīng) · 隐藏 (cáng) · 蔓延 (màn)",
           "Cặp dễ nhầm: 抚养 (nuôi con) ≠ 赡养 (nuôi cha mẹ) · 情分 ≠ 本分"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có bốn mươi ba từ, thầy chia thành mười lăm nhóm nhỏ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số chữ có nhiều cách đọc: trong 情分 và 本分, chữ thứ hai đọc thanh bốn; trong 应届, chữ đầu đọc thanh một; trong 隐藏, chữ thứ hai đọc là cáng; còn 蔓延 đọc là mànyán."),
         F(4, "Ngoài ra, hãy chú ý hai cặp từ: 抚养 là nuôi con, 赡养 là nuôi cha mẹ; 情分 là tình nghĩa, 本分 là bổn phận. Chúng ta bắt đầu.")])

sizes = [3] * 13 + [2, 2]
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
add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Kiến thức nền (注释) trước khi đọc", size=34,
    items=["## 啃老族 – “tộc ăn bám” (吃老族 · 傍老族 · 尼特族 = NEET)",
           "Không đi học, không đi làm, không học nghề; ở Trung Quốc thường chỉ người 23–30 tuổi có khả năng kiếm sống nhưng vẫn sống nhờ bố mẹ",
           "## 而立之年 – tuổi ba mươi (dùng cho nam giới)",
           "《论语·为政》：“吾十有五而志于学，三十而立，四十而不惑。”",
           "## 巨婴 – “em bé khổng lồ”",
           "Người lớn mà tâm lý vẫn như trẻ sơ sinh: dựa dẫm, lấy mình làm trung tâm; một trong 10 từ thịnh hành năm 2018"],
    say=["Bây giờ chúng ta sang phần hai: bài khóa. Trước khi đọc, các bạn cần biết ba khái niệm mà sách chú thích.",
         F(0, "Thứ nhất: 啃老族, còn gọi là 吃老族，傍老族, hoặc 尼特族, phiên âm từ chữ viết tắt tiếng Anh NEET, xuất hiện đầu tiên ở Anh."),
         F(1, "Đó là những người không học lên, không đi làm, không học nghề, cả ngày không có việc gì làm. Ở Trung Quốc, chủ yếu chỉ những người trẻ từ hai mươi ba đến ba mươi tuổi, có khả năng kiếm sống nhưng vẫn chưa cai sữa, sống nhờ bố mẹ. Các nhà xã hội học gọi họ là nhóm thất nghiệp mới."),
         F(2, "Thứ hai: 而立之年, tức là tuổi ba mươi, thường dùng cho nam giới."),
         F(3, "Cụm này xuất phát từ sách Luận ngữ, Khổng Tử nói: 吾十有五而志于学，三十而立，四十而不惑。 Ta mười lăm tuổi dốc chí vào việc học, ba mươi tuổi tự lập, bốn mươi tuổi không còn nghi hoặc. Người Việt cũng nói tam thập nhi lập, chính là câu này. Ba mươi tuổi là lúc phải tự lập về nhân cách, học vấn và sự nghiệp."),
         F(4, "Thứ ba: 巨婴, nghĩa đen là đứa bé khổng lồ."),
         F(5, "Nay người ta dùng từ này để chỉ người trưởng thành mà tâm lý vẫn dừng lại ở giai đoạn trẻ sơ sinh: quá dựa dẫm vào gia đình, lấy bản thân làm trung tâm, thiếu tinh thần trách nhiệm, hễ không vừa ý là khóc lóc, la hét. 巨婴 là một trong mười từ thịnh hành năm hai nghìn không trăm mười tám do tạp chí 咬文嚼字 công bố.")])

# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung nếu khác])
P = [
    ("俗话说“养儿防老”，然而，现代社会却频频出现“养子啃老”的现象，不仅殷实的家庭有“啃老”的孩子，连并不富裕的家庭也常出现不肯“断奶”的孩子，甚至小两口带着孩子一起“啃老”的现象也并非个例。",
     "Tục ngữ nói “nuôi con phòng già”, thế nhưng xã hội hiện đại lại liên tục xuất hiện hiện tượng “nuôi con để con ăn bám”. Không chỉ gia đình khá giả có những đứa con “ăn bám”, ngay cả gia đình chẳng mấy giàu có cũng thường có những đứa con không chịu “cai sữa”, thậm chí hiện tượng vợ chồng trẻ dắt cả con cùng “ăn bám” cũng chẳng phải cá biệt.",
     ["Câu mở đầu đặt hai cụm đối nhau: 养儿防老, nuôi con để phòng khi về già, và 养子啃老, nuôi con để con gặm bố mẹ. 然而 là thế nhưng. 频频出现 là liên tục xuất hiện, câu mẫu thứ nhất.",
      "Câu này dùng mẫu tăng tiến 不仅……连……甚至……: không chỉ nhà giàu, ngay cả nhà không giàu, thậm chí cả vợ chồng trẻ có con. 小两口 là vợ chồng trẻ, khẩu ngữ. 并非个例 là chẳng phải trường hợp cá biệt."]),
    ("湖南长沙一位即将步入而立之年、身体健全的男子，在“啃老”遭到拒绝后，居然还要向法院控告父母的不养之“罪”，令为人父母者听来不免后背发凉。",
     "Ở Trường Sa, Hồ Nam, một người đàn ông sắp bước vào tuổi ba mươi, thân thể lành lặn, sau khi bị từ chối cho “ăn bám”, lại còn định kiện bố mẹ ra tòa vì “tội” không nuôi mình, khiến những người làm cha làm mẹ nghe xong khó tránh khỏi lạnh sống lưng.",
     ["Đây là một ví dụ thật gây sốc. 即将步入而立之年 là sắp bước vào tuổi ba mươi. 身体健全 là thân thể khỏe mạnh, lành lặn, tức là hoàn toàn có thể đi làm.",
      "居然 là vậy mà, lại dám, biểu thị bất ngờ. 不养之罪 là tội không nuôi. 为人父母者 là người làm cha mẹ, chữ 为 đọc thanh hai. 令……听来不免后背发凉 là câu mẫu thứ ba: khiến ai nghe xong khó tránh khỏi lạnh sống lưng."]),
    ("这些已成年的“啃老族”多数不是缺乏谋生能力，而是不愿就业，不想独立，不敢走出家门，这种生活态度导致其衣食住行都要依赖年迈的父母，使父母难以承受，如此畸形的亲情关系不免令人叹息。",
     "Những người “ăn bám” đã trưởng thành này phần lớn không phải thiếu khả năng kiếm sống, mà là không muốn đi làm, không muốn tự lập, không dám bước ra khỏi nhà. Thái độ sống ấy khiến chuyện ăn mặc ở đi lại của họ đều phải dựa vào cha mẹ già, làm cha mẹ không sao gánh nổi. Mối quan hệ tình thân méo mó như vậy khó tránh khiến người ta thở dài.",
     ["Mẫu 不是……而是……: không phải… mà là…. Ba cụm 不愿就业，不想独立，不敢走出家门 tăng dần: không muốn, không nghĩ đến, không dám.",
      "导致 là dẫn đến. 其 là của họ, văn viết. 衣食住行 là ăn mặc ở đi lại, tức mọi nhu cầu sinh hoạt. 年迈 là tuổi già. 畸形的亲情关系 là quan hệ tình thân méo mó. 不免令人叹息 là khó tránh khiến người ta thở dài."]),
    ("首先，不可否认，在竞争日益激烈的今天，面对生活的压力，许多刚刚步入社会，处于人生和事业起跑线的年轻人的确需要得到父母的扶持和帮助，一些“啃老”的年轻人确实有几分难以自立的无奈，",
     "Trước hết, không thể phủ nhận rằng, trong thời buổi cạnh tranh ngày càng gay gắt hôm nay, đối mặt với áp lực cuộc sống, nhiều người trẻ vừa bước vào xã hội, đang đứng ở vạch xuất phát của cuộc đời và sự nghiệp quả thực cần được cha mẹ nâng đỡ và giúp đỡ; một số người trẻ “ăn bám” quả thật có phần bất lực vì khó mà tự lập,",
     ["首先 mở đầu phần phân tích. 不可否认 là không thể phủ nhận, tác giả thừa nhận một mặt khách quan trước. 日益激烈 là ngày càng gay gắt.",
      "处于人生和事业起跑线 là đang ở vạch xuất phát của cuộc đời và sự nghiệp, chữ 处 đọc thanh ba. 的确 và 确实 đều là quả thực. 有几分难以自立的无奈 là có phần bất lực vì khó tự lập: 几分 là đôi phần, một chút."]),
    ("而对于那些“理所当然”的“啃老族”而言，则完全忘记了“敬老孝老”的责任，认为父母的付出“天经地义”，毫无感恩，心安理得地靠老一辈养活而没有任何负疚感，成为中国家庭的一大困扰。",
     "còn đối với những người “ăn bám” coi đó là “lẽ đương nhiên”, thì họ hoàn toàn quên mất trách nhiệm “kính già, hiếu với cha mẹ”, cho rằng sự hy sinh của cha mẹ là “lẽ trời đất”, chẳng hề biết ơn, thản nhiên sống nhờ thế hệ trước mà không chút áy náy, trở thành một nỗi phiền muộn lớn của các gia đình Trung Quốc.",
     ["Mẫu 对于……而言 là đối với… mà nói; 则 là thì, biểu thị đối lập với nhóm người trẻ bất đắc dĩ ở câu trước. 理所当然 là lẽ đương nhiên.",
      "天经地义 là đạo lý hiển nhiên như trời đất. 毫无感恩 là không hề biết ơn. 心安理得 là thản nhiên, lòng yên ổn như thể mình có lý. 负疚感 là cảm giác áy náy. Ba thành ngữ trong một câu, rất đáng học thuộc."]),
    ("社会学者分析说，“我们的社会处在一个急剧转型的变动中，年轻一代中的部分人如果没能很好地跟上这个社会的变化，会处于相对被动的地位，就需要从父辈那里索取资源来保障自己的生存。”",
     "Một học giả xã hội học phân tích: “Xã hội chúng ta đang ở trong một quá trình chuyển đổi nhanh và mạnh. Một bộ phận người trẻ nếu không theo kịp sự thay đổi của xã hội, sẽ rơi vào vị thế tương đối bị động, và cần đòi hỏi nguồn lực từ thế hệ cha mẹ để bảo đảm sự sinh tồn của mình.”",
     ["Tác giả dẫn lời chuyên gia để tăng sức thuyết phục. 处在……中 là đang ở trong. 急剧转型 là chuyển đổi nhanh chóng, mạnh mẽ.",
      "跟上 là theo kịp. 处于被动的地位 là ở thế bị động. 从父辈那里索取资源 là đòi hỏi nguồn lực từ cha mẹ; 父辈 là thế hệ cha mẹ, đối lập với 子辈, thế hệ con cái."]),
    ("的确，在就业和创业的初期，应届毕业生难免会有“毕业季之痛”。就业难，工资偏低，房价、生活成本偏高，都构成了对年轻人的挑战。",
     "Quả thực, ở giai đoạn đầu tìm việc và khởi nghiệp, sinh viên vừa tốt nghiệp khó tránh khỏi “nỗi đau mùa tốt nghiệp”. Khó tìm việc, lương thấp, giá nhà và chi phí sinh hoạt cao, tất cả đều là thách thức đối với người trẻ.",
     ["应届毕业生 là sinh viên tốt nghiệp khóa năm nay. 难免 là khó tránh khỏi. 毕业季之痛 là nỗi đau mùa tốt nghiệp, chữ 之 tương đương 的, văn viết.",
      "偏低 và 偏高 dùng động từ 偏: lệch thấp, lệch cao so với mức hợp lý. 构成挑战 là tạo thành thách thức. Tác giả tiếp tục thừa nhận những khó khăn khách quan của người trẻ."]),
    ("但这些，都不该是他们可以心安理得“啃老”的借口。对于成年子女在生活压力下确需父母的扶持，也要尊重父母的意愿，考虑父母的经济能力，帮你是情分而不是本分。",
     "Nhưng tất cả những điều đó đều không nên là cái cớ để họ thản nhiên “ăn bám”. Với những người con trưởng thành thật sự cần cha mẹ nâng đỡ dưới áp lực cuộc sống, cũng phải tôn trọng ý nguyện của cha mẹ, cân nhắc khả năng kinh tế của cha mẹ: giúp con là tình nghĩa chứ không phải bổn phận.",
     ["Chữ 但 chuyển ý: khó khăn có thật, nhưng không phải lý do. 借口 là cái cớ. 确需 là thật sự cần, văn viết của 确实需要.",
      "意愿 là ý nguyện, mong muốn. Câu then chốt: 帮你是情分而不是本分. 情分 và 本分 đều đọc fèn ở chữ thứ hai. Cha mẹ giúp con là vì thương, chứ không phải nghĩa vụ bắt buộc."]),
    ("再者，“啃老”现象频繁发生，父母也要反思，是不是教育出了问题？有专家分析说，“啃老族”之所以出现，主要是因为父母过度地溺爱孩子。",
     "Hơn nữa, hiện tượng “ăn bám” xảy ra thường xuyên, cha mẹ cũng phải tự nhìn lại: phải chăng việc giáo dục đã có vấn đề? Có chuyên gia phân tích rằng, “tộc ăn bám” sở dĩ xuất hiện, chủ yếu là vì cha mẹ nuông chiều con cái quá mức.",
     ["再者 là hơn nữa, chuyển sang lập luận tiếp theo: trách nhiệm của cha mẹ. 频繁发生 là xảy ra thường xuyên, một nhóm kết hợp từ. 教育出了问题 là giáo dục có vấn đề.",
      "之所以……是因为…… là câu mẫu thứ tư: sở dĩ… là vì…. Mẫu này nêu kết quả trước, nguyên nhân sau, để nhấn mạnh nguyên nhân. 过度地溺爱 là nuông chiều quá mức."]),
    ("“‘啃老’与传统的家庭文化有关，家族制的传统体系意味着父辈对子辈的抚养责任和子辈对父辈的赡养义务，但在社会发展中，父辈拥有的资源往往比子辈更多，所以子辈在成长过程中有向父辈索取资源的可能性，这是形成‘啃老’现象的一个内在原因。”",
     "“‘Ăn bám’ có liên quan đến văn hóa gia đình truyền thống. Hệ thống truyền thống của chế độ gia tộc có nghĩa là thế hệ cha mẹ có trách nhiệm nuôi dạy con cái, còn con cái có nghĩa vụ phụng dưỡng cha mẹ. Nhưng trong quá trình xã hội phát triển, nguồn lực cha mẹ nắm giữ thường nhiều hơn con cái, vì thế con cái trong quá trình trưởng thành có khả năng đòi hỏi nguồn lực từ cha mẹ. Đây là một nguyên nhân nội tại hình thành hiện tượng ‘ăn bám’.”",
     ["Đoạn này tiếp tục lời chuyên gia, nên có ngoặc kép lồng nhau. 与……有关 là có liên quan đến. 家族制 là chế độ gia tộc. 意味着 là có nghĩa là.",
      "Hãy chú ý cặp đối xứng: 父辈对子辈的抚养责任, trách nhiệm nuôi con của cha mẹ; 子辈对父辈的赡养义务, nghĩa vụ phụng dưỡng cha mẹ của con. 拥有 là sở hữu. 内在原因 là nguyên nhân nội tại, bên trong."]),
    ("对此，中国多个省市发布了《老年人权益保障条例》，规定禁止有独立生活能力的成年子女“啃老”。对于这种条例，有人叫好，也有人认为这只是一厢情愿，并不能根除“啃老”现象。",
     "Trước tình hình đó, nhiều tỉnh thành ở Trung Quốc đã ban hành “Điều lệ bảo đảm quyền lợi người cao tuổi”, quy định cấm con cái trưởng thành có khả năng sống tự lập “ăn bám” cha mẹ. Đối với điều lệ này, có người hoan nghênh, cũng có người cho rằng đó chỉ là mong muốn một phía, không thể xóa bỏ tận gốc hiện tượng “ăn bám”.",
     ["对此 là đối với việc này. 条例 là điều lệ, một loại văn bản pháp quy. 规定禁止 là quy định cấm.",
      "叫好 là reo hò khen hay, hoan nghênh. 一厢情愿 là mong muốn chủ quan của một phía, không xét thực tế. 根除 là trừ tận gốc. Tác giả trình bày khách quan cả hai luồng ý kiến."]),
    ("随着现在的年轻一代在买车、买房、养孩子等方面的经济压力不断增大，越来越多的年轻人不得不加入了“啃老”的行列，而老一辈的养老资源又并不充足，在这种情况下，通过立法的形式可以有限度地控制“啃老”现象的蔓延，以保障老年人的基本权益。",
     "Cùng với việc áp lực kinh tế của thế hệ trẻ ngày nay về mua xe, mua nhà, nuôi con… không ngừng tăng lên, ngày càng nhiều người trẻ buộc phải gia nhập hàng ngũ “ăn bám”, trong khi nguồn lực dưỡng già của thế hệ trước lại chẳng dồi dào. Trong tình hình đó, thông qua hình thức lập pháp có thể khống chế ở mức độ nhất định sự lan rộng của hiện tượng “ăn bám”, nhằm bảo đảm quyền lợi cơ bản của người cao tuổi.",
     ["随着 là cùng với, theo đà. 加入行列 là gia nhập hàng ngũ, chữ 行 đọc là háng. 养老资源 là nguồn lực dưỡng già. 并不充足 là chẳng hề dồi dào.",
      "有限度地 là ở mức độ có hạn: luật không giải quyết được hết, nhưng hạn chế được phần nào. 蔓延 là lan rộng. Vế cuối 以保障老年人的基本权益 là câu mẫu mục đích với 以: nhằm bảo đảm quyền lợi cơ bản của người già."]),
    ("不过，正所谓“清官难断家务事”，一方面部分老人的牺牲欲、奉献欲太强，自愿慷慨解囊，这在客观上形成了一种变相的纵容；",
     "Tuy nhiên, đúng như câu “quan thanh liêm cũng khó xử chuyện nhà”, một mặt, ham muốn hy sinh, cống hiến của một bộ phận người già quá mạnh, họ tự nguyện hào phóng móc hầu bao, điều này về khách quan đã tạo thành một sự dung túng trá hình;",
     ["正所谓 là đúng như người ta nói. Câu 清官难断家务事 chúng ta đã học ở bài trước. 一方面……另一方面…… là một mặt… mặt khác….",
      "牺牲欲、奉献欲 là ham muốn hy sinh, cống hiến; chữ 欲 là ham muốn. 慷慨解囊 là hào phóng mở túi tiền. 在客观上 là xét về mặt khách quan. 变相的纵容 là sự dung túng trá hình: cha mẹ tự nguyện cho tiền, vô tình nuôi dưỡng thói ăn bám."]),
    ("另一方面作为“啃老方”，部分年轻人内心也隐藏着被父母强大控制欲所操纵的无奈与痛苦，对他们而言，经济难以独立，内心焦灼不安，无异于陷入另一种“水深火热”之中。",
     "mặt khác, ở phía “người ăn bám”, một bộ phận người trẻ trong lòng cũng giấu nỗi bất lực và đau khổ vì bị ham muốn kiểm soát mạnh mẽ của cha mẹ thao túng. Đối với họ, kinh tế khó độc lập, trong lòng bồn chồn bất an, chẳng khác nào rơi vào một kiểu “nước sôi lửa bỏng” khác.",
     ["啃老方 là phía ăn bám. Mẫu bị động văn viết 被……所……: 被父母强大控制欲所操纵, bị ham muốn kiểm soát của cha mẹ thao túng. Tác giả nhìn vấn đề từ cả hai phía, rất công bằng.",
      "焦灼不安 là bồn chồn bất an. 无异于 là chẳng khác nào. 水深火热 là nước sâu lửa nóng, chỉ cảnh khốn khổ cùng cực; tiếng Việt nói nước sôi lửa bỏng. Người ăn bám cũng không hề sung sướng."]),
    ("理想的家庭关系是两代人过着既彼此信赖又各自独立的生活。父母要培养孩子的社会适应能力和健全的人格，年轻人步入社会也要尽快学会自食其力，",
     "Quan hệ gia đình lý tưởng là hai thế hệ sống một cuộc sống vừa tin cậy lẫn nhau, vừa độc lập riêng. Cha mẹ phải bồi dưỡng cho con khả năng thích ứng với xã hội và nhân cách lành mạnh; người trẻ bước vào xã hội cũng phải nhanh chóng học cách tự nuôi sống bản thân;",
     ["Đoạn kết đưa ra giải pháp. 既……又…… là vừa… vừa…. 彼此信赖 là tin cậy lẫn nhau, 各自独立 là mỗi người độc lập.",
      "社会适应能力 là khả năng thích ứng xã hội. 健全的人格 là nhân cách lành mạnh. 自食其力 là tự mình làm ra mà ăn, tự lực cánh sinh. Giải pháp nêu lần lượt trách nhiệm của cha mẹ, rồi của người trẻ."]),
    ("另一方面，全社会也应当营造鼓励年轻人自立自强的社会氛围，这样才能给“巨婴”断奶，让“啃老”绝迹。",
     "mặt khác, toàn xã hội cũng nên tạo dựng bầu không khí khuyến khích người trẻ tự lập, tự cường. Có như vậy mới có thể “cai sữa” cho những “em bé khổng lồ”, khiến hiện tượng “ăn bám” biến mất hoàn toàn.",
     ["Cuối cùng là trách nhiệm của xã hội. 营造氛围 là tạo dựng bầu không khí, một nhóm kết hợp từ. 自立自强 là tự lập tự cường, theo cấu trúc 自A自B, câu mẫu thứ bảy.",
      "这样才能 là như vậy mới có thể. Câu kết dùng lại hình ảnh 断奶 ở đầu bài và khái niệm 巨婴, tạo sự hô ứng đầu cuối. 绝迹 là biến mất hoàn toàn."]),
]

add("bullets", section="Bài khóa 课文", title="Phần 2: Bài khóa “养儿防老”变“养子啃老”？", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Bài khóa được cải biên từ một bài viết trên 人民日报海外版 ngày mười chín tháng chín năm hai nghìn không trăm mười bốn, với nhan đề: 养儿防老变养子啃老？谁为啃老族断奶？ Ai sẽ cai sữa cho tộc ăn bám?",
         F(0, "Thầy chia bài thành mười sáu đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "").replace("‘", "").replace("’", "")
    zsize = 54 if len(zh) <= 70 else 50 if len(zh) <= 90 else 46
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", "").replace("‘", "").replace("’", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Ý chính bài khóa", section="Bài khóa 课文", title="Mạch lập luận của bài", size=34,
    items=["## 1. Hiện tượng: 养儿防老 → 养子啃老",
           "Nhà giàu, nhà nghèo, cả vợ chồng trẻ đều “啃老” · chàng trai gần 30 tuổi kiện bố mẹ",
           "## 2. Nguyên nhân",
           "Người trẻ: áp lực việc làm, nhà cửa (khách quan) · thói 理所当然, 心安理得 (chủ quan)",
           "Cha mẹ: 溺爱 · văn hóa gia tộc · 慷慨解囊 thành 变相的纵容",
           "## 3. Pháp luật: 《老年人权益保障条例》 – người khen, người cho là 一厢情愿",
           "## 4. Giải pháp: 彼此信赖，各自独立",
           "Cha mẹ: dạy con thích ứng · người trẻ: 自食其力 · xã hội: 营造自立自强的氛围"],
    say=["Đọc xong bài khóa, chúng ta cùng tóm tắt mạch lập luận.",
         F(0, "Phần một là hiện tượng: câu tục ngữ 养儿防老 đã biến thành 养子啃老."),
         F(1, "Không chỉ nhà khá giả, ngay cả nhà không giàu, thậm chí vợ chồng trẻ có con cũng ăn bám bố mẹ. Ví dụ điển hình là chàng trai gần ba mươi tuổi ở Trường Sa kiện bố mẹ vì không chịu nuôi mình."),
         F(2, "Phần hai là nguyên nhân, được phân tích từ hai phía."),
         F(3, "Phía người trẻ: một mặt có khó khăn khách quan như khó tìm việc, lương thấp, giá nhà cao; mặt khác có những người coi việc ăn bám là 理所当然, thản nhiên 心安理得."),
         F(4, "Phía cha mẹ: nuông chiều quá mức; văn hóa gia tộc truyền thống; và nhiều cha mẹ tự nguyện 慷慨解囊, vô tình thành 变相的纵容."),
         F(5, "Phần ba là pháp luật: nhiều tỉnh thành ban hành điều lệ cấm con cái có khả năng tự lập ăn bám bố mẹ. Có người hoan nghênh, có người cho rằng đó chỉ là 一厢情愿."),
         F(6, "Phần bốn là giải pháp: quan hệ lý tưởng là hai thế hệ vừa tin cậy lẫn nhau, vừa độc lập riêng."),
         F(7, "Cha mẹ phải dạy con khả năng thích ứng xã hội; người trẻ phải học cách 自食其力; còn xã hội phải 营造 bầu không khí khuyến khích tự lập tự cường.")])

# ======================= CÂU MẪU =======================
add("bullets", chapter="Câu mẫu: 频频 · 不仅……连……甚至", section="Câu mẫu 重点句型", title="1. 频频 pínpín – liên tiếp, nhiều lần liền", size=36,
    items=["Phó từ, đứng trước động từ: động tác/tình huống lặp lại nhiều lần trong một khoảng thời gian, phạm vi nhất định",
           "Tương đương “屡次”、“连续多次”",
           "现代社会频频出现“养子啃老”的社会现象。",
           "他频频与朋友们以及他的竞争者们打招呼。",
           "气氛十分热烈，大家频频举杯，欢声笑语不断。",
           "Lưu ý: 频频 là phó từ (频频举杯); còn 频繁 là tính từ (交往频繁 · 频繁发生)"],
    say=["Bây giờ chúng ta sang phần câu mẫu và từ ngữ trọng điểm. Điểm thứ nhất là phó từ 频频.",
         F(0, "频频 là phó từ, đứng trước động từ, biểu thị một động tác hay tình huống lặp lại nhiều lần trong một khoảng thời gian hay phạm vi nhất định. Tiếng Việt dịch là liên tục, liên tiếp."),
         F(1, "Nó tương đương với 屡次 hoặc 连续多次, nhiều lần liên tiếp."),
         F(2, "Ví dụ một, từ bài khóa: 现代社会频频出现养子啃老的社会现象。 Xã hội hiện đại liên tục xuất hiện hiện tượng nuôi con để con ăn bám."),
         F(3, "Ví dụ hai: 他频频与朋友们以及他的竞争者们打招呼。 Anh ấy liên tục chào hỏi bạn bè và cả các đối thủ cạnh tranh."),
         F(4, "Ví dụ ba: 气氛十分热烈，大家频频举杯，欢声笑语不断。 Không khí vô cùng sôi nổi, mọi người liên tục nâng ly, tiếng cười nói không ngớt."),
         F(5, "Lưu ý quan trọng: 频频 là phó từ, chỉ đứng trước động từ, như 频频举杯. Còn 频繁 là tính từ, có thể làm vị ngữ hay trạng ngữ: 交往频繁, 频繁发生. Không nói 交往频频. Bài tập hai sẽ kiểm tra điểm này.")])

add("bullets", section="Câu mẫu 重点句型", title="2. 不仅……，连……，甚至…… – không chỉ…, ngay cả…, thậm chí…", size=32,
    items=["Câu phức tăng tiến ba bậc: mức độ tăng dần, vế sau càng bất ngờ hơn vế trước",
           "不仅殷实的家庭有“啃老”的孩子，连并不富裕的家庭也常出现不肯“断奶”的孩子，甚至小两口带着孩子一起“啃老”的现象也并非个例。",
           "新冠疫情爆发以后，全国人民众志成城，不仅医生护士挺身而出，奔赴抗疫前线，连外卖小哥、出租车司机都不遗余力地帮助人们，甚至是海外华人华侨也纷纷捐款，共同筑起一道防疫之墙。",
           "有些改革不仅让老师身心俱疲，连家长也疲软无力，甚至孩子都陷入焦虑抑郁的状态无法自拔。",
           "Chú ý: vế 连 thường đi với 也 / 都"],
    say=["Điểm thứ hai là câu tăng tiến ba bậc: 不仅……连……甚至…….",
         F(0, "Đây là câu phức tăng tiến. 不仅 nêu điều thứ nhất, 连 nêu điều bất ngờ hơn, 甚至 nêu điều bất ngờ nhất. Mức độ tăng dần qua từng vế. Tiếng Việt: không chỉ…, ngay cả…, thậm chí…."),
         F(1, "Ví dụ một, từ bài khóa: 不仅殷实的家庭有啃老的孩子，连并不富裕的家庭也常出现不肯断奶的孩子，甚至小两口带着孩子一起啃老的现象也并非个例。 Nhà giàu có con ăn bám thì còn dễ hiểu; nhà không giàu cũng có, đã bất ngờ hơn; vợ chồng trẻ dắt cả con đi ăn bám, càng bất ngờ hơn nữa."),
         F(2, "Ví dụ hai: 新冠疫情爆发以后，全国人民众志成城，不仅医生护士挺身而出，奔赴抗疫前线，连外卖小哥、出租车司机都不遗余力地帮助人们，甚至是海外华人华侨也纷纷捐款，共同筑起一道防疫之墙。 Sau khi dịch Covid bùng phát, nhân dân cả nước đồng lòng: không chỉ bác sĩ, y tá xông pha ra tuyến đầu chống dịch, ngay cả các anh giao đồ ăn, tài xế taxi cũng dốc hết sức giúp đỡ mọi người, thậm chí kiều bào ở nước ngoài cũng lần lượt quyên góp, cùng dựng nên bức tường phòng dịch. 众志成城 là muôn người một lòng, 不遗余力 là dốc toàn lực."),
         F(3, "Ví dụ ba: 有些改革不仅让老师身心俱疲，连家长也疲软无力，甚至孩子都陷入焦虑抑郁的状态无法自拔。 Có những cải cách không chỉ khiến giáo viên kiệt quệ cả thể xác lẫn tinh thần, ngay cả phụ huynh cũng rã rời, thậm chí học sinh cũng rơi vào trạng thái lo âu trầm cảm không thoát ra được."),
         F(4, "Chú ý: vế có 连 thường đi kèm 也 hoặc 都, như 连并不富裕的家庭也, 连外卖小哥都.")])

add("bullets", chapter="Câu mẫu: 不免 · 之所以 · 以", section="Câu mẫu 重点句型", title="3. 令……听来不免…… / 不免令人…… – khó tránh khiến người ta…", size=34,
    items=["不免: khó tránh khỏi (kết quả tự nhiên, không mong muốn); sau 令人 thường là động từ/tính từ tâm lý",
           "令为人父母者听来不免后背发凉。",
           "他小小年纪就聪明懂事，却不得不辍学打工，担起支撑整个家庭的重任，令人听来不免叹息感伤。",
           "想到新冠病毒短时间内迅速蔓延，波及全世界，不免令人心生畏惧。",
           "Hay gặp: 不免令人担忧 · 不免令人失望 · 不免令人感慨 · 不免令人叹息"],
    say=["Điểm thứ ba là cấu trúc 令……听来不免…… hoặc 不免令人…….",
         F(0, "不免 nghĩa là khó tránh khỏi, chỉ một kết quả tự nhiên mà người ta không mong muốn. 令 là khiến. Sau 令人 thường là động từ hay tính từ chỉ tâm lý, cảm xúc như 担忧, 叹息, 畏惧."),
         F(1, "Ví dụ một, từ bài khóa: 令为人父母者听来不免后背发凉。 Khiến những người làm cha mẹ nghe xong khó tránh khỏi lạnh sống lưng."),
         F(2, "Ví dụ hai: 他小小年纪就聪明懂事，却不得不辍学打工，担起支撑整个家庭的重任，令人听来不免叹息感伤。 Tuổi còn nhỏ mà đã thông minh hiểu chuyện, nhưng phải bỏ học đi làm, gánh vác trọng trách nuôi cả gia đình, khiến người nghe không khỏi thở dài thương cảm. 辍学 là bỏ học giữa chừng."),
         F(3, "Ví dụ ba: 想到新冠病毒短时间内迅速蔓延，波及全世界，不免令人心生畏惧。 Nghĩ đến việc virus Corona lan nhanh trong thời gian ngắn, ảnh hưởng tới toàn thế giới, khó tránh khiến người ta sinh lòng sợ hãi. Ở đây lại gặp từ mới 蔓延."),
         F(4, "Những cụm hay gặp: 不免令人担忧, không khỏi khiến người ta lo lắng; 不免令人失望; 不免令人感慨; 不免令人叹息. Bài khóa có câu: 如此畸形的亲情关系不免令人叹息。")])

add("bullets", section="Câu mẫu 重点句型", title="4. 之所以……，是因为…… · 5. ……，以……", size=32,
    items=["## 之所以 + kết quả，是因为/由于 + nguyên nhân (sở dĩ… là vì…): nêu kết quả trước để nhấn mạnh nguyên nhân",
           "“啃老族”之所以出现，主要是因为父母过度地溺爱孩子。",
           "这部电影之所以好看，是因为内容很有趣。",
           "妈妈之所以生气了，是由于他不肯承认自己的错误。",
           "## ……，以 + mục đích (để, nhằm): câu phức mục đích, văn viết",
           "通过立法的形式可以有限度地控制“啃老”现象的蔓延，以保障老年人的基本权益。",
           "政府用他们的名字命名这条街，以纪念在战争中牺牲的战士。",
           "老师采用新的教学方法上课，以调动学生的积极性。"],
    say=[F(0, "Điểm thứ tư là câu nhân quả 之所以……是因为……. Vế trước có 之所以 nêu kết quả, vế sau có 是因为 hoặc 是由于 nêu nguyên nhân. Tiếng Việt: sở dĩ… là vì…. Khác với 因为……所以……, mẫu này đưa kết quả lên trước để nhấn mạnh nguyên nhân."),
         F(1, "Ví dụ một, từ bài khóa: 啃老族之所以出现，主要是因为父母过度地溺爱孩子。 Tộc ăn bám sở dĩ xuất hiện, chủ yếu là vì cha mẹ quá nuông chiều con cái."),
         F(2, "Ví dụ hai: 这部电影之所以好看，是因为内容很有趣。 Bộ phim này sở dĩ hay là vì nội dung rất thú vị."),
         F(3, "Ví dụ ba: 妈妈之所以生气了，是由于他不肯承认自己的错误。 Mẹ sở dĩ giận là vì cậu ấy không chịu nhận lỗi."),
         F(4, "Điểm thứ năm là câu mục đích với liên từ 以. Vế trước nêu cách làm, vế sau bắt đầu bằng 以, nêu mục đích. Tiếng Việt: để, nhằm. Đây là cách nói văn viết, gặp nhiều trong văn bản chính thức."),
         F(5, "Ví dụ một, từ bài khóa: 通过立法的形式可以有限度地控制啃老现象的蔓延，以保障老年人的基本权益。 Thông qua lập pháp có thể hạn chế sự lan rộng của hiện tượng ăn bám, nhằm bảo đảm quyền lợi cơ bản của người già."),
         F(6, "Ví dụ hai: 政府用他们的名字命名这条街，以纪念在战争中牺牲的战士。 Chính phủ lấy tên họ đặt cho con phố này, để tưởng nhớ những chiến sĩ đã hy sinh trong chiến tranh."),
         F(7, "Ví dụ ba: 老师采用新的教学方法上课，以调动学生的积极性。 Thầy giáo áp dụng phương pháp dạy học mới, nhằm phát huy tính tích cực của học sinh. 调动积极性 là khơi dậy tính tích cực.")])

add("bullets", chapter="Câu mẫu: 所谓 · 自A自B", section="Câu mẫu 重点句型", title="6. 所谓 suǒwèi · 7. 自A自B", size=32,
    items=["## 所谓: “cái được gọi là”, thường dùng để giải thích một khái niệm, hoặc dẫn một câu nói quen thuộc (正所谓……)",
           "正所谓“清官难断家务事”，一方面部分老人的牺牲欲、奉献欲太强，自愿慷慨解囊……",
           "所谓共识，就是指共同的认识。",
           "所谓“道不同不相为谋”，反正我和你也不是一路的人。",
           "## 自A自B: cấu trúc cố định – tự mình làm, tự mình chịu (自由自在 · 自娱自乐 · 自私自利 · 自卖自夸)",
           "全社会应该营造鼓励年轻人自立自强的社会氛围。",
           "一路上老板自说自话唠叨了半天。",
           "业余时间约上三五好友唱唱歌，自娱自乐。"],
    say=[F(0, "Điểm thứ sáu là 所谓, nghĩa là cái được gọi là. Nó thường dùng để giải thích một khái niệm, theo mẫu 所谓A，就是B; hoặc trong cụm 正所谓 để dẫn một câu nói quen thuộc, nghĩa là đúng như người ta nói."),
         F(1, "Ví dụ một, từ bài khóa: 正所谓清官难断家务事，一方面部分老人的牺牲欲、奉献欲太强，自愿慷慨解囊。 Đúng như câu quan thanh liêm cũng khó xử chuyện nhà."),
         F(2, "Ví dụ hai: 所谓共识，就是指共同的认识。 Cái gọi là đồng thuận, chính là chỉ nhận thức chung."),
         F(3, "Ví dụ ba: 所谓道不同不相为谋，反正我和你也不是一路的人。 Đúng như câu khác đường thì không cùng mưu tính, đằng nào tôi với anh cũng chẳng phải người cùng đường. 道不同不相为谋 là câu của Khổng Tử, chữ 为 đọc thanh hai."),
         F(4, "Điểm thứ bảy là cấu trúc cố định 自A自B, trong đó A và B là hai chữ gần nghĩa, nhấn mạnh việc tự mình làm, tự mình hưởng hay tự mình chịu. Hay gặp: 自由自在, tự do tự tại; 自娱自乐, tự mua vui cho mình; 自私自利, ích kỷ vụ lợi; 自卖自夸, mèo khen mèo dài đuôi."),
         F(5, "Ví dụ một, từ bài khóa: 全社会应该营造鼓励年轻人自立自强的社会氛围。 Toàn xã hội nên tạo dựng bầu không khí khuyến khích người trẻ tự lập tự cường."),
         F(6, "Ví dụ hai: 一路上老板自说自话唠叨了半天。 Suốt dọc đường ông chủ cứ tự nói tự nghe, lải nhải mãi. 自说自话 là nói một mình, chẳng cần ai nghe."),
         F(7, "Ví dụ ba: 业余时间约上三五好友唱唱歌，自娱自乐。 Lúc rảnh rỗi hẹn dăm ba người bạn đi hát, tự mua vui cho nhau.")])

add("bullets", section="Câu mẫu 重点句型", title="Luyện tập: hoàn thành câu bằng câu mẫu", reveal=True, size=34,
    items=["(1) 他最近上班___迟到，老板很不满意。（频频 / 频繁？）",
           "Đáp án: 频频 – đứng ngay trước động từ 迟到. (Cũng có thể: 他最近上班迟到很频繁。)",
           "(2) 这道题太难了，不仅我不会做，___，___。（连……甚至……）",
           "Đáp án gợi ý: 连我们班成绩最好的同学也不会做，甚至老师都想了半天。",
           "(3) 我___选择这家公司，___这里的工作环境很好。（之所以……是因为……）",
           "Đáp án: 我之所以选择这家公司，是因为这里的工作环境很好。",
           "(4) 我们每天坚持说汉语，___。（以）",
           "Đáp án gợi ý: 我们每天坚持说汉语，以提高自己的口语水平。"],
    say=["Bây giờ chúng ta luyện tập một chút: hoàn thành câu bằng các câu mẫu vừa học.",
         F(0, "Câu một: 他最近上班什么迟到，老板很不满意。 Dạo này anh ấy đi làm liên tục đến muộn, sếp rất không hài lòng. Nên dùng 频频 hay 频繁? Các bạn tạm dừng và suy nghĩ nhé."),
         F(1, "Đáp án: 频频, vì chỗ trống đứng ngay trước động từ 迟到: 他最近上班频频迟到。 Nếu muốn dùng 频繁, ta phải đổi câu, để nó làm vị ngữ: 他最近上班迟到很频繁。"),
         F(2, "Câu hai: 这道题太难了，不仅我不会做，连……甚至……. Bài này khó quá, không chỉ tôi không làm được, ngay cả…, thậm chí…."),
         F(3, "Đáp án gợi ý: 连我们班成绩最好的同学也不会做，甚至老师都想了半天。 Ngay cả bạn học giỏi nhất lớp cũng không làm được, thậm chí thầy giáo cũng phải nghĩ mãi. Mức độ tăng dần: tôi, bạn giỏi nhất, thầy giáo."),
         F(4, "Câu ba: 我选择这家公司，这里的工作环境很好。 Hãy nối bằng 之所以……是因为…….."),
         F(5, "Đáp án: 我之所以选择这家公司，是因为这里的工作环境很好。 Tôi sở dĩ chọn công ty này là vì môi trường làm việc ở đây rất tốt."),
         F(6, "Câu bốn: 我们每天坚持说汉语，rồi dùng 以 nêu mục đích."),
         F(7, "Đáp án gợi ý: 我们每天坚持说汉语，以提高自己的口语水平。 Chúng tôi kiên trì nói tiếng Trung mỗi ngày, để nâng cao trình độ khẩu ngữ của mình.")])

# ======================= KẾT HỢP TỪ =======================
add("bullets", chapter="Kết hợp từ", section="Kết hợp từ 词语搭配", title="Kết hợp từ (1): 步入 · 索取 · 频繁", size=31,
    items=["## 步入: 步入社会 · 步入……阶段 · 步入而立之年 · 步入辉煌 · 步入快车道",
           "今年你就要步入社会了，参加工作一定要好好表现，不要给别人添麻烦。",
           "在小学老师春风化雨般的辛勤培养下，我们顺利地步入了中学阶段。",
           "## 索取: 索取资源 · 索取财物 · 索取赔偿 · 索取报酬",
           "消费者受到欺诈，可以通过法律途径索取赔偿。",
           "他积极参与环保志愿者的公益活动，从不索取报酬。",
           "## 频繁: 频繁发生 · 频繁活动 · 交往频繁 · 变化频繁",
           "两国人民关系友好，交往频繁。",
           "他在工作时间频繁接听手机，惹得老板发脾气。"],
    say=["Tiếp theo là phần kết hợp từ. Bài này có sáu nhóm.",
         F(0, "Nhóm một: 步入, bước vào. 步入社会, bước vào đời; 步入中学阶段, bước vào bậc trung học; 步入而立之年, bước vào tuổi ba mươi; 步入辉煌, bước vào thời kỳ huy hoàng; 步入快车道, bước vào làn đường cao tốc, tức là phát triển nhanh."),
         F(1, "Ví dụ: 今年你就要步入社会了，参加工作一定要好好表现，不要给别人添麻烦。 Năm nay con sắp bước vào đời rồi, đi làm nhất định phải thể hiện cho tốt, đừng gây phiền phức cho người khác."),
         F(2, "Ví dụ: 在小学老师春风化雨般的辛勤培养下，我们顺利地步入了中学阶段。 Dưới sự vun đắp tận tình như gió xuân mưa móc của thầy cô tiểu học, chúng tôi đã thuận lợi bước vào bậc trung học. 春风化雨 là gió xuân mưa thuận, ví với sự giáo dục ân cần."),
         F(3, "Nhóm hai: 索取, đòi. 索取资源, đòi nguồn lực; 索取财物, đòi tiền của; 索取赔偿, đòi bồi thường; 索取报酬, đòi thù lao."),
         F(4, "Ví dụ: 消费者受到欺诈，可以通过法律途径索取赔偿。 Người tiêu dùng bị lừa đảo có thể đòi bồi thường qua con đường pháp luật."),
         F(5, "Ví dụ: 他积极参与环保志愿者的公益活动，从不索取报酬。 Anh ấy tích cực tham gia hoạt động công ích của tình nguyện viên bảo vệ môi trường, chưa bao giờ đòi thù lao."),
         F(6, "Nhóm ba: 频繁, thường xuyên, dày đặc. 频繁发生, xảy ra thường xuyên; 频繁活动, hoạt động dày đặc; 交往频繁, qua lại thường xuyên; 变化频繁, thay đổi liên tục. Như đã nói, 频繁 là tính từ, có thể đứng sau danh từ làm vị ngữ."),
         F(7, "Ví dụ: 两国人民关系友好，交往频繁。 Nhân dân hai nước quan hệ hữu hảo, qua lại thường xuyên."),
         F(8, "Ví dụ: 他在工作时间频繁接听手机，惹得老板发脾气。 Trong giờ làm việc anh ta liên tục nghe điện thoại, khiến sếp nổi cáu.")])

add("bullets", section="Kết hợp từ 词语搭配", title="Kết hợp từ (2): 蔓延 · 变相 · 营造", size=31,
    items=["## 蔓延: 疾病蔓延 · 火势蔓延 · 四处蔓延",
           "森林发生了大火，火势蔓延很快，必须马上控制住。",
           "要采取有力措施，防止传染病蔓延。",
           "## 变相: 变相剥削 · 变相贪污 · 变相加价",
           "捆绑销售，就是变相加价。",
           "现在，汽车市场上的变相加价提车已经成为一种潜规则。",
           "## 营造: 营造氛围 · 营造环境 · 营造秩序",
           "为了营造良好的学习环境，学校让工作人员将所有教室的墙壁重新粉刷了一遍。",
           "我特爱回老家过年，红灯笼、烟花、鞭炮，营造出浓浓的节日氛围。"],
    say=[F(0, "Nhóm bốn: 蔓延, lan tràn. 疾病蔓延, dịch bệnh lan tràn; 火势蔓延, ngọn lửa lan rộng; 四处蔓延, lan ra khắp nơi."),
         F(1, "Ví dụ: 森林发生了大火，火势蔓延很快，必须马上控制住。 Rừng xảy ra cháy lớn, lửa lan rất nhanh, phải lập tức khống chế."),
         F(2, "Ví dụ: 要采取有力措施，防止传染病蔓延。 Phải áp dụng biện pháp mạnh mẽ, ngăn chặn bệnh truyền nhiễm lây lan."),
         F(3, "Nhóm năm: 变相, trá hình. 变相剥削, bóc lột trá hình; 变相贪污, tham ô trá hình; 变相加价, tăng giá trá hình. Từ này luôn đi với việc xấu."),
         F(4, "Ví dụ: 捆绑销售，就是变相加价。 Bán kèm hàng chính là tăng giá trá hình. 捆绑销售 là bán gộp, bắt mua kèm."),
         F(5, "Ví dụ: 现在，汽车市场上的变相加价提车已经成为一种潜规则。 Hiện nay, việc tăng giá trá hình khi nhận xe trên thị trường ô tô đã thành một luật ngầm. 潜规则 là luật ngầm, quy tắc ngầm."),
         F(6, "Nhóm sáu: 营造, tạo dựng. 营造氛围, tạo bầu không khí; 营造环境, tạo môi trường; 营造秩序, tạo trật tự."),
         F(7, "Ví dụ: 为了营造良好的学习环境，学校让工作人员将所有教室的墙壁重新粉刷了一遍。 Để tạo môi trường học tập tốt, nhà trường cho nhân viên sơn lại tường tất cả các phòng học."),
         F(8, "Ví dụ: 我特爱回老家过年，红灯笼、烟花、鞭炮，营造出浓浓的节日氛围。 Tôi rất thích về quê ăn Tết, đèn lồng đỏ, pháo hoa, pháo nổ, tạo nên không khí ngày Tết thật đậm đà.")])

# ======================= THÀNH NGỮ =======================
add("bullets", chapter="Thành ngữ", section="Thành ngữ 成语和惯用语", title="Thành ngữ (1): 养儿防老 · 理所当然 · 天经地义", size=33,
    items=["## 养儿防老 yǎng'ér-fánglǎo – nuôi con phòng khi về già (≈ “Trẻ cậy cha, già cậy con”)",
           "当今生育观念的变化正冲击着养儿防老的旧传统观念。",
           "## 理所当然 lǐsuǒdāngrán – lẽ đương nhiên, theo lý phải như thế",
           "你永远都要记住感谢别人给你的一切，不要把任何事情当成理所当然。",
           "## 天经地义 tiānjīng-dìyì – đạo lý hiển nhiên như trời đất, không thể nghi ngờ",
           "为人子女者照顾年老的父母，这是天经地义的事。"],
    say=["Bây giờ chúng ta học tám thành ngữ của bài.",
         F(0, "Thứ nhất: 养儿防老. 养儿 là nuôi con, 防老 là phòng khi về già. Nghĩa là nuôi con để về già có chỗ nương tựa. Tiếng Việt có câu tương tự: trẻ cậy cha, già cậy con."),
         F(1, "Ví dụ: 当今生育观念的变化正冲击着养儿防老的旧传统观念。 Sự thay đổi quan niệm sinh đẻ ngày nay đang tác động mạnh đến quan niệm truyền thống cũ nuôi con phòng già. 冲击 là va đập, tác động mạnh."),
         F(2, "Thứ hai: 理所当然. 理 là lý lẽ, 当然 là lẽ ra phải thế. Theo lý mà nói thì đương nhiên phải như vậy. Trong bài: 理所当然的啃老族, những người coi việc ăn bám là đương nhiên. Sách ghi âm đầu là lí, nhưng chuẩn là lǐ, thanh ba."),
         F(3, "Ví dụ: 你永远都要记住感谢别人给你的一切，不要把任何事情当成理所当然。 Bạn phải luôn nhớ biết ơn tất cả những gì người khác cho mình, đừng coi bất cứ điều gì là lẽ đương nhiên."),
         F(4, "Thứ ba: 天经地义. 经 là đạo lý bất biến, 义 là lẽ phải. Đạo lý của trời, lẽ phải của đất, tức là chân lý hiển nhiên, không thể nghi ngờ. Mạnh hơn 理所当然."),
         F(5, "Ví dụ: 为人子女者照顾年老的父母，这是天经地义的事。 Làm con mà chăm sóc cha mẹ già, đó là lẽ trời đất. Các bạn thấy đấy: con nuôi cha mẹ là 天经地义; nhưng con trưởng thành mà cha mẹ phải nuôi, thì không phải 天经地义.")])

add("bullets", section="Thành ngữ 成语和惯用语", title="Thành ngữ (2): 心安理得 · 一厢情愿 · 慷慨解囊", size=33,
    items=["## 心安理得 xīn'ān-lǐdé – thấy mình có lý nên lòng thản nhiên, không áy náy",
           "我会清清白白做人，干干净净赚钱，这样才能心安理得，我父母也不会因我脸上无光。",
           "## 一厢情愿 yìxiāng-qíngyuàn – mong muốn đơn phương, chủ quan một phía",
           "爱情的投入和产出从来不成比例，一厢情愿的牺牲到头来感动的往往是自己！",
           "## 慷慨解囊 kāngkǎi-jiěnáng – hào phóng mở túi tiền giúp người",
           "面对遭受水灾的灾民，他慷慨解囊，一次就捐款十万元。"],
    say=[F(0, "Thứ tư: 心安理得. 心安 là lòng yên, 理得 là có lý. Tự thấy việc mình làm hợp lý nên trong lòng thản nhiên. Thành ngữ này vốn trung tính, nhưng trong bài lại mang ý chê: 心安理得地靠老一辈养活, thản nhiên sống nhờ cha mẹ mà chẳng áy náy."),
         F(1, "Ví dụ: 我会清清白白做人，干干净净赚钱，这样才能心安理得，我父母也不会因我脸上无光。 Tôi sẽ sống trong sạch, kiếm tiền lương thiện, như vậy mới thanh thản, bố mẹ tôi cũng không vì tôi mà mất mặt. 脸上无光 là mất mặt."),
         F(2, "Thứ năm: 一厢情愿. 一厢 là một phía, 情愿 là mong muốn. Chỉ mong muốn của một phía, không xét đến tình hình thực tế. Còn viết là 一相情愿. Tiếng Việt hay nói: yêu đơn phương, hay mơ tưởng viển vông."),
         F(3, "Ví dụ: 爱情的投入和产出从来不成比例，一厢情愿的牺牲到头来感动的往往是自己！ Đầu tư và thu hoạch trong tình yêu xưa nay chẳng bao giờ tương xứng, sự hy sinh đơn phương rốt cuộc thường chỉ làm cảm động chính mình!"),
         F(4, "Thứ sáu: 慷慨解囊. 慷慨 là hào phóng, 解囊 là cởi túi tiền. Rất hào phóng giúp đỡ người khác về tiền bạc. Trong bài, cha mẹ 自愿慷慨解囊, tự nguyện hào phóng cho con tiền."),
         F(5, "Ví dụ: 面对遭受水灾的灾民，他慷慨解囊，一次就捐款十万元。 Trước những người dân gặp lũ lụt, anh ấy hào phóng quyên góp, một lần đã ủng hộ mười vạn tệ.")])

add("bullets", section="Thành ngữ 成语和惯用语", title="Thành ngữ (3): 水深火热 · 自食其力", size=34,
    items=["## 水深火热 shuǐshēn-huǒrè – nước sâu lửa nóng: cảnh sống khốn khổ cùng cực",
           "又是打仗又闹饥荒，平民百姓处于水深火热之中。",
           "有时候我们觉得痛苦，并不是因为我们真的生活在水深火热中，而是因为我们对比了更好的生活……",
           "## 自食其力 zìshí-qílì – tự mình làm ra mà ăn, tự nuôi sống bản thân",
           "只有培养孩子从小认识劳动的价值，着力培养自食其力，艰苦奋斗，勇于开拓的精神，才有益于孩子的健康成长。",
           "梦想常常是宏大的，而我的梦想却很小：就是能让自己自食其力。"],
    say=[F(0, "Thứ bảy: 水深火热. Nước càng lúc càng sâu, lửa càng lúc càng nóng, ví với cuộc sống của dân chúng cực kỳ khốn khổ. Tiếng Việt có cách nói tương tự: nước sôi lửa bỏng. Mẫu hay dùng: 处于水深火热之中, 陷入水深火热之中."),
         F(1, "Ví dụ: 又是打仗又闹饥荒，平民百姓处于水深火热之中。 Nào chiến tranh, nào nạn đói, dân thường sống trong cảnh nước sôi lửa bỏng."),
         F(2, "Ví dụ: 有时候我们觉得痛苦，并不是因为我们真的生活在水深火热中，而是因为我们对比了更好的生活。 Đôi khi ta thấy đau khổ, không phải vì ta thật sự sống trong cảnh khốn cùng, mà vì ta đã so sánh với một cuộc sống tốt hơn."),
         F(3, "Thứ tám: 自食其力. 自 là tự mình, 食 là ăn, 其力 là sức lao động của mình. Dựa vào lao động của chính mình mà sống. Đây chính là điều bài khóa mong người trẻ làm được."),
         F(4, "Ví dụ: 只有培养孩子从小认识劳动的价值，着力培养自食其力，艰苦奋斗，勇于开拓的精神，才有益于孩子的健康成长。 Chỉ có giúp trẻ từ nhỏ hiểu giá trị của lao động, ra sức bồi dưỡng tinh thần tự lập, chịu khó phấn đấu, dám khai phá, mới có lợi cho sự trưởng thành lành mạnh của trẻ. 着力 là dồn sức."),
         F(5, "Ví dụ: 梦想常常是宏大的，而我的梦想却很小：就是能让自己自食其力。 Ước mơ thường lớn lao, còn ước mơ của tôi lại rất nhỏ: chỉ là có thể tự nuôi sống chính mình.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 课后练习", title="Bài tập 1: Chọn thành ngữ thích hợp điền vào chỗ trống (1)", reveal=True, size=33,
    items=["## 理所当然 · 心安理得 · 水深火热 · 清官难断家务事 · 自食其力 · 慷慨解囊 · 一厢情愿",
           "(1) 因为长期的内战，让该地区的人民生活在___中。",
           "Đáp án: 水深火热",
           "(2) 人们可以为一个陌路人的点滴帮助而感激不尽，却无视亲人的种种恩惠，将其视之为___。",
           "Đáp án: 理所当然",
           "(3) 虽然是身体残障，但他们___的精神令人钦佩。",
           "Đáp án: 自食其力",
           "(4) 这几年来，我自食其力，又不占他人便宜，自然___。",
           "Đáp án: 心安理得"],
    say=["Phần cuối là luyện tập. Bài tập một: chọn thành ngữ thích hợp điền vào chỗ trống. Có bảy thành ngữ cho bảy câu.",
         F(1, "Câu một: 因为长期的内战，让该地区的人民生活在什么中。 Vì nội chiến kéo dài, khiến nhân dân khu vực này sống trong cảnh gì. Các bạn để ý, lại gặp đại từ 该 của bài trước. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 水深火热. 生活在水深火热中, sống trong cảnh nước sôi lửa bỏng."),
         F(3, "Câu hai: 人们可以为一个陌路人的点滴帮助而感激不尽，却无视亲人的种种恩惠，将其视之为什么。 Người ta có thể biết ơn khôn xiết một chút giúp đỡ nhỏ của người dưng, nhưng lại phớt lờ bao ân huệ của người thân, coi đó là gì."),
         F(4, "Đáp án: 理所当然. Coi ân huệ của người thân là lẽ đương nhiên. Câu này cũng là lời nhắc nhở những người ăn bám bố mẹ."),
         F(5, "Câu ba: 虽然是身体残障，但他们什么的精神令人钦佩。 Tuy cơ thể khuyết tật, nhưng tinh thần gì của họ khiến người ta khâm phục."),
         F(6, "Đáp án: 自食其力. Tinh thần tự lực, tự nuôi sống bản thân."),
         F(7, "Câu bốn: 这几年来，我自食其力，又不占他人便宜，自然什么。 Mấy năm nay, tôi tự nuôi sống mình, lại không lợi dụng ai, đương nhiên thế nào. Vì câu đã có 自食其力 rồi, nên chỗ trống phải là thành ngữ khác."),
         F(8, "Đáp án: 心安理得. Tự mình làm ra mà ăn, không chiếm lợi của ai, nên lòng thanh thản. Ở đây 心安理得 mang nghĩa tốt.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 1: Chọn thành ngữ thích hợp điền vào chỗ trống (2)", reveal=True, size=33,
    items=["(5) 今天下班路上看见一位穿着破烂的妈妈抱着女儿乞讨，小女孩生了很严重的病，急需住院治疗，路人看到纷纷___。",
           "Đáp án: 慷慨解囊",
           "(6) 古话说，___，他们家的纠纷，谁都没法管。",
           "Đáp án: 清官难断家务事",
           "(7) ……问题一旦出现，就要立刻解决……这样的心态显然不切实际，但___地等待问题自行消失，这种心态更为可怕，通常不会带来任何好结果。",
           "Đáp án: 一厢情愿"],
    say=[F(0, "Câu năm: 今天下班路上看见一位穿着破烂的妈妈抱着女儿乞讨，小女孩生了很严重的病，急需住院治疗，路人看到纷纷什么。 Hôm nay trên đường tan làm thấy một người mẹ ăn mặc rách rưới bế con gái đi xin, cô bé bị bệnh rất nặng, cần nhập viện gấp, người qua đường thấy vậy lần lượt làm gì."),
         F(1, "Đáp án: 慷慨解囊. 路人纷纷慷慨解囊, người qua đường lần lượt hào phóng giúp tiền."),
         F(2, "Câu sáu: 古话说，什么，他们家的纠纷，谁都没法管。 Người xưa nói, gì đó, tranh chấp của nhà họ, chẳng ai quản được."),
         F(3, "Đáp án: 清官难断家务事. Quan thanh liêm cũng khó xử chuyện nhà."),
         F(4, "Câu bảy: 人人都有这样的倾向，问题一旦出现，就要立刻解决，不然他们就会思绪烦乱、寝食不安，这样的心态显然不切实际，但什么地等待问题自行消失，这种心态更为可怕，通常不会带来任何好结果。 Ai cũng có xu hướng: vấn đề vừa xuất hiện là phải giải quyết ngay, nếu không thì rối bời, ăn ngủ không yên; tâm thái ấy rõ ràng không thực tế, nhưng ngồi chờ vấn đề tự biến mất một cách thế nào, thì tâm thái ấy còn đáng sợ hơn."),
         F(5, "Đáp án: 一厢情愿. 一厢情愿地等待问题自行消失, mơ tưởng chủ quan rằng vấn đề sẽ tự biến mất. 更为 là càng, chữ 为 đọc thanh hai.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn từ thích hợp nhất (1)", reveal=True, size=33,
    items=["(1) 当人们变得越来越（ ）技术解决问题的时候，人类独立思考的能力将肯定会江河日下。  A.依靠 B.依赖 C.依附 D.依存",
           "Đáp án: B. 依赖 – dựa dẫm đến mức không tự lập được (sắc thái tiêu cực, đối lập với 独立).",
           "(2) 真相浮出水面，原来他才是（ ）一切的幕后黑手。  A.操纵 B.操持 C.放纵 D.把握",
           "Đáp án: A. 操纵 – đứng sau giật dây: 幕后操纵.",
           "(3) 怎样（ ）恐怖势力对生命的威胁，这个问题（ ）了联合国很久。  A.营造 B.索取 C.根除 D.困扰",
           "Đáp án: C. 根除 · D. 困扰"],
    say=["Bài tập hai: chọn từ thích hợp nhất.",
         F(0, "Câu một: 当人们变得越来越什么技术解决问题的时候，人类独立思考的能力将肯定会江河日下。 Khi con người ngày càng thế nào vào công nghệ để giải quyết vấn đề, khả năng tư duy độc lập của loài người chắc chắn sẽ ngày một sa sút. Lựa chọn: 依靠，依赖，依附，依存. 江河日下 là nước sông ngày một xuống, tức là ngày càng tệ."),
         F(1, "Đáp án: B, 依赖. 依赖 là dựa dẫm đến mức không thể tự lập, mang sắc thái tiêu cực, đối lập với 独立. 依靠 trung tính hơn, chỉ việc nhờ vào; 依附 là bám vào, phụ thuộc; 依存 là cùng tồn tại dựa vào nhau."),
         F(2, "Câu hai: 真相浮出水面，原来他才是什么一切的幕后黑手。 Sự thật lộ ra, hóa ra hắn mới là bàn tay đen đứng sau giật dây mọi chuyện. Lựa chọn: 操纵，操持，放纵，把握."),
         F(3, "Đáp án: A, 操纵. 操纵一切, thao túng mọi thứ, rất hợp với 幕后黑手. 操持 là lo liệu việc nhà; 放纵 là buông thả; 把握 là nắm bắt."),
         F(4, "Câu ba có hai chỗ trống: 怎样什么恐怖势力对生命的威胁，这个问题什么了联合国很久。 Làm sao để gì đó mối đe dọa của thế lực khủng bố đối với sinh mạng, vấn đề này đã làm gì Liên Hợp Quốc từ lâu. Lựa chọn: 营造，索取，根除，困扰."),
         F(5, "Đáp án: chỗ thứ nhất là C, 根除, trừ tận gốc mối đe dọa; chỗ thứ hai là D, 困扰, vấn đề này đã làm Liên Hợp Quốc đau đầu từ lâu.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn từ thích hợp nhất (2)", reveal=True, size=33,
    items=["(4)（ ）失去劳动能力的父母，是儿女应尽的义务。  A.抚养 B.赡养 C.扶养 D.养育",
           "Đáp án: B. 赡养 – con cái nuôi cha mẹ (抚养, 养育: cha mẹ nuôi con).",
           "(5) 真正的爱不是一味（ ）他，而是教会他分辨是非，能够很好地管理自己的情绪。  A.包容 B.忍受 C.纵容 D.扶持",
           "Đáp án: C. 纵容 – 一味纵容: cứ dung túng mãi (đối lập với dạy phân biệt phải trái).",
           "(6) 流言这东西，比流感（ ）的速度更快，比流星所蕴含的能量更巨大……  A.蔓延 B.绝迹 C.隐藏 D.延续",
           "Đáp án: A. 蔓延 – tin đồn lan nhanh hơn cúm."],
    say=[F(0, "Câu bốn: 什么失去劳动能力的父母，是儿女应尽的义务。 Làm gì đối với cha mẹ đã mất khả năng lao động, là nghĩa vụ con cái phải làm tròn. Lựa chọn: 抚养，赡养，扶养，养育."),
         F(1, "Đáp án: B, 赡养. Như đã học, con cái nuôi cha mẹ là 赡养; còn 抚养 và 养育 là cha mẹ nuôi con. 扶养 là nghĩa vụ nuôi nhau giữa vợ chồng, anh chị em."),
         F(2, "Câu năm: 真正的爱不是一味什么他，而是教会他分辨是非，能够很好地管理自己的情绪。 Tình yêu thật sự không phải là cứ một mực thế nào với nó, mà là dạy nó phân biệt phải trái, biết kiểm soát cảm xúc của mình. Lựa chọn: 包容，忍受，纵容，扶持."),
         F(3, "Đáp án: C, 纵容. 一味纵容 là cứ một mực dung túng, đối lập với 教会他分辨是非. Đây cũng chính là bài học của 溺爱 trong bài khóa."),
         F(4, "Câu sáu: 流言这东西，比流感什么的速度更快，比流星所蕴含的能量更巨大，比流氓更具有恶意，比流产更能让人心力憔悴。 Tin đồn ấy à, tốc độ thế nào còn nhanh hơn cúm, năng lượng còn lớn hơn sao băng, ác ý hơn kẻ lưu manh, làm người ta kiệt quệ hơn cả sảy thai. Lựa chọn: 蔓延，绝迹，隐藏，延续. Câu này chơi chữ với chữ 流 ở đầu mỗi từ."),
         F(5, "Đáp án: A, 蔓延. 流感蔓延的速度, tốc độ lây lan của cúm.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn từ thích hợp nhất (3)", reveal=True, size=36,
    items=["(7) 两国边境人民的贸易往来十分（ ）。  A.频频 B.频繁 C.频率 D.频道",
           "Đáp án: B. 频繁 – tính từ làm vị ngữ sau 十分: 往来十分频繁.",
           "(8) 让我们再接再厉，积极推进国际金融（ ）改革。  A.系统 B.系列 C.体系 D.体制",
           "Đáp án: C. 体系 – 国际金融体系: hệ thống tài chính quốc tế."],
    say=[F(0, "Câu bảy: 两国边境人民的贸易往来十分什么。 Giao thương của người dân vùng biên giới hai nước vô cùng thế nào. Lựa chọn: 频频，频繁，频率，频道."),
         F(1, "Đáp án: B, 频繁. Sau 十分 cần một tính từ làm vị ngữ, nên chỉ có 频繁. 频频 là phó từ, phải đứng trước động từ; 频率 là tần suất, 频道 là kênh truyền hình."),
         F(2, "Câu tám: 让我们再接再厉，积极推进国际金融什么改革。 Chúng ta hãy tiếp tục nỗ lực, tích cực thúc đẩy cải cách cái gì của tài chính quốc tế. Lựa chọn: 系统，系列，体系，体制. 再接再厉 là tiếp tục cố gắng hơn nữa."),
         F(3, "Đáp án: C, 体系. 国际金融体系 là hệ thống tài chính quốc tế, một cụm cố định. 体系 nhấn mạnh một chỉnh thể gồm nhiều bộ phận liên hệ; 体制 là thể chế, chế độ tổ chức; 系统 thường nói hệ thống kỹ thuật hay hệ thống trong cơ thể.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ và câu mẫu cho sẵn trả lời câu hỏi (1)", reveal=True, size=32,
    items=["(1) 什么是“啃老”？（所谓……）",
           "Đáp án gợi ý: 所谓“啃老”，就是指已有谋生能力的成年人仍然主要依靠父母养活。",
           "(2) 为什么会出现“啃老”现象？（之所以……是因为……）",
           "Đáp án gợi ý: “啃老”现象之所以出现，一方面是因为年轻人面临就业难、房价高等压力，另一方面是因为父母过度溺爱孩子。",
           "(3) 什么样的亲情关系变得畸形，这种亲情关系给人什么样的感觉？（不免令人……）",
           "Đáp án gợi ý: 成年子女不愿就业、不想独立，衣食住行都依赖年迈的父母，这种畸形的亲情关系不免令人叹息。"],
    say=["Bài tập ba: dùng từ và câu mẫu cho sẵn để trả lời câu hỏi. Đây là câu hỏi mở, thầy đưa đáp án gợi ý dựa theo bài khóa.",
         F(0, "Câu một: 什么是啃老？ Thế nào là ăn bám bố mẹ? Dùng 所谓."),
         F(1, "Đáp án gợi ý: 所谓啃老，就是指已有谋生能力的成年人仍然主要依靠父母养活。 Cái gọi là ăn bám bố mẹ, chính là chỉ người trưởng thành đã có khả năng kiếm sống mà vẫn chủ yếu dựa vào bố mẹ nuôi."),
         F(2, "Câu hai: 为什么会出现啃老现象？ Vì sao xuất hiện hiện tượng ăn bám? Dùng 之所以……是因为……."),
         F(3, "Đáp án gợi ý: 啃老现象之所以出现，一方面是因为年轻人面临就业难、房价高等压力，另一方面是因为父母过度溺爱孩子。 Hiện tượng ăn bám sở dĩ xuất hiện, một mặt là vì người trẻ đối mặt với áp lực khó tìm việc, giá nhà cao, mặt khác là vì cha mẹ quá nuông chiều con cái."),
         F(4, "Câu ba: 什么样的亲情关系变得畸形，这种亲情关系给人什么样的感觉？ Quan hệ tình thân như thế nào thì trở nên méo mó, và nó đem lại cảm giác gì? Dùng 不免令人."),
         F(5, "Đáp án gợi ý: 成年子女不愿就业、不想独立，衣食住行都依赖年迈的父母，这种畸形的亲情关系不免令人叹息。 Con cái trưởng thành không muốn đi làm, không muốn tự lập, mọi thứ đều dựa vào cha mẹ già; quan hệ tình thân méo mó ấy khó tránh khiến người ta thở dài.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ và câu mẫu cho sẵn trả lời câu hỏi (2)", reveal=True, size=32,
    items=["(4) 传统的家庭观念是“养儿防老”，当今社会家庭关系发生了什么样的变化？（不仅……连……甚至……）",
           "Đáp án gợi ý: 如今不仅殷实的家庭有“啃老”的孩子，连并不富裕的家庭也常出现不肯“断奶”的孩子，甚至小两口带着孩子一起“啃老”。",
           "(5) 如何保障老年人的基本权益？（……，以……）",
           "Đáp án gợi ý: 可以通过立法的形式有限度地控制“啃老”现象的蔓延，以保障老年人的基本权益。"],
    say=[F(0, "Câu bốn: 传统的家庭观念是养儿防老，当今社会家庭关系发生了什么样的变化？ Quan niệm gia đình truyền thống là nuôi con phòng già, quan hệ gia đình trong xã hội ngày nay đã thay đổi thế nào? Dùng 不仅……连……甚至……."),
         F(1, "Đáp án gợi ý: 如今不仅殷实的家庭有啃老的孩子，连并不富裕的家庭也常出现不肯断奶的孩子，甚至小两口带着孩子一起啃老。 Ngày nay không chỉ nhà khá giả có con ăn bám, ngay cả nhà không giàu cũng thường có con không chịu cai sữa, thậm chí vợ chồng trẻ dắt con cùng ăn bám."),
         F(2, "Câu năm: 如何保障老年人的基本权益？ Làm thế nào bảo đảm quyền lợi cơ bản của người già? Dùng câu mục đích với 以."),
         F(3, "Đáp án gợi ý: 可以通过立法的形式有限度地控制啃老现象的蔓延，以保障老年人的基本权益。 Có thể thông qua lập pháp để hạn chế ở mức nhất định sự lan rộng của hiện tượng ăn bám, nhằm bảo đảm quyền lợi cơ bản của người già. Ngoài ra các bạn có thể bổ sung: 子女应该自食其力，经常看望父母，以减轻父母的负担。")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Điền từ, thành ngữ vào đoạn tóm tắt bài khóa", reveal=True, size=30,
    items=["## 一厢情愿 · 扶持 · 索取 · 负疚感 · 困扰 · 畸形 · 控告 · 频繁 · 溺爱 · 根除 · 心安理得",
           "湖南长沙一名男子“啃老”遭拒绝后，向法院___父母的不养之“罪”……这样___的亲情关系令人叹息。刚步入社会的年轻人确实需要父母的___，但是___地靠老一辈养活而没有任何___，成为中国家庭的一大___。“啃老”现象___发生……这跟父母的___以及传统的家庭文化有关……子辈在成长过程中可能向父辈___资源……有人认为这只是___，并不能___“啃老”现象。",
           "Đáp án: 控告 · 畸形 · 扶持 · 心安理得 · 负疚感 · 困扰 · 频繁 · 溺爱 · 索取 · 一厢情愿 · 根除"],
    say=["Bài tập bốn: dùng từ và thành ngữ cho sẵn điền vào đoạn văn. Đoạn văn này thực chất là bản tóm tắt bài khóa, nên đây là cách ôn bài rất tốt. Có mười một lựa chọn cho mười một chỗ trống.",
         F(1, "湖南长沙一名男子啃老遭拒绝后，向法院什么父母的不养之罪，令为人父母者心寒。啃老族不缺乏谋生能力却不想独立，不愿就业，这样什么的亲情关系令人叹息。刚步入社会的年轻人确实需要父母的什么，但是什么地靠老一辈养活而没有任何什么，成为中国家庭的一大什么。 Các bạn điền thử phần đầu nhé."),
         F(1, "啃老现象什么发生，问题出现在哪里？有专家分析说，这跟父母的什么以及传统的家庭文化有关。父辈拥有的资源往往比子辈更多，所以子辈在成长过程中可能向父辈什么资源。中国多个省市明令禁止有独立生活能力的成年子女啃老。对于这种条例，有人叫好，也有人认为这只是什么，并不能什么啃老现象。 Các bạn điền tiếp phần sau."),
         F(2, "Đáp án: 向法院控告父母的不养之罪；这样畸形的亲情关系；需要父母的扶持；但是心安理得地靠老一辈养活而没有任何负疚感，成为中国家庭的一大困扰。"),
         F(2, "Phần sau: 啃老现象频繁发生；这跟父母的溺爱以及传统的家庭文化有关；子辈可能向父辈索取资源；有人认为这只是一厢情愿，并不能根除啃老现象。 Các bạn hãy đọc to cả đoạn văn hoàn chỉnh vài lần, coi như kể lại bài khóa bằng lời của mình.")])

# ======================= THẢO LUẬN =======================
add("bullets", chapter="Thảo luận: liên hệ Việt Nam", section="Thảo luận 讨论", title="Thảo luận: “ăn bám bố mẹ” ở Việt Nam", size=34,
    items=["Tục ngữ Việt: “Trẻ cậy cha, già cậy con” ≈ 养儿防老 · “Con hơn cha là nhà có phúc”",
           "Luật Người cao tuổi (2009): con cháu có nghĩa vụ phụng dưỡng ông bà, cha mẹ (= 赡养)",
           "Thực tế: ở nhà bố mẹ sau khi đi làm, nhờ bố mẹ mua nhà, trông cháu… thế nào là “ăn bám”?",
           "## Luyện nói (dùng từ của bài):",
           "我认为，父母帮助子女是情分而不是本分。年轻人步入社会以后，应该尽快学会自食其力，而不是心安理得地“啃老”。",
           "Câu hỏi: 毕业后暂住父母家，算不算“啃老”？怎样才能避免成为“啃老族”？"],
    say=["Trước khi tổng kết, chúng ta cùng liên hệ với Việt Nam.",
         F(0, "Người Việt có câu: trẻ cậy cha, già cậy con, rất gần với 养儿防老. Lại có câu: con hơn cha là nhà có phúc. Cha mẹ Việt cũng thường hy sinh rất nhiều cho con, nhiều khi giống hệt 慷慨解囊 trong bài khóa."),
         F(1, "Về pháp luật, Luật Người cao tuổi của Việt Nam, ban hành năm hai nghìn không trăm lẻ chín, quy định con cháu có nghĩa vụ phụng dưỡng ông bà, cha mẹ. Đó chính là 赡养义务 trong bài khóa."),
         F(2, "Nhưng thế nào mới là ăn bám? Đi làm rồi vẫn ở nhà bố mẹ, không đóng tiền ăn; nhờ bố mẹ bỏ tiền mua nhà, cưới vợ; nhờ ông bà trông cháu cả năm. Ranh giới không hề rõ ràng. Phần ôn tập của đơn vị ở bài sau sẽ có một bài thảo luận đúng về chủ đề này."),
         F(3, "Bây giờ các bạn hãy luyện nói, cố gắng dùng các từ vừa học."),
         F(4, "Câu mẫu: 我认为，父母帮助子女是情分而不是本分。年轻人步入社会以后，应该尽快学会自食其力，而不是心安理得地啃老。 Tôi cho rằng, cha mẹ giúp con là tình nghĩa chứ không phải bổn phận. Người trẻ sau khi bước vào đời nên nhanh chóng học cách tự nuôi sống mình, chứ không phải thản nhiên ăn bám bố mẹ."),
         F(5, "Câu hỏi cho các bạn: 毕业后暂住父母家，算不算啃老？怎样才能避免成为啃老族？ Tốt nghiệp xong tạm ở nhà bố mẹ, có tính là ăn bám không? Làm thế nào để không trở thành tộc ăn bám? Gợi ý: đóng tiền ăn, chia sẻ việc nhà, có kế hoạch dọn ra ở riêng. Hãy tạm dừng video và trả lời bằng tiếng Trung nhé.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết", section="Tổng kết", title="Tổng kết bài 5.2", size=34,
    items=["Từ vựng trọng tâm: 啃老 · 殷实 · 断奶 · 步入 · 谋生 · 畸形 · 扶持 · 负疚 · 索取 · 情分 ≠ 本分 · 抚养 ≠ 赡养 · 溺爱 · 根除 · 蔓延 · 变相 · 营造 · 绝迹",
           "Câu mẫu: 频频 + động từ · 不仅……连……甚至…… · 不免令人…… · 之所以……是因为…… · ……，以…… · 所谓 · 自A自B",
           "Kết hợp từ: 步入社会 · 索取报酬 · 频繁发生 · 疾病蔓延 · 变相加价 · 营造氛围",
           "Thành ngữ: 养儿防老 · 理所当然 · 天经地义 · 心安理得 · 一厢情愿 · 慷慨解囊 · 水深火热 · 自食其力",
           "Thông điệp: 帮你是情分而不是本分 · 两代人既彼此信赖又各自独立"],
    say=["Chúng ta cùng tổng kết bài năm chấm hai.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 啃老，殷实，断奶，步入，谋生，畸形，扶持，负疚，索取，溺爱，根除，蔓延，变相，营造，绝迹. Và hai cặp từ: 情分 khác 本分; 抚养 khác 赡养."),
         F(1, "Về câu mẫu: 频频 đứng trước động từ; câu tăng tiến 不仅……连……甚至……; 不免令人 cộng từ chỉ tâm lý; câu nhân quả 之所以……是因为……; câu mục đích với 以; 所谓 để giải thích khái niệm; và cấu trúc 自A自B như 自立自强, 自娱自乐."),
         F(2, "Về kết hợp từ: 步入社会，索取报酬，频繁发生，疾病蔓延，变相加价，营造氛围."),
         F(3, "Về thành ngữ: 养儿防老，理所当然，天经地义，心安理得，一厢情愿，慷慨解囊，水深火热，自食其力."),
         F(4, "Và thông điệp của bài: cha mẹ giúp con là tình nghĩa chứ không phải bổn phận; gia đình lý tưởng là hai thế hệ vừa tin cậy lẫn nhau, vừa độc lập riêng."),
         "Bài tập về nhà: hãy viết một đoạn văn khoảng ba trăm chữ với đề 我怎么看啃老现象, tôi nhìn nhận hiện tượng ăn bám bố mẹ như thế nào, cố gắng dùng 之所以……是因为……，不仅……连……甚至…… và ít nhất ba thành ngữ của bài.",
         "Cảm ơn các bạn đã theo dõi bài giảng. Ở bài sau, bài năm chấm ba, cũng là bài cuối của Đơn vị năm, chúng ta sẽ bàn về chuyện hôn nhân: 相亲鄙视链：爱情被黑得惨不忍睹。 Chuỗi khinh miệt khi xem mắt: tình yêu bị bôi đen thảm hại. Bài khóa kể về những phiên chợ xem mắt hộ con trong công viên Bắc Kinh. Hẹn gặp lại các bạn. Chúc các bạn học tốt!"])

lesson = {
    "title": "顶石中文 – Bài 5.2: “养儿防老”变“养子啃老”？ (“Nuôi con phòng già” thành “nuôi con ăn bám”?)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"情分": "情奋",            # qíngfèn
                    "本分": "本奋",            # běnfèn
                    "应届": "英届",            # yīngjiè
                    "蔓延": "慢延",            # mànyán
                    "变相": "变向",            # biànxiàng
                    "为人": "维人",            # wéirén
                    "处于": "楚于",            # chǔyú
                    "处在": "楚在",            # chǔzài
                    "行列": "航列",            # hángliè
                    "调动": "掉动",            # diàodòng
                    "相为谋": "相维谋",        # xiāng wéi móu
                    "剥削": "波学",            # bōxuē
                    "着力": "卓力",            # zhuólì
                    "便宜": "骈宜",            # piányi
                    "孝为": "孝维",            # xiào wéi
                    "更为": "更维",            # gèngwéi
                    "十有五": "十又五",        # shí yòu wǔ
                    "长沙": "常沙",            # Chángshā
                    "隐藏": "隐藏"},           # yǐncáng (giữ nguyên)
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds52.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
