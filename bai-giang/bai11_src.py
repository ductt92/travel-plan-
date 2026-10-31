#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Thượng) – Bài 11 «我不在时，猫在干什么？». Chạy để sinh bai11.json."""
import json
import os

TAG = "HSK 6 (Thượng) · Bài 11 · 我不在时，猫在干什么？"
slides = []


def add(type_, chapter=None, section="", **kw):
    s = {"type": type_, "section": section, **kw}
    if chapter:
        s["chapter"] = chapter
    slides.append(s)


def F(i, t, **kw):
    return {"t": t, "f": i, **kw}


# ======================= MỞ ĐẦU =======================
# Tên bài có 10 chữ (kể cả dấu câu), vừa một dòng chữ cỡ lớn nên giữ nguyên.
add("title", chapter="Mở đầu",
    top="Giáo trình chuẩn HSK 6 – Quyển Thượng",
    zh="我不在时，猫在干什么？", py="Wǒ bú zài shí, māo zài gàn shénme?",
    vi="Bài 11: Các chú mèo làm gì khi tôi đi vắng?",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Thượng.",
         "Hôm nay chúng ta học bài mười một: 我不在时，猫在干什么？ Nghĩa là: Các chú mèo làm gì khi tôi đi vắng?",
         "Bài này thuộc Chủ đề ba, 多彩社会, Xã hội muôn màu. Bài khóa kể về anh Tiền Tiểu Kỳ nuôi ba chú mèo, mỗi chú một tính cách. Anh rất tò mò không biết lúc mình đi vắng thì lũ mèo làm gì, nên đã tự tay lắp cả một hệ thống camera hiện đại để theo dõi chúng.",
         "Kết quả theo dõi vừa buồn cười vừa bất ngờ. Và hệ thống ấy còn giúp anh nhiều việc khác nữa. Chúng ta cùng tìm hiểu nhé."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài khóa: ba chú mèo nhà Tiền Tiểu Kỳ và hệ thống camera giám sát",
           "Nắm vững 46 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: phó từ 统统, cấu trúc 以……为……, cách nói 该干吗干吗",
           "Phân biệt 急切 và 急忙",
           "Mở rộng: câu sai do ý không rõ ràng (表意不明) và sắp xếp câu theo trình tự kể"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa: tính cách của ba chú mèo nhà Tiền Tiểu Kỳ, và hệ thống camera giám sát mà anh tự lắp đặt đã phát hiện ra điều gì."),
         F(1, "Thứ hai, nắm vững bốn mươi sáu từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học ba điểm ngữ pháp: phó từ 统统, nghĩa là tất cả, toàn bộ; cấu trúc văn viết 以其中一只猫为例, tức là lấy cái này làm cái kia; và cách nói khẩu ngữ 该干吗干吗, nghĩa là việc gì cần làm thì cứ làm."),
         F(3, "Thứ tư, phân biệt hai từ rất dễ nhầm: 急切 và 急忙."),
         F(4, "Thứ năm, phần mở rộng: nhận biết câu sai do ý không rõ ràng, tiếng Trung gọi là 表意不明, và luyện sắp xếp các vế câu theo đúng trình tự kể."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Câu hỏi khởi động: Mèo thích làm gì?", size=38,
    items=["你养过猫吗？猫喜欢做什么？ – Bạn đã từng nuôi mèo chưa? Mèo thích làm gì?",
           "A. 在窗台上晒太阳 – phơi nắng trên bậu cửa sổ · B. 在门口迎接主人 – đón chủ ở cửa",
           "C. 抓老鼠 – bắt chuột · D. 梳理自己的毛发 – chải chuốt bộ lông của mình",
           "E. 喝水 – uống nước · F. 睡觉 – ngủ",
           "Đáp án gợi ý: ảnh (1) F · (2) E · (3) B · (4) D · (5) C · (6) A"],
    say=["Chúng ta bắt đầu bằng phần khởi động. Câu hỏi đầu tiên rất gần gũi với những ai yêu động vật.",
         F(0, "你养过猫吗？猫喜欢做什么？ Bạn đã từng nuôi mèo chưa? Mèo thích làm gì? Sách cho sáu bức ảnh, yêu cầu tìm nội dung tương ứng với từng ảnh."),
         F(1, "Lựa chọn A: 在窗台上晒太阳。 Phơi nắng trên bậu cửa sổ. Lựa chọn B: 在门口迎接主人。 Đứng ở cửa đón chủ."),
         F(2, "Lựa chọn C: 抓老鼠。 Bắt chuột. Lựa chọn D: 梳理自己的毛发。 Chải chuốt bộ lông của mình."),
         F(3, "Lựa chọn E: 喝水。 Uống nước. Lựa chọn F: 睡觉。 Ngủ."),
         F(4, "Đáp án gợi ý: ảnh một là con mèo cuộn tròn ngủ, chọn F. Ảnh hai là mèo đang liếm nước, chọn E. Ảnh ba là mèo ngồi ở cửa, chọn B. Ảnh bốn là mèo nằm duỗi người, chọn D. Ảnh năm là mèo rình chuột trên bãi cỏ, chọn C. Ảnh sáu là mèo nằm bên cửa sổ, chọn A. Lát nữa các bạn sẽ thấy, ba chú mèo trong bài khóa làm gần như đủ cả những việc này.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 好 (hào) và 理", size=36,
    items=["## 好 (hiếu, đọc hào): thích, ham",
           "好动 hiếu động · 好客 hiếu khách · 好奇 hiếu kỳ, tò mò · 好强 hiếu thắng, không chịu thua",
           "好学 ham học · 好胜 hiếu thắng · 好战 hiếu chiến · 爱好 sở thích · 喜好 yêu thích",
           "## 理 (lý): sắp xếp, xử lý, trông coi",
           "整理 sắp xếp · 梳理 chải chuốt · 管理 quản lý · 办理 làm thủ tục · 护理 chăm sóc (bệnh nhân) · 修理 sửa chữa",
           "自理 tự lo liệu · 处理 xử lý · 代理 đại lý · 理财 quản lý tiền bạc · 理发 cắt tóc · 经理 giám đốc"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo, rất có lợi cho người Việt vì hầu hết các chữ đều có âm Hán Việt quen thuộc.",
         F(0, "Nhóm thứ nhất có chữ hiếu, đọc thanh bốn, hào, nghĩa là thích, ham. Các bạn chú ý: khi mang nghĩa này, chữ ấy không đọc thanh ba như trong từ 你好."),
         F(1, "好动，好客，好奇，好强。 Tức là: hiếu động, hiếu khách, hiếu kỳ tức tò mò, và hiếu thắng, không chịu thua kém. Trong bài khóa, chú mèo Bạch Bạch được tả là 快活而好动, vui vẻ và hiếu động; còn anh chủ thì 很好奇, rất tò mò."),
         F(2, "好学，好胜，好战，爱好，喜好。 Tức là: ham học, hiếu thắng, hiếu chiến, sở thích, và yêu thích."),
         F(3, "Nhóm thứ hai có chữ 理, Hán Việt là lý, nghĩa là sắp xếp, xử lý, trông coi."),
         F(4, "整理，梳理，管理，办理，护理，修理。 Tức là: sắp xếp, chải chuốt, quản lý, làm thủ tục, chăm sóc bệnh nhân, và sửa chữa. Trong bài, cô mèo Hỷ Nhi suốt ngày 整理自己的毛发, chải chuốt bộ lông, và 把自己梳理得漂亮而迷人."),
         F(5, "自理，处理，代理，理财，理发，经理。 Tức là: tự lo liệu, xử lý, đại lý, quản lý tiền bạc, cắt tóc, và giám đốc. Các bạn chú ý, 经理 là giám đốc, người quản lý, chứ không phải kinh lý.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 养 và 急", size=36,
    items=["## 养 (dưỡng): nuôi, trồng, chăm sóc",
           "养花 trồng hoa · 养草 trồng cỏ · 养猫 nuôi mèo · 养狗 nuôi chó · 养鸡 nuôi gà",
           "养鱼 nuôi cá · 养育 nuôi dạy · 饲养 chăn nuôi · 喂养 cho ăn, nuôi · 放养 thả nuôi",
           "## 急 (cấp): gấp, vội, khẩn cấp",
           "急切 nôn nóng · 急忙 vội vàng · 急诊 cấp cứu · 急病 bệnh cấp tính · 急救 sơ cứu",
           "急事 việc gấp · 急需 cần gấp · 急用 dùng gấp · 着急 sốt ruột · 紧急 khẩn cấp"],
    say=[F(0, "Nhóm thứ ba có chữ 养, Hán Việt là dưỡng, nghĩa là nuôi, trồng, chăm sóc. Tiếng Việt chỉ nói trồng hoa, nuôi mèo; còn tiếng Trung dùng chung một chữ 养 cho cả cây cối lẫn động vật."),
         F(1, "养花，养草，养猫，养狗，养鸡。 Tức là: trồng hoa, trồng cỏ, nuôi mèo, nuôi chó, nuôi gà. Câu đầu tiên của bài khóa là 钱小奇养了三只猫, Tiền Tiểu Kỳ nuôi ba con mèo."),
         F(2, "养鱼，养育，饲养，喂养，放养。 Tức là: nuôi cá, nuôi dạy, chăn nuôi, cho ăn, và thả nuôi. Từ 饲养 là từ mới của bài."),
         F(3, "Nhóm cuối cùng có chữ 急, Hán Việt là cấp, nghĩa là gấp, vội, như trong từ khẩn cấp."),
         F(4, "急切，急忙，急诊，急病，急救。 Tức là: nôn nóng, vội vàng, khám cấp cứu, bệnh cấp tính, và sơ cứu. Hai từ đầu tiên, 急切 và 急忙, chính là cặp từ chúng ta sẽ phân biệt trong bài này."),
         F(5, "急事，急需，急用，着急，紧急。 Tức là: việc gấp, cần gấp, dùng gấp, sốt ruột, và khẩn cấp."),
         "Các bạn thấy không, chỉ cần nắm nghĩa của một chữ gốc, ta có thể đoán được nghĩa của cả một nhóm từ. Hãy áp dụng cách này khi học từ mới nhé."])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng)
V = [
    ("流浪", "liúlàng", "lưu lãng", "động từ", "lưu lạc, lang thang", "这只流浪猫被一位好心人收养了。", "Con mèo hoang này được một người tốt bụng nhận nuôi.",
     "Động từ, nghĩa là sống lang thang, không nhà cửa, không nơi ở cố định. 流浪猫 là mèo hoang, 流浪狗 là chó hoang. Trong bài, chú mèo Đại Hoàng 原本是只流浪猫, vốn là một con mèo hoang."),
    ("淋", "lín", "lâm", "động từ", "dầm (mưa), dội vào", "他没带伞，被雨淋湿了。", "Anh ấy không mang ô, bị mưa làm ướt sũng.",
     "Động từ, nghĩa là nước hoặc mưa xối, dội lên người hay đồ vật. 淋雨 là dầm mưa. Trong bài, 淋着大雨 là đội mưa to mà đến."),
    ("拜访", "bàifǎng", "bái phỏng", "động từ", "thăm hỏi, thăm viếng", "春节期间，我去拜访了几位老同学。", "Dịp Tết, tôi đã đi thăm mấy người bạn học cũ.",
     "Động từ, nghĩa là đến thăm, là cách nói lịch sự, trang trọng. Trong bài, tác giả nói con mèo hoang 来钱小奇家拜访, đến nhà Tiền Tiểu Kỳ thăm hỏi, như thể nó là một vị khách lịch sự. Đây là cách nói nhân hóa rất dí dỏm."),
    ("见多识广", "jiàn duō shí guǎng", "kiến đa thức quảng", "thành ngữ", "thấy nhiều biết rộng", "爷爷年轻时去过很多地方，见多识广。", "Ông nội hồi trẻ đã đi nhiều nơi, thấy nhiều biết rộng.",
     "Thành ngữ, nghĩa là thấy nhiều, biết rộng, từng trải. Trong bài, chú mèo Đại Hoàng từng đi lang thang, nên được gọi đùa là 见多识广."),
    ("教养", "jiàoyǎng", "giáo dưỡng", "danh từ", "sự giáo dục, phép lịch sự", "这孩子很有教养，见了人总是主动问好。", "Đứa trẻ này rất có giáo dục, gặp ai cũng chủ động chào hỏi.",
     "Danh từ, chỉ văn hóa ứng xử, phép lịch sự được dạy dỗ từ nhỏ. 很有教养 là rất có giáo dục, 没有教养 là vô giáo dục. Chú ý: tiếng Việt nói trường giáo dưỡng là nơi cải tạo trẻ hư, nghĩa đó không có trong tiếng Trung. Chữ đầu đọc thanh bốn."),
    ("懒惰", "lǎnduò", "lãn đọa", "tính từ", "lười biếng", "懒惰的人很难成功。", "Người lười biếng rất khó thành công.",
     "Tính từ, nghĩa là lười biếng, mang màu sắc văn viết. Khẩu ngữ thường chỉ nói 懒. Trái nghĩa là 勤快 hoặc 勤劳, chăm chỉ."),
    ("馋", "chán", "sàm", "tính từ", "thèm ăn, tham ăn", "我嘴馋，看见好吃的就忍不住。", "Tôi hay thèm ăn, thấy món ngon là không nhịn được.",
     "Tính từ, nghĩa là thèm ăn, tham ăn. Hay gặp cụm 嘴馋, miệng thèm, tức là ham ăn. Trong bài, Đại Hoàng 不嘴馋, không tham ăn."),
    ("趴", "pā", "bát", "động từ", "nằm sấp; bò, gục xuống", "小狗趴在地上晒太阳。", "Chú chó con nằm bò trên đất phơi nắng.",
     "Động từ, nghĩa là nằm sấp, nằm bò; hoặc gục người lên một vật. Trong bài, 趴在窗台上晒太阳 là nằm bò trên bậu cửa sổ phơi nắng. Trong bài tập bốn, 把脸趴在他的肩上 là gục mặt lên vai anh ấy."),
    ("知足常乐", "zhīzú cháng lè", "tri túc thường lạc", "thành ngữ", "biết đủ thì luôn vui vẻ", "奶奶常说，知足常乐，不要和别人比。", "Bà thường nói, biết đủ thì luôn vui, đừng so bì với người khác.",
     "Thành ngữ, nghĩa là biết thế nào là đủ thì sẽ luôn vui vẻ, tiếng Việt có câu biết đủ là đủ. Trong bài, 一副知足常乐的样子 là một bộ dạng mãn nguyện, vui vẻ."),
    ("恭敬", "gōngjìng", "cung kính", "tính từ", "kính cẩn, cung kính", "学生们恭恭敬敬地向老师鞠了一躬。", "Các học sinh kính cẩn cúi chào thầy giáo.",
     "Tính từ, nghĩa là kính cẩn, lễ phép, âm Hán Việt giống hệt tiếng Việt. Dạng lặp lại là 恭恭敬敬, nhấn mạnh mức độ, như trong bài: 恭恭敬敬地在门口迎接."),
    ("君子", "jūnzǐ", "quân tử", "danh từ", "người quân tử", "君子说话要算数。", "Người quân tử đã nói là phải giữ lời.",
     "Danh từ, chỉ người có phẩm hạnh cao thượng, giống tiếng Việt. Trong bài, 不失君子风度 là không mất phong thái của người quân tử, ý khen con mèo rất đàng hoàng, lịch thiệp."),
    ("嗅觉", "xiùjué", "khứu giác", "danh từ", "khứu giác", "狗的嗅觉比人灵敏得多。", "Khứu giác của chó nhạy hơn người rất nhiều.",
     "Danh từ, nghĩa là khứu giác, khả năng ngửi mùi. Âm đầu đọc là xiù, thanh bốn. Chữ thứ hai ở đây đọc là jué, thanh hai, giống trong từ 感觉, 视觉."),
    ("灵敏", "língmǐn", "linh mẫn", "tính từ", "nhạy bén, nhanh nhạy", "这台仪器非常灵敏。", "Chiếc máy đo này cực kỳ nhạy.",
     "Tính từ, nghĩa là nhạy, phản ứng nhanh với những thay đổi rất nhỏ. Hay đi với 嗅觉, 反应, 仪器. Trong bài, 嗅觉灵敏 là mũi rất thính."),
    ("敏捷", "mǐnjié", "mẫn tiệp", "tính từ", "nhanh nhẹn", "他虽然七十岁了，动作还很敏捷。", "Ông ấy tuy đã bảy mươi tuổi, động tác vẫn rất nhanh nhẹn.",
     "Tính từ, nghĩa là nhanh nhẹn, lanh lẹ. Hay đi với 动作 và 思维: 动作敏捷, 思维敏捷. Các bạn chú ý phân biệt: 灵敏 là nhạy, còn 敏捷 là nhanh."),
    ("快活", "kuàihuo", "khoái hoạt", "tính từ", "vui vẻ", "孩子们在草地上快活地跑来跑去。", "Bọn trẻ vui vẻ chạy tới chạy lui trên bãi cỏ.",
     "Tính từ, nghĩa là vui vẻ, sung sướng, mang màu sắc khẩu ngữ. Âm tiết thứ hai đọc nhẹ. Trong bài, 快活而好动 là vui vẻ và hiếu động."),
    ("扑", "pū", "phác", "động từ", "bổ nhào, lao vào", "孩子一进门就扑到妈妈怀里。", "Đứa bé vừa vào cửa đã nhào vào lòng mẹ.",
     "Động từ, nghĩa là lao mạnh người về phía trước, bổ nhào tới. Trong bài, 它就扑上来 là nó liền nhào tới. Mèo bắt chuột cũng dùng từ này: 猫扑老鼠."),
    ("亲热", "qīnrè", "thân nhiệt", "tính từ", "thân mật, thắm thiết", "两个老朋友见面后亲热地聊了起来。", "Hai người bạn cũ gặp nhau liền trò chuyện thân mật.",
     "Tính từ, nghĩa là thân mật, tình cảm, quấn quýt. Cẩn thận: tiếng Việt thân nhiệt là nhiệt độ cơ thể, hoàn toàn khác nghĩa. Trong bài, 亲热地撞主人的腿 là cọ vào chân chủ một cách quấn quýt."),
    ("统统", "tǒngtǒng", "thống thống", "phó từ", "toàn bộ, tất cả", "他把旧衣服统统送人了。", "Anh ấy đem toàn bộ quần áo cũ cho người khác.",
     "Phó từ, nghĩa là tất cả, toàn bộ, không trừ cái nào. Đây là điểm ngữ pháp thứ nhất của bài."),
    ("迷人", "mírén", "mê nhân", "tính từ", "đẹp, có sức quyến rũ", "夜晚的西湖美丽迷人。", "Tây Hồ về đêm đẹp đến mê hồn.",
     "Tính từ, nghĩa là quyến rũ, làm người ta say mê. Trong bài, cô mèo Hỷ Nhi 把自己梳理得漂亮而迷人, chải chuốt cho mình xinh đẹp và quyến rũ."),
    ("模范", "mófàn", "mô phạm", "tính từ", "mẫu mực, gương mẫu", "他是我们学校的模范老师。", "Thầy ấy là giáo viên gương mẫu của trường chúng tôi.",
     "Vừa là tính từ vừa là danh từ, nghĩa là gương mẫu, người kiểu mẫu. Cẩn thận: tiếng Việt mô phạm thường nói về phong cách nghiêm trang của nhà giáo; còn 模范 là tấm gương tốt cho mọi người noi theo, như 劳动模范, chiến sĩ thi đua. Chữ đầu đọc là mó, thanh hai."),
    ("饲养", "sìyǎng", "tự dưỡng", "động từ", "chăn nuôi", "这个农场饲养了很多奶牛。", "Nông trại này nuôi rất nhiều bò sữa.",
     "Động từ, nghĩa là chăn nuôi động vật. 饲养员 là người chăm sóc động vật, như ở sở thú. Trong bài, tác giả gọi đùa anh chủ là 模范饲养员, người nuôi mèo gương mẫu."),
    ("清洁", "qīngjié", "thanh khiết", "động từ", "lau chùi, quét dọn", "每天早上，她都要清洁一遍房间。", "Sáng nào cô ấy cũng dọn dẹp phòng một lượt.",
     "Vừa là động từ, nghĩa là lau chùi, dọn sạch; vừa là tính từ, nghĩa là sạch sẽ. Cẩn thận: tiếng Việt thanh khiết là trong trẻo, tinh khiết; còn 清洁 chủ yếu là sạch sẽ, dọn dẹp. 清洁工 là công nhân vệ sinh."),
    ("喂", "wèi", "úy", "động từ", "cho ăn, bón", "妈妈正在给孩子喂饭。", "Mẹ đang bón cơm cho con.",
     "Động từ, nghĩa là cho ăn, bón cho ăn. Trong bài, 喂水，喂饭 là cho uống nước, cho ăn. Các bạn đã biết chữ này là thán từ gọi điện thoại, alo; ở đây nó là động từ, cũng đọc thanh bốn."),
    ("繁忙", "fánmáng", "phồn mang", "tính từ", "bận rộn", "他每天工作繁忙，很少休息。", "Ngày nào anh ấy cũng bận rộn công việc, rất ít khi nghỉ ngơi.",
     "Tính từ, nghĩa là bận rộn, nhiều việc, sắc thái văn viết hơn 忙. Hay gặp: 工作繁忙, 交通繁忙."),
    ("急切", "jíqiè", "cấp thiết", "tính từ", "háo hức, thiết tha, nôn nóng", "他急切地想知道考试结果。", "Anh ấy nôn nóng muốn biết kết quả thi.",
     "Tính từ, chỉ tâm trạng mong mỏi rất gấp gáp, nôn nóng. Cẩn thận: tiếng Việt cấp thiết là việc cần làm ngay; còn 急切 nói về tâm trạng của con người. Chữ thứ hai đọc là qiè, thanh bốn. Lát nữa chúng ta sẽ so sánh nó với 急忙."),
    ("例外", "lìwài", "lệ ngoại", "danh từ", "ngoại lệ", "所有人都要参加，谁也不能例外。", "Tất cả mọi người đều phải tham gia, không ai được ngoại lệ.",
     "Danh từ và động từ, nghĩa là ngoại lệ, nằm ngoài quy định chung. Lưu ý trật tự chữ ngược với tiếng Việt: tiếng Việt nói ngoại lệ, tiếng Trung nói 例外. Trong bài, 毫无例外 là không hề có ngoại lệ."),
    ("凝视", "níngshì", "ngưng thị", "động từ", "nhìn chăm chú, nhìn chằm chằm", "她站在窗前，静静地凝视着远方。", "Cô ấy đứng trước cửa sổ, lặng lẽ nhìn chăm chú về phía xa.",
     "Động từ, nghĩa là nhìn chăm chú, nhìn không chớp mắt. 凝 là đọng lại, 视 là nhìn; ánh mắt như đọng lại một chỗ. Trong bài, Hỷ Nhi 用凝视表达着它深沉的热情, dùng ánh nhìn chăm chú để bày tỏ sự nhiệt tình sâu lắng."),
    ("深沉", "shēnchén", "thâm trầm", "tính từ", "sâu lắng, sâu kín", "父亲的爱是深沉的。", "Tình yêu của cha là thứ tình cảm sâu lắng.",
     "Tính từ, nghĩa là sâu lắng, kín đáo, không lộ ra ngoài. Âm Hán Việt là thâm trầm, nghĩa khá gần tiếng Việt."),
    ("监视", "jiānshì", "giám thị", "động từ", "theo dõi, giám sát", "警察一直在监视那个人的行动。", "Cảnh sát luôn theo dõi hành động của người đó.",
     "Động từ, nghĩa là theo dõi, giám sát từ bên cạnh hoặc từ xa. Cẩn thận: tiếng Việt giám thị thường là người coi thi; còn 监视 là động từ theo dõi. Trong bài, 监视猫的一举一动 là theo dõi nhất cử nhất động của lũ mèo."),
    ("举动", "jǔdòng", "cử động", "danh từ", "động tác, hành động", "他的这个举动让大家很感动。", "Hành động này của anh ấy khiến mọi người rất cảm động.",
     "Danh từ, nghĩa là hành động, việc làm của một người. Cẩn thận: tiếng Việt cử động là động đậy chân tay; còn 举动 là hành vi, cử chỉ. Thành ngữ 一举一动 là nhất cử nhất động."),
    ("缺陷", "quēxiàn", "khuyết hãm", "danh từ", "chỗ thiếu sót, nhược điểm", "这种产品有设计缺陷。", "Loại sản phẩm này có lỗi thiết kế.",
     "Danh từ, nghĩa là khiếm khuyết, chỗ chưa hoàn thiện. Hay gặp: 设计缺陷, lỗi thiết kế; 生理缺陷, khiếm khuyết cơ thể. Trong bài, camera không di chuyển được nên 有缺陷."),
    ("镜头", "jìngtóu", "kính đầu", "danh từ", "ống kính; cảnh quay; pô ảnh", "这部电影有很多感人的镜头。", "Bộ phim này có rất nhiều cảnh quay cảm động.",
     "Danh từ, có ba nghĩa: ống kính máy ảnh; một cảnh quay trong phim; và một bức ảnh chụp. Trong bài, 拍下的很多镜头都是空的 là nhiều cảnh quay được đều trống trơn, không có con mèo nào."),
    ("自力更生", "zìlì-gēngshēng", "tự lực cánh sinh", "thành ngữ", "tự lực cánh sinh", "我们要自力更生，不能总靠别人。", "Chúng ta phải tự lực cánh sinh, không thể cứ dựa vào người khác.",
     "Thành ngữ, giống hệt tiếng Việt tự lực cánh sinh, nghĩa là tự dựa vào sức mình. Chú ý cách đọc: chữ thứ ba đọc là gēng, thanh một."),
    ("尖端", "jiānduān", "tiêm đoan", "tính từ", "tiên tiến nhất, tối tân", "这家公司掌握着尖端技术。", "Công ty này nắm trong tay công nghệ tối tân.",
     "Tính từ, nghĩa là tiên tiến nhất, mũi nhọn. 尖 là nhọn, 端 là đầu mút; đầu mũi nhọn tức là đứng đầu. Trong bài, 一套尖端玩意儿 là một bộ đồ chơi công nghệ tối tân, nói hơi đùa."),
    ("钻研", "zuānyán", "toản nghiên", "động từ", "nghiên cứu kỹ lưỡng", "他刻苦钻研业务，水平提高得很快。", "Anh ấy chăm chỉ nghiên cứu chuyên môn, trình độ tiến bộ rất nhanh.",
     "Động từ, nghĩa là đào sâu nghiên cứu, như khoan sâu vào vấn đề. Chữ đầu ở đây đọc là zuān, thanh một. Trong bài, 边钻研边安装 là vừa mày mò nghiên cứu vừa lắp đặt."),
    ("动态", "dòngtài", "động thái", "danh từ", "tình hình hoạt động, diễn biến", "记者随时关注比赛的最新动态。", "Phóng viên luôn theo sát diễn biến mới nhất của trận đấu.",
     "Danh từ, chỉ cách hành động, tình hình biến đổi. Trong bài, 对猫的动态进行抓拍 là chụp lại các hoạt động của mèo. Trên mạng xã hội, 动态 còn là bài đăng, trạng thái mới."),
    ("储存", "chǔcún", "trữ tồn", "động từ", "lưu lại, dự trữ", "手机里储存了很多照片。", "Trong điện thoại lưu rất nhiều ảnh.",
     "Động từ, nghĩa là cất giữ, lưu trữ, dự trữ. Dùng cho cả đồ vật lẫn dữ liệu. Trong bài, 储存下图像 là lưu lại hình ảnh."),
    ("遥控", "yáokòng", "dao khống", "động từ", "điều khiển từ xa", "这辆玩具汽车可以遥控。", "Chiếc ô tô đồ chơi này có thể điều khiển từ xa.",
     "Động từ, nghĩa là điều khiển từ xa. 遥 là xa, 控 là khống chế. 遥控器 là cái điều khiển từ xa."),
    ("即时", "jíshí", "tức thời", "phó từ", "ngay lập tức", "新闻网站即时报道了这个消息。", "Trang tin tức đã đưa tin này ngay lập tức.",
     "Phó từ, nghĩa là ngay lập tức, tức thời. Trong bài, 即时监控 là giám sát trực tiếp theo thời gian thực. Từ này sách đánh dấu sao, tức là từ ngoài đề cương HSK."),
    ("操纵", "cāozòng", "thao túng", "động từ", "điều khiển, vận hành", "这台机器操纵起来很简单。", "Chiếc máy này vận hành rất đơn giản.",
     "Động từ, nghĩa là điều khiển máy móc. Cẩn thận: tiếng Việt thao túng thường mang nghĩa xấu, giật dây người khác. Tiếng Trung cũng có nghĩa đó, nhưng trong bài, 操纵摄像头 chỉ đơn giản là điều khiển camera."),
    ("跟踪", "gēnzōng", "cân tung", "động từ", "theo dõi, bám theo", "警察跟踪了那辆可疑的汽车。", "Cảnh sát đã bám theo chiếc xe khả nghi đó.",
     "Động từ, nghĩa là bám theo sát dấu vết. 跟 là đi theo, 踪 là dấu vết. Trong bài, 跟踪到家里的任何一个角落 là theo dõi tới mọi ngóc ngách trong nhà."),
    ("角落", "jiǎoluò", "giác lạc", "danh từ", "góc, xó xỉnh", "房间的角落里放着一盆花。", "Trong góc phòng có đặt một chậu hoa.",
     "Danh từ, nghĩa là góc, ngóc ngách. Chữ đầu đọc là jiǎo, thanh ba; chữ thứ hai đọc là luò, thanh bốn."),
    ("误差", "wùchā", "ngộ sai", "danh từ", "sai số, độ sai lệch", "这块手表一个月的误差不到一秒。", "Chiếc đồng hồ này mỗi tháng sai lệch không tới một giây.",
     "Danh từ, nghĩa là sai số. Chữ thứ hai ở đây đọc là chā, thanh một. Trong bài, 时间误差平均不到五分钟 là thời gian sai lệch trung bình không tới năm phút."),
    ("踪迹", "zōngjì", "tung tích", "danh từ", "tung tích, vết tích, dấu vết", "他找遍了整个公园，也没发现小狗的踪迹。", "Anh ấy tìm khắp công viên mà không thấy tung tích chú chó con.",
     "Danh từ, nghĩa là dấu vết, tung tích, giống tiếng Việt. Chữ 踪 cũng có trong từ 跟踪 mà các bạn vừa học."),
    ("动静", "dòngjing", "tiếng động", "danh từ", "tiếng động; động tĩnh", "夜里，院子里有一点儿动静，把我吓醒了。", "Đêm qua, trong sân có chút tiếng động làm tôi giật mình tỉnh giấc.",
     "Danh từ, nghĩa là tiếng động, hoặc tình hình biến động. Âm tiết thứ hai đọc nhẹ. Tiếng Việt động tĩnh cũng gần nghĩa này. Trong bài, 只要家里稍有动静 là chỉ cần trong nhà có chút động tĩnh."),
    ("操作", "cāozuò", "thao tác", "động từ", "thao tác, điều hành", "请按照说明书操作。", "Xin hãy thao tác theo sách hướng dẫn.",
     "Động từ, nghĩa là thao tác, vận hành theo quy trình. 操作系统 là hệ điều hành của máy tính. Các bạn so sánh: 操纵 nhấn mạnh việc điều khiển, còn 操作 nhấn mạnh làm theo các bước quy định."),
]

add("bullets", chapter="Từ mới (46 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 11 có 46 từ mới, chia thành 16 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 教养 (jiào) · 嗅觉 (jué) · 自力更生 (gēng) · 误差 (chā)",
           "Từ dễ nhầm: 亲热 · 模范 · 清洁 · 急切 · 监视 · 举动 · 操纵"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có bốn mươi sáu từ, thầy chia thành mười sáu nhóm nhỏ, mỗi nhóm hai hoặc ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số từ có âm đọc cần chú ý, như 教养，嗅觉，自力更生，误差. Thầy sẽ nhắc khi gặp."),
         F(4, "Ngoài ra, có mấy từ Hán Việt rất dễ hiểu nhầm, như 亲热，模范，清洁，急切，监视，举动，操纵. Nghĩa của chúng trong tiếng Trung khác với tiếng Việt, các bạn nhớ nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

sizes = [3] * 14 + [2, 2]
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
    ("钱小奇养了3只猫。大黄原本是只流浪猫，那天，淋着大雨来钱小奇家拜访，下完雨就不走了。",
     "Tiền Tiểu Kỳ nuôi ba con mèo. Đại Hoàng vốn là một con mèo hoang. Hôm ấy, nó đội mưa to đến nhà Tiền Tiểu Kỳ thăm hỏi, mưa tạnh rồi cũng chẳng chịu đi nữa.",
     ["大黄 là tên con mèo, nghĩa là Vàng To, chắc vì bộ lông màu vàng. 原本 là vốn dĩ, ban đầu. 是只流浪猫 là cách nói tắt của 是一只流浪猫.",
      "淋着大雨 là đội mưa to; 着 chỉ trạng thái đi kèm hành động 来. Tác giả dùng 拜访 cho một con mèo hoang, như thể nó là vị khách lịch sự đến chơi rồi ở lại luôn. Thật dí dỏm!"],
     "钱小奇养了三只猫。大黄原本是只流浪猫，那天，淋着大雨来钱小奇家拜访，下完雨就不走了。"),
    ("见多识广的大黄虽有流浪史，却很有教养，它既不懒惰，也不嘴馋，天天趴在窗台上晒太阳，一副知足常乐的样子。",
     "Đại Hoàng thấy nhiều biết rộng, tuy có quá khứ lang thang, nhưng lại rất có giáo dục. Nó vừa không lười biếng, vừa không tham ăn, ngày ngày nằm bò trên bậu cửa sổ phơi nắng, ra dáng một kẻ biết đủ và luôn vui vẻ.",
     ["虽……却…… là tuy… nhưng…, văn viết hơn 虽然……但是. 流浪史 là quá khứ lang thang, 史 là lịch sử.",
      "既不……也不…… là vừa không… cũng không…. 一副……的样子 là ra cái dáng vẻ…; 副 là lượng từ cho nét mặt, dáng vẻ."]),
    ("每次钱小奇出门回来，它都恭恭敬敬地在门口迎接，不失君子风度。",
     "Mỗi lần Tiền Tiểu Kỳ đi ra ngoài trở về, nó đều kính cẩn ra cửa đón, không mất phong thái người quân tử.",
     ["恭恭敬敬 là dạng lặp của 恭敬, theo kiểu AABB, nhấn mạnh mức độ, làm trạng ngữ cho động từ 迎接.",
      "不失 là không mất đi; 风度 là phong thái, phong độ. Ba câu đầu tả chú mèo Đại Hoàng: điềm đạm, lịch sự, như một quý ông."]),
    ("白白是个男孩儿，嗅觉灵敏，动作敏捷，快活而好动。钱小奇一回家，它就扑上来，亲热地撞主人的腿，还要把钱小奇和他带回来的东西统统闻一遍。",
     "Bạch Bạch là một cậu bé, mũi rất thính, động tác nhanh nhẹn, vui vẻ và hiếu động. Tiền Tiểu Kỳ vừa về đến nhà, nó liền nhào tới, quấn quýt cọ vào chân chủ, còn đem Tiền Tiểu Kỳ và đồ đạc anh mang về ngửi hết một lượt.",
     ["白白 là Trắng Trắng, tên con mèo thứ hai. 是个男孩儿 là một cậu bé, tức là mèo đực. 一……就…… là vừa… liền….",
      "把……统统闻一遍 là ngửi tất cả một lượt; 统统 nghĩa là toàn bộ, đây chính là điểm ngữ pháp thứ nhất. Các bạn so sánh: Đại Hoàng điềm tĩnh, còn Bạch Bạch hiếu động."]),
    ("喜儿是个人见人爱的女孩儿，每天大部分时间都在整理自己的毛发，把自己梳理得漂亮而迷人。",
     "Hỷ Nhi là một cô bé ai gặp cũng yêu, mỗi ngày phần lớn thời gian đều dành để chải chuốt bộ lông của mình, làm cho mình thật xinh đẹp và quyến rũ.",
     ["人见人爱 là ai gặp cũng yêu, cấu trúc 人 cộng động từ, 人 cộng động từ, như 人见人怕.",
      "把自己梳理得漂亮而迷人 là câu chữ 把 có bổ ngữ trạng thái: chải chuốt cho bản thân trở nên xinh đẹp. 而 nối hai tính từ: 漂亮而迷人, 快活而好动."]),
    ("钱小奇是个模范饲养员，每天早起第一件事就是伺候猫：清洁猫舍，喂水，喂饭。",
     "Tiền Tiểu Kỳ là một người nuôi mèo gương mẫu, mỗi sáng thức dậy việc đầu tiên là chăm sóc lũ mèo: dọn dẹp chuồng mèo, cho uống nước, cho ăn.",
     ["伺候 nghĩa là hầu hạ, chăm sóc; chữ đầu đọc là cì. 猫舍 là chỗ ở của mèo, 舍 là nhà, như trong 宿舍.",
      "Dấu hai chấm dùng để liệt kê những việc cụ thể của 伺候猫. Gọi người nuôi mèo là 模范饲养员 là cách nói hài hước."]),
    ("他虽然工作繁忙，但每天最急切盼望的就是回家开门的那一刻——大黄和白白在门口等候他，喜儿则毫无例外地站在远处，用凝视表达着它深沉的热情。",
     "Tuy công việc bận rộn, nhưng điều anh nôn nóng mong đợi nhất mỗi ngày chính là giây phút mở cửa về nhà: Đại Hoàng và Bạch Bạch chờ anh ở cửa, còn Hỷ Nhi thì không lần nào khác, luôn đứng ở đằng xa, dùng ánh nhìn chăm chú để bày tỏ sự nhiệt tình sâu lắng của nó.",
     ["急切盼望 là nôn nóng mong đợi; 急切 làm trạng ngữ. 那一刻 là khoảnh khắc ấy. Dấu gạch ngang dài dùng để giải thích khoảnh khắc ấy cụ thể ra sao.",
      "则 ở đây nghĩa là còn, thì, dùng để đối chiếu với vế trước, văn viết. 毫无例外 là không hề có ngoại lệ, tức là lần nào cũng vậy."]),
    ("钱小奇很好奇，自己不在家时猫在做什么？那么长时间，猫们多无聊，会不会忧郁得生病？",
     "Tiền Tiểu Kỳ rất tò mò, lúc mình không có nhà thì lũ mèo làm gì? Thời gian dài như thế, lũ mèo buồn chán biết bao, liệu có buồn bực đến phát bệnh không?",
     ["猫们 là cách nói nhân hóa, vì bình thường 们 chỉ dùng cho người. 多无聊 là buồn chán biết bao, 多 ở đây là phó từ cảm thán.",
      "忧郁得生病 là buồn rầu đến mức sinh bệnh, động từ cộng 得 cộng kết quả. Đây là câu hỏi chính của bài, cũng là tên bài khóa."]),
    ("为了弄清楚这事，他在家里安了个摄像头，监视猫的一举一动。",
     "Để làm rõ chuyện này, anh lắp một chiếc camera trong nhà, theo dõi nhất cử nhất động của lũ mèo.",
     ["弄清楚 là làm cho rõ ràng. 安 ở đây là lắp đặt, giống 安装. 摄像头 là camera, webcam.",
      "监视 là theo dõi, giám sát; 一举一动 là nhất cử nhất động, mọi hành động dù nhỏ nhất."]),
    ("很快，他发现这个不能移动的摄像头有缺陷，拍下的很多镜头都是空的，于是，他增加了设备，并决定自力更生安装一套尖端玩意儿。",
     "Rất nhanh, anh phát hiện chiếc camera không di chuyển được này có nhược điểm, nhiều cảnh quay được đều trống trơn. Thế là anh bổ sung thêm thiết bị, và quyết định tự lực cánh sinh lắp đặt một bộ đồ chơi công nghệ tối tân.",
     ["镜头都是空的 là các cảnh quay đều trống, không có mèo, vì mèo đã đi ra ngoài vùng camera quay được.",
      "玩意儿 là đồ chơi, thứ đồ, khẩu ngữ. Ghép văn viết 尖端 với khẩu ngữ 玩意儿 tạo hiệu quả hài hước. 并 ở đây là liên từ, nghĩa là và, đồng thời."]),
    ("他边钻研边安装，经过三个多月的努力，安装好的设备不仅能够对猫的动态进行抓拍并储存下图像，钱小奇在外面时还能通过互联网遥控摄像头，对家里的猫进行即时监控，同时能通过操纵、移动摄像头，跟踪到家里的任何一个角落。",
     "Anh vừa mày mò vừa lắp đặt, sau hơn ba tháng nỗ lực, bộ thiết bị lắp xong không những có thể chụp nhanh và lưu lại hình ảnh hoạt động của mèo, mà khi ở bên ngoài, anh còn có thể điều khiển camera từ xa qua Internet để giám sát lũ mèo theo thời gian thực, đồng thời điều khiển, di chuyển camera để theo dõi tới mọi ngóc ngách trong nhà.",
     ["边……边…… là vừa… vừa…. 三个多月 là hơn ba tháng; 多 đứng sau lượng từ 个 chỉ số lẻ.",
      "对……进行…… là tiến hành… đối với…, cấu trúc văn viết: 对猫的动态进行抓拍, 对家里的猫进行即时监控. 抓拍 là chụp nhanh khoảnh khắc. 不仅……还…… là không những… mà còn…."]),
    ("通过对大量数据和图片进行分析，钱小奇发现，这三只猫大多数时间都在睡觉。",
     "Thông qua phân tích một lượng lớn dữ liệu và hình ảnh, Tiền Tiểu Kỳ phát hiện ba con mèo này phần lớn thời gian đều đang ngủ.",
     ["通过对……进行分析 là thông qua việc phân tích…, lại là cấu trúc 对……进行…….",
      "Đây là phát hiện đầu tiên, khá buồn cười: anh lo mèo buồn chán, nhưng thật ra chúng chỉ ngủ."]),
    ("除了睡觉，猫们的行动很有规律，以其中一只猫为例，它每天下午两点左右吃饭喝水，时间误差平均不到5分钟。",
     "Ngoài ngủ ra, hoạt động của lũ mèo rất có quy luật. Lấy một con trong số đó làm ví dụ, mỗi ngày nó ăn uống vào khoảng hai giờ chiều, thời gian sai lệch trung bình không tới năm phút.",
     ["以其中一只猫为例 là lấy một con mèo trong số đó làm ví dụ. Đây là cấu trúc văn viết 以……为……, điểm ngữ pháp thứ hai của bài.",
      "左右 là khoảng, đặt sau con số. 误差 là sai số; 平均 là trung bình. 不到 là chưa tới."],
     "除了睡觉，猫们的行动很有规律，以其中一只猫为例，它每天下午两点左右吃饭喝水，时间误差平均不到五分钟。"),
    ("更有趣的是，每次回家时，守在门口的大黄和白白也不是长时间在门口等他，而是在屋里该干吗干吗，听到主人的脚步声和钥匙响后，才会跑到门口来迎接。",
     "Thú vị hơn nữa là, mỗi lần anh về nhà, Đại Hoàng và Bạch Bạch canh ở cửa cũng không phải chờ anh ở cửa thật lâu, mà ở trong nhà, việc gì cần làm thì cứ làm, nghe thấy tiếng bước chân và tiếng chìa khóa của chủ, chúng mới chạy ra cửa đón.",
     ["不是……而是…… là không phải… mà là…. 该干吗干吗 nghĩa là việc gì cần làm thì cứ làm, mọi thứ vẫn như bình thường; đây là điểm ngữ pháp thứ ba.",
      "钥匙响 là tiếng chìa khóa kêu. 才 nhấn mạnh: đến lúc đó chúng mới ra đón. Hóa ra sự đón chờ cảm động kia là nhờ đôi tai thính chứ không phải chờ cả ngày!"]),
    ("这套系统除了帮钱小奇了解了猫的踪迹以外，还帮过钱小奇不少忙。一次，他在办公室上网遥控摄像头，找到了掉在家里桌子下的钱包。",
     "Hệ thống này ngoài việc giúp Tiền Tiểu Kỳ biết được tung tích của lũ mèo, còn giúp anh không ít việc. Có lần, anh ở văn phòng lên mạng điều khiển camera từ xa, tìm được chiếc ví rơi dưới gầm bàn ở nhà.",
     ["除了……以外，还…… là ngoài… ra, còn…. 套 là lượng từ cho một bộ, một hệ thống: 一套系统, 一套设备.",
      "帮忙 là từ ly hợp, nên tách ra thành 帮过不少忙, đã giúp không ít việc. 掉在 là rơi xuống ở chỗ nào đó."]),
    ("如今，只要家里稍有动静，操作系统就能将图像记录下来，并把拍下的照片即时发到他的邮箱里“报警”。这是一套多么有用的远程遥控家庭安全机器人啊。",
     "Ngày nay, chỉ cần trong nhà có chút động tĩnh, hệ thống điều khiển sẽ ghi lại hình ảnh, và gửi ngay ảnh chụp được vào hộp thư của anh để báo động. Đây quả là một chú robot an ninh gia đình điều khiển từ xa hữu ích biết bao.",
     ["只要……就…… là chỉ cần… thì…. 稍有 là hơi có, có một chút. 将 ở đây giống 把, mang màu sắc văn viết: 将图像记录下来.",
      "报警 là báo cảnh sát, báo động; dấu ngoặc kép vì đây là nói ví von. Câu cảm thán 多么……啊 khép lại bài, khen hệ thống này rất hữu ích."],
     "如今，只要家里稍有动静，操作系统就能将图像记录下来，并把拍下的照片即时发到他的邮箱里报警。这是一套多么有用的远程遥控家庭安全机器人啊。"),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 我不在时，猫在干什么", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 我不在时，猫在干什么, dài tám trăm bốn mươi lăm chữ. Bài được cải biên từ bài báo của tác giả Lý Hoàn Vũ, đăng trên Bắc Kinh Vãn báo.",
         F(0, "Thầy chia bài thành mười sáu đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 100 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Tóm tắt nội dung", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5) – phần 1", size=34,
    items=["## 1. 描述一下钱小奇家的三只猫。",
           "大黄：原本是流浪猫，见多识广，很有教养，天天趴在窗台上晒太阳",
           "白白：嗅觉灵敏，动作敏捷，快活而好动 · 喜儿：人见人爱，整天梳理毛发",
           "## 2. 钱小奇跟三只猫的感情怎么样？",
           "钱小奇是模范饲养员，每天伺候猫，最急切盼望回家开门的那一刻",
           "大黄和白白在门口迎接他 · 喜儿站在远处用凝视表达热情"],
    say=["Bài tập năm của sách yêu cầu dựa vào gợi ý để tóm tắt nội dung chính của bài khóa. Chúng ta cùng làm luôn nhé.",
         F(0, "Câu hỏi một: hãy miêu tả ba con mèo nhà Tiền Tiểu Kỳ."),
         F(1, "大黄原本是流浪猫，见多识广，很有教养，天天趴在窗台上晒太阳。 Đại Hoàng vốn là mèo hoang, thấy nhiều biết rộng, rất có giáo dục, ngày ngày nằm phơi nắng trên bậu cửa sổ."),
         F(2, "白白嗅觉灵敏，动作敏捷，快活而好动。 Bạch Bạch mũi thính, nhanh nhẹn, vui vẻ hiếu động. 喜儿人见人爱，整天梳理毛发。 Hỷ Nhi ai gặp cũng yêu, suốt ngày chải chuốt bộ lông."),
         F(3, "Câu hỏi hai: tình cảm giữa Tiền Tiểu Kỳ và ba con mèo thế nào?"),
         F(4, "Về phía chủ: anh là một người nuôi mèo gương mẫu, ngày nào cũng chăm sóc chúng, và điều anh nôn nóng mong đợi nhất là giây phút mở cửa về nhà."),
         F(5, "Về phía mèo: Đại Hoàng và Bạch Bạch ra cửa đón anh, còn Hỷ Nhi đứng ở xa, dùng ánh nhìn chăm chú để bày tỏ tình cảm.")])

add("bullets", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5) – phần 2", size=34,
    items=["## 3. 为了弄清楚猫在做什么，钱小奇采取了什么措施？",
           "安摄像头，监视猫的一举一动 → 增加设备：抓拍、储存、遥控、即时监控、跟踪",
           "## 4. 主人不在时，猫到底在干吗？",
           "大多数时间都在睡觉 · 行动很有规律 · 听到脚步声和钥匙响才跑到门口",
           "## 5. 这套系统还帮过钱小奇什么忙？",
           "找到了掉在桌子下的钱包 · 家里稍有动静，就即时发照片“报警”"],
    say=[F(0, "Câu hỏi ba: để biết lũ mèo làm gì, Tiền Tiểu Kỳ đã áp dụng biện pháp gì?"),
         F(1, "Đầu tiên anh 安摄像头, lắp một chiếc camera để theo dõi nhất cử nhất động của mèo. Sau đó anh 增加设备, bổ sung thiết bị, tự lắp một hệ thống có thể chụp nhanh, lưu trữ, điều khiển từ xa, giám sát tức thời và theo dõi khắp nhà."),
         F(2, "Câu hỏi bốn: lúc chủ vắng nhà, rốt cuộc lũ mèo làm gì?"),
         F(3, "Phần lớn thời gian chúng ngủ. Hoạt động rất có quy luật, chẳng hạn ăn uống vào khoảng hai giờ chiều. Và chúng không chờ ở cửa cả ngày, mà nghe thấy tiếng bước chân và tiếng chìa khóa mới chạy ra đón."),
         F(4, "Câu hỏi năm: hệ thống này còn giúp Tiền Tiểu Kỳ việc gì?"),
         F(5, "Nó giúp anh tìm thấy chiếc ví rơi dưới gầm bàn. Và chỉ cần trong nhà có chút động tĩnh, nó sẽ gửi ảnh ngay vào hộp thư của anh để báo động. Bố cục này rất có ích khi các bạn tự kể lại bài khóa.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 统统", section="Ngữ pháp 注释", title="1. 统统 tǒngtǒng – tất cả, toàn bộ", size=36,
    items=["Phó từ: hành động liên quan đến toàn bộ đối tượng, nghĩa là 毫无例外地、一个不剩地",
           "Thường dùng trong khẩu ngữ · cũng nói 通通 · đứng trước động từ, đối tượng đặt phía trước",
           "我把随身携带着的DV小摄像机、录音机以及照相机统统从包里取了出来。",
           "钱小奇一回家，它就扑上来，亲热地撞主人的腿，还要把钱小奇和他带回来的东西统统闻一遍。",
           "他不抽烟、不喝酒、不喝茶、不喝咖啡、不讲究饮食，什么电影院、酒吧，统统与他无缘。"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là phó từ 统统.",
         F(0, "统统 là phó từ, biểu thị hành động liên quan đến toàn bộ đối tượng, nghĩa là 毫无例外地，一个不剩地, tức là không có ngoại lệ, không sót một cái nào. Tiếng Việt dịch là tất cả, toàn bộ, hết thảy."),
         F(1, "统统 thường dùng trong khẩu ngữ, cũng có thể nói 通通. Nó đứng trước động từ, còn các đối tượng được nói đến thường đặt ở phía trước, hoặc đưa lên bằng chữ 把."),
         F(2, "Ví dụ một: 我把随身携带着的小摄像机、录音机以及照相机统统从包里取了出来。 Tôi lấy hết máy quay nhỏ, máy ghi âm và máy ảnh mang theo người ra khỏi túi."),
         F(3, "Ví dụ hai, lấy từ bài khóa: 还要把钱小奇和他带回来的东西统统闻一遍。 Còn đem Tiền Tiểu Kỳ và đồ đạc anh mang về ngửi hết một lượt."),
         F(4, "Ví dụ ba: 他不抽烟、不喝酒、不喝茶、不喝咖啡、不讲究饮食，什么电影院、酒吧，统统与他无缘。 Anh ấy không hút thuốc, không uống rượu, không uống trà, không uống cà phê, không cầu kỳ chuyện ăn uống; nào là rạp chiếu phim, quán bar, tất cả đều chẳng dính dáng gì đến anh ấy.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: dùng 统统 viết lại câu", reveal=True, size=36,
    items=["(1) 这回我也想把放假的时间全部用来打工。",
           "Đáp án: 这回我也想把放假的时间统统用来打工。",
           "(2) 今天的节目没意思，节目还没演完，剧场里的人就都走光了。",
           "Đáp án: ……节目还没演完，剧场里的人就统统走光了。",
           "(3) 二十年后再回到北京，我几乎认不出它了，到处都是高楼，我熟悉的胡同里的老房子全都被拆掉了。",
           "Đáp án: ……我熟悉的胡同里的老房子统统被拆掉了。"],
    say=[F(0, "Luyện tập: dùng 统统 viết lại câu. Câu một: 这回我也想把放假的时间全部用来打工。 Lần này tôi cũng muốn dùng toàn bộ thời gian nghỉ để đi làm thêm. Các bạn tạm dừng và thử viết lại nhé."),
         F(1, "Đáp án: 这回我也想把放假的时间统统用来打工。 Thay 全部 bằng 统统, đặt trước động từ 用来."),
         F(2, "Câu hai: 今天的节目没意思，节目还没演完，剧场里的人就都走光了。 Chương trình hôm nay chán quá, chương trình chưa diễn xong, người trong rạp đã về hết rồi."),
         F(3, "Đáp án: 节目还没演完，剧场里的人就统统走光了。 Thay 都 bằng 统统."),
         F(4, "Câu ba: 二十年后再回到北京，我几乎认不出它了，到处都是高楼，我熟悉的胡同里的老房子全都被拆掉了。 Hai mươi năm sau trở lại Bắc Kinh, tôi gần như không nhận ra nó nữa, khắp nơi đều là nhà cao tầng, những ngôi nhà cũ trong ngõ nhỏ quen thuộc của tôi đều bị dỡ bỏ hết."),
         F(5, "Đáp án: 我熟悉的胡同里的老房子统统被拆掉了。 Chú ý: 统统 đứng trước 被, tức là đứng trước cả cụm động từ bị động.")])

add("bullets", chapter="Ngữ pháp: 以……为……", section="Ngữ pháp 注释", title="2. 以……为…… yǐ…wéi… – lấy… làm…", size=36,
    items=["Cách nói văn viết, tương đương khẩu ngữ 把/拿……作为/当作……",
           "Hai cụm 以……为…… dùng liền nhau: 以 thứ hai có thể lược bỏ",
           "猫们的行动很有规律，以其中一只猫为例，它每天下午两点左右吃饭喝水，时间误差平均不到5分钟。",
           "普通话以北京语音为标准音，以北方方言为基础方言，以典范的现代白话文著作作为语法规范。",
           "今天的晚会大伙准备了不少节目，当然以学生为主，老师为辅。",
           "Hay gặp: 以……为例 · 以……为主 · 以……为荣 · 以……为中心"],
    say=["Điểm ngữ pháp thứ hai là cấu trúc văn viết 以其中一只猫为例 mà chúng ta gặp trong bài khóa, gọi tắt là cấu trúc lấy cái này làm cái kia.",
         F(0, "Đây là cách nói văn viết, nghĩa là lấy cái gì làm cái gì, coi cái gì là cái gì. Trong khẩu ngữ, ta nói 把某物作为某物, hoặc 拿某物当作某物. Chữ thứ hai trong cấu trúc này đọc là wéi, thanh hai, giống trong từ 作为."),
         F(1, "Khi hai cụm như vậy dùng liền nhau, chữ 以 ở cụm thứ hai có thể lược bỏ."),
         F(2, "Ví dụ một, lấy từ bài khóa: 猫们的行动很有规律，以其中一只猫为例，它每天下午两点左右吃饭喝水，时间误差平均不到五分钟。 Lấy một con mèo trong số đó làm ví dụ."),
         F(3, "Ví dụ hai: 普通话以北京语音为标准音，以北方方言为基础方言，以典范的现代白话文著作作为语法规范。 Tiếng phổ thông lấy ngữ âm Bắc Kinh làm âm chuẩn, lấy phương ngữ phương Bắc làm phương ngữ cơ sở, lấy các tác phẩm văn bạch thoại hiện đại tiêu biểu làm chuẩn mực ngữ pháp."),
         F(4, "Ví dụ ba: 今天的晚会大伙准备了不少节目，当然以学生为主，老师为辅。 Buổi tiệc tối nay mọi người chuẩn bị khá nhiều tiết mục, tất nhiên học sinh là chính, thầy cô là phụ. Các bạn thấy đấy, ở cụm thứ hai, chữ 以 đã được lược bỏ."),
         F(5, "Một số cụm rất hay gặp: 以此为例, lấy đây làm ví dụ; 以学生为主, lấy học sinh làm chính; 以你为荣, lấy bạn làm niềm tự hào; và 以人为本, lấy con người làm gốc.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: dùng 以……为…… viết lại câu", reveal=True, size=36,
    items=["(1) 考试不要把学生当作敌人，把难倒学生作为目的。",
           "Đáp án: 考试不要以学生为敌人，以难倒学生为目的。",
           "(2) 这部短篇小说集里描写农村生活的作品最多。",
           "Đáp án: 这部短篇小说集以描写农村生活的作品为主。",
           "(3) 教育学是一门科学，它的研究对象是教育。",
           "Đáp án: 教育学是一门以教育为研究对象的科学。"],
    say=[F(0, "Luyện tập: dùng cấu trúc vừa học để viết lại câu. Câu một: 考试不要把学生当作敌人，把难倒学生作为目的。 Thi cử đừng coi học sinh là kẻ thù, đừng lấy việc làm khó học sinh làm mục đích. Các bạn tạm dừng và thử viết lại nhé."),
         F(1, "Đáp án: 考试不要以学生为敌人，以难倒学生为目的。 Khẩu ngữ 把某物当作某物 được đổi thành văn viết 以某物为某物."),
         F(2, "Câu hai: 这部短篇小说集里描写农村生活的作品最多。 Trong tập truyện ngắn này, tác phẩm miêu tả cuộc sống nông thôn là nhiều nhất."),
         F(3, "Đáp án: 这部短篇小说集以描写农村生活的作品为主。 Tập truyện ngắn này lấy các tác phẩm về nông thôn làm chủ yếu. Cũng có thể nói 以描写农村生活的作品为最多."),
         F(4, "Câu ba: 教育学是一门科学，它的研究对象是教育。 Giáo dục học là một môn khoa học, đối tượng nghiên cứu của nó là giáo dục."),
         F(5, "Đáp án: 教育学是一门以教育为研究对象的科学。 Giáo dục học là môn khoa học lấy giáo dục làm đối tượng nghiên cứu. Ở đây cả cụm 以教育为研究对象 làm định ngữ cho 科学.")])

add("bullets", chapter="Ngữ pháp: 该干吗干吗", section="Ngữ pháp 注释", title="3. 该干吗干吗 gāi gàn má gàn má – việc gì cứ làm nấy", size=34,
    items=["Rút gọn từ: 该 + động từ + tân ngữ + 还/就得 + động từ + tân ngữ (该学汉语还得学汉语)",
           "Nghĩa: mọi việc vẫn diễn ra như cũ, không gì thay đổi được · 还/就得 thường lược bỏ",
           "Biến thể: 该吃吃，该玩儿玩儿 · 该打球打球 · 该什么结果还是什么结果",
           "在中国，过年过节商店最忙了，哪儿有假呀，该开门就得开门。",
           "每次回家时，守在门口的大黄和白白也不是长时间在门口等他，而是在屋里该干吗干吗。",
           "哭、着急都不管用，该什么结果还是什么结果。"],
    say=["Điểm ngữ pháp thứ ba là cách nói khẩu ngữ 该干吗干吗.",
         F(0, "Cách nói này được rút gọn từ một mẫu dài hơn: chữ 该, cộng động từ và tân ngữ, rồi lặp lại động từ và tân ngữ đó. Ví dụ đầy đủ là 该学汉语还得学汉语, việc phải học tiếng Trung thì vẫn phải học tiếng Trung."),
         F(1, "Ý nghĩa: mọi việc vẫn diễn ra như vốn có, không có chuyện gì thay đổi được. Hai cụm động từ trước và sau là một. Phần ở giữa, tức 还得 hoặc 就得, thường được lược bỏ. Tiếng Việt có thể dịch là việc gì cứ làm nấy, đâu vẫn vào đấy."),
         F(2, "Cách nói này rất linh hoạt. Có thể nói 该吃吃，该玩儿玩儿, đến lúc ăn thì ăn, đến lúc chơi thì chơi; hoặc 该打球打球; hoặc 该什么结果还是什么结果, kết quả thế nào thì vẫn thế ấy, khi động từ là chữ 是 thì nó được lược đi."),
         F(3, "Ví dụ một: 在中国，过年过节商店最忙了，哪儿有假呀，该开门就得开门。 Ở Trung Quốc, dịp lễ Tết cửa hàng bận nhất, làm gì có ngày nghỉ, phải mở cửa thì vẫn phải mở cửa."),
         F(4, "Ví dụ hai, lấy từ bài khóa: 守在门口的大黄和白白也不是长时间在门口等他，而是在屋里该干吗干吗。 Đại Hoàng và Bạch Bạch không chờ ở cửa thật lâu, mà ở trong nhà làm việc của mình như thường."),
         F(5, "Ví dụ ba: 哭、着急都不管用，该什么结果还是什么结果。 Khóc hay sốt ruột đều vô ích, kết quả thế nào thì vẫn thế ấy.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: dùng 该干吗干吗 và biến thể viết lại câu", reveal=True, size=36,
    items=["(1) 到点了，走吧，别等她了。",
           "Đáp án: 到点了，该走就走吧，别等她了。",
           "(2) 不管是和平年代还是战争年代，人们到了年龄就会恋爱、结婚，丝毫没有改变。",
           "Đáp án: ……人们该恋爱恋爱，该结婚结婚，丝毫没有改变。",
           "(3) 没有什么事情能让他发愁，他整天都是乐呵呵的，吃、玩儿都不耽误。",
           "Đáp án: ……他整天都是乐呵呵的，该吃吃，该玩儿玩儿。"],
    say=[F(0, "Luyện tập: dùng mẫu 该打球打球 hoặc dạng rút gọn để viết lại câu. Câu một: 到点了，走吧，别等她了。 Đến giờ rồi, đi thôi, đừng đợi cô ấy nữa. Các bạn thử viết lại nhé."),
         F(1, "Đáp án gợi ý: 到点了，该走就走吧，别等她了。 Đến giờ rồi, phải đi thì cứ đi thôi."),
         F(2, "Câu hai: 不管是和平年代还是战争年代，人们到了年龄就会恋爱、结婚，丝毫没有改变。 Dù là thời bình hay thời chiến, người ta đến tuổi là yêu đương, kết hôn, không hề thay đổi."),
         F(3, "Đáp án gợi ý: 人们该恋爱恋爱，该结婚结婚，丝毫没有改变。 Đến lúc yêu thì yêu, đến lúc cưới thì cưới."),
         F(4, "Câu ba: 没有什么事情能让他发愁，他整天都是乐呵呵的，吃、玩儿都不耽误。 Chẳng có chuyện gì làm anh ấy phiền lòng, cả ngày lúc nào cũng tươi cười hớn hở, ăn chơi chẳng lỡ việc gì."),
         F(5, "Đáp án gợi ý: 他整天都是乐呵呵的，该吃吃，该玩儿玩儿。 Đến lúc ăn thì ăn, đến lúc chơi thì chơi. Cách nói này mang sắc thái thoải mái, vô tư.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 急切 – 急忙", section="Phân biệt từ 词语辨析", title="Phân biệt 急切 và 急忙",
    common="Giống nhau: đều có nghĩa sốt ruột, gấp gáp, nhưng thường không thay thế cho nhau được.",
    cols=[{"head": "急切",
           "lines": ["(1) Tính từ: tâm trạng mong mỏi bức thiết",
                     "Đúng: 大家急切地盼望试验成功。",
                     "(2) Có thể đứng trước danh từ",
                     "Đúng: 你急切的心情我们都能理解。"]},
          {"head": "急忙",
           "lines": ["(1) Phó từ: vì sốt ruột mà hành động vội vàng",
                     "Đúng: 听说公司有要紧事，他急忙穿上衣服跑出门去。",
                     "(2) Chỉ đứng trước động từ, không đứng trước danh từ",
                     "Sai: 他急忙的样子。"]}],
    say=["Tiếp theo là phần phân biệt từ: 急切 và 急忙. Hai từ này đều có chữ 急, nên học sinh rất hay dùng lẫn lộn.",
         "Điểm giống nhau: cả hai đều mang nghĩa sốt ruột, gấp gáp, nhưng thông thường không thể thay thế cho nhau.",
         F(0, "Điểm khác thứ nhất. 急切 là tính từ, nói về tâm trạng: mong mỏi rất bức thiết, nôn nóng trong lòng. Ví dụ: 大家急切地盼望试验成功。 Mọi người nôn nóng mong thí nghiệm thành công. Trong bài khóa cũng có: 每天最急切盼望的就是回家开门的那一刻."),
         F(1, "Còn 急忙 là phó từ, nói về hành động: vì sốt ruột mà làm một việc rất vội vàng, hấp tấp. Ví dụ: 听说公司有要紧事，他急忙穿上衣服跑出门去。 Nghe nói công ty có việc gấp, anh ấy vội vàng mặc áo chạy ra ngoài."),
         F(0, "Điểm khác thứ hai. Vì là tính từ, 急切 có thể đứng trước danh từ làm định ngữ. Ví dụ: 你急切的心情我们都能理解，但凡事都要慢慢来。 Tâm trạng nôn nóng của bạn chúng tôi đều hiểu, nhưng việc gì cũng phải từ từ."),
         F(1, "Còn 急忙 là phó từ, phía sau chỉ có thể là động từ, không thể là danh từ. Vì vậy không nói 他急忙的样子. Muốn tả dáng vẻ vội vàng, phải dùng 匆忙: 他匆忙的样子."),
         "Mẹo nhớ: 急切 là trong lòng gấp, thường đi với các động từ tâm lý như 盼望，希望，想知道; còn 急忙 là tay chân vội, đi với các động từ hành động như 跑，穿，赶."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: chọn 急切 hay 急忙?", reveal=True, size=36,
    items=["(1) 一听说是急诊病人，大夫___进行抢救。",
           "Đáp án: 急忙 – hành động vội vàng (抢救)",
           "(2) 妈妈___地盼望孩子早点儿放假回家。",
           "Đáp án: 急切 – tâm trạng mong mỏi (盼望)",
           "(3) 她___的表情引起了我的注意。",
           "Đáp án: 急切 – đứng trước danh từ (表情)",
           "(4) 一接到命令我们就___出发了，没来得及跟大家告别。",
           "Đáp án: 急忙 – hành động vội vàng (出发)"],
    say=[F(0, "Bây giờ chúng ta làm thử: chọn 急切 hay 急忙 để điền vào chỗ trống. Câu một: 一听说是急诊病人，大夫什么进行抢救。 Vừa nghe nói là bệnh nhân cấp cứu, bác sĩ liền làm gì để cấp cứu? Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: 急忙. 大夫急忙进行抢救。 Bác sĩ vội vàng tiến hành cấp cứu. Đây là hành động vội vàng."),
         F(2, "Câu hai: 妈妈什么地盼望孩子早点儿放假回家。 Mẹ mong con sớm được nghỉ về nhà."),
         F(3, "Đáp án: 急切. 妈妈急切地盼望孩子早点儿放假回家。 盼望 là động từ tâm lý, nói về tâm trạng mong mỏi."),
         F(4, "Câu ba: 她什么的表情引起了我的注意。 Vẻ mặt thế nào của cô ấy đã thu hút sự chú ý của tôi."),
         F(5, "Đáp án: 急切. 她急切的表情引起了我的注意。 Phía sau là danh từ 表情, nên chỉ có tính từ 急切 mới dùng được."),
         F(6, "Câu bốn: 一接到命令我们就什么出发了，没来得及跟大家告别。 Vừa nhận được lệnh, chúng tôi liền xuất phát, không kịp chào tạm biệt mọi người."),
         F(7, "Đáp án: 急忙. 我们就急忙出发了。 Chúng tôi vội vàng lên đường. Đây là hành động vội vàng, vì gấp quá nên không kịp chào ai.")])

# ======================= MỞ RỘNG: CÂU SAI Ý KHÔNG RÕ RÀNG =======================
add("bullets", chapter="Mở rộng: câu sai ý không rõ", section="Mở rộng 扩展", title="Câu sai: ý không rõ ràng (表意不明)", size=34,
    items=["Người đọc không hiểu chính xác ý của câu, rất khó hiểu",
           "Chủ yếu do đại từ chỉ thay không rõ ràng (指代不明)",
           "## (1) 它 chỉ cái gì?",
           "Sai: 醋最好不要和羊肉一起吃，一起吃会使它的温补作用大打折扣。",
           "Sửa: ……一起吃会使羊肉的温补作用大打折扣。",
           "## (2) Chủ ngữ ngầm thay đổi",
           "Sai: 慕尼黑的啤酒生产已有四百多年历史了，它以清香甘醇而遐迩闻名，因而素有“啤酒城”之称。"],
    say=["Bây giờ chúng ta sang phần mở rộng của sách. Quyển Thượng không có mục tu từ riêng, thay vào đó là kỹ năng nhận biết câu sai. Các bài trước chúng ta đã học câu thiếu thành phần, câu sai trật tự từ, câu sai do kết hợp từ; hôm nay là câu sai do ý không rõ ràng, tiếng Trung gọi là 表意不明.",
         F(0, "表意不明 là khi người đọc không hiểu được ý chính xác của câu, đọc xong thấy rất khó hiểu, hoặc có thể hiểu theo nhiều cách."),
         F(1, "Lỗi này chủ yếu xuất hiện khi đại từ chỉ thay không rõ ràng, tiếng Trung gọi là 指代不明. Tức là dùng 它，他，这，自己 mà người đọc không biết nó chỉ ai, chỉ cái gì."),
         F(2, "Ví dụ một: đại từ 它 chỉ cái gì?"),
         F(3, "Câu sai: 醋最好不要和羊肉一起吃，一起吃会使它的温补作用大打折扣。 Giấm tốt nhất đừng ăn cùng thịt dê, ăn cùng sẽ làm tác dụng bồi bổ, làm ấm cơ thể của nó giảm đi nhiều."),
         F(4, "Chữ 它 ở vế sau chỉ giấm hay chỉ thịt dê? Không rõ. Theo ý câu, thứ có tác dụng bồi bổ là thịt dê, nên phải đổi 它 thành 羊肉: 一起吃会使羊肉的温补作用大打折扣。"),
         F(5, "Ví dụ hai: chủ ngữ ngầm thay đổi."),
         F(6, "Câu sai: 慕尼黑的啤酒生产已有四百多年历史了，它以清香甘醇而遐迩闻名，因而素有啤酒城之称。 Ngành sản xuất bia của Munich đã có hơn bốn trăm năm lịch sử, nó nổi tiếng gần xa nhờ hương thơm, vị ngọt đậm, vì thế từ lâu đã được gọi là thành phố bia.")])

add("bullets", section="Mở rộng 扩展", title="Câu sai ý không rõ ràng: phân tích tiếp", size=34,
    items=["Sửa (2): 慕尼黑生产啤酒已有四百多年历史了，素有“啤酒城”之称，那里的啤酒以清香甘醇而遐迩闻名。",
           "## (3) “这方面” chỉ việc gì?",
           "Sai: 唱好一首歌不容易，创作出一首好歌更不容易，她是个文艺爱好者，平时在这方面下了不少功夫。",
           "## (4) Thiếu thông tin rõ ràng",
           "Sai: 开刀的是他父亲。 (bác sĩ mổ hay người bị mổ?)",
           "## (5) Thiếu chủ ngữ ở vế giữa",
           "Sai: 记得吗，我和你认识的时候，还是个中学生，充满热情，充满理想。"],
    say=[F(0, "Phân tích câu hai: 它 chỉ bia, còn thứ được gọi là thành phố bia lại là Munich. Như vậy vế thứ hai và thứ ba đã ngầm đổi chủ ngữ, khiến cả câu khó hiểu. Sửa: 慕尼黑生产啤酒已有四百多年历史了，素有啤酒城之称，那里的啤酒以清香甘醇而遐迩闻名。 Munich sản xuất bia đã hơn bốn trăm năm, từ lâu được gọi là thành phố bia, bia ở đó nổi tiếng gần xa nhờ hương thơm vị ngọt đậm."),
         F(1, "Ví dụ ba: cụm 这方面 chỉ việc gì?"),
         F(2, "Câu sai: 唱好一首歌不容易，创作出一首好歌更不容易，她是个文艺爱好者，平时在这方面下了不少功夫。 Hát hay một bài hát đã không dễ, sáng tác ra một bài hát hay còn khó hơn, cô ấy là người yêu văn nghệ, ngày thường đã bỏ nhiều công sức vào mặt này. Mặt này là hát hay, hay là sáng tác? Không rõ. Phải nói rõ một trong hai."),
         F(3, "Ví dụ bốn: thiếu thông tin rõ ràng."),
         F(4, "Câu sai: 开刀的是他父亲。 Người mổ là bố anh ấy. Câu này có thể hiểu là bố anh ấy là bác sĩ cầm dao mổ, cũng có thể hiểu bố anh ấy là bệnh nhân được mổ. Phải bổ sung cho rõ, ví dụ: 给病人开刀的是他父亲, hoặc 做手术的病人是他父亲。"),
         F(5, "Ví dụ năm: thiếu chủ ngữ ở vế giữa."),
         F(6, "Câu sai: 记得吗，我和你认识的时候，还是个中学生，充满热情，充满理想。 Nhớ không, lúc tôi và bạn quen nhau, vẫn còn là học sinh trung học, tràn đầy nhiệt huyết và lý tưởng. Ai là học sinh trung học, tôi hay bạn? Phải thêm chủ ngữ: 我还是个中学生, hoặc 你还是个中学生。")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chỉ ra lỗi và sửa lại (1)", reveal=True, size=34,
    items=["(1) 我一定说服妈妈和你一同去，这样你在路上就有个伴儿了。",
           "Đáp án: Ai đi cùng? → 我一定说服妈妈，让她和你一同去，……",
           "(2) 今天师傅在班会上表扬了自己，但是我觉得还需要继续努力。",
           "Đáp án: 自己 chỉ ai? → 今天师傅在班会上表扬了我，但是我觉得自己还需要继续努力。",
           "(3) 小张和小王商量好了，他请他看电影，他请他吃饭。",
           "Đáp án: 他 chỉ ai? → 小张请小王看电影，小王请小张吃饭。"],
    say=[F(0, "Luyện tập: chỉ ra lỗi của các câu sau và đề xuất cách sửa. Câu một: 我一定说服妈妈和你一同去，这样你在路上就有个伴儿了。 Tôi nhất định thuyết phục mẹ cùng đi với bạn, như vậy trên đường bạn sẽ có bạn đồng hành. Câu này không rõ ở đâu? Các bạn tạm dừng và suy nghĩ nhé."),
         F(1, "Đáp án: không rõ ai đi cùng bạn, là mẹ hay là tôi. Nếu là mẹ, sửa: 我一定说服妈妈，让她和你一同去。 Nếu là tôi, sửa: 我一定说服妈妈，让我和你一同去。"),
         F(2, "Câu hai: 今天师傅在班会上表扬了自己，但是我觉得还需要继续努力。 Hôm nay sư phụ khen bản thân trong buổi họp lớp, nhưng tôi thấy còn cần phải cố gắng hơn."),
         F(3, "Đáp án: 自己 có thể là sư phụ, cũng có thể là tôi. Theo ý câu, người được khen là tôi. Sửa: 今天师傅在班会上表扬了我，但是我觉得自己还需要继续努力。"),
         F(4, "Câu ba: 小张和小王商量好了，他请他看电影，他请他吃饭。 Tiểu Trương và Tiểu Vương bàn bạc xong rồi, anh ấy mời anh ấy xem phim, anh ấy mời anh ấy ăn cơm."),
         F(5, "Đáp án: bốn chữ 他 không biết chỉ ai. Sửa: 小张请小王看电影，小王请小张吃饭。")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chỉ ra lỗi và sửa lại (2)", reveal=True, size=34,
    items=["(4) 对学生会提出的建议，我举双手赞成。",
           "Đáp án: 学生会 = hội sinh viên, hay 学生 + 会 (sẽ)? → 对学生会这个组织提出的建议，…… / 对学生们将会提出的建议，……",
           "(5) 我看见小李和他女朋友有说有笑地走过来，肩上背着双肩包。",
           "Đáp án: Ai đeo ba lô? → 我看见小李肩上背着双肩包，和他女朋友有说有笑地走过来。"],
    say=[F(0, "Câu bốn: 对学生会提出的建议，我举双手赞成。 Câu này có hai cách hiểu, các bạn có nhận ra không?"),
         F(1, "Đáp án: 学生会 có thể là một danh từ, nghĩa là hội sinh viên; cũng có thể là 学生 cộng 会, nghĩa là học sinh sẽ đề xuất. Sửa cho rõ: 对学生会这个组织提出的建议, hoặc 对学生们将会提出的建议, tôi giơ cả hai tay tán thành."),
         F(2, "Câu năm: 我看见小李和他女朋友有说有笑地走过来，肩上背着双肩包。 Tôi thấy Tiểu Lý và bạn gái vừa nói vừa cười đi tới, trên vai đeo ba lô."),
         F(3, "Đáp án: ai đeo ba lô, Tiểu Lý hay bạn gái anh ấy, hay cả hai? Nếu là Tiểu Lý, sửa: 我看见小李肩上背着双肩包，和他女朋友有说有笑地走过来。 Mẹo: khi viết, mỗi lần dùng đại từ như 他，它，自己，这, hãy tự hỏi xem người đọc có biết chắc nó chỉ ai không.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ có dấu chấm", size=40,
    items=["拜访 (拜) → 拜会 · 拜见 · 拜望 · 拜年",
           "灵敏 (灵) → 灵活 · 灵巧 · 机灵 · 失灵",
           "亲热 (热) → 热情 · 热心 · 热爱 · 热闹",
           "镜头 (镜) → 眼镜 · 镜子 · 墨镜 · 望远镜",
           "误差 (误) → 错误 · 误会 · 失误 · 耽误"],
    say=["Phần luyện tập. Bài tập một: mô phỏng ví dụ, viết thêm các từ có chứa chữ được đánh dấu chấm.",
         F(0, "Ví dụ mẫu: 拜访, chữ được đánh dấu là chữ đầu, nghĩa là bái, thăm viếng với lòng kính trọng. Ta có 拜会，拜见，拜望，拜年. Tức là đến gặp, bái kiến, thăm hỏi, và chúc Tết."),
         F(1, "灵敏, chữ được đánh dấu là chữ đầu, nghĩa là nhanh nhạy. Ta có 灵活，灵巧，机灵，失灵. Tức là linh hoạt, khéo léo, lanh lợi, và mất tác dụng, như máy móc bị hỏng."),
         F(2, "亲热, chữ được đánh dấu là chữ thứ hai, nghĩa là nóng, nhiệt tình. Ta có 热情，热心，热爱，热闹. Tức là nhiệt tình, sốt sắng, yêu tha thiết, và náo nhiệt."),
         F(3, "镜头, chữ được đánh dấu là chữ đầu, nghĩa là kính, gương. Ta có 眼镜，镜子，墨镜，望远镜. Tức là kính mắt, cái gương, kính râm, và ống nhòm."),
         F(4, "误差, chữ được đánh dấu là chữ đầu, nghĩa là sai, lỡ. Ta có 错误，误会，失误，耽误. Tức là sai lầm, hiểu lầm, sơ suất, và làm lỡ việc.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Hoàn thành câu bằng từ cho sẵn (1)", reveal=True, size=36,
    items=["(1) 我不喜欢的东西___。（统统）",
           "Đáp án: 我不喜欢的东西统统扔掉了。",
           "(2) 他的心情一点儿都没受这个坏消息的影响，___。（该+动词+宾语+动词+宾语）",
           "Đáp án: ……该上班上班，该睡觉睡觉。",
           "(3) 上个周末我___，我们聊得很高兴。（拜访）",
           "Đáp án: 上个周末我去拜访了一位老同学，我们聊得很高兴。"],
    say=[F(0, "Bài tập hai: dùng từ hoặc cấu trúc cho sẵn để hoàn thành câu. Câu một, dùng 统统: 我不喜欢的东西，后面怎么说？ Những thứ tôi không thích thì sao? Các bạn tạm dừng và thử hoàn thành nhé."),
         F(1, "Đáp án gợi ý: 我不喜欢的东西统统扔掉了。 Những thứ tôi không thích, tôi vứt hết rồi. Cũng có thể nói 统统送给别人了, đem cho người khác hết."),
         F(2, "Câu hai, dùng mẫu 该打球打球: 他的心情一点儿都没受这个坏消息的影响。 Tâm trạng anh ấy không hề bị tin xấu này ảnh hưởng chút nào."),
         F(3, "Đáp án gợi ý: 该上班上班，该睡觉睡觉。 Đến giờ đi làm thì đi làm, đến giờ ngủ thì ngủ, tức là mọi thứ vẫn như bình thường."),
         F(4, "Câu ba, dùng 拜访: 上个周末我，后面怎么说？ 我们聊得很高兴。 Cuối tuần trước tôi làm gì, chúng tôi trò chuyện rất vui."),
         F(5, "Đáp án gợi ý: 上个周末我去拜访了一位老同学，我们聊得很高兴。 Cuối tuần trước tôi đi thăm một người bạn học cũ, chúng tôi trò chuyện rất vui.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Hoàn thành câu bằng từ cho sẵn (2)", reveal=True, size=36,
    items=["(4) 每个人都应该遵守学校纪律，___。（例外）",
           "Đáp án: ……，谁也不能例外。",
           "(5) 任何事情都___，不要总依靠别人。（自力更生）",
           "Đáp án: 任何事情都要自力更生，不要总依靠别人。",
           "(6) 他游历过很多国家，___。（见多识广）",
           "Đáp án: 他游历过很多国家，是个见多识广的人。"],
    say=[F(0, "Câu bốn, dùng 例外: 每个人都应该遵守学校纪律。 Mọi người đều phải tuân thủ kỷ luật của trường."),
         F(1, "Đáp án gợi ý: 每个人都应该遵守学校纪律，谁也不能例外。 Không ai được ngoại lệ."),
         F(2, "Câu năm, dùng 自力更生: 任何事情都，后面怎么说？ 不要总依靠别人。 Việc gì cũng phải thế nào, đừng lúc nào cũng dựa vào người khác."),
         F(3, "Đáp án gợi ý: 任何事情都要自力更生，不要总依靠别人。 Việc gì cũng phải tự lực cánh sinh."),
         F(4, "Câu sáu, dùng 见多识广: 他游历过很多国家。 Anh ấy đã đi chu du nhiều nước."),
         F(5, "Đáp án gợi ý: 他游历过很多国家，是个见多识广的人。 Anh ấy là người thấy nhiều biết rộng. Cũng có thể nói ngắn gọn: 他游历过很多国家，见多识广。")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (1)", reveal=True, size=34,
    items=["## Từ cho sẵn: 敏捷 · 流浪 · 亲热 · 饲养 · 教养",
           "昨天，我在小区里遇到一只___狗，金色的毛发，动作___，看见我，___地跟在我身边。虽然它没有主人，但看起来很有___，像个君子似的。我心里想：这么帅气的狗，主人怎么忍心扔掉呢？我们人类一旦决定___一种动物，就要对它负责到底。",
           "Đáp án: 流浪 · 敏捷 · 亲热 · 教养 · 饲养"],
    say=[F(0, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn một có năm từ: 敏捷，流浪，亲热，饲养，教养."),
         F(1, "昨天，我在小区里遇到一只什么狗，金色的毛发，动作什么，看见我，什么地跟在我身边。虽然它没有主人，但看起来很有什么，像个君子似的。我心里想：这么帅气的狗，主人怎么忍心扔掉呢？我们人类一旦决定什么一种动物，就要对它负责到底。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 一只流浪狗，动作敏捷，亲热地跟在我身边，很有教养，一旦决定饲养一种动物。 Hôm qua, tôi gặp một con chó hoang trong khu dân cư, bộ lông màu vàng, động tác nhanh nhẹn, thấy tôi là quấn quýt đi theo bên cạnh. Tuy không có chủ, nhưng trông nó rất có giáo dục, như một người quân tử. Tôi nghĩ: một con chó đẹp như vậy, sao chủ nó nỡ vứt bỏ chứ? Loài người chúng ta một khi đã quyết định nuôi một con vật, thì phải có trách nhiệm với nó đến cùng.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (2)", reveal=True, size=34,
    items=["## Từ cho sẵn: 统统 · 快活 · 凝视 · 扑 · 趴",
           "最近，家里的母猫生了几只小猫。小家伙们___而好动。我一回家，它们就___过来，跟我玩耍。而母猫则___在沙发上___着它的孩子们，眼神中充满了母爱。现在我每天最急切盼望的就是早点儿回家看看它们，别的事情___都不重要。",
           "Đáp án: 快活 · 扑 · 趴 · 凝视 · 统统"],
    say=[F(0, "Đoạn hai có năm từ: 统统，快活，凝视，扑，趴."),
         F(1, "最近，家里的母猫生了几只小猫。小家伙们什么而好动。我一回家，它们就什么过来，跟我玩耍。而母猫则什么在沙发上什么着它的孩子们，眼神中充满了母爱。现在我每天最急切盼望的就是早点儿回家看看它们，别的事情什么都不重要。 Các bạn điền thử nhé."),
         F(2, "Đáp án: 快活而好动，就扑过来，母猫则趴在沙发上凝视着它的孩子们，别的事情统统都不重要。 Gần đây, mèo mẹ nhà tôi sinh mấy chú mèo con. Lũ nhóc vui vẻ và hiếu động. Tôi vừa về nhà, chúng liền nhào tới chơi đùa với tôi. Còn mèo mẹ thì nằm trên sofa chăm chú nhìn đàn con, ánh mắt tràn đầy tình mẫu tử. Giờ đây điều tôi nôn nóng mong đợi nhất mỗi ngày là được về nhà sớm để ngắm chúng, những việc khác đều không quan trọng."),
         "Các bạn thấy không, đoạn văn này dùng gần như toàn bộ những từ tả mèo trong bài khóa. Hãy đọc to nó vài lần để nhớ từ nhé."])

add("bullets", section="Luyện tập 练习", title="Bài tập 4: Sắp xếp các vế thành câu hoàn chỉnh", reveal=True, size=34,
    items=["(1) A. 小王压不住火气 B. 然后，又把脸趴在他的肩上 C. 突然用拳头打丈夫的肩膀 D. 哭了起来",
           "Đáp án: A C B D – 小王压不住火气，突然用拳头打丈夫的肩膀，然后，又把脸趴在他的肩上，哭了起来。",
           "(2) A. 山上住着个种树的老爷爷 B. 他的胡子很长 C. 听说在很远很远的地方有一座山 D. 白头发白眉毛白胡子 E. 一直拖到地上",
           "Đáp án: C A D B E – 听说在很远很远的地方有一座山，山上住着个种树的老爷爷，白头发白眉毛白胡子，他的胡子很长，一直拖到地上。"],
    say=[F(0, "Bài tập bốn: sắp xếp các vế câu theo trình tự kể để thành câu hoàn chỉnh. Đây là kỹ năng rất hay gặp trong đề thi. Câu một có bốn vế: A, 小王压不住火气。 B, 然后，又把脸趴在他的肩上。 C, 突然用拳头打丈夫的肩膀。 D, 哭了起来。 Các bạn tạm dừng và thử sắp xếp nhé."),
         F(1, "Đáp án: A C B D. 小王压不住火气，突然用拳头打丈夫的肩膀，然后，又把脸趴在他的肩上，哭了起来。 Tiểu Vương không nén được cơn giận, bỗng dùng nắm đấm đánh vào vai chồng, rồi lại gục mặt lên vai anh ấy, òa khóc. Mẹo: vế A có chủ ngữ nên đứng đầu; vế B có từ chỉ thứ tự 然后 và đại từ 他, nên phải đứng sau vế đã nhắc tới người chồng; vế D là kết quả cuối cùng."),
         F(2, "Câu hai có năm vế: A, 山上住着个种树的老爷爷。 B, 他的胡子很长。 C, 听说在很远很远的地方有一座山。 D, 白头发白眉毛白胡子。 E, 一直拖到地上。 Các bạn thử sắp xếp nhé."),
         F(3, "Đáp án: C A D B E. 听说在很远很远的地方有一座山，山上住着个种树的老爷爷，白头发白眉毛白胡子，他的胡子很长，一直拖到地上。 Nghe nói ở nơi rất xa có một ngọn núi, trên núi có một ông lão trồng cây, tóc trắng, lông mày trắng, râu trắng, râu ông rất dài, dài chấm đất. Mẹo: các vế nối với nhau như một sợi xích: 一座山 nối với 山上, 老爷爷 nối với tả ngoại hình, 胡子 nối với 他的胡子很长, rồi 一直拖到地上 nói rõ dài đến đâu.")])

add("bullets", section="Luyện tập 练习", title="Mở rộng 扩展: từ vựng đồ vật qua hình ảnh", size=36,
    items=["床单 ga trải giường · 铺床单 trải ga · 她正在给新床铺床单。",
           "膜 màng · 保鲜膜 màng bọc thực phẩm · 家里的保鲜膜用完了。",
           "锤 búa · 一把锤子 một cái búa · 帮我拿一把锤子过来。",
           "话筒 micro · 一个话筒 một chiếc micro · 桌子上放着一个话筒。",
           "轮胎 lốp xe · 一个轮胎 một cái lốp · 汽车的轮胎被扎破了。",
           "钩子 cái móc · 一个钩子 một cái móc · 钩子上挂着几个杯子。"],
    say=["Phần mở rộng thứ hai của sách là học từ qua hình ảnh: sáu danh từ chỉ đồ vật thường dùng trong nhà. Thầy đọc qua để các bạn làm quen nhé.",
         F(0, "床单, ga trải giường. 铺床单 là trải ga giường. Ví dụ: 她正在给新床铺床单。 Cô ấy đang trải ga cho chiếc giường mới."),
         F(1, "膜, màng mỏng. 保鲜膜 là màng bọc thực phẩm, nghĩa đen là màng giữ tươi. Ví dụ: 家里的保鲜膜用完了。 Màng bọc thực phẩm ở nhà dùng hết rồi."),
         F(2, "锤, cái búa, thường nói là 锤子, lượng từ là 把. Ví dụ: 帮我拿一把锤子过来。 Lấy giúp tôi cái búa lại đây."),
         F(3, "话筒, micro, ống nói. Ví dụ: 桌子上放着一个话筒。 Trên bàn có đặt một chiếc micro."),
         F(4, "轮胎, lốp xe. Ví dụ: 汽车的轮胎被扎破了。 Lốp xe ô tô bị đâm thủng rồi."),
         F(5, "钩子, cái móc. Ví dụ: 钩子上挂着几个杯子。 Trên móc có treo mấy cái cốc. Các bạn thử nhìn quanh nhà mình và gọi tên đồ vật bằng tiếng Trung nhé.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 11", size=36,
    items=["Từ vựng trọng tâm: 流浪 · 拜访 · 见多识广 · 教养 · 灵敏 · 敏捷 · 亲热 · 统统 · 凝视 · 监视 · 缺陷 · 自力更生 · 动静",
           "Ngữ pháp: 统统 (tất cả) · 以……为…… (lấy… làm…) · 该干吗干吗 (việc gì cứ làm nấy)",
           "Phân biệt: 急切 (tính từ, tâm trạng; trước danh từ được) ≠ 急忙 (phó từ, hành động vội)",
           "Mở rộng: câu sai do ý không rõ ràng · sắp xếp vế câu theo trình tự kể",
           "## Bài tập về nhà (运用)",
           "Dựa vào bài tập 5, viết tóm tắt bài khóa thành một đoạn văn khoảng 300 chữ"],
    say=["Chúng ta cùng tổng kết bài mười một.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 流浪，拜访，见多识广，教养，灵敏，敏捷，亲热，统统，凝视，监视，缺陷，自力更生，动静. Và đừng quên những từ dễ nhầm như 亲热，模范，清洁，监视，举动."),
         F(1, "Về ngữ pháp: 统统 là phó từ, nghĩa là tất cả, không trừ cái nào. Cấu trúc văn viết 以学生为主 nghĩa là lấy cái này làm cái kia, tương đương khẩu ngữ 把某物当作某物. Còn 该干吗干吗 là cách nói khẩu ngữ, nghĩa là việc gì cứ làm nấy, mọi thứ vẫn như cũ."),
         F(2, "Về phân biệt từ: 急切 là tính từ, nói về tâm trạng nôn nóng, có thể đứng trước danh từ; còn 急忙 là phó từ, nói về hành động vội vàng, chỉ đứng trước động từ."),
         F(3, "Về phần mở rộng: câu sai do ý không rõ ràng, chủ yếu là do đại từ chỉ thay không rõ; và kỹ năng sắp xếp các vế câu dựa vào chủ ngữ, từ nối và đại từ."),
         F(5, "Bài tập về nhà, theo phần vận dụng của sách: bài khóa giới thiệu mấy chú mèo đáng yêu nhà Tiền Tiểu Kỳ, tình cảm giữa chủ và mèo, và cho chúng ta biết lúc chủ vắng nhà thì mèo làm gì. Các bạn hãy tham khảo bài tập năm, viết tóm tắt bài khóa thành một đoạn văn ngắn khoảng ba trăm chữ. Nhớ thử dùng 统统，以学生为主 và 该干吗干吗 trong bài viết nhé."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Nếu nhà các bạn cũng có thú cưng, hãy thử quan sát xem lúc mình đi vắng chúng làm gì nhé. Hẹn gặp lại các bạn ở bài mười hai: 我们都爱白噪音, Chúng ta đều yêu tiếng ồn trắng. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Thượng) – Bài 11: 我不在时，猫在干什么？ (Các chú mèo làm gì khi tôi đi vắng?)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"干什么": "赣什么",          # gàn shénme
                    "干吗": "赣吗",              # gànmá
                    "好动": "号动",              # hàodòng
                    "好客": "号客",              # hàokè
                    "好奇": "号奇",              # hàoqí
                    "好强": "号强",              # hàoqiáng
                    "好学": "号学",              # hàoxué
                    "好胜": "号胜",              # hàoshèng
                    "好战": "号战",              # hàozhàn
                    "喜好": "喜号",              # xǐhào
                    "教养": "叫养",              # jiàoyǎng
                    "嗅觉": "嗅决",              # xiùjué
                    "模范": "魔范",              # mófàn
                    "伺候": "刺候",              # cìhou
                    "急切": "急窃",              # jíqiè
                    "猫舍": "猫社",              # māoshè
                    "自力更生": "自力耕生",      # zìlì-gēngshēng
                    "为例": "维例",              # wéilì
                    "为主": "维主",              # wéizhǔ
                    "为辅": "维辅",              # wéifǔ
                    "为标准音": "维标准音",      # wéi
                    "为基础": "维基础",          # wéi
                    "为敌人": "维敌人",          # wéi
                    "为目的": "维目的",          # wéi
                    "为最多": "维最多",          # wéi
                    "为研究": "维研究",          # wéi
                    "为荣": "维荣",              # wéiróng
                    "为本": "维本",              # wéiběn
                    "为某物": "维某物",          # wéi
                    "当作": "荡作",              # dàngzuò
                    "难倒": "难岛",              # nándǎo
                    "有假": "有架",              # yǒu jià
                    "大夫": "代夫",              # dàifu
                    "君子似的": "君子是的",      # shìde
                    "种树": "众树",              # zhòngshù
                    "铺床单": "扑床单",          # pū chuángdān
                    "扎破": "渣破",              # zhāpò
                    "背着": "杯着"},             # bēizhe
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai11.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
