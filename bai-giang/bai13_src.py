#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Thượng) – Bài 13 «从旅游指南看世事变迁». Chạy để sinh bai13.json."""
import json
import os

TAG = "HSK 6 (Thượng) · Bài 13 · 从旅游指南看世事变迁"
slides = []


def add(type_, chapter=None, section="", **kw):
    s = {"type": type_, "section": section, **kw}
    if chapter:
        s["chapter"] = chapter
    slides.append(s)


def F(i, t, **kw):
    return {"t": t, "f": i, **kw}


# ======================= MỞ ĐẦU =======================
# Tên bài có 9 chữ, vừa một dòng chữ cỡ lớn nên giữ nguyên.
add("title", chapter="Mở đầu",
    top="Giáo trình chuẩn HSK 6 – Quyển Thượng",
    zh="从旅游指南看世事变迁", py="Cóng lǚyóu zhǐnán kàn shìshì biànqiān",
    vi="Bài 13: Thế sự đổi thay qua cẩm nang du lịch",
    sub="Nhìn thế sự đổi thay qua trang sách cẩm nang du lịch\nBài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Thượng.",
         "Hôm nay chúng ta học bài mười ba: 从旅游指南看世事变迁。 Nghĩa là: Nhìn thế sự đổi thay qua trang sách cẩm nang du lịch.",
         "Đây là bài mở đầu của Chủ đề bốn, 走遍天下, Đi khắp thế giới. Bài khóa kể lại lịch sử du lịch của loài người, từ những cuộc di cư để sống còn thời xa xưa, cho đến chuyện du lịch tự túc ngày nay. Song song với đó là câu chuyện về những cuốn cẩm nang du lịch của Trung Quốc: từ chỗ không có cuốn nào, đến những cuốn sách bỏ túi, rồi các trang web và hệ thống định vị vệ tinh.",
         "Qua một cuốn sách nhỏ, chúng ta thấy được cả một thời cuộc đổi thay. Các bạn có hay dùng cẩm nang du lịch không? Hãy vừa học vừa nghĩ xem nhé."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài khóa: mục đích du lịch thay đổi ra sao, và cẩm nang du lịch Trung Quốc phát triển thế nào",
           "Nắm vững 51 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: động từ 便于, động từ 犹如, cấu trúc 和……相比",
           "Phân biệt hai phó từ 一向 và 一度",
           "Mở rộng: câu sai về logic (逻辑不通) và từ vựng giao thông, nông nghiệp"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa: mục đích đi lại của con người đã thay đổi như thế nào qua các thời kỳ, và cẩm nang du lịch của Trung Quốc đã phát triển ra sao."),
         F(1, "Thứ hai, nắm vững năm mươi mốt từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học ba điểm ngữ pháp: động từ 便于, nghĩa là tiện cho, dễ làm gì; động từ 犹如, nghĩa là giống như; và cấu trúc so sánh 和……相比, nghĩa là so với."),
         F(3, "Thứ tư, phân biệt hai phó từ chỉ thời gian rất dễ nhầm: 一向 và 一度."),
         F(4, "Thứ năm, phần mở rộng: nhận biết câu sai về logic, tiếng Trung gọi là 逻辑不通, và làm quen với một số từ vựng về giao thông và nông nghiệp."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Câu hỏi khởi động: Cẩm nang du lịch có những gì?", reveal=True, size=38,
    items=["旅游指南包括哪些内容？请选择填空。 – Cẩm nang du lịch gồm những nội dung gì?",
           "名胜古迹 danh lam cổ tích · 地理环境 môi trường địa lý · 人文特色 nét văn hóa đặc sắc",
           "酒店住宿 khách sạn, chỗ ở · 特色饮食 ẩm thực đặc sắc · 交通路线 tuyến đường giao thông",
           "Ảnh: (1) hồ nước, núi đồi · (2) phòng khách sạn · (3) Vạn Lý Trường Thành",
           "Ảnh: (4) đội nhạc diễu hành · (5) bản đồ và ô tô · (6) bánh nướng",
           "Đáp án: (1) 地理环境 (2) 酒店住宿 (3) 名胜古迹 (4) 人文特色 (5) 交通路线 (6) 特色饮食"],
    say=["Chúng ta bắt đầu bằng phần khởi động. Bài hôm nay nói về cẩm nang du lịch, vậy trước hết hãy xem một cuốn cẩm nang thường có những gì.",
         F(0, "旅游指南包括哪些内容？请选择填空。 Cẩm nang du lịch gồm những nội dung gì? Hãy chọn từ để điền vào dưới mỗi bức ảnh."),
         F(1, "Sách cho sáu cụm từ. 名胜古迹, danh lam thắng cảnh và di tích cổ. 地理环境, môi trường địa lý. 人文特色, nét đặc sắc về văn hóa, con người."),
         F(2, "酒店住宿, khách sạn và chỗ nghỉ. 特色饮食, ẩm thực đặc sắc. 交通路线, tuyến đường giao thông. Hai từ 人文 và 饮食 lát nữa sẽ gặp lại trong bài khóa."),
         F(3, "Sáu bức ảnh trong sách như sau. Ảnh một là một hồ nước bên núi đồi. Ảnh hai là một phòng khách sạn. Ảnh ba là Vạn Lý Trường Thành."),
         F(4, "Ảnh bốn là một đội nhạc mặc trang phục truyền thống đang diễu hành. Ảnh năm là tấm bản đồ với hai chiếc ô tô đồ chơi. Ảnh sáu là những chiếc bánh nướng đặc sản. Các bạn tạm dừng video và tự ghép nhé."),
         F(5, "Đáp án: ảnh một là 地理环境, ảnh hai là 酒店住宿, ảnh ba là 名胜古迹, ảnh bốn là 人文特色, ảnh năm là 交通路线, và ảnh sáu là 特色饮食. Một cuốn cẩm nang tốt thường có đủ cả sáu nội dung này.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 初 và 居", size=38,
    items=["## 初 (sơ): ban đầu, lần đầu",
           "起初 lúc đầu · 最初 ban đầu nhất · 当初 hồi đó · 年初 đầu năm · 月初 đầu tháng · 初步 bước đầu",
           "初春 đầu xuân · 初夏 đầu hè · 初学 mới học · 初恋 mối tình đầu · 初创 mới thành lập",
           "## 居 (cư): ở, sinh sống",
           "居住 cư trú · 居民 cư dân · 居留 cư trú, lưu trú · 居家 ở nhà · 安居 an cư",
           "邻居 hàng xóm · 定居 định cư · 同居 sống chung · 分居 ly thân · 群居 sống thành bầy"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo, rất có lợi cho người Việt vì hầu hết các chữ đều có âm Hán Việt quen thuộc.",
         F(0, "Nhóm thứ nhất có chữ 初, Hán Việt là sơ, như trong sơ khai, sơ cấp; nghĩa là ban đầu, lần đầu."),
         F(1, "起初，最初，当初，年初，月初，初步。 Tức là: lúc đầu, ban đầu nhất, hồi đó, đầu năm, đầu tháng, bước đầu. Từ 起初 là từ mới của bài, mở đầu đoạn thứ hai của bài khóa."),
         F(2, "初春，初夏，初学，初恋，初创。 Tức là: đầu xuân, đầu hè, mới học, mối tình đầu, và mới thành lập."),
         F(3, "Nhóm thứ hai có chữ 居, Hán Việt là cư, như trong cư dân, định cư; nghĩa là ở, sinh sống."),
         F(4, "居住，居民，居留，居家，安居。 Tức là: cư trú, cư dân, lưu trú, ở nhà, và an cư. Bài khóa có câu 寻找能够安居的地方, tìm nơi có thể an cư."),
         F(5, "邻居，定居，同居，分居，群居。 Tức là: hàng xóm, định cư, sống chung, ly thân, và sống thành bầy đàn.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 类 và 世", size=38,
    items=["## 类 (loại): loại, nhóm",
           "类别 loại · 类型 loại hình · 种类 chủng loại · 分类 phân loại · 门类 ngành loại · 同类 cùng loại",
           "人类 loài người · 鸟类 loài chim · 肉类 các loại thịt · 鱼类 loài cá · 指南类 loại sách hướng dẫn · 旅游类 loại du lịch",
           "## 世 (thế): đời, thế gian",
           "问世 ra đời · 去世 qua đời · 人世 cõi đời · 世界 thế giới · 世道 thế đạo · 世事 thế sự · 世上 trên đời · 世态 thế thái",
           "举世瞩目 cả thế giới chú ý · 与世无争 không tranh giành với đời · 人情世故 sự đời, cách đối nhân xử thế"],
    say=[F(0, "Nhóm thứ ba có chữ 类, Hán Việt là loại, nghĩa là loại, nhóm."),
         F(1, "类别，类型，种类，分类，门类，同类。 Tức là: loại, loại hình, chủng loại, phân loại, ngành loại, và cùng loại."),
         F(2, "人类，鸟类，肉类，鱼类，指南类，旅游类。 Tức là: loài người, loài chim, các loại thịt, loài cá, loại sách hướng dẫn, và loại sách du lịch. Bài khóa có cụm 旅游指南类的书籍, sách thuộc loại cẩm nang du lịch."),
         F(3, "Nhóm cuối cùng có chữ 世, Hán Việt là thế, như trong thế giới, thế sự; nghĩa là đời, thế gian."),
         F(4, "问世，去世，人世，世界，世道，世事，世上，世态。 Tức là: ra đời, qua đời, cõi đời, thế giới, thế đạo, thế sự, trên đời, và thế thái. Tên bài có từ 世事, thế sự, tức là những việc đời."),
         F(5, "举世瞩目，与世无争，人情世故。 Tức là: được cả thế giới chú ý, sống không tranh giành với đời, và sự đời, cách đối nhân xử thế."),
         "Các bạn thấy không, chỉ cần nắm nghĩa của một chữ gốc, ta có thể đoán được nghĩa của cả một nhóm từ. Hãy áp dụng cách này khi học từ mới nhé."])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng)
V = [
    ("变迁", "biànqiān", "biến thiên", "động từ", "biến đổi, đổi thay (theo thời gian)", "几十年过去了，这座城市发生了很大的变迁。", "Mấy chục năm trôi qua, thành phố này đã đổi thay rất nhiều.",
     "Động từ, cũng dùng như danh từ, chỉ sự thay đổi lớn của sự vật, xã hội qua một thời gian dài. Tên bài 世事变迁 nghĩa là thế sự đổi thay. Chú ý: trong tiếng Việt, biến thiên hay dùng trong toán học, vật lý; còn 变迁 nói về những đổi thay của thời cuộc, như 社会变迁，时代变迁."),
    ("一向", "yíxiàng", "nhất hướng", "phó từ", "từ trước đến nay, xưa nay", "他一向很守时，今天怎么迟到了？", "Anh ấy xưa nay rất đúng giờ, sao hôm nay lại đến muộn?",
     "Phó từ, nghĩa là từ trước đến nay vẫn luôn như vậy. Cẩn thận, không hiểu theo mặt chữ là một hướng. Lát nữa chúng ta sẽ phân biệt kỹ 一向 với 一度."),
    ("起初", "qǐchū", "khởi sơ", "danh từ", "ban đầu, lúc đầu", "起初大家都不同意，后来才慢慢接受了他的想法。", "Lúc đầu mọi người đều không đồng ý, về sau mới dần chấp nhận ý kiến của anh ấy.",
     "Danh từ chỉ thời gian, nghĩa là lúc đầu, ban đầu. Thường đứng đầu câu, phía sau hay có 后来 để đối lập, đúng như bài khóa: 起初 rồi đến 后来."),
    ("迁徙", "qiānxǐ", "thiên tỉ", "động từ", "di chuyển, dời đi nơi khác, di cư", "每年冬天，很多候鸟都要迁徙到南方。", "Mỗi mùa đông, rất nhiều loài chim di cư bay về phương Nam.",
     "Động từ, nghĩa là dời chỗ ở, di cư; thường nói về một nhóm người hay động vật di chuyển đi xa. Tiếng Việt có từ thiên di, cùng chữ 迁. Trong bài, tác giả nói những chuyến đi đầu tiên của loài người thực ra là 迁徙."),
    ("侵犯", "qīnfàn", "xâm phạm", "động từ", "xâm phạm, xâm lược", "任何人都不能侵犯别人的合法权利。", "Không ai được xâm phạm quyền lợi hợp pháp của người khác.",
     "Động từ, nghĩa là xâm phạm, xâm lấn. Dùng cho lãnh thổ, cũng dùng cho quyền lợi, đời tư: 侵犯隐私，侵犯权利. Âm Hán Việt và nghĩa giống tiếng Việt."),
    ("居住", "jūzhù", "cư trú", "động từ", "cư trú, sinh sống, ở", "他们一家在这个小镇居住了二十多年。", "Gia đình họ đã sống ở thị trấn nhỏ này hơn hai mươi năm.",
     "Động từ, nghĩa là ở, sinh sống lâu dài tại một nơi; trang trọng hơn từ 住. Trong bài có cụm 居住地, nơi cư trú."),
    ("纯粹", "chúncuì", "thuần túy", "phó từ", "đơn thuần, chỉ là, hoàn toàn", "我这么说纯粹是为了你好。", "Tôi nói vậy hoàn toàn là vì muốn tốt cho bạn.",
     "Trong bài là phó từ, nghĩa là đơn thuần, hoàn toàn, chỉ là. 纯粹 còn là tính từ, nghĩa là thuần khiết, không pha tạp. Âm Hán Việt thuần túy, rất dễ nhớ."),
    ("生存", "shēngcún", "sinh tồn", "động từ", "sinh tồn, sống còn", "水是人类生存不可缺少的条件。", "Nước là điều kiện không thể thiếu cho sự sống còn của loài người.",
     "Động từ, nghĩa là sống còn, tồn tại. Trong bài, 生存和安全的需要 là nhu cầu sống còn và an toàn."),
    ("指南针", "zhǐnánzhēn", "chỉ nam châm", "danh từ", "la bàn, kim chỉ nam", "指南针是中国古代四大发明之一。", "La bàn là một trong bốn phát minh lớn của Trung Quốc cổ đại.",
     "Danh từ, nghĩa là la bàn. 指南 là chỉ về phía nam, 针 là cây kim. Chú ý: trong tiếng Việt, kim chỉ nam còn có nghĩa bóng là phương châm hành động; còn 指南 trong tiếng Trung hay dùng để chỉ sách hướng dẫn, như 旅游指南, cẩm nang du lịch, chính là tên bài hôm nay."),
    ("若干", "ruògān", "nhược can", "đại từ", "một số, một vài (số lượng không xác định)", "这个问题可以分成若干个小问题。", "Vấn đề này có thể chia thành một số vấn đề nhỏ.",
     "Đại từ, chỉ một số lượng không xác định, nghĩa là một số, một vài; mang màu sắc văn viết. Trong bài, 若干年来 là bao năm nay. Âm tiết thứ hai đọc thanh một."),
    ("遍布", "biànbù", "biến bố", "động từ", "phân bố khắp nơi, rải khắp", "这家公司的分店遍布全国。", "Chi nhánh của công ty này có mặt khắp cả nước.",
     "Động từ, nghĩa là có mặt ở khắp nơi. 遍 là khắp, 布 là phân bố. Trong bài, 足迹遍布世界 là dấu chân in khắp thế giới."),
    ("千方百计", "qiānfāng-bǎijì", "thiên phương bách kế", "thành ngữ", "trăm phương nghìn kế, tìm đủ mọi cách", "父母千方百计地为孩子创造好的学习条件。", "Cha mẹ tìm đủ mọi cách để tạo điều kiện học tập tốt cho con.",
     "Thành ngữ, tương đương trăm phương nghìn kế trong tiếng Việt, nghĩa là tìm đủ mọi cách để đạt mục đích. Thường làm trạng ngữ: 千方百计地 cộng động từ."),
    ("书籍", "shūjí", "thư tịch", "danh từ", "sách vở (nói chung)", "图书馆里有各种各样的书籍。", "Trong thư viện có đủ loại sách.",
     "Danh từ, chỉ sách vở nói chung, mang màu sắc văn viết. Trong bài có cụm 旅游指南类的书籍, sách thuộc loại cẩm nang du lịch."),
    ("问世", "wènshì", "vấn thế", "động từ", "ra đời, ra mắt, được xuất bản", "他的第一部小说去年问世了。", "Cuốn tiểu thuyết đầu tay của anh ấy ra mắt năm ngoái.",
     "Động từ, nghĩa là ra mắt công chúng, dùng cho tác phẩm, sách, sản phẩm mới, phát minh. Chữ 问 ở đây không phải là hỏi; cả từ nghĩa là xuất hiện trên đời. Từ này không mang tân ngữ."),
    ("携带", "xiédài", "huề đới", "động từ", "mang theo", "乘客不能携带危险物品上飞机。", "Hành khách không được mang theo vật phẩm nguy hiểm lên máy bay.",
     "Động từ, nghĩa là mang theo bên mình, trang trọng hơn 带. Hay gặp trên biển báo, quy định: 随身携带, mang theo người. Trong bài, 携带方便 là tiện mang theo."),
    ("序言", "xùyán", "tự ngôn", "danh từ", "lời tựa, lời nói đầu", "这本书的序言是一位著名作家写的。", "Lời tựa của cuốn sách này do một nhà văn nổi tiếng viết.",
     "Danh từ, nghĩa là lời tựa, lời nói đầu của một cuốn sách. Chữ 序 chính là chữ tựa trong lời tựa của tiếng Việt."),
    ("繁华", "fánhuá", "phồn hoa", "tính từ", "phồn hoa, sầm uất, phồn thịnh", "这条街是城里最繁华的商业街。", "Con phố này là phố thương mại sầm uất nhất thành phố.",
     "Tính từ, nghĩa là sầm uất, nhộn nhịp, thường nói về thành phố, đường phố. Trong bài, 天津异常繁华 là Thiên Tân vô cùng sầm uất."),
    ("便于", "biànyú", "tiện vu", "động từ", "tiện cho, dễ (làm gì)", "这种包很轻，便于携带。", "Loại túi này rất nhẹ, tiện mang theo.",
     "Động từ, nghĩa là thuận tiện cho việc gì, dễ làm việc gì; phía sau thường là động từ. Đây là điểm ngữ pháp thứ nhất của bài."),
    ("习俗", "xísú", "tập tục", "danh từ", "phong tục, tập tục", "每个民族都有自己独特的习俗。", "Mỗi dân tộc đều có phong tục riêng của mình.",
     "Danh từ, nghĩa là phong tục tập quán. Hán Việt là tập tục, giống hệt tiếng Việt."),
    ("码头", "mǎtóu", "mã đầu", "danh từ", "bến tàu, bến cảng", "我们在码头等了半个小时，船才来。", "Chúng tôi đợi ở bến tàu nửa tiếng thì thuyền mới tới.",
     "Danh từ, nghĩa là bến tàu, bến cảng, nơi tàu thuyền neo đậu, đón trả khách và hàng hóa. Trong khẩu ngữ, âm tiết thứ hai thường đọc nhẹ. Trong bài, 车船码头 là bến xe, bến tàu."),
    ("简要", "jiǎnyào", "giản yếu", "tính từ", "ngắn gọn, vắn tắt", "请你简要地介绍一下你的工作经历。", "Mời anh giới thiệu ngắn gọn kinh nghiệm làm việc của mình.",
     "Tính từ, nghĩa là ngắn gọn mà nêu được ý chính. Hay gặp: 简要介绍，简要说明. Tiếng Việt có từ giản yếu, cùng nghĩa."),
    ("一度", "yídù", "nhất độ", "phó từ", "đã có một thời, có một dạo", "他一度想出国留学，后来改变了主意。", "Anh ấy từng có lúc muốn đi du học, về sau thì đổi ý.",
     "Phó từ, nghĩa là trong quá khứ đã từng có một thời gian như vậy. Cẩn thận, không hiểu là một độ như nhiệt độ. 一度 còn là số lượng từ, nghĩa là một lần, như 一年一度, mỗi năm một lần."),
    ("轰动", "hōngdòng", "oanh động", "động từ", "gây chấn động, làm xôn xao", "这部电影一上映就轰动了全国。", "Bộ phim này vừa công chiếu đã gây chấn động cả nước.",
     "Động từ, nghĩa là gây chấn động, làm cả một vùng xôn xao bàn tán. Hay gặp: 引起轰动, gây xôn xao. Chữ 轰 là tiếng nổ ầm, nên 轰动 giống như một tiếng nổ khiến ai cũng chú ý."),
    ("趣味", "qùwèi", "thú vị", "danh từ", "sự thú vị, hứng thú", "这本书既有知识性，又有趣味性。", "Cuốn sách này vừa có tính kiến thức, vừa có tính thú vị.",
     "Danh từ, nghĩa là sự thú vị, sức hấp dẫn; cũng chỉ sở thích, gu. Cẩn thận: tiếng Việt thú vị là tính từ, như cuốn sách rất thú vị; còn 趣味 là danh từ, nên phải nói 有趣味，趣味性强, hoặc dùng tính từ 有趣."),
    ("人士", "rénshì", "nhân sĩ", "danh từ", "nhân sĩ, người (thuộc một giới nào đó)", "各界人士都参加了这次会议。", "Đại diện các giới đều tham dự hội nghị lần này.",
     "Danh từ, chỉ những người thuộc một giới, một lĩnh vực nào đó, sắc thái trang trọng: 各界人士，专业人士，中外人士. Chú ý: tiếng Việt nhân sĩ thường chỉ trí thức có danh vọng; còn 人士 dùng rộng hơn, như 专业人士 là người làm chuyên môn."),
    ("版本", "bǎnběn", "bản bản", "danh từ", "phiên bản", "这本小说有中文和英文两个版本。", "Cuốn tiểu thuyết này có hai phiên bản tiếng Trung và tiếng Anh.",
     "Danh từ, nghĩa là phiên bản, ấn bản của sách, phần mềm, bộ phim. Ví dụ 最新版本, phiên bản mới nhất."),
    ("发行", "fāxíng", "phát hành", "động từ", "phát hành", "这套邮票将于下个月发行。", "Bộ tem này sẽ được phát hành vào tháng sau.",
     "Động từ, nghĩa là phát hành sách báo, tem, tiền, phim, đĩa nhạc. Âm Hán Việt và nghĩa giống tiếng Việt. Âm tiết thứ hai đọc thanh hai, giống trong từ 旅行."),
    ("事业", "shìyè", "sự nghiệp", "danh từ", "sự nghiệp; công cuộc, lĩnh vực hoạt động", "他把一生都献给了教育事业。", "Ông ấy đã cống hiến cả đời cho sự nghiệp giáo dục.",
     "Danh từ, nghĩa là sự nghiệp của một người, hoặc công cuộc, lĩnh vực hoạt động có ảnh hưởng đến xã hội: 教育事业，外交事业. Trong bài, 外交事业 là công tác ngoại giao."),
    ("延伸", "yánshēn", "diên thân", "động từ", "kéo dài, mở rộng", "这条公路一直延伸到海边。", "Con đường này kéo dài mãi đến tận bờ biển.",
     "Động từ, nghĩa là kéo dài, vươn ra xa; nghĩa bóng là mở rộng phạm vi. Trong bài, 外交事业的延伸和补充 là sự nối dài và bổ sung cho công tác ngoại giao."),
    ("产业", "chǎnyè", "sản nghiệp", "danh từ", "ngành kinh tế, ngành sản xuất", "旅游业已经成为这个地区的重要产业。", "Du lịch đã trở thành ngành kinh tế quan trọng của vùng này.",
     "Danh từ. Cẩn thận: tiếng Việt sản nghiệp thường là của cải, tài sản; còn 产业 trong tiếng Trung hiện đại chủ yếu chỉ ngành kinh tế, ngành sản xuất: 文化产业，旅游产业."),
    ("振兴", "zhènxīng", "chấn hưng", "động từ", "làm hưng thịnh, chấn hưng", "发展旅游业可以振兴当地经济。", "Phát triển du lịch có thể chấn hưng kinh tế địa phương.",
     "Động từ, nghĩa là làm cho phát triển, hưng thịnh; dùng cho kinh tế, ngành nghề, quốc gia. Âm tiết thứ hai đọc thanh một. Tiếng Việt chấn hưng cùng nghĩa."),
    ("主流", "zhǔliú", "chủ lưu", "danh từ", "xu hướng chính, bộ phận chủ yếu", "网上购物已经成为年轻人消费的主流。", "Mua sắm trên mạng đã trở thành xu hướng tiêu dùng chính của giới trẻ.",
     "Danh từ, nghĩa gốc là dòng chính của một con sông; nghĩa bóng là xu hướng chính, bộ phận chiếm đa số. Trái nghĩa là 支流, dòng nhánh."),
    ("犹如", "yóurú", "do như", "động từ", "giống như, như là", "这里的风景犹如一幅美丽的画。", "Phong cảnh nơi đây giống như một bức tranh tuyệt đẹp.",
     "Động từ, nghĩa là giống như, tựa như, dùng trong văn viết. Đây là điểm ngữ pháp thứ hai của bài."),
    ("宗旨", "zōngzhǐ", "tôn chỉ", "danh từ", "tôn chỉ, mục đích", "我们的宗旨是一切为了顾客。", "Tôn chỉ của chúng tôi là tất cả vì khách hàng.",
     "Danh từ, nghĩa là mục đích, ý định chủ yếu của một tổ chức hay một hoạt động. Hay gặp: 服务宗旨，办学宗旨. Hán Việt của chữ đầu vốn là tông, nhưng tiếng Việt quen nói tôn chỉ."),
    ("栏目", "lánmù", "lan mục", "danh từ", "chuyên mục (báo, tạp chí, truyền hình…)", "这是我最喜欢的电视栏目。", "Đây là chuyên mục truyền hình mà tôi thích nhất.",
     "Danh từ, chỉ chuyên mục trên báo, tạp chí, đài truyền hình, trang web. Trong bài, 增加了相关栏目 là thêm các chuyên mục liên quan."),
    ("人性", "rénxìng", "nhân tính", "danh từ", "nhân tính, bản chất con người", "这家酒店的服务非常人性化。", "Dịch vụ của khách sạn này rất chu đáo, thân thiện với khách.",
     "Danh từ, nghĩa là nhân tính, bản tính con người. Đặc biệt hay gặp từ 人性化, nghĩa là lấy con người làm trung tâm, chu đáo, tiện lợi cho người dùng. Đừng dịch máy móc là nhân tính hóa."),
    ("偏僻", "piānpì", "thiên tích", "tính từ", "xa xôi, hẻo lánh", "他出生在一个偏僻的小山村。", "Anh ấy sinh ra ở một bản làng nhỏ hẻo lánh trên núi.",
     "Tính từ, nghĩa là xa xôi hẻo lánh, ít người qua lại, giao thông không tiện. Trong bài, 偏僻省份 là những tỉnh xa xôi."),
    ("沿海", "yánhǎi", "duyên hải", "danh từ", "vùng duyên hải, ven biển", "中国东部沿海地区经济比较发达。", "Vùng duyên hải phía đông Trung Quốc kinh tế khá phát triển.",
     "Danh từ, chỉ vùng ven biển. Chữ 沿 Hán Việt là duyên, nghĩa là men theo. Duyên hải miền Trung trong tiếng Việt chính là từ này."),
    ("风土人情", "fēngtǔ rénqíng", "phong thổ nhân tình", "thành ngữ", "phong thổ và phong tục, tập quán của một vùng", "旅行可以让我们了解各地的风土人情。", "Du lịch giúp chúng ta hiểu phong thổ, phong tục của mỗi vùng.",
     "Thành ngữ, chỉ điều kiện tự nhiên như khí hậu, sản vật, cùng với phong tục tập quán, lễ nghĩa của một địa phương. Rất hay dùng khi nói về du lịch."),
    ("宗教", "zōngjiào", "tôn giáo", "danh từ", "tôn giáo", "这个国家的人民有宗教信仰自由。", "Nhân dân nước này có quyền tự do tín ngưỡng tôn giáo.",
     "Danh từ, nghĩa là tôn giáo. Âm tiết thứ hai đọc thanh bốn. Giống từ 宗旨, chữ đầu vốn đọc tông, nhưng tiếng Việt quen nói tôn giáo."),
    ("考古", "kǎogǔ", "khảo cổ", "danh từ", "khảo cổ, khảo cổ học", "这次考古发现了很多珍贵的文物。", "Đợt khảo cổ lần này đã phát hiện nhiều cổ vật quý.",
     "Danh từ, cũng dùng như động từ, chỉ ngành khảo cổ, nghiên cứu lịch sử qua di vật. Trong bài, 考古新发现 là những phát hiện khảo cổ mới."),
    ("经费", "jīngfèi", "kinh phí", "danh từ", "kinh phí, tiền chi tiêu", "由于经费不足，这个项目只好暂停。", "Vì thiếu kinh phí, dự án này đành phải tạm dừng.",
     "Danh từ, nghĩa là kinh phí, khoản tiền chi cho một công việc. Âm Hán Việt và nghĩa giống tiếng Việt."),
    ("预算", "yùsuàn", "dự toán", "danh từ, động từ", "ngân sách; dự trù kinh phí", "这次旅行的预算是五千块钱。", "Ngân sách cho chuyến du lịch này là năm nghìn tệ.",
     "Vừa là danh từ vừa là động từ. Danh từ là ngân sách, khoản chi dự kiến; động từ là dự trù chi phí. Cẩn thận: dự toán trong tiếng Việt thường là bảng tính chi phí công trình; còn 预算 dịch sát nhất là ngân sách, như 国家预算, ngân sách nhà nước."),
    ("参谋", "cānmóu", "tham mưu", "danh từ, động từ", "người cố vấn; góp ý, tư vấn", "买衣服的时候，我喜欢让妈妈给我当参谋。", "Khi mua quần áo, tôi thích nhờ mẹ làm quân sư.",
     "Vừa là danh từ vừa là động từ. Gốc là sĩ quan tham mưu trong quân đội; trong đời thường, 参谋 là người góp ý, cố vấn, giống quân sư trong tiếng Việt. Trong bài, 好参谋 là người cố vấn đắc lực."),
    ("繁体字", "fántǐzì", "phồn thể tự", "danh từ", "chữ phồn thể", "台湾和香港现在还在使用繁体字。", "Đài Loan và Hồng Kông hiện vẫn dùng chữ phồn thể.",
     "Danh từ, nghĩa là chữ phồn thể, tức chữ Hán viết theo lối cũ, nhiều nét. Chữ 繁 là phồn, nghĩa là nhiều, rườm rà, như trong 繁华."),
    ("简体字", "jiǎntǐzì", "giản thể tự", "danh từ", "chữ giản thể", "我们现在学的是简体字。", "Chữ chúng ta đang học là chữ giản thể.",
     "Danh từ, nghĩa là chữ giản thể, tức chữ Hán đã được giản hóa, ít nét hơn, dùng ở Trung Quốc đại lục. 繁体字 và 简体字 là một cặp từ trái nghĩa."),
    ("卫星", "wèixīng", "vệ tinh", "danh từ", "vệ tinh", "月亮是地球的卫星。", "Mặt trăng là vệ tinh của Trái Đất.",
     "Danh từ, nghĩa là vệ tinh, cả vệ tinh tự nhiên và vệ tinh nhân tạo. Trong bài, 卫星导航系统 là hệ thống định vị dẫn đường bằng vệ tinh."),
    ("导航", "dǎoháng", "đạo hàng", "động từ", "dẫn đường, định vị", "开车去陌生的地方，最好用手机导航。", "Lái xe đến nơi lạ, tốt nhất là dùng điện thoại để dẫn đường.",
     "Động từ, nghĩa là dẫn đường cho tàu thuyền, máy bay, xe cộ; cũng dùng như danh từ, chỉ thiết bị dẫn đường. Chữ 导 là dẫn, chữ 航 là hàng, như trong hàng hải, hàng không."),
    ("向导", "xiàngdǎo", "hướng đạo", "danh từ", "người dẫn đường", "我们请了一位当地人做向导。", "Chúng tôi thuê một người địa phương làm người dẫn đường.",
     "Danh từ, nghĩa là người dẫn đường. Cẩn thận: tiếng Việt hướng đạo thường gợi đến phong trào hướng đạo sinh; còn 向导 là người dẫn đường. Còn 导游 là hướng dẫn viên du lịch chuyên nghiệp."),
    ("租赁", "zūlìn", "tô nhẫm", "động từ", "thuê, cho thuê", "他在机场附近开了一家汽车租赁公司。", "Anh ấy mở một công ty cho thuê ô tô gần sân bay.",
     "Động từ, nghĩa là thuê hoặc cho thuê, trang trọng hơn 租, hay dùng trong kinh doanh: 汽车租赁，房屋租赁."),
    ("帐篷", "zhàngpeng", "trướng bồng", "danh từ", "cái lều", "晚上我们在湖边搭帐篷过夜。", "Buổi tối chúng tôi dựng lều ở bên hồ để qua đêm.",
     "Danh từ, nghĩa là cái lều. Lượng từ là 顶: 一顶帐篷. Động từ đi kèm là 搭, dựng lều. Âm tiết thứ hai đọc nhẹ."),
]

add("bullets", chapter="Từ mới (51 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 13 có 51 từ mới, chia thành 17 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 若干 (gān) · 振兴 (xīng) · 码头 · 帐篷 (peng)",
           "Từ dễ nhầm: 一向 · 一度 · 趣味 · 人士 · 产业 · 预算 · 向导"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có năm mươi mốt từ, thầy chia thành mười bảy nhóm, mỗi nhóm ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số từ có âm đọc cần chú ý, như 若干，振兴，码头，帐篷. Thầy sẽ nhắc khi gặp."),
         F(4, "Ngoài ra, có mấy từ Hán Việt rất dễ hiểu nhầm, như 一向，一度，趣味，人士，产业，预算，向导. Nghĩa của chúng trong tiếng Trung khác với tiếng Việt, các bạn nhớ nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

sizes = [3] * 17
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
    ("人类一向与旅游共存。从有了人类，就有了旅行。起初，人类旅行更准确地说，应该叫迁徙。",
     "Loài người từ trước đến nay vẫn luôn gắn liền với du lịch. Từ khi có loài người, là đã có những chuyến đi. Ban đầu, việc đi lại của loài người, nói cho chính xác hơn, thì phải gọi là di cư.",
     ["与……共存 là cùng tồn tại với…. 从……就…… là từ khi… thì đã…, nhấn mạnh hai việc xuất hiện cùng lúc.",
      "更准确地说 là nói cho chính xác hơn, dùng để chỉnh lại cách gọi. Tác giả phân biệt 旅行 và 迁徙: những chuyến đi đầu tiên không phải để ngắm cảnh, mà là để di cư."]),
    ("天气变化、食物短缺，或者有敌人侵犯，人们不得不远离居住地，寻找能够安居的地方，那时的旅行纯粹是生存和安全的需要。",
     "Thời tiết thay đổi, thức ăn khan hiếm, hoặc có kẻ thù xâm lược, con người buộc phải rời xa nơi ở, tìm đến nơi có thể an cư. Khi ấy, việc đi lại thuần túy là vì nhu cầu sinh tồn và an toàn.",
     ["短缺 là thiếu hụt, khan hiếm. 不得不 là không thể không, buộc phải. 安居 là an cư, sống yên ổn.",
      "纯粹是……的需要 là hoàn toàn chỉ vì nhu cầu…. Ba nguyên nhân thời tiết, thiếu ăn, chiến tranh đều liên quan đến sự sống còn."]),
    ("后来，古人远离家乡，去游山玩水，也就有了真正意义上的旅游。指南针发明后，中国有了海外旅行者。若干年来，旅游在世界范围内都是一个热门话题。",
     "Về sau, người xưa rời quê hương đi du ngoạn sơn thủy, thế là mới có du lịch theo đúng nghĩa. Sau khi la bàn được phát minh, Trung Quốc bắt đầu có những người đi ra nước ngoài. Bao năm nay, du lịch luôn là một chủ đề nóng trên phạm vi toàn thế giới.",
     ["游山玩水 là thành ngữ, du sơn ngoạn thủy, đi ngắm núi sông. 真正意义上的旅游 là du lịch theo đúng nghĩa của nó.",
      "热门话题 là chủ đề nóng, được nhiều người quan tâm. Đoạn này cho thấy mục đích đi lại đã thay đổi: từ sinh tồn chuyển sang thưởng ngoạn."]),
    ("一些足迹遍布世界的旅行者千方百计来到了中国，可开始，他们连一本旅游指南类的书籍都没有，可以说是困难重重。",
     "Một số người du lịch đã in dấu chân khắp thế giới tìm mọi cách đến được Trung Quốc, nhưng lúc đầu, họ đến một cuốn sách cẩm nang du lịch cũng không có, có thể nói là khó khăn chồng chất.",
     ["足迹 là dấu chân. 足迹遍布世界 là dấu chân in khắp thế giới, tức là đã đi rất nhiều nơi.",
      "连……都没有 là đến… cũng không có, nhấn mạnh sự thiếu thốn. 困难重重 là khó khăn chồng chất; hai chữ cuối đọc thanh hai, nghĩa là tầng tầng lớp lớp."]),
    ("直到1898年，中国最早的旅游指南问世了。那是一本携带方便的口袋书，作者在序言中说“天津异常繁华”，为便于外地人出行，他搜集了当地文化习俗以及车船码头等信息，做了简要介绍。",
     "Mãi đến năm 1898, cuốn cẩm nang du lịch sớm nhất của Trung Quốc mới ra đời. Đó là một cuốn sách bỏ túi tiện mang theo. Trong lời tựa, tác giả viết: Thiên Tân vô cùng sầm uất. Để người nơi khác đến tiện đi lại, ông đã thu thập thông tin về văn hóa, phong tục địa phương cùng các bến xe, bến tàu, rồi giới thiệu ngắn gọn.",
     ["直到 là mãi đến. 口袋书 là sách bỏ túi. 天津 là Thiên Tân; theo chú thích của sách, đây là một thành phố trực thuộc trung ương, trung tâm kinh tế và hải cảng quan trọng ở phía bắc Trung Quốc.",
      "为便于外地人出行 là để người nơi khác tiện đi lại, đây chính là điểm ngữ pháp 便于. 以及 là cùng với, văn viết. 外地人 là người từ nơi khác đến."],
     "直到一八九八年，中国最早的旅游指南问世了。那是一本携带方便的口袋书，作者在序言中说天津异常繁华，为便于外地人出行，他搜集了当地文化习俗以及车船码头等信息，做了简要介绍。"),
    ("之后，一度引起轰动的旅游指南要算《北平旅行指南》了，它趣味性强，实用价值高。这本书是在中外人士的共同努力下完成的，中、外文版本同时发行，真正方便了读者。",
     "Sau đó, cuốn cẩm nang từng gây xôn xao một thời phải kể đến Bắc Bình lữ hành chỉ nam; nó rất thú vị, lại có giá trị thực dụng cao. Cuốn sách được hoàn thành nhờ nỗ lực chung của các nhân sĩ Trung Quốc và nước ngoài, bản tiếng Trung và bản tiếng nước ngoài được phát hành cùng lúc, thật sự tiện lợi cho bạn đọc.",
     ["要算……了 là phải kể đến…, dùng khi nêu ra cái tiêu biểu nhất. 北平 là tên cũ của Bắc Kinh.",
      "趣味性强 là tính thú vị cao; hậu tố 性 biến từ thành danh từ chỉ tính chất. 在……的共同努力下 là nhờ nỗ lực chung của…."]),
    ("改革开放前，旅游是中国外交事业的延伸和补充。改革开放以后，旅游真正作为经济型产业受到重视，旅游指南也随着旅游业的振兴变得越来越丰富，越来越全面。",
     "Trước cải cách mở cửa, du lịch là sự nối dài và bổ sung cho công tác ngoại giao của Trung Quốc. Sau cải cách mở cửa, du lịch mới thật sự được coi trọng như một ngành kinh tế; cẩm nang du lịch cũng theo đà chấn hưng của ngành du lịch mà ngày càng phong phú, ngày càng toàn diện.",
     ["改革开放 là cải cách mở cửa, bắt đầu từ cuối thập niên bảy mươi của thế kỷ hai mươi. 作为……受到重视 là được coi trọng với tư cách là….",
      "随着……变得越来越…… là theo đà… mà ngày càng…. Đây là mẫu câu rất hay dùng khi nói về sự thay đổi."]),
    ("开始，由于游客主要是外国人，旅游类书籍便把服务对象锁定为他们。",
     "Lúc đầu, vì du khách chủ yếu là người nước ngoài, nên sách du lịch đã xác định đối tượng phục vụ là họ.",
     ["由于 là do, vì. Ở vế sau, cụm 便把 tương đương 就把, mang màu sắc văn viết.",
      "锁定为 là khóa chặt vào, xác định là. 服务对象 là đối tượng phục vụ."]),
    ("1999年以后，中国人逐渐成为游客中的主流，国内旅游和出国旅游都变得犹如家常便饭，旅游书籍也就扩大了服务对象，调整了服务宗旨，增加了相关栏目，变得越来越接地气，越来越人性化了。",
     "Sau năm 1999, người Trung Quốc dần trở thành bộ phận chủ yếu trong số du khách; du lịch trong nước và du lịch nước ngoài đều trở nên như cơm bữa. Sách du lịch cũng mở rộng đối tượng phục vụ, điều chỉnh tôn chỉ phục vụ, thêm các chuyên mục liên quan, ngày càng gần gũi đời thường, ngày càng chu đáo với người đọc.",
     ["犹如家常便饭 là giống như cơm bữa ở nhà, ý nói chuyện rất bình thường, ai cũng làm. Đây là điểm ngữ pháp 犹如.",
      "接地气 là cách nói mới, nghĩa đen là chạm vào hơi đất, nghĩa bóng là gần gũi với đời sống người dân. Ba cụm 扩大了，调整了，增加了 tạo thành một chuỗi song song rất nhịp nhàng."],
     "一九九九年以后，中国人逐渐成为游客中的主流，国内旅游和出国旅游都变得犹如家常便饭，旅游书籍也就扩大了服务对象，调整了服务宗旨，增加了相关栏目，变得越来越接地气，越来越人性化了。"),
    ("现在，最受欢迎的是自助游。背包客、自由行已成为中国人旅游最重要的方式之一。",
     "Hiện nay, được ưa chuộng nhất là du lịch tự túc. Du lịch ba lô và du lịch tự do đã trở thành một trong những hình thức du lịch quan trọng nhất của người Trung Quốc.",
     ["自助游 là du lịch tự túc, tự lên kế hoạch, không theo đoàn. 背包客 là khách du lịch ba lô.",
      "自由行 là du lịch tự do: thường chỉ đặt vé máy bay và khách sạn, còn lịch trình thì tự sắp xếp. ……之一 là một trong những…."]),
    ("和过去相比，游客不再仅关注著名旅游城市，偏僻省份、沿海城市、秀美的乡镇，都成了游客感兴趣的地方。",
     "So với trước đây, du khách không còn chỉ quan tâm đến các thành phố du lịch nổi tiếng nữa; những tỉnh xa xôi hẻo lánh, những thành phố ven biển, những thị trấn làng quê xinh đẹp đều đã trở thành nơi du khách thích thú.",
     ["和过去相比 là so với trước đây, đây là điểm ngữ pháp 和……相比. Trọng tâm của câu là nói về hiện tại.",
      "不再仅…… là không còn chỉ…. 秀美 là thanh tú, xinh đẹp. 乡镇 là làng xã, thị trấn."]),
    ("旅游指南不仅介绍地理环境、风土人情、人文特色、著名风景，还会介绍当地饮食、宗教、考古新发现等，青年旅社、经济型酒店、当地交通等内容更是必不可少。",
     "Cẩm nang du lịch không chỉ giới thiệu môi trường địa lý, phong thổ nhân tình, nét đặc sắc văn hóa, phong cảnh nổi tiếng, mà còn giới thiệu ẩm thực, tôn giáo, các phát hiện khảo cổ mới của địa phương; còn những nội dung như nhà nghỉ thanh niên, khách sạn bình dân, giao thông địa phương thì càng không thể thiếu.",
     ["不仅……还…… là không những… mà còn…. 人文特色 là nét đặc sắc về văn hóa, con người.",
      "青年旅社 là nhà nghỉ thanh niên. 经济型酒店 là khách sạn bình dân, giá rẻ. ……更是必不可少 là lại càng không thể thiếu, nhấn mạnh mức độ cao nhất."]),
    ("帮助读者选择最佳旅游时间，甚至为游客提供经费预算方面的信息，旅游指南绝对是游客的好参谋。",
     "Giúp người đọc chọn thời gian du lịch thích hợp nhất, thậm chí cung cấp cho du khách thông tin về dự trù kinh phí, cẩm nang du lịch hoàn toàn xứng đáng là người cố vấn đắc lực của du khách.",
     ["最佳 là tốt nhất, văn viết, giống 最好. 甚至 là thậm chí, đưa ra một ví dụ ở mức độ cao hơn.",
      "经费预算 là dự trù kinh phí. 绝对是 là chắc chắn là. 好参谋 là quân sư giỏi: cẩm nang du lịch được nhân hóa thành một người bạn biết góp ý."]),
    ("如今，繁体字、简体字旅游网站的开通，更大范围地方便了游客。卫星导航系统的广泛应用，使得人们不管走到哪儿，都犹如有位随身的向导。",
     "Ngày nay, việc các trang web du lịch bằng chữ phồn thể và chữ giản thể được mở ra đã mang lại tiện lợi cho du khách trên phạm vi rộng hơn. Hệ thống định vị vệ tinh được ứng dụng rộng rãi, khiến cho dù người ta đi đến đâu, cũng như có một người dẫn đường đi theo bên mình.",
     ["开通 là khai thông, đưa vào hoạt động, dùng cho trang web, đường dây, tuyến đường. Trong cụm 更大范围地方便了游客, từ 方便 là động từ, nghĩa là làm tiện lợi cho.",
      "使得 là khiến cho, văn viết. 不管……都…… là bất kể… đều…. 随身 là đi theo bên người. Đây lại là điểm ngữ pháp 犹如."]),
    ("说得夸张点儿，到汽车租赁公司租上辆汽车，带上顶帐篷，就算走到天边，你都不用发愁。",
     "Nói hơi cường điệu một chút, đến công ty cho thuê xe thuê một chiếc ô tô, mang theo một cái lều, thì dù có đi đến tận chân trời, bạn cũng chẳng phải lo lắng gì.",
     ["租上辆汽车 là thuê một chiếc xe; ở đây lược bỏ số từ một trước lượng từ, tương tự 带上顶帐篷 là mang theo một cái lều. Đây là cách nói khẩu ngữ.",
      "就算……都…… là cho dù… cũng…. 走到天边 là đi đến tận chân trời. 发愁 là lo lắng, rầu rĩ. Câu kết hóm hỉnh, cho thấy du lịch ngày nay tiện lợi hơn xưa rất nhiều."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 从旅游指南看世事变迁", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 从旅游指南看世事变迁, dài tám trăm sáu mươi tám chữ. Bài được cải biên từ bài báo Nhìn sự thay đổi qua cẩm nang du lịch của tác giả Vương Thi Bồi, đăng trên báo Tham khảo tin tức.",
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
    items=["## 1. 从古到今，人类旅行的目的有什么变化？",
           "起初：天气变化、食物短缺、敌人侵犯 → 人们不得不远离居住地（迁徙）",
           "后来：古人远离家乡，游山玩水 → 有了真正意义上的旅游",
           "## 2. 说一说中国旅游指南的发展历程",
           "开始：连一本旅游指南类的书籍都没有",
           "1898年：最早的旅游指南问世 · 为便于外地人出行，搜集了文化习俗、车船码头等信息",
           "之后：《北平旅行指南》趣味性强，实用价值高 · 中、外文版本同时发行"],
    say=["Bài tập năm của sách yêu cầu dựa vào gợi ý để tóm tắt nội dung chính của bài khóa. Chúng ta cùng làm luôn nhé.",
         F(0, "Câu hỏi một: từ xưa đến nay, mục đích đi lại của loài người đã thay đổi như thế nào?"),
         F(1, "起初，天气变化、食物短缺、敌人侵犯，人们不得不远离居住地。 Ban đầu, vì thời tiết thay đổi, thức ăn khan hiếm, kẻ thù xâm lược, con người buộc phải rời xa nơi ở. Đó là di cư."),
         F(2, "后来，古人远离家乡，游山玩水，有了真正意义上的旅游。 Về sau, người xưa rời quê đi du ngoạn sơn thủy, mới có du lịch theo đúng nghĩa."),
         F(3, "Câu hỏi hai: hãy nói về quá trình phát triển của cẩm nang du lịch Trung Quốc."),
         F(4, "开始，连一本旅游指南类的书籍都没有。 Lúc đầu, đến một cuốn cẩm nang cũng không có."),
         F(5, "一八九八年，中国最早的旅游指南问世了。 Năm một tám chín tám, cuốn cẩm nang đầu tiên ra đời. 为便于外地人出行，作者搜集了文化习俗、车船码头等信息。 Để người nơi khác tiện đi lại, tác giả đã thu thập thông tin về phong tục, bến xe, bến tàu."),
         F(6, "之后，北平旅行指南趣味性强，实用价值高，中、外文版本同时发行。 Sau đó là cuốn Bắc Bình lữ hành chỉ nam, vừa thú vị vừa thiết thực, có cả bản tiếng Trung và tiếng nước ngoài.")])

add("bullets", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5) – phần 2", size=34,
    items=["## 3. 改革开放前后，旅游指南有什么变化？",
           "前：旅游是外交事业的延伸和补充 · 游客主要是外国人，服务对象锁定为他们",
           "后：旅游作为经济型产业受到重视，旅游指南变得越来越丰富、全面",
           "1999年后：中国人成了主流 → 扩大了服务对象，调整了服务宗旨，增加了相关栏目",
           "## 4. 说一说目前旅游指南的内容和发展情况",
           "内容：不仅介绍地理环境、风土人情……，还会介绍饮食、宗教……，青年旅社等更是必不可少",
           "发展：旅游网站开通 · 卫星导航系统广泛应用，使人们犹如有位随身的向导"],
    say=[F(0, "Câu hỏi ba: trước và sau cải cách mở cửa, cẩm nang du lịch đã thay đổi thế nào?"),
         F(1, "Trước cải cách mở cửa, du lịch là sự nối dài và bổ sung cho công tác ngoại giao; du khách chủ yếu là người nước ngoài, nên sách du lịch chỉ phục vụ họ."),
         F(2, "Sau cải cách mở cửa, du lịch được coi trọng như một ngành kinh tế, cẩm nang du lịch ngày càng phong phú, toàn diện."),
         F(3, "Sau năm một chín chín chín, người Trung Quốc trở thành bộ phận chủ yếu trong số du khách. Sách du lịch 扩大了服务对象，调整了服务宗旨，增加了相关栏目, tức là mở rộng đối tượng phục vụ, điều chỉnh tôn chỉ, và thêm chuyên mục liên quan."),
         F(4, "Câu hỏi bốn: hãy nói về nội dung và tình hình phát triển của cẩm nang du lịch hiện nay."),
         F(5, "Về nội dung: 不仅介绍地理环境、风土人情，还会介绍饮食、宗教，青年旅社、经济型酒店等更是必不可少。 Không chỉ giới thiệu địa lý, phong tục, mà còn giới thiệu ẩm thực, tôn giáo; nhà nghỉ thanh niên, khách sạn bình dân thì càng không thể thiếu."),
         F(6, "Về sự phát triển: các trang web du lịch được mở ra, hệ thống định vị vệ tinh được ứng dụng rộng rãi, khiến người ta như có một người dẫn đường bên mình. Bố cục này rất có ích khi các bạn tự kể lại bài khóa.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 便于", section="Ngữ pháp 注释", title="1. 便于 biànyú – tiện cho, dễ (làm gì)", size=38,
    items=["Động từ: biểu thị làm việc gì đó tương đối dễ dàng, thuận tiện",
           "Phía sau thường là cụm động từ · phủ định: 不便于",
           "科普文章应该写得简明易懂、便于理解。",
           "多数学者认为目前图书分类太过繁杂，不便于利用。",
           "为便于外地人出行，他搜集了当地文化习俗以及车船码头等信息，做了简要介绍。"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là động từ 便于.",
         F(0, "便于 là động từ, biểu thị làm một việc gì đó tương đối dễ dàng, thuận tiện. Tiếng Việt dịch là tiện cho, dễ cho."),
         F(1, "Phía sau 便于 thường là một cụm động từ, như 便于理解，便于携带，便于管理. Dạng phủ định là 不便于. Hay gặp trong mẫu 为便于, hoặc 为了便于, nghĩa là để cho tiện."),
         F(2, "Ví dụ một: 科普文章应该写得简明易懂、便于理解。 Bài viết phổ biến khoa học nên viết ngắn gọn, dễ hiểu, để người đọc tiện nắm bắt."),
         F(3, "Ví dụ hai: 多数学者认为目前图书分类太过繁杂，不便于利用。 Đa số học giả cho rằng cách phân loại sách hiện nay quá rườm rà, không tiện sử dụng."),
         F(4, "Ví dụ ba, lấy từ bài khóa: 为便于外地人出行，他搜集了当地文化习俗以及车船码头等信息，做了简要介绍。 Để người nơi khác tiện đi lại, ông thu thập thông tin về phong tục địa phương, bến xe, bến tàu, rồi giới thiệu ngắn gọn.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: chọn vị trí thích hợp cho 便于", reveal=True, size=34,
    items=["(1) A为了B推销，她给这种儿童服装C起了个D好听的名字——帅王子。",
           "Đáp án: B → 为了便于推销……",
           "(2) 那时的建筑系只A收男生，B不收女生，学校的管理者说，这样更C管理，因为建筑系的学生需要经常在夜里作图画画，而一个女生深夜待在画室是很不D适当的。",
           "Đáp án: C → 这样更便于管理",
           "(3) 一种A说法是，B老年人胃的消化力弱，C吃面条，更D消化吸收。",
           "Đáp án: D → ……吃面条，更便于消化吸收。"],
    say=[F(0, "Luyện tập: chọn vị trí thích hợp cho 便于. Câu một: 为了推销，她给这种儿童服装起了个好听的名字，帅王子。 Để bán hàng, cô ấy đặt cho loại quần áo trẻ em này một cái tên thật hay: Hoàng tử đẹp trai. Các vị trí A, B, C, D, chọn vị trí nào? Các bạn tạm dừng và suy nghĩ nhé."),
         F(1, "Đáp án: vị trí B, ngay trước 推销: 为了便于推销。 Để tiện cho việc bán hàng. Phía sau 便于 là động từ 推销."),
         F(2, "Câu hai: 那时的建筑系只收男生，不收女生，学校的管理者说，这样更管理，因为建筑系的学生需要经常在夜里作图画画，而一个女生深夜待在画室是很不适当的。 Hồi đó khoa kiến trúc chỉ nhận nam sinh, không nhận nữ sinh. Người quản lý nhà trường nói, như vậy dễ quản lý hơn, vì sinh viên kiến trúc thường phải vẽ ban đêm, mà một nữ sinh ở lại phòng vẽ lúc đêm khuya thì rất không thích hợp."),
         F(3, "Đáp án: vị trí C: 这样更便于管理。 Như vậy tiện quản lý hơn. Phó từ 更 đứng trước 便于, còn 便于 đứng trước động từ 管理."),
         F(4, "Câu ba: 一种说法是，老年人胃的消化力弱，吃面条，更消化吸收。 Có một cách nói là, dạ dày người già tiêu hóa yếu, ăn mì thì dễ tiêu hóa hấp thu hơn."),
         F(5, "Đáp án: vị trí D: 吃面条，更便于消化吸收。 Chú ý, 便于 luôn đứng ngay trước động từ chỉ việc được làm cho dễ dàng.")])

add("bullets", chapter="Ngữ pháp: 犹如", section="Ngữ pháp 注释", title="2. 犹如 yóurú – giống như, tựa như", size=38,
    items=["Động từ, nghĩa là 好像、如同: giống như, tựa như · dùng trong văn viết",
           "Hay gặp mẫu 犹如……般 / 犹如……一般",
           "公司的劣质产品气坏了消费者，顾客的愤怒情绪犹如火山爆发般难以控制。",
           "1999年以后，中国人逐渐成为游客中的主流，国内旅游和出国旅游都变得犹如家常便饭。",
           "卫星导航系统的广泛应用，使得人们不管走到哪儿，都犹如有位随身的向导。"],
    say=["Điểm ngữ pháp thứ hai là động từ 犹如.",
         F(0, "犹如 là động từ, nghĩa giống 好像 và 如同, tiếng Việt là giống như, tựa như. Từ này dùng trong văn viết, khi nói chuyện hằng ngày người ta thường dùng 像 hoặc 好像."),
         F(1, "犹如 hay đi với 般 hoặc 一般 ở phía sau, tạo thành mẫu 犹如……般, nghĩa là giống như… vậy."),
         F(2, "Ví dụ một: 公司的劣质产品气坏了消费者，顾客的愤怒情绪犹如火山爆发般难以控制。 Sản phẩm kém chất lượng của công ty làm người tiêu dùng tức điên, cơn giận của khách hàng như núi lửa phun trào, khó mà kiểm soát."),
         F(3, "Ví dụ hai, lấy từ bài khóa: 一九九九年以后，中国人逐渐成为游客中的主流，国内旅游和出国旅游都变得犹如家常便饭。 Sau năm một chín chín chín, người Trung Quốc dần thành bộ phận chủ yếu trong số du khách, du lịch trong nước và nước ngoài đều trở nên như cơm bữa."),
         F(4, "Ví dụ ba, cũng lấy từ bài khóa: 卫星导航系统的广泛应用，使得人们不管走到哪儿，都犹如有位随身的向导。 Hệ thống định vị vệ tinh được dùng rộng rãi, khiến người ta đi đến đâu cũng như có một người dẫn đường bên mình.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: chọn vế trước thích hợp cho câu có 犹如", reveal=True, size=34,
    items=["## A. 我们的人生 · B. 先生讲课声调不高 · C. 夕阳照耀下的古城",
           "(1) （　　），犹如温暖的春风扑面，智慧的清泉入心。",
           "Đáp án: B – 先生讲课声调不高，犹如温暖的春风扑面……",
           "(2) （　　），色彩犹如油画般厚重。",
           "Đáp án: C – 夕阳照耀下的古城，色彩犹如油画般厚重。",
           "(3) （　　），犹如一片一望无际的大海，我们每个人，每天都在这片广阔的大海上航行。……",
           "Đáp án: A – 我们的人生，犹如一片一望无际的大海……"],
    say=[F(0, "Luyện tập: chọn vế trước thích hợp. Ba lựa chọn là: A, 我们的人生, cuộc đời chúng ta. B, 先生讲课声调不高, thầy giảng bài giọng không to. C, 夕阳照耀下的古城, tòa cổ thành dưới ánh hoàng hôn."),
         F(1, "Câu một: 犹如温暖的春风扑面，智慧的清泉入心。 Như làn gió xuân ấm áp phả vào mặt, như dòng suối trí tuệ trong lành thấm vào tim. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: B. 先生讲课声调不高，犹如温暖的春风扑面，智慧的清泉入心。 Thầy giảng bài giọng không to, nhưng như gió xuân ấm áp, như suối trí tuệ thấm vào lòng người nghe."),
         F(3, "Câu hai: 色彩犹如油画般厚重。 Màu sắc đậm đà như một bức tranh sơn dầu."),
         F(4, "Đáp án: C. 夕阳照耀下的古城，色彩犹如油画般厚重。 Tòa cổ thành dưới ánh hoàng hôn, màu sắc đậm đà như tranh sơn dầu. Câu này dùng mẫu 犹如……般."),
         F(5, "Câu ba: 犹如一片一望无际的大海，我们每个人，每天都在这片广阔的大海上航行。不爱大海的人，每天都会觉得度日如年、生无所盼；只有热爱海洋的人，才会懂得大海。 Như một vùng biển mênh mông bất tận, mỗi chúng ta ngày ngày đều đi thuyền trên biển rộng ấy. Người không yêu biển sẽ thấy mỗi ngày dài như một năm, sống chẳng có gì mong đợi; chỉ người yêu biển mới hiểu được biển cả."),
         F(6, "Đáp án: A. 我们的人生，犹如一片一望无际的大海。 Cuộc đời chúng ta giống như một vùng biển mênh mông.")])

add("bullets", chapter="Ngữ pháp: 和……相比", section="Ngữ pháp 注释", title="3. 和……相比 – so với…", size=36,
    items=["Dạng đầy đủ: A和B相比，A…… (hai chữ A chỉ cùng một sự vật)",
           "Trọng tâm: miêu tả, trình bày đầy đủ về A · cũng nói 与……相比、同……相比",
           "由于经济环境的不确定，企业的寿命越来越短，和10年前相比，人们要经历更多次的职业选择。",
           "走出书店的大门，他眼前一亮，和昏暗、冷清的书店相比，外面的大街既明亮又热闹。",
           "和过去相比，游客不再仅关注著名旅游城市，偏僻省份、沿海城市、秀美的乡镇，都成了游客感兴趣的地方。"],
    say=["Điểm ngữ pháp thứ ba là cấu trúc 和……相比, nghĩa là so với.",
         F(0, "Dạng đầy đủ của cấu trúc này là: A和B相比，A thế nào. Hai chữ A trong mẫu chỉ cùng một sự vật. Trong thực tế, A thứ nhất thường được lược đi, nên ta hay gặp dạng 和B相比, rồi đến phần nói về A."),
         F(1, "Trọng tâm của câu nằm ở phần trình bày, miêu tả về A, còn B chỉ là mốc để so sánh. Ngoài 和, còn có thể nói 与……相比 trong văn viết, hoặc 同……相比."),
         F(2, "Ví dụ một: 由于经济环境的不确定，企业的寿命越来越短，和十年前相比，人们要经历更多次的职业选择。 Do môi trường kinh tế bất ổn, tuổi thọ doanh nghiệp ngày càng ngắn; so với mười năm trước, con người phải trải qua nhiều lần chọn nghề hơn."),
         F(3, "Ví dụ hai: 走出书店的大门，他眼前一亮，和昏暗、冷清的书店相比，外面的大街既明亮又热闹。 Bước ra khỏi cửa hiệu sách, mắt anh ấy sáng bừng lên; so với hiệu sách tối tăm, vắng vẻ, con phố bên ngoài vừa sáng sủa vừa nhộn nhịp."),
         F(4, "Ví dụ ba, lấy từ bài khóa: 和过去相比，游客不再仅关注著名旅游城市，偏僻省份、沿海城市、秀美的乡镇，都成了游客感兴趣的地方。 So với trước đây, du khách không còn chỉ quan tâm đến thành phố du lịch nổi tiếng. Ở đây B là quá khứ, còn A, tức hiện tại, mới là trọng tâm.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: đặt cụm trong ngoặc vào vị trí thích hợp", reveal=True, size=34,
    items=["(1) 今天，A我们B从阅读、写信、学习、购物到看病，C无不依赖电脑来完成。D人们的生活方式、工作方式已发生了深刻的变革。（和昨天相比，）",
           "Đáp án: D → ……和昨天相比，人们的生活方式、工作方式已发生了深刻的变革。",
           "(2) 虽然，A大学生对自我情绪B具有一定的控制能力，C但在激动状态下，D也常因情绪失控而产生冲动性的行为。（和中学生相比，）",
           "Đáp án: A → 虽然，和中学生相比，大学生对自我情绪具有一定的控制能力……",
           "(3) A影视服装有着自身的艺术形式和规律B，其设计C必须服从影视剧的特定时间、环境、情节和角色的身份需求D。（和其他服装相比，）",
           "Đáp án: A → 和其他服装相比，影视服装有着自身的艺术形式和规律……"],
    say=[F(0, "Luyện tập: đặt cụm từ trong ngoặc vào vị trí thích hợp. Câu một, cụm cần đặt là 和昨天相比: 今天，我们从阅读、写信、学习、购物到看病，无不依赖电脑来完成。人们的生活方式、工作方式已发生了深刻的变革。 Ngày nay, từ đọc sách, viết thư, học tập, mua sắm cho đến khám bệnh, chúng ta đều dựa vào máy tính. Lối sống, cách làm việc của con người đã thay đổi sâu sắc. Các bạn tạm dừng và chọn vị trí nhé."),
         F(1, "Đáp án: vị trí D: 和昨天相比，人们的生活方式、工作方式已发生了深刻的变革。 So với hôm qua, lối sống và cách làm việc đã thay đổi sâu sắc. Phần nói về A, tức là lối sống hôm nay, đứng ngay sau cụm so sánh."),
         F(2, "Câu hai, cụm cần đặt là 和中学生相比: 虽然，大学生对自我情绪具有一定的控制能力，但在激动状态下，也常因情绪失控而产生冲动性的行为。 Tuy sinh viên đại học có khả năng kiểm soát cảm xúc nhất định, nhưng khi xúc động, vẫn thường mất kiểm soát mà có hành vi bốc đồng."),
         F(3, "Đáp án: vị trí A: 虽然，和中学生相比，大学生对自我情绪具有一定的控制能力。 Tuy so với học sinh trung học, sinh viên có khả năng tự kiểm soát cảm xúc hơn. Cụm so sánh đứng trước chủ ngữ A, tức là 大学生."),
         F(4, "Câu ba, cụm cần đặt là 和其他服装相比: 影视服装有着自身的艺术形式和规律，其设计必须服从影视剧的特定时间、环境、情节和角色的身份需求。 Trang phục điện ảnh có hình thức nghệ thuật và quy luật riêng, việc thiết kế phải tuân theo thời gian, bối cảnh, tình tiết và thân phận nhân vật của bộ phim."),
         F(5, "Đáp án: vị trí A: 和其他服装相比，影视服装有着自身的艺术形式和规律。 So với các loại trang phục khác, trang phục điện ảnh có hình thức và quy luật riêng. Mẹo: cụm 和……相比 thường đứng ngay trước sự vật A được đem ra so sánh.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 一向 – 一度", section="Phân biệt từ 词语辨析", title="Phân biệt 一向 và 一度 (1)",
    common="Giống nhau: khi làm phó từ, đều chỉ phạm vi thời gian, nhưng thường không thay thế cho nhau được.",
    cols=[{"head": "一向",
           "lines": ["(1) Từ quá khứ đến hiện tại, luôn luôn như vậy",
                     "Đúng: 我们家一向好客，来了客人总是热情招待。"]},
          {"head": "一度",
           "lines": ["(1) Trong quá khứ từng xảy ra một thời gian, có một dạo",
                     "Đúng: 去年，老师一度病得很厉害，现在好多了。"]}],
    say=["Tiếp theo là phần phân biệt từ: 一向 và 一度. Hai từ này đều bắt đầu bằng 一, đều là phó từ chỉ thời gian, nên người học rất hay dùng lẫn lộn.",
         "Điểm giống nhau: khi làm phó từ, cả hai đều chỉ một phạm vi thời gian, nhưng nghĩa khác nhau rõ rệt, nên thường không thay thế cho nhau được.",
         F(0, "Điểm khác thứ nhất. 一向 chỉ một trạng thái kéo dài từ quá khứ đến hiện tại, xưa nay vẫn luôn như vậy. Ví dụ: 我们家一向好客，来了客人总是热情招待。 Nhà chúng tôi xưa nay vẫn hiếu khách, có khách đến là luôn tiếp đãi nhiệt tình."),
         F(1, "Còn 一度 chỉ một việc đã từng xảy ra trong một khoảng thời gian ở quá khứ, bây giờ không còn nữa. Ví dụ: 去年，老师一度病得很厉害，现在好多了。 Năm ngoái thầy giáo có một dạo ốm rất nặng, bây giờ đã đỡ nhiều rồi."),
         "Các bạn thấy không: 一向 là một đường thẳng kéo dài đến hiện tại; còn 一度 chỉ là một đoạn ngắn trong quá khứ."])

add("compare", section="Phân biệt từ 词语辨析", title="Phân biệt 一向 và 一度 (2)",
    cols=[{"head": "一向",
           "lines": ["(2) Từ lần gặp trước đến nay (lời hỏi thăm)",
                     "Đúng: 你一向好啊！",
                     "(3) Không có cách dùng số lượng từ"]},
          {"head": "一度",
           "lines": ["(2) Không có nghĩa này",
                     "(3) Còn là số lượng từ: một lần, một đợt · 一年一度",
                     "Đúng: 一年一度的春节又到了。"]}],
    say=[F(0, "Điểm khác thứ hai. 一向 còn chỉ khoảng thời gian từ lần gặp trước đến bây giờ, hay dùng trong lời hỏi thăm khi gặp lại. Ví dụ: 你一向好啊！ Dạo này anh vẫn khỏe chứ! 一度 không có nghĩa này."),
         F(1, "Điểm khác thứ ba. 一度 còn là số lượng từ, nghĩa là một lần, một đợt. Hay nói 一年一度, mỗi năm một lần. Ví dụ: 一年一度的春节又到了。 Tết Xuân mỗi năm một lần lại đến rồi. 一向 không có cách dùng này."),
         "Mẹo nhớ: nói về thói quen, tính cách lâu dài thì dùng 一向; nói về một giai đoạn đã qua, hoặc mỗi năm một lần, thì dùng 一度."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: chọn 一向 hay 一度 điền vào chỗ trống", reveal=True, size=36,
    items=["(1) 他的性格比较古怪，___独来独往，不跟别人交流。",
           "Đáp án: 一向 – tính cách xưa nay vẫn vậy",
           "(2) 一年___春又到，柳树已经发芽，燕子也都飞回来了。",
           "Đáp án: 一度 – 一年一度, mỗi năm một lần",
           "(3) 老王，好久不见，你___可好？",
           "Đáp án: 一向 – lời hỏi thăm khi gặp lại",
           "(4) 汉语太难了，我___想放弃，但最后还是坚持下来了。",
           "Đáp án: 一度 – một dạo trong quá khứ, nay không còn"],
    say=[F(0, "Bây giờ chúng ta làm thử: chọn 一向 hay 一度 điền vào chỗ trống. Câu một: 他的性格比较古怪，什么独来独往，不跟别人交流。 Tính cách anh ấy khá kỳ quặc, đi đâu cũng một mình, không giao lưu với ai. Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: 一向. 他的性格比较古怪，一向独来独往。 Đây là tính cách lâu dài, xưa nay vẫn vậy."),
         F(2, "Câu hai: 一年什么春又到，柳树已经发芽，燕子也都飞回来了。 Mùa xuân lại về, cây liễu đã nảy mầm, chim én cũng đã bay về."),
         F(3, "Đáp án: 一度. 一年一度春又到。 Mỗi năm một lần, mùa xuân lại về. Đây là cách dùng số lượng từ."),
         F(4, "Câu ba: 老王，好久不见，你什么可好？ Anh Vương, lâu quá không gặp, dạo này anh vẫn khỏe chứ?"),
         F(5, "Đáp án: 一向. 你一向可好？ Đây là lời hỏi thăm từ lần gặp trước đến nay."),
         F(6, "Câu bốn: 汉语太难了，我什么想放弃，但最后还是坚持下来了。 Tiếng Trung khó quá, tôi có lúc đã muốn bỏ cuộc, nhưng cuối cùng vẫn kiên trì được."),
         F(7, "Đáp án: 一度. 我一度想放弃。 Ý muốn bỏ cuộc chỉ có trong một thời gian ở quá khứ, bây giờ đã không còn. Hy vọng các bạn cũng như vậy nhé!")])

# ======================= MỞ RỘNG: CÂU SAI VỀ LOGIC =======================
add("bullets", chapter="Mở rộng: câu sai về logic", section="Mở rộng 扩展", title="Câu sai: logic không thông (逻辑不通)", size=36,
    items=["Câu đúng ngữ pháp, nhưng ý nghĩa mâu thuẫn trước sau",
           "Hoặc trái với logic hình thức (khái niệm, phán đoán, suy luận), hay trái với lẽ thường của sự việc",
           "## Các dạng thường gặp",
           "Dùng sai từ liên kết · Ý trước sau mâu thuẫn",
           "Khái niệm bao hàm lẫn nhau · Phán đoán không thành lập",
           "Phủ định hai lần thành khẳng định"],
    say=["Bây giờ chúng ta sang phần mở rộng của sách. Quyển Thượng không có mục tu từ riêng, thay vào đó là kỹ năng nhận biết câu sai. Ở các bài trước, các bạn đã gặp câu sai do thiếu thành phần hay trật tự từ không đúng. Hôm nay là một loại câu sai khó nhận ra hơn: câu sai về logic, tiếng Trung gọi là 逻辑不通.",
         F(0, "逻辑不通 là khi câu văn hoàn toàn đúng về mặt ngữ pháp, nhưng ý nghĩa thì mâu thuẫn, câu trước nói một đằng, câu sau nói một nẻo."),
         F(1, "Hoặc câu văn không phù hợp với logic hình thức, như khái niệm, phán đoán, suy luận; hay không phù hợp với lẽ thường của sự việc."),
         F(2, "Qua năm ví dụ của sách, ta có thể thấy các dạng thường gặp."),
         F(3, "Một là dùng sai từ liên kết, ví dụ đảo lộn nguyên nhân và kết quả. Hai là ý trước sau mâu thuẫn nhau."),
         F(4, "Ba là các khái niệm bao hàm lẫn nhau, khái niệm lớn và khái niệm nhỏ bị đặt ngang hàng. Bốn là phán đoán không thành lập."),
         F(5, "Năm là phủ định hai lần, vô tình biến thành khẳng định, khiến câu nói ngược hẳn ý mình muốn nói. Chúng ta cùng xem từng ví dụ.")])

add("bullets", section="Mở rộng 扩展", title="Ví dụ câu sai về logic (1)", size=34,
    items=["## (1) Dùng sai từ liên kết",
           "Sai: 骑自行车可以锻炼身体，还不用汽油，因为它是最环保的交通工具。",
           "Sửa: ……，所以/因此它是最环保的交通工具。 (hai vế trước là nguyên nhân)",
           "## (2) Ý trước sau mâu thuẫn",
           "Sai: 下一步金融改革的重点之一是加快建立存款保险制度，目前存款保险制度建立接近成熟。",
           "Phân tích: vế trước cho thấy chế độ này chưa được xây dựng, vế sau lại nói đã gần hoàn thiện"],
    say=[F(0, "Ví dụ một: dùng sai từ liên kết."),
         F(1, "Câu sai: 骑自行车可以锻炼身体，还不用汽油，因为它是最环保的交通工具。 Đi xe đạp có thể rèn luyện thân thể, lại không tốn xăng, bởi vì nó là phương tiện giao thông thân thiện với môi trường nhất."),
         F(2, "Hai vế đầu, rèn luyện thân thể và không tốn xăng, mới là nguyên nhân; còn vế cuối là kết luận. Vậy từ liên kết phải là 所以 hoặc 因此: 所以它是最环保的交通工具。"),
         F(3, "Ví dụ hai: ý trước sau mâu thuẫn."),
         F(4, "Câu sai: 下一步金融改革的重点之一是加快建立存款保险制度，目前存款保险制度建立接近成熟。 Một trong những trọng điểm của bước cải cách tài chính tiếp theo là đẩy nhanh việc xây dựng chế độ bảo hiểm tiền gửi; hiện nay việc xây dựng chế độ bảo hiểm tiền gửi đã gần hoàn thiện."),
         F(5, "Vế trước nói phải đẩy nhanh việc xây dựng, tức là chế độ này còn chưa có; vế sau lại nói đã gần hoàn thiện. Hai vế mâu thuẫn nhau, câu không thể đứng được.")])

add("bullets", section="Mở rộng 扩展", title="Ví dụ câu sai về logic (2)", size=34,
    items=["## (3) Khái niệm bao hàm lẫn nhau",
           "Sai: 人们更喜欢吃一些新鲜的梨、桃、瓜果，而不喜欢服用维生素C药丸。",
           "Sửa: thay 瓜果 bằng tên một loại quả cụ thể (梨、桃 vốn thuộc 瓜果)",
           "## (4) Phán đoán không thành lập",
           "Sai: 中国是个多民族国家，是56个民族。 → Sửa: ……，有56个民族。",
           "## (5) Phủ định hai lần thành khẳng định",
           "Sai: 为了杜绝假冒伪劣产品不再流入市场，必须加强生产、流通环节的监督管理。",
           "Sửa: 为了杜绝假冒伪劣产品流入市场，……"],
    say=[F(0, "Ví dụ ba: khái niệm bao hàm lẫn nhau."),
         F(1, "Câu sai: 人们更喜欢吃一些新鲜的梨、桃、瓜果，而不喜欢服用维生素C药丸。 Mọi người thích ăn lê, đào, dưa và hoa quả tươi hơn là uống viên vitamin C."),
         F(2, "Lê và đào vốn thuộc nhóm 瓜果, hoa quả nói chung. Đặt khái niệm lớn ngang hàng với khái niệm nhỏ là sai logic. Phải thay 瓜果 bằng tên một loại quả cụ thể khác, ví dụ 苹果."),
         F(3, "Ví dụ bốn: phán đoán không thành lập."),
         F(4, "Câu sai: 中国是个多民族国家，是五十六个民族。 Câu Trung Quốc là năm mươi sáu dân tộc không đúng, vì một đất nước không phải là các dân tộc. Phải sửa: 中国有五十六个民族。 Trung Quốc có năm mươi sáu dân tộc."),
         F(5, "Ví dụ năm: phủ định hai lần thành khẳng định."),
         F(6, "Câu sai: 为了杜绝假冒伪劣产品不再流入市场，必须加强生产、流通环节的监督管理。"),
         F(7, "杜绝 nghĩa là ngăn chặn triệt để, đã mang nghĩa phủ định; thêm 不再 nữa là phủ định hai lần, thành ra ý câu là để hàng giả được vào thị trường. Phải bỏ 不再: 为了杜绝假冒伪劣产品流入市场。 Để ngăn chặn triệt để hàng giả, hàng kém chất lượng tràn vào thị trường.")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chỉ ra lỗi và sửa lại (1)", reveal=True, size=34,
    items=["(1) 年轻人缺乏的就是理论水平不高和工作经验不足。",
           "Đáp án: Mâu thuẫn (缺乏 + 不高, 不足) → 年轻人缺乏的就是理论水平和工作经验。",
           "(2) 晚会上表演了音乐、舞蹈、武术和很多文艺节目。",
           "Đáp án: Khái niệm bao hàm → ……音乐、舞蹈、武术等很多文艺节目。",
           "(3) 由北京人民艺术剧院复排的大型历史话剧《蔡文姬》定于5月1日在首都剧场上演，日前正在紧张的排练之中。",
           "Đáp án: Mâu thuẫn thời gian (日前 là mấy hôm trước) → 目前正在紧张的排练之中。"],
    say=[F(0, "Luyện tập: chỉ ra lỗi của các câu sau và đề xuất cách sửa. Câu một: 年轻人缺乏的就是理论水平不高和工作经验不足。 Thứ người trẻ thiếu chính là trình độ lý luận không cao và kinh nghiệm làm việc không đủ. Câu này sai ở đâu? Các bạn tạm dừng và suy nghĩ nhé."),
         F(1, "Đáp án: 缺乏 đã có nghĩa là thiếu, phía sau lại có 不高 và 不足, thành ra thiếu cái không cao, thiếu cái không đủ, ý mâu thuẫn. Sửa: 年轻人缺乏的就是理论水平和工作经验。 Hoặc: 年轻人的问题就是理论水平不高和工作经验不足。"),
         F(2, "Câu hai: 晚会上表演了音乐、舞蹈、武术和很多文艺节目。 Buổi dạ hội biểu diễn âm nhạc, múa, võ thuật và rất nhiều tiết mục văn nghệ."),
         F(3, "Đáp án: âm nhạc, múa, võ thuật vốn đều là tiết mục văn nghệ của buổi dạ hội, không thể đặt ngang hàng với 文艺节目 bằng chữ 和. Sửa: 晚会上表演了音乐、舞蹈、武术等很多文艺节目。"),
         F(4, "Câu ba: 由北京人民艺术剧院复排的大型历史话剧蔡文姬定于五月一日在首都剧场上演，日前正在紧张的排练之中。 Vở kịch lịch sử lớn Thái Văn Cơ do Nhà hát Nghệ thuật Nhân dân Bắc Kinh dàn dựng lại, dự kiến công diễn ngày một tháng năm tại Nhà hát Thủ đô, hiện đang tập luyện khẩn trương."),
         F(5, "Đáp án: 日前 nghĩa là mấy hôm trước, mâu thuẫn với 正在, nghĩa là đang. Phải đổi thành 目前, nghĩa là hiện nay: 目前正在紧张的排练之中。 Các bạn chú ý cặp từ dễ nhầm này: 日前 là mấy hôm trước, 目前 là hiện nay.")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chỉ ra lỗi và sửa lại (2)", reveal=True, size=34,
    items=["(4) 在古代，这类音乐作品只有文字记载，没有乐谱资料，既无法演奏，也无法演唱。",
           "Đáp án: Trái lẽ thường (thời xưa vẫn diễn được) → 这类古代音乐作品只有文字记载，没有乐谱资料，现在既无法演奏，也无法演唱。",
           "(5) 昨天是HSK考试报名截止日期的最后一天，还陆续有人前来报名。",
           "Đáp án: Khái niệm không hợp (ngày hết hạn không có ngày cuối) → 昨天是HSK考试报名的最后一天 / 截止日期，……"],
    say=[F(0, "Câu bốn: 在古代，这类音乐作品只有文字记载，没有乐谱资料，既无法演奏，也无法演唱。 Thời cổ đại, loại tác phẩm âm nhạc này chỉ có ghi chép bằng chữ, không có bản nhạc, nên không thể diễn tấu, cũng không thể biểu diễn hát. Câu này sai ở đâu?"),
         F(1, "Đáp án: thời cổ đại, người ta vẫn biểu diễn được các tác phẩm này; chính bây giờ, vì không có bản nhạc, nên mới không biểu diễn được. Câu sai lẽ thường của sự việc. Sửa: 这类古代音乐作品只有文字记载，没有乐谱资料，现在既无法演奏，也无法演唱。"),
         F(2, "Câu năm: 昨天是HSK考试报名截止日期的最后一天，还陆续有人前来报名。 Hôm qua là ngày cuối cùng của ngày hết hạn đăng ký thi HSK, vẫn lần lượt có người đến đăng ký."),
         F(3, "Đáp án: 截止日期 là ngày hết hạn, bản thân nó đã là một ngày, nên không thể có ngày cuối cùng của ngày hết hạn. Sửa: 昨天是HSK考试报名的最后一天, hoặc 昨天是HSK考试报名的截止日期。 Mẹo: với câu sai logic, hãy đọc chậm, tự hỏi từng vế có hợp lý không, và các khái niệm có bao hàm lẫn nhau hay không.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ có dấu chấm", size=40,
    items=["犹如 (如) → 比如 · 例如 · 譬如 · 一如既往",
           "生存 (存) → 存在 · 保存 · 储存 · 存款",
           "简要 (简) → 简单 · 简短 · 简便 · 简化",
           "趣味 (趣) → 兴趣 · 乐趣 · 有趣 · 情趣",
           "产业 (业) → 工业 · 农业 · 商业 · 企业"],
    say=["Phần luyện tập. Bài tập một: mô phỏng ví dụ, viết thêm các từ có chứa chữ được đánh dấu chấm.",
         F(0, "Ví dụ mẫu: 犹如, chữ được đánh dấu là chữ 如. Ta có 比如，例如，譬如，一如既往. Tức là ví như, ví dụ như, chẳng hạn như, và trước sau như một."),
         F(1, "生存, chữ được đánh dấu là chữ 存, nghĩa là còn, giữ lại. Ta có 存在，保存，储存，存款. Tức là tồn tại, bảo tồn, tích trữ, và tiền gửi tiết kiệm."),
         F(2, "简要, chữ được đánh dấu là chữ 简, nghĩa là đơn giản, gọn. Ta có 简单，简短，简便，简化. Tức là đơn giản, ngắn gọn, giản tiện, và giản hóa."),
         F(3, "趣味, chữ được đánh dấu là chữ 趣, nghĩa là thú vị. Ta có 兴趣，乐趣，有趣，情趣. Tức là hứng thú, niềm vui, thú vị, và tình thú."),
         F(4, "产业, chữ được đánh dấu là chữ 业, nghĩa là ngành, nghề. Ta có 工业，农业，商业，企业. Tức là công nghiệp, nông nghiệp, thương nghiệp, và doanh nghiệp.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Hoàn thành câu với từ cho sẵn (1)", reveal=True, size=36,
    items=["(1) ________，后来我慢慢明白了父母的心。（起初）",
           "Đáp án: 起初我不理解父母为什么对我那么严格，后来我慢慢明白了父母的心。",
           "(2) ________，他几乎没生过病。（和……相比）",
           "Đáp án: 和同龄人相比，他的身体非常好，这些年他几乎没生过病。",
           "(3) 大学毕业以后，________。（若干）",
           "Đáp án: 大学毕业以后，他在国外工作了若干年，去年才回国。"],
    say=[F(0, "Bài tập hai: dùng từ hoặc cấu trúc cho sẵn để hoàn thành câu. Câu một, dùng 起初: 什么什么，后来我慢慢明白了父母的心。 Về sau tôi dần dần hiểu được tấm lòng của bố mẹ. Các bạn tạm dừng và thử viết nhé."),
         F(1, "Đáp án gợi ý: 起初我不理解父母为什么对我那么严格，后来我慢慢明白了父母的心。 Lúc đầu tôi không hiểu vì sao bố mẹ nghiêm khắc với tôi như vậy, về sau tôi dần hiểu được tấm lòng của bố mẹ. Chú ý cặp 起初 và 后来."),
         F(2, "Câu hai, dùng 和……相比: 什么什么，他几乎没生过病。 Anh ấy hầu như chưa từng bị ốm."),
         F(3, "Đáp án gợi ý: 和同龄人相比，他的身体非常好，这些年他几乎没生过病。 So với những người cùng tuổi, sức khỏe của anh ấy rất tốt, mấy năm nay hầu như chưa ốm lần nào."),
         F(4, "Câu ba, dùng 若干: 大学毕业以后，什么什么。 Sau khi tốt nghiệp đại học."),
         F(5, "Đáp án gợi ý: 大学毕业以后，他在国外工作了若干年，去年才回国。 Sau khi tốt nghiệp đại học, anh ấy làm việc ở nước ngoài một số năm, năm ngoái mới về nước.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Hoàn thành câu với từ cho sẵn (2)", reveal=True, size=36,
    items=["(4) 印度尼西亚被称为千岛之国，________。（遍布）",
           "Đáp án: ……，大大小小的岛屿遍布全国。",
           "(5) 虽然他现在很成功，但________。（一度）",
           "Đáp án: ……，但他一度失去工作，生活非常困难。",
           "(6) 为了公司的发展，________。（千方百计）",
           "Đáp án: ……，他千方百计地寻找新的客户。"],
    say=[F(0, "Câu bốn, dùng 遍布: 印度尼西亚被称为千岛之国，什么什么。 Indonesia được gọi là đất nước nghìn đảo."),
         F(1, "Đáp án gợi ý: 印度尼西亚被称为千岛之国，大大小小的岛屿遍布全国。 Những hòn đảo lớn nhỏ rải khắp cả nước."),
         F(2, "Câu năm, dùng 一度: 虽然他现在很成功，但什么什么。 Tuy bây giờ anh ấy rất thành công, nhưng…"),
         F(3, "Đáp án gợi ý: 虽然他现在很成功，但他一度失去工作，生活非常困难。 Nhưng đã có một dạo anh ấy mất việc, cuộc sống vô cùng khó khăn. Ở đây phải dùng 一度, vì đó là một giai đoạn trong quá khứ."),
         F(4, "Câu sáu, dùng 千方百计: 为了公司的发展，什么什么。 Vì sự phát triển của công ty."),
         F(5, "Đáp án gợi ý: 为了公司的发展，他千方百计地寻找新的客户。 Vì sự phát triển của công ty, anh ấy tìm đủ mọi cách để kiếm khách hàng mới.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (1)", reveal=True, size=36,
    items=["## Từ cho sẵn: 人士 · 版本 · 问世 · 简要 · 序言",
           "他是一位深受广大读者喜爱的作家。最近，他的又一本新书___了，在中外___的共同努力下，该书的中、外文___同时发行。作者在___中___介绍了这本书的内容，除此以外，还对家人和朋友的支持表示了感谢。",
           "Đáp án: 问世 · 人士 · 版本 · 序言 · 简要"],
    say=[F(0, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn một có năm từ: 人士，版本，问世，简要，序言."),
         F(1, "他是一位深受广大读者喜爱的作家。最近，他的又一本新书什么了，在中外什么的共同努力下，该书的中、外文什么同时发行。作者在什么中什么介绍了这本书的内容，除此以外，还对家人和朋友的支持表示了感谢。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 新书问世了，在中外人士的共同努力下，中、外文版本同时发行，作者在序言中简要介绍了这本书的内容。 Ông là nhà văn được đông đảo bạn đọc yêu mến. Gần đây, một cuốn sách mới nữa của ông ra mắt; nhờ nỗ lực chung của các nhân sĩ trong và ngoài nước, bản tiếng Trung và bản tiếng nước ngoài được phát hành cùng lúc. Trong lời tựa, tác giả giới thiệu ngắn gọn nội dung cuốn sách, ngoài ra còn cảm ơn sự ủng hộ của gia đình và bạn bè.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (2)", reveal=True, size=36,
    items=["## Từ cho sẵn: 振兴 · 偏僻 · 人性 · 产业 · 风土人情",
           "随着中国经济的发展，旅游逐渐成为人们生活中必不可少的一部分。人们不但关注那些著名的旅游城市，也把越来越多的目光投向了___省份，那些地方独特的___吸引了越来越多的游客。随着当地旅游___的___，服务质量也有所提升，变得越来越___化了。",
           "Đáp án: 偏僻 · 风土人情 · 产业 · 振兴 · 人性"],
    say=[F(0, "Đoạn hai có năm từ: 振兴，偏僻，人性，产业，风土人情."),
         F(1, "随着中国经济的发展，旅游逐渐成为人们生活中必不可少的一部分。人们不但关注那些著名的旅游城市，也把越来越多的目光投向了什么省份，那些地方独特的什么吸引了越来越多的游客。随着当地旅游什么的什么，服务质量也有所提升，变得越来越什么化了。 Các bạn điền thử nhé."),
         F(2, "Đáp án: 投向了偏僻省份，独特的风土人情，随着当地旅游产业的振兴，变得越来越人性化了。 Cùng với sự phát triển kinh tế, du lịch dần trở thành phần không thể thiếu trong cuộc sống. Người ta không chỉ quan tâm đến các thành phố du lịch nổi tiếng, mà còn hướng ánh mắt đến các tỉnh xa xôi; phong thổ, phong tục độc đáo nơi đó thu hút ngày càng nhiều du khách. Cùng với sự chấn hưng của ngành du lịch địa phương, chất lượng phục vụ cũng được nâng lên, ngày càng chu đáo hơn."),
         "Các bạn thấy không, đoạn văn này gần như tóm tắt lại phần cuối của bài khóa. Làm bài tập điền từ cũng là một cách ôn lại bài rất hiệu quả."])

add("bullets", section="Luyện tập 练习", title="Bài tập 4: Sắp xếp lại thứ tự câu phức", reveal=True, size=34,
    items=["(1) A. 因为我不但是北京人 · B. 看见过许多西方的名城 · C. 北京是美丽的，我知道 · D. 而且到过欧美",
           "Đáp án: C – A – D – B → 北京是美丽的，我知道，因为我不但是北京人，而且到过欧美，看见过许多西方的名城。",
           "(2) A. 我们无论认识什么事物 · B. 不但要看到它的正面 · C. 都必须全面地去看 · D. 而且要看到它的反面 · E. 否则，就不能有比较完整和正确的认识",
           "Đáp án: A – C – B – D – E → 我们无论认识什么事物，都必须全面地去看，不但要看到它的正面，而且要看到它的反面，否则，就不能有比较完整和正确的认识。"],
    say=[F(0, "Bài tập bốn: sắp xếp lại thứ tự của hai nhóm câu phức. Nhóm một có bốn vế: A, 因为我不但是北京人。 B, 看见过许多西方的名城。 C, 北京是美丽的，我知道。 D, 而且到过欧美。 Các bạn tạm dừng và sắp xếp thử nhé. Gợi ý: hãy tìm các cặp từ liên kết."),
         F(1, "Đáp án: C, A, D, B. 北京是美丽的，我知道，因为我不但是北京人，而且到过欧美，看见过许多西方的名城。 Bắc Kinh đẹp, tôi biết điều đó, vì tôi không những là người Bắc Kinh, mà còn từng đến Âu Mỹ, đã thấy nhiều thành phố nổi tiếng của phương Tây. Câu chính đứng đầu, 因为 giải thích lý do, cặp 不但……而且 đi liền nhau, và chỉ khi đến Âu Mỹ rồi mới thấy được các thành phố phương Tây."),
         F(2, "Nhóm hai có năm vế: A, 我们无论认识什么事物。 B, 不但要看到它的正面。 C, 都必须全面地去看。 D, 而且要看到它的反面。 E, 否则，就不能有比较完整和正确的认识。"),
         F(3, "Đáp án: A, C, B, D, E. 我们无论认识什么事物，都必须全面地去看，不但要看到它的正面，而且要看到它的反面，否则，就不能有比较完整和正确的认识。 Dù nhận thức sự vật gì, chúng ta cũng phải nhìn toàn diện, không những thấy mặt phải mà còn phải thấy mặt trái, nếu không thì không thể có nhận thức tương đối đầy đủ và đúng đắn. Mẹo: 无论 đi với 都, 不但 đi với 而且, còn 否则 luôn đứng cuối để nêu hậu quả.")])

add("bullets", section="Luyện tập 练习", title="Mở rộng 扩展: từ vựng giao thông và nông nghiệp", reveal=True, size=34,
    items=["## Giao thông 交通",
           "工具: 轮船 tàu thủy · 路桥: 隧道 đường hầm · 立交桥 cầu vượt",
           "Động từ: 航行 đi tàu, bay · 航天 du hành vũ trụ · 失事 gặp nạn · 托运 gửi hàng, ký gửi",
           "## Nông nghiệp: 灌溉 tưới tiêu · 化肥 phân hóa học · 水利 thủy lợi · 畜牧 chăn nuôi · 杂交 lai giống",
           "(1) 这个地区大面积种植了___水稻，为了方便___，人们兴修___。",
           "Đáp án: 杂交 · 灌溉 · 水利",
           "(2) 草原地区可以大力发展___业。 (3) 使用___可以提高农作物单位面积的产量。",
           "Đáp án: (2) 畜牧 (3) 化肥"],
    say=["Phần mở rộng thứ hai của sách là từ vựng theo chủ đề. Chủ đề bốn của chúng ta là đi khắp thế giới, nên trước hết là từ vựng về giao thông.",
         F(0, "Sách sắp xếp các từ giao thông thành sơ đồ, gồm ba nhóm: phương tiện, đường và cầu, và các động từ liên quan."),
         F(1, "Phương tiện: 轮船, tàu thủy. Đường và cầu: 隧道, đường hầm, và 立交桥, cầu vượt nhiều tầng."),
         F(2, "Các động từ liên quan: 航行, đi tàu, đi máy bay; 航天, du hành vũ trụ; 失事, gặp tai nạn, thường nói về máy bay, tàu thuyền; và 托运, ký gửi hành lý, hàng hóa."),
         F(3, "Tiếp theo là từ vựng nông nghiệp: 灌溉, tưới tiêu; 化肥, phân bón hóa học; 水利, thủy lợi; 畜牧, chăn nuôi; và 杂交, lai giống. Hãy dùng các từ này điền vào chỗ trống."),
         F(4, "Câu một: 这个地区大面积种植了什么水稻，为了方便什么，人们兴修什么。 Vùng này trồng trên diện tích lớn lúa gì, để tiện cho việc gì, người ta xây dựng công trình gì? Các bạn thử điền nhé."),
         F(5, "Đáp án: 这个地区大面积种植了杂交水稻，为了方便灌溉，人们兴修水利。 Vùng này trồng lúa lai trên diện tích lớn, để tiện tưới tiêu, người ta xây dựng công trình thủy lợi."),
         F(6, "Câu hai: 草原地区可以大力发展什么业。 Vùng thảo nguyên có thể phát triển mạnh ngành gì? Câu ba: 使用什么可以提高农作物单位面积的产量。 Dùng gì để nâng cao sản lượng cây trồng trên một đơn vị diện tích?"),
         F(7, "Đáp án: câu hai là 畜牧: 草原地区可以大力发展畜牧业, vùng thảo nguyên có thể phát triển mạnh ngành chăn nuôi. Câu ba là 化肥: 使用化肥可以提高农作物单位面积的产量, dùng phân hóa học có thể tăng năng suất cây trồng.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 13", size=36,
    items=["Từ vựng trọng tâm: 变迁 · 一向 · 起初 · 迁徙 · 千方百计 · 问世 · 便于 · 一度 · 轰动 · 振兴 · 犹如 · 偏僻 · 风土人情 · 参谋 · 向导",
           "Ngữ pháp: 便于 (tiện cho, dễ) · 犹如 (giống như) · 和……相比 (so với…)",
           "Phân biệt: 一向 (xưa nay; từ lần gặp trước) ≠ 一度 (có một dạo; một lần)",
           "Mở rộng: câu sai về logic (逻辑不通) · từ vựng giao thông, nông nghiệp",
           "## Bài tập về nhà (运用)",
           "Viết bài ít nhất 400 chữ với đề 我最喜欢的一本旅行指南: nội dung cuốn sách và lý do bạn thích nó"],
    say=["Chúng ta cùng tổng kết bài mười ba.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 变迁，一向，起初，迁徙，千方百计，问世，便于，一度，轰动，振兴，犹如，偏僻，风土人情，参谋，向导. Và đừng quên những từ dễ nhầm như 趣味，人士，产业，预算，向导."),
         F(1, "Về ngữ pháp: 便于 là động từ, nghĩa là tiện cho, phía sau thường là động từ. 犹如 nghĩa là giống như, dùng trong văn viết, hay đi với 般. 和……相比 dùng để so sánh, trọng tâm là phần miêu tả sự vật đang được nói đến."),
         F(2, "Về phân biệt từ: 一向 là xưa nay vẫn vậy, còn dùng để hỏi thăm từ lần gặp trước; 一度 là có một dạo trong quá khứ, và còn là số lượng từ trong 一年一度."),
         F(3, "Về phần mở rộng: câu sai về logic gồm dùng sai từ liên kết, ý trước sau mâu thuẫn, khái niệm bao hàm lẫn nhau, phán đoán không thành lập, và phủ định hai lần. Ngoài ra, chúng ta làm quen với từ vựng giao thông và nông nghiệp."),
         F(5, "Bài tập về nhà, theo phần vận dụng của sách: các bạn có hay đi du lịch không, có hay dùng cẩm nang du lịch không? Hãy tham khảo bài khóa, viết một bài ít nhất bốn trăm chữ với đề 我最喜欢的一本旅行指南, cuốn cẩm nang du lịch tôi thích nhất. Nói rõ cuốn sách có những nội dung gì, và vì sao bạn thích nó. Nhớ thử dùng 便于，犹如，和……相比 trong bài viết nhé."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Chúc các bạn sẽ có nhiều chuyến đi thật vui, với một cuốn cẩm nang thật tốt trong tay. Hẹn gặp lại các bạn ở bài mười bốn: 背着电饭锅拍北极, Vác nồi cơm điện đi chụp ảnh Bắc Cực. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Thượng) – Bài 13: 从旅游指南看世事变迁 (Nhìn thế sự đổi thay qua trang sách cẩm nang du lịch)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    # Thứ tự có ý nghĩa: cụm dài chứa 便于 phải đứng trước 便于.
    "tts_replace": {"为便于": "位便于",          # wèi
                    "便于": "变于",              # biànyú
                    "为游客": "位游客",          # wèi
                    "为孩子": "位孩子",          # wèi
                    "锁定为": "锁定维",          # wéi
                    "为题": "维题",              # 以……为题 wéi
                    "若干": "若甘",              # ruògān
                    "困难重重": "困难虫虫",      # chóngchóng
                    "范围地方便": "范围的方便",  # dì → de (tránh đọc thành 地方 dìfang)
                    "背包": "杯包",              # bēibāo
                    "背着": "杯着",              # bēizhe
                    "待在": "呆在",              # dāi
                    "适当": "适荡",              # shìdàng
                    "声调": "声掉",              # shēngdiào
                    "调整": "条整",              # tiáozhěng
                    "角色": "决色",              # juésè
                    "好客": "浩客",              # hàokè
                    "乐谱": "月谱",              # yuèpǔ
                    "种植": "众植",              # zhòngzhí
                    "兴修": "星修",              # xīngxiū
                    "畜牧": "蓄牧"},             # xùmù
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai13.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
