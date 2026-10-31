#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Hạ) – Bài 31 «运动的学问». Chạy để sinh bai31.json."""
import json
import os

TAG = "HSK 6 (Hạ) · Bài 31 · 运动的学问"
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
    zh="运动的学问", py="Yùndòng de xuéwen", vi="Bài 31: Những hiểu biết về vận động",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Hạ.",
         "Hôm nay chúng ta học bài ba mươi mốt: 运动的学问。 Nghĩa là: Những hiểu biết về vận động.",
         "Đây là bài thứ ba của Đơn vị tám, chủ đề 人体探秘, tức là Khám phá cơ thể người. Bài khóa là một cuộc trò chuyện trên truyền hình giữa phóng viên và thầy Vương, một chuyên gia khí công. Thầy Vương sẽ cho chúng ta biết sức khỏe gồm những gì, và muốn khỏe mạnh thì nên vận động như thế nào."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu nội dung bài khóa 运动的学问 – vận động thế nào cho đúng, cho khoa học",
           "Nắm vững 54 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: giới từ 逐 và thành phần chêm xen 归根到底",
           "Phân biệt 胡乱 và 随便",
           "Tu từ: dùng từ lớn cho việc nhỏ (大词小用)"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa: sức khỏe bao gồm những phương diện nào, và vận động thế nào cho đúng, cho khoa học."),
         F(1, "Thứ hai, nắm vững năm mươi tư từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học hai điểm ngữ pháp: giới từ 逐, nghĩa là lần lượt từng cái một, và thành phần chêm xen 归根到底, nghĩa là suy cho cùng."),
         F(3, "Thứ tư, phân biệt hai từ đều mang nghĩa qua loa, cẩu thả: 胡乱 và 随便."),
         F(4, "Thứ năm, một thủ pháp tu từ rất hài hước: 大词小用, tức là dùng một từ có phạm vi lớn, nghĩa nặng, để nói về một chuyện nhỏ."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Câu hỏi khởi động", size=40,
    items=["你关注自己的健康吗？ – Bạn có quan tâm đến sức khỏe của mình không?",
           "你觉得健康应该包括哪些方面？请举例说明。 – Theo bạn sức khỏe gồm những phương diện nào? Hãy nêu ví dụ.",
           "Từ khóa trong ảnh: ngủ nghỉ · vệ sinh · ăn uống · lối sống · chăm sóc y tế · tiền sử gia đình · môi trường · tập thể dục · xử lý căng thẳng · các mối quan hệ",
           "健康应该包括：身体、精神、心理、其他"],
    say=["Chúng ta bắt đầu bằng phần khởi động. Sách đưa ra câu hỏi sau.",
         F(0, "你关注自己的健康吗？ Bạn có quan tâm đến sức khỏe của mình không? 关注 là quan tâm, chú ý theo dõi."),
         F(1, "你觉得健康应该包括哪些方面？请举例说明。 Theo bạn, sức khỏe nên bao gồm những phương diện nào? Hãy nêu ví dụ để giải thích."),
         F(2, "Bức ảnh trong sách có rất nhiều mảnh giấy ghi chú bằng tiếng Anh xoay quanh chữ sức khỏe: ngủ nghỉ, vệ sinh, ăn uống, lối sống, chăm sóc y tế, tiền sử bệnh của gia đình, môi trường, tập thể dục, xử lý căng thẳng, và các mối quan hệ."),
         F(3, "Sách gợi ý chia thành bốn phương diện: 身体，精神，心理，其他。 Tức là: thể chất, tinh thần, tâm lý, và những mặt khác."),
         "Các bạn hãy tạm dừng video, thử nói bằng tiếng Trung, ví dụ: 身体方面，要多运动，吃得健康；心理方面，要学会减轻压力。 Sau đó hãy xem tiếp nhé."])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 会 và 首", size=36,
    items=["## 会 (hội): hội, tổ chức, đoàn thể",
           "协会 hiệp hội · 工会 công đoàn · 商会 thương hội · 农会 nông hội · 学会 hội học thuật · 学生会 hội sinh viên",
           "总会 tổng hội · 分会 chi hội · 国会 quốc hội · 议会 nghị viện · 会长 hội trưởng · 会员 hội viên · 会费 hội phí",
           "## 首 (thủ): đầu, đứng đầu, thứ nhất",
           "首要 hàng đầu · 首都 thủ đô · 首府 thủ phủ · 首批 đợt đầu tiên · 首任 người nhậm chức đầu tiên",
           "首位 vị trí số một · 首届 khóa đầu tiên · 首富 người giàu nhất · 首功 công đầu · 首席 ghế đầu, trưởng"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo, rất có lợi cho người Việt vì hầu hết các chữ đều có âm Hán Việt quen thuộc.",
         F(0, "Nhóm thứ nhất có chữ 会, Hán Việt là hội, nghĩa là hội, tổ chức, đoàn thể."),
         F(1, "协会，工会，商会，农会，学会，学生会。 Tức là: hiệp hội, công đoàn, thương hội, nông hội, hội học thuật, và hội sinh viên. Trong bài khóa các bạn sẽ gặp 气功协会, hiệp hội khí công."),
         F(2, "总会，分会，国会，议会，会长，会员，会费。 Tức là: tổng hội, chi hội, quốc hội, nghị viện, hội trưởng, hội viên, và hội phí."),
         F(3, "Nhóm thứ hai có chữ 首, Hán Việt là thủ, như trong thủ đô, thủ lĩnh, nghĩa là cái đầu, đứng đầu, thứ nhất."),
         F(4, "首要，首都，首府，首批，首任。 Tức là: quan trọng hàng đầu, thủ đô, thủ phủ, đợt đầu tiên, và người nhậm chức đầu tiên. Từ 首要 có trong bài khóa: 首要问题, vấn đề hàng đầu."),
         F(5, "首位，首届，首富，首功，首席。 Tức là: vị trí số một, khóa hay kỳ đầu tiên, người giàu nhất, công đầu, và ghế đầu, ví dụ 首席代表 là trưởng đại diện.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 生 và 射", size=36,
    items=["## 生 (sinh): sinh ra, nảy ra, phát sinh",
           "生锈 bị gỉ · 生病 bị ốm · 生财 sinh lời · 生产 sản xuất · 生效 có hiệu lực · 生疑 sinh nghi",
           "产生 sản sinh · 发生 xảy ra · 新生 mới ra đời · 再生 tái sinh · 急中生智 gấp quá nảy ra kế hay · 节外生枝 nảy thêm rắc rối",
           "## 射 (xạ): phóng ra, chiếu ra",
           "放射 phóng ra, tỏa ra · 反射 phản xạ · 照射 chiếu rọi · 直射 chiếu thẳng · 折射 khúc xạ · 辐射 bức xạ",
           "散射 tán xạ · 投射 chiếu vào · 透射 xuyên qua · 斜射 chiếu xiên · 映射 phản chiếu · 射线 tia (xạ tuyến)"],
    say=[F(0, "Nhóm thứ ba có chữ 生, Hán Việt là sinh, nghĩa là sinh ra, nảy ra, phát sinh."),
         F(1, "生锈，生病，生财，生产，生效，生疑。 Tức là: bị gỉ, bị ốm, sinh lời, sản xuất, có hiệu lực, và sinh nghi. Từ 生锈 có trong bài khóa: 人的大脑不用也会生锈, não không dùng cũng sẽ bị gỉ."),
         F(2, "产生，发生，新生，再生，急中生智，节外生枝。 Tức là: sản sinh, xảy ra, mới ra đời, tái sinh. Còn 急中生智 là trong lúc nguy cấp bỗng nảy ra kế hay, và 节外生枝 là nghĩa đen mắt cây lại mọc thêm cành, nghĩa bóng là nảy sinh thêm rắc rối ngoài dự kiến."),
         F(3, "Nhóm cuối cùng có chữ 射, Hán Việt là xạ, như trong xạ thủ, phóng xạ, nghĩa là phóng ra, bắn ra, chiếu ra."),
         F(4, "放射，反射，照射，直射，折射，辐射。 Tức là: phóng ra hay tỏa ra, phản xạ, chiếu rọi, chiếu thẳng, khúc xạ, và bức xạ. Bài khóa có hai từ 放射 và 反射."),
         F(5, "散射，投射，透射，斜射，映射，射线。 Tức là: tán xạ, chiếu vào, xuyên qua, chiếu xiên, phản chiếu, và tia, tức xạ tuyến, ví dụ 紫外线 là tia tử ngoại, một từ mới của bài."),
         "Các bạn thấy không, chỉ cần nắm nghĩa của một chữ gốc, ta có thể đoán được nghĩa của cả một nhóm từ. Hãy áp dụng cách này khi học từ mới nhé."])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng)
V = [
    ("忠实", "zhōngshí", "trung thực", "tính từ", "trung thành, chung thủy; trung thực với nguyên bản", "今天来的都是您的忠实观众。", "Hôm nay người đến đều là khán giả trung thành của thầy.",
     "Tính từ, nghĩa là trung thành, gắn bó lâu dài, như 忠实观众, khán giả trung thành, 忠实读者, độc giả trung thành. Cẩn thận: trung thực trong tiếng Việt là thật thà, còn 忠实 chủ yếu là trung thành; khi nói về dịch thuật thì 忠实于原文 là trung thành với nguyên văn."),
    ("不敢当", "bùgǎndāng", "bất cảm đương", "động từ", "không dám nhận (lời khiêm tốn khi được khen)", "您过奖了，我实在不敢当。", "Thầy quá khen rồi, tôi thật không dám nhận.",
     "Động từ, là lời khiêm tốn khi được người khác khen hay đối xử trọng thị, nghĩa là không dám nhận. Trong bài, thầy Vương được gọi là chuyên gia, nên thầy nói 专家不敢当."),
    ("走廊", "zǒuláng", "tẩu lang", "danh từ", "hành lang", "请不要在走廊里大声说话。", "Xin đừng nói to ngoài hành lang.",
     "Danh từ, nghĩa là hành lang, lối đi có mái che. Chữ 廊 là lang, như hành lang, 画廊 là phòng tranh."),
    ("徒弟", "túdì", "đồ đệ", "danh từ", "học trò, đồ đệ (học nghề, học võ)", "师傅带了好几个徒弟。", "Người thầy dạy mấy người đồ đệ.",
     "Danh từ, nghĩa là học trò theo thầy học nghề hoặc học võ, chính là đồ đệ trong tiếng Việt. Đi đôi với nó là 师傅, sư phụ."),
    ("气功", "qìgōng", "khí công", "danh từ", "khí công (phương pháp luyện thở, dưỡng sinh)", "每天早上，很多老人在公园里练气功。", "Mỗi sáng, rất nhiều người già tập khí công trong công viên.",
     "Danh từ, nghĩa là khí công, một phương pháp rèn luyện sức khỏe truyền thống của Trung Quốc, chú trọng hơi thở. Động từ đi kèm là 练, ví dụ 练气功, tập khí công."),
    ("剑", "jiàn", "kiếm", "danh từ", "thanh kiếm", "他每天早上都在公园里练太极剑。", "Sáng nào ông ấy cũng tập Thái cực kiếm trong công viên.",
     "Danh từ, nghĩa là thanh kiếm. 太极剑 là Thái cực kiếm, bài tập dưỡng sinh dùng kiếm, giống như Thái cực quyền 太极拳 dùng tay không."),
    ("哦", "ò", "nga", "thán từ", "ồ, à (chợt hiểu ra)", "哦，原来是这样！", "Ồ, hóa ra là vậy!",
     "Thán từ, đọc thanh bốn, biểu thị chợt hiểu ra hoặc chợt nhớ ra điều gì, giống ồ, à của tiếng Việt. Trong bài, thầy Vương nói 哦，不是徒弟, để đính chính lại lời phóng viên."),
    ("协会", "xiéhuì", "hiệp hội", "danh từ", "hiệp hội, hội", "他是气功协会的会员。", "Ông ấy là hội viên của hiệp hội khí công.",
     "Danh từ, nghĩa là hiệp hội, âm Hán Việt giống hệt tiếng Việt."),
    ("爆发", "bàofā", "bộc phát", "động từ", "bùng nổ, bộc phát", "这座火山上一次爆发是在一百年前。", "Lần phun trào gần nhất của ngọn núi lửa này là cách đây một trăm năm.",
     "Động từ, nghĩa là bùng nổ, bộc phát đột ngột, dùng cho núi lửa, chiến tranh, sức mạnh, cảm xúc. Trong bài có cụm 力量一爆发, sức mạnh vừa bộc phát."),
    ("劈", "pī", "phách", "động từ", "chẻ, bổ, chặt", "他用斧头把木头劈开了。", "Anh ấy dùng rìu bổ khúc gỗ ra.",
     "Động từ, nghĩa là dùng dao, rìu hoặc bàn tay bổ mạnh xuống cho vật tách ra, tức là chẻ, bổ. Bài khóa nói đến kiểu khí công có thể 把好几块砖就给劈开, chẻ đôi mấy viên gạch."),
    ("误解", "wùjiě", "ngộ giải", "động từ", "hiểu lầm, hiểu sai", "你误解我的意思了。", "Bạn hiểu lầm ý tôi rồi.",
     "Động từ, nghĩa là hiểu lầm, hiểu sai, cũng dùng được như danh từ: 消除误解, xóa bỏ hiểu lầm. Chữ 误 là ngộ, như ngộ nhận."),
    ("群众", "qúnzhòng", "quần chúng", "danh từ", "quần chúng, đông đảo người dân", "广大群众的健身意识在逐年提升。", "Ý thức rèn luyện sức khỏe của đông đảo quần chúng tăng lên qua từng năm.",
     "Danh từ, nghĩa là quần chúng, người dân nói chung. Cụm cố định hay gặp nhất là 广大群众, đông đảo quần chúng."),
    ("逐年", "zhúnián", "trục niên", "phó từ", "qua từng năm, năm này qua năm khác", "城市人口逐年增加。", "Dân số thành phố tăng lên qua từng năm.",
     "Phó từ, nghĩa là theo từng năm, năm sau hơn năm trước. Chữ 逐 là điểm ngữ pháp thứ nhất của bài hôm nay."),
    ("要素", "yàosù", "yếu tố", "danh từ", "yếu tố (cơ bản, cấu thành)", "有人提出了健康五要素。", "Có người đưa ra năm yếu tố của sức khỏe.",
     "Danh từ, nghĩa là yếu tố cơ bản cấu thành nên sự vật. Hán Việt là yếu tố, giống hệt tiếng Việt."),
    ("智力", "zhìlì", "trí lực", "danh từ", "trí lực, trí tuệ, trí thông minh", "这种游戏可以开发孩子的智力。", "Trò chơi này có thể phát triển trí tuệ của trẻ.",
     "Danh từ, nghĩa là trí lực, khả năng nhận thức và suy nghĩ. Cụm hay gặp: 开发智力, phát triển trí tuệ."),
    ("预期", "yùqī", "dự kỳ", "động từ", "dự tính, mong đợi (từ trước)", "比赛结果和我们预期的一样。", "Kết quả trận đấu đúng như chúng tôi dự tính.",
     "Động từ, nghĩa là dự tính, mong đợi trước. Cụm hay gặp trong bài: 达到预期效果, đạt được hiệu quả như mong đợi."),
    ("首要", "shǒuyào", "thủ yếu", "tính từ", "hàng đầu, quan trọng nhất", "安全是首要的。", "An toàn là quan trọng hàng đầu.",
     "Tính từ, nghĩa là quan trọng hàng đầu, cần đặt lên trước tiên. Bài khóa có cụm 首要问题, vấn đề hàng đầu."),
    ("生锈", "shēng xiù", "sinh tú", "động từ", "bị gỉ, han gỉ", "刀很久不用就生锈了。", "Con dao lâu không dùng nên bị gỉ rồi.",
     "Động từ ly hợp, nghĩa là bị gỉ, gồm 生 là sinh ra và 锈 là gỉ sét. Bài khóa dùng theo nghĩa bóng: não không dùng cũng sẽ bị gỉ."),
    ("放射", "fàngshè", "phóng xạ", "động từ", "phóng ra, tỏa ra (ánh sáng, tia…)", "太阳放射出耀眼的光芒。", "Mặt trời tỏa ra ánh sáng chói lòa.",
     "Động từ, nghĩa là tỏa ra, phóng ra từ một điểm ra bốn phía. Chú ý: phóng xạ trong tiếng Việt thường là tia phóng xạ, còn 放射 có nghĩa rộng hơn. Bài khóa có 放射出新的火花, lóe ra những tia lửa mới."),
    ("夫人", "fūrén", "phu nhân", "danh từ", "phu nhân, vợ (cách gọi trang trọng)", "钱学森的夫人是音乐家。", "Phu nhân của Tiền Học Sâm là nhạc sĩ.",
     "Danh từ, nghĩa là phu nhân, cách gọi trang trọng vợ của người khác, không dùng để gọi vợ mình."),
    ("端端正正", "duānduānzhèngzhèng", "đoan đoan chính chính", "tính từ", "ngay ngắn, nghiêm chỉnh (dạng lặp của 端正)", "他端端正正地坐在桌子前面。", "Anh ấy ngồi ngay ngắn trước bàn.",
     "Đây là dạng lặp AABB của tính từ 端正, đoan chính, nghĩa là ngay ngắn, nghiêm chỉnh. Lặp lại để nhấn mạnh và miêu tả sinh động hơn. 端正 còn dùng cho thái độ, phẩm hạnh: 态度端正, thái độ đúng đắn."),
    ("潜力", "qiánlì", "tiềm lực", "danh từ", "tiềm năng, tiềm lực", "这个年轻人很有潜力。", "Người thanh niên này rất có tiềm năng.",
     "Danh từ, nghĩa là sức mạnh còn ẩn giấu, chưa được phát huy, tức tiềm năng. Bài khóa nói 大脑潜力巨大, tiềm năng của não rất lớn."),
    ("衰退", "shuāituì", "suy thoái", "động từ", "suy giảm, suy thoái", "年纪大了，记忆力逐渐衰退。", "Tuổi cao rồi, trí nhớ dần dần suy giảm.",
     "Động từ, nghĩa là suy giảm, sa sút, dùng cho sức khỏe, trí nhớ, hoặc kinh tế: 经济衰退, kinh tế suy thoái."),
    ("著作", "zhùzuò", "trứ tác", "danh từ", "tác phẩm, sách chuyên khảo", "他一生写了很多重要的著作。", "Cả đời ông ấy đã viết rất nhiều tác phẩm quan trọng.",
     "Danh từ, nghĩa là tác phẩm, sách do một người viết ra, thường là sách học thuật. Bài khóa có cụm 养生著作, sách về dưỡng sinh."),
    ("反射", "fǎnshè", "phản xạ", "động từ", "phản xạ", "镜子能反射光线。", "Gương có thể phản xạ tia sáng.",
     "Động từ, nghĩa là phản xạ, vừa dùng cho ánh sáng, âm thanh, vừa dùng trong sinh học: 条件反射, phản xạ có điều kiện."),
    ("弱点", "ruòdiǎn", "nhược điểm", "danh từ", "nhược điểm, điểm yếu", "懒惰是人天生的弱点。", "Lười biếng là nhược điểm bẩm sinh của con người.",
     "Danh từ, nghĩa là nhược điểm, điểm yếu, ngược nghĩa với 优点, ưu điểm."),
    ("迁就", "qiānjiù", "thiên tựu", "động từ", "chiều theo, nhân nhượng, dễ dãi", "父母不能总是迁就孩子。", "Bố mẹ không thể lúc nào cũng chiều theo con.",
     "Động từ, nghĩa là chiều theo, nhân nhượng, hạ yêu cầu của mình cho vừa ý người khác. Trong bài có 不要迁就自己, đừng dễ dãi với bản thân."),
    ("坚定", "jiāndìng", "kiên định", "tính từ", "kiên định, vững vàng", "他的态度非常坚定。", "Thái độ của anh ấy rất kiên định.",
     "Tính từ, nghĩa là kiên định, vững vàng, không dao động. Hay đi với 意志, ý chí, 立场, lập trường."),
    ("坚韧", "jiānrèn", "kiên nhận", "tính từ", "bền bỉ, dẻo dai, kiên cường", "他有着坚韧的精神。", "Anh ấy có tinh thần bền bỉ.",
     "Tính từ, nghĩa là bền bỉ, dẻo dai, khó bị bẻ gãy. Chú ý chữ 韧 là dẻo dai, khác với chữ 忍 trong kiên nhẫn. Thành ngữ hay gặp: 坚韧不拔, kiên cường không gì lay chuyển."),
    ("狠心", "hěnxīn", "ngận tâm", "danh từ", "quyết tâm sắt đá; (tính từ) nhẫn tâm", "他下狠心戒了烟。", "Anh ấy hạ quyết tâm cai thuốc lá.",
     "Trong bài là danh từ, đi với động từ 下: 下狠心, hạ quyết tâm sắt đá, dù khó khăn đến mấy cũng làm. Khi là tính từ, 狠心 lại có nghĩa là nhẫn tâm, độc ác."),
    ("半途而废", "bàntú'érfèi", "bán đồ nhi phế", "thành ngữ", "bỏ dở nửa chừng", "做事情不能半途而废。", "Làm việc gì cũng không được bỏ dở nửa chừng.",
     "Thành ngữ, nghĩa đen là đi được nửa đường thì bỏ, nghĩa bóng là làm việc gì cũng bỏ dở giữa chừng."),
    ("虐待", "nüèdài", "ngược đãi", "động từ", "ngược đãi, hành hạ", "我们不应该虐待动物。", "Chúng ta không nên ngược đãi động vật.",
     "Động từ, nghĩa là ngược đãi, đối xử tàn nhẫn. Chú ý chữ 虐 đọc là nüè, có hai chấm trên chữ u. Trong bài, phóng viên dùng từ nặng nề này một cách hài hước."),
    ("落实", "luòshí", "lạc thực", "động từ", "thực hiện đến nơi đến chốn, triển khai", "这项工作要落实到每个人。", "Công việc này phải được triển khai đến từng người.",
     "Động từ, nghĩa là đưa kế hoạch, chính sách vào thực hiện cụ thể đến nơi đến chốn. Bài khóa có câu 有计划，有落实, có kế hoạch và có thực hiện."),
    ("归根到底", "guīgēn-dàodǐ", "quy căn đáo để", "thành ngữ", "suy cho cùng, xét đến cùng", "运动健身归根到底是自己的事。", "Rèn luyện sức khỏe suy cho cùng là việc của chính mình.",
     "Nghĩa đen là quay về gốc rễ, đến tận đáy, tức là suy cho cùng, xét đến cùng. Đây là điểm ngữ pháp thứ hai của bài."),
    ("胡乱", "húluàn", "hồ loạn", "phó từ", "bừa bãi, qua loa, tùy tiện", "他胡乱吃了几口就走了。", "Anh ấy ăn qua loa vài miếng rồi đi.",
     "Phó từ, nghĩa là bừa bãi, qua loa, không nghiêm túc. Lát nữa chúng ta sẽ phân biệt kỹ 胡乱 với 随便."),
    ("间接", "jiànjiē", "gián tiếp", "tính từ", "gián tiếp", "这件事我是间接听说的。", "Việc này tôi nghe gián tiếp qua người khác.",
     "Tính từ, nghĩa là gián tiếp, ngược nghĩa với 直接, trực tiếp. Chú ý: trong từ 间接, chữ đầu đọc là jiàn, thanh bốn, chứ không phải jiān."),
    ("品行", "pǐnxíng", "phẩm hạnh", "danh từ", "phẩm hạnh, đạo đức và hành vi", "这个孩子品行端正。", "Đứa trẻ này có phẩm hạnh đoan chính.",
     "Danh từ, nghĩa là phẩm hạnh, tức đạo đức và cách cư xử của một người. Chú ý: trong từ 品行, chữ sau đọc là xíng, chứ không phải háng. Cụm hay gặp là 品行端正, đúng với chữ 端正 vừa học."),
    ("紫外线", "zǐwàixiàn", "tử ngoại tuyến", "danh từ", "tia tử ngoại, tia cực tím (tia UV)", "夏天紫外线很强，出门要注意防晒。", "Mùa hè tia cực tím rất mạnh, ra ngoài phải chú ý chống nắng.",
     "Danh từ, gồm 紫 là màu tím, 外 là ngoài, 线 là tia, tức tia tử ngoại, hay tia cực tím."),
    ("消毒", "xiāo dú", "tiêu độc", "động từ", "khử trùng, tiêu độc", "医生用酒精给伤口消毒。", "Bác sĩ dùng cồn khử trùng vết thương.",
     "Động từ ly hợp, nghĩa là khử trùng, diệt vi khuẩn. Bài khóa nói tia tử ngoại trong ánh nắng 对人体有消毒作用, có tác dụng khử trùng cho cơ thể."),
    ("钙", "gài", "cái", "danh từ", "canxi", "多喝牛奶可以补钙。", "Uống nhiều sữa có thể bổ sung canxi.",
     "Danh từ, nghĩa là canxi. 补钙 là bổ sung canxi, một từ rất hay gặp trong quảng cáo thực phẩm."),
    ("二氧化碳", "èryǎnghuàtàn", "nhị dưỡng hóa thán", "danh từ", "khí cacbonic (CO₂)", "植物吸收二氧化碳，放出氧气。", "Thực vật hấp thụ khí cacbonic, thải ra khí oxy.",
     "Danh từ, nghĩa là khí cacbonic. Gồm 二 là hai, 氧 là oxy, 化 là hóa hợp, 碳 là cacbon, tức là cacbon kết hợp với hai nguyên tử oxy."),
    ("舒畅", "shūchàng", "thư sướng", "tính từ", "thư thái, khoan khoái (tinh thần)", "运动可以使人心情舒畅。", "Vận động có thể làm tâm trạng con người thư thái.",
     "Tính từ, nghĩa là thư thái, khoan khoái, không có gì lo lắng. Thường đi với 心情 hoặc 精神."),
    ("宣扬", "xuānyáng", "tuyên dương", "động từ", "rêu rao, quảng bá, truyền bá rộng rãi", "这件事你别到处宣扬。", "Chuyện này bạn đừng đi rêu rao khắp nơi.",
     "Động từ, nghĩa là truyền bá rộng rãi cho mọi người biết, nhiều khi mang ý phô trương, rêu rao. Cẩn thận: tuyên dương trong tiếng Việt là khen ngợi, tương đương 表扬, còn 宣扬 thì không có nghĩa khen."),
    ("孔", "kǒng", "khổng", "danh từ", "lỗ", "墙上有一个小孔。", "Trên tường có một lỗ nhỏ.",
     "Danh từ, nghĩa là cái lỗ. 毛孔 là lỗ chân lông, 鼻孔 là lỗ mũi."),
    ("循序渐进", "xúnxù-jiànjìn", "tuần tự tiệm tiến", "thành ngữ", "tiến dần từng bước, theo trình tự", "学习外语要循序渐进。", "Học ngoại ngữ phải tiến dần từng bước.",
     "Thành ngữ, gồm 循序 là theo trình tự, 渐进 là tiến dần, nghĩa là làm từng bước một, từ dễ đến khó."),
    ("急于求成", "jíyú qiú chéng", "cấp ư cầu thành", "thành ngữ", "nóng vội muốn thành công ngay", "减肥不能急于求成。", "Giảm cân không được nóng vội.",
     "Thành ngữ, nghĩa là nóng vội muốn thành công ngay. Đây là từ trái nghĩa với 循序渐进 ở trên, hai từ thường đi liền với nhau như trong bài khóa."),
    ("剧烈", "jùliè", "kịch liệt", "tính từ", "mạnh, dữ dội, kịch liệt", "饭后不要做剧烈运动。", "Sau khi ăn đừng vận động mạnh.",
     "Tính từ, nghĩa là mạnh, dữ dội. 剧烈运动 là vận động mạnh, 剧烈的疼痛 là cơn đau dữ dội."),
    ("幅度", "fúdù", "bức độ", "danh từ", "biên độ, mức độ (dao động, thay đổi)", "今年物价上涨的幅度很大。", "Năm nay mức tăng giá cả rất lớn.",
     "Danh từ, nghĩa là biên độ, phạm vi của động tác hoặc mức độ thay đổi. Bài khóa có 大幅度动作, động tác biên độ lớn."),
    ("蛋白质", "dànbáizhì", "đản bạch chất", "danh từ", "protein, chất đạm", "鸡蛋里含有丰富的蛋白质。", "Trong trứng gà có nhiều protein.",
     "Danh từ, nghĩa là protein, chất đạm. Nghĩa đen là chất lòng trắng trứng."),
    ("维生素", "wéishēngsù", "duy sinh tố", "danh từ", "vitamin", "水果里有很多维生素。", "Trong hoa quả có rất nhiều vitamin.",
     "Danh từ, nghĩa là vitamin. Trước đây tiếng Việt cũng gọi vitamin là sinh tố."),
    ("不愧", "búkuì", "bất quý", "phó từ", "không hổ là, xứng đáng là", "您真不愧是这方面的专家。", "Thầy thật xứng đáng là chuyên gia trong lĩnh vực này.",
     "Phó từ, nghĩa là không hổ thẹn với danh hiệu, tức là xứng đáng là. Thường dùng theo mẫu 不愧是 cộng danh từ. Chú ý: trong 不愧, chữ đầu đọc thanh hai vì đứng trước một chữ thanh bốn."),
    ("定期", "dìngqī", "định kỳ", "tính từ", "định kỳ", "我们应该定期检查身体。", "Chúng ta nên khám sức khỏe định kỳ.",
     "Tính từ, nghĩa là định kỳ, theo một khoảng thời gian cố định. Âm Hán Việt giống hệt tiếng Việt."),
    ("联络", "liánluò", "liên lạc", "động từ", "liên lạc", "毕业以后我们一直保持联络。", "Sau khi tốt nghiệp chúng tôi vẫn luôn giữ liên lạc.",
     "Động từ, nghĩa là liên lạc, gần nghĩa với 联系."),
    ("保重", "bǎozhòng", "bảo trọng", "động từ", "giữ gìn sức khỏe, bảo trọng", "天冷了，您多多保重！", "Trời lạnh rồi, bác giữ gìn sức khỏe nhé!",
     "Động từ, nghĩa là giữ gìn sức khỏe, bảo trọng, thường dùng làm lời chào, lời dặn khi chia tay."),
]

add("bullets", chapter="Từ mới (54 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 31 có 54 từ mới, chia thành 18 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 间接 (jiàn) · 品行 (xíng) · 虐待 (nüè) · 不愧 (bú)"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có năm mươi tư từ, thầy chia thành mười tám nhóm nhỏ, mỗi nhóm ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số từ có âm đọc đặc biệt, thầy sẽ nhắc khi gặp. Bài này cũng có nhiều từ Hán Việt giống hệt tiếng Việt như 协会，群众，弱点，虐待，定期, các bạn sẽ thấy dễ nhớ hơn nhiều. Chúng ta bắt đầu nhé.")])

for g in range(0, len(V), 3):
    group = V[g:g + 3]
    words, say = [], []
    for i, (zh, py, hv, loai, vi, ex, exvi, expl) in enumerate(group):
        n = g + i + 1
        words.append({"zh": zh, "py": py, "hv": hv.upper(), "loai": f"{n}. {loai}", "vi": vi, "ex": ex, "exvi": exvi})
        say.append(F(i, f"Từ số {n}: {zh}。 {zh}。 Hán Việt là {hv}.", zr=120))
        say.append(F(i, f"{expl} Ví dụ: {ex}{'' if ex[-1] in '。…？！，' else '，'} {exvi[0].upper() + exvi[1:]}{'' if exvi.endswith(('.', '!', '?')) else '.'}", zr=130))
    add("vocab", section="Từ mới 生词", title=f"Từ mới ({g + 1}–{g + len(group)} / {len(V)})",
        words=words, say=say)

# ======================= BÀI KHÓA =======================
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung nếu khác]); bài khóa là hội thoại,
# mỗi lượt lời xuống dòng. Bài không có chữ số Ả Rập nên lời đọc = chữ hiển thị bỏ ngoặc kép.
P = [
    ("记者：王老师，欢迎您到我们节目来做客。今天来的都是您的忠实观众，大家特别愿意和您这样的大专家进行交流。\n王老师：“专家”不敢当，有这样的机会，我也很高兴。",
     "Phóng viên: Thưa thầy Vương, chào mừng thầy đến làm khách mời của chương trình. Hôm nay những người có mặt đều là khán giả trung thành của thầy, mọi người rất muốn được giao lưu với một chuyên gia lớn như thầy.\nThầy Vương: Chuyên gia thì tôi không dám nhận, có được cơ hội như thế này, tôi cũng rất vui.",
     ["到……来做客 là đến làm khách. 忠实观众 là khán giả trung thành; nhớ là 忠实 ở đây không phải thật thà, mà là trung thành, gắn bó.",
      "不敢当 là lời khiêm tốn khi được khen. Thầy Vương đặt chữ 专家 trong ngoặc kép, ý là mình không dám nhận danh hiệu chuyên gia."]),
    ("记者：那天采访您，在公园走廊那儿，您和您徒弟是练气功还是练太极剑呢？\n王老师：哦，不是徒弟，是气功协会的气功爱好者。",
     "Phóng viên: Hôm phỏng vấn thầy, ở chỗ hành lang trong công viên, thầy và đồ đệ đang tập khí công hay tập Thái cực kiếm vậy?\nThầy Vương: Ồ, không phải đồ đệ đâu, đó là những người yêu thích khí công của hiệp hội khí công.",
     ["是……还是……呢？ là câu hỏi lựa chọn: là… hay là…? 那儿 đặt sau danh từ chỉ nơi chốn: 走廊那儿, chỗ hành lang.",
      "哦 ở đây biểu thị muốn đính chính lại: không phải đồ đệ đâu. 爱好者 là người yêu thích, người đam mê."]),
    ("记者：你们的气功不是那种力量一爆发，能瞬间把好几块砖就给劈开的啊？\n王老师：那只是气功的一种。气功还是中国独特的健身方法之一，可以增强体质，促进慢性病康复，还可以辅助治疗某些疾病。",
     "Phóng viên: Khí công của các thầy chẳng phải loại vừa bộc phát sức mạnh là chẻ đôi mấy viên gạch sao?\nThầy Vương: Đó chỉ là một loại thôi. Khí công còn là một trong những phương pháp rèn luyện sức khỏe độc đáo của Trung Quốc, có thể tăng cường thể chất, giúp bệnh mãn tính hồi phục, còn hỗ trợ điều trị một số bệnh.",
     ["不是……啊？ là câu hỏi phản vấn: chẳng phải là… sao? 瞬间 là trong nháy mắt. Trong 把好几块砖就给劈开, chữ 给 đứng trước động từ để nhấn mạnh, rất khẩu ngữ.",
      "之一 là một trong những. 增强体质 là tăng cường thể chất, 慢性病 là bệnh mãn tính, 辅助治疗 là hỗ trợ điều trị."]),
    ("记者：看来我是误解气功了。最近有个调查，广大群众的健身意识在逐年提升。对于健康，您能对我们说点儿什么吗？",
     "Phóng viên: Xem ra tôi đã hiểu lầm khí công rồi. Gần đây có một cuộc điều tra cho thấy ý thức rèn luyện sức khỏe của đông đảo quần chúng đang tăng lên qua từng năm. Về sức khỏe, thầy có thể nói với chúng tôi đôi điều được không?",
     ["看来 là xem ra. 广大群众 là đông đảo quần chúng, một cụm cố định. 健身意识 là ý thức rèn luyện sức khỏe.",
      "在逐年提升: 在 là phó từ chỉ sự việc đang diễn ra, còn 逐年 là qua từng năm, đây chính là điểm ngữ pháp 逐 mà ta học ở phần sau."]),
    ("王老师：健康的新概念不仅是不生病，还包括心理健康和社会交往方面的能力，甚至有人提出健康五要素，包括身体、情绪、智力、精神和社交，这五个方面共同构成健康的完美状态。",
     "Thầy Vương: Khái niệm mới về sức khỏe không chỉ là không ốm đau, mà còn bao gồm sức khỏe tâm lý và năng lực giao tiếp xã hội; thậm chí có người còn đưa ra năm yếu tố của sức khỏe, gồm thể chất, cảm xúc, trí lực, tinh thần và giao tiếp xã hội, năm phương diện này cùng nhau tạo nên trạng thái hoàn hảo của sức khỏe.",
     ["不仅……还…… là không chỉ… mà còn…; 甚至 là thậm chí, nâng ý lên một mức cao hơn.",
      "共同构成 là cùng nhau tạo thành. 社交 là giao tiếp xã hội, cách nói gọn của 社会交往."]),
    ("有句名言：生命在于运动，其实健康也在于运动。当然要达到预期效果，怎样运动很重要。\n记者：那您就着重跟我们谈谈运动的学问吧。",
     "Có một câu danh ngôn: Sự sống nằm ở vận động; thật ra sức khỏe cũng nằm ở vận động. Đương nhiên, muốn đạt được hiệu quả như mong đợi thì vận động thế nào là rất quan trọng.\nPhóng viên: Vậy thầy hãy tập trung nói với chúng tôi về những hiểu biết trong vận động nhé.",
     ["生命在于运动 là một câu danh ngôn nổi tiếng. 在于 nghĩa là nằm ở, do… quyết định.",
      "着重 đọc là zhuózhòng, nghĩa là tập trung, chú trọng, các bạn đã gặp ở bài hai mươi mốt. 学问 ở đây là những hiểu biết, những điều cần biết, chính là tên của bài khóa."]),
    ("王老师：要健康，首要问题是勤于运用大脑，人的大脑不用也会生锈。大家知道，人脑左半球主管抽象思维，右半球主管形象思维，二者有分工有联系。左右脑交替使用，思维常可以放射出新的火花。",
     "Thầy Vương: Muốn khỏe mạnh, vấn đề hàng đầu là phải chăm sử dụng bộ não, não người không dùng cũng sẽ bị gỉ. Mọi người đều biết, bán cầu não trái phụ trách tư duy trừu tượng, bán cầu não phải phụ trách tư duy hình tượng, hai bên vừa có phân công vừa có liên hệ. Sử dụng luân phiên não trái và não phải, tư duy thường có thể lóe ra những tia lửa mới.",
     ["勤于 là chăm làm việc gì, 于 là giới từ văn viết. 不用也会生锈 là cách nói hình ảnh: não giống như sắt, không dùng thì bị gỉ.",
      "主管 là phụ trách chính. 二者 là cả hai, cách nói văn viết. 放射出新的火花 nghĩa đen là tỏa ra tia lửa mới, tức là nảy ra ý tưởng mới."]),
    ("著名科学家钱学森的夫人是音乐家，钱学森的很多重要科学理论不是端端正正地坐在桌子前面想出来的，而是听过音乐之后冒出来的。科学运用左右脑，工作的高效和防止脑衰就成为了可能。",
     "Phu nhân của nhà khoa học nổi tiếng Tiền Học Sâm là một nhạc sĩ; rất nhiều lý thuyết khoa học quan trọng của ông Tiền Học Sâm không phải được nghĩ ra khi ngồi ngay ngắn trước bàn, mà là nảy ra sau khi nghe nhạc. Sử dụng não trái và não phải một cách khoa học thì làm việc hiệu quả cao và phòng chống suy giảm trí não sẽ trở thành điều có thể.",
     ["钱学森 là Tiền Học Sâm, nhà khoa học nổi tiếng, được gọi là cha đẻ của ngành tên lửa Trung Quốc. 不是……而是…… là không phải… mà là….",
      "冒出来 là bỗng nảy ra, trồi lên, rất khẩu ngữ. 脑衰 là não suy giảm, cách nói gọn của 大脑衰退."]),
    ("大脑潜力巨大，它是人体衰退最慢的器官。一些养生著作中指出，人用脑越勤，大脑各神经细胞之间的联系越多，形成的条件反射也越多。",
     "Não bộ có tiềm năng rất lớn, đó là cơ quan suy thoái chậm nhất của cơ thể người. Một số sách dưỡng sinh chỉ ra rằng, con người dùng não càng chăm thì mối liên hệ giữa các tế bào thần kinh trong não càng nhiều, phản xạ có điều kiện được hình thành cũng càng nhiều.",
     ["潜力巨大 là tiềm năng rất lớn. 器官 là cơ quan trong cơ thể. 养生著作 là sách về dưỡng sinh.",
      "越……越…… là càng… càng…: 用脑越勤，联系越多, dùng não càng chăm thì liên hệ càng nhiều. 神经细胞 là tế bào thần kinh, 条件反射 là phản xạ có điều kiện."]),
    ("记者：大脑就像我们身体的指挥中心，大脑不健康，人就谈不上健康。\n王老师：对。其次呢，运动贵在坚持。",
     "Phóng viên: Não bộ giống như trung tâm chỉ huy của cơ thể chúng ta, não không khỏe thì con người chẳng thể nói là khỏe được.\nThầy Vương: Đúng vậy. Thứ hai là, vận động quý ở sự kiên trì.",
     ["谈不上 là chưa thể nói là, chưa đạt tới mức. 大脑不健康，人就谈不上健康: não không khỏe thì người không thể gọi là khỏe.",
      "Ở trên thầy Vương nói 首要问题, vấn đề hàng đầu, giờ đến 其次, thứ hai là. 贵在坚持 nghĩa là điều đáng quý nằm ở sự kiên trì; 贵在 là quý ở."]),
    ("懒惰是人天生的弱点，所以不要迁就自己，要以坚定的意志，坚韧的精神克服惰性，下狠心咬牙坚持，绝不能半途而废。\n记者：王老师，您怎么好像在说我呢？我就不想虐待自己，所以很难坚持。",
     "Lười biếng là nhược điểm bẩm sinh của con người, vì thế đừng dễ dãi với bản thân, phải dùng ý chí kiên định và tinh thần bền bỉ để khắc phục tính lười, hạ quyết tâm nghiến răng kiên trì, tuyệt đối không được bỏ dở nửa chừng.\nPhóng viên: Thầy Vương ơi, sao thầy nói cứ như đang nói tôi vậy? Tôi chẳng muốn ngược đãi bản thân, nên rất khó kiên trì.",
     ["天生 là bẩm sinh. 以坚定的意志, chữ 以 bằng 用, nghĩa là bằng. 惰性 là tính lười, cùng chữ 惰 với 懒惰.",
      "下狠心 là hạ quyết tâm sắt đá, 咬牙 là nghiến răng. Phóng viên dùng từ 虐待, ngược đãi, cho việc chăm tập thể dục. Đây là cách nói hài hước gọi là 大词小用, ta sẽ học ở cuối bài."]),
    ("王老师：怎么会是虐待呢？你以后联系我，我带你锻炼。咱们有计划，有落实。运动健身归根到底是自己的事，胡乱对付其实是在骗自己，坚持运动也是培养人的意志力、完善人格的过程。",
     "Thầy Vương: Sao lại là ngược đãi được? Sau này anh cứ liên hệ với tôi, tôi sẽ dẫn anh tập luyện. Chúng ta có kế hoạch, có thực hiện đến nơi đến chốn. Rèn luyện sức khỏe suy cho cùng là việc của chính mình, đối phó qua loa thật ra là đang tự lừa mình; kiên trì vận động cũng là quá trình rèn luyện ý chí và hoàn thiện nhân cách của con người.",
     ["怎么会是虐待呢？ là câu hỏi phản vấn: sao lại là ngược đãi được, tức là hoàn toàn không phải. 有计划，有落实 là có kế hoạch, có thực hiện.",
      "归根到底 là suy cho cùng, điểm ngữ pháp thứ hai của bài. 胡乱对付 là đối phó qua loa, 对付 ở đây là làm cho xong chuyện."]),
    ("记者：看来运动真不是小事，还间接体现着我们的品行呢。\n王老师：另外，冬季健身好处很多，可以提高人的御寒能力；冬天阳光中的紫外线对人体有消毒作用，还能促进对钙的吸收；",
     "Phóng viên: Xem ra vận động thật không phải chuyện nhỏ, nó còn gián tiếp thể hiện phẩm hạnh của chúng ta nữa.\nThầy Vương: Ngoài ra, tập luyện vào mùa đông có rất nhiều lợi ích: có thể nâng cao khả năng chịu lạnh; tia tử ngoại trong ánh nắng mùa đông có tác dụng khử trùng cho cơ thể, lại còn thúc đẩy hấp thụ canxi;",
     ["体现着 là đang thể hiện. 冬季健身 là tập luyện vào mùa đông. 御寒 là chống lạnh, 御寒能力 là khả năng chịu lạnh.",
      "对……有……作用 là có tác dụng… đối với…, và 促进对钙的吸收 là thúc đẩy hấp thụ canxi. Câu này rất dài, dùng dấu chấm phẩy để liệt kê lần lượt các lợi ích của tập luyện mùa đông."]),
    ("冬天空气中二氧化碳浓度比夏天低，所以冬天运动对身体更为有利；运动还可以使人心情舒畅。许多保健食品都宣扬能够促进健康，其实运动才是维护健康最好的方法。",
     "nồng độ khí cacbonic trong không khí mùa đông thấp hơn mùa hè, vì vậy vận động vào mùa đông càng có lợi cho cơ thể; vận động còn khiến tâm trạng con người thư thái. Rất nhiều thực phẩm chức năng đều quảng cáo là có thể tăng cường sức khỏe, thật ra vận động mới là cách tốt nhất để giữ gìn sức khỏe.",
     ["浓度 là nồng độ. 更为有利 là càng có lợi hơn, 更为 là cách nói văn viết, nghĩa như 更加. 使人心情舒畅 là khiến tâm trạng con người thư thái.",
      "保健食品 là thực phẩm chức năng. 宣扬 ở đây là quảng cáo rùm beng. 其实……才是…… là thật ra… mới là…, nhấn mạnh vận động mới là cách tốt nhất."]),
    ("记者：运动对皮肤是不是也有好处？\n王老师：运动能令全身排汗，毛孔内的垃圾及多余油脂会被排走，皮肤自然会更好。",
     "Phóng viên: Vận động có phải cũng có lợi cho làn da không?\nThầy Vương: Vận động có thể khiến toàn thân đổ mồ hôi, chất bẩn và dầu thừa trong lỗ chân lông sẽ được đẩy ra ngoài, da tự nhiên sẽ đẹp hơn.",
     ["是不是也……？ là câu hỏi chính phản: có phải cũng… không? 好处 là lợi ích, 对……有好处 là có lợi cho….",
      "令 bằng 让, khiến cho. 毛孔 là lỗ chân lông, chữ 孔 là cái lỗ. 及 bằng 和, cách nói văn viết. 排走 là thải ra, đẩy đi."]),
    ("记者：运动是不是也要讲究科学？\n王老师：当然。运动健身要循序渐进，不要急于求成；不适合自己身体状况的剧烈运动或大幅度动作尽量别勉强。",
     "Phóng viên: Vận động có phải cũng cần chú trọng tính khoa học không?\nThầy Vương: Đương nhiên. Rèn luyện sức khỏe phải tiến dần từng bước, đừng nóng vội; những bài vận động mạnh hoặc động tác biên độ lớn không phù hợp với tình trạng cơ thể mình thì cố gắng đừng gượng ép.",
     ["讲究 ở đây là động từ, nghĩa là chú trọng, coi trọng. 循序渐进 và 急于求成 là hai thành ngữ trái nghĩa, thường đi liền nhau.",
      "尽量别勉强 là cố gắng đừng gượng ép. 大幅度动作 là động tác có biên độ lớn."]),
    ("记者：运动之后，我们常常觉得又渴又饿，运动和饮食之间有什么讲究吗？\n王老师：锻炼后是肌肉细胞的“进食时间”，它们渴望得到足够的蛋白质、水和维生素。运动后的两小时，是补充营养的最佳时机。",
     "Phóng viên: Sau khi vận động, chúng ta thường thấy vừa khát vừa đói, giữa vận động và ăn uống có điều gì cần chú ý không?\nThầy Vương: Sau khi tập luyện là giờ ăn của các tế bào cơ, chúng khao khát được nhận đủ protein, nước và vitamin. Hai giờ sau khi vận động là thời điểm tốt nhất để bổ sung dinh dưỡng.",
     ["又渴又饿 là vừa khát vừa đói, cấu trúc 又……又……. Còn 讲究 ở câu này là danh từ: điều cần chú ý.",
      "进食时间 là giờ ăn. Tác giả đặt cụm này trong ngoặc kép vì đây là cách nói nhân hóa: tế bào cơ cũng có giờ ăn. 最佳时机 là thời điểm tốt nhất."]),
    ("记者：王老师，您真不愧是这方面的专家，以后要是能定期和您做些交流就好了。\n王老师：这是我的联系方式，以后我们可以多联络。希望大家回去以后坚持锻炼，多多保重。",
     "Phóng viên: Thầy Vương, thầy thật xứng đáng là chuyên gia trong lĩnh vực này, sau này nếu có thể giao lưu định kỳ với thầy thì tốt quá.\nThầy Vương: Đây là cách liên lạc của tôi, sau này chúng ta có thể liên lạc nhiều hơn. Mong mọi người về rồi hãy kiên trì tập luyện, giữ gìn sức khỏe nhé.",
     ["不愧是 là thật xứng đáng là. 要是……就好了 là nếu… thì tốt quá, biểu thị mong muốn.",
      "多多保重 là xin hãy giữ gìn sức khỏe, một câu chào thân thiết khi chia tay."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 运动的学问",
    items=["Bài khóa là cuộc trò chuyện giữa 记者 (phóng viên) và 王老师 (thầy Vương)",
           "Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 运动的学问, dài một nghìn ba trăm mười tám chữ.",
         F(0, "Bài khóa là một cuộc trò chuyện trên truyền hình giữa 记者, tức là phóng viên, và 王老师, thầy Vương, một người tập khí công lâu năm."),
         F(1, "Thầy chia bài thành từng đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(2, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(3, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "").replace("\n", "")
    zsize = 54 if len(zh) <= 80 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("\n", " "), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Tóm tắt nội dung", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5)", size=36,
    items=["## 1. 气功的作用有哪些？ – 健身、增强体质、促进慢性病康复、辅助治疗疾病",
           "## 2. 健康包括哪些方面？ – 不生病、心理、社会交往 · 健康五要素",
           "## 3. 运动的学问有哪些？",
           "(1) 勤于运用大脑：左脑主管抽象思维，右脑主管形象思维",
           "(2) 贵在坚持：不要迁就、不能半途而废、有计划、有落实",
           "(3) 冬季健身好处多：紫外线、二氧化碳、心情、皮肤",
           "(4) 讲究科学：循序渐进、锻炼后进食"],
    say=["Chúng ta cùng nhìn lại bố cục của cả bài khóa. Bài tập năm trong sách gợi ý đúng bố cục này, bằng ba câu hỏi.",
         F(0, "Câu hỏi một: 气功的作用有哪些？ Khí công có những tác dụng gì? Trả lời: rèn luyện sức khỏe, tăng cường thể chất, giúp bệnh mãn tính hồi phục, và hỗ trợ điều trị bệnh."),
         F(1, "Câu hỏi hai: 健康包括哪些方面？ Sức khỏe bao gồm những phương diện nào? Không chỉ là không ốm đau, mà còn có tâm lý và giao tiếp xã hội; có người còn đưa ra năm yếu tố của sức khỏe."),
         F(2, "Câu hỏi ba: 运动的学问有哪些？ Những hiểu biết về vận động gồm những gì? Thầy Vương nêu bốn ý."),
         F(3, "Một là, phải chăm sử dụng bộ não: não trái phụ trách tư duy trừu tượng, não phải phụ trách tư duy hình tượng."),
         F(4, "Hai là, vận động quý ở kiên trì: không dễ dãi với bản thân, không bỏ dở nửa chừng, có kế hoạch và có thực hiện."),
         F(5, "Ba là, tập luyện mùa đông có nhiều lợi ích: tia tử ngoại, khí cacbonic ít hơn, tâm trạng thư thái, và còn tốt cho làn da."),
         F(6, "Bốn là, phải vận động khoa học: tiến dần từng bước, và ăn uống bổ sung dinh dưỡng đúng lúc sau khi tập. Bố cục này rất có ích khi các bạn kể lại nội dung bài khóa.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 逐", section="Ngữ pháp 注释", title="1. 逐 zhú – lần lượt từng…, theo thứ tự", size=40,
    items=["Giới từ: theo thứ tự, lần lượt từng cái một",
           "Cấu trúc: 逐 + danh từ / lượng từ đơn âm tiết → 逐年 · 逐月 · 逐日 · 逐个 · 逐字逐句",
           "Từ quen thuộc: 逐步 (từng bước) · 逐渐 (dần dần)",
           "最近有个调查，广大群众的健身意识在逐年提升。",
           "雨季快到了，对大大小小的水库，要逐个检查，以排除安全隐患。",
           "他花了一年多时间，逐字逐句地反复推敲，再三修改，终于完成了整套书的翻译工作。"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là giới từ 逐.",
         F(0, "逐 là giới từ, nghĩa là theo thứ tự, lần lượt từng cái một. Hán Việt là trục."),
         F(1, "Cấu trúc thường gặp: 逐 cộng một danh từ hoặc lượng từ đơn âm tiết, tạo thành những cụm như 逐年 là qua từng năm, 逐月 là qua từng tháng, 逐日 là qua từng ngày, 逐个 là từng cái một, và 逐字逐句 là từng chữ từng câu."),
         F(2, "Các bạn đã quen với hai từ 逐步, từng bước một, và 逐渐, dần dần. Chữ 逐 trong hai từ này cũng mang nghĩa lần lượt, từ từ."),
         F(3, "Ví dụ một, lấy từ bài khóa: 最近有个调查，广大群众的健身意识在逐年提升。 Gần đây có một cuộc điều tra, ý thức rèn luyện sức khỏe của đông đảo quần chúng tăng lên qua từng năm."),
         F(4, "Ví dụ hai: 雨季快到了，对大大小小的水库，要逐个检查，以排除安全隐患。 Mùa mưa sắp đến rồi, phải kiểm tra từng hồ chứa nước lớn nhỏ, để loại trừ nguy cơ mất an toàn."),
         F(5, "Ví dụ ba: 他花了一年多时间，逐字逐句地反复推敲，再三修改，终于完成了整套书的翻译工作。 Anh ấy mất hơn một năm, cân nhắc từng chữ từng câu, sửa đi sửa lại, cuối cùng đã hoàn thành việc dịch cả bộ sách. 推敲 là cân nhắc kỹ câu chữ.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập 逐: ghép 6 vế thành 3 đoạn văn (đề bài)", size=36,
    items=["A. 人类要生存和发展，社会要延续和进步，就必须将社会实践中积累起来的经验逐步完善起来",
           "B. 他们的小店开门了，由于经营有道",
           "C. 并把更成熟、完善的经验传给下一代",
           "D. 想当年他们的企业也是国内名牌，短短几个月就开发了十来个新品投放市场",
           "E. 同时符合市场需求，营业额逐日增加",
           "F. 产品产量逐月提高，资金迅速回笼"],
    say=["Luyện tập điểm ngữ pháp 逐. Sách yêu cầu: hãy ghép sáu vế câu dưới đây thành ba đoạn văn liền mạch. Thầy đọc từng vế nhé.",
         F(0, "Vế A: 人类要生存和发展，社会要延续和进步，就必须将社会实践中积累起来的经验逐步完善起来。 Loài người muốn sinh tồn và phát triển, xã hội muốn tiếp nối và tiến bộ, thì phải từng bước hoàn thiện những kinh nghiệm tích lũy được trong thực tiễn xã hội."),
         F(1, "Vế B: 他们的小店开门了，由于经营有道。 Cửa hàng nhỏ của họ đã khai trương, nhờ kinh doanh có phương pháp."),
         F(2, "Vế C: 并把更成熟、完善的经验传给下一代。 Đồng thời truyền lại những kinh nghiệm chín chắn, hoàn thiện hơn cho thế hệ sau."),
         F(3, "Vế D: 想当年他们的企业也是国内名牌，短短几个月就开发了十来个新品投放市场。 Nhớ năm xưa doanh nghiệp của họ cũng là thương hiệu nổi tiếng trong nước, chỉ trong vài tháng ngắn ngủi đã phát triển khoảng mười sản phẩm mới tung ra thị trường."),
         F(4, "Vế E: 同时符合市场需求，营业额逐日增加。 Đồng thời phù hợp với nhu cầu thị trường, doanh thu tăng lên từng ngày."),
         F(5, "Vế F: 产品产量逐月提高，资金迅速回笼。 Sản lượng tăng lên từng tháng, vốn nhanh chóng thu hồi. Các bạn hãy tạm dừng video và thử ghép nhé.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập 逐: đáp án", reveal=True, size=36,
    items=["(1) Vế A (……经验逐步完善起来) ghép với vế nào?",
           "Đáp án: A + C → ……就必须将……经验逐步完善起来，并把更成熟、完善的经验传给下一代。",
           "(2) Vế B (他们的小店开门了，由于经营有道) ghép với vế nào?",
           "Đáp án: B + E → 他们的小店开门了，由于经营有道，同时符合市场需求，营业额逐日增加。",
           "(3) Vế D (想当年他们的企业也是国内名牌……) ghép với vế nào?",
           "Đáp án: D + F → ……开发了十来个新品投放市场，产品产量逐月提高，资金迅速回笼。"],
    say=[F(0, "Bây giờ chúng ta xem đáp án. Câu một: vế A nói về kinh nghiệm của loài người, vậy nó ghép với vế nào?"),
         F(1, "Đáp án: A ghép với C. Vế C bắt đầu bằng 并把, đồng thời đem, nối tiếp ý từng bước hoàn thiện kinh nghiệm, rồi truyền kinh nghiệm cho thế hệ sau. Chữ 逐 ở đây nằm trong từ 逐步."),
         F(2, "Câu hai: vế B nói cửa hàng nhỏ khai trương, nhờ kinh doanh có phương pháp. Ghép với vế nào?"),
         F(3, "Đáp án: B ghép với E: 由于经营有道，同时符合市场需求，营业额逐日增加。 Nhờ kinh doanh có phương pháp, lại phù hợp nhu cầu thị trường, nên doanh thu tăng lên từng ngày."),
         F(4, "Câu ba: vế D nói năm xưa doanh nghiệp từng là thương hiệu nổi tiếng. Ghép với vế nào?"),
         F(5, "Đáp án: D ghép với F: 短短几个月就开发了十来个新品投放市场，产品产量逐月提高，资金迅速回笼。 Các bạn để ý: 逐日 và 逐月, từng ngày và từng tháng, đều là cách dùng của giới từ 逐.")])

add("bullets", chapter="Ngữ pháp: 归根到底", section="Ngữ pháp 注释", title="2. 归根到底 guīgēn-dàodǐ – suy cho cùng, xét đến cùng", size=38,
    items=["Thành phần chêm xen (插入语): nói từ gốc rễ của vấn đề · còn nói 归根结底",
           "Vị trí: đứng trước phần kết luận, thường trước 是 hoặc 都是",
           "运动健身归根到底是自己的事，胡乱对付其实是在骗自己，坚持运动也是培养人的意志力、完善人格的过程。",
           "年轻人在成长过程中会有很多不如意，归根结底都是因为和别人相比造成的。不看别人，只看自己是否有收获，那么幸福感每天都是满满的。"],
    say=["Điểm ngữ pháp thứ hai là 归根到底.",
         F(0, "归根到底 là một thành phần chêm xen, tiếng Trung gọi là 插入语, dùng để nói về vấn đề từ gốc rễ, tiếng Việt dịch là suy cho cùng, xét đến cùng. Cũng có thể nói 归根结底, nghĩa hoàn toàn giống nhau."),
         F(1, "Nó thường đứng ngay trước phần kết luận của câu, hay đi với 是 hoặc 都是."),
         F(2, "Ví dụ một, lấy từ bài khóa: 运动健身归根到底是自己的事，胡乱对付其实是在骗自己。 Rèn luyện sức khỏe suy cho cùng là việc của chính mình, đối phó qua loa thật ra là đang tự lừa mình."),
         F(3, "Ví dụ hai: 年轻人在成长过程中会有很多不如意，归根结底都是因为和别人相比造成的。 Người trẻ trong quá trình trưởng thành sẽ gặp nhiều điều không như ý, suy cho cùng đều là do so sánh mình với người khác. 不看别人，只看自己是否有收获，那么幸福感每天都是满满的。 Không nhìn người khác, chỉ xem bản thân có thu hoạch gì không, thì ngày nào cũng tràn đầy hạnh phúc.")])

add("bullets", section="Ngữ pháp 注释", title="Các cách nói gần nghĩa với 归根到底", size=38,
    items=["说到底 · 从根本上说 · 一句话 · 说白了 · 说穿了",
           "地区差别、城乡差别、贫富差别等问题，从根本上说，都是经济社会发展不平衡的问题。",
           "据说国外很多街头艺人都是技艺超群，完全可以到音乐厅去演奏。但为什么他们会在街头或地铁站里表演呢？说白了就是一种生活方式。"],
    say=["Sách giới thiệu thêm một số cách nói gần nghĩa với 归根到底.",
         F(0, "Đó là: 说到底, nói cho cùng; 从根本上说, nói từ gốc rễ; 一句话, tóm lại một câu; 说白了, nói thẳng ra; và 说穿了, nói toạc ra. Hai cách 说白了 và 说穿了 mang màu sắc khẩu ngữ hơn."),
         F(1, "Ví dụ: 地区差别、城乡差别、贫富差别等问题，从根本上说，都是经济社会发展不平衡的问题。 Những vấn đề như chênh lệch vùng miền, chênh lệch thành thị và nông thôn, chênh lệch giàu nghèo, xét từ gốc rễ, đều là vấn đề phát triển kinh tế xã hội không cân bằng."),
         F(2, "Ví dụ: 据说国外很多街头艺人都是技艺超群，完全可以到音乐厅去演奏。但为什么他们会在街头或地铁站里表演呢？说白了就是一种生活方式。 Nghe nói nhiều nghệ sĩ đường phố ở nước ngoài có tay nghề xuất chúng, hoàn toàn có thể biểu diễn ở nhà hát. Nhưng tại sao họ lại biểu diễn ngoài phố hay trong ga tàu điện ngầm? Nói thẳng ra, đó chỉ là một lối sống.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: chọn vị trí cho thành phần chêm xen", reveal=True, size=36,
    items=["(1) A他爸爸上周B刚给他寄来了生活费，C他却告诉我没钱，D就是不想借。（说穿了）",
           "Đáp án: D → ……他却告诉我没钱，说穿了，就是不想借。",
           "(2) 从今天起，A她的电话、短信、邮件，B我一概不理，C凡是与她有关的消息我也不听，D我和她彻底绝交了。（一句话）",
           "Đáp án: D → ……凡是与她有关的消息我也不听，一句话，我和她彻底绝交了。",
           "(3) 所谓史学，A就是B研究和阐述人类社会历史C发展过程D及其规律的一门学科和科学。（说到底）",
           "Đáp án: A → 所谓史学，说到底，就是研究和阐述人类社会历史发展过程及其规律的一门学科和科学。"],
    say=[F(0, "Luyện tập: chọn vị trí thích hợp cho thành phần chêm xen trong ngoặc. Câu một: 他爸爸上周刚给他寄来了生活费，他却告诉我没钱，就是不想借。 Bố cậu ta tuần trước vừa gửi tiền sinh hoạt, vậy mà cậu ta lại bảo tôi là không có tiền. Đặt 说穿了 ở đâu? Các bạn tạm dừng và suy nghĩ nhé."),
         F(1, "Đáp án: vị trí D. 他却告诉我没钱，说穿了，就是不想借。 Nói toạc ra, chỉ là không muốn cho mượn. Thành phần chêm xen đứng trước phần kết luận."),
         F(2, "Câu hai: 从今天起，她的电话、短信、邮件，我一概不理，凡是与她有关的消息我也不听，我和她彻底绝交了。 Từ hôm nay, điện thoại, tin nhắn, thư của cô ấy tôi đều mặc kệ, tin tức gì liên quan đến cô ấy tôi cũng không nghe, tôi tuyệt giao hẳn với cô ấy. Đặt 一句话 ở đâu?"),
         F(3, "Đáp án: vị trí D. 一句话，我和她彻底绝交了。 Tóm lại một câu, tôi tuyệt giao với cô ấy rồi. 一句话 dùng để tóm tắt các ý đã kể ở trước."),
         F(4, "Câu ba: 所谓史学，就是研究和阐述人类社会历史发展过程及其规律的一门学科和科学。 Cái gọi là sử học là một môn khoa học nghiên cứu và trình bày quá trình phát triển của lịch sử xã hội loài người cùng quy luật của nó. Đặt 说到底 ở đâu?"),
         F(5, "Đáp án: vị trí A. 所谓史学，说到底，就是研究……的一门学科和科学。 Sử học, nói cho cùng, chính là môn khoa học nghiên cứu lịch sử. 说到底 đứng ngay trước 就是, phần kết luận.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 胡乱 – 随便", section="Phân biệt từ 词语辨析", title="Phân biệt 胡乱 và 随便 (1): từ loại",
    common="Giống nhau: đều có nghĩa qua loa, không nghiêm túc (马虎、不认真). Ví dụ: 他胡乱/随便吃了两口就走了。",
    cols=[{"head": "胡乱",
           "lines": ["(1) Phó từ: chỉ đứng trước động từ, không làm vị ngữ, không bổ nghĩa cho danh từ",
                     "Đúng: 他在纸上胡乱画了几笔。",
                     "Sai: 他这个人说话很胡乱。"]},
          {"head": "随便",
           "lines": ["(1) Tính từ: làm được vị ngữ, bổ nghĩa được cho danh từ",
                     "Đúng: A：中午吃什么呢？B：随便。",
                     "Đúng: 他不是个随便的人。"]}],
    say=["Tiếp theo là phần phân biệt từ: 胡乱 và 随便. Hai từ này đều có thể dịch là qua loa, tùy tiện, nên rất dễ dùng lẫn.",
         "Điểm giống nhau: cả hai đều biểu thị sự qua loa, không nghiêm túc. Ví dụ: 他胡乱吃了两口就走了, hoặc 他随便吃了两口就走了, đều đúng. Anh ấy ăn qua loa hai miếng rồi đi.",
         F(0, "Điểm khác thứ nhất là từ loại. 胡乱 là phó từ, chỉ có thể đứng trước động từ, không làm vị ngữ, cũng không bổ nghĩa cho danh từ."),
         F(0, "Ví dụ: 他在纸上胡乱画了几笔 là đúng, anh ấy vẽ bừa vài nét lên giấy, vì 胡乱 đứng trước động từ 画. Nhưng 他这个人说话很胡乱 là sai, vì ở đây 胡乱 làm vị ngữ."),
         F(1, "Còn 随便 là tính từ, có thể làm vị ngữ, có thể bổ nghĩa cho danh từ. Hỏi: 中午吃什么呢？ Trưa nay ăn gì? Trả lời: 随便。 Tùy, gì cũng được. Câu này đúng."),
         F(1, "Và 他不是个随便的人。 Anh ấy không phải là người tùy tiện. Ở đây 随便 bổ nghĩa cho danh từ 人, cũng đúng.")])

add("compare", section="Phân biệt từ 词语辨析", title="Phân biệt 胡乱 và 随便 (2): dạng lặp và liên từ",
    common="Tiếp theo: dạng lặp AABB, và cách dùng làm liên từ.",
    cols=[{"head": "胡乱",
           "lines": ["(2) Không có dạng lặp AABB",
                     "Sai: 胡胡乱乱",
                     "(3) Không dùng làm liên từ"]},
          {"head": "随便",
           "lines": ["(2) Có dạng lặp AABB: 随随便便",
                     "Đúng: 我对他这种随随便便的工作态度很不满。",
                     "(3) Làm liên từ, nghĩa như 无论 (bất kể)",
                     "Đúng: 随便我怎么说，他就是不听。"]}],
    say=[F(0, "Điểm khác thứ hai: 胡乱 không có dạng lặp AABB. Nói 胡胡乱乱 là sai."),
         F(1, "Còn 随便 có dạng lặp 随随便便. Ví dụ: 我对他这种随随便便的工作态度很不满。 Tôi rất không hài lòng với thái độ làm việc tùy tiện như thế của anh ta."),
         F(0, "Điểm khác thứ ba: 胡乱 không có cách dùng làm liên từ."),
         F(1, "Còn 随便 có thể làm liên từ, nghĩa giống 无论, bất kể. Ví dụ: 随便我怎么说，他就是不听。 Bất kể tôi nói thế nào, anh ta cũng không nghe."),
         "Mẹo nhớ: 胡乱 chỉ là phó từ, luôn đứng trước động từ, và mang ý bừa bãi, lộn xộn; còn 随便 linh hoạt hơn nhiều: làm vị ngữ, làm định ngữ, lặp thành 随随便便, và làm liên từ được."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: Đúng hay sai?", reveal=True, size=38,
    items=["(1) 我当时只是随便答应的，没想到他认真了。",
           "Đáp án: Đúng – 随便 đứng trước động từ 答应.",
           "(2) A：假期想去哪儿玩儿？ B：胡乱。",
           "Đáp án: Sai – 胡乱 không làm vị ngữ, không đứng một mình. Sửa: B：随便。",
           "(3) 话剧也好，京剧也好，胡乱什么戏，他都爱看。",
           "Đáp án: Sai – 胡乱 không làm liên từ. Sửa: 随便什么戏，他都爱看。",
           "(4) 无数事实告诉我们：没有人可以随随便便成功。",
           "Đáp án: Đúng – 随便 có dạng lặp 随随便便."],
    say=[F(0, "Bây giờ chúng ta làm thử. Câu một: 我当时只是随便答应的，没想到他认真了。 Lúc đó tôi chỉ tiện miệng nhận lời, không ngờ anh ấy lại tưởng thật. Đúng hay sai? Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: đúng. 随便 đứng trước động từ 答应, mang nghĩa tùy tiện, không suy nghĩ kỹ."),
         F(2, "Câu hai: 假期想去哪儿玩儿？ Kỳ nghỉ muốn đi đâu chơi? Trả lời: 胡乱。"),
         F(3, "Đáp án: sai. 胡乱 là phó từ, không thể đứng một mình làm câu trả lời. Phải nói: 随便。 Đi đâu cũng được."),
         F(4, "Câu ba: 话剧也好，京剧也好，胡乱什么戏，他都爱看。 Kịch nói cũng được, kinh kịch cũng được, vở gì anh ấy cũng thích xem."),
         F(5, "Đáp án: sai. Ở đây cần nghĩa bất kể, tức là liên từ, mà 胡乱 không làm liên từ được. Phải sửa thành: 随便什么戏，他都爱看。"),
         F(6, "Câu bốn: 无数事实告诉我们：没有人可以随随便便成功。 Vô số sự thật cho chúng ta biết: không ai có thể thành công một cách dễ dàng, tùy tiện."),
         F(7, "Đáp án: đúng. 随便 có dạng lặp AABB 随随便便. Câu này cũng là một câu nói rất hay, các bạn nên ghi nhớ.")])

# ======================= TU TỪ =======================
add("bullets", chapter="Tu từ: 大词小用", section="Tu từ 篇章修辞", title="Tu từ (7): Dùng từ lớn cho việc nhỏ (大词小用)", size=36,
    items=["Dùng từ có phạm vi, khái niệm lớn cho sự vật có phạm vi nhỏ → tô đậm, gây ấn tượng mạnh, thường hài hước",
           "王老师：……下狠心咬牙坚持，绝不能半途而废。 记者：王老师，您怎么好像在说我呢？我就不想虐待自己，所以很难坚持。",
           "(虐待 vốn là đối xử bằng thủ đoạn tàn bạo, ác độc; phóng viên chỉ là không kiên trì tập luyện)",
           "和朋友冷战了两周后，我们终于在老师的斡旋下恢复了邦交正常化。",
           "忽听一声门响，原来是妈妈大人光临了。"],
    say=["Phần cuối cùng về lý thuyết là một thủ pháp tu từ: 大词小用, tức là dùng từ lớn cho việc nhỏ.",
         F(0, "Định nghĩa: đem một từ có phạm vi, khái niệm lớn, dùng cho một sự vật có phạm vi, khái niệm nhỏ, để tô đậm và tạo ấn tượng mạnh cho người đọc. Hiệu quả thường rất hài hước."),
         F(1, "Ví dụ một, lấy từ bài khóa: thầy Vương khuyên phải nghiến răng kiên trì, phóng viên đáp: 我就不想虐待自己，所以很难坚持。 Tôi chẳng muốn ngược đãi bản thân, nên rất khó kiên trì."),
         F(2, "Từ 虐待 vốn có nghĩa là đối xử bằng thủ đoạn tàn bạo, độc ác. Nhưng phóng viên chỉ đơn giản là lười, không kiên trì tập thể dục. Dùng một từ rất nặng cho một chuyện nhỏ như vậy tạo nên tiếng cười."),
         F(3, "Ví dụ hai: 和朋友冷战了两周后，我们终于在老师的斡旋下恢复了邦交正常化。 Sau hai tuần chiến tranh lạnh với bạn, nhờ thầy giáo hòa giải, chúng tôi cuối cùng đã bình thường hóa quan hệ ngoại giao. 冷战, 斡旋, 邦交正常化 vốn là từ ngữ chính trị giữa các quốc gia, ở đây dùng cho hai người bạn giận nhau."),
         F(4, "Ví dụ ba: 忽听一声门响，原来是妈妈大人光临了。 Chợt nghe tiếng cửa, hóa ra là mẹ đại nhân giá lâm. 大人 và 光临 là những từ rất trang trọng, dùng cho mẹ về nhà nghe vừa kính trọng vừa đáng yêu.")])

add("bullets", section="Tu từ 篇章修辞", title="Luyện tập: câu nào KHÔNG dùng 大词小用?", reveal=True, size=36,
    items=["(1) 昨天我们俩还一块儿逛街，今天他就不理我了，我一定得找他问个明白。",
           "(2) 经过几次谈判，我终于和父母签订了每周打游戏的条约。",
           "(3) 小儒放学回家……连忙冲妈妈喊：“妈妈，您赶紧来帮我捍卫电视，免得被爸爸占领了！”",
           "Câu nào không dùng 大词小用?",
           "Đáp án: câu (1) không dùng.",
           "Câu (2): 谈判、签订、条约 · Câu (3): 捍卫、占领"],
    say=[F(0, "Luyện tập: câu nào dưới đây không dùng thủ pháp dùng từ lớn cho việc nhỏ? Câu một: 昨天我们俩还一块儿逛街，今天他就不理我了，我一定得找他问个明白。 Hôm qua hai đứa còn đi dạo phố cùng nhau, hôm nay cậu ấy đã không thèm để ý đến tôi, tôi nhất định phải tìm cậu ấy hỏi cho ra lẽ."),
         F(1, "Câu hai: 经过几次谈判，我终于和父母签订了每周打游戏的条约。 Sau mấy lần đàm phán, tôi cuối cùng đã ký với bố mẹ một hiệp ước về việc chơi điện tử mỗi tuần."),
         F(2, "Câu ba: 小儒放学回家，要看电视。可是又着急上厕所，担心爸爸占用电视，连忙冲妈妈喊：妈妈，您赶紧来帮我捍卫电视，免得被爸爸占领了！ Tiểu Nho tan học về muốn xem tivi, nhưng lại vội đi vệ sinh, sợ bố chiếm tivi, liền gọi mẹ: Mẹ ơi, mẹ mau đến bảo vệ tivi giúp con, kẻo bị bố chiếm đóng mất!"),
         F(3, "Các bạn tạm dừng và chọn nhé."),
         F(4, "Đáp án: câu một không dùng. Mọi từ ngữ trong câu đều bình thường, đúng với sự việc."),
         F(5, "Câu hai dùng 谈判, đàm phán, 签订, ký kết, và 条约, hiệp ước, vốn là từ ngữ ngoại giao giữa các nước. Câu ba dùng 捍卫, bảo vệ, và 占领, chiếm đóng, vốn là từ ngữ quân sự, ở đây chỉ dùng cho chuyện tranh nhau cái tivi.")])

add("bullets", section="Tu từ 篇章修辞", title="Bài tập 4: Chỉ ra 大词小用 trong đoạn văn (1)", reveal=True, size=36,
    items=["(1) 平静的教室里爆发了第三次世界大战。",
           "Đáp án: 爆发了第三次世界大战 (chỉ một trận cãi nhau ầm ĩ trong lớp)",
           "(2) ……年龄稍长，我的野心膨胀，开始了移民扩张：获奖的作文和古典名著都成了我涉猎的对象。",
           "Đáp án: 野心膨胀、移民扩张 (chỉ việc mở rộng phạm vi đọc sách)"],
    say=[F(0, "Bài tập bốn trong sách: chỉ ra cách dùng từ lớn cho việc nhỏ trong các đoạn văn. Đoạn một: 平静的教室里爆发了第三次世界大战。 Trong lớp học đang yên tĩnh bỗng nổ ra chiến tranh thế giới thứ ba. Các bạn tìm thử nhé."),
         F(1, "Đáp án: 爆发了第三次世界大战. Thực ra chỉ là học sinh cãi nhau, nô đùa ầm ĩ trong lớp, nhưng tác giả dùng cụm từ chiến tranh thế giới để phóng đại, gây cười."),
         F(2, "Đoạn hai: 我从小就喜欢读书。开始，我读的是带拼音的童话书，年龄稍长，我的野心膨胀，开始了移民扩张：获奖的作文和古典名著都成了我涉猎的对象。 Tôi thích đọc sách từ nhỏ. Lúc đầu tôi đọc truyện cổ tích có phiên âm, lớn lên một chút, dã tâm của tôi bành trướng, tôi bắt đầu di dân mở rộng lãnh thổ: những bài văn đoạt giải và các tác phẩm kinh điển đều trở thành đối tượng để tôi đọc qua."),
         F(3, "Đáp án: 野心膨胀 và 移民扩张. Dã tâm bành trướng, di dân mở rộng lãnh thổ, vốn là từ ngữ về chính trị, chiến tranh, ở đây chỉ việc mở rộng phạm vi đọc sách. 涉猎 là đọc lướt qua nhiều loại sách.")])

add("bullets", section="Tu từ 篇章修辞", title="Bài tập 4: Chỉ ra 大词小用 trong đoạn văn (2)", reveal=True, size=36,
    items=["(3) 初学自行车的我，竟想对一个小土坡发起进攻。我先后退几步，然后上车猛骑过去，“砰！轰！”沙土飞溅，灰尘飞扬，我连人带车摔了个四脚朝天。",
           "Đáp án: 发起进攻 (chỉ việc đạp xe lên con dốc nhỏ)",
           "(4) 爸爸、妈妈和我，在家里谁也不服谁，形成了三国鼎立之势。",
           "Đáp án: 三国鼎立之势 (chỉ ba người trong nhà không ai chịu ai)"],
    say=[F(0, "Đoạn ba: 初学自行车的我，竟想对一个小土坡发起进攻。我先后退几步，然后上车猛骑过去，砰！轰！沙土飞溅，灰尘飞扬，我连人带车摔了个四脚朝天。 Tôi mới tập đi xe đạp mà lại muốn phát động tấn công một con dốc đất nhỏ. Tôi lùi lại mấy bước, rồi lên xe đạp thật mạnh lao tới, rầm một cái, đất cát bắn tung, bụi bay mù mịt, tôi ngã chổng vó cả người lẫn xe."),
         F(1, "Đáp án: 发起进攻, phát động tấn công, vốn là từ quân sự, ở đây chỉ việc đạp xe lên một con dốc nhỏ. 四脚朝天 là ngã ngửa, chổng bốn vó lên trời."),
         F(2, "Đoạn bốn: 爸爸、妈妈和我，在家里谁也不服谁，形成了三国鼎立之势。 Bố, mẹ và tôi, ở nhà chẳng ai chịu ai, tạo thành thế chân vạc của ba nước."),
         F(3, "Đáp án: 三国鼎立之势, thế chân vạc thời Tam Quốc, vốn chỉ ba nước Ngụy, Thục, Ngô chia ba thiên hạ, ở đây chỉ ba người trong một gia đình. Rất hài hước phải không các bạn?")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ được đánh dấu", size=40,
    items=["坚定 (坚) → 坚韧 · 坚持 · 坚强 · 坚决",
           "走廊 (廊) → 画廊 · 长廊 · 回廊 · 游廊",
           "误解 (解) → 理解 · 了解 · 讲解 · 谅解",
           "预期 (期) → 学期 · 星期 · 周期 · 时期",
           "衰退 (衰) → 衰老 · 衰弱 · 衰落 · 衰竭"],
    say=["Phần luyện tập. Bài tập một: mô phỏng ví dụ, viết thêm các từ khác. Chú ý: trong sách, chữ được đánh dấu chấm ở dưới là chữ chung, có khi là chữ đầu, có khi là chữ sau.",
         F(0, "Ví dụ mẫu: 坚定, chữ được đánh dấu là chữ đầu 坚. Ta có 坚韧，坚持，坚强，坚决. Tức là bền bỉ, kiên trì, kiên cường, và kiên quyết."),
         F(1, "走廊, chữ được đánh dấu là chữ sau 廊. Ta có 画廊，长廊，回廊，游廊. Tức là phòng tranh, hành lang dài, hành lang vòng quanh, và hành lang trong vườn để dạo chơi."),
         F(2, "误解, chữ được đánh dấu là chữ sau 解. Ta có 理解，了解，讲解，谅解. Tức là hiểu, tìm hiểu, giảng giải, và thông cảm, lượng thứ."),
         F(3, "预期, chữ được đánh dấu là chữ sau 期. Ta có 学期，星期，周期，时期. Tức là học kỳ, tuần lễ, chu kỳ, và thời kỳ."),
         F(4, "衰退, chữ được đánh dấu là chữ đầu 衰. Ta có 衰老，衰弱，衰落，衰竭. Tức là già yếu, suy nhược, suy tàn, và suy kiệt.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Hoàn thành câu bằng từ cho sẵn (1)", reveal=True, size=38,
    items=["(1) A：你对中国了解得如此深入，真是个中国通。 B：____。（不敢当）",
           "Đáp án: B：哪里哪里，中国通我可不敢当，我还要继续努力呢。",
           "(2) 产品的销量____。（逐年）",
           "Đáp án: 产品的销量逐年增加。",
           "(3) 面对市场竞争，____。（首要）",
           "Đáp án: 面对市场竞争，首要的任务是提高产品质量。"],
    say=[F(0, "Bài tập hai: dùng từ cho sẵn để hoàn thành câu. Câu một, dùng 不敢当: 你对中国了解得如此深入，真是个中国通。 Bạn hiểu Trung Quốc sâu sắc như vậy, đúng là một người am hiểu Trung Quốc. 中国通 là người rất thạo về Trung Quốc. Bạn B sẽ đáp thế nào?"),
         F(1, "Đáp án gợi ý: 哪里哪里，中国通我可不敢当，我还要继续努力呢。 Đâu có đâu có, tôi không dám nhận là người thạo Trung Quốc đâu, tôi còn phải cố gắng nhiều."),
         F(2, "Câu hai, dùng 逐年: 产品的销量…… Lượng tiêu thụ sản phẩm thế nào?"),
         F(3, "Đáp án gợi ý: 产品的销量逐年增加。 Lượng tiêu thụ sản phẩm tăng lên qua từng năm. Cũng có thể nói 逐年下降, giảm dần qua từng năm."),
         F(4, "Câu ba, dùng 首要: 面对市场竞争…… Đối mặt với cạnh tranh thị trường, thì sao?"),
         F(5, "Đáp án gợi ý: 面对市场竞争，首要的任务是提高产品质量。 Đối mặt với cạnh tranh thị trường, nhiệm vụ hàng đầu là nâng cao chất lượng sản phẩm.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Hoàn thành câu bằng từ cho sẵn (2)", reveal=True, size=38,
    items=["(4) 对孩子的坏习惯____。（迁就）",
           "Đáp án: 对孩子的坏习惯绝不能迁就。",
           "(5) 无论做什么事情____。（半途而废）",
           "Đáp án: 无论做什么事情都不能半途而废。",
           "(6) 他在这个专业成就非凡，____。（不愧）",
           "Đáp án: 他在这个专业成就非凡，不愧是著名的专家。"],
    say=[F(0, "Câu bốn, dùng 迁就: 对孩子的坏习惯…… Đối với thói quen xấu của trẻ thì sao?"),
         F(1, "Đáp án gợi ý: 对孩子的坏习惯绝不能迁就。 Đối với thói quen xấu của trẻ, tuyệt đối không được chiều theo."),
         F(2, "Câu năm, dùng 半途而废: 无论做什么事情…… Bất kể làm việc gì thì sao?"),
         F(3, "Đáp án gợi ý: 无论做什么事情都不能半途而废。 Bất kể làm việc gì cũng không được bỏ dở nửa chừng. Nhớ là 无论 thường đi với 都."),
         F(4, "Câu sáu, dùng 不愧: 他在这个专业成就非凡…… Anh ấy có thành tựu phi thường trong chuyên ngành này."),
         F(5, "Đáp án gợi ý: 不愧是著名的专家。 Thật xứng đáng là chuyên gia nổi tiếng. Nhớ mẫu 不愧是 cộng danh từ nhé.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống", reveal=True, size=34,
    items=["## Từ cho sẵn: 气功 · 徒弟 · 群众 · 协会 · 剑",
           "(1) 我是武术___的成员，每天我们都在公园里练习，有时练习___，有时练习太极___。现在广大___的健身意识都增强了，我还收了好几个___呢。",
           "Đáp án: 协会 · 气功 · 剑 · 群众 · 徒弟",
           "## Từ cho sẵn: 预期 · 定期 · 钙 · 蛋白质 · 急于求成",
           "(2) 最近的一次体检结果显示，我有点儿缺___。大夫让我多晒晒太阳，多补充___，然后___到医院检查。但是补钙也不能___，只要每天坚持，就能达到___的效果。",
           "Đáp án: 钙 · 蛋白质 · 定期 · 急于求成 · 预期"],
    say=[F(0, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn một có năm từ: 气功，徒弟，群众，协会，剑."),
         F(1, "我是武术什么的成员，每天我们都在公园里练习，有时练习什么，有时练习太极什么。现在广大什么的健身意识都增强了，我还收了好几个什么呢。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 武术协会的成员，有时练习气功，有时练习太极剑，广大群众的健身意识，收了好几个徒弟。 Tôi là thành viên hiệp hội võ thuật, có lúc tập khí công, có lúc tập Thái cực kiếm, ý thức rèn luyện của quần chúng đã tăng lên, tôi còn nhận mấy người đồ đệ nữa."),
         F(3, "Đoạn hai có năm từ: 预期，定期，钙，蛋白质，急于求成."),
         F(4, "最近的一次体检结果显示，我有点儿缺什么。大夫让我多晒晒太阳，多补充什么，然后什么到医院检查。但是补钙也不能什么，只要每天坚持，就能达到什么的效果。"),
         F(5, "Đáp án: 有点儿缺钙，多补充蛋白质，定期到医院检查，补钙也不能急于求成，达到预期的效果。 Kết quả khám sức khỏe cho thấy tôi hơi thiếu canxi, bác sĩ bảo tôi phơi nắng nhiều, bổ sung protein, khám định kỳ; nhưng bổ sung canxi cũng không được nóng vội, chỉ cần kiên trì hằng ngày là đạt hiệu quả như mong đợi.")])

add("bullets", section="Luyện tập 练习", title="Mở rộng 扩展: nghĩa của từng yếu tố trong từ", size=34,
    items=["偏差: 偏 lệch, nghiêng + 差 sai sót → sai lệch · 名额: 名 tên + 额 số lượng quy định → chỉ tiêu",
           "致辞: 致 bày tỏ với người khác + 辞 lời lẽ → phát biểu · 屏障: 屏 che chắn + 障 vật che chắn → rào chắn",
           "倾斜: 倾 nghiêng, lệch + 斜 không ngay → nghiêng · 清除: 清 sạch hết + 除 bỏ đi → loại bỏ",
           "手势: 手 bàn tay + 势 tư thế → cử chỉ tay · 挽回: 挽 xoay chuyển, kéo + 回 trở lại → cứu vãn",
           "威力: 威 uy thế khiến người nể sợ + 力 sức mạnh → uy lực · 挑衅: 挑 gây chuyện + 衅 tranh chấp → khiêu khích",
           "压榨: 压 đè, ép + 榨 ép cho ra → ép, bóc lột · 压制: 压 dùng sức mạnh khuất phục + 制 hạn chế → áp chế"],
    say=["Phần mở rộng của sách giúp các bạn làm quen với nghĩa của từng yếu tố trong từ. Hiểu nghĩa từng chữ thì nhớ từ rất nhanh.",
         F(0, "偏差: chữ đầu 偏 là lệch, nghiêng, chữ sau là sai sót, ghép lại là sai lệch. 名额: 名 là tên, 额 là số lượng quy định, ghép lại là chỉ tiêu, số suất."),
         F(1, "致辞: 致 là bày tỏ với người khác, 辞 là lời lẽ, ghép lại là đọc lời phát biểu. 屏障: chữ đầu là che chắn, 障 là vật dùng để che chắn, phòng vệ, ghép lại là bức rào chắn."),
         F(2, "倾斜: 倾 là nghiêng, lệch, 斜 là không ngay, ghép lại là nghiêng. 清除: 清 là sạch hết, không còn chút nào, 除 là bỏ đi, ghép lại là loại bỏ sạch."),
         F(3, "手势: 手 là bàn tay, 势 là tư thế, ghép lại là cử chỉ tay. 挽回: 挽 là xoay chuyển, kéo lại, 回 là trở về, ghép lại là cứu vãn, gỡ lại."),
         F(4, "威力: 威 là uy thế khiến người ta kính sợ, 力 là sức mạnh, ghép lại là uy lực. 挑衅: chữ đầu là gây chuyện thị phi, 衅 là tranh chấp, ghép lại là khiêu khích."),
         F(5, "压榨: 压 là đè, ép, 榨 là dùng sức ép cho chảy ra, ghép lại là ép, nghĩa bóng là bóc lột. 压制: 压 là dùng sức mạnh khuất phục, 制 là hạn chế, ràng buộc, ghép lại là áp chế, đè nén.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 31", size=36,
    items=["Từ vựng trọng tâm: 不敢当 · 逐年 · 首要 · 迁就 · 半途而废 · 归根到底 · 循序渐进 · 急于求成 · 不愧",
           "Ngữ pháp: 逐 (逐年、逐个、逐字逐句) · 归根到底 = 归根结底 = 说到底、说白了、说穿了",
           "Phân biệt: 胡乱 (chỉ là phó từ) ≠ 随便 (tính từ, lặp 随随便便, làm liên từ)",
           "Tu từ: 大词小用 – 虐待自己、邦交正常化、妈妈大人光临",
           "## Bài tập về nhà",
           "Viết bài văn không dưới 400 chữ với đề 运动健身好处多: bạn rèn luyện sức khỏe như thế nào?"],
    say=["Chúng ta cùng tổng kết bài ba mươi mốt.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 不敢当，逐年，首要，迁就，半途而废，归根到底，循序渐进，急于求成，不愧."),
         F(1, "Về ngữ pháp: 逐 là giới từ, nghĩa là lần lượt từng…, như 逐年，逐个，逐字逐句. 归根到底 là thành phần chêm xen, nghĩa là suy cho cùng, cũng nói 归根结底, và gần nghĩa với 说到底，说白了，说穿了."),
         F(2, "Về phân biệt từ: 胡乱 chỉ là phó từ, luôn đứng trước động từ; 随便 là tính từ, có dạng lặp 随随便便, và còn làm liên từ được với nghĩa bất kể."),
         F(3, "Về tu từ: 大词小用 là dùng từ lớn cho việc nhỏ, như 虐待自己，邦交正常化，妈妈大人光临, tạo hiệu quả hài hước, gây ấn tượng."),
         F(5, "Bài tập về nhà, theo phần vận dụng của sách: các bạn hãy lấy đề 运动健身好处多, rèn luyện sức khỏe có nhiều lợi ích, viết một bài văn không dưới bốn trăm chữ, kể xem bạn thích môn thể thao nào, và bạn giữ gìn sức khỏe bằng cách vận động như thế nào. Hãy thử dùng 逐，归根到底, và một câu dùng từ lớn cho việc nhỏ nhé."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Hẹn gặp lại các bạn ở bài ba mươi hai: 有时，不妨悲伤, Đôi khi, buồn một chút cũng không sao. Chúc các bạn học tốt và luôn khỏe mạnh!"])

lesson = {
    "title": "HSK 6 (Hạ) – Bài 31: 运动的学问 (Những hiểu biết về vận động)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh; cụm dài trước)
    "tts_replace": {"着重": "酌重",        # zhuózhòng
                    "间接": "建接",        # jiànjiē
                    "品行": "品形",        # pǐnxíng
                    "更为": "更维",        # gèngwéi
                    "勉强": "勉抢",        # miǎnqiǎng
                    "稍长": "稍涨",        # shāo zhǎng
                    "朝天": "潮天",        # cháotiān
                    "冲妈妈": "铳妈妈",    # chòng
                    "散射": "伞射",        # sǎnshè
                    "偏差": "偏插",        # piānchā
                    "差别": "插别",        # chābié
                    "屏": "平",            # píng (屏障)
                    "挑衅": "窕衅"},       # tiǎoxìn
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai31.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
