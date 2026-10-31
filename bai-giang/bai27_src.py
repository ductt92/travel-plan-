#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Hạ) – Bài 27 «完璧归赵». Chạy để sinh bai27.json."""
import json
import os

TAG = "HSK 6 (Hạ) · Bài 27 · 完璧归赵"
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
    zh="完璧归赵", py="Wán bì guī Zhào", vi="Bài 27: Hoàn bích quy Triệu",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Hạ.",
         "Hôm nay chúng ta học bài hai mươi bảy: 完璧归赵。 Hán Việt là Hoàn bích quy Triệu, nghĩa là: viên ngọc bích được đem về nước Triệu một cách nguyên vẹn.",
         "Đây là một bài trong Đơn vị bảy, chủ đề 经典阅读, tức là Đọc tác phẩm kinh điển. Bài khóa kể câu chuyện nổi tiếng trong sách Sử Ký: Lạn Tương Như mang ngọc Hòa Thị Bích sang nước Tần, và bằng trí tuệ cùng lòng dũng cảm, ông đã đem viên ngọc trở về nước Triệu nguyên vẹn."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bối cảnh thời Chiến Quốc và câu chuyện 完璧归赵",
           "Nắm vững 50 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: cấu trúc 左……右…… và trợ từ 不成",
           "Phân biệt hai từ 一贯 và 一直",
           "Kỹ năng viết: phép trích dẫn (引用)"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu bối cảnh lịch sử thời Chiến Quốc, và nắm được nội dung câu chuyện Hoàn bích quy Triệu."),
         F(1, "Thứ hai, nắm vững năm mươi từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học hai điểm ngữ pháp: cấu trúc 左……右……， và trợ từ cuối câu 不成."),
         F(3, "Thứ tư, phân biệt hai từ rất dễ nhầm: 一贯 và 一直."),
         F(4, "Thứ năm, một kỹ năng viết rất hữu ích: phép trích dẫn, tiếng Trung gọi là 引用."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Câu hỏi khởi động: nhà ngoại giao bạn yêu thích", size=38,
    items=["每个国家都有一些著名的外交家，请描述一下你心目中最喜爱的一位外交家。",
           "Mỗi nước đều có những nhà ngoại giao nổi tiếng. Hãy miêu tả nhà ngoại giao mà bạn yêu thích nhất.",
           "1. 机智 cơ trí, nhanh trí · 2. 勇敢 dũng cảm · 3. 坚定 kiên định",
           "4. 幽默 hài hước · 5. 灵活 linh hoạt · 6. 有感染力 có sức lôi cuốn",
           "Gợi ý: Mạc Đĩnh Chi đi sứ nhà Nguyên · 周恩来 Chu Ân Lai"],
    say=["Chúng ta bắt đầu bằng phần khởi động. Sách cho xem bức ảnh hai bàn tay bắt nhau, biểu tượng của ngoại giao.",
         F(0, "每个国家都有一些著名的外交家，请描述一下你心目中最喜爱的一位外交家。"),
         F(1, "Nghĩa là: mỗi nước đều có những nhà ngoại giao nổi tiếng, hãy miêu tả nhà ngoại giao mà bạn yêu thích nhất. Có thể dùng lời của mình, hoặc dùng các từ sau."),
         F(2, "机智， là cơ trí, nhanh trí. 勇敢， là dũng cảm. 坚定， là kiên định, vững vàng."),
         F(3, "幽默， là hài hước. 灵活， là linh hoạt. Và 有感染力， là có sức lôi cuốn, có sức truyền cảm với người khác."),
         F(4, "Ví dụ, người Việt chúng ta có Mạc Đĩnh Chi, đi sứ nhà Nguyên, nổi tiếng nhờ tài ứng đối nhanh trí. Trung Quốc có 周恩来， Chu Ân Lai, nhà ngoại giao rất linh hoạt và có sức lôi cuốn. Lạn Tương Như trong bài hôm nay chính là một nhà ngoại giao vừa cơ trí vừa dũng cảm."),
         "Các bạn hãy tạm dừng video, thử dùng vài từ trên để nói về một nhà ngoại giao bằng tiếng Trung, rồi mới xem tiếp nhé."])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 商 và 过", size=38,
    items=["## 商 (thương): bàn bạc, trao đổi ý kiến",
           "商议 thương nghị · 商量 thương lượng · 商讨 thương thảo · 商谈 thương đàm",
           "商定 bàn rồi quyết định · 商洽 tiếp xúc bàn bạc · 磋商 thương lượng · 协商 hiệp thương",
           "## 过 (quá): lỗi lầm",
           "过错 lỗi lầm · 过失 sơ suất · 改过 sửa lỗi · 悔过 hối lỗi",
           "记过 ghi lỗi kỷ luật · 罪过 tội lỗi · 功过 công và tội · 将功补过 lấy công chuộc tội"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo, rất có lợi cho người Việt nhờ âm Hán Việt.",
         F(0, "Nhóm thứ nhất có chữ 商, Hán Việt là thương. Ngoài nghĩa buôn bán, chữ này còn có nghĩa là bàn bạc, trao đổi ý kiến, như trong từ thương lượng."),
         F(1, "商议，商量，商讨，商谈。 Tức là: bàn bạc, thương lượng, thương thảo, và hội đàm. Bài khóa có câu 召集大臣商议对策, triệu tập đại thần bàn đối sách."),
         F(2, "商定，商洽，磋商，协商。 Tức là: bàn bạc rồi quyết định, tiếp xúc bàn bạc, thương lượng, và hiệp thương. Từ 磋商 là từ mới của bài hôm nay."),
         F(3, "Nhóm thứ hai có chữ 过, Hán Việt là quá. Ngoài nghĩa đi qua, vượt qua, chữ này còn có nghĩa là lỗi lầm."),
         F(4, "过错，过失，改过，悔过。 Tức là: lỗi lầm, sơ suất, sửa lỗi, và hối lỗi. Lạn Tương Như nói 过错在赵, lỗi ở nước Triệu."),
         F(5, "记过，罪过，功过，将功补过。 Tức là: ghi lỗi kỷ luật, tội lỗi, công và tội, và 将功补过, lấy công chuộc tội.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 诚 và 众", size=38,
    items=["## 诚 (thành): thật lòng",
           "诚实 thành thật · 诚心 thành tâm · 诚信 thành tín · 诚恳 thành khẩn · 真诚 chân thành",
           "热诚 nhiệt thành · 忠诚 trung thành · 至诚 chí thành · 精诚合作 hợp tác hết lòng · 真心诚意 thật lòng thật dạ",
           "## 众 (chúng): nhiều người",
           "众臣 các quan · 众人 mọi người · 大众 đại chúng · 公众 công chúng · 观众 khán giả",
           "听众 thính giả · 群众 quần chúng · 民众 dân chúng · 万众一心 muôn người một lòng",
           "众望所归 được mọi người tín nhiệm · 兴师动众 huy động nhiều người"],
    say=[F(0, "Nhóm thứ ba có chữ 诚, Hán Việt là thành, nghĩa là thật lòng, thành thật."),
         F(1, "诚实，诚心，诚信，诚恳，真诚。 Tức là: thành thật, thành tâm, thành tín, thành khẩn, chân thành. Bài khóa có từ 诚意, thành ý: vua Tần không có thành ý đổi thành."),
         F(2, "热诚，忠诚，至诚，精诚合作，真心诚意。 Tức là: nhiệt thành, trung thành, chí thành, hợp tác hết lòng, và thật lòng thật dạ."),
         F(3, "Nhóm cuối cùng có chữ 众, Hán Việt là chúng, nghĩa là nhiều người."),
         F(4, "众臣，众人，大众，公众，观众。 Tức là: các quan, mọi người, đại chúng, công chúng, khán giả. Bài khóa có câu 秦王率领众臣, vua Tần dẫn các quan."),
         F(5, "听众，群众，民众，万众一心。 Tức là: thính giả, quần chúng, dân chúng, và muôn người một lòng."),
         F(6, "众望所归， nghĩa là được mọi người tín nhiệm, kỳ vọng. 兴师动众， nghĩa là huy động nhiều người, làm rùm beng."),
         "Các bạn thấy không, chỉ cần nắm nghĩa của một chữ gốc, ta có thể đoán được nghĩa của cả một nhóm từ. Hãy áp dụng cách này khi học từ mới nhé."])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng)
V = [
    ("玉", "yù", "ngọc", "danh từ", "ngọc", "秦以十五座城换一块玉。", "Nước Tần lấy mười lăm tòa thành đổi một khối ngọc.",
     "Danh từ, nghĩa là ngọc. 宝玉 là ngọc quý, 玉器 là đồ làm bằng ngọc. Lượng từ thường dùng là 块."),
    ("答复", "dáfù", "đáp phục", "động từ", "trả lời, hồi đáp (chính thức)", "不知如何答复秦王。", "Không biết trả lời vua Tần thế nào.",
     "Động từ, nghĩa là trả lời, hồi đáp, thường là trả lời chính thức cho một yêu cầu. Cũng dùng làm danh từ: 给个答复, cho một câu trả lời."),
    ("得罪", "dézuì", "đắc tội", "động từ", "làm mất lòng, đắc tội", "又怕得罪秦国。", "Lại sợ đắc tội với nước Tần.",
     "Động từ, nghĩa là làm mất lòng, làm phật ý người khác, giống từ đắc tội trong tiếng Việt."),
    ("大臣", "dàchén", "đại thần", "danh từ", "đại thần, quan lớn (thời quân chủ)", "召集大臣商议对策", "triệu tập các đại thần bàn bạc đối sách",
     "Danh từ, nghĩa là đại thần, quan lớn trong triều đình thời phong kiến."),
    ("对策", "duìcè", "đối sách", "danh từ", "đối sách, biện pháp đối phó", "我们得赶快想出对策。", "Chúng ta phải mau nghĩ ra cách đối phó.",
     "Danh từ, nghĩa là đối sách, biện pháp để đối phó với một tình huống."),
    ("提议", "tíyì", "đề nghị", "động từ", "đề nghị, đề xuất", "有人提议，听听蔺相如怎么说。", "Có người đề nghị nghe thử Lạn Tương Như nói thế nào.",
     "Động từ, nghĩa là đề nghị, đưa ra ý kiến cho mọi người bàn. Cũng có thể làm danh từ: 这个提议很好, đề nghị này rất hay."),
    ("请教", "qǐngjiào", "thỉnh giáo", "động từ", "xin chỉ giáo, hỏi ý kiến", "赵王亲自向他请教。", "Vua Triệu đích thân hỏi ý kiến ông.",
     "Động từ, nghĩa là xin chỉ bảo, hỏi ý kiến một cách khiêm tốn. Mẫu thường gặp: 向某人请教, hỏi ý kiến ai đó."),
    ("实力", "shílì", "thực lực", "danh từ", "thực lực, sức mạnh thực tế", "凭实力，我们不答应不行。", "Xét về thực lực, chúng ta không đồng ý không được.",
     "Danh từ, nghĩa là thực lực, sức mạnh thật sự về kinh tế, quân sự hay năng lực."),
    ("慷慨", "kāngkǎi", "khảng khái", "tính từ", "hào phóng, rộng rãi", "他对朋友很慷慨。", "Anh ấy rất hào phóng với bạn bè.",
     "Tính từ, nghĩa là hào phóng, rộng rãi, không tiếc tiền của. Cẩn thận: khảng khái trong tiếng Việt thường là thẳng thắn, cương trực; còn 慷慨 trong bài là hào phóng."),
    ("亏待", "kuīdài", "khuy đãi", "động từ", "bạc đãi, đối xử tệ", "并未亏待赵国", "hoàn toàn không bạc đãi nước Triệu",
     "Động từ, nghĩa là đối xử không công bằng, bạc đãi người khác. Thường dùng ở dạng phủ định: 不会亏待你, sẽ không bạc đãi anh đâu."),
    ("动身", "dòng shēn", "động thân", "động từ", "lên đường, khởi hành", "请先生即刻动身。", "Xin tiên sinh lập tức lên đường.",
     "Động từ ly hợp, nghĩa là lên đường, bắt đầu một chuyến đi xa."),
    ("磋商", "cuōshāng", "tha thương", "động từ", "bàn bạc, thương lượng", "两国正在进行磋商。", "Hai nước đang tiến hành thương lượng.",
     "Động từ, nghĩa là bàn bạc kỹ, thương lượng, thường dùng trong ngoại giao, kinh doanh."),
    ("荣幸", "róngxìng", "vinh hạnh", "tính từ", "vinh hạnh, vinh dự", "大王派我去，是我的荣幸。", "Đại vương cử thần đi là vinh hạnh của thần.",
     "Tính từ, nghĩa là vinh hạnh. Câu lịch sự rất hay gặp: 很荣幸认识您, rất vinh hạnh được quen biết ngài."),
    ("转达", "zhuǎndá", "chuyển đạt", "động từ", "chuyển lời, chuyển đạt", "转达了赵王的问候", "chuyển lời hỏi thăm của vua Triệu",
     "Động từ, nghĩa là chuyển lời của người này đến người khác."),
    ("爱不释手", "àibúshìshǒu", "ái bất thích thủ", "thành ngữ", "thích đến mức cầm mãi không rời tay", "秦王左看右看，爱不释手。", "Vua Tần ngắm tới ngắm lui, cầm mãi không nỡ rời tay.",
     "Thành ngữ. Chữ 释 ở đây là buông ra, nên nghĩa là thích đến mức cầm mãi không muốn buông tay."),
    ("圈套", "quāntào", "khuyên sáo", "danh từ", "cái bẫy, mưu lừa", "心想果然是个圈套。", "Trong lòng nghĩ quả nhiên là một cái bẫy.",
     "Danh từ, nghĩa là cái bẫy, mưu kế để lừa người khác. 设圈套 là giăng bẫy."),
    ("归还", "guīhuán", "quy hoàn", "động từ", "trả lại, hoàn trả", "请大王把璧归还于我。", "Xin đại vương trả ngọc lại cho thần.",
     "Động từ, nghĩa là trả lại đồ cho chủ, trang trọng hơn 还. Chú ý: chữ 还 ở đây đọc là huán."),
    ("从容", "cóngróng", "thung dung", "tính từ", "ung dung, bình tĩnh, thong thả", "从容地站在殿中央", "ung dung đứng giữa điện",
     "Tính từ, nghĩa là ung dung, bình tĩnh, không vội vàng, giống từ thung dung trong tiếng Việt."),
    ("中央", "zhōngyāng", "trung ương", "danh từ", "chính giữa; trung ương", "广场中央有一座雕像。", "Giữa quảng trường có một bức tượng.",
     "Danh từ, nghĩa là chính giữa. Ngoài ra còn có nghĩa là cơ quan trung ương."),
    ("兑现", "duìxiàn", "đoái hiện", "động từ", "thực hiện (lời hứa); đổi ra tiền mặt", "没有兑现的诚意", "không có thành ý thực hiện lời hứa",
     "Động từ, nghĩa là thực hiện lời hứa, biến lời hứa thành hiện thực. Nghĩa gốc là đổi chi phiếu ra tiền mặt."),
    ("妄想", "wàngxiǎng", "vọng tưởng", "danh từ", "vọng tưởng, mơ tưởng hão huyền", "想不交城拿走璧，那是妄想。", "Muốn lấy ngọc mà không giao thành, đó là vọng tưởng.",
     "Danh từ, nghĩa là vọng tưởng, ý nghĩ viển vông không thể thực hiện được."),
    ("发誓", "fā shì", "phát thệ", "động từ", "thề, thề thốt", "他发誓再也不喝酒了。", "Anh ấy thề sẽ không bao giờ uống rượu nữa.",
     "Động từ ly hợp, nghĩa là thề. Có thể tách ra: 发了誓, đã thề."),
    ("尸体", "shītǐ", "thi thể", "danh từ", "thi thể, xác chết", "秦王看到的将是他的尸体。", "Thứ vua Tần nhìn thấy sẽ là thi thể của ông.",
     "Danh từ, nghĩa là thi thể, xác người hoặc xác động vật."),
    ("撒谎", "sā huǎng", "tát hoang", "động từ", "nói dối", "我怎么会撒谎呢？", "Ta sao lại nói dối được chứ?",
     "Động từ ly hợp, nghĩa là nói dối, giống 说谎. Có thể tách ra: 撒了个谎, nói một lời dối."),
    ("隆重", "lóngzhòng", "long trọng", "tính từ", "long trọng, trọng thể", "举行了隆重的仪式", "đã cử hành một nghi lễ long trọng",
     "Tính từ, nghĩa là long trọng, trọng thể, âm Hán Việt giống hệt tiếng Việt."),
    ("仪式", "yíshì", "nghi thức", "danh từ", "nghi lễ, nghi thức, buổi lễ", "开幕仪式", "lễ khai mạc",
     "Danh từ, nghĩa là nghi lễ, buổi lễ. Động từ đi kèm thường là 举行, cử hành."),
    ("沐浴", "mùyù", "mộc dục", "động từ", "tắm gội", "沐浴更衣", "tắm gội, thay áo",
     "Động từ, nghĩa là tắm gội, sắc thái trang trọng. Người xưa tắm gội thay áo trước những nghi lễ quan trọng."),
    ("荤", "hūn", "huân", "danh từ", "đồ mặn (thịt, cá)", "戒掉荤腥，只吃素食", "kiêng đồ mặn đồ tanh, chỉ ăn chay",
     "Danh từ, nghĩa là đồ mặn như thịt, cá. Ngược lại là 素, đồ chay. 荤腥 là đồ mặn và đồ tanh."),
    ("庄严", "zhuāngyán", "trang nghiêm", "tính từ", "trang nghiêm, nghiêm trang", "以示庄严", "để tỏ sự trang nghiêm",
     "Tính từ, nghĩa là trang nghiêm, nghiêm trang và đáng kính."),
    ("无理取闹", "wúlǐ-qǔnào", "vô lý thủ náo", "thành ngữ", "vô cớ gây sự, làm ầm lên vô lý", "我并非无理取闹。", "Thần không phải vô cớ gây chuyện.",
     "Thành ngữ. 无理 là không có lý, 取闹 là gây ồn ào, nghĩa là cố ý gây chuyện mà không có lý do chính đáng."),
    ("冒犯", "màofàn", "mạo phạm", "động từ", "mạo phạm, xúc phạm", "也不是冒犯大王", "cũng không phải mạo phạm đại vương",
     "Động từ, nghĩa là mạo phạm, có lời nói hay hành động vô lễ với người khác."),
    ("亦", "yì", "diệc", "phó từ", "cũng (văn viết)", "亦请举行同样的仪式", "cũng xin cử hành nghi lễ như vậy",
     "Phó từ, nghĩa là cũng, giống 也 nhưng dùng trong văn viết, văn cổ."),
    ("边境", "biānjìng", "biên cảnh", "danh từ", "biên giới, vùng biên", "偷偷越过边境", "lén vượt qua biên giới",
     "Danh từ, nghĩa là vùng biên giới giữa hai nước."),
    ("泄露", "xièlòu", "tiết lộ", "động từ", "tiết lộ, để lộ (bí mật)", "不可泄露秘密。", "Không được tiết lộ bí mật.",
     "Động từ, nghĩa là để lộ ra điều cần giữ kín. Chú ý: chữ 露 ở đây đọc là lòu."),
    ("率领", "shuàilǐng", "suất lĩnh", "động từ", "dẫn đầu, thống lĩnh", "秦王率领众臣", "vua Tần dẫn các quan",
     "Động từ, nghĩa là dẫn đầu, chỉ huy một nhóm người. Chú ý: chữ 率 ở đây đọc là shuài."),
    ("镇静", "zhènjìng", "trấn tĩnh", "tính từ", "bình tĩnh, điềm tĩnh", "镇静地对秦王说", "điềm tĩnh nói với vua Tần",
     "Tính từ, nghĩa là bình tĩnh, điềm tĩnh, không hoảng hốt."),
    ("雄厚", "xiónghòu", "hùng hậu", "tính từ", "hùng hậu, dồi dào", "秦国仗着国力雄厚。", "Nước Tần cậy quốc lực hùng hậu.",
     "Tính từ, nghĩa là hùng hậu, dồi dào, thường nói về sức mạnh, tiền vốn, lực lượng."),
    ("一贯", "yíguàn", "nhất quán", "tính từ", "trước sau như một, xưa nay vẫn thế", "一贯霸道", "xưa nay vẫn ngang ngược",
     "Tính từ, nghĩa là xưa nay vẫn vậy, trước sau như một. Lát nữa ta sẽ phân biệt kỹ với 一直."),
    ("霸道", "bàdào", "bá đạo", "tính từ", "ngang ngược, hống hách", "他这个人太霸道了。", "Người này ngang ngược quá.",
     "Tính từ, nghĩa là ngang ngược, hống hách, ỷ mạnh hiếp yếu. Cẩn thận: bá đạo trong tiếng lóng Việt Nam có khi là giỏi, ngầu; còn 霸道 luôn mang nghĩa xấu."),
    ("声誉", "shēngyù", "thanh dự", "danh từ", "danh tiếng, uy tín", "声誉不好", "danh tiếng không tốt",
     "Danh từ, nghĩa là danh tiếng, tiếng tăm, uy tín."),
    ("列举", "lièjǔ", "liệt cử", "động từ", "liệt kê, kể ra", "事情我就不一一列举了。", "Những chuyện ấy tôi không kể ra từng việc nữa.",
     "Động từ, nghĩa là liệt kê, kể ra từng cái. Hay đi với 一一: 一一列举, kể ra từng cái một."),
    ("履行", "lǚxíng", "lý hành", "động từ", "thực hiện (lời hứa, nghĩa vụ)", "我怕大王不履行承诺。", "Thần sợ đại vương không thực hiện lời hứa.",
     "Động từ, nghĩa là thực hiện lời hứa, nghĩa vụ, hợp đồng. Cụm cố định: 履行承诺, 履行义务, 履行合同."),
    ("歪曲", "wāiqū", "oai khúc", "động từ", "xuyên tạc, bóp méo", "你这不是歪曲我的意思吗？", "Ngươi đây chẳng phải là xuyên tạc ý ta sao?",
     "Động từ, nghĩa là xuyên tạc, cố ý làm sai lệch sự thật hay ý của người khác. 歪 là méo, lệch; 曲 là cong."),
    ("理直气壮", "lǐzhí-qìzhuàng", "lý trực khí tráng", "thành ngữ", "lý lẽ vững vàng, khí thế mạnh mẽ", "蔺相如理直气壮地说。", "Lạn Tương Như hùng hồn nói.",
     "Thành ngữ. 理直 là lý lẽ ngay thẳng, 气壮 là khí thế mạnh, nghĩa là có lý nên nói năng mạnh mẽ, tự tin."),
    ("压迫", "yāpò", "áp bách", "động từ", "áp bức, chèn ép", "弱国不可能压迫强国。", "Nước yếu không thể chèn ép nước mạnh.",
     "Động từ, nghĩa là áp bức, dùng quyền lực hay sức mạnh để chèn ép người khác."),
    ("口头", "kǒutóu", "khẩu đầu", "tính từ", "bằng miệng, bằng lời nói", "口头承诺", "lời hứa miệng",
     "Tính từ, nghĩa là bằng miệng, bằng lời nói. Ngược lại là 书面, bằng văn bản. Bài khóa có câu 不要光口头说, đừng chỉ nói miệng."),
    ("副", "fù", "phó", "lượng từ", "vẻ, bộ (dùng cho nét mặt, dáng vẻ)", "装出一副高姿态", "làm ra vẻ cao thượng",
     "Lượng từ, dùng cho nét mặt, dáng vẻ, thường đi với số một: 一副笑脸, một khuôn mặt tươi cười. Ngoài ra còn dùng cho đồ vật thành bộ, như 一副眼镜, một cặp kính."),
    ("姿态", "zītài", "tư thái", "danh từ", "dáng vẻ, tư thế; thái độ", "他的姿态很优美。", "Dáng vẻ của anh ấy rất đẹp.",
     "Danh từ, nghĩa là tư thế, dáng vẻ; cũng có nghĩa là thái độ. 高姿态 là thái độ cao thượng, độ lượng."),
    ("隔阂", "géhé", "cách ngại", "danh từ", "sự ngăn cách, hiềm khích", "闹出隔阂", "sinh ra hiềm khích",
     "Danh từ, nghĩa là sự ngăn cách về tình cảm, hiểu lầm, hiềm khích giữa hai bên."),
    ("争端", "zhēngduān", "tranh đoan", "danh từ", "tranh chấp, xung đột", "再起争端", "lại nổi lên tranh chấp",
     "Danh từ, nghĩa là mối tranh chấp, xung đột, ví dụ 国际争端, tranh chấp quốc tế."),
]

add("bullets", chapter="Từ mới (50 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 27 có 50 từ mới, chia thành 17 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc đặc biệt: 归还 (huán), 泄露 (lòu), 率领 (shuài)"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có năm mươi từ, thầy chia thành mười bảy nhóm nhỏ, mỗi nhóm ba từ, nhóm cuối có hai từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ, phần lớn lấy ngay từ bài khóa."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số từ có âm đọc đặc biệt, thầy sẽ nhắc khi gặp. Chúng ta bắt đầu nhé.")])

for g in range(0, len(V), 3):
    group = V[g:g + 3]
    words, say = [], []
    for i, (zh, py, hv, loai, vi, ex, exvi, expl) in enumerate(group):
        n = g + i + 1
        words.append({"zh": zh, "py": py, "hv": hv.upper(), "loai": f"{n}. {loai}", "vi": vi, "ex": ex, "exvi": exvi})
        say.append(F(i, f"Từ số {n}: {zh}。 {zh}。 Hán Việt là {hv}.", zr=120))
        say.append(F(i, f"{expl} Ví dụ: {ex}{'' if ex[-1] in '。…！？' else '，'} {exvi[0].upper() + exvi[1:]}{'' if exvi[-1] in '.!?' else '.'}", zr=130))
    add("vocab", section="Từ mới 生词", title=f"Từ mới ({g + 1}–{g + len(group)} / {len(V)})",
        words=words, say=say)

# ======================= BỐI CẢNH =======================
add("bullets", chapter="Bối cảnh Chiến Quốc", section="Bài khóa 课文", title="Bối cảnh: thời Chiến Quốc", size=38,
    items=["战国 Chiến Quốc (475–221 TCN): bảy nước lớn tranh hùng – 战国七雄",
           "秦 Tần · 楚 Sở · 齐 Tề · 燕 Yên · 韩 Hàn · 赵 Triệu · 魏 Ngụy",
           "秦国 nước Tần ở phía tây: mạnh nhất, năm 221 TCN thống nhất Trung Quốc",
           "赵国 nước Triệu ở phía bắc: cũng là nước lớn, nhưng thực lực kém Tần",
           "Sự việc 完璧归赵 xảy ra năm 283 TCN (theo chú thích của sách)"],
    say=["Trước khi đọc bài khóa, thầy kể một chút về bối cảnh lịch sử, để các bạn hiểu câu chuyện dễ hơn.",
         F(0, "战国， tức thời Chiến Quốc, kéo dài từ khoảng năm bốn trăm bảy mươi lăm đến năm hai trăm hai mươi mốt trước Công nguyên. Thời kỳ này có bảy nước lớn liên tục đánh nhau để tranh giành thiên hạ, gọi là 战国七雄, Chiến Quốc thất hùng."),
         F(1, "Bảy nước đó là: 秦，楚，齐，燕，韩，赵，魏。 Tức là Tần, Sở, Tề, Yên, Hàn, Triệu, Ngụy."),
         F(2, "Trong đó, 秦国， nước Tần ở phía tây, ngày càng mạnh nhất. Cuối cùng, năm hai trăm hai mươi mốt trước Công nguyên, Tần Thủy Hoàng đã thống nhất Trung Quốc."),
         F(3, "Còn 赵国， nước Triệu ở phía bắc, cũng là một nước lớn, nhưng thực lực kém nước Tần. Vì vậy, khi nước Tần đưa ra yêu cầu, vua Triệu rất khó xử."),
         F(4, "Theo chú thích ở cuối trang bài khóa, câu chuyện Hoàn bích quy Triệu xảy ra vào năm hai trăm tám mươi ba trước Công nguyên, tức là cuối thời Chiến Quốc.")])

add("bullets", section="Bài khóa 课文", title="Ngọc Hòa Thị Bích 和氏璧", size=38,
    items=["璧 bích: một loại ngọc dẹt, hình tròn, ở giữa có lỗ",
           "卞和 Biện Hòa người nước Sở tìm được một khối ngọc thô, đem dâng vua",
           "Thợ ngọc nói chỉ là đá → Biện Hòa bị chặt chân, hai đời vua liền",
           "Vua Sở sau cho mài giũa: quả nhiên là ngọc quý → đặt tên 和氏璧",
           "Về sau ngọc thuộc về nước Triệu · thành ngữ 价值连城 giá trị liên thành"],
    say=["Tiếp theo, chúng ta tìm hiểu về nhân vật thứ hai của câu chuyện, đó là chính viên ngọc: 和氏璧， ngọc Hòa Thị Bích.",
         F(0, "Trước hết, chữ 璧 là gì? Theo chú thích của sách, 璧 là một loại đồ ngọc, dẹt, hình tròn, ở giữa có một cái lỗ. Người xưa dùng ngọc bích trong các nghi lễ quan trọng."),
         F(1, "Tương truyền, có một người nước Sở tên là 卞和， Biện Hòa, tìm được một khối ngọc thô bọc trong đá, liền đem dâng lên vua Sở."),
         F(2, "Nhưng thợ ngọc nói đó chỉ là hòn đá. Vua cho rằng Biện Hòa lừa mình, nên sai chặt một chân của ông. Đến đời vua sau, ông lại dâng ngọc, và lại bị chặt nốt chân kia."),
         F(3, "Đến đời vua tiếp theo, Biện Hòa ôm khối đá khóc suốt ba ngày ba đêm. Vua cho người mài giũa, quả nhiên bên trong là ngọc quý tuyệt đẹp. Viên ngọc được đặt tên theo họ của ông: 和氏璧， tức ngọc của họ Hòa."),
         F(4, "Về sau, viên ngọc này thuộc về nước Triệu. Vì vua Tần muốn đổi nó bằng mười lăm tòa thành, nên tiếng Trung có thành ngữ 价值连城， giá trị liên thành, nghĩa là quý giá vô cùng.")])

add("bullets", section="Bài khóa 课文", title="Nhân vật và nguồn gốc câu chuyện", size=38,
    items=["蔺相如 Lạn Tương Như: người nước Triệu, nhờ chuyến đi sứ này mà được trọng dụng",
           "赵王 vua Triệu (Triệu Huệ Văn Vương) · 秦王 vua Tần (Tần Chiêu Tương Vương)",
           "Nguồn: 《史记》 Sử Ký của 司马迁 Tư Mã Thiên – Liêm Pha Lạn Tương Như liệt truyện",
           "Câu chuyện tiếp theo: 将相和 – Liêm Pha chịu đòn nhận tội (负荆请罪)",
           "Thành ngữ 完璧归赵: trả lại đồ vật nguyên vẹn cho chủ cũ"],
    say=["Bây giờ chúng ta làm quen với các nhân vật.",
         F(0, "Nhân vật chính là 蔺相如， Lạn Tương Như, người nước Triệu. Lúc đầu ông chỉ là môn khách trong nhà một vị quan. Nhờ chuyến đi sứ nước Tần này, ông được vua Triệu trọng dụng, về sau làm đến chức quan rất cao."),
         F(1, "Hai nhân vật còn lại là hai vị vua: 赵王， vua Triệu, tức Triệu Huệ Văn Vương; và 秦王， vua Tần, tức Tần Chiêu Tương Vương, một vị vua đầy tham vọng."),
         F(2, "Câu chuyện được ghi lại trong 史记， Sử Ký, bộ sử nổi tiếng của 司马迁， Tư Mã Thiên, trong thiên Liêm Pha Lạn Tương Như liệt truyện. Bài khóa của chúng ta được cải biên từ câu chuyện ấy, viết bằng tiếng Trung hiện đại."),
         F(3, "Sau sự kiện này còn có một câu chuyện rất nổi tiếng: 将相和， tướng và tướng quốc hòa thuận. Đại tướng Liêm Pha ghen tị vì Lạn Tương Như được làm quan cao hơn mình, nhưng Lạn Tương Như luôn nhường nhịn vì lợi ích của đất nước. Cuối cùng Liêm Pha cởi áo, cõng roi gai đến xin chịu tội, tiếng Trung là 负荆请罪."),
         F(4, "Từ câu chuyện này, tiếng Trung có thành ngữ 完璧归赵， dùng để ví việc trả lại đồ vật nguyên vẹn cho chủ cũ. Ví dụ, khi trả sách đã mượn, ta có thể nói vui: 这本书我完璧归赵了。 Cuốn sách này tôi xin trả lại nguyên vẹn.")])

# ======================= BÀI KHÓA =======================
P = [
    ("战国后期，秦国最强。秦王得知赵王得到一块叫“和氏璧”的宝玉，传话给赵王，说愿用十五座城换和氏璧。",
     "Cuối thời Chiến Quốc, nước Tần mạnh nhất. Vua Tần biết tin vua Triệu có được một viên ngọc quý tên là Hòa Thị Bích, bèn cho người nhắn với vua Triệu rằng mình muốn dùng mười lăm tòa thành để đổi lấy viên ngọc ấy.",
     ["后期 là giai đoạn cuối, ngược lại là 前期, giai đoạn đầu. 得知 là biết được, được tin, văn viết hơn 知道.",
      "座 là lượng từ của thành trì, núi, cầu: 十五座城, mười lăm tòa thành. 传话 là nhắn lời, truyền lời qua người khác."]),
    ("赵王左右为难，不知如何答复秦王：答应吧，怕上当受骗——给了和氏璧，拿不到城；不答应吧，又怕得罪秦国。于是，赶忙召集大臣商议对策。",
     "Vua Triệu tiến thoái lưỡng nan, không biết trả lời vua Tần thế nào: đồng ý thì sợ bị mắc lừa, đưa ngọc rồi mà không lấy được thành; không đồng ý thì lại sợ đắc tội với nước Tần. Thế là vua vội vàng triệu tập các đại thần bàn bạc đối sách.",
     ["左右为难 là thành ngữ, nghĩa là làm thế này cũng khó, làm thế kia cũng khó, tức tiến thoái lưỡng nan. Đây cũng chính là ví dụ về phép trích dẫn mà ta học ở cuối bài.",
      "Cấu trúc A吧，……；不A吧，…… nghĩa là: làm A thì…, không làm A thì…, diễn tả sự phân vân giữa hai lựa chọn. 上当受骗 là mắc lừa, bị lừa gạt."]),
    ("大臣们也没有好办法。有人提议，蔺相如见多识广，有勇有谋，可以听听他怎么说。赵王请来了蔺相如，并亲自向他请教。",
     "Các đại thần cũng không có cách gì hay. Có người đề nghị: Lạn Tương Như hiểu nhiều biết rộng, vừa dũng cảm vừa mưu trí, có thể nghe thử ông ấy nói thế nào. Vua Triệu mời Lạn Tương Như đến, và đích thân hỏi ý kiến ông.",
     ["见多识广 là thành ngữ: thấy nhiều biết rộng. 有勇有谋 là vừa có dũng vừa có mưu. Cấu trúc 有A有B rất hay gặp, ví dụ 有说有笑, vừa nói vừa cười.",
      "亲自 là đích thân. Một vị vua đích thân hỏi ý kiến một người chưa có chức vị gì, cho thấy tình thế lúc đó rất gấp."]),
    ("蔺相如说：“秦强赵弱，凭实力，我们不答应不行；秦以十五座城换一块玉，也算慷慨，并未亏待赵国，若不答应，过错在赵；若将和氏璧送去，秦不交出城来，那么错就在秦了，因此我们只有送和氏璧。”",
     "Lạn Tương Như nói: Tần mạnh Triệu yếu, xét về thực lực, chúng ta không đồng ý thì không được. Tần lấy mười lăm tòa thành đổi một khối ngọc, cũng coi là hào phóng, hoàn toàn không bạc đãi nước Triệu; nếu không đồng ý thì lỗi ở Triệu. Còn nếu đem ngọc sang mà Tần không giao thành, thì lỗi lại ở Tần. Vì vậy chúng ta chỉ có cách đem ngọc sang.",
     ["凭 là dựa vào. 以 cộng danh từ là lấy, dùng: 秦以十五座城换一块玉. 并未 là hoàn toàn không, văn viết, nhấn mạnh hơn 没有. 若 là nếu, văn viết.",
      "Lập luận của Lạn Tương Như rất chặt chẽ: không đồng ý thì Triệu mang lỗi; đưa ngọc sang tức là đẩy cái lỗi về phía nước Tần, nếu Tần lừa thì Tần sai."]),
    ("赵王说：“那就请先生即刻动身前去磋商。”蔺相如说：“大王派我去，是我的荣幸。此去秦国，秦若是交了城，我便把璧留下；不交城，我一定完璧归赵。”",
     "Vua Triệu nói: Vậy xin tiên sinh lập tức lên đường sang đó thương lượng. Lạn Tương Như nói: Đại vương cử thần đi là vinh hạnh của thần. Chuyến này sang Tần, nếu Tần giao thành, thần sẽ để ngọc lại; nếu không giao thành, thần nhất định đem ngọc nguyên vẹn trở về nước Triệu.",
     ["先生 ở đây là cách gọi tôn kính: tiên sinh. 即刻 là lập tức. 此去 là chuyến đi này. 便 bằng 就, văn viết.",
      "完璧归赵: 完 là trọn vẹn, 璧 là ngọc bích, 归 là trở về, 赵 là nước Triệu. Đây chính là câu nói làm nên tên bài và thành ngữ nổi tiếng."]),
    ("蔺相如带着和氏璧到了秦国，转达了赵王的问候，把玉献给了秦王。秦王对着和氏璧左看右看，爱不释手。",
     "Lạn Tương Như mang ngọc Hòa Thị Bích đến nước Tần, chuyển lời hỏi thăm của vua Triệu, rồi dâng ngọc lên vua Tần. Vua Tần cầm ngọc ngắm tới ngắm lui, thích đến mức không nỡ rời tay.",
     ["献 là dâng, hiến: 献给, dâng lên. 左看右看 là ngắm tới ngắm lui, đây là điểm ngữ pháp thứ nhất: cấu trúc 左……右…….",
      "爱不释手 là thích đến mức không buông tay. Vua Tần rất thích ngọc, nhưng lại không hề nhắc đến chuyện giao thành."]),
    ("蔺相如等了半天不见秦王提换城之事，心想果然是个圈套，可璧在秦王手里，怎么把璧拿回来呢？",
     "Lạn Tương Như đợi rất lâu mà không thấy vua Tần nhắc đến chuyện đổi thành, trong lòng nghĩ quả nhiên là một cái bẫy; nhưng ngọc đang trong tay vua Tần, làm sao lấy lại được đây?",
     ["等了半天 là đợi rất lâu; 半天 ở đây không phải nửa ngày, mà là rất lâu. 之事 là việc…, văn viết: 换城之事, việc đổi thành.",
      "果然 là quả nhiên, đúng như đã đoán. Lạn Tương Như đã lường trước nước Tần có thể lừa mình."]),
    ("左思右想之后，他对秦王说：“这璧有点儿小毛病，请大王把璧归还于我，我指给大王看。”秦王把璧递给蔺相如。",
     "Suy đi tính lại, ông nói với vua Tần: Viên ngọc này có một chút tì vết nhỏ, xin đại vương trả ngọc cho thần, thần chỉ cho đại vương xem. Vua Tần đưa ngọc cho Lạn Tương Như.",
     ["左思右想 là suy đi tính lại, lại là cấu trúc 左……右……. 毛病 ở đây là khuyết điểm, tì vết.",
      "归还于我: 于 là giới từ văn viết, nghĩa là cho, với. Đây là một mẹo thông minh: lấy cớ chỉ tì vết để lấy lại ngọc."]),
    ("蔺相如从容地站在殿中央，手抱和氏璧说：“大王派人到赵国，说用十五座城换赵国的璧。赵王派我将璧送来。可大王您好像并没有兑现的诚意。如今璧在我手里，想不交城拿走璧，那是妄想。”",
     "Lạn Tương Như ung dung đứng giữa điện, tay ôm ngọc nói: Đại vương cho người đến nước Triệu, nói dùng mười lăm tòa thành đổi ngọc của Triệu. Vua Triệu cử thần đem ngọc đến. Nhưng đại vương dường như không hề có thành ý thực hiện lời hứa. Nay ngọc ở trong tay thần, muốn không giao thành mà lấy ngọc, đó là vọng tưởng.",
     ["殿 là cung điện. 将 ở đây bằng 把, văn viết: 将璧送来. 诚意 là thành ý.",
      "Chú ý giọng điệu: lúc nãy còn nói xin đại vương, giờ thì nói thẳng 那是妄想, đó là vọng tưởng. Thái độ ung dung mà cứng rắn."]),
    ("蔺相如发誓，如若逼他，就将自己的头和璧一起撞碎在柱子上，秦王看到的将是他的尸体和破碎的玉。秦王连忙说：“别误会，我怎么会撒谎呢？”忙命大臣拿出地图，把十五座城指给蔺相如看。",
     "Lạn Tương Như thề rằng, nếu ép ông, ông sẽ đập đầu mình cùng viên ngọc vào cột cho vỡ nát, thứ vua Tần nhìn thấy sẽ là thi thể của ông và viên ngọc vỡ vụn. Vua Tần vội nói: Đừng hiểu lầm, ta sao lại nói dối được? Rồi vội sai đại thần mang bản đồ ra, chỉ mười lăm tòa thành cho Lạn Tương Như xem.",
     ["如若 là nếu như, văn viết. 撞碎 là đập vỡ, chữ 碎 là bổ ngữ kết quả. Trong 将是他的尸体, chữ 将 nghĩa là sẽ.",
      "连忙 và 忙 đều là vội vàng. 命 là ra lệnh. Vua Tần sợ mất ngọc nên lập tức đổi thái độ."]),
    ("蔺相如还是不敢相信秦王，说：“赵王送璧之前，举行了隆重的仪式：沐浴更衣，戒掉荤腥，只吃素食，以示庄严。我并非无理取闹，也不是冒犯大王。大王如真心换璧，亦请举行同样的仪式，我才敢把璧献给您。”",
     "Lạn Tương Như vẫn không dám tin vua Tần, nói: Trước khi gửi ngọc, vua Triệu đã cử hành một nghi lễ long trọng: tắm gội thay áo, kiêng đồ mặn đồ tanh, chỉ ăn chay, để tỏ lòng trang nghiêm. Thần không phải vô cớ gây chuyện, cũng không phải mạo phạm đại vương. Nếu đại vương thật lòng đổi ngọc, cũng xin cử hành nghi lễ như vậy, thần mới dám dâng ngọc lên ngài.",
     ["沐浴更衣 là tắm gội thay áo. 荤腥 là đồ mặn, đồ tanh; 素食 là đồ chay. 以示 là để tỏ ra. 并非 là không phải, văn viết. 如 là nếu, 亦 là cũng.",
      "Đòi cử hành nghi lễ chính là kế hoãn binh: Lạn Tương Như cần thời gian để đưa ngọc về nước."]),
    ("秦王想，璧都到了我这儿，我还怕他跑了不成？就说：“好，就依你。”",
     "Vua Tần nghĩ: ngọc đã đến tận chỗ ta rồi, lẽ nào ta còn sợ hắn chạy mất hay sao? Liền nói: Được, theo ý ngươi.",
     ["……不成？ ở cuối câu là câu hỏi ngược, nghĩa là lẽ nào… hay sao, ý là không thể nào. Đây là điểm ngữ pháp thứ hai.",
      "依 là theo, nghe theo: 就依你, theo ý ngươi. Sự chủ quan của vua Tần đã tạo cơ hội cho Lạn Tương Như."]),
    ("蔺相如回到住处，立刻派人打扮成商人的模样，偷偷越过边境，把璧送回了赵国，并嘱咐身边的人，不可泄露秘密。",
     "Lạn Tương Như về đến chỗ ở, lập tức sai người cải trang thành thương nhân, lén vượt qua biên giới, đưa ngọc về nước Triệu, đồng thời dặn dò những người bên cạnh không được tiết lộ bí mật.",
     ["打扮成……的模样 là ăn mặc thành dáng vẻ của…, tức là cải trang. 偷偷 là lén lút. 越过 là vượt qua.",
      "不可 là không được, văn viết. 嘱咐 là dặn dò. Đến đây, ngọc đã thật sự trở về nước Triệu."]),
    ("五天后，秦王率领众臣，准备接收和氏璧。蔺相如镇静地对秦王说：“秦国仗着国力雄厚，一贯霸道，不讲信用，声誉不好，事情我就不一一列举了，今天，我怕大王您不履行承诺，已经把璧送回了赵国。”",
     "Năm ngày sau, vua Tần dẫn các quan chuẩn bị nhận ngọc. Lạn Tương Như điềm tĩnh nói với vua Tần: Nước Tần cậy quốc lực hùng hậu, xưa nay vẫn ngang ngược, không giữ chữ tín, danh tiếng không tốt, những chuyện ấy thần không kể ra nữa. Hôm nay, vì sợ đại vương không thực hiện lời hứa, thần đã đưa ngọc về nước Triệu rồi.",
     ["仗着 là cậy vào, ỷ vào, mang nghĩa xấu. 不讲信用 là không giữ chữ tín. 一一列举 là kể ra từng cái một.",
      "履行承诺 là thực hiện lời hứa, cụm cố định rất hay gặp. Lạn Tương Như nói thẳng sự thật một cách điềm tĩnh, dù biết có thể nguy hiểm đến tính mạng."]),
    ("秦王听后大怒，说：“我堂堂秦王，还会骗你不成？你这不是歪曲我的意思吗？”",
     "Vua Tần nghe xong nổi giận, nói: Ta đường đường là vua Tần, lẽ nào lại lừa ngươi sao? Ngươi nói vậy chẳng phải là xuyên tạc ý ta à?",
     ["堂堂 là đường đường, đàng hoàng oai nghiêm. Lại gặp 不成: 还会骗你不成, lẽ nào lại lừa ngươi?",
      "这不是……吗？ là câu hỏi tu từ, nghĩa là đây chẳng phải là… sao, tức là khẳng định."]),
    ("蔺相如理直气壮地说：“众所周知，秦强赵弱。天下只可能强国欺负弱国，不可能弱国压迫强国。大王真要那块璧的话，不要光口头说，请先把十五座城割让给赵国，赵得到十五座城，绝不敢不把璧交出来。”",
     "Lạn Tương Như hùng hồn nói: Ai cũng biết, Tần mạnh Triệu yếu. Trong thiên hạ chỉ có nước mạnh ức hiếp nước yếu, chứ không thể có chuyện nước yếu chèn ép nước mạnh. Nếu đại vương thật sự muốn viên ngọc ấy, thì đừng chỉ nói miệng, xin hãy cắt nhường mười lăm tòa thành cho nước Triệu trước; Triệu có được mười lăm tòa thành rồi, tuyệt đối không dám không giao ngọc ra.",
     ["众所周知 là thành ngữ: ai ai cũng biết. 光 ở đây là phó từ, nghĩa là chỉ: 光口头说, chỉ nói miệng. 割让 là cắt đất nhường cho.",
      "绝不敢不 là phủ định hai lần: tuyệt đối không dám không giao, tức là chắc chắn sẽ giao."]),
    ("秦王听蔺相如说得在理，只得装出一副高姿态说：“不就是一块玉嘛，秦赵两国总不能为这点儿小事闹出隔阂，再起争端。”",
     "Vua Tần nghe Lạn Tương Như nói có lý, đành làm ra vẻ độ lượng mà nói: Chẳng qua chỉ là một khối ngọc thôi mà, hai nước Tần Triệu đâu thể vì chút chuyện nhỏ này mà sinh hiềm khích, lại nổi lên tranh chấp.",
     ["说得在理 là nói có lý. 只得 là đành phải. 装出一副高姿态 là làm ra vẻ cao thượng, độ lượng.",
      "不就是……嘛 là câu hỏi tu từ, nghĩa là chẳng qua chỉ là… thôi mà, ý coi nhẹ. Vua Tần nói vậy để giữ thể diện."]),
    ("蔺相如归赵以后，秦国再也没有提过以城换玉的事情。",
     "Sau khi Lạn Tương Như trở về nước Triệu, nước Tần không bao giờ nhắc lại chuyện lấy thành đổi ngọc nữa.",
     ["再也没有 cộng động từ cộng 过 nghĩa là không bao giờ… nữa.",
      "Câu kết cho thấy Lạn Tương Như đã thắng trọn vẹn: vừa giữ được ngọc, vừa không để nước Tần có cớ gây chiến."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 完璧归赵",
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 完璧归赵, dài một nghìn một trăm mười bốn chữ, được cải biên từ sách 学圣人悟做人。",
         F(0, "Thầy chia bài thành từng đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, (zh, vi, notes) in enumerate(P, 1):
    zsize = 54 if len(zh) <= 100 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, zh, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi, cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Tóm tắt nội dung", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5)", size=36,
    items=["## 1. 赵王因为什么事情发愁？ – 和氏璧",
           "答应…… sợ mắc lừa, mất ngọc mà không được thành · 不答应…… sợ đắc tội nước Tần",
           "## 2. 赵王派谁去秦国磋商？为什么？",
           "蔺相如：见多识广，足智多谋 · phân tích: 秦国强，赵国弱；送璧 → lỗi thuộc về Tần",
           "## 3. 蔺相如出使秦国的经过",
           "献玉 → 拿回玉 → 发誓 → 请秦王举行仪式 → 把玉偷偷送回赵国 → 跟秦王辩论",
           "## Kết quả: 完璧归赵 · 秦国再也没有提过以城换玉"],
    say=["Chúng ta cùng nhìn lại bố cục của cả bài khóa, theo gợi ý của bài tập năm trong sách.",
         F(0, "Câu hỏi thứ nhất: 赵王因为什么事情发愁？ Vua Triệu buồn rầu vì chuyện gì? Đó là chuyện ngọc Hòa Thị Bích."),
         F(1, "答应， nếu đồng ý thì sợ mắc lừa, mất ngọc mà không được thành. 不答应， nếu không đồng ý thì sợ đắc tội với nước Tần."),
         F(2, "Câu hỏi thứ hai: 赵王派谁去秦国磋商？为什么？ Vua Triệu cử ai sang Tần thương lượng, vì sao?"),
         F(3, "Đó là Lạn Tương Như, vì ông 见多识广，足智多谋， hiểu nhiều biết rộng, lắm mưu nhiều kế. Ông phân tích: Tần mạnh Triệu yếu, đưa ngọc sang thì nếu có lỗi, lỗi sẽ thuộc về nước Tần."),
         F(4, "Câu hỏi thứ ba: quá trình Lạn Tương Như đi sứ nước Tần."),
         F(5, "Gồm sáu bước: 献玉，拿回玉，发誓，请秦王举行仪式，把玉偷偷送回赵国，跟秦王辩论。 Tức là: dâng ngọc, lấy lại ngọc, thề liều chết, đòi vua Tần cử hành nghi lễ, lén đưa ngọc về nước Triệu, và tranh luận với vua Tần."),
         F(6, "Kết quả: ngọc trở về nước Triệu nguyên vẹn, và nước Tần không bao giờ nhắc lại chuyện lấy thành đổi ngọc nữa. Bố cục này rất có ích khi các bạn làm bài tập kể lại nội dung bài khóa.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 左……右……", section="Ngữ pháp 注释", title="1. 左……右…… (1): 左 + V₁ + 右 + V₂", size=40,
    items=["Nhấn mạnh một hành động lặp đi lặp lại nhiều lần",
           "Mẫu 1: 左V₁右V₂ – V₁ và V₂ giống nhau hoặc gần nghĩa",
           "秦王对着和氏璧左看右看，爱不释手。",
           "……怎么把璧拿回来呢？左思右想之后，他对秦王说……",
           "这个学生上课不专心听讲，总是左顾右盼。",
           "Thường gặp: 左看右看 · 左思右想 · 左顾右盼 · 左挑右选 · 左劝右劝"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là cấu trúc 左……右…….",
         F(0, "Cấu trúc này nhấn mạnh một hành động cùng loại được lặp đi lặp lại nhiều lần. Tiếng Việt hay dịch là: tới tới lui lui, đi đi lại lại, hết lần này đến lần khác."),
         F(1, "Mẫu thứ nhất: 左 cộng động từ một, 右 cộng động từ hai. Hai động từ này giống nhau, hoặc có nghĩa gần nhau."),
         F(2, "Ví dụ một, lấy từ bài khóa: 秦王对着和氏璧左看右看，爱不释手。 Vua Tần cầm ngọc ngắm tới ngắm lui, không nỡ rời tay. Ở đây hai động từ giống nhau: 看 và 看."),
         F(3, "Ví dụ hai, cũng trong bài khóa: 左思右想之后，他对秦王说。 Suy đi tính lại, ông nói với vua Tần. Ở đây 思 và 想 là hai động từ gần nghĩa, đều là suy nghĩ."),
         F(4, "Ví dụ ba: 这个学生上课不专心听讲，总是左顾右盼。 Cậu học sinh này lên lớp không chăm chú nghe giảng, cứ ngó nghiêng ngó dọc. 顾 và 盼 đều là nhìn."),
         F(5, "Những cụm thường gặp: 左看右看，左思右想，左顾右盼，左挑右选，左劝右劝。 Ngắm tới ngắm lui, suy đi tính lại, ngó nghiêng, chọn tới chọn lui, khuyên hết lời.")])

add("bullets", section="Ngữ pháp 注释", title="1. 左……右…… (2): 左一 + lượng từ + 右一 + lượng từ", size=40,
    items=["Mẫu 2: 左 + 一 + lượng từ (+ danh từ) + 右 + 一 + lượng từ (+ danh từ)",
           "那个电影，他左一遍右一遍地看，看了七八遍也看不够。",
           "她长得漂亮，爱玩儿自拍，手机里左一张右一张，都是自己的自拍照。",
           "妈妈左一个电话右一个电话地催他回家。",
           "Ý nghĩa: số lần rất nhiều, thường kèm cảm xúc (phàn nàn, sốt ruột)"],
    say=["Cấu trúc 左……右…… còn có mẫu thứ hai.",
         F(0, "Mẫu thứ hai: 左 cộng 一 cộng lượng từ, có thể thêm danh từ, rồi 右 cộng 一 cộng lượng từ, có thể thêm danh từ."),
         F(1, "Ví dụ một: 那个电影，他左一遍右一遍地看，看了七八遍也看不够。 Bộ phim đó, anh ấy xem hết lượt này đến lượt khác, xem bảy tám lần vẫn chưa đủ."),
         F(2, "Ví dụ hai: 她长得漂亮，爱玩儿自拍，手机里左一张右一张，都是自己的自拍照。 Cô ấy xinh đẹp, thích tự chụp ảnh, trong điện thoại hết tấm này đến tấm khác, toàn là ảnh tự chụp."),
         F(3, "Ví dụ ba: 妈妈左一个电话右一个电话地催他回家。 Mẹ gọi hết cuộc này đến cuộc khác giục anh ấy về nhà. Chú ý: khi làm trạng ngữ, phía sau thường có chữ 地."),
         F(4, "Mẫu này nhấn mạnh số lần rất nhiều, và thường mang theo cảm xúc của người nói, như phàn nàn, sốt ruột, hoặc ngạc nhiên.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: dùng 左……右…… hoàn thành câu", reveal=True, size=40,
    items=["(1) 我__________地去了你家五六趟了，你怎么老不在家呀！",
           "Đáp án: 我左一趟右一趟地去了你家五六趟了……",
           "(2) 大家__________，总算把她说通了。",
           "Đáp án: 大家左劝右劝，总算把她说通了。",
           "(3) 妈妈拿着女儿买的礼物，__________，越看越喜欢。",
           "Đáp án: ……左看右看，越看越喜欢。"],
    say=[F(0, "Luyện tập. Câu một: 我怎么样地去了你家五六趟了，你怎么老不在家呀！ Tôi đã đến nhà cậu năm sáu chuyến rồi, sao cậu cứ không có nhà thế! Chỗ trống điền gì? Các bạn hãy tạm dừng và thử hoàn thành câu."),
         F(1, "Đáp án: 我左一趟右一趟地去了你家五六趟了。 Tôi hết chuyến này đến chuyến khác đến nhà cậu. 趟 là lượng từ chỉ số chuyến đi, nên dùng mẫu thứ hai."),
         F(2, "Câu hai: 大家怎么样，总算把她说通了。 Mọi người làm sao đó, cuối cùng cũng thuyết phục được cô ấy."),
         F(3, "Đáp án: 大家左劝右劝，总算把她说通了。 Mọi người khuyên hết lời, cuối cùng cũng thuyết phục được cô ấy."),
         F(4, "Câu ba: 妈妈拿着女儿买的礼物，怎么样，越看越喜欢。 Mẹ cầm món quà con gái mua, càng nhìn càng thích."),
         F(5, "Đáp án: 妈妈拿着女儿买的礼物，左看右看，越看越喜欢。 Mẹ cầm món quà ngắm tới ngắm lui, càng ngắm càng thích. Câu này giống hệt câu 秦王左看右看 trong bài khóa.")])

add("bullets", chapter="Ngữ pháp: 不成", section="Ngữ pháp 注释", title="2. 不成 bùchéng – lẽ nào… hay sao?", size=40,
    items=["Trợ từ, đứng cuối câu: biểu thị suy đoán hoặc hỏi ngược (phản vấn)",
           "Phía trước thường có 难道 / 莫非 hô ứng",
           "璧都到了我这儿，我还怕他跑了不成？",
           "我堂堂秦王，(难道)还会骗你不成？",
           "他大吃一惊，头脑中一片空白——莫非受了骗不成？",
           "难道……不成？ = lẽ nào… hay sao? (ý: không thể nào)"],
    say=["Điểm ngữ pháp thứ hai là trợ từ 不成.",
         F(0, "不成 là trợ từ, đứng ở cuối câu, biểu thị ngữ khí suy đoán, hoặc ngữ khí hỏi ngược, tức là câu hỏi tu từ. Lúc này 不成 không còn nghĩa là không được nữa."),
         F(1, "Phía trước câu thường có các từ 难道 hoặc 莫非 để hô ứng với nhau. 难道 là lẽ nào, 莫非 là phải chăng, hay là."),
         F(2, "Ví dụ một, lấy từ bài khóa: 璧都到了我这儿，我还怕他跑了不成？ Ngọc đã đến tận chỗ ta rồi, lẽ nào ta còn sợ hắn chạy mất hay sao? Ý là: không có gì phải sợ."),
         F(3, "Ví dụ hai, cũng trong bài khóa: 我堂堂秦王，还会骗你不成？ Ta đường đường là vua Tần, lẽ nào lại lừa ngươi sao? Có thể thêm 难道 vào trước 还会 mà nghĩa không đổi."),
         F(4, "Ví dụ ba, ngữ khí suy đoán: 他大吃一惊，头脑中一片空白——莫非受了骗不成？ Anh ta giật mình, đầu óc trống rỗng: phải chăng mình đã bị lừa rồi?"),
         F(5, "Mẹo nhớ: 难道……不成？ tương đương 难道……吗？, nghĩa là lẽ nào… hay sao, và ý thật của người nói là: không thể nào.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: đổi thành câu hỏi ngược với 不成", reveal=True, size=38,
    items=["(1) 到现在你都不说出实情，难道是想一直这样骗下去吗？",
           "Đáp án: ……难道是想一直这样骗下去不成？",
           "(2) 你们大家都不说话，事情就这么算了吗？",
           "Đáp án: ……事情(难道)就这么算了不成？",
           "(3) 咱们多少年的朋友了，难道我会害你吗？",
           "Đáp án: 咱们多少年的朋友了，难道我会害你不成？"],
    say=[F(0, "Luyện tập: đổi câu hỏi thành câu hỏi ngược có 不成. Câu một: 到现在你都不说出实情，难道是想一直这样骗下去吗？ Đến giờ mà cậu vẫn không nói sự thật, lẽ nào muốn lừa mãi như vậy sao? Các bạn tạm dừng và thử đổi nhé."),
         F(1, "Đáp án: thay 吗 bằng 不成: 难道是想一直这样骗下去不成？"),
         F(2, "Câu hai: 你们大家都不说话，事情就这么算了吗？ Mọi người đều không nói gì, chuyện cứ thế cho qua sao?"),
         F(3, "Đáp án: 事情就这么算了不成？ Có thể thêm 难道 cho mạnh hơn: 事情难道就这么算了不成？"),
         F(4, "Câu ba: 咱们多少年的朋友了，难道我会害你吗？ Chúng ta là bạn bao nhiêu năm rồi, lẽ nào tôi lại hại cậu sao?"),
         F(5, "Đáp án: 难道我会害你不成？ Ý thật là: tôi không bao giờ hại cậu đâu.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 一贯 – 一直", section="Phân biệt từ 词语辨析", title="Phân biệt 一贯 và 一直 (1)",
    common="Giống nhau: đều có nghĩa xưa nay vẫn vậy, chưa từng thay đổi. Ví dụ: 他干活儿一贯/一直很卖力。",
    cols=[{"head": "一贯",
           "lines": ["(1) Thiên về tư tưởng, tác phong, thái độ; không chỉ hành động kéo dài",
                     "Đúng: 谦虚、朴素是他一贯的作风。",
                     "Sai: 雨一贯下了三天。"]},
          {"head": "一直",
           "lines": ["(1) Hành động liên tục không ngắt quãng, hoặc trạng thái không đổi",
                     "Đúng: 雨一直下了三天。",
                     "Đúng: 他一直是这个样子。"]}],
    say=["Tiếp theo là phần phân biệt từ: 一贯 và 一直. Cả hai đều có thể dịch là luôn luôn, xưa nay, nên rất dễ nhầm.",
         "Điểm giống nhau: cả hai đều có nghĩa là xưa nay vẫn như vậy, chưa từng thay đổi. Ví dụ: 他干活儿一贯很卖力， hoặc 一直很卖力， đều đúng. Anh ấy làm việc xưa nay luôn rất chăm chỉ.",
         F(0, "Điểm khác thứ nhất. 一贯 thiên về tư tưởng, tác phong, thái độ của con người, xưa nay vẫn thế. Nó thường không dùng để chỉ một hành động kéo dài liên tục."),
         F(0, "Ví dụ: 谦虚、朴素是他一贯的作风。 Khiêm tốn, giản dị là tác phong xưa nay của anh ấy. Nhưng nói 雨一贯下了三天 là sai, vì mưa là một hành động kéo dài, không phải tác phong."),
         F(1, "Còn 一直 có thể chỉ hành động liên tục không ngắt quãng, cũng có thể chỉ trạng thái không thay đổi. Ví dụ: 雨一直下了三天。 Mưa liền ba ngày. Và: 他一直是这个样子。 Anh ấy lúc nào cũng như vậy.")])

add("compare", section="Phân biệt từ 词语辨析", title="Phân biệt 一贯 và 一直 (2)",
    cols=[{"head": "一贯",
           "lines": ["(2) Từ quá khứ đến hiện tại, không dùng cho tương lai",
                     "Sai: 要把这种作风一贯坚持下去。",
                     "(3) Tính từ, bổ nghĩa được cho danh từ",
                     "Đúng: 这是他一贯的态度。"]},
          {"head": "一直",
           "lines": ["(2) Dùng được cho tương lai",
                     "Đúng: 要把这种作风一直坚持下去。",
                     "(3) Phó từ, không bổ nghĩa cho danh từ",
                     "Sai: 这是他一直的态度。"]}],
    say=[F(0, "Điểm khác thứ hai. 一贯 chỉ hành vi từ quá khứ đến hiện tại, không dùng cho tương lai. Vì vậy nói 要把这种作风一贯坚持下去 là sai."),
         F(1, "Còn 一直 dùng được cho tương lai. 要把这种作风一直坚持下去。 Phải luôn giữ vững tác phong này. Câu này đúng."),
         F(0, "Điểm khác thứ ba. 一贯 là tính từ, có thể bổ nghĩa cho danh từ. 这是他一贯的态度。 Đây là thái độ xưa nay của anh ấy. Câu này đúng. Trong bài khóa, 一贯霸道 cũng là tính từ làm trạng ngữ."),
         F(1, "Còn 一直 là phó từ, không bổ nghĩa cho danh từ. Nói 这是他一直的态度 là sai."),
         "Mẹo nhớ: nói về tác phong, phẩm chất, thái độ, hoặc cần đứng trước danh từ, dùng 一贯. Nói về hành động kéo dài, hoặc về tương lai, dùng 一直."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: chọn 一贯 hay 一直 điền vào chỗ trống", reveal=True, size=36,
    items=["(1) 自从昨天晚上听到这个不幸的消息，她就______在哭。",
           "Đáp án: 一直 – hành động kéo dài liên tục",
           "(2) 说实话，欺上瞒下是他______的手段。",
           "Đáp án: 一贯 – bổ nghĩa cho danh từ 手段",
           "(3) 爷爷______为人谦虚热情，是个公认的好人。",
           "Đáp án: 一贯 – nói về phẩm chất, tác phong (一直 cũng chấp nhận được)",
           "(4) 凝视着男友英俊的面庞，小文暗想：“多希望能______陪他走下去啊！”",
           "Đáp án: 一直 – nói về tương lai"],
    say=[F(0, "Bây giờ chúng ta làm thử. Câu một: 自从昨天晚上听到这个不幸的消息，她就什么在哭。 Từ tối qua nghe tin dữ này, cô ấy cứ khóc mãi. Chọn 一贯 hay 一直? Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: 一直. Vì khóc là hành động kéo dài liên tục từ tối qua đến giờ."),
         F(2, "Câu hai: 说实话，欺上瞒下是他什么的手段。 Nói thật, lừa trên dối dưới là thủ đoạn quen thuộc của anh ta."),
         F(3, "Đáp án: 一贯. Vì phía sau có chữ 的 và danh từ 手段, chỉ có tính từ 一贯 mới bổ nghĩa cho danh từ được."),
         F(4, "Câu ba: 爷爷什么为人谦虚热情，是个公认的好人。 Ông nội xưa nay sống khiêm tốn, nhiệt tình, ai cũng công nhận là người tốt."),
         F(5, "Đáp án: 一贯 là hay nhất, vì đây là nói về phẩm chất, cách làm người. Dùng 一直 cũng có thể chấp nhận được."),
         F(6, "Câu bốn: 凝视着男友英俊的面庞，小文暗想：多希望能什么陪他走下去啊！ Ngắm khuôn mặt điển trai của bạn trai, Tiểu Văn thầm nghĩ: mong sao có thể mãi bên anh ấy."),
         F(7, "Đáp án: 一直. Vì đây là mong ước cho tương lai, mà 一贯 không dùng cho tương lai.")])

# ======================= KỸ NĂNG VIẾT =======================
add("bullets", chapter="Kỹ năng viết: trích dẫn", section="Tu từ 篇章修辞", title="Phép trích dẫn (引用)", size=36,
    items=["Cố ý dẫn thành ngữ, thơ, cách ngôn, điển tích… để biểu đạt tư tưởng, tình cảm và kiến giải của mình",
           "(1) 赵王左右为难，不知如何答复秦王…… → thành ngữ 左右为难: thế này không xong, thế kia cũng không xong",
           "(2) 一个村民，怎么会有如此高超的修复古代文物的技艺？这还得从几年前一批珍贵文物被盗，之后完璧归赵的故事说起。 → điển tích 完璧归赵",
           "(3) 以前中国人深信的是“酒香不怕巷子深”，我的酒好，不用自己宣传…… → tục ngữ",
           "Tác dụng: ngắn gọn, giàu hình ảnh, tăng sức thuyết phục"],
    say=["Phần cuối cùng về lý thuyết là kỹ năng viết: phép trích dẫn, tiếng Trung gọi là 引用.",
         F(0, "Khi viết văn, người viết cố ý dẫn thành ngữ, câu thơ, cách ngôn, điển tích, để biểu đạt tư tưởng tình cảm của mình, và nói rõ cách hiểu của mình về vấn đề mới, đạo lý mới. Thủ pháp này gọi là trích dẫn."),
         F(1, "Ví dụ một, lấy từ bài khóa: 赵王左右为难，不知如何答复秦王。 Tác giả dẫn thành ngữ 左右为难, để tả tình cảnh làm thế này cũng không xong, làm thế kia cũng không xong."),
         F(2, "Ví dụ hai: 一个村民，怎么会有如此高超的修复古代文物的技艺？这还得从几年前一批珍贵文物被盗，之后完璧归赵的故事说起。 Một người dân làng sao lại có tay nghề phục chế cổ vật cao siêu như vậy? Chuyện này phải kể từ việc mấy năm trước một lô cổ vật quý bị trộm, rồi được trả về nguyên vẹn. Ở đây tác giả dẫn điển tích 完璧归赵."),
         F(3, "Ví dụ ba: 以前中国人深信的是酒香不怕巷子深。 Trước đây người Trung Quốc tin chắc rằng: rượu thơm thì chẳng sợ ngõ sâu. Ý là hàng tốt thì không cần quảng cáo, khách vẫn tự tìm đến. Đây là trích dẫn tục ngữ."),
         F(4, "Trích dẫn đúng chỗ giúp câu văn ngắn gọn, giàu hình ảnh, và tăng sức thuyết phục, vì những câu được dẫn đã được mọi người công nhận.")])

add("bullets", section="Tu từ 篇章修辞", title="Luyện tập: ghép 6 câu nhỏ thành 3 đoạn văn mạch lạc", size=32,
    items=["A. 以前咱们讲究的是什么？童叟无欺；言而有信；君子一言，驷马难追；酒香不怕巷子深",
           "B. 近年来，失眠症发病率居高不下，美国的失眠发生率高达32%~50%，英国在10%~14%之间，中国也在30%以上",
           "C. 从小我就常听妈妈说，“一寸光阴一寸金，寸金难买寸光阴”",
           "D. 现在可好，做假广告的，卖假冒伪劣产品的，考试作弊的，都出现了",
           "E. 世界卫生组织对14个国家的调查显示",
           "F. “少壮不努力，老大徒伤悲”，所以，人应该珍惜时间，从小努力"],
    say=["Luyện tập: hãy ghép sáu câu nhỏ sau thành ba đoạn văn mạch lạc. Mỗi đoạn đều có sử dụng phép trích dẫn.",
         F(0, "Câu A: 以前咱们讲究的是什么？童叟无欺；言而有信；君子一言，驷马难追；酒香不怕巷子深。 Trước đây chúng ta coi trọng điều gì? Không lừa người già trẻ nhỏ; nói phải giữ lời; quân tử nhất ngôn, tứ mã nan truy; rượu thơm chẳng sợ ngõ sâu."),
         F(1, "Câu B: 近年来，失眠症发病率居高不下，美国的失眠发生率高达百分之三十二到百分之五十，英国在百分之十到百分之十四之间，中国也在百分之三十以上。 Những năm gần đây tỷ lệ mắc chứng mất ngủ luôn ở mức cao."),
         F(2, "Câu C: 从小我就常听妈妈说，一寸光阴一寸金，寸金难买寸光阴。 Từ nhỏ tôi đã thường nghe mẹ nói: một tấc thời gian là một tấc vàng, tấc vàng khó mua được tấc thời gian."),
         F(3, "Câu D: 现在可好，做假广告的，卖假冒伪劣产品的，考试作弊的，都出现了。 Bây giờ thì hay rồi, kẻ quảng cáo gian dối, kẻ bán hàng giả hàng kém chất lượng, kẻ gian lận thi cử, đều xuất hiện cả."),
         F(4, "Câu E: 世界卫生组织对十四个国家的调查显示。 Điều tra của Tổ chức Y tế Thế giới ở mười bốn quốc gia cho thấy."),
         F(5, "Câu F: 少壮不努力，老大徒伤悲，所以，人应该珍惜时间，从小努力。 Lúc trẻ không cố gắng, về già chỉ biết đau buồn; vì vậy con người nên quý trọng thời gian, cố gắng từ nhỏ. Các bạn hãy tạm dừng và thử ghép nhé.")])

add("bullets", section="Tu từ 篇章修辞", title="Đáp án: ghép thành 3 đoạn văn", reveal=True, size=38,
    items=["(1) A + D: lời xưa (童叟无欺、言而有信……) ↔ hiện nay (做假广告……)",
           "Đáp án: 以前咱们讲究的是什么？童叟无欺……酒香不怕巷子深。现在可好，做假广告的……都出现了。",
           "(2) E + B: dẫn số liệu điều tra",
           "Đáp án: 世界卫生组织对14个国家的调查显示，近年来，失眠症发病率居高不下……",
           "(3) C + F: dẫn lời mẹ, câu tục ngữ về thời gian",
           "Đáp án: 从小我就常听妈妈说，“一寸光阴一寸金，寸金难买寸光阴”，“少壮不努力，老大徒伤悲”，所以……"],
    say=[F(0, "Đoạn thứ nhất: ghép A với D. Câu A dẫn những câu nói của người xưa về chữ tín, câu D nói về tình trạng ngày nay. Hai câu đối lập với nhau."),
         F(1, "Đáp án: 以前咱们讲究的是什么？童叟无欺，言而有信，君子一言，驷马难追，酒香不怕巷子深。现在可好，做假广告的，卖假冒伪劣产品的，考试作弊的，都出现了。"),
         F(2, "Đoạn thứ hai: ghép E với B. Câu E nêu nguồn là điều tra của Tổ chức Y tế Thế giới, câu B đưa ra số liệu. Các bạn chú ý: trích dẫn số liệu cũng là một dạng trích dẫn."),
         F(3, "Đáp án: 世界卫生组织对十四个国家的调查显示，近年来，失眠症发病率居高不下。"),
         F(4, "Đoạn thứ ba: ghép C với F. Cả hai đều dẫn những câu tục ngữ về thời gian, rồi rút ra kết luận."),
         F(5, "Đáp án: 从小我就常听妈妈说，一寸光阴一寸金，寸金难买寸光阴，少壮不努力，老大徒伤悲，所以，人应该珍惜时间，从小努力。")])

add("bullets", section="Tu từ 篇章修辞", title="Bài tập 4: tìm phần được trích dẫn", reveal=True, size=36,
    items=["(1) 俗话说：“不到长城非好汉！”今天我终于登上了长城。",
           "Đáp án: 不到长城非好汉 (câu nói nổi tiếng của Mao Trạch Đông, nay thành tục ngữ)",
           "(2) “只要功夫深，铁杵磨成针。”无论做什么事情，只要能坚持，有恒心，一定会成功的。",
           "Đáp án: 只要功夫深，铁杵磨成针 (tục ngữ: có công mài sắt, có ngày nên kim)",
           "(3) 我看他是醉翁之意不在酒啊，你千万小心，别上了他的当。",
           "Đáp án: 醉翁之意不在酒 (thành ngữ: ý của ông say không phải ở rượu)",
           "(4) 刚开学时，老师记不住大家的名字，常常张冠李戴。",
           "Đáp án: 张冠李戴 (thành ngữ: mũ ông Trương đội đầu ông Lý)"],
    say=[F(0, "Bài tập bốn trong sách cũng luyện phép trích dẫn: hãy tìm phần được trích dẫn trong mỗi câu. Câu một: 俗话说：不到长城非好汉！今天我终于登上了长城。 Tục ngữ nói: chưa đến Trường Thành chưa phải hảo hán. Hôm nay tôi cuối cùng đã leo lên Trường Thành."),
         F(1, "Đáp án: phần trích dẫn là 不到长城非好汉. Câu này vốn là một câu thơ của Mao Trạch Đông, nay đã thành tục ngữ."),
         F(2, "Câu hai: 只要功夫深，铁杵磨成针。无论做什么事情，只要能坚持，有恒心，一定会成功的。 Làm việc gì cũng vậy, chỉ cần kiên trì, có lòng bền bỉ, nhất định sẽ thành công."),
         F(3, "Đáp án: 只要功夫深，铁杵磨成针。 Câu này giống hệt câu tục ngữ Việt Nam: có công mài sắt, có ngày nên kim."),
         F(4, "Câu ba: 我看他是醉翁之意不在酒啊，你千万小心，别上了他的当。 Tôi thấy hắn có ý đồ khác đấy, cậu phải hết sức cẩn thận, đừng để mắc lừa hắn."),
         F(5, "Đáp án: 醉翁之意不在酒。 Thành ngữ này lấy từ bài văn của Âu Dương Tu, nghĩa đen là ý của ông lão say không phải ở rượu, nghĩa bóng là có mục đích khác."),
         F(6, "Câu bốn: 刚开学时，老师记不住大家的名字，常常张冠李戴。 Lúc mới khai giảng, thầy giáo không nhớ được tên mọi người, thường xuyên gọi nhầm."),
         F(7, "Đáp án: 张冠李戴。 Nghĩa đen là mũ của ông Trương đội lên đầu ông Lý, tức là nhầm lẫn người này với người kia.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ có dấu chấm", size=40,
    items=["妄想 (想) → 梦想 · 理想 · 空想 · 想法 (ví dụ mẫu)",
           "答复 (复) → 复习 · 复杂 · 重复 · 恢复",
           "荣幸 (幸) → 幸福 · 幸运 · 不幸 · 庆幸",
           "撒谎 (谎) → 谎言 · 谎话 · 说谎 · 谎报",
           "边境 (边) → 边疆 · 边界 · 旁边 · 周边"],
    say=["Phần luyện tập. Bài tập một: bắt chước ví dụ, dựa vào chữ có dấu chấm bên dưới, hãy viết thêm các từ khác.",
         F(0, "Ví dụ mẫu: 妄想, lấy chữ 想, có 梦想，理想，空想，想法. Tức là ước mơ, lý tưởng, không tưởng, và ý nghĩ."),
         F(1, "答复, lấy chữ 复, có 复习，复杂，重复，恢复. Tức là ôn tập, phức tạp, lặp lại, và khôi phục."),
         F(2, "荣幸, lấy chữ 幸, có 幸福，幸运，不幸，庆幸. Tức là hạnh phúc, may mắn, bất hạnh, và mừng thầm vì may mắn."),
         F(3, "撒谎, lấy chữ 谎, có 谎言，谎话，说谎，谎报. Tức là lời nói dối, lời nói dối, nói dối, và báo cáo sai sự thật."),
         F(4, "边境, lấy chữ 边, có 边疆，边界，旁边，周边. Tức là biên cương, đường biên giới, bên cạnh, và xung quanh.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (1–3)", reveal=True, size=36,
    items=["(1) 我的手机铃声不断响起，让我有点儿烦。（左一……右一……）",
           "Đáp án: 我的手机左一个电话右一个电话地响个不停，让我有点儿烦。",
           "(2) 为提高工作效率，小王建议把两个部门合并起来。（提议）",
           "Đáp án: 为提高工作效率，小王提议把两个部门合并起来。",
           "(3) 你对他诚挚的问候，我一定当面转告。（转达）",
           "Đáp án: 你对他诚挚的问候，我一定当面转达。"],
    say=[F(0, "Bài tập hai: dùng từ hoặc cấu trúc cho sẵn để viết lại câu. Câu một, dùng 左一……右一……: 我的手机铃声不断响起，让我有点儿烦。"),
         F(1, "Đáp án: 我的手机左一个电话右一个电话地响个不停，让我有点儿烦。 Điện thoại của tôi hết cuộc gọi này đến cuộc gọi khác, reo không ngừng, làm tôi hơi bực."),
         F(2, "Câu hai, dùng 提议: 为提高工作效率，小王建议把两个部门合并起来。"),
         F(3, "Đáp án: thay 建议 bằng 提议: 小王提议把两个部门合并起来。 Để nâng cao hiệu quả công việc, Tiểu Vương đề nghị sáp nhập hai bộ phận."),
         F(4, "Câu ba, dùng 转达: 你对他诚挚的问候，我一定当面转告。"),
         F(5, "Đáp án: 我一定当面转达。 Lời hỏi thăm chân thành của anh dành cho ông ấy, tôi nhất định sẽ chuyển tận mặt.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (4–6)", reveal=True, size=36,
    items=["(4) 我终于做到了若干年前对你的承诺。（兑现）",
           "Đáp án: 我终于兑现了若干年前对你的承诺。",
           "(5) 民族素质指国内各民族全体成员个体和群体的素质，也称国民素质。（亦）",
           "Đáp án: ……，亦称国民素质。",
           "(6) 你刚答应我的事，转眼就改变主意了，难道你想反悔吗？（不成）",
           "Đáp án: ……，难道你想反悔不成？"],
    say=[F(0, "Câu bốn, dùng 兑现: 我终于做到了若干年前对你的承诺。"),
         F(1, "Đáp án: 我终于兑现了若干年前对你的承诺。 Cuối cùng anh đã thực hiện được lời hứa với em từ nhiều năm trước."),
         F(2, "Câu năm, dùng 亦: 民族素质指国内各民族全体成员个体和群体的素质，也称国民素质。"),
         F(3, "Đáp án: thay 也 bằng 亦: 亦称国民素质。 Tố chất dân tộc là tố chất của cá nhân và tập thể mọi thành viên các dân tộc trong nước, cũng gọi là tố chất quốc dân. Câu này mang phong cách định nghĩa, văn viết, nên dùng 亦 rất hợp."),
         F(4, "Câu sáu, dùng 不成: 你刚答应我的事，转眼就改变主意了，难道你想反悔吗？"),
         F(5, "Đáp án: 难道你想反悔不成？ Việc cậu vừa hứa với tớ, chớp mắt đã đổi ý, lẽ nào cậu muốn nuốt lời hay sao?")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (1)", reveal=True, size=36,
    items=["Từ cho sẵn: 慷慨 · 答复 · 转达 · 实力 · 亏待",
           "一家公司想聘请我去工作，于是派人来说服我。来人先___了总经理的问候，然后又开始劝说：“凭你的___，几年之内，一定能升到副总的职位。而且我们老板很___，一定不会___你，……”我没有立即___他们，决定慎重地考虑考虑再说。",
           "Đáp án: 转达 · 实力 · 慷慨 · 亏待 · 答复"],
    say=[F(0, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn thứ nhất có năm từ: 慷慨，答复，转达，实力，亏待."),
         F(1, "一家公司想聘请我去工作，于是派人来说服我。 Một công ty muốn mời tôi đến làm việc, nên cử người đến thuyết phục. Người đó trước tiên chuyển lời hỏi thăm của tổng giám đốc, rồi khuyên: với năng lực của anh, vài năm là lên được phó tổng; hơn nữa sếp chúng tôi rất hào phóng, chắc chắn không bạc đãi anh. Tôi không trả lời họ ngay, quyết định suy nghĩ kỹ đã. Các bạn hãy tạm dừng và điền thử."),
         F(2, "Đáp án: 来人先转达了总经理的问候。 凭你的实力。 我们老板很慷慨，一定不会亏待你。 我没有立即答复他们。 Thứ tự là: 转达，实力，慷慨，亏待，答复.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (2)", reveal=True, size=36,
    items=["Từ cho sẵn: 列举 · 冒犯 · 雄厚 · 霸道 · 无理取闹",
           "班里有个很___的学生，大家都讨厌他。他仗着家里资金___，常常___。不但欺负同学，还___老师、撒谎、不讲信用……劣迹太多，无法一一___了。",
           "Đáp án: 霸道 · 雄厚 · 无理取闹 · 冒犯 · 列举"],
    say=[F(0, "Đoạn thứ hai có năm từ: 列举，冒犯，雄厚，霸道，无理取闹."),
         F(1, "班里有个很什么的学生，大家都讨厌他。 Trong lớp có một học sinh rất thế nào đó, ai cũng ghét. Cậu ta cậy nhà giàu, thường xuyên gây sự vô cớ, không chỉ bắt nạt bạn học mà còn vô lễ với thầy cô, nói dối, không giữ chữ tín, thói xấu nhiều đến mức không kể hết được. Các bạn hãy tạm dừng và điền thử."),
         F(2, "Đáp án: 班里有个很霸道的学生。 他仗着家里资金雄厚，常常无理取闹。 还冒犯老师。 无法一一列举了。 Thứ tự là: 霸道，雄厚，无理取闹，冒犯，列举. Các bạn để ý: 仗着，一一列举，不讲信用 đều là những cụm vừa gặp trong bài khóa.")])

add("bullets", section="Mở rộng 扩展", title="Mở rộng (1): cặp từ trái nghĩa", size=40,
    items=["保卫 bảo vệ ↔ 侵略 xâm lược",
           "撤退 rút lui ↔ 进攻 tấn công",
           "被告 bị cáo ↔ 原告 nguyên cáo",
           "暴力 bạo lực ↔ 和平 hòa bình",
           "招标 mời thầu ↔ 投标 dự thầu",
           "独裁 độc tài ↔ 民主 dân chủ · 书面 văn bản ↔ 口头 bằng miệng"],
    say=["Phần mở rộng của sách có hai nội dung. Nội dung thứ nhất: làm quen với các cặp từ trái nghĩa.",
         F(0, "保卫， là bảo vệ, trái nghĩa với 侵略， là xâm lược."),
         F(1, "撤退， là rút lui, trái nghĩa với 进攻， là tấn công."),
         F(2, "被告， là bị cáo, bên bị kiện; trái nghĩa với 原告， là nguyên cáo, bên đi kiện."),
         F(3, "暴力， là bạo lực, trái nghĩa với 和平， là hòa bình."),
         F(4, "招标， là mời thầu, trái nghĩa với 投标， là dự thầu."),
         F(5, "独裁， là độc tài, trái nghĩa với 民主， là dân chủ. Và 书面， là bằng văn bản, trái nghĩa với 口头， là bằng miệng, chính là từ mới số bốn mươi sáu của bài.")])

add("bullets", section="Mở rộng 扩展", title="Mở rộng (2): từ ngữ về học tập ở đại học", size=36,
    items=["大学毕业生想拿到文凭，首先得通过各科目的考试，考试时当然不能作弊，平时也不能总是旷课……",
           "文凭 văn bằng · 科目 môn học · 作弊 gian lận · 旷课 trốn học, nghỉ học không phép",
           "格式 định dạng · 标题 tiêu đề · 摘要 tóm tắt · 注释 chú thích · 要点 ý chính",
           "刊登 đăng (báo, tạp chí) · 刊物 tạp chí, ấn phẩm",
           "答辩 bảo vệ (luận văn) · 典礼 lễ, đại lễ"],
    say=["Nội dung mở rộng thứ hai: đọc một đoạn văn ngắn để làm quen với các từ ngữ về chuyện học ở đại học.",
         F(0, "大学毕业生想拿到文凭，首先得通过各科目的考试，考试时当然不能作弊，平时也不能总是旷课。 Sinh viên muốn lấy được bằng tốt nghiệp, trước hết phải thi qua các môn, khi thi đương nhiên không được gian lận, ngày thường cũng không được trốn học. Sau đó quan trọng nhất là viết khóa luận tốt nghiệp."),
         F(1, "文凭， là văn bằng. 科目， là môn học. 作弊， là gian lận. 旷课， là nghỉ học không phép, trốn học."),
         F(2, "Khóa luận phải đúng quy cách: 格式，标题，摘要，注释，要点。 Tức là định dạng, tiêu đề, tóm tắt, chú thích, và ý chính. Khóa luận phải có ý chính nổi bật, lập luận chặt chẽ."),
         F(3, "Một khóa luận tốt rất có thể được 刊登在专业刊物上， đăng trên tạp chí chuyên ngành. 刊登 là đăng, 刊物 là tạp chí, ấn phẩm."),
         F(4, "Viết xong thì phải 答辩， bảo vệ khóa luận. Bảo vệ thành công rồi thì vui vẻ dự 毕业典礼， lễ tốt nghiệp. Chúc các bạn sau này cũng bảo vệ thành công nhé!")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 27", size=36,
    items=["Từ vựng trọng tâm: 得罪 · 请教 · 慷慨 · 亏待 · 圈套 · 归还 · 从容 · 兑现 · 无理取闹 · 一贯 · 履行 · 歪曲 · 理直气壮",
           "Ngữ pháp: 左……右…… (lặp lại nhiều lần) · 不成 (cuối câu, hỏi ngược)",
           "Phân biệt: 一贯 (tác phong, tính từ, không dùng cho tương lai) ≠ 一直",
           "Viết: phép trích dẫn 引用 (左右为难 · 完璧归赵 · 酒香不怕巷子深)",
           "## Bài tập về nhà",
           "1. Kể lại câu chuyện 完璧归赵 theo gợi ý ở bài tập 5",
           "2. Viết bài 善于外交的…… (≥ 400 chữ) về một câu chuyện ngoại giao trong lịch sử Việt Nam"],
    say=["Chúng ta cùng tổng kết bài hai mươi bảy.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 得罪，请教，慷慨，亏待，圈套，归还，从容，兑现，无理取闹，一贯，履行，歪曲，理直气壮."),
         F(1, "Về ngữ pháp: 左……右…… nhấn mạnh hành động lặp lại nhiều lần. 不成 đứng cuối câu, thường hô ứng với 难道, tạo câu hỏi ngược."),
         F(2, "Về phân biệt từ: 一贯 nói về tác phong, thái độ, là tính từ, không dùng cho tương lai. 一直 chỉ hành động liên tục, là phó từ, dùng được cho tương lai."),
         F(3, "Về kỹ năng viết: dùng phép trích dẫn thành ngữ, tục ngữ, điển tích để câu văn ngắn gọn và thuyết phục hơn."),
         F(5, "Bài tập về nhà thứ nhất: dựa vào các gợi ý ở bài tập năm, hãy kể lại câu chuyện Hoàn bích quy Triệu bằng tiếng Trung."),
         F(6, "Bài tập thứ hai, phần vận dụng của sách: bài khóa kể một ví dụ kinh điển trong lịch sử ngoại giao Trung Quốc. Lịch sử Việt Nam cũng có rất nhiều câu chuyện như vậy, ví dụ Mạc Đĩnh Chi đi sứ nhà Nguyên, hay Giang Văn Minh đi sứ nhà Minh. Hãy viết một bài khoảng bốn trăm chữ trở lên, đặt tên là 善于外交的…… và kể lại một câu chuyện như vậy. Nhớ dùng các từ mới và phép trích dẫn nhé."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Hẹn gặp lại các bạn ở bài hai mươi tám: 高山流水遇知音, Núi cao nước chảy gặp tri âm, câu chuyện về tình bạn tri kỷ giữa Bá Nha và Tử Kỳ. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Hạ) – Bài 27: 完璧归赵 (Hoàn bích quy Triệu)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm
    "tts_replace": {
        "相如": "象如",          # Lìn Xiàngrú, tránh đọc xiāng
        "将相和": "匠象和",      # jiàng xiàng hé
        "列传": "列撰",          # lièzhuàn
        "为难": "违难",          # wéinán
        "上当": "上荡",          # shàngdàng
        "他的当": "他的荡",      # dàng
        "归还": "归环",          # guīhuán
        "泄露": "泄漏",          # xièlòu
        "歪曲": "歪屈",          # wāiqū
        "更衣": "耕衣",          # gēngyī
        "只得": "只德",          # zhǐdé
        "为人": "围人",          # wéirén
        "兴师": "星师",          # xīngshī
        "少壮": "绍壮",          # shàozhuàng
        "空白": "控白",          # kòngbái
        "重复": "虫复",          # chóngfù
        "请教": "请叫",          # qǐngjiào
    },
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai27.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
