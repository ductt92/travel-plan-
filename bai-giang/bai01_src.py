#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Thượng) – Bài 1 «孩子给我们的启示». Chạy để sinh bai01.json."""
import json
import os

TAG = "HSK 6 (Thượng) · Bài 1 · 孩子给我们的启示"
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
    zh="孩子给我们的启示", py="Háizi gěi wǒmen de qǐshì", vi="Bài 1: Điều con trẻ dạy chúng ta",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Thượng.",
         "Hôm nay chúng ta học bài một: 孩子给我们的启示。 Nghĩa là: Điều con trẻ dạy chúng ta.",
         "Đây là bài đầu tiên của cả khóa HSK 6, và cũng là bài mở đầu của Chủ đề một: 生活点滴, tức là Những việc nhỏ nhặt trong cuộc sống.",
         "Bài khóa kể một câu chuyện gia đình rất nhẹ nhàng: một cô bé đã khiến bố mẹ mình nhận ra một bài học quan trọng về cách làm cha mẹ."])

add("bullets", section="Mở đầu", title="HSK 6 là gì?", size=40,
    items=["Cấp cao nhất trong hệ thống HSK 6 cấp",
           "Yêu cầu vốn từ khoảng 5000 từ trở lên",
           "Đọc báo, xem phim, nghe tin tức, diễn đạt ý kiến bằng tiếng Trung khá trôi chảy",
           "Giáo trình chuẩn HSK 6 gồm 2 quyển: Thượng (bài 1–20) và Hạ (bài 21–40)",
           "Bài khóa dài 600–1000 chữ, văn phong gần với báo chí, tạp chí"],
    say=["Vì đây là bài đầu tiên của khóa học, trước khi vào bài, thầy muốn giới thiệu ngắn gọn về HSK 6.",
         F(0, "HSK 6 là cấp cao nhất trong hệ thống HSK sáu cấp, và giáo trình này được biên soạn theo hệ thống đó."),
         F(1, "Ở cấp này, các bạn cần nắm khoảng năm nghìn từ trở lên."),
         F(2, "Đạt HSK 6 nghĩa là các bạn có thể đọc báo, xem phim, nghe tin tức, và trình bày ý kiến của mình bằng tiếng Trung một cách khá trôi chảy."),
         F(3, "Giáo trình chuẩn HSK 6 có hai quyển. Quyển Thượng gồm bài một đến bài hai mươi, quyển Hạ gồm bài hai mươi mốt đến bài bốn mươi. Các bài được chia theo những chủ đề lớn."),
         F(4, "Bài khóa ở cấp này khá dài, thường từ sáu trăm đến một nghìn chữ, văn phong gần với báo chí và tạp chí. Vì vậy, ngoài từ vựng, chúng ta còn phải chú ý nhiều đến phong cách văn viết.")])

add("bullets", section="Mở đầu", title="Mỗi bài giảng được tổ chức thế nào?", size=40,
    items=["Khởi động: câu hỏi làm nóng, học từ theo chữ gốc",
           "Từ mới: đọc mẫu, âm Hán Việt, nghĩa, ví dụ, lưu ý từ dễ nhầm",
           "Bài khóa: nghe từng đoạn → dịch → giảng từ ngữ, cấu trúc",
           "Ngữ pháp, phân biệt từ, phong cách – mỗi phần đều có bài làm thử",
           "Mở rộng, luyện tập, tổng kết và bài tập về nhà"],
    say=["Mỗi bài giảng của thầy đều đi theo một trình tự cố định, giống với bố cục của sách.",
         F(0, "Đầu tiên là phần khởi động: trả lời vài câu hỏi để làm nóng, và học từ theo chữ gốc."),
         F(1, "Tiếp theo là từ mới. Mỗi từ được đọc mẫu hai lần, kèm âm Hán Việt, nghĩa, ví dụ; thầy sẽ đặc biệt nhắc những từ Hán Việt dễ hiểu nhầm."),
         F(2, "Sau đó là bài khóa. Các bạn nghe từng đoạn tiếng Trung trước, rồi xem bản dịch và nghe thầy giảng."),
         F(3, "Rồi đến ngữ pháp, phân biệt từ và phong cách diễn đạt. Phần nào cũng có bài làm thử, có đáp án để các bạn tự kiểm tra."),
         F(4, "Cuối cùng là phần mở rộng, luyện tập, tổng kết và bài tập về nhà.")])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu nội dung bài khóa 孩子给我们的启示 – bài học từ một câu hỏi của con",
           "Nắm vững 40 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: 巴不得 và 别提多……了",
           "Phong cách: từ đồng nghĩa khác nhau về văn viết – khẩu ngữ",
           "Phân biệt hai đại từ 人家 và 别人",
           "Mở rộng: câu sai do dùng từ không đúng"],
    say=["Bài học hôm nay có sáu mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa: chỉ một câu hỏi ngây thơ của con gái đã khiến bố mẹ phải suy nghĩ lại về chính mình."),
         F(1, "Thứ hai, nắm vững bốn mươi từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học hai điểm ngữ pháp rất khẩu ngữ: 巴不得, nghĩa là chỉ mong sao; và cấu trúc 别提多 cộng tính từ, như 别提多高兴了, nghĩa là vui khỏi phải nói."),
         F(3, "Thứ tư, phong cách diễn đạt: những cặp từ cùng nghĩa nhưng một từ dùng trong văn viết, một từ dùng trong khẩu ngữ."),
         F(4, "Thứ năm, phân biệt hai đại từ đều có nghĩa là người khác: 人家 và 别人."),
         F(5, "Thứ sáu, phần mở rộng về các loại câu sai do dùng từ không đúng, một dạng bài rất hay gặp trong đề thi HSK 6."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Câu hỏi khởi động", size=38,
    items=["在你跟父母（或孩子）的关系中，遇到过下列情况吗？如果遇到，想一想该怎么办？",
           "(1) 父母不让孩子看电视，自己却在看。",
           "(2) 父母教育孩子要诚实，自己却说谎。",
           "(3) 父母告诉孩子要多帮助别人，自己有时候却怕麻烦不愿意帮助别人。",
           "如有更多情况，请补充说明。"],
    say=["Chúng ta bắt đầu bằng phần khởi động.",
         F(0, "Sách hỏi: 在你跟父母或孩子的关系中，遇到过下列情况吗？如果遇到，想一想该怎么办？ Trong quan hệ giữa bạn với bố mẹ, hoặc với con cái, bạn đã gặp những tình huống sau chưa? Nếu gặp rồi, hãy nghĩ xem nên làm thế nào."),
         F(1, "Tình huống một: 父母不让孩子看电视，自己却在看。 Bố mẹ không cho con xem tivi, còn mình thì lại xem."),
         F(2, "Tình huống hai: 父母教育孩子要诚实，自己却说谎。 Bố mẹ dạy con phải trung thực, còn mình thì lại nói dối."),
         F(3, "Tình huống ba: 父母告诉孩子要多帮助别人，自己有时候却怕麻烦不愿意帮助别人。 Bố mẹ dặn con phải giúp đỡ người khác, còn mình đôi khi lại ngại phiền, không muốn giúp ai."),
         F(4, "如有更多情况，请补充说明。 Nếu có tình huống khác, hãy bổ sung thêm. Các bạn để ý chữ 却 xuất hiện trong cả ba câu, nghĩa là nhưng lại, dùng để nói hai việc trái ngược nhau. Đây cũng chính là chủ đề của bài khóa hôm nay."),
         "Các bạn hãy tạm dừng video, thử trả lời bằng tiếng Trung, rồi mới xem tiếp nhé."])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 女 và 无", size=36,
    items=["## 女 (nữ): phụ nữ, con gái",
           "女人 phụ nữ · 女士 quý bà, quý cô · 女厕 nhà vệ sinh nữ · 女方 nhà gái · 女生 nữ sinh · 女皇 nữ hoàng · 女装 đồ nữ · 女性 nữ giới",
           "妇女 phụ nữ · 少女 thiếu nữ · 美女 mỹ nữ · 独生女 con gái một · 母女 mẹ con (gái)",
           "## 无 (vô): không có",
           "无数 vô số · 无边 vô biên · 无价 vô giá · 无声 không tiếng động · 无语 cạn lời · 无法 không thể",
           "无关 không liên quan · 无私 không vụ lợi, không ích kỷ · 无悔 không hối tiếc · 无望 vô vọng"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo. Cách này rất có lợi cho người Việt, vì hầu hết các chữ đều có âm Hán Việt quen thuộc.",
         F(0, "Nhóm thứ nhất có chữ 女, Hán Việt là nữ, nghĩa là phụ nữ, con gái."),
         F(1, "女人，女士，女厕，女方，女生，女皇，女装，女性。 Tức là: phụ nữ, quý bà hay quý cô, nhà vệ sinh nữ, nhà gái, nữ sinh, nữ hoàng, đồ nữ, và nữ giới."),
         F(2, "妇女，少女，美女，独生女，母女。 Tức là: phụ nữ, thiếu nữ, mỹ nữ, con gái một, và mẹ con. Từ 独生女 có ngay trong câu đầu của bài khóa."),
         F(3, "Nhóm thứ hai có chữ 无, Hán Việt là vô, nghĩa là không có."),
         F(4, "无数，无边，无价，无声，无语，无法。 Tức là: vô số, vô biên, vô giá, không tiếng động, cạn lời, và không thể."),
         F(5, "无关，无私，无悔，无望。 Tức là: không liên quan, không vụ lợi, không hối tiếc, và vô vọng. Cẩn thận với từ 无私! Tiếng Việt vô tư thường hiểu là hồn nhiên, không lo nghĩ; còn 无私 tiếng Trung là không ích kỷ, hết lòng vì người khác. Trong bài khóa có cụm 热情无私, nhiệt tình và không ích kỷ.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 醒 và 视", size=38,
    items=["## 醒 (tỉnh): thức dậy, tỉnh ra",
           "叫醒 gọi dậy · 吵醒 làm ồn đánh thức · 惊醒 giật mình tỉnh giấc · 推醒 lay dậy · 睡醒 ngủ dậy",
           "## 视 (thị): nhìn, xem",
           "重视 coi trọng · 忽视 xem nhẹ · 轻视 coi thường · 环视 nhìn quanh · 对视 nhìn nhau · 相视 nhìn nhau",
           "视觉 thị giác · 视线 tầm nhìn · 视而不见 nhìn mà như không thấy"],
    say=[F(0, "Nhóm thứ ba có chữ 醒, Hán Việt là tỉnh, nghĩa là thức dậy, tỉnh ra."),
         F(1, "叫醒，吵醒，惊醒，推醒，睡醒。 Tức là: gọi dậy, làm ồn đánh thức, giật mình tỉnh giấc, lay dậy, và ngủ dậy. Bài khóa có câu 不用叫就醒了, không cần gọi cũng tự dậy."),
         F(2, "Nhóm cuối cùng có chữ 视, Hán Việt là thị, nghĩa là nhìn, xem."),
         F(3, "重视，忽视，轻视，环视，对视，相视。 Tức là: coi trọng, xem nhẹ, coi thường, nhìn quanh, và hai từ cuối đều là nhìn nhau. Bài khóa có hai từ trong nhóm này: 我和老公对视一眼, tôi và chồng nhìn nhau một cái; và 不可忽视, không thể xem nhẹ."),
         F(4, "视觉，视线，视而不见。 Tức là: thị giác, tầm nhìn, và nhìn mà như không thấy."),
         "Các bạn thấy không, chỉ cần nắm nghĩa của một chữ gốc, ta có thể đoán được nghĩa của cả một nhóm từ. Hãy áp dụng cách này khi học từ mới nhé."])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng)
V = [
    ("启示", "qǐshì", "khải thị", "danh từ", "sự gợi mở, bài học rút ra", "这件事给了我很大的启示。", "Chuyện này đã cho tôi một bài học lớn.",
     "Danh từ, nghĩa là sự gợi mở, điều khai sáng, bài học ta rút ra từ một sự việc. Tên bài 孩子给我们的启示 chính là điều con trẻ dạy chúng ta. Hay gặp trong các cụm 给人启示，得到启示."),
    ("老公", "lǎogōng", "lão công", "danh từ", "chồng (khẩu ngữ)", "我和老公爽快地答应下来。", "Tôi và chồng vui vẻ nhận lời ngay.",
     "Danh từ khẩu ngữ, nghĩa là chồng. Chữ 老 ở đây không có nghĩa là già, mà là tiền tố thân mật. Vợ thì gọi là 老婆. Trong văn viết trang trọng, người ta dùng 丈夫 và 妻子."),
    ("爽快", "shuǎngkuai", "sảng khoái", "tính từ", "thẳng thắn, dứt khoát, vui vẻ (nhận lời)", "他爽快地答应了我的要求。", "Anh ấy vui vẻ nhận lời đề nghị của tôi ngay.",
     "Tính từ. Cẩn thận, đây là từ dễ hiểu nhầm! Tiếng Việt sảng khoái thường chỉ cảm giác khoan khoái, dễ chịu. Còn 爽快 trong bài chủ yếu chỉ tính cách thẳng thắn, dứt khoát, nhận lời ngay không chần chừ. Chữ thứ hai đọc nhẹ."),
    ("巴不得", "bābude", "ba bất đắc", "động từ", "chỉ mong sao, mong mỏi tha thiết", "我巴不得马上放假。", "Tôi chỉ mong được nghỉ ngay lập tức.",
     "Động từ khẩu ngữ, nghĩa là chỉ mong sao, mong đến mức không đợi được. Đây là điểm ngữ pháp thứ nhất của bài, thầy sẽ giảng kỹ ở phần sau."),
    ("嚷", "rǎng", "nhượng", "động từ", "la to, kêu lên, đòi ầm lên", "孩子嚷着要吃冰淇淋。", "Đứa trẻ cứ la lên đòi ăn kem.",
     "Động từ, nghĩa là la to, kêu ầm lên. Trong bài, 嚷着要 nghĩa là cứ một mực kêu đòi, rất hợp với tính cách trẻ con."),
    ("拿手", "náshǒu", "nã thủ", "tính từ", "sở trường, giỏi, thành thạo", "这是我妈妈的拿手菜。", "Đây là món tủ của mẹ tôi.",
     "Tính từ, nghĩa là sở trường, làm rất giỏi. 拿手菜 là món tủ, món nấu ngon nhất. Trong bài: 爸爸最拿手的美味佳肴, những món ngon mà bố nấu giỏi nhất."),
    ("佳肴", "jiāyáo", "giai hào", "danh từ", "món ăn ngon", "桌上摆满了美味佳肴。", "Trên bàn bày đầy món ngon.",
     "Danh từ văn viết, nghĩa là món ăn ngon. Hay dùng trong cụm 美味佳肴, món ngon vật lạ. Chữ đầu là giai, nghĩa là tốt đẹp, như trong giai nhân."),
    ("异常", "yìcháng", "dị thường", "phó từ", "đặc biệt, hết sức, cực kỳ", "林林变得异常勤劳。", "Lâm Lâm trở nên chăm chỉ lạ thường.",
     "Cẩn thận, từ dễ nhầm! Tiếng Việt dị thường nghĩa là bất thường, khác lạ. Trong tiếng Trung, 异常 làm tính từ cũng có nghĩa đó, nhưng trong bài này nó là phó từ đứng trước tính từ, nghĩa là hết sức, cực kỳ, giống 非常 nhưng mang màu sắc văn viết."),
    ("勤劳", "qínláo", "cần lao", "tính từ", "siêng năng, cần cù", "她是一位勤劳的母亲。", "Bà là một người mẹ cần cù.",
     "Tính từ, nghĩa là siêng năng, chịu khó lao động. Gần nghĩa với 勤奋, nhưng 勤劳 nhấn mạnh chăm làm việc, còn 勤奋 hay dùng cho chăm học, chăm nghiên cứu."),
    ("绅士", "shēnshì", "thân sĩ", "danh từ", "quý ông, người lịch thiệp", "他是一位真正的绅士。", "Anh ấy là một quý ông thực thụ.",
     "Danh từ, nghĩa là quý ông, người đàn ông lịch thiệp. 绅士风度 là phong thái quý ông. Lưu ý: tiếng Việt thân sĩ là tầng lớp có danh vọng thời xưa, còn tiếng Trung hiện đại thường dùng theo nghĩa quý ông lịch thiệp."),
    ("风度", "fēngdù", "phong độ", "danh từ", "phong thái, cốt cách, cách cư xử", "他输了比赛也很有风度。", "Anh ấy thua trận vẫn rất có phong thái.",
     "Lại một từ dễ nhầm! Tiếng Việt phong độ hay dùng cho trạng thái thi đấu, như cầu thủ đang có phong độ tốt. Còn 风度 tiếng Trung là phong thái, cách cư xử đẹp, đàng hoàng. Thua mà không cáu giận thì gọi là 有风度."),
    ("十足", "shízú", "thập túc", "tính từ", "tràn đầy, mười phần, hết mức", "他对这次比赛信心十足。", "Anh ấy tràn đầy tự tin vào trận đấu này.",
     "Tính từ, nghĩa là đầy đủ, mười phần mười, thường đứng sau danh từ: 信心十足，干劲十足，风度十足."),
    ("督促", "dūcù", "đốc xúc", "động từ", "đôn đốc, thúc giục", "老师督促学生按时完成作业。", "Thầy giáo đôn đốc học sinh làm bài đúng hạn.",
     "Động từ, nghĩa là giám sát và thúc giục người khác làm việc. Tiếng Việt có từ đốc thúc, rất gần nghĩa."),
    ("打架", "dǎ jià", "đả giá", "động từ", "đánh nhau", "两个孩子从来不打架。", "Hai đứa trẻ chưa bao giờ đánh nhau.",
     "Động từ ly hợp, nghĩa là đánh nhau. Có thể tách ra: 打了一架, đánh nhau một trận. Còn cãi nhau thì gọi là 吵架."),
    ("别扭", "bièniu", "biệt nữu", "tính từ", "khó chịu, gượng gạo; (闹别扭) giận dỗi nhau", "他们俩又闹别扭了。", "Hai đứa lại giận dỗi nhau rồi.",
     "Tính từ, nghĩa là khó chịu, gượng gạo, không thuận. 闹别扭 là giận dỗi, xích mích với nhau. Chú ý chữ đầu đọc thanh bốn, chữ sau đọc nhẹ, khác với 别人."),
    ("融洽", "róngqià", "dung hiệp", "tính từ", "hòa hợp, êm thấm", "同事之间的关系很融洽。", "Quan hệ giữa các đồng nghiệp rất hòa hợp.",
     "Tính từ, nghĩa là hòa hợp, êm thấm, thường dùng cho quan hệ hoặc bầu không khí: 关系融洽，气氛融洽."),
    ("亲密", "qīnmì", "thân mật", "tính từ", "thân thiết, gắn bó", "他们是一对亲密的朋友。", "Họ là một đôi bạn thân thiết.",
     "Tính từ, nghĩa là thân thiết, gắn bó khăng khít. Âm Hán Việt là thân mật, nhưng nghĩa mạnh hơn, chỉ quan hệ rất gần gũi, như 亲密无间, thân thiết không chút khoảng cách."),
    ("忽略", "hūlüè", "hốt lược", "động từ", "lơ là, bỏ qua, không để ý đến", "这个问题不能忽略。", "Vấn đề này không thể bỏ qua.",
     "Động từ, nghĩa là bỏ sót, không để ý tới. Gần nghĩa với 忽视. Trong bài: 大有忽略我们的趋势, hai đứa trẻ có vẻ sắp quên luôn cả bố mẹ."),
    ("嫉妒", "jídù", "tật đố", "động từ", "ghen tị, đố kỵ", "他嫉妒别人的成功。", "Anh ta ghen tị với thành công của người khác.",
     "Động từ, nghĩa là ghen tị, đố kỵ. Trong bài, bố mẹ nói đùa rằng mình hơi 嫉妒 vì hai đứa trẻ thân nhau quá."),
    ("滔滔不绝", "tāotāo bù jué", "thao thao bất tuyệt", "thành ngữ", "nói thao thao bất tuyệt, không ngớt", "他一说起足球就滔滔不绝。", "Hễ nói đến bóng đá là anh ấy thao thao bất tuyệt.",
     "Thành ngữ, âm Hán Việt là thao thao bất tuyệt, giống hệt tiếng Việt, nghĩa là nói liên tục không dứt."),
    ("嘲笑", "cháoxiào", "trào tiếu", "động từ", "chê cười, chế nhạo", "不要嘲笑别人的缺点。", "Đừng chế nhạo khuyết điểm của người khác.",
     "Động từ, nghĩa là chế giễu, cười nhạo. Chữ đầu là trào, như trong trào phúng của tiếng Việt."),
    ("讨好", "tǎo hǎo", "thảo hảo", "động từ", "lấy lòng, nịnh", "他总是想办法讨好领导。", "Anh ta lúc nào cũng tìm cách lấy lòng sếp.",
     "Động từ, nghĩa là lấy lòng, cố làm vừa lòng người khác, thường mang nghĩa xấu là nịnh bợ."),
    ("郑重", "zhèngzhòng", "trịnh trọng", "tính từ", "nghiêm túc, trịnh trọng", "他郑重地向大家道歉。", "Anh ấy nghiêm túc xin lỗi mọi người.",
     "Tính từ, nghĩa là nghiêm túc, trịnh trọng, thể hiện thái độ coi trọng. Hay làm trạng ngữ, như 郑重地说，郑重地宣布."),
    ("当面", "dāng miàn", "đương diện", "phó từ", "trước mặt, trực tiếp", "有意见应该当面提。", "Có ý kiến thì nên nói thẳng trước mặt.",
     "Phó từ, nghĩa là trước mặt, mặt đối mặt. Trái nghĩa với 背后, sau lưng. Trong bài: 应该当面说, nên nói thẳng trước mặt."),
    ("人家", "rénjia", "nhân gia", "đại từ", "người ta, người khác", "人家都这么说。", "Người ta đều nói như vậy.",
     "Đại từ, nghĩa là người ta, người khác. Chữ sau đọc nhẹ. Đây là đề tài phân biệt từ của bài, thầy sẽ so sánh nó với 别人 ở phần sau."),
    ("附和", "fùhè", "phụ họa", "động từ", "phụ họa, hùa theo", "他总是附和别人的意见。", "Anh ta lúc nào cũng hùa theo ý kiến người khác.",
     "Động từ, nghĩa là nói theo, hùa theo, âm Hán Việt phụ họa giống tiếng Việt. Chú ý chữ thứ hai đọc thanh bốn, không phải thanh hai như trong 和平."),
    ("大伙儿", "dàhuǒr", "đại hỏa", "đại từ", "mọi người, cả bọn (khẩu ngữ)", "大伙儿一起去吧！", "Mọi người cùng đi nào!",
     "Đại từ khẩu ngữ, nghĩa là mọi người, cả bọn, giống 大家. Chữ giữa giống trong 伙伴, nghĩa là bạn bè."),
    ("和睦", "hémù", "hòa mục", "tính từ", "hòa thuận", "他们一家人生活得很和睦。", "Cả nhà họ sống rất hòa thuận.",
     "Tính từ, nghĩa là hòa thuận, thường dùng cho gia đình, hàng xóm: 和睦相处, chung sống hòa thuận."),
    ("宽容", "kuānróng", "khoan dung", "động từ", "khoan dung, bao dung", "对别人要宽容一些。", "Với người khác nên bao dung một chút.",
     "Động từ, cũng dùng như tính từ, nghĩa là khoan dung, rộng lượng. Âm Hán Việt khoan dung giống hệt tiếng Việt."),
    ("疑惑", "yíhuò", "nghi hoặc", "danh từ", "sự nghi ngờ, thắc mắc", "她一脸疑惑地看着我。", "Cô ấy nhìn tôi với vẻ mặt đầy thắc mắc.",
     "Danh từ, cũng dùng làm động từ, nghĩa là nghi hoặc, thắc mắc, chưa hiểu. 一脸的疑惑 là vẻ mặt đầy thắc mắc."),
    ("反问", "fǎnwèn", "phản vấn", "động từ", "hỏi lại, hỏi vặn lại", "他不回答，却反问我为什么。", "Anh ấy không trả lời, lại hỏi ngược tôi tại sao.",
     "Động từ, nghĩa là hỏi ngược lại. 反问句 là câu hỏi tu từ. Trong bài: 女儿反问道, con gái hỏi vặn lại."),
    ("瞬间", "shùnjiān", "thuấn gian", "danh từ", "khoảnh khắc, trong chớp mắt", "瞬间，天就黑了。", "Trong chớp mắt, trời đã tối.",
     "Danh từ, nghĩa là khoảnh khắc rất ngắn, chỉ bằng một cái chớp mắt."),
    ("鸦雀无声", "yāquè-wúshēng", "nha tước vô thanh", "thành ngữ", "im phăng phắc, lặng ngắt như tờ", "教室里鸦雀无声。", "Lớp học im phăng phắc.",
     "Thành ngữ. Chữ đầu là con quạ, chữ thứ hai là chim sẻ, như trong 麻雀. Nghĩa đen là đến quạ và sẻ cũng không kêu, tức là im phăng phắc."),
    ("启蒙", "qǐméng", "khải mông", "động từ", "khai tâm, dạy vỡ lòng", "她是我的启蒙老师。", "Cô ấy là cô giáo vỡ lòng của tôi.",
     "Động từ, nghĩa là dạy vỡ lòng, khai sáng cho người mới bắt đầu. 启蒙老师 là người thầy dạy mình đầu tiên."),
    ("任", "rèn", "nhiệm", "lượng từ", "đời, nhiệm kỳ (lần giữ một chức vụ)", "他是这所学校的第三任校长。", "Ông ấy là hiệu trưởng đời thứ ba của trường này.",
     "Lượng từ, dùng để đếm số lần, số đời đảm nhiệm một chức vụ. Âm Hán Việt là nhiệm, như trong nhiệm kỳ. Trong bài: 父母就是孩子的第一任老师, cha mẹ là người thầy đầu tiên của con."),
    ("反驳", "fǎnbó", "phản bác", "động từ", "phản bác, bác lại", "他的观点被大家反驳了。", "Quan điểm của anh ấy bị mọi người phản bác.",
     "Động từ, âm Hán Việt phản bác, nghĩa giống tiếng Việt: đưa ra lý lẽ để bác bỏ ý kiến của người khác."),
    ("意识", "yìshí", "ý thức", "động từ", "nhận ra, ý thức được (thường: 意识到)", "我意识到自己错了。", "Tôi nhận ra mình đã sai.",
     "Tiếng Việt ý thức thường là danh từ. Tiếng Trung 意识 cũng là danh từ, nhưng trong bài nó là động từ, thường đi với 到: 意识到, nhận ra; phủ định là 意识不到, không nhận ra."),
    ("实行", "shíxíng", "thực hành", "động từ", "thực hiện, thi hành, áp dụng", "这个城市实行垃圾分类。", "Thành phố này thực hiện phân loại rác.",
     "Từ dễ nhầm! Tiếng Việt thực hành là luyện tập bằng thao tác thực tế, như giờ thực hành. Còn 实行 tiếng Trung là đưa vào thực hiện một chính sách, chế độ, tiêu chuẩn. Thực hành theo nghĩa tiếng Việt thì tiếng Trung nói là 实践 hoặc 练习."),
    ("严厉", "yánlì", "nghiêm lệ", "tính từ", "nghiêm khắc, gay gắt", "父亲对我一直很严厉。", "Bố luôn rất nghiêm khắc với tôi.",
     "Tính từ, nghĩa là nghiêm khắc, gay gắt. Mạnh hơn 严格: 严格 là chặt chẽ theo quy định, còn 严厉 nhấn mạnh thái độ nghiêm khắc, khiến người khác phải sợ."),
    ("约束", "yuēshù", "ước thúc", "động từ", "ràng buộc, kiềm chế, giữ gìn", "我们要约束好自己的言行。", "Chúng ta phải giữ gìn tốt lời nói và việc làm của mình.",
     "Động từ, nghĩa là ràng buộc, kiềm chế, giữ cho không vượt quá giới hạn. 约束自己 là tự kiềm chế bản thân. Từ này nằm trong câu chốt của bài khóa."),
]

add("bullets", chapter="Từ mới (40 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 1 có 40 từ mới, chia thành 14 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 爽快 (kuai nhẹ) · 别扭 (biè) · 附和 (hè) · 人家 (jia nhẹ)",
           "Từ Hán Việt dễ nhầm: 爽快 · 异常 · 风度 · 实行"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có bốn mươi từ, thầy chia thành mười bốn nhóm nhỏ, mỗi nhóm hai hoặc ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số từ có âm đọc đặc biệt, như 爽快，别扭，附和，人家. Thầy sẽ nhắc khi gặp."),
         F(4, "Đặc biệt, có mấy từ Hán Việt rất dễ hiểu nhầm, như 爽快，异常，风度，实行. Nghĩa của chúng trong tiếng Trung khác với tiếng Việt, các bạn chú ý nhé. Chúng ta bắt đầu.")])

sizes = [3] * 12 + [2, 2]
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
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung nếu khác: số viết bằng chữ Hán])
P = [
    ("林林和天天是同学。天天的父母要出差，想请我们帮忙照看几天女儿，我和老公爽快地答应下来，有个孩子和我们的独生女朝夕相处，我们巴不得呢！",
     "Lâm Lâm và Thiên Thiên là bạn học. Bố mẹ Thiên Thiên phải đi công tác, muốn nhờ chúng tôi trông giúp con gái họ vài ngày. Tôi và chồng vui vẻ nhận lời ngay: có một đứa trẻ sớm tối ở bên con gái một của chúng tôi, chúng tôi mong còn chẳng được ấy chứ!",
     ["出差 là đi công tác. 照看 là trông nom, chăm sóc. 爽快地答应下来 là vui vẻ nhận lời ngay; 下来 ở đây cho biết việc đã được chốt lại.",
      "朝夕相处 nghĩa là sớm tối ở bên nhau; 朝夕 là sáng và tối. 我们巴不得呢 nghĩa là chúng tôi mong còn không được ấy chứ, đây là điểm ngữ pháp thứ nhất."]),
    ("最兴奋的是林林，嚷着要用爸爸最拿手的美味佳肴欢迎天天来我家，还提出，她的书桌可以和天天共用。看到女儿对伙伴热情无私，我和老公别提多高兴了。",
     "Phấn khởi nhất là Lâm Lâm, cứ một mực đòi bố nấu những món ngon sở trường nhất để chào đón Thiên Thiên đến nhà, lại còn đề nghị cho Thiên Thiên dùng chung bàn học của mình. Thấy con gái nhiệt tình, không chút ích kỷ với bạn, tôi và chồng vui khỏi phải nói.",
     ["最兴奋的是林林: câu đảo nhấn mạnh, đưa phần được nhấn mạnh 林林 ra sau 是. 嚷着要 là cứ kêu đòi. 提出 là đề xuất, nêu ra. 共用 là dùng chung.",
      "伙伴 là bạn bè, bạn cùng chơi. 热情无私 là nhiệt tình, không ích kỷ. 别提多高兴了 là vui khỏi phải nói, đây là điểm ngữ pháp thứ hai."]),
    ("天天还没来，林林就变得异常勤劳，将屋子收拾得干干净净，东西摆放得整整齐齐，什么好事都想着天天。我家林林虽是女孩，却也绅士风度十足。",
     "Thiên Thiên còn chưa đến, Lâm Lâm đã trở nên chăm chỉ lạ thường: dọn dẹp nhà cửa sạch sẽ tinh tươm, xếp đặt đồ đạc ngăn nắp gọn gàng, có chuyện gì tốt cũng nghĩ đến Thiên Thiên. Lâm Lâm nhà tôi tuy là con gái, nhưng lại đầy phong thái của một quý ông.",
     ["还没……就…… nghĩa là còn chưa… đã…. 将屋子收拾得干干净净: chữ đầu câu này là cách nói văn viết, tương đương 把屋子. Tính từ lặp lại như 干干净净，整整齐齐 làm mức độ mạnh hơn.",
      "什么好事都想着天天: chuyện tốt gì cũng nghĩ đến Thiên Thiên. 虽是……却也…… nghĩa là tuy là… nhưng lại…. Nói một cô bé 绅士风度十足 là cách nói hài hước, ý khen cô bé rất biết nhường nhịn, chăm lo cho bạn."]),
    ("天天的到来，使我和老公的日子过得异常省心。两个孩子每天早上不用叫就醒了，上学不用接送，做作业不用督促；她们不打架，不闹别扭，关系别提多融洽了。",
     "Sự có mặt của Thiên Thiên khiến những ngày của tôi và chồng trôi qua nhàn nhã lạ thường. Mỗi sáng hai đứa trẻ không cần gọi cũng tự dậy, đi học không cần đưa đón, làm bài tập không cần đốc thúc; chúng không đánh nhau, không giận dỗi, quan hệ hòa hợp khỏi phải nói.",
     ["天天的到来 là sự xuất hiện của Thiên Thiên; 到来 ở đây là danh từ. 使 nghĩa là khiến cho. 省心 là đỡ phải lo, nhàn tâm.",
      "Tác giả dùng một loạt vế song song: 不用叫就醒了，不用接送，不用督促，rồi 不打架，不闹别扭. Cách liệt kê này làm câu văn nhịp nhàng và rất sinh động."]),
    ("看到女儿和天天这么亲密，大有忽略我们的趋势，我和老公都有点儿嫉妒了。",
     "Thấy con gái và Thiên Thiên thân thiết như vậy, đến mức có vẻ như sắp quên mất bố mẹ, tôi và chồng đều thấy hơi ghen tị.",
     ["大有……的趋势 nghĩa là rất có xu hướng…, có vẻ như sắp…. Bố mẹ ghen tị với con là một cách nói đùa, giọng văn rất dí dỏm."]),
    ("这天晚上，两个孩子做完作业，开始滔滔不绝地聊了起来，一个说，我不喜欢王朵朵，她就喜欢跟穿得漂亮的同学一起玩儿，还老嘲笑别人。另一个说我讨厌高春来，他最会讨好老师了……",
     "Tối hôm đó, hai đứa làm xong bài tập rồi bắt đầu trò chuyện thao thao bất tuyệt. Một đứa nói: con không thích Vương Đóa Đóa, bạn ấy chỉ thích chơi với những bạn ăn mặc đẹp, lại còn hay chế giễu người khác. Đứa kia nói: con ghét Cao Xuân Lai, bạn ấy giỏi nịnh thầy cô nhất…",
     ["一个说……另一个说…… nghĩa là một người nói…, người kia nói…. Đây là mẫu câu trong bài tập bốn. 聊了起来: 起来 chỉ hành động bắt đầu và tiếp diễn.",
      "就喜欢 ở đây là chỉ thích. 还老嘲笑别人: 老 trong khẩu ngữ nghĩa là luôn luôn, hay. 最会讨好老师 nghĩa là giỏi nịnh thầy cô nhất."]),
    ("我和老公对视一眼，这么小的孩子怎么学会了背后议论人。我郑重地走到她们跟前，严肃地说：“看到别人有缺点，应该当面说，背后说人家的坏话不好。”",
     "Tôi và chồng nhìn nhau: trẻ con bé thế này sao đã học được cách bàn tán sau lưng người khác? Tôi nghiêm trang bước đến trước mặt hai đứa, nghiêm giọng nói: Thấy người khác có khuyết điểm thì nên nói thẳng trước mặt, nói xấu người ta sau lưng là không tốt.",
     ["对视一眼 là nhìn nhau một cái. 背后议论人 là bàn tán sau lưng người khác. 跟前 là trước mặt, ngay cạnh.",
      "Lời bố mẹ dạy có cặp từ trái nghĩa 当面 và 背后: trước mặt và sau lưng. 人家 ở đây nghĩa là người khác. 说坏话 là nói xấu."]),
    ("老公也在旁边附和：“大伙儿要和睦相处，对人要宽容。”女儿却是一脸的疑惑，反问道：“你们不是也有时候说，哪个朋友好相处，哪个朋友很自私吗？”",
     "Chồng tôi ở bên cạnh cũng phụ họa: Mọi người phải chung sống hòa thuận, đối xử với người khác phải bao dung. Con gái lại có vẻ mặt đầy thắc mắc, hỏi vặn lại: Chẳng phải bố mẹ đôi khi cũng nói bạn nào dễ gần, bạn nào ích kỷ đó sao?",
     ["附和 là hùa theo. 和睦相处 là chung sống hòa thuận. 一脸的疑惑 là vẻ mặt đầy thắc mắc. 反问道 là hỏi vặn lại, cách nói văn viết của 反问说.",
      "你们不是也有时候说，哪个朋友好相处，哪个朋友很自私吗？ là câu hỏi phản vấn, nghĩa là chẳng phải bố mẹ cũng… sao? Thật ra cô bé muốn nói: bố mẹ cũng nhận xét người khác sau lưng đấy thôi. 好相处 là dễ gần, 自私 là ích kỷ."]),
    ("瞬间我和老公被问得说不出话来，屋子里鸦雀无声。",
     "Trong khoảnh khắc ấy, tôi và chồng bị hỏi đến mức không nói nên lời, trong phòng im phăng phắc.",
     ["被问得说不出话来 là câu bị động có bổ ngữ chỉ mức độ, nghĩa là bị hỏi đến mức cứng họng. 鸦雀无声 diễn tả rất đắt sự im lặng ngượng ngùng của bố mẹ."]),
    ("人们常说，启蒙老师的重要性不可忽视，父母就是孩子的第一任老师，这话确实不假，可如果这次不是女儿反驳，我还意识不到，我们自己的做法和对孩子的要求实行的是两套标准，那便是对自己宽容，对孩子严厉。",
     "Người ta thường nói, vai trò của người thầy vỡ lòng không thể xem nhẹ, cha mẹ chính là người thầy đầu tiên của con cái. Câu này quả thật không sai. Nhưng nếu lần này không có con gái phản bác, tôi vẫn chưa nhận ra rằng cách làm của chính chúng tôi và yêu cầu đối với con là hai tiêu chuẩn khác nhau, đó là: dễ dãi với bản thân, nghiêm khắc với con cái.",
     ["人们常说……，这话确实不假，可如果…… nghĩa là: người ta thường nói…, câu đó quả không sai, nhưng nếu…. Đây là cách thừa nhận một ý rồi chuyển sang ý mới, có trong bài tập bốn. 不可忽视 là không thể xem nhẹ.",
      "两套标准 là hai tiêu chuẩn, hay tiêu chuẩn kép. 那便是 là cách nói văn viết của 那就是. 对自己宽容，对孩子严厉 là hai vế đối nhau rất cân đối."]),
    ("孩子也可以是我们的老师啊。说真的，这次是孩子给我上了一课：我深深地感到，想当好父母，首先要约束好自己的言行。",
     "Trẻ con cũng có thể là thầy của chúng ta đấy! Nói thật, lần này con đã dạy tôi một bài học: tôi cảm nhận sâu sắc rằng, muốn làm cha mẹ tốt, trước hết phải giữ gìn tốt lời nói và việc làm của chính mình.",
     ["给我上了一课 nghĩa là dạy cho tôi một bài học. 想……，首先要…… nghĩa là muốn… thì trước hết phải….",
      "言行 là lời nói và việc làm. Câu cuối này chính là chủ đề của cả bài: cha mẹ muốn dạy con thì phải làm gương trước."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 孩子给我们的启示",
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Nhân vật: 林林 Lâm Lâm (con gái) · 天天 Thiên Thiên (bạn học) · 我 và 老公 (bố mẹ)",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 孩子给我们的启示, dài sáu trăm chín mươi tám chữ.",
         F(0, "Thầy chia bài thành mười một đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Bài khóa có các nhân vật: 林林, cô con gái; 天天, bạn học của cô bé; và người kể chuyện là người mẹ, cùng 老公, tức là người bố."),
         F(3, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 100 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi, cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Tóm tắt nội dung", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5) – phần 1", size=36,
    items=["## 1. 天天要来，全家的态度怎么样？",
           "“我”和老公爽快地答应 · 林林嚷着要用爸爸最拿手的佳肴欢迎天天 · 全家别提多高兴了",
           "## 2. 天天到来之前，林林有什么变化？",
           "变得异常勤劳 · 屋子收拾得干干净净 · 东西摆放得整整齐齐 · 什么好事都想着天天",
           "## 3. 天天来了之后，两个孩子表现如何？",
           "早上不用叫就醒 · 上学不用接送 · 做作业不用督促 · 不打架，不闹别扭，关系融洽"],
    say=["Chúng ta cùng nhìn lại bố cục của cả bài khóa, theo các câu hỏi gợi ý trong bài tập năm của sách.",
         F(0, "Câu một: 天天要来，全家的态度怎么样？ Thiên Thiên sắp đến, thái độ của cả nhà thế nào?"),
         F(1, "Bố mẹ vui vẻ nhận lời ngay, Lâm Lâm đòi bố nấu món sở trường để đón bạn, cả nhà vui khỏi phải nói."),
         F(2, "Câu hai: 天天到来之前，林林有什么变化？ Trước khi Thiên Thiên đến, Lâm Lâm có thay đổi gì?"),
         F(3, "Cô bé trở nên chăm chỉ lạ thường, dọn nhà sạch sẽ, xếp đồ ngăn nắp, chuyện gì tốt cũng nghĩ đến bạn."),
         F(4, "Câu ba: 天天来了之后，两个孩子表现如何？ Sau khi Thiên Thiên đến, hai đứa trẻ thể hiện ra sao?"),
         F(5, "Sáng không cần gọi cũng dậy, đi học không cần đưa đón, làm bài không cần đốc thúc, không đánh nhau, không giận dỗi, rất hòa hợp.")])

add("bullets", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5) – phần 2", size=36,
    items=["## 4. 两个孩子做错了什么？父母怎样教育他们？",
           "一个说……，另一个说…… · “我”严肃地说：应该当面说 · 老公附和：要和睦相处",
           "## 5. 孩子的疑惑是什么？大人有什么做错了的地方？",
           "女儿反问：“你们不是也……吗？” · 两套标准：对自己宽容，对孩子严厉",
           "## 6. 这个故事告诉我们什么道理？",
           "想当好父母，首先要约束好自己的言行"],
    say=[F(0, "Câu bốn: 两个孩子做错了什么？父母怎样教育他们？ Hai đứa trẻ đã làm sai điều gì? Bố mẹ dạy chúng thế nào?"),
         F(1, "Hai đứa nói xấu bạn sau lưng. Mẹ nghiêm giọng dạy phải nói thẳng trước mặt, bố phụ họa rằng phải sống hòa thuận, bao dung."),
         F(2, "Câu năm: 孩子的疑惑是什么？大人有什么做错了的地方？ Đứa trẻ thắc mắc điều gì? Người lớn đã sai ở đâu?"),
         F(3, "Con gái hỏi vặn: chẳng phải bố mẹ cũng nhận xét bạn bè sau lưng sao? Hóa ra bố mẹ dùng hai tiêu chuẩn: dễ dãi với mình, nghiêm khắc với con."),
         F(4, "Câu sáu: 这个故事告诉我们什么道理？ Câu chuyện này cho ta bài học gì?"),
         F(5, "想当好父母，首先要约束好自己的言行。 Muốn làm cha mẹ tốt, trước hết phải giữ gìn lời nói và việc làm của chính mình. Bố cục này rất có ích cho bài tập viết ở cuối bài.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 巴不得", section="Ngữ pháp 注释", title="1. 巴不得 bābude – chỉ mong sao", size=40,
    items=["Động từ, nghĩa là mong mỏi tha thiết (迫切盼望) · dùng trong khẩu ngữ",
           "Cấu trúc: 巴不得 + động từ / mệnh đề · hoặc đứng cuối câu: ……，我巴不得呢！",
           "有个孩子和我们的独生女朝夕相处，我们巴不得呢！",
           "就快到春节了，在外地打工一整年的他巴不得马上回到老家和父母、孩子团聚。",
           "我巴不得他们能真的和好，从此以后和和睦睦过日子。"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là động từ 巴不得.",
         F(0, "巴不得 có nghĩa là mong mỏi một cách tha thiết, sách giải thích là 迫切盼望. Tiếng Việt dịch là chỉ mong sao, mong còn không được. Từ này dùng trong khẩu ngữ."),
         F(1, "Sau 巴不得 có thể là một động từ hoặc cả một mệnh đề. Nó cũng có thể đứng cuối câu, thường kèm trợ từ ngữ khí, như 我巴不得呢, tôi mong còn chẳng được ấy chứ."),
         F(2, "Ví dụ một, lấy từ bài khóa: 有个孩子和我们的独生女朝夕相处，我们巴不得呢！ Có một đứa trẻ sớm tối ở bên con gái một của chúng tôi, chúng tôi mong còn chẳng được ấy chứ!"),
         F(3, "Ví dụ hai: 就快到春节了，在外地打工一整年的他巴不得马上回到老家和父母、孩子团聚。 Sắp đến Tết rồi, anh ấy làm thuê xa nhà cả năm trời, chỉ mong sao được về quê đoàn tụ với bố mẹ, con cái ngay."),
         F(4, "Ví dụ ba: 我巴不得他们能真的和好，从此以后和和睦睦过日子。 Tôi chỉ mong họ thật sự làm lành, từ nay về sau sống hòa thuận với nhau."),
         "Mở rộng thêm: có một từ gần nghĩa là 恨不得, nghĩa là hận không thể, thường dùng cho điều khó thực hiện được. Còn 巴不得 thì điều mong muốn hoàn toàn có thể xảy ra."])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: viết lại câu với 巴不得", reveal=True, size=40,
    items=["(1) 他不来太好了，我就希望他不来呢。",
           "Đáp án: 他不来太好了，我巴不得他不来呢。",
           "(2) 有人请你玩儿你还不去？这样的好事我盼还盼不来呢。",
           "Đáp án: ……这样的好事我巴不得呢！",
           "(3) 我多么希望你来帮帮我呀，怎么会觉得你多事呢？",
           "Đáp án: 我巴不得你来帮帮我呢，怎么会觉得你多事呢？"],
    say=[F(0, "Luyện tập: dùng 巴不得 viết lại câu. Câu một: 他不来太好了，我就希望他不来呢。 Anh ta không đến thì tốt quá, tôi chỉ mong anh ta đừng đến. Các bạn hãy tạm dừng và thử viết lại."),
         F(1, "Đáp án: 他不来太好了，我巴不得他不来呢。 Thay 就希望 bằng 巴不得."),
         F(2, "Câu hai: 有人请你玩儿你还不去？这样的好事我盼还盼不来呢。 Có người mời đi chơi mà bạn còn không đi à? Chuyện tốt như vậy tôi mong còn chẳng được."),
         F(3, "Đáp án: 这样的好事我巴不得呢！ Ở đây 巴不得 đứng cuối câu, như trong bài khóa."),
         F(4, "Câu ba: 我多么希望你来帮帮我呀，怎么会觉得你多事呢？ Tôi mong bạn đến giúp tôi biết bao, sao lại thấy bạn lắm chuyện được?"),
         F(5, "Đáp án: 我巴不得你来帮帮我呢，怎么会觉得你多事呢？ 巴不得 thay cho 多么希望.")])

add("bullets", chapter="Ngữ pháp: 别提多……了", section="Ngữ pháp 注释", title="2. 别提多……了 – … khỏi phải nói", size=40,
    items=["Biểu thị mức độ rất cao, không cần nói chi tiết · giọng cường điệu, khẩu ngữ",
           "Cấu trúc: (Chủ ngữ) + 别提多 + tính từ / động từ tâm lý + 了",
           "这个人办事，别提多负责了。",
           "看到女儿对伙伴热情无私，我和老公别提多高兴了。",
           "为了帮我的忙，把他累成那样，弄得我心里别提多过意不去了。"],
    say=["Điểm ngữ pháp thứ hai là cấu trúc 别提多, rồi tính từ, rồi trợ từ cuối câu, ví dụ 别提多高兴了.",
         F(0, "Cấu trúc này biểu thị mức độ rất cao, cao đến mức không cần nói chi tiết nữa, mang giọng điệu cường điệu. Tiếng Việt dịch là: khỏi phải nói, hoặc không biết… đến nhường nào."),
         F(1, "Sau 别提多 là một tính từ, hoặc một động từ chỉ tâm lý như 高兴，生气，担心, và cuối câu luôn có trợ từ, như 别提多担心了."),
         F(2, "Ví dụ một: 这个人办事，别提多负责了。 Người này làm việc thì có trách nhiệm khỏi phải nói."),
         F(3, "Ví dụ hai, lấy từ bài khóa: 看到女儿对伙伴热情无私，我和老公别提多高兴了。 Thấy con gái nhiệt tình, không ích kỷ với bạn, tôi và chồng vui khỏi phải nói."),
         F(4, "Ví dụ ba: 为了帮我的忙，把他累成那样，弄得我心里别提多过意不去了。 Vì giúp tôi mà anh ấy mệt đến thế, khiến tôi áy náy vô cùng. 过意不去 nghĩa là áy náy, ngại trong lòng."),
         "Các bạn nhớ: đừng bỏ trợ từ ở cuối câu, và 别提 ở đây không có nghĩa là đừng nhắc đến, mà là nhiều đến mức không cần nói nữa."])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: viết lại câu với 别提多……了", reveal=True, size=40,
    items=["(1) 听说女儿把这么好的工作给辞了，妈妈气坏了。",
           "Đáp án: ……妈妈别提多生气了。",
           "(2) 看到他们两个相处得这么好，我高兴极了。",
           "Đáp án: ……我别提多高兴了。",
           "(3) 联欢会上，我们自编自演的节目特别特别受欢迎。",
           "Đáp án: ……我们自编自演的节目别提多受欢迎了。"],
    say=[F(0, "Luyện tập. Câu một: 听说女儿把这么好的工作给辞了，妈妈气坏了。 Nghe nói con gái bỏ một công việc tốt như vậy, mẹ tức lắm. Các bạn thử viết lại nhé."),
         F(1, "Đáp án: 妈妈别提多生气了。 Mẹ tức giận khỏi phải nói. Chú ý: 气坏了 chuyển thành 别提多生气了."),
         F(2, "Câu hai: 看到他们两个相处得这么好，我高兴极了。 Thấy hai người họ hòa thuận như vậy, tôi vui vô cùng."),
         F(3, "Đáp án: 我别提多高兴了。 Bỏ 极了, đưa 别提多 lên trước 高兴."),
         F(4, "Câu ba: 联欢会上，我们自编自演的节目特别特别受欢迎。 Trong buổi liên hoan, tiết mục do chúng tôi tự biên tự diễn được hoan nghênh cực kỳ."),
         F(5, "Đáp án: 我们自编自演的节目别提多受欢迎了。 Tiết mục được yêu thích khỏi phải nói.")])

add("bullets", chapter="Phong cách: văn viết – khẩu ngữ", section="Ngữ pháp 注释", title="3. Từ đồng nghĩa khác nhau về phong cách (语体)", size=36,
    items=["Cùng nghĩa, khác phong cách: từ trước thiên về văn viết, từ sau thường dùng trong khẩu ngữ",
           "将 – 把 · 道 – 说 · 便 – 就 · 即 – 就是 · 令 – 让 · 食 – 吃",
           "Chọn từ theo phong cách chung của bài để cả bài văn thống nhất",
           "(1) 天天还没来，林林就变得异常勤劳，将屋子收拾得干干净净……",
           "(2) 女儿却是一脸的疑惑，反问道：“你们不是也有时候说……吗？”",
           "(3) ……实行的是两套标准，那便是对自己宽容，对孩子严厉。"],
    say=["Điểm thứ ba trong phần chú thích là về phong cách diễn đạt: những từ đồng nghĩa nhưng khác nhau về ngữ thể, tiếng Trung gọi là 语体.",
         F(0, "Trong tiếng Trung, có những cặp từ nghĩa giống nhau, nhưng từ trước mang màu sắc văn viết, còn từ sau thường dùng trong khẩu ngữ."),
         F(1, "Ví dụ: 将屋子 và 把屋子; 反问道 và 反问说; 那便是 và 那就是; 即 và 就是; 令人感动 và 让人感动; 食用 và 吃. Từ đứng trước trong mỗi cặp dùng trong văn viết."),
         F(2, "Khi viết, chọn từ nào phải dựa vào phong cách ngôn ngữ của cả bài, để toàn bài thống nhất. Bài văn trang trọng mà xen từ quá khẩu ngữ, hoặc ngược lại, sẽ đọc rất lạc giọng."),
         F(3, "Ví dụ một, lấy từ bài khóa: 将屋子收拾得干干净净, dùng cách nói văn viết thay cho 把屋子."),
         F(4, "Ví dụ hai: 女儿却是一脸的疑惑，反问道, dùng 反问道 thay cho 反问说."),
         F(5, "Ví dụ ba: 那便是对自己宽容，对孩子严厉, dùng 那便是 thay cho 那就是. Bài khóa là văn tự sự, nên tác giả xen kẽ cả lời nói khẩu ngữ của nhân vật lẫn cách nói văn viết của người kể chuyện.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: tìm từ khẩu ngữ tương ứng", reveal=True, size=36,
    items=["(1) 在与林小雨的相处中，我发现她不仅爽快，还很健谈，跟谁都能滔滔不绝，聊起来没完。（与）",
           "Đáp án: 与 → 跟 / 和",
           "(2) 中国是世界上最早种茶、制茶、饮茶的国家，种茶的历史已有几千年了。（饮）",
           "Đáp án: 饮 → 喝（饮茶 → 喝茶）",
           "(3) 他在信中写道：“我不知道这本书是否能让你了解我及我生活的全部，我们努力吧。”（是否）",
           "Đáp án: 是否 → 是不是"],
    say=[F(0, "Luyện tập: viết từ khẩu ngữ tương ứng với từ được đánh dấu. Câu một: 在与林小雨的相处中，我发现她不仅爽快，还很健谈，跟谁都能滔滔不绝，聊起来没完。 Trong thời gian chơi với Lâm Tiểu Vũ, tôi thấy cô ấy không những thẳng thắn mà còn rất hoạt ngôn, nói chuyện với ai cũng thao thao bất tuyệt. Từ được đánh dấu nằm trong cụm 与林小雨."),
         F(1, "Đáp án: 与林小雨 là văn viết, khẩu ngữ nói là 跟林小雨 hoặc 和林小雨."),
         F(2, "Câu hai: 中国是世界上最早种茶、制茶、饮茶的国家，种茶的历史已有几千年了。 Trung Quốc là nước sớm nhất trên thế giới trồng chè, chế biến chè và uống trà; lịch sử trồng chè đã có mấy nghìn năm. Từ được đánh dấu nằm trong cụm 饮茶."),
         F(3, "Đáp án: 饮茶 là văn viết, khẩu ngữ nói là 喝茶."),
         F(4, "Câu ba: 他在信中写道：我不知道这本书是否能让你了解我及我生活的全部，我们努力吧。 Anh ấy viết trong thư: anh không biết cuốn sách này có giúp em hiểu được anh và toàn bộ cuộc sống của anh hay không, chúng ta cùng cố gắng nhé. Từ được đánh dấu là 是否."),
         F(5, "Đáp án: 是否 là văn viết, khẩu ngữ nói là 是不是. Ngoài ra, 写道 trong câu này cũng là cách nói văn viết, khẩu ngữ là 写着; còn 我及我生活的全部 nói theo khẩu ngữ là 我和我生活的全部.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 人家 – 别人", section="Phân biệt từ 词语辨析", title="Phân biệt 人家 và 别人 (1)",
    common="Giống nhau: đều là đại từ, chỉ người ngoài người nói và người nghe, không xác định. Ví dụ: 人家/别人都这么说，可是我不相信。",
    cols=[{"head": "人家",
           "lines": ["(1) Có thể chỉ xác định một người hoặc một nhóm người đã nhắc đến ở trước, gần bằng 他 / 他们",
                     "Đúng: 李阳天天帮我复习功课，我要是考不好，都对不起人家。（人家 = 李阳）"]},
          {"head": "别人",
           "lines": ["(1) Không có cách dùng này",
                     "别人 luôn chỉ người khác nói chung, không chỉ một người cụ thể đã nhắc ở trước"]}],
    say=["Tiếp theo là phần phân biệt từ: 人家 và 别人. Hai từ này đều có thể dịch là người khác, người ta, nên rất dễ nhầm.",
         "Điểm giống nhau: cả hai đều là đại từ, chỉ những người ngoài người nói và người nghe, không xác định là ai. Ví dụ: 人家都这么说，可是我不相信, hoặc 别人都这么说，可是我不相信, đều đúng. Người ta đều nói vậy, nhưng tôi không tin.",
         F(0, "Điểm khác thứ nhất: 人家 có thể chỉ xác định một người hay một nhóm người đã được nhắc đến ở phía trước, gần giống 他 hoặc 他们."),
         F(0, "Ví dụ: 李阳天天帮我复习功课，我要是考不好，都对不起人家。 Lý Dương ngày nào cũng giúp tôi ôn bài, nếu tôi thi không tốt thì thật có lỗi với cậu ấy. Ở đây 人家 chính là 李阳."),
         F(1, "Còn 别人 không có cách dùng này. 别人 luôn chỉ người khác nói chung, không thể thay cho một người cụ thể vừa nhắc đến.")])

add("compare", section="Phân biệt từ 词语辨析", title="Phân biệt 人家 và 别人 (2)",
    common="人家 còn có một cách dùng đặc biệt mà 别人 không có:",
    cols=[{"head": "人家",
           "lines": ["(2) Có thể chỉ chính người nói, gần bằng 我",
                     "Mang sắc thái thân mật, tinh nghịch, hay dùng khi con gái làm nũng",
                     "Đúng: 你跑慢点儿行不行？人家跟不上。（人家 = 我）"]},
          {"head": "别人",
           "lines": ["(2) Không có cách dùng này",
                     "Sai: 你跑慢点儿行不行？别人跟不上。（nếu muốn nói chính mình）"]}],
    say=[F(0, "Điểm khác thứ hai: 人家 còn có thể chỉ chính người nói, tức là bằng 我. Cách dùng này mang sắc thái thân mật, tinh nghịch, thường gặp khi các bạn gái làm nũng."),
         F(0, "Ví dụ: 你跑慢点儿行不行？人家跟不上。 Anh chạy chậm một chút được không? Người ta theo không kịp. Ở đây người ta chính là cô gái đang nói. Tiếng Việt cũng có cách nói y hệt, đúng không các bạn?"),
         F(1, "Còn 别人 không có cách dùng này. Nếu nói 别人跟不上, người nghe sẽ hiểu là một người khác theo không kịp, chứ không phải chính mình."),
         "Mẹo nhớ: 别人 lúc nào cũng là người khác. Còn 人家 thì linh hoạt hơn: có thể là người khác nói chung, là người vừa được nhắc đến, hoặc là chính mình."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: 人家 chỉ ai?", reveal=True, size=38,
    items=["(1) 我说了我的观点，可是人家都不同意。",
           "Đáp án: 别人 – người khác nói chung (sách đã làm mẫu).",
           "(2) 你老给小丽打电话，不知道人家喜欢不喜欢你啊！",
           "Đáp án: người đã nhắc ở trước – 人家 = 小丽.",
           "(3) 你把我的生日都忘了，人家能不生气吗？",
           "Đáp án: chính người nói – 人家 = 我.",
           "(4) 你昨天借了小王100块钱，今天别忘了还给人家！",
           "Đáp án: người đã nhắc ở trước – 人家 = 小王."],
    say=[F(0, "Bây giờ chúng ta làm thử: trong mỗi câu, 人家 chỉ ai? Là người khác nói chung, là người đã nhắc ở trước, hay là chính người nói? Câu một: 我说了我的观点，可是人家都不同意。 Tôi đã nói quan điểm của mình, nhưng người ta đều không đồng ý."),
         F(1, "Đáp án: ở đây 人家 là người khác nói chung, giống 别人. Câu này sách đã làm mẫu."),
         F(2, "Câu hai: 你老给小丽打电话，不知道人家喜欢不喜欢你啊！ Cậu cứ gọi điện cho Tiểu Lệ hoài, chẳng biết người ta có thích cậu không nữa!"),
         F(3, "Đáp án: 人家 là người đã nhắc ở trước, chính là 小丽."),
         F(4, "Câu ba: 你把我的生日都忘了，人家能不生气吗？ Anh quên cả sinh nhật em, người ta không giận sao được?"),
         F(5, "Đáp án: 人家 là chính người nói, tức là 我. Câu này mang giọng làm nũng."),
         F(6, "Câu bốn: 你昨天借了小王一百块钱，今天别忘了还给人家！ Hôm qua cậu mượn Tiểu Vương một trăm tệ, hôm nay đừng quên trả cho người ta nhé!"),
         F(7, "Đáp án: 人家 là người đã nhắc ở trước, chính là 小王.")])

# ======================= MỞ RỘNG =======================
add("bullets", chapter="Mở rộng: câu sai do dùng từ", section="Mở rộng 扩展", title="Câu sai: dùng từ không đúng (词语误用 一) – phần 1", size=36,
    items=["Từ gần nghĩa thường khác nhau ở: phạm vi rộng hẹp · mức độ nặng nhẹ · trọng điểm nghĩa · sắc thái khen chê",
           "(1) *在公益行为中，受助者固然得益，助人者也获得了精神的满足。",
           "Sửa: 行为 → 行动 (行为 thường là của cá nhân, không phải tập thể)",
           "(2) *他的毕业论文被评为优秀论文，爸妈都为儿子的成就高兴。",
           "Sửa: 成就 → 成绩 (成就 dùng cho thành quả lớn trong sự nghiệp)",
           "(3) *飞机还没落地，接机大厅便站满了数百名前来迎接的人群。",
           "Sửa: 人群 → 人 (人群 là danh từ tập thể, không đi với 数百名)"],
    say=["Bây giờ chúng ta sang phần mở rộng: các loại câu sai do dùng từ không đúng. Đây là dạng bài rất hay gặp trong phần đọc của đề thi HSK 6.",
         F(0, "Trong tiếng Trung có những từ nghĩa gần nhau, chỉ khác nhau một chút: phạm vi rộng hay hẹp, mức độ nặng hay nhẹ, trọng điểm nghĩa khác nhau, hoặc sắc thái khen chê khác nhau. Chỉ cần không cẩn thận là dùng sai ngay."),
         F(1, "Câu sai thứ nhất: 在公益行为中，受助者固然得益，助人者也获得了精神的满足。 Trong hoạt động công ích, người được giúp đương nhiên có lợi, người giúp cũng có được sự thỏa mãn về tinh thần."),
         F(2, "Lỗi về phạm vi nghĩa. 行为 là hành vi, thường là của một cá nhân. Ở đây là hoạt động của tập thể, nên phải sửa thành 行动."),
         F(3, "Câu sai thứ hai: 他的毕业论文被评为优秀论文，爸妈都为儿子的成就高兴。 Luận văn tốt nghiệp của anh ấy được xếp loại xuất sắc, bố mẹ đều mừng cho thành tích của con."),
         F(4, "Lỗi về mức độ nặng nhẹ. 成就 là thành tựu, dùng cho thành quả lớn trong sự nghiệp. Một luận văn tốt nghiệp chỉ nên gọi là 成绩."),
         F(5, "Câu sai thứ ba: 飞机还没落地，接机大厅便站满了数百名前来迎接的人群。 Máy bay còn chưa hạ cánh, sảnh đón đã đứng chật mấy trăm người đến đón."),
         F(6, "Lỗi dùng danh từ tập thể. 人群 là đám đông, một danh từ tập thể, không thể đi với số lượng 数百名. Phải sửa 人群 thành 人.")])

add("bullets", section="Mở rộng 扩展", title="Câu sai: dùng từ không đúng (词语误用 一) – phần 2", size=36,
    items=["(4) *网络的隐蔽性，使人在交往中减少了顾虑，就算是初次在聊天室搭话，也可以做到无所拘谨。",
           "Sửa: 拘谨 → 拘束 (拘谨 thiên về quá thận trọng trong lời nói, hành động; 无所拘束 = không bị gò bó)",
           "(5) *我们的晚会开得可喧闹了，大家玩儿得高兴极了，直到凌晨才散。",
           "Sửa: 喧闹 → 热闹 (喧闹 mang nghĩa xấu: ồn ào khó chịu)"],
    say=[F(0, "Câu sai thứ tư: 网络的隐蔽性，使人在交往中减少了顾虑，就算是初次在聊天室搭话，也可以做到无所拘谨。 Tính ẩn danh của mạng khiến người ta bớt e ngại khi giao tiếp, dù là lần đầu bắt chuyện trong phòng chat cũng có thể thoải mái tự nhiên."),
         F(1, "Lỗi về trọng điểm nghĩa. 拘谨 thiên về sự quá dè dặt, thận trọng trong lời nói và hành động. Ở đây muốn nói không bị gò bó, nên phải dùng 拘束: 无所拘束."),
         F(2, "Câu sai thứ năm: 我们的晚会开得可喧闹了，大家玩儿得高兴极了，直到凌晨才散。 Buổi liên hoan của chúng tôi rất náo nhiệt, mọi người chơi vui vô cùng, đến tận rạng sáng mới tan."),
         F(3, "Lỗi về sắc thái khen chê. 喧闹 là ồn ào, mang nghĩa xấu, gây khó chịu. Buổi liên hoan vui vẻ phải dùng từ mang nghĩa tốt là 热闹.")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chỉ ra lỗi và sửa lại (1)", reveal=True, size=36,
    items=["(1) 看到这样的事情，我惊讶得目瞪口呆，不信任这样离奇的事竟然真的在我眼前发生了。",
           "Đáp án: 信任 → 相信 (信任 dùng cho người; tin một sự việc là thật → 相信)",
           "(2) 这次比赛暴露出很多思维敏捷、口才出众、演讲能力强的学生。",
           "Đáp án: 暴露 → 涌现 (暴露 mang nghĩa xấu: lộ ra điều không hay)",
           "(3) 他们觉得你刚工作，年龄又小，实际上你聪明，能力也很强，你不能太衰弱了，要做生活的强者。",
           "Đáp án: 衰弱 → 软弱 (衰弱 nói về cơ thể suy yếu; 软弱 là tính cách yếu đuối)"],
    say=[F(0, "Luyện tập: chỉ ra lỗi trong câu và sửa lại. Câu một: 看到这样的事情，我惊讶得目瞪口呆，不信任这样离奇的事竟然真的在我眼前发生了。 Thấy chuyện như vậy, tôi kinh ngạc đến há hốc mồm, không tin chuyện kỳ lạ như thế lại thật sự xảy ra trước mắt mình. Các bạn tạm dừng và tìm lỗi nhé."),
         F(1, "Đáp án: 信任 là tín nhiệm, tin tưởng một người hay một tổ chức. Còn tin rằng một sự việc là có thật thì phải dùng 相信. Sửa thành 不相信."),
         F(2, "Câu hai: 这次比赛暴露出很多思维敏捷、口才出众、演讲能力强的学生。 Cuộc thi lần này làm xuất hiện nhiều học sinh tư duy nhanh nhạy, ăn nói xuất sắc, giỏi diễn thuyết."),
         F(3, "Đáp án: 暴露 là bộc lộ, phơi bày, thường dùng cho khuyết điểm, bí mật, tức là nghĩa xấu. Ở đây đang khen, nên phải dùng 涌现, nghĩa là xuất hiện nhiều, nổi lên."),
         F(4, "Câu ba: 他们觉得你刚工作，年龄又小，实际上你聪明，能力也很强，你不能太衰弱了，要做生活的强者。 Họ nghĩ cậu mới đi làm, tuổi lại nhỏ, nhưng thực ra cậu thông minh, năng lực cũng mạnh, cậu không được quá yếu đuối, phải làm người mạnh mẽ trong cuộc sống."),
         F(5, "Đáp án: 衰弱 là suy nhược, nói về cơ thể. Ở đây nói về tính cách, nên phải dùng 软弱, yếu đuối, nhu nhược.")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chỉ ra lỗi và sửa lại (2)", reveal=True, size=36,
    items=["(4) 越是到了冬天，我越爱迟到，这星期我迟到了好几次，老师批判了我，弄得我好没面子。",
           "Đáp án: 批判 → 批评 (批判 quá nặng, dùng cho tư tưởng, sai lầm nghiêm trọng)",
           "(5) 每到上下班的时候，马路上一辆辆的车辆排成长龙，把马路堵得水泄不通。",
           "Đáp án: 车辆 → 车 (车辆 là danh từ tập thể, không đi với 一辆辆)"],
    say=[F(0, "Câu bốn: 越是到了冬天，我越爱迟到，这星期我迟到了好几次，老师批判了我，弄得我好没面子。 Càng đến mùa đông tôi càng hay đi muộn, tuần này tôi đã muộn mấy lần, bị thầy phê bình, thật là mất mặt."),
         F(1, "Đáp án: 批判 là phê phán, rất nặng, dùng cho tư tưởng sai lầm hay hành vi nghiêm trọng. Đi học muộn chỉ cần 批评, phê bình. Lỗi về mức độ nặng nhẹ."),
         F(2, "Câu năm: 每到上下班的时候，马路上一辆辆的车辆排成长龙，把马路堵得水泄不通。 Cứ đến giờ đi làm và tan tầm, xe cộ trên đường xếp thành hàng dài, làm đường tắc nghẽn không lối thoát."),
         F(3, "Đáp án: 车辆 là xe cộ nói chung, một danh từ tập thể, giống như 人群 lúc nãy, không thể đi với 一辆辆. Phải sửa thành 一辆辆的车.")])

add("bullets", section="Mở rộng 扩展", title="Từ vựng: làm quen các cách kết hợp (1)", size=38,
    items=["留恋 lưu luyến: 十分留恋 · 留恋故土",
           "开朗 cởi mở, vui tươi: 性格开朗 · 心情开朗",
           "闲话 chuyện phiếm; lời ra tiếng vào: 说闲话",
           "风趣 dí dỏm, hài hước: 幽默风趣",
           "恩怨 ân oán: 个人恩怨 · 恩怨情仇",
           "娇气 yếu ớt, õng ẹo: 太娇气了"],
    say=["Phần mở rộng thứ hai: làm quen với cách kết hợp của một số từ. Học từ theo cụm sẽ giúp các bạn dùng từ tự nhiên hơn.",
         F(0, "留恋, lưu luyến. Kết hợp: 十分留恋，留恋故土. Ví dụ: 飞机起飞了，对这片土地，我心中充满留恋。 Máy bay cất cánh, lòng tôi tràn đầy lưu luyến với mảnh đất này."),
         F(1, "开朗, cởi mở, vui tươi. Kết hợp: 性格开朗，心情开朗. Ví dụ: 她开朗乐观，热爱生活。 Cô ấy cởi mở, lạc quan, yêu đời."),
         F(2, "闲话, chuyện phiếm, cũng có nghĩa là lời ra tiếng vào. Kết hợp: 说闲话. Ví dụ: 大家在院里聊了会儿闲话，就回家了。 Mọi người tán gẫu một lúc trong sân rồi về nhà."),
         F(3, "风趣, dí dỏm. Kết hợp: 幽默风趣. Ví dụ: 王教授讲课十分风趣，选他的课的人特别多。 Giáo sư Vương giảng bài rất dí dỏm, người đăng ký lớp của ông rất đông."),
         F(4, "恩怨, ân oán. Kết hợp: 个人恩怨，恩怨情仇. Ví dụ: 我们决定，为了工作，忘掉多年的恩怨。 Chúng tôi quyết định, vì công việc, quên đi ân oán bao năm."),
         F(5, "娇气, yếu ớt, õng ẹo, không chịu được vất vả. Kết hợp: 太娇气了. Ví dụ: 她个子瘦小，却不娇气。 Cô ấy dáng người nhỏ bé nhưng không hề yếu ớt.")])

add("bullets", section="Mở rộng 扩展", title="Từ vựng: làm quen các cách kết hợp (2)", size=38,
    items=["伶俐 lanh lợi: 口齿伶俐 · 聪明伶俐",
           "挑剔 kén chọn, bới lông tìm vết: 过分挑剔",
           "挑拨 khiêu khích, xúi giục: 挑拨离间",
           "气质 khí chất, phong thái: 有气质 · 气质优雅",
           "容貌 dung mạo: 容貌秀美",
           "福气 phúc, phước: 有福气 · 福气大"],
    say=[F(0, "伶俐, lanh lợi. Kết hợp: 口齿伶俐，聪明伶俐. Ví dụ: 他们有个聪明伶俐的好儿子。 Họ có một cậu con trai thông minh lanh lợi."),
         F(1, "挑剔, kén chọn, bới lông tìm vết. Kết hợp: 过分挑剔. Ví dụ: 她把自己打扮得很美，美得无可挑剔。 Cô ấy trang điểm rất đẹp, đẹp đến mức không chê vào đâu được."),
         F(2, "挑拨, xúi giục, gây chia rẽ. Kết hợp: 挑拨离间, châm ngòi ly gián. Ví dụ: 没有人能够挑拨我们之间的关系。 Không ai có thể chia rẽ quan hệ giữa chúng ta."),
         F(3, "气质, khí chất, phong thái. Kết hợp: 有气质，气质优雅. Ví dụ: 他变得更英俊，也更有气质了。 Anh ấy trở nên đẹp trai hơn, cũng có khí chất hơn."),
         F(4, "容貌, dung mạo. Kết hợp: 容貌秀美. Ví dụ: 她不但有出众的容貌，而且心地善良。 Cô ấy không những có dung mạo xuất chúng mà còn có tấm lòng lương thiện."),
         F(5, "福气, phúc. Kết hợp: 有福气，福气大. Ví dụ: 一生没有遇到战争就是福气。 Cả đời không gặp chiến tranh đã là một phúc lớn.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Viết thêm từ theo chữ được đánh dấu", reveal=True, size=36,
    items=["Mẫu: 反问 → 询问 · 提问 · 疑问 · 问题",
           "(1) 爽快",
           "Đáp án gợi ý: 愉快 · 痛快 · 凉快 · 赶快",
           "(2) 打架",
           "Đáp án gợi ý: 吵架 · 劝架 · 书架 · 衣架",
           "(3) 亲密",
           "Đáp án gợi ý: 秘密 · 保密 · 紧密 · 严密",
           "(4) 反驳",
           "Đáp án gợi ý: 辩驳 · 批驳 · 驳斥 · 驳回"],
    say=[F(0, "Phần luyện tập. Bài tập một: theo mẫu, viết thêm các từ có chứa chữ được đánh dấu, tức là chữ thứ hai của mỗi từ. Mẫu: 反问, có 询问，提问，疑问，问题. Tức là hỏi thăm, đặt câu hỏi, nghi vấn, và vấn đề."),
         F(1, "Từ thứ nhất: 爽快. Các bạn tạm dừng và thử viết các từ có chữ 快 nhé."),
         F(2, "Đáp án gợi ý: 愉快，痛快，凉快，赶快. Tức là vui vẻ, thỏa thích, mát mẻ, và mau lên."),
         F(3, "Từ thứ hai: 打架. Hãy viết các từ có chữ 架."),
         F(4, "Đáp án gợi ý: 吵架，劝架，书架，衣架. Tức là cãi nhau, can ngăn đánh nhau, giá sách, và mắc áo."),
         F(5, "Từ thứ ba: 亲密. Hãy viết các từ có chữ 密."),
         F(6, "Đáp án gợi ý: 秘密，保密，紧密，严密. Tức là bí mật, giữ bí mật, chặt chẽ, và nghiêm mật."),
         F(7, "Từ thứ tư: 反驳. Hãy viết các từ có chữ 驳."),
         F(8, "Đáp án gợi ý: 辩驳，批驳，驳斥，驳回. Tức là biện bác, phê phán bác bỏ, bác bỏ mạnh mẽ, và bác đơn, bác yêu cầu.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (1)", reveal=True, size=38,
    items=["(1) 听到这个消息，大家非常兴奋，忍不住欢呼起来。（异常）",
           "Đáp án: 听到这个消息，大家异常兴奋，忍不住欢呼起来。",
           "(2) 他做得最好吃的菜是西红柿炒鸡蛋。（拿手）",
           "Đáp án: 他最拿手的菜是西红柿炒鸡蛋。/ 西红柿炒鸡蛋是他的拿手菜。",
           "(3) 我的工作就是不断提醒食品厂加强卫生管理。（督促）",
           "Đáp án: 我的工作就是不断督促食品厂加强卫生管理。"],
    say=[F(0, "Bài tập hai: dùng từ hoặc cấu trúc cho sẵn để viết lại câu. Câu một, dùng 异常: 听到这个消息，大家非常兴奋，忍不住欢呼起来。 Nghe tin này, mọi người vô cùng phấn khởi, không kìm được reo hò."),
         F(1, "Đáp án: thay 非常 bằng 异常: 大家异常兴奋. Đây chính là cách dùng 异常 làm phó từ, như trong bài khóa."),
         F(2, "Câu hai, dùng 拿手: 他做得最好吃的菜是西红柿炒鸡蛋。 Món anh ấy nấu ngon nhất là trứng xào cà chua."),
         F(3, "Đáp án: 他最拿手的菜是西红柿炒鸡蛋, hoặc 西红柿炒鸡蛋是他的拿手菜. Món tủ của anh ấy là trứng xào cà chua."),
         F(4, "Câu ba, dùng 督促: 我的工作就是不断提醒食品厂加强卫生管理。 Công việc của tôi là liên tục nhắc nhở nhà máy thực phẩm tăng cường quản lý vệ sinh."),
         F(5, "Đáp án: thay 提醒 bằng 督促: 不断督促食品厂加强卫生管理. Đôn đốc mạnh hơn nhắc nhở, vì có cả ý giám sát.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (2)", reveal=True, size=38,
    items=["(4) 这个老师很严格，谁不做作业都不行。（严厉）",
           "Đáp án: 这个老师很严厉，谁不做作业都不行。",
           "(5) 我非常希望能马上回家见到妈妈。（巴不得）",
           "Đáp án: 我巴不得马上回家见到妈妈。",
           "(6) 这件事情太复杂了，我一个人根本处理不了。（别提多……了）",
           "Đáp án: 这件事情别提多复杂了，我一个人根本处理不了。"],
    say=[F(0, "Câu bốn, dùng 严厉: 这个老师很严格，谁不做作业都不行。 Thầy giáo này rất nghiêm, ai không làm bài tập cũng không được."),
         F(1, "Đáp án: 这个老师很严厉. Ở đây nói về thái độ nghiêm khắc của thầy, nên dùng 严厉 rất hợp."),
         F(2, "Câu năm, dùng 巴不得: 我非常希望能马上回家见到妈妈。 Tôi rất mong được về nhà gặp mẹ ngay."),
         F(3, "Đáp án: 我巴不得马上回家见到妈妈。 Tôi chỉ mong sao được về nhà gặp mẹ ngay."),
         F(4, "Câu sáu, dùng cấu trúc 别提多: 这件事情太复杂了，我一个人根本处理不了。 Việc này phức tạp quá, một mình tôi không tài nào xử lý được."),
         F(5, "Đáp án: 这件事情别提多复杂了，我一个人根本处理不了。 Việc này phức tạp khỏi phải nói.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (1)", reveal=True, size=36,
    items=["Từ cho sẵn: 和睦 · 绅士 · 爽快 · 宽容 · 十足",
           "我老公是个热心人，别人有事需要帮忙时，他总是____地答应；我老公也很____，能原谅伤害过他的人，几乎跟所有的人都能____相处；我老公还很____，不管是挤汽车，还是上电梯，都坚持女士优先，风度____，我身边的朋友都羡慕我找了个好老公。",
           "Đáp án: 爽快 · 宽容 · 和睦 · 绅士 · 十足"],
    say=[F(0, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn thứ nhất có năm từ: 和睦，绅士，爽快，宽容，十足."),
         F(1, "Đoạn văn kể về một người chồng: anh ấy là người nhiệt tình, ai cần giúp là anh nhận lời ngay; anh rộng lượng, tha thứ cho cả người từng làm hại mình, sống hòa thuận với hầu hết mọi người; anh còn rất lịch thiệp, chen xe buýt hay vào thang máy đều nhường phụ nữ trước. Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 他总是爽快地答应；我老公也很宽容；几乎跟所有的人都能和睦相处；我老公还很绅士；风度十足。 Các bạn để ý các cụm cố định: 爽快地答应，和睦相处，风度十足, đều có trong bài khóa.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (2)", reveal=True, size=36,
    items=["Từ cho sẵn: 别扭 · 亲密 · 嘲笑 · 当面 · 反问",
           "我和小丽关系很融洽，从来没闹过____。可突然有一天，我听说小丽在背后____我长得又胖又丑，我非常吃惊，马上要找她____问个究竟。小丽听了我的话后，笑了，她____道：“你觉得我会说那样的话吗？一定是有人嫉妒我们关系好，故意那么说的。”我的疑惑没有了，我们仍然是____的朋友。",
           "Đáp án: 别扭 · 嘲笑 · 当面 · 反问 · 亲密"],
    say=[F(0, "Đoạn thứ hai có năm từ: 别扭，亲密，嘲笑，当面，反问."),
         F(1, "Đoạn văn kể: tôi và Tiểu Lệ rất thân, chưa bao giờ giận nhau. Một hôm, tôi nghe nói Tiểu Lệ chê tôi vừa béo vừa xấu sau lưng, liền muốn gặp cô ấy hỏi cho ra lẽ. Tiểu Lệ cười, hỏi lại tôi, và hai đứa vẫn là bạn thân. Các bạn thử điền nhé."),
         F(2, "Đáp án: 从来没闹过别扭；小丽在背后嘲笑我；马上要找她当面问个究竟；她反问道；我们仍然是亲密的朋友。 Chú ý cặp 背后 và 当面 lại xuất hiện, giống hệt bài khóa.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 1", size=36,
    items=["Từ vựng trọng tâm: 爽快 · 巴不得 · 异常 · 风度 · 融洽 · 当面 · 附和 · 意识 · 实行 · 约束",
           "Ngữ pháp: 巴不得 (chỉ mong sao) · 别提多……了 (… khỏi phải nói)",
           "Phong cách: 将/把 · 道/说 · 便/就 · 即/就是 · 令/让 · 食/吃 – văn viết / khẩu ngữ",
           "Phân biệt: 人家 (có thể chỉ người đã nhắc, hoặc chính mình) ≠ 别人 (chỉ người khác)",
           "Mở rộng: câu sai do dùng từ – phạm vi, mức độ, trọng điểm, sắc thái khen chê",
           "## Bài tập về nhà",
           "Dựa vào bố cục bài tập 5, rút gọn bài khóa thành đoạn văn khoảng 300 chữ",
           "Làm bài tập 4: đặt câu theo mẫu 一个说……，另一个说…… và 人们常说……，这话确实不假，可如果……"],
    say=["Chúng ta cùng tổng kết bài một.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 爽快，巴不得，异常，风度，融洽，当面，附和，意识，实行，约束. Nhất là những từ Hán Việt dễ nhầm như 爽快，异常，风度，实行."),
         F(1, "Về ngữ pháp: 巴不得 nghĩa là chỉ mong sao, dùng trong khẩu ngữ. 别提多高兴了 nghĩa là vui khỏi phải nói, đừng quên trợ từ ở cuối câu."),
         F(2, "Về phong cách: các cặp như 将屋子 và 把屋子, 反问道 và 反问说, 那便是 và 那就是. Từ trước dùng trong văn viết, từ sau dùng trong khẩu ngữ."),
         F(3, "Về phân biệt từ: 人家 có thể chỉ người vừa nhắc đến, hoặc chính người nói; còn 别人 lúc nào cũng là người khác."),
         F(4, "Về phần mở rộng: khi dùng từ gần nghĩa, phải chú ý phạm vi, mức độ, trọng điểm nghĩa, và sắc thái khen chê."),
         F(6, "Bài tập về nhà thứ nhất: sách viết rằng, bài khóa qua một chuyện nhỏ trong gia đình cho ta thấy, cha mẹ là người thầy vỡ lòng của con, nhưng đôi khi con cũng là thầy của cha mẹ. Muốn làm cha mẹ tốt, trước hết phải giữ gìn lời nói và việc làm của mình. Các bạn hãy dựa vào bố cục sáu câu hỏi trong bài tập năm, rút gọn bài khóa thành một đoạn văn khoảng ba trăm chữ."),
         F(7, "Bài tập thứ hai: đặt câu theo hai mẫu trong bài tập bốn. Mẫu một: 刚一下课，他们就争论起来，一个说……，另一个说…… Mẫu hai: 人们常说有钱就有幸福，这话确实不假，可如果…… Các bạn hãy tự hoàn thành nhé."),
         "Cảm ơn các bạn đã theo dõi bài giảng đầu tiên của khóa HSK 6. Hẹn gặp lại các bạn ở bài hai: 父母之爱, Tình yêu của ba mẹ. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Thượng) – Bài 1: 孩子给我们的启示 (Điều con trẻ dạy chúng ta)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"朝夕": "招夕",          # zhāoxī, tránh đọc cháo
                    "相处": "相楚",          # xiāngchǔ, tránh đọc chù
                    "附和": "附贺",          # fùhè, tránh đọc hé
                    "嚷": "壤",              # rǎng (chỉ có âm này trong bài, không dùng 嚷嚷)
                    "任": "认",              # rèn (lượng từ 第一任, tránh đọc Rén)
                    "还给人家": "环给人家",  # huán, tránh đọc hái
                    "为儿子": "位儿子",      # wèi
                    "评为": "评维",          # píngwéi
                    "数百名": "树百名",      # shù, tránh đọc shǔ
                    "少女": "绍女",          # shàonǚ, tránh đọc shǎo
                    "种茶": "众茶",          # zhòng chá (trồng chè), tránh đọc zhǒng
                    "离间": "离建",          # líjiàn
                    "挑拨": "窕拨"},         # tiǎobō, tránh đọc tiāo
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai01.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
