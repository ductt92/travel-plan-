#!/usr/bin/env python3
"""Kịch bản bài giảng 顶石中文 – Bài 2.2 «信息化社会：“一个都不能少”». Chạy để sinh ds22.json."""
import json
import os

TAG = "顶石中文 · Bài 2.2 · 信息化社会：“一个都不能少”"
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
    zh="信息化社会", py="“一个都不能少”",
    vi="Bài 2.2: Xã hội thông tin: “Không ai bị bỏ lại”",
    sub="Xìnxīhuà shèhuì: “yí gè dōu bù néng shǎo”\nBài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn trở lại với bài giảng giáo trình 顶石中文, Đỉnh cao tiếng Trung.",
         "Hôm nay chúng ta học bài thứ hai của Đơn vị hai, chủ đề 时代篇, Thời đại: bài hai chấm hai, 信息化社会：一个都不能少。 Nghĩa là: Xã hội thông tin hóa: không một ai bị bỏ lại.",
         "Cụm 一个都不能少 nghĩa đen là một người cũng không được thiếu. Đây cũng là tên một bộ phim nổi tiếng của đạo diễn Trương Nghệ Mưu về một cô giáo làng quyết không để học trò nào bỏ học.",
         "Bài khóa là một bài bình luận trên báo Nhân Dân Trung Quốc, 人民日报. Câu chuyện bắt đầu từ một cô gái tự tay vẽ cho bà ngoại cuốn hướng dẫn dùng WeChat. Từ đó, bài viết bàn về khoảng cách số giữa người già và thời đại điện thoại thông minh, và việc xã hội cần làm để không bỏ lại ai phía sau. Chắc hẳn ông bà, cha mẹ của chúng ta cũng từng gặp những khó khăn như vậy."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài bình luận: người cao tuổi và “khoảng cách số” (数字鸿沟)",
           "Nắm vững 51 từ mới và thành ngữ, kèm âm Hán Việt và ví dụ",
           "Câu mẫu: ……得不行 · 得益于 · 不知……好 · 连……也……，更不用说 · 以致 · 一度 · 鉴于 · 并举 · 致力于 · 由此可见",
           "Kết hợp từ (词语搭配): 一众 · 视野 · 鸿沟 · 顺畅 · 人文 · 优化",
           "Luyện tập theo sách và thảo luận, liên hệ với Việt Nam"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài bình luận: người cao tuổi gặp những khó khăn gì trong xã hội số, vì sao giúp họ là nghĩa vụ và trách nhiệm, và xã hội đã làm những gì."),
         F(1, "Thứ hai, nắm vững năm mươi mốt từ mới và thành ngữ. Bài này có rất nhiều từ của thời đại số, như 扫码，界面，在线，浏览, rất hữu ích trong đời sống."),
         F(2, "Thứ ba, học mười câu mẫu trọng điểm, như 得不行, đến mức không chịu nổi; 鉴于, xét thấy; 致力于, dốc sức vào; và 由此可见, từ đó có thể thấy."),
         F(3, "Thứ tư, học cách kết hợp từ: 一众网友，公众视野，数字鸿沟，交流顺畅，人文关怀，优化环境."),
         F(4, "Thứ năm, làm toàn bộ bài tập của sách và thảo luận. Các bạn chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé.")])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 课前思考", title="Câu hỏi trước bài (课前思考)", size=40,
    items=["1. 你身边的老年人使用智能手机吗？情况如何？",
           "2. “信息化社会”给老年人的生活带来了哪些不便？",
           "3. 我们年轻人可以给身边的老年人提供怎样的帮助？",
           "Gợi ý: quét mã QR · đặt lịch khám online · mua vé tàu · thanh toán di động · gọi video"],
    say=["Chúng ta bắt đầu với ba câu hỏi trước bài, 课前思考.",
         F(0, "Câu một: 你身边的老年人使用智能手机吗？情况如何？ Những người cao tuổi bên cạnh bạn có dùng điện thoại thông minh không? Tình hình thế nào?"),
         F(1, "Câu hai: 信息化社会给老年人的生活带来了哪些不便？ Xã hội thông tin hóa đã mang lại cho người già những bất tiện gì? 不便 là bất tiện."),
         F(2, "Câu ba: 我们年轻人可以给身边的老年人提供怎样的帮助？ Người trẻ chúng ta có thể giúp đỡ những người già bên cạnh như thế nào?"),
         F(3, "Các bạn có thể nghĩ đến những việc rất cụ thể: quét mã QR, đặt lịch khám bệnh trên mạng, mua vé tàu, thanh toán bằng điện thoại, gọi video. Ở Việt Nam, những việc này cũng đã trở nên rất phổ biến. Các bạn tạm dừng video và thử trả lời bằng tiếng Trung nhé.")])

add("bullets", section="Khởi động 课前思考", title="Bối cảnh (注释)", size=34,
    items=["## 点赞 · 收藏 · 转发 – thích (like) · lưu · chia sẻ: chức năng cơ bản của mạng xã hội",
           "## 新冠肺炎 xīnguān fèiyán – viêm phổi do virus corona chủng mới (COVID-19)",
           "## 健康码 – mã sức khỏe",
           "Mã QR cá nhân thời phòng chống dịch: tự khai báo trên mạng, được xét duyệt rồi cấp mã; dùng làm giấy thông hành điện tử",
           "## “十四五” – Quy hoạch 5 năm lần thứ 14 (2021–2025) và mục tiêu tầm nhìn 2035",
           "## 文化反哺 – “văn hóa mớm ngược”: thế hệ trẻ truyền lại tri thức, kỹ năng mới cho thế hệ trước"],
    say=["Trước khi học từ mới, chúng ta xem năm chú thích của sách, giúp hiểu bối cảnh bài khóa.",
         F(0, "Một: 点赞，收藏，转发, tức là bấm thích, lưu lại, và chia sẻ lại, những chức năng cơ bản trên mạng xã hội. 点赞 nghĩa đen là bấm một cái tán thưởng, chính là nút like."),
         F(1, "Hai: 新冠肺炎, viêm phổi do virus corona chủng mới, tức COVID mười chín. 新冠 là viết tắt của 新型冠状病毒, chữ 冠 ở đây đọc thanh một."),
         F(2, "Ba: 健康码, mã sức khỏe."),
         F(3, "Đó là mã QR cá nhân ra đời trong thời kỳ phòng chống dịch ở Trung Quốc: người dân tự khai báo trên mạng, sau khi xét duyệt thì được cấp mã. Mã này là giấy thông hành điện tử để ra vào các nơi. Người già không có điện thoại thông minh thì không có mã, và gặp rất nhiều khó khăn."),
         F(4, "Bốn: 十四五, tức Quy hoạch năm năm lần thứ mười bốn về phát triển kinh tế xã hội của Trung Quốc, giai đoạn hai nghìn không trăm hai mươi mốt đến hai nghìn không trăm hai mươi lăm, cùng mục tiêu tầm nhìn đến năm hai nghìn không trăm ba mươi lăm."),
         F(5, "Năm: 文化反哺. 反哺 vốn là chim con lớn lên mớm mồi lại cho chim mẹ. 文化反哺 là thuật ngữ xã hội học: trong thời đại văn hóa thay đổi nhanh, thế hệ trẻ lại truyền dạy tri thức mới cho thế hệ trước. Đây là ý then chốt của bài khóa.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("手绘", "shǒuhuì", "thủ hội", "động từ", "vẽ tay", "她给朋友手绘了一张生日卡。", "Cô ấy vẽ tay một tấm thiệp sinh nhật tặng bạn.",
     "Động từ, nghĩa là tự tay vẽ, không dùng máy móc. Chữ 绘 là vẽ, như trong 绘画, hội họa. Ví dụ của sách: 手绘书签, đánh dấu sách vẽ tay. Trong bài: 一个女孩为外婆手绘了一份微信使用说明书, một cô gái tự tay vẽ cho bà ngoại một bản hướng dẫn dùng WeChat."),
    ("字迹", "zìjì", "tự tích", "danh từ", "nét chữ, chữ viết", "这封信的字迹已经模糊了。", "Nét chữ của bức thư này đã mờ rồi.",
     "Danh từ, nghĩa là nét chữ, hình dáng chữ viết. 迹 là dấu vết. Kết hợp hay gặp: 字迹模糊, chữ mờ; 字迹清晰, chữ rõ ràng; 字迹工整, chữ ngay ngắn."),
    ("工整", "gōngzhěng", "công chỉnh", "tính từ", "ngay ngắn, chỉn chu", "他的字写得非常工整。", "Chữ anh ấy viết rất ngay ngắn.",
     "Tính từ, nghĩa là tỉ mỉ, ngay ngắn, gọn gàng, thường nói về chữ viết: 字迹工整，笔画工整. Trong bài: 字迹工整、内容详细、图文并茂, chữ viết ngay ngắn, nội dung chi tiết, hình và chữ đều phong phú."),
    ("暖心", "nuǎnxīn", "noãn tâm", "tính từ", "ấm lòng, làm ấm lòng", "这个小女孩的举动真暖心。", "Hành động của cô bé này thật ấm lòng.",
     "Tính từ, nghĩa là khiến lòng người cảm thấy ấm áp, rất hay dùng trên mạng và báo chí. Trong bài: 此举相当暖心, việc làm này thật ấm lòng; 此举 là hành động này, văn viết."),
    ("一众", "yīzhòng", "nhất chúng", "lượng từ", "một loạt, đông đảo", "该剧汇集了一众老演员。", "Bộ phim quy tụ đông đảo diễn viên gạo cội.",
     "Lượng từ, nghĩa là một đám, một nhóm đông người. Kết hợp hay gặp: 一众网友，一众朋友，一众游客. Trong bài: 打动了一众网友, làm cảm động đông đảo cư dân mạng."),
    ("视野", "shìyě", "thị dã", "danh từ", "tầm nhìn, tầm mắt; tầm hiểu biết", "旅行可以开拓视野。", "Du lịch có thể mở rộng tầm nhìn.",
     "Danh từ, nghĩa gốc là phạm vi mắt nhìn thấy, nghĩa rộng là lĩnh vực tư tưởng, hiểu biết. Kết hợp hay gặp: 开拓视野，扩大视野，公众视野. Trong bài: 再次带进公众视野, một lần nữa đưa vào tầm mắt của công chúng."),
    ("得益", "déyì", "đắc ích", "động từ", "được lợi, được hưởng lợi", "他的成功得益于多年的努力。", "Thành công của anh ấy là nhờ nhiều năm nỗ lực.",
     "Động từ, nghĩa là được lợi, nhận được lợi ích. Hay dùng theo mẫu 得益于……, nhờ vào…, đây là câu mẫu thứ hai. Trong bài: 得益于数字化、信息化的发展, nhờ sự phát triển của số hóa, tin học hóa."),
    ("没得说", "méideshuō", "một đắc thuyết", "tính từ", "không chê vào đâu được, tuyệt vời", "这家餐厅的服务真是没得说。", "Dịch vụ của nhà hàng này thật không chê vào đâu được.",
     "Tính từ khẩu ngữ, nghĩa là không có gì để chê, rất tuyệt. Chữ giữa đọc nhẹ. Trong bài: 为人们带来的便利那真是没得说, sự tiện lợi mang lại cho mọi người thì thật khỏi phải bàn."),
    ("导医", "dǎoyī", "đạo y", "động từ", "hướng dẫn người bệnh đi khám", "导医带我去了三楼的诊室。", "Nhân viên hướng dẫn đưa tôi đến phòng khám ở tầng ba.",
     "Động từ, nghĩa là hướng dẫn bệnh nhân khám chữa bệnh hợp lý; cũng dùng như danh từ chỉ nhân viên làm việc này ở bệnh viện. Trong bài: 寻求导医的帮助, tìm sự giúp đỡ của nhân viên hướng dẫn."),
    ("扫码", "sǎomǎ", "tảo mã", "động từ", "quét mã (QR)", "请扫码点餐。", "Xin quét mã để gọi món.",
     "Động từ ly hợp, nghĩa là quét mã vạch hay mã QR. 扫 là quét, 码 là mã, viết tắt của 二维码, mã hai chiều. Trong bài: 扫码点餐、移动支付, quét mã gọi món, thanh toán di động."),
    ("鸿沟", "hónggōu", "hồng câu", "danh từ", "hố sâu ngăn cách", "老人和年轻人之间存在一道数字鸿沟。", "Giữa người già và người trẻ tồn tại một khoảng cách số.",
     "Danh từ, vốn là tên một con kênh thời cổ, ranh giới giữa nước Sở và nước Hán; nghĩa bóng là ranh giới rõ rệt, khó vượt qua. Lượng từ là 道. Cụm then chốt của bài: 数字鸿沟, khoảng cách số."),
    ("疫情", "yìqíng", "dịch tình", "danh từ", "tình hình dịch bệnh, dịch bệnh", "新冠疫情改变了很多人的生活。", "Dịch COVID đã thay đổi cuộc sống của rất nhiều người.",
     "Danh từ, nghĩa là tình hình phát sinh và lây lan của dịch bệnh. Kết hợp hay gặp: 新冠疫情，疫情防控."),
    ("防控", "fángkòng", "phòng khống", "động từ", "phòng chống và kiểm soát", "政府正在全力防控疫情。", "Chính phủ đang dốc toàn lực phòng chống dịch bệnh.",
     "Động từ, viết tắt của 预防 và 控制, phòng ngừa và kiểm soát. Trong bài: 新冠肺炎疫情防控期间, thời kỳ phòng chống dịch COVID."),
    ("屡屡", "lǚlǚ", "lũ lũ", "phó từ", "nhiều lần, hết lần này đến lần khác", "他上班屡屡迟到。", "Anh ta đi làm hết lần này đến lần khác bị muộn.",
     "Phó từ, văn viết, nghĩa là lặp đi lặp lại nhiều lần, thường nói về việc không hay: 屡屡迟到，屡屡出错. Trong bài: 这样的情况屡屡发生, tình trạng như vậy xảy ra liên tiếp."),
    ("一度", "yídù", "nhất độ", "phó từ", "có một thời, từng có lúc", "他一度对生活失去了信心。", "Có một thời anh ấy đã mất niềm tin vào cuộc sống.",
     "Phó từ, nghĩa là đã từng xảy ra một lần hay một khoảng thời gian, ngụ ý nay đã khác. Đây là câu mẫu thứ sáu. Trong bài: 一度引起社会关注, đã có lúc gây sự chú ý của xã hội."),
    ("年迈", "niánmài", "niên mại", "tính từ", "già cả, tuổi cao", "他每周都回家看望年迈的父母。", "Tuần nào anh ấy cũng về thăm cha mẹ già.",
     "Tính từ, văn viết, nghĩa là tuổi đã cao. Chữ 迈 ở đây là già, cũng có trong 老迈. Trong bài: 不能落下那些年迈的身影, không thể bỏ lại phía sau những bóng dáng tuổi già."),
    ("身影", "shēnyǐng", "thân ảnh", "danh từ", "bóng dáng", "我在人群中看到了妈妈的身影。", "Tôi nhìn thấy bóng dáng mẹ giữa đám đông.",
     "Danh từ, nghĩa là hình bóng, dáng người. Kết hợp hay gặp: 忙碌的身影, bóng dáng tất bật; 高大的身影, bóng dáng cao lớn."),
    ("及", "jí", "cập", "liên từ", "và, cùng (văn viết)", "童话、寓言、故事及科幻小说，都是孩子们喜爱的读物。", "Truyện cổ tích, ngụ ngôn, truyện kể và tiểu thuyết khoa học viễn tưởng đều là sách trẻ em yêu thích.",
     "Liên từ văn viết, nghĩa là và, giống 和, thường đứng trước thành phần cuối cùng của một chuỗi liệt kê. Trong bài: 六十岁及以上人口, dân số từ sáu mươi tuổi trở lên; 及以上 là và cao hơn."),
    ("截至", "jiézhì", "tiệt chí", "giới từ", "tính đến (thời điểm)", "截至目前，尚未收到不良反应报告。", "Tính đến nay vẫn chưa nhận được báo cáo phản ứng phụ nào.",
     "Giới từ, nghĩa là tính đến một thời điểm nào đó, hay gặp trong số liệu thống kê. Phân biệt: 截止 là động từ, nghĩa là hết hạn, như 报名已经截止. Trong bài: 截至今年六月, tính đến tháng sáu năm nay."),
    ("占比", "zhànbǐ", "chiếm tỷ", "danh từ", "tỷ lệ (chiếm trong tổng số)", "女性员工的占比越来越高。", "Tỷ lệ nhân viên nữ ngày càng cao.",
     "Danh từ, nghĩa là tỷ lệ phần trăm mà một số lượng chiếm trong tổng số. Trong bài: 六十岁及以上人群占比为百分之十点三, nhóm từ sáu mươi tuổi trở lên chiếm mười phẩy ba phần trăm."),
    ("顺畅", "shùnchàng", "thuận sướng", "tính từ", "suôn sẻ, thông suốt", "虽然来自不同国家，但同学们的交流很顺畅。", "Tuy đến từ các nước khác nhau, nhưng các bạn học giao tiếp với nhau rất suôn sẻ.",
     "Tính từ, nghĩa là thuận lợi, trôi chảy, không bị cản trở. Kết hợp hay gặp: 交通顺畅，交流顺畅，呼吸顺畅. Trong bài: 更加顺畅地拥抱智能生活, đón nhận cuộc sống thông minh một cách suôn sẻ hơn."),
    ("鉴于", "jiànyú", "giám vu", "giới từ", "xét thấy, căn cứ vào", "鉴于天气原因，比赛推迟了。", "Do thời tiết, trận đấu đã bị hoãn.",
     "Giới từ, văn viết, nghĩa là lấy một tình hình làm tiền đề để cân nhắc, thường đứng đầu câu. Chữ 鉴 là soi xét, như trong 借鉴. Đây là câu mẫu thứ bảy."),
    ("反哺", "fǎnbǔ", "phản bộ", "động từ", "mớm mồi lại; (bóng) con cái báo đáp cha mẹ", "子女长大后应该反哺父母。", "Con cái lớn lên nên báo đáp cha mẹ.",
     "Động từ. 哺 là mớm cho ăn. Tương truyền có loài chim khi lớn lên sẽ tìm mồi mớm cho chim mẹ đã già không bay được. Nghĩa bóng là con cái lớn lên phụng dưỡng cha mẹ: 反哺之情. Trong bài: 文化反哺, thế hệ trẻ truyền lại tri thức cho thế hệ trước."),
    ("别样", "biéyàng", "biệt dạng", "tính từ", "khác lạ, đặc biệt, khác thường", "雨中的西湖有一种别样的美。", "Tây Hồ trong mưa có một vẻ đẹp khác lạ.",
     "Tính từ thuộc tính, nghĩa là kiểu khác, không giống bình thường. Kết hợp hay gặp: 别样的美，别样的人生. Trong bài: 创造别样的精彩, tạo nên những điều tuyệt vời theo một cách khác."),
    ("老花镜", "lǎohuājìng", "lão hoa kính", "danh từ", "kính lão", "奶奶戴上老花镜看报纸。", "Bà đeo kính lão lên để đọc báo.",
     "Danh từ, kính dành cho người mắt bị lão thị. 老花 là lão thị, mắt kém khi về già; 镜 là kính. Trong bài: 有的爷爷奶奶戴上老花镜, có những ông bà đeo kính lão lên."),
    ("乐呵呵", "lèhēhē", "lạc ha ha", "tính từ", "vui vẻ, tươi cười hớn hở", "爷爷见人总是乐呵呵的。", "Ông gặp ai cũng tươi cười hớn hở.",
     "Tính từ, nghĩa là dáng vẻ vui vẻ, hớn hở. Chữ đầu đọc lè. Đây là kiểu tính từ ABB như 绿油油，红彤彤. Trong bài: 乐呵呵地观看网上有趣的短视频, vui vẻ xem những video ngắn thú vị trên mạng."),
    ("浏览", "liúlǎn", "lưu lãm", "động từ", "xem lướt, xem qua; duyệt (web)", "我每天早上都会浏览新闻。", "Sáng nào tôi cũng xem lướt tin tức.",
     "Động từ, nghĩa là xem qua một lượt, đọc lướt. Ngày nay rất hay dùng cho mạng: 浏览网页, duyệt web; 浏览器, trình duyệt. Trong bài: 浏览朋友圈, lướt xem vòng bạn bè trên WeChat."),
    ("美满", "měimǎn", "mỹ mãn", "tính từ", "tốt đẹp, viên mãn, hạnh phúc", "祝你们婚姻美满！", "Chúc hai bạn hôn nhân hạnh phúc viên mãn!",
     "Tính từ, nghĩa là tốt đẹp, trọn vẹn, hạnh phúc. Kết hợp hay gặp: 美满的生活，美满婚姻. Trong bài: 生活上更加幸福、美满."),
    ("选项", "xuǎnxiàng", "tuyển hạng", "danh từ", "lựa chọn, phương án (để chọn)", "本题有四个选项。", "Câu này có bốn phương án lựa chọn.",
     "Danh từ, nghĩa là mục có thể lựa chọn, như các phương án A, B, C, D trong bài thi. Trong bài có hình ảnh rất hay: 给老年人在快时代留个慢选项, để lại cho người già một lựa chọn chậm trong thời đại nhanh."),
    ("人文", "rénwén", "nhân văn", "danh từ", "nhân văn", "这体现了社会的人文关怀。", "Điều này thể hiện sự quan tâm mang tính nhân văn của xã hội.",
     "Danh từ, chỉ tư tưởng lấy con người làm trung tâm, tôn trọng giá trị và quan tâm đến lợi ích của con người. Kết hợp hay gặp: 人文关怀，人文精神，人文学科. Tiểu mục thứ hai của bài: 这体现了信息化时代的人文关怀."),
    ("构建", "gòujiàn", "cấu kiến", "động từ", "xây dựng (sự vật trừu tượng)", "我们要构建新的学科体系。", "Chúng ta cần xây dựng hệ thống học thuật mới.",
     "Động từ, nghĩa là xây dựng, thường dùng cho sự vật trừu tượng như hệ thống, xã hội, mô hình. Khác với 建设 hay 建造 dùng cho công trình cụ thể. Trong bài: 构建更具包容性的智慧老龄社会新形态, xây dựng hình thái mới của xã hội già hóa thông minh, bao trùm hơn."),
    ("多元", "duōyuán", "đa nguyên", "tính từ", "đa dạng, nhiều loại", "这是一个多元的社会。", "Đây là một xã hội đa dạng.",
     "Tính từ, nghĩa là nhiều dạng, không đơn nhất. Tiếng Việt đa nguyên thường dùng trong chính trị, còn 多元 dùng rất rộng, thường dịch là đa dạng: 多元文化, văn hóa đa dạng; 多元选择, lựa chọn đa dạng."),
    ("并举", "bìngjǔ", "tịnh cử", "động từ", "đồng thời tiến hành", "我们要坚持教育与科研并举。", "Chúng ta phải kiên trì song song phát triển giáo dục và nghiên cứu.",
     "Động từ, nghĩa là cùng lúc thực hiện nhiều việc. 并 là cùng nhau, 举 là tiến hành. Hay gặp: 多措并举, nhiều biện pháp cùng lúc; A与B并举. Đây là câu mẫu thứ tám."),
    ("柜员", "guìyuán", "quỹ viên", "danh từ", "nhân viên quầy (giao dịch)", "银行柜员耐心地帮老人办理业务。", "Nhân viên giao dịch ngân hàng kiên nhẫn giúp cụ già làm thủ tục.",
     "Danh từ, chỉ nhân viên làm việc ở quầy, thường là ở ngân hàng: 银行柜员, giao dịch viên. 柜台 là quầy. Trong bài: 机器人柜员, giao dịch viên robot; 人工柜员服务, dịch vụ giao dịch viên là người thật."),
    ("标识", "biāoshí", "tiêu thức", "danh từ", "ký hiệu, biển chỉ dẫn", "医院调大了门诊标识。", "Bệnh viện đã làm to các biển chỉ dẫn khu khám bệnh.",
     "Danh từ, nghĩa là dấu hiệu dùng để nhận biết, như biển báo, biển chỉ dẫn, logo. Từ điển thường đọc biāozhì, sách ghi biāoshí, cả hai cách đều gặp. Trong bài: 调大门诊标识, làm to biển chỉ dẫn ở khu khám ngoại trú."),
    ("在线", "zàixiàn", "tại tuyến", "tính từ", "trực tuyến, online", "现在很多人在线学习汉语。", "Bây giờ nhiều người học tiếng Trung trực tuyến.",
     "Nghĩa là trực tuyến, dịch thẳng từ chữ online của tiếng Anh: 在 là ở, 线 là đường dây. Kết hợp hay gặp: 在线学习，在线支付，在线预约. Trong bài: 改善在线预约系统布局, cải thiện bố cục hệ thống đặt lịch trực tuyến."),
    ("布局", "bùjú", "bố cục", "danh từ", "bố cục, cách bố trí", "这个房间的布局很合理。", "Cách bố trí căn phòng này rất hợp lý.",
     "Danh từ, nghĩa là sự quy hoạch, sắp xếp tổng thể. Âm Hán Việt và nghĩa giống tiếng Việt. Kết hợp: 布局合理，优化布局，产业布局."),
    ("致力", "zhìlì", "trí lực", "động từ", "dốc sức vào, tập trung sức lực vào", "他一生致力于环保事业。", "Cả đời ông dốc sức cho sự nghiệp bảo vệ môi trường.",
     "Động từ, nghĩa là đem sức lực dồn vào một lĩnh vực, thường dùng 致力于. Đây là câu mẫu thứ chín. Trong bài: 致力于优化老年就医环境, dốc sức cải thiện môi trường khám chữa bệnh cho người già."),
    ("优化", "yōuhuà", "ưu hóa", "động từ", "tối ưu hóa, cải thiện", "我们要不断优化用户界面。", "Chúng ta cần không ngừng tối ưu hóa giao diện người dùng.",
     "Động từ, nghĩa là làm cho tốt hơn, cải tiến. Kết hợp hay gặp: 优化设计，优化环境，优化结构，优化布局. Tiếng Việt thường dịch là tối ưu hóa."),
    ("就医", "jiùyī", "tựu y", "động từ", "đi khám chữa bệnh", "一旦感染应该及时就医。", "Một khi bị nhiễm bệnh thì nên đi khám kịp thời.",
     "Động từ, nghĩa là đến chỗ bác sĩ để chữa bệnh. Chữ 就 ở đây là đến gần, như trong 就业, đi làm; 就学, đi học. Trong bài: 就医问诊, đi khám bệnh; 老年就医环境, môi trường khám bệnh của người già."),
    ("界面", "jièmiàn", "giới diện", "danh từ", "giao diện", "这个软件的界面很简洁。", "Giao diện của phần mềm này rất gọn gàng.",
     "Danh từ, chỉ trạng thái hình ảnh hiện trên màn hình điện thoại, máy tính, tức giao diện. Kết hợp hay gặp: 用户界面，优化界面. Trong bài: 打造老年友好界面, tạo ra giao diện thân thiện với người già."),
    ("沟壑", "gōuhè", "câu hác", "danh từ", "khe rãnh; (bóng) hố ngăn cách", "两代人存在难以跨越的沟壑。", "Giữa hai thế hệ tồn tại hố ngăn cách khó vượt qua.",
     "Danh từ, nghĩa gốc là khe núi, rãnh sâu; nghĩa bóng là sự ngăn cách, gần nghĩa với 鸿沟. Chữ thứ hai đọc hè. Trong bài: 填补代际间的数字沟壑, lấp đầy hố ngăn cách số giữa các thế hệ."),
    ("馈赠", "kuìzèng", "quỹ tặng", "động từ", "biếu tặng, tặng", "他带些特产馈赠亲友。", "Anh ấy mang ít đặc sản biếu họ hàng bạn bè.",
     "Động từ, văn viết, nghĩa là tặng quà. Cũng dùng như danh từ, nghĩa là món quà: 数字时代的馈赠, món quà của thời đại số, như trong câu cuối bài."),
    ("信手拈来", "xìnshǒu-niānlái", "tín thủ niêm lai", "thành ngữ", "tiện tay nhặt lấy; viết, nói dễ dàng trôi chảy", "王教授讲课时总能将各种典故信手拈来。", "Giáo sư Vương khi giảng bài luôn dẫn các điển tích một cách dễ dàng.",
     "Thành ngữ. 信手 là tiện tay, 拈 là nhón lấy bằng ngón tay. Thường chỉ khi viết văn có thể tự do dùng từ ngữ, điển tích mà chẳng cần nghĩ ngợi. Trong bài: 年轻人信手拈来的操作, những thao tác người trẻ làm dễ như trở bàn tay."),
    ("图文并茂", "túwén-bìngmào", "đồ văn tịnh mậu", "thành ngữ", "hình ảnh và chữ viết đều phong phú", "这本书图文并茂，很受孩子们欢迎。", "Cuốn sách này hình đẹp chữ hay, rất được trẻ em yêu thích.",
     "Thành ngữ. 图 là hình, 文 là chữ, 并 là cùng, 茂 là tươi tốt: hình ảnh và chữ viết đều phong phú, bổ sung cho nhau. Trong bài: bản hướng dẫn vẽ tay 字迹工整、内容详细、图文并茂."),
    ("力不从心", "lìbùcóngxīn", "lực bất tòng tâm", "thành ngữ", "lực bất tòng tâm", "我年纪渐大，常感到力不从心。", "Tôi ngày một có tuổi, thường thấy lực bất tòng tâm.",
     "Thành ngữ, trong lòng muốn làm nhưng sức lực, khả năng không theo kịp. Âm Hán Việt giống hệt tiếng Việt. Trong bài: 一些老年人对此却感到力不从心."),
    ("秩序井然", "zhìxù-jǐngrán", "trật tự tỉnh nhiên", "thành ngữ", "trật tự ngăn nắp, nề nếp", "比赛结束后，观众依次退场，现场秩序井然。", "Trận đấu kết thúc, khán giả lần lượt ra về, hiện trường trật tự ngăn nắp.",
     "Thành ngữ. 井然 là ngay ngắn, có thứ tự như những ô ruộng hình chữ 井. Cả cụm là quản lý quy củ, có trật tự, không hỗn loạn. Trong bài: 预约挂号使得就医问诊秩序井然."),
    ("一筹莫展", "yìchóu-mòzhǎn", "nhất trù mạc triển", "thành ngữ", "bó tay, không nghĩ ra cách nào", "由于没有任何线索，当地警方一筹莫展。", "Vì không có manh mối nào, cảnh sát địa phương đành bó tay.",
     "Thành ngữ. 筹 là thẻ tre để tính toán, ví như kế sách; 莫展 là không thi triển được. Không có lấy một kế sách nào, tức là bó tay. Trong bài: 一筹莫展的老人, những cụ già bó tay không biết làm thế nào."),
    ("无所适从", "wúsuǒshìcóng", "vô sở thích tòng", "thành ngữ", "không biết theo ai, không biết làm sao", "太多人对他提出建议，弄得他一时间无所适从。", "Quá nhiều người góp ý khiến anh ấy nhất thời không biết nghe theo ai.",
     "Thành ngữ. 适从 là nghe theo: không biết nên nghe theo ai, không biết làm thế nào mới phải. Trong bài: 还在使用老年机的人就会无所适从, những người vẫn dùng điện thoại cục gạch sẽ không biết xoay xở ra sao."),
    ("微不足道", "wēibùzúdào", "vi bất túc đạo", "thành ngữ", "nhỏ bé không đáng kể", "个人的作用是微不足道的。", "Vai trò của cá nhân là nhỏ bé không đáng kể.",
     "Thành ngữ. 微 là nhỏ, 不足道 là không đáng nói đến. Ý nghĩa, giá trị nhỏ đến mức chẳng đáng nhắc tới. Trong bài: 连看似微不足道的生活细节, ngay cả những chi tiết đời sống tưởng chừng nhỏ nhặt."),
    ("风驰电掣", "fēngchí-diànchè", "phong trì điện xế", "thành ngữ", "nhanh như gió cuốn chớp giật", "在百米赛中，运动员们一个个风驰电掣般冲向终点。", "Trong cuộc thi chạy trăm mét, các vận động viên lần lượt lao về đích nhanh như chớp.",
     "Thành ngữ. 驰 là phi nhanh, 掣 là vụt qua, chữ này đọc chè. Hình dung cực kỳ nhanh, như gió thổi chớp giật. Trong bài: 风驰电掣的快时代, thời đại nhanh như gió cuốn."),
]

add("bullets", chapter="Từ mới (51 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 2.2 có 43 từ mới và 8 thành ngữ, chia thành 17 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 没得说 (de) · 乐呵呵 (lè) · 沟壑 (hè) · 风驰电掣 (chè)",
           "Từ của thời đại số: 扫码 · 在线 · 界面 · 浏览 · 点赞 · 疫情 · 占比"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có bốn mươi ba từ mới và tám thành ngữ, tổng cộng năm mươi mốt mục, thầy chia thành mười bảy nhóm nhỏ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe nhé."),
         F(3, "Chú ý cách đọc của một số từ, như 没得说，乐呵呵，沟壑，风驰电掣. Thầy sẽ nhắc khi gặp."),
         F(4, "Bài này có rất nhiều từ của thời đại số như 扫码，在线，界面，浏览，疫情，占比. Đây là những từ các bạn sẽ gặp hằng ngày khi dùng điện thoại hay đọc báo Trung Quốc. Chúng ta bắt đầu.")])

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
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung: số viết bằng chữ Hán, bỏ ngoặc kép])
P = [
    ("语音聊天、视频通话、点赞收藏、转发分享……在社交软件上，年轻人信手拈来的操作，对家里的老年人来说可能会复杂得不行。",
     "Trò chuyện bằng giọng nói, gọi video, bấm thích, lưu lại, chia sẻ… trên các ứng dụng mạng xã hội, những thao tác mà người trẻ làm dễ như trở bàn tay, với người già trong nhà có thể lại phức tạp vô cùng.",
     ["Bài mở đầu bằng một chuỗi liệt kê các thao tác quen thuộc: 语音聊天，视频通话，点赞收藏，转发分享. 社交软件 là phần mềm mạng xã hội.",
      "信手拈来的操作 là những thao tác làm dễ dàng, tiện tay. 复杂得不行 là phức tạp vô cùng: 得不行 là bổ ngữ chỉ mức độ cực cao, câu mẫu thứ nhất của bài. Hai vế đối lập: người trẻ thì dễ như không, người già thì khó vô cùng."]),
    ("不久前，浙江杭州一个女孩为外婆手绘了一份“微信使用说明书”，字迹工整、内容详细、图文并茂，此举相当暖心，打动了一众网友，也将老年人如何更好适应数字生活的话题，再次带进公众视野。",
     "Cách đây không lâu, một cô gái ở Hàng Châu, Chiết Giang đã tự tay vẽ cho bà ngoại một bản “hướng dẫn sử dụng WeChat”, chữ viết ngay ngắn, nội dung chi tiết, hình ảnh và chữ đều phong phú. Việc làm này thật ấm lòng, làm cảm động đông đảo cư dân mạng, và cũng một lần nữa đưa chủ đề làm sao để người già thích nghi tốt hơn với đời sống số vào tầm mắt của công chúng.",
     ["Đây là sự việc dẫn nhập của bài bình luận. 为外婆手绘了一份说明书: 为 ở đây đọc wèi, nghĩa là cho, vì. 说明书 là bản hướng dẫn sử dụng. Ba cụm bốn chữ 字迹工整、内容详细、图文并茂 tạo nhịp văn cân đối.",
      "此举相当暖心: 此举 là việc làm này, 相当 là khá, rất. 打动了一众网友 là làm cảm động đông đảo cư dân mạng. 将……带进公众视野 là đưa… vào tầm mắt công chúng; 将 ở đây giống 把. Đây là cách mở bài thường gặp của bài bình luận thời sự: từ một sự kiện nhỏ, dẫn ra một vấn đề xã hội lớn."]),
    ("如今，得益于数字化、信息化的发展，智能生活加速推进，为人们带来的便利那真是没得说。然而，一些老年人对此却感到力不从心。",
     "Ngày nay, nhờ sự phát triển của số hóa và tin học hóa, cuộc sống thông minh đang tăng tốc, sự tiện lợi nó mang lại cho mọi người thì thật khỏi phải bàn. Thế nhưng, một số người già lại cảm thấy lực bất tòng tâm trước điều đó.",
     ["得益于数字化、信息化的发展 là nhờ sự phát triển của số hóa và tin học hóa, câu mẫu 得益于. 加速推进 là đẩy nhanh, tăng tốc. 那真是没得说 là thì thật không chê vào đâu được; chữ 那 ở đây nhấn mạnh, mang giọng khẩu ngữ.",
      "然而 là thế nhưng, chuyển ý. 对此 là đối với điều này. 感到力不从心 là cảm thấy lực bất tòng tâm. Câu này nêu luận điểm của đoạn: tiện lợi cho đa số, nhưng khó khăn cho người già."]),
    ("在火车站，电子客票的推广极大地节省了旅客的出行时间，却也让需要出行却不会网上购票的老人不知如何是好；在医院，预约挂号使得就医问诊秩序井然，但一筹莫展的老人不得不站在挂号机前寻求导医的帮助；",
     "Ở ga tàu, việc phổ biến vé điện tử đã tiết kiệm rất nhiều thời gian đi lại cho hành khách, nhưng cũng khiến những cụ già cần đi xa mà không biết mua vé trên mạng chẳng biết phải làm sao; ở bệnh viện, đặt lịch đăng ký khám giúp việc khám chữa bệnh trật tự ngăn nắp, nhưng những cụ già bó tay đành phải đứng trước máy đăng ký, nhờ nhân viên hướng dẫn giúp đỡ;",
     ["Đoạn này dùng phép liệt kê theo địa điểm: 在火车站，在医院，在餐厅, mỗi nơi đều có hai mặt: tiện lợi cho đa số, nhưng khó khăn cho người già.",
      "电子客票的推广 là việc phổ biến vé điện tử. 不知如何是好 là không biết làm sao cho phải, câu mẫu thứ ba 不知……好. 预约挂号 là đặt lịch, đăng ký khám bệnh; 使得 là khiến cho. 一筹莫展 là bó tay. 寻求导医的帮助 là tìm kiếm sự giúp đỡ của nhân viên hướng dẫn."]),
    ("在餐厅，扫码点餐、移动支付方便又卫生，而还在使用老年机的人就会无所适从。对上了年纪的人来说，连看似微不足道的生活细节，也有可能构成一道数字鸿沟，造成日常生活的不便。",
     "Ở nhà hàng, quét mã gọi món, thanh toán di động vừa tiện vừa vệ sinh, còn những người vẫn dùng điện thoại cho người già thì sẽ không biết xoay xở ra sao. Với người đã có tuổi, ngay cả những chi tiết đời sống tưởng chừng nhỏ nhặt cũng có thể tạo thành một khoảng cách số, gây bất tiện cho cuộc sống hằng ngày.",
     ["扫码点餐 là quét mã gọi món; 移动支付 là thanh toán di động. 老年机 là điện thoại dành cho người già, loại phím bấm to, không có chức năng thông minh. 无所适从 là không biết làm sao.",
      "连看似微不足道的生活细节，也有可能构成一道数字鸿沟: mẫu 连……也……, ngay cả… cũng…, câu mẫu thứ tư. 看似 là trông có vẻ, tưởng chừng. 构成一道数字鸿沟 là tạo thành một hố ngăn cách số, lượng từ của 鸿沟 là 道."]),
    ("更不用说新冠肺炎疫情防控期间，由于老年人没有健康码以致无法乘坐公交、甚至无法出入小区的情况屡屡发生，一度引起社会关注。",
     "Chưa kể trong thời kỳ phòng chống dịch COVID, tình trạng người già vì không có mã sức khỏe mà không thể đi xe buýt, thậm chí không thể ra vào khu dân cư liên tục xảy ra, đã có lúc gây sự chú ý của cả xã hội.",
     ["更不用说 là càng không cần phải nói, chưa kể đến, nối tiếp mẫu 连……也…… ở câu trước: ngay cả việc nhỏ cũng khó, huống chi thời kỳ dịch bệnh.",
      "由于……以致…… là do… đến nỗi…, câu mẫu thứ năm; 以致 dẫn ra kết quả xấu. 乘坐公交 là đi xe buýt; 出入小区 là ra vào khu chung cư. 屡屡发生 là xảy ra liên tiếp. 一度引起社会关注 là đã có thời gây sự chú ý của xã hội, câu mẫu 一度."]),
    ("【帮助老人顺利融入信息化社会是义务也是责任】\n数字时代，不能落下那些年迈的身影。第七次全国人口普查结果显示，我国60岁及以上人口已达2.64亿人。",
     "【Giúp người già hòa nhập suôn sẻ vào xã hội thông tin là nghĩa vụ và cũng là trách nhiệm】 Trong thời đại số, không thể bỏ lại phía sau những bóng dáng tuổi già. Kết quả cuộc Tổng điều tra dân số toàn quốc lần thứ bảy cho thấy, dân số từ 60 tuổi trở lên của nước ta đã lên tới 264 triệu người.",
     ["Tiểu mục thứ nhất nêu luận điểm: giúp người già hòa nhập xã hội thông tin vừa là nghĩa vụ, vừa là trách nhiệm.",
      "不能落下那些年迈的身影: chữ 落 ở đây đọc là, 落下 nghĩa là bỏ sót lại, để rơi lại phía sau. 年迈的身影 là bóng dáng tuổi già, cách nói hình ảnh để chỉ người già.",
      "第七次全国人口普查 là cuộc Tổng điều tra dân số toàn quốc lần thứ bảy, tiến hành năm hai nghìn không trăm hai mươi. 六十岁及以上 là từ sáu mươi tuổi trở lên. 已达二点六四亿人 là đã đạt hai trăm sáu mươi tư triệu người. Số liệu được dùng làm luận cứ cho luận điểm."],
     "帮助老人顺利融入信息化社会是义务也是责任。数字时代，不能落下那些年迈的身影。第七次全国人口普查结果显示，我国六十岁及以上人口已达二点六四亿人。"),
    ("“十四五”时期，全国60周岁及以上老年人口预计将超过3亿，占总人口比例将超过20%，中国将进入中度老龄化社会。根据统计，截至今年6月，在超过9亿的网民中，60岁及以上人群占比为10.3%。",
     "Trong thời kỳ “Quy hoạch 5 năm lần thứ 14”, dân số cao tuổi từ đủ 60 tuổi trở lên trên cả nước dự kiến sẽ vượt 300 triệu, chiếm hơn 20% tổng dân số, Trung Quốc sẽ bước vào xã hội già hóa ở mức trung bình. Theo thống kê, tính đến tháng 6 năm nay, trong hơn 900 triệu người dùng Internet, nhóm từ 60 tuổi trở lên chiếm 10,3%.",
     ["十四五时期 là giai đoạn quy hoạch năm năm lần thứ mười bốn. 周岁 là tuổi tròn, tính theo ngày sinh. 占总人口比例将超过百分之二十 là chiếm hơn hai mươi phần trăm tổng dân số. 中度老龄化社会 là xã hội già hóa mức trung bình.",
      "截至今年六月 là tính đến tháng sáu năm nay. 网民 là cư dân mạng, người dùng Internet. 占比为百分之十点三 là chiếm mười phẩy ba phần trăm. Hai con số đặt cạnh nhau cho thấy: người già chiếm hơn một phần năm dân số, nhưng chỉ chiếm khoảng một phần mười người dùng mạng."],
     "十四五时期，全国六十周岁及以上老年人口预计将超过三亿，占总人口比例将超过百分之二十，中国将进入中度老龄化社会。根据统计，截至今年六月，在超过九亿的网民中，六十岁及以上人群占比为百分之十点三。"),
    ("让老年人口更好分享信息化时代的发展红利，需要以更多的耐心帮助他们，从而让他们更加顺畅地拥抱智能生活。",
     "Muốn để người cao tuổi được chia sẻ tốt hơn thành quả phát triển của thời đại thông tin, cần giúp đỡ họ với nhiều kiên nhẫn hơn, từ đó giúp họ đón nhận cuộc sống thông minh một cách suôn sẻ hơn.",
     ["分享发展红利 là chia sẻ thành quả, lợi ích của sự phát triển; các bạn nhớ từ 红利 trong bài trước: 共享城市发展带来的红利.",
      "以更多的耐心帮助他们: 以 là bằng, dùng: bằng nhiều kiên nhẫn hơn. 从而 là từ đó, nhờ đó. 拥抱智能生活 là ôm lấy, đón nhận cuộc sống thông minh, một cách nói hình ảnh rất hay dùng trên báo chí."]),
    ("如果说传统的教育模式是从父母一代到子女一代的知识传递，那么在信息化社会，鉴于老年人所面对的“数字困境”，这就需要年轻人来帮助父母和祖父母辈，进行“文化反哺”。",
     "Nếu nói mô hình giáo dục truyền thống là sự truyền thụ tri thức từ thế hệ cha mẹ sang thế hệ con cái, thì trong xã hội thông tin, xét đến “cảnh khó số” mà người già phải đối mặt, cần có người trẻ giúp đỡ thế hệ cha mẹ và ông bà, thực hiện việc “mớm ngược văn hóa”.",
     ["如果说……，那么…… là nếu nói… thì…, dùng để so sánh hai sự việc. 知识传递 là truyền đạt tri thức.",
      "鉴于老年人所面对的数字困境 là xét thấy cảnh khó khăn số mà người già đối mặt, câu mẫu 鉴于. 所面对的 có chữ 所 trước động từ, văn viết. 祖父母辈 là thế hệ ông bà. 文化反哺 là con cháu truyền lại kỹ năng mới cho ông bà cha mẹ, ngược với truyền thống."]),
    ("在浙江嘉兴图书馆，有一门专门课程，教授如何开关手机、怎么联网、怎样使用相机等“常规操作”。2019年，8名馆员共组织了159场讲座，吸引了60岁到89岁的众多老人参与。",
     "Ở thư viện Gia Hưng, Chiết Giang, có một khóa học chuyên dạy những “thao tác cơ bản” như cách bật tắt điện thoại, cách kết nối mạng, cách dùng máy ảnh. Năm 2019, 8 nhân viên thư viện đã tổ chức tổng cộng 159 buổi giảng, thu hút đông đảo người già từ 60 đến 89 tuổi tham gia.",
     ["Đây là ví dụ thực tế đầu tiên về việc giúp người già. 一门专门课程 là một khóa học chuyên đề, lượng từ của 课程 là 门. 教授 ở đây là động từ, đọc jiāoshòu, nghĩa là giảng dạy; khác với danh từ 教授 jiàoshòu là giáo sư.",
      "开关手机 là bật tắt điện thoại; 联网 là kết nối mạng; 常规操作 là thao tác thông thường. 馆员 là nhân viên thư viện. 讲座 là buổi giảng, buổi tọa đàm. 吸引了众多老人参与 là thu hút đông đảo người già tham gia."],
     "在浙江嘉兴图书馆，有一门专门课程，教授如何开关手机、怎么联网、怎样使用相机等常规操作。二零一九年，八名馆员共组织了一百五十九场讲座，吸引了六十岁到八十九岁的众多老人参与。"),
    ("如今，越来越多的老年人拥抱数字生活，创造别样的精彩。有的爷爷奶奶戴上老花镜，认真学起了手机扫码、手机观看新闻、视频通话，跟孩子们的交流变得顺畅无阻；",
     "Ngày nay, ngày càng nhiều người già đón nhận đời sống số, tạo nên những điều tuyệt vời theo cách riêng. Có những ông bà đeo kính lão lên, chăm chú học quét mã bằng điện thoại, xem tin tức trên điện thoại, gọi video, việc trò chuyện với con cháu trở nên thông suốt không trở ngại;",
     ["拥抱数字生活 là đón nhận đời sống số. 创造别样的精彩 là tạo nên những điều tuyệt vời theo một kiểu khác; 精彩 ở đây dùng như danh từ.",
      "学起了 là bắt đầu học: 起 làm bổ ngữ xu hướng, biểu thị bắt đầu một hành động. 顺畅无阻 là trôi chảy, không bị cản trở. Đoạn văn vẽ ra một bức tranh tươi sáng, đối lập với đoạn đầu bài."]),
    ("不少老年人也开始乐呵呵地观看网上有趣的短视频，浏览朋友圈，给亲戚朋友点赞。老年人的“数字需求”得到满足，使他们在物质上和精神上更加丰富，生活上更加幸福、美满。",
     "nhiều người già cũng bắt đầu vui vẻ xem những video ngắn thú vị trên mạng, lướt xem vòng bạn bè, bấm thích cho họ hàng bạn bè. “Nhu cầu số” của người già được đáp ứng, khiến họ phong phú hơn cả về vật chất lẫn tinh thần, cuộc sống hạnh phúc, viên mãn hơn.",
     ["乐呵呵地观看 là vui vẻ xem, tính từ ABB làm trạng ngữ với 地. 短视频 là video ngắn, như trên Douyin, tức TikTok bản Trung Quốc. 朋友圈 là vòng bạn bè, chức năng đăng trạng thái của WeChat. 点赞 là bấm thích.",
      "数字需求得到满足 là nhu cầu số được đáp ứng. 在物质上和精神上 là về mặt vật chất và tinh thần. Mẫu 在……上 chỉ phương diện."]),
    ("【有温度的社会需要包容不同的选项】\n【这体现了信息化时代的人文关怀】\n对一些互联网平台来说，要针对老年人的需求提供替代选择，构建更具包容性的智慧老龄社会新形态。",
     "【Xã hội có hơi ấm cần bao dung những lựa chọn khác nhau – Điều này thể hiện sự quan tâm nhân văn của thời đại thông tin】 Đối với một số nền tảng Internet, cần nhắm vào nhu cầu của người già mà đưa ra những lựa chọn thay thế, xây dựng hình thái mới của xã hội già hóa thông minh, có tính bao trùm hơn.",
     ["Tiểu mục thứ hai gồm hai dòng: 有温度的社会 là xã hội có hơi ấm, tức xã hội biết quan tâm con người; 包容不同的选项 là bao dung những lựa chọn khác nhau; 人文关怀 là sự quan tâm mang tính nhân văn.",
      "针对……提供替代选择 là nhắm vào… đưa ra lựa chọn thay thế. 更具包容性 là có tính bao trùm hơn, 具 là có, văn viết. 智慧老龄社会 là xã hội già hóa thông minh; 智慧 ở đây giống 智能, như 智慧城市, thành phố thông minh."]),
    ("有专家建议，除了在技术开发中更加注重老年人的需求和习惯外，在公共政策制定和公共服务方面，也要给老年人提供多元选择和替代方案。",
     "Có chuyên gia đề xuất, ngoài việc chú trọng hơn đến nhu cầu và thói quen của người già trong quá trình phát triển công nghệ, thì trong việc hoạch định chính sách công và cung cấp dịch vụ công, cũng cần dành cho người già những lựa chọn đa dạng và phương án thay thế.",
     ["除了……外，……也…… là ngoài… ra, … cũng…. 注重 là chú trọng. 技术开发 là phát triển công nghệ.",
      "公共政策制定 là việc hoạch định chính sách công. 多元选择和替代方案 là lựa chọn đa dạng và phương án thay thế. Ý chính: không thể bắt mọi người già phải theo kịp công nghệ, mà công nghệ và chính sách cũng phải chừa chỗ cho họ."]),
    ("现实中，不少地方多措并举，帮助老年人融入移动互联网世界。这些年来，银行在普遍设立了ATM机、机器人柜员后，还始终保留着适合老年人的人工柜员服务；",
     "Trên thực tế, nhiều nơi đã áp dụng đồng thời nhiều biện pháp, giúp người già hòa nhập vào thế giới Internet di động. Mấy năm nay, sau khi đã lắp đặt rộng rãi máy ATM và giao dịch viên robot, các ngân hàng vẫn luôn giữ lại dịch vụ giao dịch viên là người thật, phù hợp với người già;",
     ["多措并举 là nhiều biện pháp cùng lúc, câu mẫu 并举; 措 là 措施, biện pháp. 移动互联网 là Internet di động.",
      "普遍设立了 là đã lắp đặt rộng rãi. 机器人柜员 là giao dịch viên robot. 始终保留着 là trước sau vẫn giữ lại. 人工柜员服务 là dịch vụ do nhân viên trực tiếp phục vụ; 人工 ở đây là do con người làm, đối lập với máy móc."]),
    ("在上海，有医院调大门诊标识、诊间字体，改善在线预约系统布局，致力于优化老年就医环境，打造“老年友好界面”；在浙江杭州，市民卡和健康码深度融合，老年人刷一下卡就能看病就医、公交出行。",
     "Ở Thượng Hải, có bệnh viện đã làm to biển chỉ dẫn khu khám bệnh và cỡ chữ trong phòng khám, cải thiện bố cục hệ thống đặt lịch trực tuyến, dốc sức cải thiện môi trường khám chữa bệnh cho người già, tạo ra “giao diện thân thiện với người cao tuổi”; ở Hàng Châu, Chiết Giang, thẻ công dân và mã sức khỏe được tích hợp sâu, người già chỉ cần quẹt thẻ là có thể đi khám bệnh, đi xe buýt.",
     ["调大门诊标识、诊间字体: chữ 调 ở đây đọc tiáo, nghĩa là điều chỉnh; 调大 là chỉnh cho to lên. 门诊 là khám ngoại trú; 诊间 là phòng khám.",
      "致力于优化老年就医环境 là dốc sức cải thiện môi trường khám bệnh của người già, câu mẫu 致力于. 打造 là tạo dựng. 市民卡 là thẻ công dân thành phố. 深度融合 là tích hợp sâu. 刷一下卡 là quẹt thẻ một cái."]),
    ("由此可见，给老年人在风驰电掣的“快时代”留个“慢选项”，能填补代际间的数字沟壑，也让老年人享受到数字时代的馈赠。因为今天的他们，就是明天的我们。",
     "Từ đó có thể thấy, để lại cho người già một “lựa chọn chậm” trong “thời đại nhanh” như gió cuốn chớp giật, có thể lấp đầy hố ngăn cách số giữa các thế hệ, cũng để người già được tận hưởng món quà của thời đại số. Bởi vì họ của hôm nay, chính là chúng ta của ngày mai.",
     ["由此可见 là từ đó có thể thấy, dùng để rút ra kết luận, câu mẫu cuối cùng. 快时代 và 慢选项 là cặp đối lập rất hay: thời đại thì nhanh, nhưng cần chừa một lựa chọn chậm cho người già. 代际间 là giữa các thế hệ.",
      "Câu kết 今天的他们，就是明天的我们 là câu nổi tiếng nhất của bài: họ của hôm nay chính là chúng ta của ngày mai. Ai rồi cũng sẽ già, giúp người già hôm nay cũng là giúp chính mình mai sau."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 信息化社会：“一个都不能少”", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa. Bài được cải biên từ bài bình luận 微信使用说明书为何暖心, Vì sao bản hướng dẫn dùng WeChat lại ấm lòng, đăng trên 人民日报 ngày mười ba tháng mười năm hai nghìn không trăm hai mươi, tác giả là 盛玉雷.",
         F(0, "Thầy chia bài thành mười tám đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng. Các dòng trong ngoặc vuông là tiểu mục của bài."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "").replace("【", "").replace("】", "。").replace("\n", "")
    zsize = 54 if len(zh) <= 100 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", "").replace("【", "").replace("】", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Tóm tắt nội dung", section="Bài khóa 课文", title="Bố cục bài khóa", size=35,
    items=["## Dẫn nhập: 女孩为外婆手绘“微信使用说明书” → 老年人如何适应数字生活",
           "## Hiện tượng: 智能生活很便利，老年人却力不从心",
           "火车站：不会网上购票 · 医院：不会预约挂号 · 餐厅：不会扫码点餐 · 疫情期间：没有健康码",
           "## Luận điểm 1: 帮助老人融入信息化社会是义务也是责任",
           "老龄化数据 → 需要耐心 → “文化反哺” · 嘉兴图书馆的手机课程",
           "## Luận điểm 2: 有温度的社会需要包容不同的选项",
           "提供替代选择 · 银行保留人工柜员 · 上海医院“老年友好界面” · 杭州市民卡 → 给“快时代”留个“慢选项”"],
    say=["Bây giờ chúng ta cùng nhìn lại bố cục của bài bình luận.",
         F(0, "Phần dẫn nhập: một cô gái tự tay vẽ cho bà ngoại bản hướng dẫn dùng WeChat; từ chuyện nhỏ ấy, tác giả dẫn ra vấn đề lớn: người già thích nghi với đời sống số như thế nào."),
         F(1, "Tiếp theo là hiện tượng: cuộc sống thông minh rất tiện lợi, nhưng người già lại lực bất tòng tâm."),
         F(2, "Tác giả liệt kê bốn tình huống: ở ga tàu không biết mua vé trên mạng, ở bệnh viện không biết đặt lịch khám, ở nhà hàng không biết quét mã gọi món, và thời dịch bệnh không có mã sức khỏe."),
         F(3, "Luận điểm thứ nhất: giúp người già hòa nhập xã hội thông tin là nghĩa vụ và cũng là trách nhiệm."),
         F(4, "Luận cứ là số liệu già hóa dân số; vì vậy cần kiên nhẫn, cần con cháu mớm ngược văn hóa; và ví dụ là khóa học điện thoại ở thư viện Gia Hưng."),
         F(5, "Luận điểm thứ hai: một xã hội có hơi ấm cần bao dung những lựa chọn khác nhau."),
         F(6, "Ví dụ là ngân hàng giữ lại giao dịch viên, bệnh viện Thượng Hải làm giao diện thân thiện với người già, Hàng Châu tích hợp thẻ công dân. Kết luận: hãy để lại một lựa chọn chậm trong thời đại nhanh, vì họ của hôm nay chính là chúng ta của ngày mai.")])

# ======================= CÂU MẪU =======================
add("bullets", chapter="Câu mẫu: 得不行 · 得益于 · 不知……好 · 更不用说", section="Câu mẫu 重点句型", title="1. ……得不行  ·  2. 得益于……", size=33,
    items=["## Tính từ/động từ tâm lý + 得不行: mức độ rất cao (khẩu ngữ) – đến mức không chịu nổi",
           "在社交软件上，年轻人信手拈来的操作，对家里的老年人来说可能会复杂得不行。",
           "一家人终于要去旅游了，儿子兴奋得不行。",
           "和很多孩子一样，上学时我对写作文讨厌得不行。",
           "## 得益于……: nhờ vào…, được lợi từ… (động từ)",
           "如今，得益于数字化、信息化的发展，智能生活加速推进，为人们带来的便利那真是没得说。",
           "据销售人员介绍，本月汽车销量大涨主要得益于多款新车的上市以及购车税费的减免政策。",
           "这里的环境非常优美，得益于政府的环境保护措施，也得益于公众自觉的环保意识。"],
    say=["Bây giờ chúng ta sang phần câu mẫu trọng điểm. Bài này có mười câu mẫu, thầy giảng hai câu một lần.",
         F(0, "Câu mẫu thứ nhất: 得不行. Đặt sau tính từ hoặc động từ chỉ tâm lý, biểu thị mức độ rất cao, mang màu sắc khẩu ngữ. Tiếng Việt dịch là vô cùng, đến mức không chịu nổi, kinh khủng."),
         F(1, "Ví dụ một, từ bài khóa: 在社交软件上，年轻人信手拈来的操作，对家里的老年人来说可能会复杂得不行。 Phức tạp vô cùng."),
         F(2, "Ví dụ hai: 一家人终于要去旅游了，儿子兴奋得不行。 Cả nhà cuối cùng cũng sắp đi du lịch, cậu con trai phấn khích không tả nổi."),
         F(3, "Ví dụ ba: 和很多孩子一样，上学时我对写作文讨厌得不行。 Giống như nhiều đứa trẻ khác, hồi đi học tôi ghét viết văn kinh khủng."),
         F(4, "Câu mẫu thứ hai: 得益于, là động từ, nghĩa là được lợi ở mặt nào đó, nhờ vào cái gì. Phía sau là nguyên nhân tích cực."),
         F(5, "Ví dụ một, từ bài khóa: 得益于数字化、信息化的发展，智能生活加速推进。 Nhờ sự phát triển của số hóa, cuộc sống thông minh đang tăng tốc."),
         F(6, "Ví dụ hai: 据销售人员介绍，本月汽车销量大涨主要得益于多款新车的上市以及购车税费的减免政策。 Theo nhân viên bán hàng, doanh số ô tô tháng này tăng mạnh chủ yếu nhờ nhiều mẫu xe mới ra mắt và chính sách giảm miễn thuế phí mua xe."),
         F(7, "Ví dụ ba: 这里的环境非常优美，得益于政府的环境保护措施，也得益于公众自觉的环保意识。 Môi trường ở đây rất đẹp, là nhờ các biện pháp bảo vệ môi trường của chính phủ, và cũng nhờ ý thức bảo vệ môi trường tự giác của người dân.")])

add("bullets", section="Câu mẫu 重点句型", title="3. 不知……好  ·  4. 连……也……，更不用说……", size=33,
    items=["## 不知 + 如何/怎么/说什么… + (才)好: không biết… thế nào cho phải",
           "在火车站，电子客票的推广……却也让需要出行却不会网上购票的老人不知如何是好。",
           "这件事很复杂，涉及到许多人的切身利益，我不知如何解决才好。",
           "看他紧张得手心都是汗，我也不知说什么好。",
           "## 连A也……，更不用说B了: ngay cả A cũng…, huống chi B",
           "很多传统戏曲连中国人也不会唱，更不用说外国人了。",
           "他连那里的语言也不会说，更不用说融入当地社会了。"],
    say=[F(0, "Câu mẫu thứ ba: 不知……好. Giữa hai chữ là các cụm như 如何是，怎么办，说什么, thường có thêm 才. Nghĩa là không biết làm thế nào mới phải, thể hiện sự lúng túng."),
         F(1, "Ví dụ một, từ bài khóa: 电子客票的推广极大地节省了旅客的出行时间，却也让需要出行却不会网上购票的老人不知如何是好。 Khiến những cụ già không biết mua vé trên mạng chẳng biết làm sao cho phải. 不知如何是好 là cụm cố định rất hay dùng."),
         F(2, "Ví dụ hai: 这件事很复杂，涉及到许多人的切身利益，我不知如何解决才好。 Việc này rất phức tạp, liên quan đến lợi ích thiết thân của nhiều người, tôi không biết giải quyết thế nào mới phải."),
         F(3, "Ví dụ ba: 看他紧张得手心都是汗，我也不知说什么好。 Thấy anh ấy căng thẳng đến mức lòng bàn tay đầy mồ hôi, tôi cũng chẳng biết nói gì cho phải."),
         F(4, "Câu mẫu thứ tư: 连A也……，更不用说B了. Vế trước đưa ra trường hợp dễ nhất mà vẫn không làm được, vế sau suy ra trường hợp khó hơn thì càng không. Tiếng Việt dịch là ngay cả… cũng…, huống chi…. Trong bài khóa: 连看似微不足道的生活细节，也有可能构成一道数字鸿沟。更不用说新冠肺炎疫情防控期间……"),
         F(5, "Ví dụ: 很多传统戏曲连中国人也不会唱，更不用说外国人了。 Nhiều loại hí khúc truyền thống ngay cả người Trung Quốc cũng không biết hát, huống chi người nước ngoài."),
         F(6, "Ví dụ: 他连那里的语言也不会说，更不用说融入当地社会了。 Anh ấy ngay cả ngôn ngữ ở đó cũng không biết nói, nói gì đến hòa nhập vào xã hội địa phương. Các bạn có thấy câu này rất giống tình cảnh của người lao động nhập cư trong bài trước không?")])

add("bullets", chapter="Câu mẫu: 以致 · 一度 · 鉴于 · 并举", section="Câu mẫu 重点句型", title="5. ……，以致……  ·  6. 一度……", size=33,
    items=["## 以致: dẫn ra kết quả (thường là xấu, ngoài ý muốn) – đến nỗi, dẫn đến",
           "由于老年人没有健康码以致无法乘坐公交、甚至无法出入小区的情况屡屡发生。",
           "他最近经常熬夜加班，以致身体出现了亚健康状况。",
           "由于资金迟迟不能到位，以致这个项目一直停留在图纸上。",
           "## 一度: đã từng có một lần / một thời gian (nay đã khác)",
           "……由于老年人没有健康码以致无法乘坐公交……的情况屡屡发生，一度引起社会关注。",
           "他考研失败后，一度心灰意冷，对生活失去了信心。",
           "这里一度大厦林立、车水马龙，如今却是一片荒芜。"],
    say=[F(0, "Câu mẫu thứ năm: 以致. Đứng đầu vế sau, dẫn ra kết quả do nguyên nhân phía trước gây nên, thường là kết quả xấu, ngoài ý muốn. Hay đi với 由于 ở vế trước. Tiếng Việt dịch là đến nỗi, dẫn đến."),
         F(1, "Ví dụ một, từ bài khóa: 由于老年人没有健康码以致无法乘坐公交、甚至无法出入小区的情况屡屡发生。 Vì không có mã sức khỏe mà đến nỗi không đi được xe buýt."),
         F(2, "Ví dụ hai: 他最近经常熬夜加班，以致身体出现了亚健康状况。 Dạo này anh ấy thường thức khuya tăng ca, đến nỗi cơ thể rơi vào tình trạng nửa khỏe nửa yếu. 亚健康 là tình trạng sức khỏe dưới mức tốt."),
         F(3, "Ví dụ ba: 由于资金迟迟不能到位，以致这个项目一直停留在图纸上。 Vì vốn mãi chưa về, dự án này đến giờ vẫn chỉ nằm trên bản vẽ."),
         F(4, "Câu mẫu thứ sáu: 一度. Phó từ, nghĩa là đã từng có một lần, hoặc một khoảng thời gian, ngụ ý tình hình nay đã thay đổi. Tiếng Việt dịch là có một thời, đã có lúc."),
         F(5, "Ví dụ một, từ bài khóa: 这样的情况屡屡发生，一度引起社会关注。 Tình trạng ấy đã có lúc gây sự chú ý của xã hội."),
         F(6, "Ví dụ hai: 他考研失败后，一度心灰意冷，对生活失去了信心。 Sau khi thi cao học thất bại, có một thời anh ấy chán nản, mất niềm tin vào cuộc sống. 心灰意冷 là nản lòng thoái chí."),
         F(7, "Ví dụ ba: 这里一度大厦林立、车水马龙，如今却是一片荒芜。 Nơi này từng có một thời cao ốc san sát, xe cộ tấp nập, nay lại hoang vắng tiêu điều.")])

add("bullets", section="Câu mẫu 重点句型", title="7. 鉴于……，……  ·  8. ……并举", size=33,
    items=["## 鉴于 + tình hình, (结论/措施): xét thấy… nên… (văn viết, đứng đầu câu)",
           "鉴于老年人所面对的“数字困境”，这就需要年轻人来帮助父母和祖父母辈，进行“文化反哺”。",
           "鉴于目前全球金融危机尚无转危为安的迹象，许多人开始推测经济迟滞将带来何种政治影响。",
           "鉴于气候变化带来的不确定性，该国农业部长呼吁本国消费者减少肉类的购买。",
           "## A与B并举 / 多措并举: đồng thời tiến hành",
           "坚持“引资”与“引智”并举，积极引进先进技术、管理经验和高素质人才。",
           "租售并举的消费观念已经为许多市民所接受。"],
    say=[F(0, "Câu mẫu thứ bảy: 鉴于. Giới từ văn viết, đứng đầu câu, nêu một tình hình làm căn cứ, rồi vế sau đưa ra kết luận hay biện pháp. Tiếng Việt dịch là xét thấy, căn cứ vào, do."),
         F(1, "Ví dụ một, từ bài khóa: 鉴于老年人所面对的数字困境，这就需要年轻人来帮助父母和祖父母辈，进行文化反哺。"),
         F(2, "Ví dụ hai: 鉴于目前全球金融危机尚无转危为安的迹象，许多人开始推测经济迟滞将带来何种政治影响。 Xét thấy khủng hoảng tài chính toàn cầu hiện chưa có dấu hiệu chuyển nguy thành an, nhiều người bắt đầu phỏng đoán sự trì trệ kinh tế sẽ gây ra ảnh hưởng chính trị gì."),
         F(3, "Ví dụ ba: 鉴于气候变化带来的不确定性，该国农业部长呼吁本国消费者减少肉类的购买。 Do những bất định mà biến đổi khí hậu mang lại, bộ trưởng nông nghiệp nước này kêu gọi người tiêu dùng trong nước giảm mua thịt."),
         F(4, "Câu mẫu thứ tám: 并举, nghĩa là đồng thời tiến hành. Hai dạng thường gặp: A与B并举, và cụm bốn chữ như 多措并举, nhiều biện pháp cùng lúc, trong bài khóa: 不少地方多措并举，帮助老年人融入移动互联网世界。"),
         F(5, "Ví dụ: 坚持引资与引智并举，积极引进先进技术、管理经验和高素质人才。 Kiên trì song song thu hút vốn và thu hút trí tuệ, tích cực đưa vào công nghệ tiên tiến, kinh nghiệm quản lý và nhân tài chất lượng cao."),
         F(6, "Ví dụ: 租售并举的消费观念已经为许多市民所接受。 Quan niệm tiêu dùng vừa thuê vừa mua đã được nhiều người dân chấp nhận. Các bạn có nhận ra mẫu bị động 为……所…… đã học ở bài trước không?")])

add("bullets", chapter="Câu mẫu: 致力于 · 由此可见", section="Câu mẫu 重点句型", title="9. 致力（于）……  ·  10. 由此可见（一斑）", size=33,
    items=["## 致力于 + lĩnh vực / mục tiêu: dốc sức vào…",
           "有医院调大门诊标识、诊间字体，改善在线预约系统布局，致力于优化老年就医环境。",
           "医生们正致力于不断改进这项技术，并对其长期疗效进行研究。",
           "李老师用尽毕生的心血投身教学，致力于祖国的教育事业。",
           "## 由此可见，……: từ đó có thể thấy (rút ra kết luận) · ……由此可见一斑: qua đó thấy được phần nào",
           "最近，教育主管部门频频查问学生的复习情况，由此可见他们对这次考试的重视。",
           "龟兔赛跑中的兔子在睡梦中被乌龟赶超，由此可见，一时领先不代表一世领先。",
           "过去“黄沙弥漫”的荒漠如今被改造成“国家生态公园”，政府对环保工作的重视由此可见一斑。"],
    say=[F(0, "Câu mẫu thứ chín: 致力于. Phía sau là lĩnh vực hay mục tiêu mà người ta dồn sức vào, văn viết, trang trọng. Tiếng Việt dịch là dốc sức vào, tận tâm với."),
         F(1, "Ví dụ một, từ bài khóa: 有医院调大门诊标识、诊间字体，改善在线预约系统布局，致力于优化老年就医环境。"),
         F(2, "Ví dụ hai: 医生们正致力于不断改进这项技术，并对其长期疗效进行研究。 Các bác sĩ đang dốc sức không ngừng cải tiến kỹ thuật này, đồng thời nghiên cứu hiệu quả điều trị lâu dài của nó."),
         F(3, "Ví dụ ba: 李老师用尽毕生的心血投身教学，致力于祖国的教育事业。 Thầy Lý dồn hết tâm huyết cả đời vào việc dạy học, tận tụy với sự nghiệp giáo dục của Tổ quốc."),
         F(4, "Câu mẫu thứ mười: 由此可见. Đứng đầu câu kết luận, nghĩa là từ đó có thể thấy. Dạng thứ hai là 由此可见一斑, đứng cuối câu: 一斑 là một đốm trên da báo, nhìn một đốm mà biết cả con báo, tức là qua đó thấy được phần nào. Trong bài khóa: 由此可见，给老年人在风驰电掣的快时代留个慢选项……"),
         F(5, "Ví dụ: 最近，教育主管部门频频查问学生的复习情况，由此可见他们对这次考试的重视。 Gần đây, cơ quan quản lý giáo dục liên tục hỏi han tình hình ôn tập của học sinh, từ đó có thể thấy họ coi trọng kỳ thi này thế nào."),
         F(6, "Ví dụ: 龟兔赛跑中的兔子在睡梦中被乌龟赶超，由此可见，一时领先不代表一世领先。 Trong truyện rùa và thỏ, chú thỏ bị rùa vượt qua khi đang ngủ, từ đó có thể thấy, dẫn trước nhất thời không có nghĩa là dẫn trước cả đời."),
         F(7, "Ví dụ: 过去黄沙弥漫的荒漠如今被改造成国家生态公园，政府对环保工作的重视由此可见一斑。 Vùng hoang mạc cát vàng mù mịt ngày trước nay được cải tạo thành công viên sinh thái quốc gia, qua đó đủ thấy chính phủ coi trọng công tác bảo vệ môi trường đến mức nào.")])

# ======================= KẾT HỢP TỪ =======================
add("bullets", chapter="Kết hợp từ (词语搭配)", section="Kết hợp từ 词语搭配", title="Kết hợp từ (1): 一众 · 视野 · 鸿沟", size=34,
    items=["## 一众：～朋友 · ～工作人员 · ～游客 · ～网友",
           "自1997年于香港亮相后，该品牌瞬间成为一众时尚达人的最爱。",
           "## 视野：公众～ · 全球～ · 进入～ · 退出～ · 扩大～ · 开拓～",
           "由于经营不善，这个老品牌慢慢淡出了人们的视野。",
           "## 鸿沟：数字～ · 年龄～ · 知识～ · 认知～",
           "由于这对夫妻存在难以逾越的年龄鸿沟，他们磨合了几年后还是以离婚告终。"],
    say=["Tiếp theo là phần kết hợp từ, 词语搭配. Các bạn hãy học cả cụm nhé.",
         F(0, "Từ thứ nhất: 一众. Hay đi với 朋友，工作人员，游客，网友. Trong bài: 打动了一众网友."),
         F(1, "Ví dụ: 自一九九七年于香港亮相后，该品牌瞬间成为一众时尚达人的最爱。 Từ khi ra mắt ở Hồng Kông năm một nghìn chín trăm chín mươi bảy, thương hiệu này lập tức trở thành món yêu thích của đông đảo tín đồ thời trang. Và: 该剧不仅汇集了一众老演员，更吸引了一批有实力的新人加盟。"),
         F(2, "Từ thứ hai: 视野. Hay gặp 公众视野，全球视野，进入视野，退出视野，扩大视野，开拓视野. Trong bài: 再次带进公众视野."),
         F(3, "Ví dụ: 由于经营不善，这个老品牌慢慢淡出了人们的视野。 Do kinh doanh kém, thương hiệu lâu đời này dần biến mất khỏi tầm mắt mọi người. Và: 我热爱旅行，因为可以在旅行中认识很多朋友，开拓视野。"),
         F(4, "Từ thứ ba: 鸿沟. Hay gặp 数字鸿沟，年龄鸿沟，知识鸿沟，认知鸿沟. Trong bài: 构成一道数字鸿沟."),
         F(5, "Ví dụ: 由于这对夫妻存在难以逾越的年龄鸿沟，他们磨合了几年后还是以离婚告终。 Vì cặp vợ chồng này có khoảng cách tuổi tác khó vượt qua, sau mấy năm cố gắng thích nghi với nhau họ vẫn đi đến ly hôn. Và về 知识鸿沟: 大众媒介传送的信息越多，二者之间的知识鸿沟也就越有扩大的趋势, thông tin truyền thông càng nhiều thì khoảng cách tri thức giữa người giàu và người nghèo càng có xu hướng nới rộng.")])

add("bullets", section="Kết hợp từ 词语搭配", title="Kết hợp từ (2): 顺畅 · 人文 · 优化", size=34,
    items=["## 顺畅：交通～ · 交流～ · 心情～ · 呼吸～",
           "在我们的日常交际中，想要交流顺畅，就要提高自己的沟通技巧。",
           "## 人文：～关怀 · ～精神 · ～学科 · ～素养 · ～景观",
           "要在全社会培养友好和谐的环境意识，弘扬崇尚科学的文明风尚，倡导以人为本的人文精神。",
           "## 优化：～环境 · ～结构 · ～方法 · ～布局",
           "根据产业振兴规划，政府将调整产业布局，优化结构，深化改革以及加强管理。"],
    say=[F(0, "Từ thứ tư: 顺畅. Hay gặp 交通顺畅，交流顺畅，心情顺畅，呼吸顺畅. Ví dụ: 由于该市严格执行交通法，违章行车的行为大大减少，交通顺畅多了。 Vì thành phố thực thi nghiêm luật giao thông, hành vi lái xe vi phạm giảm hẳn, giao thông thông suốt hơn nhiều."),
         F(1, "Ví dụ khác: 在我们的日常交际中，想要交流顺畅，就要提高自己的沟通技巧。 Trong giao tiếp hằng ngày, muốn trao đổi suôn sẻ thì phải nâng cao kỹ năng giao tiếp của mình."),
         F(2, "Từ thứ năm: 人文. Hay gặp 人文关怀，人文精神，人文学科，人文素养，人文景观. 人文学科 là các ngành khoa học nhân văn; 人文景观 là cảnh quan nhân văn, do con người tạo ra, đối lập với cảnh quan tự nhiên."),
         F(3, "Ví dụ: 要在全社会培养友好和谐的环境意识，弘扬崇尚科学的文明风尚，倡导以人为本的人文精神。 Cần bồi dưỡng ý thức môi trường thân thiện, hài hòa trong toàn xã hội, phát huy nếp sống văn minh tôn trọng khoa học, đề cao tinh thần nhân văn lấy con người làm gốc."),
         F(4, "Từ thứ sáu: 优化. Hay gặp 优化环境，优化结构，优化方法，优化布局. Trong bài: 致力于优化老年就医环境."),
         F(5, "Ví dụ: 根据产业振兴规划，政府将调整产业布局，优化结构，深化改革以及加强管理。 Theo quy hoạch chấn hưng công nghiệp, chính phủ sẽ điều chỉnh bố cục ngành, tối ưu hóa cơ cấu, đi sâu cải cách và tăng cường quản lý.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 课后练习", title="Bài tập 1: Chọn thành ngữ điền vào chỗ trống (1)", reveal=True, size=33,
    items=["## Từ cho sẵn: 无所适从 · 图文并茂 · 秩序井然 · 风驰电掣 · 一筹莫展 · 力不从心 · 信手拈来 · 微不足道",
           "(1) 黑暗中，小小的烛光看起来是那么___，但却给人带来了无限的勇气与希望。",
           "Đáp án: 微不足道",
           "(2) 熟记成语，写文章时便能___，毫不费力。",
           "Đáp án: 信手拈来",
           "(3) 趁年轻多做一些事吧，一旦年老体衰，想干也___了。",
           "Đáp án: 力不从心",
           "(4) 虽然毕业于名牌大学，他还是因为找不到工作而___。",
           "Đáp án: 一筹莫展"],
    say=["Phần luyện tập, 趁热打铁. Bài tập một: chọn thành ngữ thích hợp điền vào chỗ trống.",
         F(0, "Có tám thành ngữ: 无所适从，图文并茂，秩序井然，风驰电掣，一筹莫展，力不从心，信手拈来，微不足道. Mỗi thành ngữ dùng một lần."),
         F(1, "Câu một: 黑暗中，小小的烛光看起来是那么什么，但却给人带来了无限的勇气与希望。 Trong bóng tối, ánh nến nhỏ bé trông thật thế nào, nhưng lại mang đến cho người ta dũng khí và hy vọng vô hạn. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 微不足道. Ánh nến trông nhỏ bé không đáng kể, nhưng lại mang đến hy vọng. Chữ 但 cho thấy hai vế đối lập."),
         F(3, "Câu hai: 熟记成语，写文章时便能什么，毫不费力。 Thuộc lòng thành ngữ, khi viết văn sẽ có thể thế nào, chẳng tốn chút sức nào."),
         F(4, "Đáp án: 信手拈来. Viết văn dùng thành ngữ dễ dàng, tiện tay là có."),
         F(5, "Câu ba: 趁年轻多做一些事吧，一旦年老体衰，想干也什么了。 Hãy tranh thủ lúc còn trẻ làm nhiều việc, một khi già yếu rồi, muốn làm cũng thế nào."),
         F(6, "Đáp án: 力不从心. 想干也力不从心了, muốn làm cũng lực bất tòng tâm rồi."),
         F(7, "Câu bốn: 虽然毕业于名牌大学，他还是因为找不到工作而什么。 Tuy tốt nghiệp trường danh tiếng, anh ấy vẫn vì không tìm được việc mà thế nào."),
         F(8, "Đáp án: 一筹莫展. Vì không tìm được việc mà bó tay, không biết làm sao.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 1: Chọn thành ngữ điền vào chỗ trống (2)", reveal=True, size=33,
    items=["(5) 英语等级考试中，所有学生都按要求参加考试，没有出现任何异常情况，考场___。",
           "Đáp án: 秩序井然",
           "(6) 如果父母双方的态度和意见总是不一致，就会使孩子感到___。",
           "Đáp án: 无所适从",
           "(7) 本书充分考虑到学生的接受程度和兴趣点，___，可读性很强。",
           "Đáp án: 图文并茂",
           "(8) 司机突然把车开得___一般，车上的乘客都给吓得直冒冷汗。",
           "Đáp án: 风驰电掣"],
    say=[F(0, "Câu năm: 英语等级考试中，所有学生都按要求参加考试，没有出现任何异常情况，考场什么。 Trong kỳ thi chứng chỉ tiếng Anh, mọi thí sinh đều dự thi theo đúng yêu cầu, không có bất kỳ sự cố nào, phòng thi thế nào."),
         F(1, "Đáp án: 秩序井然. Phòng thi trật tự ngăn nắp."),
         F(2, "Câu sáu: 如果父母双方的态度和意见总是不一致，就会使孩子感到什么。 Nếu thái độ và ý kiến của cha và mẹ luôn không thống nhất, sẽ khiến đứa trẻ cảm thấy thế nào."),
         F(3, "Đáp án: 无所适从. Đứa trẻ không biết nên nghe theo ai, đúng nghĩa đen của thành ngữ này."),
         F(4, "Câu bảy: 本书充分考虑到学生的接受程度和兴趣点，什么，可读性很强。 Cuốn sách cân nhắc kỹ mức độ tiếp thu và điểm hứng thú của học sinh, thế nào, rất dễ đọc."),
         F(5, "Đáp án: 图文并茂. Hình ảnh và chữ đều phong phú, nên 可读性很强, tính dễ đọc rất cao."),
         F(6, "Câu tám: 司机突然把车开得什么一般，车上的乘客都给吓得直冒冷汗。 Tài xế đột nhiên lái xe như thế nào, hành khách trên xe đều sợ toát mồ hôi lạnh."),
         F(7, "Đáp án: 风驰电掣. 开得风驰电掣一般, lái nhanh như gió cuốn chớp giật. Mẫu 像……一般 hay 风驰电掣般 rất hay gặp với thành ngữ này.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn đáp án đúng", reveal=True, size=32,
    items=["(1) 对待工作他从来都是一丝不苟的，他的教案书写（ ）、格式规范，称得上教案中的精品。 A.整洁 B.工整 C.整齐 D.齐整",
           "Đáp án: B. 工整 – 书写工整, chữ viết ngay ngắn",
           "(2) 读书开阔了我的（ ），陶冶了我的性情，使我获益匪浅。 A.视力 B.视角 C.视野 D.视线",
           "Đáp án: C. 视野 – 开阔视野, mở rộng tầm nhìn",
           "(3) 这几年政府加大空气污染治理力度，颇有成效，我感到呼吸（ ）了许多。 A.流畅 B.通顺 C.顺利 D.顺畅",
           "Đáp án: D. 顺畅 – 呼吸顺畅, thở dễ chịu",
           "(4) 成功是对执着者的一种（ ），失败是对追求者的一种考验。 A.赠送 B.回赠 C.馈赠 D.赠给",
           "Đáp án: C. 馈赠 – danh từ: món quà"],
    say=["Bài tập hai: chọn đáp án đúng.",
         F(0, "Câu một: 对待工作他从来都是一丝不苟的，他的教案书写什么、格式规范，称得上教案中的精品。 Anh ấy luôn làm việc tỉ mỉ, giáo án của anh chữ viết thế nào, thể thức chuẩn mực, xứng đáng là giáo án mẫu mực. Bốn lựa chọn: 整洁，工整，整齐，齐整."),
         F(1, "Đáp án: B, 工整. Nói về chữ viết, ta dùng 书写工整，字迹工整. 整洁 là sạch sẽ gọn gàng, nói về phòng ốc, quần áo; 整齐 và 齐整 là đều đặn, ngay hàng thẳng lối."),
         F(2, "Câu hai: 读书开阔了我的什么，陶冶了我的性情，使我获益匪浅。 Đọc sách đã mở rộng cái gì của tôi, hun đúc tính tình tôi, giúp tôi được lợi không ít. Bốn lựa chọn: 视力，视角，视野，视线."),
         F(3, "Đáp án: C, 视野. 开阔视野 là mở rộng tầm nhìn, tầm hiểu biết. 视力 là thị lực; 视角 là góc nhìn; 视线 là đường nhìn, ánh mắt."),
         F(4, "Câu ba: 这几年政府加大空气污染治理力度，颇有成效，我感到呼吸什么了许多。 Mấy năm nay chính phủ đẩy mạnh xử lý ô nhiễm không khí, khá có hiệu quả, tôi cảm thấy hít thở thế nào hơn nhiều. Bốn lựa chọn: 流畅，通顺，顺利，顺畅."),
         F(5, "Đáp án: D, 顺畅. 呼吸顺畅 là thở thông suốt, dễ chịu, đúng như phần kết hợp từ. 流畅 là trôi chảy, nói về văn viết, lời nói; 通顺 là câu văn xuôi tai; 顺利 là thuận lợi, nói về công việc."),
         F(6, "Câu bốn: 成功是对执着者的一种什么，失败是对追求者的一种考验。 Thành công là một thứ gì đó dành cho người kiên trì, thất bại là một thử thách dành cho người theo đuổi. Bốn lựa chọn: 赠送，回赠，馈赠，赠给."),
         F(7, "Đáp án: C, 馈赠. Sau 一种 cần một danh từ; trong bốn từ chỉ có 馈赠 dùng được như danh từ, nghĩa là món quà, đối xứng với 考验 ở vế sau.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ và câu mẫu cho sẵn để trả lời", reveal=True, size=32,
    items=["(1) 老人熟悉社交软件上的操作吗？（……得不行）",
           "Đáp án gợi ý: 很多老人不太熟悉。年轻人信手拈来的点赞、转发、视频通话等操作，对他们来说复杂得不行。",
           "(2) 请说说新冠肺炎疫情期间，健康码的重要性。（一度）",
           "Đáp án gợi ý: 疫情期间，健康码是出入通行的电子凭证。很多老人因为没有健康码，无法乘坐公交、出入小区，这种情况一度引起社会关注。",
           "(3) 如何帮助老年人融入信息化社会？（鉴于……，……并举，致力于……）",
           "Đáp án gợi ý: 鉴于老年人面对的“数字困境”，社会应该多措并举：年轻人进行“文化反哺”，银行保留人工服务，互联网平台致力于打造“老年友好界面”。"],
    say=["Bài tập ba: dùng từ ngữ và câu mẫu cho sẵn để trả lời câu hỏi. Đây là câu hỏi mở, thầy đưa ra đáp án gợi ý.",
         F(0, "Câu một: 老人熟悉社交软件上的操作吗？ Người già có quen thao tác trên mạng xã hội không? Dùng 得不行. Các bạn tạm dừng và thử trả lời nhé."),
         F(1, "Đáp án gợi ý: 很多老人不太熟悉。年轻人信手拈来的点赞、转发、视频通话等操作，对他们来说复杂得不行。 Nhiều người già không quen lắm. Những thao tác người trẻ làm dễ như không, như bấm thích, chia sẻ, gọi video, đối với họ lại phức tạp vô cùng."),
         F(2, "Câu hai: 请说说新冠肺炎疫情期间，健康码的重要性。 Hãy nói về tầm quan trọng của mã sức khỏe trong thời kỳ dịch COVID. Dùng 一度."),
         F(3, "Đáp án gợi ý: 疫情期间，健康码是出入通行的电子凭证。很多老人因为没有健康码，无法乘坐公交、出入小区，这种情况一度引起社会关注。 Trong thời kỳ dịch, mã sức khỏe là giấy thông hành điện tử. Nhiều cụ già vì không có mã nên không đi được xe buýt, không ra vào được khu dân cư, tình trạng này đã có lúc gây chú ý của xã hội. 凭证 là giấy chứng nhận, bằng chứng."),
         F(4, "Câu ba: 如何帮助老年人融入信息化社会？ Làm thế nào giúp người già hòa nhập xã hội thông tin? Dùng 鉴于，并举 và 致力于."),
         F(5, "Đáp án gợi ý: 鉴于老年人面对的数字困境，社会应该多措并举：年轻人进行文化反哺，银行保留人工服务，互联网平台致力于打造老年友好界面。 Xét thấy cảnh khó số mà người già gặp phải, xã hội nên áp dụng nhiều biện pháp cùng lúc: người trẻ mớm ngược văn hóa, ngân hàng giữ dịch vụ nhân viên, các nền tảng Internet dốc sức tạo giao diện thân thiện với người già.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Dùng từ cho sẵn điền vào đoạn văn", reveal=True, size=32,
    items=["## Từ cho sẵn: 顺畅 · 鸿沟 · 人文 · 浏览 · 打造 · 无所适从 · 力不从心",
           "当年轻一代拥抱数字时代、尽情地享受数字红利时，一些老年人却对智能技术感到___。对上了年纪的他们来说，学习新技能实在是___。如何让老年人___地使用新一代的智能技术，缩小数字___，不仅关系到千家万户，更是国家现代化建设和社会文明进步的必答题。",
           "Đáp án: 无所适从 · 力不从心 · 顺畅 · 鸿沟",
           "2021年，北京市推动开展智能技术的适老化及无障碍改造工作，如___更为人性化的手机界面，使老年人能更轻松地___手机网页，充分兼顾了老年人和特殊人群的需求，体现了信息化社会的___关怀。",
           "Đáp án: 打造 · 浏览 · 人文"],
    say=["Bài tập bốn: dùng bảy từ cho sẵn điền vào đoạn văn: 顺畅，鸿沟，人文，浏览，打造，无所适从，力不从心.",
         F(1, "Đoạn một: 当年轻一代拥抱数字时代、尽情地享受数字红利时，一些老年人却对智能技术感到什么。对上了年纪的他们来说，学习新技能实在是什么。如何让老年人什么地使用新一代的智能技术，缩小数字什么，不仅关系到千家万户，更是国家现代化建设和社会文明进步的必答题。 Các bạn tạm dừng và điền nhé."),
         F(2, "Đáp án: 对智能技术感到无所适从, cảm thấy không biết xoay xở ra sao với công nghệ thông minh; 学习新技能实在是力不从心, học kỹ năng mới thật là lực bất tòng tâm; 顺畅地使用, sử dụng suôn sẻ; 缩小数字鸿沟, thu hẹp khoảng cách số. Hai chỗ trống đầu, nếu đổi cho nhau cũng có thể chấp nhận, nhưng 实在是力不从心 là cách nói tự nhiên nhất. 必答题 là câu hỏi bắt buộc phải trả lời."),
         F(3, "Đoạn hai: 二零二一年，北京市推动开展智能技术的适老化及无障碍改造工作，如什么更为人性化的手机界面，使老年人能更轻松地什么手机网页，充分兼顾了老年人和特殊人群的需求，体现了信息化社会的什么关怀。"),
         F(4, "Đáp án: 打造更为人性化的手机界面, tạo ra giao diện điện thoại thân thiện hơn; 更轻松地浏览手机网页, lướt web trên điện thoại dễ dàng hơn; 人文关怀, sự quan tâm nhân văn. 适老化 là điều chỉnh cho phù hợp với người già; 无障碍改造 là cải tạo không rào cản, dành cho người khuyết tật.")])

# ======================= THẢO LUẬN =======================
add("bullets", chapter="Thảo luận", section="Thảo luận 讨论", title="Thảo luận: liên hệ Việt Nam", reveal=True, size=33,
    items=["(1) 你身边的老年人使用智能手机吗？情况如何？",
           "Đáp án gợi ý: 我的爷爷奶奶也用智能手机，他们最常用的是视频通话和看新闻，但是网上购物、扫码支付对他们来说还是复杂得不行。",
           "(2) 我们年轻人可以给身边的老年人提供怎样的帮助？",
           "Đáp án gợi ý: 我们可以像那个杭州女孩一样，耐心地教他们，给他们写一份简单的说明书，进行“文化反哺”。",
           "(3) 社会是否应该给老年人保留“慢选项”？为什么？",
           "Đáp án gợi ý: 应该。因为不是每个老人都能学会新技术，况且今天的他们，就是明天的我们。"],
    say=["Bây giờ chúng ta cùng thảo luận. Thầy đưa ra đáp án gợi ý bằng tiếng Trung, các bạn hãy thử nói theo ý mình trước nhé.",
         F(0, "Câu một: 你身边的老年人使用智能手机吗？情况如何？ Những người già bên cạnh bạn có dùng điện thoại thông minh không?"),
         F(1, "Gợi ý: 我的爷爷奶奶也用智能手机，他们最常用的是视频通话和看新闻，但是网上购物、扫码支付对他们来说还是复杂得不行。 Ông bà tôi cũng dùng điện thoại thông minh, thường dùng nhất là gọi video và xem tin tức, nhưng mua sắm trên mạng, quét mã thanh toán thì với họ vẫn phức tạp vô cùng. Ở Việt Nam, nhiều ông bà gọi video với con cháu ở xa rất thành thạo, nhưng chuyển khoản hay đặt lịch khám online thì vẫn phải nhờ con cháu."),
         F(2, "Câu hai: 我们年轻人可以给身边的老年人提供怎样的帮助？ Người trẻ có thể giúp người già như thế nào?"),
         F(3, "Gợi ý: 我们可以像那个杭州女孩一样，耐心地教他们，给他们写一份简单的说明书，进行文化反哺。 Chúng ta có thể giống cô gái Hàng Châu, kiên nhẫn dạy ông bà, viết cho họ một bản hướng dẫn đơn giản, thực hiện việc mớm ngược văn hóa."),
         F(4, "Câu ba, thầy thêm vào: 社会是否应该给老年人保留慢选项？为什么？ Xã hội có nên giữ lại lựa chọn chậm cho người già không? Vì sao?"),
         F(5, "Gợi ý: 应该。因为不是每个老人都能学会新技术，况且今天的他们，就是明天的我们。 Nên. Vì không phải cụ già nào cũng học được công nghệ mới, hơn nữa, họ của hôm nay chính là chúng ta của ngày mai. Câu trả lời dùng lại 况且 và câu kết của bài khóa.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết", section="Tổng kết", title="Tổng kết bài 2.2", size=34,
    items=["Nội dung: 数字鸿沟 · 文化反哺 · 给“快时代”留个“慢选项” – 今天的他们，就是明天的我们",
           "Từ vựng trọng tâm: 视野 · 得益 · 鸿沟 · 屡屡 · 一度 · 年迈 · 截至 · 顺畅 · 鉴于 · 反哺 · 浏览 · 构建 · 多元 · 并举 · 致力 · 优化 · 界面 · 馈赠",
           "Thành ngữ: 信手拈来 · 图文并茂 · 力不从心 · 秩序井然 · 一筹莫展 · 无所适从 · 微不足道 · 风驰电掣",
           "Câu mẫu: 得不行 · 得益于 · 不知……好 · 连……也……，更不用说 · 以致 · 一度 · 鉴于 · 并举 · 致力于 · 由此可见",
           "Bài tập về nhà: phỏng vấn ông bà, cha mẹ về việc dùng điện thoại thông minh; viết 200 chữ, dùng ít nhất 3 câu mẫu"],
    say=["Chúng ta cùng tổng kết bài hai chấm hai.",
         F(0, "Về nội dung: người già đang đứng trước khoảng cách số, 数字鸿沟. Người trẻ cần mớm ngược văn hóa, 文化反哺, còn xã hội cần để lại một lựa chọn chậm trong thời đại nhanh. Và đừng quên câu kết: 今天的他们，就是明天的我们。"),
         F(1, "Về từ vựng, các bạn cần đặc biệt nhớ: 视野，得益，鸿沟，屡屡，一度，年迈，截至，顺畅，鉴于，反哺，浏览，构建，多元，并举，致力，优化，界面，馈赠."),
         F(2, "Về thành ngữ: 信手拈来，图文并茂，力不从心，秩序井然，一筹莫展，无所适从，微不足道，风驰电掣."),
         F(3, "Về câu mẫu: 得不行, mức độ rất cao; 得益于, nhờ vào; 不知……好, không biết làm sao cho phải; 连……也……，更不用说……, ngay cả… cũng…, huống chi…; 以致, đến nỗi; 一度, có một thời; 鉴于, xét thấy; 并举, đồng thời tiến hành; 致力于, dốc sức vào; và 由此可见, từ đó có thể thấy."),
         F(4, "Bài tập về nhà: theo gợi ý phần ôn tập của đơn vị, các bạn hãy hỏi ông bà hoặc cha mẹ: bắt đầu dùng điện thoại thông minh từ khi nào, thường dùng ứng dụng gì, gặp khó khăn gì, có ai dạy không. Sau đó viết khoảng hai trăm chữ tiếng Trung, dùng ít nhất ba câu mẫu vừa học."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Bài sau, bài hai chấm ba, là bài cuối của Đơn vị hai: 群体性孤独：网络社交正在扼杀深度关系, Cô đơn tập thể: mạng xã hội đang bóp chết những mối quan hệ sâu sắc. Chúng ta sẽ bàn về chức năng chỉ hiện ba ngày trên WeChat, và vì sao càng kết nối, con người lại càng cô đơn. Hẹn gặp lại các bạn. Chúc các bạn học tốt!"])

lesson = {
    "title": "顶石中文 – Bài 2.2: 信息化社会：“一个都不能少” (Xã hội thông tin: không ai bị bỏ lại)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"新冠": "新官",            # xīnguān
                    "落下": "辣下",            # làxia (bỏ lại phía sau)
                    "教授如何": "交授如何",    # jiāoshòu (động từ: dạy)
                    "乐呵呵": "勒呵呵",        # lèhēhē
                    "调大": "条大",            # tiáodà
                    "没得说": "没的说",        # méideshuō
                    "为许多": "维许多",        # 为……所: wéi
                    "为外婆": "位外婆",        # wèi
                    "沟壑": "沟贺",            # gōuhè
                    "风驰电掣": "风驰电彻",    # chè
                    "一筹": "亦筹",            # yìchóu
                    "转发": "转发",
                    "相机": "相机"},
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds22.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
