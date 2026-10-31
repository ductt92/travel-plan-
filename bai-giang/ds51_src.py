#!/usr/bin/env python3
"""Kịch bản bài giảng 顶石中文 – Bài 5.1 «对家暴必须“零容忍”». Chạy để sinh ds51.json."""
import json
import os

TAG = "顶石中文 · Bài 5.1 · 对家暴必须“零容忍”"
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
    zh="对家暴必须“零容忍”", py="Duì jiābào bìxū “líng róngrěn”",
    vi="Bài 5.1: Phải “không khoan nhượng” với bạo lực gia đình",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng giáo trình 顶石中文, Đỉnh cao tiếng Trung.",
         "Hôm nay chúng ta bắt đầu Đơn vị năm: 家庭篇, chủ đề Gia đình. Bài đầu tiên của đơn vị là bài năm chấm một: 对家暴必须零容忍。 Nghĩa là: Phải không khoan nhượng với bạo lực gia đình.",
         "Bài khóa là một bài bình luận đăng trên 人民日报, báo Nhân dân, viết sau một vụ bạo lực gia đình gây xôn xao mạng xã hội Trung Quốc. Tác giả phân tích vì sao nạn nhân thường im lặng, pháp luật đã làm gì, và xã hội cần làm gì để không ai phải chịu đựng một mình.",
         "Đây là một chủ đề nặng nề nhưng rất thiết thực. Học xong bài này, các bạn sẽ có đủ từ ngữ để đọc báo, nghe tin tức và bày tỏ quan điểm về bạo lực gia đình bằng tiếng Trung."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài bình luận: nguyên nhân của bạo lực gia đình và vì sao phải “零容忍”",
           "Nắm vững 43 từ mới, kèm âm Hán Việt và ví dụ",
           "Câu mẫu: 该 · ……，相比之下，…… · 进而 · 宁愿……，也……",
           "Kết hợp từ: 附上 · 摆脱 · 零 · 起",
           "11 thành ngữ, quán ngữ: 直起腰杆 · 家丑不可外扬 · 清官难断家务事 · 熟视无睹……"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu bài bình luận: bạo lực gia đình có những nguyên nhân sâu xa nào, vì sao nạn nhân thường im lặng, và vì sao cả xã hội phải giữ thái độ 零容忍, tức là không dung thứ dù chỉ một chút."),
         F(1, "Thứ hai, nắm vững bốn mươi ba từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt, giải thích nghĩa và đưa ví dụ. Bài này có rất nhiều từ của ngôn ngữ báo chí và pháp luật."),
         F(2, "Thứ ba, bốn câu mẫu: đại từ 该 trong văn phong công văn; cấu trúc 相比之下, nghĩa là so ra thì; liên từ 进而, rồi tiến thêm một bước; và câu lựa chọn 宁愿……也……, thà… chứ không…."),
         F(3, "Thứ tư, bốn nhóm kết hợp từ: 附上，摆脱，零 và lượng từ 起."),
         F(4, "Thứ năm, mười một thành ngữ và quán ngữ, như 直起腰杆，家丑不可外扬，清官难断家务事，熟视无睹. Đây là phần rất đáng học, vì người Trung Quốc dùng chúng thường xuyên khi bàn về chuyện gia đình."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Suy nghĩ trước bài 课前思考", title="Suy nghĩ trước bài học 课前思考", reveal=True, size=34,
    items=["(1) 你接触过家暴的相关案例吗？",
           "Đáp án gợi ý: 我在新闻里看到过不少家暴案例，有的受害者被打了很多次才敢报警。",
           "(2) 你觉得什么样的行为算家暴？",
           "Đáp án gợi ý: 打人、骂人、威胁、长期不理睬对方（冷暴力）、限制人身自由、控制经济，都算家暴。",
           "(3) 你觉得家暴会对一个家庭产生什么危害？",
           "Đáp án gợi ý: 受害者身心受到伤害，夫妻感情破裂，孩子在恐惧中长大，甚至以后也会用暴力解决问题。"],
    say=["Trước khi vào bài, sách đưa ra ba câu hỏi để chúng ta suy nghĩ. Đây là câu hỏi mở, các bạn hãy tạm dừng video và thử trả lời bằng tiếng Trung trước nhé.",
         F(0, "Câu một: 你接触过家暴的相关案例吗？ Bạn đã từng tiếp xúc với vụ việc bạo lực gia đình nào chưa? 案例 là vụ việc, trường hợp cụ thể."),
         F(1, "Đáp án gợi ý: 我在新闻里看到过不少家暴案例，有的受害者被打了很多次才敢报警。 Tôi đã đọc được không ít vụ bạo lực gia đình trên báo, có nạn nhân bị đánh rất nhiều lần mới dám báo cảnh sát."),
         F(2, "Câu hai: 你觉得什么样的行为算家暴？ Theo bạn, hành vi như thế nào thì được coi là bạo lực gia đình?"),
         F(3, "Đáp án gợi ý: 打人、骂人、威胁、长期不理睬对方、限制人身自由、控制经济，都算家暴。 Đánh, chửi, đe dọa, phớt lờ đối phương trong thời gian dài, hạn chế tự do thân thể, kiểm soát kinh tế, đều là bạo lực gia đình. Phớt lờ kéo dài gọi là 冷暴力, bạo lực lạnh; từ này sẽ gặp lại trong bài tập bốn."),
         F(4, "Câu ba: 你觉得家暴会对一个家庭产生什么危害？ Bạn nghĩ bạo lực gia đình gây ra những tác hại gì cho một gia đình?"),
         F(5, "Đáp án gợi ý: 受害者身心受到伤害，夫妻感情破裂，孩子在恐惧中长大，甚至以后也会用暴力解决问题。 Nạn nhân bị tổn thương cả thể xác lẫn tinh thần, tình cảm vợ chồng tan vỡ, con cái lớn lên trong sợ hãi, thậm chí sau này cũng dùng bạo lực để giải quyết vấn đề.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("家暴", "jiābào", "gia bạo", "danh từ", "bạo lực gia đình", "家暴不是家务事，而是违法行为。", "Bạo lực gia đình không phải chuyện riêng trong nhà, mà là hành vi phạm pháp.",
     "Danh từ, là cách nói tắt của 家庭暴力, bạo lực gia đình. Tiếng Trung rất hay rút gọn như vậy trên báo chí. Ta có 家暴事件, vụ bạo lực gia đình; 遭受家暴, bị bạo hành gia đình."),
    ("容忍", "róngrěn", "dung nhẫn", "động từ", "dung thứ, chịu đựng, nhẫn nhịn", "这种行为绝对不能容忍。", "Hành vi này tuyệt đối không thể dung thứ.",
     "Động từ, nghĩa là bao dung và nhẫn nhịn, chịu đựng điều không hay. Tên bài 零容忍 là không dung thứ chút nào, tức là không khoan nhượng."),
    ("牵动", "qiāndòng", "khiên động", "động từ", "tác động đến, làm xao động (lòng người)", "孩子的病情牵动着全家人的心。", "Bệnh tình của đứa trẻ khiến cả nhà lo lắng không yên.",
     "Động từ, nghĩa là một việc khiến suy nghĩ, tình cảm của người ta thay đổi, thường kèm theo lo lắng. Cụm cố định: 牵动着社会公众的心, khiến cả xã hội quan tâm lo lắng. Chữ 牵 là kéo, dắt, như kéo theo trái tim người khác."),
    ("底线", "dǐxiàn", "để tuyến", "danh từ", "giới hạn cuối cùng, ranh giới tối thiểu", "做人要有自己的底线。", "Làm người phải có giới hạn của riêng mình.",
     "Danh từ, nghĩa là điều kiện, tiêu chuẩn, giới hạn thấp nhất, không thể lùi thêm. Trong bài: 挑战道德和文明的底线, thách thức giới hạn tối thiểu của đạo đức và văn minh."),
    ("坠入", "zhuìrù", "trụy nhập", "động từ", "rơi vào, sa vào", "他们俩一见面就坠入了爱河。", "Hai người họ vừa gặp nhau đã rơi vào lưới tình.",
     "Động từ, nghĩa là rơi sâu vào một hoàn cảnh nào đó, không thoát ra được. Hai cụm hay gặp: 坠入深渊, rơi xuống vực thẳm; và 坠入爱河, rơi vào dòng sông tình yêu, tức là phải lòng."),
    ("深渊", "shēnyuān", "thâm uyên", "danh từ", "vực sâu, vực thẳm", "毒品把他推向了犯罪的深渊。", "Ma túy đã đẩy anh ta xuống vực thẳm tội ác.",
     "Danh từ, nghĩa gốc là đầm nước rất sâu, nghĩa bóng là hoàn cảnh nguy hiểm, khốn khổ. Trong bài: 让许多家庭因此坠入深渊, khiến nhiều gia đình vì thế mà rơi xuống vực thẳm."),
    ("噩梦", "èmèng", "ngạc mộng", "danh từ", "ác mộng, cơn mơ đáng sợ", "那次车祸成了他多年的噩梦。", "Vụ tai nạn xe năm ấy đã thành cơn ác mộng nhiều năm của anh ấy.",
     "Danh từ, nghĩa là giấc mơ đáng sợ, nghĩa bóng là trải nghiệm kinh hoàng. Chữ 噩 Hán Việt là ngạc, như trong 噩耗, tin dữ. Trong bài: 我仿佛活在噩梦里, tôi như sống trong cơn ác mộng."),
    ("该", "gāi", "cai", "đại từ", "(người, vật) này, đó – đã nhắc ở trên", "该公司成立于二〇一〇年。", "Công ty này được thành lập năm 2010.",
     "Ở bài này, 该 không phải là nên, mà là đại từ chỉ thị, chỉ người hay sự vật vừa nói ở trên, tương đương 这个, dùng nhiều trong công văn, tin tức. Trong bài: 该博主, blogger này. Lát nữa đây là câu mẫu thứ nhất."),
    ("博主", "bózhǔ", "bác chủ", "danh từ", "chủ blog, blogger (người viết Weibo)", "这位美食博主有几百万粉丝。", "Blogger ẩm thực này có mấy triệu người theo dõi.",
     "Danh từ, từ thông dụng trên mạng, nghĩa gốc là chủ của 博客, blog; nay thường chỉ chủ tài khoản 微博, Weibo, hay người làm nội dung trên mạng."),
    ("附", "fù", "phụ", "động từ", "kèm theo, đính kèm", "信中附寄照片一张。", "Trong thư có gửi kèm một tấm ảnh.",
     "Động từ, nghĩa là kèm theo. Thường nói 附上, đính kèm: 附上影像记录, kèm theo đoạn ghi hình. Trong email, tệp đính kèm gọi là 附件. Đây là một nhóm kết hợp từ của bài."),
    ("声援", "shēngyuán", "thanh viện", "động từ", "lên tiếng ủng hộ", "很多网友在网上声援这位受害者。", "Rất nhiều cư dân mạng lên tiếng ủng hộ nạn nhân này trên mạng.",
     "Động từ, nghĩa là công khai phát biểu để ủng hộ ai đó. 声 là tiếng nói, 援 là viện trợ, giúp đỡ: giúp đỡ bằng tiếng nói."),
    ("决断", "juéduàn", "quyết đoán", "động từ", "đưa ra quyết định dứt khoát", "关键时刻，他必须做出决断。", "Vào thời khắc then chốt, anh ấy phải đưa ra quyết định.",
     "Động từ, nghĩa là quyết định, đưa ra chủ ý; cũng dùng như danh từ: 做出决断. Cẩn thận: tiếng Việt quyết đoán thường là tính từ chỉ tính cách; còn trong bài, 理性的决断 là một quyết định lý trí."),
    ("弱点", "ruòdiǎn", "nhược điểm", "danh từ", "điểm yếu, nhược điểm", "每个人都有自己的弱点。", "Ai cũng có điểm yếu của riêng mình.",
     "Danh từ, nghĩa là chỗ còn thiếu sót, mặt yếu kém. Âm Hán Việt và nghĩa giống hệt tiếng Việt. Trong bài: 毕竟人都有弱点, dù sao con người ai cũng có điểm yếu."),
    ("界线", "jièxiàn", "giới tuyến", "danh từ", "ranh giới, đường phân giới", "工作和生活之间要划清界线。", "Giữa công việc và cuộc sống phải vạch rõ ranh giới.",
     "Danh từ, nghĩa là đường phân chia giữa hai khu vực, hay ranh giới giữa hai sự việc khác nhau. Trong bài: 心软和宽容之间并没有特别明确的界线, giữa mềm lòng và bao dung chẳng có ranh giới rõ ràng nào."),
    ("赡养", "shànyǎng", "thiệm dưỡng", "động từ", "phụng dưỡng (cha mẹ, người già)", "子女有赡养父母的义务。", "Con cái có nghĩa vụ phụng dưỡng cha mẹ.",
     "Động từ, nghĩa là con cái giúp đỡ về vật chất và chăm sóc về đời sống cho cha mẹ, người dưới với người trên. Phân biệt: 抚养 là nuôi con; 赡养 là nuôi cha mẹ. Bài sau sẽ gặp lại hai từ này."),
    ("舆论", "yúlùn", "dư luận", "danh từ", "dư luận, ý kiến công chúng", "这件事引起了社会舆论的广泛关注。", "Việc này đã thu hút sự quan tâm rộng rãi của dư luận xã hội.",
     "Danh từ, nghĩa là ý kiến, lời bàn tán của công chúng. Âm Hán Việt là dư luận, nghĩa giống hệt. Hay gặp 社会舆论，国际舆论，舆论压力."),
    ("施暴", "shībào", "thi bạo", "động từ", "dùng bạo lực, hành hung", "施暴者必须受到法律的惩罚。", "Kẻ bạo hành phải bị pháp luật trừng phạt.",
     "Động từ, nghĩa là dùng bạo lực. Chữ 施 là thi hành, thực hiện. Từ 施暴者 là kẻ bạo hành, xuất hiện nhiều lần trong bài; đối lập với 受害者, nạn nhân."),
    ("行政拘留", "xíngzhèng jūliú", "hành chính câu lưu", "cụm danh từ", "tạm giữ hành chính", "他因打人被行政拘留十天。", "Anh ta bị tạm giữ hành chính mười ngày vì đánh người.",
     "Đây là thuật ngữ pháp luật: cơ quan công an hạn chế tự do thân thể của người vi phạm trật tự quản lý hành chính trong một thời gian ngắn, như một hình thức xử phạt. 拘留 là giam giữ, tạm giữ."),
    ("人身", "rénshēn", "nhân thân", "danh từ", "thân thể, tính mạng, danh dự (của con người)", "法律保护公民的人身自由。", "Pháp luật bảo vệ quyền tự do thân thể của công dân.",
     "Danh từ, chỉ tính mạng, sức khỏe, hành động, danh dự của một người, thường dùng khi nói về bảo vệ hay xâm hại. Hay gặp 人身自由，人身安全. Trong bài: 人身安全保护令, lệnh bảo vệ an toàn thân thể."),
    ("正视", "zhèngshì", "chính thị", "động từ", "nhìn thẳng vào, đối diện nghiêm túc", "我们必须正视自己的缺点。", "Chúng ta phải nhìn thẳng vào khuyết điểm của mình.",
     "Động từ, nghĩa đen là nhìn thẳng, nghĩa bóng là đối diện nghiêm túc, không né tránh, không qua loa. Hay gặp 正视现实, đối diện với thực tế; 正视问题."),
    ("受理", "shòulǐ", "thụ lý", "động từ", "tiếp nhận và giải quyết", "法院已经受理了这个案件。", "Tòa án đã thụ lý vụ án này.",
     "Động từ, nghĩa là tiếp nhận để giải quyết, như tòa án thụ lý vụ án, cơ quan tiếp nhận đơn khiếu nại. Âm Hán Việt giống tiếng Việt. Trong bài: 每年受理四到五万件家暴投诉."),
    ("唏嘘", "xīxū", "hi hư", "động từ", "thở dài, ngậm ngùi", "听完他的故事，大家唏嘘不已。", "Nghe xong câu chuyện của anh ấy, ai nấy đều ngậm ngùi.",
     "Động từ, nghĩa là thở dài, sụt sùi vì xúc động hay thương cảm. Trong bài: 令人唏嘘的家庭悲剧, những bi kịch gia đình khiến người ta ngậm ngùi."),
    ("恶劣", "èliè", "ác liệt", "tính từ", "rất xấu, tồi tệ, khắc nghiệt", "这里的自然环境非常恶劣。", "Môi trường tự nhiên ở đây vô cùng khắc nghiệt.",
     "Tính từ, nghĩa là rất xấu. Đây là từ dễ nhầm: tiếng Việt ác liệt thường nói trận đánh dữ dội; còn 恶劣 là tồi tệ, như 品行恶劣, phẩm hạnh tồi tệ; 环境恶劣, môi trường khắc nghiệt. Trong bài: 恶劣的原生家庭, gia đình gốc tồi tệ."),
    ("施行", "shīxíng", "thi hành", "động từ", "(luật, quy định) có hiệu lực, được thi hành", "这部法律从明年一月一日起施行。", "Bộ luật này có hiệu lực từ ngày mùng một tháng một năm sau.",
     "Động từ, chỉ luật lệ, quy định sau khi công bố thì bắt đầu có hiệu lực từ một thời điểm. Trong bài: 反家庭暴力法正式施行, Luật Chống bạo lực gia đình chính thức có hiệu lực."),
    ("公权力", "gōng quánlì", "công quyền lực", "danh từ", "quyền lực công (của nhà nước)", "要防止滥用公权力。", "Phải ngăn chặn việc lạm dụng quyền lực công.",
     "Danh từ, là tên gọi chung của quyền lực nhà nước, như quyền lập pháp, hành pháp. Còn nói tắt là 公权. Trong bài: 公权力干预家庭暴力, quyền lực nhà nước can thiệp vào bạo lực gia đình."),
    ("进而", "jìn'ér", "tiến nhi", "liên từ", "rồi tiến thêm một bước, từ đó", "先了解情况，进而解决问题。", "Trước hết tìm hiểu tình hình, rồi từ đó giải quyết vấn đề.",
     "Liên từ, biểu thị trên cơ sở đã có, tiến thêm một bước nữa. Đây là câu mẫu thứ ba của bài."),
    ("阐明", "chǎnmíng", "xiển minh", "động từ", "trình bày rõ, làm sáng tỏ", "他在文章中阐明了自己的观点。", "Trong bài viết, anh ấy đã trình bày rõ quan điểm của mình.",
     "Động từ, nghĩa là giải thích rõ ràng một đạo lý, một quan điểm. Văn viết. Chữ 阐 Hán Việt là xiển, nghĩa là làm cho rõ."),
    ("公害", "gōnghài", "công hại", "danh từ", "mối hại chung cho xã hội", "赌博是一大公害。", "Cờ bạc là một mối hại lớn cho xã hội.",
     "Danh từ, chỉ chung những thứ gây hại cho công chúng. Trong bài: 家庭暴力不是个人私事而是社会公害, bạo lực gia đình không phải việc riêng của cá nhân mà là mối hại của xã hội."),
    ("极为", "jíwéi", "cực vi", "phó từ", "cực kỳ, hết sức", "他对这个结果极为不满。", "Anh ấy hết sức bất mãn với kết quả này.",
     "Phó từ, biểu thị mức độ đạt tới cực điểm, văn viết, giống 极其. Chữ thứ hai đọc thanh hai. Trong bài: 极为严重的侵犯, sự xâm phạm cực kỳ nghiêm trọng."),
    ("宁愿", "nìngyuàn", "ninh nguyện", "phó từ", "thà, thà rằng", "我宁愿走路，也不想挤公交车。", "Tôi thà đi bộ còn hơn chen xe buýt.",
     "Phó từ, nghĩa là thà; so sánh hai bên, chỉ chọn một bên và bỏ bên kia. Chữ đầu đọc thanh bốn. Mẫu 宁愿……也…… là câu mẫu thứ tư."),
    ("救济", "jiùjì", "cứu tế", "động từ", "cứu trợ, cứu tế; (pháp lý) bảo vệ, khắc phục", "政府拿出一笔钱救济灾民。", "Chính phủ bỏ ra một khoản tiền để cứu trợ người dân vùng thiên tai.",
     "Động từ, nghĩa là dùng tiền bạc, vật chất giúp đỡ người gặp khó khăn. Trong bài, 救济渠道 là các kênh trợ giúp, các con đường để nạn nhân được bảo vệ quyền lợi."),
    ("通畅", "tōngchàng", "thông sướng", "tính từ", "thông suốt, không bị tắc", "节日期间，这条路一直很通畅。", "Trong dịp lễ, con đường này luôn thông suốt.",
     "Tính từ, nghĩa là đi qua mà không bị cản trở. Dùng cho đường sá, cũng như cho kênh thông tin, hơi thở. Trong bài: 救济渠道不通畅, các kênh trợ giúp không thông suốt."),
    ("反馈", "fǎnkuì", "phản quỹ", "động từ", "phản hồi", "请把顾客的意见及时反馈给我们。", "Xin hãy phản hồi kịp thời ý kiến của khách hàng cho chúng tôi.",
     "Động từ, nghĩa là thông tin, ý kiến được truyền ngược trở lại. Cũng làm danh từ: 及时有效的反馈, sự phản hồi kịp thời và hiệu quả."),
    ("无辜", "wúgū", "vô cô", "tính từ", "vô tội", "事实证明那个人是无辜的。", "Sự thật chứng minh người đó vô tội.",
     "Tính từ, nghĩa là không có tội. Chữ 辜 là tội. Trong bài: 旁观者看似无辜，实则纵容犯罪, người đứng xem tưởng như vô tội, nhưng thực ra là dung túng tội ác."),
    ("纵容", "zòngróng", "túng dung", "động từ", "dung túng, nuông chiều (cái sai)", "父母不能纵容孩子的坏习惯。", "Cha mẹ không được dung túng thói hư của con cái.",
     "Động từ, nghĩa là không ngăn cản hành vi sai trái, mặc cho nó phát triển. Âm Hán Việt túng dung, gần với dung túng của tiếng Việt, chỉ đảo vị trí hai chữ."),
    ("迈出", "màichū", "mại xuất", "động từ", "bước ra, cất bước", "他终于迈出了创业的第一步。", "Cuối cùng anh ấy đã bước bước đầu tiên trên con đường khởi nghiệp.",
     "Động từ, nghĩa là bước ra, sải bước. Cụm hay gặp: 迈出第一步, bước bước đầu tiên. Trong bài: 不再沉默是必须迈出的第一步, không im lặng nữa là bước đầu tiên bắt buộc phải bước."),
    ("起", "qǐ", "khởi", "lượng từ", "vụ, việc (lượng từ cho sự kiện)", "今天早上发生了一起交通事故。", "Sáng nay xảy ra một vụ tai nạn giao thông.",
     "Ở đây 起 là lượng từ, dùng cho sự việc, sự cố, vụ án, giống 件, 次. Hay gặp 一起事故，一起案件，一起事件. Đây cũng là một nhóm kết hợp từ."),
    ("劝阻", "quànzǔ", "khuyến trở", "động từ", "khuyên ngăn", "在大家的劝阻下，他没有开车。", "Nhờ mọi người khuyên ngăn, anh ấy đã không lái xe.",
     "Động từ, nghĩa là khuyên người khác đừng làm một việc gì. 劝 là khuyên, 阻 là ngăn cản."),
    ("报案", "bào'àn", "báo án", "động từ", "trình báo vụ việc với công an", "钱包被偷后，她马上去派出所报案了。", "Bị mất trộm ví, cô ấy lập tức đến đồn công an trình báo.",
     "Động từ ly hợp, nghĩa là báo cho công an hay cơ quan tư pháp biết về một vụ vi phạm pháp luật. Có thể tách ra: 报了案. Gần nghĩa với 报警, báo cảnh sát."),
    ("疏导", "shūdǎo", "sơ đạo", "động từ", "khơi thông; (tâm lý) giải tỏa, hướng dẫn", "老师耐心地对学生进行心理疏导。", "Thầy giáo kiên nhẫn tư vấn tâm lý cho học sinh.",
     "Động từ, nghĩa gốc là khơi thông dòng chảy; trong bài là hướng dẫn, giải tỏa về mặt tâm lý: 心理疏导, tư vấn, gỡ rối tâm lý."),
    ("维权", "wéiquán", "duy quyền", "động từ", "bảo vệ quyền lợi hợp pháp", "消费者要学会依法维权。", "Người tiêu dùng phải biết bảo vệ quyền lợi theo pháp luật.",
     "Động từ, là cách nói tắt của 维护合法权益, bảo vệ quyền lợi hợp pháp. Trong bài: 降低受害者的维权成本, giảm chi phí đòi quyền lợi của nạn nhân."),
    ("凝聚", "níngjù", "ngưng tụ", "động từ", "tập hợp, gắn kết, kết tinh", "我们要凝聚力量，共同面对困难。", "Chúng ta phải tập hợp sức mạnh, cùng nhau đối mặt khó khăn.",
     "Động từ, nghĩa là tụ lại thật sâu, thật chặt. Hay gặp 凝聚力量，凝聚共识，凝聚力, sức gắn kết. Trong bài: 凝聚更广泛的社会共识, tập hợp sự đồng thuận xã hội rộng rãi hơn."),
    ("防线", "fángxiàn", "phòng tuyến", "danh từ", "phòng tuyến, tuyến phòng thủ", "我们要筑起保护儿童的坚固防线。", "Chúng ta phải dựng nên phòng tuyến vững chắc bảo vệ trẻ em.",
     "Danh từ, nghĩa là tuyến ngăn chặn sức mạnh nguy hiểm, bảo vệ an toàn. Động từ đi kèm là 筑起, dựng lên. Câu kết của bài: 筑起反对家庭暴力的坚固防线."),
]

add("bullets", chapter="Từ mới (43 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 5.1 có 43 từ mới, chia thành 15 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Nhiều từ báo chí – pháp luật: 施暴 · 行政拘留 · 受理 · 施行 · 公权力 · 维权",
           "Từ dễ nhầm: 该 (đại từ) · 决断 · 恶劣 · 赡养"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có bốn mươi ba từ, thầy chia thành mười lăm nhóm nhỏ. Các từ có dấu sao trong sách là từ mở rộng, nhưng vì đây là bài báo thật, thầy vẫn giảng đủ cả.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Bài khóa là văn bình luận trên báo, nên có nhiều từ thuộc lĩnh vực pháp luật: 施暴，行政拘留，受理，施行，公权力，维权. Âm Hán Việt của chúng sẽ giúp các bạn nhớ rất nhanh."),
         F(4, "Ngoài ra, có mấy từ cần chú ý: 该 ở đây là đại từ chứ không phải nên; 决断 và 恶劣 có nghĩa khác với quyết đoán, ác liệt trong tiếng Việt; còn 赡养 là phụng dưỡng cha mẹ. Chúng ta bắt đầu.")])

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
    items=["## 国际消除家庭暴力日 – Ngày 25/11",
           "Ngày Quốc tế xóa bỏ bạo lực đối với phụ nữ do Liên Hợp Quốc xác lập; nguồn gốc: ba chị em nhà Mirabal (Dominica) bị sát hại ngày 25/11/1960",
           "## 热搜榜 – bảng tìm kiếm nóng trên Weibo",
           "Thước đo một sự kiện có được công chúng quan tâm hay không",
           "## 妇联 – Hội Liên hiệp Phụ nữ (妇女联合会), thành lập tháng 4/1949",
           "## 《反家庭暴力法》 – Luật Chống bạo lực gia đình, có hiệu lực từ 1/3/2016",
           "Lập ra chế độ 人身安全保护令: lệnh bảo vệ an toàn thân thể cho nạn nhân"],
    say=["Bây giờ chúng ta sang phần hai: bài khóa. Trước khi đọc, các bạn cần biết bốn kiến thức nền mà sách chú thích.",
         F(0, "Thứ nhất: 国际消除家庭暴力日. Đó là ngày hai mươi lăm tháng mười một, Ngày Quốc tế xóa bỏ bạo lực đối với phụ nữ do Liên Hợp Quốc xác lập, ở Trung Quốc còn gọi là Ngày quốc tế xóa bỏ bạo lực gia đình."),
         F(1, "Ngày này bắt nguồn từ một sự kiện năm một nghìn chín trăm sáu mươi: ba chị em nhà Mirabal ở Cộng hòa Dominica bị sát hại vào ngày hai mươi lăm tháng mười một. Năm một nghìn chín trăm chín mươi ba, cũng vào ngày này, Liên Hợp Quốc ra Tuyên bố về xóa bỏ bạo lực đối với phụ nữ."),
         F(2, "Thứ hai: 热搜榜, bảng tìm kiếm nóng trên Weibo, liệt kê những chủ đề được bàn tán nhiều nhất."),
         F(3, "Lên 热搜 là dấu hiệu một sự kiện đã thu hút sự chú ý của cả xã hội. Sách cũng nhắc rằng có hiện tượng bỏ tiền mua hot search để lái sự chú ý của công chúng."),
         F(4, "Thứ ba: 妇联, là tên gọi tắt của 妇女联合会, Hội Liên hiệp Phụ nữ, thành lập tháng tư năm một nghìn chín trăm bốn mươi chín, có nhiệm vụ bảo vệ quyền lợi phụ nữ, thúc đẩy bình đẳng nam nữ. Ở Việt Nam, chúng ta cũng có Hội Liên hiệp Phụ nữ."),
         F(5, "Thứ tư: 反家庭暴力法, Luật Chống bạo lực gia đình, có hiệu lực từ ngày mùng một tháng ba năm hai nghìn không trăm mười sáu."),
         F(6, "Luật này lập ra chế độ 人身安全保护令, lệnh bảo vệ an toàn thân thể: cơ quan tư pháp ra quyết định để bảo vệ nạn nhân, con cái và người thân của họ. Trong bài, tòa án đã ra lệnh này cho cô blogger.")])

# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung nếu khác])
P = [
    ("近年来，一些恶性家暴事件时有发生，牵动着社会公众的心。家庭暴力，挑战道德和文明的底线，让许多家庭因此坠入深渊。",
     "Những năm gần đây, một số vụ bạo lực gia đình nghiêm trọng thỉnh thoảng lại xảy ra, khiến cả xã hội lo lắng. Bạo lực gia đình thách thức giới hạn tối thiểu của đạo đức và văn minh, khiến biết bao gia đình vì thế mà rơi xuống vực thẳm.",
     ["恶性 là ác tính, nghiêm trọng, như 恶性事件, vụ việc nghiêm trọng; 恶性肿瘤, khối u ác tính. 时有发生 là thỉnh thoảng lại xảy ra, một cụm rất hay gặp trên báo.",
      "牵动着社会公众的心 là khiến lòng công chúng xao động lo lắng. 挑战底线 là thách thức giới hạn cuối cùng. 因此 là vì thế. Đoạn mở đầu nêu thẳng vấn đề và mức độ nghiêm trọng của nó."]),
    ("“我被家暴了，过去的半年我仿佛活在噩梦里，关于家暴的这一切，我必须说出来！”在联合国确立的“国际消除家庭暴力日”当天，一名博主发布的一段视频登上了热搜榜。",
     "“Tôi đã bị bạo hành gia đình. Nửa năm qua tôi như sống trong cơn ác mộng, tất cả những gì liên quan đến bạo hành, tôi phải nói ra!” Đúng vào Ngày quốc tế xóa bỏ bạo lực gia đình do Liên Hợp Quốc xác lập, một đoạn video do một blogger đăng tải đã lên bảng tìm kiếm nóng.",
     ["Bài báo mở đầu bằng lời kể trực tiếp của nạn nhân, rất gây ấn tượng. 我被家暴了: ở đây 家暴 được dùng như động từ, bị bạo hành gia đình. 仿佛 là dường như.",
      "确立 là xác lập. 当天 là ngay ngày hôm đó. 一名博主: 名 là lượng từ cho người, trang trọng hơn 个. 登上了热搜榜 là leo lên bảng tìm kiếm nóng."]),
    ("视频中，该博主讲述了自己恋爱一年来五次被家暴的经历，并附上了在电梯间里面遭到殴打的影像记录。",
     "Trong video, blogger này kể lại trải nghiệm bị bạo hành năm lần trong một năm yêu nhau, đồng thời đính kèm đoạn ghi hình cảnh cô bị đánh trong thang máy.",
     ["该博主 là blogger này, đây là cách dùng đại từ 该 trong văn phong tin tức. 恋爱一年来 là trong một năm yêu nhau kể từ khi bắt đầu.",
      "附上 là đính kèm. 遭到殴打 là bị đánh đập: 遭到 nghĩa là gặp phải điều không may, 殴打 là đánh đập. 影像记录 là bản ghi hình."]),
    ("“姐姐告他！不能忍”，网友的声援不少，但也有人问，第一次被打为什么不分手呢？事实上，亲密关系中，很难做到如此理性的决断，毕竟人都有弱点，心软和宽容之间并没有特别明确的界线。",
     "“Chị ơi kiện hắn đi! Không thể nhịn được”, cư dân mạng lên tiếng ủng hộ rất nhiều, nhưng cũng có người hỏi: lần đầu bị đánh sao không chia tay? Thực tế, trong một mối quan hệ thân mật, rất khó đưa ra một quyết định lý trí như vậy, dù sao con người ai cũng có điểm yếu, giữa mềm lòng và bao dung cũng chẳng có ranh giới thật rõ ràng.",
     ["告他 là kiện hắn. 网友的声援不少 là sự ủng hộ của cư dân mạng không ít. Câu hỏi 第一次被打为什么不分手呢 là một câu hỏi người ngoài rất hay đặt ra cho nạn nhân.",
      "Tác giả phản bác: 很难做到如此理性的决断, rất khó quyết định lý trí như thế. 毕竟 là dù sao, rốt cuộc, đưa ra lý do. 心软 là mềm lòng, 宽容 là bao dung: người trong cuộc khó phân biệt mình đang bao dung hay đang nhu nhược."]),
    ("现实中家庭暴力的存在有着复杂的原因，这背后往往是不平等的社会经济关系，比方说老人因为年迈离不开子女的赡养与照顾，一些妻子由于全身心投入家庭使得育娃需要依赖丈夫的收入，",
     "Trong thực tế, bạo lực gia đình tồn tại vì những nguyên nhân phức tạp, đằng sau nó thường là quan hệ kinh tế xã hội bất bình đẳng. Chẳng hạn, người già vì tuổi cao không thể sống thiếu sự phụng dưỡng và chăm sóc của con cái; một số người vợ vì dồn toàn bộ tâm sức cho gia đình, nên việc nuôi con phải dựa vào thu nhập của chồng;",
     ["Đây là đoạn phân tích nguyên nhân. 有着复杂的原因 là có những nguyên nhân phức tạp. 不平等的社会经济关系 là quan hệ kinh tế xã hội bất bình đẳng, tức là nạn nhân phụ thuộc vào kẻ bạo hành.",
      "比方说 là ví dụ như. 年迈 là tuổi già. 离不开 là không thể rời xa, không thể thiếu. 全身心投入家庭 là dồn hết tâm sức cho gia đình. 使得 là khiến cho. 育娃 là nuôi con, 娃 là con nít, khẩu ngữ."]),
    ("孩子们也因为幼小需要父母长辈提供养育资源，在这些情况下，受害者往往难以“直起腰杆”，理直气壮地寻求法律的保护，维护自己的合法权益。",
     "trẻ con cũng vì còn nhỏ nên cần cha mẹ, người lớn cung cấp nguồn lực nuôi dưỡng. Trong những trường hợp đó, nạn nhân thường khó mà “đứng thẳng lưng”, mạnh dạn tìm đến sự bảo vệ của pháp luật, bảo vệ quyền lợi hợp pháp của mình.",
     ["Ba ví dụ: người già, người vợ, trẻ em; đều là những người phải phụ thuộc kinh tế. 幼小 là còn nhỏ dại. 长辈 là bậc trên, người lớn tuổi trong nhà.",
      "直起腰杆 là đứng thẳng lưng, ý nói có chỗ dựa, tự tin. 理直气壮 là lý lẽ đanh thép, khí thế hùng hồn. Hai thành ngữ này sẽ được học kỹ. 维护合法权益 là bảo vệ quyền lợi hợp pháp, từ 维权 chính là viết tắt của cụm này."]),
    ("在舆论的关注下，施暴者已被当地警方行政拘留二十日，并被处以罚款。当地法院也对该博主发出人身安全保护令。",
     "Trước sự quan tâm của dư luận, kẻ bạo hành đã bị cảnh sát địa phương tạm giữ hành chính hai mươi ngày và bị phạt tiền. Tòa án địa phương cũng đã ra lệnh bảo vệ an toàn thân thể cho blogger này.",
     ["在舆论的关注下: mẫu 在……下 là trong điều kiện, dưới tác động của. 被……行政拘留二十日 là bị tạm giữ hành chính hai mươi ngày, 日 là ngày, văn viết.",
      "处以罚款 là xử phạt tiền, chữ 处 ở đây đọc thanh ba, nghĩa là xử lý. 发出人身安全保护令 là ra lệnh bảo vệ an toàn thân thể, như chúng ta đã nói ở phần kiến thức nền."]),
    ("相比之下，对那些没有关注度甚至没有收入的家暴受害者来说，如何摆脱施暴者的毒手，走出家庭暴力的阴影，依然是不得不正视的社会问题。",
     "So ra thì, đối với những nạn nhân bạo lực gia đình không được ai chú ý, thậm chí không có thu nhập, làm thế nào thoát khỏi bàn tay độc ác của kẻ bạo hành, bước ra khỏi bóng tối của bạo lực gia đình, vẫn là một vấn đề xã hội buộc phải nhìn thẳng vào.",
     ["相比之下 là so ra thì, đây là câu mẫu thứ hai. Tác giả so sánh: cô blogger nổi tiếng được dư luận giúp đỡ, còn những nạn nhân bình thường thì sao? 关注度 là mức độ được quan tâm.",
      "摆脱施暴者的毒手 là thoát khỏi bàn tay độc ác của kẻ bạo hành; 摆脱 là một nhóm kết hợp từ của bài. 走出阴影 là bước ra khỏi bóng tối. 不得不正视 là buộc phải nhìn thẳng vào."]),
    ("据统计，我国有24.7%的家庭存在不同形式的家庭暴力，绝大多数受害者为妇女、儿童、老人等，妇联系统每年受理4到5万件家暴投诉。",
     "Theo thống kê, ở nước ta có 24,7% gia đình tồn tại bạo lực gia đình dưới các hình thức khác nhau, tuyệt đại đa số nạn nhân là phụ nữ, trẻ em, người già…; hệ thống Hội Phụ nữ mỗi năm tiếp nhận từ 40 đến 50 nghìn đơn tố cáo bạo lực gia đình.",
     ["据统计 là theo thống kê. 百分之二十四点七 là gần một phần tư số gia đình, một con số đáng giật mình. 受害者为妇女: chữ 为 ở đây đọc thanh hai, nghĩa là là.",
      "妇联系统 là hệ thống Hội Phụ nữ. 受理投诉 là tiếp nhận đơn khiếu nại, tố cáo. Chú ý cách đọc số: 四到五万件 là bốn đến năm vạn vụ, tức bốn mươi đến năm mươi nghìn vụ."],
     "据统计，我国有百分之二十四点七的家庭存在不同形式的家庭暴力，绝大多数受害者为妇女、儿童、老人等，妇联系统每年受理四到五万件家暴投诉。"),
    ("数字背后是一个个生活在暴力阴影下的受害者，和一个个令人唏嘘的家庭悲剧，而如此恶劣的原生家庭对下一代来说更是后患无穷。",
     "Đằng sau những con số là từng nạn nhân đang sống dưới bóng tối của bạo lực, là từng bi kịch gia đình khiến người ta ngậm ngùi; và một gia đình gốc tồi tệ như vậy càng để lại hậu họa khôn lường cho thế hệ sau.",
     ["一个个 là từng người một, lặp lượng từ để nhấn mạnh số lượng nhiều và cụ thể. 令人唏嘘 là khiến người ta thở dài ngậm ngùi.",
      "原生家庭 là gia đình gốc, nơi một người sinh ra và lớn lên, một thuật ngữ tâm lý học rất phổ biến hiện nay. 后患无穷 là hậu họa vô cùng: trẻ lớn lên trong bạo lực sẽ chịu ảnh hưởng suốt đời."]),
    ("对弱者最有力的支持便是法律。2016年3月1日，我国《反家庭暴力法》正式施行，打通了公权力干预家庭暴力的渠道，强调了对家暴“零容忍”的原则，",
     "Sự ủng hộ mạnh mẽ nhất đối với kẻ yếu chính là pháp luật. Ngày 1 tháng 3 năm 2016, Luật Chống bạo lực gia đình của nước ta chính thức có hiệu lực, khai thông con đường để quyền lực nhà nước can thiệp vào bạo lực gia đình, nhấn mạnh nguyên tắc “không khoan nhượng” với bạo lực gia đình,",
     ["便是 là chính là, văn viết của 就是. 最有力的支持 là sự ủng hộ mạnh mẽ nhất. Đoạn này chuyển sang vai trò của pháp luật.",
      "打通渠道 là khai thông con đường. 干预 là can thiệp, chữ đầu đọc thanh một. 强调原则 là nhấn mạnh nguyên tắc. Tên bài 零容忍 xuất hiện ở đây; 零 là một nhóm kết hợp từ, như 零排放, 零误差."],
     "对弱者最有力的支持便是法律。二零一六年三月一日，我国反家庭暴力法正式施行，打通了公权力干预家庭暴力的渠道，强调了对家暴零容忍的原则，"),
    ("进而向社会阐明：家庭暴力不是个人私事而是社会公害；不是一般的家庭纠纷，而是违法犯罪，是对家庭成员权利极为严重的侵犯。",
     "rồi từ đó nói rõ với xã hội rằng: bạo lực gia đình không phải chuyện riêng của cá nhân mà là mối hại của xã hội; không phải mâu thuẫn gia đình thông thường, mà là hành vi vi phạm pháp luật, phạm tội, là sự xâm phạm cực kỳ nghiêm trọng đến quyền của các thành viên trong gia đình.",
     ["进而 là rồi tiến thêm một bước: luật đã có hiệu lực, từ đó còn khẳng định với xã hội một quan điểm. 阐明 là nói rõ. Đây là ví dụ đầu tiên của câu mẫu 进而.",
      "Hai cặp 不是……而是…… đứng song song: 不是个人私事而是社会公害; 不是一般的家庭纠纷，而是违法犯罪. 纠纷 là tranh chấp, mâu thuẫn. 侵犯 là xâm phạm. Đây là luận điểm trung tâm của cả bài."]),
    ("调查显示，女性被家暴35次之后，才会选择报警，报警率不到10%，这是因为在很多人的意识中“家丑不可外扬”，她们宁愿忍气吞声，也不会公之于众。",
     "Điều tra cho thấy, phụ nữ bị bạo hành gia đình 35 lần rồi mới chọn báo cảnh sát, tỷ lệ báo cảnh sát chưa tới 10%. Đó là vì trong ý thức của rất nhiều người, “xấu chàng hổ ai”, chuyện xấu trong nhà không được đưa ra ngoài; họ thà nuốt giận làm thinh, chứ không công khai cho mọi người biết.",
     ["调查显示 là điều tra cho thấy. 被家暴三十五次之后，才会选择报警: chữ 才 nhấn mạnh muộn, phải ba mươi lăm lần mới báo. 报警率不到百分之十 là tỷ lệ báo cảnh sát chưa đến mười phần trăm.",
      "家丑不可外扬 là chuyện xấu trong nhà không được truyền ra ngoài. Câu 她们宁愿忍气吞声，也不会公之于众 chính là ví dụ của câu mẫu 宁愿……也……. 忍气吞声 là nuốt giận làm thinh; 公之于众 là công khai cho mọi người biết."],
     "调查显示，女性被家暴三十五次之后，才会选择报警，报警率不到百分之十，这是因为在很多人的意识中家丑不可外扬，她们宁愿忍气吞声，也不会公之于众。"),
    ("当然，不少地方“清官难断家务事”的传统观念根深蒂固，此外，救济渠道不通畅，对家暴受害者的求助不能给予及时有效的反馈与干预，这些都是造成“沉默的大多数”的原因。",
     "Tất nhiên, ở không ít nơi, quan niệm truyền thống “quan thanh liêm cũng khó xử chuyện nhà” đã ăn sâu bén rễ; ngoài ra, các kênh trợ giúp không thông suốt, những lời kêu cứu của nạn nhân không được phản hồi và can thiệp kịp thời, hiệu quả. Tất cả đều là nguyên nhân tạo nên “số đông im lặng”.",
     ["清官难断家务事 là quan thanh liêm cũng khó phân xử chuyện nhà, ý nói chuyện trong nhà người ngoài khó can thiệp. 根深蒂固 là rễ sâu gốc chắc, ăn sâu bén rễ.",
      "此外 là ngoài ra. 给予 là dành cho, trao cho, chữ đầu đọc là jǐ. 沉默的大多数 là số đông im lặng. Đoạn này tổng kết ba nguyên nhân khiến nạn nhân im lặng: tâm lý giữ thể diện, quan niệm truyền thống, và kênh trợ giúp chưa thông suốt."]),
    ("对家暴沉默的旁观者看似无辜，实则纵容犯罪，不再沉默是必须迈出的第一步。在这起事件中令人感动的是，施暴者的两位前妻、两位朋友和一位学生也为受害者发了声。",
     "Người ngoài cuộc im lặng trước bạo lực gia đình tưởng như vô tội, nhưng thực ra là dung túng tội ác; không im lặng nữa là bước đầu tiên nhất định phải bước. Điều cảm động trong vụ việc này là hai người vợ cũ, hai người bạn và một học trò của kẻ bạo hành cũng đã lên tiếng vì nạn nhân.",
     ["看似……实则…… là trông thì có vẻ…, thực ra là…, một cấu trúc rất hay của văn nghị luận. 旁观者 là người đứng ngoài quan sát. 纵容犯罪 là dung túng tội ác.",
      "这起事件: 起 là lượng từ cho sự việc. 前妻 là vợ cũ. 为受害者发了声: 发声 là lên tiếng, chữ 为 đọc thanh bốn, nghĩa là vì, thay cho. Ngay cả vợ cũ của kẻ bạo hành cũng đứng ra làm chứng."]),
    ("这位勇敢的女学生在镜头中说：“我不能再装聋作哑……受害者保持沉默，周围的人熟视无睹，就是助长了这种人的暴行，受害者及时报警才是正确的应对。”",
     "Cô học trò dũng cảm ấy nói trước ống kính: “Tôi không thể giả câm giả điếc nữa… Nạn nhân giữ im lặng, những người xung quanh nhìn mãi thành quen mà làm ngơ, chính là tiếp tay cho hành vi bạo lực của loại người này. Nạn nhân kịp thời báo cảnh sát mới là cách ứng phó đúng đắn.”",
     ["镜头 là ống kính máy quay. 装聋作哑 là giả câm giả điếc. 熟视无睹 là nhìn quen rồi coi như không thấy. Hai thành ngữ này đều chỉ thái độ làm ngơ.",
      "助长 là tiếp tay, làm cho cái xấu phát triển thêm, chữ thứ hai đọc là zhǎng. 暴行 là hành vi tàn bạo. 才是正确的应对 là mới là cách ứng phó đúng: chữ 才 nhấn mạnh, chỉ có cách này mới đúng."]),
    ("不过，面对施暴者的威胁，谁来保护站出来的人？如何让施暴者得到应有的惩罚？首先家暴目击者进行力所能及的劝阻或者及时报案，帮助受害者打破沉默，形成对家暴“零容忍”的社会氛围；",
     "Tuy nhiên, trước sự đe dọa của kẻ bạo hành, ai sẽ bảo vệ những người đã đứng ra? Làm thế nào để kẻ bạo hành nhận hình phạt thích đáng? Trước hết, người chứng kiến bạo lực gia đình nên khuyên ngăn trong khả năng của mình hoặc kịp thời báo án, giúp nạn nhân phá vỡ sự im lặng, tạo nên bầu không khí xã hội “không khoan nhượng” với bạo lực gia đình;",
     ["Hai câu hỏi tu từ mở ra phần giải pháp. 站出来的人 là người dám đứng ra. 应有的惩罚 là hình phạt đáng phải chịu, chữ 应 đọc thanh một.",
      "目击者 là người chứng kiến tận mắt. 力所能及 là trong khả năng của mình. 劝阻 là khuyên ngăn, 报案 là báo án. 打破沉默 là phá vỡ sự im lặng. 社会氛围 là bầu không khí xã hội."]),
    ("同时，加大对于受害者的舆论支持、提供法律帮助以及开展及时的心理疏导等也是非常必要的。只有进一步加大法律制度的保障，降低受害者的维权成本，凝聚更广泛的社会共识，在机制上形成合力，才能筑起反对家庭暴力的坚固防线。",
     "Đồng thời, tăng cường sự ủng hộ của dư luận đối với nạn nhân, cung cấp trợ giúp pháp lý và kịp thời hỗ trợ tâm lý… cũng là điều rất cần thiết. Chỉ có tăng cường hơn nữa sự bảo đảm của chế độ pháp luật, giảm chi phí đòi quyền lợi của nạn nhân, tập hợp sự đồng thuận xã hội rộng rãi hơn, tạo thành sức mạnh tổng hợp về cơ chế, mới có thể dựng nên một phòng tuyến vững chắc chống bạo lực gia đình.",
     ["加大 là tăng cường, đẩy mạnh. 以及 là cùng với, văn viết của 和. 心理疏导 là hỗ trợ, gỡ rối tâm lý.",
      "Câu kết dùng mẫu 只有……才…… với bốn vế song song: 加大保障，降低成本，凝聚共识，形成合力. 维权成本 là chi phí, công sức để đòi quyền lợi. 筑起防线 là dựng nên phòng tuyến. Một kết bài rất tiêu biểu cho văn xã luận Trung Quốc."]),
]

add("bullets", section="Bài khóa 课文", title="Phần 2: Bài khóa 对家暴必须“零容忍”", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Bài khóa được cải biên từ bài 反家暴尤需打破沉默, Chống bạo lực gia đình càng cần phá vỡ sự im lặng, đăng trên 人民日报 ngày mùng hai tháng mười hai năm hai nghìn không trăm mười chín, tác giả là 程晨.",
         F(0, "Bài khá dài, thầy chia thành mười tám đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 70 else 50 if len(zh) <= 90 else 46
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Ý chính bài khóa", section="Bài khóa 课文", title="Mạch lập luận của bài", size=34,
    items=["## 1. Nêu vấn đề: một vụ bạo hành lên hot search ngày 25/11",
           "Blogger kể 5 lần bị bạo hành · dư luận: 为什么不分手？",
           "## 2. Phân tích nguyên nhân",
           "Quan hệ kinh tế bất bình đẳng → nạn nhân khó 直起腰杆 · 家丑不可外扬 · 清官难断家务事 · kênh trợ giúp không thông",
           "## 3. Số liệu & pháp luật",
           "24.7% gia đình · báo cảnh sát sau 35 lần, tỷ lệ < 10% · 《反家庭暴力法》 2016: 家暴是违法犯罪",
           "## 4. Giải pháp: phá vỡ im lặng",
           "Người chứng kiến lên tiếng · dư luận, pháp lý, tâm lý · 只有……才能筑起坚固防线"],
    say=["Đọc xong bài khóa, chúng ta cùng tóm tắt mạch lập luận. Đây là kết cấu rất điển hình của văn bình luận trên báo Trung Quốc: nêu vấn đề, phân tích, đưa số liệu, rồi đề xuất giải pháp.",
         F(0, "Phần một: nêu vấn đề. Đúng ngày hai mươi lăm tháng mười một, video của một blogger bị bạo hành lên hot search."),
         F(1, "Cô kể đã bị đánh năm lần trong một năm. Dư luận ủng hộ, nhưng cũng có người hỏi: 第一次被打为什么不分手？"),
         F(2, "Phần hai: phân tích nguyên nhân vì sao nạn nhân không dễ dứt ra và không dám lên tiếng."),
         F(3, "Thứ nhất là quan hệ kinh tế bất bình đẳng, nạn nhân phụ thuộc nên khó 直起腰杆. Thứ hai là tâm lý 家丑不可外扬. Thứ ba là quan niệm 清官难断家务事. Thứ tư là các kênh trợ giúp chưa thông suốt."),
         F(4, "Phần ba: số liệu và pháp luật."),
         F(5, "Hai mươi bốn phẩy bảy phần trăm gia đình có bạo lực; phụ nữ bị đánh ba mươi lăm lần mới báo cảnh sát, tỷ lệ báo chưa tới mười phần trăm. Luật Chống bạo lực gia đình năm hai nghìn không trăm mười sáu khẳng định: 家暴不是家务事，而是违法犯罪."),
         F(6, "Phần bốn: giải pháp, mà từ khóa là 打破沉默, phá vỡ sự im lặng."),
         F(7, "Người chứng kiến phải lên tiếng hoặc báo án; xã hội hỗ trợ nạn nhân về dư luận, pháp lý, tâm lý; và chỉ khi pháp luật, xã hội cùng chung tay, mới dựng được phòng tuyến vững chắc chống bạo lực gia đình.")])

# ======================= CÂU MẪU =======================
add("bullets", chapter="Câu mẫu: 该 · 相比之下", section="Câu mẫu 重点句型", title="1. 该 gāi – (người, vật) này, nói trên", size=34,
    items=["Đại từ chỉ thị: chỉ người hoặc sự vật đã nói ở trên, tương đương “这个”; dùng nhiều trong công văn, tin tức",
           "Cấu trúc: 该 + danh từ (该博主 · 该地 · 该同学 · 该公司 · 该法律)",
           "……一名博主发布的一段视频登上了热搜榜。视频中，该博主讲述了自己恋爱一年来五次被家暴的经历。",
           "南京是一座美丽的城市，该地风景优美、交通便利。",
           "老师给她写的评语是“该同学学习成绩优异，为人诚恳谦虚，乐观向上，乐于助人，是一位品学兼优的学生。”"],
    say=["Bây giờ chúng ta sang phần câu mẫu và từ ngữ trọng điểm. Điểm thứ nhất là đại từ 该.",
         F(0, "Các bạn đã quen với 该 nghĩa là nên, như 你该走了. Nhưng ở đây, 该 là đại từ chỉ thị, chỉ người hay sự vật vừa được nhắc đến ở trên, tương đương 这个. Cách dùng này mang màu sắc trang trọng, gặp nhiều trong công văn, tin tức, văn bản pháp luật."),
         F(1, "Cấu trúc là 该 cộng thẳng danh từ, không cần lượng từ: 该博主，该地，该同学，该公司. Tiếng Việt thường dịch là này, nói trên, hoặc đó."),
         F(2, "Ví dụ một, từ bài khóa: 一名博主发布的一段视频登上了热搜榜。视频中，该博主讲述了自己恋爱一年来五次被家暴的经历。 Câu trước nhắc đến 一名博主, câu sau dùng 该博主 để chỉ lại chính blogger đó."),
         F(3, "Ví dụ hai: 南京是一座美丽的城市，该地风景优美、交通便利。 Nam Kinh là một thành phố đẹp, nơi đây phong cảnh đẹp đẽ, giao thông thuận tiện. 该地 là nơi này, chính là Nam Kinh."),
         F(4, "Ví dụ ba: 老师给她写的评语是：该同学学习成绩优异，为人诚恳谦虚，乐观向上，乐于助人，是一位品学兼优的学生。 Lời nhận xét thầy cô viết cho cô ấy là: em học sinh này thành tích học tập xuất sắc, sống chân thành khiêm tốn, lạc quan cầu tiến, thích giúp đỡ người khác, là một học sinh giỏi cả học lẫn hạnh. Đây đúng là giọng văn của học bạ, rất trang trọng.")])

add("bullets", section="Câu mẫu 重点句型", title="2. ……，相比之下，…… – so ra thì, so với điều đó", size=34,
    items=["Đứng đầu vế sau, nêu sự so sánh với điều vừa nói ở trước; nhấn mạnh sự khác biệt",
           "相比之下，对那些没有关注度甚至没有收入的家暴受害者来说，如何摆脱施暴者的毒手，走出家庭暴力的阴影，依然是不得不正视的社会问题。",
           "相比之下，硕士学历比本科学历在找工作的时候更有优势，基础工资水平也会更高。",
           "韩国女队平均年龄只有18.6岁，相比之下，中国女队则年长三岁。",
           "Mẹo: vế sau thường có 则、更、反而 để làm rõ sự đối lập"],
    say=["Điểm thứ hai là cấu trúc 相比之下.",
         F(0, "相比之下 nghĩa là khi so sánh với điều vừa nói thì. Nó thường đứng đầu một câu hay một vế câu, nối với nội dung phía trước, để làm nổi bật sự khác biệt. Tiếng Việt dịch là so ra thì, so với điều đó, ngược lại."),
         F(1, "Ví dụ một, từ bài khóa: 相比之下，对那些没有关注度甚至没有收入的家暴受害者来说，如何摆脱施暴者的毒手，走出家庭暴力的阴影，依然是不得不正视的社会问题。 Phía trước là cô blogger được dư luận chú ý, được cảnh sát và tòa án bảo vệ; so ra thì những nạn nhân vô danh vẫn khó thoát khỏi bạo lực."),
         F(2, "Ví dụ hai: 相比之下，硕士学历比本科学历在找工作的时候更有优势，基础工资水平也会更高。 So ra thì, bằng thạc sĩ có ưu thế hơn bằng cử nhân khi tìm việc, mức lương cơ bản cũng cao hơn."),
         F(3, "Ví dụ ba: 韩国女队平均年龄只有十八点六岁，相比之下，中国女队则年长三岁。 Đội tuyển nữ Hàn Quốc tuổi trung bình chỉ có mười tám phẩy sáu, so ra thì đội nữ Trung Quốc lớn hơn ba tuổi. 年长 là lớn tuổi hơn, chữ 长 đọc là zhǎng."),
         F(4, "Mẹo nhỏ: vế sau 相比之下 thường có các từ như 则，更，反而, để làm rõ sự đối lập. Như ví dụ ba có chữ 则.")])

add("bullets", chapter="Câu mẫu: 进而 · 宁愿", section="Câu mẫu 重点句型", title="3. 进而 jìn'ér – rồi tiến thêm một bước, từ đó", size=34,
    items=["Liên từ: trên cơ sở điều đã có (vế trước), tiến thêm một bước (vế sau)",
           "Vế trước thường có 首先、先; vế sau thường có 再、又",
           "强调了对家暴“零容忍”的原则，进而向社会阐明：家庭暴力不是个人私事而是社会公害。",
           "先调查研究，进而提出改革方案。",
           "这就是为什么我说首先要在自己身上下功夫，然后推向你的家庭，进而再达到之外的世界。"],
    say=["Điểm thứ ba là liên từ 进而. Chúng ta đã gặp từ này ở phần từ mới.",
         F(0, "进而 biểu thị: trên cơ sở điều đã làm được ở vế trước, tiến thêm một bước ở vế sau. Hai vế có quan hệ tăng tiến, vế sau cao hơn, sâu hơn vế trước. Tiếng Việt dịch là rồi tiến thêm, từ đó, tiến tới."),
         F(1, "Vế trước thường có 首先 hoặc 先, vế sau có thể có thêm 再, 又."),
         F(2, "Ví dụ một, từ bài khóa: 强调了对家暴零容忍的原则，进而向社会阐明：家庭暴力不是个人私事而是社会公害。 Luật nhấn mạnh nguyên tắc không khoan nhượng, rồi từ đó còn khẳng định với xã hội rằng bạo lực gia đình là mối hại chung."),
         F(3, "Ví dụ hai: 先调查研究，进而提出改革方案。 Trước tiên điều tra nghiên cứu, rồi tiến tới đề xuất phương án cải cách."),
         F(4, "Ví dụ ba: 这就是为什么我说首先要在自己身上下功夫，然后推向你的家庭，进而再达到之外的世界。 Đó là lý do tôi nói trước hết phải bỏ công sức rèn luyện chính mình, sau đó mở rộng ra gia đình, rồi tiến tới thế giới bên ngoài. Câu này gợi nhớ tư tưởng tu thân, tề gia của Nho giáo.")])

add("bullets", section="Câu mẫu 重点句型", title="4. 宁愿……，也…… – thà… chứ (không)…", size=34,
    items=["Câu phức lựa chọn: trong hoàn cảnh không mấy vừa ý, cân nhắc lợi hại rồi chọn một bên",
           "宁愿 + điều chọn (thường là thiệt thòi) + 也不 + điều bỏ  /  宁愿 + cái giá + 也要 + mục đích",
           "她们宁愿忍气吞声，也不会公之于众。",
           "我宁愿待在家里，也不要雨天出门逛街。",
           "我宁愿今晚不看电视，也要把这道题攻下来。"],
    say=["Điểm thứ tư là câu lựa chọn 宁愿……也……. Chữ 宁 ở đây đọc thanh bốn.",
         F(0, "Đây là câu phức lựa chọn: trong hoàn cảnh không mấy vừa ý, người nói cân nhắc lợi hại, rồi chọn một phương án, bỏ phương án kia. Tiếng Việt là thà… chứ không…."),
         F(1, "Có hai dạng. Dạng một: 宁愿 cộng điều mình chọn, thường là chịu thiệt, rồi 也不 cộng điều mình nhất quyết không làm. Dạng hai: 宁愿 cộng cái giá phải trả, rồi 也要 cộng mục đích nhất định phải đạt."),
         F(2, "Ví dụ một, từ bài khóa: 她们宁愿忍气吞声，也不会公之于众。 Họ thà nuốt giận làm thinh, chứ không công khai cho mọi người biết. Đây là dạng một: nhịn nhục là điều chọn, công khai là điều bỏ."),
         F(3, "Ví dụ hai: 我宁愿待在家里，也不要雨天出门逛街。 Tôi thà ở nhà, chứ không muốn ra ngoài dạo phố ngày mưa."),
         F(4, "Ví dụ ba: 我宁愿今晚不看电视，也要把这道题攻下来。 Tôi thà tối nay không xem tivi, cũng phải giải cho xong bài toán này. Đây là dạng hai: 也要 nêu mục đích. 攻下来 là chinh phục được, giải được.")])

add("bullets", section="Câu mẫu 重点句型", title="Luyện tập: chọn 该 · 相比之下 · 进而 · 宁愿 điền vào chỗ trống", reveal=True, size=34,
    items=["(1) 警方抓到了一名小偷，___男子已经多次在地铁上偷钱包。",
           "Đáp án: 该 – 该男子 chỉ lại 一名小偷 ở vế trước.",
           "(2) 他___每天多走半个小时，也不愿意开车上班。",
           "Đáp án: 宁愿 – 宁愿……也不……",
           "(3) 我们先要发现问题，___找到解决问题的办法。",
           "Đáp án: 进而 – từ phát hiện vấn đề tiến thêm một bước đến giải quyết vấn đề.",
           "(4) 大城市机会多，但压力也大；___，小城市的生活节奏慢得多。",
           "Đáp án: 相比之下 – so sánh hai thành phố, nhấn mạnh khác biệt."],
    say=["Chúng ta luyện tập một chút: chọn một trong bốn từ 该，相比之下，进而，宁愿 điền vào chỗ trống.",
         F(0, "Câu một: 警方抓到了一名小偷，什么男子已经多次在地铁上偷钱包。 Cảnh sát đã bắt được một tên trộm, người đàn ông này đã nhiều lần trộm ví trên tàu điện ngầm. Các bạn tạm dừng và chọn nhé."),
         F(1, "Đáp án: 该. 该男子 chỉ lại tên trộm vừa nhắc ở vế trước, đúng giọng văn tin tức."),
         F(2, "Câu hai: 他什么每天多走半个小时，也不愿意开车上班。 Anh ấy thà mỗi ngày đi bộ thêm nửa tiếng, chứ không muốn lái xe đi làm."),
         F(3, "Đáp án: 宁愿. Mẫu 宁愿……也不……."),
         F(4, "Câu ba: 我们先要发现问题，什么找到解决问题的办法。 Trước tiên chúng ta phải phát hiện vấn đề, rồi từ đó tìm ra cách giải quyết."),
         F(5, "Đáp án: 进而. Vế trước có 先, vế sau tiến thêm một bước."),
         F(6, "Câu bốn: 大城市机会多，但压力也大；什么，小城市的生活节奏慢得多。 Thành phố lớn nhiều cơ hội, nhưng áp lực cũng lớn; so ra thì nhịp sống ở thành phố nhỏ chậm hơn nhiều."),
         F(7, "Đáp án: 相比之下. Đây là phép so sánh giữa hai đối tượng, và vế sau có 得多 nhấn mạnh sự khác biệt.")])

# ======================= KẾT HỢP TỪ =======================
add("bullets", chapter="Kết hợp từ", section="Kết hợp từ 词语搭配", title="Kết hợp từ (1): 附（上）+ danh từ · 摆脱", size=33,
    items=["## 附（上）: 附上……的明细 · 附上资料 · 附上祝福",
           "视频中，该博主……并附上了在电梯间里面遭到殴打的影像记录。",
           "请你在给我发邮件的时候附上本次消费的明细，谢谢！",
           "他在给女方的信中介绍了自己的家庭和工作情况，并附上近照一张。",
           "## 摆脱: 摆脱毒手 · 摆脱困境 · 摆脱束缚 · 摆脱阴影 · 摆脱危险",
           "与其这样坐以待毙，还不如积极行动摆脱困境。",
           "叛逆伴随人的一生，人的成长过程就是摆脱束缚的叛逆过程。"],
    say=["Tiếp theo là phần kết hợp từ, tức là những từ thường đi với nhau. Học theo cụm sẽ giúp các bạn dùng từ tự nhiên như người bản ngữ.",
         F(0, "Nhóm một: 附上 cộng danh từ, nghĩa là đính kèm thứ gì. 附上明细, kèm theo bảng kê chi tiết; 附上资料, kèm tài liệu; 附上祝福, gửi kèm lời chúc."),
         F(1, "Ví dụ từ bài khóa: 视频中，该博主讲述了自己恋爱一年来五次被家暴的经历，并附上了在电梯间里面遭到殴打的影像记录。"),
         F(2, "Ví dụ hai: 请你在给我发邮件的时候附上本次消费的明细，谢谢！ Khi gửi email cho tôi, xin đính kèm bảng kê chi tiết lần tiêu dùng này, cảm ơn!"),
         F(3, "Ví dụ ba: 他在给女方的信中介绍了自己的家庭和工作情况，并附上近照一张。 Trong thư gửi nhà gái, anh ấy giới thiệu gia cảnh và công việc của mình, kèm theo một tấm ảnh gần đây. 近照 là ảnh chụp gần đây."),
         F(4, "Nhóm hai: 摆脱, nghĩa là thoát khỏi điều bất lợi. 摆脱毒手, thoát khỏi bàn tay độc ác; 摆脱困境, thoát khỏi cảnh khốn khó; 摆脱束缚, thoát khỏi sự trói buộc; 摆脱阴影, thoát khỏi bóng tối; 摆脱危险, thoát khỏi nguy hiểm."),
         F(5, "Ví dụ: 与其这样坐以待毙，还不如积极行动摆脱困境。 Thay vì ngồi chờ chết như thế này, chẳng thà tích cực hành động để thoát khỏi khốn cảnh. 坐以待毙 là ngồi chờ chết."),
         F(6, "Ví dụ: 叛逆伴随人的一生，人的成长过程就是摆脱束缚的叛逆过程。 Sự nổi loạn đi theo con người suốt đời, quá trình trưởng thành chính là quá trình nổi loạn để thoát khỏi trói buộc.")])

add("bullets", section="Kết hợp từ 词语搭配", title="Kết hợp từ (2): 零 · 起", size=33,
    items=["## 零 + danh từ/động từ: 零容忍 · 零排放 · 零误差",
           "2016年3月1日，我国《反家庭暴力法》正式施行，……强调了对家暴“零容忍”的原则。",
           "该公司的工业废水零排放技术先进，处于国内领先位置，在全国同行业具有推广价值。",
           "航空航天领域的火箭轨道运行运算应力求做到零误差。",
           "## 起 (lượng từ): 一起事故 · 一起案件 · 一起事件",
           "这是一起蓄谋已久的诈骗案件，经过数月追查，终于成功破案。",
           "今天中午发生了一起严重交通事故，至少造成交通拥堵三个小时。"],
    say=[F(0, "Nhóm ba: 零, số không, đứng trước danh từ hay động từ, nghĩa là hoàn toàn không có. 零容忍, không dung thứ; 零排放, không phát thải; 零误差, không sai số. Tiếng Việt cũng nói tương tự: không khoan nhượng, phát thải bằng không."),
         F(1, "Ví dụ từ bài khóa: 二零一六年三月一日，我国反家庭暴力法正式施行，强调了对家暴零容忍的原则。"),
         F(2, "Ví dụ hai: 该公司的工业废水零排放技术先进，处于国内领先位置，在全国同行业具有推广价值。 Công nghệ không xả thải nước thải công nghiệp của công ty này rất tiên tiến, dẫn đầu trong nước, có giá trị nhân rộng trong toàn ngành. Lại gặp đại từ 该 ở đây."),
         F(3, "Ví dụ ba: 航空航天领域的火箭轨道运行运算应力求做到零误差。 Trong lĩnh vực hàng không vũ trụ, việc tính toán quỹ đạo tên lửa phải cố gắng đạt sai số bằng không."),
         F(4, "Nhóm bốn: lượng từ 起, dùng cho sự việc, vụ việc: 一起事故, một vụ tai nạn; 一起案件, một vụ án; 一起事件, một sự kiện. Trong bài: 在这起事件中."),
         F(5, "Ví dụ: 这是一起蓄谋已久的诈骗案件，经过数月追查，终于成功破案。 Đây là một vụ lừa đảo đã được mưu tính từ lâu, sau mấy tháng truy tìm, cuối cùng đã phá án thành công."),
         F(6, "Ví dụ: 今天中午发生了一起严重交通事故，至少造成交通拥堵三个小时。 Trưa nay xảy ra một vụ tai nạn giao thông nghiêm trọng, gây ùn tắc ít nhất ba tiếng đồng hồ.")])

# ======================= THÀNH NGỮ =======================
add("bullets", chapter="Thành ngữ & quán ngữ", section="Thành ngữ 成语和惯用语", title="Thành ngữ (1): 直起腰杆 · 理直气壮 · 后患无穷", size=33,
    items=["## 直起腰杆 zhíqǐ yāogǎn – đứng thẳng lưng: có chỗ dựa, tự tin, cứng cỏi",
           "清贫与富有本身都不值得赞美，值得赞美的是在清贫和富有面前都能直起腰杆、保持尊严。",
           "## 理直气壮 lǐzhí-qìzhuàng – lý lẽ đanh thép, hùng hồn, không chút sợ hãi",
           "当我们的权益受到侵害，我们有权理直气壮地讨回公道。",
           "## 后患无穷 hòuhuàn-wúqióng – hậu họa khôn lường",
           "如果继续纵容破坏生态的行为，将后患无穷。"],
    say=["Bây giờ chúng ta học mười một thành ngữ và quán ngữ của bài. Thầy sẽ giải thích nghĩa từng chữ, rồi đọc ví dụ trong sách.",
         F(0, "Thứ nhất: 直起腰杆. 腰杆 là cái lưng, 直起 là dựng thẳng lên. Nghĩa bóng là có chỗ dựa, có khí phách, tự tin mà đối mặt. Trong bài: 受害者往往难以直起腰杆, nạn nhân thường khó đứng thẳng lưng."),
         F(1, "Ví dụ: 清贫与富有本身都不值得赞美，值得赞美的是在清贫和富有面前都能直起腰杆、保持尊严。 Nghèo hay giàu tự nó đều không đáng khen, điều đáng khen là dù nghèo hay giàu đều có thể đứng thẳng lưng, giữ được phẩm giá."),
         F(2, "Thứ hai: 理直气壮. 理直 là lý lẽ ngay thẳng, 气壮 là khí thế mạnh mẽ. Lý lẽ đầy đủ nên nói năng, hành động hùng hồn, trong lòng không hổ thẹn. Tiếng Việt có câu: cây ngay không sợ chết đứng."),
         F(3, "Ví dụ: 当我们的权益受到侵害，我们有权理直气壮地讨回公道。 Khi quyền lợi bị xâm hại, chúng ta có quyền đường hoàng đòi lại công bằng. 讨回公道 là đòi lại công lý."),
         F(4, "Thứ ba: 后患无穷. 后患 là tai họa về sau, 无穷 là không cùng. Tức là để lại hậu họa khôn lường. Trong bài: 如此恶劣的原生家庭对下一代来说更是后患无穷."),
         F(5, "Ví dụ: 如果继续纵容破坏生态的行为，将后患无穷。 Nếu tiếp tục dung túng hành vi phá hoại sinh thái, sẽ để lại hậu họa khôn lường. Lại gặp từ mới 纵容 ở đây.")])

add("bullets", section="Thành ngữ 成语和惯用语", title="Thành ngữ (2): 家丑不可外扬 · 忍气吞声 · 公之于众", size=33,
    items=["## 家丑不可外扬 – chuyện xấu trong nhà không được đưa ra ngoài (丑: điều xấu hổ; 扬: truyền đi)",
           "你为什么要把那些家里的事情告诉外人，你要知道，家丑不可外扬。",
           "## 忍气吞声 rěnqì-tūnshēng – nuốt giận làm thinh, nhẫn nhục chịu đựng",
           "面对继父的打骂，他只有忍气吞声，委曲求全。",
           "## 公之于众 gōngzhī-yúzhòng – công bố cho mọi người biết (之: việc đó; 于: với)",
           "建议政府部门将减税方案公之于众，广泛听取人民的意见，进一步完善该方案。"],
    say=[F(0, "Thứ tư: quán ngữ 家丑不可外扬. 丑 là điều xấu hổ, 扬 là truyền ra, rêu rao. Chuyện xấu trong nhà không được truyền ra ngoài, vì nói với người ngoài sẽ bị tính toán hay chê cười. Tiếng Việt có những câu tương tự: tốt đẹp phô ra, xấu xa đậy lại; hay đóng cửa bảo nhau."),
         F(1, "Ví dụ: 你为什么要把那些家里的事情告诉外人，你要知道，家丑不可外扬。 Sao cậu lại đem chuyện trong nhà kể với người ngoài, cậu phải biết, chuyện xấu trong nhà không được đưa ra ngoài."),
         F(2, "Thứ năm: 忍气吞声. 忍气 là nén giận, 吞声 là nuốt tiếng, có lời mà không dám nói. Tức là bị ức hiếp mà chỉ đành nén chịu, không dám lên tiếng. Tiếng Việt: nuốt giận làm thinh, ngậm bồ hòn làm ngọt."),
         F(3, "Ví dụ: 面对继父的打骂，他只有忍气吞声，委曲求全。 Trước những trận đòn roi, chửi mắng của bố dượng, cậu chỉ biết nuốt giận làm thinh, nhẫn nhịn cho yên chuyện. 继父 là bố dượng, 委曲求全 là chịu thiệt để vẹn toàn."),
         F(4, "Thứ sáu: 公之于众. 公 là công khai, 之 chỉ sự việc, 于 là với, 众 là mọi người. Tức là công bố sự thật cho mọi người biết. Ba thành ngữ này đi cùng nhau trong bài khóa: vì 家丑不可外扬, nên 她们宁愿忍气吞声，也不会公之于众."),
         F(5, "Ví dụ: 建议政府部门将减税方案公之于众，广泛听取人民的意见，进一步完善该方案。 Đề nghị cơ quan chính phủ công bố phương án giảm thuế, lắng nghe rộng rãi ý kiến nhân dân, hoàn thiện thêm phương án đó.")])

add("bullets", section="Thành ngữ 成语和惯用语", title="Thành ngữ (3): 清官难断家务事 · 根深蒂固 · 装聋作哑", size=33,
    items=["## 清官难断家务事 – quan thanh liêm cũng khó phân xử chuyện nhà",
           "其他人见状便都散去了，清官难断家务事，这其中的是非曲直，外人能说什么？",
           "## 根深蒂固 gēnshēn-dìgù – rễ sâu gốc chắc, ăn sâu bén rễ, khó lay chuyển",
           "几千年来，迷信思想流传，尤其在这文化不发达的山区，更是根深蒂固。",
           "## 装聋作哑 zhuānglóng-zuòyǎ – giả câm giả điếc, cố tình làm ngơ",
           "对于社会的不良风气，不能装聋作哑，不闻不问。"],
    say=[F(0, "Thứ bảy: quán ngữ 清官难断家务事. 清官 là vị quan thanh liêm, 断 là phân xử, 家务事 là chuyện trong nhà. Dù là vị quan công minh nhất cũng khó phân xử đúng sai trong tranh chấp gia đình; ý nói chuyện nhà người ta, người ngoài khó mà hiểu rõ."),
         F(1, "Ví dụ: 其他人见状便都散去了，清官难断家务事，这其中的是非曲直，外人能说什么？ Những người khác thấy vậy đều tản đi, quan thanh liêm cũng khó xử chuyện nhà, phải trái đúng sai trong đó, người ngoài nói được gì? 是非曲直 là phải trái đúng sai."),
         F(2, "Thứ tám: 根深蒂固. 根 là rễ, 蒂 là cuống. Rễ sâu cuống chắc, ví với nền tảng vững chắc, khó lay chuyển. Thường dùng cho quan niệm, thói quen, thế lực. Trong bài: 清官难断家务事的传统观念根深蒂固."),
         F(3, "Ví dụ: 几千年来，迷信思想流传，尤其在这文化不发达的山区，更是根深蒂固。 Mấy nghìn năm nay, tư tưởng mê tín lưu truyền, nhất là ở vùng núi văn hóa kém phát triển này, lại càng ăn sâu bén rễ."),
         F(4, "Thứ chín: 装聋作哑. 装 là giả vờ, 聋 là điếc, 哑 là câm. Giả câm giả điếc, cố tình làm như không biết gì. Trong bài, cô học trò nói: 我不能再装聋作哑."),
         F(5, "Ví dụ: 对于社会的不良风气，不能装聋作哑，不闻不问。 Đối với những thói xấu trong xã hội, không thể giả câm giả điếc, không nghe không hỏi.")])

add("bullets", section="Thành ngữ 成语和惯用语", title="Thành ngữ (4): 熟视无睹 · 力所能及", size=34,
    items=["## 熟视无睹 shúshì-wúdǔ – nhìn quen mà như không thấy, thờ ơ",
           "对于损坏公物的现象，我们决不能熟视无睹。",
           "他生活在那样的环境中，久而久之，对一些不良现象竟是熟视无睹。",
           "## 力所能及 lìsuǒnéngjí – trong khả năng của mình (力: sức; 及: đạt tới)",
           "我们平常可以做一些力所能及的家务活来减轻父母的负担。",
           "当你发现有人需要救助时，除了报告警察外，自己也要给予力所能及的帮助。"],
    say=[F(0, "Thứ mười: 熟视无睹. 熟视 là nhìn quen, nhìn mãi; 无睹 là như không thấy. Tuy thường xuyên nhìn thấy mà như không thấy, chỉ thái độ thờ ơ với điều đáng quan tâm. Khác với 装聋作哑 là cố tình giả vờ, 熟视无睹 nhấn mạnh sự quen mắt đến mức thờ ơ."),
         F(1, "Ví dụ: 对于损坏公物的现象，我们决不能熟视无睹。 Đối với hiện tượng phá hoại của công, chúng ta quyết không thể làm ngơ."),
         F(2, "Ví dụ: 他生活在那样的环境中，久而久之，对一些不良现象竟是熟视无睹。 Sống trong môi trường như thế, lâu dần, anh ta lại thờ ơ trước những hiện tượng xấu. 久而久之 là lâu dần."),
         F(3, "Thứ mười một: 力所能及. 力 là sức lực, năng lực; 及 là đạt tới. Những việc mà sức mình có thể làm được. Trong bài: 家暴目击者进行力所能及的劝阻."),
         F(4, "Ví dụ: 我们平常可以做一些力所能及的家务活来减轻父母的负担。 Hằng ngày chúng ta có thể làm những việc nhà vừa sức để giảm gánh nặng cho bố mẹ."),
         F(5, "Ví dụ: 当你发现有人需要救助时，除了报告警察外，自己也要给予力所能及的帮助。 Khi phát hiện có người cần cứu giúp, ngoài báo cảnh sát, bản thân cũng nên giúp đỡ trong khả năng của mình.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 课后练习", title="Bài tập 1: Chọn thành ngữ thích hợp điền vào chỗ trống (1)", reveal=True, size=33,
    items=["## 直起腰杆 · 理直气壮 · 后患无穷 · 忍气吞声 · 公之于众 · 装聋作哑 · 力所能及 · 根深蒂固 · 熟视无睹",
           "(1) 我们要培养孩子做一些___的事，不要娇生惯养。",
           "Đáp án: 力所能及",
           "(2) 遇事要有一个明确的态度，___，回避矛盾是不行的。",
           "Đáp án: 装聋作哑",
           "(3) 为了儿女的前途，她对娘家人的嘲讽只能___。",
           "Đáp án: 忍气吞声",
           "(4) 很多人担心自己的名字被___将会影响他们的就业前景，或者导致他们在现实世界中被跟踪。",
           "Đáp án: 公之于众",
           "(5) 你放走这些狡诈的强盗，简直就是放虎归山，___！",
           "Đáp án: 后患无穷"],
    say=["Phần cuối là luyện tập, phần 趁热打铁 của sách, nghĩa là rèn sắt khi còn nóng. Bài tập một: chọn thành ngữ thích hợp điền vào chỗ trống. Có chín thành ngữ cho chín câu, mỗi thành ngữ dùng một lần.",
         F(1, "Câu một: 我们要培养孩子做一些什么的事，不要娇生惯养。 Chúng ta phải tập cho trẻ làm những việc như thế nào, đừng nuông chiều. 娇生惯养 là được nuông chiều từ bé. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 力所能及. 做一些力所能及的事, làm những việc vừa sức mình."),
         F(3, "Câu hai: 遇事要有一个明确的态度，什么，回避矛盾是不行的。 Gặp việc phải có thái độ rõ ràng, né tránh mâu thuẫn là không được."),
         F(4, "Đáp án: 装聋作哑. Câu này chính là ví dụ của sách: giả câm giả điếc, né tránh mâu thuẫn là không được."),
         F(5, "Câu ba: 为了儿女的前途，她对娘家人的嘲讽只能什么。 Vì tương lai của con cái, trước những lời giễu cợt của nhà ngoại, cô ấy chỉ đành làm gì? 娘家 là nhà mẹ đẻ của người phụ nữ."),
         F(6, "Đáp án: 忍气吞声. Chỉ đành nuốt giận làm thinh."),
         F(7, "Câu bốn: 很多人担心自己的名字被什么将会影响他们的就业前景，或者导致他们在现实世界中被跟踪。 Nhiều người lo rằng tên mình bị làm sao đó sẽ ảnh hưởng đến triển vọng việc làm, hoặc khiến họ bị theo dõi ngoài đời thực."),
         F(8, "Đáp án: 公之于众. Tên bị công khai cho mọi người biết. Chú ý cấu trúc bị động 被公之于众."),
         F(9, "Câu năm: 你放走这些狡诈的强盗，简直就是放虎归山，什么！ Anh thả những tên cướp xảo quyệt này đi, chẳng khác nào thả hổ về rừng!"),
         F(10, "Đáp án: 后患无穷. 放虎归山，后患无穷, thả hổ về rừng thì hậu họa khôn lường. Hai thành ngữ này rất hay đi với nhau.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 1: Chọn thành ngữ thích hợp điền vào chỗ trống (2)", reveal=True, size=34,
    items=["(6) 我们总是容易对自己身边的幸福___。",
           "Đáp án: 熟视无睹",
           "(7) 几千年来“养儿防老”“多子多福”的旧观念，在文化不发达的山区，至今仍是___。",
           "Đáp án: 根深蒂固",
           "(8) 我___地对他说：“做人应该要讲原则！”",
           "Đáp án: 理直气壮",
           "(9) 小时候父亲总是教育我们，要弯下腰来做事，___做人。",
           "Đáp án: 直起腰杆"],
    say=[F(0, "Câu sáu: 我们总是容易对自己身边的幸福什么。 Chúng ta luôn dễ như thế nào với hạnh phúc ngay bên cạnh mình?"),
         F(1, "Đáp án: 熟视无睹. Hạnh phúc ở ngay bên cạnh, nhìn mãi thành quen, nên chẳng còn nhận ra."),
         F(2, "Câu bảy: 几千年来养儿防老、多子多福的旧观念，在文化不发达的山区，至今仍是什么。 Mấy nghìn năm nay, quan niệm cũ nuôi con phòng già, đông con nhiều phúc, ở vùng núi văn hóa kém phát triển, đến nay vẫn ra sao?"),
         F(3, "Đáp án: 根深蒂固. Quan niệm ăn sâu bén rễ. Các bạn để ý cụm 养儿防老, đây chính là chủ đề của bài sau."),
         F(4, "Câu tám: 我什么地对他说：做人应该要讲原则！ Tôi nói với anh ta một cách thế nào: làm người phải có nguyên tắc!"),
         F(5, "Đáp án: 理直气壮. Nói một cách đường hoàng, hùng hồn, vì mình có lý."),
         F(6, "Câu chín: 小时候父亲总是教育我们，要弯下腰来做事，什么做人。 Hồi nhỏ bố luôn dạy chúng tôi: phải cúi lưng xuống mà làm việc, và làm người thì sao?"),
         F(7, "Đáp án: 直起腰杆. 弯下腰来做事，直起腰杆做人: làm việc thì khiêm tốn, chăm chỉ; làm người thì ngay thẳng, có khí phách. Một câu rất đẹp, các bạn nên ghi nhớ.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn từ thích hợp nhất (1)", reveal=True, size=34,
    items=["(1) 长江流域发生特大洪灾，___着全国亿万人民的心。  A.打动 B.触动 C.牵动 D.感动",
           "Đáp án: C. 牵动 – cụm cố định 牵动……的心: khiến lòng người lo lắng không yên.",
           "(2) 眼看敌人就要攻陷我们的城市，千钧一发之际我们必须迅速作出___。  A.决断 B.决议 C.坚决 D.判决",
           "Đáp án: A. 决断 – 作出决断: đưa ra quyết định. 决议 là nghị quyết của hội nghị; 判决 là phán quyết của tòa.",
           "(3) 新颁布的《教师法》从今日起正式___。  A.实施 B.试用 C.施行 D.实行",
           "Đáp án: C. 施行 – luật, quy định bắt đầu có hiệu lực từ một thời điểm: 从……起施行."],
    say=["Bài tập hai: chọn từ thích hợp nhất điền vào chỗ trống.",
         F(0, "Câu một: 长江流域发生特大洪灾，什么着全国亿万人民的心。 Lưu vực sông Trường Giang xảy ra trận lũ lớn đặc biệt, khiến trái tim hàng trăm triệu người dân cả nước thế nào. Bốn lựa chọn: 打动，触动，牵动，感动."),
         F(1, "Đáp án: C, 牵动. 牵动着……的心 là cụm cố định, chỉ một sự việc khiến người ta lo lắng, dõi theo. Còn 打动 và 感动 là làm cảm động, không hợp với tin thiên tai; 触动 là chạm đến, gây xúc động hay khiến suy nghĩ lại."),
         F(2, "Câu hai: 眼看敌人就要攻陷我们的城市，千钧一发之际我们必须迅速作出什么。 Mắt thấy quân địch sắp chiếm được thành phố, vào lúc ngàn cân treo sợi tóc, chúng ta phải nhanh chóng đưa ra cái gì. Lựa chọn: 决断，决议，坚决，判决."),
         F(3, "Đáp án: A, 决断. 作出决断, đưa ra quyết định dứt khoát. 决议 là nghị quyết do hội nghị thông qua; 坚决 là tính từ kiên quyết, không làm tân ngữ; 判决 là phán quyết của tòa án."),
         F(4, "Câu ba: 新颁布的教师法从今日起正式什么。 Luật Giáo viên mới ban hành chính thức có hiệu lực từ hôm nay. Lựa chọn: 实施，试用，施行，实行."),
         F(5, "Đáp án: C, 施行. Đúng định nghĩa của từ mới: luật lệ sau khi công bố thì có hiệu lực từ một thời điểm, giống câu trong bài 反家庭暴力法正式施行. 实施 và 实行 nhấn mạnh việc đưa vào thực hiện một kế hoạch, chính sách; 试用 là dùng thử.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn từ thích hợp nhất (2)", reveal=True, size=34,
    items=["(4) 在这次的发言中，他引用了大量的古语来___自己的观点。  A.注明 B.查明 C.声名 D.阐明",
           "Đáp án: D. 阐明 – 阐明观点: trình bày rõ quan điểm.",
           "(5) 务必让孩子保持呼吸道___，躺下的时候头胸部可稍稍抬高。  A.通畅 B.畅通 C.通顺 D.流畅",
           "Đáp án: A. 通畅 – 呼吸道通畅: đường hô hấp thông thoáng. 畅通 hay nói đường sá; 通顺 nói câu văn; 流畅 nói lời nói, văn viết trôi chảy."],
    say=[F(0, "Câu bốn: 在这次的发言中，他引用了大量的古语来什么自己的观点。 Trong bài phát biểu lần này, ông ấy dẫn rất nhiều câu cổ ngữ để làm gì với quan điểm của mình. Lựa chọn: 注明，查明，声名，阐明."),
         F(1, "Đáp án: D, 阐明. 阐明观点, trình bày rõ quan điểm. 注明 là ghi chú rõ, 查明 là điều tra làm rõ, còn 声名 là danh tiếng."),
         F(2, "Câu năm: 务必让孩子保持呼吸道什么，躺下的时候头胸部可稍稍抬高。 Nhất định phải giữ cho đường hô hấp của trẻ thế nào, khi nằm có thể kê đầu và ngực cao lên một chút. Lựa chọn: 通畅，畅通，通顺，流畅."),
         F(3, "Đáp án: A, 通畅. 呼吸道通畅 là đường hô hấp thông thoáng. 通畅 và 畅通 rất gần nhau; nhưng với hơi thở, đại tiện, kênh thông tin người ta hay dùng 通畅, còn 畅通 hay dùng cho giao thông: 道路畅通. 通顺 dùng cho câu văn, 流畅 cho lời nói, văn viết trôi chảy.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Giải thích nghĩa phần gạch chân", reveal=True, size=34,
    items=["(1) 让受害者【直起腰杆】，反家暴需要打破沉默。",
           "Đáp án: 有底气、硬气，不再害怕、不再忍让 – giúp nạn nhân tự tin, cứng cỏi đứng lên bảo vệ mình.",
           "(2) 这个社会需要有人站出来，为弱势群体【发声】。",
           "Đáp án: 公开说出意见、表明态度，替他们说话 – công khai lên tiếng, nói thay cho nhóm yếu thế.",
           "(3) 你为什么要把那些事情告诉他，你要知道，【家丑不可外扬】。",
           "Đáp án: 家里不光彩的事不应该告诉外人 – chuyện xấu trong nhà không nên kể với người ngoài.",
           "(4) 【清官难断家务事】的传统观念根深蒂固。",
           "Đáp án: 家庭内部的纠纷，外人很难判断谁对谁错 – tranh chấp trong nhà, người ngoài khó phân xử đúng sai."],
    say=["Bài tập ba: nói ra nghĩa của phần được gạch chân. Trên slide, phần gạch chân được đặt trong ngoặc vuông.",
         F(0, "Câu một: 让受害者直起腰杆，反家暴需要打破沉默。 Phần gạch chân là 直起腰杆."),
         F(1, "Đáp án: 有底气、硬气，不再害怕、不再忍让。 Tức là có chỗ dựa, có khí phách, không còn sợ hãi, không còn nhẫn nhịn. Cả câu: muốn nạn nhân đứng thẳng lưng, chống bạo lực gia đình cần phá vỡ sự im lặng."),
         F(2, "Câu hai: 这个社会需要有人站出来，为弱势群体发声。 Phần gạch chân là 发声. 弱势群体 là nhóm yếu thế."),
         F(3, "Đáp án: 公开说出意见、表明态度，替他们说话。 Tức là công khai nói lên ý kiến, bày tỏ thái độ, nói thay cho họ. Giống như vợ cũ, bạn bè và cô học trò đã 为受害者发了声."),
         F(4, "Câu ba: 你为什么要把那些事情告诉他，你要知道，家丑不可外扬。"),
         F(5, "Đáp án: 家里不光彩的事不应该告诉外人。 Chuyện không vẻ vang trong nhà thì không nên kể với người ngoài. 不光彩 là không vẻ vang, đáng xấu hổ."),
         F(6, "Câu bốn: 清官难断家务事的传统观念根深蒂固。"),
         F(7, "Đáp án: 家庭内部的纠纷，外人很难判断谁对谁错。 Tranh chấp trong gia đình, người ngoài rất khó phán đoán ai đúng ai sai; vì thế người ta thường ngại can thiệp vào chuyện nhà người khác.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Điền từ, thành ngữ vào đoạn văn về “bạo lực lạnh”", reveal=True, size=32,
    items=["## 底线 · 家丑不可外扬 · 坠入 · 忍气吞声 · 装聋作哑 · 恶性",
           "……家庭冷暴力，多指夫妻双方产生矛盾时，漠不关心对方，在一方表达出交流意愿时，另一方仍然___，不予理睬。遭受冷暴力的一方，抱着___的态度，即使受了委屈，也只是___，暗自伤心。在一方持续挑战另一方的___后，夫妻关系进入___循环，婚姻就此___深渊，双方都成了这段关系的受害者。",
           "Đáp án: 装聋作哑 · 家丑不可外扬 · 忍气吞声 · 底线 · 恶性 · 坠入"],
    say=["Bài tập bốn: dùng từ và thành ngữ cho sẵn điền vào đoạn văn. Đoạn văn nói về 冷暴力, bạo lực lạnh. Có sáu lựa chọn: 底线，家丑不可外扬，坠入，忍气吞声，装聋作哑，恶性.",
         "Đoạn văn mở đầu thế này: 冷暴力是暴力的一种，其表现形式多为冷淡、轻视、放任、疏远和漠不关心，致使他人精神上和心理上受到侵犯和伤害。 Bạo lực lạnh là một dạng bạo lực, biểu hiện thường là lạnh nhạt, coi thường, bỏ mặc, xa lánh và thờ ơ, khiến người khác bị xâm hại, tổn thương về tinh thần và tâm lý.",
         F(1, "Tiếp theo là phần cần điền: 家庭冷暴力，多指夫妻双方产生矛盾时，漠不关心对方，在一方表达出交流意愿时，另一方仍然什么，不予理睬。遭受冷暴力的一方，抱着什么的态度，即使受了委屈，也只是什么，暗自伤心。在一方持续挑战另一方的什么后，夫妻关系进入什么循环，婚姻就此什么深渊，双方都成了这段关系的受害者。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 另一方仍然装聋作哑，不予理睬。遭受冷暴力的一方，抱着家丑不可外扬的态度，即使受了委屈，也只是忍气吞声，暗自伤心。在一方持续挑战另một方的底线后，夫妻关系进入恶性循环，婚姻就此坠入深渊。".replace("另một方", "另一方")),
         "Dịch nghĩa: khi một bên muốn trò chuyện, bên kia vẫn giả câm giả điếc, không thèm đáp lại. Bên bị bạo lực lạnh mang thái độ chuyện xấu trong nhà không được đưa ra ngoài, dù bị ấm ức cũng chỉ nuốt giận làm thinh, âm thầm đau khổ. Khi một bên liên tục thách thức giới hạn của bên kia, quan hệ vợ chồng rơi vào vòng luẩn quẩn tồi tệ, hôn nhân từ đó rơi xuống vực thẳm, cả hai đều trở thành nạn nhân. 恶性循环 là vòng luẩn quẩn, vòng xoáy tiêu cực, một cụm rất hay dùng."])

# ======================= THẢO LUẬN =======================
add("bullets", chapter="Thảo luận: liên hệ Việt Nam", section="Thảo luận 讨论", title="Thảo luận: Việt Nam và bạo lực gia đình", size=34,
    items=["Tục ngữ Việt gần với 家丑不可外扬: “Tốt đẹp phô ra, xấu xa đậy lại” · “Đóng cửa bảo nhau”",
           "Việt Nam có Luật Phòng, chống bạo lực gia đình (2007; sửa đổi năm 2022)",
           "Khẩn cấp gọi 113 · Trẻ em bị bạo hành: Tổng đài 111",
           "## Luyện nói (dùng từ của bài):",
           "家暴不是家务事，而是违法犯罪。作为邻居，我们不能熟视无睹，应该进行力所能及的劝阻或者及时报警。",
           "Câu hỏi: 如果你的邻居发生了家暴，你会袖手旁观还是出手相助？"],
    say=["Trước khi tổng kết, chúng ta cùng liên hệ với Việt Nam.",
         F(0, "Quan niệm 家丑不可外扬 không chỉ có ở Trung Quốc. Tiếng Việt cũng có những câu như: tốt đẹp phô ra, xấu xa đậy lại; hay đóng cửa bảo nhau. Ở nhiều gia đình Việt, chuyện vợ chồng đánh nhau vẫn bị coi là chuyện riêng, người ngoài không nên xen vào. Đó chính là 清官难断家务事."),
         F(1, "Về pháp luật, Việt Nam đã có Luật Phòng, chống bạo lực gia đình từ năm hai nghìn không trăm lẻ bảy, và luật này được sửa đổi vào năm hai nghìn không trăm hai mươi hai. Cũng giống Trung Quốc, luật khẳng định bạo lực gia đình là hành vi vi phạm pháp luật, không phải chuyện riêng."),
         F(2, "Nếu chứng kiến bạo lực, trong trường hợp khẩn cấp hãy gọi một một ba cho công an; nếu nạn nhân là trẻ em, có thể gọi Tổng đài quốc gia bảo vệ trẻ em một một một."),
         F(3, "Bây giờ các bạn hãy luyện nói, cố gắng dùng các từ vừa học."),
         F(4, "Câu mẫu: 家暴不是家务事，而是违法犯罪。作为邻居，我们不能熟视无睹，应该进行力所能及的劝阻或者及时报警。 Bạo lực gia đình không phải chuyện riêng trong nhà, mà là vi phạm pháp luật. Là hàng xóm, chúng ta không thể làm ngơ, mà nên khuyên ngăn trong khả năng của mình hoặc kịp thời báo cảnh sát."),
         F(5, "Câu hỏi cho các bạn, cũng là đề tài điều tra trong phần ôn tập của đơn vị: 如果你的邻居发生了家暴，你会袖手旁观还是出手相助？ Nếu nhà hàng xóm xảy ra bạo lực gia đình, bạn sẽ khoanh tay đứng nhìn hay ra tay giúp đỡ? 袖手旁观 là khoanh tay đứng nhìn. Hãy tạm dừng video và trả lời bằng tiếng Trung, ít nhất năm câu nhé.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết", section="Tổng kết", title="Tổng kết bài 5.1", size=34,
    items=["Từ vựng trọng tâm: 家暴 · 容忍 · 牵动 · 底线 · 坠入深渊 · 赡养 · 舆论 · 施暴 · 正视 · 恶劣 · 施行 · 阐明 · 纵容 · 劝阻 · 报案 · 维权 · 凝聚 · 防线",
           "Câu mẫu: 该 + danh từ (văn công vụ) · ……，相比之下，…… · 进而 · 宁愿……也不/也要……",
           "Kết hợp từ: 附上资料 · 摆脱困境 · 零容忍/零排放/零误差 · 一起事故/案件/事件",
           "Thành ngữ: 直起腰杆 · 理直气壮 · 后患无穷 · 家丑不可外扬 · 忍气吞声 · 公之于众 · 清官难断家务事 · 根深蒂固 · 装聋作哑 · 熟视无睹 · 力所能及",
           "Thông điệp: 家暴不是家务事 → 打破沉默 → 零容忍"],
    say=["Chúng ta cùng tổng kết bài năm chấm một.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 家暴，容忍，牵动，底线，坠入深渊，赡养，舆论，施暴，正视，恶劣，施行，阐明，纵容，劝阻，报案，维权，凝聚，防线. Đây đều là những từ rất hay gặp trên báo chí khi nói về vấn đề xã hội."),
         F(1, "Về câu mẫu: 该 cộng danh từ là giọng văn công vụ, tin tức; 相比之下 dùng để so sánh, làm nổi bật khác biệt; 进而 là từ đó tiến thêm một bước; và 宁愿……也不 hay 宁愿……也要 là câu lựa chọn thà… chứ…."),
         F(2, "Về kết hợp từ: 附上资料，摆脱困境，零容忍，零排放，零误差, và lượng từ 起 trong 一起事故，一起案件，一起事件."),
         F(3, "Về thành ngữ, mười một thành ngữ và quán ngữ, trong đó hai câu 家丑不可外扬 và 清官难断家务事 là chìa khóa để hiểu vì sao nạn nhân bạo lực gia đình thường im lặng."),
         F(4, "Và thông điệp của bài: bạo lực gia đình không phải chuyện nhà, phải phá vỡ sự im lặng, và cả xã hội phải không khoan nhượng."),
         "Bài tập về nhà: các bạn hãy viết một đoạn văn khoảng ba trăm chữ với đề 为什么家暴受害者常常保持沉默？, vì sao nạn nhân bạo lực gia đình thường im lặng, cố gắng dùng 相比之下，进而，宁愿……也…… và ít nhất ba thành ngữ của bài.",
         "Cảm ơn các bạn đã theo dõi bài giảng. Ở bài sau, bài năm chấm hai, chúng ta sẽ chuyển sang một vấn đề gia đình khác: 养儿防老变养子啃老？ Nuôi con phòng già, hay nuôi con để con ăn bám? Bài khóa bàn về hiện tượng 啃老族, những người trưởng thành vẫn sống dựa vào bố mẹ. Hẹn gặp lại các bạn. Chúc các bạn học tốt!"])

lesson = {
    "title": "顶石中文 – Bài 5.1: 对家暴必须“零容忍” (Phải “không khoan nhượng” với bạo lực gia đình)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"宁愿": "佞愿",            # nìngyuàn
                    "当天": "荡天",            # dàngtiān
                    "处以": "楚以",            # chǔyǐ
                    "为妇女": "维妇女",        # wéi (là)
                    "极为": "极维",            # jíwéi
                    "为人": "维人",            # wéirén
                    "给予": "己予",            # jǐyǔ
                    "助长": "助掌",            # zhùzhǎng
                    "长辈": "掌辈",            # zhǎngbèi
                    "年长": "年掌",            # niánzhǎng
                    "曲直": "屈直",            # qūzhí
                    "应有": "英有",            # yīngyǒu
                    "处于": "楚于"},           # chǔyú
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds51.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
