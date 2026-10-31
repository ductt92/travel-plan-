#!/usr/bin/env python3
"""Kịch bản bài giảng 顶石中文 – Bài 1.2 «学区房情结怎么破？». Chạy để sinh ds12.json."""
import json
import os

TAG = "顶石中文 · Bài 1.2 · 学区房情结怎么破？"
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
    zh="学区房情结怎么破？", py="Xuéqūfáng qíngjié zěnme pò?",
    vi="Bài 1.2: Làm sao gỡ nỗi ám ảnh nhà gần trường tốt?",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng giáo trình 顶石中文, Đỉnh cao tiếng Trung.",
         "Hôm nay chúng ta học bài một chấm hai, bài thứ hai của Đơn vị một, 教育篇, chủ đề Giáo dục: 学区房情结怎么破？ Nghĩa là: Làm sao gỡ bỏ nỗi ám ảnh nhà gần trường tốt?",
         "学区房 là nhà nằm trong khu tuyển sinh của một trường tốt. Ở Trung Quốc, trẻ em thường học trường thuộc khu vực nơi gia đình có nhà và hộ khẩu, nên phụ huynh sẵn sàng bỏ ra rất nhiều tiền, có khi mua cả một căn nhà cũ nát, chỉ để con được vào trường tốt. 情结 là nỗi ám ảnh, tâm lý khó dứt bỏ; 破 là phá bỏ, gỡ bỏ.",
         "Bài khóa được cải biên từ video 唯一的世界大同：学区房 của kênh Candice talk. Tác giả so sánh nhà gần trường ở Trung Quốc và ở nước ngoài, và chỉ ra một điểm khác biệt rất thú vị về quan hệ nhân quả giữa trường tốt và giá nhà cao."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài khóa: so sánh 学区房 ở Trung Quốc và ở nước ngoài",
           "Nắm vững 45 từ mới (40 từ trong sách + 5 từ bổ sung), kèm âm Hán Việt và ví dụ",
           "11 mẫu câu: 不尽然 · 何 · 乃至 · 越发 · 何以见得 · 不妨 · 话又说回来 · 区别在于 · 脱胎于 · 一则……二则…… · 如此一来",
           "Kết hợp từ (词语搭配) và 7 thành ngữ: 茶余饭后 · 层出不穷 · 众所周知 · 水涨船高……",
           "Luyện tập, thảo luận: chuyện “học trái tuyến”, nhà gần trường điểm ở Việt Nam"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa: nhà gần trường tốt ở Trung Quốc và ở nước ngoài giống và khác nhau như thế nào."),
         F(1, "Thứ hai, nắm vững bốn mươi lăm từ mới: bốn mươi từ trong sách và năm từ thầy bổ sung từ bài khóa."),
         F(2, "Thứ ba, học mười một mẫu câu trọng điểm. Bài này có rất nhiều từ nối dùng trong văn nghị luận, như 不尽然, không hẳn vậy; 何以见得, lấy gì mà biết; 话又说回来, nói đi cũng phải nói lại; và 一则……二则……, một là…, hai là…."),
         F(3, "Thứ tư, học các kết hợp từ và bảy thành ngữ, như 茶余饭后, 层出不穷, 众所周知, 水涨船高."),
         F(4, "Cuối cùng là luyện tập và thảo luận, liên hệ với chuyện học trái tuyến và nhà gần trường điểm ở Việt Nam. Các bạn hãy chuẩn bị giấy bút nhé.")])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 课前思考", title="Khởi động: Suy nghĩ trước khi học (课前思考)", reveal=True, size=34,
    items=["(1) 你们国家也有学区房吗？",
           "Đáp án gợi ý: 有。在越南，公立中小学一般按居住地区招生，所以河内、胡志明市一些名校附近的房子也特别贵。",
           "(2) 你们觉得高价买学区房值不值？",
           "Đáp án gợi ý: 我觉得不一定值得。好学区有好的教育资源，但孩子的成长更取决于家庭教育和自己的努力。",
           "(3) 学区房存在有合理性吗？政府有无必要出台政策限制学区房？",
           "Đáp án gợi ý: 学区房反映了教育资源不均衡的问题。政府有必要出台政策，比如教师轮换、就近入学，让每所学校都差不多好。"],
    say=["Chúng ta bắt đầu bằng phần 课前思考, suy nghĩ trước khi học. Các bạn hãy tạm dừng video, tự trả lời bằng tiếng Trung trước, rồi nghe đáp án gợi ý nhé.",
         F(0, "Câu một: 你们国家也有学区房吗？ Ở nước bạn có nhà gần trường tốt không?"),
         F(1, "Đáp án gợi ý: 有。在越南，公立中小学一般按居住地区招生，所以河内、胡志明市一些名校附近的房子也特别贵。 Có. Ở Việt Nam, trường tiểu học và trung học cơ sở công lập thường tuyển sinh theo địa bàn cư trú, nên nhà gần một số trường nổi tiếng ở Hà Nội, Thành phố Hồ Chí Minh cũng rất đắt."),
         F(2, "Câu hai: 你们觉得高价买学区房值不值？ Bạn thấy bỏ giá cao mua nhà gần trường tốt có đáng không?"),
         F(3, "Đáp án gợi ý: 我觉得不一定值得。好学区有好的教育资源，但孩子的成长更取决于家庭教育和自己的努力。 Tôi thấy chưa chắc đáng. Khu trường tốt có tài nguyên giáo dục tốt, nhưng sự trưởng thành của trẻ phụ thuộc nhiều hơn vào giáo dục gia đình và sự cố gắng của bản thân."),
         F(4, "Câu ba: 学区房存在有合理性吗？政府有无必要出台政策限制学区房？ Nhà gần trường tốt tồn tại có hợp lý không? Chính phủ có cần ban hành chính sách hạn chế không? 有无 là có hay không, văn viết; 出台 là ban hành."),
         F(5, "Đáp án gợi ý: 学区房反映了教育资源不均衡的问题。政府有必要出台政策，比如教师轮换、就近入学，让每所学校都差不多好。 Nhà gần trường tốt phản ánh vấn đề tài nguyên giáo dục không đồng đều. Chính phủ cần có chính sách, như luân chuyển giáo viên, học sinh học trường gần nhà, để trường nào cũng tốt như nhau.")])

add("bullets", section="Khởi động 课前思考", title="Bối cảnh: các khái niệm cần biết (注释)", size=36,
    items=["老破小: nhà cũ, nát, nhỏ ở khu nội thành – năm xây đã lâu, môi trường xung quanh kém",
           "学区房: danh từ riêng, chỉ nhà ở gần tài nguyên giáo dục chất lượng cao (trường tốt)",
           "高净值人群: ở Trung Quốc, người có tài sản ròng từ 10 triệu nhân dân tệ trở lên",
           "精英群体: tầng lớp thành công – giàu có, có địa vị, học vấn cao, có quan hệ xã hội",
           "“别让孩子输在起跑线上” – câu cửa miệng của phụ huynh Trung Quốc"],
    say=["Trước khi học từ mới, chúng ta tìm hiểu một số khái niệm qua phần chú thích, 注释, của sách.",
         F(0, "老破小, ghép từ ba chữ: cũ, nát, nhỏ. Đó là những căn hộ diện tích nhỏ ở khu nội thành, xây đã rất lâu, môi trường xung quanh thường khá kém. Vậy mà nếu nằm cạnh trường tốt, chúng có thể bán được giá cao hơn hẳn nhà mới cùng khu."),
         F(1, "学区房 là danh từ riêng, chỉ những căn nhà ở có tài nguyên giáo dục chất lượng cao ở xung quanh."),
         F(2, "高净值人群 là nhóm người có tài sản ròng cao. Ở Trung Quốc, thường chỉ người có tài sản ròng từ mười triệu nhân dân tệ trở lên; ở Mỹ, tiêu chuẩn là tài sản có thể đầu tư từ một triệu, ba triệu, năm triệu hoặc mười triệu đô la Mỹ trở lên."),
         F(3, "精英群体 là tầng lớp tinh hoa: những người thành công, có của cải và địa vị xã hội, được học hành đến nơi đến chốn, và có những mối quan hệ, bối cảnh xã hội nhất định."),
         F(4, "Và một câu các bạn sẽ gặp đi gặp lại: 别让孩子输在起跑线上, đừng để con thua ngay từ vạch xuất phát. Chính tâm lý này đã đẩy giá nhà gần trường tốt lên rất cao.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("学区", "xuéqū", "học khu", "danh từ", "khu tuyển sinh (khu vực phân tuyến trường học)", "我家在这所小学的学区里。", "Nhà tôi nằm trong khu tuyển sinh của trường tiểu học này.",
     "Danh từ, chỉ khu vực quản lý được chia theo sự phân bố các trường tiểu học và trung học, để học sinh đi học gần nhà. 学区房 là nhà nằm trong khu tuyển sinh của trường tốt."),
    ("情结", "qíngjié", "tình kết", "danh từ", "nỗi niềm khó dứt, nỗi ám ảnh, tâm lý", "很多老人都有很深的故乡情结。", "Nhiều người già mang nỗi niềm quê hương rất sâu nặng.",
     "Danh từ, chỉ một thứ tình cảm khó dứt bỏ, không buông xuống được, như 思乡情结, nỗi nhớ quê. Tên bài 学区房情结怎么破 là làm sao gỡ bỏ nỗi ám ảnh nhà gần trường tốt."),
    ("谈资", "tánzī", "đàm tư", "danh từ", "đề tài bàn tán, chuyện để nói", "这件事成了大家茶余饭后的谈资。", "Chuyện này thành đề tài bàn tán lúc rảnh rỗi của mọi người.",
     "Danh từ, nghĩa là tư liệu để nói chuyện, đề tài bàn tán. Thường đi với thành ngữ 茶余饭后. Trong bài: 学区房这三个字就变成了人们茶余饭后的谈资."),
    ("不尽然", "bù jìnrán", "bất tận nhiên", "cụm từ", "không hẳn như vậy, không hoàn toàn đúng", "都说贵的东西好，其实不尽然。", "Ai cũng nói đồ đắt là tốt, thực ra không hẳn vậy.",
     "Cụm từ, nghĩa là không nhất định như thế, không hoàn toàn như vậy. Chữ giữa đọc thanh bốn, nghĩa là hết, hoàn toàn. Dùng để phản bác nhẹ nhàng một ý kiến phổ biến. Đây là mẫu câu đầu tiên của bài."),
    ("发源", "fāyuán", "phát nguyên", "động từ", "bắt nguồn (sông); khởi nguồn", "黄河发源于青海省。", "Sông Hoàng Hà bắt nguồn từ tỉnh Thanh Hải.",
     "Động từ, nghĩa gốc là sông bắt đầu chảy ra, nghĩa rộng là khởi nguồn. Mẫu thường gặp: 发源于 cộng nơi chốn; 发源地 là nơi khởi nguồn. Trong bài: 学区房这个概念在十几年前发源于英美."),
    ("联手", "liánshǒu", "liên thủ", "động từ", "bắt tay, hợp sức", "两家公司联手开发新产品。", "Hai công ty bắt tay phát triển sản phẩm mới.",
     "Động từ, nghĩa là liên kết, hợp tác với nhau. Trong bài: 教育集团和房地产机构强强联手, tập đoàn giáo dục và công ty bất động sản, hai bên mạnh bắt tay nhau."),
    ("房地产", "fángdìchǎn", "phòng địa sản", "danh từ", "bất động sản, nhà đất", "他在一家房地产公司工作。", "Anh ấy làm việc ở một công ty bất động sản.",
     "Danh từ, gọi chung nhà cửa và đất đai. Hay gặp 房地产公司，房地产市场，投资房地产."),
    ("净值", "jìngzhí", "tịnh trị", "danh từ", "giá trị ròng, tài sản ròng", "这家公司的资产净值超过一亿元。", "Tài sản ròng của công ty này vượt quá một trăm triệu tệ.",
     "Danh từ, là tổng tài sản trừ đi tổng nợ. Chữ 净 là sạch, ở đây là ròng. 高净值人群 là nhóm người có tài sản ròng cao."),
    ("入住", "rùzhù", "nhập trú", "động từ", "dọn vào ở; nhận phòng", "新房下个月就可以入住了。", "Nhà mới tháng sau là có thể dọn vào ở.",
     "Động từ, nghĩa là dọn vào ở, hoặc nhận phòng khách sạn. Trong bài: 吸引了很多高净值人群入住."),
    ("原本", "yuánběn", "nguyên bản", "phó từ", "vốn dĩ, ban đầu", "他原本是学医的，后来改学了戏剧。", "Anh ấy vốn học y, sau chuyển sang học kịch.",
     "Phó từ, nghĩa là vốn dĩ, lúc đầu, giống 原来，本来. Chú ý: tiếng Việt nguyên bản là bản gốc; còn phó từ 原本 là vốn dĩ. Trong bài: 一块块原本很普通的住宅用地."),
    ("圣地", "shèngdì", "thánh địa", "danh từ", "thánh địa; nơi nổi tiếng nhất về một mặt", "这里是有名的旅游圣地。", "Đây là thánh địa du lịch nổi tiếng.",
     "Danh từ, chỉ nơi có ý nghĩa lịch sử hay tôn giáo đặc biệt; nghĩa rộng là nơi nổi tiếng nhất về một mặt nào đó: 佛教圣地，旅游圣地，教育圣地."),
    ("乃至", "nǎizhì", "nãi chí", "liên từ", "thậm chí, cho đến cả", "他的发明引起了全国乃至国际上的重视。", "Phát minh của anh ấy được cả nước, thậm chí cả quốc tế chú ý.",
     "Liên từ văn viết, nghĩa là thậm chí, cho đến cả, nối thành phần mang ý tăng tiến. Đây là một mẫu câu trọng điểm của bài."),
    ("师资", "shīzī", "sư tư", "danh từ", "đội ngũ giáo viên", "这所学校的师资力量很强。", "Đội ngũ giáo viên của trường này rất mạnh.",
     "Danh từ, chỉ những người có thể làm giáo viên, tức đội ngũ giáo viên. Hay gặp 师资力量，师资不足，培养师资."),
    ("雄厚", "xiónghòu", "hùng hậu", "tính từ", "hùng hậu, dồi dào", "这家公司资金雄厚。", "Công ty này có nguồn vốn hùng hậu.",
     "Tính từ, nói về nhân lực, vật lực, tài lực dồi dào, mạnh. Âm Hán Việt và nghĩa giống tiếng Việt. Hay gặp 实力雄厚，资金雄厚，师资力量雄厚."),
    ("周边", "zhōubiān", "chu biên", "danh từ", "xung quanh, lân cận", "学校周边有很多小饭馆。", "Xung quanh trường có rất nhiều quán ăn nhỏ.",
     "Danh từ, nghĩa là xung quanh, vùng lân cận. Hay gặp 周边地区，周边国家. Ngày nay 周边 còn chỉ hàng lưu niệm ăn theo phim, truyện, gọi là 周边产品."),
    ("越发", "yuèfā", "việt phát", "phó từ", "càng, càng thêm", "离开家以后，他越发想念父母了。", "Sau khi rời nhà, anh ấy càng nhớ bố mẹ hơn.",
     "Phó từ mức độ, nghĩa là càng thêm, mức độ sâu hơn trước, tác dụng giống 越来越. Trong bài: 使周边的房子越发吃香."),
    ("吃香", "chīxiāng", "cật hương", "tính từ", "được ưa chuộng, được trọng dụng", "会说中文的人在这里很吃香。", "Người biết nói tiếng Trung rất được trọng dụng ở đây.",
     "Tính từ khẩu ngữ, nghĩa đen là ăn thơm, nghĩa là được hoan nghênh, được coi trọng. Hay gặp 很吃香，越来越吃香."),
    ("不妨", "bùfáng", "bất phương", "phó từ", "cứ thử, chẳng ngại gì mà không", "这个办法你不妨试一试。", "Cách này cậu cứ thử xem sao.",
     "Phó từ ngữ khí, nghĩa là có thể thử làm, sai cũng không sao. Chữ 妨 là cản trở, 不妨 là không có gì cản trở. Đây là cách đưa ra lời khuyên rất nhẹ nhàng, lịch sự."),
    ("来历", "láilì", "lai lịch", "danh từ", "lai lịch, nguồn gốc", "这个节日的来历很有意思。", "Nguồn gốc của ngày lễ này rất thú vị.",
     "Danh từ, chỉ bối cảnh lịch sử, nguồn gốc của người hay sự vật. Hay gặp 查明来历，来历不明, lai lịch không rõ ràng."),
    ("起跑线", "qǐpǎoxiàn", "khởi bào tuyến", "danh từ", "vạch xuất phát", "别让孩子输在起跑线上。", "Đừng để con thua ngay từ vạch xuất phát.",
     "Danh từ, vạch xuất phát trong cuộc thi chạy; nghĩa bóng là điểm khởi đầu. Trong bài: 太多人想让孩子赢在起跑线上, quá nhiều người muốn con thắng ngay từ vạch xuất phát."),
    ("所属", "suǒshǔ", "sở thuộc", "tính từ", "trực thuộc, thuộc về", "请写上你所属的单位。", "Hãy ghi đơn vị mà bạn trực thuộc.",
     "Tính từ, nghĩa là thuộc về, trực thuộc. Hay gặp 所属学校，所属机构. Trong bài: 不停地在所属学区买买买, liên tục mua nhà trong khu tuyển sinh tương ứng."),
    ("公立", "gōnglì", "công lập", "tính từ", "công lập", "公立学校的学费比较低。", "Học phí trường công lập tương đối thấp.",
     "Tính từ, nghĩa là do nhà nước thành lập. Đối lập là 私立, tư thục, cũng là từ mới của bài."),
    ("地理", "dìlǐ", "địa lý", "danh từ", "địa lý; vị trí địa lý", "这家酒店的地理位置很好。", "Vị trí địa lý của khách sạn này rất đẹp.",
     "Danh từ, chỉ tình hình chung về tự nhiên, giao thông, dân cư của một vùng; cũng là môn địa lý. Trong bài: 外国的公立学校区别在于地理位置."),
    ("地处", "dìchǔ", "địa xứ", "động từ", "nằm ở, tọa lạc tại", "我们学校地处市中心。", "Trường chúng tôi nằm ở trung tâm thành phố.",
     "Động từ, nghĩa là về mặt địa lý nằm ở vị trí nào đó. Chữ thứ hai đọc thanh ba. Hay gặp 地处市中心，地处闹市. Trong bài: 一些学校地处郊区."),
    ("轮换", "lúnhuàn", "luân hoán", "động từ", "luân chuyển, thay phiên", "他们轮换着值夜班。", "Họ thay phiên nhau trực ca đêm.",
     "Động từ, nghĩa là lần lượt thay thế nhau. Trong bài: 教师轮换制度, chế độ luân chuyển giáo viên giữa các trường. Gần nghĩa với 轮流 ở bài trước."),
    ("区分", "qūfēn", "khu phân", "động từ", "phân biệt, phân loại", "这两个词的意思很难区分。", "Nghĩa của hai từ này rất khó phân biệt.",
     "Động từ, nghĩa là phân biệt, chia ra. Hay gặp 区分优劣，难以区分. Trong bài: 那如何区分好学区和坏学区呢？"),
    ("生源", "shēngyuán", "sinh nguyên", "danh từ", "nguồn học sinh, chất lượng đầu vào", "这所学校的生源很好。", "Nguồn học sinh đầu vào của trường này rất tốt.",
     "Danh từ, chỉ nguồn học sinh, thường dùng khi nói về tuyển sinh. Hay gặp 争夺生源, tranh giành học sinh. Bài khóa nói: phân biệt khu trường tốt hay xấu, 核心在于生源."),
    ("深信", "shēnxìn", "thâm tín", "động từ", "tin chắc, rất tin", "我深信他一定会成功。", "Tôi tin chắc anh ấy nhất định sẽ thành công.",
     "Động từ, nghĩa là vô cùng tin tưởng. Hay gặp 深信不疑, tin không chút nghi ngờ."),
    ("户口", "hùkǒu", "hộ khẩu", "danh từ", "hộ khẩu", "他的户口在北京。", "Hộ khẩu của anh ấy ở Bắc Kinh.",
     "Danh từ, hộ khẩu, âm Hán Việt và nghĩa giống tiếng Việt. Hay gặp 报户口, đăng ký hộ khẩu; 迁户口, chuyển hộ khẩu. Ở Trung Quốc, hộ khẩu ảnh hưởng trực tiếp đến việc con cái được học trường nào."),
    ("户籍", "hùjí", "hộ tịch", "danh từ", "hộ tịch, thân phận cư dân", "没有本地户籍，孩子很难在这里上学。", "Không có hộ tịch địa phương, con cái rất khó đi học ở đây.",
     "Danh từ, nghĩa gốc là sổ đăng ký dân cư theo hộ, sau chỉ thân phận cư dân của một địa phương. Trong bài đi đôi với 户口: 户口户籍这个概念."),
    ("就读", "jiùdú", "tựu độc", "động từ", "theo học, học tại", "她目前就读于南京大学。", "Hiện cô ấy đang theo học tại Đại học Nam Kinh.",
     "Động từ, nghĩa là học ở một trường nào đó. Mẫu văn viết: 就读于 cộng tên trường. Trong bài: 让孩子在这所公立学校就读."),
    ("私立", "sīlì", "tư lập", "tính từ", "tư thục, tư nhân", "这是一所私立医院。", "Đây là một bệnh viện tư nhân.",
     "Tính từ, nghĩa là do tư nhân bỏ tiền thành lập. Hay gặp 私立学校，私立医院. Đối lập với 公立."),
    ("脱胎", "tuōtāi", "thoát thai", "động từ", "thoát thai, hình thành từ (cái khác)", "这种新技术脱胎于传统工艺。", "Kỹ thuật mới này phát triển từ nghề thủ công truyền thống.",
     "Động từ, chỉ một sự vật được thai nghén, biến đổi từ một sự vật khác mà thành. Mẫu: 脱胎于. Tiếng Việt cũng có từ thoát thai."),
    ("贵族", "guìzú", "quý tộc", "danh từ", "quý tộc", "这所学校以前是一所贵族学校。", "Ngôi trường này trước kia là một trường quý tộc.",
     "Danh từ, tầng lớp trên có đặc quyền trong xã hội phong kiến hoặc các nước quân chủ. 贵族学校 là trường quý tộc, ngày nay còn chỉ trường có học phí rất cao."),
    ("寄宿", "jìsù", "ký túc", "động từ", "ở nội trú, ở ký túc xá", "他在一所寄宿学校读书。", "Cậu ấy học ở một trường nội trú.",
     "Động từ, nghĩa là học sinh ở lại ký túc xá của trường, đối lập với 走读, đi học rồi về nhà trong ngày. Hay gặp 寄宿生，寄宿学校，寄宿制度."),
    ("享有", "xiǎngyǒu", "hưởng hữu", "động từ", "được hưởng, có (quyền lợi, danh tiếng)", "公民享有受教育的权利。", "Công dân được hưởng quyền được giáo dục.",
     "Động từ, nghĩa là được hưởng, có được về quyền lợi, danh tiếng. Hay gặp 享有权利，享有盛誉."),
    ("盛誉", "shèngyù", "thịnh dự", "danh từ", "danh tiếng lớn, tiếng tăm lừng lẫy", "这所大学在国际上享有盛誉。", "Trường đại học này có danh tiếng lớn trên thế giới.",
     "Danh từ, nghĩa là vinh dự, danh tiếng rất cao. Hầu như luôn đi với 享有: 享有盛誉."),
    ("分支", "fēnzhī", "phân chi", "danh từ", "chi nhánh, nhánh", "这家银行在越南设立了分支机构。", "Ngân hàng này đã lập chi nhánh ở Việt Nam.",
     "Danh từ, chỉ phần được tách ra từ một hệ thống hay một chủ thể. 分支机构 là chi nhánh. Trong bài: 去周边设立分支机构."),
    ("精英", "jīngyīng", "tinh anh", "danh từ", "tinh hoa, người ưu tú", "他是商界的精英。", "Anh ấy là người ưu tú trong giới kinh doanh.",
     "Danh từ, chỉ nhân tài xuất chúng. 精英群体 là tầng lớp tinh hoa. Ở bài sau và phần ôn tập, chúng ta còn gặp cụm 精英教育, giáo dục tinh hoa."),
    ("相应", "xiāngyìng", "tương ứng", "động từ", "tương ứng, theo đó", "环境变了，方法也要相应地改变。", "Môi trường thay đổi, phương pháp cũng phải thay đổi tương ứng.",
     "Động từ, nghĩa là thích ứng với nhau, theo đó mà thay đổi. Chữ thứ hai đọc thanh bốn. Hay dùng 相应地 làm trạng ngữ. Trong bài: 房价便相应上涨, giá nhà theo đó mà tăng."),
    # năm từ bổ sung lấy từ bài khóa
    ("打造", "dǎzào", "đả tạo", "động từ (bổ sung)", "xây dựng, tạo dựng", "这座城市想打造国际化大都市。", "Thành phố này muốn xây dựng thành đô thị quốc tế.",
     "Động từ, nghĩa gốc là rèn đúc, nghĩa thường dùng ngày nay là xây dựng, tạo ra một thương hiệu, sản phẩm hay khu vực. Trong bài: 联手打造了一个又一个学区."),
    ("住宅", "zhùzhái", "trú trạch", "danh từ (bổ sung)", "nhà ở", "这里是一片新建的住宅区。", "Đây là một khu nhà ở mới xây.",
     "Danh từ, nghĩa là nhà ở, văn viết. Hay gặp 住宅区，住宅用地, đất ở. Trong bài: 原本很普通的住宅用地."),
    ("优质", "yōuzhì", "ưu chất", "tính từ (bổ sung)", "chất lượng cao", "优质的服务能留住顾客。", "Dịch vụ chất lượng cao giữ chân được khách hàng.",
     "Tính từ, nghĩa là chất lượng tốt. Trong bài: 优质的教育资源，优质的大学. Cụm 优质教育资源 sẽ gặp lại ở bài một chấm ba."),
    ("核心", "héxīn", "hạch tâm", "danh từ (bổ sung)", "cốt lõi, trọng tâm", "这个问题的核心是钱。", "Cốt lõi của vấn đề này là tiền.",
     "Danh từ, nghĩa là phần trung tâm, quan trọng nhất. Hay gặp 核心在于, cốt lõi nằm ở. Trong bài: 核心在于生源."),
    ("逻辑", "luójí", "la tập", "danh từ (bổ sung)", "lôgic, quy luật suy luận", "他说话很有逻辑。", "Anh ấy nói chuyện rất có lôgic.",
     "Danh từ, phiên âm từ tiếng Anh logic, nghĩa là quy luật suy luận. Trong bài: 这就是国外高房价带动了好学区的逻辑."),
]

add("bullets", chapter="Từ mới (45 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 1.2 có 40 từ trong sách + 5 từ bổ sung, chia thành 15 nhóm",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 不尽然 (jìn) · 地处 (chǔ) · 相应 (yìng)",
           "Từ dễ nhầm: 原本 · 情结 · 吃香"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bảng từ của sách có bốn mươi từ; thầy bổ sung thêm năm từ quan trọng trong bài khóa, tổng cộng bốn mươi lăm từ, chia thành mười lăm nhóm. Bài này có nhiều từ về nhà đất, trường học và hộ khẩu.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe nhé."),
         F(3, "Chú ý một số chữ nhiều âm đọc: chữ giữa trong 不尽然 đọc thanh bốn; chữ thứ hai trong 地处 đọc thanh ba; chữ thứ hai trong 相应 đọc thanh bốn."),
         F(4, "Có mấy từ dễ hiểu nhầm, như 原本, không phải bản gốc mà là vốn dĩ; 吃香, không phải ăn ngon mà là được ưa chuộng. Chúng ta bắt đầu.")])

sizes = [3] * 15
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
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung nếu khác: số viết bằng chữ, bỏ ngoặc kép])
P = [
    ("一到开学季，学区房这三个字就变成了人们茶余饭后的谈资，关于学区房的新闻也层出不穷，比如某某学校旁边的“老破小”卖出了高出同地区房价不少的价钱。",
     "Cứ đến mùa khai giảng, ba chữ “nhà khu trường tốt” lại trở thành đề tài bàn tán lúc rảnh rỗi của mọi người, tin tức về nhà khu trường tốt cũng xuất hiện liên tục, chẳng hạn căn “cũ nát nhỏ” cạnh trường nọ trường kia đã bán được với giá cao hơn khá nhiều so với giá nhà cùng khu vực.",
     ["一到开学季 là cứ đến mùa khai giảng; mẫu 一……就…… nghĩa là hễ… thì…. 茶余饭后的谈资 là đề tài bàn tán lúc trà dư tửu hậu. 层出不穷 là xuất hiện liên tục, không dứt.",
      "某某学校 là trường nọ trường kia. 老破小 là nhà cũ, nát, nhỏ. 高出同地区房价不少 là cao hơn khá nhiều so với giá nhà cùng khu; mẫu 高出 cộng đối tượng so sánh cộng mức chênh lệch."]),
    ("学区房到底是不是中国特色呢？其实不尽然，学区房这个概念在十几年前发源于英美，那个时候它们的教育集团和房地产机构强强联手打造了一个又一个学区，吸引了很多高净值人群入住，",
     "Nhà khu trường tốt rốt cuộc có phải là đặc sản của Trung Quốc không? Thực ra không hẳn vậy. Khái niệm này khởi nguồn từ Anh và Mỹ hơn mười năm trước; khi ấy, các tập đoàn giáo dục và công ty bất động sản ở đó đã hợp sức xây dựng hết khu tuyển sinh này đến khu tuyển sinh khác, thu hút rất nhiều người có tài sản lớn đến ở,",
     ["中国特色 là đặc sắc Trung Quốc, chỉ thứ chỉ Trung Quốc mới có. 其实不尽然 là thực ra không hẳn vậy, mẫu câu đầu tiên của bài. 发源于英美 là khởi nguồn từ Anh và Mỹ.",
      "强强联手 là mạnh bắt tay mạnh. 打造了一个又一个学区 là xây dựng hết khu này đến khu khác. 高净值人群入住 là những người có tài sản ròng cao dọn đến ở."]),
    ("于是把一块块原本很普通的住宅用地变成了教育圣地，那中国的学区房和外国的学区房到底有何差别呢？",
     "thế là biến từng mảnh đất ở vốn rất bình thường thành thánh địa giáo dục. Vậy nhà khu trường tốt ở Trung Quốc và ở nước ngoài rốt cuộc khác nhau ở điểm nào?",
     ["于是 là thế là, nối kết quả. 一块块 là từng mảnh, lượng từ lặp lại chỉ số nhiều. 原本很普通的住宅用地 là đất ở vốn rất bình thường. 教育圣地 là thánh địa giáo dục.",
      "有何差别 là có gì khác biệt; 何 là đại từ nghi vấn văn viết, bằng 什么. Câu hỏi này là luận đề của cả bài: phần còn lại sẽ trả lời nó."]),
    ("国内有省重点、市重点、区重点，这些学校可能十几年前乃至一百年前就有了，一开始这些学校旁边是没有那么多房子的，就因为师资力量雄厚，使周边的房子越发吃香。",
     "Trong nước có trường trọng điểm cấp tỉnh, cấp thành phố, cấp quận; những trường này có thể đã có từ mười mấy năm, thậm chí một trăm năm trước. Lúc đầu cạnh những trường này không có nhiều nhà như vậy; chỉ vì đội ngũ giáo viên hùng hậu mà nhà cửa xung quanh ngày càng được săn đón.",
     ["省重点、市重点、区重点 là trường trọng điểm cấp tỉnh, cấp thành phố, cấp quận. 十几年前乃至一百年前 là mười mấy năm trước, thậm chí một trăm năm trước; 乃至 nối ý tăng tiến.",
      "师资力量雄厚 là đội ngũ giáo viên hùng hậu. 使周边的房子越发吃香 là khiến nhà xung quanh càng được ưa chuộng; 越发 là càng thêm."]),
    ("中国的学区房是好学区带动了高房价，而外国的学区房是高房价带动了好学区。何以见得呢？",
     "Nhà khu trường tốt ở Trung Quốc là khu trường tốt kéo giá nhà lên cao, còn ở nước ngoài thì là giá nhà cao kéo theo khu trường tốt. Lấy gì mà biết được như vậy?",
     ["带动 là kéo theo, thúc đẩy. Đây là ý quan trọng nhất của bài: ở Trung Quốc, có trường tốt trước rồi giá nhà mới tăng; ở nước ngoài, giá nhà cao trước rồi mới có trường tốt. Quan hệ nhân quả ngược nhau.",
      "何以见得 là lấy gì mà biết được, căn cứ vào đâu mà khẳng định như vậy, giọng hỏi vặn. Tác giả tự đặt câu hỏi để dẫn dắt người đọc vào phần chứng minh."]),
    ("我们不妨来看看这些学区房的来历，众所周知现在太多人想让孩子赢在起跑线上，把孩子送进这些学校读书，于是不停地在所属学区买买买，房价便自然水涨船高了。",
     "Chúng ta thử xem lai lịch của những căn nhà khu trường tốt này. Ai cũng biết, bây giờ có quá nhiều người muốn con thắng ngay từ vạch xuất phát, muốn đưa con vào những trường này học, thế là cứ mua, mua, mua trong khu tuyển sinh tương ứng, giá nhà đương nhiên nước lên thuyền lên.",
     ["不妨来看看 là thử xem sao. 众所周知 là ai ai cũng biết. 赢在起跑线上 là thắng ngay từ vạch xuất phát.",
      "所属学区 là khu tuyển sinh mà trường đó thuộc về. 买买买 là cách nói vui trên mạng, mua liên tục. 水涨船高 là nước lên thuyền lên: nhu cầu tăng thì giá tăng theo. 便 là liền, văn viết của 就."]),
    ("那外国呢？外国的公立学校区别在于地理位置，一些学校地处郊区，另一些学校在市区，但其实几乎一模一样。至于师资力量，因为有教师轮换制度，所以相差无几。",
     "Còn nước ngoài thì sao? Các trường công lập ở nước ngoài khác nhau ở vị trí địa lý: một số trường nằm ở ngoại ô, một số khác ở nội thành, nhưng thực ra gần như giống hệt nhau. Còn về đội ngũ giáo viên, vì có chế độ luân chuyển giáo viên nên cũng chẳng chênh lệch bao nhiêu.",
     ["区别在于 là khác biệt nằm ở. 地处郊区 là nằm ở ngoại ô. 一模一样 là giống hệt nhau.",
      "至于 là còn về, dùng để chuyển sang một khía cạnh khác. 教师轮换制度 là chế độ luân chuyển giáo viên giữa các trường. 相差无几 là chênh lệch không đáng kể."]),
    ("那如何区分好学区和坏学区呢？核心在于生源。那怎么判断生源好不好呢？那就要看旁边是富人多还是穷人多。",
     "Vậy làm sao phân biệt khu trường tốt và khu trường kém? Cốt lõi nằm ở nguồn học sinh. Vậy làm sao đánh giá nguồn học sinh tốt hay không? Thì phải xem xung quanh người giàu nhiều hay người nghèo nhiều.",
     ["如何区分 là làm sao phân biệt; 如何 là văn viết của 怎么. 核心在于生源 là cốt lõi nằm ở nguồn học sinh.",
      "Đoạn này dùng liên tiếp các câu hỏi tự đặt rồi tự trả lời, một cách lập luận rất hay gặp trong văn nói và văn bình luận: 那……呢？……。那……呢？……."]),
    ("很多人都深信如果他们的孩子成长在富人堆里，就会比成长在穷人堆里的孩子未来发展好很多，这也就导致一个地区的房价高，富人就多；",
     "Rất nhiều người tin chắc rằng, nếu con họ lớn lên giữa đám người giàu, thì tương lai sẽ phát triển tốt hơn nhiều so với những đứa trẻ lớn lên giữa đám người nghèo; điều này dẫn đến việc một khu vực giá nhà cao thì người giàu sẽ nhiều;",
     ["深信 là tin chắc. 富人堆里 là giữa đám người giàu; 堆 là đống, ở đây chỉ một đám đông. 比……发展好很多 là phát triển tốt hơn nhiều so với….",
      "导致 là dẫn đến, thường dẫn đến kết quả không mong muốn hoặc trung tính. 房价高，富人就多 là chuỗi lập luận đầu tiên: giá nhà cao thì chỉ người giàu mới ở được."]),
    ("富人多，学校生源就好，这个学校自然而然就成了好学校了，这就是国外高房价带动了好学区的逻辑。",
     "người giàu nhiều thì nguồn học sinh của trường sẽ tốt, ngôi trường ấy tự nhiên trở thành trường tốt. Đó chính là lôgic giá nhà cao kéo theo khu trường tốt ở nước ngoài.",
     ["富人多，学校生源就好 nối tiếp chuỗi lập luận: người giàu nhiều thì học sinh tốt. Các vế nối nhau như dây chuyền, gọi là lối lập luận móc xích.",
      "自然而然 là tự nhiên mà thành. 这就是……的逻辑 là đó chính là lôgic của…, câu tổng kết cho đoạn chứng minh."]),
    ("话又说回来，因为国外是没有户口户籍这个概念的，所以很多人不用在那里买房，只要租房就可以让孩子在这所公立学校就读，所以国外就没有那么多砸锅卖铁要去买房子的故事了。",
     "Nhưng nói đi cũng phải nói lại, vì ở nước ngoài không có khái niệm hộ khẩu, hộ tịch, nên nhiều người không cần mua nhà ở đó, chỉ cần thuê nhà là có thể cho con học ở trường công lập ấy, vì vậy ở nước ngoài không có nhiều câu chuyện đập nồi bán sắt để mua nhà như thế.",
     ["话又说回来 là nói đi cũng phải nói lại, dùng để chuyển sang một góc nhìn khác. 户口户籍 là hộ khẩu, hộ tịch.",
      "只要……就…… là chỉ cần… là…. 在这所公立学校就读 là theo học ở trường công lập này. 砸锅卖铁 là đập nồi bán sắt vụn, tức là dốc hết tài sản, giống câu bán nhà bán cửa của tiếng Việt."]),
    ("那第二个区别在哪儿呢？第二个区别在于私立学校。在国外，优质的教育资源往往都是集中在私立学校的，而私立学校呢，又是脱胎于贵族学校的，",
     "Vậy khác biệt thứ hai nằm ở đâu? Khác biệt thứ hai nằm ở trường tư thục. Ở nước ngoài, tài nguyên giáo dục chất lượng cao thường tập trung ở trường tư, mà trường tư thì lại thoát thai từ trường quý tộc,",
     ["第二个区别在于私立学校 là khác biệt thứ hai nằm ở trường tư thục. 优质的教育资源 là tài nguyên giáo dục chất lượng cao. 集中在 là tập trung ở.",
      "而私立学校呢: chữ 呢 ở giữa câu tạo một quãng ngắt, nêu chủ đề rồi mới nói tiếp, rất khẩu ngữ. 脱胎于贵族学校 là hình thành từ trường quý tộc."]),
    ("所以很多富人是习惯直接把孩子送去贵族学校或者是私立学校读书的，这样的一些学校往往都是有宿舍的，学生也是习惯了这种寄宿制度，所以富人也没有必要去买学区房，只要能够负担学费就行了。",
     "nên nhiều người giàu có thói quen gửi thẳng con vào trường quý tộc hoặc trường tư học. Những trường như vậy thường có ký túc xá, học sinh cũng đã quen với chế độ nội trú này, nên người giàu cũng chẳng cần mua nhà khu trường tốt, chỉ cần trả nổi học phí là được.",
     ["是习惯……的: cấu trúc 是……的 nhấn mạnh thói quen. 宿舍 là ký túc xá. 寄宿制度 là chế độ nội trú.",
      "没有必要 là không cần thiết. 负担学费 là gánh vác học phí, trả nổi học phí. Vì học ở trường tư nội trú nên nhà ở gần trường không còn quan trọng."]),
    ("那么国外到底有没有学区房呢？其实也是有的，国外的学区房，真正的学区指的是大学。名牌大学旁边的房子总是不断有人购入，",
     "Vậy rốt cuộc ở nước ngoài có nhà khu trường tốt không? Thực ra cũng có. Ở nước ngoài, khu trường thực sự là nói đến trường đại học. Nhà gần các trường đại học danh tiếng lúc nào cũng có người mua vào,",
     ["其实也是有的 là thực ra cũng có. 真正的学区指的是大学 là khu trường thực sự chính là trường đại học, ý bất ngờ của bài.",
      "名牌大学 là đại học danh tiếng. 不断有人购入 là liên tục có người mua vào; 购入 là mua vào, văn viết."]),
    ("一则是因为优质的大学，往往会吸引更多的优秀学生，然而这些大学没有那么多宿舍，所以很多大学生可能大二就出去租房子了；二则是这些享有盛誉的大学，会吸引更多的企业去周边设立分支机构。",
     "một là vì đại học chất lượng cao thường thu hút nhiều sinh viên giỏi hơn, nhưng các trường này không có nhiều ký túc xá như vậy, nên nhiều sinh viên có thể từ năm thứ hai đã ra ngoài thuê nhà; hai là những trường đại học danh tiếng này sẽ thu hút nhiều doanh nghiệp hơn đến lập chi nhánh ở khu vực xung quanh.",
     ["一则……；二则…… là một là…, hai là…, dùng để liệt kê nguyên nhân. 大二 là năm thứ hai đại học; tương tự 大一，大三，大四.",
      "享有盛誉的大学 là đại học có danh tiếng lớn. 设立分支机构 là lập chi nhánh. Hai nguyên nhân: sinh viên cần thuê nhà, và doanh nghiệp kéo đến."]),
    ("如此一来，工作机会也就增加了，有更多精英群体在那一带工作，所以很多人可能会在那里买房、租房，于是名牌大学周边的房价便相应上涨，这就是真正的学区房了。",
     "Như vậy, cơ hội việc làm cũng tăng lên, có thêm nhiều người thuộc tầng lớp tinh hoa làm việc ở khu vực đó, nên nhiều người có thể sẽ mua nhà, thuê nhà ở đó, thế là giá nhà quanh các trường đại học danh tiếng cũng theo đó tăng lên. Đó mới là nhà khu trường tốt thực sự.",
     ["如此一来 là như vậy thì, như thế là, nối kết quả của điều vừa nói. 精英群体 là tầng lớp tinh hoa. 那一带 là vùng ấy, khu vực ấy.",
      "房价便相应上涨 là giá nhà theo đó mà tăng. 这就是真正的学区房了 là câu kết, trả lời câu hỏi ở đầu đoạn năm: ở nước ngoài, nhà gần trường thực sự là nhà gần đại học."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 学区房情结怎么破？", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa. Bài được cải biên từ lời bình trong một video, nên giọng văn rất gần văn nói, có nhiều câu tự hỏi tự trả lời như 何以见得呢, 那外国呢.",
         F(0, "Bài có năm đoạn, thầy chia thành mười sáu phần ngắn. Với mỗi phần, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    assert len(item) in (3, 4), item[0][:10]
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 70 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", ""), cap="")] + [F(1, n) for n in notes])

# ======================= ĐỌC HIỂU =======================
add("bullets", chapter="Đọc hiểu", section="Đọc hiểu 课文理解", title="Bố cục bài khóa", size=36,
    items=["Đoạn 1: 学区房 thành đề tài nóng; khởi nguồn từ Anh, Mỹ → câu hỏi: Trung Quốc và nước ngoài khác nhau ở đâu?",
           "Đoạn 2: Trung Quốc – 好学区带动了高房价 (trường tốt kéo giá nhà lên)",
           "Đoạn 3: Nước ngoài (khác biệt 1) – trường công gần như nhau; cốt lõi là 生源 → 高房价带动了好学区; không có hộ khẩu, thuê nhà cũng được học",
           "Đoạn 4: Khác biệt 2 – trường tư thục (thoát thai từ trường quý tộc), có chế độ nội trú",
           "Đoạn 5: Nhà khu trường tốt thực sự ở nước ngoài là nhà quanh trường đại học danh tiếng"],
    say=["Chúng ta cùng nhìn lại bố cục của bài khóa. Đây là một bài so sánh rất rõ ràng, đáng để học cách tổ chức ý.",
         F(0, "Đoạn một: nêu hiện tượng nhà khu trường tốt thành đề tài nóng, chỉ ra rằng khái niệm này khởi nguồn từ Anh và Mỹ, rồi đặt câu hỏi: nhà khu trường tốt ở Trung Quốc và ở nước ngoài khác nhau ở đâu?"),
         F(1, "Đoạn hai: ở Trung Quốc, trường tốt có từ lâu, vì giáo viên giỏi nên nhà xung quanh mới đắt lên: 好学区带动了高房价."),
         F(2, "Đoạn ba: khác biệt thứ nhất. Ở nước ngoài, trường công lập gần như như nhau; cốt lõi là nguồn học sinh, nơi nào nhà đắt thì người giàu nhiều, trường thành trường tốt: 高房价带动了好学区. Hơn nữa không có hộ khẩu, thuê nhà cũng được học."),
         F(3, "Đoạn bốn: khác biệt thứ hai là trường tư thục. Người giàu gửi con vào trường tư, trường quý tộc có nội trú, nên không cần mua nhà gần trường."),
         F(4, "Đoạn năm: ở nước ngoài, nhà khu trường tốt thực sự là nhà quanh các trường đại học danh tiếng. Bố cục này chính là gợi ý cho phần viết bài so sánh trong phần ôn tập đơn vị ở bài sau.")])

add("bullets", section="Đọc hiểu 课文理解", title="Câu hỏi đọc hiểu (1)", reveal=True, size=34,
    items=["(1) 学区房的概念最早发源于哪里？当时是怎么形成的？",
           "Đáp án: 十几年前发源于英美，当时教育集团和房地产机构联手打造学区，吸引了很多高净值人群入住。",
           "(2) 中国和外国的学区房，因果关系有什么不同？",
           "Đáp án: 中国是好学区带动了高房价，外国是高房价带动了好学区。",
           "(3) 中国学区房的房价为什么会水涨船高？",
           "Đáp án: 因为太多人想让孩子赢在起跑线上，都在所属学区买房。"],
    say=["Bây giờ chúng ta kiểm tra mức độ hiểu bài. Thầy đọc câu hỏi, các bạn tạm dừng, trả lời bằng tiếng Trung, rồi nghe đáp án.",
         F(0, "Câu một: 学区房的概念最早发源于哪里？当时是怎么形成的？ Khái niệm nhà khu trường tốt khởi nguồn từ đâu? Khi đó hình thành như thế nào?"),
         F(1, "Đáp án: 十几年前发源于英美，当时教育集团和房地产机构联手打造学区，吸引了很多高净值人群入住。 Khởi nguồn từ Anh và Mỹ hơn mười năm trước; khi ấy các tập đoàn giáo dục và công ty bất động sản hợp sức xây dựng các khu tuyển sinh, thu hút người giàu đến ở."),
         F(2, "Câu hai: 中国和外国的学区房，因果关系有什么不同？ Quan hệ nhân quả của nhà khu trường tốt ở Trung Quốc và ở nước ngoài khác nhau thế nào?"),
         F(3, "Đáp án: 中国是好学区带动了高房价，外国是高房价带动了好学区。 Ở Trung Quốc là trường tốt kéo giá nhà lên; ở nước ngoài là giá nhà cao kéo theo trường tốt."),
         F(4, "Câu ba: 中国学区房的房价为什么会水涨船高？ Vì sao giá nhà khu trường tốt ở Trung Quốc cứ nước lên thuyền lên?"),
         F(5, "Đáp án: 因为太多人想让孩子赢在起跑线上，都在所属学区买房。 Vì quá nhiều người muốn con thắng từ vạch xuất phát, ai cũng mua nhà trong khu tuyển sinh của trường.")])

add("bullets", section="Đọc hiểu 课文理解", title="Câu hỏi đọc hiểu (2)", reveal=True, size=33,
    items=["(4) 在国外，怎么区分好学区和坏学区？",
           "Đáp án: 核心在于生源，要看旁边是富人多还是穷人多。",
           "(5) 为什么国外没有那么多“砸锅卖铁”买学区房的故事？",
           "Đáp án: 一是国外没有户口户籍的概念，租房也能让孩子上公立学校；二是富人习惯送孩子去有宿舍的私立学校或贵族学校。",
           "(6) 国外“真正的学区房”指的是什么？那里的房价为什么高？",
           "Đáp án: 指名牌大学周边的房子。一则学生多、宿舍少，要租房；二则企业到周边设立分支机构，精英群体多。"],
    say=[F(0, "Câu bốn: 在国外，怎么区分好学区和坏学区？ Ở nước ngoài, phân biệt khu trường tốt và kém thế nào?"),
         F(1, "Đáp án: 核心在于生源，要看旁边是富人多还是穷人多。 Cốt lõi là nguồn học sinh: xem xung quanh người giàu nhiều hay người nghèo nhiều."),
         F(2, "Câu năm: 为什么国外没有那么多砸锅卖铁买学区房的故事？ Vì sao ở nước ngoài không có nhiều chuyện dốc hết gia sản mua nhà gần trường?"),
         F(3, "Đáp án: 一是国外没有户口户籍的概念，租房也能让孩子上公立学校；二是富人习惯送孩子去有宿舍的私立学校或贵族学校。 Một là không có hộ khẩu, thuê nhà cũng được học trường công; hai là người giàu quen gửi con vào trường tư hoặc trường quý tộc có ký túc xá."),
         F(4, "Câu sáu: 国外真正的学区房指的是什么？那里的房价为什么高？ Nhà khu trường tốt thực sự ở nước ngoài là gì? Vì sao giá ở đó cao?"),
         F(5, "Đáp án: 指名牌大学周边的房子。一则学生多、宿舍少，要租房；二则企业到周边设立分支机构，精英群体多。 Là nhà quanh các trường đại học danh tiếng: một là sinh viên đông mà ký túc xá ít, phải thuê nhà; hai là doanh nghiệp đến lập chi nhánh, tầng lớp tinh hoa đông.")])

# ======================= MẪU CÂU TRỌNG ĐIỂM =======================
add("bullets", chapter="Mẫu câu: 不尽然 · 何 · 乃至 · 越发", section="Mẫu câu 重点句型", title="1. 不尽然 bù jìnrán – không hẳn như vậy", size=34,
    items=["Không nhất định như thế, không hoàn toàn như vậy – phản bác nhẹ nhàng một ý kiến phổ biến",
           "Thường đứng sau 其实 · 也 · 但也: 其实不尽然 / 也不尽然",
           "学区房到底是不是中国特色呢？其实不尽然。",
           "人们都说“江山易改，本性难移”，但也不尽然！受环境影响，人的性格也会有变化。",
           "都说做生意能赚钱，也不尽然，亏本的也大有人在。"],
    say=["Bây giờ chúng ta sang phần mẫu câu và từ trọng điểm, 重点句型与词汇. Bài này có mười một điểm.",
         F(0, "Điểm thứ nhất: 不尽然. Nghĩa là không nhất định như thế, không hoàn toàn như vậy. Ta dùng nó khi muốn phản bác nhẹ nhàng một ý kiến mà nhiều người cho là đúng."),
         F(1, "不尽然 thường đứng sau 其实, 也 hoặc 但也, tạo thành 其实不尽然, thực ra không hẳn vậy; 也不尽然, cũng không hẳn vậy."),
         F(2, "Ví dụ một, trong bài khóa: 学区房到底是不是中国特色呢？其实不尽然。 Nhà khu trường tốt có phải đặc sản Trung Quốc không? Thực ra không hẳn vậy."),
         F(3, "Ví dụ hai: 人们都说江山易改，本性难移，但也不尽然！受环境影响，人的性格也会有变化。 Người ta nói giang sơn dễ đổi, bản tính khó dời, nhưng cũng không hẳn vậy! Chịu ảnh hưởng của môi trường, tính cách con người cũng sẽ thay đổi."),
         F(4, "Ví dụ ba: 都说做生意能赚钱，也不尽然，亏本的也大有人在。 Ai cũng nói làm ăn kiếm được tiền, cũng không hẳn vậy, người lỗ vốn cũng nhiều lắm. 大有人在 là có rất nhiều người như thế.")])

add("bullets", section="Mẫu câu 重点句型", title="2. 何 hé – (văn viết) gì, nào", size=36,
    items=["Đại từ nghi vấn văn viết, nghĩa là 什么; hay gặp: 有何 · 何时 · 何地 · 何人 · 何处",
           "中国的学区房和外国的学区房到底有何差别呢？",
           "我这样日复一日躺在病床上，到底何时是尽头啊！",
           "不管你有何疑问，都可以到办公室找我。"],
    say=["Điểm thứ hai: 何.",
         F(0, "何 là đại từ nghi vấn văn viết, nghĩa là cái gì, giống 什么. Chữ này Hán Việt là hà, như trong câu hà cớ gì. Những cụm hay gặp: 有何, có gì; 何时, khi nào; 何地, ở đâu; 何人, ai; 何处, nơi nào."),
         F(1, "Ví dụ một, trong bài khóa: 中国的学区房和外国的学区房到底有何差别呢？ Nhà khu trường tốt ở Trung Quốc và nước ngoài rốt cuộc có gì khác nhau?"),
         F(2, "Ví dụ hai: 我这样日复一日躺在病床上，到底何时是尽头啊！ Tôi cứ ngày này qua ngày khác nằm trên giường bệnh thế này, rốt cuộc đến bao giờ mới hết đây! 日复一日 là ngày này qua ngày khác."),
         F(3, "Ví dụ ba: 不管你有何疑问，都可以到办公室找我。 Dù bạn có thắc mắc gì, đều có thể đến văn phòng tìm tôi.")])

add("bullets", section="Mẫu câu 重点句型", title="3. ……，乃至（于）…… – …, thậm chí…", size=34,
    items=["Liên từ văn viết, nối thành phần tăng tiến (= 甚至): phần sau 乃至 có mức độ, phạm vi cao hơn",
           "国内有省重点、市重点、区重点，这些学校可能十几年前乃至一百年前就有了。",
           "他的一举一动，乃至脸色、眼神，都被别人看得清清楚楚。",
           "达·芬奇擅长绘画、雕刻，精通数学、生物学、物理学，乃至天文学等学科，是人类历史上少见的全才。"],
    say=["Điểm thứ ba: 乃至, cũng nói 乃至于.",
         F(0, "乃至 là liên từ văn viết, nghĩa là thậm chí, cho đến cả, giống 甚至. Phần đứng sau 乃至 có mức độ hoặc phạm vi cao hơn phần đứng trước."),
         F(1, "Ví dụ một, trong bài khóa: 这些学校可能十几年前乃至一百年前就有了。 Những trường này có thể đã có từ mười mấy năm, thậm chí một trăm năm trước."),
         F(2, "Ví dụ hai: 他的一举一动，乃至脸色、眼神，都被别人看得清清楚楚。 Từng cử chỉ, thậm chí cả sắc mặt, ánh mắt của anh ấy, đều bị người khác nhìn rõ mồn một."),
         F(3, "Ví dụ ba: 达芬奇擅长绘画、雕刻，精通数学、生物学、物理学，乃至天文学等学科，是人类历史上少见的全才。 Leonardo da Vinci giỏi hội họa, điêu khắc, tinh thông toán học, sinh học, vật lý học, thậm chí cả thiên văn học, là thiên tài toàn năng hiếm có trong lịch sử nhân loại.")])

add("bullets", section="Mẫu câu 重点句型", title="4. 越发 yuèfā – càng thêm", size=34,
    items=["Phó từ mức độ: càng thêm, mức độ sâu hơn so với trước (tác dụng giống 越……越……, 越来越)",
           "Thường có nguyên nhân phía trước: (因为/使/让)……，……越发 + tính từ/động từ tâm lý",
           "一开始这些学校旁边是没有那么多房子的，就因为师资力量雄厚，使周边的房子越发吃香。",
           "听到这一激动人心的消息，同学们越发有干劲了。",
           "当今社会，职场竞争越来越激烈，这也让人们越发感到焦虑不安。"],
    say=["Điểm thứ tư: phó từ 越发.",
         F(0, "越发 là phó từ mức độ, nghĩa là càng thêm, chỉ mức độ sâu hơn so với trước. Sách nói tác dụng của nó giống 越……越…… và 越来越."),
         F(1, "Trong câu, phía trước thường nêu nguyên nhân, như 因为，使，让; phía sau 越发 là tính từ hoặc động từ tâm lý."),
         F(2, "Ví dụ một, trong bài khóa: 就因为师资力量雄厚，使周边的房子越发吃香。 Chỉ vì đội ngũ giáo viên hùng hậu mà nhà xung quanh càng được săn đón."),
         F(3, "Ví dụ hai: 听到这一激动人心的消息，同学们越发有干劲了。 Nghe tin vui phấn khởi ấy, các bạn học càng hăng hái hơn. 干劲 là sự hăng hái làm việc."),
         F(4, "Ví dụ ba: 当今社会，职场竞争越来越激烈，这也让人们越发感到焦虑不安。 Xã hội ngày nay cạnh tranh nơi công sở ngày càng gay gắt, điều đó khiến người ta càng cảm thấy lo âu bất an. Câu này dùng cả 越来越 lẫn 越发, các bạn để ý nhé.")])

add("bullets", chapter="Mẫu câu: 何以见得 · 不妨 · 话又说回来", section="Mẫu câu 重点句型", title="5. 何以见得 héyǐ jiàndé – lấy gì mà biết?", size=34,
    items=["Lấy gì mà biết, căn cứ vào đâu mà khẳng định như vậy? – giọng hỏi vặn, đòi bằng chứng",
           "Dùng để tự đặt câu hỏi dẫn vào phần chứng minh, hoặc để chất vấn người khác",
           "中国的学区房是好学区带动了高房价，而外国的学区房是高房价带动了好学区。何以见得呢？",
           "你说你把我当真正的朋友，但何以见得？你骗了我不止一次啊！",
           "你为什么那么怀疑他，何以见得这件事就是他做的呢？"],
    say=["Điểm thứ năm: 何以见得.",
         F(0, "何以见得 nghĩa là lấy gì mà biết được, căn cứ vào đâu mà khẳng định như vậy. 何以 là văn viết của 凭什么, 见得 là thấy được. Câu này mang giọng hỏi vặn, đòi bằng chứng."),
         F(1, "Có hai cách dùng: tự đặt câu hỏi để dẫn vào phần chứng minh, như trong bài khóa; hoặc chất vấn người khác."),
         F(2, "Ví dụ một, trong bài khóa: 中国的学区房是好学区带动了高房价，而外国的学区房是高房价带动了好学区。何以见得呢？ Lấy gì mà biết được? Sau đó tác giả mới đưa ra lập luận."),
         F(3, "Ví dụ hai: 你说你把我当真正的朋友，但何以见得？你骗了我不止一次啊！ Cậu nói coi tôi là bạn thật sự, nhưng lấy gì chứng minh? Cậu đã lừa tôi không chỉ một lần rồi!"),
         F(4, "Ví dụ ba: 你为什么那么怀疑他，何以见得这件事就是他做的呢？ Sao cậu nghi anh ấy đến vậy, căn cứ vào đâu mà nói chuyện này là do anh ấy làm?")])

add("bullets", section="Mẫu câu 重点句型", title="6. 不妨 bùfáng – cứ thử, chẳng ngại gì", size=36,
    items=["Phó từ ngữ khí: có thể thử làm, sai cũng không sao – đưa ra gợi ý, lời khuyên nhẹ nhàng",
           "我们不妨来看看这些学区房的来历……",
           "据说这个药效果很好，你不妨试一试。",
           "同学之间有什么意见不妨当面提出来，不要在背后议论。"],
    say=["Điểm thứ sáu: 不妨.",
         F(0, "不妨 là phó từ ngữ khí, nghĩa là có thể thử làm, làm sai cũng chẳng sao. Ta dùng nó để đưa ra gợi ý, lời khuyên một cách nhẹ nhàng, không ép buộc."),
         F(1, "Ví dụ một, trong bài khóa: 我们不妨来看看这些学区房的来历。 Chúng ta thử xem lai lịch của những căn nhà này."),
         F(2, "Ví dụ hai: 据说这个药效果很好，你不妨试一试。 Nghe nói thuốc này hiệu quả lắm, cậu cứ thử xem."),
         F(3, "Ví dụ ba: 同学之间有什么意见不妨当面提出来，不要在背后议论。 Giữa bạn học với nhau có ý kiến gì thì cứ nói thẳng trước mặt, đừng bàn tán sau lưng.")])

add("compare", section="Mẫu câu 重点句型", title="Phân biệt 不妨 và 何必",
    common="Đều dùng để khuyên, nhưng hướng ngược nhau (bài tập 2 có câu kiểm tra điểm này)",
    cols=[{"head": "不妨",
           "lines": ["Khuyên NÊN thử làm: cứ làm đi, chẳng sao đâu",
                     "Đúng: 他最近没有时间，你不妨派别人去出差。",
                     "Đúng: 这件事你不妨问问老师。"]},
          {"head": "何必",
           "lines": ["Hỏi vặn: hà tất, cần gì phải – ý là KHÔNG cần làm",
                     "Đúng: 一点小事，何必生气呢？",
                     "Sai: 他最近没有时间，你何必派别人去出差。"]}],
    say=["Bài tập hai của sách có một câu chọn giữa 何，何必，不妨，未免. Vì vậy chúng ta phân biệt 不妨 và 何必.",
         F(0, "不妨 khuyên người khác nên thử làm một việc: cứ làm đi, chẳng sao đâu. Ví dụ: 他最近没有时间，你不妨派别人去出差。 Dạo này anh ấy không có thời gian, cậu cứ cử người khác đi công tác. Hoặc: 这件事你不妨问问老师, chuyện này cậu cứ thử hỏi thầy xem."),
         F(1, "Còn 何必 là câu hỏi vặn, nghĩa là hà tất, cần gì phải, tức là không cần làm. Ví dụ: 一点小事，何必生气呢？ Chuyện nhỏ thôi mà, cần gì phải tức giận?"),
         F(1, "Vì vậy câu 他最近没有时间，你何必派别人去出差 là sai: người nói muốn khuyên nên cử người khác đi, chứ không phải bảo đừng cử. Mẹo nhớ: 不妨, không có gì cản trở, nên cứ làm; 何必, hà tất, nên không cần làm.")])

add("bullets", section="Mẫu câu 重点句型", title="7. （不过/但/可是）话又说回来 – nói đi cũng phải nói lại", size=33,
    items=["Khẩu ngữ: chuyển ý, nhìn vấn đề từ góc độ, lập trường ngược lại",
           "话又说回来，因为国外是没有户口户籍这个概念的，所以很多人不用在那里买房。",
           "虽然你不在乎别人在背后说什么，但是话又说回来，人言可畏，你还是小心为好。",
           "独身主义者现在越来越多，他们享受自由，可是话又说回来，一个人生活会不会孤独呢？"],
    say=["Điểm thứ bảy: 话又说回来, thường đi sau 不过，但 hoặc 可是.",
         F(0, "Đây là cách nói khẩu ngữ dùng để chuyển ý, xem xét vấn đề từ góc độ, lập trường ngược lại. Tiếng Việt có câu tương đương rất hay: nói đi cũng phải nói lại."),
         F(1, "Ví dụ một, trong bài khóa: 话又说回来，因为国外是没有户口户籍这个概念的，所以很多人不用在那里买房。 Nói đi cũng phải nói lại, vì nước ngoài không có hộ khẩu nên nhiều người không cần mua nhà."),
         F(2, "Ví dụ hai: 虽然你不在乎别人在背后说什么，但是话又说回来，人言可畏，你还是小心为好。 Tuy cậu không để ý người khác nói gì sau lưng, nhưng nói đi cũng phải nói lại, lời đời đáng sợ, cậu vẫn nên cẩn thận thì hơn. 人言可畏 là lời thiên hạ đáng sợ."),
         F(3, "Ví dụ ba: 独身主义者现在越来越多，他们享受自由，可是话又说回来，一个人生活会不会孤独呢？ Người chủ trương sống độc thân ngày càng nhiều, họ tận hưởng tự do, nhưng nói đi cũng phải nói lại, sống một mình liệu có cô đơn không?")])

add("bullets", chapter="Mẫu câu: 区别在于 · 脱胎于 · 一则…二则 · 如此一来", section="Mẫu câu 重点句型", title="8. 区别在于 + N / câu – khác biệt nằm ở…", size=36,
    items=["Chỉ ra điểm khác biệt; cùng kiểu với 核心在于 · 关键在于 · 问题在于",
           "那第二个区别在哪儿呢？第二个区别在于私立学校。",
           "人和动物的重要区别在于人能够制造和使用劳动工具。",
           "私立学校和公立学校的区别在于资金来源不同。"],
    say=["Điểm thứ tám: 区别在于, theo sau là danh từ hoặc một câu.",
         F(0, "区别在于 nghĩa là sự khác biệt nằm ở. Cùng kiểu với nó có 核心在于, cốt lõi nằm ở, như 核心在于生源 trong bài; 关键在于, mấu chốt nằm ở; 问题在于, vấn đề là ở chỗ. Đây là những cụm rất hữu ích khi viết bài so sánh."),
         F(1, "Ví dụ một, trong bài khóa: 那第二个区别在哪儿呢？第二个区别在于私立学校。 Khác biệt thứ hai nằm ở đâu? Nằm ở trường tư thục."),
         F(2, "Ví dụ hai: 人和动物的重要区别在于人能够制造和使用劳动工具。 Khác biệt quan trọng giữa người và động vật là con người biết chế tạo và sử dụng công cụ lao động."),
         F(3, "Ví dụ ba: 私立学校和公立学校的区别在于资金来源不同。 Khác biệt giữa trường tư và trường công nằm ở nguồn kinh phí khác nhau.")])

add("bullets", section="Mẫu câu 重点句型", title="9. 脱胎于 + N – thoát thai từ…, hình thành từ…", size=36,
    items=["Ví một sự vật được thai nghén, biến đổi từ một sự vật khác mà thành",
           "而私立学校呢，又是脱胎于贵族学校的。",
           "我们现今能看到的京剧剧目，有很多都脱胎于昆曲。",
           "这种技术脱胎于专业相机，让人们用手机也可以随手抓拍。"],
    say=["Điểm thứ chín: 脱胎于.",
         F(0, "脱胎 nghĩa đen là thoát khỏi thai mẹ, nghĩa bóng là một sự vật được thai nghén, biến đổi từ một sự vật khác mà thành. 脱胎于 cộng danh từ là hình thành từ cái gì. Tiếng Việt cũng nói thoát thai từ."),
         F(1, "Ví dụ một, trong bài khóa: 而私立学校呢，又是脱胎于贵族学校的。 Mà trường tư thì lại hình thành từ trường quý tộc."),
         F(2, "Ví dụ hai: 我们现今能看到的京剧剧目，有很多都脱胎于昆曲。 Những vở Kinh kịch chúng ta xem được ngày nay, có rất nhiều vở thoát thai từ Côn khúc. 昆曲 là một loại hình hí khúc cổ của Trung Quốc."),
         F(3, "Ví dụ ba: 这种技术脱胎于专业相机，让人们用手机也可以随手抓拍。 Công nghệ này phát triển từ máy ảnh chuyên nghiệp, giúp mọi người dùng điện thoại cũng có thể chụp nhanh tiện tay.")])

add("bullets", section="Mẫu câu 重点句型", title="10. 一则……，二则…… – một là…, hai là…", size=33,
    items=["Liệt kê nguyên nhân, lý do (văn viết); có thể thêm 三则……",
           "一则是因为优质的大学，往往会吸引更多的优秀学生……；二则是这些享有盛誉的大学，会吸引更多的企业去周边设立分支机构。",
           "乡村学校办学条件相对较差，一则专业教师人数不足，二则教学设备比较落后。",
           "夏天空调温度设置26度，一则不容易得空调病，二则节约能源。"],
    say=["Điểm thứ mười: 一则……，二则…….",
         F(0, "Mẫu này nghĩa là một là…, hai là…, dùng để liệt kê nguyên nhân, lý do, mang màu sắc văn viết. Nếu có ba lý do, ta thêm 三则. Nó gần với 一来……，二来…… mà các bạn đã gặp."),
         F(1, "Ví dụ một, trong bài khóa: 一则是因为优质的大学，往往会吸引更多的优秀学生；二则是这些享有盛誉的大学，会吸引更多的企业去周边设立分支机构。"),
         F(2, "Ví dụ hai: 乡村学校办学条件相对较差，一则专业教师人数不足，二则教学设备比较落后。 Điều kiện dạy học ở trường nông thôn tương đối kém: một là thiếu giáo viên chuyên môn, hai là thiết bị dạy học khá lạc hậu."),
         F(3, "Ví dụ ba: 夏天空调温度设置二十六度，一则不容易得空调病，二则节约能源。 Mùa hè đặt điều hòa ở hai mươi sáu độ: một là khó mắc bệnh điều hòa, hai là tiết kiệm năng lượng.")])

add("bullets", section="Mẫu câu 重点句型", title="11. 如此一来 – như vậy thì, như thế là", size=36,
    items=["= 这样一来: nối kết quả của điều vừa nói (thường là giả định hoặc dự đoán)",
           "如此一来，工作机会也就增加了。",
           "城市规划有助于缓解交通压力，如此一来，人们的出行会更加便利。",
           "现在很多数据都可以上传到网络，如此一来，可以保证数据的安全。"],
    say=["Điểm cuối cùng: 如此一来.",
         F(0, "如此一来 bằng 这样一来, nghĩa là như vậy thì, như thế là. Nó nối kết quả của điều vừa nói, thường dùng khi giả định hoặc dự đoán. 如此 là văn viết của 这样."),
         F(1, "Ví dụ một, trong bài khóa: 如此一来，工作机会也就增加了。 Như vậy, cơ hội việc làm cũng tăng lên."),
         F(2, "Ví dụ hai: 城市规划有助于缓解交通压力，如此一来，人们的出行会更加便利。 Quy hoạch đô thị giúp giảm áp lực giao thông, như thế việc đi lại của mọi người sẽ thuận tiện hơn."),
         F(3, "Ví dụ ba: 现在很多数据都可以上传到网络，如此一来，可以保证数据的安全。 Bây giờ nhiều dữ liệu có thể tải lên mạng, như vậy có thể bảo đảm an toàn dữ liệu.")])

# ======================= KẾT HỢP TỪ & THÀNH NGỮ =======================
add("bullets", chapter="Kết hợp từ & thành ngữ", section="Kết hợp từ 词语搭配", title="Kết hợp từ (1): 联手 · 圣地 · 雄厚", size=34,
    items=["## 联手 + V: ～合作 · ～打击 · ～打造",
           "最近社会上违法案件层出不穷，警民应该联手打击犯罪。",
           "## N + 圣地: 教育～ · 佛教～ · 艺术～ · 旅行～",
           "峨眉山位于中国四川省境内，是中外著名的旅游风景区和佛教圣地。",
           "## 雄厚: 实力～ · 资金～ · 国力～ · 警力～",
           "他们公司既有雄厚的资金，又拥有充足的货源，自然市场竞争力强。"],
    say=["Tiếp theo là phần 词语搭配, kết hợp từ.",
         F(0, "联手 đứng trước động từ: 联手合作, bắt tay hợp tác; 联手打击, cùng nhau trấn áp; 联手打造, cùng nhau xây dựng, như 强强联手打造了一个又一个学区 trong bài."),
         F(1, "Ví dụ: 最近社会上违法案件层出不穷，警民应该联手打击犯罪。 Gần đây các vụ phạm pháp xuất hiện liên tục, cảnh sát và người dân nên chung tay trấn áp tội phạm."),
         F(2, "圣地 đứng sau danh từ: 教育圣地，佛教圣地，艺术圣地，旅行圣地."),
         F(3, "Ví dụ: 峨眉山位于中国四川省境内，是中外著名的旅游风景区和佛教圣地。 Núi Nga Mi nằm trong tỉnh Tứ Xuyên, là khu du lịch và thánh địa Phật giáo nổi tiếng trong và ngoài nước."),
         F(4, "雄厚 đi với 实力，资金，国力，警力: thực lực, vốn, sức mạnh quốc gia, lực lượng cảnh sát hùng hậu."),
         F(5, "Ví dụ: 他们公司既有雄厚的资金，又拥有充足的货源，自然市场竞争力强。 Công ty họ vừa có vốn hùng hậu, vừa có nguồn hàng dồi dào, đương nhiên sức cạnh tranh trên thị trường rất mạnh.")])

add("bullets", section="Kết hợp từ 词语搭配", title="Kết hợp từ (2): 轮换 · 区分 · 享有", size=34,
    items=["## 轮换 + N: ～休息 · ～演出 · 定期～ · ～岗位",
           "新员工入职后，有一年的岗位轮换期。",
           "## 区分 + N: ～优劣 · 难以～ · ～不同 · ～等级",
           "我们不能只凭考试结果来区分学生优秀与否。",
           "## 享有 + N: ～盛名 · ～威望 · ～权利 · ～特权",
           "在中国，法律规定男女享有同等的权利。"],
    say=[F(0, "轮换 đi với 休息，演出，岗位, và cụm 定期轮换, luân chuyển định kỳ."),
         F(1, "Ví dụ: 新员工入职后，有一年的岗位轮换期。 Nhân viên mới sau khi vào làm có một năm luân chuyển vị trí."),
         F(2, "区分 đi với 优劣，不同，等级, và cụm 难以区分, khó phân biệt."),
         F(3, "Ví dụ: 我们不能只凭考试结果来区分学生优秀与否。 Chúng ta không thể chỉ dựa vào kết quả thi để phân biệt học sinh giỏi hay không. 与否 là hay không, văn viết."),
         F(4, "享有 đi với 盛名，威望，权利，特权: được hưởng danh tiếng, uy tín, quyền lợi, đặc quyền. Trong bài có 享有盛誉."),
         F(5, "Ví dụ: 在中国，法律规定男女享有同等的权利。 Ở Trung Quốc, pháp luật quy định nam nữ được hưởng quyền lợi như nhau.")])

add("bullets", section="Thành ngữ 成语", title="Thành ngữ (1): 茶余饭后 · 层出不穷 · 众所周知 · 水涨船高", size=33,
    items=["## 茶余饭后 – lúc trà dư tửu hậu, lúc rảnh rỗi",
           "这几年，教育改革成了市民茶余饭后的热门话题。",
           "## 层出不穷 – liên tục xuất hiện, không dứt (层: lặp lại; 穷: hết)",
           "在改革发展新时期，新情况、新问题层出不穷。",
           "## 众所周知 – ai ai cũng biết",
           "众所周知，文化是没有国界的，许多外国朋友慕名来学习中国功夫。",
           "## 水涨船高 – nước lên thuyền lên: cái nền tăng thì cái dựa vào nó cũng tăng",
           "随着原材料涨价，我们的产品价格也水涨船高。"],
    say=["Bài này có bảy thành ngữ, rất nhiều thành ngữ đắt giá.",
         F(0, "茶余饭后: sau bữa trà, sau bữa cơm, chỉ lúc nghỉ ngơi rảnh rỗi. Tiếng Việt có câu tương tự: trà dư tửu hậu."),
         F(1, "Ví dụ: 这几年，教育改革成了市民茶余饭后的热门话题。 Mấy năm nay, cải cách giáo dục trở thành đề tài nóng lúc rảnh rỗi của người dân thành phố."),
         F(2, "层出不穷: chữ 层 là lặp lại, chữ 穷 là hết. Liên tục xuất hiện, không bao giờ hết."),
         F(3, "Ví dụ: 在改革发展新时期，新情况、新问题层出不穷。 Trong thời kỳ cải cách phát triển mới, tình hình mới, vấn đề mới liên tục nảy sinh."),
         F(4, "众所周知: điều mà mọi người đều biết. Thường đứng đầu câu, có dấu phẩy phía sau."),
         F(5, "Ví dụ: 众所周知，文化是没有国界的，许多外国朋友慕名来学习中国功夫。 Ai cũng biết, văn hóa không có biên giới, nhiều bạn bè nước ngoài vì ngưỡng mộ mà đến học võ thuật Trung Quốc."),
         F(6, "水涨船高: nước dâng lên thì thuyền cũng nổi lên. Ví sự vật tăng lên theo cái nền mà nó dựa vào."),
         F(7, "Ví dụ: 随着原材料涨价，我们的产品价格也水涨船高。 Theo đà tăng giá của nguyên liệu, giá sản phẩm của chúng tôi cũng tăng theo.")])

add("bullets", section="Thành ngữ 成语", title="Thành ngữ (2): 相差无几 · 自然而然 · 砸锅卖铁", size=34,
    items=["## 相差无几 – chênh lệch không đáng kể (无几: chẳng bao nhiêu)",
           "这两种酒的味道相差无几，我喝不出区别。",
           "## 自然而然 – tự nhiên mà thành, tất yếu như thế",
           "写毛笔字没有什么捷径可言，经过一段时间苦练，字自然而然就能写好了。",
           "## 砸锅卖铁 – đập nồi bán sắt vụn: dốc hết tài sản, không chừa đường lui",
           "中国人相信知识改变命运，就是砸锅卖铁也会供孩子上学。"],
    say=[F(0, "相差无几: 相差 là chênh lệch, 无几 là chẳng bao nhiêu. Hai bên chẳng khác nhau là mấy."),
         F(1, "Ví dụ: 这两种酒的味道相差无几，我喝不出区别。 Vị của hai loại rượu này gần như nhau, tôi uống không phân biệt được."),
         F(2, "自然而然: cứ để tự nhiên phát triển thì tất yếu sẽ như thế."),
         F(3, "Ví dụ: 写毛笔字没有什么捷径可言，经过一段时间苦练，字自然而然就能写好了。 Viết chữ bằng bút lông chẳng có đường tắt nào, khổ luyện một thời gian, chữ tự nhiên sẽ đẹp."),
         F(4, "砸锅卖铁: đập cả nồi đi bán sắt vụn, nghĩa là nghèo đến cùng cực, không chừa đường lui; cũng ví việc đem hết tất cả ra. Tiếng Việt có thể nói bán nhà bán cửa, bán cả gia tài."),
         F(5, "Ví dụ: 中国人相信知识改变命运，就是砸锅卖铁也会供孩子上学。 Người Trung Quốc tin tri thức thay đổi số phận, dù có phải bán cả gia tài cũng nuôi con ăn học. 供孩子上学 là nuôi con ăn học.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 趁热打铁", title="Bài tập 1: Chọn từ điền vào chỗ trống (1)", reveal=True, size=36,
    items=["## Từ cho sẵn: 层出不穷 · 水涨船高 · 茶余饭后 · 雄厚 · 发源于 · 相差无几",
           "(1) 长江___青藏高原，一路向东，最终流入东海。",
           "Đáp án: 发源于",
           "(2) 最新调查显示，新政府支持率与上一届___。",
           "Đáp án: 相差无几",
           "(3) 眼下的电视节目新创意___，这样才有看头。",
           "Đáp án: 层出不穷"],
    say=["Bây giờ là phần luyện tập của sách, 趁热打铁. Bài tập một: chọn từ cho sẵn điền vào chỗ trống.",
         F(0, "Có sáu từ: 层出不穷，水涨船高，茶余饭后，雄厚，发源于，相差无几."),
         F(1, "Câu một: 长江什么青藏高原，一路向东，最终流入东海。 Sông Trường Giang… cao nguyên Thanh Tạng, chảy một mạch về phía đông, cuối cùng đổ ra biển Đông Hải. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 发源于. 长江发源于青藏高原, sông Trường Giang bắt nguồn từ cao nguyên Thanh Tạng."),
         F(3, "Câu hai: 最新调查显示，新政府支持率与上一届什么。 Khảo sát mới nhất cho thấy tỷ lệ ủng hộ chính phủ mới so với khóa trước…."),
         F(4, "Đáp án: 相差无几, gần như ngang nhau. Mẫu 与……相差无几, chênh lệch không đáng kể so với…."),
         F(5, "Câu ba: 眼下的电视节目新创意什么，这样才有看头。 Chương trình truyền hình bây giờ ý tưởng mới…, như vậy mới đáng xem."),
         F(6, "Đáp án: 层出不穷. 新创意层出不穷, ý tưởng mới liên tục xuất hiện. 有看头 là đáng xem.")])

add("bullets", section="Luyện tập 趁热打铁", title="Bài tập 1: Chọn từ điền vào chỗ trống (2)", reveal=True, size=36,
    items=["## Từ cho sẵn: 层出不穷 · 水涨船高 · 茶余饭后 · 雄厚 · 发源于 · 相差无几",
           "(4) 中国乒乓球队凭借其___的整体实力，取得了优异的成绩。",
           "Đáp án: 雄厚",
           "(5) 人们经常把演员们的八卦，当作___的谈资。",
           "Đáp án: 茶余饭后",
           "(6) 由于一线城市房价飙升，周边二线城市的商品房价格也跟着___。",
           "Đáp án: 水涨船高"],
    say=[F(1, "Câu bốn: 中国乒乓球队凭借其什么的整体实力，取得了优异的成绩。 Đội bóng bàn Trung Quốc dựa vào thực lực tổng thể… của mình, đã giành thành tích xuất sắc."),
         F(2, "Đáp án: 雄厚. 雄厚的整体实力, thực lực tổng thể hùng hậu. Đây chính là kết hợp 实力雄厚."),
         F(3, "Câu năm: 人们经常把演员们的八卦，当作什么的谈资。 Người ta thường coi chuyện đời tư của diễn viên là đề tài bàn tán…. 八卦 là chuyện phiếm, chuyện đời tư."),
         F(4, "Đáp án: 茶余饭后. 茶余饭后的谈资, đúng như câu đầu bài khóa."),
         F(5, "Câu sáu: 由于一线城市房价飙升，周边二线城市的商品房价格也跟着什么。 Do giá nhà ở các thành phố hạng nhất tăng vọt, giá nhà thương mại ở các thành phố hạng hai lân cận cũng theo đó…."),
         F(6, "Đáp án: 水涨船高. 跟着水涨船高, tăng theo. 飙升 là tăng vọt.")])

add("bullets", section="Luyện tập 趁热打铁", title="Bài tập 2: Chọn đáp án đúng", reveal=True, size=32,
    items=["(1) 小敏的病已经完全康复了，人也稍稍胖了一点，与生病以前（ ）。\nA.相差无几  B.天差地别  C.一模一样  D.天壤之别",
           "Đáp án: A – 相差无几 (chỉ hơi béo lên nên không thể 一模一样)",
           "(2) 导师对学生的批评是严厉了些，但（ ），他的论文中确实有许多错误，批评也是为了帮助他进步。\nA.说来话长  B.二话不说  C.话又说回来  D.换句话说",
           "Đáp án: C – 话又说回来",
           "(3) 中亚地区是古文明（ ）地之一，对世界文明发展影响巨大。\nA.源头  B.发源  C.源于  D.来源",
           "Đáp án: B – 发源地",
           "(4) 他最近没有时间，你（ ）派别人去出差。\nA.何  B.何必  C.不妨  D.未免",
           "Đáp án: C – 不妨"],
    say=["Bài tập hai: chọn một đáp án đúng.",
         F(0, "Câu một: 小敏的病已经完全康复了，人也稍稍胖了一点，与生病以前什么。 Tiểu Mẫn đã khỏi bệnh hoàn toàn, người cũng hơi béo lên một chút, so với trước khi ốm thì…. Lựa chọn: 相差无几，天差地别，一模一样，天壤之别."),
         F(1, "Đáp án: A, 相差无几, chẳng khác bao nhiêu. Vì cô ấy hơi béo lên một chút nên không thể nói 一模一样, giống hệt; còn 天差地别 và 天壤之别 là khác nhau một trời một vực, ngược nghĩa."),
         F(2, "Câu hai: 导师对学生的批评是严厉了些，但什么，他的论文中确实有许多错误，批评也是为了帮助他进步。 Thầy hướng dẫn phê bình sinh viên hơi nghiêm khắc, nhưng…, luận văn của cậu ấy đúng là có nhiều lỗi, phê bình cũng là để giúp cậu ấy tiến bộ. Lựa chọn: 说来话长，二话不说，话又说回来，换句话说."),
         F(3, "Đáp án: C, 话又说回来, nói đi cũng phải nói lại. 说来话长 là chuyện dài lắm; 二话不说 là không nói hai lời; 换句话说 là nói cách khác."),
         F(4, "Câu ba: 中亚地区是古文明什么地之一，对世界文明发展影响巨大。 Khu vực Trung Á là một trong những… của văn minh cổ đại, có ảnh hưởng to lớn đến sự phát triển của văn minh thế giới. Lựa chọn: 源头，发源，源于，来源."),
         F(5, "Đáp án: B, 发源, ghép với chữ 地 thành 发源地, nơi khởi nguồn."),
         F(6, "Câu bốn: 他最近没有时间，你什么派别人去出差。 Lựa chọn: 何，何必，不妨，未免."),
         F(7, "Đáp án: C, 不妨, đúng như chúng ta vừa phân biệt: 你不妨派别人去出差, cậu cứ cử người khác đi công tác.")])

add("bullets", section="Luyện tập 趁热打铁", title="Bài tập 3: Dùng từ cho sẵn trả lời câu hỏi (1)", reveal=True, size=33,
    items=["(1) 中国的学区房是怎么涨价的？（……如此一来）",
           "Đáp án gợi ý: 好学校师资力量雄厚，家长们都想让孩子进这些学校，纷纷在学区里买房，如此一来，学区房的价格就水涨船高了。",
           "(2) 中国和外国的学区房有何区别？（区别在于……）",
           "Đáp án gợi ý: 区别在于因果关系不同：中国是好学区带动了高房价，外国是高房价带动了好学区。",
           "(3) 为何国外的学区指的是大学？（一则……二则……）",
           "Đáp án gợi ý: 一则名牌大学宿舍不够，很多学生要在周边租房；二则大学会吸引企业在周边设立分支机构，带来更多工作机会。"],
    say=["Bài tập ba: dùng từ và mẫu câu cho sẵn để trả lời câu hỏi. Các bạn hãy tự trả lời trước, rồi nghe đáp án gợi ý.",
         F(0, "Câu một, dùng 如此一来: 中国的学区房是怎么涨价的？ Nhà khu trường tốt ở Trung Quốc tăng giá như thế nào?"),
         F(1, "Đáp án gợi ý: 好学校师资力量雄厚，家长们都想让孩子进这些学校，纷纷在学区里买房，如此一来，学区房的价格就水涨船高了。 Trường tốt có giáo viên giỏi, phụ huynh đều muốn con vào, đổ xô mua nhà trong khu tuyển sinh, như thế giá nhà cứ nước lên thuyền lên."),
         F(2, "Câu hai, dùng 区别在于: 中国和外国的学区房有何区别？"),
         F(3, "Đáp án gợi ý: 区别在于因果关系不同：中国是好学区带动了高房价，外国是高房价带动了好学区。 Khác biệt nằm ở quan hệ nhân quả."),
         F(4, "Câu ba, dùng 一则……二则: 为何国外的学区指的是大学？ Vì sao ở nước ngoài khu trường tốt lại là trường đại học?"),
         F(5, "Đáp án gợi ý: 一则名牌大学宿舍不够，很多学生要在周边租房；二则大学会吸引企业在周边设立分支机构，带来更多工作机会。 Một là ký túc xá không đủ, sinh viên phải thuê nhà xung quanh; hai là trường thu hút doanh nghiệp lập chi nhánh, mang lại nhiều việc làm.")])

add("bullets", section="Luyện tập 趁热打铁", title="Bài tập 3: Dùng từ cho sẵn trả lời câu hỏi (2)", reveal=True, size=34,
    items=["(4) 你能解释一下私立学校的历史吗？（脱胎于……）",
           "Đáp án gợi ý: 国外的私立学校脱胎于贵族学校，过去主要是贵族子弟上学的地方，所以往往有宿舍，实行寄宿制度。",
           "(5) 好学区和学生成绩之间有必然联系吗？（不尽然）",
           "Đáp án gợi ý: 很多人认为上了好学区的学校成绩一定好，其实不尽然。成绩还取决于学生自己的努力和家庭教育。"],
    say=[F(0, "Câu bốn, dùng 脱胎于: 你能解释一下私立学校的历史吗？ Bạn có thể giải thích lịch sử của trường tư thục không?"),
         F(1, "Đáp án gợi ý: 国外的私立学校脱胎于贵族学校，过去主要是贵族子弟上学的地方，所以往往有宿舍，实行寄宿制度。 Trường tư ở nước ngoài hình thành từ trường quý tộc, trước kia chủ yếu là nơi con em quý tộc theo học, vì vậy thường có ký túc xá, áp dụng chế độ nội trú."),
         F(2, "Câu năm, dùng 不尽然: 好学区和学生成绩之间有必然联系吗？ Giữa khu trường tốt và thành tích học sinh có mối liên hệ tất yếu không?"),
         F(3, "Đáp án gợi ý: 很多人认为上了好学区的学校成绩一定好，其实不尽然。成绩还取决于学生自己的努力和家庭教育。 Nhiều người cho rằng học trường ở khu tốt thì thành tích nhất định tốt, thực ra không hẳn vậy. Thành tích còn phụ thuộc vào sự cố gắng của học sinh và giáo dục gia đình.")])

add("bullets", section="Luyện tập 趁热打铁", title="Bài tập 4: Chọn từ điền vào đoạn văn", reveal=True, size=33,
    items=["## Từ cho sẵn: 就读 · 越发 · 区分 · 如此一来 · 周边 · 享有 · 所属",
           "面对___严峻的学区房问题，部分地区政府及时出手，将对学区房进行大调整。首先是学生改为就近入学，在以往，有的小区距离学校仅有一路之隔，但因为不在学区而不能入学，新政策实行后，将以学校为单位，___多个小区的学生，都可以在此读书，___，学生就无须到更远的学校读书。二是尝试不再___户籍，租房与买房居民___同等的权利，租房人子女也可以___于区域内的公立学校，享受高质量的教育资源。",
           "Đáp án: 越发 · 周边 · 如此一来 · 区分 · 享有 · 就读 (thừa: 所属)"],
    say=["Bài tập bốn: chọn từ cho sẵn điền vào đoạn văn. Có bảy từ nhưng chỉ có sáu chỗ trống.",
         F(0, "Bảy từ là: 就读，越发，区分，如此一来，周边，享有，所属."),
         F(1, "Đoạn văn như sau: 面对什么严峻的学区房问题，部分地区政府及时出手，将对学区房进行大调整。首先是学生改为就近入学，在以往，有的小区距离学校仅有一路之隔，但因为不在学区而不能入学，新政策实行后，将以学校为单位，什么多个小区的学生，都可以在此读书，什么，学生就无须到更远的学校读书。二是尝试不再什么户籍，租房与买房居民什么同等的权利，租房人子女也可以什么于区域内的公立学校，享受高质量的教育资源。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 面对越发严峻的学区房问题；周边多个小区的学生；如此一来，学生就无须到更远的学校读书；不再区分户籍；享有同等的权利；就读于区域内的公立学校. Từ 所属 là từ thừa. Cả đoạn nghĩa là: Trước vấn đề nhà khu trường tốt ngày càng gay gắt, chính quyền một số nơi đã kịp thời ra tay điều chỉnh lớn. Thứ nhất, học sinh chuyển sang học trường gần nhà: trước đây có khu dân cư chỉ cách trường một con đường mà không được vào học vì không thuộc khu tuyển sinh; nay lấy trường làm đơn vị, học sinh của nhiều khu dân cư xung quanh đều được học ở đó. Thứ hai, thử không phân biệt hộ tịch nữa, người thuê nhà và người mua nhà được hưởng quyền như nhau, con em người thuê nhà cũng được học ở trường công lập trong khu vực.")])

# ======================= THẢO LUẬN =======================
add("bullets", chapter="Thảo luận", section="Thảo luận 讨论", title="Liên hệ Việt Nam: nhà gần trường điểm, học “trái tuyến”", size=36,
    items=["Tiểu học, THCS công lập ở Việt Nam tuyển sinh theo địa bàn cư trú (“đúng tuyến” / “trái tuyến”)",
           "Nhà gần trường nổi tiếng ở Hà Nội, TP.HCM đắt hơn hẳn – giống 好学区带动了高房价",
           "Có phụ huynh chuyển hộ khẩu, nhờ người quen để con học “trái tuyến” – giống 户口户籍 · 找门路",
           "Thử nói: 在越南，学区房的问题也不尽然……；话又说回来，……"],
    say=["Bây giờ chúng ta liên hệ với Việt Nam.",
         F(0, "Ở Việt Nam, các trường tiểu học và trung học cơ sở công lập cũng tuyển sinh theo địa bàn cư trú. Học sinh ở đúng địa bàn gọi là đúng tuyến; học ở trường ngoài địa bàn gọi là trái tuyến."),
         F(1, "Vì vậy, nhà gần một số trường nổi tiếng ở Hà Nội hay Thành phố Hồ Chí Minh thường đắt hơn hẳn. Đây chính là logic 好学区带动了高房价 của Trung Quốc."),
         F(2, "Cũng có phụ huynh chuyển hộ khẩu, hoặc nhờ người quen để con được học trái tuyến. Các bạn thấy không, rất giống chuyện 户口户籍 trong bài này và chuyện 找门路 ở bài trước."),
         F(3, "Các bạn hãy thử nói vài câu bằng tiếng Trung, ví dụ: 在越南，很多人觉得只有名校才能培养出好学生，其实不尽然。话又说回来，好学校的教育资源确实更多，家长们想让孩子进名校也是可以理解的。 Ở Việt Nam nhiều người nghĩ chỉ trường danh tiếng mới đào tạo được học sinh giỏi, thực ra không hẳn vậy. Nhưng nói đi cũng phải nói lại, trường tốt đúng là có nhiều tài nguyên hơn, phụ huynh muốn con vào trường tốt cũng dễ hiểu.")])

add("bullets", section="Thảo luận 讨论", title="Thảo luận: 学区房情结怎么破？", reveal=True, size=34,
    items=["(1) 如果你是家长，你愿意砸锅卖铁买学区房吗？为什么？",
           "Đáp án gợi ý: 我不愿意。好学区的学校不尽然适合每个孩子；与其砸锅卖铁，不如多花时间陪孩子，培养好的学习习惯。",
           "(2) 政府应该怎样给学区房降温？",
           "Đáp án gợi ý: 一则推行教师轮换制度，缩小学校之间的差距；二则实行就近入学，不再区分户籍。如此一来，学区房自然而然就会降温。"],
    say=["Cuối cùng, chúng ta trả lời câu hỏi ở tên bài: 学区房情结怎么破？ Làm sao gỡ bỏ nỗi ám ảnh này?",
         F(0, "Câu hỏi một: 如果你是家长，你愿意砸锅卖铁买学区房吗？为什么？ Nếu bạn là phụ huynh, bạn có sẵn lòng dốc hết gia tài mua nhà khu trường tốt không? Vì sao?"),
         F(1, "Gợi ý: 我不愿意。好学区的学校不尽然适合每个孩子；与其砸锅卖铁，不如多花时间陪孩子，培养好的学习习惯。 Tôi không muốn. Trường ở khu tốt chưa hẳn phù hợp với mọi đứa trẻ; thay vì bán cả gia tài, chi bằng dành nhiều thời gian bên con, giúp con có thói quen học tập tốt."),
         F(2, "Câu hỏi hai: 政府应该怎样给学区房降温？ Chính phủ nên làm gì để hạ nhiệt cơn sốt này? 降温 là hạ nhiệt."),
         F(3, "Gợi ý: 一则推行教师轮换制度，缩小学校之间的差距；二则实行就近入学，不再区分户籍。如此一来，学区房自然而然就会降温。 Một là thực hiện chế độ luân chuyển giáo viên, thu hẹp khoảng cách giữa các trường; hai là cho học sinh học trường gần nhà, không phân biệt hộ tịch. Như vậy, cơn sốt sẽ tự nhiên hạ nhiệt. Câu trả lời này dùng lại ba mẫu câu của bài: 一则……二则，如此一来，và thành ngữ 自然而然.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 1.2", size=34,
    items=["Từ vựng trọng tâm: 情结 · 不尽然 · 发源 · 联手 · 原本 · 乃至 · 师资 · 雄厚 · 越发 · 吃香 · 不妨 · 来历 · 区分 · 生源 · 户籍 · 就读 · 脱胎 · 享有盛誉 · 相应",
           "Mẫu câu (1): 其实不尽然 · 有何 · ……乃至…… · 越发 · 何以见得 · 不妨",
           "Mẫu câu (2): 话又说回来 · 区别在于 · 脱胎于 · 一则……二则…… · 如此一来",
           "Thành ngữ: 茶余饭后 · 层出不穷 · 众所周知 · 水涨船高 · 相差无几 · 自然而然 · 砸锅卖铁",
           "## Bài tập về nhà",
           "Viết đoạn văn khoảng 300 chữ so sánh “nhà gần trường tốt” ở Việt Nam và Trung Quốc, dùng 区别在于 · 一则……二则…… · 话又说回来"],
    say=["Chúng ta cùng tổng kết bài một chấm hai.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 情结，不尽然，发源，联手，原本，乃至，师资，雄厚，越发，吃香，不妨，来历，区分，生源，户籍，就读，脱胎，享有盛誉，相应."),
         F(1, "Về mẫu câu, nhóm một: 其实不尽然, phản bác nhẹ nhàng; 有何, văn viết của có gì; 乃至, thậm chí; 越发, càng thêm; 何以见得, lấy gì mà biết; 不妨, cứ thử."),
         F(2, "Nhóm hai: 话又说回来, nói đi cũng phải nói lại; 区别在于, khác biệt nằm ở; 脱胎于, hình thành từ; 一则……二则……, một là, hai là; và 如此一来, như vậy thì. Đây đều là những từ nối rất có ích khi viết văn so sánh, nghị luận."),
         F(3, "Bảy thành ngữ: 茶余饭后，层出不穷，众所周知，水涨船高，相差无几，自然而然，砸锅卖铁."),
         F(5, "Bài tập về nhà: hãy viết một đoạn văn khoảng ba trăm chữ, so sánh chuyện nhà gần trường tốt ở Việt Nam và ở Trung Quốc. Hãy dùng 区别在于 để nêu điểm khác, 一则……二则…… để giải thích nguyên nhân, và 话又说回来 để nhìn vấn đề từ phía ngược lại."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Bài sau, bài một chấm ba, là bài cuối cùng của Đơn vị một: “高考移民”动了谁的奶酪？ Di cư thi đại học đã động đến miếng pho mát của ai? Chúng ta sẽ tìm hiểu vì sao có những thí sinh chuyển hộ khẩu sang tỉnh khác để thi đại học, và vì sao điều đó bị coi là không công bằng. Sau bài đó còn có phần ôn tập cả đơn vị. Hẹn gặp lại các bạn. Chúc các bạn học tốt!"])

lesson = {
    "title": "顶石中文 – Bài 1.2: 学区房情结怎么破？ (Làm sao gỡ nỗi ám ảnh nhà gần trường tốt?)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"尽然": "进然",            # bù jìnrán
                    "地处": "地楚",            # dìchǔ
                    "相应": "相映",            # xiāngyìng
                    "相差": "相岔",            # xiāngchà
                    "水涨": "水掌",            # shuǐzhǎng
                    "当真正": "荡真正",        # dàng
                    "为好": "维好",            # wéihǎo
                    "干劲": "赣劲",            # gànjìn
                    "供孩子": "公孩子",        # gōng
                    "出差": "出拆",            # chūchāi
                    "差地别": "岔地别",        # tiānchà-dìbié
                    "一模一样": "一谋一样"},   # yīmú-yīyàng
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds12.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
