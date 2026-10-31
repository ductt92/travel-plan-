#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Thượng) – Bài 15 «山脉上的雕刻». Chạy để sinh bai15.json."""
import json
import os

TAG = "HSK 6 (Thượng) · Bài 15 · 山脉上的雕刻"
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
    zh="山脉上的雕刻", py="Shānmài shang de diāokè",
    vi="Bài 15: Các tác phẩm điêu khắc trên dãy núi",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Thượng.",
         "Hôm nay chúng ta học bài mười lăm: 山脉上的雕刻。 Nghĩa là: Các tác phẩm điêu khắc trên dãy núi.",
         "Bài này thuộc Chủ đề bốn, 走遍天下, Đi khắp thiên hạ. Tác phẩm điêu khắc ở đây không phải là tượng đá hay tượng gỗ, mà là những thửa ruộng bậc thang của người Hà Nhì, tiếng Trung gọi là 哈尼梯田, trên dãy núi Ai Lao ở miền nam tỉnh Vân Nam, Trung Quốc.",
         "Điều thú vị là dân tộc Hà Nhì cũng sống ở Việt Nam, tại Lai Châu, Lào Cai, Điện Biên; và con sông Hồng Hà trong bài chính là thượng nguồn sông Hồng của chúng ta. Ruộng bậc thang Hồng Hà của người Hà Nhì đã được công nhận là di sản văn hóa thế giới. Các bạn hãy thử nhớ đến ruộng bậc thang ở Mù Cang Chải hay Hoàng Su Phì khi học bài này nhé."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài khóa: ruộng bậc thang Hà Nhì (哈尼梯田) – kiệt tác của con người trên núi",
           "Nắm vững 47 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: phó từ 时而, phó từ 不禁, phó từ 无不",
           "Phân biệt hai động từ 拥有 và 具有",
           "Mở rộng: câu sai do thừa thành phần (成分冗余) và từ vựng về thiên nhiên"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa: vẻ đẹp của ruộng bậc thang Hà Nhì, lý do người dân chọn làm ruộng bậc thang, và giá trị của kỳ quan này."),
         F(1, "Thứ hai, nắm vững bốn mươi bảy từ mới. Bài này có rất nhiều từ miêu tả phong cảnh, như 壮丽，蔚蓝，漂浮，纵横，汹涌. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học ba phó từ: 时而, nghĩa là lúc thì, thỉnh thoảng; 不禁, nghĩa là không kìm được; và 无不, nghĩa là không cái nào không, tất cả đều."),
         F(3, "Thứ tư, phân biệt hai động từ đều có nghĩa là có: 拥有 và 具有."),
         F(4, "Thứ năm, phần mở rộng: nhận biết câu sai do thừa thành phần, tiếng Trung gọi là 成分冗余, và học thêm một số từ vựng về thiên nhiên."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Khởi động: Chọn hình phù hợp cho các từ", size=38,
    items=["(1) 森林 sēnlín – rừng → hình A: rừng cây cao thẳng tắp",
           "(2) 小溪 xiǎo xī – suối nhỏ → hình F: dòng suối giữa lá thu",
           "(3) 山脉 shānmài – dãy núi → hình B: những dãy núi nhấp nhô",
           "(4) 梯田 tītián – ruộng bậc thang → hình C: ruộng bậc thang có người cày",
           "(5) 峡谷 xiágǔ – hẻm núi → hình E: khe sâu giữa hai vách núi",
           "(6) 瀑布 pùbù – thác nước → hình D: thác nước trắng xóa"],
    say=["Chúng ta bắt đầu bằng phần khởi động. Sách đưa ra sáu bức ảnh phong cảnh, và yêu cầu chọn bức ảnh phù hợp với từng từ. Cả sáu từ này đều xuất hiện trong bài khóa.",
         F(0, "Từ thứ nhất: 森林, nghĩa là rừng, Hán Việt là sâm lâm. Đó là hình A, một khu rừng có những thân cây cao thẳng tắp."),
         F(1, "Từ thứ hai: 小溪, nghĩa là suối nhỏ. Đó là hình F, dòng suối chảy qua những tảng đá, bên cạnh là lá vàng mùa thu."),
         F(2, "Từ thứ ba: 山脉, nghĩa là dãy núi, Hán Việt là sơn mạch. Đó là hình B, những dãy núi xanh nối tiếp nhau. Đây cũng là chữ đầu tiên trong tên bài."),
         F(3, "Từ thứ tư: 梯田, nghĩa là ruộng bậc thang. 梯 là cái thang, 田 là ruộng. Đó là hình C, có người đang cày ruộng trên các bậc thang. Đây là nhân vật chính của bài khóa hôm nay."),
         F(4, "Từ thứ năm: 峡谷, nghĩa là hẻm núi, khe núi sâu. Đó là hình E, một khe sâu giữa hai vách núi dựng đứng."),
         F(5, "Từ thứ sáu: 瀑布, nghĩa là thác nước. Đó là hình D, dòng thác trắng xóa đổ xuống. Lát nữa đọc bài, các bạn sẽ gặp lại cả sáu cảnh này trên đường lên ruộng bậc thang.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 干 và 饮", size=38,
    items=["## 干 (can): khô",
           "干旱 khô hạn · 干燥 khô ráo · 干草 cỏ khô · 干花 hoa khô · 干渴 khô khát",
           "干裂 nứt nẻ · 干枯 khô héo · 风干 hong gió · 晒干 phơi khô · 晾干 phơi cho khô",
           "## 饮 (ẩm): uống",
           "饮水 uống nước · 饮茶 uống trà · 饮酒 uống rượu · 饮料 đồ uống · 饮食 ăn uống",
           "冷饮 đồ uống lạnh · 热饮 đồ uống nóng · 畅饮 uống thỏa thích · 饮水思源 uống nước nhớ nguồn"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo, rất có lợi cho người Việt vì hầu hết các chữ đều có âm Hán Việt quen thuộc.",
         F(0, "Nhóm thứ nhất có chữ can, như trong từ 干旱, nghĩa là khô. Chữ này còn một cách đọc khác với nghĩa là làm, nhưng trong nhóm này tất cả đều đọc thanh một."),
         F(1, "干旱，干燥，干草，干花，干渴。 Tức là: khô hạn, khô ráo, cỏ khô, hoa khô, và khô khát. Từ 干旱 là từ mới đầu tiên trong bài khóa: 遭遇百年不遇的干旱, gặp phải trận hạn hán trăm năm có một."),
         F(2, "干裂，干枯，风干，晒干，晾干。 Tức là: nứt nẻ, khô héo, hong gió cho khô, phơi nắng cho khô, và phơi ở chỗ thoáng cho khô."),
         F(3, "Nhóm thứ hai có chữ ẩm, như trong từ 饮水, nghĩa là uống, giống ẩm thực trong tiếng Việt."),
         F(4, "饮水，饮茶，饮酒，饮料，饮食。 Tức là: uống nước, uống trà, uống rượu, đồ uống, và ăn uống. Bài khóa có câu 人和牲畜饮水都难, người và gia súc đều khó có nước uống."),
         F(5, "冷饮，热饮，畅饮，饮水思源。 Tức là: đồ uống lạnh, đồ uống nóng, uống thỏa thích, và thành ngữ 饮水思源, uống nước nhớ nguồn, rất quen thuộc với người Việt chúng ta.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 旧 và 有", size=38,
    items=["## 旧 (cựu): cũ",
           "依旧 vẫn như cũ · 仍旧 vẫn còn · 照旧 như cũ · 古旧 cũ kỹ · 旧书 sách cũ · 旧物 đồ cũ",
           "旧地 chốn cũ · 旧居 nhà cũ · 旧日 ngày trước · 旧时 thời xưa · 旧式 kiểu cũ · 旧地重游 thăm lại chốn xưa",
           "## 有 (hữu): có",
           "拥有 sở hữu · 具有 có · 含有 chứa · 设有 có đặt · 留有 còn lưu · 持有 nắm giữ · 保有 giữ được · 享有 được hưởng",
           "公有 công hữu · 国有 quốc hữu · 占有 chiếm hữu · 原有 vốn có · 只有 chỉ có · 专有 độc quyền · 稀有 hiếm có · 私有 tư hữu · 富有 giàu có"],
    say=[F(0, "Nhóm thứ ba có chữ 旧, Hán Việt là cựu, nghĩa là cũ, như trong từ cựu học sinh."),
         F(1, "依旧，仍旧，照旧，古旧，旧书，旧物。 Tức là: vẫn như cũ, vẫn còn, y như cũ, cũ kỹ, sách cũ, đồ cũ. Từ 依旧 là từ mới của bài: 梯田壮丽依旧, ruộng bậc thang vẫn tráng lệ như xưa."),
         F(2, "旧地，旧居，旧日，旧时，旧式，旧地重游。 Tức là: chốn cũ, nhà cũ, ngày trước, thời xưa, kiểu cũ, và thành ngữ 旧地重游, thăm lại chốn xưa."),
         F(3, "Nhóm cuối cùng có chữ 有, Hán Việt là hữu, nghĩa là có."),
         F(4, "拥有，具有，含有，设有，留有，持有，保有，享有。 Tức là: sở hữu, có, chứa, có đặt, còn lưu lại, nắm giữ, giữ được, và được hưởng. Hai từ đầu tiên, 拥有 và 具有, chính là cặp từ chúng ta sẽ phân biệt trong bài hôm nay."),
         F(5, "公有，国有，占有，原有，只有，专有，稀有，私有，富有。 Tức là: công hữu, quốc hữu, chiếm hữu, vốn có, chỉ có, độc quyền, hiếm có, tư hữu, và giàu có."),
         "Các bạn thấy không, chỉ cần nắm nghĩa của một chữ gốc, ta có thể đoán được nghĩa của cả một nhóm từ. Hãy áp dụng cách này khi học từ mới nhé."])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng)
V = [
    ("山脉", "shānmài", "sơn mạch", "danh từ", "dãy núi, rặng núi", "这条山脉从东向西延伸了几百公里。", "Dãy núi này kéo dài mấy trăm cây số từ đông sang tây.",
     "Danh từ, nghĩa là dãy núi, rặng núi. 山 là núi, 脉 là mạch, tức là núi nối liền thành mạch. Đây là chữ đầu tiên trong tên bài."),
    ("雕刻", "diāokè", "điêu khắc", "động từ", "điêu khắc, chạm trổ", "这块石头上雕刻着一条龙。", "Trên tảng đá này có chạm khắc một con rồng.",
     "Động từ, nghĩa là điêu khắc, chạm trổ trên gỗ, đá, ngọc. Âm Hán Việt và nghĩa giống tiếng Việt. Tên bài dùng từ này theo nghĩa ví von: ruộng bậc thang giống như tác phẩm điêu khắc trên núi."),
    ("干旱", "gānhàn", "can hạn", "tính từ", "khô hạn, hạn hán", "这个地区常年干旱，很少下雨。", "Vùng này quanh năm khô hạn, rất ít mưa.",
     "Tính từ, nghĩa là khô hạn, thiếu nước vì lâu không mưa. Trong bài, 百年不遇的干旱 là trận hạn hán trăm năm có một. Chữ đầu đọc thanh một."),
    ("耕地", "gēngdì", "canh địa", "danh từ", "đất canh tác, đất trồng trọt", "这里的耕地越来越少了。", "Đất canh tác ở đây ngày càng ít đi.",
     "Danh từ, nghĩa là đất canh tác, đất trồng trọt. 耕 là cày, như trong canh tác. Từ này còn có thể là động từ, nghĩa là cày ruộng."),
    ("庄稼", "zhuāngjia", "trang giá", "danh từ", "hoa màu, cây trồng", "今年雨水充足，庄稼长得很好。", "Năm nay mưa nhiều, hoa màu mọc rất tốt.",
     "Danh từ, nghĩa là hoa màu, cây trồng ngoài đồng như lúa, ngô, lúa mì. Âm tiết thứ hai đọc nhẹ. Đây là từ rất khẩu ngữ, nông dân Trung Quốc dùng hằng ngày."),
    ("枯萎", "kūwěi", "khô nuy", "tính từ", "khô héo", "好几天没浇水，花都枯萎了。", "Mấy ngày không tưới, hoa đều héo cả rồi.",
     "Tính từ, nghĩa là khô héo, nói về hoa lá cây cối; cũng dùng nghĩa bóng, chỉ tinh thần suy sụp. Trong bài, 庄稼枯萎而死 là hoa màu khô héo mà chết."),
    ("牲畜", "shēngchù", "sinh súc", "danh từ", "súc vật, gia súc", "农民把牲畜赶到了山上。", "Nông dân lùa gia súc lên núi.",
     "Danh từ, nghĩa là gia súc nuôi trong nhà như trâu, bò, ngựa, dê. Chú ý cách đọc: âm tiết thứ hai đọc là chù, thanh bốn."),
    ("梯田", "tītián", "thê điền", "danh từ", "ruộng bậc thang", "山坡上有一层层的梯田。", "Trên sườn núi có từng tầng ruộng bậc thang.",
     "Danh từ, nghĩa là ruộng bậc thang. 梯 là cái thang, 田 là ruộng. Đây là từ khóa của cả bài. Lượng từ thường dùng là 片 hoặc 层: 一片片梯田，一层层梯田."),
    ("壮丽", "zhuànglì", "tráng lệ", "tính từ", "tráng lệ, lộng lẫy, đẹp đẽ", "站在山顶，我看到了壮丽的日出。", "Đứng trên đỉnh núi, tôi thấy cảnh mặt trời mọc tráng lệ.",
     "Tính từ, nghĩa là tráng lệ, hùng vĩ mà đẹp đẽ. Thường dùng cho phong cảnh lớn: 壮丽的山河，壮丽的景色."),
    ("依旧", "yījiù", "y cựu", "động từ", "như cũ, vẫn như xưa", "十年过去了，这里的风景依旧美丽。", "Mười năm trôi qua, phong cảnh nơi đây vẫn đẹp như xưa.",
     "Nghĩa là vẫn như cũ, vẫn như xưa. Có thể làm vị ngữ, như 壮丽依旧, hoặc đứng trước động từ, tính từ như phó từ, giống 仍然."),
    ("峡谷", "xiágǔ", "hiệp cốc", "danh từ", "khe sâu, hẻm núi", "一条小河从峡谷中流过。", "Một con sông nhỏ chảy qua hẻm núi.",
     "Danh từ, nghĩa là hẻm núi, khe núi sâu và hẹp. Chữ 峡 Hán Việt là hiệp, như trong Tam Hiệp, tức 三峡."),
    ("铺", "pū", "phô", "động từ", "trải, rải", "地上铺着一块红地毯。", "Trên sàn trải một tấm thảm đỏ.",
     "Động từ, nghĩa là trải, rải ra trên một bề mặt: 铺地毯, trải thảm; 铺路, rải đường. Đọc thanh một. Trong bài có thành ngữ 铺天盖地, phủ kín trời đất, ý nói rất nhiều, rất rộng."),
    ("卷", "juǎn", "quyển", "động từ", "cuốn, cuộn", "他把袖子卷了起来。", "Anh ấy xắn tay áo lên.",
     "Động từ, nghĩa là cuộn lại, cuốn đi. Đọc thanh ba. Trong bài có cụm 席卷而至, cuốn đến như cuộn chiếu, ý nói ruộng bậc thang tràn đến trước mắt. Chú ý: khi là danh từ chỉ bức tranh cuộn, như trong 画卷, chữ này đọc thanh bốn."),
    ("蔚蓝", "wèilán", "úy lam", "tính từ", "xanh biếc, xanh thẳm", "蔚蓝的大海一望无际。", "Biển xanh thẳm mênh mông bát ngát.",
     "Tính từ, nghĩa là xanh biếc, xanh thẳm, thường nói về bầu trời và biển cả: 蔚蓝的天空，蔚蓝的大海."),
    ("漂浮", "piāofú", "phiêu phù", "động từ", "trôi, bồng bềnh", "河面上漂浮着几片树叶。", "Trên mặt sông có mấy chiếc lá trôi bồng bềnh.",
     "Động từ, nghĩa là trôi nổi bồng bềnh trên mặt nước hay trên không. Chữ đầu đọc thanh một. Trong bài, 漂浮的白云 là những đám mây trắng bồng bềnh."),
    ("摇摆", "yáobǎi", "dao bãi", "động từ", "đong đưa, lắc lư", "小树在风中摇摆。", "Cây non đong đưa trong gió.",
     "Động từ, nghĩa là đong đưa, lắc lư qua lại. Nghĩa bóng là dao động, không kiên định: 立场摇摆, lập trường dao động."),
    ("衬托", "chèntuō", "sấn thác", "động từ", "làm nổi lên, tôn lên", "绿叶衬托着红花，显得更美了。", "Lá xanh tôn lên hoa đỏ, trông càng đẹp hơn.",
     "Động từ, nghĩa là làm nền để tôn cái khác lên. Trong bài, trời xanh, mây trắng, bóng cây 更衬托出梯田的壮美, càng tôn lên vẻ đẹp hùng vĩ của ruộng bậc thang."),
    ("盘旋", "pánxuán", "bàn toàn", "động từ", "lượn vòng, đi vòng", "一只老鹰在天空中盘旋。", "Một con đại bàng đang lượn vòng trên bầu trời.",
     "Động từ, nghĩa là lượn vòng, đi vòng quanh. Dùng cho chim bay lượn, hoặc đường núi quanh co: 盘旋而行, đi vòng vèo quanh núi."),
    ("时而", "shí'ér", "thời nhi", "phó từ", "lúc thì…, lúc thì…; thỉnh thoảng", "他时而看看窗外，时而看看手表。", "Anh ấy lúc thì nhìn ra cửa sổ, lúc thì xem đồng hồ.",
     "Phó từ, nghĩa là lúc thì, thỉnh thoảng, dùng trong văn viết. Đây là điểm ngữ pháp thứ nhất của bài."),
    ("海拔", "hǎibá", "hải bạt", "danh từ", "độ cao so với mặt biển", "这座山海拔三千多米。", "Ngọn núi này cao hơn ba nghìn mét so với mực nước biển.",
     "Danh từ, nghĩa là độ cao so với mực nước biển. 拔 là nhổ lên, vươn cao. Cách nói thường gặp: 海拔一千多米, cao hơn một nghìn mét so với mực nước biển."),
    ("瀑布", "pùbù", "bộc bố", "danh từ", "thác nước", "瀑布从高高的山上流下来。", "Thác nước đổ xuống từ trên núi cao.",
     "Danh từ, nghĩa là thác nước. Chữ 布 là tấm vải, vì thác nước trông như một dải lụa trắng treo trên núi."),
    ("纵横", "zònghéng", "tung hoành", "tính từ", "ngang dọc, ngang và dọc", "这座城市道路纵横，交通很方便。", "Thành phố này đường sá chằng chịt, giao thông rất thuận tiện.",
     "Tính từ, nghĩa là ngang dọc, đan xen chằng chịt. Cẩn thận: tung hoành trong tiếng Việt thường là tự do ngang dọc, làm mưa làm gió; còn 纵横 ở đây chỉ miêu tả hình dáng đan xen ngang dọc. Trong bài, 纵横万里 là trải dài ngang dọc hàng vạn dặm."),
    ("汹涌", "xiōngyǒng", "hung dũng", "động từ", "cuộn trào, dâng trào", "海上波涛汹涌，船不能出海。", "Trên biển sóng cuộn trào dữ dội, thuyền không thể ra khơi.",
     "Nghĩa là nước cuộn trào, dâng lên dữ dội. Cẩn thận: hung dũng trong tiếng Việt là dữ tợn, mạnh mẽ; còn 汹涌 tả sóng nước. Trong bài, 汹涌而来的梯田 ví ruộng bậc thang như sóng biển cuồn cuộn kéo đến."),
    ("目睹", "mùdǔ", "mục đổ", "động từ", "chứng kiến, mắt thấy", "他亲眼目睹了这次事故。", "Anh ấy tận mắt chứng kiến vụ tai nạn này.",
     "Động từ, nghĩa là tận mắt chứng kiến. 目 là mắt, 睹 là nhìn thấy. Văn viết, thường đi với 亲眼: 亲眼目睹."),
    ("重叠", "chóngdié", "trùng điệp", "động từ", "trùng điệp, chồng chéo", "两张图片重叠在一起。", "Hai bức ảnh chồng lên nhau.",
     "Động từ, nghĩa là chồng lên nhau, xếp lớp lên nhau. Chú ý cách đọc: chữ đầu đọc là chóng, thanh hai. Trong bài có dạng lặp 重重叠叠, trùng trùng điệp điệp."),
    ("雕塑", "diāosù", "điêu tố", "động từ / danh từ", "điêu khắc; tác phẩm điêu khắc", "广场中间有一座高大的雕塑。", "Giữa quảng trường có một bức tượng điêu khắc cao lớn.",
     "Vừa là động từ, nghĩa là điêu khắc, nặn tượng; vừa là danh từ, nghĩa là tác phẩm điêu khắc. Chữ 塑 là nặn, như trong 塑料, nhựa. Trong bài, 将一座座大山雕塑成了梯田 là tạc cả những ngọn núi lớn thành ruộng bậc thang."),
    ("毅力", "yìlì", "nghị lực", "danh từ", "nghị lực", "学好一门外语需要很大的毅力。", "Học giỏi một ngoại ngữ cần nghị lực rất lớn.",
     "Danh từ, nghĩa là nghị lực, ý chí bền bỉ. Âm Hán Việt và nghĩa giống hệt tiếng Việt."),
    ("杰出", "jiéchū", "kiệt xuất", "tính từ", "phi thường, xuất sắc, tuyệt vời", "他是一位杰出的科学家。", "Ông ấy là một nhà khoa học kiệt xuất.",
     "Tính từ, nghĩa là kiệt xuất, xuất sắc hơn người. Thường đi với người, tác phẩm, cống hiến: 杰出人物，杰出作品，杰出贡献."),
    ("震撼", "zhènhàn", "chấn hám", "động từ", "chấn động, rung động, lay động", "这部电影让我非常震撼。", "Bộ phim này khiến tôi vô cùng rung động.",
     "Động từ, nghĩa là làm chấn động, làm rung động mạnh mẽ trong lòng. Mạnh hơn 感动 rất nhiều. Trong bài: 它比万里长城更让我震撼."),
    ("宫殿", "gōngdiàn", "cung điện", "danh từ", "cung điện", "故宫里有很多古老的宫殿。", "Trong Cố Cung có rất nhiều cung điện cổ.",
     "Danh từ, nghĩa là cung điện, âm Hán Việt giống hệt tiếng Việt."),
    ("不禁", "bùjīn", "bất cấm", "phó từ", "không kìm được, không nhịn được", "看到这张老照片，她不禁笑了起来。", "Nhìn tấm ảnh cũ này, cô ấy bất giác bật cười.",
     "Phó từ, nghĩa là không kìm được, bất giác. Chú ý cách đọc: chữ thứ hai đọc là jīn, thanh một. Đây là điểm ngữ pháp thứ hai của bài."),
    ("曲子", "qǔzi", "khúc tử", "danh từ", "ca khúc, bản nhạc", "她弹了一首好听的曲子。", "Cô ấy đã đàn một bản nhạc hay.",
     "Danh từ, nghĩa là bài hát, bản nhạc. Chú ý chữ đầu đọc thanh ba, qǔ; lượng từ là 首: 一首曲子."),
    ("采集", "cǎijí", "thái tập", "động từ", "thu thập, sưu tầm, thu nhặt", "他们在山上采集了很多植物标本。", "Họ đã thu thập nhiều mẫu thực vật trên núi.",
     "Động từ, nghĩa là hái lượm, thu thập. Trong bài, 采集树果 là hái lượm quả cây, cách sống của người xưa trước khi biết trồng trọt."),
    ("种子", "zhǒngzi", "chủng tử", "danh từ", "hạt giống", "春天，农民把种子播到地里。", "Mùa xuân, nông dân gieo hạt giống xuống ruộng.",
     "Danh từ, nghĩa là hạt giống. Chú ý chữ đầu đọc thanh ba, zhǒng; còn khi là động từ trồng, như 种植, thì đọc thanh bốn."),
    ("稻谷", "dàogǔ", "đạo cốc", "danh từ", "hạt lúa, thóc", "秋天，田里的稻谷熟了。", "Mùa thu, lúa ngoài đồng đã chín.",
     "Danh từ, nghĩa là lúa, thóc còn nguyên vỏ. Trong bài, 金闪闪的稻谷 là những hạt lúa vàng óng."),
    ("锲而不舍", "qiè'érbùshě", "khiết nhi bất xả", "thành ngữ", "kiên nhẫn, miệt mài, không bỏ dở", "只要锲而不舍，就一定能成功。", "Chỉ cần kiên trì bền bỉ, nhất định sẽ thành công.",
     "Thành ngữ. 锲 là khắc, chạm; 舍 là bỏ. Nghĩa đen là khắc mãi không buông tay, nghĩa bóng là kiên trì bền bỉ đến cùng, giống nước chảy đá mòn."),
    ("开辟", "kāipì", "khai tịch", "động từ", "khai thác, mở mang, xây dựng", "他们在山里开辟了一条新路。", "Họ đã mở một con đường mới trong núi.",
     "Động từ, nghĩa là mở ra, khai phá: 开辟道路，开辟梯田，开辟市场. Chữ thứ hai đọc là pì, thanh bốn."),
    ("心血", "xīnxuè", "tâm huyết", "danh từ", "tâm huyết", "这本书花了他十年的心血。", "Cuốn sách này tốn mười năm tâm huyết của ông ấy.",
     "Danh từ, nghĩa là tâm huyết, công sức và tâm trí bỏ ra. Chú ý chữ 血 trong từ này đọc là xuè, thanh bốn."),
    ("辛勤", "xīnqín", "tân cần", "tính từ", "siêng năng, chăm chỉ", "老师辛勤地培养了一代又一代学生。", "Thầy cô cần mẫn vun đắp hết lớp học sinh này đến lớp khác.",
     "Tính từ, nghĩa là cần cù, vất vả mà chăm chỉ. Thường đi với 劳动 và 工作: 辛勤劳动，辛勤工作."),
    ("阻拦", "zǔlán", "trở lan", "động từ", "ngăn cản, cản trở", "他想走，谁也阻拦不了。", "Anh ấy muốn đi thì không ai ngăn được.",
     "Động từ, nghĩa là ngăn cản, chặn lại không cho làm. Trong bài, 任何困难也阻拦不了他们, không khó khăn nào ngăn cản được họ."),
    ("生态", "shēngtài", "sinh thái", "danh từ", "sinh thái học, sinh thái", "我们要保护好生态环境。", "Chúng ta phải bảo vệ tốt môi trường sinh thái.",
     "Danh từ, nghĩa là sinh thái, âm Hán Việt giống hệt tiếng Việt. Hay gặp: 生态环境, môi trường sinh thái."),
    ("审美", "shěnměi", "thẩm mỹ", "động từ", "thẩm mỹ, cảm thụ cái đẹp", "每个人的审美标准都不一样。", "Tiêu chuẩn thẩm mỹ của mỗi người đều khác nhau.",
     "Nghĩa là cảm nhận, đánh giá cái đẹp. Cẩn thận: thẩm mỹ trong tiếng Việt hay gợi đến làm đẹp, như thẩm mỹ viện; còn 审美 chỉ khả năng cảm thụ cái đẹp, như 审美价值, giá trị thẩm mỹ."),
    ("罕见", "hǎnjiàn", "hãn kiến", "tính từ", "hiếm thấy", "今年冬天下了一场罕见的大雪。", "Mùa đông năm nay có một trận tuyết lớn hiếm thấy.",
     "Tính từ, nghĩa là hiếm thấy. 罕 là hiếm, như trong hãn hữu của tiếng Việt."),
    ("珍稀", "zhēnxī", "trân hi", "tính từ", "quý hiếm", "大熊猫是一种珍稀动物。", "Gấu trúc là một loài động vật quý hiếm.",
     "Tính từ, nghĩa là quý và hiếm. Thường dùng cho động vật, thực vật: 珍稀动物，珍稀植物."),
    ("陶醉", "táozuì", "đào túy", "động từ", "say sưa, ngây ngất", "大家都陶醉在美妙的音乐中。", "Mọi người đều say sưa trong tiếng nhạc tuyệt diệu.",
     "Động từ, nghĩa là say sưa, đắm chìm trong một cảnh đẹp hay một cảm xúc. 醉 là say. Trong bài, 美景让人陶醉, cảnh đẹp làm người ta ngây ngất."),
    ("遗产", "yíchǎn", "di sản", "danh từ", "di sản", "长城是世界文化遗产。", "Vạn Lý Trường Thành là di sản văn hóa thế giới.",
     "Danh từ, nghĩa là di sản, tài sản người đi trước để lại, có thể là vật chất hoặc văn hóa. Âm Hán Việt giống tiếng Việt."),
    ("拥有", "yōngyǒu", "ủng hữu", "động từ", "sở hữu, có", "他拥有一家很大的公司。", "Ông ấy sở hữu một công ty rất lớn.",
     "Động từ, nghĩa là sở hữu, có trong tay, thường là thứ nhiều và quý giá. Lát nữa chúng ta sẽ phân biệt từ này với 具有."),
]

add("bullets", chapter="Từ mới (47 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 15 có 47 từ mới, chia thành 16 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 牲畜 (chù) · 重叠 (chóng) · 不禁 (jīn) · 心血 (xuè) · 种子 (zhǒng)",
           "Từ dễ nhầm: 纵横 · 汹涌 · 审美"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có bốn mươi bảy từ, thầy chia thành mười sáu nhóm nhỏ, mỗi nhóm ba từ, riêng nhóm cuối có hai từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Bài này có khá nhiều chữ đa âm, như 牲畜，重叠，不禁，心血，种子. Thầy sẽ nhắc cách đọc khi gặp."),
         F(4, "Ngoài ra, có mấy từ Hán Việt rất dễ hiểu nhầm, như 纵横，汹涌，审美. Nghĩa của chúng trong tiếng Trung khác với tiếng Việt, các bạn nhớ nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

sizes = [3] * 15 + [2]
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
    ("2010年中国西南遭遇百年不遇的干旱，耕地上，庄稼枯萎而死，农作物大面积绝收。",
     "Năm 2010, vùng tây nam Trung Quốc gặp phải trận hạn hán trăm năm có một. Trên đồng ruộng, hoa màu khô héo mà chết, cây nông nghiệp mất trắng trên diện rộng.",
     ["遭遇 là gặp phải, thường là chuyện không may. 百年不遇 là trăm năm không gặp, tức là trăm năm mới có một lần.",
      "绝收 là mất trắng, không thu hoạch được gì. Câu mở đầu vẽ ra một bức tranh khô cằn, để làm nền cho vẻ đẹp tươi tốt của ruộng bậc thang ở câu sau."],
     "二零一零年中国西南遭遇百年不遇的干旱，耕地上，庄稼枯萎而死，农作物大面积绝收。"),
    ("就在各地旱情严重、人和牲畜饮水都难的时候，滇南红河哀牢山南部的一片片梯田壮丽依旧，它们依山形而流转，一片片、一层层由半山腰延伸至峡谷，像一张张亮丽的油画，铺天盖地，席卷而至。",
     "Chính vào lúc hạn hán ở khắp nơi rất nghiêm trọng, người và gia súc đều khó có nước uống, thì những thửa ruộng bậc thang ở phía nam núi Ai Lao, vùng Hồng Hà, miền nam Vân Nam vẫn tráng lệ như xưa. Chúng uốn lượn theo thế núi, từng mảnh, từng tầng trải dài từ lưng chừng núi xuống tận hẻm núi, như từng bức tranh sơn dầu tươi sáng, phủ kín trời đất, ùa đến trước mắt.",
     ["滇 là tên gọi tắt của tỉnh Vân Nam, theo chú thích của sách. 红河 là Hồng Hà, thượng nguồn sông Hồng; 哀牢山 là núi Ai Lao. 依旧 làm vị ngữ: 壮丽依旧, vẫn tráng lệ như xưa.",
      "依山形而流转 là uốn lượn theo thế núi. 由……延伸至…… là kéo dài từ… đến…, 至 là đến, văn viết. 铺天盖地 là phủ kín trời đất, 席卷而至 là cuộn tới như cuốn chiếu; hai cụm này tả ruộng bậc thang nhiều vô kể."]),
    ("蔚蓝的天空，漂浮的白云，摇摆的树影，更衬托出梯田的壮美。",
     "Bầu trời xanh thẳm, những đám mây trắng bồng bềnh, bóng cây đong đưa, càng tôn lên vẻ đẹp hùng vĩ của ruộng bậc thang.",
     ["Câu này dùng ba cụm danh từ song song: 蔚蓝的天空，漂浮的白云，摇摆的树影, mỗi cụm là tính từ hoặc động từ cộng 的 cộng danh từ. Đây là cách tả cảnh rất hay trong văn viết.",
      "衬托出 là tôn lên, làm nổi bật lên. 壮美 là hùng vĩ và đẹp đẽ."]),
    ("我们的车在大山里沿着公路盘旋而行，时而行驶在深深的谷底，时而爬升到海拔一千多米高的山腰。",
     "Xe của chúng tôi men theo con đường quốc lộ, đi vòng vèo trong núi lớn, lúc thì chạy dưới đáy thung lũng sâu hun hút, lúc thì leo lên lưng chừng núi cao hơn một nghìn mét so với mực nước biển.",
     ["盘旋而行 là đi vòng vèo. 时而……，时而…… là lúc thì…, lúc thì…, đây chính là điểm ngữ pháp 时而.",
      "谷底 là đáy thung lũng. 爬升 là leo lên cao. 海拔一千多米高的山腰 là lưng chừng núi cao hơn một nghìn mét so với mực nước biển."]),
    ("遥望山顶，是大片的森林，峡谷间闪闪发光的是小溪、泉水和瀑布，半山腰是村子，村子下是如山如海、纵横万里、汹涌而来的梯田。",
     "Nhìn xa lên đỉnh núi là những cánh rừng bạt ngàn; lấp lánh giữa các hẻm núi là suối nhỏ, nước suối và thác nước; lưng chừng núi là làng bản; dưới làng là ruộng bậc thang nhiều như núi như biển, trải dài ngang dọc hàng vạn dặm, cuồn cuộn kéo đến.",
     ["Câu này tả cảnh theo thứ tự từ trên xuống dưới: 山顶，峡谷间，半山腰，村子下. Mỗi vế dùng mẫu nơi chốn cộng 是 cộng sự vật, rất dễ bắt chước khi tả cảnh. Đây cũng là câu hỏi hai của bài tập năm.",
      "遥望 là nhìn ra xa. 如山如海 là như núi như biển, ý nói rất nhiều. 纵横万里 là ngang dọc vạn dặm. 汹涌而来 là cuồn cuộn kéo đến như sóng."]),
    ("尽管已目睹这奇迹无数次，但我每次身临其境，都会为哈尼族山民们在这重重叠叠的山脉上雕塑出的美丽画卷而震惊。",
     "Mặc dù đã tận mắt chứng kiến kỳ tích này vô số lần, nhưng mỗi lần đặt chân đến đây, tôi đều kinh ngạc trước bức tranh tuyệt đẹp mà người dân tộc Hà Nhì đã tạc nên trên những dãy núi trùng trùng điệp điệp này.",
     ["尽管……，但……，都…… là mặc dù…, nhưng…, đều…. Đây là mẫu câu của bài tập bốn. 身临其境 là thành ngữ, nghĩa là đích thân có mặt tại nơi đó.",
      "为……而震惊 là kinh ngạc vì điều gì. 哈尼族 là dân tộc Hà Nhì, một dân tộc thiểu số lâu đời của Trung Quốc, theo chú thích của sách. 画卷 là bức tranh cuộn, ví ruộng bậc thang như một bức tranh lớn."]),
    ("这是以大地为背景，用生命和毅力雕刻出的杰出作品，它比万里长城更让我震撼，它比历史悠久的宫殿更让我感动。",
     "Đây là tác phẩm kiệt xuất được khắc nên bằng sinh mệnh và nghị lực, lấy mặt đất làm phông nền. Nó khiến tôi rung động hơn cả Vạn Lý Trường Thành, khiến tôi cảm động hơn cả những cung điện lâu đời.",
     ["以大地为背景 là lấy mặt đất làm phông nền. Ở đây chữ 为 nghĩa là làm, đọc thanh hai. Tác giả ví ruộng bậc thang là một tác phẩm điêu khắc khổng lồ, đúng như tên bài.",
      "Hai vế 它比……更让我…… song song với nhau, so sánh ruộng bậc thang với Trường Thành và cung điện, những công trình nổi tiếng nhất của Trung Quốc."]),
    ("我不禁问自己，这里的人为什么选择了梯田？",
     "Tôi không kìm được mà tự hỏi mình: vì sao người ở đây lại chọn ruộng bậc thang?",
     ["不禁 là không kìm được, bất giác. Đây là điểm ngữ pháp 不禁, và câu này chính là ví dụ một trong phần ngữ pháp.",
      "Câu hỏi này chuyển bài khóa từ phần tả cảnh sang phần giải thích lý do, và cũng là câu hỏi bốn của bài tập năm."]),
    ("后来，我在当地听到了一首古老的曲子，歌词的意思是，祖先们只靠打猎过不了日子，光靠采集树果也过不了日子，于是学会了翻地，学会了种植。",
     "Về sau, tôi được nghe một bài hát cổ ở địa phương, lời bài hát có ý là: tổ tiên chỉ dựa vào săn bắn thì không sống nổi, chỉ dựa vào hái lượm quả cây cũng không sống nổi, thế là học cách cày xới đất, học cách trồng trọt.",
     ["过不了日子 là không sống được, không qua ngày được; 过不了 là không thể vượt qua được. 只靠 và 光靠 đều là chỉ dựa vào.",
      "翻地 là cày xới đất. 种植 là trồng trọt, chữ đầu đọc thanh bốn. Bài hát cổ kể lại quá trình con người chuyển từ săn bắn, hái lượm sang trồng trọt."]),
    ("他们发现种子和水最亲近，喝过水的种子就是金闪闪的稻谷，从此他们再也离不开梯田和水。",
     "Họ phát hiện hạt giống và nước gần gũi nhau nhất, hạt giống được uống nước sẽ thành những hạt lúa vàng óng, từ đó họ không bao giờ rời xa ruộng bậc thang và nước nữa.",
     ["Câu này dùng phép nhân hóa: hạt giống thân thiết với nước, hạt giống uống nước. 金闪闪 là vàng óng ánh, dạng tính từ lặp ABB.",
      "从此 là từ đó trở đi. 再也离不开 là không bao giờ rời xa được nữa."]),
    ("经过数十代人的锲而不舍，他们终于将一座座大山，雕塑成了梯田。",
     "Trải qua sự kiên trì bền bỉ của mấy chục thế hệ, cuối cùng họ đã tạc những ngọn núi lớn thành ruộng bậc thang.",
     ["数十代人 là mấy chục thế hệ người. 锲而不舍 là kiên trì không bỏ cuộc. 将 ở đây giống 把, văn viết: 将一座座大山雕塑成了梯田.",
      "雕塑成 là tạc thành. Một lần nữa tác giả dùng hình ảnh điêu khắc, gắn với tên bài."]),
    ("面对大山，山民们没有对抗，而是选择了服从——他们服从自然规律，选择开辟梯田这种农耕方式，最终与大自然和谐相处。",
     "Đối mặt với núi lớn, người dân miền núi không chống lại, mà chọn cách thuận theo: họ thuận theo quy luật tự nhiên, chọn cách khai phá ruộng bậc thang làm phương thức canh tác, cuối cùng chung sống hài hòa với thiên nhiên.",
     ["没有……，而是…… là không…, mà là…. Đây là mẫu câu thứ hai của bài tập bốn: 面对……，……没有……，而是选择……，最终…….",
      "Dấu gạch ngang dài dùng để giải thích thêm cho từ 服从. 和谐相处 là chung sống hài hòa, chữ 处 ở đây đọc thanh ba."]),
    ("1300多年，山民们用汗水，用心血，用日复一日的辛勤劳动完成了山脉上的雕刻，任何困难也阻拦不了他们。",
     "Hơn 1300 năm, người dân miền núi đã dùng mồ hôi, dùng tâm huyết, dùng sự lao động cần cù ngày này qua ngày khác để hoàn thành tác phẩm điêu khắc trên dãy núi, không khó khăn nào ngăn cản được họ.",
     ["Ba cụm 用汗水，用心血，用日复一日的辛勤劳动 là phép điệp, nhấn mạnh công sức của người dân. 日复一日 là ngày này qua ngày khác.",
      "任何……也…… là bất cứ… cũng…. 阻拦不了 là không ngăn cản được. Câu này nhắc lại đúng tên bài: 山脉上的雕刻."],
     "一千三百多年，山民们用汗水，用心血，用日复一日的辛勤劳动完成了山脉上的雕刻，任何困难也阻拦不了他们。"),
    ("这幅画卷以其宝贵的生态、文化和审美价值，展示着它的罕见和珍稀。",
     "Bức tranh này, với những giá trị quý báu về sinh thái, văn hóa và thẩm mỹ, đang phô bày sự hiếm có và quý giá của nó.",
     ["以其…… là bằng cái… của nó, văn viết; 其 thay cho 这幅画卷. Đây là câu hỏi năm của bài tập năm: 哈尼梯田有什么价值？",
      "幅 là lượng từ của tranh. 展示 là phô bày, cho thấy. 罕见 và 珍稀 vốn là tính từ, ở đây làm tân ngữ."]),
    ("有人说：“哈尼梯田的美景让人陶醉，这里的一切无不体现着当地百姓与自然和谐相处的智慧，体现着民众对自身文化和自然环境的尊重。",
     "Có người nói: Cảnh đẹp của ruộng bậc thang Hà Nhì khiến người ta say đắm, mọi thứ ở đây đều thể hiện trí tuệ chung sống hài hòa với thiên nhiên của người dân địa phương, thể hiện sự tôn trọng của người dân đối với văn hóa của chính mình và môi trường tự nhiên.",
     ["无不 là không cái nào không, tức là tất cả đều. 无不体现着 là đều thể hiện. Đây là điểm ngữ pháp 无不.",
      "与……和谐相处 là chung sống hài hòa với…. 对……的尊重 là sự tôn trọng đối với…."]),
    ("它所蕴含的人与自然高度和谐发展的古老文化特征，正是21世纪人类所追求的一种精神。”",
     "Đặc trưng văn hóa cổ xưa về sự phát triển hài hòa cao độ giữa con người và thiên nhiên mà nó chứa đựng, chính là một tinh thần mà nhân loại thế kỷ 21 đang theo đuổi.",
     ["所 cộng động từ làm định ngữ, văn viết: 它所蕴含的 là cái mà nó chứa đựng; 人类所追求的 là cái mà nhân loại theo đuổi. 蕴含 là chứa đựng bên trong.",
      "Câu có chủ ngữ rất dài, trung tâm là 特征, đặc trưng. Bỏ hết định ngữ, khung câu chỉ là: 特征正是一种精神."],
     "它所蕴含的人与自然高度和谐发展的古老文化特征，正是二十一世纪人类所追求的一种精神。"),
    ("也有人说，哈尼梯田“是人类的宝贵遗产，它向我们证明人类拥有惊人的创造精神”！",
     "Cũng có người nói, ruộng bậc thang Hà Nhì là di sản quý báu của nhân loại, nó chứng minh cho chúng ta thấy con người có tinh thần sáng tạo đáng kinh ngạc!",
     ["遗产 là di sản. 向我们证明 là chứng minh với chúng ta. 拥有惊人的创造精神 là có tinh thần sáng tạo đáng kinh ngạc; chú ý 拥有 đi với thứ quý giá.",
      "Bài khóa kết thúc bằng hai lời đánh giá của người khác, dùng dấu ngoặc kép để trích dẫn, làm cho lời khen ngợi thêm khách quan và thuyết phục."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 山脉上的雕刻", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 山脉上的雕刻, dài bảy trăm tám mươi ba chữ. Bài được cải biên từ một bài viết về ruộng bậc thang Hà Nhì ở Hồng Hà, núi Ai Lao, đăng trên tạp chí Địa lý quốc gia Trung Quốc, tác giả là Lý Húc.",
         F(0, "Thầy chia bài thành mười bảy đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    spoken = spoken.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 100 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Tóm tắt nội dung", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5) – phần 1", size=34,
    items=["## 1. 当中国西南遭遇干旱时，哈尼梯田怎么样？",
           "梯田壮丽依旧 · 蔚蓝的天空，漂浮的白云，摇摆的树影，更衬托出梯田的壮美",
           "## 2. 坐在车上遥望梯田时看到的风景",
           "山顶是森林，峡谷间是小溪、泉水和瀑布，半山腰是村子，村子下是梯田",
           "## 3. 为什么“我”每次目睹哈尼梯田都感到震惊？",
           "这是用生命和毅力雕刻出的杰出作品，它比长城更让我震撼，比宫殿更让我感动"],
    say=["Bài tập năm của sách yêu cầu dựa vào gợi ý để trả lời câu hỏi về nội dung bài khóa. Chúng ta cùng làm luôn nhé, đây cũng là bố cục của bài.",
         F(0, "Câu hỏi một: khi vùng tây nam Trung Quốc gặp hạn hán, ruộng bậc thang Hà Nhì thế nào?"),
         F(1, "Trả lời: 梯田壮丽依旧。蔚蓝的天空，漂浮的白云，摇摆的树影，更衬托出梯田的壮美。 Ruộng bậc thang vẫn tráng lệ như xưa, trời xanh, mây trắng, bóng cây càng tôn lên vẻ đẹp của nó."),
         F(2, "Câu hỏi hai: hãy tả lại phong cảnh nhìn thấy khi ngồi trên xe ngắm ruộng bậc thang."),
         F(3, "Trả lời: 山顶是森林，峡谷间是小溪、泉水和瀑布，半山腰是村子，村子下是梯田。 Các bạn nhớ thứ tự từ trên xuống dưới nhé."),
         F(4, "Câu hỏi ba: vì sao mỗi lần chứng kiến ruộng bậc thang, nhân vật tôi đều thấy kinh ngạc?"),
         F(5, "Trả lời: 这是用生命和毅力雕刻出的杰出作品，它比长城更让我震撼，比宫殿更让我感动。 Đây là tác phẩm kiệt xuất khắc bằng sinh mệnh và nghị lực, rung động lòng người hơn cả Trường Thành và cung điện.")])

add("bullets", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5) – phần 2", size=34,
    items=["## 4. 这里的人为什么选择了梯田？",
           "古老的曲子：只靠打猎、采集过不了日子 · 经过数十代人的锲而不舍 · 服从自然规律，与大自然和谐相处",
           "## 5. 哈尼梯田有什么价值？",
           "以其宝贵的生态、文化和审美价值，展示着它的罕见和珍稀",
           "## 6. 哈尼梯田体现了什么样的智慧和精神？",
           "体现：与自然和谐相处的智慧，对自身文化和自然环境的尊重 · 蕴含：人与自然高度和谐发展 · 人类惊人的创造精神"],
    say=[F(0, "Câu hỏi bốn: vì sao người ở đây lại chọn ruộng bậc thang?"),
         F(1, "Trả lời: theo bài hát cổ, tổ tiên chỉ dựa vào săn bắn và hái lượm thì không sống nổi, nên phải trồng trọt. 经过数十代人的锲而不舍, trải qua mấy chục thế hệ kiên trì, họ tạc núi thành ruộng. Họ thuận theo quy luật tự nhiên, và chung sống hài hòa với thiên nhiên."),
         F(2, "Câu hỏi năm: ruộng bậc thang Hà Nhì có giá trị gì?"),
         F(3, "Trả lời: 以其宝贵的生态、文化和审美价值，展示着它的罕见和珍稀。 Đó là giá trị sinh thái, văn hóa và thẩm mỹ."),
         F(4, "Câu hỏi sáu: ruộng bậc thang Hà Nhì thể hiện trí tuệ và tinh thần như thế nào?"),
         F(5, "Trả lời: nó thể hiện trí tuệ chung sống hài hòa với thiên nhiên, sự tôn trọng văn hóa và môi trường; nó chứa đựng đặc trưng phát triển hài hòa giữa người và tự nhiên; và chứng minh tinh thần sáng tạo đáng kinh ngạc của con người. Bố cục này rất có ích khi các bạn tự kể lại bài khóa.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 时而", section="Ngữ pháp 注释", title="1. 时而 shí'ér – lúc thì…, lúc thì… (1)", size=36,
    items=["Phó từ, dùng trong văn viết; có hai cách dùng chính",
           "## (1) Hai hay nhiều 时而 dùng liền nhau: nhiều tình huống thay nhau xảy ra",
           "我们的车在大山里沿着公路盘旋而行，时而行驶在深深的谷底，时而爬升到海拔一千多米高的山腰。",
           "五彩的蝴蝶颜色鲜艳极了，尤其是在阳光下，时而金黄，时而翠绿，时而由紫变蓝。"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là phó từ 时而.",
         F(0, "时而 là phó từ, dùng trong văn viết. Nó có hai cách dùng chính."),
         F(1, "Cách dùng thứ nhất: hai hoặc nhiều hơn hai chữ 时而 dùng liền nhau, tạo thành câu ghép đẳng lập, biểu thị nhiều tình huống thay nhau xảy ra. Tiếng Việt dịch là lúc thì…, lúc thì…, giống 一会儿……一会儿…… trong khẩu ngữ."),
         F(2, "Ví dụ một, lấy từ bài khóa: 我们的车在大山里沿着公路盘旋而行，时而行驶在深深的谷底，时而爬升到海拔一千多米高的山腰。 Xe chúng tôi đi vòng vèo trong núi, lúc thì chạy dưới đáy thung lũng, lúc thì leo lên lưng chừng núi cao hơn một nghìn mét."),
         F(3, "Ví dụ hai: 五彩的蝴蝶颜色鲜艳极了，尤其是在阳光下，时而金黄，时而翠绿，时而由紫变蓝。 Con bướm nhiều màu sắc rực rỡ vô cùng, nhất là dưới ánh nắng, lúc thì vàng óng, lúc thì xanh biếc, lúc thì từ tím chuyển sang lam. Ở đây có ba chữ 时而 liền nhau.")])

add("bullets", section="Ngữ pháp 注释", title="1. 时而 shí'ér – thỉnh thoảng (2)", size=36,
    items=["## (2) Dùng một 时而: hành động lặp lại hoặc xuất hiện không định kỳ",
           "Thường đứng trước cụm động từ; nghĩa là thỉnh thoảng, chốc chốc",
           "主人去世以后，那狗没有了往日的精神，一点儿东西不吃，时而发出令人伤心的叫声。",
           "女儿第一天上幼儿园回来特别高兴，时而掏出老师奖励的小红花，看后又小心地珍藏起来。"],
    say=[F(0, "Cách dùng thứ hai: chỉ dùng một chữ 时而, biểu thị một hành động nào đó lặp lại hoặc xuất hiện không theo thời gian cố định."),
         F(1, "Lúc này 时而 thường đứng trước cụm động từ, tiếng Việt dịch là thỉnh thoảng, chốc chốc lại."),
         F(2, "Ví dụ ba: 主人去世以后，那狗没有了往日的精神，一点儿东西不吃，时而发出令人伤心的叫声。 Sau khi chủ qua đời, con chó mất hết vẻ hăng hái ngày trước, chẳng ăn chút gì, thỉnh thoảng lại phát ra tiếng kêu nghe rất đau lòng."),
         F(3, "Ví dụ bốn: 女儿第一天上幼儿园回来特别高兴，时而掏出老师奖励的小红花，看后又小心地珍藏起来。 Con gái đi nhà trẻ ngày đầu tiên về rất vui, chốc chốc lại lấy bông hoa đỏ cô giáo thưởng ra xem, xem xong lại cẩn thận cất đi.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: chọn vế câu phù hợp với 时而", reveal=True, size=33,
    items=["A. 高低不平，延伸到看不到尽头的远方 · B. 他的语言来自民间 · C. 半天了，他还是拿不定主意",
           "(1) 那是一条年久失修的老路，时而土路，时而水泥道，（ ）。",
           "Đáp án: A – ……时而土路，时而水泥道，高低不平，延伸到看不到尽头的远方。",
           "(2) （ ），时而说已经想好了，就这么办，时而又犹豫不决，说还得好好想想。",
           "Đáp án: C – 半天了，他还是拿不定主意，时而说已经想好了……",
           "(3) （ ），时而朴实、自然，时而幽默、生动，有的像政论，有的像诗歌，深受读者喜爱。",
           "Đáp án: B – 他的语言来自民间，时而朴实、自然，时而幽默、生动……"],
    say=[F(0, "Luyện tập: chọn vế câu phía trước hoặc phía sau phù hợp. Có ba lựa chọn. A: 高低不平，延伸到看不到尽头的远方, cao thấp gập ghềnh, kéo dài đến nơi xa không thấy điểm cuối. B: 他的语言来自民间, ngôn ngữ của anh ấy đến từ dân gian. C: 半天了，他还是拿不定主意, mãi rồi mà anh ấy vẫn chưa quyết được."),
         F(1, "Câu một: 那是一条年久失修的老路，时而土路，时而水泥道，括号。 Đó là một con đường cũ lâu năm không sửa, lúc là đường đất, lúc là đường xi măng. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: A. 高低不平，延伸到看不到尽头的远方。 Con đường cao thấp gập ghềnh, kéo dài đến tận nơi xa không thấy điểm cuối."),
         F(3, "Câu hai: 括号，时而说已经想好了，就这么办，时而又犹豫不决，说还得好好想想。 Lúc thì nói đã nghĩ kỹ rồi, cứ làm vậy đi, lúc lại do dự, nói còn phải suy nghĩ kỹ thêm."),
         F(4, "Đáp án: C. 半天了，他还是拿不定主意。 Mãi rồi anh ấy vẫn chưa quyết được. Hai chữ 时而 tả sự do dự, thay đổi liên tục."),
         F(5, "Câu ba: 括号，时而朴实、自然，时而幽默、生动，有的像政论，有的像诗歌，深受读者喜爱。 Lúc thì mộc mạc, tự nhiên, lúc thì hài hước, sinh động, có chỗ như văn chính luận, có chỗ như thơ ca, được độc giả rất yêu thích."),
         F(6, "Đáp án: B. 他的语言来自民间。 Ngôn ngữ của anh ấy đến từ dân gian, nên lúc thì mộc mạc, lúc thì hài hước.")])

add("bullets", chapter="Ngữ pháp: 不禁", section="Ngữ pháp 注释", title="2. 不禁 bùjīn – không kìm được, bất giác", size=36,
    items=["Phó từ, nghĩa là 不由自主地、无法控制地: không tự chủ được",
           "Sau 不禁 có thể là cụm động từ, cụm chủ vị, hoặc tính từ",
           "这是以大地为背景，用生命和毅力雕刻出的杰出作品……我不禁问自己，这里的人为什么选择了梯田？",
           "那是我第一次用汉语演讲，走上讲台，不禁心里有些发慌。",
           "听到这个消息，大家不禁兴奋起来。"],
    say=["Điểm ngữ pháp thứ hai là phó từ 不禁. Các bạn nhớ chữ thứ hai đọc thanh một nhé.",
         F(0, "不禁 nghĩa là 不由自主地，无法控制地, tức là không tự chủ được, không kìm được. Tiếng Việt có thể dịch là bất giác, không nhịn được mà."),
         F(1, "Sau 不禁 có thể là cụm động từ, cụm chủ vị, hoặc tính từ."),
         F(2, "Ví dụ một, lấy từ bài khóa: 这是以大地为背景，用生命和毅力雕刻出的杰出作品，我不禁问自己，这里的人为什么选择了梯田？ Đây là tác phẩm kiệt xuất lấy mặt đất làm nền, tôi không kìm được mà tự hỏi: vì sao người ở đây lại chọn ruộng bậc thang? Sau 不禁 là cụm động từ 问自己."),
         F(3, "Ví dụ hai: 那是我第一次用汉语演讲，走上讲台，不禁心里有些发慌。 Đó là lần đầu tiên tôi diễn thuyết bằng tiếng Trung, bước lên bục, trong lòng bất giác thấy hơi luống cuống. Sau 不禁 là cụm chủ vị 心里有些发慌."),
         F(4, "Ví dụ ba: 听到这个消息，大家不禁兴奋起来。 Nghe tin này, mọi người không kìm được mà phấn khởi hẳn lên. Sau 不禁 là tính từ 兴奋 cộng 起来.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: hoàn thành câu với 不禁", reveal=True, size=36,
    items=["(1) 听他说得______，大家不禁连连点头。",
           "Đáp án: 听他说得很有道理，大家不禁连连点头。",
           "(2) 看着电影中父子情深，他不禁______。",
           "Đáp án: ……他不禁流下了眼泪。",
           "(3) 看到污染的河流，人们不禁要问：“______？”",
           "Đáp án: ……人们不禁要问：“这是谁造成的？”"],
    say=[F(0, "Luyện tập: hoàn thành câu. Câu một: 听他说得什么，大家不禁连连点头。 Nghe anh ấy nói thế nào đó, mọi người bất giác gật đầu liên tục. Các bạn tạm dừng và thử hoàn thành câu nhé."),
         F(1, "Đáp án gợi ý: 听他说得很有道理，大家不禁连连点头。 Nghe anh ấy nói rất có lý, mọi người không kìm được mà gật đầu liên tục."),
         F(2, "Câu hai: 看着电影中父子情深，他不禁什么。 Xem tình cha con sâu nặng trong phim, anh ấy không kìm được mà làm gì?"),
         F(3, "Đáp án gợi ý: 他不禁流下了眼泪。 Anh ấy không kìm được mà rơi nước mắt."),
         F(4, "Câu ba: 看到污染的河流，人们不禁要问：什么？ Nhìn thấy dòng sông bị ô nhiễm, người ta không khỏi muốn hỏi điều gì?"),
         F(5, "Đáp án gợi ý: 这是谁造成的？ Đây là do ai gây ra? Hoặc: 我们还能做些什么？ Chúng ta còn có thể làm gì? Chú ý: phía trước 不禁 thường là nguyên nhân, như 听到，看到，看着.")])

add("bullets", chapter="Ngữ pháp: 无不", section="Ngữ pháp 注释", title="3. 无不 wúbù – không cái nào không, tất cả đều", size=34,
    items=["Phó từ, nghĩa là 没有一个不、全都 · đứng trước động từ, cụm động từ · văn viết",
           "坏人受到了应有的惩罚，百姓无不拍手称快。",
           "哈尼梯田的美景让人陶醉，这里的一切无不体现着当地百姓与自然和谐相处的智慧，体现着民众对自身文化和自然环境的尊重。",
           "在社会教育中，人人都是施教者，又都是受教育者；在人们的学习、生活、工作中，任何人的一言一行，一举一动，无不影响着你周围的人们，而你本身也每时每刻都受着别人的影响。"],
    say=["Điểm ngữ pháp thứ ba là phó từ 无不.",
         F(0, "无不 nghĩa là 没有一个不，全都, tức là không có cái nào không, tất cả đều. Đây là phủ định của phủ định, nên mang ý khẳng định rất mạnh. Nó thường đứng trước động từ hoặc cụm động từ, và dùng trong văn viết. Chủ ngữ phía trước phải là số nhiều, như 百姓，一切，人人."),
         F(1, "Ví dụ một: 坏人受到了应有的惩罚，百姓无不拍手称快。 Kẻ xấu đã bị trừng phạt thích đáng, người dân ai nấy đều vỗ tay hả hê."),
         F(2, "Ví dụ hai, lấy từ bài khóa: 哈尼梯田的美景让人陶醉，这里的一切无不体现着当地百姓与自然和谐相处的智慧，体现着民众对自身文化和自然环境的尊重。 Mọi thứ ở đây đều thể hiện trí tuệ chung sống hài hòa với thiên nhiên của người dân địa phương."),
         F(3, "Ví dụ ba: 在社会教育中，人人都是施教者，又都是受教育者；在人们的学习、生活、工作中，任何人的一言一行，一举一动，无不影响着你周围的人们，而你本身也每时每刻都受着别人的影响。 Trong giáo dục xã hội, ai cũng vừa là người dạy, vừa là người được dạy; mỗi lời nói, mỗi hành động của bất kỳ ai đều ảnh hưởng đến những người xung quanh, còn bản thân bạn cũng luôn chịu ảnh hưởng của người khác.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: chọn vị trí thích hợp cho 无不", reveal=True, size=32,
    items=["(1) A他设计的灯具、家具B和各种装饰品，C造型新颖，D光彩照人。",
           "Đáp án: C – ……和各种装饰品，无不造型新颖，光彩照人。",
           "(2) 他创业其实A只有十多年，但他却能将自己的创业心得B升华，并总结成朴实易懂的语言，C但凡有一些创业体会的人，D在他一针见血的点评中了解到了创业的本质。",
           "Đáp án: D – ……但凡有一些创业体会的人，无不在他一针见血的点评中了解到了创业的本质。",
           "(3) ……李敖的情感经历C与他笔下那颇含激情的文章一样，D充满传奇的色彩。",
           "Đáp án: D – ……与他笔下那颇含激情的文章一样，无不充满传奇的色彩。"],
    say=[F(0, "Luyện tập: chọn vị trí thích hợp cho 无不. Câu một: 他设计的灯具、家具和各种装饰品，造型新颖，光彩照人。 Đèn, đồ nội thất và các loại đồ trang trí anh ấy thiết kế, kiểu dáng mới lạ, rực rỡ bắt mắt. Đặt 无不 ở đâu? Các bạn tạm dừng và suy nghĩ nhé."),
         F(1, "Đáp án: C. 他设计的灯具、家具和各种装饰品，无不造型新颖，光彩照人。 Chủ ngữ là số nhiều, gồm đèn, đồ nội thất và đồ trang trí; 无不 đứng trước cả hai vị ngữ, nghĩa là món nào cũng mới lạ, rực rỡ."),
         F(2, "Câu hai: 他创业其实只有十多年，但他却能将自己的创业心得升华，并总结成朴实易懂的语言，但凡有一些创业体会的人，在他一针见血的点评中了解到了创业的本质。 Anh ấy khởi nghiệp thật ra mới hơn mười năm, nhưng lại có thể nâng tầm những điều tâm đắc khi khởi nghiệp, đúc kết thành ngôn ngữ mộc mạc dễ hiểu; phàm là người có chút trải nghiệm khởi nghiệp, đều hiểu ra bản chất của khởi nghiệp qua những lời bình sắc sảo của anh ấy."),
         F(3, "Đáp án: D. 但凡有一些创业体会的人，无不在他一针见血的点评中了解到了创业的本质。 但凡……的人 là phàm là những người…, chủ ngữ số nhiều, nên 无不 đứng ngay sau, trước cụm giới từ."),
         F(4, "Câu ba nói về nhà văn Đài Loan Lý Ngao: 李敖的情感经历与他笔下那颇含激情的文章一样，充满传奇的色彩。 Những trải nghiệm tình cảm của Lý Ngao cũng giống như những bài văn đầy nhiệt huyết dưới ngòi bút của ông, đều đầy màu sắc huyền thoại."),
         F(5, "Đáp án: D. 李敖的情感经历与他笔下那颇含激情的文章一样，无不充满传奇的色彩。 Ở đây chủ ngữ gồm hai thứ: trải nghiệm tình cảm và bài văn, nên dùng 无不 trước vị ngữ 充满.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 拥有 – 具有", section="Phân biệt từ 词语辨析", title="Phân biệt 拥有 và 具有",
    common="Giống nhau: đều là động từ, đều có nghĩa là có. Nhưng thường không thay thế cho nhau được.",
    cols=[{"head": "拥有",
           "lines": ["(1) Nhấn mạnh sự chiếm hữu, sở hữu",
                     "(2) Thường là thứ nhiều, quý giá: 土地、人口、财产、资源、爱、权利",
                     "Đúng: 我国拥有丰富的水电资源。",
                     "Sai: 他具有一套大房子。"]},
          {"head": "具有",
           "lines": ["(1) Nhấn mạnh sự tồn tại, vốn có",
                     "(2) Thường đi với sự vật trừu tượng: 特色、特点、兴趣、水平、意义",
                     "Đúng: 我喜欢看具有民族风情的电视节目。",
                     "Sai: 这次改革拥有伟大意义。"]}],
    say=["Tiếp theo là phần phân biệt từ: 拥有 và 具有. Cả hai từ đều có chữ 有, và đều dịch là có, nên người học rất hay dùng lẫn lộn.",
         "Điểm giống nhau: cả hai đều là động từ, đều mang nghĩa có. Nhưng sách nhấn mạnh: thông thường hai từ này không thể thay thế cho nhau.",
         F(0, "拥有 nghiêng về sự chiếm hữu, sở hữu. Chữ 拥 là ôm, tức là ôm trong tay. Tân ngữ thường là thứ nhiều về số lượng, hoặc quý giá, như 土地，人口，财产，资源，爱，权利, tức là đất đai, dân số, tài sản, tài nguyên, tình yêu, quyền lợi."),
         F(0, "Ví dụ: 我国拥有丰富的水电资源。 Nước ta có nguồn tài nguyên thủy điện phong phú. Tài nguyên là thứ có thể sở hữu, nên dùng 拥有."),
         F(1, "具有 nghiêng về sự tồn tại, tức là sự vật vốn mang trong mình một đặc điểm nào đó. Tân ngữ thường là sự vật trừu tượng, như 特色，特点，兴趣，水平，意义, tức là đặc sắc, đặc điểm, hứng thú, trình độ, ý nghĩa."),
         F(1, "Ví dụ: 我喜欢看具有民族风情的电视节目。 Tôi thích xem những chương trình truyền hình mang phong vị dân tộc. Phong vị là thứ trừu tượng, vốn có trong chương trình, nên dùng 具有."),
         F(0, "Vì vậy câu 他具有一套大房子 là sai, vì nhà cửa là tài sản cụ thể mà người ta sở hữu; phải nói 他拥有一套大房子。"),
         F(1, "Ngược lại, câu 这次改革拥有伟大意义 là sai, vì ý nghĩa là thứ trừu tượng; phải nói 这次改革具有伟大意义。"),
         "Mẹo nhớ: 拥有 là ôm trong tay, dùng cho của cải, tài nguyên, quyền lợi; còn 具有 là mang trong mình, dùng cho đặc điểm, ý nghĩa, giá trị."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: chọn 拥有 hay 具有", reveal=True, size=38,
    items=["(1) 柴达木盆地______22万平方公里的面积。",
           "Đáp án: 拥有 – diện tích, đất đai là thứ sở hữu",
           "(2) 这次改革______划时代的伟大意义。",
           "Đáp án: 具有 – ý nghĩa là sự vật trừu tượng",
           "(3) 每个公民都______选举权和被选举权。",
           "Đáp án: 拥有 – quyền lợi thuộc nhóm thứ được sở hữu",
           "(4) 这项工艺______相当高的技术水准。",
           "Đáp án: 具有 – trình độ, tiêu chuẩn là thứ trừu tượng"],
    say=[F(0, "Bây giờ chúng ta làm thử: chọn 拥有 hay 具有 để điền vào chỗ trống. Câu một: 柴达木盆地什么二十二万平方公里的面积。 Bồn địa Sài Đạt Mộc có diện tích hai mươi hai vạn ki-lô-mét vuông. Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: 拥有. 柴达木盆地拥有二十二万平方公里的面积。 Diện tích đất đai là thứ to lớn được sở hữu, giống 土地 trong bảng so sánh."),
         F(2, "Câu hai: 这次改革什么划时代的伟大意义。 Cuộc cải cách lần này có ý nghĩa vĩ đại, mở ra một thời đại mới."),
         F(3, "Đáp án: 具有. 这次改革具有划时代的伟大意义。 Ý nghĩa là thứ trừu tượng, nên dùng 具有."),
         F(4, "Câu ba: 每个公民都什么选举权和被选举权。 Mỗi công dân đều có quyền bầu cử và quyền ứng cử."),
         F(5, "Đáp án: 拥有. 每个公民都拥有选举权和被选举权。 Sách xếp 权利, quyền lợi, vào nhóm của 拥有."),
         F(6, "Câu bốn: 这项工艺什么相当高的技术水准。 Kỹ thuật thủ công này có trình độ kỹ thuật khá cao."),
         F(7, "Đáp án: 具有. 这项工艺具有相当高的技术水准。 水准 giống 水平, là thứ trừu tượng, nên dùng 具有.")])

# ======================= MỞ RỘNG: CÂU THỪA THÀNH PHẦN =======================
add("bullets", chapter="Mở rộng: câu thừa thành phần", section="Mở rộng 扩展", title="Câu sai: thừa thành phần (成分冗余)", size=34,
    items=["Câu đã đủ cấu trúc, ý đã rõ, nhưng lại thêm từ ngữ không cần thiết",
           "## (1) Lặp chủ ngữ (主语重复)",
           "Sai: 我们班同学，上课的时候，我们都能专心听讲，认真思考问题。",
           "Sửa: bỏ chữ 我们 thứ hai → 我们班同学上课的时候都能专心听讲……",
           "## (2) Lặp tân ngữ (宾语重复)",
           "Sai: 一想起我教过的学生，真的打心眼里舍不得离开这些学生。",
           "Sửa: bỏ 这些学生 ở cuối câu, hoặc đổi thành 他们"],
    say=["Bây giờ chúng ta sang phần mở rộng của sách. Quyển này không có mục tu từ riêng, thay vào đó là kỹ năng nhận biết câu sai. Ở bài năm chúng ta đã học câu sai do thiếu thành phần; hôm nay là loại ngược lại: câu sai do thừa thành phần, tiếng Trung gọi là 成分冗余.",
         F(0, "成分冗余 là khi cấu trúc câu đã hoàn chỉnh, ý câu đã rõ ràng, nhưng lại xuất hiện thêm những từ ngữ không cần thiết. Câu như vậy bị coi là câu sai."),
         F(1, "Loại thứ nhất: lặp chủ ngữ, 主语重复."),
         F(2, "Câu sai: 我们班同学，上课的时候，我们都能专心听讲，认真思考问题。 Các bạn lớp chúng tôi, khi lên lớp, chúng tôi đều chăm chú nghe giảng, nghiêm túc suy nghĩ vấn đề."),
         F(3, "Chủ ngữ 我们班同学 đã có ở đầu câu, lại thêm 我们 lần nữa là thừa. Phải bỏ chữ 我们 thứ hai."),
         F(4, "Loại thứ hai: lặp tân ngữ, 宾语重复."),
         F(5, "Câu sai: 一想起我教过的学生，真的打心眼里舍不得离开这些学生。 Hễ nhớ đến những học sinh tôi từng dạy, tôi thật lòng không nỡ rời xa những học sinh này."),
         F(6, "这些学生 ở cuối câu lặp lại 学生 phía trước. Có thể bỏ đi, hoặc đổi thành 他们: 真的打心眼里舍不得离开他们。")])

add("bullets", section="Mở rộng 扩展", title="Câu sai: lặp phó từ, trạng ngữ, nghĩa từ", size=34,
    items=["## (3) Lặp phó từ (副词重复)",
           "Sai: 那个地方谁也都不想去。 → Sửa: 谁也不想去 / 谁都不想去",
           "## (4) Lặp trạng ngữ (状语重复)",
           "Sai: 我们碰到了一些困难，这个问题短时间内不可能很快得到解决。 → bỏ 短时间内 hoặc 很快",
           "## (5) Lặp nghĩa từ (词义重复)",
           "Sai: 人们如果连续看电视超过四个多小时，就会疲劳。 → bỏ 超过 hoặc 多"],
    say=[F(0, "Loại thứ ba: lặp phó từ, 副词重复."),
         F(1, "Câu sai: 那个地方谁也都不想去。 Từ chỉ bất kỳ ai như 谁, thường đi với 也 hoặc 都 phía sau, nhưng dùng cả 也 lẫn 都 thì thừa. Sửa thành 那个地方谁也不想去, hoặc 那个地方谁都不想去。 Chỗ đó chẳng ai muốn đi cả."),
         F(2, "Loại thứ tư: lặp trạng ngữ, 状语重复."),
         F(3, "Câu sai: 我们碰到了一些困难，这个问题短时间内不可能很快得到解决。 Hai trạng ngữ 短时间内 và 很快 trùng nghĩa nhau, chỉ cần giữ một: 这个问题短时间内不可能得到解决, hoặc 这个问题不可能很快得到解决。"),
         F(4, "Loại thứ năm: lặp nghĩa từ, 词义重复."),
         F(5, "Câu sai: 人们如果连续看电视超过四个多小时，就会疲劳。 超过 là vượt quá, 多 là hơn, hai từ trùng nghĩa. Sửa: 连续看电视超过四个小时, hoặc 连续看电视四个多小时。 Nếu xem ti vi liên tục hơn bốn tiếng thì sẽ mệt mỏi.")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chỉ ra lỗi và sửa lại (1)", reveal=True, size=34,
    items=["(1) 我始终不明白，他为什么要那样做的原因。",
           "Đáp án: 为什么 và 原因 trùng nghĩa → 我始终不明白他为什么要那样做。/ ……他那样做的原因。",
           "(2) 凡事要依靠群众，否则只靠自己，什么事也做不成。",
           "Đáp án: 否则 và 只靠自己 trùng ý → 凡事要依靠群众，否则什么事也做不成。",
           "(3) 经法院审理，违约经营的张某被判赔偿原告经济损失5万多余元。",
           "Đáp án: 多 và 余 trùng nghĩa → ……5万多元 / 5万余元。"],
    say=[F(0, "Luyện tập: chỉ ra lỗi của các câu sau và đề xuất cách sửa. Câu một: 我始终不明白，他为什么要那样做的原因。 Tôi mãi không hiểu, nguyên nhân vì sao anh ấy lại làm như vậy. Câu này thừa gì? Các bạn tạm dừng và suy nghĩ nhé."),
         F(1, "Đáp án: 为什么 và 原因 trùng nghĩa, đều hỏi về lý do. Sửa: 我始终不明白他为什么要那样做。 Hoặc: 我始终不明白他那样做的原因。"),
         F(2, "Câu hai: 凡事要依靠群众，否则只靠自己，什么事也做不成。 Mọi việc phải dựa vào quần chúng, nếu không, chỉ dựa vào bản thân, thì chẳng làm được việc gì."),
         F(3, "Đáp án: 否则 đã có nghĩa là nếu không dựa vào quần chúng, tức là chỉ dựa vào mình, nên 只靠自己 bị thừa. Sửa: 凡事要依靠群众，否则什么事也做不成。 Hoặc bỏ 否则: 凡事要依靠群众，只靠自己，什么事也做不成。"),
         F(4, "Câu ba: 经法院审理，违约经营的张某被判赔偿原告经济损失五万多余元。 Qua xét xử của tòa án, ông Trương kinh doanh vi phạm hợp đồng bị phán bồi thường cho nguyên đơn thiệt hại kinh tế hơn năm vạn tệ."),
         F(5, "Đáp án: 多 và 余 đều nghĩa là hơn, chỉ giữ một. Sửa: 五万多元, hoặc 五万余元。 Trong đó 余 mang màu sắc văn viết hơn.")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chỉ ra lỗi và sửa lại (2)", reveal=True, size=34,
    items=["(4) 这幅画是祖上传下来的，出自于名家之手。",
           "Đáp án: 自 đã có nghĩa là từ, trùng với 于 → ……出自名家之手。",
           "(5) 根据美国某大学研究所发布的《2013全球幸福指数报告》显示，丹麦成为世界最幸福的国家。",
           "Đáp án: 根据 và 显示 dùng chồng → bỏ 根据: 美国某大学研究所发布的《……》显示，…… / hoặc bỏ 显示: 根据……，丹麦成为……"],
    say=[F(0, "Câu bốn: 这幅画是祖上传下来的，出自于名家之手。 Bức tranh này là do tổ tiên truyền lại, xuất phát từ tay một danh họa. Câu này thừa gì?"),
         F(1, "Đáp án: 出自 đã có nghĩa là xuất phát từ, chữ 自 chính là từ, nên thêm 于 là thừa. Sửa: 这幅画是祖上传下来的，出自名家之手。"),
         F(2, "Câu năm: 根据美国某大学研究所发布的《二零一三全球幸福指数报告》显示，丹麦成为世界最幸福的国家。 Căn cứ vào Báo cáo chỉ số hạnh phúc toàn cầu năm hai nghìn không trăm mười ba do một viện nghiên cứu của một trường đại học Mỹ công bố cho thấy, Đan Mạch trở thành quốc gia hạnh phúc nhất thế giới."),
         F(3, "Đáp án: 根据 và 显示 dùng chồng lên nhau, khiến câu mất chủ ngữ của 显示. Cách sửa thứ nhất: bỏ 根据, để bản báo cáo làm chủ ngữ của 显示. Cách sửa thứ hai: bỏ 显示, giữ 根据 làm trạng ngữ: 根据……报告，丹麦成为世界最幸福的国家。"),
         "Mẹo: khi gặp câu thừa thành phần, hãy tìm những từ trùng nghĩa với nhau, như 为什么 với 原因, 多 với 余, 超过 với 多, 自 với 于, rồi bỏ đi một từ."])

add("bullets", section="Mở rộng 扩展", title="Mở rộng 扩展: từ vựng – danh từ và thiên nhiên", size=34,
    items=["## (1) Danh từ qua hình ảnh",
           "泡沫 bọt: 洗手时一定要把泡沫清洗干净。 · 杂技 xiếc: 我喜欢看杂技表演。",
           "书法 thư pháp: 这是一幅书法作品。 · 压岁钱 tiền mừng tuổi: 过春节时，大人要给孩子压岁钱。",
           "塔 tháp: 远处有一座塔。 · 亭子 cái đình, chòi nghỉ: 河边有一个小亭子。",
           "## (2) Từ ngữ về thiên nhiên 自然",
           "天气: 冰雹 mưa đá · 台风 bão · 气象 khí tượng · 气压 khí áp",
           "资源: 淡水 nước ngọt · 天然气 khí thiên nhiên · 宇宙: 太空 không gian vũ trụ"],
    say=["Phần mở rộng thứ hai của sách là từ vựng. Thầy đọc qua để các bạn làm quen nhé.",
         F(0, "Nhóm thứ nhất là sáu danh từ, sách minh họa bằng hình ảnh."),
         F(1, "泡沫, bọt: 洗手时一定要把泡沫清洗干净。 Khi rửa tay nhất định phải rửa sạch bọt xà phòng. 杂技, xiếc, tạp kỹ: 我喜欢看杂技表演。 Tôi thích xem biểu diễn xiếc."),
         F(2, "书法, thư pháp: 这是一幅书法作品。 Đây là một tác phẩm thư pháp. 压岁钱, tiền mừng tuổi: 过春节时，大人要给孩子压岁钱。 Dịp Tết, người lớn mừng tuổi cho trẻ con."),
         F(3, "塔, tháp: 远处有一座塔。 Ở đằng xa có một ngọn tháp. 亭子, cái đình nhỏ, chòi nghỉ chân: 河边有一个小亭子。 Bên sông có một chòi nghỉ nhỏ."),
         F(4, "Nhóm thứ hai là từ ngữ về thiên nhiên, tiếng Trung là 自然, chia thành ba nhánh: 天气，资源，宇宙."),
         F(5, "Về 天气, thời tiết: 冰雹，台风，气象，气压. Tức là mưa đá, bão, khí tượng, và khí áp."),
         F(6, "Về 资源, tài nguyên: 淡水，天然气, tức là nước ngọt và khí thiên nhiên. Về 宇宙, vũ trụ: 太空, không gian vũ trụ. Những từ này rất hữu ích khi các bạn viết bài giới thiệu một danh lam thắng cảnh.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ có dấu chấm", size=40,
    items=["雕刻 (雕) → 雕塑 · 雕花 · 雕像 · 石雕",
           "枯萎 (枯) → 干枯 · 枯黄 · 枯燥 · 枯竭",
           "震撼 (震) → 震动 · 震惊 · 地震 · 震耳欲聋",
           "辛勤 (辛) → 辛苦 · 艰辛 · 辛劳 · 辛酸",
           "珍稀 (珍) → 珍贵 · 珍惜 · 珍珠 · 珍品"],
    say=["Phần luyện tập. Bài tập một: mô phỏng ví dụ, viết thêm các từ có chứa chữ được đánh dấu chấm. Trong bài này, chữ được đánh dấu đều là chữ đầu tiên.",
         F(0, "Ví dụ mẫu: 雕刻, chữ được đánh dấu là chữ 雕, nghĩa là chạm khắc. Ta có 雕塑，雕花，雕像，石雕. Tức là điêu khắc, hoa văn chạm khắc, bức tượng, và tượng đá."),
         F(1, "枯萎, chữ được đánh dấu là chữ 枯, nghĩa là khô. Ta có 干枯，枯黄，枯燥，枯竭. Tức là khô héo, úa vàng, khô khan, và cạn kiệt. Chú ý 枯燥 là khô khan, nhàm chán, dùng cho công việc, bài giảng."),
         F(2, "震撼, chữ được đánh dấu là chữ 震, nghĩa là rung chuyển. Ta có 震动，震惊，地震，震耳欲聋. Tức là rung động, kinh ngạc, động đất, và thành ngữ 震耳欲聋, to đến điếc cả tai."),
         F(3, "辛勤, chữ được đánh dấu là chữ 辛, nghĩa là vất vả, cay đắng. Ta có 辛苦，艰辛，辛劳，辛酸. Tức là vất vả, gian khổ, cực nhọc, và chua xót."),
         F(4, "珍稀, chữ được đánh dấu là chữ 珍, nghĩa là quý. Ta có 珍贵，珍惜，珍珠，珍品. Tức là quý giá, quý trọng, ngọc trai, và vật quý.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (1)", reveal=True, size=36,
    items=["(1) 几十年过去了，这个地方还是贫穷落后。（依旧）",
           "Đáp án: 几十年过去了，这个地方依旧贫穷落后。",
           "(2) 他们玩儿得兴高采烈，一会儿唱歌，一会儿跳舞。（时而……，时而……）",
           "Đáp án: 他们玩儿得兴高采烈，时而唱歌，时而跳舞。",
           "(3) 他患上了一种非常少见的疾病，连最有经验的大夫都感到头疼。（罕见）",
           "Đáp án: 他患上了一种非常罕见的疾病，连最有经验的大夫都感到头疼。"],
    say=[F(0, "Bài tập hai: dùng từ hoặc cấu trúc cho sẵn để viết lại câu. Câu một, dùng 依旧: 几十年过去了，这个地方还是贫穷落后。 Mấy chục năm trôi qua, nơi này vẫn nghèo nàn lạc hậu. Các bạn tạm dừng và thử viết lại nhé."),
         F(1, "Đáp án: thay 还是 bằng 依旧: 几十年过去了，这个地方依旧贫穷落后。 Ở đây 依旧 đứng trước tính từ, giống 仍然."),
         F(2, "Câu hai, dùng 时而……，时而……: 他们玩儿得兴高采烈，一会儿唱歌，一会儿跳舞。 Họ chơi đùa vui vẻ hớn hở, lúc thì hát, lúc thì nhảy."),
         F(3, "Đáp án: 他们玩儿得兴高采烈，时而唱歌，时而跳舞。 Mẫu khẩu ngữ 一会儿……一会儿…… được đổi thành mẫu văn viết 时而……时而……."),
         F(4, "Câu ba, dùng 罕见: 他患上了一种非常少见的疾病，连最有经验的大夫都感到头疼。 Anh ấy mắc một căn bệnh rất ít gặp, đến bác sĩ giàu kinh nghiệm nhất cũng thấy đau đầu."),
         F(5, "Đáp án: thay 少见 bằng 罕见: 他患上了一种非常罕见的疾病。 Anh ấy mắc một căn bệnh vô cùng hiếm gặp.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (2)", reveal=True, size=36,
    items=["(4) 他要做的事情，谁也拦不住，你们就别管他了。（阻拦）",
           "Đáp án: 他要做的事情，谁也阻拦不了，你们就别管他了。",
           "(5) 她亲眼看到自己的家被大火烧掉了，内心非常痛苦。（目睹）",
           "Đáp án: 她目睹自己的家被大火烧掉了，内心非常痛苦。",
           "(6) 由于小王做事能坚持到底、不放弃，所以最后取得了成功。（锲而不舍）",
           "Đáp án: 由于小王做事锲而不舍，所以最后取得了成功。"],
    say=[F(0, "Câu bốn, dùng 阻拦: 他要做的事情，谁也拦不住，你们就别管他了。 Việc anh ấy muốn làm thì chẳng ai cản nổi, các bạn đừng quản anh ấy nữa."),
         F(1, "Đáp án: 他要做的事情，谁也阻拦不了，你们就别管他了。 Giống câu trong bài khóa: 任何困难也阻拦不了他们."),
         F(2, "Câu năm, dùng 目睹: 她亲眼看到自己的家被大火烧掉了，内心非常痛苦。 Cô ấy tận mắt nhìn thấy nhà mình bị lửa thiêu rụi, trong lòng vô cùng đau khổ."),
         F(3, "Đáp án: 她目睹自己的家被大火烧掉了，内心非常痛苦。 Vì 目睹 đã có nghĩa là tận mắt thấy, nên thay cả cụm 亲眼看到. Cũng có thể nói 亲眼目睹."),
         F(4, "Câu sáu, dùng 锲而不舍: 由于小王做事能坚持到底、不放弃，所以最后取得了成功。 Vì Tiểu Vương làm việc kiên trì đến cùng, không bỏ cuộc, nên cuối cùng đã thành công."),
         F(5, "Đáp án: 由于小王做事锲而不舍，所以最后取得了成功。 Thành ngữ 锲而不舍 thay cho cả cụm 坚持到底、不放弃.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (1)", reveal=True, size=34,
    items=["## Từ cho sẵn: 庄稼 · 牲畜 · 干旱 · 耕地 · 枯萎",
           "连续几个月没下雨，我国西部地区遭遇了几十年不遇的___，___大面积___，人和___饮水困难，旱情十分严重。但勤劳的农民们想方设法从各地运水来浇灌___，使得农作物没有大面积绝收。",
           "Đáp án: 干旱 · 庄稼 · 枯萎 · 牲畜 · 耕地"],
    say=[F(0, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn một có năm từ: 庄稼，牲畜，干旱，耕地，枯萎."),
         F(1, "连续几个月没下雨，我国西部地区遭遇了几十年不遇的什么，什么大面积什么，人和什么饮水困难，旱情十分严重。但勤劳的农民们想方设法从各地运水来浇灌什么，使得农作物没有大面积绝收。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 几十年不遇的干旱，庄稼大面积枯萎，人和牲畜饮水困难，运水来浇灌耕地。 Liên tục mấy tháng không mưa, vùng phía tây nước ta gặp trận hạn hán mấy chục năm mới có, hoa màu khô héo trên diện rộng, người và gia súc khó có nước uống. Nhưng những người nông dân cần cù đã tìm mọi cách chở nước từ khắp nơi về tưới ruộng, nhờ vậy cây trồng không bị mất trắng. Các bạn thấy không, đoạn này rất giống câu mở đầu của bài khóa.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (2)", reveal=True, size=34,
    items=["## Từ cho sẵn: 珍稀 · 审美 · 生态 · 遗产 · 陶醉",
           "九寨沟是中国第一个以保护自然风景为主要目的的自然保护区。它像一幅美丽画卷展示在人们面前，令人___。由于风景优美，___环境良好，它获得了“世界自然___”的称号。除了具有很高的___价值，九寨沟还蕴藏着丰富、___的动植物资源。",
           "Đáp án: 陶醉 · 生态 · 遗产 · 审美 · 珍稀"],
    say=[F(0, "Đoạn hai có năm từ: 珍稀，审美，生态，遗产，陶醉."),
         F(1, "九寨沟是中国第一个以保护自然风景为主要目的的自然保护区。它像一幅美丽画卷展示在人们面前，令人什么。由于风景优美，什么环境良好，它获得了世界自然什么的称号。除了具有很高的什么价值，九寨沟还蕴藏着丰富、什么的动植物资源。 Các bạn điền thử nhé."),
         F(2, "Đáp án: 令人陶醉，生态环境良好，世界自然遗产，很高的审美价值，丰富、珍稀的动植物资源。 Cửu Trại Câu là khu bảo tồn thiên nhiên đầu tiên của Trung Quốc lấy bảo vệ phong cảnh tự nhiên làm mục đích chính. Nó như một bức tranh tuyệt đẹp bày ra trước mắt, khiến người ta say đắm. Nhờ phong cảnh đẹp, môi trường sinh thái tốt, nơi đây được công nhận là di sản thiên nhiên thế giới. Ngoài giá trị thẩm mỹ cao, Cửu Trại Câu còn có nguồn động thực vật phong phú và quý hiếm.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 4: Đọc đoạn văn, mô phỏng đặt câu", reveal=True, size=34,
    items=["尽管已目睹这奇迹无数次，但我每次身临其境，都会为哈尼族的山民们在这重重叠叠的山脉上雕塑出的美丽画卷而震惊。",
           "Đáp án: 尽管我已经去过长城很多次，但每次登上长城，都会为它的雄伟而感叹。",
           "面对大山，山民们没有对抗，而是选择了服从——他们服从自然规律，选择开辟梯田这种农耕方式，最终与大自然和谐相处。",
           "Đáp án: 面对困难，他没有放弃，而是选择了坚持——他每天练习到深夜，最终取得了好成绩。"],
    say=[F(0, "Bài tập bốn: đọc đoạn văn, rồi mô phỏng để đặt câu. Câu mẫu một: 尽管已目睹这奇迹无数次，但我每次身临其境，都会为哈尼族的山民们在这重重叠叠的山脉上雕塑出的美丽画卷而震惊。 Khung câu là: 尽管什么，但什么，都什么。 Các bạn thử viết nhé."),
         F(1, "Đáp án gợi ý: 尽管我已经去过长城很多次，但每次登上长城，都会为它的雄伟而感叹。 Mặc dù tôi đã đến Trường Thành nhiều lần, nhưng mỗi lần leo lên, tôi đều trầm trồ trước sự hùng vĩ của nó."),
         F(2, "Câu mẫu hai: 面对大山，山民们没有对抗，而是选择了服从，他们服从自然规律，选择开辟梯田这种农耕方式，最终与大自然和谐相处。 Khung câu là: 面对什么，某人没有什么，而是选择什么，最终什么。"),
         F(3, "Đáp án gợi ý: 面对困难，他没有放弃，而是选择了坚持，他每天练习到深夜，最终取得了好成绩。 Đối mặt với khó khăn, anh ấy không bỏ cuộc, mà chọn cách kiên trì: ngày nào cũng luyện tập đến khuya, cuối cùng đạt được thành tích tốt.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 15", size=34,
    items=["Từ vựng trọng tâm: 山脉 · 梯田 · 壮丽 · 依旧 · 衬托 · 纵横 · 汹涌 · 目睹 · 震撼 · 锲而不舍 · 罕见 · 珍稀 · 陶醉",
           "Ngữ pháp: 时而 (lúc thì…, lúc thì…; thỉnh thoảng) · 不禁 (không kìm được) · 无不 (tất cả đều)",
           "Phân biệt: 拥有 (sở hữu thứ nhiều, quý giá) ≠ 具有 (mang đặc điểm, ý nghĩa trừu tượng)",
           "Mở rộng: câu thừa thành phần – lặp chủ ngữ, tân ngữ, phó từ, trạng ngữ, nghĩa từ",
           "## Bài tập về nhà (运用)",
           "Viết bài ít nhất 400 chữ, đề 我熟悉的……: giới thiệu một danh lam thắng cảnh mà bạn quen thuộc"],
    say=["Chúng ta cùng tổng kết bài mười lăm.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 山脉，梯田，壮丽，依旧，衬托，纵横，汹涌，目睹，震撼，锲而不舍，罕见，珍稀，陶醉. Và đừng quên cách đọc của những chữ đa âm như 牲畜，重叠，不禁，心血，种子."),
         F(1, "Về ngữ pháp: 时而 dùng hai lần trở lên là lúc thì…, lúc thì…; dùng một lần là thỉnh thoảng. 不禁 là không kìm được, bất giác. 无不 là không cái nào không, tức là tất cả đều, chủ ngữ phải là số nhiều."),
         F(2, "Về phân biệt từ: 拥有 nhấn mạnh sở hữu những thứ nhiều và quý giá như tài nguyên, đất đai, quyền lợi; còn 具有 nhấn mạnh sự tồn tại của những thứ trừu tượng như đặc điểm, ý nghĩa, trình độ."),
         F(3, "Về phần mở rộng: câu sai do thừa thành phần, như lặp chủ ngữ, lặp tân ngữ, lặp phó từ, lặp trạng ngữ, và lặp nghĩa từ. Cách sửa là tìm từ trùng nghĩa và bỏ đi một từ."),
         F(5, "Bài tập về nhà, theo phần vận dụng của sách: bài khóa giới thiệu ruộng bậc thang Hà Nhì ở Vân Nam. Hãy mô phỏng bài khóa, lấy đề 我熟悉的……, giới thiệu một danh lam thắng cảnh hoặc phong cảnh thiên nhiên mà bạn quen thuộc, ví dụ vịnh Hạ Long, Sa Pa, hay ruộng bậc thang Mù Cang Chải. Nội dung nên gồm vị trí địa lý, môi trường xung quanh, những thay đổi trong lịch sử, và giá trị văn hóa hoặc thiên nhiên. Viết ít nhất bốn trăm chữ. Nhớ thử dùng 时而，不禁，无不 trong bài viết nhé."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Mong rằng mỗi lần ngắm một cảnh đẹp, các bạn cũng sẽ nghĩ đến bàn tay và tâm huyết của con người đã làm nên nó. Hẹn gặp lại các bạn ở bài mười sáu: 徐健和他的野生动物摄影师们, Từ Kiện và các nhà nhiếp ảnh động vật hoang dã. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Thượng) – Bài 15: 山脉上的雕刻 (Các tác phẩm điêu khắc trên dãy núi)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    # Thứ tự có ý nghĩa: khóa dài phải đứng trước khóa ngắn nằm bên trong nó.
    "tts_replace": {"重重叠叠": "虫虫叠叠",    # chóngchóngdiédié
                    "重叠": "虫叠",            # chóngdié
                    "重复": "虫复",            # chóngfù
                    "画卷": "画倦",            # huàjuàn
                    "席卷": "席捲",            # xíjuǎn
                    "卷了起来": "捲了起来",    # juǎn
                    "卷。": "捲。",            # juǎn (từ đơn trong phần từ mới)
                    "铺": "扑",                # pū (bài này không có 铺 đọc pù)
                    "牲畜": "牲触",            # shēngchù
                    "漂浮": "飘浮",            # piāofú
                    "不禁": "不今",            # bùjīn
                    "曲子": "取子",            # qǔzi
                    "种子": "肿子",            # zhǒngzi
                    "种植": "众植",            # zhòngzhí
                    "锲而不舍": "锲而不捨",    # qiè'érbùshě
                    "舍不得": "捨不得",        # shěbude
                    "开辟": "开僻",            # kāipì
                    "心血": "心谑",            # xīnxuè
                    "相处": "相楚",            # xiāngchǔ
                    "远处": "远触",            # yuǎnchù
                    "为哈尼族": "位哈尼族",    # wèi (vì)
                    "为背景": "维背景",        # yǐ…wéi bèijǐng
                    "为主要目的": "维主要目的",  # yǐ…wéi zhǔyào mùdì
                    "过不了": "过不蓼",        # guòbuliǎo
                    "阻拦不了": "阻拦不蓼",    # zǔlán bu liǎo
                    "庄稼长得": "庄稼涨得",    # zhǎng
                    "应有": "英有",            # yīngyǒu
                    "称快": "撑快",            # chēngkuài
                    "一针见血": "一针见写",    # yì zhēn jiàn xiě
                    "划时代": "画时代",        # huàshídài
                    "大夫": "代夫",            # dàifu
                    "兴高采烈": "幸高采烈",    # xìnggāo
                    "教过": "交过",            # jiāo guo
                    "干草": "甘草",            # gāncǎo
                    "干花": "甘花",            # gānhuā
                    "干渴": "甘渴",            # gānkě
                    "干裂": "甘裂",            # gānliè
                    "干枯": "甘枯",            # gānkū
                    "风干": "风甘",            # fēnggān
                    "晒干": "晒甘",            # shàigān
                    "晾干": "晾甘"},           # liànggān
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai15.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
