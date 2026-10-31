#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Hạ) – Bài 37 «警察的故事». Chạy để sinh bai37.json."""
import json
import os

TAG = "HSK 6 (Hạ) · Bài 37 · 警察的故事"
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
    zh="警察的故事", py="Jǐngchá de gùshi", vi="Bài 37: Những câu chuyện về cảnh sát",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Hạ.",
         "Hôm nay chúng ta học bài ba mươi bảy: 警察的故事。 Nghĩa là: Những câu chuyện về cảnh sát.",
         "Đây là bài mở đầu của Đơn vị mười, chủ đề 热点追踪, Theo dấu điểm nóng. Bài khóa gồm ba câu chuyện có thật, cải biên từ báo chí: một nữ cảnh sát giỏi giám định vân tay, một cảnh sát phòng chống ma túy mưu trí, và một chú chó nghiệp vụ đã hy sinh cả cuộc đời cho công việc chống ma túy."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu nội dung ba câu chuyện trong bài khóa 警察的故事",
           "Nắm vững 55 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: cấu trúc 为……起见 và phó từ 暂且",
           "Phân biệt hai từ 恐惧 và 恐怖",
           "Kỹ năng viết: hô ứng trước sau (照应)"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung ba câu chuyện trong bài khóa, và cảm nhận được sự vất vả, tận tụy của những người làm cảnh sát."),
         F(1, "Thứ hai, nắm vững năm mươi lăm từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ. Bài này có nhiều từ về điều tra phá án, rất hữu ích khi đọc tin tức."),
         F(2, "Thứ ba, học hai điểm ngữ pháp: cấu trúc 为了……起见, nghĩa là để cho, vì mục đích; và phó từ 暂且, nghĩa là tạm thời, tạm."),
         F(3, "Thứ tư, phân biệt hai từ cùng có nghĩa sợ hãi: 恐惧 và 恐怖."),
         F(4, "Thứ năm, một kỹ năng viết rất hay: hô ứng trước sau, tiếng Trung gọi là 照应. Chính bài khóa hôm nay là một ví dụ mẫu mực."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Câu hỏi khởi động", size=40,
    items=["请对照图片熟悉下列词语。你觉得哪些图片与警察有关系？",
           "指纹 zhǐwén – vân tay",
           "舌头 shétou – cái lưỡi",
           "粉末 fěnmò – bột",
           "警犬 jǐngquǎn – chó nghiệp vụ (chó cảnh sát)",
           "农用车 nóngyòngchē – xe nông dụng"],
    say=[F(0, "Chúng ta bắt đầu bằng phần khởi động. Sách cho năm bức tranh và hỏi: 请对照图片熟悉下列词语。你觉得哪些图片与警察有关系？ Hãy đối chiếu tranh để làm quen với các từ sau. Bạn thấy những bức tranh nào có liên quan đến cảnh sát?"),
         F(1, "指纹, vân tay. Cảnh sát dùng dấu vân tay để tìm ra thủ phạm. Đây chính là nội dung câu chuyện thứ nhất."),
         F(2, "舌头, cái lưỡi. Trong câu chuyện thứ ba, chú chó nghiệp vụ mỗi lần gặp người huấn luyện là thè lưỡi ra liếm."),
         F(3, "粉末, bột. Ma túy dạng bột xuất hiện ở cuối câu chuyện thứ ba, và đó là một chi tiết rất xúc động."),
         F(4, "警犬, chó nghiệp vụ, tức là chó của cảnh sát. Chữ 犬 nghĩa là con chó, dùng trong văn viết."),
         F(5, "农用车, xe nông dụng, loại xe chở hàng ở nông thôn. Trong câu chuyện thứ hai, bọn buôn ma túy lái loại xe này đến điểm giao hàng."),
         "Như vậy, cả năm bức tranh đều liên quan đến các câu chuyện về cảnh sát trong bài hôm nay. Các bạn hãy tạm dừng và thử nói xem mình biết gì về công việc của cảnh sát nhé."])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 指 và 查", size=36,
    items=["## 指 (chỉ): ngón tay; chỉ, trỏ",
           "指纹 vân tay · 指尖 đầu ngón tay · 指头 ngón tay · 指甲 móng tay · 指环 nhẫn · 指印 dấu ngón tay",
           "手指 ngón tay · 拇指 ngón cái · 食指 ngón trỏ · 中指 ngón giữa · 小指 ngón út · 无名指 ngón áp út · 了如指掌 rõ như lòng bàn tay",
           "## 查 (tra): kiểm tra, tra xét",
           "勘查 khám nghiệm · 检查 kiểm tra · 抽查 kiểm tra xác suất · 复查 kiểm tra lại · 审查 thẩm tra · 搜查 lục soát · 巡查 tuần tra · 查对 đối chiếu",
           "查封 niêm phong · 查获 tra bắt, thu giữ · 查看 xem xét · 查票 soát vé · 查收 kiểm nhận · 查验 kiểm nghiệm · 查账 kiểm tra sổ sách"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo, rất có lợi cho người Việt vì hầu hết các chữ đều có âm Hán Việt quen thuộc.",
         F(0, "Nhóm thứ nhất có chữ 指, Hán Việt là chỉ, nghĩa là ngón tay, hoặc chỉ, trỏ."),
         F(1, "指纹，指尖，指头，指甲，指环，指印。 Tức là: vân tay, đầu ngón tay, ngón tay, móng tay, chiếc nhẫn, và dấu ngón tay. Trong bài khóa, 指纹 và 指尖 xuất hiện rất nhiều lần."),
         F(2, "手指，拇指，食指，中指，小指，无名指，了如指掌。 Tức là: ngón tay, ngón cái, ngón trỏ, ngón giữa, ngón út, ngón áp út, và thành ngữ 了如指掌, hiểu rõ như lòng bàn tay."),
         F(3, "Nhóm thứ hai xoay quanh các từ như 检查 và 查获. Chữ chung ở đây Hán Việt là tra, nghĩa là kiểm tra, tra xét."),
         F(4, "勘查，检查，抽查，复查，审查，搜查，巡查，查对。 Tức là: khám nghiệm, kiểm tra, kiểm tra xác suất, kiểm tra lại, thẩm tra, lục soát, tuần tra, và đối chiếu. 勘查 có trong bài khóa: 现场勘查, khám nghiệm hiện trường."),
         F(5, "查封，查获，查看，查票，查收，查验，查账。 Tức là: niêm phong, tra bắt và thu giữ, xem xét, soát vé, kiểm nhận, kiểm nghiệm, và kiểm tra sổ sách. 查获 là một từ mới của bài.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 形 và 关", size=36,
    items=["## 形 (hình): hình dạng, hình thể",
           "变形 biến dạng · 方形 hình vuông · 圆形 hình tròn · 地形 địa hình · 口形 khẩu hình · 情形 tình hình · 人形 hình người · 图形 hình vẽ",
           "外形 hình dáng bên ngoài · 形状 hình dạng · 形态 hình thái · 形象 hình tượng · 奇形怪状 hình thù kỳ quái",
           "## 关 (quan): đóng, nhốt",
           "关押 giam giữ · 关闭 đóng cửa · 关门 đóng cửa · 关窗 đóng cửa sổ · 关上 đóng lại",
           "关紧 đóng chặt · 关起来 nhốt lại · 关进去 nhốt vào · 开关 công tắc"],
    say=[F(0, "Nhóm thứ ba có chữ 形, Hán Việt là hình, nghĩa là hình dạng, hình thể."),
         F(1, "变形，方形，圆形，地形，口形，情形，人形，图形。 Tức là: biến dạng, hình vuông, hình tròn, địa hình, khẩu hình, tình hình, hình người, hình vẽ. Bài khóa có 指纹严重变形, dấu vân tay bị biến dạng nghiêm trọng, và 山里地形复杂, địa hình trong núi phức tạp."),
         F(2, "外形，形状，形态，形象，奇形怪状。 Tức là: hình dáng bên ngoài, hình dạng, hình thái, hình tượng, và 奇形怪状, hình thù kỳ quái."),
         F(3, "Nhóm cuối cùng có chữ 关, Hán Việt là quan, ở đây mang nghĩa đóng lại, nhốt lại."),
         F(4, "关押，关闭，关门，关窗，关上。 Tức là: giam giữ, đóng cửa, đóng cửa, đóng cửa sổ, đóng lại. 关押 có trong bài khóa: 因刑事犯罪被关押, bị giam giữ vì phạm tội hình sự."),
         F(5, "关紧，关起来，关进去，开关。 Tức là: đóng chặt, nhốt lại, nhốt vào, và công tắc. Các bạn thấy đấy, nắm được nghĩa một chữ gốc là đoán được cả một nhóm từ.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng)
V = [
    ("化妆", "huàzhuāng", "hóa trang", "động từ", "trang điểm", "她每天出门前都要化妆。", "Ngày nào trước khi ra ngoài cô ấy cũng trang điểm.",
     "Động từ, nghĩa là trang điểm. Đây là một từ dễ nhầm: âm Hán Việt là hóa trang, nhưng nghĩa là trang điểm cho đẹp. Còn hóa trang theo nghĩa tiếng Việt, tức là cải trang thành người khác, thì tiếng Trung viết là 化装, với chữ 装 trong 服装. Bài khóa có cả hai: 正在化妆的女士 là người phụ nữ đang trang điểm, còn 化装行动 là hành động cải trang."),
    ("屑", "xiè", "tiết", "danh từ", "vụn, mảnh vụn", "桌子上掉了很多面包屑。", "Trên bàn rơi rất nhiều vụn bánh mì.",
     "Danh từ, nghĩa là vụn, mảnh vụn, thường đứng sau một danh từ khác: 纸屑 là giấy vụn, 面包屑 là vụn bánh mì."),
    ("抢劫", "qiǎngjié", "thưởng kiếp", "động từ", "cướp, cướp bóc", "那个男人抢劫了一家商店。", "Gã đàn ông đó đã cướp một cửa hàng.",
     "Động từ, nghĩa là cướp, dùng vũ lực để cướp tài sản. 抢劫案 là vụ cướp, 入室抢劫 là đột nhập vào nhà để cướp."),
    ("痕迹", "hénjì", "ngân tích", "danh từ", "dấu vết", "现场没有留下任何痕迹。", "Hiện trường không để lại bất kỳ dấu vết nào.",
     "Danh từ, nghĩa là dấu vết. 犯罪痕迹 là dấu vết phạm tội, 痕迹检验 là giám định dấu vết."),
    ("停顿", "tíngdùn", "đình đốn", "động từ", "ngừng lại; đình trệ", "他说到这里停顿了一下。", "Nói đến đây anh ấy ngừng lại một chút.",
     "Động từ, nghĩa là ngừng lại, tạm dừng; cũng chỉ công việc bị đình trệ, như 侦破工作陷入停顿, công tác phá án rơi vào bế tắc. Tiếng Việt đình đốn thường nói về kinh tế, sản xuất bị ngưng trệ; còn 停顿 dùng rộng hơn, ngay cả ngừng một chút khi nói cũng dùng được."),
    ("嫌疑", "xiányí", "hiềm nghi", "danh từ", "sự tình nghi, hiềm nghi", "警察认为他有很大的嫌疑。", "Cảnh sát cho rằng hắn bị tình nghi rất lớn.",
     "Danh từ, nghĩa là sự tình nghi. 有嫌疑 là bị tình nghi, 犯罪嫌疑人 là nghi phạm, một từ rất hay gặp trong tin tức."),
    ("线索", "xiànsuǒ", "tuyến tác", "danh từ", "manh mối", "这枚指纹是唯一的线索。", "Dấu vân tay này là manh mối duy nhất.",
     "Danh từ, nghĩa là manh mối, đầu mối để lần ra sự việc. 提供线索 là cung cấp manh mối."),
    ("歹徒", "dǎitú", "đãi đồ", "danh từ", "kẻ gian, tên côn đồ", "警察很快抓住了歹徒。", "Cảnh sát nhanh chóng bắt được tên côn đồ.",
     "Danh từ, nghĩa là kẻ gian, tên côn đồ. Chữ 歹 nghĩa là xấu, ác; chữ 徒 nghĩa là kẻ, như trong 匪徒, kẻ cướp."),
    ("恐惧", "kǒngjù", "khủng cụ", "tính từ", "sợ hãi, khiếp sợ", "孩子对黑暗充满了恐惧。", "Đứa trẻ đầy sợ hãi trước bóng tối.",
     "Tính từ, nghĩa là sợ hãi, nói về tâm lý của con người. Lát nữa ta sẽ phân biệt kỹ 恐惧 với 恐怖."),
    ("铜", "tóng", "đồng", "danh từ", "đồng (kim loại)", "这座雕像是用铜做的。", "Bức tượng này làm bằng đồng.",
     "Danh từ, nghĩa là đồng, một loại kim loại. 铜制 là làm bằng đồng, 铜牌 là huy chương đồng."),
    ("框架", "kuàngjià", "khuông giá", "danh từ", "khung; khuôn khổ", "这扇窗户的框架是铜制的。", "Khung cửa sổ này làm bằng đồng.",
     "Danh từ, nghĩa là cái khung, như khung cửa, khung kính. Nghĩa bóng là khuôn khổ, dàn ý, ví dụ 文章的框架, dàn ý bài văn."),
    ("残留", "cánliú", "tàn lưu", "động từ", "còn sót lại", "杯子上残留着他的指纹。", "Trên chiếc cốc còn sót lại dấu vân tay của anh ta.",
     "Động từ, nghĩa là còn sót lại một phần. Trong bài: 指纹只残留有指尖部位, dấu vân tay chỉ còn sót lại phần đầu ngón tay."),
    ("刑事", "xíngshì", "hình sự", "tính từ", "hình sự", "他因刑事犯罪被判刑。", "Hắn bị kết án vì phạm tội hình sự.",
     "Tính từ, âm Hán Việt giống hệt tiếng Việt. 刑事案件 là vụ án hình sự, đối lập với 民事, dân sự."),
    ("监狱", "jiānyù", "giám ngục", "danh từ", "nhà tù", "他在监狱里度过了三年。", "Anh ta đã trải qua ba năm trong tù.",
     "Danh từ, nghĩa là nhà tù. 出狱 là ra tù, 刑满出狱 là mãn hạn tù ra trại."),
    ("慎重", "shènzhòng", "thận trọng", "tính từ", "thận trọng", "这件事你要慎重考虑。", "Việc này bạn phải cân nhắc thận trọng.",
     "Tính từ, nghĩa là thận trọng, giống hệt tiếng Việt. Trong bài có cụm 为了慎重起见, để cho thận trọng, ta sẽ học ở phần ngữ pháp."),
    ("麻痹", "mábì", "ma tý", "tính từ", "lơ là, mất cảnh giác", "工作中不能有半点麻痹。", "Trong công việc không được lơ là một chút nào.",
     "Nghĩa gốc là tê liệt, như 小儿麻痹, bệnh bại liệt ở trẻ em. Nhưng trong bài, 麻痹 là tính từ, nghĩa là lơ là, mất cảnh giác. Cụm hay gặp là 麻痹大意, lơ là chủ quan."),
    ("失误", "shīwù", "thất ngộ", "danh từ", "sai sót, sơ suất", "一个小小的失误可能造成大问题。", "Một sơ suất nhỏ có thể gây ra vấn đề lớn.",
     "Danh từ, nghĩa là sai sót, sơ suất, thường do không cẩn thận. Trong thể thao, 失误 là lỗi đánh hỏng."),
    ("考验", "kǎoyàn", "khảo nghiệm", "động từ", "thử thách", "这是一项考验耐心的工作。", "Đây là một công việc thử thách lòng kiên nhẫn.",
     "Động từ, nghĩa là thử thách. Đây là một từ dễ nhầm: tiếng Việt khảo nghiệm thường là thử nghiệm, kiểm tra chất lượng, như khảo nghiệm giống cây trồng. Còn 考验 trong tiếng Trung là thử thách ý chí, lòng kiên nhẫn hay tình cảm của con người, như 经受考验, trải qua thử thách."),
    ("检验", "jiǎnyàn", "kiểm nghiệm", "động từ", "kiểm nghiệm, kiểm tra", "这批产品已经通过了检验。", "Lô sản phẩm này đã qua kiểm nghiệm.",
     "Động từ, nghĩa là kiểm nghiệm, kiểm tra xem có đạt tiêu chuẩn không. Câu nổi tiếng: 实践是检验真理的唯一标准, thực tiễn là tiêu chuẩn duy nhất để kiểm nghiệm chân lý."),
    ("查获", "cháhuò", "tra hoạch", "động từ", "tra bắt, thu giữ", "警方查获了一批毒品。", "Cảnh sát đã thu giữ một lô ma túy.",
     "Động từ, nghĩa là điều tra rồi bắt được người phạm tội, hoặc thu giữ được tang vật. Chữ 获 nghĩa là bắt được, thu được."),
    ("制裁", "zhìcái", "chế tài", "động từ", "trừng trị, trừng phạt", "罪犯得到了应得的制裁。", "Tội phạm đã bị trừng trị thích đáng.",
     "Động từ, nghĩa là trừng trị, trừng phạt, thường bằng pháp luật. 经济制裁 là trừng phạt kinh tế, cấm vận."),
    ("公安局", "gōng'ānjú", "công an cục", "danh từ", "cục công an, sở công an", "他在市公安局工作。", "Anh ấy làm việc ở công an thành phố.",
     "Danh từ, nghĩa là cơ quan công an. 公安 chính là công an, giống hệt tiếng Việt."),
    ("情报", "qíngbào", "tình báo", "danh từ", "tin tức, tin báo; tình báo", "警方接到了一条重要情报。", "Cảnh sát nhận được một tin báo quan trọng.",
     "Danh từ, nghĩa là tin tức, tin báo, đặc biệt là tin mật. Chú ý: tiếng Việt tình báo thường gắn với gián điệp; còn 情报 trong tiếng Trung rộng hơn, mọi tin tức có giá trị đều có thể gọi là 情报, như 科技情报, thông tin khoa học kỹ thuật."),
    ("毒品", "dúpǐn", "độc phẩm", "danh từ", "ma túy", "毒品严重危害人们的健康。", "Ma túy gây hại nghiêm trọng cho sức khỏe con người.",
     "Danh từ, nghĩa là ma túy. Các từ liên quan trong bài: 毒贩 là kẻ buôn ma túy, 缉毒 là truy bắt ma túy, 吸毒 là hút chích ma túy."),
    ("带领", "dàilǐng", "đái lĩnh", "động từ", "dẫn dắt, dẫn đầu", "队长带领队员出发了。", "Đội trưởng dẫn các đội viên xuất phát.",
     "Động từ, nghĩa là dẫn dắt, dẫn đầu một nhóm người làm việc gì đó."),
    ("沉着", "chénzhuó", "trầm trước", "tính từ", "bình tĩnh, điềm tĩnh", "遇到危险时要沉着冷静。", "Khi gặp nguy hiểm phải bình tĩnh.",
     "Tính từ, nghĩa là bình tĩnh, điềm tĩnh. Chú ý âm đọc: chữ thứ hai đọc là zhuó, thanh hai, giống trong từ 着重. Cụm hay gặp là 沉着冷静."),
    ("暂且", "zànqiě", "tạm thả", "phó từ", "tạm thời, tạm", "这个问题我们暂且不谈。", "Vấn đề này chúng ta tạm thời không bàn.",
     "Phó từ, nghĩa là tạm thời, tạm cứ như vậy đã. Đây là điểm ngữ pháp thứ hai của bài."),
    ("部署", "bùshǔ", "bộ thự", "động từ", "bố trí, triển khai (lực lượng)", "警方在附近部署了大量警力。", "Cảnh sát đã triển khai lực lượng lớn ở gần đó.",
     "Động từ, nghĩa là bố trí, triển khai, thường dùng cho việc lớn như lực lượng, nhiệm vụ. 部署兵力 là bố trí binh lực."),
    ("埋伏", "máifú", "mai phục", "động từ", "mai phục", "警察埋伏在附近。", "Cảnh sát mai phục ở gần đó.",
     "Động từ, âm Hán Việt giống hệt tiếng Việt. Chú ý: chữ đầu ở đây đọc là mái, thanh hai."),
    ("布置", "bùzhì", "bố trí", "động từ", "bố trí, sắp đặt", "她把房间布置得很漂亮。", "Cô ấy bài trí căn phòng rất đẹp.",
     "Động từ, vừa là sắp đặt, trang trí đồ đạc, vừa là phân công công việc, như 布置作业, giao bài tập. So với 部署 thì 布置 dùng cho việc nhỏ, đời thường hơn."),
    ("反抗", "fǎnkàng", "phản kháng", "động từ", "phản kháng, chống cự", "歹徒来不及反抗就被抓住了。", "Tên côn đồ chưa kịp chống cự đã bị bắt.",
     "Động từ, nghĩa là phản kháng, chống cự, giống hệt tiếng Việt."),
    ("逮捕", "dàibǔ", "đãi bộ", "động từ", "bắt giữ", "警察依法逮捕了犯罪嫌疑人。", "Cảnh sát đã bắt giữ nghi phạm theo pháp luật.",
     "Động từ, nghĩa là bắt giữ theo pháp luật, sắc thái trang trọng. Chú ý: chữ đầu trong từ này đọc là dài, thanh bốn."),
    ("非法", "fēifǎ", "phi pháp", "tính từ", "phi pháp, trái phép", "非法运输毒品是严重的犯罪。", "Vận chuyển ma túy trái phép là tội nghiêm trọng.",
     "Tính từ, nghĩa là phi pháp, trái phép, giống hệt tiếng Việt. Trái nghĩa là 合法, hợp pháp."),
    ("贩卖", "fànmài", "phán mại", "động từ", "buôn bán (thường là trái phép)", "他们因贩卖毒品被逮捕了。", "Bọn họ bị bắt vì buôn bán ma túy.",
     "Động từ, nghĩa là buôn bán, thường mang sắc thái xấu, đi với hàng cấm: 贩卖毒品, buôn bán ma túy; 贩卖人口, buôn người. Kẻ buôn ma túy gọi là 毒贩."),
    ("平面", "píngmiàn", "bình diện", "danh từ", "mặt phẳng", "两条直线在同一个平面上。", "Hai đường thẳng nằm trên cùng một mặt phẳng.",
     "Danh từ, nghĩa là mặt phẳng. Chú ý: tiếng Việt bình diện thường là phương diện, khía cạnh; còn 平面 là mặt phẳng theo nghĩa đen, như 平面图, bản vẽ mặt bằng."),
    ("平行", "píngxíng", "bình hành", "động từ", "song song", "这两条路是平行的。", "Hai con đường này song song với nhau.",
     "Động từ, nghĩa là song song. 平行线 là đường song song, 平行四边形 là hình bình hành."),
    ("并列", "bìngliè", "tịnh liệt", "động từ", "đứng ngang hàng, sóng đôi", "两个人并列第一名。", "Hai người đồng hạng nhất.",
     "Động từ, nghĩa là đứng cạnh nhau, ngang hàng nhau. Trong bài: 平行而非并列, song song chứ không sóng đôi, nghĩa là người lính và chú chó vốn chẳng liên quan gì đến nhau."),
    ("交叉", "jiāochā", "giao xoa", "động từ", "giao nhau, cắt nhau", "两条公路在这里交叉。", "Hai con đường giao nhau ở đây.",
     "Động từ, nghĩa là giao nhau, cắt nhau. 交叉口 là giao lộ, ngã giao."),
    ("包袱", "bāofu", "bao phục", "danh từ", "gánh nặng (tâm lý); tay nải", "别有思想包袱，大胆去做吧。", "Đừng nặng lòng lo nghĩ, cứ mạnh dạn mà làm.",
     "Nghĩa gốc là tay nải, bọc vải. Nghĩa bóng hay dùng hơn là gánh nặng tâm lý: 心里包袱很重, trong lòng nặng trĩu lo âu; 放下包袱, trút bỏ gánh nặng."),
    ("胆怯", "dǎnqiè", "đảm khiếp", "tính từ", "nhút nhát, sợ sệt", "第一次上台，他有点儿胆怯。", "Lần đầu lên sân khấu, cậu ấy hơi rụt rè.",
     "Tính từ, nghĩa là nhút nhát, sợ sệt. Chữ 胆 là lá mật, tượng trưng cho lòng can đảm; chữ 怯 là sợ. Giống tiếng Việt nhát gan."),
    ("哄", "hǒng", "hống", "động từ", "dỗ, dỗ dành", "妈妈哄了半天，孩子才不哭了。", "Mẹ dỗ mãi, đứa bé mới nín khóc.",
     "Động từ, nghĩa là dỗ dành, dùng lời ngọt ngào để làm ai đó vui hoặc nghe theo. Chú ý âm đọc: với nghĩa dỗ dành thì đọc là hǒng, thanh ba. Chữ này còn có âm khác mang nghĩa ồn ào, nhưng trong bài chỉ có nghĩa dỗ dành."),
    ("信赖", "xìnlài", "tín lại", "động từ", "tin cậy, tin tưởng", "他是一个值得信赖的朋友。", "Anh ấy là một người bạn đáng tin cậy.",
     "Động từ, nghĩa là tin cậy, tin tưởng và dựa vào. 值得信赖 là đáng tin cậy."),
    ("忠诚", "zhōngchéng", "trung thành", "tính từ", "trung thành", "狗是人类最忠诚的朋友。", "Chó là người bạn trung thành nhất của con người.",
     "Tính từ, nghĩa là trung thành, âm Hán Việt giống hệt tiếng Việt."),
    ("舌头", "shétou", "thiệt đầu", "danh từ", "cái lưỡi", "小狗伸出舌头舔了舔我的手。", "Chú chó con thè lưỡi liếm tay tôi.",
     "Danh từ, nghĩa là cái lưỡi. 伸出舌头 là thè lưỡi ra."),
    ("舔", "tiǎn", "thiểm", "động từ", "liếm", "小猫在舔自己的毛。", "Con mèo con đang liếm lông mình.",
     "Động từ, nghĩa là liếm. Trong bài dùng dạng lặp 舔一舔, liếm liếm, diễn tả hành động nhẹ nhàng, thân mật."),
    ("空隙", "kòngxì", "không khích", "danh từ", "khe hở, chỗ trống", "毒品藏在车厢的空隙里。", "Ma túy được giấu trong khe hở của thùng xe.",
     "Danh từ, nghĩa là khe hở, chỗ trống. Chú ý âm đọc: chữ đầu ở đây đọc là kòng, thanh bốn. Ngoài khe hở về không gian, từ này còn chỉ khoảng thời gian rảnh xen giữa, như 利用工作的空隙学习, tranh thủ lúc rảnh trong công việc để học."),
    ("扒", "bā", "bát", "động từ", "bới, vạch, gạt ra", "他扒开草丛，发现了一个鸟窝。", "Anh ấy vạch bụi cỏ ra, phát hiện một tổ chim.",
     "Động từ, nghĩa là bới, vạch, gạt sang một bên, thường đi với chữ 开 thành 扒开. Chú ý: với nghĩa này thì đọc là bā, thanh một."),
    ("垫", "diàn", "điếm", "danh từ", "tấm lót, cái đệm", "椅子上放着一个软垫。", "Trên ghế có đặt một tấm đệm mềm.",
     "Danh từ, nghĩa là tấm lót, cái đệm. 塑料垫 là tấm lót bằng nhựa, 鼠标垫 là bàn di chuột."),
    ("叼", "diāo", "điêu", "động từ", "ngậm, tha (bằng miệng)", "小狗叼着一个球跑了过来。", "Chú chó con ngậm quả bóng chạy tới.",
     "Động từ, nghĩa là ngậm, cắp bằng miệng, như chó ngậm xương, chim tha mồi, hoặc 叼着烟, ngậm điếu thuốc."),
    ("粉末", "fěnmò", "phấn mạt", "danh từ", "bột", "这种药是白色的粉末。", "Loại thuốc này là bột màu trắng.",
     "Danh từ, nghĩa là bột. 粉末状 là dạng bột."),
    ("口腔", "kǒuqiāng", "khẩu xoang", "danh từ", "khoang miệng", "医生正在检查他的口腔。", "Bác sĩ đang khám khoang miệng cho anh ấy.",
     "Danh từ, nghĩa là khoang miệng. 口腔医院 là bệnh viện răng hàm mặt."),
    ("岗位", "gǎngwèi", "cương vị", "danh từ", "vị trí công tác", "他又回到了工作岗位上。", "Anh ấy lại trở về vị trí công tác.",
     "Danh từ, nghĩa là vị trí công tác. Chú ý: tiếng Việt cương vị thường chỉ chức vụ; còn 岗位 là chỗ làm việc, vị trí công việc cụ thể, như 坚守岗位, kiên trì bám trụ vị trí."),
    ("战役", "zhànyì", "chiến dịch", "danh từ", "chiến dịch, trận đánh lớn", "这是一场决定性的战役。", "Đây là một chiến dịch mang tính quyết định.",
     "Danh từ, nghĩa là chiến dịch. Trong bài, 战役 được đặt trong ngoặc kép, chỉ những lần làm nhiệm vụ chống ma túy của chú chó, một cách nói ví von."),
    ("光辉", "guānghuī", "quang huy", "tính từ", "vẻ vang, rực rỡ", "他走完了光辉的一生。", "Ông đã đi hết một cuộc đời vẻ vang.",
     "Tính từ, nghĩa là vẻ vang, rực rỡ. 光辉的一生 là một cuộc đời vẻ vang."),
    ("思念", "sīniàn", "tư niệm", "động từ", "nhớ nhung, tưởng nhớ", "我非常思念远方的家人。", "Tôi rất nhớ gia đình ở phương xa.",
     "Động từ, nghĩa là nhớ nhung, tưởng nhớ, sắc thái văn viết và sâu lắng hơn 想念."),
]
# cách đọc mẫu cho chữ đa âm đứng một mình (đọc trong cụm từ để giọng máy đọc đúng)
WORD_SAY = {"哄": "哄孩子", "扒": "扒开"}

add("bullets", chapter="Từ mới (55 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 37 có 55 từ mới, chia thành 19 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 沉着 (zhuó) · 埋伏 (mái) · 逮捕 (dài) · 哄 (hǒng) · 空隙 (kòng) · 扒 (bā)"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có năm mươi lăm từ, thầy chia thành mười chín nhóm nhỏ, mỗi nhóm hai hoặc ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Bài này có mấy từ có âm đọc đặc biệt, như 沉着，埋伏，逮捕，空隙, thầy sẽ nhắc khi gặp. Ngoài ra còn nhiều từ Hán Việt giống hệt tiếng Việt như 慎重，刑事，埋伏，反抗，忠诚, các bạn sẽ thấy dễ nhớ hơn nhiều. Chúng ta bắt đầu nhé.")])

sizes = [3] * 17 + [2, 2]
assert sum(sizes) == len(V)
g = 0
for gs in sizes:
    group = V[g:g + gs]
    words, say = [], []
    for i, (zh, py, hv, loai, vi, ex, exvi, expl) in enumerate(group):
        n = g + i + 1
        words.append({"zh": zh, "py": py, "hv": hv.upper(), "loai": f"{n}. {loai}", "vi": vi, "ex": ex, "exvi": exvi})
        if zh in WORD_SAY:
            w = WORD_SAY[zh]
            say.append(F(i, f"Từ số {n}, thầy đọc trong cụm {w}。 {w}。 Hán Việt là {hv}.", zr=120))
        else:
            say.append(F(i, f"Từ số {n}: {zh}。 {zh}。 Hán Việt là {hv}.", zr=120))
        say.append(F(i, f"{expl} Ví dụ: {ex}{'' if ex[-1] in '。…？！，' else '，'} {exvi[0].upper() + exvi[1:]}{'' if exvi.endswith('.') else '.'}", zr=130))
    add("vocab", section="Từ mới 生词", title=f"Từ mới ({g + 1}–{g + len(group)} / {len(V)})",
        words=words, say=say)
    g += gs

# ======================= BÀI KHÓA =======================
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung nếu khác: số viết bằng chữ Hán])
P = [
    ("（一）优秀女警官\n女警官李真是公认的“指纹破译专家”。",
     "(1) Nữ cảnh sát xuất sắc. Nữ cảnh sát Lý Chân là chuyên gia giải mã vân tay được mọi người công nhận.",
     ["Bài khóa gồm ba câu chuyện. Câu chuyện thứ nhất kể về một nữ cảnh sát chuyên giám định vân tay. 公认 nghĩa là được mọi người công nhận.",
      "破译 là giải mã, vốn dùng cho mật mã. Ở đây tác giả ví việc đọc ra manh mối từ dấu vân tay giống như giải một bức mật mã."],
     "第一个故事，优秀女警官。女警官李真是公认的指纹破译专家。"),
    ("一次，某酒店一位正在化妆的女士被残忍地杀害在室内，现场没有烟头，没有纸屑，也没有抢劫等犯罪痕迹，侦破工作一时陷入停顿，一位曾在楼道内徘徊的男子有嫌疑，却苦于找不到证据。",
     "Một lần, tại một khách sạn nọ, một người phụ nữ đang trang điểm bị sát hại dã man trong phòng. Hiện trường không có đầu mẩu thuốc lá, không có giấy vụn, cũng không có dấu vết phạm tội nào như cướp của; công tác phá án nhất thời rơi vào bế tắc. Một người đàn ông từng lảng vảng ở hành lang bị tình nghi, nhưng khổ nỗi không tìm được chứng cứ.",
     ["某 nghĩa là nào đó, một… nọ: 某酒店 là một khách sạn nọ. 被残忍地杀害在室内 là câu bị động: bị sát hại dã man trong phòng. 侦破 là điều tra và phá án.",
      "苦于 nghĩa là khổ vì, khổ nỗi: 苦于找不到证据, khổ nỗi không tìm ra chứng cứ. 徘徊 là đi đi lại lại, lảng vảng."]),
    ("经过反复多次的现场勘查，窗台上一枚残缺的指纹成了唯一的线索，李真经过几个昼夜反复细致的比对，最终得出结论，抓住了歹徒。",
     "Sau nhiều lần khám nghiệm hiện trường, một dấu vân tay không trọn vẹn trên bậu cửa sổ trở thành manh mối duy nhất. Lý Chân mất mấy ngày đêm so sánh đối chiếu tỉ mỉ, cuối cùng rút ra kết luận và bắt được hung thủ.",
     ["勘查 là khám nghiệm, khảo sát hiện trường. 枚 là lượng từ cho vật nhỏ, ở đây dùng cho dấu vân tay: 一枚指纹. 残缺 là không đầy đủ, bị khuyết mất một phần.",
      "昼夜 là ngày đêm. 比对 là so sánh đối chiếu. 得出结论 là rút ra kết luận."]),
    ("另一次，某地发生多起入室抢劫案，附近居民恐惧感大增。其中两起案件提取到了犯罪嫌疑人的指纹，一枚是在玻璃上，而且指纹严重变形；另一枚是在铜制的框架上，指纹只残留有指尖部位。",
     "Một lần khác, ở một nơi xảy ra nhiều vụ đột nhập vào nhà cướp của, cư dân quanh đó vô cùng sợ hãi. Trong đó, ở hai vụ án đã lấy được dấu vân tay của nghi phạm: một dấu trên kính, lại bị biến dạng nghiêm trọng; dấu kia trên một khung bằng đồng, chỉ còn sót lại phần đầu ngón tay.",
     ["起 là lượng từ cho vụ án, sự việc: 多起入室抢劫案, nhiều vụ đột nhập cướp của; 两起案件, hai vụ án. 恐惧感大增 là cảm giác sợ hãi tăng mạnh.",
      "提取 là lấy ra, thu thập: 提取指纹, lấy dấu vân tay. Cấu trúc 一枚……另一枚…… nghĩa là một dấu thì…, dấu kia thì…."]),
    ("李真天天盯着指纹看，开始怎么也理不出头绪，两枚指纹都是残缺变形的，可以把两枚指纹结合起来分析吗？",
     "Ngày nào Lý Chân cũng chăm chăm nhìn vào hai dấu vân tay; lúc đầu, dù thế nào cô cũng không tìm ra đầu mối. Cả hai dấu vân tay đều khuyết thiếu và biến dạng, liệu có thể kết hợp chúng lại để phân tích không?",
     ["盯着看 là nhìn chằm chằm. 怎么也理不出头绪 nghĩa là dù thế nào cũng không gỡ ra được đầu mối, giống như cuộn chỉ rối không tìm thấy đầu.",
      "Câu hỏi cuối là suy nghĩ của chính Lý Chân. Tác giả để nhân vật tự hỏi, giúp người đọc đi theo dòng suy luận của cô."]),
    ("经过努力，李真发现因刑事犯罪被关押，一年前刑满放出监狱的王某的指纹与现场指纹具有共同特点，王某作案嫌疑很大。",
     "Sau nhiều nỗ lực, Lý Chân phát hiện dấu vân tay của một người họ Vương, từng bị giam vì phạm tội hình sự và mãn hạn tù ra trại một năm trước, có đặc điểm chung với dấu vân tay ở hiện trường; khả năng Vương là thủ phạm rất lớn.",
     ["Câu này có định ngữ rất dài: 因刑事犯罪被关押，一年前刑满放出监狱的 đều bổ nghĩa cho 王某. Gặp câu dài như vậy, hãy tìm danh từ trung tâm trước.",
      "王某 là một người họ Vương nào đó, cách giấu tên thường gặp trong tin tức. 刑满 là mãn hạn tù. 作案 là gây án."]),
    ("为了慎重起见，她又将其他现场遗留的指尖部位指纹与王某的指纹反复比较，最终认定该系列抢劫案为王某所为。",
     "Để cho thận trọng, cô lại đem những dấu vân tay đầu ngón còn để lại ở các hiện trường khác so sánh nhiều lần với vân tay của Vương, cuối cùng xác định loạt vụ cướp này là do Vương gây ra.",
     ["为了慎重起见 chính là điểm ngữ pháp thứ nhất của bài, nghĩa là để cho thận trọng. 她又将 trong văn viết tương đương với 她又把.",
      "该系列抢劫案 là loạt vụ cướp này; chữ 该 ở đây là đại từ văn viết, nghĩa là này, đó. Cụm 为王某所为 nghĩa là do Vương gây ra, một cấu trúc văn viết rất hay gặp."]),
    ("李真说，指纹认定工作繁重、枯燥，不能有半点麻痹和失误，是一项考验耐心的工作。十余年间，李真全身心投入到痕迹检验和指纹管理工作中，查获了不少犯罪分子，使罪犯得到了应得的制裁。",
     "Lý Chân nói, công việc giám định vân tay vừa nặng nhọc vừa khô khan, không được có một chút lơ là hay sai sót nào, là một công việc thử thách lòng kiên nhẫn. Hơn mười năm qua, Lý Chân dồn hết tâm sức vào công tác giám định dấu vết và quản lý vân tay, đã tra bắt được không ít tội phạm, khiến chúng phải chịu sự trừng trị thích đáng.",
     ["半点 nghĩa là một chút xíu, thường đi với phủ định: 不能有半点麻痹, không được lơ là chút nào. 十余年间 là trong hơn mười năm.",
      "全身心投入 là dốc toàn bộ thể xác và tinh thần vào. 应得的制裁 là sự trừng phạt đáng phải nhận."]),
    ("（二）缉毒警察的故事\n公安局接到情报，有人要在某地进行毒品交易，志强立刻带领手下实地走访调查，很快了解到：几天前，的确有一伙人运来大批毒品。",
     "(2) Câu chuyện của cảnh sát phòng chống ma túy. Công an nhận được tin báo có kẻ sắp giao dịch ma túy tại một nơi nọ. Chí Cường lập tức dẫn thuộc cấp đến tận nơi điều tra, và nhanh chóng nắm được: mấy hôm trước, quả thật có một băng nhóm chở đến một lượng lớn ma túy.",
     ["缉毒 là truy bắt ma túy; chữ đầu của từ này nghĩa là truy bắt, như trong 通缉, truy nã. 手下 là cấp dưới, thuộc hạ. 实地走访 là đến tận nơi thăm hỏi, điều tra.",
      "的确 nghĩa là quả thật. 一伙人 là một bọn người, thường mang nghĩa xấu. 大批 là số lượng lớn."],
     "第二个故事，缉毒警察的故事。公安局接到情报，有人要在某地进行毒品交易，志强立刻带领手下实地走访调查，很快了解到：几天前，的确有一伙人运来大批毒品。"),
    ("因各处防守严密，毒贩把东西藏在了桃花乡附近的大山里，准备参与交易的人也住在附近。志强感到毒贩十分狡猾，为了做到万无一失，他确定了“化装行动、引蛇出洞、主动出击”的破案思路。",
     "Vì các nơi đều canh phòng nghiêm ngặt, bọn buôn ma túy đã giấu hàng trong núi gần xã Đào Hoa, những kẻ chuẩn bị tham gia giao dịch cũng ở gần đó. Chí Cường cảm thấy bọn chúng rất xảo quyệt; để đảm bảo vạn vô nhất thất, anh đã xác định hướng phá án: cải trang hành động, dụ rắn ra khỏi hang, chủ động tấn công.",
     ["因 ở đầu câu là vì, cách nói văn viết của 因为. 毒贩 là kẻ buôn ma túy. 狡猾 là xảo quyệt.",
      "万无一失 là thành ngữ, nghĩa là chắc chắn không có một sơ suất nào, giống vạn vô nhất thất. 化装 ở đây là cải trang, khác với 化妆, trang điểm, ở câu chuyện thứ nhất. 引蛇出洞 là dụ rắn ra khỏi hang, tức là dụ đối phương lộ diện."]),
    ("志强假扮成购买毒品的毒贩，与对方接上了头。对方提出在山里进行交易，志强认为山里地形复杂，提出在山下交易。信息传过去，对方却保持了沉默。",
     "Chí Cường giả làm kẻ buôn ma túy đến mua hàng và bắt được liên lạc với đối phương. Đối phương đề nghị giao dịch trong núi; Chí Cường cho rằng địa hình trong núi phức tạp, nên đề nghị giao dịch dưới chân núi. Tin nhắn gửi đi, đối phương lại im lặng.",
     ["假扮成 là giả làm, đóng giả thành. 接上了头 là bắt được liên lạc, cách nói khẩu ngữ, nhất là giữa những người hoạt động bí mật.",
      "却 nghĩa là lại, biểu thị điều trái với mong đợi: tin gửi đi rồi, đối phương lại im lặng."]),
    ("时间一天天过去，志强心中十分焦急，但他清楚，必须沉着冷静，他决定暂且拖一拖这帮毒贩。他放出风说，自己在外地还有事，没货就算了。听到这话，对方急了，提出要不就在镇子附近交易。",
     "Ngày qua ngày, Chí Cường trong lòng vô cùng sốt ruột, nhưng anh hiểu rõ mình phải bình tĩnh, điềm đạm, nên quyết định tạm thời kéo dài thời gian với bọn buôn ma túy này. Anh tung tin rằng mình còn có việc ở nơi khác, không có hàng thì thôi. Nghe vậy, đối phương cuống lên, đề nghị hay là giao dịch ngay gần thị trấn.",
     ["暂且拖一拖 là tạm thời kéo dài thời gian, đây là điểm ngữ pháp thứ hai, 暂且. 这帮毒贩: 帮 là lượng từ cho một nhóm người, thường mang nghĩa xấu, giống 一伙人.",
      "放出风 là tung tin. 没货就算了 là không có hàng thì thôi. 要不 nghĩa là hay là, dùng để đưa ra đề nghị."]),
    ("大清早，志强和全队民警出发了。到了交货地点，志强开始部署兵力。他让一个同事在车里隐蔽好，一个随他下车，其他同事埋伏在附近。",
     "Sáng sớm tinh mơ, Chí Cường cùng toàn đội cảnh sát xuất phát. Đến điểm giao hàng, Chí Cường bắt đầu bố trí lực lượng. Anh để một đồng đội ẩn nấp kỹ trong xe, một người theo anh xuống xe, những đồng đội khác mai phục ở gần đó.",
     ["大清早 là sáng sớm tinh mơ. 民警 là cảnh sát nhân dân. 部署兵力 là bố trí lực lượng.",
      "Chú ý cách liệt kê: 一个同事在车里，一个随他下车，其他同事埋伏在附近, nghĩa là một người thì…, một người thì…, những người khác thì…."]),
    ("刚刚布置妥当，一辆农用车和一辆摩托车朝自己缓缓驶来。面对毒贩，志强提出先验货后交钱，并告诉毒贩钱就放在车里。",
     "Vừa bố trí xong xuôi, một chiếc xe nông dụng và một chiếc xe máy từ từ chạy về phía họ. Đối mặt với bọn buôn ma túy, Chí Cường đề nghị kiểm hàng trước, trả tiền sau, và nói với chúng rằng tiền để ngay trong xe.",
     ["妥当 là thỏa đáng, xong xuôi. 农用车 là xe nông dụng, ta đã gặp ở phần khởi động. 缓缓驶来 là từ từ chạy tới.",
      "先验货后交钱 là kiểm hàng trước, trả tiền sau, theo mẫu 先……后……. 验货 là kiểm tra hàng."]),
    ("毒贩拿出毒品，奔向车门去取钱，车内民警扑上去，毒贩来不及反抗就被逮捕了。",
     "Tên buôn ma túy lấy hàng ra, lao về phía cửa xe để lấy tiền; cảnh sát trong xe lập tức xông ra, hắn chưa kịp chống cự đã bị bắt giữ.",
     ["奔向 là lao về phía. 扑上去 là xông tới, chồm tới. 来不及反抗就被逮捕了 là chưa kịp chống cự đã bị bắt.",
      "Các bạn để ý: kế hoạch dụ rắn ra khỏi hang của Chí Cường đã thành công đúng như dự tính. Tiền để trong xe chính là mồi nhử."]),
    ("这次，缉毒大队成功破获了当地有史以来最大的一起非法运输贩卖毒品案。",
     "Lần này, đội phòng chống ma túy đã phá thành công vụ án vận chuyển, buôn bán ma túy trái phép lớn nhất từ trước đến nay ở địa phương.",
     ["破获 là phá án và bắt được thủ phạm. 有史以来 là từ khi có lịch sử đến nay, tức là từ trước tới nay.",
      "Chú ý định ngữ dài đứng trước 案: 非法运输贩卖毒品案, vụ án vận chuyển buôn bán ma túy trái phép."]),
    ("（三）特殊的“缉毒警察”\n小罗是个兵，辉杰是只犬，这原本是一个平面上两条平行而非并列的线，却在缉毒战场上交叉，创造出感人的故事。",
     "(3) Một cảnh sát chống ma túy đặc biệt. Tiểu La là một người lính, Huy Kiệt là một con chó. Vốn dĩ đây là hai đường thẳng song song chứ không sóng đôi trên cùng một mặt phẳng, vậy mà lại giao nhau trên chiến trường chống ma túy, tạo nên một câu chuyện cảm động.",
     ["Tác giả mượn hình ảnh hình học: 平面 mặt phẳng, 平行 song song, 交叉 giao nhau, để nói rằng người và chó vốn chẳng liên quan gì, nhưng công việc lại gắn họ với nhau. 而非 nghĩa là chứ không phải, văn viết.",
      "Tiêu đề đặt 缉毒警察 trong ngoặc kép, vì nhân vật chính ở đây là một chú chó nghiệp vụ, không phải người."],
     "第三个故事，特殊的缉毒警察。小罗是个兵，辉杰是只犬，这原本是一个平面上两条平行而非并列的线，却在缉毒战场上交叉，创造出感人的故事。"),
    ("接手缉毒犬辉杰，小罗心里包袱很重。小罗怕狗，小时候被狗狂追的经历让他提起狗就胆怯。和辉杰初次见面，小罗努力和它搞好关系，可任你怎么哄，辉杰就是不理，弄得小罗很着急。",
     "Nhận chú chó nghiệp vụ Huy Kiệt, Tiểu La trong lòng rất nặng nề. Tiểu La sợ chó, trải nghiệm bị chó đuổi điên cuồng hồi nhỏ khiến anh cứ nhắc đến chó là sợ. Lần đầu gặp Huy Kiệt, Tiểu La cố gắng làm thân với nó, nhưng mặc cho anh dỗ thế nào, Huy Kiệt vẫn không thèm để ý, khiến Tiểu La rất sốt ruột.",
     ["接手 là tiếp nhận công việc, ở đây là nhận nuôi và huấn luyện chú chó. 提起狗就胆怯 là cứ nhắc đến chó là sợ.",
      "任你怎么哄，辉杰就是不理 nghĩa là mặc cho bạn dỗ thế nào, Huy Kiệt vẫn cứ không thèm để ý. 任 ở đây là mặc cho, còn 就是 nhấn mạnh thái độ cứng đầu. 弄得 là làm cho, khiến cho."]),
    ("没几天，辉杰生病了，小罗悉心照顾它。辉杰很快就好了，自此它对小罗非常的信赖和忠诚，每次见到小罗就会亲热地伸出舌头舔一舔。",
     "Chẳng được mấy hôm, Huy Kiệt bị ốm, Tiểu La tận tình chăm sóc nó. Huy Kiệt nhanh chóng khỏe lại, từ đó nó vô cùng tin cậy và trung thành với Tiểu La, mỗi lần gặp Tiểu La đều thân mật thè lưỡi ra liếm liếm.",
     ["悉心 là hết lòng, tận tâm. 自此 là từ đó trở đi, văn viết. 舔一舔 là động từ lặp lại, diễn tả hành động nhẹ nhàng, ngắn."]),
    ("训练中，辉杰表现突出，无论毒品藏得多隐秘，辉杰一出手，不出一分钟，肯定能查出来。",
     "Trong huấn luyện, Huy Kiệt thể hiện rất xuất sắc: dù ma túy được giấu kín đến đâu, Huy Kiệt chỉ cần ra tay, không quá một phút, chắc chắn sẽ tìm ra.",
     ["无论毒品藏得多隐秘 nghĩa là dù ma túy được giấu kín đến đâu. 一出手 là vừa ra tay. 不出一分钟 là không quá một phút.",
      "Các bạn để ý: 一出手 và 不出一分钟 cùng có chữ 出, nhưng nghĩa khác nhau: một bên là ra tay, một bên là vượt quá."]),
    ("小罗和辉杰可以正式执行任务了。这天辉杰按小罗的指令对一辆车实施搜嗅，很快就从车厢尾部空隙内查出了毒品。此后，辉杰累立战功。",
     "Tiểu La và Huy Kiệt đã có thể chính thức làm nhiệm vụ. Hôm ấy, Huy Kiệt theo lệnh của Tiểu La đánh hơi lục soát một chiếc xe, rất nhanh đã tìm ra ma túy trong khe hở ở đuôi thùng xe. Từ đó về sau, Huy Kiệt liên tiếp lập chiến công.",
     ["对一辆车实施搜嗅 là tiến hành đánh hơi lục soát một chiếc xe; mẫu 对 cộng đối tượng cộng 实施 cộng động từ là cách nói văn viết. 车厢 là thùng xe.",
      "累立战功 là nhiều lần lập chiến công; chữ đầu đọc là lěi, thanh ba, nghĩa là nhiều lần, liên tiếp, giống trong từ 积累."]),
    ("那是9月的一天，辉杰在一辆车上发现了毒品，它扒开车厢底板上铺着的塑料垫，直接从下面叼出一个装有粉末状毒品的塑料袋，薄薄的塑料袋一咬即破，毒品直接渗入了辉杰的口腔。",
     "Đó là một ngày tháng Chín, Huy Kiệt phát hiện ma túy trên một chiếc xe. Nó bới tấm lót nhựa trải trên sàn thùng xe ra, ngậm thẳng từ bên dưới lên một túi nhựa đựng ma túy dạng bột; chiếc túi nhựa mỏng manh vừa cắn đã rách, ma túy ngấm thẳng vào khoang miệng của Huy Kiệt.",
     ["Ba động từ nối nhau rất sinh động: 扒开, bới ra; 叼出, ngậm ra; 一咬即破, vừa cắn đã rách. 即 nghĩa là liền, ngay, cách nói văn viết.",
      "薄薄的 là mỏng manh; chữ này ở đây đọc là báo, thanh hai. 渗入 là thấm vào, ngấm vào."],
     "那是九月的一天，辉杰在一辆车上发现了毒品，它扒开车厢底板上铺着的塑料垫，直接从下面叼出一个装有粉末状毒品的塑料袋，薄薄的塑料袋一咬即破，毒品直接渗入了辉杰的口腔。"),
    ("辉杰中毒了，它呼吸急促，无法站立，得赶快上医院。路上，辉杰眼看就不行了，小罗来不及多想便给辉杰做起了人工呼吸。",
     "Huy Kiệt bị trúng độc, nó thở gấp, không thể đứng dậy, phải đưa ngay đến bệnh viện. Trên đường đi, Huy Kiệt trông như sắp không qua khỏi, Tiểu La không kịp nghĩ ngợi gì, liền hô hấp nhân tạo cho Huy Kiệt.",
     ["中毒 là trúng độc; chữ đầu đọc là zhòng, thanh bốn. 得赶快上医院 nghĩa là phải nhanh chóng đến bệnh viện; chữ đầu ở đây đọc là děi, nghĩa là phải.",
      "眼看就不行了 là trông thấy sắp không qua khỏi. 来不及多想 là không kịp nghĩ nhiều. 做起了人工呼吸 là bắt đầu hô hấp nhân tạo."]),
    ("14公里路程，小罗一次次把辉杰从死亡线上拉回来。经过抢救，辉杰脱离了生命危险，半个月后它又出现在缉毒岗位上。",
     "Suốt quãng đường mười bốn cây số, Tiểu La hết lần này đến lần khác kéo Huy Kiệt trở về từ lằn ranh sinh tử. Sau khi được cấp cứu, Huy Kiệt thoát khỏi nguy hiểm tính mạng, nửa tháng sau nó lại có mặt ở vị trí chống ma túy.",
     ["一次次 là hết lần này đến lần khác. 从死亡线上拉回来 là kéo về từ ranh giới của cái chết.",
      "抢救 là cấp cứu. 脱离了生命危险 là thoát khỏi nguy hiểm tính mạng. 缉毒岗位 là vị trí công tác chống ma túy."],
     "十四公里路程，小罗一次次把辉杰从死亡线上拉回来。经过抢救，辉杰脱离了生命危险，半个月后它又出现在缉毒岗位上。"),
    ("中毒事件让辉杰的身体每况愈下，几年后，辉杰离世。参加过无数次大大小小“战役”的辉杰走完了它光辉的一生，也给小罗的心中留下了无尽的思念。",
     "Vụ trúng độc khiến sức khỏe của Huy Kiệt ngày càng sa sút, mấy năm sau, Huy Kiệt qua đời. Chú chó đã tham gia vô số chiến dịch lớn nhỏ ấy đã đi hết cuộc đời vẻ vang của mình, và để lại trong lòng Tiểu La nỗi nhớ thương khôn nguôi.",
     ["每况愈下 là thành ngữ, nghĩa là tình hình ngày càng xấu đi. 离世 là qua đời, cách nói trang trọng, nhẹ nhàng.",
      "Câu kết này hô ứng với câu mở đầu của câu chuyện thứ ba. Đây chính là thủ pháp 照应 mà ta sẽ học ở phần kỹ năng viết. Bài khóa được cải biên từ báo 华西都市报, Hoa Tây đô thị báo."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 警察的故事",
    items=["Ba câu chuyện: (1) 优秀女警官 · (2) 缉毒警察的故事 · (3) 特殊的“缉毒警察”",
           "Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 警察的故事, dài một nghìn năm trăm bốn mươi sáu chữ.",
         F(0, "Bài gồm ba câu chuyện: 优秀女警官, nữ cảnh sát xuất sắc; 缉毒警察的故事, câu chuyện của cảnh sát chống ma túy; và 特殊的缉毒警察, một cảnh sát chống ma túy đặc biệt."),
         F(1, "Thầy chia bài thành từng đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(2, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(3, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 100 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi, cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Tóm tắt nội dung", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5)", size=34,
    items=["## 1. 优秀女警察李真的故事",
           "女士被杀案：现场 · 嫌疑人 · 苦于 · 唯一线索 · 经过比对 · 得出结论",
           "入室抢劫案：提取到指纹，一枚……另一枚…… · 把指纹结合起来 · 发现嫌疑人",
           "## 2. 缉毒警察志强的故事",
           "接到情报 → 实地走访 → 确定破案思路 → 假扮毒贩接头 → 等待时机 → 部署兵力 → 抓获毒贩",
           "## 3. 特殊“缉毒警察”辉杰的故事",
           "建立感情：怕狗，哄狗，悉心照顾 · 执行任务：累立战功，中毒，抢救 · 分别：离世，思念"],
    say=["Chúng ta cùng nhìn lại bố cục của cả bài khóa. Bài tập năm trong sách gợi ý đúng bố cục này, với những từ khóa để các bạn kể lại câu chuyện.",
         F(0, "Câu chuyện thứ nhất: 优秀女警察李真的故事, câu chuyện về nữ cảnh sát xuất sắc Lý Chân."),
         F(1, "Vụ án thứ nhất, người phụ nữ bị sát hại. Từ khóa: 现场，嫌疑人，苦于，唯一线索，经过比对，得出结论. Hiện trường không có dấu vết, có người bị tình nghi nhưng không có chứng cứ, manh mối duy nhất là một dấu vân tay, sau khi đối chiếu thì rút ra kết luận."),
         F(2, "Vụ án thứ hai, các vụ đột nhập cướp của. Từ khóa: 提取到指纹，一枚在玻璃上，另一枚在铜制的框架上，把指纹结合起来，发现嫌疑人."),
         F(3, "Câu chuyện thứ hai: 缉毒警察志强的故事, câu chuyện về cảnh sát chống ma túy Chí Cường."),
         F(4, "Diễn biến theo trình tự: 接到情报，实地走访，确定破案思路，假扮毒贩接头，等待时机，部署兵力，抓获毒贩. Nhận tin báo, điều tra tại chỗ, xác định hướng phá án, đóng giả kẻ buôn để bắt liên lạc, chờ thời cơ, bố trí lực lượng, và bắt gọn bọn buôn ma túy."),
         F(5, "Câu chuyện thứ ba: 特殊缉毒警察辉杰的故事, câu chuyện về chú chó nghiệp vụ Huy Kiệt."),
         F(6, "Có ba chặng. Một, xây dựng tình cảm: 怕狗，哄狗，悉心照顾. Hai, làm nhiệm vụ: 累立战功，中毒，抢救. Ba, chia ly: 离世，思念. Bố cục này rất có ích khi các bạn làm bài tập kể lại nội dung bài khóa.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 为……起见", section="Ngữ pháp 注释", title="1. 为……起见 wèi…qǐjiàn – để cho…, vì mục đích…", size=36,
    items=["Biểu thị mục đích: để cho…, vì (lý do)…",
           "Cấu trúc: 为（了）+ động từ / tính từ + 起见，…… – đặt trước chủ ngữ",
           "(1) 为了慎重起见，她又将其他现场遗留的指尖部位指纹与王某的指纹反复比较，最终认定该系列抢劫案为王某所为。",
           "(2) 为安全起见，家庭购买餐具后，可将餐具放在稀释后的食用醋中煮一煮，然后再使用。",
           "(3) ……在说明问题时，为了周到或强调起见，往往也从正反两方面阐述表达。",
           "Hay gặp: 为安全起见 · 为慎重起见 · 为方便起见 · 为保险起见"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là cấu trúc 为了……起见.",
         F(0, "Cấu trúc này biểu thị mục đích, tiếng Việt dịch là: để cho…, hoặc vì lý do…."),
         F(1, "Công thức: 为了, hoặc chỉ cần một chữ đầu của từ này cũng được, cộng một động từ hay tính từ, cộng 起见. Ví dụ 为安全起见, hay 为了安全起见. Cả cụm này đặt ở đầu câu, trước chủ ngữ, sau đó mới đến phần chính của câu. Phần ở giữa thường là những từ hai âm tiết như 安全，慎重，方便."),
         F(2, "Ví dụ một, lấy từ bài khóa: 为了慎重起见，她又将其他现场遗留的指尖部位指纹与王某的指纹反复比较，最终认定该系列抢劫案为王某所为。 Để cho thận trọng, cô lại so sánh nhiều lần vân tay đầu ngón ở các hiện trường khác với vân tay của Vương, cuối cùng xác định loạt vụ cướp này do Vương gây ra."),
         F(3, "Ví dụ hai: 为安全起见，家庭购买餐具后，可将餐具放在稀释后的食用醋中煮一煮，然后再使用。 Để an toàn, sau khi mua bát đĩa về, các gia đình có thể cho chúng vào nước giấm pha loãng đun sôi một lúc rồi hãy dùng. 稀释 là pha loãng."),
         F(4, "Ví dụ ba: 通常人们在思考问题时总是习惯于从正面和反面两个角度进行；在说明问题时，为了周到或强调起见，往往也从正反两方面阐述表达。 Khi suy nghĩ, người ta thường quen nhìn từ cả mặt thuận lẫn mặt nghịch; khi trình bày vấn đề, để cho chu đáo hoặc để nhấn mạnh, người ta cũng thường trình bày từ cả hai mặt."),
         F(5, "Những cụm hay gặp nhất là: 为安全起见，为慎重起见，为方便起见，为保险起见. Các bạn chỉ cần thuộc mấy cụm này là dùng được ngay.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: chọn cụm thích hợp điền vào chỗ trống", reveal=True, size=34,
    items=["## 为了叙述方便起见 · 为了慎重起见 · 为了安全起见",
           "(1) ____，我们把世界造型艺术分为三大块——西方艺术、东方艺术以及中南美洲、非洲、大洋洲艺术。",
           "Đáp án: 为了叙述方便起见",
           "(2) 加拿大人与冰雪有着不解之缘，他们在冬季驾车也有着丰富的经验。但____，他们在大风雪的时候还是尽量不出门或少出门……",
           "Đáp án: 为了安全起见",
           "(3) ……这么多书，卖得出去吗？____，我们主动向这家书店介绍了情况，提请他们全面考虑。",
           "Đáp án: 为了慎重起见"],
    say=[F(0, "Luyện tập: chọn cụm thích hợp điền vào chỗ trống. Có ba cụm: 为了叙述方便起见，为了慎重起见，为了安全起见."),
         F(1, "Câu một: chỗ trống, 我们把世界造型艺术分为三大块——西方艺术、东方艺术以及中南美洲、非洲、大洋洲艺术。 Chỗ trống, chúng tôi chia nghệ thuật tạo hình thế giới thành ba khối lớn: nghệ thuật phương Tây, phương Đông, và Trung Nam Mỹ, châu Phi, châu Đại Dương. Các bạn tạm dừng và thử chọn nhé."),
         F(2, "Đáp án: 为了叙述方便起见。 Để tiện cho việc trình bày. Chia thành ba khối là để kể cho dễ."),
         F(3, "Câu hai: 加拿大人与冰雪有着不解之缘，他们在冬季驾车也有着丰富的经验。但，chỗ trống，他们在大风雪的时候还是尽量不出门或少出门，而且还都非常注意天气预报。 Người Canada gắn bó với băng tuyết, lái xe mùa đông rất có kinh nghiệm. Nhưng, chỗ trống, khi có bão tuyết họ vẫn cố gắng không ra ngoài hoặc ít ra ngoài."),
         F(4, "Đáp án: 为了安全起见。 Để an toàn."),
         F(5, "Câu ba: 接到这么大的订单，我们心中高兴之余也有一分担心：一个地处偏僻山区的县城，这么多书，卖得出去吗？ chỗ trống，我们主动向这家书店介绍了情况，提请他们全面考虑。 Nhận được đơn hàng lớn như vậy, chúng tôi vừa mừng vừa lo: một huyện lỵ ở vùng núi hẻo lánh, nhiều sách như vậy có bán được không? Chỗ trống, chúng tôi chủ động trình bày tình hình với hiệu sách, đề nghị họ cân nhắc kỹ."),
         F(6, "Đáp án: 为了慎重起见。 Để cho thận trọng. Nhớ rằng cụm 为了……起见 luôn đứng ở đầu vế câu, trước phần chính.")])

add("bullets", chapter="Ngữ pháp: 暂且", section="Ngữ pháp 注释", title="2. 暂且 zànqiě – tạm thời, tạm cứ như vậy đã", size=36,
    items=["Phó từ: tạm thời cứ làm như vậy đã (sau này sẽ tính tiếp)",
           "Vị trí: sau chủ ngữ, trước động từ – 暂且 + động từ / 不 + động từ",
           "(1) 干了几天，小王就不想干了。大家没办法，只得暂且由他去。",
           "(2) ……但他清楚，必须沉着冷静，他决定暂且拖一拖这帮毒贩。",
           "(3) 我们暂且不说染烫发对身体的伤害，对头发巨大的影响就足以引起我们的重视了。",
           "Hay gặp: 暂且不论 · 暂且不说 · 暂且不提 · 暂且放一放",
           "So với 暂时: 暂且 chỉ làm trạng ngữ; 暂时 còn làm định ngữ (暂时的困难)"],
    say=["Điểm ngữ pháp thứ hai là phó từ 暂且.",
         F(0, "暂且 nghĩa là tạm thời cứ làm như vậy đã, chuyện sau này sẽ tính tiếp. Tiếng Việt dịch là tạm thời, tạm, hoặc hẵng."),
         F(1, "暂且 đứng sau chủ ngữ, trước động từ. Rất hay gặp dạng 暂且不 cộng động từ, ví dụ 暂且不说, tạm chưa nói đến."),
         F(2, "Ví dụ một: 干了几天，小王就不想干了。大家没办法，只得暂且由他去。 Làm được mấy hôm, cậu Vương đã không muốn làm nữa. Mọi người hết cách, đành tạm mặc kệ cậu ấy. 由他去 là mặc kệ anh ta."),
         F(3, "Ví dụ hai, lấy từ bài khóa: 时间一天天过去，志强心中十分焦急，但他清楚，必须沉着冷静，他决定暂且拖一拖这帮毒贩。 Chí Cường quyết định tạm thời kéo dài thời gian với bọn buôn ma túy."),
         F(4, "Ví dụ ba: 我们暂且不说染烫发对身体的伤害，对头发巨大的影响就足以引起我们的重视了。 Tạm chưa nói đến tác hại của việc nhuộm uốn tóc đối với cơ thể, chỉ riêng ảnh hưởng rất lớn đến mái tóc cũng đủ khiến chúng ta phải coi trọng rồi."),
         F(5, "Những cụm hay gặp: 暂且不论，暂且不说，暂且不提，暂且放一放. Tức là tạm không bàn, tạm chưa nói, tạm không nhắc, tạm gác lại."),
         F(6, "So với 暂时: hai từ nghĩa gần nhau, nhưng 暂且 mang sắc thái văn viết và chỉ đứng trước động từ; còn 暂时 có thể làm định ngữ, như 暂时的困难, khó khăn tạm thời. Ta không nói 暂且的困难.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: chọn vị trí thích hợp cho 暂且", reveal=True, size=34,
    items=["(1) 在A这个名叫《金姑娘》的童话中，B她没有姓名。我们C称她D是穿蓝裙的小姑娘吧。",
           "Đáp án: C – 我们暂且称她是穿蓝裙的小姑娘吧。",
           "(2) 网球场的大门敞开着，场内比赛A进行得正激烈，却没有观众进来。这其中的原因B不论，但C没有观众的决赛，总D给人一种怅然若失的感觉。",
           "Đáp án: B – 这其中的原因暂且不论……",
           "(3) A大家没办法，只得B由他去，等C他心情恢复正常后，再D劝他回来。",
           "Đáp án: B – 只得暂且由他去……"],
    say=[F(0, "Luyện tập: chọn vị trí thích hợp cho 暂且. Câu một: 在这个名叫金姑娘的童话中，她没有姓名。我们称她是穿蓝裙的小姑娘吧。 Trong truyện cổ tích tên là Cô gái vàng, cô bé không có tên. Chúng ta hãy gọi cô là cô bé mặc váy xanh nhé. Có bốn vị trí A, B, C, D. Các bạn tạm dừng và thử chọn nhé."),
         F(1, "Đáp án: C. 我们暂且称她是穿蓝裙的小姑娘吧。 Chúng ta tạm gọi cô là cô bé mặc váy xanh. Vì không có tên thật, nên chỉ là cách gọi tạm."),
         F(2, "Câu hai: 网球场的大门敞开着，场内比赛进行得正激烈，却没有观众进来。这其中的原因不论，但没有观众的决赛，总给人一种怅然若失的感觉。 Cổng sân quần vợt mở toang, trận đấu bên trong đang gay cấn, nhưng không có khán giả nào vào. Nguyên nhân thì không bàn, nhưng một trận chung kết không có khán giả luôn khiến người ta thấy hụt hẫng."),
         F(3, "Đáp án: B. 这其中的原因暂且不论。 Nguyên nhân trong đó tạm không bàn đến. Đây chính là cụm 暂且不论 mà ta vừa học."),
         F(4, "Câu ba: 大家没办法，只得由他去，等他心情恢复正常后，再劝他回来。 Mọi người hết cách, đành mặc kệ anh ấy, đợi khi tâm trạng anh ấy bình thường lại, rồi mới khuyên anh quay về."),
         F(5, "Đáp án: B. 只得暂且由他去。 Đành tạm mặc kệ anh ấy. Chữ 再 ở vế sau cho thấy việc mặc kệ chỉ là tạm thời.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 恐惧 – 恐怖", section="Phân biệt từ 词语辨析", title="Phân biệt 恐惧 và 恐怖",
    common="Giống nhau: đều có nghĩa sợ hãi, nhưng thường không thay nhau được. Ví dụ: 昨天的经历让我感到恐惧。/ 昨天的经历太恐怖了。",
    cols=[{"head": "恐惧",
           "lines": ["(1) Tâm lý hoảng sợ của con người → chủ ngữ là người",
                     "Đúng: 遇到这样的事情，他恐惧极了。",
                     "Sai: 这件事情太恐惧了。",
                     "(2) Hay gặp: 感到恐惧 · 内心的恐惧 · 恐惧感 · 克服恐惧"]},
          {"head": "恐怖",
           "lines": ["(1) Sự việc, cảnh tượng, thủ đoạn gây sợ → không nói về người",
                     "Sai: 遇到这样的事情，他恐怖极了。",
                     "Đúng: 那血腥的场面太恐怖了。",
                     "(2) Hay gặp: 恐怖电影 · 恐怖分子 · 恐怖袭击 · 气氛恐怖"]}],
    say=["Tiếp theo là phần phân biệt từ: 恐惧 và 恐怖. Hai từ này đều có chữ 恐, đều liên quan đến sợ hãi, nên rất dễ nhầm.",
         "Điểm giống nhau: cả hai đều có nghĩa sợ hãi, đáng sợ, nhưng thường không thay thế cho nhau được. Ví dụ: 昨天的经历让我感到恐惧。 Trải nghiệm hôm qua khiến tôi thấy sợ hãi. Và: 昨天的经历太恐怖了。 Trải nghiệm hôm qua thật đáng sợ.",
         F(0, "恐惧 nhấn mạnh tâm lý hoảng sợ bên trong con người, vì vậy chủ ngữ thường là người. Ví dụ đúng: 遇到这样的事情，他恐惧极了。 Gặp chuyện như vậy, anh ấy vô cùng sợ hãi."),
         F(0, "Còn câu 这件事情太恐惧了 là sai, vì sự việc không thể tự cảm thấy sợ. Những cụm hay gặp với 恐惧: 感到恐惧，内心的恐惧，恐惧感，克服恐惧, tức là cảm thấy sợ hãi, nỗi sợ trong lòng, cảm giác sợ hãi, vượt qua nỗi sợ."),
         F(1, "恐怖 thì nhấn mạnh sự việc, cảnh tượng, thủ đoạn khiến người ta sợ, tức là đáng sợ, kinh hoàng. Vì vậy thường không dùng để nói về người. Câu 遇到这样的事情，他恐怖极了 là sai."),
         F(1, "Câu đúng: 那血腥的场面太恐怖了。 Cảnh tượng đẫm máu ấy thật kinh hoàng. Những cụm hay gặp: 恐怖电影，恐怖分子，恐怖袭击，气氛恐怖, tức là phim kinh dị, phần tử khủng bố, tấn công khủng bố, bầu không khí rùng rợn."),
         "Mẹo nhớ: 恐惧 là nỗi sợ ở trong lòng người, giống tiếng Việt sợ hãi; còn 恐怖 là cái đáng sợ ở bên ngoài, giống tiếng Việt kinh hoàng, khủng khiếp. Người cảm thấy 恐惧 vì sự việc 恐怖."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: Đúng hay sai?", reveal=True, size=38,
    items=["(1) 使用这么恐惧残忍的手段太不应该了。",
           "Đáp án: Sai – thủ đoạn đáng sợ phải dùng 恐怖. Sửa: 使用这么恐怖残忍的手段太不应该了。",
           "(2) 他无法克服内心的恐惧，于是拼命呼救。",
           "Đáp án: Đúng – nói về nỗi sợ trong lòng người.",
           "(3) 这个电影太恐怖了，害得我一晚都没敢睡觉。",
           "Đáp án: Đúng – bộ phim là sự vật khiến người ta sợ.",
           "(4) 看到他反常怪异的样子，我很恐怖。",
           "Đáp án: Sai – chủ ngữ là người. Sửa: ……我很恐惧。"],
    say=[F(0, "Bây giờ chúng ta làm thử. Câu một: 使用这么恐惧残忍的手段太不应该了。 Dùng thủ đoạn tàn nhẫn như vậy thật không nên. Đúng hay sai? Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: sai. Thủ đoạn là thứ khiến người ta sợ, nên phải dùng 恐怖: 使用这么恐怖残忍的手段太不应该了。"),
         F(2, "Câu hai: 他无法克服内心的恐惧，于是拼命呼救。 Anh ấy không vượt qua được nỗi sợ trong lòng, liền ra sức kêu cứu."),
         F(3, "Đáp án: đúng. 内心的恐惧 là nỗi sợ trong lòng người, dùng 恐惧 là chuẩn."),
         F(4, "Câu ba: 这个电影太恐怖了，害得我一晚都没敢睡觉。 Bộ phim này đáng sợ quá, làm tôi cả đêm không dám ngủ."),
         F(5, "Đáp án: đúng. Bộ phim là sự vật gây sợ hãi, nên dùng 恐怖."),
         F(6, "Câu bốn: 看到他反常怪异的样子，我很恐怖。 Nhìn thấy dáng vẻ bất thường, kỳ quái của anh ta, tôi rất sợ."),
         F(7, "Đáp án: sai. Chủ ngữ là tôi, đang nói về cảm giác của người, nên phải sửa thành 我很恐惧.")])

# ======================= KỸ NĂNG VIẾT =======================
add("bullets", chapter="Kỹ năng viết: 照应", section="Tu từ 篇章修辞", title="Hô ứng trước sau (照应)", size=38,
    items=["Nội dung trước và sau của bài văn có liên hệ, hô ứng với nhau",
           "Người, việc, vật nêu ở phía trước → xuất hiện lại ở phía sau",
           "Tình tiết ở phía sau → đã có chi tiết dẫn dắt (铺垫) từ phía trước",
           "Tác dụng: kết cấu chặt chẽ · chủ đề rõ ràng · gợi suy nghĩ và dư vị cho người đọc",
           "## Ba kiểu thường gặp",
           "(1) Nhan đề – nội dung · (2) Mở đầu – kết thúc · (3) Một hình ảnh lặp lại xuyên suốt"],
    say=["Phần cuối cùng về lý thuyết là kỹ năng viết: hô ứng trước sau, tiếng Trung gọi là 照应.",
         F(0, "照应 là việc nội dung phía trước và phía sau của bài văn có liên hệ, hô ứng với nhau."),
         F(1, "Cụ thể là: người, sự việc, đồ vật đã nêu ở phía trước thì xuất hiện lại ở phía sau."),
         F(2, "Và ngược lại, tình tiết ở phía sau thì đã được chuẩn bị, dẫn dắt từ phía trước. Sự chuẩn bị đó tiếng Trung gọi là 铺垫."),
         F(3, "Một bài văn có sự hô ứng chu đáo, tỉ mỉ thì kết cấu chặt chẽ hơn, chủ đề nổi bật hơn, và gợi cho người đọc suy nghĩ, dư vị nhiều hơn."),
         F(4, "Có ba kiểu hô ứng thường gặp."),
         F(5, "Một, nhan đề hô ứng với nội dung. Hai, phần mở đầu hô ứng với phần kết thúc. Ba, một hình ảnh được lặp đi lặp lại xuyên suốt bài văn. Chúng ta cùng xem ví dụ cho từng kiểu.")])

add("bullets", section="Tu từ 篇章修辞", title="Ví dụ (1) và (2): nhan đề – nội dung, mở đầu – kết thúc", size=34,
    items=["(1) 我这永久的悔就是：不该离开故乡，离开母亲。",
           "→ Đoạn đầu bài tản văn 《永久的悔》: vào đề ngay, nhan đề và nội dung khớp chặt",
           "(2) Mở đầu: 小罗是个兵，辉杰是只犬，这原本是一个平面上两条平行而非并列的线，却在缉毒战场上交叉，创造出感人的故事。",
           "Kết thúc: 中毒事件让辉杰的身体每况愈下，几年后，辉杰离世。参加过无数次大大小小“战役”的辉杰走完了它光辉的一生，也给小罗的心中留下了无尽的思念。",
           "→ Đầu cuối hô ứng: bài trọn vẹn, khái quát toàn văn, làm rõ chủ đề"],
    say=[F(0, "Ví dụ một: 我这永久的悔就是：不该离开故乡，离开母亲。 Nỗi ân hận mãi mãi của tôi chính là: lẽ ra không nên rời quê hương, rời xa mẹ."),
         F(1, "Đây là đoạn mở đầu của bài tản văn 永久的悔, Nỗi ân hận mãi mãi. Ngay câu đầu tiên tác giả đã bám sát chủ đề, làm cho nhan đề và nội dung hô ứng chặt chẽ."),
         F(2, "Ví dụ hai lấy ngay từ bài khóa. Mở đầu câu chuyện thứ ba: 小罗是个兵，辉杰是只犬，这原本是一个平面上两条平行而非并列的线，却在缉毒战场上交叉，创造出感人的故事。"),
         F(3, "Kết thúc: 中毒事件让辉杰的身体每况愈下，几年后，辉杰离世。参加过无数次大大小小战役的辉杰走完了它光辉的一生，也给小罗的心中留下了无尽的思念。"),
         F(4, "Mở đầu nói về hai con đường giao nhau và hứa hẹn một câu chuyện cảm động; kết thúc khép lại bằng sự ra đi của Huy Kiệt và nỗi nhớ của Tiểu La. Đầu cuối hô ứng như vậy vừa làm bài văn trọn vẹn, vừa khái quát toàn bài, lại làm nổi bật chủ đề.")])

add("bullets", section="Tu từ 篇章修辞", title="Ví dụ (3): một hình ảnh lặp lại xuyên suốt", size=36,
    items=["我与父亲不相见已二年余了，我最不能忘记的是他的背影。",
           "……这时我看见他的背影，我的泪很快地流下来了……",
           "……在晶莹的泪光中，又看见那肥胖的，青布棉袍，黑布马褂的背影。",
           "→ Bài 《背影》 (Chu Tự Thanh): hình ảnh 背影 lặp lại nhiều lần",
           "→ Được nhấn mạnh qua sự lặp lại · khắc họa nhân vật · nổi bật chủ đề · làm mạch văn"],
    say=[F(0, "Ví dụ ba là bài tản văn nổi tiếng 背影, Bóng lưng, của nhà văn Chu Tự Thanh. Câu mở đầu: 我与父亲不相见已二年余了，我最不能忘记的是他的背影。 Tôi và cha không gặp nhau đã hơn hai năm, điều tôi không thể nào quên là bóng lưng của cha."),
         F(1, "Ở giữa bài: 这时我看见他的背影，我的泪很快地流下来了。 Lúc ấy tôi nhìn thấy bóng lưng cha, nước mắt tôi tuôn rơi."),
         F(2, "Và ở cuối bài: 在晶莹的泪光中，又看见那肥胖的，青布棉袍，黑布马褂的背影。 Trong làn nước mắt long lanh, tôi lại thấy bóng lưng mập mạp, mặc áo bông vải xanh, áo khoác ngắn vải đen ấy."),
         F(3, "Hình ảnh 背影 được tác giả cố ý cho xuất hiện nhiều lần, từ đầu đến cuối bài."),
         F(4, "Nhờ lặp lại, hình ảnh ấy được nhấn mạnh, khắc họa nhân vật người cha rõ nét hơn, làm nổi bật chủ đề tình cha con, và trở thành mạch văn xuyên suốt bài.")])

add("bullets", section="Tu từ 篇章修辞", title="Luyện tập: đoạn văn sau có dùng 照应 không?", reveal=True, size=36,
    items=["Mở đầu: 自从我家养了猫以后，我就觉得猫活得比人好，要是能做一只猫该有多好啊！",
           "Thân bài: 猫的好处（想干什么就干什么，不用为生活担心……）→ 猫的缺点（只能活十几年，生了病也不会说，不能学知识……）",
           "Kết thúc: 想想看，我现在还是当人好了。",
           "Đáp án: Có. Mở đầu ước được làm mèo → kết thúc quay lại chính ý đó: thôi, vẫn làm người thì hơn. Đầu cuối hô ứng, bài văn trọn vẹn."],
    say=[F(0, "Luyện tập: đoạn văn sau có dùng cách hô ứng không? Câu mở đầu: 自从我家养了猫以后，我就觉得猫活得比人好，要是能做一只猫该有多好啊！ Từ khi nhà tôi nuôi mèo, tôi thấy mèo sống sướng hơn người, giá mà được làm một con mèo thì hay biết mấy!"),
         F(1, "Thân bài kể những cái sướng của mèo: muốn làm gì thì làm, không phải lo chuyện sinh sống, ngủ muộn dậy muộn cũng không ai quản. Rồi kể những cái dở: mèo chỉ sống được mười mấy năm, ốm cũng không nói được, không được học hành, không có lý tưởng."),
         F(2, "Câu kết: 想想看，我现在还是当人好了。 Nghĩ lại thì, bây giờ tôi vẫn nên làm người thì hơn. Các bạn tạm dừng và suy nghĩ nhé."),
         F(3, "Đáp án: có. Mở đầu nêu mong ước được làm mèo, kết thúc quay lại đúng ý đó và đưa ra kết luận ngược lại: vẫn làm người thì hơn. Mở đầu và kết thúc hô ứng với nhau, làm cho bài văn chặt chẽ, trọn vẹn và rất dí dỏm.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ có dấu chấm", size=40,
    items=["嫌疑 (疑) → 可疑 · 怀疑 · 疑问 · 疑惑",
           "残留 (留) → 停留 · 保留 · 遗留 · 留言 · 留恋",
           "失误 (误) → 错误 · 耽误 · 误会 · 误解 · 延误",
           "查获 (获) → 获得 · 收获 · 获奖 · 捕获 · 荣获",
           "非法 (非) → 非常 · 非凡 · 是非 · 无非 · 并非"],
    say=["Phần luyện tập. Bài tập một: mô phỏng ví dụ, viết thêm các từ có chứa chữ được đánh dấu chấm ở bên dưới.",
         F(0, "Ví dụ mẫu: 嫌疑, chữ được đánh dấu là chữ thứ hai, 疑. Ta có 可疑，怀疑，疑问，疑惑, tức là khả nghi, nghi ngờ, nghi vấn, và nghi hoặc."),
         F(1, "残留, chữ được đánh dấu là 留, lưu. Ta có 停留，保留，遗留，留言，留恋, tức là dừng lại, bảo lưu, để lại, để lại lời nhắn, và lưu luyến."),
         F(2, "失误, chữ được đánh dấu là 误, ngộ, nghĩa là sai, lỡ. Ta có 错误，耽误，误会，误解，延误, tức là sai lầm, làm lỡ việc, hiểu lầm, hiểu sai, và trì hoãn."),
         F(3, "查获, chữ được đánh dấu là 获, hoạch, nghĩa là thu được. Ta có 获得，收获，获奖，捕获，荣获, tức là giành được, thu hoạch, đoạt giải, bắt được, và vinh dự giành được."),
         F(4, "非法, lần này chữ được đánh dấu là chữ đầu, 非, phi. Ta có 非常，非凡，是非，无非，并非, tức là vô cùng, phi thường, phải trái, chẳng qua là, và hoàn toàn không phải.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (1)", reveal=True, size=38,
    items=["(1) 他稍微停了一下，又继续发表演讲。（停顿）",
           "Đáp án: 他稍微停顿了一下，又继续发表演讲。",
           "(2) 为了更保险，你还是把钱存在银行里吧。（为……起见）",
           "Đáp án: 为安全起见，你还是把钱存在银行里吧。",
           "(3) 如此重大的事件，一定要谨慎处理。（慎重）",
           "Đáp án: 如此重大的事件，一定要慎重处理。"],
    say=[F(0, "Bài tập hai: dùng từ cho sẵn để viết lại câu. Câu một, dùng 停顿: 他稍微停了一下，又继续发表演讲。 Anh ấy dừng lại một chút, rồi tiếp tục bài diễn thuyết. Các bạn tạm dừng và thử viết nhé."),
         F(1, "Đáp án: 他稍微停顿了一下，又继续发表演讲。 Thay 停 bằng 停顿, câu văn trang trọng hơn."),
         F(2, "Câu hai, dùng 为了……起见: 为了更保险，你还是把钱存在银行里吧。 Cho chắc ăn hơn, bạn nên gửi tiền vào ngân hàng."),
         F(3, "Đáp án: 为安全起见，你还是把钱存在银行里吧。 Hoặc có thể nói 为保险起见. Cả cụm vẫn đặt ở đầu câu."),
         F(4, "Câu ba, dùng 慎重: 如此重大的事件，一定要谨慎处理。 Sự việc hệ trọng như vậy nhất định phải xử lý cẩn trọng."),
         F(5, "Đáp án: 如此重大的事件，一定要慎重处理。 谨慎 thiên về cẩn thận trong lời nói, hành động; còn với việc hệ trọng cần cân nhắc kỹ, 慎重 là từ thích hợp nhất.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (2)", reveal=True, size=38,
    items=["(4) 导游带着游客一边游览名胜古迹，一边体验当地民俗。（带领）",
           "Đáp án: 导游带领游客一边游览名胜古迹，一边体验当地民俗。",
           "(5) 我们先把这个问题放一放，等时机成熟了再讨论吧。（暂且）",
           "Đáp án: 我们暂且把这个问题放一放，等时机成熟了再讨论吧。",
           "(6) 快住手，你这么做是违反法律规定的。（非法）",
           "Đáp án: 快住手，你这么做是非法的。"],
    say=[F(0, "Câu bốn, dùng 带领: 导游带着游客一边游览名胜古迹，一边体验当地民俗。 Hướng dẫn viên dẫn du khách vừa tham quan danh lam thắng cảnh, vừa trải nghiệm phong tục địa phương."),
         F(1, "Đáp án: 导游带领游客一边游览名胜古迹，一边体验当地民俗。 Thay 带着 bằng 带领."),
         F(2, "Câu năm, dùng 暂且: 我们先把这个问题放一放，等时机成熟了再讨论吧。 Chúng ta hãy gác vấn đề này lại, đợi thời cơ chín muồi rồi thảo luận."),
         F(3, "Đáp án: 我们暂且把这个问题放一放，等时机成熟了再讨论吧。 暂且 đứng sau chủ ngữ, trước cụm 把 cộng tân ngữ."),
         F(4, "Câu sáu, dùng 非法: 快住手，你这么做是违反法律规定的。 Dừng tay ngay, bạn làm vậy là vi phạm quy định pháp luật."),
         F(5, "Đáp án: 快住手，你这么做是非法的。 Một từ 非法 thay được cả cụm 违反法律规定, câu ngắn gọn hơn hẳn.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ điền vào chỗ trống (1)", reveal=True, size=36,
    items=["## Từ cho sẵn: 沉着 · 埋伏 · 麻痹 · 情报 · 考验",
           "作为警察，在工作中不能有半点___和失误，接到___后，必须冷静___，仔细考虑，部署兵力。有时在一个地方可能要___好几天才能抓到罪犯，所以这也是一项___耐力的工作。",
           "Đáp án: 麻痹 · 情报 · 沉着 · 埋伏 · 考验"],
    say=[F(0, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn một có năm từ: 沉着，埋伏，麻痹，情报，考验."),
         F(1, "作为警察，在工作中不能有半点, chỗ trống, 和失误，接到, chỗ trống, 后，必须冷静, chỗ trống, 仔细考虑，部署兵力。有时在一个地方可能要, chỗ trống, 好几天才能抓到罪犯，所以这也是一项, chỗ trống, 耐力的工作。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 作为警察，在工作中不能有半点麻痹和失误，接到情报后，必须冷静沉着，仔细考虑，部署兵力。有时在一个地方可能要埋伏好几天才能抓到罪犯，所以这也是一项考验耐力的工作。 Làm cảnh sát, trong công việc không được có chút lơ là hay sai sót nào; nhận được tin báo phải bình tĩnh, điềm đạm, suy nghĩ kỹ rồi bố trí lực lượng. Có khi phải mai phục ở một chỗ mấy ngày mới bắt được tội phạm, nên đây cũng là công việc thử thách sức bền.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ điền vào chỗ trống (2)", reveal=True, size=36,
    items=["## Từ cho sẵn: 痕迹 · 嫌疑 · 线索 · 歹徒 · 停顿",
           "近期，小区内连续发生了几起入室盗窃案件。犯罪分子非常狡猾，地上没有脚印，家具上也没有留下___，虽然发现几个年轻人有___，但找不到证据，侦破工作陷入___状态，好在最终有一个目击者提供了重要___，才成功抓获了___。",
           "Đáp án: 痕迹 · 嫌疑 · 停顿 · 线索 · 歹徒"],
    say=[F(0, "Đoạn hai có năm từ: 痕迹，嫌疑，线索，歹徒，停顿."),
         F(1, "近期，小区内连续发生了几起入室盗窃案件。犯罪分子非常狡猾，地上没有脚印，家具上也没有留下, chỗ trống, 虽然发现几个年轻人有, chỗ trống, 但找不到证据，侦破工作陷入, chỗ trống, 状态，好在最终有一个目击者提供了重要, chỗ trống, 才成功抓获了, chỗ trống。"),
         F(2, "Đáp án: 家具上也没有留下痕迹，虽然发现几个年轻人有嫌疑，但找不到证据，侦破工作陷入停顿状态，好在最终有一个目击者提供了重要线索，才成功抓获了歹徒。 Gần đây trong khu dân cư liên tiếp xảy ra mấy vụ trộm đột nhập. Bọn tội phạm rất xảo quyệt, không để lại dấu vết; dù phát hiện vài thanh niên bị tình nghi nhưng không có chứng cứ, việc phá án rơi vào bế tắc. May mà cuối cùng có một nhân chứng cung cấp manh mối quan trọng, mới bắt được bọn gian. 目击者 là nhân chứng, người chứng kiến.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 4: Đoạn văn sau dùng 照应 như thế nào?", reveal=True, size=34,
    items=["探望远在异乡工作的叔叔之前，接到叔叔的微信，要我为他带几颗生枣核，而且是再三托付，这是为什么呢？我感到很蹊跷。",
           "……他小心翼翼地托在掌心……“等会儿你就明白啦。”……介绍他的住房……就是不提“枣核”。",
           "临别时，他感慨地说：“近来，我老是想老家院里那颗枣树。所以托你带几颗种子，试种一下。”",
           "Đáp án: Mở đầu nêu chi tiết lạ (mang hạt táo) làm 铺垫, gây tò mò → giữa bài nhắc lại 枣核 nhiều lần, càng thêm bí ẩn → kết thúc giải đáp: chú nhớ cây táo quê nhà. Trước có dẫn dắt, sau có hô ứng."],
    say=[F(0, "Bài tập bốn: hãy chỉ ra đoạn văn sau dùng cách hô ứng như thế nào. Mở đầu: 探望远在异乡工作的叔叔之前，接到叔叔的微信，要我为他带几颗生枣核，而且是再三托付，这是为什么呢？我感到很蹊跷。 Trước khi đi thăm người chú làm việc ở nơi xa, tôi nhận được tin nhắn của chú, nhờ mang cho chú mấy hạt táo sống, lại còn dặn đi dặn lại. Vì sao vậy? Tôi thấy rất lạ. 枣核 là hạt táo, 蹊跷 là kỳ lạ, khó hiểu."),
         F(1, "Ở giữa: vừa xuống xe chú đã hỏi hạt táo mang đến chưa, rồi nâng niu đặt trên lòng bàn tay như vật quý. Tôi hỏi để làm gì, chú chỉ nói: 等会儿你就明白啦。 Lát nữa cháu sẽ hiểu. Về đến nhà, chú giới thiệu nhà cửa, gia đình, vườn tược, mà tuyệt nhiên không nhắc đến hạt táo, khiến tôi càng tò mò."),
         F(2, "Kết thúc: 临别时，他感慨地说：近来，我老是想老家院里那颗枣树。所以托你带几颗种子，试种一下。 Lúc chia tay, chú bùi ngùi nói: dạo này chú cứ nhớ cây táo trong sân nhà ở quê, nên nhờ cháu mang mấy hạt giống để trồng thử. Các bạn tạm dừng và thử phân tích nhé."),
         F(3, "Đáp án: mở đầu đưa ra một chi tiết lạ, mang hạt táo, làm 铺垫, gây tò mò cho người đọc. Giữa bài, hạt táo được nhắc lại nhiều lần mà vẫn chưa có lời giải, càng thêm bí ẩn. Kết thúc mới giải đáp: người chú nhớ cây táo ở quê nhà, tức là nỗi nhớ quê hương. Trước có dẫn dắt, sau có hô ứng, chủ đề nổi bật hẳn lên.")])

add("bullets", section="Luyện tập 练习", title="Vận dụng 运用: Viết một câu chuyện về cảnh sát", size=36,
    items=["Đề bài: lấy 警察故事 làm đầu đề, viết câu chuyện cảnh sát mà bạn biết, ít nhất 400 chữ",
           "Gợi ý bố cục: hoàn cảnh → diễn biến (khó khăn, cách giải quyết) → kết quả → cảm nghĩ",
           "Dùng từ mới: 线索 · 嫌疑 · 慎重 · 沉着 · 部署 · 埋伏 · 逮捕 · 考验",
           "Dùng ngữ pháp: 为了……起见 · 暂且",
           "Dùng 照应: câu mở đầu và câu kết thúc hô ứng với nhau"],
    say=[F(0, "Phần vận dụng của sách: 本课给我们讲了三个警察的故事。在你的印象中，有没有特别感动你的警察故事？请以警察故事为题写一写你所知道的警察故事，字数不少于四百字。 Bài học kể cho chúng ta ba câu chuyện về cảnh sát. Trong ấn tượng của bạn, có câu chuyện cảnh sát nào khiến bạn đặc biệt xúc động không? Hãy lấy 警察故事 làm đầu đề, viết một câu chuyện mà bạn biết, ít nhất bốn trăm chữ."),
         F(1, "Thầy gợi ý bố cục: mở đầu giới thiệu hoàn cảnh, nhân vật; tiếp theo là diễn biến, gặp khó khăn gì và giải quyết thế nào; sau đó là kết quả; cuối cùng là cảm nghĩ của bạn."),
         F(2, "Hãy cố gắng dùng các từ mới như 线索，嫌疑，慎重，沉着，部署，埋伏，逮捕，考验."),
         F(3, "Và dùng hai điểm ngữ pháp vừa học: 为了……起见, và 暂且."),
         F(4, "Quan trọng nhất là áp dụng kỹ năng 照应: câu mở đầu và câu kết thúc nên hô ứng với nhau, giống như câu chuyện về Huy Kiệt trong bài khóa.")])

add("bullets", section="Luyện tập 练习", title="Mở rộng 扩展 (1): nghĩa của từng chữ (语素义)", size=34,
    items=["事迹: 事 – sự việc · 迹 – dấu vết để lại → sự tích, việc làm đáng ghi nhớ",
           "通讯: 通 – nối liền, qua lại · 讯 – tin tức → thông tin liên lạc; bài phóng sự",
           "物资: 物 – đồ vật · 资 – tiền của, tài sản → vật tư",
           "迹象: 迹 – dấu vết sự vật để lại · 象 – hình dạng → dấu hiệu",
           "事态: 事 – sự việc · 态 – tình hình, dáng vẻ → tình hình sự việc (thường là xấu)",
           "推理: 推 – từ sự thật đã biết suy đoán điều khác · 理 – đạo lý → suy luận",
           "转折: 转 – đổi hướng, vị trí, tình thế · 折 – đổi sang hướng ngược lại → bước ngoặt"],
    say=["Phần mở rộng của sách: làm quen với nghĩa của từng chữ trong từ. Nắm được nghĩa từng chữ thì nhớ từ rất nhanh. Các từ trong phần này đều liên quan đến chủ đề cảnh sát và tin tức.",
         F(0, "事迹: chữ đầu là sự việc, chữ sau là dấu vết để lại. Ghép lại là sự tích, những việc làm đáng ghi nhớ, như 英雄事迹, sự tích anh hùng."),
         F(1, "通讯: chữ đầu là nối liền, qua lại; chữ sau là tin tức. Ghép lại là thông tin liên lạc; ngoài ra còn chỉ thể loại bài phóng sự trên báo."),
         F(2, "物资: chữ đầu là đồ vật, chữ sau là tiền của. Ghép lại là vật tư, như 救灾物资, hàng cứu trợ."),
         F(3, "迹象: chữ đầu là dấu vết sự vật để lại, chữ sau là hình dạng. Ghép lại là dấu hiệu, như 没有任何迹象, không có dấu hiệu nào."),
         F(4, "事态: chữ đầu là sự việc, chữ sau là tình hình, dáng vẻ. Ghép lại là tình hình sự việc, thường nói về chuyện xấu, như 事态严重, tình hình nghiêm trọng."),
         F(5, "推理: chữ đầu là từ những sự thật đã biết mà suy đoán điều khác, chữ sau là đạo lý. Ghép lại là suy luận, như 推理小说, tiểu thuyết trinh thám."),
         F(6, "转折: chữ đầu là thay đổi phương hướng, vị trí, tình thế; chữ sau là đổi sang hướng ngược lại. Ghép lại là bước ngoặt, như 人生的转折点, bước ngoặt của cuộc đời.")])

add("bullets", section="Luyện tập 练习", title="Mở rộng 扩展 (2): nghĩa của từng chữ (语素义)", size=34,
    items=["团体: 团 – tập thể có tổ chức · 体 – bản thân hoặc toàn bộ sự vật → đoàn thể",
           "消防: 消 – tiêu diệt, trừ bỏ · 防 – phòng bị → phòng cháy chữa cháy",
           "追悼: 追 – nhớ lại quá khứ · 悼 – đau buồn tưởng nhớ → truy điệu",
           "事项: 事 – sự việc · 项 – loại, điều mục → các mục công việc",
           "事务: 事 – sự việc · 务 – công việc → sự vụ, công việc",
           "值班: 值 – luân phiên đảm nhận công việc trong một thời gian · 班 – ca làm việc, ca trực trong ngày → trực ban"],
    say=[F(0, "团体: chữ đầu là tập thể có tổ chức, chữ sau là bản thân hoặc toàn bộ sự vật. Ghép lại là đoàn thể, như 团体票, vé đoàn."),
         F(1, "消防: chữ đầu là tiêu diệt, trừ bỏ; chữ sau là phòng bị. Ghép lại là phòng cháy chữa cháy, như 消防车, xe cứu hỏa; 消防员, lính cứu hỏa."),
         F(2, "追悼: chữ đầu là nhớ lại quá khứ, chữ sau là đau buồn tưởng nhớ. Ghép lại là truy điệu, như 追悼会, lễ truy điệu."),
         F(3, "事项: chữ đầu là sự việc, chữ sau là chủng loại hay điều mục. Ghép lại là các mục công việc, như 注意事项, những điều cần chú ý."),
         F(4, "事务: cả hai chữ đều chỉ sự việc, công việc. Ghép lại là sự vụ, công việc, như 日常事务, công việc hằng ngày."),
         F(5, "值班: chữ đầu là luân phiên đảm nhận công việc trong một khoảng thời gian, chữ sau là ca làm việc hay ca trực quy định trong ngày. Ghép lại là trực ban, như 今天我值班, hôm nay tôi trực. Cảnh sát thường phải trực cả đêm đấy.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 37", size=36,
    items=["Từ vựng trọng tâm: 嫌疑 · 线索 · 慎重 · 麻痹 · 考验 · 沉着 · 部署 · 埋伏 · 逮捕 · 包袱 · 信赖 · 光辉",
           "Ngữ pháp: 为……起见 (để cho…, đặt đầu câu) · 暂且 (tạm thời, tạm)",
           "Phân biệt: 恐惧 (tâm lý sợ hãi của người) ≠ 恐怖 (sự việc, cảnh tượng đáng sợ)",
           "Viết: 照应 – nhan đề và nội dung, mở đầu và kết thúc, hình ảnh lặp lại",
           "## Bài tập về nhà",
           "Viết bài 警察故事 (ít nhất 400 chữ), dùng từ mới, 为……起见, 暂且 và hô ứng đầu cuối"],
    say=["Chúng ta cùng tổng kết bài ba mươi bảy.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 嫌疑，线索，慎重，麻痹，考验，沉着，部署，埋伏，逮捕，包袱，信赖，光辉. Nhớ cả những từ dễ nhầm với tiếng Việt như 化妆, 考验, 情报, 平面."),
         F(1, "Về ngữ pháp: 为了……起见 nghĩa là để cho…, vì mục đích…, đặt ở đầu câu. 暂且 nghĩa là tạm thời, tạm, đứng trước động từ."),
         F(2, "Về phân biệt từ: 恐惧 là nỗi sợ trong lòng người, chủ ngữ là người; 恐怖 là sự việc, cảnh tượng đáng sợ."),
         F(3, "Về kỹ năng viết: 照应, hô ứng trước sau, có thể là nhan đề với nội dung, mở đầu với kết thúc, hoặc một hình ảnh lặp lại xuyên suốt."),
         F(5, "Bài tập về nhà: các bạn hãy viết một bài văn với đầu đề 警察故事, ít nhất bốn trăm chữ. Hãy dùng các từ mới, hai điểm ngữ pháp 为了……起见 và 暂且, và nhớ cho câu mở đầu và câu kết thúc hô ứng với nhau nhé."),
         "Như vậy là chúng ta đã học xong bài ba mươi bảy, bài mở đầu của Đơn vị mười. Cảm ơn các bạn đã theo dõi bài giảng. Hẹn gặp lại các bạn ở bài ba mươi tám: 慧眼捕捉商机, Con mắt tinh tường nắm bắt cơ hội kinh doanh. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Hạ) – Bài 37: 警察的故事 (Những câu chuyện về cảnh sát)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thứ tự quan trọng: cụm dài trước)
    "tts_replace": {"为王某所为": "维王某所维",  # wéi … wéi
                    "了如指掌": "瞭如指掌",      # liǎo
                    "应得的": "英得的",          # yīngdé
                    "朝自己": "潮自己",          # cháo
                    "薄薄的": "雹雹的",          # báobáo
                    "干了几天": "赣了几天",      # gàn
                    "不想干了": "不想赣了",      # gàn
                    "为题": "维题",              # 以……为题 wéi
                    "着重": "酌重",              # zhuózhòng
                    "曾在": "层在",              # céng
                    "的确": "敌确",              # díquè
                    "参与": "参预",              # cānyù
                    "沉着": "沉酌",              # chénzhuó
                    "累立": "垒立",              # lěi lì
                    "扒开": "巴开",              # bā kāi
                    "空隙": "控隙",              # kòngxì
                    "中毒": "众毒",              # zhòngdú
                    "分子": "份子",              # fènzǐ (犯罪分子, 恐怖分子)
                    "分为": "分维",              # fēnwéi
                    "尽量": "紧量",              # jǐnliàng
                    "地处": "地楚",              # dìchǔ
                    "只得": "只德",              # zhǐdé
                    "照应": "照映",              # zhàoyìng
                    "血腥": "谑腥",              # xuèxīng
                    "蹊跷": "期跷",              # qīqiāo
                    "试种": "试众",              # shìzhòng
                    "睡觉": "睡叫"},             # shuìjiào
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai37.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
