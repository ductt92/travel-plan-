#!/usr/bin/env python3
"""Kịch bản bài giảng 顶石中文 – Bài 8.1 «“大头条”对簿“小油条”». Chạy để sinh ds81.json."""
import json
import os

TAG = "顶石中文 · Bài 8.1 · “大头条”对簿“小油条”"
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
    zh="“大头条”对簿“小油条”", py="“Dà tóutiáo” duìbù “xiǎo yóutiáo”",
    vi="Bài 8.1: “Đại Đầu Điều” ra tòa với “Tiểu Du Điều”",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng giáo trình 顶石中文, Đỉnh cao tiếng Trung.",
         {"t": "Hôm nay chúng ta bước sang Đơn vị tám, 法律篇, chủ đề Pháp luật, cũng là đơn vị cuối cùng của giáo trình. Bài đầu tiên là bài tám chấm một: 大头条对簿小油条。 Nghĩa là: Đại Đầu Điều ra tòa với Tiểu Du Điều.",
          "cap": "Hôm nay chúng ta bước sang Đơn vị 8, 法律篇, chủ đề Pháp luật, cũng là đơn vị cuối cùng của giáo trình. Bài đầu tiên là bài 8.1: “大头条”对簿“小油条”。 Nghĩa là: “Đại Đầu Điều” ra tòa với “Tiểu Du Điều”."},
         "Tên bài là một cách chơi chữ. 今日头条 là ứng dụng tin tức nổi tiếng nhất Trung Quốc, của công ty mẹ ByteDance, chủ sở hữu TikTok. Còn 今日油条 là một tiệm ăn sáng bán quẩy. 头条 là tin trang nhất, 油条 là cái quẩy, hai từ chỉ khác nhau đúng một âm tiết. Năm hai nghìn không trăm hai mươi, ông lớn internet đã kiện tiệm quẩy nhỏ ra tòa vì tội nhái nhãn hiệu.",
         "Qua câu chuyện vừa buồn cười vừa nghiêm túc này, chúng ta sẽ tìm hiểu về nhãn hiệu, quyền sở hữu trí tuệ, hàng nhái và chuyện ăn theo thương hiệu lớn. Đây cũng là vấn đề rất nóng ở Việt Nam đấy."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài báo về vụ kiện nhãn hiệu giữa 《今日头条》 và tiệm quẩy “今日油条”",
           "Nắm vững 50 từ mới, kèm âm Hán Việt và ví dụ",
           "11 mẫu câu: 酷似 · 直呼 · 任……也 · 揣着明白装糊涂 · 令……不解 · 乍听起来 · 明摆着 · 就……而言 · 近乎 · 说到底 · 将……落到实处",
           "Kết hợp từ: 蹭～ · 经受～ · 恶意～ và 12 thành ngữ, quán dụng ngữ",
           "Luyện tập theo sách; liên hệ: hàng nhái và “đăng ký chặn trước” nhãn hiệu ở Việt Nam"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu bài báo về vụ kiện nhãn hiệu giữa ứng dụng 今日头条 và tiệm quẩy 今日油条: vì sao tiệm quẩy bị kiện, các luật sư nói gì, và doanh nghiệp nên bảo vệ nhãn hiệu thế nào."),
         F(1, "Thứ hai, nắm vững năm mươi từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học mười một mẫu câu trọng điểm, như 酷似，任也，揣着明白装糊涂，乍听起来，就而言, và 落到实处."),
         F(3, "Thứ tư, học các kết hợp từ với 蹭，经受，恶意, cùng mười hai thành ngữ và quán dụng ngữ, trong đó có rất nhiều từ lóng mạng rất thú vị như 抱大腿，抖机灵，脑洞大开."),
         F(4, "Thứ năm, làm bài luyện tập của sách, và liên hệ với chuyện hàng nhái, ăn theo thương hiệu ở Việt Nam."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 课前思考", title="Câu hỏi trước bài học 课前思考", reveal=True, size=35,
    items=["(1) 你周围的人有没有买到过假货的经历？",
           "Đáp án gợi ý: 有。我朋友在网上买过一双运动鞋，收到以后才发现是假货，跟图片上的完全不一样。",
           "(2) 有的人会知假买假，你认为是出于什么心理呢？",
           "Đáp án gợi ý: 有的人是贪便宜，买不起正品；有的人是爱面子，觉得用名牌有面子，假的也无所谓。",
           "(3) 在你们国家有哪些打击盗版侵权的法律？",
           "Đáp án gợi ý: 越南有《知识产权法》，保护商标、专利和著作权；侵权的人要承担民事、行政甚至刑事责任。"],
    say=["Chúng ta bắt đầu bằng ba câu hỏi trước bài học, 课前思考. Thầy đọc câu hỏi, các bạn tạm dừng để tự trả lời bằng tiếng Trung, rồi nghe câu trả lời gợi ý nhé.",
         F(0, "Câu một: 你周围的人有没有买到过假货的经历？ Những người xung quanh bạn có ai từng mua phải hàng giả chưa? 假货 là hàng giả."),
         F(1, "Gợi ý: 有。我朋友在网上买过一双运动鞋，收到以后才发现是假货，跟图片上的完全不一样。 Có. Bạn tôi từng mua một đôi giày thể thao trên mạng, nhận hàng rồi mới phát hiện là hàng giả, khác hẳn với ảnh."),
         F(2, "Câu hai: 有的人会知假买假，你认为是出于什么心理呢？ Có người biết là hàng giả mà vẫn mua, bạn cho rằng đó là xuất phát từ tâm lý gì? 知假买假 là biết giả vẫn mua."),
         F(3, "Gợi ý: 有的人是贪便宜，买不起正品；有的人是爱面子，觉得用名牌有面子，假的也无所谓。 Có người ham rẻ, không mua nổi hàng chính hãng; có người sĩ diện, thấy dùng hàng hiệu là oai, giả cũng chẳng sao. 正品 là hàng chính hãng."),
         F(4, "Câu ba: 在你们国家有哪些打击盗版侵权的法律？ Ở nước bạn có những luật nào chống làm lậu và xâm phạm quyền? 盗版 là làm lậu, in lậu."),
         F(5, "Gợi ý: 越南有知识产权法，保护商标、专利和著作权；侵权的人要承担民事、行政甚至刑事责任。 Việt Nam có Luật Sở hữu trí tuệ, bảo hộ nhãn hiệu, sáng chế và quyền tác giả; người xâm phạm phải chịu trách nhiệm dân sự, hành chính, thậm chí hình sự.")])

add("bullets", section="Khởi động 课前思考", title="Khởi động: từ vựng pháp luật nền tảng của Đơn vị 8", size=34,
    items=["## Kiện tụng",
           "打官司 kiện tụng · 起诉 khởi kiện · 法庭 tòa án · 原告 nguyên đơn · 被告 bị đơn, bị cáo",
           "胜诉 thắng kiện · 败诉 thua kiện · 判决 phán quyết, tuyên án · 上诉 kháng cáo · 赔偿 bồi thường",
           "## Sở hữu trí tuệ 知识产权",
           "商标 nhãn hiệu · 专利 sáng chế, bằng độc quyền · 著作权 (版权) quyền tác giả, bản quyền",
           "注册 đăng ký · 侵权 xâm phạm quyền · 盗版 làm lậu · 山寨 hàng nhái · 高仿 hàng nhái loại 1"],
    say=["Vì đây là đơn vị Pháp luật, trước khi vào bài, chúng ta làm quen với một số từ vựng pháp luật nền tảng. Nhiều từ sẽ còn xuất hiện ở cả ba bài.",
         F(1, "Nhóm thứ nhất là kiện tụng. 打官司 là kiện tụng, đi kiện; 起诉 là khởi kiện; 法庭 là tòa án. 原告 là nguyên đơn, người đi kiện; 被告 là bị đơn, người bị kiện, trong vụ án hình sự thì là bị cáo."),
         F(2, "胜诉 là thắng kiện, 败诉 là thua kiện. 判决 là phán quyết, tuyên án; 上诉 là kháng cáo lên tòa cấp trên; 赔偿 là bồi thường."),
         F(4, "Nhóm thứ hai là sở hữu trí tuệ, 知识产权. 商标 là nhãn hiệu; 专利 là sáng chế, hay bằng độc quyền sáng chế; 著作权, còn gọi là 版权, là quyền tác giả, bản quyền."),
         F(5, "注册 là đăng ký; 侵权 là xâm phạm quyền; 盗版 là làm lậu; 山寨 là hàng nhái; và 高仿 là hàng nhái tinh vi, người Việt hay gọi là hàng fake loại một. Bài hôm nay nói về nhãn hiệu, bài sau nói về bằng sáng chế.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("对簿", "duìbù", "đối bạ", "động từ", "đối chất trước tòa, ra tòa", "两家公司为了商标问题对簿公堂。", "Hai công ty đưa nhau ra tòa vì vấn đề nhãn hiệu.",
     "Động từ, văn viết. Chữ 簿 là sổ sách; thời xưa khi xử án, quan đối chiếu lời khai ghi trong sổ, nên 对簿 là đối chất trước tòa. Hay gặp nhất là 对簿公堂, ra hầu tòa, đưa nhau ra tòa. Tên bài 大头条对簿小油条 chính là Đầu Điều lớn kiện Du Điều nhỏ ra tòa."),
    ("跨界", "kuàjiè", "khóa giới", "động từ", "vượt ranh giới ngành, lấn sân", "这位歌手跨界当起了演员。", "Ca sĩ này lấn sân sang làm diễn viên.",
     "Động từ, nghĩa là vượt qua ranh giới, bước sang một lĩnh vực khác. Chữ 跨 là bước qua, 界 là ranh giới. Tiếng Việt hay nói lấn sân, đa năng. Trong bài: 今日头条跨界卖油条了？"),
    ("调侃", "tiáokǎn", "điều khản", "động từ", "trêu chọc, chế giễu", "他常常调侃自己是“月光族”。", "Anh ấy hay tự trêu mình là “tộc tháng nào hết sạch tiền tháng ấy”.",
     "Động từ, nghĩa là dùng lời nói để trêu chọc, giễu cợt, thường là đùa vui chứ không ác ý. Chú ý chữ 调 ở đây đọc tiáo, như trong 调皮, chứ không đọc diào."),
    ("连锁", "liánsuǒ", "liên tỏa", "tính từ", "nối tiếp nhau như dây xích; chuỗi (cửa hàng)", "这家咖啡连锁店在全国有上千家门店。", "Chuỗi cà phê này có hơn một nghìn cửa hàng trên cả nước.",
     "Tính từ, nghĩa là nối tiếp nhau như mắt xích. 连锁店 là chuỗi cửa hàng; 连锁反应 là phản ứng dây chuyền. Trong bài, 餐饮连锁店 là chuỗi nhà hàng ăn uống."),
    ("闹剧", "nàojù", "náo kịch", "danh từ", "trò hề, màn kịch lố bịch", "这场婚礼最后变成了一场闹剧。", "Đám cưới này cuối cùng biến thành một trò hề.",
     "Danh từ, nghĩa gốc là hài kịch náo nhiệt, nghĩa bóng là sự việc lố bịch, vô lý như một trò hề. Trong bài: 到底是喜剧还是闹剧？ Rốt cuộc là hài kịch hay trò hề?"),
    ("火爆", "huǒbào", "hỏa bạo", "tính từ", "đắt khách, nhộn nhịp, rất “hot”", "这家店的生意非常火爆。", "Cửa hàng này buôn bán cực kỳ đắt khách.",
     "Tính từ, nghĩa là thịnh vượng, náo nhiệt, rất được ưa chuộng. Hay nói 生意火爆, buôn bán đắt hàng; 场面火爆, cảnh tượng sôi động. Trong bài: 今日油条早餐店的火爆, sự nổi như cồn của tiệm ăn sáng."),
    ("酷似", "kùsì", "khốc tự", "động từ", "giống hệt, rất giống", "他长得酷似他的父亲。", "Anh ấy trông giống hệt bố mình.",
     "Động từ, nghĩa là cực kỳ giống. Chữ 酷 ở đây không phải là ngầu, mà là cực kỳ, như trong 酷热, nóng gay gắt. Đây cũng là mẫu câu trọng điểm thứ nhất."),
    ("起因", "qǐyīn", "khởi nhân", "danh từ", "nguyên nhân phát sinh (sự việc)", "这次争吵的起因是一件小事。", "Nguyên nhân của trận cãi nhau này là một chuyện nhỏ.",
     "Danh từ, chỉ nguyên nhân làm một sự việc nổ ra. Trong bài: 火爆的起因是, nguyên nhân khiến tiệm nổi tiếng là."),
    ("资讯", "zīxùn", "tư tấn", "danh từ", "thông tin, tin tức", "我每天早上用手机看新闻资讯。", "Sáng nào tôi cũng xem tin tức trên điện thoại.",
     "Danh từ, nghĩa là thông tin, tin tức. 资讯软件 là ứng dụng tin tức, như 今日头条."),
    ("扑面而来", "pūmiàn-érlái", "phác diện nhi lai", "thành ngữ", "ập thẳng vào mặt", "一打开门，一股热气扑面而来。", "Vừa mở cửa, một luồng hơi nóng ập thẳng vào mặt.",
     "Cụm thành ngữ, nghĩa đen là ập thẳng vào mặt, nói về gió, hơi nóng, mùi hương; nghĩa bóng là một cảm giác ập đến rất mạnh. Trong bài: 这扑面而来的熟悉感, cảm giác quen thuộc ập thẳng vào mặt."),
    ("直呼", "zhíhū", "trực hô", "động từ", "thốt lên, nói thẳng ra", "看完比赛，球迷们直呼过瘾。", "Xem xong trận đấu, người hâm mộ đều thốt lên: đã quá!",
     "Động từ, nghĩa là nói thẳng ra, thốt lên. Bảng từ của sách ghi là tính từ, nhưng thực tế nó được dùng như động từ. Đây cũng là một mẫu câu trọng điểm."),
    ("母公司", "mǔgōngsī", "mẫu công ty", "danh từ", "công ty mẹ", "抖音的母公司是字节跳动。", "Công ty mẹ của Douyin là ByteDance.",
     "Danh từ, chỉ công ty nắm cổ phần chi phối của một công ty khác; đối lập là 子公司, công ty con. Trong bài, công ty mẹ của 今日头条 là 字节跳动, tức ByteDance."),
    ("梯队", "tīduì", "thê đội", "danh từ", "thê đội; nhóm theo cấp bậc", "这几家企业属于行业的第一梯队。", "Mấy doanh nghiệp này thuộc nhóm dẫn đầu của ngành.",
     "Danh từ, nghĩa gốc là các đội quân xếp theo từng tầng lớp; nay chỉ các nhóm xếp theo trình độ, quy mô. 第一梯队 là nhóm hàng đầu. Chữ 梯 là cái thang."),
    ("概率", "gàilǜ", "khái suất", "danh từ", "xác suất, khả năng xảy ra", "中彩票的概率非常低。", "Xác suất trúng xổ số rất thấp.",
     "Danh từ, nghĩa là xác suất. Chú ý chữ 率 ở đây đọc lǜ, như trong 效率, 利润率; còn khi nói 率领, dẫn dắt, thì đọc shuài."),
    ("任", "rèn", "nhậm", "liên từ", "dù, bất kể", "任你怎么劝，他都不听。", "Dù bạn khuyên thế nào, anh ấy cũng không nghe.",
     "Liên từ, nghĩa là dù, bất kể, giống 无论 và 不论; vế sau thường có 也 hoặc 都. Hay gặp 任谁也, dù là ai cũng. Đây là mẫu câu 任也 mà chúng ta sẽ học. Khi làm họ người, chữ này đọc thanh hai.", "认"),
    ("万万", "wànwàn", "vạn vạn", "phó từ", "tuyệt đối, dù thế nào (dùng trong câu phủ định)", "我万万没想到他会骗我。", "Tôi tuyệt đối không ngờ anh ta lại lừa tôi.",
     "Phó từ, nghĩa là tuyệt đối, dù thế nào cũng, chỉ dùng trong câu phủ định: 万万没想到, hoàn toàn không ngờ; 万万不可, tuyệt đối không được."),
    ("碰瓷", "pèngcí", "bính từ", "động từ", "cố tình va chạm để ăn vạ, tống tiền", "有人故意撞车碰瓷，被警察抓了。", "Có kẻ cố tình đâm vào xe để ăn vạ, đã bị cảnh sát bắt.",
     "Động từ. 碰 là va chạm, 瓷 là đồ sứ: cố tình để người khác làm vỡ đồ sứ của mình, hoặc làm mình bị thương, rồi nhân đó đòi tiền, tức là ăn vạ. Nghĩa bóng là bám vào người nổi tiếng để gây chú ý; trong bài, 碰瓷营销 là marketing ăn theo, ăn vạ."),
    ("营销", "yíngxiāo", "doanh tiêu", "động từ", "tiếp thị, marketing", "这家公司很擅长网络营销。", "Công ty này rất giỏi tiếp thị trên mạng.",
     "Động từ, nghĩa là kinh doanh và bán hàng, tức tiếp thị, marketing. Bảng từ của sách in nhầm phiên âm; cách đọc đúng là yíngxiāo. 营销策略 là chiến lược marketing."),
    ("直言", "zhíyán", "trực ngôn", "động từ", "nói thẳng", "他直言自己不喜欢这个方案。", "Anh ấy nói thẳng rằng mình không thích phương án này.",
     "Động từ, nghĩa là nói thẳng ý kiến của mình. Thành ngữ 直言不讳 là nói thẳng không kiêng nể."),
    ("不解", "bùjiě", "bất giải", "động từ", "không hiểu, khó hiểu", "他的做法让大家很不解。", "Cách làm của anh ấy khiến mọi người rất khó hiểu.",
     "Động từ, nghĩa là không hiểu. Hay gặp trong mẫu 令人不解, 让人不解, khiến người ta không hiểu nổi. Đây là mẫu câu 令不解 của bài."),
    ("忠实", "zhōngshí", "trung thực", "tính từ", "trung thành, đáng tin cậy", "我是这个节目的忠实观众。", "Tôi là khán giả trung thành của chương trình này.",
     "Tính từ, nghĩa là trung thành và đáng tin cậy. Cẩn thận, đây là từ dễ nhầm: Hán Việt là trung thực, nhưng nghĩa chính là trung thành, như 忠实用户, người dùng trung thành; 忠实粉丝, fan trung thành. Còn trung thực của tiếng Việt là 诚实."),
    ("傍", "bàng", "bạng", "động từ", "dựa vào, bám vào", "有些小品牌喜欢傍名牌来吸引顾客。", "Một số thương hiệu nhỏ thích bám vào thương hiệu nổi tiếng để thu hút khách.",
     "Động từ, khẩu ngữ, nghĩa là dựa vào, bám vào người hay thứ có thế lực. 傍大款 là bám đại gia; 傍大牌, 傍名牌 là bám thương hiệu lớn, tức là nhái tên thương hiệu nổi tiếng để ăn theo."),
    ("告", "gào", "cáo", "động từ", "kiện, tố cáo", "他把邻居告上了法庭。", "Anh ấy kiện hàng xóm ra tòa.",
     "Động từ, nghĩa là kiện, tố cáo lên cơ quan nhà nước. 告上法庭 là kiện ra tòa. Từ đây có 原告, nguyên đơn, và 被告, bị đơn. Trong bài: 没想到被告侵权了, không ngờ lại bị kiện là xâm phạm quyền."),
    ("侵权", "qīnquán", "xâm quyền", "động từ", "xâm phạm quyền (hợp pháp của người khác)", "未经允许使用别人的照片属于侵权行为。", "Dùng ảnh của người khác khi chưa được phép là hành vi xâm phạm quyền.",
     "Động từ, nghĩa là xâm phạm, làm tổn hại quyền lợi hợp pháp của người khác. Kết hợp: 构成侵权, cấu thành xâm phạm quyền; 商标侵权, xâm phạm nhãn hiệu. Đây là từ khóa của cả bài."),
    ("判定", "pàndìng", "phán định", "động từ", "phán đoán, xác định; phán quyết", "法院判定这家公司侵权。", "Tòa án phán quyết công ty này xâm phạm quyền.",
     "Động từ, nghĩa là phân biệt và xác định. Hay gặp mẫu 判定为, xác định là, phán quyết là: 被判定为驰名商标, được công nhận là nhãn hiệu nổi tiếng."),
    ("脑洞", "nǎodòng", "não động", "danh từ", "trí tưởng tượng (bay bổng)", "这部电影的脑洞真大。", "Bộ phim này có trí tưởng tượng thật phong phú.",
     "Danh từ, từ lóng mạng. Nghĩa đen là cái lỗ trong não, chỉ trí tưởng tượng phong phú, kỳ lạ. 脑洞大 là tưởng tượng bay bổng; thành ngữ mạng 脑洞大开 sẽ học ở phần sau."),
    ("佩服", "pèifú", "bội phục", "động từ", "khâm phục, phục", "我很佩服他的勇气。", "Tôi rất khâm phục lòng dũng cảm của anh ấy.",
     "Động từ, nghĩa là cảm thấy đáng kính mà trong lòng chịu phục, tức khâm phục. Mẫu hay gặp: 佩服得五体投地, phục sát đất."),
    ("蹭", "cèng", "thặng", "động từ", "cọ, quệt; ké, ăn theo", "他经常来我家蹭饭。", "Anh ấy hay đến nhà tôi ăn ké.",
     "Động từ, nghĩa gốc là cọ, quệt. Khẩu ngữ hay dùng nghĩa là không bỏ tiền mà hưởng ké: 蹭饭, ăn chực; 蹭车, đi nhờ xe; 蹭网, dùng ké wifi; 蹭热度, ăn theo độ hot. Phần kết hợp từ sẽ học kỹ."),
    ("说得过去", "shuōdeguòqù", "thuyết đắc quá khứ", "động từ", "tạm chấp nhận được, nói cho qua được", "这个价格还算说得过去。", "Giá này cũng tạm chấp nhận được.",
     "Cụm động từ, nghĩa là có thể chấp nhận được, có lý do để biện minh. Phủ định là 说不过去, không thể chấp nhận được, khó coi. Trong bài: 不是好玩就能说得过去的, đâu phải cứ nói cho vui là xong."),
    ("经受", "jīngshòu", "kinh thụ", "động từ", "trải qua, chịu đựng", "这座桥经受住了地震的考验。", "Cây cầu này đã chịu được thử thách của trận động đất.",
     "Động từ, nghĩa là trải qua, chịu đựng một điều gì đó. Thường đi với 考验, thử thách; 打击, đả kích; 磨炼, rèn luyện. Chúng ta sẽ học ở phần kết hợp từ."),
    ("力度", "lìdù", "lực độ", "danh từ", "mức độ mạnh mẽ, cường độ", "政府加大了打击盗版的力度。", "Chính phủ đã tăng cường mức độ trấn áp hàng lậu.",
     "Danh từ, chỉ độ mạnh yếu của một lực, nghĩa bóng là mức độ quyết liệt của một biện pháp. Kết hợp: 加大力度, tăng cường; 保护力度, mức độ bảo vệ."),
    ("明摆着", "míngbǎizhe", "minh bãi trước", "động từ", "rõ rành rành, bày ra trước mắt", "这明摆着是骗人的。", "Cái này rõ rành rành là lừa người ta.",
     "Động từ, khẩu ngữ, nghĩa là bày ra rõ ràng trước mắt, ai cũng thấy. Đây cũng là một mẫu câu trọng điểm."),
    ("混淆", "hùnxiáo", "hỗn hào", "động từ", "lẫn lộn, nhầm lẫn", "这两个词很容易混淆。", "Hai từ này rất dễ nhầm lẫn.",
     "Động từ, nghĩa là trộn lẫn, làm ranh giới mờ đi, thường dùng cho sự vật trừu tượng: 混淆黑白, đổi trắng thay đen; 混淆视听, làm rối mắt rối tai thiên hạ. Chữ thứ hai đọc xiáo."),
    ("败诉", "bàisù", "bại tố", "động từ", "thua kiện", "这家公司最后败诉了。", "Công ty này cuối cùng đã thua kiện.",
     "Động từ, nghĩa là thua kiện; trái nghĩa là 胜诉, thắng kiện. Chữ 诉 là kiện, như trong 起诉, 诉讼."),
    ("操心", "cāoxīn", "thao tâm", "động từ", "lo lắng, bận tâm", "孩子大了，父母还是为他操心。", "Con đã lớn rồi mà bố mẹ vẫn lo cho nó.",
     "Động từ, nghĩa là tốn tâm sức lo nghĩ. 爱操心 là hay lo, hay bận tâm. Cũng có thể tách ra: 操了不少心, lo không ít."),
    ("转眼", "zhuǎnyǎn", "chuyển nhãn", "động từ", "chớp mắt, thoáng chốc", "转眼间，我们毕业已经十年了。", "Thoáng chốc, chúng tôi tốt nghiệp đã mười năm rồi.",
     "Động từ, nghĩa là trong nháy mắt, chỉ thời gian rất ngắn. Hay dùng 转眼间, 一转眼. Trong bài: 转眼就被抄过去, chớp mắt đã bị chép mất."),
    ("制止", "zhìzhǐ", "chế chỉ", "động từ", "ngăn chặn, ngăn cấm", "警察及时制止了这场打架。", "Cảnh sát đã kịp thời ngăn chặn vụ đánh nhau này.",
     "Động từ, nghĩa là ép phải dừng lại, không cho tiếp tục. Thường dùng với hành vi xấu: 制止侵权, 制止违法行为."),
    ("山寨", "shānzhài", "sơn trại", "danh từ", "hàng nhái, đồ giả", "这款山寨手机看起来跟真的一模一样。", "Chiếc điện thoại nhái này trông giống hệt hàng thật.",
     "Danh từ, nghĩa gốc là trại trên núi, nơi ở của thảo khấu ngoài vòng pháp luật. Nay chỉ hàng nhái, không phải hàng chính hãng: 山寨货, 山寨手机. Phần ôn tập đơn vị còn có một đề thảo luận về hàng nhái."),
    ("要不是", "yàobúshì", "yếu bất thị", "liên từ", "nếu không phải (vì), nếu không nhờ", "要不是下雨，我们早就到了。", "Nếu không phải vì trời mưa thì chúng tôi đã đến từ lâu rồi.",
     "Liên từ, nghĩa là nếu không phải, nếu không nhờ. Vế sau nói kết quả trái với thực tế, hay có 早就, 就. Trong bài: 要不是这一波炒作造势，谁知道有个今日油条！"),
    ("造势", "zàoshì", "tạo thế", "động từ", "tạo thanh thế, gây tiếng vang", "新电影上映前，公司花了很多钱造势。", "Trước khi phim mới ra rạp, công ty đã chi rất nhiều tiền để tạo tiếng vang.",
     "Động từ, nghĩa là tạo ra thanh thế, gây sự chú ý của dư luận. Hay đi với 炒作, thổi phồng: 炒作造势, thổi phồng gây tiếng vang, tức là làm PR."),
    ("定性", "dìngxìng", "định tính", "động từ", "xác định tính chất (sai phạm, sự việc)", "这起事件已被定性为交通事故。", "Vụ việc này đã được xác định là tai nạn giao thông.",
     "Động từ, nghĩa là xác định tính chất của một sai phạm hay sự việc. Mẫu hay gặp: 被定性为, được xác định là. Trong bài: 确需法律层面的定性, quả thật cần pháp luật xác định tính chất."),
    ("近乎", "jìnhū", "cận hồ", "động từ", "gần như", "他的要求近乎无理。", "Yêu cầu của anh ta gần như vô lý.",
     "Động từ, văn viết, nghĩa là gần như, tiếp cận với. Đứng trước danh từ hay tính từ. Đây cũng là một mẫu câu trọng điểm."),
    ("高仿", "gāofǎng", "cao phỏng", "tính từ", "nhái tinh vi, nhái loại một", "这个包是高仿的，不是真品。", "Cái túi này là hàng nhái tinh vi, không phải hàng thật.",
     "Tính từ, nghĩa là bắt chước ở trình độ rất cao, giống đến mức khó phân biệt. 高仿货 là hàng fake loại một, hàng super fake."),
    ("驰名", "chímíng", "trì danh", "động từ", "nổi tiếng khắp nơi", "这家老字号驰名中外。", "Cửa hiệu lâu đời này nổi tiếng trong và ngoài nước.",
     "Động từ, nghĩa là danh tiếng lan truyền rất xa. Chữ 驰 là phi ngựa. 驰名中外 là nổi tiếng trong và ngoài nước. 驰名商标 là nhãn hiệu nổi tiếng, một khái niệm pháp lý rất quan trọng trong bài."),
    ("理应", "lǐyīng", "lý ứng", "động từ", "lẽ ra phải, đương nhiên nên", "子女理应孝敬父母。", "Con cái đương nhiên phải hiếu kính cha mẹ.",
     "Động từ, nghĩa là theo lẽ thì nên. Chú ý chữ 应 đọc thanh một. Trong bài: 合法权益理应得到保护, quyền lợi hợp pháp lẽ đương nhiên phải được bảo vệ."),
    ("否决", "fǒujué", "phủ quyết", "động từ", "bác bỏ, phủ quyết", "这个方案被董事会否决了。", "Phương án này đã bị hội đồng quản trị bác bỏ.",
     "Động từ, nghĩa là phủ định, bác bỏ một đề án, đề nghị. 否决权 là quyền phủ quyết."),
    ("严惩", "yánchéng", "nghiêm trừng", "động từ", "trừng trị nghiêm khắc", "对酒后驾车的人应该严惩。", "Người lái xe sau khi uống rượu cần bị trừng trị nghiêm khắc.",
     "Động từ, nghĩa là xử phạt nghiêm khắc. Trong bài: 将受到法律严惩, sẽ bị pháp luật trừng trị nghiêm khắc."),
    ("恶意", "èyì", "ác ý", "danh từ", "ác ý, ý đồ xấu", "他并没有恶意，只是开个玩笑。", "Anh ấy không hề có ác ý, chỉ là đùa thôi.",
     "Danh từ, nghĩa là ý đồ xấu, lòng dạ không tốt; trái nghĩa là 善意, thiện ý. Thường làm trạng ngữ: 恶意抢注, ác ý đăng ký chặn trước; 恶意中伤, cố ý bôi nhọ."),
    ("抢注", "qiǎngzhù", "thương chú", "động từ", "đăng ký chặn trước (nhãn hiệu, tên miền)", "这个品牌的商标在国外被人抢注了。", "Nhãn hiệu của thương hiệu này đã bị người khác đăng ký trước ở nước ngoài.",
     "Động từ, nghĩa là giành đăng ký trước, thường là đăng ký trước nhãn hiệu hay tên miền của người khác để trục lợi. Chữ 抢 là giành giật, 注 là 注册, đăng ký."),
    ("营商", "yíngshāng", "doanh thương", "danh từ", "kinh doanh", "政府努力改善营商环境。", "Chính phủ nỗ lực cải thiện môi trường kinh doanh.",
     "Danh từ, nghĩa là hoạt động kinh doanh thương mại. Hầu như luôn gặp trong cụm 营商环境, môi trường kinh doanh, một cụm từ rất hay xuất hiện trên báo chí."),
]

add("bullets", chapter="Từ mới (50 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 8.1 có 50 từ mới, chia thành 17 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 调侃 (tiáo) · 概率 (lǜ) · 营销 (yíngxiāo) · 混淆 (xiáo) · 理应 (yīng)",
           "Từ dễ nhầm: 忠实 (trung thành ≠ trung thực) · 酷似 · 山寨"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có năm mươi từ, thầy chia thành mười bảy nhóm nhỏ. Bài báo dùng rất nhiều từ ngữ pháp luật, xen lẫn với từ lóng mạng rất sinh động.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Chú ý cách đọc của một số chữ: 调侃 đọc là tiáokǎn, 概率 đọc là gàilǜ, 营销 đọc là yíngxiāo, 混淆 đọc là hùnxiáo, và 理应 đọc là lǐyīng."),
         F(4, "Ngoài ra, có những từ Hán Việt rất dễ hiểu nhầm, như 忠实: Hán Việt là trung thực, nhưng nghĩa là trung thành. Các bạn nhớ nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

sizes = [3] * 16 + [2]
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
    ("《今日头条》跨界卖油条了？一家名为“今日油条”的早餐店出现在大众的视野中。有网友调侃，上班早高峰一边刷着“《今日头条》”，一边吃着“今日油条”，亦庄亦谐，颇为搞笑。当互联网公司遇上餐饮连锁店，到底是喜剧还是闹剧？",
     "“Tin nóng hôm nay” lấn sân sang bán quẩy rồi sao? Một tiệm ăn sáng tên là “Quẩy hôm nay” đã lọt vào tầm mắt công chúng. Có cư dân mạng trêu rằng: giờ cao điểm sáng đi làm, vừa lướt “Tin nóng hôm nay”, vừa ăn “Quẩy hôm nay”, vừa nghiêm túc vừa hài hước, khá là buồn cười. Khi công ty internet gặp chuỗi nhà hàng ăn uống, rốt cuộc là hài kịch hay trò hề?",
     ["《今日头条》 là ứng dụng tin tức, tên dịch sát là Tin nóng hôm nay; 今日油条 là Quẩy hôm nay. 名为 là có tên là, văn viết. 大众的视野 là tầm mắt của công chúng. 早高峰 là giờ cao điểm buổi sáng; 刷 là lướt điện thoại.",
      "亦庄亦谐 là thành ngữ: vừa nghiêm túc vừa hài hước, sẽ học ở phần sau. 颇为搞笑 là khá buồn cười; 颇为 là khá, văn viết. 喜剧还是闹剧 là hài kịch hay trò hề: câu hỏi mở đầu rất gây tò mò."]),
    ("“今日油条”早餐店的火爆，起因是这家店从商标到海报，都酷似手机资讯软件《今日头条》，其中，《今日头条》的口号是“你关心的，才是头条”，而今日油条的口号是“关心你的，才是好油条”。这扑面而来的熟悉感让人直呼：不管是口号还是菜单设计都有一股浓浓的“头条味儿”。",
     "Tiệm ăn sáng “Quẩy hôm nay” nổi như cồn là vì từ nhãn hiệu đến áp phích của tiệm đều giống hệt ứng dụng tin tức “Tin nóng hôm nay”. Trong đó, khẩu hiệu của “Tin nóng hôm nay” là “Điều bạn quan tâm mới là tin nóng”, còn khẩu hiệu của “Quẩy hôm nay” là “Thứ quan tâm đến bạn mới là quẩy ngon”. Cảm giác quen thuộc ập vào mặt này khiến người ta phải thốt lên: dù là khẩu hiệu hay thiết kế thực đơn đều đậm đặc “mùi Toutiao”.",
     ["Tiêu đề nhỏ của phần này là 油条抱头条大腿？ Quẩy ôm đùi Tin nóng? 抱大腿 là ôm đùi, tức bám vào người có thế. 火爆的起因是 là nguyên nhân khiến tiệm nổi như cồn là. 商标 là nhãn hiệu, 海报 là áp phích. 酷似 là giống hệt, mẫu câu trọng điểm.",
      "Hai khẩu hiệu là một trò chơi chữ: 你关心的 là điều bạn quan tâm, còn 关心你的 là thứ quan tâm đến bạn, chỉ đảo vị trí hai chữ. 扑面而来的熟悉感 là cảm giác quen thuộc ập đến. 直呼 là thốt lên. 浓浓的头条味儿 là đậm đặc mùi Toutiao."]),
    ("《今日头条》的母公司字节跳动作为中国第一梯队的互联网大厂，这种事情发生的概率可以说是微乎其微。一来《今日头条》早已声名在外，任谁也不会这么明目张胆地模仿和盗版；二来这样的跨行业模仿，《今日头条》也是被打了个措手不及，万万没想到一家餐饮连锁店居然“碰瓷营销”到互联网企业的头上！",
     "Công ty mẹ của “Tin nóng hôm nay” là ByteDance, một “ông lớn” internet thuộc nhóm hàng đầu Trung Quốc; chuyện như thế này có thể nói là xác suất cực kỳ nhỏ. Một là, “Tin nóng hôm nay” từ lâu đã nổi tiếng khắp nơi, dù là ai cũng không dám bắt chước và làm nhái trắng trợn đến vậy; hai là, kiểu bắt chước xuyên ngành này cũng khiến “Tin nóng hôm nay” trở tay không kịp, tuyệt đối không ngờ một chuỗi nhà hàng ăn uống lại dám “marketing ăn vạ” lên đầu một doanh nghiệp internet!",
     ["字节跳动 là ByteDance, công ty mẹ của 今日头条 và 抖音, tức TikTok. 作为 là với tư cách là. 互联网大厂 là ông lớn internet. 微乎其微 là thành ngữ: ít ỏi, nhỏ bé vô cùng.",
      "一来，二来 là một là, hai là, dùng để liệt kê lý do. 声名在外 là tiếng tăm vang xa. 任谁也不会 là dù là ai cũng không, mẫu câu 任也. 明目张胆 là trắng trợn. 被打了个措手不及 là bị đánh cho trở tay không kịp. 万万没想到 là hoàn toàn không ngờ. 碰瓷营销 là marketing ăn vạ, ăn theo người nổi tiếng."]),
    ("网友对于这种“抱大腿”行为也发出质疑，对此今日油条相关负责人揣着明白装糊涂，直言自己不知道哪个字不能用。大公司《今日头条》起诉卖油条的小公司今日油条，这也令他不解。“我天天刷《今日头条》，是忠实用户，‘傍大牌’只是觉得好玩而已，没想到被告侵权了。要是非要判定我输，我也只好面对。”",
     "Cư dân mạng cũng đặt nghi vấn về hành vi “ôm đùi” này. Trước điều đó, người phụ trách của “Quẩy hôm nay” biết rõ mà vờ như không biết, nói thẳng rằng mình chẳng biết chữ nào là không được dùng. Việc công ty lớn “Tin nóng hôm nay” kiện công ty nhỏ bán quẩy cũng khiến anh ta không hiểu nổi. “Ngày nào tôi cũng lướt ‘Tin nóng hôm nay’, là người dùng trung thành, ‘bám thương hiệu lớn’ chỉ là thấy vui thôi, không ngờ lại bị kiện là xâm phạm quyền. Nếu nhất định phải xử tôi thua, thì tôi cũng đành chấp nhận.”",
     ["发出质疑 là đưa ra nghi vấn. 相关负责人 là người phụ trách liên quan. 揣着明白装糊涂 là bụng biết rõ mà vờ hồ đồ, mẫu câu trọng điểm. 直言 là nói thẳng. 起诉 là khởi kiện. 令他不解 là khiến anh ta không hiểu, mẫu câu 令不解.",
      "忠实用户 là người dùng trung thành. 傍大牌 là bám thương hiệu lớn. 好玩而已 là cho vui mà thôi. 被告侵权 ở đây là 被 cộng 告: bị kiện là xâm phạm quyền. 非要 là nhất định phải. 只好面对 là đành đối mặt, đành chấp nhận."]),
    ("乍听起来，“今日油条”抖得一手好机灵，起名者脑洞大开，着实让人佩服。然而，很多“蹭IP”的行为可不是“好玩”就能说得过去的，还得经受法律的审视——在保护知识产权力度不断强化的背景下，有些名字或商标不是想模仿就能模仿、想蹭就可以蹭的。",
     "Thoạt nghe thì “Quẩy hôm nay” đúng là khéo khoe sự lanh lợi, người đặt tên có trí tưởng tượng bay bổng, thật khiến người ta khâm phục. Thế nhưng, nhiều hành vi “ăn theo IP” đâu phải cứ nói “cho vui” là có thể cho qua, mà còn phải chịu sự soi xét của pháp luật: trong bối cảnh việc bảo vệ quyền sở hữu trí tuệ ngày càng được tăng cường, có những cái tên hay nhãn hiệu đâu phải muốn bắt chước là bắt chước được, muốn ăn theo là ăn theo được.",
     ["Tiêu đề nhỏ của phần này là 今日油条是否侵权？ Quẩy hôm nay có xâm phạm quyền không? 乍听起来 là thoạt nghe, mẫu câu trọng điểm. 抖机灵 là khoe khôn, khoe lanh lợi; 抖得一手好机灵 theo mẫu động từ 得一手好 danh từ, như 写得一手好字. 起名者 là người đặt tên. 着实 là thật sự.",
      "蹭IP là ăn theo hình ảnh, thương hiệu nổi tiếng. 说得过去 là chấp nhận được. 经受法律的审视 là chịu sự soi xét của pháp luật. 知识产权 là quyền sở hữu trí tuệ. Mẫu 不是想A就能A的 là đâu phải muốn A là A được."]),
    ("对此事件，网友看法不一。有网友认为“小商家跨界蹭个热度而已。”“明摆着是两种行业，消费者怎么可能混淆呢？”“《今日头条》不仅有可能败诉，还有可能为今日油条打了一波好广告。”",
     "Về sự việc này, cư dân mạng mỗi người một ý. Có người cho rằng: “Chỉ là cửa hàng nhỏ lấn sân, ăn theo độ hot một chút thôi mà.” “Rõ ràng là hai ngành khác nhau, người tiêu dùng sao có thể nhầm lẫn được?” “‘Tin nóng hôm nay’ không những có thể thua kiện, mà còn có thể đã làm một đợt quảng cáo không công cho ‘Quẩy hôm nay’.”",
     ["看法不一 là ý kiến không thống nhất, mỗi người một ý. 小商家 là nhà buôn nhỏ. 蹭个热度而已 là chỉ ăn theo độ hot chút thôi; 热度 là độ nóng, độ hot.",
      "明摆着 là rõ rành rành, mẫu câu trọng điểm. 混淆 là nhầm lẫn. 败诉 là thua kiện. 打了一波好广告 là làm một đợt quảng cáo hay; 一波 là một đợt, cách nói rất phổ biến trên mạng. Đây là phe cho rằng tiệm quẩy không có lỗi."]),
    ("也有爱操心的网友认为，“大公司花了几十上百万设计出来的商标，转眼就被抄过去，这种行为不被制止，将会有更多山寨。”“今天放过了你，明天就会有阿外巴巴。”“要不是这一波炒作造势，谁知道有个‘今日油条’！”",
     "Cũng có những cư dân mạng hay lo xa cho rằng: “Nhãn hiệu mà công ty lớn bỏ ra mấy chục, cả trăm vạn tệ để thiết kế, chớp mắt đã bị chép mất; hành vi này mà không bị ngăn chặn thì sẽ còn nhiều hàng nhái hơn nữa.” “Hôm nay tha cho anh, ngày mai sẽ có ‘A Ngoại Ba Ba’.” “Nếu không nhờ đợt thổi phồng, gây tiếng vang này, thì ai biết có một tiệm ‘Quẩy hôm nay’!”",
     ["爱操心 là hay lo, hay bận tâm. 几十上百万 là mấy chục đến cả trăm vạn tệ. 转眼就被抄过去 là chớp mắt đã bị chép mất. 制止 là ngăn chặn. 山寨 là hàng nhái.",
      "阿外巴巴 là cái tên bịa ra để nhái 阿里巴巴, Alibaba: chữ 里 là trong, nên đổi thành 外 là ngoài, rất hài hước. 要不是 là nếu không nhờ. 炒作造势 là thổi phồng, gây tiếng vang. Đây là phe cho rằng tiệm quẩy cố tình ăn theo."]),
    ("就此事而言，“今日油条”是否构成侵权，确需法律层面的定性，可名字近乎“高仿”，商标标识跟字体也高度相似，这很难不受到质疑。上海协力（郑州）律师事务所律师刘棒认为，一般情况下，如果《今日头条》没有在食品类或餐饮类注册商标，“今日油条”是不构成对《今日头条》商标侵权的。",
     "Riêng về việc này, “Quẩy hôm nay” có cấu thành xâm phạm quyền hay không thì quả thật cần pháp luật xác định tính chất; nhưng cái tên gần như “nhái loại một”, biểu tượng nhãn hiệu và kiểu chữ cũng giống nhau đến mức cao độ, thật khó mà không bị nghi vấn. Luật sư Lưu Bổng của Văn phòng luật Thượng Hải Hiệp Lực (Trịnh Châu) cho rằng: thông thường, nếu “Tin nóng hôm nay” chưa đăng ký nhãn hiệu ở nhóm thực phẩm hay ăn uống, thì “Quẩy hôm nay” không cấu thành xâm phạm nhãn hiệu của “Tin nóng hôm nay”.",
     ["就此事而言 là riêng về việc này mà nói, mẫu câu 就而言. 是否构成侵权 là có cấu thành xâm phạm quyền hay không. 确需 là quả thật cần. 层面 là phương diện, góc độ. 近乎高仿 là gần như nhái loại một, mẫu câu 近乎. 很难不受到质疑 là phủ định kép: khó mà không bị nghi vấn.",
      "律师事务所 là văn phòng luật sư. Ý kiến của luật sư dựa trên một nguyên tắc quan trọng: nhãn hiệu được bảo hộ theo nhóm hàng hóa, dịch vụ đã đăng ký. 今日头条 đăng ký ở nhóm thông tin, internet, chứ không phải nhóm 食品类, thực phẩm, hay 餐饮类, ăn uống."]),
    ("“如果《今日头条》是中国驰名商标的话，那么无论是否在食品、餐饮方面申请商标，‘今日油条’都会构成侵权。”刘棒解释，驰名商标知名度通常比较大，影响力是“跨界”的。“还得看《今日头条》能否被判定为中国驰名商标，可以的话，他就能顺利追究模仿企业的责任。否则两者只能是井水不犯河水的关系。”",
     "“Nếu ‘Tin nóng hôm nay’ là nhãn hiệu nổi tiếng của Trung Quốc, thì dù có đăng ký nhãn hiệu ở mảng thực phẩm, ăn uống hay không, ‘Quẩy hôm nay’ đều sẽ cấu thành xâm phạm quyền.” Luật sư Lưu Bổng giải thích: nhãn hiệu nổi tiếng thường có độ nhận biết khá lớn, sức ảnh hưởng vượt ra ngoài ranh giới ngành. “Còn phải xem ‘Tin nóng hôm nay’ có được công nhận là nhãn hiệu nổi tiếng của Trung Quốc hay không; nếu được, họ có thể thuận lợi truy cứu trách nhiệm của doanh nghiệp bắt chước. Nếu không, hai bên chỉ có thể là quan hệ nước giếng không phạm nước sông.”",
     ["驰名商标 là nhãn hiệu nổi tiếng: đây là ngoại lệ của nguyên tắc bảo hộ theo nhóm. Nhãn hiệu nổi tiếng được bảo hộ cả ở những nhóm hàng hóa chưa đăng ký, vì sức ảnh hưởng của nó là 跨界, vượt ngành. 申请商标 là nộp đơn đăng ký nhãn hiệu. 知名度 là độ nổi tiếng.",
      "能否 là có thể hay không. 判定为 là được công nhận là. 追究责任 là truy cứu trách nhiệm. 否则 là nếu không thì. 井水不犯河水 là nước giếng không phạm nước sông, tức là ai lo việc nấy, không liên quan gì đến nhau."]),
    ("通常知名品牌往往是经过多年打造而成的。无论是当初注册商标，还是之后的宣传、维护，都需要投入相应的精力、资金等。因此，知名商标持有人的合法权益理应得到保护。而恶意抢注商标、傍名牌搭便车行为，被法律“否决”则是理所当然的。",
     "Thường thì một thương hiệu nổi tiếng phải trải qua nhiều năm gây dựng mới thành. Dù là đăng ký nhãn hiệu lúc đầu, hay quảng bá, duy trì về sau, đều cần bỏ ra công sức, tiền vốn tương ứng. Vì vậy, quyền lợi hợp pháp của người sở hữu nhãn hiệu nổi tiếng lẽ đương nhiên phải được bảo vệ. Còn những hành vi ác ý đăng ký chặn trước nhãn hiệu, bám thương hiệu nổi tiếng để “đi nhờ xe”, thì bị pháp luật “bác bỏ” là điều đương nhiên.",
     ["Tiêu đề nhỏ của phần cuối là 屡屡被打擦边球，企业应如何保护商标？ Liên tục bị người ta lách luật, doanh nghiệp nên bảo vệ nhãn hiệu thế nào? 屡屡 là nhiều lần; 打擦边球 là đánh bóng sượt mép bàn, tức là lách luật.",
      "打造而成 là gây dựng mà thành. 当初 là lúc đầu. 相应的 là tương ứng. 持有人 là người sở hữu. 合法权益 là quyền và lợi ích hợp pháp. 理应 là lẽ ra phải. 恶意抢注 là ác ý đăng ký chặn trước. 搭便车 là đi nhờ xe, tức hưởng thành quả của người khác. 理所当然 là lẽ đương nhiên."]),
    ("“经营者必须增强知识产权意识，尊重他人商标权益。‘傍大牌’一时爽，算后账泪两行，恶意侵犯他人注册商标专用权的行为将受到法律严惩。”说到底，只有对恶意抢注行为果断说“不”，正常的营商环境才会更有保障，也才能将知识产权的保护更好地落到实处。",
     "“Người kinh doanh phải nâng cao ý thức về sở hữu trí tuệ, tôn trọng quyền lợi nhãn hiệu của người khác. ‘Bám thương hiệu lớn’ thì sướng nhất thời, đến lúc tính sổ thì nước mắt hai hàng; hành vi ác ý xâm phạm quyền sử dụng độc quyền nhãn hiệu đã đăng ký của người khác sẽ bị pháp luật trừng trị nghiêm khắc.” Suy cho cùng, chỉ có dứt khoát nói “không” với hành vi ác ý đăng ký chặn trước, thì môi trường kinh doanh bình thường mới được bảo đảm hơn, và việc bảo vệ quyền sở hữu trí tuệ mới thực sự đi vào thực chất.",
     ["经营者 là người kinh doanh. 傍大牌一时爽，算后账泪两行 là bám thương hiệu lớn thì sướng nhất thời, lúc tính sổ thì nước mắt hai hàng. Câu này nhại khẩu hiệu an toàn giao thông trong phim 流浪地球, Lưu lạc Địa Cầu: 行车不规范，亲人泪两行, lái xe không đúng luật, người thân khóc hai hàng.",
      "专用权 là quyền sử dụng độc quyền. 严惩 là trừng trị nghiêm khắc. 说到底 là suy cho cùng, mẫu câu trọng điểm. 果断说不 là dứt khoát nói không. 将知识产权的保护落到实处 là đưa việc bảo vệ sở hữu trí tuệ vào thực tế, mẫu câu 将落到实处."]),
]
# tiêu đề nhỏ của bài khóa: đoạn bắt đầu phần đó
HEAD = {2: "“油条”抱“头条”大腿？", 5: "今日油条是否侵权？", 10: "屡屡被打擦边球……"}

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa “大头条”对簿“小油条”", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa. Bài được cải biên từ ba bài báo tháng mười năm hai nghìn không trăm hai mươi, đăng trên chương trình 国事说法, báo 电商报 và báo 新京报. Bài dài khoảng một nghìn ba trăm chữ, có ba tiêu đề nhỏ.",
         F(0, "Thầy chia bài thành mười một đoạn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 90 else 50 if len(zh) <= 115 else 46 if len(zh) <= 150 else 44
    title = f"Bài khóa – đoạn {i}/{len(P)}" + (f" · {HEAD[i]}" if i in HEAD else "")
    add("passage", section="Bài khóa 课文", title=title, zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", "").replace("‘", "").replace("’", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Bố cục & ghi chú", section="Bài khóa 课文", title="Bố cục bài khóa", size=34,
    items=["## 1. Mở đầu (đoạn 1)",
           "Tiệm ăn sáng “今日油条” xuất hiện → 喜剧还是闹剧？",
           "## 2. “油条”抱“头条”大腿？(đoạn 2–4)",
           "Nhãn hiệu, áp phích, khẩu hiệu 酷似《今日头条》 · ông lớn bị đánh 措手不及 · chủ tiệm 揣着明白装糊涂",
           "## 3. 今日油条是否侵权？(đoạn 5–9)",
           "Cư dân mạng 看法不一 · luật sư: bảo hộ theo nhóm; trừ khi là 驰名商标",
           "## 4. 屡屡被打擦边球，企业应如何保护商标？(đoạn 10–11)",
           "Bảo vệ người sở hữu nhãn hiệu · 对恶意抢注果断说“不” · 将知识产权保护落到实处"],
    say=["Trước khi sang phần mẫu câu, chúng ta cùng nhìn lại bố cục bài khóa. Đây là một bài báo kết hợp tin tức và bình luận, có bốn phần.",
         F(1, "Phần một, mở đầu: một tiệm ăn sáng tên 今日油条 xuất hiện, khiến cư dân mạng vừa buồn cười vừa thắc mắc: đây là hài kịch hay trò hề?"),
         F(3, "Phần hai, với tiêu đề 油条抱头条大腿: tiệm quẩy nhái cả nhãn hiệu, áp phích lẫn khẩu hiệu của ứng dụng tin tức; ông lớn bị bất ngờ, còn chủ tiệm thì biết rõ mà giả vờ không biết."),
         F(5, "Phần ba, với tiêu đề 今日油条是否侵权: cư dân mạng chia làm hai phe. Luật sư giải thích: nhãn hiệu được bảo hộ theo nhóm, nên tiệm quẩy chỉ xâm phạm quyền nếu 今日头条 được công nhận là nhãn hiệu nổi tiếng."),
         F(7, "Phần bốn, kết luận: phải bảo vệ người sở hữu nhãn hiệu, dứt khoát nói không với việc ác ý đăng ký chặn trước, thì môi trường kinh doanh mới lành mạnh.")])

add("bullets", section="Bài khóa 课文", title="Ghi chú 注释: hiểu thêm về bối cảnh", size=32,
    items=["字节跳动 (ByteDance): lập tháng 3/2012 tại Bắc Kinh; sản phẩm: 《今日头条》, 西瓜视频, 抖音 (TikTok); 《今日头条》 do 张一鸣 lập, gợi ý tin theo dữ liệu người dùng",
           "今日油条: công ty ở Hà Nam, lập ngày 13/5/2020, bán quẩy, sữa đậu nành, bánh kếp…; chỉ 5 tháng đã thành “tiệm hot”, mở nhượng quyền; tháng 10/2020 bị kiện",
           "阿外巴巴: tên bịa, nhái 阿里巴巴 (Alibaba) – tập đoàn do 马云 và 17 người khác lập năm 1999 ở Hàng Châu",
           "“……一时爽，……泪两行”: nhại khẩu hiệu trong phim 《流浪地球》 (2019): “道路千万条，安全第一条。行车不规范，亲人泪两行。” → 超速一时爽，罚款泪两行"],
    say=["Sách có bốn ghi chú giúp hiểu thêm bối cảnh bài khóa.",
         F(0, "Một: 字节跳动, tức ByteDance, thành lập tháng ba năm hai nghìn không trăm mười hai ở Bắc Kinh, là một trong những công ty đầu tiên ở Trung Quốc ứng dụng trí tuệ nhân tạo vào internet di động. Sản phẩm gồm 今日头条, 西瓜视频 và 抖音, tức TikTok. 今日头条 do 张一鸣 sáng lập, gợi ý tin tức dựa trên khai thác dữ liệu người dùng."),
         F(1, "Hai: nhãn hiệu 今日油条 thuộc về một công ty ăn uống ở tỉnh Hà Nam, thành lập ngày mười ba tháng năm năm hai nghìn không trăm hai mươi, bán quẩy, sữa đậu nành, bánh kếp, canh cay. Chỉ năm tháng sau đã thành tiệm nổi tiếng trên mạng, còn mở mô hình nhượng quyền. Tháng mười năm đó, 今日头条 khởi kiện, gây xôn xao dư luận."),
         F(2, "Ba: 阿外巴巴 là tên bịa ra để nhái 阿里巴巴, tức Alibaba, tập đoàn do 马云, Mã Vân, cùng mười bảy người khác sáng lập năm một nghìn chín trăm chín mươi chín ở Hàng Châu."),
         F(3, "Bốn: câu 傍大牌一时爽，算后账泪两行 nhại khẩu hiệu an toàn giao thông trong phim khoa học viễn tưởng 流浪地球 năm hai nghìn không trăm mười chín: 道路千万条，安全第一条。行车不规范，亲人泪两行。 Đường có nghìn vạn lối, an toàn là số một; lái xe không đúng luật, người thân khóc hai hàng. Cư dân mạng chế ra rất nhiều câu theo mẫu này, như 超速一时爽，罚款泪两行, chạy quá tốc độ sướng nhất thời, nộp phạt nước mắt hai hàng.")])

# ======================= MẪU CÂU =======================
add("bullets", chapter="Mẫu câu: 酷似 · 直呼 · 任…也 · 揣着明白装糊涂", section="Mẫu câu 重点句型", title="1. ……酷似…… · 2. 直呼……", size=33,
    items=["## A 酷似 B: A giống hệt B, rất giống B",
           "“今日油条”早餐店的火爆，起因是这家店从商标到海报，都酷似手机资讯软件《今日头条》。",
           "……中国馆……由于形状酷似一顶古帽，因此被命名为“东方之冠”。",
           "刘钊，外形酷似香港著名演员周润发，……圈里人都称他为“发哥”。",
           "## 直呼……: thốt lên, nói thẳng ra",
           "这扑面而来的熟悉感让人直呼：不管口号还是菜单设计都有一股浓浓的“头条味儿”。",
           "看完这电影，他直呼过瘾，还想再看一遍。",
           "他走出考场，直呼：“完了完了，今天的考试难死了，鬼才能过呢！”"],
    say=["Bây giờ chúng ta sang phần mẫu câu và từ ngữ trọng điểm. Bài này có mười một điểm, thầy gộp mỗi slide hai điểm. Đầu tiên là 酷似 và 直呼.",
         F(0, "A 酷似 B nghĩa là A giống hệt B, giống đến mức khó phân biệt. Mức độ mạnh hơn 很像, và mang màu sắc văn viết."),
         F(1, "Ví dụ từ bài khóa: 今日油条早餐店的火爆，起因是这家店从商标到海报，都酷似手机资讯软件今日头条。"),
         F(2, "在二零一零上海世博会中，各国展馆精彩亮相，中国馆的主题是城市发展中的中华智慧，由于形状酷似一顶古帽，因此被命名为东方之冠。 Tại Hội chợ triển lãm thế giới Thượng Hải năm hai nghìn không trăm mười, nhà triển lãm Trung Quốc có hình dáng giống hệt một chiếc mũ cổ, nên được đặt tên là Vương miện phương Đông.",
           cap="在2010上海世博会中，各国展馆精彩亮相，中国馆的主题是“城市发展中的中华智慧”，由于形状酷似一顶古帽，因此被命名为“东方之冠”。 Nhà triển lãm Trung Quốc ở Expo Thượng Hải 2010 giống hệt một chiếc mũ cổ, nên được gọi là “Vương miện phương Đông”."),
         F(3, "刘钊，外形酷似香港著名演员周润发，加上神态举止也有几分神似，圈里人都称他为发哥。 Lưu Chiêu có ngoại hình giống hệt nam diễn viên nổi tiếng Hồng Kông Châu Nhuận Phát, thần thái cử chỉ cũng có vài phần giống, nên người trong giới đều gọi anh là anh Phát."),
         F(4, "直呼 nghĩa là nói thẳng ra, thốt lên, thường là một cảm xúc mạnh như sung sướng, ngạc nhiên, thất vọng. Theo sau là nội dung lời thốt lên."),
         F(5, "Ví dụ từ bài khóa: 这扑面而来的熟悉感让人直呼：不管口号还是菜单设计都有一股浓浓的头条味儿。"),
         F(6, "看完这电影，他直呼过瘾，还想再看一遍。 Xem xong bộ phim, anh ấy thốt lên đã quá, còn muốn xem lại lần nữa. 过瘾 là đã, thỏa thích."),
         F(7, "他走出考场，直呼：完了完了，今天的考试难死了，鬼才能过呢！ Ra khỏi phòng thi, cậu ấy thốt lên: Tiêu rồi tiêu rồi, bài thi hôm nay khó chết đi được, ma mới qua nổi! 鬼才能过 là chỉ có ma mới qua được, tức là không ai qua được.")])

add("bullets", section="Mẫu câu 重点句型", title="3. 任……也 · 4. 揣着明白装糊涂", size=33,
    items=["## 任……也……: dù… cũng… (điều kiện khác nhau, kết quả như nhau)",
           "《今日头条》早已声名在外，任谁也不会这么明目张胆地模仿和盗版。",
           "这是不可抗力的天灾，任谁也无可奈何啊！",
           "任你们怎么说，我也不会改变自己的想法。",
           "## 揣着明白装糊涂: bụng biết rõ mà vờ như không biết",
           "……对此今日油条相关负责人揣着明白装糊涂，直言自己不知道哪个字不能用。",
           "他什么事都知道，却揣着明白装糊涂，一问三不知。",
           "公司出了这个问题，你应该负主要责任，不要揣着明白装糊涂。"],
    say=["Tiếp theo là 任也 và 揣着明白装糊涂.",
         F(0, "任……也…… nghĩa là dù… cũng…, biểu thị điều kiện có khác nhau thế nào thì kết quả vẫn như nhau. 任 là liên từ, giống 无论; sau nó thường là đại từ nghi vấn như 谁，怎么，什么. Cụm hay gặp nhất là 任谁也, dù là ai cũng."),
         F(1, "Ví dụ từ bài khóa: 今日头条早已声名在外，任谁也不会这么明目张胆地模仿和盗版。 Dù là ai cũng không dám nhái trắng trợn như vậy."),
         F(2, "这是不可抗力的天灾，任谁也无可奈何啊！ Đây là thiên tai bất khả kháng, dù là ai cũng đành bó tay thôi! 不可抗力 là bất khả kháng, cũng là một thuật ngữ pháp lý."),
         F(3, "任你们怎么说，我也不会改变自己的想法。 Dù các anh nói thế nào, tôi cũng sẽ không thay đổi suy nghĩ của mình."),
         F(4, "揣着明白装糊涂: 揣 đọc chuāi, là giấu trong người, trong ngực áo. Ôm sự hiểu biết trong lòng mà giả vờ hồ đồ, tức là biết rõ mà vờ như không biết. Câu này mang ý chê trách."),
         F(5, "Ví dụ từ bài khóa: 对此今日油条相关负责人揣着明白装糊涂，直言自己不知道哪个字不能用。"),
         F(6, "他什么事都知道，却揣着明白装糊涂，一问三不知。 Chuyện gì anh ta cũng biết, nhưng lại vờ như không biết, hỏi gì cũng không biết. 一问三不知 là hỏi một câu thì ba điều không biết."),
         F(7, "公司出了这个问题，你应该负主要责任，不要揣着明白装糊涂。 Công ty xảy ra vấn đề này, anh phải chịu trách nhiệm chính, đừng có biết rồi còn giả vờ không biết.")])

add("bullets", chapter="Mẫu câu: 令…不解 · 乍听起来 · 明摆着 · 就…而言", section="Mẫu câu 重点句型", title="5. 令……不解 · 6. 乍听起来……", size=33,
    items=["## 令/让……不解: khiến… không hiểu nổi",
           "大公司《今日头条》起诉卖油条的小公司今日油条，这也令他不解。",
           "他拿着那么高的工资，开着这么破的车，实在是令人不解。",
           "昨天的会上，他说了很多莫名其妙的话，事后什么事情都没有，简直令人不解。",
           "## 乍听起来……(实则/实际上……): thoạt nghe thì… (nhưng thực ra…)",
           "乍听起来，“今日油条”抖得一手好机灵，起名者的创意和脑洞也着实让人佩服。",
           "他说的话乍听起来好像很厉害，实则经不起仔细推敲。",
           "乍听起来，他这样的推销语言充满吸引力，实际上只是花言巧语罢了。"],
    say=["Tiếp theo là 令不解 và 乍听起来.",
         F(0, "令……不解 nghĩa là khiến ai đó không hiểu nổi. 令 là khiến, làm cho, văn viết hơn 让. Hay gặp nhất là 令人不解, khiến người ta khó hiểu."),
         F(1, "Ví dụ từ bài khóa: 大公司今日头条起诉卖油条的小公司今日油条，这也令他不解。"),
         F(2, "他拿着那么高的工资，开着这么破的车，实在是令人不解。 Anh ấy lĩnh lương cao như thế mà lại đi chiếc xe cũ nát thế này, thật khiến người ta khó hiểu."),
         F(3, "昨天的会上，他说了很多莫名其妙的话，事后什么事情都没有，简直令人不解。 Trong cuộc họp hôm qua, anh ấy nói rất nhiều câu khó hiểu, sau đó lại chẳng có chuyện gì, thật không hiểu nổi. 莫名其妙 là không hiểu ra sao."),
         F(4, "乍听起来 nghĩa là thoạt nghe, mới nghe qua. 乍 là vừa mới, đột nhiên. Vế sau thường có 实则, 实际上, 然而 để nói sự thật khác với ấn tượng ban đầu. Tương tự có 乍一看, thoạt nhìn."),
         F(5, "Ví dụ từ bài khóa: 乍听起来，今日油条抖得一手好机灵，起名者的创意和脑洞也着实让人佩服。 Câu sau của bài khóa bắt đầu bằng 然而."),
         F(6, "他说的话乍听起来好像很厉害，实则经不起仔细推敲。 Lời anh ta nói thoạt nghe có vẻ rất ghê gớm, thực ra không chịu nổi sự xem xét kỹ. 推敲 là cân nhắc, xem xét kỹ từng chữ."),
         F(7, "乍听起来，他这样的推销语言充满吸引力，实际上只是花言巧语罢了。 Thoạt nghe, lời chào hàng của anh ta đầy sức hấp dẫn, nhưng thực ra chỉ là lời đường mật mà thôi. 花言巧语 là lời hoa mỹ, đường mật.")])

add("bullets", section="Mẫu câu 重点句型", title="7. 明摆着…… · 8. 就……而言", size=33,
    items=["## 明摆着……: rõ rành rành, bày ra trước mắt",
           "明摆着是两种行业，消费者怎么可能混淆呢？",
           "你们真无聊！谁对谁错不是明摆着的吗？有什么好争的！",
           "他明摆着没兴趣，你就不要硬拉他入伙了！",
           "## 就……而言: xét về…, đối với… mà nói",
           "就此事儿而言，今日油条是否构成侵权，确需法律层面的定性……",
           "就这件事而言，他做得不无道理。",
           "小赵说：“选择去一线城市工作，就我而言，主要考虑的是城市未来的发展前景。”"],
    say=["Tiếp theo là 明摆着 và 就而言.",
         F(0, "明摆着 nghĩa là bày ra rõ ràng trước mắt, ai cũng thấy, không cần giải thích. Có thể đứng trước động từ, cụm động từ, hoặc làm vị ngữ theo mẫu 是明摆着的. Thường dùng trong khẩu ngữ, có khi mang giọng bực bội."),
         F(1, "Ví dụ từ bài khóa: 明摆着是两种行业，消费者怎么可能混淆呢？ Rõ ràng là hai ngành khác nhau, người tiêu dùng sao nhầm được?"),
         F(2, "你们真无聊！谁对谁错不是明摆着的吗？有什么好争的！ Các cậu thật vô vị! Ai đúng ai sai chẳng phải đã rõ rành rành sao? Có gì mà cãi!"),
         F(3, "他明摆着没兴趣，你就不要硬拉他入伙了！ Rõ ràng là anh ấy không có hứng thú, cậu đừng cố kéo anh ấy nhập hội nữa! 入伙 là nhập hội, góp vốn làm ăn chung."),
         F(4, "就……而言 nghĩa là xét về mặt nào đó, đối với ai đó mà nói, giống 对来说 nhưng văn viết hơn. Dùng để giới hạn phạm vi của nhận xét."),
         F(5, "Ví dụ từ bài khóa: 就此事而言，今日油条是否构成侵权，确需法律层面的定性。 Riêng về việc này mà nói."),
         F(6, "就这件事而言，他做得不无道理。 Xét riêng chuyện này, anh ấy làm cũng không phải không có lý. 不无道理 là phủ định kép, nghĩa là cũng có lý."),
         F(7, "小赵说：选择去一线城市工作，就我而言，主要考虑的是城市未来的发展前景。 Tiểu Triệu nói: chọn đến thành phố tuyến một làm việc, đối với tôi mà nói, điều chủ yếu cân nhắc là triển vọng phát triển tương lai của thành phố. 一线城市 là thành phố hạng một như Bắc Kinh, Thượng Hải.")])

add("bullets", chapter="Mẫu câu: 近乎 · 说到底 · 落到实处", section="Mẫu câu 重点句型", title="9. 近乎…… · 10. 说到底……", size=33,
    items=["## 近乎……: gần như… (văn viết)",
           "……可名字近乎“高仿”，商标标志跟字体也高度相似，这很难不遭受质疑。",
           "最近他刷抖音刷得近乎疯狂。",
           "那次意外被困于井下，他在近乎绝望的情况下，还是凭着顽强的毅力挺了过来。",
           "## 说到底……: suy cho cùng, nói cho cùng",
           "说到底，只有对恶意抢注行为果断说“不”，……正常的营商环境才会更有保障……",
           "人生说到底是自己的选择，自己的路在自己的脚下。",
           "写小说，说到底，就是写人物。小说艺术的精髓就是塑造人物。"],
    say=["Tiếp theo là 近乎 và 说到底.",
         F(0, "近乎 nghĩa là gần như, tiếp cận với một trạng thái nào đó, văn viết hơn 几乎. Thường đứng trước tính từ hay danh từ chỉ mức độ cao, như 近乎疯狂, gần như điên cuồng; 近乎绝望, gần như tuyệt vọng."),
         F(1, "Ví dụ từ bài khóa: 可名字近乎高仿，商标标志跟字体也高度相似，这很难不遭受质疑。 Cái tên gần như nhái loại một."),
         F(2, "最近他刷抖音刷得近乎疯狂。 Gần đây anh ấy lướt Douyin đến mức gần như phát cuồng."),
         F(3, "那次意外被困于井下，他在近乎绝望的情况下，还是凭着顽强的毅力挺了过来。 Lần bị mắc kẹt dưới giếng mỏ vì tai nạn ấy, trong hoàn cảnh gần như tuyệt vọng, anh ấy vẫn dựa vào nghị lực kiên cường mà vượt qua. 挺过来 là gắng gượng vượt qua."),
         F(4, "说到底 nghĩa là nói đến tận cùng, suy cho cùng. Dùng để đưa ra kết luận, chỉ ra bản chất của vấn đề sau khi đã phân tích. Thường đứng đầu câu hoặc sau chủ ngữ."),
         F(5, "Ví dụ từ bài khóa: 说到底，只有对恶意抢注行为果断说不，不纵容商标恶意抢注，正常的营商环境才会更有保障。 Câu kết luận của cả bài. 纵容 là dung túng."),
         F(6, "人生说到底是自己的选择，自己的路在自己的脚下。 Suy cho cùng, đời người là lựa chọn của chính mình, con đường của mình nằm dưới chân mình."),
         F(7, "写小说，说到底，就是写人物。小说艺术的精髓就是塑造人物。 Viết tiểu thuyết, nói cho cùng, là viết về nhân vật. Tinh túy của nghệ thuật tiểu thuyết là xây dựng nhân vật.")])

add("bullets", section="Mẫu câu 重点句型", title="11. 将（把）……落到实处", size=34,
    items=["## 将/把 + kế hoạch, biện pháp, chính sách + 落到实处: biến thành hiện thực, thực hiện đến nơi đến chốn",
           "……正常的营商环境才会更有保障，也才能将知识产权的保护更好地落到实处。",
           "只要我们不失时机，尽一切可能将政策落到实处，就一定能够实现全年经济增长目标。",
           "我们要把为人民服务的宗旨落到实处，全心全意地为老百姓谋福利。",
           "Kết hợp hay gặp: 把责任落到实处 · 把工作落到实处 · 把措施落到实处"],
    say=["Điểm cuối cùng là 将落到实处.",
         F(0, "将 hoặc 把, cộng một kế hoạch, biện pháp, chính sách, rồi đến 落到实处, nghĩa là làm cho nó rơi xuống chỗ thực, tức là thực hiện đến nơi đến chốn, không chỉ nói suông trên giấy. Đây là cách nói rất hay gặp trong văn bản chính thức và báo chí Trung Quốc."),
         F(1, "Ví dụ từ bài khóa: 也才能将知识产权的保护更好地落到实处。 Mới có thể thực sự đưa việc bảo vệ sở hữu trí tuệ vào cuộc sống."),
         F(2, "只要我们不失时机，尽一切可能将政策落到实处，就一定能够实现全年经济增长目标。 Chỉ cần chúng ta không bỏ lỡ thời cơ, dốc hết khả năng thực hiện chính sách đến nơi đến chốn, thì nhất định sẽ đạt được mục tiêu tăng trưởng kinh tế cả năm. 不失时机 là không để lỡ thời cơ."),
         F(3, "我们要把为人民服务的宗旨落到实处，全心全意地为老百姓谋福利。 Chúng ta phải thực hiện đến nơi đến chốn tôn chỉ phục vụ nhân dân, toàn tâm toàn ý mưu cầu phúc lợi cho dân. 宗旨 là tôn chỉ; 谋福利 là mưu cầu phúc lợi."),
         F(4, "Những kết hợp hay gặp: 把责任落到实处, 把工作落到实处, 把措施落到实处. Người Việt cũng hay nói đưa nghị quyết vào cuộc sống, chính là ý này.")])

# ======================= KẾT HỢP TỪ & THÀNH NGỮ =======================
add("bullets", chapter="Kết hợp từ & thành ngữ", section="Kết hợp từ 词语搭配", title="Kết hợp từ: 蹭～ · 经受～ · 恶意～", size=34,
    items=["## 蹭: ～饭 ăn chực · ～网 dùng ké wifi · ～课 học ké · ～热度 ăn theo độ hot",
           "弟弟回家一开冰箱，发现只剩鸡蛋，便决定去朋友家蹭一顿饭。",
           "## 经受: ～考验 · ～折磨 · ～打击 · ～历练 · ～磨炼",
           "哥哥大学毕业后参了军，在部队里经受了磨炼。",
           "## 恶意: ～中伤 bôi nhọ · ～冲撞 · ～打压 chèn ép · ～蛊惑 mê hoặc",
           "他的这些罪名都是子虚乌有的，完全是背后有人恶意抹黑。"],
    say=["Tiếp theo là phần kết hợp từ.",
         F(0, "蹭 đi với 饭, ăn chực; 网, dùng ké mạng; 课, đi học ké lớp không đăng ký; và 热度, ăn theo độ hot. Sinh viên Trung Quốc rất hay 蹭课, vào nghe giảng ké ở các trường danh tiếng."),
         F(1, "Ví dụ: 弟弟回家一开冰箱，发现只剩鸡蛋，便决定去朋友家蹭一顿饭。 Em trai về nhà mở tủ lạnh, thấy chỉ còn trứng, bèn quyết định sang nhà bạn ăn chực một bữa."),
         F(2, "经受 đi với 考验, thử thách; 折磨, giày vò; 打击, đả kích; 历练, trải nghiệm rèn giũa; 磨炼, tôi luyện. Đều là những điều gian khổ. Thêm 住 thành 经受住, chịu đựng được."),
         F(3, "Ví dụ: 哥哥大学毕业后参了军，在部队里经受了磨炼。 Anh trai tốt nghiệp đại học xong thì nhập ngũ, được tôi luyện trong quân đội."),
         F(4, "恶意 làm trạng ngữ, đi với 中伤, bôi nhọ, vu khống, chữ 中 đọc thanh bốn; 冲撞, va chạm, xúc phạm; 打压, chèn ép; 蛊惑, mê hoặc, kích động. Trong bài là 恶意抢注."),
         F(5, "Ví dụ: 他的这些罪名都是子虚乌有的，完全是背后有人恶意抹黑。 Những tội danh này của anh ấy đều là bịa đặt, hoàn toàn là có kẻ sau lưng cố ý bôi đen. 子虚乌有 là chuyện hư cấu, không có thật; 抹黑 là bôi đen, bôi nhọ.")])

add("bullets", section="Thành ngữ 成语和惯用语", title="Thành ngữ (1): 亦庄亦谐 · 微乎其微 · 声名在外 · 明目张胆", size=33,
    items=["## 亦庄亦谐 yìzhuāng-yìxié – vừa nghiêm túc vừa hài hước",
           "他扮演的这个角色，亦庄亦谐，让人十分喜欢。",
           "## 微乎其微 wēihūqíwēi – rất ít, rất nhỏ, nhỏ nhoi",
           "今年的研究生考试，竞争特别激烈，他考上的可能性微乎其微。",
           "## 声名在外 shēngmíng-zàiwài – tiếng tăm vang xa",
           "尽管他已经声名在外了，但是在本单位他还是个小讲师。",
           "## 明目张胆 míngmù-zhāngdǎn – trắng trợn, không kiêng nể gì",
           "考试时，他居然明目张胆地作弊，一点羞耻心都没有。"],
    say=["Bài này có mười hai thành ngữ và quán dụng ngữ, trong đó có nhiều từ lóng mạng. Chúng ta học từng nhóm bốn.",
         F(0, "亦庄亦谐: 亦 là cũng, 庄 là trang nghiêm, 谐 là hài hước. Vừa nghiêm túc vừa hài hước, thường dùng để khen lời nói, bài viết, vai diễn."),
         F(1, "Ví dụ: 他扮演的这个角色，亦庄亦谐，让人十分喜欢。 Vai diễn của anh ấy vừa nghiêm túc vừa hài hước, rất được yêu thích."),
         F(2, "微乎其微: 微 là nhỏ, 乎 là trợ từ văn ngôn. Nhỏ lại càng nhỏ, chỉ số lượng hay khả năng rất ít, rất nhỏ. Thường đi với 可能性，概率，希望."),
         F(3, "Ví dụ: 今年的研究生考试，竞争特别激烈，他考上的可能性微乎其微。 Kỳ thi cao học năm nay cạnh tranh đặc biệt gay gắt, khả năng anh ấy đỗ là vô cùng nhỏ."),
         F(4, "声名在外: 声名 là danh tiếng. Tiếng tăm lan ra bên ngoài, tức rất nổi tiếng."),
         F(5, "Ví dụ: 尽管他已经声名在外了，但是在本单位他还是个小讲师。 Tuy anh ấy đã nổi tiếng bên ngoài, nhưng ở đơn vị mình thì vẫn chỉ là một giảng viên nhỏ."),
         F(6, "明目张胆: 明目 là mở to mắt, 张胆 là gan to. Nghĩa là trắng trợn, công khai làm việc xấu mà không chút kiêng sợ. Luôn mang nghĩa chê, thường làm trạng ngữ với 地."),
         F(7, "Ví dụ: 考试时，他居然明目张胆地作弊，一点羞耻心都没有。 Lúc thi, cậu ta lại dám trắng trợn gian lận, chẳng có chút liêm sỉ nào.")])

add("bullets", section="Thành ngữ 成语和惯用语", title="Thành ngữ (2): 措手不及 · 抱大腿 · 抖机灵 · 脑洞大开", size=33,
    items=["## 措手不及 cuòshǒu-bùjí – trở tay không kịp",
           "必须做好防洪抗灾准备工作，以免汛期到来时措手不及。",
           "## 抱大腿 bào dàtuǐ – ôm đùi: dựa vào thế của người khác để hưởng lợi (từ lóng mạng)",
           "自己在这儿也是人生地不熟，能抱上大腿总比一个人瞎闯要好得多。",
           "## 抖机灵 dǒu jīling – khoe khôn, giở trò khôn vặt (phương ngữ phương Bắc, ý chê)",
           "善良对于一个情感节目主持人而言是非常重要的，它比抖机灵更能赢得人心。",
           "## 脑洞大开 nǎodòng dàkāi – trí tưởng tượng bay bổng, kỳ lạ đến bất ngờ",
           "在老师的启发下，同学们脑洞大开，造出了很多精彩的句子。"],
    say=[F(0, "措手不及: 措手 là ra tay xử lý. Sự việc đến quá bất ngờ, không kịp ứng phó, tức là trở tay không kịp. Hay dùng mẫu 打了个措手不及, đánh cho trở tay không kịp."),
         F(1, "Ví dụ: 必须做好防洪抗灾准备工作，以免汛期到来时措手不及。 Phải chuẩn bị tốt công tác phòng lũ chống thiên tai, kẻo khi mùa lũ đến lại trở tay không kịp. 汛期 là mùa lũ."),
         F(2, "抱大腿: từ lóng mạng, nghĩa đen là ôm lấy đùi, chỉ việc dựa vào ưu thế của người khác để hưởng lợi. Giữa bạn bè, nó còn được dùng để trêu đùa, tự giễu: 大神，求抱大腿！ Cao thủ ơi, cho em bám với!"),
         F(3, "Ví dụ: 自己在这儿也是人生地不熟，能抱上大腿总比一个人瞎闯要好得多。 Mình ở đây cũng lạ người lạ đất, bám được vào ai đó vẫn hơn nhiều so với một mình đâm đầu loạn xạ. 人生地不熟 là lạ nước lạ cái."),
         F(4, "抖机灵: phương ngữ phương Bắc. 抖 là giũ, khoe ra; 机灵 là lanh lợi. Nghĩa là khoe sự lanh lợi của mình, giở trò khôn vặt, có ý chê nhẹ."),
         F(5, "Ví dụ: 善良对于一个情感节目主持人而言是非常重要的，它比抖机灵更能赢得人心。 Lòng tốt rất quan trọng với người dẫn chương trình tư vấn tình cảm, nó chiếm được lòng người hơn là khoe khôn vặt. Câu này lại có mẫu 对于而言."),
         F(6, "脑洞大开: trí tưởng tượng bay bổng tự do, liên tưởng cực kỳ phong phú, kỳ lạ, thậm chí đến mức khiến người ta kinh ngạc. Thường mang ý khen."),
         F(7, "Ví dụ: 在老师的启发下，同学们脑洞大开，造出了很多精彩的句子。 Được thầy gợi mở, các bạn học sinh tha hồ tưởng tượng, đặt được rất nhiều câu hay.")])

add("bullets", section="Thành ngữ 成语和惯用语", title="Thành ngữ (3): 蹭IP · 井水不犯河水 · 打擦边球 · 搭便车", size=32,
    items=["## 蹭IP（热度）– ăn theo hình ảnh, thương hiệu, sự kiện nổi tiếng để được chú ý",
           "这位网红通过蹭IP，赚了许多关注度。",
           "## 井水不犯河水 – nước giếng không phạm nước sông: ai lo việc nấy, không đụng chạm nhau",
           "你干你的，我干我的，咱们井水不犯河水。",
           "## 打擦边球 dǎ cābiānqiú – đánh bóng sượt mép bàn: lách luật, làm ở sát ranh giới quy định",
           "有的企业通过打擦边球广告来吸引消费者的目光。",
           "## 搭便车 dā biànchē – đi nhờ xe: không bỏ công mà hưởng thành quả của người khác",
           "……家居行业更是“搭便车”现象的高发区。"],
    say=[F(0, "蹭IP, còn nói là 蹭热度: IP ở đây là hình ảnh, thương hiệu, nhân vật nổi tiếng mà ai cũng biết. Mượn hình ảnh hay sự kiện nổi tiếng để bản thân lọt vào tầm mắt công chúng, tăng độ chú ý, tức là ăn theo."),
         F(1, "Ví dụ: 这位网红通过蹭IP，赚了许多关注度。 Người nổi tiếng trên mạng này nhờ ăn theo hình ảnh nổi tiếng mà kiếm được rất nhiều lượt chú ý."),
         F(2, "井水不犯河水: nước giếng ở trong giếng, nước sông ở trong sông, hai bên không bao giờ gặp nhau. Ví với việc không can thiệp vào nhau, không có mâu thuẫn xung đột."),
         F(3, "Ví dụ: 你干你的，我干我的，咱们井水不犯河水。 Anh làm việc của anh, tôi làm việc của tôi, chúng ta nước giếng không phạm nước sông."),
         F(4, "打擦边球: trong bóng bàn, 擦边球 là quả bóng sượt qua mép bàn, vẫn được tính điểm. Về sau ví với việc làm ở sát ranh giới quy định mà không vi phạm, tức là lách luật."),
         F(5, "Ví dụ: 有的企业通过打擦边球广告来吸引消费者的目光。 Có doanh nghiệp dùng quảng cáo lách luật để thu hút ánh mắt người tiêu dùng."),
         F(6, "搭便车: nghĩa gốc là đi nhờ một chiếc xe thuận đường, không mất tiền. Nghĩa bóng là không bỏ công sức mà ngồi hưởng thành quả lao động của người khác."),
         F(7, "Ví dụ: 各行各业都出现了大大小小的精明商家，欲免费从前人身上分一杯现成的羹，家居行业更是搭便车现象的高发区。 Ngành nào cũng có những nhà buôn khôn lỏi muốn chia phần canh có sẵn của người đi trước; ngành nội thất lại càng là vùng hay xảy ra hiện tượng đi nhờ xe. 分一杯羹 là chia một bát canh, tức chia phần lợi.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 课后练习", title="Bài tập 1: Chọn từ điền vào chỗ trống (1)", reveal=True, size=35,
    items=["## 刷 · 微乎其微 · 蹭 · 屡屡 · 措手不及 · 追究",
           "(1) 有乘客到站了都没有要下车的意思，要继续___网看电影。",
           "Đáp án: 蹭 – 蹭网 dùng ké mạng",
           "(2) 对于过去的事情，如果你能改过自新，我们就不再___你的责任了。",
           "Đáp án: 追究 – 追究责任 truy cứu trách nhiệm",
           "(3) 前一阵子领导突然来检查，搞得我们___。",
           "Đáp án: 措手不及"],
    say=["Bây giờ chúng ta sang phần luyện tập của sách. Bài tập một: chọn từ thích hợp điền vào chỗ trống. Có sáu từ: 刷，微乎其微，蹭，屡屡，措手不及，追究.",
         F(1, "Câu một: 有乘客到站了都没有要下车的意思，要继续什么网看电影。 Có hành khách đến bến rồi mà chẳng có ý định xuống xe, còn muốn tiếp tục làm gì mạng để xem phim. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 蹭. 蹭网 là dùng ké wifi, ở đây là wifi miễn phí trên xe buýt."),
         F(3, "Câu hai: 对于过去的事情，如果你能改过自新，我们就不再什么你的责任了。 Với những chuyện đã qua, nếu anh biết hối cải làm lại, chúng tôi sẽ không làm gì trách nhiệm của anh nữa. 改过自新 là sửa lỗi làm người mới."),
         F(4, "Đáp án: 追究. 追究责任, truy cứu trách nhiệm, một kết hợp các bạn đã gặp trong bài khóa."),
         F(5, "Câu ba: 前一阵子领导突然来检查，搞得我们什么。 Dạo trước lãnh đạo bất ngờ đến kiểm tra, làm chúng tôi thế nào?"),
         F(6, "Đáp án: 措手不及. Lãnh đạo đến đột ngột nên trở tay không kịp.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 1: Chọn từ điền vào chỗ trống (2)", reveal=True, size=35,
    items=["(4) 这种病目前还没有特效药可以医治，要康复的概率可以说是___。",
           "Đáp án: 微乎其微",
           "(5) 无聊的时候___微博、看视频，很容易打发时间。",
           "Đáp án: 刷 – 刷微博 lướt Weibo",
           "(6) 尽管我___劝告他，但是他还是不听劝，执意要按照自己的想法来做。",
           "Đáp án: 屡屡 – nhiều lần"],
    say=[F(0, "Câu bốn: 这种病目前还没有特效药可以医治，要康复的概率可以说是什么。 Bệnh này hiện chưa có thuốc đặc trị, xác suất khỏi bệnh có thể nói là thế nào?"),
         F(1, "Đáp án: 微乎其微. 概率微乎其微, xác suất vô cùng nhỏ, giống hệt câu trong bài khóa."),
         F(2, "Câu năm: 无聊的时候什么微博、看视频，很容易打发时间。 Lúc buồn chán thì làm gì Weibo, xem video, rất dễ giết thời gian."),
         F(3, "Đáp án: 刷. 刷微博 là lướt Weibo; tương tự 刷抖音, 刷朋友圈. 打发时间 là giết thời gian."),
         F(4, "Câu sáu: 尽管我什么劝告他，但是他还是不听劝，执意要按照自己的想法来做。 Tuy tôi đã thế nào khuyên anh ấy, nhưng anh ấy vẫn không nghe, khăng khăng làm theo ý mình."),
         F(5, "Đáp án: 屡屡, nhiều lần, liên tục, phó từ văn viết. Trong bài khóa có tiêu đề 屡屡被打擦边球. 执意 là khăng khăng.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn từ thích hợp nhất", reveal=True, size=33,
    items=["(1) 他这次的演唱会重金（  ），登峰造极，让他的演艺生涯又达到巅峰。 A.创造 B.打造 C.制造 D.构造",
           "Đáp án: B 打造 – 重金打造 đầu tư lớn để dày công xây dựng",
           "(2) 在赛场上，他优异的表现让人（  ）得五体投地。 A.克服 B.佩服 C.说服 D.征服",
           "Đáp án: B 佩服 – 佩服得五体投地 phục sát đất",
           "(3) 当我们的合法权益受到（  ）时，我们应该拿起法律的武器保护自己。 A.侵权 B.危害 C.侵害 D.伤害",
           "Đáp án: C 侵害 – 合法权益受到侵害"],
    say=["Bài tập hai: chọn từ thích hợp nhất.",
         F(0, "Câu một: 他这次的演唱会重金什么，登峰造极，让他的演艺生涯又达到巅峰。 Buổi hòa nhạc lần này được đầu tư lớn, đạt đến đỉnh cao, đưa sự nghiệp của anh ấy lên tột đỉnh lần nữa. A, 创造; B, 打造; C, 制造; D, 构造."),
         F(1, "Đáp án: B, 打造. 重金打造 là bỏ nhiều tiền ra dày công xây dựng, rất hay gặp với buổi diễn, bộ phim, thương hiệu. Bài khóa cũng có 知名品牌是经过多年打造而成的. 创造 là sáng tạo ra cái mới, 制造 là chế tạo sản phẩm, 构造 là cấu tạo."),
         F(2, "Câu hai: 在赛场上，他优异的表现让人什么得五体投地。 Trên sân đấu, màn thể hiện xuất sắc của anh ấy khiến người ta thế nào sát đất. A, 克服; B, 佩服; C, 说服; D, 征服."),
         F(3, "Đáp án: B, 佩服. 佩服得五体投地 là phục sát đất; 五体投地 là năm vóc gieo xuống đất, cách lạy cung kính nhất. 征服 là chinh phục, phải có tân ngữ, không đi với 五体投地."),
         F(4, "Câu ba: 当我们的合法权益受到什么时，我们应该拿起法律的武器保护自己。 Khi quyền lợi hợp pháp của chúng ta bị gì, chúng ta nên cầm lấy vũ khí pháp luật để tự bảo vệ. A, 侵权; B, 危害; C, 侵害; D, 伤害."),
         F(5, "Đáp án: C, 侵害. 权益受到侵害 là quyền lợi bị xâm hại, một kết hợp cố định. 侵权 bản thân đã chứa chữ 权, nghĩa là xâm phạm quyền, nên không nói 权益受到侵权. 危害 hay đi với 健康，安全; 伤害 hay đi với 身体，感情.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn từ thích hợp nhất (tiếp)", reveal=True, size=34,
    items=["(4) 这一起知识产权纠纷案，最终被秦淮区法院（  ）为侵权。 A.判定 B.判决 C.决断 D.鉴定",
           "Đáp án: A 判定 – 被判定为…… được xác định là…",
           "(5) 钱不是万能的，没有钱是（  ）不能的。 A.万万 B.万一 C.一旦 D.千万",
           "Đáp án: A 万万 – 万万不能 tuyệt đối không thể"],
    say=[F(0, "Câu bốn: 这一起知识产权纠纷案，最终被秦淮区法院什么为侵权。 Vụ tranh chấp sở hữu trí tuệ này cuối cùng đã bị tòa án quận Tần Hoài làm gì là xâm phạm quyền. A, 判定; B, 判决; C, 决断; D, 鉴定."),
         F(1, "Đáp án: A, 判定. Mẫu 判定为 là xác định là, phán quyết là, giống 被判定为中国驰名商标 trong bài khóa. 判决 là tuyên án, phía sau thường là nội dung bản án, không đi với 为; 决断 là quyết đoán; 鉴定 là giám định."),
         F(2, "Câu năm: 钱不是万能的，没有钱是什么不能的。 Tiền không phải là vạn năng, nhưng không có tiền thì thế nào cũng không xong. A, 万万; B, 万一; C, 一旦; D, 千万."),
         F(3, "Đáp án: A, 万万. 万万不能 là tuyệt đối không thể; câu này chơi chữ với 万能, vạn năng. 千万 cũng là nhất thiết, nhưng dùng trong câu khuyên bảo, như 千万别忘了, nhất định đừng quên; còn 万一 là lỡ như, 一旦 là một khi.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ ngữ, mẫu câu cho sẵn trả lời câu hỏi (1)", reveal=True, size=33,
    items=["(1) “今日油条”负责人因什么而困惑，他的理由是什么？（令……不解）",
           "Đáp án gợi ý: 大公司《今日头条》起诉卖油条的小公司，这令他不解。他的理由是：他天天刷《今日头条》，是忠实用户，“傍大牌”只是觉得好玩而已。",
           "(2) 在名字上，为什么“今日油条”容易遭受质疑？（近乎……）",
           "Đáp án gợi ý: 因为“今日油条”的名字近乎“高仿”，跟《今日头条》只差一个字，商标标识和字体也高度相似。"],
    say=["Bài tập ba: dùng từ ngữ và mẫu câu cho sẵn để trả lời câu hỏi về bài khóa. Thầy đưa ra đáp án gợi ý, các bạn có thể trả lời theo cách của mình.",
         F(0, "Câu một: 今日油条负责人因什么而困惑，他的理由是什么？ Người phụ trách tiệm quẩy thắc mắc vì điều gì, lý do của anh ta là gì? Dùng 令不解."),
         F(1, "Gợi ý: 大公司今日头条起诉卖油条的小公司，这令他不解。他的理由是：他天天刷今日头条，是忠实用户，傍大牌只是觉得好玩而已。 Công ty lớn kiện công ty nhỏ bán quẩy, điều này khiến anh ta không hiểu. Lý do: ngày nào anh ta cũng lướt Tin nóng hôm nay, là người dùng trung thành, bám thương hiệu lớn chỉ là cho vui."),
         F(2, "Câu hai: 在名字上，为什么今日油条容易遭受质疑？ Về mặt tên gọi, vì sao Quẩy hôm nay dễ bị nghi vấn? Dùng 近乎."),
         F(3, "Gợi ý: 因为今日油条的名字近乎高仿，跟今日头条只差一个字，商标标识和字体也高度相似。 Vì cái tên gần như nhái loại một, chỉ khác Tin nóng hôm nay đúng một chữ, biểu tượng và kiểu chữ cũng giống nhau đến mức cao độ.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ ngữ, mẫu câu cho sẵn trả lời câu hỏi (2)", reveal=True, size=33,
    items=["(3) 为什么要对恶意抢注商标行为果断说“不”？（把/将……落到实处）",
           "Đáp án gợi ý: 因为只有对恶意抢注行为果断说“不”，正常的营商环境才会更有保障，也才能将知识产权的保护落到实处。",
           "(4) 面对网友的质疑，今日油条相关负责人的表现是什么？（揣着明白装糊涂）",
           "Đáp án gợi ý: 他揣着明白装糊涂，直言自己不知道哪个字不能用，还说“傍大牌”只是觉得好玩。"],
    say=[F(0, "Câu ba: 为什么要对恶意抢注商标行为果断说不？ Vì sao phải dứt khoát nói không với hành vi ác ý đăng ký chặn trước nhãn hiệu? Dùng 将落到实处."),
         F(1, "Gợi ý: 因为只有对恶意抢注行为果断说不，正常的营商环境才会更有保障，也才能将知识产权的保护落到实处。 Vì chỉ có dứt khoát nói không, môi trường kinh doanh bình thường mới được bảo đảm, việc bảo vệ sở hữu trí tuệ mới đi vào thực chất."),
         F(2, "Câu bốn: 面对网友的质疑，今日油条相关负责人的表现是什么？ Trước nghi vấn của cư dân mạng, người phụ trách tiệm quẩy đã thể hiện thế nào? Dùng 揣着明白装糊涂."),
         F(3, "Gợi ý: 他揣着明白装糊涂，直言自己不知道哪个字不能用，还说傍大牌只是觉得好玩。 Anh ta biết rõ mà vờ không biết, nói thẳng là mình không biết chữ nào không được dùng, còn bảo bám thương hiệu lớn chỉ là cho vui.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Chọn từ điền vào đoạn văn", reveal=True, size=33,
    items=["## 碰瓷 · 母公司 · 微乎其微 · 明目张胆 · 梯队 · 措手不及 · 声名在外",
           "《今日头条》的___字节跳动作为中国第一___的互联网大厂，这种事情发生的概率可以说是___。一来《今日头条》早已___，哪怕是模仿和盗版，任谁也不会这么___；二来这样的跨行业模仿，《今日头条》也是被打了个___，万万没想到一家餐饮连锁店居然“___营销”到互联网企业的头上！",
           "Đáp án: 母公司 · 梯队 · 微乎其微 · 声名在外 · 明目张胆 · 措手不及 · 碰瓷"],
    say=["Bài tập bốn: chọn từ điền vào đoạn văn. Có bảy từ: 碰瓷，母公司，微乎其微，明目张胆，梯队，措手不及，声名在外.",
         F(1, "今日头条的什么字节跳动作为中国第一什么的互联网大厂，这种事情发生的概率可以说是什么。一来今日头条早已什么，哪怕是模仿和盗版，任谁也不会这么什么；二来这样的跨行业模仿，今日头条也是被打了个什么，万万没想到一家餐饮连锁店居然什么营销到互联网企业的头上！ Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 母公司，第一梯队，微乎其微，声名在外，明目张胆，措手不及，碰瓷营销。"),
         F(2, "Các bạn thấy không, đây chính là đoạn ba của bài khóa. Gợi ý: sau 第一 phải là 梯队; sau 概率可以说是 là 微乎其微; còn trước 营销 là 碰瓷. Hãy đọc to cả đoạn vài lần để nhớ cả bảy từ nhé.")])

add("bullets", chapter="Liên hệ: hàng nhái & nhãn hiệu ở Việt Nam", section="Thảo luận 讨论", title="Liên hệ Việt Nam: hàng nhái, “ăn theo” và đăng ký chặn trước", size=33,
    items=["Luật Sở hữu trí tuệ Việt Nam: nhãn hiệu bảo hộ theo nhóm đã đăng ký; “nhãn hiệu nổi tiếng” được bảo hộ rộng hơn ≈ 驰名商标",
           "抢注 ở nước ngoài: cà phê Trung Nguyên từng bị đăng ký trước tại Mỹ; tên “Buôn Ma Thuột” từng bị một công ty Trung Quốc đăng ký nhãn hiệu",
           "Từ lóng tương ứng: hàng fake loại 1 ≈ 高仿 · ăn theo ≈ 蹭热度 · đi nhờ xe ≈ 搭便车 · lách luật ≈ 打擦边球",
           "Câu hỏi: 你会买山寨货吗？为什么？ · 小店起名“傍大牌”，你觉得可以接受吗？"],
    say=["Trước khi tổng kết, chúng ta cùng liên hệ với Việt Nam.",
         F(0, "Việt Nam có Luật Sở hữu trí tuệ, cũng theo nguyên tắc giống như luật sư trong bài nói: nhãn hiệu được bảo hộ theo nhóm hàng hóa, dịch vụ đã đăng ký. Riêng nhãn hiệu nổi tiếng thì được bảo hộ rộng hơn, cả với những hàng hóa không cùng loại, rất giống 驰名商标 của Trung Quốc."),
         F(1, "Doanh nghiệp Việt Nam cũng từng là nạn nhân của 抢注. Thương hiệu cà phê Trung Nguyên từng bị một công ty đăng ký trước tại Mỹ; cái tên Buôn Ma Thuột, vùng cà phê nổi tiếng, cũng từng bị một công ty Trung Quốc đăng ký làm nhãn hiệu, Việt Nam phải mất nhiều năm mới đòi lại được. Bài học là: muốn ra thị trường nước ngoài, phải đăng ký nhãn hiệu trước."),
         F(2, "Rất nhiều từ lóng trong bài có từ tương ứng trong tiếng Việt: 高仿 là hàng fake loại một, hàng super fake; 蹭热度 là ăn theo; 搭便车 là đi nhờ xe; 打擦边球 là lách luật. Ở Việt Nam cũng không thiếu những cái tên quán nhái thương hiệu lớn cho vui đấy."),
         F(3, "Câu hỏi cho các bạn: 你会买山寨货吗？为什么？ Bạn có mua hàng nhái không? Vì sao? Và: 小店起名傍大牌，你觉得可以接受吗？ Cửa hàng nhỏ đặt tên bám thương hiệu lớn, bạn thấy có chấp nhận được không? Hãy thử trả lời bằng tiếng Trung, dùng 明摆着, 就而言, 说到底 nhé.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 8.1", size=33,
    items=["Từ vựng trọng tâm: 对簿 · 跨界 · 调侃 · 酷似 · 概率 · 碰瓷 · 营销 · 忠实 · 傍 · 侵权 · 判定 · 蹭 · 经受 · 混淆 · 败诉 · 山寨 · 定性 · 驰名 · 理应 · 恶意 · 抢注 · 营商",
           "Mẫu câu: 酷似 · 直呼 · 任……也 · 揣着明白装糊涂 · 令……不解 · 乍听起来 · 明摆着 · 就……而言 · 近乎 · 说到底 · 将……落到实处",
           "Thành ngữ: 亦庄亦谐 · 微乎其微 · 声名在外 · 明目张胆 · 措手不及 · 抱大腿 · 抖机灵 · 脑洞大开 · 蹭IP · 井水不犯河水 · 打擦边球 · 搭便车",
           "## Bài tập về nhà",
           "Viết đoạn văn khoảng 300 chữ: 你怎么看“傍大牌”现象？ – dùng ít nhất 3 mẫu câu và 3 thành ngữ của bài"],
    say=["Chúng ta cùng tổng kết bài tám chấm một.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 对簿，跨界，调侃，酷似，概率，碰瓷，营销，忠实，傍，侵权，判定，蹭，经受，混淆，败诉，山寨，定性，驰名，理应，恶意，抢注，营商. Nhớ cách đọc 调侃, 概率, 营销 và từ dễ nhầm 忠实 nhé."),
         F(1, "Về mẫu câu: 酷似 là giống hệt; 直呼 là thốt lên; 任也 là dù… cũng…; 揣着明白装糊涂 là biết rõ mà vờ không biết; 令不解 là khiến không hiểu nổi; 乍听起来 là thoạt nghe; 明摆着 là rõ rành rành; 就而言 là xét về; 近乎 là gần như; 说到底 là suy cho cùng; và 将落到实处 là thực hiện đến nơi đến chốn."),
         F(2, "Về thành ngữ và quán dụng ngữ: 亦庄亦谐，微乎其微，声名在外，明目张胆，措手不及，抱大腿，抖机灵，脑洞大开，蹭IP，井水不犯河水，打擦边球，搭便车. Nhiều từ lóng mạng trong số này người Trung Quốc dùng hằng ngày."),
         F(4, "Bài tập về nhà: hãy viết một đoạn văn khoảng ba trăm chữ với đề 你怎么看傍大牌现象？ Bạn nhìn nhận thế nào về hiện tượng bám thương hiệu lớn? Hãy dùng ít nhất ba mẫu câu và ba thành ngữ của bài, như 酷似，明摆着，说到底，明目张胆，搭便车."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Bài sau, bài tám chấm hai, là 高通：打官司打出的江山, Qualcomm: giang sơn dựng nên từ kiện tụng. Từ nhãn hiệu, chúng ta chuyển sang bằng sáng chế: gã khổng lồ chip Qualcomm thu phí bản quyền khắp thế giới, đấu khẩu với Apple, và từng bị Trung Quốc phạt hơn sáu tỷ tệ vì độc quyền. Bài sau có tới hai mươi mốt thành ngữ, các bạn chuẩn bị tinh thần nhé. Hẹn gặp lại các bạn. Chúc các bạn học tốt!"])

lesson = {
    "title": "顶石中文 – Bài 8.1: “大头条”对簿“小油条” (“Đại Đầu Điều” ra tòa với “Tiểu Du Điều”)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"调侃": "条侃",              # tiáokǎn
                    "调皮": "条皮",              # tiáopí
                    "概率": "概律",              # gàilǜ
                    "效率": "效律",              # xiàolǜ
                    "利润率": "利润律",          # lìrùnlǜ
                    "着实": "酌实",              # zhuóshí
                    "揣着": "搋着",              # chuāizhe
                    "理应": "理英",              # lǐyīng
                    "实处": "实触",              # shíchù
                    "行业": "航业",              # hángyè
                    "各行各业": "各航各业",      # gè háng gè yè
                    "泪两行": "泪两航",          # lèi liǎng háng
                    "为今日油条": "位今日油条",  # wèi
                    "为老百姓": "位老百姓",      # wèi
                    "称他为": "称他维",          # chēng tā wéi
                    "命名为": "命名维",          # mìngmíng wéi
                    "判定为": "判定维",          # pàndìng wéi
                    "定性为": "定性维",          # dìngxìng wéi
                    "之冠": "之官",              # Dōngfāng zhī guān
                    "中伤": "众伤",              # zhòngshāng
                    "角色": "决色",              # juésè
                    "处罚": "楚罚",              # chǔfá
                    "宁可": "佞可",              # nìngkě
                    "三舍": "三设",              # tuì bì sān shè
                    "参了军": "餐了军",          # cān le jūn
                    "重金": "众金",              # zhòngjīn
                    "鬼才": "鬼财"},             # guǐ cái
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds81.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
