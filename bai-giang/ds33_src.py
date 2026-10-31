#!/usr/bin/env python3
"""Kịch bản bài giảng 顶石中文 – Bài 3.3 «“塑战”能否速决？» (kèm ôn tập Đơn vị 3). Chạy để sinh ds33.json."""
import json
import os

TAG = "顶石中文 · Bài 3.3 · “塑战”能否速决？"
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
    zh="“塑战”能否速决？", py="“Sùzhàn” néngfǒu sùjué?",
    vi="Bài 3.3: “Cuộc chiến nhựa” có thắng nhanh được không?",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng giáo trình 顶石中文, Đỉnh cao tiếng Trung.",
         "Hôm nay chúng ta học bài ba chấm ba: 塑战能否速决？ Nghĩa là: Cuộc chiến với nhựa có thể thắng nhanh được không?",
         "Đây là bài cuối cùng của Đơn vị ba, 环保篇, chủ đề Bảo vệ môi trường. Từ 塑战 được ghép từ 塑料, nhựa, và 战, cuộc chiến. Bài khóa là một bài báo mạng, bàn về lệnh cấm nhựa năm 2020 của Trung Quốc: túi ni lông tiện lợi đến thế, vì sao lại trở thành phát minh tồi tệ nhất, và vì sao sống không nhựa lại khó đến vậy.",
         "Cuối bài, chúng ta sẽ có thêm một phần ôn tập cả Đơn vị ba, theo phần 单元练习 của sách."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học", size=40,
    items=["Hiểu bài báo: từ “限塑” đến “禁塑”, vì sao “塑战” không thể thắng nhanh",
           "Nắm vững 50 từ mới (có 10 thành ngữ), kèm âm Hán Việt và ví dụ",
           "10 mẫu câu: 被誉为 · 扮演……角色 · 经久难…… · 之余 · 贴标签 · 谈何 · 别说……就是…… · 从……入手 · 可喜的是 · 进行到底",
           "Kết hợp từ: 渗透 · 切入 · 先行 · 随机 · 瘾 · 植入",
           "Bài tập của sách, liên hệ Việt Nam, và ôn tập Đơn vị 3"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu bài báo: chính sách của Trung Quốc đã đi từ hạn chế nhựa đến cấm nhựa như thế nào, và vì sao cuộc chiến với nhựa không thể thắng nhanh."),
         F(1, "Thứ hai, nắm vững năm mươi từ mới, trong đó có mười thành ngữ rất hay dùng như 举足轻重，罪魁祸首，谈何容易，一朝一夕."),
         F(2, "Thứ ba, học mười mẫu câu trọng điểm, như 被誉为, 扮演什么的角色, 谈何容易, 别说什么就是什么, 从什么入手, 可喜的是, và 进行到底."),
         F(3, "Thứ tư, học kết hợp từ của 渗透，切入，先行，随机，瘾，植入."),
         F(4, "Thứ năm, làm bài tập của sách, liên hệ với cuộc chiến chống rác thải nhựa ở Việt Nam, và cuối cùng là ôn tập cả Đơn vị ba."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 课前思考", title="Câu hỏi khởi động 课前思考", size=36,
    items=["1．塑料给人类生活带来了哪些便利？",
           "Gợi ý: 轻便、便宜、结实、防水 · 塑料袋、包装、吸管、外卖餐盒……",
           "2．你清楚塑料对环境的危害吗？都有哪些？",
           "Gợi ý: 难以降解 · 污染土地和海洋 · 伤害海洋生物 · 微塑料进入食物链",
           "3．如果在生活中限制一次性塑料制品的使用，你认为我们会遇到哪些挑战？"],
    say=["Trước khi vào bài, sách đưa ra ba câu hỏi để chúng ta suy nghĩ.",
         F(0, "Câu một: 塑料给人类生活带来了哪些便利？ Nhựa đã mang lại cho cuộc sống con người những tiện lợi gì?"),
         F(1, "Gợi ý: 轻便、便宜、结实、防水, nhẹ, rẻ, bền, chống nước. Chúng ta dùng nhựa ở khắp nơi: túi ni lông, bao bì, ống hút, hộp đựng đồ ăn mang về."),
         F(2, "Câu hai: 你清楚塑料对环境的危害吗？都有哪些？ Bạn có biết rõ tác hại của nhựa đối với môi trường không? Có những tác hại nào?"),
         F(3, "Gợi ý: 难以降解, khó phân hủy, có loại mấy trăm năm mới phân hủy; 污染土地和海洋, gây ô nhiễm đất và biển; 伤害海洋生物, làm hại sinh vật biển; và 微塑料进入食物链, vi nhựa đi vào chuỗi thức ăn, cuối cùng vào cơ thể con người."),
         F(4, "Câu ba: 如果在生活中限制一次性塑料制品的使用，你认为我们会遇到哪些挑战？ Nếu hạn chế dùng đồ nhựa dùng một lần trong cuộc sống, bạn nghĩ chúng ta sẽ gặp những thách thức gì? Câu này chúng ta sẽ thảo luận ở cuối bài.")])

add("compare", section="Khởi động 课前思考", title="Bối cảnh: 限塑令 và 禁塑令 (theo phần 注释)",
    common="Bài khóa so sánh hai văn bản chính sách của Trung Quốc về túi ni lông và đồ nhựa.",
    cols=[{"head": "限塑令 (2008)",
           "lines": ["Lệnh hạn chế nhựa: thông tri của Văn phòng Quốc vụ viện, 31/12/2007",
                     "Từ 1/6/2008: siêu thị, chợ… không được phát túi ni lông miễn phí",
                     "Kết quả: thành chuyện “trả thêm hai hào mua cái túi”"]},
          {"head": "禁塑令 (2020)",
           "lines": ["Lệnh cấm nhựa: ý kiến của Ủy ban Cải cách và Phát triển cùng Bộ Sinh thái và Môi trường, 19/1/2020",
                     "Cuối 2020: các thành phố lớn cấm túi ni lông không phân hủy ở siêu thị, đồ ăn mang về…",
                     "Cụ thể hơn, đi thẳng vào cuộc sống"]}],
    say=["Để hiểu bài khóa, chúng ta cần phân biệt hai văn bản chính sách, theo phần chú thích của sách: 限塑令 và 禁塑令.",
         F(0, "限塑令, lệnh hạn chế nhựa, là tên người dân gọi thông tri của Văn phòng Quốc vụ viện ban hành ngày ba mươi mốt tháng mười hai năm 2007. Từ ngày một tháng sáu năm 2008, siêu thị, trung tâm thương mại, chợ không được phát túi ni lông miễn phí; muốn dùng túi thì phải trả tiền."),
         F(0, "Kết quả thế nào? Bài khóa nói, lâu dần nó chỉ còn là chuyện trả thêm hai hào mua cái túi. Chữ 限 là hạn chế."),
         F(1, "禁塑令, lệnh cấm nhựa, là văn bản ý kiến do Ủy ban Cải cách và Phát triển Quốc gia cùng Bộ Sinh thái và Môi trường ban hành ngày mười chín tháng một năm 2020. Đến cuối năm 2020, siêu thị, trung tâm thương mại, dịch vụ đồ ăn mang về ở các thành phố trực thuộc trung ương, thủ phủ các tỉnh phải ngừng dùng túi ni lông không phân hủy được."),
         F(1, "Chữ 禁 là cấm. So với lệnh cũ, lệnh mới cụ thể hơn, đi thẳng vào cuộc sống hơn. Nhưng liệu nó có thành công? Chúng ta cùng đọc bài.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("誉", "yù", "dự", "động từ", "khen ngợi, ca tụng (被誉为: được mệnh danh là)", "他被誉为计算机之父。", "Ông được tôn vinh là cha đẻ của máy tính.",
     "Động từ, nghĩa là khen ngợi, ca tụng, văn viết. Gần như luôn dùng trong mẫu 被誉为, được ca ngợi là, được mệnh danh là. Âm Hán Việt là dự, như trong danh dự, vinh dự. Câu mở đầu bài khóa: 塑料被誉为人类最伟大的发明之一. Đây cũng là mẫu câu thứ nhất."),
    ("渗透", "shèntòu", "thẩm thấu", "động từ", "thấm vào, len lỏi, thâm nhập", "污水渗透到了地下水源。", "Nước thải đã ngấm vào nguồn nước ngầm.",
     "Động từ, nghĩa gốc là chất lỏng thấm qua; nghĩa bóng là một thứ dần dần đi vào và lan rộng ra các mặt khác, thường dùng cho sự vật trừu tượng: 思想渗透, sự thâm nhập tư tưởng. Trong bài: 塑料已经渗透到我们衣食住行的方方面面, nhựa đã len lỏi vào mọi mặt của đời sống."),
    ("衣食住行", "yī-shí-zhù-xíng", "y thực trú hành", "thành ngữ", "ăn mặc ở đi lại; nhu cầu cơ bản", "改革开放改变了老百姓的衣食住行。", "Cải cách mở cửa đã thay đổi chuyện ăn mặc ở đi lại của người dân.",
     "Thành ngữ: mặc, ăn, ở, đi lại, tức là những nhu cầu cơ bản của cuộc sống. Chú ý thứ tự trong tiếng Trung là mặc trước ăn sau, ngược với tiếng Việt ăn mặc. Trong bài: 衣食住行的方方面面, mọi mặt của đời sống."),
    ("进程", "jìnchéng", "tiến trình", "danh từ", "tiến trình, quá trình", "比赛进程比预想的要快。", "Tiến trình trận đấu nhanh hơn dự tính.",
     "Danh từ, nghĩa là quá trình sự việc biến đổi, tiến triển. Hay gặp: 会议进程, 历史进程, 城镇化进程. Trong bài: 在当今人类文明的进程中, trong tiến trình văn minh nhân loại ngày nay."),
    ("举足轻重", "jǔzú-qīngzhòng", "cử túc khinh trọng", "thành ngữ", "giữ vai trò cực kỳ quan trọng", "他在公司里有着举足轻重的地位。", "Anh ấy có vị trí cực kỳ quan trọng trong công ty.",
     "Thành ngữ. Nghĩa đen là nhấc chân lên cũng làm lệch cán cân: một người đứng giữa hai bên, nghiêng về bên nào thì bên đó nặng hơn. Nghĩa bóng là có vai trò quyết định, cực kỳ quan trọng. Hay đi với 角色，作用，地位. Trong bài: 扮演着举足轻重的角色."),
    ("瞬间", "shùnjiān", "thuấn gian", "danh từ", "khoảnh khắc, trong nháy mắt", "那一瞬间，我明白了一切。", "Trong khoảnh khắc ấy, tôi đã hiểu ra tất cả.",
     "Danh từ, nghĩa là trong chớp mắt; chữ 瞬 là chớp mắt. Có thể làm trạng ngữ: 瞬间爆炸. Trong bài: 塑料垃圾产出量瞬间爆炸, lượng rác nhựa bùng nổ trong chớp mắt."),
    ("泛滥成灾", "fànlàn-chéngzāi", "phiếm lạm thành tai", "thành ngữ", "tràn lan thành thảm họa", "假冒伪劣商品泛滥成灾。", "Hàng giả, hàng kém chất lượng tràn lan thành nạn.",
     "Thành ngữ. 泛滥 là nước lũ tràn bờ, 成灾 là thành tai họa. Nghĩa đen là lũ lụt gây thiên tai; nghĩa bóng là thứ gì đó nhiều quá mức đến nỗi thành tai họa. Trong bài: 塑料垃圾产出量瞬间爆炸，泛滥成灾."),
    ("罪魁祸首", "zuìkuí-huòshǒu", "tội khôi họa thủ", "thành ngữ", "thủ phạm chính, nguyên nhân chính gây họa", "高糖食物是导致肥胖的罪魁祸首。", "Đồ ăn nhiều đường là thủ phạm chính gây béo phì.",
     "Thành ngữ. 罪魁 là kẻ cầm đầu tội ác, 祸首 là kẻ gây ra tai họa: chỉ người hoặc nguyên nhân chủ yếu gây ra tai họa. Trong bài: 其中的罪魁祸首便是塑料袋, thủ phạm chính trong đó chính là túi ni lông."),
    ("双刃剑", "shuāngrènjiàn", "song nhận kiếm", "danh từ", "con dao hai lưỡi", "权力是一把双刃剑。", "Quyền lực là con dao hai lưỡi.",
     "Danh từ, nghĩa đen là thanh kiếm có lưỡi ở cả hai bên; nghĩa bóng là thứ vừa có lợi vừa có hại, giống con dao hai lưỡi của tiếng Việt. Lượng từ là 把. Trong bài: 科学技术是一把双刃剑."),
    ("顽疾", "wánjí", "ngoan tật", "danh từ", "bệnh dai dẳng, bệnh khó chữa", "大夫治好了我多年的顽疾。", "Bác sĩ đã chữa khỏi căn bệnh dai dẳng nhiều năm của tôi.",
     "Danh từ, nghĩa là căn bệnh khó chữa, kéo dài; nghĩa bóng là vấn đề tồn tại lâu năm khó giải quyết. Chữ 顽 là ngoan cố, như 顽固. Trong bài: 白色污染的顽疾, căn bệnh nan y mang tên ô nhiễm trắng."),
    ("愈", "yù", "dũ", "động từ", "khỏi (bệnh)", "他的病已经痊愈了。", "Bệnh của anh ấy đã khỏi hẳn rồi.",
     "Động từ, nghĩa là khỏi bệnh, văn viết. Hay gặp: 病愈, 痊愈, 不治而愈. Trong bài: 经久难愈, lâu ngày khó khỏi. Chú ý: chữ này còn là phó từ trong 愈来愈, càng ngày càng, giống 越来越."),
    ("痛恨", "tònghèn", "thống hận", "động từ", "căm ghét, căm hận", "我痛恨那些虚假的新闻。", "Tôi căm ghét những tin tức giả dối ấy.",
     "Động từ, nghĩa là căm ghét đến cực độ. Âm Hán Việt thống hận. Trong bài: 一家英国媒体痛恨之余, một tờ báo Anh căm ghét đến mức."),
    ("标签", "biāoqiān", "tiêu thiêm", "danh từ", "nhãn, mác", "每件衣服上都有价格标签。", "Mỗi bộ quần áo đều có nhãn giá.",
     "Danh từ, nghĩa gốc là mẩu giấy dán hoặc buộc trên hàng hóa, ghi tên, công dụng, giá cả; nghĩa bóng là cái mác người ta gán cho ai đó. Mẫu 给什么贴上标签 là mẫu câu thứ năm. Trong bài: 贴上人类最糟糕的发明的标签."),
    ("恐怖", "kǒngbù", "khủng bố", "tính từ", "kinh hoàng, đáng sợ", "这部电影太恐怖了。", "Bộ phim này đáng sợ quá.",
     "Tính từ, nghĩa là đáng sợ, kinh hoàng. Cẩn thận: tiếng Việt khủng bố thường chỉ bạo lực chính trị; tiếng Trung cũng có nghĩa đó, như 恐怖主义, 恐怖分子; nhưng trong đời thường, 恐怖 chủ yếu là đáng sợ: 恐怖片 là phim kinh dị. Trong bài: 白色污染的恐怖, sự đáng sợ của ô nhiễm trắng."),
    ("谈何容易", "tánhé-róngyì", "đàm hà dung dịch", "thành ngữ", "nói thì dễ, làm mới khó", "想要脱颖而出谈何容易。", "Muốn nổi bật hẳn lên đâu phải chuyện dễ.",
     "Thành ngữ, nghĩa đen là nói ra thì dễ gì đâu: việc làm không đơn giản như lời nói. Trong bài: 无塑化生活又谈何容易, sống không nhựa đâu phải chuyện dễ. Từ đây ta có mẫu câu 谈何 cộng tính từ, danh từ hoặc động từ."),
    ("棉签", "miánqiān", "miên thiêm", "danh từ", "tăm bông", "护士用棉签给他擦药。", "Y tá dùng tăm bông bôi thuốc cho anh ấy.",
     "Danh từ, đồ dùng y tế: que nhỏ quấn bông ở đầu, tức tăm bông. Lượng từ là 根. Trong bài: 一次性塑料棉签, tăm bông thân nhựa dùng một lần, một trong những sản phẩm bị cấm."),
    ("降解", "jiàngjiě", "giáng giải", "động từ", "phân hủy", "这种塑料袋可以自然降解。", "Loại túi ni lông này có thể tự phân hủy.",
     "Động từ, thuật ngữ hóa học, nghĩa là phân giải hợp chất phức tạp thành chất đơn giản. Hay gặp: 可降解塑料, nhựa phân hủy được; 不可降解, không phân hủy được; 生物降解, phân hủy sinh học."),
    ("切入", "qiērù", "thiết nhập", "động từ", "đi sâu vào, đi thẳng vào", "他的演讲直接切入主题。", "Bài diễn thuyết của anh ấy đi thẳng vào chủ đề.",
     "Động từ, nghĩa là từ một điểm nào đó đi sâu vào bên trong. Chữ đầu đọc thanh một. Hay gặp: 切入点, điểm tiếp cận; 切入正题, vào thẳng vấn đề. Trong bài: 更直接地切入了人们的生活, đi thẳng vào cuộc sống của mọi người hơn."),
    ("先行", "xiānxíng", "tiên hành", "động từ", "đi trước, làm trước", "你们先行一步，我随后就到。", "Các bạn đi trước một bước, tôi đến ngay sau.",
     "Động từ, nghĩa là đi trước, làm trước. Hay gặp: 先行一步, 先行者, người đi tiên phong. Trong bài: 禁塑令在部分城市已先行执行, lệnh cấm nhựa đã được thực hiện trước ở một số thành phố."),
    ("落地", "luòdì", "lạc địa", "động từ", "đi vào thực tế, được triển khai", "这个项目终于落地了。", "Dự án này cuối cùng đã được triển khai.",
     "Động từ, nghĩa gốc là rơi xuống đất, hạ cánh; nghĩa mới là một ý tưởng, chính sách, dự án được triển khai cụ thể, có hiệu quả thực tế. Trong bài: 在政策已落地的广州市, ở Quảng Châu, nơi chính sách đã được triển khai."),
    ("随机", "suíjī", "tùy cơ", "phó từ", "ngẫu nhiên", "电脑会随机选出三名幸运观众。", "Máy tính sẽ chọn ngẫu nhiên ba khán giả may mắn.",
     "Phó từ, nghĩa là không đặt điều kiện, chọn tùy ý, ngẫu nhiên. Cẩn thận: tiếng Việt tùy cơ là tùy cơ ứng biến; còn 随机 là ngẫu nhiên. Hay gặp: 随机采访, 随机调查, 随机抽样."),
    ("政令", "zhènglìng", "chính lệnh", "danh từ", "chính lệnh, pháp lệnh của chính phủ", "政府颁布了最新政令。", "Chính phủ đã ban hành chính lệnh mới nhất.",
     "Danh từ, nghĩa là pháp lệnh do chính phủ công bố. Hay gặp: 颁布政令, 最新政令. Trong bài: 此次政令再度升级, chính lệnh lần này lại được nâng cấp."),
    ("再度", "zàidù", "tái độ", "phó từ", "lại một lần nữa", "两家公司再度合作。", "Hai công ty lại hợp tác một lần nữa.",
     "Phó từ, nghĩa là lần thứ hai, lại một lần nữa, văn viết. Hay gặp: 再度合作, 再度发生, 再度升级."),
    ("漫漫", "mànmàn", "man man", "tính từ", "dằng dặc, đằng đẵng", "漫漫长夜终于过去了。", "Đêm dài đằng đẵng cuối cùng cũng qua.",
     "Tính từ, nghĩa là thời gian hay quãng đường dài dằng dặc, không thấy điểm cuối. Hay gặp: 漫漫长夜, 路途漫漫. Tiểu mục thứ hai của bài: 无塑化前路漫漫, con đường không nhựa phía trước còn dài dằng dặc."),
    ("高昂", "gāo'áng", "cao ngang", "tính từ", "đắt đỏ (giá cả); dâng cao", "他为此付出了高昂的代价。", "Anh ấy đã phải trả một cái giá đắt cho việc này.",
     "Tính từ, nghĩa trong bài là giá cả rất cao, đắt đỏ: 价格高昂, 高昂的成本, 高昂的代价. Ngoài ra còn nghĩa là dâng cao, hăng hái: 士气高昂."),
    ("望而却步", "wàng'ér-quèbù", "vọng nhi khước bộ", "thành ngữ", "nhìn thấy đã chùn bước", "这本小说太难懂了，许多读者翻了两页就望而却步。", "Tiểu thuyết khó hiểu quá, nhiều người đọc mới lật hai trang đã bỏ.",
     "Thành ngữ. 却步 là lùi bước: vừa nhìn thấy đã lùi lại, chỉ thứ gì đáng sợ hoặc quá khó khiến người ta chùn bước. Trong bài: 谈及高昂的成本，人们望而却步, nhắc đến giá thành đắt đỏ là mọi người chùn bước."),
    ("总计", "zǒngjì", "tổng kế", "động từ", "tổng cộng", "这次活动总计花费了五万元。", "Hoạt động lần này tốn tổng cộng năm vạn tệ.",
     "Động từ, nghĩa là cộng tất cả lại. Trong bài: 全世界总计生产出的九十亿吨塑料制品中, trong tổng cộng chín tỷ tấn sản phẩm nhựa mà cả thế giới đã sản xuất ra."),
    ("草草", "cǎocǎo", "thảo thảo", "phó từ", "qua loa, vội vàng", "他草草吃了几口饭就出门了。", "Anh ấy ăn vội vài miếng cơm rồi ra ngoài.",
     "Phó từ, nghĩa là làm qua loa, cẩu thả, vội vàng. Hay gặp: 草草了事, làm qua quýt cho xong; 草草收场, kết thúc vội vàng. Trong bài: 草草地丢进垃圾箱, vứt vội vào thùng rác."),
    ("一朝一夕", "yīzhāo-yīxī", "nhất triêu nhất tịch", "thành ngữ", "một sớm một chiều", "十几年养成的习惯，不是一朝一夕就能改变的。", "Thói quen mười mấy năm không thể đổi trong một sớm một chiều.",
     "Thành ngữ. Chữ thứ hai đọc zhāo, là buổi sáng; chữ cuối là buổi tối: một sớm một chiều, chỉ thời gian rất ngắn, giống hệt tiếng Việt. Thường dùng ở dạng phủ định. Trong bài: 又怎么可能在一朝一夕就戒掉对塑料的瘾, làm sao có thể cai nghiện nhựa trong một sớm một chiều."),
    ("瘾", "yǐn", "ẩn", "danh từ", "cơn nghiện, thói nghiện", "他的烟瘾很大。", "Anh ấy nghiện thuốc lá rất nặng.",
     "Danh từ, nghĩa là sự ham thích, lệ thuộc thành thói quen khó bỏ. Hay gặp: 烟瘾, nghiện thuốc; 上瘾, bị nghiện; 戒瘾, cai nghiện; 过瘾, thỏa thích, đã đời. Trong bài: 戒掉对塑料的瘾, cai cơn nghiện nhựa."),
    ("塑造", "sùzào", "tố tạo", "động từ", "nhào nặn, xây dựng, định hình", "这部小说成功地塑造了一个英雄形象。", "Cuốn tiểu thuyết đã xây dựng thành công một hình tượng anh hùng.",
     "Động từ, nghĩa gốc là nặn tượng; nghĩa bóng là xây dựng, định hình: 塑造形象, xây dựng hình tượng; 塑造人文精神. Chữ 塑 cũng là chữ đầu của 塑料, nhựa. Trong bài: 重新塑造被塑料慢慢渗透的生活, định hình lại cuộc sống đã bị nhựa dần dần len lỏi."),
    ("入手", "rùshǒu", "nhập thủ", "động từ", "bắt tay vào, bắt đầu từ", "解决问题要从调查研究入手。", "Giải quyết vấn đề phải bắt đầu từ điều tra nghiên cứu.",
     "Động từ, nghĩa là bắt tay vào làm, bắt đầu từ chỗ nào đó. Hay gặp trong mẫu 从……入手, mẫu câu thứ tám. Trong bài: 只有从生活细节中入手, chỉ có bắt đầu từ những chi tiết trong đời sống."),
    ("剥离", "bōlí", "bác ly", "động từ", "tách ra, bóc tách", "他的作品无法同故乡剥离开来。", "Tác phẩm của anh ấy không thể tách rời khỏi quê hương.",
     "Động từ, nghĩa là làm cho tróc ra, tách rời ra. Chữ đầu đọc bō. Trong bài: 将塑料从我们的生活中剥离, tách nhựa ra khỏi cuộc sống của chúng ta."),
    ("公益", "gōngyì", "công ích", "danh từ", "công ích, lợi ích công cộng", "她一直热心公益事业。", "Cô ấy luôn nhiệt tình với các hoạt động công ích.",
     "Danh từ, nghĩa là lợi ích chung của cộng đồng, thường chỉ các hoạt động từ thiện, phúc lợi. Hay gặp: 公益活动, 公益组织, 公益广告. Tiểu mục thứ ba của bài: 公益，助力无塑化生活."),
    ("助力", "zhùlì", "trợ lực", "động từ", "giúp sức, hỗ trợ", "科技助力乡村振兴。", "Khoa học công nghệ giúp sức chấn hưng nông thôn.",
     "Động từ, nghĩa là giúp đỡ, tiếp sức, từ thường gặp trong khẩu hiệu và tin tức: 助力绿色生活, 助力经济发展. Trong bài: 助力无塑化生活, góp sức cho cuộc sống không nhựa."),
    ("借助", "jièzhù", "tá trợ", "động từ", "nhờ vào, dựa vào", "他借助词典读懂了这篇文章。", "Nhờ có từ điển, anh ấy đã đọc hiểu bài văn này.",
     "Động từ, nghĩa là nhờ vào sự giúp đỡ của người hay vật khác. Trong bài: 借助一系列公益活动, nhờ vào một loạt hoạt động công ích."),
    ("着手", "zhuóshǒu", "trước thủ", "động từ", "bắt tay vào (làm)", "公司已经着手实施新计划。", "Công ty đã bắt tay vào thực hiện kế hoạch mới.",
     "Động từ, nghĩa là bắt đầu làm, động tay vào. Chữ đầu đọc zhuó. Gần nghĩa với 入手, nhưng 着手 thường có động từ theo sau: 着手改善, 着手调查. Trong bài: 着手改善现状, bắt tay vào cải thiện hiện trạng."),
    ("携手", "xiéshǒu", "huề thủ", "động từ", "chung tay, bắt tay nhau", "两国携手应对气候变化。", "Hai nước chung tay ứng phó với biến đổi khí hậu.",
     "Động từ, nghĩa đen là nắm tay nhau; nghĩa bóng là cùng nhau làm việc gì. Hay gặp: 携手合作, 携手共进. Trong bài: 菜鸟携手通达、百世, Cainiao bắt tay với Tongda và Best."),
    ("缺失", "quēshī", "khuyết thất", "động từ", "thiếu, thiếu hụt", "体育比赛不能缺失公平公正的原则。", "Thi đấu thể thao không thể thiếu nguyên tắc công bằng, công chính.",
     "Động từ, nghĩa là thiếu, mất đi; cũng làm danh từ: sự thiếu hụt. Trong bài: 填补人们塑料环保意识的缺失, bù đắp sự thiếu hụt ý thức bảo vệ môi trường về nhựa của mọi người."),
    ("巨头", "jùtóu", "cự đầu", "danh từ", "ông lớn, gã khổng lồ", "他是金融界的巨头。", "Ông ấy là ông trùm của giới tài chính.",
     "Danh từ, chỉ cá nhân hay tập đoàn có thế lực lớn, chi phối cục diện chính trị, kinh tế. Hay gặp: 金融巨头, 科技巨头. Trong bài: 互联网巨头腾讯, gã khổng lồ Internet Tencent."),
    ("不遗余力", "bùyí-yúlì", "bất di dư lực", "thành ngữ", "dốc hết sức, không tiếc sức", "只要朋友需要，他都会不遗余力地帮忙。", "Chỉ cần bạn bè cần, anh ấy đều dốc hết sức giúp đỡ.",
     "Thành ngữ. 遗 là để lại, 余力 là sức còn dư: không để lại chút sức nào, tức là dốc toàn lực. Trong bài: 腾讯在推动无塑化环保进程中也不遗余力, Tencent cũng dốc hết sức thúc đẩy tiến trình không nhựa."),
    ("源头", "yuántóu", "nguyên đầu", "danh từ", "đầu nguồn, gốc rễ", "解决问题要从源头抓起。", "Giải quyết vấn đề phải nắm từ gốc.",
     "Danh từ, nghĩa gốc là nơi khởi nguồn của dòng nước; nghĩa bóng là căn nguyên của sự việc. Trong bài: 乡村源头垃圾减量, giảm lượng rác ngay từ nguồn ở nông thôn."),
    ("原生态", "yuánshēngtài", "nguyên sinh thái", "danh từ", "trạng thái tự nhiên nguyên sơ", "这里保留着原生态的自然风光。", "Nơi đây còn giữ được phong cảnh thiên nhiên nguyên sơ.",
     "Danh từ, nghĩa là trạng thái tự nhiên vốn có, không bị phá hoại, hài hòa với thiên nhiên. Hay gặp: 保护原生态, 原生态文化. Trong bài: 原生态智慧减塑计划, kế hoạch giảm nhựa thông minh theo hướng sinh thái tự nhiên."),
    ("枚", "méi", "mai", "lượng từ", "chiếc, cái (vật nhỏ)", "他收藏了一百多枚邮票。", "Anh ấy sưu tầm hơn một trăm con tem.",
     "Lượng từ, giống 个, dùng cho vật nhỏ: 一枚邮票, một con tem; 一枚硬币, một đồng xu; 一枚奖章, một tấm huy chương. Trong bài: 减少一枚塑料袋, bớt đi một chiếc túi ni lông."),
    ("联动", "liándòng", "liên động", "động từ", "liên kết, phối hợp cùng chuyển động", "上下联动，才能把工作做好。", "Trên dưới phối hợp nhịp nhàng mới làm tốt được công việc.",
     "Động từ, nghĩa là nhiều sự vật liên quan với nhau, một cái chuyển động thì các cái khác cũng chuyển động theo. Hay gặp: 上下联动, 联动效应. Trong bài: 线上线下联动的公益活动, hoạt động công ích kết hợp trực tuyến và trực tiếp."),
    ("欣慰", "xīnwèi", "hân úy", "tính từ", "vui mừng yên lòng, mãn nguyện", "看到孩子长大成人，父母感到很欣慰。", "Thấy con khôn lớn trưởng thành, cha mẹ rất mãn nguyện.",
     "Tính từ, nghĩa là vui mừng và yên lòng. Hay gặp: 欣慰的笑容, 感到欣慰. Trong bài: 更令人欣慰的是越来越多的孩子参与其中, điều đáng mừng hơn là ngày càng nhiều trẻ em tham gia."),
    ("植入", "zhírù", "thực nhập", "động từ", "cấy vào, đưa vào, lồng ghép", "很多电视剧里都有植入广告。", "Rất nhiều phim truyền hình có quảng cáo lồng ghép.",
     "Động từ, nghĩa là cấy vào, đưa vào: 植入人体, cấy vào cơ thể; 植入广告, quảng cáo lồng ghép; 植入观念, gieo một quan niệm. Trong bài: 无塑化环保理念开始植入孩子的成长过程, ý thức không nhựa bắt đầu được gieo vào quá trình trưởng thành của trẻ."),
    ("赖以", "làiyǐ", "lại dĩ", "động từ", "dựa vào (để)", "土地是农民赖以生存的基础。", "Đất đai là nền tảng mà người nông dân dựa vào để sống.",
     "Động từ, nghĩa là dựa vào cái gì để đạt mục đích, văn viết. Gần như chỉ gặp trong cụm 赖以生存 và 赖以为生. Trong bài: 我们赖以生存的地球, trái đất mà chúng ta dựa vào để sinh tồn."),
    ("点点滴滴", "diǎndiǎn-dīdī", "điểm điểm tích tích", "thành ngữ", "từng chút một, những điều nhỏ nhặt", "他记录下了生活中的点点滴滴。", "Anh ấy ghi lại những điều nhỏ nhặt trong cuộc sống.",
     "Thành ngữ, nghĩa là từng giọt từng chút, chỉ những điều nhỏ nhặt, thường dùng cho quá trình tích lũy dần dần. Trong bài: 通过生活的点点滴滴，从自身做起, qua từng việc nhỏ trong cuộc sống, bắt đầu từ chính mình."),
    ("深入人心", "shēnrù-rénxīn", "thâm nhập nhân tâm", "thành ngữ", "đi sâu vào lòng người", "这句广告词早已深入人心。", "Câu quảng cáo này từ lâu đã in sâu vào lòng người.",
     "Thành ngữ, nghĩa là một lý luận, tư tưởng, chính sách được mọi người hiểu sâu sắc và tin phục. Trong bài: 环保从个人做起的理念正在深入人心, ý tưởng bảo vệ môi trường bắt đầu từ mỗi người đang đi sâu vào lòng người."),
]

add("bullets", chapter="Từ mới (50 từ)", section="Từ mới 生词", title="Phần 1: Từ mới", size=40,
    items=["Bài 3.3 có 40 từ trong bảng từ + 10 thành ngữ (成语) = 50 từ, chia 17 nhóm",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Nhiều thành ngữ “ăn điểm” trong bài viết: 举足轻重 · 罪魁祸首 · 谈何容易 · 一朝一夕 · 深入人心",
           "Chú ý âm đọc: 切入 (qiē) · 剥离 (bō) · 着手 (zhuó) · 一朝一夕 (zhāo)",
           "Từ dễ nhầm: 恐怖 · 随机"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bảng từ của sách có bốn mươi từ; thầy thêm mười thành ngữ trong phần 成语和惯用语, tổng cộng năm mươi từ, chia thành mười bảy nhóm.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Bài này có nhiều thành ngữ rất đắt giá khi viết văn nghị luận, như 举足轻重，罪魁祸首，谈何容易，一朝一夕，深入人心. Các bạn hãy cố gắng dùng chúng trong bài viết của mình."),
         F(3, "Chú ý cách đọc của mấy từ có chữ đa âm: 切入，剥离，着手，一朝一夕. Thầy sẽ nhắc khi gặp từng từ."),
         F(4, "Ngoài ra có hai từ Hán Việt dễ hiểu nhầm: 恐怖 và 随机. Các bạn nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

sizes = [3] * 16 + [2]
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
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung: số viết bằng chữ, bỏ ngoặc kép])
P = [
    ("塑料被誉为人类最伟大的发明之一，因其独特的性能在人类生活中被广泛应用，已经渗透到我们衣食住行的方方面面，在当今人类文明的进程中扮演着举足轻重的角色。然而，近年来随着社会的快速发展，塑料垃圾产出量瞬间爆炸，泛滥成灾，其中的罪魁祸首便是塑料袋。",
     "Nhựa được ca ngợi là một trong những phát minh vĩ đại nhất của loài người. Nhờ tính năng độc đáo, nó được ứng dụng rộng rãi trong đời sống, đã len lỏi vào mọi mặt của chuyện ăn mặc ở đi lại, đóng vai trò cực kỳ quan trọng trong tiến trình văn minh nhân loại ngày nay. Thế nhưng, những năm gần đây, cùng với sự phát triển nhanh chóng của xã hội, lượng rác nhựa thải ra bùng nổ trong chớp mắt, tràn lan thành thảm họa, mà thủ phạm chính trong đó chính là túi ni lông.",
     ["被誉为 là được ca ngợi là, mẫu câu thứ nhất. 因其独特的性能 là nhờ tính năng độc đáo của nó; 其 là nó, văn viết. 渗透到……的方方面面 là len lỏi vào mọi mặt. 扮演着举足轻重的角色 là đóng vai trò cực kỳ quan trọng; 扮演……的角色 là mẫu câu thứ hai.",
      "然而 đánh dấu sự chuyển ý: từ ưu điểm sang tác hại. 产出量 là lượng thải ra. 瞬间爆炸，泛滥成灾 là bùng nổ trong chớp mắt, tràn lan thành họa. 罪魁祸首便是塑料袋: 便 là cách nói văn viết của 就, nghĩa là chính là."]),
    ("科学技术是一把“双刃剑”，诞生于科学家实验室中的塑料袋在给人类生活带来极大便利的同时，也给我们的地球带来了白色污染的顽疾，经久难愈，一家英国媒体痛恨之余，甚至给其贴上“人类最糟糕的发明”的标签。\n我们深知白色污染的恐怖，但是“无塑化”生活又谈何容易？",
     "Khoa học kỹ thuật là một con dao hai lưỡi. Túi ni lông ra đời trong phòng thí nghiệm của các nhà khoa học, vừa mang lại cho con người sự tiện lợi to lớn, vừa mang đến cho trái đất căn bệnh nan y mang tên ô nhiễm trắng, lâu ngày khó chữa. Một tờ báo Anh căm ghét đến mức gán cho nó cái mác “phát minh tồi tệ nhất của loài người”. Chúng ta hiểu rõ sự đáng sợ của ô nhiễm trắng, nhưng sống “không nhựa” đâu phải chuyện dễ?",
     ["诞生于 là ra đời ở; 于 là ở, tại, văn viết. 在……的同时，也…… là vừa… đồng thời cũng…. 白色污染 là ô nhiễm trắng, cách gọi rác nhựa, vì túi ni lông, hộp xốp ngày trước phần lớn màu trắng. 经久难愈 là lâu ngày khó khỏi, mẫu câu thứ ba.",
      "痛恨之余 là căm ghét đến mức, ngoài căm ghét ra còn…; mẫu 之余 là mẫu câu thứ tư. 给其贴上……的标签 là gán cho nó cái mác…, mẫu câu thứ năm. 又谈何容易 là đâu phải chuyện dễ, mẫu 谈何 là mẫu câu thứ sáu."]),
    ("国家发展改革委、生态环境部2020年1月19日公布《关于进一步加强塑料污染治理的意见》，到2020年底，我国将率先在部分地区、部分领域禁止、限制部分塑料制品的生产、销售和使用，",
     "Ngày 19 tháng 1 năm 2020, Ủy ban Cải cách và Phát triển Quốc gia cùng Bộ Sinh thái và Môi trường công bố “Ý kiến về việc tăng cường hơn nữa công tác xử lý ô nhiễm nhựa”: đến cuối năm 2020, nước ta sẽ đi đầu cấm, hạn chế việc sản xuất, bán và sử dụng một số sản phẩm nhựa ở một số khu vực, một số lĩnh vực,",
     ["国家发展改革委 là Ủy ban Cải cách và Phát triển Quốc gia, cơ quan thuộc Quốc vụ viện; 生态环境部 là Bộ Sinh thái và Môi trường. 意见 ở đây là một loại văn bản chính sách, ý kiến chỉ đạo. 塑料污染治理 là xử lý ô nhiễm nhựa.",
      "率先 là đi đầu. Từ 部分 lặp lại ba lần: 部分地区、部分领域、部分塑料制品, nhấn mạnh lệnh cấm được làm từng bước, chưa áp dụng toàn bộ. 禁止、限制 là cấm và hạn chế."],
     "国家发展改革委、生态环境部二零二零年一月十九日公布《关于进一步加强塑料污染治理的意见》，到二零二零年底，我国将率先在部分地区、部分领域禁止、限制部分塑料制品的生产、销售和使用，"),
    ("如：一次性塑料棉签、不可降解一次性塑料吸管、不可降解塑料袋等。相比旧版“限塑令”，本次“禁塑令”更具体、更直接地切入了人们的生活。\n虽然“禁塑令”在部分城市已先行执行，但效果并不理想。有媒体在政策已落地的广州市街头随机采访50位居民，居然有近6成完全不知道“禁塑令”。",
     "chẳng hạn: tăm bông thân nhựa dùng một lần, ống hút nhựa dùng một lần không phân hủy được, túi ni lông không phân hủy được, v.v. So với “lệnh hạn chế nhựa” bản cũ, “lệnh cấm nhựa” lần này cụ thể hơn, đi thẳng vào cuộc sống hơn. Tuy “lệnh cấm nhựa” đã được thực hiện trước ở một số thành phố, nhưng hiệu quả không được như mong đợi. Có cơ quan báo chí phỏng vấn ngẫu nhiên 50 người dân trên đường phố Quảng Châu, nơi chính sách đã được triển khai, vậy mà gần 6 phần 10 hoàn toàn không biết đến “lệnh cấm nhựa”.",
     ["一次性 là dùng một lần. 吸管 là ống hút. 相比旧版限塑令 là so với lệnh hạn chế nhựa bản cũ: lệnh năm 2008 chỉ buộc thu tiền túi ni lông, còn lệnh năm 2020 là cấm hẳn. 切入了人们的生活 là đi thẳng vào cuộc sống.",
      "先行执行 là thực hiện trước. 并不理想 là không được như mong đợi. 随机采访 là phỏng vấn ngẫu nhiên. 居然 là vậy mà, tỏ ý bất ngờ. 近六成 là gần sáu phần mười; 成 ở đây là một phần mười."],
     "如：一次性塑料棉签、不可降解一次性塑料吸管、不可降解塑料袋等。相比旧版限塑令，本次禁塑令更具体、更直接地切入了人们的生活。虽然禁塑令在部分城市已先行执行，但效果并不理想。有媒体在政策已落地的广州市街头随机采访五十位居民，居然有近六成完全不知道禁塑令。"),
    ("2008年的“限塑令”作为当年的社会热点曾广受关注，但在时间消磨下，此后竟成了“多加两毛买个袋子”的存在。此次政令再度升级，真的能减少塑料污染吗？",
     "“Lệnh hạn chế nhựa” năm 2008 từng là điểm nóng xã hội được quan tâm rộng rãi, nhưng dưới sự bào mòn của thời gian, về sau nó lại chỉ còn là chuyện “trả thêm hai hào mua cái túi”. Lần này chính lệnh lại được nâng cấp, liệu có thật sự giảm được ô nhiễm nhựa không?",
     ["作为当年的社会热点 là với tư cách điểm nóng xã hội năm ấy. 曾广受关注 là từng được quan tâm rộng rãi. 在时间消磨下 là dưới sự bào mòn của thời gian; ta lại gặp từ 消磨 của bài trước.",
      "竟成了……的存在 là vậy mà trở thành một thứ…, cách nói kiểu mạng. 两毛 là hai hào, tức hai mươi xu: mua túi chỉ mất hai hào nên ai cũng mua, lệnh hạn chế mất tác dụng. 再度升级 là lại được nâng cấp."],
     "二零零八年的限塑令作为当年的社会热点曾广受关注，但在时间消磨下，此后竟成了多加两毛买个袋子的存在。此次政令再度升级，真的能减少塑料污染吗？"),
    ("新版“限塑令”一发布，关于“禁止使用不可降解塑料”这一点，大部分人首先想到的是塑料替代品。其实市面上并不缺乏塑料替代品，但是谈及高昂的成本，人们望而却步。",
     "“Lệnh hạn chế nhựa” bản mới vừa công bố, về điểm “cấm sử dụng nhựa không phân hủy được”, phần lớn mọi người nghĩ ngay đến các sản phẩm thay thế nhựa. Thật ra trên thị trường không thiếu sản phẩm thay thế, nhưng hễ nhắc đến giá thành đắt đỏ là mọi người chùn bước.",
     ["一发布 là vừa công bố: mẫu 一 cộng động từ, nghĩa là hễ, vừa… thì…. 关于……这一点 là về điểm…. 替代品 là sản phẩm thay thế.",
      "市面上 là trên thị trường. 并不缺乏 là chẳng hề thiếu. 谈及 là nhắc đến, văn viết. 望而却步 là nhìn thấy đã chùn bước: túi phân hủy sinh học đắt gấp mấy lần túi thường."]),
    ("如果说替代品的核心在于减少污染，那么塑料回收，更应是我们关注的重点。联合国环境规划署（UNEP）2018年的一份报告称，全世界总计生产出的90亿吨塑料制品中，被循环利用的只有9%。",
     "Nếu nói cốt lõi của sản phẩm thay thế là giảm ô nhiễm, thì tái chế nhựa càng phải là trọng tâm mà chúng ta quan tâm. Một báo cáo năm 2018 của Chương trình Môi trường Liên Hợp Quốc (UNEP) cho biết, trong tổng cộng 9 tỷ tấn sản phẩm nhựa mà cả thế giới đã sản xuất ra, chỉ có 9% được tái chế.",
     ["如果说……那么…… là nếu nói… thì…, dùng để so sánh, đẩy ý lên cao hơn. 核心在于 là cốt lõi nằm ở. 回收 là thu hồi, tái chế. 更应是 là càng phải là.",
      "联合国环境规划署 là Chương trình Môi trường Liên Hợp Quốc. 报告称 là báo cáo cho biết; 称 là nói, văn viết. 循环利用 là tái chế, tái sử dụng. Con số chín phần trăm cho thấy tái chế mới là khâu yếu nhất."],
     "如果说替代品的核心在于减少污染，那么塑料回收，更应是我们关注的重点。联合国环境规划署二零一八年的一份报告称，全世界总计生产出的九十亿吨塑料制品中，被循环利用的只有百分之九。"),
    ("互联网带来的便利生活可以说是“限塑令”的最大敌人。别说超市购物、菜场买菜用几个塑料袋，就是每天中午一份外卖，回家网购些日常用品，随便拆拆快递，都是一堆塑料垃圾，而这些垃圾最终被草草地丢进垃圾箱，已成为我们生活的日常。",
     "Cuộc sống tiện lợi mà Internet mang lại có thể nói là kẻ thù lớn nhất của “lệnh hạn chế nhựa”. Chưa nói đến chuyện đi siêu thị, ra chợ mua rau dùng mấy chiếc túi ni lông, chỉ riêng mỗi trưa một suất đồ ăn mang về, về nhà mua vài món đồ dùng hằng ngày trên mạng, tiện tay bóc vài kiện hàng, đã là một đống rác nhựa; rồi đống rác ấy cuối cùng bị vứt vội vào thùng rác, chuyện này đã thành thường ngày trong cuộc sống của chúng ta.",
     ["可以说是 là có thể nói là. 别说……，就是……都…… là chưa nói đến…, ngay cả… cũng…, mẫu câu thứ bảy: chuyện lớn khỏi phải bàn, đến chuyện nhỏ cũng vậy. 外卖 là đồ ăn giao tận nơi. 网购 là mua hàng trên mạng.",
      "拆拆快递 là bóc mấy kiện hàng; động từ lặp lại chỉ hành động nhẹ nhàng, tùy tiện. 草草地丢进垃圾箱 là vứt vội vào thùng rác. 已成为我们生活的日常 là đã thành chuyện thường ngày."]),
    ("人们早已习惯了有塑料的便利生活，又怎么可能在一朝一夕就戒掉对塑料的“瘾”？重新塑造被塑料慢慢渗透的生活，只有从生活细节中入手，才有可能将塑料从我们的生活中剥离。",
     "Con người từ lâu đã quen với cuộc sống tiện lợi có nhựa, sao có thể cai “nghiện” nhựa trong một sớm một chiều? Muốn định hình lại cuộc sống đã bị nhựa dần dần len lỏi, chỉ có bắt đầu từ những chi tiết nhỏ trong đời sống, mới có thể tách nhựa ra khỏi cuộc sống của chúng ta.",
     ["又怎么可能 là làm sao có thể, câu phản vấn. 一朝一夕 là một sớm một chiều. 戒掉对塑料的瘾 là cai cơn nghiện nhựa: tác giả ví thói quen dùng nhựa như một cơn nghiện.",
      "重新塑造 là định hình lại; chữ đầu của 塑造 cũng là chữ đầu của 塑料, một cách chơi chữ thú vị. 只有……才…… là chỉ có… mới…. 从……入手 là bắt đầu từ…, mẫu câu thứ tám. 将……剥离 là tách cái gì ra."]),
    ("可喜的是，快递或者外卖行业的企业在“惯坏”我们的同时，也在借助一系列公益活动着手改善现状，增强环保意识。\n2019年8月，菜鸟携手通达、百世在浙江全面启动“回箱计划”，首批铺设1500个绿色回收箱，推进快递包装分类回收、二次利用，并宣布将在全国投放5万个绿色回收箱。",
     "Điều đáng mừng là, các doanh nghiệp chuyển phát và giao đồ ăn, trong khi “chiều hư” chúng ta, cũng đang nhờ vào một loạt hoạt động công ích để bắt tay cải thiện hiện trạng, nâng cao ý thức bảo vệ môi trường. Tháng 8 năm 2019, Cainiao bắt tay với Tongda và Best khởi động toàn diện “Kế hoạch thu hồi thùng” ở Chiết Giang, đợt đầu lắp đặt 1500 thùng thu hồi xanh, thúc đẩy phân loại thu hồi và tái sử dụng bao bì chuyển phát, đồng thời tuyên bố sẽ đặt 50 nghìn thùng thu hồi xanh trên toàn quốc.",
     ["可喜的是 là điều đáng mừng là: mẫu 可 cộng tính từ đơn âm tiết cộng 的是, mẫu câu thứ chín. 惯坏 là chiều hư: dịch vụ giao hàng tiện lợi khiến chúng ta quen dùng đồ nhựa. 借助 là nhờ vào. 着手改善现状 là bắt tay cải thiện hiện trạng.",
      "菜鸟 là Cainiao, mạng lưới logistics thuộc tập đoàn Alibaba; 通达 và 百世 là các công ty chuyển phát. 回箱计划 là kế hoạch thu hồi thùng các-tông. 首批铺设 là đợt đầu lắp đặt. 二次利用 là tái sử dụng. 投放 ở đây là đặt, đưa vào sử dụng."],
     "可喜的是，快递或者外卖行业的企业在惯坏我们的同时，也在借助一系列公益活动着手改善现状，增强环保意识。二零一九年八月，菜鸟携手通达、百世在浙江全面启动回箱计划，首批铺设一千五百个绿色回收箱，推进快递包装分类回收、二次利用，并宣布将在全国投放五万个绿色回收箱。"),
    ("参与环保公益活动并不只是外卖快递相关行业的责任，越来越多的企业和公益组织也在通过一系列的公益活动去填补人们塑料环保意识的缺失。\n互联网巨头腾讯虽然不是塑料垃圾的制造者，但在推动无塑化环保进程中也不遗余力。",
     "Tham gia các hoạt động công ích bảo vệ môi trường không chỉ là trách nhiệm của các ngành liên quan đến giao đồ ăn và chuyển phát; ngày càng nhiều doanh nghiệp và tổ chức công ích cũng đang thông qua một loạt hoạt động công ích để bù đắp sự thiếu hụt ý thức bảo vệ môi trường về nhựa của mọi người. Gã khổng lồ Internet Tencent tuy không phải là nhà sản xuất rác nhựa, nhưng cũng dốc hết sức thúc đẩy tiến trình bảo vệ môi trường không nhựa.",
     ["并不只是……的责任 là không chỉ là trách nhiệm của…. 公益组织 là tổ chức công ích, tổ chức phi lợi nhuận. 填补……的缺失 là bù đắp sự thiếu hụt; ta lại gặp từ 填补 của bài trước.",
      "腾讯 là Tencent; theo chú thích của sách, đây là một trong những công ty Internet lớn nhất Trung Quốc, sản phẩm nổi tiếng nhất là 微信, WeChat. 虽然……但…… là tuy… nhưng…. 不遗余力 là dốc hết sức."]),
    ("在国内最大的互联网公益平台“腾讯公益”，我们看到既有乡村源头垃圾减量的“原生态智慧减塑”计划，也有号召“减少一枚塑料袋，还给海洋生物一口深呼吸”的“助力无塑化环保计划”。",
     "Trên nền tảng công ích Internet lớn nhất trong nước, “Tencent Công ích”, chúng ta thấy vừa có kế hoạch “giảm nhựa thông minh, sinh thái tự nhiên” nhằm giảm rác ngay từ nguồn ở nông thôn, vừa có “Kế hoạch góp sức bảo vệ môi trường không nhựa” với lời kêu gọi “bớt một chiếc túi ni lông, trả lại cho sinh vật biển một hơi thở sâu”.",
     ["既有……也有…… là vừa có… vừa có…. 乡村源头垃圾减量 là giảm lượng rác từ nguồn ở nông thôn. 原生态智慧减塑 là giảm nhựa một cách thông minh, theo hướng giữ gìn sinh thái tự nhiên.",
      "号召 là kêu gọi. 减少一枚塑料袋，还给海洋生物一口深呼吸 là một khẩu hiệu rất giàu hình ảnh: rác nhựa trên biển làm sinh vật biển ngạt thở. Chú ý lượng từ 枚 dùng cho vật nhỏ; còn 还给 nghĩa là trả lại."]),
    ("在这些线上线下联动的公益活动中，更令人欣慰的是越来越多的孩子参与其中，无塑化环保理念开始植入孩子的成长过程，并成为孩子们生活的一部分。",
     "Trong các hoạt động công ích kết hợp trực tuyến và trực tiếp này, điều đáng mừng hơn là ngày càng nhiều trẻ em tham gia; ý thức bảo vệ môi trường không nhựa bắt đầu được gieo vào quá trình trưởng thành của các em, và trở thành một phần cuộc sống của các em.",
     ["线上线下联动 là kết hợp trực tuyến và trực tiếp. 更令人欣慰的是 là điều khiến người ta vui mừng hơn là. 参与其中 là tham gia vào đó.",
      "植入孩子的成长过程 là gieo vào quá trình trưởng thành của trẻ. Giống bài trước, khi trẻ em có ý thức, các em sẽ tác động ngược lại cha mẹ, giúp lối sống xanh bén rễ trong gia đình."]),
    ("无论此次“限塑令”能否真正推动“无塑化”生活的实现，面对我们赖以生存的地球，尽可能地通过生活的点点滴滴，从自身做起并带动身边的人去改变，这才是正确的“无塑化”之路。",
     "Bất kể lần này “lệnh hạn chế nhựa” có thật sự thúc đẩy được cuộc sống “không nhựa” thành hiện thực hay không, trước trái đất mà chúng ta dựa vào để sinh tồn, hãy cố gắng hết mức thông qua từng việc nhỏ trong cuộc sống, bắt đầu từ chính mình và kéo theo những người xung quanh cùng thay đổi, đó mới là con đường “không nhựa” đúng đắn.",
     ["无论……能否…… là bất kể có… hay không. 面对 là đối mặt, đứng trước. 赖以生存的地球 là trái đất mà ta dựa vào để sinh tồn. 尽可能地 là cố gắng hết mức có thể.",
      "通过生活的点点滴滴 là qua từng việc nhỏ trong đời sống. 从自身做起 là bắt đầu từ chính mình. 带动身边的人 là kéo theo người xung quanh. 这才是……之路 là đó mới là con đường…."]),
    ("塑战，无法速决，但“环保从个人做起”的理念正在深入人心，只有这样才能将“塑战”进行到底。",
     "Cuộc chiến với nhựa không thể thắng nhanh, nhưng ý tưởng “bảo vệ môi trường bắt đầu từ mỗi người” đang đi sâu vào lòng người, chỉ có như vậy mới có thể tiến hành “cuộc chiến nhựa” đến cùng.",
     ["塑战 là cuộc chiến với nhựa, ghép từ 塑料 và 战, theo lối chơi chữ. 无法速决 là không thể đánh nhanh thắng nhanh: câu trả lời trực tiếp cho câu hỏi ở tên bài. Các bạn còn nhớ từ 持久战 của bài trước chứ? Cuộc chiến nhựa cũng là một cuộc chiến trường kỳ.",
      "深入人心 là đi sâu vào lòng người. 将……进行到底 là tiến hành… đến cùng, mẫu câu thứ mười. Bài kết thúc bằng một thông điệp rõ ràng: không thể thắng nhanh, nên phải kiên trì, bắt đầu từ mỗi người."]),
]
# tiểu mục trong bài khóa (số đoạn: tên tiểu mục, nghĩa)
SUB = {3: ("“限塑”升级为“禁塑”", "限塑升级为禁塑", "Từ hạn chế nhựa nâng cấp thành cấm nhựa"),
       6: ("“无塑化”前路漫漫", "无塑化前路漫漫", "Con đường không nhựa còn dài dằng dặc"),
       10: ("公益，助力“无塑化”生活", "公益，助力无塑化生活", "Công ích, góp sức cho cuộc sống không nhựa")}

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa “塑战”能否速决？", size=40,
    items=["Bài báo mạng, chia 3 tiểu mục: “限塑”升级为“禁塑” · “无塑化”前路漫漫 · 公益，助力“无塑化”生活",
           "Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa. Bài được cải biên từ một bài báo trên trang tin 网易新闻, NetEase News, có tiêu đề: 最严限塑令倒计时，你离奶茶外卖涨价还有多远, lệnh hạn chế nhựa nghiêm nhất đang đếm ngược, bạn còn cách ngày trà sữa mang về tăng giá bao xa?",
         F(0, "Sau phần mở đầu, bài chia làm ba tiểu mục: 限塑升级为禁塑, từ hạn chế nhựa nâng cấp thành cấm nhựa; 无塑化前路漫漫, con đường không nhựa còn dài; và 公益，助力无塑化生活, công ích góp sức cho cuộc sống không nhựa."),
         F(1, "Thầy chia bài thành mười lăm đoạn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(2, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(3, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

ZS = {4: 44, 10: 44}  # cỡ chữ riêng cho đoạn dài hơn khung
for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    n = len(zh)
    zsize = ZS.get(i) or (54 if n <= 100 else 50 if n <= 125 else 46)
    title = f"Bài khóa – đoạn {i}/{len(P)}"
    intro = []
    if i in SUB:
        shown, read, mean = SUB[i]
        title += f" · {shown}"
        intro = [F(0, f"Tiểu mục mới: {read}。 Nghĩa là: {mean}.", cap=f"Tiểu mục mới: {shown} – {mean}")]
    add("passage", section="Bài khóa 课文", title=title, zh=zh, vi=vi, zsize=zsize,
        say=intro + [F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
                     F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Bố cục & hiểu bài", section="Bài khóa 课文", title="Bố cục bài khóa", size=34,
    items=["## Mở đầu (đoạn 1–2): 塑料 – phát minh vĩ đại & “双刃剑” → 白色污染 · “无塑化”生活又谈何容易？",
           "## “限塑”升级为“禁塑” (đoạn 3–5)",
           "禁塑令 2020 cụ thể hơn · nhưng gần 6/10 người dân Quảng Châu không biết · 限塑令 2008 → “多加两毛买个袋子”",
           "## “无塑化”前路漫漫 (đoạn 6–9): 替代品成本高 · 回收只有9% · 外卖、网购、快递 · 戒“瘾”不能一朝一夕",
           "## 公益，助力“无塑化”生活 (đoạn 10–13): 回箱计划 · 腾讯公益 · 孩子参与",
           "## Kết luận (đoạn 14–15): 从自身做起 · 塑战无法速决 → 进行到底"],
    say=["Trước khi sang phần ngữ pháp, chúng ta cùng nhìn lại bố cục của bài khóa.",
         F(0, "Phần mở đầu, đoạn một và hai: nhựa là phát minh vĩ đại, nhưng khoa học kỹ thuật là con dao hai lưỡi; túi ni lông gây ra ô nhiễm trắng. Sống không nhựa đâu phải chuyện dễ."),
         F(1, "Tiểu mục một, đoạn ba đến năm: từ hạn chế nhựa đến cấm nhựa."),
         F(2, "Lệnh cấm năm 2020 cụ thể hơn, nhưng ở Quảng Châu gần sáu phần mười người được hỏi không hề biết đến nó; còn lệnh hạn chế năm 2008 thì dần dần chỉ còn là chuyện trả thêm hai hào mua cái túi."),
         F(3, "Tiểu mục hai, đoạn sáu đến chín: con đường không nhựa còn dài. Sản phẩm thay thế đắt; chỉ chín phần trăm nhựa được tái chế; đồ ăn mang về, mua sắm trên mạng, chuyển phát tạo ra cả đống rác nhựa; và cơn nghiện nhựa không thể cai trong một sớm một chiều."),
         F(4, "Tiểu mục ba, đoạn mười đến mười ba: các doanh nghiệp chuyển phát, tập đoàn Internet và tổ chức công ích chung tay, và đáng mừng là ngày càng nhiều trẻ em tham gia."),
         F(5, "Kết luận, đoạn mười bốn và mười lăm: bắt đầu từ chính mình; cuộc chiến nhựa không thể thắng nhanh, nhưng phải tiến hành đến cùng.")])

add("bullets", section="Bài khóa 课文", title="Kiểm tra hiểu bài", reveal=True, size=32,
    items=["(1) 为什么说科学技术是一把“双刃剑”？",
           "Đáp án: 塑料袋在给人类生活带来极大便利的同时，也给地球带来了白色污染的顽疾。",
           "(2) 2008年的“限塑令”后来效果怎么样？",
           "Đáp án: 在时间消磨下，此后竟成了“多加两毛买个袋子”的存在。",
           "(3) 为什么说互联网带来的便利生活是“限塑令”的最大敌人？",
           "Đáp án: 外卖、网购、快递都会产生一堆塑料垃圾，而这些垃圾最终被草草地丢进垃圾箱。",
           "(4) 作者认为正确的“无塑化”之路是什么？",
           "Đáp án: 尽可能地通过生活的点点滴滴，从自身做起并带动身边的人去改变。"],
    say=["Bây giờ chúng ta kiểm tra xem mình đã hiểu bài chưa. Các bạn nghe câu hỏi, tạm dừng để trả lời, rồi nghe đáp án nhé.",
         F(0, "Câu một: 为什么说科学技术是一把双刃剑？ Vì sao nói khoa học kỹ thuật là con dao hai lưỡi?"),
         F(1, "Đáp án: 塑料袋在给人类生活带来极大便利的同时，也给地球带来了白色污染的顽疾。 Túi ni lông vừa mang lại tiện lợi to lớn, vừa mang đến căn bệnh nan y ô nhiễm trắng."),
         F(2, "Câu hai: 二零零八年的限塑令后来效果怎么样？ Lệnh hạn chế nhựa năm 2008 về sau hiệu quả ra sao?"),
         F(3, "Đáp án: 在时间消磨下，此后竟成了多加两毛买个袋子的存在。 Thời gian bào mòn, nó chỉ còn là chuyện trả thêm hai hào mua cái túi."),
         F(4, "Câu ba: 为什么说互联网带来的便利生活是限塑令的最大敌人？ Vì sao nói cuộc sống tiện lợi do Internet mang lại là kẻ thù lớn nhất của lệnh hạn chế nhựa?"),
         F(5, "Đáp án: 外卖、网购、快递都会产生一堆塑料垃圾，而这些垃圾最终被草草地丢进垃圾箱。 Đồ ăn mang về, mua sắm trên mạng, chuyển phát đều tạo ra cả đống rác nhựa, và rác ấy cuối cùng bị vứt vội vào thùng."),
         F(6, "Câu bốn: 作者认为正确的无塑化之路是什么？ Theo tác giả, con đường không nhựa đúng đắn là gì?"),
         F(7, "Đáp án: 尽可能地通过生活的点点滴滴，从自身做起并带动身边的人去改变。 Cố gắng hết mức qua từng việc nhỏ trong cuộc sống, bắt đầu từ chính mình và kéo theo người xung quanh cùng thay đổi.")])

# ======================= MẪU CÂU =======================
add("bullets", chapter="Mẫu câu: 被誉为 · 扮演角色 · 经久 · 之余", section="Mẫu câu 重点句型", title="1. ……被誉为…… · 2. 扮演……的角色", size=32,
    items=["## 1. 被誉为 – được ca ngợi là, được mệnh danh là (văn viết, khen ngợi)",
           "塑料被誉为人类最伟大的发明之一。",
           "教师被誉为塑造人类灵魂的工程师。 · 这座城市的植被覆盖率已经达到80%，被誉为天然氧吧。",
           "## 2. 扮演……的角色 – đóng vai trò… (thường có 重要 / 举足轻重 / 关键)",
           "塑料在当今人类文明的进程中扮演着举足轻重的角色。",
           "无论哪个年代，知识分子总是在社会变革中扮演着至关重要的角色。 · 我不需要任何人在我生活中扮演救世主的角色。"],
    say=["Bây giờ chúng ta sang phần mẫu câu trọng điểm. Bài này có mười mẫu, thầy ghép thành từng cặp cho dễ nhớ.",
         F(0, "Mẫu thứ nhất: 被誉为, được ca ngợi là, được mệnh danh là. Đây là cách nói văn viết, mang sắc thái khen ngợi; phía sau thường là một danh hiệu, một cách gọi đẹp."),
         F(1, "Ví dụ từ bài khóa: 塑料被誉为人类最伟大的发明之一。 Nhựa được ca ngợi là một trong những phát minh vĩ đại nhất của loài người."),
         F(2, "Ví dụ khác: 教师被誉为塑造人类灵魂的工程师。 Giáo viên được mệnh danh là kỹ sư tâm hồn của loài người. Và: 这座城市的植被覆盖率已经达到百分之八十，被誉为天然氧吧。 Tỷ lệ che phủ thực vật của thành phố này đã đạt tám mươi phần trăm, được mệnh danh là quán ô xy tự nhiên."),
         F(3, "Mẫu thứ hai: 扮演什么的角色, đóng vai trò gì. 扮演 nghĩa gốc là đóng vai trên sân khấu; trước 角色 thường có tính từ như 重要，举足轻重，关键."),
         F(4, "Ví dụ từ bài khóa: 塑料在当今人类文明的进程中扮演着举足轻重的角色。 Nhựa đóng vai trò cực kỳ quan trọng trong tiến trình văn minh nhân loại ngày nay."),
         F(5, "Ví dụ khác: 无论哪个年代，知识分子总是在社会变革中扮演着至关重要的角色。 Dù ở thời đại nào, trí thức luôn đóng vai trò hết sức quan trọng trong biến đổi xã hội. Và: 我不需要任何人在我生活中扮演救世主的角色。 Tôi không cần ai đóng vai cứu tinh trong cuộc đời tôi.")])

add("bullets", section="Mẫu câu 重点句型", title="3. 经久 + 难 / 不 + V. · 4. （在）……之余", size=32,
    items=["## 3. 经久难愈 / 经久难忘 / 经久不衰 / 经久不息 – trải qua thời gian dài mà vẫn…",
           "……也给我们的地球带来了白色污染的顽疾，经久难愈。",
           "爱情片是影视业中最经久不衰的类型之一。 · 王教授的演讲太精彩了，会场上掌声经久不息。",
           "## 4. （在）……之余 – ngoài…, sau khi / trong lúc…",
           "一家英国媒体痛恨之余，甚至给其贴上“人类最糟糕的发明”的标签。",
           "在学习之余，多关心一下周围充满活力的人和物…… · 临近毕业，大家兴奋之余，憧憬着将来美好的生活。"],
    say=["Mẫu thứ ba: 经久 cộng 难 hoặc 不, cộng động từ.",
         F(0, "经久 là trải qua thời gian dài. Mẫu này nghĩa là dù trải qua thời gian dài, vẫn khó hoặc không thay đổi. Hay gặp: 经久难愈, lâu ngày khó khỏi; 经久难忘, mãi khó quên; 经久不衰, bền bỉ không suy tàn; 经久不息, kéo dài không dứt."),
         F(1, "Ví dụ từ bài khóa: 也给我们的地球带来了白色污染的顽疾，经久难愈。 Mang đến cho trái đất căn bệnh nan y ô nhiễm trắng, lâu ngày khó khỏi."),
         F(2, "Ví dụ khác: 爱情片是影视业中最经久不衰的类型之一。 Phim tình cảm là một trong những thể loại bền bỉ nhất của ngành điện ảnh. Và: 王教授的演讲太精彩了，会场上掌声经久不息。 Bài diễn thuyết của giáo sư Vương quá hay, tiếng vỗ tay trong hội trường kéo dài không dứt."),
         F(3, "Mẫu thứ tư: 在什么之余, có thể bỏ 在. 之余 nghĩa là ngoài việc chính ra, hoặc sau khi, trong lúc một trạng thái nào đó. Phía trước có thể là động từ chỉ việc chính như 学习，工作, hoặc chỉ cảm xúc như 兴奋，痛恨."),
         F(4, "Ví dụ từ bài khóa: 一家英国媒体痛恨之余，甚至给其贴上人类最糟糕的发明的标签。 Một tờ báo Anh căm ghét đến mức gán cho nó cái mác phát minh tồi tệ nhất."),
         F(5, "Ví dụ khác: 在学习之余，多关心一下周围充满活力的人和物。 Ngoài giờ học, hãy quan tâm nhiều hơn đến những con người và sự vật đầy sức sống xung quanh. Và: 临近毕业，大家兴奋之余，憧憬着将来美好的生活。 Sắp tốt nghiệp, mọi người vừa phấn khởi vừa mơ về cuộc sống tươi đẹp tương lai.")])

add("bullets", chapter="Mẫu câu: 贴标签 · 谈何 · 别说……就是……", section="Mẫu câu 重点句型", title="5. 给……贴上……标签 · 6. 谈何 + Adj / N / V", size=32,
    items=["## 5. 给……贴上……（的）标签 / 被贴上……（的）标签 – gán cho ai cái mác…",
           "甚至给其贴上“人类最糟糕的发明”的标签。",
           "给所有网红贴上恶俗的标签，这样真的公平吗？ · 朋友圈“屏蔽父母”的年轻人不能被简单地贴上不孝的标签。",
           "## 6. 谈何…… – nói gì đến…, đâu dễ… (phản vấn: không thể)",
           "我们深知白色污染的恐怖，但是“无塑化”生活又谈何容易？",
           "我目前养活自己都很困难，没有稳固的经济基础，谈何婚姻？"],
    say=["Mẫu thứ năm: 给ai贴上什么的标签, gán cho ai cái mác gì; dạng bị động là 被贴上什么的标签.",
         F(0, "Mẫu này thường mang ý phê phán: đánh giá ai đó một cách đơn giản, phiến diện, như dán một cái nhãn lên người họ."),
         F(1, "Ví dụ từ bài khóa: 甚至给其贴上人类最糟糕的发明的标签。 Thậm chí gán cho nó cái mác phát minh tồi tệ nhất của loài người."),
         F(2, "Ví dụ khác: 给所有网红贴上恶俗的标签，这样真的公平吗？ Gán cho tất cả người nổi tiếng trên mạng cái mác dung tục, như vậy có thật công bằng không? Và: 朋友圈屏蔽父母的年轻人不能被简单地贴上不孝的标签。 Những người trẻ chặn bố mẹ xem trang cá nhân không thể bị gán đơn giản cái mác bất hiếu."),
         F(3, "Mẫu thứ sáu: 谈何 cộng tính từ, danh từ hoặc động từ. 谈何 là nói gì đến, dùng trong câu phản vấn, ý là không thể, rất khó. Cụm quen thuộc nhất là 谈何容易."),
         F(4, "Ví dụ từ bài khóa: 我们深知白色污染的恐怖，但是无塑化生活又谈何容易？ Chúng ta hiểu rõ sự đáng sợ của ô nhiễm trắng, nhưng sống không nhựa đâu phải chuyện dễ?"),
         F(5, "Ví dụ khác: 我目前养活自己都很困难，没有稳固的经济基础，谈何婚姻？ Hiện giờ tự nuôi mình tôi còn khó, không có nền tảng kinh tế vững chắc, nói gì đến chuyện kết hôn? Ngoài ra, sách còn có ví dụ: 如果连分数运算都不会，还谈何理解当今物理学研究的前沿动向呢？ Nếu ngay cả phép tính phân số cũng không biết, thì nói gì đến hiểu xu hướng nghiên cứu mới nhất của vật lý?")])

add("bullets", section="Mẫu câu 重点句型", title="7. 别说……，……就（是 / 更）…… – chưa nói đến…, ngay cả… cũng…", size=33,
    items=["Vế 别说 nêu trường hợp dễ thấy (hiển nhiên); vế 就是 nêu trường hợp đặc biệt hơn → nhấn mạnh mức độ",
           "别说超市购物、菜场买菜用几个塑料袋，就是每天中午一份外卖，回家网购些日常用品，随便拆拆快递，都是一堆塑料垃圾。",
           "别说儿童了，就是成年人都不一定明白这个道理。",
           "别说考高分了，他就是考及格都不一定做得到。"],
    say=["Mẫu thứ bảy: 别说 vế trước, 就是 vế sau, thường có 都 hoặc 也.",
         F(0, "Vế có 别说 nêu một trường hợp mà ai cũng thấy là đương nhiên; vế có 就是 nêu một trường hợp đặc biệt hơn, nhẹ hơn hoặc nặng hơn, để nhấn mạnh mức độ. Tiếng Việt dịch là chưa nói đến…, ngay cả… cũng…. Cẩn thận: thứ tự hai vế tùy theo logic. Ở bài khóa, vế sau là chuyện tưởng nhỏ mà vẫn tạo ra rác."),
         F(1, "Ví dụ từ bài khóa: 别说超市购物、菜场买菜用几个塑料袋，就是每天中午一份外卖，回家网购些日常用品，随便拆拆快递，都是一堆塑料垃圾。 Chưa nói đến đi siêu thị, ra chợ dùng mấy chiếc túi, ngay cả một suất đồ ăn trưa, vài món hàng mua trên mạng, mấy kiện hàng bóc ra, cũng đã là một đống rác nhựa."),
         F(2, "Ví dụ hai: 别说儿童了，就是成年人都不一定明白这个道理。 Chưa nói đến trẻ con, ngay cả người lớn cũng chưa chắc hiểu được đạo lý này. Trẻ con không hiểu là đương nhiên; người lớn không hiểu mới đáng nói."),
         F(3, "Ví dụ ba: 别说考高分了，他就是考及格都不一定做得到。 Đừng nói đến điểm cao, ngay cả thi đỗ anh ta cũng chưa chắc làm được.")])

add("bullets", chapter="Mẫu câu: 入手 · 可喜的是 · 进行到底", section="Mẫu câu 重点句型", title="8. 从……入手 · 9. 可 + Adj. / V.（单音节）的是", size=32,
    items=["## 8. 从……入手 – bắt đầu từ…, bắt tay từ…",
           "只有从生活细节中入手，才有可能将塑料从我们的生活中剥离。",
           "若想在工作中取得成绩，就要从大处着眼，从小处入手，从点滴做起。",
           "## 9. 可喜 / 可悲 / 可叹 / 可惜的是…… – điều đáng mừng / đáng buồn / đáng than là…",
           "可喜的是，快递或者外卖行业的企业在“惯坏”我们的同时，也在借助一系列公益活动着手改善现状……",
           "每个人出生的时候都是“原创”的，可悲的是，很多人却渐渐变成了“盗版”。"],
    say=["Mẫu thứ tám: 从什么入手, bắt đầu từ đâu.",
         F(0, "Mẫu này chỉ điểm xuất phát khi giải quyết một vấn đề, một công việc. Giống 从什么着手, 从什么做起."),
         F(1, "Ví dụ từ bài khóa: 只有从生活细节中入手，才有可能将塑料从我们的生活中剥离。 Chỉ có bắt đầu từ những chi tiết đời sống, mới có thể tách nhựa ra khỏi cuộc sống."),
         F(2, "Ví dụ khác: 若想在工作中取得成绩，就要从大处着眼，从小处入手，从点滴做起。 Muốn đạt thành tích trong công việc, phải nhìn từ cái lớn, bắt tay từ cái nhỏ, làm từ từng việc nhỏ. 从大处着眼，从小处入手 là một cặp câu đối rất hay dùng."),
         F(3, "Mẫu thứ chín: 可 cộng tính từ hoặc động từ, thường là một âm tiết, cộng 的是. Ví dụ 可喜的是, điều đáng mừng là; 可悲的是, điều đáng buồn là; 可叹的是, điều đáng than là; 可惜的是, điều đáng tiếc là. Mẫu này đứng đầu câu, nêu thái độ của người nói trước khi kể sự việc."),
         F(4, "Ví dụ từ bài khóa: 可喜的是，快递或者外卖行业的企业在惯坏我们的同时，也在借助一系列公益活动着手改善现状。 Điều đáng mừng là các doanh nghiệp chuyển phát, giao đồ ăn, trong khi chiều hư chúng ta, cũng đang bắt tay cải thiện hiện trạng."),
         F(5, "Ví dụ khác: 每个人出生的时候都是原创的，可悲的是，很多人却渐渐变成了盗版。 Mỗi người khi sinh ra đều là bản gốc, đáng buồn là nhiều người lại dần dần biến thành bản sao. Và: 爱应该是相互的，然而可叹的是，你最爱的人往往是伤害你最深的人。 Tình yêu lẽ ra phải từ hai phía, nhưng đáng than thay, người bạn yêu nhất thường lại là người làm bạn tổn thương sâu nhất.")])

add("bullets", section="Mẫu câu 重点句型", title="10. 将 / 把……进行到底 – tiến hành… đến cùng", size=34,
    items=["Quyết tâm làm một việc đến cùng, không bỏ dở; giọng khẩu hiệu, mạnh mẽ",
           "但“环保从个人做起”的理念正在深入人心，只有这样才能将“塑战”进行到底。",
           "我们应该继往开来，把改革开放的伟大事业进行到底。",
           "希望你们用心去爱，去创造幸福的每一天，不离不弃将爱情进行到底。"],
    say=["Mẫu thứ mười: 将什么进行到底, hoặc 把什么进行到底.",
         F(0, "Mẫu này biểu thị quyết tâm làm một việc đến cùng, không bỏ dở giữa chừng. Giọng điệu mạnh mẽ, thường gặp trong khẩu hiệu, diễn văn, lời chúc."),
         F(1, "Ví dụ từ bài khóa: 但环保从个人做起的理念正在深入人心，只有这样才能将塑战进行到底。 Ý tưởng bảo vệ môi trường từ mỗi người đang đi sâu vào lòng người, chỉ có như vậy mới tiến hành được cuộc chiến nhựa đến cùng."),
         F(2, "Ví dụ hai: 我们应该继往开来，把改革开放的伟大事业进行到底。 Chúng ta nên kế thừa quá khứ, mở đường tương lai, tiến hành sự nghiệp cải cách mở cửa vĩ đại đến cùng."),
         F(3, "Ví dụ ba, một lời chúc đám cưới: 希望你们用心去爱，去创造幸福的每一天，不离不弃将爱情进行到底。 Mong hai bạn yêu nhau bằng cả trái tim, tạo nên mỗi ngày hạnh phúc, không rời không bỏ, đưa tình yêu đi đến cùng.")])

# ======================= KẾT HỢP TỪ =======================
add("bullets", chapter="Kết hợp từ", section="Kết hợp từ 词语搭配", title="Kết hợp từ (1): 渗透 · 切入 · 先行", size=33,
    items=["## 渗透：意识～ · 思想～ · 汗水～",
           "人们能够抵御武装的入侵，却阻挡不住思想的渗透。",
           "## 切入：～主题 · ～问题 · ～点",
           "本文将以人口结构及妇女生活空间为切入点，阐述古代女性面临的多重压力。",
           "## 先行：～一步 · ～离开 · ～者",
           "在推动环保政策的落实方面，这座城市先行一步，加大对绿色能源的资金投入。"],
    say=["Tiếp theo là phần kết hợp từ, 词语搭配.",
         F(0, "渗透 đi với 意识，思想，汗水: ý thức thâm nhập, tư tưởng thâm nhập, mồ hôi thấm ướt."),
         F(1, "Ví dụ: 人们能够抵御武装的入侵，却阻挡不住思想的渗透。 Người ta có thể chống lại cuộc xâm lược bằng vũ trang, nhưng không ngăn được sự thâm nhập của tư tưởng."),
         F(2, "切入 đi với 主题，问题, và 切入点: đi vào chủ đề, đi vào vấn đề, điểm tiếp cận."),
         F(3, "Ví dụ: 本文将以人口结构及妇女生活空间为切入点，阐述古代女性面临的多重压力。 Bài viết này lấy cơ cấu dân số và không gian sống của phụ nữ làm điểm tiếp cận, trình bày những áp lực chồng chất mà phụ nữ thời xưa phải đối mặt."),
         F(4, "先行 đi với 一步，离开, và 先行者: đi trước một bước, rời đi trước, người đi tiên phong."),
         F(5, "Ví dụ: 在推动环保政策的落实方面，这座城市先行一步，加大对绿色能源的资金投入。 Trong việc thúc đẩy thực hiện chính sách môi trường, thành phố này đi trước một bước, tăng vốn đầu tư cho năng lượng xanh.")])

add("bullets", section="Kết hợp từ 词语搭配", title="Kết hợp từ (2): 随机 · 瘾 · 植入", size=33,
    items=["## 随机：～调查 · ～抽样 · ～性",
           "本报随机调查了200名市民，涉及职业有公务员、公司经理、会计、教师……",
           "## 瘾：戒～ · 上～ · 成～ · 过～",
           "终于来到了演唱会现场，整整三个小时的表演让我们过足了瘾。",
           "## 植入：～广告 · ～脑海 · ～心底",
           "虽然我们只是短短相处了一周，但那一段快乐的回忆深深地植入了我的脑海。"],
    say=[F(0, "随机 đi với 调查，抽样, và 随机性: điều tra ngẫu nhiên, lấy mẫu ngẫu nhiên, tính ngẫu nhiên."),
         F(1, "Ví dụ: 本报随机调查了二百名市民，涉及职业有公务员、公司经理、会计、教师、出租车司机、个体经营者等。 Báo chúng tôi đã điều tra ngẫu nhiên hai trăm người dân, gồm các nghề công chức, giám đốc công ty, kế toán, giáo viên, tài xế taxi, chủ hộ kinh doanh."),
         F(2, "瘾 đi với 戒，上，成，过: cai nghiện, bị nghiện, thành nghiện, và 过瘾, đã đời, thỏa thích."),
         F(3, "Ví dụ: 终于来到了演唱会现场，整整三个小时的表演让我们过足了瘾。 Cuối cùng cũng đến được buổi hòa nhạc, ba tiếng đồng hồ biểu diễn khiến chúng tôi được thỏa thích. Sách còn có ví dụ 网络成瘾, nghiện mạng."),
         F(4, "植入 đi với 广告，脑海，心底: quảng cáo lồng ghép, khắc sâu vào tâm trí, in sâu vào đáy lòng."),
         F(5, "Ví dụ: 虽然我们只是短短相处了一周，但那一段快乐的回忆深深地植入了我的脑海，再也无法忘怀。 Tuy chúng tôi chỉ ở bên nhau ngắn ngủi một tuần, nhưng kỷ niệm vui vẻ ấy đã khắc sâu vào tâm trí tôi, không bao giờ quên được.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 课后练习", title="Bài tập 1: Chọn thành ngữ điền vào chỗ trống (1)", reveal=True, size=33,
    items=["## 深入人心 · 不遗余力 · 一朝一夕 · 泛滥成灾 · 点点滴滴 · 望而却步 · 举足轻重 · 谈何容易",
           "(1) 幸福在我们每个人的身边，只要用心感受，身边的___都是幸福！",
           "Đáp án: 点点滴滴",
           "(2) 如今，“科学技术是第一生产力”这种思想早已___。",
           "Đáp án: 深入人心",
           "(3) 陈教授是学术界德高望重的老教授，他的看法在学术界___。",
           "Đáp án: 举足轻重",
           "(4) 事业的成功，并非___所能达成，而是长期努力的结果。",
           "Đáp án: 一朝一夕"],
    say=["Bây giờ chúng ta sang phần luyện tập của sách. Bài tập một: chọn từ điền vào chỗ trống. Cả tám từ đều là thành ngữ: 深入人心，不遗余力，一朝一夕，泛滥成灾，点点滴滴，望而却步，举足轻重，谈何容易.",
         F(1, "Câu một: 幸福在我们每个人的身边，只要用心感受，身边的什么都是幸福！ Hạnh phúc ở ngay bên mỗi người, chỉ cần dùng trái tim cảm nhận, những gì bên cạnh đều là hạnh phúc. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 点点滴滴. 身边的点点滴滴都是幸福, từng điều nhỏ nhặt bên cạnh đều là hạnh phúc."),
         F(3, "Câu hai: 如今，科学技术是第一生产力这种思想早已什么。 Ngày nay, tư tưởng khoa học kỹ thuật là lực lượng sản xuất hàng đầu từ lâu đã làm sao."),
         F(4, "Đáp án: 深入人心, đã đi sâu vào lòng người."),
         F(5, "Câu ba: 陈教授是学术界德高望重的老教授，他的看法在学术界什么。 Giáo sư Trần là bậc lão thành đức cao vọng trọng, quan điểm của ông trong giới học thuật thế nào."),
         F(6, "Đáp án: 举足轻重, có sức nặng, cực kỳ quan trọng."),
         F(7, "Câu bốn: 事业的成功，并非什么所能达成，而是长期努力的结果。 Thành công trong sự nghiệp không phải đạt được trong khoảng thời gian nào, mà là kết quả của sự nỗ lực lâu dài."),
         F(8, "Đáp án: 一朝一夕. Các bạn để ý mẫu 并非……而是…… của bài trước.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 1: Chọn thành ngữ điền vào chỗ trống (2)", reveal=True, size=33,
    items=["(5) 这位老师一直对年轻人关爱有加，___地帮助他们走向成功。",
           "Đáp án: 不遗余力",
           "(6) 20世纪80年代，该物种作为食物引入我国广东等地，没想到现已在广东、广西、浙江等地___。",
           "Đáp án: 泛滥成灾",
           "(7) 别看师傅做起来很顺手，要练到这样的手艺___。",
           "Đáp án: 谈何容易",
           "(8) 从前电脑是让普通百姓___的贵重商品，如今很多家庭都配备了电脑，它改变了人们的生活。",
           "Đáp án: 望而却步"],
    say=[F(0, "Câu năm: 这位老师一直对年轻人关爱有加，什么地帮助他们走向成功。 Thầy giáo này luôn hết mực quan tâm đến người trẻ, giúp họ đi đến thành công một cách thế nào."),
         F(1, "Đáp án: 不遗余力地帮助, dốc hết sức giúp đỡ."),
         F(2, "Câu sáu: 二十世纪八十年代，该物种作为食物引入我国广东等地，没想到现已在广东、广西、浙江等地什么。 Những năm tám mươi của thế kỷ hai mươi, loài này được du nhập vào Quảng Đông làm thực phẩm, không ngờ nay ở Quảng Đông, Quảng Tây, Chiết Giang đã thế nào."),
         F(3, "Đáp án: 泛滥成灾, sinh sôi tràn lan thành thảm họa. Đây có lẽ là ốc bươu vàng, một loài gây hại mà nông dân Việt Nam cũng rất quen thuộc."),
         F(4, "Câu bảy: 别看师傅做起来很顺手，要练到这样的手艺什么。 Đừng thấy bác thợ làm thuận tay thế, muốn luyện được tay nghề như vậy thì thế nào."),
         F(5, "Đáp án: 谈何容易, đâu phải chuyện dễ."),
         F(6, "Câu tám: 从前电脑是让普通百姓什么的贵重商品，如今很多家庭都配备了电脑，它改变了人们的生活。 Trước đây máy tính là món hàng đắt tiền khiến người dân bình thường làm sao, nay nhiều gia đình đã có máy tính."),
         F(7, "Đáp án: 望而却步, nhìn thấy đã chùn bước vì giá quá đắt.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn đáp án đúng", reveal=True, size=33,
    items=["(1) 第一道安检处设在园区内，这里安检员会（ ）对一些游客进行检查。 A.随意 B.随便 C.随机 D.随处",
           "Đáp án: C. 随机 – kiểm tra ngẫu nhiên",
           "(2) 他没有放弃，一直坚持到最后，这一点让父亲很（ ）。 A.欣慰 B.欣喜 C.安慰 D.抚慰",
           "Đáp án: A. 欣慰 – 让人很欣慰 (khiến người ta vui lòng)",
           "(3) 这篇论文从乡村生态环境研究（ ），试图为乡村绿色发展提供一个新的视角与思路。 A.切入 B.植入 C.进入 D.深入",
           "Đáp án: A. 切入 – 从……切入 (lấy… làm điểm tiếp cận)",
           "(4) 西部地区发展不平衡不充分问题依然突出，西部大开发要转换（ ），才能打开新局面。 A.思路 B.门路 C.思想 D.思考",
           "Đáp án: A. 思路 – 转换思路"],
    say=["Bài tập hai: chọn đáp án đúng.",
         F(0, "Câu một: 第一道安检处设在园区内，这里安检员会什么对一些游客进行检查。 Điểm kiểm tra an ninh đầu tiên đặt trong khu vực, nhân viên ở đây sẽ kiểm tra một số du khách như thế nào. A, 随意; B, 随便; C, 随机; D, 随处."),
         F(1, "Đáp án: C, 随机, kiểm tra ngẫu nhiên. 随意 và 随便 là tùy tiện, không phù hợp với công việc an ninh; 随处 là bất cứ chỗ nào."),
         F(2, "Câu hai: 他没有放弃，一直坚持到最后，这一点让父亲很什么。 Anh ấy không bỏ cuộc, kiên trì đến cùng, điều này khiến bố anh rất thế nào. A, 欣慰; B, 欣喜; C, 安慰; D, 抚慰."),
         F(3, "Đáp án: A, 欣慰, vui mừng yên lòng. 欣喜 là vui mừng nhưng thường không đi sau 让人很; 安慰 và 抚慰 là động từ an ủi người khác."),
         F(4, "Câu ba: 这篇论文从乡村生态环境研究什么，试图为乡村绿色发展提供一个新的视角与思路。 Luận văn này làm gì từ nghiên cứu môi trường sinh thái nông thôn, cố gắng cung cấp một góc nhìn và hướng đi mới cho phát triển xanh ở nông thôn. A, 切入; B, 植入; C, 进入; D, 深入."),
         F(5, "Đáp án: A, 切入. 从什么切入, lấy cái gì làm điểm tiếp cận."),
         F(6, "Câu bốn: 西部地区发展不平衡不充分问题依然突出，西部大开发要转换什么，才能打开新局面。 Vấn đề phát triển không cân bằng, không đầy đủ ở miền Tây vẫn nổi cộm, đại khai phát miền Tây phải thay đổi cái gì mới mở ra cục diện mới. A, 思路; B, 门路; C, 思想; D, 思考."),
         F(7, "Đáp án: A, 思路. 转换思路, thay đổi cách tiếp cận, là kết hợp ta đã học ở bài ba chấm hai.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ, mẫu câu cho sẵn để trả lời (1)", reveal=True, size=33,
    items=["(1) 塑料在我们生活中占据何等地位？（渗透、扮演……角色、举足轻重）",
           "Đáp án gợi ý: 塑料已经渗透到我们衣食住行的方方面面，在人类文明的进程中扮演着举足轻重的角色。",
           "(2) 怎样才能戒掉“塑料瘾”？（从……入手）",
           "Đáp án gợi ý: 只有从生活细节入手，比如自带购物袋、少点外卖、不用一次性吸管，才能慢慢戒掉“塑料瘾”。"],
    say=["Bài tập ba: dùng từ và mẫu câu cho sẵn để trả lời câu hỏi. Đây là câu hỏi mở, thầy đưa ra đáp án gợi ý.",
         F(0, "Câu một, dùng 渗透, 扮演角色, 举足轻重: 塑料在我们生活中占据何等地位？ Nhựa chiếm vị trí như thế nào trong cuộc sống của chúng ta? 何等 là như thế nào, văn viết."),
         F(1, "Đáp án gợi ý: 塑料已经渗透到我们衣食住行的方方面面，在人类文明的进程中扮演着举足轻重的角色。 Nhựa đã len lỏi vào mọi mặt của đời sống, đóng vai trò cực kỳ quan trọng trong tiến trình văn minh nhân loại."),
         F(2, "Câu hai, dùng 从什么入手: 怎样才能戒掉塑料瘾？ Làm thế nào mới cai được cơn nghiện nhựa?"),
         F(3, "Đáp án gợi ý: 只有从生活细节入手，比如自带购物袋、少点外卖、不用一次性吸管，才能慢慢戒掉塑料瘾。 Chỉ có bắt đầu từ những chi tiết đời sống, như tự mang túi đi chợ, bớt gọi đồ ăn mang về, không dùng ống hút dùng một lần, mới dần cai được cơn nghiện nhựa.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ, mẫu câu cho sẵn để trả lời (2)", reveal=True, size=33,
    items=["(3) 快递或外卖行业有什么环保举措？（可喜的是……）",
           "Đáp án gợi ý: 可喜的是，这些企业借助公益活动着手改善现状，比如菜鸟携手通达、百世启动“回箱计划”，推进快递包装分类回收、二次利用。",
           "(4) 如何打赢“塑战”？（将……进行到底）",
           "Đáp án gợi ý: 每个人都要从自身做起，并带动身边的人，让“环保从个人做起”的理念深入人心，才能将“塑战”进行到底。"],
    say=[F(0, "Câu ba, dùng 可喜的是: 快递或外卖行业有什么环保举措？ Ngành chuyển phát và giao đồ ăn có những biện pháp bảo vệ môi trường nào?"),
         F(1, "Đáp án gợi ý: 可喜的是，这些企业借助公益活动着手改善现状，比如菜鸟携手通达、百世启动回箱计划，推进快递包装分类回收、二次利用。 Điều đáng mừng là các doanh nghiệp này nhờ hoạt động công ích mà bắt tay cải thiện hiện trạng, chẳng hạn Cainiao cùng Tongda, Best khởi động kế hoạch thu hồi thùng, thúc đẩy phân loại thu hồi và tái sử dụng bao bì."),
         F(2, "Câu bốn, dùng 将什么进行到底: 如何打赢塑战？ Làm thế nào để thắng cuộc chiến nhựa?"),
         F(3, "Đáp án gợi ý: 每个人都要从自身做起，并带动身边的人，让环保从个人做起的理念深入人心，才能将塑战进行到底。 Mỗi người phải bắt đầu từ chính mình, kéo theo người xung quanh, để ý tưởng bảo vệ môi trường từ mỗi người đi sâu vào lòng người, mới tiến hành được cuộc chiến nhựa đến cùng.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Điền từ vào đoạn văn (1)", reveal=True, size=33,
    items=["## 植入 · 先行 · 举足轻重 · 一朝一夕 · 不遗余力 · 入手 · 泛滥成灾 · 点点滴滴 · 深入人心 · 罪魁祸首",
           "塑料虽然给我们提供了巨大的便利，具有___的作用，但也在我们的生活中___，是造成白色垃圾的___。“禁塑”不是___就能实现的。一般认为，“禁塑”可以从以下两个方面___：",
           "Đáp án: 举足轻重 · 泛滥成灾 · 罪魁祸首 · 一朝一夕 · 入手"],
    say=["Bài tập bốn: chọn từ cho sẵn điền vào đoạn văn. Có mười từ: 植入，先行，举足轻重，一朝一夕，不遗余力，入手，泛滥成灾，点点滴滴，深入人心，罪魁祸首. Đoạn văn chia làm hai phần.",
         F(1, "Phần một: 塑料虽然给我们提供了巨大的便利，具有什么的作用，但也在我们的生活中什么，是造成白色垃圾的什么。禁塑不是什么就能实现的。一般认为，禁塑可以从以下两个方面什么。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 具有举足轻重的作用, có vai trò cực kỳ quan trọng; 在我们的生活中泛滥成灾, tràn lan thành họa trong cuộc sống; 是造成白色垃圾的罪魁祸首, là thủ phạm chính gây ra rác trắng; 禁塑不是一朝一夕就能实现的, cấm nhựa không thể thực hiện trong một sớm một chiều; và 可以从以下两个方面入手, có thể bắt đầu từ hai mặt sau.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Điền từ vào đoạn văn (2)", reveal=True, size=33,
    items=["一是政府___地推出强制性的政策，“绿色环保，政策___”；二是加大宣传力度，将环保意识___国民头脑之中，使“禁塑”___，人们便会自觉地从___做起。",
           "Đáp án: 不遗余力 · 先行 · 植入 · 深入人心 · 点点滴滴",
           "Phần tiếp theo của đoạn văn: 从源头上堵住“白色污染”，关键在于寻找相关替代品。以海南为例，海南在“禁塑”的同时，促进全生物降解替代产品的研发和推广……"],
    say=[F(0, "Phần hai: 一是政府什么地推出强制性的政策，绿色环保，政策什么；二是加大宣传力度，将环保意识什么国民头脑之中，使禁塑什么，人们便会自觉地从什么做起。"),
         F(1, "Đáp án: 政府不遗余力地推出强制性的政策, chính phủ dốc hết sức đưa ra chính sách bắt buộc; 绿色环保，政策先行, sống xanh thì chính sách đi trước; 将环保意识植入国民头脑之中, gieo ý thức môi trường vào đầu óc người dân; 使禁塑深入人心, làm cho việc cấm nhựa đi sâu vào lòng người; và 人们便会自觉地从点点滴滴做起, mọi người sẽ tự giác bắt đầu từ những việc nhỏ."),
         F(2, "Đoạn văn kết thúc bằng ví dụ về tỉnh Hải Nam: 从源头上堵住白色污染，关键在于寻找相关替代品。以海南为例，海南在禁塑的同时，促进全生物降解替代产品的研发和推广。 Muốn chặn ô nhiễm trắng từ gốc, mấu chốt là tìm sản phẩm thay thế. Hải Nam vừa cấm nhựa, vừa thúc đẩy nghiên cứu và phổ biến sản phẩm thay thế phân hủy sinh học hoàn toàn, có triển vọng trở thành tỉnh đầu tiên thật sự cấm nhựa ở Trung Quốc.")])

# ======================= THẢO LUẬN =======================
add("bullets", chapter="Thảo luận", section="Thảo luận 讨论", title="Thảo luận: cuộc chiến nhựa ở Việt Nam", reveal=True, size=33,
    items=["如果在生活中限制一次性塑料制品的使用，你认为我们会遇到哪些挑战？",
           "Đáp án gợi ý: 最大的挑战是习惯和成本。人们已经习惯了塑料的便利，而替代品价格高昂，很多小商贩和消费者会望而却步。另外，外卖和网购也会产生大量塑料垃圾。",
           "## Liên hệ Việt Nam",
           "Siêu thị gói rau bằng lá chuối (2019) · lộ trình hạn chế túi ni lông khó phân hủy và đồ nhựa dùng một lần",
           "Thử nói: 你自己在生活中可以从哪些点点滴滴做起？"],
    say=["Bây giờ chúng ta quay lại câu hỏi khởi động thứ ba: 如果在生活中限制一次性塑料制品的使用，你认为我们会遇到哪些挑战？ Nếu hạn chế đồ nhựa dùng một lần, chúng ta sẽ gặp những thách thức gì?",
         F(0, "Các bạn tạm dừng video, thử nói vài câu bằng tiếng Trung, dùng các từ vừa học như 谈何容易，一朝一夕，望而却步，从什么入手."),
         F(1, "Đáp án gợi ý: 最大的挑战是习惯和成本。人们已经习惯了塑料的便利，而替代品价格高昂，很多小商贩和消费者会望而却步。另外，外卖和网购也会产生大量塑料垃圾。 Thách thức lớn nhất là thói quen và chi phí. Mọi người đã quen với sự tiện lợi của nhựa, còn sản phẩm thay thế lại đắt, nhiều tiểu thương và người tiêu dùng sẽ chùn bước. Ngoài ra, đồ ăn mang về và mua sắm trên mạng cũng tạo ra lượng lớn rác nhựa."),
         F(2, "Còn ở Việt Nam thì sao?"),
         F(3, "Năm 2019, nhiều siêu thị ở Việt Nam bắt đầu gói rau củ bằng lá chuối thay cho túi ni lông, hình ảnh này từng được báo chí nước ngoài khen ngợi. Nhà nước cũng đã ban hành lộ trình hạn chế dần túi ni lông khó phân hủy và đồ nhựa dùng một lần. Nhưng giống như bài khóa nói, ở chợ truyền thống, quán ăn, hàng mang về, túi ni lông vẫn có mặt khắp nơi: cuộc chiến nhựa ở đâu cũng là một cuộc chiến trường kỳ."),
         F(4, "Các bạn thử nói: 你自己在生活中可以从哪些点点滴滴做起？ Bản thân bạn có thể bắt đầu từ những việc nhỏ nào? Ví dụ: 我出门时自带水杯和购物袋，点外卖时选择不要一次性餐具。 Tôi mang theo bình nước và túi khi ra ngoài, khi gọi đồ ăn thì chọn không lấy dụng cụ ăn dùng một lần.")])

# ======================= TỔNG KẾT BÀI =======================
add("bullets", chapter="Tổng kết", section="Tổng kết", title="Tổng kết bài 3.3", size=34,
    items=["Từ vựng trọng tâm: 誉 · 渗透 · 进程 · 顽疾 · 降解 · 切入 · 落地 · 随机 · 高昂 · 塑造 · 入手 · 剥离 · 借助 · 着手 · 缺失 · 植入 · 赖以",
           "Thành ngữ: 衣食住行 · 举足轻重 · 泛滥成灾 · 罪魁祸首 · 谈何容易 · 望而却步 · 一朝一夕 · 不遗余力 · 点点滴滴 · 深入人心",
           "Mẫu câu: 被誉为 · 扮演……角色 · 经久难…… · 之余 · 贴标签 · 谈何 · 别说……就是…… · 从……入手 · 可喜的是 · 进行到底",
           "Ý chính: 塑料是“双刃剑” → 限塑 → 禁塑 → “塑战”无法速决，要从自身做起",
           "## Bài tập về nhà",
           "Theo sách (妙笔生花): viết 限塑倡议书 – thư kêu gọi hạn chế nhựa gửi thầy cô và bạn học"],
    say=["Chúng ta cùng tổng kết bài ba chấm ba.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 誉，渗透，进程，顽疾，降解，切入，落地，随机，高昂，塑造，入手，剥离，借助，着手，缺失，植入，赖以."),
         F(1, "Mười thành ngữ: 衣食住行，举足轻重，泛滥成灾，罪魁祸首，谈何容易，望而却步，一朝一夕，不遗余力，点点滴滴，深入人心."),
         F(2, "Mười mẫu câu: 被誉为; 扮演什么的角色; 经久难愈, 经久不衰; 之余; 给什么贴上标签; 谈何容易; 别说什么就是什么; 从什么入手; 可喜的是; và 将什么进行到底."),
         F(3, "Về nội dung: nhựa là con dao hai lưỡi; chính sách đi từ hạn chế đến cấm, nhưng cuộc chiến nhựa không thể thắng nhanh; con đường đúng là bắt đầu từ chính mình."),
         F(5, "Bài tập về nhà, theo phần 妙笔生花 của sách: hãy viết một bức thư kêu gọi hạn chế nhựa, 限塑倡议书, gửi toàn thể thầy cô và bạn học, kêu gọi mọi người tự giác tuân thủ quy định hạn chế nhựa. Hãy dùng các thành ngữ và mẫu câu của bài, như 谈何容易，从什么入手，将什么进行到底.")])

# ======================= ÔN TẬP ĐƠN VỊ 3 =======================
add("bullets", chapter="Ôn tập đơn vị 3", section="Ôn tập đơn vị 单元练习", title="Ôn tập Đơn vị 3 环保篇: ba bài, một chủ đề", size=33,
    items=["## 3.1 碳排放的“蛋糕”怎么切？ – khí hậu toàn cầu",
           "排放权 = 发展权 · 人与人之间大致相等的排放空间 · 人类拯救自己 · 减排 · 共识 · 公允 · 取决于",
           "## 3.2 “随手扔”还是“随手分” – phân loại rác ở Thượng Hải",
           "并非一蹴而就 · 刚柔并济 · 长效机制 · 持久战 · 磨合 · 一刀切 · 为……做铺垫",
           "## 3.3 “塑战”能否速决？ – cuộc chiến với nhựa",
           "双刃剑 · 限塑 → 禁塑 · 一朝一夕 · 从……入手 · 无法速决 → 进行到底"],
    say=["Chúng ta đã học xong ba bài của Đơn vị ba, 环保篇. Bây giờ là phần ôn tập cả đơn vị, theo phần 单元练习，学以致用 của sách, tức là học để vận dụng.",
         F(0, "Bài ba chấm một bàn về khí hậu toàn cầu: chia chiếc bánh phát thải carbon thế nào."),
         F(1, "Ý chính: quyền phát thải là quyền phát triển; công bằng là giữa người với người có không gian phát thải gần như nhau; con người không cứu trái đất mà tự cứu mình. Từ khóa: 减排，共识，公允，取决于."),
         F(2, "Bài ba chấm hai bàn về phân loại rác ở Thượng Hải."),
         F(3, "Ý chính: thành công không phải một bước là xong; chính sách cần cương nhu kết hợp và cơ chế lâu dài. Từ khóa: 持久战，磨合，一刀切，为某事做铺垫."),
         F(4, "Bài ba chấm ba bàn về cuộc chiến với nhựa."),
         F(5, "Ý chính: nhựa là con dao hai lưỡi; từ hạn chế đến cấm; không thể thắng nhanh, nên phải tiến hành đến cùng. Các bạn thấy không, cả ba bài đều có chung một thông điệp: bảo vệ môi trường là một cuộc chiến trường kỳ, cần cả chính sách lẫn hành động của mỗi người.")])

add("bullets", section="Ôn tập đơn vị 单元练习", title="众说纷纭 · 针锋相对: thảo luận và tranh biện", reveal=True, size=32,
    items=["(1) 讨论：在节能减排上，发达国家是否有义务帮助发展中国家？",
           "Đáp án gợi ý: 有。发达国家历史排放多，资金和技术实力强，应该通过资金支持和技术转让，帮助发展中国家减排。",
           "(2) 辩论：垃圾分类重在宣传教育还是严格执法？",
           "Đáp án gợi ý: 应该刚柔并济：宣传教育让市民了解分类方法，严格执法能杜绝侥幸心理和惰性，两者缺一不可。",
           "(3) 辩论：谁该为环保产品买单？消费者还是国家？",
           "Đáp án gợi ý: 可以共同承担：国家补贴研发和生产，降低成本；消费者也应该为保护环境付出一点代价。"],
    say=["Phần ôn tập của sách có nhiều hoạt động nói. Thầy chọn ba đề tài tiêu biểu trong mục 众说纷纭, mỗi người một ý, và 针锋相对, tranh biện đối đầu.",
         F(0, "Đề một: 在节能减排上，发达国家是否有义务帮助发展中国家？ Trong việc tiết kiệm năng lượng, giảm phát thải, các nước phát triển có nghĩa vụ giúp các nước đang phát triển không? Các bạn hãy nhớ lại lập luận của ông Đinh Trọng Lễ ở bài ba chấm một."),
         F(1, "Đáp án gợi ý: 有。发达国家历史排放多，资金和技术实力强，应该通过资金支持和技术转让，帮助发展中国家减排。 Có. Các nước phát triển trong lịch sử đã thải ra nhiều, lại mạnh về vốn và công nghệ, nên giúp các nước đang phát triển giảm phát thải bằng hỗ trợ tài chính và chuyển giao công nghệ."),
         F(2, "Đề hai: 垃圾分类重在宣传教育还是严格执法？ Phân loại rác nên chú trọng tuyên truyền giáo dục hay thực thi pháp luật nghiêm khắc? Theo tài liệu của sách, ở Thượng Hải chín mươi ba phần trăm người dân muốn phân loại rác nhưng chưa hiểu rõ cách phân loại."),
         F(3, "Đáp án gợi ý: 应该刚柔并济：宣传教育让市民了解分类方法，严格执法能杜绝侥幸心理和惰性，两者缺一不可。 Nên cương nhu kết hợp: tuyên truyền giúp người dân hiểu cách phân loại, thực thi nghiêm khắc thì dập tắt tâm lý cầu may và sự lười biếng, thiếu một trong hai đều không được. 侥幸心理 là tâm lý cầu may, 惰性 là tính ỳ."),
         F(4, "Đề ba: 谁该为环保产品买单？消费者还是国家？ Ai nên trả tiền cho sản phẩm thân thiện môi trường, người tiêu dùng hay nhà nước? Sách cho biết túi phân hủy được có giá thành đắt gấp mấy lần túi thường. 买单 là trả tiền, thanh toán."),
         F(5, "Đáp án gợi ý: 可以共同承担：国家补贴研发和生产，降低成本；消费者也应该为保护环境付出一点代价。 Có thể cùng gánh vác: nhà nước trợ cấp nghiên cứu và sản xuất để hạ giá thành; người tiêu dùng cũng nên trả một chút chi phí vì môi trường.")])

add("bullets", section="Ôn tập đơn vị 单元练习", title="从句段到篇章: cấu trúc báo cáo điều tra bằng bảng hỏi", size=33,
    items=["## 引言 – lý do, ý nghĩa, thời gian, đối tượng, cách điều tra",
           "由于/鉴于……，了解……尤为重要 · 为此，就……问题进行了问卷调查 · 在受访人群中，……占……%",
           "## 问卷及结果 – câu hỏi, câu trả lời tiêu biểu, số liệu",
           "调查发现，受访者普遍认为…… · ……%的受访人群表示 · 持……意见的受访者达……%",
           "## 分析 → 总结与评价",
           "通过分析，我们大致可以得出以下几点结论 · 整体而言 · 换言之 · 由此可见 · 综上所述 · 总而言之"],
    say=["Phần ôn tập còn dạy một kỹ năng viết quan trọng: 从句段到篇章, từ câu, đoạn đến cả bài văn, cụ thể là viết báo cáo điều tra bằng bảng hỏi, 问卷调查报告.",
         F(0, "Phần thứ nhất là 引言, lời mở đầu: giải thích lý do và ý nghĩa của cuộc điều tra, thời gian, địa điểm, đối tượng được hỏi, cách điều tra."),
         F(1, "Mẫu câu hay dùng: 由于什么，了解什么尤为重要, vì… nên việc tìm hiểu… càng đặc biệt quan trọng; 为此，就什么问题进行了问卷调查, vì vậy đã tiến hành điều tra bằng bảng hỏi về vấn đề…. Các bạn để ý, đây chính là mẫu 就 của bài ba chấm một."),
         F(2, "Phần thứ hai là 问卷及结果, bảng hỏi và kết quả: liệt kê câu hỏi, câu trả lời tiêu biểu, số liệu thu được."),
         F(3, "Mẫu câu: 调查发现，受访者普遍认为, điều tra phát hiện người được hỏi nhìn chung cho rằng; 百分之几的受访人群表示, bao nhiêu phần trăm người được hỏi cho biết; 持什么意见的受访者达百分之几, số người có ý kiến ấy đạt bao nhiêu phần trăm."),
         F(4, "Phần thứ ba là 分析, phân tích kết quả, rút ra quy luật; cuối cùng là 总结与评价, tổng kết và đánh giá, nêu hạn chế và kiến nghị cho các cuộc điều tra sau."),
         F(5, "Mẫu câu: 通过分析，我们大致可以得出以下几点结论; 整体而言, nhìn chung; 换言之, nói cách khác; 由此可见, từ đó có thể thấy; 综上所述 và 总而言之, tóm lại. Sách còn liệt kê cả 简单一句话 và 也就是说 của bài ba chấm một.")])

add("bullets", section="Ôn tập đơn vị 单元练习", title="Đọc bài mẫu, điền từ: 占 · 通过分析 · 为此 · 此外 · 就 · 总而言之 · 鉴于 · 据数据统计", reveal=True, size=31,
    items=["环保已成为当下的热门话题，了解公众的环保意识至关重要。(1)___，本人于上周末(2)___公众的环保习惯进行了调查。……年龄在20到30岁的(3)___80%。",
           "Đáp án: (1) 为此 · (2) 就 · (3) 占",
           "(4)___：（1）在办公室或家里休息时，把空调温度调到26度或以上的有47人……",
           "Đáp án: (4) 据数据统计",
           "(5)___，我们大致可以得出以下结论：……环保意识得到提高。(6)___，数据也显示，有一部分人的环保意识还需进一步加强……(7)___，环保工作并非一朝一夕之事，践行绿色环保的理念永远在路上。",
           "Đáp án: (5) 通过分析 · (6) 此外 · (7) 总而言之 · 鉴于 không dùng (phải có tân ngữ: 鉴于……，……)"],
    say=["Bài tập của phần này: đọc bài báo cáo mẫu về thói quen bảo vệ môi trường, chọn từ điền vào chỗ trống. Có tám từ: 占，通过分析，为此，此外，就，总而言之，鉴于，据数据统计.",
         F(0, "Đoạn mở đầu: 环保已成为当下的热门话题，了解公众的环保意识至关重要。什么，本人于上周末什么公众的环保习惯进行了调查。参加本次网上问卷调查的总人数为一百四十八人次，其中男性七十人，女性八十人，年龄在二十到三十岁的什么百分之八十。 Các bạn tạm dừng và điền thử nhé."),
         F(1, "Đáp án: 为此，本人于上周末就公众的环保习惯进行了调查, vì vậy, cuối tuần trước tôi đã điều tra về thói quen bảo vệ môi trường của công chúng; và 年龄在二十到三十岁的占百分之八十, người từ hai mươi đến ba mươi tuổi chiếm tám mươi phần trăm. Mẫu 就什么进行调查 rất quen thuộc rồi."),
         F(2, "Tiếp theo: 什么：第一，在办公室或家里休息时，把空调温度调到二十六度或以上的有四十七人。 Sau đó là một loạt số liệu."),
         F(3, "Đáp án: 据数据统计, theo thống kê số liệu."),
         F(4, "Đoạn cuối: 什么，我们大致可以得出以下结论：经过多年宣传，公众在日常生活中培养了不少良好的环保习惯，环保意识得到提高。什么，数据也显示，有一部分人的环保意识还需进一步加强。什么，环保工作并非一朝一夕之事，践行绿色环保的理念永远在路上。"),
         F(5, "Đáp án: 通过分析，我们大致可以得出以下结论, qua phân tích, có thể rút ra kết luận; 此外，数据也显示, ngoài ra, số liệu cũng cho thấy; 总而言之，环保工作并非一朝一夕之事, tóm lại, công tác môi trường không phải chuyện một sớm một chiều. Còn 鉴于 không dùng, vì phía sau nó phải có một cụm danh từ hay mệnh đề làm căn cứ, như 鉴于环保已成为热门话题. Các bạn thấy đấy, chỉ một bài báo cáo ngắn mà gặp lại 就，进一步，并非，一朝一夕，践行，理念 của cả đơn vị.")])

add("bullets", section="Ôn tập đơn vị 单元练习", title="Vận dụng: nhiệm vụ của phần 学以致用", size=33,
    items=["新闻报告 – giới thiệu tin tức về “禁塑令”: bối cảnh, thay đổi, ý kiến của mọi người, ý kiến của em",
           "问卷调查 · 明察暗访 – thiết kế bảng hỏi, phỏng vấn người xung quanh về rác thải, đồ nhựa",
           "研究报告 · 建言献策 – tìm hiểu nguồn gốc, tác hại của rác nhựa; đề xuất biện pháp hạn chế nhựa ở nước em",
           "## 妙笔生花 – bài viết",
           "垃圾，放错位置的资源 (Rác là tài nguyên đặt sai chỗ) · 限塑倡议书 (Thư kêu gọi hạn chế nhựa)"],
    say=["Cuối cùng, phần 学以致用 còn có nhiều nhiệm vụ vận dụng. Thầy tóm tắt để các bạn tự luyện.",
         F(0, "新闻报告, báo cáo tin tức: lên mạng tìm tin về việc thực hiện lệnh cấm nhựa, rồi giới thiệu: bối cảnh ra đời, nó thay đổi cuộc sống thế nào, mọi người nghĩ gì, và bạn nghĩ gì."),
         F(1, "问卷调查 và 明察暗访: thiết kế bảng hỏi, phỏng vấn người xung quanh về cách phân loại rác, tác hại của rác, thái độ với lệnh cấm nhựa. Các bạn có thể làm ngay với bạn bè người Việt, rồi viết báo cáo bằng tiếng Trung theo cấu trúc vừa học."),
         F(2, "研究报告 và 建言献策: tìm hiểu rác nhựa đến từ những ngành nào, có những tác hại gì, vì sao hạn chế nhựa lại khó; rồi đề xuất biện pháp hạn chế nhựa cho đất nước mình."),
         F(3, "Và 妙笔生花, phần viết văn, có hai đề."),
         F(4, "Đề một: 垃圾，放错位置的资源, rác là tài nguyên đặt sai chỗ, viết về ngành công nghiệp môi trường ở nước bạn. Đề hai: 限塑倡议书, thư kêu gọi hạn chế nhựa, chính là bài tập về nhà của bài này.",
           cap="Đề một: 垃圾，放错位置的资源 – rác là tài nguyên đặt sai chỗ. Đề hai: 限塑倡议书 – thư kêu gọi hạn chế nhựa."),
         "Cảm ơn các bạn đã theo dõi bài giảng, và xin chúc mừng: chúng ta đã hoàn thành Đơn vị ba, 环保篇. Bài sau, chúng ta bước sang Đơn vị bốn, 科技篇, chủ đề Khoa học công nghệ, với bài bốn chấm một: 真的，你的隐私只值一分钱！ Thật đấy, quyền riêng tư của bạn chỉ đáng một xu! Một nghệ sĩ đã mua hàng trăm nghìn thông tin cá nhân với giá rẻ như cho, rồi đem trưng bày. Hẹn gặp lại các bạn. Chúc các bạn học tốt!"])

lesson = {
    "title": "顶石中文 – Bài 3.3: “塑战”能否速决？ (“Cuộc chiến nhựa” có thắng nhanh được không?)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"誉为": "誉维",            # yùwéi
                    "落地": "洛地",            # luòdì
                    "剥离": "拨离",            # bōlí
                    "着手": "酌手",            # zhuóshǒu
                    "着眼": "酌眼",            # zhuóyǎn
                    "铺设": "扑设",            # pūshè
                    "一朝一夕": "一招一夕",    # yīzhāo-yīxī
                    "还给": "环给",            # huángěi
                    "重新": "虫新",            # chóngxīn
                    "覆盖率": "覆盖律",        # fùgàilǜ
                    "氧吧": "氧巴",            # yǎngbā
                    "角色": "决色",            # juésè
                    "大处": "大触",            # dàchù
                    "小处": "小触",            # xiǎochù
                    "曾广受": "层广受",        # céng
                    "草草了事": "草草蓼事",    # liǎoshì
                    "规划": "规话",            # guīhuà
                    "参与": "参预",            # cānyù
                    "长大": "掌大",            # zhǎngdà
                    "长期": "常期",            # chángqī
                    "分子": "份子",            # fènzǐ
                    "物种": "物肿",            # wùzhǒng
                    "调查": "掉查",            # diàochá
                    "数倍": "树倍",            # shùbèi
                    "为例": "维例",            # wéilì
                    "行业": "航业",            # hángyè
                    "兴奋": "星奋",            # xīngfèn
                    "尽可能": "仅可能",        # jǐnkěnéng
                    "处理": "楚理",            # chǔlǐ
                    "相处": "相楚",            # xiāngchǔ
                    "会计": "快计",            # kuàijì
                    "为切入点": "维切入点",    # wéi
                    "为此": "位此",            # wèicǐ
                    "空调": "空条",            # kōngtiáo
                    "调到": "条到",            # tiáodào
                    "尤为": "尤维",            # yóuwéi
                    "赖以为生": "赖以维生",    # wéi
                    "安检处": "安检触",        # chù
                    "屏蔽": "平蔽",            # píngbì
                    "多重": "多虫",            # duōchóng
                    "效应": "效映"},           # xiàoyìng
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds33.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
