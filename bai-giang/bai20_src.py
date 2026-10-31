#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Thượng) – Bài 20 «金鸡窝». Chạy để sinh bai20.json."""
import json
import os

TAG = "HSK 6 (Thượng) · Bài 20 · 金鸡窝"
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
    zh="金鸡窝", py="Jīn jī wō",
    vi="Bài 20: Ổ gà vàng",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Thượng.",
         "Hôm nay chúng ta học bài hai mươi: 金鸡窝。 Nghĩa là: Ổ gà vàng.",
         "Đây là bài cuối cùng của Chủ đề năm, 美丽家园, Quê hương xinh đẹp, và cũng là bài cuối cùng của quyển Thượng. Bài khóa là một truyền thuyết dân gian ở làng quê Trung Quốc: bên bờ ao có một tảng đá hình ổ gà, và đằng sau nó là câu chuyện về một đàn gà con biến thành vàng.",
         "Câu chuyện mang một lời răn rất sâu sắc: làm người đừng tham lam, thứ gì không phải của mình thì đừng tranh giành. Nghe xong, có lẽ các bạn sẽ nhớ ngay đến truyện cổ tích Cây khế của Việt Nam đấy."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài khóa: truyền thuyết về tảng đá ổ gà vàng và lời răn của nó",
           "Nắm vững 51 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: liên từ 况且, tính từ 大 nhấn mạnh thời điểm, 倒不如",
           "Phân biệt hai phó từ 将近 và 将要",
           "Mở rộng: tám danh từ qua hình ảnh (皮革、钻石、哨、启事……)"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa: truyền thuyết về tảng đá ổ gà vàng, và bài học làm người mà nó gửi gắm."),
         F(1, "Thứ hai, nắm vững năm mươi mốt từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học ba điểm ngữ pháp: liên từ 况且, nghĩa là hơn nữa, vả lại; tính từ 大 đứng trước từ chỉ thời gian để nhấn mạnh, như 大冬天的; và cấu trúc 倒不如, nghĩa là chẳng thà."),
         F(3, "Thứ tư, phân biệt hai phó từ rất dễ nhầm: 将近 và 将要."),
         F(4, "Thứ năm, phần mở rộng: làm quen với tám danh từ qua hình ảnh, như 皮革，钻石，启事，炊烟."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Khởi động 1: Nhìn tranh, chọn từ điền vào chỗ trống", reveal=True, size=38,
    items=["## Từ cho sẵn: 母鸡 · 鸡仔 (zǎi) · 鸡窝 (wō) · 找食 · 跟随",
           "___旁的草地上，一只___正带着一群小___四处___吃，那些小鸡___妈妈走来走去，可爱极了。",
           "Đáp án: 鸡窝 · 母鸡 · 鸡仔 · 找食 · 跟随",
           "鸡窝旁的草地上，一只母鸡正带着一群小鸡仔四处找食吃，那些小鸡跟随妈妈走来走去，可爱极了。"],
    say=["Chúng ta bắt đầu bằng phần khởi động. Trong sách có một bức tranh: một con gà mẹ đang dẫn một đàn gà con đi trên bãi cỏ. Đề bài yêu cầu dựa vào bức tranh, chọn từ thích hợp điền vào đoạn văn ngắn.",
         F(0, "Có năm từ: 母鸡, gà mái; 鸡仔, gà con, chữ thứ hai đọc là zǎi; 鸡窝, ổ gà, chữ thứ hai đọc là wō; 找食, kiếm ăn; và 跟随, đi theo."),
         F(1, "Đoạn văn như sau: 什么旁的草地上，一只什么正带着一群小什么四处什么吃，那些小鸡什么妈妈走来走去，可爱极了。 Các bạn tạm dừng video và điền thử nhé."),
         F(2, "Đáp án: 鸡窝，母鸡，鸡仔，找食，跟随."),
         F(3, "Cả đoạn là: 鸡窝旁的草地上，一只母鸡正带着一群小鸡仔四处找食吃，那些小鸡跟随妈妈走来走去，可爱极了。 Trên bãi cỏ cạnh ổ gà, một con gà mái đang dẫn một đàn gà con đi kiếm ăn khắp nơi, lũ gà con theo mẹ đi tới đi lui, đáng yêu vô cùng. Hình ảnh này sẽ xuất hiện ngay trong bài khóa đấy.")])

add("bullets", section="Khởi động 热身", title="Khởi động 2: Học từ theo yếu tố cấu tạo: 得 và 远", size=38,
    items=["## 得 (đắc, dé): được, đạt được",
           "得知 được biết · 得到 nhận được · 得分 ghi điểm · 得力 đắc lực · 得空 rảnh rỗi · 得救 được cứu · 得胜 thắng lợi",
           "得闲 có thời gian rảnh · 难得 hiếm có · 取得 giành được · 获得 thu được · 赢得 giành được · 求之不得 cầu còn không được · 一举两得 một công đôi việc",
           "## 远 (viễn): xa",
           "久远 xa xưa · 长远 lâu dài · 深远 sâu xa · 遥远 xa xôi · 永远 mãi mãi · 远古 thời xa xưa · 远见 tầm nhìn xa",
           "源远流长 nguồn xa dòng dài, lâu đời · 为期不远 chẳng còn bao lâu nữa"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo, rất có lợi cho người Việt.",
         F(0, "Nhóm thứ nhất là các từ có chữ Hán Việt là đắc, đọc là dé, như trong 得到. Chữ này nghĩa là được, đạt được."),
         F(1, "得知，得到，得分，得力，得空，得救，得胜。 Tức là: được biết, nhận được, ghi điểm, đắc lực, rảnh rỗi, được cứu, thắng lợi. Từ 得知 có trong bài khóa: 这才得知那个久远的传说, lúc ấy mới biết được truyền thuyết xa xưa kia."),
         F(2, "得闲，难得，取得，获得，赢得，求之不得，一举两得。 Tức là: có thời gian rảnh, hiếm có, giành được, thu được, giành được, cầu còn không được, và một công đôi việc."),
         F(3, "Nhóm thứ hai có chữ 远, Hán Việt là viễn, nghĩa là xa, như trong viễn cảnh, viễn thông."),
         F(4, "久远，长远，深远，遥远，永远，远古，远见。 Tức là: xa xưa, lâu dài, sâu xa, xa xôi, mãi mãi, thời thượng cổ, và tầm nhìn xa. Từ 久远 cũng có trong câu bài khóa vừa nhắc."),
         F(5, "源远流长，为期不远。 Tức là: nguồn xa dòng dài, chỉ truyền thống lâu đời; và chẳng còn bao lâu nữa.")])

add("bullets", section="Khởi động 热身", title="Khởi động 2: Học từ theo yếu tố cấu tạo: 金 và 壮", size=38,
    items=["## 金 (kim): vàng, kim loại; tiền bạc",
           "金子 vàng · 金矿 mỏ vàng · 金块 cục vàng · 金条 thỏi vàng · 黄金 hoàng kim · 纯金 vàng ròng · 金钱 tiền bạc · 美金 đô la Mỹ",
           "资金 vốn · 礼金 tiền mừng · 租金 tiền thuê · 押金 tiền đặt cọc · 奖金 tiền thưởng · 现金 tiền mặt · 金融 tài chính",
           "## 壮 (tráng): khỏe mạnh, cường tráng",
           "身强力壮 khỏe mạnh vạm vỡ · 壮大 lớn mạnh · 壮实 rắn chắc · 粗壮 to khỏe · 健壮 tráng kiện",
           "精壮 khỏe mạnh lanh lợi · 少壮 trẻ khỏe · 壮年 tráng niên · 茁壮 khỏe mạnh, lớn nhanh · 兵强马壮 quân hùng tướng mạnh"],
    say=[F(0, "Nhóm thứ ba có chữ 金, Hán Việt là kim, nghĩa là vàng, kim loại, và mở rộng ra là tiền bạc."),
         F(1, "金子，金矿，金块，金条，黄金，纯金，金钱，美金。 Tức là: vàng, mỏ vàng, cục vàng, thỏi vàng, hoàng kim, vàng ròng, tiền bạc, và đô la Mỹ. Trong bài khóa, gà con biến thành 一块金子, một cục vàng."),
         F(2, "资金，礼金，租金，押金，奖金，现金，金融。 Tức là: vốn, tiền mừng, tiền thuê, tiền đặt cọc, tiền thưởng, tiền mặt, và tài chính. Ở nhóm này, chữ kim mang nghĩa tiền bạc."),
         F(3, "Nhóm cuối cùng có chữ 壮, Hán Việt là tráng, nghĩa là khỏe mạnh, như trong cường tráng, tráng sĩ."),
         F(4, "身强力壮，壮大，壮实，粗壮，健壮。 Tức là: khỏe mạnh vạm vỡ, lớn mạnh, rắn chắc, to khỏe, tráng kiện. Bài khóa có câu 一个身强力壮的小伙子, một chàng trai khỏe mạnh vạm vỡ."),
         F(5, "精壮，少壮，壮年，茁壮，兵强马壮。 Tức là: khỏe mạnh lanh lợi, trẻ khỏe, tuổi tráng niên, lớn nhanh khỏe mạnh, và quân hùng tướng mạnh."),
         "Các bạn thấy không, chỉ cần nắm nghĩa của một chữ gốc, ta có thể đoán được nghĩa của cả một nhóm từ. Hãy áp dụng cách này khi học từ mới nhé."])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("窝", "wō", "oa", "danh từ", "ổ, tổ (chim, thú, côn trùng)", "树上有一个鸟窝。", "Trên cây có một tổ chim.",
     "Danh từ, nghĩa là ổ, tổ của chim, thú hay côn trùng, như 鸟窝, tổ chim; 鸡窝, ổ gà. 窝 còn làm lượng từ cho một lứa con vật: 一窝小鸡, một đàn gà con cùng lứa. Tên bài 金鸡窝 chính là ổ gà vàng."),
    ("畔", "pàn", "bạn", "danh từ", "bờ, bên (sông, hồ)", "我们在湖畔散步。", "Chúng tôi đi dạo bên bờ hồ.",
     "Danh từ, nghĩa là bờ, bên cạnh sông, hồ, ao, mang màu sắc văn viết. Hay gặp 湖畔，河畔，池塘畔. Chú ý: Hán Việt là bạn, nhưng không liên quan gì đến bạn bè."),
    ("椭圆", "tuǒyuán", "thỏa viên", "danh từ", "hình bầu dục, hình elip", "鸡蛋是椭圆形的。", "Quả trứng gà có hình bầu dục.",
     "Danh từ, nghĩa là hình bầu dục, hình elip. Thường nói 椭圆形. Chữ 圆 là tròn, còn 椭圆 là tròn dẹt, thuôn dài."),
    ("外表", "wàibiǎo", "ngoại biểu", "danh từ", "bề ngoài, mặt ngoài", "不能只看一个人的外表。", "Không thể chỉ nhìn vẻ bề ngoài của một người.",
     "Danh từ, nghĩa là bề ngoài, vẻ ngoài, dùng cho cả người lẫn đồ vật. Trong bài, 金鸡窝外表有些古怪 là bề ngoài ổ gà vàng có phần kỳ lạ."),
    ("镶嵌", "xiāngqiàn", "tương khảm", "động từ", "khảm, nạm, dát", "这块手表上镶嵌着几颗小宝石。", "Trên chiếc đồng hồ này có nạm mấy viên đá quý nhỏ.",
     "Động từ, nghĩa là khảm, nạm, gắn một vật nhỏ vào trong một vật khác. Chữ 嵌 Hán Việt là khảm, chính là chữ khảm trong khảm xà cừ."),
    ("坚硬", "jiānyìng", "kiên ngạnh", "tính từ", "cứng, rắn", "这种石头非常坚硬。", "Loại đá này cực kỳ cứng.",
     "Tính từ, nghĩa là cứng, rắn, thường nói về đồ vật như đá, sắt, vỏ cây. Trái nghĩa là 柔软, mềm mại."),
    ("工艺品", "gōngyìpǐn", "công nghệ phẩm", "danh từ", "hàng mỹ nghệ, đồ thủ công mỹ nghệ", "这些竹子做的工艺品很受游客欢迎。", "Những món đồ mỹ nghệ làm bằng tre này rất được du khách ưa chuộng.",
     "Danh từ, nghĩa là hàng mỹ nghệ. Cẩn thận, đây là từ dễ nhầm: Hán Việt là công nghệ phẩm, nhưng không phải sản phẩm công nghệ cao, mà là đồ thủ công đẹp, dùng để trang trí hay làm quà."),
    ("美观", "měiguān", "mỹ quan", "tính từ", "đẹp, đẹp mắt", "这套家具既美观又实用。", "Bộ đồ nội thất này vừa đẹp mắt vừa tiện dụng.",
     "Tính từ, nghĩa là đẹp mắt, nói về hình thức của đồ vật, nhà cửa, không dùng để khen người đẹp. Mẫu hay gặp: 美观大方，美观实用."),
    ("别致", "biézhì", "biệt trí", "tính từ", "độc đáo, mới lạ", "她的衣服样式很别致。", "Kiểu dáng quần áo của cô ấy rất độc đáo.",
     "Tính từ, nghĩa là độc đáo, mới lạ, khác thường mà đẹp, thường nói về kiểu dáng, cách bày trí. Trong bài, 美观别致 là vừa đẹp mắt vừa độc đáo."),
    ("浸泡", "jìnpào", "tẩm phao", "động từ", "ngâm, nhúng", "豆子要先在水里浸泡一夜。", "Đậu phải ngâm trong nước một đêm trước đã.",
     "Động từ, nghĩa là ngâm lâu trong nước hay chất lỏng. Âm tiết thứ hai đọc thanh bốn. Trong bài, 把脚浸泡在水里 là ngâm chân xuống nước."),
    ("责怪", "zéguài", "trách quái", "động từ", "trách móc, trách mắng", "这件事不能责怪孩子。", "Chuyện này không thể trách đứa trẻ.",
     "Động từ, nghĩa là trách móc, đổ lỗi cho ai đó. Mức độ nhẹ hơn 批评, phê bình."),
    ("嗨", "hēi", "hải", "thán từ", "này, ấy, nè, ơ", "嗨，你怎么还在这儿？", "Này, sao cậu vẫn còn ở đây?",
     "Thán từ, dùng để gọi, nhắc nhở hoặc tỏ ý ngạc nhiên, giống này, ơ trong tiếng Việt. Sách ghi âm hēi, đọc giống chữ 嘿. Trong bài, các cụ già trách bọn trẻ: 嗨，坐在金鸡窝上，想干吗呀！"),
    ("祖父", "zǔfù", "tổ phụ", "danh từ", "ông nội", "我的祖父今年九十岁了。", "Ông nội tôi năm nay chín mươi tuổi rồi.",
     "Danh từ, nghĩa là ông nội, văn viết; khẩu ngữ gọi là 爷爷. Còn ông ngoại là 外祖父, khẩu ngữ gọi là 姥爷 hoặc 外公. Trong bài, 姥爷祖父的祖父 là ông nội của ông nội của ông ngoại, tức là tổ tiên rất xa."),
    ("废寝忘食", "fèiqǐn-wàngshí", "phế tẩm vong thực", "thành ngữ", "quên ăn quên ngủ", "他废寝忘食地研究这个问题。", "Anh ấy quên ăn quên ngủ để nghiên cứu vấn đề này.",
     "Thành ngữ. 废 là bỏ, 寝 là ngủ, 忘 là quên, 食 là ăn: bỏ ngủ quên ăn, chỉ sự chăm chỉ, chuyên tâm cao độ. Giống hệt câu quên ăn quên ngủ của tiếng Việt."),
    ("勤俭", "qínjiǎn", "cần kiệm", "tính từ", "cần kiệm, cần cù tiết kiệm", "勤俭是中华民族的传统美德。", "Cần kiệm là đức tính truyền thống của dân tộc Trung Hoa.",
     "Tính từ, nghĩa là cần cù và tiết kiệm, âm Hán Việt và nghĩa giống hệt tiếng Việt. Hay gặp 勤俭节约，勤俭持家. Trong bài, 勤劳加勤俭 là cần cù lại thêm tiết kiệm."),
    ("富裕", "fùyù", "phú dụ", "tính từ", "giàu có, sung túc", "这几年村里的生活越来越富裕了。", "Mấy năm nay cuộc sống trong làng ngày càng sung túc.",
     "Tính từ, nghĩa là giàu có, sung túc, thường nói về đời sống, gia đình, một vùng đất. Trái nghĩa là 贫穷, nghèo khó."),
    ("农历", "nónglì", "nông lịch", "danh từ", "âm lịch", "中秋节是农历八月十五。", "Tết Trung thu là ngày rằm tháng tám âm lịch.",
     "Danh từ, nghĩa là âm lịch, lịch nhà nông. Tết Nguyên đán, Tết Trung thu đều tính theo âm lịch. Trong bài, 农历年将近 là sắp đến Tết âm lịch."),
    ("将近", "jiāngjìn", "tương cận", "phó từ", "gần, sắp tới, gần tới", "他在这里工作了将近十年。", "Anh ấy đã làm việc ở đây gần mười năm.",
     "Phó từ, nghĩa là gần tới, sắp đến, về thời gian hoặc số lượng. Lát nữa chúng ta sẽ phân biệt kỹ 将近 với 将要."),
    ("况且", "kuàngqiě", "huống thả", "liên từ", "hơn nữa, vả lại", "天太晚了，况且还下着雨，你就别走了。", "Trời đã khuya lắm rồi, vả lại còn đang mưa, cậu đừng về nữa.",
     "Liên từ, nghĩa là hơn nữa, vả lại, dùng để bổ sung thêm một lý do. Đây là điểm ngữ pháp thứ nhất của bài."),
    ("乌黑", "wūhēi", "ô hắc", "tính từ", "đen nhánh, đen sẫm, đen sì", "她有一头乌黑的长发。", "Cô ấy có mái tóc dài đen nhánh.",
     "Tính từ, nghĩa là đen nhánh, đen sẫm. Chữ 乌 vốn là con quạ, loài chim màu đen. Có thể lặp lại thành 乌黑乌黑 để nhấn mạnh, như trong bài: 乌黑乌黑的身子."),
    ("跟随", "gēnsuí", "cân tùy", "động từ", "đi theo, theo sau", "小狗一直跟随着主人。", "Chú chó nhỏ cứ đi theo chủ mãi.",
     "Động từ, nghĩa là đi theo sau. Trong bài, 跟随着母鸡 là lũ gà con lẽo đẽo theo gà mẹ."),
    ("寻觅", "xúnmì", "tầm mịch", "động từ", "tìm kiếm", "他在人群中寻觅着朋友的身影。", "Anh ấy tìm kiếm bóng dáng người bạn giữa đám đông.",
     "Động từ, nghĩa là tìm kiếm, văn viết, giống 寻找. Chữ 觅 cũng là tìm, như trong 觅食, kiếm ăn."),
    ("颇", "pō", "phả", "phó từ", "rất, khá, có phần", "这本书颇受年轻人欢迎。", "Cuốn sách này khá được giới trẻ ưa chuộng.",
     "Phó từ, nghĩa là rất, khá, văn viết. Hay gặp 颇感，颇为，颇受. Trong bài, 颇感诧异 là cảm thấy khá kinh ngạc."),
    ("分明", "fēnmíng", "phân minh", "phó từ", "rõ ràng là, hiển nhiên", "这分明是你的错，你怎么不承认？", "Đây rõ ràng là lỗi của cậu, sao cậu không thừa nhận?",
     "Phó từ, nghĩa là rõ ràng là, hiển nhiên là, thường dùng khi người nói thấy bất bình. Cẩn thận: tiếng Việt phân minh thường là rạch ròi, như công tư phân minh; còn phó từ 分明 là rõ ràng là. Nó cũng làm tính từ, nghĩa là rõ ràng: 黑白分明, trắng đen rõ ràng."),
    ("隐蔽", "yǐnbì", "ẩn tế", "động từ", "ẩn nấp, che giấu", "士兵们隐蔽在树林里。", "Những người lính ẩn nấp trong rừng cây.",
     "Động từ, nghĩa là ẩn nấp, che giấu để người khác không nhìn thấy. Cũng làm tính từ, nghĩa là kín đáo: 这个地方很隐蔽."),
    ("扎", "zhā", "trát", "động từ", "chui vào, lủi vào, lặn; đâm", "小鸡一下子扎进了草丛里。", "Chú gà con chui tọt vào bụi cỏ.",
     "Động từ, ở đây đọc thanh một, nghĩa là chui, lủi vào; cũng có nghĩa là đâm, châm, như 扎针, châm kim. Trong bài, 跑着往干草丛里扎 là chạy lủi vào bụi cỏ khô."),
    ("砖", "zhuān", "chuyên", "danh từ", "gạch", "这座房子是用红砖盖的。", "Ngôi nhà này được xây bằng gạch đỏ.",
     "Danh từ, nghĩa là viên gạch. Lượng từ là 块: 一块砖, một viên gạch."),
    ("拣", "jiǎn", "giản", "động từ", "lượm, nhặt", "他从地上拣起了一块石头。", "Anh ấy nhặt một hòn đá dưới đất lên.",
     "Động từ, nghĩa là nhặt, lượm, giống 捡. Ngoài ra còn nghĩa là chọn lựa. Trong bài, 顺手拣起一块砖 là tiện tay nhặt một viên gạch."),
    ("撇", "piě", "phiết", "động từ", "quăng, ném", "他把石头撇进了河里。", "Anh ấy quăng hòn đá xuống sông.",
     "Động từ, ở đây đọc thanh ba, nghĩa là quăng, ném. Nét phẩy trong chữ Hán cũng gọi là 一撇. Trong bài, 拣起一块砖撇过去 là nhặt viên gạch ném qua."),
    ("砸", "zá", "tạp", "động từ", "đập, đánh, nện; ném trúng", "小心，别让石头砸到脚。", "Cẩn thận, đừng để hòn đá rơi trúng chân.",
     "Động từ, nghĩa là dùng vật nặng đập, nện vào, hoặc ném trúng. Trong bài, 一下砸中了一只小鸡 là ném một phát trúng ngay một chú gà con. Khẩu ngữ còn có nghĩa làm hỏng việc: 事情办砸了."),
    ("膝盖", "xīgài", "tất cái", "danh từ", "đầu gối", "他摔倒了，膝盖受了伤。", "Anh ấy bị ngã, đầu gối bị thương.",
     "Danh từ, nghĩa là đầu gối. Chữ 膝 là gối, chữ 盖 là cái nắp, tức là phần xương như cái nắp ở đầu gối."),
    ("枝", "zhī", "chi", "danh từ", "nhánh cây, cành cây", "树枝上站着几只小鸟。", "Trên cành cây có mấy chú chim nhỏ đậu.",
     "Danh từ, nghĩa là cành cây, thường nói 树枝. Cũng là lượng từ cho hoa có cành: 一枝花. Hán Việt là chi, như trong kim chi ngọc diệp, cành vàng lá ngọc."),
    ("拐杖", "guǎizhàng", "quải trượng", "danh từ", "gậy chống, cái nạng", "爷爷走路需要拄拐杖。", "Ông nội đi lại cần chống gậy.",
     "Danh từ, nghĩa là gậy chống, cái nạng. Động từ đi kèm là 拄, chống: 拄拐杖."),
    ("拄", "zhǔ", "trụ", "động từ", "chống (gậy)", "老人拄着拐杖慢慢地走。", "Ông cụ chống gậy chầm chậm bước đi.",
     "Động từ, nghĩa là chống gậy để đỡ thân người. Gần như chỉ đi với gậy: 拄拐杖，拄着棍子."),
    ("瘸", "qué", "qua", "động từ", "đi khập khiễng, cà nhắc, què", "他的腿瘸了，走路一瘸一拐的。", "Chân anh ấy bị què, đi lại tập tễnh.",
     "Động từ, nghĩa là què, đi khập khiễng. Cụm cố định 一瘸一拐 là đi cà nhắc, tập tễnh, như trong bài: 一瘸一拐地回了家."),
    ("挖掘", "wājué", "oạt quật", "động từ", "đào, khai quật", "考古学家在这里挖掘出很多古代文物。", "Các nhà khảo cổ đã khai quật được rất nhiều cổ vật ở đây.",
     "Động từ, nghĩa là đào, khai quật. Nghĩa bóng là khai thác, tìm ra: 挖掘潜力, khai thác tiềm năng."),
    ("坑", "kēng", "khanh", "danh từ", "lỗ, hố", "路上有个大坑，开车要小心。", "Trên đường có một cái hố lớn, lái xe phải cẩn thận.",
     "Danh từ, nghĩa là hố, chỗ trũng trên mặt đất. Khẩu ngữ ngày nay còn dùng làm động từ, nghĩa là lừa gạt: 坑人."),
    ("发炎", "fāyán", "phát viêm", "động từ", "sưng, bị viêm", "伤口发炎了，最好去医院看看。", "Vết thương bị viêm rồi, tốt nhất là đi bệnh viện khám.",
     "Động từ, nghĩa là bị viêm, sưng tấy. Âm Hán Việt phát viêm, nghĩa giống hệt tiếng Việt."),
    ("咋", "zǎ", "trách", "đại từ", "sao, thế nào, tại sao", "你咋才来呀？", "Sao giờ cậu mới đến?",
     "Đại từ nghi vấn, khẩu ngữ phương Bắc, nghĩa là sao, thế nào, giống 怎么. Hay gặp 咋办, làm sao bây giờ; 咋样, thế nào. Trong bài, 咋能光躺在床上呢 là sao có thể chỉ nằm trên giường được."),
    ("侥幸", "jiǎoxìng", "kiểu hạnh", "tính từ", "may, hên, may mắn", "他侥幸地躲过了这场车祸。", "Anh ấy may mắn thoát được vụ tai nạn xe này.",
     "Tính từ, nghĩa là may mắn tránh được điều xấu, nhờ may chứ không phải nhờ sức mình. Cụm hay gặp: 侥幸心理, tâm lý cầu may. Trong bài, 还算侥幸 là cũng còn may."),
    ("滋味", "zīwèi", "tư vị", "danh từ", "mùi vị; cảm giác", "失败的滋味很不好受。", "Mùi vị thất bại thật khó chịu.",
     "Danh từ, nghĩa gốc là mùi vị món ăn, nghĩa bóng là cảm giác, nỗi niềm. Cẩn thận, từ dễ nhầm: tiếng Việt tư vị là thiên vị, bênh người quen; còn 滋味 là mùi vị. Trong bài, 尝到了久病不愈的滋味 là nếm trải cảm giác bệnh lâu không khỏi."),
    ("逢", "féng", "phùng", "động từ", "gặp, gặp gỡ", "每逢过年，我们全家都会去看望姥姥。", "Mỗi dịp Tết, cả nhà tôi đều đi thăm bà ngoại.",
     "Động từ, nghĩa là gặp, văn viết. Hay gặp 每逢, mỗi khi, mỗi dịp; 逢人就说, gặp ai cũng nói. Hán Việt là phùng, như trong tương phùng, trùng phùng."),
    ("得不偿失", "débùchángshī", "đắc bất thường thất", "thành ngữ", "được một mất mười, được ít mất nhiều", "为了赚钱累坏了身体，真是得不偿失。", "Vì kiếm tiền mà làm hỏng cả sức khỏe, thật là được ít mất nhiều.",
     "Thành ngữ. Chữ đầu là cái được, 偿 là bù đắp, chữ cuối là cái mất: cái được không bù nổi cái mất, tức là được ít mất nhiều. Sách dịch là được một mất mười."),
    ("宁肯", "nìngkěn", "ninh khẳng", "phó từ", "thà, thà rằng", "我宁肯走路，也不坐他的车。", "Tôi thà đi bộ chứ không ngồi xe của anh ta.",
     "Phó từ, nghĩa là thà, thà rằng, giống 宁可 và 宁愿. Chú ý chữ đầu đọc thanh bốn. Mẫu hay gặp: 宁肯……也不……, thà… chứ không…."),
    ("告诫", "gàojiè", "cáo giới", "động từ", "khuyên răn, khuyên bảo, răn đe", "父亲常常告诫我做人要诚实。", "Bố thường răn dạy tôi làm người phải trung thực.",
     "Động từ, nghĩa là khuyên răn, răn dạy, thường là người trên nói với người dưới. Chữ 诫 là răn, như trong 十诫, mười điều răn."),
    ("欲望", "yùwàng", "dục vọng", "danh từ", "dục vọng, sự ham muốn", "人的欲望是无穷的。", "Ham muốn của con người là vô cùng tận.",
     "Danh từ, nghĩa là sự ham muốn. Chú ý: tiếng Việt dục vọng thường mang sắc thái xấu; còn 欲望 trong tiếng Trung trung tính hơn, chỉ mọi mong muốn nói chung, như 购买欲望, ham muốn mua sắm."),
    ("贪婪", "tānlán", "tham lam", "tính từ", "tham lam", "他贪婪地看着桌上的钱。", "Hắn nhìn chằm chằm vào đống tiền trên bàn một cách tham lam.",
     "Tính từ, nghĩa là tham lam, muốn có thật nhiều mà không biết đủ. Âm Hán Việt và nghĩa giống hệt tiếng Việt."),
    ("争夺", "zhēngduó", "tranh đoạt", "động từ", "giành giật, tranh giành", "两支球队正在争夺冠军。", "Hai đội bóng đang tranh chức vô địch.",
     "Động từ, nghĩa là tranh giành, giành giật một thứ gì đó. Trong bài: 东西不是你的就不要去争夺, thứ gì không phải của mình thì đừng tranh giành."),
    ("贪污", "tānwū", "tham ô", "động từ", "tham nhũng, tham ô", "他因为贪污被判了刑。", "Ông ta bị kết án vì tội tham ô.",
     "Động từ, nghĩa là tham ô, lợi dụng chức vụ để lấy của công làm của riêng. Âm Hán Việt giống hệt tiếng Việt."),
    ("贿赂", "huìlù", "hối lộ", "động từ", "hối lộ, đút lót", "他想贿赂法官，结果被抓了。", "Hắn định hối lộ thẩm phán, kết quả là bị bắt.",
     "Động từ, nghĩa là hối lộ, đút lót. Cũng làm danh từ, chỉ của đút lót: 接受贿赂, nhận hối lộ."),
    ("不择手段", "bùzé-shǒuduàn", "bất trạch thủ đoạn", "thành ngữ", "bất chấp mọi thủ đoạn, dùng mọi thủ đoạn", "他为了成功不择手段。", "Hắn bất chấp mọi thủ đoạn để thành công.",
     "Thành ngữ. 择 là chọn, 手段 là thủ đoạn, cách thức: không cần lựa chọn cách làm, tức là dùng mọi cách, kể cả cách xấu. Luôn mang nghĩa chê."),
]

add("bullets", chapter="Từ mới (51 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 20 có 51 từ mới, chia thành 17 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 扎 (zhā) · 撇 (piě) · 嗨 (hēi) · 宁肯 (nìng) · 咋 (zǎ)",
           "Từ dễ nhầm: 工艺品 · 分明 · 滋味 · 欲望"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có năm mươi mốt từ, thầy chia thành mười bảy nhóm nhỏ, mỗi nhóm ba từ. Bài khóa kể chuyện dân gian nên có rất nhiều động từ chỉ hành động cụ thể, như nhặt, ném, đập, chống gậy.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số chữ có nhiều cách đọc, các bạn cần chú ý cách đọc trong bài, như 宁肯 và 咋样. Thầy sẽ nhắc khi gặp."),
         F(4, "Ngoài ra, có mấy từ Hán Việt rất dễ hiểu nhầm, như 工艺品，分明，滋味，欲望. Nghĩa của chúng trong tiếng Trung khác với tiếng Việt, các bạn nhớ nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

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
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung nếu khác])
P = [
    ("姥姥住的村东池塘畔有一块椭圆形的大石头。那石头中间凹陷，像个鸡窝，村里人叫它金鸡窝。",
     "Bên bờ ao phía đông ngôi làng nơi bà ngoại sống có một tảng đá lớn hình bầu dục. Giữa tảng đá lõm xuống, giống như một cái ổ gà, người trong làng gọi nó là ổ gà vàng.",
     ["姥姥 là bà ngoại, cách gọi khẩu ngữ ở miền Bắc Trung Quốc; còn 姥爷 là ông ngoại. 村东 là phía đông làng. 池塘畔 là bên bờ ao.",
      "凹陷 là lõm xuống. 叫它金鸡窝 là gọi nó là ổ gà vàng, theo mẫu 叫 cộng tân ngữ cộng tên gọi. Câu mở đầu giới thiệu ngay tên bài."]),
    ("金鸡窝外表有些古怪，红色的石头，上面镶嵌着些不同色彩、不同形状、或坚硬或不十分坚硬的小石头，像件工艺品，很是美观别致。",
     "Bề ngoài ổ gà vàng có phần kỳ lạ: đó là một tảng đá màu đỏ, trên mặt khảm những viên đá nhỏ khác màu, khác hình dạng, viên thì cứng, viên thì không cứng lắm, trông như một món đồ mỹ nghệ, rất đẹp mắt và độc đáo.",
     ["古怪 là kỳ quái, lạ lùng. 镶嵌着些小石头: chữ 些 ở đây là 一些 lược bỏ 一; tương tự 像件工艺品 là 像一件工艺品.",
      "或坚硬或不十分坚硬: cấu trúc 或A或B nghĩa là hoặc A hoặc B, mang màu sắc văn viết. 很是美观别致: 很是 nhấn mạnh, nghĩa là rất, thật là."]),
    ("我们小时候都喜欢坐在石头上，把脚浸泡在水里。老人们见了，就会责怪：“嗨，坐在金鸡窝上，想干吗呀！”",
     "Hồi nhỏ, bọn trẻ chúng tôi đều thích ngồi trên tảng đá, ngâm chân xuống nước. Các cụ già trông thấy là thế nào cũng trách: Này, ngồi lên ổ gà vàng là định làm gì hả!",
     ["把脚浸泡在水里 là câu chữ 把: đem chân ngâm xuống nước. 见了 là trông thấy. 就会责怪 là thế nào cũng trách mắng.",
      "想干吗呀 là định làm gì hả, 干吗 là làm gì, khẩu ngữ. Câu trách này gợi sự tò mò: ổ gà vàng có gì đặc biệt mà không được ngồi lên?"]),
    ("我被说得糊涂，就去问姥姥，这才得知那个久远的传说。",
     "Tôi bị nói đến mức chẳng hiểu ra sao, bèn đi hỏi bà ngoại, lúc ấy mới biết được truyền thuyết xa xưa kia.",
     ["我被说得糊涂 là câu bị động với 被 có bổ ngữ trình độ: tôi bị nói đến mức mơ hồ, chẳng hiểu gì. 糊涂 là mơ hồ, lú lẫn.",
      "这才 là đến lúc ấy mới. 得知 là được biết, văn viết. 久远的传说 là truyền thuyết xa xưa. Từ đây, câu chuyện truyền thuyết bắt đầu."]),
    ("姥爷祖父的祖父宋家有几兄弟，大家起早贪黑，废寝忘食，勤劳加勤俭，日子过得还算富裕。",
     "Ông nội của ông nội của ông ngoại tôi, tức nhà họ Tống, có mấy anh em trai. Mọi người thức khuya dậy sớm, quên ăn quên ngủ, cần cù lại thêm tiết kiệm, nên cuộc sống cũng xem như khá giả.",
     ["姥爷祖父的祖父 là ông nội của ông nội của ông ngoại, tức là tổ tiên từ rất nhiều đời trước. 宋家 là nhà họ Tống. 几兄弟 là mấy anh em trai.",
      "起早贪黑 là thức khuya dậy sớm. 勤劳加勤俭 là cần cù lại thêm tiết kiệm. 还算富裕 là cũng xem như khá giả: 还算 nghĩa là cũng được coi là, tạm coi là."]),
    ("农历年将近，宋家三祖爷早早下了地，突然看到了一窝小鸡。那小鸡仿佛刚出窝没几天，况且是乌黑乌黑的身子，可爱极了，跟随着母鸡，四处寻觅，像是在找食。",
     "Gần đến Tết âm lịch, cụ ba nhà họ Tống ra đồng từ sớm, bỗng nhìn thấy một đàn gà con. Lũ gà con dường như mới nở được vài ngày, lại thêm thân mình đen nhánh, đáng yêu vô cùng. Chúng theo sau gà mẹ, tìm kiếm khắp nơi, như đang kiếm ăn.",
     ["农历年将近 là sắp đến Tết âm lịch, 将近 đứng sau từ chỉ thời gian. 三祖爷 là cụ tổ thứ ba. 下了地 là ra đồng làm ruộng. 一窝小鸡 là một đàn gà con cùng lứa.",
      "仿佛 là dường như. 况且 bổ sung thêm lý do vì sao lũ gà đáng yêu: vừa mới nở, lại thêm thân mình đen nhánh. Đây chính là điểm ngữ pháp 况且. 四处寻觅 là tìm kiếm khắp nơi."]),
    ("三祖爷颇感诧异，大冬天的，这里离村子又远，分明不该有这么小的鸡仔呀！三祖爷去捉小鸡，小鸡想隐蔽自己，跑着往干草丛里扎。",
     "Cụ ba cảm thấy khá lạ lùng: giữa mùa đông giá rét, chỗ này lại cách làng xa, rõ ràng là không thể có gà con nhỏ như thế! Cụ ba đi bắt gà con, gà con muốn trốn, chạy lủi vào bụi cỏ khô.",
     ["颇感诧异 là cảm thấy khá kinh ngạc. 大冬天的 là giữa mùa đông, chữ 大 nhấn mạnh thời điểm: mùa đông thì lẽ ra không có gà con mới nở. Đây là điểm ngữ pháp thứ hai.",
      "分明不该有 là rõ ràng là không thể có. 鸡仔 là gà con. 隐蔽自己 là trốn đi. 往干草丛里扎 là lủi vào bụi cỏ khô."]),
    ("三祖爷顺手拣起一块砖撇过去，一下砸中了一只小鸡。小鸡就地打了个滚，瞬间变成了一块金子。",
     "Cụ ba tiện tay nhặt một viên gạch ném qua, một phát trúng ngay một chú gà con. Chú gà con lăn một vòng tại chỗ, trong nháy mắt biến thành một cục vàng.",
     ["顺手 là tiện tay. 拣起一块砖撇过去 là nhặt một viên gạch ném qua. 一下砸中 là một phát ném trúng ngay; trong từ 砸中, chữ sau đọc thanh bốn, nghĩa là trúng.",
      "就地打了个滚 là lăn một vòng ngay tại chỗ. 瞬间 là trong nháy mắt. Đây là chi tiết thần kỳ của truyền thuyết: gà con biến thành vàng."]),
    ("这时候，老母鸡急了，跳起来在三祖爷膝盖下边就是一口，三祖爷疼得要命，哼哼着，路也走不动了，只好拣个树枝当拐杖拄着，一瘸一拐地回了家。",
     "Lúc ấy, gà mẹ cuống lên, nhảy lên mổ một cái ngay dưới đầu gối cụ ba. Cụ ba đau chết đi được, rên hừ hừ, không đi nổi nữa, đành nhặt một cành cây làm gậy chống, tập tễnh trở về nhà.",
     ["就是一口 là mổ luôn một cái: 就是 nhấn mạnh hành động xảy ra ngay lập tức, dứt khoát. 疼得要命 là đau chết đi được, 要命 chỉ mức độ cực cao.",
      "哼哼着 là rên hừ hừ. 当拐杖拄着 là dùng làm gậy mà chống, chữ đầu đọc thanh bốn, nghĩa là coi như, dùng làm. 一瘸一拐 là đi cà nhắc, tập tễnh."]),
    ("回到家，三祖爷把事情跟家里人一说，大家赶到地里，可怎么也找不着那窝鸡。大家开始在附近挖掘，挖了个大坑，结果还是没有看到鸡，只是挖出了那块像鸡窝一样的大石头。",
     "Về đến nhà, cụ ba vừa kể chuyện cho người nhà nghe, mọi người liền vội chạy ra đồng, nhưng tìm thế nào cũng không thấy đàn gà kia. Mọi người bắt đầu đào bới quanh đó, đào thành một cái hố lớn, kết quả vẫn không thấy gà, chỉ đào được tảng đá lớn giống như cái ổ gà kia.",
     ["跟家里人一说: mẫu 一 cộng động từ, nghĩa là vừa nói ra thì…. 赶到地里 là vội chạy ra đồng. 怎么也找不着 là tìm thế nào cũng không thấy.",
      "挖了个大坑 là đào một cái hố lớn. 只是挖出了 là chỉ đào được. Thì ra, tảng đá ổ gà vàng có nguồn gốc như vậy."]),
    ("他们把那石头抬回村里，因为形状不规则，派不上什么用场，最后就扔在了池塘边。",
     "Họ khiêng tảng đá về làng, nhưng vì hình dạng không đều đặn, chẳng dùng được vào việc gì, cuối cùng đành vứt bên bờ ao.",
     ["抬回村里 là khiêng về làng. 形状不规则 là hình dạng không đều đặn, không vuông vức.",
      "派不上什么用场 là chẳng dùng được vào việc gì; 派用场 là đem ra dùng. 扔在了池塘边 là vứt bên bờ ao, khớp lại với câu đầu bài: tảng đá nằm bên bờ ao."]),
    ("三祖爷受伤的腿一直发炎，疼得下不了床。一个身强力壮的小伙子，咋能光躺在床上呢？三祖爷只好用那金子换了钱去看病。",
     "Cái chân bị thương của cụ ba cứ bị viêm mãi, đau đến mức không xuống giường được. Một chàng trai khỏe mạnh vạm vỡ, sao có thể chỉ nằm trên giường được? Cụ ba đành đem cục vàng ấy đổi lấy tiền để chữa bệnh.",
     ["一直发炎 là cứ bị viêm mãi. 疼得下不了床 là đau đến mức không xuống giường được. Thì ra lúc ấy cụ ba vẫn còn là một chàng trai trẻ.",
      "咋能光躺在床上呢 là câu hỏi tu từ: sao có thể chỉ nằm trên giường được? 光 ở đây là chỉ. 用那金子换了钱 là đem cục vàng đổi lấy tiền."]),
    ("还算侥幸，金子换来的钱用完了，三祖爷的腿也好了。三祖爷尝到了久病不愈的滋味，后来逢人就说，真是得不偿失，早知道这样，宁肯当初不搭理那窝小鸡。",
     "Cũng còn may, tiền đổi từ vàng vừa tiêu hết thì chân cụ ba cũng khỏi. Cụ ba đã nếm trải mùi vị bệnh lâu không khỏi, về sau gặp ai cũng nói: thật là được ít mất nhiều, sớm biết thế này, thà lúc đầu đừng thèm để ý đến đàn gà con ấy.",
     ["还算侥幸 là cũng còn may. Tiền đổi từ vàng vừa hết thì chân cũng khỏi, như thể của cải ấy vốn không thuộc về cụ, có được rồi cũng phải trả lại.",
      "久病不愈 là bệnh lâu không khỏi. 逢人就说 là gặp ai cũng kể. 宁肯当初不搭理那窝小鸡 là thà lúc đầu đừng để ý đến đàn gà con ấy; 搭理 là để ý, đáp lời."]),
    ("三祖爷的故事告诫后人，做人不要欲望太多，不要贪婪。东西不是你的就不要去争夺，就是争来，也守不住。倒不如付出一分努力，得到一分收获，过平稳和顺的日子。",
     "Câu chuyện của cụ ba răn dạy đời sau: làm người đừng có quá nhiều ham muốn, đừng tham lam. Thứ gì không phải của mình thì đừng tranh giành, cho dù có giành được, cũng chẳng giữ nổi. Chẳng thà bỏ ra một phần công sức, nhận lại một phần thành quả, sống những ngày bình ổn, êm ấm.",
     ["告诫后人 là răn dạy đời sau. 就是争来，也守不住: 就是……也…… nghĩa là cho dù… cũng…, giống 即使……也…….",
      "倒不如 nghĩa là chẳng thà, sau khi so sánh thì chọn cách này. Đây là điểm ngữ pháp thứ ba. 付出一分努力，得到一分收获 là bỏ ra bao nhiêu công sức thì nhận về bấy nhiêu thành quả. 平稳和顺 là bình ổn, êm ấm."]),
    ("后来，三祖爷的故事传了一代又一代，宋家的子孙也有做了官的，但没有人敢贪污、贿赂、不择手段，因为他们心里都有一个“金鸡窝”。",
     "Về sau, câu chuyện của cụ ba được truyền từ đời này sang đời khác. Con cháu nhà họ Tống cũng có người làm quan, nhưng không ai dám tham ô, hối lộ, hay bất chấp thủ đoạn, bởi vì trong lòng họ đều có một ổ gà vàng.",
     ["传了一代又一代 là truyền hết đời này sang đời khác. 也有做了官的 là cũng có người làm quan, cấu trúc chữ 的 thay cho danh từ chỉ người.",
      "Câu kết rất hay: 心里都有一个金鸡窝. Ổ gà vàng không còn là tảng đá nữa, mà trở thành một lời răn trong lòng mỗi người: không tham lam, không tranh giành thứ không thuộc về mình."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 金鸡窝", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 金鸡窝, dài tám trăm ba mươi mốt chữ. Bài được cải biên từ một bài viết cùng tên trên 北京青年报, báo Thanh niên Bắc Kinh, tác giả là 寒崖.",
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
    items=["## 1. 姥姥村里的人把什么称为“金鸡窝”？描述一下金鸡窝的样子。",
           "大石头、凹陷、鸟窝",
           "古怪、红色、镶嵌……小石头、像……、美观别致",
           "## 2. 讲述一下那个久远的传说：背景、时间、人物",
           "背景：宋家几兄弟、起早贪黑、废寝忘食、勤劳勤俭、日子富裕",
           "时间：农历年将近 · 人物：宋家三祖爷"],
    say=["Bài tập năm của sách yêu cầu dựa vào gợi ý để kể tóm tắt nội dung chính của bài khóa. Chúng ta cùng làm luôn nhé.",
         F(0, "Câu hỏi một: người trong làng của bà ngoại gọi cái gì là ổ gà vàng? Hãy miêu tả hình dáng của nó."),
         F(1, "Gợi ý: 大石头，凹陷，鸟窝. Tức là: đó là một tảng đá lớn, giữa lõm xuống như một cái ổ."),
         F(2, "古怪，红色，镶嵌小石头，像工艺品，美观别致. Tức là: bề ngoài kỳ lạ, màu đỏ, khảm những viên đá nhỏ, trông như đồ mỹ nghệ, đẹp mắt và độc đáo."),
         F(3, "Câu hỏi hai: kể lại truyền thuyết xa xưa ấy. Trước hết là bối cảnh, thời gian và nhân vật."),
         F(4, "Bối cảnh: 宋家几兄弟，起早贪黑，废寝忘食，勤劳勤俭，日子富裕. Nhà họ Tống có mấy anh em, chăm chỉ cần kiệm, cuộc sống khá giả."),
         F(5, "Thời gian: 农历年将近, sắp đến Tết âm lịch. Nhân vật: 宋家三祖爷, cụ ba nhà họ Tống.")])

add("bullets", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5) – phần 2", size=34,
    items=["## 事情经过 – diễn biến sự việc",
           "(1) 发现一窝小鸡 · (2) 捉小鸡，小鸡变金子 · (3) 三祖爷受伤",
           "(4) 再次找小鸡，没找到，发现大石头 · (5) 三祖爷治疗受伤的腿",
           "## 3. 这个故事给人们的启发",
           "不要欲望太多，不要贪婪 · 东西不是你的就不要去争夺"],
    say=[F(0, "Tiếp theo là diễn biến sự việc, gồm năm bước."),
         F(1, "Một: 发现一窝小鸡, phát hiện một đàn gà con. Hai: 捉小鸡，小鸡变金子, bắt gà con, gà con biến thành vàng. Ba: 三祖爷受伤, cụ ba bị gà mẹ mổ bị thương."),
         F(2, "Bốn: 再次找小鸡，没找到，发现大石头, cả nhà quay lại tìm gà, không thấy, chỉ đào được tảng đá lớn. Năm: 三祖爷治疗受伤的腿, cụ ba đem vàng đổi tiền chữa chân, tiền hết thì chân cũng khỏi."),
         F(3, "Câu hỏi ba: câu chuyện này gợi cho mọi người điều gì?"),
         F(4, "不要欲望太多，不要贪婪。 Đừng có quá nhiều ham muốn, đừng tham lam. Thứ gì không phải của mình thì đừng tranh giành. Bố cục này rất có ích khi các bạn tự kể lại bài khóa, và cũng là dàn ý cho bài tập về nhà cuối bài.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 况且", section="Ngữ pháp 注释", title="1. 况且 kuàngqiě – hơn nữa, vả lại", size=36,
    items=["Liên từ, đứng đầu vế sau: ngoài lý do đã nêu, bổ sung thêm một lý do mới",
           "Vế có 况且 thường có thêm 又、也、还",
           "那小鸡仿佛刚出窝没几天，况且是乌黑乌黑的身子，可爱极了。",
           "这套房子交通方便，附近有书店，况且房租又不贵，真是再合适不过了。",
           "……原因很简单，我在石油行业工作了20多年，有份难舍的情感，况且我也热爱自己的专业，还想有所成就。"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là liên từ 况且.",
         F(0, "况且 là liên từ, đặt ở đầu vế câu phía sau. Nó biểu thị: ngoài lý do đã nêu ở trước, còn bổ sung thêm một lý do mới. Tiếng Việt dịch là hơn nữa, vả lại, huống hồ."),
         F(1, "Trong vế có 况且, ta thường thấy thêm các phó từ 又，也，还, để nhấn mạnh ý cộng thêm."),
         F(2, "Ví dụ một, lấy từ bài khóa: 那小鸡仿佛刚出窝没几天，况且是乌黑乌黑的身子，可爱极了。 Lũ gà con dường như mới nở được vài ngày, lại thêm thân mình đen nhánh, đáng yêu vô cùng. Hai lý do cộng lại khiến chúng đáng yêu."),
         F(3, "Ví dụ hai: 这套房子交通方便，附近有书店，况且房租又不贵，真是再合适不过了。 Căn nhà này giao thông thuận tiện, gần đó có hiệu sách, vả lại tiền thuê cũng không đắt, thật là không gì hợp hơn."),
         F(4, "Ví dụ ba: 虽然这工作很苦，但我不想离开现在的岗位。原因很简单，我在石油行业工作了二十多年，有份难舍的情感，况且我也热爱自己的专业，还想有所成就。 Tuy công việc này vất vả, nhưng tôi không muốn rời vị trí hiện tại. Lý do rất đơn giản: tôi đã làm trong ngành dầu khí hơn hai mươi năm, có một tình cảm khó rời bỏ, hơn nữa tôi cũng yêu chuyên môn của mình, còn muốn đạt được thành tựu.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: chọn vị trí thích hợp cho 况且", reveal=True, size=34,
    items=["(1) A飞行员驾机到目的地时，B能见度不到500米，C大大低于规定标准，D只有4个马灯照明。（况且该机场没有夜航设备，）",
           "Đáp án: D – ……大大低于规定标准，况且该机场没有夜航设备，只有4个马灯照明。",
           "(2) 这次假期我不想去旅行了，A一来假期短，B二来车票也不好买，C我想好好休息休息，复习复习功课，D也可以在近处玩儿玩儿。（况且假期过后就是考试，）",
           "Đáp án: C – ……二来车票也不好买，况且假期过后就是考试，我想好好休息休息……",
           "(3) 毕竟已年过50，A忙了整整三天，B他突然发现自己双腿已无法站稳，C头痛欲裂，D大家赶紧把他送到了医院。（况且他原本就有心脏病，）",
           "Đáp án: A – 毕竟已年过50，况且他原本就有心脏病，忙了整整三天……"],
    say=[F(0, "Luyện tập: chọn vị trí thích hợp cho phần trong ngoặc. Câu một: 飞行员驾机到目的地时，能见度不到五百米，大大低于规定标准，只有四个马灯照明。 Phần cần đặt vào là: 况且该机场没有夜航设备. Khi phi công lái máy bay đến nơi, tầm nhìn chưa tới năm trăm mét, thấp hơn nhiều so với tiêu chuẩn, chỉ có bốn ngọn đèn bão chiếu sáng. Các bạn tạm dừng và chọn nhé."),
         F(1, "Đáp án: D. 大大低于规定标准，况且该机场没有夜航设备，只有四个马灯照明。 Tầm nhìn đã thấp, hơn nữa sân bay lại không có thiết bị bay đêm, nên chỉ có bốn ngọn đèn bão. Khó khăn thứ hai được cộng thêm vào khó khăn thứ nhất."),
         F(2, "Câu hai: 这次假期我不想去旅行了，一来假期短，二来车票也不好买，我想好好休息休息，复习复习功课，也可以在近处玩儿玩儿。 Phần cần đặt vào là: 况且假期过后就是考试. Kỳ nghỉ này tôi không muốn đi du lịch: một là kỳ nghỉ ngắn, hai là vé xe khó mua."),
         F(3, "Đáp án: C. 一来，二来, rồi 况且 bổ sung lý do thứ ba: hơn nữa nghỉ xong là thi ngay. Sau ba lý do mới đến kết luận: tôi muốn nghỉ ngơi, ôn bài."),
         F(4, "Câu ba: 毕竟已年过五十，忙了整整三天，他突然发现自己双腿已无法站稳，头痛欲裂，大家赶紧把他送到了医院。 Phần cần đặt vào là: 况且他原本就有心脏病. Dù sao ông ấy cũng đã ngoài năm mươi, bận rộn suốt ba ngày, bỗng thấy hai chân không đứng vững, đầu đau như búa bổ."),
         F(5, "Đáp án: A. 毕竟已年过五十，况且他原本就有心脏病, đã ngoài năm mươi, hơn nữa vốn có bệnh tim; hai lý do này đứng cạnh nhau, giải thích vì sao ông ấy kiệt sức sau ba ngày bận rộn.")])

add("bullets", chapter="Ngữ pháp: 大", section="Ngữ pháp 注释", title="2. 大 dà – nhấn mạnh thời điểm", size=36,
    items=["Tính từ, đứng trước một số từ chỉ mùa, thời tiết, thời gian, ngày lễ để nhấn mạnh",
           "Thường dùng mẫu 大……的, ngụ ý: vào lúc ấy lẽ ra không nên (không thể) làm việc đó",
           "他一大清早就不知道忙什么去了。",
           "大周末的，让人家多睡会儿吧。",
           "三祖爷颇感诧异，大冬天的，这里离村子又远，分明不该有这么小的鸡仔呀！",
           "Hay gặp: 大清早 · 大白天 · 大中午 · 大半夜 · 大热天 · 大冷天 · 大过年的"],
    say=["Điểm ngữ pháp thứ hai là một cách dùng rất khẩu ngữ của tính từ 大.",
         F(0, "Ở đây, 大 không có nghĩa là to lớn. Nó đứng trước một số từ chỉ mùa, thời tiết, thời gian hay ngày lễ, để nhấn mạnh thời điểm đó."),
         F(1, "Mẫu thường gặp là 大 cộng từ chỉ thời gian cộng 的, đứng ở đầu câu. Hàm ý là: vào đúng lúc ấy, lẽ ra không nên, hoặc không thể có việc như vậy."),
         F(2, "Ví dụ một: 他一大清早就不知道忙什么去了。 Mới sáng sớm tinh mơ, anh ấy đã đi đâu bận việc gì không biết. 一大清早 nhấn mạnh là còn rất sớm."),
         F(3, "Ví dụ hai: 大周末的，让人家多睡会儿吧。 Cuối tuần cơ mà, để người ta ngủ thêm chút đi. Hàm ý: cuối tuần thì không nên đánh thức người ta dậy sớm. 人家 ở đây là người nói tự chỉ mình."),
         F(4, "Ví dụ ba, lấy từ bài khóa: 三祖爷颇感诧异，大冬天的，这里离村子又远，分明不该有这么小的鸡仔呀！ Giữa mùa đông giá rét, lẽ ra không thể có gà con mới nở."),
         F(5, "Những cụm hay gặp: 大清早，大白天，大中午，大半夜，大热天，大冷天，大过年的. Ví dụ: 大白天的，开什么灯啊？ Ban ngày ban mặt thế này, bật đèn làm gì?")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: câu nào có 大 mang nghĩa khác?", reveal=True, size=38,
    items=["(1) 大晴天的，带什么雨伞呀！",
           "(2) 大年初一的，也该好好休息休息啦。",
           "(3) 哥哥比弟弟大三岁。",
           "Đáp án: Câu (3). 大 ở câu (3) là tính từ so sánh tuổi tác: lớn hơn. Câu (1), (2): 大 nhấn mạnh thời điểm.",
           "## Đặt câu thêm với 大……的",
           "Đáp án gợi ý: 大半夜的，你怎么还不睡觉？ · 大热天的，别出去跑步了。"],
    say=[F(0, "Luyện tập: trong các câu sau, chữ 大 ở câu nào mang nghĩa khác với điểm ngữ pháp vừa học? Câu một: 大晴天的，带什么雨伞呀！ Trời nắng đẹp thế này, mang ô làm gì!"),
         F(1, "Câu hai: 大年初一的，也该好好休息休息啦。 Mùng một Tết cơ mà, cũng nên nghỉ ngơi cho tử tế chứ."),
         F(2, "Câu ba: 哥哥比弟弟大三岁。 Anh trai hơn em trai ba tuổi. Các bạn tạm dừng và suy nghĩ nhé."),
         F(3, "Đáp án: câu ba. Ở câu ba, 大 là tính từ chỉ tuổi lớn hơn, dùng trong câu so sánh với 比. Còn ở câu một và câu hai, 大 đứng trước từ chỉ thời gian, nhấn mạnh thời điểm: trời nắng thì không cần ô, mùng một Tết thì nên nghỉ."),
         F(4, "Bây giờ các bạn thử tự đặt câu với mẫu 大……的 nhé."),
         F(5, "Đáp án gợi ý: 大半夜的，你怎么还不睡觉？ Nửa đêm rồi, sao cậu còn chưa ngủ? Và: 大热天的，别出去跑步了。 Trời nóng như thế này, đừng ra ngoài chạy bộ nữa.")])

add("bullets", chapter="Ngữ pháp: 倒不如", section="Ngữ pháp 注释", title="3. 倒不如 dào bùrú – chẳng thà, chi bằng", size=36,
    items=["So sánh nhiều mặt rồi chọn một phương án; phương án sau 倒不如 là phương án được chọn",
           "Thường đi với 与其: 与其A，倒不如B (thay vì A, chẳng thà B)",
           "假期所有的旅游景点都是人山人海，就算能买上车票，也玩儿不好，倒不如在家清清静静看看书，听听音乐。",
           "东西不是你的就不要去争夺，就是争来，也守不住。倒不如付出一分努力，得到一分收获，过平稳和顺的日子。",
           "翻开像册，我不禁肃然起敬，与其说这是一本像册，倒不如说这是他大半生的历史。"],
    say=["Điểm ngữ pháp thứ ba là 倒不如. Chữ đầu đọc thanh bốn.",
         F(0, "倒不如 biểu thị: sau khi so sánh nhiều mặt, người nói chọn một phương án. Phương án đứng sau 倒不如 là phương án được chọn, tiếng Việt dịch là chẳng thà, chi bằng."),
         F(1, "倒不如 thường đi với 与其, tạo thành mẫu 与其A，倒不如B, nghĩa là thay vì A, chẳng thà B. Đặc biệt, mẫu 与其说A，倒不如说B nghĩa là nói A chẳng bằng nói B, dùng để đưa ra một cách nhìn chính xác hơn."),
         F(2, "Ví dụ một: 假期所有的旅游景点都是人山人海，就算能买上车票，也玩儿不好，倒不如在家清清静静看看书，听听音乐。 Ngày nghỉ, điểm du lịch nào cũng đông nghịt người, dù mua được vé xe cũng chơi không vui, chi bằng ở nhà yên tĩnh đọc sách, nghe nhạc."),
         F(3, "Ví dụ hai, lấy từ bài khóa: 东西不是你的就不要去争夺，就是争来，也守不住。倒不如付出一分努力，得到一分收获，过平稳和顺的日子。 So sánh hai cách: tranh giành, và tự mình nỗ lực; người viết chọn cách thứ hai."),
         F(4, "Ví dụ ba: 翻开像册，我不禁肃然起敬，与其说这是一本像册，倒不如说这是他大半生的历史。 Mở cuốn album ảnh ra, tôi bất giác thấy kính phục, nói đây là một cuốn album, chẳng bằng nói đây là lịch sử của hơn nửa đời ông ấy.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: chọn vế thích hợp điền vào ( )", reveal=True, size=34,
    items=["## A. 与其说大海是一个安静的少女， · B. 与其天天为钱财奔忙， · C. 你有时间去批评人家，",
           "(1) (   )倒不如过清贫日子。",
           "Đáp án: B – 与其天天为钱财奔忙，倒不如过清贫日子。",
           "(2) 我渐渐开始明白，要想找出人家的漏洞太容易了，难的是建设一个新的东西出来。(   )倒不如好好琢磨自己能建设什么。",
           "Đáp án: C – 你有时间去批评人家，倒不如好好琢磨自己能建设什么。",
           "(3) 走向大洋深处，我才发现，(   )倒不如说是一只凶猛的怪兽。在看似平静的海面下，时时充满着凶险、恐怖，充满着数不清的暗礁、险滩。",
           "Đáp án: A – 与其说大海是一个安静的少女，倒不如说是一只凶猛的怪兽。"],
    say=[F(0, "Luyện tập: chọn vế câu thích hợp điền vào chỗ trống. Có ba lựa chọn. A: 与其说大海是一个安静的少女. B: 与其天天为钱财奔忙. C: 你有时间去批评人家."),
         F(1, "Câu một: 什么，倒不如过清贫日子。 Chẳng thà sống những ngày thanh bần. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: B. 与其天天为钱财奔忙，倒不如过清贫日子。 Thay vì ngày ngày bôn ba vì tiền bạc, chẳng thà sống những ngày thanh bần."),
         F(3, "Câu hai: 我渐渐开始明白，要想找出人家的漏洞太容易了，难的是建设一个新的东西出来。什么，倒不如好好琢磨自己能建设什么。 Tôi dần hiểu ra rằng, muốn tìm ra lỗ hổng của người khác thì dễ quá, cái khó là xây dựng nên một thứ mới."),
         F(4, "Đáp án: C. 你有时间去批评人家，倒不如好好琢磨自己能建设什么。 Bạn có thời gian đi phê bình người khác, chi bằng hãy suy nghĩ kỹ xem mình có thể xây dựng được gì. Ở đây không có 与其, nhưng ý so sánh vẫn rõ."),
         F(5, "Câu ba: 走向大洋深处，我才发现，什么，倒不如说是一只凶猛的怪兽。在看似平静的海面下，时时充满着凶险、恐怖，充满着数不清的暗礁、险滩。 Đi ra giữa đại dương, tôi mới phát hiện…"),
         F(6, "Đáp án: A. 与其说大海是一个安静的少女，倒不如说是一只凶猛的怪兽。 Nói biển cả là một thiếu nữ dịu dàng, chẳng bằng nói nó là một con quái vật hung dữ. Đây chính là mẫu 与其说A，倒不如说B.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 将近 – 将要", section="Phân biệt từ 词语辨析", title="Phân biệt 将近 và 将要 (1): chỉ thời gian",
    common="Giống nhau: đều là phó từ, chỉ sắp đến một thời điểm. Ví dụ: 将近/将要毕业时，他还没找到工作。",
    cols=[{"head": "将近",
           "lines": ["将近 + từ chỉ thời gian / động từ / tính từ: gần đến về mặt thời gian",
                     "Đúng: 将近下午四点时，下了一场大雨。",
                     "Đúng: 天将近黑了，他怎么还不回来？"]},
          {"head": "将要",
           "lines": ["将要 + động từ / cụm động từ (ít khi + tính từ): sắp xảy ra, sắp thay đổi",
                     "Đúng: 下月三号学校将要举办毕业典礼。",
                     "Đúng: 如果这次不成功，下次将要困难得多。"]}],
    say=["Tiếp theo là phần phân biệt từ: 将近 và 将要. Hai từ đều có chữ 将, nghĩa là sắp, nên rất dễ dùng lẫn lộn.",
         "Điểm giống nhau: cả hai đều là phó từ, biểu thị sắp đến một thời điểm nào đó. Ví dụ: 将近毕业时，他还没找到工作, hoặc 将要毕业时，他还没找到工作, đều đúng. Sắp tốt nghiệp rồi mà anh ấy vẫn chưa tìm được việc.",
         F(0, "Điểm khác thứ nhất. 将近 đi với từ chỉ thời gian, động từ hoặc tính từ, nhấn mạnh sự gần kề về mặt thời gian. Chữ 近 nghĩa là gần."),
         F(0, "Ví dụ: 将近下午四点时，下了一场大雨。 Gần bốn giờ chiều thì có một trận mưa lớn. Và: 天将近黑了，他怎么还不回来？ Trời sắp tối rồi, sao anh ấy vẫn chưa về?"),
         F(1, "Còn 将要 đi với động từ hoặc cụm động từ, rất ít khi đi với tính từ, biểu thị không lâu nữa sẽ xảy ra một việc, hoặc sẽ có một sự thay đổi. Nó nhấn mạnh sự việc sắp xảy ra, chứ không đo khoảng cách thời gian."),
         F(1, "Ví dụ: 下月三号学校将要举办毕业典礼。 Mùng ba tháng sau trường sẽ tổ chức lễ tốt nghiệp. Và: 如果这次不成功，下次将要困难得多。 Nếu lần này không thành công, lần sau sẽ khó khăn hơn nhiều.")])

add("compare", section="Phân biệt từ 词语辨析", title="Phân biệt 将近 và 将要 (2): chỉ số lượng",
    common="将近 còn đứng trước cụm số lượng, nghĩa là gần đạt tới con số đó; 将要 không có cách dùng này.",
    cols=[{"head": "将近",
           "lines": ["将近 + cụm số lượng: số lượng sắp đạt tới",
                     "Đúng: 这本书将近十万字，不过我一天就看完了。",
                     "Đúng: 他在这里工作了将近十年。"]},
          {"head": "将要",
           "lines": ["Không có cách dùng này",
                     "Sai: 这本书将要十万字。",
                     "Sai: 中国有将要四千年的历史。"]}],
    say=[F(0, "Điểm khác thứ hai. 将近 còn đứng trước cụm số lượng, biểu thị số lượng sắp đạt tới con số đó, tiếng Việt dịch là gần, ngót nghét. Ví dụ: 这本书将近十万字，不过我一天就看完了。 Cuốn sách này gần mười vạn chữ, nhưng tôi đọc một ngày là xong."),
         F(0, "Ví dụ khác, trong phần từ mới: 他在这里工作了将近十年。 Anh ấy đã làm việc ở đây gần mười năm."),
         F(1, "将要 không có cách dùng này. Vì vậy các câu 这本书将要十万字, hay 中国有将要四千年的历史, đều sai. Phải dùng 将近."),
         "Mẹo nhớ: 将近 có chữ 近, gần, nên đo khoảng cách gần đến một mốc thời gian hay một con số; còn 将要 có chữ 要, sắp, nên chỉ một sự việc sắp xảy ra, đứng trước động từ."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: chọn 将近 hay 将要?", reveal=True, size=36,
    items=["(1) 想到今后___在这所名牌大学学习，我心中激动极了。",
           "Đáp án: 将要 – đứng trước động từ, chỉ việc sắp xảy ra.",
           "(2) 中国有___四千年的有文字记载的历史。",
           "Đáp án: 将近 – đứng trước số lượng.",
           "(3) 他每天都学习到___半夜，真令人佩服。",
           "Đáp án: 将近 – gần đến một mốc thời gian.",
           "(4) 如果经济状况不改善，不少工人___面临失业。",
           "Đáp án: 将要 – đứng trước động từ 面临."],
    say=[F(0, "Bây giờ chúng ta làm thử: chọn 将近 hay 将要 điền vào chỗ trống. Câu một: 想到今后什么在这所名牌大学学习，我心中激动极了。 Nghĩ đến việc sau này sẽ học ở ngôi trường danh tiếng này, lòng tôi vô cùng xúc động. Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: 将要. Phía sau là động từ 学习, chỉ việc sắp xảy ra: 今后将要在这所名牌大学学习。"),
         F(2, "Câu hai: 中国有什么四千年的有文字记载的历史。 Trung Quốc có gần bốn nghìn năm lịch sử được ghi chép bằng chữ viết."),
         F(3, "Đáp án: 将近. Phía sau là cụm số lượng 四千年, nên chỉ dùng được 将近."),
         F(4, "Câu ba: 他每天都学习到什么半夜，真令人佩服。 Ngày nào anh ấy cũng học đến gần nửa đêm, thật khiến người ta khâm phục."),
         F(5, "Đáp án: 将近. 半夜 là một mốc thời gian, 将近半夜 là gần nửa đêm."),
         F(6, "Câu bốn: 如果经济状况不改善，不少工人什么面临失业。 Nếu tình hình kinh tế không được cải thiện, không ít công nhân sẽ đối mặt với thất nghiệp."),
         F(7, "Đáp án: 将要. Phía sau là động từ 面临, chỉ sự việc sắp xảy ra: 不少工人将要面临失业。")])

# ======================= MỞ RỘNG: DANH TỪ QUA HÌNH ẢNH =======================
add("bullets", chapter="Mở rộng: danh từ qua hình ảnh", section="Mở rộng 扩展", title="Mở rộng 扩展: nhìn tranh, làm quen danh từ (1)", size=34,
    items=["## 皮革 pígé (bì cách) – da thuộc",
           "皮革包 túi da · 他在皮革厂工作。 Anh ấy làm ở xưởng da thuộc.",
           "## 钻石 zuànshí (toản thạch) – kim cương",
           "一颗钻石 một viên kim cương · 这件首饰非常昂贵，上面镶满了钻石。",
           "## 哨 shào (tiếu) – cái còi",
           "吹哨 thổi còi · 足球场上裁判员吹哨的动作很帅。",
           "## 启事 qǐshì (khải sự) – mẩu thông báo, rao vặt",
           "寻物启事 thông báo tìm đồ thất lạc · 墙上贴着一张寻物启事。"],
    say=["Bây giờ chúng ta sang phần mở rộng của sách. Quyển này không có mục tu từ riêng; ở bài này, phần mở rộng là từ vựng: nhìn tranh để làm quen với tám danh từ thường gặp trong đời sống.",
         F(0, "Từ thứ nhất: 皮革, Hán Việt là bì cách, nghĩa là da thuộc, tức là da động vật đã qua xử lý."),
         F(1, "皮革包 là túi da. Ví dụ: 他在皮革厂工作。 Anh ấy làm việc ở xưởng da thuộc."),
         F(2, "Từ thứ hai: 钻石, Hán Việt là toản thạch, nghĩa là kim cương. Chữ đầu đọc thanh bốn."),
         F(3, "Lượng từ là 颗: 一颗钻石, một viên kim cương. Ví dụ: 这件首饰非常昂贵，上面镶满了钻石。 Món trang sức này cực kỳ đắt, trên đó nạm đầy kim cương. Các bạn để ý, ở đây lại gặp chữ 镶 trong từ mới 镶嵌."),
         F(4, "Từ thứ ba: 哨, Hán Việt là tiếu, nghĩa là cái còi, cũng nói là 哨子."),
         F(5, "Động từ đi kèm là 吹, thổi: 吹哨, thổi còi. Ví dụ: 足球场上裁判员吹哨的动作很帅。 Động tác thổi còi của trọng tài trên sân bóng trông rất ngầu."),
         F(6, "Từ thứ tư: 启事, Hán Việt là khải sự, nghĩa là mẩu thông báo dán nơi công cộng hoặc đăng báo. Chú ý: đừng nhầm với 启示, nghĩa là sự gợi mở, bài học."),
         F(7, "寻物启事 là thông báo tìm đồ thất lạc; ngoài ra còn có 招聘启事, thông báo tuyển dụng. Ví dụ: 墙上贴着一张寻物启事。 Trên tường dán một tờ thông báo tìm đồ thất lạc.")])

add("bullets", section="Mở rộng 扩展", title="Mở rộng 扩展: nhìn tranh, làm quen danh từ (2)", size=34,
    items=["## 油漆 yóuqī (du tất) – sơn",
           "刷油漆 quét sơn · 用油漆刷墙。 Dùng sơn quét tường.",
           "## 炊烟 chuīyān (xuy yên) – khói bếp",
           "傍晚时，村子里家家升起了炊烟。",
           "## 证书 zhèngshū (chứng thư) – giấy chứng nhận, bằng",
           "荣誉证书 bằng khen · 上学期间他获得了不少荣誉证书。",
           "## 火焰 huǒyàn (hỏa diễm) – ngọn lửa",
           "一团火焰 một ngọn lửa · 红色的火焰让人感觉很温暖。"],
    say=[F(0, "Từ thứ năm: 油漆, Hán Việt là du tất, nghĩa là sơn. Chữ 漆 vốn là cây sơn, như trong sơn mài."),
         F(1, "Động từ đi kèm là 刷, quét: 刷油漆, quét sơn. Ví dụ: 用油漆刷墙。 Dùng sơn quét tường."),
         F(2, "Từ thứ sáu: 炊烟, Hán Việt là xuy yên, nghĩa là khói bếp. Chữ 炊 là nấu nướng, chữ 烟 là khói."),
         F(3, "Ví dụ: 傍晚时，村子里家家升起了炊烟。 Lúc chiều tà, nhà nhà trong làng bốc lên khói bếp. Đây là một hình ảnh rất đẹp, rất thân thuộc của làng quê, rất hợp với chủ đề Quê hương xinh đẹp."),
         F(4, "Từ thứ bảy: 证书, Hán Việt là chứng thư, nghĩa là giấy chứng nhận, văn bằng."),
         F(5, "荣誉证书 là bằng khen, giấy khen; 毕业证书 là bằng tốt nghiệp. Ví dụ: 上学期间他获得了不少荣誉证书。 Trong thời gian đi học, anh ấy đã nhận được không ít giấy khen."),
         F(6, "Từ thứ tám: 火焰, Hán Việt là hỏa diễm, nghĩa là ngọn lửa."),
         F(7, "Lượng từ là 团: 一团火焰, một ngọn lửa. Ví dụ: 红色的火焰让人感觉很温暖。 Ngọn lửa đỏ khiến người ta cảm thấy thật ấm áp.")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chọn danh từ điền vào chỗ trống (1)", reveal=True, size=36,
    items=["## Từ cho sẵn: 皮革 · 钻石 · 哨 · 启事",
           "(1) 比赛开始了，裁判员吹响了___。",
           "Đáp án: 哨",
           "(2) 他的钱包丢了，就在学校门口贴了一张寻物___。",
           "Đáp án: 启事",
           "(3) 这枚戒指上镶嵌着一颗很大的___。",
           "Đáp án: 钻石",
           "(4) 这个包是用真___做的，所以很贵。",
           "Đáp án: 皮革"],
    say=[F(0, "Bây giờ chúng ta luyện tập: chọn danh từ thích hợp điền vào chỗ trống. Nhóm một có bốn từ: 皮革，钻石，哨，启事."),
         F(1, "Câu một: 比赛开始了，裁判员吹响了什么。 Trận đấu bắt đầu, trọng tài đã thổi vang cái gì? Các bạn tạm dừng và suy nghĩ nhé."),
         F(2, "Đáp án: 哨. 裁判员吹响了哨。 Trọng tài đã thổi còi."),
         F(3, "Câu hai: 他的钱包丢了，就在学校门口贴了一张寻物什么。 Anh ấy mất ví, liền dán một tờ gì đó ở cổng trường."),
         F(4, "Đáp án: 启事. 贴了一张寻物启事, dán một tờ thông báo tìm đồ thất lạc."),
         F(5, "Câu ba: 这枚戒指上镶嵌着一颗很大的什么。 Trên chiếc nhẫn này có nạm một viên rất to."),
         F(6, "Đáp án: 钻石. 一颗很大的钻石, một viên kim cương rất to. Lượng từ 颗 là gợi ý quan trọng."),
         F(7, "Câu bốn: 这个包是用真什么做的，所以很贵。 Chiếc túi này làm bằng thứ thật, nên rất đắt. Đáp án: 皮革. 真皮革, da thật.")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chọn danh từ điền vào chỗ trống (2)", reveal=True, size=36,
    items=["## Từ cho sẵn: 油漆 · 炊烟 · 证书 · 火焰",
           "(5) 墙上的___刚刷过，请不要用手摸。",
           "Đáp án: 油漆",
           "(6) 太阳落山了，村子里升起了一缕缕___。",
           "Đáp án: 炊烟",
           "(7) 冬天的晚上，大家围着火堆，看着跳动的___。",
           "Đáp án: 火焰",
           "(8) 他工作非常努力，获得了公司颁发的荣誉___。",
           "Đáp án: 证书"],
    say=[F(0, "Nhóm hai có bốn từ: 油漆，炊烟，证书，火焰."),
         F(1, "Câu năm: 墙上的什么刚刷过，请不要用手摸。 Thứ gì trên tường vừa mới quét xong, xin đừng sờ tay vào?"),
         F(2, "Đáp án: 油漆. 墙上的油漆刚刷过, sơn trên tường vừa mới quét. Động từ 刷 là gợi ý."),
         F(3, "Câu sáu: 太阳落山了，村子里升起了一缕缕什么。 Mặt trời đã lặn, trong làng bốc lên từng làn gì?"),
         F(4, "Đáp án: 炊烟. 升起了一缕缕炊烟, bốc lên từng làn khói bếp."),
         F(5, "Câu bảy: 冬天的晚上，大家围着火堆，看着跳动的什么。 Đêm mùa đông, mọi người quây quanh đống lửa, ngắm nhìn cái gì đang nhảy múa?"),
         F(6, "Đáp án: 火焰. 跳动的火焰, ngọn lửa bập bùng."),
         F(7, "Câu tám: 他工作非常努力，获得了公司颁发的荣誉什么。 Anh ấy làm việc rất chăm chỉ, nhận được cái gì do công ty trao tặng? Đáp án: 证书. 荣誉证书, giấy khen. Mẹo: khi học danh từ, hãy học kèm lượng từ và động từ hay đi cùng, như 一颗钻石，吹哨，刷油漆，一团火焰.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ có dấu chấm", size=40,
    items=["欲望 (望) → 愿望 · 希望 · 失望 · 盼望",
           "富裕 (富) → 富有 · 丰富 · 财富 · 富强",
           "隐蔽 (隐) → 隐藏 · 隐私 · 隐瞒 · 隐约",
           "贪婪 (贪) → 贪心 · 贪玩 · 贪吃 · 贪污",
           "争夺 (争) → 争取 · 竞争 · 争论 · 战争"],
    say=["Phần luyện tập. Bài tập một: mô phỏng ví dụ, viết thêm các từ có chứa chữ được đánh dấu chấm.",
         F(0, "Ví dụ mẫu: 欲望, chữ được đánh dấu là chữ thứ hai, nghĩa là mong. Ta có 愿望，希望，失望，盼望. Tức là nguyện vọng, hy vọng, thất vọng, và mong ngóng."),
         F(1, "富裕, chữ được đánh dấu là chữ đầu, nghĩa là giàu. Ta có 富有，丰富，财富，富强. Tức là giàu có, phong phú, của cải, và giàu mạnh."),
         F(2, "隐蔽, chữ được đánh dấu là chữ đầu, nghĩa là ẩn, giấu. Ta có 隐藏，隐私，隐瞒，隐约. Tức là cất giấu, đời tư, giấu giếm, và thấp thoáng, lờ mờ."),
         F(3, "贪婪, chữ được đánh dấu là chữ đầu, nghĩa là tham. Ta có 贪心，贪玩，贪吃，贪污. Tức là lòng tham, ham chơi, ham ăn, và tham ô. Từ 贪污 cũng là từ mới của bài."),
         F(4, "争夺, chữ được đánh dấu là chữ đầu, nghĩa là tranh. Ta có 争取，竞争，争论，战争. Tức là tranh thủ, cạnh tranh, tranh luận, và chiến tranh.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (1)", reveal=True, size=36,
    items=["(1) 他们夫妻快到40岁才有了这个孩子，所以特别疼爱。（将近）",
           "Đáp án: 他们夫妻将近40岁才有了这个孩子，所以特别疼爱。",
           "(2) 上海那么大，再说你又不知道地址，怎么能找到他呢？（况且）",
           "Đáp án: 上海那么大，况且你又不知道地址，怎么能找到他呢？",
           "(3) 他对中国京剧非常感兴趣，所以参加了一个京剧培训班。（颇）",
           "Đáp án: 他对中国京剧颇感兴趣，所以参加了一个京剧培训班。"],
    say=[F(0, "Bài tập hai: dùng từ cho sẵn để viết lại câu. Câu một, dùng 将近: 他们夫妻快到四十岁才有了这个孩子，所以特别疼爱。 Vợ chồng họ gần bốn mươi tuổi mới có đứa con này, nên đặc biệt cưng chiều. Các bạn tạm dừng và thử viết lại nhé."),
         F(1, "Đáp án: 他们夫妻将近四十岁才有了这个孩子，所以特别疼爱。 快到 được thay bằng 将近, đứng trước số lượng."),
         F(2, "Câu hai, dùng 况且: 上海那么大，再说你又不知道地址，怎么能找到他呢？ Thượng Hải rộng như thế, hơn nữa cậu lại không biết địa chỉ, làm sao tìm được anh ấy?"),
         F(3, "Đáp án: 上海那么大，况且你又不知道地址，怎么能找到他呢？ 再说 được thay bằng 况且, bổ sung thêm lý do. Các bạn để ý, vế có 况且 vẫn giữ chữ 又."),
         F(4, "Câu ba, dùng 颇: 他对中国京剧非常感兴趣，所以参加了一个京剧培训班。 Anh ấy rất hứng thú với Kinh kịch, nên đã tham gia một lớp học Kinh kịch."),
         F(5, "Đáp án: 他对中国京剧颇感兴趣，所以参加了一个京剧培训班。 Giống 颇感诧异 trong bài khóa, ta có 颇感兴趣, khá hứng thú.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (2)", reveal=True, size=36,
    items=["(4) 很明显他是喜欢你的，你怎么感觉不到呢？（分明）",
           "Đáp án: 他分明是喜欢你的，你怎么感觉不到呢？",
           "(5) 假期我们一起去欧洲玩儿一趟，怎么样？（咋）",
           "Đáp án: 假期我们一起去欧洲玩儿一趟，咋样？",
           "(6) 为了安全，我宁愿绕远儿走大路。（宁肯）",
           "Đáp án: 为了安全，我宁肯绕远儿走大路。"],
    say=[F(0, "Câu bốn, dùng 分明: 很明显他是喜欢你的，你怎么感觉不到呢？ Rõ ràng là anh ấy thích cậu, sao cậu không cảm nhận được?"),
         F(1, "Đáp án: 他分明是喜欢你的，你怎么感觉不到呢？ 很明显 được thay bằng phó từ 分明, đặt sau chủ ngữ."),
         F(2, "Câu năm, dùng 咋样: 假期我们一起去欧洲玩儿一趟，怎么样？ Kỳ nghỉ chúng mình cùng đi châu Âu một chuyến, thế nào?"),
         F(3, "Đáp án: 假期我们一起去欧洲玩儿一趟，咋样？ 怎么样 được thay bằng 咋样, giọng điệu khẩu ngữ, thân mật hơn."),
         F(4, "Câu sáu, dùng 宁肯: 为了安全，我宁愿绕远儿走大路。 Để an toàn, tôi thà đi vòng xa theo đường lớn."),
         F(5, "Đáp án: 为了安全，我宁肯绕远儿走大路。 宁愿 và 宁肯 nghĩa giống nhau, đều là thà, thà rằng.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (1)", reveal=True, size=34,
    items=["## Từ cho sẵn: 勤俭 · 将近 · 祖父 · 富裕 · 废寝忘食",
           "我的___在___三十岁时才找到第一份工作，他很珍惜这个机会，每天___地工作。加上祖母很___，家里的日子渐渐___起来。",
           "Đáp án: 祖父 · 将近 · 废寝忘食 · 勤俭 · 富裕"],
    say=[F(0, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn một có năm từ: 勤俭，将近，祖父，富裕，废寝忘食."),
         F(1, "我的什么在什么三十岁时才找到第一份工作，他很珍惜这个机会，每天什么地工作。加上祖母很什么，家里的日子渐渐什么起来。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 我的祖父在将近三十岁时才找到第一份工作，他很珍惜这个机会，每天废寝忘食地工作。加上祖母很勤俭，家里的日子渐渐富裕起来。 Ông nội tôi gần ba mươi tuổi mới tìm được công việc đầu tiên, ông rất trân trọng cơ hội này, ngày nào cũng làm việc quên ăn quên ngủ. Thêm vào đó bà nội rất cần kiệm, nên cuộc sống trong nhà dần dần sung túc lên.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (2)", reveal=True, size=34,
    items=["## Từ cho sẵn: 坑 · 瘸 · 膝盖 · 扎 · 侥幸",
           "上周的一个晚上，我骑着自行车回家，不小心掉进了一个大___，爬起来一看，原来是附近种树的人挖的。___摔破了，手也被___破了，鲜血直流，还算___，骨头没事。我只好推着自行车一___一拐地走回了家。",
           "Đáp án: 坑 · 膝盖 · 扎 · 侥幸 · 瘸"],
    say=[F(0, "Đoạn hai có năm từ: 坑，瘸，膝盖，扎破，侥幸."),
         F(1, "上周的一个晚上，我骑着自行车回家，不小心掉进了一个大什么，爬起来一看，原来是附近种树的人挖的。什么摔破了，手也被什么破了，鲜血直流，还算什么，骨头没事。我只好推着自行车一什么一拐地走回了家。 Các bạn điền thử nhé."),
         F(2, "Đáp án: 掉进了一个大坑，膝盖摔破了，手也被扎破了，还算侥幸，一瘸一拐地走回了家。 Tối thứ hai tuần trước, tôi đạp xe về nhà, không cẩn thận rơi xuống một cái hố lớn, bò dậy nhìn thì ra là hố của người trồng cây gần đó đào. Đầu gối bị trầy, tay cũng bị đâm rách, máu chảy ròng ròng, cũng còn may là xương không sao. Tôi đành dắt xe đạp tập tễnh đi về nhà."),
         "Các bạn thấy không, đoạn văn này dùng lại rất nhiều từ của bài khóa: 坑，膝盖，侥幸，一瘸一拐. Giống như cụ ba trong truyện vậy."])

add("bullets", section="Luyện tập 练习", title="Bài tập 4: Chọn vị trí thích hợp cho từ trong ngoặc", reveal=True, size=34,
    items=["(1) A晴天，B你出门时C干吗要D带把雨伞呢？（大） → Đáp án: A",
           "(2) 与其A一个人生气，B不如C找个朋友D说出来更好。（倒） → Đáp án: B",
           "(3) A父亲年龄大了，B身体也不好，C我不放心D他一个人去旅行。（况且） → Đáp án: B",
           "(4) 他A自己吃点儿亏，B也不愿C让朋友D吃亏。（宁肯） → Đáp án: A",
           "(5) 他A朝你这个方向B走来的，C你怎么D没看见他呢？（分明） → Đáp án: A"],
    say=["Bài tập bốn: chọn vị trí thích hợp cho từ trong ngoặc. Thầy đọc từng câu, các bạn tạm dừng để chọn, rồi nghe đáp án nhé.",
         F(0, "Câu một, từ 大: 晴天，你出门时干吗要带把雨伞呢？ Đáp án: A. 大晴天，你出门时干吗要带把雨伞呢？ Trời nắng chang chang, ra ngoài mang ô làm gì? Đây là cách dùng 大 nhấn mạnh thời điểm."),
         F(1, "Câu hai, từ 倒: 与其一个人生气，不如找个朋友说出来更好。 Đáp án: B. 与其一个人生气，倒不如找个朋友说出来更好。 Thay vì một mình bực bội, chi bằng tìm một người bạn nói ra cho nhẹ lòng."),
         F(2, "Câu ba, từ 况且: 父亲年龄大了，身体也不好，我不放心他一个人去旅行。 Đáp án: B. 父亲年龄大了，况且身体也不好，我不放心他一个人去旅行。 Bố đã có tuổi, hơn nữa sức khỏe lại không tốt, tôi không yên tâm để ông đi du lịch một mình."),
         F(3, "Câu bốn, từ 宁肯: 他自己吃点儿亏，也不愿让朋友吃亏。 Đáp án: A. 他宁肯自己吃点儿亏，也不愿让朋友吃亏。 Anh ấy thà mình chịu thiệt một chút, chứ không muốn để bạn bè chịu thiệt. Đây là mẫu 宁肯……也不……."),
         F(4, "Câu năm, từ 分明: 他朝你这个方向走来的，你怎么没看见他呢？ Đáp án: A. 他分明朝你这个方向走来的，你怎么没看见他呢？ Rõ ràng là anh ấy đi về phía cậu, sao cậu lại không nhìn thấy?")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 20", size=36,
    items=["Từ vựng trọng tâm: 镶嵌 · 别致 · 废寝忘食 · 勤俭 · 将近 · 况且 · 颇 · 分明 · 侥幸 · 得不偿失 · 宁肯 · 告诫 · 贪婪 · 不择手段",
           "Ngữ pháp: 况且 (hơn nữa, vả lại) · 大……的 (nhấn mạnh thời điểm) · (与其……)倒不如 (chẳng thà)",
           "Phân biệt: 将近 (thời gian; số lượng) ≠ 将要 (+ động từ, việc sắp xảy ra)",
           "Mở rộng: 皮革 · 钻石 · 哨 · 启事 · 油漆 · 炊烟 · 证书 · 火焰",
           "## Bài tập về nhà (运用)",
           "Viết bài ít nhất 400 chữ với đề 争来的东西守不住, kể một truyền thuyết hay câu chuyện tương tự ở nước bạn"],
    say=["Chúng ta cùng tổng kết bài hai mươi.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 镶嵌，别致，废寝忘食，勤俭，将近，况且，颇，分明，侥幸，得不偿失，宁肯，告诫，贪婪，不择手段. Và đừng quên những từ dễ nhầm như 工艺品，分明，滋味，欲望."),
         F(1, "Về ngữ pháp: 况且 đứng đầu vế sau, bổ sung thêm lý do. 大 đứng trước từ chỉ thời gian theo mẫu 大……的, nhấn mạnh thời điểm, ngụ ý lúc ấy lẽ ra không nên làm việc đó. 倒不如 dùng để chọn một phương án sau khi so sánh, thường đi với 与其."),
         F(2, "Về phân biệt từ: 将近 đo sự gần kề, đứng trước từ chỉ thời gian hoặc cụm số lượng; còn 将要 đứng trước động từ, chỉ sự việc sắp xảy ra, và không đi với số lượng."),
         F(3, "Về phần mở rộng: tám danh từ 皮革，钻石，哨，启事，油漆，炊烟，证书，火焰. Nhớ học kèm lượng từ và động từ đi cùng nhé."),
         F(5, "Bài tập về nhà, theo phần vận dụng của sách: bài khóa dạy chúng ta rằng, làm người đừng có quá nhiều ham muốn, đừng tham lam; thứ gì không phải của mình thì đừng tranh giành, cho dù giành được cũng chẳng giữ nổi. Ở nước các bạn có truyền thuyết hay câu chuyện nào tương tự không? Hãy dựa vào dàn ý của bài tập năm, kể theo thời gian, địa điểm, bối cảnh, diễn biến và bài học, viết một bài ít nhất bốn trăm chữ với đề 争来的东西守不住. Các bạn người Việt có thể kể truyện Cây khế, ăn một quả trả cục vàng, may túi ba gang mang đi mà đựng. Nhớ thử dùng 况且，倒不如 và mẫu 大……的 trong bài viết nhé."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Và xin chúc mừng các bạn: với bài hai mươi này, chúng ta đã hoàn thành trọn vẹn quyển Thượng của Giáo trình chuẩn HSK 6! Hai mươi bài học, hàng nghìn từ mới, các bạn đã đi được một chặng đường thật dài. Hãy dành chút thời gian ôn lại, rồi cùng thầy bước sang quyển Hạ. Hẹn gặp lại các bạn ở bài hai mươi mốt: 未来商店, Cửa hàng tương lai. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Thượng) – Bài 20: 金鸡窝 (Ổ gà vàng)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"嗨": "嘿",                # hēi (theo sách)
                    "扎": "渣",                # zhā (mọi chỗ trong bài đều đọc zhā)
                    "撇": "苤",                # piě (mọi chỗ trong bài đều đọc piě)
                    "干吗": "赣吗",            # gànmá
                    "还算": "孩算",            # háisuàn
                    "鸡仔": "鸡宰",            # jīzǎi
                    "干草": "甘草",            # gāncǎo
                    "砸中": "砸众",            # zázhòng
                    "当拐杖": "荡拐杖",        # dàng
                    "下不了": "下不瞭",        # xià bu liǎo
                    "宁肯": "佞肯",            # nìngkěn
                    "宁愿": "佞愿",            # nìngyuàn
                    "宁可": "佞可",            # nìngkě
                    "倒不如": "到不如",        # dào bùrú
                    "四处": "四触",            # sìchù
                    "近处": "近触",            # jìnchù
                    "深处": "深触",            # shēnchù
                    "行业": "航业",            # hángyè
                    "为钱财": "位钱财",        # wèi
                    "为期": "维期",            # wéiqī
                    "数不清": "属不清",        # shǔ bu qīng
                    "记载": "记宰",            # jìzǎi
                    "种树": "众树",            # zhòngshù
                    "朝你": "潮你",            # cháo
                    "钻石": "攥石",            # zuànshí
                    "得空": "得控",            # dékòng
                    "少壮": "绍壮",            # shàozhuàng
                    "长远": "常远",            # chángyuǎn
                    "流长": "流常",            # liúcháng
                    "假期": "架期",            # jiàqī
                    "心脏": "心葬",            # xīnzàng
                    "不禁": "不今",            # bùjīn
                    "摔倒": "摔岛",            # shuāidǎo
                    "琢磨": "昨磨"},           # zuómo
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai20.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
