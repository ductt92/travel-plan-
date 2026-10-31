#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Hạ) – Bài 36 «中国古代书院». Chạy để sinh bai36.json."""
import json
import os

TAG = "HSK 6 (Hạ) · Bài 36 · 中国古代书院"
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
    top="Giáo trình chuẩn HSK 6 – Quyển Hạ",
    zh="中国古代书院", py="Zhōngguó gǔdài shūyuàn", vi="Bài 36: Thư viện (học viện) cổ đại Trung Quốc",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Hạ.",
         "Hôm nay chúng ta học bài ba mươi sáu: 中国古代书院。 Nghĩa là: Thư viện cổ đại Trung Quốc.",
         "Các bạn chú ý ngay từ đầu: 书院 đọc theo Hán Việt là thư viện, nhưng nó không phải là nơi mượn sách như thư viện ngày nay, tiếng Trung gọi nơi đó là 图书馆. 书院 thời xưa là một loại học viện, vừa cất giữ sách, vừa dạy học, vừa nghiên cứu.",
         "Đây là bài cuối cùng của Đơn vị chín, chủ đề 古今博览, tức là nhìn rộng chuyện xưa nay. Bài khóa kể lại lịch sử của thư viện, cách thư viện đào tạo nhân tài, và những phương pháp dạy học rất tiến bộ của nó."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu nội dung bài khóa 中国古代书院 – lịch sử, mục tiêu và cách dạy học của thư viện",
           "Nắm vững 50 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: phó từ 一经 và giới từ 本着",
           "Phân biệt hai động từ 截止 và 终止",
           "Kỹ năng viết: luận điểm + dẫn chứng (论点 + 例证)"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa: thư viện ra đời thế nào, thư viện đào tạo con người ra sao, và vì sao cách dạy học của thư viện được coi là rất cởi mở."),
         F(1, "Thứ hai, nắm vững năm mươi từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học hai điểm ngữ pháp: phó từ 一经, nghĩa là hễ, một khi đã; và giới từ 本着, nghĩa là dựa trên, theo."),
         F(3, "Thứ tư, phân biệt hai động từ đều có nghĩa dừng lại: 截止 và 终止."),
         F(4, "Thứ năm, một kỹ năng viết văn nghị luận rất quan trọng: nêu luận điểm rồi dùng dẫn chứng để chứng minh, tiếng Trung gọi là 论点加例证."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Câu hỏi khởi động", size=34,
    items=["你认为一个好的教育体系应该包含哪些方面？ – Một hệ thống giáo dục tốt nên gồm những mặt nào?",
           "## 下列教育理念你同意吗？ – Bạn có đồng ý với các quan niệm sau không?",
           "要有刻苦、严谨的治学精神 – phải có tinh thần học tập chăm chỉ, nghiêm cẩn",
           "学问比道德培养更重要 – học vấn quan trọng hơn bồi dưỡng đạo đức",
           "学习没有捷径 – học tập không có đường tắt · 不断地复习很重要 – ôn tập không ngừng rất quan trọng",
           "独立思考很重要 – suy nghĩ độc lập rất quan trọng",
           "形成讨论，质疑，不同观点互相辩论的风气 – tạo không khí thảo luận, chất vấn, tranh luận giữa các quan điểm"],
    say=["Chúng ta bắt đầu bằng phần khởi động. Sách hỏi như sau.",
         F(0, "你认为一个好的教育体系应该包含哪些方面？ Theo bạn, một hệ thống giáo dục tốt nên bao gồm những mặt nào? 体系 là hệ thống, 包含 là bao gồm."),
         F(1, "下列教育理念你同意吗？ Bạn có đồng ý với những quan niệm giáo dục dưới đây không? 理念 là quan niệm, triết lý. Sách kẻ một bảng có hai cột: 同意, đồng ý, và 不同意, không đồng ý."),
         F(2, "Một: 要有刻苦、严谨的治学精神。 Phải có tinh thần học tập chăm chỉ, nghiêm cẩn. 治学 là làm học vấn, một từ quan trọng của bài."),
         F(3, "Hai: 学问比道德培养更重要。 Học vấn quan trọng hơn bồi dưỡng đạo đức. Các bạn có đồng ý không? Bài khóa hôm nay sẽ có câu trả lời khá rõ ràng."),
         F(4, "Ba: 学习没有捷径。 Học tập không có đường tắt. Bốn: 不断地复习很重要。 Ôn tập không ngừng rất quan trọng."),
         F(5, "Năm: 独立思考很重要。 Suy nghĩ độc lập rất quan trọng."),
         F(6, "Sáu: 形成讨论，质疑，不同观点互相辩论的风气。 Tạo nên bầu không khí thảo luận, chất vấn, và tranh luận giữa các quan điểm khác nhau. 风气 là phong khí, tức nếp chung, không khí chung."),
         "Các bạn hãy tạm dừng video, đánh dấu đồng ý hay không đồng ý, rồi thử nói lý do bằng tiếng Trung, ví dụ: 我同意学习没有捷径，因为学问要一点一点积累。 Sau đó hãy xem tiếp nhé."])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 私 và 流", size=36,
    items=["## 私 (tư): riêng, cá nhân",
           "私人 tư nhân · 私事 việc riêng · 私下 riêng, ngầm · 私信 thư riêng · 私有 tư hữu · 私营 tư doanh",
           "私立 tư lập · 私宅 nhà riêng · 私生活 đời tư · 私房钱 tiền riêng giấu kín · 公私分明 công tư phân minh",
           "## 流 (lưu): chảy, trôi, di chuyển",
           "流转 lưu chuyển · 流动 lưu động · 流浪 lang thang · 流放 lưu đày · 流年 năm tháng trôi · 流失 thất thoát",
           "流通 lưu thông · 流星 sao băng · 流离 phiêu bạt · 流落 lưu lạc · 轮流 luân phiên · 漂流 trôi dạt"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo, rất có lợi cho người Việt vì hầu hết các chữ đều có âm Hán Việt quen thuộc.",
         F(0, "Nhóm thứ nhất có chữ 私, Hán Việt là tư, như trong tư nhân, nghĩa là riêng, của cá nhân."),
         F(1, "私人，私事，私下，私信，私有，私营。 Tức là: tư nhân, việc riêng, riêng tư hay lén lút, thư riêng, tư hữu, và tư doanh. Bài khóa có cụm 私人藏书, sách do tư nhân cất giữ."),
         F(2, "私立，私宅，私生活，私房钱，公私分明。 Tức là: tư lập, nhà riêng, đời tư, tiền riêng giấu kín, và công tư phân minh. Ví dụ 私立学校 là trường tư thục."),
         F(3, "Nhóm thứ hai có chữ 流, Hán Việt là lưu, nghĩa là chảy, trôi, di chuyển."),
         F(4, "流转，流动，流浪，流放，流年，流失。 Tức là: lưu chuyển, lưu động, lang thang, lưu đày, năm tháng trôi qua, và thất thoát. Bài khóa có cụm 时光流转, thời gian trôi đi."),
         F(5, "流通，流星，流离，流落，轮流，漂流。 Tức là: lưu thông, sao băng, phiêu bạt, lưu lạc, luân phiên, và trôi dạt.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 缩 và 长 (zhǎng)", size=36,
    items=["## 缩 (súc): co lại, thu nhỏ",
           "缩影 hình ảnh thu nhỏ · 缩小 thu nhỏ · 缩短 rút ngắn · 缩回 rụt lại · 缩减 cắt giảm · 缩水 co (vải)",
           "缩写 viết tắt · 缩印 in thu nhỏ · 紧缩 thắt chặt · 简缩 rút gọn · 浓缩 cô đặc · 压缩 nén · 节衣缩食 thắt lưng buộc bụng",
           "## 长 zhǎng (trưởng): lớn tuổi, bậc trên",
           "长幼 người lớn và trẻ nhỏ · 长辈 bậc bề trên · 长亲 họ hàng bậc trên · 长者 bậc trưởng thượng",
           "年长 lớn tuổi · 师长 thầy và bậc trên · 兄长 anh trưởng · 学长 đàn anh khóa trên · 尊长 bậc tôn trưởng"],
    say=[F(0, "Nhóm thứ ba có chữ 缩, Hán Việt là súc, nghĩa là co lại, thu nhỏ lại."),
         F(1, "缩影，缩小，缩短，缩回，缩减，缩水。 Tức là: hình ảnh thu nhỏ, thu nhỏ, rút ngắn, rụt lại, cắt giảm, và vải bị co lại khi giặt. Bài khóa có câu: 东佳书院是中国书院制度的一个缩影。"),
         F(2, "缩写，缩印，紧缩，简缩，浓缩，压缩，节衣缩食。 Tức là: viết tắt, in thu nhỏ, thắt chặt, rút gọn, cô đặc, nén, và thắt lưng buộc bụng."),
         F(3, "Nhóm cuối cùng có chữ trưởng. Chữ này có hai cách đọc, nhưng trong nhóm từ này đều đọc là zhǎng, thanh ba, nghĩa là lớn tuổi, bậc trên, như trong trưởng bối, trưởng lão."),
         F(4, "长幼，长辈，长亲，长者。 Tức là: người lớn và trẻ nhỏ, bậc bề trên, họ hàng bậc trên, và bậc trưởng thượng. Bài khóa có hai cụm 孝顺长辈 và 讲究长幼."),
         F(5, "年长，师长，兄长，学长，尊长。 Tức là: lớn tuổi, thầy và bậc trên, anh trưởng, đàn anh khóa trên, và bậc tôn trưởng."),
         "Các bạn thấy không, chỉ cần nắm nghĩa của một chữ gốc, ta có thể đoán được nghĩa của cả một nhóm từ. Hãy áp dụng cách này khi học từ mới nhé."])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng)
V = [
    ("官方", "guānfāng", "quan phương", "danh từ", "phía chính quyền, chính thức (của nhà nước)", "这是官方公布的最新数据。", "Đây là số liệu mới nhất do phía nhà nước công bố.",
     "Danh từ, nghĩa là phía chính quyền, phía nhà nước, hay chính thức. 官方藏书 trong bài là sách do triều đình cất giữ, đối lập với 私人藏书."),
    ("层出不穷", "céngchū-bùqióng", "tằng xuất bất cùng", "thành ngữ", "liên tiếp xuất hiện, nhiều không kể xiết", "网络上的新词层出不穷。", "Từ mới trên mạng liên tục xuất hiện không ngớt.",
     "Thành ngữ. 层出 là lớp lớp xuất hiện, 不穷 là không bao giờ hết. Nghĩa là liên tiếp xuất hiện, nhiều không kể xiết."),
    ("命名", "mìng míng", "mệnh danh", "động từ", "đặt tên (chính thức)", "这座桥是用一位英雄的名字命名的。", "Cây cầu này được đặt theo tên một vị anh hùng.",
     "Động từ, nghĩa là đặt tên. Cẩn thận: được mệnh danh trong tiếng Việt là được gọi là, có biệt danh là; còn 命名 là đặt tên một cách chính thức. Mẫu hay gặp: 把 A 命名为 B, hoặc 以……命名."),
    ("规章", "guīzhāng", "quy chương", "danh từ", "quy chế, điều lệ", "每个员工都要遵守公司的规章制度。", "Mỗi nhân viên đều phải tuân thủ quy chế của công ty.",
     "Danh từ, nghĩa là quy chế, điều lệ. Cụm rất hay gặp là 规章制度, quy chế và chế độ."),
    ("截止", "jiézhǐ", "tiệt chỉ", "động từ", "hết hạn, tính đến (một thời hạn)", "报名截止到本月三十号。", "Hạn đăng ký kéo dài đến hết ngày ba mươi tháng này.",
     "Động từ, nghĩa là dừng lại khi đến một thời hạn nhất định, tức hết hạn, tính đến. 截止日期 là hạn chót. Lát nữa ta sẽ so sánh với 终止."),
    ("终止", "zhōngzhǐ", "chung chỉ", "động từ", "chấm dứt, kết thúc", "双方决定终止合同。", "Hai bên quyết định chấm dứt hợp đồng.",
     "Động từ, nghĩa là chấm dứt, kết thúc, kết hợp được với nhiều danh từ như 合同, 比赛, 活动."),
    ("完备", "wánbèi", "hoàn bị", "tính từ", "đầy đủ, hoàn chỉnh", "这家医院的设备非常完备。", "Trang thiết bị của bệnh viện này rất đầy đủ.",
     "Tính từ, nghĩa là đầy đủ, hoàn chỉnh, không thiếu thứ gì. Trong bài, 完备于宋 nghĩa là hoàn thiện vào đời Tống."),
    ("立足", "lìzú", "lập túc", "động từ", "đứng vững; lấy… làm nền tảng", "我们要立足现在，放眼未来。", "Chúng ta phải đứng vững ở hiện tại, nhìn xa tới tương lai.",
     "Động từ, nghĩa đen là đặt chân, đứng vững; nghĩa bóng là lấy cái gì làm nền tảng, chỗ dựa. Mẫu 立足于…… rất hay gặp."),
    ("灵魂", "línghún", "linh hồn", "danh từ", "linh hồn, tâm hồn; cốt lõi", "音乐是这部电影的灵魂。", "Âm nhạc là linh hồn của bộ phim này.",
     "Danh từ, nghĩa là linh hồn, tâm hồn, âm Hán Việt giống hệt tiếng Việt. Nghĩa bóng là phần cốt lõi. Trong bài, 灵魂塑造 là hun đúc tâm hồn, tức giáo dục nhân cách."),
    ("颁布", "bānbù", "ban bố", "động từ", "ban hành, công bố (luật lệ)", "国家颁布了新的教育法。", "Nhà nước đã ban hành luật giáo dục mới.",
     "Động từ, nghĩa là ban hành, công bố luật lệ, quy định, thường do cơ quan có thẩm quyền."),
    ("品德", "pǐndé", "phẩm đức", "danh từ", "phẩm chất đạo đức", "他学习好，品德也好。", "Cậu ấy học giỏi, phẩm chất đạo đức cũng tốt.",
     "Danh từ, nghĩa là phẩm chất đạo đức. 品德修养 là tu dưỡng đạo đức."),
    ("过失", "guòshī", "quá thất", "danh từ", "lỗi lầm, sai sót (thường vô ý)", "这次事故是由于司机的过失造成的。", "Vụ tai nạn lần này là do lỗi của tài xế gây ra.",
     "Danh từ, nghĩa là lỗi lầm, sai sót, thường là do sơ suất, vô ý gây ra."),
    ("无耻", "wúchǐ", "vô sỉ", "tính từ", "vô liêm sỉ, trơ trẽn", "他竟然说出这么无耻的话！", "Hắn lại có thể nói ra những lời vô liêm sỉ như vậy!",
     "Tính từ, nghĩa là vô liêm sỉ, không biết xấu hổ. 无耻之徒 trong bài là kẻ vô liêm sỉ."),
    ("容纳", "róngnà", "dung nạp", "động từ", "chứa, chứa được; chấp nhận", "这个体育场可以容纳五万人。", "Sân vận động này có thể chứa năm vạn người.",
     "Động từ, nghĩa là chứa được, hoặc chấp nhận, dung nạp. Trong bài, 本书院定不容纳 là thư viện này nhất định không chấp nhận."),
    ("透露", "tòulù", "thấu lộ", "động từ", "tiết lộ, để lộ ra", "他没有透露比赛的结果。", "Anh ấy không tiết lộ kết quả cuộc thi.",
     "Động từ, nghĩa là tiết lộ, để lộ ra. Chú ý: 透露 đọc là tòulù, thanh bốn."),
    ("治理", "zhìlǐ", "trị lý", "động từ", "quản lý, cai quản; xử lý (ô nhiễm…)", "政府正在大力治理空气污染。", "Chính phủ đang ra sức xử lý ô nhiễm không khí.",
     "Động từ, nghĩa là quản lý, cai quản, như 治理国家; hoặc xử lý, khắc phục, như 治理污染."),
    ("树立", "shùlì", "thụ lập", "động từ", "xây dựng, dựng nên (hình ảnh, tấm gương…)", "父母要给孩子树立好榜样。", "Cha mẹ phải làm tấm gương tốt cho con cái.",
     "Động từ, nghĩa là xây dựng, dựng nên, thường dùng cho những thứ trừu tượng như 树立榜样, nêu gương, 树立正气, xây dựng chính khí."),
    ("正气", "zhèngqì", "chính khí", "danh từ", "chính khí, tác phong lành mạnh", "这个人身上有一股正气。", "Người này toát lên một luồng chính khí.",
     "Danh từ, nghĩa là chính khí, phong khí lành mạnh, ngay thẳng."),
    ("唾弃", "tuòqì", "thóa khí", "động từ", "phỉ nhổ, ruồng bỏ, khinh bỉ", "这种自私的行为被大家唾弃。", "Hành vi ích kỷ này bị mọi người khinh bỉ.",
     "Động từ. 唾 là nhổ nước bọt, 弃 là vứt bỏ. Nghĩa là phỉ nhổ, ruồng bỏ, khinh bỉ."),
    ("卑鄙", "bēibǐ", "ti bỉ", "tính từ", "hèn hạ, đê tiện", "他用卑鄙的手段骗了朋友的钱。", "Hắn dùng thủ đoạn hèn hạ để lừa tiền của bạn bè.",
     "Tính từ, nghĩa là hèn hạ, đê tiện. 卑鄙的手段 là thủ đoạn hèn hạ."),
    ("堕落", "duòluò", "đọa lạc", "động từ", "sa đọa, sa ngã", "他因为交了坏朋友而堕落了。", "Anh ta sa ngã vì kết bạn xấu.",
     "Động từ, nghĩa là sa đọa, sa ngã, trượt dần vào con đường xấu."),
    ("腐败", "fǔbài", "hủ bại", "tính từ", "thối rữa; tham nhũng, hủ bại", "政府坚决打击腐败行为。", "Chính phủ kiên quyết trấn áp hành vi tham nhũng.",
     "Tính từ, có hai nghĩa: thức ăn thối rữa; và chính trị, tác phong hủ bại, tham nhũng. Trong bài, 腐败行为 là hành vi hủ bại."),
    ("崇高", "chónggāo", "sùng cao", "tính từ", "cao cả, cao quý", "教师是一个崇高的职业。", "Giáo viên là một nghề cao quý.",
     "Tính từ, nghĩa là cao cả, cao quý, dùng cho lý tưởng, phẩm chất, nghề nghiệp."),
    ("境界", "jìngjiè", "cảnh giới", "danh từ", "cảnh giới, trình độ, tầm (tư tưởng)", "他的画已经达到了很高的境界。", "Tranh của ông ấy đã đạt tới một cảnh giới rất cao.",
     "Danh từ, nghĩa là cảnh giới, tức mức độ, tầm cao mà tư tưởng hay nghệ thuật đạt được. Chú ý: không nhầm với cảnh giới theo nghĩa canh gác trong tiếng Việt, tiếng Trung là 警戒."),
    ("攀登", "pāndēng", "phan đăng", "động từ", "leo, trèo lên (cao)", "他们终于攀登上了山顶。", "Cuối cùng họ đã leo lên tới đỉnh núi.",
     "Động từ, nghĩa là leo, trèo lên chỗ cao; nghĩa bóng là phấn đấu vươn tới, như 攀登科学高峰."),
    ("窍门", "qiàomén", "khiếu môn", "danh từ", "mẹo, bí quyết", "学外语有什么窍门吗？", "Học ngoại ngữ có mẹo gì không?",
     "Danh từ, nghĩa là mẹo, bí quyết để làm việc gì đó nhanh và hiệu quả."),
    ("发扬", "fāyáng", "phát dương", "động từ", "phát huy, phát triển (truyền thống, tinh thần)", "我们要发扬艰苦奋斗的精神。", "Chúng ta phải phát huy tinh thần gian khổ phấn đấu.",
     "Động từ, nghĩa là phát huy, như trong câu phát dương quang đại. Thường đi với 精神, 传统, 优点."),
    ("敞开", "chǎngkāi", "sưởng khai", "động từ", "mở toang, mở rộng", "他敞开窗户，让新鲜空气进来。", "Anh ấy mở toang cửa sổ cho không khí trong lành vào.",
     "Động từ, nghĩa là mở toang, mở rộng. Nghĩa bóng: 敞开心扉 là mở lòng."),
    ("招收", "zhāoshōu", "chiêu thu", "động từ", "tuyển, thu nhận (học sinh, nhân viên)", "这所大学今年招收了三千名新生。", "Năm nay trường đại học này tuyển ba nghìn sinh viên mới.",
     "Động từ, nghĩa là tuyển, thu nhận học sinh hoặc nhân viên."),
    ("开明", "kāimíng", "khai minh", "tính từ", "cởi mở, tiến bộ, thoáng", "他的父母很开明，从不干涉他的选择。", "Bố mẹ cậu ấy rất cởi mở, không can thiệp vào lựa chọn của cậu.",
     "Tính từ, nghĩa là cởi mở, tiến bộ, tư tưởng thoáng. 开明之举 trong bài là một việc làm cởi mở, tiến bộ."),
    ("倡议", "chàngyì", "xướng nghị", "động từ", "đề xướng, kêu gọi", "学校倡议大家节约用水。", "Nhà trường kêu gọi mọi người tiết kiệm nước.",
     "Động từ, nghĩa là đề xướng, kêu gọi mọi người cùng làm một việc. Cũng dùng như danh từ: 一份倡议书, một bản lời kêu gọi."),
    ("杜绝", "dùjué", "đỗ tuyệt", "động từ", "ngăn chặn hoàn toàn, chấm dứt hẳn", "我们要杜绝浪费现象。", "Chúng ta phải chấm dứt hẳn hiện tượng lãng phí.",
     "Động từ, nghĩa là ngăn chặn triệt để, chấm dứt hẳn, thường dùng với điều xấu."),
    ("干涉", "gānshè", "can thiệp", "động từ", "can thiệp, xen vào", "别人的私事，我们不应该干涉。", "Việc riêng của người khác, chúng ta không nên can thiệp.",
     "Động từ, nghĩa là can thiệp, xen vào, âm Hán Việt giống hệt tiếng Việt. Chú ý 干涉 đọc là gānshè, thanh một."),
    ("过问", "guòwèn", "quá vấn", "động từ", "hỏi đến, quan tâm can dự", "这件事你就别过问了。", "Chuyện này anh đừng hỏi đến nữa.",
     "Động từ, nghĩa là hỏi đến, để ý can dự vào. Cẩn thận: không phải là hỏi quá nhiều; muốn nói hỏi quá nhiều thì phải thêm 过多, như trong bài: 不会过多过问."),
    ("激发", "jīfā", "kích phát", "động từ", "khơi dậy, kích thích", "老师用游戏激发学生的学习兴趣。", "Thầy dùng trò chơi để khơi dậy hứng thú học tập của học sinh.",
     "Động từ, nghĩa là khơi dậy, kích thích, thường đi với 兴趣, 热情, 积极性, 创造性."),
    ("多元化", "duōyuánhuà", "đa nguyên hóa", "tính từ", "đa dạng, nhiều chiều", "现代社会的文化越来越多元化。", "Văn hóa xã hội hiện đại ngày càng đa dạng.",
     "Tính từ, nghĩa là đa dạng, nhiều chiều. Cẩn thận: trong tiếng Việt, đa nguyên thường mang sắc thái chính trị, còn 多元化 chỉ đơn giản là đa dạng hóa. 观点的多元化 là sự đa dạng về quan điểm."),
    ("开展", "kāizhǎn", "khai triển", "động từ", "triển khai, tiến hành (hoạt động)", "学校开展了丰富多彩的课外活动。", "Nhà trường triển khai nhiều hoạt động ngoại khóa phong phú.",
     "Động từ, nghĩa là triển khai, tiến hành. Cẩn thận: từ này là bẫy, vì khai triển trong tiếng Việt là khai triển biểu thức trong toán học, còn 开展 tương đương với triển khai."),
    ("对立", "duìlì", "đối lập", "động từ", "đối lập, đối chọi", "双方的观点完全对立。", "Quan điểm của hai bên hoàn toàn đối lập.",
     "Động từ, nghĩa là đối lập, đối chọi nhau, âm Hán Việt giống hệt tiếng Việt."),
    ("分歧", "fēnqí", "phân kỳ", "danh từ", "bất đồng, khác biệt (ý kiến)", "我们在这个问题上有一些分歧。", "Chúng tôi có một số bất đồng về vấn đề này.",
     "Danh từ, nghĩa là sự bất đồng ý kiến. Cẩn thận: phân kỳ trong tiếng Việt thường là chia giai đoạn, còn 分歧 là bất đồng. Mẫu hay gặp: 出现分歧, 产生分歧."),
    ("保守", "bǎoshǒu", "bảo thủ", "tính từ", "bảo thủ; (động từ) giữ (bí mật)", "老一辈人的思想比较保守。", "Tư tưởng của thế hệ trước tương đối bảo thủ.",
     "Tính từ, nghĩa là bảo thủ, giống tiếng Việt. Ngoài ra nó còn là động từ, nghĩa là giữ gìn, như 保守秘密, giữ bí mật."),
    ("较量", "jiàoliàng", "giảo lượng", "động từ", "so tài, đọ sức", "两支球队在决赛中展开了激烈的较量。", "Hai đội bóng đã có màn so tài quyết liệt ở trận chung kết.",
     "Động từ, nghĩa là so tài, đọ sức. Chú ý 较量 đọc là jiàoliàng, chữ thứ hai thanh bốn."),
    ("论坛", "lùntán", "luận đàn", "danh từ", "diễn đàn", "他参加了一个国际教育论坛。", "Anh ấy đã tham gia một diễn đàn giáo dục quốc tế.",
     "Danh từ, nghĩa là diễn đàn, cả diễn đàn hội thảo lẫn diễn đàn trên mạng. Tiếng Việt không nói luận đàn mà nói diễn đàn."),
    ("激励", "jīlì", "kích lệ", "động từ", "khích lệ, động viên", "老师的话激励我努力学习。", "Lời thầy khích lệ tôi cố gắng học tập.",
     "Động từ, nghĩa là khích lệ, động viên. Tiếng Việt quen nói khích lệ."),
    ("礼节", "lǐjié", "lễ tiết", "danh từ", "lễ tiết, phép lịch sự", "中国人很讲究礼节。", "Người Trung Quốc rất coi trọng lễ nghĩa.",
     "Danh từ, nghĩa là lễ tiết, phép tắc lịch sự trong giao tiếp."),
    ("衷心", "zhōngxīn", "trung tâm", "tính từ", "chân thành, từ đáy lòng", "衷心感谢大家的帮助！", "Chân thành cảm ơn sự giúp đỡ của mọi người!",
     "Tính từ, nghĩa là chân thành, xuất phát từ đáy lòng. Đây là bẫy lớn: âm Hán Việt cũng là trung tâm, nhưng chữ này là 衷, tấm lòng, chứ không phải 中心, trung tâm. Cả hai đều đọc là zhōngxīn, phải phân biệt bằng chữ viết."),
    ("爱戴", "àidài", "ái đái", "động từ", "yêu kính, kính yêu", "这位老教授深受学生爱戴。", "Vị giáo sư già này được sinh viên hết mực yêu kính.",
     "Động từ, nghĩa là yêu quý và kính trọng, thường dùng cho người dưới đối với người trên như thầy giáo, lãnh tụ."),
    ("示范", "shìfàn", "thị phạm", "động từ", "làm mẫu, nêu gương", "老师先给大家示范了一遍。", "Thầy giáo làm mẫu cho mọi người trước một lượt.",
     "Động từ, nghĩa là làm mẫu, nêu gương, giống thị phạm trong tiếng Việt."),
    ("崇敬", "chóngjìng", "sùng kính", "động từ", "tôn kính, kính trọng", "我们怀着崇敬的心情参观了纪念馆。", "Chúng tôi tham quan nhà tưởng niệm với lòng tôn kính.",
     "Động từ, nghĩa là tôn kính, sùng kính, sắc thái trang trọng."),
    ("偶像", "ǒuxiàng", "ngẫu tượng", "danh từ", "thần tượng", "这位歌手是很多年轻人的偶像。", "Ca sĩ này là thần tượng của rất nhiều bạn trẻ.",
     "Danh từ, nghĩa là thần tượng. Nghĩa gốc là tượng gỗ, tượng đất để thờ cúng."),
    ("封建", "fēngjiàn", "phong kiến", "danh từ", "chế độ phong kiến; phong kiến", "封建社会里，女孩子很难有读书的机会。", "Trong xã hội phong kiến, con gái rất khó có cơ hội đi học.",
     "Danh từ, nghĩa là chế độ phong kiến, âm Hán Việt giống hệt tiếng Việt. Cũng dùng như tính từ: 思想很封建, tư tưởng rất phong kiến."),
]

add("bullets", chapter="Từ mới (50 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 36 có 50 từ mới, chia thành 17 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Cẩn thận bẫy Hán Việt: 衷心 (≠ 中心) · 开展 · 分歧 · 多元化 · 命名"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có năm mươi từ, thầy chia thành mười bảy nhóm nhỏ, mỗi nhóm hai hoặc ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Bài này có rất nhiều từ Hán Việt giống hệt tiếng Việt như 灵魂，干涉，对立，保守，封建. Nhưng cũng có vài cái bẫy, ví dụ 衷心, Hán Việt là trung tâm nhưng nghĩa là chân thành. Thầy sẽ nhắc khi gặp. Chúng ta bắt đầu nhé.")])

sizes = [3] * 16 + [2]
assert sum(sizes) == len(V)
g = 0
for gs in sizes:
    group = V[g:g + gs]
    words, say = [], []
    for i, (zh, py, hv, loai, vi, ex, exvi, expl) in enumerate(group):
        n = g + i + 1
        words.append({"zh": zh, "py": py, "hv": hv.upper(), "loai": f"{n}. {loai}", "vi": vi, "ex": ex, "exvi": exvi})
        say.append(F(i, f"Từ số {n}: {zh}。 {zh}。 Hán Việt là {hv}.", zr=120))
        say.append(F(i, f"{expl} Ví dụ: {ex}{'' if ex[-1] in '。…？！，' else '，'} {exvi[0].upper() + exvi[1:]}{'' if exvi[-1] in '.!?' else '.'}", zr=130))
    add("vocab", section="Từ mới 生词", title=f"Từ mới ({g + 1}–{g + len(group)} / {len(V)})",
        words=words, say=say)
    g += gs

# ======================= BÀI KHÓA =======================
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung nếu khác: số viết bằng chữ Hán])
P = [
    ("中国藏书的历史很长，有2000多年了，有官方藏书，也有私人藏书。",
     "Lịch sử tàng trữ sách của Trung Quốc rất dài, đã hơn 2000 năm; có sách do nhà nước cất giữ, cũng có sách do tư nhân cất giữ.",
     ["藏书 là cất giữ sách, cũng chỉ sách được cất giữ, Hán Việt là tàng thư. 官方藏书 là sách do triều đình cất giữ, còn 私人藏书 là sách do tư nhân cất giữ.",
      "Cấu trúc 有……，也有…… nghĩa là có…, cũng có…, dùng để nêu hai loại. 两千多年 là hơn hai nghìn năm."],
     "中国藏书的历史很长，有两千多年了，有官方藏书，也有私人藏书。"),
    ("唐代有人把藏书的地方称作书院，之后各种书院层出不穷，甚至有人把自己的书屋也命名为书院。",
     "Vào đời Đường, có người gọi nơi cất giữ sách là thư viện; sau đó đủ loại thư viện liên tiếp ra đời, thậm chí có người còn đặt tên cho phòng sách của mình là thư viện.",
     ["把 A 称作 B nghĩa là gọi A là B. 把 A 命名为 B nghĩa là đặt tên cho A là B. Cả hai đều là câu chữ 把 rất hay gặp trong văn viết.",
      "Các bạn để ý: lúc ban đầu, 书院 chỉ là nơi cất sách. Ở đoạn sau, ta sẽ thấy nó dần dần trở thành một cơ sở giáo dục."]),
    ("时光流转，书院渐渐发展成了藏书、教学和研究相结合的教育机构。比如，东佳书院就是中国书院史上最早拥有学田、订有规章制度、收有学生的私办书院。",
     "Thời gian trôi đi, thư viện dần dần phát triển thành cơ sở giáo dục kết hợp tàng trữ sách, giảng dạy và nghiên cứu. Ví dụ, Đông Giai thư viện chính là thư viện tư nhân sớm nhất trong lịch sử thư viện Trung Quốc có học điền, có quy chế và có nhận học trò.",
     ["时光流转 là thời gian trôi đi, 流转 ta vừa gặp ở phần khởi động. ……相结合 là kết hợp với nhau. 机构 là cơ quan, cơ sở.",
      "学田 là học điền. Theo chú thích của sách, đó là ruộng đất dành riêng cho trường học, thu hoạch từ ruộng dùng để trả lương thầy và giúp đỡ người đi học. 订有，收有 là có đặt ra, có thu nhận. 私办 là do tư nhân lập ra."]),
    ("它前后存在了千余年，名字更换了三四次，截止到清朝末年，书院制度终止，东佳书院改成了学校。",
     "Nó tồn tại trước sau hơn một nghìn năm, đổi tên ba bốn lần; tính đến cuối đời nhà Thanh, chế độ thư viện chấm dứt, Đông Giai thư viện được đổi thành trường học.",
     ["千余年 là hơn nghìn năm, 余 nghĩa là hơn, cách nói văn viết. 更换 là thay đổi, thay thế.",
      "Câu này có cả 截止 và 终止: 截止到清朝末年 là tính đến cuối đời Thanh, gắn với một mốc thời gian; còn 书院制度终止 là chế độ thư viện chấm dứt. Đây chính là nội dung của phần phân biệt từ."]),
    ("可以这样说，萌芽于唐，完备于宋，废止于清的东佳书院是中国书院制度的一个缩影。",
     "Có thể nói rằng, Đông Giai thư viện, nảy mầm vào đời Đường, hoàn thiện vào đời Tống, bị bãi bỏ vào đời Thanh, chính là hình ảnh thu nhỏ của chế độ thư viện Trung Quốc.",
     ["Ba cụm 萌芽于唐，完备于宋，废止于清 có cấu trúc giống nhau: động từ, cộng 于, cộng triều đại, nghĩa là… vào đời…. 于 ở đây bằng 在, văn viết. Ba cụm song song tạo nhịp điệu rất đẹp.",
      "缩影 là hình ảnh thu nhỏ. Cả đoạn từ 时光流转 đến 缩影 là một ví dụ mẫu của kỹ năng luận điểm cộng dẫn chứng mà ta học ở cuối bài."]),
    ("历史上的书院立足于人才培养。它把灵魂塑造看得和学问同等重要；提倡刻苦、严谨的治学精神；努力实践自由活泼的办学宗旨。书院的历史是中国古代教育史上的一份珍贵遗产。",
     "Các thư viện trong lịch sử lấy việc đào tạo nhân tài làm nền tảng. Thư viện coi việc hun đúc tâm hồn quan trọng ngang với học vấn; đề cao tinh thần học tập chăm chỉ, nghiêm cẩn; ra sức thực hiện tôn chỉ dạy học tự do, sinh động. Lịch sử thư viện là một di sản quý báu của lịch sử giáo dục cổ đại Trung Quốc.",
     ["立足于 là lấy… làm nền tảng. 把 A 看得和 B 同等重要 là coi A quan trọng ngang với B. 灵魂塑造 là hun đúc tâm hồn, tức giáo dục nhân cách.",
      "治学 là làm học vấn, 办学 là mở trường, tổ chức dạy học. Ba vế nối nhau bằng dấu chấm phẩy cũng chính là ba ý lớn mà các đoạn sau sẽ lần lượt triển khai."]),
    ("德业并重是书院自始至终的追求目标。翻开各时代书院颁布的《学规》就能发现，书院重视学问，更重视品德修养。",
     "Coi trọng cả đạo đức lẫn học nghiệp là mục tiêu theo đuổi từ đầu đến cuối của thư viện. Lật xem bản Học quy do thư viện các thời đại ban bố là có thể thấy, thư viện coi trọng học vấn, nhưng càng coi trọng tu dưỡng đạo đức hơn.",
     ["德业并重: 德 là đạo đức, 业 là học nghiệp, 并重 là coi trọng như nhau. 自始至终 là từ đầu đến cuối.",
      "《学规》 là học quy, tức nội quy học tập của thư viện. Mẫu 重视……，更重视…… là coi trọng…, càng coi trọng… hơn, dùng để nhấn mạnh vế sau. Câu đầu tiên là luận điểm, phần sau sẽ là dẫn chứng."]),
    ("比如，丽泽书院《学规》第一条大意是：凡是本书院的学子，都要孝顺长辈，敬爱兄长，为人忠诚，守信用。",
     "Ví dụ, đại ý điều thứ nhất trong Học quy của Lệ Trạch thư viện là: phàm là học trò của thư viện này, đều phải hiếu thuận với bậc bề trên, kính yêu anh trưởng, sống trung thực, giữ chữ tín.",
     ["凡是 nghĩa là phàm là, hễ là, vế sau thường có 都要 hoặc 都会 đi kèm. 学子 là học trò, cách nói văn viết. 大意 là đại ý.",
      "孝顺长辈 là hiếu thuận với bề trên, 敬爱兄长 là kính yêu anh trưởng, 为人忠诚 là làm người trung thực. Chú ý: trong 为人, chữ đầu đọc là wéi, thanh hai, nghĩa là làm người, cách cư xử."]),
    ("不顺从长辈，和兄弟不友善，与人不和睦，对朋友不忠诚，言行不一，擅以虚伪的言辞掩饰过失的无耻之徒，一经发现，本书院定不容纳。",
     "Những kẻ vô liêm sỉ không vâng lời bề trên, không thân thiện với anh em, không hòa thuận với người khác, không trung thực với bạn bè, nói một đằng làm một nẻo, quen dùng lời lẽ giả dối để che đậy lỗi lầm, hễ bị phát hiện, thư viện này nhất định không dung nạp.",
     ["Sáu vế đầu đều làm định ngữ cho cụm 无耻之徒, kẻ vô liêm sỉ. 之徒 là kẻ, phường, mang nghĩa xấu. 擅以 là quen dùng, giỏi dùng. 言行不一 là lời nói và việc làm không khớp nhau.",
      "一经发现，本书院定不容纳: hễ bị phát hiện thì nhất định không dung nạp. 一经 là điểm ngữ pháp thứ nhất của bài. 定 ở đây là nhất định, bằng 一定."]),
    ("短短一段文字透露出这样的信息：书院在人文环境的治理上是有标准的，那就是树立正气，唾弃卑鄙、堕落的腐败行为。",
     "Đoạn văn ngắn ngủi ấy hé lộ thông tin thế này: thư viện có tiêu chuẩn trong việc quản lý môi trường nhân văn, đó là xây dựng chính khí, ruồng bỏ những hành vi hủ bại hèn hạ, sa đọa.",
     ["短短 là ngắn ngủi, dạng lặp nhấn mạnh. 透露出 là hé lộ ra. 人文环境 là môi trường nhân văn, tức môi trường đạo đức, văn hóa giữa người với người.",
      "那就是…… là đó chính là…, dùng để nói rõ tiêu chuẩn vừa nhắc. Chú ý cặp đối lập: 树立正气, xây dựng chính khí, và 唾弃腐败行为, ruồng bỏ hành vi hủ bại."]),
    ("因此，有学问、有道德、有崇高的境界，就成为了古代知识分子立志终生攀登的道德高峰。",
     "Vì vậy, có học vấn, có đạo đức, có cảnh giới cao cả đã trở thành đỉnh cao đạo đức mà người trí thức thời xưa lập chí suốt đời leo tới.",
     ["Ba cụm 有学问、有道德、有崇高的境界 liệt kê song song. 知识分子 là người trí thức.",
      "立志 là lập chí, quyết chí. 终生 là suốt đời. 攀登高峰 là leo lên đỉnh cao, ở đây dùng theo nghĩa bóng: phấn đấu cả đời để đạt tới."]),
    ("提倡刻苦、严谨的治学精神是古代书院的共同特点。古代书院学术思想各有不同，但治学态度却极为相似，",
     "Đề cao tinh thần học tập chăm chỉ, nghiêm cẩn là đặc điểm chung của các thư viện cổ đại. Tư tưởng học thuật của các thư viện cổ đại mỗi nơi một khác, nhưng thái độ học tập thì lại cực kỳ giống nhau,",
     ["Câu đầu tiên chính là luận điểm của cả đoạn. Các câu tiếp theo là dẫn chứng.",
      "各有不同 là mỗi cái một khác. 却 là nhưng lại, biểu thị chuyển ý. 极为 là cực kỳ, văn viết, giống 非常."]),
    ("认为读书没有窍门，没有捷径，唯有发扬勤奋好学的精神，扎扎实实，一步一个脚印，才能做好学问。",
     "họ cho rằng đọc sách không có mẹo, không có đường tắt, chỉ có phát huy tinh thần cần cù ham học, chắc chắn vững vàng, đi bước nào chắc bước ấy, thì mới làm tốt được học vấn.",
     ["唯有……才能…… là chỉ có… mới có thể…, giống 只有……才…… nhưng trang trọng hơn. 捷径 là đường tắt.",
      "勤奋好学 là cần cù, ham học; trong cụm này, chữ thứ ba đọc là hào, thanh bốn, nghĩa là ham thích. Còn trong 做好学问 thì đọc là hǎo, nghĩa là làm tốt. 一步一个脚印 là mỗi bước một dấu chân, tức là làm chắc chắn từng bước."]),
    ("在学习方法上，提倡读书成诵，因为“书读百遍，其义自见”；提倡温故知新；提倡博学求精；提倡读书须有疑。",
     "Về phương pháp học tập, thư viện đề cao đọc sách đến mức thuộc lòng, vì đọc sách trăm lần thì nghĩa tự hiện ra; đề cao ôn cũ biết mới; đề cao học rộng mà tinh thông; đề cao đọc sách phải biết hoài nghi.",
     ["读书成诵 là đọc sách đến thuộc lòng. 书读百遍，其义自见: đọc trăm lần, nghĩa tự hiện ra; theo chú thích của sách, sách đọc thuộc rồi thì tự nhiên lĩnh hội. Chú ý chữ cuối cùng của câu này đọc là xiàn, nghĩa là hiện ra.",
      "温故知新 là ôn cũ biết mới, xuất phát từ sách 论语, câu gốc là 温故而知新. 博学求精 là học rộng và tinh thông. 读书须有疑 là đọc sách phải biết đặt câu hỏi. Bốn lần lặp lại 提倡 tạo thành phép điệp rất mạnh."]),
    ("书院在办学方法上，努力实践自由活泼的办学思想。首先，书院本着贫富平等的原则，敞开大门，招收平民子弟入学，这在当时确实是令人震撼的开明之举。",
     "Về phương pháp tổ chức dạy học, thư viện ra sức thực hiện tư tưởng dạy học tự do, sinh động. Trước hết, thư viện dựa trên nguyên tắc giàu nghèo bình đẳng, mở rộng cửa, thu nhận con em thường dân vào học; điều này vào thời đó thực sự là một việc làm cởi mở gây chấn động.",
     ["本着……的原则 là dựa trên nguyên tắc…. 本着 là điểm ngữ pháp thứ hai của bài.",
      "敞开大门 là mở toang cửa lớn. 平民子弟 là con em thường dân. 之举 là hành động, việc làm. Từ 首先 mở đầu một chuỗi liệt kê: 首先，其二，其三，其四，另外."]),
    ("其二，书院重视自修和研究，在读书的过程中倡议自行思考，杜绝外来因素的干涉，也不会过多过问，以便开发学生的自主学习能力，激发学生的主动性和创造性。",
     "Thứ hai, thư viện coi trọng tự học và nghiên cứu; trong quá trình đọc sách, khuyến khích tự mình suy nghĩ, ngăn chặn triệt để sự can thiệp từ bên ngoài, cũng không hỏi han quá nhiều, để khai phá năng lực tự học của học trò, khơi dậy tính chủ động và sáng tạo của họ.",
     ["自修 là tự học. 自行思考 là tự mình suy nghĩ. 杜绝外来因素的干涉 là ngăn chặn triệt để sự can thiệp của các yếu tố bên ngoài.",
      "过多过问 là hỏi han, can dự quá nhiều. 以便 là để, nhằm, đứng đầu vế sau để nêu mục đích."]),
    ("其三，鉴于一个人的知识是有限的，大家的知识是无限的，个人解决不了的问题，在众人的智慧面前就不是问题，书院倡导互相切磋、互相学习。",
     "Thứ ba, xét thấy kiến thức của một người là có hạn, còn kiến thức của mọi người là vô hạn, vấn đề mà một cá nhân không giải quyết được thì trước trí tuệ của số đông sẽ không còn là vấn đề, thư viện khuyến khích cùng nhau trao đổi, học hỏi lẫn nhau.",
     ["鉴于 là xét thấy, căn cứ vào, đứng đầu câu để nêu căn cứ. Cặp 有限 và 无限, hữu hạn và vô hạn, đối nhau rất rõ.",
      "切磋 là trao đổi, cùng nhau mài giũa học vấn; nghĩa gốc là cắt và mài ngọc, xương. 倡导 là đề xướng, khởi xướng."]),
    ("其四，鼓励师生之间相互质疑，形成探讨争辩、求真求实的学习风气。另外，重视观点的多元化，开展不同观点的论辩、交流，也是书院提倡的。",
     "Thứ tư, khuyến khích thầy trò chất vấn lẫn nhau, hình thành phong khí học tập thảo luận tranh biện, tìm chân lý và sự thật. Ngoài ra, coi trọng sự đa dạng của quan điểm, tổ chức tranh luận, giao lưu giữa các quan điểm khác nhau, cũng là điều thư viện đề cao.",
     ["质疑 là chất vấn, đặt nghi vấn. 求真求实 là tìm cái thật, cầu sự thực. 风气 là phong khí, nếp chung.",
      "Câu sau có cấu trúc ……，也是书院提倡的, nghĩa là… cũng là điều mà thư viện đề cao. Cách nói này đưa phần nhận xét ra cuối câu để nhấn mạnh."]),
    ("观点对立、有分歧不要紧，开放、保守也无关紧要，书院主张不同学派、不同主张之间的争辩与较量，为此书院设立了讲演辩论制度，类似今天的“论坛”。",
     "Quan điểm đối lập, có bất đồng cũng không sao, cởi mở hay bảo thủ cũng chẳng quan trọng; thư viện chủ trương tranh biện và so tài giữa các học phái, các chủ trương khác nhau; vì thế thư viện đã lập ra chế độ diễn thuyết và tranh luận, giống như diễn đàn ngày nay.",
     ["不要紧 và 无关紧要 đều nghĩa là không sao, không quan trọng. Tác giả dùng hai cách nói khác nhau để tránh lặp từ.",
      "Chú ý 主张 xuất hiện hai lần với hai từ loại: 书院主张 là động từ, chủ trương; 不同主张 là danh từ, quan điểm. 为此 là vì thế, vì mục đích này. 类似 là giống như."]),
    ("这种学术活动很受欢迎，学子们学习热情高涨，相互激励，取长补短，共同进步。",
     "Hoạt động học thuật như vậy rất được hoan nghênh; học trò hăng hái học tập, khích lệ lẫn nhau, lấy sở trường bù sở đoản, cùng nhau tiến bộ.",
     ["热情高涨 là nhiệt tình dâng cao. 取长补短 là lấy cái hay của người bù cho cái dở của mình. Chú ý: trong thành ngữ này, chữ thứ hai đọc là cháng, khác với nhóm từ zhǎng ở phần khởi động."]),
    ("书院讲究长幼，注重礼节，但不拘泥；主张刻苦自励，自主学习，却又鼓励相互质疑、辩论。",
     "Thư viện coi trọng thứ bậc trên dưới, chú trọng lễ tiết nhưng không câu nệ; chủ trương chăm chỉ tự rèn luyện, tự chủ học tập, nhưng lại khuyến khích chất vấn, tranh luận lẫn nhau.",
     ["讲究长幼 là coi trọng thứ bậc người lớn người nhỏ. 拘泥 là câu nệ, cứng nhắc; trong từ này chữ thứ hai đọc là nì, thanh bốn. 自励 là tự khích lệ, tự rèn mình.",
      "Câu này có hai vế, mỗi vế đều có chuyển ý bằng 但 và 却又. Thư viện vừa nghiêm vừa thoáng: có lễ nghĩa nhưng không cứng nhắc, tự học nhưng vẫn tranh luận."]),
    ("书院内师生关系融洽，感情深厚，学生衷心爱戴名师，因为他们学识广博，品德过人，给学生做出了最好的示范，是学生崇敬的偶像。",
     "Trong thư viện, quan hệ thầy trò hòa hợp, tình cảm sâu đậm; học trò thật lòng yêu kính các danh sư, vì họ học thức uyên bác, phẩm đức hơn người, làm tấm gương tốt nhất cho học trò, là thần tượng mà học trò tôn kính.",
     ["融洽 là hòa hợp, êm thấm. 衷心爱戴 là thật lòng yêu kính. 名师 là thầy giỏi, danh sư. 过人 là hơn người.",
      "Các bạn thấy đấy, tôn sư trọng đạo cũng là một truyền thống rất quen thuộc với người Việt chúng ta."]),
    ("书院对中国封建社会教育、学术的发展，产生过重要影响。",
     "Thư viện đã có ảnh hưởng quan trọng đối với sự phát triển giáo dục và học thuật của xã hội phong kiến Trung Quốc.",
     ["对……产生影响 là có ảnh hưởng đối với…. 产生过 biểu thị việc đã từng xảy ra trong quá khứ.",
      "Câu kết rất ngắn gọn, khẳng định lại vai trò của thư viện. Phần vận dụng của sách cũng lấy câu này làm câu mở đầu cho bài viết tóm tắt."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 中国古代书院",
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 中国古代书院, dài một nghìn hai trăm lẻ hai chữ. Bài được cải biên từ một bài báo trên 北京青年报, Báo Thanh niên Bắc Kinh.",
         F(0, "Thầy chia bài thành từng đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 100 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi, cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Tóm tắt nội dung", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5)", size=34,
    items=["## 1. 为什么说书院渐渐发展成了藏书、教学和研究的教育机构？",
           "藏书历史 · 东佳书院：学田、规章制度、学生；唐、宋、清",
           "## 2. 书院怎样立足于人才培养？",
           "提倡刻苦、严谨的治学精神 · 德业并重：重视学问，重视品德修养",
           "## 3. 书院的办学方法是什么？",
           "首先，招收平民子弟入学 · 其二，重视自修和研究 · 其三，倡导互相切磋",
           "其四，鼓励相互质疑 · 另外，重视观点的多元化"],
    say=["Chúng ta cùng nhìn lại bố cục của cả bài khóa. Bài tập năm trong sách gợi ý bố cục này qua ba câu hỏi.",
         F(0, "Câu hỏi một: 为什么说书院渐渐发展成了藏书、教学和研究的教育机构？ Vì sao nói thư viện dần dần phát triển thành cơ sở giáo dục vừa tàng trữ sách, vừa giảng dạy, vừa nghiên cứu?"),
         F(1, "Gợi ý: lịch sử tàng trữ sách, và ví dụ Đông Giai thư viện, có học điền, có quy chế, có học trò, nảy mầm đời Đường, hoàn thiện đời Tống, bãi bỏ đời Thanh."),
         F(2, "Câu hỏi hai: 书院怎样立足于人才培养？ Thư viện lấy việc đào tạo nhân tài làm nền tảng như thế nào?"),
         F(3, "Gợi ý: đề cao tinh thần học tập chăm chỉ, nghiêm cẩn; và coi trọng cả đạo đức lẫn học vấn, tức 德业并重."),
         F(4, "Câu hỏi ba: 书院的办学方法是什么？ Phương pháp dạy học của thư viện là gì?"),
         F(5, "Gợi ý: trước hết, thu nhận con em thường dân vào học; thứ hai, coi trọng tự học và nghiên cứu; thứ ba, khuyến khích trao đổi học hỏi lẫn nhau."),
         F(6, "Thứ tư, khuyến khích chất vấn lẫn nhau; ngoài ra, coi trọng sự đa dạng của quan điểm. Bố cục này rất có ích khi các bạn làm bài viết tóm tắt ở cuối bài.")])

add("bullets", section="Bài khóa 课文", title="Liên hệ Việt Nam: 书院 và Quốc Tử Giám", size=38,
    items=["Văn Miếu (1070) – Quốc Tử Giám (1076): trường của triều đình, giống 官学 (quan học)",
           "书院 phần lớn do tư nhân lập (私办), mở cửa cho 平民子弟 – con em thường dân",
           "Thầy Chu Văn An: mở trường tư ở Huỳnh Cung, sau làm Tư nghiệp Quốc Tử Giám",
           "Điểm chung: tôn sư trọng đạo, 德业并重 – học để làm người"],
    say=["Trước khi sang phần ngữ pháp, chúng ta liên hệ một chút với Việt Nam.",
         F(0, "Ở Hà Nội có Văn Miếu, xây năm một nghìn không trăm bảy mươi, và Quốc Tử Giám, lập năm một nghìn không trăm bảy mươi sáu. Quốc Tử Giám là trường của triều đình, ban đầu dành cho con em vua quan, giống như trường 官学, quan học, của Trung Quốc."),
         F(1, "Còn 书院 trong bài khóa phần lớn do tư nhân lập ra, và điểm tiến bộ nhất là mở cửa cho con em thường dân, không phân biệt giàu nghèo."),
         F(2, "Việt Nam cũng có những trường tư nổi tiếng. Thầy Chu Văn An từng mở trường dạy học ở Huỳnh Cung, học trò rất đông, sau đó mới được mời làm Tư nghiệp ở Quốc Tử Giám."),
         F(3, "Dù là trường công hay trường tư, điểm chung của nền giáo dục xưa ở cả hai nước là tôn sư trọng đạo và coi trọng đạo đức, đúng như tinh thần 德业并重 trong bài: học trước hết là để làm người.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 一经", section="Ngữ pháp 注释", title="1. 一经 yījīng – hễ, một khi đã", size=36,
    items=["Phó từ, dùng ở vế trước: hễ một hành động / bước nào đó được thực hiện, thì sẽ có kết quả tương ứng",
           "Cấu trúc: 一经 + động từ，(就 / 便 / 必须 / 定……) + kết quả",
           "(1) ……擅以虚伪的言辞掩饰过失的无耻之徒，一经发现，本书院定不容纳。",
           "(2) 语言一经产生，又对人类的心理发展起了巨大的推动作用，使人类的心理产生质的飞跃。",
           "(3) ……由领导集团全体成员讨论，做出决策和决定，一经决定，必须共同遵守。"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là phó từ 一经.",
         F(0, "一经 là phó từ, dùng ở vế câu trước. Nó biểu thị: chỉ cần một hành động hay một bước nào đó được thực hiện, thì sẽ dẫn đến kết quả tương ứng. Tiếng Việt dịch là hễ, một khi đã."),
         F(1, "Cấu trúc: 一经 cộng động từ, rồi đến vế sau nêu kết quả, thường có 就，便，必须, hoặc 定 đi kèm. Động từ sau 一经 thường là hai âm tiết, như 发现，决定，推出，发布."),
         F(2, "Ví dụ một, lấy từ bài khóa: 不顺从长辈，和兄弟不友善，与人不和睦，对朋友不忠诚，言行不一，擅以虚伪的言辞掩饰过失的无耻之徒，一经发现，本书院定不容纳。 Những kẻ vô liêm sỉ như vậy, hễ bị phát hiện, thư viện nhất định không dung nạp."),
         F(3, "Ví dụ hai: 语言是人类祖先在社会劳动和社会交往中，出于交流思想、传递信息的需要而产生的。语言一经产生，又对人类的心理发展起了巨大的推动作用，使人类的心理产生质的飞跃。 Ngôn ngữ do tổ tiên loài người tạo ra trong lao động và giao tiếp xã hội. Ngôn ngữ một khi đã ra đời thì lại thúc đẩy mạnh mẽ sự phát triển tâm lý của con người, tạo nên bước nhảy vọt về chất."),
         F(4, "Ví dụ ba: 所谓集体领导，是集体决策、共同负责的制度，即对重大问题，由领导集团全体成员讨论，做出决策和决定，一经决定，必须共同遵守。 Lãnh đạo tập thể là chế độ cùng quyết sách, cùng chịu trách nhiệm: các vấn đề lớn do toàn thể thành viên thảo luận và quyết định, một khi đã quyết định thì phải cùng tuân thủ."),
         "Mẹo nhớ: 一经 gần nghĩa với 一旦, một khi. Nhưng 一经 nhấn mạnh việc đã trải qua một hành động cụ thể, nên phía sau luôn có động từ."])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: chọn cụm từ thích hợp với 一经", reveal=True, size=34,
    items=["## 一经腐败菌和病菌光顾 · 一经推出 · 一经发布",
           "(1) 那一年的8月18日，他的第一张个人专辑______就突破了20万张的销售成绩。",
           "Đáp án: ……他的第一张个人专辑一经推出就突破了20万张的销售成绩。",
           "(2) 据报道，这是国内民间最大的一起知识产权交易，消息______，当即引起轰动。",
           "Đáp án: ……消息一经发布，当即引起轰动。",
           "(3) 许多味美可口的菜肴和食物，______，不消几天甚至几小时，就会变酸变质……",
           "Đáp án: ……一经腐败菌和病菌光顾，不消几天甚至几小时，就会变酸变质。"],
    say=[F(0, "Luyện tập: chọn cụm từ thích hợp điền vào chỗ trống. Ba cụm từ là: 一经腐败菌和病菌光顾，一经推出，一经发布。 Nghĩa là: hễ bị vi khuẩn gây thối và vi khuẩn gây bệnh ghé thăm, hễ được tung ra, và hễ được công bố."),
         F(1, "Câu một: 那一年的八月十八日，他的第一张个人专辑, chỗ trống, 就突破了二十万张的销售成绩。 Ngày mười tám tháng tám năm ấy, album cá nhân đầu tiên của anh ấy, thế nào đó, đã vượt mốc hai mươi vạn bản. Các bạn tạm dừng và chọn thử nhé."),
         F(2, "Đáp án: 一经推出。 他的第一张个人专辑一经推出就突破了二十万张的销售成绩。 Album vừa tung ra đã bán được hơn hai mươi vạn bản. 专辑 là album, 推出 là tung ra, cho ra mắt."),
         F(3, "Câu hai: 据报道，这是国内民间最大的一起知识产权交易，消息, chỗ trống, 当即引起轰动。 Theo tin tức, đây là vụ giao dịch sở hữu trí tuệ lớn nhất trong dân gian ở trong nước, tin tức thế nào đó thì lập tức gây chấn động."),
         F(4, "Đáp án: 一经发布。 消息一经发布，当即引起轰动。 Tin vừa công bố đã lập tức gây chấn động. 当即 là ngay lập tức, 轰动 là chấn động, xôn xao."),
         F(5, "Câu ba: 许多味美可口的菜肴和食物, chỗ trống, 不消几天甚至几小时，就会变酸变质，人吃了就会中毒生病，严重的还会危及生命。 Nhiều món ăn ngon miệng, thế nào đó, chẳng mấy ngày, thậm chí vài giờ, sẽ chua và biến chất, người ăn vào sẽ ngộ độc, nặng thì nguy hiểm đến tính mạng."),
         F(6, "Đáp án: 一经腐败菌和病菌光顾。 Hễ bị vi khuẩn ghé thăm thì thức ăn sẽ nhanh chóng hỏng. 光顾 vốn là khách ghé thăm cửa hàng, ở đây dùng một cách hài hước. 不消 là chẳng cần, chẳng mất.")])

add("bullets", chapter="Ngữ pháp: 本着", section="Ngữ pháp 注释", title="2. 本着 běnzhe – dựa trên, theo (nguyên tắc…)", size=36,
    items=["Giới từ: biểu thị tuân theo một chuẩn mực nào đó",
           "本着 + cụm danh từ; trung tâm ngữ thường là: 原则、精神、宗旨、态度、方针、观点",
           "(1) 书院本着贫富平等的原则，敞开大门，招收平民子弟入学，这在当时确实是令人震撼的开明之举。",
           "(2) 两国谈判代表本着互谅互让、平等协商的精神，解决了拖延多年的问题。",
           "(3) 该公司本着“一切为用户着想，一切为用户服务”的宗旨，积极主动地征求用户意见……"],
    say=["Điểm ngữ pháp thứ hai là giới từ 本着.",
         F(0, "本着 là giới từ, biểu thị việc tuân theo một chuẩn mực nào đó. Tiếng Việt dịch là dựa trên, theo, hoặc với tinh thần."),
         F(1, "Cấu trúc: 本着 cộng một cụm danh từ. Danh từ trung tâm của cụm này thường là 原则，精神，宗旨，态度，方针，观点, tức là nguyên tắc, tinh thần, tôn chỉ, thái độ, phương châm, quan điểm. Các bạn nhớ cả cụm, ví dụ 本着……的原则, 本着……的精神."),
         F(2, "Ví dụ một, lấy từ bài khóa: 书院本着贫富平等的原则，敞开大门，招收平民子弟入学，这在当时确实是令人震撼的开明之举。 Thư viện dựa trên nguyên tắc giàu nghèo bình đẳng, mở rộng cửa thu nhận con em thường dân."),
         F(3, "Ví dụ hai: 两国谈判代表本着互谅互让、平等协商的精神，解决了拖延多年的问题。这充分说明，只要两国有诚意加强沟通，加强合作，没有解决不了的问题。 Đại diện đàm phán hai nước, với tinh thần thông cảm nhân nhượng lẫn nhau, bình đẳng hiệp thương, đã giải quyết vấn đề kéo dài nhiều năm. Điều đó cho thấy chỉ cần có thành ý thì không có vấn đề gì không giải quyết được."),
         F(4, "Ví dụ ba: 该公司本着一切为用户着想，一切为用户服务的宗旨，积极主动地征求用户意见，定期征求经销单位的意见，使他们的产品在市场上越来越受欢迎。 Công ty này theo tôn chỉ mọi thứ vì khách hàng, chủ động lấy ý kiến khách hàng và đại lý, nhờ đó sản phẩm ngày càng được ưa chuộng. 着想 là nghĩ cho, lo cho; chữ đầu đọc là zhuó.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: ghép 6 vế thành 3 câu với 本着", reveal=True, size=34,
    items=["A. 成人教育本着学用结合的原则",
           "B. 把岗位培训和继续教育作为重点，重视搞好从业人员的知识更新",
           "C. 作为一名医生，他一直是本着对患者高度负责的精神",
           "D. 地震过后，全国人民本着“一方有难，八方支持”的精神",
           "E. 对危重病人从不推脱，而是勇于承担风险，积极治病救人",
           "F. 为灾区捐钱、捐物、捐食品",
           "Đáp án: (1) A + B · (2) C + E · (3) D + F"],
    say=[F(0, "Luyện tập: hãy ghép sáu vế câu sau thành ba câu hoàn chỉnh. Vế A: 成人教育本着学用结合的原则。 Giáo dục người lớn dựa trên nguyên tắc học đi đôi với hành."),
         F(1, "Vế B: 把岗位培训和继续教育作为重点，重视搞好从业人员的知识更新。 Lấy đào tạo tại vị trí công tác và giáo dục thường xuyên làm trọng điểm, chú trọng cập nhật kiến thức cho người lao động."),
         F(2, "Vế C: 作为一名医生，他一直是本着对患者高度负责的精神。 Là một bác sĩ, anh ấy luôn làm việc với tinh thần hết mực trách nhiệm với người bệnh."),
         F(3, "Vế D: 地震过后，全国人民本着一方有难，八方支持的精神。 Sau trận động đất, nhân dân cả nước với tinh thần một nơi gặp nạn, tám phương chi viện."),
         F(4, "Vế E: 对危重病人从不推脱，而是勇于承担风险，积极治病救人。 Với bệnh nhân nguy kịch, chưa bao giờ thoái thác, mà dũng cảm gánh vác rủi ro, tích cực chữa bệnh cứu người."),
         F(5, "Vế F: 为灾区捐钱、捐物、捐食品。 Quyên góp tiền, đồ dùng và thực phẩm cho vùng bị thiên tai. Các bạn tạm dừng và thử ghép nhé."),
         F(6, "Đáp án: câu một là A cộng B, nói về giáo dục người lớn. Câu hai là C cộng E, nói về người bác sĩ. Câu ba là D cộng F, nói về động đất và quyên góp. Các bạn thấy đấy, vế có 本着 nêu tinh thần, nguyên tắc; vế sau nêu hành động cụ thể.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 截止 – 终止", section="Phân biệt từ 词语辨析", title="Phân biệt 截止 và 终止",
    common="Giống nhau: đều có nghĩa dừng lại. Ví dụ: 这项活动上个月已经截止/终止了。",
    cols=[{"head": "截止",
           "lines": ["(1) Nhấn mạnh dừng lại khi đến một thời hạn nhất định",
                     "(2) Chỉ kết hợp với từ ngữ chỉ thời gian",
                     "Đúng: 报名的截止日期是10月15号。",
                     "Sai: 截止比赛 / 截止活动 / 截止战争"]},
          {"head": "终止",
           "lines": ["(1) Nhấn mạnh sự kết thúc",
                     "(2) Kết hợp được với nhiều từ ngữ khác",
                     "Đúng: 终止比赛 / 终止活动 / 终止战争",
                     "Đúng: 双方决定终止合同。"]}],
    say=["Tiếp theo là phần phân biệt từ: 截止 và 终止. Hai từ này đều có chữ 止, dừng, và trong bài khóa chúng đứng ngay cạnh nhau, nên rất dễ dùng lẫn.",
         "Điểm giống nhau: cả hai đều có nghĩa dừng lại. Ví dụ: 这项活动上个月已经截止了, hoặc 已经终止了, đều đúng. Hoạt động này tháng trước đã dừng rồi.",
         F(0, "Điểm khác. 截止 nhấn mạnh việc dừng lại khi đến một thời hạn nhất định. Vì vậy nó chỉ kết hợp với từ ngữ chỉ thời gian, như 截止日期, hạn chót, hay 截止到清朝末年, tính đến cuối đời Thanh."),
         F(0, "Ví dụ: 报名的截止日期是十月十五号。 Hạn chót đăng ký là ngày mười lăm tháng mười. Nhưng nói 截止比赛，截止活动，截止战争 là sai, vì 比赛，活动，战争 không phải là thời gian."),
         F(1, "Còn 终止 nhấn mạnh sự kết thúc, và kết hợp được với nhiều từ ngữ khác. 终止比赛，终止活动，终止战争 đều đúng: chấm dứt cuộc thi, chấm dứt hoạt động, chấm dứt chiến tranh."),
         F(1, "Ví dụ thêm: 双方决定终止合同。 Hai bên quyết định chấm dứt hợp đồng. Trong bài khóa: 书院制度终止, chế độ thư viện chấm dứt."),
         "Mẹo nhớ: 截 là chặn, cắt ngang, nên 截止 là cắt ở một mốc thời gian; 终 là cuối cùng, nên 终止 là đi đến hồi kết, dùng cho mọi sự việc."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: Đúng hay sai?", reveal=True, size=36,
    items=["(1) 截止到1998年，公司在15年里已经带来了2056%的回报率。",
           "Đáp án: Đúng – 截止 đi với mốc thời gian 1998年。",
           "(2) 要采取必要的措施，以截止那些错误的、过时的、无效的政策。",
           "Đáp án: Sai – 政策 không phải thời gian. Sửa: 以终止那些……政策。",
           "(3) 当设定好起始日时，系统会自动推算出终止日期。",
           "Đáp án: Đúng – 终止日期 là ngày kết thúc, đi đôi với 起始日。",
           "(4) 婚姻关系终止时，夫妻按照约定分割共有财产。",
           "Đáp án: Đúng – kết thúc một mối quan hệ, dùng 终止。"],
    say=[F(0, "Bây giờ chúng ta làm thử. Câu một: 截止到一九九八年，公司在十五年里已经带来了百分之两千零五十六的回报率。 Tính đến năm một nghìn chín trăm chín mươi tám, trong mười lăm năm công ty đã mang lại tỷ suất lợi nhuận hai nghìn không trăm năm mươi sáu phần trăm. Đúng hay sai? Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: đúng. 截止到 đi với một mốc thời gian là năm một nghìn chín trăm chín mươi tám, nên dùng 截止 là chuẩn."),
         F(2, "Câu hai: 要采取必要的措施，以截止那些错误的、过时的、无效的政策。 Phải áp dụng biện pháp cần thiết để chấm dứt những chính sách sai lầm, lỗi thời, không hiệu quả."),
         F(3, "Đáp án: sai. 政策, chính sách, không phải là thời gian, nên không dùng 截止 được. Phải sửa thành 以终止那些错误的、过时的、无效的政策。"),
         F(4, "Câu ba: 当设定好起始日时，系统会自动推算出终止日期。 Khi đã cài đặt ngày bắt đầu, hệ thống sẽ tự động tính ra ngày kết thúc."),
         F(5, "Đáp án: đúng. 终止日期 là ngày kết thúc, đi đôi với 起始日, ngày bắt đầu. 终止 kết hợp được với nhiều từ, kể cả từ chỉ thời gian. Còn 截止日期 là hạn chót, nghĩa hơi khác."),
         F(6, "Câu bốn: 婚姻关系终止时，夫妻按照约定分割共有财产。 Khi quan hệ hôn nhân chấm dứt, vợ chồng phân chia tài sản chung theo thỏa thuận."),
         F(7, "Đáp án: đúng. Đây là sự kết thúc của một mối quan hệ, không phải một thời hạn, nên dùng 终止 là hợp lý.")])

# ======================= KỸ NĂNG VIẾT =======================
add("bullets", chapter="Kỹ năng viết: luận điểm + dẫn chứng", section="Tu từ 篇章修辞", title="Luận điểm + dẫn chứng (论点 + 例证)", size=34,
    items=["Cách viết văn nghị luận: nêu luận điểm trước, sau đó dùng ví dụ cụ thể để chứng minh",
           "## Ví dụ 1",
           "论点：我们的地球正在不断变暖，这是毋庸置疑的。",
           "例证：IPCC报告：最近100年（1906–2005年）全球平均地表温度上升了0.74℃；过去50年的升温速度几乎是过去100年的2倍。",
           "## Ví dụ 2",
           "论点：面对气候变暖，我们可以从身边的一点一滴做起。",
           "例证：多乘坐公共交通工具 · 调小中央暖气 · 购买节能家电 · 不让电器处于待机状态 · 利用太阳能"],
    say=["Phần cuối cùng về lý thuyết là kỹ năng viết: luận điểm cộng dẫn chứng, tiếng Trung là 论点加例证.",
         F(0, "Đây là cách viết thường dùng trong văn nghị luận: trước hết nêu ra luận điểm, sau đó dùng những ví dụ cụ thể để chứng minh luận điểm đó."),
         F(2, "Ví dụ một. Luận điểm: 我们的地球正在不断变暖，这是毋庸置疑的。 Trái đất của chúng ta đang không ngừng nóng lên, điều đó là không cần nghi ngờ. 毋庸置疑 là không cần phải nghi ngờ."),
         F(3, "Dẫn chứng là số liệu: 政府间气候变化专门委员会第四次评估报告指出，最近一百年，一九零六年至二零零五年，全球平均地表温度上升了零点七四摄氏度。过去五十年的升温速度几乎是过去一百年升温速度的两倍。 Tức là báo cáo của Ủy ban liên chính phủ về biến đổi khí hậu, viết tắt là I P C C, cho biết nhiệt độ trung bình bề mặt trái đất đã tăng không phẩy bảy bốn độ trong một trăm năm, và năm mươi năm gần đây tốc độ tăng nhanh gần gấp đôi."),
         F(5, "Ví dụ hai. Luận điểm: 面对气候变暖，我们可以从身边的一点一滴做起。 Trước tình trạng khí hậu nóng lên, chúng ta có thể bắt đầu từ từng việc nhỏ quanh mình."),
         F(6, "Dẫn chứng là các việc cụ thể: 尽量多乘坐公共交通工具；调小中央暖气，多穿一件衣服；购买家用电器时尽量选择节能家电；电视机和电脑如果不用就关掉，不要让它们处于待机状态；充分利用太阳能。 Đi phương tiện công cộng, vặn nhỏ máy sưởi và mặc thêm áo, chọn đồ điện tiết kiệm năng lượng, tắt hẳn tivi và máy tính khi không dùng, tận dụng năng lượng mặt trời.")])

add("bullets", section="Tu từ 篇章修辞", title="Ví dụ 3: luận điểm + dẫn chứng trong bài khóa", size=36,
    items=["论点：时光流转，书院渐渐发展成了藏书、教学和研究相结合的教育机构。",
           "例证：比如，东佳书院就是中国书院史上最早拥有学田、订有规章制度、收有学生的私办书院……",
           "……萌芽于唐，完备于宋，废止于清的东佳书院是中国书院制度的一个缩影。",
           "Bố cục: luận điểm ở đầu đoạn → dẫn chứng mở đầu bằng 比如 → kết lại bằng 可以这样说"],
    say=["Ví dụ thứ ba lấy ngay từ bài khóa.",
         F(0, "Luận điểm: 时光流转，书院渐渐发展成了藏书、教学和研究相结合的教育机构。 Thư viện dần dần phát triển thành cơ sở giáo dục kết hợp tàng trữ sách, giảng dạy và nghiên cứu."),
         F(1, "Dẫn chứng: 比如，东佳书院就是中国书院史上最早拥有学田、订有规章制度、收有学生的私办书院。 Tác giả lấy ví dụ cụ thể là Đông Giai thư viện, có học điền, có quy chế, có học trò."),
         F(2, "Và kết lại: 可以这样说，萌芽于唐，完备于宋，废止于清的东佳书院是中国书院制度的一个缩影。 Một thư viện cụ thể trở thành hình ảnh thu nhỏ của cả chế độ thư viện."),
         F(3, "Các bạn nhớ bố cục này: luận điểm đặt ở đầu đoạn; dẫn chứng thường mở đầu bằng 比如，例如; cuối cùng có thể kết lại bằng 可以这样说，由此可见. Khi viết đoạn văn nghị luận, hãy làm theo khuôn này, bài viết sẽ rất thuyết phục.")])

add("bullets", section="Tu từ 篇章修辞", title="Luyện tập: tìm luận điểm và dẫn chứng trong bài khóa", reveal=True, size=34,
    items=["(1) Đoạn bắt đầu bằng 德业并重……",
           "Đáp án: 论点：德业并重是书院自始至终的追求目标。例证：丽泽书院《学规》第一条。",
           "(2) Đoạn bắt đầu bằng 提倡刻苦、严谨的治学精神……",
           "Đáp án: 论点：提倡刻苦、严谨的治学精神是古代书院的共同特点。例证：读书没有捷径；读书成诵、温故知新、博学求精、读书须有疑。",
           "(3) Đoạn bắt đầu bằng 书院在办学方法上……",
           "Đáp án: 论点：努力实践自由活泼的办学思想。例证：首先……其二……其三……其四……另外……"],
    say=[F(0, "Luyện tập: sách yêu cầu tìm xem trong bài khóa còn chỗ nào dùng cách luận điểm cộng dẫn chứng. Thứ nhất, đoạn bắt đầu bằng 德业并重. Luận điểm là gì, dẫn chứng là gì? Các bạn tạm dừng và thử tìm nhé."),
         F(1, "Đáp án: luận điểm là 德业并重是书院自始至终的追求目标。 Dẫn chứng là điều thứ nhất trong Học quy của Lệ Trạch thư viện, yêu cầu học trò hiếu thuận, trung thực, và không dung nạp kẻ vô liêm sỉ."),
         F(2, "Thứ hai, đoạn bắt đầu bằng 提倡刻苦、严谨的治学精神."),
         F(3, "Đáp án: luận điểm là 提倡刻苦、严谨的治学精神是古代书院的共同特点。 Dẫn chứng là quan niệm đọc sách không có đường tắt, và bốn phương pháp: 读书成诵，温故知新，博学求精，读书须有疑."),
         F(4, "Thứ ba, đoạn bắt đầu bằng 书院在办学方法上."),
         F(5, "Đáp án: luận điểm là 努力实践自由活泼的办学思想。 Dẫn chứng là năm điểm được liệt kê bằng 首先，其二，其三，其四，另外. Các bạn thấy không, gần như cả bài khóa được viết theo khuôn luận điểm cộng dẫn chứng.")])

add("bullets", section="Tu từ 篇章修辞", title="Bài tập 4: Phân tích luận điểm và dẫn chứng", reveal=True, size=32,
    items=["图书室在很多小学已经名存实亡了。首先，在不少学校，上级下拨的经费中并没有专门的图书经费，而学校自己又实在拿不出钱来购置新书，从而造成藏书少，更新缓慢，许多图书内容陈旧过时，不适合今天的学生阅读这样一种情况。其次，某些学校的经济条件较好，图书室也不错，但这样的学校一般都组织大量的课外活动，同学们把大部分课外时间都用在了参加音乐、舞蹈、美术、电脑培训等活动上，挤不出时间去图书室。另外，大多数小学图书室的工作都是教师兼任，因而开放时间短，图书利用率低。",
           "Đáp án: 论点：图书室在很多小学已经名存实亡了。",
           "Đáp án: 例证 (1) 首先：没有专门的图书经费 → 藏书少，更新缓慢，内容陈旧过时。",
           "Đáp án: 例证 (2) 其次：课外活动多 → 学生挤不出时间去图书室。",
           "Đáp án: 例证 (3) 另外：教师兼任 → 开放时间短，图书利用率低。"],
    say=[F(0, "Bài tập bốn trong sách: hãy phân tích luận điểm và dẫn chứng của đoạn văn sau. Thầy đọc đoạn văn: 图书室在很多小学已经名存实亡了。首先，在不少学校，上级下拨的经费中并没有专门的图书经费，而学校自己又实在拿不出钱来购置新书，从而造成藏书少，更新缓慢，许多图书内容陈旧过时，不适合今天的学生阅读这样一种情况。"),
         F(0, "其次，某些学校的经济条件较好，图书室也不错，但这样的学校一般都组织大量的课外活动，同学们把大部分课外时间都用在了参加音乐、舞蹈、美术、电脑培训等活动上，挤不出时间去图书室。另外，大多数小学图书室的工作都是教师兼任，因而开放时间短，图书利用率低。 Các bạn tạm dừng và thử tìm luận điểm nhé. 名存实亡 là chỉ còn cái tên, thực chất đã mất."),
         F(1, "Đáp án: luận điểm là câu đầu tiên: 图书室在很多小学已经名存实亡了。 Phòng đọc sách ở nhiều trường tiểu học chỉ còn trên danh nghĩa."),
         F(2, "Dẫn chứng thứ nhất, mở đầu bằng 首先: không có kinh phí riêng cho sách, trường lại không có tiền mua sách mới, nên sách ít, cập nhật chậm, nội dung cũ kỹ lỗi thời."),
         F(3, "Dẫn chứng thứ hai, mở đầu bằng 其次: trường có điều kiện thì lại tổ chức quá nhiều hoạt động ngoại khóa, học sinh không còn thời gian đến phòng đọc. 挤不出时间 là không thu xếp được thời gian."),
         F(4, "Dẫn chứng thứ ba, mở đầu bằng 另外: giáo viên làm kiêm nhiệm, nên thời gian mở cửa ngắn, tỷ lệ sử dụng sách thấp. 兼任 là kiêm nhiệm.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ có dấu chấm", size=40,
    items=["官方 (方) → 官方 · 多方 · 我方 · 双方",
           "规章 (规) → 规定 · 规则 · 规范 · 规矩 · 规律",
           "终止 (止) → 停止 · 禁止 · 防止 · 阻止 · 截止",
           "无耻 (耻) → 羞耻 · 可耻 · 廉耻 · 雪耻",
           "树立 (立) → 建立 · 成立 · 设立 · 独立 · 确立"],
    say=["Phần luyện tập. Bài tập một: mô phỏng ví dụ, viết thêm các từ có chứa chữ được đánh dấu chấm ở bên dưới.",
         F(0, "Ví dụ mẫu: 官方, chữ được đánh dấu là chữ thứ hai, 方. Ta có 官方，多方，我方，双方, tức là phía nhà nước, nhiều phía, phía chúng tôi, và hai bên."),
         F(1, "规章, chữ được đánh dấu là chữ đầu, 规. Ta có 规定，规则，规范，规矩，规律, tức là quy định, quy tắc, quy phạm, phép tắc, và quy luật."),
         F(2, "终止, chữ được đánh dấu là 止. Ta có 停止，禁止，防止，阻止，截止, tức là đình chỉ, cấm, phòng ngừa, ngăn cản, và hết hạn."),
         F(3, "无耻, chữ được đánh dấu là 耻, sỉ, xấu hổ. Ta có 羞耻，可耻，廉耻，雪耻, tức là xấu hổ, đáng xấu hổ, liêm sỉ, và rửa nhục."),
         F(4, "树立, chữ được đánh dấu là 立, lập. Ta có 建立，成立，设立，独立，确立, tức là kiến lập, thành lập, thiết lập, độc lập, và xác lập.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (1)", reveal=True, size=38,
    items=["(1) 那颗小行星的名字用的是发现者的名字。（命名）",
           "Đáp án: 那颗小行星是以发现者的名字命名的。",
           "(2) 违反纪律的行为一旦被发现，学校会毫不留情地处理。（一经）",
           "Đáp án: 违反纪律的行为一经发现，学校会毫不留情地处理。",
           "(3) 这就是一种高尚的人道主义精神。（崇高）",
           "Đáp án: 这就是一种崇高的人道主义精神。"],
    say=[F(0, "Bài tập hai: dùng từ cho sẵn để viết lại câu. Câu một, dùng 命名: 那颗小行星的名字用的是发现者的名字。 Tên của tiểu hành tinh ấy là tên của người phát hiện ra nó. Các bạn tạm dừng và thử viết nhé."),
         F(1, "Đáp án: 那颗小行星是以发现者的名字命名的。 Tiểu hành tinh ấy được đặt theo tên người phát hiện. Nhớ mẫu 以……命名, đặt tên theo…."),
         F(2, "Câu hai, dùng 一经: 违反纪律的行为一旦被发现，学校会毫不留情地处理。 Hành vi vi phạm kỷ luật một khi bị phát hiện, nhà trường sẽ xử lý không nương tay."),
         F(3, "Đáp án: thay 一旦被发现 bằng 一经发现: 违反纪律的行为一经发现，学校会毫不留情地处理。 Chú ý: sau 一经 thường không cần chữ 被."),
         F(4, "Câu ba, dùng 崇高: 这就是一种高尚的人道主义精神。 Đây chính là một tinh thần nhân đạo cao thượng."),
         F(5, "Đáp án: 这就是一种崇高的人道主义精神。 Đây chính là một tinh thần nhân đạo cao cả.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (2)", reveal=True, size=38,
    items=["(4) 我们按照互惠互利的原则进行协商。（本着）",
           "Đáp án: 我们本着互惠互利的原则进行协商。",
           "(5) 我们坚决不允许这种腐败行为的发生。（杜绝）",
           "Đáp án: 我们坚决杜绝这种腐败行为的发生。",
           "(6) 真心祝愿你事事顺利、马到成功。（衷心）",
           "Đáp án: 衷心祝愿你事事顺利、马到成功。"],
    say=[F(0, "Câu bốn, dùng 本着: 我们按照互惠互利的原则进行协商。 Chúng tôi hiệp thương theo nguyên tắc cùng có lợi."),
         F(1, "Đáp án: thay 按照 bằng 本着: 我们本着互惠互利的原则进行协商。 互惠互利 là đôi bên cùng có lợi."),
         F(2, "Câu năm, dùng 杜绝: 我们坚决不允许这种腐败行为的发生。 Chúng tôi kiên quyết không cho phép hành vi hủ bại này xảy ra."),
         F(3, "Đáp án: 我们坚决杜绝这种腐败行为的发生。 Chúng tôi kiên quyết ngăn chặn triệt để hành vi hủ bại này."),
         F(4, "Câu sáu, dùng 衷心: 真心祝愿你事事顺利、马到成功。 Thật lòng chúc bạn mọi việc thuận lợi, mã đáo thành công."),
         F(5, "Đáp án: 衷心祝愿你事事顺利、马到成功。 衷心祝愿 là cách chúc rất trang trọng, hay dùng trong thư từ và phát biểu.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ điền vào chỗ trống (1)", reveal=True, size=36,
    items=["## Từ cho sẵn: 发扬 · 树立 · 灵魂 · 品德 · 正气",
           "人们常说，教师是人类___的工程师。老师的___修养和治学精神都会对学生产生深远的影响。因此，老师应该一身___，___严谨扎实的治学精神，为学生___榜样。",
           "Đáp án: 灵魂 · 品德 · 正气 · 发扬 · 树立"],
    say=[F(0, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn một có năm từ: 发扬，树立，灵魂，品德，正气."),
         F(1, "人们常说，教师是人类, chỗ trống, 的工程师。老师的, chỗ trống, 修养和治学精神都会对学生产生深远的影响。因此，老师应该一身, chỗ trống, chỗ trống, 严谨扎实的治学精神，为学生, chỗ trống, 榜样。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 教师是人类灵魂的工程师。老师的品德修养和治学精神都会对学生产生深远的影响。因此，老师应该一身正气，发扬严谨扎实的治学精神，为学生树立榜样。 Người ta thường nói giáo viên là kỹ sư tâm hồn của loài người. Vì vậy thầy cô phải có một thân chính khí, phát huy tinh thần học tập nghiêm cẩn vững chắc, làm tấm gương cho học trò.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ điền vào chỗ trống (2)", reveal=True, size=36,
    items=["## Từ cho sẵn: 敞开 · 对立 · 开明 · 分歧 · 干涉",
           "如果父母过多___孩子的自由，就会使孩子与父母的情绪___日益严重。当家长与孩子的意见出现___时，家长应该采取___的态度，鼓励孩子___心扉，勇敢对父母说出自己的想法。",
           "Đáp án: 干涉 · 对立 · 分歧 · 开明 · 敞开"],
    say=[F(0, "Đoạn hai có năm từ: 敞开，对立，开明，分歧，干涉."),
         F(1, "如果父母过多, chỗ trống, 孩子的自由，就会使孩子与父母的情绪, chỗ trống, 日益严重。当家长与孩子的意见出现, chỗ trống, 时，家长应该采取, chỗ trống, 的态度，鼓励孩子, chỗ trống, 心扉，勇敢对父母说出自己的想法。"),
         F(2, "Đáp án: 如果父母过多干涉孩子的自由，就会使孩子与父母的情绪对立日益严重。当家长与孩子的意见出现分歧时，家长应该采取开明的态度，鼓励孩子敞开心扉，勇敢对父母说出自己的想法。 Nếu cha mẹ can thiệp quá nhiều vào tự do của con, sự đối lập cảm xúc giữa con và cha mẹ sẽ ngày càng nghiêm trọng. Khi có bất đồng, cha mẹ nên có thái độ cởi mở, khuyến khích con mở lòng, mạnh dạn nói ra suy nghĩ của mình. 心扉 là cánh cửa lòng.")])

add("bullets", section="Luyện tập 练习", title="Mở rộng 扩展 (1): kết hợp từ thường gặp", size=34,
    items=["过渡 · 过渡时期 / 过渡地带 – 进入少年期，人的心理发展处于半幼稚、半成熟的过渡状态。",
           "周折 · 大费周折 – 为了进行这次采访，记者颇费了一番周折。",
           "酗酒 · 酗酒滋事 – 年轻人可以少量饮用低度酒，但不要酗酒。",
           "利害 · 不计利害 / 利害得失 – 他们之间一直就有利害冲突。"],
    say=["Phần mở rộng của sách có hai nội dung. Thứ nhất là làm quen với cách kết hợp của tám từ.",
         F(0, "过渡, quá độ, chuyển tiếp: 过渡时期, thời kỳ quá độ; 过渡地带, vùng chuyển tiếp. Ví dụ: 进入少年期，人的心理发展处于半幼稚、半成熟的过渡状态。 Bước vào tuổi thiếu niên, tâm lý con người ở trạng thái chuyển tiếp, nửa non nớt nửa trưởng thành."),
         F(1, "周折, sự trắc trở, quanh co: 大费周折, tốn rất nhiều công sức. Ví dụ: 为了进行这次采访，记者颇费了一番周折。 Để thực hiện cuộc phỏng vấn này, phóng viên đã phải tốn khá nhiều công sức."),
         F(2, "酗酒, rượu chè say sưa: 酗酒滋事, say rượu gây chuyện. Ví dụ: 年轻人可以少量饮用低度酒，但不要酗酒。 Người trẻ có thể uống chút rượu nhẹ, nhưng đừng rượu chè say sưa."),
         F(3, "利害, lợi và hại: 不计利害, không tính toán thiệt hơn; 利害得失, được mất lợi hại. Ví dụ: 他们之间一直就有利害冲突。 Giữa họ luôn có xung đột lợi ích.")])

add("bullets", section="Luyện tập 练习", title="Mở rộng 扩展 (2): kết hợp từ thường gặp", size=34,
    items=["呻吟 · 无病呻吟 – 他躺在床上，满头都是汗，呻吟不止。",
           "人质 · 扣押人质 / 解救人质 – 大家正在想办法，要赎回人质。",
           "声势 · 声势浩大 – 他们的婚礼搞得颇有声势。",
           "野心 · 有野心 / 野心家 – 他从小就野心勃勃，想干一番大事业。"],
    say=[F(0, "呻吟, rên rỉ: 无病呻吟, không bệnh mà rên, tức là than vãn vô cớ. Ví dụ: 他躺在床上，满头都是汗，呻吟不止。 Anh ấy nằm trên giường, mồ hôi đầm đìa, rên rỉ không ngớt."),
         F(1, "人质, con tin: 扣押人质, bắt giữ con tin; 解救人质, giải cứu con tin. Ví dụ: 大家正在想办法，要赎回人质。 Mọi người đang tìm cách chuộc con tin về."),
         F(2, "声势, thanh thế: 声势浩大, thanh thế lớn lao. Ví dụ: 他们的婚礼搞得颇有声势。 Đám cưới của họ tổ chức khá rình rang."),
         F(3, "野心, dã tâm, tham vọng: 有野心, có tham vọng; 野心家, kẻ có dã tâm. Ví dụ: 他从小就野心勃勃，想干一番大事业。 Từ nhỏ cậu ấy đã đầy tham vọng, muốn làm nên sự nghiệp lớn.")])

add("bullets", section="Luyện tập 练习", title="Mở rộng 扩展 (3): nghĩa của từng chữ (语素义)", size=36,
    items=["悬念: 悬 – chưa có kết quả, lơ lửng · 念 – ý nghĩ → sự hồi hộp chờ đợi",
           "剪彩: 剪 – cắt bằng kéo · 彩 – dải lụa màu → cắt băng khánh thành",
           "条理: 条 – trình tự của tư tưởng, lời lẽ, công việc · 理 – vân, thớ → mạch lạc",
           "福利: 福 – hạnh phúc, phúc khí · 利 – lợi ích → phúc lợi",
           "声明: 声 – tuyên bố, bày tỏ · 明 – rõ ràng → tuyên bố công khai",
           "污蔑: 污 – vu cho người khác làm điều xấu · 蔑 – bịa đặt → vu khống"],
    say=["Nội dung mở rộng thứ hai: làm quen với nghĩa của từng chữ trong từ. Nắm được nghĩa từng chữ thì nhớ từ rất nhanh.",
         F(0, "悬念: chữ đầu nghĩa là chưa có kết quả, còn lơ lửng; chữ sau là ý nghĩ. Ghép lại là sự hồi hộp chờ đợi, như 电影充满悬念, bộ phim đầy kịch tính."),
         F(1, "剪彩: chữ đầu là cắt bằng kéo, chữ sau là dải lụa màu. Ghép lại là cắt băng khánh thành."),
         F(2, "条理: chữ đầu chỉ trình tự, tầng lớp của tư tưởng, lời nói, văn chương, công việc; chữ sau là vân, thớ của vật chất. Ghép lại là mạch lạc, có trật tự, như 说话很有条理, nói năng rất mạch lạc."),
         F(3, "福利: chữ đầu là hạnh phúc, phúc khí; chữ sau là lợi ích. Ghép lại là phúc lợi."),
         F(4, "声明: chữ đầu là tuyên bố, bày tỏ; chữ sau là rõ ràng. Ghép lại là tuyên bố công khai, hoặc bản tuyên bố."),
         F(5, "污蔑: chữ đầu là vô cớ nói người khác làm điều xấu; chữ sau là bịa đặt sự thật để làm hại người khác. Ghép lại là vu khống, bôi nhọ.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 36", size=36,
    items=["Từ vựng trọng tâm: 层出不穷 · 截止 · 终止 · 颁布 · 树立 · 唾弃 · 敞开 · 杜绝 · 干涉 · 分歧 · 衷心 · 爱戴",
           "Ngữ pháp: 一经 (hễ, một khi đã + động từ) · 本着 (dựa trên + 原则/精神/宗旨……)",
           "Phân biệt: 截止 (đến thời hạn, chỉ đi với từ chỉ thời gian) ≠ 终止 (kết thúc, kết hợp rộng)",
           "Viết: luận điểm + dẫn chứng – nêu luận điểm trước, dùng ví dụ cụ thể để chứng minh",
           "## Bài tập về nhà",
           "Tham khảo bài tập 5, viết tóm tắt bài khóa khoảng 400 chữ, theo khuôn luận điểm + dẫn chứng"],
    say=["Chúng ta cùng tổng kết bài ba mươi sáu.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 层出不穷，截止，终止，颁布，树立，唾弃，敞开，杜绝，干涉，分歧，衷心，爱戴. Và đừng quên bẫy Hán Việt: 衷心 là chân thành, không phải trung tâm."),
         F(1, "Về ngữ pháp: 一经 là phó từ, nghĩa là hễ, một khi đã, phía sau là động từ, vế sau nêu kết quả. 本着 là giới từ, nghĩa là dựa trên, theo, thường đi với 原则，精神，宗旨."),
         F(2, "Về phân biệt từ: 截止 là dừng lại khi đến thời hạn, chỉ đi với từ chỉ thời gian; 终止 là kết thúc, kết hợp được với nhiều từ."),
         F(3, "Về kỹ năng viết: luận điểm cộng dẫn chứng. Nêu luận điểm ở đầu đoạn, rồi dùng ví dụ cụ thể, số liệu cụ thể để chứng minh."),
         F(5, "Bài tập về nhà: phần vận dụng của sách viết: 书院对中国封建社会教育、学术的发展，产生过重要影响。 Các bạn hãy tham khảo bài tập năm, viết tóm tắt bài khóa thành một đoạn văn khoảng bốn trăm chữ, đi lần lượt ba ý: lịch sử phát triển của thư viện, cách thư viện đào tạo nhân tài, và phương pháp dạy học. Hãy thử dùng 一经 và 本着 trong bài viết nhé."),
         "Như vậy là chúng ta đã học xong bài ba mươi sáu, và cũng hoàn thành toàn bộ Đơn vị chín, chủ đề 古今博览. Cảm ơn các bạn đã theo dõi bài giảng. Hẹn gặp lại các bạn ở bài ba mươi bảy: 警察的故事, Những câu chuyện về cảnh sát, bài mở đầu Đơn vị mười, chủ đề 热点追踪, Theo dõi các vấn đề nóng. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Hạ) – Bài 36: 中国古代书院 (Thư viện cổ đại Trung Quốc)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thứ tự quan trọng: cụm dài trước)
    "tts_replace": {"其义自见": "其义自现",      # xiàn (hiện ra), tránh đọc jiàn
                    "勤奋好学": "勤奋浩学",      # hàoxué, tránh đọc hǎo
                    "取长补短": "取常补短",      # cháng
                    "扎扎实实": "渣渣实实",      # zhāzhāshíshí
                    "扎实": "渣实",              # zhāshi
                    "为人": "维人",              # wéirén
                    "更换": "耕换",              # gēnghuàn
                    "更新": "耕新",              # gēngxīn
                    "长辈": "掌辈",              # zhǎngbèi
                    "兄长": "兄掌",              # xiōngzhǎng
                    "长幼": "掌幼",              # zhǎngyòu
                    "长亲": "掌亲",              # zhǎngqīn
                    "长者": "掌者",              # zhǎngzhě
                    "年长": "年掌",              # niánzhǎng
                    "师长": "师掌",              # shīzhǎng
                    "学长": "学掌",              # xuézhǎng
                    "尊长": "尊掌",              # zūnzhǎng
                    "家长": "家掌",              # jiāzhǎng
                    "透露": "透路",              # tòulù, tránh đọc lòu
                    "较量": "较亮",              # jiàoliàng
                    "拘泥": "拘逆",              # jūnì
                    "着想": "酌想",              # zhuóxiǎng
                    "调小": "条小",              # tiáoxiǎo
                    "处于": "楚于",              # chǔyú
                    "干涉": "甘涉",              # gānshè
                    "干一番": "赣一番",          # gàn
                    "中毒": "众毒"},            # zhòngdú
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai36.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
