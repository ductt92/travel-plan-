#!/usr/bin/env python3
"""Kịch bản bài giảng 顶石中文 – Bài 7.2 «天下没有永远免费的午餐». Chạy để sinh ds72.json."""
import json
import os

TAG = "顶石中文 · Bài 7.2 · 天下没有永远免费的午餐"
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
    zh="天下没有", py="永远免费的午餐",
    vi="Bài 7.2: Trên đời không có bữa trưa nào miễn phí mãi",
    sub="Tiānxià méiyǒu yǒngyuǎn miǎnfèi de wǔcān\nBài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng giáo trình 顶石中文, Đỉnh cao tiếng Trung.",
         {"t": "Hôm nay chúng ta học bài thứ hai của Đơn vị bảy, chủ đề Kinh tế: bài bảy chấm hai, 天下没有永远免费的午餐。 Nghĩa là: Trên đời không có bữa trưa nào miễn phí mãi mãi.",
          "cap": "Hôm nay chúng ta học bài thứ hai của Đơn vị 7, chủ đề Kinh tế: bài 7.2, 天下没有永远免费的午餐。 Nghĩa là: Trên đời không có bữa trưa nào miễn phí mãi mãi."},
         "Bài khóa là một bài bình luận trên tuần báo Nam Phương Chu Mạt. Câu chuyện bắt đầu từ năm hào tiền: năm hai nghìn không trăm hai mươi, công ty tủ nhận hàng Phong Sào thu phí giữ hàng quá giờ, và cả mạng xã hội Trung Quốc nổi sóng. Từ sự kiện nhỏ ấy, tác giả giải thích vì sao internet từng miễn phí, ai đã trả tiền cho sự miễn phí đó, và vì sao thời đại miễn phí nhất định phải kết thúc.",
         "Ở Việt Nam, chắc các bạn cũng quen với mã freeship, với những ứng dụng gọi xe từng khuyến mãi rất mạnh rồi tăng giá dần. Người Việt cũng có câu: không ai cho không ai cái gì. Trong lúc học, các bạn hãy liên hệ với những gì mình thấy hằng ngày nhé."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài bình luận: vì sao internet từng miễn phí, ai trả tiền, vì sao miễn phí phải kết thúc",
           "Nắm vững 51 từ mới, kèm âm Hán Việt và ví dụ",
           "6 mẫu câu: 随着……的普及 · ……的优势在于 · 以……换…… · 换一个角度看 · ……可以休矣 · 难怪",
           "8 kết hợp từ: 颇 · 遵循 · 浓厚 · 放宽 · 排斥 · 反常 · 泡沫 · 留恋 và 9 thành ngữ, quán ngữ",
           "Luyện tập theo sách; liên hệ: freeship, “đốt tiền” và chuyện trả phí ở Việt Nam"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu bài bình luận: vì sao internet từng miễn phí, ai thực sự trả tiền cho sự miễn phí ấy, và vì sao miễn phí không thể kéo dài mãi."),
         F(1, "Thứ hai, nắm vững năm mươi mốt từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ. Bài này có nhiều thuật ngữ kinh tế như 亏损，热钱，泡沫，超发."),
         F(2, "Thứ ba, học sáu mẫu câu trọng điểm: 随着的普及，的优势在于，以换，换一个角度看，可以休矣, và 难怪."),
         F(3, "Thứ tư, học tám kết hợp từ và chín thành ngữ, quán ngữ, trong đó có những câu rất sinh động như 瞎猫撞到死耗子, mèo mù vớ cá rán, hay 赔本赚吆喝, chịu lỗ để lấy tiếng."),
         F(4, "Thứ năm, làm bài luyện tập của sách, và liên hệ với Việt Nam: mã freeship, các ứng dụng đốt tiền giành thị phần, và thói quen trả phí cho nội dung số."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 课前思考", title="Câu hỏi trước bài học 课前思考", reveal=True, size=34,
    items=["(1) 你们国家网购包邮吗？",
           "Đáp án gợi ý: 越南的电商平台经常有包邮活动，比如发放免运费优惠券，不过近年来包邮的门槛越来越高了。",
           "(2) 你有过被收取高额服务费的经历吗？",
           "Đáp án gợi ý: 有过。有一次节假日用打车软件叫车，价格比平时贵了一倍多，还加收了服务费。",
           "(3) 你怎么看免费包邮？",
           "Đáp án gợi ý: 我认为免费包邮其实并不免费，运费往往已经算进了商品价格里，天下没有免费的午餐。"],
    say=["Chúng ta bắt đầu bằng ba câu hỏi trước bài học, 课前思考. Thầy đọc câu hỏi, các bạn tạm dừng để tự trả lời bằng tiếng Trung, rồi nghe câu trả lời gợi ý nhé.",
         F(0, "Câu một: 你们国家网购包邮吗？ Ở nước bạn mua hàng online có được miễn phí vận chuyển không? 包邮 là bao phí bưu điện, tức là miễn phí vận chuyển, freeship."),
         F(1, "Gợi ý: 越南的电商平台经常有包邮活动，比如发放免运费优惠券，不过近年来包邮的门槛越来越高了。 Các sàn thương mại điện tử Việt Nam thường có chương trình freeship, ví dụ phát mã miễn phí vận chuyển, nhưng mấy năm gần đây điều kiện để được freeship ngày càng cao."),
         F(2, "Câu hai: 你有过被收取高额服务费的经历吗？ Bạn đã bao giờ bị thu phí dịch vụ cao chưa?"),
         F(3, "Gợi ý: 有过。有一次节假日用打车软件叫车，价格比平时贵了一倍多，还加收了服务费。 Có. Có lần vào ngày lễ tôi gọi xe bằng ứng dụng, giá đắt gấp đôi ngày thường, lại còn thu thêm phí dịch vụ."),
         F(4, "Câu ba: 你怎么看免费包邮？ Bạn nghĩ thế nào về việc miễn phí vận chuyển?"),
         F(5, "Gợi ý: 我认为免费包邮其实并不免费，运费往往已经算进了商品价格里，天下没有免费的午餐。 Tôi cho rằng freeship thật ra không hề miễn phí, phí vận chuyển thường đã được tính vào giá hàng rồi; trên đời không có bữa trưa nào miễn phí.")])

add("bullets", section="Khởi động 课前思考", title="Khởi động: từ ngữ về “miễn phí” và “trả phí” trên mạng", size=34,
    items=["## 免费 miễn phí ↔ 收费 / 付费 thu phí / trả phí",
           "包邮 freeship · 会员 thành viên (VIP) · 超时费 phí quá giờ · 服务费 phí dịch vụ",
           "## Mô hình “đốt tiền” của doanh nghiệp internet",
           "补贴 trợ giá · 获客 giành khách · 流量 lưu lượng · 广告收入 thu nhập quảng cáo · 亏损 thua lỗ",
           "## 天下没有免费的午餐 = There is no such thing as a free lunch",
           "≈ “Không ai cho không ai cái gì” · “Miếng pho mát miễn phí chỉ có trong bẫy chuột”"],
    say=["Trước khi học từ mới, chúng ta làm quen với một số từ ngữ về miễn phí và trả phí trên mạng.",
         F(0, "免费 là miễn phí; ngược lại là 收费, thu phí, nhìn từ phía doanh nghiệp, và 付费, trả phí, nhìn từ phía người dùng."),
         F(1, "包邮 là freeship; 会员 là thành viên, như 视频会员, gói VIP xem phim; 超时费 là phí quá giờ; 服务费 là phí dịch vụ."),
         F(2, "Bài khóa giải thích mô hình đốt tiền của doanh nghiệp internet. Các từ khóa là:"),
         F(3, "补贴, trợ giá; 获客, giành khách hàng; 流量, lưu lượng truy cập; 广告收入, thu nhập quảng cáo; và 亏损, thua lỗ. Doanh nghiệp chịu lỗ, trợ giá để kéo thật nhiều người dùng, rồi mới tính chuyện kiếm tiền."),
         F(4, "Tên bài dựa trên một câu rất nổi tiếng của kinh tế học: 天下没有免费的午餐, There is no such thing as a free lunch. Tác giả thêm chữ 永远, mãi mãi: có thể miễn phí một thời gian, nhưng không thể miễn phí mãi."),
         F(5, "Tiếng Việt cũng có những câu tương tự: không ai cho không ai cái gì; hay miếng pho mát miễn phí chỉ có trong bẫy chuột.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("时段", "shíduàn", "thời đoạn", "danh từ", "khung giờ, khoảng thời gian", "晚上八点是电视的黄金时段。", "Tám giờ tối là khung giờ vàng của truyền hình.",
     "Danh từ, chỉ một khoảng thời gian nhất định. Hay gặp: 黄金时段, khung giờ vàng; 免费时段, khung giờ miễn phí. Trong bài: 十二小时免费时段之外, ngoài khung mười hai giờ miễn phí."),
    ("封顶", "fēngdǐng", "phong đỉnh", "động từ", "giới hạn mức trần, tối đa; (xây dựng) cất nóc", "这个停车场每天收费二十元封顶。", "Bãi đỗ xe này mỗi ngày thu tối đa hai mươi tệ.",
     "Động từ, nghĩa là quy định mức cao nhất. Trong bài: 每小时收取零点五元，封顶三元, mỗi giờ thu năm hào, tối đa ba tệ. Trong xây dựng, 封顶 là cất nóc, đổ mái."),
    ("妥协", "tuǒxié", "thỏa hiệp", "động từ", "thỏa hiệp, nhượng bộ", "经过谈判，双方都做出了妥协。", "Sau đàm phán, cả hai bên đều đã nhượng bộ.",
     "Động từ, nghĩa là nhượng bộ để tránh xung đột, tranh cãi. Âm Hán Việt và nghĩa giống hệt tiếng Việt. Trong bài: 最终以企业妥协告终, cuối cùng kết thúc bằng việc doanh nghiệp nhượng bộ."),
    ("放宽", "fàngkuān", "phóng khoan", "động từ", "nới lỏng, nới rộng (yêu cầu, tiêu chuẩn)", "学校放宽了入学年龄限制。", "Nhà trường đã nới lỏng giới hạn độ tuổi nhập học.",
     "Động từ, nghĩa là làm cho yêu cầu, tiêu chuẩn từ chặt thành lỏng. Trái nghĩa là 收紧, siết chặt. Hay gặp: 放宽标准，放宽条件，放宽管制. Đây là một kết hợp từ trọng điểm."),
    ("时限", "shíxiàn", "thời hạn", "danh từ", "thời hạn (để hoàn thành)", "这项工作必须在规定的时限内完成。", "Công việc này phải hoàn thành trong thời hạn quy định.",
     "Danh từ, nghĩa là thời hạn để hoàn thành một việc. Phân biệt: 时段 là một khoảng giờ, còn 时限 là hạn chót. Trong bài: 放宽免费时限, nới rộng thời hạn miễn phí."),
    ("告终", "gàozhōng", "cáo chung", "động từ", "kết thúc, chấm dứt", "这场比赛以平局告终。", "Trận đấu này kết thúc với tỷ số hòa.",
     "Động từ, văn viết, nghĩa là tuyên bố kết thúc. Mẫu cố định: 以……告终, kết thúc bằng…, như 以失败告终, kết thúc bằng thất bại. Tiếng Việt cáo chung cũng là kết thúc, cáo chung một thời đại."),
    ("若干", "ruògān", "nhược can", "đại từ", "một số, bao nhiêu (số lượng không xác định)", "若干年后，他又回到了这里。", "Nhiều năm sau, anh ấy lại quay về nơi này.",
     "Đại từ, văn viết, chỉ một số lượng không xác định, giống 一些，几. Hay gặp: 若干年，若干问题. Trong bài: 相信若干年以后的经济史中, tin rằng trong lịch sử kinh tế nhiều năm sau."),
    ("兴起", "xīngqǐ", "hưng khởi", "động từ", "nổi lên, bắt đầu thịnh hành", "最近年轻人中兴起了一股露营热。", "Gần đây giới trẻ nổi lên phong trào cắm trại.",
     "Động từ, nghĩa là bắt đầu xuất hiện và phát triển. Chú ý chữ đầu đọc thanh một, xīng, như trong 新兴; khác với 兴趣, xìngqù. Trong bài: 互联网兴起后, sau khi internet nổi lên."),
    ("默认", "mòrèn", "mặc nhận", "động từ", "mặc định; ngầm thừa nhận", "这是手机的默认设置。", "Đây là cài đặt mặc định của điện thoại.",
     "Động từ, nghĩa gốc là trong lòng thừa nhận nhưng không nói ra, tức là ngầm thừa nhận; trong tin học là mặc định. Trong bài: 免费服务成了默认模式, dịch vụ miễn phí trở thành mô hình mặc định."),
    ("颇", "pō", "phả", "phó từ", "khá, rất, tương đối", "他的话颇有道理。", "Lời anh ấy nói khá có lý.",
     "Phó từ, văn viết, nghĩa là khá, rất. Hay gặp: 颇为，颇具，颇感. Trong bài: 其中的原因颇为复杂, nguyên nhân trong đó khá phức tạp. Đây là kết hợp từ trọng điểm đầu tiên của bài."),
    ("小众", "xiǎozhòng", "tiểu chúng", "danh từ", "nhóm thiểu số; (sở thích) ít người theo", "这是一部很小众的电影。", "Đây là một bộ phim rất kén người xem.",
     "Danh từ, chỉ nhóm ít người, đối lập với 大众, đại chúng. Thường dùng như tính từ: 小众电影, 小众音乐, phim, nhạc ít người biết. Trong bài: 属于边缘小众群体, thuộc nhóm thiểu số bên lề."),
    ("浓厚", "nónghòu", "nùng hậu", "tính từ", "đậm đà, nồng đậm (hứng thú, không khí, màu sắc)", "他对中国历史有浓厚的兴趣。", "Anh ấy có hứng thú sâu sắc với lịch sử Trung Quốc.",
     "Tính từ, chỉ mức độ sâu, đậm, dùng cho màu sắc, ý thức, không khí, hứng thú. Chú ý: tiếng Việt nồng hậu là nói về tình cảm đón tiếp; còn 浓厚 hay đi với 兴趣，氛围，色彩. Đây là một kết hợp từ trọng điểm."),
    ("乌托邦", "wūtuōbāng", "ô thác bang", "danh từ", "xứ sở không tưởng, Utopia", "完全平等的社会只是一个乌托邦。", "Một xã hội hoàn toàn bình đẳng chỉ là một xứ sở không tưởng.",
     "Danh từ, là phiên âm của Utopia, tên cuốn sách của Thomas More, chỉ một thế giới lý tưởng không có thật. Trong bài: 互联网乌托邦, xứ sở không tưởng internet."),
    ("意识形态", "yìshí xíngtài", "ý thức hình thái", "danh từ", "hệ tư tưởng, hình thái ý thức", "两国的意识形态不同。", "Hệ tư tưởng của hai nước khác nhau.",
     "Danh từ, chỉ hệ thống quan điểm của con người về thế giới và xã hội, thể hiện qua triết học, chính trị, pháp luật, nghệ thuật, tôn giáo, đạo đức. Tiếng Việt gọi là hệ tư tưởng hoặc hình thái ý thức."),
    ("排斥", "páichì", "bài xích", "động từ", "bài xích, gạt bỏ, loại trừ", "新同学刚来时受到了一些排斥。", "Bạn học mới lúc đầu bị bài xích ít nhiều.",
     "Động từ, nghĩa là đẩy người hay sự vật khác ra khỏi phía mình. Âm Hán Việt và nghĩa giống tiếng Việt. Hay gặp: 受到排斥，排斥他人. Trong bài: 商业化受到普遍的排斥."),
    ("趋近", "qūjìn", "xu cận", "động từ", "tiến gần, xích lại gần", "两国的看法逐渐趋近。", "Quan điểm của hai nước dần xích lại gần nhau.",
     "Động từ, nghĩa là có xu hướng tiến gần tới. So với 趋于 ở bài trước, 趋近 nhấn mạnh sự tiếp cận. Trong bài: 大众化的互联网生态趋近现实社会, hệ sinh thái internet đại chúng ngày càng giống xã hội thực."),
    ("驱动", "qūdòng", "khu động", "động từ", "thúc đẩy, dẫn động", "这辆车是用电驱动的。", "Chiếc xe này chạy bằng điện.",
     "Động từ, nghĩa là dùng lực bên ngoài làm cho chuyển động; nghĩa bóng là thúc đẩy. 驱动力 là động lực; 利益驱动 là bị lợi ích chi phối. Trong bài: 驱动力已然不同, động lực đã khác."),
    ("取代", "qǔdài", "thủ đại", "động từ", "thay thế, thế chỗ", "智能手机已经取代了很多传统设备。", "Điện thoại thông minh đã thay thế rất nhiều thiết bị truyền thống.",
     "Động từ, nghĩa là gạt người hay vật khác đi để thế vào chỗ đó. Phân biệt: 代替 là thay mặt, thay vào, trung tính; 取代 nhấn mạnh cái mới chiếm hẳn chỗ của cái cũ. Trong bài: 互联网营销取代了原来的乌托邦理想."),
    ("标配", "biāopèi", "tiêu phối", "danh từ", "cấu hình tiêu chuẩn; thứ mặc nhiên phải có", "现在手机几乎是每个人的标配。", "Bây giờ điện thoại gần như là thứ ai cũng phải có.",
     "Danh từ, nói tắt của 标准配置, cấu hình tiêu chuẩn của máy móc; nghĩa mở rộng là thứ mặc nhiên phải có. Trong bài: 广告收入成为了互联网企业的标配, thu nhập quảng cáo thành thứ doanh nghiệp internet nào cũng có."),
    ("涉足", "shèzú", "thiệp túc", "động từ", "đặt chân vào, dấn thân vào (lĩnh vực)", "这家公司开始涉足房地产行业。", "Công ty này bắt đầu lấn sân sang ngành bất động sản.",
     "Động từ, nghĩa đen là đặt chân vào, nghĩa bóng là bước vào một môi trường, lĩnh vực nào đó, giống lấn sân. Trong bài: 无需深度涉足互联网企业的业务, không cần dấn sâu vào nghiệp vụ của doanh nghiệp internet."),
    ("微薄", "wēibó", "vi bạc", "tính từ", "ít ỏi, nhỏ nhoi", "他靠微薄的工资养活一家人。", "Anh ấy nuôi cả nhà bằng đồng lương ít ỏi.",
     "Tính từ, nghĩa là nhỏ bé, ít ỏi, thường nói về thu nhập, sức lực. Hay gặp: 微薄的收入, 尽一份微薄之力, góp một phần sức nhỏ. Trong bài: 微薄的广告收益, nguồn thu quảng cáo ít ỏi."),
    ("亏损", "kuīsǔn", "khuy tổn", "động từ", "thua lỗ, lỗ vốn", "这家公司去年亏损了五千万元。", "Năm ngoái công ty này lỗ năm mươi triệu tệ.",
     "Động từ, nghĩa là chi vượt thu, bị lỗ. Trái nghĩa là 盈利, có lãi. Trong bài: 大规模亏损却又欣欣向荣的企业群体, những doanh nghiệp lỗ khổng lồ mà vẫn phát triển rực rỡ."),
    ("烧钱", "shāo qián", "thiêu tiền", "động từ", "đốt tiền, tiêu tiền như đốt", "拍这部电影可烧了不少钱。", "Quay bộ phim này đã đốt không ít tiền.",
     "Động từ, nghĩa là tiêu tiền nhiều và nhanh như đốt; cũng chỉ việc bỏ thật nhiều vốn mà không tính đến lợi nhuận trước mắt. Tiếng Việt cũng nói đốt tiền. Trong bài: 烧钱获客, đốt tiền để giành khách."),
    ("反常", "fǎncháng", "phản thường", "tính từ", "bất thường, khác thường", "这几天他的举动很反常。", "Mấy hôm nay cử chỉ của anh ấy rất bất thường.",
     "Tính từ, nghĩa là khác với tình trạng bình thường. Hay gặp: 表现反常，气候反常. Trong bài: 资本请客的白吃白喝，着实有点反常, ăn chùa uống chùa do giới tư bản mời, quả thật có phần bất thường."),
    ("幸运儿", "xìngyùn'ér", "hạnh vận nhi", "danh từ", "người may mắn, đứa con cưng của số phận", "他是这次抽奖的幸运儿。", "Anh ấy là người may mắn trong lần bốc thăm trúng thưởng này.",
     "Danh từ, nghĩa là người may mắn. Trong bài, internet được nhân hóa: 互联网是时代的幸运儿, internet là đứa con may mắn của thời đại."),
    ("热钱", "rèqián", "nhiệt tiền", "danh từ", "tiền nóng (dòng vốn đầu cơ ngắn hạn)", "大量热钱流入了股市。", "Một lượng lớn tiền nóng đã chảy vào thị trường chứng khoán.",
     "Danh từ, thuật ngữ tài chính, chỉ dòng vốn ngắn hạn chảy đi khắp nơi tìm lợi nhuận nhanh. Bảng từ của sách ghi là động từ, nhưng thực chất đây là danh từ. Tiếng Việt cũng gọi là tiền nóng."),
    ("流入", "liúrù", "lưu nhập", "động từ", "chảy vào, đổ vào", "这条河最后流入大海。", "Con sông này cuối cùng đổ ra biển.",
     "Động từ, nghĩa là chảy vào; nghĩa bóng là tiền, người, hàng hóa đổ vào một nơi. Trái nghĩa là 流出. Trong bài: 大量热钱流入金融资本市场."),
    ("难怪", "nánguài", "nan quái", "phó từ", "thảo nào, hèn chi, chẳng trách", "原来他是北京人，难怪普通话说得这么好。", "Thì ra anh ấy là người Bắc Kinh, thảo nào nói tiếng phổ thông hay đến thế.",
     "Phó từ, biểu thị đã hiểu ra nguyên nhân nên không còn thấy lạ nữa, giống 怪不得. Đây là mẫu câu thứ sáu của bài."),
    ("次于", "cìyú", "thứ vu", "động từ", "kém hơn, đứng sau", "他的成绩仅次于第一名。", "Thành tích của anh ấy chỉ đứng sau người hạng nhất.",
     "Động từ, nghĩa là kém hơn, xếp sau. Hầu như luôn đi với 仅: 仅次于, chỉ đứng sau. Trong bài: 互联网成为仅次于房地产的第二大受益者, internet thành bên hưởng lợi lớn thứ hai, chỉ sau bất động sản."),
    ("受益", "shòuyì", "thụ ích", "động từ", "được lợi, hưởng lợi", "这项政策让很多农民受益。", "Chính sách này giúp rất nhiều nông dân được hưởng lợi.",
     "Động từ, nghĩa là nhận được lợi ích. 受益者 là người hưởng lợi; 受益匪浅 là được lợi không ít, hay dùng khi cảm ơn một bài giảng, một lời khuyên."),
    ("造就", "zàojiù", "tạo tựu", "động từ", "tạo nên, đào tạo nên", "艰苦的环境造就了他坚强的性格。", "Hoàn cảnh gian khổ đã tạo nên tính cách kiên cường của anh ấy.",
     "Động từ, nghĩa là bồi dưỡng cho thành tài, tạo nên. Phân biệt: 造就 thường đi với kết quả tốt, như nhân tài, tính cách; còn 造成 thường đi với kết quả xấu, như 造成损失. Trong bài: 不差钱的时代造就了烧钱的互联网营销."),
    ("副作用", "fùzuòyòng", "phó tác dụng", "danh từ", "tác dụng phụ", "这种药的副作用很小。", "Loại thuốc này có tác dụng phụ rất nhỏ.",
     "Danh từ, chỉ tác dụng xấu đi kèm ngoài tác dụng chính. Dùng cho thuốc men, cũng dùng nghĩa bóng cho chính sách. Trong bài: 掩盖了货币超发的副作用, che lấp tác dụng phụ của việc phát hành tiền vượt mức."),
    ("超发", "chāofā", "siêu phát", "động từ", "phát hành vượt mức (tiền tệ)", "货币超发容易引起通货膨胀。", "Phát hành tiền vượt mức dễ gây ra lạm phát.",
     "Động từ, thuật ngữ kinh tế, chỉ việc tổng mệnh giá tiền phát hành lớn hơn tổng giá trị của nền kinh tế. Hay gặp: 货币超发. 通货膨胀 trong ví dụ là lạm phát."),
    ("沉淀", "chéndiàn", "trầm điện", "động từ", "lắng xuống, lắng đọng; tích tụ", "这些经验需要时间来沉淀。", "Những kinh nghiệm này cần thời gian để lắng đọng.",
     "Động từ, nghĩa gốc là chất rắn lắng xuống đáy nước; nghĩa bóng là lắng lại, tích lũy dần. Trong bài: 超发货币在互联网领域的新兴产业沉淀, tiền phát hành dư lắng đọng trong các ngành mới nổi của internet."),
    ("泡沫", "pàomò", "bào mạt", "danh từ", "bọt; bong bóng (kinh tế)", "很多人担心房地产会出现泡沫。", "Nhiều người lo bất động sản sẽ xuất hiện bong bóng.",
     "Danh từ, nghĩa gốc là bọt nước; nghĩa bóng chỉ sự phồn vinh giả tạo, hão huyền. Bảng từ của sách ghi là động từ, nhưng thực chất là danh từ. Hay gặp: 泡沫经济, kinh tế bong bóng; 房地产泡沫, bong bóng bất động sản."),
    ("遵循", "zūnxún", "tuân tuần", "động từ", "tuân theo, làm theo", "做事要遵循客观规律。", "Làm việc phải tuân theo quy luật khách quan.",
     "Động từ, nghĩa là tuân theo. Phân biệt: 遵守 đi với luật lệ, kỷ luật cụ thể, như 遵守交通规则; còn 遵循 đi với quy luật, nguyên tắc, logic, như 遵循规律. Đây là một kết hợp từ trọng điểm."),
    ("悬念", "xuánniàn", "huyền niệm", "danh từ", "sự hồi hộp, tình tiết gây tò mò; điều chưa ngã ngũ", "这部电影悬念不断，非常吸引人。", "Bộ phim này liên tục có những tình tiết gây hồi hộp, rất cuốn hút.",
     "Danh từ, chỉ tâm lý rất muốn biết diễn biến, kết cục mà không đoán trước được khi xem phim, đọc truyện. 毫无悬念 là không có chút bất ngờ nào, kết quả đã rõ. Trong bài: 免费时代的终结已经毫无悬念."),
    ("注定", "zhùdìng", "chú định", "động từ", "định sẵn, đã được định trước", "没有准备的人注定会失败。", "Người không chuẩn bị thì định sẵn sẽ thất bại.",
     "Động từ, nghĩa là do quy luật hay số phận định trước, chắc chắn sẽ như vậy. Trong bài: 注定伴随着痛苦指数的上升, chắc chắn sẽ đi kèm với chỉ số đau đớn tăng lên."),
    ("迈", "mài", "mại", "động từ", "bước, sải bước", "他迈出了人生的第一步。", "Anh ấy đã bước bước đầu tiên của cuộc đời.",
     "Động từ, nghĩa là nhấc chân bước tới. Hay dùng nghĩa bóng: 迈向成熟, tiến tới trưởng thành; 迈出一步, bước một bước. Trong bài: 互联网经济迈向成熟的标志."),
    ("轻狂", "qīngkuáng", "khinh cuồng", "tính từ", "nông nổi ngông cuồng", "年轻时他有些轻狂，现在成熟多了。", "Hồi trẻ anh ấy hơi nông nổi ngông cuồng, bây giờ chín chắn hơn nhiều.",
     "Tính từ, nghĩa là nông nổi, ngông cuồng. Cụm hay gặp: 年少轻狂, tuổi trẻ bồng bột ngông cuồng, như trong bài: 年少轻狂的乌托邦理想."),
    ("违背", "wéibèi", "vi bội", "động từ", "làm trái, đi ngược", "这样做违背了我的原则。", "Làm như vậy là đi ngược nguyên tắc của tôi.",
     "Động từ, nghĩa là làm trái, không tuân theo. Hay gặp: 违背规律，违背承诺，违背良心. Trong bài: 违背常理的烧钱狂欢, cuộc cuồng hoan đốt tiền đi ngược lẽ thường."),
    ("常理", "chánglǐ", "thường lý", "danh từ", "lẽ thường, đạo lý thông thường", "按常理，他今天应该到了。", "Theo lẽ thường, hôm nay anh ấy lẽ ra đã đến rồi.",
     "Danh từ, nghĩa là đạo lý thông thường. Hay gặp: 按常理，违背常理, 不合常理."),
    ("狂欢", "kuánghuān", "cuồng hoan", "động từ", "vui chơi cuồng nhiệt, thả cửa", "新年夜，人们在广场上狂欢。", "Đêm giao thừa, mọi người vui chơi cuồng nhiệt trên quảng trường.",
     "Động từ, nghĩa là vui chơi thỏa thích, cuồng nhiệt. 狂欢节 là lễ hội carnival. Trong bài dùng nghĩa bóng, mang ý chê: 烧钱狂欢, cuộc cuồng hoan đốt tiền."),
    ("管控", "guǎnkòng", "quản khống", "động từ", "quản lý và kiểm soát", "银行必须加强风险管控。", "Ngân hàng phải tăng cường quản lý, kiểm soát rủi ro.",
     "Động từ, nghĩa là quản lý và khống chế. Hay gặp: 风险管控, kiểm soát rủi ro; 疫情管控, kiểm soát dịch bệnh."),
    ("留恋", "liúliàn", "lưu luyến", "động từ", "lưu luyến, không nỡ rời xa", "毕业多年，大家仍然留恋母校。", "Tốt nghiệp nhiều năm, mọi người vẫn lưu luyến trường cũ.",
     "Động từ, nghĩa là không nỡ bỏ, không nỡ rời. Âm Hán Việt và nghĩa giống hệt tiếng Việt. Hay gặp: 留恋过去，值得留恋，毫不留恋. Đây là một kết hợp từ trọng điểm."),
    ("休", "xiū", "hưu", "động từ", "thôi, dừng, chấm dứt", "这件事就此罢休吧。", "Chuyện này đến đây thì thôi nhé.",
     "Động từ, nghĩa gốc là nghỉ, như 休息; ở đây là thôi, chấm dứt, như 罢休, 善罢甘休. Trong bài: 免费午餐可以休矣, bữa trưa miễn phí có thể thôi được rồi."),
    ("矣", "yǐ", "hĩ", "trợ từ", "(văn ngôn) rồi, đặt cuối câu, giống 了", "此事可以休矣。", "Chuyện này có thể thôi được rồi.",
     "Trợ từ văn ngôn, đặt cuối câu, giống 了 trong tiếng hiện đại. Âm Hán Việt là hĩ, như trong câu văn cổ 足矣, đủ rồi. Mẫu 可以休矣 là mẫu câu thứ năm của bài."),
    ("逐一", "zhúyī", "trục nhất", "phó từ", "lần lượt từng cái, từng cái một", "老师对学生的问题逐一作了回答。", "Thầy giáo lần lượt trả lời từng câu hỏi của học sinh.",
     "Phó từ, nghĩa là từng cái một, lần lượt, giống 逐个. Chữ 逐 là lần lượt, như trong 逐步, 逐渐. Trong bài: 当年埋下的雷会逐一引爆, những quả mìn chôn năm ấy sẽ lần lượt phát nổ."),
    ("雷", "léi", "lôi", "danh từ", "mìn; sấm", "士兵们正在排雷。", "Những người lính đang rà phá mìn.",
     "Danh từ, nghĩa gốc là sấm, như 打雷, sấm rền; ở đây là mìn, nói tắt của 地雷. Nghĩa bóng là mối nguy tiềm ẩn: 埋雷, chôn mìn; 踩雷, giẫm phải mìn, tức là gặp rắc rối."),
    ("引爆", "yǐnbào", "dẫn bộc", "động từ", "kích nổ; (nghĩa bóng) làm bùng nổ", "这条新闻引爆了网络。", "Tin tức này đã làm bùng nổ cõi mạng.",
     "Động từ, nghĩa gốc là dùng thiết bị kích nổ cho vật liệu nổ phát nổ; nghĩa bóng là làm bùng nổ, như 引爆话题, làm bùng nổ một chủ đề."),
    ("侥幸", "jiǎoxìng", "kiểu hạnh", "tính từ", "may mắn (nhờ ngẫu nhiên); cầu may", "不要存侥幸心理。", "Đừng mang tâm lý cầu may.",
     "Tính từ, nghĩa là nhờ ngẫu nhiên mà thành công hay thoát nạn. Cụm hay gặp: 侥幸心理, tâm lý cầu may. Câu cuối bài chơi chữ: 没有侥幸，只有瑞幸."),
]

add("bullets", chapter="Từ mới (51 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 7.2 có 51 từ mới, chia thành 17 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 兴起 (xīng) · 涉足 (shèzú) · 矣 (yǐ) · 年少轻狂 (shào)",
           "Nhiều thuật ngữ kinh tế: 亏损 · 烧钱 · 热钱 · 超发 · 泡沫 · 管控"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có năm mươi mốt từ, thầy chia thành mười bảy nhóm nhỏ, mỗi nhóm ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Chú ý cách đọc của một số chữ: 兴起 đọc là xīngqǐ; 涉足 đọc là shèzú; 矣 đọc là yǐ; và trong cụm 年少轻狂, chữ 少 đọc thanh bốn, shào."),
         F(4, "Bài này có rất nhiều thuật ngữ kinh tế, như 亏损，烧钱，热钱，超发，泡沫，管控. Bảng từ của sách có vài chỗ ghi nhầm từ loại, như 热钱 và 泡沫 bị ghi là động từ; thầy sẽ nhắc khi gặp. Chúng ta bắt đầu.")])

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
    ("“丰巢收取超时费，十二小时免费时段之外，每小时收取0.5元，封顶3元。”这一变动瞬间引发了网民们的热议，最终以企业妥协、放宽免费时限告终，好在收费的目的还是达到了，相信若干年以后的经济史中会浓墨重彩地记录这一“五毛钱”事件，它标志着互联网经济“免费时代”的终结。",
     "“Phong Sào thu phí quá giờ: ngoài khung 12 giờ miễn phí, mỗi giờ thu 0,5 tệ, tối đa 3 tệ.” Thay đổi này lập tức gây ra cuộc tranh luận sôi nổi trên mạng, cuối cùng kết thúc bằng việc doanh nghiệp nhượng bộ, nới rộng thời hạn miễn phí. May là mục đích thu phí vẫn đạt được. Tin rằng nhiều năm sau, lịch sử kinh tế sẽ ghi đậm nét sự kiện “năm hào” này, nó đánh dấu sự kết thúc của “thời đại miễn phí” trong kinh tế internet.",
     ["丰巢 là Hive Box, công ty tủ nhận hàng thông minh ở Thâm Quyến: shipper bỏ hàng vào tủ, người nhận quét mã lấy hàng. 超时费 là phí quá giờ; 时段 là khung giờ; 封顶 là mức trần. 五毛钱 là năm hào, tức nửa tệ.",
      "瞬间 là trong chớp mắt. 以……告终 là kết thúc bằng…; 妥协 là nhượng bộ. 好在 là may mà. 浓墨重彩地记录 là ghi lại thật đậm nét, một thành ngữ trọng điểm. 标志着 là đánh dấu. Chỉ năm hào thôi, nhưng tác giả coi đó là dấu mốc của cả một thời đại."],
     "丰巢收取超时费，十二小时免费时段之外，每小时收取零点五元，封顶三元。这一变动瞬间引发了网民们的热议，最终以企业妥协、放宽免费时限告终，好在收费的目的还是达到了，相信若干年以后的经济史中会浓墨重彩地记录这一五毛钱事件，它标志着互联网经济免费时代的终结。"),
    ("互联网兴起后，“免费服务”作为绝对主流，成了默认模式。其中的原因颇为复杂。互联网早期，是一个“理想主义时期”，这一时期，互联网参与者的社会比重不高，属于边缘小众群体，自娱自乐的氛围浓厚。",
     "Sau khi internet nổi lên, “dịch vụ miễn phí” với tư cách là dòng chủ lưu tuyệt đối đã trở thành mô hình mặc định. Nguyên nhân trong đó khá phức tạp. Thời kỳ đầu, internet là một “thời kỳ lý tưởng chủ nghĩa”; trong thời kỳ này, tỷ lệ người tham gia internet trong xã hội không cao, họ thuộc về một nhóm nhỏ bên lề, bầu không khí tự mua vui cho nhau rất đậm.",
     ["作为绝对主流 là với tư cách dòng chủ lưu tuyệt đối. 默认模式 là mô hình mặc định. 颇为复杂 là khá phức tạp; 颇为 cộng tính từ hai âm tiết, rất hay gặp trong văn viết.",
      "比重 là tỷ trọng, chữ sau đọc là zhòng. 边缘小众群体 là nhóm thiểu số bên lề xã hội. 自娱自乐 là thành ngữ: tự mua vui cho mình. 氛围浓厚 là bầu không khí đậm đà. Đây là giai đoạn thứ nhất của sự miễn phí: miễn phí vì lý tưởng."]),
    ("而且，年龄也偏低，“公开共享”是互联网乌托邦的主流意识形态。日常运营维护依靠热心玩家的业余支持，商业化受到普遍的排斥。",
     "Hơn nữa, độ tuổi cũng khá thấp, “công khai chia sẻ” là hệ tư tưởng chủ đạo của xứ sở không tưởng internet. Việc vận hành, bảo trì hằng ngày dựa vào sự hỗ trợ nghiệp dư của những người chơi nhiệt tình, còn thương mại hóa thì bị bài xích ở khắp nơi.",
     ["偏低 là hơi thấp, thiên về thấp. 公开共享 là công khai chia sẻ, ví dụ phần mềm mã nguồn mở, diễn đàn chia sẻ tài liệu miễn phí. 乌托邦 là Utopia; 意识形态 là hệ tư tưởng.",
      "运营维护 là vận hành và bảo trì. 热心玩家 là những người chơi nhiệt tình; 业余 là nghiệp dư, làm ngoài giờ. 受到普遍的排斥 là bị bài xích khắp nơi: thời ấy, ai nói chuyện kiếm tiền trên mạng là bị coi thường."]),
    ("“理想主义时期”持续的时间并不长，随着互联网应用的普及，大众化的互联网生态趋近现实社会。免费模式还在继续，但驱动力已然不同。",
     "“Thời kỳ lý tưởng chủ nghĩa” kéo dài không lâu. Cùng với sự phổ cập của các ứng dụng internet, hệ sinh thái internet đại chúng hóa ngày càng tiến gần xã hội thực. Mô hình miễn phí vẫn tiếp tục, nhưng động lực thúc đẩy nó đã khác rồi.",
     ["随着……的普及 là cùng với sự phổ cập của…, mẫu câu thứ nhất. 大众化 là đại chúng hóa. 生态 là hệ sinh thái. 趋近现实社会 là tiến gần xã hội thực: trên mạng cũng có đủ hạng người, đủ chuyện như ngoài đời.",
      "驱动力 là động lực thúc đẩy. 已然 là đã, văn viết, giống 已经. Câu này là bản lề của bài: miễn phí vẫn còn, nhưng không còn vì lý tưởng nữa."]),
    ("所谓“互联网营销”取代了原来的乌托邦理想，从营销角度维持“免费”的形式。而此时的“免费”已经不是愤世嫉俗的反商业化，广告收入成为了互联网企业的标配。",
     "Cái gọi là “tiếp thị internet” đã thay thế lý tưởng không tưởng ban đầu, duy trì hình thức “miễn phí” từ góc độ tiếp thị. Còn “miễn phí” lúc này đã không còn là sự chống thương mại hóa kiểu bất bình với đời nữa, thu nhập từ quảng cáo đã trở thành thứ doanh nghiệp internet nào cũng có.",
     ["所谓 là cái gọi là. 营销 là tiếp thị, marketing. 取代 là thay thế. 从营销角度维持免费的形式: miễn phí giờ chỉ là hình thức, một chiêu tiếp thị để kéo người dùng. Đây là giai đoạn thứ hai: miễn phí vì tiếp thị.",
      "愤世嫉俗 là thành ngữ: căm ghét thói đời, bất bình với xã hội. 反商业化 là chống thương mại hóa. 标配 là cấu hình tiêu chuẩn, thứ ai cũng phải có, dạng nói tắt của 标准配置."]),
    ("广告收入的优势在于，无需深度涉足互联网企业的业务，可以单纯从流量中产生收益，第三方买单在形式上维护了用户免费的舒适感。",
     "Ưu thế của thu nhập quảng cáo nằm ở chỗ: không cần dấn sâu vào nghiệp vụ của doanh nghiệp internet, chỉ đơn thuần từ lưu lượng truy cập là có thể sinh ra lợi nhuận; bên thứ ba trả tiền, về hình thức đã giữ được cảm giác dễ chịu vì được dùng miễn phí của người dùng.",
     ["……的优势在于 là ưu thế của… nằm ở chỗ, mẫu câu thứ hai. 无需 là không cần. 深度涉足 là dấn sâu vào. 流量 là lưu lượng, lượt truy cập. 收益 là lợi nhuận, thu nhập.",
      "第三方买单 là bên thứ ba trả tiền: người dùng xem miễn phí, nhà quảng cáo trả tiền. 买单 vốn là thanh toán hóa đơn ở nhà hàng. 舒适感 là cảm giác dễ chịu. Chữ 在形式上 ngầm nói: về thực chất, người dùng vẫn trả bằng thời gian và sự chú ý của mình."]),
    ("然而绝大部分互联网企业都不能靠微薄的广告收益维持经营，人类经济活动中首次出现了大规模亏损却又欣欣向荣的企业群体，这就是“互联网营销”的奇妙之处。以金钱换时间，以时间换规模，烧钱获客、规模为王。",
     "Thế nhưng tuyệt đại đa số doanh nghiệp internet đều không thể dựa vào nguồn thu quảng cáo ít ỏi để duy trì kinh doanh; lần đầu tiên trong hoạt động kinh tế của loài người xuất hiện một nhóm doanh nghiệp vừa thua lỗ quy mô lớn lại vừa phát triển rực rỡ, đó chính là chỗ kỳ diệu của “tiếp thị internet”. Lấy tiền đổi thời gian, lấy thời gian đổi quy mô, đốt tiền giành khách, quy mô là vua.",
     ["微薄 là ít ỏi. 维持经营 là duy trì kinh doanh. 亏损却又欣欣向荣: vừa lỗ vừa phát triển rực rỡ, nghịch lý của thời internet. 欣欣向荣 là thành ngữ: cây cỏ tươi tốt, ví với sự nghiệp hưng thịnh. 奇妙之处 là chỗ kỳ diệu.",
      "以金钱换时间，以时间换规模 là mẫu câu thứ ba 以A换B, lấy A đổi B. 烧钱获客 là đốt tiền giành khách. 规模为王 là quy mô là vua, chữ thứ ba đọc là wéi. Đây là giai đoạn thứ ba: miễn phí vì tư bản đốt tiền."]),
    ("此时的互联网免费，是“资本请客”的白吃白喝，着实有点反常。其实，“赔本赚吆喝”不是创新，连传统相声《卖布头》都会反复讲“先赔后赚”的道理。",
     "Miễn phí trên internet lúc này là kiểu ăn chùa uống chùa do “tư bản mời khách”, quả thật có phần bất thường. Thực ra, “chịu lỗ để lấy tiếng” chẳng phải sáng tạo gì mới, ngay cả tiết mục tấu nói truyền thống “Bán vải vụn” cũng nhắc đi nhắc lại đạo lý “lỗ trước lãi sau”.",
     ["资本请客 là tư bản mời khách, tức nhà đầu tư bỏ tiền ra trợ giá cho người dùng. 白吃白喝 là ăn uống chùa, không mất tiền. 着实 là quả thật, chữ đầu đọc là zhuó. 反常 là bất thường, một kết hợp từ trọng điểm.",
      "赔本赚吆喝 là quán ngữ: bán lỗ để kiếm tiếng rao, tức là chịu lỗ để gây tiếng tăm, kéo khách. 相声 là tấu nói, một loại hình nghệ thuật hài của Trung Quốc. 卖布头 là Bán vải vụn. 先赔后赚 là lỗ trước lãi sau."]),
    ("“获客成本”和此前企业的营销成本、广告成本没有本质的区别。只不过，传统企业哪有持续烧钱几个月、几年的能力？",
     "“Chi phí giành khách” và chi phí tiếp thị, chi phí quảng cáo của doanh nghiệp trước đây không khác nhau về bản chất. Chỉ có điều, doanh nghiệp truyền thống làm gì có khả năng đốt tiền liên tục mấy tháng, mấy năm trời?",
     ["获客成本 là chi phí thu hút khách hàng, thuật ngữ marketing. 此前 là trước đây. 没有本质的区别 là không khác nhau về bản chất.",
      "只不过 là chỉ có điều. 哪有……的能力 là câu hỏi tu từ: làm gì có khả năng…, tức là hoàn toàn không có. Tác giả ngầm hỏi: vậy tiền đâu ra để internet đốt? Đoạn sau sẽ trả lời."]),
    ("互联网是时代的幸运儿，赶上了各国政府超发货币的饕餮盛宴。大量热钱流入金融资本市场，为互联网烧钱提供了充足的燃料。这就难怪在金融资本市场中互联网成为仅次于房地产的第二大受益者，“不差钱”的时代造就了烧钱的“互联网营销”。",
     "Internet là đứa con may mắn của thời đại, gặp đúng bữa tiệc thịnh soạn mang tên phát hành tiền vượt mức của chính phủ các nước. Một lượng lớn tiền nóng chảy vào thị trường vốn tài chính, cung cấp nhiên liệu dồi dào cho internet đốt tiền. Thảo nào trên thị trường vốn tài chính, internet trở thành bên hưởng lợi lớn thứ hai, chỉ sau bất động sản; thời đại “không thiếu tiền” đã tạo nên “tiếp thị internet” kiểu đốt tiền.",
     ["幸运儿 là người may mắn. 赶上 là gặp đúng dịp. 超发货币 là phát hành tiền vượt mức: các ngân hàng trung ương in thêm tiền để kích thích kinh tế. 饕餮盛宴 là bữa tiệc linh đình; 饕餮 là con quái thú tham ăn trong truyền thuyết.",
      "热钱 là tiền nóng. 燃料 là nhiên liệu, nối tiếp hình ảnh đốt tiền. 难怪 là thảo nào, mẫu câu thứ sáu. 仅次于 là chỉ đứng sau. 不差钱 là không thiếu tiền, câu nói nổi tiếng từ tiểu phẩm cùng tên trên Xuân vãn năm 2009."]),
    ("换一个角度看，互联网的烧钱高潮掩盖了货币超发的副作用，多少有点“瞎猫撞到死耗子”的喜剧氛围。",
     "Nhìn từ một góc độ khác, cao trào đốt tiền của internet đã che lấp tác dụng phụ của việc phát hành tiền vượt mức, ít nhiều mang không khí hài kịch kiểu “mèo mù vớ cá rán”.",
     ["换一个角度看 là nhìn từ góc độ khác, mẫu câu thứ tư. 高潮 là cao trào. 掩盖 là che đậy. 副作用 là tác dụng phụ: in nhiều tiền thường gây lạm phát, nhưng tiền đổ vào internet nên tác hại chưa lộ ra.",
      "瞎猫撞到死耗子 là quán ngữ: mèo mù đụng phải chuột chết, giống câu mèo mù vớ cá rán của tiếng Việt: chẳng có tài cán gì mà lại gặp may. 多少有点 là ít nhiều có phần. 喜剧氛围 là không khí hài kịch."]),
    ("超发货币在互联网领域的新兴产业沉淀，一部分以“请客吃饭”的形式转为商品消费，其中确实产生了真金白银的社会效益，但也积累了不少的泡沫。长此以往，难以为继。",
     "Tiền phát hành vượt mức lắng đọng trong các ngành mới nổi của lĩnh vực internet, một phần chuyển thành tiêu dùng hàng hóa dưới hình thức “mời khách ăn uống”, trong đó quả thật đã tạo ra lợi ích xã hội bằng vàng thật bạc thật, nhưng cũng tích tụ không ít bong bóng. Cứ kéo dài mãi như thế thì khó lòng duy trì được.",
     ["沉淀 là lắng đọng, tích tụ lại. 新兴产业 là ngành mới nổi. 以请客吃饭的形式 là dưới hình thức mời khách ăn uống, ví dụ trợ giá cho người dùng gọi xe, gọi đồ ăn. 转为 là chuyển thành.",
      "真金白银 là vàng thật bạc thật, tức lợi ích thực sự. 泡沫 là bong bóng kinh tế. 长此以往 là cứ kéo dài như thế mãi; 难以为继 là khó lòng duy trì, chữ thứ ba đọc là wéi. Hai thành ngữ này thường đi liền nhau."]),
    ("任何投资最终都要遵循基本的商业逻辑，天下没有永远免费的午餐。新冠来袭之前，摆在大部分互联网企业面前的已经不是收不收费的问题，而是怎么收费合适。新冠对经济的冲击更造成了资本的冬季。丰巢不是第一家终结免费的互联网企业，也不会是最后一家。",
     "Bất kỳ khoản đầu tư nào rốt cuộc cũng phải tuân theo logic kinh doanh cơ bản: trên đời không có bữa trưa nào miễn phí mãi. Trước khi Covid ập đến, vấn đề đặt ra trước mặt phần lớn doanh nghiệp internet đã không phải là có thu phí hay không, mà là thu phí thế nào cho hợp lý. Cú sốc của Covid đối với kinh tế càng gây ra mùa đông của nguồn vốn. Phong Sào không phải doanh nghiệp internet đầu tiên chấm dứt miễn phí, và cũng sẽ không phải là doanh nghiệp cuối cùng.",
     ["遵循 là tuân theo: 遵循商业逻辑. 天下没有永远免费的午餐 là tên bài. 新冠 là Covid-19, nói tắt của 新冠肺炎; 来袭 là ập tới.",
      "不是A的问题，而是B: không phải chuyện A mà là chuyện B. 收不收费 là có thu phí hay không. 资本的冬季 là mùa đông của vốn, khi nhà đầu tư không dám rót tiền. 不是第一家，也不会是最后一家: không phải người đầu tiên, cũng chẳng phải người cuối cùng."]),
    ("免费时代的终结已经毫无悬念。走出免费的舒适区，注定伴随着痛苦指数的上升，企业要面对失去客户的风险，客户要承担支出的成本。可冷静思考，还是应该承认进入收费时代是互联网经济迈向成熟的标志。",
     "Sự kết thúc của thời đại miễn phí đã không còn gì phải bàn cãi. Bước ra khỏi vùng thoải mái của miễn phí, chắc chắn sẽ đi kèm với chỉ số đau đớn tăng lên: doanh nghiệp phải đối mặt với nguy cơ mất khách, khách hàng phải gánh thêm chi phí. Nhưng suy nghĩ bình tĩnh, vẫn nên thừa nhận rằng bước vào thời đại thu phí là dấu hiệu nền kinh tế internet tiến tới trưởng thành.",
     ["毫无悬念 là không còn chút hồi hộp nào, tức là kết quả đã rõ. 舒适区 là vùng thoải mái, comfort zone. 注定 là định sẵn, chắc chắn sẽ. 痛苦指数 là chỉ số đau đớn.",
      "可 ở đây là nhưng, giống 可是. 冷静思考 là suy nghĩ bình tĩnh. 迈向成熟 là tiến tới trưởng thành; 迈 là sải bước. 标志 là dấu hiệu. Tác giả đánh giá tích cực: thu phí là điều tất yếu và lành mạnh."]),
    ("年少轻狂的乌托邦理想不能支撑产业的持续健康发展，违背常理的烧钱狂欢只能是一场高风险的游戏。以合理的利润预期为前提进行有效的风险管控，金融投资才会有长期的社会效益。",
     "Lý tưởng không tưởng của tuổi trẻ bồng bột không thể chống đỡ sự phát triển lành mạnh, bền vững của cả một ngành; cuộc cuồng hoan đốt tiền đi ngược lẽ thường chỉ có thể là một trò chơi rủi ro cao. Lấy kỳ vọng lợi nhuận hợp lý làm tiền đề để kiểm soát rủi ro hiệu quả, đầu tư tài chính mới có lợi ích xã hội lâu dài.",
     ["年少轻狂 là tuổi trẻ bồng bột ngông cuồng, chữ thứ hai đọc là shào. 支撑 là chống đỡ. 违背常理 là đi ngược lẽ thường. 狂欢 là cuồng hoan, vui chơi thả cửa.",
      "以……为前提 là lấy… làm tiền đề. 利润预期 là kỳ vọng lợi nhuận. 风险管控 là kiểm soát rủi ro. Cấu trúc ……才…… nhấn mạnh điều kiện: phải như vậy thì mới…."]),
    ("热钱烧出来的免费时代或许可以怀念却不值得留恋，免费午餐可以休矣！当年埋下的雷会逐一引爆——没有侥幸，只有瑞幸。",
     "Thời đại miễn phí được đốt ra bằng tiền nóng có lẽ đáng để hoài niệm nhưng không đáng để lưu luyến, bữa trưa miễn phí có thể dừng lại được rồi! Những quả mìn chôn năm ấy sẽ lần lượt phát nổ: không có may mắn thoát nạn, chỉ có Luckin.",
     ["或许可以怀念却不值得留恋 là có lẽ đáng hoài niệm nhưng không đáng lưu luyến. 可以休矣 là có thể thôi được rồi, mẫu câu thứ năm: 休 là thôi, 矣 là trợ từ văn ngôn giống 了.",
      "埋下的雷 là quả mìn đã chôn, tức rủi ro tích tụ từ trước; 逐一引爆 là lần lượt phát nổ. 没有侥幸，只有瑞幸 là chơi chữ: 侥幸 là may mắn nhờ ăn may; 瑞幸 là Luckin Coffee, cũng có chữ 幸, năm 2020 bị phanh phui làm giả doanh thu. Ý nói: chẳng ai ăn may thoát được, chỉ có những vụ đổ vỡ như Luckin."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 天下没有永远免费的午餐", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa. Bài được cải biên từ bài 互联网经济正在告别免费时代, Kinh tế internet đang từ biệt thời đại miễn phí, của tác giả 江东瑜, đăng trên tuần báo 南方周末, Nam Phương Chu Mạt, ngày hai mươi sáu tháng năm năm hai nghìn không trăm hai mươi.",
         F(0, "Bài gốc có bảy đoạn khá dài; thầy chia thành mười sáu đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Đây là một bài bình luận kinh tế, câu văn dài và nhiều thuật ngữ. Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "").replace("《", "").replace("》", "")
    zsize = 54 if len(zh) <= 90 else 50 if len(zh) <= 115 else 46
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Bố cục & ghi chú", section="Bài khóa 课文", title="Bố cục bài khóa: miễn phí qua ba giai đoạn", size=33,
    items=["## 1. Sự kiện “五毛钱” của 丰巢 → 免费时代的终结 (đoạn 1)",
           "## 2. Vì sao internet từng miễn phí? (đoạn 2–9)",
           "(1) 理想主义时期: 小众、自娱自乐、公开共享、排斥商业化",
           "(2) 互联网营销: 免费 chỉ là hình thức · 广告收入成为标配 · 第三方买单",
           "(3) 资本请客: 以金钱换时间，以时间换规模 · 烧钱获客、规模为王 · 赔本赚吆喝",
           "## 3. Tiền đâu mà đốt? 超发货币 → 热钱 → 泡沫，长此以往，难以为继 (đoạn 10–12)",
           "## 4. Kết luận: thu phí là tất yếu, là dấu hiệu trưởng thành · 免费午餐可以休矣 (đoạn 13–16)"],
    say=["Trước khi sang phần mẫu câu, chúng ta cùng nhìn lại bố cục bài khóa. Bài có bốn phần, lập luận rất chặt chẽ.",
         F(0, "Phần một, mở bài: sự kiện năm hào của Phong Sào, được tác giả coi là dấu mốc kết thúc thời đại miễn phí."),
         F(1, "Phần hai, trả lời câu hỏi: vì sao internet từng miễn phí? Tác giả chỉ ra ba giai đoạn với ba động lực khác nhau."),
         F(2, "Giai đoạn một, thời kỳ lý tưởng chủ nghĩa: người dùng ít, trẻ tuổi, tự mua vui cho nhau, đề cao chia sẻ công khai, bài xích thương mại hóa. Miễn phí vì lý tưởng."),
         F(3, "Giai đoạn hai, tiếp thị internet: miễn phí chỉ còn là hình thức, quảng cáo trở thành nguồn thu tiêu chuẩn, bên thứ ba trả tiền thay người dùng. Miễn phí vì tiếp thị."),
         F(4, "Giai đoạn ba, tư bản mời khách: lấy tiền đổi thời gian, lấy thời gian đổi quy mô, đốt tiền giành khách, chịu lỗ để lấy tiếng. Miễn phí vì tư bản đốt tiền."),
         F(5, "Phần ba trả lời câu hỏi: tiền đâu mà đốt? Đó là tiền do các nước phát hành vượt mức, biến thành tiền nóng chảy vào internet, tạo ra bong bóng; cứ thế mãi thì không thể duy trì."),
         F(6, "Phần bốn, kết luận: thu phí là tất yếu, là dấu hiệu kinh tế internet trưởng thành; bữa trưa miễn phí nên dừng lại được rồi.")])

add("bullets", section="Bài khóa 课文", title="Ghi chú 注释: hiểu thêm về bối cảnh", size=32,
    items=["丰巢 (Hive Box, Thâm Quyến, 2015): tủ nhận hàng tự động 24/24 · 30/4/2020: người không phải hội viên để hàng quá 12 giờ → 0,5 tệ/giờ, tối đa 3 tệ, ngày lễ không tính → tranh cãi dữ dội",
           "《卖布头》: tấu nói về người bán hàng rong thời xưa tự khen hàng mình, rao bán ầm ĩ, càng nói càng hạ giá, cuối cùng bán rẻ thành… cho không",
           "瑞幸 Luckin Coffee (Hạ Môn): chuỗi cà phê lớn nhất Trung Quốc · 2019 niêm yết Nasdaq · 2/4/2020 tự thú làm giả 2,2 tỷ tệ doanh thu → cổ phiếu lao dốc hơn 80%, bị hủy niêm yết"],
    say=["Sách có ba ghi chú giúp hiểu thêm bối cảnh bài khóa.",
         F(0, "Một: sự kiện năm hào của Phong Sào. 丰巢, Hive Box, thành lập năm hai nghìn không trăm mười lăm ở Thâm Quyến, chuyên vận hành tủ nhận hàng tự động hai mươi bốn giờ cho các hãng chuyển phát. Từ ngày ba mươi tháng tư năm hai nghìn không trăm hai mươi, Phong Sào thông báo: người dùng không phải hội viên để hàng trong tủ quá mười hai giờ sẽ bị thu năm hào mỗi giờ, tối đa ba tệ, ngày lễ không tính phí. Số tiền rất nhỏ, nhưng trong mắt người dùng, bốn chữ thu phí quá giờ như được tô đậm, viết to, nên gây tranh cãi dữ dội."),
         F(1, "Hai: 卖布头, Bán vải vụn, một tiết mục tấu nói. Tiết mục kể về những người bán hàng rong thời xưa, tự khen hàng của mình, rao bán ầm ĩ để kéo khách; họ càng nói càng hạ giá, cuối cùng bán rẻ biến thành cho không. Đây chính là chịu lỗ để lấy tiếng."),
         F(2, "Ba: 瑞幸, Luckin Coffee, trụ sở ở Hạ Môn, từng là chuỗi cà phê lớn nhất Trung Quốc. Tháng năm năm hai nghìn không trăm mười chín, Luckin niêm yết trên sàn Nasdaq. Ngày hai tháng tư năm hai nghìn không trăm hai mươi, Luckin bất ngờ tự công bố đã làm giả khoảng hai tỷ hai trăm triệu tệ doanh thu; cổ phiếu lao dốc hơn tám mươi phần trăm, rồi bị buộc hủy niêm yết. Vì thế câu cuối bài mới viết: 没有侥幸，只有瑞幸.")])

# ======================= MẪU CÂU =======================
add("bullets", chapter="Mẫu câu: 随着…的普及 · 的优势在于 · 以…换…", section="Mẫu câu 重点句型", title="1. 随着……的普及 · 2. ……的优势在于……", size=32,
    items=["## 随着……的普及: cùng với sự phổ cập của… (vế sau nêu sự thay đổi)",
           "随着互联网应用的普及，大众化的互联网生态趋近现实社会。",
           "随着无人加油站的普及，越来越多的车主选择自助加油的方式。",
           "随着智能手机等电子产品的普及，“低头族”的数量越来越庞大。",
           "## ……的优势在于……: ưu thế của… nằm ở chỗ…",
           "广告收入的优势在于，无需深度涉入互联网企业的业务，可以单纯从流量中产生收益……",
           "工厂建在港口城市的优势在于：运输成本较低，效率较高。"],
    say=["Bây giờ chúng ta sang phần mẫu câu trọng điểm. Bài có sáu mẫu, thầy chia thành ba slide.",
         F(0, "Mẫu thứ nhất: 随着……的普及, cùng với sự phổ cập của một thứ gì đó. Vế sau nêu sự thay đổi do việc phổ cập ấy mang lại, thường có 越来越 hoặc động từ chỉ biến đổi."),
         F(1, "Ví dụ một, lấy từ bài khóa: 随着互联网应用的普及，大众化的互联网生态趋近现实社会。"),
         F(2, "Ví dụ hai: 随着无人加油站的普及，越来越多的车主选择自助加油的方式。 Cùng với sự phổ biến của trạm xăng không người, ngày càng nhiều chủ xe chọn cách tự đổ xăng."),
         F(3, "Ví dụ ba: 随着智能手机等电子产品的普及，低头族的数量越来越庞大。 Cùng với sự phổ cập của điện thoại thông minh, số người cắm mặt vào điện thoại ngày càng đông. 低头族 là tộc cúi đầu."),
         F(4, "Mẫu thứ hai: 的优势在于, ưu thế của một thứ nằm ở chỗ. 在于 là nằm ở, chính là ở. Sau 在于 có thể dùng dấu phẩy hoặc dấu hai chấm rồi liệt kê ưu thế."),
         F(5, "Ví dụ một, lấy từ bài khóa: 广告收入的优势在于，无需深度涉入互联网企业的业务，可以单纯从流量中产生收益。 Ở đây sách viết 涉入, cũng nghĩa là dấn vào, như 涉足."),
         F(6, "Ví dụ hai: 工厂建在港口城市的优势在于：运输成本较低，效率较高。 Ưu thế của việc đặt nhà máy ở thành phố cảng là chi phí vận chuyển thấp, hiệu quả cao. Sách còn có ví dụ so sánh hai cách tuyển dụng: 外部招聘的优势在于, ưu thế của tuyển dụng bên ngoài là nhân viên mới mang đến quan điểm mới; 内部选聘的优势在于, ưu thế của tuyển chọn nội bộ là nhân viên cũ nắm rõ tình hình, chi phí thấp.")])

add("bullets", section="Mẫu câu 重点句型", title="3. 以……换…… · 4. 换一个角度看", size=33,
    items=["## 以A换B: lấy A đổi lấy B (bỏ ra A để được B)",
           "以金钱换时间，以时间换规模，烧钱获客、规模为王。",
           "以旧换新是资源回收再利用的重要方法之一。",
           "以土地换和平能够避免战争和冲突吗？",
           "## 换一个角度看: nhìn từ góc độ khác (thường dẫn ra nhận định mới, bất ngờ)",
           "换一个角度看，互联网的烧钱高潮掩盖了货币超发的副作用……",
           "换一个角度看，也许会发现一个更精彩的世界。 · 也许换一个角度看，问题就会迎刃而解。"],
    say=[F(0, "Mẫu thứ ba: 以A换B, lấy A đổi lấy B, tức là bỏ ra A để có được B. 以 là lấy, dùng; 换 là đổi."),
         F(1, "Ví dụ một, lấy từ bài khóa: 以金钱换时间，以时间换规模，烧钱获客、规模为王。 Lấy tiền đổi thời gian, lấy thời gian đổi quy mô. Hai vế nối đuôi nhau rất nhịp nhàng."),
         F(2, "Ví dụ hai: 以旧换新是资源回收再利用的重要方法之一。 Thu cũ đổi mới là một trong những cách quan trọng để thu hồi, tái sử dụng tài nguyên. 以旧换新 đã thành cụm cố định, ta đã gặp ở bài trước."),
         F(3, "Ví dụ ba: 以土地换和平能够避免战争和冲突吗？ Lấy đất đổi hòa bình có thể tránh được chiến tranh và xung đột không?"),
         F(4, "Mẫu thứ tư: 换一个角度看, nhìn từ một góc độ khác. Cụm này thường đứng đầu câu, dẫn ra một cách nhìn mới, đôi khi bất ngờ, so với điều vừa nói."),
         F(5, "Ví dụ một, lấy từ bài khóa: 换一个角度看，互联网的烧钱高潮掩盖了货币超发的副作用，多少有点瞎猫撞到死耗子的喜剧氛围。"),
         F(6, "Ví dụ hai và ba: 换一个角度看，也许会发现一个更精彩的世界。 Nhìn từ góc độ khác, có lẽ sẽ phát hiện một thế giới đặc sắc hơn. 也许换一个角度看，问题就会迎刃而解。 Có lẽ đổi một góc nhìn, vấn đề sẽ được giải quyết dễ dàng. 迎刃而解 là thành ngữ: chẻ tre gặp lưỡi dao là tách, tức là giải quyết dễ dàng.")])

add("bullets", chapter="Mẫu câu: 可以休矣 · 难怪", section="Mẫu câu 重点句型", title="5. ……可以休矣 · 6. 难怪……", size=33,
    items=["## ……可以休矣: có thể thôi được rồi, nên chấm dứt (văn viết, giọng phê phán)",
           "热钱烧出来的免费时代或许可以怀念却不值得留恋，免费午餐可以休矣！",
           "你想靠搞证券投机买卖发财的美梦可以休矣。 · 这么无聊的幼稚儿戏，可以休矣。",
           "## 难怪: thảo nào, hèn chi (hiểu ra nguyên nhân nên không còn lạ)",
           "这就难怪在金融资本市场互联网成为仅次于房地产的第二大受益者……",
           "难怪爸爸这么高兴，原来他获得了发明专利。",
           "他老对别人冷言冷语的，难怪人缘不好。"],
    say=[F(0, "Mẫu thứ năm: 可以休矣. 休 là thôi, dừng; 矣 là trợ từ văn ngôn, giống 了. Cả cụm nghĩa là có thể thôi được rồi, nên chấm dứt đi. Đây là cách nói văn viết, mang giọng phê phán, chê một việc, một ý nghĩ không nên tiếp tục."),
         F(1, "Ví dụ một, lấy từ bài khóa: 热钱烧出来的免费时代或许可以怀念却不值得留恋，免费午餐可以休矣！"),
         F(2, "Ví dụ hai và ba: 你想靠搞证券投机买卖发财的美梦可以休矣。 Giấc mộng làm giàu nhờ đầu cơ chứng khoán của anh nên dừng lại đi. 这么无聊的幼稚儿戏，可以休矣。 Trò trẻ con vô vị như thế này, thôi đi được rồi."),
         F(3, "Mẫu thứ sáu: 难怪, thảo nào, hèn chi, giống 怪不得. Biểu thị người nói đã hiểu ra nguyên nhân nên không còn thấy lạ. Phần nguyên nhân có thể đứng trước hoặc sau, và thường có 原来 đi kèm."),
         F(4, "Ví dụ một, lấy từ bài khóa: 这就难怪在金融资本市场互联网成为仅次于房地产的第二大受益者。 Vì có nhiều tiền nóng, nên thảo nào internet hưởng lợi lớn thứ hai."),
         F(5, "Ví dụ hai: 难怪爸爸这么高兴，原来他获得了发明专利。 Thảo nào bố vui thế, thì ra bố được cấp bằng sáng chế. Ở đây kết quả đứng trước, nguyên nhân với 原来 đứng sau."),
         F(6, "Ví dụ ba: 他老对别人冷言冷语的，难怪人缘不好。 Anh ta cứ nói năng lạnh nhạt với người khác, hèn chi không được lòng ai. Ở đây nguyên nhân đứng trước. 冷言冷语 là lời lẽ lạnh lùng, mỉa mai.")])

add("bullets", section="Mẫu câu 重点句型", title="Luyện tập: hoàn thành câu bằng mẫu câu vừa học", reveal=True, size=34,
    items=["(1) ___智能手机___，人们越来越离不开网络。",
           "Đáp án: 随着智能手机的普及，人们越来越离不开网络。",
           "(2) 网上购物的优势___：方便、省时间。",
           "Đáp án: 网上购物的优势在于：方便、省时间。",
           "(3) 原来他考上了研究生，___他今天这么高兴。",
           "Đáp án: 原来他考上了研究生，难怪他今天这么高兴。",
           "(4) 这种靠烧钱抢市场的做法，可以___！",
           "Đáp án: 这种靠烧钱抢市场的做法，可以休矣！"],
    say=["Bây giờ chúng ta luyện tập nhanh: hoàn thành câu bằng mẫu câu vừa học. Các bạn tạm dừng sau mỗi câu nhé.",
         F(0, "Câu một: 什么智能手机什么，人们越来越离不开网络。 Cùng với sự phổ cập của điện thoại thông minh, con người ngày càng không thể rời xa mạng internet."),
         F(1, "Đáp án: 随着智能手机的普及，人们越来越离不开网络。 Mẫu 随着……的普及."),
         F(2, "Câu hai: 网上购物的优势什么：方便、省时间。 Ưu thế của mua sắm trực tuyến là tiện lợi, tiết kiệm thời gian."),
         F(3, "Đáp án: 网上购物的优势在于：方便、省时间。"),
         F(4, "Câu ba: 原来他考上了研究生，什么他今天这么高兴。 Thì ra anh ấy đỗ cao học, thảo nào hôm nay vui thế."),
         F(5, "Đáp án: 难怪. 原来他考上了研究生，难怪他今天这么高兴。 Nguyên nhân với 原来 đứng trước, 难怪 đứng sau."),
         F(6, "Câu bốn: 这种靠烧钱抢市场的做法，可以什么！ Cách làm đốt tiền giành thị trường như thế này nên chấm dứt được rồi!"),
         F(7, "Đáp án: 可以休矣！ Giọng văn phê phán, giống câu kết của bài khóa.")])

# ======================= KẾT HỢP TỪ & THÀNH NGỮ =======================
add("bullets", chapter="Kết hợp từ (8 từ)", section="Kết hợp từ 词语搭配", title="Kết hợp từ (1): 颇 · 遵循 · 浓厚 · 放宽", size=31,
    items=["## 颇: ～佳 · ～感兴趣 · ～具影响 · ～不以为然 · ～为费解 · ～为复杂 · ～为醒目 · ～为流行",
           "其中的原因颇为复杂。 · 南京大学在国内高校中颇具影响力。",
           "## 遵循: ～规律 · ～逻辑 · ～法度 · ～内心",
           "任何投资最终都要遵循基本的商业逻辑。 · 人类必须遵循自然规律，这样才能与自然和谐相处。",
           "## 浓厚: 兴趣～ · 底蕴～ · ～的文化 · ～的色彩",
           "也许是受父母熏陶吧，表哥从小就对绘画产生了浓厚的兴趣。",
           "## 放宽: ～标准 · ～要求 · ～尺度 · ～管制 · ～条件",
           "招聘人才要严格掌握标准，不能任意放宽尺度。"],
    say=["Tiếp theo là phần kết hợp từ, 词语搭配. Bài này có tám từ, thầy chia thành hai slide.",
         F(0, "Từ thứ nhất: 颇, khá, rất, văn viết. Hay gặp: 颇佳, khá tốt; 颇感兴趣, khá hứng thú; 颇具影响, khá có ảnh hưởng; 颇不以为然, rất không đồng tình; và 颇为 cộng tính từ hai âm tiết: 颇为费解，颇为复杂，颇为醒目，颇为流行."),
         F(1, "Ví dụ: 其中的原因颇为复杂。 Nguyên nhân trong đó khá phức tạp. 南京大学在国内高校中颇具影响力。 Đại học Nam Kinh khá có tầm ảnh hưởng trong các trường đại học trong nước. Sách giáo khoa này cũng do Đại học Nam Kinh biên soạn đấy."),
         F(2, "Từ thứ hai: 遵循, tuân theo. Đi với 规律, quy luật; 逻辑, logic; 法度, phép tắc; 内心, tiếng lòng."),
         F(3, "Ví dụ: 任何投资最终都要遵循基本的商业逻辑。 Và: 人类必须遵循自然规律，这样才能与自然和谐相处。 Con người phải tuân theo quy luật tự nhiên, như vậy mới chung sống hài hòa với thiên nhiên được. Sách còn có câu: 真正的自由不是为所欲为, tự do thật sự không phải là muốn làm gì thì làm."),
         F(4, "Từ thứ ba: 浓厚, đậm, sâu đậm. Đi với 兴趣浓厚, hứng thú sâu sắc; 底蕴浓厚, nền tảng văn hóa sâu dày; 浓厚的文化, 浓厚的色彩, màu sắc đậm nét. Trong bài: 自娱自乐的氛围浓厚."),
         F(5, "Ví dụ: 也许是受父母熏陶吧，表哥从小就对绘画产生了浓厚的兴趣。 Có lẽ do được bố mẹ hun đúc, anh họ tôi từ nhỏ đã rất say mê hội họa. 熏陶 là hun đúc, ảnh hưởng dần dần."),
         F(6, "Từ thứ tư: 放宽, nới lỏng. Đi với 标准，要求，尺度，管制，条件. Trong bài: 放宽免费时限."),
         F(7, "Ví dụ: 招聘人才要严格掌握标准，不能任意放宽尺度。 Tuyển dụng nhân tài phải nắm chặt tiêu chuẩn, không được tùy tiện nới lỏng. Sách còn có: 外贸体制改革的方向是放宽管制, phương hướng cải cách ngoại thương là nới lỏng quản lý.")])

add("bullets", section="Kết hợp từ 词语搭配", title="Kết hợp từ (2): 排斥 · 反常 · 泡沫 · 留恋", size=31,
    items=["## 排斥: 受到～ · 出现～ · ～外援 · ～他人",
           "他的不诚实使他受到了全班同学的排斥。",
           "## 反常: 表现～ · 举动～ · 情绪～ · 态度～ · ～的反应",
           "这几天他的举动很反常。 · 今年气候反常，南方大旱，北方大涝。",
           "## 泡沫: 形成～ · ～经济 · ～化 · 房地产～",
           "股市的萧条令人心寒，泡沫经济是否会破裂也让人担忧。",
           "## 留恋: ～往事 · ～过去 · 值得～ · 毫不～",
           "我们不应总留恋过去，而应该多多展望未来。"],
    say=[F(0, "Từ thứ năm: 排斥, bài xích. Đi với 受到排斥，出现排斥，排斥外援，排斥他人. Trong bài: 商业化受到普遍的排斥."),
         F(1, "Ví dụ: 他的不诚实使他受到了全班同学的排斥。 Sự không trung thực khiến cậu ta bị cả lớp xa lánh. Sách còn có câu: 他性格内向，习惯独来独往，所以排斥所有聚会活动, cậu ấy hướng nội, quen đi về một mình, nên né tránh mọi cuộc tụ tập."),
         F(2, "Từ thứ sáu: 反常, bất thường. Đi với 表现反常，举动反常，情绪反常，态度反常，反常的反应."),
         F(3, "Ví dụ: 这几天他的举动很反常。 Mấy hôm nay cử chỉ của anh ấy rất lạ. Và: 今年气候反常，南方大旱，北方大涝。 Năm nay khí hậu thất thường, miền nam hạn nặng, miền bắc úng lụt."),
         F(4, "Từ thứ bảy: 泡沫, bong bóng. Đi với 形成泡沫，泡沫经济，泡沫化，房地产泡沫. Trong bài: 积累了不少的泡沫."),
         F(5, "Ví dụ: 股市的萧条令人心寒，泡沫经济是否会破裂也让人担忧。 Thị trường chứng khoán ảm đạm khiến người ta nản lòng, bong bóng kinh tế liệu có vỡ không cũng khiến người ta lo lắng. Sách còn có: 房地产市场泡沫破灭的后果不堪设想, hậu quả của việc bong bóng bất động sản vỡ thật khó lường."),
         F(6, "Từ thứ tám: 留恋, lưu luyến. Đi với 留恋往事，留恋过去，值得留恋，毫不留恋. Trong bài: 不值得留恋."),
         F(7, "Ví dụ: 我们不应总留恋过去，而应该多多展望未来。 Chúng ta không nên mãi lưu luyến quá khứ, mà nên hướng về tương lai nhiều hơn. Và: 毕业这么多年了，大家仍然十分留恋自己的母校。 Tốt nghiệp bao năm rồi, mọi người vẫn rất lưu luyến mái trường xưa.")])

add("bullets", chapter="Thành ngữ (9)", section="Thành ngữ 成语和惯用语", title="Thành ngữ (1): 浓墨重彩 · 自娱自乐 · 愤世嫉俗", size=32,
    items=["## 浓墨重彩 nóngmò-zhòngcǎi: mực đậm màu nặng – miêu tả, ghi lại thật đậm nét",
           "……若干年以后的经济史中会浓墨重彩地记录这一“五毛钱”事件……",
           "明清时期，晋商……在中国商业史上写下了浓墨重彩的一笔。",
           "## 自娱自乐 zìyú-zìlè: tự mua vui cho mình",
           "那些上了年纪的大叔、大妈们，练着太极，下着象棋，自娱自乐，悠然自得。",
           "## 愤世嫉俗 fènshì-jísú: căm ghét thói đời, bất bình với xã hội",
           "年轻人不要受了一点委屈就愤世嫉俗，甚至做出一些过激的举动。"],
    say=["Bây giờ là phần thành ngữ và quán ngữ. Bài có chín cụm, thầy chia thành ba slide.",
         F(0, "Thành ngữ thứ nhất: 浓墨重彩. Mực đậm, màu nặng: vốn chỉ cách vẽ dùng mực và màu đậm, nghĩa bóng là miêu tả, ghi chép thật đậm nét, dồn sức vào. Chữ 重 đọc là zhòng."),
         F(1, "Ví dụ trong bài: 相信若干年以后的经济史中会浓墨重彩地记录这一五毛钱事件。"),
         F(2, "Ví dụ khác: 明清时期，晋商创造了令世人瞩目的商业奇迹，在中国商业史上写下了浓墨重彩的一笔。 Thời Minh Thanh, thương nhân Sơn Tây đã làm nên kỳ tích kinh doanh khiến thế giới chú ý, viết nên một nét son đậm trong lịch sử thương nghiệp Trung Quốc. Cụm 写下浓墨重彩的一笔 rất hay gặp."),
         F(3, "Thành ngữ thứ hai: 自娱自乐, tự mình tìm cách làm cho mình vui. 娱 là vui, làm vui; chữ cuối đọc là lè."),
         F(4, "Ví dụ: 慢慢的，广场上的人越来越多，那些上了年纪的大叔、大妈们，练着太极，下着象棋，自娱自乐，悠然自得。 Dần dần người trên quảng trường đông lên, các ông các bà có tuổi, người tập thái cực quyền, người đánh cờ tướng, tự mua vui, thảnh thơi tự tại."),
         F(5, "Thành ngữ thứ ba: 愤世嫉俗. 愤 là căm phẫn, 世 là thời thế, 嫉 là ghét, 俗 là thói tục: người có chính nghĩa căm ghét hiện thực đen tối và những thói tục bất hợp lý. Ngày nay hay dùng với ý hơi chê: bất mãn với đời. 愤青, thanh niên phẫn nộ, cũng từ đây mà ra."),
         F(6, "Ví dụ: 年轻人不要受了一点委屈就愤世嫉俗，甚至做出一些过激的举动。 Người trẻ đừng vì chịu chút oan ức mà oán đời, thậm chí có những hành động quá khích. Và: 他总觉得自己怀才不遇，所以会如此愤世嫉俗。 Anh ta luôn thấy mình có tài mà không gặp thời, nên mới oán đời như vậy.")])

add("bullets", section="Thành ngữ 成语和惯用语", title="Thành ngữ (2): 欣欣向荣 · 饕餮盛宴 · 瞎猫撞到死耗子", size=32,
    items=["## 欣欣向荣 xīnxīn-xiàngróng: cây cỏ tươi tốt – sự nghiệp phát triển rực rỡ",
           "……人类经济活动中首次出现了大规模亏损却又欣欣向荣的企业群体……",
           "经历了十几年的风风雨雨，我们的企业终于迎来了欣欣向荣的高速发展阶段。",
           "## 饕餮盛宴 tāotiè shèngyàn: bữa tiệc linh đình; (nghĩa bóng) nội dung vô cùng phong phú",
           "春晚是全球华人每年除夕夜必不可少的饕餮盛宴。",
           "## 瞎猫撞到死耗子: mèo mù vớ cá rán – không có tài mà gặp may",
           "这次考试很难，我考高分，完全是瞎猫撞到死耗子，运气好而已。"],
    say=[F(0, "Thành ngữ thứ tư: 欣欣向荣. 欣欣 là cây cỏ tốt tươi, 荣 là sum suê: vốn tả cây cỏ phát triển mạnh, nghĩa bóng là sự nghiệp phát triển rực rỡ, hưng thịnh."),
         F(1, "Ví dụ trong bài: 人类经济活动中首次出现了大规模亏损却又欣欣向荣的企业群体。 Ở đây tác giả dùng với ý mỉa mai: lỗ mà vẫn rực rỡ."),
         F(2, "Ví dụ khác: 经历了十几年的风风雨雨，我们的企业终于迎来了欣欣向荣的高速发展阶段。 Trải qua mười mấy năm sóng gió, doanh nghiệp chúng tôi cuối cùng đã bước vào giai đoạn phát triển nhanh và rực rỡ."),
         F(3, "Thành ngữ thứ năm: 饕餮盛宴. 饕餮 đọc là tāotiè, con quái thú tham ăn trong truyền thuyết, hình của nó hay được khắc trên đồ đồng cổ. 饕餮盛宴 là bữa tiệc thịnh soạn, nghĩa bóng chỉ nội dung vô cùng phong phú, hấp dẫn."),
         F(4, "Ví dụ: 春晚是全球华人每年除夕夜必不可少的饕餮盛宴。 Xuân vãn là bữa tiệc tinh thần không thể thiếu của người Hoa toàn cầu mỗi đêm giao thừa. Trong bài: 赶上了各国政府超发货币的饕餮盛宴."),
         F(5, "Quán ngữ thứ sáu: 瞎猫撞到死耗子. Mèo mù đụng phải chuột chết: bản thân không có tài hay không nắm chắc, lại tình cờ thành công. Tiếng Việt có câu mèo mù vớ cá rán, giống hệt. 耗子 là cách gọi con chuột trong khẩu ngữ phương Bắc."),
         F(6, "Ví dụ: 这次考试很难，我考高分，完全是瞎猫撞到死耗子，运气好而已。 Kỳ thi lần này rất khó, tôi được điểm cao hoàn toàn là mèo mù vớ cá rán, chỉ là may thôi. Người nói thường dùng câu này để khiêm tốn.")])

add("bullets", section="Thành ngữ 成语和惯用语", title="Thành ngữ (3): 长此以往 · 难以为继 · 赔本赚吆喝", size=32,
    items=["## 长此以往 chángcǐ-yǐwǎng: cứ tiếp tục như thế mãi (thường dẫn tới hậu quả xấu)",
           "他闷闷不乐，脾气暴躁，长此以往，朋友们就都疏远他了。",
           "这样近距离地看书，长此以往，非成近视眼不可。",
           "## 难以为继 nányǐwéijì: khó lòng tiếp tục, khó duy trì",
           "……缺乏市场竞争力，导致负债累累、难以为继。",
           "## 赔本赚吆喝 péiběn zhuàn yāohe: bán lỗ để lấy tiếng, chịu lỗ để kéo khách",
           "瑞幸咖啡刚创立时，以低价售卖咖啡，赔本赚吆喝，以此扩大市场。"],
    say=[F(0, "Thành ngữ thứ bảy: 长此以往. 长此 là lâu dài như thế này, 以往 là cứ thế mà đi tiếp. Cứ tiếp tục như thế mãi; phía sau thường là hậu quả xấu. Chữ đầu đọc là cháng."),
         F(1, "Ví dụ: 他闷闷不乐，脾气暴躁，长此以往，朋友们就都疏远他了。 Anh ấy buồn bực không vui, tính tình nóng nảy, cứ thế mãi, bạn bè đều xa lánh anh ấy."),
         F(2, "Ví dụ khác: 这样近距离地看书，长此以往，非成近视眼不可。 Đọc sách gần như thế, cứ kéo dài mãi thì thế nào cũng bị cận thị. 非……不可 là không… không được, tức là nhất định."),
         F(3, "Thành ngữ thứ tám: 难以为继. 为继 là tiếp tục; chữ 为 đọc là wéi. Khó lòng tiếp tục được. Trong bài, hai thành ngữ đi liền nhau: 长此以往，难以为继."),
         F(4, "Ví dụ: 改革开放以后，某些企业未能有效地转换经营机制，缺乏市场竞争力，导致负债累累、难以为继。 Sau cải cách mở cửa, một số doanh nghiệp không chuyển đổi cơ chế kinh doanh hiệu quả, thiếu sức cạnh tranh, dẫn đến nợ nần chồng chất, khó duy trì. 负债累累 là nợ nần chồng chất, hai chữ cuối đọc là lěilěi."),
         F(5, "Quán ngữ thứ chín: 赔本赚吆喝. 赔本 là lỗ vốn; 吆喝 là tiếng rao hàng. Bán lỗ để kiếm tiếng rao, tức là chịu lỗ để gây tiếng tăm, kéo khách."),
         F(6, "Ví dụ: 瑞幸咖啡刚创立时，以低价售卖咖啡，赔本赚吆喝，以此扩大市场。 Luckin Coffee lúc mới thành lập bán cà phê giá thấp, chịu lỗ để lấy tiếng, nhờ đó mở rộng thị trường. Sách còn có câu: nhiều nhà hàng coi việc nhận đặt cơm tất niên là 赔本赚吆喝, chẳng thà đóng cửa nghỉ Tết với gia đình.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 课后练习", title="Bài tập 1: Chọn thành ngữ điền vào chỗ trống (1)", reveal=True, size=32,
    items=["## 毫无悬念 · 欣欣向荣 · 自娱自乐 · 难以为继 · 饕餮盛宴 · 浓墨重彩 · 瞎猫撞到死耗子 · 愤世嫉俗",
           "(1) 愤青指的是___的青年。",
           "Đáp án: 愤世嫉俗",
           "(2) 即使生活___，我们也不能轻言放弃。",
           "Đáp án: 难以为继",
           "(3) 牧羊人花了35年的时间在荒漠上种树……这片荒漠变成了一片___的森林。",
           "Đáp án: 欣欣向荣",
           "(4) 作为一号种子选手，他___地进入了最后的决赛。",
           "Đáp án: 毫无悬念"],
    say=["Phần luyện tập 趁热打铁. Bài tập một: chọn thành ngữ điền vào chỗ trống. Có tám cụm: 毫无悬念，欣欣向荣，自娱自乐，难以为继，饕餮盛宴，浓墨重彩，瞎猫撞到死耗子，愤世嫉俗.",
         F(1, "Câu một: 愤青指的是什么的青年。 Thanh niên phẫn nộ là chỉ những thanh niên thế nào? Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 愤世嫉俗. 愤青 chính là nói tắt của 愤世嫉俗的青年."),
         F(3, "Câu hai: 即使生活什么，我们也不能轻言放弃。 Dù cuộc sống khó lòng tiếp tục, chúng ta cũng không được dễ dàng bỏ cuộc."),
         F(4, "Đáp án: 难以为继. 生活难以为继, cuộc sống khó khăn đến mức khó duy trì."),
         F(5, "Câu ba: 牧羊人花了三十五年的时间在荒漠上种树，付出终有回报，这片荒漠变成了一片什么的森林。 Người chăn cừu dành ba mươi lăm năm trồng cây trên hoang mạc, công sức cuối cùng được đền đáp, vùng hoang mạc biến thành một khu rừng thế nào?"),
         F(6, "Đáp án: 欣欣向荣. 欣欣向荣的森林, khu rừng xanh tươi tốt, đúng nghĩa gốc của thành ngữ."),
         F(7, "Câu bốn: 作为一号种子选手，他什么地进入了最后的决赛。 Là hạt giống số một, anh ấy vào chung kết một cách thế nào?"),
         F(8, "Đáp án: 毫无悬念. 毫无悬念地进入决赛, vào chung kết không chút bất ngờ, ai cũng đoán trước được.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 1: Chọn thành ngữ điền vào chỗ trống (2)", reveal=True, size=32,
    items=["(5) 他是一个不太合群的人，喜欢___。",
           "Đáp án: 自娱自乐",
           "(6) 对足球迷来说，世界杯完全就是一场___。",
           "Đáp án: 饕餮盛宴",
           "(7) 诸葛亮借东风大败曹操，这在三国故事里面留下了___的一笔。",
           "Đáp án: 浓墨重彩",
           "(8) 不要总是觉得别人的成功只是___，没有付出，哪来的成功？",
           "Đáp án: 瞎猫撞到死耗子"],
    say=[F(0, "Câu năm: 他是一个不太合群的人，喜欢什么。 Anh ấy là người không hòa đồng lắm, thích làm gì?"),
         F(1, "Đáp án: 自娱自乐. 不太合群, không hòa đồng, nên thích tự mua vui một mình."),
         F(2, "Câu sáu: 对足球迷来说，世界杯完全就是一场什么。 Với người hâm mộ bóng đá, World Cup hoàn toàn là một bữa gì?"),
         F(3, "Đáp án: 饕餮盛宴. Lượng từ 一场 và chữ 盛宴 là gợi ý: World Cup là bữa tiệc thịnh soạn của người hâm mộ."),
         F(4, "Câu bảy: 诸葛亮借东风大败曹操，这在三国故事里面留下了什么的一笔。 Gia Cát Lượng mượn gió đông đánh bại Tào Tháo, để lại một nét thế nào trong chuyện Tam Quốc?"),
         F(5, "Đáp án: 浓墨重彩. 留下了浓墨重彩的一笔, để lại một nét son đậm. Cụm 浓墨重彩的一笔 các bạn nên học thuộc."),
         F(6, "Câu tám: 不要总是觉得别人的成功只是什么，没有付出，哪来的成功？ Đừng lúc nào cũng nghĩ thành công của người khác chỉ là gì đó; không bỏ công sức thì lấy đâu ra thành công?"),
         F(7, "Đáp án: 瞎猫撞到死耗子. Đừng nghĩ người ta thành công chỉ nhờ ăn may.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn đáp án đúng (1)", reveal=True, size=33,
    items=["(1) 大明星的签售会现场人山人海，需要大量的保安（  ）现场秩序。 A.维持 B.维护 C.维系 D.维稳",
           "Đáp án: A 维持 – 维持秩序 giữ gìn trật tự (cố định)",
           "(2) 很多事情都是有（  ）的，错过了对的时间，结果就不一样了。 A.时间 B.时段 C.时限 D.时速",
           "Đáp án: C 时限 – thời hạn, quá hạn là lỡ",
           "(3) 面对命运不（  ），面对困难不退缩，这样才能做自己的英雄。 A.忍受 B.退步 C.协商 D.妥协",
           "Đáp án: D 妥协 – không khuất phục số phận"],
    say=["Bài tập hai: chọn đáp án đúng. Bài này luyện phân biệt các từ gần nghĩa.",
         F(0, "Câu một: 大明星的签售会现场人山人海，需要大量的保安什么现场秩序。 Buổi ký tặng của ngôi sao đông nghịt người, cần nhiều bảo vệ để làm gì với trật tự hiện trường? Bốn lựa chọn: 维持，维护，维系，维稳."),
         F(1, "Đáp án: A, 维持. 维持秩序, duy trì trật tự, là kết hợp cố định. 维护 đi với 权益, quyền lợi, hay 形象, hình ảnh; 维系 là gắn kết, như 维系感情; 维稳 là giữ ổn định xã hội."),
         F(2, "Câu hai: 很多事情都是有什么的，错过了对的时间，结果就不一样了。 Nhiều việc đều có gì đó, lỡ mất đúng thời điểm thì kết quả sẽ khác. Bốn lựa chọn: 时间，时段，时限，时速."),
         F(3, "Đáp án: C, 时限, thời hạn. Câu sau nói lỡ mất thời điểm thì kết quả khác, tức là việc gì cũng có hạn của nó. 时段 là khung giờ, 时速 là tốc độ theo giờ."),
         F(4, "Câu ba: 面对命运不什么，面对困难不退缩，这样才能做自己的英雄。 Đối mặt với số phận không làm gì, đối mặt khó khăn không lùi bước, như thế mới làm người hùng của chính mình. Bốn lựa chọn: 忍受，退步，协商，妥协."),
         F(5, "Đáp án: D, 妥协. 不向命运妥协, không thỏa hiệp với số phận, tức là không khuất phục. 忍受 là chịu đựng; 退步 là thụt lùi; 协商 là bàn bạc.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn đáp án đúng (2)", reveal=True, size=33,
    items=["(4) 最近在一部分年轻人中，（  ）一股汉服热。 A.兴起 B.崛起 C.激起 D.引起",
           "Đáp án: A 兴起 – 兴起一股……热 nổi lên một cơn sốt",
           "(5) 继父虽然对我非常好，但他终究无法（  ）父亲在我心中的位置。 A.取代 B.代表 C.替换 D.交换",
           "Đáp án: A 取代 – thay thế, chiếm chỗ (vị trí trong lòng)",
           "(6) 互联网时代（  ）了一批年轻的CEO。 A.造就 B.造成 C.成就 D.制造",
           "Đáp án: A 造就 – tạo nên nhân tài (造成 đi với kết quả xấu)"],
    say=[F(0, "Câu bốn: 最近在一部分年轻人中，什么一股汉服热。 Gần đây trong một bộ phận giới trẻ, nổi lên một cơn sốt Hán phục. Bốn lựa chọn: 兴起，崛起，激起，引起."),
         F(1, "Đáp án: A, 兴起. 兴起一股热, nổi lên một cơn sốt, một phong trào. 崛起 là vươn lên, trỗi dậy, như 大国崛起; 激起 và 引起 cần có tác nhân gây ra, như 引起关注."),
         F(2, "Câu năm: 继父虽然对我非常好，但他终究无法什么父亲在我心中的位置。 Bố dượng tuy rất tốt với tôi, nhưng rốt cuộc không thể làm gì với vị trí của bố trong lòng tôi? Bốn lựa chọn: 取代，代表，替换，交换."),
         F(3, "Đáp án: A, 取代. 取代位置, thay thế vị trí. 替换 là thay đổi vật này bằng vật khác, như 替换零件, không dùng cho vị trí trong lòng; 交换 là trao đổi."),
         F(4, "Câu sáu: 互联网时代什么了一批年轻的CEO。 Thời đại internet đã làm gì với một lớp giám đốc điều hành trẻ? Bốn lựa chọn: 造就，造成，成就，制造."),
         F(5, "Đáp án: A, 造就. 造就人才, tạo nên, đào tạo nên nhân tài. 造成 đi với kết quả xấu, như 造成损失; 成就 làm động từ thì tân ngữ thường là sự nghiệp, như 成就事业; 制造 là chế tạo đồ vật.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ ngữ, mẫu câu cho sẵn trả lời câu hỏi", reveal=True, size=31,
    items=["(1) 互联网对现代社会的影响？（随着……的普及）",
           "Đáp án gợi ý: 随着互联网的普及，人们的生活方式发生了巨大的变化，购物、学习、工作、社交都可以在网上完成。",
           "(2) 广告收入有何优势？（……的优势在于）",
           "Đáp án gợi ý: 广告收入的优势在于，无需深度涉足互联网企业的业务，可以单纯从流量中产生收益。",
           "(3) 文中如何看待金钱与时间的关系？（以……换）",
           "Đáp án gợi ý: 文中认为互联网企业以金钱换时间，以时间换规模，靠烧钱获客来扩大规模。",
           "(4) 互联网投资应该以何种方式进行？（遵循）",
           "Đáp án gợi ý: 互联网投资应该遵循基本的商业逻辑，以合理的利润预期为前提，进行有效的风险管控。"],
    say=["Bài tập ba: dùng từ ngữ và mẫu câu cho sẵn để trả lời câu hỏi. Đây là câu hỏi mở, thầy đưa ra đáp án gợi ý.",
         F(0, "Câu một: 互联网对现代社会的影响？ Internet ảnh hưởng thế nào đến xã hội hiện đại? Dùng 随着的普及."),
         F(1, "Gợi ý: 随着互联网的普及，人们的生活方式发生了巨大的变化，购物、学习、工作、社交都可以在网上完成。 Cùng với sự phổ cập của internet, lối sống của con người thay đổi rất lớn, mua sắm, học tập, làm việc, giao lưu đều có thể làm trên mạng."),
         F(2, "Câu hai: 广告收入有何优势？ Thu nhập quảng cáo có ưu thế gì? 何 là gì, văn viết. Dùng 的优势在于."),
         F(3, "Gợi ý: 广告收入的优势在于，无需深度涉足互联网企业的业务，可以单纯从流量中产生收益。"),
         F(4, "Câu ba: 文中如何看待金钱与时间的关系？ Bài khóa nhìn nhận quan hệ giữa tiền và thời gian thế nào? Dùng 以换."),
         F(5, "Gợi ý: 文中认为互联网企业以金钱换时间，以时间换规模，靠烧钱获客来扩大规模。"),
         F(6, "Câu bốn: 互联网投资应该以何种方式进行？ Đầu tư internet nên tiến hành theo cách nào? Dùng 遵循."),
         F(7, "Gợi ý: 互联网投资应该遵循基本的商业逻辑，以合理的利润预期为前提，进行有效的风险管控。 Phải tuân theo logic kinh doanh, lấy kỳ vọng lợi nhuận hợp lý làm tiền đề, kiểm soát rủi ro hiệu quả.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Chọn từ điền vào đoạn văn", reveal=True, size=31,
    items=["## 趋近 · 乌托邦 · 舒适感 · 愤世嫉俗 · 标配 · 驱动 · 取代 · 无需",
           "“理想主义时期”持续的时间并不长，随着互联网应用的普及，大众化的互联网生态___现实社会。免费模式还在继续，但___力已然不同。所谓“互联网营销”___了原来的___理想，从营销角度维持“免费”的形式。而此时的“免费”已经不是___的反商业化，广告收入成为了互联网企业的___。广告收入的优势在于，___深度涉入互联网企业的业务，可以单纯从流量中产生收益，第三方买单在形式上维护了用户免费的___。",
           "Đáp án: 趋近 · 驱动 · 取代 · 乌托邦 · 愤世嫉俗 · 标配 · 无需 · 舒适感"],
    say=["Bài tập bốn: chọn từ điền vào đoạn văn. Có tám từ: 趋近，乌托邦，舒适感，愤世嫉俗，标配，驱动，取代，无需.",
         F(1, "理想主义时期持续的时间并不长，随着互联网应用的普及，大众化的互联网生态什么现实社会。免费模式还在继续，但什么力已然不同。所谓互联网营销什么了原来的什么理想，从营销角度维持免费的形式。而此时的免费已经不是什么的反商业化，广告收入成为了互联网企业的什么。广告收入的优势在于，什么深度涉入互联网企业的业务，可以单纯从流量中产生收益，第三方买单在形式上维护了用户免费的什么。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 趋近现实社会；驱动力；取代了原来的乌托邦理想；愤世嫉俗的反商业化；互联网企业的标配；无需深度涉入；用户免费的舒适感。"),
         F(2, "Đoạn văn này chính là đoạn ba của bài khóa. Gợi ý ngữ pháp: trước 力 là 驱动, tạo thành 驱动力; sau 原来的 cần một danh từ bổ nghĩa cho 理想, nên chọn 乌托邦; còn trước 的反商业化 là một thành ngữ làm định ngữ, chính là 愤世嫉俗. Hãy đọc to cả đoạn vài lần để nhớ cách dùng từ nhé.")])

# ======================= LIÊN HỆ =======================
add("bullets", chapter="Liên hệ: “miễn phí” ở Việt Nam", section="Thảo luận 讨论", title="Liên hệ Việt Nam: freeship, “đốt tiền” và trả phí", size=33,
    items=["Mã freeship, “siêu sale” 11.11 trên Shopee, Lazada, TikTok Shop ≈ 包邮、双11",
           "Ứng dụng gọi xe, giao đồ ăn: khuyến mãi mạnh để giành thị phần, rồi giảm khuyến mãi, tăng phí ≈ 烧钱获客、规模为王",
           "Trả phí cho nội dung: Netflix, Spotify, YouTube Premium, VieON… ≈ 视频会员、音乐会员",
           "“Không ai cho không ai cái gì” · “Của rẻ là của ôi” ≈ 天下没有免费的午餐",
           "Câu hỏi: 你愿意为哪些网络服务付费？为什么？"],
    say=["Trước khi tổng kết, chúng ta cùng liên hệ với Việt Nam.",
         F(0, "Ở Việt Nam, mã freeship và những đợt siêu sale ngày mười một tháng mười một trên Shopee, Lazada, TikTok Shop chính là 包邮 và 双十一 trong bài."),
         F(1, "Các ứng dụng gọi xe, giao đồ ăn khi mới vào Việt Nam đều khuyến mãi rất mạnh, chuyến xe chỉ vài nghìn đồng, để giành người dùng; sau đó khuyến mãi giảm dần, phí tăng dần. Có hãng đốt tiền nhiều năm rồi vẫn phải rút khỏi thị trường. Đó chính là 烧钱获客，规模为王, và cũng là lời cảnh báo 长此以往，难以为继."),
         F(2, "Ngày càng nhiều người Việt trả phí cho nội dung số, như Netflix, Spotify, YouTube Premium hay VieON, giống 视频会员, 音乐会员 ở Trung Quốc. Thời đại xem phim lậu, nghe nhạc chùa đang dần qua đi."),
         F(3, "Tiếng Việt có những câu rất gần với tên bài: không ai cho không ai cái gì; của rẻ là của ôi."),
         F(4, "Câu hỏi cho các bạn: 你愿意为哪些网络服务付费？为什么？ Bạn sẵn lòng trả phí cho những dịch vụ mạng nào? Vì sao? Câu mẫu: 我愿意为音乐和学习软件付费，因为付费以后没有广告，内容质量也更有保障。 Tôi sẵn lòng trả phí cho ứng dụng nghe nhạc và học tập, vì trả phí rồi thì không có quảng cáo, chất lượng nội dung cũng đảm bảo hơn. Các bạn hãy tạm dừng và tự trả lời bằng tiếng Trung nhé.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 7.2", size=32,
    items=["Từ vựng trọng tâm: 封顶 · 妥协 · 告终 · 若干 · 默认 · 排斥 · 驱动 · 取代 · 标配 · 亏损 · 烧钱 · 热钱 · 造就 · 泡沫 · 遵循 · 悬念 · 注定 · 违背 · 留恋 · 逐一",
           "Mẫu câu: 随着……的普及 · ……的优势在于 · 以……换…… · 换一个角度看 · ……可以休矣 · 难怪",
           "Kết hợp từ: 颇为复杂 · 遵循规律 · 浓厚的兴趣 · 放宽标准 · 受到排斥 · 举动反常 · 泡沫经济 · 毫不留恋",
           "Thành ngữ: 浓墨重彩 · 自娱自乐 · 愤世嫉俗 · 欣欣向荣 · 饕餮盛宴 · 瞎猫撞到死耗子 · 长此以往 · 难以为继 · 赔本赚吆喝",
           "## Bài tập về nhà",
           "Viết đoạn văn khoảng 300 chữ: 互联网进入付费时代，你会买单吗？"],
    say=["Chúng ta cùng tổng kết bài bảy chấm hai.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 封顶，妥协，告终，若干，默认，排斥，驱动，取代，标配，亏损，烧钱，热钱，造就，泡沫，遵循，悬念，注定，违背，留恋，逐一. Nhớ phân biệt 造就 với 造成, 遵循 với 遵守 nhé."),
         F(1, "Về mẫu câu: 随着的普及 là cùng với sự phổ cập của; 的优势在于 là ưu thế nằm ở chỗ; 以A换B là lấy A đổi B; 换一个角度看 là nhìn từ góc độ khác; 可以休矣 là thôi được rồi; và 难怪 là thảo nào."),
         F(2, "Về kết hợp từ: 颇为复杂，遵循规律，浓厚的兴趣，放宽标准，受到排斥，举动反常，泡沫经济，毫不留恋."),
         F(3, "Về thành ngữ: 浓墨重彩，自娱自乐，愤世嫉俗，欣欣向荣，饕餮盛宴，瞎猫撞到死耗子，长此以往，难以为继，赔本赚吆喝. Đặc biệt nhớ cặp 长此以往，难以为继 hay đi liền nhau."),
         F(5, "Bài tập về nhà: hãy viết một đoạn văn khoảng ba trăm chữ với đề 互联网进入付费时代，你会买单吗？ Internet bước vào thời đại trả phí, bạn có xuống tiền không? Đây cũng là một đề trong phần ôn tập đơn vị của sách. Hãy dùng ít nhất ba mẫu câu và hai thành ngữ của bài."),
         {"t": "Cảm ơn các bạn đã theo dõi bài giảng. Bài sau, bài bảy chấm ba, là bài cuối của Đơn vị bảy: 中国扶贫的道路选择, Con đường xóa đói giảm nghèo của Trung Quốc. Chúng ta sẽ tìm hiểu vì sao cải cách ruộng đất và khoán hộ đã giúp hàng trăm triệu nông dân Trung Quốc thoát nghèo, và cùng ôn tập toàn bộ Đơn vị bảy. Hẹn gặp lại các bạn. Chúc các bạn học tốt!",
          "cap": "Cảm ơn các bạn đã theo dõi bài giảng. Bài sau, bài 7.3, là bài cuối của Đơn vị 7: 中国扶贫的道路选择, Con đường xóa đói giảm nghèo của Trung Quốc. Hẹn gặp lại các bạn. Chúc các bạn học tốt!"}])

lesson = {
    "title": "顶石中文 – Bài 7.2: 天下没有永远免费的午餐 (Trên đời không có bữa trưa nào miễn phí mãi)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"兴起": "星起",              # xīngqǐ
                    "新兴": "新星",              # xīnxīng
                    "重彩": "众彩",              # zhòngcǎi
                    "比重": "比众",              # bǐzhòng
                    "自乐": "自勒",              # zìlè
                    "不乐": "不勒",              # bú lè
                    "着实": "酌实",              # zhuóshí
                    "相声": "象声",              # xiàngsheng
                    "不差钱": "不岔钱",          # bú chà qián
                    "为王": "维王",              # wéiwáng
                    "为继": "维继",              # nányǐwéijì
                    "转为": "转维",              # zhuǎnwéi
                    "颇为": "颇维",              # pōwéi
                    "为前提": "维前提",          # yǐ … wéi qiántí
                    "为所欲为": "维所欲维",      # wéi suǒ yù wéi
                    "长此": "常此",              # chángcǐ
                    "年少": "年绍",              # niánshào
                    "新冠": "新官",              # xīnguān
                    "累累": "垒垒",              # lěilěi
                    "曲艺": "取艺",              # qǔyì
                    "种树": "众树",              # zhòngshù
                    "露营": "路营"},             # lùyíng
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds72.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
