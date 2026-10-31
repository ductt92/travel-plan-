#!/usr/bin/env python3
"""Kịch bản bài giảng 顶石中文 – Bài 2.3 «群体性孤独：网络社交正在扼杀深度关系». Chạy để sinh ds23.json."""
import json
import os

TAG = "顶石中文 · Bài 2.3 · 群体性孤独：网络社交正在扼杀深度关系"
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
    zh="群体性孤独", py="网络社交正在扼杀深度关系",
    vi="Bài 2.3: Cô đơn tập thể",
    sub="Qúntǐxìng gūdú: wǎngluò shèjiāo zhèngzài èshā shēndù guānxi\nBài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn trở lại với bài giảng giáo trình 顶石中文, Đỉnh cao tiếng Trung.",
         "Hôm nay chúng ta học bài hai chấm ba, bài cuối cùng của Đơn vị hai, chủ đề 时代篇, Thời đại: 群体性孤独：网络社交正在扼杀深度关系。 Nghĩa là: Cô đơn tập thể: mạng xã hội đang bóp chết những mối quan hệ sâu sắc.",
         "Bài khóa xuất phát từ một chức năng mới của WeChat: vòng bạn bè, 朋友圈, có thể cài đặt chỉ hiển thị trong ba ngày, hay một tháng. Vì sao ngày càng nhiều người muốn trốn khỏi vòng bạn bè? Vì sao công nghệ càng tiện lợi, con người lại càng xa cách? Bài viết dựa trên cuốn sách 群体性孤独, Cô đơn tập thể, của nhà xã hội học Mỹ Sherry Turkle.",
         "Cuối bài, chúng ta sẽ có thêm một phần ôn tập toàn bộ Đơn vị hai, theo mục 单元练习 của sách. Đây là một bài rất gần gũi với cuộc sống của mỗi chúng ta, những người ngày nào cũng lướt Facebook, Zalo hay WeChat."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài báo: “cô đơn tập thể” và ba ảo giác của mạng xã hội",
           "Nắm vững 46 từ mới và thành ngữ, kèm âm Hán Việt và ví dụ",
           "Câu mẫu: 与……形成对比的是 · 说白了 · 说到底 · 比起……更…… · 半A不B · 不在少数 · 白白 · 把A与B划等号 · 在……的同时，更要……",
           "Kết hợp từ (词语搭配): 扼杀 · 不堪 · 挖掘 · 错觉 · 排解 · 剥夺",
           "Luyện tập, thảo luận và ôn tập Đơn vị 2 (单元练习): viết bài bàn về lợi và hại"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài báo: thế nào là cô đơn tập thể, mạng xã hội tạo ra những ảo giác gì, và vì sao nó đang bóp chết các mối quan hệ sâu sắc."),
         F(1, "Thứ hai, nắm vững bốn mươi sáu từ mới và thành ngữ, với rất nhiều từ của mạng xã hội như 热搜，屏蔽，拉黑，秒回，流量."),
         F(2, "Thứ ba, học chín câu mẫu trọng điểm, nhiều câu rất khẩu ngữ, như 说白了, nói trắng ra; 说到底, suy cho cùng; 半生不熟, nửa sống nửa chín."),
         F(3, "Thứ tư, học cách kết hợp từ: 扼杀个性，不堪重负，挖掘潜能，产生错觉，排解孤独，剥夺权利."),
         F(4, "Thứ năm, làm bài tập, thảo luận, rồi ôn tập cả Đơn vị hai, đặc biệt là cách viết một bài văn bàn về lợi và hại. Các bạn chuẩn bị giấy bút nhé.")])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 课前思考", title="Câu hỏi trước bài (课前思考)", size=40,
    items=["1. 你更喜欢网络社交还是面对面交流？为什么？",
           "2. 你每天在社交媒体上花多少时间？",
           "3. 如果没有线上社交，你是否感到孤独？",
           "Gợi ý: Facebook · Zalo · TikTok · WeChat (微信) · 朋友圈 – vòng bạn bè"],
    say=["Chúng ta bắt đầu với ba câu hỏi trước bài.",
         F(0, "Câu một: 你更喜欢网络社交还是面对面交流？为什么？ Bạn thích giao tiếp trên mạng hay trò chuyện trực tiếp hơn? Vì sao? 网络社交 là giao tiếp xã hội qua mạng; 面对面 là mặt đối mặt."),
         F(1, "Câu hai: 你每天在社交媒体上花多少时间？ Mỗi ngày bạn dành bao nhiêu thời gian cho mạng xã hội? 社交媒体 là mạng xã hội, truyền thông xã hội."),
         F(2, "Câu ba: 如果没有线上社交，你是否感到孤独？ Nếu không có giao tiếp trực tuyến, bạn có cảm thấy cô đơn không? 线上 là trên mạng, trực tuyến; đối lại là 线下, ngoài đời thực."),
         F(3, "Ở Việt Nam, chúng ta dùng Facebook, Zalo, TikTok; còn ở Trung Quốc, ứng dụng phổ biến nhất là WeChat, 微信. Chức năng 朋友圈, vòng bạn bè, của WeChat giống như trang cá nhân trên Facebook, nơi mọi người đăng ảnh và trạng thái. Các bạn tạm dừng video và thử trả lời bằng tiếng Trung nhé.")])

add("bullets", section="Khởi động 课前思考", title="Bối cảnh (注释)", size=35,
    items=["## 张小龙 – “微信之父”, cha đẻ của WeChat",
           "Phó chủ tịch cấp cao của Tencent (腾讯); từng phát triển Foxmail. 朋友圈 là một chức năng mạng xã hội của WeChat",
           "## 《群体性孤独》 Alone Together – Sherry Turkle (雪莉·特克尔)",
           "Bản tiếng Trung xuất bản năm 2014; bàn về ảnh hưởng tâm lý tiêu cực của công nghệ thông tin, tập trung vào “thổ dân điện tử” (电子土著)",
           "## 我分享故我在 – “Tôi chia sẻ, vậy tôi tồn tại”",
           "Biến tấu câu nổi tiếng của Descartes 我思故我在 – “Tôi tư duy, vậy tôi tồn tại”"],
    say=["Trước khi học từ mới, chúng ta xem ba chú thích của sách.",
         F(0, "Một: 张小龙, người được gọi là 微信之父, cha đẻ của WeChat."),
         F(1, "Ông tốt nghiệp Đại học Khoa học Kỹ thuật Hoa Trung, là phó chủ tịch cấp cao của tập đoàn 腾讯, Tencent. Trước đó ông phát triển phần mềm thư điện tử Foxmail, sau khi về Tencent thì tạo ra WeChat. 朋友圈 là một chức năng mạng xã hội của WeChat."),
         F(2, "Hai: cuốn sách 群体性孤独, tên tiếng Anh là Alone Together, nghĩa là ở bên nhau mà vẫn cô đơn, của giáo sư Sherry Turkle, Học viện Công nghệ Massachusetts."),
         F(3, "Bản tiếng Trung xuất bản năm hai nghìn không trăm mười bốn. Cuốn sách tập trung vào thế hệ trẻ lớn lên cùng điện thoại và đồ chơi điện tử, mà sách gọi là 电子土著, thổ dân điện tử. Tác giả rất lo ngại về ảnh hưởng tiêu cực của công nghệ thông tin đến tâm lý xã hội của con người."),
         F(4, "Ba: 我分享故我在, tôi chia sẻ, vậy tôi tồn tại."),
         F(5, "Câu này biến tấu từ câu danh ngôn của triết gia Pháp Descartes: 我思故我在, tôi tư duy, vậy tôi tồn tại. Chữ 故 là cho nên, văn ngôn. Ý nói: trong thế giới mạng, chia sẻ trạng thái trở thành cách để con người tìm kiếm cảm giác mình đang tồn tại.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("扼杀", "èshā", "ách sát", "động từ", "bóp chết, bóp nghẹt, kìm hãm", "不要扼杀孩子的想象力。", "Đừng bóp chết trí tưởng tượng của trẻ.",
     "Động từ. Nghĩa gốc là bóp cổ cho chết; nghĩa bóng là chèn ép, vùi dập khiến một thứ không thể tồn tại hay phát triển. Chữ 扼 là bóp chặt, như trong 扼要, tóm tắt cái then chốt. Tên bài: 网络社交正在扼杀深度关系."),
    ("前阵子", "qiánzhènzi", "tiền trận tử", "danh từ", "dạo trước, thời gian vừa rồi", "前阵子我去了一趟上海。", "Dạo trước tôi có đi Thượng Hải một chuyến.",
     "Danh từ khẩu ngữ, chỉ khoảng thời gian vừa mới qua. 阵子 là một khoảng thời gian; tương tự có 这阵子, dạo này. Câu đầu bài khóa: 前阵子，微信悄悄上线了一项新功能."),
    ("上线", "shàngxiàn", "thượng tuyến", "động từ", "ra mắt, đưa vào hoạt động (sản phẩm trên mạng)", "这款新游戏下个月上线。", "Trò chơi mới này sẽ ra mắt vào tháng sau.",
     "Động từ, nghĩa là sản phẩm Internet bắt đầu được vận hành, đưa đến người dùng. Ngoài ra 上线 còn nghĩa là vào mạng, online. Trong bài: 微信悄悄上线了一项新功能, WeChat lặng lẽ tung ra một chức năng mới."),
    ("热搜", "rèsōu", "nhiệt sưu", "danh từ", "tìm kiếm nóng, chủ đề được tìm nhiều nhất", "这条新闻很快就上了热搜。", "Tin tức này nhanh chóng lên top tìm kiếm.",
     "Danh từ, chỉ những sự kiện, chủ đề được nhiều người tìm kiếm, bàn luận nhất trong một thời gian, thường là bảng chủ đề nóng của Weibo. Cụm hay gặp: 上热搜, lên top tìm kiếm, tương tự lên trending."),
    ("当下", "dāngxià", "đương hạ", "danh từ", "hiện nay, lúc này, ở đây", "活在当下，珍惜眼前的人。", "Hãy sống cho hiện tại, trân trọng người trước mắt.",
     "Danh từ, nghĩa là lúc này và nơi này, hiện nay. Câu rất phổ biến: 活在当下, sống trọn hiện tại. Trong bài: 在越来越多人逃离朋友圈的当下, vào lúc ngày càng nhiều người trốn chạy khỏi vòng bạn bè."),
    ("解读", "jiědú", "giải độc", "động từ", "giải thích, phân tích, giải mã", "专家正在解读最新的经济数据。", "Các chuyên gia đang phân tích số liệu kinh tế mới nhất.",
     "Động từ, nghĩa là đọc và giải thích, phân tích nghiên cứu: 解读信息，解读新形势, 解读政策. Chú ý chữ 读 là đọc, không liên quan đến độc hại. Trong bài: 如何解读虚拟社交, phải hiểu giao tiếp ảo như thế nào."),
    ("虚拟", "xūnǐ", "hư nghĩ", "tính từ", "ảo, hư cấu", "网络是一个虚拟世界。", "Mạng Internet là một thế giới ảo.",
     "Nghĩa là không phù hợp hoặc không chắc phù hợp với sự thật; ở đây chỉ thế giới do mạng tạo ra. Kết hợp hay gặp: 虚拟世界，虚拟社交，虚拟现实. Bảng từ của sách xếp từ này là danh từ, nhưng thường dùng như tính từ."),
    ("业绩", "yèjì", "nghiệp tích", "danh từ", "thành tích (công việc), kết quả kinh doanh", "他今年的销售业绩非常好。", "Năm nay thành tích bán hàng của anh ấy rất tốt.",
     "Danh từ, nghĩa là thành tích, kết quả của công việc. Kết hợp hay gặp: 销售业绩，辉煌的业绩，业绩报告. Trong bài: 腾讯发布的业绩报告, báo cáo kết quả kinh doanh do Tencent công bố."),
    ("不堪", "bùkān", "bất kham", "động từ", "không chịu nổi", "这样的日子实在是不堪忍受。", "Những ngày như thế này thật không chịu đựng nổi.",
     "Động từ, nghĩa là không chịu đựng nổi. Chữ 堪 là chịu được. Kết hợp hay gặp: 不堪重负，不堪忍受，不堪回首，不堪一击. Chúng ta sẽ học kỹ ở phần kết hợp từ."),
    ("重负", "zhòngfù", "trọng phụ", "danh từ", "gánh nặng", "听到这个消息，他如释重负。", "Nghe tin này, anh ấy như trút được gánh nặng.",
     "Danh từ, nghĩa là gánh nặng. Hai cụm cố định: 如释重负, như trút được gánh nặng; 不堪重负, không chịu nổi gánh nặng, như trong bài: 又让人感到不堪重负."),
    ("屏蔽", "píngbì", "bình tế", "động từ", "chặn, ẩn (không cho xem)", "我屏蔽了他的朋友圈。", "Tôi đã ẩn vòng bạn bè của anh ta.",
     "Động từ, nghĩa gốc là che chắn; ở đây chỉ việc ẩn vòng bạn bè của mình để người khác không thấy, hoặc chặn không xem bài của người khác. Cũng dùng cho 屏蔽广告, chặn quảng cáo."),
    ("波澜", "bōlán", "ba lan", "danh từ", "sóng lớn; (bóng) sự xao động trong lòng", "听到这个消息，她内心毫无波澜。", "Nghe tin ấy, lòng cô ấy chẳng chút gợn sóng.",
     "Danh từ, nghĩa gốc là sóng to; ở đây ví với phản ứng tâm lý. Cụm rất hay dùng trên mạng: 内心毫无波澜, trong lòng không một gợn sóng, tức là dửng dưng."),
    ("愈加", "yùjiā", "dũ gia", "phó từ", "càng thêm, càng", "他的病情愈加严重了。", "Bệnh tình của ông ấy càng thêm nặng.",
     "Nghĩa là càng thêm, càng hơn, văn viết, giống 更加 và 越发. Sách xếp là tính từ, nhưng cách dùng là đứng trước tính từ như phó từ: 愈加聪明，愈加理性. Trong bài có cặp đối: 科技愈加便利，彼此交往却愈加疏远."),
    ("挖掘", "wājué", "oạt quật", "động từ", "đào; (bóng) khai thác, tìm ra", "记者努力挖掘事件的真相。", "Phóng viên ra sức tìm ra sự thật của vụ việc.",
     "Động từ, các bạn đã học nghĩa đen là đào bới ở HSK sáu. Ở đây dùng nghĩa bóng: đi sâu khai thác, tìm tòi: 挖掘真相，挖掘潜力，挖掘根源. Trong bài: 挖掘了互联网时代群体孤独的根源."),
    ("根源", "gēnyuán", "căn nguyên", "danh từ", "căn nguyên, nguồn gốc", "我们要找到问题的根源。", "Chúng ta phải tìm ra căn nguyên của vấn đề.",
     "Danh từ, nghĩa là nguyên nhân gốc rễ làm nảy sinh sự vật. Âm Hán Việt và nghĩa giống tiếng Việt."),
    ("重构", "chónggòu", "trùng cấu", "động từ", "tái cấu trúc, xây dựng lại", "互联网重构了人与人之间的关系。", "Internet đã tái cấu trúc mối quan hệ giữa người với người.",
     "Động từ, nghĩa là sắp xếp, tổ chức lại cấu trúc cũ. Chữ 重 ở đây đọc chóng, nghĩa là lại, lần nữa. Trong bài: 也重构了以往的人际关系."),
    ("小圈子", "xiǎoquānzi", "tiểu khuyên tử", "danh từ", "nhóm nhỏ, vòng nhỏ; bè phái", "在公司里不要搞小圈子。", "Ở công ty đừng kéo bè kéo cánh.",
     "Danh từ, nghĩa là phạm vi sống nhỏ hẹp, hoặc nhóm nhỏ lôi kéo nhau vì lợi ích riêng, như trong 搞小圈子, kéo bè kéo cánh. Trong bài dùng nghĩa trung tính: 建立线上的虚拟小圈子, lập những nhóm nhỏ ảo trên mạng."),
    ("伪装", "wěizhuāng", "ngụy trang", "động từ", "giả làm, ngụy trang", "警察识破了犯罪分子的伪装。", "Cảnh sát đã nhìn thấu sự ngụy trang của tên tội phạm.",
     "Động từ, nghĩa là giả vờ, giả làm; cũng làm danh từ, nghĩa là sự ngụy trang. Mẫu: 把自己伪装成……, giả làm…. Trong bài: 甚至可以把自己伪装成想成为的任何人, thậm chí có thể giả làm bất cứ ai mình muốn trở thành."),
    ("客体", "kètǐ", "khách thể", "danh từ", "khách thể, đối tượng", "在认识过程中，人是主体，世界是客体。", "Trong quá trình nhận thức, con người là chủ thể, thế giới là khách thể.",
     "Danh từ, thuật ngữ triết học, chỉ sự vật khách quan tồn tại bên ngoài chủ thể. Đối lập là 主体, chủ thể. Trong bài: 把每个人简化成实用的客体, giản lược mỗi con người thành một đối tượng để sử dụng."),
    ("隐匿", "yǐnnì", "ẩn nặc", "động từ", "che giấu, giấu giếm", "他隐匿了事情的真相。", "Anh ta đã che giấu sự thật của sự việc.",
     "Động từ, văn viết, nghĩa là giấu giếm, ẩn giấu: 隐匿实情, giấu sự thật. Trong bài: 真实的缺点却被隐匿了, khuyết điểm thật lại bị giấu đi."),
    ("错觉", "cuòjué", "thác giác", "danh từ", "ảo giác, cảm giác sai lầm", "这只是你的错觉。", "Đó chỉ là cảm giác sai của bạn thôi.",
     "Danh từ, nghĩa là cảm nhận không đúng về sự vật khách quan. Chữ 错 là sai, 觉 là cảm giác. Kết hợp hay gặp: 产生错觉. Trong bài: 虚拟社交制造出的三大错觉, ba ảo giác lớn do giao tiếp ảo tạo ra."),
    ("倾听", "qīngtīng", "khuynh thính", "động từ", "lắng nghe", "好的老师懂得倾听学生的想法。", "Người thầy giỏi biết lắng nghe suy nghĩ của học trò.",
     "Động từ, nghĩa là chăm chú lắng nghe; sách ghi thường dùng cho người trên nghe người dưới, nhưng ngày nay dùng rất rộng: 倾听他人. Chữ 倾 là nghiêng: nghiêng người về phía trước để nghe. Trong bài: 幻想总有人倾听我们."),
    ("束缚", "shùfù", "thúc phược", "động từ", "trói buộc, ràng buộc", "不要被小事束缚住手脚。", "Đừng để những chuyện nhỏ trói buộc chân tay.",
     "Động từ, nghĩa là ràng buộc, hạn chế. Cũng làm danh từ: 摆脱束缚, thoát khỏi ràng buộc. Trong bài: 因为讨厌被真实关系束缚, vì ghét bị các mối quan hệ thật trói buộc."),
    ("排解", "páijiě", "bài giải", "động từ", "giải tỏa (buồn phiền)", "他常常用跑步来排解压力。", "Anh ấy thường chạy bộ để giải tỏa áp lực.",
     "Động từ, nghĩa là xua tan những cảm xúc không vui trong lòng: 排解愁闷，排解孤独，排解压力. Chữ 排 là bài trừ, đẩy ra. Trong bài: 来排解孤独."),
    ("直白", "zhíbái", "trực bạch", "tính từ", "thẳng thắn, thẳng thừng, trần trụi", "他说话很直白，从不拐弯抹角。", "Anh ấy nói chuyện rất thẳng, chưa bao giờ vòng vo.",
     "Tính từ, nghĩa là thẳng thắn, nói thẳng vào vấn đề. Trong bài: 他人直白的恶意, ác ý trắng trợn của người khác."),
    ("拉黑", "lāhēi", "lạp hắc", "động từ", "chặn, cho vào danh sách đen", "吵架以后，她把男朋友拉黑了。", "Sau khi cãi nhau, cô ấy chặn luôn bạn trai.",
     "Động từ, từ mới của mạng: kéo vào danh sách đen, 黑名单, tức là chặn tài khoản của ai đó. Trong bài: 一言不合就拉黑, nói một câu không hợp là chặn ngay."),
    ("躲避", "duǒbì", "đóa tị", "động từ", "tránh né, lẩn tránh", "他总是躲避我的目光。", "Anh ấy luôn tránh ánh mắt của tôi.",
     "Động từ, nghĩa là tránh xa những điều bất lợi cho mình: 躲避灾难，躲避不及. Trong bài: 上网原本是为躲避孤独, lên mạng vốn là để trốn tránh cô đơn."),
    ("无端", "wúduān", "vô đoan", "phó từ", "vô cớ, không duyên cớ", "他无端受到了指责。", "Anh ấy bị chỉ trích vô cớ.",
     "Phó từ, văn viết, nghĩa là không có lý do, vô duyên vô cớ. Trong bài: 反而无端受到伤害, ngược lại còn bị tổn thương vô cớ."),
    ("脆弱", "cuìruò", "thúy nhược", "tính từ", "yếu đuối, mong manh, dễ vỡ", "她的感情很脆弱。", "Tình cảm của cô ấy rất mong manh.",
     "Tính từ, nghĩa là không vững vàng, dễ tổn thương: 感情脆弱，体质脆弱. Chữ 脆 là giòn, dễ vỡ. Trong bài: 以新的方式暴露脆弱, phơi bày sự yếu đuối theo một cách mới."),
    ("俨然", "yǎnrán", "nghiễm nhiên", "phó từ", "y như, hệt như, ra vẻ", "他俨然一副大人模样。", "Cậu bé ra dáng hệt như người lớn.",
     "Phó từ, nghĩa là rất giống, y như. Cẩn thận, từ dễ nhầm: tiếng Việt nghiễm nhiên là đương nhiên, mặc nhiên; còn 俨然 là trông y như. Trong bài: 微信俨然成了多数人的生活日常, WeChat gần như đã trở thành chuyện thường ngày của đa số người."),
    ("流量", "liúliàng", "lưu lượng", "danh từ", "lượt truy cập; dữ liệu di động", "这个月的手机流量快用完了。", "Dung lượng dữ liệu di động tháng này sắp dùng hết rồi.",
     "Danh từ, thuật ngữ mạng, chỉ lượng truy cập vào một trang web trong một thời gian, hoặc dung lượng dữ liệu di động. Ngày nay còn có 流量明星, ngôi sao có lượng người hâm mộ lớn. Trong bài: 在互联网快节奏的流量中, trong dòng chảy thông tin nhịp độ nhanh của Internet."),
    ("白白", "báibái", "bạch bạch", "phó từ", "uổng công, phí hoài, không được gì", "我白白等了他一个小时。", "Tôi đợi anh ta suốt một tiếng đồng hồ một cách uổng công.",
     "Phó từ, nghĩa là không có hiệu quả, uổng phí. Đây là câu mẫu thứ bảy: 白白 cộng cụm động từ, như 白白浪费，白白错过."),
    ("剥夺", "bōduó", "bác đoạt", "động từ", "tước đoạt, tước bỏ", "没有人能剥夺你受教育的权利。", "Không ai có thể tước đoạt quyền được học hành của bạn.",
     "Động từ, nghĩa là dùng sức ép để lấy đi. Chữ 剥 ở đây đọc bō. Kết hợp hay gặp: 剥夺权利，剥夺时间. Trong bài: 白白剥夺了我们原本用于独立思考的时间."),
    ("秒回", "miǎohuí", "miểu hồi", "động từ", "trả lời ngay lập tức", "她每次都秒回我的微信。", "Lần nào cô ấy cũng trả lời tin nhắn WeChat của tôi ngay lập tức.",
     "Động từ, từ lóng mạng, nghĩa là trả lời trong vòng một giây. 秒 là giây. Tương tự có 秒杀, mua hàng giây lát hết sạch. Trong bài: 秒回成了微信社交的第一美德."),
    ("美德", "měidé", "mỹ đức", "danh từ", "đức tính tốt đẹp", "中国人历来有尊老爱幼的传统美德。", "Người Trung Quốc xưa nay có truyền thống tốt đẹp kính già yêu trẻ.",
     "Danh từ, nghĩa là phẩm chất tốt đẹp. Trong bài, tác giả nói một cách mỉa mai: 秒回成了微信社交的第一美德, trả lời ngay lập tức đã trở thành đức tính số một trong giao tiếp WeChat."),
    ("敷衍", "fūyǎn", "phu diễn", "động từ", "làm qua loa, đối phó, chiếu lệ", "做事喜欢敷衍是不好的习惯。", "Làm việc qua loa đại khái là thói quen không tốt.",
     "Động từ, nghĩa là làm việc thiếu trách nhiệm hoặc đối xử với người không thật lòng, chỉ ứng phó bề ngoài. Trong bài: 而其中的敷衍却被有意无意地忽略了, còn sự qua loa trong đó thì lại bị cố tình hay vô tình bỏ qua."),
    ("有助于", "yǒuzhùyú", "hữu trợ vu", "động từ", "có ích cho, giúp cho", "跑步有助于减肥。", "Chạy bộ giúp giảm cân.",
     "Động từ, nghĩa là có tác dụng giúp đỡ cho việc gì, văn viết. Trong bài: 明确朋友圈的真相，有助于我们合理分配社交能量, hiểu rõ bản chất của vòng bạn bè giúp chúng ta phân bổ năng lượng giao tiếp hợp lý."),
    ("消耗", "xiāohào", "tiêu hao", "động từ", "tiêu hao, hao tốn", "爬山很消耗体力。", "Leo núi rất tốn sức.",
     "Động từ, nghĩa là làm cho dần dần giảm đi, mất đi: 消耗体力，消耗能量. Âm Hán Việt và nghĩa giống tiếng Việt. Trong bài: 被虚拟社交关系消耗了大量时间精力的网民们."),
    ("警惕", "jǐngtì", "cảnh dịch", "động từ", "cảnh giác", "我们要时刻保持警惕。", "Chúng ta phải luôn luôn giữ cảnh giác.",
     "Động từ, nghĩa là luôn tỉnh táo đề phòng nguy hiểm hay khuynh hướng sai lầm: 警惕危险, 保持警惕. Tiếng Việt nói cảnh giác."),
    ("守护", "shǒuhù", "thủ hộ", "động từ", "canh giữ, gìn giữ, bảo vệ", "他用一生守护着自己的家人。", "Ông ấy dùng cả cuộc đời để che chở gia đình mình.",
     "Động từ, nghĩa là canh giữ, bảo vệ: 守护家人，守护信仰. Câu kết bài khóa: 守护内心的那一份纯粹，那一份真诚, gìn giữ sự thuần khiết và chân thành trong lòng."),
    ("纯粹", "chúncuì", "thuần túy", "tính từ", "thuần khiết, thuần túy, trong sáng", "这是一份纯粹的感情。", "Đây là một thứ tình cảm thuần khiết.",
     "Tính từ, nghĩa là không pha lẫn thứ khác. Tiếng Việt thuần túy; khi nói về tình cảm, tâm hồn thì dịch là thuần khiết, trong sáng. Trong bài, 纯粹 được dùng như danh từ: 那一份纯粹."),
    ("不冷不热", "bùlěng-bùrè", "bất lãnh bất nhiệt", "thành ngữ", "không nóng không lạnh; (thái độ) hờ hững, nhạt nhẽo", "由于某种原因，他对我一直不冷不热。", "Vì lý do nào đó, anh ấy luôn hờ hững với tôi.",
     "Thành ngữ, nghĩa gốc là nhiệt độ vừa phải, không nóng không lạnh; nghĩa bóng là thái độ với người khác bình thường, không mặn không nhạt. Trong bài: 想保持一种不冷不热的礼貌, muốn giữ một kiểu lịch sự xã giao không nóng không lạnh."),
    ("恰恰相反", "qiàqià xiāngfǎn", "kháp kháp tương phản", "thành ngữ", "hoàn toàn ngược lại", "我根本不想和你争吵，恰恰相反，我想与你和好如初。", "Tôi hoàn toàn không muốn cãi nhau với bạn, ngược lại, tôi muốn làm lành như xưa.",
     "Thành ngữ, nghĩa là vừa đúng ngược lại. 恰恰 là vừa vặn, đúng là. Trong bài: 但起到的效果可能恰恰相反, nhưng hiệu quả đạt được có thể hoàn toàn ngược lại."),
    ("一言不合", "yīyán-bùhé", "nhất ngôn bất hợp", "thành ngữ", "một lời không hợp", "他们两人只因一言不合就吵了起来。", "Hai người họ chỉ vì một câu không hợp mà cãi nhau.",
     "Thành ngữ, nghĩa là một câu nói không hợp ý nhau. Thường dùng theo mẫu 一言不合就……, một lời không hợp là…, nay rất phổ biến trên mạng. Trong bài: 一言不合就拉黑."),
    ("有意无意", "yǒuyì-wúyì", "hữu ý vô ý", "thành ngữ", "vừa cố ý vừa như vô tình", "当我们回忆过去的时候，总是有意无意地将其美化。", "Khi hồi tưởng quá khứ, chúng ta luôn ít nhiều tô hồng nó.",
     "Thành ngữ, nghĩa là có vẻ cố ý mà cũng như vô tình; hoặc trông như vô tình nhưng thật ra là cố ý. Thường làm trạng ngữ với 地. Trong bài: 敷衍却被有意无意地忽略了."),
    ("心照不宣", "xīnzhào-bùxuān", "tâm chiếu bất tuyên", "thành ngữ", "trong lòng đều hiểu, không cần nói ra", "他是如何被招进单位的，大家都心照不宣。", "Anh ta vào cơ quan bằng cách nào, mọi người đều ngầm hiểu.",
     "Thành ngữ. 心照 là lòng đã soi rõ, tức là đều hiểu; 不宣 là không nói ra. Tiếng Việt có thể nói là ngầm hiểu với nhau. Trong bài: 虚拟社交扼杀深度关系的建立已成为心照不宣的事实."),
]

add("bullets", chapter="Từ mới (46 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 2.3 có 41 từ mới và 5 thành ngữ, chia thành 16 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 重构 (chóng) · 剥夺 (bō) · 当下 (dāng)",
           "Từ dễ nhầm: 俨然 (≠ nghiễm nhiên) · 解读 · 纯粹",
           "Từ lóng mạng: 热搜 · 屏蔽 · 拉黑 · 秒回 · 流量 · 上线"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có bốn mươi mốt từ mới và năm thành ngữ, tổng cộng bốn mươi sáu mục, thầy chia thành mười sáu nhóm nhỏ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe nhé."),
         F(3, "Chú ý cách đọc của một số từ, như 重构，剥夺，当下."),
         F(4, "Có mấy từ dễ hiểu nhầm, đặc biệt là 俨然: nó không phải nghiễm nhiên theo nghĩa tiếng Việt."),
         F(5, "Và bài này có rất nhiều từ lóng của mạng xã hội, như 热搜，屏蔽，拉黑，秒回，流量，上线. Đây là những từ người trẻ Trung Quốc dùng hằng ngày. Chúng ta bắt đầu.")])

sizes = [3] * 14 + [2, 2]
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
    ("前阵子，微信悄悄上线了一项新功能：朋友圈可设置为仅一个月可见。这个没写进版本介绍的新功能，一经推出就上了热搜——“三天太短，半年太长，一个月刚刚好。”“不用设，一天我也不想看。”",
     "Dạo trước, WeChat lặng lẽ tung ra một chức năng mới: vòng bạn bè có thể cài đặt chỉ hiển thị trong một tháng. Chức năng mới này không hề được ghi trong phần giới thiệu phiên bản, nhưng vừa ra mắt đã lên ngay top tìm kiếm: “Ba ngày thì ngắn quá, nửa năm thì dài quá, một tháng là vừa đẹp.” “Khỏi cần cài, một ngày tôi cũng chẳng muốn xem.”",
     ["悄悄上线 là lặng lẽ ra mắt. 可设置为仅一个月可见 là có thể cài đặt thành chỉ hiển thị một tháng; 可见 là có thể nhìn thấy. Trước đó WeChat đã có chế độ ba ngày và nửa năm.",
      "一经推出就上了热搜: mẫu 一经……就…… nghĩa là vừa mới… liền…, văn viết. Hai câu trong ngoặc kép là bình luận của cư dân mạng; câu thứ hai rất hài hước: một ngày tôi cũng không muốn xem, cho thấy nhiều người đã chán vòng bạn bè."]),
    ("在越来越多人逃离朋友圈的当下，这项功能给了我们一个明确的提示：如何理解微信，如何解读虚拟社交。",
     "Vào lúc ngày càng nhiều người trốn chạy khỏi vòng bạn bè, chức năng này đã cho chúng ta một gợi ý rõ ràng: nên hiểu WeChat như thế nào, nên nhìn nhận giao tiếp ảo ra sao.",
     ["在……的当下 là vào lúc…, trong bối cảnh hiện nay khi…. 逃离 là trốn chạy, rời bỏ. 明确的提示 là gợi ý rõ ràng.",
      "如何解读虚拟社交 là nên giải mã, nhìn nhận giao tiếp ảo như thế nào. Hai đoạn đầu là phần dẫn nhập: từ một chức năng nhỏ, tác giả nêu ra vấn đề lớn của bài."]),
    ("【朋友圈里的“群体性孤独”】\n前段时间，腾讯发布的2019年第1季度业绩报告显示：微信月活跃用户已突破11亿，与此形成对比的是另一组数据，",
     "【“Cô đơn tập thể” trong vòng bạn bè】 Thời gian trước, báo cáo kết quả kinh doanh quý 1 năm 2019 do Tencent công bố cho thấy: số người dùng hoạt động hằng tháng của WeChat đã vượt 1,1 tỷ; đối lập với con số này là một nhóm số liệu khác,",
     ["Tiểu mục thứ nhất: 朋友圈里的群体性孤独, cô đơn tập thể trong vòng bạn bè. 群体性 là mang tính tập thể, tính bầy đàn.",
      "第一季度 là quý một. 月活跃用户 là người dùng hoạt động hằng tháng, thuật ngữ của ngành Internet. 已突破十一亿 là đã vượt mốc một tỷ một trăm triệu. 与此形成对比的是 là đối lập với điều này là…, câu mẫu thứ nhất của bài."],
     "朋友圈里的群体性孤独。前段时间，腾讯发布的二零一九年第一季度业绩报告显示：微信月活跃用户已突破十一亿，与此形成对比的是另一组数据，"),
    ("2019年初，“微信之父”张小龙说，每天有7.5亿人使用微信朋友圈，不过，其中有超过一亿人设置了“朋友圈三天可见”。当代人的社交困境由此可见一斑。",
     "đầu năm 2019, “cha đẻ của WeChat” Trương Tiểu Long cho biết, mỗi ngày có 750 triệu người dùng vòng bạn bè, nhưng trong số đó có hơn 100 triệu người đã cài đặt “vòng bạn bè chỉ hiển thị ba ngày”. Qua đó đủ thấy cảnh khó khăn trong giao tiếp xã hội của con người thời nay.",
     ["Số liệu đối lập: 七点五亿 là bảy trăm năm mươi triệu người dùng vòng bạn bè mỗi ngày, nhưng hơn một trăm triệu người cài đặt chỉ hiển thị ba ngày, tức là không muốn người khác xem nhiều về mình.",
      "由此可见一斑 là qua đó thấy được phần nào, các bạn đã học ở bài hai chấm hai. 社交困境 là cảnh khó khăn, bế tắc trong giao tiếp xã hội."],
     "二零一九年初，微信之父张小龙说，每天有七点五亿人使用微信朋友圈，不过，其中有超过一亿人设置了朋友圈三天可见。当代人的社交困境由此可见一斑。"),
    ("朋友圈成为社交必需品的同时，又让人感到不堪重负。至于朋友圈三天可见、一个月可见、半年可见，乃至屏蔽朋友圈等功能，说白了，都是为了满足人们的社交心理：想保持一种不冷不热的礼貌。表面配合演出，内心毫无波澜。",
     "Vòng bạn bè vừa trở thành món đồ thiết yếu của giao tiếp xã hội, lại vừa khiến người ta thấy quá sức chịu đựng. Còn những chức năng như chỉ hiển thị ba ngày, một tháng, nửa năm, thậm chí ẩn hẳn vòng bạn bè, nói trắng ra, đều là để đáp ứng tâm lý xã giao của con người: muốn giữ một kiểu lịch sự không nóng không lạnh. Bề ngoài thì phối hợp diễn cho tròn vai, trong lòng thì chẳng chút gợn sóng.",
     ["……的同时，又…… là vừa… lại vừa…. 社交必需品 là thứ thiết yếu của giao tiếp. 不堪重负 là không chịu nổi gánh nặng.",
      "至于 là còn về, dẫn sang một chủ đề liên quan. 乃至 là thậm chí, cho đến. 说白了 là nói trắng ra, câu mẫu thứ hai. 不冷不热的礼貌 là sự lịch sự hờ hững.",
      "表面配合演出，内心毫无波澜 là câu cửa miệng trên mạng: bề ngoài thì hùa theo diễn kịch, như bấm thích, bình luận cho có, nhưng trong lòng chẳng có chút cảm xúc nào."]),
    ("麻省理工学院社会学教授雪莉·特克尔就曾发出这样的疑问：为什么科技愈加便利，彼此交往却愈加疏远？",
     "Giáo sư xã hội học Sherry Turkle của Học viện Công nghệ Massachusetts từng đặt ra câu hỏi: vì sao công nghệ càng tiện lợi, mà con người giao tiếp với nhau lại càng xa cách?",
     ["麻省理工学院 là Học viện Công nghệ Massachusetts, MIT; 麻省 là bang Massachusetts. 雪莉·特克尔 là phiên âm tên Sherry Turkle, dấu chấm giữa ngăn cách tên và họ người nước ngoài.",
      "发出疑问 là đặt ra câu hỏi. 科技愈加便利，彼此交往却愈加疏远: cặp 愈加……却愈加…… tạo thành nghịch lý, giống mẫu 越……越……. Đây chính là câu hỏi trung tâm của bài."]),
    ("在对人与信息技术的关系进行了长达15年的系统研究后，她写出《群体性孤独》一书，挖掘了互联网时代群体孤独的根源。特克尔教授认为，互联网在改变我们的思维、生活的同时，也重构了以往的人际关系。",
     "Sau mười lăm năm nghiên cứu có hệ thống về mối quan hệ giữa con người và công nghệ thông tin, bà đã viết cuốn “Cô đơn tập thể”, đào sâu tìm ra căn nguyên của sự cô đơn tập thể trong thời đại Internet. Giáo sư Turkle cho rằng, Internet vừa thay đổi tư duy và cuộc sống của chúng ta, vừa tái cấu trúc các mối quan hệ giữa người với người trước đây.",
     ["对……进行了研究 là tiến hành nghiên cứu về…, kiểu câu văn viết với động từ hình thức 进行. 长达十五年 là kéo dài tới mười lăm năm. 一书 là cuốn sách, văn viết.",
      "挖掘根源 là đào sâu tìm ra căn nguyên. 在……的同时，也…… là đồng thời với…, cũng…. 重构了以往的人际关系 là tái cấu trúc các quan hệ con người trước kia."],
     "在对人与信息技术的关系进行了长达十五年的系统研究后，她写出群体性孤独一书，挖掘了互联网时代群体孤独的根源。特克尔教授认为，互联网在改变我们的思维、生活的同时，也重构了以往的人际关系。"),
    ("在网上，我们可以找到很多有共同兴趣的陌生人，建立线上的虚拟小圈子，甚至可以把自己伪装成想成为的任何人。但特克尔教授认为，这种快餐式的虚拟关系，说到底，是把每个人简化成实用的客体，美好和有趣的一面被放大，而真实的缺点却被隐匿了。",
     "Trên mạng, chúng ta có thể tìm được nhiều người lạ có chung sở thích, lập nên những nhóm nhỏ ảo trực tuyến, thậm chí có thể giả làm bất cứ ai mình muốn trở thành. Nhưng giáo sư Turkle cho rằng, kiểu quan hệ ảo “ăn liền” này, suy cho cùng, là giản lược mỗi con người thành một đối tượng thực dụng: mặt tốt đẹp, thú vị bị phóng đại, còn khuyết điểm thật thì bị giấu đi.",
     ["Đoạn này nêu mặt hấp dẫn của mạng trước, rồi mới phê phán. 线上 là trực tuyến. 把自己伪装成想成为的任何人 là giả làm bất cứ người nào mình muốn trở thành.",
      "快餐式的虚拟关系 là quan hệ ảo kiểu đồ ăn nhanh, tức là nhanh, tiện, nhưng hời hợt. 说到底 là suy cho cùng, câu mẫu thứ ba. 简化成实用的客体 là giản lược thành đối tượng để sử dụng. Hai vế 美好的一面被放大，真实的缺点被隐匿 đối nhau, đều là câu bị động với 被."]),
    ("在《群体性孤独》里，特克尔教授还总结了虚拟社交制造出的三大错觉：\n一是觉得我们可以把精力分配到任何自己想关注的领域；\n二是幻想总有人倾听我们；\n三是以为我们永远不孤独。",
     "Trong cuốn “Cô đơn tập thể”, giáo sư Turkle còn tổng kết ba ảo giác lớn mà giao tiếp ảo tạo ra: một là cảm thấy chúng ta có thể phân bổ sức lực vào bất cứ lĩnh vực nào mình muốn quan tâm; hai là ảo tưởng rằng luôn có người lắng nghe chúng ta; ba là tưởng rằng chúng ta sẽ không bao giờ cô đơn.",
     ["三大错觉 là ba ảo giác lớn. Cách liệt kê 一是……二是……三是…… là một là…, hai là…, ba là…, rất hay dùng trong văn nghị luận.",
      "Chú ý ba động từ chỉ suy nghĩ sai: 觉得, cảm thấy; 幻想, ảo tưởng; 以为, cứ tưởng, thường dùng khi điều mình nghĩ không đúng sự thật. 分配精力 là phân bổ sức lực, tinh thần."]),
    ("因为讨厌被真实关系束缚，很多人选择在社交平台上表达自我、分享隐私，来排解孤独，希望获得陌生人的关注和认同，但起到的效果可能恰恰相反。",
     "Vì ghét bị các mối quan hệ thật trói buộc, nhiều người chọn bày tỏ bản thân, chia sẻ chuyện riêng tư trên mạng xã hội để giải tỏa cô đơn, mong nhận được sự quan tâm và đồng cảm của người lạ, nhưng hiệu quả đạt được có thể hoàn toàn ngược lại.",
     ["被真实关系束缚 là bị các mối quan hệ thật trói buộc. 社交平台 là nền tảng mạng xã hội. 表达自我 là thể hiện bản thân; 分享隐私 là chia sẻ đời tư.",
      "来排解孤独: chữ 来 nối phương thức với mục đích, nghĩa là để. 关注和认同 là sự quan tâm và công nhận. 起到的效果 là hiệu quả đạt được; 恰恰相反 là hoàn toàn ngược lại."]),
    ("比起收获的善意，他人直白的恶意，更让人难以接受。哪怕是在朋友圈这种半生不熟的社交环境里，一言不合就拉黑的情况也不在少数。",
     "So với những thiện ý nhận được, thì ác ý trắng trợn của người khác càng khiến người ta khó chấp nhận. Ngay cả trong môi trường giao tiếp nửa quen nửa lạ như vòng bạn bè, chuyện một lời không hợp là chặn ngay cũng không hiếm.",
     ["比起……，……更…… là so với… thì… càng…, câu mẫu thứ tư. 善意 là thiện ý, 恶意 là ác ý, chữ 恶 đọc è. 直白的恶意 là ác ý trắng trợn.",
      "半生不熟 nghĩa đen là nửa sống nửa chín, ở đây chỉ quan hệ nửa quen nửa lạ, theo mẫu 半A不B, câu mẫu thứ năm. 一言不合就拉黑 là một câu không hợp là chặn luôn. 不在少数 là không ít, câu mẫu thứ sáu."]),
    ("上网原本是为躲避孤独，寻求温暖，反而无端受到伤害，可见这种“我分享故我在”的做法，不仅会让虚拟社交变成“自我表演”，还会让我们以新的方式暴露脆弱。",
     "Lên mạng vốn là để trốn tránh cô đơn, tìm kiếm hơi ấm, vậy mà ngược lại còn bị tổn thương vô cớ. Có thể thấy, cách làm “tôi chia sẻ, vậy tôi tồn tại” này không chỉ biến giao tiếp ảo thành “màn tự biểu diễn”, mà còn khiến chúng ta phơi bày sự yếu đuối của mình theo một cách mới.",
     ["原本是为……，反而…… là vốn là để…, ngược lại…; chữ 反而 cho thấy kết quả trái với mong muốn. 无端受到伤害 là bị tổn thương vô cớ.",
      "可见 là có thể thấy, dẫn ra kết luận. 我分享故我在 là biến tấu từ câu của Descartes. 不仅……还…… là không chỉ… mà còn…. 自我表演 là tự biểu diễn; 暴露脆弱 là phơi bày sự yếu đuối."]),
    ("【虚拟社交正在扼杀深度关系】\n如今我们已经进入了网络社交时代，“永远在线，时刻沟通”，微信俨然成了多数人的生活日常。",
     "【Giao tiếp ảo đang bóp chết những mối quan hệ sâu sắc】 Ngày nay chúng ta đã bước vào thời đại giao tiếp mạng, “luôn luôn trực tuyến, lúc nào cũng liên lạc”, WeChat gần như đã trở thành chuyện thường ngày của đa số người.",
     ["Tiểu mục thứ hai lặp lại gần đúng tên bài: 虚拟社交正在扼杀深度关系. 深度关系 là quan hệ có chiều sâu.",
      "永远在线，时刻沟通 là luôn luôn online, lúc nào cũng liên lạc. 俨然成了 là trông như đã trở thành, gần như đã thành. 生活日常 là chuyện thường ngày; 日常 ở đây dùng như danh từ."]),
    ("特克尔教授却指出，在互联网快节奏的流量中，大量持续的沟通，白白剥夺了我们原本用于独立思考的时间，也大大降低了我们对回复质量的期待。比起质量，人们更在乎回复的速度。",
     "Thế nhưng giáo sư Turkle chỉ ra rằng, trong dòng chảy thông tin nhịp độ nhanh của Internet, việc liên lạc liên tục với khối lượng lớn đã tước đi một cách vô ích khoảng thời gian vốn dành cho suy nghĩ độc lập của chúng ta, và cũng hạ thấp rất nhiều kỳ vọng của chúng ta về chất lượng của lời hồi đáp. So với chất lượng, người ta quan tâm hơn đến tốc độ trả lời.",
     ["却指出 là thế nhưng lại chỉ ra, chữ 却 đối lập với hình ảnh tích cực ở đoạn trước. 快节奏的流量 là dòng lưu lượng nhịp độ nhanh.",
      "白白剥夺了……的时间 là tước đi một cách uổng phí khoảng thời gian…, câu mẫu 白白. 原本用于独立思考 là vốn dùng cho suy nghĩ độc lập. 比起质量，人们更在乎回复的速度 lại là mẫu 比起……更……."]),
    ("秒回成了微信社交的第一美德，而其中的敷衍却被有意无意地忽略了，虚拟社交扼杀深度关系的建立已成为心照不宣的事实。如果你还把一个人的朋友圈与他全部的真实生活划等号，那只能说明身处互联网时代的你还不够成熟。",
     "Trả lời ngay lập tức đã trở thành đức tính số một trong giao tiếp trên WeChat, còn sự qua loa trong đó thì lại bị cố tình hay vô tình bỏ qua; việc giao tiếp ảo bóp chết sự hình thành các mối quan hệ sâu sắc đã trở thành sự thật mà ai cũng ngầm hiểu. Nếu bạn vẫn đánh đồng vòng bạn bè của một người với toàn bộ cuộc sống thật của họ, thì điều đó chỉ chứng tỏ bạn, người đang sống trong thời đại Internet, vẫn chưa đủ trưởng thành.",
     ["秒回成了第一美德 là cách nói mỉa mai. 有意无意地忽略了 là cố ý hay vô tình mà bỏ qua. 心照不宣的事实 là sự thật ai cũng ngầm hiểu.",
      "把A与B划等号 là đánh đồng A với B, vẽ dấu bằng giữa A và B, câu mẫu thứ tám. 身处 là thân ở, đang ở trong, chữ 处 đọc chǔ. 那只能说明 là thì chỉ có thể chứng tỏ."]),
    ("明确朋友圈的真相，有助于我们合理分配社交能量，把时间和精力留给更重要的现实关系，尤其是留给自己。对于被虚拟社交关系消耗了大量时间精力的网民们，在享受网络社交带来的便利性的同时，更要时刻保持警惕，守护内心的那一份纯粹，那一份真诚。",
     "Hiểu rõ bản chất của vòng bạn bè giúp chúng ta phân bổ năng lượng giao tiếp một cách hợp lý, dành thời gian và sức lực cho những mối quan hệ thật quan trọng hơn, nhất là dành cho chính mình. Đối với những cư dân mạng đã bị các quan hệ ảo tiêu hao nhiều thời gian và sức lực, trong khi tận hưởng sự tiện lợi của mạng xã hội, càng phải luôn giữ cảnh giác, gìn giữ sự thuần khiết và chân thành trong lòng mình.",
     ["Đoạn kết đưa ra lời khuyên. 明确真相 là hiểu rõ sự thật. 有助于 là giúp cho. 社交能量 là năng lượng giao tiếp. 尤其是留给自己 là nhất là dành cho bản thân.",
      "在……的同时，更要…… là trong khi…, càng phải…, câu mẫu cuối cùng. 时刻保持警惕 là luôn giữ cảnh giác. 守护内心的那一份纯粹，那一份真诚: điệp cấu trúc 那一份 ở cuối bài tạo âm hưởng nhẹ nhàng, sâu lắng."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 群体性孤独", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa. Bài được cải biên từ bài viết 朋友圈设置一个月可见，透露了什么社交观？, Vòng bạn bè cài đặt hiển thị một tháng tiết lộ quan niệm giao tiếp gì?, đăng trên tài khoản WeChat 书单 ngày năm tháng sáu năm hai nghìn không trăm mười chín.",
         F(0, "Thầy chia bài thành mười sáu đoạn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng. Các dòng trong ngoặc vuông là tiểu mục của bài."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "").replace("《", "").replace("》", "").replace("【", "").replace("】", "。").replace("\n", "")
    zsize = 54 if len(zh) <= 100 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", "").replace("【", "").replace("】", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Tóm tắt nội dung", section="Bài khóa 课文", title="Bố cục bài khóa", size=35,
    items=["## Dẫn nhập: 朋友圈可设置为仅一个月可见 → 如何解读虚拟社交",
           "## 1. 朋友圈里的“群体性孤独”",
           "数据对比：11亿用户 ↔ 超过一亿人设置“三天可见” · 想保持一种不冷不热的礼貌",
           "特克尔：科技愈加便利，交往却愈加疏远 · 快餐式的虚拟关系 · 三大错觉 · “我分享故我在”",
           "## 2. 虚拟社交正在扼杀深度关系",
           "秒回成了第一美德，敷衍被忽略 · 朋友圈 ≠ 真实生活",
           "## 结论: 合理分配社交能量，把时间留给现实关系和自己，守护纯粹与真诚"],
    say=["Bây giờ chúng ta cùng nhìn lại bố cục của bài báo.",
         F(0, "Phần dẫn nhập: WeChat ra mắt chức năng vòng bạn bè chỉ hiển thị một tháng, và từ đó đặt ra câu hỏi: nên nhìn nhận giao tiếp ảo như thế nào."),
         F(1, "Tiểu mục một: cô đơn tập thể trong vòng bạn bè."),
         F(2, "Tác giả dùng số liệu đối lập: hơn một tỷ người dùng WeChat, nhưng hơn một trăm triệu người chỉ cho xem ba ngày. Người ta muốn giữ một kiểu lịch sự không nóng không lạnh."),
         F(3, "Sau đó dẫn quan điểm của giáo sư Turkle: công nghệ càng tiện, con người càng xa cách; quan hệ ảo kiểu ăn liền; ba ảo giác lớn; và kiểu tôi chia sẻ, vậy tôi tồn tại, khiến ta dễ bị tổn thương."),
         F(4, "Tiểu mục hai: giao tiếp ảo đang bóp chết những mối quan hệ sâu sắc."),
         F(5, "Trả lời ngay trở thành đức tính số một, còn sự qua loa thì bị bỏ qua; và đừng đánh đồng vòng bạn bè của một người với cuộc sống thật của họ."),
         F(6, "Kết luận: hãy phân bổ năng lượng giao tiếp hợp lý, dành thời gian cho các mối quan hệ thật và cho chính mình, gìn giữ sự thuần khiết và chân thành trong lòng.")])

# ======================= CÂU MẪU =======================
add("bullets", chapter="Câu mẫu: 形成对比 · 说白了 · 说到底 · 比起", section="Câu mẫu 重点句型", title="1. 与……形成对比的是……  ·  2. 说/讲白了", size=33,
    items=["## 与A形成（鲜明）对比的是B: đối lập (rõ rệt) với A là B",
           "报告显示：微信月活跃用户已突破11亿，与此形成对比的是另一组数据，……",
           "他仅用三年的时间就升任总经理助理，与他的成功形成鲜明对比的是我还在原地踏步。",
           "双胞胎的性格也可能差异很大，与哥哥沉稳的性格形成对比的是弟弟的莽撞。",
           "## 说白了: nói trắng ra, nói toạc ra – giải thích lại bằng lời dễ hiểu, thẳng thắn hơn",
           "我一直想过一种自由自在的生活，不受约束，说白了就是没人管。",
           "依我所见，所谓美满的婚姻，说白了其实就是彼此包容。"],
    say=["Bây giờ chúng ta sang phần câu mẫu trọng điểm. Bài này có chín câu mẫu.",
         F(0, "Câu mẫu thứ nhất: 与……形成对比的是……. Dùng để đặt hai sự việc cạnh nhau cho thấy sự đối lập; có thể thêm 鲜明, rõ rệt. Tiếng Việt dịch là trái ngược với A là B, đối lập với A là B."),
         F(1, "Ví dụ một, từ bài khóa: 微信月活跃用户已突破十一亿，与此形成对比的是另一组数据. Chữ 此 là điều này, tức con số một tỷ một trăm triệu."),
         F(2, "Ví dụ hai: 他仅用三年的时间就升任总经理助理，与他的成功形成鲜明对比的是我还在原地踏步。 Anh ấy chỉ mất ba năm đã lên chức trợ lý tổng giám đốc; trái ngược hẳn với thành công của anh ấy là tôi vẫn giậm chân tại chỗ."),
         F(3, "Ví dụ ba: 双胞胎的性格也可能差异很大，与哥哥沉稳的性格形成对比的是弟弟的莽撞。 Tính cách của anh em sinh đôi cũng có thể rất khác nhau; đối lập với tính điềm đạm của người anh là sự lỗ mãng của người em."),
         F(4, "Câu mẫu thứ hai: 说白了, hoặc 讲白了. Dùng lời lẽ đơn giản, dễ hiểu để giải thích sâu hơn, thấu đáo hơn điều vừa nói. Tiếng Việt dịch là nói trắng ra, nói toạc ra. Trong bài khóa: 至于朋友圈三天可见……等功能，说白了，都是为了满足人们的社交心理."),
         F(5, "Ví dụ: 我一直想过一种自由自在的生活，不受约束，说白了就是没人管。 Tôi luôn muốn sống một cuộc sống tự do tự tại, không bị ràng buộc, nói trắng ra là không ai quản."),
         F(6, "Ví dụ: 依我所见，所谓美满的婚姻，说白了其实就是彼此包容。 Theo tôi thấy, cái gọi là hôn nhân hạnh phúc, nói trắng ra chính là bao dung lẫn nhau.")])

add("bullets", section="Câu mẫu 重点句型", title="3. 说到底  ·  4. 比起……，……更……", size=33,
    items=["## 说到底: suy cho cùng, xét đến cùng – nói ra bản chất của vấn đề",
           "这种快餐式的虚拟关系，说到底，是把每个人简化成实用的客体。",
           "人生说到底是自己的选择，自己的路在自己的脚下。",
           "你现在对我不冷不热，说到底，就是没把我放在眼里。",
           "## 比起A，B更……: so với A thì B … hơn",
           "比起收获的善意，他人直白的恶意，更让人难以接受。",
           "由于长时间不练习英文，比起去年，我的口语水平明显退步了。",
           "比起外表，她丰富的精神世界更让我着迷。"],
    say=[F(0, "Câu mẫu thứ ba: 说到底, nghĩa là nói đến cùng, suy cho cùng, dùng để nói ra bản chất của vấn đề. Khác với 说白了 nhấn mạnh nói cho dễ hiểu, 说到底 nhấn mạnh đi đến tận gốc."),
         F(1, "Ví dụ một, từ bài khóa: 这种快餐式的虚拟关系，说到底，是把每个人简化成实用的客体。"),
         F(2, "Ví dụ hai: 人生说到底是自己的选择，自己的路在自己的脚下。 Đời người suy cho cùng là lựa chọn của chính mình, con đường của mình nằm dưới chân mình."),
         F(3, "Ví dụ ba: 你现在对我不冷不热，说到底，就是没把我放在眼里。 Bây giờ anh đối với tôi lúc nóng lúc lạnh, suy cho cùng là không coi tôi ra gì. 没把我放在眼里 là không để tôi vào mắt."),
         F(4, "Câu mẫu thứ tư: 比起A，B更……, nghĩa là so với A thì B hơn. Khác với câu so sánh với 比, cái được nhắc sau 比起 là mốc so sánh, đứng đầu câu."),
         F(5, "Ví dụ một, từ bài khóa: 比起收获的善意，他人直白的恶意，更让人难以接受。"),
         F(6, "Ví dụ hai: 由于长时间不练习英文，比起去年，我的口语水平明显退步了。 Vì lâu không luyện tiếng Anh, so với năm ngoái, khả năng nói của tôi đã kém đi rõ rệt. Ở đây không có 更, nhưng ý so sánh vẫn rõ."),
         F(7, "Ví dụ ba: 比起外表，她丰富的精神世界更让我着迷。 So với vẻ bề ngoài, thế giới tinh thần phong phú của cô ấy càng làm tôi say mê.")])

add("bullets", chapter="Câu mẫu: 半A不B · 不在少数 · 白白 · 划等号", section="Câu mẫu 重点句型", title="5. 半A不B  ·  6. ……不在少数", size=33,
    items=["## 半A不B (A, B trái nghĩa): nửa A nửa B, lưng chừng – thường mang ý chê",
           "哪怕是在朋友圈这种半生不熟的社交环境里，一言不合就拉黑的情况也不在少数。",
           "她看这个男人头上戴着一顶浅灰色的帽子，穿了件半新不旧的大衣。",
           "他就爱吃半生不熟的牛排。 · 她女儿已经上大学了，家里还有个半大不小的老二。",
           "## ……不在少数: không ít, khá nhiều (văn viết)",
           "在经济危机的冲击下，对国内经济前景持怀疑态度的人不在少数。",
           "近年来，选择自驾回家过年的人不在少数。"],
    say=[F(0, "Câu mẫu thứ năm: 半A不B. A và B là hai từ đơn âm tiết trái nghĩa, biểu thị trạng thái lưng chừng, nửa nọ nửa kia, thường mang ý không hài lòng. Tiếng Việt cũng có nửa sống nửa chín, dở dở ương ương."),
         F(1, "Ví dụ một, từ bài khóa: 朋友圈这种半生不熟的社交环境. 半生不熟 nghĩa đen là nửa sống nửa chín, ở đây chỉ những người nửa quen nửa lạ."),
         F(2, "Ví dụ hai: 她看这个男人头上戴着一顶浅灰色的帽子，穿了件半新不旧的大衣。 Cô thấy người đàn ông đội một chiếc mũ màu xám nhạt, mặc chiếc áo khoác cũ cũ mới mới."),
         F(3, "Ví dụ ba: 他就爱吃半生不熟的牛排。 Anh ấy lại thích ăn bít tết tái. Và: 她女儿已经上大学了，家里还有个半大不小的老二。 Con gái chị ấy đã lên đại học, nhà còn đứa thứ hai đang tuổi lưng chừng, chẳng lớn chẳng bé."),
         F(4, "Câu mẫu thứ sáu: 不在少数, nghĩa là không phải số ít, tức là khá nhiều, văn viết. Trong bài khóa: 一言不合就拉黑的情况也不在少数。"),
         F(5, "Ví dụ: 在经济危机的冲击下，对国内经济前景持怀疑态度的人不在少数。 Dưới tác động của khủng hoảng kinh tế, không ít người hoài nghi về triển vọng kinh tế trong nước. 持怀疑态度 là giữ thái độ hoài nghi."),
         F(6, "Ví dụ: 近年来，选择自驾回家过年的人不在少数。 Mấy năm gần đây, không ít người chọn tự lái xe về quê ăn Tết.")])

add("bullets", section="Câu mẫu 重点句型", title="7. 白白 + cụm động từ  ·  8. 把A与B划等号", size=33,
    items=["## 白白 + VP: một cách uổng phí, chẳng được gì",
           "大量持续的沟通，白白剥夺了我们原本用于独立思考的时间。",
           "我们不能白白浪费青春年华，青春就是用来奋斗的。",
           "有好几次机会他都白白错过了，真是后悔莫及。",
           "## 把A与/和B划等号: đánh đồng A với B, coi A là B",
           "如果你还把一个人的朋友圈与他全部的真实生活划等号，那只能说明身处互联网时代的你还不够成熟。",
           "简单地把财富和幸福划等号，对此我不敢苟同。",
           "虽然传统儒学不能与传统制度划等号，但它们确实有着紧密的联系。"],
    say=[F(0, "Câu mẫu thứ bảy: 白白 cộng cụm động từ, nghĩa là làm một việc mà không thu được kết quả gì, uổng phí. Tiếng Việt dịch là uổng công, phí hoài, không công."),
         F(1, "Ví dụ một, từ bài khóa: 大量持续的沟通，白白剥夺了我们原本用于独立思考的时间。"),
         F(2, "Ví dụ hai: 我们不能白白浪费青春年华，青春就是用来奋斗的。 Chúng ta không thể để tuổi xuân trôi qua phí hoài, tuổi trẻ là để phấn đấu."),
         F(3, "Ví dụ ba: 有好几次机会他都白白错过了，真是后悔莫及。 Mấy lần cơ hội đến anh ấy đều để vuột mất, thật là hối hận không kịp."),
         F(4, "Câu mẫu thứ tám: 把A与B划等号, nghĩa là vẽ dấu bằng giữa A và B, tức là coi A và B là một, đánh đồng. Thường dùng trong câu phủ định hay phê phán. Chữ 划 ở đây đọc huà."),
         F(5, "Ví dụ một, từ bài khóa: 如果你还把一个人的朋友圈与他全部的真实生活划等号，那只能说明身处互联网时代的你还不够成熟。"),
         F(6, "Ví dụ hai: 简单地把财富和幸福划等号，对此我不敢苟同。 Đơn giản đánh đồng giàu có với hạnh phúc, tôi không dám đồng tình. 不敢苟同 là không dám tùy tiện đồng ý, cách nói lịch sự để phản đối."),
         F(7, "Ví dụ ba: 虽然传统儒学不能与传统制度划等号，但它们确实有着紧密的联系。 Tuy Nho học truyền thống không thể đánh đồng với chế độ truyền thống, nhưng chúng quả thực có mối liên hệ chặt chẽ.")])

add("bullets", chapter="Câu mẫu: 在……的同时，更要……", section="Câu mẫu 重点句型", title="9. 在……的同时，更要……", size=35,
    items=["Vế trước: việc đang làm / điều được hưởng · vế sau (更要): điều quan trọng hơn cần chú ý",
           "在享受网络社交带来便利的同时，更要时刻保持警惕，守护内心的那一份纯粹，那一份真诚。",
           "我希望你在倾听的同时，更要打破缄默，多发表自己的看法。",
           "在传授知识的同时，更要注重学生实际应用能力的培养。"],
    say=["Câu mẫu thứ chín, cũng là câu cuối cùng: 在……的同时，更要…….",
         F(0, "Vế trước nêu một việc đang làm hoặc điều đang được hưởng; vế sau với 更要 nhấn mạnh một điều còn quan trọng hơn cần chú ý. Tiếng Việt dịch là trong khi…, càng phải…, hoặc đồng thời với…, còn phải…. Mẫu này rất hay dùng ở phần kết của bài nghị luận."),
         F(1, "Ví dụ một, từ bài khóa: 在享受网络社交带来便利的同时，更要时刻保持警惕，守护内心的那一份纯粹，那一份真诚。"),
         F(2, "Ví dụ hai: 我希望你在倾听的同时，更要打破缄默，多发表自己的看法。 Tôi mong bạn trong khi lắng nghe, càng phải phá vỡ sự im lặng, phát biểu nhiều hơn ý kiến của mình. 缄默 là im lặng, văn viết."),
         F(3, "Ví dụ ba: 在传授知识的同时，更要注重学生实际应用能力的培养。 Đồng thời với việc truyền thụ kiến thức, càng phải chú trọng bồi dưỡng năng lực ứng dụng thực tế của học sinh.")])

# ======================= KẾT HỢP TỪ =======================
add("bullets", chapter="Kết hợp từ (词语搭配)", section="Kết hợp từ 词语搭配", title="Kết hợp từ (1): 扼杀 · 不堪 · 挖掘", size=33,
    items=["## 扼杀：～深度关系 · ～个性 · ～潜力 · ～希望",
           "如果我们一味否定学生已有的兴趣，认为他们是不务正业，那么很可能会扼杀他们的创造力。",
           "## 不堪：～重负 · ～回首 · ～一击",
           "青春时光拥有难以忘怀的经历，也有不堪回首的往事。",
           "## 挖掘：～根源 · ～潜力 · ～潜能 · ～主题 · ～宝藏",
           "教师应该善于挖掘孩子的潜能，培养他们多方面的能力。"],
    say=["Tiếp theo là phần kết hợp từ, 词语搭配.",
         F(0, "Từ thứ nhất: 扼杀. Hay đi với 深度关系，个性，潜力，希望. Ví dụ: 狭隘的人总是想扼杀别人的个性, người hẹp hòi luôn muốn bóp chết cá tính của người khác."),
         F(1, "Ví dụ khác: 如果我们一味否定学生已有的兴趣，认为他们是不务正业，那么很可能会扼杀他们的创造力。 Nếu chúng ta cứ một mực phủ nhận sở thích của học sinh, cho rằng các em không lo việc chính, thì rất có thể sẽ bóp chết óc sáng tạo của các em."),
         F(2, "Từ thứ hai: 不堪. Ba cụm cố định: 不堪重负, không chịu nổi gánh nặng; 不堪回首, không dám nhìn lại, chỉ quá khứ đau buồn; 不堪一击, không chịu nổi một đòn, rất yếu ớt."),
         F(3, "Ví dụ: 青春时光拥有难以忘怀的经历，也有不堪回首的往事。 Tuổi thanh xuân có những trải nghiệm khó quên, cũng có những chuyện cũ không dám nhớ lại. Và: 没想到他那么坚强的人，遇到感情问题竟然也不堪一击, không ngờ người cứng cỏi như anh ấy, gặp chuyện tình cảm lại yếu đuối đến thế."),
         F(4, "Từ thứ ba: 挖掘. Hay gặp 挖掘根源，挖掘潜力，挖掘潜能，挖掘主题，挖掘宝藏."),
         F(5, "Ví dụ: 教师应该善于挖掘孩子的潜能，培养他们多方面的能力。 Giáo viên nên giỏi khai thác tiềm năng của trẻ, bồi dưỡng năng lực nhiều mặt cho các em. Và: 作家应该善于从生活中挖掘主题, nhà văn nên giỏi tìm chủ đề từ cuộc sống.")])

add("bullets", section="Kết hợp từ 词语搭配", title="Kết hợp từ (2): 错觉 · 排解 · 剥夺", size=33,
    items=["## 错觉：产生～ · 出现～ · 时空～ · 色彩～",
           "广告中一些故意误导消费者的说法，会让消费者产生错觉。",
           "## 排解：～孤独 · ～压力 · 自我～",
           "生活中，人人都会有很多的不如意，如何排解压力对心理健康至关重要。",
           "## 剥夺：～时间 · ～权利 · ～成果",
           "人生其实就是由大大小小的选择组成的，没有人能干涉和剥夺你自由选择的权利。"],
    say=[F(0, "Từ thứ tư: 错觉. Hay gặp 产生错觉，出现错觉，时空错觉，色彩错觉."),
         F(1, "Ví dụ: 广告中一些故意误导消费者的说法，会让消费者产生错觉。 Một số cách nói cố tình đánh lừa người tiêu dùng trong quảng cáo sẽ khiến họ có cảm nhận sai lầm. Và: 在恶劣的环境条件下，人极容易出现错觉, trong điều kiện môi trường khắc nghiệt, con người rất dễ bị ảo giác."),
         F(2, "Từ thứ năm: 排解. Hay gặp 排解孤独，排解压力，自我排解."),
         F(3, "Ví dụ: 生活中，人人都会有很多的不如意，如何排解压力对心理健康至关重要。 Trong cuộc sống ai cũng có nhiều điều không như ý, giải tỏa áp lực thế nào có ý nghĩa cực kỳ quan trọng với sức khỏe tâm lý. Và: 在生活中遇到困扰要学会自我排解, gặp phiền muộn phải học cách tự giải tỏa."),
         F(4, "Từ thứ sáu: 剥夺. Hay gặp 剥夺时间，剥夺权利，剥夺成果."),
         F(5, "Ví dụ: 人生其实就是由大大小小的选择组成的，没有人能干涉和剥夺你自由选择的权利。 Đời người thực ra được tạo nên từ những lựa chọn lớn nhỏ, không ai có thể can thiệp và tước đoạt quyền tự do lựa chọn của bạn. Và: 没有人能随意剥夺他人的劳动所得, không ai được tùy tiện tước đoạt thành quả lao động của người khác.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 课后练习", title="Bài tập 1: Chọn từ điền vào chỗ trống", reveal=True, size=32,
    items=["## Từ cho sẵn: 排解 · 扼杀 · 屏蔽 · 说到底 · 有意无意 · 心照不宣",
           "(1) 大量刷题会___孩子们的学习兴趣。",
           "Đáp án: 扼杀",
           "(2) 他经常以关心的名义___地触碰我的感情伤口。",
           "Đáp án: 有意无意",
           "(3) 在国外求学的过程中，她经常靠唱歌来___身在异乡的孤独。",
           "Đáp án: 排解",
           "(4) 这款软件能___广告、弹窗和其他网页垃圾，减少干扰，让你的工作更高效。",
           "Đáp án: 屏蔽",
           "(5) 小说艺术的精髓就是塑造人物，写小说___就是写人物。",
           "Đáp án: 说到底",
           "(6) 我们都看到了对方，但由于太过尴尬，于是彼此___，装不认识。",
           "Đáp án: 心照不宣"],
    say=["Phần luyện tập, 趁热打铁. Bài tập một: chọn từ thích hợp điền vào chỗ trống.",
         F(0, "Có sáu từ: 排解，扼杀，屏蔽，说到底，有意无意，心照不宣."),
         F(1, "Câu một: 大量刷题会什么孩子们的学习兴趣。 Làm bài tập ồ ạt sẽ thế nào hứng thú học tập của trẻ? 刷题 là cày đề. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 扼杀. 扼杀学习兴趣, bóp chết hứng thú học tập."),
         F(3, "Câu hai: 他经常以关心的名义什么地触碰我的感情伤口。 Anh ta thường nhân danh quan tâm mà thế nào chạm vào vết thương tình cảm của tôi."),
         F(4, "Đáp án: 有意无意. Chữ 地 phía sau cho thấy cần một trạng ngữ: cố ý mà như vô tình."),
         F(5, "Câu ba: 在国外求学的过程中，她经常靠唱歌来什么身在异乡的孤独。 Trong thời gian du học, cô ấy thường hát để thế nào nỗi cô đơn nơi đất khách."),
         F(6, "Đáp án: 排解. 排解孤独, giải tỏa nỗi cô đơn."),
         F(7, "Câu bốn: 这款软件能什么广告、弹窗和其他网页垃圾，减少干扰，让你的工作更高效。 Phần mềm này có thể thế nào quảng cáo, cửa sổ bật lên và các thứ rác trên trang web."),
         F(8, "Đáp án: 屏蔽. 屏蔽广告, chặn quảng cáo. 弹窗 là cửa sổ bật lên, pop-up."),
         F(9, "Câu năm: 小说艺术的精髓就是塑造人物，写小说什么就是写人物。 Tinh túy của nghệ thuật tiểu thuyết là xây dựng nhân vật, viết tiểu thuyết thế nào chính là viết về con người."),
         F(10, "Đáp án: 说到底. Viết tiểu thuyết suy cho cùng là viết về con người."),
         F(11, "Câu sáu: 我们都看到了对方，但由于太过尴尬，于是彼此什么，装不认识。 Chúng tôi đều nhìn thấy nhau, nhưng vì quá ngượng, nên đôi bên thế nào, giả vờ không quen."),
         F(12, "Đáp án: 心照不宣. Hai bên ngầm hiểu mà không nói ra, giả vờ như không quen biết.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn đáp án đúng (1)", reveal=True, size=33,
    items=["(1) 河南安阳出土了一大批甲骨，上面的文字只有古文字学家才能（ ）。\nA.解读 B.解说 C.解决 D.排解",
           "Đáp án: A. 解读 – đọc và giải thích (văn tự)",
           "(2) 我频频向他请教问题，让他产生了（ ），误以为我对他有意思。\nA.知觉 B.错觉 C.幻觉 D.直觉",
           "Đáp án: B. 错觉 – 产生错觉, hiểu lầm",
           "(3) 不知是什么缘故，大家都有意无意地（ ）了他。\nA.疏离 B.疏忽 C.疏远 D.生疏",
           "Đáp án: C. 疏远 – xa lánh (một người)"],
    say=["Bài tập hai: chọn đáp án đúng.",
         F(0, "Câu một: 河南安阳出土了一大批甲骨，上面的文字只有古文字学家才能什么。 Ở An Dương, Hà Nam khai quật được rất nhiều mai rùa xương thú, chữ trên đó chỉ có các nhà cổ văn tự học mới có thể thế nào. Bốn lựa chọn: 解读，解说，解决，排解."),
         F(1, "Đáp án: A, 解读. Đọc hiểu và giải thích văn tự cổ là 解读. 解说 là thuyết minh, bình luận; 解决 là giải quyết vấn đề; 排解 là giải tỏa nỗi buồn."),
         F(2, "Câu hai: 我频频向他请教问题，让他产生了什么，误以为我对他有意思。 Tôi liên tục hỏi bài anh ấy, khiến anh ấy nảy sinh cái gì, tưởng nhầm tôi có ý với anh. Bốn lựa chọn: 知觉，错觉，幻觉，直觉."),
         F(3, "Đáp án: B, 错觉. 产生错觉, có cảm nhận sai, đi với 误以为, tưởng nhầm. 幻觉 là ảo giác do bệnh lý hay tưởng tượng, thấy những thứ không có thật; 知觉 là tri giác; 直觉 là trực giác."),
         F(4, "Câu ba: 不知是什么缘故，大家都有意无意地什么了他。 Không biết vì duyên cớ gì, mọi người đều cố ý hay vô tình thế nào với anh ấy. Bốn lựa chọn: 疏离，疏忽，疏远，生疏."),
         F(5, "Đáp án: C, 疏远. 疏远 là động từ mang tân ngữ chỉ người, nghĩa là xa lánh. 疏忽 là sơ suất, lơ là; 生疏 là lạ lẫm, lụt nghề; 疏离 thường dùng như tính từ, chỉ trạng thái xa cách, ít mang tân ngữ.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn đáp án đúng (2)", reveal=True, size=33,
    items=["(4) 他（ ）已经知道这个问题的正确答案了，不然怎么会这么胸有成竹呢？\nA.居然 B.诚然 C.不然 D.俨然",
           "Đáp án: D. 俨然 – trông y như, ra vẻ như",
           "(5) 那些战地护士非常勇敢，像天使一样（ ）着伤员们。\nA.维护 B.守护 C.守卫 D.看守",
           "Đáp án: B. 守护 – che chở, chăm sóc",
           "(6) 残酷的战争，吞食人类的良知，（ ）人类的生命。\nA.争夺 B.剥夺 C.抢夺 D.剥削",
           "Đáp án: B. 剥夺 – tước đoạt (sinh mạng, quyền lợi)"],
    say=[F(0, "Câu bốn: 他什么已经知道这个问题的正确答案了，不然怎么会这么胸有成竹呢？ Anh ấy thế nào đã biết đáp án đúng của câu hỏi này rồi, nếu không sao lại tự tin như đã nắm chắc trong tay như vậy? Bốn lựa chọn: 居然，诚然，不然，俨然."),
         F(1, "Đáp án: D, 俨然. Trông anh ấy y như đã biết đáp án. 居然 là không ngờ, biểu thị bất ngờ, không hợp với ngữ cảnh suy đoán; 诚然 là quả thật, đành rằng; 不然 là nếu không, đã có ở vế sau. 胸有成竹 là trong lòng đã có sẵn cây trúc, tức là đã tính trước, nắm chắc."),
         F(2, "Câu năm: 那些战地护士非常勇敢，像天使一样什么着伤员们。 Những nữ y tá chiến trường ấy rất dũng cảm, như những thiên thần thế nào các thương binh. Bốn lựa chọn: 维护，守护，守卫，看守."),
         F(3, "Đáp án: B, 守护. Che chở, chăm sóc người là 守护. 维护 là giữ gìn quyền lợi, trật tự; 守卫 là canh gác, bảo vệ vùng đất, cửa ải; 看守 là canh giữ, trông coi, có khi là canh phạm nhân."),
         F(4, "Câu sáu: 残酷的战争，吞食人类的良知，什么人类的生命。 Chiến tranh tàn khốc nuốt chửng lương tri, thế nào sinh mạng con người. Bốn lựa chọn: 争夺，剥夺，抢夺，剥削."),
         F(5, "Đáp án: B, 剥夺. 剥夺生命 là tước đoạt sinh mạng. 争夺 là tranh giành; 抢夺 là cướp đoạt đồ vật; 剥削 là bóc lột sức lao động.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ và câu mẫu cho sẵn để trả lời", reveal=True, size=31,
    items=["(1) 当今，人们为什么选择朋友圈三天可见甚至屏蔽朋友圈？（说白了）",
           "Đáp án gợi ý: 因为朋友圈成为社交必需品的同时，又让人感到不堪重负。说白了，人们只是想保持一种不冷不热的礼貌。",
           "(2) 特克尔如何定义快餐式的虚拟性社交关系？（说到底）",
           "Đáp án gợi ý: 特克尔认为，这种关系说到底是把每个人简化成实用的客体，美好的一面被放大，真实的缺点却被隐匿了。",
           "(3) 人们为什么把秒回当作微信社交的第一美德？（比起……更……）",
           "Đáp án gợi ý: 因为在快节奏的网络社交中，比起回复的质量，人们更在乎回复的速度。",
           "(4) 明确了朋友圈的真相，我们该如何做？（在……的同时，更要……）",
           "Đáp án gợi ý: 我们应该把时间和精力留给现实关系和自己，在享受网络社交带来便利的同时，更要守护内心的纯粹和真诚。"],
    say=["Bài tập ba: dùng từ ngữ và câu mẫu cho sẵn để trả lời câu hỏi. Thầy đưa ra đáp án gợi ý.",
         F(0, "Câu một: 当今，人们为什么选择朋友圈三天可见甚至屏蔽朋友圈？ Ngày nay, vì sao người ta chọn cho vòng bạn bè chỉ hiển thị ba ngày, thậm chí ẩn hẳn? Dùng 说白了. Các bạn tạm dừng và thử trả lời nhé."),
         F(1, "Đáp án gợi ý: 因为朋友圈成为社交必需品的同时，又让人感到不堪重负。说白了，人们只是想保持一种不冷不热的礼貌。 Vì vòng bạn bè vừa thành thứ thiết yếu, lại vừa khiến người ta quá tải. Nói trắng ra, người ta chỉ muốn giữ một kiểu lịch sự không nóng không lạnh."),
         F(2, "Câu hai: 特克尔如何定义快餐式的虚拟性社交关系？ Turkle định nghĩa quan hệ ảo kiểu ăn liền như thế nào? Dùng 说到底."),
         F(3, "Đáp án gợi ý: 特克尔认为，这种关系说到底是把每个人简化成实用的客体，美好的一面被放大，真实的缺点却被隐匿了。"),
         F(4, "Câu ba: 人们为什么把秒回当作微信社交的第一美德？ Vì sao người ta coi trả lời ngay là đức tính số một? Dùng 比起……更……."),
         F(5, "Đáp án gợi ý: 因为在快节奏的网络社交中，比起回复的质量，人们更在乎回复的速度。 Vì trong giao tiếp mạng nhịp độ nhanh, so với chất lượng, người ta quan tâm hơn đến tốc độ trả lời."),
         F(6, "Câu bốn: 明确了朋友圈的真相，我们该如何做？ Hiểu rõ bản chất của vòng bạn bè rồi, chúng ta nên làm gì? Dùng 在……的同时，更要……."),
         F(7, "Đáp án gợi ý: 我们应该把时间和精力留给现实关系和自己，在享受网络社交带来便利的同时，更要守护内心的纯粹和真诚。 Chúng ta nên dành thời gian và sức lực cho các mối quan hệ thật và cho bản thân; trong khi tận hưởng sự tiện lợi của mạng xã hội, càng phải gìn giữ sự thuần khiết và chân thành trong lòng.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Dùng từ cho sẵn điền vào đoạn văn", reveal=True, size=32,
    items=["## Từ cho sẵn: 扼杀 · 愈加 · 排解 · 虚拟 · 波澜 · 不冷不热 · 敷衍",
           "日本传播学者中野牧在1980年曾经提出过“容器人”的概念。它指的是：在电视等大众媒介环境中成长起来的现代人，他们就像是一个封闭的容器，每次社交都只是容器外壁的碰撞，内心毫无___。",
           "Đáp án: 波澜",
           "40年过去了，这种情况愈演愈烈，在互联网等___社交媒介中成长起来的我们变得___封闭。互联网看似方便了人与人之间的社交，却___了彼此间的深度交往，使我们变成了一座孤岛，充斥着无法___的孤独感。时下的社交场合中，我们哪怕面对面坐在一起吃饭，也只有___的客气加___的交流。",
           "Đáp án: 虚拟 · 愈加 · 扼杀 · 排解 · 不冷不热 · 敷衍"],
    say=["Bài tập bốn: dùng bảy từ cho sẵn điền vào đoạn văn: 扼杀，愈加，排解，虚拟，波澜，不冷不热，敷衍.",
         F(1, "Đoạn một: 日本传播学者中野牧在一九八零年曾经提出过容器人的概念。它指的是：在电视等大众媒介环境中成长起来的现代人，他们就像是一个封闭的容器，每次社交都只是容器外壁的碰撞，内心毫无什么。 Năm một nghìn chín trăm tám mươi, học giả truyền thông Nhật Bản Nakano Maki đưa ra khái niệm con người vật chứa: người hiện đại lớn lên trong môi trường truyền thông đại chúng như ti vi giống như những chiếc bình kín, mỗi lần giao tiếp chỉ là vỏ ngoài va chạm nhau."),
         F(2, "Đáp án: 波澜. 内心毫无波澜, trong lòng không chút gợn sóng, đúng như cụm trong bài khóa."),
         F(3, "Đoạn hai: 四十年过去了，这种情况愈演愈烈，在互联网等什么社交媒介中成长起来的我们变得什么封闭。互联网看似方便了人与人之间的社交，却什么了彼此间的深度交往，使我们变成了一座孤岛，充斥着无法什么的孤独感。时下的社交场合中，我们哪怕面对面坐在一起吃饭，也只有什么的客气加什么的交流。 Các bạn điền sáu chỗ trống còn lại nhé."),
         F(4, "Đáp án: 虚拟社交媒介, phương tiện giao tiếp ảo; 变得愈加封闭, trở nên càng khép kín; 扼杀了彼此间的深度交往, bóp chết sự giao lưu sâu sắc giữa con người; 无法排解的孤独感, nỗi cô đơn không thể giải tỏa; 不冷不热的客气加敷衍的交流, sự khách sáo hờ hững cộng với những trao đổi qua loa. 愈演愈烈 là ngày càng trầm trọng; 孤岛 là hòn đảo cô độc.")])

# ======================= THẢO LUẬN =======================
add("bullets", chapter="Thảo luận", section="Thảo luận 讨论", title="Thảo luận: bạn và mạng xã hội", reveal=True, size=32,
    items=["(1) 你更喜欢网络社交还是面对面交流？为什么？",
           "Đáp án gợi ý: 我更喜欢面对面交流。网络社交固然方便，可是面对面交流更真诚，也更容易建立深度关系。",
           "(2) 你会设置“朋友圈三天可见”吗？为什么？",
           "Đáp án gợi ý: 我会。说白了，我不想让不太熟的人看到我太多的生活，想保护自己的隐私。",
           "(3) 如果没有线上社交，你是否感到孤独？",
           "Đáp án gợi ý: 刚开始可能会，但是我会把时间留给家人、朋友和自己，比起刷手机，这样的生活更充实。"],
    say=["Bây giờ chúng ta cùng thảo luận. Thầy đưa ra đáp án gợi ý bằng tiếng Trung, các bạn hãy thử nói theo ý mình trước nhé.",
         F(0, "Câu một: 你更喜欢网络社交还是面对面交流？为什么？"),
         F(1, "Gợi ý: 我更喜欢面对面交流。网络社交固然方便，可是面对面交流更真诚，也更容易建立深度关系。 Tôi thích trò chuyện trực tiếp hơn. Giao tiếp mạng đành là tiện, nhưng trò chuyện trực tiếp chân thành hơn, cũng dễ tạo nên quan hệ sâu sắc hơn. Câu này dùng lại mẫu 固然……可是…… của bài hai chấm một."),
         F(2, "Câu hai, thầy thêm vào từ phần ôn tập của sách: 你会设置朋友圈三天可见吗？为什么？ Bạn có cài đặt vòng bạn bè chỉ hiển thị ba ngày không? Ở Việt Nam, câu hỏi tương tự là: bạn có để chế độ chỉ mình tôi hay giới hạn bài viết cũ trên Facebook không?"),
         F(3, "Gợi ý: 我会。说白了，我不想让不太熟的人看到我太多的生活，想保护自己的隐私。 Có. Nói trắng ra, tôi không muốn người không thân lắm nhìn thấy quá nhiều về cuộc sống của mình, muốn bảo vệ đời tư."),
         F(4, "Câu ba: 如果没有线上社交，你是否感到孤独？"),
         F(5, "Gợi ý: 刚开始可能会，但是我会把时间留给家人、朋友和自己，比起刷手机，这样的生活更充实。 Lúc đầu có lẽ sẽ có, nhưng tôi sẽ dành thời gian cho gia đình, bạn bè và bản thân; so với lướt điện thoại, cuộc sống như vậy phong phú hơn. 刷手机 là lướt điện thoại.")])

# ======================= TỔNG KẾT BÀI =======================
add("bullets", chapter="Tổng kết bài 2.3", section="Tổng kết", title="Tổng kết bài 2.3", size=34,
    items=["Nội dung: 群体性孤独 · 科技愈加便利，交往却愈加疏远 · 三大错觉 · 朋友圈 ≠ 真实生活",
           "Từ vựng trọng tâm: 扼杀 · 当下 · 解读 · 虚拟 · 不堪 · 屏蔽 · 波澜 · 愈加 · 挖掘 · 根源 · 伪装 · 隐匿 · 错觉 · 倾听 · 束缚 · 排解 · 俨然 · 剥夺 · 敷衍 · 警惕 · 纯粹",
           "Thành ngữ: 不冷不热 · 恰恰相反 · 一言不合 · 有意无意 · 心照不宣",
           "Câu mẫu: 与……形成对比的是 · 说白了 · 说到底 · 比起……更…… · 半A不B · 不在少数 · 白白 · 把A与B划等号 · 在……的同时，更要……"],
    say=["Chúng ta cùng tổng kết bài hai chấm ba.",
         F(0, "Về nội dung: mạng xã hội khiến chúng ta ở bên nhau mà vẫn cô đơn. Công nghệ càng tiện lợi, con người càng xa cách. Giao tiếp ảo tạo ra ba ảo giác, và đừng đánh đồng vòng bạn bè của một người với cuộc sống thật của họ."),
         F(1, "Về từ vựng, các bạn cần đặc biệt nhớ: 扼杀，当下，解读，虚拟，不堪，屏蔽，波澜，愈加，挖掘，根源，伪装，隐匿，错觉，倾听，束缚，排解，俨然，剥夺，敷衍，警惕，纯粹."),
         F(2, "Về thành ngữ: 不冷不热，恰恰相反，一言不合，有意无意，心照不宣."),
         F(3, "Về câu mẫu: 与……形成对比的是, đối lập với… là…; 说白了, nói trắng ra; 说到底, suy cho cùng; 比起……更……, so với… thì càng…; 半A不B, nửa nọ nửa kia; 不在少数, không ít; 白白, uổng phí; 把A与B划等号, đánh đồng A với B; và 在……的同时，更要……, trong khi…, càng phải…. Tiếp theo, chúng ta ôn tập toàn bộ Đơn vị hai.")])

# ======================= ÔN TẬP ĐƠN VỊ =======================
add("bullets", chapter="Ôn tập đơn vị", section="Ôn tập đơn vị 单元练习", title="Ôn tập Đơn vị 2 (时代篇): ba bài, một thời đại", size=33,
    items=["## 2.1 融不进的城市，回不去的农村 – 新生代农民工",
           "向往城市，却不被城市所接纳；根在农村，却对农村日益疏远 · 纵然……也…… · 固然……可是……",
           "## 2.2 信息化社会：“一个都不能少” – 老年人与数字鸿沟",
           "文化反哺 · 给“快时代”留个“慢选项” · 鉴于 · 致力于 · 由此可见",
           "## 2.3 群体性孤独 – 网络社交与深度关系",
           "科技愈加便利，交往却愈加疏远 · 说白了 · 说到底 · 把A与B划等号",
           "## 单元练习 (学以致用): 新闻报告 · 明察暗访 · 众说纷纭 · 建言献策 · 权衡利弊 · 针锋相对 · 妙笔生花"],
    say=["Bây giờ là phần ôn tập Đơn vị hai, theo mục 单元练习 của sách, sách gọi là 学以致用, học để vận dụng. Trước hết, chúng ta nhìn lại ba bài của đơn vị.",
         F(0, "Bài hai chấm một: 融不进的城市，回不去的农村, viết về lao động nhập cư thế hệ mới."),
         F(1, "Câu then chốt: 向往城市，却不被城市所接纳；根在农村，却对农村日益疏远. Câu mẫu quan trọng: 纵然……也…… và 固然……可是……."),
         F(2, "Bài hai chấm hai: 信息化社会：一个都不能少, viết về người cao tuổi và khoảng cách số."),
         F(3, "Ý then chốt: con cháu cần mớm ngược văn hóa, và xã hội cần để lại một lựa chọn chậm trong thời đại nhanh. Câu mẫu quan trọng: 鉴于，致力于，由此可见."),
         F(4, "Bài hai chấm ba: 群体性孤独, viết về mạng xã hội và các mối quan hệ sâu sắc."),
         F(5, "Câu then chốt: 科技愈加便利，交往却愈加疏远. Câu mẫu quan trọng: 说白了，说到底，把A与B划等号."),
         F(6, "Ba bài đều nói về những người bị bỏ lại hoặc bị chia cắt trong thời đại thay đổi nhanh: người lao động trẻ giữa thành phố và nông thôn, người già giữa thế giới cũ và thế giới số, và mỗi chúng ta giữa quan hệ ảo và quan hệ thật. Phần luyện tập của đơn vị gồm bảy loại hoạt động: báo cáo tin tức, khảo sát thực tế, thảo luận, hiến kế, cân nhắc lợi hại, tranh biện và viết văn. Thầy sẽ đi qua những phần quan trọng nhất.")])

add("bullets", section="Ôn tập đơn vị 单元练习", title="新闻报告 · 明察暗访: báo cáo tin tức và khảo sát", size=32,
    items=["## Hai thế hệ lao động nhập cư (新闻报告一)",
           "“老一代是拉着蛇皮袋进城的，新生代是带着拉杆箱；老一代的目标是挣钱回乡发展，新生代的目标是融入城市发展……”",
           "## Người già và thời đại thông minh (新闻报告二、三)",
           "陌生的二维码、复杂的家电和智能手机、怎么招手都不停的网约车…… · 老年网红",
           "## Khảo sát (明察暗访)",
           "Phỏng vấn người trung niên, cao tuổi về điện thoại thông minh · Khảo sát vì sao nhiều người cài đặt “三天可见”"],
    say=[F(0, "Phần một là 新闻报告, báo cáo tin tức. Tư liệu thứ nhất so sánh hai thế hệ lao động nhập cư."),
         F(1, "老一代是拉着蛇皮袋进城的，新生代是带着拉杆箱；老一代的目标是挣钱回乡发展，新生代的目标是融入城市发展。 Thế hệ cũ kéo bao tải dứa lên thành phố, thế hệ mới thì kéo vali; thế hệ cũ đặt mục tiêu kiếm tiền rồi về quê phát triển, thế hệ mới muốn hòa nhập để phát triển ở thành phố. Sách còn viết: 老一代要求支付工资，新生代要求参加保险, thế hệ cũ đòi trả lương, thế hệ mới đòi được đóng bảo hiểm. Đây chính là nội dung của bài hai chấm một."),
         F(2, "Tư liệu thứ hai và thứ ba nói về người già trong thời đại thông minh."),
         F(3, "陌生的二维码、复杂的家电和智能手机、怎么招手都不停的网约车. Mã QR lạ lẫm, đồ điện gia dụng và điện thoại phức tạp, xe công nghệ vẫy mãi không dừng. Có cụ già than: 不愁吃穿的年代，竟被新技术抛弃了, thời không lo cơm áo, lại bị công nghệ mới bỏ rơi. Mặt khác, cũng có nhiều cụ trở thành 老年网红, người nổi tiếng trên mạng, trên các nền tảng như Douyin, Bilibili."),
         F(4, "Phần hai là 明察暗访, khảo sát thực tế."),
         F(5, "Sách gợi ý hai cuộc khảo sát: phỏng vấn người trung niên, cao tuổi về việc dùng điện thoại thông minh, như 您什么时候开始使用智能手机的？使用智能手机时觉得有哪些困难？; và khảo sát vì sao nhiều người cài đặt vòng bạn bè chỉ hiển thị ba ngày. Các bạn có thể làm khảo sát nhỏ với người thân, bạn bè người Việt rồi kể lại bằng tiếng Trung.")])

add("bullets", section="Ôn tập đơn vị 单元练习", title="众说纷纭: thảo luận", reveal=True, size=32,
    items=["(1) 梭罗《瓦尔登湖》：“在小屋里有三把椅子，独处时用一把，交友时用两把，社交时用三把。”在互联网时代该如何用好这“三把椅子”？",
           "Đáp án gợi ý: 第一把椅子提醒我们要留时间独处、和自己交谈；第二把椅子是和朋友面对面深谈；第三把椅子是参与群体。网络社交不能代替前两把椅子。",
           "(2) 为什么吃小龙虾时更能和朋友聊得热火朝天？",
           "Đáp án gợi ý: 因为吃小龙虾时，双手忙着剥虾，根本没时间看手机，所以大家只能面对面交流。",
           "(3) 我们更依赖打破时空的社交还是面对面的社交？",
           "Đáp án gợi ý: 说白了，我们离不开网络社交，但真正的深度关系还是需要面对面的交流。"],
    say=["Phần ba là 众说纷纭, mỗi người một ý, tức là thảo luận. Thầy chọn ba đề tài gắn với bài hai chấm ba.",
         F(0, "Đề tài một: nhà văn Mỹ Thoreau, trong cuốn Walden, 瓦尔登湖, viết: 在小屋里有三把椅子，独处时用一把，交友时用两把，社交时用三把。 Trong căn nhà nhỏ có ba chiếc ghế: một mình thì dùng một chiếc, kết bạn thì dùng hai, giao tế thì dùng ba. Ba chiếc ghế tượng trưng cho trò chuyện với chính mình, với người khác và với tập thể. Trong thời đại Internet, nên dùng ba chiếc ghế này thế nào?"),
         F(1, "Gợi ý: 第一把椅子提醒我们要留时间独处、和自己交谈；第二把椅子是和朋友面对面深谈；第三把椅子是参与群体。网络社交不能代替前两把椅子。 Chiếc ghế thứ nhất nhắc ta dành thời gian ở một mình, trò chuyện với bản thân; chiếc thứ hai là trò chuyện sâu với bạn bè; chiếc thứ ba là tham gia tập thể. Giao tiếp mạng không thể thay thế hai chiếc ghế đầu. Sách nói ba chiếc ghế tạo nên một vòng tuần hoàn tốt, nối liền trò chuyện, sự thấu cảm và khả năng tự xét mình."),
         F(2, "Đề tài hai: vì sao khi ăn tôm hùm đất, 小龙虾, người ta lại trò chuyện với bạn bè sôi nổi hơn?"),
         F(3, "Gợi ý: 因为吃小龙虾时，双手忙着剥虾，根本没时间看手机，所以大家只能面对面交流。 Vì khi ăn tôm hùm đất, hai tay bận bóc tôm, chẳng có thời gian xem điện thoại, nên mọi người chỉ có thể trò chuyện trực tiếp. Theo sách, Turkle gọi đó là tôm hùm đất tự mang thuộc tính xã giao. Ở Việt Nam, có lẽ là những buổi ăn ốc, ăn lẩu cùng bạn bè!"),
         F(4, "Đề tài ba: 我们更依赖打破时空的社交还是面对面的社交？ Chúng ta phụ thuộc nhiều hơn vào giao tiếp vượt không gian thời gian, hay giao tiếp mặt đối mặt?"),
         F(5, "Gợi ý: 说白了，我们离不开网络社交，但真正的深度关系还是需要面对面的交流。 Nói trắng ra, chúng ta không thể rời mạng xã hội, nhưng những quan hệ sâu sắc thật sự vẫn cần trò chuyện trực tiếp. Ngoài ra sách còn có hai đề tài về chính sách nhập cư và về sự bình đẳng trên mạng, các bạn có thể tự tìm hiểu thêm.")])

add("bullets", section="Ôn tập đơn vị 单元练习", title="从句段到篇章：权衡利弊 – viết bài bàn về lợi và hại", size=31,
    items=["## 总起 – Mở bài: dẫn ra hiện tượng, định nghĩa, nêu khái quát lợi hại",
           "所谓……是指…… · 凡事有一利必有一弊 · 凡事都有两面性 · 整体来看，……有利有弊/利弊参半/利大于弊/弊大于利 · 对此，人们莫衷一是 · 尺有所短，寸有所长",
           "## 分析 – Thân bài: phân tích mặt lợi, rồi mặt hại, có luận cứ",
           "就有利之处来说，可以分为以下几点 · 其一、其二、其三…… · 不利之处在于…… · 首先是……其次是……此外…… · 拿……来说 · 况且…… · 加之…… · 除此之外……",
           "## 总结与个人评价 – Kết bài: tổng kết và nêu quan điểm",
           "总而言之 · 在我看来 · ……是一把双刃剑 · 瑕不掩瑜 · 固然……但…… · 一分为二地看问题 · 不能因噎废食 · 趋利避害 / 扬长避短 / 取长补短"],
    say=["Phần năm của ôn tập rất quan trọng cho kỹ năng viết: 从句段到篇章：权衡利弊, từ câu đoạn đến bài văn: cân nhắc lợi hại. Bài viết bàn về lợi và hại dùng phép đối chiếu và liệt kê, phân tích ưu điểm và nhược điểm, rồi kết luận bằng quan điểm của người viết. Bài gồm ba phần.",
         F(0, "Phần một, 总起, mở bài: đi thẳng vào vấn đề, dẫn ra hiện tượng, định nghĩa đối tượng, nêu khái quát lợi và hại."),
         F(1, "Các câu hay dùng: 所谓……是指……, cái gọi là… là chỉ…; 凡事有一利必有一弊, việc gì có lợi ắt có hại; 凡事都有两面性, mọi việc đều có hai mặt; 整体来看，有利有弊, 利弊参半, 利大于弊, 弊大于利, nhìn tổng thể là có lợi có hại, lợi hại ngang nhau, lợi nhiều hơn hại, hại nhiều hơn lợi; 对此，人们莫衷一是, về việc này mọi người mỗi người một ý; và 尺有所短，寸有所长, thước có khi ngắn, tấc có khi dài."),
         F(2, "Phần hai, 分析, thân bài: phân tích cụ thể mặt lợi, rồi mặt hại, có lý lẽ và dẫn chứng."),
         F(3, "Các câu hay dùng: 就有利之处来说，可以分为以下几点, xét về mặt lợi, có thể chia thành mấy điểm sau; 其一、其二、其三, thứ nhất, thứ hai, thứ ba; 不利之处在于, mặt bất lợi nằm ở; 首先是，其次是，此外, trước hết, tiếp theo, ngoài ra; 拿……来说, lấy… mà nói; và 况且，加之，除此之外, hơn nữa, thêm vào đó, ngoài ra."),
         F(4, "Phần ba, 总结与个人评价, kết bài: tổng kết và nêu quan điểm của mình."),
         F(5, "Các câu hay dùng: 总而言之, tóm lại; 在我看来, theo tôi; 是一把双刃剑, là con dao hai lưỡi; 瑕不掩瑜, vết nhỏ không che được ngọc; 固然……但……, đành rằng… nhưng…; 一分为二地看问题, nhìn vấn đề theo hai mặt; 不能因噎废食, không thể vì sợ hóc mà bỏ ăn; và 趋利避害，扬长避短，取长补短, hướng lợi tránh hại, phát huy sở trường tránh sở đoản, lấy dài bù ngắn.")])

add("bullets", section="Ôn tập đơn vị 单元练习", title="Luyện viết: 社交媒体的利与弊 – lợi và hại của mạng xã hội", reveal=True, size=31,
    items=["(1) 总起 – Mở bài",
           "Đáp án gợi ý: 所谓社交媒体，是指人们用来分享信息、交流观点的网络平台。凡事有一利必有一弊，社交媒体也是一把双刃剑。",
           "(2) 分析 – Thân bài",
           "Đáp án gợi ý: 就有利之处来说，其一，它打破了时空的限制；其二，它让我们获得信息更方便。不利之处在于：首先，它白白剥夺了我们独立思考的时间；其次，快餐式的虚拟关系正在扼杀深度关系。",
           "(3) 总结与个人评价 – Kết bài",
           "Đáp án gợi ý: 总而言之，我们应该一分为二地看问题，既不能因噎废食，也不能沉迷其中，而要趋利避害，在享受便利的同时，更要守护现实中的深度关系。"],
    say=["Sách yêu cầu luyện viết với đề 社交媒体的利与弊, lợi và hại của mạng xã hội. Thầy gợi ý một dàn bài ngắn theo ba phần, dùng lại nhiều từ và câu mẫu của cả đơn vị.",
         F(0, "Phần mở bài. Các bạn thử viết trước nhé."),
         F(1, "Gợi ý: 所谓社交媒体，是指人们用来分享信息、交流观点的网络平台。凡事有一利必有一弊，社交媒体也是一把双刃剑。 Cái gọi là mạng xã hội là các nền tảng mạng mà con người dùng để chia sẻ thông tin, trao đổi quan điểm. Việc gì có lợi ắt có hại, mạng xã hội cũng là một con dao hai lưỡi."),
         F(2, "Phần thân bài."),
         F(3, "Gợi ý: 就有利之处来说，其一，它打破了时空的限制；其二，它让我们获得信息更方便。不利之处在于：首先，它白白剥夺了我们独立思考的时间；其次，快餐式的虚拟关系正在扼杀深度关系。 Về mặt lợi, thứ nhất, nó phá vỡ giới hạn không gian thời gian; thứ hai, nó giúp ta có thông tin dễ dàng hơn. Mặt hại là: trước hết, nó tước đi một cách uổng phí thời gian suy nghĩ độc lập của ta; tiếp theo, những quan hệ ảo kiểu ăn liền đang bóp chết các mối quan hệ sâu sắc."),
         F(4, "Phần kết bài."),
         F(5, "Gợi ý: 总而言之，我们应该一分为二地看问题，既不能因噎废食，也不能沉迷其中，而要趋利避害，在享受便利的同时，更要守护现实中的深度关系。 Tóm lại, chúng ta nên nhìn vấn đề theo hai mặt, không thể vì sợ hóc mà bỏ ăn, cũng không được đắm chìm trong đó, mà phải hướng lợi tránh hại; trong khi tận hưởng sự tiện lợi, càng phải gìn giữ những mối quan hệ sâu sắc ngoài đời thực. 沉迷 là say mê, đắm chìm.")])

add("bullets", section="Ôn tập đơn vị 单元练习", title="针锋相对 · 妙笔生花: tranh biện và viết văn", size=32,
    items=["## 辩论题 – Đề tranh biện",
           "应支持更严格的移民政策还是更开放的移民政策？",
           "社交媒体是扩大了还是缩小了我们的社交范围？ · 社交媒体让人更亲近还是更疏远？ · 网恋找得到真爱吗？",
           "## 作文 – Viết văn (không dưới 800 chữ, tự đặt tên)",
           "Đề 1: đọc tư liệu về 新生代农民工 (“三高一低”), viết cảm nghĩ – “他们的命运，不该是父辈的轮回。”",
           "Đề 2: phỏng vấn một người cao tuổi – “莫道桑榆晚，为霞尚满天。”"],
    say=[F(0, "Phần sáu là 针锋相对, mũi kim chọi nhau, tức là tranh biện. Sách đưa ra hai nhóm đề."),
         F(1, "Nhóm một: 应支持更严格的移民政策还是更开放的移民政策？ Nên ủng hộ chính sách nhập cư chặt chẽ hơn hay cởi mở hơn?"),
         F(2, "Nhóm hai, chọn một đề: 社交媒体是扩大了还是缩小了我们的社交范围？ Mạng xã hội mở rộng hay thu hẹp phạm vi giao tiếp của chúng ta? 社交媒体让人更亲近还是更疏远？ Mạng xã hội làm con người gần nhau hơn hay xa nhau hơn? Hay vui hơn: 网恋找得到真爱吗？ Yêu qua mạng có tìm được tình yêu đích thực không? Khi tranh biện, các bạn hãy dùng các câu mẫu như 固然……可是……，说到底，比起……更……."),
         F(3, "Phần bảy là 妙笔生花, ngòi bút nở hoa, tức là viết văn, mỗi bài không dưới tám trăm chữ, tự đặt tên."),
         F(4, "Đề một: đọc tư liệu về lao động nhập cư thế hệ mới. Họ có đặc điểm ba cao một thấp, 三高一低: trình độ học vấn cao, kỳ vọng nghề nghiệp cao, yêu cầu hưởng thụ vật chất và tinh thần cao, nhưng sức chịu đựng công việc thấp. Tư liệu kết thúc bằng câu: 他们的命运，不该是父辈的轮回, số phận của họ không nên là sự lặp lại vòng đời của cha ông."),
         F(5, "Đề hai: phỏng vấn một người cao tuổi bên cạnh mình về những điều họ quan tâm và cách nhìn về thời đại, về cuộc đời. Sách dẫn hai câu thơ: 夕阳无限好，只是近黄昏, hoàng hôn đẹp vô hạn, chỉ tiếc đã gần tối, của Lý Thương Ẩn; và 莫道桑榆晚，为霞尚满天, chớ bảo bóng chiều đã muộn, ráng chiều vẫn đỏ rực trời, của Lưu Vũ Tích, thể hiện tinh thần lạc quan của tuổi già.")])

add("bullets", chapter="Tổng kết & bài sau", section="Tổng kết", title="Kết thúc Đơn vị 2 – bài tập về nhà", size=36,
    items=["Ôn lại từ vựng và câu mẫu của 3 bài: 2.1 · 2.2 · 2.3",
           "Viết bài 400–800 chữ: 社交媒体的利与弊 (theo cấu trúc 总起 → 分析 → 总结)",
           "Dùng ít nhất 5 cách nói của bảng 权衡利弊 và 3 câu mẫu của đơn vị",
           "Bài sau: Đơn vị 3 · 环保篇 · Bài 3.1 碳排放的“蛋糕”怎么切？"],
    say=["Như vậy là chúng ta đã hoàn thành Đơn vị hai, chủ đề Thời đại.",
         F(0, "Các bạn hãy ôn lại từ vựng và câu mẫu của cả ba bài. Trên trang web học tập, các bạn có thể dùng thẻ ghi nhớ để ôn từ."),
         F(1, "Bài tập về nhà: viết một bài từ bốn trăm đến tám trăm chữ với đề 社交媒体的利与弊, theo cấu trúc ba phần: mở bài, thân bài, kết bài."),
         F(2, "Hãy dùng ít nhất năm cách nói trong bảng cân nhắc lợi hại, như 凡事有一利必有一弊，就有利之处来说，是一把双刃剑，趋利避害, và ít nhất ba câu mẫu của đơn vị, như 固然……可是……，说白了，在……的同时，更要……."),
         F(3, "Cảm ơn các bạn đã theo dõi bài giảng. Bài sau, chúng ta bước sang Đơn vị ba, 环保篇, chủ đề Bảo vệ môi trường, với bài ba chấm một: 碳排放的蛋糕怎么切？ Chia chiếc bánh phát thải carbon thế nào? Đó là một cuộc phỏng vấn về Hội nghị thượng đỉnh khí hậu Copenhagen và cuộc tranh cãi về quyền phát thải giữa các nước. Hẹn gặp lại các bạn. Chúc các bạn học tốt!")])

lesson = {
    "title": "顶石中文 – Bài 2.3: 群体性孤独：网络社交正在扼杀深度关系 (Cô đơn tập thể: mạng xã hội đang bóp chết những mối quan hệ sâu sắc)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"重构": "虫构",            # chónggòu
                    "剥夺": "波夺",            # bōduó
                    "剥削": "波削",            # bōxuē
                    "剥虾": "包虾",            # bāo xiā
                    "弹窗": "谈窗",            # tánchuāng
                    "身处": "身楚",            # shēnchǔ
                    "独处": "独楚",            # dúchǔ
                    "自省": "自醒",            # zìxǐng
                    "为霞": "维霞",            # wéi xiá
                    "宝藏": "宝葬",            # bǎozàng
                    "间隙": "见隙",            # jiànxì
                    "所长": "所常",            # 寸有所长: cháng
                    "扬长": "扬常",            # yángcháng
                    "取长": "取常",            # qǔcháng
                    "热火朝天": "热火潮天",    # cháo
                    "划等号": "话等号",        # huà
                    "当下": "当夏",            # dāngxià
                    "说白了": "说白勒",        # le
                    "恶意": "饿意",            # èyì
                    "着迷": "着迷"},
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds23.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
