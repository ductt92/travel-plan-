#!/usr/bin/env python3
"""Kịch bản bài giảng 顶石中文 – Bài 5.3 «相亲鄙视链：爱情被黑得惨不忍睹». Chạy để sinh ds53.json."""
import json
import os

TAG = "顶石中文 · Bài 5.3 · 相亲鄙视链：爱情被黑得惨不忍睹"
slides = []


def add(type_, chapter=None, section="", **kw):
    s = {"type": type_, "section": section, **kw}
    if chapter:
        s["chapter"] = chapter
    slides.append(s)


def F(i, t, **kw):
    return {"t": t, "f": i, **kw}


# ======================= MỞ ĐẦU =======================
# Tên bài có 14 chữ, quá dài cho một dòng chữ cỡ lớn, nên tách làm hai dòng: zh + py (như Bài 40)
add("title", chapter="Mở đầu",
    top="顶石中文 – Đỉnh cao tiếng Trung",
    zh="相亲鄙视链", py="爱情被黑得惨不忍睹",
    vi="Bài 5.3: Chuỗi khinh miệt xem mắt – tình yêu bị bôi đen",
    sub="Xiāngqīn bǐshìliàn: àiqíng bèi hēi de cǎnbùrěndǔ\nBài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn trở lại với bài giảng giáo trình 顶石中文, Đỉnh cao tiếng Trung.",
         "Hôm nay chúng ta học bài năm chấm ba, bài cuối cùng của Đơn vị năm, chủ đề Gia đình: 相亲鄙视链：爱情被黑得惨不忍睹。 Nghĩa là: Chuỗi khinh miệt khi xem mắt, tình yêu bị bôi đen đến thảm hại.",
         "Ở các công viên lớn của Trung Quốc, cuối tuần thường có những phiên chợ xem mắt: các ông bà cụ ngồi thành hàng, trước mặt là tờ giấy ghi hộ khẩu, thu nhập, nhà cửa, học vấn của con mình. Tác giả bài báo, đăng trên 中国青年报, báo Thanh niên Trung Quốc, đã chứng kiến cảnh ấy và bày tỏ suy nghĩ của mình: liệu tình yêu thật có thể định giá được không?",
         "Cuối bài, chúng ta sẽ có thêm một chương ôn tập toàn bộ Đơn vị năm, với những đề tài thảo luận, tranh biện và viết bài rất thú vị."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài báo: chuyện cha mẹ đi xem mắt hộ con và “chuỗi khinh miệt” trong hôn nhân",
           "Nắm vững 49 từ mới, kèm âm Hán Việt và ví dụ",
           "Câu mẫu: 乍一看 · 无非 · 不由得 · 看似……实则…… · 眼见着 · 索性 · 不只是……更在于…… · 一时间",
           "Kết hợp từ: 实属 · 隔阂 · 辜负 — và 15 thành ngữ: 惨不忍睹 · 待价而沽 · 揠苗助长 · 哭笑不得……",
           "Ôn tập Đơn vị 5: đọc hiểu, thảo luận, tranh biện, viết"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu bài báo: chuyện các bậc cha mẹ ra công viên xem mắt hộ con, những tiêu chuẩn chọn bạn đời kỳ quặc, và cái gọi là chuỗi khinh miệt trong chuyện hôn nhân."),
         F(1, "Thứ hai, nắm vững bốn mươi chín từ mới, kèm âm Hán Việt, nghĩa và ví dụ."),
         F(2, "Thứ ba, tám câu mẫu: 乍一看，无非，不由得，看似……实则……，眼见着，索性，不只是……更在于……, và 一时间."),
         F(3, "Thứ tư, ba nhóm kết hợp từ 实属，隔阂，辜负, cùng mười lăm thành ngữ, nhiều nhất trong cả đơn vị."),
         F(4, "Thứ năm, ôn tập toàn bộ Đơn vị năm qua các bài đọc hiểu, thảo luận, tranh biện và viết của sách."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Suy nghĩ trước bài 课前思考", title="Suy nghĩ trước bài học 课前思考", reveal=True, size=33,
    items=["(1) 你会为了脱单而去相亲吗？",
           "Đáp án gợi ý: 会。工作太忙，很难认识新朋友，相亲是一个认识异性的好机会。",
           "(2) 你认为择偶过程中，哪些因素最重要？",
           "Đáp án gợi ý: 我认为人品最重要，其次是性格合不合得来、价值观是否相同，经济条件只是参考。",
           "(3) 你知道“裸婚”吗？你愿意为爱“裸婚”吗？",
           "Đáp án gợi ý: “裸婚”是指不买房、不买车、不办婚礼、不买戒指就结婚。只要两个人真心相爱，我愿意。"],
    say=["Trước khi vào bài, sách đưa ra ba câu hỏi để chúng ta suy nghĩ. Các bạn hãy tạm dừng video và thử trả lời bằng tiếng Trung trước nhé.",
         F(0, "Câu một: 你会为了脱单而去相亲吗？ Bạn có đi xem mắt để thoát ế không? 脱单 là thoát khỏi cảnh độc thân, một từ rất thông dụng của giới trẻ. 相亲 là xem mắt, từ mới đầu tiên của bài."),
         F(1, "Đáp án gợi ý: 会。工作太忙，很难认识新朋友，相亲是一个认识异性的好机会。 Có. Công việc quá bận, rất khó quen bạn mới, xem mắt là một cơ hội tốt để làm quen người khác giới."),
         F(2, "Câu hai: 你认为择偶过程中，哪些因素最重要？ Theo bạn, trong quá trình chọn bạn đời, những yếu tố nào quan trọng nhất? 择偶 là chọn bạn đời."),
         F(3, "Đáp án gợi ý: 我认为人品最重要，其次是性格合不合得来、价值观是否相同，经济条件只是参考。 Tôi cho rằng nhân phẩm quan trọng nhất, tiếp đến là tính cách có hợp nhau không, giá trị quan có giống nhau không; điều kiện kinh tế chỉ để tham khảo."),
         F(4, "Câu ba: 你知道裸婚吗？你愿意为爱裸婚吗？ Bạn có biết cưới trần không? Bạn có sẵn lòng vì tình yêu mà cưới trần không?"),
         F(5, "Đáp án gợi ý: 裸婚是指不买房、不买车、不办婚礼、不买戒指就结婚。只要两个人真心相爱，我愿意。 Cưới trần là kết hôn mà không mua nhà, không mua xe, không tổ chức đám cưới, không mua nhẫn. Chỉ cần hai người thật lòng yêu nhau, tôi sẵn lòng.")])

add("bullets", section="Suy nghĩ trước bài 课前思考", title="Bối cảnh: “中国式相亲价目表” và 注释", size=34,
    items=["Sách in kèm một bảng “giá” xem mắt kiểu Trung Quốc (lan truyền trên mạng): chia nam, nữ thành các bậc",
           "顶配 → 高配 → 标配 → 低配 → 简配 → 不考虑 (cấu hình cao nhất → … → không xét)",
           "Tiêu chí: 北京户口 · 房 · 车 · 月薪 · 学历 · 长相",
           "Bậc “不考虑” của nữ: 属羊 · bậc thấp: 女博士 & 女强人",
           "## 注释: 十羊九不全",
           "Vốn là tục ngữ “十羊九福全” (tuổi Mùi phần lớn có phúc), bị viết nhầm thành “十羊九弗全” (弗 = 不), lâu dần thành lời đồn sai “十羊九不全”"],
    say=["Trước khi học từ mới, các bạn hãy xem bối cảnh của bài.",
         F(0, "Trong sách có in một bức ảnh lan truyền trên mạng: 中国式相亲价目表, bảng giá xem mắt kiểu Trung Quốc. Nam và nữ được chia thành từng bậc như hàng hóa."),
         F(1, "Tên các bậc mượn từ cách gọi cấu hình xe hơi: 顶配，高配，标配，低配，简配, tức là bản cao cấp nhất, bản cao, bản tiêu chuẩn, bản thấp, bản giản lược; và cuối cùng là 不考虑, không xem xét."),
         F(2, "Tiêu chí để xếp hạng là hộ khẩu Bắc Kinh, nhà, xe, lương tháng, học vấn, và với nữ còn có ngoại hình."),
         F(3, "Điều đáng chú ý là: ở bậc không xem xét của nữ có những cô gái tuổi Mùi, còn ở bậc thấp là 女博士 và 女强人, nữ tiến sĩ và nữ cường nhân. Bài khóa sẽ bình luận đúng những điều này."),
         F(4, "Sách có một chú thích: 十羊九不全, nghĩa đen là mười con dê thì chín con không trọn vẹn, ý nói người tuổi Mùi phần lớn số khổ."),
         F(5, "Thực ra câu gốc là 十羊九福全, mười người tuổi Mùi thì chín người có phúc. Về sau bị viết nhầm thành 十羊九弗全, chữ 弗 nghĩa là không, rồi lâu dần thành lời đồn sai 十羊九不全. Một câu chúc phúc đã biến thành một lời mê tín!")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("相亲", "xiāngqīn", "tương thân", "động từ", "xem mắt (gặp mặt để tìm hiểu kết hôn)", "妈妈又给我安排了一次相亲。", "Mẹ lại sắp xếp cho tôi một buổi xem mắt.",
     "Động từ ly hợp, nghĩa là nam nữ được người khác giới thiệu để gặp mặt, tìm đối tượng kết hôn. Có thể tách ra: 相过一次亲. Trong bài: 代子相亲, xem mắt thay con."),
    ("鄙视", "bǐshì", "bỉ thị", "động từ", "khinh thường, coi khinh", "他从来不鄙视比自己穷的人。", "Anh ấy chưa bao giờ coi khinh người nghèo hơn mình.",
     "Động từ, nghĩa là xem thường, coi khinh. Mức độ mạnh hơn 轻视. Chữ 鄙 cũng có trong 卑鄙, hèn hạ."),
    ("链", "liàn", "liên", "danh từ", "chuỗi, dây xích", "这家公司的资金链断了。", "Chuỗi dòng tiền của công ty này đã đứt.",
     "Danh từ, chỉ thứ móc nối với nhau từng vòng như sợi xích. Hay gặp 项链, dây chuyền; 产业链, chuỗi ngành nghề. Tên bài 鄙视链 là chuỗi khinh miệt: nhóm trên coi thường nhóm dưới, nối tiếp thành một chuỗi."),
    ("黑", "hēi", "hắc", "động từ", "bôi đen, bôi nhọ, nói xấu", "有人在网上故意黑这位明星。", "Có người cố ý bôi nhọ ngôi sao này trên mạng.",
     "Ở bài này, 黑 là động từ, từ lóng trên mạng, nghĩa là bôi đen, dùng lời nói, chữ viết làm xấu hình ảnh người khác. Tên bài 爱情被黑得惨不忍睹 là tình yêu bị bôi đen đến thảm hại. Người hay đi bôi nhọ người khác gọi là 黑粉."),
    ("板凳", "bǎndèng", "bản đắng", "danh từ", "ghế băng, ghế đẩu bằng gỗ", "爷爷坐在小板凳上晒太阳。", "Ông nội ngồi trên chiếc ghế đẩu nhỏ phơi nắng.",
     "Danh từ, chỉ loại ghế gỗ không có lưng tựa, thường hình dài. Trong bài: 坐在小板凳上, ngồi trên ghế đẩu nhỏ, hình ảnh rất quen thuộc ở công viên Trung Quốc."),
    ("纸片", "zhǐpiàn", "chỉ phiến", "danh từ", "mẩu giấy, mảnh giấy", "地上到处都是碎纸片。", "Trên đất khắp nơi là những mẩu giấy vụn.",
     "Danh từ, nghĩa là mẩu giấy nhỏ. Trong bài, mỗi người đặt trước mặt 一张纸片, chính là tờ lý lịch xem mắt của con mình."),
    ("乍", "zhà", "sạ", "phó từ", "vừa mới, thoạt đầu", "乍一看，这两个人长得很像。", "Thoạt nhìn, hai người này trông rất giống nhau.",
     "Phó từ, nghĩa là vừa mới, ban đầu. Hay gặp 乍一看, thoạt nhìn; 乍暖还寒, trời vừa ấm lại lạnh. 乍一看 là câu mẫu đầu tiên của bài."),
    ("展销会", "zhǎnxiāohuì", "triển tiêu hội", "danh từ", "hội chợ triển lãm kết hợp bán hàng", "这个周末有一场汽车展销会。", "Cuối tuần này có một hội chợ triển lãm bán ô tô.",
     "Danh từ, nghĩa là hoạt động bán hàng dưới hình thức triển lãm: 展 là triển lãm, 销 là tiêu thụ, 会 là hội. Tác giả ví phiên chợ xem mắt như 一场大型的展销会, một hội chợ hàng hóa lớn."),
    ("征婚", "zhēnghūn", "trưng hôn", "động từ", "(công khai) tìm bạn đời", "他在网上发了一则征婚启事。", "Anh ấy đăng một mẩu tin tìm bạn đời trên mạng.",
     "Động từ ly hợp, nghĩa là công khai tìm đối tượng kết hôn. 征 là trưng cầu, tìm kiếm. Hay gặp 征婚启事, tin tìm bạn đời; 征婚简历, lý lịch tìm bạn đời."),
    ("房产", "fángchǎn", "phòng sản", "danh từ", "nhà đất, nhà cửa (tài sản)", "他在北京有两处房产。", "Anh ấy có hai bất động sản nhà ở Bắc Kinh.",
     "Danh từ, chỉ nhà cửa thuộc sở hữu của cá nhân hay tổ chức. Một trong những điều kiện quan trọng nhất khi xem mắt ở Trung Quốc, cùng với 户籍, 收入, 学历."),
    ("醒目", "xǐngmù", "tỉnh mục", "tính từ", "nổi bật, dễ thấy", "广告上的标题非常醒目。", "Tiêu đề trên tờ quảng cáo rất nổi bật.",
     "Tính từ, nói về chữ viết, hình vẽ rõ ràng, dễ nhìn thấy. 醒 là tỉnh, 目 là mắt: làm mắt tỉnh ra. Trong bài: 醒目地用了大红的粗字体, dùng chữ in đậm màu đỏ thật nổi bật."),
    ("抢眼", "qiǎngyǎn", "thương nhãn", "tính từ", "bắt mắt, gây chú ý", "她今天穿了一条很抢眼的红裙子。", "Hôm nay cô ấy mặc một chiếc váy đỏ rất bắt mắt.",
     "Tính từ, nghĩa là nổi bật, thu hút ánh nhìn, như thể giành lấy con mắt người khác. Gần nghĩa với 醒目 và 显眼."),
    ("灵魂", "línghún", "linh hồn", "danh từ", "linh hồn; tâm hồn, tư tưởng", "教师是人类灵魂的工程师。", "Giáo viên là kỹ sư tâm hồn của nhân loại.",
     "Danh từ, chỉ tư tưởng, tâm hồn của con người. Trong bài: 有思想有灵魂的男孩女孩, những chàng trai cô gái có tư tưởng, có tâm hồn, đối lập với những tờ giấy A4 vô hồn."),
    ("硬性", "yìngxìng", "ngạnh tính", "tính từ", "cứng nhắc, bắt buộc, không châm chước", "这是公司的硬性规定。", "Đây là quy định bắt buộc của công ty.",
     "Tính từ thuộc tính, nghĩa là không thể thay đổi, không thể châm chước. Hay gặp 硬性规定，硬性条件，硬性指标. Trong bài: 被抽出一条条硬性条件, bị rút ra thành từng điều kiện cứng."),
    ("供", "gōng", "cung", "động từ", "cung cấp (cho người khác dùng)", "这些资料仅供参考。", "Những tài liệu này chỉ để tham khảo.",
     "Động từ, ở đây đọc thanh một, nghĩa là cung cấp điều kiện cho người khác sử dụng: 供读者参考, để độc giả tham khảo. Trong bài: 供众人评头论足, để mọi người bình phẩm. Khi đọc thanh bốn, gòng, nó có nghĩa khác: cúng, như 供品, đồ cúng.", "工"),
    ("贩卖", "fànmài", "phán mại", "động từ", "buôn bán (kiếm lời); buôn người", "贩卖人口是严重的犯罪行为。", "Buôn bán người là hành vi phạm tội nghiêm trọng.",
     "Động từ, nghĩa là mua vào rồi bán ra để kiếm chênh lệch. Thường mang nghĩa xấu: 贩卖毒品, buôn ma túy; 贩卖人口, buôn người. Cư dân mạng gọi chợ xem mắt là 人口贩卖市场, chợ buôn người."),
    ("透过", "tòuguò", "thấu quá", "động từ", "thông qua, xuyên qua", "阳光透过窗户照进房间。", "Ánh nắng xuyên qua cửa sổ chiếu vào phòng.",
     "Động từ, nghĩa là xuyên qua, thông qua. Trong bài: 透过一张张征婚简历, nhìn qua từng tờ lý lịch tìm bạn đời. Nghĩa bóng hay gặp: 透过现象看本质, nhìn qua hiện tượng để thấy bản chất."),
    ("滑稽", "huájī", "hoạt kê", "tính từ", "buồn cười, khôi hài", "他的表情很滑稽，大家都笑了。", "Vẻ mặt anh ấy rất buồn cười, mọi người đều bật cười.",
     "Tính từ, nói về lời nói, cử chỉ, dáng vẻ gây cười. Âm Hán Việt hoạt kê, như trong truyện hoạt kê. Trong bài: 滑稽可笑, khôi hài đáng cười."),
    ("不由得", "bùyóude", "bất do đắc", "phó từ", "bất giác, không kìm được", "想起过去的苦难，他不由得掉下眼泪来。", "Nhớ lại những khổ đau ngày trước, anh ấy bất giác rơi nước mắt.",
     "Phó từ, nghĩa là không tự chủ được, bất giác, giống 不禁. Đây là câu mẫu thứ ba của bài."),
    ("浏览", "liúlǎn", "lưu lãm", "động từ", "xem lướt, đọc lướt", "我每天早上都会浏览一下新闻。", "Sáng nào tôi cũng lướt qua tin tức một chút.",
     "Động từ, nghĩa là xem qua một lượt. Trình duyệt web gọi là 浏览器. Trong bài: 浏览相亲材料, xem lướt tài liệu xem mắt."),
    ("闲聊", "xiánliáo", "nhàn liêu", "động từ", "tán gẫu, nói chuyện phiếm", "几个老人坐在树下闲聊。", "Mấy cụ già ngồi dưới gốc cây tán gẫu.",
     "Động từ, nghĩa là nói chuyện phiếm lúc rảnh rỗi, giống 闲谈, 聊天. Trong bài: 看似闲聊、实则互相摸底, trông như tán gẫu, thực ra là dò hỏi nhau."),
    ("摸底", "mōdǐ", "mô để", "động từ", "thăm dò, dò hỏi ngọn ngành", "考试前，老师先给大家摸摸底。", "Trước kỳ thi, thầy giáo kiểm tra thử trình độ mọi người trước.",
     "Động từ, nghĩa là tìm hiểu tình hình thực tế, dò xét nội tình. 摸 là sờ, 底 là đáy: sờ xuống tận đáy. Hay gặp 摸底考试, bài kiểm tra đánh giá trình độ."),
    ("殆尽", "dàijìn", "đãi tận", "động từ", "gần như hết sạch", "这里的森林资源已经被破坏殆尽。", "Tài nguyên rừng ở đây đã bị phá hoại gần hết.",
     "Động từ, nghĩa là gần như hết hoàn toàn, văn viết. Hay gặp 消失殆尽，破坏殆尽，瓜分殆尽. Trong bài: 时间和精力在城市的快节奏中消失殆尽."),
    ("适婚", "shìhūn", "thích hôn", "tính từ", "đến tuổi lập gia đình, thích hợp kết hôn", "她已经到了适婚年龄。", "Cô ấy đã đến tuổi lập gia đình.",
     "Tính từ, nghĩa là về tuổi tác, thể chất và tâm lý đều thích hợp để kết hôn. Hay gặp 适婚年龄, 适婚青年."),
    ("索性", "suǒxìng", "sách tính", "phó từ", "dứt khoát, đã thế thì… luôn", "雨越下越大，我们索性不走了。", "Mưa càng lúc càng to, chúng tôi dứt khoát không đi nữa.",
     "Phó từ, biểu thị thẳng thắn, dứt khoát, giống 干脆. Đây là câu mẫu thứ sáu của bài."),
    ("出马", "chūmǎ", "xuất mã", "động từ", "ra mặt, đích thân ra tay", "这件事只有经理亲自出马才能解决。", "Việc này chỉ khi giám đốc đích thân ra mặt mới giải quyết được.",
     "Động từ, nghĩa gốc là ra trận, nay chỉ việc đứng ra làm việc. Hay gặp 亲自出马, đích thân ra tay. Trong bài: 索性亲自出马, dứt khoát tự mình ra tay tìm vợ tìm chồng cho con."),
    ("质疑", "zhìyí", "chất nghi", "động từ", "đặt nghi vấn, chất vấn", "很多专家质疑这个调查的结果。", "Nhiều chuyên gia đặt nghi vấn về kết quả cuộc điều tra này.",
     "Động từ, nghĩa là nêu ra nghi vấn. Văn viết, mạnh hơn 怀疑 vì là công khai đặt câu hỏi. Trong bài: 人们质疑最多的, điều mọi người nghi ngờ nhiều nhất."),
    ("择偶", "zé'ǒu", "trạch ngẫu", "động từ", "chọn bạn đời", "每个人的择偶标准都不一样。", "Tiêu chuẩn chọn bạn đời của mỗi người đều khác nhau.",
     "Động từ, nghĩa là chọn người phối ngẫu. 择 là chọn, 偶 là đôi, bạn đời, như trong 配偶. Cụm hay gặp: 择偶标准, 择偶观."),
    ("引爆", "yǐnbào", "dẫn bạo", "động từ", "kích nổ; (bóng) làm bùng nổ", "这条新闻一下子引爆了网络。", "Tin này lập tức làm bùng nổ cõi mạng.",
     "Động từ, nghĩa gốc là dùng ngòi nổ làm thuốc nổ phát nổ; nghĩa bóng là làm bùng lên một cuộc tranh luận. Trong bài: 瞬间引爆了舆论场, lập tức làm bùng nổ dư luận."),
    ("隔阂", "géhé", "cách ngại", "danh từ", "sự ngăn cách, khoảng cách (tình cảm, tư tưởng)", "两代人之间难免有一些隔阂。", "Giữa hai thế hệ khó tránh khỏi có chút khoảng cách.",
     "Danh từ, nghĩa là trở ngại trong giao lưu tình cảm, khoảng cách về tư tưởng. Đây là một nhóm kết hợp từ: 产生隔阂，消除隔阂，打破隔阂."),
    ("一边倒", "yībiāndǎo", "nhất biên đảo", "tính từ", "nghiêng hẳn về một phía", "网上的评论几乎是一边倒的。", "Bình luận trên mạng gần như nghiêng hẳn về một phía.",
     "Tính từ, chỉ lập trường, thái độ, quan điểm hoàn toàn nghiêng về một bên. Cũng dùng cho trận đấu chênh lệch: 一边倒的比赛. Trong bài: 几乎一边倒地指责北京人."),
    ("优越感", "yōuyuègǎn", "ưu việt cảm", "danh từ", "cảm giác hơn người", "他说话总是带着一种优越感。", "Anh ta nói chuyện lúc nào cũng mang vẻ hơn người.",
     "Danh từ, chỉ tâm lý tự cho mình hơn người khác. Trong bài: 总有一种莫名其妙的优越感, lúc nào cũng có một thứ cảm giác hơn người khó hiểu."),
    ("辩解", "biànjiě", "biện giải", "động từ", "biện bạch, thanh minh", "做错了就要承认，不要再辩解了。", "Làm sai thì phải thừa nhận, đừng biện bạch nữa.",
     "Động từ, nghĩa là giải thích, biện bạch trước lời phê bình, chỉ trích của người khác. Trong bài: 北京人则委屈地辩解, còn người Bắc Kinh thì ấm ức thanh minh."),
    ("争吵", "zhēngchǎo", "tranh sảo", "động từ", "cãi nhau, tranh cãi", "他们俩为了一点小事争吵起来。", "Hai người họ cãi nhau vì một chuyện nhỏ.",
     "Động từ, nghĩa là vì bất đồng ý kiến mà lớn tiếng tranh cãi, không ai nhường ai. Trong bài: 争吵来争吵去, cãi qua cãi lại."),
    ("不服", "bùfú", "bất phục", "động từ", "không phục, không chịu", "他输了比赛，心里很不服。", "Anh ấy thua trận, trong lòng rất không phục.",
     "Động từ, nghĩa là không chịu thua, không tin phục. Trong bài: 谁也不服谁, chẳng ai phục ai."),
    ("苟同", "gǒutóng", "cẩu đồng", "động từ", "tùy tiện đồng ý (thường: 不敢苟同)", "对于你的看法，我不敢苟同。", "Đối với quan điểm của anh, tôi không dám đồng tình.",
     "Động từ, nghĩa là dễ dãi đồng ý. Hầu như chỉ dùng trong cụm 不敢苟同, một cách nói lịch sự, trang trọng để bày tỏ sự không đồng tình."),
    ("海归", "hǎiguī", "hải quy", "động từ", "du học, làm việc ở nước ngoài rồi về nước", "他是一名海归博士。", "Anh ấy là một tiến sĩ du học trở về.",
     "Động từ, cũng dùng như danh từ, chỉ người du học hay làm việc ở nước ngoài một thời gian rồi về nước lập nghiệp. 海 là biển, tức hải ngoại; 归 là trở về. Đồng âm với 海龟, con rùa biển, nên người ta hay đùa gọi họ là rùa biển."),
    ("大专", "dàzhuān", "đại chuyên", "danh từ", "cao đẳng", "她大专毕业后就开始工作了。", "Cô ấy tốt nghiệp cao đẳng xong là đi làm luôn.",
     "Danh từ, là cách gọi tắt của trường chuyên khoa trình độ đại học, tương đương cao đẳng ở Việt Nam. Trong bài: nữ tiến sĩ bị xếp ngang hàng với nam giới học vấn 大专高中."),
    ("生肖", "shēngxiào", "sinh tiếu", "danh từ", "con giáp (cầm tinh)", "我的生肖是马。", "Tôi cầm tinh con ngựa.",
     "Danh từ, chỉ mười hai con vật đại diện cho mười hai địa chi, dùng để chỉ năm sinh: 鼠，牛，虎，兔，龙，蛇，马，羊，猴，鸡，狗，猪. Còn gọi là 属相. Hỏi tuổi con gì: 你属什么？ Chú ý: tuổi Mão của Việt Nam là con mèo, còn Trung Quốc là con thỏ."),
    ("世故", "shìgu", "thế cố", "danh từ", "kinh nghiệm đối nhân xử thế", "他虽然年轻，却很懂人情世故。", "Anh ấy tuy trẻ nhưng rất hiểu nhân tình thế thái.",
     "Danh từ, nghĩa là kinh nghiệm xử thế, chữ thứ hai đọc nhẹ. Hay gặp 人情世故. Làm tính từ thì có nghĩa là khôn đời, thạo đời, hơi mang ý chê. Trong bài: 用他们的经验世故衡量下一代的人生."),
    ("妖魔化", "yāomóhuà", "yêu ma hóa", "động từ", "ma quỷ hóa, bôi đen quá mức", "我们不应该把网络游戏妖魔化。", "Chúng ta không nên ma quỷ hóa trò chơi trực tuyến.",
     "Động từ, nghĩa là nhìn nhận sự việc tồi tệ, đáng sợ hơn bản chất thật của nó. 化 là hậu tố biến thành, như 现代化. Trong bài: 他们的择偶观被妖魔化, quan niệm chọn bạn đời của người trẻ bị bôi đen."),
    ("背锅者", "bēiguōzhě", "bối oa giả", "danh từ", "người gánh tội thay, người bị đổ lỗi oan", "出了问题，他总是成为背锅者。", "Hễ có chuyện, anh ấy luôn là người bị đổ lỗi.",
     "Danh từ, từ lóng trên mạng. 背黑锅 là cõng nồi đen, ví với việc bị oan, chịu tội thay người khác. Chữ 背 ở đây theo từ điển đọc thanh một, nghĩa là cõng, vác; sách ghi thanh bốn, khẩu ngữ cũng có người đọc như vậy. Tiếng Việt vui có thể nói: người đổ vỏ."),
    ("功利主义", "gōnglì zhǔyì", "công lợi chủ nghĩa", "danh từ", "chủ nghĩa vụ lợi, thực dụng", "这种做法带有明显的功利主义色彩。", "Cách làm này mang màu sắc thực dụng rõ rệt.",
     "Danh từ, chỉ quan điểm lấy hiệu quả thực tế và lợi ích làm chuẩn mực hành động. Trong bài: 充满着功利主义的色彩, đầy màu sắc thực dụng: hôn nhân bị tính toán như mua bán."),
    ("价码", "jiàmǎ", "giá mã", "danh từ", "giá, giá cả (khẩu ngữ)", "他开出的价码太高了。", "Cái giá anh ta đưa ra cao quá.",
     "Danh từ khẩu ngữ, nghĩa là giá cả. Trong bài: 寻找高于自身价码的另一半, tìm một nửa có giá cao hơn mình, như thể con người là hàng hóa."),
    ("攀高枝", "pān gāozhī", "phan cao chi", "động từ", "trèo cao, kết thân với người địa vị cao", "她不想攀高枝，只想找个真心爱她的人。", "Cô ấy không muốn trèo cao, chỉ muốn tìm một người thật lòng yêu mình.",
     "Cụm động từ, 攀 là trèo, 高枝 là cành cao: kết bạn hay kết thông gia với người có địa vị xã hội cao hơn mình. Tiếng Việt cũng nói: trèo cao. Trong bài: 希望攀上高枝."),
    ("精明", "jīngmíng", "tinh minh", "tính từ", "khôn ngoan, tinh tường, sắc sảo", "他是个精明的商人。", "Ông ấy là một thương nhân khôn ngoan.",
     "Tính từ, nghĩa là tinh tế, sáng suốt, nhanh nhạy. Sách ghi là danh từ, nhưng thực tế thường dùng làm tính từ. Trong bài: 一场精明人的游戏, một trò chơi của những người khôn ngoan, tính toán."),
    ("估价", "gūjià", "cổ giá", "động từ", "định giá, ước tính giá", "请专家给这幅画估个价。", "Nhờ chuyên gia định giá bức tranh này.",
     "Động từ ly hợp, nghĩa là ước tính giá trị hàng hóa. Câu hỏi then chốt của bài: 真爱难道可以估价吗？ Lẽ nào tình yêu đích thực có thể định giá được?"),
    ("辜负", "gūfù", "cô phụ", "động từ", "phụ lòng", "我一定不会辜负你的期望。", "Tôi nhất định sẽ không phụ kỳ vọng của bạn.",
     "Động từ, nghĩa là phụ lòng tốt, kỳ vọng hay sự giúp đỡ của người khác. Âm Hán Việt cô phụ. Đây là một nhóm kết hợp từ: 辜负厚望，辜负好意."),
    ("鲜活", "xiānhuó", "tiên hoạt", "tính từ", "tươi sống; sinh động, đầy sức sống", "这部小说塑造了许多鲜活的人物。", "Cuốn tiểu thuyết này đã khắc họa nhiều nhân vật sinh động.",
     "Tính từ, nghĩa gốc là tươi sống, như 鲜活的鱼; nghĩa bóng là sống động, tươi mới. Câu kết của bài: 一代人鲜活的人生, cuộc đời tươi trẻ, sống động của cả một thế hệ."),
]

add("bullets", chapter="Từ mới (49 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 5.3 có 49 từ mới, chia thành 17 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Nhiều từ lóng trên mạng: 黑 · 鄙视链 · 海归 · 背锅者 · 妖魔化",
           "Chú ý âm đọc: 供 (gōng) · 乍 (zhà) · 世故 (shìgu) · 背锅 (bēi)"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có bốn mươi chín từ, thầy chia thành mười bảy nhóm nhỏ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Bài báo này viết cho giới trẻ, nên có khá nhiều từ lóng trên mạng: 黑 nghĩa là bôi nhọ, 鄙视链, 海归, 背锅者, 妖魔化. Những từ này không có trong các giáo trình cũ, nhưng người Trung Quốc dùng hằng ngày."),
         F(4, "Một số chữ cần chú ý âm đọc: 供 ở đây đọc thanh một; 乍 đọc là zhà; trong 世故, chữ thứ hai đọc nhẹ; và 背 trong 背锅 theo từ điển đọc thanh một. Chúng ta bắt đầu.")])

sizes = [3] * 15 + [2, 2]
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
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung nếu khác])
P = [
    ("媒体热议的相亲鄙视链，让我想起曾在北京的公园里见过这种场景：一字排开的大爷大妈，坐在小板凳上，每人面前的空地上摆一张纸片，整整齐齐，井然有序，乍一看简直无异于一场大型的展销会。",
     "Chuỗi khinh miệt khi xem mắt mà truyền thông đang bàn tán sôi nổi khiến tôi nhớ lại cảnh tượng từng thấy trong một công viên ở Bắc Kinh: các ông các bà xếp thành một hàng dài, ngồi trên những chiếc ghế đẩu nhỏ, trước mặt mỗi người trên khoảng đất trống đặt một mẩu giấy, ngay ngắn chỉnh tề, trật tự đâu ra đấy; thoạt nhìn chẳng khác nào một hội chợ triển lãm bán hàng quy mô lớn.",
     ["热议 là bàn luận sôi nổi. 让我想起 là khiến tôi nhớ lại. 一字排开 là xếp thành một hàng như nét chữ nhất. 大爷大妈 là các ông các bà, cách gọi thân mật người lớn tuổi ở miền Bắc Trung Quốc.",
      "井然有序 là ngăn nắp trật tự, thành ngữ của bài. 乍一看 là thoạt nhìn, câu mẫu thứ nhất. 无异于 là chẳng khác gì, từ mới của bài trước. Phép so sánh với 展销会 đã ngầm phê phán: con người bị bày ra như hàng hóa."]),
    ("混在人群里上前瞧了一眼，大爷大妈们竟然是替子女相亲来的，那地上一字排开的纸片便是征婚简历，无非列了几行个人介绍，而户籍、收入、房产、学历等条件则醒目地用了大红的粗字体，十分抢眼。",
     "Lẫn vào đám đông tiến lên ngó thử, hóa ra các ông các bà đến đây để xem mắt thay cho con cái. Những mẩu giấy xếp hàng dưới đất chính là lý lịch tìm bạn đời, chẳng qua chỉ liệt kê vài dòng giới thiệu bản thân, còn các điều kiện như hộ khẩu, thu nhập, nhà cửa, học vấn thì được in bằng chữ đậm màu đỏ thật nổi bật, vô cùng bắt mắt.",
     ["混在人群里 là trà trộn vào đám đông. 瞧了一眼 là ngó một cái, 瞧 là khẩu ngữ của 看. 竟然 là vậy mà, hóa ra, biểu thị bất ngờ. 替子女相亲 là xem mắt thay con.",
      "便是 là chính là. 无非 là chẳng qua chỉ, câu mẫu thứ hai. Phần giới thiệu bản thân chỉ vài dòng, còn 户籍、收入、房产、学历 thì in to, đỏ, đậm: điều kiện vật chất quan trọng hơn con người."]),
    ("此刻，一个个有血有肉、有思想有灵魂的男孩女孩，一律被压扁成一张张A4纸，被抽出一条条硬性条件，躺在被太阳烤热的水泥地上，供众人评头论足。",
     "Lúc này, từng chàng trai cô gái bằng xương bằng thịt, có tư tưởng có tâm hồn, đều bị ép dẹt thành từng tờ giấy A4, bị rút ra thành từng điều kiện cứng nhắc, nằm trên nền xi măng bị mặt trời nung nóng, cho mọi người bình phẩm soi mói.",
     ["Câu văn giàu hình ảnh: con người sống động 有血有肉、有思想有灵魂 bị 压扁成一张张A4纸, ép dẹt thành tờ giấy. 一律 là đều, nhất loạt. 一个个，一张张，一条条: lặp lượng từ nhấn mạnh số lượng nhiều.",
      "抽出 là rút ra. 烤热 là nướng nóng. 供众人评头论足: chữ 供 đọc thanh một, nghĩa là để cho; 评头论足 là bình đầu luận chân, soi mói từ đầu đến chân. Hai câu bị động 被 liên tiếp cho thấy người trẻ hoàn toàn bị động."],
     "此刻，一个个有血有肉、有思想有灵魂的男孩女孩，一律被压扁成一张张诶四纸，被抽出一条条硬性条件，躺在被太阳烤热的水泥地上，供众人评头论足。"),
    ("这种待价而沽的商品式相亲被网友们开玩笑地称为“人口贩卖市场”。透过一张张征婚简历，我只能看到一张张相似的、模糊的脸，让人不免觉得有几分滑稽可笑，",
     "Kiểu xem mắt như hàng hóa chờ giá cao mới bán này bị cư dân mạng đùa gọi là “chợ buôn người”. Nhìn qua từng tờ lý lịch tìm bạn đời, tôi chỉ thấy những gương mặt na ná nhau, mờ nhạt, khiến người ta không khỏi thấy có phần khôi hài, nực cười.",
     ["待价而沽 là chờ giá cao mới bán, thành ngữ của bài. 商品式相亲 là xem mắt kiểu hàng hóa. 称为 là gọi là. 人口贩卖市场 là chợ buôn người, một cách nói đùa nhưng rất chua chát.",
      "透过 là thông qua. 相似的、模糊的脸 là những gương mặt giống nhau, mờ nhạt: khi chỉ nhìn điều kiện, ai cũng như ai. 不免 là khó tránh, các bạn đã học ở bài trước. 几分 là đôi phần."]),
    ("我不由得冲旁边的大爷一乐，这一乐可不要紧，大爷来了精神：“姑娘，怎么样，我儿子条件还可以吧？”",
     "Tôi bất giác mỉm cười với ông cụ bên cạnh. Cười một cái thì không sao, ai ngờ ông cụ phấn chấn hẳn lên: “Cô gái, thế nào, điều kiện của con trai tôi cũng được đấy chứ?”",
     ["不由得 là bất giác, câu mẫu thứ ba. 冲 ở đây đọc thanh bốn, là giới từ khẩu ngữ, nghĩa là hướng về, nhìn về phía. 一乐 là cười một cái.",
      "这一乐可不要紧 là cười một cái thì chẳng sao, nhưng… một cách nói khẩu ngữ hài hước, báo trước một hậu quả bất ngờ. 来了精神 là phấn chấn hẳn lên. Thì ra tác giả là một cô gái, và ông cụ tưởng cô cũng đến xem mắt!"]),
    ("大爷大妈们通过浏览相亲材料，以及看似闲聊、实则互相摸底的方式，就想为子女找到另一半。心情如此迫切，简直有些揠苗助长、急功近利的意味了。",
     "Các ông các bà chỉ thông qua việc xem lướt tài liệu xem mắt, cùng cách trò chuyện tưởng như tán gẫu, thực ra là dò hỏi lẫn nhau, mà muốn tìm được một nửa kia cho con. Tâm trạng nóng vội như vậy, quả thật có chút ý vị của kiểu kéo mạ cho mau lớn, nóng vội cầu lợi trước mắt.",
     ["以及 là cùng với. 看似闲聊、实则互相摸底 là trông như tán gẫu, thực ra là dò hỏi nhau, câu mẫu 看似……实则…… thứ tư. 另一半 là một nửa kia, tức bạn đời.",
      "迫切 là cấp bách, nóng lòng. 揠苗助长 là nhổ mạ lên cho mau lớn, chữ 长 đọc là zhǎng. 急功近利 là nóng vội lập công, ham lợi trước mắt. 意味 là ý vị, hàm ý."]),
    ("身为父母，眼见着子女们忙于事业，时间和精力在城市的快节奏中消失殆尽，又确实难有与异性相处的机会，担心他们错过适婚年龄，心急火燎，索性亲自出马也实属无奈。",
     "Là cha mẹ, tận mắt thấy con cái bận rộn với sự nghiệp, thời gian và sức lực tiêu tan gần hết trong nhịp sống nhanh của thành phố, lại thật sự khó có cơ hội tiếp xúc với người khác giới; lo con lỡ mất tuổi kết hôn, sốt ruột như lửa đốt, thế là dứt khoát tự mình ra tay, cũng thật là chuyện bất đắc dĩ.",
     ["Ở đoạn này tác giả tỏ ra thông cảm với cha mẹ. 身为父母 là thân là cha mẹ, chữ 为 đọc thanh hai. 眼见着 là tận mắt thấy, câu mẫu thứ năm. 忙于事业 là bận rộn với sự nghiệp. 消失殆尽 là tiêu tan gần hết.",
      "与异性相处 là tiếp xúc, chung sống với người khác giới. 心急火燎 là lòng nóng như lửa đốt. 索性 là dứt khoát, câu mẫu thứ sáu. 亲自出马 là đích thân ra tay. 实属无奈 là thật sự bất đắc dĩ, một nhóm kết hợp từ."]),
    ("不过人们质疑最多的，不只是父母这种为子女相亲的方式，更在于他们眼中的择偶标准。新闻里一句“不考虑没北京户口的姑娘；有户口，残疾也行”瞬间引爆了舆论场。",
     "Thế nhưng điều mọi người nghi ngờ nhiều nhất không chỉ là cách cha mẹ đi xem mắt cho con, mà còn ở tiêu chuẩn chọn bạn đời trong mắt họ. Một câu trên bản tin: “Không xét những cô gái không có hộ khẩu Bắc Kinh; có hộ khẩu thì tàn tật cũng được” lập tức làm bùng nổ dư luận.",
     ["不只是……更在于…… là không chỉ là… mà còn ở chỗ…, câu mẫu thứ bảy. Đoạn này chuyển từ cách thức sang tiêu chuẩn chọn bạn đời.",
      "户口 là hộ khẩu, ở Trung Quốc hộ khẩu Bắc Kinh gắn với nhiều phúc lợi như giáo dục, y tế. 残疾也行 là tàn tật cũng được: hộ khẩu quan trọng hơn cả sức khỏe! 瞬间 là trong chớp mắt. 引爆舆论场 là làm bùng nổ dư luận."]),
    ("北京人与外地人的隔阂、地域歧视等问题又被推上风口浪尖。微博的评论里几乎一边倒地指责北京人“总有一种莫名其妙的优越感”，而北京人则委屈地辩解“确实和外地人生活习惯不同”，一时间双方争吵来争吵去，谁也不服谁。",
     "Những vấn đề như khoảng cách giữa người Bắc Kinh và người nơi khác, sự kỳ thị vùng miền… lại bị đẩy lên đầu sóng ngọn gió. Bình luận trên Weibo gần như nghiêng hẳn về một phía, chỉ trích người Bắc Kinh “lúc nào cũng có một thứ cảm giác hơn người khó hiểu”, còn người Bắc Kinh thì ấm ức thanh minh “thói quen sinh hoạt quả thật khác với người nơi khác”. Trong một thời gian, hai bên cãi qua cãi lại, chẳng ai phục ai.",
     ["外地人 là người nơi khác đến. 隔阂 là khoảng cách, sự ngăn cách. 地域歧视 là kỳ thị vùng miền. 推上风口浪尖 là đẩy lên đầu sóng ngọn gió, tức là trở thành tâm điểm tranh cãi.",
      "指责 là chỉ trích. 莫名其妙 là khó hiểu, chẳng hiểu vì sao. 委屈地辩解 là ấm ức thanh minh. 一时间 là trong một thời gian ngắn, câu mẫu thứ tám. 争吵来争吵去 là cãi qua cãi lại, mẫu động từ cộng 来 cộng động từ cộng 去 chỉ sự lặp đi lặp lại."]),
    ("如果说“要求北京户口”还能被理解，那么“坚决不要女博士”这种价值观我就真的不敢苟同了。在网上的中国式相亲鄙视链上，女博士尤其是海归女博士在鄙视链的最下端，与她们同等级的男性是“大专高中”学历。",
     "Nếu nói “yêu cầu hộ khẩu Bắc Kinh” còn có thể hiểu được, thì cái giá trị quan “nhất quyết không lấy nữ tiến sĩ” tôi thật sự không dám đồng tình. Trên chuỗi khinh miệt xem mắt kiểu Trung Quốc trên mạng, nữ tiến sĩ, nhất là nữ tiến sĩ du học về, nằm ở tận cùng của chuỗi, ngang hàng với nam giới có học vấn “cao đẳng, cấp ba”.",
     ["如果说……那么…… là nếu nói… thì…, so sánh hai mức độ: cái trước còn hiểu được, cái sau thì không thể chấp nhận. 坚决 là kiên quyết. 不敢苟同 là không dám đồng tình, cách nói phản đối lịch sự.",
      "尤其是 là nhất là. 海归女博士 là nữ tiến sĩ du học về. 最下端 là tận cùng phía dưới. 同等级 là cùng đẳng cấp. Nghịch lý: người phụ nữ học càng cao lại càng bị coi thường trên chợ hôn nhân."]),
    ("如果“女博士”们的不满还能说出几分原因，那生肖属羊姑娘们的遭遇则就毫无理性可言了。仅仅是因为生肖为羊，无论有什么优点都一棒子打死了。“十羊九不全”，大爷大妈们的迷信心理令网友们哭笑不得：“属羊的吃你家草了？！”",
     "Nếu sự bất mãn với “nữ tiến sĩ” còn nói ra được đôi phần lý do, thì cảnh ngộ của các cô gái tuổi Mùi lại hoàn toàn chẳng có chút lý trí nào. Chỉ vì cầm tinh con dê, dù có ưu điểm gì cũng bị một gậy đánh chết. “Mười dê chín không trọn”, tâm lý mê tín của các ông các bà khiến cư dân mạng dở khóc dở cười: “Người tuổi Mùi ăn cỏ nhà các người à?!”",
     ["Lại một cặp so sánh tăng tiến: 如果……还能……，那……则就…… . 毫无理性可言 là chẳng có chút lý trí nào để nói đến. 生肖为羊 là cầm tinh con dê, chữ 为 đọc thanh hai.",
      "一棒子打死 là một gậy đánh chết, tức là phủ định hoàn toàn. 十羊九不全 chúng ta đã biết là một lời đồn sai. 哭笑不得 là dở khóc dở cười. Câu đáp trả của cư dân mạng 属羊的吃你家草了 rất hóm hỉnh: dê thì ăn cỏ, nhưng có ăn cỏ nhà ông đâu!"]),
    ("奇葩的择偶标准充分暴露出父母代子相亲的弊端。传统价值观念、迷信思想在老一辈的内心根深蒂固，他们仍在用他们的经验世故衡量下一代的人生。在相亲鄙视链的媒体想象中，年轻一代是缺席的，他们的择偶观被妖魔化，成为无奈的背锅者。",
     "Những tiêu chuẩn chọn bạn đời kỳ quặc đã phơi bày đầy đủ mặt trái của việc cha mẹ đi xem mắt thay con. Quan niệm giá trị truyền thống, tư tưởng mê tín đã ăn sâu bén rễ trong lòng thế hệ trước; họ vẫn dùng kinh nghiệm đối nhân xử thế của mình để đo đếm cuộc đời của thế hệ sau. Trong hình dung của truyền thông về chuỗi khinh miệt xem mắt, thế hệ trẻ lại vắng mặt, quan niệm chọn bạn đời của họ bị ma quỷ hóa, họ trở thành những người bất đắc dĩ phải gánh tội thay.",
     ["奇葩 nghĩa gốc là bông hoa lạ, nay là từ lóng chỉ người hay việc kỳ quặc. 暴露 là phơi bày. 弊端 là tệ hại, mặt trái. 根深蒂固 là ăn sâu bén rễ, đã học ở bài năm chấm một.",
      "衡量 là đo lường, đánh giá. 缺席 là vắng mặt. Đây là luận điểm quan trọng: người ta tưởng giới trẻ thực dụng, nhưng thực ra những tiêu chuẩn ấy là của cha mẹ; người trẻ bị 妖魔化, thành 背锅者, người gánh tội thay."]),
    ("公园里上演的一场场代子相亲的大戏，充满着功利主义的色彩。他们不约而同地列出子女具备的各种优势，“明码标价”，坚持不懈地寻找高于自身价码，或者至少价码相等的另一半。",
     "Những màn kịch lớn xem mắt thay con diễn ra trong công viên đầy màu sắc thực dụng. Họ không hẹn mà cùng liệt kê đủ mọi ưu thế của con cái, “niêm yết giá rõ ràng”, kiên trì không mệt mỏi tìm kiếm một nửa kia có giá cao hơn mình, hoặc ít nhất là ngang giá.",
     ["上演 là trình diễn. 一场场大戏 là từng màn kịch lớn, một cách nói châm biếm. 充满着功利主义的色彩 là đầy màu sắc thực dụng.",
      "不约而同 là không hẹn mà cùng. 明码标价 là niêm yết giá công khai, vốn là thuật ngữ thương mại; đặt trong ngoặc kép để mỉa mai. 坚持不懈 là kiên trì bền bỉ, vốn là lời khen, ở đây lại mang giọng châm biếm. 价码 là giá."]),
    ("一方面急功近利，希望攀上高枝；一方面忧心忡忡，担心被别人分走一杯羹。这看似是一场精明人的游戏，但他们似乎恰恰忘了最关键的一点，真爱难道可以估价吗？如此相亲被辜负的不只是爱情，更是一代人鲜活的人生啊！",
     "Một mặt nóng vội cầu lợi, mong con trèo được cành cao; một mặt lo lắng không yên, sợ bị người khác chia mất phần canh. Trông thì có vẻ là một trò chơi của những người khôn ngoan, nhưng dường như họ lại quên đúng điều quan trọng nhất: lẽ nào tình yêu đích thực lại có thể định giá? Xem mắt như vậy, thứ bị phụ bạc không chỉ là tình yêu, mà còn là cuộc đời tươi trẻ, sống động của cả một thế hệ!",
     ["一方面……一方面…… là một mặt… một mặt…. 攀上高枝 là trèo lên cành cao. 忧心忡忡 là lo lắng không yên. 分一杯羹 là chia một bát canh, tức là chia phần lợi ích.",
      "看似 là trông như. 恰恰 là đúng, chính. Câu hỏi tu từ 真爱难道可以估价吗 là chủ đề của cả bài. Câu kết dùng mẫu 不只是……更是……, cùng kết hợp từ 辜负爱情, để lại ấn tượng sâu sắc."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 相亲鄙视链", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa. Bài được cải biên từ bài viết 相亲鄙视链，这是爱情被黑得最惨的一次, Chuỗi khinh miệt xem mắt, lần tình yêu bị bôi đen thảm hại nhất, đăng trên trang tin của 中国青年报 ngày mười bảy tháng bảy năm hai nghìn không trăm mười bảy, tác giả là 孙一秋.",
         F(0, "Thầy chia bài thành mười bốn đoạn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng. Bài này có giọng văn châm biếm nhẹ nhàng, các bạn hãy chú ý những chỗ tác giả mỉa mai nhé."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 70 else 50 if len(zh) <= 90 else 46
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Ý chính bài khóa", section="Bài khóa 课文", title="Mạch bài báo", size=34,
    items=["## 1. Cảnh tượng: chợ xem mắt trong công viên Bắc Kinh",
           "大爷大妈一字排开 · 征婚简历: 户籍、收入、房产、学历 in đỏ, đậm · 人口贩卖市场",
           "## 2. Thông cảm: vì sao cha mẹ 亲自出马？",
           "Con bận sự nghiệp, ít cơ hội gặp người khác giới · sợ lỡ 适婚年龄 → 实属无奈",
           "## 3. Phê phán: tiêu chuẩn chọn bạn đời kỳ quặc",
           "Chỉ cần 北京户口 · 不要女博士 · 不要属羊的 → 父母代子相亲的弊端, người trẻ thành 背锅者",
           "## 4. Kết luận: 真爱难道可以估价吗？",
           "功利主义 · 明码标价 · 被辜负的不只是爱情，更是一代人鲜活的人生"],
    say=["Đọc xong bài khóa, chúng ta cùng tóm tắt mạch bài báo.",
         F(0, "Phần một: cảnh tượng. Tác giả kể lại phiên chợ xem mắt trong công viên Bắc Kinh."),
         F(1, "Các ông bà ngồi thành hàng, trước mặt là tờ lý lịch của con, trên đó hộ khẩu, thu nhập, nhà cửa, học vấn được in đỏ, in đậm. Cư dân mạng gọi đó là chợ buôn người."),
         F(2, "Phần hai: tác giả bày tỏ sự thông cảm. Vì sao cha mẹ phải đích thân ra tay?"),
         F(3, "Vì con cái bận rộn với sự nghiệp, ít cơ hội gặp người khác giới, cha mẹ sợ con lỡ tuổi kết hôn, nên đây là chuyện bất đắc dĩ."),
         F(4, "Phần ba: phê phán những tiêu chuẩn chọn bạn đời kỳ quặc."),
         F(5, "Chỉ cần có hộ khẩu Bắc Kinh, tàn tật cũng được; không lấy nữ tiến sĩ; không lấy người tuổi Mùi. Điều đó phơi bày mặt trái của việc cha mẹ xem mắt thay con, và giới trẻ bị đổ oan, thành người gánh tội thay."),
         F(6, "Phần bốn: kết luận bằng một câu hỏi: tình yêu đích thực có thể định giá được không?"),
         F(7, "Kiểu xem mắt đầy tính thực dụng, niêm yết giá như hàng hóa, thứ bị phụ bạc không chỉ là tình yêu, mà còn là cuộc đời sống động của cả một thế hệ.")])

# ======================= CÂU MẪU =======================
add("bullets", chapter="Câu mẫu: 乍一看 · 无非 · 不由得 · 看似", section="Câu mẫu 重点句型", title="1. 乍一看…… · 2. 无非（是）……", size=31,
    items=["## 乍一看: thoạt nhìn, nhìn qua lần đầu (không có ý “quan sát kỹ”); vế sau thường là ấn tượng ban đầu, có thể khác thực tế",
           "……整整齐齐，井然有序，乍一看简直无异于一场大型的展销会。",
           "他戴着一副银丝边圆眼镜，乍一看有一种儒雅的风度。",
           "乍一看，异国恋和跨国婚姻像童话般美好，但它们往往根植于浪漫的想象。",
           "## 无非（是）: phó từ – chỉ, chẳng qua, không ngoài (hạ thấp, cho là không có gì đặc biệt)",
           "那地上一字排开的纸片便是征婚简历，无非列了几行个人介绍。",
           "我们活在世上，无非想要明白些道理，遇到些有趣的事。",
           "人生在世无非是让别人笑笑，偶尔笑笑别人。"],
    say=["Bây giờ chúng ta sang phần câu mẫu và từ ngữ trọng điểm. Bài này có tám điểm, thầy chia làm bốn slide.",
         F(0, "Điểm thứ nhất: 乍一看. 乍 là vừa mới, 一看 là nhìn một cái. 乍一看 là thoạt nhìn, nhìn qua lần đầu, không có ý quan sát kỹ. Vế sau thường nêu ấn tượng ban đầu, và ấn tượng này có khi khác với thực tế."),
         F(1, "Ví dụ một, từ bài khóa: 整整齐齐，井然有序，乍一看简直无异于一场大型的展销会。 Ngay ngắn, trật tự, thoạt nhìn chẳng khác nào một hội chợ lớn."),
         F(2, "Ví dụ hai: 他戴着一副银丝边圆眼镜，乍一看有一种儒雅的风度。 Ông ấy đeo cặp kính tròn gọng bạc, thoạt nhìn có phong thái nho nhã."),
         F(3, "Ví dụ ba: 乍一看，异国恋和跨国婚姻像童话般美好，但它们往往根植于浪漫的想象。 Thoạt nhìn, yêu xa khác quốc gia và hôn nhân xuyên quốc gia đẹp như cổ tích, nhưng chúng thường bắt rễ từ trí tưởng tượng lãng mạn. Các bạn thấy vế sau có 但: thực tế khác ấn tượng ban đầu."),
         F(4, "Điểm thứ hai: 无非, hoặc 无非是, phó từ, nghĩa là chỉ, chẳng qua là, không ngoài. Người nói dùng nó để hạ thấp, cho rằng sự việc chẳng có gì đặc biệt."),
         F(5, "Ví dụ một, từ bài khóa: 那地上一字排开的纸片便是征婚简历，无非列了几行个人介绍。 Chẳng qua chỉ liệt kê vài dòng giới thiệu bản thân."),
         F(6, "Ví dụ hai: 我们活在世上，无非想要明白些道理，遇到些有趣的事。 Chúng ta sống trên đời, chẳng qua là muốn hiểu được vài đạo lý, gặp được vài chuyện thú vị."),
         F(7, "Ví dụ ba: 人生在世无非是让别人笑笑，偶尔笑笑别人。 Đời người chẳng qua là để người khác cười mình một chút, thỉnh thoảng mình cười người khác một chút.")])

add("bullets", section="Câu mẫu 重点句型", title="3. 不由得…… · 4. 看似……，实则……", size=31,
    items=["## 不由得: không kìm được, bất giác (thường là vô thức); = 不禁",
           "我不由得冲旁边的大爷一乐，这一乐可不要紧，大爷来了精神……",
           "沐浴在春风里，我们感受着万物复苏的清新气息，心中不由得产生了对生命至诚的热爱。",
           "看着他认真的眼睛里闪烁着智慧的光芒，她不由得怦然心动。",
           "## 看似……，实则……: trông thì có vẻ…, thực ra lại… (bề ngoài và thực chất khác nhau)",
           "大爷大妈们通过浏览相亲材料，以及看似闲聊、实则互相摸底的方式，就想为子女找到另一半。",
           "人生如海，有时看似风平浪静，实则暗流涌动。",
           "这则看似令人震惊的新闻，……实则不过是意料中事。"],
    say=[F(0, "Điểm thứ ba: 不由得. Nghĩa là không kìm được, không tự chủ được, thường là phản ứng vô thức. Giống 不禁. Sau 不由得 là một động tác hay cảm xúc bột phát."),
         F(1, "Ví dụ một, từ bài khóa: 我不由得冲旁边的大爷一乐。 Tôi bất giác mỉm cười với ông cụ bên cạnh."),
         F(2, "Ví dụ hai: 沐浴在春风里，我们感受着万物复苏的清新气息，心中不由得产生了对生命至诚的热爱。 Tắm mình trong gió xuân, cảm nhận hơi thở tươi mới của vạn vật hồi sinh, trong lòng bất giác trào dâng một tình yêu chân thành với sự sống."),
         F(3, "Ví dụ ba: 看着他认真的眼睛里闪烁着智慧的光芒，她不由得怦然心动。 Nhìn ánh sáng trí tuệ lấp lánh trong đôi mắt nghiêm túc của anh, cô bất giác rung động. 怦然心动 là tim đập rộn ràng, rung động."),
         F(4, "Điểm thứ tư: 看似……实则……. Trông thì có vẻ như thế này, thực ra lại là thế khác. Bề ngoài và thực chất không giống nhau. Bài năm chấm một cũng có câu: 旁观者看似无辜，实则纵容犯罪."),
         F(5, "Ví dụ một, từ bài khóa: 看似闲聊、实则互相摸底的方式。 Trông như tán gẫu, thực ra là dò hỏi nhau."),
         F(6, "Ví dụ hai: 人生如海，有时看似风平浪静，实则暗流涌动。 Đời người như biển cả, có lúc trông sóng yên biển lặng, thực ra bên dưới dòng chảy ngầm cuồn cuộn."),
         F(7, "Ví dụ ba: 这则看似令人震惊的新闻，对于任何一位稍稍知悉中国科研管理实际状况的人士而言，实则不过是意料中事。 Tin tức tưởng như gây chấn động này, với bất cứ ai hơi hiểu thực trạng quản lý nghiên cứu khoa học ở Trung Quốc, thực ra chỉ là chuyện đã nằm trong dự liệu.")])

add("bullets", chapter="Câu mẫu: 眼见着 · 索性 · 不只是 · 一时间", section="Câu mẫu 重点句型", title="5. 眼见（着）…… · 6. 索性", size=31,
    items=["## 眼见（着）: tận mắt thấy (sự việc đang diễn ra), hoặc nhấn mạnh sự việc diễn ra rất nhanh",
           "身为父母，眼见着子女们忙于事业，时间和精力在城市的快节奏中消失殆尽……",
           "老爷子已到了风烛残年，眼见儿孙不成器，已无能为力了。",
           "他眼见事迹败露，已经无法掩人耳目，只好俯首认罪。",
           "## 索性: phó từ – dứt khoát, đã vậy thì… luôn (= 干脆)",
           "……担心他们错过适婚年龄，心急火燎，索性亲自出马也实属无奈。",
           "现在已经很晚了，我索性在外面吃完饭再回家好了。",
           "既然已经开始做了，索性就把它做完吧。"],
    say=[F(0, "Điểm thứ năm: 眼见, hoặc 眼见着. Thường dùng để nhấn mạnh tận mắt nhìn thấy một sự việc đang xảy ra, hoặc cho thấy sự việc diễn ra rất nhanh. Tiếng Việt: trơ mắt nhìn, tận mắt thấy, mắt thấy."),
         F(1, "Ví dụ một, từ bài khóa: 身为父母，眼见着子女们忙于事业，时间和精力在城市的快节奏中消失殆尽。 Là cha mẹ, tận mắt thấy con cái bận rộn sự nghiệp, thời gian sức lực tiêu tan hết."),
         F(2, "Ví dụ hai: 老爷子已到了风烛残年，眼见儿孙不成器，已无能为力了。 Ông cụ đã đến tuổi gió thổi đèn tàn, trơ mắt nhìn con cháu chẳng nên người mà đành bất lực. 风烛残年 là tuổi già sắp tàn như ngọn nến trước gió; 不成器 là không nên người."),
         F(3, "Ví dụ ba: 他眼见事迹败露，已经无法掩人耳目，只好俯首认罪。 Hắn thấy chuyện đã bại lộ, không thể che mắt thiên hạ được nữa, đành cúi đầu nhận tội."),
         F(4, "Điểm thứ sáu: 索性, phó từ, nghĩa là dứt khoát, thẳng thừng, giống 干脆. Thường dùng khi tình huống đã như vậy rồi, thì làm luôn một cách triệt để."),
         F(5, "Ví dụ một, từ bài khóa: 担心他们错过适婚年龄，心急火燎，索性亲自出马也实属无奈。 Lo con lỡ tuổi kết hôn, sốt ruột như lửa đốt, thế là dứt khoát tự mình ra tay."),
         F(6, "Ví dụ hai: 现在已经很晚了，我索性在外面吃完饭再回家好了。 Bây giờ muộn lắm rồi, tôi ăn cơm ở ngoài luôn rồi hãy về nhà vậy."),
         F(7, "Ví dụ ba: 既然已经开始做了，索性就把它做完吧。 Đã bắt đầu làm rồi thì làm cho xong luôn đi.")])

add("bullets", section="Câu mẫu 重点句型", title="7. 不只是……，更在于…… · 8. 一时间", size=31,
    items=["## 不只是A，更在于B: không chỉ là A, mà (quan trọng hơn) còn ở B – cấu trúc tăng tiến",
           "不过人们质疑最多的，不只是父母这种为子女相亲的方式，更在于他们眼中的择偶标准。",
           "培养“阳刚之气”不只是体魄，更在于精神。",
           "感恩不只是言谢，更在于铭记于心，落实于行。",
           "## 一时间: trong chốc lát, nhất thời – thời gian rất ngắn",
           "……一时间双方争吵来争吵去，谁也不服谁。",
           "一场突如其来的大灾难让人们意识到生命的脆弱，“平安活着”一时间成为大家最真实的渴望。",
           "面对这封没有署名的求助信，大家一时间不知如何是好。"],
    say=[F(0, "Điểm thứ bảy: 不只是……更在于……. Đây là cấu trúc tăng tiến: không chỉ là A, mà quan trọng hơn còn ở B. Vế sau là điều người nói muốn nhấn mạnh."),
         F(1, "Ví dụ một, từ bài khóa: 不过人们质疑最多的，不只是父母这种为子女相亲的方式，更在于他们眼中的择偶标准。 Điều mọi người nghi ngờ nhiều nhất không chỉ là cách thức, mà quan trọng hơn là tiêu chuẩn chọn bạn đời của cha mẹ."),
         F(2, "Ví dụ hai: 培养阳刚之气不只是体魄，更在于精神。 Rèn luyện khí chất nam tính không chỉ là thể chất, mà quan trọng hơn là tinh thần. 体魄 là thể chất, cơ thể."),
         F(3, "Ví dụ ba: 感恩不只是言谢，更在于铭记于心，落实于行。 Biết ơn không chỉ là nói lời cảm ơn, mà còn ở chỗ khắc ghi trong lòng, thể hiện bằng hành động."),
         F(4, "Điểm thứ tám: 一时间, nghĩa là trong chốc lát, trong một thời gian rất ngắn. Thường đứng đầu câu hay trước động từ."),
         F(5, "Ví dụ một, từ bài khóa: 一时间双方争吵来争吵去，谁也不服谁。 Trong một thời gian, hai bên cãi qua cãi lại, chẳng ai phục ai."),
         F(6, "Ví dụ hai: 一场突如其来的大灾难让人们意识到生命的脆弱，平安活着一时间成为大家最真实的渴望。 Một thảm họa bất ngờ khiến mọi người nhận ra sự mong manh của sinh mệnh, được sống bình an bỗng chốc trở thành khát khao chân thật nhất của mọi người."),
         F(7, "Ví dụ ba: 面对这封没有署名的求助信，大家一时间不知如何是好。 Trước bức thư cầu cứu không ký tên này, mọi người nhất thời không biết phải làm sao.")])

add("bullets", section="Câu mẫu 重点句型", title="Luyện tập: chọn câu mẫu thích hợp", reveal=True, size=33,
    items=["## 乍一看 · 无非 · 不由得 · 看似……实则…… · 索性 · 一时间",
           "(1) 这道题___很简单，___很复杂。",
           "Đáp án: 看似……实则…… → 这道题看似很简单，实则很复杂。",
           "(2) 听到这个好消息，大家___欢呼起来。",
           "Đáp án: 不由得",
           "(3) 他说了半天，___是想让我们帮他搬家。",
           "Đáp án: 无非",
           "(4) 等了一个小时公交车还没来，我___打车去了。",
           "Đáp án: 索性",
           "(5) 消息传开，___全村的人都知道了。",
           "Đáp án: 一时间"],
    say=["Chúng ta luyện tập một chút: chọn câu mẫu thích hợp điền vào chỗ trống.",
         F(1, "Câu một: 这道题什么很简单，什么很复杂。 Bài này trông thì đơn giản, thực ra lại phức tạp. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 看似……实则……. 这道题看似很简单，实则很复杂。"),
         F(3, "Câu hai: 听到这个好消息，大家什么欢呼起来。 Nghe tin vui này, mọi người bất giác reo hò."),
         F(4, "Đáp án: 不由得. Reo hò là phản ứng vô thức, không kìm được."),
         F(5, "Câu ba: 他说了半天，什么是想让我们帮他搬家。 Anh ta nói cả buổi, chẳng qua là muốn chúng tôi giúp chuyển nhà."),
         F(6, "Đáp án: 无非. 无非是, chẳng qua là."),
         F(7, "Câu bốn: 等了一个小时公交车还没来，我什么打车去了。 Đợi một tiếng xe buýt vẫn chưa đến, tôi dứt khoát bắt taxi đi luôn."),
         F(8, "Đáp án: 索性. Tình huống đã thế, thì dứt khoát đổi cách."),
         F(9, "Câu năm: 消息传开，什么全村的人都知道了。 Tin tức lan ra, chỉ trong chốc lát cả làng đều biết."),
         F(10, "Đáp án: 一时间. Chỉ thời gian rất ngắn.")])

# ======================= KẾT HỢP TỪ =======================
add("bullets", chapter="Kết hợp từ", section="Kết hợp từ 词语搭配", title="Kết hợp từ: 实属 · 隔阂 · 辜负", size=31,
    items=["## 实属 + 无奈 / 不易 / 罕见 / 难得 (thật sự là…, văn viết)",
           "仅凭一纸限令就想遏制群租现象，实属不易。",
           "这个地瓜真是硕大无比，实属罕见。",
           "## 隔阂: 产生隔阂 · 消除隔阂 · 打破隔阂",
           "同学之间产生隔阂应该及时消除，以免影响班级团结。",
           "父母、子女任何一方的优越感都会对其他家庭成员造成心理压力，产生心理隔阂。",
           "## 辜负 + 爱情 / 厚望 / 重托 / 好意",
           "老师苦口婆心地教育我们要好好学习，我们不会辜负她的厚望。",
           "他身为国家干部，徇私枉法，辜负了人民的重托。"],
    say=["Tiếp theo là phần kết hợp từ. Bài này có ba nhóm.",
         F(0, "Nhóm một: 实属, nghĩa là thật sự là, văn viết, giống 确实是. Hay đi với 无奈，不易，罕见，难得: thật là bất đắc dĩ, thật không dễ, thật hiếm thấy, thật đáng quý. Trong bài: 索性亲自出马也实属无奈."),
         F(1, "Ví dụ: 仅凭一纸限令就想遏制群租现象，实属不易。 Chỉ dựa vào một tờ lệnh hạn chế mà muốn ngăn chặn hiện tượng cho thuê chia nhỏ, thật không dễ. 群租 là nhiều người chen chúc thuê chung một căn hộ."),
         F(2, "Ví dụ: 这个地瓜真是硕大无比，实属罕见。 Củ khoai lang này to vô cùng, thật hiếm thấy."),
         F(3, "Nhóm hai: 隔阂, khoảng cách. 产生隔阂, nảy sinh khoảng cách; 消除隔阂, xóa bỏ khoảng cách; 打破隔阂, phá vỡ khoảng cách. Trong bài: 北京人与外地人的隔阂."),
         F(4, "Ví dụ: 同学之间产生隔阂应该及时消除，以免影响班级团结。 Giữa bạn học nảy sinh khoảng cách thì nên kịp thời xóa bỏ, để khỏi ảnh hưởng đến đoàn kết của lớp."),
         F(5, "Ví dụ: 父母、子女任何一方的优越感都会对其他家庭成员造成心理压力，产生心理隔阂。 Cảm giác hơn người của bất kỳ ai, cha mẹ hay con cái, đều gây áp lực tâm lý cho các thành viên khác, sinh ra khoảng cách trong lòng."),
         F(6, "Nhóm ba: 辜负, phụ lòng. 辜负爱情, phụ bạc tình yêu; 辜负厚望, phụ kỳ vọng lớn; 辜负重托, phụ sự giao phó nặng nề; 辜负好意, phụ lòng tốt. Câu kết bài khóa: 如此相亲被辜负的不只是爱情."),
         F(7, "Ví dụ: 老师苦口婆心地教育我们要好好学习，我们不会辜负她的厚望。 Cô giáo hết lời khuyên bảo chúng tôi phải học hành chăm chỉ, chúng tôi sẽ không phụ kỳ vọng của cô. 苦口婆心 là hết lời khuyên nhủ."),
         F(8, "Ví dụ: 他身为国家干部，徇私枉法，辜负了人民的重托。 Ông ta là cán bộ nhà nước mà lại vì tư lợi làm trái pháp luật, phụ sự ủy thác của nhân dân. 徇私枉法 là vì tư lợi mà bẻ cong pháp luật.")])

# ======================= THÀNH NGỮ =======================
add("bullets", chapter="Thành ngữ (15)", section="Thành ngữ 成语", title="Thành ngữ (1): 惨不忍睹 · 井然有序 · 有血有肉", size=33,
    items=["## 惨不忍睹 cǎnbùrěndǔ – thảm khốc đến mức không nỡ nhìn (睹: nhìn)",
           "台风暴雨所造成的水灾，把市区淹得惨不忍睹。",
           "## 井然有序 jǐngrán-yǒuxù – ngăn nắp, có trật tự (井然: ngay ngắn)",
           "走进客厅，只见各样家具摆得井然有序，且窗明几净，看了真让人舒心。",
           "## 有血有肉 yǒuxuè-yǒuròu – bằng xương bằng thịt; (nhân vật) sinh động, sống động",
           "这部小说塑造了一个有血有肉、个性鲜明的人物形象，读后让人久久难忘。"],
    say=["Bây giờ chúng ta học mười lăm thành ngữ của bài, mỗi slide ba thành ngữ.",
         F(0, "Thứ nhất: 惨不忍睹. 惨 là thê thảm, 忍 là nỡ, 睹 là nhìn. Thê thảm đến mức không nỡ nhìn. Tên bài dùng theo nghĩa phóng đại, hài hước: 爱情被黑得惨不忍睹, tình yêu bị bôi đen thảm hại đến mức không nỡ nhìn."),
         F(1, "Ví dụ: 台风暴雨所造成的水灾，把市区淹得惨不忍睹。 Trận lụt do bão và mưa lớn gây ra đã nhấn chìm khu nội thành thảm khốc không nỡ nhìn."),
         F(2, "Thứ hai: 井然有序. 井然 là ngay ngắn chỉnh tề như ô ruộng hình chữ tỉnh, 有序 là có thứ tự. Ngăn nắp, trật tự, không lộn xộn."),
         F(3, "Ví dụ: 走进客厅，只见各样家具摆得井然有序，且窗明几净，看了真让人舒心。 Bước vào phòng khách, chỉ thấy đồ đạc bày biện ngăn nắp, cửa sổ sáng sủa, bàn ghế sạch bong, nhìn thật dễ chịu. 窗明几净 là cửa sáng bàn sạch."),
         F(4, "Thứ ba: 有血有肉. Có máu có thịt, ví với sự sống động, giàu sức sống, hay dùng để khen nhân vật trong tác phẩm văn học được khắc họa sinh động. Trong bài: 有血有肉、有思想有灵魂的男孩女孩."),
         F(5, "Ví dụ: 这部小说塑造了一个有血有肉、个性鲜明的人物形象，读后让人久久难忘。 Cuốn tiểu thuyết khắc họa một nhân vật sống động, cá tính rõ nét, đọc xong khiến người ta nhớ mãi.")])

add("bullets", section="Thành ngữ 成语", title="Thành ngữ (2): 评头论足 · 待价而沽 · 揠苗助长", size=33,
    items=["## 评头论足 píngtóu-lùnzú – bình phẩm soi mói từ đầu đến chân, chê bai tùy tiện",
           "随便对别人的容貌评头论足是非常没有教养的行为。",
           "## 待价而沽 dàijià'érgū – chờ giá cao mới bán; chờ được trọng dụng, đãi ngộ tốt",
           "他刚离职，就被猎头公司盯上了，正待价而沽。",
           "## 揠苗助长 yàmiáo-zhùzhǎng – nhổ mạ lên cho mau lớn: nóng vội làm trái quy luật, hỏng việc",
           "学习要循序渐近，若是急于求成，最后只能落得个揠苗助长的后果，得不偿失。"],
    say=[F(0, "Thứ tư: 评头论足. 评 và 论 là bình luận, 头 và 足 là đầu và chân. Bình phẩm từ đầu đến chân, tùy tiện chê bai, soi mói người khác. Trong bài: 供众人评头论足."),
         F(1, "Ví dụ: 随便对别人的容貌评头论足是非常没有教养的行为。 Tùy tiện bình phẩm dung mạo người khác là hành vi rất thiếu giáo dục."),
         F(2, "Thứ năm: 待价而沽. 待 là chờ, 价 là giá, 沽 là bán. Chờ có giá cao mới bán. Xưa ví với người tài chờ thời cơ ra làm quan; nay hay chỉ việc chờ được trọng dụng, có đãi ngộ tốt mới chịu nhận việc. Trong bài dùng nghĩa đen để mỉa mai: 待价而沽的商品式相亲."),
         F(3, "Ví dụ: 他刚离职，就被猎头公司盯上了，正待价而沽。 Anh ấy vừa nghỉ việc đã bị công ty săn đầu người để mắt tới, đang chờ được trả giá cao."),
         F(4, "Thứ sáu: 揠苗助长. 揠 là nhổ lên, 苗 là mạ, 助长 là giúp lớn, chữ 长 đọc zhǎng. Truyện kể một người nước Tống chê lúa lớn chậm, bèn nhổ từng cây lên một chút, kết quả lúa chết héo hết. Ví với việc nóng vội làm trái quy luật, kết quả hỏng việc. Tiếng Việt có câu: dục tốc bất đạt."),
         F(5, "Ví dụ: 学习要循序渐近，若是急于求成，最后只能落得个揠苗助长的后果，得不偿失。 Học tập phải tuần tự từng bước, nếu nóng vội cầu thành, cuối cùng chỉ chuốc lấy hậu quả nhổ mạ cho mau lớn, được ít mất nhiều. 得不偿失 các bạn đã học ở HSK sáu.")])

add("bullets", section="Thành ngữ 成语", title="Thành ngữ (3): 急功近利 · 心急火燎 · 风口浪尖", size=33,
    items=["## 急功近利 jígōng-jìnlì – nóng vội cầu thành tích và lợi ích trước mắt",
           "做学术研究需要刻苦钻研和长期的努力，急功近利肯定是不行的。",
           "## 心急火燎 xīnjí-huǒliǎo – lòng nóng như lửa đốt, sốt ruột vô cùng",
           "当收到奶奶病危的消息时，我们都放下手头上的工作，心急火燎地赶回家。",
           "## 风口浪尖 fēngkǒu-làngjiān – đầu sóng ngọn gió: nơi tranh cãi, căng thẳng gay gắt nhất",
           "疫苗问世后不久，关于疫苗安全性的问题马上被推上了风口浪尖。"],
    say=[F(0, "Thứ bảy: 急功近利. 急功 là nóng vội lập công, 近利 là ham lợi trước mắt. Chỉ việc nóng lòng đạt được thành quả và lợi ích trong thời gian ngắn. Trong bài, 揠苗助长 và 急功近利 đi liền nhau để phê phán sự nóng vội của cha mẹ."),
         F(1, "Ví dụ: 做学术研究需要刻苦钻研和长期的努力，急功近利肯定是不行的。 Làm nghiên cứu học thuật cần chuyên tâm khổ luyện và nỗ lực lâu dài, nóng vội cầu lợi chắc chắn không được."),
         F(2, "Thứ tám: 心急火燎. Lòng nóng như bị lửa đốt, chữ cuối đọc là liǎo, nghĩa là xém, đốt. Tức là vô cùng sốt ruột, lo lắng. Trong bài: 担心他们错过适婚年龄，心急火燎."),
         F(3, "Ví dụ: 当收到奶奶病危的消息时，我们都放下手头上的工作，心急火燎地赶回家。 Khi nhận tin bà nguy kịch, chúng tôi đều gác lại công việc, lòng như lửa đốt vội vã về nhà."),
         F(4, "Thứ chín: 风口浪尖. Nơi gió to sóng lớn nhất, ví với nơi tình thế căng thẳng, gay gắt nhất, hay tâm điểm của dư luận. Tiếng Việt: đầu sóng ngọn gió. Mẫu hay dùng: 被推上风口浪尖, bị đẩy lên đầu sóng ngọn gió."),
         F(5, "Ví dụ: 疫苗问世后不久，关于疫苗安全性的问题马上被推上了风口浪尖。 Vắc-xin ra đời chưa bao lâu, vấn đề an toàn của vắc-xin lập tức bị đẩy lên đầu sóng ngọn gió.")])

add("bullets", section="Thành ngữ 成语", title="Thành ngữ (4): 哭笑不得 · 不约而同 · 明码标价", size=33,
    items=["## 哭笑不得 kūxiào-bùdé – dở khóc dở cười",
           "我小时候特别调皮，搞过很多令人哭笑不得的恶作剧。",
           "## 不约而同 bùyuē'értóng – không hẹn mà gặp, không hẹn mà cùng",
           "大家对于他新颖的设计赞叹不已，不约而同地站起来为他鼓掌。",
           "## 明码标价 míngmǎ-biāojià – niêm yết giá công khai",
           "当地新出台的政策规定，商品一律明码标价，广告必须实事求是。"],
    say=[F(0, "Thứ mười: 哭笑不得. Khóc cũng không được, cười cũng không xong, chỉ tình huống trớ trêu, không biết phải làm sao. Tiếng Việt: dở khóc dở cười. Trong bài: 大爷大妈们的迷信心理令网友们哭笑不得."),
         F(1, "Ví dụ: 我小时候特别调皮，搞过很多令人哭笑不得的恶作剧。 Hồi nhỏ tôi rất nghịch ngợm, đã bày ra nhiều trò đùa khiến người ta dở khóc dở cười. 恶作剧 là trò chơi khăm."),
         F(2, "Thứ mười một: 不约而同. 约 là hẹn. Không hẹn trước mà ý kiến, hành động lại hoàn toàn giống nhau. Tiếng Việt: không hẹn mà cùng. Trong bài: 他们不约而同地列出子女具备的各种优势."),
         F(3, "Ví dụ: 大家对于他新颖的设计赞叹不已，不约而同地站起来为他鼓掌。 Mọi người trầm trồ không ngớt trước thiết kế mới lạ của anh, không hẹn mà cùng đứng dậy vỗ tay."),
         F(4, "Thứ mười hai: 明码标价. 明码 là con số công khai, 标价 là ghi giá. Niêm yết giá công khai, vốn là quy định thương mại. Trong bài đặt trong ngoặc kép để châm biếm: cha mẹ ghi giá con mình như hàng hóa."),
         F(5, "Ví dụ: 当地新出台的政策规定，商品一律明码标价，广告必须实事求是。 Chính sách mới ban hành của địa phương quy định hàng hóa phải niêm yết giá công khai, quảng cáo phải đúng sự thật.")])

add("bullets", section="Thành ngữ 成语", title="Thành ngữ (5): 坚持不懈 · 忧心忡忡 · 分一杯羹", size=33,
    items=["## 坚持不懈 jiānchí-bùxiè – kiên trì bền bỉ, không lơi lỏng",
           "在科研人员坚持不懈地努力下，这项实验终于成功了。",
           "## 忧心忡忡 yōuxīn-chōngchōng – lo lắng không yên, lo âu canh cánh",
           "住在隔壁的奶奶担心在外打拼的儿子，总是一副忧心忡忡的样子。",
           "## 分一杯羹 fēn yì bēi gēng – chia một bát canh: chia phần lợi ích",
           "鲜花速递使得网上订花成为可能，几家电商也纷纷加入七夕鲜花市场试图分一杯羹。"],
    say=[F(0, "Thứ mười ba: 坚持不懈. 懈 là lơi lỏng. Kiên trì, không hề buông lỏng, chỉ người làm việc có ý chí, có nghị lực."),
         F(1, "Ví dụ: 在科研人员坚持不懈地努力下，这项实验终于成功了。 Nhờ sự nỗ lực bền bỉ của các nhà nghiên cứu, thí nghiệm này cuối cùng đã thành công."),
         F(2, "Thứ mười bốn: 忧心忡忡. 忧心 là lòng lo, 忡忡 là dáng lo âu không yên. Lo lắng canh cánh trong lòng."),
         F(3, "Ví dụ: 住在隔壁的奶奶担心在外打拼的儿子，总是一副忧心忡忡的样子。 Bà cụ nhà bên lo cho cậu con trai đang bươn chải nơi xa, lúc nào cũng mang vẻ lo âu."),
         F(4, "Thứ mười lăm: 分一杯羹. 羹 là canh. Chia một bát canh, ví với việc chia phần lợi ích. Trong bài: 担心被别人分走一杯羹, sợ người khác chia mất phần."),
         F(5, "Ví dụ: 鲜花速递使得网上订花成为可能，几家电商也纷纷加入七夕鲜花市场试图分一杯羹。 Dịch vụ giao hoa nhanh khiến việc đặt hoa qua mạng trở nên khả thi, mấy sàn thương mại điện tử cũng lần lượt nhảy vào thị trường hoa ngày Thất tịch để mong chia phần. 七夕 là ngày Thất tịch, ngày lễ tình nhân của Trung Quốc.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 课后练习", title="Bài tập 1: Điền thành ngữ (1)", reveal=True, size=33,
    items=["## 急功近利 · 不约而同 · 坚持不懈 · 忧心忡忡 · 哭笑不得 · 惨不忍睹 · 风口浪尖",
           "(1) 在候车室里，面对一位贫病交加的老妇人，大家___地向她伸出了援助之手。",
           "Đáp án: 不约而同",
           "(2) 所谓“十年树木，百年树人”，人才培养不应该是一件___的事情。",
           "Đáp án: 急功近利",
           "(3) 生活总是这样，期盼与世无争的人，却往往被推上___。",
           "Đáp án: 风口浪尖",
           "(4) 战争影片中___的搏杀情景，让每个观众都受到强烈的刺激。",
           "Đáp án: 惨不忍睹"],
    say=["Phần cuối là luyện tập. Bài tập một: điền thành ngữ. Có bảy thành ngữ cho bảy câu.",
         F(1, "Câu một: 在候车室里，面对一位贫病交加的老妇人，大家什么地向她伸出了援助之手。 Trong phòng chờ xe, trước một bà cụ vừa nghèo vừa bệnh, mọi người thế nào chìa tay giúp đỡ. 贫病交加 là nghèo đói bệnh tật dồn dập. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 不约而同. Mọi người không hẹn mà cùng giúp đỡ bà cụ."),
         F(3, "Câu hai: 所谓十年树木，百年树人，人才培养不应该是一件什么的事情。 Như câu mười năm trồng cây, trăm năm trồng người, việc đào tạo nhân tài không nên là việc thế nào."),
         F(4, "Đáp án: 急功近利. Trồng người cần cả trăm năm, không thể nóng vội cầu lợi trước mắt. 十年树木，百年树人 cũng là câu người Việt rất quen thuộc."),
         F(5, "Câu ba: 生活总是这样，期盼与世无争的人，却往往被推上什么。 Cuộc đời luôn như vậy, người mong sống không tranh giành với đời, lại thường bị đẩy lên đâu."),
         F(6, "Đáp án: 风口浪尖. Nhớ mẫu 被推上风口浪尖."),
         F(7, "Câu bốn: 战争影片中什么的搏杀情景，让每个观众都受到强烈的刺激。 Những cảnh chém giết thế nào trong phim chiến tranh khiến mỗi khán giả đều bị kích động mạnh."),
         F(8, "Đáp án: 惨不忍睹. Cảnh chém giết thảm khốc đến không nỡ nhìn.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 1: Điền thành ngữ (2)", reveal=True, size=34,
    items=["(5) 通过___的努力，他终于在科研上取得了令人瞩目的成就。",
           "Đáp án: 坚持不懈",
           "(6) 第一次做饭时，他把糖当成盐放进了锅里，令站在一旁的妈妈___。",
           "Đáp án: 哭笑不得",
           "(7) 他最近失业了，总是一副___的样子，担心家庭经济陷入危机。",
           "Đáp án: 忧心忡忡"],
    say=[F(0, "Câu năm: 通过什么的努力，他终于在科研上取得了令人瞩目的成就。 Nhờ nỗ lực thế nào, cuối cùng anh ấy đã đạt được thành tựu nổi bật trong nghiên cứu khoa học."),
         F(1, "Đáp án: 坚持不懈. 坚持不懈的努力, sự nỗ lực bền bỉ."),
         F(2, "Câu sáu: 第一次做饭时，他把糖当成盐放进了锅里，令站在一旁的妈妈什么。 Lần đầu nấu cơm, cậu ấy bỏ đường vào nồi thay muối, khiến bà mẹ đứng bên cạnh thế nào."),
         F(3, "Đáp án: 哭笑不得. Mẹ dở khóc dở cười."),
         F(4, "Câu bảy: 他最近失业了，总是一副什么的样子，担心家庭经济陷入危机。 Dạo này anh ấy thất nghiệp, lúc nào cũng mang vẻ thế nào, lo kinh tế gia đình rơi vào khủng hoảng."),
         F(5, "Đáp án: 忧心忡忡. 一副忧心忡忡的样子, vẻ mặt lo âu không yên.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn từ thích hợp nhất (1)", reveal=True, size=33,
    items=["(1) 有付出才有回报，我们（ ）那些不劳而获，坐享其成的人。  A.鄙视 B.轻视 C.忽视 D.歧视",
           "Đáp án: A. 鄙视 – coi khinh vì phẩm chất kém (轻视: xem nhẹ; 忽视: lơ là; 歧视: kỳ thị, phân biệt đối xử).",
           "(2) 只要当中任何一个人（ ）这个机密，整个任务就会功亏一篑。  A.暴露 B.泄露 C.显露 D.透露",
           "Đáp án: B. 泄露 – làm lộ bí mật (泄露机密); 暴露: phơi bày ra; 透露: tiết lộ (thông tin, thường cố ý, không xấu).",
           "(3) 在科学研究中，敢于（ ）权威的观点，才谈得上创新与进步。  A.质疑 B.怀疑 C.疑问 D.质问",
           "Đáp án: A. 质疑 – công khai đặt nghi vấn với quan điểm (质疑权威); 质问: chất vấn người; 疑问 là danh từ."],
    say=["Bài tập hai: chọn từ thích hợp nhất. Đây là bài phân biệt từ gần nghĩa, rất đáng chú ý.",
         F(0, "Câu một: 有付出才有回报，我们什么那些不劳而获，坐享其成的人。 Có bỏ công mới có đền đáp, chúng ta thế nào với những kẻ không làm mà hưởng, ngồi mát ăn bát vàng. Lựa chọn: 鄙视，轻视，忽视，歧视."),
         F(1, "Đáp án: A, 鄙视. Coi khinh vì phẩm chất kém. 轻视 là xem nhẹ, coi thường năng lực; 忽视 là lơ là, không chú ý; 歧视 là kỳ thị, đối xử bất công vì giới tính, chủng tộc, vùng miền, như 地域歧视 trong bài."),
         F(2, "Câu hai: 只要当中任何一个人什么这个机密，整个任务就会功亏一篑。 Chỉ cần bất cứ ai trong số đó làm sao với bí mật này, cả nhiệm vụ sẽ đổ bể vào phút chót. Lựa chọn: 暴露，泄露，显露，透露. 功亏一篑 là công dã tràng vì thiếu một sọt đất cuối cùng."),
         F(3, "Đáp án: B, 泄露. 泄露机密 là làm lộ bí mật, cụm cố định. 暴露 là phơi bày ra, thường là điều vốn bị che giấu như 暴露弊端, 暴露身份; 显露 là hiện ra; 透露 là tiết lộ thông tin, thường là cố ý và không mang nghĩa xấu."),
         F(4, "Câu ba: 在科学研究中，敢于什么权威的观点，才谈得上创新与进步。 Trong nghiên cứu khoa học, dám làm gì với quan điểm của người có uy tín, mới nói đến chuyện sáng tạo và tiến bộ. Lựa chọn: 质疑，怀疑，疑问，质问."),
         F(5, "Đáp án: A, 质疑. 质疑权威 là đặt nghi vấn với quyền uy. 怀疑 thiên về nghi ngờ trong lòng; 疑问 là danh từ, không mang tân ngữ; 质问 là chất vấn, hỏi vặn một người nào đó.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn từ thích hợp nhất (2)", reveal=True, size=34,
    items=["(4) 现在回想起来，我真是（ ）了父亲平日里对我谆谆不倦的教诲。  A.无辜 B.辜负 C.负疚 D.负担",
           "Đáp án: B. 辜负 – phụ lời dạy bảo của cha (辜负教诲).",
           "(5) 所谓的“忘年交”，不会因为年龄的差距而产生（ ）。  A.隔阂 B.隔离 C.分隔 D.隔壁",
           "Đáp án: A. 隔阂 – 产生隔阂: nảy sinh khoảng cách."],
    say=[F(0, "Câu bốn: 现在回想起来，我真是什么了父亲平日里对我谆谆不倦的教诲。 Bây giờ nghĩ lại, tôi thật đã làm sao với những lời dạy bảo ân cần không mệt mỏi của cha ngày thường. Lựa chọn: 无辜，辜负，负疚，负担."),
         F(1, "Đáp án: B, 辜负. 辜负了父亲的教诲, phụ lời dạy bảo của cha. 无辜 là vô tội, từ mới bài năm chấm một; 负疚 là áy náy, bài năm chấm hai; 负担 là gánh nặng. Một câu ôn được từ của cả ba bài!"),
         F(2, "Câu năm: 所谓的忘年交，不会因为年龄的差距而产生什么。 Cái gọi là bạn vong niên, sẽ không vì khoảng cách tuổi tác mà nảy sinh cái gì. Lựa chọn: 隔阂，隔离，分隔，隔壁."),
         F(3, "Đáp án: A, 隔阂. 产生隔阂 là cụm kết hợp từ vừa học. 隔离 là cách ly; 分隔 là ngăn chia; 隔壁 là nhà bên cạnh. 忘年交 là tình bạn vong niên, bạn bè chênh lệch nhiều tuổi.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ và câu mẫu trả lời câu hỏi", reveal=True, size=31,
    items=["(1) 北京公园有什么样的场景？（乍一看……，无异于……）",
           "Đáp án gợi ý: 大爷大妈们一字排开坐在小板凳上，每人面前摆一张纸片，乍一看，简直无异于一场大型的展销会。",
           "(2) 征婚简历写了什么？（无非是……）",
           "Đáp án gợi ý: 无非是几行个人介绍，而户籍、收入、房产、学历等条件则用大红的粗字体写得十分醒目。",
           "(3) 父母们为什么如此着急？（眼见着……）",
           "Đáp án gợi ý: 父母们眼见着子女忙于事业，很难有与异性相处的机会，担心他们错过适婚年龄。",
           "(4) 父母代相亲出于何种心理？（攀高枝，被分走一杯羹）",
           "Đáp án gợi ý: 他们一方面急功近利，希望子女攀上高枝；另一方面忧心忡忡，担心被别人分走一杯羹。"],
    say=["Bài tập ba: dùng từ và câu mẫu cho sẵn để trả lời câu hỏi về bài khóa. Thầy đưa đáp án gợi ý.",
         F(0, "Câu một: 北京公园有什么样的场景？ Trong công viên Bắc Kinh có cảnh tượng gì? Dùng 乍一看 và 无异于."),
         F(1, "Đáp án gợi ý: 大爷大妈们一字排开坐在小板凳上，每人面前摆一张纸片，乍一看，简直无异于一场大型的展销会。"),
         F(2, "Câu hai: 征婚简历写了什么？ Lý lịch tìm bạn đời viết những gì? Dùng 无非是."),
         F(3, "Đáp án gợi ý: 无非是几行个人介绍，而户籍、收入、房产、学历等条件则用大红的粗字体写得十分醒目。"),
         F(4, "Câu ba: 父母们为什么如此着急？ Vì sao cha mẹ sốt ruột như vậy? Dùng 眼见着."),
         F(5, "Đáp án gợi ý: 父母们眼见着子女忙于事业，很难有与异性相处的机会，担心他们错过适婚年龄。"),
         F(6, "Câu bốn: 父母代相亲出于何种心理？ Cha mẹ xem mắt thay con xuất phát từ tâm lý gì? Dùng 攀高枝 và 被分走一杯羹."),
         F(7, "Đáp án gợi ý: 他们一方面急功近利，希望子女攀上高枝；另一方面忧心忡忡，担心被别人分走一杯羹。 Một mặt nóng vội cầu lợi, mong con trèo cao; mặt khác lo lắng không yên, sợ người khác chia mất phần.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Điền thành ngữ vào đoạn văn “年关恐惧症”", reveal=True, size=32,
    items=["## 坚持不懈 · 僵持不下 · 心急火燎 · 评头论足 · 有血有肉 · 待价而沽",
           "……春节正是家中长辈的“催婚季”，没有一个___的年轻人愿意在相亲市场上被___，如同商品一样___，许多父母___、一厢情愿地为儿女安排各种相亲……老年人___地催促儿女成婚，反倒造成双方___的局面。",
           "Đáp án: 有血有肉 · 评头论足 · 待价而沽 · 心急火燎 · 坚持不懈 · 僵持不下"],
    say=["Bài tập bốn: dùng thành ngữ cho sẵn điền vào đoạn văn. Đoạn văn nói về 年关恐惧症, hội chứng sợ Tết: nhiều người trẻ độc thân sợ về nhà ăn Tết vì bị giục cưới. Có sáu thành ngữ, trong đó 僵持不下 là từ mới, nghĩa là giằng co không ai chịu ai.",
         F(1, "许多人忙着买票回家过年，但一些适婚却仍单身的年轻人却患上了年关恐惧症，因为春节正是家中长辈的催婚季，没有一个什么的年轻人愿意在相亲市场上被什么，如同商品一样什么，许多父母什么、一厢情愿地为儿女安排各种相亲，甚至有父母认为女性超过三十岁自身优势就消失殆尽。老年人什么地催促儿女成婚，反倒造成双方什么的局面。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 没有一个有血有肉的年轻人愿意在相亲市场上被评头论足，如同商品一样待价而沽，许多父母心急火燎、一厢情愿地为儿女安排各种相亲。老年人坚持不懈地催促儿女成婚，反倒造成双方僵持不下的局面。"),
         "Đoạn văn kết thúc thế này: 实际上，这种对立说到底，无非是两种不同婚恋观的碰撞。心理咨询师建议，父母要体谅儿女们的心情和愿望，不要给孩子太大的压力，更不要把欢聚变成了不欢而散。 Thực ra, sự đối lập này nói cho cùng chẳng qua là cuộc va chạm giữa hai quan niệm hôn nhân khác nhau. Chuyên gia tư vấn tâm lý khuyên cha mẹ nên thông cảm với tâm tư, mong muốn của con, đừng gây áp lực quá lớn, càng đừng biến cuộc sum họp thành cuộc chia tay chẳng vui vẻ gì. 不欢而散 là tan cuộc trong không vui."])

# ======================= THẢO LUẬN =======================
add("bullets", chapter="Thảo luận: liên hệ Việt Nam", section="Thảo luận 讨论", title="Thảo luận: xem mắt và chọn bạn đời ở Việt Nam", size=34,
    items=["“Môn đăng hộ đối” = 门当户对 · Tết đến: “Bao giờ lấy chồng?” = 催婚",
           "Mê tín tương tự 十羊九不全: “gái tuổi Dần” bị cho là khó lấy chồng; xem tuổi hợp – khắc trước khi cưới",
           "Giới trẻ: xem mắt qua ứng dụng, mạng xã hội (≈ 云相亲)",
           "## Luyện nói (dùng từ của bài):",
           "我认为择偶不应该只看户口、房产和收入。爱情不是商品，不能明码标价；父母可以给建议，但不应该代替子女做决定。",
           "Câu hỏi: 婚姻中的物质基础和爱情基础，孰轻孰重？"],
    say=["Trước khi ôn tập đơn vị, chúng ta cùng liên hệ với Việt Nam.",
         F(0, "Người Việt có câu môn đăng hộ đối, chính là 门当户对 của tiếng Trung: hai gia đình phải tương xứng về địa vị, gia thế. Và mỗi dịp Tết, câu hỏi bao giờ lấy chồng, bao giờ lấy vợ cũng là nỗi sợ của nhiều bạn trẻ, giống hệt 催婚 trong bài."),
         F(1, "Về mê tín, Việt Nam cũng có quan niệm gái tuổi Dần khó lấy chồng, hay phải xem tuổi hợp khắc trước khi cưới. Những định kiến này cũng vô lý như 十羊九不全 vậy."),
         F(2, "Ngày nay, nhiều bạn trẻ Việt Nam làm quen qua ứng dụng hẹn hò, mạng xã hội, giống 云相亲, xem mắt trên mây, mà phần ôn tập đơn vị sẽ nhắc tới."),
         F(3, "Bây giờ các bạn hãy luyện nói, cố gắng dùng các từ vừa học."),
         F(4, "Câu mẫu: 我认为择偶不应该只看户口、房产和收入。爱情不是商品，不能明码标价；父母可以给建议，但不应该代替子女做决定。 Tôi cho rằng chọn bạn đời không nên chỉ nhìn hộ khẩu, nhà cửa và thu nhập. Tình yêu không phải hàng hóa, không thể niêm yết giá; cha mẹ có thể góp ý, nhưng không nên quyết định thay con."),
         F(5, "Câu hỏi cho các bạn, cũng là một đề tranh biện của sách: 婚姻中的物质基础和爱情基础，孰轻孰重？ Trong hôn nhân, nền tảng vật chất và nền tảng tình yêu, cái nào nhẹ cái nào nặng? 孰 là cái nào, văn ngôn. Hãy tạm dừng video và trả lời bằng tiếng Trung nhé.")])

# ======================= ÔN TẬP ĐƠN VỊ =======================
add("bullets", chapter="Ôn tập đơn vị 5", section="Ôn tập đơn vị 单元练习", title="Ôn tập Đơn vị 5: 单元练习 “学以致用”", size=33,
    items=["一、建言献策: hậu quả của bạo lực gia đình với trẻ em, đề xuất biện pháp",
           "二、众说纷纭: nam giới bị bạo hành · thế nào là 啃老 · cha mẹ có quyền giục cưới? · tiểu phẩm 《每逢佳节被催婚》",
           "三、新闻报告: 单身 · 代相亲 · 催婚 · 逼婚   四、明察暗访: điều tra về 家暴 · 啃老 · 择偶标准",
           "五、各抒己见: 啃老族 hình thành thế nào · 每逢佳节被催婚 · 云相亲的利弊",
           "六、针锋相对: 6 đề tranh biện   七、Video tuyên truyền chống bạo lực gia đình",
           "八、妙笔生花: viết thư trả lời mẹ (≥ 800 chữ) · 一纸婚书真的重要吗？ · viết tiếp phim 《橄榄树下的情人》"],
    say=["Bây giờ chúng ta sang chương ôn tập Đơn vị năm. Sách có một phần bài tập tổng hợp mang tên 学以致用, học để vận dụng, gồm tám phần, nối kết cả ba bài: bạo lực gia đình, ăn bám bố mẹ, và xem mắt.",
         F(0, "Phần một, 建言献策, góp ý hiến kế: đọc ba tư liệu về ảnh hưởng của bạo lực gia đình đến tâm lý trẻ em, rồi đề xuất biện pháp. Một tư liệu kể: vì lớn lên trong bạo lực, người viết luôn tự ti, chỉ cần ai đối tốt một chút là đã rất mãn nguyện."),
         F(1, "Phần hai, 众说纷纭, mỗi người một ý: bàn về nam giới bị vợ bạo hành; thế nào thì tính là ăn bám; cha mẹ có quyền giục cưới không; và tiểu phẩm 每逢佳节被催婚, cứ đến ngày lễ là bị giục cưới."),
         F(2, "Phần ba, 新闻报告: chọn một từ khóa như 单身, độc thân; 代相亲, xem mắt thay; 催婚, giục cưới; 逼婚, ép cưới, tìm tin tức và báo cáo trước lớp. Phần bốn, 明察暗访: phỏng vấn mọi người về bạo lực gia đình, ăn bám và tiêu chuẩn chọn bạn đời."),
         F(3, "Phần năm, 各抒己见, mỗi người nói ý mình: một kẻ ăn bám hoàn hảo được hình thành thế nào; vì sao cha mẹ Trung Quốc thích giục cưới; và ưu nhược điểm của 云相亲, xem mắt trực tuyến."),
         F(4, "Phần sáu, 针锋相对, tranh biện đối đầu, với sáu đề; phần bảy là làm video tuyên truyền chống bạo lực gia đình."),
         F(5, "Phần tám, 妙笔生花, ngòi bút nở hoa: viết thư trả lời mẹ, bàn về việc có nhất thiết phải đăng ký kết hôn không, và viết tiếp kết thúc bộ phim Iran 橄榄树下的情人, Dưới bóng cây ô liu. Thầy sẽ chọn những phần tiêu biểu nhất để chúng ta cùng làm.")])

add("bullets", section="Ôn tập đơn vị 单元练习", title="Đọc hiểu: 父母有权催婚吗？", reveal=True, size=32,
    items=["Tóm tắt: dư luận gọi người giục cưới là “逼婚者”; tác giả cho rằng “催婚自有催婚的道理”: 男大当婚，女大当嫁, đừng lỡ tuổi sinh nở; người lớn “吃的盐多一些”, giục một chút “有何不可？”",
           "(1) 舆论如何看待催婚者？",
           "Đáp án: 舆论对催婚者很不友好，把“催婚者”叫做“逼婚者”，每逢过年就对“逼婚”一族口诛笔伐。",
           "(2) 作者对催婚持何种态度？",
           "Đáp án: 作者支持（理解）催婚，认为催婚自有催婚的道理，有些婚还非催不可。",
           "(3) 作者认为“男大当婚，女大当嫁”有什么道理？",
           "Đáp án: 人每个时期都有特定的使命，到了一定年龄就该婚嫁、生子，顺应生命时序；最佳生育年龄错过就无法挽回。",
           "(4) “吃的盐多一些”是什么意思？",
           "Đáp án: 指长辈年纪大、人生经验丰富，看事情比年轻人更远。"],
    say=["Bài đọc hiểu trong phần mỗi người một ý: 父母有权催婚吗？ Cha mẹ có quyền giục cưới không?",
         F(0, "Nội dung chính: dư luận dường như rất không thân thiện với người giục cưới, gọi họ là 逼婚者, kẻ ép cưới, cứ Tết đến là cùng nhau chỉ trích. Nhưng tác giả cho rằng giục cưới có cái lý của nó: 男大当婚，女大当嫁, trai lớn lấy vợ, gái lớn gả chồng; mỗi giai đoạn đời người có sứ mệnh riêng, lỡ tuổi sinh nở thì không lấy lại được. Người lớn là người từng trải, 吃的盐多一些, giục một chút thì có gì không được."),
         F(1, "Câu hỏi một: 舆论如何看待催婚者？ Dư luận nhìn nhận người giục cưới thế nào?"),
         F(2, "Đáp án: 舆论对催婚者很不友好，把催婚者叫做逼婚者，每逢过年就对逼婚一族口诛笔伐。 口诛笔伐 là dùng lời nói và ngòi bút để lên án."),
         F(3, "Câu hai: 作者对催婚持何种态度？ Tác giả có thái độ thế nào với việc giục cưới?"),
         F(4, "Đáp án: 作者支持催婚，认为催婚自有催婚的道理，有些婚还非催不可。 Tác giả ủng hộ, hay ít nhất là thông cảm với việc giục cưới; có những đám cưới không giục không được. Mẫu 非……不可 là không… không được."),
         F(5, "Câu ba: 作者认为男大当婚，女大当嫁有什么道理？ Theo tác giả, câu trai lớn lấy vợ, gái lớn gả chồng có lý ở chỗ nào?"),
         F(6, "Đáp án: 人每个时期都有特定的使命，到了一定年龄就该婚嫁、生子，顺应生命时序；最佳生育年龄错过就无法挽回。 Mỗi thời kỳ có sứ mệnh riêng, đến tuổi thì nên cưới xin, sinh con, thuận theo trình tự của sự sống; tuổi sinh nở tốt nhất đã lỡ thì không cứu vãn được."),
         F(7, "Câu bốn: 吃的盐多一些是什么意思？ Ăn muối nhiều hơn nghĩa là gì?"),
         F(8, "Đáp án: 指长辈年纪大、人生经验丰富，看事情比年轻人更远。 Chỉ người lớn tuổi từng trải, giàu kinh nghiệm, nhìn xa hơn người trẻ. Người Trung Quốc hay nói: 我吃的盐比你吃的饭还多, tôi ăn muối còn nhiều hơn anh ăn cơm. Tiếng Việt cũng có câu: tôi ăn muối nhiều hơn anh ăn cơm, giống hệt!")])

add("bullets", section="Ôn tập đơn vị 单元练习", title="Thảo luận: 哪些行为算啃老？(xếp hạng từ cao đến thấp)", reveal=True, size=30,
    items=["(1) 住在父母家，不给生活费  (2) 找不到工作，要父母资助出国留学  (3) 父母托熟人安排工作  (4) 让父母出结婚买房钱",
           "(5) 请父母带孩子，给“带孙费”，但父母一刻不得闲  (6) 回家两手空空，父母承担家务、开销还照顾孩子",
           "(7) 父母自愿给钱，“一个愿打一个愿挨”  (8) 经济不依赖，但事事甩手、向父母吐苦水 – “精神啃老”？",
           "请小组讨论，按啃老等级从高到低排序，并说明理由。",
           "Đáp án gợi ý: (2) > (4) > (1) > (6) > (8) > (5) > (3) > (7) – càng đòi nhiều tiền, càng coi là đương nhiên thì “啃老” càng nặng; (7) cha mẹ tự nguyện nên nhẹ nhất, nhưng vẫn là 变相的纵容."],
    say=["Một đề thảo luận rất hay trong phần ôn tập: 哪些行为算啃老？ Những hành vi nào thì tính là ăn bám bố mẹ? Sách đưa ra tám tình huống.",
         F(0, "Một: tốt nghiệp xong làm việc ở thành phố của bố mẹ, ở nhà bố mẹ, không đưa tiền sinh hoạt. Hai: mãi không tìm được việc, đề nghị bố mẹ bỏ tiền cho đi du học. Ba: không tìm được việc, bố mẹ nhờ người quen sắp xếp. Bốn: bắt bố mẹ bỏ tiền cưới vợ, mua nhà."),
         F(1, "Năm: sau khi cưới nhờ bố mẹ trông con, có đưa tiền trông cháu, nhưng bố mẹ năm này qua năm khác không lúc nào được nghỉ. Sáu: hay về thăm bố mẹ, nhưng về chỉ mang theo vợ con và cái miệng, hai tay không, mấy ngày ở nhà bố mẹ gánh hết việc nhà, chi tiêu, lại còn trông cháu."),
         F(2, "Bảy: bố mẹ tự nguyện cho con tiền, kiểu một người muốn đánh, một người muốn chịu đòn, có tính là ăn bám không? Tám: không dựa vào bố mẹ về kinh tế, nhưng việc gì cũng phủi tay, động chút là than thở, trút bầu tâm sự, bắt bố mẹ gánh áp lực tinh thần, có tính là ăn bám về tinh thần không?"),
         F(3, "Yêu cầu: thảo luận nhóm, xếp hạng mức độ ăn bám từ cao đến thấp và giải thích lý do. Các bạn tạm dừng và thử xếp hạng nhé."),
         F(4, "Đáp án gợi ý của thầy: hai, rồi bốn, rồi một, rồi sáu, rồi tám, rồi năm, rồi ba, cuối cùng là bảy. Tiêu chí là: càng đòi nhiều tiền, càng coi việc cha mẹ hy sinh là đương nhiên, thì mức độ càng nặng. Tình huống bảy cha mẹ tự nguyện nên nhẹ nhất, nhưng như bài năm chấm hai đã nói, đó vẫn là 变相的纵容. Đây là câu hỏi mở, các bạn hoàn toàn có thể xếp khác, miễn là giải thích được bằng tiếng Trung.")])

add("bullets", section="Ôn tập đơn vị 单元练习", title="Tranh biện & viết: chọn một đề để luyện", size=32,
    items=["## 针锋相对 – 6 đề tranh biện",
           "制止家暴，法律惩罚更有效还是道德教育更有效？ · 父母愿意给予经济支持，我该接受吗？",
           "父母帮忙带孙，是情分还是本分？ · 婚姻中的物质基础和爱情基础，孰轻孰重？",
           "门当户对的婚恋观过时了吗？ · 婚姻制度会消失吗？",
           "## 妙笔生花 – thư của một bà mẹ Hàng Châu (2018) từ chối mua nhà cho con trai 26 tuổi",
           "“你终归要自己飞翔的，而我和你爸爸只是你坚强的后盾，而不是永远顶在前面的那个。”",
           "Gợi ý thư trả lời (≥ 800 chữ): 感谢 → 反思自己的依赖 → 理解妈妈的苦心 → 计划自食其力 → 承诺"],
    say=["Phần cuối của chương ôn tập: tranh biện và viết.",
         F(0, "Sách đưa ra sáu đề tranh biện, liên quan đến cả ba bài."),
         F(1, "Đề một: 制止家暴，法律惩罚更有效还是道德教育更有效？ Ngăn chặn bạo lực gia đình, trừng phạt bằng pháp luật hiệu quả hơn hay giáo dục đạo đức hiệu quả hơn? Đề hai: 父母愿意给予一定的经济支持，我该接受吗？ Tốt nghiệp xong áp lực lớn, bố mẹ sẵn lòng hỗ trợ kinh tế, tôi có nên nhận không?"),
         F(2, "Đề ba: 父母帮忙带孙，是情分还是本分？ Ông bà trông cháu là tình nghĩa hay bổn phận? Đề bốn: 婚姻中的物质基础和爱情基础，孰轻孰重？ Nền tảng vật chất và nền tảng tình yêu trong hôn nhân, cái nào quan trọng hơn?"),
         F(3, "Đề năm: 门当户对的婚恋观过时了吗？ Quan niệm môn đăng hộ đối đã lỗi thời chưa? Đề sáu: 婚姻制度会消失吗？ Chế độ hôn nhân có biến mất không?"),
         F(4, "Phần viết tiêu biểu nhất: năm hai nghìn không trăm mười tám, một bà mẹ ở Hàng Châu viết thư từ chối mua nhà cho cậu con trai hai mươi sáu tuổi, bức thư lan truyền khắp mạng xã hội. Đề bài yêu cầu đóng vai con trai, viết thư trả lời mẹ, ít nhất tám trăm chữ."),
         F(5, "Câu đáng nhớ nhất trong thư: 你终归要自己飞翔的，而我和你爸爸只是你坚强的后盾，而不是永远顶在前面的那个。 Rốt cuộc con phải tự mình bay, còn bố mẹ chỉ là hậu phương vững chắc, chứ không phải người mãi mãi đứng chắn phía trước con."),
         F(6, "Gợi ý dàn ý thư trả lời: cảm ơn mẹ; tự nhìn lại sự dựa dẫm của mình; thấu hiểu tấm lòng của mẹ; lập kế hoạch tự nuôi sống bản thân, tức là 自食其力; và hứa hẹn. Hãy dùng thật nhiều từ của bài năm chấm hai như 情分，本分，自立自强，心安理得 nhé.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết", section="Tổng kết", title="Tổng kết bài 5.3 và Đơn vị 5", size=32,
    items=["Từ vựng bài 5.3: 相亲 · 鄙视 · 黑 · 征婚 · 醒目 · 硬性 · 供 · 浏览 · 摸底 · 殆尽 · 索性 · 质疑 · 择偶 · 隔阂 · 苟同 · 妖魔化 · 功利主义 · 辜负 · 鲜活",
           "Câu mẫu: 乍一看 · 无非 · 不由得 · 看似……实则…… · 眼见着 · 索性 · 不只是……更在于…… · 一时间",
           "Thành ngữ: 惨不忍睹 · 井然有序 · 有血有肉 · 评头论足 · 待价而沽 · 揠苗助长 · 急功近利 · 心急火燎 · 风口浪尖 · 哭笑不得 · 不约而同 · 明码标价 · 坚持不懈 · 忧心忡忡 · 分一杯羹",
           "## Đơn vị 5 · 家庭篇: ba câu chuyện, một thông điệp",
           "5.1 家暴 – 打破沉默，零容忍 · 5.2 啃老 – 情分不是本分，自食其力 · 5.3 相亲 – 真爱不能明码标价"],
    say=["Chúng ta cùng tổng kết bài năm chấm ba, và cũng là tổng kết Đơn vị năm.",
         F(0, "Về từ vựng bài năm chấm ba, các bạn cần đặc biệt nhớ: 相亲，鄙视，黑，征婚，醒目，硬性，供，浏览，摸底，殆尽，索性，质疑，择偶，隔阂，苟同，妖魔化，功利主义，辜负，鲜活."),
         F(1, "Về câu mẫu: 乍一看 là thoạt nhìn; 无非 là chẳng qua; 不由得 là bất giác; 看似……实则…… là trông thì… thực ra…; 眼见着 là tận mắt thấy; 索性 là dứt khoát; 不只是……更在于…… là không chỉ… mà còn ở…; và 一时间 là trong chốc lát."),
         F(2, "Về thành ngữ, mười lăm thành ngữ, nhiều nhất trong đơn vị. Hãy ôn kỹ những cặp hay đi cùng nhau như 揠苗助长 và 急功近利, 被推上风口浪尖, 一副忧心忡忡的样子."),
         F(3, "Và nhìn lại cả Đơn vị năm, chủ đề Gia đình: ba câu chuyện, một thông điệp."),
         F(4, "Bài năm chấm một: với bạo lực gia đình, phải phá vỡ sự im lặng, không khoan nhượng. Bài năm chấm hai: cha mẹ giúp con là tình nghĩa chứ không phải bổn phận, người trẻ phải tự lập. Bài năm chấm ba: tình yêu đích thực không thể niêm yết giá. Cả ba bài đều nói về một điều: gia đình hạnh phúc phải dựa trên sự tôn trọng, bình đẳng và độc lập của mỗi thành viên."),
         "Bài tập về nhà: hãy chọn một đề tranh biện trong phần ôn tập, viết bài nêu quan điểm khoảng năm trăm chữ, dùng ít nhất năm thành ngữ và ba câu mẫu của đơn vị. Nếu có thời gian, hãy thử viết thư trả lời bà mẹ Hàng Châu nhé.",
         "Cảm ơn các bạn đã theo dõi bài giảng. Chúc mừng các bạn đã hoàn thành Đơn vị năm! Ở bài sau, chúng ta bước sang Đơn vị sáu, 职场篇, chủ đề Nơi làm việc, với bài sáu chấm một: 职场九九六, văn hóa làm việc chín giờ sáng đến chín giờ tối, sáu ngày một tuần. Hẹn gặp lại các bạn. Chúc các bạn học tốt!"])

lesson = {
    "title": "顶石中文 – Bài 5.3: 相亲鄙视链：爱情被黑得惨不忍睹 (Chuỗi khinh miệt khi xem mắt: tình yêu bị bôi đen thảm hại)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"供众人": "工众人",        # gōng
                    "供读者": "工读者",        # gōng
                    "供参考": "工参考",        # gōng
                    "冲旁边": "铳旁边",        # chòng
                    "助长": "助掌",            # zhùzhǎng
                    "身为": "身维",            # shēnwéi
                    "称为": "称维",            # chēngwéi
                    "生肖为羊": "生肖维羊",    # wéi
                    "火燎": "火蓼",            # huǒliǎo
                    "背锅": "杯锅",            # bēiguō
                    "背黑锅": "杯黑锅",        # bēi hēiguō
                    "相处": "相楚",            # xiāngchǔ
                    "择偶": "则偶",            # zé'ǒu
                    "几净": "机净",            # jī jìng
                    "调皮": "条皮",            # tiáopí
                    "外行": "外航",            # wàiháng
                    "泄露": "泄漏",            # xièlòu
                    "孰轻孰重": "孰轻孰众",    # zhòng
                    "处以": "楚以",            # chǔyǐ
                    "给予": "己予",            # jǐyǔ
                    "长辈": "掌辈"},           # zhǎngbèi
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds53.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
