#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Thượng) – Bài 14 «背着电饭锅拍北极». Chạy để sinh bai14.json."""
import json
import os

TAG = "HSK 6 (Thượng) · Bài 14 · 背着电饭锅拍北极"
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
    zh="背着电饭锅拍北极", py="Bēizhe diànfànguō pāi Běijí",
    vi="Bài 14: Vác nồi cơm điện đi chụp ảnh Bắc Cực",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Thượng.",
         "Hôm nay chúng ta học bài mười bốn: 背着电饭锅拍北极。 Nghĩa là: Vác nồi cơm điện đi chụp ảnh Bắc Cực.",
         "Đây là bài thứ hai của Chủ đề bốn, 走遍天下, Đi khắp thiên hạ. Bài khóa kể về ông Vương Kiến Nam, một người làm báo thành đạt. Đang ở đỉnh cao sự nghiệp, ông bất ngờ từ chức, rồi cùng vợ đi Bắc Cực mười bảy lần, mang theo nồi cơm, mì sợi, sống rất tiết kiệm, chỉ để chụp lại đời sống đang thay đổi của người Inuit.",
         "Qua bài này, chúng ta cùng suy nghĩ một câu hỏi lớn: rốt cuộc chúng ta sống vì điều gì?"])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài khóa: hành trình chụp ảnh Bắc Cực của Vương Kiến Nam",
           "Nắm vững 50 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: lượng từ lặp lại (一拨拨), động từ 难以, liên từ 免得",
           "Phân biệt hai động từ 鼓动 và 鼓励",
           "Kỹ năng: kể trải nghiệm theo trình tự thời gian (先是……不久……再后来……)",
           "Mở rộng: 16 cặp từ trái nghĩa"],
    say=["Bài học hôm nay có sáu mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa: vì sao Vương Kiến Nam rời bỏ sự nghiệp, và hành trình chụp ảnh Bắc Cực của vợ chồng ông diễn ra như thế nào."),
         F(1, "Thứ hai, nắm vững năm mươi từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học ba điểm ngữ pháp: lượng từ lặp lại như 一拨拨; động từ 难以, nghĩa là khó mà; và liên từ 免得, nghĩa là để tránh, kẻo."),
         F(3, "Thứ tư, phân biệt hai động từ rất dễ nhầm: 鼓动 và 鼓励."),
         F(4, "Thứ năm, một kỹ năng viết rất thực dụng: kể lại một trải nghiệm theo trình tự thời gian, với các từ nối như 先是，不久，再后来."),
         F(5, "Thứ sáu, phần mở rộng: làm quen với mười sáu cặp từ trái nghĩa."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Câu hỏi khởi động: Bạn biết gì về Bắc Cực?", size=40,
    items=["你去过北极吗？你印象中北极人的生活是什么样的？",
           "白令海峡 eo biển Bering · 北极熊 gấu Bắc Cực · 雪屋 nhà tuyết",
           "北极圈 vòng Bắc Cực · 因纽特人 người Inuit · 打猎 săn bắn"],
    say=["Chúng ta bắt đầu bằng phần khởi động.",
         F(0, "Câu hỏi của sách: 你去过北极吗？你印象中北极人的生活是什么样的？ Bạn đã từng đến Bắc Cực chưa? Trong ấn tượng của bạn, cuộc sống của người Bắc Cực như thế nào? Sách cho sáu bức tranh để chúng ta tìm hiểu."),
         F(1, "Tranh một là 白令海峡, eo biển Bering, nằm giữa châu Á và châu Mỹ. Tranh hai là 北极熊, gấu Bắc Cực, tức là gấu trắng. Tranh ba là 雪屋, nhà tuyết, ngôi nhà tròn làm bằng những khối băng tuyết."),
         F(2, "Tranh bốn là 北极圈, vòng Bắc Cực. Tranh năm là 因纽特人, người Inuit, cư dân bản địa của vùng Bắc Cực. Tranh sáu là 打猎, săn bắn."),
         "Có lẽ trong đầu nhiều bạn, người Bắc Cực vẫn sống trong nhà tuyết và đi săn bằng giáo. Nhưng Bắc Cực ngày nay có thật như vậy không? Bài khóa sẽ cho chúng ta một câu trả lời rất bất ngờ."])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 论 và 访", size=38,
    items=["## 论 (luận): bàn bạc, lý lẽ",
           "评论 bình luận · 言论 ngôn luận · 谈论 bàn tán · 议论 bàn luận · 讨论 thảo luận · 辩论 tranh luận",
           "结论 kết luận · 理论 lý luận · 争论 tranh cãi · 论述 luận giải · 论文 luận văn",
           "## 访 (phỏng): thăm hỏi, tìm hiểu",
           "访问 thăm viếng · 访友 thăm bạn · 拜访 đến thăm · 出访 thăm nước ngoài · 回访 thăm đáp lễ",
           "来访 đến thăm · 探访 thăm hỏi · 走访 đến tận nơi thăm · 家访 thăm nhà học sinh"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo, rất có lợi cho người Việt vì hầu hết các chữ đều có âm Hán Việt quen thuộc.",
         F(0, "Nhóm thứ nhất có chữ luận, như trong từ 评论. Chữ này nghĩa là bàn bạc, phân tích lý lẽ."),
         F(1, "评论，言论，谈论，议论，讨论，辩论。 Tức là: bình luận, ngôn luận, bàn tán, bàn luận, thảo luận, và tranh luận. Trong bài khóa, Vương Kiến Nam từng làm 新闻评论员, nhà bình luận tin tức."),
         F(2, "结论，理论，争论，论述，论文。 Tức là: kết luận, lý luận, tranh cãi, luận giải, và luận văn."),
         F(3, "Nhóm thứ hai có chữ 访, Hán Việt là phỏng, nghĩa là đến thăm, hỏi han, tìm hiểu."),
         F(4, "访问，访友，拜访，出访，回访。 Tức là: thăm viếng, thăm bạn, đến thăm, đi thăm nước ngoài, và thăm đáp lễ. Trong bài có câu 每天都会有一拨拨同行前来考察访问."),
         F(5, "来访，探访，走访，家访。 Tức là: đến thăm, thăm hỏi, đến tận nơi thăm, và giáo viên đến thăm nhà học sinh.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 差 (chā) và 惊", size=38,
    items=["## 差 (sai), đọc chā: chênh lệch, khác nhau",
           "差别 khác biệt · 差距 khoảng cách · 差异 sự khác nhau · 差价 chênh lệch giá",
           "反差 tương phản · 色差 chênh lệch màu · 温差 chênh lệch nhiệt độ · 时差 lệch múi giờ",
           "## 惊 (kinh): sợ hãi, ngạc nhiên",
           "惊奇 kinh ngạc · 惊动 kinh động · 惊喜 vui bất ngờ · 惊慌 hoảng hốt · 惊吓 hoảng sợ · 惊叫 kêu thất thanh",
           "惊人 kinh người · 惊险 gay cấn · 惊心 kinh hãi · 吃惊 giật mình · 震惊 chấn động · 受惊 bị hoảng sợ"],
    say=[F(0, "Nhóm thứ ba là chữ sai trong từ 差别. Chữ này có nhiều cách đọc; trong nhóm này nó đọc thanh một, nghĩa là chênh lệch, khác nhau."),
         F(1, "差别，差距，差异，差价。 Tức là: sự khác biệt, khoảng cách, sự khác nhau, và chênh lệch giá. Từ 差别 có trong bài khóa: 生活差别竟是如此之大."),
         F(2, "反差，色差，温差，时差。 Tức là: sự tương phản, chênh lệch màu sắc, chênh lệch nhiệt độ, và lệch múi giờ. Ví dụ, bay từ Việt Nam sang châu Âu thì phải 倒时差, tức là làm quen lại với múi giờ mới."),
         F(3, "Nhóm cuối cùng có chữ 惊, Hán Việt là kinh, như trong kinh ngạc, kinh hãi."),
         F(4, "惊奇，惊动，惊喜，惊慌，惊吓，惊叫。 Tức là: kinh ngạc, làm kinh động, vui mừng bất ngờ, hoảng hốt, hoảng sợ, và kêu thất thanh. Bài khóa có câu 他们惊奇地发现, họ ngạc nhiên phát hiện ra."),
         F(5, "惊人，惊险，惊心，吃惊，震惊，受惊。 Tức là: kinh người, gay cấn nguy hiểm, kinh hãi, giật mình, chấn động, và bị hoảng sợ."),
         "Các bạn thấy không, chỉ cần nắm nghĩa của một chữ gốc, ta có thể đoán được nghĩa của cả một nhóm từ. Hãy áp dụng cách này khi học từ mới nhé."])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng)
V = [
    ("北极", "běijí", "bắc cực", "danh từ", "Bắc Cực", "北极熊生活在北极地区。", "Gấu Bắc Cực sống ở vùng Bắc Cực.",
     "Danh từ, nghĩa là Bắc Cực, vùng tận cùng phía bắc của Trái Đất. Chữ 极 ở đây là cực, điểm tận cùng. Trái nghĩa là 南极, Nam Cực. Từ này nằm ngay trong tên bài."),
    ("评论", "pínglùn", "bình luận", "động từ", "bình luận, nhận xét", "他经常在网上评论新闻。", "Anh ấy thường bình luận tin tức trên mạng.",
     "Động từ, nghĩa là bình luận, nhận xét; cũng dùng làm danh từ, lời bình luận. Trong bài có 新闻评论员, nhà bình luận tin tức; chữ 员 chỉ người làm một công việc."),
    ("典型", "diǎnxíng", "điển hình", "danh từ", "điển hình, gương điển hình", "他是努力学习的典型。", "Cậu ấy là tấm gương điển hình về chăm chỉ học tập.",
     "Danh từ, chỉ người hoặc sự việc tiêu biểu nhất, có tính đại diện; cũng làm tính từ: 典型的例子, ví dụ điển hình. Trong bài, tờ báo của Vương Kiến Nam trở thành 中国报业改革的典型."),
    ("考察", "kǎochá", "khảo sát", "động từ", "khảo sát, quan sát tỉ mỉ", "专家们去农村考察了一个月。", "Các chuyên gia đi khảo sát ở nông thôn một tháng.",
     "Động từ, nghĩa là đến tận nơi để khảo sát, tìm hiểu kỹ. Chữ thứ hai là chữ sát trong quan sát, đọc thanh hai."),
    ("访问", "fǎngwèn", "phỏng vấn", "động từ", "thăm, đi thăm; phỏng vấn", "总统下个月将访问中国。", "Tổng thống sẽ thăm Trung Quốc vào tháng sau.",
     "Động từ. Cẩn thận, đây là từ dễ nhầm: tiếng Việt phỏng vấn là hỏi chuyện để lấy tin, còn 访问 trong tiếng Trung chủ yếu là đến thăm, như một chuyến thăm chính thức. Đi phỏng vấn lấy tin thường dùng 采访. Ngoài ra, 访问网站 là truy cập trang web."),
    ("高峰", "gāofēng", "cao phong", "danh từ", "đỉnh cao", "早上八点是上班的高峰。", "Tám giờ sáng là giờ cao điểm đi làm.",
     "Danh từ, nghĩa gốc là đỉnh núi cao, nghĩa bóng là đỉnh cao, giai đoạn cực thịnh. Trong bài, 事业达到高峰 là sự nghiệp lên đến đỉnh cao. Hay gặp 高峰期, giờ cao điểm."),
    ("毅然", "yìrán", "nghị nhiên", "phó từ", "kiên quyết, cương quyết", "他毅然辞去了工作。", "Anh ấy kiên quyết từ bỏ công việc.",
     "Phó từ, nghĩa là kiên quyết, không chút do dự, thường dùng khi đưa ra một quyết định lớn và khó khăn. Hay đi với 毅然决定，毅然离开. Chữ 毅 cũng có trong 毅力, nghị lực."),
    ("疲惫", "píbèi", "bì bại", "tính từ", "mệt mỏi, mệt nhọc", "加了一夜班，他显得非常疲惫。", "Tăng ca cả đêm, anh ấy trông vô cùng mệt mỏi.",
     "Tính từ, nghĩa là mệt mỏi rã rời, mức độ nặng hơn 累, mang màu sắc văn viết. Trong bài có 身心疲惫, cả thể xác lẫn tinh thần đều mệt mỏi."),
    ("力所能及", "lìsuǒnéngjí", "lực sở năng cập", "thành ngữ", "nằm trong khả năng, vừa sức", "孩子应该做些力所能及的家务。", "Trẻ con nên làm những việc nhà vừa sức mình.",
     "Thành ngữ, nghĩa là việc mà sức mình có thể làm được, vừa sức. 力 là sức, 所能及 là cái có thể với tới. Thường làm định ngữ: 力所能及的事; hoặc làm trạng ngữ: 力所能及地帮助别人."),
    ("开拓", "kāituò", "khai thác", "động từ", "mở rộng, phát triển, khai phá", "公司正在开拓海外市场。", "Công ty đang mở rộng thị trường nước ngoài.",
     "Động từ, nghĩa là khai phá, mở mang ra cái mới. Cẩn thận: tiếng Việt khai thác thường là khai thác tài nguyên, tiếng Trung gọi là 开采 hoặc 开发; còn 开拓 thiên về mở đường, mở rộng: 开拓市场，开拓新的生活. Âm tiết thứ hai đọc thanh bốn."),
    ("职务", "zhíwù", "chức vụ", "danh từ", "chức vụ", "他担任经理职务已经五年了。", "Ông ấy giữ chức vụ giám đốc đã năm năm rồi.",
     "Danh từ, nghĩa là chức vụ, âm Hán Việt và nghĩa giống tiếng Việt. Trong bài, 没有了职务 là không còn chức vụ nữa, tức là ông đã rời tòa báo."),
    ("捆绑", "kǔnbǎng", "khổn bảng", "động từ", "trói, buộc", "他们把行李捆绑在车顶上。", "Họ buộc hành lý lên nóc xe.",
     "Động từ, nghĩa là dùng dây trói, buộc chặt lại. Nghĩa bóng là bị ràng buộc, mất tự do. Trong bài, 从捆绑状态中被释放出来 là được giải thoát khỏi trạng thái bị trói buộc."),
    ("释放", "shìfàng", "thích phóng", "động từ", "thả ra, phóng thích", "运动可以释放压力。", "Vận động có thể giải tỏa áp lực.",
     "Động từ, nghĩa là thả ra, phóng thích, như 释放犯人, thả phạm nhân. Nghĩa mở rộng là giải tỏa, tỏa ra: 释放压力, giải tỏa áp lực. Tiếng Việt nói ngược thứ tự: phóng thích."),
    ("出身", "chūshēn", "xuất thân", "danh từ", "sự xuất thân, lai lịch", "他出身于一个普通工人家庭。", "Anh ấy xuất thân từ một gia đình công nhân bình thường.",
     "Danh từ hoặc động từ, chỉ thân phận do gia đình hoặc nghề nghiệp trước đây quyết định. Mẫu nghề nghiệp cộng 出身 nghĩa là trước đây làm nghề đó: 记者出身的妻子, người vợ vốn là nhà báo."),
    ("鼓动", "gǔdòng", "cổ động", "động từ", "động viên, khuyến khích; xúi giục", "是朋友鼓动他去创业的。", "Chính bạn bè đã khích anh ấy đi khởi nghiệp.",
     "Động từ, nghĩa là dùng lời nói, chữ viết để khích động, thúc giục người khác hành động. Chú ý: hành động đó có thể tốt, cũng có thể xấu; khi xấu thì dịch là xúi giục. Lát nữa chúng ta sẽ so sánh kỹ 鼓动 với 鼓励."),
    ("夫妇", "fūfù", "phu phụ", "danh từ", "vợ chồng", "那对老夫妇每天都去公园散步。", "Đôi vợ chồng già ấy ngày nào cũng ra công viên đi dạo.",
     "Danh từ, nghĩa là vợ chồng, giống 夫妻 nhưng trang trọng hơn. Lượng từ là 对: 一对夫妇. Trong bài có 他们夫妇, vợ chồng họ."),
    ("头脑", "tóunǎo", "đầu não", "danh từ", "đầu óc", "他很有经济头脑。", "Anh ấy rất có đầu óc kinh doanh.",
     "Danh từ, nghĩa là đầu óc, khả năng suy nghĩ; cũng chỉ những gì đang có trong đầu. Cẩn thận: tiếng Việt đầu não là trung tâm chỉ huy, còn 头脑 là đầu óc. Trong bài, 头脑中全是书本中对北极的描述 là trong đầu toàn là những miêu tả về Bắc Cực trong sách."),
    ("遭遇", "zāoyù", "tao ngộ", "động từ", "gặp phải (điều không may)", "他们在路上遭遇了大雨。", "Trên đường, họ gặp phải một trận mưa lớn.",
     "Động từ, nghĩa là gặp phải điều không may, kẻ thù, khó khăn. Cẩn thận: tiếng Việt tao ngộ là cuộc gặp gỡ tình cờ, thường mang sắc thái đẹp; còn 遭遇 luôn đi với chuyện xấu: 遭遇困难，遭遇不幸，遭遇围堵. Cũng làm danh từ, nghĩa là cảnh ngộ."),
    ("灾难", "zāinàn", "tai nạn", "danh từ", "tai họa, tai ương, thảm họa", "这场地震带来了巨大的灾难。", "Trận động đất này đã gây ra thảm họa to lớn.",
     "Danh từ, chỉ thảm họa, tai họa lớn gây tổn thất nghiêm trọng, như động đất, chiến tranh. Cẩn thận: tiếng Việt tai nạn thường là tai nạn giao thông, tiếng Trung gọi là 事故; còn 灾难 lớn hơn nhiều, là thảm họa."),
    ("饥饿", "jī'è", "cơ ngạ", "tính từ", "đói", "世界上还有很多人生活在饥饿中。", "Trên thế giới vẫn còn nhiều người sống trong cảnh đói khát.",
     "Tính từ, nghĩa là đói, mức độ nặng, thường là đói lâu ngày do thiếu ăn, mang màu sắc văn viết. Khẩu ngữ hằng ngày chỉ nói 饿. Chữ 饥 cũng có trong 饥荒, nạn đói."),
    ("风暴", "fēngbào", "phong bạo", "danh từ", "gió bão, giông bão", "一场风暴就要来了。", "Một trận giông bão sắp đến rồi.",
     "Danh từ, nghĩa là gió bão, giông bão, thường kèm mưa lớn. Nghĩa bóng là biến động lớn: 金融风暴, cơn bão tài chính."),
    ("严寒", "yánhán", "nghiêm hàn", "tính từ", "giá rét", "战士们在严寒中站岗。", "Các chiến sĩ đứng gác trong giá rét.",
     "Tính từ, nghĩa là cực kỳ lạnh, giá rét; cũng dùng như danh từ chỉ cái giá rét. Trong bài, 饥饿、风暴、严寒 là ba thử thách lớn của người Inuit."),
    ("惊奇", "jīngqí", "kinh kỳ", "tính từ", "kinh ngạc, sửng sốt", "大家都惊奇地看着他。", "Mọi người đều kinh ngạc nhìn anh ấy.",
     "Tính từ, nghĩa là ngạc nhiên, lấy làm lạ vì thấy điều không ngờ tới. Thường làm trạng ngữ: 惊奇地发现, ngạc nhiên phát hiện ra, như trong bài."),
    ("记载", "jìzǎi", "ký tải", "động từ", "ghi chép, ghi lại", "这本书记载了很多历史故事。", "Cuốn sách này ghi lại nhiều câu chuyện lịch sử.",
     "Động từ, nghĩa là ghi chép lại, thường là sự việc lịch sử; cũng làm danh từ: 文字记载, những ghi chép bằng chữ viết. Chú ý: âm tiết thứ hai đọc thanh ba."),
    ("差别", "chābié", "sai biệt", "danh từ", "sự khác biệt", "城市和农村的差别越来越小。", "Sự khác biệt giữa thành thị và nông thôn ngày càng nhỏ.",
     "Danh từ, nghĩa là sự khác biệt, chỗ khác nhau. Chú ý: chữ đầu đọc thanh một, giống như trong 差距，差异."),
    ("连锁", "liánsuǒ", "liên tỏa", "tính từ", "dây chuyền, chuỗi", "这家连锁店在全国有一百多家分店。", "Chuỗi cửa hàng này có hơn một trăm chi nhánh trên cả nước.",
     "Tính từ, nghĩa là nối liền như các mắt xích, dây chuyền. Hay gặp 连锁店, chuỗi cửa hàng; 连锁超市, chuỗi siêu thị; 连锁反应, phản ứng dây chuyền."),
    ("包装", "bāozhuāng", "bao trang", "động từ / danh từ", "đóng gói; bao bì", "这种饼干的包装很漂亮。", "Bao bì của loại bánh quy này rất đẹp.",
     "Vừa là động từ, đóng gói, vừa là danh từ, bao bì. Trong bài có 包装食品, thực phẩm đóng gói. Nghĩa bóng: 包装自己, đánh bóng hình ảnh bản thân."),
    ("衣裳", "yīshang", "y thường", "danh từ", "quần áo", "她穿了一件漂亮的衣裳。", "Cô ấy mặc một bộ quần áo đẹp.",
     "Danh từ, nghĩa là quần áo, giống 衣服, mang màu sắc khẩu ngữ. Chú ý: âm tiết thứ hai đọc nhẹ."),
    ("潇洒", "xiāosǎ", "tiêu sái", "tính từ", "phóng khoáng và thanh lịch", "他穿上西装，显得很潇洒。", "Anh ấy mặc vest vào trông rất phong độ.",
     "Tính từ, chỉ dáng vẻ, phong thái tự nhiên, phóng khoáng, không gò bó và rất cuốn hút. Ngày nay người trẻ hay nói 活得潇洒, sống thật tự do, thoải mái."),
    ("本能", "běnnéng", "bản năng", "danh từ", "bản năng", "保护孩子是母亲的本能。", "Bảo vệ con là bản năng của người mẹ.",
     "Danh từ, nghĩa là bản năng, âm Hán Việt và nghĩa giống tiếng Việt. Trong bài có 记者的职业本能, bản năng nghề nghiệp của nhà báo."),
    ("冲动", "chōngdòng", "xung động", "danh từ", "sự thôi thúc, sự thúc đẩy", "我突然有一种想去旅行的冲动。", "Tôi bỗng có một sự thôi thúc muốn đi du lịch.",
     "Danh từ, nghĩa là sự thôi thúc mạnh mẽ trong lòng muốn làm một việc gì đó. Ngoài ra còn là tính từ, nghĩa là bốc đồng: 别太冲动, đừng bốc đồng quá."),
    ("相差", "xiāngchà", "tương sai", "động từ", "khác nhau, chênh lệch", "我们俩的年龄相差三岁。", "Hai chúng tôi chênh nhau ba tuổi.",
     "Động từ, nghĩa là chênh lệch, khác nhau bao nhiêu. Chú ý: chữ thứ hai ở đây đọc thanh bốn, khác với 差别. Trong bài, 相差多么遥远 là cách xa nhau biết bao."),
    ("古董", "gǔdǒng", "cổ đổng", "danh từ", "đồ cổ", "爷爷喜欢收藏古董。", "Ông nội thích sưu tầm đồ cổ.",
     "Danh từ, nghĩa là đồ cổ, đồ vật quý từ thời xưa để lại. Nói đùa về người thì chỉ người cổ hủ: 老古董. Trong bài, 老照片已成为了古董 là những bức ảnh cũ đã thành đồ cổ, tức là không còn đúng với hiện tại."),
    ("在意", "zàiyì", "tại ý", "động từ", "để ý, quan tâm, để tâm", "别人怎么说，他一点儿也不在意。", "Người khác nói gì, anh ấy chẳng để tâm chút nào.",
     "Động từ, nghĩa là để ý, để tâm, bận lòng, thường dùng trong câu phủ định: 不在意，别在意. Gần nghĩa với 在乎."),
    ("捕捉", "bǔzhuō", "bộ tróc", "động từ", "bắt, tóm", "猫在草地上捕捉老鼠。", "Con mèo bắt chuột trên bãi cỏ.",
     "Động từ, nghĩa là bắt, tóm, nói về động vật hoặc người đang chạy trốn. Nghĩa bóng là nắm bắt: 捕捉机会，捕捉镜头, chớp lấy khoảnh khắc khi chụp ảnh."),
    ("赤道", "chìdào", "xích đạo", "danh từ", "xích đạo", "赤道附近的国家一年四季都很热。", "Các nước gần xích đạo nóng quanh năm.",
     "Danh từ, nghĩa là đường xích đạo. Chữ 赤 nghĩa là màu đỏ, như trong 赤字, thâm hụt. Trong bài, 赤道血统的北极姑娘 là cô gái Bắc Cực mang dòng máu vùng xích đạo."),
    ("专题", "zhuāntí", "chuyên đề", "danh từ", "chuyên đề", "电视台做了一个环保专题节目。", "Đài truyền hình làm một chương trình chuyên đề về môi trường.",
     "Danh từ, nghĩa là chuyên đề, một đề tài riêng được nghiên cứu, thảo luận sâu. Trong bài, 采访专题 là chuyên đề phóng sự của Vương Kiến Nam."),
    ("抢救", "qiǎngjiù", "thương cứu", "động từ", "giải cứu, cứu nguy, cứu vãn", "医生们正在全力抢救病人。", "Các bác sĩ đang dốc toàn lực cấp cứu bệnh nhân.",
     "Động từ, nghĩa là cứu gấp trong tình huống nguy cấp, như 抢救病人, cấp cứu bệnh nhân. Nghĩa mở rộng là cứu vãn những thứ sắp mất đi: 抢救文物, cứu vãn di sản văn hóa. Chữ 抢 ở đây là tranh thủ, giành giật thời gian."),
    ("刻不容缓", "kèbùrónghuǎn", "khắc bất dung hoãn", "thành ngữ", "vô cùng khẩn cấp, không thể chậm trễ", "保护环境已经刻不容缓。", "Bảo vệ môi trường đã là việc không thể chậm trễ.",
     "Thành ngữ. 刻 là khắc, một khoảng thời gian rất ngắn; 不容缓 là không cho phép trì hoãn. Cả câu nghĩa là không thể chậm trễ dù chỉ một khắc. Thường làm vị ngữ, đứng cuối câu."),
    ("支出", "zhīchū", "chi xuất", "danh từ", "phí tổn, khoản chi", "这个月家里的支出比较多。", "Tháng này chi tiêu trong nhà khá nhiều.",
     "Danh từ, nghĩa là khoản chi, tiền chi ra; cũng làm động từ, nghĩa là chi ra. Trái nghĩa là 收入, thu nhập."),
    ("精打细算", "jīngdǎ-xìsuàn", "tinh đả tế toán", "thành ngữ", "tính toán kỹ lưỡng", "她过日子很会精打细算。", "Cô ấy sống rất biết tính toán chi li.",
     "Thành ngữ, nghĩa là tính toán tỉ mỉ, chi tiêu dè sẻn, không lãng phí. 打 và 算 đều là tính toán, 精 và 细 đều là tỉ mỉ."),
    ("开支", "kāizhī", "khai chi", "danh từ", "khoản chi, tiền tiêu", "我们要减少不必要的开支。", "Chúng ta phải cắt giảm những khoản chi không cần thiết.",
     "Danh từ, nghĩa là khoản chi, chi phí; cũng làm động từ, nghĩa là chi trả. Gần nghĩa với 支出. Trong bài có cụm 节省开支, tiết kiệm chi tiêu."),
    ("免得", "miǎnde", "miễn đắc", "liên từ", "để tránh, đỡ phải, kẻo", "多穿点儿衣服，免得感冒。", "Mặc thêm áo vào, kẻo bị cảm.",
     "Liên từ, nghĩa là để tránh, kẻo, đỡ phải, đứng đầu vế sau. Đây là điểm ngữ pháp thứ ba của bài. Âm tiết thứ hai đọc nhẹ."),
    ("储蓄", "chǔxù", "trữ súc", "danh từ", "tiền để dành, tiền tiết kiệm", "他用多年的储蓄买了房子。", "Anh ấy dùng tiền tiết kiệm bao năm để mua nhà.",
     "Danh từ, nghĩa là tiền để dành, tiền tiết kiệm; cũng làm động từ, nghĩa là gửi tiết kiệm, tích trữ. 储 là chứa, 蓄 là tích lại."),
    ("穿越", "chuānyuè", "xuyên việt", "động từ", "đi qua, xuyên qua", "这条铁路穿越了整个沙漠。", "Tuyến đường sắt này xuyên qua cả sa mạc.",
     "Động từ, nghĩa là băng qua, xuyên qua một vùng rộng lớn, khó đi: 穿越沙漠，穿越森林. Ngày nay 穿越 còn chỉ thể loại phim, truyện xuyên không."),
    ("腹泻", "fùxiè", "phúc tả", "động từ", "bị tiêu chảy", "他吃了不干净的东西，开始腹泻。", "Anh ấy ăn phải đồ không sạch, bắt đầu bị tiêu chảy.",
     "Động từ, nghĩa là bị tiêu chảy, là từ dùng trong y học, văn viết. Khẩu ngữ hay nói 拉肚子. 腹 là bụng, 泻 là chảy ra."),
    ("时常", "shícháng", "thời thường", "phó từ", "thường xuyên", "他时常想起小时候的事情。", "Anh ấy thường nhớ lại những chuyện hồi nhỏ.",
     "Phó từ, nghĩa là thường thường, hay, giống 常常 và 经常. Trong bài, 时常煮一锅面条 là thường nấu một nồi mì."),
    ("将就", "jiāngjiu", "tương tựu", "động từ", "tạm, đỡ, chịu theo", "房间小了点儿，你将就住一晚吧。", "Phòng hơi nhỏ, bạn ở tạm một đêm nhé.",
     "Động từ, nghĩa là tạm chấp nhận dù điều kiện chưa tốt, như ở tạm, ăn tạm. Có thể lặp lại: 将就将就, như trong bài: 将就将就就是一餐, ăn tạm cho xong một bữa. Âm tiết thứ hai đọc nhẹ."),
    ("支配", "zhīpèi", "chi phối", "động từ", "sắp đặt, sắp xếp; điều khiển", "我想自由地支配自己的时间。", "Tôi muốn tự do sắp xếp thời gian của mình.",
     "Động từ, nghĩa là sắp xếp, phân bổ, như 支配时间，支配金钱; cũng có nghĩa là điều khiển, chi phối. Chú ý: tiếng Việt chi phối thường là ảnh hưởng, khống chế; còn trong bài, 自己支配自己的生命 là tự mình làm chủ, tự sắp xếp cuộc đời mình."),
    ("执着", "zhízhuó", "chấp trước", "tính từ", "cố chấp; kiên trì, bền bỉ", "他对音乐的追求非常执着。", "Anh ấy theo đuổi âm nhạc vô cùng bền bỉ.",
     "Tính từ, nghĩa gốc là cố chấp, bám chặt không buông. Cẩn thận: trong tiếng Trung hiện đại, 执着 thường mang nghĩa tốt, là kiên trì theo đuổi đến cùng; khác với chấp trước trong tiếng Việt, thường mang nghĩa xấu. Chữ thứ hai đọc thanh hai."),
]

add("bullets", chapter="Từ mới (50 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 14 có 50 từ mới, chia thành 17 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 记载 (zǎi) · 差别 (chā) · 相差 (chà) · 执着 (zhuó) · 衣裳 (shang)",
           "Từ dễ nhầm: 访问 · 开拓 · 头脑 · 遭遇 · 灾难 · 支配 · 执着"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có năm mươi từ, thầy chia thành mười bảy nhóm nhỏ, mỗi nhóm hai hoặc ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số từ có âm đọc cần chú ý, như 记载，差别，相差，执着，衣裳. Thầy sẽ nhắc khi gặp."),
         F(4, "Ngoài ra, có mấy từ Hán Việt rất dễ hiểu nhầm, như 访问，开拓，头脑，遭遇，灾难，支配，执着. Nghĩa của chúng trong tiếng Trung khác với tiếng Việt, các bạn nhớ nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

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
        say.append(F(i, f"{expl} Ví dụ: {ex}{'' if ex[-1] in '。…？！，' else '，'} {exvi[0].upper() + exvi[1:]}{'' if exvi.endswith('.') else '.'}", zr=130))
    add("vocab", section="Từ mới 生词", title=f"Từ mới ({g + 1}–{g + len(group)} / {len(V)})",
        words=words, say=say)
    g += gs

# ======================= BÀI KHÓA =======================
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung nếu khác])
P = [
    ("王建男大学毕业做过摄影记者、新闻评论员、编辑，50岁做了社长。",
     "Vương Kiến Nam sau khi tốt nghiệp đại học từng làm phóng viên ảnh, nhà bình luận tin tức, biên tập viên; năm mươi tuổi, ông trở thành giám đốc tòa báo.",
     ["王建男 là tên nhân vật chính, đọc theo Hán Việt là Vương Kiến Nam. 摄影记者 là phóng viên ảnh; 摄影 là chụp ảnh, nhiếp ảnh.",
      "做过 chỉ những công việc ông từng làm trong quá khứ. 社长 là người đứng đầu một tòa báo hay nhà xuất bản, ở đây là giám đốc tòa báo."],
     "王建男大学毕业做过摄影记者、新闻评论员、编辑，五十岁做了社长。"),
    ("追求完美的性格，使他领导的报社成为中国报业改革的典型，每天都会有一拨拨同行前来考察访问。",
     "Tính cách theo đuổi sự hoàn hảo khiến tòa báo do ông lãnh đạo trở thành điển hình của công cuộc cải cách ngành báo chí Trung Quốc; ngày nào cũng có hết tốp này đến tốp khác người cùng ngành đến khảo sát, tham quan.",
     ["使 cộng người hoặc vật cộng động từ là khiến cho. 报社 là tòa báo, 报业 là ngành báo chí.",
      "一拨拨 là lượng từ lặp lại, nghĩa là từng tốp, từng đoàn nối tiếp nhau; đây là điểm ngữ pháp thứ nhất. 同行 ở đây là những người cùng làm một nghề, tức là đồng nghiệp trong ngành."]),
    ("就在王建男事业达到高峰的时候，他毅然决定离开报社：他累了，身心疲惫，他想做自己愿意做的事，力所能及地开拓新的生活。",
     "Đúng vào lúc sự nghiệp của Vương Kiến Nam lên đến đỉnh cao, ông kiên quyết rời khỏi tòa báo: ông mệt rồi, thân tâm rã rời, ông muốn làm những việc mình thích, mở ra một cuộc sống mới trong khả năng của mình.",
     ["就在……的时候 nghĩa là đúng vào lúc…, nhấn mạnh thời điểm bất ngờ: đang ở đỉnh cao thì lại ra đi.",
      "Dấu hai chấm dùng để giải thích lý do. 力所能及地开拓新的生活: thành ngữ 力所能及地 làm trạng ngữ, nghĩa là làm vừa sức mình."]),
    ("没有了职务，王建男像是从捆绑状态中被释放出来，一身轻松。",
     "Không còn chức vụ, Vương Kiến Nam như được giải thoát khỏi trạng thái bị trói buộc, cả người nhẹ nhõm.",
     ["像是 nghĩa là giống như, dường như. 被释放出来 là câu bị động; 出来 chỉ hướng từ trong ra ngoài.",
      "一身轻松 là cả người nhẹ nhõm, thoải mái. Tác giả ví chức vụ như sợi dây trói, rời chức vụ là được thả ra."]),
    ("他先是办了家企业；不久他跨洋过海，到了加拿大；再后来，他恋上了北极。",
     "Đầu tiên ông mở một doanh nghiệp; không lâu sau ông vượt biển sang Canada; rồi về sau nữa, ông đem lòng yêu Bắc Cực.",
     ["先是……；不久……；再后来…… là chuỗi từ nối kể theo trình tự thời gian. Đây chính là mẫu câu của bài tập bốn, và là kỹ năng chúng ta sẽ học riêng ở cuối bài.",
      "办了家企业 là nói gọn của 办了一家企业. 跨洋过海 là vượt đại dương. 恋上 là đem lòng yêu, phải lòng."]),
    ("以前他一直认为去北极不是普通人的事，记者出身的妻子鼓动他说，年轻人自驾都能去，咱们怎么不行？于是，他们出发了。",
     "Trước đây ông vẫn luôn cho rằng đi Bắc Cực không phải là việc của người bình thường. Người vợ vốn là nhà báo khích lệ ông: Người trẻ tự lái xe còn đi được, sao chúng mình lại không được? Thế là, họ lên đường.",
     ["记者出身的妻子 là người vợ xuất thân là nhà báo, theo mẫu nghề nghiệp cộng 出身. 自驾 là tự lái xe đi du lịch.",
      "咱们怎么不行？ là câu hỏi tu từ, nghĩa là chúng mình chắc chắn đi được. 咱们 là chúng mình, bao gồm cả người nghe."]),
    ("因纽特人的传奇，是鼓舞他们夫妇勇闯北极的最大动力。",
     "Những câu chuyện huyền thoại về người Inuit là động lực lớn nhất cổ vũ vợ chồng ông dũng cảm xông pha Bắc Cực.",
     ["因纽特人 là người Inuit, cư dân bản địa vùng Bắc Cực, trước đây hay được gọi là người Eskimo. 传奇 là truyền kỳ, câu chuyện ly kỳ.",
      "鼓舞 là cổ vũ, làm phấn chấn. 勇闯 là dũng cảm xông vào nơi nguy hiểm."]),
    ("一路上，王建男头脑中全是书本中对北极的描述：大约4000年前，最后一批跨过白令海峡的亚裔族群，向美洲进发，途中遭遇印第安人的围堵，",
     "Suốt dọc đường, trong đầu Vương Kiến Nam toàn là những miêu tả về Bắc Cực trong sách: khoảng bốn nghìn năm trước, nhóm tộc người gốc Á cuối cùng vượt qua eo biển Bering, tiến về châu Mỹ, giữa đường gặp phải sự vây chặn của người da đỏ,",
     ["白令海峡 là eo biển Bering, nằm giữa châu Á và châu Mỹ. 亚裔族群 là tộc người gốc Á. 印第安人 là người da đỏ châu Mỹ.",
      "遭遇 đi với điều không may: 遭遇围堵, gặp phải sự vây chặn. 进发 là lên đường tiến về phía trước."],
     "一路上，王建男头脑中全是书本中对北极的描述：大约四千年前，最后一批跨过白令海峡的亚裔族群，向美洲进发，途中遭遇印第安人的围堵，"),
    ("最终退进气候恶劣的北极圈，住雪屋、用长矛打猎，他们遇到过想象中难以度过的灾难，最后在饥饿、风暴、严寒中奇迹般地生存下来，成为北极最大的原住民部族……",
     "cuối cùng lui vào vùng Bắc Cực khí hậu khắc nghiệt, ở nhà tuyết, dùng giáo dài săn bắn. Họ từng gặp những tai họa khó vượt qua đến mức không thể tưởng tượng, cuối cùng sống sót kỳ diệu giữa đói khát, bão tố và giá rét, trở thành tộc người bản địa lớn nhất Bắc Cực…",
     ["北极圈 là vòng Bắc Cực. 雪屋 là nhà tuyết, tức lều igloo. 长矛 là ngọn giáo dài.",
      "想象中难以度过的灾难 là những tai họa khó vượt qua đến mức khó tưởng tượng; đây là điểm ngữ pháp 难以. 奇迹般地 là một cách kỳ diệu, như một phép màu."]),
    ("到了北极，他们惊奇地发现，现实和文字记载中因纽特人的生活差别竟是如此之大：因纽特村落家家屋内温暖如春，家电齐全，户户都能上网；",
     "Đến Bắc Cực, họ ngạc nhiên phát hiện ra rằng cuộc sống của người Inuit trong thực tế và trong sách vở khác nhau lớn đến vậy: trong làng của người Inuit, nhà nào cũng ấm áp như mùa xuân, đồ điện đầy đủ, nhà nhà đều lên mạng được;",
     ["竟 là vậy mà, lại, biểu thị sự bất ngờ. 如此之大 là lớn đến như thế, cách nói văn viết.",
      "家家 và 户户 đều là danh từ lặp lại, nghĩa là nhà nào cũng. 温暖如春 là ấm áp như mùa xuân, 家电齐全 là đồ điện gia dụng đầy đủ."]),
    ("连锁超市里卖的是包装食品，年轻人穿着时髦的衣裳，潇洒而快活。",
     "Các siêu thị chuỗi bán thực phẩm đóng gói, người trẻ mặc quần áo thời trang, phóng khoáng và vui tươi.",
     ["时髦 là hợp mốt, thời thượng. 潇洒而快活: 而 nối hai tính từ, nghĩa là và.",
      "Hình ảnh này trái ngược hẳn với nhà tuyết và giáo dài trong sách: Bắc Cực ngày nay đã hiện đại hóa."]),
    ("记者的职业本能让王建男产生了这样的冲动：用我的照片让世人知道，北极的过去和现在相差多么遥远。老照片已成为了古董，那时的北极已经不复存在。",
     "Bản năng nghề nghiệp của nhà báo khiến Vương Kiến Nam nảy ra một sự thôi thúc: dùng ảnh của mình cho người đời biết quá khứ và hiện tại của Bắc Cực cách xa nhau đến nhường nào. Ảnh cũ đã thành đồ cổ, Bắc Cực thời ấy không còn tồn tại nữa.",
     ["产生冲动 là nảy sinh sự thôi thúc. 世人 là người đời, mọi người trên thế giới.",
      "相差多么遥远 là chênh lệch xa đến mức nào. 不复存在 là không còn tồn tại nữa; 不复 là cách nói văn viết, nghĩa là không còn."]),
    ("从此，王建男不再在意自然风光和千奇百怪的动植物，只专注于人文。他的镜头中有捕捉动物的妇人，有赤道血统的北极姑娘……",
     "Từ đó, Vương Kiến Nam không còn để tâm đến phong cảnh thiên nhiên và muôn loài động thực vật kỳ lạ nữa, mà chỉ tập trung vào con người và văn hóa. Trong ống kính của ông có người phụ nữ đang bắt thú, có cô gái Bắc Cực mang dòng máu xích đạo…",
     ["从此 là từ đó trở đi. 千奇百怪 là muôn hình vạn trạng, kỳ lạ đủ kiểu. 专注于 là chuyên tâm vào; 于 là giới từ văn viết.",
      "人文 ở đây chỉ con người, đời sống và văn hóa. 镜头 là ống kính, cũng chỉ khung hình. 血统 là huyết thống, dòng máu."]),
    ("他的采访专题是“北极人文圈”，他知道抢救因纽特人生活中正在消失的东西刻不容缓。",
     "Chuyên đề phóng sự của ông là Vòng nhân văn Bắc Cực; ông biết rằng việc cứu vãn những gì đang biến mất trong đời sống người Inuit là vô cùng cấp bách.",
     ["采访 là đi phỏng vấn, lấy tin, khác với 访问 chúng ta đã học. 专题 là chuyên đề.",
      "Chủ ngữ của 刻不容缓 là cả cụm dài 抢救因纽特人生活中正在消失的东西, nghĩa là việc cứu vãn những thứ đang mất dần không thể chậm trễ."],
     "他的采访专题是北极人文圈，他知道抢救因纽特人生活中正在消失的东西刻不容缓。"),
    ("他和妻子往返北极17次，支出很大，他们处处精打细算，千方百计节省开支，免得多年的储蓄减少得太快，",
     "Ông cùng vợ đi về Bắc Cực mười bảy lần, chi phí rất lớn. Họ tính toán chi li mọi mặt, tìm đủ mọi cách tiết kiệm chi tiêu, để khoản tiết kiệm bao năm khỏi vơi đi quá nhanh.",
     ["往返 là đi và về, khứ hồi. 处处 là ở mọi nơi, mọi mặt. 千方百计 là trăm phương nghìn kế.",
      "免得多年的储蓄减少得太快 là để tránh tiền tiết kiệm bao năm hao hụt quá nhanh. Đây là điểm ngữ pháp 免得, đứng ở đầu vế sau."],
     "他和妻子往返北极十七次，支出很大，他们处处精打细算，千方百计节省开支，免得多年的储蓄减少得太快，"),
    ("即使穿越辽阔的无人区，他们也只租用最便宜的汽车；发烧、腹泻什么的，也多数是自带药品解决，",
     "Ngay cả khi băng qua những vùng không người bao la, họ cũng chỉ thuê loại ô tô rẻ nhất; những bệnh như sốt, tiêu chảy, phần lớn cũng tự chữa bằng thuốc mang theo.",
     ["即使……也…… nghĩa là cho dù… cũng…. 辽阔 là bao la, rộng lớn. 无人区 là vùng không có người ở.",
      "什么的 đặt sau một loạt danh từ, nghĩa là vân vân, những thứ như thế, cách nói khẩu ngữ. 自带药品 là thuốc tự mang theo."]),
    ("他们带着饭锅、面条、自制肉酱，时常煮一锅面条，放点儿蔬菜和肉酱，将就将就就是一餐。",
     "Họ mang theo nồi cơm, mì sợi, tương thịt tự làm, thường nấu một nồi mì, bỏ chút rau và tương thịt, ăn tạm vậy là xong một bữa.",
     ["饭锅 chính là cái nồi cơm điện trong tên bài. 肉酱 là tương thịt. 一锅面条 là một nồi mì; ở đây 锅 được mượn làm lượng từ.",
      "将就将就就是一餐: động từ 将就 lặp lại, mang ý tạm bợ, qua loa; từ 就是 phía sau nghĩa là thế là thành. Câu này cho thấy cuộc sống rất kham khổ của hai vợ chồng."]),
    ("日子艰苦是艰苦，可是王建男却很有幸福感，他愿意自己支配自己的生命，执着地要为历史留下些印迹。",
     "Cuộc sống vất vả thì vất vả thật, nhưng Vương Kiến Nam lại cảm thấy rất hạnh phúc. Ông muốn tự mình làm chủ cuộc đời mình, bền bỉ để lại cho lịch sử một vài dấu ấn.",
     ["艰苦是艰苦，可是…… theo mẫu A thì A thật, nhưng…: thừa nhận một sự thật rồi chuyển ý, giống 固然 mà chúng ta đã học ở bài năm.",
      "执着地 làm trạng ngữ, nghĩa là bền bỉ, kiên trì. 印迹 là dấu vết, dấu ấn. Câu kết nói lên ý nghĩa của cả bài: sống theo cách mình chọn và để lại giá trị cho đời."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 背着电饭锅拍北极", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 背着电饭锅拍北极, dài tám trăm bốn mươi bốn chữ. Bài được cải biên từ bài báo 背着电饭锅拍遍北极 trên 北京晚报, tác giả là 邱伟.",
         F(0, "Thầy chia bài thành mười tám đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
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
    items=["## 1. 王建男的工作经历 – quá trình làm việc",
           "大学毕业做过摄影记者、评论员、编辑 · 报社成为报业改革的典型 · 身心疲惫，毅然决定离开报社",
           "## 2. 辞职后，王建男有什么经历？",
           "先是办了家企业；不久到了加拿大；再后来，恋上了北极",
           "## 3. 书中一般是怎样描述北极的？",
           "大约4000年前……途中遭遇印第安人的围堵，最终退进北极圈，住雪屋、用长矛打猎……生存下来"],
    say=["Bài tập năm của sách yêu cầu dựa vào gợi ý để tóm tắt nội dung chính của bài khóa. Chúng ta cùng làm luôn nhé.",
         F(0, "Câu hỏi một: hãy tóm tắt quá trình làm việc của Vương Kiến Nam."),
         F(1, "大学毕业做过摄影记者、新闻评论员、编辑。 Tốt nghiệp đại học, ông làm phóng viên ảnh, nhà bình luận, biên tập viên. 他领导的报社成为中国报业改革的典型。 Tòa báo ông lãnh đạo trở thành điển hình cải cách. Rồi 身心疲惫，毅然决定离开报社, thân tâm mệt mỏi, ông kiên quyết rời tòa báo."),
         F(2, "Câu hỏi hai: sau khi từ chức, Vương Kiến Nam đã trải qua những gì?"),
         F(3, "他先是办了家企业；不久到了加拿大；再后来，他恋上了北极。 Đầu tiên mở doanh nghiệp, không lâu sau sang Canada, rồi về sau đem lòng yêu Bắc Cực."),
         F(4, "Câu hỏi ba: sách vở thường miêu tả Bắc Cực như thế nào?"),
         F(5, "大约四千年前，最后一批亚裔族群跨过白令海峡，途中遭遇印第安人的围堵，最终退进北极圈，住雪屋、用长矛打猎，在饥饿、风暴、严寒中生存下来。 Khoảng bốn nghìn năm trước, tộc người gốc Á vượt eo biển Bering, bị người da đỏ vây chặn, lui vào vòng Bắc Cực, ở nhà tuyết, săn bằng giáo, và sống sót giữa đói rét.")])

add("bullets", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5) – phần 2", size=34,
    items=["## 4. 现实的北极是什么样的？",
           "屋内温暖如春，家电齐全 · 连锁超市卖包装食品 · 年轻人穿着时髦，潇洒而快活",
           "## 5. 现在，王建男专注于什么事情？",
           "不再在意自然风光和动植物，只专注于人文 · 采访专题是“北极人文圈”",
           "## 6. 为了节省开支，王建男夫妇采取了什么措施？",
           "处处精打细算 · 租用最便宜的汽车 · 自带药品 · 将就将就就是一餐"],
    say=[F(0, "Câu hỏi bốn: Bắc Cực ngoài đời thực như thế nào?"),
         F(1, "屋内温暖如春，家电齐全。 Trong nhà ấm áp như mùa xuân, đồ điện đầy đủ. 连锁超市里卖的是包装食品。 Siêu thị chuỗi bán thực phẩm đóng gói. 年轻人穿着时髦，潇洒而快活。 Người trẻ ăn mặc hợp mốt, phóng khoáng và vui tươi."),
         F(2, "Câu hỏi năm: hiện nay Vương Kiến Nam tập trung vào việc gì?"),
         F(3, "他不再在意自然风光和千奇百怪的动植物，只专注于人文，采访专题是北极人文圈。 Ông không còn để tâm đến phong cảnh và động thực vật, chỉ tập trung vào con người và văn hóa, với chuyên đề Vòng nhân văn Bắc Cực."),
         F(4, "Câu hỏi sáu: để tiết kiệm chi phí, vợ chồng ông đã làm những gì?"),
         F(5, "处处精打细算，租用最便宜的汽车，自带药品，带着饭锅，将就将就就是一餐。 Tính toán chi li mọi mặt, thuê xe rẻ nhất, tự mang thuốc, mang nồi cơm theo, ăn tạm cho xong bữa. Bố cục này rất có ích khi các bạn làm bài tập về nhà: tóm tắt bài khóa.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: lượng từ lặp lại", section="Ngữ pháp 注释", title="1. Lặp lại cụm số lượng: 一拨拨", size=34,
    items=["一 + lượng từ + lượng từ (= 一 + lượng từ + 一 + lượng từ): 一拨一拨 → 一拨拨",
           "Miêu tả số lượng nhiều, nhưng sự vật hiện ra theo từng cá thể, nối tiếp nhau → khác với 很多",
           "Số từ chỉ dùng 一; chữ 一 thứ hai có thể lược bỏ",
           "每天都会有一拨拨同行前来考察访问。",
           "她收集的那一幅幅图片、一本本资料、一盘盘调查录音带，都是不容置疑的铁证。",
           "饭要一口口吃，话要一句句说，事要一件件做。"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là cách lặp lại cụm số lượng, tiếng Trung gọi là 数量短语的重叠.",
         F(0, "Trong bài khóa có cụm 一拨拨. 一拨 là một tốp, một đoàn. Lặp lại lượng từ, ta được 一拨一拨, và nói gọn thành 一拨拨."),
         F(1, "Cấu trúc này miêu tả số lượng rất nhiều, nhưng sự vật hiện ra theo từng cá thể, cái này nối tiếp cái kia. Vì vậy nghĩa và chức năng của nó khác với 很多. Nói 很多同行 chỉ là có nhiều người; còn 一拨拨同行 cho ta thấy hình ảnh từng đoàn, từng đoàn nối nhau kéo đến."),
         F(2, "Chú ý: số từ chỉ dùng 一, không dùng số khác. Và chữ 一 thứ hai có thể lược bỏ."),
         F(3, "Ví dụ một, lấy từ bài khóa: 每天都会有一拨拨同行前来考察访问。 Ngày nào cũng có hết tốp này đến tốp khác người cùng ngành đến khảo sát, tham quan."),
         F(4, "Ví dụ hai: 她收集的那一幅幅图片、一本本资料、一盘盘调查录音带，都是不容置疑的铁证。 Từng bức ảnh, từng cuốn tài liệu, từng cuộn băng ghi âm điều tra mà cô ấy thu thập được, đều là bằng chứng không thể chối cãi. Ở đây cụm lặp lại làm định ngữ, đứng trước danh từ."),
         F(5, "Ví dụ ba: 饭要一口口吃，话要一句句说，事要一件件做。 Cơm phải ăn từng miếng, lời phải nói từng câu, việc phải làm từng việc một. Ở đây cụm lặp lại làm trạng ngữ, đứng trước động từ, nghĩa là lần lượt, từng cái một.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: điền cụm số lượng lặp lại", reveal=True, size=36,
    items=["(1) 他在心里努力搜寻着（    ）能够说服妈妈的理由。",
           "Đáp án: 一条条",
           "(2) 学校是如何把（    ）十多岁的中学生培养成（    ）能够抗击风浪、展翅高飞的山鹰的。",
           "Đáp án: 一个个 · 一只只",
           "(3) 他所做的（    ）看似平常的小事，感动着身边的每一个人。",
           "Đáp án: 一件件"],
    say=[F(0, "Luyện tập: điền vào ngoặc hình thức lặp lại thích hợp của cụm số lượng. Câu một: 他在心里努力搜寻着什么能够说服妈妈的理由。 Trong lòng anh ấy cố tìm kiếm những lý do có thể thuyết phục mẹ. Lý do dùng lượng từ gì? Các bạn tạm dừng và thử nhé."),
         F(1, "Đáp án: 一条条. Lý do dùng lượng từ 条, nên ta có 一条条能够说服妈妈的理由, từng lý do một."),
         F(2, "Câu hai: 学校是如何把什么十多岁的中学生培养成什么能够抗击风浪、展翅高飞的山鹰的。 Nhà trường đã làm thế nào để đào tạo những học sinh mười mấy tuổi thành những chú đại bàng núi có thể chống chọi sóng gió, dang cánh bay cao?"),
         F(3, "Đáp án: 一个个十多岁的中学生, và 一只只山鹰. Người dùng 个, còn chim dùng 只."),
         F(4, "Câu ba: 他所做的什么看似平常的小事，感动着身边的每一个人。 Những việc nhỏ tưởng như bình thường mà anh ấy làm, đã làm cảm động mọi người xung quanh."),
         F(5, "Đáp án: 一件件. Việc dùng lượng từ 件: 他所做的一件件看似平常的小事.")])

add("bullets", chapter="Ngữ pháp: 难以", section="Ngữ pháp 注释", title="2. 难以 nányǐ – khó mà", size=36,
    items=["Động từ, nghĩa là 不容易、很难 · dùng trong văn viết",
           "Sau 难以 là động từ hoặc tính từ hai âm tiết trở lên, không đi với từ một âm tiết",
           "事情已经过去好久了，可是每次回想起当时的情景，心情还是难以平静。",
           "这样的假话最好不要说，因为你自己都难以自圆其说，别人怎么能够相信呢？",
           "他们遇到过想象中难以度过的灾难，最后在饥饿、风暴、严寒中奇迹般地生存下来……"],
    say=["Điểm ngữ pháp thứ hai là động từ 难以.",
         F(0, "难以 là động từ, nghĩa giống 不容易 và 很难, tiếng Việt dịch là khó mà, khó có thể. Từ này dùng trong văn viết."),
         F(1, "Chú ý quan trọng: sau 难以 thường là động từ hoặc tính từ hai âm tiết trở lên, như 难以平静，难以想象，难以忘怀. Không nói 难以说, mà phải nói 难以说明 hoặc 很难说."),
         F(2, "Ví dụ một: 事情已经过去好久了，可是每次回想起当时的情景，心情还是难以平静。 Chuyện đã qua lâu rồi, nhưng mỗi lần nhớ lại cảnh lúc đó, lòng vẫn khó mà bình tĩnh được."),
         F(3, "Ví dụ hai: 这样的假话最好不要说，因为你自己都难以自圆其说，别人怎么能够相信呢？ Những lời nói dối như vậy tốt nhất đừng nói, vì chính bạn còn khó mà nói cho trót lọt, người khác sao tin được? 自圆其说 là thành ngữ, nghĩa là tự nói cho hợp lý, không mâu thuẫn."),
         F(4, "Ví dụ ba, lấy từ bài khóa: 他们遇到过想象中难以度过的灾难，最后在饥饿、风暴、严寒中奇迹般地生存下来。 Họ từng gặp những tai họa khó vượt qua đến mức không thể tưởng tượng, cuối cùng sống sót một cách kỳ diệu.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: chọn vế trước thích hợp", reveal=True, size=36,
    items=["A. 居然发生了这样的事情 · B. 虽然他经历了常人难以忍受的痛苦和艰辛 · C. 在老家度过的每一天都很愉快",
           "(1) （    ），至今令人难以忘怀。",
           "Đáp án: C – 在老家度过的每一天都很愉快，至今令人难以忘怀。",
           "(2) （    ），真是令人难以想象！",
           "Đáp án: A – 居然发生了这样的事情，真是令人难以想象！",
           "(3) （    ），他却从来没退缩过。",
           "Đáp án: B – 虽然他经历了常人难以忍受的痛苦和艰辛，他却从来没退缩过。"],
    say=[F(0, "Luyện tập: chọn vế trước thích hợp cho mỗi câu. Ba lựa chọn là: A, 居然发生了这样的事情, vậy mà lại xảy ra chuyện như thế này. B, 虽然他经历了常人难以忍受的痛苦和艰辛, tuy anh ấy đã trải qua những đau khổ và gian nan mà người thường khó chịu nổi. C, 在老家度过的每一天都很愉快, mỗi ngày sống ở quê đều rất vui."),
         F(1, "Câu một: 至今令人难以忘怀。 Đến nay vẫn khiến người ta khó mà quên được. Các bạn chọn vế nào?"),
         F(2, "Đáp án: C. 在老家度过的每一天都很愉快，至今令人难以忘怀。 Những ngày vui ở quê thì khó mà quên."),
         F(3, "Câu hai: 真是令人难以想象！ Thật khiến người ta khó mà tưởng tượng nổi!"),
         F(4, "Đáp án: A. 居然发生了这样的事情，真是令人难以想象！ Từ 居然 biểu thị bất ngờ, rất hợp với 难以想象."),
         F(5, "Câu ba: 他却从来没退缩过。 Nhưng anh ấy chưa bao giờ lùi bước."),
         F(6, "Đáp án: B. 虽然他经历了常人难以忍受的痛苦和艰辛，他却从来没退缩过。 Cặp 虽然 và 却 tạo thành quan hệ nhượng bộ. Các bạn để ý, cả ba câu đều có 令人难以 hoặc 常人难以, đây là những cách kết hợp rất hay gặp.")])

add("bullets", chapter="Ngữ pháp: 免得", section="Ngữ pháp 注释", title="3. 免得 miǎnde – để tránh, kẻo", size=36,
    items=["Liên từ: làm như vậy để tránh xảy ra một tình huống không mong muốn",
           "Thường đứng đầu vế sau · cũng nói 以免 (trang trọng hơn)",
           "今天大家晚点儿走，把活儿都干完，免得明天再来。",
           "自己能做的事就自己做吧，免得麻烦别人。",
           "他和妻子往返北极17次，支出很大，他们处处精打细算，千方百计节省开支，免得多年的储蓄减少得太快。"],
    say=["Điểm ngữ pháp thứ ba là liên từ 免得.",
         F(0, "免得 biểu thị làm việc ở vế trước là để tránh xảy ra một tình huống không mong muốn ở vế sau. Tiếng Việt dịch là để tránh, kẻo, đỡ phải."),
         F(1, "免得 thường đứng ở đầu vế câu phía sau. Cũng có thể nói 以免, với nghĩa tương tự nhưng trang trọng hơn, hay dùng trong văn viết."),
         F(2, "Ví dụ một: 今天大家晚点儿走，把活儿都干完，免得明天再来。 Hôm nay mọi người về muộn một chút, làm xong hết việc, để đỡ phải mai lại đến."),
         F(3, "Ví dụ hai: 自己能做的事就自己做吧，免得麻烦别人。 Việc gì mình làm được thì tự làm, kẻo làm phiền người khác."),
         F(4, "Ví dụ ba, lấy từ bài khóa: 他和妻子往返北极十七次，支出很大，他们处处精打细算，千方百计节省开支，免得多年的储蓄减少得太快。 Họ tiết kiệm đủ đường, để tránh khoản tiết kiệm bao năm vơi đi quá nhanh. Các bạn thấy đấy, vế sau 免得 luôn là điều người nói không muốn xảy ra.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: hoàn thành câu với 免得", reveal=True, size=38,
    items=["(1) 到了以后来个电话，免得……",
           "Đáp án: ……免得家里人担心。",
           "(2) 小声点儿，大伙儿都睡了，免得……",
           "Đáp án: ……免得把大家吵醒。",
           "(3) 麻烦你跟他解释清楚，免得……",
           "Đáp án: ……免得他误会。"],
    say=[F(0, "Luyện tập: hoàn thành câu. Câu một: 到了以后来个电话，免得…… Đến nơi thì gọi điện về nhé, kẻo làm sao? Các bạn tạm dừng và thử hoàn thành câu nhé."),
         F(1, "Đáp án gợi ý: 免得家里人担心。 Kẻo người nhà lo lắng."),
         F(2, "Câu hai: 小声点儿，大伙儿都睡了，免得…… Nói nhỏ thôi, mọi người ngủ cả rồi, kẻo làm sao?"),
         F(3, "Đáp án gợi ý: 免得把大家吵醒。 Kẻo đánh thức mọi người dậy. 吵醒 là làm ồn khiến người khác thức giấc."),
         F(4, "Câu ba: 麻烦你跟他解释清楚，免得…… Phiền bạn giải thích rõ với anh ấy, để tránh điều gì?"),
         F(5, "Đáp án gợi ý: 免得他误会。 Để tránh anh ấy hiểu lầm. Các bạn nhớ nhé: vế sau 免得 là điều không mong muốn, như lo lắng, đánh thức, hiểu lầm.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 鼓动 – 鼓励", section="Phân biệt từ 词语辨析", title="Phân biệt 鼓动 và 鼓励",
    common="Giống nhau: đều là động từ, dùng lời nói, chữ viết… khơi dậy cảm xúc, khiến người khác hành động. Ví dụ: 在朋友的鼓动/鼓励下，我走上舞台，完成了表演。",
    cols=[{"head": "鼓动",
           "lines": ["(1) Thiên về 发动: thúc giục, khích động người khác làm",
                     "(2) Hành động sau đó có thể tiêu cực → xúi giục",
                     "Đúng: 在他的鼓动下，那些人参加了非法组织。"]},
          {"head": "鼓励",
           "lines": ["(1) Thiên về 勉励: khích lệ, động viên",
                     "(2) Hành động sau đó luôn tích cực, không dùng cho việc xấu",
                     "Đúng: 父母鼓励他坚持下去，最后一定能取得成功。",
                     "Sai: 在他的鼓励下，那些人参加了非法组织。"]}],
    say=["Tiếp theo là phần phân biệt từ: 鼓动 và 鼓励. Hai từ này đều có chữ 鼓, nghĩa gốc là cái trống, đánh trống để thúc giục, nên học sinh rất hay dùng lẫn lộn.",
         "Điểm giống nhau: cả hai đều là động từ, đều chỉ việc dùng lời nói, chữ viết để khơi dậy cảm xúc, khiến người khác hành động. Ví dụ: 在朋友的鼓动下，我走上舞台，完成了表演, hoặc 在朋友的鼓励下, đều đúng. Được bạn bè khích lệ, tôi bước lên sân khấu và hoàn thành tiết mục biểu diễn.",
         F(0, "Điểm khác thứ nhất. 鼓动 thiên về nghĩa 发动, tức là thúc giục, khích động người khác đứng lên làm một việc gì đó."),
         F(0, "Điểm khác thứ hai, cũng là điểm quan trọng nhất: hành động sau 鼓动 có thể là hành động tiêu cực. Ví dụ: 在他的鼓动下，那些人参加了非法组织。 Dưới sự xúi giục của hắn, những người đó đã gia nhập tổ chức phi pháp. Lúc này tiếng Việt phải dịch là xúi giục."),
         F(1, "Còn 鼓励 thiên về nghĩa 勉励, tức là khích lệ, động viên, cổ vũ tinh thần cho người khác."),
         F(1, "Và hành động sau 鼓励 luôn là hành động tích cực, không thể là việc xấu. Ví dụ: 父母鼓励他坚持下去，最后一定能取得成功。 Bố mẹ động viên anh ấy kiên trì, cuối cùng nhất định sẽ thành công."),
         F(1, "Vì vậy câu 在他的鼓励下，那些人参加了非法组织 là sai, vì gia nhập tổ chức phi pháp là việc xấu, không thể dùng 鼓励."),
         "Mẹo nhớ: 鼓励 có chữ 励, như trong 勉励, nên luôn là động viên điều tốt; còn 鼓动 có chữ 动, chỉ thúc người ta hành động, tốt hay xấu đều được. Trong bài khóa, người vợ 鼓动 chồng đi Bắc Cực, nghĩa là thúc giục ông lên đường."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: Đúng hay sai?", reveal=True, size=36,
    items=["(1) 在她的鼓励下，我把唯一的一份工作也丢了。",
           "Đáp án: Sai – mất việc là kết quả xấu. Sửa: 在她的鼓动下……",
           "(2) 在我快要放弃时，朋友的鼓励给了我勇气。",
           "Đáp án: Đúng – được động viên để có dũng khí là việc tốt.",
           "(3) 他鼓动我买股票，结果赔得干干净净。",
           "Đáp án: Đúng – 鼓动 dùng được cho hành động có kết quả xấu.",
           "(4) 如果不是当初他鼓励我，我也不会像现在这么惨。",
           "Đáp án: Sai – kết quả rất thảm. Sửa: 如果不是当初他鼓动我……"],
    say=[F(0, "Bây giờ chúng ta làm thử: phán đoán đúng sai. Câu một: 在她的鼓励下，我把唯一的一份工作也丢了。 Được cô ấy khích lệ, tôi mất luôn cả công việc duy nhất. Đúng hay sai? Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: sai. Mất việc là một kết quả xấu, nên không dùng 鼓励. Phải sửa thành 在她的鼓动下, dưới sự xúi giục của cô ấy."),
         F(2, "Câu hai: 在我快要放弃时，朋友的鼓励给了我勇气。 Khi tôi sắp bỏ cuộc, sự động viên của bạn bè đã cho tôi dũng khí."),
         F(3, "Đáp án: đúng. Được động viên để có thêm dũng khí là việc tốt, dùng 鼓励 rất hợp."),
         F(4, "Câu ba: 他鼓动我买股票，结果赔得干干净净。 Anh ta xúi tôi mua cổ phiếu, kết quả lỗ sạch sành sanh."),
         F(5, "Đáp án: đúng. 鼓动 dùng được cho hành động dẫn đến kết quả xấu."),
         F(6, "Câu bốn: 如果不是当初他鼓励我，我也不会像现在这么惨。 Nếu ngày đó không phải anh ta khích lệ tôi, thì tôi cũng không thảm hại như bây giờ."),
         F(7, "Đáp án: sai. Kết quả rất thảm, nên phải dùng 鼓动: 如果不是当初他鼓动我，我也不会像现在这么惨。")])

# ======================= KỸ NĂNG: KỂ THEO TRÌNH TỰ THỜI GIAN =======================
add("bullets", chapter="Kỹ năng: kể theo trình tự thời gian", section="Kỹ năng 技能", title="Kể trải nghiệm theo trình tự thời gian", size=34,
    items=["Bài khóa kể cuộc đời Vương Kiến Nam theo trình tự thời gian, nhờ các từ ngữ chỉ thời gian nối các giai đoạn",
           "## Các mốc thời gian trong bài",
           "大学毕业做过…… · 50岁做了社长 → 就在……的时候，他毅然决定离开报社",
           "他先是……；不久……；再后来…… → 以前…… → 于是，他们出发了",
           "一路上…… → 到了北极…… → 从此……",
           "## Lợi ích: mạch kể rõ ràng, người đọc dễ theo dõi từng giai đoạn của câu chuyện"],
    say=["Bây giờ chúng ta sang phần kỹ năng. Quyển này không có mục tu từ riêng, nên thầy chọn một kỹ năng rất thực dụng từ bài tập bốn của sách: kể lại một trải nghiệm theo trình tự thời gian.",
         F(0, "Các bạn để ý, cả bài khóa kể lại cuộc đời của Vương Kiến Nam từ trẻ đến già. Người đọc không bị rối, là nhờ tác giả dùng rất nhiều từ ngữ chỉ thời gian để nối các giai đoạn với nhau."),
         F(1, "Chúng ta cùng tìm các mốc thời gian trong bài."),
         F(2, "Mở đầu: 大学毕业做过摄影记者, tốt nghiệp đại học thì làm phóng viên ảnh; 五十岁做了社长, năm mươi tuổi làm giám đốc. Rồi 就在王建男事业达到高峰的时候，他毅然决定离开报社, đúng lúc đang ở đỉnh cao thì ông rời đi."),
         F(3, "Tiếp theo là chuỗi 先是，不久，再后来: ba giai đoạn sau khi nghỉ việc. Rồi 以前他一直认为, trước đây ông vẫn nghĩ; và 于是，他们出发了, thế là họ lên đường."),
         F(4, "Sau đó là 一路上, suốt dọc đường; 到了北极, đến Bắc Cực; và 从此, từ đó trở đi. Mỗi từ ngữ này mở ra một cảnh mới của câu chuyện."),
         F(5, "Khi các bạn viết bài kể chuyện hoặc giới thiệu một người, hãy dùng những từ ngữ này để bài viết mạch lạc, người đọc dễ theo dõi.")])

add("bullets", section="Kỹ năng 技能", title="Mẫu 1: 先是……；不久……；再后来……", size=36,
    items=["先是 đầu tiên là · 不久 không lâu sau · 再后来 rồi về sau nữa",
           "Mỗi vế là một giai đoạn, các vế thường ngăn cách bằng dấu chấm phẩy (；)",
           "他先是办了家企业；不久他跨洋过海，到了加拿大；再后来，他恋上了北极。",
           "Cách nói tương tự: 起初……后来……最后…… · 先……然后……最后……",
           "她先是在中学当老师；不久去了一家出版社；再后来，她成了一名作家。"],
    say=[F(0, "Mẫu thứ nhất: 先是……；不久……；再后来……. 先是 nghĩa là đầu tiên là; 不久 là không lâu sau; 再后来 là rồi về sau nữa."),
         F(1, "Mỗi vế kể một giai đoạn. Vì các giai đoạn ngang hàng nhau, nên thường ngăn cách bằng dấu chấm phẩy."),
         F(2, "Câu trong bài khóa: 他先是办了家企业；不久他跨洋过海，到了加拿大；再后来，他恋上了北极。 Đầu tiên ông mở doanh nghiệp; không lâu sau vượt biển sang Canada; rồi về sau nữa, ông đem lòng yêu Bắc Cực. Chỉ một câu mà kể được cả mấy năm cuộc đời."),
         F(3, "Các bạn cũng có thể dùng những cách nói tương tự: 起初……后来……最后……, hoặc 先……然后……最后……."),
         F(4, "Ví dụ: 她先是在中学当老师；不久去了一家出版社；再后来，她成了一名作家。 Đầu tiên cô ấy làm giáo viên trung học; không lâu sau chuyển đến một nhà xuất bản; rồi về sau nữa, cô ấy trở thành nhà văn.")])

add("bullets", section="Kỹ năng 技能", title="Mẫu 2: kể một chuỗi việc làm hướng tới mục đích", size=34,
    items=["处处…… mọi mặt đều (thái độ chung)",
           "千方百计…… tìm đủ mọi cách (hành động cụ thể)",
           "免得…… để tránh (điều không mong muốn)",
           "即使……也…… cho dù… cũng… (nhấn mạnh quyết tâm)",
           "他们处处精打细算，千方百计节省开支，免得多年的储蓄减少得太快，即使穿越辽阔的无人区，他们也只租用最便宜的汽车。"],
    say=["Mẫu thứ hai cũng nằm trong bài tập bốn: kể một chuỗi việc làm để đạt một mục đích. Mỗi từ nối đảm nhận một vai trò riêng.",
         F(0, "处处, mọi nơi mọi mặt, nêu thái độ chung."),
         F(1, "千方百计, trăm phương nghìn kế, nêu hành động cụ thể."),
         F(2, "免得, để tránh, nêu điều không mong muốn, tức là lý do của những hành động ấy."),
         F(3, "即使……也……, cho dù… cũng…, đưa ra một ví dụ ở mức cao nhất, để nhấn mạnh quyết tâm."),
         F(4, "Câu trong bài: 他们处处精打细算，千方百计节省开支，免得多年的储蓄减少得太快，即使穿越辽阔的无人区，他们也只租用最便宜的汽车。 Các bạn thấy đấy, câu văn đi từ khái quát đến cụ thể, rồi kết bằng một ví dụ ấn tượng, nên rất có sức thuyết phục.")])

add("bullets", section="Kỹ năng 技能", title="Bài tập 4: Đọc đoạn văn, mô phỏng đặt câu", reveal=True, size=34,
    items=["(1) 大学毕业以后，他先是……；不久……；再后来，……。",
           "Đáp án: 大学毕业以后，他先是在一家小公司当职员；不久自己开了一家饭馆；再后来，他成了有名的老板。",
           "(2) 因为需要帮助的孩子很多，他们处处……，千方百计……，免得……，即使……，也……。",
           "Đáp án: ……他们处处节约，千方百计筹钱，免得孩子们失学，即使自己生活很困难，也坚持给孩子们寄钱。"],
    say=[F(0, "Bây giờ chúng ta làm bài tập bốn: mô phỏng đặt câu. Câu một: 大学毕业以后，他先是……；不久……；再后来，…… Sau khi tốt nghiệp đại học, đầu tiên anh ấy…, không lâu sau…, rồi về sau nữa…. Các bạn tạm dừng và thử viết nhé."),
         F(1, "Đáp án gợi ý: 大学毕业以后，他先是在一家小公司当职员；不久自己开了一家饭馆；再后来，他成了有名的老板。 Tốt nghiệp đại học, đầu tiên anh ấy làm nhân viên ở một công ty nhỏ; không lâu sau tự mở một quán ăn; rồi về sau nữa, anh ấy trở thành một ông chủ nổi tiếng."),
         F(2, "Câu hai: 因为需要帮助的孩子很多，他们处处……，千方百计……，免得……，即使……，也…… Vì có rất nhiều trẻ em cần giúp đỡ, họ… Các bạn thử viết tiếp nhé."),
         F(3, "Đáp án gợi ý: 他们处处节约，千方百计筹钱，免得孩子们失学，即使自己生活很困难，也坚持给孩子们寄钱。 Họ tiết kiệm mọi mặt, tìm mọi cách gom tiền, để các em khỏi phải bỏ học; cho dù bản thân sống rất khó khăn, họ vẫn kiên trì gửi tiền cho các em. 筹钱 là gom góp tiền, 失学 là thất học, phải nghỉ học.")])

add("bullets", section="Kỹ năng 技能", title="Luyện tập: điền 先是 · 不久 · 再后来 · 从此", reveal=True, size=36,
    items=["小李大学毕业后，(1)___在北京当了两年记者；(2)___他辞了职，回到家乡；(3)___，他在家乡开了一家咖啡馆。有一天，一位游客说他的咖啡是全城最好喝的，(4)___，他更加用心地经营这家小店。",
           "Đáp án: (1) 先是 · (2) 不久 · (3) 再后来 · (4) 从此"],
    say=[F(0, "Luyện tập thêm: điền 先是，不久，再后来，从此 vào chỗ trống. 小李大学毕业后，什么在北京当了两年记者；什么他辞了职，回到家乡；什么，他在家乡开了一家咖啡馆。有一天，一位游客说他的咖啡是全城最好喝的，什么，他更加用心地经营这家小店。 Các bạn tạm dừng và điền thử nhé."),
         F(1, "Đáp án: 小李大学毕业后，先是在北京当了两年记者；不久他辞了职，回到家乡；再后来，他在家乡开了一家咖啡馆。有一天，一位游客说他的咖啡是全城最好喝的，从此，他更加用心地经营这家小店。 Tiểu Lý tốt nghiệp đại học, đầu tiên làm phóng viên ở Bắc Kinh hai năm; không lâu sau thì nghỉ việc về quê; rồi về sau nữa, anh mở một quán cà phê ở quê. Một hôm, một du khách nói cà phê của anh ngon nhất thành phố, từ đó anh càng tận tâm với quán nhỏ của mình."),
         "Các bạn để ý: 从此 dùng sau một sự kiện cụ thể, chỉ sự thay đổi kéo dài từ thời điểm đó về sau, giống như trong bài khóa: 从此，王建男不再在意自然风光."])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ có dấu chấm", size=40,
    items=["专题 (题) → 话题 · 主题 · 问题 · 题目",
           "北极 (极) → 南极 · 极地 · 极点 · 极限 · 积极 · 消极",
           "开拓 (开) → 开发 · 开放 · 开辟 · 开展 · 开设 · 开创",
           "释放 (放) → 放松 · 放弃 · 放心 · 解放 · 发放 · 放假",
           "鼓动 (鼓) → 鼓励 · 鼓舞 · 鼓掌 · 打鼓 · 鼓足 · 鼓起"],
    say=["Phần luyện tập. Bài tập một: mô phỏng ví dụ, viết thêm các từ có chứa chữ được đánh dấu chấm.",
         F(0, "Ví dụ mẫu: 专题, chữ được đánh dấu là chữ 题, nghĩa là đề, đề tài. Ta có 话题，主题，问题，题目. Tức là chủ đề câu chuyện, chủ đề, vấn đề, và đề bài."),
         F(1, "北极, chữ được đánh dấu là chữ 极, nghĩa là cực, điểm tận cùng. Ta có 南极，极地，极点，极限，积极，消极. Tức là Nam Cực, vùng cực, cực điểm, giới hạn, tích cực, và tiêu cực."),
         F(2, "开拓, chữ được đánh dấu là chữ 开, nghĩa là mở. Ta có 开发，开放，开辟，开展，开设，开创. Tức là khai phát, mở cửa, khai phá, triển khai, mở ra, và khai sáng."),
         F(3, "释放, chữ được đánh dấu là chữ 放, nghĩa là thả, buông. Ta có 放松，放弃，放心，解放，发放，放假. Tức là thả lỏng, từ bỏ, yên tâm, giải phóng, phát cho, và nghỉ lễ."),
         F(4, "鼓动, chữ được đánh dấu là chữ 鼓, nghĩa gốc là trống, đánh trống để cổ vũ. Ta có 鼓励，鼓舞，鼓掌，打鼓，鼓足，鼓起. Tức là khích lệ, cổ vũ, vỗ tay, đánh trống, dồn hết, và lấy hết, như 鼓起勇气, lấy hết can đảm.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (1)", reveal=True, size=36,
    items=["(1) 看到祖国需要自己，他毫不犹豫地回国了。（毅然）",
           "Đáp án: 看到祖国需要自己，他毅然回国了。",
           "(2) 走自己的路，别在乎其他人怎么说。（在意）",
           "Đáp án: 走自己的路，别在意其他人怎么说。",
           "(3) 为了不引起误会，我再多说几句。（免得）",
           "Đáp án: 我再多说几句，免得引起误会。"],
    say=[F(0, "Bài tập hai: dùng từ cho sẵn để viết lại câu. Câu một, dùng 毅然: 看到祖国需要自己，他毫不犹豫地回国了。 Thấy tổ quốc cần mình, anh ấy không chút do dự trở về nước. Các bạn tạm dừng và thử viết lại nhé."),
         F(1, "Đáp án: 看到祖国需要自己，他毅然回国了。 Thay 毫不犹豫地 bằng 毅然, vì 毅然 chính là kiên quyết, không chút do dự."),
         F(2, "Câu hai, dùng 在意: 走自己的路，别在乎其他人怎么说。 Hãy đi con đường của mình, đừng bận tâm người khác nói gì."),
         F(3, "Đáp án: 走自己的路，别在意其他人怎么说。 在乎 và 在意 gần nghĩa nhau, đều hay dùng trong câu phủ định."),
         F(4, "Câu ba, dùng 免得: 为了不引起误会，我再多说几句。 Để không gây hiểu lầm, tôi nói thêm mấy câu."),
         F(5, "Đáp án: 我再多说几句，免得引起误会。 Chú ý vị trí: 为了 đứng ở vế trước, còn 免得 phải chuyển xuống đầu vế sau.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (2)", reveal=True, size=36,
    items=["(4) 知道我一个人在异国他乡，他常常打电话问候我。（时常）",
           "Đáp án: 知道我一个人在异国他乡，他时常打电话问候我。",
           "(5) 条件有限，招待不周，你们凑合着住两天吧。（将就）",
           "Đáp án: 条件有限，招待不周，你们将就着住两天吧。",
           "(6) 做点儿你能做的事情吧，难度太大的就不要做了。（力所能及）",
           "Đáp án: 做点儿力所能及的事情吧，难度太大的就不要做了。"],
    say=[F(0, "Câu bốn, dùng 时常: 知道我一个人在异国他乡，他常常打电话问候我。 Biết tôi một mình nơi đất khách quê người, anh ấy thường gọi điện hỏi thăm tôi."),
         F(1, "Đáp án: thay 常常 bằng 时常: 他时常打电话问候我。"),
         F(2, "Câu năm, dùng 将就: 条件有限，招待不周，你们凑合着住两天吧。 Điều kiện có hạn, tiếp đãi không chu đáo, các bạn ở tạm vài hôm nhé."),
         F(3, "Đáp án: 你们将就着住两天吧。 凑合 và 将就 đều là tạm chấp nhận, ở đây có thể thay cho nhau."),
         F(4, "Câu sáu, dùng 力所能及: 做点儿你能做的事情吧，难度太大的就不要做了。 Hãy làm những việc bạn làm được thôi, việc quá khó thì đừng làm."),
         F(5, "Đáp án: 做点儿力所能及的事情吧，难度太大的就不要做了。 力所能及的事情 chính là những việc vừa sức mình.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (1)", reveal=True, size=34,
    items=["## Từ cho sẵn: 毅然 · 捆绑 · 在意 · 支配 · 疲惫",
           "现代人生活、工作压力都很大，被事业、家庭___着，身心___。但大部分人很___自己已有的一切，没有勇气离开固有的生活圈子。只有少数人会___决定换一种生活方式，做自己愿意做的事情，自己___自己的时间和生命。",
           "Đáp án: 捆绑 · 疲惫 · 在意 · 毅然 · 支配"],
    say=[F(0, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn một có năm từ: 毅然，捆绑，在意，支配，疲惫."),
         F(1, "现代人生活、工作压力都很大，被事业、家庭什么着，身心什么。但大部分人很什么自己已有的一切，没有勇气离开固有的生活圈子。只有少数人会什么决定换一种生活方式，做自己愿意做的事情，自己什么自己的时间和生命。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 被事业、家庭捆绑着，身心疲惫，很在意自己已有的一切，毅然决定换一种生活方式，自己支配自己的时间和生命。 Người hiện đại áp lực rất lớn, bị sự nghiệp và gia đình trói buộc, thân tâm mệt mỏi. Nhưng phần lớn mọi người rất coi trọng những gì mình đang có, không đủ dũng khí rời khỏi vòng sống quen thuộc. Chỉ số ít người kiên quyết đổi một lối sống khác, tự mình làm chủ thời gian và cuộc đời mình. Đoạn văn này nói đúng về Vương Kiến Nam trong bài khóa.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (2)", reveal=True, size=34,
    items=["## Từ cho sẵn: 灾难 · 记载 · 刻不容缓 · 抢救 · 捕捉",
           "由于环境污染、全球变暖和人类无节制的___动物，世界上动物的种类正日益减少，很多动物种群面临___性的毁灭。有些动物，我们的后代可能只有在文字___中去了解了。因此，___正在消失的珍稀动物___。",
           "Đáp án: 捕捉 · 灾难 · 记载 · 抢救 · 刻不容缓"],
    say=[F(0, "Đoạn hai có năm từ: 灾难，记载，刻不容缓，抢救，捕捉."),
         F(1, "由于环境污染、全球变暖和人类无节制的什么动物，世界上动物的种类正日益减少，很多动物种群面临什么性的毁灭。有些动物，我们的后代可能只有在文字什么中去了解了。因此，什么正在消失的珍稀动物什么。 Các bạn điền thử nhé."),
         F(2, "Đáp án: 人类无节制的捕捉动物，面临灾难性的毁灭，只有在文字记载中去了解，抢救正在消失的珍稀动物刻不容缓。 Do ô nhiễm môi trường, Trái Đất nóng lên và việc con người săn bắt động vật không kiểm soát, số loài động vật đang ngày càng giảm, nhiều quần thể đứng trước nguy cơ bị hủy diệt thảm khốc. Có những loài mà con cháu chúng ta có lẽ chỉ còn biết qua sách vở. Vì vậy, cứu lấy những loài quý hiếm đang biến mất là việc không thể chậm trễ."),
         "Các bạn để ý: 灾难性 là mang tính thảm họa, chữ 性 biến danh từ thành tính từ. Và 刻不容缓 đứng ở cuối câu làm vị ngữ, giống hệt câu trong bài khóa."])

add("bullets", section="Luyện tập 练习", title="Mở rộng 扩展: các cặp từ trái nghĩa", size=34,
    items=["贬低 – 抬高 hạ thấp – đề cao · 贬义 – 褒义 nghĩa xấu – nghĩa tốt",
           "稠密 – 稀疏 dày đặc – thưa thớt · 丑恶 – 美好 xấu xa – tốt đẹp",
           "反面 – 正面 mặt trái – mặt phải · 放大 – 缩小 phóng to – thu nhỏ",
           "奉献 – 索取 cống hiến – đòi hỏi · 宏观 – 微观 vĩ mô – vi mô",
           "全局 – 局部 toàn cục – cục bộ · 上级 – 下级 cấp trên – cấp dưới",
           "上游 – 下游 thượng nguồn – hạ nguồn · 压缩 – 扩张 thu hẹp – mở rộng",
           "油腻 – 清淡 béo ngậy – thanh đạm · 自卑 – 自信 tự ti – tự tin",
           "固体 – 液体 chất rắn – chất lỏng · 外向 – 内向 hướng ngoại – hướng nội"],
    say=["Phần mở rộng của sách giới thiệu mười sáu cặp từ trái nghĩa. Thầy đọc qua để các bạn làm quen; học từ theo cặp trái nghĩa giúp nhớ nhanh gấp đôi đấy.",
         F(0, "贬低，抬高: hạ thấp và đề cao. 贬义，褒义: nghĩa xấu và nghĩa tốt, như từ 鼓动 đôi khi mang nghĩa xấu, còn 鼓励 luôn mang nghĩa tốt."),
         F(1, "稠密，稀疏: dày đặc và thưa thớt, như dân cư đông đúc hay thưa thớt. 丑恶，美好: xấu xa và tốt đẹp."),
         F(2, "反面，正面: mặt trái và mặt phải. 放大，缩小: phóng to và thu nhỏ."),
         F(3, "奉献，索取: cống hiến và đòi hỏi, cho đi và lấy về. 宏观，微观: vĩ mô và vi mô."),
         F(4, "全局，局部: toàn cục và cục bộ. 上级，下级: cấp trên và cấp dưới."),
         F(5, "上游，下游: thượng nguồn và hạ nguồn của con sông. 压缩，扩张: thu hẹp và mở rộng."),
         F(6, "油腻，清淡: béo ngậy và thanh đạm, nói về món ăn. 自卑，自信: tự ti và tự tin."),
         F(7, "固体，液体: chất rắn và chất lỏng. 外向，内向: hướng ngoại và hướng nội. Các bạn hãy thử đặt câu với từng cặp từ nhé, ví dụ: 他性格外向，他妹妹却很内向。")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 14", size=34,
    items=["Từ vựng trọng tâm: 毅然 · 疲惫 · 力所能及 · 开拓 · 鼓动 · 遭遇 · 灾难 · 惊奇 · 冲动 · 在意 · 刻不容缓 · 精打细算 · 免得 · 将就 · 支配 · 执着",
           "Ngữ pháp: lượng từ lặp lại 一拨拨 (từng… một, nhiều) · 难以 (khó mà) · 免得 (để tránh, kẻo)",
           "Phân biệt: 鼓动 (thúc giục, có thể là việc xấu) ≠ 鼓励 (động viên, luôn là việc tốt)",
           "Kỹ năng: kể theo trình tự thời gian 先是……不久……再后来…… · 处处……千方百计……免得……",
           "## Bài tập về nhà (运用)",
           "Dựa vào bài tập 5, tóm tắt bài khóa thành một đoạn văn khoảng 400 chữ"],
    say=["Chúng ta cùng tổng kết bài mười bốn.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 毅然，疲惫，力所能及，开拓，鼓动，遭遇，灾难，惊奇，冲动，在意，刻不容缓，精打细算，免得，将就，支配，执着. Và đừng quên những từ dễ nhầm như 访问，头脑，遭遇，灾难，执着."),
         F(1, "Về ngữ pháp: cụm số lượng lặp lại như 一拨拨，一件件, miêu tả số lượng nhiều, hiện ra từng cái một. 难以 nghĩa là khó mà, đi với từ hai âm tiết trở lên. 免得 đứng đầu vế sau, nghĩa là để tránh điều không mong muốn."),
         F(2, "Về phân biệt từ: 鼓动 là thúc giục người khác hành động, hành động đó có thể là việc xấu; còn 鼓励 là động viên, khích lệ, luôn là việc tốt."),
         F(3, "Về kỹ năng: kể trải nghiệm theo trình tự thời gian với 先是，不久，再后来，从此; và kể chuỗi việc làm với 处处，千方百计，免得，即使……也……."),
         F(5, "Bài tập về nhà, theo phần vận dụng của sách: bài khóa kể lại những trải nghiệm của Vương Kiến Nam sau khi tốt nghiệp, từ thành công trong sự nghiệp, đến kiên quyết từ chức, rồi đem lòng yêu Bắc Cực. Câu chuyện ấy khiến chúng ta suy nghĩ: 我们究竟为了什么活着？ Rốt cuộc chúng ta sống vì điều gì? Hãy tham khảo bài tập năm, tóm tắt bài khóa thành một đoạn văn khoảng bốn trăm chữ. Nhớ thử dùng 先是，不久，再后来，难以，免得 trong bài viết nhé."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Mong rằng, giống như Vương Kiến Nam, các bạn cũng tìm được điều mình thật sự yêu thích và kiên trì theo đuổi nó. Hẹn gặp lại các bạn ở bài mười lăm: 山脉上的雕刻, Các tác phẩm điêu khắc trên dãy núi. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Thượng) – Bài 14: 背着电饭锅拍北极 (Vác nồi cơm điện đi chụp ảnh Bắc Cực)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"背着": "杯着",            # bēizhe
                    "社长": "社涨",            # shèzhǎng
                    "同行": "同杭",            # tóngháng (người cùng ngành)
                    "长矛": "常矛",            # chángmáo
                    "记载": "记宰",            # jìzǎi
                    "差别": "插别",            # chābié
                    "差距": "插距",            # chājù
                    "差异": "插异",            # chāyì
                    "差价": "插价",            # chājià
                    "反差": "反插",            # fǎnchā
                    "色差": "色插",            # sèchā
                    "温差": "温插",            # wēnchā
                    "时差": "时插",            # shíchā
                    "相差": "相岔",            # xiāngchà
                    "血统": "谑统",            # xuètǒng
                    "处处": "触触",            # chùchù
                    "将就": "江就",            # jiāngjiu
                    "执着": "执酌",            # zhízhuó
                    "为历史": "位历史",        # wèi
                    "重叠": "虫叠",            # chóngdié
                    "调查": "掉查",            # diàochá
                    "干完": "赣完",            # gànwán
                    "干干净净": "甘甘净净",    # gāngānjìngjìng
                    "山脉": "山卖"},           # shānmài
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai14.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
