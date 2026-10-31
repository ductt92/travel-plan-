#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Thượng) – Bài 6 «当好职场插班生». Chạy để sinh bai06.json."""
import json
import os

TAG = "HSK 6 (Thượng) · Bài 6 · 当好职场插班生"
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
    zh="当好职场插班生", py="Dāng hǎo zhíchǎng chābānshēng",
    vi="Bài 6: Hãy là học sinh giỏi tại nơi làm việc",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Thượng.",
         "Hôm nay chúng ta học bài sáu: 当好职场插班生。 Sách dịch là: Hãy là học sinh giỏi tại nơi làm việc.",
         "Thầy giải thích tên bài một chút. 当好 là làm tốt vai trò. 职场 là chốn công sở, môi trường làm việc. Còn 插班生 vốn là học sinh vào học giữa chừng một lớp đang học. Ghép lại, tên bài có nghĩa là: hãy làm tốt vai trò của một người mới chen chân vào chốn công sở.",
         "Đây là bài thứ hai của Chủ đề hai, 不甘平庸, Không cam chịu tầm thường. Bài khóa kể lại những ngày đầu đi làm của nhân vật tôi: bị người cũ lạnh nhạt, bị giao toàn việc khó, nhưng anh ấy không so đo, dốc hết sức làm việc, và cuối cùng được mọi người công nhận.",
         "Ai trong chúng ta cũng từng là người mới ở một nơi nào đó. Hy vọng câu chuyện hôm nay sẽ cho các bạn thêm động lực."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài khóa: những ngày đầu ở công ty mới của nhân vật tôi và cách anh ấy vượt qua",
           "Nắm vững 46 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: phó từ 唯独, phó từ 明明, phó từ 大不了",
           "Phân biệt hai động từ 创立 và 创办",
           "Mở rộng: 12 cụm kết hợp từ (词语搭配) thường gặp"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa: những ngày đầu ở công ty mới của nhân vật tôi, những bất công anh ấy gặp phải, và cách anh ấy vượt qua."),
         F(1, "Thứ hai, nắm vững bốn mươi sáu từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học ba điểm ngữ pháp, đều là phó từ: 唯独, nghĩa là chỉ có, duy chỉ; 明明, nghĩa là rõ ràng; và 大不了, nghĩa là cùng lắm thì."),
         F(3, "Thứ tư, phân biệt hai động từ có nghĩa rất gần nhau: 创立 và 创办."),
         F(4, "Thứ năm, phần mở rộng: làm quen với mười hai từ và các cụm kết hợp từ thường gặp của chúng, tiếng Trung gọi là 词语搭配."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Câu hỏi khởi động: Lần đầu đến môi trường mới", size=40,
    items=["当你到了一个新环境时，曾经受到热情欢迎还是冷淡对待？",
           "比如：转学到一个新的班级 – chuyển đến một lớp mới",
           "刚加入一个新的球队或团体 – vừa gia nhập một đội bóng hay một nhóm mới",
           "第一天工作 – ngày đầu tiên đi làm",
           "具体说一说你当时的感受。 – Hãy kể cụ thể cảm nhận của bạn lúc đó."],
    say=["Chúng ta bắt đầu bằng phần khởi động. Câu hỏi đầu tiên rất gần gũi với cuộc sống của mỗi người.",
         F(0, "当你到了一个新环境时，曾经受到热情欢迎还是冷淡对待？ Khi bạn đến một môi trường mới, bạn từng được chào đón nhiệt tình, hay bị đối xử lạnh nhạt?"),
         F(1, "Ví dụ: 转学到一个新的班级。 Chuyển trường, vào một lớp học mới."),
         F(2, "刚加入一个新的球队或团体。 Vừa gia nhập một đội bóng, hay một nhóm, một tập thể mới."),
         F(3, "Hoặc 第一天工作。 Ngày đầu tiên đi làm."),
         F(4, "具体说一说你当时的感受。 Hãy kể cụ thể cảm nhận của bạn lúc đó. Các bạn tạm dừng video và thử kể bằng tiếng Trung nhé. Lát nữa đọc bài khóa, các bạn sẽ thấy ngày đầu đi làm của nhân vật tôi chẳng dễ chịu chút nào.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 手 và 色", size=38,
    items=["## 手 (thủ): người giỏi hoặc làm một việc nào đó",
           "老手 người lão luyện · 新手 người mới · 对手 đối thủ · 帮手 người giúp · 高手 cao thủ · 巧手 người khéo tay · 人手 nhân lực",
           "生手 người chưa thạo việc · 歌手 ca sĩ · 好手 tay giỏi · 快手 người làm nhanh · 能手 người giỏi · 多面手 người đa năng",
           "## 色 (sắc): sắc mặt, nét mặt",
           "脸色 sắc mặt · 面色 sắc mặt · 气色 khí sắc · 神色 thần sắc · 喜色 vẻ vui mừng",
           "眼色 ánh mắt ra hiệu · 变色 biến sắc · 不动声色 không lộ cảm xúc · 大惊失色 sợ tái mặt · 眉飞色舞 mặt mày hớn hở"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo, rất có lợi cho người Việt vì hầu hết các chữ đều có âm Hán Việt quen thuộc.",
         F(0, "Nhóm thứ nhất có chữ 手, Hán Việt là thủ, nghĩa gốc là bàn tay. Đứng cuối từ, nó chỉ người giỏi một việc, hoặc người làm một việc nào đó."),
         F(1, "老手，新手，对手，帮手，高手，巧手，人手。 Tức là: người lão luyện, người mới, đối thủ, người giúp việc, cao thủ, người khéo tay, và nhân lực. Bài khóa mở đầu bằng câu 这里老手多、新手少, ở đây người lâu năm nhiều, người mới ít."),
         F(2, "生手，歌手，好手，快手，能手，多面手。 Tức là: người chưa thạo việc, ca sĩ, tay giỏi, người làm nhanh, người giỏi, và người đa năng, việc gì cũng làm được."),
         F(3, "Nhóm thứ hai có chữ Hán Việt là sắc, như trong từ 脸色. Ở đây nó chỉ sắc mặt, nét mặt, tức là cảm xúc hiện lên trên khuôn mặt."),
         F(4, "脸色，面色，气色，神色，喜色。 Tức là: sắc mặt, sắc mặt, khí sắc, thần sắc, và vẻ vui mừng. Trong bài có câu 顿时小林的脸色变了, ngay lập tức sắc mặt Tiểu Lâm thay đổi."),
         F(5, "眼色，变色，不动声色，大惊失色，眉飞色舞。 Tức là: ánh mắt ra hiệu, biến sắc, không để lộ cảm xúc, sợ tái mặt, và mặt mày hớn hở. 眼色 là một từ mới của bài, chúng ta sẽ gặp lại ngay.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 化 và 式", size=38,
    items=["## 化 (hóa): biến thành, làm cho trở nên",
           "边缘化 bị gạt ra rìa · 丑化 bôi xấu · 美化 làm đẹp · 弱化 làm yếu đi · 淡化 làm nhạt đi · 强化 tăng cường",
           "软化 làm mềm · 硬化 xơ cứng · 绿化 phủ xanh · 多样化 đa dạng hóa · 大众化 đại chúng hóa · 现代化 hiện đại hóa",
           "## 式 (thức): kiểu, kiểu cách",
           "旧式 kiểu cũ · 老式 kiểu cũ · 新式 kiểu mới · 中式 kiểu Trung Quốc · 西式 kiểu Tây · 欧式 kiểu châu Âu",
           "美式 kiểu Mỹ · 飞跃式 kiểu nhảy vọt · 花园式 kiểu vườn · 家庭式 kiểu gia đình"],
    say=[F(0, "Nhóm thứ ba có chữ 化, Hán Việt là hóa. Đứng sau tính từ hoặc danh từ, nó biểu thị biến thành, hoặc làm cho trở nên như thế, giống chữ hóa trong hiện đại hóa của tiếng Việt."),
         F(1, "边缘化，丑化，美化，弱化，淡化，强化。 Tức là: bị gạt ra rìa, bôi xấu, làm đẹp, làm yếu đi, làm nhạt đi, và tăng cường. Bài khóa có câu 我也有被边缘化的感觉, tôi cũng có cảm giác bị gạt ra rìa."),
         F(2, "软化，硬化，绿化，多样化，大众化，现代化。 Tức là: làm mềm, xơ cứng, phủ xanh, đa dạng hóa, đại chúng hóa, và hiện đại hóa."),
         F(3, "Nhóm cuối cùng có chữ 式, Hán Việt là thức, nghĩa là kiểu, kiểu cách, như trong hình thức, công thức."),
         F(4, "旧式，老式，新式，中式，西式，欧式。 Tức là: kiểu cũ, kiểu cũ, kiểu mới, kiểu Trung Quốc, kiểu Tây, và kiểu châu Âu."),
         F(5, "美式，飞跃式，花园式，家庭式。 Tức là: kiểu Mỹ, kiểu nhảy vọt, kiểu vườn, và kiểu gia đình. Bài khóa có cụm 飞跃式的提高, sự tiến bộ kiểu nhảy vọt, tức là tiến bộ vượt bậc."),
         "Các bạn thấy không, chỉ cần nắm nghĩa của một chữ gốc, ta có thể đoán được nghĩa của cả một nhóm từ. Hãy áp dụng cách này khi học từ mới nhé."])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng)
V = [
    ("上任", "shàng rèn", "thượng nhậm", "động từ", "nhậm chức, nhận chức", "新经理上任后做了很多改革。", "Giám đốc mới nhậm chức xong đã cải cách rất nhiều.",
     "Động từ, nghĩa là nhậm chức, bắt đầu đảm nhận một chức vụ. Câu đầu tiên của bài khóa là 这天是我到这家公司上任的第一天, hôm nay là ngày đầu tiên tôi nhận chức ở công ty này."),
    ("职位", "zhíwèi", "chức vị", "danh từ", "chức vụ, vị trí công việc", "他在公司的职位是部门经理。", "Chức vụ của anh ấy ở công ty là trưởng phòng.",
     "Danh từ, nghĩa là chức vụ, vị trí công việc trong một tổ chức. Trong bài, 我的职位是咨询师, chức vụ của tôi là chuyên viên tư vấn."),
    ("资深", "zīshēn", "tư thâm", "tính từ", "thâm niên, lâu năm", "她是一位资深记者。", "Bà ấy là một phóng viên lâu năm.",
     "Tính từ, nghĩa là có thâm niên, lâu năm trong nghề. 资 là lý lịch, tư cách; 深 là sâu. Bài khóa nhắc nhiều lần cụm 资深员工, nhân viên lâu năm."),
    ("创立", "chuànglì", "sáng lập", "động từ", "sáng lập, thành lập", "这家公司创立于二十年前。", "Công ty này được thành lập từ hai mươi năm trước.",
     "Động từ, nghĩa là sáng lập, lập ra lần đầu. Âm tiết đầu đọc thanh bốn, Hán Việt là sáng, như trong sáng tạo. Trong bài, 在公司创立之初 là ngay từ lúc công ty mới thành lập. Lát nữa ta sẽ phân biệt 创立 với 创办."),
    ("沏", "qī", "thế", "động từ", "pha (trà, cà phê…)", "妈妈给客人沏了一壶茶。", "Mẹ pha cho khách một ấm trà.",
     "Động từ, nghĩa là rót nước sôi vào để pha trà hoặc cà phê. Hay gặp nhất là 沏茶, pha trà. Trong sách, từ này có đánh dấu sao, tức là từ nằm ngoài đề cương, các bạn chỉ cần hiểu nghĩa."),
    ("风气", "fēngqì", "phong khí", "danh từ", "bầu không khí, nếp sống, tập quán", "我们学校的学习风气很好。", "Bầu không khí học tập ở trường chúng tôi rất tốt.",
     "Danh từ, chỉ nếp sống, thói quen chung đang thịnh hành trong một tập thể hay một xã hội. Cẩn thận: không phải là gió hay không khí theo nghĩa thời tiết. Hay gặp: 社会风气, nếp sống xã hội; 学习风气, phong trào học tập."),
    ("唯独", "wéidú", "duy độc", "phó từ", "chỉ có, duy nhất", "大家都同意了，唯独他反对。", "Mọi người đều đồng ý, chỉ có anh ấy phản đối.",
     "Phó từ, nghĩa là chỉ có, duy chỉ có, tách riêng một đối tượng ra khỏi số đông. Đây là điểm ngữ pháp thứ nhất của bài."),
    ("搭档", "dādàng", "đáp đáng", "danh từ", "cộng sự, người cộng tác", "我们俩是工作上的好搭档。", "Hai chúng tôi là cặp cộng sự ăn ý trong công việc.",
     "Danh từ, chỉ người cùng hợp tác làm việc với mình, bạn đồng hành, cặp đôi ăn ý. Âm tiết thứ hai đọc thanh bốn. Trong bài, 搭档 của nhân vật tôi chính là Tiểu Lâm."),
    ("就职", "jiù zhí", "tựu chức", "động từ", "nhận chức, nhận việc", "他下个月正式就职。", "Tháng sau anh ấy chính thức nhận chức.",
     "Động từ ly hợp, nghĩa là chính thức nhận chức, bắt đầu nhận việc. Hay gặp: 就职典礼, lễ nhậm chức. Trái nghĩa với 辞职, từ chức, nghỉ việc."),
    ("边缘", "biānyuán", "biên duyên", "danh từ", "rìa, vùng ven, bên lề", "他们住在城市的边缘。", "Họ sống ở vùng ven thành phố.",
     "Danh từ, nghĩa là mép, rìa, vùng giáp ranh. Trong bài có cụm 被边缘化, bị gạt ra rìa, bị cho ra lề, tức là không ai để ý đến mình."),
    ("眼色", "yǎnsè", "nhãn sắc", "danh từ", "cái nháy mắt ra hiệu, cái liếc mắt đầy ngụ ý", "他向我使了个眼色，让我别说话。", "Anh ấy nháy mắt ra hiệu bảo tôi đừng nói.",
     "Danh từ. Cẩn thận: không phải là màu mắt. 眼色 là ánh mắt dùng để ra hiệu, ngầm báo cho người khác. Động từ đi kèm là 使: 使眼色, nháy mắt ra hiệu. Ngoài ra, 看眼色 là nhìn sắc mặt người khác mà hành động."),
    ("指标", "zhǐbiāo", "chỉ tiêu", "danh từ", "chỉ tiêu", "这个月的销售指标已经完成了。", "Chỉ tiêu bán hàng tháng này đã hoàn thành rồi.",
     "Danh từ, nghĩa là chỉ tiêu, mức phải đạt được, âm Hán Việt và nghĩa giống hệt tiếng Việt. Trong bài, 完不成指标 là không hoàn thành được chỉ tiêu."),
    ("成天", "chéngtiān", "thành thiên", "phó từ", "suốt ngày", "他成天玩儿手机，不学习。", "Cậu ấy suốt ngày chơi điện thoại, chẳng học hành.",
     "Phó từ, khẩu ngữ, nghĩa là suốt ngày, cả ngày, giống 整天, thường mang ý chê trách. Trong bài, 几乎成天聊天儿 là gần như suốt ngày tán gẫu."),
    ("吹牛", "chuī niú", "xuy ngưu", "động từ", "ba hoa, khoác lác", "别吹牛了，你根本做不到。", "Đừng khoác lác nữa, cậu căn bản không làm được đâu.",
     "Động từ ly hợp. Nghĩa đen là thổi trâu, nghĩa bóng là ba hoa, nói khoác. Cũng nói 吹牛皮. Đây là cách nói khẩu ngữ rất thông dụng."),
    ("溜", "liū", "lựu", "động từ", "chuồn mất, lẻn đi", "会还没开完，他就偷偷溜走了。", "Cuộc họp chưa xong, anh ta đã lén chuồn mất.",
     "Động từ, nghĩa là lén lút bỏ đi, chuồn đi mà không để ai biết. Trong bài, 溜出去逛街 là lẻn ra ngoài đi dạo phố trong giờ làm."),
    ("等级", "děngjí", "đẳng cấp", "danh từ", "đẳng cấp, cấp bậc", "这家酒店的等级很高。", "Khách sạn này có đẳng cấp rất cao.",
     "Danh từ, nghĩa là cấp bậc, thứ hạng. Trong bài, 根本就不是一个等级 là căn bản không cùng một cấp độ, ý nói việc của người mới khó hơn nhiều."),
    ("公道", "gōngdao", "công đạo", "danh từ", "sự công bằng, lẽ phải", "这件事我一定要讨个公道。", "Chuyện này tôi nhất định phải đòi lại công bằng.",
     "Danh từ, nghĩa là lẽ phải, sự công bằng. Cụm hay gặp là 讨公道, đòi lẽ phải, đòi công bằng. Khi làm tính từ, 公道 nghĩa là hợp lý, phải chăng, như 价钱公道, giá cả phải chăng."),
    ("哼", "hng", "hanh", "thán từ", "hừ, hừm (bực bội hoặc không tin)", "哼，我才不信他的话呢！", "Hừ, tôi chẳng tin lời anh ta đâu!",
     "Thán từ, dùng để biểu thị sự bực bội, khinh thường, hoặc không tin. Khi là thán từ, nó được phát âm bằng giọng mũi, ghi là hng. Trong bài, Tiểu Lâm bực tức nói: 哼，太不像话了."),
    ("不像话", "bú xiàng huà", "bất tượng thoại", "tính từ", "vô lý, kỳ cục, chẳng ra sao", "他这样对待父母，真不像话！", "Anh ta đối xử với bố mẹ như vậy, thật chẳng ra sao!",
     "Tính từ, khẩu ngữ. Nghĩa đen là không ra lời nói, nghĩa thật là lời nói hay việc làm vô lý, quá đáng, chẳng ra thể thống gì. Thường đi với 太，真: 太不像话了."),
    ("明明", "míngmíng", "minh minh", "phó từ", "rõ ràng", "他明明知道，却说不知道。", "Anh ta rõ ràng biết, vậy mà lại nói không biết.",
     "Phó từ, nghĩa là rõ ràng, rành rành. Đây là điểm ngữ pháp thứ hai của bài."),
    ("欺负", "qīfu", "khi phụ", "động từ", "ăn hiếp, bắt nạt", "大孩子不应该欺负小孩子。", "Trẻ lớn không nên bắt nạt trẻ nhỏ.",
     "Động từ, nghĩa là ăn hiếp, bắt nạt, ức hiếp người yếu hơn. Âm tiết thứ hai đọc nhẹ. Trong bài, 明明是在欺负人 là rõ ràng là đang bắt nạt người ta."),
    ("大不了", "dàbuliǎo", "đại bất liễu", "phó từ", "cùng lắm, trong trường hợp xấu nhất", "大不了再做一遍。", "Cùng lắm thì làm lại một lần nữa.",
     "Phó từ, nghĩa là cùng lắm thì, xấu nhất cũng chỉ đến thế. Chú ý âm cuối đọc là liǎo, không đọc là le. Đây là điểm ngữ pháp thứ ba của bài."),
    ("展示", "zhǎnshì", "triển thị", "động từ", "thể hiện, trưng bày", "这次比赛是展示自己的好机会。", "Cuộc thi lần này là cơ hội tốt để thể hiện bản thân.",
     "Động từ, nghĩa là bày ra cho người khác thấy, thể hiện. Hay gặp: 展示才能, thể hiện tài năng; 展示产品, trưng bày sản phẩm."),
    ("才干", "cáigàn", "tài cán", "danh từ", "tài năng, năng lực", "他是一个很有才干的年轻人。", "Anh ấy là một người trẻ rất có năng lực.",
     "Danh từ, nghĩa là tài năng, năng lực làm việc. Tiếng Việt cũng có từ tài cán với nghĩa tương tự. Âm tiết thứ hai đọc thanh bốn. Trong bài, 展示自己才干的好机会 là cơ hội tốt để thể hiện năng lực của mình."),
    ("计较", "jìjiào", "kế giảo", "động từ", "tính toán, so đo", "他从来不计较个人得失。", "Anh ấy chưa bao giờ so đo được mất cá nhân.",
     "Động từ. Cẩn thận: không phải tính toán sổ sách. 计较 là so đo, chấp nhặt hơn thiệt, thường dùng ở dạng phủ định. Trong bài, 不和他们计较 là không chấp nhặt với họ."),
    ("全力以赴", "quánlìyǐfù", "toàn lực dĩ phó", "thành ngữ", "dốc toàn lực, không tiếc công sức", "我们会全力以赴完成任务。", "Chúng tôi sẽ dốc toàn lực hoàn thành nhiệm vụ.",
     "Thành ngữ. 全力 là toàn bộ sức lực, 赴 là lao vào, dấn thân vào. Nghĩa là dồn hết sức lực vào một việc. Trong bài, 全力以赴投入工作 là dốc toàn lực lao vào công việc."),
    ("怠慢", "dàimàn", "đãi mạn", "động từ", "lạnh nhạt, thờ ơ", "客人来了，千万不能怠慢。", "Khách đến rồi, tuyệt đối không được tiếp đãi lạnh nhạt.",
     "Động từ, nghĩa là đối xử lạnh nhạt, thờ ơ, không chu đáo. Cẩn thận: chữ đãi ở đây nghĩa là lười nhác, khác với chữ đãi trong 接待. Người Trung Quốc hay nói khách sáo: 怠慢了, tức là đã tiếp đãi không chu đáo."),
    ("敷衍", "fūyǎn", "phu diễn", "động từ", "làm lấy lệ, làm qua loa, hời hợt", "你别敷衍我，说实话吧。", "Anh đừng nói cho qua chuyện với tôi, nói thật đi.",
     "Động từ, nghĩa là làm cho có, làm lấy lệ, đối phó cho qua chuyện. Trong bài, 不敷衍每一位客户 là không đối phó qua loa với bất kỳ khách hàng nào."),
    ("想方设法", "xiǎngfāng-shèfǎ", "tưởng phương thiết pháp", "thành ngữ", "nghĩ đủ mọi cách", "父母想方设法让孩子吃得健康。", "Bố mẹ nghĩ đủ mọi cách để con ăn uống lành mạnh.",
     "Thành ngữ, nghĩa là nghĩ đủ mọi cách, tìm mọi biện pháp. Nghĩa gần giống thành ngữ 千方百计."),
    ("凑合", "còuhe", "thấu hợp", "động từ", "làm qua quýt, miễn cưỡng; tạm bợ", "这件衣服虽然旧了，还能凑合着穿。", "Bộ quần áo này tuy cũ rồi, vẫn mặc tạm được.",
     "Động từ, khẩu ngữ, âm tiết thứ hai đọc nhẹ. Nghĩa thường gặp là tạm bợ, tạm chấp nhận dù chưa tốt. Trong bài, 多忙都不凑合 là dù bận đến mấy cũng không làm qua quýt, không làm cho có."),
    ("忙碌", "mánglù", "mang lục", "tính từ", "bận rộn", "他每天都过着忙碌的生活。", "Ngày nào anh ấy cũng sống trong bận rộn.",
     "Tính từ, nghĩa là bận rộn, tất bật, mang sắc thái văn viết hơn 忙. Trong bài, 忙碌中，时光过得飞快, trong bận rộn, thời gian trôi nhanh như bay."),
    ("时光", "shíguāng", "thời quang", "danh từ", "thời gian, quãng thời gian", "大学时光是最美好的。", "Quãng thời gian đại học là đẹp nhất.",
     "Danh từ, chỉ thời gian, năm tháng, mang màu sắc văn chương. Hay gặp: 美好时光, quãng thời gian tươi đẹp."),
    ("飞跃", "fēiyuè", "phi dược", "động từ", "vượt bậc, nhảy vọt", "这几年，中国的科技有了飞跃的发展。", "Mấy năm nay, khoa học kỹ thuật Trung Quốc phát triển vượt bậc.",
     "Động từ, nghĩa đen là bay vọt lên, nghĩa bóng là tiến bộ vượt bậc. Trong bài, 飞跃式的提高 là sự nâng cao kiểu nhảy vọt, như ta đã gặp ở phần khởi động."),
    ("投诉", "tóusù", "đầu tố", "động từ", "khiếu nại", "顾客投诉了这家餐厅的服务。", "Khách hàng đã khiếu nại dịch vụ của nhà hàng này.",
     "Động từ, nghĩa là khiếu nại, phàn nàn với cơ quan hay cấp trên có thẩm quyền. Trong bài, 客户投诉赵姐了, khách hàng khiếu nại chị Triệu rồi."),
    ("激情", "jīqíng", "kích tình", "danh từ", "tình cảm mãnh liệt, nhiệt huyết", "年轻人对工作充满激情。", "Người trẻ tràn đầy nhiệt huyết với công việc.",
     "Danh từ, chỉ tình cảm mãnh liệt, cảm xúc mạnh mẽ, sự nhiệt huyết. Trong bài, 充满激情地工作 là làm việc tràn đầy nhiệt huyết. Từ này mang nghĩa tích cực, các bạn đừng hiểu lệch sang nghĩa tình cảm nam nữ nhé."),
    ("年度", "niándù", "niên độ", "danh từ", "hằng năm; năm (theo kế hoạch)", "公司每年都举行年度总结大会。", "Năm nào công ty cũng tổ chức hội nghị tổng kết năm.",
     "Danh từ, chỉ một năm tính theo kế hoạch công việc hay tài chính. Hay gặp: 年度考核, đánh giá cuối năm; 年度计划, kế hoạch năm."),
    ("考核", "kǎohé", "khảo hạch", "động từ", "kiểm tra, đánh giá", "新员工要通过考核才能转正。", "Nhân viên mới phải qua đánh giá mới được vào chính thức.",
     "Động từ, nghĩa là kiểm tra, đánh giá năng lực và thành tích làm việc. Ở công sở, 年度考核 là đợt đánh giá nhân viên cuối năm."),
    ("敬业", "jìngyè", "kính nghiệp", "động từ", "yêu nghề, cống hiến cho công việc", "他是一位非常敬业的医生。", "Ông ấy là một bác sĩ vô cùng tận tụy với nghề.",
     "Nghĩa là tận tụy, hết lòng với nghề nghiệp của mình. Hay gặp: 敬业精神, tinh thần tận tụy với nghề."),
    ("兢兢业业", "jīngjīngyèyè", "căng căng nghiệp nghiệp", "tính từ", "thận trọng tỉ mỉ, cần mẫn", "她兢兢业业地工作了三十年。", "Bà ấy đã cần mẫn làm việc suốt ba mươi năm.",
     "Tính từ, nghĩa là cẩn thận, chăm chỉ, tận tụy trong công việc. Trong bài, 兢兢业业的工作态度 là thái độ làm việc cần mẫn, tận tụy."),
    ("回报", "huíbào", "hồi báo", "động từ", "đền đáp", "我一定要好好工作，回报父母。", "Tôi nhất định phải làm việc thật tốt để đền đáp cha mẹ.",
     "Động từ, nghĩa là đền đáp, báo đáp; cũng làm danh từ, nghĩa là sự đền đáp, thành quả xứng đáng. Trong bài, 得到了丰厚的回报 là nhận được sự đền đáp hậu hĩnh."),
    ("当初", "dāngchū", "đương sơ", "danh từ", "lúc đầu, trước đây", "当初我也不同意这个计划。", "Lúc đầu tôi cũng không đồng ý kế hoạch này.",
     "Danh từ, nghĩa là lúc đầu, hồi ấy, chỉ thời điểm khi sự việc mới bắt đầu. Trong bài, 当初对我们不友好的资深前辈们, những tiền bối lúc đầu không thân thiện với chúng tôi."),
    ("技巧", "jìqiǎo", "kỹ xảo", "danh từ", "kỹ năng, kỹ xảo", "学习也需要讲究技巧。", "Học tập cũng cần chú ý đến kỹ năng.",
     "Danh từ, nghĩa là kỹ năng, mẹo, cách làm khéo léo. Trong bài, 工作经验和技巧 là kinh nghiệm và kỹ năng làm việc."),
    ("传授", "chuánshòu", "truyền thụ", "động từ", "truyền dạy, truyền đạt", "老师把自己的经验传授给学生。", "Thầy truyền dạy kinh nghiệm của mình cho học trò.",
     "Động từ, nghĩa là truyền dạy kiến thức, kỹ năng cho người khác. Thường dùng theo mẫu 把什么传授给某人."),
    ("人格", "réngé", "nhân cách", "danh từ", "nhân cách, tính cách", "我们应该尊重每个人的人格。", "Chúng ta nên tôn trọng nhân cách của mỗi người.",
     "Danh từ, nghĩa là nhân cách, phẩm chất con người. Trong bài, 人格魅力 là sức hút của nhân cách, sức hấp dẫn toát ra từ phẩm chất của một người."),
    ("施展", "shīzhǎn", "thi triển", "động từ", "phát huy, thi thố", "这份工作让他有机会施展才能。", "Công việc này cho anh ấy cơ hội phát huy tài năng.",
     "Động từ, nghĩa là phát huy, thi thố tài năng, bản lĩnh. Thường đi với 才能，才华，本领."),
    ("时机", "shíjī", "thời cơ", "danh từ", "cơ hội, thời cơ", "我们要抓住时机，不能犹豫。", "Chúng ta phải nắm bắt thời cơ, không được do dự.",
     "Danh từ, nghĩa là thời cơ, thời điểm thích hợp. Câu cuối bài khóa: 也是你施展才能的时机, cũng là thời cơ để bạn phát huy tài năng."),
]

add("bullets", chapter="Từ mới (46 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 6 có 46 từ mới, chia thành 16 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 搭档 (dàng) · 大不了 (liǎo) · 才干 (gàn) · 欺负 (fu) · 凑合 (he)",
           "Từ dễ nhầm: 风气 · 眼色 · 计较 · 怠慢 · 激情"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có bốn mươi sáu từ, thầy chia thành mười sáu nhóm nhỏ, mỗi nhóm hai hoặc ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số từ có âm đọc cần chú ý, như 搭档，大不了，才干，欺负，凑合. Thầy sẽ nhắc khi gặp."),
         F(4, "Ngoài ra, có mấy từ Hán Việt rất dễ hiểu nhầm, như 风气，眼色，计较，怠慢，激情. Nghĩa của chúng trong tiếng Trung khác với cách hiểu thông thường của người Việt, các bạn nhớ nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

sizes = [3] * 14 + [2] * 2
assert sum(sizes) == len(V)
g = 0
for gs in sizes:
    group = V[g:g + gs]
    words, say = [], []
    for i, (zh, py, hv, loai, vi, ex, exvi, expl) in enumerate(group):
        n = g + i + 1
        words.append({"zh": zh, "py": py, "hv": hv.upper(), "loai": f"{n}. {loai}", "vi": vi, "ex": ex, "exvi": exvi})
        say.append(F(i, f"Từ số {n}: {zh}。 {zh}。 Hán Việt là {hv}.", zr=120))
        say.append(F(i, f"{expl} Ví dụ: {ex}{'' if ex[-1] in '。…？！，' else '，'} {exvi[0].upper() + exvi[1:]}{'' if exvi.endswith(('.', '!', '?')) else '.'}", zr=130))
    add("vocab", section="Từ mới 生词", title=f"Từ mới ({g + 1}–{g + len(group)} / {len(V)})",
        words=words, say=say)
    g += gs

# ======================= BÀI KHÓA =======================
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung nếu khác])
P = [
    ("这天是我到这家公司上任的第一天，我的职位是咨询师。早就听说这里老手多、新手少，不少资深员工在公司创立之初就开始在这里工作了。",
     "Hôm nay là ngày đầu tiên tôi đến nhận chức ở công ty này, chức vụ của tôi là chuyên viên tư vấn. Từ lâu tôi đã nghe nói ở đây người lâu năm nhiều, người mới ít, không ít nhân viên kỳ cựu đã làm việc ở đây ngay từ lúc công ty mới thành lập.",
     ["咨询师 là chuyên viên tư vấn. 早就听说 là từ lâu đã nghe nói.",
      "老手 là người lâu năm, thạo việc; 新手 là người mới. 之初 là lúc ban đầu, văn viết: 在公司创立之初, ngay từ khi công ty mới thành lập."]),
    ("清早上班，和新同事一一认识后，我以为一天的工作就此开始，没想到赵姐工作的第一件事是忙着沏茶和咖啡，给张哥端一碗，给孙姐送一杯……",
     "Sáng sớm đi làm, sau khi lần lượt làm quen với các đồng nghiệp mới, tôi tưởng rằng công việc của một ngày bắt đầu từ đây, không ngờ việc đầu tiên của chị Triệu là tất bật pha trà và cà phê, bưng cho anh Trương một bát, mang cho chị Tôn một cốc…",
     ["一一 là lần lượt từng người một. 就此 là từ đây, văn viết. 以为……没想到…… là tưởng rằng…, không ngờ…, đây là mẫu câu của bài tập bốn.",
      "赵姐，张哥，孙姐 là cách gọi thân mật nơi công sở: họ cộng với 姐 hoặc 哥, như chị Triệu, anh Trương, chị Tôn. 端 là bưng bằng hai tay."]),
    ("我想这单位风气真好，明天这事我来做。正想着，赵姐已经坐在那儿开始自己享受，唯独剩下我和我的搭档——与我同一天就职的小林。",
     "Tôi nghĩ cơ quan này có nếp sống thật tốt, ngày mai việc này để tôi làm. Đang nghĩ vậy thì chị Triệu đã ngồi xuống bắt đầu tự thưởng thức, chỉ còn lại tôi và cộng sự của tôi, Tiểu Lâm, người nhận việc cùng ngày với tôi.",
     ["Nhân vật tôi tưởng mọi người ở đây quan tâm nhau, nên định ngày mai mình sẽ pha trà. 正想着 là đang nghĩ như vậy thì…",
      "唯独剩下我和我的搭档 là chỉ còn lại tôi và cộng sự của tôi, tức là hai người mới không được mời. Dấu gạch ngang dài dùng để giải thích: cộng sự đó chính là Tiểu Lâm."],
     "我想这单位风气真好，明天这事我来做。正想着，赵姐已经坐在那儿开始自己享受，唯独剩下我和我的搭档，与我同一天就职的小林。"),
    ("顿时小林的脸色变了，我也有被边缘化的感觉，不过我还是向小林使了个眼色。屋子里鸦雀无声，第一天就这样开始了。",
     "Ngay lập tức sắc mặt Tiểu Lâm thay đổi, tôi cũng có cảm giác bị gạt ra rìa, nhưng tôi vẫn nháy mắt ra hiệu cho Tiểu Lâm. Trong phòng im phăng phắc, ngày đầu tiên cứ thế bắt đầu.",
     ["顿时 là ngay lập tức. 被边缘化 là bị gạt ra rìa. 向小林使了个眼色 là nháy mắt ra hiệu cho Tiểu Lâm, ý bảo bạn hãy bình tĩnh.",
      "鸦雀无声 là thành ngữ, nghĩa đen là không có cả tiếng quạ, tiếng chim sẻ, tức là im phăng phắc."]),
    ("我和小林的业务很难做，件件都让人头痛，有时候还完不成指标，可别人的工作很快就完了，几乎成天聊天儿、上网、吹牛，还有人溜出去逛街。我和小林虽然是新来的，可我们之前在别的公司也是好手呀。",
     "Công việc của tôi và Tiểu Lâm rất khó làm, việc nào cũng khiến người ta đau đầu, có lúc còn không hoàn thành được chỉ tiêu, nhưng công việc của người khác thì xong rất nhanh, gần như suốt ngày tán gẫu, lên mạng, khoác lác, còn có người lẻn ra ngoài dạo phố. Tôi và Tiểu Lâm tuy là người mới, nhưng trước đây ở công ty khác chúng tôi cũng là những tay giỏi đấy.",
     ["件件都让人头痛 là việc nào cũng khiến người ta đau đầu. 完不成指标 là không hoàn thành được chỉ tiêu. 可 ở đây là nhưng.",
      "成天聊天儿、上网、吹牛 là suốt ngày tán gẫu, lên mạng, khoác lác. 好手 là tay giỏi. Câu 也是好手呀 thể hiện chút ấm ức của nhân vật tôi."]),
    ("后来我发现，领导分配业务时，总是让资深员工先挑，他们挑剩下的才是我和小林的。我们的工作从难度上讲，和他们根本就不是一个等级。",
     "Sau đó tôi phát hiện ra, khi lãnh đạo phân công công việc, luôn để nhân viên lâu năm chọn trước, những việc họ chọn còn thừa lại mới là của tôi và Tiểu Lâm. Công việc của chúng tôi xét về độ khó, căn bản không cùng một cấp độ với họ.",
     ["分配业务 là phân công công việc. 先挑 là chọn trước. 挑剩下的 là những thứ chọn xong còn thừa lại.",
      "从……上讲 là xét về mặt…: 从难度上讲, xét về độ khó. 根本就不是一个等级 là hoàn toàn không cùng một cấp độ."]),
    ("小林要去找领导讨公道：“哼，太不像话了，明明是在欺负人，大不了辞职。”",
     "Tiểu Lâm định đi tìm lãnh đạo đòi lẽ phải: Hừ, thật quá đáng, rõ ràng là đang bắt nạt người ta, cùng lắm thì nghỉ việc.",
     ["讨公道 là đòi lẽ phải, đòi công bằng. 太不像话了 là thật quá đáng, chẳng ra sao cả.",
      "Câu này chứa hai điểm ngữ pháp: 明明是在欺负人, rõ ràng là đang bắt nạt người ta; và 大不了辞职, cùng lắm thì nghỉ việc. Lát nữa chúng ta sẽ học kỹ."],
     "小林要去找领导讨公道：哼，太不像话了，明明是在欺负人，大不了辞职。"),
    ("我也觉得不像话，可静下来，也觉得没什么不好，应该说这反而是我们可以展示自己才干的好机会。",
     "Tôi cũng thấy thật quá đáng, nhưng bình tĩnh lại, tôi lại thấy cũng chẳng có gì không tốt, phải nói rằng đây trái lại là cơ hội tốt để chúng tôi thể hiện năng lực của mình.",
     ["静下来 là bình tĩnh lại. 应该说 là phải nói rằng, có thể nói rằng.",
      "反而 là trái lại, ngược lại: tưởng là chuyện xấu, hóa ra lại là cơ hội tốt. Đây là bước ngoặt trong suy nghĩ của nhân vật tôi."]),
    ("我和小林决定不和他们计较，全力以赴投入工作，不怠慢、不敷衍每一位客户，想方设法做好每一单业务，多忙都不凑合。",
     "Tôi và Tiểu Lâm quyết định không so đo với họ, dốc toàn lực lao vào công việc, không lạnh nhạt, không qua loa với bất kỳ khách hàng nào, nghĩ đủ mọi cách để làm tốt từng đơn hàng, bận đến mấy cũng không làm qua quýt.",
     ["不和他们计较 là không so đo với họ. 全力以赴投入工作 là dốc toàn lực lao vào công việc. 一单业务 là một đơn hàng, một vụ việc.",
      "Chú ý chuỗi phủ định: 不怠慢，不敷衍，多忙都不凑合. Cấu trúc này nghĩa là dù… đến mấy cũng…: 多忙都不凑合, bận đến mấy cũng không làm cho có; tương tự, 多累都不怕, mệt đến mấy cũng không sợ."]),
    ("忙碌中，时光过得飞快，我们的业务能力得到了飞跃式的提高，点名找我们的客户越来越多。",
     "Trong bận rộn, thời gian trôi nhanh như bay, năng lực nghiệp vụ của chúng tôi được nâng cao vượt bậc, khách hàng chỉ đích danh tìm chúng tôi ngày càng nhiều.",
     ["时光过得飞快 là thời gian trôi nhanh như bay. 飞跃式的提高 là sự nâng cao kiểu nhảy vọt, tức là tiến bộ vượt bậc.",
      "点名 là gọi tên, chỉ đích danh. 点名找我们的客户 là những khách hàng chỉ đích danh muốn chúng tôi phục vụ, chứng tỏ họ rất tin tưởng."]),
    ("有时领导会说，服务对象对张哥不满意，活儿你们接手吧；客户投诉赵姐了，你们处理一下吧。我们每天都充满激情地工作，享受着工作的快乐。",
     "Có khi lãnh đạo nói: khách hàng không hài lòng với anh Trương, việc này các cậu nhận lấy đi; khách hàng khiếu nại chị Triệu rồi, các cậu xử lý một chút nhé. Chúng tôi ngày nào cũng làm việc tràn đầy nhiệt huyết, tận hưởng niềm vui của công việc.",
     ["服务对象 là đối tượng phục vụ, tức là khách hàng. 活儿 là công việc, khẩu ngữ. 接手 là tiếp nhận công việc từ người khác.",
      "Tình thế đã đảo ngược: việc người cũ làm không tốt lại được giao cho hai người mới. 充满激情地工作 là làm việc tràn đầy nhiệt huyết."]),
    ("年度考核，我和小林的敬业精神、兢兢业业的工作态度受到了表扬，经济上也得到了丰厚的回报。当初对我们不友好的资深前辈们也变得热情起来。",
     "Trong đợt đánh giá cuối năm, tinh thần tận tụy và thái độ làm việc cần mẫn của tôi và Tiểu Lâm được khen ngợi, về mặt kinh tế cũng nhận được sự đền đáp hậu hĩnh. Những tiền bối lâu năm lúc đầu không thân thiện với chúng tôi cũng trở nên nhiệt tình.",
     ["年度考核 là đánh giá cuối năm. 受到了表扬 là được khen ngợi. 经济上 là về mặt kinh tế. 丰厚的回报 là sự đền đáp hậu hĩnh.",
      "前辈 là tiền bối, người đi trước. 变得热情起来 là trở nên nhiệt tình; 起来 chỉ trạng thái bắt đầu và tiếp diễn."]),
    ("再后来，公司来了新人，领导让我带他们，我把工作经验和技巧传授给他们，毫无保留。",
     "Về sau nữa, công ty có người mới đến, lãnh đạo bảo tôi kèm cặp họ, tôi truyền dạy kinh nghiệm và kỹ năng làm việc cho họ, không giữ lại chút nào.",
     ["领导让我带他们 là lãnh đạo bảo tôi kèm cặp họ. 把工作经验和技巧传授给他们 là truyền dạy kinh nghiệm và kỹ năng làm việc cho họ.",
      "毫无保留 là không giữ lại chút nào. Các bạn thấy không, nhân vật tôi không đối xử với người mới như cách mình từng bị đối xử."]),
    ("其实，进入新单位，作为一个职场插班生，这个过程，正是展示你人格魅力的时候，遇到困难，也是你施展才能的时机。",
     "Thật ra, bước vào một cơ quan mới, với tư cách là một người mới chen chân vào chốn công sở, quá trình này chính là lúc thể hiện sức hút nhân cách của bạn; gặp khó khăn, cũng là thời cơ để bạn phát huy tài năng.",
     ["作为 là với tư cách là. 职场插班生 là người mới vào làm giữa chừng, giống như học sinh vào lớp khi lớp đã học được một thời gian.",
      "正是……的时候 là chính là lúc…. Câu kết nêu chủ đề của bài: khó khăn khi mới vào nghề cũng là thời cơ để phát huy tài năng. Đây là mẫu câu thứ hai của bài tập bốn."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 当好职场插班生", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 当好职场插班生, dài bảy trăm tám mươi lăm chữ. Bài được cải biên từ một bài báo cùng tên trên báo Thanh niên Bắc Kinh, tác giả là Tô Tiểu Ni.",
         F(0, "Thầy chia bài thành mười bốn đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
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
    items=["## 1. “我”的职位以及公司的人员构成",
           "咨询师 · 老手多、新手少 · 资深员工在公司创立之初就在这里工作",
           "## 2. 上班第一天，老员工对“我”和小林的态度",
           "赵姐给张哥、孙姐沏茶/咖啡 · 唯独剩下“我”和小林 · 被边缘化",
           "## 3. “我”和小林的工作与别人有何不同？为什么？",
           "业务难做，件件头痛，完不成指标 · 别人成天聊天、吹牛 · 资深员工先挑，挑剩下的才给我们"],
    say=["Bài tập năm của sách yêu cầu dựa vào gợi ý để tóm tắt nội dung chính của bài khóa. Chúng ta cùng làm luôn nhé. Có sáu câu hỏi, thầy chia làm hai phần.",
         F(0, "Câu hỏi một: hãy nói về chức vụ của nhân vật tôi ở công ty này, và thành phần nhân sự của công ty."),
         F(1, "Nhân vật tôi là 咨询师, chuyên viên tư vấn. Công ty thì 老手多、新手少, người lâu năm nhiều, người mới ít, nhiều nhân viên kỳ cựu đã làm ở đây từ ngày công ty mới thành lập."),
         F(2, "Câu hỏi hai: ngày đầu đi làm, các nhân viên cũ có thái độ thế nào với nhân vật tôi và Tiểu Lâm?"),
         F(3, "Chị Triệu pha trà, pha cà phê cho anh Trương, chị Tôn, 唯独剩下我和小林, chỉ bỏ lại hai người mới. Hai người có cảm giác bị gạt ra rìa."),
         F(4, "Câu hỏi ba: công việc của nhân vật tôi và Tiểu Lâm khác người khác thế nào, vì sao?"),
         F(5, "Việc của họ rất khó, việc nào cũng đau đầu, có lúc không đạt chỉ tiêu; còn người khác thì suốt ngày tán gẫu, khoác lác. Lý do là khi phân công, lãnh đạo để nhân viên lâu năm chọn trước, việc thừa lại mới đến lượt người mới.")])

add("bullets", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5) – phần 2", size=34,
    items=["## 4. “我”和小林如何对待自己的工作？",
           "不计较、全力以赴、不怠慢、不敷衍、想方设法、不凑合",
           "## 5. “我们”在公司的处境有了什么变化？",
           "业务能力飞跃式提高 · 客户点名 · 接手老员工的活儿 · 年度考核受表扬 · 前辈热情起来 · 带新人",
           "## 6. 通过“职场插班生”的经历，“我”有什么收获？",
           "展示人格魅力 · 施展才能"],
    say=[F(0, "Câu hỏi bốn: nhân vật tôi và Tiểu Lâm đối xử với công việc của mình như thế nào?"),
         F(1, "Sáu cụm từ gợi ý: 不计较，全力以赴，不怠慢，不敷衍，想方设法，不凑合. Không so đo, dốc toàn lực, không lạnh nhạt, không qua loa, nghĩ đủ mọi cách, và không làm cho có."),
         F(2, "Câu hỏi năm: hoàn cảnh của chúng tôi ở công ty đã thay đổi thế nào?"),
         F(3, "Năng lực nghiệp vụ tiến bộ vượt bậc, khách hàng chỉ đích danh tìm đến, được giao tiếp nhận việc của nhân viên cũ, đánh giá cuối năm được khen ngợi, các tiền bối trở nên nhiệt tình, và nhân vật tôi còn được giao kèm cặp người mới."),
         F(4, "Câu hỏi sáu: qua trải nghiệm làm người mới nơi công sở, nhân vật tôi thu hoạch được gì?"),
         F(5, "Đó là 展示人格魅力, thể hiện sức hút nhân cách, và 施展才能, phát huy tài năng. Bố cục này rất có ích khi các bạn tự kể lại bài khóa.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 唯独", section="Ngữ pháp 注释", title="1. 唯独 wéidú – chỉ có, duy chỉ", size=38,
    items=["Phó từ, nghĩa là 只是、单单 – chỉ, riêng chỉ",
           "Vế trước thường nêu nội dung đối lập: số đông thế này, riêng một đối tượng thế kia",
           "那次旅行大家都去了，唯独你没有去成。",
           "中国的传统节日都是喜气洋洋的，唯独清明节，庄严而伤感。",
           "正想着，赵姐已经坐在那儿开始自己享受，唯独剩下我和我的搭档——与我同一天就职的小林。"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là phó từ 唯独.",
         F(0, "唯独 là phó từ, nghĩa giống 只是 và 单单, tiếng Việt dịch là chỉ có, duy chỉ, riêng chỉ."),
         F(1, "Phía trước 唯独 thường có một nội dung đối lập: số đông thì thế này, riêng một đối tượng lại thế kia. Vì vậy câu có 唯独 thường có hai vế, vế trước nói chung, vế sau tách riêng một trường hợp."),
         F(2, "Ví dụ một: 那次旅行大家都去了，唯独你没有去成。 Chuyến du lịch lần đó mọi người đều đi, chỉ có bạn là không đi được."),
         F(3, "Ví dụ hai: 中国的传统节日都是喜气洋洋的，唯独清明节，庄严而伤感。 Các ngày lễ truyền thống của Trung Quốc đều vui tươi rộn rã, riêng chỉ có Tết Thanh minh là trang nghiêm và buồn thương."),
         F(4, "Ví dụ ba, lấy từ bài khóa: 正想着，赵姐已经坐在那儿开始自己享受，唯独剩下我和我的搭档，与我同一天就职的小林。 Mọi người đều có trà, chỉ còn lại tôi và cộng sự của tôi.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: hoàn thành câu với 唯独", reveal=True, size=36,
    items=["(1) 我上学的时候，哪门功课都好，……",
           "Đáp án: ……唯独体育不太好。",
           "(2) 说理、鼓励、引导、表扬，什么样的教育方式都可以尝试，……",
           "Đáp án: ……唯独打骂孩子不行。",
           "(3) 他对什么都不在意，……，他格外用心。",
           "Đáp án: ……唯独对孩子的学习，他格外用心。"],
    say=[F(0, "Luyện tập: dùng 唯独 hoàn thành câu. Câu một: 我上学的时候，哪门功课都好，…… Hồi đi học, môn nào tôi cũng giỏi, nhưng sao? Các bạn tạm dừng và thử hoàn thành câu nhé."),
         F(1, "Đáp án gợi ý: 唯独体育不太好。 Chỉ có môn thể dục là không giỏi lắm. Vế trước nói môn nào cũng giỏi, vế sau tách riêng một môn."),
         F(2, "Câu hai: 说理、鼓励、引导、表扬，什么样的教育方式都可以尝试，…… Giảng giải, động viên, hướng dẫn, khen ngợi, cách giáo dục nào cũng có thể thử."),
         F(3, "Đáp án gợi ý: 唯独打骂孩子不行。 Chỉ có đánh mắng con là không được."),
         F(4, "Câu ba: 他对什么都不在意，……，他格外用心。 Anh ấy chẳng để tâm đến chuyện gì, chỉ có… là anh ấy đặc biệt chú tâm."),
         F(5, "Đáp án gợi ý: 唯独对孩子的学习，他格外用心。 Chỉ có việc học của con là anh ấy đặc biệt chú tâm.")])

add("bullets", chapter="Ngữ pháp: 明明", section="Ngữ pháp 注释", title="2. 明明 míngmíng – rõ ràng, rành rành", size=38,
    items=["Phó từ: biểu thị rất rõ ràng, sự thật đúng là như vậy",
           "Trước hoặc sau vế có 明明 thường có câu hỏi ngược hoặc vế chuyển ý · dùng nhiều trong khẩu ngữ",
           "你唱的明明是流行歌曲，哪里是京剧啊？",
           "明明是你把书弄丢了，还说不知道，真不像话！",
           "哼，太不像话了，明明是在欺负人。"],
    say=["Điểm ngữ pháp thứ hai là phó từ 明明.",
         F(0, "明明 biểu thị một điều rất rõ ràng, sự thật đúng là như vậy, tiếng Việt dịch là rõ ràng, rành rành."),
         F(1, "Trước hoặc sau vế câu có 明明, thường có một câu hỏi ngược, hoặc một vế chuyển ý, để phản bác lại điều trái với sự thật đó. Từ này dùng nhiều trong khẩu ngữ, thường mang giọng trách móc, bất mãn."),
         F(2, "Ví dụ một: 你唱的明明是流行歌曲，哪里是京剧啊？ Cái bạn hát rõ ràng là nhạc thịnh hành, kinh kịch ở chỗ nào chứ? Phía sau là câu hỏi ngược."),
         F(3, "Ví dụ hai: 明明是你把书弄丢了，还说不知道，真不像话！ Rõ ràng là cậu làm mất sách, vậy mà còn nói không biết, thật chẳng ra sao! Phía sau là vế chuyển ý 还说不知道."),
         F(4, "Ví dụ ba, lấy từ bài khóa: 哼，太不像话了，明明是在欺负人。 Hừ, thật quá đáng, rõ ràng là đang bắt nạt người ta.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: hoàn thành câu với 明明", reveal=True, size=36,
    items=["(1) ……，却不承认，真不讲理！",
           "Đáp án: 明明是他打破了杯子，却不承认，真不讲理！",
           "(2) 你……，这样做不对，为什么还要坚持呢？",
           "Đáp án: 你明明知道这样做不对，为什么还要坚持呢？",
           "(3) ……，怎么非说没看见？",
           "Đáp án: 你明明看见他进来了，怎么非说没看见？"],
    say=[F(0, "Luyện tập: dùng 明明 hoàn thành câu. Câu một: ……，却不承认，真不讲理！ …vậy mà không thừa nhận, thật là vô lý! Các bạn thử nhé."),
         F(1, "Đáp án gợi ý: 明明是他打破了杯子，却不承认，真不讲理！ Rõ ràng là anh ta làm vỡ cốc, vậy mà không thừa nhận, thật vô lý!"),
         F(2, "Câu hai: 你……，这样做不对，为什么还要坚持呢？ Bạn…, làm thế này là sai, sao vẫn còn khăng khăng?"),
         F(3, "Đáp án gợi ý: 你明明知道这样做不对，为什么还要坚持呢？ Bạn rõ ràng biết làm thế này là sai, sao vẫn còn khăng khăng? Phía sau là câu hỏi ngược."),
         F(4, "Câu ba: ……，怎么非说没看见？ …sao cứ nhất định nói là không nhìn thấy?"),
         F(5, "Đáp án gợi ý: 你明明看见他进来了，怎么非说没看见？ Bạn rõ ràng nhìn thấy anh ấy đi vào, sao cứ khăng khăng nói không thấy?")])

add("bullets", chapter="Ngữ pháp: 大不了", section="Ngữ pháp 注释", title="3. 大不了 dàbuliǎo – cùng lắm thì", size=38,
    items=["Phó từ, nghĩa là 最坏也不过 – xấu nhất cũng chỉ đến thế · dùng trong khẩu ngữ",
           "Dù gặp khó khăn, nhưng cuối cùng vẫn giải quyết được",
           "小林要去找领导讨公道：“哼，太不像话了，明明是在欺负人，大不了辞职。”",
           "失败了不要紧，大不了从头再来。",
           "别难过了，不就是衣服丢了吗，大不了再买一件。",
           "Mở rộng: tính từ “to tát, nghiêm trọng” – 这有什么大不了的？"],
    say=["Điểm ngữ pháp thứ ba là phó từ 大不了.",
         F(0, "大不了 nghĩa là 最坏也不过, xấu nhất cũng chỉ đến thế, tiếng Việt dịch là cùng lắm thì. Từ này dùng trong khẩu ngữ."),
         F(1, "Nó biểu thị: tuy đã xảy ra khó khăn, nhưng cuối cùng vẫn có thể giải quyết được, nên không cần quá lo lắng."),
         F(2, "Ví dụ một, lấy từ bài khóa: 小林要去找领导讨公道：哼，太不像话了，明明是在欺负人，大不了辞职。 Cùng lắm thì nghỉ việc, ý Tiểu Lâm là chẳng có gì phải sợ."),
         F(3, "Ví dụ hai: 失败了不要紧，大不了从头再来。 Thất bại cũng không sao, cùng lắm thì làm lại từ đầu."),
         F(4, "Ví dụ ba: 别难过了，不就是衣服丢了吗，大不了再买一件。 Đừng buồn nữa, chẳng phải chỉ là mất bộ quần áo thôi sao, cùng lắm thì mua bộ khác."),
         F(5, "Mở rộng thêm: 大不了 còn là tính từ, nghĩa là to tát, nghiêm trọng, thường dùng trong câu phủ định hoặc câu hỏi ngược. Ví dụ: 这有什么大不了的？ Chuyện này có gì to tát đâu?")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: dùng 大不了 viết lại câu", reveal=True, size=36,
    items=["(1) 坐错车没关系，最多就是坐回去。",
           "Đáp án: 坐错车没关系，大不了坐回去。",
           "(2) 别难过了，不过就是画儿湿了，我再给你画一张就完了。",
           "Đáp án: 别难过了，不过就是画儿湿了，大不了我再给你画一张。",
           "(3) 少一个座位？没关系，最多就是少去一个人。",
           "Đáp án: 少一个座位？没关系，大不了少去一个人。"],
    say=[F(0, "Luyện tập: dùng 大不了 viết lại câu. Câu một: 坐错车没关系，最多就是坐回去。 Đi nhầm xe không sao, nhiều nhất là đi ngược trở về. Các bạn tạm dừng và thử viết lại nhé."),
         F(1, "Đáp án: 坐错车没关系，大不了坐回去。 Đi nhầm xe không sao, cùng lắm thì đi ngược về. 最多就是 được thay bằng 大不了."),
         F(2, "Câu hai: 别难过了，不过就是画儿湿了，我再给你画一张就完了。 Đừng buồn nữa, chẳng qua là bức tranh bị ướt thôi, tôi vẽ lại cho bạn một bức là xong."),
         F(3, "Đáp án: 别难过了，不过就是画儿湿了，大不了我再给你画一张。 Cùng lắm thì tôi vẽ lại cho bạn một bức."),
         F(4, "Câu ba: 少一个座位？没关系，最多就是少去一个人。 Thiếu một chỗ ngồi à? Không sao, nhiều nhất là bớt đi một người."),
         F(5, "Đáp án: 少一个座位？没关系，大不了少去一个人。 Cùng lắm thì bớt đi một người. Các bạn thấy không, 大不了 luôn mang ý: chuyện này chẳng có gì nghiêm trọng.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 创立 – 创办", section="Phân biệt từ 词语辨析", title="Phân biệt 创立 và 创办",
    common="Giống nhau: đều là động từ, nghĩa là lần đầu lập ra. Ví dụ: 这所女子职业学校于1985年创立/创办。",
    cols=[{"head": "创立",
           "lines": ["(1) Nhấn mạnh 开创、成立: khai sáng, thành lập",
                     "Đúng: 这个组织创立于1942年。",
                     "(2) Dùng được cho chính đảng, quốc gia, học thuyết, lý luận",
                     "Đúng: 创立一个新的学术体系是个复杂的过程。"]},
          {"head": "创办",
           "lines": ["(1) Nhấn mạnh 创设、经营: lập ra và điều hành",
                     "Đúng: 他们几个人一起创办了一家民营企业。",
                     "(2) Không dùng cho chính đảng, quốc gia, học thuyết, lý luận",
                     "Sai: 这个学说创办于18世纪中期。"]}],
    say=["Tiếp theo là phần phân biệt từ: 创立 và 创办. Hai từ này có chung chữ Hán Việt là sáng, nên rất dễ dùng lẫn lộn.",
         "Điểm giống nhau: cả hai đều là động từ, đều có nghĩa là lần đầu lập ra, bắt đầu làm một việc. Ví dụ: 这所女子职业学校于一九八五年创立, hoặc 于一九八五年创办, đều đúng. Ngôi trường nghề dành cho nữ này được thành lập năm một chín tám lăm.",
         F(0, "Điểm khác thứ nhất. 创立 nhấn mạnh nghĩa 开创 và 成立, tức là khai sáng, thành lập ra một cái mới. Ví dụ: 这个组织创立于一九四二年。 Tổ chức này được thành lập năm một chín bốn hai."),
         F(1, "Còn 创办 nhấn mạnh nghĩa 创设 và 经营, tức là lập ra rồi còn điều hành, kinh doanh. Chữ 办 nghĩa là làm, lo liệu. Ví dụ: 他们几个人一起创办了一家民营企业。 Mấy người họ cùng nhau lập ra một doanh nghiệp tư nhân."),
         F(0, "Điểm khác thứ hai. 创立 dùng được cho chính đảng, quốc gia, học thuyết, lý luận. Ví dụ: 这个政党刚创立时，参加人员并不多。 Khi đảng này mới thành lập, số người tham gia không nhiều. Hay: 创立一个新的学术体系是个复杂的过程。 Sáng lập một hệ thống học thuật mới là một quá trình phức tạp."),
         F(1, "创办 thì không dùng cho chính đảng, quốc gia, học thuyết hay lý luận. Vì vậy câu 这个学说创办于十八世纪中期 là sai; phải nói 这个学说创立于十八世纪中期。"),
         "Mẹo nhớ: 创办 gắn với chữ 办, làm, lo liệu, nên thường đi với những thứ cần điều hành như trường học, công ty, nhà máy, tờ báo. Còn những thứ trừu tượng như học thuyết, lý luận, hay chính đảng, quốc gia, thì dùng 创立."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: chọn 创立 hay 创办 điền vào chỗ trống", reveal=True, size=36,
    items=["(1) 他们夫妻俩一手___起这家汽车修理厂。",
           "Đáp án: 创办 – nhà máy, xưởng cần điều hành, kinh doanh.",
           "(2) 这个学说___于18世纪中期，开始时遭到许多质疑。",
           "Đáp án: 创立 – học thuyết chỉ dùng 创立.",
           "(3) 近年来，一些地方相继___了各种以营利为目的的服务中心。",
           "Đáp án: 创办 – trung tâm dịch vụ kinh doanh kiếm lời.",
           "(4) 新理论___初期，遇到很多困难和挑战。",
           "Đáp án: 创立 – lý luận chỉ dùng 创立."],
    say=[F(0, "Bây giờ chúng ta làm thử: chọn 创立 hoặc 创办 để điền vào chỗ trống. Câu một: 他们夫妻俩一手什么起这家汽车修理厂。 Hai vợ chồng họ một tay gây dựng nên xưởng sửa chữa ô tô này. Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: 创办. 他们夫妻俩一手创办起这家汽车修理厂。 Xưởng sửa xe là thứ cần lập ra rồi điều hành, kinh doanh."),
         F(2, "Câu hai: 这个学说什么于十八世纪中期，开始时遭到许多质疑。 Học thuyết này ra đời vào giữa thế kỷ mười tám, ban đầu gặp phải nhiều nghi vấn."),
         F(3, "Đáp án: 创立. 这个学说创立于十八世纪中期。 Học thuyết là thứ trừu tượng, chỉ dùng 创立."),
         F(4, "Câu ba: 近年来，一些地方相继什么了各种以营利为目的的服务中心。 Mấy năm gần đây, một số địa phương lần lượt mở ra các trung tâm dịch vụ nhằm mục đích kiếm lời."),
         F(5, "Đáp án: 创办. 一些地方相继创办了各种服务中心。 Trung tâm dịch vụ là nơi kinh doanh, cần điều hành, nên dùng 创办."),
         F(6, "Câu bốn: 新理论什么初期，遇到很多困难和挑战。 Thời kỳ đầu khi lý luận mới ra đời, gặp phải rất nhiều khó khăn và thử thách."),
         F(7, "Đáp án: 创立. 新理论创立初期，遇到很多困难和挑战。 Lý luận cũng giống học thuyết, chỉ dùng 创立.")])

# ======================= MỞ RỘNG: KẾT HỢP TỪ =======================
add("bullets", chapter="Mở rộng: kết hợp từ", section="Mở rộng 扩展", title="Kết hợp từ (词语搭配) (1): 性感 · 澄清 · 奠定 · 动机", size=34,
    items=["## 性感 (tính cảm) – gợi cảm",
           "身材性感 · 她是一位性感明星。",
           "## 澄清 (trừng thanh) – làm sáng tỏ",
           "澄清事实 · 他决心一定要澄清事情的真相。",
           "## 奠定 (điện định) – đặt nền móng",
           "奠定基础 · 他数年来的刻苦训练为赢得今天的大赛奠定了基础。",
           "## 动机 (động cơ) – động cơ, ý đồ",
           "没有动机 / 动机不纯 · 即便动机是好的，如果方法不对，也会把事情办坏。"],
    say=["Bây giờ chúng ta sang phần mở rộng của sách. Bài này không có mục tu từ riêng; phần mở rộng giới thiệu mười hai từ cùng các cụm kết hợp từ thường gặp, tiếng Trung gọi là 词语搭配. Học từ theo cụm sẽ giúp các bạn dùng từ tự nhiên như người bản ngữ.",
         F(0, "Từ thứ nhất: 性感, nghĩa là gợi cảm. Cẩn thận: Hán Việt là tính cảm, không phải tình cảm."),
         F(1, "Cụm kết hợp: 身材性感, thân hình gợi cảm. Ví dụ: 她是一位性感明星。 Cô ấy là một ngôi sao gợi cảm."),
         F(2, "Từ thứ hai: 澄清, nghĩa là làm sáng tỏ, đính chính một sự việc bị hiểu lầm."),
         F(3, "Cụm kết hợp: 澄清事实, làm sáng tỏ sự thật. Ví dụ: 他决心一定要澄清事情的真相。 Anh ấy quyết tâm nhất định phải làm sáng tỏ chân tướng sự việc."),
         F(4, "Từ thứ ba: 奠定, nghĩa là đặt nền móng, tạo cơ sở vững chắc."),
         F(5, "Cụm kết hợp: 奠定基础, đặt nền móng. Ví dụ: 他数年来的刻苦训练为赢得今天的大赛奠定了基础。 Nhiều năm khổ luyện đã đặt nền móng cho chiến thắng trong giải đấu lớn hôm nay của anh ấy."),
         F(6, "Từ thứ tư: 动机, nghĩa là động cơ, ý định bên trong thúc đẩy hành động, âm Hán Việt và nghĩa giống tiếng Việt."),
         F(7, "Cụm kết hợp: 没有动机, không có động cơ; 动机不纯, động cơ không trong sáng. Ví dụ: 即便动机是好的，如果方法不对，也会把事情办坏。 Cho dù động cơ là tốt, nếu cách làm không đúng, cũng sẽ làm hỏng việc.")])

add("bullets", section="Mở rộng 扩展", title="Kết hợp từ (2): 断绝 · 见闻 · 章程 · 周年", size=34,
    items=["## 断绝 (đoạn tuyệt) – cắt đứt",
           "断绝来往 · 和他那样的人断绝来往绝对是明智的。",
           "## 见闻 (kiến văn) – điều tai nghe mắt thấy, hiểu biết",
           "旅游见闻 / 增长见闻 · 旅游不光使我们增长见闻，还能让我们认识更多的朋友。",
           "## 章程 (chương trình) – điều lệ, quy chế",
           "公司章程 · 员工们都应该熟悉本公司的章程。",
           "## 周年 (chu niên) – tròn năm, ngày kỷ niệm",
           "结婚周年 / 周年庆典 · 明天是我们公司成立十周年庆典。"],
    say=[F(0, "Từ thứ năm: 断绝, Hán Việt là đoạn tuyệt, nghĩa là cắt đứt hoàn toàn một mối quan hệ hay sự liên lạc."),
         F(1, "Cụm kết hợp: 断绝来往, cắt đứt qua lại. Ví dụ: 和他那样的人断绝来往绝对是明智的。 Cắt đứt qua lại với loại người như anh ta chắc chắn là sáng suốt."),
         F(2, "Từ thứ sáu: 见闻, Hán Việt là kiến văn, nghĩa là những điều tai nghe mắt thấy, vốn hiểu biết."),
         F(3, "Cụm kết hợp: 旅游见闻, những điều mắt thấy tai nghe khi du lịch; 增长见闻, mở mang hiểu biết. Ví dụ: 旅游不光使我们增长见闻，还能让我们认识更多的朋友。 Du lịch không chỉ giúp ta mở mang hiểu biết, mà còn giúp ta quen thêm nhiều bạn bè."),
         F(4, "Từ thứ bảy: 章程, Hán Việt là chương trình. Đây là từ rất dễ nhầm! 章程 không phải là chương trình theo nghĩa tiếng Việt, mà là điều lệ, quy chế của một tổ chức. Chương trình trong tiếng Việt, tiếng Trung là 节目 hoặc 程序."),
         F(5, "Cụm kết hợp: 公司章程, điều lệ công ty. Ví dụ: 员工们都应该熟悉本公司的章程。 Nhân viên đều nên nắm rõ điều lệ của công ty mình."),
         F(6, "Từ thứ tám: 周年, Hán Việt là chu niên, nghĩa là tròn một năm, ngày kỷ niệm hằng năm."),
         F(7, "Cụm kết hợp: 结婚周年, kỷ niệm ngày cưới; 周年庆典, lễ kỷ niệm. Ví dụ: 明天是我们公司成立十周年庆典。 Ngày mai là lễ kỷ niệm mười năm thành lập công ty chúng tôi.")])

add("bullets", section="Mở rộng 扩展", title="Kết hợp từ (3): 起草 · 无赖 · 暧昧 · 后顾之忧", size=34,
    items=["## 起草 (khởi thảo) – soạn thảo, viết bản nháp",
           "起草文件 · 我起草了一个俱乐部章程，你再修改一下。",
           "## 无赖 (vô lại) – kẻ vô lại; ngang ngược vô lý",
           "耍无赖 · 谁都不喜欢毫不讲理的无赖。",
           "## 暧昧 (ái muội) – mập mờ, không rõ ràng",
           "态度暧昧 / 关系暧昧 · 你有没有发现，咱们办公室的小王和小李关系有点儿暧昧。",
           "## 后顾之忧 (hậu cố chi ưu) – nỗi lo về sau",
           "只有不断完善社会保障制度，才能让人民生活没有后顾之忧。"],
    say=[F(0, "Từ thứ chín: 起草, Hán Việt là khởi thảo, nghĩa là soạn thảo, viết bản nháp đầu tiên của một văn bản."),
         F(1, "Cụm kết hợp: 起草文件, soạn thảo văn bản. Ví dụ: 我起草了一个俱乐部章程，你再修改一下。 Tôi đã soạn thảo một bản điều lệ câu lạc bộ, bạn sửa lại giúp nhé. Các bạn thấy không, từ 章程 lại xuất hiện ở đây."),
         F(2, "Từ thứ mười: 无赖, Hán Việt là vô lại, nghĩa là kẻ vô lại, kẻ ngang ngược không nói lý lẽ."),
         F(3, "Cụm kết hợp: 耍无赖, giở trò vô lại, ăn vạ. Ví dụ: 谁都不喜欢毫不讲理的无赖。 Chẳng ai thích kẻ vô lại không chút lý lẽ."),
         F(4, "Từ thứ mười một: 暧昧, Hán Việt là ái muội, nghĩa là mập mờ, không rõ ràng; khi nói về quan hệ nam nữ thì là mờ ám, có gì đó khó nói."),
         F(5, "Cụm kết hợp: 态度暧昧, thái độ mập mờ; 关系暧昧, quan hệ mờ ám. Ví dụ: 你有没有发现，咱们办公室的小王和小李关系有点儿暧昧。 Cậu có thấy không, quan hệ giữa Tiểu Vương và Tiểu Lý ở văn phòng mình hơi mờ ám đấy."),
         F(6, "Từ cuối cùng: 后顾之忧, Hán Việt là hậu cố chi ưu, nghĩa đen là nỗi lo khi ngoảnh lại phía sau, tức là nỗi lo về sau, nỗi lo ở hậu phương."),
         F(7, "Ví dụ: 只有不断完善社会保障制度，才能让人民生活没有后顾之忧。 Chỉ có không ngừng hoàn thiện chế độ bảo đảm xã hội, mới khiến cuộc sống của người dân không còn nỗi lo về sau.")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chọn từ điền vào chỗ trống (1)", reveal=True, size=36,
    items=["## Từ cho sẵn: 澄清 · 奠定 · 起草 · 后顾之忧",
           "(1) 公司发表声明，___了网上的错误消息。",
           "Đáp án: 澄清",
           "(2) 大学四年的学习为他后来的工作___了基础。",
           "Đáp án: 奠定",
           "(3) 这份合同由小王负责___，明天交给经理。",
           "Đáp án: 起草",
           "(4) 公司为员工的孩子开办了幼儿园，让员工没有了___。",
           "Đáp án: 后顾之忧"],
    say=[F(0, "Bây giờ chúng ta luyện tập: chọn từ thích hợp điền vào chỗ trống. Bốn từ cho sẵn là: 澄清，奠定，起草，后顾之忧."),
         F(1, "Câu một: 公司发表声明，什么了网上的错误消息。 Công ty ra thông cáo, … những tin sai lệch trên mạng. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 澄清. 公司发表声明，澄清了网上的错误消息。 Công ty ra thông cáo đính chính những tin sai lệch trên mạng."),
         F(3, "Câu hai: 大学四年的学习为他后来的工作什么了基础。 Bốn năm đại học đã … cho công việc sau này của anh ấy."),
         F(4, "Đáp án: 奠定. 奠定了基础, đặt nền móng. Đây chính là cụm kết hợp ta vừa học."),
         F(5, "Câu ba: 这份合同由小王负责什么，明天交给经理。 Bản hợp đồng này do Tiểu Vương phụ trách …, ngày mai nộp cho giám đốc."),
         F(6, "Đáp án: 起草. 这份合同由小王负责起草。 Bản hợp đồng này do Tiểu Vương phụ trách soạn thảo."),
         F(7, "Câu bốn: 公司为员工的孩子开办了幼儿园，让员工没有了什么。 Công ty mở nhà trẻ cho con của nhân viên, giúp nhân viên không còn …"),
         F(8, "Đáp án: 后顾之忧. 让员工没有了后顾之忧。 Giúp nhân viên không còn phải lo lắng chuyện ở nhà, yên tâm làm việc.")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chọn từ điền vào chỗ trống (2)", reveal=True, size=36,
    items=["## Từ cho sẵn: 动机 · 断绝 · 章程 · 周年",
           "(5) 我不明白他这样做的___是什么。",
           "Đáp án: 动机",
           "(6) 两个人吵了一架以后，就___了来往。",
           "Đáp án: 断绝",
           "(7) 加入俱乐部以前，请先认真阅读俱乐部的___。",
           "Đáp án: 章程",
           "(8) 下个月是我们结婚十___，我想给妻子一个惊喜。",
           "Đáp án: 周年"],
    say=[F(0, "Phần hai, bốn từ cho sẵn là: 动机，断绝，章程，周年."),
         F(1, "Câu năm: 我不明白他这样做的什么是什么。 Tôi không hiểu … của anh ta khi làm như vậy là gì."),
         F(2, "Đáp án: 动机. 我不明白他这样做的动机是什么。 Tôi không hiểu động cơ anh ta làm như vậy là gì."),
         F(3, "Câu sáu: 两个人吵了一架以后，就什么了来往。 Sau khi cãi nhau một trận, hai người … qua lại."),
         F(4, "Đáp án: 断绝. 断绝了来往, cắt đứt qua lại."),
         F(5, "Câu bảy: 加入俱乐部以前，请先认真阅读俱乐部的什么。 Trước khi gia nhập câu lạc bộ, xin hãy đọc kỹ … của câu lạc bộ."),
         F(6, "Đáp án: 章程. 俱乐部的章程, điều lệ câu lạc bộ. Nhớ nhé, không phải chương trình đâu."),
         F(7, "Câu tám: 下个月是我们结婚十什么，我想给妻子一个惊喜。 Tháng sau là kỷ niệm mười năm ngày cưới của chúng tôi, tôi muốn tạo bất ngờ cho vợ."),
         F(8, "Đáp án: 周年. 结婚十周年, kỷ niệm mười năm ngày cưới.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ có dấu chấm", size=40,
    items=["就职 (职) → 辞职 · 兼职 · 职业 · 职务",
           "职位 (位) → 地位 · 座位 · 单位 · 岗位",
           "唯独 (唯) → 唯一 · 唯有 · 唯恐 · 唯美",
           "才干 (才) → 才能 · 人才 · 天才 · 口才",
           "敬业 (业) → 专业 · 事业 · 毕业 · 创业"],
    say=["Phần luyện tập. Bài tập một: mô phỏng ví dụ, viết thêm các từ có chứa chữ được đánh dấu chấm.",
         F(0, "Ví dụ mẫu: 就职, chữ được đánh dấu là chữ thứ hai, nghĩa là chức vụ, công việc. Ta có 辞职，兼职，职业，职务. Tức là từ chức, làm thêm, nghề nghiệp, và chức vụ."),
         F(1, "职位, chữ được đánh dấu là chữ thứ hai, nghĩa là vị trí, chỗ. Ta có 地位，座位，单位，岗位. Tức là địa vị, chỗ ngồi, đơn vị cơ quan, và vị trí công tác."),
         F(2, "唯独, chữ được đánh dấu là chữ đầu, nghĩa là chỉ, duy nhất. Ta có 唯一，唯有，唯恐，唯美. Tức là duy nhất, chỉ có, chỉ sợ, và duy mỹ, đẹp thuần túy."),
         F(3, "才干, chữ được đánh dấu là chữ đầu, nghĩa là tài. Ta có 才能，人才，天才，口才. Tức là tài năng, nhân tài, thiên tài, và tài ăn nói."),
         F(4, "敬业, chữ được đánh dấu là chữ thứ hai, nghĩa là nghề nghiệp, sự nghiệp. Ta có 专业，事业，毕业，创业. Tức là chuyên ngành, sự nghiệp, tốt nghiệp, và khởi nghiệp.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Hoàn thành câu bằng từ cho sẵn (1)", reveal=True, size=36,
    items=["(1) 别的事还可以放一放，……。（唯独）",
           "Đáp án: 别的事还可以放一放，唯独这件事必须马上办。",
           "(2) 爸爸……，从来没有闲下来的时候。（成天）",
           "Đáp án: 爸爸成天忙着工作，从来没有闲下来的时候。",
           "(3) 失业了也没什么，……。（大不了）",
           "Đáp án: 失业了也没什么，大不了再找一份工作。"],
    say=[F(0, "Bài tập hai: dùng từ cho sẵn để hoàn thành câu. Câu một, dùng 唯独: 别的事还可以放一放，…… Những việc khác còn có thể để đó đã, … Các bạn tạm dừng và thử hoàn thành nhé."),
         F(1, "Đáp án gợi ý: 别的事还可以放一放，唯独这件事必须马上办。 Những việc khác còn có thể gác lại, chỉ riêng việc này phải làm ngay."),
         F(2, "Câu hai, dùng 成天: 爸爸……，从来没有闲下来的时候。 Bố…, chưa bao giờ có lúc rảnh rỗi."),
         F(3, "Đáp án gợi ý: 爸爸成天忙着工作，从来没有闲下来的时候。 Bố suốt ngày bận công việc, chưa bao giờ có lúc rảnh rỗi."),
         F(4, "Câu ba, dùng 大不了: 失业了也没什么，…… Thất nghiệp cũng chẳng sao, …"),
         F(5, "Đáp án gợi ý: 失业了也没什么，大不了再找一份工作。 Thất nghiệp cũng chẳng sao, cùng lắm thì tìm việc khác.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Hoàn thành câu bằng từ cho sẵn (2)", reveal=True, size=36,
    items=["(4) 我的笔……，怎么一转眼不见了呢？（明明）",
           "Đáp án: 我的笔明明就放在桌子上，怎么一转眼不见了呢？",
           "(5) 没有床，只有一张沙发，你……。（凑合）",
           "Đáp án: 没有床，只有一张沙发，你就凑合着睡一晚吧。",
           "(6) 每当我遇到困难时，他……。（想方设法）",
           "Đáp án: 每当我遇到困难时，他总是想方设法地帮助我。"],
    say=[F(0, "Câu bốn, dùng 明明: 我的笔……，怎么一转眼不见了呢？ Cây bút của tôi…, sao chớp mắt đã không thấy đâu?"),
         F(1, "Đáp án gợi ý: 我的笔明明就放在桌子上，怎么一转眼不见了呢？ Cây bút của tôi rõ ràng để ngay trên bàn, sao chớp mắt đã biến mất? Phía sau là câu hỏi ngược, đúng như cách dùng của 明明."),
         F(2, "Câu năm, dùng 凑合: 没有床，只有一张沙发，你…… Không có giường, chỉ có một chiếc ghế sô pha, bạn…"),
         F(3, "Đáp án gợi ý: 你就凑合着睡一晚吧。 Bạn ngủ tạm một đêm vậy nhé. Ở đây 凑合 là tạm bợ, tạm chấp nhận."),
         F(4, "Câu sáu, dùng 想方设法: 每当我遇到困难时，他…… Mỗi khi tôi gặp khó khăn, anh ấy…"),
         F(5, "Đáp án gợi ý: 他总是想方设法地帮助我。 Anh ấy luôn nghĩ đủ mọi cách để giúp tôi.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (1)", reveal=True, size=34,
    items=["## Từ cho sẵn: 计较 · 搭档 · 风气 · 资深 · 创立",
           "上个星期，我加入了学校篮球队，跟球队的___们一一认识之后，我的训练生活就此开始。张教练在球队___之初就在这儿了，他是一位富有经验的___篮球教练。我们球队的___非常好，大家互相帮助，训练刻苦认真，没人喊累，没人抱怨，训练中受点儿伤也都不___，我很喜欢这个集体。",
           "Đáp án: 搭档 · 创立 · 资深 · 风气 · 计较"],
    say=[F(0, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn một có năm từ: 计较，搭档，风气，资深，创立."),
         F(1, "上个星期，我加入了学校篮球队，跟球队的什么们一一认识之后，我的训练生活就此开始。张教练在球队什么之初就在这儿了，他是一位富有经验的什么篮球教练。我们球队的什么非常好，大家互相帮助，训练刻苦认真，没人喊累，没人抱怨，训练中受点儿伤也都不什么，我很喜欢这个集体。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 跟球队的搭档们一一认识，张教练在球队创立之初就在这儿了，一位富有经验的资深篮球教练，我们球队的风气非常好，受点儿伤也都不计较。 Tuần trước tôi gia nhập đội bóng rổ của trường. Huấn luyện viên Trương đã ở đây từ khi đội mới thành lập, là một huấn luyện viên lâu năm giàu kinh nghiệm. Nề nếp của đội rất tốt, mọi người giúp đỡ nhau, có bị thương một chút cũng không so đo.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (2)", reveal=True, size=34,
    items=["## Từ cho sẵn: 激情 · 全力以赴 · 想方设法 · 忙碌 · 凑合",
           "同事小张非常敬业，他对待工作充满___，总是___出色完成每一项任务，从来不___。最近，他接到一个新任务，为一个新项目做前期准备。小张带领他们部门的员工___投入工作，虽然很___，却享受到了工作的快乐。",
           "Đáp án: 激情 · 想方设法 · 凑合 · 全力以赴 · 忙碌"],
    say=[F(0, "Đoạn hai có năm từ: 激情，全力以赴，想方设法，忙碌，凑合."),
         F(1, "同事小张非常敬业，他对待工作充满什么，总是什么出色完成每一项任务，从来不什么。最近，他接到一个新任务，为一个新项目做前期准备。小张带领他们部门的员工什么投入工作，虽然很什么，却享受到了工作的快乐。 Các bạn điền thử nhé."),
         F(2, "Đáp án: 充满激情，总是想方设法出色完成每一项任务，从来不凑合，带领员工全力以赴投入工作，虽然很忙碌。 Đồng nghiệp Tiểu Trương rất tận tụy, làm việc tràn đầy nhiệt huyết, luôn nghĩ mọi cách hoàn thành xuất sắc từng nhiệm vụ, chưa bao giờ làm qua quýt. Anh ấy dẫn dắt nhân viên dốc toàn lực làm việc, tuy rất bận rộn nhưng lại tận hưởng được niềm vui công việc."),
         F(2, "Các bạn thấy không, Tiểu Trương trong đoạn văn này rất giống nhân vật tôi trong bài khóa: không so đo, dốc toàn lực, và tìm thấy niềm vui trong công việc.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 4: Đọc đoạn văn, mô phỏng đặt câu", reveal=True, size=34,
    items=["清早上班，和新同事一一认识后，我以为一天的工作就此开始，没想到……我想这单位风气真好……",
           "Đáp án: 今天在办公室，我怎么也找不到自己的手机了，我以为丢在出租车上了，没想到它一直在我的包里，我想以后一定要细心一点儿。",
           "其实，进入新单位，作为一个职场插班生，这个过程，正是展示你人格魅力的时候，遇到困难，也是你施展才能的时机。",
           "Đáp án: 其实，进入新球队，作为一名新队员，这个过程，正是锻炼自己的时候，遇到困难，也是你提高水平的时机。"],
    say=[F(0, "Bài tập bốn: đọc đoạn văn, rồi mô phỏng để đặt câu. Câu mẫu một có khung 我以为……没想到……我想……, tôi tưởng rằng…, không ngờ…, tôi nghĩ…. Đề bài cho sẵn đầu câu: 今天在办公室，我怎么也找不到自己的手机了。 Hôm nay ở văn phòng, tôi tìm mãi không thấy điện thoại của mình. Các bạn thử viết tiếp nhé."),
         F(1, "Đáp án gợi ý: 我以为丢在出租车上了，没想到它一直在我的包里，我想以后一定要细心一点儿。 Tôi tưởng là để quên trên taxi, không ngờ nó vẫn nằm trong túi của tôi, tôi nghĩ sau này nhất định phải cẩn thận hơn."),
         F(2, "Câu mẫu hai là câu kết của bài khóa, với khung: 其实，进入……，作为……，这个过程，正是……的时候，遇到……，也是……的时机。"),
         F(3, "Đáp án gợi ý: 其实，进入新球队，作为一名新队员，这个过程，正是锻炼自己的时候，遇到困难，也是你提高水平的时机。 Thật ra, vào một đội bóng mới, với tư cách là thành viên mới, quá trình này chính là lúc rèn luyện bản thân; gặp khó khăn, cũng là thời cơ để bạn nâng cao trình độ.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 6", size=36,
    items=["Từ vựng trọng tâm: 资深 · 搭档 · 边缘 · 计较 · 全力以赴 · 敷衍 · 想方设法 · 凑合 · 兢兢业业 · 施展",
           "Ngữ pháp: 唯独 (chỉ có, duy chỉ) · 明明 (rõ ràng) · 大不了 (cùng lắm thì)",
           "Phân biệt: 创立 (khai sáng; cả học thuyết, lý luận) ≠ 创办 (lập ra và điều hành)",
           "Mở rộng: 12 cụm kết hợp từ – chú ý 章程 là điều lệ, không phải chương trình",
           "## Bài tập về nhà (运用)",
           "Viết bài khoảng 300 chữ, tựa đề “初入……”: lần đầu vào một tập thể mới, bạn gặp gì và đã làm thế nào?"],
    say=["Chúng ta cùng tổng kết bài sáu.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 资深，搭档，边缘，计较，全力以赴，敷衍，想方设法，凑合，兢兢业业，施展. Và đừng quên những từ dễ nhầm như 风气，眼色，计较，怠慢."),
         F(1, "Về ngữ pháp: 唯独 tách riêng một đối tượng ra khỏi số đông, nghĩa là chỉ có. 明明 nghĩa là rõ ràng, thường đi kèm câu hỏi ngược hoặc vế chuyển ý. 大不了 nghĩa là cùng lắm thì, cho thấy khó khăn rồi cũng giải quyết được."),
         F(2, "Về phân biệt từ: 创立 nhấn mạnh khai sáng, thành lập, dùng được cho chính đảng, quốc gia, học thuyết, lý luận; còn 创办 nhấn mạnh lập ra và điều hành, không dùng cho những thứ đó."),
         F(3, "Về phần mở rộng: hãy học thuộc mười hai cụm kết hợp từ, đặc biệt nhớ 章程 là điều lệ, còn 性感 là gợi cảm."),
         F(5, "Bài tập về nhà, theo phần vận dụng của sách: bài khóa kể rằng khi mới vào nghề, ta có thể gặp những đối xử không công bằng, nhưng nếu không bỏ cuộc, kiên trì nỗ lực, nhất định sẽ được mọi người công nhận. Khi bạn bước vào một tập thể mới, như công ty, đội bóng, lớp học hay ban nhạc, bạn có từng gặp tình huống tương tự không? Bạn đã làm thế nào, kết quả ra sao? Hãy viết một bài khoảng ba trăm chữ, với tựa đề 初入……, nghĩa là lần đầu bước vào…. Nhớ thử dùng 唯独，明明，大不了 trong bài viết nhé."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Dù ở bất kỳ môi trường mới nào, hãy nhớ rằng khó khăn ban đầu cũng chính là thời cơ để chúng ta thể hiện mình. Hẹn gặp lại các bạn ở bài bảy: 我的人生我做主, Tôi làm chủ cuộc đời tôi. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Thượng) – Bài 6: 当好职场插班生 (Hãy là học sinh giỏi tại nơi làm việc)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"搭档": "搭荡",            # dādàng
                    "溜": "熘",                # liū (bài chỉ dùng nghĩa chuồn, lẻn)
                    "才干": "才赣",            # cáigàn
                    "澄清": "橙清",            # chéngqīng
                    "增长": "增涨",            # zēngzhǎng
                    "数年来": "树年来",        # shùniánlái
                    "为赢得": "位赢得"},        # wèi
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai06.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
