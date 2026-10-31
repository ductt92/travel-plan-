#!/usr/bin/env python3
"""Kịch bản bài giảng 顶石中文 – Bài 4.2 «机器人医生，简直神了！». Chạy để sinh ds42.json."""
import json
import os

TAG = "顶石中文 · Bài 4.2 · 机器人医生，简直神了！"
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
    zh="机器人医生，", py="简直神了！",
    vi="Bài 4.2: Bác sĩ robot, đúng là thần kỳ!",
    sub="Jīqìrén yīshēng, jiǎnzhí shén le!\nBài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng giáo trình 顶石中文, Đỉnh cao tiếng Trung.",
         "Hôm nay chúng ta học bài bốn chấm hai: 机器人医生，简直神了！ Nghĩa là: Bác sĩ robot, đúng là thần kỳ!",
         "Đây là bài thứ hai của Đơn vị bốn, 科技篇, Khoa học công nghệ. Ở bài trước, chúng ta thấy mặt trái của Internet: quyền riêng tư chỉ đáng một xu. Còn bài hôm nay cho thấy mặt sáng của công nghệ: trí tuệ nhân tạo giúp chữa bệnh ung thư.",
         "Bài khóa là một bản tin của 中国青年报, báo Thanh niên Trung Quốc, năm hai nghìn không trăm mười bảy. Nhân vật chính là Watson, bác sĩ robot của công ty IBM: chỉ trong mười giây, nó lục tìm hàng triệu trang tài liệu và đưa ra phác đồ điều trị trùng khớp với ý kiến của bác sĩ trưởng khoa. Vậy bác sĩ con người có bị thay thế không? Chúng ta cùng tìm hiểu nhé."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bản tin: bác sĩ robot Watson lần đầu khám bệnh ở Trung Quốc",
           "Nắm vững 44 từ mới (nhiều từ ngành y), kèm âm Hán Việt và ví dụ",
           "9 mẫu câu trọng điểm: 甚为 · 顺便 · 与此同时 · 也就是说 · 短短…… · N之adj · 比N还N · 愈发 · 造福(于)",
           "Kết hợp từ (生涯、从、庞大、倾力、打造) và 6 thành ngữ",
           "Luyện tập theo sách, thảo luận: AI trong y tế"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu bản tin: bác sĩ robot Watson lần đầu tiên khám bệnh ở Trung Quốc như thế nào, nó giỏi đến đâu, và người ta lo lắng điều gì."),
         F(1, "Thứ hai, nắm vững bốn mươi bốn từ mới. Bài này có rất nhiều từ ngành y, như 癌症，确诊，肿瘤，临床，化疗. Nhiều từ có âm Hán Việt giống hệt tiếng Việt, như lâm sàng, bệnh lý, nên rất dễ nhớ."),
         F(2, "Thứ ba, học chín mẫu câu trọng điểm, như 甚为, hết sức; 与此同时, đồng thời; cấu trúc 比医生还医生, bác sĩ hơn cả bác sĩ; và 造福于人类, mang lại hạnh phúc cho nhân loại."),
         F(3, "Thứ tư, học các kết hợp từ và sáu thành ngữ, như 破天荒，英雄所见略同，杞人忧天."),
         F(4, "Thứ năm, làm toàn bộ bài tập của sách, rồi thảo luận về trí tuệ nhân tạo trong y tế. Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé.")])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 课前思考", title="Suy nghĩ trước bài học (课前思考)", reveal=True, size=33,
    items=["(1) 在你们国家的医疗机构中，机器诊断的使用频率如何，费用高不高？",
           "Đáp án gợi ý: 大医院常用CT、核磁共振等机器做检查，费用不算低；人工智能诊断还在起步阶段。",
           "(2) 你手边使用了哪些人工智能设备？人工智能在生活中还有哪些应用？",
           "Đáp án gợi ý: 手机语音助手、智能音箱、翻译软件、聊天机器人；还有自动驾驶、人脸识别、智能客服……",
           "(3) 你对人工智能技术发展有没有担心？",
           "Đáp án gợi ý: 有一点担心：很多工作可能被机器取代，个人信息也可能被泄露。"],
    say=["Chúng ta bắt đầu bằng phần suy nghĩ trước bài học. Sách đưa ra ba câu hỏi.",
         F(0, "Câu một: 在你们国家的医疗机构中，机器诊断的使用频率如何，费用高不高？ Ở các cơ sở y tế nước bạn, máy móc được dùng để chẩn đoán nhiều không, chi phí có cao không? 医疗机构 là cơ sở y tế, 诊断 là chẩn đoán. Các bạn tạm dừng và nghĩ thử nhé."),
         F(1, "Đáp án gợi ý: 大医院常用CT、核磁共振等机器做检查，费用不算低；人工智能诊断还在起步阶段。 Bệnh viện lớn thường dùng máy CT, cộng hưởng từ để kiểm tra, chi phí không hề thấp; còn chẩn đoán bằng trí tuệ nhân tạo vẫn đang ở giai đoạn khởi đầu. 核磁共振 là chụp cộng hưởng từ, MRI."),
         F(2, "Câu hai: 你手边使用了哪些人工智能设备？人工智能在生活中还有哪些应用？ Bạn đang dùng những thiết bị trí tuệ nhân tạo nào? Trí tuệ nhân tạo còn được ứng dụng ở đâu trong cuộc sống?"),
         F(3, "Đáp án gợi ý: 手机语音助手，智能音箱，翻译软件，聊天机器人；还有自动驾驶，人脸识别，智能客服. Tức là trợ lý giọng nói trên điện thoại, loa thông minh, phần mềm dịch, chatbot; còn có xe tự lái, nhận diện khuôn mặt, và tổng đài chăm sóc khách hàng tự động."),
         F(4, "Câu ba: 你对人工智能技术发展有没有担心？ Bạn có lo lắng gì về sự phát triển của công nghệ trí tuệ nhân tạo không?"),
         F(5, "Đáp án gợi ý: 有一点担心：很多工作可能被机器取代，个人信息也可能被泄露。 Có hơi lo: nhiều công việc có thể bị máy móc thay thế, thông tin cá nhân cũng có thể bị rò rỉ. Từ 泄露 các bạn vừa học ở bài trước đấy.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("神", "shén", "thần", "tính từ", "thần kỳ, tài tình đến khó tin", "这个魔术太神了！", "Màn ảo thuật này thần kỳ quá!",
     "Tính từ, nghĩa là cao siêu, kỳ lạ đến mức khiến người ta kinh ngạc, khẩu ngữ. Hay gặp 神速, nhanh như thần; 神效, hiệu nghiệm như thần; và câu 这事真是越说越神了, chuyện này càng kể càng thần kỳ. Tên bài 简直神了 là đúng là thần kỳ."),
    ("亮相", "liàngxiàng", "lượng tướng", "động từ", "ra mắt, xuất hiện công khai", "这款新车将在车展上首次亮相。", "Mẫu xe mới này sẽ lần đầu ra mắt tại triển lãm ô tô.",
     "Động từ, nghĩa gốc là diễn viên kịch tạo dáng khi bước ra sân khấu; nay chỉ việc ra mắt, xuất hiện công khai trước mọi người. Chữ thứ hai đọc thanh bốn. Hay gặp 首次亮相, lần đầu ra mắt."),
    ("义诊", "yìzhěn", "nghĩa chẩn", "động từ", "khám bệnh miễn phí (từ thiện)", "医生们周末去农村义诊。", "Cuối tuần các bác sĩ về nông thôn khám bệnh miễn phí.",
     "Động từ, nghĩa là bác sĩ khám chữa bệnh không lấy tiền. Chữ 义 là nghĩa, như trong 义务, nghĩa vụ; 义卖, bán hàng gây quỹ từ thiện."),
    ("癌症", "áizhèng", "nham chứng", "danh từ", "bệnh ung thư", "吸烟会增加患癌症的风险。", "Hút thuốc làm tăng nguy cơ mắc bệnh ung thư.",
     "Danh từ, nghĩa là bệnh ung thư, do khối u ác tính gây ra. Chữ 癌 đọc là ái, Hán Việt là nham. Các loại ung thư đều có chữ này: 胃癌，肺癌，乳腺癌. Động từ đi kèm là 患, mắc: 患癌症."),
    ("诊疗", "zhěnliáo", "chẩn liệu", "động từ", "chẩn đoán và điều trị, khám chữa bệnh", "这家医院提供免费诊疗服务。", "Bệnh viện này cung cấp dịch vụ khám chữa bệnh miễn phí.",
     "Động từ, nghĩa là chẩn đoán và điều trị. 诊 là chẩn, khám; 疗 là liệu, chữa, như trong trị liệu. Hay gặp 诊疗室，诊疗方案, tức là phòng khám và phác đồ điều trị. Đây là từ xuất hiện nhiều nhất trong bài."),
    ("确诊", "quèzhěn", "xác chẩn", "động từ", "chẩn đoán xác định", "经过检查，他被确诊为肺炎。", "Sau khi kiểm tra, anh ấy được chẩn đoán xác định là viêm phổi.",
     "Động từ, nghĩa là đưa ra chẩn đoán chính xác, khẳng định. Mẫu hay gặp: 被确诊为 cộng tên bệnh. Thời dịch bệnh, các bạn hẳn đã nghe nhiều cụm 确诊病例, ca bệnh xác nhận."),
    ("罕见", "hǎnjiàn", "hãn kiến", "tính từ", "hiếm thấy, hiếm có", "这是一种罕见的疾病。", "Đây là một căn bệnh hiếm gặp.",
     "Tính từ, nghĩa là hiếm thấy. 罕 là hiếm, như trong 罕有. Hay gặp 罕见的奇迹, kỳ tích hiếm có; 世间罕见, hiếm có trên đời."),
    ("白血病", "báixuèbìng", "bạch huyết bệnh", "danh từ", "bệnh bạch cầu, ung thư máu", "白血病俗称血癌。", "Bệnh bạch cầu thường được gọi là ung thư máu.",
     "Danh từ, nghĩa là bệnh bạch cầu, tức ung thư máu. Chữ 血 ở đây đọc là xuè. Cẩn thận: tiếng Việt bạch huyết là chất lympho, như hệ bạch huyết; còn 白血病 là bệnh bạch cầu."),
    ("精准", "jīngzhǔn", "tinh chuẩn", "tính từ", "chính xác cao, chuẩn xác", "这款手机可以精准定位。", "Chiếc điện thoại này có thể định vị chính xác.",
     "Tính từ, nghĩa là cực kỳ chính xác. Hay gặp 精准判断，精准定位. Ở bài trước có quảng cáo 精准推送; còn bài này nói 诊疗的速度与精准."),
    ("权威", "quánwēi", "quyền uy", "danh từ", "người, tổ chức có uy tín nhất; chuyên gia đầu ngành", "他是心脏病方面的权威。", "Ông ấy là chuyên gia đầu ngành về bệnh tim.",
     "Danh từ, nghĩa là người hoặc tổ chức có uy tín, địa vị cao nhất trong một lĩnh vực, như 医学权威，学术权威. Cũng làm tính từ, nghĩa là có uy tín: 权威医院，权威杂志."),
    ("甚为", "shènwéi", "thậm vi", "phó từ", "rất, hết sức", "大家对这个结果甚为满意。", "Mọi người hết sức hài lòng với kết quả này.",
     "Phó từ, văn viết, nghĩa là rất, hết sức, chỉ mức độ khá cao. Chữ 甚 là thậm, như trong thậm chí; chữ thứ hai đọc thanh hai. Đây là mẫu câu trọng điểm đầu tiên."),
    ("惊叹", "jīngtàn", "kinh thán", "động từ", "kinh ngạc và thán phục", "他的表演令人惊叹。", "Màn biểu diễn của anh ấy khiến người ta kinh ngạc thán phục.",
     "Động từ, nghĩa là vừa kinh ngạc vừa khen ngợi. Hay gặp 令人惊叹，惊叹不已, tức là khiến người ta thán phục, và thán phục không thôi."),
    ("出诊", "chūzhěn", "xuất chẩn", "động từ", "khám bệnh (cho bệnh nhân)", "王医生每周二上午出诊。", "Bác sĩ Vương khám bệnh vào sáng thứ ba hằng tuần.",
     "Động từ. Sách giải thích là bác sĩ khám bệnh cho bệnh nhân ở bệnh viện hay phòng khám. Từ này cũng thường chỉ việc bác sĩ đến tận nhà khám bệnh. Trong bài, robot Watson lần đầu 出诊 ở Trung Quốc."),
    ("资深", "zīshēn", "tư thâm", "tính từ", "lâu năm, kỳ cựu, giàu kinh nghiệm", "她是一位资深记者。", "Bà ấy là một nhà báo kỳ cựu.",
     "Tính từ, nghĩa là từng trải, thâm niên lâu năm. 资 là tư cách, thâm niên; 深 là sâu. Hay gặp 资深主持人，资深经理. Trong bài, 资深人类主任医生 là các bác sĩ trưởng khoa kỳ cựu."),
    ("得力", "délì", "đắc lực", "tính từ", "đắc lực, giỏi giang", "小王是经理的得力助手。", "Tiểu Vương là trợ thủ đắc lực của giám đốc.",
     "Tính từ, nghĩa là giỏi giang, làm việc được việc, âm Hán Việt và nghĩa giống hệt tiếng Việt. Hay gặp nhất là 得力助手, trợ thủ đắc lực."),
    ("肿瘤", "zhǒngliú", "thũng lựu", "danh từ", "khối u", "医生说他的肿瘤是良性的。", "Bác sĩ nói khối u của anh ấy là lành tính.",
     "Danh từ, nghĩa là khối u, do tế bào tăng sinh bất thường lâu ngày tạo thành, khẩu ngữ gọi là 瘤子. Có 良性肿瘤, u lành tính, và 恶性肿瘤, u ác tính. 肿瘤科 là khoa ung bướu."),
    ("心胸", "xīnxiōng", "tâm hung", "danh từ", "ngực và tim; tấm lòng, lòng dạ", "他心胸宽广，从不计较小事。", "Anh ấy có tấm lòng rộng lượng, không bao giờ chấp nhặt chuyện nhỏ.",
     "Danh từ, nghĩa đen là lồng ngực và tim, như 心胸外科, khoa phẫu thuật tim lồng ngực trong bài. Nghĩa bóng hay gặp hơn là tấm lòng, độ lượng: 心胸宽广, rộng lượng; 心胸狭窄, hẹp hòi."),
    ("科室", "kēshì", "khoa thất", "danh từ", "các khoa, phòng", "医院一共有二十多个科室。", "Bệnh viện có tổng cộng hơn hai mươi khoa phòng.",
     "Danh từ, nghĩa là tên gọi chung các khoa, các phòng trong một cơ quan, xí nghiệp hay bệnh viện. Trong bài, 肿瘤科，普外科，心胸外科 đều là các 科室."),
    ("从医", "cóngyī", "tòng y", "động từ", "làm nghề y, hành nghề y", "他从医三十年，救了无数病人。", "Ông ấy hành nghề y ba mươi năm, cứu vô số bệnh nhân.",
     "Động từ, nghĩa là theo nghề y. Chữ 从 là tòng, theo, như trong tòng quân. Tương tự có 从商，从政，从教, tức là kinh doanh, làm chính trị, và dạy học."),
    ("生涯", "shēngyá", "sinh nhai", "danh từ", "sự nghiệp, quãng đời làm một nghề", "他的运动生涯只有短短五年。", "Sự nghiệp thể thao của anh ấy chỉ vỏn vẹn năm năm.",
     "Danh từ, nghĩa là quãng đời làm một nghề, một hoạt động nào đó. Từ dễ nhầm: tiếng Việt sinh nhai là kiếm sống; còn 生涯 là sự nghiệp, như 学术生涯，运动生涯. Trong bài, 从医生涯 là sự nghiệp làm nghề y."),
    ("破天荒", "pòtiānhuāng", "phá thiên hoang", "tính từ", "chưa từng có, lần đầu tiên xuất hiện", "他破天荒地给妈妈做了一顿饭。", "Lần đầu tiên trong đời anh ấy nấu cho mẹ một bữa cơm.",
     "Cụm từ cố định, nghĩa là sự việc lần đầu tiên xuất hiện, xưa nay chưa từng có. Thường làm định ngữ, như 破天荒的经历, hoặc trạng ngữ với 地: 破天荒地."),
    ("局部", "júbù", "cục bộ", "danh từ", "cục bộ, một phần", "明天局部地区有阵雨。", "Ngày mai một số nơi có mưa rào.",
     "Danh từ, nghĩa là một phần của tổng thể, trái nghĩa với 整体 hoặc 全局. Hay gặp 局部麻醉, gây tê cục bộ. Trong bài, 胃癌局部晚期 là ung thư dạ dày giai đoạn tiến triển tại chỗ."),
    ("临床", "línchuáng", "lâm sàng", "động từ", "lâm sàng (khám chữa trực tiếp cho bệnh nhân)", "他有二十年的临床经验。", "Ông ấy có hai mươi năm kinh nghiệm lâm sàng.",
     "Động từ, nghĩa đen là đến bên giường bệnh, tức là bác sĩ trực tiếp chẩn đoán, điều trị cho người bệnh. Âm Hán Việt lâm sàng giống hệt tiếng Việt. Hay gặp 临床经验，临床教学."),
    ("病理", "bìnglǐ", "bệnh lý", "danh từ", "bệnh lý", "医生正在分析病人的病理报告。", "Bác sĩ đang phân tích báo cáo bệnh lý của bệnh nhân.",
     "Danh từ, nghĩa là quá trình và nguyên lý phát sinh, phát triển của bệnh tật. Âm Hán Việt giống hệt tiếng Việt. Trong bài, 病理数据 là số liệu bệnh lý."),
    ("庞大", "pángdà", "bàng đại", "tính từ", "đồ sộ, khổng lồ", "这是一个庞大的工程。", "Đây là một công trình đồ sộ.",
     "Tính từ, nghĩa là cực lớn về hình thể, tổ chức hay số lượng, như 庞大的身躯, thân hình khổng lồ; 开支庞大, chi tiêu rất lớn. Trong bài, 庞大的数据库 là cơ sở dữ liệu khổng lồ."),
    ("数据库", "shùjùkù", "số cứ khố", "danh từ", "cơ sở dữ liệu", "图书馆建立了电子数据库。", "Thư viện đã xây dựng cơ sở dữ liệu điện tử.",
     "Danh từ, dịch từ tiếng Anh database. 数据 là dữ liệu, 库 là kho. Tiếng Việt gọi là cơ sở dữ liệu."),
    ("翻阅", "fānyuè", "phiên duyệt", "động từ", "lật xem, giở xem, tra cứu", "他翻阅了大量历史资料。", "Anh ấy đã lật xem rất nhiều tư liệu lịch sử.",
     "Động từ, nghĩa là lật giở xem sách vở, tài liệu. 翻 là lật, 阅 là đọc, như trong 阅读. Trong bài, Watson 翻阅 tạp chí, sách giáo khoa chỉ trong mấy giây."),
    ("顺便", "shùnbiàn", "thuận tiện", "phó từ", "tiện thể, nhân tiện", "你去超市的时候，顺便帮我买瓶水。", "Lúc cậu đi siêu thị, tiện thể mua giúp tớ chai nước.",
     "Phó từ, nghĩa là nhân lúc làm việc này thì làm luôn việc khác. Từ dễ nhầm: tiếng Việt thuận tiện là tiện lợi, tiếng Trung là 方便; còn 顺便 là tiện thể. Đây là mẫu câu trọng điểm thứ hai."),
    ("化疗", "huàliáo", "hóa liệu", "danh từ", "hóa trị", "化疗以后，他的头发都掉光了。", "Sau khi hóa trị, tóc anh ấy rụng hết.",
     "Danh từ, viết tắt của 化学治疗, điều trị bằng thuốc hóa học, tức là hóa trị. Tương tự, xạ trị là 放疗."),
    ("赞许", "zànxǔ", "tán hứa", "động từ", "khen ngợi, tán thưởng", "老师赞许地点了点头。", "Thầy giáo gật đầu tán thưởng.",
     "Động từ, nghĩa là khen là làm tốt, đồng tình. Trái nghĩa là 责怪 hoặc 批评. Trong bài, 赞许地点了点头 là gật đầu tán thưởng, câu y hệt ví dụ."),
    ("闪烁", "shǎnshuò", "thiểm thước", "động từ", "lấp lánh, nhấp nháy", "夜空中群星闪烁。", "Trên bầu trời đêm, muôn sao lấp lánh.",
     "Động từ, nghĩa là ánh sáng lúc sáng lúc tối, lấp lánh, nhấp nháy, như 闪烁的灯光, ánh đèn nhấp nháy. Nghĩa bóng là nói năng úp mở: 闪烁其词."),
    ("条目", "tiáomù", "điều mục", "danh từ", "điều mục, mục", "合同里的每个条目都要看清楚。", "Mỗi điều mục trong hợp đồng đều phải đọc cho rõ.",
     "Danh từ, nghĩa là từng mục cụ thể chia theo nội dung, như 合同条目, điều khoản hợp đồng. Trong bài, 闪烁着绿色的条目 là mục màu xanh lá đang nhấp nháy."),
    ("文献", "wénxiàn", "văn hiến", "danh từ", "tài liệu, văn liệu", "写论文需要查阅大量文献。", "Viết luận văn cần tra cứu rất nhiều tài liệu.",
     "Danh từ, nghĩa là sách vở, tài liệu có giá trị lịch sử hay giá trị tham khảo. Từ dễ nhầm: tiếng Việt văn hiến là truyền thống văn hóa, như nền văn hiến; còn 文献 là tài liệu. 参考文献 là tài liệu tham khảo."),
    ("标示", "biāoshì", "tiêu thị", "động từ", "ghi rõ, đánh dấu", "地图上用红色标示危险区域。", "Trên bản đồ dùng màu đỏ để đánh dấu vùng nguy hiểm.",
     "Động từ, nghĩa là ghi rõ, biểu thị bằng ký hiệu. Trong bài, Watson 标示出了橙色和红色的部分, đánh dấu những phần màu cam và màu đỏ."),
    ("谨慎", "jǐnshèn", "cẩn thận", "tính từ", "thận trọng", "投资一定要谨慎。", "Đầu tư nhất định phải thận trọng.",
     "Tính từ, nghĩa là thận trọng trong lời nói việc làm. Chú ý: âm Hán Việt là cẩn thận, nhưng cẩn thận hằng ngày tiếng Trung thường nói 小心; còn 谨慎 trang trọng hơn, nghĩa là thận trọng. Hay gặp 谨慎处理，保持谨慎，谨慎使用."),
    ("推荐", "tuījiàn", "suy tiến", "động từ", "giới thiệu, đề cử, khuyến nghị", "老师向我们推荐了几本好书。", "Thầy giới thiệu cho chúng tôi mấy cuốn sách hay.",
     "Động từ, nghĩa là giới thiệu người hay vật tốt để được dùng, được nhận, như 推荐信, thư giới thiệu. Trong bài, 不推荐使用 là không khuyến nghị dùng."),
    ("评定", "píngdìng", "bình định", "động từ", "đánh giá, xét duyệt và quyết định", "他今年被评定为高级工程师。", "Năm nay anh ấy được xét công nhận là kỹ sư cao cấp.",
     "Động từ, nghĩa là qua bình xét mà quyết định, như 评定职称, xét chức danh; 评定成绩, chấm điểm. Từ dễ nhầm: tiếng Việt bình định là dẹp yên; còn 评定 là đánh giá. Trong bài, 执业医师资格评定考试 là kỳ thi sát hạch chứng chỉ hành nghề bác sĩ."),
    ("记忆力", "jìyìlì", "ký ức lực", "danh từ", "trí nhớ, khả năng ghi nhớ", "老人的记忆力越来越差了。", "Trí nhớ của ông cụ ngày càng kém.",
     "Danh từ, nghĩa là khả năng ghi nhớ. 记忆 là ký ức, ghi nhớ; 力 là sức. Hay gặp 记忆力好，记忆力差, và trong bài là 超强的记忆力, trí nhớ siêu phàm."),
    ("倾力", "qīnglì", "khuynh lực", "động từ", "dốc toàn lực, dốc hết sức", "感谢大家的倾力相助。", "Cảm ơn mọi người đã dốc sức giúp đỡ.",
     "Động từ, văn viết, nghĩa là dốc hết sức lực. 倾 là nghiêng, đổ hết ra, như 倾盆大雨, mưa như trút nước. Hay gặp 倾力相助，倾力打造."),
    ("打造", "dǎzào", "đả tạo", "động từ", "xây dựng, tạo dựng, tạo ra", "这座城市正在打造旅游品牌。", "Thành phố này đang xây dựng thương hiệu du lịch.",
     "Động từ, nghĩa gốc là rèn đúc đồ kim loại; nay nghĩa là tạo ra, xây dựng, như 打造品牌，打造企业形象，打造优秀人才. Từ này rất hay gặp trên báo chí."),
    ("企及", "qǐjí", "xí cập", "động từ", "mong đạt tới, theo kịp", "他的成就是我们难以企及的。", "Thành tựu của ông ấy là điều chúng ta khó lòng theo kịp.",
     "Động từ, văn viết, nghĩa là mong đạt tới, đuổi kịp. 企 ở đây là kiễng chân trông ngóng, Hán Việt là xí. Gần như chỉ dùng trong cụm 难以企及, khó lòng theo kịp."),
    ("愈发", "yùfā", "dũ phát", "phó từ", "càng thêm, ngày càng", "天气愈发冷了。", "Trời càng lúc càng lạnh.",
     "Phó từ, văn viết, nghĩa là càng, càng thêm, giống 越发 và 更加. Chữ 愈 là dũ, như trong 愈来愈, càng ngày càng. Đây là mẫu câu trọng điểm thứ tám."),
    ("但愿", "dànyuàn", "đãn nguyện", "động từ", "chỉ mong, mong sao", "但愿明天是个好天气。", "Mong sao ngày mai trời đẹp.",
     "Động từ, nghĩa là chỉ mong, chỉ ước, đứng đầu câu biểu thị một mong ước. 但 ở đây là chỉ, 愿 là mong muốn. Trong bài: 但愿这只是杞人忧天, mong sao đây chỉ là lo hão."),
    ("造福", "zàofú", "tạo phúc", "động từ", "mang lại hạnh phúc, mang lại lợi ích", "这项发明将造福全人类。", "Phát minh này sẽ mang lại lợi ích cho toàn nhân loại.",
     "Động từ, nghĩa là tạo ra hạnh phúc cho con cháu, cho nhân dân. Hay gặp 造福人民，造福子孙后代，造福于人类. Đây là mẫu câu trọng điểm cuối cùng."),
]

add("bullets", chapter="Từ mới (44 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 4.2 có 44 từ mới, chia thành 15 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Nhiều từ ngành y: 癌症 · 确诊 · 白血病 · 肿瘤 · 临床 · 病理 · 化疗",
           "Từ dễ nhầm: 白血病 · 生涯 · 顺便 · 文献 · 评定"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có bốn mươi bốn từ, thầy chia thành mười lăm nhóm nhỏ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Bài khóa nói về bệnh viện, nên có nhiều từ ngành y: 癌症，确诊，白血病，肿瘤，临床，病理，化疗. Tin vui là nhiều từ có âm Hán Việt giống hệt tiếng Việt, như lâm sàng, bệnh lý."),
         F(4, "Tuy vậy, cũng có mấy từ Hán Việt rất dễ hiểu nhầm, như 白血病，生涯，顺便，文献，评定. Các bạn nhớ nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

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
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung nếu khác])
P = [
    ("近日，机器人医生沃森第一次在中国患者面前亮相，并为20多位患者做了义诊。沃森医生出生于2015年，年仅2岁。",
     "Mới đây, bác sĩ robot Watson lần đầu tiên ra mắt trước bệnh nhân Trung Quốc, và đã khám bệnh miễn phí cho hơn 20 bệnh nhân. Bác sĩ Watson 'chào đời' năm 2015, mới vỏn vẹn 2 tuổi.",
     ["近日 là mới đây, văn viết. 沃森 là Watson, tên phiên âm của bác sĩ robot. 亮相 là ra mắt. 为二十多位患者做了义诊 là khám miễn phí cho hơn hai mươi bệnh nhân; 患者 là bệnh nhân, văn viết của 病人.",
      "出生于二零一五年 là ra đời năm hai nghìn không trăm mười lăm; 于 là vào, văn viết. 年仅两岁 là mới chỉ hai tuổi. Tác giả nhân cách hóa robot như một con người, rất sinh động."],
     "近日，机器人医生沃森第一次在中国患者面前亮相，并为二十多位患者做了义诊。沃森医生出生于二零一五年，年仅两岁。"),
    ("是拥有更强大脑的癌症专家，在印度，它为一名已经无药可救的癌症晚期患者找到了诊疗方案；在日本，它只花了10分钟就确诊了一例罕见白血病……其诊疗的速度与精准让一众医学权威甚为惊叹！",
     "Nó là chuyên gia ung thư sở hữu 'bộ não' mạnh hơn: ở Ấn Độ, nó tìm ra phác đồ điều trị cho một bệnh nhân ung thư giai đoạn cuối tưởng như hết thuốc chữa; ở Nhật Bản, nó chỉ mất 10 phút để chẩn đoán xác định một ca bệnh bạch cầu hiếm gặp... Tốc độ và độ chính xác trong khám chữa của nó khiến hàng loạt chuyên gia y học đầu ngành hết sức kinh ngạc, thán phục!",
     ["拥有更强大脑 là sở hữu bộ não mạnh hơn. 无药可救 là không còn thuốc nào cứu được, một thành ngữ của bài. 癌症晚期 là ung thư giai đoạn cuối. 诊疗方案 là phác đồ điều trị.",
      "一例罕见白血病 là một ca bệnh bạch cầu hiếm gặp; 例 là lượng từ cho ca bệnh. 其 là của nó. 一众 là cả một loạt, một nhóm đông. 甚为惊叹 là hết sức kinh ngạc thán phục, mẫu câu trọng điểm thứ nhất."],
     "是拥有更强大脑的癌症专家，在印度，它为一名已经无药可救的癌症晚期患者找到了诊疗方案；在日本，它只花了十分钟就确诊了一例罕见白血病，其诊疗的速度与精准让一众医学权威甚为惊叹！"),
    ("这是机器人医生沃森第一次在中国“出诊”，它作为现场5位资深人类主任医生的得力助手，全程参与了诊疗。这些人类医生分别来自肿瘤科、普外科、心胸外科等科室。这在他们的从医生涯中是破天荒的经历。",
     "Đây là lần đầu tiên bác sĩ robot Watson 'khám bệnh' ở Trung Quốc. Với vai trò trợ thủ đắc lực của 5 bác sĩ chủ nhiệm kỳ cựu có mặt tại chỗ, nó tham gia suốt toàn bộ quá trình khám chữa. Các bác sĩ này lần lượt đến từ khoa ung bướu, khoa ngoại tổng quát, khoa phẫu thuật tim lồng ngực... Đây là trải nghiệm chưa từng có trong sự nghiệp hành nghề y của họ.",
     ["作为 là với tư cách là. 主任医生 là bác sĩ chủ nhiệm, chức danh cao nhất của bác sĩ ở Trung Quốc. 得力助手 là trợ thủ đắc lực. 全程参与 là tham gia suốt cả quá trình.",
      "分别来自 là lần lượt đến từ. 普外科 là khoa ngoại tổng quát, viết tắt của 普通外科. 从医生涯 là sự nghiệp làm nghề y. 破天荒的经历 là trải nghiệm xưa nay chưa từng có."],
     "这是机器人医生沃森第一次在中国出诊，它作为现场五位资深人类主任医生的得力助手，全程参与了诊疗。这些人类医生分别来自肿瘤科、普外科、心胸外科等科室。这在他们的从医生涯中是破天荒的经历。"),
    ("一位胃癌局部晚期患者坐到肿瘤科主任吴尘轩面前，递上自己的各种检查单据。有着多年肿瘤临床经验的吴尘轩一边思考，一边把病理数据“讲述”给电脑里的助手沃森，沃森医生“思考”了不到10秒钟，在电脑屏幕上开出了一张详细的西医诊疗方案分析单。",
     "Một bệnh nhân ung thư dạ dày giai đoạn tiến triển ngồi xuống trước mặt trưởng khoa ung bướu Ngô Trần Hiên, đưa ra đủ loại phiếu xét nghiệm của mình. Bác sĩ Ngô, người có nhiều năm kinh nghiệm lâm sàng về ung bướu, vừa suy nghĩ vừa 'kể' số liệu bệnh lý cho trợ lý Watson trong máy tính. Bác sĩ Watson 'suy nghĩ' chưa đầy 10 giây, đã đưa ra trên màn hình một bản phân tích phác đồ điều trị Tây y chi tiết.",
     ["胃癌局部晚期 là ung thư dạ dày giai đoạn tiến triển tại chỗ. 主任 ở đây là trưởng khoa. 递上 là đưa lên, trao cho. 检查单据 là các loại phiếu xét nghiệm, kết quả kiểm tra.",
      "有着多年肿瘤临床经验 là có nhiều năm kinh nghiệm lâm sàng về ung bướu. 讲述 và 思考 được đặt trong ngoặc kép, vì máy tính không thật sự nghe kể hay suy nghĩ. 开出 là kê ra, như 开药方, kê đơn thuốc. 西医 là Tây y, đối lập với 中医."],
     "一位胃癌局部晚期患者坐到肿瘤科主任吴尘轩面前，递上自己的各种检查单据。有着多年肿瘤临床经验的吴尘轩一边思考，一边把病理数据讲述给电脑里的助手沃森，沃森医生思考了不到十秒钟，在电脑屏幕上开出了一张详细的西医诊疗方案分析单。"),
    ("在这不可思议的10秒里，沃森都干了些什么呢？在患者看不见的网络时空里，它跑了趟美国，在庞大的数据库里翻阅了超过300份全球最权威的医学杂志、200余种教科书，以及1500多万页资料中的关键信息。",
     "Trong 10 giây khó tin ấy, Watson đã làm những gì? Trong không gian mạng mà bệnh nhân không nhìn thấy, nó đã 'chạy' một chuyến sang Mỹ, lục tìm trong cơ sở dữ liệu khổng lồ những thông tin then chốt từ hơn 300 tạp chí y học uy tín nhất thế giới, hơn 200 loại sách giáo khoa và hơn 15 triệu trang tài liệu.",
     ["不可思议 là không thể tưởng tượng nổi, thành ngữ gốc nhà Phật. 都干了些什么呢 là đã làm những gì thế; 都 ở đây nhấn mạnh câu hỏi bao quát.",
      "网络时空 là không gian và thời gian trên mạng. 跑了趟美国 là chạy một chuyến sang Mỹ, 趟 là lượng từ cho một chuyến đi. 庞大的数据库 là cơ sở dữ liệu khổng lồ. 两百余种 là hơn hai trăm loại; 余 là hơn, văn viết của 多."],
     "在这不可思议的十秒里，沃森都干了些什么呢？在患者看不见的网络时空里，它跑了趟美国，在庞大的数据库里翻阅了超过三百份全球最权威的医学杂志、两百余种教科书，以及一千五百多万页资料中的关键信息。"),
    ("在返回中国这位患者身边之前，它又顺便把自己的诊疗方案部分内容翻译成了中文。",
     "Trước khi quay về bên bệnh nhân Trung Quốc này, nó còn tiện thể dịch một phần phác đồ điều trị của mình sang tiếng Trung.",
     ["在返回之前 là trước khi quay về. 又 ở đây là còn, thêm nữa. 顺便 là tiện thể, mẫu câu trọng điểm thứ hai.",
      "把自己的诊疗方案部分内容翻译成了中文 là câu chữ 把 với bổ ngữ kết quả 成: dịch một phần phác đồ sang tiếng Trung. Watson vốn được phát triển bằng tiếng Anh."]),
    ("“通过化疗将肿瘤缩小后再进行手术。”吴尘轩赞许地点了点头，指着电脑屏幕上的分析单上闪烁着绿色的条目说，“这是沃森提供给医生参考的最佳诊疗方案，跟我的判断完全一致。”这真是“英雄所见略同”！",
     "'Hóa trị để thu nhỏ khối u rồi mới phẫu thuật.' Bác sĩ Ngô gật đầu tán thưởng, chỉ vào mục màu xanh lá đang nhấp nháy trên bản phân tích trên màn hình mà nói: 'Đây là phác đồ điều trị tốt nhất mà Watson đưa ra để bác sĩ tham khảo, hoàn toàn trùng khớp với nhận định của tôi.' Đúng là 'anh hùng gặp nhau, ý kiến tương đồng'!",
     ["通过化疗将肿瘤缩小 là thông qua hóa trị làm khối u nhỏ lại; 将 ở đây là văn viết của 把. 再进行手术 là rồi mới tiến hành phẫu thuật. 赞许地点了点头 là gật đầu tán thưởng.",
      "闪烁着绿色的条目 là mục màu xanh lá đang nhấp nháy. 完全一致 là hoàn toàn trùng khớp. 英雄所见略同 là anh hùng nhìn nhận gần giống nhau, câu khen khi hai người cùng ý kiến; ở đây khen cả bác sĩ lẫn robot."]),
    ("神奇的是，吴尘轩依据的是自己多年临床诊断的经验，而沃森依据的是目前全球范围内对相关病例的大数据分析。",
     "Điều kỳ diệu là, bác sĩ Ngô dựa vào kinh nghiệm chẩn đoán lâm sàng nhiều năm của bản thân, còn Watson dựa vào việc phân tích dữ liệu lớn về các ca bệnh liên quan trên phạm vi toàn cầu hiện nay.",
     ["神奇的是 là điều thần kỳ là, cấu trúc tính từ cộng 的是 đứng đầu câu. 依据 là căn cứ, dựa vào.",
      "Câu dùng mẫu A依据的是什么，而B依据的是什么 để so sánh: một bên là kinh nghiệm con người, một bên là dữ liệu lớn, nhưng kết quả lại trùng khớp. 病例 là ca bệnh."]),
    ("与此同时，沃森还列出了详细的用药、治疗建议、参考文献全文等。也就是说，针对这个患者的具体情况，如何服药，效果怎样，风险多高，沃森都已经进行了精准评估。",
     "Đồng thời, Watson còn liệt kê chi tiết cách dùng thuốc, đề xuất điều trị, toàn văn tài liệu tham khảo... Nói cách khác, với tình trạng cụ thể của bệnh nhân này, uống thuốc thế nào, hiệu quả ra sao, rủi ro cao đến đâu, Watson đều đã đánh giá chính xác.",
     ["与此同时 là cùng lúc đó, đồng thời, mẫu câu trọng điểm thứ ba. 列出 là liệt kê ra. 参考文献全文 là toàn văn tài liệu tham khảo.",
      "也就是说 là nói cách khác, tức là, mẫu câu thứ tư, dùng để giải thích rõ hơn ý phía trước. 针对 là nhằm vào. 服药 là uống thuốc, văn viết. 精准评估 là đánh giá chính xác."]),
    ("短短两个小时，在沃森医生的神助力下，20多位患有胃癌、肺癌、直肠癌、结肠癌、乳腺癌和宫颈癌的患者获得了诊疗方案。",
     "Chỉ vỏn vẹn hai tiếng đồng hồ, nhờ sự 'trợ giúp thần sầu' của bác sĩ Watson, hơn 20 bệnh nhân mắc ung thư dạ dày, ung thư phổi, ung thư trực tràng, ung thư đại tràng, ung thư vú và ung thư cổ tử cung đã nhận được phác đồ điều trị.",
     ["短短两个小时 là chỉ vỏn vẹn hai tiếng, mẫu câu thứ năm. 在什么的神助力下 là nhờ sự trợ giúp thần sầu của ai: sách chú thích, 神助力 là từ lóng trên mạng, giống 神助攻, nghĩa là giúp người khác làm được việc vốn rất khó.",
      "患有 là mắc bệnh. Các loại ung thư: 胃癌 dạ dày, 肺癌 phổi, 直肠癌 trực tràng, 结肠癌 đại tràng, 乳腺癌 vú, 宫颈癌 cổ tử cung. Âm Hán Việt của 直肠，结肠 là trực trường, kết trường."],
     "短短两个小时，在沃森医生的神助力下，二十多位患有胃癌、肺癌、直肠癌、结肠癌、乳腺癌和宫颈癌的患者获得了诊疗方案。"),
    ("与人类医生相比，沃森的反应之快令人惊叹，“大大提高了诊疗效率。”吴尘轩说，沃森的分析单中还同时标示出了橙色和红色的部分，分别代表谨慎使用和不推荐使用，“甚至能比人类医生考虑得更全面更细致，把风险降到了最低。”",
     "So với bác sĩ con người, tốc độ phản ứng của Watson nhanh đến kinh ngạc. 'Hiệu quả khám chữa được nâng cao rất nhiều', bác sĩ Ngô nói. Trong bản phân tích của Watson còn đánh dấu những phần màu cam và màu đỏ, lần lượt có nghĩa là thận trọng khi dùng và không khuyến nghị dùng. 'Nó thậm chí còn cân nhắc toàn diện, tỉ mỉ hơn cả bác sĩ con người, giảm rủi ro xuống mức thấp nhất.'",
     ["与人类医生相比 là so với bác sĩ con người. 反应之快 là sự nhanh nhạy trong phản ứng: mẫu danh từ cộng 之 cộng tính từ, mẫu câu trọng điểm thứ sáu. 大大提高 là nâng cao rất nhiều.",
      "标示出了橙色和红色的部分 là đánh dấu phần màu cam và màu đỏ. 分别代表 là lần lượt đại diện cho. 谨慎使用 là dùng thận trọng, 不推荐使用 là không khuyến nghị dùng. 把风险降到了最低 là giảm rủi ro xuống thấp nhất."]),
    ("事实上，这个没有生命却有着“最强大脑”的人工智能医生，是由IBM公司开发，并与美国癌症治疗领域的权威医院——纪念斯隆-凯特琳癌症中心共同倾力打造出来的，目前，在美国已通过执业医师资格评定考试，是目前国际上癌症治疗领域最先进的机器人。",
     "Thực ra, vị bác sĩ trí tuệ nhân tạo không có sự sống nhưng sở hữu 'bộ não mạnh nhất' này do công ty IBM phát triển, cùng với bệnh viện đầu ngành về điều trị ung thư của Mỹ là Trung tâm Ung thư Memorial Sloan Kettering dốc sức tạo nên. Hiện nay ở Mỹ, nó đã vượt qua kỳ thi sát hạch chứng chỉ hành nghề bác sĩ, là robot tiên tiến nhất thế giới hiện nay trong lĩnh vực điều trị ung thư.",
     ["没有生命却有着最强大脑 là không có sự sống nhưng có bộ não mạnh nhất: sách chú thích, 最强大脑 vốn là tên một chương trình truyền hình thi trí nhớ nổi tiếng của Trung Quốc. 是由什么开发 là do ai phát triển.",
      "纪念斯隆凯特琳癌症中心 là Trung tâm Ung thư Memorial Sloan Kettering ở New York. 倾力打造 là dốc toàn lực tạo dựng. 执业医师资格评定考试 là kỳ thi sát hạch chứng chỉ hành nghề bác sĩ, ở Mỹ gọi là USMLE."],
     "事实上，这个没有生命却有着最强大脑的人工智能医生，是由IBM公司开发，并与美国癌症治疗领域的权威医院，纪念斯隆凯特琳癌症中心共同倾力打造出来的，目前，在美国已通过执业医师资格评定考试，是目前国际上癌症治疗领域最先进的机器人。"),
    ("它们比医生还医生，有着人类大脑难以企及的学习与决策能力，其超强的记忆力和超快的反应速度，对于任何一个人类医生来说，几乎都是望尘莫及的。",
     "Chúng còn 'bác sĩ hơn cả bác sĩ', có năng lực học tập và ra quyết định mà bộ não con người khó lòng theo kịp. Trí nhớ siêu phàm và tốc độ phản ứng siêu nhanh của chúng, đối với bất kỳ bác sĩ con người nào, gần như đều là điều chỉ biết nhìn theo mà không sao đuổi kịp.",
     ["比医生还医生 là còn bác sĩ hơn cả bác sĩ: mẫu 比N还N, mẫu câu trọng điểm thứ bảy. 难以企及 là khó lòng theo kịp. 决策 là ra quyết sách, ra quyết định.",
      "对于什么来说 là đối với ai mà nói. 望尘莫及 là thành ngữ: nhìn bụi xe ngựa người đi trước mà không đuổi kịp, tức là bị bỏ xa, không sao theo kịp. Thành ngữ này sẽ xuất hiện trong bài tập một."]),
    ("随着科学技术的不断突破，沃森医生的“大脑”将愈发强大，有人担心人类医生最终会被他取而代之。但愿这只是“杞人忧天”，毕竟最先进的技术是由人类发明并造福于人类的。",
     "Cùng với những đột phá không ngừng của khoa học kỹ thuật, 'bộ não' của bác sĩ Watson sẽ ngày càng mạnh mẽ, có người lo rằng bác sĩ con người rốt cuộc sẽ bị nó thay thế. Mong sao đây chỉ là 'lo trời sập', dù sao thì công nghệ tiên tiến nhất cũng là do con người phát minh ra và để mang lại hạnh phúc cho chính con người.",
     ["随着 là cùng với. 不断突破 là đột phá không ngừng. 愈发强大 là ngày càng mạnh mẽ, mẫu câu thứ tám. 被他取而代之 là bị nó thay thế; 取而代之 là gạt đi mà thế chỗ.",
      "但愿 là mong sao. 杞人忧天 là người nước Kỷ lo trời sập, tức là lo hão. 毕竟 là dù sao thì, rốt cuộc thì. 造福于人类 là mang lại hạnh phúc cho nhân loại, mẫu câu cuối cùng. Bài kết thúc bằng một thái độ lạc quan."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 机器人医生，简直神了！", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Bài là một bản tin: chú ý các con số và cách tường thuật",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa. Bài được cải biên từ bản tin đăng trên 中国青年报, báo Thanh niên Trung Quốc, ngày mười tháng hai năm hai nghìn không trăm mười bảy, tác giả là 胡春艳.",
         F(0, f"Thầy chia bài thành {len(P)} đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Đây là một bản tin, nên có rất nhiều con số: hai tuổi, mười phút, mười giây, ba trăm tạp chí, hơn mười lăm triệu trang tài liệu. Các bạn chú ý cách đọc số trong tiếng Trung nhé."),
         F(3, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh
    spoken = spoken.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 100 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Đọc hiểu", section="Bài khóa 课文", title="Kiểm tra đọc hiểu: đúng hay sai?", reveal=True, size=34,
    items=["(1) 沃森是在美国第一次为患者做义诊的。",
           "Đáp án: Sai. 沃森是第一次在中国患者面前亮相，在中国“出诊”。",
           "(2) 沃森医生只用了不到10秒钟，就开出了一张诊疗方案分析单。",
           "Đáp án: Đúng.",
           "(3) 吴尘轩和沃森依据的都是多年的临床经验。",
           "Đáp án: Sai. 吴尘轩依据临床经验，沃森依据全球病例的大数据分析。",
           "(4) 分析单上的红色部分表示不推荐使用。",
           "Đáp án: Đúng. 橙色代表谨慎使用，红色代表不推荐使用。",
           "(5) 作者认为人类医生一定会被机器人取而代之。",
           "Đáp án: Sai. 作者希望这只是“杞人忧天”，技术是造福于人类的。"],
    say=["Trước khi sang phần mẫu câu, chúng ta kiểm tra nhanh xem các bạn đã hiểu bài khóa chưa. Thầy đọc năm câu, các bạn phán đoán đúng hay sai nhé.",
         F(0, "Câu một: 沃森是在美国第一次为患者做义诊的。 Watson lần đầu khám miễn phí cho bệnh nhân là ở Mỹ. Đúng hay sai?"),
         F(1, "Sai. Bài khóa nói đây là lần đầu Watson ra mắt bệnh nhân Trung Quốc, lần đầu 出诊 ở Trung Quốc; ở Mỹ thì nó đã được dùng từ trước."),
         F(2, "Câu hai: 沃森医生只用了不到十秒钟，就开出了一张诊疗方案分析单。 Bác sĩ Watson chỉ mất chưa đầy mười giây đã đưa ra bản phân tích phác đồ điều trị."),
         F(3, "Đúng. Bài khóa viết: 思考了不到十秒钟."),
         F(4, "Câu ba: 吴尘轩和沃森依据的都是多年的临床经验。 Bác sĩ Ngô và Watson đều dựa vào kinh nghiệm lâm sàng nhiều năm."),
         F(5, "Sai. Bác sĩ Ngô dựa vào kinh nghiệm lâm sàng, còn Watson dựa vào phân tích dữ liệu lớn về các ca bệnh trên toàn cầu. Hai con đường khác nhau mà kết quả lại trùng khớp."),
         F(6, "Câu bốn: 分析单上的红色部分表示不推荐使用。 Phần màu đỏ trên bản phân tích có nghĩa là không khuyến nghị dùng."),
         F(7, "Đúng. Màu cam là thận trọng khi dùng, màu đỏ là không khuyến nghị dùng; còn màu xanh lá là phác đồ tốt nhất."),
         F(8, "Câu năm: 作者认为人类医生一定会被机器人取而代之。 Tác giả cho rằng bác sĩ con người nhất định sẽ bị robot thay thế."),
         F(9, "Sai. Tác giả mong rằng nỗi lo ấy chỉ là 杞人忧天, lo hão, vì công nghệ là do con người tạo ra để phục vụ con người.")])

add("bullets", chapter="Chú thích & bố cục", section="Bài khóa 课文", title="Chú thích (注释) và bố cục bản tin", size=33,
    items=["## Chú thích",
           "执业医师资格评定考试: kỳ thi cấp chứng chỉ hành nghề bác sĩ – “giấy thông hành” để hành nghề (Mỹ: USMLE, 3 bước)",
           "神助力: từ lóng trên mạng, như 神助攻 (助攻 = kiến tạo trong bóng rổ) – giúp người khác làm được việc rất khó",
           "最强大脑: tên chương trình truyền hình 《最强大脑》 (2014, Giang Tô) – ví Watson có trí não siêu phàm",
           "## Bố cục bản tin",
           "Sự kiện (Watson khám bệnh ở Trung Quốc) → diễn biến (10 giây, phác đồ trùng khớp) → so sánh người và máy → lai lịch Watson → nỗi lo và thái độ lạc quan"],
    say=["Đọc xong bài khóa, chúng ta xem lại phần chú thích của sách, và bố cục của bản tin.",
         F(1, "Chú thích một: 执业医师资格评定考试, kỳ thi sát hạch chứng chỉ hành nghề bác sĩ. Đây là kỳ thi đầu vào của ngành, đỗ rồi mới được đăng ký hành nghề, nên chứng chỉ này được ví như giấy thông hành của bác sĩ. Ở Mỹ, kỳ thi này gọi là USMLE, gồm ba bước."),
         F(2, "Chú thích hai: 神助力, từ lóng trên mạng, giống 神助攻. 助攻 vốn là pha kiến tạo trong bóng rổ, giúp đồng đội ghi điểm; nay chỉ sự giúp đỡ cực lớn trong đời sống."),
         F(3, "Chú thích ba: 最强大脑 là tên một chương trình truyền hình thực tế thi trí não, do đài truyền hình Giang Tô mua bản quyền từ chương trình Super Brain của Đức năm hai nghìn không trăm mười bốn. Bài khóa dùng tên này để nói Watson có trí não siêu phàm như các thí sinh."),
         F(5, "Về bố cục, bản tin đi theo trình tự: nêu sự kiện, Watson khám bệnh ở Trung Quốc; kể diễn biến, mười giây và phác đồ trùng khớp; so sánh người và máy; giới thiệu lai lịch của Watson; và cuối cùng là nỗi lo bị thay thế, cùng thái độ lạc quan của tác giả.")])

# ======================= MẪU CÂU TRỌNG ĐIỂM =======================
add("bullets", chapter="Mẫu câu: 甚为 · 顺便", section="Mẫu câu 重点句型", title="1. 甚为 shènwéi – rất, hết sức (văn viết)", size=36,
    items=["Phó từ, văn viết: chỉ mức độ cao; đứng trước tính từ / động từ hai âm tiết",
           "甚为惊叹 · 甚为复杂 · 甚为缓慢 · 甚为不满 · 甚为热情",
           "(1) 其诊疗的速度与精准让一众医学权威甚为惊叹！",
           "(2) 最初的线上购票系统并不完善，整个过程甚为复杂，十分耗时。",
           "(3) 时逢雨季，工程进展甚为缓慢，房子很可能无法按期交付。"],
    say=["Bây giờ chúng ta sang phần mẫu câu trọng điểm. Sách đưa ra chín mẫu câu.",
         F(0, "Mẫu thứ nhất: 甚为. Đây là phó từ văn viết, nghĩa là rất, hết sức, chỉ mức độ khá cao. Nó thường đứng trước tính từ hoặc động từ hai âm tiết. Trong khẩu ngữ, ta dùng 非常 hoặc 很."),
         F(1, "Hay gặp: 甚为惊叹，甚为复杂，甚为缓慢，甚为不满，甚为热情."),
         F(2, "Ví dụ một, lấy từ bài khóa: 其诊疗的速度与精准让一众医学权威甚为惊叹！ Tốc độ và độ chính xác của nó khiến hàng loạt chuyên gia y học hết sức kinh ngạc thán phục."),
         F(3, "Ví dụ hai: 最初的线上购票系统并不完善，整个过程甚为复杂，十分耗时。 Hệ thống mua vé trực tuyến lúc đầu chưa hoàn thiện, cả quá trình hết sức phức tạp, rất tốn thời gian."),
         F(4, "Ví dụ ba: 时逢雨季，工程进展甚为缓慢，房子很可能无法按期交付。 Đúng vào mùa mưa, công trình tiến triển hết sức chậm, nhà rất có thể không bàn giao đúng hạn. 时逢 là đúng lúc gặp, văn viết.")])

add("bullets", section="Mẫu câu 重点句型", title="2. 顺便 shùnbiàn – tiện thể, nhân tiện", size=36,
    items=["Nhân lúc làm việc A thì làm luôn việc B; 顺便 đứng trước việc B",
           "Cấu trúc: (làm A) …… 顺便 + (把……) + V (việc B)",
           "(1) 在返回中国这位患者身边之前，它又顺便把自己的诊疗方案部分内容翻译成了中文。",
           "(2) 你回来的时候，顺便帮我把快递拿回来吧。",
           "(3) 你定机票的时候，顺便给我也订一张往返机票吧，我想要经济舱。"],
    say=[F(0, "Mẫu thứ hai: 顺便. Nó biểu thị nhân lúc làm việc này, làm luôn việc khác cho tiện. 顺便 đứng trước việc làm thêm. Nhớ nhé, đây không phải thuận tiện, mà là tiện thể."),
         F(1, "Cấu trúc: trước là việc chính, sau là 顺便 cộng việc phụ. Rất hay đi với câu chữ 把, hoặc 帮我, khi nhờ ai làm giúp."),
         F(2, "Ví dụ một, lấy từ bài khóa: 在返回中国这位患者身边之前，它又顺便把自己的诊疗方案部分内容翻译成了中文。 Trước khi về bên bệnh nhân, nó còn tiện thể dịch một phần phác đồ sang tiếng Trung."),
         F(3, "Ví dụ hai: 你回来的时候，顺便帮我把快递拿回来吧。 Lúc cậu về, tiện thể lấy giúp tớ bưu kiện nhé. 快递 là hàng chuyển phát nhanh."),
         F(4, "Ví dụ ba: 你定机票的时候，顺便给我也订一张往返机票吧，我想要经济舱。 Lúc cậu đặt vé máy bay, tiện thể đặt cho tớ một vé khứ hồi nhé, tớ muốn hạng phổ thông. 往返 là khứ hồi, 经济舱 là khoang phổ thông.")])

add("bullets", chapter="Mẫu câu: 与此同时 · 也就是说", section="Mẫu câu 重点句型", title="3. 与此同时 – đồng thời · 4. 也就是说 – nói cách khác", size=33,
    items=["## 与此同时: cùng lúc đó, đồng thời; đứng đầu câu / vế sau, nối thêm một việc xảy ra song song",
           "(1) 与此同时，沃森还列出了详细的用药、治疗建议、参考文献全文等。",
           "(2) 他乐于和中国朋友探讨问题，与此同时，也能提高自己的中文水平。",
           "(3) 上了两年的网课，他的眼睛时常有酸胀的感觉，与此同时他的视力也越来越差。",
           "## 也就是说: từ nối của câu giải thích; nói lại ý trước cho rõ, cụ thể hơn",
           "(1) 也就是说，针对这个患者的具体情况，如何服药，效果怎样，风险多高，沃森都已经进行了精准评估。",
           "(2) 蓝牙的有效传输距离为十米，也就是说，在十米范围内手机可以搜索到其他正在使用蓝牙功能的设备……",
           "(3) 我们要对市场上那些潜在的风险保持警惕，也就是说，投资时不要过分冲动。"],
    say=[F(0, "Mẫu thứ ba: 与此同时. 此 là cái này, việc này: cùng lúc với việc này, tức là đồng thời. Nó đứng đầu câu hoặc đầu vế sau, nối thêm một việc xảy ra song song; vế sau thường có 也 hoặc 还."),
         F(1, "Ví dụ một, lấy từ bài khóa: 与此同时，沃森还列出了详细的用药、治疗建议、参考文献全文等。 Đồng thời, Watson còn liệt kê chi tiết cách dùng thuốc, đề xuất điều trị, toàn văn tài liệu tham khảo."),
         F(2, "Ví dụ hai: 他乐于和中国朋友探讨问题，与此同时，也能提高自己的中文水平。 Anh ấy thích cùng bạn Trung Quốc bàn luận các vấn đề, đồng thời cũng nâng cao được trình độ tiếng Trung. Đây cũng là một lời khuyên hay cho người học tiếng."),
         F(3, "Ví dụ ba: 上了两年的网课，他的眼睛时常有酸胀的感觉，与此同时他的视力也越来越差。 Học trực tuyến hai năm, mắt cậu ấy thường xuyên mỏi nhức, đồng thời thị lực cũng ngày càng kém."),
         F(4, "Mẫu thứ tư: 也就是说. Đây là từ nối của câu phức giải thích. Nó nói lại ý phía trước bằng cách khác, rõ ràng và cụ thể hơn. Tiếng Việt dịch là nói cách khác, tức là."),
         F(5, "Ví dụ một, lấy từ bài khóa: 也就是说，针对这个患者的具体情况，如何服药，效果怎样，风险多高，沃森都已经进行了精准评估。 Nói cách khác, uống thuốc thế nào, hiệu quả ra sao, rủi ro cao đến đâu, Watson đều đã đánh giá chính xác."),
         F(6, "Ví dụ hai: 蓝牙的有效传输距离为十米，也就是说，在十米范围内手机可以搜索到其他正在使用蓝牙功能的设备，并向其发送信息。 Khoảng cách truyền hiệu quả của Bluetooth là mười mét, tức là trong phạm vi mười mét, điện thoại có thể dò thấy các thiết bị khác đang bật Bluetooth và gửi thông tin cho chúng."),
         F(7, "Ví dụ ba: 我们要对市场上那些潜在的风险保持警惕，也就是说，投资时不要过分冲动。 Chúng ta phải cảnh giác với những rủi ro tiềm ẩn trên thị trường, nói cách khác, khi đầu tư đừng quá bốc đồng.")])

add("bullets", chapter="Mẫu câu: 短短 · N之adj · 比N还N", section="Mẫu câu 重点句型", title="5. 短短…… – chỉ vỏn vẹn (thời gian, khoảng cách ngắn)", size=36,
    items=["短短 + số lượng (thời gian / khoảng cách): nhấn mạnh rất ngắn, rất ít",
           "Thường đứng đầu câu; vế sau nêu một kết quả lớn (hoặc một việc rất chậm)",
           "(1) 短短两个小时，在沃森医生的神助力下，20多位……的患者获得了诊疗方案。",
           "(2) 短短几天，活动就吸引了十几万人参与。",
           "(3) 他的脚受伤了，短短一公里，他走了一个小时。"],
    say=[F(0, "Mẫu thứ năm: 短短 cộng một cụm số lượng chỉ thời gian hoặc khoảng cách. Nó nhấn mạnh thời gian, khoảng cách ấy rất ngắn. Tiếng Việt nói là chỉ vỏn vẹn, chỉ trong."),
         F(1, "Thường đứng đầu câu, vế sau nêu một kết quả lớn, khiến người ta bất ngờ. Bài trước cũng có câu 短短数年，我们已经适应了互联网加的生活."),
         F(2, "Ví dụ một, lấy từ bài khóa: 短短两个小时，在沃森医生的神助力下，二十多位患者获得了诊疗方案。 Chỉ vỏn vẹn hai tiếng, hơn hai mươi bệnh nhân đã có phác đồ điều trị."),
         F(3, "Ví dụ hai: 短短几天，活动就吸引了十几万人参与。 Chỉ trong mấy ngày, hoạt động đã thu hút hơn một trăm nghìn người tham gia. Chú ý chữ 就, nhấn mạnh sự nhanh chóng."),
         F(4, "Ví dụ ba: 他的脚受伤了，短短一公里，他走了一个小时。 Chân anh ấy bị thương, chỉ một cây số ngắn ngủi mà đi mất một tiếng. Ở đây 短短 nói về khoảng cách, và vế sau là việc rất chậm.")])

add("bullets", section="Mẫu câu 重点句型", title="6. N + 之 + adj · 7. 比 N 还/更 N", size=33,
    items=["## N + 之 + tính từ: 之 là trợ từ, tạo cụm danh từ (sự … của N), làm chủ ngữ hoặc tân ngữ",
           "(1) 与人类医生相比，沃森的反应之快令人惊叹。",
           "(2) ……这种现象常让我们感叹“世界之大，无奇不有”。",
           "(3) “没有永远的朋友，只有永远的敌人。”现代商业竞争之激烈远远超出我们的想象。",
           "## 比 N 还/更 N: N có một đặc điểm ai cũng biết, A còn thể hiện đặc điểm ấy mạnh hơn",
           "(1) 它们比医生还医生，有着人类大脑难以企及的学习与决策能力。",
           "(2) 他这种行为简直比强盗还强盗！",
           "(3) 他的生活比和尚还和尚，非常简朴。"],
    say=[F(0, "Mẫu thứ sáu: danh từ cộng 之 cộng tính từ. 之 là trợ từ văn viết, giống 的, biến cả cụm thành một cụm danh từ, nghĩa là sự… của cái gì. Cụm này làm chủ ngữ hoặc tân ngữ, và thường nhấn mạnh mức độ."),
         F(1, "Ví dụ một, lấy từ bài khóa: 与人类医生相比，沃森的反应之快令人惊叹。 So với bác sĩ con người, sự nhanh nhạy của Watson khiến người ta kinh ngạc. Cụm 沃森的反应之快 làm chủ ngữ."),
         F(2, "Ví dụ hai: 有些动物天生就具有器官再生能力，这种现象常让我们感叹世界之大，无奇不有。 Có loài động vật bẩm sinh có khả năng tái tạo cơ quan, hiện tượng này khiến ta cảm thán: thế giới rộng lớn, chuyện lạ gì cũng có."),
         F(3, "Ví dụ ba: 没有永远的朋友，只有永远的敌人。现代商业竞争之激烈远远超出我们的想象。 Không có bạn bè vĩnh viễn, chỉ có kẻ thù vĩnh viễn. Sự khốc liệt của cạnh tranh thương mại hiện đại vượt xa sức tưởng tượng của chúng ta."),
         F(4, "Mẫu thứ bảy: 比 N 还 N, hoặc 比 N 更 N. N là một danh từ có đặc điểm mà ai cũng biết, như bác sĩ thì giỏi chữa bệnh, nhà sư thì sống giản dị. Câu này nói A còn mang đặc điểm ấy rõ hơn cả chính N. Lúc này danh từ thứ hai mang chức năng như tính từ."),
         F(5, "Ví dụ một, lấy từ bài khóa: 它们比医生还医生，有着人类大脑难以企及的学习与决策能力。 Chúng còn bác sĩ hơn cả bác sĩ, có năng lực học tập và ra quyết định mà não người khó theo kịp."),
         F(6, "Ví dụ hai: 他这种行为简直比强盗还强盗！ Hành vi này của hắn đúng là còn cướp hơn cả kẻ cướp!"),
         F(7, "Ví dụ ba: 他的生活比和尚还和尚，非常简朴。 Cuộc sống của anh ấy còn thanh đạm hơn cả nhà sư, vô cùng giản dị. 和尚 là nhà sư.")])

add("bullets", chapter="Mẫu câu: 愈发 · 造福", section="Mẫu câu 重点句型", title="8. 愈发 – càng thêm · 9. 造福（于）…… – mang lại hạnh phúc cho", size=33,
    items=["## 愈发 + tính từ / động từ: phó từ, văn viết = 越发、更加; mức độ tăng thêm",
           "(1) 随着科学技术的不断突破，沃森医生的“大脑”将愈发强大……",
           "(2) 经历了重重困难与考验，他愈发坚定了心中的信念。",
           "(3) 看着那一轮明月，诗人愈发想念自己的家乡。",
           "## 造福（于）+ đối tượng: tạo hạnh phúc, mang lại lợi ích cho con cháu, nhân dân",
           "(1) 但愿这只是“杞人忧天”，毕竟最先进的技术是由人类发明并造福于人类的。",
           "(2) 植树造林是一件造福子孙后代的大事。",
           "(3) 一个办教育，一个修水利，都将造福于人民。"],
    say=[F(0, "Mẫu thứ tám: 愈发. Đây là phó từ văn viết, nghĩa giống 越发 và 更加: càng, càng thêm, biểu thị mức độ tăng lên. Thường đứng trước tính từ hoặc động từ chỉ tâm lý."),
         F(1, "Ví dụ một, lấy từ bài khóa: 随着科学技术的不断突破，沃森医生的大脑将愈发强大。 Cùng với đột phá của khoa học kỹ thuật, bộ não của Watson sẽ ngày càng mạnh mẽ."),
         F(2, "Ví dụ hai: 经历了重重困难与考验，他愈发坚定了心中的信念。 Trải qua bao khó khăn thử thách chồng chất, anh ấy càng thêm kiên định niềm tin trong lòng. 重重 ở đây đọc là chóng chóng, nghĩa là chồng chất."),
         F(3, "Ví dụ ba: 看着那一轮明月，诗人愈发想念自己的家乡。 Ngắm vầng trăng sáng, nhà thơ càng thêm nhớ quê hương."),
         F(4, "Mẫu thứ chín: 造福, có thể thêm 于. Nghĩa là tạo ra hạnh phúc, mang lại lợi ích cho một đối tượng, thường là nhân dân, con cháu, nhân loại. 于 ở đây giống 给, văn viết."),
         F(5, "Ví dụ một, câu kết bài khóa: 毕竟最先进的技术是由人类发明并造福于人类的。 Dù sao công nghệ tiên tiến nhất cũng do con người phát minh và để phục vụ con người."),
         F(6, "Ví dụ hai: 植树造林是一件造福子孙后代的大事。 Trồng cây gây rừng là việc lớn mang lại phúc cho con cháu đời sau."),
         F(7, "Ví dụ ba: 一个办教育，一个修水利，都将造福于人民。 Một là làm giáo dục, một là làm thủy lợi, đều sẽ mang lại hạnh phúc cho nhân dân.")])

add("bullets", section="Mẫu câu 重点句型", title="Luyện tập mẫu câu: hoàn thành câu", reveal=True, size=34,
    items=["(1) 这家店的生意___________，每天都排长队。（N之adj）",
           "Đáp án gợi ý: 这家店生意之好，超出了我的想象，每天都排长队。",
           "(2) 他每天都在图书馆学到半夜，___________。（比N还N）",
           "Đáp án gợi ý: 他每天都在图书馆学到半夜，简直比学霸还学霸。",
           "(3) 你去邮局寄信的时候，___________。（顺便）",
           "Đáp án gợi ý: 你去邮局寄信的时候，顺便帮我买几张邮票吧。",
           "(4) 这次会议的气氛___________。（甚为）",
           "Đáp án gợi ý: 这次会议的气氛甚为轻松，大家都畅所欲言。"],
    say=["Bây giờ các bạn thử vận dụng: hoàn thành câu bằng mẫu câu cho sẵn. Đây là bài luyện thêm, thầy đưa ra đáp án gợi ý.",
         F(0, "Câu một, dùng mẫu danh từ cộng 之 cộng tính từ: 这家店的生意什么，每天都排长队。 Việc buôn bán của cửa hàng này thế nào, ngày nào cũng xếp hàng dài."),
         F(1, "Đáp án gợi ý: 这家店生意之好，超出了我的想象，每天都排长队。 Cửa hàng này đắt khách đến mức vượt ngoài sức tưởng tượng của tôi, ngày nào cũng xếp hàng dài."),
         F(2, "Câu hai, dùng 比N还N: 他每天都在图书馆学到半夜，什么。 Ngày nào anh ấy cũng học ở thư viện đến nửa đêm."),
         F(3, "Đáp án gợi ý: 他每天都在图书馆学到半夜，简直比学霸还学霸。 Đúng là còn mọt sách hơn cả mọt sách. 学霸 là từ lóng chỉ học sinh học cực giỏi, cực chăm."),
         F(4, "Câu ba, dùng 顺便: 你去邮局寄信的时候，什么。 Lúc cậu ra bưu điện gửi thư."),
         F(5, "Đáp án gợi ý: 你去邮局寄信的时候，顺便帮我买几张邮票吧。 Lúc cậu ra bưu điện gửi thư, tiện thể mua giúp tớ mấy con tem nhé."),
         F(6, "Câu bốn, dùng 甚为: 这次会议的气氛什么。 Bầu không khí của cuộc họp lần này thế nào."),
         F(7, "Đáp án gợi ý: 这次会议的气氛甚为轻松，大家都畅所欲言。 Bầu không khí cuộc họp lần này hết sức thoải mái, mọi người đều nói hết điều muốn nói. 畅所欲言 là nói thoải mái mọi điều muốn nói.")])

# ======================= KẾT HỢP TỪ =======================
add("bullets", chapter="Kết hợp từ", section="Kết hợp từ 词语搭配", title="Kết hợp từ (1): N + 生涯 · 从 + N · 庞大", size=34,
    items=["## N + 生涯: 教书～ · 舞台～ · 演艺～ · 运动～ · 军旅～",
           "毕业后他参了军，开始了他的军旅生涯。",
           "在近三十年的教学生涯里，王老师一直兢兢业业。",
           "## 从 + N: ～军 · ～医 · ～教 · ～政 · ～商",
           "她从教近半个世纪，可谓是桃李满天下。",
           "## 庞大: 体型～ · 市场～ · 人口数量～ · ～开支 · ～工程",
           "医院信息化是一项庞大、复杂的系统工程，需要各个部门合力完成。"],
    say=["Tiếp theo là phần kết hợp từ, sách có năm nhóm.",
         F(0, "Nhóm một: danh từ cộng 生涯. Hay gặp: 教书生涯，舞台生涯，演艺生涯，运动生涯，军旅生涯. Tức là sự nghiệp dạy học, sự nghiệp sân khấu, sự nghiệp diễn xuất, sự nghiệp thể thao, và cuộc đời binh nghiệp."),
         F(1, "Ví dụ: 毕业后他参了军，开始了他的军旅生涯。 Tốt nghiệp xong anh ấy nhập ngũ, bắt đầu cuộc đời binh nghiệp."),
         F(2, "Và: 在近三十年的教学生涯里，王老师一直兢兢业业。 Trong gần ba mươi năm dạy học, thầy Vương luôn tận tụy, chu đáo. 兢兢业业 là cần mẫn, tận tụy."),
         F(3, "Nhóm hai: 从 cộng danh từ chỉ nghề. Hay gặp: 从军，从医，从教，从政，从商. Tức là tòng quân, làm nghề y, làm nghề giáo, làm chính trị, và kinh doanh."),
         F(4, "Ví dụ: 她从教近半个世纪，可谓是桃李满天下。 Bà ấy dạy học gần nửa thế kỷ, có thể nói học trò khắp thiên hạ. 桃李满天下 là đào mận khắp thiên hạ, ví học trò đông đúc. Sách còn có câu: 他九零年放弃了稳定的工作，决定下海从商, năm chín mươi anh ấy bỏ công việc ổn định, quyết định ra kinh doanh; 下海 là bỏ việc nhà nước ra làm ăn."),
         F(5, "Nhóm ba: 庞大. Hay gặp: 体型庞大，市场庞大，人口数量庞大，庞大开支，庞大工程. Tức là thân hình khổng lồ, thị trường rộng lớn, dân số đông đảo, chi tiêu khổng lồ, và công trình đồ sộ."),
         F(6, "Ví dụ: 医院信息化是一项庞大、复杂的系统工程，需要各个部门合力完成。 Tin học hóa bệnh viện là một công trình hệ thống đồ sộ, phức tạp, cần các bộ phận chung sức hoàn thành.")])

add("bullets", section="Kết hợp từ 词语搭配", title="Kết hợp từ (2): 倾力 + V · 打造 + N", size=35,
    items=["## 倾力 + V: ～打造 · ～相助 · ～支持",
           "市政府正在投巨资倾力打造度假旅游基础设施。",
           "这件事由于有他倾力相助，终于圆满完成。",
           "## 打造 + N: ～精品 · ～品牌 · 重金～ · ～新产品",
           "这件艺术品是数十位艺术家合力打造的精品。",
           "这是我们公司重金打造的新产品。"],
    say=[F(0, "Nhóm bốn: 倾力 cộng động từ. Hay gặp: 倾力打造，倾力相助，倾力支持. Tức là dốc sức tạo dựng, dốc sức giúp đỡ, dốc sức ủng hộ."),
         F(1, "Ví dụ: 市政府正在投巨资倾力打造度假旅游基础设施。 Chính quyền thành phố đang bỏ vốn lớn, dốc sức xây dựng cơ sở hạ tầng du lịch nghỉ dưỡng."),
         F(2, "Và: 这件事由于有他倾力相助，终于圆满完成。 Việc này nhờ có anh ấy dốc sức giúp đỡ, cuối cùng đã hoàn thành tốt đẹp."),
         F(3, "Nhóm năm: 打造 cộng danh từ. Hay gặp: 打造精品，打造品牌，重金打造，打造新产品. Tức là tạo ra sản phẩm tinh hoa, xây dựng thương hiệu, đầu tư lớn để tạo ra, và tạo ra sản phẩm mới."),
         F(4, "Ví dụ: 这件艺术品是数十位艺术家合力打造的精品。 Tác phẩm nghệ thuật này là tinh phẩm do mấy chục nghệ sĩ chung tay tạo nên."),
         F(5, "Và: 这是我们公司重金打造的新产品。 Đây là sản phẩm mới mà công ty chúng tôi đã đầu tư rất nhiều tiền để tạo ra. Các bạn thấy không, trong bài khóa, Watson cũng là do IBM 倾力打造.")])

# ======================= THÀNH NGỮ =======================
add("bullets", chapter="Thành ngữ (6 câu)", section="Thành ngữ 成语", title="Thành ngữ (1)", size=34,
    items=["## 无药可救 wúyàokějiù – hết thuốc chữa; không còn cứu vãn được",
           "这种病目前还无药可救，完全治愈，可以说希望渺茫。",
           "## 破天荒 pòtiānhuāng – lần đầu tiên, xưa nay chưa từng có",
           "看到我的录取通知书，从不喝酒的父亲破天荒地喝了一杯。",
           "## 不可思议 bùkě-sīyì – không thể tưởng tượng nổi, khó tin",
           "古埃及人到底是用什么方法建筑起金字塔的，至今仍让人觉得不可思议。"],
    say=["Bài này có sáu thành ngữ. Mỗi câu, thầy giải thích nghĩa và đọc một ví dụ ngoài bài khóa.",
         F(0, "Câu thứ nhất: 无药可救, không có thuốc nào cứu chữa được; nghĩa bóng là đã đến mức không thể cứu vãn. Trong bài: 一名已经无药可救的癌症晚期患者."),
         F(1, "Ví dụ: 这种病目前还无药可救，完全治愈，可以说希望渺茫。 Bệnh này hiện vẫn chưa có thuốc chữa, khỏi hoàn toàn thì có thể nói là hy vọng mong manh. Từ 渺茫 các bạn vừa gặp trong bài tập bài trước."),
         F(2, "Câu thứ hai: 破天荒. Tương truyền thời Đường, vùng Kinh Châu không có ai đỗ tiến sĩ, bị gọi là 天荒, đất hoang của trời; đến khi có người đỗ, gọi là 破天荒, phá được đất hoang. Nghĩa là lần đầu tiên xuất hiện, xưa nay chưa từng có."),
         F(3, "Ví dụ: 看到我的录取通知书，从不喝酒的父亲破天荒地喝了一杯。 Nhìn thấy giấy báo trúng tuyển của tôi, người cha chưa bao giờ uống rượu lần đầu tiên uống một ly."),
         F(4, "Câu thứ ba: 不可思议. Vốn là từ nhà Phật, chỉ điều huyền diệu không thể nghĩ bàn; nay nghĩa là không thể tưởng tượng nổi, rất khó hiểu. Tiếng Việt cũng có cụm bất khả tư nghị. Trong bài: 在这不可思议的十秒里."),
         F(5, "Ví dụ: 古埃及人到底是用什么方法建筑起金字塔的，至今仍让人觉得不可思议。 Người Ai Cập cổ đại rốt cuộc đã dùng cách gì để xây kim tự tháp, đến nay vẫn khiến người ta thấy khó tin.")])

add("bullets", section="Thành ngữ 成语", title="Thành ngữ (2)", size=34,
    items=["## 英雄所见略同 – anh hùng gặp nhau, ý kiến tương đồng",
           "咱们俩对此的看法竟然不谋而合，可见英雄所见略同。",
           "## 取而代之 qǔ'érdàizhī – gạt đi mà thế chỗ, thay thế",
           "这家工厂经过技术改造后，许多落后工艺被淘汰，取而代之的是先进的新工艺。",
           "## 杞人忧天 qǐrén-yōutiān – người nước Kỷ lo trời sập; lo hão",
           "你真是杞人忧天，我们这个地区地势高，即便下大雨，也绝不会被水淹。"],
    say=[F(0, "Câu thứ tư: 英雄所见略同. 所见 là cái nhìn, 略同 là gần giống nhau: anh hùng nhìn nhận gần như nhau. Đây là câu nói dân gian, thường dùng để khen cả hai người có cùng ý kiến, có khi là tự khen mình một cách hài hước."),
         F(1, "Ví dụ: 咱们俩对此的看法竟然不谋而合，可见英雄所见略同。 Quan điểm của hai chúng ta về việc này lại trùng hợp như đã hẹn, đúng là anh hùng gặp nhau. 不谋而合 là không bàn trước mà vẫn trùng khớp."),
         F(2, "Câu thứ năm: 取而代之, gạt người khác hay vật khác đi để thế vào chỗ đó. Trong bài: 有人担心人类医生最终会被他取而代之. Mẫu rất hay gặp là 取而代之的是 cộng danh từ, nghĩa là thay vào đó là."),
         F(3, "Ví dụ: 这家工厂经过技术改造后，许多落后工艺被淘汰，取而代之的是先进的新工艺。 Sau khi cải tiến kỹ thuật, nhiều quy trình lạc hậu của nhà máy bị loại bỏ, thay vào đó là quy trình mới tiên tiến."),
         F(4, "Câu thứ sáu: 杞人忧天. Chuyện xưa kể rằng có một người nước Kỷ suốt ngày lo trời sập, ăn không ngon ngủ không yên. Thành ngữ này chỉ nỗi lo hão huyền, không có căn cứ."),
         F(5, "Ví dụ: 你真是杞人忧天，我们这个地区地势高，即便下大雨，也绝不会被水淹。 Cậu đúng là lo hão, vùng chúng ta địa thế cao, dù mưa lớn cũng tuyệt đối không bị ngập.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 课后练习", title="Bài tập 1: Chọn từ thích hợp điền vào chỗ trống (1)", reveal=True, size=33,
    items=["## 确诊 · 甚为 · 望尘莫及 · 谨慎 · 罕见 · 亮相 · 权威 · 取而代之",
           "(1) 这是成都熊猫宝宝的最新照片，它们已经为十一黄金周的初次___做好了准备。",
           "Đáp án: 亮相",
           "(2) 在地质博物馆中，我见到许多世间___的奇石珍宝。",
           "Đáp án: 罕见",
           "(3) 老师在小学生心目中地位非常高，所以他们的一言一行都应该非常___。",
           "Đáp án: 谨慎",
           "(4) 经过反复的检测，他被___为新冠阳性。",
           "Đáp án: 确诊"],
    say=["Bây giờ chúng ta sang phần luyện tập. Bài tập một: chọn từ thích hợp điền vào chỗ trống.",
         F(0, "Có tám từ: 确诊，甚为，望尘莫及，谨慎，罕见，亮相，权威，取而代之. Trong đó 望尘莫及 là thành ngữ ta vừa gặp ở cuối bài khóa: bị bỏ xa, không sao đuổi kịp."),
         F(1, "Câu một: 这是成都熊猫宝宝的最新照片，它们已经为十一黄金周的初次什么做好了准备。 Đây là ảnh mới nhất của những bé gấu trúc ở Thành Đô, chúng đã sẵn sàng cho lần đầu gì đó vào tuần lễ vàng Quốc khánh. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 亮相. 初次亮相, lần đầu ra mắt. 十一 ở đây là ngày một tháng mười, Quốc khánh Trung Quốc."),
         F(3, "Câu hai: 在地质博物馆中，我见到许多世间什么的奇石珍宝。 Trong bảo tàng địa chất, tôi thấy nhiều đá lạ, châu báu thế nào trên đời?"),
         F(4, "Đáp án: 罕见. 世间罕见, hiếm có trên đời."),
         F(5, "Câu ba: 老师在小学生心目中地位非常高，所以他们的一言一行都应该非常什么。 Thầy cô có địa vị rất cao trong lòng học sinh tiểu học, nên mỗi lời nói việc làm đều phải rất thế nào?"),
         F(6, "Đáp án: 谨慎. 一言一行都应该非常谨慎, mỗi lời nói việc làm đều phải rất thận trọng."),
         F(7, "Câu bốn: 经过反复的检测，他被什么为新冠阳性。 Qua nhiều lần xét nghiệm, anh ấy bị làm sao là dương tính với Covid?"),
         F(8, "Đáp án: 确诊. 被确诊为新冠阳性, được chẩn đoán xác định dương tính với Covid. Đây đúng là mẫu 被确诊为 trong phần từ mới.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 1: Chọn từ thích hợp điền vào chỗ trống (2)", reveal=True, size=33,
    items=["(5) 电子时代，固定电话已经逐渐被淘汰，___的是手机。",
           "Đáp án: 取而代之",
           "(6) 很多资深HR认为：面试时，言行举止___关键。",
           "Đáp án: 甚为",
           "(7) 怎样培养学生不惧___，勇于表达，这是现代教育讨论的核心话题。",
           "Đáp án: 权威",
           "(8) 他表现得太优异了，让其余参赛者___。",
           "Đáp án: 望尘莫及"],
    say=[F(0, "Câu năm: 电子时代，固定电话已经逐渐被淘汰，什么的是手机。 Thời đại điện tử, điện thoại cố định dần dần bị đào thải, cái gì là điện thoại di động?"),
         F(1, "Đáp án: 取而代之. 取而代之的是手机, thay vào đó là điện thoại di động. Đây chính là mẫu 取而代之的是 vừa học."),
         F(2, "Câu sáu: 很多资深HR认为：面试时，言行举止什么关键。 Nhiều chuyên viên nhân sự kỳ cựu cho rằng: khi phỏng vấn, cử chỉ lời nói thế nào là then chốt?"),
         F(3, "Đáp án: 甚为. 言行举止甚为关键, cử chỉ lời nói hết sức quan trọng. Phía sau là tính từ 关键, nên cần một phó từ chỉ mức độ."),
         F(4, "Câu bảy: 怎样培养学生不惧什么，勇于表达，这是现代教育讨论的核心话题。 Làm sao để học sinh không sợ gì, dám bày tỏ ý kiến, đó là chủ đề cốt lõi của giáo dục hiện đại."),
         F(5, "Đáp án: 权威. 不惧权威, không sợ uy quyền, không sợ người có địa vị."),
         F(6, "Câu tám: 他表现得太优异了，让其余参赛者什么。 Anh ấy thể hiện quá xuất sắc, khiến các thí sinh khác làm sao?"),
         F(7, "Đáp án: 望尘莫及. 让其余参赛者望尘莫及, khiến các thí sinh còn lại chỉ biết nhìn theo, không sao đuổi kịp.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn đáp án đúng (1)", reveal=True, size=34,
    items=["(1) 张大千先生在书画上的杰出成就，令人难以（  ）。 A.权威 B.赞许 C.企及 D.资深",
           "Đáp án: C. 企及 – 难以企及 (khó lòng theo kịp)",
           "(2) 在自然科学（  ），数学是最重要的基础学科。 A.领域 B.界限 C.范围 D.规模",
           "Đáp án: A. 领域 – 在……领域 (trong lĩnh vực …)",
           "(3) 团队终于突破了技术难关，新研制的无人机可以实现GPS（  ）定位。 A.精准 B.明确 C.精细 D.正确",
           "Đáp án: A. 精准 – 精准定位 (định vị chính xác)"],
    say=["Bài tập hai: chọn đáp án đúng.",
         F(0, "Câu một: 张大千先生在书画上的杰出成就，令人难以什么。 Thành tựu xuất sắc của ông Trương Đại Thiên về thư họa khiến người ta khó lòng làm gì? A, 权威; B, 赞许; C, 企及; D, 资深. 张大千 là một danh họa nổi tiếng của Trung Quốc thế kỷ hai mươi."),
         F(1, "Đáp án: C, 企及. 难以企及 là cụm cố định, nghĩa là khó lòng theo kịp. Các từ còn lại không đứng sau 难以 được."),
         F(2, "Câu hai: 在自然科学什么，数学是最重要的基础学科。 Trong cái gì của khoa học tự nhiên, toán học là môn cơ sở quan trọng nhất? A, 领域; B, 界限; C, 范围; D, 规模."),
         F(3, "Đáp án: A, 领域. 在自然科学领域, trong lĩnh vực khoa học tự nhiên. Bài khóa cũng có 癌症治疗领域. 界限 là ranh giới, 范围 là phạm vi, 规模 là quy mô."),
         F(4, "Câu ba: 团队终于突破了技术难关，新研制的无人机可以实现GPS什么定位。 Nhóm nghiên cứu cuối cùng đã vượt qua khó khăn kỹ thuật, máy bay không người lái mới chế tạo có thể định vị GPS thế nào? A, 精准; B, 明确; C, 精细; D, 正确."),
         F(5, "Đáp án: A, 精准. 精准定位 là kết hợp cố định, định vị chính xác. 明确 là rõ ràng, 精细 là tinh xảo, tỉ mỉ.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn đáp án đúng (2)", reveal=True, size=34,
    items=["(4) 面对巨大的市场商机，一个成熟的领导者要（  ）决断，切不可冲动行事。 A.谨慎 B.细致 C.细心 D.严谨",
           "Đáp án: A. 谨慎 – 谨慎决断, đối lập với 冲动行事",
           "(5) 他花费七年时间（  ）的新服饰品牌，一上市就受到追捧。 A.打造 B.创造 C.制造 D.营造",
           "Đáp án: A. 打造 – 打造品牌 (xây dựng thương hiệu)"],
    say=[F(0, "Câu bốn: 面对巨大的市场商机，一个成熟的领导者要什么决断，切不可冲动行事。 Trước cơ hội kinh doanh lớn trên thị trường, một người lãnh đạo chín chắn phải quyết đoán thế nào, tuyệt đối không được hành động bốc đồng. A, 谨慎; B, 细致; C, 细心; D, 严谨."),
         F(1, "Đáp án: A, 谨慎. 谨慎决断 là quyết định một cách thận trọng, đối lập trực tiếp với 冲动行事. 细致，细心 là tỉ mỉ, cẩn thận trong công việc nhỏ; 严谨 là chặt chẽ, nghiêm cẩn, thường nói về thái độ học thuật. Các bạn để ý chữ 切 trong 切不可, giống 切勿 ở bài trước."),
         F(2, "Câu năm: 他花费七年时间什么的新服饰品牌，一上市就受到追捧。 Thương hiệu thời trang mới mà anh ấy mất bảy năm để làm gì, vừa ra thị trường đã được săn đón. A, 打造; B, 创造; C, 制造; D, 营造."),
         F(3, "Đáp án: A, 打造. 打造品牌 là kết hợp cố định, xây dựng thương hiệu. 创造 là sáng tạo ra cái mới, như 创造奇迹; 制造 là chế tạo sản phẩm; 营造 là tạo ra bầu không khí, như 营造气氛.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ và mẫu câu cho sẵn trả lời câu hỏi", reveal=True, size=32,
    items=["(1) 在你看来，未来哪些职业会被人工智能取代？（比N还/更N）",
           "Đáp án gợi ý: 翻译、客服、收银员可能会被取代，因为有些翻译软件翻得比翻译还翻译。",
           "(2) 人工智能在生活中的应用有哪些？（与此同时……）",
           "Đáp án gợi ý: 手机可以用语音助手帮我们设闹钟，与此同时，它还能帮我们翻译和导航。",
           "(3) 人工智能医生和人类医生相比有哪些优势？（短短……，甚为……）",
           "Đáp án gợi ý: 短短十秒，它就能翻阅上千万页资料，速度甚为惊人，而且不会累。",
           "(4) 线上教育是否能够创造新的就业机会？（愈发……）",
           "Đáp án gợi ý: 能。随着网络愈发普及，网课老师、课程设计师等新职业也愈发受欢迎。"],
    say=["Bài tập ba: dùng từ và mẫu câu cho sẵn để trả lời câu hỏi. Đây là câu hỏi mở, thầy đưa ra đáp án gợi ý.",
         F(0, "Câu một: 在你看来，未来哪些职业会被人工智能取代？ Theo bạn, trong tương lai nghề nào sẽ bị trí tuệ nhân tạo thay thế? Dùng mẫu 比N还N."),
         F(1, "Đáp án gợi ý: 翻译、客服、收银员可能会被取代，因为有些翻译软件翻得比翻译还翻译。 Phiên dịch, chăm sóc khách hàng, thu ngân có thể bị thay thế, vì có những phần mềm dịch còn dịch giỏi hơn cả phiên dịch viên."),
         F(2, "Câu hai: 人工智能在生活中的应用有哪些？ Trí tuệ nhân tạo được ứng dụng những gì trong cuộc sống? Dùng 与此同时."),
         F(3, "Đáp án gợi ý: 手机可以用语音助手帮我们设闹钟，与此同时，它还能帮我们翻译和导航。 Điện thoại có thể dùng trợ lý giọng nói giúp ta đặt báo thức, đồng thời còn giúp ta dịch thuật và dẫn đường."),
         F(4, "Câu ba: 人工智能医生和人类医生相比有哪些优势？ So với bác sĩ con người, bác sĩ trí tuệ nhân tạo có ưu thế gì? Dùng 短短 và 甚为."),
         F(5, "Đáp án gợi ý: 短短十秒，它就能翻阅上千万页资料，速度甚为惊人，而且不会累。 Chỉ trong mười giây, nó có thể lật xem hàng chục triệu trang tài liệu, tốc độ hết sức kinh người, mà lại không biết mệt."),
         F(6, "Câu bốn: 线上教育是否能够创造新的就业机会？ Giáo dục trực tuyến có thể tạo ra cơ hội việc làm mới không? Dùng 愈发."),
         F(7, "Đáp án gợi ý: 能。随着网络愈发普及，网课老师、课程设计师等新职业也愈发受欢迎。 Có. Khi mạng Internet ngày càng phổ biến, những nghề mới như giáo viên dạy trực tuyến, nhà thiết kế khóa học cũng ngày càng được ưa chuộng. Các bạn thấy không, chính bài giảng các bạn đang xem cũng là một ví dụ.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Chọn từ điền vào đoạn văn", reveal=True, size=32,
    items=["## 庞大 · 倾力 · 造福 · 时空 · 得力 · 识别 · 愈发",
           "在医学影像诊断中，人工智能（AI）技术已成为医生的___助手。“AI+医学影像”技术在一众医疗服务中率先得到应用。随着科技的不断进步，医学影像的采集___便利和精准，加上___的数据库突破了___障碍，使得医学影像处理和___的技术逐渐成熟。未来，在企业与医院、医生的___合作之下，“AI+医学影像”技术的发展必将___更多患者。",
           "Đáp án: 得力 · 愈发 · 庞大 · 时空 · 识别 · 倾力 · 造福"],
    say=[F(0, "Bài tập bốn: chọn từ điền vào đoạn văn. Có bảy từ: 庞大，倾力，造福，时空，得力，识别，愈发."),
         F(1, "在医学影像诊断中，人工智能技术已成为医生的什么助手。人工智能加医学影像技术在一众医疗服务中率先得到应用。随着科技的不断进步，医学影像的采集什么便利和精准，加上什么的数据库突破了什么障碍，使得医学影像处理和什么的技术逐渐成熟。未来，在企业与医院、医生的什么合作之下，人工智能加医学影像技术的发展必将什么更多患者。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 已成为医生的得力助手；医学影像的采集愈发便利和精准；加上庞大的数据库突破了时空障碍；医学影像处理和识别的技术逐渐成熟；在企业与医院、医生的倾力合作之下；必将造福更多患者。 Trong chẩn đoán hình ảnh y khoa, trí tuệ nhân tạo đã trở thành trợ thủ đắc lực của bác sĩ. Cùng với tiến bộ khoa học, việc thu thập hình ảnh ngày càng tiện lợi và chính xác, thêm vào đó cơ sở dữ liệu khổng lồ đã vượt qua rào cản không gian và thời gian, khiến kỹ thuật xử lý và nhận dạng hình ảnh dần hoàn thiện. Tương lai, với sự hợp tác hết sức giữa doanh nghiệp, bệnh viện và bác sĩ, công nghệ này chắc chắn sẽ mang lại lợi ích cho nhiều bệnh nhân hơn.")])

# ======================= THẢO LUẬN =======================
add("bullets", chapter="Thảo luận: AI trong y tế", section="Thảo luận 讨论", title="Thảo luận: bác sĩ robot có thay thế bác sĩ con người?", reveal=True, size=33,
    items=["(1) 你愿意让机器人医生给你看病吗？为什么？",
           "Đáp án gợi ý: 愿意让它做助手：它速度快、记忆力强；但最后的决定还是应该由人类医生来做。",
           "(2) 机器人医生能完全取代人类医生吗？",
           "Đáp án gợi ý: 不能。看病不只是分析数据，还需要沟通、安慰和关心病人，这些是机器难以企及的。",
           "(3) 在越南，人工智能在医疗方面有哪些应用？",
           "Đáp án gợi ý: 一些医院用人工智能辅助看X光片、CT片；2018年，越南也有医院引进过沃森辅助癌症诊疗。"],
    say=["Cuối cùng, chúng ta cùng thảo luận. Các bạn hãy thử trả lời bằng tiếng Trung, dùng các từ và mẫu câu vừa học.",
         F(0, "Câu một: 你愿意让机器人医生给你看病吗？为什么？ Bạn có sẵn lòng để bác sĩ robot khám bệnh cho mình không? Vì sao?"),
         F(1, "Đáp án gợi ý: 愿意让它做助手：它速度快、记忆力强；但最后的决定还是应该由人类医生来做。 Sẵn lòng để nó làm trợ lý: nó nhanh, trí nhớ tốt; nhưng quyết định cuối cùng vẫn nên do bác sĩ con người đưa ra. Đây cũng chính là cách Watson làm việc trong bài khóa: 得力助手."),
         F(2, "Câu hai: 机器人医生能完全取代人类医生吗？ Bác sĩ robot có thể hoàn toàn thay thế bác sĩ con người không?"),
         F(3, "Đáp án gợi ý: 不能。看病不只是分析数据，还需要沟通、安慰和关心病人，这些是机器难以企及的。 Không thể. Khám bệnh không chỉ là phân tích số liệu, mà còn cần trò chuyện, an ủi và quan tâm người bệnh, đó là những điều máy móc khó lòng theo kịp."),
         F(4, "Câu ba: 在越南，人工智能在医疗方面有哪些应用？ Ở Việt Nam, trí tuệ nhân tạo được ứng dụng trong y tế như thế nào?"),
         F(5, "Đáp án gợi ý: 一些医院用人工智能辅助看X光片、CT片；二零一八年，越南也有医院引进过沃森辅助癌症诊疗。 Một số bệnh viện dùng trí tuệ nhân tạo hỗ trợ đọc phim X quang, phim CT; năm hai nghìn không trăm mười tám, Việt Nam cũng có bệnh viện, như Bệnh viện Đa khoa tỉnh Phú Thọ, từng đưa Watson vào hỗ trợ điều trị ung thư."),
         F(5, "Tuy vậy, về sau Watson cũng bị phê bình là có những đề xuất chưa phù hợp với bệnh nhân châu Á, và năm hai nghìn không trăm hai mươi hai IBM đã bán mảng y tế này. Điều đó cho thấy: máy móc rất giỏi, nhưng vẫn cần con người kiểm tra lại.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết", section="Tổng kết", title="Tổng kết bài 4.2", size=34,
    items=["Từ vựng trọng tâm: 亮相 · 癌症 · 诊疗 · 确诊 · 罕见 · 精准 · 权威 · 甚为 · 资深 · 得力 · 生涯 · 临床 · 庞大 · 顺便 · 谨慎 · 倾力 · 打造 · 企及 · 愈发 · 造福",
           "Mẫu câu: 甚为 · 顺便 · 与此同时 · 也就是说 · 短短…… · N之adj · 比N还N · 愈发 · 造福(于)",
           "Thành ngữ: 无药可救 · 破天荒 · 不可思议 · 英雄所见略同 · 取而代之 · 杞人忧天 (+ 望尘莫及)",
           "Từ dễ nhầm: 白血病 · 生涯 · 顺便 · 文献 · 评定 · 谨慎",
           "## Bài tập về nhà",
           "Viết một đoạn khoảng 300 chữ: 机器人医生会取代人类医生吗？ (dùng 与此同时 · 也就是说 · 比N还N · 愈发)"],
    say=["Chúng ta cùng tổng kết bài bốn chấm hai.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 亮相，癌症，诊疗，确诊，罕见，精准，权威，甚为，资深，得力，生涯，临床，庞大，顺便，谨慎，倾力，打造，企及，愈发，造福."),
         F(1, "Về mẫu câu: 甚为 là hết sức; 顺便 là tiện thể; 与此同时 là đồng thời; 也就是说 là nói cách khác; 短短 nhấn mạnh thời gian ngắn; danh từ cộng 之 cộng tính từ, như 反应之快; 比医生还医生; 愈发 là càng thêm; và 造福于人类."),
         F(2, "Về thành ngữ, hãy ôn lại sáu câu: 无药可救，破天荒，不可思议，英雄所见略同，取而代之，杞人忧天, và thêm 望尘莫及 trong bài tập."),
         F(3, "Và nhớ những từ Hán Việt dễ nhầm: 白血病 là bệnh bạch cầu, 生涯 là sự nghiệp, 顺便 là tiện thể, 文献 là tài liệu, 评定 là đánh giá, 谨慎 là thận trọng."),
         F(5, "Bài tập về nhà: hãy viết một đoạn văn khoảng ba trăm chữ với đề 机器人医生会取代人类医生吗？ Bác sĩ robot có thay thế bác sĩ con người không? Hãy dùng 与此同时，也就是说，比什么还什么，愈发."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Ở bài sau, công nghệ sẽ bước vào một lĩnh vực rất riêng tư: tình yêu và hôn nhân. Liệu thuật toán có tìm được người hợp với bạn? Hẹn gặp lại các bạn ở bài bốn chấm ba, bài cuối của Đơn vị bốn: 算法时代：谁是你的菜？ Thời đại thuật toán: ai là người hợp gu bạn? Chúc các bạn học tốt!"])

lesson = {
    "title": "顶石中文 – Bài 4.2: 机器人医生，简直神了！ (Bác sĩ robot, đúng là thần kỳ!)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"亮相": "亮象",            # liàngxiàng
                    "甚为": "甚维",            # shènwéi
                    "血病": "谑病",            # báixuèbìng
                    "血癌": "谑癌",            # xuè'ái
                    "它为": "它位",            # tā wèi (vì, cho)
                    "并为": "并位",            # bìng wèi
                    "切不可": "怯不可",        # qiè bù kě
                    "重重": "虫虫",            # chóngchóng
                    "数十位": "树十位"},       # shù shí wèi
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds42.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
