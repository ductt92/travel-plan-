#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Thượng) – Bài 8 «遇见原来的我». Chạy để sinh bai08.json."""
import json
import os

TAG = "HSK 6 (Thượng) · Bài 8 · 遇见原来的我"
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
    zh="遇见原来的我", py="Yùjiàn yuánlái de wǒ",
    vi="Bài 8: Gặp lại tôi của ngày xưa",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Thượng.",
         "Hôm nay chúng ta học bài tám: 遇见原来的我。 Nghĩa là: Gặp lại tôi của ngày xưa.",
         "Đây là bài cuối cùng của Chủ đề hai, 不甘平庸, Không cam chịu tầm thường. Bài khóa đặt ra một câu hỏi triết học nghe thì đơn giản mà rất khó trả lời: tôi của hôm qua và tôi của hôm nay có phải là cùng một người không?",
         "Chúng ta sẽ cùng nghe ý kiến của ba nhà triết học nổi tiếng, rồi tự hỏi: nếu một ngày thức dậy, ta thấy mình không còn giống tôi của ngày xưa nữa, thì sao nhỉ?"])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài khóa: câu hỏi về bản thể (本体) và quan điểm của ba nhà triết học",
           "Nắm vững 41 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: 对……而言, 有关 (động từ và giới từ), xen ngữ 不瞒你说",
           "Phân biệt hai từ 极端 và 极度",
           "Kỹ năng: sắp xếp câu thành đoạn văn · Mở rộng: 13 cặp từ trái nghĩa"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa: câu hỏi về bản thể, tiếng Trung là 本体, và quan điểm khác nhau của ba nhà triết học về vấn đề này."),
         F(1, "Thứ hai, nắm vững bốn mươi mốt từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học ba điểm ngữ pháp: cấu trúc 对……而言, nghĩa là đối với… mà nói; từ 有关, vừa là động từ vừa là giới từ; và xen ngữ 不瞒你说, nghĩa là nói thật với bạn."),
         F(3, "Thứ tư, phân biệt hai từ rất dễ nhầm: 极端 và 极度."),
         F(4, "Thứ năm, luyện kỹ năng sắp xếp các câu thành một đoạn văn hoàn chỉnh, và làm quen với mười ba cặp từ trái nghĩa trong phần mở rộng."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Câu hỏi khởi động: Hôm qua và hôm nay", size=38,
    items=["“昨天的你和今天的你是同一个人吗？” – Bạn của hôm qua và bạn của hôm nay có phải cùng một người?",
           "(1) 不管你变化了多少，始终只有一个你。",
           "(2) 以前的你跟现在的你并不是同一个人。",
           "(3) 人的思想最重要，本体并不是最重要的。"],
    say=["Chúng ta bắt đầu bằng phần khởi động. Sách hỏi: 你思考过这样的哲学问题吗？ Bạn đã từng suy nghĩ về câu hỏi triết học như thế này chưa?",
         F(0, "昨天的你和今天的你是同一个人吗？ Bạn của hôm qua và bạn của hôm nay có phải là cùng một người không? Trong ba quan điểm sau, bạn đồng ý với quan điểm nào?"),
         F(1, "Quan điểm một: 不管你变化了多少，始终只有一个你。 Dù bạn thay đổi bao nhiêu, thì trước sau vẫn chỉ có một bạn mà thôi."),
         F(2, "Quan điểm hai: 以前的你跟现在的你并不是同一个人。 Bạn của trước kia và bạn của bây giờ không phải là cùng một người."),
         F(3, "Quan điểm ba: 人的思想最重要，本体并不是最重要的。 Tư tưởng của con người là quan trọng nhất, còn bản thể thì không phải là điều quan trọng nhất."),
         "Các bạn hãy tạm dừng video, chọn một quan điểm và thử giải thích bằng tiếng Trung. Lát nữa đọc bài khóa, các bạn sẽ thấy: ba quan điểm này chính là ý kiến của ba nhà triết học được nhắc đến trong bài."])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 信 và 现", size=38,
    items=["## 信 (tín): tin, lòng tin",
           "确信 tin chắc · 相信 tin tưởng · 自信 tự tin · 坚信 tin chắc chắn · 可信 đáng tin · 听信 nghe theo, tin lời",
           "信用 uy tín · 信心 lòng tin · 信任 tín nhiệm · 信念 niềm tin · 半信半疑 nửa tin nửa ngờ",
           "## 现 (hiện): hiện ra, lộ ra",
           "发现 phát hiện · 表现 biểu hiện · 实现 thực hiện · 再现 tái hiện · 体现 thể hiện",
           "展现 phô bày · 呈现 hiện ra · 现象 hiện tượng · 活灵活现 sống động như thật"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo, rất có lợi cho người Việt vì các chữ đều có âm Hán Việt quen thuộc.",
         F(0, "Nhóm thứ nhất có chữ 信, Hán Việt là tín, nghĩa là tin, lòng tin, như trong uy tín, tín nhiệm."),
         F(1, "确信，相信，自信，坚信，可信，听信。 Tức là: tin chắc, tin tưởng, tự tin, tin chắc chắn, đáng tin, và nghe theo lời người khác. Từ 确信 là từ mới trong bài khóa."),
         F(2, "信用，信心，信任，信念，半信半疑。 Tức là: uy tín, lòng tin, tín nhiệm, niềm tin, và nửa tin nửa ngờ."),
         F(3, "Nhóm thứ hai có chữ 现, Hán Việt là hiện, nghĩa là hiện ra, lộ ra."),
         F(4, "发现，表现，实现，再现，体现。 Tức là: phát hiện, biểu hiện, thực hiện, tái hiện, thể hiện."),
         F(5, "展现，呈现，现象，活灵活现。 Tức là: phô bày, hiện ra, hiện tượng, và sống động như thật. Từ 呈现 có trong bài: 河流流动时会呈现出不同的状态, dòng sông khi chảy sẽ hiện ra những trạng thái khác nhau.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 述 và 变", size=36,
    items=["## 述 (thuật): kể, trình bày",
           "口述 kể miệng · 讲述 kể lại · 复述 thuật lại · 记述 ghi lại · 论述 luận giải · 转述 thuật lại lời người khác",
           "自述 tự thuật · 陈述 trình bày · 表述 diễn đạt · 描述 miêu tả · 阐述 trình bày rõ · 述说 kể ra",
           "## 变 (biến): thay đổi",
           "改变 thay đổi · 变化 biến hóa · 变动 biến động · 变换 hoán đổi · 变样 đổi khác · 变形 biến dạng · 转变 chuyển biến",
           "渐变 đổi dần · 巨变 biến đổi lớn · 演变 diễn biến · 变心 thay lòng · 变种 biến chủng · 千变万化 thiên biến vạn hóa · 一成不变 bất biến"],
    say=[F(0, "Nhóm thứ ba có chữ 述, Hán Việt là thuật, như trong tường thuật, nghĩa là kể, trình bày."),
         F(1, "口述，讲述，复述，记述，论述，转述。 Tức là: kể miệng, kể lại, thuật lại, ghi lại, luận giải, và thuật lại lời của người khác."),
         F(2, "自述，陈述，表述，描述，阐述，述说。 Tức là: tự thuật, trình bày, diễn đạt, miêu tả, trình bày rõ, và kể ra. Hai từ 陈述 và 阐述 đều là từ mới của bài hôm nay."),
         F(3, "Nhóm cuối cùng có chữ 变, Hán Việt là biến, nghĩa là thay đổi. Đây chính là từ khóa của cả bài khóa."),
         F(4, "改变，变化，变动，变换，变样，变形，转变。 Tức là: thay đổi, biến hóa, biến động, hoán đổi, đổi khác, biến dạng, chuyển biến."),
         F(5, "渐变，巨变，演变，变心，变种，千变万化，一成不变。 Tức là: đổi dần dần, biến đổi lớn, diễn biến, thay lòng đổi dạ, biến chủng, thiên biến vạn hóa, và bất biến."),
         "Các bạn thấy không, chỉ cần nắm nghĩa của một chữ gốc, ta có thể đoán được nghĩa của cả một nhóm từ. Hãy áp dụng cách này khi học từ mới nhé."])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng)
V = [
    ("婴儿", "yīng'ér", "anh nhi", "danh từ", "trẻ sơ sinh, em bé", "婴儿每天要睡很长时间。", "Trẻ sơ sinh mỗi ngày phải ngủ rất lâu.",
     "Danh từ, chỉ em bé mới sinh, thường dưới một tuổi. Trong bài có cụm 婴儿时期, thời kỳ còn là em bé."),
    ("翻天覆地", "fāntiān-fùdì", "phiên thiên phúc địa", "thành ngữ", "long trời lở đất; (thay đổi) to lớn, triệt để", "这些年，家乡发生了翻天覆地的变化。", "Mấy năm nay, quê hương đã đổi thay hoàn toàn.",
     "Thành ngữ, nghĩa đen là lật trời đổ đất. Trong tiếng Trung, nó thường dùng để nói sự thay đổi rất lớn, rất triệt để, hay đi với 变化: 翻天覆地的变化. Chú ý: long trời lở đất trong tiếng Việt gợi sự chấn động dữ dội, còn 翻天覆地 hay dùng cho sự đổi thay to lớn, thường là tích cực."),
    ("更新", "gēngxīn", "canh tân", "động từ", "đổi mới, thay mới; cập nhật", "这个软件每个月都会更新一次。", "Phần mềm này mỗi tháng đều cập nhật một lần.",
     "Động từ, nghĩa là thay cái cũ bằng cái mới; ngày nay còn dùng với nghĩa cập nhật phần mềm. Chú ý cách đọc: âm tiết đầu đọc thanh một, khác với âm thanh bốn trong từ 更加. Trong bài: 皮肤被更新一百三十多次, làn da đã được thay mới hơn một trăm ba mươi lần."),
    ("酒窝", "jiǔwō", "tửu oa", "danh từ", "lúm đồng tiền", "她一笑，脸上就有两个酒窝。", "Cô ấy cười một cái là trên má hiện hai lúm đồng tiền.",
     "Danh từ, nghĩa là lúm đồng tiền. 酒 là rượu, 窝 là cái ổ, cái hõm: cái hõm nhỏ trên má như có thể chứa rượu, nghe rất thú vị phải không?"),
    ("蹦", "bèng", "bặng", "động từ", "nhảy", "孩子高兴得又蹦又跳。", "Đứa trẻ vui đến mức nhảy cẫng lên.",
     "Động từ, nghĩa là nhảy, bật người lên, thường dùng trong khẩu ngữ. Hay gặp cụm 又蹦又跳, nhảy nhót tưng bừng. Trong bài: 从高处往下蹦, nhảy từ trên cao xuống."),
    ("跌", "diē", "điệt", "động từ", "té, ngã; (giá cả) giảm", "他不小心跌了一跤。", "Anh ấy không cẩn thận bị ngã một cái.",
     "Động từ, nghĩa là té, ngã. Trong bài có từ 跌倒, ngã xuống. Ngoài ra, từ này còn dùng khi giá cả giảm xuống, như 股票跌了, cổ phiếu giảm giá."),
    ("疤", "bā", "ba", "danh từ", "vết sẹo", "他的手上有一块疤。", "Trên tay anh ấy có một vết sẹo.",
     "Danh từ, nghĩa là vết sẹo. Trong bài dùng từ 疤痕, cũng là vết sẹo, nhưng mang sắc thái văn viết hơn."),
    ("掩盖", "yǎngài", "yểm cái", "động từ", "che, phủ; che giấu", "大雪掩盖了整个村庄。", "Tuyết lớn phủ kín cả ngôi làng.",
     "Động từ, nghĩa đen là che phủ lên trên; nghĩa bóng là che giấu, như 掩盖错误, che giấu sai lầm. Trong bài, vết sẹo đã che mất cái lúm đồng tiền."),
    ("大脑", "dànǎo", "đại não", "danh từ", "bộ óc, đại não", "多读书可以锻炼大脑。", "Đọc nhiều sách có thể rèn luyện bộ óc.",
     "Danh từ, nghĩa là đại não, bộ óc. Âm Hán Việt và nghĩa giống hệt tiếng Việt."),
    ("确信", "quèxìn", "xác tín", "động từ", "tin chắc", "我确信他一定会来。", "Tôi tin chắc anh ấy nhất định sẽ đến.",
     "Động từ, nghĩa là tin chắc. Tiếng Việt ít dùng từ xác tín, nên các bạn cứ nhớ là tin chắc. Phía sau thường là cả một mệnh đề: 我确信，他一定会来."),
    ("比喻", "bǐyù", "tỷ dụ", "động từ", "ví như, so sánh ví von", "人们常把老师比喻为园丁。", "Người ta thường ví thầy cô như người làm vườn.",
     "Động từ, nghĩa là ví von, so sánh sự vật này với sự vật khác. Mẫu hay dùng là 把什么比喻为什么. Cẩn thận, đây là từ dễ nhầm: tỷ dụ trong tiếng Việt có nghĩa là ví dụ; còn 比喻 là ví von, cũng là danh từ chỉ phép so sánh trong tu từ."),
    ("呈现", "chéngxiàn", "trình hiện", "động từ", "thể hiện, lộ ra, hiện ra", "春天到了，公园里呈现出一片绿色。", "Mùa xuân đến, công viên hiện ra một màu xanh.",
     "Động từ, nghĩa là hiện ra, bày ra trước mắt, mang sắc thái văn viết. Hay dùng 呈现出 cộng một trạng thái. Trong bài: 河流流动时会呈现出不同的状态."),
    ("固有", "gùyǒu", "cố hữu", "tính từ", "vốn có, sẵn có", "每个民族都有自己固有的文化。", "Mỗi dân tộc đều có nền văn hóa vốn có của mình.",
     "Tính từ, nghĩa là vốn có, sẵn có từ trước, giống cố hữu trong cụm thói quen cố hữu của tiếng Việt. Thường làm định ngữ, như trong bài: 固有的那条河, dòng sông vốn có ấy."),
    ("阐述", "chǎnshù", "xiển thuật", "động từ", "trình bày, nêu rõ", "他在会上阐述了自己的看法。", "Trong cuộc họp, anh ấy trình bày rõ quan điểm của mình.",
     "Động từ, nghĩa là trình bày, giải thích rõ ràng một quan điểm, một lý luận, mang sắc thái văn viết. Trong bài: 他将自己的观点阐述为, ông ấy trình bày quan điểm của mình là."),
    ("陈述", "chénshù", "trần thuật", "động từ", "phát biểu, trình bày, nói rõ", "请你把事情的经过陈述一遍。", "Mời anh trình bày lại diễn biến sự việc một lượt.",
     "Động từ, nghĩa là trình bày, nói rõ một sự việc hay một ý kiến. Chú ý: trần thuật trong tiếng Việt hay dùng trong văn học, chỉ lời kể chuyện; còn 陈述 dùng rộng hơn, như trình bày trước tòa, trong cuộc họp. Câu trần thuật trong ngữ pháp gọi là 陈述句."),
    ("见解", "jiànjiě", "kiến giải", "danh từ", "cách nhìn, quan điểm", "他对这个问题有独到的见解。", "Anh ấy có cách nhìn độc đáo về vấn đề này.",
     "Danh từ, nghĩa là cách nhìn, quan điểm, nhận thức về một vấn đề. Hay gặp 独到的见解, cách nhìn độc đáo, và 发表见解, bày tỏ quan điểm."),
    ("演变", "yǎnbiàn", "diễn biến", "động từ", "biến đổi, tiến hóa (dần dần)", "汉字经历了几千年的演变。", "Chữ Hán đã trải qua mấy nghìn năm biến đổi.",
     "Động từ, nghĩa là biến đổi, phát triển dần dần qua một thời gian dài. Cẩn thận: diễn biến trong tiếng Việt thường chỉ quá trình xảy ra của một sự việc; còn 演变 nhấn mạnh sự thay đổi lâu dài, như chữ viết, ngôn ngữ, phong tục. Trong bài: 演变过程, quá trình biến đổi."),
    ("推测", "tuīcè", "suy trắc", "động từ", "suy đoán, dự đoán", "根据天气情况推测，明天可能会下雨。", "Đoán theo tình hình thời tiết, ngày mai có thể sẽ mưa.",
     "Động từ, nghĩa là dựa vào những điều đã biết để suy đoán điều chưa biết. 测 là đo, như trong 测量, đo lường. Từ này có trong bài tập hai."),
    ("譬如", "pìrú", "thí như", "động từ", "ví dụ, như", "我喜欢运动，譬如游泳、跑步。", "Tôi thích thể thao, ví dụ như bơi, chạy bộ.",
     "Động từ, nghĩa là ví dụ, chẳng hạn như; giống 比如 nhưng mang sắc thái văn viết hơn. Âm Hán Việt thí như, gần với thí dụ trong tiếng Việt. Đừng nhầm với 比喻 là ví von nhé."),
    ("各抒己见", "gèshū-jǐjiàn", "các trữ kỷ kiến", "thành ngữ", "mỗi người phát biểu ý kiến của mình", "会上，大家各抒己见，讨论得很热烈。", "Trong cuộc họp, mọi người đều nói lên ý kiến riêng, thảo luận rất sôi nổi.",
     "Thành ngữ. 各 là mỗi, 抒 là bày tỏ, như trong 抒情, trữ tình; 己见 là ý kiến của bản thân. Cả cụm nghĩa là mỗi người nói ra quan điểm riêng của mình."),
    ("通缉", "tōngjī", "thông tập", "động từ", "truy nã, truy bắt (tội phạm)", "警方正在通缉这名逃犯。", "Cảnh sát đang truy nã tên tội phạm bỏ trốn này.",
     "Động từ, nghĩa là truy nã, tức cơ quan công an ra lệnh truy bắt tội phạm đang lẩn trốn. Hay gặp 通缉令, lệnh truy nã."),
    ("触犯", "chùfàn", "xúc phạm", "động từ", "vi phạm, xâm phạm", "他的行为触犯了法律。", "Hành vi của anh ta đã vi phạm pháp luật.",
     "Động từ, nghĩa là vi phạm, đụng chạm đến luật pháp, quy định hay lợi ích của người khác. Cẩn thận, đây là từ dễ nhầm: xúc phạm trong tiếng Việt là làm tổn thương danh dự người khác; còn 触犯 thường đi với 法律 hay 规定, nghĩa là vi phạm. Muốn nói xúc phạm ai đó, tiếng Trung hay dùng 侮辱 hoặc 冒犯."),
    ("惩罚", "chéngfá", "trừng phạt", "động từ", "trừng phạt nghiêm khắc", "做错了事就应该受到惩罚。", "Làm sai thì phải chịu trừng phạt.",
     "Động từ, nghĩa là trừng phạt. Chú ý cách nói 受到惩罚, bị trừng phạt. Âm tiết đầu đọc thanh hai."),
    ("忧郁", "yōuyù", "ưu uất", "tính từ", "sầu muộn, buồn bã, u uất", "她最近总是很忧郁，不爱说话。", "Dạo này cô ấy lúc nào cũng buồn bã, không thích nói chuyện.",
     "Tính từ, nghĩa là buồn rầu, u uất kéo dài, gần với từ u uất của tiếng Việt. Còn bệnh trầm cảm thì tiếng Trung gọi là 忧郁症 hoặc 抑郁症."),
    ("肺", "fèi", "phế", "danh từ", "phổi", "吸烟对肺不好。", "Hút thuốc không tốt cho phổi.",
     "Danh từ, nghĩa là phổi. Hán Việt là phế, như trong viêm phế quản. Trong bài: 心、肺或者其他器官, tim, phổi hoặc các cơ quan khác."),
    ("器官", "qìguān", "khí quan", "danh từ", "(sinh vật học) bộ phận, cơ quan", "心是人体最重要的器官之一。", "Tim là một trong những cơ quan quan trọng nhất của cơ thể.",
     "Danh từ, chỉ các bộ phận của cơ thể như tim, phổi, mắt. Cẩn thận: cơ quan trong tiếng Việt còn nghĩa là nơi làm việc; còn 器官 chỉ dùng cho bộ phận cơ thể, cơ quan nhà nước phải nói là 机关. Cũng đừng nhầm với 气管, khí quản."),
    ("移植", "yízhí", "di thực", "động từ", "cấy, ghép", "这棵树是从山上移植过来的。", "Cái cây này được đánh từ trên núi về trồng.",
     "Động từ, nghĩa gốc là đánh cây từ nơi này đem trồng sang nơi khác; trong y học là cấy ghép, như 器官移植, ghép tạng, hay 移植手术, phẫu thuật cấy ghép."),
    ("面貌", "miànmào", "diện mạo", "danh từ", "bộ mặt, diện mạo, tướng mạo", "这座城市的面貌发生了很大的变化。", "Diện mạo của thành phố này đã thay đổi rất nhiều.",
     "Danh từ, nghĩa là diện mạo, khuôn mặt của con người; nghĩa bóng là bộ mặt, tình trạng chung của một nơi, như 城市面貌, bộ mặt thành phố, hay 精神面貌, tinh thần."),
    ("极端", "jíduān", "cực đoan", "tính từ", "cực đoan, quá khích", "他的想法太极端了。", "Suy nghĩ của anh ấy cực đoan quá.",
     "Tính từ, nghĩa là cực đoan, quá khích. Ngoài ra còn làm phó từ, nghĩa là cực kỳ, và làm danh từ, như 走极端, đi đến chỗ cực đoan. Lát nữa chúng ta sẽ phân biệt 极端 với 极度."),
    ("空前绝后", "kōngqián-juéhòu", "không tiền tuyệt hậu", "thành ngữ", "có một không hai", "这场演出的规模可以说是空前绝后。", "Quy mô buổi biểu diễn này có thể nói là có một không hai.",
     "Thành ngữ. 空前 là trước đây chưa từng có, 绝后 là sau này cũng không có nữa; giống thành ngữ vô tiền khoáng hậu của tiếng Việt. Trong bài: 一个极端得空前绝后的假设, một giả thuyết cực đoan có một không hai."),
    ("昏迷", "hūnmí", "hôn mê", "động từ", "hôn mê, bất tỉnh", "他受伤后昏迷了三天。", "Sau khi bị thương, anh ấy hôn mê ba ngày.",
     "Động từ, nghĩa là hôn mê, bất tỉnh. Âm Hán Việt và nghĩa giống hệt tiếng Việt. Trong bài: 从昏迷中清醒过来, tỉnh lại sau cơn hôn mê."),
    ("清醒", "qīngxǐng", "thanh tỉnh", "động từ", "tỉnh lại; tỉnh táo", "病人终于清醒过来了。", "Bệnh nhân cuối cùng đã tỉnh lại.",
     "Động từ, nghĩa là tỉnh lại sau khi hôn mê. Từ này còn làm tính từ, nghĩa là tỉnh táo, sáng suốt, như 头脑清醒, đầu óc tỉnh táo."),
    ("言论", "yánlùn", "ngôn luận", "danh từ", "ngôn luận, lời bàn", "网上的言论不一定都是真的。", "Những lời bàn tán trên mạng chưa chắc đều là thật.",
     "Danh từ, nghĩa là lời nói, ý kiến bàn luận về chính trị, xã hội hay một vấn đề nào đó. Hay gặp 言论自由, tự do ngôn luận."),
    ("学说", "xuéshuō", "học thuyết", "danh từ", "học thuyết", "这种学说影响了很多人。", "Học thuyết này đã ảnh hưởng đến rất nhiều người.",
     "Danh từ, nghĩa là học thuyết, tức hệ thống lý luận của một người hay một trường phái. Âm Hán Việt và nghĩa giống tiếng Việt."),
    ("遥远", "yáoyuǎn", "dao viễn", "tính từ", "xa xôi, xa vời", "那是一个遥远的国家。", "Đó là một đất nước xa xôi.",
     "Tính từ, nghĩa là xa xôi, dùng cho cả khoảng cách lẫn thời gian, như 遥远的未来, tương lai xa xôi. Trong bài: 离我们十分遥远, rất xa vời với chúng ta."),
    ("陷入", "xiànrù", "hãm nhập", "động từ", "rơi vào, sa vào", "他陷入了深深的思考。", "Anh ấy chìm vào suy tư sâu lắng.",
     "Động từ, nghĩa là rơi vào, sa vào một hoàn cảnh không tốt hay một trạng thái nào đó, như 陷入困境, rơi vào cảnh khó khăn, hay 陷入沉思, chìm vào suy tư."),
    ("思索", "sīsuǒ", "tư sách", "động từ", "suy nghĩ tìm tòi", "他思索了很久，才回答这个问题。", "Anh ấy suy nghĩ rất lâu mới trả lời câu hỏi này.",
     "Động từ, nghĩa là suy nghĩ kỹ, suy nghĩ tìm tòi để hiểu một vấn đề. Hay gặp thành ngữ 不假思索, chẳng cần suy nghĩ."),
    ("设想", "shèxiǎng", "thiết tưởng", "động từ", "tưởng tượng, hình dung", "我无法设想没有手机的生活。", "Tôi không thể tưởng tượng cuộc sống không có điện thoại.",
     "Động từ, nghĩa là hình dung, tưởng tượng ra một điều chưa xảy ra; cũng làm danh từ, nghĩa là ý tưởng, dự tính. Cẩn thận: thiết tưởng trong tiếng Việt có nghĩa là tôi nghĩ rằng, dùng để nêu ý kiến; còn 设想 là hình dung, giả định."),
    ("性命", "xìngmìng", "tính mệnh", "danh từ", "tính mạng, mạng sống", "医生救了他的性命。", "Bác sĩ đã cứu mạng anh ấy.",
     "Danh từ, nghĩa là tính mạng. Trong bài: 拿自己的性命开玩笑, đem tính mạng của mình ra làm trò đùa."),
    ("无忧无虑", "wú yōu wú lǜ", "vô ưu vô lự", "thành ngữ", "vô tư lự, không lo lắng gì", "小时候，我们过着无忧无虑的生活。", "Hồi nhỏ, chúng ta sống một cuộc sống vô tư lự.",
     "Thành ngữ. 忧 là buồn, 虑 là lo; cả cụm nghĩa là chẳng buồn chẳng lo, giống vô tư lự của tiếng Việt. Trong bài: 无忧无虑地过日子, sống những ngày vô tư lự."),
    ("崭新", "zhǎnxīn", "tiệm tân", "tính từ", "hoàn toàn mới, mới tinh", "他穿着一双崭新的皮鞋。", "Anh ấy đi một đôi giày da mới tinh.",
     "Tính từ, nghĩa là mới tinh, hoàn toàn mới; dùng được cho đồ vật lẫn điều trừu tượng, như 崭新的生活, cuộc sống hoàn toàn mới. Chú ý: âm tiết đầu đọc thanh ba. Câu cuối bài khóa là 一个崭新的我, một tôi hoàn toàn mới."),
]

add("bullets", chapter="Từ mới (41 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 8 có 41 từ mới, chia thành 14 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 更新 (gēng) · 惩罚 (chéng) · 崭新 (zhǎn)",
           "Từ dễ nhầm: 比喻 · 陈述 · 演变 · 触犯 · 器官 · 设想"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có bốn mươi mốt từ, thầy chia thành mười bốn nhóm nhỏ, mỗi nhóm hai hoặc ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số từ có âm đọc cần chú ý, như 更新，惩罚，崭新. Thầy sẽ nhắc khi gặp."),
         F(4, "Ngoài ra, có mấy từ Hán Việt rất dễ hiểu nhầm, như 比喻，陈述，演变，触犯，器官，设想. Nghĩa của chúng trong tiếng Trung khác với tiếng Việt, các bạn nhớ nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

sizes = [3] * 13 + [2]
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
    ("如果有一天，你看到自己婴儿时期的一张照片，你能认出自己吗？",
     "Nếu có một ngày, bạn nhìn thấy một tấm ảnh hồi bạn còn là em bé, bạn có nhận ra mình không?",
     ["认出 là nhận ra, 出 là bổ ngữ xu hướng chỉ kết quả: nhận diện ra được. 婴儿时期 là thời kỳ còn là em bé.",
      "Bài khóa mở đầu bằng một câu hỏi rất đời thường, để dẫn người đọc vào một vấn đề triết học."]),
    ("也许你会一下子认出自己，因为你觉得你一直都是你，但实际上，从拍照片的那一刻起，你的身上已经发生了翻天覆地的变化。",
     "Có lẽ bạn sẽ nhận ra mình ngay lập tức, vì bạn cảm thấy mình trước sau vẫn là mình; nhưng thực ra, kể từ khoảnh khắc chụp tấm ảnh ấy, trên người bạn đã xảy ra những thay đổi long trời lở đất.",
     ["一下子 là ngay lập tức, trong chốc lát. 从……起 nghĩa là kể từ… trở đi: 从拍照片的那一刻起, kể từ khoảnh khắc chụp ảnh.",
      "翻天覆地的变化 là sự thay đổi vô cùng to lớn. Chú ý cặp 你觉得…… với 但实际上……: cái ta cảm thấy và sự thật là hai chuyện khác nhau."]),
    ("比如说，你的皮肤自你出生以来已经被更新130多次了。你的酒窝不见了，5岁那年，你从高处往下蹦，跌倒了，脸上留下的疤痕掩盖了它。",
     "Ví dụ, làn da của bạn kể từ khi bạn ra đời đã được thay mới hơn một trăm ba mươi lần rồi. Lúm đồng tiền của bạn không còn nữa: năm năm tuổi, bạn nhảy từ trên cao xuống, bị ngã, vết sẹo để lại trên mặt đã che mất nó.",
     ["自……以来 nghĩa là từ… đến nay, văn viết: 自你出生以来, từ khi bạn ra đời đến nay. 被更新 là câu bị động với 被.",
      "从高处往下蹦 là nhảy từ chỗ cao xuống. 掩盖了它: chữ 它 ở đây thay cho 酒窝, lúm đồng tiền."],
     "比如说，你的皮肤自你出生以来已经被更新一百三十多次了。你的酒窝不见了，五岁那年，你从高处往下蹦，跌倒了，脸上留下的疤痕掩盖了它。"),
    ("你的大脑已经比拍照时增加了2～3倍的重量。",
     "Bộ não của bạn đã nặng thêm gấp hai đến ba lần so với lúc chụp ảnh.",
     ["比拍照时 là so với lúc chụp ảnh. Câu so sánh 比 kết hợp với 增加了……倍, tăng thêm bao nhiêu lần.",
      "Ba ví dụ về da, lúm đồng tiền và bộ não cho thấy: về mặt cơ thể, chúng ta thay đổi liên tục. Đây chính là ý của bài tập năm."],
     "你的大脑已经比拍照时增加了两到三倍的重量。"),
    ("如果你确信你就是你，不管怎样变化，那么，照片上的婴儿到底是不是你？是现在的你，还是一个不同的过去的你？",
     "Nếu bạn tin chắc rằng bạn vẫn là bạn, dù có thay đổi thế nào đi nữa, thì em bé trong ảnh rốt cuộc có phải là bạn không? Là bạn của hiện tại, hay là một bạn khác của quá khứ?",
     ["如果……那么…… là nếu… thì…. 不管怎样变化 là dù thay đổi thế nào, chen vào giữa câu để bổ sung ý.",
      "到底 dùng trong câu hỏi, nghĩa là rốt cuộc, nhấn mạnh muốn biết câu trả lời. 是……还是……？ là câu hỏi lựa chọn."]),
    ("如果是过去的你，那么，有多少个过去的你？是不是还会有更多的不同的你？",
     "Nếu là bạn của quá khứ, vậy thì có bao nhiêu cái bạn của quá khứ? Liệu có còn nhiều cái bạn khác nhau hơn nữa không?",
     ["Tác giả dùng một loạt câu hỏi liên tiếp để người đọc tự suy nghĩ. 是不是 đặt đầu câu hỏi, nghĩa là liệu có phải.",
      "有多少个过去的你 là có bao nhiêu cái tôi của quá khứ. Đây là cách diễn đạt rất triết học: mỗi giai đoạn của đời người là một cái tôi khác nhau."]),
    ("你用电脑生成了一张你50岁时的图片，对你而言，就像看一个陌生人。",
     "Bạn dùng máy tính tạo ra một bức ảnh của bạn lúc năm mươi tuổi; đối với bạn mà nói, nó giống như đang nhìn một người lạ.",
     ["生成 là tạo ra, thường dùng cho máy tính. 陌生人 là người lạ.",
      "对你而言 nghĩa là đối với bạn mà nói. Đây là điểm ngữ pháp thứ nhất của bài: 对……而言."],
     "你用电脑生成了一张你五十岁时的图片，对你而言，就像看一个陌生人。"),
    ("有关本体的问题，困扰了哲学家2500多年。什么是本体？这里说的本体就是我们的思想或身体。",
     "Vấn đề liên quan đến bản thể đã làm các nhà triết học bối rối hơn hai nghìn năm trăm năm. Bản thể là gì? Bản thể nói ở đây chính là tư tưởng hoặc cơ thể của chúng ta.",
     ["有关本体的问题 là vấn đề liên quan đến bản thể. 有关 là điểm ngữ pháp thứ hai của bài. 困扰 là làm phiền não, làm bối rối.",
      "本体 là bản thể, tức cái làm nên chính con người mình. Tác giả giải thích ngay: đó là tư tưởng hoặc cơ thể của chúng ta."],
     "有关本体的问题，困扰了哲学家两千五百多年。什么是本体？这里说的本体就是我们的思想或身体。"),
    ("赫拉克利特把自我比喻为一条河，河流流动时会呈现出不同的状态，但它始终是固有的那条河。",
     "Heraclitus ví cái tôi như một dòng sông: khi dòng sông chảy, nó sẽ hiện ra những trạng thái khác nhau, nhưng trước sau nó vẫn là dòng sông vốn có ấy.",
     ["赫拉克利特 là Heraclitus, nhà triết học Hy Lạp cổ đại, sống khoảng năm năm trăm bốn mươi đến bốn trăm tám mươi trước Công nguyên.",
      "把自我比喻为一条河 là ví cái tôi như một dòng sông, theo mẫu 把什么比喻为什么. 始终 là trước sau, từ đầu đến cuối."]),
    ("他将自己的观点阐述为：不管你变化了多少，始终只有一个你。",
     "Ông trình bày quan điểm của mình là: dù bạn thay đổi bao nhiêu, trước sau vẫn chỉ có một bạn.",
     ["Trong cụm 他将自己的观点阐述为, từ đứng sau chủ ngữ có nghĩa giống 把, mang sắc thái văn viết: đem quan điểm của mình trình bày thành.",
      "Đây chính là quan điểm thứ nhất trong phần khởi động. 不管……始终…… nghĩa là dù… thì trước sau vẫn…."]),
    ("大卫·休谟不同意“连续的自我”的观点。他是这样陈述自己的见解的：“我们的思想，是连续不断的认知组成的演变过程”。",
     "David Hume không đồng ý với quan điểm về một cái tôi liên tục. Ông trình bày cách nhìn của mình như sau: Tư tưởng của chúng ta là một quá trình biến đổi được tạo nên bởi những nhận thức nối tiếp không ngừng.",
     ["大卫·休谟 là David Hume, nhà triết học người Anh, sống từ năm một nghìn bảy trăm mười một đến năm một nghìn bảy trăm bảy mươi sáu.",
      "他是这样陈述自己的见解的 dùng cấu trúc nhấn mạnh để nói rõ cách thức: ông trình bày như thế này. 连续不断 là nối tiếp không ngừng. 认知 là nhận thức. 演变过程 là quá trình biến đổi dần dần."]),
    ("而你可以推测，譬如，婴儿大卫的油画呈现的是一个与成年大卫类似的人，并非完全相同。",
     "Và bạn có thể suy đoán, ví dụ như, bức tranh sơn dầu vẽ cậu bé David lúc còn sơ sinh thể hiện một người giống với David trưởng thành, chứ không hoàn toàn giống hệt.",
     ["油画 là tranh sơn dầu. 与成年大卫类似 là giống với David trưởng thành. 并非 là hoàn toàn không phải, văn viết, giống 并不是.",
      "Theo Hume, em bé David và David người lớn chỉ giống nhau chứ không phải là một. Đây là quan điểm thứ hai trong phần khởi động."]),
    ("哲学家们对本体的问题各抒己见，我们却在想一些更为实际的问题，假如休谟是对的，那么从现在开始，10年后你就会成为另一个人，你还需要遵守现在的你做出的承诺吗？",
     "Các nhà triết học mỗi người một ý về vấn đề bản thể, còn chúng ta thì lại nghĩ đến những vấn đề thực tế hơn: giả sử Hume đúng, thì tính từ bây giờ, mười năm sau bạn sẽ trở thành một người khác; vậy bạn còn cần giữ những lời hứa mà bạn của hiện tại đã đưa ra không?",
     ["却 là lại, chỉ sự đối lập: các nhà triết học bàn lý thuyết, còn chúng ta lại nghĩ chuyện thực tế. 更为实际 là thực tế hơn, văn viết.",
      "假如……那么…… là giả sử… thì…. 遵守承诺 là giữ lời hứa. 做出承诺 là đưa ra lời hứa."],
     "哲学家们对本体的问题各抒己见，我们却在想一些更为实际的问题，假如休谟是对的，那么从现在开始，十年后你就会成为另一个人，你还需要遵守现在的你做出的承诺吗？"),
    ("或者说，一个被通缉了15年的罪犯，今天还应该为当初触犯法律的行为受到惩罚吗？",
     "Hoặc nói cách khác, một tội phạm đã bị truy nã mười lăm năm, hôm nay có còn phải chịu trừng phạt vì hành vi vi phạm pháp luật năm xưa không?",
     ["或者说 là hay nói cách khác. 被通缉了十五年 là đã bị truy nã mười lăm năm. 当初 là lúc đầu, hồi đó.",
      "为当初触犯法律的行为受到惩罚 là bị trừng phạt vì hành vi vi phạm pháp luật năm xưa. Đây là câu hỏi rất thực tế: nếu con người thay đổi hoàn toàn, thì ai phải chịu trách nhiệm?"],
     "或者说，一个被通缉了十五年的罪犯，今天还应该为当初触犯法律的行为受到惩罚吗？"),
    ("我们每个人都会发生变化。譬如，你去整形，你因为过于忧郁而吃药，你做心、肺或者其他器官移植手术，这些都会逐渐改变你的面貌、情绪和行为，你还是你吗？",
     "Mỗi người chúng ta đều sẽ thay đổi. Ví dụ, bạn đi phẫu thuật thẩm mỹ, bạn uống thuốc vì quá u uất, bạn phẫu thuật ghép tim, phổi hay các cơ quan khác; tất cả những điều đó sẽ dần dần thay đổi diện mạo, cảm xúc và hành vi của bạn, vậy bạn có còn là bạn không?",
     ["整形 là phẫu thuật thẩm mỹ. 因为……而…… là vì… mà…, văn viết: 因为过于忧郁而吃药, vì quá u uất mà phải uống thuốc. 过于 là quá.",
      "逐渐 là dần dần. Ba ví dụ 整形、吃药、手术 chính là những nhân tố khiến con người thay đổi, câu hỏi của bài tập năm."]),
    ("德里克·帕菲特有一个极端得空前绝后的假设，例如将他的大脑一分为二，移植进另外两个身体中，两个人术后从昏迷中清醒过来，都会认为：“我是德里克。”",
     "Derek Parfit có một giả thuyết cực đoan có một không hai: ví dụ đem bộ não của ông chia làm đôi, cấy vào hai cơ thể khác; sau ca phẫu thuật, khi hai người tỉnh lại từ cơn hôn mê, cả hai đều sẽ cho rằng: Tôi là Derek.",
     ["德里克·帕菲特 là Derek Parfit, nhà triết học đương đại người Anh. 极端得空前绝后 là cực đoan đến mức có một không hai, cấu trúc tính từ cộng bổ ngữ trình độ.",
      "一分为二 là chia một thành hai. 移植进 là cấy vào. 术后 là sau phẫu thuật, văn viết của 手术以后."]),
    ("但是，德里克不可能是两个人，他也不可能只是其中的一个。由此，他得出结论：“个人的本体并不是真正重要的事情。”",
     "Nhưng Derek không thể là hai người, ông cũng không thể chỉ là một trong hai người đó. Từ đó, ông rút ra kết luận: Bản thể của mỗi cá nhân không phải là điều thật sự quan trọng.",
     ["其中的一个 là một trong số đó. 由此 là từ đó, do đó, văn viết. 得出结论 là rút ra kết luận.",
      "Đây là quan điểm thứ ba trong phần khởi động: bản thể không phải là điều quan trọng nhất."]),
    ("不瞒你说，对这个问题，我是这样想的：哲学家们的言论、学说离我们十分遥远，我们不会陷入本体的思索，",
     "Nói thật với bạn, về vấn đề này, tôi nghĩ như thế này: những ngôn luận, học thuyết của các nhà triết học rất xa vời với chúng ta, chúng ta sẽ không sa vào những suy tư về bản thể,",
     ["不瞒你说 là nói thật với bạn, một xen ngữ, điểm ngữ pháp thứ ba của bài. 瞒 là giấu giếm.",
      "陷入本体的思索 là sa vào suy tư về bản thể. Đến đây, tác giả chuyển từ ý kiến của triết gia sang suy nghĩ của người bình thường."]),
    ("我们也不会设想将大脑移植给两个人，那简直就是拿自己的性命开玩笑，我们只想无忧无虑地过日子。",
     "chúng ta cũng sẽ không hình dung chuyện đem bộ não cấy ghép cho hai người, điều đó quả thực là đem tính mạng của mình ra làm trò đùa; chúng ta chỉ muốn sống những ngày vô tư lự.",
     ["简直 là quả thực, gần như, dùng để nói quá. 拿……开玩笑 là đem… ra đùa giỡn: 拿自己的性命开玩笑.",
      "无忧无虑地过日子 là sống vô tư, không lo nghĩ. Với người bình thường, vấn đề bản thể rất xa vời."]),
    ("可是，会不会有一天，你醒来，感觉今天的我不像原来的我，而像是一个崭新的我了呢？",
     "Thế nhưng, liệu có một ngày nào đó, bạn thức dậy và cảm thấy tôi của hôm nay không giống tôi của ngày xưa, mà giống như một tôi hoàn toàn mới không nhỉ?",
     ["会不会 là liệu có…không. 不像……而像是…… là không giống… mà lại giống….",
      "Câu kết để mở, nối với tên bài: 遇见原来的我. Thay đổi là điều tất yếu; câu hỏi là ta có nhận ra tôi của ngày xưa không."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 遇见原来的我", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 遇见原来的我, dài chín trăm ba mươi hai chữ. Bài được cải biên từ bài viết cùng tên trong cuốn 同龄鸟·问你问我, tác giả là Cynthia Levinson.",
         F(0, "Thầy chia bài thành hai mươi đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh
    spoken = spoken.replace("“", "").replace("”", "").replace("·", "")
    zsize = 54 if len(zh) <= 90 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Tóm tắt nội dung", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5) – phần 1", size=36,
    items=["## 1. 从婴儿时期到现在，“你”发生了什么变化？",
           "皮肤：已经被更新130多次了",
           "酒窝：不见了，被疤痕掩盖了 · 大脑：增加了2～3倍的重量",
           "## 2. 到底有多少个“你”？",
           "婴儿时期的你 · 现在的你 · 以后的你（50岁的你，就像一个陌生人）"],
    say=["Bài tập năm của sách yêu cầu dựa vào gợi ý để tóm tắt nội dung chính của bài khóa. Chúng ta cùng làm luôn nhé.",
         F(0, "Câu hỏi một: 从婴儿时期到现在，你发生了什么变化？ Từ thời còn là em bé đến nay, bạn đã thay đổi những gì?"),
         F(1, "Về làn da: 你的皮肤已经被更新一百三十多次了。 Làn da đã được thay mới hơn một trăm ba mươi lần."),
         F(2, "Về lúm đồng tiền: 酒窝不见了，被疤痕掩盖了。 Lúm đồng tiền không còn, bị vết sẹo che mất. Về bộ não: 大脑增加了两到三倍的重量。 Bộ não nặng thêm gấp hai đến ba lần."),
         F(3, "Câu hỏi hai: 到底有多少个你？ Rốt cuộc có bao nhiêu cái bạn?"),
         F(4, "Có bạn của thời em bé, bạn của hiện tại, và bạn của sau này. Ví dụ bức ảnh bạn lúc năm mươi tuổi, nhìn vào chẳng khác gì nhìn một người lạ.")])

add("bullets", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5) – phần 2", size=34,
    items=["## 3. 关于本体的问题，哲学家们都有什么言论？",
           "赫拉克利特：不管你变化了多少，始终只有一个你。",
           "大卫·休谟：不同意“连续的自我”的观点，思想是连续不断的认知组成的演变过程。",
           "德里克·帕菲特：个人的本体并不是真正重要的事情。",
           "## 4. 假如休谟是对的，会带来什么样的问题？",
           "10年后还需要遵守现在的承诺吗？ · 罪犯还应该受到惩罚吗？"],
    say=[F(0, "Câu hỏi ba: 关于本体的问题，哲学家们都有什么言论？ Về vấn đề bản thể, các nhà triết học có những ý kiến gì?"),
         F(1, "Heraclitus cho rằng: 不管你变化了多少，始终只有一个你。 Dù bạn thay đổi bao nhiêu, trước sau vẫn chỉ có một bạn."),
         F(2, "David Hume không đồng ý với quan điểm cái tôi liên tục. Ông cho rằng: 思想是连续不断的认知组成的演变过程。 Tư tưởng là một quá trình biến đổi do những nhận thức nối tiếp tạo nên."),
         F(3, "Derek Parfit kết luận: 个人的本体并不是真正重要的事情。 Bản thể cá nhân không phải là điều thật sự quan trọng."),
         F(4, "Câu hỏi bốn: 假如休谟是对的，会带来什么样的问题？ Giả sử Hume đúng, thì sẽ nảy sinh vấn đề gì?"),
         F(5, "Thứ nhất, 十年后你还需要遵守现在的承诺吗？ Mười năm sau, bạn có còn phải giữ lời hứa của bây giờ không? Thứ hai, 被通缉了十五年的罪犯还应该受到惩罚吗？ Tội phạm bị truy nã mười lăm năm có còn phải chịu phạt không?")])

add("bullets", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5) – phần 3", size=36,
    items=["## 5. 导致人们改变的因素有哪些？",
           "整形 · 吃药 · （器官移植）手术",
           "## 6. 对普通人而言，本体的问题是怎样的？",
           "哲学家们的言论、学说离我们十分遥远，我们只想无忧无虑地过日子。",
           "可是，会不会有一天，你感觉自己像是一个崭新的我？"],
    say=[F(0, "Câu hỏi năm: 导致人们改变的因素有哪些？ Những nhân tố nào khiến con người thay đổi?"),
         F(1, "Sách gợi ý ba nhân tố: 整形，吃药，手术。 Phẫu thuật thẩm mỹ, uống thuốc, và phẫu thuật cấy ghép cơ quan."),
         F(2, "Câu hỏi sáu, phần này sách để trống cho các bạn tự viết: 对普通人而言，本体的问题是怎样的？ Đối với người bình thường, vấn đề bản thể là như thế nào?"),
         F(3, "Gợi ý: 哲学家们的言论、学说离我们十分遥远，我们只想无忧无虑地过日子。 Ngôn luận, học thuyết của các nhà triết học rất xa vời, chúng ta chỉ muốn sống vô tư lự."),
         F(4, "Nhưng tác giả vẫn để lại một câu hỏi: liệu có một ngày, ta cảm thấy mình đã trở thành một tôi hoàn toàn mới không? Bố cục sáu ý này rất có ích khi các bạn làm bài tập viết ở cuối bài.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 对……而言", section="Ngữ pháp 注释", title="1. 对……而言 – đối với… mà nói", size=38,
    items=["Biểu thị nhìn từ góc độ của một người, một sự việc nào đó",
           "Dùng trong văn viết · khẩu ngữ thường nói 对……来说、对……说来",
           "对今天的中国而言，经济发展必须坚持走可持续发展的道路。",
           "对年轻的我们而言，面对困难是件快乐的事情——那意味着挑战。",
           "你用电脑生成了一张你50岁时的图片，对你而言，就像看一个陌生人。"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là cấu trúc 对……而言.",
         F(0, "对……而言 biểu thị nhìn nhận sự việc từ góc độ của một người hay một sự việc nào đó, tiếng Việt dịch là đối với… mà nói. Ở giữa là danh từ hoặc đại từ chỉ đối tượng."),
         F(1, "Cấu trúc này dùng trong văn viết. Trong khẩu ngữ, người ta thường nói 对……来说, hoặc 对……说来, nghĩa tương tự."),
         F(2, "Ví dụ một: 对今天的中国而言，经济发展必须坚持走可持续发展的道路。 Đối với Trung Quốc ngày nay, phát triển kinh tế phải kiên trì đi theo con đường phát triển bền vững."),
         F(3, "Ví dụ hai: 对年轻的我们而言，面对困难是件快乐的事情，那意味着挑战。 Đối với những người trẻ như chúng ta, đối mặt với khó khăn là một chuyện vui, vì điều đó có nghĩa là thử thách."),
         F(4, "Ví dụ ba, lấy từ bài khóa: 你用电脑生成了一张你五十岁时的图片，对你而言，就像看一个陌生人。 Đối với bạn mà nói, nó giống như nhìn một người lạ.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: hoàn thành câu với 对……而言", reveal=True, size=38,
    items=["(1) 对母亲而言，……",
           "Đáp án: 对母亲而言，孩子的健康比什么都重要。",
           "(2) 对年轻人而言，……",
           "Đáp án: 对年轻人而言，最重要的是多学习、多积累经验。",
           "(3) ……，不看那场球，简直就是一辈子的遗憾。",
           "Đáp án: 对球迷而言，不看那场球，简直就是一辈子的遗憾。"],
    say=[F(0, "Luyện tập: hoàn thành câu. Câu một: 对母亲而言，…… Đối với người mẹ mà nói, điều gì? Các bạn tạm dừng và thử hoàn thành câu nhé."),
         F(1, "Đáp án gợi ý: 对母亲而言，孩子的健康比什么都重要。 Đối với người mẹ, sức khỏe của con quan trọng hơn bất cứ điều gì."),
         F(2, "Câu hai: 对年轻人而言，…… Đối với người trẻ mà nói, điều gì?"),
         F(3, "Đáp án gợi ý: 对年轻人而言，最重要的是多学习、多积累经验。 Đối với người trẻ, quan trọng nhất là học nhiều và tích lũy nhiều kinh nghiệm."),
         F(4, "Câu ba: 不看那场球，简直就是一辈子的遗憾。 Không xem trận bóng đó thì quả thực là tiếc nuối cả đời. Vậy đối với ai mới nói như vậy?"),
         F(5, "Đáp án gợi ý: 对球迷而言，不看那场球，简直就是一辈子的遗憾。 Đối với người hâm mộ bóng đá, không xem trận đó thì quả thực là tiếc cả đời.")])

add("bullets", chapter="Ngữ pháp: 有关", section="Ngữ pháp 注释", title="2. 有关 – có liên quan; về, liên quan đến", size=36,
    items=["## (1) Động từ: có quan hệ, có liên quan (= 有关系)",
           "有关本体的问题，困扰了哲学家2500多年。",
           "中国的语文教学向来重视识字，这固然和汉字的特点有关。",
           "## (2) Giới từ: liên quan đến, về (= 涉及)",
           "手术前，他仔细研究了中外有关病例的文字记载。",
           "为了这部历史剧服装的设计，他查阅了大量有关服饰问题的资料。"],
    say=["Điểm ngữ pháp thứ hai là từ 有关.",
         F(0, "Cách dùng thứ nhất: 有关 là động từ, nghĩa là có quan hệ, có liên quan, giống 有关系. Mẫu quen thuộc là 和什么有关, hoặc 与什么有关, có liên quan đến cái gì."),
         F(1, "Ví dụ một, lấy từ bài khóa: 有关本体的问题，困扰了哲学家两千五百多年。 Những vấn đề có liên quan đến bản thể đã làm các nhà triết học bối rối hơn hai nghìn năm trăm năm."),
         F(2, "Ví dụ hai: 中国的语文教学向来重视识字，这固然和汉字的特点有关。 Việc dạy ngữ văn ở Trung Quốc xưa nay luôn coi trọng việc nhận mặt chữ, điều này tất nhiên có liên quan đến đặc điểm của chữ Hán. Các bạn thấy từ 固然 của bài năm xuất hiện lại ở đây."),
         F(3, "Cách dùng thứ hai: 有关 là giới từ, nghĩa là liên quan đến, về, giống 涉及. Lúc này nó đi với một danh từ, cả cụm đứng trước danh từ khác làm định ngữ, như 有关病例的文字记载."),
         F(4, "Ví dụ ba: 手术前，他仔细研究了中外有关病例的文字记载。 Trước ca phẫu thuật, anh ấy nghiên cứu kỹ các ghi chép trong và ngoài nước về những ca bệnh liên quan."),
         F(5, "Ví dụ bốn: 为了这部历史剧服装的设计，他查阅了大量有关服饰问题的资料。 Để thiết kế trang phục cho bộ phim lịch sử này, anh ấy đã tra cứu rất nhiều tài liệu về vấn đề trang phục.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: chọn vị trí thích hợp cho 有关", reveal=True, size=34,
    items=["(1) 据A记载，从B明代中后期始，中国C的丝绸、瓷器等商品已由D中外商人贩运到拉美地区。",
           "Đáp án: A → 据有关记载……",
           "(2) A专家提出，办好B没有围墙的C大学，是中国高等教育迈入D大众化时代的关键一步。",
           "Đáp án: A → 有关专家提出……",
           "(3) A人们仿照B“酒吧”一词，在C汉语中复制出了很多“吧”。其中与原意稍为近似、与“喝”D的营业性场所就有：“啤酒吧”“水吧”“咖啡吧”“茶吧”“鲜果吧”等。",
           "Đáp án: D → 与“喝”有关的营业性场所"],
    say=[F(0, "Luyện tập: chọn vị trí thích hợp cho 有关. Câu một: 据记载，从明代中后期始，中国的丝绸、瓷器等商品已由中外商人贩运到拉美地区。 Theo ghi chép, từ giữa và cuối thời Minh, hàng hóa như lụa, đồ sứ của Trung Quốc đã được thương nhân trong và ngoài nước buôn bán sang khu vực Mỹ La-tinh. Đặt 有关 ở vị trí nào?"),
         F(1, "Đáp án: vị trí A. 据有关记载, theo những ghi chép có liên quan. Ở đây 有关 đứng ngay trước danh từ 记载."),
         F(2, "Câu hai: 专家提出，办好没有围墙的大学，是中国高等教育迈入大众化时代的关键一步。 Chuyên gia đưa ra ý kiến rằng làm tốt trường đại học không có tường rào là bước then chốt để giáo dục đại học Trung Quốc bước vào thời đại đại chúng hóa."),
         F(3, "Đáp án: vị trí A. 有关专家提出, các chuyên gia liên quan đưa ra ý kiến. Đây là cách nói rất phổ biến trên báo chí: 有关专家，有关部门."),
         F(4, "Câu ba: 人们仿照酒吧一词，在汉语中复制出了很多新词。其中与原意稍为近似的营业性场所就有啤酒吧，水吧，咖啡吧，茶吧，鲜果吧等。 Người ta mô phỏng từ quán bar, tạo ra rất nhiều từ mới; trong đó những địa điểm kinh doanh gần với nghĩa gốc là quán bia, quán nước, quán cà phê, quán trà, quán hoa quả tươi."),
         F(5, "Đáp án: vị trí D. 与喝有关的营业性场所, những địa điểm kinh doanh có liên quan đến việc uống. Ở đây 有关 là động từ, theo mẫu 与什么有关.")])

add("bullets", chapter="Ngữ pháp: 不瞒你说", section="Ngữ pháp 注释", title="3. 不瞒你说 – nói thật với bạn", size=36,
    items=["Xen ngữ (插入语): nêu suy nghĩ, cách nhìn, ý kiến hay thái độ chủ quan của người nói",
           "不瞒你说，对这个问题，我是这样想的。",
           "不瞒你说，书法方面，本人虽称不上“家”，但水平还是有一些的。",
           "Xen ngữ cùng loại: 我看 · 我想 · 说实在的 · 说真的 · 依我看 · 依我说 · 依我之见",
           "说真的，这次真是孩子给我上了一课：我深深地感到，想当好父母，首先要约束好自己的言行。",
           "说实在的，她的问题涉及了我的隐私，我很反感，话也变得火药味十足。"],
    say=["Điểm ngữ pháp thứ ba là 不瞒你说. Chữ 瞒 nghĩa là giấu giếm, nên 不瞒你说 nghĩa đen là không giấu gì bạn, tức là nói thật với bạn.",
         F(0, "不瞒你说 là một xen ngữ, tiếng Trung gọi là 插入语. Nó chen vào câu để biểu thị suy nghĩ, cách nhìn, ý kiến hay thái độ chủ quan của người nói. Bỏ nó đi, câu vẫn đúng ngữ pháp."),
         F(1, "Ví dụ một, lấy từ bài khóa: 不瞒你说，对这个问题，我是这样想的。 Nói thật với bạn, về vấn đề này, tôi nghĩ như thế này."),
         F(2, "Ví dụ hai: 不瞒你说，书法方面，本人虽称不上家，但水平还是有一些的。 Nói thật với bạn, về thư pháp, tôi tuy chưa dám gọi là nhà thư pháp, nhưng cũng có chút trình độ. 本人 là bản thân tôi, cách nói khiêm tốn và trang trọng."),
         F(3, "Những xen ngữ cùng loại thường dùng là: 我看，我想，说实在的，说真的，依我看，依我说，依我之见. Tức là: tôi thấy, tôi nghĩ, nói thật lòng, nói thật, theo tôi thấy, theo tôi nói, và theo ý kiến của tôi."),
         F(4, "Ví dụ ba: 说真的，这次真是孩子给我上了一课：我深深地感到，想当好父母，首先要约束好自己的言行。 Nói thật, lần này đúng là con đã dạy cho tôi một bài học: tôi cảm nhận sâu sắc rằng muốn làm cha mẹ tốt, trước hết phải giữ gìn lời nói và việc làm của chính mình."),
         F(5, "Ví dụ bốn, lấy từ bài năm: 说实在的，她的问题涉及了我的隐私，我很反感，话也变得火药味十足。 Nói thật lòng, câu hỏi của cô ấy đụng đến đời tư của tôi, tôi rất khó chịu, lời nói cũng sặc mùi thuốc súng.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: hoàn thành câu với xen ngữ", reveal=True, size=38,
    items=["(1) 依我之见，无论你怎么选择，……",
           "Đáp án: ……都应该先跟父母好好儿商量一下。",
           "(2) 不瞒你说，这个歌儿……",
           "Đáp án: ……我已经听了一百多遍了，可还是听不够。",
           "(3) 他淡淡地说：“我写文章，说真的，就是玩儿，……。”",
           "Đáp án: ……从来没想过要出名。"],
    say=[F(0, "Luyện tập: hoàn thành câu. Câu một: 依我之见，无论你怎么选择，…… Theo ý kiến của tôi, dù bạn lựa chọn thế nào thì sao? Các bạn tạm dừng và thử hoàn thành nhé."),
         F(1, "Đáp án gợi ý: 依我之见，无论你怎么选择，都应该先跟父母好好儿商量一下。 Theo tôi, dù bạn chọn thế nào, cũng nên bàn bạc kỹ với bố mẹ trước đã."),
         F(2, "Câu hai: 不瞒你说，这个歌儿…… Nói thật với bạn, bài hát này thì sao?"),
         F(3, "Đáp án gợi ý: 不瞒你说，这个歌儿我已经听了一百多遍了，可还是听不够。 Nói thật với bạn, bài hát này tôi đã nghe hơn một trăm lần rồi, mà vẫn nghe không chán."),
         F(4, "Câu ba: 他淡淡地说，我写文章，说真的，就是玩儿，…… Anh ấy thản nhiên nói: tôi viết văn, nói thật, chỉ là chơi thôi, rồi sao nữa?"),
         F(5, "Đáp án gợi ý: 我写文章，说真的，就是玩儿，从来没想过要出名。 Tôi viết văn, nói thật, chỉ là chơi thôi, chưa bao giờ nghĩ đến chuyện nổi tiếng.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 极端 – 极度", section="Phân biệt từ 词语辨析", title="Phân biệt 极端 và 极度",
    common="Giống nhau: làm phó từ, đều chỉ mức độ rất cao. Ví dụ: 他感到极度/极端疲劳。",
    cols=[{"head": "极端",
           "lines": ["(1) Thường bổ nghĩa cho từ mang nghĩa xấu",
                     "Đúng: 他极端苦恼。",
                     "(2) Làm được danh từ",
                     "Đúng: 看问题不要走极端。",
                     "(3) Làm tính từ: tuyệt đối, cực đoan",
                     "Đúng: 这种观点太极端。"]},
          {"head": "极度",
           "lines": ["(1) Bổ nghĩa được cả những từ khác",
                     "Đúng: 我们都极度兴奋。",
                     "(2) Thường không làm danh từ",
                     "Sai: 看问题不要走极度。",
                     "(3) Không làm tính từ",
                     "Sai: 这种观点太极度。"]}],
    say=["Tiếp theo là phần phân biệt từ: 极端 và 极度. Hai từ này đều có chữ 极, nghĩa là cực, nên học sinh rất hay dùng lẫn lộn.",
         "Điểm giống nhau: khi làm phó từ, cả hai đều chỉ mức độ rất cao, tiếng Việt là cực kỳ, vô cùng. Ví dụ: 整整工作了二十四小时，他感到极度疲劳, hoặc 极端疲劳, đều đúng. Làm việc suốt hai mươi bốn tiếng, anh ấy cảm thấy vô cùng mệt mỏi.",
         F(0, "Điểm khác thứ nhất. 极端 thường bổ nghĩa cho những từ mang nghĩa không tốt. Ví dụ: 面对这件自己解决不了的事情，他极端苦恼。 Đối mặt với việc mình không giải quyết được, anh ấy vô cùng phiền não."),
         F(1, "Còn 极度 thì bổ nghĩa được cả những từ khác, kể cả từ mang nghĩa tốt. Ví dụ: 听到这个消息，我们都极度兴奋。 Nghe tin này, chúng tôi đều vô cùng phấn khởi. Ở đây không nên dùng 极端, vì phấn khởi là cảm xúc tích cực."),
         F(0, "Điểm khác thứ hai. 极端 làm được danh từ, nghĩa là chỗ cực đoan. Ví dụ: 看问题要全面，不要走极端。 Nhìn nhận vấn đề phải toàn diện, đừng đi đến cực đoan."),
         F(1, "极度 thì thường không làm danh từ, nên không nói 走极度."),
         F(0, "Điểm khác thứ ba. 极端 còn làm tính từ, nghĩa là tuyệt đối, cực đoan, quá khích. Ví dụ: 这种观点太极端。 Quan điểm này quá cực đoan. Và trong bài khóa: 他有个极端得空前绝后的想法。 Ông ấy có một ý tưởng cực đoan có một không hai."),
         F(1, "极度 không có cách dùng này, nên không nói 这种观点太极度."),
         "Mẹo nhớ: 极端 có chữ 端, là đầu mút, nên làm được danh từ và tính từ, chỉ cái đầu cực đoan; còn 极度 có chữ cuối là mức độ, như trong 程度, nên chủ yếu chỉ dùng làm phó từ chỉ mức độ."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: chọn 极端 hay 极度 điền vào chỗ trống", reveal=True, size=38,
    items=["(1) 他的做法___得让我们无法相信。",
           "Đáp án: 极端 – tính từ, có bổ ngữ trình độ phía sau",
           "(2) 紧张的考试之后，他感到___地放松。",
           "Đáp án: 极度 – bổ nghĩa cho từ mang nghĩa tốt (放松)",
           "(3) 他从一个___走向了另一个___。",
           "Đáp án: 极端 · 极端 – dùng làm danh từ",
           "(4) 你的这种观点太___了，不能代表大多数人的看法。",
           "Đáp án: 极端 – tính từ, nghĩa là cực đoan"],
    say=[F(0, "Bây giờ chúng ta làm thử: chọn 极端 hay 极度 điền vào chỗ trống. Câu một: 他的做法什么得让我们无法相信。 Cách làm của anh ta như thế nào đến mức chúng tôi không thể tin nổi. Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: 极端. 他的做法极端得让我们无法相信。 Cách làm của anh ta cực đoan đến mức không thể tin nổi. Ở đây từ cần điền là tính từ, phía sau có bổ ngữ trình độ, nên chỉ dùng được 极端."),
         F(2, "Câu hai: 紧张的考试之后，他感到什么地放松。 Sau kỳ thi căng thẳng, anh ấy cảm thấy vô cùng thư thái."),
         F(3, "Đáp án: 极度. 他感到极度地放松。 放松 là cảm giác dễ chịu, mang nghĩa tốt, nên dùng 极度."),
         F(4, "Câu ba: 他从一个什么走向了另一个什么。 Anh ấy đi từ một thái cực này sang một thái cực khác."),
         F(5, "Đáp án: cả hai chỗ đều là 极端. 他从一个极端走向了另一个极端。 Ở đây cần danh từ, đứng sau lượng từ 一个, nên chỉ dùng được 极端."),
         F(6, "Câu bốn: 你的这种观点太什么了，不能代表大多数人的看法。 Quan điểm này của bạn quá thế nào đó, không thể đại diện cho cách nhìn của đa số."),
         F(7, "Đáp án: 极端. 你的这种观点太极端了。 Quan điểm của bạn cực đoan quá. Đây là cách dùng tính từ, nghĩa là cực đoan.")])

# ======================= KỸ NĂNG: SẮP XẾP CÂU THÀNH ĐOẠN =======================
add("bullets", chapter="Kỹ năng: sắp xếp câu thành đoạn", section="Kỹ năng 语段", title="Kỹ năng: sắp xếp câu thành đoạn văn (语段排序)", size=34,
    items=["Dạng bài của bài tập 4, rất hay gặp trong đề thi đọc hiểu",
           "Bước 1: Tìm câu mở đầu – nêu đủ nhân vật, thời gian; không bắt đầu bằng 可是、所以、这",
           "Bước 2: Dựa vào từ nối – 可是、但是 (chuyển ý) · 所以、因此 (kết quả) · 于是 (tiếp nối)",
           "Bước 3: Dựa vào đại từ – 他、她、这、那 phải đứng sau từ mà nó thay thế",
           "Bước 4: Dựa vào trình tự thời gian và logic – 去年 → 一年后的今天; nguyên nhân → kết quả",
           "Bước 5: Đọc lại cả đoạn, kiểm tra ý có liền mạch không"],
    say=["Bây giờ chúng ta sang phần kỹ năng. Quyển này không có mục tu từ riêng, nên thầy chọn kỹ năng của bài tập bốn: sắp xếp các câu theo đúng thứ tự để tạo thành một đoạn văn, tiếng Trung gọi là 语段排序.",
         F(0, "Đây là dạng bài rất hay gặp trong đề thi đọc hiểu. Muốn làm tốt, các bạn đi theo năm bước sau."),
         F(1, "Bước một: tìm câu mở đầu. Câu mở đầu thường giới thiệu đầy đủ nhân vật, thời gian, địa điểm. Nó không bắt đầu bằng từ nối như 可是，所以, hay đại từ như 这."),
         F(2, "Bước hai: dựa vào từ nối. 可是 và 但是 báo hiệu chuyển ý, nên phía trước phải có một ý ngược lại. 所以 và 因此 chỉ kết quả, nên phía trước phải có nguyên nhân. 于是 chỉ việc xảy ra tiếp theo."),
         F(3, "Bước ba: dựa vào đại từ. Các đại từ như 他，她，这，那 phải đứng sau danh từ mà nó thay thế."),
         F(4, "Bước bốn: dựa vào trình tự thời gian và logic, ví dụ 去年 rồi mới đến 一年后的今天, nguyên nhân rồi mới đến kết quả."),
         F(5, "Bước năm: đọc lại cả đoạn từ đầu đến cuối, kiểm tra xem ý có liền mạch, tự nhiên không. Bây giờ chúng ta áp dụng vào bài tập bốn của sách.")])

add("bullets", section="Kỹ năng 语段", title="Bài tập 4: Sắp xếp thành đoạn văn", reveal=True, size=36,
    items=["A. 她一个人坐在这里 · B. 她想起去年的现在，她是和男朋友两个人坐在这地方",
           "C. 她当时心情是多么激动和欢快啊 · D. 心里像装着一块冰 · E. 可是一年后的今天",
           "Đáp án: B – C – E – A – D",
           "她想起去年的现在，她是和男朋友两个人坐在这地方，她当时心情是多么激动和欢快啊！可是一年后的今天，她一个人坐在这里，心里像装着一块冰。"],
    say=[F(0, "Bài tập bốn có năm câu. A: 她一个人坐在这里。 Cô ấy ngồi đây một mình. B: 她想起去年的现在，她是和男朋友两个人坐在这地方。 Cô ấy nhớ lại giờ này năm ngoái, cô ấy cùng bạn trai hai người ngồi ở chỗ này."),
         F(1, "C: 她当时心情是多么激动和欢快啊。 Lúc ấy tâm trạng cô ấy xúc động và vui sướng biết bao. D: 心里像装着一块冰。 Trong lòng như chứa một tảng băng. E: 可是一年后的今天。 Nhưng hôm nay, một năm sau. Các bạn tạm dừng và thử sắp xếp nhé."),
         F(2, "Đáp án: B, C, E, A, D. Câu B nêu thời gian 去年的现在 và nhân vật đầy đủ, nên mở đầu. Câu C có 当时, lúc ấy, nên theo sau B. Câu E có 可是, chuyển sang hiện tại, đối lập với quá khứ. Sau đó A nói cô ấy ngồi một mình, và D kết thúc bằng tâm trạng lạnh giá."),
         F(3, "Cả đoạn là: 她想起去年的现在，她是和男朋友两个人坐在这地方，她当时心情是多么激动和欢快啊！可是一年后的今天，她一个人坐在这里，心里像装着一块冰。 Các bạn thấy không: hai người đối lập với một người, vui sướng đối lập với tảng băng. Chính sự đối lập này giúp ta sắp xếp đúng.")])

add("bullets", section="Kỹ năng 语段", title="Luyện thêm: sắp xếp thành đoạn văn", reveal=True, size=36,
    items=["A. 于是他每天早上六点起床跑步 · B. 去年体检时，医生说他太胖了",
           "C. 现在他已经瘦了十公斤 · D. 一开始他觉得很辛苦 · E. 但坚持了三个月以后，就习惯了",
           "Đáp án: B – A – D – E – C",
           "去年体检时，医生说他太胖了，于是他每天早上六点起床跑步。一开始他觉得很辛苦，但坚持了三个月以后，就习惯了。现在他已经瘦了十公斤。"],
    say=[F(0, "Chúng ta luyện thêm một bài nữa. A: 于是他每天早上六点起床跑步。 Thế là mỗi sáng anh ấy dậy lúc sáu giờ để chạy bộ. B: 去年体检时，医生说他太胖了。 Năm ngoái khi khám sức khỏe, bác sĩ nói anh ấy béo quá."),
         F(1, "C: 现在他已经瘦了十公斤。 Bây giờ anh ấy đã giảm được mười cân. D: 一开始他觉得很辛苦。 Lúc đầu anh ấy thấy rất vất vả. E: 但坚持了三个月以后，就习惯了。 Nhưng sau khi kiên trì ba tháng thì đã quen. Các bạn tạm dừng và thử sắp xếp nhé."),
         F(2, "Đáp án: B, A, D, E, C. Câu B có thời gian 去年 và nêu nguyên nhân, nên đứng đầu. Câu A có 于是, chỉ việc làm tiếp theo. D có 一开始, E có 但 chuyển ý, và C có 现在 là kết quả cuối cùng."),
         F(3, "Cả đoạn là: 去年体检时，医生说他太胖了，于是他每天早上六点起床跑步。一开始他觉得很辛苦，但坚持了三个月以后，就习惯了。现在他已经瘦了十公斤。 Các bạn để ý các từ chỉ thời gian: 去年，一开始，三个月以后，现在. Đó chính là cái khung của đoạn văn.")])

# ======================= MỞ RỘNG: TỪ TRÁI NGHĨA =======================
add("bullets", chapter="Mở rộng: từ trái nghĩa", section="Mở rộng 扩展", title="Mở rộng 扩展: các cặp từ trái nghĩa", size=36,
    items=["动荡 bất ổn ↔ 稳定 ổn định · 服从 phục tùng ↔ 违抗 chống lệnh",
           "复活 sống lại ↔ 灭亡 diệt vong · 高潮 cao trào ↔ 低潮 thoái trào",
           "高尚 cao thượng ↔ 低俗 dung tục · 合并 sáp nhập ↔ 解散 giải tán",
           "混浊 đục ↔ 清澈 trong vắt · 简陋 sơ sài ↔ 豪华 sang trọng",
           "歌颂 ca ngợi ↔ 批判 phê phán · 停滞 đình trệ ↔ 发展 phát triển",
           "推翻 lật đổ ↔ 建立 thành lập · 延期 hoãn lại ↔ 提前 đưa lên sớm",
           "制止 ngăn chặn ↔ 允许 cho phép"],
    say=["Phần mở rộng của sách giới thiệu mười ba cặp từ trái nghĩa. Học từ theo cặp trái nghĩa giúp các bạn nhớ nhanh gấp đôi.",
         F(0, "动荡，稳定: bất ổn, rối ren, đối với ổn định. 服从，违抗: phục tùng, đối với chống lại mệnh lệnh."),
         F(1, "复活，灭亡: sống lại, phục sinh, đối với diệt vong. 高潮，低潮: cao trào, đối với thoái trào."),
         F(2, "高尚，低俗: cao thượng, đối với dung tục, thấp kém. 合并，解散: sáp nhập, đối với giải tán."),
         F(3, "混浊，清澈: nước đục, đối với trong vắt. 简陋，豪华: sơ sài, đơn sơ, đối với sang trọng, xa hoa."),
         F(4, "歌颂，批判: ca ngợi, đối với phê phán. 停滞，发展: đình trệ, đối với phát triển."),
         F(5, "推翻，建立: lật đổ, đối với thành lập. 延期，提前: hoãn lại, đối với đưa lên sớm hơn."),
         F(6, "Và cuối cùng, 制止，允许: ngăn chặn, đối với cho phép. Các bạn hãy thử đặt câu với từng cặp từ nhé.")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: điền từ trái nghĩa thích hợp", reveal=True, size=36,
    items=["(1) 这条小河的水原来很___，现在却变得混浊了。",
           "Đáp án: 清澈",
           "(2) 因为天气原因，比赛___了，改到下周举行。",
           "Đáp án: 延期 (trái nghĩa với 提前)",
           "(3) 他们住在一间___的小屋里，屋里只有一张床和一张桌子。",
           "Đáp án: 简陋 (trái nghĩa với 豪华)",
           "(4) 看到有人在公园里乱扔垃圾，他马上上前___。",
           "Đáp án: 制止 (trái nghĩa với 允许)"],
    say=[F(0, "Luyện tập: điền từ thích hợp trong các cặp trái nghĩa vừa học. Câu một: 这条小河的水原来很什么，现在却变得混浊了。 Nước con sông nhỏ này trước kia rất thế nào, bây giờ lại trở nên đục ngầu."),
         F(1, "Đáp án: 清澈. 这条小河的水原来很清澈。 Nước sông trước kia rất trong. 清澈 là từ trái nghĩa với 混浊."),
         F(2, "Câu hai: 因为天气原因，比赛什么了，改到下周举行。 Vì lý do thời tiết, trận đấu bị làm sao, chuyển sang tuần sau tổ chức."),
         F(3, "Đáp án: 延期. 比赛延期了。 Trận đấu bị hoãn lại. Trái nghĩa với nó là 提前, đưa lên sớm hơn."),
         F(4, "Câu ba: 他们住在一间什么的小屋里，屋里只有一张床和一张桌子。 Họ sống trong một căn nhà nhỏ thế nào đó, trong nhà chỉ có một cái giường và một cái bàn."),
         F(5, "Đáp án: 简陋. 一间简陋的小屋, một căn nhà nhỏ đơn sơ. Trái nghĩa là 豪华, sang trọng."),
         F(6, "Câu bốn: 看到有人在公园里乱扔垃圾，他马上上前什么。 Thấy có người vứt rác bừa bãi trong công viên, anh ấy lập tức tiến lên làm gì?"),
         F(7, "Đáp án: 制止. 他马上上前制止。 Anh ấy lập tức tiến lên ngăn lại. Trái nghĩa là 允许, cho phép.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ có dấu chấm", size=40,
    items=["更新 (更) → 更改 · 更换 · 更替 · 变更",
           "比喻 (比) → 比较 · 比赛 · 比方 · 对比",
           "昏迷 (昏) → 昏倒 · 黄昏 · 头昏 · 昏暗",
           "思索 (思) → 思考 · 思想 · 思念 · 构思",
           "崭新 (新) → 新鲜 · 新闻 · 重新 · 创新"],
    say=["Phần luyện tập. Bài tập một: mô phỏng ví dụ, viết thêm các từ có chứa chữ được đánh dấu chấm.",
         F(0, "Ví dụ mẫu: 更新, chữ được đánh dấu là chữ đầu, nghĩa là thay đổi, đọc thanh một. Ta có 更改，更换，更替，变更. Tức là sửa đổi, thay thế, thay phiên, và thay đổi."),
         F(1, "比喻, chữ được đánh dấu là chữ đầu, nghĩa là so sánh. Ta có 比较，比赛，比方，对比. Tức là so sánh, thi đấu, ví như, và đối chiếu."),
         F(2, "昏迷, chữ được đánh dấu là chữ đầu, Hán Việt là hôn, nghĩa là tối, mê man. Ta có 昏倒，黄昏，头昏，昏暗. Tức là ngất xỉu, hoàng hôn, chóng mặt, và tối tăm."),
         F(3, "思索, chữ được đánh dấu là chữ đầu, nghĩa là nghĩ. Ta có 思考，思想，思念，构思. Tức là suy nghĩ, tư tưởng, nhớ nhung, và lên ý tưởng."),
         F(4, "崭新, lần này chữ được đánh dấu là chữ thứ hai, nghĩa là mới. Ta có 新鲜，新闻，重新，创新. Tức là tươi mới, tin tức, làm lại từ đầu, và sáng tạo đổi mới.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Hoàn thành câu bằng từ cho sẵn (1)", reveal=True, size=36,
    items=["(1) 如果明天天气不好，……。（那么）",
           "Đáp án: ……那么我们就改天再去爬山。",
           "(2) 日韩同学觉得汉字没那么难，可……。（对……而言）",
           "Đáp án: ……可对欧美同学而言，汉字是最难的部分。",
           "(3) 同学们……。（各抒己见）",
           "Đáp án: 同学们对这个问题各抒己见，讨论得非常热烈。"],
    say=[F(0, "Bài tập hai: dùng từ hoặc cấu trúc cho sẵn để hoàn thành câu. Câu một, dùng 那么: 如果明天天气不好，…… Nếu ngày mai thời tiết không tốt, thì sao? Các bạn tạm dừng và thử viết nhé."),
         F(1, "Đáp án gợi ý: 如果明天天气不好，那么我们就改天再去爬山。 Nếu mai trời xấu, thì hôm khác chúng ta hãy đi leo núi. 如果……那么…… là cặp liên từ có trong bài khóa."),
         F(2, "Câu hai, dùng 对……而言: 日韩同学觉得汉字没那么难，可…… Các bạn học Nhật Bản và Hàn Quốc thấy chữ Hán không khó đến thế, nhưng mà sao?"),
         F(3, "Đáp án gợi ý: 可对欧美同学而言，汉字是最难的部分。 Nhưng đối với các bạn Âu Mỹ, chữ Hán là phần khó nhất."),
         F(4, "Câu ba, dùng 各抒己见: 同学们…… Các bạn học sinh làm gì?"),
         F(5, "Đáp án gợi ý: 同学们对这个问题各抒己见，讨论得非常热烈。 Các bạn học sinh mỗi người nêu một ý kiến về vấn đề này, thảo luận vô cùng sôi nổi.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Hoàn thành câu bằng từ cho sẵn (2)", reveal=True, size=36,
    items=["(4) 经过一段时间的观察，……。（确信）",
           "Đáp án: ……我确信这种新药对治疗感冒很有效。",
           "(5) 如果环境继续恶化，专家们……。（推测）",
           "Đáp án: ……专家们推测，几十年后很多动物将会灭绝。",
           "(6) 青藏高原海拔很高，氧气稀薄，环境……。（极端）",
           "Đáp án: ……环境极端恶劣，不适合人类长期居住。"],
    say=[F(0, "Câu bốn, dùng 确信: 经过一段时间的观察，…… Sau một thời gian quan sát, thì sao?"),
         F(1, "Đáp án gợi ý: 经过一段时间的观察，我确信这种新药对治疗感冒很有效。 Sau một thời gian quan sát, tôi tin chắc loại thuốc mới này rất hiệu quả trong việc chữa cảm cúm."),
         F(2, "Câu năm, dùng 推测: 如果环境继续恶化，专家们…… Nếu môi trường tiếp tục xấu đi, các chuyên gia thì sao?"),
         F(3, "Đáp án gợi ý: 专家们推测，几十年后很多动物将会灭绝。 Các chuyên gia suy đoán rằng, vài chục năm nữa rất nhiều loài động vật sẽ tuyệt chủng."),
         F(4, "Câu sáu, dùng 极端: 青藏高原海拔很高，氧气稀薄，环境…… Cao nguyên Thanh Tạng có độ cao so với mặt biển rất lớn, không khí loãng, môi trường thì sao?"),
         F(5, "Đáp án gợi ý: 环境极端恶劣，不适合人类长期居住。 Môi trường cực kỳ khắc nghiệt, không thích hợp cho con người sống lâu dài. Ở đây 极端 là phó từ, bổ nghĩa cho từ mang nghĩa xấu 恶劣.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (1)", reveal=True, size=34,
    items=["## Từ cho sẵn: 各抒己见 · 见解 · 无忧无虑 · 思索 · 比喻",
           "今天讨论课的话题是“幸福是什么？”同学们经过一番___后纷纷___。有人说：“幸福就是___地过日子。”有人把幸福___为盛开的花儿，虽然美好，却很短暂；也有人认为幸福是以物质为基础的。可以说，以上这些___其实代表了每个人不同的价值观和人生观。",
           "Đáp án: 思索 · 各抒己见 · 无忧无虑 · 比喻 · 见解"],
    say=[F(0, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn một có năm từ: 各抒己见，见解，无忧无虑，思索，比喻."),
         F(1, "今天讨论课的话题是幸福是什么。同学们经过一番什么后纷纷什么。有人说，幸福就是什么地过日子。有人把幸福什么为盛开的花儿，虽然美好，却很短暂；也有人认为幸福是以物质为基础的。可以说，以上这些什么其实代表了每个人不同的价值观和人生观。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 经过一番思索后纷纷各抒己见，幸福就是无忧无虑地过日子，有人把幸福比喻为盛开的花儿，以上这些见解。 Chủ đề giờ thảo luận hôm nay là hạnh phúc là gì. Sau một hồi suy nghĩ, các bạn lần lượt nêu ý kiến. Có người nói hạnh phúc là sống vô tư lự. Có người ví hạnh phúc như bông hoa nở rộ, đẹp nhưng ngắn ngủi. Những cách nhìn này thể hiện giá trị quan và nhân sinh quan khác nhau của mỗi người.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (2)", reveal=True, size=34,
    items=["## Từ cho sẵn: 忧郁 · 遥远 · 呈现 · 譬如 · 器官",
           "现代社会，人们的压力越来越大，精神类疾病日益增多。这类疾病会___出不同的状态，___，有的人因为过于___而吃药；有的人怀疑身边的人或事；还有的人出现幻觉……这类疾病离我们并不___，所以我们应该像关注身体___上的疾病一样去关注心理问题。",
           "Đáp án: 呈现 · 譬如 · 忧郁 · 遥远 · 器官"],
    say=[F(0, "Đoạn hai có năm từ: 忧郁，遥远，呈现，譬如，器官."),
         F(1, "现代社会，人们的压力越来越大，精神类疾病日益增多。这类疾病会什么出不同的状态，什么，有的人因为过于什么而吃药；有的人怀疑身边的人或事；还有的人出现幻觉。这类疾病离我们并不什么，所以我们应该像关注身体什么上的疾病一样去关注心理问题。 Các bạn điền thử nhé."),
         F(2, "Đáp án: 会呈现出不同的状态，譬如，有的人因为过于忧郁而吃药，离我们并不遥远，像关注身体器官上的疾病一样。 Xã hội hiện đại, áp lực ngày càng lớn, bệnh tâm thần ngày càng nhiều. Những bệnh này thể hiện ra nhiều trạng thái khác nhau, ví dụ có người vì quá u uất mà phải uống thuốc, có người nghi ngờ người và việc xung quanh, có người bị ảo giác. Những bệnh này không hề xa vời, nên chúng ta cần quan tâm đến sức khỏe tâm lý như quan tâm đến bệnh của các cơ quan trong cơ thể."),
         "Các bạn để ý: câu 因为过于忧郁而吃药 lấy nguyên từ bài khóa. Khi làm bài điền từ, hãy nhớ lại những cụm từ đã gặp trong bài, đó là manh mối rất tốt."])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 8", size=34,
    items=["Từ vựng trọng tâm: 翻天覆地 · 确信 · 比喻 · 呈现 · 阐述 · 陈述 · 演变 · 各抒己见 · 触犯 · 极端 · 空前绝后 · 无忧无虑 · 崭新",
           "Ngữ pháp: 对……而言 (đối với… mà nói) · 有关 (có liên quan; về) · 不瞒你说 (nói thật với bạn)",
           "Phân biệt: 极端 (nghĩa xấu; danh từ; tính từ) ≠ 极度 (chủ yếu là phó từ chỉ mức độ)",
           "Kỹ năng: sắp xếp câu – câu mở đầu, từ nối, đại từ, thời gian · Mở rộng: 13 cặp từ trái nghĩa",
           "## Bài tập về nhà (运用)",
           "Dựa vào bài tập 5, viết tóm tắt bài khóa thành đoạn văn khoảng 300 chữ"],
    say=["Chúng ta cùng tổng kết bài tám.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 翻天覆地，确信，比喻，呈现，阐述，陈述，演变，各抒己见，触犯，极端，空前绝后，无忧无虑，崭新. Và đừng quên những từ dễ nhầm như 比喻，触犯，器官，设想."),
         F(1, "Về ngữ pháp: 对……而言 nghĩa là đối với… mà nói, dùng trong văn viết. 有关 vừa là động từ, nghĩa là có liên quan, vừa là giới từ, nghĩa là về, liên quan đến. 不瞒你说 là xen ngữ, nghĩa là nói thật với bạn."),
         F(2, "Về phân biệt từ: 极端 thường đi với từ mang nghĩa xấu, còn làm được danh từ và tính từ; 极度 chủ yếu là phó từ chỉ mức độ, bổ nghĩa được cả từ mang nghĩa tốt."),
         F(3, "Về kỹ năng: khi sắp xếp câu thành đoạn, hãy tìm câu mở đầu, rồi dựa vào từ nối, đại từ, và trình tự thời gian. Phần mở rộng có mười ba cặp từ trái nghĩa."),
         F(5, "Bài tập về nhà, theo phần vận dụng của sách: 今天的你跟昨天的你是同一个人吗？ Đây là một câu hỏi triết học về bản thể. Các bạn hãy dựa vào bài tập năm, viết tóm tắt bài khóa thành một đoạn văn khoảng ba trăm chữ. Nhớ thử dùng 对……而言，有关，不瞒你说 trong bài viết nhé."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Đến đây, chúng ta đã hoàn thành Chủ đề hai, 不甘平庸, Không cam chịu tầm thường. Bài sau, chúng ta bước sang Chủ đề ba, 多彩社会, Xã hội nhiều màu sắc, với bài chín: 不用手机的日子, Một ngày không sử dụng điện thoại di động. Các bạn thử tưởng tượng xem, một ngày không có điện thoại sẽ như thế nào nhé. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Thượng) – Bài 8: 遇见原来的我 (Gặp lại tôi của ngày xưa)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"更新": "耕新",            # gēngxīn
                    "更改": "耕改",            # gēnggǎi
                    "更换": "耕换",            # gēnghuàn
                    "更替": "耕替",            # gēngtì
                    "变更": "变耕",            # biàngēng
                    "更为": "更维",            # gèngwéi
                    "比喻为": "比喻维",        # wéi
                    "阐述为": "阐述维",        # wéi
                    "稍为": "稍维",            # shāowéi
                    "分为二": "分维二",        # yì fēn wéi èr
                    "为当初": "位当初",        # wèi
                    "跌倒": "跌岛",            # diēdǎo
                    "昏倒": "昏岛",            # hūndǎo
                    "高处": "高触",            # gāochù
                    "变种": "变肿",            # biànzhǒng
                    "重新": "虫新",            # chóngxīn
                    "稀薄": "稀博",            # xībó
                    "青藏": "青葬",            # Qīng-Zàng
                    "记载": "记宰",            # jìzǎi
                    "称不上": "撑不上",        # chēng bu shàng
                    "什么为盛开": "什么维盛开",  # wéi
                    "为基础": "维基础",        # wéi
                    "兴奋": "星奋",            # xīngfèn
                    "幻觉": "幻决",            # huànjué
                    "酒吧": "酒巴",            # jiǔbā
                    "水吧": "水巴",            # shuǐbā
                    "咖啡吧": "咖啡巴",        # kāfēibā
                    "茶吧": "茶巴",            # chábā
                    "果吧": "果巴"},           # xiānguǒbā
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai08.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
