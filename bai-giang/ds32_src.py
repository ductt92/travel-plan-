#!/usr/bin/env python3
"""Kịch bản bài giảng 顶石中文 – Bài 3.2 «“随手扔”还是“随手分”，你“拎得清”吗？». Chạy để sinh ds32.json."""
import json
import os

TAG = "顶石中文 · Bài 3.2 · “随手扔”还是“随手分”，你“拎得清”吗？"
slides = []


def add(type_, chapter=None, section="", **kw):
    s = {"type": type_, "section": section, **kw}
    if chapter:
        s["chapter"] = chapter
    slides.append(s)


def F(i, t, **kw):
    return {"t": t, "f": i, **kw}


# ======================= MỞ ĐẦU =======================
# tên bài dài: tách hai dòng như Bài 40 (dòng đầu của "sub" là pinyin đầy đủ)
add("title", chapter="Mở đầu",
    top="顶石中文 – Đỉnh cao tiếng Trung",
    zh="“随手扔”还是“随手分”", py="你“拎得清”吗？",
    vi="Bài 3.2: “Tiện tay vứt” hay “tiện tay phân loại”, bạn có rõ không?",
    sub="“Suíshǒu rēng” háishi “suíshǒu fēn”, nǐ “līn de qīng” ma?\nBài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng giáo trình 顶石中文, Đỉnh cao tiếng Trung.",
         "Hôm nay chúng ta học bài ba chấm hai: 随手扔还是随手分，你拎得清吗？ Nghĩa là: Tiện tay vứt hay tiện tay phân loại, bạn có phân biệt rõ không?",
         "Đây là bài thứ hai của Đơn vị ba, 环保篇, chủ đề Bảo vệ môi trường. Nếu bài trước bàn chuyện khí hậu của cả thế giới, thì bài này nói về một việc rất đời thường: phân loại rác. Ngày một tháng bảy năm 2019, Thượng Hải bắt đầu bắt buộc phân loại rác, và chuyện đổ rác bỗng trở thành đề tài cả nước bàn tán.",
         "Bài khóa là cuộc đối thoại giữa hai bình luận viên của Nhân dân Nhật báo và Giải phóng Nhật báo, bàn về kinh nghiệm của Thượng Hải: làm sao để một chính sách mới đi vào cuộc sống, từ một trào lưu trở thành thói quen hằng ngày."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học", size=40,
    items=["Hiểu bài đối thoại: kinh nghiệm phân loại rác của Thượng Hải, “cương nhu kết hợp”",
           "Nắm vững 51 từ mới, kèm âm Hán Việt và ví dụ",
           "8 mẫu câu: 一V了之 · A归A · 区区 · 何必 · 并非……而是…… · 为……做铺垫 · 经过……磨合 · 终究",
           "Kết hợp từ (消磨 · 纵观 · 填补 · 鼓足 · 树立) và 8 thành ngữ",
           "Làm bài tập của sách; thảo luận: phân loại rác ở Việt Nam"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài đối thoại: Thượng Hải đã làm thế nào để chính sách phân loại rác có một khởi đầu suôn sẻ, và vì sao chính sách cần cương nhu kết hợp."),
         F(1, "Thứ hai, nắm vững năm mươi mốt từ mới, kèm âm Hán Việt, nghĩa và ví dụ."),
         F(2, "Thứ ba, học tám mẫu câu trọng điểm: 一扔了之 của mẫu 一 động từ 了之, 玩笑归玩笑 của mẫu A归A, 区区，何必, 并非而是, 为某事做铺垫, 经过磨合, và 终究."),
         F(3, "Thứ tư, học kết hợp từ của 消磨，纵观，填补，鼓足，树立, cùng tám thành ngữ rất hay dùng như 一蹴而就，循序渐进，坚持不懈."),
         F(4, "Thứ năm, làm các bài tập của sách, và thảo luận: ở Việt Nam, rác sinh hoạt được xử lý thế nào."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 课前思考", title="Câu hỏi khởi động 课前思考", size=38,
    items=["1．在你们国家，家庭生活的垃圾是如何处理的？",
           "2．政府主导垃圾分类进入“强制时代”是否符合大多数人的意愿？",
           "3．垃圾分类处理政策实施有哪些困难？",
           "Gợi ý: thói quen khó đổi · thiếu thùng rác phân loại · “phân loại xong lại đổ chung” · chi phí xử lý"],
    say=["Trước khi vào bài, sách đưa ra ba câu hỏi để chúng ta suy nghĩ.",
         F(0, "Câu một: 在你们国家，家庭生活的垃圾是如何处理的？ Ở nước bạn, rác sinh hoạt gia đình được xử lý thế nào? Câu này chúng ta sẽ thảo luận kỹ ở cuối bài."),
         F(1, "Câu hai: 政府主导垃圾分类进入强制时代是否符合大多数人的意愿？ Việc chính phủ dẫn dắt phân loại rác bước vào thời đại bắt buộc có phù hợp với mong muốn của đa số người dân không? 主导 là chủ đạo, dẫn dắt; 强制 là cưỡng chế, bắt buộc; 意愿 là nguyện vọng."),
         F(2, "Câu ba: 垃圾分类处理政策实施有哪些困难？ Thực hiện chính sách phân loại và xử lý rác gặp những khó khăn gì?"),
         F(3, "Gợi ý: thói quen lâu năm khó thay đổi; thiếu thùng rác phân loại; người dân lo phân loại xong rồi xe rác lại đổ chung; chi phí xử lý cao. Các bạn tạm dừng và thử trả lời bằng tiếng Trung nhé, ví dụ: 最大的困难是人们的习惯很难改变。")])

add("bullets", section="Khởi động 课前思考", title="Bối cảnh: Thượng Hải chia rác thành bốn loại", size=36,
    items=["## 可回收物 – rác tái chế: giấy, chai nhựa, kim loại, thủy tinh, quần áo cũ…",
           "## 有害垃圾 – rác độc hại: pin, bóng đèn, thuốc hết hạn, sơn…",
           "## 湿垃圾 – rác ướt (rác nhà bếp): thức ăn thừa, vỏ trái cây, rau củ…",
           "## 干垃圾 – rác khô: phần còn lại (khăn giấy ướt, tã giấy, gốm sứ vỡ…)",
           "Mẹo của dân mạng: 猪能吃的是湿垃圾，猪都不吃的是干垃圾，猪吃了会死的是有害垃圾，卖了能买猪的是可回收垃圾"],
    say=["Để hiểu bài khóa, chúng ta cần biết Thượng Hải chia rác thành bốn loại như thế nào.",
         F(0, "Loại thứ nhất: 可回收物, rác có thể tái chế, như giấy, chai nhựa, kim loại, thủy tinh, quần áo cũ."),
         F(1, "Loại thứ hai: 有害垃圾, rác độc hại, như pin, bóng đèn, thuốc hết hạn, sơn."),
         F(2, "Loại thứ ba: 湿垃圾, rác ướt, thực chất là rác nhà bếp dễ phân hủy, như thức ăn thừa, vỏ trái cây, rau củ."),
         F(3, "Loại thứ tư: 干垃圾, rác khô, tức là tất cả những thứ còn lại, như khăn giấy ướt, tã giấy, gốm sứ vỡ. Các bạn thấy đấy, khăn giấy ướt lại là rác khô, nên mới có câu đùa trong bài khóa."),
         F(4, "Để nhớ, dân mạng nghĩ ra mẹo con lợn: 猪能吃的是湿垃圾，猪都不吃的是干垃圾，猪吃了会死的是有害垃圾，卖了能买猪的是可回收垃圾。 Thứ lợn ăn được là rác ướt; thứ lợn cũng chê là rác khô; thứ lợn ăn vào mà chết là rác độc hại; thứ bán đi mua được lợn là rác tái chế.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("条例", "tiáolì", "điều lệ", "danh từ", "điều lệ, quy định (do nhà nước ban hành)", "城市绿化条例已经正式实施。", "Điều lệ phủ xanh đô thị đã chính thức có hiệu lực.",
     "Danh từ, nghĩa là văn bản quy định do cơ quan hành chính nhà nước hay tổ chức ban hành. Trong bài: 上海市生活垃圾管理条例, Điều lệ quản lý rác thải sinh hoạt thành phố Thượng Hải, gọi tắt là 条例, đặt trong dấu sách."),
    ("热词", "rècí", "nhiệt từ", "danh từ", "từ khóa hot, từ ngữ thịnh hành", "“内卷”成了这几年的网络热词。", "“Nội quyển” đã thành từ khóa hot trên mạng mấy năm nay.",
     "Danh từ, nghĩa là từ ngữ thịnh hành, mang dấu ấn thời đại, phản ánh vấn đề nóng của một giai đoạn, như 内卷, cuộc đua khốc liệt vô nghĩa, hay 打工人, người làm công. Từ cùng họ trong bài: 热议, bàn tán sôi nổi. Trong bài: 垃圾分类一时间成了热词, phân loại rác bỗng chốc thành từ khóa hot."),
    ("废弃物", "fèiqìwù", "phế khí vật", "danh từ", "chất thải, đồ bỏ đi", "这些废弃物可以回收利用。", "Những chất thải này có thể thu hồi để tái sử dụng.",
     "Danh từ, chỉ những thứ sinh ra trong quá trình sống và sản xuất mà không còn giá trị giữ lại hay sử dụng. 废 là bỏ, 弃 là vứt bỏ, 物 là vật. Trong bài: 将废弃物胡乱丢进垃圾桶, vứt bừa đồ bỏ đi vào thùng rác."),
    ("胡乱", "húluàn", "hồ loạn", "phó từ", "bừa bãi, qua loa, tùy tiện", "他胡乱吃了几口就走了。", "Anh ấy ăn qua loa vài miếng rồi đi.",
     "Phó từ, nghĩa là làm một cách bừa bãi, cẩu thả, không suy nghĩ. Chữ 胡 ở đây là bừa, như trong 胡说, nói bừa. Trong bài: 胡乱丢进垃圾桶, vứt bừa vào thùng rác."),
    ("吐槽", "tùcáo", "thổ tào", "động từ", "chê bai, “cà khịa”, châm chọc", "网友们纷纷吐槽这部电影太无聊。", "Cư dân mạng thi nhau chê bộ phim này quá chán.",
     "Động từ, từ mạng, nghĩa là bắt lấy một sơ hở hay một từ khóa trong lời nói, hành động của người khác để bình luận mang tính trêu chọc, chế giễu; gần với cà khịa trong tiếng Việt. Trong bài: 上海人用吐槽的方式学习和传播着分类知识, người Thượng Hải học và truyền bá kiến thức phân loại bằng những câu đùa tự trào."),
    ("分寸", "fēncun", "phân thốn", "danh từ", "chừng mực", "他说话很有分寸。", "Anh ấy ăn nói rất có chừng mực.",
     "Danh từ, nghĩa là mức độ thích hợp khi nói năng, làm việc; âm tiết sau đọc nhẹ. Hay gặp: 有分寸, có chừng mực; 乱了分寸, rối trí, mất bình tĩnh. Trong bài: 明事理、知分寸, hiểu lẽ phải, biết chừng mực; 事理 là đạo lý của sự việc."),
    ("褒奖", "bāojiǎng", "bao tưởng", "động từ", "khen ngợi, khen thưởng", "他因突出贡献受到了褒奖。", "Anh ấy được khen thưởng vì có đóng góp nổi bật.",
     "Động từ, nghĩa là biểu dương, khen ngợi, khen thưởng; cũng làm danh từ, lời khen. Chữ 褒 là khen, ngược với 贬, chê: 褒义词 là từ mang nghĩa khen. Trong bài: 拎得清 là lời khen trong tiếng Thượng Hải."),
    ("拷问", "kǎowèn", "khảo vấn", "động từ", "tra hỏi; tự vấn", "这是一次来自灵魂的拷问。", "Đây là một câu hỏi chất vấn đến tận tâm hồn.",
     "Động từ, nghĩa gốc là tra hỏi, tra khảo; trong bài dùng theo nghĩa tự hỏi, tự xét lại mình: 出门倒垃圾前的自我拷问, câu tự vấn trước khi ra khỏi nhà đổ rác. Cụm 灵魂拷问, câu hỏi chất vấn lương tâm, rất hay gặp trên mạng."),
    ("区区", "qūqū", "khu khu", "tính từ", "nhỏ nhoi, cỏn con", "区区小事，何足挂齿。", "Chuyện cỏn con, có đáng gì mà nhắc đến.",
     "Tính từ, nghĩa là số lượng ít hoặc không quan trọng, thường mang giọng coi nhẹ. Cẩn thận: tiếng Việt khư khư là ôm chặt; còn 区区 là nhỏ nhoi. Câu khách sáo 区区小事，何足挂齿 là chuyện nhỏ, không đáng nhắc. Đây cũng là một mẫu câu của bài."),
    ("较真", "jiàozhēn", "giảo chân", "tính từ", "quá nghiêm túc, chấp nhặt", "朋友之间开玩笑，不必较真。", "Bạn bè đùa nhau thôi, không cần chấp nhặt.",
     "Tính từ, cũng là động từ ly hợp, nghĩa là quá nghiêm túc, quá coi là chuyện lớn; có khi mang nghĩa tốt là làm đến nơi đến chốn. Trong bài: 区区小事何必那么较真, chuyện cỏn con cần gì phải nghiêm trọng hóa như thế."),
    ("践行", "jiànxíng", "tiễn hành", "động từ", "thực hành, thực hiện", "他用行动践行了自己的诺言。", "Anh ấy đã dùng hành động thực hiện lời hứa của mình.",
     "Động từ, nghĩa là thực hiện, đem vào thực tế, văn viết. Hay gặp: 践行诺言, giữ lời hứa; 践行理念, thực hiện triết lý. Trong bài: 接受并践行这一全新的环保方式, chấp nhận và thực hành phương thức bảo vệ môi trường hoàn toàn mới này."),
    ("开局", "kāijú", "khai cục", "động từ", "khởi đầu, mở màn", "今年一季度工作开局良好。", "Công việc quý một năm nay khởi đầu tốt đẹp.",
     "Động từ, nghĩa gốc là bắt đầu một ván cờ, một trận đấu; nghĩa rộng là bắt đầu một công việc, hoạt động. Trong bài: 实现平稳开局, có được một khởi đầu suôn sẻ."),
    ("试水", "shìshuǐ", "thí thủy", "động từ", "thử nghiệm, dò đường", "一些厂家谨慎试水，小批量生产。", "Một số nhà máy thận trọng thử nghiệm, sản xuất số lượng nhỏ.",
     "Động từ ly hợp, nghĩa đen là thử nước nông sâu, nóng lạnh; nghĩa bóng là thử nghiệm, dò đường trước khi làm thật. Trong bài: 从十九年前率先试水, từ mười chín năm trước đã đi đầu thử nghiệm."),
    ("强制", "qiángzhì", "cưỡng chế", "động từ", "cưỡng chế, bắt buộc", "法院决定强制执行。", "Tòa án quyết định cưỡng chế thi hành.",
     "Động từ, nghĩa là dùng quyền lực buộc phải làm. Hay gặp: 强制执行, cưỡng chế thi hành; 强制措施, biện pháp cưỡng chế. Trong bài: 立法强制执行, lập pháp để bắt buộc thực hiện. Chữ 强 ở đây đọc qiáng, thanh hai."),
    ("试错", "shìcuò", "thí thác", "động từ", "thử và sai", "我们应该在不断试错的过程中获得经验。", "Chúng ta nên tích lũy kinh nghiệm qua việc liên tục thử và sai.",
     "Động từ, nghĩa là khi chưa chắc cách giải quyết có đúng không, thì thử liên tục để loại dần những cách sai. Trong bài: 不断试错和创新的过程, quá trình không ngừng thử sai và đổi mới."),
    ("基层", "jīcéng", "cơ tầng", "danh từ", "cơ sở, cấp cơ sở", "大学毕业后，他到基层工作了三年。", "Tốt nghiệp đại học, anh ấy xuống cơ sở làm việc ba năm.",
     "Danh từ, nghĩa là tầng thấp nhất trong các tổ chức xã hội, gần gũi với quần chúng nhất, tương đương cấp cơ sở. Hay gặp: 基层干部, cán bộ cơ sở; 深入基层, đi sâu xuống cơ sở."),
    ("试点", "shìdiǎn", "thí điểm", "danh từ", "thí điểm", "这个小区是垃圾分类的试点。", "Khu dân cư này là điểm thí điểm phân loại rác.",
     "Danh từ, cũng là động từ, nghĩa là làm thử ở quy mô nhỏ trước khi triển khai chính thức, để rút kinh nghiệm. Âm Hán Việt thí điểm, nghĩa giống hệt tiếng Việt. Trong bài: 基层的大量试点, rất nhiều điểm thí điểm ở cơ sở."),
    ("铺垫", "pūdiàn", "phô điếm", "động từ", "làm nền, chuẩn bị trước", "现在的努力都是为以后做铺垫。", "Những cố gắng bây giờ đều là để chuẩn bị cho sau này.",
     "Động từ, nghĩa gốc là trải lót bên dưới; nghĩa bóng là làm công tác chuẩn bị, tạo tiền đề. Hay dùng trong mẫu 为某事做铺垫, mẫu câu thứ sáu của bài. Chữ 铺 ở đây đọc pū, thanh một."),
    ("切身", "qièshēn", "thiết thân", "động từ", "của chính mình, trực tiếp, thiết thân", "这是我的切身体会。", "Đây là trải nghiệm của chính bản thân tôi.",
     "Theo sách là động từ, nghĩa là chính bản thân mình, liên quan trực tiếp đến mình, thường đứng trước danh từ: 切身感受, cảm nhận trực tiếp; 切身利益, lợi ích thiết thân. Chữ 切 đọc thanh bốn. Trong bài: 切身感受到垃圾围城的风险, tự mình cảm nhận được nguy cơ rác bao vây thành phố."),
    ("理念", "lǐniàn", "lý niệm", "danh từ", "quan niệm, triết lý, tư tưởng", "这所学校的教育理念很先进。", "Triết lý giáo dục của trường này rất tiên tiến.",
     "Danh từ, nghĩa là tư tưởng, quan niệm chỉ đạo hành động. Hay gặp: 教育理念, 人生理念, 环保理念. Trong bài: 垃圾分类理念, ý thức, quan niệm về phân loại rác."),
    ("果断", "guǒduàn", "quả đoán", "tính từ", "quả quyết, dứt khoát", "她果断地拒绝了对方的要求。", "Cô ấy dứt khoát từ chối yêu cầu của đối phương.",
     "Tính từ, nghĩa là quyết đoán, không do dự. Âm Hán Việt quả đoán, nghĩa giống tiếng Việt. Trong bài: 果断坚决, quả quyết, kiên quyết."),
    ("犹疑", "yóuyí", "do nghi", "động từ", "do dự, chần chừ", "他犹疑不决，错过了机会。", "Anh ấy do dự không quyết, bỏ lỡ cơ hội.",
     "Động từ, nghĩa là do dự, phân vân, giống 犹豫. Hay gặp: 犹疑不决, do dự không quyết; 心生犹疑, trong lòng nảy sinh nghi ngại. Trong bài: 在反复、犹疑中, trong sự lặp đi lặp lại và chần chừ."),
    ("消磨", "xiāomó", "tiêu ma", "động từ", "làm hao mòn; giết (thời gian)", "他每天靠玩游戏消磨时间。", "Ngày nào anh ấy cũng chơi game để giết thời gian.",
     "Động từ, có hai nghĩa: làm hao mòn dần ý chí, sức lực, như 消磨热情, làm nguội nhiệt tình; và tiêu phí thời gian một cách nhàn rỗi, như 消磨时间. Trong bài: 消磨公众参与的热情, làm hao mòn nhiệt tình tham gia của công chúng."),
    ("红线", "hóngxiàn", "hồng tuyến", "danh từ", "lằn ranh đỏ, giới hạn không được vượt", "安全是一条不能跨越的红线。", "An toàn là lằn ranh đỏ không được vượt qua.",
     "Danh từ, nghĩa bóng là giới hạn tuyệt đối không được vượt qua, giống tiếng Việt lằn ranh đỏ. Trong bài: 立法首先划出一道红线, lập pháp trước hết vạch ra một lằn ranh đỏ."),
    ("酝酿", "yùnniàng", "uấn nhưỡng", "động từ", "ấp ủ, chuẩn bị, thai nghén", "他们为了这件事酝酿了两年。", "Họ đã ấp ủ chuẩn bị cho việc này suốt hai năm.",
     "Động từ, nghĩa gốc là quá trình lên men để ủ rượu; nghĩa bóng là chuẩn bị, bàn bạc, thai nghén một kế hoạch. Trong bài: 立法的过程本身就是酝酿探讨、形成共识的过程, quá trình lập pháp chính là quá trình thai nghén, thảo luận, hình thành đồng thuận."),
    ("持久战", "chíjiǔzhàn", "trì cửu chiến", "danh từ", "cuộc chiến trường kỳ, lâu dài", "减肥是一场持久战。", "Giảm cân là một cuộc chiến trường kỳ.",
     "Danh từ, nghĩa là trận chiến kéo dài, đối lập với 速决战, đánh nhanh thắng nhanh. Hay gặp: 打持久战. Trong bài: 垃圾分类的持久战, cuộc chiến trường kỳ về phân loại rác. Tên bài sau, 塑战能否速决, đối lại rất thú vị với từ này."),
    ("磨合", "móhé", "ma hợp", "động từ", "mài giũa cho ăn khớp, thích nghi lẫn nhau", "新同事之间需要一段时间的磨合。", "Đồng nghiệp mới cần một thời gian để thích nghi với nhau.",
     "Động từ, nghĩa gốc là cho máy móc mới chạy rà để các bộ phận ăn khớp; nghĩa bóng là dần dần thích nghi, phối hợp với nhau trong quá trình hợp tác. Hay gặp: 相互磨合, 磨合期. Trong bài: 经过长达半个世纪的磨合, trải qua nửa thế kỷ mài giũa."),
    ("纵观", "zòngguān", "tung quan", "động từ", "nhìn bao quát, xem xét toàn diện", "纵观历史，没有一个国家能靠封闭发展起来。", "Nhìn lại lịch sử, không nước nào phát triển được nhờ đóng cửa.",
     "Động từ, nghĩa là nhìn bao quát toàn bộ, thường đứng đầu câu: 纵观历史, 纵观世界, 纵观全局. Chữ 纵 là chiều dọc, theo chiều dài thời gian."),
    ("到位", "dàowèi", "đáo vị", "tính từ", "đến nơi đến chốn, đạt yêu cầu", "他的工作总是做得很到位。", "Công việc của anh ấy lúc nào cũng làm rất chu đáo.",
     "Tính từ, nghĩa bóng là đạt yêu cầu, làm trọn vẹn: 工作到位, 措施到位. Trong bài: 奖惩措施没有落实到位, các biện pháp thưởng phạt chưa được thực hiện đến nơi đến chốn."),
    ("填补", "tiánbǔ", "điền bổ", "động từ", "lấp đầy, bù vào chỗ trống", "这项研究填补了国内的空白。", "Công trình nghiên cứu này đã lấp đầy khoảng trống trong nước.",
     "Động từ, nghĩa là bổ sung vào chỗ trống, chỗ thiếu. Kết hợp quan trọng nhất là 填补空白, lấp khoảng trống. Trong bài: 上海在立法方面走在了前边，填补了空白, Thượng Hải đi đầu về lập pháp, lấp đầy khoảng trống."),
    ("借鉴", "jièjiàn", "tá giám", "động từ", "tham khảo, học hỏi kinh nghiệm", "我们可以借鉴别国的成功经验。", "Chúng ta có thể học hỏi kinh nghiệm thành công của nước khác.",
     "Động từ, nghĩa là nghiên cứu cái của người khác hay của quá khứ để rút ra kinh nghiệm, bài học. Chữ 鉴 là cái gương: lấy người khác làm gương soi. Trong bài: 可以借鉴的宝贵经验, kinh nghiệm quý báu có thể học hỏi."),
    ("一刀切", "yīdāoqiē", "nhất đao thiết", "động từ", "cào bằng, áp một khuôn cho mọi trường hợp", "选拔人才的方式和标准不能一刀切。", "Cách thức và tiêu chuẩn tuyển chọn nhân tài không thể cào bằng.",
     "Động từ, nghĩa đen là một nhát dao cắt thẳng; nghĩa bóng là không xét tình hình thực tế, xử lý mọi việc theo cùng một cách, gần với cào bằng trong tiếng Việt. Trong bài: 不能一刀切, không được cào bằng."),
    ("硬性", "yìngxìng", "ngạnh tính", "tính từ", "cứng, bắt buộc, không thể châm chước", "这是公司的硬性规定。", "Đây là quy định bắt buộc của công ty.",
     "Tính từ, nghĩa là không thể thay đổi, không thể châm chước. Hay gặp: 硬性规定, 硬性要求, 硬性约束. Từ gần nghĩa trong bài là 刚性, từ số bốn mươi hai."),
    ("思路", "sīlù", "tư lộ", "danh từ", "mạch suy nghĩ, hướng tiếp cận", "你的电话打断了我的思路。", "Cuộc gọi của bạn làm đứt mạch suy nghĩ của tôi.",
     "Danh từ, nghĩa là dòng, mạch suy nghĩ; cách tiếp cận vấn đề. Hay gặp: 打断思路, 转换思路, 理清思路. Trong bài: 在执行中转换思路, thay đổi cách tiếp cận trong quá trình thực hiện."),
    ("氛围", "fēnwéi", "phân vi", "danh từ", "bầu không khí", "人们在欢乐的氛围中迎来了新的一年。", "Mọi người đón năm mới trong bầu không khí vui tươi.",
     "Danh từ, nghĩa là bầu không khí, không khí tinh thần xung quanh, gần nghĩa với 气氛. Trong bài: 在家庭内部形成孩子监督家长的良好氛围, tạo trong gia đình một bầu không khí tốt, nơi con cái giám sát cha mẹ."),
    ("扎根", "zhāgēn", "trát căn", "động từ", "bén rễ, cắm rễ", "他毕业后一直扎根基层。", "Sau khi tốt nghiệp, anh ấy luôn gắn bó với cơ sở.",
     "Động từ ly hợp, nghĩa đen là rễ cây bám vào đất; nghĩa bóng là đi sâu, gắn bó lâu dài, đặt nền móng. Trong bài tách ra thành 扎下根来: 让一项政策真正扎下根来, làm cho một chính sách thật sự bén rễ. Chữ 扎 ở đây đọc zhā."),
    ("前端", "qiánduān", "tiền đoan", "danh từ", "khâu đầu (của một quá trình); ≠ 后端", "垃圾分类的前端是居民投放。", "Khâu đầu của phân loại rác là việc người dân bỏ rác.",
     "Danh từ, nghĩa là giai đoạn phía trước của một quá trình; ngược lại là 后端, khâu sau. Trong bài: 前端分类, phân loại ở khâu đầu, tức người dân tự phân loại; 后端处理, xử lý ở khâu sau, tức thu gom, vận chuyển, xử lý. Trong tin học, hai từ này là front-end và back-end."),
    ("士气", "shìqì", "sĩ khí", "danh từ", "tinh thần, khí thế (của tập thể)", "这场胜利大大鼓舞了球队的士气。", "Chiến thắng này cổ vũ rất lớn tinh thần của đội bóng.",
     "Danh từ, nghĩa là ý chí chiến đấu, tinh thần của một tập thể. Hay gặp: 鼓足士气, 振奋士气. Trong bài: 前端分类的士气已鼓足了, khí thế phân loại ở khâu đầu đã dâng cao."),
    ("鼓足", "gǔzú", "cổ túc", "động từ", "dồn hết, lấy hết (dũng khí, sức lực)", "他鼓足勇气向她表白了。", "Anh ấy lấy hết can đảm tỏ tình với cô ấy.",
     "Động từ, nghĩa là khơi dậy đến mức đầy đủ, dồn hết sức. Hay gặp: 鼓足勇气, lấy hết can đảm; 鼓足干劲, dồn hết nhiệt huyết; 鼓足士气."),
    ("新奇", "xīnqí", "tân kỳ", "tính từ", "mới lạ, mới mẻ", "孩子对什么都感到新奇。", "Trẻ con thấy cái gì cũng mới lạ.",
     "Tính từ, nghĩa là mới mẻ, lạ lùng, ít gặp. Hay gặp: 感到新奇, 设计新奇. Trong bài: 前期新奇引发的热议, những bàn tán sôi nổi do sự mới lạ ban đầu gây ra; 热议 là bàn tán sôi nổi."),
    ("终究", "zhōngjiū", "chung cứu", "phó từ", "rốt cuộc, suy cho cùng", "一个人的力量终究有限。", "Sức lực của một người suy cho cùng cũng có hạn.",
     "Phó từ, nghĩa là rốt cuộc, sau cùng vẫn, giống 毕竟 và 终归; nhấn mạnh kết quả tất yếu. Đây là mẫu câu thứ tám của bài."),
    ("刚性", "gāngxìng", "cương tính", "tính từ", "cứng rắn, không thể thay đổi; ≠ 柔性", "环保要求是刚性的，不能讨价还价。", "Yêu cầu về môi trường là cứng, không thể mặc cả.",
     "Tính từ, nghĩa là không cho phép thay đổi, đối lập với 柔性, mềm dẻo. Trong bài: 法律刚性执行, thực thi pháp luật một cách cứng rắn. Chữ 刚 cũng là chữ đầu của thành ngữ 刚柔并济 mà ta sẽ học."),
    ("规矩", "guīju", "quy củ", "danh từ", "phép tắc, quy củ, nề nếp", "新来的员工要守规矩。", "Nhân viên mới phải giữ quy củ.",
     "Danh từ, nghĩa là tiêu chuẩn, phép tắc hay thói quen nhất định; âm tiết sau đọc nhẹ. Hay gặp: 老规矩, lệ cũ; 立规矩, đặt ra phép tắc; 守规矩, giữ phép tắc. Trong bài: 立好规矩, đặt ra quy củ cho tốt."),
    ("树立", "shùlì", "thụ lập", "động từ", "xây dựng, tạo dựng (điều tốt đẹp, trừu tượng)", "父母要给孩子树立好榜样。", "Cha mẹ phải làm gương tốt cho con cái.",
     "Động từ, nghĩa là xây dựng, dựng lên, thường dùng cho những điều trừu tượng và tốt đẹp: 树立榜样, 树立风气, 树立目标, 树立信心. Trong bài: 树立风气, tạo dựng nếp sống."),
    ("投放", "tóufàng", "đầu phóng", "động từ", "bỏ vào; đưa vào (thị trường)", "请把垃圾投放到指定地点。", "Xin bỏ rác vào đúng nơi quy định.",
     "Động từ, nghĩa là thả vào, bỏ vào, đưa vào. Trong đề tài rác thải, 投放 là bỏ rác: 垃圾分类投放, bỏ rác theo phân loại. Ngoài ra còn nghĩa là đưa hàng hóa, vốn ra thị trường: 投放市场."),
    ("协力", "xiélì", "hiệp lực", "động từ", "hợp sức, chung sức", "大家齐心协力，终于完成了任务。", "Mọi người đồng lòng hợp sức, cuối cùng đã hoàn thành nhiệm vụ.",
     "Động từ, nghĩa là cùng nhau nỗ lực, giống tiếng Việt hiệp lực. Hay gặp: 同心协力, 齐心协力. Trong bài: 需要协力推进, cần chung sức thúc đẩy."),
    ("公信力", "gōngxìnlì", "công tín lực", "danh từ", "uy tín, sự tín nhiệm của công chúng", "政府部门要不断提升自己的公信力。", "Cơ quan chính phủ phải không ngừng nâng cao uy tín của mình.",
     "Danh từ, nghĩa là sức mạnh khiến công chúng tin tưởng. Hay gặp: 政府公信力, 媒体公信力. Trong bài: 确保公共治理的公信力, bảo đảm uy tín của công tác quản lý công."),
    ("长效", "chángxiào", "trường hiệu", "tính từ", "hiệu quả lâu dài", "我们要建立长效机制。", "Chúng ta phải xây dựng cơ chế lâu dài.",
     "Tính từ, nghĩa là có hiệu quả lâu dài. Hay gặp: 长效机制, cơ chế hiệu quả lâu dài; 长效措施. Chữ 长 đọc cháng. Trong bài: 短期行动容易，长效推进不易, hành động ngắn hạn thì dễ, thúc đẩy lâu dài mới khó."),
    ("内化", "nèihuà", "nội hóa", "động từ", "thấm vào trong, biến thành cái của mình", "我们要将理论知识内化为行动实践。", "Chúng ta phải biến kiến thức lý thuyết thành hành động thực tiễn.",
     "Động từ, nghĩa là tiếp thu quan điểm của người khác, biến thành cái của chính mình. Mẫu hay gặp: A内化为B. Trong bài: 一时兴起的兴奋劲才会内化为持久的习惯, sự hào hứng nhất thời mới biến thành thói quen bền vững."),
    ("草根", "cǎogēn", "thảo căn", "danh từ", "người bình dân, giới bình dân", "他是一位草根英雄。", "Anh ấy là một người hùng bình dân.",
     "Danh từ, nghĩa đen là rễ cỏ; nghĩa bóng là người dân thường, quần chúng bình dân, đối lập với giới tinh hoa. Hay gặp: 草根英雄, 草根文化. Trong bài: 发挥草根智慧, phát huy trí tuệ của người dân bình thường."),
    ("生态", "shēngtài", "sinh thái", "danh từ", "sinh thái", "我们要保护生态环境。", "Chúng ta phải bảo vệ môi trường sinh thái.",
     "Danh từ, chỉ trạng thái sinh tồn và phát triển của sinh vật trong môi trường tự nhiên. Âm Hán Việt và nghĩa giống tiếng Việt. Câu kết của bài: 才有生态文明的可持续进步, mới có sự tiến bộ bền vững của văn minh sinh thái."),
]

add("bullets", chapter="Từ mới (51 từ)", section="Từ mới 生词", title="Phần 1: Từ mới", size=40,
    items=["Bảng từ có 54 từ; 3 từ ghép vào phần giảng: 事理 (→ 分寸) · 热议 (→ 热词, 新奇) · 后端 (→ 前端)",
           "Còn 51 từ, chia 17 nhóm; mỗi từ: nghe đọc mẫu 2 lần → Hán Việt → nghĩa → ví dụ",
           "Nhiều từ mạng, từ thời sự: 热词 · 吐槽 · 试水 · 试错 · 一刀切 · 草根",
           "Chú ý âm đọc: 铺垫 (pū) · 扎根 (zhā) · 长效 (cháng) · 分寸 / 规矩 (thanh nhẹ)",
           "Từ dễ nhầm: 区区 · 切身 · 借鉴"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bảng từ của sách có năm mươi tư từ. Thầy ghép ba từ vào phần giảng của từ gần nghĩa: 事理 giảng cùng 分寸, 热议 giảng cùng 热词 và 新奇, 后端 giảng cùng 前端.",
         F(1, "Như vậy còn năm mươi mốt từ, chia thành mười bảy nhóm. Với mỗi từ, các bạn nghe đọc mẫu hai lần, rồi đến âm Hán Việt, nghĩa và ví dụ."),
         F(2, "Bài này có nhiều từ mạng và từ thời sự rất sống động, như 热词，吐槽，试水，试错，一刀切，草根. Học xong, các bạn có thể đọc báo, lướt mạng Trung Quốc dễ dàng hơn nhiều."),
         F(3, "Chú ý cách đọc: 铺垫 đọc pū; 扎根 đọc zhā; 长效 đọc cháng; còn âm tiết sau của 分寸 và 规矩 đọc nhẹ."),
         F(4, "Ngoài ra có mấy từ Hán Việt dễ hiểu nhầm, như 区区，切身，借鉴. Các bạn nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

sizes = [3] * 17
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
    ("何鼎鼎：2019年7月1日，《上海市生活垃圾管理条例》（以下简称《条例》）正式实施，对垃圾分类提出明确要求，“垃圾分类”一时间成了热词和技术活。将废弃物胡乱丢进垃圾桶，一扔了之的生活情景成了历史。",
     "Hà Đỉnh Đỉnh: Ngày 1 tháng 7 năm 2019, Điều lệ quản lý rác thải sinh hoạt thành phố Thượng Hải (dưới đây gọi tắt là Điều lệ) chính thức có hiệu lực, đặt ra yêu cầu rõ ràng về phân loại rác. “Phân loại rác” bỗng chốc trở thành từ khóa hot và một việc cần có kỹ thuật. Cảnh vứt bừa đồ bỏ đi vào thùng rác, vứt xong là xong chuyện, đã trở thành lịch sử.",
     ["何鼎鼎 là bình luận viên của Nhân dân Nhật báo, 本报评论员; người đối thoại là 朱珉迕, bình luận viên của Giải phóng Nhật báo, tờ báo lớn của Thượng Hải. 以下简称 là dưới đây gọi tắt là. 正式实施 là chính thức có hiệu lực.",
      "一时间 là bỗng chốc, trong một thời gian ngắn. 技术活 là việc đòi hỏi kỹ thuật, ý đùa rằng phân loại rác khó như một nghề. 一扔了之 là vứt đi là xong chuyện: mẫu 一 cộng động từ cộng 了之, mẫu câu thứ nhất. Chữ 了 ở đây đọc liǎo."],
     "何鼎鼎：二零一九年七月一日，《上海市生活垃圾管理条例》（以下简称《条例》）正式实施，对垃圾分类提出明确要求，垃圾分类一时间成了热词和技术活。将废弃物胡乱丢进垃圾桶，一扔了之的生活情景成了历史。"),
    ("“湿纸巾再湿也是干垃圾，干香菇再干也是湿垃圾”，“猪吃了会死的是有害垃圾，可以卖钱买猪的是可回收垃圾”，上海人用吐槽的方式学习和传播着分类知识，认真的样子让全国人民不得不点赞。",
     "“Khăn giấy ướt có ướt đến mấy cũng là rác khô, nấm hương khô có khô đến mấy cũng là rác ướt”, “thứ lợn ăn vào mà chết là rác độc hại, thứ bán lấy tiền mua được lợn là rác tái chế”: người Thượng Hải học và truyền bá kiến thức phân loại bằng những câu đùa tự trào, dáng vẻ nghiêm túc ấy khiến cả nước không thể không bấm like.",
     ["Mẫu 再……也…… nghĩa là dù… đến mấy cũng…: 湿纸巾再湿也是干垃圾, khăn giấy ướt có ướt mấy cũng là rác khô, vì nó không phân hủy như rác nhà bếp. Ngược lại, nấm hương khô vẫn là thực phẩm, nên là rác ướt.",
      "Câu về con lợn chính là mẹo nhớ mà thầy giới thiệu ở phần khởi động. 传播着 là đang lan truyền. 点赞 là bấm like, khen ngợi; 不得不点赞 là không thể không khen."]),
    ("曾经“拎得清”是上海话里对“明事理、知分寸”的褒奖，现在也成了上海人出门倒垃圾前的自我拷问。可玩笑归玩笑，垃圾分类对垃圾减量与绿色发展不是小事儿，但对大多数中国人而言是新鲜事儿，也是“麻烦事儿”，",
     "Trước đây, “拎得清” là lời khen trong tiếng Thượng Hải dành cho người “hiểu lẽ phải, biết chừng mực”, giờ đây nó cũng trở thành câu tự vấn của người Thượng Hải trước khi ra khỏi nhà đổ rác. Nhưng đùa thì đùa, phân loại rác không phải chuyện nhỏ đối với việc giảm lượng rác và phát triển xanh, còn với phần lớn người Trung Quốc thì đó là chuyện mới mẻ, và cũng là “chuyện phiền phức”,",
     ["拎得清 là từ thường dùng trong tiếng Ngô, phương ngữ của vùng Thượng Hải, nghĩa gốc là hiểu chuyện, biết việc gì nên làm, việc gì không. Chữ 拎 là xách: từ khi phân loại rác bắt buộc, cư dân mạng đùa rằng người Thượng Hải xách túi rác trong tay thì phải phân cho rõ.",
      "玩笑归玩笑 là đùa thì đùa, nhưng…: mẫu A归A, mẫu câu thứ hai. 对……而言 là đối với. Các chữ 事儿 có âm cuốn lưỡi, mang giọng khẩu ngữ thân mật."]),
    ("“不就是扔个垃圾嘛，区区小事何必那么较真？”如何让普通百姓接受并践行这一全新的环保方式呢？很多城市想到上海，这样一项公共政策他们是如何实现平稳开局的？",
     "“Chẳng qua chỉ là vứt rác thôi mà, chuyện cỏn con cần gì phải nghiêm trọng như thế?” Làm thế nào để người dân bình thường chấp nhận và thực hành phương thức bảo vệ môi trường hoàn toàn mới này? Nhiều thành phố nghĩ đến Thượng Hải: một chính sách công như vậy, họ đã khởi đầu suôn sẻ bằng cách nào?",
     ["不就是……嘛 là chẳng qua chỉ là… thôi mà, câu phản vấn coi nhẹ sự việc. 区区小事 là chuyện cỏn con; 何必那么较真 là cần gì phải nghiêm trọng hóa như thế: 区区 và 何必 đều là mẫu câu của bài.",
      "接受并践行 là chấp nhận và thực hành. 平稳开局 là khởi đầu suôn sẻ, ổn định. Câu hỏi này là chủ đề của cả cuộc đối thoại: kinh nghiệm của Thượng Hải là gì?"]),
    ("朱珉迕：从十九年前率先试水，到如今立法强制执行，上海的垃圾分类并非一蹴而就，而是不断试错和创新的过程。",
     "Chu Mân Ngỗ: Từ mười chín năm trước đi đầu thử nghiệm, đến nay lập pháp để bắt buộc thực hiện, việc phân loại rác của Thượng Hải không phải một bước là xong, mà là một quá trình không ngừng thử sai và đổi mới.",
     ["从……到…… là từ… đến…. 率先 là đi đầu. 十九年前 tức là khoảng năm 2000, khi Thượng Hải là một trong những thành phố đầu tiên của Trung Quốc thí điểm phân loại rác.",
      "并非……而是…… là không phải… mà là…, mẫu câu thứ năm; 并非 là cách nói văn viết của 并不是. 一蹴而就 là một bước là thành công, thành ngữ ta sẽ học."]),
    ("《条例》正式推行是在今年，但上海人垃圾分类理念的输入已开展多年，基层的大量试点、广泛的社会动员为最终的政策推行做好了铺垫。同时，更多人切身感受到“垃圾围城”的风险，这加速了垃圾分类理念的被认同。",
     "Điều lệ được chính thức triển khai vào năm nay, nhưng việc truyền bá ý thức phân loại rác cho người dân Thượng Hải đã diễn ra nhiều năm; rất nhiều điểm thí điểm ở cơ sở và sự vận động xã hội rộng rãi đã làm nền cho việc thực thi chính sách sau cùng. Đồng thời, ngày càng nhiều người tự mình cảm nhận được nguy cơ “rác bao vây thành phố”, điều này đã đẩy nhanh việc ý thức phân loại rác được mọi người đồng tình.",
     ["推行 là triển khai thực hiện. 理念的输入 là việc truyền bá, đưa ý thức vào đầu người dân. 为……做好了铺垫 là đã làm nền, chuẩn bị sẵn cho…, mẫu câu thứ sáu.",
      "垃圾围城 là rác bao vây thành phố: theo chú thích của sách, rác đô thị thường được chôn lấp hay chất đống ở ngoại ô, lâu ngày thành phố bị rác bao quanh. 理念的被认同 là cách nói hơi lạ, nghĩa là việc ý thức ấy được mọi người đồng tình."]),
    ("何鼎鼎：有人说，政策制定与推行需要刚柔并济。柔呢，就是政策形成过程要有吸收接纳，也要循序渐进，给公众留出适应时间；刚呢，就是推进过程中要一鼓作气、果断坚决，不能在反复、犹疑中消磨公众参与的热情。上海的垃圾分类政策是如何平衡两者的？",
     "Hà Đỉnh Đỉnh: Có người nói, xây dựng và thực thi chính sách cần cương nhu kết hợp. Nhu, tức là quá trình hình thành chính sách phải biết lắng nghe, tiếp thu, cũng phải tiến hành từng bước, chừa thời gian cho công chúng thích nghi; cương, tức là khi triển khai phải làm một mạch, quả quyết, kiên quyết, không thể để nhiệt tình tham gia của công chúng bị bào mòn trong sự lặp đi lặp lại, do dự. Chính sách phân loại rác của Thượng Hải đã cân bằng hai mặt này như thế nào?",
     ["刚柔并济 là cương nhu kết hợp; sau đó người nói giải thích từng chữ theo lối 柔呢，就是……；刚呢，就是……; chữ 呢 ở đây dùng để nêu chủ đề, tạo chỗ ngắt. 吸收接纳 là tiếp thu, đón nhận ý kiến. 循序渐进 là tuần tự tiến dần.",
      "一鼓作气 là thừa lúc khí thế đang lên mà làm một mạch. 果断坚决 là quả quyết, kiên quyết. 消磨公众参与的热情 là làm hao mòn nhiệt tình tham gia của công chúng. 平衡两者 là cân bằng cả hai."]),
    ("朱珉迕：对，立法首先划出一道红线，立法的过程本身就是酝酿探讨、形成共识的过程。早在几十年前，德国、日本、英国、澳大利亚等国家就开始了垃圾分类的持久战。经过长达半个世纪的磨合，目前有些做法已经比较成熟并取得了良好效果。",
     "Chu Mân Ngỗ: Đúng vậy, lập pháp trước hết vạch ra một lằn ranh đỏ, và bản thân quá trình lập pháp chính là quá trình thai nghén, thảo luận, hình thành đồng thuận. Từ mấy chục năm trước, các nước như Đức, Nhật Bản, Anh, Úc đã bắt đầu cuộc chiến trường kỳ về phân loại rác. Trải qua nửa thế kỷ mài giũa, hiện nay một số cách làm đã khá hoàn thiện và đạt hiệu quả tốt.",
     ["划出一道红线 là vạch ra một lằn ranh đỏ: luật đặt ra giới hạn ai cũng phải tuân thủ, đây là chữ cương. Còn 酝酿探讨、形成共识 là thai nghén, thảo luận, hình thành đồng thuận, đây là chữ nhu.",
      "早在……就…… là từ tận… đã…, nhấn mạnh việc xảy ra rất sớm. 持久战 là cuộc chiến trường kỳ. 经过长达半个世纪的磨合 là trải qua nửa thế kỷ mài giũa; 长达 là kéo dài tới; mẫu 经过……的磨合 là mẫu câu thứ bảy."]),
    ("纵观历史，我国也曾多次制定垃圾分类的相关规定，可对垃圾分类的标准和具体做法、相应的奖惩措施没有落实到位，以致工作推进十分缓慢，其关键在于法律体系不健全，而上海在立法方面走在了前边，填补了空白，为其他城市提供了可以借鉴的宝贵经验。",
     "Nhìn lại lịch sử, nước ta cũng từng nhiều lần ban hành các quy định liên quan đến phân loại rác, nhưng tiêu chuẩn và cách làm cụ thể, cùng các biện pháp thưởng phạt tương ứng, đều chưa được thực hiện đến nơi đến chốn, khiến công việc tiến triển rất chậm; mấu chốt là hệ thống pháp luật chưa hoàn thiện. Còn Thượng Hải đã đi trước về mặt lập pháp, lấp đầy khoảng trống, cung cấp cho các thành phố khác những kinh nghiệm quý báu có thể học hỏi.",
     ["纵观历史 là nhìn lại toàn bộ lịch sử. 曾 là đã từng. 相应的奖惩措施 là biện pháp thưởng phạt tương ứng; 奖惩 là thưởng và phạt. 没有落实到位 là chưa thực hiện đến nơi đến chốn.",
      "以致 là đến nỗi, dẫn đến kết quả không mong muốn. 其关键在于 là mấu chốt của nó nằm ở chỗ. 走在了前边 là đi trước, đi đầu. 填补了空白 là lấp khoảng trống, rồi 为其他城市提供了可以借鉴的宝贵经验."]),
    ("与此同时，上海相关部门的管理者也提出不能“一刀切”，既要严格执行硬性约束，也要充分考虑居民需求，政府和相关部门还是要保持足够的耐心，要包容百姓的难处，要坚持不懈地引导。",
     "Đồng thời, những người quản lý ở các cơ quan liên quan của Thượng Hải cũng cho rằng không được “cào bằng”: vừa phải nghiêm túc thực thi các ràng buộc bắt buộc, vừa phải xem xét đầy đủ nhu cầu của cư dân; chính quyền và các cơ quan liên quan vẫn phải giữ đủ kiên nhẫn, phải thông cảm với cái khó của người dân, phải kiên trì không ngừng hướng dẫn.",
     ["与此同时 là cùng lúc đó, đồng thời. 一刀切 là cào bằng. 既要……也要…… là vừa phải… vừa phải…. 硬性约束 là ràng buộc cứng, bắt buộc.",
      "包容百姓的难处 là thông cảm, bao dung với cái khó của dân; 难处 là chỗ khó khăn. 坚持不懈地引导 là kiên trì không ngừng hướng dẫn. Ba chữ 要 lặp lại tạo nhịp điệu, nhấn mạnh mặt nhu của chính sách."]),
    ("在执行中转换思路，比如中小学将垃圾分类作为“开学第一课”，在家庭内部形成孩子监督家长的良好氛围，就能让一项政策真正扎下根来。",
     "Thay đổi cách tiếp cận trong khi thực hiện, chẳng hạn các trường tiểu học và trung học lấy phân loại rác làm “bài học đầu tiên của năm học”, tạo ra trong gia đình một bầu không khí tốt, nơi con cái giám sát cha mẹ, như vậy sẽ khiến một chính sách thật sự bén rễ.",
     ["转换思路 là thay đổi cách tiếp cận. 将……作为…… là lấy… làm…, cách nói văn viết của 把……当作……. 开学第一课 vốn là tên một chương trình truyền hình giáo dục nổi tiếng ở Trung Quốc, phát vào ngày khai giảng.",
      "孩子监督家长 là con cái giám sát cha mẹ: trẻ học ở trường rồi về nhà nhắc bố mẹ phân loại rác. 扎下根来 là bén rễ: tách từ 扎根 ra, thêm bổ ngữ xu hướng 下来."]),
    ("何鼎鼎：那现在人们还有两个集中关心的问题。第一个，前端分类的士气已鼓足了，后端处理的工作能否及时跟上？第二个，前期新奇引发的热议终究会过去，垃圾分类如何从时尚走向日常？",
     "Hà Đỉnh Đỉnh: Vậy hiện nay mọi người còn tập trung quan tâm đến hai vấn đề. Thứ nhất, khí thế phân loại ở khâu đầu đã dâng cao, liệu công việc xử lý ở khâu sau có theo kịp không? Thứ hai, những bàn tán sôi nổi do sự mới lạ ban đầu rốt cuộc sẽ qua đi, làm sao để phân loại rác từ một trào lưu trở thành chuyện thường ngày?",
     ["集中关心的问题 là những vấn đề được quan tâm tập trung. 前端 và 后端 là khâu đầu và khâu sau. 士气已鼓足 là khí thế đã dâng cao. 能否及时跟上 là có theo kịp không.",
      "前期 là giai đoạn đầu. 热议终究会过去 là những bàn tán sôi nổi rốt cuộc sẽ qua đi; 终究 là mẫu câu thứ tám. 从时尚走向日常 là từ trào lưu trở thành thường ngày; đây cũng là tiêu đề gốc của bài báo trên Nhân dân Nhật báo."]),
    ("朱珉迕：前端最重要的是法律刚性执行，立好规矩、养成习惯、树立风气；后端处理最重要的是避免“前端分类后端混运”现象的发生，投放、收集、运输、处理等一环扣一环，需要协力推进，确保公共治理的公信力。",
     "Chu Mân Ngỗ: Ở khâu đầu, quan trọng nhất là thực thi pháp luật một cách cứng rắn, đặt ra quy củ, hình thành thói quen, tạo dựng nếp sống; ở khâu xử lý phía sau, quan trọng nhất là tránh hiện tượng “khâu đầu phân loại, khâu sau chở lẫn”. Các khâu bỏ rác, thu gom, vận chuyển, xử lý móc nối với nhau như mắt xích, cần chung sức thúc đẩy, bảo đảm uy tín của công tác quản lý công.",
     ["法律刚性执行 là thực thi pháp luật cứng rắn. Ba cụm động tân: 立好规矩，养成习惯，树立风气. 前端分类后端混运 là người dân phân loại cẩn thận, nhưng xe rác lại chở lẫn tất cả; điều này làm người dân mất lòng tin.",
      "一环扣一环 là vòng này móc vòng kia, các khâu liên quan chặt chẽ. 协力推进 là chung sức thúc đẩy. 确保公共治理的公信力 là bảo đảm uy tín của quản lý công: nếu khâu sau làm hỏng, công sức của khâu đầu sẽ đổ sông đổ biển."]),
    ("也要更开放包容地调动社会力量参与其中，许多公共事务都是如此，短期行动容易，长效推进不易。我们要形成真正的“长效机制”，也只有这样，一时兴起的“兴奋劲”才会内化为持久的习惯。",
     "Cũng cần huy động lực lượng xã hội tham gia một cách cởi mở, bao dung hơn. Rất nhiều việc công đều như vậy: hành động ngắn hạn thì dễ, thúc đẩy lâu dài mới khó. Chúng ta phải hình thành “cơ chế lâu dài” thật sự, cũng chỉ có như vậy, “cơn hào hứng” nhất thời mới chuyển hóa thành thói quen bền vững.",
     ["调动社会力量 là huy động lực lượng xã hội. 参与其中 là tham gia vào đó. 许多公共事务都是如此 là nhiều việc công đều như thế. 短期 và 长效 đối nhau: ngắn hạn và lâu dài.",
      "长效机制 là cơ chế hiệu quả lâu dài. 只有这样，……才…… là chỉ có như vậy mới…. 一时兴起的兴奋劲 là sự hào hứng nổi lên nhất thời; 劲 ở đây là cái hăng hái. 内化为持久的习惯 là biến thành thói quen lâu bền."]),
    ("垃圾分类是新问卷，也是新课题。好习惯的养成不可能毕其功于一役，生活垃圾分类要取得明显成效，需要几十年甚至几代人的坚持与努力。只有全民共同参与，发挥草根智慧，变“随手扔”为“随手分”，才有生态文明的可持续进步。",
     "Phân loại rác là một bài thi mới, cũng là một đề tài mới. Việc hình thành thói quen tốt không thể xong trong một trận; phân loại rác sinh hoạt muốn đạt hiệu quả rõ rệt cần sự kiên trì và nỗ lực của vài chục năm, thậm chí vài thế hệ. Chỉ khi toàn dân cùng tham gia, phát huy trí tuệ của người dân bình thường, biến “tiện tay vứt” thành “tiện tay phân loại”, thì mới có sự tiến bộ bền vững của văn minh sinh thái.",
     ["新问卷，新课题 là bài thi mới, đề tài mới: phân loại rác như một bài kiểm tra cho cả xã hội. 毕其功于一役 là mong làm xong mọi việc chỉ trong một trận, thành ngữ ta sẽ học. 取得明显成效 là đạt hiệu quả rõ rệt.",
      "只有……才…… là chỉ khi… mới…. 变A为B là biến A thành B: 变随手扔为随手分, biến tiện tay vứt thành tiện tay phân loại, khớp với tên bài. 可持续进步 là tiến bộ bền vững."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa “随手扔”还是“随手分”", size=40,
    items=["Đối thoại: 何鼎鼎 (Nhân dân Nhật báo) hỏi – 朱珉迕 (Giải phóng Nhật báo) đáp",
           "Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa. Bài được trích từ Nhân dân Nhật báo, số ra ngày tám tháng bảy năm 2019, trang năm, với tiêu đề: 垃圾分类，如何更好走向日常, phân loại rác, làm sao trở thành chuyện thường ngày tốt hơn.",
         F(0, "Bài có dạng đối thoại giữa hai bình luận viên: 何鼎鼎, Hà Đỉnh Đỉnh, của Nhân dân Nhật báo, người đặt câu hỏi; và 朱珉迕, Chu Mân Ngỗ, của Giải phóng Nhật báo ở Thượng Hải, người chia sẻ kinh nghiệm. Ngôn ngữ là văn bình luận báo chí, nhiều từ chính luận nhưng cũng có những câu đùa rất đời thường."),
         F(1, "Thầy chia bài thành mười lăm đoạn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(2, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(3, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    n = len(zh)
    zsize = 54 if n <= 100 else 50 if n <= 125 else 46
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Bố cục & hiểu bài", section="Bài khóa 课文", title="Bố cục bài khóa", size=34,
    items=["## Đặt vấn đề (đoạn 1–4): 《条例》 có hiệu lực → 吐槽, 拎得清 → làm sao để dân 接受并践行?",
           "## Kinh nghiệm Thượng Hải (đoạn 5–11)",
           "并非一蹴而就：19年试水、试点、社会动员 → 为政策推行做好铺垫",
           "刚柔并济：刚 = 立法划红线、严格执行 · 柔 = 不能一刀切、耐心引导、孩子监督家长",
           "## Hai câu hỏi mới (đoạn 12–14): 后端能否跟上？如何从时尚走向日常？ → 长效机制",
           "## Kết luận (đoạn 15): 不可能毕其功于一役 · 变“随手扔”为“随手分”"],
    say=["Trước khi sang phần ngữ pháp, chúng ta cùng nhìn lại bố cục của bài khóa.",
         F(0, "Phần một, đoạn một đến bốn, đặt vấn đề: Điều lệ có hiệu lực, người Thượng Hải học phân loại rác bằng những câu đùa, từ 拎得清 trở thành câu tự vấn. Câu hỏi đặt ra: làm sao để người dân chấp nhận và thực hành?"),
         F(1, "Phần hai, đoạn năm đến mười một, là kinh nghiệm của Thượng Hải."),
         F(2, "Thứ nhất, thành công không phải một bước là xong: mười chín năm thử nghiệm, thí điểm ở cơ sở, vận động xã hội, tất cả đã làm nền cho chính sách."),
         F(3, "Thứ hai, cương nhu kết hợp. Cương là lập pháp vạch lằn ranh đỏ, thực thi nghiêm túc. Nhu là không cào bằng, kiên nhẫn hướng dẫn, và để con cái giám sát cha mẹ."),
         F(4, "Phần ba, đoạn mười hai đến mười bốn: hai câu hỏi mới. Khâu xử lý phía sau có theo kịp không? Và làm sao để phân loại rác từ trào lưu trở thành thường ngày? Câu trả lời là phải có cơ chế lâu dài."),
         F(5, "Phần cuối, đoạn mười lăm, kết luận: thói quen tốt không thể hình thành trong một trận; phải biến tiện tay vứt thành tiện tay phân loại.")])

add("bullets", section="Bài khóa 课文", title="Kiểm tra hiểu bài", reveal=True, size=32,
    items=["(1) 《条例》是哪一天正式实施的？",
           "Đáp án: 2019年7月1日。",
           "(2) “拎得清”在上海话里原来是什么意思？现在又成了什么？",
           "Đáp án: 原来是对“明事理、知分寸”的褒奖，现在也成了上海人出门倒垃圾前的自我拷问。",
           "(3) 政策制定与推行中的“柔”和“刚”分别指什么？",
           "Đáp án: 柔：吸收接纳、循序渐进，给公众留出适应时间；刚：一鼓作气、果断坚决。",
           "(4) 人们集中关心的两个问题是什么？",
           "Đáp án: 后端处理的工作能否及时跟上；垃圾分类如何从时尚走向日常。"],
    say=["Bây giờ chúng ta kiểm tra xem mình đã hiểu bài chưa. Các bạn nghe câu hỏi, tạm dừng để trả lời, rồi nghe đáp án nhé.",
         F(0, "Câu một: 条例是哪一天正式实施的？ Điều lệ chính thức có hiệu lực vào ngày nào?"),
         F(1, "Đáp án: 二零一九年七月一日。 Ngày một tháng bảy năm 2019."),
         F(2, "Câu hai: 拎得清在上海话里原来是什么意思？现在又成了什么？ Trong tiếng Thượng Hải, 拎得清 vốn có nghĩa gì? Bây giờ nó lại trở thành gì?"),
         F(3, "Đáp án: 原来是对明事理、知分寸的褒奖，现在也成了上海人出门倒垃圾前的自我拷问。 Vốn là lời khen người hiểu lẽ phải, biết chừng mực; nay thành câu tự vấn trước khi đi đổ rác."),
         F(4, "Câu ba: 政策制定与推行中的柔和刚分别指什么？ Trong việc xây dựng và thực thi chính sách, nhu và cương lần lượt chỉ điều gì?"),
         F(5, "Đáp án: 柔是吸收接纳、循序渐进，给公众留出适应时间；刚是一鼓作气、果断坚决。 Nhu là lắng nghe tiếp thu, tiến từng bước, cho dân thời gian thích nghi; cương là làm một mạch, quả quyết, kiên quyết."),
         F(6, "Câu bốn: 人们集中关心的两个问题是什么？ Hai vấn đề mọi người tập trung quan tâm là gì?"),
         F(7, "Đáp án: 后端处理的工作能否及时跟上；垃圾分类如何从时尚走向日常。 Khâu xử lý phía sau có theo kịp không; và phân loại rác làm sao từ trào lưu trở thành thường ngày.")])

# ======================= MẪU CÂU =======================
add("bullets", chapter="Mẫu câu: 一V了之 · A归A · 区区 · 何必", section="Mẫu câu 重点句型", title="1. 一 + V. + 了之 – làm… là xong chuyện", size=35,
    items=["Chọn cách đơn giản, đỡ việc nhất để “giải quyết” vấn đề; thường mang sắc thái tiêu cực",
           "了 đọc liǎo (kết thúc): 一扔了之 · 一走了之 · 一笑了之 · 一推了之",
           "将废弃物胡乱丢进垃圾桶，一扔了之的生活情景成了历史。",
           "面对巨大的家庭经济压力，他选择了一走了之。",
           "虽然听到许多嘲讽，但他并不较真，只是一笑了之。"],
    say=["Bây giờ chúng ta sang phần mẫu câu trọng điểm. Bài này có tám mẫu. Mẫu thứ nhất: 一 cộng động từ cộng 了之.",
         F(0, "Mẫu này biểu thị chọn cách đơn giản, đỡ việc nhất để giải quyết vấn đề: làm một cái là xong chuyện, không quan tâm hậu quả. Thường mang sắc thái tiêu cực."),
         F(1, "Chú ý: chữ 了 ở đây đọc liǎo, nghĩa là kết thúc, xong; 之 là đại từ chỉ sự việc. Hay gặp: 一扔了之, vứt đi là xong; 一走了之, bỏ đi là xong; 一笑了之, cười trừ cho qua; 一推了之, đẩy đi là xong."),
         F(2, "Ví dụ một, từ bài khóa: 将废弃物胡乱丢进垃圾桶，一扔了之的生活情景成了历史。 Cảnh vứt bừa rác vào thùng, vứt xong là xong chuyện, đã thành lịch sử."),
         F(3, "Ví dụ hai: 面对巨大的家庭经济压力，他选择了一走了之。 Trước áp lực kinh tế gia đình quá lớn, anh ta chọn cách bỏ đi cho xong chuyện. Ở đây sắc thái tiêu cực rất rõ: trốn tránh trách nhiệm."),
         F(4, "Ví dụ ba: 虽然听到许多嘲讽，但他并不较真，只是一笑了之。 Tuy nghe nhiều lời chế giễu, nhưng anh ấy không chấp, chỉ cười cho qua. Ở câu này, 一笑了之 lại mang ý điềm tĩnh, độ lượng.")])

add("bullets", section="Mẫu câu 重点句型", title="2. A 归 A – A thì A (nhưng…)", size=35,
    items=["Đặt giữa hai từ giống nhau: tạm thừa nhận A, rồi chuyển ý; trọng tâm nằm ở vế sau (可 / 但是 / 然而 / 也)",
           "可玩笑归玩笑，垃圾分类对垃圾减量与绿色发展不是小事儿……",
           "……在大连、威海、青岛、厦门等地也能寻找到夏日消暑的好去处。然而，玩归玩，也要注意健康和安全。",
           "朋友归朋友，但是法律是一条红线，谁也不能逾越。"],
    say=["Mẫu thứ hai: A归A, giống tiếng Việt: đùa thì đùa, bạn thì bạn.",
         F(0, "Mẫu này đặt chữ 归 giữa hai từ giống nhau, biểu thị nhượng bộ rồi chuyển ý: tạm thừa nhận A, nhưng điều người nói muốn nhấn mạnh nằm ở vế sau, thường bắt đầu bằng 可，但是，然而, hoặc có chữ 也."),
         F(1, "Ví dụ một, từ bài khóa: 可玩笑归玩笑，垃圾分类对垃圾减量与绿色发展不是小事儿。 Nhưng đùa thì đùa, phân loại rác không phải chuyện nhỏ đối với việc giảm rác và phát triển xanh."),
         F(2, "Ví dụ hai: 在大连、威海、青岛、厦门等地也能寻找到夏日消暑的好去处。然而，玩归玩，也要注意健康和安全。 Ở Đại Liên, Uy Hải, Thanh Đảo, Hạ Môn cũng tìm được nơi tránh nóng mùa hè lý tưởng. Tuy nhiên, chơi thì chơi, cũng phải chú ý sức khỏe và an toàn."),
         F(3, "Ví dụ ba: 朋友归朋友，但是法律是一条红线，谁也不能逾越。 Bạn bè thì là bạn bè, nhưng pháp luật là lằn ranh đỏ, ai cũng không được vượt qua. 逾越 là vượt qua.")])

add("bullets", section="Mẫu câu 重点句型", title="3. 区区 + NP (cỏn con) · 4. 何必……？ (cần gì phải)", size=34,
    items=["区区 + danh từ: nhấn mạnh ít ỏi, không đáng kể; giọng coi thường",
           "区区“恶作剧”三个字已不足以形容这个“熊孩子”的恶劣行为。",
           "没想到区区一个小要求，你都不肯爽快答应。",
           "何必……？: câu phản vấn = 不必 (không cần phải)",
           "不就是扔个垃圾嘛，区区小事何必那么较真？",
           "前进中出现些失误是难免的，何必大惊小怪呢！ · 美景就在眼前，何必舍近求远。"],
    say=["Mẫu thứ ba và thứ tư cùng xuất hiện trong một câu của bài khóa: 不就是扔个垃圾嘛，区区小事何必那么较真？",
         F(0, "区区 cộng danh từ, nhấn mạnh số lượng ít ỏi hoặc sự việc không đáng kể, thường mang giọng coi nhẹ, thậm chí coi thường."),
         F(1, "Ví dụ: 区区恶作剧三个字已不足以形容这个熊孩子的恶劣行为。 Chỉ ba chữ trò đùa tai quái thôi thì không đủ để diễn tả hành vi tồi tệ của đứa trẻ hư này. 熊孩子 là từ mạng chỉ trẻ con nghịch ngợm, hư hỏng."),
         F(2, "Ví dụ: 没想到区区一个小要求，你都不肯爽快答应。 Không ngờ chỉ một yêu cầu cỏn con mà bạn cũng không chịu vui vẻ nhận lời."),
         F(3, "Mẫu thứ tư: 何必, dùng trong câu phản vấn, nghĩa là cần gì phải, tức là không cần, giống 不必. Cuối câu thường có 呢."),
         F(4, "Ví dụ từ bài khóa: 区区小事何必那么较真？ Chuyện cỏn con cần gì phải nghiêm trọng như thế?"),
         F(5, "Ví dụ khác: 前进中出现些失误是难免的，何必大惊小怪呢！ Trên đường tiến lên có chút sai sót là khó tránh, cần gì phải làm to chuyện! Và: 美景就在眼前，何必舍近求远。 Cảnh đẹp ngay trước mắt, cần gì phải bỏ gần tìm xa.")])

add("bullets", chapter="Mẫu câu: 并非 · 铺垫 · 磨合 · 终究", section="Mẫu câu 重点句型", title="5. 并非……，而是…… – không phải…, mà là…", size=35,
    items=["Phủ định vế trước, khẳng định vế sau; 并非 = 并不是 (văn viết, nhấn mạnh)",
           "上海的垃圾分类并非一蹴而就，而是不断试错和创新的过程。",
           "喝醉了就会想念你，其实并非有意记起你，而是心底里和脑海中从未忘记过你。",
           "能取得今天的成就，并非他仅有聪慧的头脑，而是他身怀教育救国的信念。"],
    say=["Mẫu thứ năm: 并非 vế trước, 而是 vế sau.",
         F(0, "Mẫu này phủ định vế trước và khẳng định vế sau, dùng để đính chính một cách hiểu sai. 并非 là cách nói văn viết của 并不是, chữ 并 nhấn mạnh sự phủ định."),
         F(1, "Ví dụ một, từ bài khóa: 上海的垃圾分类并非一蹴而就，而是不断试错和创新的过程。 Phân loại rác ở Thượng Hải không phải một bước là xong, mà là quá trình không ngừng thử sai và đổi mới."),
         F(2, "Ví dụ hai: 喝醉了就会想念你，其实并非有意记起你，而是心底里和脑海中从未忘记过你。 Say rồi là lại nhớ em; thật ra không phải cố ý nhớ đến em, mà là trong đáy lòng và trong tâm trí chưa bao giờ quên em."),
         F(3, "Ví dụ ba: 能取得今天的成就，并非他仅有聪慧的头脑，而是他身怀教育救国的信念。 Đạt được thành tựu hôm nay, không phải chỉ vì ông có bộ óc thông minh, mà vì ông mang trong mình niềm tin dùng giáo dục để cứu nước.")])

add("bullets", section="Mẫu câu 重点句型", title="6. 为……做（好）铺垫 – làm nền, chuẩn bị cho…", size=34,
    items=["Việc làm trước tạo điều kiện, tiền đề cho việc sau; 为 đọc wèi",
           "……基层的大量试点、广泛的社会动员为最终的政策推行做好了铺垫。",
           "作为一名实习生，他紧紧抓住向前辈们学习的机会，现在的努力都是在为之后的工作做好铺垫。",
           "借着年终的时机，总经理带着下属一起拜访合作伙伴和老客户，为明年新的销售模式的推出做好铺垫。"],
    say=["Mẫu thứ sáu: 为某事做铺垫, hoặc 为某事做好铺垫. Chữ 为 ở đây đọc wèi, nghĩa là cho, vì.",
         F(0, "Mẫu này biểu thị việc làm trước tạo điều kiện, tạo tiền đề cho việc sau. Tiếng Việt nói là làm nền cho, dọn đường cho, chuẩn bị cho."),
         F(1, "Ví dụ một, từ bài khóa: 基层的大量试点、广泛的社会动员为最终的政策推行做好了铺垫。 Rất nhiều điểm thí điểm ở cơ sở và sự vận động xã hội rộng rãi đã làm nền cho việc thực thi chính sách sau cùng."),
         F(2, "Ví dụ hai: 作为一名实习生，他紧紧抓住向前辈们学习的机会，现在的努力都是在为之后的工作做好铺垫。 Là một thực tập sinh, anh ấy nắm chặt cơ hội học hỏi các tiền bối; những cố gắng bây giờ đều là chuẩn bị cho công việc sau này."),
         F(3, "Ví dụ ba: 借着年终的时机，总经理带着下属一起拜访合作伙伴和老客户，为明年新的销售模式的推出做好铺垫。 Nhân dịp cuối năm, tổng giám đốc dẫn cấp dưới đi thăm các đối tác và khách hàng cũ, dọn đường cho việc ra mắt mô hình bán hàng mới vào năm sau.")])

add("bullets", section="Mẫu câu 重点句型", title="7. 经过……（的）磨合 – qua một thời gian mài giũa, thích nghi", size=34,
    items=["Sau một quá trình điều chỉnh, thích nghi lẫn nhau → kết quả tốt ở vế sau",
           "经过长达半个世纪的磨合，目前有些做法已经比较成熟并取得了良好效果。",
           "……当初性格差异很大的四个人，是如何经过一段艰难的磨合而成为朋友的。",
           "经过长期磨合，在政府与企业之间，正在逐步建立起一种新型的经济关系。"],
    say=["Mẫu thứ bảy: 经过什么的磨合.",
         F(0, "Mẫu này nói rằng sau một quá trình điều chỉnh, thích nghi lẫn nhau, thì đạt được một kết quả tốt; kết quả ấy nằm ở vế sau. Giữa 经过 và 磨合 thường là cụm chỉ thời gian hay tính chất: 长期，一段艰难的，长达半个世纪的."),
         F(1, "Ví dụ một, từ bài khóa: 经过长达半个世纪的磨合，目前有些做法已经比较成熟并取得了良好效果。 Trải qua nửa thế kỷ mài giũa, một số cách làm đã khá hoàn thiện và đạt hiệu quả tốt."),
         F(2, "Ví dụ hai: 现在看着她们亲密无间的样子，确实很难想象，当初性格差异很大的四个人，是如何经过一段艰难的磨合而成为朋友的。 Nhìn các cô ấy thân thiết như hình với bóng bây giờ, thật khó tưởng tượng bốn người tính cách khác nhau rất xa đã trải qua một giai đoạn thích nghi khó khăn thế nào để trở thành bạn."),
         F(3, "Ví dụ ba: 经过长期磨合，在政府与企业之间，正在逐步建立起一种新型的经济关系。 Trải qua thời gian dài mài giũa, giữa chính phủ và doanh nghiệp đang dần hình thành một kiểu quan hệ kinh tế mới.")])

add("bullets", section="Mẫu câu 重点句型", title="8. 终究…… – rốt cuộc, suy cho cùng (kết quả tất yếu)", size=35,
    items=["Phó từ, nhấn mạnh kết quả cuối cùng tất yếu sẽ như vậy, dù quá trình thế nào; ≈ 毕竟 / 终归",
           "前期新奇引发的热议终究会过去，垃圾分类如何从时尚走向日常？",
           "……想不到事与愿违，到头来终究是竹篮打水一场空。",
           "你何必要患得患失呢，是你的终究会是你的，别人抢不走的。"],
    say=["Mẫu thứ tám: phó từ 终究.",
         F(0, "终究 nhấn mạnh rằng dù quá trình ra sao, kết quả cuối cùng tất yếu vẫn là như vậy. Nghĩa gần với 毕竟 và 终归; tiếng Việt dịch là rốt cuộc, suy cho cùng, sớm muộn gì cũng."),
         F(1, "Ví dụ một, từ bài khóa: 前期新奇引发的热议终究会过去，垃圾分类如何从时尚走向日常？ Những bàn tán do sự mới lạ ban đầu sớm muộn gì cũng qua đi, làm sao để phân loại rác trở thành thường ngày?"),
         F(2, "Ví dụ hai: 这几年来，他千方百计地想求得名利，想不到事与愿违，到头来终究是竹篮打水一场空。 Mấy năm nay anh ta tìm trăm phương nghìn kế để mưu cầu danh lợi, không ngờ sự việc trái với mong muốn, rốt cuộc chỉ là dã tràng xe cát. 竹篮打水一场空 là lấy giỏ tre múc nước, công cốc."),
         F(3, "Ví dụ ba: 你何必要患得患失呢，是你的终究会是你的，别人抢不走的。 Bạn cần gì phải lo được lo mất, cái gì là của bạn thì rốt cuộc vẫn là của bạn, người khác không cướp được đâu. Câu này lại có cả mẫu 何必 nữa.")])

# ======================= KẾT HỢP TỪ & THÀNH NGỮ =======================
add("bullets", chapter="Kết hợp từ & thành ngữ", section="Kết hợp từ 词语搭配", title="Kết hợp từ (1): 消磨 · 纵观 · 填补", size=33,
    items=["## 消磨 + N.：～热情 · ～时间 · ～耐心",
           "日复一日的工作并没有让他的身体感到疲惫，却在不断地消磨着他的耐心。",
           "## 纵观 + N.：～历史 · ～局势 · ～社会",
           "纵观世界局势，既有空前的机遇，也有许多难以预见的挑战。",
           "## 填补 + N.：～空白 · ～缺陷 · ～需求",
           "道德常常能填补智慧的缺陷，而智慧却填补不了道德的短板。"],
    say=["Tiếp theo là phần kết hợp từ, 词语搭配.",
         F(0, "消磨 đi với 热情，时间，耐心: làm nguội nhiệt tình, giết thời gian, bào mòn sự kiên nhẫn."),
         F(1, "Ví dụ: 日复一日的工作并没有让他的身体感到疲惫，却在不断地消磨着他的耐心。 Công việc ngày này qua ngày khác không làm cơ thể anh ấy mệt mỏi, nhưng lại không ngừng bào mòn sự kiên nhẫn của anh ấy."),
         F(2, "纵观 đi với 历史，局势，社会: nhìn lại lịch sử, nhìn bao quát cục diện, nhìn khắp xã hội."),
         F(3, "Ví dụ: 纵观世界局势，既有空前的机遇，也有许多难以预见的挑战。 Nhìn bao quát cục diện thế giới, vừa có cơ hội chưa từng có, vừa có nhiều thách thức khó lường trước."),
         F(4, "填补 đi với 空白，缺陷，需求: lấp khoảng trống, bù khiếm khuyết, đáp ứng nhu cầu còn thiếu."),
         F(5, "Ví dụ: 道德常常能填补智慧的缺陷，而智慧却填补不了道德的短板。 Đạo đức thường bù đắp được khiếm khuyết của trí tuệ, còn trí tuệ thì không bù được chỗ thiếu của đạo đức. 短板 là điểm yếu, tấm ván ngắn.")])

add("bullets", section="Kết hợp từ 词语搭配", title="Kết hợp từ (2): 鼓足 · 树立", size=34,
    items=["## 鼓足 + N.：～士气 · ～勇气 · ～干劲",
           "站在黄山脚下，我们望而生畏，但鼓足勇气登上去后，却体会到前所未有的成就感。",
           "## 树立 + N.：～风气 · ～榜样 · ～目标",
           "班干部要以身作则，为同学们树立爱学习、守纪律的榜样。",
           "“万事开头难”，我们要做一件事，树立目标只是第一步，之后还要踏踏实实付出努力。"],
    say=[F(0, "鼓足 đi với 士气，勇气，干劲: dâng cao khí thế, lấy hết can đảm, dồn hết nhiệt huyết."),
         F(1, "Ví dụ: 站在黄山脚下，我们望而生畏，但鼓足勇气登上去后，却体会到前所未有的成就感。 Đứng dưới chân núi Hoàng Sơn, chúng tôi nhìn mà thấy sợ, nhưng sau khi lấy hết can đảm leo lên, lại cảm nhận được niềm tự hào chưa từng có."),
         F(2, "树立 đi với 风气，榜样，目标: tạo dựng nếp sống, làm gương, đặt mục tiêu."),
         F(3, "Ví dụ: 班干部要以身作则，为同学们树立爱学习、守纪律的榜样。 Cán bộ lớp phải lấy mình làm gương, làm tấm gương chăm học, giữ kỷ luật cho các bạn."),
         F(4, "Ví dụ: 万事开头难，我们要做一件事，树立目标只是第一步，之后还要踏踏实实付出努力。 Vạn sự khởi đầu nan; muốn làm một việc, đặt mục tiêu chỉ là bước đầu, sau đó còn phải chăm chỉ, vững vàng bỏ công sức.")])

add("bullets", section="Thành ngữ 成语和惯用语", title="Thành ngữ (1): 一蹴而就 · 刚柔并济 · 循序渐进 · 一鼓作气", size=32,
    items=["## 一蹴而就 yīcù'érjiù – một bước là thành công",
           "学习任何技能技巧，都不会是一蹴而就，而是要付出艰苦的劳动才能成功。",
           "## 刚柔并济 gāngróu-bìngjì – cương nhu kết hợp",
           "为人处事须刚柔并济，把握分寸，事情才能处理得圆满。",
           "## 循序渐进 xúnxù-jiànjìn – tuần tự tiến dần",
           "学习要循序渐进，不先掌握扎实的基础知识，就无法进行深入研究。",
           "## 一鼓作气 yīgǔ-zuòqì – thừa thắng làm một mạch",
           "老师提醒大家：参加比赛有如作战，要一鼓作气，才能夺得胜利。"],
    say=["Bài này có tám thành ngữ và quán ngữ, 成语和惯用语. Đây đều là những thành ngữ rất hay dùng trong văn nghị luận. Chúng ta học bốn thành ngữ đầu.",
         F(0, "一蹴而就. 蹴 là bước, đạp: chỉ một bước là xong, chỉ việc dễ dàng thành công ngay. Thường dùng ở dạng phủ định: 并非一蹴而就，不可能一蹴而就. Trong bài: 上海的垃圾分类并非一蹴而就."),
         F(1, "Ví dụ: 学习任何技能技巧，都不会是一蹴而就，而是要付出艰苦的劳动才能成功。 Học bất cứ kỹ năng nào cũng không thể một bước là thành, mà phải bỏ ra công sức gian khổ mới thành công."),
         F(2, "刚柔并济: 刚 là cứng rắn, 柔 là mềm mỏng, 并济 là cùng bổ trợ nhau: cương nhu kết hợp. Trong bài: 政策制定与推行需要刚柔并济."),
         F(3, "Ví dụ: 为人处事须刚柔并济，把握分寸，事情才能处理得圆满。 Đối nhân xử thế phải cương nhu kết hợp, biết giữ chừng mực, thì mọi việc mới giải quyết được trọn vẹn."),
         F(4, "循序渐进: tuần theo thứ tự, tiến dần từng bước. Trong bài: 也要循序渐进，给公众留出适应时间."),
         F(5, "Ví dụ: 学习要循序渐进，不先掌握扎实的基础知识，就无法进行深入研究。 Học phải tiến từng bước; không nắm vững kiến thức cơ bản trước thì không thể nghiên cứu sâu."),
         F(6, "一鼓作气: thời xưa ra trận, hồi trống đầu tiên khí thế binh sĩ mạnh nhất. Nghĩa bóng là thừa lúc hăng hái nhất mà làm một mạch cho xong. Trong bài: 推进过程中要一鼓作气、果断坚决."),
         F(7, "Ví dụ: 老师提醒大家：参加比赛有如作战，要一鼓作气，才能夺得胜利。 Thầy nhắc mọi người: thi đấu như ra trận, phải làm một mạch mới giành được chiến thắng.")])

add("bullets", section="Thành ngữ 成语和惯用语", title="Thành ngữ (2): 坚持不懈 · 一环扣一环 · 一时兴起 · 毕其功于一役", size=32,
    items=["## 坚持不懈 jiānchí-bùxiè – kiên trì không ngừng",
           "人们常说“有志者事竟成”，只有坚持不懈地努力拼搏，才能有所成就。",
           "## 一环扣一环 yī huán kòu yī huán – các khâu móc nối chặt chẽ",
           "这部电影人物众多、关系复杂，剧情一环扣一环、层层递进，扣人心弦。",
           "## 一时兴起 yīshí xìngqǐ – hứng lên nhất thời",
           "他买这些书只是一时兴起，带回家后就再也没翻开过。",
           "## 毕其功于一役 bì qí gōng yú yī yì – làm xong mọi việc trong một trận",
           "创建精神文明城市不能毕其功于一役，需要打持久战，年复一年，长抓不懈。"],
    say=["Bốn thành ngữ tiếp theo.",
         F(0, "坚持不懈: 懈 là lơi lỏng: kiên trì không chút lơi lỏng. Trong bài: 要坚持不懈地引导."),
         F(1, "Ví dụ: 人们常说有志者事竟成，只有坚持不懈地努力拼搏，才能有所成就。 Người ta thường nói có chí thì nên, chỉ có kiên trì nỗ lực phấn đấu không ngừng mới đạt được thành tựu."),
         F(2, "一环扣一环: vòng này móc vào vòng kia, chỉ các sự việc liên quan chặt chẽ với nhau như mắt xích. Trong bài: 投放、收集、运输、处理等一环扣一环."),
         F(3, "Ví dụ: 这部电影人物众多、关系复杂，剧情一环扣一环、层层递进，扣人心弦。 Bộ phim này nhiều nhân vật, quan hệ phức tạp, tình tiết móc nối chặt chẽ, tăng tiến từng lớp, vô cùng hấp dẫn."),
         F(4, "一时兴起: chữ 兴 đọc xìng, thanh bốn: bỗng nhiên nổi hứng nhất thời. Trong bài: 一时兴起的兴奋劲才会内化为持久的习惯."),
         F(5, "Ví dụ: 他买这些书只是一时兴起，带回家后就再也没翻开过。 Anh ấy mua mấy cuốn sách này chỉ vì hứng lên nhất thời, mang về nhà rồi không bao giờ mở ra nữa."),
         F(6, "毕其功于一役: 毕 là hoàn thành, 役 là trận đánh: muốn hoàn thành mọi việc chỉ trong một trận; cũng chỉ sự nóng vội muốn thành công ngay. Thường dùng ở dạng phủ định. Trong bài: 好习惯的养成不可能毕其功于一役."),
         F(7, "Ví dụ: 创建精神文明城市不能毕其功于一役，需要打持久战，年复一年，长抓不懈。 Xây dựng thành phố văn minh không thể xong trong một trận, cần đánh trận trường kỳ, năm này qua năm khác, kiên trì không lơi lỏng. Các bạn để ý, 毕其功于一役 và 持久战 thường đi cùng nhau.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 课后练习", title="Bài tập 1: Chọn từ điền vào chỗ trống (1)", reveal=True, size=33,
    items=["## 内化 · 磨合 · 公信力 · 坚持不懈 · 一时兴起 · 纵观 · 消磨 · 填补 · 热词 · 持久战 · 毕其功于一役",
           "(1) 爱情需要两个人相互___，两个人相互容忍，才能相处融洽。",
           "Đáp án: 磨合",
           "(2) 维护职业规范与操守，要严防媒体自由度的过界，捍卫司法的独立性，提高司法的___。",
           "Đáp án: 公信力",
           "(3) 教育的基本功能是把人类所创造的文化科学知识或经验___为个体的精神财富。",
           "Đáp án: 内化",
           "(4) 循环经济从理论到实践，都还有许多空白等待___和研究。",
           "Đáp án: 填补"],
    say=["Bây giờ chúng ta sang phần luyện tập của sách. Bài tập một: chọn từ thích hợp điền vào chỗ trống. Có mười một từ: 内化，磨合，公信力，坚持不懈，一时兴起，纵观，消磨，填补，热词，持久战，毕其功于一役.",
         F(1, "Câu một: 爱情需要两个人相互什么，两个人相互容忍，才能相处融洽。 Tình yêu cần hai người cùng làm gì, cùng bao dung nhau, mới sống hòa hợp được. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 磨合. 相互磨合, thích nghi với nhau."),
         F(3, "Câu hai: 维护职业规范与操守，要严防媒体自由度的过界，捍卫司法的独立性，提高司法的什么。 Giữ gìn chuẩn mực và đạo đức nghề nghiệp, phải đề phòng truyền thông tự do quá giới hạn, bảo vệ tính độc lập của tư pháp, nâng cao cái gì của tư pháp."),
         F(4, "Đáp án: 公信力. 提高司法的公信力, nâng cao uy tín của tư pháp."),
         F(5, "Câu ba: 教育的基本功能是把人类所创造的文化科学知识或经验什么为个体的精神财富。 Chức năng cơ bản của giáo dục là biến tri thức, kinh nghiệm mà loài người tạo ra thành của cải tinh thần của mỗi cá nhân."),
         F(6, "Đáp án: 内化. Mẫu 把A内化为B, chuyển hóa A thành B."),
         F(7, "Câu bốn: 循环经济从理论到实践，都还有许多空白等待什么和研究。 Kinh tế tuần hoàn từ lý thuyết đến thực tiễn đều còn nhiều khoảng trống chờ được làm gì và nghiên cứu."),
         F(8, "Đáp án: 填补. 填补空白, lấp khoảng trống.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 1: Chọn từ điền vào chỗ trống (2)", reveal=True, size=33,
    items=["(5) 高考是一场___，只有___的人才能笑到最后。",
           "Đáp án: 持久战 · 坚持不懈",
           "(6) ___今年国际经济形势，世界经济增长速度将进一步放慢，国际贸易环境更加趋紧，因此扩大出口会更加困难。",
           "Đáp án: 纵观",
           "(7) 我喜欢去充满书香、咖啡香的书店，写稿、看书、打瞌睡，___午后的时光。",
           "Đáp án: 消磨"],
    say=[F(0, "Câu năm có hai chỗ trống: 高考是一场什么，只有什么的人才能笑到最后。 Kỳ thi đại học là một cái gì, chỉ người như thế nào mới cười được đến cuối cùng."),
         F(1, "Đáp án: 持久战 và 坚持不懈. 高考是一场持久战，只有坚持不懈的人才能笑到最后。 Thi đại học là một cuộc chiến trường kỳ, chỉ người kiên trì không ngừng mới là người cười sau cùng."),
         F(2, "Câu sáu: 什么今年国际经济形势，世界经济增长速度将进一步放慢，国际贸易环境更加趋紧，因此扩大出口会更加困难。 Làm gì tình hình kinh tế quốc tế năm nay: tốc độ tăng trưởng kinh tế thế giới sẽ chậm lại hơn nữa, môi trường thương mại quốc tế càng căng thẳng, nên mở rộng xuất khẩu sẽ càng khó."),
         F(3, "Đáp án: 纵观. 纵观今年国际经济形势, nhìn bao quát tình hình kinh tế quốc tế năm nay. Từ này thường đứng đầu câu."),
         F(4, "Câu bảy: 我喜欢去充满书香、咖啡香的书店，写稿、看书、打瞌睡，什么午后的时光。 Tôi thích đến hiệu sách thơm mùi sách, mùi cà phê, viết bài, đọc sách, ngủ gà ngủ gật, làm gì với buổi chiều."),
         F(5, "Đáp án: 消磨. 消磨午后的时光, thong thả trải qua buổi chiều.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 1: Chọn từ điền vào chỗ trống (3)", reveal=True, size=33,
    items=["(8) “锦鲤”作为___意外走红，成为“好运”的象征，隐含着人们对美好生活的向往。",
           "Đáp án: 热词",
           "(9) 该品牌的失败，是因为把过多资金、精力、希望都放在广告宣传上，期望___。",
           "Đáp án: 毕其功于一役",
           "(10) 我之所以大力投资人工智能行业，是因为看好其发展前景，并非___。",
           "Đáp án: 一时兴起"],
    say=[F(0, "Câu tám: 锦鲤作为什么意外走红，成为好运的象征，隐含着人们对美好生活的向往。 Cá chép Koi, với tư cách là một cái gì đó, bất ngờ nổi tiếng, trở thành biểu tượng của may mắn, ẩn chứa niềm khao khát của mọi người về cuộc sống tốt đẹp."),
         F(1, "Đáp án: 热词. 锦鲤作为热词意外走红. Trên mạng Trung Quốc, 锦鲤 chỉ người cực kỳ may mắn."),
         F(2, "Câu chín: 该品牌的失败，是因为把过多资金、精力、希望都放在广告宣传上，期望什么。 Thương hiệu này thất bại vì dồn quá nhiều vốn, sức lực và hy vọng vào quảng cáo, mong muốn điều gì."),
         F(3, "Đáp án: 毕其功于一役. Mong một trận quảng cáo là thành công ngay, đây là nghĩa nóng vội của thành ngữ."),
         F(4, "Câu mười: 我之所以大力投资人工智能行业，是因为看好其发展前景，并非什么。 Sở dĩ tôi đầu tư mạnh vào ngành trí tuệ nhân tạo là vì tin vào triển vọng phát triển của nó, chứ không phải vì sao."),
         F(5, "Đáp án: 一时兴起. 并非一时兴起, không phải hứng lên nhất thời. Câu này kết hợp cả mẫu 之所以……是因为…… và 并非.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn đáp án đúng (1)", reveal=True, size=33,
    items=["(1) 作家对知识分子的自我批判、灵魂（ ）给作品带来了前所未有的深度。 A.拷问 B.检查 C.监督 D.审计",
           "Đáp án: A. 拷问 – 灵魂拷问",
           "(2) 那个地方只有（ ）几条街道，但却拥有该市近半的纳税大户。 A.短短 B.长长 C.区区 D.小小",
           "Đáp án: C. 区区 – + số lượng: ít ỏi",
           "(3) 要抓好小城镇户籍管理制度改革的（ ）工作…… A.使用 B.试点 C.举措 D.尝试",
           "Đáp án: B. 试点 – 试点工作",
           "(4) 由于突如其来的疫情，大家（ ）已久的旅游计划被取消了。 A.沉淀 B.累积 C.酝酿 D.斟酌",
           "Đáp án: C. 酝酿 – 酝酿已久的计划"],
    say=["Bài tập hai: chọn đáp án đúng.",
         F(0, "Câu một: 作家对知识分子的自我批判、灵魂什么给作品带来了前所未有的深度。 Sự tự phê phán và cái gì của tâm hồn mà nhà văn dành cho giới trí thức đã mang lại cho tác phẩm chiều sâu chưa từng có. A, 拷问; B, 检查; C, 监督; D, 审计."),
         F(1, "Đáp án: A, 拷问. 灵魂拷问, sự chất vấn tâm hồn, là kết hợp cố định."),
         F(2, "Câu hai: 那个地方只有什么几条街道，但却拥有该市近半的纳税大户。 Nơi đó chỉ có mấy con phố như thế nào, nhưng lại có gần một nửa số doanh nghiệp nộp thuế lớn của thành phố. A, 短短; B, 长长; C, 区区; D, 小小."),
         F(3, "Đáp án: C, 区区. 区区几条街道, chỉ vài con phố ít ỏi; đặt cạnh 近半的纳税大户 để tạo sự tương phản."),
         F(4, "Câu ba: 要抓好小城镇户籍管理制度改革的什么工作，制定支持小城镇发展的相关政策。 Phải làm tốt công tác gì trong cải cách chế độ quản lý hộ tịch ở các thị trấn nhỏ. A, 使用; B, 试点; C, 举措; D, 尝试."),
         F(5, "Đáp án: B, 试点. 试点工作, công tác thí điểm."),
         F(6, "Câu bốn: 由于突如其来的疫情，大家什么已久的旅游计划被取消了。 Vì dịch bệnh ập đến bất ngờ, kế hoạch du lịch mà mọi người làm gì từ lâu đã bị hủy. A, 沉淀; B, 累积; C, 酝酿; D, 斟酌."),
         F(7, "Đáp án: C, 酝酿. 酝酿已久的旅游计划, kế hoạch du lịch ấp ủ đã lâu.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn đáp án đúng (2)", reveal=True, size=33,
    items=["(5) 一粒金子，可以悄无声息地在风沙中（ ）掉，也可以散发出耀眼光芒。 A.消磨 B.失去 C.花费 D.耗费",
           "Đáp án: A. 消磨 – bị bào mòn dần",
           "(6) 尝试可能会失败，但每一次的尝试都是为下一次的成功做（ ）。 A.伏笔 B.奠定 C.衬托 D.铺垫",
           "Đáp án: D. 铺垫 – 为……做铺垫",
           "(7) 道德可以弥补知识的不足，知识无法（ ）道德的空白。 A.补充 B.填补 C.填空 D.填满",
           "Đáp án: B. 填补 – 填补空白"],
    say=[F(0, "Câu năm: 一粒金子，可以悄无声息地在风沙中什么掉，也可以散发出耀眼光芒。 Một hạt vàng có thể lặng lẽ bị làm sao trong gió cát, cũng có thể tỏa ra ánh sáng chói lọi. A, 消磨; B, 失去; C, 花费; D, 耗费."),
         F(1, "Đáp án: A, 消磨. 在风沙中消磨掉, bị gió cát bào mòn dần. 花费 và 耗费 là tiêu tốn tiền bạc, sức lực; 失去 không đi với 掉 trong ngữ cảnh này."),
         F(2, "Câu sáu: 尝试可能会失败，但每一次的尝试都是为下一次的成功做什么。 Thử có thể thất bại, nhưng mỗi lần thử đều là làm gì cho thành công lần sau. A, 伏笔; B, 奠定; C, 衬托; D, 铺垫."),
         F(3, "Đáp án: D, 铺垫. Mẫu câu 为某事做铺垫. 伏笔 là chi tiết cài cắm trong tác phẩm văn học; 奠定 phải đi với 基础."),
         F(4, "Câu bảy: 道德可以弥补知识的不足，知识无法什么道德的空白。 Đạo đức có thể bù đắp sự thiếu hụt của tri thức, còn tri thức không thể làm gì khoảng trống của đạo đức. A, 补充; B, 填补; C, 填空; D, 填满."),
         F(5, "Đáp án: B, 填补. 填补空白, lấp khoảng trống, là kết hợp cố định.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ, mẫu câu cho sẵn để trả lời (1)", reveal=True, size=33,
    items=["(1) 人们过去是如何处理垃圾的？（一……了之）",
           "Đáp án gợi ý: 过去人们常常把废弃物胡乱丢进垃圾桶，一扔了之，根本不分类。",
           "(2) 如何贯彻执行“垃圾分类”举措？（经过……磨合）",
           "Đáp án gợi ý: 要经过政府和居民之间长期的磨合：政府既要严格执法，也要耐心引导，居民也要慢慢适应，养成习惯。",
           "(3) 上海市垃圾分类后取得显著效果的原因是什么？（并非……而是……）",
           "Đáp án gợi ý: 上海的成功并非一蹴而就，而是十九年来不断试错和创新的结果，立法强制执行也起了关键作用。"],
    say=["Bài tập ba: dùng từ và mẫu câu cho sẵn để trả lời câu hỏi. Đây là câu hỏi mở, thầy đưa ra đáp án gợi ý.",
         F(0, "Câu một, dùng mẫu 一什么了之: 人们过去是如何处理垃圾的？ Trước đây người ta xử lý rác thế nào?"),
         F(1, "Đáp án gợi ý: 过去人们常常把废弃物胡乱丢进垃圾桶，一扔了之，根本不分类。 Trước đây người ta thường vứt bừa đồ bỏ đi vào thùng rác, vứt xong là xong, hoàn toàn không phân loại."),
         F(2, "Câu hai, dùng 经过磨合: 如何贯彻执行垃圾分类举措？ Làm thế nào để quán triệt thực hiện biện pháp phân loại rác?"),
         F(3, "Đáp án gợi ý: 要经过政府和居民之间长期的磨合：政府既要严格执法，也要耐心引导，居民也要慢慢适应，养成习惯。 Cần một thời gian dài để chính quyền và người dân thích nghi với nhau: chính quyền vừa phải thực thi nghiêm, vừa phải kiên nhẫn hướng dẫn; người dân cũng phải dần thích nghi, hình thành thói quen."),
         F(4, "Câu ba, dùng 并非而是: 上海市垃圾分类后取得显著效果的原因是什么？ Vì sao Thượng Hải đạt hiệu quả rõ rệt sau khi phân loại rác?"),
         F(5, "Đáp án gợi ý: 上海的成功并非一蹴而就，而是十九年来不断试错和创新的结果，立法强制执行也起了关键作用。 Thành công của Thượng Hải không phải một bước là xong, mà là kết quả của mười chín năm không ngừng thử sai và đổi mới; việc lập pháp bắt buộc thực hiện cũng đóng vai trò then chốt.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ, mẫu câu cho sẵn để trả lời (2)", reveal=True, size=33,
    items=["(4) 什么加速了垃圾分类理念被认同？（为……做铺垫）",
           "Đáp án gợi ý: 基层的大量试点和广泛的社会动员为理念被认同做好了铺垫；同时，人们切身感受到“垃圾围城”的风险，这加速了理念被认同。",
           "(5) 我国提倡绿色环保，有什么意义？（终究）",
           "Đáp án gợi ý: 绿色环保终究关系到每个人的生活和子孙后代的未来。热议终究会过去，只有养成习惯，才有生态文明的可持续进步。"],
    say=[F(0, "Câu bốn, dùng 为某事做铺垫: 什么加速了垃圾分类理念被认同？ Điều gì đã đẩy nhanh việc ý thức phân loại rác được đồng tình?"),
         F(1, "Đáp án gợi ý: 基层的大量试点和广泛的社会动员为理念被认同做好了铺垫；同时，人们切身感受到垃圾围城的风险，这加速了理念被认同。 Các điểm thí điểm ở cơ sở và sự vận động xã hội rộng rãi đã làm nền; đồng thời, người dân tự mình cảm nhận nguy cơ rác bao vây thành phố, điều đó đã đẩy nhanh sự đồng tình."),
         F(2, "Câu năm, dùng 终究: 我国提倡绿色环保，有什么意义？ Đất nước đề xướng bảo vệ môi trường xanh có ý nghĩa gì? Câu hỏi đứng ở góc độ người Trung Quốc; khi trả lời, các bạn có thể nói về Việt Nam."),
         F(3, "Đáp án gợi ý: 绿色环保终究关系到每个人的生活和子孙后代的未来。热议终究会过去，只有养成习惯，才有生态文明的可持续进步。 Bảo vệ môi trường suy cho cùng liên quan đến cuộc sống của mỗi người và tương lai của con cháu. Những bàn tán rồi sẽ qua, chỉ khi hình thành thói quen mới có tiến bộ bền vững của văn minh sinh thái.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Điền từ vào đoạn văn (1)", reveal=True, size=33,
    items=["## Từ cho sẵn: 热词 · 协力 · 投放 · 理念 · 践行 · 循序渐进",
           "在国家政策的引导和鼓励下，绿色环保的___如今已经成为人们日常生活中的___之一。垃圾分类___，我们需要以点带面、___地动员全社会民众积极参与，___环保。尽管这个过程是漫长而又艰难的，但我们相信，在不久的将来，在社会各方的同心___下，环保行业将迎来新格局……",
           "Đáp án: 理念 · 热词 · 投放 · 循序渐进 · 践行 · 协力"],
    say=["Bài tập bốn: chọn từ cho sẵn điền vào đoạn văn. Đoạn một có sáu từ: 热词，协力，投放，理念，践行，循序渐进.",
         F(1, "在国家政策的引导和鼓励下，绿色环保的什么如今已经成为人们日常生活中的什么之一。垃圾分类什么，我们需要以点带面、什么地动员全社会民众积极参与，什么环保。尽管这个过程是漫长而又艰难的，但我们相信，在不久的将来，在社会各方的同心什么下，环保行业将迎来新格局。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 绿色环保的理念如今已经成为人们日常生活中的热词之一。垃圾分类投放，我们需要以点带面、循序渐进地动员全社会民众积极参与，践行环保。……在社会各方的同心协力下。 Dưới sự dẫn dắt và khuyến khích của chính sách, ý thức sống xanh nay đã thành một trong những từ khóa hot của đời sống; về việc phân loại khi bỏ rác, chúng ta cần lấy điểm kéo diện, từng bước vận động toàn dân tích cực tham gia, thực hành bảo vệ môi trường. 以点带面 là lấy điểm kéo diện, từ thí điểm nhân rộng ra; 同心协力 là đồng lòng hợp sức.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Điền từ vào đoạn văn (2)", reveal=True, size=32,
    items=["## Từ cho sẵn: 磨合 · 填补 · 持久战 · 一蹴而就 · 借鉴 · 纵观",
           "……垃圾处理成为一个无法回避但也无法___的难题。……虽然经历了漫长的___，现状同样不容乐观。垃圾处理方面还有许多等待___的空白。___世界各大主要经济体，经过数百年的___，很多发达国家在垃圾处理方面已经找到了一些行之有效的方法和途径，值得我们学习和___。",
           "Đáp án: 一蹴而就 · 持久战 · 填补 · 纵观 · 磨合 · 借鉴"],
    say=["Đoạn hai có sáu từ: 磨合，填补，持久战，一蹴而就，借鉴，纵观.",
         F(1, "随着我国城镇化进程的加快，城市人口密度的不断增长，垃圾处理成为一个无法回避但也无法什么的难题。……虽然经历了漫长的什么，现状同样不容乐观。垃圾处理方面还有许多等待什么的空白。什么世界各大主要经济体，经过数百年的什么，很多发达国家在垃圾处理方面已经找到了一些行之有效的方法和途径，值得我们学习和什么。"),
         F(2, "Đáp án: 无法一蹴而就的难题, bài toán không thể giải quyết trong một bước; 经历了漫长的持久战, đã trải qua cuộc chiến trường kỳ dài đằng đẵng; 等待填补的空白, khoảng trống chờ được lấp; 纵观世界各大主要经济体, nhìn khắp các nền kinh tế lớn trên thế giới; 经过数百年的磨合, trải qua mấy trăm năm mài giũa; và 值得我们学习和借鉴, đáng để chúng ta học tập và tham khảo. Đoạn văn kết thúc bằng ý: phải thiết kế cơ chế xử lý rác phù hợp với tình hình của nước mình.")])

# ======================= THẢO LUẬN =======================
add("bullets", chapter="Thảo luận", section="Thảo luận 讨论", title="Thảo luận: rác sinh hoạt ở Việt Nam", reveal=True, size=33,
    items=["在你们国家，家庭生活的垃圾是如何处理的？",
           "Đáp án gợi ý: 在越南，以前大部分家庭都把垃圾混在一起扔。根据2020年的《环境保护法》，从2025年起，家庭垃圾要分成可回收垃圾、食物垃圾和其他垃圾三类。不过，要真正做到“随手分”，还需要时间和耐心。",
           "## Liên hệ Việt Nam",
           "Luật Bảo vệ môi trường 2020: hộ gia đình phân loại rác tại nguồn thành 3 nhóm; thu phí theo khối lượng, thể tích",
           "Thử nói: 你觉得越南推行垃圾分类，应该“刚”一点还是“柔”一点？"],
    say=["Bây giờ chúng ta quay lại câu hỏi khởi động đầu tiên: 在你们国家，家庭生活的垃圾是如何处理的？ Ở nước bạn, rác sinh hoạt gia đình được xử lý thế nào?",
         F(0, "Các bạn tạm dừng video, thử nói vài câu bằng tiếng Trung, dùng các từ vừa học như 强制，试点，循序渐进，刚柔并济."),
         F(1, "Đáp án gợi ý: 在越南，以前大部分家庭都把垃圾混在一起扔。根据二零二零年的环境保护法，从二零二五年起，家庭垃圾要分成可回收垃圾、食物垃圾和其他垃圾三类。不过，要真正做到随手分，还需要时间和耐心。 Ở Việt Nam, trước đây phần lớn gia đình bỏ chung rác với nhau. Theo Luật Bảo vệ môi trường năm 2020, từ năm 2025, rác sinh hoạt phải phân thành ba nhóm: rác tái chế, rác thực phẩm và rác khác. Tuy vậy, để thật sự tiện tay phân loại, vẫn cần thời gian và sự kiên nhẫn."),
         F(2, "Cùng liên hệ thêm với Việt Nam."),
         F(3, "Luật Bảo vệ môi trường năm 2020 quy định hộ gia đình phải phân loại rác tại nguồn thành ba nhóm chính, và hướng tới thu phí theo khối lượng hoặc thể tích rác thải ra: càng thải nhiều, càng trả nhiều. Cũng giống Thượng Hải, khó nhất là đổi thói quen, và bảo đảm khâu thu gom phía sau không đổ chung trở lại."),
         F(4, "Các bạn thử nói: 你觉得越南推行垃圾分类，应该刚一点还是柔一点？ Theo bạn, Việt Nam triển khai phân loại rác nên cương hơn hay nhu hơn? Ví dụ: 我认为应该刚柔并济：先循序渐进地宣传和试点，再严格执行。")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết", section="Tổng kết", title="Tổng kết bài 3.2", size=34,
    items=["Từ vựng trọng tâm: 强制 · 试点 · 铺垫 · 理念 · 消磨 · 磨合 · 纵观 · 到位 · 填补 · 借鉴 · 一刀切 · 硬性 · 公信力 · 长效 · 内化",
           "Thành ngữ: 一蹴而就 · 刚柔并济 · 循序渐进 · 一鼓作气 · 坚持不懈 · 一环扣一环 · 一时兴起 · 毕其功于一役",
           "Mẫu câu: 一V了之 · A归A · 区区 · 何必 · 并非……而是…… · 为……做铺垫 · 经过……磨合 · 终究",
           "Ý chính: phân loại rác 并非一蹴而就 → cần 刚柔并济 và 长效机制, biến “随手扔” thành “随手分”",
           "## Bài tập về nhà",
           "Viết đoạn văn 300 chữ: 越南的垃圾分类应该怎样从“时尚”走向“日常”？"],
    say=["Chúng ta cùng tổng kết bài ba chấm hai.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 强制，试点，铺垫，理念，消磨，磨合，纵观，到位，填补，借鉴，一刀切，硬性，公信力，长效，内化."),
         F(1, "Tám thành ngữ: 一蹴而就，刚柔并济，循序渐进，一鼓作气，坚持不懈，一环扣一环，一时兴起，毕其功于一役."),
         F(2, "Tám mẫu câu: 一扔了之 theo mẫu 一 động từ 了之; 玩笑归玩笑 theo mẫu A归A; 区区 và 何必; 并非而是; 为某事做铺垫; 经过磨合; và 终究."),
         F(3, "Về nội dung: phân loại rác ở Thượng Hải không phải một bước là xong; chính sách cần cương nhu kết hợp, cần cơ chế lâu dài, và cần sự tham gia của toàn dân, để biến tiện tay vứt thành tiện tay phân loại."),
         F(5, "Bài tập về nhà: hãy viết một đoạn văn khoảng ba trăm chữ với đề 越南的垃圾分类应该怎样从时尚走向日常, phân loại rác ở Việt Nam làm sao để từ trào lưu trở thành thường ngày. Cố gắng dùng các mẫu câu như 并非而是，为某事做铺垫，终究, và vài thành ngữ của bài."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Bài sau là bài cuối của Đơn vị ba, bài ba chấm ba: 塑战能否速决？ Cuộc chiến với nhựa có thể thắng nhanh không? Chúng ta sẽ bàn về túi ni lông, lệnh hạn chế và lệnh cấm đồ nhựa, và vì sao sống không nhựa lại khó đến vậy. Hẹn gặp lại các bạn. Chúc các bạn học tốt!"])

lesson = {
    "title": "顶石中文 – Bài 3.2: “随手扔”还是“随手分”，你“拎得清”吗？ (Tiện tay vứt hay tiện tay phân loại?)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"了之": "蓼之",            # liǎozhī (一扔了之、一走了之、一笑了之)
                    "干垃圾": "甘垃圾",        # gān lājī
                    "干香菇再干": "甘香菇再甘",  # gān
                    "倒垃圾": "到垃圾",        # dào lājī
                    "铺垫": "扑垫",            # pūdiàn
                    "切身": "窃身",            # qièshēn
                    "扎下根": "渣下根",        # zhā
                    "扎根": "渣根",            # zhāgēn
                    "长效": "常效",            # chángxiào
                    "长达": "常达",            # chángdá
                    "长期": "常期",            # chángqī
                    "划出": "画出",            # huàchū
                    "相应": "相映",            # xiāngyìng
                    "难处": "难触",            # nánchu
                    "空白": "控白",            # kòngbái
                    "调动": "掉动",            # diàodòng
                    "兴奋": "星奋",            # xīngfèn
                    "兴起": "星起",            # xìngqǐ (theo bộ thay âm sẵn có)
                    "内化为": "内化维",        # nèihuà wéi
                    "为随手分": "维随手分",    # wéi
                    "为最终": "位最终",        # wèi
                    "为之后": "位之后",        # wèi
                    "为明年": "位明年",        # wèi
                    "为其他城市": "位其他城市",  # wèi
                    "为下一次": "位下一次",    # wèi
                    "为理念": "位理念",        # wèi
                    "为以后": "位以后",        # wèi
                    "为某事": "位某事",        # wèi
                    "为同学们": "位同学们",    # wèi
                    "为钱财": "位钱财",        # wèi
                    "作为": "作维",            # zuòwéi
                    "处理": "楚理",            # chǔlǐ
                    "还价": "环价",            # huánjià
                    "干劲": "赣劲",            # gànjìn
                    "强制": "墙制",            # qiángzhì
                    "累积": "垒积",            # lěijī
                    "打瞌睡": "打瞌睡",
                    "散发": "伞发",            # sànfā
                    "处事": "楚事",            # chǔshì
                    "称为": "称维"},           # chēngwéi
    "slides": slides,
}
lesson["tts_replace"] = {k: v for k, v in lesson["tts_replace"].items() if k != v}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds32.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
