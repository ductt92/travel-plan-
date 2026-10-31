#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Thượng) – Bài 5 «学一门外语需要理由吗？». Chạy để sinh bai05.json."""
import json
import os

TAG = "HSK 6 (Thượng) · Bài 5 · 学一门外语需要理由吗？"
slides = []


def add(type_, chapter=None, section="", **kw):
    s = {"type": type_, "section": section, **kw}
    if chapter:
        s["chapter"] = chapter
    slides.append(s)


def F(i, t, **kw):
    return {"t": t, "f": i, **kw}


# ======================= MỞ ĐẦU =======================
# Tên bài có 11 chữ (kể cả dấu hỏi), vừa khít một dòng chữ cỡ lớn nên giữ nguyên.
add("title", chapter="Mở đầu",
    top="Giáo trình chuẩn HSK 6 – Quyển Thượng",
    zh="学一门外语需要理由吗？", py="Xué yì mén wàiyǔ xūyào lǐyóu ma?",
    vi="Bài 5: Học ngoại ngữ cần lý do ư?",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Thượng.",
         "Hôm nay chúng ta học bài năm: 学一门外语需要理由吗？ Nghĩa là: Học một ngoại ngữ thì cần phải có lý do ư?",
         "Đây là bài mở đầu của Chủ đề hai, 不甘平庸, Không cam chịu tầm thường. Bài khóa là lời kể rất dí dỏm của một người muốn học ngoại ngữ. Anh ấy hào hứng đến trung tâm ngoại ngữ, nhưng lại bị hỏi dồn: vì sao muốn học, có định đi nước ngoài không, làm nghề gì. Cuối cùng anh ấy bỏ về và tự tìm cho mình một cách học riêng.",
         "Qua bài này, chúng ta cũng thử tự hỏi: mình học tiếng Trung để làm gì, và cách học nào hợp với mình nhất."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài khóa: câu chuyện đi học ngoại ngữ và lựa chọn cách học của nhân vật tôi",
           "Nắm vững 44 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: trợ từ 而已, liên từ 固然, phó từ 无非",
           "Phân biệt hai phó từ 专程 và 专门",
           "Mở rộng: câu sai do thiếu thành phần (成分残缺) và các cặp từ gần nghĩa"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa: câu chuyện đi học ngoại ngữ của nhân vật tôi, và vì sao cuối cùng anh ấy chọn cách tự học trên mạng."),
         F(1, "Thứ hai, nắm vững bốn mươi bốn từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học ba điểm ngữ pháp: trợ từ 而已, nghĩa là mà thôi; liên từ 固然, nghĩa là tất nhiên, tuy; và phó từ 无非, nghĩa là chẳng qua, chỉ là."),
         F(3, "Thứ tư, phân biệt hai phó từ rất dễ nhầm: 专程 và 专门."),
         F(4, "Thứ năm, phần mở rộng: nhận biết câu sai do thiếu thành phần, tiếng Trung gọi là 成分残缺, và làm quen với mười sáu cặp từ gần nghĩa."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Câu hỏi khởi động: Vì sao bạn học tiếng Trung?", size=40,
    items=["你为什么学习汉语？ – Vì sao bạn học tiếng Trung?",
           "为了找工作 – để tìm việc · 大学的专业是中文 – chuyên ngành đại học là tiếng Trung",
           "为了在中国旅行 – để đi du lịch Trung Quốc · 我有中国朋友 – tôi có bạn người Trung Quốc",
           "对汉语感兴趣 – hứng thú với tiếng Trung · 为了显得很酷 – để trông thật ngầu",
           "其他原因 – lý do khác: ……"],
    say=["Chúng ta bắt đầu bằng phần khởi động. Câu hỏi đầu tiên rất gần gũi với chính các bạn.",
         F(0, "你为什么学习汉语？ Vì sao bạn học tiếng Trung? Sách yêu cầu các bạn chọn đáp án trong các lựa chọn sau; nếu không có đáp án nào đúng với mình, thì hãy tự viết thêm."),
         F(1, "为了找工作。 Để tìm việc làm. 大学的专业是中文。 Chuyên ngành đại học của tôi là tiếng Trung."),
         F(2, "为了在中国旅行。 Để đi du lịch ở Trung Quốc. 我有中国朋友。 Tôi có bạn người Trung Quốc."),
         F(3, "对汉语感兴趣。 Tôi hứng thú với tiếng Trung. Và một lý do rất vui: 为了显得很酷。 Để trông thật ngầu. 酷 là phiên âm của từ cool trong tiếng Anh, nghĩa là ngầu."),
         F(4, "其他原因。 Lý do khác. Các bạn hãy tạm dừng video, nói lý do học tiếng Trung của mình bằng tiếng Trung. Lát nữa đọc bài khóa, các bạn sẽ thấy câu hỏi vì sao học ngoại ngữ lại gây ra cả một câu chuyện đấy.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 原 và 员", size=38,
    items=["## 原 (nguyên): ban đầu, vốn có",
           "原文 nguyên văn · 原来 vốn dĩ · 原先 lúc đầu · 原地 tại chỗ · 原因 nguyên nhân · 原有 vốn có",
           "原价 giá gốc · 原版 bản gốc · 原始 nguyên thủy · 原形 nguyên hình · 原状 trạng thái cũ · 原意 ý ban đầu",
           "## 员 (viên): người làm một công việc, thành viên",
           "学员 học viên · 服务员 nhân viên phục vụ · 售货员 người bán hàng · 售票员 người bán vé",
           "演员 diễn viên · 人员 nhân viên · 职员 viên chức · 运动员 vận động viên · 店员 nhân viên cửa hàng · 船员 thuyền viên · 员工 nhân viên"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo, rất có lợi cho người Việt vì hầu hết các chữ đều có âm Hán Việt quen thuộc.",
         F(0, "Nhóm thứ nhất có chữ 原, Hán Việt là nguyên, nghĩa là ban đầu, vốn có."),
         F(1, "原文，原来，原先，原地，原因，原有。 Tức là: nguyên văn, vốn dĩ, lúc đầu, tại chỗ, nguyên nhân, vốn có. Trong bài khóa, nhân vật tôi muốn 阅读原文, đọc nguyên văn, tức là đọc bản gốc không qua dịch."),
         F(2, "原价，原版，原始，原形，原状，原意。 Tức là: giá gốc, bản gốc, nguyên thủy, nguyên hình, trạng thái ban đầu, và ý ban đầu."),
         F(3, "Nhóm thứ hai có chữ 员, Hán Việt là viên, chỉ người làm một công việc nào đó, hoặc thành viên của một tổ chức."),
         F(4, "学员，服务员，售货员，售票员。 Tức là: học viên, nhân viên phục vụ, người bán hàng, người bán vé. Từ 学员 xuất hiện nhiều lần trong bài khóa."),
         F(5, "演员，人员，职员，运动员，店员，船员，员工。 Tức là: diễn viên, nhân viên, viên chức, vận động viên, nhân viên cửa hàng, thuyền viên, và nhân viên của công ty.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 力 và 久", size=38,
    items=["## 力 (lực): sức, sức mạnh",
           "动力 động lực · 精力 sức lực · 能力 năng lực · 压力 áp lực · 财力 tài lực · 脑力 trí lực · 体力 thể lực",
           "听力 khả năng nghe · 努力 nỗ lực · 尽力 tận lực · 出力 góp sức · 用力 dùng sức · 力气 sức lực · 力量 lực lượng, sức mạnh",
           "## 久 (cửu): lâu",
           "持久 lâu bền · 悠久 lâu đời · 不久 không lâu · 长久 lâu dài · 多久 bao lâu · 好久 rất lâu",
           "许久 hồi lâu · 永久 vĩnh cửu · 久远 xa xưa · 久别 xa cách lâu · 日久天长 ngày tháng dài lâu"],
    say=[F(0, "Nhóm thứ ba có chữ 力, Hán Việt là lực, nghĩa là sức, sức mạnh."),
         F(1, "动力，精力，能力，压力，财力，脑力，体力。 Tức là: động lực, sức lực, năng lực, áp lực, tài lực, trí lực, thể lực. Từ 动力 có trong bài khóa: 没有目标就缺乏动力, không có mục tiêu thì thiếu động lực."),
         F(2, "听力，努力，尽力，出力，用力，力气，力量。 Tức là: khả năng nghe, nỗ lực, tận lực, góp sức, dùng sức, sức lực, và sức mạnh."),
         F(3, "Nhóm cuối cùng có chữ 久, Hán Việt là cửu, nghĩa là lâu, như trong từ vĩnh cửu."),
         F(4, "持久，悠久，不久，长久，多久，好久。 Tức là: lâu bền, lâu đời, không lâu, lâu dài, bao lâu, rất lâu. Bài khóa có câu 光凭兴趣，恐怕难以持久, chỉ dựa vào hứng thú thì e là khó bền lâu."),
         F(5, "许久，永久，久远，久别，日久天长。 Tức là: hồi lâu, vĩnh cửu, xa xưa, xa cách lâu ngày, và ngày tháng dài lâu."),
         "Các bạn thấy không, chỉ cần nắm nghĩa của một chữ gốc, ta có thể đoán được nghĩa của cả một nhóm từ. Hãy áp dụng cách này khi học từ mới nhé."])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng)
V = [
    ("迫不及待", "pòbùjídài", "bách bất cập đãi", "thành ngữ", "nóng lòng, không thể chờ đợi được", "他迫不及待地打开了礼物。", "Anh ấy nóng lòng mở ngay món quà.",
     "Thành ngữ. Nghĩa đen là gấp đến mức không kịp chờ đợi, tức là nóng lòng, sốt ruột muốn làm ngay. Thường dùng theo mẫu 迫不及待地 cộng động từ."),
    ("依靠", "yīkào", "y kháo", "động từ", "dựa vào, phụ thuộc vào", "我不想永远依靠父母。", "Tôi không muốn mãi dựa dẫm vào bố mẹ.",
     "Động từ, nghĩa là dựa vào, phụ thuộc vào. Trong bài, 不再依靠翻译 là không còn phải dựa vào bản dịch nữa."),
    ("借助", "jièzhù", "tá trợ", "động từ", "nhờ vào, nhờ sự giúp đỡ của", "他借助字典读完了这本小说。", "Anh ấy nhờ từ điển mà đọc xong cuốn tiểu thuyết này.",
     "Động từ, nghĩa là nhờ vào, mượn sức của một công cụ hay một người nào đó. Hay gặp: 借助字典，借助网络，借助工具."),
    ("勉强", "miǎnqiǎng", "miễn cưỡng", "tính từ", "gắng gượng, cố gượng (sức chưa đủ)", "他病还没好，勉强上了一天班。", "Bệnh chưa khỏi, anh ấy gắng gượng đi làm một ngày.",
     "Tính từ, nghĩa là gắng gượng, cố gượng, tức là năng lực hay sức lực chưa đủ nhưng vẫn cố làm. Chú ý: tiếng Việt miễn cưỡng thường là không tự nguyện; còn trong bài, 勉强查阅 là chật vật tra cứu, vì trình độ chưa đủ. Âm tiết thứ hai của từ này đọc thanh ba."),
    ("机构", "jīgòu", "cơ cấu", "danh từ", "đơn vị, cơ quan, tổ chức", "我找到了一家语言学习机构。", "Tôi đã tìm được một trung tâm dạy ngoại ngữ.",
     "Danh từ, nghĩa là đơn vị, cơ quan, tổ chức. Cẩn thận, đây là từ dễ nhầm: cơ cấu trong tiếng Việt là cấu trúc, còn 机构 trong tiếng Trung là cơ quan, tổ chức. 语言学习机构 chính là trung tâm ngoại ngữ."),
    ("栋", "dòng", "đống", "lượng từ", "tòa (nhà)", "那栋楼有三十层。", "Tòa nhà kia có ba mươi tầng.",
     "Lượng từ, dùng cho nhà cửa, tương đương tòa, ngôi. Ví dụ 一栋办公楼, một tòa nhà văn phòng. Hán Việt là đống, như trong từ đống lương, tức cột trụ nhà."),
    ("兴致勃勃", "xìngzhì bóbó", "hứng trí bột bột", "thành ngữ", "vô cùng hào hứng", "孩子们兴致勃勃地参观了动物园。", "Bọn trẻ hào hứng đi tham quan vườn thú.",
     "Thành ngữ, nghĩa là vô cùng hào hứng, hứng thú dạt dào. 兴致 là hứng thú, 勃勃 là dồi dào, mạnh mẽ."),
    ("专程", "zhuānchéng", "chuyên trình", "phó từ", "đặc biệt đi (chỉ vì việc này)", "我专程去北京看你。", "Tôi đặc biệt đến Bắc Kinh để thăm bạn.",
     "Phó từ, nghĩa là đặc biệt đi một chuyến chỉ vì một việc. Lát nữa chúng ta sẽ so sánh kỹ từ này với từ 专门."),
    ("修养", "xiūyǎng", "tu dưỡng", "danh từ", "trình độ, thái độ xử sự đúng mực", "她是一位很有修养的女士。", "Bà ấy là một quý cô rất có giáo dưỡng.",
     "Danh từ, chỉ trình độ hiểu biết và thái độ cư xử lịch sự, đúng mực của một người. Chú ý: tu dưỡng trong tiếng Việt thường là động từ, rèn luyện bản thân; còn 很有修养 là rất có giáo dưỡng, rất lịch sự."),
    ("接连", "jiēlián", "tiếp liên", "phó từ", "liên tiếp, liên tục", "他接连问了好几个问题。", "Anh ấy liên tiếp hỏi mấy câu liền.",
     "Phó từ, nghĩa là liên tiếp, hết cái này đến cái khác. Trong bài có cụm 接连不断的发问, những câu hỏi dồn dập không ngớt."),
    ("涉及", "shèjí", "thiệp cập", "động từ", "liên quan đến, đề cập đến", "这个问题涉及个人隐私。", "Câu hỏi này liên quan đến đời tư cá nhân.",
     "Động từ, nghĩa là liên quan đến, đụng chạm đến, đề cập đến một phạm vi nào đó."),
    ("隐私", "yǐnsī", "ẩn tư", "danh từ", "sự riêng tư, đời tư", "我们应该尊重别人的隐私。", "Chúng ta nên tôn trọng sự riêng tư của người khác.",
     "Danh từ, nghĩa là chuyện riêng tư, đời tư, những điều không muốn người khác biết."),
    ("反感", "fǎngǎn", "phản cảm", "tính từ", "có ác cảm, bực mình, khó chịu", "大家对他的做法很反感。", "Mọi người rất khó chịu với cách làm của anh ta.",
     "Tính từ, nghĩa là có ác cảm, thấy khó chịu, bực mình. Cẩn thận: tiếng Việt phản cảm là nói một hình ảnh hay hành vi gây khó chịu cho người khác; còn 我很反感 là nói cảm giác của chính mình: tôi rất khó chịu, tôi rất ghét."),
    ("火药", "huǒyào", "hỏa dược", "danh từ", "thuốc nổ, thuốc súng", "火药是中国古代四大发明之一。", "Thuốc súng là một trong bốn phát minh lớn của Trung Quốc cổ đại.",
     "Danh từ, nghĩa là thuốc nổ, thuốc súng. Trong bài có cụm 火药味十足, sặc mùi thuốc súng, tức là lời nói rất gay gắt, như sắp cãi nhau."),
    ("忍耐", "rěnnài", "nhẫn nại", "động từ", "nhẫn nại, kiềm chế", "她极力忍耐着，没有发火。", "Cô ấy cố hết sức kiềm chế, không nổi nóng.",
     "Động từ, nghĩa là nén nhịn, kiềm chế cảm xúc. Chú ý: tiếng Việt nhẫn nại thiên về kiên trì bền bỉ; còn 忍耐 thiên về nén giận, nhịn đau, không để lộ ra ngoài."),
    ("着想", "zhuóxiǎng", "trước tưởng", "động từ", "nghĩ cho, lo cho", "你应该多为别人着想。", "Bạn nên nghĩ cho người khác nhiều hơn.",
     "Động từ, nghĩa là nghĩ cho, lo cho lợi ích của ai đó. Mẫu cố định là 为某人着想. Chú ý cách đọc: âm tiết đầu của từ này đọc thanh hai."),
    ("策划", "cèhuà", "sách hoạch", "động từ", "lên kế hoạch, chuẩn bị, trù tính", "这次活动是他一手策划的。", "Hoạt động lần này do một tay anh ấy lên kế hoạch.",
     "Động từ, nghĩa là lên kế hoạch, trù tính cho một việc. Ngày nay người ta hay nói 策划 cho các hoạt động, sự kiện, chương trình."),
    ("达成", "dáchéng", "đạt thành", "động từ", "đạt được", "双方达成了协议。", "Hai bên đã đạt được thỏa thuận.",
     "Động từ, nghĩa là đạt được, thường đi với 目标, mục tiêu, hoặc 协议, thỏa thuận."),
    ("口气", "kǒuqì", "khẩu khí", "danh từ", "giọng điệu", "他说话的口气很硬。", "Giọng điệu anh ta nói rất cứng.",
     "Danh từ, nghĩa là giọng điệu, thái độ thể hiện qua lời nói. Khác với khẩu khí trong tiếng Việt, thường chỉ chí khí toát ra từ lời nói."),
    ("缓和", "huǎnhé", "hoãn hòa", "tính từ", "dịu đi, hòa hoãn", "两国关系有所缓和。", "Quan hệ hai nước đã dịu đi phần nào.",
     "Nghĩa là dịu đi, bớt căng thẳng; vừa là tính từ vừa là động từ. Trong bài, 使自己的口气缓和下来 là làm cho giọng mình dịu xuống."),
    ("随意", "suíyì", "tùy ý", "tính từ", "tùy ý", "请随意，别客气。", "Cứ tự nhiên, đừng khách sáo.",
     "Tính từ, nghĩa là tùy ý, tùy thích, không gò bó. Âm Hán Việt giống hệt tiếng Việt."),
    ("而已", "éryǐ", "nhi dĩ", "trợ từ", "mà thôi", "我只是随便问问而已。", "Tôi chỉ hỏi chơi vậy thôi.",
     "Trợ từ, đặt ở cuối câu, nghĩa là mà thôi. Đây là điểm ngữ pháp thứ nhất của bài."),
    ("设置", "shèzhì", "thiết trí", "động từ", "thiết lập; cài đặt", "学校根据学生的水平设置课程。", "Nhà trường thiết lập khóa học theo trình độ học sinh.",
     "Động từ, nghĩa là thiết lập, bố trí. Ngoài ra, khi nói về điện thoại, máy tính, 设置 là cài đặt."),
    ("动力", "dònglì", "động lực", "danh từ", "động lực", "兴趣是学习最好的动力。", "Hứng thú là động lực học tập tốt nhất.",
     "Danh từ, nghĩa là động lực, âm Hán Việt và nghĩa giống hệt tiếng Việt."),
    ("固然", "gùrán", "cố nhiên", "liên từ", "tất nhiên, dĩ nhiên; tuy", "这个办法固然好，但是成本太高。", "Cách này tuy tốt, nhưng chi phí quá cao.",
     "Liên từ, nghĩa là tất nhiên, dĩ nhiên, hoặc tuy. Đây là điểm ngữ pháp thứ hai của bài."),
    ("恳切", "kěnqiè", "khẩn thiết", "tính từ", "tha thiết, ân cần, chân thành", "他的态度非常恳切。", "Thái độ của anh ấy vô cùng chân thành, tha thiết.",
     "Tính từ, nghĩa là tha thiết, chân thành, ân cần. Thường đi với 真诚: 真诚恳切."),
    ("无非", "wúfēi", "vô phi", "phó từ", "chẳng qua, chỉ", "他说的无非是些客气话。", "Những gì anh ta nói chẳng qua là mấy lời khách sáo.",
     "Phó từ, nghĩa là chẳng qua, chỉ là. Đây là điểm ngữ pháp thứ ba của bài."),
    ("知音", "zhīyīn", "tri âm", "danh từ", "bạn tri âm", "人生难得一知音。", "Đời người khó tìm được một người tri âm.",
     "Danh từ, nghĩa là bạn tri âm, người hiểu mình. Từ này gắn với câu chuyện Bá Nha gảy đàn, chỉ có Chung Tử Kỳ hiểu được tiếng đàn của ông."),
    ("客户", "kèhù", "khách hộ", "danh từ", "khách hàng", "我们要认真对待每一位客户。", "Chúng ta phải đối xử nghiêm túc với từng khách hàng.",
     "Danh từ, nghĩa là khách hàng, thường dùng trong kinh doanh, dịch vụ."),
    ("持久", "chíjiǔ", "trì cửu", "tính từ", "lâu dài, bền vững", "我们希望建立持久的合作关系。", "Chúng tôi mong xây dựng quan hệ hợp tác lâu dài.",
     "Tính từ, nghĩa là lâu dài, bền bỉ. Trong bài có cụm 难以持久, khó mà bền lâu."),
    ("崩溃", "bēngkuì", "băng hội", "động từ", "sụp đổ, suy sụp", "听到这个消息，她差点儿崩溃了。", "Nghe tin này, cô ấy suýt nữa suy sụp.",
     "Động từ, nghĩa gốc là sụp đổ, tan vỡ; nói về con người là suy sụp tinh thần. Giới trẻ hay nói 我要崩溃了, tôi phát điên mất, như nhân vật tôi trong bài."),
    ("果断", "guǒduàn", "quả đoán", "tính từ", "quả quyết, kiên quyết", "他做事非常果断。", "Anh ấy làm việc rất quả quyết.",
     "Tính từ, nghĩa là quả quyết, dứt khoát, không do dự."),
    ("斩钉截铁", "zhǎndīng-jiétiě", "trảm đinh tiệt thiết", "thành ngữ", "như đinh đóng cột, cương quyết", "他斩钉截铁地拒绝了。", "Anh ấy dứt khoát từ chối.",
     "Thành ngữ. Nghĩa đen là chặt đinh, cắt sắt; nghĩa bóng là nói năng, hành động dứt khoát, cương quyết, giống như đinh đóng cột của tiếng Việt."),
    ("思维", "sīwéi", "tư duy", "danh từ", "ý nghĩ, tư duy, tư tưởng", "学外语能锻炼人的思维。", "Học ngoại ngữ có thể rèn luyện tư duy.",
     "Danh từ, nghĩa là tư duy, cách suy nghĩ, âm Hán Việt giống hệt tiếng Việt."),
    ("搭", "dā", "đáp", "động từ", "ăn khớp, phù hợp", "这件衬衫和裤子很搭。", "Chiếc áo sơ mi này rất hợp với chiếc quần.",
     "Động từ, trong khẩu ngữ nghĩa là hợp, ăn khớp với nhau. Trong bài, 和我的思维很搭 là rất hợp với cách nghĩ của tôi. Ngoài ra, 搭 còn nghĩa là bắc, dựng, như 搭桥, bắc cầu; hoặc đi nhờ, như 搭车, đi nhờ xe."),
    ("执行", "zhíxíng", "chấp hành", "động từ", "chấp hành, tiến hành, thực hiện", "我们必须严格执行公司的规定。", "Chúng ta phải chấp hành nghiêm túc quy định của công ty.",
     "Động từ, nghĩa là chấp hành, thực hiện một kế hoạch, mệnh lệnh hay quy định."),
    ("啥", "shá", "xá", "đại từ", "cái gì, nào (khẩu ngữ)", "你想吃啥？", "Bạn muốn ăn gì?",
     "Đại từ nghi vấn, nghĩa là cái gì, giống 什么, nhưng mang màu sắc khẩu ngữ, phương ngữ miền Bắc Trung Quốc. Trong bài có 为啥, tức là 为什么, tại sao."),
    ("薪水", "xīnshui", "tân thủy", "danh từ", "tiền lương", "他的薪水不太高。", "Lương của anh ấy không cao lắm.",
     "Danh từ, nghĩa là tiền lương. Âm tiết thứ hai đọc nhẹ."),
    ("弊端", "bìduān", "tệ đoan", "danh từ", "mặt hại, mặt hạn chế", "这种做法有很多弊端。", "Cách làm này có rất nhiều mặt hạn chế.",
     "Danh từ, nghĩa là mặt hại, mặt hạn chế của một cách làm, một chế độ. Cẩn thận: tệ đoan trong tiếng Việt là tệ nạn xã hội; còn 弊端 chỉ là nhược điểm, mặt tiêu cực. Từ trái nghĩa là 利, cái lợi."),
    ("拼命", "pīnmìng", "bính mệnh", "phó từ", "dốc sức, ra sức, liều mạng", "他拼命地工作。", "Anh ấy làm việc bán mạng.",
     "Phó từ, nghĩa là dốc hết sức, liều mạng mà làm. Trong bài, 高兴了拼命学一阵子 là lúc vui thì học bán mạng một thời gian."),
    ("搁", "gē", "các", "động từ", "đặt, để; gác lại", "他把书搁在桌子上就出去了。", "Anh ấy đặt sách lên bàn rồi đi ra ngoài.",
     "Động từ, nghĩa là đặt, để; cũng có nghĩa gác lại, bỏ đó. Trong bài, 不高兴了就搁在一边 là không vui thì gác sang một bên."),
    ("颠倒", "diāndǎo", "điên đảo", "động từ", "đảo ngược, lộn ngược", "你把顺序弄颠倒了。", "Bạn làm đảo lộn thứ tự rồi.",
     "Động từ, nghĩa là đảo ngược vị trí trên dưới, trước sau. Cẩn thận: điên đảo trong tiếng Việt thường là hỗn loạn, khốn đốn; còn 前后颠倒 chỉ là trước sau đảo lộn. Âm tiết thứ hai đọc thanh ba."),
    ("权衡", "quánhéng", "quyền hành", "động từ", "cân nhắc, so đo, suy tính", "权衡利弊之后，他决定留下来。", "Sau khi cân nhắc lợi hại, anh ấy quyết định ở lại.",
     "Động từ, nghĩa là cân nhắc, so sánh hơn thiệt. Cẩn thận: quyền hành trong tiếng Việt là quyền lực; còn ở đây, chữ 权 vốn là quả cân, chữ 衡 là cán cân, nên 权衡 là đặt lên cân mà so."),
    ("津津有味", "jīnjīn yǒu wèi", "tân tân hữu vị", "thành ngữ", "thích thú, say mê, ngon lành", "孩子们听故事听得津津有味。", "Bọn trẻ nghe kể chuyện say sưa thích thú.",
     "Thành ngữ, nghĩa là ăn rất ngon lành, hoặc làm việc gì đó rất say sưa, thích thú."),
]

add("bullets", chapter="Từ mới (44 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 5 có 44 từ mới, chia thành 15 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 勉强 (qiǎng) · 着想 (zhuó) · 颠倒 (dǎo) · 薪水 (shui)",
           "Từ dễ nhầm: 机构 · 反感 · 弊端 · 颠倒 · 权衡"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có bốn mươi bốn từ, thầy chia thành mười lăm nhóm nhỏ, mỗi nhóm hai hoặc ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số từ có âm đọc cần chú ý, như 勉强，着想，颠倒，薪水. Thầy sẽ nhắc khi gặp."),
         F(4, "Ngoài ra, có mấy từ Hán Việt rất dễ hiểu nhầm, như 机构，反感，弊端，颠倒，权衡. Nghĩa của chúng trong tiếng Trung khác với tiếng Việt, các bạn nhớ nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

sizes = [3] * 14 + [2]
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
    ("我想学一门外语，迫不及待地想不再依靠翻译，独自阅读原文，哪怕是借助字典勉强查阅呢。",
     "Tôi muốn học một ngoại ngữ. Tôi nóng lòng muốn không còn phải dựa vào bản dịch nữa, tự mình đọc nguyên văn, cho dù là phải nhờ từ điển mà chật vật tra cứu đi nữa.",
     ["门 là lượng từ cho môn học, ngoại ngữ, kỹ thuật: 一门外语，一门课，一门技术. 独自 là một mình, tự mình.",
      "哪怕……呢 nghĩa là cho dù… đi nữa. Câu này cho thấy nhân vật tôi rất quyết tâm: dù phải tra từ điển vất vả cũng muốn đọc bản gốc."]),
    ("我很快找到了一家语言学习机构，它在离我家不远的一栋办公楼上。这天我兴致勃勃地专程前去咨询。",
     "Tôi nhanh chóng tìm được một trung tâm dạy ngoại ngữ, nó nằm trong một tòa nhà văn phòng cách nhà tôi không xa. Hôm ấy, tôi hào hứng đặc biệt đến đó để hỏi thông tin.",
     ["家 là lượng từ cho cửa hàng, công ty, trung tâm: 一家机构. Còn 栋 là lượng từ cho tòa nhà: 一栋办公楼.",
      "前去 là đi đến đó, văn viết. 咨询 là hỏi ý kiến, tư vấn. Các bạn để ý: 兴致勃勃 và 专程 cho thấy lúc đầu nhân vật tôi rất hăm hở."]),
    ("进了门，一位很有修养的女士迎上来，我以为交了学费就能开始快乐而美好的学习了，不料首先面对的是她接连不断的发问：“为什么要学外语？最近有出国计划吗？职业是什么？”",
     "Vừa vào cửa, một quý cô rất lịch sự bước ra đón. Tôi tưởng rằng đóng học phí xong là có thể bắt đầu việc học vui vẻ và tươi đẹp, không ngờ điều đầu tiên phải đối mặt là những câu hỏi dồn dập không ngớt của cô ấy: Tại sao lại học ngoại ngữ? Gần đây có kế hoạch đi nước ngoài không? Nghề nghiệp là gì?",
     ["以为 nghĩa là tưởng rằng, thường dùng khi điều mình nghĩ hóa ra không đúng. 不料 nghĩa là không ngờ, báo hiệu một chuyện bất ngờ ở phía sau.",
      "迎上来 là bước ra đón. 发问 là đặt câu hỏi. Ba câu hỏi liên tiếp làm nhân vật tôi bắt đầu thấy khó chịu."]),
    ("“这很重要吗？”说实在的，她的问题涉及了我的隐私，我很反感，话也变得火药味十足。",
     "Điều đó quan trọng lắm sao? Nói thật, câu hỏi của cô ấy đụng chạm đến đời tư của tôi, tôi rất khó chịu, lời nói cũng trở nên sặc mùi thuốc súng.",
     ["说实在的 nghĩa là nói thật lòng, dùng để chen vào khi nói ra suy nghĩ thật của mình.",
      "火药味十足 là đầy mùi thuốc súng, ví lời nói gay gắt như sắp cãi nhau. 十足 là đầy đủ, mười phần."]),
    ("她极力忍耐着，“是这样，我必须了解学员，为学员着想，帮他策划学习方案，以达成他的目标。”",
     "Cô ấy cố hết sức kiềm chế: Là thế này, tôi phải hiểu học viên, nghĩ cho học viên, giúp họ lên phương án học tập, để đạt được mục tiêu của họ.",
     ["极力 là cố hết sức. 为学员着想 là nghĩ cho học viên, theo mẫu 为某人着想.",
      "以 ở đầu vế cuối nghĩa là để, nhằm: 以达成他的目标, để đạt được mục tiêu của họ. Câu này có trong bài tập bốn, các bạn nhớ cấu trúc nhé."]),
    ("我努力使自己的口气缓和下来：“我没什么具体目标。就是找一个班插班听课，随意学学而已。”",
     "Tôi cố làm cho giọng mình dịu xuống: Tôi chẳng có mục tiêu cụ thể gì cả. Chỉ là tìm một lớp để học chen vào, học tùy thích vậy thôi.",
     ["使 cộng người cộng trạng thái là làm cho ai đó thế nào. 缓和下来 là dịu xuống, 下来 chỉ trạng thái từ mạnh chuyển sang yếu.",
      "插班 là vào học giữa chừng một lớp đang học. 就是……而已 nghĩa là chỉ là… mà thôi, đây chính là điểm ngữ pháp 而已."]),
    ("“可是，我们的班都是根据学员的具体情况设置的，如果您没有具体目标，是学不好一种语言的。”",
     "Nhưng các lớp của chúng tôi đều được thiết lập dựa trên tình hình cụ thể của học viên. Nếu anh không có mục tiêu cụ thể, thì không thể học tốt một ngôn ngữ được.",
     ["是……的 ở đây dùng để nhấn mạnh thái độ khẳng định của người nói: 是学不好一种语言的, chắc chắn là không học tốt được.",
      "Cô nhân viên dùng 您, cách xưng hô lịch sự, nhưng nội dung thì vẫn kiên quyết."]),
    ("没有目标就缺乏动力，这道理我固然懂，可是，我的确说不出她所说的目标。我说我回去想想。",
     "Không có mục tiêu thì thiếu động lực, đạo lý này tất nhiên tôi hiểu, nhưng tôi quả thật không nói ra được cái mục tiêu mà cô ấy nói. Tôi bảo tôi về nghĩ thêm đã.",
     ["固然……可是…… nghĩa là tất nhiên…, nhưng…: thừa nhận một sự thật, rồi chuyển sang ý khác. Đây là điểm ngữ pháp 固然.",
      "的确 là quả thật. 说不出 là không nói ra được. 所说的 là cái mà… nói, 所 cộng động từ làm định ngữ, mang màu sắc văn viết."]),
    ("“您等一下。”她迅速出门，瞬间换来了一位男士。“您学这门语言是为了……”",
     "Anh đợi một chút. Cô ấy nhanh chóng ra ngoài, trong chớp mắt đã đổi sang một người đàn ông. Anh học ngôn ngữ này là để…",
     ["瞬间 là trong nháy mắt. 换来了一位男士 là đổi một người đàn ông khác đến tiếp chuyện.",
      "Câu hỏi bỏ lửng 是为了…… cho thấy người này cũng hỏi đúng câu hỏi đó, nhưng hỏi khéo hơn."]),
    ("他态度和蔼，真诚恳切，我被打动了，跟他滔滔不绝起来：“我喜欢这个国家的文化，学习语言无非是为了看原文电影、读文学作品……”",
     "Ông ấy thái độ hòa nhã, chân thành tha thiết, tôi bị lay động, bắt đầu nói thao thao bất tuyệt với ông ấy: Tôi thích văn hóa của nước này, học ngôn ngữ chẳng qua là để xem phim nguyên bản, đọc tác phẩm văn học…",
     ["和蔼 là hòa nhã, dễ gần. 被打动 là bị lay động, bị thuyết phục. 滔滔不绝 là thao thao bất tuyệt; 起来 ở đây chỉ hành động bắt đầu.",
      "无非是为了…… nghĩa là chẳng qua chỉ là để…. Đây là điểm ngữ pháp 无非, có ý nói nhẹ đi, coi đó là việc đơn giản."]),
    ("“明白了。不想通过翻译，直接进入原文的世界？”“对！”我欢天喜地，终于碰上了知音。",
     "Hiểu rồi. Anh không muốn thông qua bản dịch, mà muốn trực tiếp bước vào thế giới của nguyên tác? – Đúng! Tôi vui mừng hớn hở, cuối cùng cũng gặp được người tri âm.",
     ["欢天喜地 là thành ngữ, vui mừng hớn hở. 碰上 là tình cờ gặp được.",
      "Tác giả dùng từ 知音 hơi cường điệu, để chuẩn bị cho cú bất ngờ ở câu tiếp theo."]),
    ("“我碰到过您这样的客户，可是，光凭兴趣，恐怕难以持久。”我顿时崩溃了，怎么说着说着又绕回来了。",
     "Tôi từng gặp những khách hàng như anh, nhưng chỉ dựa vào hứng thú thì e là khó bền lâu. Tôi lập tức suy sụp, sao nói tới nói lui lại quay về chỗ cũ rồi.",
     ["光凭 nghĩa là chỉ dựa vào, giống 只凭. 难以 là khó mà, văn viết. 顿时 là lập tức, ngay lúc đó.",
      "说着说着 là cấu trúc động từ lặp lại hai lần, giống 走着走着, nghĩa là đang nói thì…, sau đó là một sự việc bất ngờ. Cấu trúc này có trong bài tập hai. 绕回来 là vòng trở lại."]),
    ("我果断地站起来，斩钉截铁地表明要走。",
     "Tôi dứt khoát đứng dậy, cương quyết nói rõ là mình muốn đi.",
     ["果断地 và 斩钉截铁地 đều làm trạng ngữ, nhấn mạnh thái độ dứt khoát. 表明 là bày tỏ rõ ràng.",
      "Đến đây kết thúc phần một của câu chuyện: nhân vật tôi bỏ về vì không chịu nổi những câu hỏi về lý do học."]),
    ("回家后，我不死心，开始在网上找在线学习。后来发现有一家，还真不错，从基础教起，每个句子的语法都详细讲解，不留死角，和我的思维很搭。",
     "Về nhà, tôi vẫn chưa bỏ cuộc, bắt đầu tìm cách học trực tuyến trên mạng. Sau đó phát hiện ra có một nơi thật sự rất tốt: dạy từ cơ bản, ngữ pháp của từng câu đều giảng giải tỉ mỉ, không bỏ sót chỗ nào, rất hợp với cách nghĩ của tôi.",
     ["不死心 là chưa từ bỏ hy vọng, chưa bỏ cuộc. 在线 là trực tuyến. 还真不错 là thật sự không tồi, 还真 ở đây biểu thị hơi bất ngờ.",
      "从基础教起 là dạy từ cơ bản trở đi. 不留死角 là không để lại góc chết, tức là không bỏ sót chỗ nào. 很搭 là rất hợp, cách nói khẩu ngữ."]),
    ("更重要的是心里舒服——没有人硬逼着我执行学习计划，也没人问我为啥要学它，以及我的单位、身份，包括薪水——我就是个语言学习者，你管我这些干吗？",
     "Quan trọng hơn là trong lòng thấy thoải mái: không có ai ép buộc tôi phải thực hiện kế hoạch học tập, cũng không ai hỏi tôi tại sao muốn học nó, rồi cơ quan, thân phận, kể cả tiền lương của tôi. Tôi chỉ là một người học ngôn ngữ thôi, anh quản mấy chuyện đó của tôi làm gì?",
     ["硬逼着 là ép buộc, cưỡng ép. 为啥 là tại sao, khẩu ngữ. 以及 là cùng với, và, nối thêm các thành phần phía sau.",
      "你管我这些干吗？ là câu hỏi tu từ, nghĩa là anh chẳng cần quản những chuyện đó. 干吗 là làm gì, khẩu ngữ. Hai dấu gạch ngang dài dùng để giải thích vì sao trong lòng thấy thoải mái."]),
    ("我的学习方式绝对对学习效果有利，当然弊端也不少：有利的方面如上所说，弊端在于高兴了拼命学一阵子，不高兴了就搁在一边。",
     "Cách học của tôi chắc chắn có lợi cho hiệu quả học tập, tất nhiên mặt hạn chế cũng không ít: mặt có lợi thì như đã nói ở trên, còn mặt hạn chế là lúc vui thì học bán mạng một thời gian, lúc không vui thì gác sang một bên.",
     ["Chú ý 绝对对学习效果有利: chữ 对 thứ nhất thuộc từ 绝对, tuyệt đối; chữ thứ hai là giới từ: 对……有利, có lợi cho….",
      "如上所说 là như đã nói ở trên. 在于 là nằm ở, ở chỗ. Câu này là mẫu câu của bài tập bốn: 当然……也不少，有利的方面……，弊端在于……"]),
    ("有时还前后颠倒，因为后面那课的话题太诱惑我了。但是，利弊权衡，利还是大于弊。因为我总能在忘我的快乐中，津津有味地享受学习。",
     "Có khi còn học đảo lộn trước sau, vì chủ đề của bài phía sau hấp dẫn tôi quá. Nhưng cân nhắc lợi hại, cái lợi vẫn lớn hơn cái hại. Vì tôi luôn có thể say sưa tận hưởng việc học trong niềm vui quên cả bản thân.",
     ["利弊 là lợi và hại. 利还是大于弊 là cái lợi vẫn lớn hơn cái hại, 大于 là lớn hơn, văn viết.",
      "忘我 là quên mình, quá say mê đến mức quên cả bản thân. Câu kết trả lời câu hỏi của đầu bài: học ngoại ngữ có thể đơn giản chỉ vì niềm vui."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 学一门外语需要理由吗？", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 学一门外语需要理由吗？, dài tám trăm ba mươi hai chữ. Bài được cải biên từ một bài báo cùng tên trên báo Thanh niên Bắc Kinh.",
         F(0, "Thầy chia bài thành mười bảy đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 100 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Tóm tắt nội dung", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5)", size=34,
    items=["## 1. “我”学习外语的原因 – lý do học",
           "喜欢这个国家的文化 · 不依靠翻译，看原文电影，阅读原文",
           "## 2. 那家机构认为学习外语必须有什么？",
           "具体目标，比如：出国、职业…… → “我”反感，果断离开",
           "## 3. 最后“我”选择了什么方式学习，为什么？",
           "在线学习 · 从基础教起，详细讲解 · 没有人硬逼着我 · 没有人问我隐私",
           "## 4. “我”的学习方式的利弊",
           "利：心里舒服，享受学习 · 弊：高兴了拼命学，不高兴了就搁在一边，有时前后颠倒"],
    say=["Bài tập năm của sách yêu cầu dựa vào gợi ý để tóm tắt nội dung chính của bài khóa. Chúng ta cùng làm luôn nhé.",
         F(0, "Câu hỏi một: lý do học ngoại ngữ của nhân vật tôi là gì?"),
         F(1, "Thứ nhất, 喜欢这个国家的文化, thích văn hóa của nước đó. Thứ hai, 不依靠翻译，看原文电影，阅读原文, không dựa vào bản dịch, xem phim nguyên bản, đọc nguyên văn."),
         F(2, "Câu hỏi hai: trung tâm ngoại ngữ kia cho rằng học ngoại ngữ thì phải có gì?"),
         F(3, "Phải có 具体目标, mục tiêu cụ thể, ví dụ đi nước ngoài, hay vì nghề nghiệp. Nhân vật tôi thấy khó chịu, nên dứt khoát bỏ về."),
         F(4, "Câu hỏi ba: cuối cùng nhân vật tôi chọn cách học nào, vì sao?"),
         F(5, "Anh ấy chọn 在线学习, học trực tuyến. Vì ở đó dạy từ cơ bản, giảng giải tỉ mỉ, không ai ép anh ấy thực hiện kế hoạch, và cũng không ai hỏi chuyện riêng tư."),
         F(6, "Câu hỏi bốn: cách học của anh ấy có lợi và hại gì?"),
         F(7, "Lợi là trong lòng thoải mái, say sưa tận hưởng việc học. Hại là lúc vui thì học bán mạng, lúc không vui thì gác sang một bên, có khi còn học đảo lộn trước sau. Bố cục này rất có ích khi các bạn tự kể lại bài khóa.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 而已", section="Ngữ pháp 注释", title="1. 而已 éryǐ – mà thôi", size=38,
    items=["Trợ từ, đặt ở cuối câu trần thuật, có ý nói nhẹ đi, coi là chuyện nhỏ",
           "Thường đi với 不过、只、只是、仅 · cũng nói 罢了、就是了",
           "你怎么做的，谁心里都明白，大家不过嘴上说说而已。",
           "他的工作是警察，写小说仅仅是他的业余爱好而已。",
           "我没什么具体目标。就是找一个班插班听课，随意学学而已。"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là trợ từ 而已.",
         F(0, "而已 là trợ từ, đặt ở cuối câu trần thuật, nghĩa là mà thôi. Nó mang ý nói nhẹ đi, coi sự việc là nhỏ, là không đáng kể."),
         F(1, "而已 thường đi cùng các từ 不过，只是，仅仅, ở phía trước. Trong khẩu ngữ, người ta cũng nói 罢了, hoặc 就是了, với nghĩa tương tự."),
         F(2, "Ví dụ một: 你怎么做的，谁心里都明白，大家不过嘴上说说而已。 Anh làm thế nào thì ai cũng biết trong lòng, chẳng qua mọi người chỉ nói ngoài miệng vậy thôi."),
         F(3, "Ví dụ hai: 他的工作是警察，写小说仅仅是他的业余爱好而已。 Công việc của anh ấy là cảnh sát, viết tiểu thuyết chỉ là sở thích lúc rảnh mà thôi."),
         F(4, "Ví dụ ba, lấy từ bài khóa: 我没什么具体目标。就是找一个班插班听课，随意学学而已。 Tôi chẳng có mục tiêu cụ thể gì, chỉ là tìm một lớp học chen vào, học tùy thích vậy thôi.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: dùng 而已 viết lại câu", reveal=True, size=36,
    items=["(1) 他心中的家乡“美食”，在大多数人眼里，是再大众不过的食品了。",
           "Đáp án: ……在大多数人眼里，只是很普通的大众食品而已。",
           "(2) 谁都不想做饭，到外面吃去吧，不就是多花点儿钱吗！",
           "Đáp án: 谁都不想做饭，到外面吃去吧，只不过多花点儿钱而已。",
           "(3) 我仅仅是举个例子，类似的情况还有很多。",
           "Đáp án: 我只是举个例子而已，类似的情况还有很多。"],
    say=[F(0, "Luyện tập: dùng 而已 viết lại câu. Câu một: 他心中的家乡美食，在大多数人眼里，是再大众不过的食品了。 Món ngon quê nhà trong lòng anh ấy, trong mắt đa số người, lại là món ăn bình dân không thể bình dân hơn. Các bạn tạm dừng và thử viết lại nhé."),
         F(1, "Đáp án gợi ý: 在大多数人眼里，只是很普通的大众食品而已。 Trong mắt đa số người, đó chỉ là món ăn bình dân rất bình thường mà thôi."),
         F(2, "Câu hai: 谁都不想做饭，到外面吃去吧，不就是多花点儿钱吗！ Chẳng ai muốn nấu cơm, ra ngoài ăn đi, chẳng phải chỉ tốn thêm chút tiền thôi sao!"),
         F(3, "Đáp án gợi ý: 只不过多花点儿钱而已。 Chẳng qua chỉ tốn thêm chút tiền mà thôi. Câu hỏi tu từ 不就是……吗 được đổi thành câu trần thuật với 只不过……而已."),
         F(4, "Câu ba: 我仅仅是举个例子，类似的情况还有很多。 Tôi chỉ đưa ra một ví dụ, những trường hợp tương tự còn rất nhiều."),
         F(5, "Đáp án gợi ý: 我只是举个例子而已，类似的情况还有很多。 Tôi chỉ đưa ra một ví dụ mà thôi. Chú ý: 而已 đặt ở cuối vế câu cần nói nhẹ đi.")])

add("bullets", chapter="Ngữ pháp: 固然", section="Ngữ pháp 注释", title="2. 固然 gùrán – tất nhiên, tuy", size=36,
    items=["Liên từ, xác nhận một sự thật; đứng ở vế trước",
           "## (1) Vế sau chuyển ý, nêu sự thật đối lập – đi với 可是、但是、却、然而",
           "没有目标就缺乏动力，这道理我固然懂，可是，我的确说不出她所说的目标。",
           "这么做，好固然是好，可是又费时间，成本又高，肯定不行。",
           "## (2) Vế sau thuận ý, thừa nhận thêm một sự thật – thường đi với 也",
           "考上大学固然好，没考上大学也不是就没有出路了。",
           "上世纪末兴起的积极心理学运动，固然有心理学自身发展要求的原因，另一方面也是时代发展的必然。"],
    say=["Điểm ngữ pháp thứ hai là liên từ 固然.",
         F(0, "固然 dùng để xác nhận một sự thật, tiếng Việt dịch là tất nhiên, dĩ nhiên, hoặc tuy. Nó đứng ở vế câu phía trước."),
         F(1, "Cách dùng thứ nhất: vế sau chuyển ý, nêu ra một sự thật đối lập. Vế sau thường có 可是，但是，却，然而."),
         F(2, "Ví dụ một, lấy từ bài khóa: 没有目标就缺乏动力，这道理我固然懂，可是，我的确说不出她所说的目标。 Không có mục tiêu thì thiếu động lực, đạo lý này tất nhiên tôi hiểu, nhưng tôi quả thật không nói ra được mục tiêu đó."),
         F(3, "Ví dụ hai: 这么做，好固然是好，可是又费时间，成本又高，肯定不行。 Làm như vậy, tốt thì tốt thật, nhưng vừa tốn thời gian, chi phí lại cao, chắc chắn không được."),
         F(4, "Cách dùng thứ hai: vế sau thuận ý, thừa nhận thêm một sự thật khác. Ý chuyển rất nhẹ, trọng tâm nằm ở vế sau. Vế sau thường đi với 也, đôi khi dùng 但是 hoặc 可是."),
         F(5, "Ví dụ ba: 考上大学固然好，没考上大学也不是就没有出路了。 Thi đỗ đại học tất nhiên là tốt, nhưng không đỗ đại học cũng đâu phải là hết đường."),
         F(6, "Ví dụ bốn: 上世纪末兴起的积极心理学运动，固然有心理学自身发展要求的原因，另一方面也是时代发展的必然。 Phong trào tâm lý học tích cực nổi lên cuối thế kỷ trước, tất nhiên có nguyên nhân từ yêu cầu phát triển của bản thân ngành tâm lý học, mặt khác cũng là tất yếu của sự phát triển thời đại.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: hoàn thành câu với 固然", reveal=True, size=38,
    items=["(1) 搬家以后新家离单位固然是远了许多，可是……",
           "Đáp án: ……可是房子大了，周围的环境也好多了。",
           "(2) 谁有意见大胆地提，说得对，固然好，说错了，……",
           "Đáp án: ……说错了也没关系。",
           "(3) 屋里挂张画儿固然不错，可并……，要是一点儿美感都没有的画，不挂也罢。",
           "Đáp án: ……可并不是什么画儿都可以挂……"],
    say=[F(0, "Luyện tập: hoàn thành câu. Câu một: 搬家以后新家离单位固然是远了许多，可是…… Sau khi chuyển nhà, nhà mới tất nhiên là xa cơ quan hơn nhiều, nhưng sao? Các bạn tạm dừng và thử hoàn thành câu nhé."),
         F(1, "Đáp án gợi ý: 可是房子大了，周围的环境也好多了。 Nhưng nhà rộng hơn, môi trường xung quanh cũng tốt hơn nhiều. Đây là cách dùng thứ nhất, vế sau chuyển ý."),
         F(2, "Câu hai: 谁有意见大胆地提，说得对，固然好，说错了，…… Ai có ý kiến thì cứ mạnh dạn nêu ra, nói đúng thì tất nhiên tốt, nói sai thì sao?"),
         F(3, "Đáp án gợi ý: 说错了也没关系。 Nói sai cũng không sao. Đây là cách dùng thứ hai, vế sau đi với 也."),
         F(4, "Câu ba: 屋里挂张画儿固然不错，可并……，要是一点儿美感都没有的画，不挂也罢。 Treo một bức tranh trong phòng tất nhiên là hay, nhưng mà…, nếu là bức tranh chẳng có chút thẩm mỹ nào thì không treo cũng được."),
         F(5, "Đáp án gợi ý: 可并不是什么画儿都可以挂。 Nhưng không phải bức tranh nào cũng treo được. 不挂也罢 nghĩa là không treo cũng chẳng sao.")])

add("bullets", chapter="Ngữ pháp: 无非", section="Ngữ pháp 注释", title="3. 无非 wúfēi – chẳng qua, chỉ là", size=36,
    items=["Phó từ: không vượt quá một phạm vi nào đó, nghĩa là 只、不过",
           "Có ý nói nhẹ đi, coi sự việc là nhỏ, là đơn giản",
           "他这么努力地工作，无非想多挣些钱，让妻子、孩子生活得更舒适。",
           "我喜欢这个国家的文化，学习语言无非是为了看原文电影、读文学作品……",
           "我们把汉语口语称作“说的汉语”，把汉语书面语称作“看的汉语”，无非是强调汉语两种不同的语言形式具有不同的特性和使用场合。"],
    say=["Điểm ngữ pháp thứ ba là phó từ 无非.",
         F(0, "无非 biểu thị không vượt quá một phạm vi nào đó, nghĩa giống 只是 và 不过, tiếng Việt dịch là chẳng qua, chỉ là."),
         F(1, "Giống 而已, 无非 cũng có ý nói nhẹ đi, coi sự việc là nhỏ, là đơn giản. Hai từ này có thể dùng cùng nhau: 无非……而已."),
         F(2, "Ví dụ một: 他这么努力地工作，无非想多挣些钱，让妻子、孩子生活得更舒适。 Anh ấy làm việc chăm chỉ như vậy, chẳng qua là muốn kiếm thêm chút tiền, để vợ con sống thoải mái hơn."),
         F(3, "Ví dụ hai, lấy từ bài khóa: 我喜欢这个国家的文化，学习语言无非是为了看原文电影、读文学作品。 Tôi thích văn hóa nước này, học ngôn ngữ chẳng qua là để xem phim nguyên bản, đọc tác phẩm văn học."),
         F(4, "Ví dụ ba: 我们把汉语口语称作说的汉语，把汉语书面语称作看的汉语，无非是强调汉语两种不同的语言形式具有不同的特性和使用场合。 Chúng ta gọi khẩu ngữ là tiếng Trung để nói, gọi văn viết là tiếng Trung để đọc, chẳng qua là để nhấn mạnh hai hình thức ngôn ngữ này có đặc tính và hoàn cảnh sử dụng khác nhau.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: dùng 无非 viết lại câu", reveal=True, size=36,
    items=["(1) 父母们在一起也实在没什么好谈的，就是孩子的成长、教育问题。",
           "Đáp án: 父母们在一起谈的，无非是孩子的成长、教育问题。",
           "(2) 他的菜谱特别单调，只有西红柿炒鸡蛋，偶尔还可能有黄瓜炒鸡蛋。",
           "Đáp án: 他的菜谱特别单调，无非是西红柿炒鸡蛋，偶尔还可能有黄瓜炒鸡蛋。",
           "(3) 人类的穿戴只不过十几年、几十年为一周期地来回换，来回时髦。",
           "Đáp án: 人类的穿戴无非是十几年、几十年为一周期地来回换，来回时髦。"],
    say=[F(0, "Luyện tập: dùng 无非 viết lại câu. Câu một: 父母们在一起也实在没什么好谈的，就是孩子的成长、教育问题。 Các bậc cha mẹ ngồi với nhau thật ra cũng chẳng có gì để nói, chỉ là chuyện con cái lớn lên và học hành. Các bạn thử viết lại nhé."),
         F(1, "Đáp án gợi ý: 父母们在一起谈的，无非是孩子的成长、教育问题。 Điều các bậc cha mẹ nói với nhau, chẳng qua là chuyện con cái lớn lên và học hành."),
         F(2, "Câu hai: 他的菜谱特别单调，只有西红柿炒鸡蛋，偶尔还可能有黄瓜炒鸡蛋。 Thực đơn của anh ấy rất đơn điệu, chỉ có trứng xào cà chua, thỉnh thoảng có thể có trứng xào dưa chuột."),
         F(3, "Đáp án gợi ý: thay 只有 bằng 无非是: 他的菜谱特别单调，无非是西红柿炒鸡蛋。 Thực đơn của anh ấy rất đơn điệu, chẳng qua chỉ là trứng xào cà chua."),
         F(4, "Câu ba: 人类的穿戴只不过十几年、几十年为一周期地来回换，来回时髦。 Cách ăn mặc của con người chẳng qua cứ mười mấy năm, vài chục năm lại quay vòng một lần, mốt cũ lại thành mốt mới."),
         F(5, "Đáp án gợi ý: thay 只不过 bằng 无非是: 人类的穿戴无非是十几年、几十年为一周期地来回换，来回时髦。")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 专程 – 专门", section="Phân biệt từ 词语辨析", title="Phân biệt 专程 và 专门",
    common="Giống nhau: đều chỉ cố ý, đặc biệt làm một việc. Ví dụ: 这次到上海来，我是专程/专门来看你的。",
    cols=[{"head": "专程",
           "lines": ["(1) Chỉ dùng cho hành động phải đi một chặng đường, nhấn mạnh sự trịnh trọng",
                     "Đúng: 他专程来机场送你。",
                     "(2) Không có nghĩa giới hạn phạm vi",
                     "(3) Không làm tính từ",
                     "Sai: 他专程研究中国文学。"]},
          {"head": "专门",
           "lines": ["(1) Dùng cho cả đi lại lẫn mọi hành động khác",
                     "Đúng: 这个礼物是专门给你买的。",
                     "(2) Chỉ giới hạn trong một phạm vi",
                     "Đúng: 会议专门讨论了人事问题。",
                     "(3) Tính từ, đứng trước danh từ",
                     "Đúng: 他们是电脑方面的专门人才。"]}],
    say=["Tiếp theo là phần phân biệt từ: 专程 và 专门. Hai từ này đều có chữ 专, nên học sinh rất hay dùng lẫn lộn.",
         "Điểm giống nhau: cả hai đều chỉ việc cố ý, đặc biệt làm một việc gì đó. Ví dụ: 这次到上海来，我是专程来看你的, hoặc 我是专门来看你的, đều đúng. Lần này đến Thượng Hải, tôi đặc biệt đến để thăm bạn.",
         F(0, "Điểm khác thứ nhất. 专程 chỉ dùng cho những hành động phải đi một chặng đường, và nhấn mạnh thái độ trịnh trọng, nghiêm túc. Chữ 程 chính là chặng đường, như trong 路程. Ví dụ: 他专程来机场送你。 Anh ấy đặc biệt đến sân bay tiễn bạn."),
         F(1, "Còn 专门 thì ngoài hành động đi lại, còn dùng được cho mọi hành động khác. Ví dụ: 这个礼物是专门给你买的，不知道你喜欢不喜欢。 Món quà này mua riêng cho bạn, không biết bạn có thích không. Mua quà không phải là đi một chặng đường, nên không dùng 专程."),
         F(1, "Điểm khác thứ hai. 专门 còn là phó từ biểu thị hành động chỉ giới hạn trong một phạm vi. Ví dụ: 这次会议专门讨论了公司的人事问题。 Cuộc họp lần này chỉ chuyên thảo luận vấn đề nhân sự của công ty. 专程 không có nghĩa này."),
         F(1, "Điểm khác thứ ba. 专门 còn là tính từ, chỉ người chuyên làm một việc hay chuyên nghiên cứu một ngành, đứng trước danh từ. Ví dụ: 他们都是电脑方面的专门人才。 Họ đều là nhân tài chuyên về máy tính. 专程 không có cách dùng này."),
         F(0, "Vì vậy câu 他专程研究中国文学 là sai, vì nghiên cứu không phải là đi một chặng đường. Phải nói 他专门研究中国文学。"),
         "Mẹo nhớ: 专程 gắn với chữ 程, chặng đường, nên chỉ dùng khi phải đi đâu đó; còn 专门 có phạm vi dùng rộng hơn nhiều."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: Đúng hay sai?", reveal=True, size=36,
    items=["(1) 他专程研究中国文学，发表了一些这方面的论文。",
           "Đáp án: Sai – nghiên cứu không phải đi một chặng đường. Sửa: 他专门研究中国文学。",
           "(2) 他们为国家培养了很多相关学科的专门人才。",
           "Đáp án: Đúng – 专门 là tính từ, đứng trước danh từ 人才.",
           "(3) 今天是我的生日，妈妈专程做了我喜欢吃的饭菜。",
           "Đáp án: Sai – nấu ăn không phải đi lại. Sửa: 妈妈专门做了我喜欢吃的饭菜。",
           "(4) 昨天同事们专门举行了一个晚会欢迎我。",
           "Đáp án: Đúng – 专门 dùng được cho mọi hành động."],
    say=[F(0, "Bây giờ chúng ta làm thử: phán đoán đúng sai. Câu một: 他专程研究中国文学，发表了一些这方面的论文。 Anh ấy chuyên nghiên cứu văn học Trung Quốc, đã đăng một số bài luận về mảng này. Đúng hay sai? Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: sai. Nghiên cứu không phải là hành động đi một chặng đường, nên không dùng 专程. Phải sửa thành 他专门研究中国文学。"),
         F(2, "Câu hai: 他们为国家培养了很多相关学科的专门人才。 Họ đã đào tạo cho đất nước rất nhiều nhân tài chuyên môn thuộc các ngành liên quan."),
         F(3, "Đáp án: đúng. Ở đây 专门 là tính từ, đứng trước danh từ 人才, nghĩa là chuyên môn."),
         F(4, "Câu ba: 今天是我的生日，妈妈专程做了我喜欢吃的饭菜。 Hôm nay là sinh nhật tôi, mẹ đặc biệt nấu những món tôi thích ăn."),
         F(5, "Đáp án: sai. Nấu ăn ở nhà không phải đi đâu cả, nên phải dùng 专门: 妈妈专门做了我喜欢吃的饭菜。"),
         F(6, "Câu bốn: 昨天同事们专门举行了一个晚会欢迎我。 Hôm qua các đồng nghiệp đặc biệt tổ chức một buổi tiệc tối để chào đón tôi."),
         F(7, "Đáp án: đúng. 专门 dùng được cho mọi hành động, kể cả tổ chức tiệc.")])

# ======================= MỞ RỘNG: CÂU THIẾU THÀNH PHẦN =======================
add("bullets", chapter="Mở rộng: câu thiếu thành phần", section="Mở rộng 扩展", title="Câu sai: thiếu thành phần (成分残缺)", size=34,
    items=["Lược bỏ phần không được lược bỏ → câu không hoàn chỉnh, diễn đạt không chính xác",
           "## (1) Thiếu chủ ngữ (主语残缺)",
           "Sai: 他向国家捐献出了一张祖传的字画，具有极高的研究、保存价值。",
           "Sửa: ……，这张字画具有极高的研究、保存价值。 (vế sau ngầm đổi chủ ngữ)",
           "## (2) Thiếu vị ngữ (谓语残缺)",
           "Sai: 我们已办理了婚姻登记手续，我们真的夫妻了。",
           "Sửa: ……，我们真的是夫妻了。 / 我们是真的夫妻了。"],
    say=["Bây giờ chúng ta sang phần mở rộng của sách. Quyển này không có mục tu từ riêng, thay vào đó là một kỹ năng rất thực dụng: nhận biết câu sai. Hôm nay là loại câu sai do thiếu thành phần, tiếng Trung gọi là 成分残缺.",
         F(0, "成分残缺 là khi trong câu lược bỏ mất phần không được phép lược bỏ, khiến cấu trúc câu không hoàn chỉnh, và ý diễn đạt không chính xác."),
         F(1, "Loại thứ nhất: thiếu chủ ngữ, 主语残缺."),
         F(2, "Câu sai: 他向国家捐献出了一张祖传的字画，具有极高的研究、保存价值。 Anh ấy hiến tặng nhà nước một bức tranh chữ gia truyền, có giá trị nghiên cứu và bảo tồn rất cao."),
         F(3, "Vế trước chủ ngữ là 他, vế sau chủ ngữ phải là bức tranh, nhưng câu đã ngầm đổi chủ ngữ mà không nói ra. Phải sửa: 这张字画具有极高的研究、保存价值。"),
         F(4, "Loại thứ hai: thiếu vị ngữ, 谓语残缺."),
         F(5, "Câu sai: 我们已办理了婚姻登记手续，我们真的夫妻了。 Vế sau thiếu động từ vị ngữ 是. Phải sửa thành 我们真的是夫妻了, hoặc 我们是真的夫妻了。 Chúng tôi thật sự là vợ chồng rồi.")])

add("bullets", section="Mở rộng 扩展", title="Câu sai: thiếu tân ngữ, bổ ngữ, từ liên kết", size=34,
    items=["## (3) Thiếu tân ngữ (宾语残缺)",
           "Sai: 我们将提前做好各项筹备工作，最终实现举办一届“有特色、高水平”奥运会。",
           "Sửa: ……最终实现举办一届“有特色、高水平”奥运会的目标。",
           "## (4) Thiếu bổ ngữ (补语残缺)",
           "Sai: 我读杂志的时候，看一张广告，有话剧，我决定买两张票。 → Sửa: 看到一张广告",
           "## (5) Thiếu từ liên kết (关联词语残缺)",
           "Sai: 就算肉再好吃，你也不准吃太多，以后更胖了。 → Sửa: ……，不然以后更胖了。"],
    say=[F(0, "Loại thứ ba: thiếu tân ngữ, 宾语残缺."),
         F(1, "Câu sai: 我们将提前做好各项筹备工作，最终实现举办一届有特色、高水平奥运会。 Chúng tôi sẽ làm tốt trước các công tác chuẩn bị, cuối cùng thực hiện việc tổ chức một kỳ Thế vận hội có bản sắc, trình độ cao."),
         F(2, "Vì trước tân ngữ có một định ngữ rất dài, người viết nhầm một phần của định ngữ là tân ngữ, nên câu thiếu tân ngữ thật sự. Phải sửa: 最终实现举办一届有特色、高水平奥运会的目标。 Thực hiện mục tiêu là tổ chức một kỳ Thế vận hội như vậy."),
         F(3, "Loại thứ tư: thiếu bổ ngữ, 补语残缺."),
         F(4, "Câu sai: 我读杂志的时候，看一张广告，有话剧，我决定买两张票。 Cụm 看一张广告 thiếu bổ ngữ kết quả. Phải sửa thành 看到一张广告, nhìn thấy một mẩu quảng cáo."),
         F(5, "Loại thứ năm: thiếu từ liên kết, 关联词语残缺."),
         F(6, "Câu sai: 就算肉再好吃，你也不准吃太多，以后更胖了。 Theo ý câu, trước vế chỉ kết quả phải thêm 不然: 不然以后更胖了。 Dù thịt có ngon đến đâu, con cũng không được ăn nhiều, nếu không sau này sẽ càng béo.")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chỉ ra lỗi và sửa lại (1)", reveal=True, size=36,
    items=["(1) 为了写好汉字，他每天抄写一篇短文，养成了书写规范、端正、整洁。",
           "Đáp án: Thiếu tân ngữ → ……养成了书写规范、端正、整洁的习惯。",
           "(2) 他边走边想，非常投入，突然路旁的河里有人喊“救命！”",
           "Đáp án: Thiếu vị ngữ → ……突然听到路旁的河里有人喊“救命！”",
           "(3) 他的习惯是一边吃早饭，一边看报纸，对身体不好。",
           "Đáp án: Thiếu chủ ngữ → ……一边看报纸，这对身体不好。"],
    say=[F(0, "Luyện tập: chỉ ra lỗi của các câu sau và đề xuất cách sửa. Câu một: 为了写好汉字，他每天抄写一篇短文，养成了书写规范、端正、整洁。 Để viết đẹp chữ Hán, mỗi ngày anh ấy chép một bài văn ngắn, đã hình thành viết chuẩn, ngay ngắn, sạch sẽ. Câu này thiếu gì? Các bạn tạm dừng và suy nghĩ nhé."),
         F(1, "Đáp án: thiếu tân ngữ. 养成 phải đi với tân ngữ như 习惯. Sửa: 养成了书写规范、端正、整洁的习惯。 Đã hình thành thói quen viết chữ chuẩn, ngay ngắn, sạch sẽ."),
         F(2, "Câu hai: 他边走边想，非常投入，突然路旁的河里有人喊救命！ Anh ấy vừa đi vừa nghĩ, rất tập trung, đột nhiên dưới con sông bên đường có người kêu cứu."),
         F(3, "Đáp án: thiếu vị ngữ. Chủ ngữ 他 cần một động từ như 听到. Sửa: 突然听到路旁的河里有人喊救命！ Đột nhiên anh ấy nghe thấy có người kêu cứu dưới sông."),
         F(4, "Câu ba: 他的习惯是一边吃早饭，一边看报纸，对身体不好。 Thói quen của anh ấy là vừa ăn sáng vừa đọc báo, không tốt cho sức khỏe."),
         F(5, "Đáp án: thiếu chủ ngữ ở vế cuối. Cái không tốt cho sức khỏe là thói quen đó, chứ không phải tờ báo. Sửa: 这对身体不好, hoặc 这种习惯对身体不好。")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chỉ ra lỗi và sửa lại (2)", reveal=True, size=36,
    items=["(4) 经过专家组分析论证，排除了人为破坏因素导致事故发生的可能性。",
           "Đáp án: Thiếu chủ ngữ → 专家组经过分析论证，排除了……",
           "(5) 我觉得她好棒啊，居然把一件旧牛仔裤改造了一个洋气又实用的背包。",
           "Đáp án: Thiếu bổ ngữ → ……把一件旧牛仔裤改造成了一个洋气又实用的背包。"],
    say=[F(0, "Câu bốn: 经过专家组分析论证，排除了人为破坏因素导致事故发生的可能性。 Qua phân tích luận chứng của tổ chuyên gia, đã loại trừ khả năng sự cố do yếu tố phá hoại của con người gây ra. Câu này thiếu gì?"),
         F(1, "Đáp án: thiếu chủ ngữ. Vì có giới từ 经过 ở đầu câu, nên 专家组 trở thành một phần của trạng ngữ, câu không còn chủ ngữ. Sửa: bỏ 经过 ra phía sau: 专家组经过分析论证，排除了人为破坏因素导致事故发生的可能性。"),
         F(2, "Câu năm: 我觉得她好棒啊，居然把一件旧牛仔裤改造了一个洋气又实用的背包。 Tôi thấy cô ấy giỏi thật, vậy mà biến một chiếc quần bò cũ thành một chiếc ba lô vừa sành điệu vừa tiện dụng."),
         F(3, "Đáp án: thiếu bổ ngữ. Sau 改造 phải có bổ ngữ kết quả 成, tức là cải tạo thành cái gì: 把一件旧牛仔裤改造成了一个洋气又实用的背包。 Mẹo: khi sửa câu sai, hãy tìm chủ ngữ, vị ngữ, tân ngữ trước, rồi mới xét đến bổ ngữ và từ liên kết.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ có dấu chấm", size=40,
    items=["拼命 (命) → 救命 · 生命 · 寿命 · 命运",
           "忍耐 (耐) → 耐心 · 耐用 · 耐力 · 耐寒",
           "缓和 (缓) → 缓慢 · 缓解 · 缓冲 · 延缓",
           "客户 (户) → 用户 · 住户 · 账户 · 户口",
           "思维 (思) → 思考 · 思想 · 思念 · 构思"],
    say=["Phần luyện tập. Bài tập một: mô phỏng ví dụ, viết thêm các từ có chứa chữ được đánh dấu chấm.",
         F(0, "Ví dụ mẫu: 拼命, chữ được đánh dấu là chữ thứ hai. Ta có 救命，生命，寿命，命运. Tức là cứu mạng, sinh mệnh, tuổi thọ, và vận mệnh."),
         F(1, "忍耐, chữ được đánh dấu là chữ thứ hai, nghĩa là chịu được. Ta có 耐心，耐用，耐力，耐寒. Tức là kiên nhẫn, bền, sức bền, và chịu lạnh."),
         F(2, "缓和, chữ được đánh dấu là chữ đầu, nghĩa là chậm. Ta có 缓慢，缓解，缓冲，延缓. Tức là chậm chạp, làm dịu, giảm xóc, và trì hoãn."),
         F(3, "客户, chữ được đánh dấu là chữ thứ hai, nghĩa là hộ, nhà. Ta có 用户，住户，账户，户口. Tức là người dùng, hộ gia đình, tài khoản, và hộ khẩu."),
         F(4, "思维, chữ được đánh dấu là chữ đầu, nghĩa là nghĩ. Ta có 思考，思想，思念，构思. Tức là suy nghĩ, tư tưởng, nhớ nhung, và lên ý tưởng.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (1)", reveal=True, size=36,
    items=["(1) 为孩子的未来考虑，家长应该培养孩子独立的能力。（为……着想）",
           "Đáp án: 家长应该为孩子的未来着想，培养孩子独立的能力。",
           "(2) 商店增加了很多手推车，是为了便于顾客购物。（以）",
           "Đáp án: 商店增加了很多手推车，以方便顾客购物。",
           "(3) 他只不过是不小心碰了你一下，你干吗生那么大的气啊？（无非）",
           "Đáp án: 他无非是不小心碰了你一下，你干吗生那么大的气啊？"],
    say=[F(0, "Bài tập hai: dùng từ hoặc cấu trúc cho sẵn để viết lại câu. Câu một, dùng 为某人着想: 为孩子的未来考虑，家长应该培养孩子独立的能力。 Vì tương lai của con, cha mẹ nên bồi dưỡng khả năng tự lập cho con. Các bạn tạm dừng và thử viết lại nhé."),
         F(1, "Đáp án: 家长应该为孩子的未来着想，培养孩子独立的能力。 Cha mẹ nên nghĩ cho tương lai của con, bồi dưỡng khả năng tự lập cho con."),
         F(2, "Câu hai, dùng 以, nghĩa là để: 商店增加了很多手推车，是为了便于顾客购物。 Cửa hàng tăng thêm nhiều xe đẩy, là để khách hàng tiện mua sắm."),
         F(3, "Đáp án: 商店增加了很多手推车，以方便顾客购物。 Giống câu trong bài khóa: 以达成他的目标. 以 đứng đầu vế sau, chỉ mục đích, mang màu sắc văn viết."),
         F(4, "Câu ba, dùng 无非: 他只不过是不小心碰了你一下，你干吗生那么大的气啊？ Anh ấy chỉ vô ý đụng vào bạn một cái, sao bạn lại giận dữ đến thế?"),
         F(5, "Đáp án: thay 只不过 bằng 无非: 他无非是不小心碰了你一下，你干吗生那么大的气啊？")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (2)", reveal=True, size=36,
    items=["(4) 他并不比别人聪明，只是比别人更努力一些。（而已）",
           "Đáp án: 他并不比别人聪明，只是比别人更努力一些而已。",
           "(5) 这个方法好是好，可实施起来太难了。（固然）",
           "Đáp án: 这个方法固然好，可实施起来太难了。",
           "(6) 周末去郊外玩儿，走了一段时间后，我发现自己迷路了。（……着……着）",
           "Đáp án: 周末去郊外玩儿，走着走着，我发现自己迷路了。"],
    say=[F(0, "Câu bốn, dùng 而已: 他并不比别人聪明，只是比别人更努力一些。 Anh ấy chẳng thông minh hơn người khác, chỉ là chăm chỉ hơn một chút."),
         F(1, "Đáp án: thêm 而已 vào cuối câu: 只是比别人更努力一些而已。 Chỉ là chăm chỉ hơn người khác một chút mà thôi."),
         F(2, "Câu năm, dùng 固然: 这个方法好是好，可实施起来太难了。 Cách này tốt thì tốt thật, nhưng thực hiện thì khó quá."),
         F(3, "Đáp án: 这个方法固然好，可实施起来太难了。 Cách này tất nhiên là tốt, nhưng thực hiện thì khó quá. Mẫu 好是好 có thể đổi thành 固然."),
         F(4, "Câu sáu, dùng cấu trúc động từ lặp lại như 说着说着: 周末去郊外玩儿，走了一段时间后，我发现自己迷路了。 Cuối tuần đi chơi ngoại ô, đi được một lúc, tôi phát hiện mình bị lạc đường."),
         F(5, "Đáp án: 周末去郊外玩儿，走着走着，我发现自己迷路了。 Đi mãi đi mãi, tôi phát hiện mình bị lạc. Giống câu trong bài: 怎么说着说着又绕回来了。")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (1)", reveal=True, size=34,
    items=["## Từ cho sẵn: 兴致勃勃 · 迫不及待 · 啥 · 接连 · 栋",
           "朋友邀请我参加他们的新年晚会，他住在离我家不远的一___居民楼上。我___地前去参加。晚会上惊喜___不断，不但有好吃的、好喝的，朋友还为每位客人准备了一份礼物。我很想知道里边是___东西，就___地打开包装，原来是我最喜欢吃的巧克力……",
           "Đáp án: 栋 · 兴致勃勃 · 接连 · 啥 · 迫不及待"],
    say=[F(0, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn một có năm từ: 兴致勃勃，迫不及待，啥，接连，栋."),
         F(1, "朋友邀请我参加他们的新年晚会，他住在离我家不远的一什么居民楼上。我什么地前去参加。晚会上惊喜什么不断，不但有好吃的、好喝的，朋友还为每位客人准备了一份礼物。我很想知道里边是什么东西，就什么地打开包装，原来是我最喜欢吃的巧克力。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 一栋居民楼，我兴致勃勃地前去参加，惊喜接连不断，里边是啥东西，就迫不及待地打开包装。 Bạn tôi mời tôi dự tiệc mừng năm mới, anh ấy sống trong một tòa chung cư không xa nhà tôi. Tôi hào hứng đến dự. Bữa tiệc có hết bất ngờ này đến bất ngờ khác, bạn tôi còn chuẩn bị quà cho mỗi vị khách. Tôi rất muốn biết bên trong là gì, nên nóng lòng mở ngay, hóa ra là sô-cô-la mà tôi thích nhất.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (2)", reveal=True, size=34,
    items=["## Từ cho sẵn: 依靠 · 动力 · 设置 · 持久 · 执行",
           "学习一门外语，光___热情是远远不够的，那样的话，恐怕难以___。我们还应该根据自身的情况___短期和长期的学习目标，制定详细的学习计划，有了目标就有了学习的___。……最后，严格___学习计划也是非常重要的。",
           "Đáp án: 依靠 · 持久 · 设置 · 动力 · 执行"],
    say=[F(0, "Đoạn hai có năm từ: 依靠，动力，设置，持久，执行."),
         F(1, "学习一门外语，光什么热情是远远不够的，那样的话，恐怕难以什么。我们还应该根据自身的情况什么短期和长期的学习目标，制定详细的学习计划，有了目标就有了学习的什么。最后，严格什么学习计划也是非常重要的。 Các bạn điền thử nhé."),
         F(2, "Đáp án: 光依靠热情，恐怕难以持久，设置短期和长期的学习目标，有了学习的动力，严格执行学习计划。 Học một ngoại ngữ, chỉ dựa vào nhiệt tình thì không đủ, e là khó bền lâu. Chúng ta còn phải đặt ra mục tiêu ngắn hạn và dài hạn, có mục tiêu thì có động lực. Cuối cùng, nghiêm túc thực hiện kế hoạch học tập cũng rất quan trọng."),
         "Các bạn thấy không, đoạn văn này chính là lời khuyên của cô nhân viên trung tâm trong bài khóa: học ngoại ngữ thì nên có mục tiêu. Còn các bạn đồng ý với ai hơn?"])

add("bullets", section="Luyện tập 练习", title="Bài tập 4: Đọc đoạn văn, mô phỏng đặt câu", reveal=True, size=34,
    items=["她极力忍耐着，“是这样，我必须了解学员，为学员着想，帮他策划学习方案，以达成他的目标。”",
           "Đáp án: 球队教练说：“我必须了解每一位队员，为队员着想，帮他们制订训练计划，以提高全队的水平。”",
           "我的学习方式绝对对学习效果有利，当然弊端也不少：有利的方面如上所说，弊端在于高兴了拼命学一阵子，不高兴了就搁在一边。",
           "Đáp án: 那个人绝对是个很好的人，当然缺点也不少，好的方面是热情、乐于助人，缺点在于脾气太急，说话太直。"],
    say=[F(0, "Bài tập bốn: đọc đoạn văn, rồi mô phỏng để đặt câu. Câu mẫu một: 她极力忍耐着，是这样，我必须了解学员，为学员着想，帮他策划学习方案，以达成他的目标。 Đề bài yêu cầu viết lời của huấn luyện viên đội bóng theo khung: 我必须做什么，为某人着想，帮某人做什么，以达到什么目的。 Các bạn thử viết nhé."),
         F(1, "Đáp án gợi ý: 球队教练说：我必须了解每一位队员，为队员着想，帮他们制订训练计划，以提高全队的水平。 Huấn luyện viên đội bóng nói: Tôi phải hiểu từng cầu thủ, nghĩ cho cầu thủ, giúp họ lập kế hoạch tập luyện, để nâng cao trình độ của cả đội."),
         F(2, "Câu mẫu hai: 我的学习方式绝对对学习效果有利，当然弊端也不少：有利的方面如上所说，弊端在于高兴了拼命学一阵子，不高兴了就搁在一边。 Đề bài yêu cầu viết về một người theo khung: 那个人绝对是个很好的人，当然……也不少，好的方面是……，缺点在于……"),
         F(3, "Đáp án gợi ý: 那个人绝对是个很好的人，当然缺点也不少，好的方面是热情、乐于助人，缺点在于脾气太急，说话太直。 Người đó chắc chắn là người rất tốt, tất nhiên khuyết điểm cũng không ít: mặt tốt là nhiệt tình, thích giúp người; khuyết điểm là tính nóng nảy, nói năng quá thẳng.")])

add("bullets", section="Luyện tập 练习", title="Mở rộng 扩展: các cặp từ gần nghĩa", size=36,
    items=["安详 – 祥和 điềm tĩnh, an lành · 报仇 – 复仇 báo thù · 报答 – 回报 báo đáp",
           "弊病 – 弊端 mặt hại, tệ hại · 采纳 – 采用 tiếp thu, áp dụng · 参照 – 参考 tham khảo",
           "操练 – 训练 luyện tập, huấn luyện · 充沛 – 充足 dồi dào, đầy đủ",
           "代理 – 代办 làm thay, đại lý · 丰盛 – 丰富 phong phú, thịnh soạn · 抚养 – 养活 nuôi nấng",
           "更正 – 改正 sửa lại cho đúng · 供给 – 供应 cung cấp · 宏伟 – 雄伟 hùng vĩ",
           "混合 – 掺杂 trộn lẫn, pha tạp · 加剧 – 加重 tăng thêm, nặng thêm"],
    say=["Phần mở rộng thứ hai của sách giới thiệu mười sáu cặp từ gần nghĩa. Thầy đọc qua để các bạn làm quen; khi gặp trong bài đọc, các bạn sẽ nhận ra ngay.",
         F(0, "安详，祥和: điềm tĩnh, an lành. 报仇，复仇: báo thù. 报答，回报: báo đáp, đền đáp."),
         F(1, "弊病，弊端: mặt hại, tệ hại. Từ 弊端 chính là từ mới trong bài. 采纳，采用: tiếp thu, áp dụng. 参照，参考: tham khảo, đối chiếu."),
         F(2, "操练，训练: luyện tập, huấn luyện. 充沛，充足: dồi dào, đầy đủ."),
         F(3, "代理，代办: làm thay. 丰盛，丰富: thịnh soạn, phong phú. 抚养，养活: nuôi nấng."),
         F(4, "更正，改正: sửa lại cho đúng. 供给，供应: cung cấp. 宏伟，雄伟: hùng vĩ, to lớn."),
         F(5, "混合，掺杂: trộn lẫn, pha tạp. 加剧，加重: tăng thêm, nặng thêm. Các cặp từ này nghĩa gần nhau nhưng cách kết hợp có khác biệt, các bạn hãy tra từ điển và đặt câu với từng từ nhé.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 5", size=36,
    items=["Từ vựng trọng tâm: 迫不及待 · 兴致勃勃 · 专程 · 反感 · 着想 · 固然 · 无非 · 斩钉截铁 · 弊端 · 权衡 · 津津有味",
           "Ngữ pháp: 而已 (mà thôi) · 固然 (tất nhiên, tuy) · 无非 (chẳng qua, chỉ là)",
           "Phân biệt: 专程 (chỉ dùng khi phải đi một chặng đường) ≠ 专门 (mọi hành động; phạm vi; tính từ)",
           "Mở rộng: câu thiếu chủ ngữ, vị ngữ, tân ngữ, bổ ngữ, từ liên kết",
           "## Bài tập về nhà (运用)",
           "Phỏng vấn 3–4 người khác tuổi, khác nước, khác nghề: 你为什么学习外语？ Viết báo cáo điều tra ít nhất 300 chữ"],
    say=["Chúng ta cùng tổng kết bài năm.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 迫不及待，兴致勃勃，专程，反感，着想，固然，无非，斩钉截铁，弊端，权衡，津津有味. Và đừng quên những từ dễ nhầm như 机构，反感，弊端，颠倒."),
         F(1, "Về ngữ pháp: 而已 đặt cuối câu, nghĩa là mà thôi. 固然 xác nhận một sự thật rồi chuyển ý, hoặc thừa nhận thêm một sự thật. 无非 nghĩa là chẳng qua, chỉ là. Cả ba đều có thể mang ý nói nhẹ đi."),
         F(2, "Về phân biệt từ: 专程 chỉ dùng khi phải đi một chặng đường; còn 专门 dùng cho mọi hành động, còn có nghĩa chỉ giới hạn trong một phạm vi, và còn làm tính từ."),
         F(3, "Về phần mở rộng: câu sai do thiếu thành phần có năm loại: thiếu chủ ngữ, thiếu vị ngữ, thiếu tân ngữ, thiếu bổ ngữ, và thiếu từ liên kết."),
         F(5, "Bài tập về nhà, theo phần vận dụng của sách: hãy phỏng vấn ba đến bốn người khác tuổi, khác quốc tịch, khác nghề nghiệp, với chủ đề 你为什么学习外语？ Ghi lại quốc tịch, tuổi, nghề nghiệp, lý do học ngoại ngữ, và cách học hiện tại cùng lợi hại của nó. Sau đó viết thành một bản báo cáo điều tra ít nhất ba trăm chữ. Nhớ thử dùng 而已，固然，无非 trong bài viết nhé."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Dù lý do học tiếng Trung của các bạn là gì, quan trọng nhất là tìm được niềm vui trong việc học. Hẹn gặp lại các bạn ở bài sáu: 当好职场插班生, Hãy là học sinh giỏi tại nơi làm việc. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Thượng) – Bài 5: 学一门外语需要理由吗？ (Học ngoại ngữ cần lý do ư?)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"勉强": "勉抢",            # miǎnqiǎng
                    "着想": "酌想",            # zhuóxiǎng
                    "为学员": "位学员",        # wèi
                    "为别人": "位别人",        # wèi
                    "为某人": "位某人",        # wèi
                    "为孩子": "位孩子",        # wèi
                    "为队员": "位队员",        # wèi
                    "为国家": "位国家",        # wèi
                    "为每位": "位每位",        # wèi
                    "为啥": "位啥",            # wèishá
                    "为一周期": "维一周期",    # wéi
                    "人为": "人维",            # rénwéi
                    "的确": "敌确",            # díquè
                    "恳切": "恳窃",            # kěnqiè
                    "教起": "交起",            # jiāo qǐ
                    "干吗": "赣吗",            # gànmá
                    "颠倒": "颠岛",            # diāndǎo
                    "兴起": "星起",            # xīngqǐ
                    "成长": "成涨",            # chéngzhǎng
                    "家长": "家涨",            # jiāzhǎng
                    "单调": "单掉",            # dāndiào
                    "供给": "工己",            # gōngjǐ
                    "更正": "耕正",            # gēngzhèng
                    "背包": "杯包"},           # bēibāo
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai05.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
