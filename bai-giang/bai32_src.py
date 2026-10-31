#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Hạ) – Bài 32 «有时，不妨悲伤». Chạy để sinh bai32.json."""
import json
import os

TAG = "HSK 6 (Hạ) · Bài 32 · 有时，不妨悲伤"
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
    zh="有时，不妨悲伤", py="Yǒushí, bùfáng bēishāng", vi="Bài 32: Đôi khi, cứ buồn cũng được",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Hạ.",
         "Hôm nay chúng ta học bài ba mươi hai: 有时，不妨悲伤。 Nghĩa là: Đôi khi, cứ buồn một chút cũng chẳng sao.",
         "Đây là bài cuối cùng của Đơn vị tám, chủ đề 人体探秘, tức là Khám phá cơ thể người. Bài khóa bàn về một quan niệm rất quen thuộc: đàn ông thì không được khóc. Tác giả sẽ dùng cả kiến thức y học lẫn tâm lý học để chứng minh rằng khóc, nếu đúng lúc và đúng cách, lại rất có lợi cho sức khỏe."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu nội dung bài khóa 有时，不妨悲伤 – vì sao đàn ông cũng nên được khóc",
           "Nắm vững 52 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: liên từ 哪怕 và liên từ 反之",
           "Phân biệt hai động từ 许可 và 允许",
           "Tu từ (8): phép điệp cấu trúc song song (排比)"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa: xã hội đòi hỏi gì ở đàn ông, vì sao đàn ông không dám khóc, và vì sao khóc lại tốt cho sức khỏe."),
         F(1, "Thứ hai, nắm vững năm mươi hai từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học hai liên từ: 哪怕, nghĩa là dù cho, cho dù; và 反之, nghĩa là ngược lại."),
         F(3, "Thứ tư, phân biệt hai động từ đều có nghĩa cho phép: 许可 và 允许."),
         F(4, "Thứ năm, một phép tu từ rất hay dùng trong văn nghị luận và trữ tình: 排比, tức là xếp liền nhau nhiều câu hoặc cụm từ có cấu trúc giống nhau."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Câu hỏi khởi động", size=40,
    items=["中国有句俗话“男儿有泪不轻弹”，你同意吗？",
           "你觉得应该怎样面对悲伤？ – Theo bạn nên đối mặt với nỗi buồn thế nào?",
           "## 怎样面对悲伤 – Đối mặt với nỗi buồn ra sao",
           "找朋友聊天儿 tìm bạn tâm sự · 去旅行 đi du lịch · 购物 mua sắm · 吃东西 ăn uống · 其他 cách khác"],
    say=["Chúng ta bắt đầu bằng phần khởi động. Sách hỏi như sau.",
         F(0, "中国有句俗话，男儿有泪不轻弹，你同意吗？ Trung Quốc có câu tục ngữ: 男儿有泪不轻弹, nghĩa là nam nhi có nước mắt nhưng không dễ để rơi. Bạn có đồng ý không? 俗话 là tục ngữ, câu nói dân gian. Chữ cuối của câu tục ngữ đọc là tán, nghĩa là búng, gạt đi."),
         F(1, "你觉得应该怎样面对悲伤？ Theo bạn, nên đối mặt với nỗi buồn như thế nào? 面对 là đối mặt, 悲伤 là đau buồn."),
         F(3, "Sách gợi ý mấy cách: 找朋友聊天儿，去旅行，购物，吃东西，其他。 Tức là: tìm bạn bè để trò chuyện, đi du lịch, mua sắm, ăn uống, và những cách khác."),
         "Các bạn hãy tạm dừng video, thử nói bằng tiếng Trung, ví dụ: 我难过的时候，喜欢找朋友聊天儿。 Khi buồn, tôi thích tìm bạn bè để trò chuyện. Sau đó hãy xem tiếp nhé."])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 正 và 进", size=36,
    items=["## 正 (chính): ngay thẳng, đúng đắn",
           "正直 chính trực · 正常 bình thường · 正规 chính quy · 正经 đứng đắn · 正路 con đường đúng · 正派 đứng đắn, tử tế",
           "正气 chính khí · 正确 chính xác, đúng · 正式 chính thức · 正义 chính nghĩa · 公正 công bằng · 真正 thực sự",
           "## 进 (tiến): tiến lên, đi vào",
           "上进 cầu tiến · 促进 thúc đẩy · 前进 tiến lên · 先进 tiên tiến · 增进 tăng cường · 进步 tiến bộ · 进程 tiến trình",
           "进度 tiến độ · 进而 tiến thêm · 进化 tiến hóa · 进取 tiến thủ · 进展 tiến triển · 进退 tiến lui · 进行 tiến hành"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo, rất có lợi cho người Việt vì hầu hết các chữ đều có âm Hán Việt quen thuộc.",
         F(0, "Nhóm thứ nhất có chữ chính, như trong từ 正直. Hán Việt là chính, nghĩa là ngay thẳng, đúng đắn."),
         F(1, "正直，正常，正规，正经，正路，正派。 Tức là: chính trực, bình thường, chính quy, đứng đắn, con đường đúng đắn, và tử tế, đứng đắn. Bài khóa có cụm 为人正直, sống ngay thẳng."),
         F(2, "正气，正确，正式，正义，公正，真正。 Tức là: chính khí, đúng đắn, chính thức, chính nghĩa, công bằng, và thực sự. Bài khóa còn có từ 正道, con đường đúng đắn."),
         F(3, "Nhóm thứ hai có chữ 进, Hán Việt là tiến, nghĩa là tiến lên, đi vào."),
         F(4, "上进，促进，前进，先进，增进，进步，进程。 Tức là: cầu tiến, thúc đẩy, tiến lên, tiên tiến, tăng cường, tiến bộ, và tiến trình. Từ 上进 là một từ mới của bài hôm nay."),
         F(5, "进度，进而，进化，进取，进展，进退，进行。 Tức là: tiến độ, tiến thêm một bước, tiến hóa, tiến thủ, tiến triển, tiến lui, và tiến hành.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 视 và 神", size=36,
    items=["## 视 (thị): nhìn, đối xử, coi",
           "鄙视 khinh bỉ · 敌视 thù địch · 忽视 xem nhẹ · 轻视 coi thường · 重视 coi trọng · 无视 phớt lờ · 珍视 trân trọng",
           "正视 nhìn thẳng · 仇视 căm thù · 蔑视 miệt thị · 藐视 khinh thường · 漠视 thờ ơ · 歧视 kỳ thị",
           "## 神 (thần): thần linh",
           "神仙 thần tiên · 神话 thần thoại · 神灵 thần linh · 神人 thần nhân · 神明 thần minh",
           "神像 tượng thần · 神学 thần học · 财神 thần tài · 山神 sơn thần · 天神 thiên thần"],
    say=[F(0, "Nhóm thứ ba có chữ 视, Hán Việt là thị, như trong thị giác. Nghĩa gốc là nhìn, từ đó mở rộng thành coi, đối xử với ai đó."),
         F(1, "鄙视，敌视，忽视，轻视，重视，无视，珍视。 Tức là: khinh bỉ, thù địch, xem nhẹ, coi thường, coi trọng, phớt lờ, và trân trọng. Từ 鄙视 là từ mới quan trọng trong bài khóa."),
         F(2, "正视，仇视，蔑视，藐视，漠视，歧视。 Tức là: nhìn thẳng vào, căm thù, miệt thị, khinh thường, thờ ơ, và kỳ thị. Các bạn để ý: rất nhiều từ trong nhóm này mang nghĩa coi thường người khác."),
         F(3, "Nhóm cuối cùng có chữ 神, Hán Việt là thần, nghĩa là thần linh."),
         F(4, "神仙，神话，神灵，神人，神明。 Tức là: thần tiên, thần thoại, thần linh, người phi thường, và thần minh. Bài khóa có câu 男人不是魔鬼，也不是神仙, đàn ông không phải ma quỷ, cũng chẳng phải thần tiên."),
         F(5, "神像，神学，财神，山神，天神。 Tức là: tượng thần, thần học, thần tài, sơn thần, và thiên thần."),
         "Các bạn thấy không, chỉ cần nắm nghĩa của một chữ gốc, ta có thể đoán được nghĩa của cả một nhóm từ. Hãy áp dụng cách này khi học từ mới nhé."])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng)
V = [
    ("背叛", "bèipàn", "bội bạn", "động từ", "phản bội", "他宁死也不会背叛自己的朋友。", "Anh ấy thà chết cũng không phản bội bạn bè của mình.",
     "Động từ, nghĩa là phản bội. Chữ 叛 Hán Việt là bạn, như trong phản bạn, bạn nghịch, chứ không phải bạn bè. Chú ý: 背叛 đọc là bèipàn, chữ đầu thanh bốn."),
    ("上进", "shàngjìn", "thượng tiến", "động từ", "cầu tiến, chí tiến thủ", "这个年轻人很上进，下班后还去学习。", "Chàng trai trẻ này rất cầu tiến, tan làm rồi vẫn đi học thêm.",
     "Động từ, nghĩa là cầu tiến, luôn muốn vươn lên. Nó thường được dùng như tính từ, đứng sau 很: 很上进, rất cầu tiến."),
    ("抱负", "bàofù", "bão phụ", "danh từ", "hoài bão, chí hướng", "他从小就有远大的抱负。", "Từ nhỏ anh ấy đã có hoài bão lớn lao.",
     "Danh từ, nghĩa là hoài bão, chí hướng lớn. Cụm hay gặp: 远大的抱负, hoài bão lớn lao; 有抱负, có chí hướng."),
    ("魄力", "pòlì", "phách lực", "danh từ", "bản lĩnh, sự quyết đoán", "这位新经理做事很有魄力。", "Vị giám đốc mới làm việc rất quyết đoán, có bản lĩnh.",
     "Danh từ, nghĩa là bản lĩnh, sự quả quyết, dám nghĩ dám làm. Chữ 魄 là phách, như trong khí phách. Cụm hay gặp: 有魄力, có bản lĩnh."),
    ("开阔", "kāikuò", "khai khoát", "tính từ", "rộng, thoáng; (lòng) rộng mở", "他心胸开阔，从不计较小事。", "Anh ấy rộng lượng, không bao giờ so đo chuyện nhỏ.",
     "Tính từ, nghĩa là rộng rãi, thoáng đãng; khi nói về tấm lòng thì là rộng mở, độ lượng. Cụm 心胸开阔 xuất hiện trong bài khóa."),
    ("处境", "chǔjìng", "xử cảnh", "danh từ", "hoàn cảnh, tình cảnh (thường là khó khăn)", "公司现在的处境非常困难。", "Tình cảnh hiện nay của công ty vô cùng khó khăn.",
     "Danh từ, nghĩa là hoàn cảnh, tình cảnh mà một người đang gặp phải, thường là hoàn cảnh không thuận lợi. Chú ý: 处境 đọc là chǔjìng, chữ đầu thanh ba."),
    ("打击", "dǎjī", "đả kích", "động từ", "đánh vào; giáng đòn; cú sốc", "考试失败对他是一个很大的打击。", "Thi trượt là một cú sốc lớn đối với cậu ấy.",
     "Động từ, nghĩa là đánh, giáng đòn; cũng dùng như danh từ chỉ cú sốc, đòn giáng về tinh thần. Cẩn thận: đả kích trong tiếng Việt là chỉ trích, công kích bằng lời nói, còn 打击 thường chỉ cú sốc, nỗi đau mà ai đó phải chịu, hoặc trấn áp, ví dụ 打击犯罪, trấn áp tội phạm."),
    ("脆弱", "cuìruò", "thúy nhược", "tính từ", "mỏng manh, yếu đuối", "生病的时候，人的心理会变得很脆弱。", "Khi ốm, tâm lý con người trở nên rất yếu đuối.",
     "Tính từ, nghĩa là mỏng manh, dễ vỡ, yếu đuối, dùng cho cả đồ vật lẫn tình cảm, tâm lý."),
    ("榜样", "bǎngyàng", "bảng dạng", "danh từ", "tấm gương, hình mẫu", "哥哥一直是我学习的榜样。", "Anh trai luôn là tấm gương để tôi noi theo.",
     "Danh từ, nghĩa là tấm gương, hình mẫu để người khác noi theo. Cụm hay gặp: 做榜样, làm gương; 学习的榜样, tấm gương học tập."),
    ("光彩", "guāngcǎi", "quang thái", "danh từ", "ánh hào quang, vẻ rực rỡ; vẻ vang", "他的成功给家乡增添了光彩。", "Thành công của anh ấy đã làm rạng danh quê hương.",
     "Danh từ, nghĩa là ánh sáng rực rỡ, vẻ vang. Bài khóa có thành ngữ 光彩照人, rạng rỡ chói lọi."),
    ("理智", "lǐzhì", "lý trí", "tính từ", "lý trí, tỉnh táo, biết suy xét", "他是个很理智的人，从不冲动。", "Anh ấy là người rất lý trí, chưa bao giờ bốc đồng.",
     "Âm Hán Việt giống hệt tiếng Việt. Nhưng chú ý, trong bài 理智 là tính từ, nghĩa là tỉnh táo, biết dùng lý trí: 理智的男子汉, người đàn ông lý trí."),
    ("哭泣", "kūqì", "khốc khấp", "động từ", "khóc, khóc thút thít", "她一个人坐在角落里哭泣。", "Cô ấy ngồi khóc một mình trong góc.",
     "Động từ, nghĩa là khóc, thường là khóc nhỏ, khóc thút thít. 哭泣 mang sắc thái văn viết hơn 哭."),
    ("否决", "fǒujué", "phủ quyết", "động từ", "phủ quyết, bác bỏ", "他的建议被大家否决了。", "Đề xuất của anh ấy bị mọi người bác bỏ.",
     "Động từ, nghĩa là phủ quyết, bác bỏ. Bài khóa có cụm 一票否决, chỉ cần một phiếu chống là bị loại."),
    ("出息", "chūxi", "xuất tức", "danh từ", "triển vọng, tiền đồ; nên người", "父母都希望孩子将来有出息。", "Bố mẹ nào cũng mong con sau này nên người, thành đạt.",
     "Danh từ khẩu ngữ, nghĩa là tiền đồ, triển vọng. 有出息 là nên người, thành đạt; 没出息 là chẳng làm nên trò trống gì. Chữ thứ hai đọc nhẹ."),
    ("娃娃", "wáwa", "oa oa", "danh từ", "em bé, trẻ con; búp bê", "这个胖娃娃真可爱。", "Em bé mũm mĩm này thật đáng yêu.",
     "Danh từ, nghĩa là em bé, trẻ nhỏ; cũng có nghĩa là búp bê. Bài khóa có cụm 娃娃时代, thời còn bé tí."),
    ("潜移默化", "qiányí-mòhuà", "tiềm di mặc hóa", "thành ngữ", "ảnh hưởng ngấm ngầm, thầm lặng", "父母的言行对孩子有潜移默化的影响。", "Lời nói, việc làm của bố mẹ ảnh hưởng thầm lặng đến con cái.",
     "Thành ngữ. 潜 là ngầm, 移 là dời đổi, 默 là lặng lẽ, 化 là biến đổi. Ghép lại nghĩa là thay đổi dần dần, ngấm ngầm mà không hề hay biết, thường nói về ảnh hưởng của môi trường, giáo dục."),
    ("鞭策", "biāncè", "tiên sách", "động từ", "thúc giục, thôi thúc", "老师的话一直鞭策着我努力学习。", "Lời thầy dạy luôn thôi thúc tôi chăm chỉ học tập.",
     "Động từ. Nghĩa đen là quất roi cho ngựa chạy, 鞭 là roi; nghĩa bóng là thúc giục, thôi thúc người ta cố gắng."),
    ("赋予", "fùyǔ", "phú dữ", "động từ", "giao cho, trao cho, ban cho", "时代赋予了我们新的使命。", "Thời đại đã trao cho chúng ta sứ mệnh mới.",
     "Động từ, nghĩa là giao cho, trao cho, thường là trao nhiệm vụ, ý nghĩa, hình tượng. Từ trang trọng, dùng trong văn viết."),
    ("扮演", "bànyǎn", "phẫn diễn", "động từ", "đóng vai, sắm vai", "她在电影里扮演一位老师。", "Cô ấy đóng vai một cô giáo trong phim.",
     "Động từ, nghĩa là đóng vai. Nghĩa bóng là giữ vai trò nào đó trong cuộc sống, như 扮演强者, sắm vai kẻ mạnh."),
    ("鄙视", "bǐshì", "bỉ thị", "động từ", "khinh bỉ, coi thường", "大家都鄙视这种不劳而获的人。", "Mọi người đều khinh bỉ loại người không làm mà hưởng.",
     "Động từ, nghĩa là khinh bỉ, coi thường. Chữ 鄙 là bỉ, như trong bỉ ổi."),
    ("讥笑", "jīxiào", "cơ tiếu", "động từ", "chế giễu, chê cười", "不要讥笑别人的缺点。", "Đừng chế giễu khuyết điểm của người khác.",
     "Động từ, nghĩa là chế giễu, cười cợt người khác. Chữ 讥 là cơ, như trong cơ phúng của tiếng Việt cổ, tức là châm biếm."),
    ("恶心", "ěxīn", "ác tâm", "tính từ", "buồn nôn; ghê tởm, đáng ghét", "这种气味让人觉得恶心。", "Mùi này khiến người ta thấy buồn nôn.",
     "Tính từ, nghĩa là buồn nôn, lợm giọng; nghĩa bóng là ghê tởm, đáng ghét. Cẩn thận: ác tâm trong tiếng Việt là lòng dạ độc ác, hoàn toàn khác nghĩa. Từ này đọc là ěxīn."),
    ("体面", "tǐmiàn", "thể diện", "tính từ", "đàng hoàng, tử tế, đáng mặt", "他有一份体面的工作。", "Anh ấy có một công việc đàng hoàng, tử tế.",
     "Tính từ, nghĩa là đàng hoàng, tử tế, coi được. Cẩn thận: thể diện trong tiếng Việt là danh từ chỉ danh dự, sĩ diện, tiếng Trung thường nói là 面子. Còn 体面 ở đây là tính từ."),
    ("含糊", "hánhu", "hàm hồ", "tính từ", "mập mờ, không rõ ràng; qua loa", "这是原则问题，一点儿也不能含糊。", "Đây là vấn đề nguyên tắc, không được qua loa chút nào.",
     "Tính từ, nghĩa là mập mờ, không rõ ràng; hoặc qua loa, đại khái. Cẩn thận: hàm hồ trong tiếng Việt thường là nói bừa, không có căn cứ. Còn 不能含糊 là không được qua loa, phải dứt khoát."),
    ("束缚", "shùfù", "thúc phược", "động từ", "trói buộc, ràng buộc", "不要被旧观念束缚住。", "Đừng để bị những quan niệm cũ trói buộc.",
     "Động từ, nghĩa là trói buộc, ràng buộc. Cũng dùng như danh từ: 一种束缚, một sự ràng buộc, như trong bài khóa."),
    ("魔鬼", "móguǐ", "ma quỷ", "danh từ", "ma quỷ, ác quỷ", "故事里的魔鬼最后被打败了。", "Con quỷ trong truyện cuối cùng đã bị đánh bại.",
     "Danh từ, nghĩa là ma quỷ, âm Hán Việt giống hệt tiếng Việt."),
    ("神仙", "shénxiān", "thần tiên", "danh từ", "thần tiên", "这里风景优美，生活得像神仙一样。", "Ở đây phong cảnh tuyệt đẹp, sống sung sướng như tiên.",
     "Danh từ, nghĩa là thần tiên. 像神仙一样 là sung sướng như tiên."),
    ("健全", "jiànquán", "kiện toàn", "tính từ", "lành mạnh, hoàn chỉnh, đầy đủ", "这家公司的管理制度很健全。", "Chế độ quản lý của công ty này rất hoàn chỉnh.",
     "Tính từ, nghĩa là lành mạnh, hoàn chỉnh, không thiếu sót. Cẩn thận: kiện toàn trong tiếng Việt là động từ, nghĩa là củng cố, sắp xếp lại bộ máy. Còn 健全 ở đây là tính từ: 健全的情感, tình cảm lành mạnh, đầy đủ."),
    ("塌", "tā", "tháp", "động từ", "sập, đổ sụp", "大雨过后，那座旧房子塌了。", "Sau trận mưa lớn, ngôi nhà cũ đó bị sập.",
     "Động từ, nghĩa là sập, đổ sụp. Bài khóa có cụm 被压塌, bị đè sập."),
    ("反之", "fǎnzhī", "phản chi", "liên từ", "ngược lại", "努力就会进步，反之就会落后。", "Cố gắng thì sẽ tiến bộ, ngược lại thì sẽ tụt hậu.",
     "Liên từ, nghĩa là ngược lại, nói theo chiều ngược lại. Đây là điểm ngữ pháp thứ hai của bài."),
    ("激素", "jīsù", "kích tố", "danh từ", "hormone", "压力大的时候，人体会分泌更多激素。", "Khi áp lực lớn, cơ thể sẽ tiết ra nhiều hormone hơn.",
     "Danh từ, nghĩa là hormone, Hán Việt gọi là kích tố. Đây là từ ngoài đề cương, nên sách đánh dấu sao."),
    ("转移", "zhuǎnyí", "chuyển di", "động từ", "chuyển, dời đi; đánh lạc", "他想转移大家的注意力。", "Anh ta muốn đánh lạc hướng sự chú ý của mọi người.",
     "Động từ, nghĩa là chuyển đi, dời đi chỗ khác. 转移注意力 là đánh lạc sự chú ý; 转移压力 là giải tỏa áp lực."),
    ("喉咙", "hóulóng", "hầu lung", "danh từ", "cổ họng", "我感冒了，喉咙很疼。", "Tôi bị cảm, cổ họng rất đau.",
     "Danh từ, nghĩa là cổ họng. Chữ 喉 là hầu, như trong yết hầu."),
    ("鼻涕", "bítì", "tị thế", "danh từ", "nước mũi", "天冷了，孩子一直流鼻涕。", "Trời lạnh, đứa bé cứ chảy nước mũi mãi.",
     "Danh từ, nghĩa là nước mũi. 流鼻涕 là chảy nước mũi."),
    ("之际", "zhījì", "chi tế", "danh từ", "lúc, khi, nhân dịp", "在新年到来之际，祝大家身体健康。", "Nhân dịp năm mới đến, chúc mọi người mạnh khỏe.",
     "Nghĩa là lúc, khi, nhân dịp, dùng trong văn viết. Mẫu thường gặp: ……之际, vào lúc…; 在……之际, nhân dịp…."),
    ("修复", "xiūfù", "tu phục", "động từ", "tu sửa, phục hồi", "工人们正在修复这座古桥。", "Công nhân đang tu sửa cây cầu cổ này.",
     "Động từ, nghĩa là tu sửa, phục hồi như cũ. Dùng cho công trình, đồ vật, và cả cơ thể, tinh thần."),
    ("宣泄", "xuānxiè", "tuyên tiết", "động từ", "giải tỏa, trút ra (cảm xúc)", "运动是宣泄压力的好方法。", "Vận động là cách tốt để giải tỏa áp lực.",
     "Động từ, nghĩa là trút ra, giải tỏa những cảm xúc bị dồn nén. Đây cũng là từ ngoài đề cương có đánh dấu sao."),
    ("许可", "xǔkě", "hứa khả", "động từ", "cho phép, chấp thuận", "没有老师的许可，学生不能离开教室。", "Không có sự cho phép của thầy, học sinh không được rời lớp.",
     "Động từ, nghĩa là cho phép. 许可证 là giấy phép. Lát nữa chúng ta sẽ phân biệt kỹ 许可 với 允许."),
    ("倡导", "chàngdǎo", "xướng đạo", "động từ", "đề xướng, khởi xướng, cổ vũ", "政府倡导绿色出行。", "Chính phủ khuyến khích đi lại xanh, thân thiện với môi trường.",
     "Động từ, nghĩa là đề xướng, cổ vũ mọi người làm theo một việc tốt. Chữ 倡 là xướng, như trong đề xướng."),
    ("情理", "qínglǐ", "tình lý", "danh từ", "lẽ thường, tình lý", "他这样做完全在情理之中。", "Anh ấy làm vậy hoàn toàn hợp tình hợp lý.",
     "Danh từ, nghĩa là lẽ thường tình, tình và lý. Cụm cố định: 在情理之中, hợp tình hợp lý; 不近情理, không hợp lẽ thường."),
    ("忌讳", "jìhuì", "kỵ húy", "động từ", "kiêng kỵ, kiêng; tránh", "中国人过年时忌讳说不吉利的话。", "Người Trung Quốc kiêng nói điều xui xẻo vào dịp Tết.",
     "Động từ, nghĩa là kiêng kỵ; cũng có nghĩa là nên tránh, rất không nên làm điều gì đó, như trong bài: 忌讳哭泣时间过长, tránh khóc quá lâu."),
    ("外界", "wàijiè", "ngoại giới", "danh từ", "bên ngoài, thế giới bên ngoài", "他不太在乎外界的评价。", "Anh ấy không mấy bận tâm đến đánh giá của người ngoài.",
     "Danh từ, nghĩa là bên ngoài, xã hội bên ngoài, những người xung quanh."),
    ("狭隘", "xiá'ài", "hiệp ải", "tính từ", "hẹp; hẹp hòi, thiển cận", "这种想法太狭隘了。", "Cách nghĩ này hẹp hòi quá.",
     "Tính từ, nghĩa gốc là chật hẹp; nghĩa bóng là hẹp hòi, thiển cận. 狭隘的偏见 là định kiến hẹp hòi."),
    ("偏见", "piānjiàn", "thiên kiến", "danh từ", "định kiến, thành kiến", "我们不应该对别人有偏见。", "Chúng ta không nên có định kiến với người khác.",
     "Danh từ, nghĩa là định kiến, cái nhìn thiên lệch. Mẫu hay gặp: 对……有偏见, có định kiến với…."),
    ("阻挠", "zǔnáo", "trở nạo", "động từ", "ngăn cản, cản trở", "父母阻挠他们俩结婚。", "Bố mẹ ngăn cản hai người họ kết hôn.",
     "Động từ, nghĩa là ngăn cản, gây khó dễ để việc gì đó không thành, thường mang nghĩa xấu."),
    ("尊严", "zūnyán", "tôn nghiêm", "danh từ", "phẩm giá, lòng tự trọng", "每个人都有自己的尊严。", "Mỗi người đều có phẩm giá của riêng mình.",
     "Danh từ, nghĩa là phẩm giá, lòng tự trọng. Cẩn thận: tôn nghiêm trong tiếng Việt là tính từ chỉ không khí trang nghiêm, còn 尊严 là phẩm giá. 丧失尊严 là đánh mất phẩm giá."),
    ("理睬", "lǐcǎi", "lý thải", "động từ", "để ý, đếm xỉa đến", "我叫了他好几声，他都不理睬我。", "Tôi gọi mấy lần mà anh ta chẳng thèm để ý.",
     "Động từ, nghĩa là để ý, đếm xỉa đến. Thường dùng ở dạng phủ định: 不理睬, 不必理睬, không thèm để ý."),
    ("淹没", "yānmò", "yêm một", "động từ", "nhấn chìm, ngập", "大水淹没了整个村庄。", "Nước lũ đã nhấn chìm cả ngôi làng.",
     "Động từ, nghĩa là nhấn chìm, làm ngập. Nghĩa bóng là chìm ngập trong cảm xúc nào đó. Chú ý: 淹没 đọc là yānmò, chữ thứ hai thanh bốn, không đọc là méi."),
    ("须知", "xūzhī", "tu tri", "động từ", "phải biết rằng, cần biết", "须知，成功没有捷径。", "Phải biết rằng, thành công không có đường tắt.",
     "Động từ, nghĩa là phải biết rằng, thường đứng đầu câu để nhấn mạnh một điều quan trọng. Làm danh từ thì có nghĩa là điều cần biết, ví dụ 游客须知, những điều du khách cần biết."),
    ("抹杀", "mǒshā", "mạt sát", "động từ", "xóa bỏ, phủ nhận sạch trơn", "谁也不能抹杀他的贡献。", "Không ai có thể phủ nhận công lao của anh ấy.",
     "Động từ, nghĩa là xóa sạch, phủ nhận hoàn toàn. Cẩn thận: mạt sát trong tiếng Việt là chửi bới, sỉ nhục, còn 抹杀 là phủ nhận, xóa bỏ, như 抹杀功劳, phủ nhận công lao."),
    ("岁月", "suìyuè", "tuế nguyệt", "danh từ", "năm tháng", "岁月在她脸上留下了痕迹。", "Năm tháng đã để lại dấu vết trên gương mặt bà.",
     "Danh từ, nghĩa là năm tháng, thời gian, từ mang màu sắc văn chương."),
    ("沉淀", "chéndiàn", "trầm điến", "động từ", "lắng xuống, lắng đọng", "杯子底部沉淀了一层沙子。", "Đáy cốc lắng xuống một lớp cát.",
     "Động từ, nghĩa là lắng xuống, lắng đọng. Nghĩa bóng là tích lũy, đúc kết lại: 沉淀出智慧, lắng đọng thành trí tuệ, như câu kết của bài khóa."),
]

add("bullets", chapter="Từ mới (52 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 32 có 52 từ mới, chia thành 18 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 背叛 (bèi) · 处境 (chǔ) · 恶心 (ě) · 淹没 (mò) · 出息 (xi đọc nhẹ)",
           "Cẩn thận từ giả Hán Việt: 打击 · 恶心 · 体面 · 健全 · 尊严 · 抹杀"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có năm mươi hai từ, thầy chia thành mười tám nhóm nhỏ, mỗi nhóm hai hoặc ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Bài này có một số từ chứa chữ đa âm, như 背叛，处境，恶心，淹没, thầy sẽ nhắc khi gặp."),
         F(4, "Đặc biệt, bài này có khá nhiều từ mà âm Hán Việt dễ gây hiểu lầm, như 打击，恶心，体面，健全，尊严，抹杀. Nghĩa của chúng trong tiếng Trung khác hẳn nghĩa tiếng Việt, các bạn chú ý nhé. Chúng ta bắt đầu.")])

sizes = [3] * 16 + [2, 2]
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
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung nếu khác: số viết bằng chữ Hán])
P = [
    ("到今天为止，我们的社会对好男人的标准从没有改变过：男人要有责任心，为人正直、宽容、刚毅，不背叛朋友；男人要上进，有抱负，有魄力；",
     "Cho đến ngày nay, tiêu chuẩn của xã hội chúng ta về một người đàn ông tốt chưa bao giờ thay đổi: đàn ông phải có tinh thần trách nhiệm, sống ngay thẳng, khoan dung, cương nghị, không phản bội bạn bè; đàn ông phải cầu tiến, có hoài bão, có bản lĩnh;",
     ["到今天为止 nghĩa là cho đến ngày nay. 从没有改变过 nghĩa là chưa từng bao giờ thay đổi, nhấn mạnh tiêu chuẩn này xưa nay vẫn vậy.",
      "为人 là cách làm người, cách đối nhân xử thế: 为人正直, sống ngay thẳng. 刚毅 là cương nghị, cứng rắn kiên định. Các bạn để ý cụm 男人要 lặp đi lặp lại, đây chính là phép 排比 mà ta học ở cuối bài."]),
    ("男人要谦虚，诚实，大方；男人要有修养，心胸开阔，处境艰难而不退缩，面对打击而不脆弱；男人是生活中的榜样，家庭的靠山，社会的支柱。总之，男人要顶天立地，光彩照人，要有男人的气概。",
     "đàn ông phải khiêm tốn, thành thật, hào phóng; đàn ông phải có tu dưỡng, tấm lòng rộng mở, gặp cảnh khó khăn mà không lùi bước, đối mặt với cú sốc mà không yếu đuối; đàn ông là tấm gương trong cuộc sống, là chỗ dựa của gia đình, là trụ cột của xã hội. Tóm lại, đàn ông phải đội trời đạp đất, rạng rỡ chói lọi, phải có khí phách của đàn ông.",
     ["Cấu trúc A 而不 B nghĩa là A mà không B: 处境艰难而不退缩, gặp cảnh khó khăn mà không lùi bước; 面对打击而不脆弱, đối mặt với cú sốc mà không gục ngã.",
      "靠山 là chỗ dựa, 支柱 là trụ cột. 顶天立地 là đầu đội trời chân đạp đất. 光彩照人 là rạng rỡ chói lọi. 气概 là khí khái, khí phách. 总之 là tóm lại."]),
    ("不仅如此，男人们从小受到的教育就是“男儿有泪不轻弹”，意思是说，理智的男子汉再悲伤也不轻易哭泣，爱哭的男人走到哪儿都会被一票否决，",
     "Không chỉ vậy, điều mà đàn ông được dạy từ nhỏ chính là: Nam nhi có nước mắt nhưng không dễ để rơi. Nghĩa là, một đấng nam nhi có lý trí thì dù đau buồn đến đâu cũng không dễ dàng khóc lóc; người đàn ông hay khóc đi đến đâu cũng sẽ bị gạt bỏ ngay,",
     ["不仅如此 là không chỉ như vậy, dùng để bổ sung một ý tiến thêm một bước. 意思是说 là nghĩa là, dùng để giải thích câu tục ngữ.",
      "再……也…… nghĩa là dù… đến mấy cũng…: 再悲伤也不轻易哭泣, dù buồn đến mấy cũng không dễ khóc. 一票否决 nghĩa đen là chỉ một phiếu chống là bị bác bỏ, ở đây nghĩa là bị loại ngay lập tức."]),
    ("因为男人流泪就意味着软弱、没出息，而这种教育是从娃娃时代就潜移默化地在起作用了，他们天天被这样的古训鞭策着。",
     "vì đàn ông rơi lệ đồng nghĩa với yếu đuối, kém cỏi; và kiểu giáo dục này đã âm thầm phát huy tác dụng từ khi họ còn là những đứa trẻ, ngày ngày họ bị lời dạy của người xưa thúc giục như thế.",
     ["意味着 là có nghĩa là, đồng nghĩa với. 没出息 là chẳng làm nên trò trống gì. 起作用 là phát huy tác dụng.",
      "古训 là lời dạy của người xưa. 被这样的古训鞭策着 là câu bị động, có thêm trợ từ chỉ trạng thái kéo dài ở cuối: ngày nào cũng bị thúc giục."]),
    ("我们的文化赋予了男人高大、坚强的形象，他们在生活中必须扮演强者。",
     "Văn hóa của chúng ta đã gán cho đàn ông hình tượng cao lớn, kiên cường; trong cuộc sống họ buộc phải đóng vai kẻ mạnh.",
     ["赋予 cộng người cộng hình tượng: 赋予了男人高大、坚强的形象, trao cho đàn ông một hình tượng cao lớn, kiên cường.",
      "扮演强者 là đóng vai kẻ mạnh. Chữ 扮演 cho thấy đó chỉ là vai diễn, chứ không hẳn là con người thật của họ."]),
    ("男人们为了不被鄙视，不被讥笑，为了远离那些恶心、不体面的词汇，千百次暗暗叮嘱自己：伤心是软弱的表现，哪怕遭受打击、面对失败、受尽委屈，也一定要坚强，这是什么时候都不能含糊的。",
     "Để không bị khinh thường, không bị chế giễu, để tránh xa những từ ngữ đáng ghét, chẳng ra gì kia, đàn ông nghìn trăm lần thầm dặn lòng: đau lòng là biểu hiện của sự yếu đuối; dù có gặp cú sốc, đối mặt với thất bại, chịu đủ mọi oan ức, cũng nhất định phải kiên cường, điều này bất cứ lúc nào cũng không được lơ là.",
     ["为了不被……，不被……，为了远离…… : ba vế chỉ mục đích nối tiếp nhau. 暗暗叮嘱自己 là thầm dặn lòng mình. 受尽委屈 là chịu đủ mọi oan ức, chịu đến tận cùng.",
      "哪怕……也…… là điểm ngữ pháp thứ nhất, nghĩa là dù cho… cũng…. 什么时候都不能含糊 là bất cứ lúc nào cũng không được lơ là, qua loa."]),
    ("实际情况是，“男儿有泪不轻弹”是社会文化赋予男人的一种束缚。男人不是魔鬼，也不是神仙，他们也是有血有肉、有健全情感的人。",
     "Thực tế là, câu Nam nhi có nước mắt nhưng không dễ để rơi là một sự trói buộc mà văn hóa xã hội áp đặt lên đàn ông. Đàn ông không phải ma quỷ, cũng chẳng phải thần tiên, họ cũng là những con người bằng xương bằng thịt, có tình cảm lành mạnh, đầy đủ.",
     ["实际情况是 là thực tế là. Đây là bước ngoặt của bài: từ đây tác giả bắt đầu phản bác quan niệm cũ.",
      "有血有肉 là có máu có thịt, tức là bằng xương bằng thịt, một con người bình thường. 健全情感 là tình cảm lành mạnh, đầy đủ."]),
    ("男人也有喜怒哀乐，也需要关怀，也需要温柔的抚慰，否则，再有力的肩膀也有被压塌的时候。",
     "Đàn ông cũng có vui buồn hờn giận, cũng cần được quan tâm, cũng cần được vỗ về dịu dàng; nếu không, dù bờ vai có vững chắc đến đâu cũng có lúc bị đè sập.",
     ["喜怒哀乐 là hỉ nộ ai lạc, tức là vui, giận, buồn, sướng, chỉ mọi cung bậc cảm xúc. Ba vế 也有……，也需要……，也需要…… cũng là một dạng 排比.",
      "再有力的肩膀也…… là dù bờ vai có vững chắc đến mấy cũng…. 压塌 là đè sập, động từ cộng bổ ngữ kết quả."]),
    ("事实表明，长期的压抑、隐忍对健康只有坏处，没有好处，反之，以适当的方式将情绪释放一下，人的心绪才会变得平和。",
     "Thực tế cho thấy, việc dồn nén, nhẫn nhịn lâu dài chỉ có hại chứ không có lợi cho sức khỏe; ngược lại, giải tỏa cảm xúc một chút bằng cách thích hợp thì tâm trạng con người mới trở nên bình thản.",
     ["事实表明 là thực tế cho thấy. 压抑 là dồn nén, 隐忍 là nén nhịn trong lòng. 只有坏处，没有好处 là chỉ có hại, không có lợi.",
      "反之 là điểm ngữ pháp thứ hai, nghĩa là ngược lại. 以适当的方式 là bằng cách thích hợp. 将情绪释放 cũng giống 把情绪释放, giải tỏa cảm xúc. 心绪 là tâm trạng, tâm tư."]),
    ("其实，眼泪是情绪释放的一种形式，人在情绪抑郁时会分泌一种被称为痛苦激素的物质，它会让人情绪低落、无精打采，眼泪恰恰可以将它排出体外。",
     "Thật ra, nước mắt là một hình thức giải tỏa cảm xúc. Khi tâm trạng u uất, con người sẽ tiết ra một chất được gọi là hormone đau khổ, nó khiến người ta tinh thần sa sút, ủ rũ uể oải, mà nước mắt lại chính là thứ có thể thải chất đó ra ngoài cơ thể.",
     ["抑郁 là u uất, trầm uất. 被称为 là được gọi là. 无精打采 là ủ rũ, uể oải, không có tinh thần.",
      "恰恰 là vừa đúng, chính là, nhấn mạnh sự trùng khớp. 排出体外 là thải ra ngoài cơ thể."]),
    ("通常人们哭泣后，在情绪强度上会降低40%，如果不能利用眼泪把情绪压力转移掉，则会影响身体健康。",
     "Thông thường, sau khi khóc, cường độ cảm xúc của con người sẽ giảm đi 40%; nếu không thể dùng nước mắt để giải tỏa áp lực cảm xúc thì sẽ ảnh hưởng đến sức khỏe.",
     ["在……上 là về mặt…: 在情绪强度上, về mặt cường độ cảm xúc. 降低百分之四十 là giảm bốn mươi phần trăm.",
      "如果……，则…… là nếu… thì…; 则 là cách nói văn viết của 就. 转移掉 là chuyển đi mất, giải tỏa đi."],
     "通常人们哭泣后，在情绪强度上会降低百分之四十，如果不能利用眼泪把情绪压力转移掉，则会影响身体健康。"),
    ("中医认为，忧伤肺。当人难过、想哭的时候，喉咙里会觉得不舒服。喉咙直接通肺，喉咙不舒服，就是肺部受刺激了；",
     "Đông y cho rằng, buồn rầu làm tổn thương phổi. Khi con người buồn bã, muốn khóc, trong cổ họng sẽ thấy khó chịu. Cổ họng thông thẳng với phổi, cổ họng khó chịu tức là phổi bị kích thích;",
     ["忧伤肺 cần hiểu là: 忧, nỗi lo buồn, làm 伤, tổn thương, 肺, phổi. Đây là một quan niệm của Đông y, 中医.",
      "当人难过的时候 là khi con người buồn bã. 通肺 là thông với phổi. 受刺激 là bị kích thích."]),
    ("人哭起来常常会一把鼻涕一把泪，之所以会流鼻涕，也是肺受了刺激。一旦悲伤难过没有了，也就不再流鼻涕了，喉咙也会舒适起来。这说明，悲伤难过对肺会有影响。",
     "Người ta khi khóc thường nước mắt nước mũi tèm lem; sở dĩ chảy nước mũi cũng là do phổi bị kích thích. Một khi nỗi buồn qua đi thì cũng không còn chảy nước mũi nữa, cổ họng cũng dễ chịu trở lại. Điều đó cho thấy, buồn bã có ảnh hưởng đến phổi.",
     ["一把鼻涕一把泪 là nước mắt nước mũi tèm lem, tả cảnh khóc rất nhiều. 哭起来 là bắt đầu khóc.",
      "之所以……，也是…… là sở dĩ… cũng là do…. 一旦……就…… là một khi… thì…. 舒适起来 là trở nên dễ chịu."]),
    ("伤心难过之际，不妨痛哭。哭完了，一切都得到了修复。因此，不发给男人宣泄情绪的许可证不是正道，男人也有流泪的权利。我们倡导要给男人释放情绪的空间，男人流泪本在情理之中。",
     "Khi đau lòng buồn bã, cứ khóc thật to cũng chẳng sao. Khóc xong, mọi thứ đều được phục hồi. Vì vậy, không cấp cho đàn ông giấy phép giải tỏa cảm xúc là không đúng đắn, đàn ông cũng có quyền rơi nước mắt. Chúng tôi đề xướng hãy cho đàn ông không gian để giải tỏa cảm xúc, đàn ông khóc vốn là chuyện hợp tình hợp lý.",
     ["之际 là lúc, khi. 不妨 là cứ việc, chẳng ngại gì, chính là chữ trong tên bài. 痛哭 là khóc thật to, khóc cho thỏa.",
      "许可证 là giấy phép, ở đây là cách nói ẩn dụ. 正道 là con đường đúng đắn. 本在情理之中 là vốn hợp tình hợp lý, 本 ở đây là vốn dĩ."]),
    ("不过，宣泄归宣泄，宣泄时忌讳哭泣时间过长，一般不要超过15分钟，压抑的心情得到发泄、缓解后就不要再哭，否则对身体反而有害。",
     "Tuy nhiên, giải tỏa thì giải tỏa, nhưng khi giải tỏa cần tránh khóc quá lâu, thường không nên quá 15 phút; tâm trạng dồn nén được trút ra, dịu bớt rồi thì đừng khóc nữa, nếu không thì ngược lại còn có hại cho cơ thể.",
     ["A 归 A là mẫu câu rất hay: 宣泄归宣泄, giải tỏa thì giải tỏa, nhưng mà…. Vế trước thừa nhận, vế sau chuyển sang một yêu cầu khác.",
      "忌讳 ở đây là nên tránh. 不要超过十五分钟 là không nên quá mười lăm phút. 反而 là ngược lại, trái lại."],
     "不过，宣泄归宣泄，宣泄时忌讳哭泣时间过长，一般不要超过十五分钟，压抑的心情得到发泄、缓解后就不要再哭，否则对身体反而有害。"),
    ("因为人的胃肠机能对情绪极为敏感，忧愁悲伤或哭泣时间过长，胃的运动会减慢，会影响食欲，甚至引起其他胃部疾病。",
     "Bởi vì chức năng dạ dày, ruột của con người cực kỳ nhạy cảm với cảm xúc; buồn rầu hoặc khóc quá lâu, sự co bóp của dạ dày sẽ chậm lại, ảnh hưởng đến cảm giác thèm ăn, thậm chí gây ra các bệnh khác về dạ dày.",
     ["胃肠机能 là chức năng của dạ dày và ruột. 极为 là vô cùng, cách nói văn viết. 对……敏感 là nhạy cảm với….",
      "胃的运动 là sự co bóp của dạ dày. 食欲 là cảm giác thèm ăn. 甚至 là thậm chí."]),
    ("释放情绪除了哭泣，还应在想法上做调整：扔掉外界对男人流泪的鄙视，因为这种鄙视只是一种狭隘的偏见。",
     "Để giải tỏa cảm xúc, ngoài việc khóc ra còn nên điều chỉnh suy nghĩ: vứt bỏ sự khinh thường của người ngoài đối với việc đàn ông rơi lệ, vì sự khinh thường ấy chỉ là một định kiến hẹp hòi.",
     ["除了哭泣，还应…… là ngoài khóc ra, còn nên…. 在想法上做调整 là điều chỉnh về mặt suy nghĩ.",
      "扔掉 là vứt bỏ. 外界对男人流泪的鄙视 là một cụm danh từ dài: sự khinh thường của bên ngoài đối với việc đàn ông khóc."]),
    ("不要阻挠男人流泪，男人流泪不等于软弱无用，也并不丧失尊严。男人本身也不必理睬别人说三道四，谁都不能长久地淹没在忧伤、难过的情绪中。",
     "Đừng ngăn cản đàn ông rơi nước mắt, đàn ông khóc không có nghĩa là yếu đuối vô dụng, cũng chẳng hề đánh mất phẩm giá. Bản thân đàn ông cũng không cần để ý người khác nói ra nói vào; không ai có thể chìm đắm mãi trong nỗi buồn, trong cảm xúc u sầu.",
     ["不等于 là không đồng nghĩa với. 并不 nhấn mạnh sự phủ định: hoàn toàn không. 丧失尊严 là đánh mất phẩm giá.",
      "说三道四 là nói ra nói vào, bàn tán chê bai. 淹没在忧伤的情绪中 là chìm ngập trong nỗi buồn."]),
    ("偶尔具有负面情绪不是什么坏事，它能让我们更了解自己，让我们成长，让我们更深刻地体悟到什么是快乐。",
     "Thỉnh thoảng có cảm xúc tiêu cực chẳng phải chuyện xấu gì; nó giúp chúng ta hiểu bản thân hơn, giúp chúng ta trưởng thành, giúp chúng ta cảm nhận sâu sắc hơn thế nào là hạnh phúc.",
     ["负面情绪 là cảm xúc tiêu cực. 不是什么坏事 là chẳng phải chuyện xấu gì, chữ 什么 làm nhẹ giọng phủ định.",
      "Ba vế 让我们……，让我们……，让我们…… lại là phép 排比. 体悟 là thấm thía, cảm ngộ."]),
    ("须知，真正的个人成长往往来自于痛苦、磨难，而非快乐，不要抹杀掉痛苦在我们成长中的功劳。",
     "Phải biết rằng, sự trưởng thành thực sự của mỗi người thường đến từ đau khổ, gian nan, chứ không phải từ niềm vui; đừng phủ nhận công lao của nỗi đau trong quá trình trưởng thành của chúng ta.",
     ["须知 là phải biết rằng, đặt ở đầu câu. 来自于 là đến từ. 磨难 là gian nan, khổ ải. 而非 là chứ không phải, cách nói văn viết của 而不是.",
      "抹杀掉 là xóa sạch, phủ nhận. 功劳 là công lao. Tác giả coi nỗi đau như một người có công giúp ta trưởng thành."]),
    ("既然悲伤无可避免，就应该好好面对悲伤，不要妄想生命中从不出现这样的过程和阶段。毕竟，快乐往往是短暂的，人生岁月中更多地伴随着的是灰暗的情绪，而它却可以沉淀出智慧。",
     "Nỗi buồn đã không thể tránh khỏi thì nên đối mặt với nó cho tốt, đừng mơ tưởng rằng trong đời sẽ không bao giờ có những quá trình, những giai đoạn như thế. Dù sao thì niềm vui thường ngắn ngủi; năm tháng đời người phần nhiều là những cảm xúc u ám, nhưng chính nó lại có thể lắng đọng thành trí tuệ.",
     ["既然……就…… là đã… thì…. 无可避免 là không thể tránh khỏi. 妄想 là mơ tưởng hão huyền.",
      "毕竟 là dù sao thì, suy cho cùng. 灰暗 là u ám. 沉淀出智慧 là lắng đọng thành trí tuệ, một hình ảnh rất đẹp để kết bài."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 有时，不妨悲伤",
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 有时，不妨悲伤, dài một nghìn hai trăm sáu mươi tư chữ. Bài được cải biên từ bài báo cùng tên trên tờ 参考消息, Tham khảo Tin tức.",
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
    items=["## 1. 社会对好男人的标准 – tiêu chuẩn đàn ông tốt",
           "男人要……；要……；要……；要……；是……。总之……",
           "## 2. 为什么“男儿有泪不轻弹” – vì sao đàn ông không khóc",
           "理智的男子汉……，爱哭的男人……，流泪意味着…… · 文化赋予男人……",
           "## 3. 为了不被讥笑 – 为了不被……，不被……，为了远离……，叮嘱自己……",
           "## 4. 这种说法对不对 – 束缚，男人不是……，也有……，也需要……，否则……",
           "## 5. 眼泪是情绪释放的形式 – 分泌痛苦激素，眼泪排出，转移压力",
           "## 6. 哭的学问 – 忧伤肺，修复，宣泄，倡导，忌讳过度哭泣，胃肠",
           "## 7. 哭泣以外 – 调整想法：扔掉鄙视，不必理睬，不要抹杀，好好面对"],
    say=["Chúng ta cùng nhìn lại bố cục của cả bài khóa. Bài tập năm trong sách gợi ý đúng bố cục này, gồm bảy câu hỏi.",
         F(0, "Phần một: 社会对好男人的标准是什么？ Tiêu chuẩn của xã hội về người đàn ông tốt là gì?"),
         F(1, "Tác giả liệt kê bằng một loạt câu 男人要, rồi kết lại bằng 总之, đàn ông phải đội trời đạp đất, có khí phách."),
         F(2, "Phần hai: 为什么男儿有泪不轻弹？ Vì sao nam nhi không dễ rơi lệ?"),
         F(3, "Vì người ta cho rằng đàn ông khóc là yếu đuối, chẳng ra gì; kiểu giáo dục này ngấm từ thuở bé, và văn hóa đã gán cho đàn ông hình tượng kẻ mạnh."),
         F(4, "Phần ba: 为了不被讥笑，男人经常怎么办？ Để không bị chế giễu, đàn ông thường làm gì? Họ luôn thầm dặn lòng phải kiên cường."),
         F(5, "Phần bốn: 男儿有泪不轻弹对不对？ Quan niệm ấy đúng hay sai? Tác giả cho rằng đó là một sự trói buộc; đàn ông cũng có cảm xúc, cũng cần được quan tâm."),
         F(6, "Phần năm: 为什么说眼泪是情绪释放的一种形式？ Vì sao nước mắt là một cách giải tỏa cảm xúc? Vì nước mắt thải được hormone đau khổ ra ngoài."),
         F(7, "Phần sáu: 哭有什么学问？ Khóc có những hiểu biết gì? Buồn hại phổi, khóc giúp phục hồi, nhưng không nên khóc quá lâu vì hại dạ dày."),
         F(8, "Phần bảy: 除了哭泣以外，还应该如何释放情绪？ Ngoài khóc ra, còn nên giải tỏa thế nào? Phải điều chỉnh suy nghĩ, bỏ định kiến, và đối mặt với nỗi buồn. Bố cục này rất có ích khi các bạn làm bài tập viết tóm tắt ở cuối bài.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 哪怕", section="Ngữ pháp 注释", title="1. 哪怕 nǎpà – dù cho, cho dù, kể cả", size=38,
    items=["Liên từ, giống 即使: theo sau là một tình huống giả định",
           "Cấu trúc: 哪怕 + giả định，(chủ ngữ) + 也 / 都 + kết quả không đổi · hay dùng trong khẩu ngữ",
           "哪怕遭受打击、面对失败、受尽委屈，也一定要坚强，这是什么时候都不能含糊的。",
           "她真的老了，记忆力越来越差，哪怕两三天以前的事情，也会记不清。",
           "您放心，我们一定会尽全力抢救病人，哪怕只有一线希望。"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là liên từ 哪怕.",
         F(0, "哪怕 là liên từ, nghĩa giống 即使, tiếng Việt dịch là dù cho, cho dù, kể cả. Theo sau 哪怕 là một tình huống giả định."),
         F(1, "Vế còn lại thường có 也会，也要 hoặc 都会, để nói rằng tình huống đó không làm thay đổi kết quả hay kết luận. 哪怕 hay dùng trong khẩu ngữ."),
         F(2, "Ví dụ một, lấy từ bài khóa: 哪怕遭受打击、面对失败、受尽委屈，也一定要坚强，这是什么时候都不能含糊的。 Dù có gặp cú sốc, đối mặt với thất bại, chịu đủ oan ức, cũng nhất định phải kiên cường, điều này lúc nào cũng không được lơ là."),
         F(3, "Ví dụ hai: 她真的老了，记忆力越来越差，哪怕两三天以前的事情，也会记不清。 Bà ấy già thật rồi, trí nhớ ngày càng kém, kể cả chuyện mới hai ba hôm trước cũng nhớ không rõ."),
         F(4, "Ví dụ ba: 您放心，我们一定会尽全力抢救病人，哪怕只有一线希望。 Ông cứ yên tâm, chúng tôi nhất định sẽ dốc toàn lực cứu chữa bệnh nhân, dù chỉ còn một tia hy vọng. Các bạn để ý: vế có 哪怕 có thể đặt ở sau, khi đó không cần 也."),
         "Mẹo nhớ: 哪怕 gần nghĩa với 即使, 就算, 就是, nhưng 哪怕 thường nhấn mạnh một tình huống cực đoan, ít ỏi hoặc khó khăn nhất."])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: dùng 哪怕 viết lại câu", reveal=True, size=38,
    items=["(1) 她这个人真奇怪，走路的时候听音乐，吃饭的时候听音乐，就是看书，也要听音乐。",
           "Đáp án: ……哪怕是看书，也要听音乐。",
           "(2) 渴死了，就算有一口水也是好的。",
           "Đáp án: 渴死了，哪怕有一口水也是好的。",
           "(3) 说好了啊，即使晚点儿，你也一定要来。",
           "Đáp án: 说好了啊，哪怕晚点儿，你也一定要来。"],
    say=[F(0, "Luyện tập: dùng 哪怕 viết lại câu. Câu một: 她这个人真奇怪，走路的时候听音乐，吃饭的时候听音乐，就是看书，也要听音乐。 Cô ấy thật kỳ lạ, đi đường cũng nghe nhạc, ăn cơm cũng nghe nhạc, ngay cả đọc sách cũng phải nghe nhạc. Các bạn hãy tạm dừng và thử viết lại nhé."),
         F(1, "Đáp án: thay 就是 bằng 哪怕: 哪怕是看书，也要听音乐。 Kể cả khi đọc sách, cũng phải nghe nhạc."),
         F(2, "Câu hai: 渴死了，就算有一口水也是好的。 Khát chết đi được, dù chỉ có một ngụm nước thôi cũng tốt."),
         F(3, "Đáp án: thay 就算 bằng 哪怕: 渴死了，哪怕有一口水也是好的。"),
         F(4, "Câu ba: 说好了啊，即使晚点儿，你也一定要来。 Hứa rồi nhé, dù có muộn một chút, cậu cũng nhất định phải đến."),
         F(5, "Đáp án: thay 即使 bằng 哪怕: 说好了啊，哪怕晚点儿，你也一定要来。 Qua bài này các bạn thấy, 哪怕 có thể thay cho 就是，就算，即使 trong câu giả định nhượng bộ.")])

add("bullets", chapter="Ngữ pháp: 反之", section="Ngữ pháp 注释", title="2. 反之 fǎnzhī – ngược lại", size=38,
    items=["Liên từ: nói từ phía ngược lại, dẫn ra ý trái với ý phía trước",
           "Dùng giữa các câu, các đoạn, có tác dụng chuyển ý · sau 反之 có ngắt (dấu phẩy)",
           "事实表明，长期的压抑、隐忍对健康只有坏处，没有好处，反之，以适当的方式将情绪释放一下，人的心绪才会变得平和。",
           "有些东西，越是一心想要得到，越是不能如愿，反之，不去在意的时候倒会有意外来临。",
           "经济发展了，百姓的收入增加了，消费能力就强，反之，百姓的消费能力就差。"],
    say=["Điểm ngữ pháp thứ hai là liên từ 反之.",
         F(0, "反之 là liên từ, nghĩa là nói từ phía ngược lại, tiếng Việt dịch là ngược lại, trái lại. Nó dẫn ra một ý trái ngược với ý ở phía trước."),
         F(1, "反之 dùng giữa các câu hoặc các đoạn văn, có tác dụng chuyển ý. Sau 反之 luôn có một chỗ ngắt, khi viết thì dùng dấu phẩy."),
         F(2, "Ví dụ một, lấy từ bài khóa: 事实表明，长期的压抑、隐忍对健康只有坏处，没有好处，反之，以适当的方式将情绪释放一下，人的心绪才会变得平和。 Dồn nén lâu dài thì có hại; ngược lại, giải tỏa đúng cách thì tâm trạng mới bình thản."),
         F(3, "Ví dụ hai: 有些东西，越是一心想要得到，越是不能如愿，反之，不去在意的时候倒会有意外来临。 Có những thứ càng một lòng muốn có thì càng không được như ý; ngược lại, lúc không để tâm đến thì lại bất ngờ tìm đến."),
         F(4, "Ví dụ ba: 经济发展了，百姓的收入增加了，消费能力就强，反之，百姓的消费能力就差。 Kinh tế phát triển, thu nhập người dân tăng thì sức tiêu dùng mạnh; ngược lại thì sức tiêu dùng của người dân sẽ kém."),
         "Các bạn để ý: vế sau 反之 thường chỉ nêu kết quả ngược lại, còn điều kiện ngược lại thì người đọc tự hiểu, không cần nhắc lại."])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: dùng 反之 hoàn thành câu", reveal=True, size=38,
    items=["(1) 雨水多，气候就比较湿润，反之，___。",
           "Đáp án: ……反之，气候就比较干燥。",
           "(2) 有了充足的阳光、水分和空气，植物就能生长好，反之，___。",
           "Đáp án: ……反之，植物就很难生长，甚至会枯死。",
           "(3) 不断地积累，经验就会丰富起来，反之，___。",
           "Đáp án: ……反之，经验就永远不会丰富。"],
    say=[F(0, "Luyện tập. Câu một: 雨水多，气候就比较湿润，反之， Mưa nhiều thì khí hậu tương đối ẩm ướt, ngược lại thì sao? Các bạn hãy tạm dừng và thử hoàn thành câu."),
         F(1, "Đáp án gợi ý: 反之，气候就比较干燥。 Ngược lại, khí hậu sẽ khá khô hanh."),
         F(2, "Câu hai: 有了充足的阳光、水分和空气，植物就能生长好，反之， Có đủ ánh nắng, nước và không khí thì cây cối sẽ phát triển tốt, ngược lại thì sao?"),
         F(3, "Đáp án gợi ý: 反之，植物就很难生长，甚至会枯死。 Ngược lại, cây sẽ khó phát triển, thậm chí chết khô."),
         F(4, "Câu ba: 不断地积累，经验就会丰富起来，反之， Không ngừng tích lũy thì kinh nghiệm sẽ phong phú lên, ngược lại thì sao?"),
         F(5, "Đáp án gợi ý: 反之，经验就永远不会丰富。 Ngược lại, kinh nghiệm sẽ mãi mãi không phong phú được. Các bạn có thể có đáp án khác, miễn là ý của vế sau trái ngược với vế trước.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 许可 – 允许", section="Phân biệt từ 词语辨析", title="Phân biệt 许可 và 允许",
    common="Giống nhau: đều là động từ, nghĩa là cho phép. Ví dụ: 得到许可/允许，方可入内。",
    cols=[{"head": "许可",
           "lines": ["(1) Phía sau không mang tân ngữ",
                     "Sai: 他许可我在这儿拍照。",
                     "Đúng: 我在这儿拍照得到了他的许可。",
                     "(2) Bổ nghĩa được cho danh từ",
                     "Đúng: 许可证"]},
          {"head": "允许",
           "lines": ["(1) Phía sau mang được tân ngữ",
                     "Đúng: 他允许我在这儿拍照。",
                     "(2) Không bổ nghĩa cho danh từ",
                     "Sai: 允许证"]}],
    say=["Tiếp theo là phần phân biệt từ: 许可 và 允许. Hai từ này đều có chữ 许, nên rất dễ dùng lẫn.",
         "Điểm giống nhau: cả hai đều là động từ, đều có nghĩa là cho phép. Ví dụ: 得到许可，方可入内, hoặc 得到允许，方可入内, đều đúng. Được cho phép thì mới được vào. 方可 là mới được, cách nói văn viết.",
         F(0, "Điểm khác thứ nhất. Phía sau 许可 không mang tân ngữ. Vì vậy câu 他许可我在这儿拍照 là sai."),
         F(0, "Muốn dùng 许可, ta phải biến nó thành danh từ: 我在这儿拍照得到了他的许可。 Tôi chụp ảnh ở đây đã được anh ấy cho phép."),
         F(1, "Còn 允许 thì mang được tân ngữ, cả một cụm phía sau: 他允许我在这儿拍照。 Anh ấy cho phép tôi chụp ảnh ở đây."),
         F(0, "Điểm khác thứ hai. 许可 có thể đứng trước để bổ nghĩa cho danh từ, như 许可证, giấy phép, mà bài khóa vừa dùng."),
         F(1, "Còn 允许 không bổ nghĩa cho danh từ, nên không có từ 允许证."),
         "Mẹo nhớ: 允许 là động từ thông dụng, theo mẫu ai đó 允许 ai làm gì; còn 许可 trang trọng hơn, hay đi với 得到，经过，未经, và tạo thành danh từ 许可证."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: Đúng hay sai?", reveal=True, size=38,
    items=["(1) 私人物品，未经许可，不得动用。",
           "Đáp án: Đúng – 许可 không mang tân ngữ, dùng sau 未经.",
           "(2) 学校有明文规定：教室里不许可抽烟。",
           "Đáp án: Sai – 许可 không mang tân ngữ. Sửa: 教室里不允许抽烟。",
           "(3) 妈妈允许我每天玩儿半个小时游戏。",
           "Đáp án: Đúng – 允许 mang tân ngữ.",
           "(4) 公司的经营允许证终于申请下来了。",
           "Đáp án: Sai – 允许 không bổ nghĩa cho danh từ. Sửa: 经营许可证。"],
    say=[F(0, "Bây giờ chúng ta làm thử. Câu một: 私人物品，未经许可，不得动用。 Đồ dùng cá nhân, chưa được cho phép thì không được động vào. Đúng hay sai? Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: đúng. 未经许可 là chưa được cho phép, 许可 đứng một mình, không mang tân ngữ."),
         F(2, "Câu hai: 学校有明文规定：教室里不许可抽烟。 Nhà trường có quy định rõ ràng: trong lớp học không được hút thuốc."),
         F(3, "Đáp án: sai. 抽烟 là tân ngữ, mà 许可 không mang tân ngữ. Phải sửa thành: 教室里不允许抽烟。"),
         F(4, "Câu ba: 妈妈允许我每天玩儿半个小时游戏。 Mẹ cho phép tôi mỗi ngày chơi game nửa tiếng."),
         F(5, "Đáp án: đúng. 允许 mang cả một cụm tân ngữ phía sau."),
         F(6, "Câu bốn: 公司的经营允许证终于申请下来了。 Giấy phép kinh doanh của công ty cuối cùng cũng xin được rồi."),
         F(7, "Đáp án: sai. 允许 không bổ nghĩa cho danh từ, phải nói là 经营许可证, giấy phép kinh doanh.")])

# ======================= TU TỪ =======================
add("bullets", chapter="Tu từ: 排比", section="Tu từ 篇章修辞", title="Tu từ (8): Phép điệp cấu trúc song song (排比)", size=34,
    items=["Xếp liền nhau các từ ngữ / câu có cấu trúc giống nhau, nội dung liên quan, ngữ khí thống nhất → khí thế mạnh, hiệu quả diễn đạt tốt",
           "Dùng để lập luận (说理): quan điểm chặt chẽ, thấu đáo · Dùng để trữ tình (抒情): cảm xúc dâng trào, đầy đủ",
           "(1) 蔚蓝的天空，飘浮的白云，摇摆的树影，更衬托出梯田的壮美。",
           "(2) 没有理想，人生就如荒漠，没有生气；没有理想，人生就如黑夜，没有光明；没有理想，人生就如迷宫，没有方向。",
           "(3) 男人要有责任心，为人正直、宽容、刚毅，不背叛朋友；男人要上进，有抱负，有魄力；男人要谦虚，诚实，大方……"],
    say=["Phần cuối cùng về lý thuyết là tu từ số tám: 排比. Tiếng Việt có thể gọi là phép điệp cấu trúc, hay liệt kê song song.",
         F(0, "排比 là xếp liền nhau những từ ngữ hoặc câu có cấu trúc giống nhau, nội dung liên quan, ngữ khí thống nhất. Cách này làm cho khí thế câu văn mạnh hơn, hiệu quả diễn đạt tốt hơn."),
         F(1, "Câu 排比 hay dùng để lập luận, gọi là 说理, khi đó quan điểm được trình bày chặt chẽ, thấu đáo; hoặc để trữ tình, gọi là 抒情, khi đó cảm xúc được bộc lộ dâng trào, trọn vẹn."),
         F(2, "Ví dụ một: 蔚蓝的天空，飘浮的白云，摇摆的树影，更衬托出梯田的壮美。 Bầu trời xanh thẳm, mây trắng bồng bềnh, bóng cây đung đưa, càng làm nổi bật vẻ hùng vĩ của ruộng bậc thang. Ba cụm 蔚蓝的天空，飘浮的白云，摇摆的树影 có cùng một cấu trúc."),
         F(3, "Ví dụ hai: 没有理想，人生就如荒漠，没有生气；没有理想，人生就如黑夜，没有光明；没有理想，人生就如迷宫，没有方向。 Không có lý tưởng, đời người như sa mạc, không có sức sống; như đêm đen, không có ánh sáng; như mê cung, không có phương hướng. Ba vế lặp lại cùng một khuôn."),
         F(4, "Ví dụ ba, chính là đoạn mở đầu bài khóa: 男人要有责任心……男人要上进……男人要谦虚…… Cụm 男人要 lặp lại nhiều lần, liệt kê mọi tiêu chuẩn, tạo cảm giác áp lực đè nặng lên vai người đàn ông."),
         "Khi viết, các bạn hãy thử dùng ba vế song song có cùng cấu trúc, đoạn văn sẽ có nhịp điệu và sức thuyết phục hơn hẳn."])

add("bullets", section="Tu từ 篇章修辞", title="Luyện tập: câu nào không phải câu 排比?", reveal=True, size=36,
    items=["(1) 床前明月光，疑是地上霜，举头望明月，低头思故乡。",
           "(2) 拥有青春，就拥有了一份灿烂和辉煌；拥有知识，就拥有了无限的力量和财富；拥有友情，就拥有了一份理解和支持。",
           "(3) 处理问题必须瞻前顾后，不仅要看到眼前，还要看到以后；不仅要看到局部，还要看到全局；不仅要了解中国国情，还要了解世界局势……",
           "Đáp án: câu (1) – không có các vế cùng cấu trúc lặp lại; (2) và (3) là câu 排比"],
    say=[F(0, "Luyện tập: chỉ ra câu nào không phải câu 排比. Câu một: 床前明月光，疑是地上霜，举头望明月，低头思故乡。 Đây là bài thơ Tĩnh dạ tứ nổi tiếng của Lý Bạch: Đầu giường ánh trăng rọi, ngỡ mặt đất phủ sương, ngẩng đầu nhìn trăng sáng, cúi đầu nhớ cố hương."),
         F(1, "Câu hai: 拥有青春，就拥有了一份灿烂和辉煌；拥有知识，就拥有了无限的力量和财富；拥有友情，就拥有了一份理解和支持。 Có tuổi trẻ là có rực rỡ huy hoàng; có tri thức là có sức mạnh và của cải vô hạn; có tình bạn là có sự thấu hiểu và ủng hộ."),
         F(2, "Câu ba: 处理问题必须瞻前顾后，不仅要看到眼前，还要看到以后；不仅要看到局部，还要看到全局；不仅要了解中国国情，还要了解世界局势。 Giải quyết vấn đề phải nhìn trước ngó sau, không chỉ thấy trước mắt mà còn thấy về sau, không chỉ thấy cục bộ mà còn thấy toàn cục, không chỉ hiểu tình hình Trung Quốc mà còn hiểu cục diện thế giới. Các bạn tạm dừng và suy nghĩ nhé."),
         F(3, "Đáp án: câu một không phải câu 排比. Bốn câu thơ tuy đối nhau rất chỉnh, nhưng không có ba vế trở lên lặp lại cùng một khuôn. Câu hai lặp khuôn 拥有……，就拥有了……; câu ba lặp khuôn 不仅要……，还要……, nên đều là câu 排比.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ được đánh dấu", size=40,
    items=["否决 (否) → 否认 · 否定 · 是否 · 可否",
           "光彩 (光) → 光明 · 光荣 · 光辉 · 光线",
           "赋予 (予) → 给予 · 授予 · 赠予 · 准予",
           "讥笑 (笑) → 嘲笑 · 取笑 · 耻笑 · 微笑",
           "鄙视 (视) → 轻视 · 歧视 · 无视 · 重视"],
    say=["Phần luyện tập. Bài tập một: mô phỏng ví dụ, dựa vào chữ có dấu chấm bên dưới để viết thêm các từ khác. Các bạn chú ý, chữ được đánh dấu có khi là chữ đầu, có khi là chữ sau.",
         F(0, "Ví dụ mẫu: 否决, chữ được đánh dấu là chữ đầu. Có 否认，否定，是否，可否. Tức là phủ nhận, phủ định, có hay không, và có thể hay không."),
         F(1, "光彩, chữ đánh dấu là chữ đầu, nghĩa là ánh sáng. Có 光明，光荣，光辉，光线. Tức là quang minh, vẻ vang, huy hoàng, và tia sáng."),
         F(2, "赋予, chữ đánh dấu là chữ sau, nghĩa là cho, trao. Có 给予，授予，赠予，准予. Tức là dành cho, trao tặng danh hiệu, tặng, và chuẩn y cho phép."),
         F(3, "讥笑, chữ đánh dấu là chữ sau, nghĩa là cười. Có 嘲笑，取笑，耻笑，微笑. Tức là chế nhạo, trêu chọc, cười chê, và mỉm cười."),
         F(4, "鄙视, chữ đánh dấu là chữ sau. Có 轻视，歧视，无视，重视. Tức là coi thường, kỳ thị, phớt lờ, và coi trọng. Nhóm này các bạn đã gặp ở phần khởi động rồi.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Dùng từ cho sẵn viết lại câu (1)", reveal=True, size=36,
    items=["(1) 老一辈教育家强调：“教育要从小孩子抓起”。（娃娃）",
           "Đáp án: 老一辈教育家强调：“教育要从娃娃抓起”。",
           "(2) 他这种不劳而获的行为被大多数人瞧不起。（鄙视）",
           "Đáp án: 他这种不劳而获的行为被大多数人鄙视。",
           "(3) 由于智力有问题，他从小就经常被村里的孩子们笑话。（讥笑）",
           "Đáp án: 由于智力有问题，他从小就经常被村里的孩子们讥笑。"],
    say=[F(0, "Bài tập hai: dùng từ cho sẵn để viết lại câu. Câu một, dùng 娃娃: 老一辈教育家强调，教育要从小孩子抓起。 Các nhà giáo dục thế hệ trước nhấn mạnh: giáo dục phải bắt đầu từ khi còn nhỏ. Các bạn tạm dừng và thử làm nhé."),
         F(1, "Đáp án: thay 小孩子 bằng 娃娃: 教育要从娃娃抓起。 Đây là một câu khẩu hiệu rất nổi tiếng ở Trung Quốc. 抓起 ở đây là bắt tay vào làm từ…."),
         F(2, "Câu hai, dùng 鄙视: 他这种不劳而获的行为被大多数人瞧不起。 Hành vi không làm mà hưởng của anh ta bị đa số mọi người coi thường."),
         F(3, "Đáp án: thay 瞧不起 bằng 鄙视: 他这种不劳而获的行为被大多数人鄙视。 Chú ý: 瞧不起 là khẩu ngữ, còn 鄙视 trang trọng hơn và nghĩa nặng hơn."),
         F(4, "Câu ba, dùng 讥笑: 由于智力有问题，他从小就经常被村里的孩子们笑话。 Vì trí tuệ có vấn đề, từ nhỏ cậu ấy thường bị lũ trẻ trong làng cười nhạo."),
         F(5, "Đáp án: thay 笑话 bằng 讥笑: 他从小就经常被村里的孩子们讥笑。")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Dùng từ cho sẵn viết lại câu (2)", reveal=True, size=36,
    items=["(4) 衣服只要干净就行，就算旧点儿也没关系。（哪怕）",
           "Đáp án: 衣服只要干净就行，哪怕旧点儿也没关系。",
           "(5) 一切从实际出发，我们的事业就能顺利发展，相反，就会遇到挫折。（反之）",
           "Đáp án: ……我们的事业就能顺利发展，反之，就会遇到挫折。",
           "(6) 为了不让那两家公司成功合作，他想尽办法进行阻止。（阻挠）",
           "Đáp án: 他想尽办法阻挠那两家公司成功合作。"],
    say=[F(0, "Câu bốn, dùng 哪怕: 衣服只要干净就行，就算旧点儿也没关系。 Quần áo chỉ cần sạch sẽ là được, dù có cũ một chút cũng không sao."),
         F(1, "Đáp án: thay 就算 bằng 哪怕: 衣服只要干净就行，哪怕旧点儿也没关系。"),
         F(2, "Câu năm, dùng 反之: 一切从实际出发，我们的事业就能顺利发展，相反，就会遇到挫折。 Mọi việc đều xuất phát từ thực tế thì sự nghiệp của chúng ta sẽ phát triển thuận lợi, ngược lại thì sẽ gặp trắc trở."),
         F(3, "Đáp án: thay 相反 bằng 反之: 我们的事业就能顺利发展，反之，就会遇到挫折。 挫折 là trắc trở, thất bại."),
         F(4, "Câu sáu, dùng 阻挠: 为了不让那两家公司成功合作，他想尽办法进行阻止。 Để hai công ty kia không hợp tác thành công, anh ta tìm mọi cách ngăn cản."),
         F(5, "Đáp án: 他想尽办法阻挠那两家公司成功合作。 Anh ta tìm mọi cách cản trở hai công ty kia hợp tác thành công. Các bạn thấy, 阻挠 mang sắc thái xấu, đúng với hành động cố tình phá hoại này.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống", reveal=True, size=34,
    items=["## Từ cho sẵn: 开阔 · 背叛 · 榜样 · 打击 · 上进",
           "(1) 爸爸一直是我的___，他很坚强，面对___从不退缩；他为人正直，从不___朋友；他心胸___，积极___，是个顶天立地的男子汉。",
           "Đáp án: 榜样 · 打击 · 背叛 · 开阔 · 上进",
           "## Từ cho sẵn: 脆弱 · 喉咙 · 忌讳 · 鼻涕 · 修复",
           "(2) 最近我的身体不太舒服，___痛，还打喷嚏，流___，可能是感冒了。生病时身体很___，也最___过于劳累，因此我打算减少工作量，去父母家住几天，好好休息，让身体进行自我___。",
           "Đáp án: 喉咙 · 鼻涕 · 脆弱 · 忌讳 · 修复"],
    say=[F(0, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn một có năm từ: 开阔，背叛，榜样，打击，上进."),
         F(1, "爸爸一直是我的什么，他很坚强，面对什么从不退缩；他为人正直，从不什么朋友；他心胸什么，积极什么，是个顶天立地的男子汉。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 爸爸一直是我的榜样，他很坚强，面对打击从不退缩；他为人正直，从不背叛朋友；他心胸开阔，积极上进，是个顶天立地的男子汉。 Bố luôn là tấm gương của tôi; bố rất kiên cường, gặp cú sốc không bao giờ lùi bước; bố sống ngay thẳng, không bao giờ phản bội bạn bè; bố rộng lượng, luôn cầu tiến, là một người đàn ông đội trời đạp đất."),
         F(3, "Đoạn hai có năm từ: 脆弱，喉咙，忌讳，鼻涕，修复."),
         F(4, "最近我的身体不太舒服，什么痛，还打喷嚏，流什么，可能是感冒了。生病时身体很什么，也最什么过于劳累，因此我打算减少工作量，去父母家住几天，好好休息，让身体进行自我什么。"),
         F(5, "Đáp án: 喉咙痛，流鼻涕，身体很脆弱，最忌讳过于劳累，让身体进行自我修复。 Dạo này tôi không khỏe, đau họng, hắt hơi, chảy nước mũi, có lẽ bị cảm. Khi ốm cơ thể rất yếu, kỵ nhất là làm việc quá sức, nên tôi định giảm bớt việc, về nhà bố mẹ ở vài hôm để cơ thể tự phục hồi. 打喷嚏 là hắt hơi.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 4: Nối thành đoạn văn 排比", reveal=True, size=36,
    items=["(1) 大理花多，  (2) 大理花艳，  (3) 大理花娇，  (4) 大理花香，",
           "A. 娇得文学家想不出词句来描绘。",
           "B. 香得外来人一到这苍山下，洱海边，顿觉飘飘然不酒而醉。",
           "C. 多得园艺家定不出名字来称呼。",
           "D. 艳得美术家调不出颜色来点染。",
           "Đáp án: (1) – C · (2) – D · (3) – A · (4) – B"],
    say=[F(0, "Bài tập bốn: nối các vế sau thành một đoạn văn 排比 rồi đọc to. Bốn vế đầu là: 大理花多，大理花艳，大理花娇，大理花香。 Hoa Đại Lý nhiều, hoa Đại Lý rực rỡ, hoa Đại Lý kiều diễm, hoa Đại Lý thơm."),
         F(1, "Vế A: 娇得文学家想不出词句来描绘。 Kiều diễm đến mức nhà văn không nghĩ ra lời để miêu tả."),
         F(2, "Vế B: 香得外来人一到这苍山下，洱海边，顿觉飘飘然不酒而醉。 Thơm đến mức người nơi khác vừa đến chân núi Thương Sơn, bên hồ Nhĩ Hải, liền thấy lâng lâng như say mà chẳng cần rượu."),
         F(3, "Vế C: 多得园艺家定不出名字来称呼。 Nhiều đến mức nhà làm vườn không đặt nổi tên để gọi."),
         F(4, "Vế D: 艳得美术家调不出颜色来点染。 Rực rỡ đến mức họa sĩ không pha nổi màu để tô điểm. Các bạn tạm dừng và thử nối nhé."),
         F(5, "Đáp án: một nối C, hai nối D, ba nối A, bốn nối B. Mẹo: chữ đầu của mỗi vế sau lặp lại tính từ của vế trước, theo mẫu 多得，艳得，娇得，香得, tức là đến mức nào đó. Cả đoạn đọc lên là: 大理花多，多得园艺家定不出名字来称呼；大理花艳，艳得美术家调不出颜色来点染；大理花娇，娇得文学家想不出词句来描绘；大理花香，香得外来人一到这苍山下，洱海边，顿觉飘飘然不酒而醉。")])

add("bullets", section="Luyện tập 练习", title="Mở rộng 扩展: từ ngữ và cách kết hợp (1)", size=34,
    items=["出卖 bán đứng – 出卖朋友 / 出卖情报 · 他绝不会为金钱、利益出卖良心。",
           "煎 rán, sắc – 煎茶 / 煎药 · 不知从哪里飘来了煎牛排的香味。",
           "捎 gửi nhờ – 捎话 / 捎件衣服 · 麻烦您把这几样东西捎给我妹妹。",
           "秃 trụi – 光秃秃 · 天气暖和了，光秃秃的树枝上冒出了新芽。",
           "磨合 làm quen, ăn ý dần – 磨合期 · 经过一段时间的磨合，他们俩的双打配合得别提多默契了。",
           "渣 bã, vụn – 面包渣 · 这种再生纤维是用木材、竹子、甘蔗渣等天然物质制成的。",
           "染 nhuộm – 染发 · 她家从来都是窗明几净，纤尘不染。"],
    say=["Phần mở rộng của sách giới thiệu mười lăm từ cùng cách kết hợp thường gặp. Thầy đọc qua để các bạn làm quen.",
         F(0, "出卖, bán đứng: 出卖朋友，出卖情报, bán đứng bạn bè, bán tin tình báo. 他绝不会为金钱、利益出卖良心。 Anh ấy tuyệt đối không bán rẻ lương tâm vì tiền bạc, lợi ích."),
         F(1, "煎, rán, sắc: 煎茶，煎药, sắc trà, sắc thuốc. 不知从哪里飘来了煎牛排的香味。 Chẳng biết từ đâu bay tới mùi bít tết rán thơm phức."),
         F(2, "捎, gửi nhờ, mang hộ: 捎话，捎件衣服, nhắn lời, mang hộ cái áo. 麻烦您把这几样东西捎给我妹妹。 Phiền anh mang hộ mấy thứ này cho em gái tôi."),
         F(3, "秃, trụi: 光秃秃, trơ trụi. 天气暖和了，光秃秃的树枝上冒出了新芽。 Trời ấm lên, trên những cành cây trơ trụi đã nhú mầm non."),
         F(4, "磨合, mài cho khớp, tức là dần dần ăn ý: 磨合期, giai đoạn làm quen. 经过一段时间的磨合，他们俩的双打配合得别提多默契了。 Sau một thời gian tập luyện cùng nhau, hai người đánh đôi ăn ý khỏi phải nói."),
         F(5, "渣, bã, vụn: 面包渣, vụn bánh mì. 这种再生纤维是用木材、竹子、甘蔗渣等天然物质制成的。 Loại sợi tái sinh này được làm từ gỗ, tre, bã mía và các chất tự nhiên khác."),
         F(6, "染, nhuộm: 染发, nhuộm tóc. 她家从来都是窗明几净，纤尘不染。 Nhà cô ấy lúc nào cũng cửa sáng bàn sạch, không một hạt bụi. 窗明几净 là cửa sổ sáng sủa, bàn ghế sạch sẽ.")])

add("bullets", section="Luyện tập 练习", title="Mở rộng 扩展: từ ngữ và cách kết hợp (2)", size=34,
    items=["壮烈 oanh liệt – 壮烈牺牲 · 他们的爱情注定是悲剧，是带有壮烈色彩的悲剧。",
           "辩证 biện chứng – 辩证法 · 要注意培养学生的辩证思维能力。",
           "公关 quan hệ công chúng – 公关部门 / 公关活动 · “公关”是“公共关系”的简称。",
           "纪要 biên bản tóm tắt – 新闻纪要 / 会议纪要 · 这是一份完整的会议纪要。",
           "清真 Hồi giáo – 清真寺 / 清真食品 · 我最喜欢这家清真饭馆了。",
           "蒸发 bốc hơi – 水分蒸发 · 天气炎热，刚下过雨，路上的水马上就蒸发了。",
           "片断 đoạn, mẩu – 文章片断 / 生活片断 · 我对这件事的记忆已经不完整了，只是一个个的片断。",
           "集团 tập đoàn – 集团公司 · 几家报社联合起来，组建了一个大的报业集团。"],
    say=[F(0, "壮烈, oanh liệt: 壮烈牺牲, hy sinh oanh liệt. 他们的爱情注定是悲剧，是带有壮烈色彩的悲剧。 Tình yêu của họ định sẵn là bi kịch, một bi kịch mang màu sắc bi tráng."),
         F(1, "辩证, biện chứng: 辩证法, phép biện chứng. 要注意培养学生的辩证思维能力。 Cần chú ý bồi dưỡng năng lực tư duy biện chứng cho học sinh."),
         F(2, "公关, quan hệ công chúng: 公关部门，公关活动. 公关是公共关系的简称。 公关 là cách nói tắt của 公共关系."),
         F(3, "纪要, biên bản tóm tắt: 新闻纪要，会议纪要. 这是一份完整的会议纪要。 Đây là một bản tóm tắt cuộc họp đầy đủ."),
         F(4, "清真, thuộc về Hồi giáo: 清真寺 là nhà thờ Hồi giáo, 清真食品 là thực phẩm Halal. 我最喜欢这家清真饭馆了。 Tôi thích nhất quán ăn Hồi giáo này."),
         F(5, "蒸发, bốc hơi: 水分蒸发. 天气炎热，刚下过雨，路上的水马上就蒸发了。 Trời nóng bức, vừa mưa xong mà nước trên đường đã bốc hơi hết."),
         F(6, "片断, đoạn, mẩu: 文章片断，生活片断. 我对这件事的记忆已经不完整了，只是一个个的片断。 Ký ức của tôi về chuyện này không còn trọn vẹn, chỉ là từng mảnh rời rạc."),
         F(7, "集团, tập đoàn: 集团公司. 几家报社联合起来，组建了一个大的报业集团。 Mấy tòa soạn liên kết lại, thành lập một tập đoàn báo chí lớn.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 32", size=36,
    items=["Từ vựng trọng tâm: 背叛 · 魄力 · 打击 · 潜移默化 · 鞭策 · 赋予 · 鄙视 · 束缚 · 宣泄 · 忌讳 · 抹杀 · 沉淀",
           "Ngữ pháp: 哪怕……也/都…… (dù cho) · 反之 (ngược lại)",
           "Phân biệt: 许可 (không mang tân ngữ, 许可证) ≠ 允许 (mang tân ngữ)",
           "Tu từ: 排比 – nhiều vế cùng cấu trúc, tăng khí thế lập luận và cảm xúc",
           "## Bài tập về nhà (运用)",
           "Dựa vào bài tập 5, rút gọn bài khóa thành bài văn khoảng 400 chữ, thử dùng 哪怕、反之 và một câu 排比"],
    say=["Chúng ta cùng tổng kết bài ba mươi hai.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 背叛，魄力，打击，潜移默化，鞭策，赋予，鄙视，束缚，宣泄，忌讳，抹杀，沉淀. Nhớ cẩn thận với các từ giả Hán Việt như 打击 và 抹杀 nhé."),
         F(1, "Về ngữ pháp: 哪怕 nghĩa là dù cho, vế sau thường có 也会，也要, giống 即使 nhưng hay dùng trong khẩu ngữ. 反之 nghĩa là ngược lại, đứng giữa hai câu, phía sau có dấu phẩy."),
         F(2, "Về phân biệt từ: 许可 không mang tân ngữ và tạo được từ 许可证; 允许 mang được tân ngữ, theo mẫu ai đó 允许 ai làm gì."),
         F(3, "Về tu từ: 排比 là xếp liền nhiều vế có cùng cấu trúc, giúp lập luận chặt chẽ và cảm xúc dâng trào."),
         F(5, "Bài tập về nhà: phần vận dụng của sách nói rằng, 男儿有泪不轻弹 là một quan niệm truyền thống, nhưng thật ra không khoa học; đàn ông cũng cần giải tỏa, khóc có lợi cho sức khỏe, 男人不妨一哭. Các bạn hãy tham khảo bài tập năm, rút gọn bài khóa thành một bài văn khoảng bốn trăm chữ, và thử dùng 哪怕，反之 cùng một câu 排比 nhé."),
         "Và một lời nhắn nhỏ từ thầy: khi buồn, các bạn cứ cho phép mình khóc một chút, rồi đứng dậy bước tiếp nhé. Như vậy là chúng ta đã học xong Đơn vị tám, 人体探秘, Khám phá cơ thể người. Cảm ơn các bạn đã theo dõi bài giảng. Hẹn gặp lại các bạn ở bài ba mươi ba: 怀念慢生活, Nhớ về cuộc sống chậm, bài mở đầu của Đơn vị chín 古今博览. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Hạ) – Bài 32: 有时，不妨悲伤 (Đôi khi, cứ buồn cũng được)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thứ tự quan trọng: cụm dài trước);
    # mỗi chữ thay thế cùng âm, cùng thanh với chữ gốc
    "tts_replace": {
        "为人正直": "维人正直",  # wéirén
        "有血有肉": "有谑有肉",  # yǒu xuè yǒu ròu, tránh đọc xiě
        "喜怒哀乐": "喜怒哀勒",  # āi lè, tránh đọc yuè
        "调不出": "条不出",      # tiáo (pha màu)
        "轻弹": "轻谈",          # qīng tán, tránh đọc dàn
        "背叛": "倍叛",          # bèipàn
        "处境": "楚境",          # chǔjìng
        "处理": "楚理",          # chǔlǐ
        "适当": "适荡",          # shìdàng
        "称为": "称维",          # chēngwéi
        "极为": "极维",          # jíwéi
        "分泌": "分密",          # fēnmì
        "淹没": "淹莫",          # yānmò
        "强调": "强掉",          # qiángdiào
        "给予": "挤予",          # jǐyǔ
        "几净": "机净",          # chuāngmíng jījìng
        "染发": "染珐",          # rǎnfà
        "言行": "言形",          # yánxíng
        "过长": "过常",          # guò cháng
        "倒会": "到会",          # dào huì
        "为金钱": "未金钱",      # wèi (vì tiền)
        "顿觉": "顿决",          # dùn jué
    },
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai32.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
