#!/usr/bin/env python3
"""Kịch bản bài giảng 顶石中文 – Bài 6.1 «职场 996». Chạy để sinh ds61.json."""
import json
import os

TAG = "顶石中文 · Bài 6.1 · 职场 996"
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
    zh="职场 996", py="Zhíchǎng jiǔ jiǔ liù",
    vi="Bài 6.1: Văn hóa làm việc “996”",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng giáo trình 顶石中文, Đỉnh cao tiếng Trung.",
         {"t": "Hôm nay chúng ta bước sang Đơn vị sáu: 职场篇, chủ đề Nơi làm việc. Bài đầu tiên là bài sáu chấm một: 职场九九六。",
          "cap": "Hôm nay chúng ta bước sang Đơn vị 6: 职场篇, chủ đề Nơi làm việc. Bài đầu tiên là bài 6.1: 职场 996."},
         "Con số 九九六 nghĩa là làm việc từ chín giờ sáng đến chín giờ tối, sáu ngày mỗi tuần. Đây là một bài báo nghị luận đăng trên trang 光明网 năm 2019, phê phán hiện tượng nhiều công ty internet Trung Quốc ép nhân viên làm thêm giờ, phân tích nguyên nhân và đề xuất giải pháp.",
         "Chuyện tăng ca, làm việc quá sức không hề xa lạ với người đi làm ở Việt Nam. Trong lúc học, các bạn hãy thử nghĩ xem: mình có từng làm 九九六 không, và mình nghĩ gì về nó nhé."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài nghị luận về chế độ “996”: thực trạng, nguyên nhân, giải pháp",
           "Nắm vững 45 từ mới, kèm âm Hán Việt và ví dụ",
           "9 mẫu câu: 所谓……是指…… · ……而已 · 披着……的外衣 · 无论是……抑或是…… · 固然……但是…… · ……与……是两码事",
           "Kết hợp từ (词语搭配) và 16 thành ngữ, quán dụng ngữ",
           "Luyện tập theo sách; thảo luận về làm thêm giờ ở Trung Quốc và Việt Nam"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu bài nghị luận về chế độ làm việc 九九六: thực trạng ra sao, nguyên nhân ở đâu, và tác giả đề xuất giải pháp gì."),
         F(1, "Thứ hai, nắm vững bốn mươi lăm từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học chín mẫu câu trọng điểm của sách, như 所谓是指，而已，披着的外衣，固然但是, và 两码事."),
         F(3, "Thứ tư, học các kết hợp từ thường gặp và mười sáu thành ngữ, quán dụng ngữ trong bài, như 一石激起千层浪，匪夷所思，冠冕堂皇."),
         F(4, "Thứ năm, làm các bài luyện tập của sách, rồi cùng thảo luận về chuyện làm thêm giờ ở Trung Quốc và Việt Nam."),
         "Bài khóa của giáo trình 顶石 dài và mang phong cách báo chí, nên các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 课前思考", title="Câu hỏi trước bài học 课前思考", reveal=True, size=36,
    items=["(1) 在你们国家有没有所谓的“加班文化”？",
           "Đáp án gợi ý: 有。在越南，很多公司虽然不明说，但员工常常加班，下班后还要回复工作消息。",
           "(2) 在你们国家哪些行业盛行“加班文化”？",
           "Đáp án gợi ý: IT行业、银行、广告公司，还有服装厂、电子厂等工厂。",
           "(3) 你更推崇哪种工作制？为什么？",
           "Đáp án gợi ý: 我推崇八小时工作制，周末双休。这样张弛有度，工作效率反而更高。"],
    say=["Chúng ta bắt đầu bằng ba câu hỏi trước bài học của sách, gọi là 课前思考. Thầy đọc câu hỏi, các bạn tạm dừng để tự trả lời bằng tiếng Trung, rồi nghe câu trả lời gợi ý nhé.",
         F(0, "Câu một: 在你们国家有没有所谓的加班文化？ Ở nước bạn có cái gọi là văn hóa tăng ca không? 加班 là làm thêm giờ, tăng ca."),
         F(1, "Gợi ý: 有。在越南，很多公司虽然不明说，但员工常常加班，下班后还要回复工作消息。 Có. Ở Việt Nam, nhiều công ty tuy không nói thẳng, nhưng nhân viên thường xuyên tăng ca, tan làm rồi vẫn phải trả lời tin nhắn công việc."),
         F(2, "Câu hai: 在你们国家哪些行业盛行加班文化？ Ở nước bạn, những ngành nào thịnh hành văn hóa tăng ca? 盛行 là thịnh hành, phổ biến."),
         F(3, "Gợi ý: IT行业、银行、广告公司，还有服装厂、电子厂等工厂。 Ngành công nghệ thông tin, ngân hàng, công ty quảng cáo, và các nhà máy may mặc, điện tử."),
         F(4, "Câu ba: 你更推崇哪种工作制？为什么？ Bạn đề cao chế độ làm việc nào hơn? Vì sao? 推崇 là đề cao, tôn sùng; 工作制 là chế độ làm việc."),
         F(5, "Gợi ý: 我推崇八小时工作制，周末双休。这样张弛有度，工作效率反而更高。 Tôi đề cao chế độ làm việc tám tiếng, nghỉ cả thứ bảy và chủ nhật. Như vậy làm và nghỉ hợp lý, hiệu quả làm việc lại còn cao hơn. 张弛有度 là một thành ngữ trong bài, lát nữa chúng ta sẽ gặp lại.")])

add("bullets", section="Khởi động 课前思考", title="Khởi động: từ khóa nơi công sở", size=36,
    items=["加班 jiābān tăng ca · 加班费 tiền làm thêm giờ · 超时工作 làm quá giờ · 过劳 làm việc quá sức",
           "打工人 / 打工一族 người làm thuê · 上班族 dân công sở · 白领 nhân viên văn phòng",
           "带薪年假 nghỉ phép năm có lương · 调休 tiáoxiū nghỉ bù · 双休 nghỉ hai ngày cuối tuần",
           "内卷 cạnh tranh nội bộ kiệt sức · 躺平 buông xuôi, “nằm thẳng” · 摸鱼 lười việc trong giờ làm",
           "996 = 9 giờ sáng → 9 giờ tối × 6 ngày/tuần ≈ 72 giờ/tuần"],
    say=["Trước khi vào bài, chúng ta làm quen với một số từ khóa nơi công sở mà người Trung Quốc rất hay dùng. Nhiều từ trong số này sẽ xuất hiện trong bài khóa.",
         F(0, "加班，tăng ca. 加班费，tiền làm thêm giờ. 超时工作，làm việc quá giờ. Và 过劳，làm việc quá sức; từ này sinh ra từ mới 过劳死, chết vì làm việc quá sức."),
         F(1, "打工人, hay 打工一族, là người đi làm thuê, giới trẻ Trung Quốc hay dùng để tự giễu mình. 上班族 là dân công sở. 白领, cổ cồn trắng, là nhân viên văn phòng."),
         F(2, "带薪年假 là nghỉ phép năm có hưởng lương. 调休, chữ đầu đọc thanh hai, là nghỉ bù. 双休 là được nghỉ cả thứ bảy và chủ nhật."),
         F(3, "Ba từ lóng rất nổi tiếng: 内卷, cạnh tranh nội bộ đến kiệt sức mà chẳng ai được lợi; 躺平, nằm thẳng, tức là buông xuôi, không cố gắng nữa; và 摸鱼, mò cá, tức là lười việc, làm việc riêng trong giờ làm."),
         F(4, "Còn 九九六 là chín giờ sáng đến chín giờ tối, sáu ngày một tuần, tức là khoảng bảy mươi hai giờ mỗi tuần. Trong khi đó, luật lao động Trung Quốc quy định mỗi ngày không quá tám giờ, mỗi tuần bình quân không quá bốn mươi tư giờ. Các bạn thấy chênh lệch lớn thế nào chưa?")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("代码", "dàimǎ", "đại mã", "danh từ", "mã, mã nguồn (code)", "程序员每天都要写很多代码。", "Lập trình viên ngày nào cũng phải viết rất nhiều code.",
     "Danh từ, nghĩa là mã lệnh mà máy tính đọc được, tức là code. Hay gặp 写代码, viết code; 源代码, mã nguồn. Trong bài: 代码托管平台, nền tảng lưu trữ mã nguồn, như GitHub."),
    ("托管", "tuōguǎn", "thác quản", "động từ", "ủy thác quản lý, gửi giữ, lưu trữ hộ", "他把项目托管在网上平台。", "Anh ấy lưu trữ dự án trên một nền tảng trực tuyến.",
     "Động từ, nghĩa là giao cho người khác quản lý hoặc giữ hộ. Ngoài nghĩa lưu trữ mã nguồn, đời sống còn có 托管班, lớp trông trẻ sau giờ học."),
    ("抵制", "dǐzhì", "để chế", "động từ", "chống lại, ngăn cản; tẩy chay", "我们要抵制不良风气。", "Chúng ta phải chống lại những thói xấu.",
     "Động từ, nghĩa là ngăn chặn, không để thứ có hại xâm nhập hay phát huy tác dụng; với hàng hóa thì là tẩy chay. Trong bài: 抵制互联网公司超时工作, phản đối việc các công ty internet bắt làm quá giờ."),
    ("响应", "xiǎngyìng", "hưởng ứng", "động từ", "hưởng ứng, đáp lại", "大家积极响应学校的号召。", "Mọi người tích cực hưởng ứng lời kêu gọi của nhà trường.",
     "Động từ, âm Hán Việt là hưởng ứng, nghĩa cũng giống hệt tiếng Việt: dùng lời nói, hành động để ủng hộ một lời kêu gọi. Kết hợp quen thuộc là 响应号召. Trong bài: 此举得到大批程序员响应."),
    ("日前", "rìqián", "nhật tiền", "danh từ", "mấy hôm trước, mới đây", "日前他曾来过一次。", "Mấy hôm trước anh ấy có đến một lần.",
     "Danh từ, nghĩa là mấy ngày trước, mới đây, rất hay gặp trong tin tức. Cẩn thận, đừng nhầm với 目前, nghĩa là hiện nay: hai chữ đầu trông rất giống nhau."),
    ("共鸣", "gòngmíng", "cộng minh", "danh từ", "sự đồng cảm, đồng điệu; cộng hưởng", "这部电影引起了观众的共鸣。", "Bộ phim này đã gây được sự đồng cảm của khán giả.",
     "Danh từ, nghĩa gốc là cộng hưởng âm thanh, nghĩa bóng là sự đồng cảm, cùng chung suy nghĩ. Mẫu hay gặp: 引起共鸣, gây đồng cảm. Trong bài, những lời than phiền 引起年轻打工一族的共鸣."),
    ("猝死", "cùsǐ", "thốt tử", "động từ", "đột tử, chết đột ngột", "他因为过度劳累而猝死。", "Anh ấy đột tử vì làm việc quá sức.",
     "Động từ, nghĩa là chết đột ngột do bệnh tiềm ẩn trong cơ thể, tức là đột tử. Chữ 猝 nghĩa là bất ngờ, như trong 猝不及防, bất ngờ không kịp trở tay. Trong bài có cụm 被猝死, chữ 被 mang ý mỉa mai: không phải tự nhiên mà chết, mà bị công việc ép đến chết."),
    ("显性", "xiǎnxìng", "hiển tính", "tính từ", "lộ rõ ra ngoài, hiển hiện, công khai", "这是一种显性特征。", "Đây là một đặc điểm lộ rõ ra bên ngoài.",
     "Tính từ, nghĩa là biểu hiện ra bên ngoài, nhìn thấy được; trái nghĩa là 隐性, tiềm ẩn. Trong sinh học, 显性基因 là gen trội. Trong bài, 显性的控诉 là những lời tố cáo công khai."),
    ("控诉", "kòngsù", "khống tố", "danh từ", "sự tố cáo, lời tố cáo", "受害人的控诉让人愤怒。", "Lời tố cáo của nạn nhân khiến người ta phẫn nộ.",
     "Danh từ, cũng dùng làm động từ, nghĩa là kể lại sự việc bị hại trước cơ quan chức năng hay công chúng để tố cáo kẻ gây hại. Kết hợp: 控诉罪行, tố cáo tội ác; 血泪控诉, lời tố cáo đẫm máu và nước mắt."),
    ("谎称", "huǎngchēng", "hoang xưng", "động từ", "nói dối rằng, bịa ra là", "他谎称自己生病了。", "Anh ta nói dối rằng mình bị ốm.",
     "Động từ, nghĩa là cố ý nói sai sự thật, nói dối rằng. Chữ 谎 là lời nói dối, như 说谎. Trong bài: 有的公司加班成疯，却谎称是年轻人太拼."),
    ("机制", "jīzhì", "cơ chế", "danh từ", "cơ chế", "公司建立了新的奖惩机制。", "Công ty đã xây dựng cơ chế thưởng phạt mới.",
     "Danh từ, âm Hán Việt và nghĩa giống tiếng Việt: cơ chế, cách các bộ phận trong một hệ thống tác động lẫn nhau. Từ này có hai lần trong bảng từ: 倒逼机制, cơ chế ép ngược; và 体制机制, thể chế và cơ chế."),
    ("熬夜", "áoyè", "ngao dạ", "động từ", "thức khuya, thức đêm", "经常熬夜对身体不好。", "Thường xuyên thức khuya không tốt cho sức khỏe.",
     "Động từ li hợp, nghĩa là thức khuya hoặc thức trắng đêm. Chữ 熬 ở đây đọc thanh hai, nghĩa là chịu đựng, cố gượng. Có thể tách ra: 熬了一夜, thức suốt một đêm. Trong bài có loại bảo hiểm 熬夜险."),
    ("情怀", "qínghuái", "tình hoài", "danh từ", "tình cảm, tâm huyết, hoài bão", "他是一个富有情怀的人。", "Anh ấy là một người giàu tâm huyết.",
     "Danh từ, chỉ tâm trạng chứa đựng một tình cảm nào đó: 爱国情怀, lòng yêu nước. Trên mạng Trung Quốc, 情怀 hay bị dùng mỉa mai: lấy tâm huyết, lý tưởng ra để bắt người khác hy sinh. Trong bài: 靠情怀奉献毕竟是不可持续的."),
    ("招摇", "zhāoyáo", "chiêu dao", "động từ", "phô trương, khoe khoang", "他喜欢开着名车招摇过市。", "Anh ta thích lái xe sang khoe mẽ khắp phố.",
     "Động từ, nghĩa là cố ý làm rùm beng để gây chú ý, mang nghĩa chê. Thành ngữ hay gặp: 招摇过市, nghênh ngang khoe mẽ ngoài phố. Trong bài, văn hóa tăng ca 在诸多企事业单位之间招摇."),
    ("呼吁", "hūyù", "hô dụ", "động từ", "kêu gọi", "专家呼吁大家少用塑料袋。", "Các chuyên gia kêu gọi mọi người ít dùng túi ni lông.",
     "Động từ, nghĩa là kêu gọi xã hội ủng hộ, giúp đỡ hoặc đòi công bằng. Chú ý chữ thứ hai đọc thanh bốn, yù. Kết hợp: 呼吁捐款, kêu gọi quyên góp; 大力呼吁, ra sức kêu gọi."),
    ("遏制", "èzhì", "át chế", "động từ", "kiềm chế, ngăn chặn", "政府采取措施遏制房价上涨。", "Chính phủ áp dụng biện pháp kiềm chế giá nhà tăng.",
     "Động từ, nghĩa là ngăn chặn, kìm hãm, thường dùng với hiện tượng xấu: 遏制腐败，遏制通货膨胀. Trong bài: 遏制过度加班现象, ngăn chặn hiện tượng làm thêm giờ quá mức."),
    ("涉事", "shèshì", "thiệp sự", "động từ", "liên quan đến vụ việc", "警方已经找到了涉事车辆。", "Cảnh sát đã tìm thấy chiếc xe liên quan đến vụ việc.",
     "Động từ, nghĩa là có liên quan tới sự việc, thường đứng trước danh từ, rất hay gặp trong tin tức: 涉事单位, đơn vị liên quan; 涉事官员, quan chức liên quan. Chữ 涉 là thiệp, như trong can thiệp."),
    ("爆料", "bàoliào", "bạo liệu", "động từ", "tiết lộ, bóc phốt (tin gây sốc)", "有网友爆料这家公司拖欠工资。", "Có cư dân mạng tiết lộ công ty này nợ lương.",
     "Động từ, nghĩa là công bố tin tức gây bất ngờ, gây sốc, giống bóc phốt trong tiếng lóng Việt. Chữ 料 ở đây là tư liệu, thông tin."),
    ("申诉", "shēnsù", "thân tố", "động từ", "khiếu nại, kháng nghị", "不满意的话，你可以申诉。", "Nếu không hài lòng, bạn có thể khiếu nại.",
     "Động từ, nghĩa là trình bày lý lẽ lên cấp trên hay cơ quan có thẩm quyền để khiếu nại. Phân biệt với 控诉: 控诉 là tố cáo kẻ gây hại, còn 申诉 là khiếu nại để được xem xét lại."),
    ("姿态", "zītài", "tư thái", "danh từ", "thái độ, tâm thế; tư thế, dáng vẻ", "我们要以全新的姿态迎接新学期。", "Chúng ta đón học kỳ mới với một tâm thế hoàn toàn mới.",
     "Danh từ, có hai nghĩa: dáng vẻ, tư thế, như 姿态优美; và thái độ, tâm thế, như 高姿态, 放低姿态. Trong bài, 有了以上姿态 là với thái độ như trên của giới chủ doanh nghiệp."),
    ("足额", "zú'é", "túc ngạch", "danh từ", "đủ số, đủ mức quy định", "公司必须足额发放工资。", "Công ty phải trả lương đầy đủ.",
     "Danh từ, nghĩa là đủ số lượng quy định, thường làm định ngữ hay trạng ngữ: 足额发放, chi trả đủ; 足额赔偿, bồi thường đủ. Trong bài: 足额加班费, tiền làm thêm giờ trả đủ."),
    ("调休", "tiáoxiū", "điều hưu", "động từ", "nghỉ bù, đổi ngày làm và ngày nghỉ", "周末加班的话，下周可以调休。", "Nếu cuối tuần tăng ca thì tuần sau có thể nghỉ bù.",
     "Động từ, nghĩa là đổi ngày làm việc với ngày nghỉ, hay nghỉ bù cho ngày đã đi làm. Chú ý chữ đầu đọc thanh hai, tiáo. Ở Trung Quốc, dịp lễ thường phải 调休: được nghỉ liền mấy ngày, nhưng phải đi làm bù vào cuối tuần."),
    ("亚健康", "yàjiànkāng", "á kiện khang", "danh từ", "tình trạng cận bệnh, sức khỏe kém", "很多白领处于亚健康状态。", "Rất nhiều nhân viên văn phòng ở trong tình trạng sức khỏe kém.",
     "Danh từ, chỉ trạng thái cơ thể chưa mắc bệnh nhưng chức năng đã suy giảm: hay mệt, mất ngủ, đau đầu. Chữ 亚 là á, kém hơn một bậc, như 亚军, á quân. Vậy 亚健康 là kém khỏe mạnh một bậc."),
    ("致命", "zhìmìng", "trí mệnh", "tính từ", "chết người, chí mạng", "这是他的致命弱点。", "Đây là điểm yếu chí mạng của anh ấy.",
     "Tính từ, nghĩa là có thể làm mất mạng, tiếng Việt quen nói là chí mạng. Kết hợp: 致命伤, vết thương chí mạng; 致命一击, đòn chí mạng. Trong bài: 致命疾病, bệnh hiểm nghèo gây tử vong."),
    ("抑或", "yìhuò", "ức hoặc", "liên từ", "hay là, hoặc là", "你是去，抑或不去？", "Anh đi, hay là không đi?",
     "Liên từ văn viết, nghĩa là hay là, hoặc là, biểu thị lựa chọn, giống 或者 và 还是. Trong bài có mẫu câu dài 无论是，抑或是，哪怕是，都, chúng ta sẽ học kỹ ở phần mẫu câu."),
    ("性价比", "xìngjiàbǐ", "tính giá tỉ", "danh từ", "tỉ lệ chất lượng trên giá; độ đáng đồng tiền", "这款手机性价比很高。", "Mẫu điện thoại này rất đáng đồng tiền.",
     "Danh từ, là tỉ lệ giữa chất lượng, tính năng với giá cả. 性价比高 là ngon bổ rẻ, đáng đồng tiền bát gạo; 性价比低 là không đáng tiền. Trong bài, tác giả dùng từ này một cách hình ảnh: 健康中国战略的性价比, hiệu quả trên chi phí của chiến lược Trung Quốc khỏe mạnh."),
    ("关切", "guānqiè", "quan thiết", "động từ", "quan tâm sâu sắc, ân cần", "他关切地问我身体怎么样。", "Anh ấy ân cần hỏi sức khỏe tôi thế nào.",
     "Động từ, nghĩa là quan tâm tha thiết, cũng làm danh từ: 表示关切, bày tỏ sự quan tâm. Trong bài: 体现了文明社会对国计民生的关切."),
    ("症结", "zhēngjié", "chứng kết", "danh từ", "mấu chốt, nguyên nhân gốc rễ của vấn đề", "我们终于找到了问题的症结。", "Cuối cùng chúng tôi đã tìm ra mấu chốt của vấn đề.",
     "Danh từ. Chú ý chữ đầu ở đây đọc thanh một, zhēng, khác với zhèng trong 症状. Nghĩa gốc là khối u trong bụng, nghĩa bóng là điểm then chốt khiến sự việc hỏng hoặc không giải quyết được. Trong bài: 无非是两个症结, chẳng qua là hai nút thắt."),
    ("举证", "jǔzhèng", "cử chứng", "động từ", "đưa ra chứng cứ", "原告需要向法庭举证。", "Nguyên đơn cần đưa ra chứng cứ trước tòa.",
     "Động từ, thuật ngữ pháp luật, nghĩa là đưa ra bằng chứng. Hay gặp 举证责任, nghĩa vụ chứng minh. Trong bài: 举证难、认定难, khó đưa ra chứng cứ, khó được công nhận."),
    ("禁绝", "jìnjué", "cấm tuyệt", "động từ", "cấm triệt để, dẹp bỏ hoàn toàn", "毒品必须彻底禁绝。", "Ma túy phải bị cấm tuyệt đối.",
     "Động từ, nghĩa là cấm hoàn toàn, khiến điều xấu không còn tồn tại. Chữ đầu ở đây đọc thanh bốn. Trong bài: 过劳加班难以禁绝, khó mà dẹp bỏ hoàn toàn tình trạng làm thêm quá sức."),
    ("过劳死", "guòláosǐ", "quá lao tử", "động từ", "chết vì làm việc quá sức", "过劳死的新闻让人担忧。", "Những tin tức về chết vì làm việc quá sức khiến người ta lo ngại.",
     "Động từ, cũng hay dùng như danh từ, nghĩa là chết do làm việc vượt quá sức chịu đựng. Từ này vốn đến từ tiếng Nhật, karoshi. Trong bài, điều lệ bảo hiểm tai nạn lao động không xếp 过劳死 vào bảy loại tai nạn lao động."),
    ("错位", "cuòwèi", "thác vị", "động từ", "lệch chỗ; lệch lạc, sai lệch", "他的关节错位了。", "Khớp xương của anh ấy bị trật rồi.",
     "Động từ, nghĩa đen là rời khỏi vị trí vốn có, như 骨关节错位, trật khớp; nghĩa bóng là mất trạng thái bình thường, sai lệch. Trong bài: 文化价值的错位, sự lệch lạc về giá trị văn hóa."),
    ("悠着", "yōuzhe", "du trước", "động từ", "từ từ, giữ chừng mực, đừng quá sức", "悠着点儿，别累着。", "Từ từ thôi, đừng để mệt quá.",
     "Động từ, phương ngữ miền Bắc Trung Quốc, nghĩa là kiềm chế, giữ chừng mực, đừng làm quá. Hầu như luôn dùng trong cụm 悠着点儿, cứ từ từ thôi. Trong bài, 悠着点儿 và 慢生活, lối sống chậm, là nhịp sống biết căng biết chùng."),
    ("终究", "zhōngjiū", "chung cứu", "phó từ", "rốt cuộc, suy cho cùng", "孩子终究是孩子。", "Trẻ con suy cho cùng vẫn là trẻ con.",
     "Phó từ, nghĩa là rốt cuộc, cuối cùng vẫn, giống 毕竟 và 终归. Trong bài: 人终究不是劳作的机器, con người suy cho cùng không phải cỗ máy lao động."),
    ("拼搏", "pīnbó", "bính bác", "động từ", "dốc sức phấn đấu, liều mình đấu tranh", "他靠顽强拼搏取得了成功。", "Anh ấy thành công nhờ kiên cường phấn đấu.",
     "Động từ, nghĩa là dồn hết sức để đấu tranh hay giành lấy điều gì. Kết hợp: 拼搏精神, tinh thần phấn đấu; 奋力拼搏. Trong khẩu ngữ hay nói gọn là 拼, như 年轻人太拼, giới trẻ quá máu lửa."),
    ("压榨", "yāzhà", "áp trá", "động từ", "ép, vắt; bóc lột", "老板不能压榨员工。", "Ông chủ không được bóc lột nhân viên.",
     "Động từ, nghĩa đen là ép lấy nước, như 压榨甘蔗, ép mía; nghĩa bóng là bóc lột, vắt kiệt sức người khác. Trong bài: 压榨加班, bị bóc lột bằng làm thêm giờ, đối lập với 自觉拼搏, tự nguyện phấn đấu."),
    ("压根儿", "yàgēnr", "áp căn nhi", "phó từ", "hoàn toàn, vốn dĩ (thường dùng với phủ định)", "我压根儿不认识他。", "Tôi hoàn toàn không quen biết anh ta.",
     "Phó từ khẩu ngữ, nghĩa là từ đầu đến giờ, căn bản, thường đi với câu phủ định: 压根儿不知道, hoàn toàn không biết. Chú ý chữ đầu đọc thanh bốn, yà. Trong bài: 自觉拼搏与压榨加班压根儿是两码事."),
    ("遵从", "zūncóng", "tuân tòng", "động từ", "tuân theo, làm theo", "我们应该遵从上级的指示。", "Chúng ta nên tuân theo chỉ thị của cấp trên.",
     "Động từ, nghĩa là tuân theo và phục tùng. Phân biệt: 遵守 đi với quy định, luật lệ, như 遵守法律; còn 遵从 đi với ý muốn, chỉ thị, lời dạy của người khác, như 遵从父母的意愿."),
    ("初创", "chūchuàng", "sơ sáng", "động từ", "mới thành lập, mới khởi nghiệp", "这是一家初创公司。", "Đây là một công ty khởi nghiệp.",
     "Động từ, nghĩa là vừa mới thành lập. 初创公司, hay 初创企业, chính là công ty khởi nghiệp, startup. Chữ 创 Hán Việt là sáng, như trong sáng lập."),
    ("苦情", "kǔqíng", "khổ tình", "danh từ", "nỗi khổ, sự bi lụy", "这是一部苦情戏。", "Đây là một bộ phim bi lụy.",
     "Danh từ, chỉ cảm giác đau khổ, khó chịu. 苦情戏 là phim truyền hình bi lụy, sướt mướt. Trong bài, 苦情发展 là kiểu phát triển dựa vào sự khổ sở, hy sinh của nhân viên."),
    ("取向", "qǔxiàng", "thủ hướng", "danh từ", "định hướng, khuynh hướng lựa chọn", "每个人的价值取向不同。", "Định hướng giá trị của mỗi người khác nhau.",
     "Danh từ, nghĩa là phương hướng được lựa chọn. Kết hợp quen thuộc: 价值取向, định hướng giá trị; 审美取向, khuynh hướng thẩm mỹ; 以什么为取向, lấy cái gì làm định hướng."),
    ("工时", "gōngshí", "công thời", "danh từ", "giờ công, thời gian làm việc", "这项工作需要五十个工时。", "Công việc này cần năm mươi giờ công.",
     "Danh từ, là đơn vị tính lượng lao động: một người làm một giờ là một giờ công. Trong bài: 工时协商机制, cơ chế thương lượng về thời gian làm việc giữa doanh nghiệp và người lao động."),
    ("定额", "dìng'é", "định ngạch", "danh từ", "định mức, mức quy định", "工人们提前完成了生产定额。", "Công nhân đã hoàn thành định mức sản xuất trước thời hạn.",
     "Danh từ, nghĩa là số lượng được quy định, tức định mức. Trong bài: 劳动定额, định mức lao động, tức là quy định rõ mỗi người phải làm bao nhiêu việc, để công ty không thể giao việc vô hạn."),
    ("体制", "tǐzhì", "thể chế", "danh từ", "thể chế, chế độ tổ chức", "国家正在进行教育体制改革。", "Nhà nước đang cải cách thể chế giáo dục.",
     "Danh từ, âm Hán Việt là thể chế, chỉ chế độ tổ chức của nhà nước, cơ quan, doanh nghiệp. Hay gặp 体制改革, cải cách thể chế. Trong bài, 体制机制保障 là sự bảo đảm bằng thể chế và cơ chế."),
    ("刚需", "gāngxū", "cương nhu", "danh từ", "nhu cầu thiết yếu", "住房是年轻人的刚需。", "Nhà ở là nhu cầu thiết yếu của người trẻ.",
     "Danh từ, nói gọn của 刚性需求, nhu cầu cứng, tức là thứ bắt buộc phải có, giá lên vẫn phải mua. Rất hay gặp trong lĩnh vực nhà đất: 刚需房. Trong bài, hưởng thụ cuộc sống và công việc là 美好生活刚需."),
]

add("bullets", chapter="Từ mới (45 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 6.1 có 45 từ mới, chia thành 15 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 症结 (zhēng) · 调休 (tiáo) · 压根儿 (yà) · 呼吁 (yù) · 熬夜 (áo)",
           "Từ dễ nhầm: 日前 ≠ 目前 · 情怀 · 性价比 · 刚需"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bảng từ của sách có bốn mươi lăm mục; từ 机制 xuất hiện hai lần, nên thầy gộp lại và bổ sung thêm từ 共鸣 trong bài khóa. Thầy chia thành mười lăm nhóm nhỏ, mỗi nhóm ba từ. Đây là bài báo về công việc và pháp luật, nên có nhiều từ thời sự như 爆料，申诉，举证.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số chữ có cách đọc đặc biệt, các bạn cần chú ý: 症结 đọc là zhēngjié, 调休 đọc là tiáoxiū, 压根儿 đọc là yàgēnr, 呼吁 đọc là hūyù, và 熬夜 đọc là áoyè."),
         F(4, "Ngoài ra, có mấy từ dễ hiểu nhầm, như 日前 khác với 目前, hay những từ thời thượng như 情怀，性价比，刚需. Các bạn nhớ nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

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
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung: số viết bằng chữ Hán, bỏ ngoặc kép])
P = [
    ("最近，有人在知名代码托管平台上发起了一个名为“996.ICU”的项目，以此抵制互联网公司超时工作。此举得到大批程序员响应。“一石激起千层浪”，有关加班，超时，过劳的抱怨瞬间引起年轻打工一族的共鸣。",
     "Gần đây, có người khởi xướng trên một nền tảng lưu trữ mã nguồn nổi tiếng một dự án mang tên “996.ICU”, nhằm phản đối việc các công ty internet bắt làm quá giờ. Việc làm này được đông đảo lập trình viên hưởng ứng. “Một hòn đá khuấy lên nghìn lớp sóng”, những lời than phiền về tăng ca, làm quá giờ, làm quá sức lập tức khiến giới trẻ làm thuê đồng cảm.",
     ["代码托管平台 là nền tảng lưu trữ mã nguồn; dự án này ra đời trên GitHub vào mùa xuân năm hai nghìn không trăm mười chín. 名为 là mang tên. 以此 là lấy cách đó để. 此举 là việc làm này, văn viết.",
      "一石激起千层浪 là thành ngữ: ném một hòn đá xuống nước làm dậy nghìn lớp sóng, ý nói một việc nhỏ gây phản ứng dữ dội. 打工一族 là giới làm thuê; chữ 族 chỉ một nhóm người, như 上班族, dân công sở."],
     "最近，有人在知名代码托管平台上发起了一个名为九九六点ICU的项目，以此抵制互联网公司超时工作。此举得到大批程序员响应。一石激起千层浪，有关加班，超时，过劳的抱怨瞬间引起年轻打工一族的共鸣。"),
    ("所谓“996”，是指每天上午9点工作到晚上9点，每周工作6天；而“996.ICU”，意为“工作996，生病ICU”。日前有40多家互联网公司被指实行“996工作制”，其中包括多家知名互联网公司。",
     "Cái gọi là “996” là chỉ việc mỗi ngày làm từ 9 giờ sáng đến 9 giờ tối, mỗi tuần làm 6 ngày; còn “996.ICU” có nghĩa là “làm việc 996, ốm vào ICU”. Mới đây, hơn 40 công ty internet bị chỉ ra là áp dụng “chế độ làm việc 996”, trong đó có nhiều công ty internet nổi tiếng.",
     ["所谓，是指 là mẫu câu giải thích khái niệm: cái gọi là, là chỉ. Đây là mẫu câu trọng điểm số một. ICU là phòng chăm sóc đặc biệt ở bệnh viện, nên 工作九九六，生病ICU nghĩa là cứ làm kiểu 九九六 thì sớm muộn cũng vào phòng hồi sức.",
      "意为 là có nghĩa là, văn viết. 日前 là mấy hôm trước. 被指 là bị cho là, bị chỉ ra là, rất hay gặp trong tin tức. 实行 là thực hiện, áp dụng một chế độ."],
     "所谓九九六，是指每天上午九点工作到晚上九点，每周工作六天；而九九六点ICU，意为工作九九六，生病ICU。日前有四十多家互联网公司被指实行九九六工作制，其中包括多家知名互联网公司。"),
    ("“被猝死”的程序员，“累成狗”的年轻人……这两年，民间的抱怨与传闻，终于成为显性的控诉与新闻。“不是在上班，就是在上班的路上。”有的公司虽不明说，但要求员工每月加班时长要满100小时，加不够就扣钱；",
     "Những lập trình viên “bị đột tử”, những người trẻ “mệt như chó”… Mấy năm nay, những lời than phiền và tin đồn trong dân gian cuối cùng đã trở thành những lời tố cáo và tin tức công khai. “Không phải đang đi làm, thì cũng đang trên đường đi làm.” Có công ty tuy không nói thẳng, nhưng yêu cầu nhân viên mỗi tháng phải tăng ca đủ 100 giờ, không đủ thì trừ tiền;",
     ["累成狗 là tiếng lóng trên mạng, nghĩa là mệt như chó, mệt rã rời, vừa hình ảnh vừa có ý tự giễu; tương tự còn có 忙成狗，困成狗. Còn 被猝死 dùng chữ 被 một cách mỉa mai: không phải tự nhiên đột tử, mà bị công việc ép đến chết.",
      "不是，就是 là không phải cái này thì là cái kia, ý nói lúc nào cũng gắn với công việc. 虽不明说 là tuy không nói rõ ra. 时长 là độ dài thời gian. 加不够就扣钱 là tăng ca không đủ thì bị trừ lương."],
     "被猝死的程序员，累成狗的年轻人……这两年，民间的抱怨与传闻，终于成为显性的控诉与新闻。不是在上班，就是在上班的路上。有的公司虽不明说，但要求员工每月加班时长要满一百小时，加不够就扣钱；"),
    ("有的公司加班成“疯”，却谎称是“年轻人太拼”。没错，它们都没有“加班文化”，只是有着扎实的“加班考核”或者KPI倒逼机制而已。",
     "có công ty bắt tăng ca đến “phát điên”, lại nói dối rằng do “giới trẻ quá máu lửa”. Đúng vậy, họ đều không có “văn hóa tăng ca”, mà chỉ có những “tiêu chí đánh giá tăng ca” chặt chẽ, hay cơ chế KPI ép ngược mà thôi.",
     ["加班成疯 là lối chơi chữ: 成风 là thành phong trào, tác giả thay bằng chữ 疯 cùng âm, nghĩa là điên, ý nói tăng ca đến phát điên. 太拼 là quá liều mạng, quá máu lửa.",
      "Câu 没错，它们都没有加班文化 là giọng mỉa mai: công ty không thừa nhận có văn hóa tăng ca, nhưng lại có 加班考核, chấm điểm tăng ca, và 倒逼机制, cơ chế ép ngược: đặt chỉ tiêu KPI thật cao để nhân viên buộc phải tự làm thêm. Mẫu 只是，而已 nghĩa là chỉ là, mà thôi."]),
    ("去年底，一份名叫“熬夜险”的保险产品开始在微信朋友圈受到关注。夜以继日加班熬夜似乎已经成为一种工作日常，甚至披着道德与情怀的外衣，在诸多企事业单位之间招摇。",
     "Cuối năm ngoái, một sản phẩm bảo hiểm tên là “bảo hiểm thức khuya” bắt đầu được chú ý trên vòng bạn bè WeChat. Tăng ca, thức khuya ngày đêm dường như đã thành chuyện thường ngày trong công việc, thậm chí còn khoác tấm áo đạo đức và tâm huyết, nghênh ngang phô trương ở rất nhiều doanh nghiệp và đơn vị sự nghiệp.",
     ["熬夜险 là loại bảo hiểm dành cho người hay thức khuya; việc nó ra đời cho thấy thức khuya đã thành chuyện phổ biến. 微信朋友圈 là mục Khoảnh khắc, hay vòng bạn bè, trên WeChat. 夜以继日 là thành ngữ: lấy đêm nối ngày, làm việc không nghỉ.",
      "披着的外衣 là khoác tấm áo, tức là bề ngoài trông đẹp đẽ nhưng thực chất không phải vậy; đây là mẫu câu trọng điểm. 企事业单位 là doanh nghiệp và đơn vị sự nghiệp, như trường học, bệnh viện công. 诸多 là rất nhiều, văn viết."]),
    ("这当然不是杞人忧天。2018年的全国两会上，工会界委员就曾呼吁，要遏制过度加班现象，在企业层面建立健全工时协商机制等。",
     "Đây đương nhiên không phải là lo bò trắng răng. Tại kỳ họp Lưỡng hội toàn quốc năm 2018, các ủy viên thuộc giới công đoàn đã từng kêu gọi phải ngăn chặn hiện tượng làm thêm giờ quá mức, xây dựng và kiện toàn cơ chế thương lượng giờ làm ở cấp doanh nghiệp.",
     ["杞人忧天 là thành ngữ: người nước Kỷ lo trời sập, ý nói lo lắng vô căn cứ, giống lo bò trắng răng. Ở đây tác giả khẳng định: lo về chuyện tăng ca không phải là lo vô cớ.",
      "两会 là Lưỡng hội, tức kỳ họp thường niên của Đại hội Đại biểu Nhân dân toàn quốc và Hội nghị Hiệp thương Chính trị. 工会界委员 là các ủy viên thuộc giới công đoàn. 建立健全 là xây dựng và kiện toàn, cụm rất hay gặp trong văn chính luận."],
     "这当然不是杞人忧天。二零一八年的全国两会上，工会界委员就曾呼吁，要遏制过度加班现象，在企业层面建立健全工时协商机制等。"),
    ("及至眼下耸人听闻的“996.ICU”项目，足以说明过劳加班似已成为某种职场明规则，其导致的职工亚健康、患病乃至英年早逝的传闻更是层出不穷。",
     "Đến dự án “996.ICU” gây chấn động dư luận hiện nay thì đủ thấy làm thêm quá sức dường như đã thành một kiểu “luật công khai” nơi công sở; còn những tin đồn về việc nó khiến nhân viên rơi vào tình trạng sức khỏe kém, mắc bệnh, thậm chí chết khi còn trẻ thì xuất hiện liên tiếp không dứt.",
     ["及至 là đến khi, văn viết. 耸人听闻 là thành ngữ: khiến người nghe kinh hãi. 足以说明 là đủ để chứng tỏ. 明规则 là quy tắc công khai, đối lập với 潜规则, quy tắc ngầm; ý nói điều sai trái đã thành chuyện ai cũng làm một cách công khai.",
      "其导致的 là do nó gây ra, chữ 其 thay cho việc làm thêm quá sức. 乃至 là thậm chí. 英年早逝 là qua đời khi đang tuổi tráng niên. 层出不穷 là liên tiếp xuất hiện, không bao giờ hết."],
     "及至眼下耸人听闻的九九六点ICU项目，足以说明过劳加班似已成为某种职场明规则，其导致的职工亚健康、患病乃至英年早逝的传闻更是层出不穷。"),
    ("更令人匪夷所思的是，诸多涉事互联网企业负责人在面对员工爆料和申诉时，采取了以下三种可疑的策略：一是矢口否认，二是认为这是家务事、员工属于“嚼舌头”，三是干脆不以为耻、反以为荣。",
     "Điều càng khó tin hơn là, khi đối mặt với việc nhân viên tố giác và khiếu nại, nhiều người đứng đầu các doanh nghiệp internet liên quan đã áp dụng ba sách lược đáng ngờ: một là một mực chối bỏ; hai là cho rằng đây là chuyện nội bộ, nhân viên chỉ “ngồi lê đôi mách”; ba là thẳng thừng không lấy làm xấu hổ, ngược lại còn lấy làm vẻ vang.",
     ["匪夷所思 là thành ngữ: kỳ quặc đến mức người thường không thể nghĩ ra. 更令人匪夷所思的是 là điều càng khó tin hơn là. 涉事 là liên quan đến vụ việc. 爆料和申诉 là tố giác và khiếu nại.",
      "矢口否认 là một mực chối, nhất quyết không nhận. 家务事 là việc nhà, ý nói chuyện nội bộ, người ngoài đừng xen vào. 嚼舌头 là khẩu ngữ, nghĩa là nói linh tinh, đặt điều. 不以为耻、反以为荣 là không lấy làm xấu hổ mà còn lấy làm vẻ vang."]),
    ("有了以上姿态，也就不难理解以下数字了：比如全国总工会调查显示，每周工作时间在48小时以上的职工占比21.6%，而拿到足额加班费或得到调休的职工仅占44%。没有享受带薪年假、没有补偿的占35.1%。",
     "Với thái độ như trên, cũng chẳng khó hiểu những con số sau đây: chẳng hạn, khảo sát của Tổng Công đoàn toàn quốc cho thấy, người lao động làm việc trên 48 giờ mỗi tuần chiếm 21,6%, trong khi người được trả đủ tiền tăng ca hoặc được nghỉ bù chỉ chiếm 44%. Người không được nghỉ phép năm có lương, không được bù đắp chiếm 35,1%.",
     ["全国总工会 là Tổng Công đoàn toàn quốc Trung Quốc. 占比 là chiếm tỉ lệ. 足额加班费 là tiền tăng ca trả đủ. 调休 là nghỉ bù. 带薪年假 là nghỉ phép năm có hưởng lương; chữ 薪 là lương.",
      "Câu 有了以上姿态，也就不难理解以下数字了 nối hai đoạn: vì giới chủ có thái độ coi thường như vậy, nên những con số đáng buồn sau đây cũng là điều dễ hiểu. Để so sánh: luật lao động Trung Quốc quy định mỗi tuần làm bình quân không quá bốn mươi tư giờ."],
     "有了以上姿态，也就不难理解以下数字了：比如全国总工会调查显示，每周工作时间在四十八小时以上的职工占比百分之二十一点六，而拿到足额加班费或得到调休的职工仅占百分之四十四。没有享受带薪年假、没有补偿的占百分之三十五点一。"),
    ("又比如早在2010年，《中国城市白领健康白皮书》就给出了这样的数据：76%的白领处于亚健康状态。在30岁至50岁英年早逝的人群中，95.7%死于因过度疲劳引起的致命疾病。",
     "Lại ví dụ, ngay từ năm 2010, “Sách trắng về sức khỏe của giới văn phòng thành thị Trung Quốc” đã đưa ra số liệu như sau: 76% nhân viên văn phòng ở trong tình trạng sức khỏe kém. Trong số những người qua đời sớm ở độ tuổi 30 đến 50, 95,7% chết vì những căn bệnh hiểm nghèo do quá mệt mỏi gây ra.",
     ["白领 là cổ cồn trắng, tức nhân viên văn phòng; còn 蓝领, cổ cồn xanh, là công nhân. 白皮书 là sách trắng, văn bản chính thức công bố về một vấn đề lớn, gọi vậy vì bìa màu trắng.",
      "死于 là chết vì, 于 là giới từ văn viết. 因过度疲劳引起的 là do mệt mỏi quá độ gây ra. Các con số liên tiếp trong đoạn này là cách lập luận rất đặc trưng của văn chính luận: dùng số liệu để thuyết phục."],
     "又比如早在二零一零年，《中国城市白领健康白皮书》就给出了这样的数据：百分之七十六的白领处于亚健康状态。在三十岁至五十岁英年早逝的人群中，百分之九十五点七死于因过度疲劳引起的致命疾病。"),
    ("中国社科院的一项调查显示，2017年中国人每天平均休闲时间仅为2.27小时，美国、德国等国家国民每天平均休闲时间是中国人的两倍以上。",
     "Một khảo sát của Viện Khoa học Xã hội Trung Quốc cho thấy, năm 2017 thời gian nghỉ ngơi bình quân mỗi ngày của người Trung Quốc chỉ có 2,27 giờ, còn thời gian này của người dân các nước như Mỹ, Đức gấp hơn hai lần người Trung Quốc.",
     ["社科院 là nói gọn của 社会科学院, Viện Khoa học Xã hội. 休闲时间 là thời gian rảnh rỗi, nghỉ ngơi giải trí. 仅为 là chỉ có, văn viết.",
      "两倍以上 là gấp hơn hai lần. Con số này cho thấy người Trung Quốc làm việc nhiều mà nghỉ ngơi ít, và dẫn vào lập luận ở câu tiếp theo."],
     "中国社科院的一项调查显示，二零一七年中国人每天平均休闲时间仅为二点二七小时，美国、德国等国家国民每天平均休闲时间是中国人的两倍以上。"),
    ("无论是从劳动力红利终结的现实阶段来看，抑或是从健康中国战略的性价比来说，哪怕是关照柴米油盐的小日子，关注过劳加班的年轻人，都体现了文明社会对国计民生的关切。",
     "Dù là nhìn từ thực tế khi lợi thế về nguồn lao động đã chấm dứt, hay là xét từ hiệu quả trên chi phí của chiến lược Trung Quốc khỏe mạnh, hoặc thậm chí chỉ để chăm lo cho cuộc sống cơm áo gạo tiền thường ngày, thì việc quan tâm đến những người trẻ làm thêm quá sức đều thể hiện sự quan tâm của xã hội văn minh đối với quốc kế dân sinh.",
     ["劳动力红利 là lợi tức về lao động: nhờ đông người trong độ tuổi lao động mà kinh tế tăng nhanh; nay dân số già đi, lợi thế ấy chấm dứt, nên càng phải giữ gìn sức khỏe người lao động. 健康中国战略 là chiến lược Trung Quốc khỏe mạnh của nhà nước.",
      "Câu này dùng mẫu 无论是，抑或是，哪怕是，都: dù xét theo góc độ nào, kết quả vẫn không đổi. 柴米油盐 là củi gạo dầu muối, tức chuyện cơm áo hằng ngày. 国计民生 là kinh tế đất nước và đời sống nhân dân."]),
    ("不过，“996工作制”之所以日益蔓延，说到底，无非是两个症结：一是法律责任的缺位。举证难、认定难、违法成本低，这是过劳加班难以禁绝的根源。",
     "Tuy nhiên, sở dĩ “chế độ làm việc 996” ngày càng lan rộng, suy cho cùng chẳng qua là vì hai nút thắt: một là sự vắng mặt của trách nhiệm pháp lý. Khó đưa ra chứng cứ, khó được công nhận, cái giá của việc vi phạm pháp luật lại thấp, đó là gốc rễ khiến tình trạng làm thêm quá sức khó mà dẹp bỏ.",
     ["之所以，说到底，无非是 là sở dĩ, suy cho cùng, chẳng qua là: một cách nêu nguyên nhân rất chặt chẽ. 蔓延 là lan tràn như dây leo. 缺位 là thiếu vắng, đáng lẽ phải có mà không có.",
      "违法成本 là cái giá phải trả khi vi phạm pháp luật; 违法成本低 nghĩa là vi phạm mà bị phạt nhẹ, nên doanh nghiệp không sợ. 难以禁绝 là khó mà cấm tuyệt. 根源 là cội nguồn, gốc rễ."],
     "不过，九九六工作制之所以日益蔓延，说到底，无非是两个症结：一是法律责任的缺位。举证难、认定难、违法成本低，这是过劳加班难以禁绝的根源。"),
    ("比如《工伤保险条例》规定的7种工伤不包含“过劳死”，只规定“在工作时间和工作岗位，突发疾病死亡或者在48小时内经抢救无效死亡的”，视同工伤。事实上的“过劳无责”令过劳加班肆无忌惮。",
     "Chẳng hạn, bảy loại tai nạn lao động trong “Điều lệ bảo hiểm tai nạn lao động” không gồm “chết vì làm việc quá sức”; chỉ trường hợp “đột ngột phát bệnh qua đời trong giờ làm, tại nơi làm việc, hoặc qua đời trong vòng 48 giờ sau khi cấp cứu không thành” mới được coi như tai nạn lao động. Thực tế “làm quá sức mà không ai chịu trách nhiệm” khiến việc ép tăng ca càng không kiêng nể gì.",
     ["工伤 là tai nạn lao động. 条例 là điều lệ, một loại văn bản pháp quy; điều lệ này do Quốc vụ viện Trung Quốc ban hành năm hai nghìn không trăm linh ba. 经抢救无效 là cấp cứu không hiệu quả. 视同 là coi như.",
      "过劳无责 là làm quá sức mà không ai chịu trách nhiệm. 肆无忌惮 là thành ngữ: ngang nhiên, không kiêng nể gì. Chữ 令 ở đây là khiến cho."],
     "比如《工伤保险条例》规定的七种工伤不包含过劳死，只规定在工作时间和工作岗位，突发疾病死亡或者在四十八小时内经抢救无效死亡的，视同工伤。事实上的过劳无责令过劳加班肆无忌惮。"),
    ("二是文化价值的错位。拼搏与奋斗固然是时代热词，但是，人终究不是劳作的机器，从人的可持续发展来看，“悠着点儿”“慢生活”亦是张弛有度的生活节奏。",
     "Hai là sự lệch lạc về giá trị văn hóa. Phấn đấu và cống hiến hẳn nhiên là những từ khóa của thời đại, nhưng con người suy cho cùng không phải cỗ máy lao động; xét từ sự phát triển bền vững của con người, “cứ từ từ thôi” hay “sống chậm” cũng là một nhịp sống biết căng biết chùng.",
     ["固然，但是 là đành rằng, nhưng: thừa nhận ý trước là đúng rồi chuyển sang ý chính. 时代热词 là từ khóa nóng của thời đại. 可持续发展 là phát triển bền vững.",
      "悠着点儿 là cứ từ từ, đừng quá sức. 亦 là cũng, văn viết, giống 也. 张弛有度 là thành ngữ: 张 là căng, 弛 là chùng; căng chùng có mức độ, tức là làm và nghỉ hợp lý."]),
    ("更重要的是，自觉拼搏与压榨加班压根儿是两码事——前者指向个体自由选择，后者指向群体强制遵从。即便是一个初创公司，“苦情发展”也并非文明社会的价值取向。",
     "Quan trọng hơn, tự giác phấn đấu và bị bóc lột bằng tăng ca vốn dĩ là hai chuyện hoàn toàn khác nhau: cái trước là sự lựa chọn tự do của cá nhân, cái sau là sự phục tùng bắt buộc của cả tập thể. Dù là một công ty khởi nghiệp, “phát triển bằng khổ sở” cũng không phải là định hướng giá trị của một xã hội văn minh.",
     ["与，是两码事 là hai chuyện khác nhau; chữ 码 ở đây là lượng từ chỉ sự việc. 压根儿 nhấn mạnh: hoàn toàn, vốn dĩ. 前者 là cái trước, 后者 là cái sau.",
      "指向 là hướng tới. 即便是，也 là cho dù, cũng. 初创公司 là công ty khởi nghiệp, nơi người ta hay biện minh rằng phải làm cật lực mới sống sót được. 并非 là hoàn toàn không phải."]),
    ("当务之急，不让“996工作制”成为职场明规则，除了建立健全工时协商机制等高阶要求之外，最迫切的，恐怕还是企业层面的劳动定额和法律层面的过劳立法。",
     "Việc cấp bách trước mắt là không để “chế độ làm việc 996” trở thành luật công khai nơi công sở. Ngoài những yêu cầu ở tầm cao hơn như xây dựng và kiện toàn cơ chế thương lượng giờ làm, điều cấp thiết nhất có lẽ vẫn là định mức lao động ở cấp doanh nghiệp, và lập pháp về làm việc quá sức ở cấp luật pháp.",
     ["当务之急 là việc cấp bách nhất cần làm ngay. 高阶要求 là yêu cầu bậc cao, khó thực hiện ngay. 最迫切的 là điều cấp thiết nhất. 恐怕 ở đây không phải là sợ, mà là e rằng, có lẽ.",
      "Tác giả đưa ra hai giải pháp cụ thể: 劳动定额, quy định rõ khối lượng công việc để công ty không thể giao việc vô hạn; và 过劳立法, ban hành luật về làm việc quá sức, chẳng hạn công nhận chết vì làm quá sức là tai nạn lao động."],
     "当务之急，不让九九六工作制成为职场明规则，除了建立健全工时协商机制等高阶要求之外，最迫切的，恐怕还是企业层面的劳动定额和法律层面的过劳立法。"),
    ("总之，人不是定好闹钟的机器，享受生活与享受工作，是须有体制机制保障的美好生活刚需。即使偶尔因工作需要不得不“996”也必须按劳动法的有关规定按时足额发放加班工资，无论以何种冠冕堂皇的借口对职工进行道德绑架都是不可接受的。",
     "Tóm lại, con người không phải cỗ máy cài sẵn đồng hồ báo thức; tận hưởng cuộc sống và tận hưởng công việc là nhu cầu thiết yếu của cuộc sống tốt đẹp, cần thể chế và cơ chế bảo đảm. Dù đôi khi vì công việc buộc phải “996”, thì cũng phải trả đủ, đúng hạn tiền tăng ca theo luật lao động; lấy bất cứ cái cớ đường hoàng nào để trói buộc người lao động bằng đạo đức đều là không thể chấp nhận.",
     ["定好闹钟的机器 là cỗ máy đã cài sẵn đồng hồ báo thức, cứ đến giờ là chạy. 须有 là cần phải có; 须 là cách nói văn viết của 必须. 刚需 là nhu cầu thiết yếu.",
      "即使，也 là cho dù, cũng. 按时足额 là đúng hạn và đủ số. 冠冕堂皇 là thành ngữ: bề ngoài đường hoàng, nghiêm chỉnh, mang nghĩa chê. 道德绑架 là bắt cóc đạo đức, tức dùng đạo đức để ép người khác làm theo ý mình."],
     "总之，人不是定好闹钟的机器，享受生活与享受工作，是须有体制机制保障的美好生活刚需。即使偶尔因工作需要不得不九九六也必须按劳动法的有关规定按时足额发放加班工资，无论以何种冠冕堂皇的借口对职工进行道德绑架都是不可接受的。"),
    ("因为靠情怀奉献毕竟是不可持续的，抛开收获谈付出都是耍流氓。",
     "Bởi vì cống hiến chỉ dựa vào tâm huyết thì suy cho cùng không thể bền lâu; gạt chuyện người lao động được hưởng gì sang một bên mà chỉ nói đến việc họ phải bỏ ra bao nhiêu, thì đều là giở trò lưu manh.",
     ["毕竟 là dù sao, suy cho cùng. 抛开 là gạt sang một bên. 收获 là thu hoạch, ở đây là quyền lợi người lao động nhận được; 付出 là sự bỏ ra, cống hiến.",
      "耍流氓 nghĩa gốc là giở trò lưu manh, nghĩa mở rộng là giở mánh khóe để trục lợi. Câu kết rất mạnh, mô phỏng một câu nói nổi tiếng trên mạng: 一切不以结婚为目的的恋爱都是耍流氓. Ý tác giả: chỉ đòi nhân viên cống hiến mà không nói đến quyền lợi là vô lý, là gian lận."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 职场 996", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa. Bài được cải biên từ bài xã luận 莫让九九六工作制成了职场明规则, Đừng để chế độ làm việc 九九六 thành luật công khai nơi công sở, đăng trên 光明网 ngày sáu tháng tư năm hai nghìn không trăm mười chín. Bài dài hơn một nghìn năm trăm chữ, gồm bảy đoạn lớn.",
         F(0, "Thầy chia bài thành mười chín đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Văn chính luận có câu dài và nhiều thành ngữ, nên nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])


def vi_tts(s):
    """Bản dịch để giọng Việt đọc: 996 đọc là «chín chín sáu», bỏ ngoặc kép."""
    return s.replace("996", "chín chín sáu").replace("“", "").replace("”", "")


for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 90 else 50 if len(zh) <= 115 else 46
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi_tts(vi), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Bố cục & ghi chú", section="Bài khóa 课文", title="Bố cục bài khóa: hiện tượng → nguyên nhân → giải pháp", size=34,
    items=["## 1. Hiện tượng (đoạn 1–5)",
           "Dự án “996.ICU” · công ty ép tăng ca nhưng không nhận có “văn hóa tăng ca” · “熬夜险”",
           "## 2. Không phải lo vô cớ: thái độ của giới chủ và số liệu (đoạn 6–12)",
           "三种可疑的策略：矢口否认 · 家务事 · 不以为耻、反以为荣 · 21.6% · 44% · 76% · 95.7% · 2.27小时",
           "## 3. Nguyên nhân: 两个症结 (đoạn 13–16)",
           "一是法律责任的缺位 · 二是文化价值的错位（自觉拼搏≠压榨加班）",
           "## 4. Giải pháp và kết luận (đoạn 17–19)",
           "劳动定额 · 过劳立法 · 足额发放加班工资 · 反对道德绑架"],
    say=["Trước khi sang phần mẫu câu, chúng ta cùng nhìn lại bố cục bài khóa. Đây là bố cục rất điển hình của một bài xã luận: nêu hiện tượng, phân tích nguyên nhân, rồi đề xuất giải pháp.",
         F(1, "Phần một, hiện tượng: dự án 九九六点ICU được lập trình viên hưởng ứng; các công ty ép tăng ca, nhưng lại nói mình không có văn hóa tăng ca; thậm chí xuất hiện cả bảo hiểm thức khuya."),
         F(3, "Phần hai: đây không phải lo vô cớ. Giới chủ có ba sách lược đáng ngờ: 矢口否认，说是家务事，不以为耻、反以为荣. Rồi hàng loạt con số: hơn hai mươi mốt phần trăm làm trên bốn mươi tám giờ một tuần, bảy mươi sáu phần trăm dân văn phòng có sức khỏe kém, người Trung Quốc chỉ nghỉ ngơi hơn hai tiếng mỗi ngày."),
         F(5, "Phần ba, nguyên nhân, gồm hai nút thắt: 一是法律责任的缺位，二是文化价值的错位. Pháp luật thiếu chế tài, và xã hội nhầm lẫn giữa tự giác phấn đấu với bị bóc lột."),
         F(7, "Phần bốn, giải pháp: định mức lao động ở doanh nghiệp, lập pháp về làm việc quá sức, trả đủ tiền tăng ca, và phản đối việc dùng đạo đức để trói buộc người lao động. Khi tự trình bày lại bài khóa, các bạn hãy đi theo bốn bước này.")])

add("bullets", section="Bài khóa 课文", title="Ghi chú 注释: hiểu thêm về bối cảnh", size=33,
    items=["累成狗: tiếng lóng “mệt như chó”, vừa hình ảnh vừa tự giễu; còn có 忙成狗 · 困成狗",
           "两会: Lưỡng hội – kỳ họp thường niên của 全国人民代表大会 và 中国人民政治协商会议",
           "明规则 ↔ 潜规则: quy tắc ngầm bị công khai hóa, thành chuyện “đường hoàng” – vẫn mang nghĩa chê",
           "白皮书: sách trắng – văn bản chính thức về vấn đề lớn; Trung Quốc ra sách trắng đầu tiên năm 1991",
           "《工伤保险条例》: Điều lệ bảo hiểm tai nạn lao động, ban hành 27/4/2003, hiệu lực từ 1/1/2004"],
    say=["Sách có năm ghi chú giúp hiểu thêm bối cảnh bài khóa.",
         F(0, "Một: 累成狗. Trong tiếng Hán, chữ 狗 vốn mang nghĩa xấu, nhưng gần đây giới trẻ dùng 累成狗，忙成狗，困成狗 để nói mình mệt, bận, buồn ngủ đến rã rời. Cách nói này vừa hình ảnh, vừa có ý tự giễu."),
         F(1, "Hai: 两会, Lưỡng hội, là cách gọi chung kỳ họp thường niên của 全国人民代表大会, Đại hội Đại biểu Nhân dân toàn quốc, và 中国人民政治协商会议, Hội nghị Hiệp thương Chính trị Nhân dân Trung Quốc. Hai hội nghị họp cùng thời gian, nên gọi tắt là Lưỡng hội."),
         F(2, "Ba: 明规则, phát triển từ 潜规则, quy tắc ngầm, tức những luật lệ không công khai, nằm ngoài quy định chính thức. Khi những việc ấy được làm công khai, trơ trẽn, thì gọi là 明规则. Từ này vẫn mang nghĩa chê."),
         F(3, "Bốn: 白皮书, sách trắng, là văn bản chính thức của chính phủ về những vấn đề lớn như chính trị, kinh tế, ngoại giao; gọi vậy vì bìa màu trắng. Trung Quốc công bố sách trắng đầu tiên năm một nghìn chín trăm chín mươi mốt."),
         F(4, "Năm: 工伤保险条例, Điều lệ bảo hiểm tai nạn lao động, do Quốc vụ viện ban hành ngày hai mươi bảy tháng tư năm hai nghìn không trăm linh ba, có hiệu lực từ ngày một tháng một năm hai nghìn không trăm linh bốn, nhằm bảo đảm người lao động bị tai nạn hay bệnh nghề nghiệp được chữa trị và bồi thường.")])

# ======================= MẪU CÂU =======================
add("bullets", chapter="Mẫu câu: 所谓 · 而已 · 披着…外衣", section="Mẫu câu 重点句型", title="1. 所谓……是指…… – cái gọi là… là chỉ…", size=36,
    items=["Dùng để giải thích, định nghĩa một khái niệm; khái niệm đứng sau 所谓, thường trong ngoặc kép",
           "所谓“996”，是指每天上午9点工作到晚上9点，每周工作6天。",
           "所谓新媒体，是指相对于报刊、户外、广播、电视四大传统意义上的媒体之外的传播平台。",
           "所谓“八小时工作制”，是指正常一天工作时间为早上九点至下午五点，共八小时。"],
    say=["Bây giờ chúng ta sang phần mẫu câu và từ ngữ trọng điểm, sách gọi là 重点句型与词汇. Bài này có chín điểm. Điểm thứ nhất là 所谓是指.",
         F(0, "所谓 nghĩa là cái gọi là, 是指 là là chỉ. Mẫu này dùng để giải thích, định nghĩa một khái niệm. Khái niệm cần giải thích đứng ngay sau 所谓, thường đặt trong ngoặc kép. Rất hay dùng trong văn thuyết minh và nghị luận."),
         F(1, "Ví dụ một, từ bài khóa: 所谓九九六，是指每天上午九点工作到晚上九点，每周工作六天。 Cái gọi là 九九六 là chỉ mỗi ngày làm từ chín giờ sáng đến chín giờ tối, mỗi tuần làm sáu ngày."),
         F(2, "Ví dụ hai: 所谓新媒体，是指相对于报刊、户外、广播、电视四大传统意义上的媒体之外的传播平台。 Cái gọi là truyền thông mới là chỉ những nền tảng truyền thông nằm ngoài bốn loại truyền thông truyền thống: báo chí, quảng cáo ngoài trời, phát thanh và truyền hình."),
         F(3, "Ví dụ ba: 所谓八小时工作制，是指正常一天工作时间为早上九点至下午五点，共八小时。 Cái gọi là chế độ làm việc tám tiếng là chỉ thời gian làm việc bình thường trong một ngày từ chín giờ sáng đến năm giờ chiều, tổng cộng tám tiếng. Các bạn thử dùng mẫu này để giải thích từ 躺平 hay 内卷 xem nhé.")])

add("bullets", section="Mẫu câu 重点句型", title="2. ……而已 · 5. 无非/不过/只不过/只是……而已/罢了", size=34,
    items=["而已: trợ từ cuối câu = “mà thôi”, giảm nhẹ sự việc; phía trước hay có 只是 · 不过 · 无非 · 只不过",
           "它们都没有“加班文化”，只是有着扎实的“加班考核”或者KPI倒逼机制而已。",
           "这算什么，只是一堆纸而已。 · 我不过是出于好奇，随便问问而已。",
           "罢了: cũng là “mà thôi”, khẩu ngữ hơn · 无非: chẳng qua là, không ngoài",
           "“996工作制”之所以日益普遍，说到底，无非是两个症结：一是法律责任的缺位。",
           "她会做这道题，只不过假装不会而已。 · 大家都说爱情很快就会过去，剩下的只是习惯罢了。"],
    say=["Điểm thứ hai là trợ từ 而已, và điểm thứ năm là nhóm từ đi kèm với nó. Thầy gộp hai điểm này lại để các bạn dễ nhớ.",
         F(0, "而已 là trợ từ đặt cuối câu, nghĩa là mà thôi, dùng để giảm nhẹ, coi sự việc chỉ đến mức đó. Phía trước thường có 只是，不过，无非，只不过, tạo thành khung câu chỉ là, mà thôi."),
         F(1, "Ví dụ từ bài khóa: 它们都没有加班文化，只是有着扎实的加班考核或者KPI倒逼机制而已。 Họ đều không có văn hóa tăng ca, chỉ có cơ chế chấm điểm tăng ca chặt chẽ hay KPI ép ngược mà thôi."),
         F(2, "这算什么，只是一堆纸而已。 Cái này có đáng gì, chỉ là một đống giấy mà thôi. Và: 我不过是出于好奇，随便问问而已。 Tôi chẳng qua là vì tò mò, hỏi bâng quơ thôi mà."),
         F(3, "罢了 cũng nghĩa là mà thôi, nhưng mang màu khẩu ngữ hơn. Còn 无非 nghĩa là chẳng qua là, không ngoài, nhấn mạnh rằng sự việc chỉ đơn giản có vậy."),
         F(4, "Ví dụ từ bài khóa: 九九六工作制之所以日益普遍，说到底，无非是两个症结：一是法律责任的缺位。 Sở dĩ chế độ 九九六 ngày càng phổ biến, suy cho cùng chẳng qua là vì hai nút thắt."),
         F(5, "她会做这道题，只不过假装不会而已。 Cô ấy biết làm bài này, chẳng qua là giả vờ không biết mà thôi. Và: 大家都说爱情很快就会过去，剩下的只是习惯罢了。 Ai cũng nói tình yêu sẽ nhanh chóng qua đi, còn lại chỉ là thói quen mà thôi.")])

add("bullets", section="Mẫu câu 重点句型", title="3. 披着……的外衣 – khoác tấm áo…, đội lốt…", size=35,
    items=["Bề ngoài trông hào nhoáng, đẹp đẽ, nhưng thực chất không tốt như vậy; mang nghĩa chê",
           "加班熬夜似乎已经成为一种工作态势，甚至披着道德与情怀的外衣，在诸多企事业单位之间招摇。",
           "这些谣言披着科学的外衣，言之凿凿，普通人想要判定真伪也并非易事。",
           "面对如山的铁证，消费者们终于看清了披着促销外衣的骗局。",
           "Gần nghĩa trong tiếng Việt: đội lốt · khoác áo · núp bóng"],
    say=["Điểm thứ ba là cụm 披着的外衣. 披 là khoác lên vai, 外衣 là áo ngoài.",
         F(0, "Cụm này nghĩa là khoác tấm áo gì đó: bề ngoài trông hào nhoáng, đẹp đẽ, nhưng thực chất không tốt như vậy. Nó luôn mang nghĩa chê, dùng để vạch trần bản chất thật."),
         F(1, "Ví dụ một, từ bài khóa: 加班熬夜似乎已经成为一种工作态势，甚至披着道德与情怀的外衣，在诸多企事业单位之间招摇。 Tăng ca thức khuya dường như đã thành một xu thế công việc, thậm chí còn khoác tấm áo đạo đức và tâm huyết. Bề ngoài là cống hiến, thực chất là bóc lột."),
         F(2, "Ví dụ hai: 这些谣言披着科学的外衣，言之凿凿，普通人想要判定真伪也并非易事。 Những tin đồn này khoác tấm áo khoa học, nói chắc như đinh đóng cột, người bình thường muốn phân biệt thật giả cũng chẳng dễ. 言之凿凿 là nói năng chắc nịch."),
         F(3, "Ví dụ ba: 面对如山的铁证，消费者们终于看清了披着促销外衣的骗局。 Trước những bằng chứng như núi, người tiêu dùng cuối cùng đã nhìn rõ trò lừa đội lốt khuyến mãi."),
         F(4, "Trong tiếng Việt, ta có những cách nói tương tự: đội lốt, khoác áo, núp bóng. Ví dụ: núp bóng từ thiện để trục lợi, có thể nói là 披着慈善的外衣谋取私利.")])

add("bullets", chapter="Mẫu câu: 无论是…抑或是… · 说到底 · 固然", section="Mẫu câu 重点句型", title="4. 无论是……抑或是……哪怕是……都……", size=35,
    items=["Liệt kê nhiều điều kiện khác nhau (哪怕 là trường hợp cực đoan nhất) – kết quả vẫn không đổi",
           "Bài khóa: 无论是从劳动力红利终结的现实阶段来看，抑或是从健康中国战略的性价比来说，哪怕是关照柴米油盐小日子，关注过劳加班的年轻人，都体现了对国计民生的关切。",
           "无论是青春洋溢的少年，抑或是年富力强的中年人，哪怕是步入黄昏的老年人，学习都应该是生命中的重要组成部分。",
           "无论是位高权重的官员，抑或是出身卑微的平民，哪怕是犯过错误的人，他们都享有同等的基本权利。"],
    say=["Điểm thứ tư là một khung câu dài, rất đặc trưng của văn viết trang trọng: 无论是，抑或是，哪怕是，都.",
         F(0, "无论是 là dù là, 抑或是 là hay là, 哪怕是 là cho dù là, thậm chí là, và cuối cùng 都 dẫn ra kết quả. Mẫu này liệt kê nhiều điều kiện khác nhau, điều kiện sau 哪怕 thường là trường hợp cực đoan nhất, nhưng kết quả vẫn không thay đổi."),
         F(1, "Ví dụ một là câu trong bài khóa mà chúng ta vừa học ở đoạn mười hai: dù xét từ góc độ lợi thế lao động, hay từ chiến lược sức khỏe quốc gia, hay chỉ là chuyện cơm áo thường ngày, thì quan tâm đến người trẻ làm thêm quá sức đều thể hiện sự quan tâm đến quốc kế dân sinh."),
         F(2, "Ví dụ hai: 无论是青春洋溢的少年，抑或是年富力强的中年人，哪怕是步入黄昏的老年人，学习都应该是生命中的重要组成部分。 Dù là thiếu niên tràn đầy sức xuân, hay người trung niên đang sung sức, thậm chí người già đã bước vào tuổi xế chiều, thì học tập đều nên là một phần quan trọng của cuộc đời."),
         F(3, "Ví dụ ba: 无论是位高权重的官员，抑或是出身卑微的平民，哪怕是犯过错误的人，他们都享有同等的基本权利。 Dù là quan chức quyền cao chức trọng, hay thường dân xuất thân thấp kém, thậm chí là người từng phạm sai lầm, họ đều được hưởng những quyền cơ bản như nhau.")])

add("bullets", section="Mẫu câu 重点句型", title="6. 说到底 · 7. ……固然……，但是……", size=34,
    items=["说到底: suy cho cùng, nói cho cùng – dẫn ra bản chất của vấn đề",
           "写小说，说到底，就是写人物。小说艺术的精髓就是塑造人物的艺术。",
           "在企业发展中，任何重大的成功，说到底都是用人的成功。",
           "固然……但是/可是/不过……: thừa nhận ý trước là đúng, rồi chuyển sang ý chính ở sau",
           "拼搏与奋斗固然是时代热词，但是，人终究不是劳作的机器。",
           "一个人的成功，聪明固然重要，但是努力更重要。 · 网络固然给我们带来了便利，可是也给我们带来了麻烦。"],
    say=["Điểm thứ sáu là 说到底, và điểm thứ bảy là 固然.",
         F(0, "说到底 nghĩa là suy cho cùng, nói cho cùng. Nó thường đứng đầu vế câu, có dấu phẩy ngắt, dùng để gạt bỏ những thứ bề ngoài và chỉ ra bản chất của vấn đề. Trong bài khóa: 九九六工作制之所以日益普遍，说到底，无非是两个症结."),
         F(1, "Ví dụ: 写小说，说到底，就是写人物。小说艺术的精髓就是塑造人物的艺术。 Viết tiểu thuyết, suy cho cùng, là viết về nhân vật. Tinh túy của nghệ thuật tiểu thuyết chính là nghệ thuật xây dựng nhân vật."),
         F(2, "Và: 在企业发展中，任何重大的成功，说到底都是用人的成功。 Trong sự phát triển của doanh nghiệp, mọi thành công lớn, nói cho cùng đều là thành công trong việc dùng người."),
         F(3, "固然 nghĩa là đành rằng, hẳn nhiên. Mẫu 固然, 但是 hay 可是, 不过, dùng để thừa nhận ý trước là đúng, rồi chuyển sang ý chính ở vế sau. Đây là cách lập luận nhượng bộ rất hữu ích khi viết văn nghị luận."),
         F(4, "Ví dụ từ bài khóa: 拼搏与奋斗固然是时代热词，但是，人终究不是劳作的机器。 Phấn đấu và cống hiến hẳn nhiên là từ khóa của thời đại, nhưng con người suy cho cùng không phải cỗ máy lao động."),
         F(5, "一个人的成功，聪明固然重要，但是努力更重要。 Thành công của một người, thông minh đành rằng quan trọng, nhưng nỗ lực còn quan trọng hơn. Và: 网络固然给我们带来了便利，可是也给我们带来了麻烦。 Mạng internet hẳn nhiên mang lại tiện lợi, nhưng cũng mang lại phiền phức.")])

add("bullets", chapter="Mẫu câu: 亦 · 两码事", section="Mẫu câu 重点句型", title="8. ……亦…… · 9. ……与……是两码事", size=34,
    items=["亦 yì: cũng (văn viết) = 也, đứng trước động từ/tính từ",
           "这种情况现在并不存在，将来亦不会发生。",
           "若能从失败中吸取教训，失败亦是成功，即所谓“失败乃成功之母”。",
           "A与B是两码事: A và B là hai chuyện khác nhau (= 不是一回事)",
           "更重要的是，自觉拼搏与压榨加班是两码事——前者指向个体自由选择，后者指向群体强制遵从。",
           "和父母住不住在一起，和个人的独不独立是两码事。 · 投资和储蓄是两码事，在财务计划中扮演不同的角色。"],
    say=["Hai điểm cuối cùng là 亦 và 两码事.",
         F(0, "亦, đọc thanh bốn, nghĩa là cũng, là cách nói văn viết của 也, đứng trước động từ hoặc tính từ. Trong bài khóa: 悠着点儿、慢生活亦是张弛有度的生活节奏."),
         F(1, "Ví dụ: 这种情况现在并不存在，将来亦不会发生。 Tình huống này hiện nay không hề tồn tại, tương lai cũng sẽ không xảy ra."),
         F(2, "Và: 若能从失败中吸取教训，失败亦是成功，即所谓失败乃成功之母。 Nếu có thể rút ra bài học từ thất bại, thì thất bại cũng là thành công, đúng như câu thất bại là mẹ thành công. Ở đây 若 là nếu, 乃 là là, đều là từ văn viết."),
         F(3, "Mẫu A 与 B 是两码事 nghĩa là A và B là hai chuyện khác nhau; chữ 码 là lượng từ chỉ sự việc. Có thể nói tương đương: A 和 B 不是一回事."),
         F(4, "Ví dụ từ bài khóa: 更重要的是，自觉拼搏与压榨加班是两码事——前者指向个体自由选择，后者指向群体强制遵从。 Đây chính là luận điểm quan trọng nhất của tác giả."),
         F(5, "和父母住不住在一起，和个人的独不独立是两码事。 Có sống chung với bố mẹ hay không, và cá nhân có độc lập hay không, là hai chuyện khác nhau. Và: 投资和储蓄是两码事，在财务计划中扮演不同的角色。 Đầu tư và tiết kiệm là hai chuyện khác nhau, đóng vai trò khác nhau trong kế hoạch tài chính.")])

# ======================= KẾT HỢP TỪ =======================
add("bullets", chapter="Kết hợp từ 词语搭配", section="Kết hợp từ 词语搭配", title="Kết hợp từ (1): 响应 · 控诉 · 情怀", size=34,
    items=["## 响应: ～号召 · 积极～ · 热烈～ · 无人～",
           "青年们积极响应政府的号召，参加绿化祖国的义务劳动。",
           "## 控诉: ～罪行 · ～暴行 · 血泪～ · ～时代",
           "画家用手中的笔控诉着那个黑暗的时代。",
           "## 情怀: 高尚的～ · 浪漫主义～ · 伤感的～ · 无私的～ · 富有～",
           "善良是一种美德，是一种高尚的情怀。"],
    say=["Tiếp theo là phần kết hợp từ, sách gọi là 词语搭配. Học từ theo cụm sẽ giúp các bạn dùng từ tự nhiên như người bản ngữ.",
         F(0, "响应 thường đi với 号召, lời kêu gọi: 响应号召. Ngoài ra có 积极响应, tích cực hưởng ứng; 热烈响应, nhiệt liệt hưởng ứng; 无人响应, không ai hưởng ứng."),
         F(1, "Ví dụ: 青年们积极响应政府的号召，参加绿化祖国的义务劳动。 Thanh niên tích cực hưởng ứng lời kêu gọi của chính phủ, tham gia lao động tình nguyện phủ xanh đất nước."),
         F(2, "控诉 đi với 罪行, tội ác; 暴行, hành vi tàn bạo; 血泪控诉, lời tố cáo đẫm máu và nước mắt; và 控诉时代, tố cáo một thời đại."),
         F(3, "Ví dụ: 画家用手中的笔控诉着那个黑暗的时代。 Người họa sĩ dùng ngòi bút trong tay để tố cáo thời đại đen tối ấy."),
         F(4, "情怀 đi với các tính từ: 高尚的情怀, tấm lòng cao thượng; 浪漫主义情怀, tâm hồn lãng mạn; 伤感的情怀, nỗi niềm buồn thương; 无私的情怀, tấm lòng vô tư; và 富有情怀, giàu tâm huyết."),
         F(5, "Ví dụ: 善良是一种美德，是一种高尚的情怀。 Lương thiện là một đức tính tốt, là một tấm lòng cao thượng.")])

add("bullets", section="Kết hợp từ 词语搭配", title="Kết hợp từ (2): 呼吁 · 遏制 · 姿态", size=34,
    items=["## 呼吁: ～捐款 · ～环保 · ～公平 · ～平等 · 积极～ · 大力～",
           "我要向社会大力呼吁保障女性平等的就业机会。",
           "## 遏制: ～人口增长 · ～通货膨胀 · ～发展 · ～腐败 · ～……现象",
           "民众期待新的就业政策能够有效遏制失业率的持续上升。",
           "## 姿态: 放低～ · 高～ · 低～ · ～万千 · ～优美",
           "同学们个个准备以全新的姿态迎接新学期的到来。"],
    say=[F(0, "呼吁 đi với nội dung được kêu gọi: 呼吁捐款, kêu gọi quyên góp; 呼吁环保, kêu gọi bảo vệ môi trường; 呼吁公平，呼吁平等. Và hai trạng ngữ: 积极呼吁, 大力呼吁, ra sức kêu gọi."),
         F(1, "Ví dụ: 我要向社会大力呼吁保障女性平等的就业机会。 Tôi muốn ra sức kêu gọi xã hội bảo đảm cơ hội việc làm bình đẳng cho phụ nữ. Câu này dẫn đúng vào chủ đề bài sáu chấm ba đấy.", cap="Ví dụ: 我要向社会大力呼吁保障女性平等的就业机会。 Tôi muốn ra sức kêu gọi xã hội bảo đảm cơ hội việc làm bình đẳng cho phụ nữ. Câu này dẫn đúng vào chủ đề bài 6.3 đấy."),
         F(2, "遏制 đi với những thứ cần kìm hãm: 遏制人口增长, kìm hãm tăng dân số; 遏制通货膨胀, kiềm chế lạm phát; 遏制腐败, ngăn chặn tham nhũng; và mẫu 遏制什么现象, như trong bài: 遏制过度加班现象."),
         F(3, "Ví dụ: 民众期待新的就业政策能够有效遏制失业率的持续上升。 Người dân mong chính sách việc làm mới có thể kìm hãm hiệu quả việc tỉ lệ thất nghiệp liên tục tăng."),
         F(4, "姿态 có hai nhóm kết hợp. Nghĩa thái độ: 放低姿态, hạ thấp mình; 高姿态, thái độ rộng lượng, cao thượng; 低姿态, thái độ khiêm nhường. Nghĩa dáng vẻ: 姿态万千, muôn hình muôn vẻ; 姿态优美, dáng điệu uyển chuyển."),
         F(5, "Ví dụ: 同学们个个准备以全新的姿态迎接新学期的到来。 Các bạn học sinh ai cũng chuẩn bị đón học kỳ mới với một tâm thế hoàn toàn mới.")])

add("bullets", section="Kết hợp từ 词语搭配", title="Kết hợp từ (3): 致命 · 拼搏 · 取向 · 刚需", size=33,
    items=["## 致命: ～伤 · ～一击 · ～弱点 · ～错误",
           "爸爸因车祸去世，这对她来说是一个致命的打击。",
           "## 拼搏: ～精神 · 顽强～ · 奋力～",
           "篮球场上，队员们个个生龙活虎，奋力拼搏，投进一个又一个好球。",
           "## 取向: 价值～ · 错误～ · 人文主义～ · 以……为～",
           "以结果为取向的评价考核方式，导致了急功近利的行为。",
           "## 刚需: ～买家 · ～楼盘 · ～价 · ～供应",
           "问题的关键是，水电是刚需，无论涨价与否，百姓不能不用。"],
    say=[F(0, "致命 đi với 伤, vết thương; 一击, một đòn; 弱点, điểm yếu; 错误, sai lầm: vết thương chí mạng, đòn chí mạng, điểm yếu chí mạng, sai lầm chết người."),
         F(1, "Ví dụ: 爸爸因车祸去世，这对她来说是一个致命的打击。 Bố qua đời vì tai nạn xe, đối với cô ấy đây là một cú sốc nặng nề."),
         F(2, "拼搏 đi với 精神: 拼搏精神, tinh thần phấn đấu; và hai trạng ngữ 顽强拼搏, kiên cường phấn đấu; 奋力拼搏, dốc sức chiến đấu."),
         F(3, "Ví dụ: 篮球场上，队员们个个生龙活虎，奋力拼搏，投进一个又一个好球。 Trên sân bóng rổ, các cầu thủ ai nấy đều khỏe khoắn sung sức, dốc sức chiến đấu, ném vào hết quả này đến quả khác. 生龙活虎 là thành ngữ, nghĩa là hăng hái như rồng như hổ."),
         F(4, "取向 đi với 价值取向, định hướng giá trị; 错误取向, định hướng sai lầm; 人文主义取向, khuynh hướng nhân văn; và mẫu 以什么为取向, lấy cái gì làm định hướng."),
         F(5, "Ví dụ: 以结果为取向的评价考核方式，导致了急功近利的行为。 Cách đánh giá lấy kết quả làm định hướng đã dẫn đến những hành vi hám lợi trước mắt. 急功近利 là nóng vội cầu thành tích, ham lợi trước mắt."),
         F(6, "刚需 đi với 刚需买家, người mua có nhu cầu thật; 刚需楼盘, dự án nhà ở cho người có nhu cầu thật; 刚需价, mức giá cho nhu cầu thiết yếu; 刚需供应, nguồn cung thiết yếu."),
         F(7, "Ví dụ: 问题的关键是，水电是刚需，无论涨价与否，百姓不能不用。 Mấu chốt vấn đề là điện nước là nhu cầu thiết yếu, dù có tăng giá hay không, người dân cũng không thể không dùng.")])

# ======================= THÀNH NGỮ =======================
add("bullets", chapter="Thành ngữ & quán dụng ngữ", section="Thành ngữ 成语与惯用语", title="Thành ngữ (1): 一石激起千层浪 · 夜以继日 · 耸人听闻 · 层出不穷", size=33,
    items=["## 一石激起千层浪 – một hòn đá khuấy lên nghìn lớp sóng: việc nhỏ gây phản ứng lớn",
           "该市实施了教育体制改革的多项措施，一石激起千层浪，在社会上产生了强烈的反响。",
           "## 夜以继日 yèyǐjìrì – lấy đêm nối ngày, làm việc không nghỉ",
           "为了提前完成任务，工人们都在夜以继日地工作着。",
           "## 耸人听闻 sǒngréntīngwén – phóng đại, bịa đặt khiến người nghe kinh hãi",
           "许多媒体为了吸引读者，经常刊登一些耸人听闻的消息。",
           "## 层出不穷 céngchū-bùqióng – liên tiếp xuất hiện, không bao giờ hết",
           "现代社会的特点是新事物层出不穷，瞬息万变。"],
    say=["Bài này có rất nhiều thành ngữ và quán dụng ngữ, sách liệt kê mười sáu mục. Chúng ta học bốn mục một lần.",
         F(0, "一石激起千层浪: ném một hòn đá xuống nước, làm dậy lên nghìn lớp sóng. Ý nói một lời nói hay một việc làm nhỏ gây ra phản ứng mạnh mẽ trong xã hội."),
         F(1, "Ví dụ: 该市实施了教育体制改革的多项措施，一石激起千层浪，在社会上产生了强烈的反响。 Thành phố này thực hiện nhiều biện pháp cải cách thể chế giáo dục, một hòn đá khuấy nghìn lớp sóng, tạo nên tiếng vang mạnh mẽ trong xã hội."),
         F(2, "夜以继日: 夜 là đêm, 继 là nối tiếp: lấy đêm nối vào ngày, ý nói làm việc, học tập liên tục không nghỉ."),
         F(3, "Ví dụ: 为了提前完成任务，工人们都在夜以继日地工作着。 Để hoàn thành nhiệm vụ trước thời hạn, công nhân đều đang làm việc ngày đêm."),
         F(4, "耸人听闻: 耸 là làm kinh động. Nghĩa là phóng đại hoặc bịa đặt sự việc khiến người nghe kinh ngạc, sửng sốt. Giống tiếng Việt: giật gân."),
         F(5, "Ví dụ: 许多媒体为了吸引读者，经常刊登一些耸人听闻的消息。 Nhiều báo chí, để thu hút độc giả, thường đăng những tin tức giật gân."),
         F(6, "层出不穷: 层 là lặp đi lặp lại, 穷 là hết. Nghĩa là liên tiếp xuất hiện, không bao giờ hết."),
         F(7, "Ví dụ: 现代社会的特点是新事物层出不穷，瞬息万变。 Đặc điểm của xã hội hiện đại là cái mới liên tục xuất hiện, thay đổi trong chớp mắt.")])

add("bullets", section="Thành ngữ 成语与惯用语", title="Thành ngữ (2): 匪夷所思 · 矢口否认 · 不以为耻，反以为荣 · 英年早逝", size=33,
    items=["## 匪夷所思 fěiyísuǒsī – kỳ quặc, trái lẽ thường đến mức khó tưởng tượng",
           "一家五星级酒店居然十点之后就没有热水了，简直是匪夷所思。",
           "## 矢口否认 shǐkǒu-fǒurèn – một mực chối cãi, nhất quyết không nhận",
           "铁证如山，他还在矢口否认自己的罪行。",
           "## 不以为耻，反以为荣 – không lấy làm xấu hổ, ngược lại còn lấy làm vẻ vang",
           "他因丑闻登上了热搜榜，可他本人却不以为耻，反以为荣。",
           "## 英年早逝 yīngnián-zǎoshì – qua đời khi còn trẻ, đang tuổi tráng niên",
           "他英年早逝，真令人痛惜。"],
    say=[F(0, "匪夷所思: chữ 匪 là không phải, 夷 là người bình thường, 所思 là điều nghĩ tới: không phải điều người bình thường có thể nghĩ ra. Ý nói lời nói, hành động trái lẽ thường, khiến người ta khó tưởng tượng, khó hiểu nổi."),
         F(1, "Ví dụ: 一家五星级酒店居然十点之后就没有热水了，简直是匪夷所思。 Một khách sạn năm sao mà sau mười giờ đêm đã hết nước nóng, thật không thể tin nổi."),
         F(2, "矢口否认: 矢口 là một mực, khăng khăng. Nghĩa là một mực chối cãi, nhất quyết không thừa nhận."),
         F(3, "Ví dụ: 铁证如山，他还在矢口否认自己的罪行。 Bằng chứng rành rành như núi, hắn vẫn một mực chối tội."),
         F(4, "不以为耻，反以为荣: không lấy làm xấu hổ, ngược lại còn lấy làm vinh quang. Dùng để chê người làm điều sai trái mà còn tự đắc."),
         F(5, "Ví dụ: 他因丑闻登上了热搜榜，可他本人却不以为耻，反以为荣。 Anh ta lên bảng tìm kiếm nóng vì bê bối, vậy mà bản thân không lấy làm xấu hổ, còn lấy làm vẻ vang."),
         F(6, "英年早逝: 英年 là tuổi thanh xuân, tráng niên. Nghĩa là qua đời khi còn đang trẻ, đang ở độ tuổi sung sức nhất."),
         F(7, "Ví dụ: 他英年早逝，真令人痛惜。 Anh ấy mất khi còn trẻ, thật khiến người ta đau xót.")])

add("bullets", section="Thành ngữ 成语与惯用语", title="Thành ngữ (3): 柴米油盐 · 国计民生 · 肆无忌惮 · 悠着点儿", size=33,
    items=["## 柴米油盐 chái-mǐ-yóu-yán – củi gạo dầu muối: chuyện cơm áo hằng ngày",
           "所谓爱情就是花前月下，卿卿我我，所谓婚姻就是家长里短，柴米油盐。",
           "## 国计民生 guójì-mínshēng – kinh tế quốc gia và đời sống nhân dân",
           "抓好教育工作是关系到国计民生的一件大事。",
           "## 肆无忌惮 sìwú-jìdàn – ngang nhiên, không kiêng nể gì",
           "他竟然在会上指名道姓地对别人进行人身攻击，真是肆无忌惮。",
           "## 悠着点儿 yōuzhe diǎnr – cứ từ từ, đừng nóng vội, đừng quá sức",
           "慢慢来，悠着点儿，心急吃不了热豆腐。"],
    say=[F(0, "柴米油盐: củi, gạo, dầu, muối, chỉ những thứ thiết yếu cho ba bữa ăn hằng ngày, tức là chuyện cơm áo gạo tiền."),
         F(1, "Ví dụ: 所谓爱情就是花前月下，卿卿我我，所谓婚姻就是家长里短，柴米油盐。 Cái gọi là tình yêu là hẹn hò dưới trăng bên hoa, quấn quýt bên nhau; còn hôn nhân là chuyện vặt trong nhà ngoài ngõ, là cơm áo gạo tiền. Các bạn để ý, câu này lại dùng mẫu 所谓."),
         F(2, "国计民生: 国计 là kế sách, kinh tế của quốc gia; 民生 là đời sống nhân dân. Hán Việt là quốc kế dân sinh."),
         F(3, "Ví dụ: 抓好教育工作是关系到国计民生的一件大事。 Làm tốt công tác giáo dục là một việc lớn liên quan đến quốc kế dân sinh."),
         F(4, "肆无忌惮: 肆 là phóng túng, 忌 là kiêng kỵ, 惮 là sợ. Nghĩa là hết sức ngang ngược, không kiêng nể, không sợ gì cả."),
         F(5, "Ví dụ: 他竟然在会上指名道姓地对别人进行人身攻击，真是肆无忌惮。 Anh ta vậy mà lại nêu đích danh người khác để công kích cá nhân ngay trong cuộc họp, thật là ngang nhiên hết mức."),
         F(6, "悠着点儿 là quán dụng ngữ phương Bắc, nghĩa là làm gì cũng đừng quá vội, cứ thong thả, đừng quá sức."),
         F(7, "Ví dụ: 慢慢来，悠着点儿，心急吃不了热豆腐。 Cứ từ từ, thong thả thôi, nóng vội thì không ăn được đậu phụ nóng. Câu tục ngữ này giống câu dục tốc bất đạt của chúng ta.")])

add("bullets", section="Thành ngữ 成语与惯用语", title="Thành ngữ (4): 张弛有度 · 当务之急 · 冠冕堂皇 · 耍流氓", size=33,
    items=["## 张弛有度 zhāngchí-yǒudù – căng chùng có mức độ, làm và nghỉ hợp lý",
           "演讲的语速要张弛有度，语调要抑扬顿挫。",
           "## 当务之急 dāngwùzhījí – việc cấp bách nhất trước mắt",
           "作为一个中学生，当务之急就是把功课学好。",
           "## 冠冕堂皇 guānmiǎn-tánghuáng – bề ngoài đường hoàng, nghiêm chỉnh (nghĩa chê)",
           "少说些冠冕堂皇的话，多做些实实在在的事情。",
           "## 耍流氓 shuǎ liúmáng – giở trò lưu manh; giở mánh khóe để trục lợi",
           "俗话说，一切不以结婚为目的恋爱都是耍流氓！"],
    say=[F(0, "张弛有度: 张 là căng, 弛 là chùng, 有度 là có chừng mực. Như dây cung lúc căng lúc chùng, ý nói làm việc và nghỉ ngơi, nhanh và chậm phải hợp lý."),
         F(1, "Ví dụ: 演讲的语速要张弛有度，语调要抑扬顿挫。 Tốc độ nói khi diễn thuyết phải có nhanh có chậm, ngữ điệu phải lên bổng xuống trầm."),
         F(2, "当务之急: 当务 là việc đang phải làm, 急 là gấp. Nghĩa là việc cấp bách nhất trong những việc trước mắt."),
         F(3, "Ví dụ: 作为一个中学生，当务之急就是把功课学好。 Là một học sinh trung học, việc cấp bách nhất là học cho tốt."),
         F(4, "冠冕堂皇: 冠冕 là mũ của vua quan thời xưa, 堂皇 là bề thế. Nghĩa là bề ngoài trang nghiêm, đường hoàng, nhưng mang nghĩa chê: nói thì hay mà thực chất rỗng tuếch."),
         F(5, "Ví dụ: 少说些冠冕堂皇的话，多做些实实在在的事情。 Hãy bớt nói những lời đao to búa lớn, làm nhiều việc thiết thực hơn."),
         F(6, "耍流氓: nghĩa gốc là giở trò lưu manh, như ăn vạ, lừa đảo, trêu ghẹo phụ nữ; nghĩa mở rộng là giở mánh khóe, dùng thủ đoạn không chính đáng để trục lợi."),
         F(7, "Ví dụ: 俗话说，一切不以结婚为目的恋爱都是耍流氓！ Người ta thường nói, mọi cuộc yêu đương không nhằm đến hôn nhân đều là giở trò lưu manh. Câu kết bài khóa chính là mô phỏng câu nói này.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 课后练习", title="Bài tập 1: Chọn thành ngữ điền vào chỗ trống (1)", reveal=True, size=33,
    items=["## 当务之急 · 肆无忌惮 · 国计民生 · 英年早逝 · 耸人听闻 · 柴米油盐 · 张弛有度 · 杞人忧天 · 冠冕堂皇 · 匪夷所思",
           "(1) 工作就是这样，有时得加班加点，有时则要悠着点儿，这就是所谓的___。",
           "Đáp án: 张弛有度",
           "(2) 十年树木，百年树人，办好教育是我们的___，也是我们的百年大计。",
           "Đáp án: 当务之急",
           "(3) 如果没有法制，不法分子就会为所欲为，___地做出危害国家和人民利益的坏事来。",
           "Đáp án: 肆无忌惮"],
    say=["Bây giờ chúng ta sang phần luyện tập của sách, gọi là 课后练习, với tiêu đề 趁热打铁, rèn sắt khi còn nóng. Bài tập một: chọn thành ngữ thích hợp điền vào chỗ trống.",
         F(0, "Có mười thành ngữ cho sẵn: 当务之急，肆无忌惮，国计民生，英年早逝，耸人听闻，柴米油盐，张弛有度，杞人忧天，冠冕堂皇，匪夷所思. Trong đó 杞人忧天, lo bò trắng răng, có trong bài khóa nhưng không nằm trong danh sách thành ngữ."),
         F(1, "Câu một: 工作就是这样，有时得加班加点，有时则要悠着点儿，这就是所谓的什么。 Công việc là như vậy, có lúc phải tăng ca, có lúc lại phải thong thả. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 张弛有度. Lúc căng lúc chùng, chính là căng chùng có mức độ."),
         F(3, "Câu hai: 十年树木，百年树人，办好教育是我们的什么，也是我们的百年大计。 Mười năm trồng cây, trăm năm trồng người, làm tốt giáo dục là gì của chúng ta, và cũng là kế lâu dài trăm năm."),
         F(4, "Đáp án: 当务之急. Làm tốt giáo dục là việc cấp bách trước mắt, cũng là kế sách trăm năm."),
         F(5, "Câu ba: 如果没有法制，不法分子就会为所欲为，什么地做出危害国家和人民利益的坏事来。 Nếu không có pháp chế, kẻ phạm pháp sẽ muốn làm gì thì làm."),
         F(6, "Đáp án: 肆无忌惮. 肆无忌惮地做出坏事来, ngang nhiên làm điều xấu. Gợi ý là chữ 地 phía sau: chỗ trống cần một thành ngữ làm trạng ngữ.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 1: Chọn thành ngữ điền vào chỗ trống (2)", reveal=True, size=33,
    items=["(4) 爱情虽然甜蜜，回到现实，我们会为生活中的___和一些琐碎的家务事烦恼，这时我们也许会怀疑爱情是否已经结束了。",
           "Đáp án: 柴米油盐",
           "(5) 有人看到现在社会风气不好，就担心要出大乱子，这真是___。",
           "Đáp án: 杞人忧天",
           "(6) 对于有关___这样的大事，改革必须慎之又慎。",
           "Đáp án: 国计民生",
           "(7) 最近发生了好几起___的枪支犯罪，令人忧心忡忡。",
           "Đáp án: 耸人听闻"],
    say=[F(0, "Câu bốn: 爱情虽然甜蜜，回到现实，我们会为生活中的什么和一些琐碎的家务事烦恼，这时我们也许会怀疑爱情是否已经结束了。 Tình yêu tuy ngọt ngào, nhưng trở về thực tế, chúng ta sẽ phiền não vì những gì trong cuộc sống và việc nhà vụn vặt."),
         F(1, "Đáp án: 柴米油盐. Chuyện cơm áo gạo tiền và việc nhà lặt vặt."),
         F(2, "Câu năm: 有人看到现在社会风气不好，就担心要出大乱子，这真是什么。 Có người thấy phong khí xã hội không tốt, liền lo sắp xảy ra loạn lớn."),
         F(3, "Đáp án: 杞人忧天. Lo lắng vô căn cứ, đúng là lo bò trắng răng."),
         F(4, "Câu sáu: 对于有关什么这样的大事，改革必须慎之又慎。 Đối với những việc lớn liên quan đến cái gì, cải cách phải hết sức thận trọng."),
         F(5, "Đáp án: 国计民生. 慎之又慎 là cẩn thận lại càng cẩn thận."),
         F(6, "Câu bảy: 最近发生了好几起什么的枪支犯罪，令人忧心忡忡。 Gần đây xảy ra mấy vụ phạm tội dùng súng như thế nào, khiến người ta lo lắng không yên."),
         F(7, "Đáp án: 耸人听闻. Những vụ án gây chấn động, khiến người nghe kinh hãi.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 1: Chọn thành ngữ điền vào chỗ trống (3)", reveal=True, size=34,
    items=["(8) 他光会说些___的大话，能不能做到又是另外一回事。",
           "Đáp án: 冠冕堂皇",
           "(9) 在千里之外的专家指导当地医生成功实施了一台手术，真令人___。",
           "Đáp án: 匪夷所思",
           "(10) 海子是位极有才华的诗人，却不幸___，令人叹息。",
           "Đáp án: 英年早逝"],
    say=[F(0, "Câu tám: 他光会说些什么的大话，能不能做到又是另外一回事。 Anh ta chỉ giỏi nói những lời to tát thế nào, còn làm được hay không lại là chuyện khác."),
         F(1, "Đáp án: 冠冕堂皇. 冠冕堂皇的大话, những lời đao to búa lớn."),
         F(2, "Câu chín: 在千里之外的专家指导当地医生成功实施了一台手术，真令人什么。 Chuyên gia ở cách xa nghìn dặm hướng dẫn bác sĩ địa phương thực hiện thành công một ca phẫu thuật, thật khiến người ta thế nào?"),
         F(3, "Đáp án: 匪夷所思. Ở đây thành ngữ mang nghĩa tốt: điều trước kia không thể tưởng tượng nổi. Mẫu 令人匪夷所思 rất hay gặp."),
         F(4, "Câu mười: 海子是位极有才华的诗人，却不幸什么，令人叹息。 Hải Tử là một nhà thơ cực kỳ tài hoa, nhưng không may thế nào, khiến người ta thở dài tiếc nuối."),
         F(5, "Đáp án: 英年早逝. Nhà thơ Hải Tử mất năm hai mươi lăm tuổi, là một trong những nhà thơ được yêu mến nhất của Trung Quốc đương đại.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn từ thích hợp nhất (1)", reveal=True, size=34,
    items=["(1) 五六十年代，一批血气方刚的青年（  ）国家的号召，自愿报名支援边疆建设。 A.答应 B.响应 C.反应 D.反响",
           "Đáp án: B 响应 – 响应号召 là kết hợp cố định",
           "(2) 听了受害人的（  ），警察都气得不行。 A.控诉 B.指控 C.告诉 D.上诉",
           "Đáp án: A 控诉 – lời tố cáo của nạn nhân",
           "(3) 天外有天，人外有人，无论什么时候，都要放低（  ），才能走得更远。 A.姿势 B.态度 C.姿态 D.状态",
           "Đáp án: C 姿态 – 放低姿态: hạ thấp mình, khiêm tốn"],
    say=["Bài tập hai: chọn từ thích hợp nhất điền vào chỗ trống. Các bạn chú ý, đây đều là những từ gần nghĩa, phải dựa vào kết hợp từ để chọn.",
         F(0, "Câu một: 五六十年代，一批血气方刚的青年什么国家的号召，自愿报名支援边疆建设。 Những năm năm mươi, sáu mươi, một lớp thanh niên sôi nổi nhiệt huyết đã làm gì trước lời kêu gọi của đất nước, tự nguyện đăng ký đi xây dựng vùng biên cương. A, 答应; B, 响应; C, 反应; D, 反响."),
         F(1, "Đáp án: B, 响应. 响应号召 là kết hợp cố định. 答应 là đồng ý, nhận lời; 反应 là phản ứng; 反响 là tiếng vang, phản hồi của xã hội."),
         F(2, "Câu hai: 听了受害人的什么，警察都气得不行。 Nghe xong gì của nạn nhân, cảnh sát đều tức giận vô cùng. A, 控诉; B, 指控; C, 告诉; D, 上诉."),
         F(3, "Đáp án: A, 控诉, lời tố cáo của người bị hại. 指控 là buộc tội, thường do bên công tố đưa ra; 上诉 là kháng cáo lên tòa cấp trên; 告诉 là nói cho biết."),
         F(4, "Câu ba: 天外有天，人外有人，无论什么时候，都要放低什么，才能走得更远。 Núi cao còn có núi cao hơn, lúc nào cũng phải hạ thấp gì thì mới đi được xa hơn. A, 姿势; B, 态度; C, 姿态; D, 状态."),
         F(5, "Đáp án: C, 姿态. 放低姿态 là hạ thấp mình, khiêm tốn, đúng như phần kết hợp từ. 姿势 là tư thế cơ thể; 态度 tuy là thái độ, nhưng không nói 放低态度.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn từ thích hợp nhất (2)", reveal=True, size=34,
    items=["(4) 现代社会婚姻自主，父母不能一味要求子女（  ）自己的意愿。 A.遵守 B.听从 C.遵命 D.遵从",
           "Đáp án: D 遵从 – 遵从……的意愿; 遵守 đi với luật lệ, quy định",
           "(5) 人生就是一个选择的过程，只有那些清楚自己的方向和价值（  ）的人，才能够活得明白和自在。 A.取向 B.趋向 C.选取 D.指向",
           "Đáp án: A 取向 – 价值取向: định hướng giá trị"],
    say=[F(0, "Câu bốn: 现代社会婚姻自主，父母不能一味要求子女什么自己的意愿。 Xã hội hiện đại hôn nhân tự chủ, bố mẹ không thể một mực yêu cầu con cái làm gì với ý muốn của mình. A, 遵守; B, 听从; C, 遵命; D, 遵从."),
         F(1, "Đáp án: D, 遵从. 遵从意愿 là tuân theo ý muốn. 遵守 đi với luật lệ, quy định, như 遵守纪律; 遵命 là vâng lệnh, không mang tân ngữ. 听从 thường đi với 指挥，安排，劝告, không tự nhiên bằng 遵从 khi đi với 意愿."),
         F(2, "Câu năm: 人生就是一个选择的过程，只有那些清楚自己的方向和价值什么的人，才能够活得明白和自在。 Đời người là một quá trình lựa chọn, chỉ những người hiểu rõ phương hướng và giá trị gì của mình, mới sống được sáng suốt và thanh thản. A, 取向; B, 趋向; C, 选取; D, 指向."),
         F(3, "Đáp án: A, 取向. 价值取向 là định hướng giá trị, một kết hợp cố định. 趋向 là xu hướng phát triển; 选取 là động từ chọn lấy; 指向 là chỉ về hướng nào.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ ngữ, mẫu câu cho sẵn trả lời câu hỏi (1)", reveal=True, size=33,
    items=["(1) “996.ICU”指的是什么？（所谓……是指……）",
           "Đáp án gợi ý: 所谓“996.ICU”，是指程序员在代码托管平台上发起的一个项目，意为“工作996，生病ICU”，以此抵制互联网公司超时工作。",
           "(2) 为何要关注过劳加班的年轻人？（无论是……抑或是……哪怕是……都……）",
           "Đáp án gợi ý: 无论是从劳动力红利终结的现实阶段来看，抑或是从健康中国战略的性价比来说，哪怕只是为了柴米油盐的小日子，关注过劳加班的年轻人都体现了文明社会对国计民生的关切。"],
    say=["Bài tập ba: dùng từ ngữ và mẫu câu cho sẵn để trả lời câu hỏi. Đây là câu hỏi mở, thầy đưa ra đáp án gợi ý dựa theo bài khóa.",
         F(0, "Câu một: 九九六点ICU指的是什么？ 九九六点ICU là chỉ cái gì? Dùng mẫu 所谓是指. Các bạn tạm dừng và thử trả lời nhé."),
         F(1, "Gợi ý: 所谓九九六点ICU，是指程序员在代码托管平台上发起的一个项目，意为工作九九六，生病ICU，以此抵制互联网公司超时工作。"),
         F(2, "Câu hai: 为何要关注过劳加班的年轻人？ Vì sao phải quan tâm đến những người trẻ làm thêm quá sức? Dùng mẫu 无论是，抑或是，哪怕是，都."),
         F(3, "Gợi ý: 无论是从劳动力红利终结的现实阶段来看，抑或是从健康中国战略的性价比来说，哪怕只是为了柴米油盐的小日子，关注过劳加班的年轻人都体现了文明社会对国计民生的关切。")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ ngữ, mẫu câu cho sẵn trả lời câu hỏi (2)", reveal=True, size=34,
    items=["(3) 996工作制日益普遍的原因何在？（……之所以……，说到底……，无非是……）",
           "Đáp án gợi ý: 996工作制之所以日益普遍，说到底，无非是两个症结：一是法律责任的缺位，二是文化价值的错位。",
           "(4) 拼搏与压榨有何区别？（……与……是两码事）",
           "Đáp án gợi ý: 自觉拼搏与压榨加班是两码事：前者是个人的自由选择，后者是企业强迫员工遵从。"],
    say=[F(0, "Câu ba: 九九六工作制日益普遍的原因何在？ Nguyên nhân khiến chế độ 九九六 ngày càng phổ biến nằm ở đâu? Dùng mẫu 之所以，说到底，无非是. 何在 là ở đâu, văn viết."),
         F(1, "Gợi ý: 九九六工作制之所以日益普遍，说到底，无非是两个症结：一是法律责任的缺位，二是文化价值的错位。"),
         F(2, "Câu bốn: 拼搏与压榨有何区别？ Phấn đấu và bóc lột khác nhau thế nào? Dùng mẫu 与，是两码事. 有何 là có gì, văn viết của 有什么."),
         F(3, "Gợi ý: 自觉拼搏与压榨加班是两码事：前者是个人的自由选择，后者是企业强迫员工遵从。 Tự giác phấn đấu và bị bóc lột bằng tăng ca là hai chuyện khác nhau: cái trước là lựa chọn tự do của cá nhân, cái sau là doanh nghiệp ép nhân viên phải phục tùng.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Chọn từ cho sẵn điền vào đoạn văn", reveal=True, size=33,
    items=["## 亚健康 · 悠着点儿 · 过劳死 · 压榨 · 症结 · 猝死",
           "日前，又一程序员在公司___，引发了人们的广泛讨论。人们意识到，加班熬夜造成___并不是杞人忧天，虽然人们常说年轻就是资本，但也需要___。实际上，鲜有年轻人真正想“用命换钱”，___在于，许多企业披着“忠诚”和“敬业”的外衣肆无忌惮地___员工，因此员工不得不超负荷工作，以至于身体常年处于___状态。",
           "Đáp án: 猝死 · 过劳死 · 悠着点儿 · 症结 · 压榨 · 亚健康"],
    say=["Bài tập bốn: chọn từ cho sẵn điền vào đoạn văn. Có sáu từ: 亚健康，悠着点儿，过劳死，压榨，症结，猝死.",
         F(1, "日前，又一程序员在公司什么，引发了人们的广泛讨论。人们意识到，加班熬夜造成什么并不是杞人忧天，虽然人们常说年轻就是资本，但也需要什么。实际上，鲜有年轻人真正想用命换钱，什么在于，许多企业披着忠诚和敬业的外衣肆无忌惮地什么员工，因此员工不得不超负荷工作，以至于身体常年处于什么状态。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 猝死，过劳死，悠着点儿，症结，压榨，亚健康. Cả đoạn là: 日前，又一程序员在公司猝死，引发了人们的广泛讨论。人们意识到，加班熬夜造成过劳死并不是杞人忧天，虽然人们常说年轻就是资本，但也需要悠着点儿。"),
         F(2, "实际上，鲜有年轻人真正想用命换钱，症结在于，许多企业披着忠诚和敬业的外衣肆无忌惮地压榨员工，因此员工不得不超负荷工作，以至于身体常年处于亚健康状态。 Thực ra, hiếm có người trẻ nào thật sự muốn đổi mạng lấy tiền; mấu chốt là nhiều doanh nghiệp đội lốt trung thành và tận tụy để ngang nhiên bóc lột nhân viên, khiến nhân viên phải làm việc quá tải, cơ thể quanh năm ở trong tình trạng sức khỏe kém. 鲜有 là hiếm có."),
         "Các bạn thấy không, đoạn văn này gần như là bản tóm tắt của cả bài khóa, lại dùng thêm 披着的外衣 và 肆无忌惮. Hãy đọc to cả đoạn vài lần nhé."])

# ======================= THẢO LUẬN =======================
add("bullets", chapter="Thảo luận: làm thêm giờ ở Việt Nam", section="Thảo luận 讨论", title="Thảo luận: “996” ở Trung Quốc và chuyện tăng ca ở Việt Nam", reveal=True, size=33,
    items=["(1) 你怎么看“996工作制”？",
           "Đáp án gợi ý: 我反对“996”。偶尔加班可以理解，但长期加班会损害健康。况且自觉拼搏与压榨加班是两码事。",
           "(2) 如果公司按时足额发放加班费，你愿意“996”吗？",
           "Đáp án gợi ý: 短期内也许愿意，但长期不愿意。钱固然重要，但是健康和家人更重要。",
           "(3) 越南的法律对工作时间是怎么规定的？",
           "Đáp án gợi ý: 越南《劳动法》规定，正常工作时间每天不超过8小时，每周不超过48小时；加班每月一般不超过40小时。"],
    say=["Cuối cùng, chúng ta cùng thảo luận, liên hệ với thực tế Việt Nam. Các bạn hãy thử trả lời bằng tiếng Trung, dùng những mẫu câu vừa học.",
         F(0, "Câu một: 你怎么看九九六工作制？ Bạn nghĩ thế nào về chế độ làm việc 九九六?"),
         F(1, "Gợi ý: 我反对九九六。偶尔加班可以理解，但长期加班会损害健康。况且自觉拼搏与压榨加班是两码事。 Tôi phản đối 九九六. Thỉnh thoảng tăng ca thì có thể hiểu được, nhưng tăng ca lâu dài sẽ hại sức khỏe. Hơn nữa, tự giác phấn đấu và bị bóc lột bằng tăng ca là hai chuyện khác nhau."),
         F(2, "Câu hai: 如果公司按时足额发放加班费，你愿意九九六吗？ Nếu công ty trả đủ và đúng hạn tiền tăng ca, bạn có chịu làm 九九六 không?"),
         F(3, "Gợi ý: 短期内也许愿意，但长期不愿意。钱固然重要，但是健康和家人更重要。 Trong thời gian ngắn thì có lẽ chịu, nhưng lâu dài thì không. Tiền đành rằng quan trọng, nhưng sức khỏe và gia đình còn quan trọng hơn."),
         F(4, "Câu ba: 越南的法律对工作时间是怎么规定的？ Luật pháp Việt Nam quy định về thời giờ làm việc như thế nào?"),
         F(5, "Gợi ý: 越南劳动法规定，正常工作时间每天不超过八小时，每周不超过四十八小时；加班每月一般不超过四十小时。 Bộ luật Lao động năm hai nghìn không trăm mười chín của Việt Nam quy định thời giờ làm việc bình thường không quá tám giờ một ngày, bốn mươi tám giờ một tuần, làm thêm thường không quá bốn mươi giờ một tháng. Còn ở Trung Quốc, năm hai nghìn không trăm hai mươi mốt, Tòa án Nhân dân Tối cao và Bộ Nhân lực, An sinh xã hội đã công bố các vụ án điển hình, khẳng định chế độ 九九六 là vi phạm luật lao động.",
           cap="Gợi ý: 越南劳动法规定，正常工作时间每天不超过8小时，每周不超过48小时；加班每月一般不超过40小时。 Bộ luật Lao động 2019 của Việt Nam: không quá 8 giờ/ngày, 48 giờ/tuần, làm thêm thường không quá 40 giờ/tháng. Năm 2021, Tòa án Nhân dân Tối cao và Bộ Nhân lực – An sinh xã hội Trung Quốc khẳng định “996” là trái luật.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 6.1", size=34,
    items=["Từ vựng trọng tâm: 抵制 · 响应 · 控诉 · 呼吁 · 遏制 · 申诉 · 足额 · 调休 · 亚健康 · 症结 · 错位 · 压榨 · 压根儿 · 取向 · 刚需",
           "Mẫu câu: 所谓……是指…… · ……而已/罢了 · 披着……的外衣 · 无论是……抑或是……哪怕是……都…… · 说到底 · 固然……但是…… · 亦 · ……与……是两码事",
           "Thành ngữ: 一石激起千层浪 · 耸人听闻 · 匪夷所思 · 矢口否认 · 肆无忌惮 · 张弛有度 · 当务之急 · 冠冕堂皇",
           "## Bài tập về nhà",
           "Viết đoạn văn khoảng 300 chữ: 你怎么看“996工作制”？ – dùng ít nhất 3 mẫu câu của bài"],
    say=["Chúng ta cùng tổng kết bài sáu chấm một.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 抵制，响应，控诉，呼吁，遏制，申诉，足额，调休，亚健康，症结，错位，压榨，压根儿，取向，刚需. Nhớ cả cách đọc đặc biệt của 症结，调休 và 压根儿 nhé."),
         F(1, "Về mẫu câu: 所谓是指 để định nghĩa khái niệm; 而已 và 罢了 nghĩa là mà thôi; 披着的外衣 nghĩa là đội lốt; 无论是，抑或是，哪怕是，都 nghĩa là dù thế nào kết quả cũng không đổi; 说到底 là suy cho cùng; 固然但是 để nhượng bộ rồi chuyển ý; 亦 là cũng; và 两码事 là hai chuyện khác nhau."),
         F(2, "Về thành ngữ: 一石激起千层浪，耸人听闻，匪夷所思，矢口否认，肆无忌惮，张弛有度，当务之急，冠冕堂皇. Đây đều là những thành ngữ rất hay gặp trong báo chí Trung Quốc."),
         F(4, "Bài tập về nhà: hãy viết một đoạn văn khoảng ba trăm chữ trả lời câu hỏi 你怎么看九九六工作制？ Bạn nghĩ gì về chế độ 九九六? Hãy dùng ít nhất ba mẫu câu của bài, ví dụ 所谓是指，固然但是, và 两码事, và liên hệ với chuyện tăng ca ở Việt Nam."),
         {"t": "Cảm ơn các bạn đã theo dõi bài giảng. Bài sau, bài sáu chấm hai, chúng ta vẫn ở Đơn vị sáu, chủ đề Nơi làm việc, với bài 谁能站在新职业风口？ Ai có thể đứng ở đầu ngọn gió của nghề nghiệp mới? Chúng ta sẽ tìm hiểu những nghề mới như tuyển thủ thể thao điện tử, người livestream bán hàng, và cách giới trẻ Trung Quốc chọn nghề. Hẹn gặp lại các bạn. Chúc các bạn học tốt!",
          "cap": "Cảm ơn các bạn đã theo dõi bài giảng. Bài sau, bài 6.2, chúng ta vẫn ở Đơn vị 6, chủ đề Nơi làm việc, với bài 谁能站在新职业风口？ Ai có thể đứng ở đầu ngọn gió của nghề nghiệp mới? Hẹn gặp lại các bạn. Chúc các bạn học tốt!"}])

lesson = {
    "title": "顶石中文 – Bài 6.1: 职场 996 (Văn hóa làm việc “996”)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"响应": "响映",              # xiǎngyìng
                    "反应": "反映",              # fǎnyìng
                    "呼吁": "呼喻",              # hūyù
                    "调休": "条休",              # tiáoxiū
                    "调查": "掉查",              # diàochá
                    "语调": "语掉",              # yǔdiào
                    "症结": "征结",              # zhēngjié
                    "倒逼": "到逼",              # dàobī
                    "压根": "亚根",              # yàgēnr
                    "熬": "敖",                  # áo (熬夜 – trong bài luôn đọc áo)
                    "扎实": "渣实",              # zhāshi
                    "蔓延": "漫延",              # mànyán
                    "处于": "楚于",              # chǔyú
                    "年假": "年驾",              # niánjià
                    "名为": "名维",              # míngwéi
                    "意为": "意维",              # yìwéi
                    "仅为": "仅维",              # jǐnwéi
                    "为何": "位何",              # wèihé
                    "为荣": "维荣",              # yǐ…wéi róng
                    "为目的": "维目的",          # wéi mùdì
                    "为所欲为": "维所欲维",      # wéisuǒyùwéi
                    "就曾": "就层",              # céng
                    "好奇": "号奇",              # hàoqí
                    "增长": "增涨",              # zēngzhǎng
                    "分子": "份子",              # fènzǐ (不法分子)
                    "强迫": "抢迫",              # qiǎngpò
                    "行业": "航业",              # hángyè
                    "角色": "决色",              # juésè
                    "流氓": "流忙",              # liúmáng
                    "家长里短": "家常里短",      # jiācháng lǐduǎn
                    "吃不了": "吃不蓼",          # chī bu liǎo
                    "失业率": "失业律",          # shīyèlǜ
                    "血泪": "谑泪",              # xuèlèi
                    "血气": "谑气"},             # xuèqì
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds61.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
