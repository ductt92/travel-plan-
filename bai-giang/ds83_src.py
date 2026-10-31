#!/usr/bin/env python3
"""Kịch bản bài giảng 顶石中文 – Bài 8.3 «善终也是一种权利». Chạy để sinh ds83.json."""
import json
import os

TAG = "顶石中文 · Bài 8.3 · 善终也是一种权利"
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
    zh="善终也是一种权利", py="Shànzhōng yě shì yì zhǒng quánlì",
    vi="Bài 8.3: Ra đi thanh thản cũng là một quyền",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng giáo trình 顶石中文, Đỉnh cao tiếng Trung.",
         {"t": "Hôm nay chúng ta học bài thứ ba của Đơn vị tám, chủ đề Pháp luật: bài tám chấm ba, 善终也是一种权利。 Nghĩa là: Ra đi thanh thản cũng là một quyền.",
          "cap": "Hôm nay chúng ta học bài thứ ba của Đơn vị 8, chủ đề Pháp luật: bài 8.3, 善终也是一种权利。 Nghĩa là: Ra đi thanh thản cũng là một quyền."},
         "Đây là bài cuối cùng của Đơn vị tám, và cũng là bài cuối cùng của cả giáo trình 顶石中文. Bài khóa là một bài bình luận trên báo Nhân Dân, bàn về một chủ đề rất nghiêm túc: khi bệnh không còn chữa được, người bệnh có quyền tự quyết định cách mình ra đi hay không. Tác giả kể chuyện nhà văn Quỳnh Dao, nhà văn Ba Kim, và giới thiệu khái niệm 尊严死, chết có tôn nghiêm.",
         "Chủ đề này gắn liền với chữ hiếu, với tình thân trong gia đình, nên cũng rất gần gũi với người Việt. Cuối bài, chúng ta sẽ có một chương ôn tập toàn bộ Đơn vị tám."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài bình luận về “善终” và “尊严死”: quyền tự chủ của người bệnh ở cuối đời",
           "Nắm vững 44 từ mới, kèm âm Hán Việt và ví dụ",
           "7 mẫu câu: 谓之 · 视……为 · 整整 · 巴不得 · 我的……我做主 · 把……作为首选 · 与……共存",
           "6 kết hợp từ (引发 · 勉强 · 挽救 · 履行 · 免除 · 体面) và 6 thành ngữ",
           "Luyện tập theo sách; liên hệ Việt Nam; ôn tập Đơn vị 8 (学以致用)"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu bài bình luận về 善终 và 尊严死: vì sao tác giả cho rằng ra đi thanh thản cũng là một quyền, và pháp luật đã bảo vệ quyền này như thế nào."),
         F(1, "Thứ hai, nắm vững bốn mươi bốn từ mới, nhiều từ thuộc lĩnh vực y tế và pháp luật. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt và đưa ví dụ."),
         F(2, "Thứ ba, học bảy mẫu câu trọng điểm, như 谓之，视为，巴不得，我的我做主, và 与共存."),
         F(3, "Thứ tư, học sáu kết hợp từ và sáu thành ngữ, như 寿终正寝，无疾而终，痛不欲生，生不如死."),
         F(4, "Thứ năm, làm bài luyện tập của sách, liên hệ với Việt Nam, và ôn tập cả Đơn vị tám qua phần 学以致用 của sách."),
         "Chủ đề hôm nay có phần nặng nề, nhưng rất đáng suy ngẫm. Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 课前思考", title="Câu hỏi trước bài học 课前思考", reveal=True, size=35,
    items=["(1) 你们国家基础教育中有关于生命教育的内容吗？",
           "Đáp án gợi ý: 有一些，比如生物课和公民课会讲到珍爱生命，但是关于死亡的教育还比较少。",
           "(2) 你怎么看“安乐死”？",
           "Đáp án gợi ý: 我觉得安乐死是一个很复杂的问题，既要尊重病人的选择，也要有严格的法律规定，防止被滥用。",
           "(3) 谁有权决定自己生命的长度？",
           "Đáp án gợi ý: 我认为每个人都有权决定自己的生命，但是在做决定之前，应该和家人、医生充分沟通。"],
    say=["Chúng ta bắt đầu bằng ba câu hỏi trước bài học, 课前思考. Thầy đọc câu hỏi, các bạn tạm dừng để tự trả lời bằng tiếng Trung, rồi nghe câu trả lời gợi ý nhé.",
         F(0, "Câu một: 你们国家基础教育中有关于生命教育的内容吗？ Trong giáo dục phổ thông ở nước bạn có nội dung giáo dục về sự sống không? 生命教育 là giáo dục về sự sống và cái chết."),
         F(1, "Gợi ý: 有一些，比如生物课和公民课会讲到珍爱生命，但是关于死亡的教育还比较少。 Có một ít, ví dụ môn Sinh học và môn Giáo dục công dân có nói về việc trân trọng sự sống, nhưng giáo dục về cái chết thì còn khá ít."),
         F(2, "Câu hai: 你怎么看安乐死？ Bạn nhìn nhận thế nào về an tử? 安乐死 là an tử, cái chết êm ái."),
         F(3, "Gợi ý: 我觉得安乐死是一个很复杂的问题，既要尊重病人的选择，也要有严格的法律规定，防止被滥用。 Tôi thấy an tử là vấn đề rất phức tạp, vừa phải tôn trọng lựa chọn của người bệnh, vừa phải có quy định pháp luật nghiêm ngặt để tránh bị lạm dụng."),
         F(4, "Câu ba: 谁有权决定自己生命的长度？ Ai có quyền quyết định độ dài sự sống của mình?"),
         F(5, "Gợi ý: 我认为每个人都有权决定自己的生命，但是在做决定之前，应该和家人、医生充分沟通。 Tôi cho rằng mỗi người đều có quyền quyết định sự sống của mình, nhưng trước khi quyết định nên trao đổi kỹ với gia đình và bác sĩ.")])

add("bullets", section="Khởi động 课前思考", title="Khởi động: từ ngữ y tế về cuối đời", size=34,
    items=["抢救 / 急救 cấp cứu · ICU (重症监护室) phòng hồi sức tích cực · 呼吸机 máy thở · 心肺复苏 hồi sức tim phổi",
           "生命支持系统 hệ thống duy trì sự sống · 植物人 người sống thực vật · 绝症 bệnh nan y",
           "安乐死 an tử: chủ động dùng thuốc để người bệnh chết không đau đớn",
           "尊严死 chết có tôn nghiêm: không cấp cứu, không dùng máy duy trì sự sống, để cái chết đến tự nhiên",
           "临终关怀 · 安宁疗护 · 缓和医疗 chăm sóc cuối đời, chăm sóc giảm nhẹ"],
    say=["Trước khi vào bài, chúng ta làm quen với một số từ ngữ y tế liên quan đến giai đoạn cuối đời. Có hiểu những khái niệm này thì mới đọc được bài khóa.",
         F(0, "抢救 và 急救 đều là cấp cứu. ICU, tiếng Trung là 重症监护室, là phòng hồi sức tích cực. 呼吸机 là máy thở; 心肺复苏 là hồi sức tim phổi, ấn tim, thổi ngạt."),
         F(1, "生命支持系统 là hệ thống duy trì sự sống. 植物人 là người sống thực vật. 绝症 là bệnh nan y, bệnh không chữa được."),
         F(2, "Hai khái niệm quan trọng nhất của bài: 安乐死, an tử, là chủ động dùng thuốc để người bệnh vô phương cứu chữa ra đi không đau đớn."),
         F(3, "Còn 尊严死, chết có tôn nghiêm, thì khác: không chủ động làm gì để kết thúc sự sống, mà chỉ không cấp cứu, không dùng máy móc kéo dài sự sống, để cái chết đến một cách tự nhiên. Bài khóa nhấn mạnh sự khác biệt này."),
         F(4, "Cuối cùng là 临终关怀, 安宁疗护, 缓和医疗, đều chỉ chăm sóc cuối đời, chăm sóc giảm nhẹ: giảm đau, giúp người bệnh thoải mái về thể chất và tinh thần trong những ngày cuối.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("善终", "shànzhōng", "thiện chung", "động từ", "chết già yên lành, ra đi thanh thản", "爷爷九十多岁无疾而终，也算是善终了。", "Ông nội ngoài chín mươi tuổi mới ra đi vì tuổi già, cũng coi như được chết yên lành.",
     "Động từ, nghĩa là người già chết vì tuổi già, ra đi yên ổn, chứ không chết vì tai họa, bệnh tật. 善 là tốt lành, 终 là kết thúc. Người Việt hay chúc sống lâu chết lành, chính là ý này. Tên bài: 善终也是一种权利."),
    ("惧", "jù", "cụ", "động từ", "sợ, sợ hãi", "他面对困难毫无所惧。", "Anh ấy chẳng hề sợ hãi trước khó khăn.",
     "Động từ, văn viết, nghĩa là sợ. Có trong 恐惧, sợ hãi; 无所畏惧, không sợ gì cả. Trong bài: 无痛、无惧、无憾地离世, ra đi không đau đớn, không sợ hãi, không nuối tiếc."),
    ("终极", "zhōngjí", "chung cực", "tính từ", "cuối cùng, tối hậu", "幸福是人生的终极目标。", "Hạnh phúc là mục tiêu tối hậu của đời người.",
     "Tính từ, nghĩa là cuối cùng, cao nhất. Hay đi với 目标, 追求, 问题: 终极目标, mục tiêu tối hậu."),
    ("嘱咐", "zhǔfù", "chúc phó", "động từ", "dặn dò", "妈妈再三嘱咐我路上注意安全。", "Mẹ dặn đi dặn lại tôi đi đường phải chú ý an toàn.",
     "Động từ, nghĩa là dặn dò ai đó nên làm gì, không nên làm gì. 再三嘱咐 là dặn đi dặn lại. Trong khẩu ngữ, chữ sau thường đọc nhẹ."),
    ("插管", "chāguǎn", "sáp quản", "động từ", "đặt ống (nội khí quản, ống thông)", "病人呼吸困难，医生只好给他插管。", "Bệnh nhân khó thở, bác sĩ đành phải đặt ống cho ông ấy.",
     "Động từ, thuật ngữ y học: đưa ống thông vào cơ thể qua các lỗ tự nhiên để đưa vào hoặc hút ra khí, chất lỏng, như đặt nội khí quản. 插 là cắm, 管 là ống."),
    ("勉强", "miǎnqiǎng", "miễn cưỡng", "động từ", "ép (người khác làm điều họ không muốn); gượng", "他不想去，你就别勉强他了。", "Anh ấy không muốn đi thì bạn đừng ép anh ấy nữa.",
     "Động từ, nghĩa là ép người khác làm điều họ không muốn. Cũng làm tính từ, nghĩa là gượng gạo, miễn cưỡng, giống tiếng Việt. Chú ý chữ sau đọc thanh ba, qiǎng."),
    ("躯壳", "qūqiào", "khu xác", "danh từ", "thể xác, xác thân (đối lập với tinh thần)", "失去了理想，人就只剩下一具躯壳。", "Mất đi lý tưởng, con người chỉ còn lại một cái xác không hồn.",
     "Danh từ, chỉ thân thể, đối lập với tinh thần. Chú ý chữ 壳 ở đây đọc qiào, như trong 地壳, vỏ Trái Đất; còn khẩu ngữ 贝壳 thì đọc ké. Trong bài: 勉强留住我的躯壳, cố níu giữ cái xác của tôi."),
    ("引发", "yǐnfā", "dẫn phát", "động từ", "gây ra, khơi ra, dẫn đến", "这条新闻引发了网友的热议。", "Tin này đã gây ra cuộc bàn luận sôi nổi của cư dân mạng.",
     "Động từ, nghĩa là gây ra, châm ngòi cho một sự việc, phản ứng. Phần kết hợp từ sẽ học: 引发热议, 引发争议, 引发思考."),
    ("临近", "línjìn", "lâm cận", "động từ", "gần đến, tới gần", "临近春节，火车站的人越来越多。", "Gần đến Tết, người ở ga tàu ngày càng đông.",
     "Động từ, nghĩa là đến gần, về thời gian hay địa điểm. Trong bài: 当生命临近终点时, khi sự sống gần đến điểm cuối."),
    ("动弹", "dòngtan", "động đạn", "động từ", "cử động, nhúc nhích", "他累得一点儿也不想动弹。", "Anh ấy mệt đến mức chẳng muốn nhúc nhích chút nào.",
     "Động từ, khẩu ngữ, nghĩa là cử động. Chữ sau đọc nhẹ, tan. Thường dùng trong câu phủ định: 动弹不得, 无法动弹, không cử động được."),
    ("监护仪", "jiānhùyí", "giám hộ nghi", "danh từ", "máy theo dõi bệnh nhân (monitor)", "病床旁边的监护仪发出了警报。", "Máy theo dõi bên giường bệnh phát ra tiếng báo động.",
     "Danh từ, chỉ thiết bị đo và theo dõi các chỉ số sinh lý của bệnh nhân như nhịp tim, huyết áp, nồng độ ô-xy, nếu vượt ngưỡng thì báo động. 仪 là máy đo, như 仪器."),
    ("白大褂", "báidàguà", "bạch đại quái", "danh từ", "áo blouse trắng; (chỉ) bác sĩ", "穿上白大褂，他就是一名医生了。", "Khoác lên chiếc áo blouse trắng, anh ấy đã là một bác sĩ.",
     "Danh từ, nghĩa đen là chiếc áo khoác dài màu trắng, dùng để chỉ bác sĩ, nhân viên y tế. 褂 là áo khoác ngoài. Trong bài: 陌生的白大褂, những chiếc áo blouse trắng xa lạ."),
    ("孝道", "xiàodào", "hiếu đạo", "danh từ", "đạo hiếu", "中国人一向重视孝道。", "Người Trung Quốc từ trước đến nay luôn coi trọng đạo hiếu.",
     "Danh từ, chỉ chuẩn mực phụng dưỡng cha mẹ. Âm Hán Việt hiếu đạo, nghĩa như đạo hiếu trong tiếng Việt. Trong bài: 子女视抢救生命为孝道, con cái coi việc cấp cứu là đạo hiếu."),
    ("天职", "tiānzhí", "thiên chức", "danh từ", "thiên chức, bổn phận cao cả", "保护孩子是父母的天职。", "Bảo vệ con cái là thiên chức của cha mẹ.",
     "Danh từ, chỉ trách nhiệm đương nhiên phải làm, mang sắc thái cao quý. Âm Hán Việt và nghĩa giống hệt tiếng Việt thiên chức."),
    ("徒劳", "túláo", "đồ lao", "động từ", "uổng công, phí sức vô ích", "他想说服父亲，但一切都是徒劳。", "Anh ấy muốn thuyết phục bố, nhưng tất cả đều uổng công.",
     "Động từ, nghĩa là tốn sức mà không có ích gì. 徒 là uổng, không. Thành ngữ 徒劳无功 là uổng công vô ích. Trong bài: 徒劳的过度抢救, cấp cứu quá mức một cách vô ích."),
    ("凌迟", "língchí", "lăng trì", "động từ", "hình phạt lăng trì; hành hạ cho chết dần", "凌迟是古代一种非常残酷的死刑。", "Lăng trì là một hình phạt tử hình cực kỳ tàn khốc thời xưa.",
     "Động từ, chỉ một hình phạt tử hình thời cổ, khiến người ta chết dần trong đau đớn tột cùng; tiếng Việt gọi là lăng trì, hay tùng xẻo. Trong bài dùng nghĩa bóng: cấp cứu quá mức chẳng khác gì hành hạ người thân."),
    ("熬", "áo", "ngao", "động từ", "chịu đựng, cố chịu (qua)", "最困难的日子终于熬过去了。", "Những ngày khó khăn nhất cuối cùng cũng đã cố chịu qua được.",
     "Động từ, nghĩa là chịu đựng đau đớn hay cuộc sống gian khổ. Nghĩa gốc là ninh, sắc, như 熬粥, nấu cháo; 熬药, sắc thuốc. 熬夜 là thức khuya. Trong bài: 在病床上熬了整整六年, chịu đựng trên giường bệnh suốt sáu năm.", "遨"),
    ("巴不得", "bābude", "ba bất đắc", "động từ", "chỉ mong, mong sao", "我巴不得马上放假。", "Tôi chỉ mong được nghỉ ngay lập tức.",
     "Động từ, khẩu ngữ, nghĩa là rất mong, mong mỏi tha thiết. Có thể mang động từ hay một câu làm tân ngữ. Đây là mẫu câu trọng điểm."),
    ("昏迷", "hūnmí", "hôn mê", "động từ", "hôn mê", "他出车祸后昏迷了三天。", "Sau tai nạn xe, anh ấy hôn mê ba ngày.",
     "Động từ, nghĩa là mất ý thức trong thời gian dài vì não bị tổn thương. Âm Hán Việt và nghĩa giống hệt tiếng Việt hôn mê."),
    ("折磨", "zhémó", "chiết ma", "động từ", "giày vò, hành hạ", "这种病把他折磨得很痛苦。", "Căn bệnh này giày vò anh ấy rất đau đớn.",
     "Động từ, nghĩa là làm cho thể xác hay tinh thần chịu đau khổ; cũng làm danh từ: 一种折磨, một sự giày vò. Trong bài, Ba Kim nói: 长寿对我来说是一种折磨, sống lâu đối với tôi là một sự giày vò."),
    ("抉择", "juézé", "quyết trạch", "động từ", "lựa chọn (hệ trọng)", "是留在大城市还是回老家，他面临着艰难的抉择。", "Ở lại thành phố lớn hay về quê, anh ấy đứng trước một lựa chọn khó khăn.",
     "Động từ, cũng làm danh từ, nghĩa là lựa chọn, trang trọng hơn 选择. Các bạn đã gặp từ này ở bài sáu chấm hai."),
    ("临终", "línzhōng", "lâm chung", "động từ", "lúc sắp mất, lâm chung", "爷爷临终前把我叫到床边。", "Trước lúc lâm chung, ông nội gọi tôi đến bên giường.",
     "Động từ, chỉ thời điểm người sắp chết. Âm Hán Việt lâm chung, giống tiếng Việt. Kết hợp: 临终前, 临终关怀, chăm sóc cuối đời."),
    ("遗愿", "yíyuàn", "di nguyện", "danh từ", "di nguyện", "我们一定要完成父亲的遗愿。", "Chúng ta nhất định phải hoàn thành di nguyện của cha.",
     "Danh từ, chỉ nguyện vọng chưa thực hiện được của người đã mất. Âm Hán Việt di nguyện, nghĩa giống tiếng Việt. Tương tự có 遗嘱, di chúc; 遗产, di sản."),
    ("恳请", "kěnqǐng", "khẩn thỉnh", "động từ", "khẩn thiết đề nghị, kính mong", "恳请大家再给我一次机会。", "Kính mong mọi người cho tôi thêm một cơ hội.",
     "Động từ, nghĩa là thành khẩn mời hoặc đề nghị. Chữ 恳 là thành khẩn, như 诚恳. Rất hay dùng trong văn bản trang trọng: 恳请批评指正, kính mong phê bình góp ý."),
    ("透析", "tòuxī", "thấu tích", "động từ", "lọc máu, chạy thận nhân tạo", "他每周要去医院做三次透析。", "Mỗi tuần ông ấy phải đến bệnh viện chạy thận ba lần.",
     "Động từ, thuật ngữ y học: dùng kỹ thuật thẩm tách để đưa chất độc và chất thải trong máu ra ngoài cơ thể, tức lọc máu, chạy thận."),
    ("起搏器", "qǐbóqì", "khởi bác khí", "danh từ", "máy tạo nhịp tim", "医生给他装了心脏起搏器。", "Bác sĩ đã lắp máy tạo nhịp tim cho ông ấy.",
     "Danh từ, chỉ thiết bị phát xung điện nhỏ đến tim, kích thích tim đập. 搏 là đập, như 脉搏, mạch đập."),
    ("创伤", "chuāngshāng", "sáng thương", "danh từ", "vết thương, chấn thương", "这次事故给他留下了心理创伤。", "Vụ tai nạn này để lại chấn thương tâm lý cho anh ấy.",
     "Danh từ, chỉ vết thương bên ngoài, nghĩa bóng là tổn thương tinh thần. Chú ý chữ 创 ở đây đọc thanh một, chuāng, khác với 创造, sáng tạo. Trong bài, 创伤性治疗 là điều trị xâm lấn, gây tổn thương cơ thể."),
    ("尽头", "jìntóu", "tận đầu", "danh từ", "điểm cuối, tận cùng", "这条路的尽头是一片大海。", "Cuối con đường này là một vùng biển.",
     "Danh từ, chỉ điểm tận cùng. Trong bài: 走到生命的尽头, đi đến tận cùng của cuộc đời."),
    ("生前", "shēngqián", "sinh tiền", "danh từ", "lúc còn sống, sinh thời", "这是他生前最喜欢的一本书。", "Đây là cuốn sách ông ấy thích nhất lúc sinh thời.",
     "Danh từ, chỉ thời gian khi người đã mất còn sống, tức sinh thời. Trong bài có cụm 生前预嘱, chỉ thị trước về y tế."),
    ("预嘱", "yùzhǔ", "dự chúc", "danh từ", "chỉ thị trước (lập khi còn khỏe, minh mẫn)", "越来越多的人开始签署生前预嘱。", "Ngày càng nhiều người bắt đầu ký chỉ thị trước về y tế.",
     "Danh từ, chỉ văn bản người ta ký từ trước, khi còn khỏe mạnh hoặc minh mẫn, nói rõ cuối đời mình muốn hay không muốn những biện pháp y tế nào. 生前预嘱 tiếng Anh là advance directive."),
    ("治愈", "zhìyù", "trị dũ", "động từ", "chữa khỏi", "这种病已经可以完全治愈了。", "Căn bệnh này đã có thể chữa khỏi hoàn toàn.",
     "Động từ, nghĩa là chữa cho khỏi bệnh. 愈 là khỏi bệnh, như 痊愈. Trong bài: 不可治愈的伤病末期, giai đoạn cuối của bệnh tật, thương tích không thể chữa khỏi."),
    ("末期", "mòqī", "mạt kỳ", "danh từ", "giai đoạn cuối", "他的癌症已经到了末期。", "Bệnh ung thư của ông ấy đã đến giai đoạn cuối.",
     "Danh từ, chỉ giai đoạn cuối cùng. 末 là ngọn, cuối. Kết hợp: 癌症末期, ung thư giai đoạn cuối; 生命末期, giai đoạn cuối đời."),
    ("挽救", "wǎnjiù", "vãn cứu", "động từ", "cứu vãn, cứu", "及时的手术挽救了他的生命。", "Ca phẫu thuật kịp thời đã cứu sống ông ấy.",
     "Động từ, nghĩa là cứu ra khỏi nguy hiểm. Âm Hán Việt vãn cứu, gần với cứu vãn của tiếng Việt. Phần kết hợp từ sẽ học: 挽救生命, 挽救婚姻."),
    ("知情", "zhīqíng", "tri tình", "động từ", "biết rõ sự tình", "病人有知情权。", "Người bệnh có quyền được biết thông tin.",
     "Động từ, nghĩa là biết rõ đầu đuôi một việc. Kết hợp quan trọng: 知情权, quyền được biết; 知情同意, đồng ý sau khi được thông tin đầy đủ; 知情人, người biết chuyện."),
    ("履行", "lǚxíng", "lý hành", "động từ", "thực hiện (nghĩa vụ, lời hứa)", "双方都应该履行合同。", "Hai bên đều phải thực hiện hợp đồng.",
     "Động từ, nghĩa là thực hiện điều mình đã hứa hoặc phải làm. Phần kết hợp từ sẽ học: 履行义务, 履行职责, 履行诺言."),
    ("告知", "gàozhī", "cáo tri", "động từ", "báo cho biết, thông báo", "请将考试结果告知本人。", "Xin hãy thông báo kết quả thi cho chính người dự thi.",
     "Động từ, văn viết, nghĩa là báo cho biết. Mẫu: 将什么告知某人. Trong bài: 告知义务, nghĩa vụ thông báo của bác sĩ."),
    ("免除", "miǎnchú", "miễn trừ", "động từ", "miễn, miễn trừ; loại bỏ", "他因为家庭困难被免除了学费。", "Vì gia đình khó khăn, cậu ấy được miễn học phí.",
     "Động từ, nghĩa là miễn đi, bỏ đi. Âm Hán Việt miễn trừ. Phần kết hợp từ sẽ học: 免除责任, 免除费用, 免除职务."),
    ("短暂", "duǎnzàn", "đoản tạm", "tính từ", "ngắn ngủi", "人生短暂，要珍惜时间。", "Đời người ngắn ngủi, phải biết quý thời gian.",
     "Tính từ, nghĩa là ngắn ngủi về thời gian. Chữ 暂 là tạm thời, đọc thanh bốn. Trong bài: 一个短暂的瞬间, một khoảnh khắc ngắn ngủi."),
    ("共存", "gòngcún", "cộng tồn", "động từ", "cùng tồn tại", "不同的文化可以在一个城市里共存。", "Những nền văn hóa khác nhau có thể cùng tồn tại trong một thành phố.",
     "Động từ, nghĩa là cùng tồn tại. Đây là mẫu câu trọng điểm 与共存."),
    ("体面", "tǐmiàn", "thể diện", "tính từ", "đàng hoàng, tươm tất, có thể diện", "他找到了一份体面的工作。", "Anh ấy đã tìm được một công việc đàng hoàng.",
     "Tính từ, nghĩa là có thể diện, đàng hoàng, đẹp đẽ. Cẩn thận: tiếng Việt thể diện là danh từ, chỉ mặt mũi, danh dự; còn 体面 tiếng Trung chủ yếu là tính từ: 体面的生活, cuộc sống tươm tất; 体面地离开, ra đi đàng hoàng."),
    ("航船", "hángchuán", "hàng thuyền", "danh từ", "con thuyền (chở khách, chở hàng)", "一艘航船慢慢驶进了港口。", "Một con thuyền chầm chậm tiến vào bến cảng.",
     "Danh từ, chỉ thuyền chở khách, chở hàng. Trong bài là hình ảnh ẩn dụ: 如果说生命是一条航船, nếu nói sự sống là một con thuyền."),
    ("舵手", "duòshǒu", "đà thủ", "danh từ", "người cầm lái", "他是这个企业的舵手。", "Ông ấy là người cầm lái của doanh nghiệp này.",
     "Danh từ, nghĩa gốc là người cầm bánh lái thuyền, nghĩa bóng là người nắm phương hướng. 舵 là bánh lái. Trong bài: 每个人都是这条航船的舵手, mỗi người đều là người cầm lái con thuyền đời mình."),
    ("谢幕", "xièmù", "tạ mạc", "động từ", "chào khán giả khi hạ màn; (nghĩa bóng) khép lại", "演出结束后，演员们一起上台谢幕。", "Buổi diễn kết thúc, các diễn viên cùng lên sân khấu chào khán giả.",
     "Động từ li hợp. Sau khi buổi diễn kết thúc, khán giả vỗ tay, diễn viên đứng trước sân khấu cúi chào. 谢 là cảm tạ, 幕 là tấm màn. Nghĩa bóng là khép lại, kết thúc một cách đẹp đẽ: 让生命完美地谢幕."),
    ("奢望", "shēwàng", "xa vọng", "danh từ", "hy vọng xa vời, mong ước quá cao", "对他来说，出国留学只是一种奢望。", "Đối với cậu ấy, đi du học chỉ là một mong ước xa vời.",
     "Danh từ, chỉ hy vọng quá cao, khó thực hiện. 奢 là xa xỉ. Câu kết bài khóa: 让生命完美地谢幕，不应成为一种奢望, để cuộc đời khép lại trọn vẹn không nên là một mong ước xa vời."),
]

add("bullets", chapter="Từ mới (44 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 8.3 có 44 từ mới, chia thành 15 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 躯壳 (qiào) · 勉强 (qiǎng) · 创伤 (chuāng) · 动弹 (tan) · 熬 (áo)",
           "Từ Hán Việt “quen mặt”: 孝道 · 天职 · 昏迷 · 临终 · 遗愿 · 凌迟 – và từ dễ nhầm 体面"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có bốn mươi bốn từ, thầy chia thành mười lăm nhóm nhỏ. Nhiều từ thuộc lĩnh vực y tế, như 插管, 监护仪, 透析, 起搏器.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Chú ý cách đọc của một số chữ: 躯壳 đọc là qūqiào, 勉强 đọc là miǎnqiǎng, 创伤 đọc là chuāngshāng, 动弹 đọc là dòngtan."),
         F(4, "Bài này có rất nhiều từ Hán Việt người Việt dùng hằng ngày: 孝道, hiếu đạo; 天职, thiên chức; 昏迷, hôn mê; 临终, lâm chung; 遗愿, di nguyện. Nhưng hãy cẩn thận với 体面, nghĩa không hoàn toàn giống thể diện. Chúng ta bắt đầu.")])

sizes = [3] * 14 + [2]
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
    ("寿终正寝，无疾而终，谓之善终。善终既是生命的最高追求，也是生命的基本权利。尊重生命，就是要尊重患者对生命的自主权利，将无痛、无惧、无憾地离世作为终极目标。",
     "Sống trọn tuổi trời, chết già yên ổn tại nhà, không bệnh tật mà ra đi, thì gọi là “thiện chung”. Ra đi thanh thản vừa là mong cầu cao nhất của sự sống, vừa là quyền cơ bản của sự sống. Tôn trọng sự sống, chính là tôn trọng quyền tự chủ của người bệnh đối với sự sống của mình, lấy việc ra đi không đau đớn, không sợ hãi, không nuối tiếc làm mục tiêu tối hậu.",
     ["Câu mở đầu rất cô đọng, theo lối văn ngôn. 寿终正寝 là thành ngữ: người già chết yên ổn trong phòng ngủ chính ở nhà mình. 无疾而终 là không bệnh mà mất, tức chết vì tuổi già. 谓之 là gọi là, mẫu câu trọng điểm.",
      "既是，也是 là vừa là, vừa là. 患者 là người bệnh. 自主权利 là quyền tự chủ. 将，作为 là lấy cái gì làm gì. 无痛、无惧、无憾 là không đau, không sợ, không tiếc; cụm này sẽ được nhắc lại ở cuối bài. 终极目标 là mục tiêu tối hậu."]),
    ("台湾知名作家琼瑶曾发表一封公开信，表达了选择“尊严死”的意愿。她嘱咐儿子和儿媳，自己无论生什么重病，都不动大手术、不送加护病房、绝不能插管、不需要急救措施，只要没痛苦地死去就好。",
     "Nhà văn nổi tiếng Đài Loan Quỳnh Dao từng công bố một bức thư ngỏ, bày tỏ mong muốn được lựa chọn “chết có tôn nghiêm”. Bà dặn dò con trai và con dâu rằng, dù mình mắc bệnh nặng gì, cũng không phẫu thuật lớn, không đưa vào phòng chăm sóc đặc biệt, tuyệt đối không được đặt ống, không cần biện pháp cấp cứu, chỉ cần được ra đi không đau đớn là đủ.",
     ["琼瑶 là Quỳnh Dao, nhà văn có nhiều tiểu thuyết và phim rất quen thuộc với khán giả Việt Nam, như 一帘幽梦, Tình thâm khôn tả, và kịch bản phim 还珠格格, Hoàn Châu cách cách. 公开信 là thư ngỏ, công bố năm hai nghìn không trăm mười bảy. 表达意愿 là bày tỏ mong muốn.",
      "嘱咐 là dặn dò. 儿媳 là con dâu. 不动大手术 là không làm phẫu thuật lớn. 加护病房 là cách gọi ở Đài Loan của phòng chăm sóc đặc biệt, ICU. 插管 là đặt ống. 急救措施 là biện pháp cấp cứu. 只要，就好 là chỉ cần… là được."]),
    ("“你们无论多么不舍，不论面对什么压力，都不能勉强留住我的躯壳，让我变成‘求生不得，求死不能’的卧床老人！”琼瑶的生死观，引发了网上网下的热议。",
     "“Các con dù có lưu luyến thế nào, dù đối mặt với áp lực gì, cũng không được cố níu giữ thể xác của mẹ, khiến mẹ biến thành một bà già nằm liệt giường ‘muốn sống không được, muốn chết không xong’!” Quan niệm về sinh tử của Quỳnh Dao đã gây ra những cuộc bàn luận sôi nổi cả trên mạng lẫn ngoài đời.",
     ["无论，不论，都 là dù… dù… đều. 不舍 là không nỡ rời, lưu luyến. 勉强留住 là gượng ép níu giữ. 躯壳 là thể xác, chữ sau đọc qiào.",
      "求生不得，求死不能 là muốn sống không được, muốn chết không xong, chỉ hoàn cảnh cực kỳ khó khăn. 卧床 là nằm liệt giường. 生死观 là quan niệm về sống chết. 引发热议 là gây bàn luận sôi nổi. 网上网下 là trên mạng và ngoài đời."]),
    ("生命是一场说走就走的旅行，也是一场无人陪伴的旅行。当生命临近终点时，绝大多数人都是“被安排”进医院ICU的，全身插满管子，手脚无法动弹，身边只有监护仪和陌生的白大褂。",
     "Sự sống là một chuyến đi nói đi là đi, cũng là một chuyến đi không ai đi cùng. Khi sự sống gần đến điểm cuối, tuyệt đại đa số người ta đều “bị sắp xếp” vào phòng ICU của bệnh viện, khắp người cắm đầy ống, chân tay không cử động được, bên cạnh chỉ có máy theo dõi và những chiếc áo blouse trắng xa lạ.",
     ["说走就走的旅行 là chuyến đi nói đi là đi, một câu rất thịnh hành, vốn chỉ những chuyến du lịch ngẫu hứng; ở đây chỉ cái chết có thể đến bất cứ lúc nào. 无人陪伴 là không ai đi cùng.",
      "临近终点 là gần đến điểm cuối. 被安排 là bị sắp xếp: người bệnh không được tự quyết định. 插满管子 là cắm đầy ống. 动弹 là cử động. 监护仪 là máy theo dõi. 陌生的白大褂 là những bác sĩ xa lạ. Hình ảnh rất lạnh lẽo, cô độc."]),
    ("有的病人痛不欲生，但家属仍坚持抢救到底。他们认为，无论花多大代价，一定要让亲人活着。即便医生已经宣布没有抢救价值，家属依然不肯放弃，其理由就是：“如果他走了，我就没有这个亲人了。”",
     "Có người bệnh đau đớn đến mức không muốn sống, nhưng người nhà vẫn kiên quyết cấp cứu đến cùng. Họ cho rằng, dù tốn bao nhiêu cũng nhất định phải giữ người thân sống. Dù bác sĩ đã tuyên bố không còn giá trị cấp cứu, người nhà vẫn không chịu từ bỏ, lý do chỉ là: “Nếu người ấy đi rồi, tôi sẽ không còn người thân này nữa.”",
     ["痛不欲生 là đau đớn đến mức không muốn sống. 家属 là người nhà, thân nhân. 抢救到底 là cấp cứu đến cùng. 无论花多大代价 là dù phải trả giá bao nhiêu.",
      "即便，依然 là cho dù… vẫn. 宣布 là tuyên bố. 没有抢救价值 là không còn giá trị cấp cứu, tức không thể cứu được nữa. 走了 là cách nói tránh của chết, giống tiếng Việt đi rồi, mất rồi. Lý do của người nhà nghe rất cảm động, nhưng lại xuất phát từ mong muốn của chính họ."]),
    ("子女视抢救生命为“孝道”，医生视救死扶伤为天职，然而，两者都忽视了病人的自主权利。事实上，徒劳的过度抢救，往往只是增加病人的痛苦，即便生命在延续，也是没有尊严的。这种做法，无异于对亲人的“凌迟”。",
     "Con cái coi việc cấp cứu là “đạo hiếu”, bác sĩ coi cứu người là thiên chức; thế nhưng, cả hai đều bỏ qua quyền tự chủ của người bệnh. Thực tế, việc cấp cứu quá mức một cách vô ích thường chỉ làm tăng thêm đau đớn cho người bệnh; cho dù sự sống được kéo dài, đó cũng là sự sống không có tôn nghiêm. Cách làm này chẳng khác gì “lăng trì” người thân.",
     ["视，为 là coi… là, mẫu câu trọng điểm; chữ 为 đọc wéi. 孝道 là đạo hiếu. 救死扶伤 là cứu người sắp chết, chăm sóc người bị thương. 天职 là thiên chức. 两者 là cả hai bên. 忽视 là coi nhẹ, bỏ qua.",
      "徒劳 là uổng công. 过度抢救 là cấp cứu quá mức. 延续 là kéo dài. 无异于 là chẳng khác gì, văn viết. 凌迟 là lăng trì, hình phạt chết dần: một so sánh rất mạnh, cho thấy cấp cứu quá mức là một sự hành hạ."]),
    ("著名文学家巴金曾插着呼吸机，在病床上熬了整整6年。巴金巴不得放弃这种生不如死的治疗，可是他没有选择的权利。因为每一个爱他的人都希望他活下去。哪怕是昏迷着，哪怕是靠机器，只要活着就好。他说：“长寿对我来说是一种折磨。”",
     "Nhà văn nổi tiếng Ba Kim từng phải thở máy, chịu đựng trên giường bệnh suốt 6 năm. Ba Kim chỉ mong được từ bỏ cách điều trị sống không bằng chết này, nhưng ông không có quyền lựa chọn. Bởi vì ai yêu thương ông cũng mong ông sống tiếp. Dù là hôn mê, dù là phải nhờ máy móc, chỉ cần còn sống là được. Ông nói: “Sống lâu đối với tôi là một sự giày vò.”",
     ["巴金 là Ba Kim, một trong những nhà văn lớn nhất của văn học hiện đại Trung Quốc, tác giả bộ tiểu thuyết 家, Gia đình. 插着呼吸机 là cắm máy thở. 熬 là chịu đựng. 整整六年 là suốt sáu năm, mẫu câu 整整 nhấn mạnh thời gian dài.",
      "巴不得 là chỉ mong, mẫu câu trọng điểm; câu 巴金巴不得 còn tạo ra một sự lặp âm thú vị. 生不如死 là sống không bằng chết. 哪怕，只要，就好 là dù… chỉ cần… là được. 长寿 là sống lâu. 折磨 là giày vò."],
     "著名文学家巴金曾插着呼吸机，在病床上熬了整整六年。巴金巴不得放弃这种生不如死的治疗，可是他没有选择的权利。因为每一个爱他的人都希望他活下去。哪怕是昏迷着，哪怕是靠机器，只要活着就好。他说：长寿对我来说是一种折磨。"),
    ("面对生死，每个人都有不同的态度和抉择。有人追求生命的长度，有人追求生命的品质，而每个人对于生命的自主选择权都应得到尊重。对临终亲人最好的关怀，就是把死亡的权利还给亲人，使其按照自己的意愿度过最后的时光。",
     "Đối mặt với sống chết, mỗi người đều có thái độ và lựa chọn khác nhau. Có người theo đuổi độ dài của sự sống, có người theo đuổi chất lượng của sự sống, nhưng quyền tự lựa chọn của mỗi người đối với sự sống đều đáng được tôn trọng. Sự quan tâm tốt nhất dành cho người thân lúc lâm chung, chính là trả lại quyền được chết cho họ, để họ sống những ngày cuối cùng theo ý nguyện của mình.",
     ["抉择 là lựa chọn hệ trọng. 生命的长度 là độ dài của sự sống; 生命的品质 là chất lượng của sự sống: hai quan niệm đối lập. 自主选择权 là quyền tự lựa chọn.",
      "临终亲人 là người thân lúc lâm chung. 关怀 là quan tâm, chăm sóc. 把死亡的权利还给亲人 là trả lại quyền được chết cho người thân. 使其 là khiến họ, văn viết. 度过最后的时光 là sống qua những ngày cuối cùng."]),
    ("我国著名外科专家、北京医院名誉院长吴蔚然在临终前留下遗愿，恳请医院尊重自然规律，不必采用插管、透析、起搏器等创伤性治疗延长生命。最后，家人尊重了他的自主选择，陪伴他平静地走到生命的尽头。",
     "Chuyên gia ngoại khoa nổi tiếng của nước ta, Giám đốc danh dự Bệnh viện Bắc Kinh Ngô Úy Nhiên, trước lúc lâm chung đã để lại di nguyện, khẩn thiết đề nghị bệnh viện tôn trọng quy luật tự nhiên, không cần dùng các biện pháp điều trị xâm lấn như đặt ống, lọc máu, máy tạo nhịp tim để kéo dài sự sống. Cuối cùng, gia đình đã tôn trọng lựa chọn của ông, ở bên ông bình thản đi đến tận cùng cuộc đời.",
     ["我国 là nước ta, tức Trung Quốc. 外科专家 là chuyên gia ngoại khoa. 名誉院长 là giám đốc danh dự. 吴蔚然 là bác sĩ ngoại khoa nổi tiếng, mất năm hai nghìn không trăm mười sáu. 遗愿 là di nguyện. 恳请 là khẩn thiết đề nghị.",
      "自然规律 là quy luật tự nhiên. 不必 là không cần. 透析 là lọc máu; 起搏器 là máy tạo nhịp tim. 创伤性治疗 là điều trị xâm lấn. 延长生命 là kéo dài sự sống. 平静地走到生命的尽头 là bình thản đi đến cuối cuộc đời: một ví dụ đối lập với câu chuyện của Ba Kim."]),
    ("近年来，不少医学界人士致力于推广“生前预嘱”，鼓励“尊严死”，提倡“我的死亡我做主”。“尊严死”不同于安乐死，是指在不可治愈的伤病末期，放弃抢救和不使用生命支持系统，让死亡既不提前，也不拖后，而是自然来临。",
     "Những năm gần đây, không ít người trong giới y học dốc sức phổ biến “chỉ thị trước về y tế”, khuyến khích “chết có tôn nghiêm”, đề xướng “cái chết của tôi do tôi làm chủ”. “Chết có tôn nghiêm” khác với an tử: đó là khi bệnh tật, thương tích đã ở giai đoạn cuối, không thể chữa khỏi, thì từ bỏ cấp cứu và không dùng hệ thống duy trì sự sống, để cái chết không đến sớm hơn, cũng không bị kéo lùi lại, mà đến một cách tự nhiên.",
     ["医学界人士 là người trong giới y học. 致力于 là dốc sức vào. 推广 là phổ biến, mở rộng. 生前预嘱 là chỉ thị trước về y tế. 提倡 là đề xướng. 我的死亡我做主 là cái chết của tôi tôi làm chủ, mẫu câu trọng điểm.",
      "不同于 là khác với. Đây là định nghĩa quan trọng: an tử là chủ động làm cho chết; còn 尊严死 là không can thiệp, để cái chết 既不提前，也不拖后, không sớm hơn cũng không muộn hơn, mà 自然来临, đến tự nhiên. 生命支持系统 là hệ thống duy trì sự sống."]),
    ("在这个过程中，应最大限度尊重本人意愿，尽量使其有尊严地告别人生。“尊严死”不把挽救生命作为首选，而是将无痛、无惧、无憾地离世作为目标，让“生死两相憾”变成“生死两相安”。这是文明社会的基本标志。",
     "Trong quá trình này, cần tôn trọng ở mức cao nhất ý nguyện của bản thân người bệnh, cố gắng để họ giã từ cuộc đời một cách có tôn nghiêm. “Chết có tôn nghiêm” không đặt việc cứu vãn sự sống lên hàng đầu, mà lấy việc ra đi không đau đớn, không sợ hãi, không nuối tiếc làm mục tiêu, biến “kẻ ở người đi đều ân hận” thành “kẻ ở người đi đều yên lòng”. Đây là dấu hiệu cơ bản của một xã hội văn minh.",
     ["最大限度 là ở mức tối đa. 本人意愿 là ý nguyện của chính người bệnh. 尽量 là cố gắng hết mức. 告别人生 là giã từ cuộc đời.",
      "不把，作为首选，而是将，作为目标 là không lấy A làm lựa chọn hàng đầu, mà lấy B làm mục tiêu: mẫu câu 把作为首选. 生死两相憾 là cả người sống lẫn người chết đều ân hận; 生死两相安 là cả hai đều yên lòng. 文明社会的基本标志 là dấu hiệu cơ bản của xã hội văn minh."]),
    ("人生最无奈的事是既不能选择生，也不能选择死。2016年台湾通过《病人自主权利法》，并于2019年正式实施。这部法律强调尊重病人的医疗自主，保障病人的善终权益，确保病人有知情、选择或拒绝医疗的权利。",
     "Điều bất lực nhất của đời người là không thể chọn sinh ra, cũng không thể chọn cái chết. Năm 2016, Đài Loan thông qua “Luật Quyền tự chủ của bệnh nhân”, và chính thức thi hành từ năm 2019. Luật này nhấn mạnh tôn trọng quyền tự chủ về y tế của người bệnh, bảo đảm quyền lợi được ra đi thanh thản của người bệnh, bảo đảm người bệnh có quyền được biết, được lựa chọn hoặc từ chối điều trị.",
     ["无奈 là bất lực, đành chịu. 既不能，也不能 là đã không thể… cũng không thể. 通过 là thông qua, nói về luật. 病人自主权利法 là Luật Quyền tự chủ của bệnh nhân, đạo luật đầu tiên ở châu Á lấy quyền tự chủ y tế của người bệnh làm trọng tâm. 正式实施 là chính thức thi hành.",
      "医疗自主 là tự chủ về y tế. 保障 và 确保 đều là bảo đảm. 善终权益 là quyền lợi được ra đi thanh thản. 知情 là được biết: ba quyền 知情、选择、拒绝 là được biết, được chọn và được từ chối điều trị."],
     "人生最无奈的事是既不能选择生，也不能选择死。二零一六年台湾通过《病人自主权利法》，并于二零一九年正式实施。这部法律强调尊重病人的医疗自主，保障病人的善终权益，确保病人有知情、选择或拒绝医疗的权利。"),
    ("根据规定，病人可以提前作出医疗决定，选择接受或拒绝医疗；医生履行告知义务的对象是患者本人，医生必须以适当方式将病情告知病人；医生执行患者“善终指示”，可以免除法律责任。这部法律为“尊严死”提供了有力保障，维护了每个人本该拥有的“善终权”。",
     "Theo quy định, người bệnh có thể đưa ra quyết định y tế từ trước, chọn chấp nhận hoặc từ chối điều trị; đối tượng mà bác sĩ thực hiện nghĩa vụ thông báo là chính người bệnh, bác sĩ phải thông báo bệnh tình cho người bệnh bằng cách thức phù hợp; bác sĩ thực hiện “chỉ thị ra đi thanh thản” của người bệnh thì được miễn trách nhiệm pháp lý. Đạo luật này đã bảo đảm vững chắc cho “chết có tôn nghiêm”, bảo vệ “quyền ra đi thanh thản” mà lẽ ra mỗi người đều được có.",
     ["Đoạn này nêu ba điểm chính của luật, ngăn cách bằng dấu chấm phẩy. Một: 提前作出医疗决定, người bệnh được quyết định trước. Hai: 履行告知义务的对象是患者本人, bác sĩ phải nói bệnh tình với chính người bệnh, chứ không chỉ nói với người nhà như thói quen ở nhiều nước châu Á.",
      "Ba: 执行善终指示，可以免除法律责任, bác sĩ làm theo chỉ thị của người bệnh thì không bị truy cứu trách nhiệm. 履行 là thực hiện; 告知 là thông báo; 免除 là miễn. 有力保障 là sự bảo đảm vững chắc. 本该拥有 là lẽ ra phải có."]),
    ("死亡也许只是一个短暂的瞬间，但与疾病共存则是一个长期的过程。尊重患者的生命自主权，并非鼓励放弃治疗，而是要让临终者体面而有尊严地离开人世。生是偶然，死是必然。如果说生命是一条航船，每个人都是这条航船的舵手。让生命完美地谢幕，不应成为一种奢望。",
     "Cái chết có lẽ chỉ là một khoảnh khắc ngắn ngủi, nhưng sống chung với bệnh tật lại là một quá trình lâu dài. Tôn trọng quyền tự chủ về sự sống của người bệnh không phải là khuyến khích từ bỏ điều trị, mà là để người sắp ra đi được rời khỏi cõi đời một cách đàng hoàng và có tôn nghiêm. Sinh ra là ngẫu nhiên, chết đi là tất yếu. Nếu nói sự sống là một con thuyền, thì mỗi người đều là người cầm lái của con thuyền ấy. Để cuộc đời khép lại một cách trọn vẹn không nên là một mong ước xa vời.",
     ["短暂的瞬间 là khoảnh khắc ngắn ngủi. 与疾病共存 là sống chung với bệnh tật, mẫu câu 与共存; 则 là thì, lại, biểu thị đối lập. 并非，而是 là không phải… mà là: tác giả nói rõ, tôn trọng quyền tự chủ không có nghĩa là khuyến khích bỏ điều trị.",
      "体面 là đàng hoàng. 生是偶然，死是必然 là sinh là ngẫu nhiên, tử là tất yếu. 航船 và 舵手 là hình ảnh ẩn dụ: mỗi người tự cầm lái con thuyền đời mình. 谢幕 là chào khán giả khi hạ màn; 奢望 là mong ước xa vời. Câu kết rất đẹp, khép lại cả bài khóa."]),
]
HEAD = {}

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 善终也是一种权利", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa. Bài lấy từ chuyên mục 不吐不快, không nói không yên, trên báo 人民日报, Nhân Dân Nhật báo, ngày hai mươi bốn tháng ba năm hai nghìn không trăm mười bảy, tác giả 白剑锋. Bài dài khoảng một nghìn hai trăm chữ, văn phong bình luận, nhiều câu văn đẹp và giàu hình ảnh.",
         F(0, "Thầy chia bài thành mười bốn đoạn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 90 else 50 if len(zh) <= 115 else 46 if len(zh) <= 150 else 44
    title = f"Bài khóa – đoạn {i}/{len(P)}" + (f" · {HEAD[i]}" if i in HEAD else "")
    add("passage", section="Bài khóa 课文", title=title, zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", "").replace("‘", "").replace("’", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Bố cục & ghi chú", section="Bài khóa 课文", title="Bố cục bài khóa", size=34,
    items=["## 1. Luận điểm: 善终是生命的基本权利 (đoạn 1–3)",
           "无痛、无惧、无憾地离世 · 琼瑶的公开信: 不插管、不急救 → 引发热议",
           "## 2. Thực trạng: cấp cứu quá mức (đoạn 4–7)",
           "被安排进ICU · 家属抢救到底 · 视抢救生命为孝道 → 无异于凌迟 · 巴金: 长寿是一种折磨",
           "## 3. Giải pháp: tôn trọng lựa chọn, “尊严死” (đoạn 8–11)",
           "吴蔚然的遗愿 · 生前预嘱 · 尊严死≠安乐死: 既不提前，也不拖后",
           "## 4. Pháp luật bảo đảm và kết luận (đoạn 12–14)",
           "《病人自主权利法》: 知情、选择、拒绝 · 让生命完美地谢幕，不应成为一种奢望"],
    say=["Trước khi sang phần mẫu câu, chúng ta cùng nhìn lại bố cục bài khóa. Đây là một bài văn nghị luận rất chặt chẽ, có bốn phần.",
         F(1, "Phần một nêu luận điểm: ra đi thanh thản là quyền cơ bản của sự sống, mục tiêu là ra đi không đau, không sợ, không tiếc. Dẫn chứng là bức thư ngỏ của Quỳnh Dao."),
         F(3, "Phần hai nói về thực trạng: phần lớn người bệnh bị đưa vào ICU, người nhà kiên quyết cấp cứu đến cùng vì chữ hiếu, nhưng cấp cứu quá mức chẳng khác gì hành hạ. Dẫn chứng là sáu năm thở máy của Ba Kim."),
         F(5, "Phần ba đưa ra giải pháp: tôn trọng lựa chọn của người sắp mất như gia đình bác sĩ Ngô Úy Nhiên, phổ biến chỉ thị trước về y tế, khuyến khích chết có tôn nghiêm, khác với an tử."),
         F(7, "Phần bốn: pháp luật Đài Loan đã bảo đảm quyền này, và câu kết: để cuộc đời khép lại trọn vẹn không nên là một mong ước xa vời. Bố cục luận điểm, thực trạng, giải pháp, kết luận này rất đáng học khi viết bài nghị luận tiếng Trung.")])

add("bullets", section="Bài khóa 课文", title="Ghi chú 注释: hiểu thêm về bối cảnh", size=31,
    items=["琼瑶 Quỳnh Dao: tên thật 陈喆, sinh năm 1938 ở Thành Đô; nhà văn, biên kịch, nhà sản xuất phim; tác phẩm: 《窗外》《潮声》《水云间》《一帘幽梦》《心有千千结》",
           "安乐死 an tử (euthanasia): ngừng điều trị hoặc dùng thuốc để người bệnh vô phương cứu chữa ra đi không đau đớn; được phép ở một số nơi như Hà Lan, Bỉ, Canada…; Trung Quốc thảo luận từ giữa thập niên 1980, chưa lập pháp",
           "尊严死: ngừng điều trị xâm lấn và cấp cứu với người bệnh vô phương cứu chữa, để họ ra đi có tôn nghiêm",
           "巴金 Ba Kim (1904–2005): tên thật 李尧棠, du học Pháp 1927–1929; tác phẩm 《家》《寒夜》《随想录》; được coi là “lương tâm của giới trí thức”",
           "《病人自主权利法》: Đài Loan thông qua năm 2016, thi hành năm 2019 – luật đầu tiên ở châu Á lấy quyền tự chủ y tế của người bệnh làm trọng tâm"],
    say=["Sách có năm ghi chú giúp hiểu thêm bối cảnh bài khóa.",
         F(0, "Một: 琼瑶, Quỳnh Dao, tên thật là 陈喆, sinh năm một nghìn chín trăm ba mươi tám ở Thành Đô, tỉnh Tứ Xuyên, là nhà văn, nhà biên kịch và nhà sản xuất phim. Tác phẩm tiêu biểu gồm 窗外, Ngoài cửa sổ; 水云间; 一帘幽梦, và 心有千千结."),
         F(1, "Hai: 安乐死, an tử, là ngừng điều trị hoặc dùng thuốc để người bệnh không thể cứu chữa ra đi không đau đớn. Hiện một số nước và vùng lãnh thổ cho phép, như Hà Lan, Bỉ, Canada, Tây Ban Nha, New Zealand. Trung Quốc bắt đầu thảo luận về an tử từ giữa thập niên tám mươi thế kỷ hai mươi; vấn đề này liên quan đến đạo đức, luân lý, pháp luật, y học, rất phức tạp, nên Trung Quốc chưa lập pháp."),
         F(2, "Ba: 尊严死, chết có tôn nghiêm, là ngừng điều trị xâm lấn và cấp cứu đối với người bệnh không thể cứu chữa, để họ ra đi có tôn nghiêm."),
         F(3, "Bốn: 巴金, Ba Kim, sống từ năm một nghìn chín trăm linh bốn đến năm hai nghìn không trăm linh năm, tên thật là 李尧棠, từng du học ở Pháp. Ông là một trong những nhà văn có ảnh hưởng nhất từ phong trào Ngũ Tứ, với các tác phẩm 家, 寒夜, 随想录, và được coi là lương tâm của giới trí thức Trung Quốc."),
         F(4, "Năm: 病人自主权利法, Luật Quyền tự chủ của bệnh nhân, được Đài Loan thông qua năm hai nghìn không trăm mười sáu và thi hành năm hai nghìn không trăm mười chín. Đây là đạo luật đầu tiên ở châu Á lấy quyền tự chủ y tế của người bệnh làm trọng tâm.")])

# ======================= MẪU CÂU =======================
add("bullets", chapter="Mẫu câu: 谓之 · 视…为 · 整整 · 巴不得", section="Mẫu câu 重点句型", title="1. ……谓之…… · 2. 视……为……", size=33,
    items=["## A谓之B: A gọi là B (văn viết, mang màu sắc văn ngôn)",
           "寿终正寝，无疾而终，谓之善终。",
           "形而上者谓之道，形而下者谓之器。",
           "久旱逢甘霖，他乡遇故知，洞房花烛夜，金榜题名时，谓之人生四大乐事。",
           "## 视A为B: coi A là B (= 把A看作B)",
           "家属视抢救生命为“孝道”，医生视救死扶伤为天职。",
           "人与人之间的关系总是相互的，你视我为挚友，我亦视你为知己。",
           "作为一名教师，他视教书育人为自己的终生事业。"],
    say=["Bây giờ chúng ta sang phần mẫu câu. Bài này có bảy điểm. Đầu tiên là 谓之 và 视为.",
         F(0, "A 谓之 B nghĩa là A gọi là B. 谓 là gọi, nói; 之 là đại từ văn ngôn, chỉ A. Mẫu câu mang màu sắc văn ngôn, dùng trong văn viết trang trọng, thường để định nghĩa."),
         F(1, "Ví dụ từ bài khóa: 寿终正寝，无疾而终，谓之善终。 Chết già tại nhà, không bệnh mà mất, gọi là thiện chung."),
         F(2, "形而上者谓之道，形而下者谓之器。 Câu trong Kinh Dịch: cái ở trên hình thể gọi là đạo, cái ở dưới hình thể gọi là khí. Đây là nguồn gốc của từ 形而上学, siêu hình học."),
         F(3, "久旱逢甘霖，他乡遇故知，洞房花烛夜，金榜题名时，谓之人生四大乐事。 Hạn lâu gặp mưa rào, đất khách gặp bạn cũ, đêm động phòng hoa chúc, lúc bảng vàng đề tên, gọi là bốn niềm vui lớn của đời người."),
         F(4, "视 A 为 B nghĩa là coi A là B, giống 把A看作B nhưng văn viết hơn. Chữ 为 đọc wéi. Hay gặp: 视为, 视他为, 视为天职."),
         F(5, "Ví dụ từ bài khóa: 家属视抢救生命为孝道，医生视救死扶伤为天职。"),
         F(6, "人与人之间的关系总是相互的，你视我为挚友，我亦视你为知己。 Quan hệ giữa người với người luôn là hai chiều, anh coi tôi là bạn thân, tôi cũng coi anh là tri kỷ. 亦 là cũng, văn viết."),
         F(7, "作为一名教师，他视教书育人为自己的终生事业。 Là một giáo viên, ông coi việc dạy chữ dạy người là sự nghiệp cả đời mình.")])

add("bullets", section="Mẫu câu 重点句型", title="3. 整整…… · 4. 巴不得……", size=33,
    items=["## 整整 + số lượng: tròn, trọn, suốt (nhấn mạnh: thấy dài, thấy nhiều)",
           "著名文学家巴金曾插着呼吸机，在病床上熬了整整6年。",
           "这么重要一个会，他整整迟到了五分钟。",
           "去年冬天买的这件大衣花了我整整一个月的工资。",
           "## 巴不得 + V / câu: chỉ mong, mong sao (khẩu ngữ)",
           "巴金巴不得放弃这种生不如死的治疗，可是他没有选择的权利。",
           "他正巴不得你去给他帮忙呢，你怎么不愿意呢？",
           "夏天到来之前，他坚持去健身，巴不得瘦个十来斤。"],
    say=["Tiếp theo là 整整 và 巴不得.",
         F(0, "整整 đứng trước số lượng, nghĩa là tròn, trọn, suốt. Ngoài việc chỉ con số chẵn, nó còn thể hiện cảm nhận chủ quan của người nói: thấy thời gian dài, số lượng nhiều."),
         F(1, "Ví dụ từ bài khóa: 著名文学家巴金曾插着呼吸机，在病床上熬了整整六年。 Suốt sáu năm, một khoảng thời gian rất dài và đau đớn.",
           cap="Ví dụ từ bài khóa: 著名文学家巴金曾插着呼吸机，在病床上熬了整整6年。 Suốt 6 năm, một khoảng thời gian rất dài và đau đớn."),
         F(2, "这么重要一个会，他整整迟到了五分钟。 Cuộc họp quan trọng như thế mà anh ta đến muộn tròn năm phút. Năm phút không dài, nhưng với cuộc họp quan trọng thì người nói thấy là nhiều."),
         F(3, "去年冬天买的这件大衣花了我整整一个月的工资。 Chiếc áo khoác mua mùa đông năm ngoái tốn của tôi trọn một tháng lương."),
         F(4, "巴不得 nghĩa là rất mong, mong mỏi tha thiết. Theo sau có thể là động từ hoặc cả một câu. Chữ 得 đọc nhẹ."),
         F(5, "Ví dụ từ bài khóa: 巴金巴不得放弃这种生不如死的治疗，可是他没有选择的权利。"),
         F(6, "他正巴不得你去给他帮忙呢，你怎么不愿意呢？ Anh ấy đang mong cậu đến giúp lắm đấy, sao cậu lại không muốn?"),
         F(7, "夏天到来之前，他坚持去健身，巴不得瘦个十来斤。 Trước khi mùa hè đến, anh ấy kiên trì tập gym, chỉ mong giảm được chừng mười cân, tức khoảng năm ký.")])

add("bullets", chapter="Mẫu câu: 我的…我做主 · 作为首选 · 与…共存", section="Mẫu câu 重点句型", title="5. 我的……我做主 · 6. 把……作为首选", size=33,
    items=["## 我的 + N + 我做主: … của tôi, tôi làm chủ",
           "近年来，不少医学界人士致力于推广“生前预嘱”，鼓励“尊严死”，提倡“我的死亡我做主”。",
           "……几乎当时所有的年轻人都会脱口而出：“我的地盘我做主”。",
           "《我的青春我做主》是一部当代都市题材电视剧，引起了很多年轻人的共鸣。",
           "## 把/将……作为首选: chọn… làm ưu tiên hàng đầu",
           "“尊严死”不把挽救生命作为首选，而是将无痛、无惧、无憾地离世作为目标。",
           "谈到毕业后的打算，他把考研究生作为首选，暂时不考虑就业。",
           "医生认为应该把手术作为首选治疗手段。"],
    say=["Tiếp theo là 我的我做主 và 把作为首选.",
         F(0, "我的 cộng danh từ cộng 我做主 nghĩa là cái gì đó của tôi, tôi tự làm chủ. Mẫu câu nhấn mạnh quyền tự quyết đối với hành vi của bản thân, rất được giới trẻ yêu thích."),
         F(1, "Ví dụ từ bài khóa: 不少医学界人士致力于推广生前预嘱，鼓励尊严死，提倡我的死亡我做主。"),
         F(2, "提到二零零三年移动电信推出的手机套餐动感地带的广告词，几乎当时所有的年轻人都会脱口而出：我的地盘我做主。 Nhắc đến khẩu hiệu quảng cáo của gói cước Động Cảm Địa Đới năm hai nghìn không trăm linh ba, hầu như mọi người trẻ thời ấy đều buột miệng nói ngay: địa bàn của tôi, tôi làm chủ.",
           cap="提到2003年移动电信推出的手机套餐“动感地带”的广告词，几乎当时所有的年轻人都会脱口而出：“我的地盘我做主”。 Khẩu hiệu quảng cáo nổi tiếng năm 2003: “Địa bàn của tôi, tôi làm chủ”."),
         F(3, "我的青春我做主是一部当代都市题材电视剧，引起了很多年轻人的共鸣。 Thanh xuân của tôi, tôi làm chủ là một bộ phim truyền hình đề tài đô thị đương đại, khiến nhiều bạn trẻ đồng cảm. 共鸣 là đồng cảm, cộng hưởng."),
         F(4, "把 hoặc 将, cộng một phương án, rồi 作为首选, nghĩa là chọn phương án ấy làm ưu tiên hàng đầu. 首选 là lựa chọn đầu tiên. Thể phủ định thường đi với 而是: 不把A作为首选，而是将B作为目标."),
         F(5, "Ví dụ từ bài khóa: 尊严死不把挽救生命作为首选，而是将无痛、无惧、无憾地离世作为目标。"),
         F(6, "谈到毕业后的打算，他把考研究生作为首选，暂时不考虑就业。 Nói đến dự định sau khi tốt nghiệp, anh ấy chọn thi cao học là ưu tiên hàng đầu, tạm thời chưa nghĩ đến việc đi làm."),
         F(7, "医生认为应该把手术作为首选治疗手段。 Bác sĩ cho rằng nên chọn phẫu thuật làm phương pháp điều trị hàng đầu.")])

add("bullets", section="Mẫu câu 重点句型", title="7. 与……共存", size=35,
    items=["## A与B共存: A cùng tồn tại, sống chung với B",
           "死亡也许只是一个短暂的瞬间，但与疾病共存则是一个长期的过程。",
           "维持清零还是与病毒共存，每个人有不同的见解。",
           "保护环境，善待自然，人类应该与万物和谐共存。",
           "Kết hợp hay gặp: 和平共存 · 和谐共存 · 与……长期共存"],
    say=["Điểm cuối cùng là 与共存.",
         F(0, "A 与 B 共存 nghĩa là A cùng tồn tại, sống chung với B. Có thể thay 与 bằng 和. Thường dùng khi B là thứ khó tránh, không loại bỏ được, như bệnh tật, virus, hoặc khi nói về sự hài hòa."),
         F(1, "Ví dụ từ bài khóa: 死亡也许只是一个短暂的瞬间，但与疾病共存则是一个长期的过程。 Cái chết chỉ là khoảnh khắc, nhưng sống chung với bệnh tật là cả một quá trình dài."),
         F(2, "维持清零还是与病毒共存，每个人有不同的见解。 Duy trì chính sách đưa ca bệnh về không hay sống chung với virus, mỗi người có cách nhìn khác nhau. Câu này nói về thời kỳ dịch COVID; ở Việt Nam cũng từng có khẩu hiệu sống chung an toàn với dịch."),
         F(3, "保护环境，善待自然，人类应该与万物和谐共存。 Bảo vệ môi trường, đối xử tốt với thiên nhiên, con người nên chung sống hài hòa với vạn vật. 善待 là đối xử tốt."),
         F(4, "Những kết hợp hay gặp: 和平共存, chung sống hòa bình; 和谐共存, chung sống hài hòa; 与什么长期共存, chung sống lâu dài với cái gì.")])

# ======================= KẾT HỢP TỪ & THÀNH NGỮ =======================
add("bullets", chapter="Kết hợp từ & thành ngữ", section="Kết hợp từ 词语搭配", title="Kết hợp từ (1): 引发 · 勉强 · 挽救", size=33,
    items=["## 引发: ～热议 · ～思考 · ～争议 · ～讨论 · ～不满 · ～反抗",
           "一段30秒左右的视频，在社交媒体上引发了3800多万次点击。",
           "## 勉强: ～同意 · ～接受 · ～回答 · ～留下 · ～应付 · 觉得～ · 笑得很～",
           "看在老人孩子的面子上，她勉强接受了丈夫的复婚要求。",
           "## 挽救: ～生命 · ～市场 · ～婚姻 · 及时～ · 全力～ · 尽力～",
           "医学专家采取各种治疗手段，不惜一切代价，全力挽救他的生命。"],
    say=["Tiếp theo là phần kết hợp từ. Bài này có sáu từ, thầy chia làm hai slide.",
         F(0, "引发 đi với 热议, bàn luận sôi nổi; 思考, suy ngẫm; 争议, tranh cãi; 讨论, thảo luận; 不满, bất mãn; 反抗, phản kháng. Tân ngữ thường là một phản ứng của con người."),
         F(1, "Ví dụ: 一段三十秒左右的视频，在社交媒体上引发了三千八百多万次点击。 Một đoạn video khoảng ba mươi giây đã tạo ra hơn ba mươi tám triệu lượt xem trên mạng xã hội.",
           cap="Ví dụ: 一段30秒左右的视频，在社交媒体上引发了3800多万次点击。 Một đoạn video khoảng 30 giây đã tạo ra hơn 38 triệu lượt xem trên mạng xã hội."),
         F(2, "勉强 làm trạng ngữ: 勉强同意, miễn cưỡng đồng ý; 勉强接受; 勉强回答; 勉强留下; 勉强应付, đối phó cho qua. Làm tính từ: 觉得勉强, 显得勉强, 笑得很勉强, cười gượng."),
         F(3, "Ví dụ: 看在老人孩子的面子上，她勉强接受了丈夫的复婚要求。 Vì nể bố mẹ già và con cái, cô ấy miễn cưỡng chấp nhận đề nghị tái hôn của chồng. 复婚 là tái hợp sau khi ly hôn."),
         F(4, "挽救 đi với 生命, sự sống; 市场, thị trường; 婚姻, hôn nhân; và các trạng ngữ 及时, kịp thời; 极力, hết sức; 全力, dốc toàn lực; 尽力, cố gắng hết sức."),
         F(5, "Ví dụ: 医学专家采取各种治疗手段，不惜一切代价，全力挽救他的生命。 Các chuyên gia y học dùng mọi biện pháp điều trị, không tiếc bất cứ giá nào, dốc toàn lực cứu sống ông ấy. 不惜一切代价 là bằng mọi giá.")])

add("bullets", section="Kết hợp từ 词语搭配", title="Kết hợp từ (2): 履行 · 免除 · 体面", size=33,
    items=["## 履行: ～义务 · ～职责 · ～合同 · ～诺言",
           "他屡屡逃避责任，不履行抚养孩子的义务。",
           "## 免除: ～费用 · ～债务 · ～职务 · ～责任 · ～刑罚 · ～兵役 · ～资格",
           "如果符合减免条件，就可以申请部分或全部免除个人收入所得税。",
           "## 体面: ～的工作 · ～的生活 · ～地离开 · ～地放弃 · 不失～ · 有失～",
           "既然爱情已经无法挽回，不如选择体面地放手，给自己留一点尊严。"],
    say=[F(0, "履行 đi với 义务, nghĩa vụ; 职责, chức trách; 合同, hợp đồng; 诺言, lời hứa. Đều là những thứ đã hứa hoặc bắt buộc phải làm."),
         F(1, "Ví dụ: 他屡屡逃避责任，不履行抚养孩子的义务。 Anh ta nhiều lần trốn tránh trách nhiệm, không thực hiện nghĩa vụ nuôi con. 抚养 là nuôi dưỡng, cấp dưỡng."),
         F(2, "免除 đi với 费用, chi phí; 债务, nợ; 职务, chức vụ, tức là cách chức; 责任, trách nhiệm; 刑罚, hình phạt; 兵役, nghĩa vụ quân sự; 资格, tư cách."),
         F(3, "Ví dụ: 如果符合减免条件，就可以申请部分或全部免除个人收入所得税。 Nếu đủ điều kiện giảm miễn, có thể xin miễn một phần hoặc toàn bộ thuế thu nhập cá nhân."),
         F(4, "体面 đi với 的工作, công việc đàng hoàng; 的生活, cuộc sống tươm tất; 地离开, ra đi đàng hoàng; 地放弃, từ bỏ một cách đẹp đẽ; và 不失体面, không mất thể diện; 有失体面, mất thể diện."),
         F(5, "Ví dụ: 既然爱情已经无法挽回，不如选择体面地放手，给自己留一点尊严。 Tình yêu đã không thể cứu vãn, chi bằng buông tay một cách đẹp đẽ, giữ lại chút tôn nghiêm cho mình.")])

add("bullets", section="Thành ngữ 成语", title="Thành ngữ (1): 寿终正寝 · 无疾而终 · 求生不得，求死不能", size=33,
    items=["## 寿终正寝 shòuzhōng-zhèngqǐn – chết già yên ổn tại nhà; (sự vật) tự nhiên chấm dứt",
           "吴老先生于昨日寿终正寝，享年八十五岁。",
           "## 无疾而终 wújí'érzhōng – không bệnh mà mất (vì tuổi già); (sự việc) tự nhiên tan biến",
           "毕业以后，大家各奔东西，我们乐队出唱片的计划也就无疾而终。",
           "## 求生不得，求死不能 – muốn sống không được, muốn chết không xong",
           "公司资金链断了，又欠了一屁股债，处于“求生不得，求死不能”的困境。"],
    say=["Bài này có sáu thành ngữ. Thầy chia làm hai slide.",
         F(0, "寿终正寝: 寿终 là hết tuổi thọ, 正寝 là phòng ngủ chính trong nhà. Người già mất yên ổn tại nhà mình. Nghĩa bóng là sự vật tự nhiên tiêu vong."),
         F(1, "Ví dụ: 吴老先生于昨日寿终正寝，享年八十五岁。 Cụ Ngô đã an nhiên qua đời hôm qua, hưởng thọ tám mươi lăm tuổi. 享年 là hưởng thọ, dùng cho người đã mất."),
         F(2, "无疾而终: 疾 là bệnh. Không bệnh tật gì mà mất, tức chết vì tuổi già. Nghĩa bóng hay dùng hơn: một kế hoạch, một mối quan hệ không bị tác động gì mà tự nhiên tan biến."),
         F(3, "Ví dụ: 毕业以后，大家各奔东西，我们乐队出唱片的计划也就无疾而终。 Tốt nghiệp xong, mỗi người một ngả, kế hoạch ra album của ban nhạc chúng tôi cũng tự nhiên tan biến. 各奔东西 là mỗi người một ngả."),
         F(4, "求生不得，求死不能: muốn sống không được, muốn chết cũng không xong, chỉ hoàn cảnh cực kỳ khó khăn, bế tắc."),
         F(5, "Ví dụ: 公司资金链断了，又欠了一屁股债，处于求生不得，求死不能的困境。 Dòng vốn của công ty bị đứt, lại nợ ngập đầu, rơi vào cảnh sống dở chết dở. 一屁股债 là nợ ngập đầu.")])

add("bullets", section="Thành ngữ 成语", title="Thành ngữ (2): 痛不欲生 · 救死扶伤 · 生不如死", size=33,
    items=["## 痛不欲生 tòngbúyùshēng – đau đớn (buồn đau) đến mức không muốn sống",
           "那些曾经失恋后痛不欲生的人，后来怎样了？",
           "## 救死扶伤 jiùsǐ-fúshāng – cứu người sắp chết, chăm sóc người bị thương",
           "医生，被人们誉为“白衣天使”，他们的职业是救死扶伤、治病救人。",
           "## 生不如死 shēngbùrúsǐ – sống không bằng chết",
           "人可以无奈地接受死亡，但很难承受生不如死的折磨！"],
    say=[F(0, "痛不欲生: 欲 là muốn. Đau đớn hay đau buồn đến mức không muốn sống nữa, chỉ nỗi đau tột cùng."),
         F(1, "Ví dụ: 那些曾经失恋后痛不欲生的人，后来怎样了？ Những người từng thất tình đau khổ đến mức không thiết sống, về sau thế nào rồi? Ý là: nỗi đau nào rồi cũng qua."),
         F(2, "救死扶伤: 扶 là đỡ, chăm sóc. Cứu chữa người nguy kịch, chăm sóc người bị thương. Nay dùng để ca ngợi tinh thần phục vụ hết lòng của nhân viên y tế."),
         F(3, "Ví dụ: 医生，被人们誉为白衣天使，他们的职业是救死扶伤、治病救人。 Bác sĩ được mọi người ca ngợi là thiên thần áo trắng, nghề của họ là cứu người, chữa bệnh."),
         F(4, "生不如死: sống còn không bằng chết, chỉ hoàn cảnh cực kỳ tồi tệ, đau đớn. Trong bài, Ba Kim phải chịu cách điều trị sống không bằng chết."),
         F(5, "Ví dụ: 人可以无奈地接受死亡，但很难承受生不如死的折磨！ Con người có thể bất lực chấp nhận cái chết, nhưng khó mà chịu nổi sự giày vò sống không bằng chết!")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 课后练习", title="Bài tập 1: Chọn từ điền vào chỗ trống", reveal=True, size=33,
    items=["## 免除 · 履行 · 无疾而终 · 痛不欲生 · 引发 · 共存",
           "(1) 如果你答应了他，就应该___自己的诺言。  (2) 人与动物、人与自然和谐___是我们的美好心愿。",
           "Đáp án: (1) 履行 · (2) 共存",
           "(3) 人们纷纷猜测___这起事故的原因。  (4) 老人的身体一直很好，90岁才___。",
           "Đáp án: (3) 引发 · (4) 无疾而终",
           "(5) 眼见儿子被敌人带走，老母亲呼天抢地，___。  (6) 由于失职，他被___了校长职务。",
           "Đáp án: (5) 痛不欲生 · (6) 免除"],
    say=["Bây giờ chúng ta sang phần luyện tập của sách. Bài tập một: chọn từ thích hợp điền vào chỗ trống. Có sáu từ: 免除，履行，无疾而终，痛不欲生，引发，共存. Thầy đọc từng cặp câu, các bạn tạm dừng để chọn nhé.",
         F(1, "Câu một: 如果你答应了他，就应该什么自己的诺言。 Nếu đã hứa với anh ấy thì phải làm gì lời hứa của mình. Câu hai: 人与动物、人与自然和谐什么是我们的美好心愿。 Con người với động vật, con người với tự nhiên hài hòa thế nào là mong ước tốt đẹp của chúng ta."),
         F(2, "Đáp án: câu một, 履行诺言, thực hiện lời hứa; câu hai, 和谐共存, chung sống hài hòa."),
         F(3, "Câu ba: 人们纷纷猜测什么这起事故的原因。 Mọi người đua nhau đoán nguyên nhân gì vụ tai nạn này. Câu bốn: 老人的身体一直很好，九十岁才什么。 Sức khỏe của cụ luôn rất tốt, chín mươi tuổi mới thế nào.",
           cap="Câu ba: 人们纷纷猜测___这起事故的原因。 Câu bốn: 老人的身体一直很好，90岁才___。"),
         F(4, "Đáp án: câu ba, 引发这起事故的原因, nguyên nhân gây ra vụ tai nạn; câu bốn, 无疾而终, mất vì tuổi già, không bệnh tật."),
         F(5, "Câu năm: 眼见儿子被敌人带走，老母亲呼天抢地，什么。 Tận mắt thấy con trai bị kẻ thù bắt đi, bà mẹ già kêu trời gào đất, thế nào. 呼天抢地 là kêu trời gào đất, chữ 抢 đọc qiāng. Câu sáu: 由于失职，他被什么了校长职务。 Vì thiếu trách nhiệm, ông ấy bị làm gì chức hiệu trưởng."),
         F(6, "Đáp án: câu năm, 痛不欲生, đau đớn không muốn sống; câu sáu, 免除职务, miễn nhiệm chức vụ, tức bị cách chức.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn từ thích hợp nhất (1)", reveal=True, size=33,
    items=["(1) 她书看得津津有味，直到外婆来催她上床的时候，才（  ）把手中的书放下。 A.顽强 B.勉强 C.强迫 D.坚强",
           "Đáp án: B 勉强 – miễn cưỡng đặt sách xuống",
           "(2) 由于（  ）砍伐，这里的森林遭到了毁灭性的破坏。 A.过渡 B.过分 C.徒劳 D.过度",
           "Đáp án: D 过度 – 过度砍伐 chặt phá quá mức",
           "(3) 很多时候，人们总想要把婚礼办得豪华（  ），为此不惜一掷千金。 A.面貌 B.体面 C.奢望 D.场面",
           "Đáp án: B 体面 – 豪华体面 sang trọng, đàng hoàng"],
    say=["Bài tập hai: chọn từ thích hợp nhất.",
         F(0, "Câu một: 她书看得津津有味，直到外婆来催她上床的时候，才什么把手中的书放下。 Cô bé đọc sách say sưa, mãi đến khi bà ngoại giục đi ngủ mới thế nào đặt quyển sách xuống. A, 顽强; B, 勉强; C, 强迫; D, 坚强."),
         F(1, "Đáp án: B, 勉强, miễn cưỡng, không muốn mà vẫn phải làm. 顽强 là ngoan cường, 坚强 là kiên cường; 强迫 là ép buộc người khác, phải có tân ngữ chỉ người."),
         F(2, "Câu hai: 由于什么砍伐，这里的森林遭到了毁灭性的破坏。 Do chặt phá thế nào, rừng ở đây bị tàn phá nặng nề. A, 过渡; B, 过分; C, 徒劳; D, 过度."),
         F(3, "Đáp án: D, 过度, quá mức, giống 过度抢救 trong bài khóa. 过渡 là quá độ, chuyển tiếp, đồng âm nhưng khác nghĩa; 过分 là quá đáng, thường nói về lời nói, hành vi đối với người khác."),
         F(4, "Câu ba: 很多时候，人们总想要把婚礼办得豪华什么，为此不惜一掷千金。 Nhiều khi, người ta luôn muốn tổ chức đám cưới thật sang trọng và thế nào, vì thế không tiếc vung tiền. A, 面貌; B, 体面; C, 奢望; D, 场面."),
         F(5, "Đáp án: B, 体面, đàng hoàng, có thể diện, là tính từ đứng sau 办得 cùng với 豪华. 面貌, 场面, 奢望 đều là danh từ. 一掷千金 là ném nghìn vàng một lúc, tức vung tiền.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn từ thích hợp nhất (2)", reveal=True, size=33,
    items=["(4) 限于资料与笔者能力有限，不足之处在所难免，（  ）各位专家学者批评指正，以求实现新的提升。 A.恳请 B.请示 C.诚恳 D.诚实",
           "Đáp án: A 恳请",
           "(5) 教材修改的工作量很大，我们忙了（  ）一个夏天。 A.满满 B.完整 C.整整 D.整个",
           "Đáp án: C 整整",
           "(6) 人家生怕对手超越了自己，可他却（  ）对手比自己强，因为战胜强手，才能证明自己。 A.巴不得 B.舍不得 C.顾不得 D.怪不得",
           "Đáp án: A 巴不得"],
    say=[F(0, "Câu bốn: 限于资料与笔者能力有限，不足之处在所难免，什么各位专家学者批评指正，以求实现新的提升。 Do tư liệu và năng lực của người viết có hạn, thiếu sót là khó tránh, làm gì các chuyên gia, học giả phê bình góp ý. A, 恳请; B, 请示; C, 诚恳; D, 诚实."),
         F(1, "Đáp án: A, 恳请, kính mong, khẩn thiết đề nghị; đây là câu khiêm tốn quen thuộc ở cuối lời nói đầu của sách. 请示 là xin chỉ thị cấp trên; 诚恳 và 诚实 là tính từ."),
         F(2, "Câu năm: 教材修改的工作量很大，我们忙了什么一个夏天。 Khối lượng công việc sửa giáo trình rất lớn, chúng tôi bận rộn thế nào một mùa hè. A, 满满; B, 完整; C, 整整; D, 整个."),
         F(3, "Đáp án: C, 整整, trọn, suốt, nhấn mạnh thời gian dài, đứng trước cụm số lượng 一个夏天. 整个 cũng có nghĩa là cả, nhưng nói 整个夏天, không có 一个."),
         F(4, "Câu sáu: 人家生怕对手超越了自己，可他却什么对手比自己强，因为战胜强手，才能证明自己。 Người ta sợ đối thủ vượt mặt mình, còn anh ấy lại thế nào đối thủ mạnh hơn mình, vì đánh bại kẻ mạnh mới chứng minh được bản thân. A, 巴不得; B, 舍不得; C, 顾不得; D, 怪不得."),
         F(5, "Đáp án: A, 巴不得, chỉ mong. 舍不得 là không nỡ; 顾不得 là không màng tới; 怪不得 là thảo nào. Bốn từ cùng có 不得, các bạn nên ghi nhớ cả nhóm.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ ngữ, mẫu câu cho sẵn trả lời câu hỏi (1)", reveal=True, size=32,
    items=["(1) 台湾知名作家琼瑶的公开信说了什么？造成了什么样的影响？（表达……的意愿，引发……热议）",
           "Đáp án gợi ý: 琼瑶在公开信中表达了选择“尊严死”的意愿：无论生什么重病，都不动大手术、不插管、不急救，只要没痛苦地死去就好。她的生死观引发了网上网下的热议。",
           "(2) 医生和家属不肯放弃治疗的理由是什么？（视……为）",
           "Đáp án gợi ý: 家属视抢救生命为“孝道”，认为无论花多大代价，都一定要让亲人活着；医生视救死扶伤为天职。"],
    say=["Bài tập ba: dùng từ ngữ và mẫu câu cho sẵn để trả lời câu hỏi về bài khóa. Thầy đưa ra đáp án gợi ý.",
         F(0, "Câu một: 台湾知名作家琼瑶的公开信说了什么？造成了什么样的影响？ Thư ngỏ của nhà văn Quỳnh Dao nói gì? Gây ra ảnh hưởng thế nào? Dùng 表达的意愿 và 引发热议."),
         F(1, "Gợi ý: 琼瑶在公开信中表达了选择尊严死的意愿：无论生什么重病，都不动大手术、不插管、不急救，只要没痛苦地死去就好。她的生死观引发了网上网下的热议。 Trong thư ngỏ, Quỳnh Dao bày tỏ mong muốn được chết có tôn nghiêm; quan niệm sống chết của bà gây bàn luận sôi nổi trên mạng và ngoài đời."),
         F(2, "Câu hai: 医生和家属不肯放弃治疗的理由是什么？ Lý do bác sĩ và người nhà không chịu từ bỏ điều trị là gì? Dùng 视为."),
         F(3, "Gợi ý: 家属视抢救生命为孝道，认为无论花多大代价，都一定要让亲人活着；医生视救死扶伤为天职。 Người nhà coi cấp cứu là đạo hiếu, cho rằng bằng mọi giá phải giữ người thân sống; bác sĩ coi cứu người là thiên chức.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ ngữ, mẫu câu cho sẵn trả lời câu hỏi (2)", reveal=True, size=32,
    items=["(3) 没有尊严的生命延续等同于什么？（即便……也，无异于……）",
           "Đáp án gợi ý: 徒劳的过度抢救只会增加病人的痛苦，即便生命在延续，也是没有尊严的，这无异于对亲人的“凌迟”。",
           "(4) “尊严死”的目标是什么呢？（不把……而是将）",
           "Đáp án gợi ý: “尊严死”不把挽救生命作为首选，而是将无痛、无惧、无憾地离世作为目标，让“生死两相憾”变成“生死两相安”。"],
    say=[F(0, "Câu ba: 没有尊严的生命延续等同于什么？ Sự kéo dài sự sống không có tôn nghiêm thì tương đương với điều gì? Dùng 即便也 và 无异于."),
         F(1, "Gợi ý: 徒劳的过度抢救只会增加病人的痛苦，即便生命在延续，也是没有尊严的，这无异于对亲人的凌迟。 Cấp cứu quá mức vô ích chỉ làm tăng đau đớn, dù sự sống được kéo dài cũng không có tôn nghiêm, chẳng khác gì lăng trì người thân."),
         F(2, "Câu bốn: 尊严死的目标是什么呢？ Mục tiêu của chết có tôn nghiêm là gì? Dùng 不把，而是将."),
         F(3, "Gợi ý: 尊严死不把挽救生命作为首选，而是将无痛、无惧、无憾地离世作为目标，让生死两相憾变成生死两相安。 Không đặt việc cứu vãn sự sống lên hàng đầu, mà lấy việc ra đi không đau, không sợ, không tiếc làm mục tiêu, để kẻ ở người đi đều yên lòng.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Chọn từ điền vào đoạn văn", reveal=True, size=34,
    items=["## 短暂 · 体面 · 共存 · 谢幕 · 舵手 · 奢望",
           "死亡也许只是一个___的瞬间，但与疾病___则是一个长期的过程。尊重患者的生命自主权，并非鼓励放弃治疗，而是要让临终者___而有尊严地离开人世。生是偶然，死是必然。如果说生命是一条航船，每个人都是这条航船的___。让生命完美地___，不应成为一种___。",
           "Đáp án: 短暂 · 共存 · 体面 · 舵手 · 谢幕 · 奢望"],
    say=["Bài tập bốn: chọn từ điền vào đoạn văn. Có sáu từ: 短暂，体面，共存，谢幕，舵手，奢望.",
         F(1, "死亡也许只是一个什么的瞬间，但与疾病什么则是一个长期的过程。尊重患者的生命自主权，并非鼓励放弃治疗，而是要让临终者什么而有尊严地离开人世。生是偶然，死是必然。如果说生命是一条航船，每个人都是这条航船的什么。让生命完美地什么，不应成为一种什么。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 短暂的瞬间；与疾病共存；体面而有尊严地；航船的舵手；完美地谢幕；一种奢望。"),
         F(2, "Đây chính là đoạn cuối của bài khóa. Gợi ý: 短暂 đối lập với 长期; 体面 đi đôi với 有尊严; 航船 đi với 舵手. Hãy học thuộc lòng đoạn văn đẹp này nhé.")])

add("bullets", chapter="Liên hệ: chữ hiếu & quyền của người bệnh", section="Thảo luận 讨论", title="Liên hệ Việt Nam: chữ hiếu và quyền tự quyết của người bệnh", size=33,
    items=["Người Việt cũng mong “sống lâu chết lành”, muốn được mất tại nhà ≈ 寿终正寝; nhiều gia đình đưa người thân hấp hối về nhà",
           "Chữ hiếu: nhiều gia đình cố cứu chữa đến cùng, giấu bệnh với người già ≈ 视抢救生命为孝道",
           "Luật Khám bệnh, chữa bệnh: người bệnh có quyền được thông tin và quyền từ chối điều trị; an tử chưa được phép ở Việt Nam",
           "Chăm sóc giảm nhẹ (缓和医疗) đang dần phát triển ở các bệnh viện lớn",
           "Câu hỏi: 如果你的亲人想要放弃治疗，你会尊重他的选择吗？为什么？"],
    say=["Trước khi sang phần ôn tập đơn vị, chúng ta cùng liên hệ với Việt Nam.",
         F(0, "Người Việt hay chúc nhau sống lâu chết lành, và nhiều người mong được trút hơi thở cuối cùng tại nhà, bên con cháu, rất giống 寿终正寝 của người Trung Quốc. Vì thế, nhiều gia đình đưa người thân đang hấp hối từ bệnh viện về nhà."),
         F(1, "Chữ hiếu cũng khiến nhiều gia đình Việt Nam giống những người con trong bài: cố cứu chữa đến cùng, thậm chí giấu bệnh tình với ông bà, cha mẹ, vì sợ họ suy sụp. Điều này ngược hẳn với nguyên tắc 告知患者本人 trong luật của Đài Loan."),
         F(2, "Về pháp luật, Luật Khám bệnh, chữa bệnh của Việt Nam quy định người bệnh có quyền được thông tin về bệnh tình và có quyền từ chối điều trị. Còn an tử thì hiện chưa được pháp luật Việt Nam cho phép."),
         F(3, "Chăm sóc giảm nhẹ, tức 缓和医疗, giúp người bệnh giai đoạn cuối bớt đau đớn, đang dần phát triển ở các bệnh viện lớn, đặc biệt là các bệnh viện ung bướu."),
         F(4, "Câu hỏi cho các bạn: 如果你的亲人想要放弃治疗，你会尊重他的选择吗？为什么？ Nếu người thân của bạn muốn từ bỏ điều trị, bạn có tôn trọng lựa chọn của họ không? Vì sao? Đây là câu hỏi khó, không có đáp án đúng sai. Hãy thử trả lời bằng tiếng Trung, dùng 视为, 巴不得, 与共存 nhé.")])

# ======================= ÔN TẬP ĐƠN VỊ =======================
add("bullets", chapter="Ôn tập đơn vị 8", section="Ôn tập đơn vị 单元练习", title="Ôn tập Đơn vị 8: 单元练习 “学以致用”", size=33,
    items=["一、众说纷纭: vụ 敬汉卿 bị đăng ký mất tên mình làm nhãn hiệu · bàn về 山寨产品",
           "二、对簿公堂: xem video phiên tòa – tranh chấp sáng chế · 《哪吒之魔童降世》 bị kiện đòi 50 triệu tệ",
           "三、明察暗访: tìm hiểu một vụ án ở nước mình · khảo sát ý kiến về 尊严死 / 安乐死",
           "四、模拟法庭: phiên tòa giả định – vụ “an tử” đầu tiên ở Trung Quốc (1986)",
           "五、针锋相对: 3 đề tranh biện   六、妙笔生花: 我的死亡谁做主 (≥ 800 chữ)",
           "七、生前预嘱: điền thử “我的五个愿望” – năm mong muốn cuối đời"],
    say=["Bây giờ chúng ta sang chương ôn tập Đơn vị tám. Sách có phần bài tập tổng hợp mang tên 学以致用, học để vận dụng, gồm bảy phần, nối kết cả ba bài: nhãn hiệu, bằng sáng chế, và quyền ra đi thanh thản.",
         F(0, "Phần một, 众说纷纭, mỗi người một ý: bàn về vụ một Youtuber của trang Bilibili bị đăng ký mất chính tên mình làm nhãn hiệu, và bàn về hàng nhái, 山寨产品."),
         F(1, "Phần hai, 对簿公堂, ra tòa: xem video ghi lại phiên tòa về tranh chấp sáng chế, và vụ phim hoạt hình 哪吒之魔童降世, Na Tra giáng thế, bị kiện đòi bồi thường năm mươi triệu tệ."),
         F(2, "Phần ba, 明察暗访, điều tra: tìm hiểu một vụ án nổi tiếng ở nước mình, và làm khảo sát ý kiến về chết có tôn nghiêm, an tử."),
         F(3, "Phần bốn, 模拟法庭, phiên tòa giả định, dựa trên vụ an tử đầu tiên ở Trung Quốc năm một nghìn chín trăm tám mươi sáu."),
         F(4, "Phần năm, 针锋相对, có ba đề tranh biện; phần sáu, 妙笔生花, viết bài văn ít nhất tám trăm chữ với đề 我的死亡谁做主, cái chết của tôi ai làm chủ."),
         F(5, "Phần bảy, 生前预嘱: điền thử bản 我的五个愿望, năm mong muốn của tôi, một mẫu chỉ thị trước về y tế. Thầy sẽ chọn những phần tiêu biểu nhất để chúng ta cùng làm.")])

add("bullets", section="Ôn tập đơn vị 单元练习", title="众说纷纭: 敬汉卿商标维权事件", reveal=True, size=32,
    items=["Tóm tắt: 8/2019, “up主” nổi tiếng của B站 敬汉卿 phát hiện tên mình bị công ty 知桥 抢注 làm nhãn hiệu, bị yêu cầu đổi tên; 国资委、共青团中央 lên tiếng, B站 hỗ trợ pháp lý → 维权",
           "(1) 谈谈你对敬汉卿商标维权事件的认识。",
           "Đáp án gợi ý: 恶意抢注别人的名字是傍名人、蹭热度的行为，理应被法律否决；敬汉卿勇敢维权，也提高了大家的知识产权意识。",
           "(2) 维权既耗时又耗财，遇到这种事情，你会选择隐忍沉默还是站出来？理由是什么？",
           "Đáp án gợi ý: 我会站出来。如果大家都忍气吞声，侵权的人就会有恃无恐；与其沉默，不如拿起法律的武器保护自己。"],
    say=["Đề thảo luận tiêu biểu nhất của phần mỗi người một ý: vụ bảo vệ quyền nhãn hiệu của 敬汉卿.",
         F(0, "Tóm tắt: tháng tám năm hai nghìn không trăm mười chín, 敬汉卿, một người làm video nổi tiếng trên trang Bilibili, phát hiện tên thật của mình đã bị công ty 知桥 đăng ký chặn trước làm nhãn hiệu, và anh bị yêu cầu không được dùng tên mình nữa. Sự việc ngày càng ồn ào, cả 国资委 và 共青团中央 cũng lên tiếng, Bilibili tuyên bố hỗ trợ pháp lý cho anh. 维权 là bảo vệ quyền lợi."),
         F(1, "Câu hỏi một: 谈谈你对敬汉卿商标维权事件的认识。 Hãy nói nhận thức của bạn về vụ này."),
         F(2, "Gợi ý: 恶意抢注别人的名字是傍名人、蹭热度的行为，理应被法律否决；敬汉卿勇敢维权，也提高了大家的知识产权意识。 Ác ý đăng ký chặn trước tên người khác là hành vi bám người nổi tiếng, ăn theo độ hot, lẽ ra phải bị pháp luật bác bỏ; việc anh dũng cảm bảo vệ quyền lợi cũng nâng cao ý thức sở hữu trí tuệ của mọi người. Các bạn thấy không, câu trả lời dùng lại rất nhiều từ của bài tám chấm một."),
         F(3, "Câu hỏi hai: 维权既耗时又耗财，遇到这种事情，你会选择隐忍沉默还是站出来？理由是什么？ Bảo vệ quyền lợi vừa tốn thời gian vừa tốn tiền, gặp chuyện này bạn sẽ nhịn và im lặng, hay đứng ra? Vì sao?"),
         F(4, "Gợi ý: 我会站出来。如果大家都忍气吞声，侵权的人就会有恃无恐；与其沉默，不如拿起法律的武器保护自己。 Tôi sẽ đứng ra. Nếu ai cũng nhịn nhục, kẻ xâm phạm sẽ chẳng sợ gì; thay vì im lặng, chi bằng cầm vũ khí pháp luật bảo vệ mình. Câu này dùng thành ngữ và mẫu câu của bài tám chấm hai.")])

add("bullets", section="Ôn tập đơn vị 单元练习", title="明察暗访: từ ngữ để kể một vụ án", size=32,
    items=["## Nhân vật: 原告 nguyên đơn · 被告 bị đơn, bị cáo · 被害人 người bị hại · 当事人 đương sự · 委托代理人 người đại diện theo ủy quyền · 审判长 chủ tọa · 陪审员 hội thẩm",
           "Án gì: 一起……诉讼 / ……纠纷 vụ tranh chấp · 故意伤害案 vụ cố ý gây thương tích · 诈骗案 vụ lừa đảo",
           "Diễn biến: 一开始 / 起初 / 起先 → 其后 / 随后 / 随之 → 最终 · 经……鉴定 · 调查发现……",
           "Mấu chốt: 本案焦点在于…… điểm mấu chốt của vụ án là…",
           "Tố tụng, kết quả: 提起诉讼 · 公诉 · 开庭审理 · 驳回 · 胜诉 / 败诉 · 构成…… · 判决 · 判处 · 有期徒刑 · 无期徒刑 · 无罪释放"],
    say=["Phần 明察暗访 yêu cầu lên mạng tìm một vụ án nổi tiếng ở nước mình và giới thiệu với bạn học. Sách đưa ra một bảng từ ngữ rất hữu ích để kể một vụ án. Các bạn hãy ghi lại nhé.",
         F(0, "Về nhân vật: 原告, nguyên đơn; 被告, bị đơn hoặc bị cáo; 被害人, người bị hại; 当事人, đương sự; 委托代理人, người đại diện theo ủy quyền, thường là luật sư; 审判长, chủ tọa phiên tòa; 陪审员, hội thẩm."),
         F(1, "Về loại án: 一起什么诉讼, một vụ kiện về việc gì; 什么纠纷, vụ tranh chấp gì; 故意伤害案, vụ cố ý gây thương tích; 诈骗案, vụ lừa đảo."),
         F(2, "Về diễn biến: mở đầu dùng 一开始，起初，起先; tiếp theo dùng 其后，随后，随之; kết thúc dùng 最终. Ngoài ra còn 经鉴定, qua giám định; 调查发现, điều tra phát hiện."),
         F(3, "Điểm mấu chốt: 本案焦点在于, điểm mấu chốt của vụ án này nằm ở."),
         F(4, "Về tố tụng và kết quả: 提起诉讼, khởi kiện; 公诉, công tố; 开庭审理, mở phiên tòa xét xử; 驳回, bác bỏ; 胜诉, 败诉, thắng kiện, thua kiện; 构成, cấu thành tội gì; 判决, tuyên án; 判处, xử phạt; 有期徒刑, tù có thời hạn; 无期徒刑, tù chung thân; 无罪释放, tuyên vô tội và trả tự do. Với bảng từ này, các bạn có thể kể bất kỳ vụ án nào bằng tiếng Trung.")])

add("bullets", section="Ôn tập đơn vị 单元练习", title="模拟法庭: 我国首例“安乐死”案始末", reveal=True, size=31,
    items=["1986, 汉中: bà 夏素文 xơ gan nặng, nhiều lần hôn mê; con trai 王明成 xin bác sĩ 蒲连升 “an tử” cho mẹ → bác sĩ kê 100mg 复方冬眠灵, bà mất ngày 29/6",
           "检察院 truy tố hai người tội 故意杀人; 最高人民法院: “安乐死的定性问题有待立法解决” → 1991 một审宣告无罪; 1992 二审 bác kháng nghị, kháng cáo, giữ nguyên",
           "(1) 请你谈谈对这个案件的看法。",
           "Đáp án gợi ý: 我认为法院的判决比较合理：王明成是出于孝心，不忍心让母亲再受折磨，并没有杀人的恶意；但这个案件也说明，安乐死必须先有明确的法律规定。",
           "(2) “安乐死”应该如何定性，才能保障各方的利益？",
           "Đáp án gợi ý: 应该通过立法明确条件和程序：只适用于不可治愈的末期病人，必须由病人本人清醒时提出，经过多位医生鉴定，防止被滥用。"],
    say=["Phần mô phỏng phiên tòa dựa trên một vụ án có thật: vụ an tử đầu tiên ở Trung Quốc.",
         F(0, "Đầu năm một nghìn chín trăm tám mươi sáu, ở thành phố Hán Trung, tỉnh Thiểm Tây, bà 夏素文 bị xơ gan nặng, nhiều lần hôn mê. Bác sĩ nói không còn hy vọng chữa trị. Con trai bà là 王明成 không nỡ để mẹ chịu đau đớn thêm, đã nhiều lần đề nghị bác sĩ 蒲连升 thực hiện an tử. Cuối cùng bác sĩ kê một trăm mi-li-gam thuốc an thần, y tá tiêm cho bà, và bà qua đời rạng sáng ngày hai mươi chín tháng sáu."),
         F(1, "Viện kiểm sát truy tố hai người về tội cố ý giết người. Tòa án Nhân dân Tối cao trả lời rằng: 安乐死的定性问题有待立法解决, vấn đề định tính an tử cần chờ lập pháp giải quyết. Năm một nghìn chín trăm chín mươi mốt, tòa sơ thẩm tuyên hai người vô tội; năm một nghìn chín trăm chín mươi hai, tòa phúc thẩm bác cả kháng nghị của viện kiểm sát lẫn kháng cáo của hai bị cáo, giữ nguyên bản án."),
         F(2, "Câu hỏi một: 请你谈谈对这个案件的看法。 Hãy nói ý kiến của bạn về vụ án này."),
         F(3, "Gợi ý: 我认为法院的判决比较合理：王明成是出于孝心，不忍心让母亲再受折磨，并没有杀人的恶意；但这个案件也说明，安乐死必须先有明确的法律规定。 Tôi cho rằng phán quyết khá hợp lý: người con xuất phát từ lòng hiếu thảo, không nỡ để mẹ chịu giày vò, không có ác ý giết người; nhưng vụ án cũng cho thấy an tử phải có quy định pháp luật rõ ràng trước đã."),
         F(4, "Câu hỏi hai: 安乐死应该如何定性，才能保障各方的利益？ An tử nên được định tính thế nào để bảo đảm lợi ích của người bệnh, gia đình, bệnh viện và xã hội?"),
         F(5, "Gợi ý: 应该通过立法明确条件和程序：只适用于不可治愈的末期病人，必须由病人本人清醒时提出，经过多位医生鉴定，防止被滥用。 Nên lập pháp quy định rõ điều kiện và thủ tục: chỉ áp dụng cho bệnh nhân giai đoạn cuối không thể chữa khỏi, phải do chính người bệnh đề nghị khi còn tỉnh táo, qua giám định của nhiều bác sĩ, để tránh bị lạm dụng.")])

add("bullets", section="Ôn tập đơn vị 单元练习", title="针锋相对 · 妙笔生花 · 生前预嘱", size=32,
    items=["## 针锋相对 – 3 đề tranh biện",
           "你认为疫苗应该放弃专利吗？ · 你认为仿制药的存在有合理性吗？（电影《我不是药神》）",
           "痛苦的绝症病人想要放弃自己的生命，我该不该鼓励他撑下去？",
           "## 妙笔生花: 我的死亡谁做主 – viết văn ≥ 800 chữ, tự đặt tên bài",
           "## 生前预嘱 “我的五个愿望”",
           "我要或不要什么医疗服务 · 我希望使用或不使用生命支持治疗 · 我希望别人怎么对待我 · 我想让我的家人和朋友知道什么 · 我希望谁帮助我"],
    say=["Phần cuối của chương ôn tập: tranh biện, viết và chỉ thị trước về y tế.",
         F(0, "Sách đưa ra ba đề tranh biện, mỗi đề gắn với một bài."),
         F(1, "Đề một: 你认为疫苗应该放弃专利吗？ Bạn có cho rằng vắc-xin nên từ bỏ bằng sáng chế không? Đây là cuộc tranh luận ở Tổ chức Thương mại Thế giới thời dịch COVID. Đề hai: 你认为仿制药的存在有合理性吗？ Thuốc generic, tức thuốc phỏng chế, có hợp lý không? Bộ phim 我不是药神, Tôi không phải thần dược, kể chính câu chuyện này."),
         F(2, "Đề ba: 痛苦的绝症病人想要放弃自己的生命，我该不该鼓励他撑下去？ Người bệnh nan y đau đớn muốn buông bỏ, tôi có nên động viên họ cố gắng tiếp không? 撑下去 là gắng gượng tiếp."),
         F(3, "Phần viết: 我的死亡谁做主, cái chết của tôi ai làm chủ. Hãy viết một bài văn ít nhất tám trăm chữ, nêu quan điểm về sự sống và cái chết, tự đặt tên bài. Các bạn có thể theo bố cục luận điểm, thực trạng, giải pháp, kết luận của bài khóa."),
         F(4, "Cuối cùng là bản 我的五个愿望, năm mong muốn của tôi, do trang web 选择与尊严, Lựa chọn và Tôn nghiêm, ở Bắc Kinh soạn ra. Ai cũng có thể tự nguyện điền và sửa bất cứ lúc nào."),
         F(5, "Năm mong muốn là: tôi muốn hay không muốn dịch vụ y tế nào; tôi muốn dùng hay không dùng biện pháp duy trì sự sống; tôi mong người khác đối xử với tôi thế nào; tôi muốn người thân và bạn bè biết điều gì; và tôi mong ai giúp tôi. Đọc bản này cũng là một cách học rất nhiều từ ngữ y tế đấy.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết", section="Tổng kết", title="Tổng kết bài 8.3 và Đơn vị 8", size=32,
    items=["Từ vựng bài 8.3: 善终 · 嘱咐 · 勉强 · 躯壳 · 引发 · 临近 · 孝道 · 天职 · 徒劳 · 熬 · 巴不得 · 折磨 · 临终 · 遗愿 · 恳请 · 创伤 · 治愈 · 挽救 · 知情 · 履行 · 免除 · 体面 · 谢幕 · 奢望",
           "Mẫu câu: 谓之 · 视……为 · 整整 · 巴不得 · 我的……我做主 · 把……作为首选 · 与……共存",
           "Thành ngữ: 寿终正寝 · 无疾而终 · 求生不得，求死不能 · 痛不欲生 · 救死扶伤 · 生不如死",
           "## Đơn vị 8 · 法律篇: ba bài, ba quyền",
           "8.1 商标权 – đừng “傍大牌” · 8.2 专利权 – chống 垄断 · 8.3 善终权 – 我的死亡我做主"],
    say=["Chúng ta cùng tổng kết bài tám chấm ba, và cũng là tổng kết Đơn vị tám.",
         F(0, "Về từ vựng bài tám chấm ba, các bạn cần đặc biệt nhớ: 善终，嘱咐，勉强，躯壳，引发，临近，孝道，天职，徒劳，熬，巴不得，折磨，临终，遗愿，恳请，创伤，治愈，挽救，知情，履行，免除，体面，谢幕，奢望. Nhớ cách đọc 躯壳, 勉强, 创伤 nhé."),
         F(1, "Về mẫu câu: 谓之 là gọi là; 视为 là coi là; 整整 là trọn, suốt; 巴不得 là chỉ mong; 我的我做主 là của tôi tôi làm chủ; 把作为首选 là chọn làm ưu tiên hàng đầu; và 与共存 là cùng tồn tại."),
         F(2, "Về thành ngữ: 寿终正寝，无疾而终，求生不得求死不能，痛不欲生，救死扶伤，生不如死. Đều là những thành ngữ về sống và chết."),
         F(3, "Và nhìn lại cả Đơn vị tám, chủ đề Pháp luật: ba bài, ba quyền."),
         F(4, "Bài tám chấm một nói về quyền nhãn hiệu: đừng bám thương hiệu lớn, phải nói không với ác ý đăng ký chặn trước. Bài tám chấm hai nói về quyền sáng chế: bảo hộ sáng chế để khuyến khích đổi mới, nhưng phải chống độc quyền. Bài tám chấm ba nói về quyền được ra đi thanh thản. Cả ba bài đều cho thấy: pháp luật tồn tại để bảo vệ quyền lợi chính đáng của mỗi con người."),
         "Bài tập về nhà: hãy viết bài văn với đề 我的死亡谁做主, hoặc chọn một đề tranh biện trong phần ôn tập, viết khoảng năm trăm chữ, dùng ít nhất năm thành ngữ và ba mẫu câu của đơn vị."])

add("bullets", chapter="Lời kết giáo trình", section="Lời kết", title="Hoàn thành giáo trình 顶石中文!", size=34,
    items=["8 đơn vị · 24 bài: 教育 · 时代 · … · 家庭 · 职场 · 经济 · 法律",
           "Hàng nghìn từ mới, hàng trăm mẫu câu và thành ngữ của tiếng Trung báo chí, nghị luận",
           "Tiếp tục: đọc báo Trung Quốc mỗi ngày · luyện viết bài nghị luận · tranh biện bằng tiếng Trung",
           "学无止境 – học không có điểm dừng"],
    say=["Và đây là slide cuối cùng của bài, cũng là slide cuối cùng của cả giáo trình 顶石中文.",
         F(0, "Chúng ta đã cùng nhau đi qua tám đơn vị, hai mươi bốn bài, bàn về giáo dục, thời đại, gia đình, nơi làm việc, kinh tế, và hôm nay là pháp luật. Mỗi bài là một vấn đề nóng của xã hội Trung Quốc hiện đại."),
         F(1, "Các bạn đã học hàng nghìn từ mới, hàng trăm mẫu câu và thành ngữ của tiếng Trung báo chí và nghị luận, thứ tiếng Trung mà người Trung Quốc dùng để bàn luận những vấn đề nghiêm túc nhất."),
         F(2, "Để không quên những gì đã học, hãy đọc báo Trung Quốc mỗi ngày, luyện viết bài nghị luận, và nếu có thể, hãy thử tranh biện bằng tiếng Trung với bạn bè."),
         F(3, "Người Trung Quốc có câu 学无止境, học không có điểm dừng. Đỉnh cao tiếng Trung, 顶石, không phải là điểm kết thúc, mà là viên đá để các bạn bước lên những đỉnh cao mới."),
         "Cảm ơn các bạn đã kiên trì theo dõi bài giảng suốt chặng đường dài này. Xin chúc mừng các bạn đã hoàn thành giáo trình 顶石中文! Chúc các bạn học tốt, và hẹn gặp lại!"])

lesson = {
    "title": "顶石中文 – Bài 8.3: 善终也是一种权利 (Ra đi thanh thản cũng là một quyền)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"勉强": "勉抢",              # miǎnqiǎng
                    "躯壳": "躯俏",              # qūqiào
                    "动弹": "动谈",              # dòngtan
                    "熬": "遨",                  # áo (mọi chỗ trong bài đều đọc áo)
                    "创伤": "窗伤",              # chuāngshāng
                    "为孝道": "维孝道",          # shì … wéi
                    "为天职": "维天职",          # wéi
                    "为挚友": "维挚友",          # wéi
                    "为知己": "维知己",          # wéi
                    "为自己的终生事业": "维自己的终生事业",  # wéi
                    "称为": "称维",              # chēngwéi
                    "处于": "楚于",              # chǔyú
                    "判处": "判楚",              # pànchǔ
                    "乐队": "月队",              # yuèduì
                    "呼天抢地": "呼天枪地",      # hū tiān qiāng dì
                    "应付": "映付"},             # yìngfu
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds83.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
