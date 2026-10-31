#!/usr/bin/env python3
"""Kịch bản bài giảng 顶石中文 – Bài 2.1 «融不进的城市，回不去的农村». Chạy để sinh ds21.json."""
import json
import os

TAG = "顶石中文 · Bài 2.1 · 融不进的城市，回不去的农村"
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
    zh="融不进的城市", py="回不去的农村",
    vi="Bài 2.1: Phố không hòa nhập, quê chẳng thể về",
    sub="Róng bu jìn de chéngshì, huí bu qù de nóngcūn\nBài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng giáo trình 顶石中文, Đỉnh cao tiếng Trung, giáo trình tổng hợp tiếng Trung cao cấp.",
         "Hôm nay chúng ta bước sang Đơn vị hai: 时代篇, chủ đề Thời đại. Bài đầu tiên của đơn vị là bài hai chấm một: 融不进的城市，回不去的农村。 Nghĩa là: Thành phố không hòa nhập được, nông thôn không quay về được.",
         "Bài khóa là một bài báo xã hội của trang tin 中国新闻网, viết về 新生代农民工, tức lớp lao động nhập cư thế hệ mới: những người trẻ sinh sau năm một nghìn chín trăm tám mươi, rời làng quê lên thành phố làm việc, nhưng mãi vẫn chưa thật sự trở thành người thành phố.",
         "Họ đứng giữa hai thế giới: thành phố thì chưa đón nhận họ, còn làng quê thì họ đã không muốn, và cũng không thể quay về. Hiện tượng này người Việt chúng ta cũng rất quen thuộc, với hàng triệu lao động từ các tỉnh đổ về Hà Nội, Thành phố Hồ Chí Minh hay các khu công nghiệp."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài báo: hoàn cảnh và nỗi khó xử của lao động nhập cư thế hệ mới",
           "Nắm vững 55 từ mới và thành ngữ, kèm âm Hán Việt và ví dụ",
           "Câu mẫu trọng điểm: （以）……居多 · 纵然……也…… · ……固然……，可是…… · 不复 · 况且 · 被/为……所 · V准 · 这样一来",
           "Kết hợp từ (词语搭配): 承载 · 匆匆 · 薄弱 · 不争的 · 破解 · 接纳 · 日益 · 纳入 · 遭受",
           "Luyện tập theo sách và thảo luận, liên hệ với Việt Nam"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài báo: lao động nhập cư thế hệ mới là ai, vì sao họ không hòa nhập được vào thành phố, vì sao họ không muốn về nông thôn, và xã hội cần làm gì."),
         F(1, "Thứ hai, nắm vững năm mươi lăm từ mới và thành ngữ. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học tám câu mẫu trọng điểm của sách, như 以……居多, chiếm đa số; 纵然……也……, dù cho… cũng…; 固然, đành rằng; và 这样一来, như vậy thì."),
         F(3, "Thứ tư, học cách kết hợp từ, tức là một từ hay đi với những từ nào, như 承载回忆，破解难题，遭受歧视. Đây là phần rất quan trọng ở trình độ cao cấp."),
         F(4, "Thứ năm, làm toàn bộ bài tập của sách, rồi cùng thảo luận và liên hệ với thực tế Việt Nam. Các bạn chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé.")])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 课前思考", title="Câu hỏi trước bài (课前思考)", size=40,
    items=["1. 你喜欢住在城市还是农村？为什么？",
           "2. 你们国家城乡居民的差别大吗？体现在哪些方面？",
           "3. 政府是否有责任缩小区域间发展的不平衡？",
           "Gợi ý: thu nhập · nhà ở · trường học · bệnh viện · cơ hội việc làm · bảo hiểm xã hội"],
    say=["Mỗi bài trong giáo trình 顶石 đều mở đầu bằng phần 课前思考, suy nghĩ trước khi học. Chúng ta cùng đọc ba câu hỏi.",
         F(0, "Câu một: 你喜欢住在城市还是农村？为什么？ Bạn thích sống ở thành phố hay nông thôn? Vì sao?"),
         F(1, "Câu hai: 你们国家城乡居民的差别大吗？体现在哪些方面？ Ở nước bạn, sự khác biệt giữa cư dân thành thị và nông thôn có lớn không? Thể hiện ở những mặt nào? 城乡 là thành thị và nông thôn, 体现 là thể hiện."),
         F(2, "Câu ba: 政府是否有责任缩小区域间发展的不平衡？ Chính phủ có trách nhiệm thu hẹp sự phát triển không cân bằng giữa các vùng hay không? 缩小 là thu nhỏ, thu hẹp; 区域 là khu vực, vùng."),
         F(3, "Khi trả lời, các bạn có thể nghĩ đến thu nhập, nhà ở, trường học cho con, bệnh viện, cơ hội việc làm và bảo hiểm xã hội. Đây cũng chính là những vấn đề mà bài khóa sẽ nhắc đến. Các bạn tạm dừng video, thử trả lời bằng tiếng Trung nhé.")])

add("bullets", section="Khởi động 课前思考", title="Bối cảnh (注释): 农民工 là ai?", size=36,
    items=["## 农民工一代 – thế hệ lao động nhập cư thứ nhất",
           "Từ thập niên 1980, nông thôn thực hiện khoán hộ gia đình (家庭承包经营), dư lao động → một bộ phận nông dân lên thành phố làm thuê (打工)",
           "## 新生代农民工 – lao động nhập cư thế hệ mới",
           "Sinh từ năm 1980 trở về sau · làm việc phi nông nghiệp ở thành phố từ 6 tháng trở lên · sống thường xuyên ở thành phố nhưng hộ khẩu (户籍) ở nông thôn",
           "Sách gọi họ là 新时代的产业工人 – công nhân công nghiệp của thời đại mới"],
    say=["Trước khi học từ mới, chúng ta cần hiểu một khái niệm then chốt của bài: 农民工. Chữ đầu và chữ hai là nông dân, chữ cuối là công nhân: 农民工 là người có thân phận nông dân nhưng lên thành phố làm công nhân, làm thuê. Tiếng Việt thường gọi là lao động nhập cư, hay lao động từ nông thôn ra thành phố.",
         F(0, "Theo chú thích của sách, có hai thế hệ. Thế hệ thứ nhất gọi là 农民工一代."),
         F(1, "Từ những năm tám mươi của thế kỷ trước, nông thôn Trung Quốc thực hiện chế độ khoán sản phẩm đến hộ gia đình, 家庭承包经营. Năng suất tăng lên, lao động bị dư thừa, nên một bộ phận nông dân rời làng lên thành phố làm thuê, 打工."),
         F(2, "Thế hệ thứ hai là 新生代农民工, lao động nhập cư thế hệ mới. 新生代 nghĩa là thế hệ mới sinh ra."),
         F(3, "Đó là những người sinh từ năm một nghìn chín trăm tám mươi trở về sau, lên thành phố làm công việc phi nông nghiệp từ sáu tháng trở lên, sống thường xuyên ở thành phố, nhưng hộ khẩu, 户籍, vẫn ở nông thôn. Chính chiếc hộ khẩu này khiến họ khó được hưởng phúc lợi như người thành phố."),
         F(4, "Sách gọi họ là 新时代的产业工人, những công nhân công nghiệp của thời đại mới. Bài khóa hôm nay sẽ kể về nỗi khó xử của chính thế hệ này.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("庄稼人", "zhuāngjiarén", "trang giá nhân", "danh từ", "người làm ruộng, nông dân", "他是个地地道道的庄稼人。", "Ông ấy là một người nông dân chính hiệu.",
     "Danh từ, nghĩa là người trồng trọt, người làm ruộng, tức nông dân, mang sắc thái khẩu ngữ, mộc mạc. 庄稼 là cây trồng ngoài đồng, như lúa, ngô; chữ thứ hai đọc nhẹ. Bài khóa mở đầu bằng câu 他们，是一群跨入工业文明的庄稼人的后代, họ là con cháu của những người nông dân đã bước vào nền văn minh công nghiệp."),
    ("游离", "yóulí", "du ly", "động từ", "tách rời, lơ lửng, không gắn bó với tập thể", "人无法游离于社会之外。", "Con người không thể tách mình ra khỏi xã hội.",
     "Động từ, nghĩa gốc là tách ra, tách rời; nghĩa bóng là lơ lửng bên ngoài một tập thể, không nương tựa vào đâu. Mẫu hay gặp: 游离于……之外, đứng ngoài cái gì; 游离在A和B之间, lơ lửng giữa A và B, như trong bài: 游离在城市和农村之间."),
    ("边缘化", "biānyuánhuà", "biên duyên hóa", "động từ", "bị đẩy ra bên lề", "在城市化的过程当中，本土语言正逐渐被边缘化。", "Trong quá trình đô thị hóa, tiếng địa phương đang dần bị đẩy ra bên lề.",
     "Động từ, nghĩa là rời khỏi trung tâm, bị đẩy ra phía rìa. 边缘 là mép, rìa, bên lề; hậu tố 化 nghĩa là hóa, trở thành. Thường dùng với 被: 被边缘化, bị gạt ra bên lề. Trong bài: 面临边缘化的群体, một nhóm người đang đứng trước nguy cơ bị gạt ra bên lề xã hội."),
    ("涌入", "yǒngrù", "dũng nhập", "động từ", "ồ ạt đổ vào, tràn vào", "一批批的人潮涌入会场。", "Từng đợt người ồ ạt tràn vào hội trường.",
     "Động từ, nghĩa là ồ ạt đi vào với số lượng lớn, như nước dâng tràn vào. Chữ 涌 là nước trào lên, cuộn lên. Trong bài: 他们陆续涌入大大小小的城市——在原本不属于他们的高楼大厦间寻梦, họ lần lượt đổ về các thành phố lớn nhỏ, đi tìm giấc mơ giữa những tòa cao ốc vốn không thuộc về họ. 高楼大厦 là thành ngữ, nghĩa là nhà cao cửa rộng, những tòa nhà cao tầng; chữ 厦 ở đây đọc shà."),
    ("繁华", "fánhuá", "phồn hoa", "tính từ", "phồn hoa, sầm uất", "王府井是北京繁华的商业街。", "Vương Phủ Tỉnh là con phố thương mại sầm uất của Bắc Kinh.",
     "Tính từ, nghĩa là phồn hoa, sầm uất, náo nhiệt, nói về thành phố, phố xá. Âm Hán Việt và nghĩa giống tiếng Việt: chốn phồn hoa đô hội. Trong bài: 繁华的大都市, đô thị lớn phồn hoa."),
    ("变身", "biànshēn", "biến thân", "động từ", "biến thành, đổi thân phận", "没人知道她下班后竟然变身电台主播。", "Không ai biết sau giờ làm cô ấy lại hóa thân thành phát thanh viên của đài.",
     "Động từ, nghĩa là thay đổi thân phận, biến thành một người khác, phía sau thường là danh từ chỉ thân phận mới. Trong bài: 想通过自己的努力变身城市人, muốn bằng nỗ lực của mình mà biến thành người thành phố."),
    ("纵然", "zòngrán", "túng nhiên", "liên từ", "dù cho, cho dù", "纵然未来困难重重，我们也要勇往直前。", "Dù tương lai muôn vàn khó khăn, chúng ta cũng phải dũng cảm tiến lên.",
     "Liên từ, nghĩa là dù cho, cho dù, giống 即使 nhưng mang màu sắc văn viết hơn. Thường đi với 也 ở vế sau: 纵然……也……. Đây là câu mẫu trọng điểm thứ hai của bài."),
    ("诸多", "zhūduō", "chư đa", "tính từ", "nhiều, rất nhiều", "这个计划还存在诸多问题。", "Kế hoạch này vẫn còn tồn tại nhiều vấn đề.",
     "Tính từ, nghĩa là rất nhiều, văn viết, thường dùng cho sự vật trừu tượng. Kết hợp hay gặp: 诸多因素, nhiều nhân tố; 诸多问题, nhiều vấn đề; 诸多不便, nhiều bất tiện. Chữ 诸 là các, như trong chư vị."),
    ("彷徨", "pánghuáng", "bàng hoàng", "động từ", "do dự, hoang mang, không biết đi đường nào", "面对未来，他感到十分彷徨。", "Đứng trước tương lai, anh ấy cảm thấy vô cùng hoang mang.",
     "Động từ, nghĩa là do dự, chần chừ, không biết nên đi đường nào. Cẩn thận, đây là từ rất dễ nhầm: tiếng Việt bàng hoàng là sững sờ, choáng váng; còn 彷徨 là hoang mang, lưỡng lự. Thành ngữ: 彷徨失措, hoang mang không biết làm sao."),
    ("徘徊", "páihuái", "bồi hồi", "động từ", "đi đi lại lại; do dự, lưỡng lự", "他一个人在小路上徘徊了很久。", "Anh ấy một mình đi đi lại lại trên con đường nhỏ rất lâu.",
     "Động từ, nghĩa gốc là đi đi lại lại ở một chỗ, nghĩa bóng là do dự, lưỡng lự. Lại một từ dễ nhầm: tiếng Việt bồi hồi là xao xuyến trong lòng; còn 徘徊 là quanh quẩn, chần chừ. Trong bài: 不少人都在徘徊、困惑和迷茫, nhiều người đang chần chừ, bối rối và mất phương hướng."),
    ("困惑", "kùnhuò", "khốn hoặc", "tính từ", "bối rối, băn khoăn, không biết làm sao", "他的话让我很困惑。", "Lời anh ấy nói khiến tôi rất bối rối.",
     "Tính từ, nghĩa là cảm thấy khó hiểu, bối rối, không biết nên làm thế nào. Cũng làm danh từ, nghĩa là điều băn khoăn: 我心里有很多困惑."),
    ("迷茫", "mímáng", "mê mang", "tính từ", "mơ hồ, mất phương hướng", "毕业以后，很多年轻人感到迷茫。", "Sau khi tốt nghiệp, nhiều bạn trẻ cảm thấy mất phương hướng.",
     "Tính từ, nghĩa là mơ hồ, mông lung, không biết nên chọn con đường nào trong cuộc sống hay công việc. Kết hợp hay gặp: 一片迷茫, 迷茫的表情, 迷茫的眼神. Trong bài có ba từ gần nghĩa đi liền nhau: 徘徊，困惑，迷茫."),
    ("残留", "cánliú", "tàn lưu", "động từ", "còn sót lại, còn lưu lại", "桃花凋谢了，枝头残留着几片花瓣。", "Hoa đào đã tàn, trên cành còn sót lại vài cánh hoa.",
     "Động từ, nghĩa là phần còn thừa lại, còn sót lại. Chữ 残 là tàn, như tàn dư. Trong bài: 为了心里残留的那份理想与希望, vì chút lý tưởng và hy vọng còn sót lại trong lòng."),
    ("固然", "gùrán", "cố nhiên", "liên từ", "đành rằng, tuy là (thừa nhận rồi chuyển ý)", "理想固然很丰满，可现实却很骨感。", "Lý tưởng đành là rất đẹp đẽ, nhưng hiện thực lại rất phũ phàng.",
     "Liên từ, biểu thị thừa nhận một sự thật, rồi vế sau chuyển ý bằng 可是, 但是. Cẩn thận: tiếng Việt cố nhiên là tất nhiên; còn 固然 trong tiếng Trung chủ yếu dùng để nhượng bộ: đành rằng A, nhưng B. Đây là câu mẫu thứ ba."),
    ("丰满", "fēngmǎn", "phong mãn", "tính từ", "đầy đặn, đẫy đà; (bóng) đẹp đẽ, đầy đủ", "她的身材很丰满。", "Thân hình cô ấy rất đầy đặn.",
     "Tính từ, nghĩa gốc là cơ thể đầy đặn, cân đối, đẹp mắt. Trong câu nói nổi tiếng trên mạng 理想很丰满，现实很骨感, nó được dùng theo nghĩa bóng: lý tưởng thì đầy đặn, đẹp đẽ."),
    ("骨感", "gǔgǎn", "cốt cảm", "tính từ", "gầy gò, lộ xương; (bóng) khắc nghiệt, phũ phàng", "她是一位很骨感的女孩儿。", "Cô ấy là một cô gái rất mảnh khảnh.",
     "Tính từ, nghĩa gốc là thân hình gầy gò, lộ rõ đường nét xương. Đi với 丰满 trong câu 理想很丰满，现实很骨感, nó mang nghĩa bóng: hiện thực thì khô khan, trần trụi, khắc nghiệt. Theo chú thích của sách, câu này xuất phát từ bộ phim truyền hình 我的青春谁做主 năm hai nghìn lẻ chín, rồi trở thành câu cửa miệng trên mạng."),
    ("承载", "chéngzài", "thừa tải", "động từ", "chịu được (sức nặng); chứa đựng, gửi gắm", "农村承载着他们童年的回忆。", "Nông thôn chứa đựng những ký ức tuổi thơ của họ.",
     "Động từ, nghĩa gốc là chịu được sức nặng, như cầu chịu tải trọng; nghĩa bóng là gánh vác, chứa đựng, gửi gắm: 承载回忆, chứa đựng ký ức; 承载梦想, gửi gắm ước mơ. Sách in phiên âm chữ cuối là thanh ba, nhưng từ điển chuẩn đọc thanh bốn, chéngzài."),
    ("拆迁", "chāiqiān", "sách thiên", "động từ", "giải tỏa, phá dỡ nhà để di dời", "因为修路，我家的老房子拆迁了。", "Vì làm đường, ngôi nhà cũ của tôi đã bị giải tỏa.",
     "Động từ, nghĩa là vì nhu cầu xây dựng mà phá dỡ nhà cửa, bắt người dân dời đi nơi khác. 拆 là phá, dỡ; 迁 là dời. Tiếng Việt tương đương là giải tỏa, di dời. Trong bài: 家里的房子拆迁了."),
    ("玩耍", "wánshuǎ", "ngoạn sái", "động từ", "vui chơi, nô đùa", "孩子们在公园里尽情玩耍。", "Bọn trẻ thỏa thích vui đùa trong công viên.",
     "Động từ, nghĩa là vui chơi, nô đùa, thường nói về trẻ con. Chữ 耍 cũng là chơi đùa. Trong bài: 当年玩耍的小河堆满垃圾, con sông nhỏ ngày xưa từng nô đùa nay chất đầy rác."),
    ("田园", "tiányuán", "điền viên", "danh từ", "ruộng vườn; vùng quê", "他向往安静的田园生活。", "Anh ấy mơ ước cuộc sống điền viên yên tĩnh.",
     "Danh từ, nghĩa là ruộng vườn, mượn để chỉ nông thôn: 田园生活, cuộc sống điền viên; 田园诗人, nhà thơ điền viên. Trong bài có cụm 田园牧歌式的生活: 牧歌 là bài ca của người chăn gia súc, rộng ra là thơ ca, âm nhạc về đời sống thôn quê. Cả cụm là cuộc sống điền viên thanh bình như trong thơ ca."),
    ("务工", "wùgōng", "vụ công", "động từ", "làm công, đi làm thuê", "他十八岁就去城里务工了。", "Mới mười tám tuổi anh ấy đã lên thành phố làm thuê.",
     "Động từ, nghĩa là làm việc trong ngành công nghiệp, công trình, tức đi làm công. Chữ 务 là làm, lo liệu một việc. Đối lại là 务农, làm nông, cũng là từ mới của bài: 他们并非对务农一窍不通, họ không phải hoàn toàn không biết làm nông. 在外务工 là đi làm thuê xa nhà."),
    ("匆匆", "cōngcōng", "thông thông", "tính từ", "vội vàng, vội vã", "他只和朋友们打了个招呼就匆匆离开了。", "Anh ấy chỉ chào bạn bè một câu rồi vội vã rời đi.",
     "Tính từ, nghĩa là vội vội vàng vàng. Kết hợp hay gặp: 匆匆返回, vội vã quay về; 来去匆匆, đến đi vội vã; 时光匆匆, thời gian vội trôi. Trong bài: 待上四五天便匆匆返回城市, ở lại bốn năm ngày rồi lại vội vã trở về thành phố."),
    ("薄弱", "bóruò", "bạc nhược", "tính từ", "yếu, yếu kém, mỏng manh", "环保目前仍是我们工作中的薄弱环节。", "Bảo vệ môi trường hiện vẫn là khâu yếu trong công việc của chúng ta.",
     "Tính từ, nghĩa là không vững mạnh, dễ bị phá vỡ, lung lay. Chú ý chữ đầu ở đây đọc bó. Tiếng Việt bạc nhược thường nói về ý chí; còn 薄弱 dùng rộng hơn: 基础薄弱, nền tảng yếu; 薄弱环节, khâu yếu; 意志薄弱, ý chí yếu."),
    ("况且", "kuàngqiě", "huống thả", "liên từ", "hơn nữa, vả lại", "这件衣服太贵了，况且我也不太喜欢。", "Chiếc áo này đắt quá, vả lại tôi cũng không thích lắm.",
     "Liên từ, đứng trước vế sau, bổ sung thêm một lý do, đẩy ý lên một tầng nữa. Các bạn đã học từ này ở bài hai mươi giáo trình HSK sáu. Trong bài: 况且农业生产高投入、低回报, hơn nữa sản xuất nông nghiệp đầu tư cao mà thu về thấp."),
    ("不彰", "bùzhāng", "bất chương", "động từ", "không rõ rệt, không rõ ràng", "这项政策实施多年，效果不彰。", "Chính sách này thực hiện nhiều năm mà hiệu quả không rõ rệt.",
     "Động từ, văn viết, nghĩa là không rõ ràng, không nổi bật. Chữ 彰 là rõ ràng, như trong 表彰, biểu dương. Kết hợp hay gặp: 效果不彰, hiệu quả không rõ rệt. Trong bài: 效益不彰, hiệu quả kinh tế không rõ rệt."),
    ("不争", "bùzhēng", "bất tranh", "tính từ", "không thể bàn cãi, hiển nhiên", "这是一个不争的事实。", "Đây là một sự thật không thể bàn cãi.",
     "Tính từ thuộc tính, chỉ đứng trước danh từ, nghĩa là không cần tranh cãi, không thể nghi ngờ. Gần như luôn đi với 事实: 不争的事实, sự thật không thể chối cãi."),
    ("打拼", "dǎpīn", "đả bính", "động từ", "phấn đấu, bươn chải, lăn lộn", "他一个人在大城市打拼了十年。", "Anh ấy một mình bươn chải ở thành phố lớn suốt mười năm.",
     "Động từ, nghĩa là dốc sức làm việc, phấn đấu, lăn lộn kiếm sống. Kết hợp hay gặp: 奋力打拼, 为生活而打拼. Trong bài: 因为在城市多年的打拼而习惯了城市的生活, vì nhiều năm bươn chải ở thành phố nên đã quen với cuộc sống thành thị."),
    ("回归", "huíguī", "hồi quy", "động từ", "trở về (nơi cũ)", "很多人退休以后选择回归家园。", "Nhiều người sau khi nghỉ hưu chọn trở về quê nhà.",
     "Động từ, nghĩa là trở về nơi ban đầu: 回归祖国, trở về với Tổ quốc; 回归家园, trở về quê nhà. Trong bài: 已经不想再回归农村了, đã không muốn trở về nông thôn nữa."),
    ("破解", "pòjiě", "phá giải", "động từ", "giải mã; giải quyết (vấn đề khó)", "新生代农民工之困该如何破解？", "Nỗi khó khăn của lao động nhập cư thế hệ mới nên giải quyết thế nào?",
     "Động từ, nghĩa là giải mã, bẻ khóa, hoặc tìm ra cách giải quyết một vấn đề khó. Kết hợp hay gặp: 破解难题, giải bài toán khó; 破解密码, bẻ khóa mật mã. Câu ví dụ chính là tiểu mục thứ ba của bài."),
    ("过客", "guòkè", "quá khách", "danh từ", "khách qua đường, người qua đường", "我只是你生命中的一个过客。", "Tôi chỉ là một người khách qua đường trong cuộc đời bạn.",
     "Danh từ, nghĩa là người khách đi ngang qua, không ở lại lâu. Trong bài: thế hệ thứ nhất biết rõ mình chỉ là 城市的过客, khách qua đường của thành phố."),
    ("归宿", "guīsù", "quy túc", "danh từ", "chốn về cuối cùng; kết cục", "河流的归宿是大海。", "Chốn về cuối cùng của dòng sông là biển cả.",
     "Danh từ, nghĩa là nơi chốn cuối cùng mà người hay sự vật dừng lại, nơi nương tựa lâu dài. Sách có ví dụ rất đẹp: 河流的归宿是大海，落花的归宿是大地, chốn về của dòng sông là biển cả, chốn về của hoa rụng là đất mẹ. Trong bài: 他们来自农村，归宿也在农村."),
    ("接纳", "jiēnà", "tiếp nạp", "động từ", "tiếp nhận, chấp nhận, đón nhận", "我们接纳了他的建议。", "Chúng tôi đã tiếp thu đề nghị của anh ấy.",
     "Động từ, nghĩa là tiếp nhận, chấp nhận một người vào tập thể, hoặc tiếp thu ý kiến: 接纳意见, 接纳批评, 接纳移民. Trong bài: 他们向往城市，却不被城市所接纳, họ hướng về thành phố, nhưng lại không được thành phố đón nhận."),
    ("日益", "rìyì", "nhật ích", "phó từ", "ngày càng, ngày một", "该地区的空气污染日益严重。", "Ô nhiễm không khí ở khu vực này ngày càng nghiêm trọng.",
     "Phó từ, nghĩa là mức độ mỗi ngày một tăng, văn viết, giống 越来越. Thường đi với động từ hay tính từ hai âm tiết: 日益严重，日益激烈，日益疏远."),
    ("疏远", "shūyuǎn", "sơ viễn", "động từ", "xa cách, xa lánh, lạnh nhạt", "太久没见面，俩人的感情渐渐疏远了。", "Lâu quá không gặp, tình cảm hai người dần dần xa cách.",
     "Động từ, nghĩa là không còn thân thiết, có khoảng cách về quan hệ, tình cảm. Trái nghĩa là 亲近. Trong bài: 根在农村，却对农村日益疏远, gốc rễ ở nông thôn, nhưng ngày càng xa cách với nông thôn."),
    ("定居", "dìngjū", "định cư", "động từ", "định cư, ở hẳn", "他打算毕业以后在北京定居。", "Anh ấy định sau khi tốt nghiệp sẽ định cư ở Bắc Kinh.",
     "Động từ ly hợp, nghĩa là ở lâu dài tại một nơi, âm Hán Việt và nghĩa giống tiếng Việt: 回国定居，定居北京. Là động từ ly hợp nên có thể nói 定了居."),
    ("宏观", "hóngguān", "hoằng quan", "tính từ", "vĩ mô, tổng thể", "国家要加强宏观调控。", "Nhà nước cần tăng cường điều tiết vĩ mô.",
     "Tính từ, nghĩa là ở phạm vi lớn, mang tính tổng thể; tiếng Việt gọi là vĩ mô. Trái nghĩa là 微观, vi mô. Kết hợp hay gặp: 宏观经济, kinh tế vĩ mô; 宏观调控, điều tiết vĩ mô."),
    ("壁垒", "bìlěi", "bích lũy", "danh từ", "hàng rào, rào cản", "各国应该努力打破贸易壁垒。", "Các nước nên nỗ lực phá bỏ hàng rào thương mại.",
     "Danh từ, nghĩa gốc là tường lũy trong quân doanh, nghĩa bóng là ranh giới, rào cản: 市场壁垒，贸易壁垒. Trong bài: 有形无形的壁垒, những rào cản hữu hình và vô hình."),
    ("瓶颈", "píngjǐng", "bình cảnh", "danh từ", "nút thắt cổ chai, điểm nghẽn", "学者总会有遇到研究瓶颈的时候。", "Nhà nghiên cứu nào rồi cũng có lúc gặp nút thắt trong nghiên cứu.",
     "Danh từ, nghĩa đen là cổ chai, nghĩa bóng là yếu tố then chốt kìm hãm, khó vượt qua; tiếng Việt cũng nói nút thắt cổ chai. Trong bài: 还有很多瓶颈亟待打破, còn rất nhiều nút thắt đang cần gấp rút tháo gỡ."),
    ("亟", "jí", "cức", "phó từ", "gấp, cấp bách", "这个问题亟待解决。", "Vấn đề này đang cần giải quyết gấp.",
     "Phó từ, văn viết, nghĩa là gấp rút, khẩn cấp, ở đây đọc jí thanh hai. Thường gặp trong 亟待, đang cần gấp, và 亟须, cần phải gấp. Trong bài: 亟待打破, đang cần gấp rút phá bỏ.", "急"),
    ("纳入", "nàrù", "nạp nhập", "động từ", "đưa vào, đưa vào trong", "这个项目已经被纳入明年的计划。", "Dự án này đã được đưa vào kế hoạch năm sau.",
     "Động từ, nghĩa là đưa vào, xếp vào một khuôn khổ, hệ thống. Kết hợp hay gặp: 纳入规划，纳入计划，纳入体系. Mẫu câu: 将A纳入B, đưa A vào B. Trong bài: 将农民工群体纳入城市经济社会发展规划."),
    ("财政", "cáizhèng", "tài chính", "danh từ", "tài chính (nhà nước), ngân sách", "政府加大了对教育的财政投入。", "Chính phủ đã tăng đầu tư ngân sách cho giáo dục.",
     "Danh từ, chỉ việc nhà nước quản lý thu chi tiền của: 财政收入, thu ngân sách; 财政支出, chi ngân sách. Chú ý: tiếng Việt tài chính dùng rộng, nhưng tiếng Trung phân biệt 财政 là tài chính công của nhà nước, còn 金融 là ngân hàng, tiền tệ, chứng khoán."),
    ("红利", "hónglì", "hồng lợi", "danh từ", "cổ tức, tiền chia lãi; (bóng) lợi ích", "让每个人都能共享发展的红利。", "Để mỗi người đều được chia sẻ lợi ích của sự phát triển.",
     "Danh từ, nghĩa gốc là phần lợi nhuận doanh nghiệp chia cho cổ đông, hay tiền thưởng thêm cho nhân viên. Nghĩa bóng hay gặp trên báo chí là lợi ích mà một sự phát triển đem lại: 发展红利，人口红利. Trong bài: 共享城市发展带来的红利."),
    ("冷漠", "lěngmò", "lãnh mạc", "tính từ", "lạnh nhạt, thờ ơ", "他对别人的困难总是很冷漠。", "Anh ta luôn thờ ơ trước khó khăn của người khác.",
     "Tính từ, nghĩa là lạnh nhạt, dửng dưng, không quan tâm. Kết hợp hay gặp: 神情冷漠，冷漠的态度. Trong bài: 莫让他们遭受冷漠的社会歧视, đừng để họ phải chịu sự kỳ thị lạnh lùng của xã hội."),
    ("歧视", "qíshì", "kỳ thị", "động từ", "kỳ thị, phân biệt đối xử", "我们不应该歧视任何人。", "Chúng ta không nên kỳ thị bất kỳ ai.",
     "Động từ, nghĩa là đối xử không bình đẳng, âm Hán Việt và nghĩa giống tiếng Việt. Cũng làm danh từ: 性别歧视, kỳ thị giới tính; 遭受歧视, bị kỳ thị."),
    ("适宜", "shìyí", "thích nghi", "tính từ", "thích hợp, phù hợp", "这里气候温和，适宜居住。", "Ở đây khí hậu ôn hòa, thích hợp để sinh sống.",
     "Tính từ, nghĩa là thích hợp, phù hợp. Cẩn thận, từ rất dễ nhầm: tiếng Việt thích nghi là quen dần với môi trường, tương đương 适应 trong tiếng Trung; còn 适宜 là thích hợp. Kết hợp: 气温适宜，适宜居住. Trong bài: 选准适宜发展的地方, chọn đúng nơi thích hợp để phát triển."),
    ("偌大", "ruòdà", "nhược đại", "tính từ", "to lớn như thế, rộng lớn chừng ấy", "偌大的教室里只有我一个人。", "Trong phòng học rộng lớn như thế chỉ có mình tôi.",
     "Tính từ, nghĩa là to như thế, rộng như vậy, hay gặp trong bạch thoại thời kỳ đầu, nay mang màu sắc văn chương. Thường nhấn mạnh sự trống trải, nhỏ bé của con người trong không gian rộng lớn: 偌大的城市."),
    ("迷失", "míshī", "mê thất", "động từ", "lạc (đường, phương hướng), đánh mất", "我们不能在金钱面前迷失自我。", "Chúng ta không được đánh mất bản thân trước đồng tiền.",
     "Động từ, nghĩa là lạc mất, lệch khỏi phương hướng đúng đắn của cuộc đời: 迷失方向, lạc hướng; 迷失自我, đánh mất chính mình. Câu kết của bài: 他们才不会在偌大的城市中迷失自己."),
    ("浑身解数", "húnshēn-xièshù", "hồn thân giải số", "thành ngữ", "trổ hết bản lĩnh, dốc hết tài nghệ", "两队为了赢得这场重要的比赛，均使出了浑身解数。", "Để thắng trận đấu quan trọng này, cả hai đội đều trổ hết tài nghệ.",
     "Thành ngữ. 浑身 là toàn thân, tức là tất cả; 解数 là các đường võ, chữ 解 ở đây đọc xiè. Cả cụm là toàn bộ bản lĩnh, mọi mánh khóe. Gần như luôn đi với 使出: 使出浑身解数, trổ hết bản lĩnh."),
    ("望尘莫及", "wàngchén-mòjí", "vọng trần mạc cập", "thành ngữ", "theo không kịp, tụt lại rất xa", "猎豹的短跑速度是陆地上任何动物都望尘莫及的。", "Tốc độ chạy nước rút của báo săn là điều mọi loài vật trên cạn đều không theo kịp.",
     "Thành ngữ. Chỉ thấy bụi do người đi trước tung lên mà không đuổi kịp; 莫 là không, 及 là đuổi kịp. Hình dung tụt lại quá xa. Trong bài: 望尘莫及的房价, giá nhà cao đến mức không với tới."),
    ("逢年过节", "féngnián-guòjié", "phùng niên quá tiết", "thành ngữ", "dịp Tết nhất, lễ lạt", "这家公司逢年过节都会发放礼品和奖金。", "Công ty này cứ dịp Tết, ngày lễ là phát quà và tiền thưởng.",
     "Thành ngữ, nghĩa là vào dịp năm mới hay các ngày lễ. 逢 là gặp, như đã học trong từ 每逢. Trong bài: 很多都是逢年过节时才回家一趟, nhiều người chỉ dịp Tết nhất mới về nhà một chuyến."),
    ("一窍不通", "yīqiào-bùtōng", "nhất khiếu bất thông", "thành ngữ", "không biết tí gì, mù tịt", "他只是个读书人，对经商可以说是一窍不通。", "Anh ấy chỉ là người đọc sách, về buôn bán có thể nói là mù tịt.",
     "Thành ngữ. 窍 là lỗ, chỉ các khiếu trong lòng; không một khiếu nào thông, tức là hoàn toàn không hiểu gì. Mẫu: 对……一窍不通. Trong bài: 他们并非对务农一窍不通, họ không phải hoàn toàn không biết làm nông."),
    ("落叶归根", "luòyè-guīgēn", "lạc diệp quy căn", "thành ngữ", "lá rụng về cội", "很多定居国外的华侨都有落叶归根的情结。", "Nhiều Hoa kiều định cư ở nước ngoài đều mang nỗi niềm lá rụng về cội.",
     "Thành ngữ, cũng nói 叶落归根. Lá khô rơi xuống gốc cây, ví người sống nơi đất khách cuối cùng cũng trở về quê hương. Tiếng Việt có câu lá rụng về cội, rất gần. Trong bài: 想赚了钱后回农村落叶归根."),
    ("进退两难", "jìntuì-liǎngnán", "tiến thoái lưỡng nan", "thành ngữ", "tiến thoái lưỡng nan", "面对股市动荡，他一时间进退两难。", "Trước biến động của thị trường chứng khoán, nhất thời anh ấy tiến thoái lưỡng nan.",
     "Thành ngữ, tiến lên cũng khó, lùi lại cũng khó, ví việc không thể quyết định. Âm Hán Việt giống hệt tiếng Việt. Trong bài: 他们进退两难，不知道自己的未来在哪里！"),
    ("量力而行", "liànglì-érxíng", "lượng lực nhi hành", "thành ngữ", "liệu sức mà làm", "运动也要量力而行。", "Tập thể thao cũng phải liệu sức mà làm.",
     "Thành ngữ. Chữ đầu đọc liàng, nghĩa là đo, ước lượng; cả cụm là căn cứ sức mình mà làm, đừng gắng quá sức. Trong bài: 新生代农民工自己也要量力而行."),
    ("安居乐业", "ānjū-lèyè", "an cư lạc nghiệp", "thành ngữ", "an cư lạc nghiệp", "无论何时，让人民安居乐业都是政府的职责所在。", "Bất cứ lúc nào, làm cho nhân dân an cư lạc nghiệp cũng là trách nhiệm của chính phủ.",
     "Thành ngữ. 安 là yên ổn, 居 là chỗ ở, 乐 là vui thích, 业 là nghề nghiệp: sống yên ổn, vui với nghề. Chữ thứ ba đọc lè. Người Việt rất quen câu an cư lạc nghiệp. Trong bài: 选准适宜发展的地方安居乐业."),
]

add("bullets", chapter="Từ mới (55 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 2.1 có 47 từ mới và 8 thành ngữ, chia thành 19 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 薄弱 (bó) · 亟 (jí) · 浑身解数 (xiè) · 量力而行 (liàng) · 安居乐业 (lè)",
           "Từ dễ nhầm: 彷徨 · 徘徊 · 固然 · 适宜 · 财政"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bảng từ của sách có bốn mươi chín từ và chín thành ngữ. Thầy chọn ra năm mươi lăm mục quan trọng nhất, chia thành mười chín nhóm nhỏ; ba từ còn lại là 牧歌，务农 và 高楼大厦, thầy sẽ giảng kèm trong các từ liên quan.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe. Bài báo này có rất nhiều từ văn viết, đọc thành tiếng sẽ giúp các bạn nhớ lâu hơn."),
         F(3, "Một số chữ có cách đọc đặc biệt trong bài, như 薄弱，亟待，浑身解数，量力而行，安居乐业. Thầy sẽ nhắc khi gặp."),
         F(4, "Ngoài ra, có mấy từ Hán Việt rất dễ hiểu nhầm, như 彷徨，徘徊，固然，适宜，财政. Nghĩa của chúng trong tiếng Trung khác với tiếng Việt, các bạn nhớ nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

sizes = [3] * 17 + [2, 2]
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
    ("他们，是一群跨入工业文明的庄稼人的后代；他们，是游离在城市和农村之间、面临边缘化的群体。当他们身为“农民工一代”的父辈渐渐退出城市舞台，他们陆续涌入大大小小的城市——在原本不属于他们的高楼大厦间寻梦。",
     "Họ là con cháu của những người nông dân đã bước vào nền văn minh công nghiệp; họ là nhóm người lơ lửng giữa thành phố và nông thôn, có nguy cơ bị gạt ra bên lề. Khi cha chú họ, lớp lao động nhập cư đời đầu, dần rời sân khấu thành phố, họ lần lượt đổ về các thành phố lớn nhỏ, tìm giấc mơ giữa những tòa cao ốc vốn không thuộc về mình.",
     ["Đoạn mở đầu dùng phép điệp: 他们，是……；他们，是……, lặp lại chủ ngữ để gây ấn tượng mạnh, kiểu văn báo chí giàu cảm xúc. 跨入 là bước vào. 庄稼人的后代 là con cháu nhà nông.",
      "身为 nghĩa là thân là, với tư cách là: 身为农民工一代的父辈, những bậc cha chú vốn là lao động nhập cư đời đầu. 退出城市舞台 là rút khỏi sân khấu thành phố, tức là đã già, lần lượt về quê.",
      "陆续涌入 là lần lượt ồ ạt đổ vào. Dấu gạch ngang dài dẫn ra lời giải thích: 在原本不属于他们的高楼大厦间寻梦, họ đi tìm giấc mơ giữa những tòa nhà cao tầng vốn không thuộc về mình. Chữ 原本 là vốn dĩ, đã báo trước nỗi khó khăn khi hòa nhập."]),
    ("他们，有着一个共同的名字：新生代农民工。",
     "Họ có chung một cái tên: lao động nhập cư thế hệ mới.",
     ["Đoạn văn chỉ có một câu, nhưng là câu then chốt: nó gọi tên đối tượng của cả bài. 有着 là có, động từ 有 thêm 着, mang màu sắc văn viết: 有着一个共同的名字.",
      "Nhớ lại phần bối cảnh: 新生代农民工 là những người sinh từ năm một nghìn chín trăm tám mươi trở về sau, làm việc ở thành phố nhưng hộ khẩu ở nông thôn. Hai đoạn đầu là phần dẫn nhập; tiếp theo, bài báo chia làm ba tiểu mục, mỗi tiểu mục là một câu hỏi."]),
    ("【他们离“新市民”还有多远？】\n繁华的大都市有着先进的教育、发达的医疗、无数的机会……是多少农民工向往的“圣地”。目前，外出打工的人数约有2.7亿，在这当中，80后、90后的新生代农民工居多，大约有1个亿。",
     "【Họ còn cách “thị dân mới” bao xa?】 Đô thị lớn phồn hoa có nền giáo dục tiên tiến, y tế phát triển, vô số cơ hội…, là “thánh địa” mà biết bao lao động nhập cư hằng mơ ước. Hiện nay, số người rời quê đi làm thuê vào khoảng 270 triệu, trong đó phần đông là lao động nhập cư thế hệ mới sinh vào thập niên 80, 90, khoảng 100 triệu người.",
     ["Tiểu mục thứ nhất: 他们离新市民还有多远？ Họ còn cách việc trở thành thị dân mới bao xa? 新市民 là cư dân mới của thành phố.",
      "是多少农民工向往的圣地: 多少 ở đây không phải câu hỏi, mà là cảm thán, nghĩa là biết bao nhiêu. 向往 là hướng về, mong mỏi. 圣地 là thánh địa, nơi ai cũng ao ước được đến.",
      "外出打工 là rời quê đi làm thuê. 八零后、九零后 là thế hệ sinh vào thập niên tám mươi, chín mươi, tiếng Việt hay gọi là thế hệ tám X, chín X. 新生代农民工居多 nghĩa là lao động thế hệ mới chiếm đa số; đây là câu mẫu 以……居多. 一个亿 là một trăm triệu, cách nói khẩu ngữ của 一亿."],
     "他们离新市民还有多远？繁华的大都市有着先进的教育、发达的医疗、无数的机会……是多少农民工向往的圣地。目前，外出打工的人数约有二点七亿，在这当中，八零后、九零后的新生代农民工居多，大约有一个亿。"),
    ("他们十几岁时就背井离乡，想通过自己的努力变身“城市人”。然而，当他们想要融入城市的时候，才发现作为一个外乡人，纵然使出浑身解数，在繁华都市的边缘，也难免感到诸多无奈与彷徨。",
     "Mới mười mấy tuổi họ đã rời bỏ quê hương, mong bằng nỗ lực của bản thân mà trở thành “người thành phố”. Thế nhưng, khi muốn hòa nhập vào thành phố, họ mới nhận ra rằng, là một người nơi khác đến, dù có trổ hết bản lĩnh, thì ở bên rìa đô thị phồn hoa ấy, họ vẫn khó tránh khỏi biết bao bất lực và hoang mang.",
     ["背井离乡 là thành ngữ: bỏ giếng nước, rời quê hương, tức rời quê đi nơi khác sinh sống, giống tha hương cầu thực trong tiếng Việt. 变身城市人 là biến thành người thành phố. 融入 là hòa nhập, hòa vào.",
      "外乡人 là người nơi khác đến. 纵然使出浑身解数，……也难免……: 纵然……也…… nghĩa là dù cho… cũng…, câu mẫu thứ hai. 难免 là khó tránh khỏi. 无奈与彷徨 là sự bất lực và nỗi hoang mang."]),
    ("望尘莫及的房价、高昂的生活成本，没有稳定的工作也没有社会保障，自己买不起城里的房、孩子上不了城里的学校……不少人都在徘徊、困惑和迷茫。",
     "Giá nhà cao không với tới, chi phí sinh hoạt đắt đỏ, không có việc làm ổn định cũng chẳng có bảo hiểm xã hội, bản thân không mua nổi nhà ở thành phố, con cái không được học trường thành phố… nhiều người đang chần chừ, bối rối và mất phương hướng.",
     ["Câu này liệt kê một chuỗi khó khăn: 望尘莫及的房价, giá nhà cao không với tới; 高昂的生活成本, chi phí sinh hoạt đắt đỏ, 高昂 là cao vút; 社会保障 là an sinh xã hội, bảo hiểm xã hội.",
      "买不起 là không đủ tiền mua; 上不了 là không vào học được, bổ ngữ khả năng. Vì hộ khẩu ở quê, con cái họ rất khó vào trường công ở thành phố. Ba từ gần nghĩa 徘徊、困惑和迷茫 xếp liền nhau, nhấn mạnh tâm trạng rối bời."]),
    ("要不回家算了？可为了心里残留的那份理想与希望，或仅仅是为了面子，多数人还在坚持着。",
     "Hay là về quê cho xong? Nhưng vì chút lý tưởng và hy vọng còn sót lại trong lòng, hoặc chỉ đơn giản là vì sĩ diện, phần đông vẫn đang cố bám trụ.",
     ["要不……算了 là mẫu khẩu ngữ: hay là… cho xong, thôi thì…. Câu hỏi này như lời họ tự nói với chính mình. 那份理想与希望 dùng lượng từ 份 cho tình cảm, ý niệm trừu tượng.",
      "仅仅是为了面子 là chỉ là vì thể diện, sĩ diện; về quê tay trắng thì sợ bị người làng chê cười. 还在坚持着 là vẫn đang kiên trì, cố gắng trụ lại."]),
    ("他们希望经过几年甚至十几年的辛苦奋斗，融入这座城市，让下一代告别祖辈“面朝黄土背朝天”的生活。理想固然很丰满，可现实却很骨感……",
     "Họ mong rằng sau vài năm, thậm chí mười mấy năm vất vả phấn đấu, sẽ hòa nhập được vào thành phố này, để thế hệ sau giã từ cuộc sống “mặt hướng xuống đất vàng, lưng quay lên trời” của cha ông. Lý tưởng đành là rất đẹp đẽ, nhưng hiện thực lại rất phũ phàng…",
     ["面朝黄土背朝天: theo chú thích của sách, khi làm ruộng người nông dân cúi đầu, khom lưng, mặt hướng xuống đất vàng, vì đất vùng Trung Nguyên có màu vàng, lưng quay lên trời. Câu này hình dung nỗi vất vả của nhà nông, giống câu bán mặt cho đất, bán lưng cho trời của tiếng Việt. Chữ 朝 ở đây đọc cháo, nghĩa là hướng về.",
      "理想固然很丰满，可现实却很骨感: câu mẫu 固然……可……, đành rằng… nhưng…. Đây là câu cửa miệng trên mạng: lý tưởng thì đầy đặn, hiện thực thì gầy gò, tức là ước mơ đẹp nhưng thực tế khắc nghiệt."]),
    ("【农村：不想回还是不能回？】\n农村是他们的根，是承载着他们童年回忆的地方。但是随着农村城镇化的建设，家里的房子拆迁了，童年爬过的大树不见了，当年玩耍的小河堆满垃圾，农村“田园牧歌式”的生活不复存在。",
     "【Nông thôn: không muốn về hay không thể về?】 Nông thôn là gốc rễ của họ, là nơi lưu giữ ký ức tuổi thơ của họ. Nhưng cùng với quá trình đô thị hóa nông thôn, ngôi nhà cũ đã bị giải tỏa, cây to tuổi thơ từng trèo không còn nữa, con sông nhỏ ngày xưa nô đùa nay chất đầy rác, cuộc sống điền viên thanh bình nơi thôn quê không còn tồn tại.",
     ["Tiểu mục thứ hai đặt câu hỏi: 不想回还是不能回？ Không muốn về, hay không thể về? Bổ ngữ khả năng 回不去 trong tên bài chính là ý này.",
      "承载着他们童年回忆 là chứa đựng ký ức tuổi thơ của họ. 城镇化 là đô thị hóa, 城镇 là thành thị và thị trấn. Ba vế 房子拆迁了，大树不见了，小河堆满垃圾 tạo thành phép liệt kê, cho thấy làng quê xưa đã thay đổi hoàn toàn.",
      "田园牧歌式的生活 là cuộc sống điền viên thanh bình như trong thơ ca. 不复存在 là không còn tồn tại nữa; 不复 là câu mẫu thứ tư, văn viết, nghĩa là không còn… nữa."]),
    ("在外务工的年轻人，很多都是逢年过节时才回家一趟，待上四五天便匆匆返回城市。他们并非对务农一窍不通，但返乡后就是不愿呆在农村，哪怕在城镇租房居住，也不想再接触农村，不想再拿起农具从事农业生产。",
     "Những người trẻ đi làm thuê xa nhà, nhiều người chỉ dịp Tết nhất mới về nhà một chuyến, ở lại bốn năm ngày rồi lại vội vã trở về thành phố. Họ không phải hoàn toàn không biết làm nông, nhưng về quê rồi lại nhất định không chịu ở lại nông thôn; dù phải thuê nhà ở thị trấn, họ cũng không muốn tiếp xúc với nông thôn nữa, không muốn cầm lại nông cụ làm nghề nông nữa.",
     ["逢年过节时才回家一趟: chữ 才 nhấn mạnh hiếm hoi, phải đến dịp Tết mới về. 待上四五天: chữ 待 ở đây đọc dāi, nghĩa là ở lại, giống 呆. 便 là liền, văn viết của 就.",
      "并非 là hoàn toàn không phải, văn viết. 就是不愿 là nhất định không muốn, 就是 nhấn mạnh thái độ kiên quyết. 哪怕……也…… là cho dù… cũng…. 从事农业生产 là làm sản xuất nông nghiệp. Như vậy, đây là không muốn về."]),
    ("农村的基础设施相对落后，教育、医疗等公共性服务相对薄弱，况且农业生产高投入、低回报，效益不彰，这都是不争的事实。而他们自己，也因为在城市多年的打拼而习惯了城市的生活，已经不想再回归农村了。",
     "Cơ sở hạ tầng ở nông thôn tương đối lạc hậu, các dịch vụ công như giáo dục, y tế tương đối yếu kém; hơn nữa sản xuất nông nghiệp đầu tư cao mà thu về thấp, hiệu quả không rõ rệt, đó đều là những sự thật không thể chối cãi. Còn bản thân họ, vì nhiều năm bươn chải ở thành phố nên đã quen với cuộc sống thành thị, không còn muốn trở về nông thôn nữa.",
     ["Đoạn này trả lời câu hỏi của tiểu mục, nêu hai loại nguyên nhân. Nguyên nhân khách quan: 基础设施 là cơ sở hạ tầng; 公共性服务相对薄弱 là dịch vụ công tương đối yếu kém.",
      "况且 bổ sung thêm lý do: 高投入、低回报 là đầu tư cao, thu về thấp; 效益不彰 là hiệu quả không rõ rệt. 这都是不争的事实 là đó đều là sự thật không thể chối cãi.",
      "Nguyên nhân chủ quan: 因为……而…… là vì… mà…, văn viết. 习惯了城市的生活 là đã quen với cuộc sống thành phố. Như vậy, câu trả lời là: vừa không thể về, vừa không muốn về."]),
    ("【新生代农民工之困该如何破解？】\n未来在哪里？对这一问题的回答，第一代农民工和新生代农民工有着显著的差异。对大多数第一代农民工而言，他们清楚地知道自己只是城市的“过客”，他们来自农村，归宿也在农村，想赚了钱后回农村“落叶归根”。",
     "【Nỗi khó khăn của lao động nhập cư thế hệ mới nên tháo gỡ thế nào?】 Tương lai ở đâu? Với câu hỏi này, câu trả lời của lao động nhập cư đời đầu và thế hệ mới khác nhau rõ rệt. Đối với phần lớn lao động đời đầu, họ biết rõ mình chỉ là “khách qua đường” của thành phố; họ đến từ nông thôn, chốn về cũng ở nông thôn, kiếm được tiền rồi thì muốn về quê “lá rụng về cội”.",
     ["Tiểu mục thứ ba: 新生代农民工之困该如何破解？ Chữ 之 tương đương 的: 新生代农民工之困 là cái khó của lao động thế hệ mới. 破解 là tháo gỡ, giải quyết.",
      "有着显著的差异 là có sự khác biệt rõ rệt. 对……而言 là đối với… mà nói, văn viết, giống 对……来说. Đoạn này nói về thế hệ thứ nhất: 过客, khách qua đường; 归宿也在农村, chốn về cũng là nông thôn; 落叶归根, lá rụng về cội."]),
    ("对于新生代农民工来说，他们向往城市，却不被城市所接纳；根在农村，却对农村日益疏远。他们进退两难，不知道自己的未来在哪里！",
     "Còn đối với lao động nhập cư thế hệ mới, họ hướng về thành phố, nhưng lại không được thành phố đón nhận; gốc rễ ở nông thôn, nhưng lại ngày càng xa cách với nông thôn. Họ tiến thoái lưỡng nan, không biết tương lai của mình ở đâu!",
     ["Đây là câu then chốt của cả bài, giải thích tên bài. Hai vế đối nhau rất chỉnh: 向往城市，却不被城市所接纳；根在农村，却对农村日益疏远. Chữ 却 là nhưng lại, biểu thị nghịch lý.",
      "不被城市所接纳 là câu bị động văn viết theo mẫu 被……所……, câu mẫu thứ sáu. 日益疏远 là ngày càng xa cách. 进退两难 tóm gọn tình cảnh: thành phố không hòa nhập được, nông thôn không về được."]),
    ("从现实角度看，要想在城里定居，新生代农民工在劳有所得、住有所居、病有所医等方面还面临着诸多障碍。无论是宏观的国家政策层面，还是每一个具体的解决方案，都仍然存在许多有形无形的壁垒，还有很多瓶颈亟待打破。",
     "Nhìn từ góc độ thực tế, muốn định cư ở thành phố, lao động nhập cư thế hệ mới vẫn còn phải đối mặt với nhiều trở ngại ở các mặt như làm có thu nhập, ở có nhà, ốm có nơi chữa. Dù là ở tầm chính sách vĩ mô của nhà nước, hay ở từng giải pháp cụ thể, đều vẫn còn nhiều rào cản hữu hình và vô hình, còn nhiều nút thắt đang cần gấp rút tháo gỡ.",
     ["劳有所得、住有所居、病有所医 là ba cụm bốn chữ theo mẫu A有所B: lao động thì có thu nhập, cần ở thì có nhà, ốm đau thì có nơi chữa. Đây là cách nói quen thuộc trong văn bản chính sách của Trung Quốc. 障碍 là trở ngại.",
      "无论是……还是……，都…… là dù là… hay là…, đều…. 宏观的国家政策层面 là tầng chính sách vĩ mô của nhà nước. 有形无形的壁垒 là rào cản hữu hình và vô hình. 瓶颈亟待打破 là nút thắt đang chờ gấp rút phá bỏ."]),
    ("破解新生代农民工融入城市的难题，需要全社会的共同努力。\n首先，政府要将农民工群体纳入城市经济社会发展规划和公共政策体系，在教育、住房、卫生、交通等公共服务方面加大财政投入，让新生代农民工能够共享城市发展带来的红利。",
     "Tháo gỡ bài toán hòa nhập thành phố của lao động nhập cư thế hệ mới cần sự chung tay của toàn xã hội. Trước hết, chính phủ cần đưa nhóm lao động nhập cư vào quy hoạch phát triển kinh tế xã hội của thành phố và hệ thống chính sách công, tăng chi ngân sách cho giáo dục, nhà ở, y tế, giao thông, để họ được cùng hưởng thành quả phát triển của thành phố.",
     ["Phần cuối bài đưa ra giải pháp, theo trình tự 首先，其次，此外, trước hết, tiếp theo, ngoài ra. Câu chủ đề: 需要全社会的共同努力, cần sự nỗ lực chung của toàn xã hội.",
      "Giải pháp thứ nhất dành cho chính phủ: 将A纳入B, đưa A vào B; 发展规划 là quy hoạch phát triển; 加大财政投入 là tăng đầu tư ngân sách; 共享红利 là cùng hưởng lợi ích. Câu văn mang đậm phong cách văn bản chính sách."]),
    ("其次，城市居民要不断提升认同与接纳程度，给他们以温暖和关注，莫让他们遭受冷漠的社会歧视。此外，新生代农民工自己也要量力而行，选准适宜发展的地方安居乐业。这样一来，他们才不会在偌大的城市中迷失自己。",
     "Tiếp theo, cư dân thành phố cần không ngừng nâng cao mức độ đồng cảm và đón nhận, dành cho họ sự ấm áp và quan tâm, đừng để họ phải chịu sự kỳ thị lạnh lùng của xã hội. Ngoài ra, bản thân lao động nhập cư thế hệ mới cũng phải liệu sức mà làm, chọn đúng nơi thích hợp để phát triển mà an cư lạc nghiệp. Như vậy, họ mới không đánh mất chính mình giữa thành phố rộng lớn.",
     ["Giải pháp thứ hai dành cho người thành phố: 给他们以温暖和关注 theo mẫu 给……以……, văn viết, nghĩa là dành cho ai cái gì. 莫让 là đừng để, 莫 là chữ văn ngôn, nghĩa là đừng. 遭受歧视 là bị kỳ thị.",
      "Giải pháp thứ ba dành cho chính người lao động: 量力而行, liệu sức mà làm; 选准 là chọn cho đúng, theo mẫu động từ cộng 准. 这样一来 là như vậy thì, dẫn ra kết quả. Câu kết 不会在偌大的城市中迷失自己 khép lại bài báo bằng một lời khuyên đầy tình người."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 融不进的城市，回不去的农村", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa. Bài được trích từ trang tin 中国新闻网 ngày bảy tháng tám năm hai nghìn không trăm mười lăm, tên gốc là 夹层中的新市民, những thị dân mới bị kẹp giữa hai tầng, tác giả là 宋子荣.",
         F(0, "Thầy chia bài thành mười lăm đoạn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng. Các dòng trong ngoặc vuông là tiểu mục của bài báo."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "").replace("【", "").replace("】", "").replace("\n", "")
    zsize = 54 if len(zh) <= 100 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", "").replace("【", "").replace("】", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Tóm tắt nội dung", section="Bài khóa 课文", title="Bố cục bài khóa", size=36,
    items=["## Dẫn nhập: 他们……新生代农民工",
           "## 1. 他们离“新市民”还有多远？",
           "房价高 · 生活成本高 · 没有稳定的工作和社会保障 · 孩子上不了城里的学校 → 徘徊、困惑、迷茫",
           "## 2. 农村：不想回还是不能回？",
           "不能回：农村变了，基础设施落后，公共服务薄弱，农业效益不彰 · 不想回：习惯了城市生活",
           "## 3. 新生代农民工之困该如何破解？",
           "政府：纳入规划，加大财政投入 · 城市居民：接纳，莫歧视 · 农民工自己：量力而行"],
    say=["Bây giờ chúng ta cùng nhìn lại bố cục của bài báo. Đây là kiểu bài nghị luận xã hội rất điển hình: nêu hiện tượng, phân tích nguyên nhân, rồi đề xuất giải pháp.",
         F(0, "Phần dẫn nhập giới thiệu đối tượng: một nhóm người lơ lửng giữa thành phố và nông thôn, có chung một cái tên, 新生代农民工."),
         F(1, "Tiểu mục một: 他们离新市民还有多远？ Họ còn cách việc trở thành người thành phố bao xa?"),
         F(2, "Câu trả lời là còn rất xa: giá nhà cao không với tới, chi phí sinh hoạt đắt, không có việc làm ổn định và bảo hiểm xã hội, con cái không vào được trường thành phố. Vì vậy họ 徘徊、困惑、迷茫."),
         F(3, "Tiểu mục hai: 农村：不想回还是不能回？ Nông thôn: không muốn về hay không thể về?"),
         F(4, "Câu trả lời là cả hai. Không thể về, vì làng quê đã đổi khác, hạ tầng lạc hậu, dịch vụ công yếu kém, làm nông không hiệu quả. Không muốn về, vì họ đã quen với cuộc sống thành phố."),
         F(5, "Tiểu mục ba: 新生代农民工之困该如何破解？ Tháo gỡ khó khăn này thế nào?"),
         F(6, "Ba giải pháp từ ba phía: chính phủ đưa họ vào quy hoạch, tăng đầu tư ngân sách; cư dân thành phố đón nhận, không kỳ thị; còn bản thân người lao động thì liệu sức mà làm, chọn đúng nơi để an cư lạc nghiệp. Bố cục này rất hữu ích khi các bạn tự kể lại bài khóa.")])

# ======================= CÂU MẪU =======================
add("bullets", chapter="Câu mẫu: 居多 · 纵然 · 固然", section="Câu mẫu 重点句型", title="1. （以）……居多 – chiếm đa số, phần lớn là…", size=34,
    items=["Trong một tập hợp, loại nào chiếm phần lớn: (在/当中)……（以）+ danh từ + 居多",
           "目前，外出打工的人数约有2.7亿，在这当中，80后、90后的新生代农民工居多，大约有1个亿。",
           "从地域来看，排名靠前的城市多位于中国东部沿海地区，以港口城市、经济发达城市居多。",
           "根据智能手机使用频度的调查研究，智能手机成瘾人群中以生活富足的、受过良好教育的男性居多。"],
    say=["Bây giờ chúng ta sang phần câu mẫu trọng điểm, 重点句型与词汇. Bài này có tám câu mẫu. Câu mẫu thứ nhất là 以……居多.",
         F(0, "居 ở đây nghĩa là ở vào, chiếm; 居多 là chiếm phần nhiều. Mẫu này dùng khi trong một tập hợp, có một loại chiếm đa số. Phía trước thường có 在……中 hay 当中 để nêu tập hợp; chữ 以 có thể có hoặc không. Tiếng Việt dịch là phần lớn là, chủ yếu là."),
         F(1, "Ví dụ một, từ bài khóa: 目前，外出打工的人数约有二点七亿，在这当中，八零后、九零后的新生代农民工居多，大约有一个亿。 Trong số đó, phần đông là lao động thế hệ tám X, chín X."),
         F(2, "Ví dụ hai: 从地域来看，排名靠前的城市多位于中国东部沿海地区，以港口城市、经济发达城市居多。 Xét về địa lý, các thành phố xếp hạng cao phần nhiều nằm ở vùng duyên hải phía đông Trung Quốc, chủ yếu là các thành phố cảng và thành phố kinh tế phát triển."),
         F(3, "Ví dụ ba: 根据智能手机使用频度的调查研究，智能手机成瘾人群中以生活富足的、受过良好教育的男性居多。 Theo khảo sát về tần suất dùng điện thoại thông minh, trong nhóm người nghiện điện thoại, phần lớn là nam giới có cuộc sống sung túc và được giáo dục tốt. 成瘾 là nghiện.")])

add("bullets", section="Câu mẫu 重点句型", title="2. 纵然……，也…… – dù cho… cũng…", size=34,
    items=["Liên từ văn viết = 即使……也……: giả sử điều kiện bất lợi xảy ra, kết quả vẫn không đổi",
           "作为一个外乡人，纵然使出浑身解数，在繁华都市的边缘，也难免感到诸多无奈与彷徨。",
           "纵然未来困难重重，我们也要勇往直前。",
           "互联网大大缩短了人和人之间的距离，纵然两人相隔千里，消息也可以瞬间送达。"],
    say=["Câu mẫu thứ hai: 纵然……，也…….",
         F(0, "纵然 là liên từ nhượng bộ, nghĩa giống 即使, nhưng mang màu sắc văn viết, trang trọng hơn. Vế trước nêu một điều kiện, thường là bất lợi hoặc giả định; vế sau có 也, cho biết kết quả vẫn không thay đổi. Tiếng Việt dịch là dù cho… cũng…."),
         F(1, "Ví dụ một, từ bài khóa: 作为一个外乡人，纵然使出浑身解数，在繁华都市的边缘，也难免感到诸多无奈与彷徨。 Là người nơi khác đến, dù có trổ hết bản lĩnh, cũng khó tránh khỏi bất lực và hoang mang."),
         F(2, "Ví dụ hai: 纵然未来困难重重，我们也要勇往直前。 Dù tương lai muôn vàn khó khăn, chúng ta cũng phải dũng cảm tiến lên. 困难重重 là khó khăn chồng chất, 勇往直前 là dũng cảm tiến thẳng về phía trước."),
         F(3, "Ví dụ ba: 互联网大大缩短了人和人之间的距离，纵然两人相隔千里，消息也可以瞬间送达。 Internet đã rút ngắn khoảng cách giữa người với người, dù hai người cách nhau nghìn dặm, tin tức cũng có thể đến nơi trong chớp mắt.")])

add("bullets", section="Câu mẫu 重点句型", title="3. ……固然……，可（是）/ 但（是）…… – đành rằng… nhưng…", size=34,
    items=["Nhượng bộ: thừa nhận ý A là đúng, rồi chuyển sang ý B – trọng tâm ở B; 固然 thường đứng sau chủ ngữ",
           "理想固然很丰满，可现实却很骨感。",
           "大城市固然机遇良多，可小城市的慢节奏也让不少年轻人感到安心踏实。",
           "这种“一刀切”的做法固然省事，但从长期来看对我们的事业发展不利。"],
    say=["Câu mẫu thứ ba: 固然……，可是…….",
         F(0, "固然 biểu thị thừa nhận một sự thật, rồi vế sau dùng 可是 hoặc 但是 để chuyển ý. Người nói không phủ nhận ý thứ nhất, nhưng điều muốn nhấn mạnh nằm ở vế sau. 固然 thường đứng sau chủ ngữ. Tiếng Việt dịch là đành rằng… nhưng…, tất nhiên là… nhưng…."),
         F(1, "Ví dụ một, từ bài khóa: 理想固然很丰满，可现实却很骨感。 Lý tưởng đành là rất đẹp, nhưng hiện thực lại rất phũ phàng. Vế sau thường có thêm 却 hay 也."),
         F(2, "Ví dụ hai: 大城市固然机遇良多，可小城市的慢节奏也让不少年轻人感到安心踏实。 Thành phố lớn đành là nhiều cơ hội, nhưng nhịp sống chậm của thành phố nhỏ cũng khiến nhiều bạn trẻ thấy yên lòng, vững dạ. 良多 là rất nhiều, văn viết."),
         F(3, "Ví dụ ba: 这种一刀切的做法固然省事，但从长期来看对我们的事业发展不利。 Cách làm cào bằng như thế này đành là đỡ việc, nhưng về lâu dài thì bất lợi cho sự nghiệp của chúng ta. 一刀切 là một nhát dao cắt, tức là cào bằng, áp dụng một kiểu cho mọi trường hợp.")])

add("bullets", chapter="Câu mẫu: 不复 · 况且 · 被/为……所", section="Câu mẫu 重点句型", title="4. ……不复…… – không còn… nữa  ·  5. 况且 – hơn nữa", size=33,
    items=["## 不复 + động từ (văn viết): không còn … nữa – 不复存在 · 不复相见",
           "当年玩耍的小河堆满垃圾，农村“田园牧歌式”的生活不复存在。",
           "如果太阳不复存在，那么地球上所有的生命都无法存活下去。",
           "虽然今后同学们可能不复相见，但大家的情谊永远会被铭记于心。",
           "## 况且: đứng đầu vế sau, bổ sung thêm một lý do",
           "他已经29岁，对于一个想成为电影工作者的人来说年龄的确偏大，况且他也没有任何跟电影相关的工作经验。",
           "在中国，大学生打工的工资并不高，况且，我也怕耽误学习，所以只能在假期偶尔做兼职。"],
    say=["Câu mẫu thứ tư là 不复.",
         F(0, "不复 là cách nói văn viết, nghĩa là không còn… nữa, đứng trước động từ. Kết hợp hay gặp nhất là 不复存在, không còn tồn tại nữa, và 不复相见, không còn gặp lại nhau nữa."),
         F(1, "Ví dụ một, từ bài khóa: 当年玩耍的小河堆满垃圾，农村田园牧歌式的生活不复存在。 Cuộc sống điền viên nơi thôn quê không còn tồn tại nữa."),
         F(2, "Ví dụ hai: 如果太阳不复存在，那么地球上所有的生命都无法存活下去。 Nếu mặt trời không còn tồn tại, thì mọi sự sống trên Trái Đất đều không thể tiếp tục tồn tại."),
         F(3, "Ví dụ ba: 虽然今后同学们可能不复相见，但大家的情谊永远会被铭记于心。 Tuy sau này các bạn có thể không còn gặp lại nhau, nhưng tình bạn của mọi người sẽ mãi khắc ghi trong lòng."),
         F(4, "Câu mẫu thứ năm là 况且, các bạn đã học ở giáo trình HSK sáu: đứng đầu vế sau, bổ sung thêm một lý do. Ví dụ trong bài khóa: 教育、医疗等公共性服务相对薄弱，况且农业生产高投入、低回报."),
         F(5, "Ví dụ: 他已经二十九岁，对于一个想成为电影工作者的人来说年龄的确偏大，况且他也没有任何跟电影相关的工作经验。 Anh ấy đã hai mươi chín tuổi, với người muốn làm điện ảnh thì tuổi quả là hơi lớn, hơn nữa anh ấy cũng không có chút kinh nghiệm nào liên quan đến điện ảnh."),
         F(6, "Ví dụ: 在中国，大学生打工的工资并不高，况且，我也怕耽误学习，所以只能在假期偶尔做兼职。 Ở Trung Quốc, lương làm thêm của sinh viên không cao, vả lại tôi cũng sợ ảnh hưởng việc học, nên chỉ thỉnh thoảng làm thêm vào kỳ nghỉ. Các bạn để ý, sau 况且 có thể có dấu phẩy.")])

add("bullets", section="Câu mẫu 重点句型", title="6. 被 / 为 + tác nhân + 所 + động từ – bị động văn viết", size=34,
    items=["Chữ 所 đứng trước động từ (thường hai âm tiết), làm câu bị động trang trọng hơn; 为 đọc wéi",
           "对于新生代农民工来说，他们向往城市，却不被城市所接纳。",
           "看问题不要只停留在表面，或被外部因素所干扰，应该看到其实质。",
           "在新年音乐会上，观众们不由自主地为那独具艺术魅力的音乐所感染。"],
    say=["Câu mẫu thứ sáu: 被……所…… và 为……所…….",
         F(0, "Đây là câu bị động văn viết. Sau 被 hoặc 为 là tác nhân, sau đó là chữ 所, rồi đến động từ, thường là động từ hai âm tiết. Chữ 为 ở đây đọc thanh hai, wéi. So với câu bị động thường, mẫu này trang trọng hơn, hay gặp trong văn viết, báo chí."),
         F(1, "Ví dụ một, từ bài khóa: 对于新生代农民工来说，他们向往城市，却不被城市所接纳。 Họ hướng về thành phố, nhưng lại không được thành phố đón nhận."),
         F(2, "Ví dụ hai: 看问题不要只停留在表面，或被外部因素所干扰，应该看到其实质。 Nhìn nhận vấn đề đừng chỉ dừng ở bề mặt, hay bị các yếu tố bên ngoài làm nhiễu, mà phải thấy được bản chất của nó."),
         F(3, "Ví dụ ba: 在新年音乐会上，观众们不由自主地为那独具艺术魅力的音乐所感染。 Trong buổi hòa nhạc mừng năm mới, khán giả bất giác bị lay động bởi thứ âm nhạc mang sức hút nghệ thuật độc đáo ấy. 不由自主 là bất giác, không tự chủ được.")])

add("bullets", chapter="Câu mẫu: V准 · 这样一来", section="Câu mẫu 重点句型", title="7. Động từ + 准  ·  8. ……，这样一来，……", size=33,
    items=["## V + 准: làm cho đúng, cho chính xác – 选准 · 看准 · 找准 · 瞄准",
           "新生代农民工自己也要量力而行，选准适宜发展的地方安居乐业。",
           "这位老总看准了他的发展潜力，向他抛出了橄榄枝。",
           "要治愈教育乱收费这一顽疾，首先要找准“病因”，然后对症下药。",
           "## 这样一来: như vậy thì, làm thế thì – dẫn ra kết quả của việc vừa nêu",
           "做一个有用的人，每天积极生活，力求有所作为，这样一来，生命便有了意义。",
           "不要把工作的结果看得过重，多想其有趣之处，平心静气，这样一来，工作往往做得更好。"],
    say=["Câu mẫu thứ bảy: động từ cộng 准.",
         F(0, "准 làm bổ ngữ kết quả, nghĩa là chính xác, đúng. 选准 là chọn đúng, 看准 là nhìn trúng, nhận định đúng, 找准 là tìm ra đúng chỗ. Nó nhấn mạnh hành động đạt được độ chính xác."),
         F(1, "Ví dụ một, từ bài khóa: 新生代农民工自己也要量力而行，选准适宜发展的地方安居乐业。 Phải chọn đúng nơi thích hợp để phát triển."),
         F(2, "Ví dụ hai: 这位老总看准了他的发展潜力，向他抛出了橄榄枝。 Vị giám đốc này đã nhìn trúng tiềm năng phát triển của anh ấy, và chìa cành ô liu mời anh về làm. 抛出橄榄枝 là chìa cành ô liu, tức là ngỏ ý mời gọi, hợp tác."),
         F(3, "Ví dụ ba: 要治愈教育乱收费这一顽疾，首先要找准病因，然后对症下药。 Muốn chữa căn bệnh dai dẳng thu phí tràn lan trong giáo dục, trước hết phải tìm đúng nguyên nhân, rồi bốc thuốc đúng bệnh."),
         F(4, "Câu mẫu thứ tám: 这样一来, nghĩa là như vậy thì, làm như thế thì. Nó đứng đầu vế sau, nối hành động vừa nêu với kết quả của nó. Trong bài khóa: 选准适宜发展的地方安居乐业。这样一来，他们才不会在偌大的城市中迷失自己。"),
         F(5, "Ví dụ: 做一个有用的人，每天积极生活，力求有所作为，这样一来，生命便有了意义。 Làm một người có ích, mỗi ngày sống tích cực, cố gắng làm nên việc, như vậy cuộc đời liền có ý nghĩa."),
         F(6, "Ví dụ: 不要把工作的结果看得过重，多想其有趣之处，平心静气，这样一来，工作往往做得更好。 Đừng quá nặng nề về kết quả công việc, hãy nghĩ nhiều đến những điểm thú vị của nó, giữ lòng bình thản, như vậy công việc thường lại làm tốt hơn.")])

# ======================= KẾT HỢP TỪ =======================
add("bullets", chapter="Kết hợp từ (词语搭配)", section="Kết hợp từ 词语搭配", title="Kết hợp từ (1): 承载 · 匆匆 · 薄弱", size=34,
    items=["## 承载：～回忆 · ～祝福 · ～梦想 · ～希望 · ～重量 · ～压力",
           "这条短信深深地触动了我，因为它承载了朋友真情的祝福。",
           "## 匆匆：～返回 · ～离开 · 来去～ · 时光～ · 脚步～",
           "时光匆匆，一转眼两个孩子都已经上了初中了。",
           "## 薄弱：相对～ · ～环节 · ～点 · ～之处 · 意志～",
           "意志薄弱的人是经受不住艰苦生活中的种种考验的。"],
    say=["Tiếp theo là phần kết hợp từ, 词语搭配. Ở trình độ cao cấp, biết nghĩa của từ chưa đủ, mà còn phải biết nó hay đi với những từ nào. Các bạn hãy học cả cụm nhé.",
         F(0, "Từ thứ nhất: 承载. Hay đi với 回忆，祝福，梦想，希望，重量，压力. Ví dụ trong bài: 农村是他们的根，是承载着他们童年回忆的地方。"),
         F(1, "Ví dụ khác: 这条短信深深地触动了我，因为它承载了朋友真情的祝福。 Tin nhắn này làm tôi vô cùng xúc động, vì nó chứa đựng lời chúc chân thành của người bạn."),
         F(2, "Từ thứ hai: 匆匆. Hay gặp 匆匆返回，匆匆离开，来去匆匆，时光匆匆，脚步匆匆. Ví dụ trong bài: 待上四五天便匆匆返回城市。"),
         F(3, "Ví dụ khác: 时光匆匆，一转眼两个孩子都已经上了初中了。 Thời gian vội trôi, chớp mắt hai đứa trẻ đều đã lên trung học cơ sở rồi."),
         F(4, "Từ thứ ba: 薄弱. Hay gặp 相对薄弱，薄弱环节，薄弱点，薄弱之处，意志薄弱. Ví dụ trong bài: 教育、医疗等公共性服务相对薄弱. Và: 环保目前仍是我们工作中的薄弱环节。"),
         F(5, "Ví dụ khác: 意志薄弱的人是经受不住艰苦生活中的种种考验的。 Người ý chí yếu đuối không chịu nổi những thử thách của cuộc sống gian khổ.")])

add("bullets", section="Kết hợp từ 词语搭配", title="Kết hợp từ (2): 不争的 · 破解 · 接纳", size=34,
    items=["## 不争的：～事实",
           "几乎每个生态系统中都存在微塑料碎片，微塑料污染已是一个不争的事实。",
           "## 破解：～农民工之困 · ～难题 · ～困局 · ～密码",
           "要从根本上破解劳资关系紧张的难题，就必须从制度创新入手。",
           "## 接纳：～移民 · ～观众 · ～建议 · ～他人 · ～自己",
           "我认为他没有理由不接纳我们如此真诚的建议。"],
    say=[F(0, "Từ thứ tư: 不争的, gần như chỉ đi với 事实. Ví dụ trong bài: 这都是不争的事实。"),
         F(1, "Ví dụ khác: 几乎每个生态系统中都存在微塑料碎片，微塑料污染已是一个不争的事实。 Hầu như hệ sinh thái nào cũng có mảnh vi nhựa, ô nhiễm vi nhựa đã là một sự thật không thể chối cãi."),
         F(2, "Từ thứ năm: 破解. Hay gặp 破解农民工之困，破解难题，破解困局，破解密码."),
         F(3, "Ví dụ: 要从根本上破解劳资关系紧张的难题，就必须从制度创新入手。 Muốn giải quyết tận gốc bài toán quan hệ căng thẳng giữa chủ và thợ, thì phải bắt tay từ việc đổi mới chế độ. Và: 很多黑客只是通过分析用户的心理，就能破解密码, nhiều tin tặc chỉ cần phân tích tâm lý người dùng là bẻ được mật khẩu."),
         F(4, "Từ thứ sáu: 接纳. Hay gặp 接纳移民，接纳观众，接纳建议，接纳他人，接纳自己. Ví dụ: 新楼盘将接纳九百七十六户住户, khu nhà mới sẽ tiếp nhận chín trăm bảy mươi sáu hộ dân."),
         F(5, "Ví dụ khác: 我认为他没有理由不接纳我们如此真诚的建议。 Tôi cho rằng anh ấy không có lý do gì để không tiếp thu đề nghị chân thành như vậy của chúng ta. 接纳自己 là chấp nhận chính mình, một cụm rất hay dùng trong tâm lý học.")])

add("bullets", section="Kết hợp từ 词语搭配", title="Kết hợp từ (3): 日益 · 纳入 · 遭受", size=34,
    items=["## 日益：～疏远 · ～好转 · ～强盛 · ～激烈 · ～严重",
           "奶奶的病情日益好转，过几天就可以出院了。",
           "## 纳入：～发展规划 · ～计划 · ～体系 · ～系统 · ～名单 · ～议题",
           "政府将防治荒漠化作为国土整治的重点工程，纳入21世纪国民经济和社会发展计划。",
           "## 遭受（六级）：～歧视 · ～重创 · ～挫折",
           "当我们遭受挫折的时候，应该坚定自己的信念，而不是怨天尤人。"],
    say=[F(0, "Từ thứ bảy: 日益. Hay gặp 日益疏远，日益好转，日益强盛，日益激烈，日益严重."),
         F(1, "Ví dụ: 奶奶的病情日益好转，过几天就可以出院了。 Bệnh tình của bà ngày một chuyển biến tốt, vài hôm nữa là có thể xuất viện. Và: 该地区的空气污染日益严重，很多人外出都戴上口罩。"),
         F(2, "Từ thứ tám: 纳入. Hay gặp 纳入发展规划，纳入计划，纳入体系，纳入系统，纳入名单，纳入议题."),
         F(3, "Ví dụ: 政府将防治荒漠化作为国土整治的重点工程，纳入二十一世纪国民经济和社会发展计划。 Chính phủ coi phòng chống sa mạc hóa là công trình trọng điểm của việc chỉnh trị đất đai, đưa vào kế hoạch phát triển kinh tế quốc dân và xã hội thế kỷ hai mươi mốt. Một ví dụ khác: 二零二一年有十八种抗肿瘤药物被纳入国家医保药品目录, năm hai nghìn không trăm hai mươi mốt, mười tám loại thuốc chống ung thư được đưa vào danh mục thuốc bảo hiểm y tế quốc gia."),
         F(4, "Từ thứ chín: 遭受, đã học ở cấp sáu. Hay gặp 遭受歧视，遭受重创，遭受挫折. Ví dụ trong bài: 莫让他们遭受冷漠的社会歧视. Và: 在家乡遭受洪灾重创之时，他慷慨捐款, khi quê nhà bị lũ lụt tàn phá nặng nề, anh ấy đã hào phóng quyên góp."),
         F(5, "Ví dụ khác: 当我们遭受挫折的时候，应该坚定自己的信念，而不是怨天尤人。 Khi gặp thất bại, chúng ta nên giữ vững niềm tin của mình, chứ không phải oán trời trách người.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 课后练习", title="Bài tập 1: Chọn từ điền vào chỗ trống (1)", reveal=True, size=33,
    items=["## Từ cho sẵn: 繁华 · 迷茫 · 承载 · 不争 · 浑身解数 · 一窍不通 · 望尘莫及 · 量力而行 · 安居乐业",
           "(1) 大城市竞争十分激烈，这是个（ ）的事实。",
           "Đáp án: 不争",
           "(2) 对于心理学我是（ ），所以不敢随意评论。",
           "Đáp án: 一窍不通",
           "(3) 在这个风景优美的小城里，人们（ ）。",
           "Đáp án: 安居乐业",
           "(4) 没有农民工的汗水，就没有城市的（ ）。",
           "Đáp án: 繁华"],
    say=["Phần luyện tập, 课后练习, sách gọi là 趁热打铁, nghĩa là rèn sắt khi còn nóng. Bài tập một: chọn từ thích hợp điền vào chỗ trống.",
         F(0, "Có chín từ: 繁华，迷茫，承载，不争，浑身解数，一窍不通，望尘莫及，量力而行，安居乐业. Mỗi từ dùng một lần."),
         F(1, "Câu một: 大城市竞争十分激烈，这是个什么的事实。 Cạnh tranh ở thành phố lớn rất gay gắt, đây là một sự thật thế nào? Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 不争. 这是个不争的事实, đây là sự thật không thể chối cãi."),
         F(3, "Câu hai: 对于心理学我是什么，所以不敢随意评论。 Về tâm lý học tôi thế nào, nên không dám tùy tiện bình luận."),
         F(4, "Đáp án: 一窍不通. Tôi hoàn toàn mù tịt về tâm lý học. Mẫu 对……一窍不通."),
         F(5, "Câu ba: 在这个风景优美的小城里，人们什么。 Trong thành phố nhỏ phong cảnh tươi đẹp này, người dân thế nào?"),
         F(6, "Đáp án: 安居乐业. Người dân an cư lạc nghiệp."),
         F(7, "Câu bốn: 没有农民工的汗水，就没有城市的什么。 Không có mồ hôi của người lao động nhập cư, thì không có cái gì của thành phố?"),
         F(8, "Đáp án: 繁华. 就没有城市的繁华, thì không có sự phồn hoa của thành phố. Ở đây 繁华 được dùng như danh từ.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 1: Chọn từ điền vào chỗ trống (2)", reveal=True, size=32,
    items=["(5) 信仰是无言的指路人，让我们在（ ）中找到出路。",
           "Đáp án: 迷茫",
           "(6) 金灿灿的稻田中那一串串饱满的稻子，（ ）着农民一整年的梦想。",
           "Đáp án: 承载",
           "(7) 为了在市场竞争中占有一席之地，商家们动足了脑筋，使出了（ ）。",
           "Đáp án: 浑身解数",
           "(8) 人要有自知之明，处世做人，要（ ），不强求自己去做超出能力以外的事情。",
           "Đáp án: 量力而行",
           "(9) 近年来，他发表的作品无论从质量上还是数量上说，都是我们（ ）的。",
           "Đáp án: 望尘莫及"],
    say=[F(0, "Câu năm: 信仰是无言的指路人，让我们在什么中找到出路。 Niềm tin là người dẫn đường không lời, giúp ta tìm ra lối thoát giữa cái gì?"),
         F(1, "Đáp án: 迷茫. 在迷茫中找到出路, tìm ra lối thoát giữa lúc mất phương hướng."),
         F(2, "Câu sáu: 金灿灿的稻田中那一串串饱满的稻子，什么着农民一整年的梦想。 Những bông lúa trĩu hạt trên cánh đồng vàng óng, thế nào ước mơ cả năm của người nông dân?"),
         F(3, "Đáp án: 承载. 承载着农民一整年的梦想, chứa đựng ước mơ cả năm trời của nhà nông."),
         F(4, "Câu bảy: 为了在市场竞争中占有一席之地，商家们动足了脑筋，使出了什么。 Để giành một chỗ đứng trong cạnh tranh thị trường, các nhà buôn đã vắt óc suy nghĩ, tung ra cái gì?"),
         F(5, "Đáp án: 浑身解数. 使出了浑身解数, trổ hết mọi bản lĩnh. Động từ 使出 là gợi ý quan trọng."),
         F(6, "Câu tám: 人要有自知之明，处世做人，要什么，不强求自己去做超出能力以外的事情。 Con người phải biết mình, đối nhân xử thế phải thế nào, không ép mình làm những việc vượt quá khả năng?"),
         F(7, "Đáp án: 量力而行. Phải liệu sức mà làm. Vế sau 不强求自己去做超出能力以外的事情 chính là lời giải thích của thành ngữ này."),
         F(8, "Câu chín: 近年来，他发表的作品无论从质量上还是数量上说，都是我们什么的。 Mấy năm gần đây, tác phẩm anh ấy công bố, dù xét về chất lượng hay số lượng, đều là thứ chúng tôi thế nào?"),
         F(9, "Đáp án: 望尘莫及. 都是我们望尘莫及的, đều là thứ chúng tôi không theo kịp.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn đáp án đúng (1)", reveal=True, size=33,
    items=["(1) 随着大批毕业生（ ）长期以来号称“世界工厂”的经济体中，人们对市场吸收能力和未来政治局势的担忧也开始加深。\nA.涌入 B.流入 C.深入 D.进入",
           "Đáp án: A. 涌入 – số lượng lớn ồ ạt đổ vào",
           "(2) 在这人来人往的（ ）都市，他心中却感到空落落的，有一种说不出的孤独与迷茫。\nA.繁荣 B.繁华 C.繁忙 D.繁多",
           "Đáp án: B. 繁华 – 繁华都市, đô thị phồn hoa",
           "(3)（ ）以后你成了领导，也没有权利要求别人放弃自己的尊严。\nA.尽管 B.不然 C.虽然 D.纵然",
           "Đáp án: D. 纵然 – giả định, đi với 也"],
    say=["Bài tập hai: chọn đáp án đúng.",
         F(0, "Câu một: 随着大批毕业生什么长期以来号称世界工厂的经济体中，人们对市场吸收能力和未来政治局势的担忧也开始加深。 Cùng với việc một lượng lớn sinh viên tốt nghiệp thế nào vào nền kinh tế lâu nay được mệnh danh là công xưởng của thế giới, nỗi lo của mọi người về khả năng hấp thụ của thị trường cũng tăng lên. Bốn lựa chọn: 涌入，流入，深入，进入."),
         F(1, "Đáp án: A, 涌入. 大批 là số lượng lớn, nên phải dùng 涌入, ồ ạt đổ vào. 流入 thường nói về chất lỏng, tiền vốn, hàng hóa; 深入 là đi sâu vào; 进入 thì trung tính, không thể hiện được số lượng lớn."),
         F(2, "Câu hai: 在这人来人往的什么都市，他心中却感到空落落的，有一种说不出的孤独与迷茫。 Giữa đô thị thế nào người qua kẻ lại này, lòng anh lại thấy trống trải, cô đơn và mông lung không nói thành lời. Bốn lựa chọn: 繁荣，繁华，繁忙，繁多."),
         F(3, "Đáp án: B, 繁华. 繁华都市 là kết hợp cố định. 繁荣 thường nói về kinh tế, thị trường; 繁忙 là bận rộn, nói về công việc, giao thông; 繁多 là nhiều, nói về chủng loại."),
         F(4, "Câu ba: 什么以后你成了领导，也没有权利要求别人放弃自己的尊严。 Thế nào sau này bạn trở thành lãnh đạo, cũng không có quyền đòi người khác từ bỏ lòng tự trọng. Bốn lựa chọn: 尽管，不然，虽然，纵然."),
         F(5, "Đáp án: D, 纵然. Việc trở thành lãnh đạo là giả định chưa xảy ra, và vế sau có 也, nên dùng 纵然. 尽管 và 虽然 nói về sự thật đã có, vế sau thường dùng 但是.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn đáp án đúng (2)", reveal=True, size=33,
    items=["(4) 当爱情（ ）了太多不切实际的希望，它也会幻灭得更快。\nA.承载 B.承受 C.承担 D.接受",
           "Đáp án: A. 承载 – chứa đựng, gánh (hy vọng)",
           "(5) 警官使出浑身解数，也（ ）不了这如乱麻似的谜案。\nA.解决 B.解除 C.破解 D.解开",
           "Đáp án: C. 破解 – phá án, giải mã điều bí ẩn",
           "(6) 该国若要缓解人口老化问题，保持就业人口和退休人口之间的平衡关系，就需要（ ）外来移民。\nA.接待 B.采纳 C.采用 D.接纳",
           "Đáp án: D. 接纳 – tiếp nhận người (移民)"],
    say=[F(0, "Câu bốn: 当爱情什么了太多不切实际的希望，它也会幻灭得更快。 Khi tình yêu thế nào quá nhiều hy vọng viển vông, nó cũng sẽ tan vỡ nhanh hơn. Bốn lựa chọn: 承载，承受，承担，接受."),
         F(1, "Đáp án: A, 承载. 承载希望 là chứa đựng, gửi gắm hy vọng, đúng như phần kết hợp từ vừa học. 承受 là chịu đựng áp lực, đau khổ; 承担 là gánh vác trách nhiệm; 接受 là tiếp nhận."),
         F(2, "Câu năm: 警官使出浑身解数，也什么不了这如乱麻似的谜案。 Viên cảnh sát trổ hết tài nghệ cũng không thể thế nào vụ án bí ẩn rối như tơ vò này. Bốn lựa chọn: 解决，解除，破解，解开."),
         F(3, "Đáp án: C, 破解. Với 谜案, vụ án bí ẩn, ta dùng 破解, phá giải. 解除 là gỡ bỏ, như 解除合同; 解开 là cởi ra, như 解开绳子."),
         F(4, "Câu sáu: 该国若要缓解人口老化问题，保持就业人口和退休人口之间的平衡关系，就需要什么外来移民。 Nước này nếu muốn giảm bớt vấn đề già hóa dân số, giữ cân bằng giữa dân số lao động và dân số nghỉ hưu, thì cần thế nào người nhập cư từ bên ngoài. Bốn lựa chọn: 接待，采纳，采用，接纳."),
         F(5, "Đáp án: D, 接纳. 接纳移民 là tiếp nhận người nhập cư. 接待 là tiếp đón khách; 采纳 là tiếp thu ý kiến; 采用 là áp dụng phương pháp, kỹ thuật.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ và câu mẫu cho sẵn để trả lời", reveal=True, size=32,
    items=["(1) 为什么新生代农民工在城市感到无奈和彷徨 （纵然……也……）",
           "Đáp án gợi ý: 因为房价和生活成本太高，又没有稳定的工作和社会保障，作为外乡人，他们纵然使出浑身解数，也很难真正融入城市。",
           "(2) 为什么新生代农民工不想留在农村？（况且……，不争的）",
           "Đáp án gợi ý: 农村的基础设施落后，公共服务薄弱，况且农业生产高投入、低回报，这都是不争的事实。再加上他们已经习惯了城市的生活。",
           "(3) 新生代农民工怎样做才不会在城市迷失自己？（……这样一来……）",
           "Đáp án gợi ý: 他们要量力而行，选准适宜自己发展的地方安居乐业，这样一来，就不会在偌大的城市中迷失自己。"],
    say=["Bài tập ba: dùng từ ngữ và câu mẫu cho sẵn để trả lời câu hỏi. Đây là câu hỏi mở, thầy đưa ra đáp án gợi ý.",
         F(0, "Câu một: 为什么新生代农民工在城市感到无奈和彷徨？ Vì sao lao động nhập cư thế hệ mới cảm thấy bất lực và hoang mang ở thành phố? Dùng mẫu 纵然……也……. Các bạn tạm dừng và thử trả lời nhé."),
         F(1, "Đáp án gợi ý: 因为房价和生活成本太高，又没有稳定的工作和社会保障，作为外乡人，他们纵然使出浑身解数，也很难真正融入城市。 Vì giá nhà và chi phí sinh hoạt quá cao, lại không có việc làm ổn định và bảo hiểm xã hội, là người nơi khác đến, dù có trổ hết bản lĩnh, họ cũng rất khó thật sự hòa nhập vào thành phố."),
         F(2, "Câu hai: 为什么新生代农民工不想留在农村？ Vì sao họ không muốn ở lại nông thôn? Dùng 况且 và 不争的."),
         F(3, "Đáp án gợi ý: 农村的基础设施落后，公共服务薄弱，况且农业生产高投入、低回报，这都是不争的事实。再加上他们已经习惯了城市的生活。 Hạ tầng nông thôn lạc hậu, dịch vụ công yếu kém, hơn nữa làm nông đầu tư cao mà thu về thấp, đó là sự thật không thể chối cãi. Thêm vào đó, họ đã quen với cuộc sống thành phố."),
         F(4, "Câu ba: 新生代农民工怎样做才不会在城市迷失自己？ Họ phải làm thế nào mới không đánh mất mình ở thành phố? Dùng 这样一来."),
         F(5, "Đáp án gợi ý: 他们要量力而行，选准适宜自己发展的地方安居乐业，这样一来，就不会在偌大的城市中迷失自己。 Họ phải liệu sức mà làm, chọn đúng nơi thích hợp để phát triển mà an cư lạc nghiệp, như vậy sẽ không đánh mất mình giữa thành phố rộng lớn.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Dùng từ cho sẵn điền vào đoạn văn (1)", reveal=True, size=33,
    items=["## Từ cho sẵn: 涌入 · 歧视 · 接纳 · 疏远 · 定居 · 打拼 · 诸多 · 进退两难 · 落叶归根",
           "在第一代农民工逐渐退出历史舞台、___的同时，新生代农民工不断___城市，正成为当今农民工的主体。",
           "Đáp án: 落叶归根 · 涌入",
           "第一代农民工大多在城市赚了钱后便会返乡，并没有超出自己所在阶层的想法。而随着新生代农民工对土地情感的___，他们不再视“土”为谋生的根基，甚至认为以土地为生是失败的体现。他们表现出对城市生活更大的向往，以及更强的融入城市的意愿，希望能通过自己的___，最终___城市。",
           "Đáp án: 疏远 · 打拼 · 定居"],
    say=["Bài tập bốn: dùng chín từ cho sẵn điền vào đoạn văn. Đoạn văn này tóm tắt lại chính nội dung bài khóa.",
         F(0, "Chín từ là: 涌入，歧视，接纳，疏远，定居，打拼，诸多，进退两难，落叶归根."),
         F(1, "Câu đầu: 在第一代农民工逐渐退出历史舞台、什么的同时，新生代农民工不断什么城市，正成为当今农民工的主体。 Các bạn tạm dừng và điền nhé."),
         F(2, "Đáp án: 落叶归根 và 涌入. 在第一代农民工逐渐退出历史舞台、落叶归根的同时，新生代农民工不断涌入城市。 Trong khi lao động đời đầu dần rút khỏi vũ đài lịch sử, lá rụng về cội, thì lao động thế hệ mới không ngừng đổ về thành phố, đang trở thành lực lượng chủ yếu."),
         F(3, "Đoạn tiếp theo: 第一代农民工大多在城市赚了钱后便会返乡，并没有超出自己所在阶层的想法。而随着新生代农民工对土地情感的什么，他们不再视土为谋生的根基，甚至认为以土地为生是失败的体现。他们表现出对城市生活更大的向往，以及更强的融入城市的意愿，希望能通过自己的什么，最终什么城市。"),
         F(4, "Đáp án: 疏远，打拼，定居. 对土地情感的疏远, tình cảm với đất đai ngày càng xa cách; 通过自己的打拼，最终定居城市, bằng sự bươn chải của mình, cuối cùng định cư ở thành phố. Chú ý mẫu 视A为B, coi A là B: 不再视土为谋生的根基, không còn coi đất đai là nền tảng mưu sinh.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Dùng từ cho sẵn điền vào đoạn văn (2)", reveal=True, size=34,
    items=["然而，这种希望的实现却面临着___困境。新生代农民工一方面同他们的父辈一样，遭受身份___、制度排斥等不公平的待遇，很难被城市___；另一方面，他们失去了对乡土世界的认同感，也无法回归乡村，因此处于___的窘境之中。",
           "Đáp án: 诸多 · 歧视 · 接纳 · 进退两难"],
    say=[F(0, "Đoạn cuối: 然而，这种希望的实现却面临着什么困境。新生代农民工一方面同他们的父辈一样，遭受身份什么、制度排斥等不公平的待遇，很难被城市什么；另一方面，他们失去了对乡土世界的认同感，也无法回归乡村，因此处于什么的窘境之中。 Các bạn điền bốn từ còn lại nhé."),
         F(1, "Đáp án: 诸多，歧视，接纳，进退两难. 面临着诸多困境, đối mặt với nhiều khó khăn; 遭受身份歧视, bị kỳ thị vì thân phận; 很难被城市接纳, khó được thành phố đón nhận; 处于进退两难的窘境之中, rơi vào tình thế quẫn bách tiến thoái lưỡng nan. Các bạn thấy không, các kết hợp 遭受歧视，被城市接纳 đều vừa học ở phần kết hợp từ.")])

# ======================= THẢO LUẬN =======================
add("bullets", chapter="Thảo luận", section="Thảo luận 讨论", title="Thảo luận: liên hệ Việt Nam", reveal=True, size=33,
    items=["(1) 你们国家城乡居民的差别大吗？体现在哪些方面？",
           "Đáp án gợi ý: 越南的城乡差别也比较大，主要体现在收入、教育、医疗和基础设施等方面。很多农村年轻人到河内、胡志明市或工业区打工。",
           "(2) 政府是否有责任缩小区域间发展的不平衡？",
           "Đáp án gợi ý: 我认为政府有这个责任。政府应该加大对农村的财政投入，改善基础设施和公共服务，同时让外来务工人员共享城市发展的红利。",
           "(3) 如果你是一位新生代农民工，你会留在城市还是回到农村？",
           "Đáp án gợi ý: 我会量力而行。如果在城市有稳定的工作，我就留下来打拼；如果没有，回家乡创业也是一个不错的选择。"],
    say=["Bây giờ chúng ta cùng thảo luận, dựa trên các câu hỏi trước bài và nội dung bài khóa. Thầy đưa ra đáp án gợi ý bằng tiếng Trung, các bạn hãy thử nói theo ý mình trước nhé.",
         F(0, "Câu một: 你们国家城乡居民的差别大吗？体现在哪些方面？ Ở nước bạn, khác biệt giữa thành thị và nông thôn có lớn không?"),
         F(1, "Gợi ý: 越南的城乡差别也比较大，主要体现在收入、教育、医疗和基础设施等方面。很多农村年轻人到河内、胡志明市或工业区打工。 Ở Việt Nam, khác biệt giữa thành thị và nông thôn cũng khá lớn, chủ yếu ở thu nhập, giáo dục, y tế và hạ tầng. Nhiều bạn trẻ nông thôn lên Hà Nội, Thành phố Hồ Chí Minh hay các khu công nghiệp làm thuê. Họ cũng gặp những nỗi lo rất giống bài khóa: thuê trọ chật chội, con cái đi học khó khăn, Tết mới về quê một lần."),
         F(2, "Câu hai: 政府是否有责任缩小区域间发展的不平衡？ Chính phủ có trách nhiệm thu hẹp chênh lệch phát triển giữa các vùng không?"),
         F(3, "Gợi ý: 我认为政府有这个责任。政府应该加大对农村的财政投入，改善基础设施和公共服务，同时让外来务工人员共享城市发展的红利。 Tôi cho rằng chính phủ có trách nhiệm này: tăng đầu tư ngân sách cho nông thôn, cải thiện hạ tầng và dịch vụ công, đồng thời để người lao động từ nơi khác đến cùng hưởng lợi ích của sự phát triển đô thị. Các bạn để ý, câu trả lời dùng lại rất nhiều từ của bài: 财政投入，共享红利."),
         F(4, "Câu ba, thầy thêm vào: 如果你是一位新生代农民工，你会留在城市还是回到农村？ Nếu bạn là một lao động nhập cư thế hệ mới, bạn sẽ ở lại thành phố hay về nông thôn?"),
         F(5, "Gợi ý: 我会量力而行。如果在城市有稳定的工作，我就留下来打拼；如果没有，回家乡创业也是一个不错的选择。 Tôi sẽ liệu sức mà làm. Nếu ở thành phố có việc ổn định, tôi sẽ ở lại bươn chải; nếu không, về quê khởi nghiệp cũng là một lựa chọn không tồi. 创业 là khởi nghiệp.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết", section="Tổng kết", title="Tổng kết bài 2.1", size=34,
    items=["Nội dung: 新生代农民工 – 向往城市，却不被城市所接纳；根在农村，却对农村日益疏远",
           "Từ vựng trọng tâm: 游离 · 边缘化 · 涌入 · 纵然 · 彷徨 · 徘徊 · 迷茫 · 固然 · 承载 · 薄弱 · 不争 · 打拼 · 破解 · 接纳 · 日益 · 疏远 · 壁垒 · 瓶颈 · 纳入 · 歧视 · 适宜",
           "Thành ngữ: 浑身解数 · 望尘莫及 · 逢年过节 · 一窍不通 · 落叶归根 · 进退两难 · 量力而行 · 安居乐业",
           "Câu mẫu: （以）……居多 · 纵然……也…… · ……固然……，可是…… · 不复 · 况且 · 被/为……所 · V准 · 这样一来",
           "Bài tập về nhà: viết đoạn văn 200 chữ về lao động nhập cư ở Việt Nam, dùng ít nhất 3 câu mẫu"],
    say=["Chúng ta cùng tổng kết bài hai chấm một.",
         F(0, "Về nội dung: lao động nhập cư thế hệ mới hướng về thành phố nhưng không được thành phố đón nhận; gốc rễ ở nông thôn nhưng ngày càng xa cách nông thôn. Câu then chốt là: 他们向往城市，却不被城市所接纳；根在农村，却对农村日益疏远。"),
         F(1, "Về từ vựng, các bạn cần đặc biệt nhớ: 游离，边缘化，涌入，纵然，彷徨，徘徊，迷茫，固然，承载，薄弱，不争，打拼，破解，接纳，日益，疏远，壁垒，瓶颈，纳入，歧视，适宜. Và đừng quên những từ dễ nhầm như 彷徨，徘徊，适宜."),
         F(2, "Về thành ngữ: 浑身解数，望尘莫及，逢年过节，一窍不通，落叶归根，进退两难，量力而行，安居乐业. Nhiều thành ngữ rất gần với tiếng Việt, như tiến thoái lưỡng nan, an cư lạc nghiệp, lá rụng về cội."),
         F(3, "Về câu mẫu: 以……居多, chiếm đa số; 纵然……也……, dù cho… cũng…; 固然……可是……, đành rằng… nhưng…; 不复, không còn… nữa; 况且, hơn nữa; 被……所……, bị động văn viết; động từ cộng 准, làm cho đúng; và 这样一来, như vậy thì."),
         F(4, "Bài tập về nhà: các bạn hãy viết một đoạn văn khoảng hai trăm chữ, nói về lao động từ nông thôn ra thành phố ở Việt Nam: họ gặp những khó khăn gì, và xã hội nên giúp họ thế nào. Hãy dùng ít nhất ba câu mẫu vừa học, ví dụ 纵然……也……，固然……可是…… và 这样一来."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Bài sau, bài hai chấm hai, chúng ta sẽ chuyển từ người lao động trẻ sang người cao tuổi, với chủ đề 信息化社会：一个都不能少, Xã hội thông tin: không ai bị bỏ lại phía sau. Bài báo nói về việc giúp ông bà, cha mẹ vượt qua khoảng cách số trong thời đại điện thoại thông minh. Hẹn gặp lại các bạn. Chúc các bạn học tốt!"])

lesson = {
    "title": "顶石中文 – Bài 2.1: 融不进的城市，回不去的农村 (Thành phố không hòa nhập được, nông thôn không về được)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"身为": "身维",            # shēnwéi
                    "解数": "谢数",            # xièshù
                    "彷徨": "旁徨",            # pánghuáng
                    "上不了": "上不蓼",        # shàng bu liǎo
                    "朝": "潮",                # cháo (面朝黄土背朝天; mọi chỗ trong bài đều đọc cháo)
                    "待上": "呆上",            # dāi
                    "薄弱": "博弱",            # bóruò
                    "亟": "急",                # jí
                    "量力": "亮力",            # liànglì
                    "乐业": "勒业",            # lèyè
                    "承载": "承在",            # chéngzài
                    "为那": "维那",            # 为……所: wéi
                    "空落落": "空洛洛",        # kōngluòluò
                    "处世": "楚世",            # chǔshì
                    "处于": "楚于",            # chǔyú
                    "处境": "楚境",            # chǔjìng
                    "假期": "架期",            # jiàqī
                    "种种": "肿肿",            # zhǒngzhǒng
                    "重重": "虫虫",            # chóngchóng
                    "似的": "是的",            # shìde
                    "重创": "重疮",            # zhòngchuāng
                    "为谋生": "维谋生",        # 视……为: wéi
                    "为生": "维生",            # 以土地为生: wéi
                    "调控": "条控"},           # tiáokòng
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds21.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
