#!/usr/bin/env python3
"""Kịch bản bài giảng 顶石中文 – Bài 8.2 «高通：打官司打出的“江山”». Chạy để sinh ds82.json."""
import json
import os

TAG = "顶石中文 · Bài 8.2 · 高通：打官司打出的“江山”"
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
    zh="高通：打官司打出的“江山”", py="Gāotōng: dǎ guānsi dǎ chū de “jiāngshān”",
    vi="Bài 8.2: Qualcomm: “giang sơn” dựng nên từ kiện tụng",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng giáo trình 顶石中文, Đỉnh cao tiếng Trung.",
         {"t": "Hôm nay chúng ta học bài thứ hai của Đơn vị tám, chủ đề Pháp luật: bài tám chấm hai, 高通：打官司打出的江山。 Nghĩa là: Qualcomm, giang sơn dựng nên từ kiện tụng.",
          "cap": "Hôm nay chúng ta học bài thứ hai của Đơn vị 8, chủ đề Pháp luật: bài 8.2, 高通：打官司打出的“江山”。 Nghĩa là: Qualcomm, “giang sơn” dựng nên từ kiện tụng."},
         "Bài trước nói về nhãn hiệu, bài này nói về bằng sáng chế. 高通, tức Qualcomm, là gã khổng lồ chip điện thoại của Mỹ. Hầu như chiếc điện thoại nào trên thế giới cũng phải trả phí bản quyền cho Qualcomm. Công ty này nổi tiếng vì thường xuyên kiện tụng, từ đấu khẩu với Apple, đến bị Trung Quốc phạt hơn sáu tỷ tệ vì độc quyền.",
         "Bài báo dùng rất nhiều thành ngữ, tới hai mươi mốt thành ngữ, nhiều nhất trong cả giáo trình. Đây là cơ hội tuyệt vời để các bạn nâng cấp vốn thành ngữ của mình đấy."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài báo về Qualcomm: độc quyền bằng sáng chế, “điều khoản bá vương”, vụ phạt chống độc quyền ở Trung Quốc",
           "Nắm vững 50 từ mới, kèm âm Hán Việt và ví dụ",
           "6 mẫu câu: 与其……不如…… · 究其原因 · 戏称……为…… · 无形之中 · 顶多 · 加之",
           "9 kết hợp từ (贴切 · 微妙 · 争端 · 垄断 · 削弱 · 附加 · 摆脱 · 覆盖 · 下滑) và 21 thành ngữ",
           "Luyện tập theo sách; liên hệ: chip, bản quyền và luật cạnh tranh ở Việt Nam"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu bài báo về Qualcomm: công ty này dùng bằng sáng chế để độc quyền thị trường ra sao, những điều khoản bất bình đẳng của nó là gì, và vì sao nó bị Trung Quốc phạt."),
         F(1, "Thứ hai, nắm vững năm mươi từ mới, rất nhiều từ về kinh tế, pháp luật, công nghệ. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt và đưa ví dụ."),
         F(2, "Thứ ba, học sáu mẫu câu trọng điểm: 与其不如，究其原因，戏称为，无形之中，顶多, và 加之."),
         F(3, "Thứ tư, học chín kết hợp từ và hai mươi mốt thành ngữ, như 鹬蚌相争，渔翁得利，落井下石，义愤填膺，两害相权取其轻."),
         F(4, "Thứ năm, làm bài luyện tập của sách, và liên hệ với chuyện chip, bản quyền và luật cạnh tranh ở Việt Nam."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 课前思考", title="Câu hỏi trước bài học 课前思考", reveal=True, size=35,
    items=["(1) 你周围的人是否有过为了保护个人权益而打官司的经历？",
           "Đáp án gợi ý: 有。我的一个亲戚买的房子质量有问题，开发商不肯负责，他只好打官司，最后胜诉了。",
           "(2) 你们国家有没有特别著名的侵权案？最后怎么判决的？",
           "Đáp án gợi ý: 越南的“邦美蜀咖啡”曾经在国外被抢注商标，越南方面坚持维权，最后要回了商标。",
           "(3) 你觉得打官司是不是成本很高的事情？",
           "Đáp án gợi ý: 是的。打官司不但要花很多钱请律师，还要花很多时间和精力，所以很多人宁可忍气吞声。"],
    say=["Chúng ta bắt đầu bằng ba câu hỏi trước bài học, 课前思考. Thầy đọc câu hỏi, các bạn tạm dừng để tự trả lời bằng tiếng Trung, rồi nghe câu trả lời gợi ý nhé.",
         F(0, "Câu một: 你周围的人是否有过为了保护个人权益而打官司的经历？ Những người xung quanh bạn có ai từng ra tòa để bảo vệ quyền lợi cá nhân chưa? 打官司 là kiện tụng, ra tòa."),
         F(1, "Gợi ý: 有。我的一个亲戚买的房子质量有问题，开发商不肯负责，他只好打官司，最后胜诉了。 Có. Một người họ hàng của tôi mua nhà bị lỗi chất lượng, chủ đầu tư không chịu trách nhiệm, anh ấy đành phải kiện, cuối cùng đã thắng kiện. 开发商 là chủ đầu tư bất động sản."),
         F(2, "Câu hai: 你们国家有没有特别著名的侵权案？最后怎么判决的？ Nước bạn có vụ xâm phạm quyền nào đặc biệt nổi tiếng không? Cuối cùng phán quyết thế nào?"),
         F(3, "Gợi ý: 越南的邦美蜀咖啡曾经在国外被抢注商标，越南方面坚持维权，最后要回了商标。 Cà phê Buôn Ma Thuột của Việt Nam từng bị đăng ký chặn trước nhãn hiệu ở nước ngoài; phía Việt Nam kiên trì bảo vệ quyền lợi, cuối cùng đã đòi lại được. 维权 là bảo vệ quyền lợi. Đây là câu chuyện chúng ta đã nhắc ở bài trước."),
         F(4, "Câu ba: 你觉得打官司是不是成本很高的事情？ Bạn có thấy kiện tụng là việc tốn kém không?"),
         F(5, "Gợi ý: 是的。打官司不但要花很多钱请律师，还要花很多时间和精力，所以很多人宁可忍气吞声。 Đúng vậy. Kiện tụng không những tốn nhiều tiền thuê luật sư, mà còn tốn nhiều thời gian và công sức, nên nhiều người thà nhịn nhục cho qua. 忍气吞声 là nuốt giận làm lành, cũng có trong bài khóa.")])

add("bullets", section="Khởi động 课前思考", title="Khởi động: bằng sáng chế và chuyện “thu phí bản quyền”", size=34,
    items=["专利 bằng sáng chế · 专利权 quyền sáng chế · 专利许可 cấp phép sử dụng sáng chế · 许可费 phí cấp phép",
           "授权 trao quyền · 反向授权 trao quyền ngược lại (grant-back) · 标准必要专利 sáng chế thiết yếu theo tiêu chuẩn",
           "芯片 chip · 手机厂商 hãng điện thoại · 下游企业 doanh nghiệp hạ nguồn",
           "反垄断 chống độc quyền · 立案调查 lập án điều tra · 罚款 tiền phạt · 整改 chỉnh đốn, khắc phục",
           "Qualcomm vs Apple: 2017 Apple kiện Qualcomm, hai bên kiện nhau ở nhiều nước; 4/2019 hòa giải"],
    say=["Trước khi vào bài, chúng ta làm quen với một số khái niệm về bằng sáng chế. Có hiểu mô hình kinh doanh của Qualcomm thì mới hiểu được bài khóa.",
         F(0, "专利 là bằng sáng chế; 专利权 là quyền đối với sáng chế. Qualcomm sở hữu rất nhiều sáng chế về thông tin không dây. Hãng điện thoại nào muốn dùng công nghệ ấy thì phải xin 专利许可, giấy phép sử dụng sáng chế, và trả 许可费, phí cấp phép."),
         F(1, "授权 là trao quyền. 反向授权 là trao quyền ngược lại: hãng điện thoại xin phép Qualcomm thì cũng phải cho Qualcomm dùng sáng chế của mình. 标准必要专利 là những sáng chế bắt buộc phải dùng nếu muốn sản xuất theo tiêu chuẩn chung, như tiêu chuẩn 4G, 5G."),
         F(2, "芯片 là chip; 手机厂商 là hãng sản xuất điện thoại; 下游企业 là doanh nghiệp hạ nguồn, tức những công ty mua chip và công nghệ của Qualcomm để làm điện thoại."),
         F(3, "反垄断 là chống độc quyền; 立案调查 là lập án điều tra; 罚款 là tiền phạt; 整改 là chỉnh đốn, khắc phục sai phạm."),
         F(4, "Bối cảnh của bài: năm hai nghìn không trăm mười bảy, Apple kiện Qualcomm thu phí bản quyền quá cao, hai bên kiện nhau ở nhiều nước, đấu khẩu ồn ào trên báo chí. Đến tháng tư năm hai nghìn không trăm mười chín, hai công ty mới hòa giải.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("江山", "jiāngshān", "giang sơn", "danh từ", "giang sơn; (bài này) thị trường, cơ nghiệp kinh doanh", "这家公司靠质量打下了一片江山。", "Công ty này dựa vào chất lượng mà gây dựng được cả một cơ nghiệp.",
     "Danh từ, nghĩa gốc là sông núi, ví với đất nước, chính quyền. Trong bài, 江山 chỉ thị trường kinh doanh mà Qualcomm chiếm được. Tên bài 打官司打出的江山 là giang sơn giành được nhờ đánh kiện. Thành ngữ 半壁江山 trong bài cũng có chữ này."),
    ("口水战", "kǒushuǐzhàn", "khẩu thủy chiến", "danh từ", "cuộc khẩu chiến, đấu khẩu", "两位明星在网上打起了口水战。", "Hai ngôi sao đấu khẩu với nhau trên mạng.",
     "Danh từ. 口水 là nước bọt, 口水战 là chiến tranh bằng nước bọt, tức là công kích nhau bằng lời nói, tranh cãi gay gắt. Tiếng Việt gọi là khẩu chiến. Động từ đi kèm là 打: 打口水战."),
    ("刷屏", "shuāpíng", "loát bình", "động từ", "tràn ngập màn hình, phủ sóng mạng xã hội", "这条新闻一夜之间刷屏了朋友圈。", "Tin này chỉ sau một đêm đã phủ kín vòng bạn bè WeChat.",
     "Động từ li hợp, từ lóng mạng: một thông tin xuất hiện lặp đi lặp lại trên mạng, tràn ngập màn hình. 屏 là màn hình. Trong bài: 口水战持续刷屏, cuộc khẩu chiến liên tục phủ sóng mạng."),
    ("互撕", "hùsī", "hỗ tê", "động từ", "công kích, bóc mẽ lẫn nhau", "两家公司在网上互撕，吸引了很多网友围观。", "Hai công ty công kích nhau trên mạng, thu hút rất nhiều cư dân mạng hóng chuyện.",
     "Động từ, từ lóng mạng. 撕 là xé, 互撕 là xé nhau, tức công kích, bóc mẽ khuyết điểm của nhau. Trong bài: 巨头互撕的大戏, màn kịch lớn các ông trùm xâu xé nhau."),
    ("贴切", "tiēqiè", "thiếp thiết", "tính từ", "(dùng từ) xác đáng, sát nghĩa", "这个比喻用得很贴切。", "Phép so sánh này dùng rất đắt.",
     "Tính từ, nói về cách dùng từ: rất sát, rất đúng. Chữ 切 ở đây đọc thanh bốn, nghĩa là khớp, sát. Tiếng Việt hay nói dùng từ đắt. Phần kết hợp từ sẽ học kỹ."),
    ("打压", "dǎyā", "đả áp", "động từ", "chèn ép, đàn áp", "大公司利用自己的优势打压小公司。", "Công ty lớn lợi dụng ưu thế của mình để chèn ép công ty nhỏ.",
     "Động từ, nghĩa là đánh và đè nén, tức chèn ép. Trong bài: 有人希望苹果打压一把高通, có người mong Apple chèn ép Qualcomm một phen."),
    ("微妙", "wēimiào", "vi diệu", "tính từ", "tế nhị, khó nắm bắt, khó nói", "他们两个人的关系很微妙。", "Quan hệ giữa hai người họ rất tế nhị.",
     "Tính từ. Cẩn thận, từ dễ nhầm: tiếng Việt vi diệu là thần kỳ, tuyệt diệu; còn 微妙 trong tiếng Trung là tinh tế, khó nắm bắt, khó nói thành lời. 关系微妙 là quan hệ tế nhị; 微妙的心理 là tâm lý khó nói."),
    ("初衷", "chūzhōng", "sơ trung", "danh từ", "ý định ban đầu, tâm nguyện ban đầu", "我们不能忘了创业的初衷。", "Chúng ta không được quên ý định ban đầu khi khởi nghiệp.",
     "Danh từ, nghĩa là mong muốn ban đầu. Chữ 衷 là lòng, như trong 衷心, thành tâm. Kết hợp: 不改初衷, không đổi ý định ban đầu; 有负初衷, phụ lòng mong muốn ban đầu. Gần nghĩa với 初心 trong 不忘初心."),
    ("发难", "fānàn", "phát nạn", "động từ", "chất vấn, làm khó; gây sự", "会上，几位股东突然向总经理发难。", "Trong cuộc họp, mấy cổ đông bất ngờ chất vấn làm khó tổng giám đốc.",
     "Động từ, nghĩa là đặt câu hỏi để làm khó, phát động công kích. Chú ý chữ 难 đọc thanh bốn, nàn, như trong 灾难. Trong bài: 尽管发难苹果, tuy làm khó Apple."),
    ("争端", "zhēngduān", "tranh đoan", "danh từ", "mối tranh chấp", "两国通过谈判解决了边界争端。", "Hai nước đã giải quyết tranh chấp biên giới bằng đàm phán.",
     "Danh từ, chỉ sự việc gây ra tranh chấp. Chữ 端 là đầu mối. Kết hợp: 解决争端, 国际争端, 贸易争端."),
    ("芯片", "xīnpiàn", "tâm phiến", "danh từ", "chip, vi mạch", "手机的核心部件是芯片。", "Linh kiện cốt lõi của điện thoại là chip.",
     "Danh từ, nghĩa là chip bán dẫn, vi mạch tích hợp. Chữ 芯 là lõi, ruột, như 灯芯, bấc đèn; 片 là miếng mỏng. Qualcomm là công ty chip nổi tiếng với dòng chip Snapdragon."),
    ("无线", "wúxiàn", "vô tuyến", "danh từ", "vô tuyến, không dây", "这家咖啡馆有免费的无线网络。", "Quán cà phê này có mạng không dây miễn phí.",
     "Danh từ, cũng làm định ngữ, nghĩa là không dây, vô tuyến. 无线网络 là mạng không dây, wifi; 无线通信 là thông tin không dây, lĩnh vực mà Qualcomm dẫn đầu."),
    ("巨擘", "jùbò", "cự phách", "danh từ", "người (vật) kiệt xuất, ông trùm", "他是金融界的巨擘。", "Ông ấy là ông trùm của giới tài chính.",
     "Danh từ, văn viết. 擘 là ngón tay cái, chữ này đọc bò. Ví với người hay tổ chức kiệt xuất nhất trong một lĩnh vực. Âm Hán Việt cự phách, và tiếng Việt cũng dùng cự phách với đúng nghĩa này."),
    ("究", "jiū", "cứu", "động từ", "tìm tòi, truy xét đến cùng", "究其原因，主要是管理不善。", "Xét đến nguyên nhân, chủ yếu là do quản lý kém.",
     "Bảng từ của sách ghi là phó từ, nhưng trong bài nó mang nghĩa động từ: tìm tòi, truy xét. Chữ này có trong 研究, 追究, 深究, 讲究. Cụm cố định 究其原因 là mẫu câu trọng điểm của bài."),
    ("垄断", "lǒngduàn", "lũng đoạn", "động từ", "độc quyền, lũng đoạn", "这家公司垄断了国内市场。", "Công ty này độc quyền thị trường trong nước.",
     "Động từ, nghĩa là nắm giữ và độc chiếm thị trường. Âm Hán Việt lũng đoạn, tiếng Việt cũng nói lũng đoạn thị trường. 反垄断 là chống độc quyền; 垄断地位 là vị trí độc quyền."),
    ("霸王条款", "bàwáng tiáokuǎn", "bá vương điều khoản", "danh từ", "điều khoản bất bình đẳng, điều khoản “bá đạo”", "“商品一经售出，概不退换”是典型的霸王条款。", "“Hàng đã bán miễn đổi trả” là điều khoản bất bình đẳng điển hình.",
     "Danh từ. 霸王 là bá vương, kẻ ngang ngược. 霸王条款 là điều khoản do một bên tự đặt ra, hạn chế hoặc xâm hại quyền lợi người tiêu dùng, đối tác, như câu hàng đã bán miễn đổi trả rất quen thuộc."),
    ("下游", "xiàyóu", "hạ du", "danh từ", "hạ lưu; khâu hạ nguồn (của chuỗi ngành)", "芯片涨价，下游的手机厂商压力很大。", "Chip tăng giá, các hãng điện thoại ở khâu hạ nguồn chịu áp lực rất lớn.",
     "Danh từ, nghĩa gốc là hạ lưu của con sông; trong kinh tế là khâu cuối của chuỗi ngành. Trái nghĩa là 上游, thượng nguồn. Qualcomm ở thượng nguồn, các hãng điện thoại ở hạ nguồn."),
    ("高额", "gāo'é", "cao ngạch", "tính từ", "(số tiền) cao, lớn", "他为这次比赛拿到了高额奖金。", "Anh ấy nhận được khoản tiền thưởng lớn trong cuộc thi này.",
     "Tính từ thuộc tính, chỉ đứng trước danh từ chỉ tiền: 高额利润，高额奖金，高额专利许可费. Chữ 额 là định mức, như trong 金额, số tiền."),
    ("业内", "yènèi", "nghiệp nội", "danh từ", "trong ngành", "业内人士认为，房价还会继续上涨。", "Người trong ngành cho rằng giá nhà sẽ còn tiếp tục tăng.",
     "Danh từ, nghĩa là trong phạm vi một ngành nghề. Cụm hay gặp nhất là 业内人士, người trong ngành, rất phổ biến trên báo chí."),
    ("戏称", "xìchēng", "hí xưng", "động từ", "gọi đùa", "同学们戏称他为“活字典”。", "Các bạn cùng lớp gọi đùa cậu ấy là “cuốn từ điển sống”.",
     "Động từ, nghĩa là gọi đùa, gọi một cách bông đùa. Chữ 戏 là đùa, như 游戏. Đây là mẫu câu trọng điểm 戏称为."),
    ("渔利", "yúlì", "ngư lợi", "danh từ", "món lợi kiếm được nhờ thời cơ (khi người khác tranh nhau)", "两家打价格战，第三家坐收渔利。", "Hai nhà đánh nhau bằng giá, nhà thứ ba ngồi không hưởng lợi.",
     "Danh từ, nghĩa là lợi ích không chính đáng kiếm được nhờ thời cơ. Xuất phát từ câu 鹬蚌相争，渔翁得利, tiếng Việt là trai cò tranh nhau, ngư ông đắc lợi. Thành ngữ 坐收渔利 cũng có trong bài."),
    ("一站式", "yízhànshì", "nhất trạm thức", "tính từ", "trọn gói, một cửa", "这家医院为病人提供一站式服务。", "Bệnh viện này cung cấp dịch vụ trọn gói cho bệnh nhân.",
     "Tính từ, nghĩa là gom mọi thứ vào một chỗ, làm một lần là xong hết thủ tục. 一站式服务 là dịch vụ trọn gói, dịch vụ một cửa; 一站式办公 là cơ chế một cửa."),
    ("要命", "yàomìng", "yếu mệnh", "tính từ", "gay go, chết người; (mức độ) quá chừng", "更要命的是，他把护照也弄丢了。", "Gay hơn nữa là anh ấy làm mất luôn cả hộ chiếu.",
     "Tính từ, nghĩa là gây hậu quả nghiêm trọng, gay go; còn làm bổ ngữ chỉ mức độ cao như 疼得要命, đau chết đi được. Cụm 更要命的是 là gay hơn nữa là, tệ hơn nữa là, dùng để đưa ra điều nghiêm trọng hơn."),
    ("反向", "fǎnxiàng", "phản hướng", "động từ", "ngược chiều, ngược lại", "这辆车在高速公路上反向行驶，非常危险。", "Chiếc xe này chạy ngược chiều trên đường cao tốc, cực kỳ nguy hiểm.",
     "Động từ, nghĩa là theo hướng ngược lại. Kết hợp: 反向行驶, chạy ngược chiều; 反向思维, tư duy ngược; trong bài là 专利反向授权, trao quyền sáng chế ngược lại cho Qualcomm."),
    ("稳固", "wěngù", "ổn cố", "động từ", "củng cố, làm vững chắc", "公司通过降价稳固了自己的市场地位。", "Công ty đã củng cố vị thế thị trường của mình bằng cách giảm giá.",
     "Động từ, nghĩa là làm cho vững chắc; cũng làm tính từ, nghĩa là vững chắc. Trong bài: 稳固自己的市场支配地位, củng cố vị thế chi phối thị trường của mình."),
    ("无形", "wúxíng", "vô hình", "tính từ", "vô hình, không thấy được", "父母的习惯会在无形之中影响孩子。", "Thói quen của bố mẹ sẽ ảnh hưởng tới con cái một cách vô hình.",
     "Tính từ, nghĩa là không có hình dạng, không nhìn thấy được. Thường dùng 无形中, 无形之中, nghĩa là một cách vô hình, lúc nào không hay. Đây là mẫu câu trọng điểm."),
    ("削弱", "xuēruò", "tước nhược", "động từ", "làm suy yếu", "这场战争大大削弱了这个国家的实力。", "Cuộc chiến này đã làm suy yếu nghiêm trọng thực lực của đất nước ấy.",
     "Động từ, nghĩa là làm cho yếu đi. Chú ý chữ 削 ở đây đọc xuē, như trong 剥削, 削减; còn khi nói 削苹果, gọt táo, thì đọc xiāo. Phần kết hợp từ sẽ học kỹ."),
    ("搭售", "dāshòu", "đáp thụ", "động từ", "bán kèm (bắt buộc)", "商店不得强行搭售商品。", "Cửa hàng không được ép khách mua kèm hàng hóa.",
     "Động từ, nghĩa là bán kèm bắt buộc: muốn mua món này thì phải mua thêm món khác. Chữ 搭 là kèm, ghép; 售 là bán. Đây là một hành vi mà luật chống độc quyền cấm."),
    ("捆绑", "kǔnbǎng", "khổn bảng", "động từ", "trói buộc; gộp, bó chung lại", "很多运营商把手机和套餐捆绑销售。", "Nhiều nhà mạng bán điện thoại gộp chung với gói cước.",
     "Động từ, nghĩa gốc là trói, buộc; nghĩa bóng là gộp chặt hai thứ với nhau. 捆绑销售 là bán gộp, bán theo combo bắt buộc. Trong bài: 将专利许可与销售芯片进行捆绑."),
    ("附加", "fùjiā", "phụ gia", "động từ", "kèm thêm, phụ thêm", "合同里附加了几条特别说明。", "Trong hợp đồng có kèm thêm mấy điều giải thích đặc biệt.",
     "Động từ, nghĩa là thêm vào, kèm thêm. Lưu ý: tiếng Việt phụ gia thường chỉ chất phụ gia thực phẩm, tiếng Trung là 添加剂; còn 附加 là kèm thêm, như 附加费, phụ phí; 附加题, câu hỏi phụ."),
    ("立案", "lì'àn", "lập án", "động từ", "lập hồ sơ vụ án, thụ lý", "警方已对此事立案调查。", "Cảnh sát đã lập án điều tra việc này.",
     "Động từ li hợp, nghĩa là lập hồ sơ một vụ việc để điều tra, xét xử. Hay gặp 立案调查, 立案侦查. Trong bài: 发改委对高通公司采取反垄断立案调查."),
    ("路数", "lùshù", "lộ số", "danh từ", "cách thức, đường đi nước bước", "他做生意的路数跟别人不一样。", "Cách làm ăn của anh ấy khác người khác.",
     "Danh từ, nghĩa là phương pháp, cách làm, chiêu thức. Trong bài: 高通公司从来玩的都là控制专利权与出卖行业技术标准的路数, chiêu thức của Qualcomm xưa nay là kiểm soát bằng sáng chế và bán tiêu chuẩn công nghệ của ngành."),
    ("玩转", "wánzhuǎn", "ngoạn chuyển", "động từ", "chơi thạo, làm chủ, thành thạo", "我奶奶七十岁了，却能玩转智能手机。", "Bà tôi bảy mươi tuổi rồi mà vẫn dùng thạo điện thoại thông minh.",
     "Động từ, nghĩa là chơi giỏi, làm chủ hoàn toàn một việc gì đó. Rất hay gặp trong quảng cáo, như 玩转南京, khám phá trọn Nam Kinh. Trong bài: 要玩转这个模式, muốn vận hành trơn tru mô hình này."),
    ("扯皮", "chěpí", "xả bì", "động từ", "cãi cọ dây dưa, đùn đẩy", "两个部门互相扯皮，问题一直没有解决。", "Hai bộ phận đùn đẩy cho nhau, vấn đề mãi không được giải quyết.",
     "Động từ li hợp, nghĩa là tranh cãi không có nguyên tắc, cãi cọ dây dưa. 扯 là kéo, 皮 là da. Trong bài: 打官司扯皮的能力, khả năng kiện tụng, cãi lý dây dưa."),
    ("营收", "yíngshōu", "doanh thu", "danh từ", "doanh thu", "公司去年的营收超过了十亿元。", "Doanh thu năm ngoái của công ty vượt một tỷ tệ.",
     "Danh từ, nói gọn của 营业收入, thu nhập từ kinh doanh. Âm Hán Việt chính là doanh thu, nghĩa giống hệt tiếng Việt."),
    ("监管", "jiānguǎn", "giám quản", "động từ", "giám sát và quản lý", "政府加强了对食品安全的监管。", "Chính phủ đã tăng cường giám sát quản lý an toàn thực phẩm.",
     "Động từ, nghĩa là giám sát và quản lý. Kết hợp: 加强监管, 监管部门, cơ quan quản lý; trong bài là 监管壁垒, rào cản về quản lý."),
    ("乖乖", "guāiguāi", "quai quai", "tính từ", "ngoan ngoãn, ngoan ngoãn chịu", "孩子们都乖乖地坐着听故事。", "Bọn trẻ đều ngoan ngoãn ngồi nghe kể chuyện.",
     "Tính từ, nghĩa là ngoan ngoãn, nghe lời. Dùng với người lớn, tổ chức thì có ý châm biếm: buộc phải ngoan ngoãn chịu. Trong bài: 高通乖乖认罚, Qualcomm ngoan ngoãn chịu phạt."),
    ("认罚", "rènfá", "nhận phạt", "động từ", "chấp nhận bị phạt", "他承认自己违反了交通规则，愿意认罚。", "Anh ấy thừa nhận đã vi phạm luật giao thông, sẵn sàng chịu phạt.",
     "Động từ li hợp, nghĩa là đồng ý chịu phạt. Tương tự: 认错, nhận lỗi; 认输, chịu thua."),
    ("有余", "yǒuyú", "hữu dư", "động từ", "có dư; hơn (một con số)", "这项工程历时三年有余。", "Công trình này kéo dài hơn ba năm.",
     "Động từ, nghĩa là còn thừa, vượt quá mức đủ. Đứng sau con số thì nghĩa là hơn: 一年有余, hơn một năm. Thành ngữ 绰绰有余 là dư dả, thừa sức."),
    ("罚单", "fádān", "phạt đơn", "danh từ", "giấy phạt, quyết định xử phạt", "他因为超速收到了一张罚单。", "Anh ấy nhận một giấy phạt vì chạy quá tốc độ.",
     "Danh từ, nghĩa là giấy thông báo nộp phạt. Động từ đi kèm là 开: 开罚单, lập biên bản phạt. Trong bài: 开出了中国反垄断历史上金额最大的罚单."),
    ("责令", "zélìng", "trách lệnh", "động từ", "ra lệnh (buộc phải làm)", "环保部门责令这家工厂停产整改。", "Cơ quan môi trường buộc nhà máy này dừng sản xuất để khắc phục.",
     "Động từ, văn viết, nghĩa là cơ quan có thẩm quyền ra lệnh buộc ai đó phải làm việc gì. Thường đi với 整改, 停产, 退还."),
    ("整改", "zhěnggǎi", "chỉnh cải", "động từ", "chỉnh đốn và sửa đổi, khắc phục", "检查组发现问题后，要求立即整改。", "Đoàn kiểm tra phát hiện vấn đề liền yêu cầu khắc phục ngay.",
     "Động từ, nghĩa là chỉnh đốn và cải tiến, khắc phục sai phạm. Kết hợp: 全面整改, 整改措施, biện pháp khắc phục."),
    ("顶多", "dǐngduō", "đỉnh đa", "phó từ", "cùng lắm, nhiều nhất là", "这件衣服顶多值一百块。", "Chiếc áo này cùng lắm chỉ đáng một trăm tệ.",
     "Phó từ khẩu ngữ, biểu thị giới hạn tối đa: cùng lắm, nhiều nhất. Đây là mẫu câu trọng điểm."),
    ("聘用", "pìnyòng", "sính dụng", "động từ", "tuyển dụng, thuê (người làm)", "公司聘用了一位有经验的律师。", "Công ty đã thuê một luật sư giàu kinh nghiệm.",
     "Động từ, nghĩa là mời và dùng người, tuyển dụng. 聘 là mời, như 招聘, tuyển dụng; 聘请, mời. 聘用合同 là hợp đồng tuyển dụng."),
    ("覆盖", "fùgài", "phúc cái", "động từ", "che phủ, bao phủ; bù đắp (chi phí)", "这个城市的地铁已经覆盖了所有的区。", "Tàu điện ngầm của thành phố này đã phủ khắp tất cả các quận.",
     "Động từ, nghĩa gốc là che phủ: 积雪覆盖大地. Nghĩa mở rộng là bao phủ một phạm vi. Trong bài nghĩa là đủ bù đắp chi phí: 律师费用无法覆盖省下来的费用."),
    ("条款", "tiáokuǎn", "điều khoản", "danh từ", "điều khoản", "签合同前，一定要看清楚每一个条款。", "Trước khi ký hợp đồng, nhất định phải đọc kỹ từng điều khoản.",
     "Danh từ, chỉ các điều mục trong văn bản, hợp đồng. Âm Hán Việt chính là điều khoản. 法律条款 là điều khoản pháp luật; 不平等的条款 là điều khoản bất bình đẳng."),
    ("窄", "zhǎi", "trách", "tính từ", "hẹp; (nghĩa bóng) ít, hạn hẹp", "这条路太窄了，两辆车过不去。", "Con đường này hẹp quá, hai xe không đi qua được.",
     "Tính từ, nghĩa là hẹp, trái nghĩa với 宽, rộng. Nghĩa bóng là ít đường, hạn hẹp: 销售渠道越来越窄, kênh bán hàng ngày càng hẹp. 心眼儿窄 là hẹp hòi."),
    ("加之", "jiāzhī", "gia chi", "liên từ", "thêm vào đó, cộng thêm", "今天天气不好，加之路上堵车，他迟到了半个小时。", "Hôm nay thời tiết xấu, thêm vào đó đường lại tắc, anh ấy đến muộn nửa tiếng.",
     "Liên từ văn viết, nghĩa là thêm vào đó, giống 加上. Dùng để bổ sung thêm nguyên nhân hay điều kiện. Đây là mẫu câu trọng điểm."),
    ("下滑", "xiàhuá", "hạ hoạt", "động từ", "trượt xuống, giảm sút", "最近他的成绩明显下滑。", "Gần đây thành tích của cậu ấy giảm sút rõ rệt.",
     "Động từ, nghĩa là trượt xuống, thường nói về thành tích, chất lượng, kinh tế. Phần kết hợp từ sẽ học: 成绩下滑, 经济下滑, 直线下滑."),
    ("格局", "géjú", "cách cục", "danh từ", "cục diện, cơ cấu, bố cục", "新技术改变了整个行业的格局。", "Công nghệ mới đã thay đổi cục diện của cả ngành.",
     "Danh từ, chỉ cấu trúc và hình thức tổng thể của sự vật, tức cục diện. Kết hợp: 打破旧格局, 形成新格局. Giới trẻ Trung Quốc còn nói 格局大, chỉ người có tầm nhìn rộng, tâm thế rộng lượng."),
]

add("bullets", chapter="Từ mới (50 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 8.2 có 50 từ mới, chia thành 17 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 发难 (nàn) · 巨擘 (bò) · 削弱 (xuē) · 贴切 (qiè) · 一站式 (yí)",
           "Từ Hán Việt “quen mặt”: 垄断 lũng đoạn · 巨擘 cự phách · 营收 doanh thu · 条款 điều khoản · 微妙 ≠ vi diệu"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có năm mươi từ, thầy chia thành mười bảy nhóm nhỏ. Có cả từ lóng mạng như 刷屏, 互撕, lẫn từ ngữ kinh tế pháp luật như 垄断, 搭售, 立案, 整改.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Chú ý cách đọc của một số chữ: 发难 đọc là fānàn, 巨擘 đọc là jùbò, 削弱 đọc là xuēruò, 贴切 đọc là tiēqiè."),
         F(4, "Bài này có nhiều từ Hán Việt người Việt dùng hằng ngày, như 垄断, lũng đoạn; 巨擘, cự phách; 营收, doanh thu; 条款, điều khoản. Nhưng cũng có từ dễ nhầm: 微妙 không phải là vi diệu đâu nhé. Chúng ta bắt đầu.")])

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
    ("库克和高通的口水战持续刷屏，不断有新料爆出，一场巨头互撕的大戏，吃瓜群众也看得不亦乐乎。网友对这件事的心态，与其说“幸灾乐祸”，不如说“鹬蚌相争，渔翁得利”更贴切。有人希望高通啃苹果一口，也有人希望苹果打压一把高通。",
     "Cuộc khẩu chiến giữa Tim Cook và Qualcomm liên tục phủ sóng mạng, không ngừng có tin mới bị tung ra; một màn kịch lớn các ông trùm xâu xé nhau, đám đông “ăn dưa” hóng chuyện cũng xem say sưa không dứt. Tâm lý của cư dân mạng về việc này, nói là “hả hê trên nỗi đau của người khác”, chẳng bằng nói là “trai cò tranh nhau, ngư ông đắc lợi” thì đúng hơn. Có người mong Qualcomm cắn Apple một miếng, cũng có người mong Apple chèn ép Qualcomm một phen.",
     ["库克 là Tim Cook, tổng giám đốc Apple. 口水战 là khẩu chiến; 刷屏 là phủ sóng mạng. 新料 là tin mới, chuyện mới. 巨头 là ông trùm, gã khổng lồ. 吃瓜群众 là đám đông ăn dưa, tức người chỉ đứng xem, không phát biểu. 看得不亦乐乎 là xem say sưa không dứt.",
      "与其说，不如说 là nói… chẳng bằng nói…, mẫu câu trọng điểm. 幸灾乐祸 là vui sướng trên tai họa của người khác. 鹬蚌相争，渔翁得利 là trai cò tranh nhau, ngư ông đắc lợi. 啃苹果一口 là cắn quả táo một miếng, chơi chữ với tên Apple, 苹果. 打压一把 là chèn ép một phen."]),
    ("其实对高通来说，与苹果打官司的心态很微妙。有评论说高通是要逼死苹果，的确在苹果股价跌得一发不可收拾的时候，高通仿佛是要落井下石。但毋庸置疑，高通的初衷可不是想把苹果告黄。尽管发难苹果，让其左右为难，但高通并不希望在专利许可领域的争端影响双方芯片领域的正常合作。",
     "Thật ra, đối với Qualcomm, tâm lý khi kiện Apple rất tế nhị. Có bình luận nói Qualcomm muốn dồn Apple vào chỗ chết; quả thật, đúng lúc giá cổ phiếu Apple tụt dốc không phanh, Qualcomm dường như muốn ném đá xuống giếng. Nhưng không nghi ngờ gì, ý định ban đầu của Qualcomm đâu phải là kiện cho Apple sập tiệm. Tuy làm khó Apple, khiến Apple tiến thoái lưỡng nan, nhưng Qualcomm không hề muốn tranh chấp trong lĩnh vực cấp phép sáng chế ảnh hưởng đến sự hợp tác bình thường của hai bên trong lĩnh vực chip.",
     ["微妙 là tế nhị, khó nói. 逼死 là dồn vào chỗ chết. 股价 là giá cổ phiếu. 一发不可收拾 là một khi đã xảy ra thì không cứu vãn nổi. 落井下石 là ném đá xuống giếng, thừa lúc người gặp nạn mà hãm hại.",
      "毋庸置疑 là không cần nghi ngờ, chắc chắn; 毋庸 là không cần, văn viết. 初衷 là ý định ban đầu. 告黄 là kiện cho sập tiệm; 黄 trong khẩu ngữ là thất bại, đổ bể, như 生意黄了. 发难 là làm khó. 左右为难 là tiến thoái lưỡng nan. Qualcomm vừa bán chip cho Apple, vừa kiện Apple, nên tâm lý rất tế nhị."]),
    ("至今，全球通过高通技术许可生产的设备已超过100亿台，连起来可以绕地球三十圈。手握大量高价值专利的无线通信行业巨擘——高通公司近年来没少因专利问题打官司。究其原因，有恃无恐的高通，凭借着技术的垄断地位，开始了一场又一场不平等的市场交易，一系列霸王条款让下游企业苦不堪言。",
     "Đến nay, số thiết bị trên toàn cầu được sản xuất nhờ giấy phép công nghệ của Qualcomm đã vượt 10 tỷ chiếc, xếp nối nhau có thể quấn quanh Trái Đất ba mươi vòng. Ông trùm ngành thông tin không dây nắm trong tay vô số bằng sáng chế giá trị cao, Qualcomm, mấy năm gần đây đã kiện tụng không ít vì chuyện bằng sáng chế. Xét đến nguyên nhân, Qualcomm có chỗ dựa nên chẳng sợ gì, dựa vào vị trí độc quyền công nghệ, bắt đầu hết vụ giao dịch bất bình đẳng này đến vụ khác, hàng loạt điều khoản bá đạo khiến các doanh nghiệp hạ nguồn khổ không kể xiết.",
     ["技术许可 là cấp phép công nghệ. 绕地球三十圈 là quấn quanh Trái Đất ba mươi vòng. 手握 là nắm trong tay. 巨擘 là cự phách, ông trùm. 没少因专利问题打官司 là kiện tụng không ít vì chuyện sáng chế; 没少 là không ít, khẩu ngữ.",
      "究其原因 là xét đến nguyên nhân, mẫu câu trọng điểm. 有恃无恐 là có chỗ dựa nên không sợ gì. 凭借 là dựa vào. 一场又一场 là hết vụ này đến vụ khác. 霸王条款 là điều khoản bá đạo. 苦不堪言 là khổ không nói nên lời."],
     "至今，全球通过高通技术许可生产的设备已超过一百亿台，连起来可以绕地球三十圈。手握大量高价值专利的无线通信行业巨擘——高通公司近年来没少因专利问题打官司。究其原因，有恃无恐的高通，凭借着技术的垄断地位，开始了一场又一场不平等的市场交易，一系列霸王条款让下游企业苦不堪言。"),
    ("向厂商有偿提供芯片和组合专利的一站式服务，高通收取高额专利许可费的同时，另外再按厂商整机售价的5%，收取专利使用费。有业内人士戏称购了“鸡腿”却要为“整鸡”买单。要知道，2013年中国手机厂商的净利润不足0.5%，而高通却坐收5%的渔利，赚得盆满钵满。",
     "Qualcomm cung cấp có thu phí dịch vụ trọn gói gồm chip và gói bằng sáng chế cho các hãng sản xuất; cùng lúc thu phí cấp phép sáng chế rất cao, Qualcomm còn thu thêm phí sử dụng sáng chế bằng 5% giá bán nguyên chiếc máy của hãng. Có người trong ngành gọi đùa là mua cái “đùi gà” mà phải trả tiền cho cả “con gà”. Phải biết rằng, năm 2013, lợi nhuận ròng của các hãng điện thoại Trung Quốc chưa tới 0,5%, mà Qualcomm lại ngồi không hưởng 5%, kiếm bộn tiền.",
     ["厂商 là hãng sản xuất. 有偿 là có trả tiền, trái nghĩa 无偿. 一站式服务 là dịch vụ trọn gói. 整机售价 là giá bán của cả chiếc máy. Cách thu phí này bị chỉ trích vì Qualcomm chỉ cung cấp một phần công nghệ, nhưng lại tính phí theo giá của cả chiếc điện thoại.",
      "戏称 là gọi đùa, mẫu câu trọng điểm. 购了鸡腿却要为整鸡买单 là mua đùi gà mà phải trả tiền cả con gà; 买单 là trả tiền. 净利润 là lợi nhuận ròng. 坐收渔利 là ngồi không hưởng lợi. 盆满钵满 là đầy chậu đầy bát, tức kiếm bộn tiền."],
     "向厂商有偿提供芯片和组合专利的一站式服务，高通收取高额专利许可费的同时，另外再按厂商整机售价的百分之五，收取专利使用费。有业内人士戏称购了鸡腿却要为整鸡买单。要知道，二零一三年中国手机厂商的净利润不足百分之零点五，而高通却坐收百分之五的渔利，赚得盆满钵满。"),
    ("更要命的是和它交易的厂商还要接受它的“专利反向授权协议”。通过要求其他企业专利反向许可，高通公司一方面能够更进一步稳固自己的市场支配地位，另一方面也无形之中削弱了其他企业的研发能力和研发动力。",
     "Gay go hơn nữa là các hãng giao dịch với Qualcomm còn phải chấp nhận “thỏa thuận trao quyền sáng chế ngược lại” của nó. Bằng cách yêu cầu các doanh nghiệp khác cấp phép ngược lại bằng sáng chế của họ, một mặt Qualcomm có thể củng cố thêm vị thế chi phối thị trường của mình, mặt khác cũng vô hình trung làm suy yếu năng lực và động lực nghiên cứu phát triển của các doanh nghiệp khác.",
     ["更要命的是 là gay go hơn nữa là. 专利反向授权协议 là thỏa thuận trao quyền ngược: hãng điện thoại phải cho Qualcomm dùng miễn phí sáng chế của mình. 一方面，另一方面 là một mặt, mặt khác.",
      "稳固 là củng cố. 市场支配地位 là vị thế chi phối thị trường, một thuật ngữ của luật chống độc quyền. 无形之中 là vô hình trung, mẫu câu trọng điểm. 削弱 là làm suy yếu. 研发 là nghiên cứu phát triển, R&D. Sáng chế làm ra lại phải cho Qualcomm dùng, thì ai còn muốn nghiên cứu nữa?"]),
    ("高通公司在无线标准必要专利许可中，搭售非无线标准必要专利许可，还将专利许可与销售芯片进行捆绑，实行整体收费。此外，高通公司也对过期专利继续收费，拒绝对有竞争关系的芯片生产企业进行专利许可，还在专利许可和芯片销售中附加不合理的交易条件。",
     "Khi cấp phép các sáng chế thiết yếu theo tiêu chuẩn không dây, Qualcomm bán kèm giấy phép các sáng chế không thiết yếu, còn gộp chung việc cấp phép sáng chế với bán chip để thu phí trọn gói. Ngoài ra, Qualcomm còn tiếp tục thu phí với những sáng chế đã hết hạn, từ chối cấp phép cho các doanh nghiệp sản xuất chip có quan hệ cạnh tranh, và còn kèm thêm những điều kiện giao dịch bất hợp lý khi cấp phép sáng chế và bán chip.",
     ["Đoạn này liệt kê các hành vi bị coi là lạm dụng vị trí độc quyền. 标准必要专利 là sáng chế thiết yếu theo tiêu chuẩn, ai làm điện thoại cũng buộc phải dùng. 搭售 là bán kèm bắt buộc: muốn mua cái cần thiết thì phải mua cả cái không cần.",
      "捆绑 là gộp chặt; 整体收费 là thu phí trọn gói. 过期专利 là sáng chế đã hết thời hạn bảo hộ, lẽ ra phải được dùng miễn phí. 拒绝 là từ chối. 附加不合理的交易条件 là kèm thêm điều kiện giao dịch bất hợp lý."]),
    ("不仅如此，看人下菜碟的高通对诺基亚和三星的许可费用低于中国手机厂商，歧视性许可让人义愤填膺、忍无可忍。被压榨且不堪重负的手机厂商决定拿起法律的武器反戈一击，2013年11月，中国国家发改委对高通公司采取“反垄断”立案调查。",
     "Không chỉ vậy, Qualcomm còn nhìn người mà đối xử: phí cấp phép cho Nokia và Samsung thấp hơn cho các hãng điện thoại Trung Quốc; kiểu cấp phép phân biệt đối xử này khiến người ta phẫn nộ, không thể nhịn được nữa. Các hãng điện thoại bị bóc lột, không chịu nổi gánh nặng, đã quyết định cầm lấy vũ khí pháp luật để quay giáo đánh lại. Tháng 11 năm 2013, Ủy ban Phát triển và Cải cách Quốc gia Trung Quốc đã lập án điều tra “chống độc quyền” đối với Qualcomm.",
     ["看人下菜碟 là nhìn người mà dọn món, tức đối xử khác nhau tùy người, mang nghĩa chê. 诺基亚 là Nokia, 三星 là Samsung. 歧视性许可 là cấp phép mang tính phân biệt đối xử. 义愤填膺 là căm phẫn đầy lồng ngực. 忍无可忍 là không thể nhịn được nữa.",
      "压榨 là bóc lột, vắt kiệt. 不堪重负 là không chịu nổi gánh nặng. 拿起法律的武器 là cầm vũ khí pháp luật. 反戈一击 là quay giáo đánh lại. 发改委 là Ủy ban Phát triển và Cải cách Quốc gia, cơ quan phụ trách chống độc quyền về giá lúc bấy giờ."],
     "不仅如此，看人下菜碟的高通对诺基亚和三星的许可费用低于中国手机厂商，歧视性许可让人义愤填膺、忍无可忍。被压榨且不堪重负的手机厂商决定拿起法律的武器反戈一击，二零一三年十一月，中国国家发改委对高通公司采取反垄断立案调查。"),
    ("高通公司从来玩的都是控制专利权与出卖行业技术标准的路数，要玩转这个模式，必须具备两点本领：除了要有了不起的技术创新的本事，还要有无与伦比的打官司“扯皮”的能力。早已身经百战的高通，其技术水平与官司本领绝对不容小觑。",
     "Chiêu thức Qualcomm xưa nay vẫn chơi là kiểm soát quyền sáng chế và bán các tiêu chuẩn công nghệ của ngành. Muốn vận hành trơn tru mô hình này, phải có hai bản lĩnh: ngoài tài đổi mới công nghệ phi thường, còn phải có khả năng kiện tụng “cãi lý dây dưa” không ai sánh bằng. Qualcomm từ lâu đã trăm trận dày dạn, trình độ công nghệ và bản lĩnh kiện tụng của nó tuyệt đối không thể xem thường.",
     ["路数 là chiêu thức. 出卖行业技术标准 là bán tiêu chuẩn công nghệ của ngành: công nghệ của Qualcomm trở thành tiêu chuẩn chung, ai cũng phải mua. 玩转 là vận hành thành thạo. 本领 và 本事 đều là bản lĩnh, tài năng.",
      "了不起 là phi thường. 无与伦比 là không gì sánh bằng. 扯皮 là cãi lý dây dưa. 身经百战 là thân trải trăm trận. 其 là của nó. 不容小觑 là không thể xem thường; 觑 đọc qù, là nhìn."]),
    ("但要知道，中国市场占据高通营收及利润的半壁江山。而在当前中国高度强调“科技自主创新”的市场环境下，高通最担心的问题是遭遇更严厉的监管壁垒。两害相权取其轻，高通这才转变了应对策略，乖乖认罚。历时一年有余的高通反垄断案，中国发改委对其开出了中国反垄断历史上金额最大的罚单60.88亿元，并责令其全面整改。",
     "Nhưng phải biết rằng, thị trường Trung Quốc chiếm tới một nửa doanh thu và lợi nhuận của Qualcomm. Mà trong môi trường thị trường hiện nay, khi Trung Quốc hết sức coi trọng “tự chủ đổi mới khoa học công nghệ”, điều Qualcomm lo nhất là gặp phải rào cản quản lý nghiêm ngặt hơn. Giữa hai cái hại thì chọn cái nhẹ hơn, Qualcomm lúc ấy mới thay đổi chiến lược ứng phó, ngoan ngoãn chịu phạt. Vụ án chống độc quyền với Qualcomm kéo dài hơn một năm, Ủy ban Phát triển và Cải cách Quốc gia đã ra mức phạt 6,088 tỷ tệ, lớn nhất trong lịch sử chống độc quyền của Trung Quốc, đồng thời buộc Qualcomm khắc phục toàn diện.",
     ["营收及利润 là doanh thu và lợi nhuận. 半壁江山 là nửa giang sơn, tức một nửa. 自主创新 là tự chủ đổi mới. 监管壁垒 là rào cản về quản lý. 两害相权取其轻 là cân nhắc hai cái hại thì chọn cái nhẹ hơn: chịu phạt còn hơn mất cả thị trường Trung Quốc.",
      "这才 là đến lúc ấy mới. 应对策略 là chiến lược ứng phó. 乖乖认罚 là ngoan ngoãn chịu phạt. 历时一年有余 là kéo dài hơn một năm. 六十点八八亿元 là sáu tỷ không trăm tám mươi tám triệu tệ, khoảng chín trăm bảy mươi lăm triệu đô la Mỹ, công bố tháng hai năm hai nghìn không trăm mười lăm. 责令其全面整改 là buộc Qualcomm khắc phục toàn diện."],
     "但要知道，中国市场占据高通营收及利润的半壁江山。而在当前中国高度强调科技自主创新的市场环境下，高通最担心的问题是遭遇更严厉的监管壁垒。两害相权取其轻，高通这才转变了应对策略，乖乖认罚。历时一年有余的高通反垄断案，中国发改委对其开出了中国反垄断历史上金额最大的罚单六十点八八亿元，并责令其全面整改。"),
    ("然而反垄断案并没有给高通带来什么实质性的影响，顶多就是敲山震虎，高通还是用合理的价格实现了其利益的合法化。即使整改之后，小企业仍摆脱不了“被欺负”的命运。因为中小企业能力有限，新合同根本看不懂，聘用能看懂合同还能谈判的律师费用可能根本无法覆盖省下来的费用，所以很多企业选择忍气吞声接受不平等的条款继续签约。",
     "Thế nhưng vụ án chống độc quyền không hề gây ảnh hưởng thực chất nào cho Qualcomm, cùng lắm chỉ là gõ núi dọa hổ; Qualcomm vẫn dùng mức giá hợp lý để hợp pháp hóa lợi ích của mình. Kể cả sau khi khắc phục, các doanh nghiệp nhỏ vẫn không thoát khỏi số phận “bị bắt nạt”. Vì năng lực của doanh nghiệp vừa và nhỏ có hạn, hợp đồng mới căn bản không đọc hiểu nổi, còn chi phí thuê luật sư vừa đọc hiểu hợp đồng vừa biết đàm phán có khi hoàn toàn không bù nổi khoản tiền tiết kiệm được, nên nhiều doanh nghiệp chọn nhịn nhục chấp nhận điều khoản bất bình đẳng mà tiếp tục ký hợp đồng.",
     ["实质性的影响 là ảnh hưởng thực chất. 顶多 là cùng lắm, mẫu câu trọng điểm. 敲山震虎 là gõ núi dọa hổ, tức răn đe. 合法化 là hợp pháp hóa: sau vụ phạt, Qualcomm hạ phí một chút, nhưng cách thu phí của nó lại thành hợp pháp.",
      "摆脱命运 là thoát khỏi số phận. 中小企业 là doanh nghiệp vừa và nhỏ. 聘用律师 là thuê luật sư. 覆盖 ở đây là bù đắp: tiền thuê luật sư còn nhiều hơn tiền tiết kiệm được. 忍气吞声 là nhịn nhục, nuốt giận. 签约 là ký hợp đồng."]),
    ("时过境迁，眼下手机芯片产业已经从高通一家独大向“百家争鸣”发展，苹果、三星、华为等厂商纷纷崛起，使得芯片销售利润率迅速下降。作为不生产手机设备的高通公司来说，芯片销售渠道越来越窄，销售价格越来越低，来自资本市场的压力越来越大。",
     "Thời thế đã đổi thay, hiện nay ngành chip điện thoại đã chuyển từ cảnh một mình Qualcomm thống trị sang cảnh “trăm nhà đua tiếng”: Apple, Samsung, Huawei và các hãng khác lần lượt vươn lên, khiến tỷ suất lợi nhuận từ bán chip giảm nhanh chóng. Đối với Qualcomm, một công ty không sản xuất điện thoại, kênh bán chip ngày càng hẹp, giá bán ngày càng thấp, áp lực từ thị trường vốn ngày càng lớn.",
     ["时过境迁 là thời gian trôi qua, hoàn cảnh đổi thay. 眼下 là hiện nay. 一家独大 là một nhà độc chiếm. 百家争鸣 là trăm nhà đua tiếng, vốn chỉ thời Xuân Thu Chiến Quốc, nay chỉ nhiều bên cùng cạnh tranh. Apple, Samsung, Huawei đều đã tự thiết kế chip riêng.",
      "崛起 là vươn lên, trỗi dậy. 使得 là khiến cho. 利润率 là tỷ suất lợi nhuận; chữ 率 đọc lǜ. 作为来说 là đối với… mà nói. 渠道 là kênh. 窄 là hẹp. 资本市场 là thị trường vốn."]),
    ("加之各国反垄断力度加强，高通不得不下调收费，使得专利授权费用利润率大幅下滑。多方不利的格局下，失去行业垄断地位的高通，在5G时代或将面临更多的挑战。",
     "Thêm vào đó, các nước tăng cường chống độc quyền, Qualcomm buộc phải hạ mức phí, khiến tỷ suất lợi nhuận từ phí cấp quyền sáng chế giảm mạnh. Trong cục diện bất lợi nhiều mặt, Qualcomm đã mất vị trí độc quyền trong ngành, có lẽ sẽ phải đối mặt với nhiều thách thức hơn trong thời đại 5G.",
     ["加之 là thêm vào đó, mẫu câu trọng điểm. 力度加强 là được tăng cường. 下调收费 là hạ mức phí; chữ 调 ở đây đọc tiáo. 大幅下滑 là giảm mạnh.",
      "格局 là cục diện. 或将 là có lẽ sẽ, văn viết. 面临挑战 là đối mặt thách thức. Câu kết cho thấy giang sơn dựng nên bằng kiện tụng cũng không thể giữ mãi; muốn đứng vững, cuối cùng vẫn phải dựa vào đổi mới thật sự."],
     "加之各国反垄断力度加强，高通不得不下调收费，使得专利授权费用利润率大幅下滑。多方不利的格局下，失去行业垄断地位的高通，在5G时代或将面临更多的挑战。"),
]
HEAD = {}

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 高通：打官司打出的“江山”", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa. Bài được cải biên từ bài viết cùng tên trên trang 砺石商业评论, Bình luận Thương mại Lệ Thạch, tác giả 金梅. Bài dài khoảng một nghìn bốn trăm chữ, giọng văn bình luận kinh tế, dùng dày đặc thành ngữ.",
         F(0, "Thầy chia bài thành mười hai đoạn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 90 else 50 if len(zh) <= 115 else 46 if len(zh) <= 150 else 44
    title = f"Bài khóa – đoạn {i}/{len(P)}" + (f" · {HEAD[i]}" if i in HEAD else "")
    add("passage", section="Bài khóa 课文", title=title, zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Bố cục & ghi chú", section="Bài khóa 课文", title="Bố cục bài khóa", size=34,
    items=["## 1. Mở đầu: khẩu chiến Qualcomm – Apple (đoạn 1–2)",
           "吃瓜群众看得不亦乐乎 · 鹬蚌相争，渔翁得利 · tâm lý 微妙: kiện nhưng vẫn muốn hợp tác",
           "## 2. Vì sao Qualcomm kiện tụng triền miên? (đoạn 3–6)",
           "垄断地位 → 霸王条款: thu 5% giá cả máy · 反向授权 · 搭售、捆绑、对过期专利收费",
           "## 3. Vụ chống độc quyền ở Trung Quốc (đoạn 7–10)",
           "歧视性许可 → 发改委立案调查 → 两害相权取其轻，乖乖认罚 60.88 亿元 → 顶多敲山震虎",
           "## 4. Thời thế đổi thay (đoạn 11–12)",
           "一家独大 → 百家争鸣 · 加之反垄断加强 → 5G时代面临更多挑战"],
    say=["Trước khi sang phần mẫu câu, chúng ta cùng nhìn lại bố cục bài khóa. Đây là một bài bình luận kinh tế, có bốn phần.",
         F(1, "Phần một, mở đầu: cuộc khẩu chiến giữa Qualcomm và Apple khiến cư dân mạng hóng hớt say sưa. Qualcomm kiện Apple, nhưng tâm lý rất tế nhị, vì vẫn muốn tiếp tục bán chip cho Apple."),
         F(3, "Phần hai: vì sao Qualcomm kiện tụng triền miên? Vì dựa vào vị trí độc quyền, nó đặt ra hàng loạt điều khoản bá đạo: thu phí theo giá cả chiếc máy, bắt trao quyền ngược lại, bán kèm, thu phí cả sáng chế đã hết hạn."),
         F(5, "Phần ba: các hãng điện thoại Trung Quốc phản công, Ủy ban Phát triển và Cải cách lập án điều tra. Qualcomm chọn cái hại nhẹ hơn, chịu phạt hơn sáu tỷ tệ, nhưng vụ phạt cùng lắm chỉ là gõ núi dọa hổ."),
         F(7, "Phần bốn: thời thế đổi thay, ngành chip từ một nhà độc chiếm chuyển sang trăm nhà đua tiếng; thêm vào đó là sức ép chống độc quyền, Qualcomm sẽ gặp nhiều thách thức hơn trong thời đại năm G.")])

add("bullets", section="Bài khóa 课文", title="Ghi chú 注释 (1): Qualcomm, Tim Cook, 吃瓜群众, 发改委", size=32,
    items=["高通 Qualcomm: lập năm 1985, trụ sở San Diego (California, Mỹ), hơn 35.400 nhân viên; mỗi năm dành 20% doanh thu cho R&D, đến đầu 2020 đã đầu tư hơn 61 tỷ USD",
           "库克 Tim Cook: sinh 1/11/1960 ở Alabama, CEO Apple, kế nhiệm Steve Jobs; rất coi trọng thị trường Trung Quốc, hơn chục lần sang thăm",
           "吃瓜群众 “quần chúng ăn dưa”: từ 2016, chỉ cư dân mạng chỉ đứng xem, không phát biểu; một trong “10 từ thịnh hành 2016” của tạp chí 《咬文嚼字》",
           "发改委: 国家发展和改革委员会 Ủy ban Phát triển và Cải cách Quốc gia; tiền thân là Ủy ban Kế hoạch Nhà nước (1952), đổi tên năm 2003"],
    say=["Sách có bảy ghi chú. Thầy chia làm hai slide.",
         F(0, "Một: 高通, Qualcomm, thành lập năm một nghìn chín trăm tám mươi lăm, trụ sở ở San Diego, bang California, nước Mỹ, có hơn ba mươi lăm nghìn bốn trăm nhân viên. Mỗi năm công ty dành hai mươi phần trăm doanh thu cho nghiên cứu phát triển; đến đầu năm hai nghìn không trăm hai mươi, tổng vốn đầu tư nghiên cứu đã vượt sáu mươi mốt tỷ đô la Mỹ."),
         F(1, "Hai: 库克, Tim Cook, sinh ngày một tháng mười một năm một nghìn chín trăm sáu mươi ở bang Alabama, là tổng giám đốc Apple, kế nhiệm Steve Jobs. Ông rất coi trọng thị trường Trung Quốc, đã hơn chục lần sang thăm."),
         F(2, "Ba: 吃瓜群众, quần chúng ăn dưa. Năm hai nghìn không trăm mười sáu, cư dân mạng gọi những người chỉ đứng xem mà không phát biểu ý kiến là 吃瓜群众, tức là chuyện không liên quan đến mình, chỉ hóng thôi. Từ này được tạp chí 咬文嚼字 bình chọn là một trong mười từ thịnh hành năm hai nghìn không trăm mười sáu. Cư dân mạng Việt Nam cũng hay nói ăn dưa, hóng drama đấy."),
         F(3, "Bốn: 发改委 là cách gọi tắt của 国家发展和改革委员会, Ủy ban Phát triển và Cải cách Quốc gia. Tiền thân là Ủy ban Kế hoạch Nhà nước, thành lập năm một nghìn chín trăm năm mươi hai, đổi thành tên hiện nay năm hai nghìn không trăm linh ba, phụ trách hoạch định chính sách phát triển kinh tế xã hội.")])

add("bullets", section="Bài khóa 课文", title="Ghi chú 注释 (2): 华为, 5G, 百家争鸣", size=33,
    items=["华为 Huawei: lập năm 1987, trụ sở ở Thâm Quyến; nhà cung cấp giải pháp ICT hàng đầu thế giới; 2/2018 cùng Vodafone thực hiện cuộc gọi 5G đầu tiên; 2021 doanh thu 636,8 tỷ tệ",
           "5G: công nghệ thông tin di động thế hệ thứ 5 – tốc độ cao, độ trễ thấp, kết nối lớn; nền tảng cho Internet vạn vật (xe kết nối, nhà thông minh, y tế từ xa…)",
           "百家争鸣: thời Xuân Thu – Chiến Quốc, nhiều trường phái tư tưởng (儒 Nho · 法 Pháp · 道 Đạo · 墨 Mặc…) viết sách, tranh luận; nay chỉ nhiều bên cùng tự do cạnh tranh"],
    say=[F(0, "Năm: 华为, Huawei, thành lập năm một nghìn chín trăm tám mươi bảy, trụ sở ở Thâm Quyến, tỉnh Quảng Đông, là nhà cung cấp giải pháp công nghệ thông tin và truyền thông hàng đầu thế giới. Tháng hai năm hai nghìn không trăm mười tám, Huawei cùng Vodafone hoàn thành cuộc gọi thử nghiệm năm G đầu tiên. Năm hai nghìn không trăm hai mươi mốt, tổng doanh thu đạt sáu trăm ba mươi sáu tỷ tám trăm triệu tệ."),
         F(1, "Sáu: 5G, công nghệ thông tin di động thế hệ thứ năm, có tốc độ cao, độ trễ thấp và khả năng kết nối lớn. Năm G không chỉ phục vụ liên lạc giữa người với người, mà còn kết nối người với vật, vật với vật, làm nền tảng cho xe kết nối, nhà thông minh, y tế từ xa."),
         F(2, "Bảy: 百家争鸣, trăm nhà đua tiếng. Thời Xuân Thu Chiến Quốc, xã hội biến động lớn, sinh ra nhiều trường phái tư tưởng như Nho gia, Pháp gia, Đạo gia, Mặc gia; họ viết sách lập thuyết, tranh luận với nhau, tạo nên sự phồn thịnh về học thuật. Ngày nay thành ngữ này chỉ cảnh nhiều bên cùng tự do cạnh tranh, phát biểu.")])

# ======================= MẪU CÂU =======================
add("bullets", chapter="Mẫu câu: 与其…不如 · 究其原因 · 戏称", section="Mẫu câu 重点句型", title="1. 与其……不如…… · 2. 究其原因……", size=33,
    items=["## 与其A，不如B: thay vì A, chẳng bằng B (B là lựa chọn tốt hơn)",
           "网友对这件事的心态，与其说“幸灾乐祸”，不如说“鹬蚌相争，渔翁得利”更贴切。",
           "与其这样坐以待毙，还不如想办法摆脱困境。",
           "与其等待救济，不如踏踏实实找份工作。",
           "## 究其原因……: xét đến nguyên nhân, truy ra nguyên nhân",
           "究其原因，有恃无恐的高通，凭借着技术的垄断地位，开始了一场又一场不平等的市场交易……",
           "这次他没有得到升职，究其原因，与他内向的性格，不善沟通有关。",
           "这支篮球队在近几届大赛上的名次一直没有突破，究其原因主要是内外线队员能力的不均衡。"],
    say=["Bây giờ chúng ta sang phần mẫu câu và từ ngữ trọng điểm. Bài này có sáu điểm, thầy gộp mỗi slide hai điểm. Đầu tiên là 与其不如 và 究其原因.",
         F(0, "与其A，不如B là cặp liên từ biểu thị quan hệ lựa chọn: thay vì A, chẳng bằng B; vế sau B là lựa chọn tốt hơn. Ở bài hai mươi của HSK sáu, chúng ta đã gặp 与其倒不如. Mẫu 与其说A，不如说B là nói A chẳng bằng nói B, dùng để đưa ra một cách nói chính xác hơn."),
         F(1, "Ví dụ từ bài khóa: 网友对这件事的心态，与其说幸灾乐祸，不如说鹬蚌相争，渔翁得利更贴切。 Nói là hả hê, chẳng bằng nói là trai cò tranh nhau, ngư ông đắc lợi thì đúng hơn."),
         F(2, "与其这样坐以待毙，还不如想办法摆脱困境。 Thay vì ngồi chờ chết như thế này, chẳng thà nghĩ cách thoát khỏi khó khăn. 坐以待毙 là ngồi chờ chết."),
         F(3, "与其等待救济，不如踏踏实实找份工作。 Thay vì chờ cứu trợ, chi bằng chăm chỉ tìm lấy một công việc. 踏踏实实 là chắc chắn, chăm chỉ, thiết thực."),
         F(4, "究其原因 nghĩa là xét kỹ nguyên nhân của nó. 究 là truy xét, 其 là của nó. Đứng đầu câu, sau khi đã nêu hiện tượng, để dẫn ra phân tích nguyên nhân. Văn viết, rất hay gặp trong bài báo, bài luận."),
         F(5, "Ví dụ từ bài khóa: 究其原因，有恃无恐的高通，凭借着技术的垄断地位，开始了一场又一场不平等的市场交易。"),
         F(6, "这次他没有得到升职，究其原因，与他内向的性格，不善沟通有关。 Lần này anh ấy không được thăng chức, xét đến nguyên nhân thì có liên quan đến tính cách hướng nội, không giỏi giao tiếp."),
         F(7, "这支篮球队在近几届大赛上的名次一直没有突破，究其原因主要是内外线队员能力的不均衡。 Đội bóng rổ này mấy giải gần đây thứ hạng mãi không đột phá, nguyên nhân chủ yếu là năng lực cầu thủ vòng trong và vòng ngoài không đồng đều.")])

add("bullets", section="Mẫu câu 重点句型", title="3. 戏称……/戏称……为…… · 4. （在）无形之中 + V", size=33,
    items=["## 戏称…… / 戏称A为B: gọi đùa (A là B)",
           "有业内人士戏称购了“鸡腿”却要为“整鸡”买单。",
           "有人戏称那些月底前花光了所有工资的人为“月光族”。",
           "很多人因为炒股一夜之间从百万富翁到负债百万，有人戏称其为“负翁”。",
           "## （在）无形之中 + V: vô hình trung, lúc nào không hay",
           "这也无形之中削弱了其他企业的研发能力和研发动力。",
           "贫穷不是错，可是贫穷者却在无形之中有一种自卑感。",
           "流言，是这个世界上最伤人的武器，无形之中便可以伤到你和周围的人。"],
    say=["Tiếp theo là 戏称 và 无形之中.",
         F(0, "戏称 nghĩa là gọi đùa. Có hai mẫu: 戏称 cộng một câu, và 戏称A为B, gọi đùa A là B. Chữ 为 đọc wéi. Đây là cách giới thiệu những biệt danh vui, từ lóng."),
         F(1, "Ví dụ từ bài khóa: 有业内人士戏称购了鸡腿却要为整鸡买单。 Người trong ngành gọi đùa là mua đùi gà mà phải trả tiền cả con gà."),
         F(2, "有人戏称那些月底前花光了所有工资的人为月光族。 Có người gọi đùa những ai chưa hết tháng đã tiêu sạch lương là tộc ánh trăng, 月光族; chữ 月 là tháng, 光 là hết sạch."),
         F(3, "很多人因为炒股一夜之间从百万富翁到负债百万，有人戏称其为负翁。 Nhiều người chơi chứng khoán, chỉ sau một đêm từ triệu phú thành nợ cả triệu, có người gọi đùa họ là 负翁, ông nợ. 负翁 đồng âm với 富翁, phú ông; 负 là nợ, âm."),
         F(4, "无形之中, hay 在无形之中, 无形中, nghĩa là vô hình trung, một cách không nhìn thấy, lúc nào không hay. Theo sau là động từ chỉ một ảnh hưởng, tác động."),
         F(5, "Ví dụ từ bài khóa: 这也无形之中削弱了其他企业的研发能力和研发动力。"),
         F(6, "贫穷不是错，可是贫穷者却在无形之中有一种自卑感。 Nghèo không phải là lỗi, nhưng người nghèo lại vô hình trung mang một cảm giác tự ti."),
         F(7, "流言，是这个世界上最伤人的武器，无形之中便可以伤到你和周围的人。 Tin đồn là thứ vũ khí gây tổn thương nhất trên đời, lúc nào không hay đã làm tổn thương bạn và những người xung quanh.")])

add("bullets", chapter="Mẫu câu: 无形之中 · 顶多 · 加之", section="Mẫu câu 重点句型", title="5. 顶多 + …… · 6. 加之……", size=33,
    items=["## 顶多: cùng lắm, nhiều nhất là (khẩu ngữ)",
           "然而反垄断案并没有给高通带来什么实质性的影响，顶多就是敲山震虎。",
           "这部手机顶多值千八百块钱，卖三千块钱简直是宰人。",
           "每个人的人生只能自己负责，别人的意见顶多作为参考。",
           "## 加之……: thêm vào đó, cộng thêm (văn viết, = 加上)",
           "加之各国反垄断力度加强，高通不得不下调收费……",
           "……大城市里生活成本高，加之我的父母身体不好需要照顾，所以回乡是我最好的选择。",
           "这位明星获得了奥斯卡金像奖，主要在于他的坚持与努力，加之他长相帅气，在影片中有着不俗的表现。"],
    say=["Hai điểm cuối là 顶多 và 加之.",
         F(0, "顶多 là phó từ khẩu ngữ, biểu thị giới hạn cao nhất: cùng lắm, nhiều nhất cũng chỉ. Thường mang ý đánh giá thấp. Đi được với số lượng, hoặc với một nhận định."),
         F(1, "Ví dụ từ bài khóa: 然而反垄断案并没有给高通带来什么实质性的影响，顶多就是敲山震虎。 Cùng lắm chỉ là gõ núi dọa hổ."),
         F(2, "这部手机顶多值千八百块钱，卖三千块钱简直是宰人。 Chiếc điện thoại này cùng lắm đáng tám chín trăm đến một nghìn tệ, bán ba nghìn tệ đúng là chặt chém. 千八百 là khoảng một nghìn; 宰人 là chặt chém khách."),
         F(3, "每个人的人生只能自己负责，别人的意见顶多作为参考。 Đời mỗi người chỉ có thể tự mình chịu trách nhiệm, ý kiến của người khác cùng lắm chỉ để tham khảo."),
         F(4, "加之 là liên từ văn viết, nghĩa là thêm vào đó, giống 加上. Dùng để bổ sung một nguyên nhân hay điều kiện nữa, thường đứng đầu vế sau, rồi đến kết quả."),
         F(5, "Ví dụ từ bài khóa: 加之各国反垄断力度加强，高通不得不下调收费。"),
         F(6, "毕业后，我决定回老家工作，大城市里生活成本高，加之我的父母身体不好需要照顾，所以回乡是我最好的选择。 Tốt nghiệp xong, tôi quyết định về quê làm việc: sống ở thành phố lớn tốn kém, thêm vào đó bố mẹ tôi sức khỏe không tốt cần được chăm sóc, nên về quê là lựa chọn tốt nhất."),
         F(7, "这位明星获得了奥斯卡金像奖，主要在于他的坚持与努力，加之他长相帅气，在影片中有着不俗的表现。 Ngôi sao này giành được giải Oscar chủ yếu nhờ sự kiên trì và nỗ lực, thêm vào đó anh ấy điển trai, có màn thể hiện không tầm thường trong phim.")])

# ======================= KẾT HỢP TỪ =======================
add("bullets", chapter="Kết hợp từ", section="Kết hợp từ 词语搭配", title="Kết hợp từ (1): 贴切 · 微妙 · 争端", size=34,
    items=["## 贴切: 用词～ · 表达～ · 形容～ · 描述～",
           "他的文章用词贴切，能准确地表达自己的观点。",
           "## 微妙: ～心理 · 关系～ · 感情～ · 情绪～",
           "作为第三方，官方在这件事情上的表态十分微妙。",
           "## 争端: 产生～ · 解决～ · 消除～ · 国际～",
           "通过和平的手段解决国际争端是最理想的方式。"],
    say=["Tiếp theo là phần kết hợp từ. Bài này có chín từ, thầy chia làm ba slide.",
         F(0, "贴切 đi với 用词, dùng từ; 表达, diễn đạt; 形容, miêu tả; 描述, mô tả. Đều liên quan đến ngôn ngữ."),
         F(1, "Ví dụ: 他的文章用词贴切，能准确地表达自己的观点。 Bài viết của anh ấy dùng từ xác đáng, diễn đạt chính xác quan điểm của mình."),
         F(2, "微妙 đi với 心理, tâm lý; 关系, quan hệ; 感情, tình cảm; 情绪, cảm xúc. Đều là những thứ khó nắm bắt, khó nói."),
         F(3, "Ví dụ: 作为第三方，官方在这件事情上的表态十分微妙。 Là bên thứ ba, cách bày tỏ thái độ của chính quyền về việc này rất tế nhị. 表态 là bày tỏ thái độ."),
         F(4, "争端 đi với 产生, nảy sinh; 解决, giải quyết; 消除, xóa bỏ; và 国际争端, tranh chấp quốc tế."),
         F(5, "Ví dụ: 通过和平的手段解决国际争端是最理想的方式。 Giải quyết tranh chấp quốc tế bằng biện pháp hòa bình là cách lý tưởng nhất.")])

add("bullets", section="Kết hợp từ 词语搭配", title="Kết hợp từ (2): 垄断 · 削弱 · 附加", size=34,
    items=["## 垄断: ～市场 · 打破～ · ～财富 · ～集团 · ～地位",
           "既要保护知识产权，又要打破恶意的专利垄断，是市场监管部门的职责所在。",
           "## 削弱: ～实力 · ～权力 · ～力量 · ～势力",
           "几名主力队员离队后，大大地削弱了球队的实力。",
           "## 附加: ～意义 · ～题 · ～费用 · ～赛",
           "这道附加题实在太难了，网上竟然出现了五花八门的答案。"],
    say=[F(0, "垄断 đi với 市场, độc quyền thị trường; 打破垄断, phá thế độc quyền; 垄断财富, độc chiếm của cải; 垄断集团, tập đoàn độc quyền; 垄断地位, vị trí độc quyền."),
         F(1, "Ví dụ: 既要保护知识产权，又要打破恶意的专利垄断，是市场监管部门的职责所在。 Vừa phải bảo vệ sở hữu trí tuệ, vừa phải phá vỡ thế độc quyền sáng chế ác ý, đó là trách nhiệm của cơ quan quản lý thị trường. Câu này tóm tắt rất hay tinh thần của cả đơn vị."),
         F(2, "削弱 đi với 实力, thực lực; 权力, quyền lực; 力量, sức mạnh; 势力, thế lực. Nhớ đọc là xuēruò."),
         F(3, "Ví dụ: 几名主力队员离队后，大大地削弱了球队的实力。 Sau khi mấy cầu thủ chủ lực rời đội, thực lực của đội bị suy yếu nghiêm trọng."),
         F(4, "附加 đi với 意义, ý nghĩa thêm; 题, câu hỏi phụ; 费用, phụ phí; 赛, trận đấu phụ, trận play-off."),
         F(5, "Ví dụ: 这道附加题实在太难了，网上竟然出现了五花八门的答案。 Câu hỏi phụ này khó quá, trên mạng xuất hiện đủ thứ đáp án muôn hình muôn vẻ.")])

add("bullets", section="Kết hợp từ 词语搭配", title="Kết hợp từ (3): 摆脱 · 覆盖 · 下滑", size=34,
    items=["## 摆脱: ～命运 · ～痛苦 · ～控制 · ～困境",
           "他选择出国留学，就是为了摆脱父母的控制。",
           "## 覆盖: ～范围 · ～成本 · 冰雪～",
           "这项惠民工程将覆盖中国农村的大部分地区。",
           "## 下滑: 成绩～ · 经济～ · 业绩～ · 质量～ · 直线～",
           "不断下滑的成绩令他失去了代表学校参加比赛的资格。"],
    say=[F(0, "摆脱 là thoát khỏi, đi với 命运, số phận; 痛苦, đau khổ; 控制, sự kiểm soát; 困境, cảnh khó khăn. Toàn là những điều không tốt mà ta muốn thoát ra."),
         F(1, "Ví dụ: 他选择出国留学，就是为了摆脱父母的控制。 Anh ấy chọn đi du học chính là để thoát khỏi sự kiểm soát của bố mẹ."),
         F(2, "覆盖 đi với 范围, phạm vi phủ sóng; 成本, bù đắp chi phí; và 冰雪覆盖, băng tuyết bao phủ."),
         F(3, "Ví dụ: 这项惠民工程将覆盖中国农村的大部分地区。 Công trình vì dân này sẽ bao phủ phần lớn vùng nông thôn Trung Quốc. 惠民 là đem lại lợi ích cho dân."),
         F(4, "下滑 đi với 成绩, thành tích; 经济, kinh tế; 业绩, kết quả kinh doanh; 质量, chất lượng; và 直线下滑, tụt dốc thẳng đứng."),
         F(5, "Ví dụ: 不断下滑的成绩令他失去了代表学校参加比赛的资格。 Thành tích liên tục giảm sút khiến cậu ấy mất tư cách đại diện trường đi thi đấu.")])

# ======================= THÀNH NGỮ =======================
IDIOM_SEC = "Thành ngữ 成语和惯用语"
add("bullets", chapter="Thành ngữ (1–8)", section=IDIOM_SEC, title="Thành ngữ (1): 不亦乐乎 · 幸灾乐祸 · 鹬蚌相争 · 一发不可收拾", size=32,
    items=["## 不亦乐乎 bùyìlèhū – vốn là “chẳng phải vui lắm sao?” (《论语》); nay: (làm gì đó) đến cực độ, không ngớt",
           "那些街头小报为了捕捉此案的一些细节而忙得不亦乐乎。",
           "## 幸灾乐祸 xìngzāi-lèhuò – vui sướng trên tai họa của người khác",
           "品质恶劣的人对他人遭遇困境往往幸灾乐祸，甚至落井下石。",
           "## 鹬蚌相争，渔翁得利 – trai cò tranh nhau, ngư ông đắc lợi",
           "如果我们自己内部不团结，结果只能是“鹬蚌相争，渔翁得利”。",
           "## 一发不可收拾 yì fā bù kě shōushi – một khi đã xảy ra thì không cứu vãn nổi",
           "这一带全是木造房屋，使得火势一发不可收拾。"],
    say=["Bây giờ đến phần quan trọng nhất của bài: hai mươi mốt thành ngữ và quán dụng ngữ. Thầy chia làm sáu slide, theo thứ tự xuất hiện trong bài khóa.",
         F(0, "不亦乐乎: câu này xuất phát từ sách Luận Ngữ: 有朋自远方来，不亦乐乎？ Có bạn từ phương xa đến, chẳng phải vui lắm sao? Ngày nay dùng để chỉ mức độ cực cao, thường làm bổ ngữ sau 得: 忙得不亦乐乎, bận tối mắt tối mũi; 看得不亦乐乎, xem say sưa."),
         F(1, "Ví dụ: 那些街头小报为了捕捉此案的一些细节而忙得不亦乐乎。 Đám báo lá cải bận tối mắt để săn từng chi tiết của vụ án này."),
         F(2, "幸灾乐祸: 幸 và 乐 đều là vui, 灾 và 祸 đều là tai họa. Thấy người khác gặp nạn mà vui mừng, chỉ người thiếu thiện ý."),
         F(3, "Ví dụ: 品质恶劣的人对他人遭遇困境往往幸灾乐祸，甚至落井下石。 Kẻ phẩm chất xấu thấy người khác gặp khó thường hả hê, thậm chí ném đá xuống giếng."),
         F(4, "鹬蚌相争，渔翁得利: con cò và con trai giằng co nhau không ai chịu buông, ông câu đi qua bắt được cả hai. Ví với hai bên tranh chấp, để bên thứ ba hưởng lợi. Tiếng Việt có câu giống hệt: trai cò tranh nhau, ngư ông đắc lợi."),
         F(5, "Ví dụ: 如果我们自己内部不团结，结果只能是鹬蚌相争，渔翁得利。 Nếu nội bộ chúng ta không đoàn kết, kết quả chỉ có thể là trai cò tranh nhau, ngư ông đắc lợi."),
         F(6, "一发不可收拾: sự việc một khi đã bùng phát thì không thu dọn, cứu vãn nổi, ngày càng tệ hơn. Chữ 发 là phát ra, bùng lên."),
         F(7, "Ví dụ: 这一带全是木造房屋，使得火势一发不可收拾。 Vùng này toàn nhà gỗ, khiến ngọn lửa một khi bùng lên thì không sao dập nổi.")])

add("bullets", section=IDIOM_SEC, title="Thành ngữ (2): 落井下石 · 左右为难 · 有恃无恐 · 苦不堪言", size=32,
    items=["## 落井下石 luòjǐng-xiàshí – ném đá xuống giếng: thừa lúc người gặp nạn mà hãm hại",
           "他最讨厌那种嫌贫爱富、落井下石的人。",
           "## 左右为难 zuǒyòu-wéinán – tiến thoái lưỡng nan, làm thế nào cũng khó",
           "他们俩都来找我拉票，令我左右为难。",
           "## 有恃无恐 yǒushì-wúkǒng – có chỗ dựa nên chẳng sợ gì, không kiêng nể",
           "忍气吞声，只会助长犯罪分子的嚣张气焰，使他们有恃无恐。",
           "## 苦不堪言 kǔbùkānyán – khổ không kể xiết",
           "老人患病多年，终日卧床，苦不堪言。"],
    say=[F(0, "落井下石: thấy người sắp rơi xuống giếng không cứu, lại còn đẩy xuống rồi ném đá theo. Ví với việc thừa lúc người khác gặp nạn mà hãm hại. Tiếng Việt cũng nói ném đá xuống giếng."),
         F(1, "Ví dụ: 他最讨厌那种嫌贫爱富、落井下石的人。 Anh ấy ghét nhất loại người khinh nghèo trọng giàu, ném đá xuống giếng. 嫌贫爱富 là chê nghèo ham giàu."),
         F(2, "左右为难: bên trái cũng không được, bên phải cũng không xong, làm thế nào cũng khó. Chữ 为 đọc wéi."),
         F(3, "Ví dụ: 他们俩都来找我拉票，令我左右为难。 Cả hai người họ đều đến vận động tôi bỏ phiếu, khiến tôi khó xử. 拉票 là vận động phiếu bầu."),
         F(4, "有恃无恐: 恃 là dựa vào, 恐 là sợ. Vì có chỗ dựa nên không hề sợ hãi, không kiêng nể gì, thường mang nghĩa chê."),
         F(5, "Ví dụ: 忍气吞声，只会助长犯罪分子的嚣张气焰，使他们有恃无恐。 Nhịn nhục chỉ làm tăng khí thế hung hăng của bọn tội phạm, khiến chúng chẳng sợ gì. 助长 là tiếp tay, làm tăng thêm."),
         F(6, "苦不堪言: 堪 là có thể. Khổ đến mức không thể nói thành lời, tức khổ không kể xiết."),
         F(7, "Ví dụ: 老人患病多年，终日卧床，苦不堪言。 Ông cụ bị bệnh nhiều năm, suốt ngày nằm liệt giường, khổ không kể xiết.")])

add("bullets", chapter="Thành ngữ (9–15)", section=IDIOM_SEC, title="Thành ngữ (3): 坐收渔利 · 看人下菜碟儿 · 义愤填膺 · 忍无可忍", size=32,
    items=["## 坐收渔利 zuòshōu-yúlì – ngồi không hưởng lợi từ mâu thuẫn của người khác",
           "他静静地观察这两家商场的商战，自己好坐收渔利。",
           "## 看人下菜碟儿 kàn rén xià càidiér – nhìn người mà đối xử (ý chê)",
           "不要看人下菜碟。真正友善的人在任何时候对任何人都会给予足够的尊重。",
           "## 义愤填膺 yìfèn-tiányīng – căm phẫn đầy lồng ngực (vì chính nghĩa)",
           "对于歹徒残暴的行径，每个人都义愤填膺。",
           "## 忍无可忍 rěnwúkěrěn – không thể nhịn được nữa",
           "对方放肆的行为让他忍无可忍，最终破口大骂起来。"],
    say=[F(0, "坐收渔利: ngồi một chỗ mà hưởng lợi của ngư ông, tức lợi dụng mâu thuẫn giữa người khác để dễ dàng kiếm lợi. Cũng nói 坐收渔人之利. Gốc từ câu trai cò tranh nhau vừa học."),
         F(1, "Ví dụ: 他静静地观察这两家商场的商战，自己好坐收渔利。 Anh ta lặng lẽ quan sát cuộc chiến thương mại giữa hai trung tâm thương mại, để mình ngồi không hưởng lợi."),
         F(2, "看人下菜碟儿: nhìn khách mà dọn món: khách sang thì món ngon, khách thường thì món xoàng. Chỉ việc đối xử khác nhau tùy người, thường mang nghĩa chê. Tiếng Việt có thể nói trông mặt mà bắt hình dong, hay nâng người này hạ người kia."),
         F(3, "Ví dụ: 不要看人下菜碟。真正友善的人在任何时候对任何人都会给予足够的尊重。 Đừng nhìn người mà đối xử. Người thật lòng thân thiện thì lúc nào, với ai cũng đủ tôn trọng."),
         F(4, "义愤填膺: 义愤 là sự phẫn nộ vì chính nghĩa, 膺 là ngực. Lòng căm phẫn chính nghĩa chất đầy lồng ngực."),
         F(5, "Ví dụ: 对于歹徒残暴的行径，每个人都义愤填膺。 Trước hành vi tàn bạo của bọn côn đồ, ai cũng căm phẫn. 歹徒 là kẻ côn đồ, tội phạm."),
         F(6, "忍无可忍: đã nhịn đến mức không thể nhịn thêm được nữa. Trong bài, 义愤填膺 và 忍无可忍 đi liền nhau, nhấn mạnh sự phẫn nộ của các hãng điện thoại Trung Quốc."),
         F(7, "Ví dụ: 对方放肆的行为让他忍无可忍，最终破口大骂起来。 Hành vi xấc xược của đối phương khiến anh ấy không nhịn nổi, cuối cùng chửi ầm lên. 放肆 là xấc xược; 破口大骂 là chửi ầm lên.")])

add("bullets", section=IDIOM_SEC, title="Thành ngữ (4): 反戈一击 · 无与伦比 · 身经百战", size=33,
    items=["## 反戈一击 fǎngē-yìjī – quay giáo đánh lại (phe mình hoặc kẻ áp bức mình)",
           "他做梦也没有想到，他手下的人居然反戈一击，揭发了他。",
           "他加盟了竞争对手的公司，对老东家反戈一击。",
           "## 无与伦比 wúyǔlúnbǐ – không gì sánh bằng, tuyệt vời nhất",
           "中国的民间刺绣，构想新奇，工艺精美，可谓无与伦比。",
           "## 身经百战 shēnjīng-bǎizhàn – thân trải trăm trận, dày dạn kinh nghiệm",
           "无论公司遇到什么突发状况，身经百战的刘总都能化险为夷。"],
    say=[F(0, "反戈一击: 戈 là cây giáo. Quay ngọn giáo lại đánh một đòn, ví với việc quay sang chống lại phe mình vốn thuộc về hay ủng hộ. Trong bài, các hãng điện thoại vốn là khách hàng của Qualcomm, nay quay lại kiện nó."),
         F(1, "Ví dụ: 他做梦也没有想到，他手下的人居然反戈一击，揭发了他。 Hắn nằm mơ cũng không ngờ, thuộc hạ của mình lại quay giáo tố giác hắn. 揭发 là tố giác."),
         F(2, "Và: 他加盟了竞争对手的公司，对老东家反戈一击。 Anh ta về đầu quân cho công ty đối thủ, quay lại đánh chủ cũ. 老东家 là chủ cũ, công ty cũ."),
         F(3, "无与伦比: 伦比 là sánh bằng, cùng loại. Không có gì có thể sánh được, tốt đến tột bậc. Thường dùng để khen."),
         F(4, "Ví dụ: 中国的民间刺绣，构想新奇，工艺精美，可谓无与伦比。 Tranh thêu dân gian Trung Quốc có ý tưởng mới lạ, tay nghề tinh xảo, có thể nói là không gì sánh bằng. 可谓 là có thể nói là."),
         F(5, "身经百战: bản thân đã trải qua trăm trận đánh, chỉ người dày dạn rèn luyện, giàu kinh nghiệm thực tế. Tiếng Việt cũng nói trăm trận trăm thắng, hay dày dạn trận mạc."),
         F(6, "Ví dụ: 无论公司遇到什么突发状况，身经百战的刘总都能化险为夷。 Dù công ty gặp tình huống bất ngờ nào, giám đốc Lưu dày dạn kinh nghiệm đều có thể biến nguy thành an. 化险为夷 là chuyển nguy thành an.")])

add("bullets", chapter="Thành ngữ (16–21)", section=IDIOM_SEC, title="Thành ngữ (5): 不容小觑 · 半壁江山 · 两害相权取其轻", size=33,
    items=["## 不容小觑 bùróng xiǎoqù – không thể xem thường",
           "在人人都有麦克风的网络时代，网络作为舆论的公共场所，其影响力不容小觑。",
           "## 半壁江山 bànbì-jiāngshān – nửa giang sơn: một nửa, một phần lớn",
           "举重、跳水和乒乓球是中国的传统优势项目，几乎占据了中国奥运奖牌总数的半壁江山。",
           "## 两害相权取其轻 – cân nhắc hai cái hại thì chọn cái nhẹ hơn",
           "道路交通中的“车让人”是出于“两害相权取其轻”的考虑。",
           "手术治疗和药物治疗都有副作用，具体的治疗方案应该遵循“两害相权取其轻”的原则。"],
    say=[F(0, "不容小觑: 容 là cho phép, 觑 đọc qù, là nhìn. Không cho phép coi nhẹ, tức là không thể xem thường. Thường làm vị ngữ, chủ ngữ là thực lực, sức ảnh hưởng, vai trò."),
         F(1, "Ví dụ: 在人人都有麦克风的网络时代，网络作为舆论的公共场所，其影响力不容小觑。 Trong thời đại mạng ai cũng có micro trong tay, mạng internet là nơi công cộng của dư luận, sức ảnh hưởng của nó không thể xem thường."),
         F(2, "半壁江山: nửa giang sơn, vốn chỉ một nửa hay một phần đất nước. Nay hay dùng để chỉ một nửa, một phần lớn thị phần, thành tích. Động từ đi kèm là 占据 hay 占."),
         F(3, "Ví dụ: 举重、跳水和乒乓球是中国的传统优势项目，几乎占据了中国奥运奖牌总数的半壁江山。 Cử tạ, nhảy cầu và bóng bàn là các môn thế mạnh truyền thống của Trung Quốc, chiếm gần một nửa tổng số huy chương Olympic của Trung Quốc."),
         F(4, "两害相权取其轻: 权 là cân nhắc, như trong 权衡. So sánh hai điều có hại, chọn điều ít hại hơn. Câu này rất hay dùng khi phân tích một quyết định khó."),
         F(5, "Ví dụ: 道路交通中的车让人是出于两害相权取其轻的考虑。 Trong giao thông, xe nhường người đi bộ là xuất phát từ cân nhắc chọn cái hại nhẹ hơn."),
         F(6, "Và: 手术治疗和药物治疗都有副作用，具体的治疗方案应该遵循两害相权取其轻的原则。 Phẫu thuật và dùng thuốc đều có tác dụng phụ, phác đồ cụ thể nên tuân theo nguyên tắc chọn cái hại nhẹ hơn.")])

add("bullets", section=IDIOM_SEC, title="Thành ngữ (6): 敲山震虎 · 时过境迁 · 一家独大", size=33,
    items=["## 敲山震虎 qiāoshān-zhènhǔ – gõ núi dọa hổ: răn đe, cảnh cáo",
           "警方这一招是敲山震虎，使歹徒们露出了马脚。",
           "## 时过境迁 shíguò-jìngqiān – thời gian trôi qua, hoàn cảnh đổi thay",
           "时过境迁，20年后的家乡已变得富裕了，我为此感到无比欣慰。",
           "父辈的一些成功经验，已时过境迁，不可复制，我们要另辟蹊径。",
           "## 一家独大 yìjiā-dúdà – một nhà độc chiếm, không ai sánh được",
           "市场经济体制下，资本在任何领域一家独大对消费者都绝对不是好事。"],
    say=[F(0, "敲山震虎: gõ vào núi để làm con hổ kinh sợ. Ví với việc răn đe, cảnh cáo đối phương; hoặc ép đối phương đang ẩn nấp phải hành động mà lộ mặt. Tiếng Việt có câu gần nghĩa: đánh rắn động cỏ, hay giết gà dọa khỉ."),
         F(1, "Ví dụ: 警方这一招是敲山震虎，使歹徒们露出了马脚。 Chiêu này của cảnh sát là gõ núi dọa hổ, khiến bọn tội phạm lộ đuôi. 露出马脚 là lộ chân ngựa, tức lòi đuôi."),
         F(2, "时过境迁: thời gian đã qua, cảnh ngộ cũng thay đổi theo. Thường đứng đầu câu."),
         F(3, "Ví dụ: 时过境迁，二十年后的家乡已变得富裕了，我为此感到无比欣慰。 Thời thế đổi thay, hai mươi năm sau quê hương đã trở nên giàu có, tôi vô cùng vui mừng.",
           cap="Ví dụ: 时过境迁，20年后的家乡已变得富裕了，我为此感到无比欣慰。 Thời thế đổi thay, 20 năm sau quê hương đã trở nên giàu có, tôi vô cùng vui mừng."),
         F(4, "Và: 父辈的一些成功经验，已时过境迁，不可复制，我们要另辟蹊径。 Một số kinh nghiệm thành công của thế hệ cha ông đã lỗi thời, không thể sao chép, chúng ta phải mở lối đi riêng. 另辟蹊径 là mở ra con đường khác."),
         F(5, "一家独大: một nhà lớn nhất, ở vị trí độc quyền, không ai sánh được. Trong bài, 一家独大 đối lập với 百家争鸣."),
         F(6, "Ví dụ: 市场经济体制下，资本在任何领域一家独大对消费者都绝对不是好事。 Trong cơ chế kinh tế thị trường, tư bản độc chiếm ở bất kỳ lĩnh vực nào cũng tuyệt đối không phải là điều tốt cho người tiêu dùng.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 课后练习", title="Bài tập 1: Chọn thành ngữ điền vào chỗ trống (1)", reveal=True, size=33,
    items=["## 百家争鸣 · 毋庸置疑 · 义愤填膺 · 反戈一击 · 无与伦比 · 一家独大 · 有恃无恐 · 不容小觑",
           "(1) 为了促进学术进步，评论界必须___，不能强求统一。",
           "Đáp án: 百家争鸣",
           "(2) 敦煌壁画的美可谓___，让人流连忘返。",
           "Đáp án: 无与伦比",
           "(3) 因为长期___，缺乏竞争，创新能力急剧下降，因此产品迭代速度也大幅降低。",
           "Đáp án: 一家独大",
           "(4) 侵略者的暴行，令民众___。",
           "Đáp án: 义愤填膺"],
    say=["Bây giờ chúng ta sang phần luyện tập của sách. Bài tập một: chọn thành ngữ điền vào chỗ trống. Có tám thành ngữ: 百家争鸣，毋庸置疑，义愤填膺，反戈一击，无与伦比，一家独大，有恃无恐，不容小觑.",
         F(1, "Câu một: 为了促进学术进步，评论界必须什么，不能强求统一。 Để thúc đẩy học thuật tiến bộ, giới bình luận phải thế nào, không thể ép phải thống nhất. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 百家争鸣. Trăm nhà đua tiếng, đối lập với 强求统一, ép buộc thống nhất."),
         F(3, "Câu hai: 敦煌壁画的美可谓什么，让人流连忘返。 Vẻ đẹp của bích họa Đôn Hoàng có thể nói là thế nào, khiến người ta lưu luyến quên về."),
         F(4, "Đáp án: 无与伦比. Sau 可谓 là một lời khen ở mức cao nhất."),
         F(5, "Câu ba: 因为长期什么，缺乏竞争，创新能力急剧下降，因此产品迭代速度也大幅降低。 Vì lâu dài thế nào, thiếu cạnh tranh, năng lực đổi mới giảm mạnh, tốc độ ra sản phẩm mới cũng chậm hẳn. 迭代 là thay thế thế hệ sản phẩm."),
         F(6, "Đáp án: 一家独大. Một nhà độc chiếm thì thiếu cạnh tranh, chính là bài học của Qualcomm."),
         F(7, "Câu bốn: 侵略者的暴行，令民众什么。 Tội ác của kẻ xâm lược khiến dân chúng thế nào?"),
         F(8, "Đáp án: 义愤填膺. Căm phẫn đầy lồng ngực.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 1: Chọn thành ngữ điền vào chỗ trống (2)", reveal=True, size=33,
    items=["(5) 天赋影响到个人所能达到的高度，这点___，但它并不能完全左右一个人的命运。",
           "Đáp án: 毋庸置疑",
           "(6) 现代社会，广告在树立品牌形象和推销品牌方面的作用___。",
           "Đáp án: 不容小觑",
           "(7) 较低的赔偿额度助长了这种不正当竞争行为，让商家变得越发___。",
           "Đáp án: 有恃无恐",
           "(8) 他一看情况不好，马上见风使舵，___。",
           "Đáp án: 反戈一击"],
    say=[F(0, "Câu năm: 天赋影响到个人所能达到的高度，这点什么，但它并不能完全左右一个人的命运。 Thiên phú ảnh hưởng tới độ cao mà mỗi người có thể đạt được, điều này thế nào, nhưng nó không thể hoàn toàn quyết định số phận một người."),
         F(1, "Đáp án: 毋庸置疑, không cần nghi ngờ. Từ này có trong bài khóa: 但毋庸置疑，高通的初衷可不是想把苹果告黄。"),
         F(2, "Câu sáu: 现代社会，广告在树立品牌形象和推销品牌方面的作用什么。 Trong xã hội hiện đại, vai trò của quảng cáo trong việc xây dựng hình ảnh và quảng bá thương hiệu thế nào?"),
         F(3, "Đáp án: 不容小觑. 作用不容小觑, vai trò không thể xem thường."),
         F(4, "Câu bảy: 较低的赔偿额度助长了这种不正当竞争行为，让商家变得越发什么。 Mức bồi thường thấp đã tiếp tay cho hành vi cạnh tranh không lành mạnh này, khiến các nhà buôn ngày càng thế nào?"),
         F(5, "Đáp án: 有恃无恐. Bồi thường thấp thì vi phạm chẳng sợ gì, càng thêm không kiêng nể."),
         F(6, "Câu tám: 他一看情况不好，马上见风使舵，什么。 Hắn vừa thấy tình hình không ổn, lập tức gió chiều nào che chiều ấy, rồi làm gì? 见风使舵 là xem gió bẻ lái."),
         F(7, "Đáp án: 反戈一击. Thấy phe mình sắp thua thì quay giáo đánh lại phe mình.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn từ thích hợp nhất (1)", reveal=True, size=33,
    items=["(1) 当两个好朋友同时爱上一个人的时候，三个人之间的关系顿时变得（  ）起来。 A.巧妙 B.绝妙 C.微妙 D.细微",
           "Đáp án: C 微妙 – quan hệ trở nên tế nhị",
           "(2) 面对不景气的市场，企业大幅（  ）了研发经费。 A.削减 B.剥削 C.削弱 D.减弱",
           "Đáp án: A 削减 – cắt giảm (kinh phí)",
           "(3) 解决（  ）最好的方式就是双方先放下成见，加强沟通，求同存异。 A.事端 B.争斗 C.争议 D.争端",
           "Đáp án: D 争端 – 解决争端"],
    say=["Bài tập hai: chọn từ thích hợp nhất.",
         F(0, "Câu một: 当两个好朋友同时爱上一个人的时候，三个人之间的关系顿时变得什么起来。 Khi hai người bạn thân cùng yêu một người, quan hệ giữa ba người lập tức trở nên thế nào. A, 巧妙; B, 绝妙; C, 微妙; D, 细微."),
         F(1, "Đáp án: C, 微妙, tế nhị, khó nói. 巧妙 là khéo léo, 绝妙 là tuyệt diệu, đều là lời khen; 细微 là nhỏ nhặt, rất nhỏ."),
         F(2, "Câu hai: 面对不景气的市场，企业大幅什么了研发经费。 Trước thị trường ảm đạm, doanh nghiệp đã mạnh tay làm gì kinh phí nghiên cứu. A, 削减; B, 剥削; C, 削弱; D, 减弱."),
         F(3, "Đáp án: A, 削减, cắt giảm, dùng cho tiền bạc, số lượng: 削减经费，削减开支. 削弱 là làm suy yếu sức mạnh, thực lực; 剥削 là bóc lột; 减弱 là tự yếu đi, không có tân ngữ là kinh phí."),
         F(4, "Câu ba: 解决什么最好的方式就是双方先放下成见，加强沟通，求同存异。 Cách tốt nhất để giải quyết cái gì là hai bên gác lại định kiến, tăng cường giao tiếp, tìm điểm chung, gác điểm khác biệt. A, 事端; B, 争斗; C, 争议; D, 争端."),
         F(5, "Đáp án: D, 争端. 解决争端 là kết hợp cố định ta vừa học. 事端 là sự cố, thường nói 挑起事端, gây sự; 争斗 là đánh nhau. 求同存异 là tìm điểm chung, gác lại khác biệt.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn từ thích hợp nhất (2)", reveal=True, size=33,
    items=["(4) （  ）粉不同于一般的粉丝，他们关注某个明星不是因为喜欢，而是为了挑刺儿。 A.黄 B.红 C.绿 D.黑",
           "Đáp án: D 黑 – 黑粉 anti-fan",
           "(5) 大热天三天两头的停电，大家（  ）。 A.半壁江山 B.苦不堪言 C.有恃无恐 D.左右为难",
           "Đáp án: B 苦不堪言",
           "(6) 老师（  ）我们认真复习，争取在期末考试中取得好成绩。 A.责令 B.督促 C.命令 D.责怪",
           "Đáp án: B 督促 – đôn đốc, nhắc nhở"],
    say=[F(0, "Câu bốn: 什么粉不同于一般的粉丝，他们关注某个明星不是因为喜欢，而是为了挑刺儿。 Loại fan nào khác với fan bình thường: họ theo dõi một ngôi sao không phải vì thích, mà là để bới lỗi. A, 黄; B, 红; C, 绿; D, 黑."),
         F(1, "Đáp án: D, 黑粉, anti-fan. Chữ 黑 trong từ lóng mạng là bôi đen, chê bai, như 被黑 ở bài năm chấm ba. 挑刺儿 là bới lông tìm vết."),
         F(2, "Câu năm: 大热天三天两头的停电，大家什么。 Trời nóng như đổ lửa mà cứ dăm bữa nửa tháng lại mất điện, mọi người thế nào. A, 半壁江山; B, 苦不堪言; C, 有恃无恐; D, 左右为难."),
         F(3, "Đáp án: B, 苦不堪言, khổ không kể xiết. 三天两头 là thường xuyên, dăm bữa nửa tháng."),
         F(4, "Câu sáu: 老师什么我们认真复习，争取在期末考试中取得好成绩。 Thầy giáo làm gì chúng tôi ôn tập chăm chỉ, phấn đấu đạt kết quả tốt trong kỳ thi cuối kỳ. A, 责令; B, 督促; C, 命令; D, 责怪."),
         F(5, "Đáp án: B, 督促, đôn đốc, nhắc nhở. 责令 là cơ quan có thẩm quyền ra lệnh bắt buộc, như 责令整改 trong bài khóa, quá nặng với thầy trò; 命令 là ra lệnh; 责怪 là trách móc.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ ngữ, mẫu câu cho sẵn trả lời câu hỏi (1)", reveal=True, size=32,
    items=["(1) 网友如何看待高通和苹果的“口水战”？（与其……，不如……）",
           "Đáp án gợi ý: 网友对这件事的心态，与其说是“幸灾乐祸”，不如说是“鹬蚌相争，渔翁得利”更贴切，大家像吃瓜群众一样看得不亦乐乎。",
           "(2) 高通的霸王条款对下游企业有何影响？（坐收渔利，无形之中……）",
           "Đáp án gợi ý: 高通按整机售价的5%收取专利使用费，坐收渔利，让下游企业苦不堪言；“专利反向授权”也在无形之中削弱了其他企业的研发能力和研发动力。"],
    say=["Bài tập ba: dùng từ ngữ và mẫu câu cho sẵn để trả lời câu hỏi về bài khóa. Thầy đưa ra đáp án gợi ý.",
         F(0, "Câu một: 网友如何看待高通和苹果的口水战？ Cư dân mạng nhìn nhận cuộc khẩu chiến giữa Qualcomm và Apple thế nào? Dùng 与其不如."),
         F(1, "Gợi ý: 网友对这件事的心态，与其说是幸灾乐祸，不如说是鹬蚌相争，渔翁得利更贴切，大家像吃瓜群众一样看得不亦乐乎。 Tâm lý cư dân mạng, nói là hả hê chẳng bằng nói là trai cò tranh nhau, ngư ông đắc lợi; mọi người hóng chuyện say sưa."),
         F(2, "Câu hai: 高通的霸王条款对下游企业有何影响？ Điều khoản bá đạo của Qualcomm ảnh hưởng thế nào đến doanh nghiệp hạ nguồn? Dùng 坐收渔利 và 无形之中. 有何 là có gì, văn viết của 有什么."),
         F(3, "Gợi ý: 高通按整机售价的百分之五收取专利使用费，坐收渔利，让下游企业苦不堪言；专利反向授权也在无形之中削弱了其他企业的研发能力和研发动力。 Qualcomm thu phí năm phần trăm giá cả chiếc máy, ngồi không hưởng lợi, khiến doanh nghiệp hạ nguồn khổ sở; việc trao quyền ngược cũng vô hình trung làm suy yếu năng lực và động lực nghiên cứu của họ.",
           cap="Gợi ý: 高通按整机售价的5%收取专利使用费，坐收渔利，让下游企业苦不堪言；“专利反向授权”也在无形之中削弱了其他企业的研发能力和研发动力。")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ ngữ, mẫu câu cho sẵn trả lời câu hỏi (2)", reveal=True, size=32,
    items=["(3) 反垄断案对高通有何影响？（乖乖……，顶多……，摆脱……命运）",
           "Đáp án gợi ý: 高通乖乖认罚，交了60.88亿元罚款并全面整改，但反垄断案顶多是敲山震虎，没有带来实质性的影响，小企业仍摆脱不了“被欺负”的命运。",
           "(4) 未来高通将面临何种挑战？（一家独大，百家争鸣，加之……）",
           "Đáp án gợi ý: 手机芯片产业已经从高通一家独大向百家争鸣发展，芯片销售渠道越来越窄；加之各国反垄断力度加强，高通在5G时代将面临更多挑战。"],
    say=[F(0, "Câu ba: 反垄断案对高通有何影响？ Vụ án chống độc quyền ảnh hưởng thế nào đến Qualcomm? Dùng 乖乖，顶多, và 摆脱命运."),
         F(1, "Gợi ý: 高通乖乖认罚，交了六十点八八亿元罚款并全面整改，但反垄断案顶多是敲山震虎，没有带来实质性的影响，小企业仍摆脱不了被欺负的命运。 Qualcomm ngoan ngoãn chịu phạt hơn sáu tỷ tệ và khắc phục toàn diện, nhưng vụ án cùng lắm chỉ là gõ núi dọa hổ, không có ảnh hưởng thực chất, doanh nghiệp nhỏ vẫn không thoát khỏi số phận bị bắt nạt.",
           cap="Gợi ý: 高通乖乖认罚，交了60.88亿元罚款并全面整改，但反垄断案顶多是敲山震虎，没有带来实质性的影响，小企业仍摆脱不了“被欺负”的命运。"),
         F(2, "Câu bốn: 未来高通将面临何种挑战？ Trong tương lai Qualcomm sẽ đối mặt với thách thức nào? Dùng 一家独大，百家争鸣, và 加之."),
         F(3, "Gợi ý: 手机芯片产业已经从高通一家独大向百家争鸣发展，芯片销售渠道越来越窄；加之各国反垄断力度加强，高通在5G时代将面临更多挑战。 Ngành chip điện thoại đã chuyển từ một nhà độc chiếm sang trăm nhà đua tiếng, kênh bán chip ngày càng hẹp; thêm vào đó các nước tăng cường chống độc quyền, Qualcomm sẽ gặp nhiều thách thức hơn trong thời đại năm G.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Chọn từ ngữ điền vào đoạn văn", reveal=True, size=32,
    items=["## 毋庸置疑 · 百家争鸣 · 苦不堪言 · 垄断 · 义愤填膺 · 不亦乐乎 · 两害相权取其轻 · 争端 · 防不胜防",
           "直到19世纪，科技才进入了首个___的时代。专利制度的出现___是其中极为重要的一个动因。当然，专利权并非不存在争议。有网友___地指出：授予发明人以专利权这种排他性的独占权就是名正言顺的___，高昂的专利费让一些下游企业___。但也有人认为，与漫天山寨产品相比，___，不应该因噎废食，而且虽然围绕专利保护一直___不断，但这从另一方面也提高了人们的法律意识，___？",
           "Đáp án: 百家争鸣 · 毋庸置疑 · 义愤填膺 · 垄断 · 苦不堪言 · 两害相权取其轻 · 争端 · 不亦乐乎 (thừa: 防不胜防)"],
    say=["Bài tập bốn: chọn từ ngữ điền vào đoạn văn. Có chín lựa chọn cho tám chỗ trống, tức là thừa một từ: 毋庸置疑，百家争鸣，苦不堪言，垄断，义愤填膺，不亦乐乎，两害相权取其轻，争端，防不胜防.",
         F(1, "直到十九世纪，科技才进入了首个什么的时代。专利制度的出现什么是其中极为重要的一个动因。当然，专利权并非不存在争议。有网友什么地指出：授予发明人以专利权这种排他性的独占权就是名正言顺的什么，高昂的专利费让一些下游企业什么。但也有人认为，与漫天山寨产品相比，什么，不应该因噎废食，而且虽然围绕专利保护一直什么不断，但这从另一方面也提高了人们的法律意识，什么？ Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 首个百家争鸣的时代；专利制度的出现毋庸置疑是重要动因；有网友义愤填膺地指出；名正言顺的垄断；让下游企业苦不堪言；两害相权取其轻；争端不断；最后一句是不亦乐乎？ Từ thừa là 防不胜防, phòng không xuể."),
         F(2, "Hai chỗ thú vị: thứ nhất, 两害相权取其轻: so với hàng nhái tràn lan, độc quyền sáng chế là cái hại nhẹ hơn, không nên vì nghẹn mà bỏ ăn, 因噎废食. Thứ hai, câu cuối dùng 不亦乐乎 theo nghĩa gốc trong Luận Ngữ: chẳng phải đáng mừng lắm sao? Đoạn văn này tóm tắt rất hay hai mặt của chế độ bằng sáng chế.")])

add("bullets", chapter="Liên hệ: chip, bản quyền & luật cạnh tranh", section="Thảo luận 讨论", title="Liên hệ Việt Nam: chip, bản quyền và chống độc quyền", size=33,
    items=["Thành ngữ giống tiếng Việt: 鹬蚌相争，渔翁得利 = trai cò tranh nhau, ngư ông đắc lợi · 落井下石 = ném đá xuống giếng · 身经百战 = trăm trận dày dạn",
           "Điện thoại “made in Vietnam” (Bphone, VinSmart…) cũng phải trả phí bản quyền sáng chế cho các hãng nắm công nghệ như Qualcomm",
           "Luật Cạnh tranh Việt Nam cấm lạm dụng vị trí thống lĩnh, vị trí độc quyền ≈ 反垄断法",
           "Câu hỏi: 你觉得专利费是保护创新，还是阻碍创新？"],
    say=["Trước khi tổng kết, chúng ta cùng liên hệ với Việt Nam.",
         F(0, "Rất nhiều thành ngữ trong bài có câu tương ứng gần như y hệt trong tiếng Việt: 鹬蚌相争，渔翁得利 là trai cò tranh nhau, ngư ông đắc lợi; 落井下石 là ném đá xuống giếng; 身经百战 là trăm trận dày dạn. Đây là lợi thế rất lớn của người Việt khi học thành ngữ tiếng Trung."),
         F(1, "Việt Nam cũng từng có những dòng điện thoại tự sản xuất, như Bphone, VinSmart. Muốn dùng công nghệ ba G, bốn G, năm G thì các hãng này cũng phải trả phí bản quyền sáng chế cho những công ty nắm công nghệ như Qualcomm. Vì vậy, làm chủ công nghệ lõi là con đường duy nhất để không bị phụ thuộc."),
         F(2, "Việt Nam có Luật Cạnh tranh, cấm doanh nghiệp lạm dụng vị trí thống lĩnh thị trường hay vị trí độc quyền, ví dụ áp đặt giá bất hợp lý, phân biệt đối xử, ép mua kèm, rất giống những hành vi của Qualcomm trong bài. Đó chính là 反垄断法, luật chống độc quyền."),
         F(3, "Câu hỏi cho các bạn: 你觉得专利费是保护创新，还是阻碍创新？ Bạn cho rằng phí bản quyền sáng chế bảo vệ đổi mới sáng tạo hay cản trở đổi mới sáng tạo? Hãy thử trả lời bằng tiếng Trung, dùng 与其不如, 究其原因, 两害相权取其轻 nhé.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 8.2", size=32,
    items=["Từ vựng trọng tâm: 江山 · 口水战 · 刷屏 · 贴切 · 微妙 · 初衷 · 发难 · 争端 · 芯片 · 巨擘 · 垄断 · 霸王条款 · 渔利 · 削弱 · 搭售 · 立案 · 监管 · 责令 · 整改 · 覆盖 · 格局",
           "Mẫu câu: 与其……不如…… · 究其原因 · 戏称……为…… · （在）无形之中 · 顶多 · 加之",
           "Thành ngữ: 不亦乐乎 · 幸灾乐祸 · 鹬蚌相争，渔翁得利 · 一发不可收拾 · 落井下石 · 左右为难 · 有恃无恐 · 苦不堪言 · 坐收渔利 · 看人下菜碟儿 · 义愤填膺 · 忍无可忍 · 反戈一击 · 无与伦比 · 身经百战 · 不容小觑 · 半壁江山 · 两害相权取其轻 · 敲山震虎 · 时过境迁 · 一家独大",
           "## Bài tập về nhà",
           "Viết đoạn văn khoảng 300 chữ: 专利保护的利与弊 – dùng ít nhất 3 mẫu câu và 5 thành ngữ của bài"],
    say=["Chúng ta cùng tổng kết bài tám chấm hai.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 江山，口水战，刷屏，贴切，微妙，初衷，发难，争端，芯片，巨擘，垄断，霸王条款，渔利，削弱，搭售，立案，监管，责令，整改，覆盖，格局. Nhớ cách đọc 发难, 巨擘, 削弱, và từ dễ nhầm 微妙 nhé."),
         F(1, "Về mẫu câu: 与其不如 là thay vì… chẳng bằng…; 究其原因 là xét đến nguyên nhân; 戏称为 là gọi đùa là; 无形之中 là vô hình trung; 顶多 là cùng lắm; và 加之 là thêm vào đó."),
         F(2, "Về thành ngữ, hai mươi mốt thành ngữ, nhiều nhất trong giáo trình. Hãy ôn theo cặp: 义愤填膺 đi với 忍无可忍; 幸灾乐祸 đi với 落井下石; 一家独大 đối lập với 百家争鸣; 鹬蚌相争，渔翁得利 đi với 坐收渔利."),
         F(4, "Bài tập về nhà: hãy viết một đoạn văn khoảng ba trăm chữ với đề 专利保护的利与弊, lợi và hại của việc bảo hộ sáng chế. Hãy dùng ít nhất ba mẫu câu và năm thành ngữ của bài, như 与其不如，究其原因，两害相权取其轻，一家独大，不容小觑."),
         {"t": "Cảm ơn các bạn đã theo dõi bài giảng. Bài sau, bài tám chấm ba, là bài cuối cùng của giáo trình: 善终也是一种权利, Ra đi thanh thản cũng là một quyền.",
          "cap": "Cảm ơn các bạn đã theo dõi bài giảng. Bài sau, bài 8.3, là bài cuối cùng của giáo trình: 善终也是一种权利, Ra đi thanh thản cũng là một quyền."},
         "Từ chuyện kiện tụng thương mại, chúng ta sẽ bàn về một vấn đề pháp luật rất nhân văn: quyền của người bệnh được lựa chọn cách ra đi, chết một cách có tôn nghiêm, qua câu chuyện của nhà văn Quỳnh Dao và nhà văn Ba Kim. Hẹn gặp lại các bạn. Chúc các bạn học tốt!"])

lesson = {
    "title": "顶石中文 – Bài 8.2: 高通：打官司打出的“江山” (Qualcomm: “giang sơn” dựng nên từ kiện tụng)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"不亦乐乎": "不亦勒乎",      # bù yì lè hū
                    "削弱": "靴弱",              # xuēruò
                    "削减": "靴减",              # xuējiǎn
                    "剥削": "剥靴",              # bōxuē
                    "利润率": "利润律",          # lìrùnlǜ
                    "下调": "下条",              # xiàtiáo
                    "调查": "掉查",              # diàochá
                    "助长": "助掌",              # zhùzhǎng
                    "长相": "掌相",              # zhǎngxiàng
                    "蹊径": "希径",              # xījìng
                    "露出": "漏出",              # lòuchū
                    "犯罪分子": "犯罪份子",      # fànzuì fènzǐ
                    "强求": "抢求",              # qiǎngqiú
                    "为难": "维难",              # wéinán
                    "称为": "称维",              # chēngwéi
                    "人为月光族": "人维月光族",  # wéi
                    "戏称其为": "戏称其维",      # wéi
                    "为整鸡": "位整鸡",          # wèi
                    "处于": "楚于",              # chǔyú
                    "行业": "航业",              # hángyè
                    "一站式": "一站室",          # yízhànshì
                    "发难": "发难"},             # fānàn (giữ nguyên)
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds82.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
