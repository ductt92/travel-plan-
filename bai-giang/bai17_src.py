#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Thượng) – Bài 17 «小动物眼中的慢世界». Chạy để sinh bai17.json."""
import json
import os

TAG = "HSK 6 (Thượng) · Bài 17 · 小动物眼中的慢世界"
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
    top="Giáo trình chuẩn HSK 6 – Quyển Thượng",
    zh="小动物眼中的慢世界", py="Xiǎo dòngwù yǎn zhōng de màn shìjiè",
    vi="Bài 17: Thế giới chậm trong mắt động vật nhỏ",
    sub="Chủ đề 5: 美丽家园 – Quê hương xinh đẹp",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Thượng.",
         "Hôm nay chúng ta học bài mười bảy: 小动物眼中的慢世界。 Nghĩa là: Thế giới chậm trong mắt động vật nhỏ.",
         "Đây là bài mở đầu của Chủ đề năm, 美丽家园, Quê hương xinh đẹp. Chủ đề này đưa chúng ta đến gần hơn với thiên nhiên và thế giới sinh vật quanh mình.",
         "Bài khóa bắt đầu từ một chuyện rất quen thuộc: vì sao con người đập ruồi mãi không trúng, mà con mèo lại vồ một cái là bắt được? Câu trả lời nằm ở tốc độ xử lý thông tin của mắt, mà các nhà khoa học đo bằng một chỉ số gọi là tần số nhấp nháy tới hạn. Trong mắt những con vật nhỏ, thế giới của chúng ta chậm như một thước phim quay chậm."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài khóa: vì sao động vật nhỏ thấy con người chậm chạp, và chỉ số CFF là gì",
           "Nắm vững 44 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: mẫu 东A西B, động từ 中 (zhòng), phó từ 姑且",
           "Phân biệt 势必 và 一定",
           "Mở rộng: câu sai do lẫn lộn cấu trúc (句式杂糅) và nghĩa của yếu tố cấu tạo từ"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa: vì sao trong mắt động vật nhỏ, con người phản ứng chậm chạp, và chỉ số CFF đo điều gì."),
         F(1, "Thứ hai, nắm vững bốn mươi bốn từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học ba điểm ngữ pháp: mẫu 东A西B, như trong 东张西望; động từ trúng, đọc thanh bốn, như trong 打中 và 中毒; và phó từ 姑且, nghĩa là tạm thời, tạm cứ."),
         F(3, "Thứ tư, phân biệt hai phó từ cùng nghĩa tất sẽ: 势必 và 一定."),
         F(4, "Thứ năm, phần mở rộng: nhận biết câu sai do trộn lẫn hai cấu trúc, tiếng Trung gọi là 句式杂糅, và làm quen với nghĩa của các yếu tố cấu tạo trong mười hai từ."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Câu hỏi khởi động: Vì sao khó đập trúng ruồi?", size=40,
    items=["人为什么很难一下子拍到苍蝇（cāngying, con ruồi）？",
           "人太笨了 – người quá vụng về",
           "苍蝇的视力很好 – thị lực của ruồi rất tốt",
           "苍蝇飞得很快 – ruồi bay rất nhanh",
           "苍蝇有预感 – ruồi có linh cảm",
           "在苍蝇眼里，人的动作太慢了 – trong mắt ruồi, động tác của người quá chậm"],
    say=["Chúng ta bắt đầu bằng phần khởi động. Sách cho một bức ảnh: một chiếc vỉ ruồi đang nhắm vào một con ruồi.",
         F(0, "人为什么很难一下子拍到苍蝇？ Vì sao con người rất khó đập trúng ruồi ngay một lần? 苍蝇 là con ruồi. Sách yêu cầu các bạn chọn đáp án mình cho là đúng."),
         F(1, "人太笨了。 Người quá vụng về. 笨 là vụng, chậm."),
         F(2, "苍蝇的视力很好。 Thị lực của ruồi rất tốt. 视力 là từ mới của bài hôm nay."),
         F(3, "苍蝇飞得很快。 Ruồi bay rất nhanh."),
         F(4, "苍蝇有预感。 Ruồi có linh cảm, biết trước nguy hiểm."),
         F(5, "在苍蝇眼里，人的动作太慢了。 Trong mắt con ruồi, động tác của con người quá chậm. Các bạn chọn đáp án nào? Hãy tạm dừng video và trả lời bằng tiếng Trung. Đọc xong bài khóa, các bạn sẽ biết đáp án mà khoa học đưa ra.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 收 và 型", size=36,
    items=["## 收 (thu): nhận vào, gom về",
           "接收 tiếp nhận · 吸收 hấp thụ · 查收 kiểm nhận · 收入 thu nhập · 收到 nhận được",
           "收据 biên lai · 收发 nhận và gửi · 收看 xem (TV) · 收留 cưu mang · 收录 đưa vào (sách, tuyển tập)",
           "收取 thu (phí) · 收集 thu thập · 收听 nghe (đài) · 收养 nhận nuôi",
           "## 型 (hình): kiểu, dạng, cỡ",
           "体型 vóc dáng · 类型 loại hình · 大型 cỡ lớn · 中型 cỡ vừa · 小型 cỡ nhỏ · 微型 siêu nhỏ · 巨型 khổng lồ",
           "型号 mẫu mã · 成型 thành hình · 发型 kiểu tóc · 新型 kiểu mới · 轻型 loại nhẹ · 血型 nhóm máu · 原型 nguyên mẫu"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo.",
         F(0, "Nhóm thứ nhất có chữ Hán Việt là thu, như trong 收到, nghĩa là nhận vào, gom về."),
         F(1, "接收，吸收，查收，收入，收到。 Tức là: tiếp nhận, hấp thụ, kiểm tra và nhận, thu nhập, nhận được. Từ 接收 có trong bài khóa: 接收的信息量, lượng thông tin tiếp nhận được."),
         F(2, "收据，收发，收看，收留，收录。 Tức là: biên lai, nhận và gửi, xem truyền hình, cưu mang, và đưa vào một tuyển tập."),
         F(3, "收取，收集，收听，收养。 Tức là: thu phí, thu thập, nghe đài, và nhận con nuôi."),
         F(4, "Nhóm thứ hai có chữ Hán Việt là hình, như trong 类型, nghĩa là kiểu, dạng, cỡ."),
         F(5, "体型，类型，大型，中型，小型，微型，巨型。 Tức là: vóc dáng, loại hình, cỡ lớn, cỡ vừa, cỡ nhỏ, siêu nhỏ, khổng lồ. Từ 体型 xuất hiện nhiều lần trong bài, chỉ kích thước cơ thể của con vật."),
         F(6, "型号，成型，发型，新型，轻型，血型，原型。 Tức là: mẫu mã, thành hình, kiểu tóc, kiểu mới, loại nhẹ, nhóm máu, và nguyên mẫu.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 感 và 率", size=36,
    items=["## 感 (cảm): cảm nhận, cảm giác",
           "感知 cảm nhận, nhận biết · 感受 cảm nhận · 感觉 cảm giác · 感到 cảm thấy · 灵感 cảm hứng",
           "快感 khoái cảm · 敏感 nhạy cảm · 痛感 cảm giác đau · 同感 cùng cảm nhận · 预感 linh cảm · 语感 ngữ cảm",
           "## 率 (suất, đọc lǜ): tỉ lệ, tốc độ",
           "速率 tốc độ · 频率 tần số, tần suất · 心率 nhịp tim · 比率 tỉ lệ · 概率 xác suất · 汇率 tỉ giá · 利率 lãi suất",
           "出生率 tỉ lệ sinh · 死亡率 tỉ lệ tử vong · 就业率 tỉ lệ có việc · 失业率 tỉ lệ thất nghiệp · 离婚率 tỉ lệ ly hôn"],
    say=[F(0, "Nhóm thứ ba có chữ Hán Việt là cảm, nghĩa là cảm nhận, cảm giác."),
         F(1, "感知，感受，感觉，感到，灵感。 Tức là: cảm nhận và nhận biết, cảm nhận, cảm giác, cảm thấy, và cảm hứng. Bài khóa có cụm 视觉感知, sự cảm nhận bằng thị giác."),
         F(2, "快感，敏感，痛感，同感，预感，语感。 Tức là: khoái cảm, nhạy cảm, cảm giác đau, cùng chung cảm nhận, linh cảm, và ngữ cảm, tức là cảm giác về ngôn ngữ."),
         F(3, "Nhóm cuối cùng có chữ Hán Việt là suất, như trong 频率, ở đây đọc là lǜ, thanh bốn, nghĩa là tỉ lệ, hoặc tốc độ."),
         F(4, "速率，频率，心率，比率，概率，汇率，利率。 Tức là: tốc độ, tần số, nhịp tim, tỉ lệ, xác suất, tỉ giá, lãi suất. Hai từ 速率 và 频率 là từ khóa của bài khóa hôm nay."),
         F(5, "出生率，死亡率，就业率，失业率，离婚率。 Tức là: tỉ lệ sinh, tỉ lệ tử vong, tỉ lệ có việc làm, tỉ lệ thất nghiệp, và tỉ lệ ly hôn. Các bạn thấy đấy, cứ gắn chữ này vào sau một danh từ là ta có tỉ lệ của việc đó.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay khi đọc riêng từ])
V = [
    ("场面", "chǎngmiàn", "trường diện", "danh từ", "cảnh, cảnh tượng (trong hoàn cảnh nhất định)", "婚礼的场面非常热闹。", "Cảnh tượng đám cưới vô cùng náo nhiệt.",
     "Danh từ, chỉ cảnh tượng, quang cảnh diễn ra trong một hoàn cảnh cụ thể. Câu mở đầu bài khóa chính là: 你见过这样的场面吗？ Bạn đã từng thấy cảnh này chưa? Hay gặp: 感人的场面, cảnh cảm động; 大场面, cảnh hoành tráng."),
    ("端", "duān", "đoan", "động từ", "bưng, mang (bằng tay)", "服务员端来了两杯咖啡。", "Nhân viên phục vụ bưng tới hai cốc cà phê.",
     "Động từ, nghĩa là bưng, dùng tay giữ ngang một vật rồi mang đi, như bưng bát, bưng đĩa. Trong bài: 有人端来一个盘子, có người bưng tới một cái đĩa. Âm Hán Việt là đoan, như trong 端正, đoan chính."),
    ("盛", "chéng", "thịnh", "động từ", "đựng, chứa; xới (cơm), múc (canh)", "他给我盛了一碗饭。", "Anh ấy xới cho tôi một bát cơm.",
     "Động từ, ở đây đọc là chéng, thanh hai, nghĩa là đựng, chứa; hoặc xới cơm, múc canh vào bát. Trong bài: 一个盛着菜的盘子, một cái đĩa đựng thức ăn. Các bạn nhớ: chữ này khi đọc shèng, thanh bốn, lại có nghĩa là thịnh vượng, như trong 茂盛, tươi tốt.", "成"),
    ("东张西望", "dōngzhāng-xīwàng", "đông trương tây vọng", "thành ngữ", "nhìn ngang nhìn dọc, nhìn quanh quất", "他站在门口东张西望，好像在等人。", "Anh ấy đứng ở cửa nhìn quanh quất, hình như đang đợi ai.",
     "Thành ngữ, nghĩa là nhìn chỗ này rồi nhìn chỗ kia, nhìn quanh quất. Trong bài: 一只东张西望的苍蝇, một con ruồi nhìn ngang nhìn dọc. Đây là ví dụ của mẫu 东A西B, điểm ngữ pháp đầu tiên của bài."),
    ("企图", "qǐtú", "xí đồ", "động từ", "mưu tính, mưu toan, định", "小偷企图从窗户逃走。", "Tên trộm định trốn ra qua cửa sổ.",
     "Động từ, nghĩa là mưu toan, định làm một việc gì, thường là việc xấu hoặc việc khó thành. Trong bài: con ruồi 企图落在盘子上, định đậu xuống đĩa. Cũng dùng như danh từ: 他的企图, ý đồ của hắn."),
    ("动手", "dòng shǒu", "động thủ", "động từ", "bắt tay vào làm; ra tay, giơ tay đánh", "时间不多了，我们赶快动手吧。", "Không còn nhiều thời gian, chúng ta mau bắt tay vào làm đi.",
     "Động từ ly hợp, có hai nghĩa: bắt tay vào làm, và giơ tay đánh người. Cẩn thận: động thủ trong tiếng Việt chủ yếu là ra tay đánh nhau, còn tiếng Trung rất hay dùng nghĩa bắt tay vào làm, như 自己动手做饭, tự tay nấu cơm. Trong bài, 人动手去打 là người giơ tay đập ruồi."),
    ("纳闷儿", "nà mènr", "nạp muộn nhi", "động từ", "thắc mắc, thấy khó hiểu, bối rối", "他今天怎么没来？我真纳闷儿。", "Sao hôm nay cậu ấy không đến nhỉ? Tôi thật thắc mắc.",
     "Động từ, khẩu ngữ, nghĩa là thấy khó hiểu, thắc mắc trong lòng. Chữ thứ hai đọc mèn, thanh bốn, có âm cuốn lưỡi. Trong bài: 有人纳闷儿, có người thắc mắc, vì sao mèo bắt ruồi giỏi vậy."),
    ("跳跃", "tiàoyuè", "khiêu dược", "động từ", "nhảy, bật nhảy", "小鹿在草地上快乐地跳跃。", "Chú nai con vui vẻ nhảy nhót trên bãi cỏ.",
     "Động từ, mang màu sắc văn viết hơn 跳, nghĩa là nhảy, bật lên. Trong bài: 猫能快速跳跃起来, mèo có thể bật nhảy lên thật nhanh. Hay gặp: 跳跃式发展, phát triển nhảy vọt."),
    ("瞄准", "miáo zhǔn", "miêu chuẩn", "động từ", "nhắm, ngắm trúng (mục tiêu)", "他瞄准目标，开了一枪。", "Anh ấy nhắm vào mục tiêu rồi bắn một phát.",
     "Động từ, nghĩa là ngắm, nhắm vào mục tiêu; nghĩa bóng là nhắm tới, như 瞄准市场, nhắm vào thị trường. Trong bài: 瞄准都不用, chẳng cần nhắm, mèo cũng vồ trúng ruồi."),
    ("鸽子", "gēzi", "cáp tử", "danh từ", "chim bồ câu", "广场上有很多白鸽子。", "Trên quảng trường có rất nhiều chim bồ câu trắng.",
     "Danh từ, chim bồ câu. Âm tiết sau đọc nhẹ. Hay gặp: 和平鸽, chim bồ câu hòa bình. Trong bài, tác giả lấy chim bồ câu làm ví dụ cho việc động vật nhỏ tiếp nhận thông tin rất nhanh."),
    ("视线", "shìxiàn", "thị tuyến", "danh từ", "ánh mắt, tầm mắt, đường ngắm", "前面的大树挡住了我的视线。", "Cái cây lớn phía trước che mất tầm nhìn của tôi.",
     "Danh từ, chỉ đường nhìn của mắt, tầm mắt. Trong bài: 视线扫过周边, ánh mắt lướt qua xung quanh. Hay gặp: 挡住视线, che khuất tầm nhìn; 转移视线, đánh lạc hướng sự chú ý."),
    ("周边", "zhōubiān", "chu biên", "danh từ", "xung quanh, vùng lân cận", "学校周边有很多小饭馆。", "Xung quanh trường có rất nhiều quán ăn nhỏ.",
     "Danh từ, chỉ khu vực xung quanh, gần nghĩa với 周围. Hay gặp: 周边国家, các nước láng giềng; 周边地区, khu vực lân cận."),
    ("颤抖", "chàndǒu", "chiến đẩu", "động từ", "run, run rẩy", "她冷得全身颤抖。", "Cô ấy lạnh đến run rẩy cả người.",
     "Động từ, nghĩa là run, run rẩy vì lạnh, vì sợ hoặc vì xúc động. Cẩn thận: âm Hán Việt chiến đẩu nghe rất giống chiến đấu, nhưng hoàn toàn khác nghĩa; chiến đấu tiếng Trung là 战斗. Chữ đầu đọc chàn, thanh bốn. Trong bài: 它在微微颤抖, nó khẽ run lên."),
    ("确切", "quèqiè", "xác thiết", "tính từ", "chính xác, xác thực", "我想知道确切的时间。", "Tôi muốn biết thời gian chính xác.",
     "Tính từ, nghĩa là chính xác, đúng đắn, gần nghĩa với 准确. Trong bài có cụm rất hay dùng: 确切地说, nói một cách chính xác thì."),
    ("迟钝", "chídùn", "trì độn", "tính từ", "chậm chạp, không nhạy bén, không lanh lợi", "年纪大了，反应有点儿迟钝。", "Tuổi cao rồi, phản ứng hơi chậm chạp.",
     "Tính từ, nghĩa là chậm hiểu, phản ứng chậm, không nhạy bén; trái nghĩa với 敏锐 mà các bạn đã học ở bài bảy. Trong bài: 人类反应迟钝, con người phản ứng chậm chạp."),
    ("迟缓", "chíhuǎn", "trì hoãn", "tính từ", "chậm chạp, rề rà, lờ đờ", "老人的动作有些迟缓。", "Động tác của cụ già hơi chậm chạp.",
     "Tính từ, nghĩa là chậm chạp, chậm rì. Đây là từ dễ nhầm: trì hoãn trong tiếng Việt là kéo dài, lùi lại, tiếng Trung nói là 推迟 hoặc 拖延; còn 迟缓 chỉ tốc độ chậm. Trong bài: 动作迟缓, động tác chậm chạp."),
    ("庞大", "pángdà", "bàng đại", "tính từ", "khổng lồ, to lớn, đồ sộ", "这是一个非常庞大的计划。", "Đây là một kế hoạch vô cùng đồ sộ.",
     "Tính từ, nghĩa là to lớn, đồ sộ, dùng cho hình thể, tổ chức hoặc số lượng. Trong bài: 庞大、笨拙的大象, con voi to lớn, vụng về. Hay gặp: 机构庞大, bộ máy cồng kềnh."),
    ("笨拙", "bènzhuō", "bổn chuyết", "tính từ", "vụng về, lóng ngóng", "小熊走路的样子很笨拙。", "Dáng đi của chú gấu con rất vụng về.",
     "Tính từ, nghĩa là vụng về, lóng ngóng, không khéo léo. Chữ sau đọc zhuō, thanh một. Gần nghĩa với 笨, nhưng văn viết hơn."),
    ("比方", "bǐfang", "tỉ phương", "động từ", "ví như, chẳng hạn như", "我喜欢吃水果，比方说苹果、香蕉。", "Tôi thích ăn hoa quả, chẳng hạn như táo, chuối.",
     "Động từ, nghĩa là ví như, chẳng hạn; cụm 比方说 dùng giống 比如说. Cũng là danh từ: 打个比方, lấy một ví dụ so sánh. Âm tiết sau đọc nhẹ."),
    ("间隔", "jiàngé", "gián cách", "động từ", "cách nhau, ngắt quãng; khoảng cách", "两次吃药要间隔四个小时。", "Hai lần uống thuốc phải cách nhau bốn tiếng.",
     "Động từ, nghĩa là cách nhau một khoảng thời gian hay không gian; cũng dùng như danh từ, khoảng cách. Chữ đầu đọc jiàn, thanh bốn. Trong bài: 间隔频率较低的光, ánh sáng có tần số ngắt quãng thấp."),
    ("闪烁", "shǎnshuò", "thiểm thước", "động từ", "lấp lánh, lập lòe, lung linh", "夜空中，星星在闪烁。", "Trên bầu trời đêm, các vì sao đang lấp lánh.",
     "Động từ, nghĩa là ánh sáng lúc sáng lúc tối, lấp lánh, nhấp nháy. Trong bài: 一明一暗的闪烁, ánh sáng nhấp nháy lúc sáng lúc tối. Thành ngữ: 闪烁其词, nói lấp lửng, úp mở."),
    ("视力", "shìlì", "thị lực", "danh từ", "thị lực", "长时间看手机会影响视力。", "Xem điện thoại lâu sẽ ảnh hưởng đến thị lực.",
     "Danh từ, nghĩa là thị lực, khả năng nhìn của mắt, giống hệt tiếng Việt. Hay gặp: 视力很好, mắt rất tinh; 视力下降, thị lực giảm."),
    ("姑且", "gūqiě", "cô thả", "phó từ", "tạm, tạm thời", "这个办法不太好，我们姑且试试吧。", "Cách này không hay lắm, chúng ta tạm thử xem sao.",
     "Phó từ, nghĩa là tạm thời cứ như thế đã, mang ý miễn cưỡng, nhân nhượng. Đây là điểm ngữ pháp thứ ba của bài."),
    ("文雅", "wényǎ", "văn nhã", "tính từ", "nho nhã, lịch sự", "她说话很文雅。", "Cô ấy nói năng rất nho nhã.",
     "Tính từ, nghĩa là nho nhã, thanh lịch trong lời nói, cử chỉ. Trong bài, tác giả đùa: 我们姑且换一个文雅的称呼吧, ta tạm đổi một cách gọi nho nhã hơn, tức là gọi con chó bằng một từ văn vẻ hơn."),
    ("犬", "quǎn", "khuyển", "danh từ", "chó (khuyển)", "警犬帮助警察找到了线索。", "Chó nghiệp vụ đã giúp cảnh sát tìm ra manh mối.",
     "Danh từ, nghĩa là chó, dùng trong văn viết; khẩu ngữ nói 狗. Đây chính là cách gọi văn nhã mà tác giả nhắc tới. Hay gặp: 警犬, chó nghiệp vụ; 导盲犬, chó dẫn đường cho người khiếm thị."),
    ("系列", "xìliè", "hệ liệt", "danh từ", "loạt, dãy, chuỗi", "政府采取了一系列措施。", "Chính phủ đã áp dụng một loạt biện pháp.",
     "Danh từ, chỉ một loạt sự vật liên quan với nhau, thường dùng thành 一系列, một loạt. Trong bài: 一系列静止图像, một loạt hình ảnh tĩnh."),
    ("推论", "tuīlùn", "suy luận", "động từ", "suy luận, suy ra", "根据这些材料，我们可以推论出他的年龄。", "Dựa vào những tài liệu này, chúng ta có thể suy ra tuổi của anh ấy.",
     "Động từ, nghĩa là từ tiền đề mà suy ra kết luận; cũng là danh từ, lời suy luận. Âm Hán Việt suy luận giống hệt tiếng Việt. Trong bài: 有科学家推论, có nhà khoa học suy luận rằng."),
    ("本身", "běnshēn", "bản thân", "danh từ", "bản thân, tự thân (sự vật)", "这个问题本身并不难。", "Bản thân vấn đề này không hề khó.",
     "Danh từ, nghĩa là bản thân sự vật, tự nó. Chú ý: tiếng Việt bản thân hay chỉ người, như bản thân tôi; tiếng Trung nói về người thường dùng 自己, còn 本身 hay dùng cho sự vật, như trong bài: 其本身的体重, trọng lượng của chính loài ấy."),
    ("新陈代谢", "xīnchén-dàixiè", "tân trần đại tạ", "danh từ", "sự trao đổi chất", "运动可以促进新陈代谢。", "Vận động có thể thúc đẩy quá trình trao đổi chất.",
     "Danh từ, nghĩa đen là cái mới thay cái cũ; trong sinh học là quá trình trao đổi chất. Âm Hán Việt không dùng trong tiếng Việt, các bạn nhớ nghĩa là trao đổi chất. Gọi tắt là 代谢, như 代谢速率, tốc độ trao đổi chất."),
    ("能量", "néngliàng", "năng lượng", "danh từ", "năng lượng", "巧克力能很快补充能量。", "Sô cô la có thể bổ sung năng lượng rất nhanh.",
     "Danh từ, năng lượng, giống tiếng Việt. Nghĩa bóng hiện nay hay gặp: 正能量, năng lượng tích cực. Trong bài: 更充足的能量支持, có năng lượng hỗ trợ dồi dào hơn."),
    ("论证", "lùnzhèng", "luận chứng", "động từ", "lập luận chứng minh, thẩm định", "专家们正在论证这个方案是否可行。", "Các chuyên gia đang thẩm định xem phương án này có khả thi không.",
     "Động từ, nghĩa là đưa ra lý lẽ và chứng cứ để chứng minh một quan điểm, hoặc thẩm định một phương án. Trong bài: 在论证这一推论时, khi chứng minh suy luận này."),
    ("筛选", "shāixuǎn", "si tuyển", "động từ", "chọn lọc, sàng lọc", "公司从一百多份简历中筛选出了五个人。", "Công ty đã sàng lọc ra năm người từ hơn một trăm bộ hồ sơ.",
     "Động từ. Chữ đầu là cái sàng, chữ sau là chọn; gộp lại nghĩa là sàng lọc, chọn ra những cái phù hợp. Trong bài: 科学家筛选出三十四种动物, các nhà khoa học chọn ra ba mươi tư loài động vật."),
    ("标记", "biāojì", "tiêu ký", "động từ", "đánh dấu, dán nhãn; ký hiệu", "请把重要的地方用红笔标记出来。", "Hãy dùng bút đỏ đánh dấu những chỗ quan trọng.",
     "Động từ, nghĩa là đánh dấu; cũng là danh từ, dấu hiệu, ký hiệu. Trong bài: 把它们的典型体重标记在同一张图表中, đánh dấu trọng lượng điển hình của chúng trên cùng một biểu đồ."),
    ("名次", "míngcì", "danh thứ", "danh từ", "thứ hạng, thứ bậc", "他在这次比赛中取得了很好的名次。", "Anh ấy đã giành được thứ hạng rất tốt trong cuộc thi lần này.",
     "Danh từ, chỉ thứ tự xếp hạng trong một cuộc thi hay một danh sách. Âm Hán Việt không dùng trong tiếng Việt. Trong bài: 名次最靠前的是松鼠, đứng đầu bảng xếp hạng là con sóc."),
    ("感慨", "gǎnkǎi", "cảm khái", "động từ", "cảm khái, xúc động, bùi ngùi", "看到老照片，他感慨万千。", "Nhìn những bức ảnh cũ, anh ấy trăm mối bùi ngùi.",
     "Động từ, nghĩa là xúc động, dâng lên nhiều cảm xúc và suy nghĩ trước một sự việc; cũng là danh từ: 发出感慨, buông lời cảm thán. Thành ngữ hay gặp: 感慨万千."),
    ("渺小", "miǎoxiǎo", "miểu tiểu", "tính từ", "nhỏ bé, nhỏ nhoi", "在大自然面前，人类显得非常渺小。", "Trước thiên nhiên, con người trở nên vô cùng nhỏ bé.",
     "Tính từ, nghĩa là nhỏ bé, nhỏ nhoi, không đáng kể; trái nghĩa với 伟大, vĩ đại. Trong bài: 看似渺小的苍蝇, con ruồi trông có vẻ nhỏ bé."),
    ("攻击", "gōngjī", "công kích", "động từ", "tấn công, công kích", "这种动物受到攻击时会装死。", "Loài vật này khi bị tấn công sẽ giả chết.",
     "Động từ, nghĩa là tấn công; nghĩa bóng là công kích, chỉ trích người khác. Tiếng Việt cũng dùng cả hai nghĩa. Trong bài: 躲过人类的攻击, tránh được đòn tấn công của con người."),
    ("势必", "shìbì", "thế tất", "phó từ", "tất phải, ắt sẽ", "不注意休息，势必会影响健康。", "Không chú ý nghỉ ngơi thì ắt sẽ ảnh hưởng đến sức khỏe.",
     "Phó từ, nghĩa là theo đà phát triển của sự việc thì tất yếu sẽ dẫn đến kết quả nào đó, kết quả thường là điều không tốt. Lát nữa chúng ta sẽ phân biệt kỹ 势必 với 一定."),
    ("博大精深", "bódà-jīngshēn", "bác đại tinh thâm", "thành ngữ", "uyên thâm, uyên bác, rộng lớn sâu sắc", "中国文化博大精深。", "Văn hóa Trung Quốc rộng lớn và sâu sắc.",
     "Thành ngữ, nghĩa là rộng lớn và sâu sắc, dùng cho tư tưởng, học vấn, văn hóa. Trong bài: 它们没有博大精深的思想, chúng không có tư tưởng uyên thâm."),
    ("深奥", "shēn'ào", "thâm áo", "tính từ", "sâu xa, uyên áo, khó hiểu", "这本书的内容太深奥了。", "Nội dung cuốn sách này quá sâu xa, khó hiểu.",
     "Tính từ, nghĩa là sâu xa, khó hiểu, dùng cho đạo lý, kiến thức. Chú ý: sâu sắc trong tiếng Việt là lời khen, còn 深奥 thiên về khó hiểu. Trong bài: 深奥的思考, suy nghĩ sâu xa."),
    ("无能为力", "wúnéngwéilì", "vô năng vi lực", "thành ngữ", "bất lực, không làm gì được", "对于这件事，我也无能为力。", "Đối với việc này, tôi cũng đành bất lực.",
     "Thành ngữ, nghĩa là không có khả năng làm gì, bất lực. Chữ thứ ba đọc wéi, thanh hai. Trong bài: 对强大的对手无能为力, bất lực trước đối thủ mạnh."),
    ("实惠", "shíhuì", "thực huệ", "tính từ", "thiết thực, có lợi; rẻ mà tốt", "这家饭馆的菜又好吃又实惠。", "Món ăn của quán này vừa ngon vừa rẻ.",
     "Tính từ, nghĩa là có lợi ích thiết thực; khẩu ngữ rất hay dùng với nghĩa giá cả phải chăng, ngon bổ rẻ. Âm Hán Việt không dùng trong tiếng Việt. Trong bài: 这一优势真的实惠极了, ưu thế này thật vô cùng có ích."),
    ("个体", "gètǐ", "cá thể", "danh từ", "cá thể", "每个人都是一个独立的个体。", "Mỗi người đều là một cá thể độc lập.",
     "Danh từ, chỉ một cá thể riêng lẻ, người hoặc động vật. Trong bài: 成年个体, cá thể trưởng thành. Cụm hay gặp: 个体户, hộ kinh doanh cá thể."),
    ("焦急", "jiāojí", "tiêu cấp", "tính từ", "sốt ruột, nôn nóng, lo lắng", "妈妈焦急地等着孩子回家。", "Mẹ sốt ruột đợi con về nhà.",
     "Tính từ, nghĩa là sốt ruột, lo lắng như lửa đốt, mang màu sắc văn viết. Trong bài: 总显得更为好动和焦急, lúc nào cũng tỏ ra hiếu động và sốt ruột hơn."),
]

add("bullets", chapter="Từ mới (44 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 17 có 44 từ mới, chia thành 15 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 盛 (chéng) · 颤抖 (chàn) · 间隔 (jiàn) · 笨拙 (zhuō) · 无能为力 (wéi)",
           "Từ dễ nhầm: 颤抖 · 迟缓 · 动手 · 本身 · 深奥"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có bốn mươi bốn từ, thầy chia thành mười lăm nhóm nhỏ, mỗi nhóm hai hoặc ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số từ có âm đọc cần chú ý, như 颤抖，间隔，笨拙，无能为力, và động từ có nghĩa là đựng, xới cơm. Thầy sẽ nhắc khi gặp."),
         F(4, "Ngoài ra, có mấy từ Hán Việt rất dễ hiểu nhầm, như 颤抖，迟缓，动手，本身，深奥. Nghĩa của chúng trong tiếng Trung khác với tiếng Việt, các bạn nhớ nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

sizes = [3] * 14 + [2]
assert sum(sizes) == len(V)
assert all(len(v) in (8, 9) for v in V)
g = 0
for gs in sizes:
    group = V[g:g + gs]
    words, say = [], []
    for i, v in enumerate(group):
        zh, py, hv, loai, vi, ex, exvi, expl = v[:8]
        spk = v[8] if len(v) > 8 else zh
        n = g + i + 1
        words.append({"zh": zh, "py": py, "hv": hv.upper(), "loai": f"{n}. {loai}", "vi": vi, "ex": ex, "exvi": exvi})
        say.append(F(i, f"Từ số {n}: {spk}。 {spk}。 Hán Việt là {hv}.", zr=120,
                     cap=f"Từ số {n}: {zh}。 {zh}。 Hán Việt là {hv}."))
        say.append(F(i, f"{expl} Ví dụ: {ex}{'' if ex[-1] in '。…？！，' else '，'} {exvi[0].upper() + exvi[1:]}{'' if exvi.endswith(('.', '!', '?')) else '.'}", zr=130))
    add("vocab", section="Từ mới 生词", title=f"Từ mới ({g + 1}–{g + len(group)} / {len(V)})",
        words=words, say=say)
    g += gs

# ======================= BÀI KHÓA =======================
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung nếu khác])
P = [
    ("你见过这样的场面吗？有人端来一个盛着菜的盘子，立刻飞来一只东张西望的苍蝇，企图落在盘子上，人动手去打，却总是打不中。",
     "Bạn đã từng thấy cảnh này chưa? Có người bưng tới một đĩa thức ăn, lập tức một con ruồi nhìn ngang nhìn dọc bay đến, định đậu xuống đĩa, người ta giơ tay đập, nhưng lần nào cũng đập không trúng.",
     ["Bài khóa mở đầu bằng một câu hỏi để gợi sự chú ý của người đọc. 盛着菜的盘子 là cái đĩa đựng thức ăn; 着 biểu thị trạng thái đang tiếp diễn.",
      "落在盘子上 là đậu xuống đĩa. 打不中 là đập không trúng, đây là bổ ngữ khả năng với động từ trúng, điểm ngữ pháp thứ hai của bài."]),
    ("有人纳闷儿，猫为什么能快速跳跃起来，瞄准都不用，一下就能拍到苍蝇？科学家这样解释：在苍蝇眼里，人类自认为闪电般快速的一拍，只是个慢动作而已。",
     "Có người thắc mắc, vì sao con mèo có thể bật nhảy thật nhanh, chẳng cần nhắm, vồ một cái là trúng ruồi? Các nhà khoa học giải thích thế này: trong mắt con ruồi, cú đập mà con người tự cho là nhanh như chớp, chẳng qua chỉ là một động tác quay chậm mà thôi.",
     ["瞄准都不用 là ngay cả nhắm cũng không cần; 都 ở đây nhấn mạnh, nghĩa là ngay cả. 一下就能 là chỉ một cái là đã có thể.",
      "闪电般快速 là nhanh như tia chớp; 般 nghĩa là giống như. 只是……而已 là chỉ là… mà thôi, mẫu này các bạn đã học ở bài năm."]),
    ("有研究表明，昆虫这样的小动物，一秒钟之内接收的信息量，比人类等体型大的生物多得多。",
     "Có nghiên cứu cho thấy, những động vật nhỏ như côn trùng, lượng thông tin tiếp nhận trong vòng một giây nhiều hơn rất nhiều so với những sinh vật có vóc dáng lớn như con người.",
     ["有研究表明 là có nghiên cứu cho thấy, cách mở đầu rất hay gặp trong văn khoa học. 昆虫 là côn trùng.",
      "信息量 là lượng thông tin. 人类等体型大的生物 là các sinh vật vóc dáng lớn như con người; 等 ở đây là vân vân. 比……多得多 là nhiều hơn… rất nhiều."]),
    ("如果你观察一下鸽子就会发现，当它的视线扫过周边时，它在微微颤抖，看上去好像体内有另外一个钟表，走得比我们快好几倍。",
     "Nếu bạn quan sát chim bồ câu sẽ phát hiện ra, khi ánh mắt nó lướt qua xung quanh, nó khẽ run lên, trông như thể trong cơ thể nó có một chiếc đồng hồ khác, chạy nhanh hơn của chúng ta mấy lần.",
     ["当……时 là khi…. 视线扫过周边 là ánh mắt lướt qua xung quanh; 扫 vốn là quét, ở đây là lướt nhìn. 微微 là khẽ, hơi hơi.",
      "体内 là trong cơ thể. 钟表 là đồng hồ nói chung. 快好几倍 là nhanh hơn mấy lần; 好几 là khá nhiều, mấy."]),
    ("确切地说，在小动物看来，人类反应迟钝、动作迟缓，它们看人类，就像人类看庞大、笨拙的大象。",
     "Nói chính xác thì, theo cách nhìn của động vật nhỏ, con người phản ứng chậm chạp, động tác chậm rì; chúng nhìn con người, cũng giống như con người nhìn những chú voi to lớn, vụng về.",
     ["确切地说 là nói một cách chính xác. 在……看来 là theo cách nhìn của ai đó, rất hay dùng để nêu quan điểm.",
      "Hai cặp từ mới 迟钝 và 迟缓 đều bắt đầu bằng chữ trì, nghĩa là chậm. 就像……一样 là giống như; ở đây lược bỏ 一样."]),
    ("为了量化这种看不见、摸不着的视觉感知，科研人员采用了临界闪光频率的办法。“临界闪光频率”简称“CFF (Critical Flicker Frequency)”，",
     "Để định lượng loại cảm nhận thị giác không nhìn thấy, không sờ được này, các nhà nghiên cứu đã dùng phương pháp tần số nhấp nháy tới hạn. Tần số nhấp nháy tới hạn được gọi tắt là CFF,",
     ["量化 là lượng hóa, tức là biến thành con số để đo. 看不见、摸不着 là không nhìn thấy, không sờ được, ý nói rất trừu tượng. 科研人员 là nhân viên nghiên cứu khoa học.",
      "临界 là tới hạn, 闪光 là ánh sáng nhấp nháy, 频率 là tần số. 简称 là gọi tắt; CFF là viết tắt tiếng Anh của cụm này."],
     "为了量化这种看不见、摸不着的视觉感知，科研人员采用了临界闪光频率的办法。临界闪光频率简称CFF。"),
    ("比方说，当一个间隔频率较低的光刺激我们的眼睛时，我们看到的是一明一暗的闪烁，随着光刺激间隔的缩短，我们的视力感到的就会是一个连续的光。",
     "Chẳng hạn, khi một nguồn sáng có tần số ngắt quãng khá thấp kích thích mắt chúng ta, cái chúng ta thấy là ánh sáng nhấp nháy lúc sáng lúc tối; theo đà khoảng cách giữa các lần kích thích rút ngắn lại, thị giác của chúng ta sẽ cảm nhận được một luồng sáng liên tục.",
     ["比方说 là chẳng hạn như. 刺激 là kích thích. 一明一暗 là lúc sáng lúc tối; mẫu 一A一B diễn tả hai trạng thái luân phiên.",
      "随着 là cùng với, theo đà. 缩短 là rút ngắn. 连续 là liên tục. Đây là cách giải thích CFF: tần số càng cao, ánh sáng nhấp nháy càng giống ánh sáng liên tục."]),
    ("CFF值反映的就是眼睛处理光线的速度。处理速度越快，CFF值就越高。",
     "Chỉ số CFF phản ánh chính là tốc độ mắt xử lý ánh sáng. Tốc độ xử lý càng nhanh, chỉ số CFF càng cao.",
     ["值 là trị số, chỉ số. 反映的就是 là cái phản ánh chính là; 就 ở đây nhấn mạnh.",
      "越……越…… là càng… càng…. Câu này là chìa khóa để hiểu phần sau: con vật nào có chỉ số càng cao, thì thấy thế giới càng chậm."]),
    ("人眼的CFF为60HZ左右，狗，哦，我们姑且换一个文雅的称呼吧，犬的CFF为80HZ。在犬的眼里，电视画面不是连续的，而是一系列静止图像的迅速变换。",
     "Chỉ số CFF của mắt người vào khoảng sáu mươi héc, còn chó, à, chúng ta tạm đổi một cách gọi nho nhã hơn vậy, chỉ số CFF của loài khuyển là tám mươi héc. Trong mắt loài khuyển, hình ảnh trên ti vi không liên tục, mà là một loạt hình ảnh tĩnh thay đổi rất nhanh.",
     ["为 ở đây đọc wéi, thanh hai, nghĩa là là, văn viết. HZ là héc, đơn vị đo tần số, tiếng Trung là 赫兹. Câu chen 我们姑且换一个文雅的称呼吧 rất dí dỏm: tác giả tạm đổi từ khẩu ngữ sang từ văn viết.",
      "不是……，而是…… là không phải…, mà là…. 一系列静止图像 là một loạt hình ảnh tĩnh. 迅速变换 là thay đổi nhanh chóng."],
     "人眼的CFF为六十赫兹左右，狗，哦，我们姑且换一个文雅的称呼吧，犬的CFF为八十赫兹。在犬的眼里，电视画面不是连续的，而是一系列静止图像的迅速变换。"),
    ("苍蝇的CFF高达250HZ，对视觉刺激的反应速度是人眼的4倍。",
     "Chỉ số CFF của ruồi cao tới hai trăm năm mươi héc, tốc độ phản ứng với kích thích thị giác gấp bốn lần mắt người.",
     ["高达 là cao tới, dùng để nhấn mạnh con số lớn. 对……的反应速度 là tốc độ phản ứng đối với….",
      "是……的四倍 là gấp bốn lần…. Bây giờ các bạn đã hiểu vì sao đập ruồi khó đến vậy: với con ruồi, cú đập của ta chậm như quay chậm."],
     "苍蝇的CFF高达二百五十赫兹，对视觉刺激的反应速度是人眼的四倍。"),
    ("有科学家推论，物种的CFF与其本身的体重和新陈代谢速率有关。体型越小，信号传达到大脑所需时间越短；新陈代谢速率越高，说明传递过程有更充足的能量支持。",
     "Có nhà khoa học suy luận rằng, chỉ số CFF của một loài có liên quan đến trọng lượng cơ thể và tốc độ trao đổi chất của chính loài đó. Vóc dáng càng nhỏ, thời gian cần để tín hiệu truyền tới não càng ngắn; tốc độ trao đổi chất càng cao, chứng tỏ quá trình truyền dẫn có năng lượng hỗ trợ dồi dào hơn.",
     ["与……有关 là có liên quan tới…. 其 là đại từ văn viết, nghĩa là của nó. 物种 là loài.",
      "所需时间 là thời gian cần thiết; 所 cộng động từ là cấu trúc văn viết. 充足 là đầy đủ, dồi dào. Câu dùng hai lần mẫu 越……越…… để nêu hai mối quan hệ."]),
    ("在论证这一推论时，科学家筛选出34种动物，把它们的典型体重、代谢速率和CFF标记在同一张图表中，变量显示出了显著的相关性。在科学家的研究中，CFF值名次最靠前的是松鼠。",
     "Khi chứng minh suy luận này, các nhà khoa học chọn ra ba mươi tư loài động vật, đánh dấu trọng lượng điển hình, tốc độ trao đổi chất và chỉ số CFF của chúng trên cùng một biểu đồ, các biến số cho thấy mối tương quan rõ rệt. Trong nghiên cứu của các nhà khoa học, loài đứng đầu về chỉ số CFF là con sóc.",
     ["这一推论 là suy luận này; 这一 là cách nói văn viết. 典型 là điển hình. 图表 là biểu đồ.",
      "变量 là biến số. 显著的相关性 là mối tương quan rõ rệt. 名次最靠前 là xếp hạng cao nhất. 松鼠 là con sóc."],
     "在论证这一推论时，科学家筛选出三十四种动物，把它们的典型体重、代谢速率和CFF标记在同一张图表中，变量显示出了显著的相关性。在科学家的研究中，CFF值名次最靠前的是松鼠。"),
    ("我们也许曾经发出过这样的感慨：看似渺小的苍蝇既然能躲过人类的攻击，势必有其过人之处。",
     "Có lẽ chúng ta từng thốt lên cảm thán thế này: con ruồi trông có vẻ nhỏ bé, đã có thể tránh được đòn tấn công của con người, thì ắt hẳn phải có chỗ hơn người.",
     ["发出感慨 là thốt lên lời cảm thán. 看似 là trông có vẻ. 既然……，…… là đã… thì….",
      "势必 là ắt hẳn, tất sẽ. 过人之处 là điểm hơn người; 之处 là chỗ, điểm, văn viết."]),
    ("确实，它们没有博大精深的思想，不能进行深奥的思考，对强大的对手无能为力，但对外部环境能迅速做出判断，使它们有了更多的生存机会，这一优势真的实惠极了。",
     "Quả thực, chúng không có tư tưởng uyên thâm, không thể suy nghĩ sâu xa, bất lực trước đối thủ mạnh, nhưng chúng có thể nhanh chóng phán đoán môi trường bên ngoài, điều đó giúp chúng có nhiều cơ hội sống sót hơn, ưu thế này thật vô cùng có ích.",
     ["Câu có cấu trúc nhượng bộ rồi chuyển ý: ba vế đầu nói điểm yếu, từ 但 trở đi nói điểm mạnh. 对……无能为力 là bất lực trước….",
      "使它们有了更多的生存机会 là khiến chúng có thêm cơ hội sinh tồn; 使 là khiến cho. 实惠极了 là vô cùng thiết thực."]),
    ("信息处理速度上的差别，也是小动物看上去更敏捷的原因。小猫小狗甚至小孩儿，总显得比成年个体更为好动和焦急，其实对于他们，这只是个悠闲的速度。",
     "Sự khác biệt về tốc độ xử lý thông tin cũng là nguyên nhân khiến động vật nhỏ trông nhanh nhẹn hơn. Mèo con, chó con, thậm chí trẻ nhỏ, lúc nào cũng tỏ ra hiếu động và sốt ruột hơn so với cá thể trưởng thành, nhưng thật ra đối với chúng, đó chỉ là một tốc độ thong thả mà thôi.",
     ["敏捷 là nhanh nhẹn. 甚至 là thậm chí. 显得 là tỏ ra, trông có vẻ. 更为 là càng, hơn, văn viết của 更.",
      "好动 ở đây chữ đầu đọc hào, thanh bốn, nghĩa là hiếu động. 悠闲 là thong thả, nhàn nhã. Bài được cải biên từ bài Sinh linh nhỏ, thế giới chậm của tác giả Thạch Duyệt, đăng trên tuần san Nam Đô."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 小动物眼中的慢世界", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 小动物眼中的慢世界, dài tám trăm bốn mươi lăm chữ. Đây là một bài văn phổ biến khoa học, viết rất dí dỏm, dễ hiểu.",
         F(0, "Thầy chia bài thành mười lăm đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
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
    items=["## 1. 在打苍蝇方面，人和猫有什么不同？为什么？",
           "人：动手、打不中 · 猫：一下子拍到 · 在苍蝇眼里，人的一拍只是个慢动作",
           "## 2. 昆虫等小动物在接收信息方面跟人类有什么不同？",
           "小动物：接收的信息量多得多，比如鸽子…… · 人类：反应迟钝、动作迟缓",
           "## 3. 什么是CFF？",
           "视觉感知、光刺激、闪烁、连续的光、处理光线的速度"],
    say=["Bài tập năm của sách yêu cầu dựa vào gợi ý để tóm tắt nội dung chính của bài khóa. Chúng ta cùng làm luôn nhé.",
         F(0, "Câu hỏi một: trong chuyện đập ruồi, người và mèo khác nhau thế nào? Vì sao?"),
         F(1, "Người thì 动手去打，却总是打不中, giơ tay đập mà mãi không trúng. Mèo thì 一下子就能拍到, vồ một cái là trúng. Vì 在苍蝇眼里，人类的一拍只是个慢动作, trong mắt con ruồi, cú đập của người chỉ là động tác quay chậm."),
         F(2, "Câu hỏi hai: côn trùng và các động vật nhỏ khác con người thế nào trong việc tiếp nhận thông tin?"),
         F(3, "Động vật nhỏ tiếp nhận lượng thông tin trong một giây nhiều hơn rất nhiều, ví dụ như chim bồ câu, như thể có một chiếc đồng hồ chạy nhanh hơn trong cơ thể. Còn trong mắt chúng, con người 反应迟钝、动作迟缓."),
         F(4, "Câu hỏi ba: CFF là gì?"),
         F(5, "Đó là phương pháp để định lượng cảm nhận thị giác. Khi ánh sáng nhấp nháy với khoảng cách ngắn dần, mắt sẽ thấy một luồng sáng liên tục. Chỉ số CFF phản ánh tốc độ mắt xử lý ánh sáng.")])

add("bullets", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5) – phần 2", size=34,
    items=["## 4. 人和狗等动物的CFF有何不同？",
           "人：60HZ左右 · 犬：80HZ · 苍蝇：250HZ，是人眼的4倍",
           "## 5. CFF与什么有关？苍蝇为什么能躲过人类的攻击？",
           "体重、新陈代谢 · 对外部环境迅速做出判断，使它们有了更多的生存机会",
           "## 6. 为什么小动物看上去更敏捷？",
           "信息处理速度：小猫小狗、小孩儿显得更为好动和焦急"],
    say=[F(0, "Câu hỏi bốn: chỉ số CFF của người, của chó và các động vật khác khác nhau thế nào?"),
         F(1, "Người khoảng sáu mươi héc, loài khuyển tám mươi héc, còn ruồi tới hai trăm năm mươi héc, gấp bốn lần mắt người."),
         F(2, "Câu hỏi năm: CFF liên quan đến điều gì? Và vì sao ruồi tránh được đòn tấn công của con người?"),
         F(3, "CFF liên quan tới trọng lượng cơ thể và tốc độ trao đổi chất. Ruồi tránh được đòn tấn công vì 对外部环境能迅速做出判断，使它们有了更多的生存机会, chúng phán đoán môi trường rất nhanh, nhờ vậy có nhiều cơ hội sống sót hơn."),
         F(4, "Câu hỏi sáu: vì sao động vật nhỏ trông nhanh nhẹn hơn?"),
         F(5, "Vì tốc độ xử lý thông tin khác nhau. Mèo con, chó con, trẻ nhỏ trông hiếu động và sốt ruột hơn, nhưng với chúng đó chỉ là tốc độ thong thả. Bố cục này rất có ích khi các bạn tự kể lại bài khóa, và cũng là gợi ý cho bài tập về nhà.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 东A西B", section="Ngữ pháp 注释", title="1. Mẫu 东A西B – chỗ này… chỗ kia…", size=38,
    items=["Biểu thị: chỗ này…, chỗ kia… (lặp lại, tản mạn, không có trật tự)",
           "A và B thường là những từ có nghĩa gần nhau",
           "大家吃完饭没事干，只好东拉西扯地闲聊天儿。",
           "有人端来一个盛着菜的盘子，立刻飞来一只东张西望的苍蝇……",
           "客人还不走，我只好跟他东一句西一句地没话找话说。"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là mẫu 东A西B.",
         F(0, "东张西望 được tạo thành từ mẫu 东A西B. Mẫu này biểu thị nghĩa: chỗ này thì…, chỗ kia thì…, diễn tả hành động lặp đi lặp lại, tản mạn, không có trật tự."),
         F(1, "A và B đứng sau 东 và 西 thường là những từ có nghĩa gần nhau, như 张 và 望 đều là nhìn."),
         F(2, "Ví dụ một: 大家吃完饭没事干，只好东拉西扯地闲聊天儿。 Mọi người ăn cơm xong không có việc gì làm, đành ngồi tán gẫu chuyện trên trời dưới biển. 东拉西扯 là nói lan man hết chuyện này sang chuyện khác."),
         F(3, "Ví dụ hai, lấy từ bài khóa: 有人端来一个盛着菜的盘子，立刻飞来一只东张西望的苍蝇。 Có người bưng tới một đĩa thức ăn, lập tức một con ruồi nhìn ngang nhìn dọc bay đến."),
         F(4, "Ví dụ ba: 客人还不走，我只好跟他东一句西一句地没话找话说。 Khách vẫn chưa về, tôi đành nói với anh ta câu được câu chăng, cố tìm chuyện để nói. Ở đây A và B đều là 一句. Ngoài ra còn hay gặp: 东躲西藏, trốn chỗ này nấp chỗ kia; 东奔西走, chạy ngược chạy xuôi.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: chọn từ thích hợp điền vào chỗ trống", reveal=True, size=36,
    items=["## Từ cho sẵn: 东拉西扯 · 东张西望 · 东躲西藏",
           "(1) 那孩子像是找不到家了，站在路口，______，显得有些着急。",
           "Đáp án: 东张西望",
           "(2) 黑猫被打败了，被大黄猫追得______，跳上跳下。",
           "Đáp án: 东躲西藏",
           "(3) 坐在火车上，大家都没事，便天南海北、______地闲聊起来。",
           "Đáp án: 东拉西扯"],
    say=[F(0, "Luyện tập: chọn từ thích hợp điền vào chỗ trống. Ba từ cho sẵn là: 东拉西扯，东张西望，东躲西藏."),
         F(1, "Câu một: 那孩子像是找不到家了，站在路口，什么，显得有些着急。 Đứa bé kia hình như không tìm được nhà, đứng ở ngã tư làm gì, trông hơi cuống. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 东张西望。 Đứng ở ngã tư nhìn quanh quất. Người bị lạc thì nhìn chỗ này chỗ kia để tìm đường."),
         F(3, "Câu hai: 黑猫被打败了，被大黄猫追得什么，跳上跳下。 Con mèo đen bị đánh thua, bị con mèo vàng to đuổi đến mức thế nào, nhảy lên nhảy xuống."),
         F(4, "Đáp án: 东躲西藏。 Bị đuổi đến mức trốn chỗ này nấp chỗ kia."),
         F(5, "Câu ba: 坐在火车上，大家都没事，便天南海北、什么地闲聊起来。 Ngồi trên tàu hỏa, mọi người đều rảnh rỗi, bèn tán gẫu chuyện trời nam biển bắc."),
         F(6, "Đáp án: 东拉西扯。 天南海北、东拉西扯地闲聊, tán gẫu lan man đủ thứ chuyện. Các bạn để ý, 天南海北 cũng có cấu trúc tương tự, ghép hai cặp phương hướng.")])

add("bullets", chapter="Ngữ pháp: động từ 中 (zhòng)", section="Ngữ pháp 注释", title="2. 中 (zhòng) – động từ: trúng; bị, mắc", size=36,
    items=["## (1) Nghĩa: đúng vào, trúng (正对上、恰好合上)",
           "有人端来一个盛着菜的盘子……人动手去打，却总是打不中。",
           "今天的谜语，猜中了有奖。",
           "## (2) Nghĩa: bị, gặp phải (受到、遭受)",
           "晚上再出去吧，中午太热，小心出门中暑。",
           "这种蘑菇不能吃，吃了会中毒的。"],
    say=["Điểm ngữ pháp thứ hai là động từ trúng. Chữ này các bạn quen đọc là zhōng, thanh một, như trong 中国; nhưng khi làm động từ, nó đọc thanh bốn, Hán Việt là trúng.",
         F(0, "Nghĩa thứ nhất: đúng vào, trúng vào mục tiêu, hoặc vừa khớp với điều gì. Tiếng Trung giải thích là 正对上、恰好合上."),
         F(1, "Ví dụ một, lấy từ bài khóa: 人动手去打，却总是打不中。 Người giơ tay đập, nhưng lần nào cũng không trúng. 打不中 là bổ ngữ khả năng, đập không trúng."),
         F(2, "Ví dụ hai: 今天的谜语，猜中了有奖。 Câu đố hôm nay, ai đoán trúng sẽ có thưởng. Tương tự còn có 打中，击中，选中，看中, tức là đánh trúng, bắn trúng, chọn trúng, và ưng ý."),
         F(3, "Nghĩa thứ hai: bị, gặp phải, mắc phải điều không tốt. Tiếng Trung giải thích là 受到、遭受."),
         F(4, "Ví dụ ba: 晚上再出去吧，中午太热，小心出门中暑。 Tối hãy ra ngoài, buổi trưa nóng quá, ra đường cẩn thận kẻo bị say nắng. 中暑 là trúng nắng, say nắng. Các bạn chú ý: trong 中午, chữ này vẫn đọc thanh một."),
         F(5, "Ví dụ bốn: 这种蘑菇不能吃，吃了会中毒的。 Loại nấm này không ăn được, ăn vào sẽ bị trúng độc. 中毒 là trúng độc, tiếng Việt cũng nói y như vậy.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: dùng từ có 中 (zhòng) hoàn thành câu", reveal=True, size=34,
    items=["(1) 他的腿被（ ）了，走不了了。",
           "Đáp án: 他的腿被打中了，走不了了。",
           "(2) 六几年我自学英语，（ ）一套英国Longman出版社的《基础英语》，……我就是靠这套书学会了英语。",
           "Đáp án: ……选中一套英国Longman出版社的《基础英语》……",
           "(3) 那是我第一次自己做主买衣服，妈妈陪我左看右看，最后我（ ）的竟然是一件白衬衫。",
           "Đáp án: ……最后我看中的竟然是一件白衬衫。"],
    say=[F(0, "Luyện tập: dùng từ có chữ trúng để hoàn thành câu. Câu một: 他的腿被什么了，走不了了。 Chân anh ấy bị làm sao đó, không đi được nữa. Các bạn tạm dừng và thử nhé."),
         F(1, "Đáp án gợi ý: 他的腿被打中了，走不了了。 Chân anh ấy bị bắn trúng, không đi được nữa. Cũng có thể nói 击中."),
         F(2, "Câu hai: 六几年我自学英语，什么一套英国出版社的基础英语，这套书两册是外文原版，两册是国内出的影印版，我就是靠这套书学会了英语。 Những năm sáu mươi tôi tự học tiếng Anh, làm gì với một bộ sách Tiếng Anh cơ bản của một nhà xuất bản Anh; bộ sách có hai cuốn nguyên bản, hai cuốn là bản in lại trong nước, tôi đã học được tiếng Anh nhờ bộ sách này."),
         F(3, "Đáp án gợi ý: 选中一套基础英语。 Chọn được một bộ sách Tiếng Anh cơ bản. 选中 là chọn trúng, chọn được cái ưng ý."),
         F(4, "Câu ba: 那是我第一次自己做主买衣服，妈妈陪我左看右看，最后我什么的竟然是一件白衬衫。 Đó là lần đầu tôi tự quyết định mua quần áo, mẹ đi cùng tôi xem tới xem lui, cuối cùng cái tôi làm sao lại là một chiếc áo sơ mi trắng."),
         F(5, "Đáp án gợi ý: 最后我看中的竟然是一件白衬衫。 Cuối cùng cái tôi ưng ý lại là một chiếc sơ mi trắng. 看中 là nhìn thấy mà ưng, rất hay dùng khi mua sắm.")])

add("bullets", chapter="Ngữ pháp: 姑且", section="Ngữ pháp 注释", title="3. 姑且 gūqiě – tạm thời, tạm cứ", size=38,
    items=["Phó từ: bất đắc dĩ, trong tình huống hiện tại tạm thời làm như vậy, sau sẽ tính tiếp",
           "Mang ý miễn cưỡng, nhân nhượng",
           "狗，哦，我们姑且换一个文雅的称呼吧，犬的CFF为80HZ。",
           "这件事，你姑且先答应下来，然后再慢慢想办法。",
           "别让你妈妈着急了，你姑且按她说的做吧。"],
    say=["Điểm ngữ pháp thứ ba là phó từ 姑且.",
         F(0, "姑且 là phó từ, biểu thị trong tình huống bất đắc dĩ, tạm thời cứ làm như vậy đã, sau này sẽ tính chuyện khác."),
         F(1, "Vì thế, 姑且 mang ý miễn cưỡng, nhân nhượng. Tiếng Việt có thể dịch là tạm, tạm cứ, đành tạm."),
         F(2, "Ví dụ một, lấy từ bài khóa: 狗，哦，我们姑且换一个文雅的称呼吧，犬的CFF为八十赫兹。 Chó, à, ta tạm đổi một cách gọi nho nhã hơn vậy, chỉ số CFF của loài khuyển là tám mươi héc."),
         F(3, "Ví dụ hai: 这件事，你姑且先答应下来，然后再慢慢想办法。 Việc này, cậu cứ tạm nhận lời đã, rồi từ từ nghĩ cách sau. 姑且 thường đi cùng 先, rồi sau đó là 然后再."),
         F(4, "Ví dụ ba: 别让你妈妈着急了，你姑且按她说的做吧。 Đừng để mẹ cậu sốt ruột nữa, cậu tạm làm theo lời mẹ đi. Các bạn thấy đấy, người nói không hoàn toàn đồng ý, chỉ là nhân nhượng tạm thời.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: chọn vị trí thích hợp cho phần trong ngoặc", reveal=True, size=34,
    items=["(1) A最后怎么处理，B等我了解了解情况再说C。（这件事姑且先这么办，）",
           "Đáp án: A → 这件事姑且先这么办，最后怎么处理，等我了解了解情况再说。",
           "(2) A说的随便说说，B都不必认真C。（听的姑且听听，）",
           "Đáp án: B → 说的随便说说，听的姑且听听，都不必认真。",
           "(3) A但有一点可以肯定：B腐败不得人心C。（他的看法是否正确姑且不论，）",
           "Đáp án: A → 他的看法是否正确姑且不论，但有一点可以肯定：腐败不得人心。"],
    say=[F(0, "Luyện tập: chọn vị trí thích hợp cho phần trong ngoặc. Câu một: 最后怎么处理，等我了解了解情况再说。 Phần cần đặt vào là: 这件事姑且先这么办. Các bạn tạm dừng và chọn nhé."),
         F(1, "Đáp án: A. 这件事姑且先这么办，最后怎么处理，等我了解了解情况再说。 Việc này tạm cứ làm thế đã, cuối cùng xử lý thế nào thì đợi tôi tìm hiểu tình hình rồi tính."),
         F(2, "Câu hai: 说的随便说说，都不必认真。 Phần cần đặt vào là: 听的姑且听听."),
         F(3, "Đáp án: B. 说的随便说说，听的姑且听听，都不必认真。 Người nói thì cứ nói chơi, người nghe thì tạm nghe vậy, đều không cần coi là thật. Hai vế đối nhau rất cân."),
         F(4, "Câu ba: 但有一点可以肯定：腐败不得人心。 Phần cần đặt vào là: 他的看法是否正确姑且不论."),
         F(5, "Đáp án: A. 他的看法是否正确姑且不论，但有一点可以肯定：腐败不得人心。 Quan điểm của anh ta đúng hay không thì tạm chưa bàn, nhưng có một điều chắc chắn: tham nhũng thì không được lòng dân. 姑且不论 là tạm gác lại chưa bàn, một cụm rất hay dùng.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 势必 – 一定", section="Phân biệt từ 词语辨析", title="Phân biệt 势必 và 一定 (1): phỏng đoán",
    common="Giống nhau: đều là phó từ, nghĩa là tất sẽ như thế. Ví dụ: 经常不来上课，势必/一定会影响考试成绩。",
    cols=[{"head": "势必",
           "lines": ["Dựa vào chiều hướng phát triển của sự việc, phỏng đoán chắc chắn sẽ có kết quả nào đó; kết quả phần nhiều bất lợi",
                     "Đúng: 人口过度增长势必影响经济水平的提高。"]},
          {"head": "一定",
           "lines": ["Biểu thị phỏng đoán, nhưng kết quả không nhất thiết là bất lợi",
                     "Đúng: 他是健身教练，身材一定很好。",
                     "Sai: 他是健身教练，身材势必很好。"]}],
    say=["Tiếp theo là phần phân biệt từ: 势必 và 一定. Cả hai đều có thể dịch là tất sẽ, chắc chắn sẽ, nên người học rất hay dùng lẫn lộn.",
         "Điểm giống nhau: khi làm phó từ, cả hai đều có nghĩa là tất yếu sẽ như thế nào. Ví dụ: 经常不来上课，势必会影响考试成绩, hoặc 一定会影响考试成绩, đều đúng. Thường xuyên không đến lớp thì chắc chắn sẽ ảnh hưởng đến kết quả thi.",
         F(0, "Điểm khác thứ nhất: 势必 biểu thị dựa vào chiều hướng phát triển của sự việc mà phỏng đoán chắc chắn sẽ xảy ra một kết quả, và kết quả phần nhiều là bất lợi. Ví dụ: 人口过度增长势必影响经济水平的提高。 Dân số tăng quá mức ắt sẽ ảnh hưởng đến việc nâng cao trình độ kinh tế."),
         F(1, "Còn 一定 cũng biểu thị phỏng đoán, nhưng kết quả không nhất thiết là bất lợi. Ví dụ: 他是健身教练，身材一定很好。 Anh ấy là huấn luyện viên thể hình, vóc dáng chắc chắn rất đẹp."),
         F(1, "Vì kết quả ở đây là điều tốt, nên không thể dùng 势必. Câu 身材势必很好 nghe rất lạ tai."),
         "Mẹo nhớ: 势必 có chữ thế, tức là xu thế, chiều hướng; nó nhìn vào xu thế để dự đoán một kết cục, mà kết cục ấy thường là xấu."])

add("compare", section="Phân biệt từ 词语辨析", title="Phân biệt 势必 và 一定 (2): thái độ và tính từ",
    cols=[{"head": "势必",
           "lines": ["Không có cách dùng biểu thị thái độ kiên quyết",
                     "Không dùng làm tính từ",
                     "Sai: 要想学好汉语，势必得努力。"]},
          {"head": "一定",
           "lines": ["Biểu thị thái độ kiên quyết, thường đứng trước động từ hoặc trợ động từ 要, 得",
                     "Đúng: 要想学好汉语，一定得努力。",
                     "Làm tính từ: quy định, xác định; cố định, tất nhiên",
                     "Đúng: 要按一定的程序进行操作。"]}],
    say=[F(1, "Điểm khác thứ hai: 一定 còn biểu thị thái độ kiên quyết, thường đứng trước động từ, hoặc trước trợ động từ như 要. Ví dụ: 要想学好汉语，一定得努力。 Muốn học giỏi tiếng Trung thì nhất định phải cố gắng."),
         F(0, "势必 không có cách dùng này. Không nói 要想学好汉语，势必得努力."),
         F(1, "Điểm khác thứ ba: 一定 còn có thể làm tính từ, nghĩa là được quy định, xác định, hoặc cố định không đổi, tất nhiên. Ví dụ: 要按一定的程序进行操作。 Phải thao tác theo quy trình nhất định."),
         F(1, "Ví dụ khác của sách: 文章的难易跟篇幅的长短并没有一定的关系。 Độ khó dễ của bài văn không có mối quan hệ tất nhiên nào với độ dài ngắn của nó."),
         F(0, "势必 chỉ là phó từ, không làm tính từ được. Tóm lại: 势必 chỉ dùng để dự đoán kết quả, thường là xấu; còn 一定 dùng rộng hơn nhiều: dự đoán, thể hiện quyết tâm, và làm tính từ.")])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: chọn 势必 hay 一定?", reveal=True, size=36,
    items=["(1) 人人都不遵守交通规则，______会导致交通混乱。",
           "Đáp án: 势必 (dự đoán kết quả bất lợi; dùng 一定 cũng được)",
           "(2) 这件事就交给你了，你______要把它办好。",
           "Đáp án: 一定 – thái độ kiên quyết, trước 要",
           "(3) 他学习这么好，______能考上名牌大学。",
           "Đáp án: 一定 – kết quả tốt, không dùng 势必",
           "(4) 他没日没夜地工作，吃饭睡觉都没有______的时间。",
           "Đáp án: 一定 – tính từ: cố định"],
    say=[F(0, "Bây giờ chúng ta làm thử phần 做一做 của sách: chọn 势必 hay 一定. Câu một: 人人都不遵守交通规则，什么会导致交通混乱。 Ai cũng không tuân thủ luật giao thông thì tất sẽ dẫn đến giao thông hỗn loạn. Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: 势必。 人人都不遵守交通规则，势必会导致交通混乱。 Đây là dự đoán dựa trên xu thế, kết quả bất lợi, nên 势必 là hay nhất. Dùng 一定 cũng không sai."),
         F(2, "Câu hai: 这件事就交给你了，你什么要把它办好。 Việc này giao cho cậu đấy, cậu phải làm cho tốt."),
         F(3, "Đáp án: 一定。 你一定要把它办好。 Đây là thái độ kiên quyết, đứng trước 要, chỉ 一定 mới dùng được."),
         F(4, "Câu ba: 他学习这么好，什么能考上名牌大学。 Cậu ấy học giỏi như vậy, chắc chắn sẽ đỗ trường đại học danh tiếng."),
         F(5, "Đáp án: 一定。 Kết quả là điều tốt, nên không dùng 势必."),
         F(6, "Câu bốn: 他没日没夜地工作，吃饭睡觉都没有什么的时间。 Anh ấy làm việc ngày đêm, ăn ngủ cũng không có giờ giấc cố định."),
         F(7, "Đáp án: 一定。 没有一定的时间, không có thời gian cố định. Ở đây 一定 là tính từ làm định ngữ, 势必 không làm được.")])

# ======================= MỞ RỘNG: CÂU SAI DO LẪN LỘN CẤU TRÚC =======================
add("bullets", chapter="Mở rộng: câu lẫn lộn cấu trúc", section="Mở rộng 扩展", title="Câu sai: lẫn lộn cấu trúc câu (句式杂糅)", size=38,
    items=["Cùng một nội dung có thể diễn đạt theo nhiều cách khác nhau",
           "Khi nói hoặc viết, nếu nhào trộn hai cách nói vào một câu → câu sai lẫn lộn cấu trúc",
           "## Nguyên nhân chính",
           "Lẫn lộn hai kiểu câu (句式混用)",
           "Lẫn lộn hai cấu trúc (结构混用)"],
    say=["Bây giờ chúng ta sang phần mở rộng của sách. Quyển Thượng không có mục tu từ riêng, thay vào đó là kỹ năng nhận biết câu sai. Hôm nay là một kiểu câu sai rất hay gặp: lẫn lộn cấu trúc câu, tiếng Trung gọi là 句式杂糅.",
         F(0, "Cùng một nội dung, vốn dĩ có thể diễn đạt theo nhiều cách khác nhau."),
         F(1, "Nhưng có khi lúc nói hoặc viết, người ta lại nhào trộn hai cách nói vào cùng một câu, tạo thành câu sai do lẫn lộn kiểu câu hoặc cấu trúc. 杂糅 nghĩa là trộn lẫn vào nhau."),
         F(2, "Sách nêu hai nguyên nhân chính."),
         F(3, "Thứ nhất, lẫn lộn hai kiểu câu, tiếng Trung là 句式混用."),
         F(4, "Thứ hai, lẫn lộn hai cấu trúc, tiếng Trung là 结构混用. Cách sửa thường rất đơn giản: chọn một trong hai cách nói, bỏ cách còn lại. Chúng ta cùng xem năm ví dụ của sách.")])

add("bullets", section="Mở rộng 扩展", title="Ví dụ câu sai lẫn lộn cấu trúc (1)", size=34,
    items=["## (1) Lẫn lộn ngữ khí trần thuật và nghi vấn",
           "Sai: 我发觉，为什么只要你用功成绩就能提高了？",
           "Sửa: 我发觉只要你用功成绩就能提高。",
           "## (2) Câu đã hoàn chỉnh lại bị dùng làm chủ ngữ",
           "Sai: 做了演员以后，她一方面努力提高自己的专业水平，一方面努力提高自己的文化修养也是很重要的。",
           "Sửa: 做了演员以后，她一方面努力提高自己的专业水平，一方面努力提高自己的文化修养。"],
    say=[F(0, "Ví dụ một: lẫn lộn ngữ khí."),
         F(1, "Câu sai: 我发觉，为什么只要你用功成绩就能提高了？ Tôi phát hiện ra, tại sao chỉ cần bạn chăm chỉ là thành tích có thể nâng cao?"),
         F(2, "Tân ngữ đứng sau 发觉 phải dùng ngữ khí trần thuật, nhưng câu lại dùng ngữ khí nghi vấn, tức là trộn hai câu vào nhau. Sửa: 我发觉只要你用功成绩就能提高。"),
         F(3, "Ví dụ hai: một câu đã hoàn chỉnh lại bị đem làm chủ ngữ cho một vị ngữ khác."),
         F(4, "Câu sai: 做了演员以后，她一方面努力提高自己的专业水平，一方面努力提高自己的文化修养也是很重要的。 Sau khi làm diễn viên, cô ấy một mặt cố gắng nâng cao trình độ chuyên môn, một mặt cố gắng nâng cao trình độ văn hóa, cũng là rất quan trọng."),
         F(5, "Phần từ 她 đến 文化修养 đã là một câu hoàn chỉnh, nhưng lại bị đem làm chủ ngữ của 也是很重要的. Sửa: bỏ 也是很重要的 đi là xong.")])

add("bullets", section="Mở rộng 扩展", title="Ví dụ câu sai lẫn lộn cấu trúc (2)", size=32,
    items=["## (3) 分为……部分 lẫn với 由……组成",
           "Sai: 展览分为地震突袭、抗震救灾、灾后重建、美好家园四部分组成，……",
           "Sửa: 展览分为……四部分 / 展览由……四部分组成",
           "## (4) 受……欢迎 lẫn với 为……所+động từ",
           "Sai: 《消费者权益保护法》深受广大消费者所欢迎，……",
           "Sửa: ……深受广大消费者欢迎 / ……为广大消费者所欢迎",
           "## (5) Câu hoàn chỉnh lẫn với câu kiêm ngữ có 使",
           "Sai: ……黄曲霉素能够使人致癌。 → Sửa: ……黄曲霉素能够致癌。"],
    say=[F(0, "Ví dụ ba: lẫn lộn hai cấu trúc 分为什么部分 và 由什么组成."),
         F(1, "Câu sai: 展览分为地震突袭、抗震救灾、灾后重建、美好家园四部分组成，充分显示了灾区人民不怕困难、自强不息的精神。 Triển lãm chia thành bốn phần: động đất ập đến, chống động đất cứu nạn, tái thiết sau thảm họa, và quê hương tươi đẹp, thể hiện đầy đủ tinh thần không sợ khó khăn, tự cường không ngừng của người dân vùng thiên tai."),
         F(2, "Hai cách nói bị trộn vào nhau. Sửa theo một trong hai cách: 展览分为四部分, triển lãm chia thành bốn phần; hoặc 展览由四部分组成, triển lãm gồm bốn phần."),
         F(3, "Ví dụ bốn: lẫn lộn 受欢迎 và cấu trúc bị động văn viết có chữ 所."),
         F(4, "Câu sai: 消费者权益保护法深受广大消费者所欢迎，因为它使消费者的权益得到最大限度的保护。 Luật Bảo vệ quyền lợi người tiêu dùng rất được người tiêu dùng hoan nghênh, vì nó giúp quyền lợi của họ được bảo vệ ở mức tối đa. Sửa: 深受广大消费者欢迎, hoặc 为广大消费者所欢迎."),
         F(5, "Ví dụ năm: 花生在潮湿条件下储存，会生长黄曲霉素，黄曲霉素能够使人致癌。 Lạc bảo quản trong điều kiện ẩm sẽ sinh ra độc tố aflatoxin, chất này có thể gây ung thư cho người."),
         F(6, "黄曲霉素能够致癌 đã là câu hoàn chỉnh, nhưng lại bị trộn với câu kiêm ngữ dùng 使. Sửa: bỏ hai chữ 使人, thành 黄曲霉素能够致癌。")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chỉ ra lỗi và sửa lại (1)", reveal=True, size=32,
    items=["(1) 这次参加比赛的，除了本校的学生，还有来自各国的留学生也参加了比赛。",
           "Đáp án: Hai kiểu câu trộn lẫn → ……还有来自各国的留学生。 (bỏ 也参加了比赛)",
           "(2) 即使我所做的哪怕只给大家带来一点点的快乐，我也会很高兴。",
           "Đáp án: 即使 và 哪怕 trùng nhau → 我所做的哪怕只给大家带来一点点的快乐，我也会很高兴。",
           "(3) 父亲一直想让儿子学门手艺，他认为只要身怀绝技，一辈子才有了铁饭碗。",
           "Đáp án: 只要……就 lẫn với 只有……才 → 只要身怀绝技，一辈子就有了铁饭碗。"],
    say=[F(0, "Luyện tập: chỉ ra lỗi của các câu sau và đề xuất cách sửa. Câu một: 这次参加比赛的，除了本校的学生，还有来自各国的留学生也参加了比赛。 Những người tham gia cuộc thi lần này, ngoài học sinh của trường, còn có lưu học sinh các nước cũng tham gia cuộc thi. Câu này sai ở đâu? Các bạn tạm dừng và suy nghĩ nhé."),
         F(1, "Đáp án: câu trộn hai cách nói: 参加比赛的，除了本校的学生，还有留学生, và 除了本校的学生，留学生也参加了比赛. Sửa: 这次参加比赛的，除了本校的学生，还有来自各国的留学生。 Hoặc: 这次除了本校的学生，来自各国的留学生也参加了比赛。"),
         F(2, "Câu hai: 即使我所做的哪怕只给大家带来一点点的快乐，我也会很高兴。 Dù những việc tôi làm dù chỉ mang lại cho mọi người một chút niềm vui, tôi cũng sẽ rất vui."),
         F(3, "Đáp án: 即使 và 哪怕 cùng nghĩa là dù cho, dùng cả hai là thừa và trộn lẫn. Bỏ một trong hai: 我所做的哪怕只给大家带来一点点的快乐，我也会很高兴。"),
         F(4, "Câu ba: 父亲一直想让儿子学门手艺，他认为只要身怀绝技，一辈子才有了铁饭碗。 Cha luôn muốn con trai học một nghề, ông cho rằng chỉ cần có tay nghề giỏi thì cả đời mới có bát cơm sắt, tức là việc làm ổn định."),
         F(5, "Đáp án: câu trộn hai cặp liên từ 只要……就 và 只有……才. Sửa: 只要身怀绝技，一辈子就有了铁饭碗。 Hoặc: 只有身怀绝技，一辈子才有铁饭碗。")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chỉ ra lỗi và sửa lại (2)", reveal=True, size=34,
    items=["(4) 她为人的正直、诚恳，做事的严谨、认真，在我心里给我留下了深刻的印象。",
           "Đáp án: 在我心里 lẫn với 给我 → ……在我心里留下了深刻的印象 / ……给我留下了深刻的印象。",
           "(5) 钱虽然不多，却是我用汗水换来的，拿在手里似乎比从父母那里得到的重得多了。",
           "Đáp án: 重得多 lẫn với 重多了 → ……比从父母那里得到的重得多 / 重多了。"],
    say=[F(0, "Câu bốn: 她为人的正直、诚恳，做事的严谨、认真，在我心里给我留下了深刻的印象。 Sự chính trực, chân thành trong cách đối nhân xử thế, sự nghiêm túc, cẩn thận trong công việc của cô ấy đã để lại trong lòng tôi cho tôi ấn tượng sâu sắc."),
         F(1, "Đáp án: hai cách nói 在我心里留下了深刻的印象 và 给我留下了深刻的印象 bị trộn vào nhau. Chọn một: hoặc 在我心里留下了深刻的印象, hoặc 给我留下了深刻的印象."),
         F(2, "Câu năm: 钱虽然不多，却是我用汗水换来的，拿在手里似乎比从父母那里得到的重得多了。 Tiền tuy không nhiều, nhưng là do mồ hôi tôi đổi lấy, cầm trong tay dường như nặng hơn nhiều so với tiền nhận từ bố mẹ."),
         F(3, "Đáp án: hai cách nói 重得多 và 重多了 bị trộn thành 重得多了. Sửa: 比从父母那里得到的重得多, hoặc 重多了. Mẹo: khi gặp câu dài, hãy thử tách thành hai câu, nếu mỗi phần đều đứng được một mình thì rất có thể đó là câu lẫn lộn cấu trúc.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ có dấu chấm", size=40,
    items=["跳跃 (跳) → 跳舞 · 跳高 · 跳远 · 跳水",
           "瞄准 (准) → 准确 · 标准 · 准备 · 准时",
           "视线 (线) → 光线 · 路线 · 电线 · 热线",
           "周边 (周) → 周围 · 周末 · 四周 · 周到",
           "迟钝 (迟) → 迟到 · 推迟 · 迟早 · 迟疑"],
    say=["Phần luyện tập. Bài tập một: mô phỏng ví dụ, viết thêm các từ có chứa chữ được đánh dấu chấm.",
         F(0, "Ví dụ mẫu: 跳跃, chữ được đánh dấu là chữ đầu, nghĩa là nhảy. Ta có 跳舞，跳高，跳远，跳水. Tức là nhảy múa, nhảy cao, nhảy xa, và nhảy cầu."),
         F(1, "瞄准, chữ được đánh dấu là chữ thứ hai, nghĩa là chuẩn, đúng. Ta có 准确，标准，准备，准时. Tức là chính xác, tiêu chuẩn, chuẩn bị, và đúng giờ."),
         F(2, "视线, chữ được đánh dấu là chữ thứ hai, nghĩa là đường, sợi. Ta có 光线，路线，电线，热线. Tức là tia sáng, lộ trình, dây điện, và đường dây nóng."),
         F(3, "周边, chữ được đánh dấu là chữ đầu, nghĩa là vòng quanh. Ta có 周围，周末，四周，周到. Tức là xung quanh, cuối tuần, bốn phía, và chu đáo."),
         F(4, "迟钝, chữ được đánh dấu là chữ đầu, nghĩa là chậm, muộn. Ta có 迟到，推迟，迟早，迟疑. Tức là đến muộn, hoãn lại, sớm muộn gì, và chần chừ.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Hoàn thành câu bằng từ cho sẵn (1)", reveal=True, size=36,
    items=["(1) 他______，但他的计划被我识破了。（企图）",
           "Đáp án: 他企图骗走我的钱，但他的计划被我识破了。",
           "(2) 听说有人找我，______？（纳闷儿）",
           "Đáp án: 听说有人找我，我很纳闷儿：会是谁呢？",
           "(3) 我非常喜欢运动，______等等。（比方说）",
           "Đáp án: 我非常喜欢运动，比方说跑步、游泳、打篮球等等。"],
    say=[F(0, "Bài tập hai: dùng từ cho sẵn để hoàn thành câu. Câu một, dùng 企图: 他什么，但他的计划被我识破了。 Hắn làm gì đó, nhưng kế hoạch của hắn đã bị tôi nhìn thấu. Các bạn tạm dừng và thử nhé."),
         F(1, "Đáp án gợi ý: 他企图骗走我的钱，但他的计划被我识破了。 Hắn định lừa lấy tiền của tôi, nhưng kế hoạch của hắn đã bị tôi nhìn thấu. 企图 hợp với việc xấu như thế này."),
         F(2, "Câu hai, dùng 纳闷儿: 听说有人找我，什么？ Nghe nói có người tìm tôi, thế nào?"),
         F(3, "Đáp án gợi ý: 听说有人找我，我很纳闷儿：会是谁呢？ Nghe nói có người tìm, tôi rất thắc mắc: ai vậy nhỉ?"),
         F(4, "Câu ba, dùng 比方说: 我非常喜欢运动，什么等等。 Tôi rất thích thể thao, chẳng hạn như những gì?"),
         F(5, "Đáp án gợi ý: 我非常喜欢运动，比方说跑步、游泳、打篮球等等。 Tôi rất thích thể thao, chẳng hạn chạy bộ, bơi lội, chơi bóng rổ, vân vân.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Hoàn thành câu bằng từ cho sẵn (2)", reveal=True, size=36,
    items=["(4) 如果你想洗衣服，我这里有台旧洗衣机，你______。（姑且）",
           "Đáp án: ……你姑且先用着吧。",
           "(5) 不好好发展经济，______。（势必）",
           "Đáp án: 不好好发展经济，势必会影响人们的生活水平。",
           "(6) 看到家乡的巨大变化，______。（感慨）",
           "Đáp án: 看到家乡的巨大变化，他不禁感慨万千。"],
    say=[F(0, "Câu bốn, dùng 姑且: 如果你想洗衣服，我这里有台旧洗衣机，你什么。 Nếu cậu muốn giặt quần áo, chỗ tớ có cái máy giặt cũ, cậu làm sao?"),
         F(1, "Đáp án gợi ý: 你姑且先用着吧。 Cậu cứ tạm dùng đỡ đi. Máy cũ không tốt lắm, nhưng tạm dùng được, đúng ý miễn cưỡng của 姑且."),
         F(2, "Câu năm, dùng 势必: 不好好发展经济，什么。 Không phát triển kinh tế cho tốt thì sao?"),
         F(3, "Đáp án gợi ý: 不好好发展经济，势必会影响人们的生活水平。 Không phát triển kinh tế cho tốt thì ắt sẽ ảnh hưởng đến mức sống của người dân. Kết quả bất lợi, rất hợp với 势必."),
         F(4, "Câu sáu, dùng 感慨: 看到家乡的巨大变化，什么。 Nhìn thấy sự thay đổi to lớn của quê hương thì sao?"),
         F(5, "Đáp án gợi ý: 看到家乡的巨大变化，他不禁感慨万千。 Thấy quê hương đổi thay to lớn, anh ấy không khỏi trăm mối bồi hồi.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống", reveal=True, size=32,
    items=["## (1) 东张西望 · 确切 · 周边 · 企图 · 动手",
           "小偷在___偷东西时，总是先___，看看___有没有人注意自己，当___知道没人注意时，他们再___偷。",
           "Đáp án: 企图 · 东张西望 · 周边 · 确切 · 动手",
           "## (2) 无能为力 · 本身 · 迟钝 · 迟缓 · 新陈代谢",
           "人类跟其他动物一样，随着年龄的增长，反应越来越___，行动越来越___。同样的，我们___的___也逐渐变慢。年轻时，你轻而易举就能做到的动作，到了老年却___了。",
           "Đáp án: 迟钝 · 迟缓 · 本身 · 新陈代谢 · 无能为力"],
    say=[F(0, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn một có năm từ: 东张西望，确切，周边，企图，动手."),
         F(1, "小偷在什么偷东西时，总是先什么，看看什么有没有人注意自己，当什么知道没人注意时，他们再什么偷。如果在公共场合看到这样可疑的人，一定要多加小心，注意保管好自己的财物。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 小偷在企图偷东西时，总是先东张西望，看看周边有没有人注意自己，当确切知道没人注意时，他们再动手偷。 Khi kẻ trộm định trộm đồ, chúng luôn nhìn quanh quất trước, xem xung quanh có ai để ý không, khi biết chắc không ai để ý thì mới ra tay. Gặp người khả nghi như vậy ở nơi công cộng, nhất định phải cẩn thận, giữ kỹ tài sản."),
         F(3, "Đoạn hai có năm từ: 无能为力，本身，迟钝，迟缓，新陈代谢."),
         F(4, "人类跟其他动物一样，随着年龄的增长，反应越来越什么，行动越来越什么。同样的，我们什么的什么也逐渐变慢。年轻时，你轻而易举就能做到的动作，到了老年却什么了。 Các bạn điền thử nhé."),
         F(5, "Đáp án: 反应越来越迟钝，行动越来越迟缓，我们本身的新陈代谢也逐渐变慢，到了老年却无能为力了。 Con người cũng như các loài khác, tuổi càng cao, phản ứng càng chậm, hành động càng chậm chạp; quá trình trao đổi chất của chính chúng ta cũng chậm dần. Những động tác thời trẻ làm dễ như trở bàn tay, về già lại đành bất lực. Đoạn này dùng lại rất nhiều ý của bài khóa.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 4: Đọc đoạn văn, mô phỏng đặt câu", reveal=True, size=32,
    items=["(1) 有科学家推论，物种的CFF与其本身的体重和新陈代谢速率有关。体型越小，……越短；……越高，说明……",
           "Đáp án: 有科学家推论，身高与遗传有关。父母的个子越高，孩子的个子越高，这说明身高是会遗传的。",
           "(2) 虽然它们没有博大精深的思想，不能进行深奥的思考，对强大的对手无能为力，但对外部环境能迅速做出判断，使它们有了更多的生存机会……",
           "Đáp án: 虽然他没有很高的学历，不能做复杂的研究，对专业问题无能为力，但他工作非常认真，使他有了很多忠实的客户。"],
    say=[F(0, "Bài tập bốn: đọc đoạn văn rồi mô phỏng đặt câu. Mẫu một lấy từ bài khóa, dùng các khung 与……有关, 越……越……, và 说明. Sách cho khung: 有科学家推论，身高与什么有关。父母的什么越什么，孩子的什么越什么，这说明什么是会遗传的。"),
         F(1, "Đáp án gợi ý: 有科学家推论，身高与遗传有关。父母的个子越高，孩子的个子越高，这说明身高是会遗传的。 Có nhà khoa học suy luận rằng chiều cao có liên quan đến di truyền. Bố mẹ càng cao thì con càng cao, điều này cho thấy chiều cao có tính di truyền."),
         F(2, "Mẫu hai dùng khung 虽然没有……，不能……，对……无能为力，但……，使……有了……. Sách cho khung: 虽然他没有什么，不能什么，对什么无能为力，但什么，使什么有了什么。"),
         F(3, "Đáp án gợi ý: 虽然他没有很高的学历，不能做复杂的研究，对专业问题无能为力，但他工作非常认真，使他有了很多忠实的客户。 Tuy anh ấy không có bằng cấp cao, không làm được nghiên cứu phức tạp, bất lực trước các vấn đề chuyên môn, nhưng anh làm việc rất tận tâm, nhờ vậy có rất nhiều khách hàng trung thành. Các bạn hãy tự đặt thêm câu của mình nhé.")])

add("bullets", section="Luyện tập 练习", title="Mở rộng 扩展: nghĩa của yếu tố cấu tạo từ", size=34,
    items=["导向 dẫn hướng: 导 dẫn dắt + 向 phương hướng · 搏斗 vật lộn: đánh nhau + đánh nhau",
           "苍白 tái nhợt: 苍 màu xám trắng + 白 trắng · 陈列 trưng bày: 陈 đặt để + 列 xếp hàng",
           "腐蚀 ăn mòn: 腐 hỏng + 蚀 tổn hại · 精华 tinh hoa: 精 hoàn mỹ + 华 tốt đẹp nhất",
           "和解 hòa giải: bỏ mâu thuẫn + xóa bỏ · 保养 bảo dưỡng: 保 bảo vệ + 养 nghỉ ngơi, điều dưỡng",
           "腐烂 thối rữa: 腐 hỏng + 烂 vi sinh vật phá hủy · 表决 biểu quyết: 表 bày tỏ + 决 quyết định",
           "反思 suy ngẫm lại: 反 quay lại + 思 suy nghĩ · 罢工 đình công: 罢 dừng + 工 công việc"],
    say=["Phần mở rộng thứ hai của sách là từ vựng: làm quen với nghĩa của từng yếu tố cấu tạo trong mười hai từ. Hiểu nghĩa từng chữ, các bạn sẽ đoán nghĩa từ mới rất nhanh.",
         F(0, "导向: chữ đầu là dẫn dắt, chữ sau là phương hướng, gộp lại là định hướng, dẫn hướng. 搏斗: cả hai chữ đều nghĩa là đánh nhau, gộp lại là vật lộn, đánh giáp lá cà."),
         F(1, "苍白: chữ đầu là màu xám trắng, chữ sau là trắng, gộp lại là tái nhợt. 陈列: chữ đầu là đặt để, chữ sau là sắp xếp, gộp lại là trưng bày."),
         F(2, "腐蚀: chữ đầu là hư hỏng, chữ sau là tổn hại, gộp lại là ăn mòn. 精华: chữ đầu là hoàn mỹ, chữ sau là tốt đẹp nhất, gộp lại là tinh hoa."),
         F(3, "和解: chữ đầu là từ bỏ mâu thuẫn, chữ sau là xóa bỏ, gộp lại là hòa giải. 保养: chữ đầu là bảo vệ, chữ sau là nghỉ ngơi, điều dưỡng, gộp lại là bảo dưỡng, giữ gìn."),
         F(4, "腐烂: chữ đầu là hư hỏng, chữ sau là bị vi sinh vật phát triển làm hỏng, gộp lại là thối rữa. 表决: chữ đầu là bày tỏ, chữ sau là quyết định, gộp lại là biểu quyết."),
         F(5, "反思: chữ đầu là quay lại, chữ sau là suy nghĩ, gộp lại là suy ngẫm lại, tự kiểm điểm. 罢工: chữ đầu là dừng lại, chữ sau là công việc, gộp lại là đình công. Các bạn thấy không, âm Hán Việt giúp chúng ta nhớ những từ này rất dễ.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 17", size=36,
    items=["Từ vựng trọng tâm: 东张西望 · 企图 · 纳闷儿 · 确切 · 迟钝 · 迟缓 · 姑且 · 推论 · 势必 · 无能为力 · 实惠 · 焦急",
           "Ngữ pháp: 东A西B (chỗ này… chỗ kia…) · 中 zhòng (trúng; bị, mắc) · 姑且 (tạm thời, miễn cưỡng)",
           "Phân biệt: 势必 (dự đoán, kết quả thường bất lợi) ≠ 一定 (dự đoán, quyết tâm, tính từ)",
           "Mở rộng: câu sai do lẫn lộn cấu trúc (句式杂糅)",
           "## Bài tập về nhà (运用)",
           "Tham khảo bài tập 5, viết tóm tắt bài khóa thành một đoạn văn khoảng 400 chữ"],
    say=["Chúng ta cùng tổng kết bài mười bảy.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 东张西望，企图，纳闷儿，确切，迟钝，迟缓，姑且，推论，势必，无能为力，实惠，焦急. Và đừng quên những từ dễ nhầm như 颤抖，迟缓，动手."),
         F(1, "Về ngữ pháp: mẫu 东A西B biểu thị chỗ này… chỗ kia…, như 东张西望，东拉西扯. Động từ trúng đọc thanh bốn, có nghĩa là trúng đích, như 打中，猜中, và nghĩa là bị, mắc, như 中暑，中毒. 姑且 là phó từ, nghĩa là tạm thời, mang ý miễn cưỡng, nhân nhượng."),
         F(2, "Về phân biệt từ: 势必 chỉ dùng để dự đoán kết quả theo xu thế, thường là bất lợi; còn 一定 vừa dự đoán, vừa biểu thị quyết tâm, lại còn làm được tính từ."),
         F(3, "Về phần mở rộng: câu sai do lẫn lộn cấu trúc, như trộn hai ngữ khí, trộn 分为 với 由……组成, trộn 受欢迎 với cấu trúc có chữ 所, hay trộn câu hoàn chỉnh với câu kiêm ngữ. Cách sửa là giữ lại một cách nói."),
         F(5, "Bài tập về nhà, theo phần vận dụng của sách: bài khóa kể về một hiện tượng tự nhiên rất thú vị, vì sao con người đập ruồi rất khó, mà mèo con lại bắt ruồi rất dễ. Điều này chủ yếu là do chỉ số CFF. Hãy tham khảo bài tập năm, viết tóm tắt bài khóa thành một đoạn văn khoảng bốn trăm chữ. Nhớ thử dùng 姑且，势必，确切地说 trong bài viết nhé."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Lần tới đập ruồi trượt, các bạn đừng buồn, chỉ là trong mắt nó, chúng ta quá chậm mà thôi. Hẹn gặp lại các bạn ở bài mười tám: 神奇的丝瓜, Quả mướp thần kỳ. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Thượng) – Bài 17: 小动物眼中的慢世界 (Thế giới chậm trong mắt động vật nhỏ)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"盛着": "成着",              # chéngzhe
                    "盛了一碗饭": "成了一碗饭",  # chéng
                    "纳闷": "纳焖",              # nàmèn
                    "颤抖": "忏抖",              # chàndǒu
                    "间隔": "见隔",              # jiàngé
                    "笨拙": "笨捉",              # bènzhuō
                    "打不中": "打不众",          # dǎ bu zhòng
                    "猜中": "猜众",              # cāizhòng
                    "打中": "打众",              # dǎzhòng
                    "击中": "击众",              # jīzhòng
                    "选中": "选众",              # xuǎnzhòng
                    "看中": "看众",              # kànzhòng
                    "中暑": "众暑",              # zhòngshǔ
                    "中毒": "众毒",              # zhòngdú
                    "为六十": "维六十",          # wéi
                    "为八十": "维八十",          # wéi
                    "无能为力": "无能维力",      # wúnéngwéilì
                    "更为": "更维",              # gèngwéi
                    "好动": "号动",              # hàodòng
                    "为人的": "维人的",          # wéirén
                    "分为": "分维",              # fēnwéi
                    "为广大": "维广大",          # wéi
                    "增长": "增涨",              # zēngzhǎng
                    "重建": "虫建",              # chóngjiàn
                    "曲霉": "屈霉",              # qūméi
                    "没事干": "没事赣",          # gàn
                    "搏斗": "搏豆",              # bódòu
                    "速率": "速律",              # sùlǜ
                    "频率": "频律",              # pínlǜ
                    "心率": "心律",              # xīnlǜ
                    "比率": "比律",              # bǐlǜ
                    "概率": "概律",              # gàilǜ
                    "汇率": "汇律",              # huìlǜ
                    "利率": "利律"},             # lìlǜ
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai17.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
