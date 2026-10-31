#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Thượng) – Bài 9 «不用手机的日子». Chạy để sinh bai09.json."""
import json
import os

TAG = "HSK 6 (Thượng) · Bài 9 · 不用手机的日子"
slides = []


def add(type_, chapter=None, section="", **kw):
    s = {"type": type_, "section": section, **kw}
    if chapter:
        s["chapter"] = chapter
    slides.append(s)


def F(i, t, **kw):
    return {"t": t, "f": i, **kw}


def Q(s):
    """Lời đọc tiếng Trung: bỏ dấu ngoặc kép."""
    return s.replace("“", "").replace("”", "")


# ======================= MỞ ĐẦU =======================
add("title", chapter="Mở đầu",
    top="Giáo trình chuẩn HSK 6 – Quyển Thượng",
    zh="不用手机的日子", py="Bú yòng shǒujī de rìzi",
    vi="Bài 9: Một ngày không sử dụng điện thoại di động",
    sub="Bài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Thượng.",
         "Hôm nay chúng ta học bài chín: 不用手机的日子。 Nghĩa là: Những ngày không dùng điện thoại di động.",
         "Đây là bài mở đầu của Chủ đề ba, 多彩社会, Xã hội nhiều màu sắc. Bài khóa là lời kể rất hài hước của một nhân viên văn phòng nghiện điện thoại. Sau khi bị ông chủ mắng giữa cuộc họp, anh ấy quyết định thử mỗi tuần tắt điện thoại một ngày, và phát hiện ra cuộc sống không có điện thoại lại yên bình đến thế.",
         "Chắc hẳn nhiều bạn cũng sẽ thấy hình ảnh của chính mình trong câu chuyện này đấy. Chúng ta cùng bắt đầu nhé."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài khóa: một ngày tắt điện thoại của nhân vật tôi",
           "Nắm vững 47 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: tính từ trạng thái 通红、雪白 · mẫu câu 说A就A · ……得要命",
           "Phân biệt hai phó từ 索性 và 干脆",
           "Mở rộng: câu sai do kết hợp từ không phù hợp (搭配不当) và nghĩa của yếu tố cấu tạo từ"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa: vì sao nhân vật tôi quyết định tắt điện thoại, và một ngày không có điện thoại của anh ấy diễn ra như thế nào."),
         F(1, "Thứ hai, nắm vững bốn mươi bảy từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học ba điểm ngữ pháp: tính từ trạng thái như 通红 và 雪白; mẫu câu nói A là A, ví dụ 说干就干; và cấu trúc chỉ mức độ cực điểm, ví dụ 空虚得要命."),
         F(3, "Thứ tư, phân biệt hai phó từ rất dễ nhầm: 索性 và 干脆."),
         F(4, "Thứ năm, phần mở rộng: nhận biết câu sai do kết hợp từ không phù hợp, tiếng Trung gọi là 搭配不当, và tìm hiểu nghĩa của từng yếu tố cấu tạo nên một từ."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Câu hỏi khởi động: Điện thoại dùng để làm gì?", size=40,
    items=["你经常玩儿手机吗？对你来说，手机有什么用途？",
           "打电话 – gọi điện · 上网看新闻 – lên mạng đọc tin tức",
           "拍照 – chụp ảnh · 看时间 – xem giờ",
           "听音乐 – nghe nhạc · 玩儿游戏 – chơi trò chơi",
           "补充 – bổ sung: ……"],
    say=["Chúng ta bắt đầu bằng phần khởi động. Câu hỏi đầu tiên chắc chắn ai cũng trả lời được.",
         F(0, "你经常玩儿手机吗？对你来说，手机有什么用途？ Bạn có thường dùng điện thoại không? Đối với bạn, điện thoại có những công dụng gì? Sách yêu cầu các bạn khoanh vào các lựa chọn bên dưới; nếu còn công dụng khác thì viết thêm vào dòng kẻ."),
         F(1, "打电话。 Gọi điện thoại. 上网看新闻。 Lên mạng đọc tin tức."),
         F(2, "拍照。 Chụp ảnh. 看时间。 Xem giờ."),
         F(3, "听音乐。 Nghe nhạc. 玩儿游戏。 Chơi trò chơi."),
         F(4, "补充, tức là bổ sung. Các bạn có thể thêm: 发微信, gửi tin nhắn WeChat; 网上购物, mua sắm trên mạng; 导航, chỉ đường; 支付, thanh toán. Các bạn hãy tạm dừng video và tự đếm xem một ngày mình cầm điện thoại bao nhiêu lần nhé.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 好 (hǎo) và 报", size=38,
    items=["## 好 (hǎo): dễ…, …hay, …dễ chịu",
           "好玩儿 vui · 好闻 thơm · 好卖 dễ bán · 好使 dễ dùng · 好用 dễ dùng",
           "好听 hay, êm tai · 好感 thiện cảm · 好受 dễ chịu · 好过 dễ sống, dễ chịu",
           "## 报 (báo): báo cho biết, đáp lại",
           "报到 trình diện · 报道 đưa tin · 报考 đăng ký thi · 报信 báo tin · 报时 báo giờ · 报警 báo cảnh sát",
           "报告 báo cáo · 报表 bảng báo cáo · 预报 dự báo · 回报 đền đáp · 上报 báo lên trên · 通报 thông báo"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo.",
         F(0, "Nhóm thứ nhất là các từ bắt đầu bằng chữ hảo, đọc thanh ba. Đứng trước một động từ, nó tạo thành tính từ, nghĩa là làm việc đó thì dễ, hoặc làm việc đó thấy dễ chịu."),
         F(1, "好玩儿，好闻，好卖，好使，好用。 Tức là: vui, thơm, dễ bán, dễ dùng, dễ dùng. Trong bài khóa, ông chủ hỏi: 那玩意儿就那么好玩儿？ Cái thứ đó vui đến thế cơ à?"),
         F(2, "好听，好感，好受，好过。 Tức là: hay, êm tai; thiện cảm; dễ chịu; và dễ sống. Hai từ 好受 và 好过 thường dùng ở dạng phủ định: 不好受, thấy khó chịu."),
         F(3, "Nhóm thứ hai có chữ 报, Hán Việt là báo, nghĩa là báo cho biết, hoặc đáp lại."),
         F(4, "报到，报道，报考，报信，报时，报警。 Tức là: trình diện, đưa tin, đăng ký dự thi, báo tin, báo giờ, và báo cảnh sát. Từ 报警 là từ mới của bài hôm nay."),
         F(5, "报告，报表，预报，回报，上报，通报。 Tức là: báo cáo, bảng báo cáo, dự báo, đền đáp, báo cáo lên cấp trên, và thông báo.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 转 và 何", size=38,
    items=["## 转 (chuyển): chuyển sang, chuyển qua người khác",
           "转发 chuyển tiếp · 转车 đổi xe · 转告 nhắn lại · 转给 chuyển cho · 转交 chuyển giao · 转手 sang tay",
           "转卖 bán lại · 转送 tặng lại · 转运 vận chuyển tiếp · 转租 cho thuê lại · 中转 trung chuyển",
           "## 何 (hà): gì, nào, sao (văn viết)",
           "何不 sao không · 何处 nơi nào · 何种 loại nào · 何人 người nào · 何时 khi nào · 何地 nơi nào",
           "何必 hà tất · 何况 huống hồ · 如何 thế nào · 为何 vì sao"],
    say=[F(0, "Nhóm thứ ba là các từ bắt đầu bằng chữ chuyển, đọc thanh ba, nghĩa là chuyển sang chỗ khác, hoặc chuyển qua tay người khác."),
         F(1, "转发，转车，转告，转给，转交，转手。 Tức là: chuyển tiếp, đổi xe, nhắn lại, chuyển cho, chuyển giao, sang tay. Trong bài khóa có câu 要不要转发给您？ Có cần chuyển tiếp cho ông không?"),
         F(2, "转卖，转送，转运，转租，中转。 Tức là: bán lại, tặng lại, vận chuyển tiếp, cho thuê lại, và trung chuyển."),
         F(3, "Nhóm cuối cùng có chữ 何, Hán Việt là hà, như trong hà tất, nghĩa là gì, nào, sao. Đây là từ nghi vấn của tiếng Hán cổ, nay dùng nhiều trong văn viết."),
         F(4, "何不，何处，何种，何人，何时，何地。 Tức là: sao không, nơi nào, loại nào, người nào, khi nào, nơi nào. Bài khóa có câu 何不尝试一下一周关机一天？ Sao không thử mỗi tuần tắt máy một ngày?"),
         F(5, "何必，何况，如何，为何。 Tức là: hà tất, huống hồ, như thế nào, và vì sao. Các bạn thấy đấy, nhiều từ có âm Hán Việt rất quen, chỉ cần nắm nghĩa chữ gốc là đoán được nghĩa cả nhóm.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng)
V = [
    ("正经", "zhèngjing", "chính kinh", "tính từ", "đứng đắn, nghiêm chỉnh, chính đáng", "他是个正经人，从来不说假话。", "Anh ấy là người đứng đắn, chưa bao giờ nói dối.",
     "Tính từ, nghĩa là đứng đắn, nghiêm chỉnh; cũng có nghĩa chính đáng, như 正经事, việc đàng hoàng. Âm tiết thứ hai đọc nhẹ. Trong bài, 别假装正经了 là đừng giả vờ nghiêm chỉnh nữa."),
    ("玩意儿", "wányìr", "ngoạn ý nhi", "danh từ", "đồ chơi; đồ vật, cái thứ (khẩu ngữ)", "这是什么新玩意儿？", "Đây là thứ đồ mới gì vậy?",
     "Danh từ khẩu ngữ. Nghĩa gốc là đồ chơi, nghĩa rộng là cái thứ, món đồ, đôi khi mang ý coi thường. Trong bài, ông chủ gọi điện thoại là 那玩意儿, cái thứ đó."),
    ("憋", "biē", "biệt", "động từ", "kìm nén, nén, nín", "他憋着一肚子气，什么也没说。", "Anh ấy nén một bụng tức, chẳng nói gì.",
     "Động từ, nghĩa là kìm nén, nín, giữ lại không cho thoát ra, như 憋气, nín thở. Trong bài, 脸憋得通红 là mặt đỏ bừng vì cố nén."),
    ("报警", "bào jǐng", "báo cảnh", "động từ", "báo cảnh sát", "发现有人受伤，他马上报警了。", "Thấy có người bị thương, anh ấy lập tức báo cảnh sát.",
     "Động từ ly hợp, nghĩa là báo cho cảnh sát biết khi có sự cố. Ở Trung Quốc, số điện thoại báo cảnh sát là một một không."),
    ("绑架", "bǎngjià", "bảng giá", "động từ", "bắt cóc", "那个孩子被坏人绑架了。", "Đứa bé đó bị kẻ xấu bắt cóc.",
     "Động từ, nghĩa là bắt cóc người. Chú ý: âm Hán Việt trùng với từ bảng giá trong tiếng Việt, nhưng hoàn toàn không liên quan. Trong bài, 都让手机给绑架了 là nói vui: bị điện thoại bắt cóc cả rồi, tức là bị điện thoại khống chế."),
    ("受罪", "shòu zuì", "thụ tội", "động từ", "chịu khổ, bị giày vò", "这么热的天排队，真是受罪。", "Trời nóng thế này mà xếp hàng, đúng là chịu khổ.",
     "Động từ ly hợp, nghĩa là chịu khổ, bị giày vò, gặp chuyện phiền muộn. Cẩn thận: không phải là chịu tội trước pháp luật như thụ tội trong tiếng Việt. Ví dụ 受了不少罪, chịu không ít khổ."),
    ("吼", "hǒu", "hống", "động từ", "gào to, thét lên, quát", "他气得大吼了一声。", "Anh ấy tức đến mức thét lên một tiếng.",
     "Động từ, vốn chỉ tiếng gầm của thú dữ, như sư tử gầm; nói về người là gào to, quát lớn. Trong bài, 老板大吼 là ông chủ quát lớn."),
    ("智能", "zhìnéng", "trí năng", "tính từ", "thông minh (máy móc)", "现在几乎人人都有智能手机。", "Bây giờ hầu như ai cũng có điện thoại thông minh.",
     "Tính từ, chỉ máy móc có khả năng như trí tuệ con người: 智能手机, điện thoại thông minh; 人工智能, trí tuệ nhân tạo. Lưu ý: nói người thông minh thì dùng 聪明, không dùng 智能."),
    ("奴隶", "núlì", "nô lệ", "danh từ", "nô lệ", "我们不能做金钱的奴隶。", "Chúng ta không thể làm nô lệ của đồng tiền.",
     "Danh từ, nghĩa là nô lệ, giống hệt tiếng Việt. Trong bài, 手机的奴隶 là nô lệ của điện thoại."),
    ("麻木", "mámù", "ma mộc", "tính từ", "tê; thờ ơ, lãnh đạm", "坐得太久，我的腿都麻木了。", "Ngồi lâu quá, chân tôi tê cứng cả rồi.",
     "Tính từ. Nghĩa gốc là tê, mất cảm giác; nghĩa bóng là thờ ơ, chai sạn, phản ứng chậm chạp. Trong bài, 对什么都麻木了 là thờ ơ với mọi thứ."),
    ("狼吞虎咽", "lángtūn-hǔyàn", "lang thôn hổ yết", "thành ngữ", "ăn ngấu nghiến, ăn vội vàng", "他饿坏了，狼吞虎咽地吃完了饭。", "Anh ấy đói lả, ăn ngấu nghiến hết bữa cơm.",
     "Thành ngữ. Nghĩa đen là nuốt như sói, nuốt như hổ; chỉ ăn rất nhanh, rất vội, giống ăn như hổ đói của tiếng Việt."),
    ("伺候", "cìhou", "tứ hậu", "động từ", "hầu hạ, phục dịch, chăm sóc", "她在医院伺候生病的母亲。", "Cô ấy ở bệnh viện chăm sóc người mẹ bị ốm.",
     "Động từ, nghĩa là hầu hạ, chăm sóc chu đáo. Âm tiết đầu đọc thanh bốn, âm tiết sau đọc nhẹ. Trong bài, 把手机它老人家伺候得好好的 là hầu hạ ngài điện thoại thật chu đáo, cách nói rất hài hước."),
    ("眨", "zhǎ", "trát", "động từ", "nháy, chớp (mắt)", "她眨了眨眼睛，笑了。", "Cô ấy chớp chớp mắt rồi cười.",
     "Động từ, nghĩa là chớp mắt, nháy mắt. Hay gặp cụm 一眨眼, trong chớp mắt, chỉ thời gian rất ngắn."),
    ("索性", "suǒxìng", "tác tính", "phó từ", "dứt khoát, thôi thì cứ…", "雨越下越大，我们索性不走了。", "Mưa càng lúc càng to, chúng tôi dứt khoát không đi nữa.",
     "Phó từ, nghĩa là dứt khoát, thôi thì cứ làm luôn. Thường dùng khi tình hình đã như vậy, người nói quyết định làm thẳng một việc. Lát nữa chúng ta sẽ so sánh từ này với 干脆."),
    ("作息", "zuòxī", "tác tức", "động từ", "làm việc và nghỉ ngơi", "我们要养成按时作息的好习惯。", "Ta phải tập thói quen làm việc, nghỉ ngơi đúng giờ.",
     "Động từ. Chữ đầu là làm, chữ sau là nghỉ. 作息时间 là thời gian biểu, giờ giấc sinh hoạt."),
    ("着手", "zhuóshǒu", "trước thủ", "động từ", "bắt tay vào làm, bắt đầu làm", "我们下个月着手准备比赛。", "Tháng sau chúng tôi bắt tay vào chuẩn bị cho cuộc thi.",
     "Động từ, nghĩa là bắt tay vào làm, bắt đầu làm một việc. Chú ý cách đọc: âm tiết đầu đọc thanh hai."),
    ("安置", "ānzhì", "an trí", "động từ", "thu xếp, bố trí (chỗ ở, chỗ để)", "政府妥善安置了受灾群众。", "Chính phủ đã thu xếp ổn thỏa cho người dân bị thiên tai.",
     "Động từ, nghĩa là thu xếp cho người hoặc vật có chỗ ở, chỗ để thích hợp. Trong bài, 安置我的手机 là thu xếp chỗ cho điện thoại, nói như thể điện thoại là một con người."),
    ("防止", "fángzhǐ", "phòng chỉ", "động từ", "đề phòng, ngăn ngừa", "多洗手可以防止生病。", "Rửa tay thường xuyên có thể phòng bệnh.",
     "Động từ, nghĩa là đề phòng, ngăn chặn chuyện xấu xảy ra. Tân ngữ thường là điều không tốt: 防止事故，防止感冒."),
    ("薄弱", "bóruò", "bạc nhược", "tính từ", "yếu kém, yếu đuối, không vững", "他的数学基础比较薄弱。", "Nền tảng toán của cậu ấy khá yếu.",
     "Tính từ, nghĩa là yếu kém, không vững chắc. Chú ý: bạc nhược trong tiếng Việt chủ yếu nói người hèn yếu; còn 薄弱 hay dùng cho nền tảng, khâu, ý chí: 基础薄弱，意志薄弱. Âm tiết đầu ở đây đọc thanh hai."),
    ("精致", "jīngzhì", "tinh trí", "tính từ", "tinh xảo, tinh tế, đẹp", "这个小盒子做得非常精致。", "Chiếc hộp nhỏ này làm rất tinh xảo.",
     "Tính từ, nghĩa là tinh xảo, làm công phu, đẹp đẽ. Thường nói về đồ vật: 精致的盒子，精致的点心."),
    ("庄重", "zhuāngzhòng", "trang trọng", "tính từ", "trang trọng, nghiêm trang", "他庄重地接过了奖杯。", "Anh ấy trang trọng đón lấy chiếc cúp.",
     "Tính từ, nghĩa là trang trọng, nghiêm trang, giống tiếng Việt. Trong bài, 庄重地放在盒子里 là đặt điện thoại vào hộp một cách trang trọng, như đang làm lễ."),
    ("分散", "fēnsàn", "phân tán", "động từ", "phân tán, làm tản ra", "听音乐能分散注意力。", "Nghe nhạc có thể làm phân tán sự chú ý.",
     "Động từ, nghĩa là phân tán, làm tản ra. Cụm 分散注意力 là đánh lạc sự chú ý. Từ trái nghĩa là 集中, tập trung."),
    ("僵硬", "jiāngyìng", "cương ngạnh", "tính từ", "cứng đờ; cứng nhắc", "天太冷了，我的手指都僵硬了。", "Trời lạnh quá, ngón tay tôi cứng đờ cả rồi.",
     "Tính từ, nghĩa là cứng đờ, không cử động linh hoạt được; nghĩa bóng là cứng nhắc. Cẩn thận, đây là từ dễ nhầm: cương ngạnh trong tiếng Việt là bướng bỉnh, ngang ngạnh; còn 僵硬 chỉ là cứng đờ."),
    ("四肢", "sìzhī", "tứ chi", "danh từ", "tứ chi, chân tay", "他四肢发达，跑得特别快。", "Anh ấy chân tay khỏe mạnh, chạy cực nhanh.",
     "Danh từ, nghĩa là tứ chi, tức hai tay và hai chân. Trong bài, 锻炼我那僵硬的四肢 là vận động chân tay đã cứng đờ của mình."),
    ("特长", "tècháng", "đặc trường", "danh từ", "sở trường, năng khiếu", "唱歌是她的特长。", "Ca hát là sở trường của cô ấy.",
     "Danh từ, nghĩa là sở trường, điểm mạnh đặc biệt. Chú ý: âm tiết sau đọc thanh hai, nghĩa là giỏi, mạnh."),
    ("兴高采烈", "xìnggāo-cǎiliè", "hứng cao thái liệt", "thành ngữ", "phấn khởi, hớn hở", "孩子们兴高采烈地去春游了。", "Bọn trẻ hớn hở đi dã ngoại mùa xuân.",
     "Thành ngữ, nghĩa là phấn khởi, hớn hở, vui mừng hào hứng. Chú ý âm tiết đầu đọc thanh bốn. Thường dùng theo mẫu 兴高采烈地 cộng động từ."),
    ("摇滚", "yáogǔn", "dao cổn", "danh từ", "nhạc rock", "年轻人大多喜欢听摇滚。", "Giới trẻ phần lớn thích nghe nhạc rock.",
     "Danh từ, nghĩa là nhạc rock. Chữ đầu là lắc, chữ sau là lăn, dịch theo nghĩa của từ rock and roll. Trong bài, 跳起了摇滚 là nhảy theo nhạc rock."),
    ("一举两得", "yìjǔ-liǎngdé", "nhất cử lưỡng đắc", "thành ngữ", "một công đôi việc", "骑车上班既省钱又锻炼身体，一举两得。", "Đạp xe đi làm vừa đỡ tốn tiền vừa khỏe người, một công đôi việc.",
     "Thành ngữ, nghĩa là làm một việc mà được hai cái lợi, tức một công đôi việc, một mũi tên trúng hai đích."),
    ("冷落", "lěngluò", "lãnh lạc", "động từ", "đối xử lạnh nhạt, bỏ rơi", "他忙着工作，冷落了家人。", "Anh ấy mải công việc, bỏ bê gia đình.",
     "Động từ, nghĩa là đối xử lạnh nhạt, bỏ rơi. Nó còn là tính từ, nghĩa là vắng vẻ, hiu quạnh. Trong bài, 被冷落了半天儿的手机 là chiếc điện thoại bị bỏ rơi suốt nửa ngày, lại là cách nhân hóa điện thoại."),
    ("踏实", "tāshi", "đạp thực", "tính từ", "yên tâm, vững dạ; chắc chắn", "考完试，我心里踏实多了。", "Thi xong, tôi thấy yên tâm hơn nhiều.",
     "Tính từ, có hai nghĩa: yên tâm, vững dạ; và chắc chắn, thiết thực, như 他工作很踏实, anh ấy làm việc rất chắc chắn. Âm tiết đầu đọc thanh một, âm tiết sau đọc nhẹ."),
    ("空虚", "kōngxū", "không hư", "tính từ", "trống rỗng", "退休以后，他觉得生活很空虚。", "Nghỉ hưu rồi, ông ấy thấy cuộc sống rất trống rỗng.",
     "Tính từ, nghĩa là trống rỗng, thường nói về tâm trạng, tinh thần. Trong bài, 心空虚得要命 là lòng trống rỗng kinh khủng."),
    ("要命", "yào mìng", "yếu mệnh", "động từ", "chết người; cực kỳ, kinh khủng", "今天热得要命。", "Hôm nay nóng kinh khủng.",
     "Động từ. Nghĩa gốc là lấy mạng, chết người; hay dùng làm bổ ngữ chỉ mức độ cực điểm, như 热得要命, nóng chết đi được. Đây là điểm ngữ pháp thứ ba của bài."),
    ("粥", "zhōu", "chúc", "danh từ", "cháo", "生病的时候，喝碗粥最舒服。", "Lúc ốm, ăn bát cháo là dễ chịu nhất.",
     "Danh từ, nghĩa là cháo. Người Trung Quốc nói 喝粥, uống cháo, chứ không nói ăn cháo. Trong bài có 熬粥, nấu cháo nhỏ lửa trong thời gian dài."),
    ("消耗", "xiāohào", "tiêu hao", "động từ", "tiêu hao, tốn", "跑步会消耗很多体力。", "Chạy bộ tiêu hao rất nhiều thể lực.",
     "Động từ, nghĩa là tiêu hao, làm tốn dần: 消耗时间，消耗体力，消耗能源."),
    ("弥补", "míbǔ", "di bổ", "động từ", "bù đắp", "我们要想办法弥补损失。", "Chúng ta phải nghĩ cách bù đắp tổn thất.",
     "Động từ, nghĩa là bù đắp chỗ thiếu hụt: 弥补损失，弥补不足. Trong bài, 弥补心中的空虚 là bù đắp khoảng trống trong lòng."),
    ("沸腾", "fèiténg", "phí đằng", "động từ", "sôi sùng sục; sôi sục", "水已经沸腾了，可以放米了。", "Nước sôi rồi, có thể cho gạo vào.",
     "Động từ, nghĩa gốc là chất lỏng sôi sùng sục; nghĩa bóng là sôi sục, náo nhiệt, như 全场沸腾了, cả khán phòng sôi sục."),
    ("弥漫", "mímàn", "di mạn", "động từ", "tràn ngập, tỏa khắp", "早上，山里弥漫着白雾。", "Buổi sáng, sương trắng bao phủ khắp núi.",
     "Động từ, chỉ khói, sương, mùi hương lan tỏa khắp nơi. Trong bài, 屋子里渐渐弥漫着粥的香气 là trong nhà dần dần tỏa ngát hương cháo."),
    ("往常", "wǎngcháng", "vãng thường", "danh từ", "thường ngày, mọi khi", "他今天比往常来得早。", "Hôm nay anh ấy đến sớm hơn mọi khi.",
     "Danh từ, nghĩa là thường ngày, mọi khi, chỉ khoảng thời gian trước đây. Trong bài, 要在往常 là nếu như mọi khi."),
    ("侦探", "zhēntàn", "trinh thám", "danh từ", "thám tử; trinh thám", "我从小就爱看侦探小说。", "Từ nhỏ tôi đã thích đọc tiểu thuyết trinh thám.",
     "Danh từ. Ngoài nghĩa trinh thám, như 侦探小说, nó còn chỉ chính người làm nghề điều tra, tức thám tử. Tiếng Việt thì trinh thám chủ yếu chỉ thể loại truyện."),
    ("案件", "ànjiàn", "án kiện", "danh từ", "vụ án", "警察很快就破了这个案件。", "Cảnh sát nhanh chóng phá được vụ án này.",
     "Danh từ, nghĩa là vụ án. Cụm 破案 là phá án. Chú ý: không phải là kiện cáo."),
    ("突破", "tūpò", "đột phá", "động từ", "đột phá", "这项研究取得了重大突破。", "Nghiên cứu này đạt được bước đột phá quan trọng.",
     "Động từ và danh từ, nghĩa là đột phá, vượt qua giới hạn, giống tiếng Việt: 取得突破, đạt được đột phá."),
    ("震惊", "zhènjīng", "chấn kinh", "động từ", "làm kinh ngạc, chấn động", "这个消息震惊了全世界。", "Tin này làm chấn động cả thế giới.",
     "Động từ, nghĩa là làm cho kinh ngạc, bàng hoàng; mức độ mạnh hơn 吃惊 rất nhiều. Hay gặp cụm 令人震惊, khiến người ta bàng hoàng."),
    ("彩票", "cǎipiào", "thái phiếu", "danh từ", "vé số, xổ số", "他每个星期都买彩票。", "Tuần nào anh ấy cũng mua vé số.",
     "Danh từ, nghĩa là vé số. Trong bài, 彩票大奖开了没有 là giải lớn xổ số đã quay thưởng chưa."),
    ("恐怖", "kǒngbù", "khủng bố", "tính từ", "khủng khiếp, kinh hoàng", "我不敢一个人看恐怖电影。", "Tôi không dám xem phim kinh dị một mình.",
     "Tính từ, nghĩa là khủng khiếp, kinh hoàng. Cẩn thận, đây là từ dễ nhầm: khủng bố trong tiếng Việt là hành vi bạo lực chính trị; còn 恐怖 chỉ là đáng sợ. 恐怖电影 là phim kinh dị. Muốn nói khủng bố thì dùng 恐怖主义, hay 恐怖袭击 như trong bài."),
    ("袭击", "xíjī", "tập kích", "động từ", "tập kích, tấn công bất ngờ", "这个地区昨天遭到了台风袭击。", "Hôm qua khu vực này bị bão đổ bộ.",
     "Động từ, nghĩa là tập kích, tấn công bất ngờ; cũng dùng cho thiên tai: 台风袭击, bão đổ bộ."),
    ("干扰", "gānrǎo", "can nhiễu", "động từ", "quấy nhiễu, làm phiền", "他在学习，别去干扰他。", "Nó đang học, đừng làm phiền nó.",
     "Động từ, nghĩa là quấy nhiễu, làm phiền, gây nhiễu. Âm tiết đầu đọc thanh một. Trong bài, 没有手机的干扰 là không có sự quấy nhiễu của điện thoại."),
    ("安宁", "ānníng", "an ninh", "tính từ", "yên tĩnh, thanh bình", "我们希望过安宁的生活。", "Chúng tôi mong được sống cuộc sống yên bình.",
     "Tính từ, nghĩa là yên tĩnh, thanh bình, không bị quấy rầy. Cẩn thận, đây là từ dễ nhầm: an ninh trong tiếng Việt là giữ gìn trật tự, an toàn; tiếng Trung nói 安全 hoặc 治安. Còn 安宁 chỉ là yên bình."),
]

add("bullets", chapter="Từ mới (47 từ)", section="Từ mới 生词", title="Phần 1: Từ mới", size=42,
    items=["Bài 9 có 47 từ mới, chia thành 16 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 伺候 (cì) · 着手 (zhuó) · 薄弱 (bó) · 特长 (cháng) · 踏实 (tā)",
           "Từ dễ nhầm: 僵硬 · 恐怖 · 安宁 · 薄弱 · 受罪"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có bốn mươi bảy từ, thầy chia thành mười sáu nhóm nhỏ, mỗi nhóm hai hoặc ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số từ có âm đọc cần chú ý, như 伺候，着手，薄弱，特长，踏实. Thầy sẽ nhắc khi gặp."),
         F(4, "Ngoài ra, có mấy từ Hán Việt rất dễ hiểu nhầm, như 僵硬，恐怖，安宁，薄弱，受罪. Nghĩa của chúng trong tiếng Trung khác với tiếng Việt, các bạn nhớ nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

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
    ("开会时老板火了：“别假装正经了，我知道你们都在玩儿手机，那玩意儿就那么好玩儿？”",
     "Trong cuộc họp, ông chủ nổi giận: Đừng giả vờ nghiêm chỉnh nữa, tôi biết các anh chị đều đang nghịch điện thoại, cái thứ đó vui đến thế cơ à?",
     ["火了 là nổi giận, khẩu ngữ, giống tiếng Việt nổi lửa, nổi nóng. 假装 là giả vờ.",
      "那玩意儿就那么好玩儿？ là câu hỏi mang ý trách móc. 那么 nhấn mạnh mức độ: vui đến thế cơ à. Chữ hảo cộng 玩儿 thành tính từ, như ở phần khởi động."]),
    ("老板指着我：“你说说，看了什么？比我说话还有意思？”",
     "Ông chủ chỉ vào tôi: Cậu nói xem, xem cái gì thế? Còn thú vị hơn tôi nói à?",
     ["你说说 là động từ lặp lại, làm giọng nhẹ đi nhưng vẫn mang ý yêu cầu.",
      "比我说话还有意思？ là câu so sánh, có thêm 还有意思 để nhấn mạnh, ý mỉa mai: chẳng lẽ thứ cậu xem còn hay hơn tôi nói?"]),
    ("我脸憋得通红，说：“一对年轻人边开车边拿手机拍照，把桥撞坏了，没报警，先下车拍照发微信。要不要转发给您？”",
     "Mặt tôi đỏ bừng vì cố nén, tôi nói: Một đôi thanh niên vừa lái xe vừa cầm điện thoại chụp ảnh, đâm hỏng cả cây cầu, chẳng báo cảnh sát mà xuống xe chụp ảnh đăng WeChat trước đã. Có cần chuyển tiếp cho ông không ạ?",
     ["憋得通红 là mặt đỏ bừng vì cố nén. 通红 là tính từ trạng thái, đỏ hết cả, đây là điểm ngữ pháp thứ nhất.",
      "边……边…… là vừa… vừa…. 把桥撞坏了 là câu chữ 把 với bổ ngữ kết quả. 微信 là WeChat. Câu chuyện nhân vật tôi đang đọc chính là về những người nghiện điện thoại, thật trớ trêu."]),
    ("老板一摆手：“你们呀，都让手机给绑架了，这么过日子，不受罪吗？”",
     "Ông chủ xua tay: Các anh chị ấy à, đều bị điện thoại bắt cóc cả rồi, sống như thế không thấy khổ sao?",
     ["一摆手 là xua tay một cái. 让手机给绑架了 là câu bị động khẩu ngữ: 让手机 thay cho 被手机, còn 给绑架 nhấn mạnh động tác.",
      "不受罪吗？ là câu hỏi phản vấn, ý khẳng định: sống như thế thật là khổ."]),
    ("一同事举手：“老板，刚搜索了一下，离不开手机也是一种精神病。”",
     "Một đồng nghiệp giơ tay: Thưa sếp, vừa tìm trên mạng một chút, không rời được điện thoại cũng là một loại bệnh tâm thần đấy.",
     ["一同事 tức là 一个同事, lược bỏ lượng từ cho gọn. 搜索 là tìm kiếm trên mạng.",
      "离不开 là bổ ngữ khả năng, không thể rời xa. Câu này nói nửa đùa nửa thật: nghiện điện thoại cũng là bệnh."]),
    ("老板大吼：“有病就得治！”，随后黑着脸扔下一句话：“以后开会谁都不许带手机！”",
     "Ông chủ quát lớn: Có bệnh thì phải chữa! Ngay sau đó sa sầm mặt, buông lại một câu: Từ nay họp hành không ai được mang điện thoại!",
     ["就得治 nghĩa là thì phải chữa; ở đây 就得 có nghĩa là thì phải. 随后 là ngay sau đó. 黑着脸 là mặt sa sầm. 扔下一句话 là buông lại một câu.",
      "谁都不许 là đại từ nghi vấn dùng phiếm chỉ: ai cũng không được."]),
    ("老板说的没错，特别是有了智能手机，我就成了手机的奴隶，对什么都麻木了，心里只有手机：三分钟看一次新闻；十分钟发一次微信；",
     "Ông chủ nói không sai, nhất là từ khi có điện thoại thông minh, tôi đã thành nô lệ của điện thoại, thờ ơ với mọi thứ, trong lòng chỉ có điện thoại: ba phút xem tin tức một lần; mười phút gửi WeChat một lần;",
     ["对什么都麻木了 là thờ ơ với mọi thứ: 什么都 chỉ toàn bộ, không trừ cái gì.",
      "三分钟看一次 là khoảng thời gian, cộng động từ, cộng 一次, chỉ tần suất: cứ ba phút một lần. Dấu chấm phẩy dùng để liệt kê các biểu hiện nghiện điện thoại."]),
    ("吃饭前先拍照；狼吞虎咽吃完，又埋头看微信；睡觉之前先给手机充电……把手机它老人家伺候得好好的。",
     "trước khi ăn thì chụp ảnh đã; ăn ngấu nghiến xong lại cúi đầu xem WeChat; trước khi ngủ thì sạc điện cho điện thoại trước… Tôi hầu hạ ngài điện thoại thật chu đáo.",
     ["埋头 là vùi đầu, cúi đầu chăm chú. 先 nhấn mạnh việc làm trước tiên: điện thoại luôn được ưu tiên trước cả bữa ăn và giấc ngủ.",
      "它老人家 là cách gọi tôn kính dành cho người già, ở đây dùng cho điện thoại để tự giễu. 伺候得好好的 là hầu hạ chu đáo."]),
    ("有一次阿毛对我说：“我跟你说话呢，你干吗老看手机？”。我冲他眨眨眼，说：“那你也拿出手机，咱们手机上聊吧，保证不分心！”",
     "Có lần A Mao bảo tôi: Tớ đang nói chuyện với cậu đấy, sao cậu cứ nhìn điện thoại thế? Tôi nháy mắt với cậu ta, nói: Thế cậu cũng lấy điện thoại ra đi, chúng mình nói chuyện trên điện thoại, đảm bảo không phân tâm!",
     ["阿毛 là tên gọi thân mật, có tiền tố a đặt trước tên. 干吗 là làm gì, tại sao, khẩu ngữ. 老看 là cứ nhìn mãi, giống 总是看.",
      "冲他 là hướng về phía cậu ta. 咱们 là chúng mình, gồm cả người nghe. Câu trả lời ngớ ngẩn này cho thấy nhân vật tôi nghiện điện thoại đến mức nào."]),
    ("离开了手机，难道会死吗？何不尝试一下一周关机一天？说干就干，索性这礼拜就开始。",
     "Rời điện thoại thì chẳng lẽ sẽ chết sao? Sao không thử mỗi tuần tắt máy một ngày? Nói là làm, dứt khoát bắt đầu ngay tuần này.",
     ["难道会死吗 là câu phản vấn, chẳng lẽ sẽ chết sao. 何不 là sao không, tức 为什么不. 礼拜 là tuần, giống 星期.",
      "说干就干 là mẫu câu nói A là A, điểm ngữ pháp thứ hai. 索性 là dứt khoát, sẽ được so sánh với 干脆. Câu này cũng là mẫu câu của bài tập bốn."]),
    ("周日，我按小学生的作息时间七点起床，之后，先着手安置我的手机。为了防止自己意志薄弱，我找来个精致的盒子，把手机层层包好，庄重地放在盒子里，收到衣柜最里面。",
     "Chủ nhật, tôi dậy lúc bảy giờ theo giờ giấc của học sinh tiểu học, sau đó việc đầu tiên là bắt tay vào thu xếp chiếc điện thoại. Để đề phòng ý chí mình yếu đuối, tôi tìm một chiếc hộp tinh xảo, gói điện thoại từng lớp từng lớp, trang trọng đặt vào hộp, cất vào tận trong cùng tủ quần áo.",
     ["按 là theo, dựa theo. 意志薄弱 là ý chí yếu đuối: sợ mình không cưỡng lại được mà lại mở máy. 层层 là lượng từ lặp lại, nghĩa là từng lớp.",
      "Chuỗi động từ 包好，放在，收到 tả từng bước cất điện thoại. Cách làm trang trọng như an táng một người thân, rất buồn cười."]),
    ("为了分散注意力，我决定去公园锻炼我那僵硬的四肢，因为迷上智能手机以后，我已经好久不锻炼了。",
     "Để phân tán sự chú ý, tôi quyết định ra công viên vận động tứ chi đã cứng đờ của mình, vì từ khi mê điện thoại thông minh, tôi đã lâu lắm không tập thể dục.",
     ["我那僵硬的四肢 có đại từ chỉ thị xen vào giữa, mang sắc thái tự giễu: cái tứ chi cứng đờ ấy của tôi.",
      "迷上 là mê mẩn, phần sau là bổ ngữ chỉ bắt đầu và kéo dài. 好久不锻炼了 là đã lâu lắm không tập."]),
    ("公园里唱的跳的都有。跳舞是我的特长，我兴高采烈地跳起了摇滚，既能娱乐身心，又能锻炼身体，一举两得。",
     "Trong công viên, người hát người nhảy đều có. Nhảy là sở trường của tôi, tôi hớn hở nhảy theo nhạc rock, vừa giải trí thư giãn, vừa rèn luyện thân thể, một công đôi việc.",
     ["唱的跳的 thay cho danh từ: 唱歌的人，跳舞的人, người hát, người nhảy. 跳起了摇滚 chỉ hành động bắt đầu nhảy.",
      "既……又…… là vừa… vừa…. Câu này là mẫu câu thứ hai của bài tập bốn, các bạn nhớ cấu trúc nhé."]),
    ("跳完舞，我往家走，突然想起被冷落了半天儿的手机，急忙赶回家，打开衣柜，手机还在，我心里踏实了许多。",
     "Nhảy xong, tôi đi về nhà, bỗng nhớ đến chiếc điện thoại bị bỏ rơi suốt nửa ngày, vội vàng chạy về, mở tủ quần áo, điện thoại vẫn còn đó, lòng tôi yên tâm hơn nhiều.",
     ["往家走 là đi về phía nhà. 被冷落了半天儿 là câu bị động; 半天儿 là nửa ngày, cũng có thể chỉ rất lâu.",
      "踏实了许多 là tính từ cộng 了许多, nghĩa là hơn trước nhiều. Mở tủ ra thấy điện thoại vẫn còn thì mới yên tâm, đúng là vẫn còn nghiện."]),
    ("五个小时没碰它，我心空虚得要命，我决定用熬粥这件最消耗时间的事来弥补心中的空虚。",
     "Năm tiếng đồng hồ không chạm vào nó, lòng tôi trống rỗng kinh khủng, tôi quyết định dùng việc nấu cháo, việc tốn thời gian nhất, để bù đắp khoảng trống trong lòng.",
     ["空虚得要命 là trống rỗng kinh khủng, đây là điểm ngữ pháp thứ ba: tính từ cộng 得要命.",
      "熬粥 là nấu cháo nhỏ lửa trong thời gian dài. 用熬粥来弥补 nghĩa là dùng việc nấu cháo để bù đắp."]),
    ("烧水，下米，看着雪白的米在沸腾的水中翻滚，屋子里渐渐弥漫着粥的香气，屋外竟然传来了鸟的叫声，我的心慢慢静了下来。",
     "Đun nước, cho gạo vào, nhìn những hạt gạo trắng tinh lăn lộn trong nước sôi sùng sục, trong nhà dần dần tỏa ngát hương cháo, ngoài nhà vậy mà vọng vào tiếng chim hót, lòng tôi dần dần lắng lại.",
     ["雪白 là trắng như tuyết, cũng là tính từ trạng thái giống 通红. 翻滚 là lăn lộn, cuộn trào.",
      "竟然 là vậy mà, không ngờ: tiếng chim vẫn luôn có đó, chỉ là trước đây mải nhìn điện thoại nên không nghe thấy. 静了下来 có 下来 chỉ trạng thái dần lắng xuống."]),
    ("要在往常，我一定早待不住了，惦记着某某侦探的案件是不是有了突破，科学家是否有了震惊世界的发现，彩票大奖开了没有，前两天的恐怖袭击到底是谁干的……",
     "Nếu là mọi khi, chắc chắn tôi đã chẳng ngồi yên được từ lâu, cứ canh cánh không biết vụ án của thám tử nào đó đã có đột phá chưa, các nhà khoa học có phát hiện gì chấn động thế giới không, giải lớn xổ số đã quay chưa, vụ tấn công khủng bố mấy hôm trước rốt cuộc là ai làm…",
     ["要在往常 tức là 要是在往常, nếu như mọi khi, một giả thiết trái với thực tế. 待不住 là không ngồi yên được. 惦记着 là canh cánh trong lòng.",
      "某某 là người nào đó. 是否 là có… hay không, văn viết của 是不是. Chú ý 恐怖袭击 mới là tấn công khủng bố; riêng 恐怖 chỉ là đáng sợ."]),
    ("没有手机的干扰，生活这么安宁，我突然有了一种回归生活的欣慰。",
     "Không có sự quấy nhiễu của điện thoại, cuộc sống yên bình đến thế, bỗng nhiên tôi có một niềm vui như được trở về với cuộc sống thật.",
     ["回归 là trở về. 欣慰 là vui mừng, yên lòng.",
      "Câu kết là thông điệp của cả bài: thỉnh thoảng hãy rời điện thoại để cảm nhận cuộc sống thật quanh mình."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 不用手机的日子", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 不用手机的日子, dài tám trăm bốn mươi bốn chữ. Bài được cải biên từ bài viết 不用手机的一天 trên báo Buổi chiều Bắc Kinh.",
         F(0, "Thầy chia bài thành mười tám đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else Q(zh)
    zsize = 54 if len(zh) <= 100 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + Q(vi), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Tóm tắt nội dung", section="Bài khóa 课文", title="Tóm tắt bài khóa (theo bài tập 5) – phần 1", size=34,
    items=["## 1. 公司老板为什么开会时发火？",
           "大家开会时都在玩儿手机",
           "## 2. 开会时，“我”在手机上看什么？",
           "一对年轻人边开车边拍照，把桥撞坏了，没报警，先拍照发微信",
           "## 3. 为什么说“我”成了手机的奴隶？",
           "三分钟看一次新闻 · 十分钟发一次微信 · 吃饭前先拍照 · 睡觉前先充电……"],
    say=["Bài tập năm của sách yêu cầu dựa vào gợi ý để tóm tắt nội dung chính của bài khóa. Chúng ta cùng làm luôn nhé.",
         F(0, "Câu hỏi một: 公司老板为什么开会时发火？ Vì sao ông chủ nổi giận trong cuộc họp?"),
         F(1, "Vì 大家开会时都在玩儿手机, mọi người đều nghịch điện thoại trong lúc họp."),
         F(2, "Câu hỏi hai: 开会时，我在手机上看什么？ Lúc họp, nhân vật tôi xem gì trên điện thoại?"),
         F(3, "Anh ấy đọc tin: 一对年轻人边开车边拍照，把桥撞坏了，没报警，先拍照发微信。 Một đôi thanh niên vừa lái xe vừa chụp ảnh, đâm hỏng cầu, không báo cảnh sát mà chụp ảnh đăng WeChat trước."),
         F(4, "Câu hỏi ba: 为什么说我成了手机的奴隶？ Vì sao nói nhân vật tôi đã thành nô lệ của điện thoại?"),
         F(5, "Vì anh ấy 三分钟看一次新闻，十分钟发一次微信，吃饭前先拍照，睡觉前先给手机充电。 Ba phút đọc tin một lần, mười phút gửi WeChat một lần, trước khi ăn chụp ảnh, trước khi ngủ sạc điện thoại.")])

add("bullets", section="Bài khóa 课文", title="Tóm tắt bài khóa (theo bài tập 5) – phần 2", size=34,
    items=["## 4. 为了关机一天，“我”怎样安置自己的手机？",
           "把手机层层包好，放在精致的盒子里，收到衣柜最里面",
           "## 5. “我”如何出门锻炼的？",
           "去公园跳舞，既能娱乐身心，又能锻炼身体",
           "## 6. 回家后，“我”又做了什么？",
           "打开衣柜看手机 · 熬粥，心静了下来 · 往常：惦记新闻 → 现在：安宁、欣慰"],
    say=[F(0, "Câu hỏi bốn: 为了关机一天，我怎样安置自己的手机？ Để tắt máy một ngày, nhân vật tôi thu xếp điện thoại thế nào?"),
         F(1, "Anh ấy 把手机层层包好，放在精致的盒子里，收到衣柜最里面。 Gói điện thoại từng lớp, đặt vào chiếc hộp tinh xảo, cất vào tận trong cùng tủ quần áo."),
         F(2, "Câu hỏi năm: 我如何出门锻炼的？ Nhân vật tôi ra ngoài tập thể dục thế nào?"),
         F(3, "Anh ấy 去公园跳舞，既能娱乐身心，又能锻炼身体。 Ra công viên nhảy, vừa giải trí vừa rèn luyện thân thể."),
         F(4, "Câu hỏi sáu: 回家后，我又做了什么？ Về nhà, nhân vật tôi làm gì?"),
         F(5, "Anh ấy mở tủ xem điện thoại, rồi nấu cháo, lòng dần lắng lại. Nếu là mọi khi, anh ấy sẽ canh cánh đủ loại tin tức; còn bây giờ, cuộc sống thật yên bình, anh ấy thấy vui như được trở về với cuộc sống. Bố cục này rất có ích khi các bạn tự kể lại bài khóa.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 通红、雪白", section="Ngữ pháp 注释", title="1. Tính từ trạng thái: 通红、雪白", size=34,
    items=["通红 đỏ bừng, đỏ hết cả · 雪白 trắng như tuyết – nghĩa chính nằm ở chữ thứ hai",
           "Tự mang nghĩa mức độ cao → không thêm 很、非常、特别 phía trước, không thêm 极了、得很 phía sau",
           "Sai: 很通红 · 雪白极了 → Lặp lại theo kiểu ABAB: 通红通红、雪白雪白",
           "(1) 我脸憋得通红。",
           "(2) 雪白的米在沸腾的水中翻滚，屋子里渐渐弥漫着粥的香气。",
           "(3) 那几只还没断奶的小猫幸福地躺在妈妈的怀里，肚子都吃得滚圆滚圆的。"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là tính từ trạng thái, qua hai ví dụ trong bài: 通红 và 雪白.",
         F(0, "通红 nghĩa là đỏ bừng, toàn bộ đều đỏ. 雪白 nghĩa là trắng như tuyết. Loại tính từ này chủ yếu dùng để miêu tả trạng thái của sự vật, và nghĩa chính nằm ở chữ thứ hai: đỏ, trắng. Chữ đầu chỉ mức độ hoặc so sánh."),
         F(1, "Vì bản thân đã mang nghĩa mức độ cao, nên phía trước không thể thêm các phó từ chỉ mức độ như 很，非常，特别; phía sau cũng không thể thêm bổ ngữ chỉ mức độ như 极了，得很."),
         F(2, "Vì vậy nói 很通红 hay 雪白极了 đều sai. Khi muốn nhấn mạnh, ta lặp lại theo kiểu A B A B: 通红通红，雪白雪白. Các từ cùng loại còn có: 冰凉, lạnh buốt; 笔直, thẳng tắp; 雪亮, sáng như tuyết; 滚圆, tròn xoe."),
         F(3, "Ví dụ một, lấy từ bài khóa: 我脸憋得通红。 Mặt tôi đỏ bừng vì cố nén."),
         F(4, "Ví dụ hai, cũng trong bài khóa: 雪白的米在沸腾的水中翻滚，屋子里渐渐弥漫着粥的香气。 Những hạt gạo trắng tinh lăn lộn trong nước sôi, trong nhà dần tỏa ngát hương cháo."),
         F(5, "Ví dụ ba: 那几只还没断奶的小猫幸福地躺在妈妈的怀里，肚子都吃得滚圆滚圆的。 Mấy chú mèo con còn chưa cai sữa nằm hạnh phúc trong lòng mẹ, bụng con nào cũng no tròn xoe. Đây chính là dạng lặp A B A B: 滚圆滚圆.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: chọn từ điền vào chỗ trống (雪亮 · 冰凉 · 笔直)", reveal=True, size=36,
    items=["(1) 夏天，（　）的啤酒加上美味的海鲜，对很多人来讲，极具吸引力。",
           "Đáp án: 冰凉 – 冰凉的啤酒",
           "(2) 那是一条（　）的公路，她的车无精打采地在公路上前行，远处是茫茫雪山。",
           "Đáp án: 笔直 – 一条笔直的公路",
           "(3) 人民有自己的亲身经历，眼睛是（　）的。",
           "Đáp án: 雪亮 – 眼睛是雪亮的"],
    say=[F(0, "Luyện tập: chọn từ thích hợp điền vào chỗ trống. Có ba từ: 雪亮，冰凉，笔直. Câu một: 夏天，什么的啤酒加上美味的海鲜，对很多人来讲，极具吸引力。 Mùa hè, bia thế nào cộng thêm hải sản ngon thì rất hấp dẫn với nhiều người? Các bạn tạm dừng và chọn từ nhé."),
         F(1, "Đáp án: 冰凉。 冰凉的啤酒, bia lạnh buốt. Chữ đầu là băng, nghĩa là lạnh như băng."),
         F(2, "Câu hai: 那是一条什么的公路，她的车无精打采地在公路上前行，远处是茫茫雪山。 Đó là một con đường thế nào, xe của cô ấy uể oải chạy trên đường, xa xa là núi tuyết mênh mông."),
         F(3, "Đáp án: 笔直。 一条笔直的公路, một con đường thẳng tắp, thẳng như cây bút."),
         F(4, "Câu ba: 人民有自己的亲身经历，眼睛是什么的。 Nhân dân có trải nghiệm của chính mình, đôi mắt là thế nào?"),
         F(5, "Đáp án: 雪亮。 眼睛是雪亮的, đôi mắt sáng như tuyết, ý nói nhân dân nhìn rõ mọi chuyện, không thể lừa được.")])

add("bullets", chapter="Ngữ pháp: 说A就A", section="Ngữ pháp 注释", title="2. Mẫu câu 说A就A – nói là…, …ngay", size=36,
    items=["Mẫu câu khẩu ngữ: sự việc xảy ra hoặc diễn biến rất nhanh",
           "A là cùng một động từ, cụm động từ, hoặc tính từ",
           "(1) 说干就干，索性这礼拜就开始。",
           "(2) 他辞了职去旅游，可把爸妈气坏了，天天在家唠叨：“挺好的工作，一点儿都不珍惜，说不干就不干了。”",
           "(3) 六月下旬，天气说热就热了，人们争先恐后地往商店跑，去买电扇，去买空调。"],
    say=["Điểm ngữ pháp thứ hai là mẫu câu nói A là A, ví dụ trong bài: 说干就干.",
         F(0, "Đây là mẫu câu khẩu ngữ thường dùng, biểu thị sự việc xảy ra hoặc diễn biến rất nhanh, vừa nói xong là đã thành sự thật, không chần chừ."),
         F(1, "Hai chữ A ở trước và sau là cùng một từ: có thể là động từ, cụm động từ, hoặc tính từ."),
         F(2, "Ví dụ một, lấy từ bài khóa: 说干就干，索性这礼拜就开始。 Nói là làm, dứt khoát bắt đầu ngay tuần này. Ở đây A là động từ."),
         F(3, "Ví dụ hai: 他辞了职去旅游，可把爸妈气坏了，天天在家唠叨：挺好的工作，一点儿都不珍惜，说不干就不干了。 Anh ấy bỏ việc đi du lịch, làm bố mẹ tức điên, ngày nào cũng cằn nhằn: công việc tốt như thế mà chẳng biết quý, nói bỏ là bỏ luôn. Ở đây A là dạng phủ định của động từ."),
         F(4, "Ví dụ ba: 六月下旬，天气说热就热了，人们争先恐后地往商店跑，去买电扇，去买空调。 Cuối tháng sáu, trời nói nóng là nóng ngay, mọi người tranh nhau chạy ra cửa hàng mua quạt điện, mua điều hòa. Ở đây A là tính từ.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: dùng 说A就A viết lại câu", reveal=True, size=36,
    items=["(1) 你看天上，阴云密布的，马上就得下雨，不带伞哪行啊！",
           "Đáp án: 你看天上，阴云密布的，说下雨就下雨，不带伞哪行啊！",
           "(2) 小孩儿就是这样，一会儿哭，一会儿笑。",
           "Đáp án: 小孩儿就是这样，说哭就哭，说笑就笑。",
           "(3) 很快他们两个就好上了，好得朝夕相伴，形影不离。",
           "Đáp án: 他们两个说好就好上了，好得朝夕相伴，形影不离。"],
    say=[F(0, "Luyện tập: dùng mẫu câu nói A là A để viết lại câu. Câu một: 你看天上，阴云密布的，马上就得下雨，不带伞哪行啊！ Bạn nhìn trời xem, mây đen kín trời, sắp mưa ngay rồi, không mang ô sao được! Các bạn tạm dừng và thử viết lại nhé."),
         F(1, "Đáp án gợi ý: 你看天上，阴云密布的，说下雨就下雨，不带伞哪行啊！ Mây đen kín trời, nói mưa là mưa ngay đấy."),
         F(2, "Câu hai: 小孩儿就是这样，一会儿哭，一会儿笑。 Trẻ con là thế, lúc khóc lúc cười."),
         F(3, "Đáp án gợi ý: 小孩儿就是这样，说哭就哭，说笑就笑。 Trẻ con là thế, nói khóc là khóc, nói cười là cười."),
         F(4, "Câu ba: 很快他们两个就好上了，好得朝夕相伴，形影不离。 Chẳng mấy chốc hai người đã thân nhau, thân đến mức sớm tối có nhau, như hình với bóng."),
         F(5, "Đáp án gợi ý: 他们两个说好就好上了，好得朝夕相伴，形影不离。 Hai người nói thân là thân ngay. Ở câu này, A là tính từ.")])

add("bullets", chapter="Ngữ pháp: ……得要命", section="Ngữ pháp 注释", title="3. Tính từ / động từ + 得 + 要命 – …chết đi được", size=36,
    items=["Biểu thị mức độ đã đến cực điểm (khẩu ngữ)",
           "(1) 五个小时没碰它，我心空虚得要命。",
           "(2) 每次考试之前，不少同学都紧张得要命，吃不好，睡不着，有的还生病。",
           "(3) 他风趣地说，自从那次让蛇咬了一口，就害怕所有的爬行动物、虫子，见了麻绳都吓得要命。"],
    say=["Điểm ngữ pháp thứ ba là cấu trúc: tính từ hoặc động từ, cộng 得要命.",
         F(0, "Cấu trúc này biểu thị mức độ đã lên đến cực điểm, tiếng Việt dịch là chết đi được, kinh khủng, cực kỳ. Đây là cách nói khẩu ngữ, thường dùng cho cảm giác, trạng thái. Tương tự còn có 得不得了 và 得很."),
         F(1, "Ví dụ một, lấy từ bài khóa: 五个小时没碰它，我心空虚得要命。 Năm tiếng không chạm vào nó, lòng tôi trống rỗng kinh khủng."),
         F(2, "Ví dụ hai: 每次考试之前，不少同学都紧张得要命，吃不好，睡不着，有的还生病。 Mỗi lần trước kỳ thi, nhiều bạn học sinh căng thẳng kinh khủng, ăn không ngon, ngủ không được, có bạn còn bị ốm."),
         F(3, "Ví dụ ba: 他风趣地说，自从那次让蛇咬了一口，就害怕所有的爬行动物、虫子，见了麻绳都吓得要命。 Anh ấy nói đùa rằng, từ lần bị rắn cắn, anh ấy sợ tất cả loài bò sát và sâu bọ, thấy sợi dây thừng cũng sợ chết khiếp. Ở câu này, 吓得要命 là động từ cộng 得要命, nghĩa là sợ chết khiếp.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: hoàn thành câu với ……得要命", reveal=True, size=36,
    items=["(1) 他的确是个热心肠，尽管他平日大事小事特别多，____，可是只要有人求他，他一定会全力相助。",
           "Đáp án: ……特别多，忙得要命，可是……",
           "(2) 那是我第一次拍戏。临拍前一晚，我____，整晚睡不着，想戏怎么演，手势怎么摆，足足想了一夜。",
           "Đáp án: ……我紧张得要命，整晚睡不着……",
           "(3) 妈妈不但在生气，而且____。",
           "Đáp án: ……而且伤心得要命。"],
    say=[F(0, "Luyện tập: hoàn thành câu. Câu một: 他的确是个热心肠，尽管他平日大事小事特别多，什么，可是只要有人求他，他一定会全力相助。 Anh ấy quả thật là người nhiệt tình, dù ngày thường việc lớn việc nhỏ rất nhiều, thế nào, nhưng hễ có người nhờ là anh ấy dốc sức giúp đỡ. Các bạn tạm dừng và thử hoàn thành nhé."),
         F(1, "Đáp án gợi ý: 忙得要命。 Bận kinh khủng. 热心肠 nghĩa là người nhiệt tình, tốt bụng."),
         F(2, "Câu hai: 那是我第一次拍戏。临拍前一晚，我什么，整晚睡不着，想戏怎么演，手势怎么摆，足足想了一夜。 Đó là lần đầu tôi đóng phim. Đêm trước khi quay, tôi thế nào, cả đêm không ngủ được, nghĩ xem diễn thế nào, tay để ra sao, nghĩ trọn một đêm."),
         F(3, "Đáp án gợi ý: 我紧张得要命。 Tôi căng thẳng chết đi được."),
         F(4, "Câu ba: 妈妈不但在生气，而且什么。 Mẹ không chỉ đang tức giận, mà còn thế nào?"),
         F(5, "Đáp án gợi ý: 而且伤心得要命。 Mà còn buồn chết đi được. Các bạn cũng có thể nói 难过得要命. Chú ý vế sau phải tăng tiến so với vế trước, vì có 不但……而且…….")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 索性 – 干脆", section="Phân biệt từ 词语辨析", title="Phân biệt 索性 và 干脆",
    common="Giống nhau: làm phó từ, cách dùng cơ bản như nhau – nói, làm thẳng thắn, không cân nhắc nhiều. Ví dụ: 这鞋子太旧了，索性/干脆扔掉吧。",
    cols=[{"head": "索性",
           "lines": ["(1) Phó từ: dứt khoát làm luôn",
                     "Đúng: 他觉得这门课没用，索性不去上课了。",
                     "(2) Chỉ là phó từ, không làm tính từ, không làm vị ngữ",
                     "Sai: 我做事一直都很索性。"]},
          {"head": "干脆",
           "lines": ["(1) Phó từ: giống 索性",
                     "Đúng: 找不着，干脆不找了。",
                     "(2) Còn là tính từ, làm vị ngữ: thẳng thắn, dứt khoát (爽快)",
                     "Đúng: 这个人说话做事很干脆，一点儿也不拖泥带水。"]}],
    say=["Tiếp theo là phần phân biệt từ: 索性 và 干脆. Hai từ này đều dịch là dứt khoát, nên rất dễ dùng lẫn lộn.",
         "Điểm giống nhau: khi làm phó từ, cách dùng của hai từ cơ bản giống nhau, đều biểu thị nói năng, làm việc rất thẳng, không cân nhắc quá nhiều. Ví dụ: 这鞋子太旧了，索性扔掉吧, hoặc 干脆扔掉吧, đều đúng. Đôi giày này cũ quá rồi, vứt luôn đi.",
         F(0, "索性 chỉ có một cách dùng là phó từ, đứng trước động từ. Ví dụ: 他觉得这门课没用，索性不去上课了。 Anh ấy thấy môn học này vô ích, dứt khoát không đi học nữa."),
         F(1, "干脆 cũng làm phó từ giống hệt 索性. Ví dụ: 找不着，干脆不找了。 Tìm không thấy thì thôi không tìm nữa."),
         F(1, "Điểm khác biệt: ngoài cách dùng phó từ, 干脆 còn là tính từ, có thể làm vị ngữ, nghĩa là thẳng thắn, dứt khoát, giống 爽快. Ví dụ: 这个人说话做事很干脆，一点儿也不拖泥带水。 Người này nói năng làm việc rất dứt khoát, không chút dây dưa. 拖泥带水 nghĩa đen là kéo bùn mang nước, tức là dây dưa, lề mề."),
         F(0, "索性 không có cách dùng tính từ này. Vì vậy câu 我做事一直都很索性 là sai, vì 索性 không đứng sau 很 và không làm vị ngữ. Phải nói 我做事一直都很干脆。"),
         "Mẹo nhớ: thấy trước nó có 很，太，真, hoặc nó đứng cuối câu làm vị ngữ, thì chỉ dùng được 干脆."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: Đúng hay sai?", reveal=True, size=36,
    items=["(1) 他觉得这门课没有用，索性不去上课了。",
           "Đáp án: Đúng – 索性 làm phó từ, đứng trước động từ.",
           "(2) 你干脆点儿行吗？别总是犹犹豫豫的。",
           "Đáp án: Đúng – 干脆 là tính từ, làm vị ngữ.",
           "(3) 我做事一直都很索性，从来不琢磨来琢磨去。",
           "Đáp án: Sai – 索性 không làm tính từ. Sửa: 我做事一直都很干脆。",
           "(4) 他很干脆地拒绝了我，一点儿余地都没有。",
           "Đáp án: Đúng – 干脆 là tính từ, có thể đi sau 很."],
    say=[F(0, "Bây giờ chúng ta làm thử: phán đoán đúng sai. Câu một: 他觉得这门课没有用，索性不去上课了。 Anh ấy thấy môn học này vô ích, dứt khoát không đi học nữa. Đúng hay sai? Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: đúng. 索性 làm phó từ, đứng trước cụm động từ 不去上课."),
         F(2, "Câu hai: 你干脆点儿行吗？别总是犹犹豫豫的。 Cậu dứt khoát một chút được không? Đừng lúc nào cũng do dự thế."),
         F(3, "Đáp án: đúng. Ở đây 干脆 là tính từ, làm vị ngữ, phía sau có 点儿."),
         F(4, "Câu ba: 我做事一直都很索性，从来不琢磨来琢磨去。 Tôi làm việc luôn rất dứt khoát, chẳng bao giờ nghĩ tới nghĩ lui."),
         F(5, "Đáp án: sai. 索性 không phải tính từ, không đứng sau 很. Phải sửa thành 我做事一直都很干脆。"),
         F(6, "Câu bốn: 他很干脆地拒绝了我，一点儿余地都没有。 Anh ấy thẳng thừng từ chối tôi, không chừa chút đường lui nào."),
         F(7, "Đáp án: đúng. 干脆 là tính từ, có thể đi sau 很, rồi thêm trợ từ kết cấu thành 很干脆地, làm trạng ngữ.")])

# ======================= MỞ RỘNG: CÂU SAI DO KẾT HỢP KHÔNG PHÙ HỢP =======================
add("bullets", chapter="Mở rộng: câu sai do kết hợp từ", section="Mở rộng 扩展", title="Câu sai: kết hợp từ không phù hợp (搭配不当)", size=36,
    items=["Từ ngữ ghép với nhau không hợp thói quen ngôn ngữ, không đúng quy tắc ngữ pháp, ghép gượng ép",
           "## Các kiểu thường gặp",
           "Chủ ngữ – vị ngữ · chủ ngữ – tân ngữ · động từ – tân ngữ · giới từ – tân ngữ",
           "Từ liên kết · phó từ chỉ thời thái – trợ từ động thái",
           "Định ngữ, trạng ngữ – trung tâm ngữ (cũng rất dễ sai)"],
    say=["Bây giờ chúng ta sang phần mở rộng của sách. Như bài năm, quyển này không có mục tu từ riêng, thay vào đó là kỹ năng nhận biết câu sai. Hôm nay là loại câu sai do kết hợp từ không phù hợp, tiếng Trung gọi là 搭配不当.",
         F(0, "搭配不当 là khi các từ ngữ trong câu được ghép với nhau không hợp thói quen của ngôn ngữ, không đúng quy tắc ngữ pháp, bị ghép một cách gượng ép."),
         F(1, "Các trường hợp kết hợp sai rất đa dạng."),
         F(2, "Có thể sai giữa chủ ngữ và vị ngữ, giữa chủ ngữ và tân ngữ, giữa động từ và tân ngữ, giữa giới từ và tân ngữ."),
         F(3, "Cũng có thể sai ở cặp từ liên kết, hoặc giữa phó từ chỉ thời thái với trợ từ động thái."),
         F(4, "Ngoài ra, định ngữ hoặc trạng ngữ kết hợp không hợp với trung tâm ngữ cũng là loại câu sai không thể xem nhẹ. Chúng ta cùng xem năm ví dụ trong sách.")])

add("bullets", section="Mở rộng 扩展", title="Năm ví dụ trong sách (1)", size=34,
    items=["## (1) Chủ ngữ – vị ngữ",
           "Sai: 他们每年的粮食产量，除了自己消费以外，还要大量卖给国家。",
           "Sửa: 他们每年生产的粮食，除了…… (产量 không thể 消费、卖)",
           "## (2) Động từ – tân ngữ",
           "Sai: 告诉你一个好消息，我考上了HSK四级考试。",
           "Sửa: ……我通过了HSK四级考试。 (考上 + trường học, không + kỳ thi)"],
    say=[F(0, "Ví dụ một: sai giữa chủ ngữ và vị ngữ."),
         F(1, "Câu sai: 他们每年的粮食产量，除了自己消费以外，还要大量卖给国家。 Sản lượng lương thực hằng năm của họ, ngoài phần tự tiêu dùng, còn bán số lượng lớn cho nhà nước."),
         F(2, "Chủ ngữ 粮食产量 là sản lượng, một con số; mà con số thì không thể tiêu dùng hay đem bán. Phải sửa thành 他们每年生产的粮食, lương thực mà họ sản xuất hằng năm."),
         F(3, "Ví dụ hai: sai giữa động từ và tân ngữ."),
         F(4, "Câu sai: 告诉你一个好消息，我考上了HSK四级考试。 Báo cho bạn một tin vui, tôi đã thi đỗ kỳ thi HSK cấp bốn."),
         F(5, "考上 phải đi với tân ngữ là trường học, như 考上大学, thi đỗ đại học; không đi với kỳ thi. Phải sửa thành 我通过了HSK四级考试。 Tôi đã vượt qua kỳ thi HSK cấp bốn.")])

add("bullets", section="Mở rộng 扩展", title="Năm ví dụ trong sách (2)", size=34,
    items=["## (3) Cụm từ cố định",
           "Sai: 温度从24℃～26℃之间，是最适合这种植物生长的。 → Sửa: 温度在……之间",
           "## (4) Phó từ thời thái – trợ từ động thái",
           "Sai: ……自从他选择了汉语，就一直在努力学习了。 → Sửa: bỏ 了 ở cuối câu",
           "## (5) Trạng ngữ – trung tâm ngữ",
           "Sai: ……蓝方先是被打倒，接着，他渐渐地爬了起来…… → Sửa: 慢慢地"],
    say=[F(0, "Ví dụ ba: sai ở cụm từ cố định."),
         F(1, "Câu sai: 温度从二十四到二十六摄氏度之间，是最适合这种植物生长的。 Nhiệt độ từ hai mươi bốn đến hai mươi sáu độ C là thích hợp nhất cho loại cây này sinh trưởng. Cấu trúc cố định là 在……之间, ở trong khoảng. Phải sửa thành 温度在二十四到二十六摄氏度之间。"),
         F(2, "Ví dụ bốn: sai giữa phó từ chỉ thời thái và trợ từ động thái."),
         F(3, "Câu sai: 他是个勤奋好学的学生，自从他选择了汉语，就一直在努力学习了。 Cụm 一直在 biểu thị hành động đang kéo dài liên tục, không đi với trợ từ động thái ở cuối câu. Phải sửa thành 就一直在努力学习。"),
         F(4, "Ví dụ năm: sai giữa trạng ngữ và trung tâm ngữ."),
         F(5, "Câu sai: 大家紧张地注视着拳击比赛的双方，蓝方先是被打倒，接着，他渐渐地爬了起来。 渐渐 biểu thị mức độ hoặc số lượng tăng giảm dần dần, không hợp với hành động bò dậy. Phải đổi thành 慢慢地: 他慢慢地爬了起来。 Anh ta từ từ bò dậy.")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chỉ ra lỗi và sửa lại (1)", reveal=True, size=34,
    items=["(1) 这里有“庐山第一景”之称，一年四季泉水叮咚、鸟语花香、青松翠柏、云蒸雾绕。",
           "Đáp án: 一年四季 không hợp với 鸟语花香 → ……一年四季泉水叮咚、青松翠柏、云蒸雾绕，春夏更是鸟语花香。",
           "(2) 老板很赏识李朝阳温文尔雅的风度和丰富的知识，对他十分器重。",
           "Đáp án: 赏识 không hợp với 风度 → 老板很欣赏李朝阳温文尔雅的风度和丰富的知识……"],
    say=[F(0, "Luyện tập: chỉ ra lỗi của các câu sau và đề xuất cách sửa. Câu một: 这里有庐山第一景之称，一年四季泉水叮咚、鸟语花香、青松翠柏、云蒸雾绕。 Nơi đây được gọi là cảnh đẹp số một Lư Sơn, quanh năm suối chảy róc rách, chim hót hoa thơm, tùng bách xanh tươi, mây mù bao phủ. Câu này sai ở đâu? Các bạn tạm dừng và suy nghĩ nhé."),
         F(1, "Đáp án gợi ý: trạng ngữ 一年四季 không hợp với 鸟语花香, vì chim hót hoa nở không thể kéo dài suốt bốn mùa, mùa đông thì không có. Có thể sửa: 一年四季泉水叮咚、青松翠柏、云蒸雾绕，春夏更是鸟语花香。 Mùa xuân mùa hạ càng chim hót hoa thơm."),
         F(2, "Câu hai: 老板很赏识李朝阳温文尔雅的风度和丰富的知识，对他十分器重。 Ông chủ rất đánh giá cao phong thái nho nhã và kiến thức phong phú của Lý Triêu Dương, vô cùng coi trọng anh ấy."),
         F(3, "Đáp án gợi ý: 赏识 nghĩa là đánh giá cao tài năng của một người, nên tân ngữ thường là người hoặc tài năng, không đi với 风度, phong thái. Có thể đổi thành 欣赏: 老板很欣赏李朝阳温文尔雅的风度和丰富的知识。")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chỉ ra lỗi và sửa lại (2)", reveal=True, size=34,
    items=["(3) 他相信，凭着自己聪明能干的双手，一定能养活自己。",
           "Đáp án: 聪明 không hợp với 双手 → 凭着自己勤劳能干的双手……",
           "(4) 妈妈对于我不太信任，老把我当成孩子。",
           "Đáp án: Thái độ giữa người với người chỉ dùng 对 → 妈妈对我不太信任……",
           "(5) 快过春节了，人们把自己的家打扫得又干净又整齐。",
           "Đáp án: 打扫 không hợp với 整齐 → ……把自己的家收拾得又干净又整齐。"],
    say=[F(0, "Câu ba: 他相信，凭着自己聪明能干的双手，一定能养活自己。 Anh ấy tin rằng, dựa vào đôi tay thông minh tháo vát của mình, nhất định có thể tự nuôi sống bản thân. Câu này sai ở đâu?"),
         F(1, "Đáp án gợi ý: định ngữ 聪明 không hợp với trung tâm ngữ 双手, vì đôi tay thì không thể thông minh. Sửa: 凭着自己勤劳能干的双手, dựa vào đôi tay cần cù tháo vát."),
         F(2, "Câu bốn: 妈妈对于我不太信任，老把我当成孩子。 Mẹ không tin tưởng tôi lắm, lúc nào cũng coi tôi như trẻ con."),
         F(3, "Đáp án gợi ý: khi biểu thị thái độ, quan hệ giữa người với người, chỉ dùng được giới từ 对, không dùng 对于. Sửa: 妈妈对我不太信任，老把我当成孩子。"),
         F(4, "Câu năm: 快过春节了，人们把自己的家打扫得又干净又整齐。 Sắp đến Tết, mọi người dọn dẹp nhà cửa vừa sạch sẽ vừa gọn gàng."),
         F(5, "Đáp án gợi ý: 打扫 là quét dọn, kết quả là 干净, sạch sẽ; nhưng không thể quét mà ra 整齐, ngăn nắp. Sửa: 把自己的家收拾得又干净又整齐。 Hoặc tách ra: 打扫得干干净净，收拾得整整齐齐. Mẹo: khi gặp câu dài, hãy rút gọn còn bộ khung chủ ngữ, động từ, tân ngữ, rồi kiểm tra từng cặp xem có ghép được với nhau không.")])

add("bullets", section="Mở rộng 扩展", title="Mở rộng 2: nghĩa của yếu tố cấu tạo từ (语素义)", size=33,
    items=["无知: 无 không có + 知 tri thức → thiếu hiểu biết · 登陆: 登 lên cao + 陆 đất liền → đổ bộ",
           "破例: 破 phá bỏ + 例 quy tắc → phá lệ · 失踪: 失 không tìm thấy + 踪 dấu vết → mất tích",
           "盛产: 盛 thịnh + 产 sản xuất → sản xuất nhiều · 散布: 散 tản ra + 布 sắp xếp → rải rác, lan truyền",
           "额外: 额 định mức + 外 ngoài → ngoài định mức · 密封: 密 khít + 封 đóng kín → niêm phong",
           "埋没: 埋 lấp đất + 没 ẩn giấu → vùi lấp, mai một · 密度: 密 gần nhau + 度 mức độ → mật độ",
           "扩散: 扩 mở rộng + 散 tản đi khắp nơi → khuếch tán · 废墟: 废 bỏ đi + 墟 đất hoang → đống đổ nát"],
    say=["Phần mở rộng thứ hai của sách yêu cầu làm quen với nghĩa của từng yếu tố cấu tạo nên từ, tiếng Trung gọi là 语素义. Hiểu nghĩa từng chữ, ta sẽ hiểu từ rất sâu và nhớ rất lâu.",
         F(0, "无知: chữ đầu là 没有, không có; chữ sau là 知识, tri thức; ghép lại là thiếu hiểu biết. 登陆: chữ đầu là lên chỗ cao, chữ sau là 陆地, đất liền; ghép lại là đổ bộ, lên bờ. Nay 登陆 còn có nghĩa là đăng nhập."),
         F(1, "破例: chữ đầu là 突破，撤除, phá bỏ; chữ sau là 规则, quy tắc; ghép lại là phá lệ. 失踪: chữ đầu là 找不着, không tìm thấy; chữ sau là 踪迹, dấu vết; ghép lại là mất tích."),
         F(2, "盛产: chữ đầu là 兴盛, thịnh vượng; chữ sau là 生产; ghép lại là sản xuất nhiều. 散布: chữ đầu là 分开, tách ra; chữ sau là 排列, sắp xếp; ghép lại là rải rác khắp nơi, hoặc lan truyền."),
         F(3, "额外: chữ đầu là 规定的数目, con số quy định; chữ sau là 以外, ngoài; ghép lại là ngoài định mức. 密封: chữ đầu là 空隙小, khe hở nhỏ; chữ sau là 密闭，关住, đóng kín; ghép lại là niêm phong, đóng kín."),
         F(4, "埋没: chữ đầu là 用土等物盖住, lấp bằng đất; chữ sau là 隐藏, ẩn giấu; ghép lại là vùi lấp, hoặc làm mai một tài năng. 密度: chữ đầu là 事物之间距离近, khoảng cách gần; chữ sau là 程度; ghép lại là mật độ."),
         F(5, "扩散: chữ đầu là 扩大, mở rộng; chữ sau là 分散到各处, tản đi khắp nơi; ghép lại là khuếch tán, lan rộng. 废墟: chữ đầu là 没用的, bỏ đi; chữ sau là 荒废的地方, nơi hoang phế; ghép lại là đống đổ nát. Các bạn để ý, nhiều từ có âm Hán Việt rất quen, như phá lệ, mật độ, khuếch tán.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ có dấu chấm", size=40,
    items=["受罪 (受) → 受伤 · 受累 · 受骗 · 受气",
           "智能 (智) → 智力 · 智慧 · 智商 · 机智",
           "安置 (安) → 安排 · 安装 · 安放 · 安心",
           "防止 (防) → 预防 · 防守 · 防火 · 防盗",
           "精致 (精) → 精美 · 精细 · 精彩 · 精品"],
    say=["Phần luyện tập. Bài tập một: mô phỏng ví dụ, viết thêm các từ có chứa chữ được đánh dấu chấm. Trong bài này, chữ được đánh dấu đều là chữ đầu.",
         F(0, "Ví dụ mẫu: 受罪. Ta có 受伤，受累，受骗，受气. Tức là bị thương, chịu vất vả, bị lừa, và bị ức hiếp, chịu uất ức."),
         F(1, "智能, chữ đầu nghĩa là trí tuệ. Ta có 智力，智慧，智商，机智. Tức là trí lực, trí tuệ, chỉ số thông minh, và nhanh trí."),
         F(2, "安置, chữ đầu nghĩa là yên, đặt yên. Ta có 安排，安装，安放，安心. Tức là sắp xếp, lắp đặt, đặt để, và yên tâm."),
         F(3, "防止, chữ đầu nghĩa là phòng. Ta có 预防，防守，防火，防盗. Tức là dự phòng, phòng thủ, phòng cháy, và chống trộm."),
         F(4, "精致, chữ đầu nghĩa là tinh. Ta có 精美，精细，精彩，精品. Tức là tinh xảo đẹp đẽ, tỉ mỉ, đặc sắc, và sản phẩm tinh hoa.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (1)", reveal=True, size=36,
    items=["(1) 她的脾气不好，经常不知道为什么突然就生气了。（说A就A）",
           "Đáp án: 她的脾气不好，经常说生气就生气。",
           "(2) 这么做不但能增加公司的利润，还能方便用户。（既……又……）",
           "Đáp án: 这么做既能增加公司的利润，又能方便用户。",
           "(3) 找了好几个地方都没找着，干脆不找了。（索性）",
           "Đáp án: 找了好几个地方都没找着，索性不找了。"],
    say=[F(0, "Bài tập hai: dùng từ hoặc cấu trúc cho sẵn để viết lại câu. Câu một, dùng mẫu nói A là A: 她的脾气不好，经常不知道为什么突然就生气了。 Tính cô ấy không tốt, thường chẳng biết vì sao tự nhiên nổi giận. Các bạn tạm dừng và thử viết lại nhé."),
         F(1, "Đáp án: 她的脾气不好，经常说生气就生气。 Tính cô ấy không tốt, thường nói giận là giận ngay."),
         F(2, "Câu hai, dùng 既……又……: 这么做不但能增加公司的利润，还能方便用户。 Làm thế này không những tăng lợi nhuận cho công ty, mà còn tiện cho người dùng."),
         F(3, "Đáp án: 这么做既能增加公司的利润，又能方便用户。 Giống câu trong bài: 既能娱乐身心，又能锻炼身体."),
         F(4, "Câu ba, dùng 索性: 找了好几个地方都没找着，干脆不找了。 Tìm mấy chỗ rồi mà không thấy, thôi không tìm nữa."),
         F(5, "Đáp án: thay 干脆 bằng 索性: 找了好几个地方都没找着，索性不找了。 Ở đây cả hai đều là phó từ, nên thay được cho nhau.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Viết lại câu bằng từ cho sẵn (2)", reveal=True, size=36,
    items=["(4) 很多单位在年底就开始制定第二年的计划了。（着手）",
           "Đáp án: 很多单位在年底就着手制定第二年的计划了。",
           "(5) 今天不知道怎么了，堵得这么厉害，以前这里很少堵车。（往常）",
           "Đáp án: ……堵得这么厉害，往常这里很少堵车。",
           "(6) 考试时，我非常紧张，手心里都是汗。（……得要命）",
           "Đáp án: 考试时，我紧张得要命，手心里都是汗。"],
    say=[F(0, "Câu bốn, dùng 着手: 很多单位在年底就开始制定第二年的计划了。 Nhiều cơ quan từ cuối năm đã bắt đầu lập kế hoạch cho năm sau."),
         F(1, "Đáp án: thay 开始 bằng 着手: 很多单位在年底就着手制定第二年的计划了。 Bắt tay vào lập kế hoạch."),
         F(2, "Câu năm, dùng 往常: 今天不知道怎么了，堵得这么厉害，以前这里很少堵车。 Hôm nay chẳng biết làm sao, tắc đường kinh khủng, trước đây chỗ này ít khi tắc."),
         F(3, "Đáp án: thay 以前 bằng 往常: 往常这里很少堵车。 Mọi khi chỗ này ít khi tắc đường."),
         F(4, "Câu sáu, dùng 得要命: 考试时，我非常紧张，手心里都是汗。 Lúc thi, tôi rất căng thẳng, lòng bàn tay toàn mồ hôi."),
         F(5, "Đáp án: 考试时，我紧张得要命，手心里都是汗。 Lúc thi, tôi căng thẳng chết đi được. Chú ý: khi dùng 得要命 thì phải bỏ 非常, vì không thể vừa có phó từ mức độ vừa có bổ ngữ mức độ.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (1)", reveal=True, size=34,
    items=["## Từ cho sẵn: 案件 · 报警 · 绑架 · 震惊 · 侦探",
           "上个月，这里发生了一起令人___的___，两个年轻人___了他们的同学，然后向同学的父母要一大笔钱。受害孩子的家人___以后，警察迅速开展工作，他们派出一位非常有经验的___，很快就抓住了那两个年轻人，救出了他们的同学。",
           "Đáp án: 震惊 · 案件 · 绑架 · 报警 · 侦探"],
    say=[F(0, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn một có năm từ: 案件，报警，绑架，震惊，侦探."),
         F(1, "上个月，这里发生了一起令人什么的什么，两个年轻人什么了他们的同学，然后向同学的父母要一大笔钱。受害孩子的家人什么以后，警察迅速开展工作，他们派出一位非常有经验的什么，很快就抓住了那两个年轻人，救出了他们的同学。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 一起令人震惊的案件，两个年轻人绑架了他们的同学，家人报警以后，派出一位非常有经验的侦探。 Tháng trước, ở đây xảy ra một vụ án gây chấn động: hai thanh niên bắt cóc bạn học của mình rồi đòi bố mẹ bạn ấy một khoản tiền lớn. Sau khi gia đình nạn nhân báo cảnh sát, cảnh sát nhanh chóng vào cuộc, cử một thám tử rất có kinh nghiệm, chẳng mấy chốc đã bắt được hai thanh niên kia và cứu được cậu bạn học. Chú ý: 一起 ở đây là lượng từ cho vụ việc.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (2)", reveal=True, size=34,
    items=["## Từ cho sẵn: 着手 · 作息 · 干扰 · 四肢 · 狼吞虎咽",
           "我的___时间是这样的：早上6:00起床，先活动活动___，然后做一顿营养丰富的早餐，我吃饭从来不___，享受了美味的早餐后，我___写我的新书，在没人___的情况下，我的写作进度会很快，写着写着一天的时光不知不觉就过去了。",
           "Đáp án: 作息 · 四肢 · 狼吞虎咽 · 着手 · 干扰"],
    say=[F(0, "Đoạn hai có năm từ: 着手，作息，干扰，四肢，狼吞虎咽."),
         F(1, "我的什么时间是这样的：早上六点起床，先活动活动什么，然后做一顿营养丰富的早餐，我吃饭从来不什么，享受了美味的早餐后，我什么写我的新书，在没人什么的情况下，我的写作进度会很快，写着写着一天的时光不知不觉就过去了。 Các bạn điền thử nhé."),
         F(2, "Đáp án: 作息时间，活动活动四肢，吃饭从来不狼吞虎咽，我着手写我的新书，在没人干扰的情况下。 Giờ giấc sinh hoạt của tôi thế này: sáu giờ sáng dậy, vận động chân tay một chút, rồi làm một bữa sáng giàu dinh dưỡng. Tôi chưa bao giờ ăn ngấu nghiến. Thưởng thức xong bữa sáng ngon lành, tôi bắt tay vào viết cuốn sách mới. Khi không có ai quấy rầy, tôi viết rất nhanh, viết mãi viết mãi, một ngày trôi qua lúc nào không hay."),
         "Các bạn thấy không, đây là một ngày sống rất lành mạnh, không hề có bóng dáng của điện thoại."])

add("bullets", section="Luyện tập 练习", title="Bài tập 4: Đọc đoạn văn, mô phỏng đặt câu", reveal=True, size=34,
    items=["离开了手机，难道会死吗？何不尝试一下一周关机一天？说干就干，索性这礼拜就开始。",
           "Đáp án: 丢了工作，难道就活不下去了吗？何不趁机好好休息一段时间？说干就干，我索性明天就去旅行。",
           "跳舞是我的特长，我兴高采烈地跳起了摇滚，既能娱乐身心，又能锻炼身体，一举两得。",
           "Đáp án: 唱歌是我的特长，我高高兴兴地报名参加了比赛，既能展示自己，又能结交朋友，一举两得。"],
    say=[F(0, "Bài tập bốn: đọc đoạn văn, rồi mô phỏng để đặt câu. Câu mẫu một: 离开了手机，难道会死吗？何不尝试一下一周关机一天？说干就干，索性这礼拜就开始。 Đề bài cho khung: 丢了工作，难道什么吗？何不什么？说干就干，什么就什么。 Mất việc rồi, chẳng lẽ…? Sao không…? Các bạn thử viết nhé."),
         F(1, "Đáp án gợi ý: 丢了工作，难道就活不下去了吗？何不趁机好好休息一段时间？说干就干，我索性明天就去旅行。 Mất việc rồi, chẳng lẽ không sống nổi sao? Sao không nhân dịp này nghỉ ngơi một thời gian? Nói là làm, tôi dứt khoát ngày mai đi du lịch luôn."),
         F(2, "Câu mẫu hai: 跳舞是我的特长，我兴高采烈地跳起了摇滚，既能娱乐身心，又能锻炼身体，一举两得。 Đề bài cho khung: 什么是我的特长，我什么，既什么，又什么。"),
         F(3, "Đáp án gợi ý: 唱歌是我的特长，我高高兴兴地报名参加了比赛，既能展示自己，又能结交朋友，一举两得。 Ca hát là sở trường của tôi, tôi vui vẻ đăng ký dự thi, vừa thể hiện được bản thân, vừa kết bạn được, một công đôi việc.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 9", size=34,
    items=["Từ vựng trọng tâm: 绑架 · 受罪 · 麻木 · 狼吞虎咽 · 伺候 · 索性 · 着手 · 薄弱 · 一举两得 · 冷落 · 踏实 · 弥补 · 往常 · 干扰 · 安宁",
           "Ngữ pháp: 通红、雪白 (không thêm 很) · 说A就A (rất nhanh) · ……得要命 (cực điểm)",
           "Phân biệt: 索性 (chỉ là phó từ) ≠ 干脆 (phó từ + tính từ: 很干脆)",
           "Mở rộng: câu sai do kết hợp từ không phù hợp · nghĩa của yếu tố cấu tạo từ",
           "## Bài tập về nhà (运用)",
           "Viết bài ít nhất 300 chữ với đề 如何离开手机: mình có là nô lệ của điện thoại không, và có đề xuất gì?"],
    say=["Chúng ta cùng tổng kết bài chín.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 绑架，受罪，麻木，狼吞虎咽，伺候，索性，着手，薄弱，一举两得，冷落，踏实，弥补，往常，干扰，安宁. Và đừng quên những từ dễ nhầm như 僵硬，恐怖，安宁."),
         F(1, "Về ngữ pháp: tính từ trạng thái như 通红，雪白 đã mang nghĩa mức độ cao, không thêm 很 hay 极了. Mẫu câu nói A là A, như 说干就干, chỉ sự việc diễn ra rất nhanh. Và cấu trúc 得要命, như 空虚得要命, chỉ mức độ cực điểm."),
         F(2, "Về phân biệt từ: 索性 chỉ là phó từ; còn 干脆 vừa là phó từ, vừa là tính từ, có thể nói 很干脆."),
         F(3, "Về phần mở rộng: khi gặp câu sai do kết hợp từ, hãy rút gọn câu còn bộ khung rồi kiểm tra từng cặp; và hãy tập phân tích nghĩa từng chữ khi học từ mới."),
         F(5, "Bài tập về nhà, theo phần vận dụng của sách: có người nói điện thoại, máy tính và các sản phẩm công nghệ cao đã khống chế cuộc sống của con người. Bạn có giống nhân vật trong bài, trở thành nô lệ của chúng không? Muốn thay đổi tình trạng này, bạn có đề xuất gì hay? Hãy lấy đề bài 如何离开手机, kết hợp với thực tế của bản thân, viết một bài văn ít nhất ba trăm chữ. Nhớ thử dùng 说干就干，得要命，索性 trong bài viết nhé."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Tối nay, các bạn thử tắt điện thoại một giờ xem sao nhé. Hẹn gặp lại các bạn ở bài mười: 全球化视野中的中国饮食, Thức ăn Trung Quốc trong xu thế toàn cầu hóa. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Thượng) – Bài 9: 不用手机的日子 (Một ngày không sử dụng điện thoại di động)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"伺候": "刺候",            # cìhou
                    "着手": "酌手",            # zhuóshǒu
                    "薄弱": "博弱",            # bóruò
                    "特长": "特常",            # tècháng
                    "兴高采烈": "幸高采烈",    # xìnggāo
                    "冷落": "冷洛",            # lěngluò
                    "踏实": "塌实",            # tāshi
                    "熬粥": "敖粥",            # áozhōu
                    "说干就干": "说赣就赣",    # gàn
                    "说不干就不干": "说不赣就不赣",  # gàn
                    "谁干的": "谁赣的",        # gàn
                    "能干": "能赣",            # nénggàn
                    "干吗": "赣吗",            # gànmá
                    "为何": "位何",            # wèihé
                    "何处": "何触",            # héchù
                    "朝夕": "招夕",            # zhāoxī
                    "待不住": "呆不住",        # dāi
                    "冲他": "铳他",            # chòng
                    "生长": "生涨",            # shēngzhǎng
                    "打倒": "打岛",            # dǎdǎo
                    "当成": "荡成",            # dàngchéng
                    "埋没": "埋末",            # máimò
                    "琢磨": "昨磨",            # zuómo
                    "这种植物": "这肿植物",    # zhǒng
                    "的确": "敌确"},           # díquè
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai09.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
