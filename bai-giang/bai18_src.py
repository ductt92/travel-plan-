#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Thượng) – Bài 18 «神奇的丝瓜». Chạy để sinh bai18.json."""
import json
import os

TAG = "HSK 6 (Thượng) · Bài 18 · 神奇的丝瓜"
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
    zh="神奇的丝瓜", py="Shénqí de sīguā",
    vi="Bài 18: Quả mướp thần kỳ",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Thượng.",
         "Hôm nay chúng ta học bài mười tám: 神奇的丝瓜。 Nghĩa là: Quả mướp thần kỳ.",
         "Bài này thuộc Chủ đề năm, 美丽家园, Quê hương xinh đẹp. Bài khóa được cải biên từ bài văn cùng tên của 季羡林, Quý Tiện Lâm, một học giả và nhà văn nổi tiếng của Trung Quốc.",
         "Tác giả kể lại chuyện mấy cây mướp trồng bên tòa nhà mình ở. Cây mướp leo từ tầng một lên tầng ba, rồi những quả mướp lớn dần, treo lơ lửng giữa không trung. Tác giả cứ lo quả sẽ rơi xuống, nhưng lần nào cây mướp cũng tự tìm được cách. Cuối cùng ông tự hỏi: phải chăng cây mướp cũng biết suy nghĩ?",
         "Qua bài này, chúng ta sẽ học cách quan sát thiên nhiên thật tỉ mỉ, và cách miêu tả quá trình lớn lên của một loài cây sao cho sinh động."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài khóa: quá trình lớn lên của cây mướp và những nỗi lo của nhân vật tôi",
           "Nắm vững 48 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: phó từ 随即, phó từ 宁愿, cấu trúc khẩu ngữ A归A",
           "Phân biệt liên từ 连同 và phó từ 一起",
           "Kỹ năng: miêu tả quá trình biến đổi (theo bài tập 4) · Mở rộng: 16 cặp từ gần nghĩa"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa: cây mướp lớn lên như thế nào, nhân vật tôi đã lo lắng những gì, và vì sao ông thấy cây mướp thật thần kỳ."),
         F(1, "Thứ hai, nắm vững bốn mươi tám từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học ba điểm ngữ pháp: phó từ 随即, nghĩa là ngay sau đó; phó từ 宁愿, nghĩa là thà rằng; và cấu trúc khẩu ngữ A归A, ví dụ 不解归不解, không hiểu thì không hiểu."),
         F(3, "Thứ tư, phân biệt hai từ đều có nghĩa là cùng với: 连同 và 一起."),
         F(4, "Thứ năm, kỹ năng miêu tả quá trình biến đổi của sự vật, lấy từ bài tập bốn của sách; và phần mở rộng với mười sáu cặp từ gần nghĩa."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Khởi động 1: Gọi tên các bộ phận của cây mướp", size=40,
    items=["丝瓜 sīguā – quả mướp (treo trên giàn)",
           "瓜茎 guā jīng – thân, dây mướp (leo lên tường)",
           "瓜叶 guā yè – lá mướp (to, xanh, có thùy)",
           "花瓣 huābàn – cánh hoa (mướp có hoa màu vàng)",
           "土壤 tǔrǎng – đất (nơi cây mọc lên)"],
    say=["Chúng ta bắt đầu bằng phần khởi động. Sách đưa ra một bức ảnh cây mướp, và yêu cầu chọn tên thích hợp điền vào đúng vị trí. Có năm cái tên.",
         F(0, "丝瓜。 Là quả mướp. Quả mướp dài, màu xanh, treo lủng lẳng trên giàn."),
         F(1, "瓜茎。 Là thân, hay dây của cây mướp. 茎 nghĩa là thân cây. Dây mướp rất mảnh nhưng leo được rất cao."),
         F(2, "瓜叶。 Là lá mướp. Lá mướp to, có nhiều thùy, mọc dọc theo dây."),
         F(3, "花瓣。 Là cánh hoa. Hoa mướp có màu vàng, các bạn sẽ gặp lại hình ảnh này trong bài khóa."),
         F(4, "土壤。 Là đất, nơi hạt giống nảy mầm và rễ cây hút nước. Trong bức ảnh, đất nằm ở phía dưới gốc cây. Cả năm từ này đều xuất hiện trong bài khóa hôm nay đấy.")])

add("bullets", section="Khởi động 热身", title="Khởi động 2: Học từ theo yếu tố cấu tạo – 随 và 奇", size=38,
    items=["## 随 (tùy): đi theo, ngay theo; tùy ý",
           "随即 ngay sau đó · 随着 cùng với · 随身 mang theo người · 随手 tiện tay · 随后 tiếp sau đó · 随从 tùy tùng",
           "随便 tùy tiện · 随时 bất cứ lúc nào · 随口 buột miệng · 随意 tùy ý · 随地 bất cứ chỗ nào · 跟随 đi theo",
           "## 奇 (kỳ): lạ, khác thường",
           "神奇 thần kỳ · 好奇 tò mò · 新奇 mới lạ · 稀奇 hiếm lạ · 奇怪 kỳ quái · 奇妙 kỳ diệu",
           "奇特 đặc biệt lạ · 奇景 cảnh lạ · 奇谈 chuyện lạ · 奇迹 kỳ tích · 千奇百怪 muôn hình vạn trạng"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo, rất có lợi cho người Việt.",
         F(0, "Nhóm thứ nhất có chữ 随, Hán Việt là tùy. Nghĩa gốc là đi theo, từ đó có nghĩa ngay theo sau, và tùy ý."),
         F(1, "随即，随着，随身，随手，随后，随从。 Tức là: ngay sau đó, cùng với, mang theo người, tiện tay, tiếp sau đó, và tùy tùng. Từ 随即 là từ mới, đồng thời là điểm ngữ pháp thứ nhất của bài."),
         F(2, "随便，随时，随口，随意，随地，跟随。 Tức là: tùy tiện, bất cứ lúc nào, buột miệng, tùy ý, bất cứ chỗ nào, và đi theo."),
         F(3, "Nhóm thứ hai có chữ 奇, Hán Việt là kỳ, nghĩa là lạ, khác thường."),
         F(4, "神奇，好奇，新奇，稀奇，奇怪，奇妙。 Tức là: thần kỳ, tò mò, mới lạ, hiếm lạ, kỳ quái, và kỳ diệu. Tên bài hôm nay chính là 神奇的丝瓜."),
         F(5, "奇特，奇景，奇谈，奇迹，千奇百怪。 Tức là: đặc biệt lạ, cảnh lạ, chuyện lạ, kỳ tích, và muôn hình vạn trạng. Trong bài khóa, tác giả viết 我却看到了奇迹, tôi lại được thấy một kỳ tích.")])

add("bullets", section="Khởi động 热身", title="Khởi động 2: Học từ theo yếu tố cấu tạo – 转 và 落", size=38,
    items=["## 转 zhuǎn (chuyển): xoay, đổi hướng, thay đổi",
           "转眼 chớp mắt · 转身 quay người · 转头 quay đầu · 转脸 quay mặt · 转念 nghĩ lại · 转变 chuyển biến",
           "转学 chuyển trường · 转为 chuyển thành · 转瞬 chớp mắt · 好转 chuyển biến tốt · 回转 quay lại",
           "## 落 (lạc): rơi xuống, rụng xuống",
           "坠落 rơi xuống · 降落 hạ cánh · 飘落 bay lả tả rơi · 掉落 rơi rớt · 散落 rơi vãi · 洒落 vương vãi",
           "日落 mặt trời lặn · 落后 lạc hậu · 落下 rơi xuống · 落花 hoa rụng · 落叶 lá rụng · 落地 rơi xuống đất"],
    say=[F(0, "Nhóm thứ ba có chữ 转, sách ghi rõ đọc thanh ba, zhuǎn, Hán Việt là chuyển. Nghĩa là xoay, đổi hướng, thay đổi."),
         F(1, "转眼，转身，转头，转脸，转念，转变。 Tức là: chớp mắt, quay người, quay đầu, quay mặt, nghĩ lại, và chuyển biến. Bài khóa có cụm 转眼间, trong chớp mắt."),
         F(2, "转学，转为，转瞬，好转，回转。 Tức là: chuyển trường, chuyển thành, trong chớp mắt, chuyển biến tốt, và quay lại."),
         F(3, "Nhóm cuối cùng có chữ 落, Hán Việt là lạc, ở đây nghĩa là rơi xuống, rụng xuống."),
         F(4, "坠落，降落，飘落，掉落，散落，洒落。 Tức là: rơi xuống, hạ cánh, bay lả tả rơi xuống, rơi rớt, rơi vãi, và vương vãi. Từ 坠落 xuất hiện nhiều lần trong bài, vì tác giả luôn sợ quả mướp rơi xuống."),
         F(5, "日落，落后，落下，落花，落叶，落地。 Tức là: mặt trời lặn, lạc hậu, rơi xuống, hoa rụng, lá rụng, và rơi xuống đất."),
         "Các bạn thấy không, chỉ cần nắm nghĩa của một chữ gốc, ta có thể đoán được nghĩa của cả một nhóm từ. Hãy áp dụng cách này khi học từ mới nhé."])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay cho từ đa âm])
V = [
    ("神奇", "shénqí", "thần kỳ", "tính từ", "thần kỳ, kỳ diệu", "这是一个神奇的地方。", "Đây là một nơi thần kỳ.",
     "Tính từ, nghĩa là thần kỳ, kỳ diệu, hết sức đặc biệt, khó giải thích. Âm Hán Việt và nghĩa giống hệt tiếng Việt."),
    ("丝瓜", "sīguā", "ti qua", "danh từ", "(quả) mướp", "奶奶在院子里种了几棵丝瓜。", "Bà trồng mấy cây mướp trong sân.",
     "Danh từ, nghĩa là cây mướp, quả mướp. 丝 là sợi tơ, vì quả mướp già có rất nhiều xơ như sợi tơ, nên gọi là 丝瓜."),
    ("随即", "suíjí", "tùy tức", "phó từ", "lập tức, ngay sau đó", "他接到电话，随即出了门。", "Anh ấy nhận điện thoại, ngay sau đó liền ra khỏi nhà.",
     "Phó từ, nghĩa là lập tức, ngay sau đó, mang màu sắc văn viết. Đây là điểm ngữ pháp thứ nhất của bài."),
    ("株", "zhū", "chu", "lượng từ", "cây, gốc (lượng từ cho cây)", "门前有两株桃树。", "Trước cửa có hai cây đào.",
     "Lượng từ, dùng cho cây cối, tương đương cây, gốc. Trong bài có cụm 几株花, mấy cây hoa. 株 mang màu sắc văn viết hơn 棵."),
    ("粒", "lì", "lạp", "lượng từ", "viên, hạt", "碗里还剩下几粒米。", "Trong bát vẫn còn sót lại mấy hạt gạo.",
     "Lượng từ, dùng cho những vật nhỏ dạng hạt, như hạt gạo, hạt giống, viên thuốc. Trong bài có cụm 几粒丝瓜种子, mấy hạt giống mướp."),
    ("土壤", "tǔrǎng", "thổ nhưỡng", "danh từ", "đất, đất đai", "植物的生长离不开土壤。", "Sự sinh trưởng của thực vật không thể thiếu đất.",
     "Danh từ, nghĩa là đất, lớp đất trồng trọt. Tiếng Việt thổ nhưỡng là từ chuyên môn, còn 土壤 trong tiếng Trung dùng rất phổ biến."),
    ("肥沃", "féiwò", "phì ốc", "tính từ", "màu mỡ, phì nhiêu", "这一带土地肥沃，物产丰富。", "Vùng này đất đai màu mỡ, sản vật phong phú.",
     "Tính từ, nghĩa là màu mỡ, phì nhiêu, thường đi với 土地 hoặc 土壤. Bài khóa viết 土壤不是很肥沃, đất không màu mỡ lắm."),
    ("滋润", "zīrùn", "tư nhuận", "động từ", "làm ẩm, tưới nhuần", "春雨滋润着大地。", "Mưa xuân tưới nhuần mặt đất.",
     "Động từ, nghĩa là làm ẩm, tưới nhuần, nuôi dưỡng. Ngoài ra còn là tính từ, nghĩa là ẩm mượt, như 皮肤很滋润, da rất mịn màng."),
    ("照耀", "zhàoyào", "chiếu diệu", "động từ", "chiếu rọi, soi sáng", "太阳照耀着整个村庄。", "Mặt trời chiếu rọi khắp ngôi làng.",
     "Động từ, nghĩa là chiếu rọi, soi sáng, thường nói về ánh mặt trời. Trong bài có cụm 阳光的照耀, sự chiếu rọi của ánh mặt trời."),
    ("惊讶", "jīngyà", "kinh nhạ", "tính từ", "kinh ngạc, ngạc nhiên", "听到这个消息，大家都很惊讶。", "Nghe tin này, mọi người đều rất ngạc nhiên.",
     "Tính từ, nghĩa là kinh ngạc, ngạc nhiên. Trong bài có cụm 我惊讶地发现, tôi ngạc nhiên phát hiện ra."),
    ("愣", "lèng", "lăng", "phó từ", "cứ, khăng khăng, một mực (khẩu ngữ)", "大家都劝他休息，他愣是不听。", "Mọi người đều khuyên anh ấy nghỉ, anh ấy cứ nhất quyết không nghe.",
     "Phó từ khẩu ngữ, thường nói thành 愣是, nghĩa là cứ, khăng khăng, một mực làm trái với lẽ thường hay trái ý người khác. Ngoài ra, 愣 còn là động từ, nghĩa là ngây người ra, như 发愣."),
    ("拔苗助长", "bámiáo-zhùzhǎng", "bạt miêu trợ trưởng", "thành ngữ", "nóng vội hỏng việc, đốt cháy giai đoạn", "教育孩子不能拔苗助长。", "Dạy con không được nóng vội đốt cháy giai đoạn.",
     "Thành ngữ. Nghĩa đen là nhổ mạ lên cho mau lớn. Chuyện kể một người nước Tống thấy lúa lớn chậm, bèn kéo từng cây mạ lên, kết quả cả ruộng lúa chết khô. Nghĩa bóng là nóng vội, làm trái quy luật, kết quả hỏng việc."),
    ("宁愿", "nìngyuàn", "ninh nguyện", "phó từ", "thà rằng", "我宁愿走路，也不想挤公共汽车。", "Tôi thà đi bộ, chứ không muốn chen chúc trên xe buýt.",
     "Phó từ, nghĩa là thà rằng, dùng khi đã so sánh hơn thiệt rồi chọn một cách. Chú ý: âm tiết đầu đọc thanh bốn. Đây là điểm ngữ pháp thứ hai của bài."),
    ("疲倦", "píjuàn", "bì quyện", "tính từ", "mệt mỏi, mệt lử", "他一脸疲倦地回到了家。", "Anh ấy về đến nhà với vẻ mặt mệt mỏi.",
     "Tính từ, nghĩa là mệt mỏi, uể oải, gần nghĩa với 疲劳 và 累. Trong bài có câu 我每天工作疲倦了, mỗi ngày làm việc mệt rồi."),
    ("茎", "jīng", "hành", "danh từ", "thân cây, cọng", "这种花的茎又细又长。", "Thân của loài hoa này vừa mảnh vừa dài.",
     "Danh từ, nghĩa là thân cây, cọng. Trong bài, 瓜茎 là dây mướp. Hán Việt là hành, như trong từ căn hành, tức là thân rễ."),
    ("幢", "zhuàng", "tràng", "lượng từ", "tòa, ngôi, căn (nhà)", "那幢楼一共有二十层。", "Tòa nhà kia có tất cả hai mươi tầng.",
     "Lượng từ, dùng cho nhà cửa, tương đương tòa, ngôi. Nghĩa giống từ 栋 các bạn đã học ở bài năm. Trong bài có cụm 我们这幢楼, tòa nhà này của chúng tôi.", "壮"),
    ("陡峭", "dǒuqiào", "đẩu tiễu", "tính từ", "dốc đứng, cheo leo", "这条山路十分陡峭。", "Con đường núi này rất dốc đứng.",
     "Tính từ, nghĩa là dốc đứng, cheo leo, thường nói về núi, vách đá. Tác giả dùng 陡峭的楼墙 để nói bức tường nhà thẳng đứng, rất khó leo."),
    ("挺拔", "tǐngbá", "đĩnh bạt", "tính từ", "thẳng tắp, cao vút", "路边的白杨树高大挺拔。", "Hàng bạch dương bên đường cao lớn thẳng tắp.",
     "Tính từ, nghĩa là thẳng tắp, cao vút, đầy sức sống. Thường dùng cho cây cối, núi non, hoặc dáng người."),
    ("茂盛", "màoshèng", "mậu thịnh", "tính từ", "xanh tươi, tươi tốt", "公园里的树木长得很茂盛。", "Cây cối trong công viên mọc rất xanh tốt.",
     "Tính từ, nghĩa là xanh tươi, sum suê, nói về cây cỏ phát triển tốt. Trong bài có cụm 叶子茂盛, lá xanh tốt."),
    ("覆盖", "fùgài", "phúc cái", "động từ", "che, phủ", "大雪覆盖了整个城市。", "Tuyết lớn phủ kín cả thành phố.",
     "Động từ, nghĩa là che phủ, bao phủ. Ngày nay còn dùng cho phạm vi, như 网络覆盖, sóng mạng phủ khắp."),
    ("水泥", "shuǐní", "thủy nê", "danh từ", "xi măng", "工人们正在搅拌水泥。", "Các công nhân đang trộn xi măng.",
     "Danh từ, nghĩa là xi măng. 泥 là bùn, 水泥 là thứ bùn trộn với nước rồi đông cứng lại. Trong bài có cụm 水泥墙面, mặt tường xi măng."),
    ("朝气蓬勃", "zhāoqì péngbó", "triêu khí bồng bột", "thành ngữ", "tràn đầy sức sống", "年轻人朝气蓬勃，充满希望。", "Người trẻ tràn đầy sức sống, chan chứa hy vọng.",
     "Thành ngữ. 朝气 là khí buổi sớm mai, chỉ sức sống tươi trẻ; 蓬勃 là phát triển mạnh mẽ. Cẩn thận: tiếng Việt bồng bột là nông nổi, thiếu suy nghĩ; còn 蓬勃 là phồn thịnh, mạnh mẽ, hoàn toàn mang nghĩa tốt."),
    ("生机", "shēngjī", "sinh cơ", "danh từ", "sức sống; cơ hội sống", "春天来了，到处充满了生机。", "Mùa xuân đến, khắp nơi tràn đầy sức sống.",
     "Danh từ, nghĩa là sức sống, sự sống động; cũng có nghĩa là cơ hội sống sót. Cụm cố định hay gặp là 充满生机 và 生机勃勃."),
    ("花瓣", "huābàn", "hoa biện", "danh từ", "cánh hoa", "风一吹，花瓣落了一地。", "Gió thổi qua, cánh hoa rụng đầy mặt đất.",
     "Danh từ, nghĩa là cánh hoa. 瓣 là múi, cánh, như 一瓣橘子, một múi quýt."),
    ("点缀", "diǎnzhuì", "điểm xuyết", "động từ", "tô điểm, điểm xuyết", "几朵小花点缀在草地上。", "Mấy bông hoa nhỏ điểm xuyết trên bãi cỏ.",
     "Động từ, nghĩa là tô điểm, điểm xuyết, tức là thêm một chút gì đó để cảnh vật đẹp hơn. Âm Hán Việt và nghĩa giống tiếng Việt."),
    ("协调", "xiétiáo", "hiệp điều", "tính từ", "hài hòa, nhịp nhàng", "这件衣服的颜色搭配得很协调。", "Màu sắc của bộ quần áo này phối rất hài hòa.",
     "Tính từ, nghĩa là hài hòa, cân đối. Ngoài ra còn là động từ, nghĩa là điều phối, phối hợp, như 协调各部门的工作. Chú ý âm tiết thứ hai đọc là tiáo, thanh hai."),
    ("柔和", "róuhé", "nhu hòa", "tính từ", "mềm mại, dịu dàng, nhẹ nhàng", "房间里的灯光很柔和。", "Ánh đèn trong phòng rất dịu.",
     "Tính từ, nghĩa là mềm mại, dịu nhẹ, không gắt, dùng cho ánh sáng, màu sắc, giọng nói."),
    ("分量", "fènliàng", "phân lượng", "danh từ", "trọng lượng, sức nặng", "这个箱子的分量可不轻。", "Cái hòm này nặng ra phết đấy.",
     "Danh từ, nghĩa là trọng lượng, sức nặng. Nghĩa bóng là tầm quan trọng, như 他说话很有分量, lời anh ấy nói rất có trọng lượng. Chú ý cách đọc: fènliàng, cả hai âm tiết đều thanh bốn."),
    ("悬挂", "xuánguà", "huyền quải", "động từ", "treo", "墙上悬挂着一幅山水画。", "Trên tường treo một bức tranh sơn thủy.",
     "Động từ, nghĩa là treo, treo lơ lửng. 悬 là treo lơ lửng giữa không trung, như trong từ huyền không."),
    ("负担", "fùdān", "phụ đảm", "động từ", "chịu, gánh vác, đảm nhiệm", "他一个人负担全家的生活。", "Một mình anh ấy gánh vác cuộc sống của cả nhà.",
     "Động từ, nghĩa là gánh vác, chịu đựng. Cũng là danh từ, nghĩa là gánh nặng, như 减轻负担, giảm bớt gánh nặng. Mẫu hay gặp: 负担不起, gánh không nổi."),
    ("坠", "zhuì", "trụy", "động từ", "rơi, rớt", "一个苹果从树上坠了下来。", "Một quả táo từ trên cây rơi xuống.",
     "Động từ, nghĩa là rơi, rớt từ trên cao xuống. Thường dùng trong từ 坠落. Hán Việt là trụy, như trong từ trụy lạc."),
    ("沉重", "chénzhòng", "trầm trọng", "tính từ", "nặng nề, nặng trĩu", "听到这个坏消息，他的心情很沉重。", "Nghe tin xấu này, lòng anh ấy rất nặng nề.",
     "Tính từ, nghĩa là nặng nề, nặng trĩu, nói về đồ vật hoặc tâm trạng. Cẩn thận: tiếng Việt trầm trọng là nghiêm trọng, như bệnh trầm trọng; ý đó tiếng Trung phải nói là 严重."),
    ("节制", "jiézhì", "tiết chế", "động từ", "hạn chế, có chừng mực", "喝酒一定要有节制。", "Uống rượu nhất định phải có chừng mực.",
     "Động từ, nghĩa là hạn chế, kiềm chế, giữ chừng mực. Tác giả viết quả mướp 很有节制, rất biết chừng mực, như thể nó là con người."),
    ("辫子", "biànzi", "biện tử", "danh từ", "bím tóc", "小姑娘梳着两条小辫子。", "Cô bé tết hai bím tóc nhỏ.",
     "Danh từ, nghĩa là bím tóc. Âm tiết thứ hai đọc nhẹ. Trong bài, tác giả so sánh quả mướp non với bím tóc của cô bé."),
    ("臂", "bì", "tý", "danh từ", "cánh tay", "他的手臂受伤了。", "Cánh tay của anh ấy bị thương.",
     "Danh từ, nghĩa là cánh tay, hay gặp trong từ 手臂. Trong khẩu ngữ, người ta hay nói 胳膊. Hán Việt là tý, như trong từ thủ tý.", "币"),
    ("呵", "hē", "ha", "thán từ", "a, ơ, ôi, chà (ngạc nhiên)", "呵，你来得真早！", "Chà, bạn đến sớm thật đấy!",
     "Thán từ, biểu thị sự ngạc nhiên, tiếng Việt là a, ơ, ôi, chà. Trong bài, tác giả thốt lên 呵 khi thấy hai quả mướp đã to như cánh tay trẻ con.", "喝"),
    ("与日俱增", "yǔrì-jùzēng", "dữ nhật câu tăng", "thành ngữ", "tăng lên từng ngày", "他对中国文化的兴趣与日俱增。", "Hứng thú của anh ấy với văn hóa Trung Quốc tăng lên từng ngày.",
     "Thành ngữ. 与日 là cùng với ngày tháng, 俱增 là cùng tăng lên, nghĩa là ngày càng tăng. Trong bài có câu 我的担心与日俱增, nỗi lo của tôi ngày một lớn."),
    ("梢", "shāo", "sao", "danh từ", "ngọn (cây)", "小鸟站在树梢上唱歌。", "Chú chim nhỏ đứng hót trên ngọn cây.",
     "Danh từ, nghĩa là ngọn, phần đầu nhỏ của cành cây, dây leo. Trong bài có cụm 瓜茎末梢, đầu ngọn dây mướp."),
    ("垂直", "chuízhí", "thùy trực", "động từ", "thẳng đứng, vuông góc", "这两条线互相垂直。", "Hai đường thẳng này vuông góc với nhau.",
     "Nghĩa là thẳng đứng, hoặc vuông góc. 垂 là rủ xuống, 直 là thẳng. Trong bài, 垂直地吊在那里 là treo thẳng đứng ở đó."),
    ("吊", "diào", "điếu", "động từ", "treo, buộc", "天花板上吊着一盏灯。", "Trên trần nhà treo một ngọn đèn.",
     "Động từ, nghĩa là treo, móc lên cao. Ngoài ra còn có nghĩa là cẩu, kéo lên bằng dây, như 吊车, xe cẩu."),
    ("晃", "huàng", "hoảng", "động từ", "lắc lư, đu đưa", "树枝在风中晃来晃去。", "Cành cây đu đưa qua lại trong gió.",
     "Động từ, nghĩa là lắc lư, đu đưa, đọc thanh bốn. Mẫu 晃来晃去 là đu đưa qua lại. Chữ này khi đọc thanh ba có nghĩa khác: lóe sáng, vụt qua.", "滉"),
    ("断定", "duàndìng", "đoán định", "động từ", "nhận định, kết luận", "根据这些证据，警察断定他就是小偷。", "Căn cứ vào những chứng cứ này, cảnh sát kết luận hắn chính là kẻ trộm.",
     "Động từ, nghĩa là khẳng định, kết luận dứt khoát. Cẩn thận: chữ 断 ở đây là phán đoán, quyết định; không phải là đoán mò như chữ đoán trong tiếng Việt."),
    ("连同", "liántóng", "liên đồng", "liên từ", "kể cả, cùng với", "请把申请表连同照片一起交上来。", "Hãy nộp đơn đăng ký cùng với ảnh lên đây.",
     "Liên từ, nghĩa là kể cả, cùng với, nối hai danh từ. Lát nữa chúng ta sẽ so sánh kỹ từ này với từ 一起."),
    ("凹凸", "āotū", "ao đột", "tính từ", "lồi lõm, gồ ghề", "这条路凹凸不平，很难走。", "Con đường này lồi lõm gồ ghề, rất khó đi.",
     "Tính từ, nghĩa là lồi lõm, gồ ghề. 凹 là lõm, 凸 là lồi, hai chữ này nhìn hình là đoán được nghĩa. Cụm hay gặp: 凹凸不平."),
    ("修建", "xiūjiàn", "tu kiến", "động từ", "thi công, xây dựng, xây cất", "这座桥是去年修建的。", "Cây cầu này được xây dựng vào năm ngoái.",
     "Động từ, nghĩa là xây dựng, xây cất các công trình như cầu, đường, nhà cửa."),
    ("不可思议", "bùkě-sīyì", "bất khả tư nghị", "thành ngữ", "không thể tưởng tượng nổi", "他一个人完成了这么多工作，真是不可思议。", "Một mình anh ấy làm xong nhiều việc như vậy, thật không thể tin nổi.",
     "Thành ngữ, nghĩa là không thể tưởng tượng nổi, khó mà giải thích được. Tiếng Việt cũng có cách nói bất khả tư nghị, nghĩa tương tự."),
    ("徘徊", "páihuái", "bồi hồi", "động từ", "đi đi lại lại, loanh quanh; do dự", "他在门口徘徊了很久，还是没有进去。", "Anh ấy đi đi lại lại ở cửa rất lâu, rốt cuộc vẫn không vào.",
     "Động từ, nghĩa là đi đi lại lại quanh một chỗ; nghĩa bóng là do dự, lưỡng lự. Cẩn thận, đây là từ dễ nhầm: tiếng Việt bồi hồi là xao xuyến, xúc động; còn 徘徊 là hành động đi tới đi lui."),
    ("一如既往", "yìrú-jìwǎng", "nhất như ký vãng", "thành ngữ", "trước sau như một, như thường lệ", "我们会一如既往地支持你。", "Chúng tôi sẽ luôn ủng hộ bạn như trước đây.",
     "Thành ngữ, nghĩa là hoàn toàn giống như trước đây, trước sau như một. Thường dùng theo mẫu 一如既往地 cộng động từ."),
]

add("bullets", chapter="Từ mới (48 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 18 có 48 từ mới, chia thành 16 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 宁愿 (nìng) · 幢 (zhuàng) · 朝气 (zhāo) · 协调 (tiáo) · 分量 (fèn) · 晃 (huàng)",
           "Từ dễ nhầm: 朝气蓬勃 · 沉重 · 断定 · 徘徊"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có bốn mươi tám từ, thầy chia thành mười sáu nhóm nhỏ, mỗi nhóm ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Bài này có khá nhiều chữ đa âm, như 宁愿，朝气，协调，分量, và hai lượng từ, động từ một chữ là tòa nhà và lắc lư. Thầy sẽ nhắc cách đọc khi gặp."),
         F(4, "Ngoài ra, có mấy từ Hán Việt rất dễ hiểu nhầm, như 朝气蓬勃，沉重，断定，徘徊. Nghĩa của chúng trong tiếng Trung khác với tiếng Việt, các bạn nhớ nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

sizes = [3] * 16
assert sum(sizes) == len(V)
g = 0
for gs in sizes:
    group = V[g:g + gs]
    words, say = [], []
    for i, item in enumerate(group):
        zh, py, hv, loai, vi, ex, exvi, expl = item[:8]
        sp = item[8] if len(item) > 8 else zh  # chữ đọc thay cho từ đa âm đứng một mình
        n = g + i + 1
        words.append({"zh": zh, "py": py, "hv": hv.upper(), "loai": f"{n}. {loai}", "vi": vi, "ex": ex, "exvi": exvi})
        head = f"Từ số {n}: {zh}。 {zh}。 Hán Việt là {hv}."
        say.append(F(i, f"Từ số {n}: {sp}。 {sp}。 Hán Việt là {hv}.", cap=head, zr=120))
        say.append(F(i, f"{expl} Ví dụ: {ex}{'' if ex[-1] in '。…？！，' else '，'} {exvi[0].upper() + exvi[1:]}{'' if exvi.endswith(('.', '!', '?')) else '.'}", zr=130))
    add("vocab", section="Từ mới 生词", title=f"Từ mới ({g + 1}–{g + len(group)} / {len(V)})",
        words=words, say=say)
    g += gs

# ======================= BÀI KHÓA =======================
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung nếu khác])
P = [
    ("春天，孩子们在楼旁空地上开出一个小小的花园，随即种上了一棵树、几株花和几粒丝瓜种子。",
     "Mùa xuân, bọn trẻ mở một khu vườn nho nhỏ trên khoảng đất trống cạnh tòa nhà, rồi ngay sau đó trồng một cái cây, mấy cây hoa và mấy hạt giống mướp.",
     ["空地 là khoảng đất trống. 开出一个花园 là khai phá, mở ra một khu vườn. 随即 nối hai hành động liền nhau: mở vườn xong là trồng ngay.",
      "Các bạn để ý ba lượng từ khác nhau: 一棵树，几株花，几粒种子. Cây to dùng 棵, cây hoa dùng 株, hạt giống dùng 粒."]),
    ("土壤不是很肥沃，但有水的滋润，阳光的照耀，没几天，丝瓜就从土里冒了出来，接着我惊讶地发现，它好像每时每刻都在长大。",
     "Đất không màu mỡ lắm, nhưng có nước tưới nhuần, có ánh mặt trời chiếu rọi, chẳng mấy ngày, cây mướp đã nhú lên khỏi mặt đất, tiếp đó tôi ngạc nhiên phát hiện ra, hình như nó lớn lên từng giờ từng phút.",
     ["水的滋润，阳光的照耀 là hai cụm danh từ song song, rất hay dùng khi tả cây cối. 冒了出来 là nhú lên, trồi lên.",
      "每时每刻 là từng giờ từng phút, mọi lúc. Câu này là gợi ý cho bài tập năm: môi trường sinh trưởng của cây mướp là đất, nước và ánh nắng."]),
    ("看着丝瓜，我心中难免不解：古人是怎么想的，愣是编出个拔苗助长的故事来？要是我，宁愿用别的比喻。",
     "Nhìn cây mướp, trong lòng tôi khó tránh khỏi thắc mắc: người xưa nghĩ thế nào mà cứ nhất định bịa ra câu chuyện nhổ mạ cho mau lớn? Nếu là tôi, tôi thà dùng một phép so sánh khác.",
     ["难免 là khó tránh khỏi. 不解 là không hiểu, thắc mắc. 愣是 là cứ một mực, nhất định. 编出个……来 là bịa ra một câu chuyện.",
      "Ý tác giả: cây mướp tự lớn nhanh như thế, cần gì phải nhổ cho mau lớn. 要是我，宁愿…… là nếu là tôi thì tôi thà…, đây là điểm ngữ pháp 宁愿."]),
    ("不解归不解，我每天工作疲倦了，都要去看看那几棵丝瓜。丝瓜长得很快，转眼间，瓜茎已经爬上了我们这幢楼陡峭的楼墙。",
     "Không hiểu thì không hiểu, nhưng mỗi ngày làm việc mệt mỏi, tôi đều ra ngắm mấy cây mướp ấy. Mướp lớn rất nhanh, chớp mắt một cái, dây mướp đã leo lên bức tường dốc đứng của tòa nhà chúng tôi.",
     ["不解归不解 là cấu trúc A归A: không hiểu thì không hiểu, nhưng vẫn làm việc khác. Đây là điểm ngữ pháp thứ ba.",
      "转眼间 là trong chớp mắt, nhấn mạnh tốc độ lớn nhanh. 爬上 là leo lên, tác giả dùng động từ của người và động vật cho cây mướp."]),
    ("接着，它从一楼爬上了二楼，又从二楼爬上了三楼。瓜茎只有细绳一般粗，却能输送足够的水分和养料，使得瓜茎挺拔，叶子茂盛。",
     "Tiếp đó, nó leo từ tầng một lên tầng hai, rồi lại từ tầng hai lên tầng ba. Dây mướp chỉ to bằng sợi dây mảnh, vậy mà có thể vận chuyển đủ nước và chất dinh dưỡng, khiến dây mướp vươn thẳng, lá xanh tốt.",
     ["细绳一般粗 là to bằng sợi dây mảnh, mẫu so sánh A一般 cộng tính từ, nghĩa là như A. 输送 là vận chuyển, 养料 là chất dinh dưỡng.",
      "只有……却能……使得…… là mẫu câu của bài tập bốn: tuy chỉ nhỏ bé, nhưng lại làm được việc lớn, dẫn đến kết quả tốt. Thầy sẽ phân tích kỹ trong phần kỹ năng."]),
    ("那覆盖在水泥墙面上的一片浓绿显得朝气蓬勃，充满了生机与活力。",
     "Mảng xanh thẫm phủ trên mặt tường xi măng trông tràn đầy sức sống, chan chứa sinh khí và sức sống.",
     ["覆盖在水泥墙面上的 là định ngữ dài bổ nghĩa cho 一片浓绿, một mảng xanh đậm. 显得 là trông có vẻ.",
      "Màu xám của xi măng đối lập với màu xanh của lá, làm nổi bật sức sống của cây mướp."]),
    ("又过了几天，丝瓜开花了，黄色的花瓣点缀在绿叶之间，颜色协调，柔和精致。再过几天，黄花变成了小小的丝瓜。",
     "Lại qua mấy ngày, mướp ra hoa, những cánh hoa màu vàng điểm xuyết giữa đám lá xanh, màu sắc hài hòa, dịu dàng mà tinh tế. Vài ngày nữa, hoa vàng biến thành những quả mướp nho nhỏ.",
     ["又过了几天，再过几天 là các từ chỉ thời gian, giúp câu chuyện đi theo trình tự: mọc lên, leo tường, ra hoa, kết quả.",
      "点缀在绿叶之间 là điểm xuyết giữa lá xanh. 精致 là tinh xảo, tinh tế. Vàng trên nền xanh, nên tác giả khen 颜色协调."]),
    ("瓜越长越长，分量也越来越重。它悬挂在空中，细细的瓜茎好像负担不起瓜的重量，时刻都要坠落下来，我的心也变得沉重起来。",
     "Quả mướp càng lớn càng dài, cũng càng ngày càng nặng. Nó treo lơ lửng giữa không trung, dây mướp mảnh mai dường như không gánh nổi sức nặng của quả, lúc nào cũng như sắp rơi xuống, lòng tôi cũng trở nên nặng trĩu.",
     ["Chú ý 越长越长: chữ thứ nhất đọc zhǎng, là lớn lên; chữ thứ hai đọc cháng, là dài. Cả câu nghĩa là càng lớn càng dài.",
      "负担不起 là gánh không nổi. Các bạn để ý cách chơi chữ: quả mướp nặng, nên lòng tôi cũng 沉重, nặng trĩu theo."]),
    ("不久就证明，我的担心是多余的。最初长出来的瓜好像很有节制，长到一定程度就不长了，而三楼那家的窗外，又长出来两个瓜。",
     "Không lâu sau đã chứng minh, nỗi lo của tôi là thừa. Quả mướp mọc ra đầu tiên dường như rất biết chừng mực, lớn đến một mức nhất định thì không lớn nữa, còn ở ngoài cửa sổ nhà tầng ba, lại mọc thêm hai quả nữa.",
     ["多余 là thừa, không cần thiết. 很有节制 là rất biết chừng mực, tác giả nhân hóa quả mướp như một con người biết tự kiềm chế.",
      "长到一定程度就不长了 là lớn đến mức nào đó thì thôi không lớn nữa. Đây là lần lo lắng thứ nhất, và cây mướp đã tự giải quyết."]),
    ("这两个瓜开始只有小姑娘的辫子一般粗细，不久就长得如小孩胳膊一般粗了。呵，这两个瓜加起来恐怕有五六斤了，那一根细细的茎怎么承担得住呢？我的担心与日俱增。",
     "Hai quả này lúc đầu chỉ to bằng bím tóc của cô bé, chẳng bao lâu đã to bằng cánh tay trẻ con. Chà, hai quả này cộng lại e là phải năm, sáu cân rồi, cái dây mảnh mai kia làm sao chịu nổi? Nỗi lo của tôi ngày một lớn.",
     ["辫子一般粗细，如小孩胳膊一般粗 là hai phép so sánh, cho thấy quả lớn rất nhanh. 斤 là cân Trung Quốc, bằng nửa ki-lô-gam.",
      "承担得住 là chịu đựng được, 怎么承担得住呢 là câu hỏi tu từ, ý là không thể chịu nổi. 与日俱增 là tăng lên từng ngày."]),
    ("没过几天，我发现我又错了，两个瓜不知什么时候弯了起来，舒舒服服地躺在了那家的窗台上。",
     "Chưa được mấy ngày, tôi phát hiện ra mình lại sai rồi, hai quả mướp chẳng biết từ lúc nào đã cong lại, nằm thoải mái trên bậu cửa sổ nhà ấy.",
     ["弯了起来 là cong lại, 起来 chỉ trạng thái bắt đầu xuất hiện. 窗台 là bậu cửa sổ.",
      "舒舒服服地躺在 là nằm thoải mái, lại là nhân hóa. Đây là lần lo lắng thứ hai, và cây mướp lại tự tìm ra cách."]),
    ("没几天，那两个大瓜下面的瓜茎末梢上，又长出来一个瓜，垂直地吊在那里，在风中晃来晃去。",
     "Chẳng mấy ngày sau, trên đầu ngọn dây mướp phía dưới hai quả to ấy, lại mọc ra một quả nữa, treo thẳng đứng ở đó, đu đưa qua lại trong gió.",
     ["末梢 là đầu ngọn. 垂直地吊在那里 là treo thẳng đứng ở đó, 地 đứng sau tính từ để làm trạng ngữ.",
      "晃来晃去 là đu đưa qua lại, mẫu V来V去 diễn tả động tác lặp đi lặp lại, như 走来走去, đi đi lại lại."]),
    ("我断定：这个瓜上面够不到窗台，下面也是空的，总有一天，瓜茎会禁不住瓜的分量，连同上面的两个大瓜一起坠落到地上。",
     "Tôi kết luận chắc chắn: quả này phía trên không với tới bậu cửa sổ, phía dưới cũng trống không, thể nào cũng có ngày dây mướp không chịu nổi sức nặng của quả, rồi cùng với hai quả to ở trên rơi cả xuống đất.",
     ["够不到 là không với tới. 禁不住 là không chịu nổi, chữ đầu đọc thanh một, jīn. 总有一天 là thể nào cũng có một ngày.",
      "连同……一起 là cùng với… tất cả, đây chính là từ 连同 trong phần phân biệt từ. Đây là lần lo lắng thứ ba, và lần này tác giả rất chắc chắn: 断定."]),
    ("这天一早，我却看到了奇迹，那个我断定会坠落下来的瓜，已经躺在了一个凹凸不平的台子上，那个台子是加固墙体时修建的。",
     "Sáng sớm hôm ấy, tôi lại được thấy một kỳ tích: quả mướp mà tôi đã khẳng định là sẽ rơi xuống, đã nằm trên một cái bệ lồi lõm, cái bệ ấy được xây khi gia cố bức tường.",
     ["却 ở đây biểu thị sự việc trái với dự đoán. 奇迹 là kỳ tích, điều kỳ diệu. 台子 là cái bệ, cái bục.",
      "加固墙体 là gia cố thân tường. Lần thứ ba, dự đoán của tác giả lại sai, cây mướp lại tìm được chỗ đỡ cho quả."]),
    ("真是不可思议！我徘徊在丝瓜下面，我觉得丝瓜有思想，能考虑问题，而且还有行动。它能让大瓜停止生长；它能给瓜找到承担重量的地方。",
     "Thật không thể tưởng tượng nổi! Tôi đi đi lại lại dưới giàn mướp, tôi cảm thấy cây mướp có tư tưởng, biết suy nghĩ vấn đề, mà còn biết hành động nữa. Nó có thể khiến quả to ngừng lớn; nó có thể tìm cho quả một nơi đỡ được sức nặng.",
     ["徘徊在丝瓜下面 là đi tới đi lui dưới giàn mướp, cho thấy tác giả đang suy nghĩ rất lung.",
      "Hai vế 它能……；它能…… song song, ngăn cách bằng dấu chấm phẩy, tóm lại hai điều kỳ lạ mà cây mướp đã làm."]),
    ("如果真是这样，丝瓜用什么来思考呢？丝瓜靠什么来指导自己的行动呢？我想了又想，越想越糊涂，而丝瓜却一如既往地含笑面对秋阳。",
     "Nếu quả thật là như vậy, thì cây mướp dùng cái gì để suy nghĩ? Cây mướp dựa vào cái gì để chỉ đạo hành động của mình? Tôi nghĩ đi nghĩ lại, càng nghĩ càng mơ hồ, còn cây mướp thì vẫn như mọi khi, mỉm cười đón ánh nắng mùa thu.",
     ["想了又想 là nghĩ đi nghĩ lại. 越想越糊涂 là càng nghĩ càng rối. 而……却…… đối lập con người đang băn khoăn với cây mướp ung dung.",
      "含笑面对秋阳 là mỉm cười đón nắng thu. Từ mùa xuân ở đầu bài đến mùa thu ở cuối bài, câu chuyện khép lại thật nhẹ nhàng, để lại cho người đọc nhiều suy ngẫm."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 神奇的丝瓜", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 神奇的丝瓜, dài tám trăm bốn mươi sáu chữ. Bài được cải biên từ bài văn cùng tên của học giả 季羡林.",
         F(0, "Thầy chia bài thành mười sáu đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
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
    items=["## 1. 描述一下丝瓜生长的环境 – môi trường sinh trưởng",
           "土壤不是很肥沃，但有水的滋润，阳光的照耀",
           "## 2. 说一说丝瓜生长的过程 – quá trình sinh trưởng",
           "种子 → 从土里冒出来 → 瓜茎爬楼：从一楼爬到三楼",
           "开花 → 小丝瓜 → 最初的瓜 → 后来的两个瓜 → 最下面的瓜"],
    say=["Bài tập năm của sách yêu cầu dựa vào gợi ý để tóm tắt nội dung chính của bài khóa. Chúng ta cùng làm luôn nhé.",
         F(0, "Câu hỏi một: hãy miêu tả môi trường sinh trưởng của cây mướp."),
         F(1, "土壤不是很肥沃，但有水的滋润，阳光的照耀。 Đất không màu mỡ lắm, nhưng có nước tưới nhuần và ánh nắng chiếu rọi."),
         F(2, "Câu hỏi hai: hãy kể lại quá trình sinh trưởng của cây mướp."),
         F(3, "Đầu tiên là hạt giống, rồi cây nhú lên khỏi mặt đất. Sau đó, dây mướp leo tường, từ tầng một lên tận tầng ba."),
         F(4, "Tiếp theo, mướp ra hoa, hoa biến thành quả nhỏ. Rồi lần lượt xuất hiện quả mướp đầu tiên, hai quả mướp sau đó, và quả mướp ở dưới cùng.")])

add("bullets", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5) – phần 2", size=34,
    items=["## 3. 描述一下“我”对丝瓜担心的过程 – những nỗi lo của “tôi”",
           "最初的瓜：怕瓜茎负担不起 → 长到一定程度就不长了",
           "三楼窗外的两个瓜：怕茎承担不住 → 弯起来躺在了窗台上",
           "末梢上的瓜：断定会坠落 → 躺在了加固墙体的台子上",
           "## 4. 丝瓜给“我”什么感觉？",
           "有思想、有行动 · 可是靠什么来思考、指导行动呢？越想越糊涂"],
    say=[F(0, "Câu hỏi ba: hãy miêu tả quá trình lo lắng của nhân vật tôi đối với cây mướp. Có ba lần lo lắng, và cả ba lần cây mướp đều tự giải quyết."),
         F(1, "Lần thứ nhất, quả mướp đầu tiên: tác giả sợ dây mướp gánh không nổi. Kết quả, quả lớn đến một mức nhất định thì không lớn nữa."),
         F(2, "Lần thứ hai, hai quả mướp ngoài cửa sổ tầng ba: tác giả sợ dây mảnh không chịu nổi. Kết quả, hai quả cong lại, nằm thoải mái trên bậu cửa sổ."),
         F(3, "Lần thứ ba, quả mướp ở đầu ngọn: tác giả khẳng định chắc chắn nó sẽ rơi. Kết quả, quả mướp đã nằm trên cái bệ được xây khi gia cố tường."),
         F(4, "Câu hỏi bốn: cây mướp mang lại cho nhân vật tôi cảm giác gì?"),
         F(5, "Tác giả cảm thấy cây mướp có tư tưởng, có hành động. Nhưng nó dựa vào cái gì để suy nghĩ và chỉ đạo hành động? Tác giả càng nghĩ càng mơ hồ. Bố cục này rất có ích khi các bạn tự kể lại bài khóa.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 随即", section="Ngữ pháp 注释", title="1. 随即 suíjí – ngay sau đó", size=36,
    items=["Phó từ: biểu thị sự việc xảy ra liền ngay sau một sự việc khác (紧跟着就发生)",
           "Mẫu: (việc thứ nhất)，随即 + động từ (việc thứ hai) · mang màu sắc văn viết",
           "缺乏父母之爱的孩子，不安全感也会随即产生。",
           "在公司的内部会议上，大家对这个产品一致看好，总经理更是信心百倍，随即开始制定市场开拓方案。",
           "春天，孩子们在楼旁空地上开出一个小小的花园，随即种上了一棵树、几株花和几粒丝瓜种子。"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là phó từ 随即.",
         F(0, "随即 là phó từ, biểu thị một sự việc xảy ra liền ngay sau một sự việc khác. Tiếng Việt dịch là ngay sau đó, liền, lập tức."),
         F(1, "Vế trước thường nêu sự việc thứ nhất, vế sau dùng 随即 cộng động từ để nêu sự việc thứ hai. 随即 mang màu sắc văn viết, nghĩa gần với 立即 và 马上, nhưng nhấn mạnh việc sau theo sát việc trước."),
         F(2, "Ví dụ một: 缺乏父母之爱的孩子，不安全感也会随即产生。 Những đứa trẻ thiếu tình thương của cha mẹ, cảm giác bất an cũng sẽ nảy sinh ngay theo đó."),
         F(3, "Ví dụ hai: 在公司的内部会议上，大家对这个产品一致看好，总经理更是信心百倍，随即开始制定市场开拓方案。 Trong cuộc họp nội bộ, mọi người đều đánh giá cao sản phẩm này, tổng giám đốc lại càng tràn đầy tự tin, ngay sau đó bắt đầu lập phương án mở rộng thị trường."),
         F(4, "Ví dụ ba, lấy từ bài khóa: 春天，孩子们在楼旁空地上开出一个小小的花园，随即种上了一棵树、几株花和几粒丝瓜种子。 Mở vườn xong, bọn trẻ trồng cây ngay.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: chọn vị trí thích hợp cho 随即", reveal=True, size=34,
    items=["(1) 他答应 A 了 B 一声，C 把手里的东西 D 递给我。",
           "Đáp án: C – 他答应了一声，随即把手里的东西递给我。",
           "(2) 他匆匆进了屋，A 说完必要的话之后 B 转身离去，C 根本不顾及对方究竟 D 听懂了多少。",
           "Đáp án: B – ……说完必要的话之后随即转身离去……",
           "(3) 我亲眼看到，A 一只鸟死了，另外 B 几只衔着那只死鸟飞到附近一个池塘的上空，将它 C 扔进池塘，D 又飞回原地。",
           "Đáp án: D – ……将它扔进池塘，随即又飞回原地。"],
    say=[F(0, "Luyện tập: chọn vị trí thích hợp cho 随即. Câu một: 他答应A了B一声，C把手里的东西D递给我。 Anh ấy đáp một tiếng, rồi đưa đồ trong tay cho tôi. Các bạn tạm dừng và chọn nhé."),
         F(1, "Đáp án: C. 他答应了一声，随即把手里的东西递给我。 Việc thứ nhất là đáp một tiếng, việc thứ hai theo ngay sau là đưa đồ. 随即 đứng trước cụm giới từ 把."),
         F(2, "Câu hai: 他匆匆进了屋，A说完必要的话之后B转身离去，C根本不顾及对方究竟D听懂了多少。 Anh ấy vội vã vào nhà, nói xong những điều cần thiết thì quay người đi, chẳng thèm để ý đối phương rốt cuộc hiểu được bao nhiêu."),
         F(3, "Đáp án: B. 说完必要的话之后随即转身离去。 Nói xong là quay người đi ngay."),
         F(4, "Câu ba: 我亲眼看到，A一只鸟死了，另外B几只衔着那只死鸟飞到附近一个池塘的上空，将它C扔进池塘，D又飞回原地。 Tôi tận mắt thấy một con chim chết, mấy con khác ngậm xác nó bay đến trên một cái ao gần đó, thả nó xuống ao, rồi lại bay về chỗ cũ."),
         F(5, "Đáp án: D. 将它扔进池塘，随即又飞回原地。 Thả xuống ao xong là bay về ngay. Mẹo: 随即 luôn đứng ở vế chỉ việc thứ hai, ngay trước động từ.")])

add("bullets", chapter="Ngữ pháp: 宁愿", section="Ngữ pháp 注释", title="2. 宁愿 nìngyuàn – thà rằng", size=36,
    items=["Phó từ, dùng trong câu phức lựa chọn: so sánh lợi hại rồi chọn một cách làm",
           "Mẫu: 宁愿……也要…… (chọn A để đạt B) · 宁愿……也不…… (chọn A chứ không B)",
           "Cũng nói: 宁可、宁肯",
           "我心中难免不解：古人是怎么想的，愣是编出个拔苗助长的故事来？要是我，宁愿用别的比喻。",
           "咱们宁愿多花点儿钱，也要买个质量好的。",
           "他就是这样，宁愿吃苦受累，也决不求人。"],
    say=["Điểm ngữ pháp thứ hai là phó từ 宁愿. Chú ý cách đọc: nìngyuàn, âm tiết đầu thanh bốn.",
         F(0, "宁愿 dùng trong câu phức chỉ quan hệ lựa chọn. Người nói đã so sánh lợi và hại của hai cách làm, rồi chọn lấy một cách. Tiếng Việt dịch là thà rằng, thà."),
         F(1, "Có hai mẫu thường gặp. Mẫu thứ nhất: 宁愿……也要……, chấp nhận điều thiệt thòi để đạt được điều mình muốn. Mẫu thứ hai: 宁愿……也不……, chấp nhận điều thiệt thòi chứ nhất quyết không làm điều kia."),
         F(2, "Ngoài 宁愿, các bạn còn có thể nói 宁可 hoặc 宁肯, nghĩa giống nhau."),
         F(3, "Ví dụ một, lấy từ bài khóa: 我心中难免不解：古人是怎么想的，愣是编出个拔苗助长的故事来？要是我，宁愿用别的比喻。 Nếu là tôi, tôi thà dùng một phép so sánh khác."),
         F(4, "Ví dụ hai: 咱们宁愿多花点儿钱，也要买个质量好的。 Chúng ta thà tốn thêm chút tiền, cũng phải mua cái chất lượng tốt. Đây là mẫu 宁愿……也要……."),
         F(5, "Ví dụ ba: 他就是这样，宁愿吃苦受累，也决不求人。 Anh ấy là như vậy đấy, thà chịu khổ chịu cực, chứ nhất quyết không cầu xin ai. Đây là mẫu 宁愿……也不…….")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: dùng 宁愿 trả lời câu hỏi", reveal=True, size=34,
    items=["(1) 一个房子条件不错，但到学校需要一个小时；另一个房子条件差些，但五分钟就能走到学校。你选择哪个房子？",
           "Đáp án: 我宁愿住条件差些的房子，也不想每天花两个小时在路上。",
           "(2) 坐公共汽车比较舒服，但是路上会堵车；坐地铁很挤，但是时间有保证。你怎么去？",
           "Đáp án: 我宁愿挤地铁，也不想因为堵车而迟到。",
           "(3) 少睡会儿觉，把作文写完；该睡觉就睡觉，作文不写了。你会怎样？",
           "Đáp án: 我宁愿少睡会儿觉，也要把作文写完。"],
    say=[F(0, "Luyện tập: dùng câu có 宁愿 để trả lời. Câu một: 一个房子条件不错，但到学校需要一个小时；另一个房子条件差些，但五分钟就能走到学校。你选择哪个房子？ Một căn nhà điều kiện tốt nhưng đến trường mất một tiếng; căn kia điều kiện kém hơn nhưng đi bộ năm phút là tới. Bạn chọn căn nào? Các bạn tạm dừng và trả lời nhé."),
         F(1, "Đáp án gợi ý: 我宁愿住条件差些的房子，也不想每天花两个小时在路上。 Tôi thà ở căn nhà kém hơn một chút, chứ không muốn mỗi ngày mất hai tiếng trên đường. Tất nhiên các bạn có thể chọn ngược lại, miễn là dùng đúng mẫu câu."),
         F(2, "Câu hai: 坐公共汽车比较舒服，但是路上会堵车，时间没有保证；坐地铁很挤，但是时间有保证。你怎么去？ Đi xe buýt thoải mái nhưng hay tắc đường; đi tàu điện ngầm thì chật nhưng đảm bảo thời gian. Bạn đi bằng gì?"),
         F(3, "Đáp án gợi ý: 我宁愿挤地铁，也不想因为堵车而迟到。 Tôi thà chen chúc trên tàu điện ngầm, chứ không muốn bị muộn vì tắc đường."),
         F(4, "Câu ba: 少睡会儿觉，把作文写完；该睡觉就睡觉，作文不写了。你会怎样？ Ngủ ít đi một chút để viết xong bài văn; hay đến giờ ngủ thì đi ngủ, không viết nữa. Bạn sẽ làm thế nào?"),
         F(5, "Đáp án gợi ý: 我宁愿少睡会儿觉，也要把作文写完。 Tôi thà ngủ ít đi một chút, cũng phải viết xong bài văn. Đây là mẫu 宁愿……也要…….")])

add("bullets", chapter="Ngữ pháp: A归A", section="Ngữ pháp 注释", title="3. A归A – A thì A, nhưng…", size=36,
    items=["Cấu trúc khẩu ngữ; A là từ ngữ đã xuất hiện (hoặc tóm ý) ở câu trước",
           "Tăng ý nhượng bộ: thừa nhận A; vế sau nêu ý đối ứng hoặc chuyển ngược lại",
           "不解归不解，我每天工作疲倦了，都要去看看那几棵丝瓜。",
           "老张心里很不满意：大家都有意见，为什么偏叫我去说？不满归不满，老张也只能去，谁让他是长辈呢！",
           "朋友之间，开玩笑归开玩笑，但千万别过了头。"],
    say=["Điểm ngữ pháp thứ ba là cấu trúc A归A.",
         F(0, "A归A là cấu trúc khẩu ngữ. A về nghĩa phải liên quan đến câu trước: thường là từ ngữ đã xuất hiện, hoặc là ý tóm tắt của câu trước. Ví dụ, trong bài khóa, 不解 đã xuất hiện ngay ở câu trên: 我心中难免不解."),
         F(1, "A归A làm tăng ý nhượng bộ: thừa nhận có A, nhưng vế sau nêu ra một ý đối ứng, hoặc chuyển ngược lại. Tiếng Việt có cách nói rất giống: A thì A, nhưng…."),
         F(2, "Ví dụ một, lấy từ bài khóa: 不解归不解，我每天工作疲倦了，都要去看看那几棵丝瓜。 Không hiểu thì không hiểu, nhưng mỗi ngày làm việc mệt, tôi đều ra ngắm mấy cây mướp."),
         F(3, "Ví dụ hai: 老张心里很不满意：大家都有意见，为什么偏叫我去说？不满归不满，老张也只能去，谁让他是长辈呢！ Ông Trương trong lòng rất bực: ai cũng có ý kiến, sao cứ bắt tôi đi nói? Bực thì bực, ông Trương cũng đành phải đi, ai bảo ông ấy là bậc bề trên chứ!"),
         F(4, "Ví dụ ba: 朋友之间，开玩笑归开玩笑，但千万别过了头。 Giữa bạn bè với nhau, đùa thì đùa, nhưng tuyệt đối đừng quá trớn.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: hoàn thành câu với A归A", reveal=True, size=36,
    items=["(1) 咱们好归好，你要是做事不公平______。",
           "Đáp án: ……你要是做事不公平，我也照样会批评你。",
           "(2) 生气归生气，你______，我还是会帮你的。",
           "Đáp án: 生气归生气，你要是真遇到了困难，我还是会帮你的。",
           "(3) 喜欢归喜欢，价格那么贵，他还是决定______。",
           "Đáp án: ……价格那么贵，他还是决定不买了。"],
    say=[F(0, "Luyện tập: hoàn thành câu. Câu một: 咱们好归好，你要是做事不公平，什么？ Chúng ta thân thì thân thật, nhưng nếu bạn làm việc không công bằng thì sao? Các bạn tạm dừng và hoàn thành câu nhé."),
         F(1, "Đáp án gợi ý: 你要是做事不公平，我也照样会批评你。 Nếu bạn làm việc không công bằng, tôi vẫn sẽ phê bình bạn như thường."),
         F(2, "Câu hai: 生气归生气，你什么，我还是会帮你的。 Giận thì giận, nhưng nếu bạn thế nào, tôi vẫn sẽ giúp bạn."),
         F(3, "Đáp án gợi ý: 你要是真遇到了困难，我还是会帮你的。 Nếu bạn thật sự gặp khó khăn, tôi vẫn sẽ giúp bạn."),
         F(4, "Câu ba: 喜欢归喜欢，价格那么贵，他还是决定，什么？ Thích thì thích, nhưng giá đắt như vậy, anh ấy vẫn quyết định thế nào?"),
         F(5, "Đáp án gợi ý: 他还是决定不买了。 Anh ấy vẫn quyết định không mua nữa. Các bạn thấy đấy, vế sau của A归A luôn đi theo hướng ngược lại với A.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 连同 – 一起", section="Phân biệt từ 词语辨析", title="Phân biệt 连同 và 一起",
    common="Giống nhau: đều có ý A và B cùng nhau. Nhưng 连同 là liên từ, 一起 là phó từ, không thể thay thế cho nhau.",
    cols=[{"head": "连同",
           "lines": ["Liên từ, nghĩa như 连、和 (cùng với, kể cả)",
                     "Thường đứng giữa hai danh từ",
                     "Đúng: 货物连同清单一并送过去。",
                     "Sai: 我跟朋友连同住在公寓里。"]},
          {"head": "一起",
           "lines": ["Phó từ (cùng nhau)",
                     "Đứng trước động từ",
                     "Đúng: 明天你把作业和考试成绩一起带给他吧。",
                     "Có thể dùng chung: A连同B一起 + động từ"]}],
    say=["Tiếp theo là phần phân biệt từ: 连同 và 一起. Hai từ này đều có thể dịch là cùng với, nên rất dễ dùng lẫn lộn.",
         "Điểm giống nhau: cả hai đều có ý A và B cùng nhau. Nhưng 连同 là liên từ, còn 一起 là phó từ, vì vậy không thể thay thế cho nhau.",
         F(0, "连同 là liên từ, nghĩa giống 连 hoặc 和, tức là cùng với, kể cả. Nó thường đứng giữa hai danh từ. Ví dụ: 货物连同清单一并送过去。 Hàng hóa cùng với bảng kê, gửi qua một lượt."),
         F(1, "一起 là phó từ, nghĩa là cùng nhau, đứng trước động từ. Ví dụ: 明天你把作业和考试成绩一起带给他吧。 Ngày mai bạn mang bài tập và điểm thi cùng đưa cho cậu ấy nhé."),
         F(0, "Vì 连同 là liên từ, nên nó không đứng trước động từ được. Câu 我跟朋友连同住在公寓里 là sai, phải nói 我跟朋友一起住在公寓里。"),
         F(1, "Hai từ còn có thể dùng chung, như trong bài khóa: 连同上面的两个大瓜一起坠落到地上。 连同 nối hai danh từ, còn 一起 đứng trước động từ 坠落."),
         "Mẹo nhớ: 连同 nối danh từ với danh từ; 一起 đi với động từ. Nếu chỗ trống đứng ngay trước động từ, hãy chọn 一起."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: chọn 连同 hoặc 一起 điền vào chỗ trống", reveal=True, size=36,
    items=["(1) 他把上衣______裤子都弄脏了。",
           "Đáp án: 连同 – nối hai danh từ 上衣 và 裤子",
           "(2) 下个星期小王去上海出差，你跟他______去吧。",
           "Đáp án: 一起 – đứng trước động từ 去",
           "(3) 我跟朋友______住在一所离学校很近的公寓里。",
           "Đáp án: 一起 – đứng trước động từ 住",
           "(4) 到期后，请把借款______利息一并还给我。",
           "Đáp án: 连同 – nối hai danh từ 借款 và 利息"],
    say=[F(0, "Bây giờ chúng ta làm thử: chọn 连同 hoặc 一起 điền vào chỗ trống. Câu một: 他把上衣，什么，裤子都弄脏了。 Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: 连同. 他把上衣连同裤子都弄脏了。 Anh ấy làm bẩn cả áo lẫn quần. 连同 nối hai danh từ 上衣 và 裤子."),
         F(2, "Câu hai: 下个星期小王去上海出差，你跟他，什么，去吧。"),
         F(3, "Đáp án: 一起. 你跟他一起去吧。 Tuần sau Tiểu Vương đi công tác Thượng Hải, bạn đi cùng cậu ấy nhé. Chỗ trống đứng trước động từ 去."),
         F(4, "Câu ba: 我跟朋友，什么，住在一所离学校很近的公寓里。"),
         F(5, "Đáp án: 一起. 我跟朋友一起住在一所离学校很近的公寓里。 Tôi ở cùng bạn trong một căn hộ rất gần trường."),
         F(6, "Câu bốn: 到期后，请把借款，什么，利息一并还给我。"),
         F(7, "Đáp án: 连同. 请把借款连同利息一并还给我。 Đến hạn, xin hãy trả tôi khoản vay cùng với tiền lãi một lượt. 一并 nghĩa là gộp lại cùng một lúc.")])

# ======================= KỸ NĂNG: MIÊU TẢ QUÁ TRÌNH BIẾN ĐỔI =======================
add("bullets", chapter="Kỹ năng: miêu tả quá trình biến đổi", section="Kỹ năng 技能", title="Miêu tả quá trình biến đổi của sự vật", size=34,
    items=["Bài khóa theo dõi cây mướp từ hạt giống đến quả chín, mỗi giai đoạn mở đầu bằng một từ ngữ chỉ thời gian",
           "## Chuỗi thời gian trong bài",
           "春天 → 没几天 → 接着 → 转眼间 → 接着",
           "又过了几天 → 再过几天 → 不久 → 没过几天 → 没几天 → 这天一早",
           "## Từ mùa xuân (春天) đến mùa thu (秋阳): mạch kể rõ ràng, người đọc thấy được tốc độ lớn lên của cây"],
    say=["Bây giờ chúng ta sang phần kỹ năng. Quyển này không có mục tu từ riêng, nên thầy chọn một kỹ năng rất thực dụng từ bài tập bốn của sách: miêu tả quá trình biến đổi của một sự vật, ở đây là quá trình lớn lên của một loài cây.",
         F(0, "Các bạn để ý, cả bài khóa theo dõi cây mướp từ lúc gieo hạt cho đến khi ra quả. Mỗi giai đoạn mới đều được mở đầu bằng một từ ngữ chỉ thời gian."),
         F(1, "Chúng ta cùng tìm chuỗi thời gian trong bài."),
         F(2, "春天, mùa xuân, gieo hạt. 没几天, chẳng mấy ngày, cây nhú lên. 接着, tiếp đó, cây lớn từng giờ. 转眼间, chớp mắt, dây đã leo lên tường. Rồi lại 接着, leo từ tầng một lên tầng ba."),
         F(3, "又过了几天, lại qua mấy ngày, ra hoa. 再过几天, vài ngày nữa, kết quả. 不久, không lâu sau, quả lớn. 没过几天 và 没几天, chưa được mấy ngày. Cuối cùng là 这天一早, sáng sớm hôm ấy, tác giả thấy kỳ tích."),
         F(4, "Bài văn mở đầu bằng mùa xuân, kết thúc bằng 秋阳, nắng thu. Nhờ chuỗi từ chỉ thời gian ngắn gọn như 没几天，转眼间, người đọc cảm nhận được cây mướp lớn nhanh đến mức nào.")])

add("bullets", section="Kỹ năng 技能", title="Mẫu 1: 转眼间……已经……；接着……又……", size=36,
    items=["转眼间 trong chớp mắt → nhấn mạnh thời gian trôi rất nhanh",
           "已经 đã → kết quả đạt được sau khoảng thời gian ngắn",
           "接着…… tiếp đó · 又…… lại → nối tiếp từng bước phát triển",
           "丝瓜长得很快，转眼间，瓜茎已经爬上了我们这幢楼陡峭的楼墙。接着，它从一楼爬上了二楼，又从二楼爬上了三楼。",
           "这只小狗长得很快，转眼间，它已经会自己跑了。接着，它又学会了开门。"],
    say=["Mẫu thứ nhất nằm trong bài tập bốn: 转眼间……已经……；接着……又…….",
         F(0, "转眼间 là trong chớp mắt, dùng để nhấn mạnh thời gian trôi qua rất nhanh."),
         F(1, "已经 đi kèm phía sau, nêu kết quả đã đạt được chỉ sau một khoảng thời gian rất ngắn."),
         F(2, "接着 và 又 nối tiếp từng bước phát triển, bước sau cao hơn bước trước."),
         F(3, "Câu trong bài: 丝瓜长得很快，转眼间，瓜茎已经爬上了我们这幢楼陡峭的楼墙。接着，它从一楼爬上了二楼，又从二楼爬上了三楼。 Các bạn thấy đấy, từ tầng một lên tầng hai, rồi lên tầng ba, từng bước rất rõ ràng."),
         F(4, "Ví dụ của thầy: 这只小狗长得很快，转眼间，它已经会自己跑了。接着，它又学会了开门。 Chú chó con này lớn rất nhanh, chớp mắt đã biết tự chạy. Tiếp đó, nó lại học được cả cách mở cửa.")])

add("bullets", section="Kỹ năng 技能", title="Mẫu 2: 只有……，却能……，使得……", size=36,
    items=["只有…… chỉ có (nhỏ bé, ít ỏi)",
           "却能…… vậy mà lại có thể (làm được việc lớn, ngoài dự đoán)",
           "使得…… khiến cho (kết quả tốt)",
           "瓜茎只有细绳一般粗，却能输送足够的水分和养料，使得瓜茎挺拔，叶子茂盛。",
           "这家小店只有两个服务员，却能把客人照顾得很好，使得店里的生意越来越好。"],
    say=["Mẫu thứ hai cũng trong bài tập bốn: 只有……，却能……，使得……. Mẫu này dùng để khen một sự vật nhỏ bé nhưng làm được việc lớn.",
         F(0, "只有, chỉ có, nêu ra sự nhỏ bé, ít ỏi."),
         F(1, "却能, vậy mà lại có thể, nêu việc lớn làm được, trái với dự đoán. Chữ 却 tạo ra sự tương phản."),
         F(2, "使得, khiến cho, nêu kết quả tốt đẹp sau cùng."),
         F(3, "Câu trong bài: 瓜茎只有细绳一般粗，却能输送足够的水分和养料，使得瓜茎挺拔，叶子茂盛。 Dây mướp chỉ to bằng sợi dây mảnh, vậy mà vận chuyển được đủ nước và chất dinh dưỡng, khiến dây vươn thẳng, lá xanh tốt."),
         F(4, "Ví dụ của thầy: 这家小店只有两个服务员，却能把客人照顾得很好，使得店里的生意越来越好。 Quán nhỏ này chỉ có hai nhân viên, vậy mà chăm sóc khách rất chu đáo, khiến việc buôn bán ngày càng tốt.")])

add("bullets", section="Kỹ năng 技能", title="Làm cho đoạn tả sinh động: so sánh và nhân hóa", size=34,
    items=["## So sánh: A一般 + tính từ · 如A一般 + tính từ",
           "细绳一般粗 · 小姑娘的辫子一般粗细 · 如小孩胳膊一般粗",
           "## Nhân hóa (拟人): tả cây như tả người",
           "很有节制 · 舒舒服服地躺在了那家的窗台上 · 含笑面对秋阳",
           "丝瓜有思想，能考虑问题，而且还有行动",
           "## Tác dụng: hình ảnh cụ thể, cây mướp trở nên gần gũi, có “tính cách”"],
    say=["Ngoài chuỗi thời gian, tác giả còn dùng hai thủ pháp để đoạn tả thật sinh động.",
         F(0, "Thủ pháp thứ nhất là so sánh, với mẫu A一般 cộng tính từ, hoặc 如A一般 cộng tính từ. 一般 ở đây nghĩa là giống như."),
         F(1, "细绳一般粗, to như sợi dây mảnh. 小姑娘的辫子一般粗细, to bằng bím tóc cô bé. 如小孩胳膊一般粗, to như cánh tay trẻ con. Chỉ qua ba hình ảnh, người đọc thấy ngay quả mướp lớn nhanh thế nào."),
         F(2, "Thủ pháp thứ hai là nhân hóa, tiếng Trung gọi là 拟人, tức là tả cây cối như tả con người."),
         F(3, "Quả mướp 很有节制, rất biết chừng mực; hai quả mướp 舒舒服服地躺在了窗台上, nằm thoải mái trên bậu cửa sổ; và cây mướp 含笑面对秋阳, mỉm cười đón nắng thu."),
         F(4, "Đỉnh cao là câu 丝瓜有思想，能考虑问题，而且还有行动, cây mướp có tư tưởng, biết suy nghĩ, lại biết hành động."),
         F(5, "Nhờ hai thủ pháp này, cây mướp không còn là một cái cây bình thường, mà như một người bạn có tính cách riêng. Khi viết bài văn tả cây, các bạn hãy thử dùng chúng nhé.")])

add("bullets", section="Kỹ năng 技能", title="Bài tập 4 (2): Đọc đoạn văn, mô phỏng đặt câu", reveal=True, size=34,
    items=["孩子长得很快，转眼间，他已经______，接着，他又______。虽然他只有______，却能______，使得______。",
           "Đáp án: ……转眼间，他已经上小学了，接着，他又学会了游泳和骑自行车。虽然他只有七岁，却能自己照顾自己，使得爸爸妈妈省了不少心。"],
    say=[F(0, "Bây giờ chúng ta làm bài tập bốn, phần hai. Đề bài cho khung: 孩子长得很快，转眼间，他已经什么，接着，他又什么。虽然他只有什么，却能什么，使得什么。 Đứa trẻ lớn rất nhanh, chớp mắt đã…, tiếp đó lại…. Tuy chỉ mới…, vậy mà đã có thể…, khiến cho…. Các bạn tạm dừng và thử viết nhé."),
         F(1, "Đáp án gợi ý: 孩子长得很快，转眼间，他已经上小学了，接着，他又学会了游泳和骑自行车。虽然他只有七岁，却能自己照顾自己，使得爸爸妈妈省了不少心。 Đứa trẻ lớn rất nhanh, chớp mắt đã vào tiểu học, tiếp đó lại biết bơi và đi xe đạp. Tuy mới bảy tuổi, cháu đã biết tự chăm sóc bản thân, khiến bố mẹ đỡ lo đi nhiều. 省心 nghĩa là đỡ lo, đỡ phải bận tâm.")])

add("bullets", section="Kỹ năng 技能", title="Luyện tập: điền 转眼间 · 接着 · 却 · 使得", reveal=True, size=36,
    items=["春天我在阳台上种了一盆小花。(1)___，它已经长出了好几片叶子。(2)___，它又开出了几朵小红花。这盆花虽然很小，(3)___给我带来了很多快乐，(4)___我每天的心情都很好。",
           "Đáp án: (1) 转眼间 · (2) 接着 · (3) 却 · (4) 使得"],
    say=[F(0, "Luyện tập thêm: điền 转眼间，接着，却，使得 vào chỗ trống. 春天我在阳台上种了一盆小花。什么，它已经长出了好几片叶子。什么，它又开出了几朵小红花。这盆花虽然很小，什么给我带来了很多快乐，什么我每天的心情都很好。 Các bạn tạm dừng và điền thử nhé."),
         F(1, "Đáp án: 春天我在阳台上种了一盆小花。转眼间，它已经长出了好几片叶子。接着，它又开出了几朵小红花。这盆花虽然很小，却给我带来了很多快乐，使得我每天的心情都很好。 Mùa xuân tôi trồng một chậu hoa nhỏ ngoài ban công. Chớp mắt, nó đã mọc mấy chiếc lá. Tiếp đó, nó lại nở mấy bông hoa đỏ nhỏ. Chậu hoa tuy nhỏ, nhưng lại mang đến cho tôi rất nhiều niềm vui, khiến ngày nào tâm trạng tôi cũng thật tốt."),
         "Các bạn để ý: 转眼间 đi với 已经, 接着 đi với 又, 虽然 đi với 却. Nhớ theo từng cặp như vậy, các bạn sẽ dùng rất tự nhiên."])

# ======================= MỞ RỘNG: TỪ GẦN NGHĨA =======================
add("bullets", chapter="Mở rộng: từ gần nghĩa", section="Mở rộng 扩展", title="Mở rộng 扩展: các cặp từ gần nghĩa", size=36,
    items=["简化 – 精简 đơn giản hóa, tinh giản · 觉悟 – 觉醒 giác ngộ, thức tỉnh",
           "结局 – 结果 kết cục, kết quả · 救济 – 救助 cứu tế, cứu trợ",
           "局面 – 局势 cục diện, tình thế · 廉洁 – 清廉 liêm khiết, thanh liêm",
           "牵连 – 牵扯 liên lụy, dính líu · 废除 – 作废 bãi bỏ, mất hiệu lực",
           "让步 – 妥协 nhượng bộ, thỏa hiệp · 擅自 – 私自 tự ý, tự tiện",
           "生效 – 有效 có hiệu lực · 盛情 – 热情 thịnh tình, nhiệt tình",
           "瓦解 – 分解 tan rã, phân giải · 慰问 – 安慰 thăm hỏi, an ủi",
           "支援 – 援助 chi viện, viện trợ · 资助 – 赞助 giúp đỡ tiền bạc, tài trợ"],
    say=["Phần mở rộng của sách giới thiệu mười sáu cặp từ gần nghĩa. Thầy đọc qua để các bạn làm quen; khi gặp trong bài đọc, các bạn sẽ nhận ra ngay.",
         F(0, "简化，精简: đơn giản hóa, tinh giản. 觉悟，觉醒: giác ngộ, thức tỉnh."),
         F(1, "结局，结果: kết cục, kết quả. 救济，救助: cứu tế, cứu trợ."),
         F(2, "局面，局势: cục diện, tình thế. 廉洁，清廉: liêm khiết, thanh liêm."),
         F(3, "牵连，牵扯: liên lụy, dính líu. 废除，作废: bãi bỏ, mất hiệu lực."),
         F(4, "让步，妥协: nhượng bộ, thỏa hiệp. 擅自，私自: tự ý, tự tiện làm mà không xin phép."),
         F(5, "生效，有效: có hiệu lực. 生效 nhấn mạnh thời điểm bắt đầu có hiệu lực. 盛情，热情: thịnh tình, nhiệt tình."),
         F(6, "瓦解，分解: tan rã, phân giải. 慰问，安慰: thăm hỏi, an ủi."),
         F(7, "支援，援助: chi viện, viện trợ. 资助，赞助: giúp đỡ về tiền bạc, tài trợ. Các cặp từ này nghĩa gần nhau nhưng cách kết hợp có khác biệt, các bạn hãy tra từ điển và đặt câu với từng từ nhé.")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chọn từ gần nghĩa thích hợp", reveal=True, size=36,
    items=["(1) 这份合同从签字之日起______。（生效 / 有效）",
           "Đáp án: 生效 – nhấn mạnh thời điểm bắt đầu có hiệu lực",
           "(2) 地震发生后，全国各地纷纷______灾区。（支援 / 慰问）",
           "Đáp án: 支援 – chi viện sức người, sức của",
           "(3) 经过多次谈判，双方都做出了一定的______。（让步 / 结局）",
           "Đáp án: 让步 – nhượng bộ",
           "(4) 这次比赛由一家大公司______。（赞助 / 救济）",
           "Đáp án: 赞助 – tài trợ cho hoạt động, sự kiện"],
    say=[F(0, "Luyện tập: chọn từ thích hợp. Câu một: 这份合同从签字之日起，什么。 Hợp đồng này có hiệu lực kể từ ngày ký. Chọn 生效 hay 有效?"),
         F(1, "Đáp án: 生效. Khi nói từ một thời điểm bắt đầu có hiệu lực, ta dùng 生效. Còn 有效 chỉ trạng thái đang có hiệu lực, như 这张票三天内有效."),
         F(2, "Câu hai: 地震发生后，全国各地纷纷，什么，灾区。 Sau động đất, khắp cả nước lần lượt chi viện cho vùng thiên tai. Chọn 支援 hay 慰问?"),
         F(3, "Đáp án: 支援, chi viện sức người sức của. 慰问 là thăm hỏi, động viên, ý nhẹ hơn."),
         F(4, "Câu ba: 经过多次谈判，双方都做出了一定的，什么。 Sau nhiều lần đàm phán, hai bên đều có những nhượng bộ nhất định."),
         F(5, "Đáp án: 让步. Cụm cố định là 做出让步, đưa ra nhượng bộ."),
         F(6, "Câu bốn: 这次比赛由一家大公司，什么。 Cuộc thi lần này do một công ty lớn tài trợ."),
         F(7, "Đáp án: 赞助. 赞助 là tài trợ cho hoạt động, sự kiện; còn 救济 là cứu tế người gặp khó khăn.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ có dấu chấm", size=40,
    items=["负担 (担) → 承担 · 担任 · 担当 · 分担",
           "随即 (即) → 立即 · 当即 · 即将 · 即刻",
           "照耀 (照) → 照射 · 照明 · 照亮 · 关照",
           "疲倦 (疲) → 疲劳 · 疲惫 · 疲乏 · 疲软",
           "协调 (调) → 调整 · 调节 · 空调 · 调和"],
    say=["Phần luyện tập. Bài tập một: mô phỏng ví dụ, viết thêm các từ có chứa chữ được đánh dấu chấm.",
         F(0, "Ví dụ mẫu: 负担, chữ được đánh dấu là chữ thứ hai, nghĩa là gánh. Ta có 承担，担任，担当，分担. Tức là gánh vác, đảm nhiệm, đảm đương, và chia sẻ gánh nặng."),
         F(1, "随即, chữ được đánh dấu là chữ thứ hai, nghĩa là ngay, liền. Ta có 立即，当即，即将，即刻. Tức là lập tức, ngay lúc đó, sắp sửa, và tức khắc."),
         F(2, "照耀, chữ được đánh dấu là chữ đầu, nghĩa là chiếu. Ta có 照射，照明，照亮，关照. Tức là chiếu xạ, chiếu sáng, soi sáng, và quan tâm chăm sóc."),
         F(3, "疲倦, chữ được đánh dấu là chữ đầu, nghĩa là mệt. Ta có 疲劳，疲惫，疲乏，疲软. Tức là mệt mỏi, mệt rã rời, mệt lả, và yếu ớt."),
         F(4, "协调, chữ được đánh dấu là chữ thứ hai, ở đây đọc tiáo, nghĩa là điều chỉnh cho hài hòa. Ta có 调整，调节，空调，调和. Tức là điều chỉnh, điều tiết, máy điều hòa, và điều hòa cho hài hòa.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (1)", reveal=True, size=36,
    items=["(1) 时间紧迫，你们先走，然后我马上动身。（随即）",
           "Đáp án: 时间紧迫，你们先走，我随即动身。",
           "(2) 这种产品一再降价，可就是卖不动，让人觉得不可思议。（愣）",
           "Đáp án: 这种产品一再降价，可愣是卖不动，让人觉得不可思议。",
           "(3) 让我嫁给他，还不如让我一辈子不结婚。（宁愿）",
           "Đáp án: 我宁愿一辈子不结婚，也不嫁给他。"],
    say=[F(0, "Bài tập hai: dùng từ cho sẵn để viết lại câu. Câu một, dùng 随即: 时间紧迫，你们先走，然后我马上动身。 Thời gian gấp rút, các bạn đi trước, sau đó tôi sẽ lên đường ngay. Các bạn tạm dừng và thử viết lại nhé."),
         F(1, "Đáp án: 时间紧迫，你们先走，我随即动身。 Thay 然后我马上 bằng 我随即: các bạn đi trước, tôi theo ngay sau."),
         F(2, "Câu hai, dùng 愣: 这种产品一再降价，可就是卖不动，让人觉得不可思议。 Sản phẩm này hạ giá hết lần này đến lần khác, nhưng vẫn không bán được, thật khó hiểu."),
         F(3, "Đáp án: 这种产品一再降价，可愣是卖不动。 Thay 就是 bằng 愣是, nhấn mạnh kết quả cứ trái với mong đợi."),
         F(4, "Câu ba, dùng 宁愿: 让我嫁给他，还不如让我一辈子不结婚。 Bắt tôi lấy anh ta, chẳng thà để tôi cả đời không lấy chồng."),
         F(5, "Đáp án: 我宁愿一辈子不结婚，也不嫁给他。 Tôi thà cả đời không lấy chồng, chứ không lấy anh ta. Đây là mẫu 宁愿……也不…….")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (2)", reveal=True, size=36,
    items=["(4) 我敢说这件事肯定是他干的，因为别人没有这个机会。（断定）",
           "Đáp án: 我断定这件事是他干的，因为别人没有这个机会。",
           "(5) 妈妈把午饭和课本一起放进我的书包里了。（连同）",
           "Đáp án: 妈妈把午饭连同课本一起放进我的书包里了。",
           "(6) 希望你像以前一样继续关心支持我们。（一如既往）",
           "Đáp án: 希望你一如既往地关心支持我们。"],
    say=[F(0, "Câu bốn, dùng 断定: 我敢说这件事肯定是他干的，因为别人没有这个机会。 Tôi dám nói việc này chắc chắn là do anh ta làm, vì người khác không có cơ hội đó."),
         F(1, "Đáp án: 我断定这件事是他干的。 Thay 敢说……肯定 bằng 断定, tôi khẳng định chắc chắn."),
         F(2, "Câu năm, dùng 连同: 妈妈把午饭和课本一起放进我的书包里了。 Mẹ bỏ bữa trưa và sách giáo khoa vào cặp cho tôi."),
         F(3, "Đáp án: 妈妈把午饭连同课本一起放进我的书包里了。 Thay 和 bằng 连同, giữ lại 一起 trước động từ, đúng như mẫu trong bài khóa."),
         F(4, "Câu sáu, dùng 一如既往: 希望你像以前一样继续关心支持我们。 Mong bạn tiếp tục quan tâm, ủng hộ chúng tôi như trước đây."),
         F(5, "Đáp án: 希望你一如既往地关心支持我们。 一如既往 thay cho cả cụm 像以前一样继续, và đứng trước động từ với trợ từ 地.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (1)", reveal=True, size=36,
    items=["## Từ cho sẵn: 土壤 · 照耀 · 花瓣 · 粒 · 滋润",
           "找个空闲时间，找一块空地，种上几___种子。只要有肥沃的___，水的___，阳光的___，很快就能发芽开花了。红色的___点缀在绿叶之间，让人看了心情愉快。",
           "Đáp án: 粒 · 土壤 · 滋润 · 照耀 · 花瓣"],
    say=[F(0, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn một có năm từ: 土壤，照耀，花瓣，粒，滋润."),
         F(1, "找个空闲时间，找一块空地，种上几什么种子。只要有肥沃的什么，水的什么，阳光的什么，很快就能发芽开花了。红色的什么点缀在绿叶之间，让人看了心情愉快。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 种上几粒种子，肥沃的土壤，水的滋润，阳光的照耀，红色的花瓣。 Tìm lúc rảnh, tìm một khoảnh đất trống, gieo mấy hạt giống. Chỉ cần có đất màu mỡ, có nước tưới nhuần, có nắng chiếu rọi, là sẽ nhanh chóng nảy mầm ra hoa. Những cánh hoa đỏ điểm xuyết giữa lá xanh, khiến người ngắm thấy vui vẻ. Đoạn văn này dùng lại đúng các cụm từ trong bài khóa đấy.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (2)", reveal=True, size=34,
    items=["## Từ cho sẵn: 断定 · 负担 · 与日俱增 · 惊讶 · 疲倦",
           "这个孩子已经连续十几天没来上课了，我的担心___，___他一定是出什么事了。放学后，我来到男孩儿的家，看到了满脸___的妈妈，她刚看到我时，很___，随即抱歉地说：“最近孩子的父亲因为交通事故去世了，由于___不起学费，孩子只好退学去打工。”",
           "Đáp án: 与日俱增 · 断定 · 疲倦 · 惊讶 · 负担"],
    say=[F(0, "Đoạn hai có năm từ: 断定，负担，与日俱增，惊讶，疲倦."),
         F(1, "这个孩子已经连续十几天没来上课了，我的担心什么，什么他一定是出什么事了。放学后，我来到男孩儿的家，看到了满脸什么的妈妈，她刚看到我时，很什么，随即抱歉地说：最近孩子的父亲因为交通事故去世了，由于什么不起学费，孩子只好退学去打工。 Các bạn điền thử nhé."),
         F(2, "Đáp án: 我的担心与日俱增，断定他一定是出什么事了，满脸疲倦的妈妈，很惊讶，负担不起学费。"),
         F(2, "Dịch nghĩa: Cậu bé này đã liên tục mười mấy ngày không đến lớp, nỗi lo của tôi ngày một lớn, tôi khẳng định là cậu ấy đã gặp chuyện gì rồi. Tan học, tôi đến nhà cậu bé, gặp người mẹ với vẻ mặt mệt mỏi. Vừa thấy tôi, bà rất ngạc nhiên, rồi ngay sau đó áy náy nói: Gần đây bố cháu mất vì tai nạn giao thông, vì không gánh nổi học phí, cháu đành phải nghỉ học đi làm thuê. Nghe tin này, lòng tôi nặng trĩu, thật mong mọi người đều có thể chìa bàn tay ấm áp giúp cậu bé vượt qua khó khăn.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 4 (1): Đọc đoạn văn, mô phỏng đặt câu", reveal=True, size=34,
    items=["我心中难免不解：古人是怎么想的，愣是编出个拔苗助长的故事来？要是我，宁愿用别的比喻。不解归不解，我每天工作疲倦了，都要去看看那几棵丝瓜。",
           "我心中难免生气：妈妈是怎么想的，愣是不让我______，要是我，宁愿______。生气归生气，我还是______。",
           "Đáp án: ……愣是不让我养小狗，要是我，宁愿少买几件衣服，也要让孩子养一只小狗。生气归生气，我还是听了妈妈的话。"],
    say=[F(0, "Bài tập bốn, phần một: đọc đoạn văn rồi mô phỏng đặt câu. Đoạn mẫu: 我心中难免不解：古人是怎么想的，愣是编出个拔苗助长的故事来？要是我，宁愿用别的比喻。不解归不解，我每天工作疲倦了，都要去看看那几棵丝瓜。 Đoạn này dùng cả ba từ 愣是，宁愿, và cấu trúc A归A."),
         F(1, "Khung câu: 我心中难免生气：妈妈是怎么想的，愣是不让我什么，要是我，宁愿什么。生气归生气，我还是什么。 Trong lòng tôi khó tránh khỏi bực bội: mẹ nghĩ thế nào mà cứ nhất định không cho tôi…, nếu là tôi, tôi thà…. Bực thì bực, nhưng tôi vẫn…. Các bạn tạm dừng và thử viết nhé."),
         F(2, "Đáp án gợi ý: 妈妈是怎么想的，愣是不让我养小狗，要是我，宁愿少买几件衣服，也要让孩子养一只小狗。生气归生气，我还是听了妈妈的话。 Mẹ nghĩ thế nào mà cứ nhất định không cho tôi nuôi chó, nếu là tôi, tôi thà mua bớt vài bộ quần áo, cũng phải cho con nuôi một chú chó. Bực thì bực, nhưng tôi vẫn nghe lời mẹ.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 18", size=34,
    items=["Từ vựng trọng tâm: 随即 · 宁愿 · 愣 · 拔苗助长 · 朝气蓬勃 · 点缀 · 分量 · 与日俱增 · 断定 · 连同 · 不可思议 · 一如既往",
           "Ngữ pháp: 随即 (ngay sau đó) · 宁愿……也要/也不…… (thà rằng) · A归A (A thì A, nhưng…)",
           "Phân biệt: 连同 (liên từ, nối danh từ) ≠ 一起 (phó từ, trước động từ)",
           "Kỹ năng: miêu tả quá trình biến đổi – chuỗi thời gian, 转眼间……已经……, 只有……却能……使得……, so sánh và nhân hóa",
           "## Bài tập về nhà (运用)",
           "Viết bài văn «我养过的……» (ít nhất 400 chữ): môi trường, quá trình sinh trưởng, cảm nhận"],
    say=["Chúng ta cùng tổng kết bài mười tám.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 随即，宁愿，愣，拔苗助长，朝气蓬勃，点缀，分量，与日俱增，断定，连同，不可思议，一如既往. Và đừng quên những từ dễ nhầm như 朝气蓬勃，沉重，断定，徘徊."),
         F(1, "Về ngữ pháp: 随即 biểu thị việc thứ hai xảy ra ngay sau việc thứ nhất. 宁愿 dùng khi đã so sánh lợi hại rồi chọn một cách, với hai mẫu 宁愿……也要…… và 宁愿……也不……. Còn A归A thừa nhận A, rồi chuyển sang ý ngược lại."),
         F(2, "Về phân biệt từ: 连同 là liên từ, nối hai danh từ; 一起 là phó từ, đứng trước động từ. Hai từ có thể dùng chung: A连同B一起 cộng động từ."),
         F(3, "Về kỹ năng: khi miêu tả quá trình biến đổi, hãy dùng chuỗi từ chỉ thời gian, các mẫu 转眼间……已经……，接着……又……, 只有……却能……使得……, cùng với so sánh và nhân hóa."),
         F(5, "Bài tập về nhà, theo phần vận dụng của sách: bạn đã từng trồng hoa hay một loài cây nào chưa? Hãy dựa vào trải nghiệm của mình, miêu tả quá trình lớn lên của một loài cây: môi trường sinh trưởng, quá trình gieo hạt, nảy mầm, ra hoa, kết quả, và cảm nhận hay điều cây cối gợi cho bạn. Đề bài là 我养过的……, viết ít nhất bốn trăm chữ. Nhớ thử dùng 随即，宁愿，A归A, và các mẫu câu trong phần kỹ năng nhé."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Hy vọng sau bài học này, các bạn sẽ dành nhiều thời gian hơn để quan sát cây cỏ quanh mình, biết đâu cũng phát hiện ra những điều thần kỳ. Hẹn gặp lại các bạn ở bài mười chín: 无阳光的深海世界, Thế giới biển sâu không ánh mặt trời. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Thượng) – Bài 18: 神奇的丝瓜 (Quả mướp thần kỳ)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"越长越长": "越涨越常",    # yuè zhǎng yuè cháng
                    "长得": "涨得",            # zhǎng de
                    "长出": "涨出",            # zhǎngchū
                    "长到": "涨到",            # zhǎng dào
                    "不长了": "不涨了",        # bù zhǎng le
                    "助长": "助涨",            # zhùzhǎng
                    "长辈": "涨辈",            # zhǎngbèi
                    "种上": "众上",            # zhòngshang
                    "种了": "众了",            # zhòng le
                    "种下": "众下",            # zhòngxià
                    "空地": "控地",            # kòngdì
                    "空闲": "控闲",            # kòngxián
                    "宁愿": "佞愿",            # nìngyuàn
                    "宁可": "佞可",            # nìngkě
                    "宁肯": "佞肯",            # nìngkěn
                    "幢": "壮",                # zhuàng
                    "朝气": "招气",            # zhāoqì
                    "协调": "协条",            # xiétiáo
                    "调整": "条整",            # tiáozhěng
                    "调节": "条节",            # tiáojié
                    "分量": "份亮",            # fènliàng
                    "水分": "水份",            # shuǐfèn
                    "呵": "喝",                # hē
                    "落下": "洛下",            # luòxià
                    "落了": "洛了",            # luò le
                    "禁不住": "今不住",        # jīnbuzhù
                    "差些": "岔些",            # chà xiē
                    "出差": "出拆",            # chūchāi
                    "会儿觉": "会儿叫",        # huìr jiào
                    "受累": "受泪",            # shòulèi
                    "还给": "环给",            # huán gěi
                    "他干的": "他赣的",        # gàn
                    "转为": "转维"},           # zhuǎnwéi
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai18.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
