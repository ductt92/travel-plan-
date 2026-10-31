#!/usr/bin/env python3
"""Kịch bản bài giảng 顶石中文 – Bài 4.1 «真的，你的隐私只值一分钱！». Chạy để sinh ds41.json."""
import json
import os

TAG = "顶石中文 · Bài 4.1 · 真的，你的隐私只值一分钱！"
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
    zh="真的，你的隐私", py="只值一分钱！",
    vi="Bài 4.1: Thật đấy, quyền riêng tư của bạn chỉ đáng một xu!",
    sub="Zhēn de, nǐ de yǐnsī zhǐ zhí yì fēn qián!\nBài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng giáo trình 顶石中文, Đỉnh cao tiếng Trung, giáo trình tổng hợp tiếng Hán cao cấp.",
         "Hôm nay chúng ta học bài bốn chấm một: 真的，你的隐私只值一分钱！ Nghĩa là: Thật đấy, quyền riêng tư của bạn chỉ đáng một xu!",
         "Đây là bài đầu tiên của Đơn vị bốn, 科技篇, Khoa học công nghệ. Ba bài của đơn vị này bàn về mặt trái và mặt phải của công nghệ: quyền riêng tư trên mạng, bác sĩ robot, và chuyện tìm người yêu bằng thuật toán.",
         "Bài hôm nay là một bài bình luận đăng trên tạp chí 新周刊. Mở đầu là một cuộc triển lãm kỳ lạ: một nghệ sĩ mua ba trăm bốn mươi sáu nghìn mẩu thông tin cá nhân từ chợ đen, và mỗi mẩu chỉ có giá một xu. Từ đó, tác giả đặt câu hỏi: phải chăng chúng ta đã quá hào phóng với quyền riêng tư của mình? Chắc chắn các bạn sẽ thấy rất quen, vì ở Việt Nam, cuộc gọi rác và tin nhắn lừa đảo gọi đúng tên mình cũng chẳng còn hiếm."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài bình luận: thông tin cá nhân bị rò rỉ, mua bán trong thời đại Internet",
           "Nắm vững 45 từ mới, kèm âm Hán Việt và ví dụ",
           "9 mẫu câu trọng điểm: V到……地步 · V都懒得V · 殊不知 · 无异于 · 毫无……可言 · 仗着 · 非但不……反而…… · 被……绑架 · 切勿",
           "Kết hợp từ (骚扰、让渡、悉数、不乏……) và 14 thành ngữ",
           "Luyện tập theo sách, thảo luận: quyền riêng tư ở Việt Nam"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu bài bình luận: thông tin cá nhân của chúng ta bị rò rỉ, bị mua bán như thế nào trong thời đại Internet, và tác giả khuyên chúng ta điều gì."),
         F(1, "Thứ hai, nắm vững bốn mươi lăm từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học chín mẫu câu trọng điểm của sách, như 到什么地步, đến mức nào đó; 殊不知, nào ngờ; 无异于, chẳng khác gì; và 非但不，反而, chẳng những không mà ngược lại còn."),
         F(3, "Thứ tư, học các kết hợp từ thường gặp, và mười bốn thành ngữ xuất hiện trong bài, như 瞠目结舌，防不胜防，前车之鉴."),
         F(4, "Thứ năm, làm toàn bộ bài tập của sách, rồi cùng thảo luận về quyền riêng tư ở Việt Nam. Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé.")])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 课前思考", title="Suy nghĩ trước bài học (课前思考)", reveal=True, size=34,
    items=["(1) 你理解的隐私包括哪些？",
           "Đáp án gợi ý: 姓名、电话、住址、身份证号、银行账户、病历、聊天记录、行踪……",
           "(2) 在你们国家，什么样的行为算是侵犯隐私权？",
           "Đáp án gợi ý: 偷看别人的手机、未经允许公开别人的照片和聊天记录、买卖个人信息……",
           "(3) 大数据时代，你觉得哪些新技术可能侵犯了人的隐私？",
           "Đáp án gợi ý: 人脸识别、定位功能、精准推送广告、手机应用过度索取权限……"],
    say=["Chúng ta bắt đầu bằng phần suy nghĩ trước bài học, tiếng Trung là 课前思考. Sách đưa ra ba câu hỏi để các bạn tự nghĩ trước khi đọc bài.",
         F(0, "Câu một: 你理解的隐私包括哪些？ Theo bạn hiểu, quyền riêng tư bao gồm những gì? 隐私 là đời tư, chuyện riêng tư, từ khóa của cả bài. Các bạn tạm dừng và nghĩ thử nhé."),
         F(1, "Đáp án gợi ý: 姓名，电话，住址，身份证号，银行账户，病历，聊天记录，行踪. Tức là họ tên, số điện thoại, địa chỉ, số căn cước, tài khoản ngân hàng, bệnh án, lịch sử trò chuyện, và hành tung, nơi mình đi lại."),
         F(2, "Câu hai: 在你们国家，什么样的行为算是侵犯隐私权？ Ở nước bạn, hành vi như thế nào bị coi là xâm phạm quyền riêng tư? 侵犯 là xâm phạm, 隐私权 là quyền riêng tư."),
         F(3, "Đáp án gợi ý: 偷看别人的手机，未经允许公开别人的照片和聊天记录，买卖个人信息. Tức là xem trộm điện thoại người khác, công khai ảnh và tin nhắn của người khác khi chưa được phép, và mua bán thông tin cá nhân. Ở Việt Nam, mua bán thông tin cá nhân là hành vi vi phạm pháp luật."),
         F(4, "Câu ba: 大数据时代，你觉得哪些新技术可能侵犯了人的隐私？ Trong thời đại dữ liệu lớn, bạn thấy những công nghệ mới nào có thể xâm phạm quyền riêng tư?"),
         F(5, "Đáp án gợi ý: 人脸识别，定位功能，精准推送广告，手机应用过度索取权限. Tức là nhận diện khuôn mặt, chức năng định vị, quảng cáo nhắm đúng đối tượng, và ứng dụng điện thoại đòi quá nhiều quyền truy cập. Lát nữa, bài khóa sẽ nhắc đến gần như tất cả những điều này.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("黑市", "hēishì", "hắc thị", "danh từ", "chợ đen", "他在黑市上买到了一张火车票。", "Anh ấy mua được một vé tàu ở chợ đen.",
     "Danh từ, nghĩa là chợ đen, nơi mua bán lén lút, phi pháp. 黑 là đen, 市 là chợ. Trong bài, nghệ sĩ mua thông tin cá nhân 从黑市, từ chợ đen."),
    ("细化", "xìhuà", "tế hóa", "động từ", "chi tiết hóa, cụ thể hóa", "管理工作要细化到各个岗位。", "Công tác quản lý phải được cụ thể hóa đến từng vị trí.",
     "Động từ, nghĩa là chia nhỏ ra cho cụ thể, chi tiết hơn. 细 là nhỏ, tỉ mỉ; hậu tố 化 là hóa. Trong bài, 一些信息细化到令人瞠目结舌的地步 là có những thông tin chi tiết đến mức khiến người ta sững sờ."),
    ("地步", "dìbù", "địa bộ", "danh từ", "nông nỗi, tình cảnh; mức độ", "他兴奋得到了不能入睡的地步。", "Anh ấy phấn khích đến mức không ngủ được.",
     "Danh từ, nghĩa là tình cảnh, nông nỗi, thường là tình cảnh không tốt; cũng chỉ mức độ đạt tới. Hay gặp trong mẫu 到什么地步, đến mức nào đó. Đây là mẫu câu trọng điểm đầu tiên."),
    ("彼岸", "bǐ'àn", "bỉ ngạn", "danh từ", "bờ bên kia", "他的家人都在大洋彼岸。", "Gia đình anh ấy đều ở bên kia đại dương.",
     "Danh từ, nghĩa là bờ bên kia, văn viết. 彼 là kia, 岸 là bờ. Tiếng Việt có hoa bỉ ngạn, và trong nhà Phật, bỉ ngạn là bờ giác ngộ. Trong bài, 大洋彼岸的老外 là người nước ngoài ở bên kia đại dương, tức là người phương Tây."),
    ("小气", "xiǎoqì", "tiểu khí", "tính từ", "keo kiệt, bủn xỉn; hẹp hòi", "他很小气，从来不请客。", "Anh ta rất keo kiệt, chưa bao giờ mời ai.",
     "Tính từ, nghĩa là keo kiệt, không hào phóng; cũng có nghĩa là hẹp hòi, hay để bụng. Trái nghĩa là 大方, hào phóng. Bài khóa dùng hai từ này để nói về thái độ với quyền riêng tư."),
    ("懒得", "lǎnde", "lãn đắc", "động từ", "lười, chẳng buồn (làm gì)", "天太热，我懒得上街。", "Trời nóng quá, tôi chẳng buồn ra phố.",
     "Động từ, nghĩa là ngại, chẳng buồn làm việc gì, khẩu ngữ. 懒 là lười. Sau 懒得 là một động từ: 懒得说，懒得管. Trong bài có mẫu 删都懒得删, xóa cũng chẳng buồn xóa."),
    ("骚扰", "sāorǎo", "tao nhiễu", "động từ", "quấy rối, làm phiền", "我每天都会接到骚扰电话。", "Ngày nào tôi cũng nhận được cuộc gọi làm phiền.",
     "Động từ, nghĩa là quấy rối, làm phiền, khiến người khác không yên. Hay gặp 骚扰电话, cuộc gọi làm phiền; 骚扰短信, tin nhắn rác. Lát nữa ta học thêm các kết hợp của từ này."),
    ("报", "bào", "báo", "động từ", "báo, nói cho biết", "请报一下你的姓名和电话。", "Xin hãy cho biết họ tên và số điện thoại của bạn.",
     "Động từ, nghĩa là báo, nói cho người khác biết, như 报姓名, báo họ tên; 报警, báo cảnh sát. Trong bài, 一张口就能准确地报上你的姓氏 là vừa mở miệng đã nói đúng họ của bạn."),
    ("社交", "shèjiāo", "xã giao", "danh từ", "giao tiếp xã hội, giao lưu", "她每天花很多时间在社交软件上。", "Mỗi ngày cô ấy dành rất nhiều thời gian trên mạng xã hội.",
     "Danh từ, nghĩa là sự giao tiếp, qua lại giữa người với người trong xã hội. Cẩn thận: tiếng Việt xã giao thường là phép lịch sự bề ngoài; còn 社交 là giao tiếp xã hội nói chung. 社交软件 là ứng dụng mạng xã hội, 社交场合 là chốn giao tế."),
    ("漏洞", "lòudòng", "lậu động", "danh từ", "lỗ hổng, kẽ hở", "这个系统存在安全漏洞。", "Hệ thống này tồn tại lỗ hổng bảo mật.",
     "Danh từ, nghĩa gốc là lỗ thủng làm rò rỉ; nghĩa bóng là điểm yếu, sơ hở của một hệ thống, như 系统漏洞，安全漏洞; hay sơ hở trong lập luận, luật pháp: 法律漏洞."),
    ("一己", "yījǐ", "nhất kỷ", "danh từ", "bản thân, cá nhân mình", "单凭一己之力，很难改变现状。", "Chỉ dựa vào sức một mình thì rất khó thay đổi hiện trạng.",
     "Danh từ, văn viết, nghĩa là bản thân một người. 己 là mình, như trong tri kỷ. Thường dùng trong cụm 一己之力, sức của một người; 一己之见, ý kiến riêng của mình; 一己之私, lợi ích riêng."),
    ("让渡", "ràngdù", "nhượng độ", "động từ", "nhường lại, chuyển nhượng", "很多人为了便利，让渡了自己的隐私。", "Nhiều người vì tiện lợi mà nhường đi quyền riêng tư của mình.",
     "Động từ, nghĩa là nhường lại, chuyển giao quyền lợi, tài sản cho người khác. 让 là nhường, 渡 là chuyển qua. Hay gặp 让渡权利，让渡利益，让渡隐私."),
    ("授权", "shòuquán", "thụ quyền", "động từ", "ủy quyền, cấp quyền", "这个应用要求用户授权使用相机。", "Ứng dụng này yêu cầu người dùng cấp quyền sử dụng máy ảnh.",
     "Động từ, nghĩa là giao quyền cho người khác hay cơ quan khác thực hiện thay; trên điện thoại là cấp quyền truy cập. 授 là trao, như trong 授课, giảng bài."),
    ("卖身契", "màishēnqì", "mại thân khế", "danh từ", "văn tự bán thân", "这份合同简直就是一份卖身契。", "Bản hợp đồng này đúng là một văn tự bán thân.",
     "Danh từ, chỉ giấy tờ thời xưa, khi người nghèo bị ép bán thân, mất tự do. 契 là khế ước, văn tự, như 地契, văn tự đất. Trong bài, thỏa thuận cấp quyền trên mạng bị ví như văn tự bán thân, vì nó bắt người dùng giao hết quyền riêng tư."),
    ("陷阱", "xiànjǐng", "hãm tỉnh", "danh từ", "cạm bẫy, cái bẫy", "他不小心落入了骗子的陷阱。", "Anh ấy sơ ý rơi vào cạm bẫy của kẻ lừa đảo.",
     "Danh từ, nghĩa gốc là hố bẫy thú; nghĩa bóng là âm mưu, cái bẫy lừa người. Động từ đi kèm: 设陷阱, giăng bẫy; 落入陷阱, sa bẫy."),
    ("打勾", "dǎgōu", "đả câu", "động từ", "đánh dấu tích (✓)", "同意的话，请在方框里打勾。", "Nếu đồng ý, xin đánh dấu tích vào ô vuông.",
     "Động từ, nghĩa là đánh dấu tích, biểu thị chọn hoặc đồng ý. 勾 là dấu móc, dấu tích. Ngược lại, đánh dấu nhân là 打叉."),
    ("明细", "míngxì", "minh tế", "danh từ", "chi tiết các khoản, bảng kê chi tiết", "请把这个月的消费明细发给我。", "Hãy gửi cho tôi bảng kê chi tiêu tháng này.",
     "Danh từ, nghĩa là các hạng mục cụ thể, chi tiết, như 消费明细, chi tiết chi tiêu; 采购明细, chi tiết mua hàng. Trong bài, 授权明细 là danh sách chi tiết các quyền mà ứng dụng xin."),
    ("含糊", "hánhu", "hàm hồ", "tính từ", "mập mờ, không rõ ràng", "他回答得很含糊。", "Anh ta trả lời rất mập mờ.",
     "Tính từ, nghĩa là mập mờ, không rõ ràng, như 含糊不清. Từ dễ nhầm: tiếng Việt hàm hồ là nói năng bừa bãi, thiếu căn cứ; còn 含糊 là mập mờ, úp mở. Trong bài, 含糊地写个等字 là viết mập mờ một chữ vân vân."),
    ("缝", "fèng", "phùng", "danh từ", "khe, kẽ hở", "门开了一条小缝。", "Cửa hé mở một khe nhỏ.",
     "Danh từ, ở đây đọc thanh bốn, nghĩa là khe hở nhỏ, như 门缝, khe cửa. Khi đọc thanh hai, nó là động từ may vá, như 缝衣服. Trong bài, 开了一条小缝 là hé mở một khe nhỏ.", "凤"),
    ("有偿", "yǒucháng", "hữu thường", "tính từ", "có trả công, có thù lao", "这是一项有偿服务。", "Đây là một dịch vụ có thu phí.",
     "Tính từ, nghĩa là có trả giá, có thù lao. 偿 là đền bù, như trong bồi thường. Trái nghĩa là 无偿, không công, miễn phí."),
    ("识别", "shíbié", "thức biệt", "động từ", "nhận dạng, nhận biết", "现在很多手机都有人脸识别功能。", "Bây giờ nhiều điện thoại có chức năng nhận diện khuôn mặt.",
     "Động từ, nghĩa là phân biệt, nhận ra. Hay gặp 人脸识别, nhận diện khuôn mặt; 语音识别, nhận dạng giọng nói. Trong bài là 面部识别技术."),
    ("骑手", "qíshǒu", "kỵ thủ", "danh từ", "người giao đồ ăn (shipper)", "外卖骑手每天要送几十单。", "Shipper giao đồ ăn mỗi ngày phải giao mấy chục đơn.",
     "Danh từ, nghĩa gốc là người cưỡi ngựa, kỵ sĩ; ngày nay chỉ người giao đồ ăn đi xe máy, tức là shipper. Thường nói 外卖骑手."),
    ("差评", "chàpíng", "sai bình", "danh từ", "đánh giá xấu, đánh giá kém", "这家店服务不好，收到了很多差评。", "Cửa hàng này phục vụ kém nên nhận rất nhiều đánh giá xấu.",
     "Danh từ, nghĩa là lời đánh giá xấu khi mua hàng trên mạng. Chữ đầu đọc thanh bốn, nghĩa là kém. Động từ đi kèm là 给 hoặc 打: 打差评. Ngược lại là 好评, đánh giá tốt."),
    ("休止", "xiūzhǐ", "hưu chỉ", "động từ", "ngừng, dừng lại", "他们无休止地争吵。", "Họ cãi nhau không dứt.",
     "Động từ, nghĩa là ngừng, dừng lại. Hay gặp nhất là cụm 无休止, không ngừng, không dứt, như trong bài: 无休止的谩骂和恐吓. Âm nhạc có 休止符, dấu lặng."),
    ("谩骂", "mànmà", "mạn mạ", "động từ", "chửi bới, lăng mạ", "网上有人对她进行恶意谩骂。", "Trên mạng có người chửi bới cô ấy một cách ác ý.",
     "Động từ, nghĩa là chửi bới tùy tiện, lăng mạ. 骂 là chửi. Thường đi với 恶意, ác ý."),
    ("恐吓", "kǒnghè", "khủng hách", "động từ", "đe dọa, dọa dẫm", "他收到了一封恐吓信。", "Anh ấy nhận được một lá thư đe dọa.",
     "Động từ, nghĩa là đe dọa để người khác sợ. Chú ý chữ thứ hai ở đây đọc là hè, không đọc là xià. Hay gặp 恐吓信，恐吓电话."),
    ("韭菜", "jiǔcài", "cửu thái", "danh từ", "rau hẹ; (bóng) người bị bóc lột", "很多散户成了股市里的韭菜。", "Nhiều nhà đầu tư nhỏ lẻ trở thành 'rau hẹ' trên thị trường chứng khoán.",
     "Danh từ, nghĩa gốc là rau hẹ. Rau hẹ cắt rồi lại mọc, nên trên mạng Trung Quốc, 韭菜 chỉ những người bị bóc lột, bị lừa hết lần này đến lần khác, như nhà đầu tư nhỏ lẻ hay người tiêu dùng. Bị bóc lột gọi là 被割韭菜."),
    ("大佬", "dàlǎo", "đại lão", "danh từ", "ông lớn, ông trùm, đại gia", "几位互联网大佬出席了这次会议。", "Mấy ông lớn ngành Internet đã dự hội nghị này.",
     "Danh từ, vốn là từ địa phương, nghĩa là đại ca; nay chỉ người có ảnh hưởng lớn trong một ngành, như 商业大佬，行业大佬. Trong bài, 电商大佬 là các ông lớn thương mại điện tử."),
    ("殊不知", "shūbùzhī", "thù bất tri", "động từ", "nào ngờ, nào hay", "他以为自己很聪明，殊不知早被人看穿了。", "Hắn tưởng mình thông minh, nào ngờ đã bị người ta nhìn thấu từ lâu.",
     "Động từ, văn viết, nghĩa là nào ngờ, nào hay biết, dùng để sửa lại một suy nghĩ sai. Đây là mẫu câu trọng điểm thứ ba."),
    ("偏好", "piānhào", "thiên hiếu", "động từ", "đặc biệt ưa thích; sở thích riêng", "他从小就偏好京剧。", "Từ nhỏ anh ấy đã đặc biệt thích Kinh kịch.",
     "Động từ, nghĩa là đặc biệt ưa thích một thứ gì; cũng làm danh từ, nghĩa là sở thích riêng. Chữ thứ hai đọc thanh bốn. Trong bài, 个人偏好 là sở thích cá nhân."),
    ("悉数", "xīshù", "tất số", "phó từ", "toàn bộ, tất cả", "嘉宾们已经悉数到场。", "Các vị khách mời đều đã có mặt đầy đủ.",
     "Phó từ, văn viết, nghĩa là toàn bộ, không sót một ai, một thứ gì. Chữ sau đọc thanh bốn. Trong bài, 被大数据平台悉数掌握 là bị các nền tảng dữ liệu lớn nắm trọn."),
    ("无异于", "wúyìyú", "vô dị ư", "động từ", "chẳng khác gì, không khác gì", "酒后开车无异于拿生命开玩笑。", "Lái xe sau khi uống rượu chẳng khác gì đùa với tính mạng.",
     "Động từ, văn viết, nghĩa là không khác gì, nhấn mạnh hai việc giống hệt nhau. 异 là khác, như dị biệt. Đây là mẫu câu trọng điểm thứ tư."),
    ("仗着", "zhàngzhe", "trượng trước", "động từ", "cậy, ỷ vào", "他仗着父亲有钱，到处欺负人。", "Hắn cậy bố có tiền, đi đâu cũng bắt nạt người khác.",
     "Động từ, khẩu ngữ, nghĩa là cậy, ỷ vào, thường mang nghĩa chê. Tiếng Việt cũng có ỷ thế, cậy thế. Đây là mẫu câu trọng điểm thứ sáu."),
    ("可悲", "kěbēi", "khả bi", "tính từ", "đáng buồn, đáng thương", "最可悲的是，他到现在还不明白自己错在哪儿。", "Đáng buồn nhất là đến giờ anh ta vẫn không hiểu mình sai ở đâu.",
     "Tính từ, nghĩa là đáng buồn, khiến người ta đau lòng. Hay đứng đầu câu theo mẫu 可悲的是, điều đáng buồn là, như trong bài."),
    ("反面", "fǎnmiàn", "phản diện", "danh từ", "mặt trái; mặt ngược lại", "不但要看问题的正面，还要看问题的反面。", "Không chỉ nhìn mặt thuận, còn phải nhìn mặt trái của vấn đề.",
     "Danh từ, nghĩa là mặt trái, mặt đối lập với 正面. Tiếng Việt phản diện thường chỉ nhân vật xấu, tiếng Trung là 反面人物. Trong bài, 通往自由的反面 là dẫn đến mặt đối lập của tự do."),
    ("主义", "zhǔyì", "chủ nghĩa", "danh từ", "chủ nghĩa", "消费主义让很多年轻人负债累累。", "Chủ nghĩa tiêu dùng khiến nhiều người trẻ nợ nần chồng chất.",
     "Danh từ, nghĩa là chủ nghĩa, cũng chỉ lối hành xử, tác phong tư tưởng, như 自由主义，个人主义. Trong bài, 消费主义 là chủ nghĩa tiêu dùng, coi việc mua sắm là mục đích sống."),
    ("绑架", "bǎngjià", "bảng giá", "động từ", "bắt cóc; (bóng) trói buộc, khống chế", "不要用道德绑架别人。", "Đừng dùng đạo đức để ép buộc người khác.",
     "Động từ, nghĩa gốc là dùng vũ lực bắt cóc người. Nghĩa bóng là bị ép buộc, bị khống chế hành vi, như 道德绑架, ép buộc bằng đạo đức. Chú ý âm Hán Việt là bảng giá, nhưng không liên quan gì đến giá cả."),
    ("筛子", "shāizi", "si tử", "danh từ", "cái sàng, cái rây", "奶奶用筛子筛米。", "Bà dùng cái sàng để sàng gạo.",
     "Danh từ, nghĩa là cái sàng, đan bằng tre hoặc dây thép, có nhiều lỗ nhỏ để thứ nhỏ lọt xuống, thứ to ở lại. 筛 cũng làm động từ: sàng, lọc, như 筛选. Trong bài, Internet bị ví như 一个大筛子."),
    ("不乏", "bùfá", "bất phạp", "động từ", "không thiếu, có khá nhiều", "在众多科学家中，自学成才的也不乏其人。", "Trong số các nhà khoa học, người tự học thành tài cũng không thiếu.",
     "Động từ, văn viết, nghĩa là không thiếu, có số lượng khá nhiều. 乏 là thiếu, như trong 缺乏. Hay gặp 不乏其人, không thiếu người như thế; 不乏先例, không thiếu tiền lệ."),
    ("海量", "hǎiliàng", "hải lượng", "tính từ", "lượng cực lớn, khổng lồ", "互联网上有海量的信息。", "Trên Internet có lượng thông tin khổng lồ.",
     "Tính từ, nghĩa là số lượng cực lớn, như biển, như 海量信息，海量存储. Ngoài ra 海量 còn chỉ tửu lượng cao, hay lòng độ lượng; tiếng Việt hải lượng cũng có nghĩa rộng lượng."),
    ("泄露", "xièlòu", "tiết lộ", "động từ", "để lộ, rò rỉ", "他的个人信息被泄露了。", "Thông tin cá nhân của anh ấy đã bị rò rỉ.",
     "Động từ, nghĩa là để lộ ra điều không nên để người khác biết, như 泄露秘密，泄露消息. Chữ thứ hai ở đây đọc là lòu. Trong bài, 个人信息泄露 là rò rỉ thông tin cá nhân."),
    ("渺小", "miǎoxiǎo", "miểu tiểu", "tính từ", "nhỏ bé, nhỏ nhoi", "在大自然面前，人类显得十分渺小。", "Trước thiên nhiên, con người trở nên vô cùng nhỏ bé.",
     "Tính từ, nghĩa là rất nhỏ bé, không đáng kể. Trái nghĩa là 伟大, vĩ đại. Trong bài, 任何个人的力量都是渺小的 là sức của bất kỳ cá nhân nào cũng nhỏ bé."),
    ("尤为", "yóuwéi", "vưu vi", "phó từ", "càng, đặc biệt", "这一点尤为重要。", "Điểm này đặc biệt quan trọng.",
     "Phó từ, văn viết, nghĩa là đặc biệt, nổi bật hơn hẳn, thường đứng trước tính từ hoặc động từ hai âm tiết: 尤为重要，尤为必要. Chữ thứ hai đọc thanh hai."),
    ("审视", "shěnshì", "thẩm thị", "động từ", "xem xét kỹ, nhìn nhận lại", "我们应该重新审视这个问题。", "Chúng ta nên xem xét lại vấn đề này một cách kỹ lưỡng.",
     "Động từ, nghĩa là xem xét kỹ càng. 审 là thẩm, như thẩm định; 视 là nhìn. Hay gặp 重新审视, nhìn nhận lại."),
    ("切勿", "qièwù", "thiết vật", "phó từ", "tuyệt đối đừng, nhất định không được", "请切勿酒后开车。", "Xin tuyệt đối đừng lái xe sau khi uống rượu.",
     "Phó từ, văn viết, nghĩa là tuyệt đối đừng, hay gặp trên biển báo, thông báo. Chữ đầu đọc thanh bốn. Đây là mẫu câu trọng điểm cuối cùng."),
]

add("bullets", chapter="Từ mới (45 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 4.1 có 45 từ mới, chia thành 15 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 缝 (fèng) · 差评 (chà) · 恐吓 (hè) · 偏好 (hào) · 泄露 (lòu) · 切勿 (qiè)",
           "Từ dễ nhầm: 社交 · 含糊 · 反面 · 绑架"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có bốn mươi lăm từ, thầy chia thành mười lăm nhóm nhỏ, mỗi nhóm ba từ. Vì là bài bình luận về Internet, nên có nhiều từ văn viết và từ mới của mạng xã hội, như 骑手，差评，韭菜，大佬.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số chữ có nhiều cách đọc, các bạn cần chú ý cách đọc trong bài, như 差评，恐吓，偏好，泄露，切勿. Thầy sẽ nhắc khi gặp."),
         F(4, "Ngoài ra, có mấy từ Hán Việt rất dễ hiểu nhầm, như 社交，含糊，反面，绑架. Nghĩa của chúng trong tiếng Trung khác với tiếng Việt, các bạn nhớ nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

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
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung nếu khác])
P = [
    ("最近，湖北青年艺术家邓玉峰在武汉美术馆举办了一场个人展览，展览的东西有点特别：从黑市购买的34.6万条个人信息，包括姓名、电话、住址、银行存款等内容。一些信息细化到令人瞠目结舌的地步：除了基本的姓名住址，还有网购记录、购票记录、家用车发动机号等。",
     "Gần đây, nghệ sĩ trẻ người Hồ Bắc Đặng Ngọc Phong tổ chức một cuộc triển lãm cá nhân tại Bảo tàng Mỹ thuật Vũ Hán. Thứ được trưng bày có phần đặc biệt: 346 nghìn mẩu thông tin cá nhân mua từ chợ đen, gồm họ tên, số điện thoại, địa chỉ, tiền gửi ngân hàng... Có những thông tin chi tiết đến mức khiến người ta sững sờ: ngoài họ tên, địa chỉ, còn có lịch sử mua hàng qua mạng, lịch sử mua vé, cả số máy xe ô tô gia đình.",
     ["举办了一场个人展览 là tổ chức một cuộc triển lãm cá nhân, 场 là lượng từ cho sự kiện. 有点特别 là có phần đặc biệt. 三十四点六万条个人信息 là ba trăm bốn mươi sáu nghìn mẩu thông tin cá nhân; 条 là lượng từ cho tin tức, thông tin.",
      "细化到令人瞠目结舌的地步 là chi tiết đến mức khiến người ta trợn mắt líu lưỡi. Ở đây có mẫu câu 到什么地步 và thành ngữ 瞠目结舌, lát nữa ta sẽ học kỹ. 网购记录 là lịch sử mua hàng qua mạng, 发动机号 là số máy, số động cơ."],
     "最近，湖北青年艺术家邓玉峰在武汉美术馆举办了一场个人展览，展览的东西有点特别：从黑市购买的三十四点六万条个人信息，包括姓名、电话、住址、银行存款等内容。一些信息细化到令人瞠目结舌的地步：除了基本的姓名住址，还有网购记录、购票记录、家用车发动机号等。"),
    ("好奇的记者询问邓玉峰一条信息的最低价格，艺术家给出的答案是：“一分钱。”原来只用花一分钱，就能买到一个人这么多的秘密。",
     "Phóng viên tò mò hỏi Đặng Ngọc Phong giá thấp nhất của một mẩu thông tin, câu trả lời của nghệ sĩ là: 'Một xu.' Thì ra chỉ cần bỏ ra một xu là có thể mua được ngần ấy bí mật của một con người.",
     ["询问 là hỏi, văn viết. 一分钱 là một xu: 分 là đơn vị tiền nhỏ nhất của Trung Quốc, bằng một phần trăm tệ. Đây chính là hình ảnh trong tên bài.",
      "原来 là thì ra, chỉ sự vỡ lẽ. 只用花一分钱，就能 là chỉ cần bỏ ra một xu là có thể, nhấn mạnh cái giá rẻ đến khó tin của đời tư một con người."]),
    ("开展前邓玉峰还找来了几个志愿者，给这些信息的主人发短信，邀请他们来观看这场展览。但在开展当天上午，只收到了一条回复：“有病吧！”",
     "Trước khi khai mạc, Đặng Ngọc Phong còn tìm mấy tình nguyện viên gửi tin nhắn cho chủ nhân của những thông tin này, mời họ đến xem triển lãm. Nhưng sáng hôm khai mạc, chỉ nhận được đúng một tin trả lời: 'Bị điên à!'",
     ["开展 ở đây là mở cửa triển lãm, tức là 展览开幕. Chú ý: thông thường 开展 nghĩa là triển khai, như 开展活动; nhưng trong bài là khai mạc triển lãm. 志愿者 là tình nguyện viên.",
      "有病吧 là câu mắng khẩu ngữ: có bệnh à, bị điên à. Chi tiết này vừa buồn cười vừa chua xót: người ta tưởng đó là tin nhắn rác, chẳng ai quan tâm thông tin của mình đã bị bán."]),
    ("【我们是不是对隐私太大方了？】\n身在中国，我们常常听到一种声音：大洋彼岸的老外对于隐私太小气，连问个生日、年龄、工作都得小心翼翼。然而，反过来想，是不是我们对隐私太大方了呢？",
     "[Có phải chúng ta quá hào phóng với quyền riêng tư?] Sống ở Trung Quốc, ta thường nghe một luồng ý kiến: người nước ngoài bên kia đại dương quá 'keo kiệt' chuyện riêng tư, đến hỏi ngày sinh, tuổi tác, công việc thôi cũng phải dè dặt từng li từng tí. Thế nhưng nghĩ ngược lại, phải chăng chúng ta quá hào phóng với quyền riêng tư?",
     ["Đây là tiểu mục thứ nhất của bài. 大方 là hào phóng, đối lập với 小气, keo kiệt. Tác giả dùng cặp từ này một cách dí dỏm khi nói về thái độ với quyền riêng tư.",
      "老外 là người nước ngoài, khẩu ngữ. 连问个生日都得小心翼翼: mẫu 连……都…… nghĩa là ngay cả… cũng…, còn 小心翼翼 là thận trọng từng li từng tí. 反过来想 là nghĩ ngược lại."]),
    ("打开手机，看看垃圾短信划几下才能划到头？打开邮箱，广告邮件是不是多到删都懒得删？更不要说无数骚扰电话，一张口就能准确地报上你的姓氏。",
     "Mở điện thoại ra, thử xem phải vuốt bao nhiêu lần mới hết tin nhắn rác? Mở hộp thư, có phải thư quảng cáo nhiều đến mức xóa cũng chẳng buồn xóa? Chưa kể vô số cuộc gọi làm phiền, vừa mở miệng đã gọi đúng họ của bạn.",
     ["垃圾短信 là tin nhắn rác. 划 là vuốt màn hình, 划到头 là vuốt đến cuối. 多到删都懒得删 là nhiều đến mức xóa cũng chẳng buồn xóa, đây là mẫu câu V都懒得V.",
      "更不要说 là chưa kể, huống chi. 骚扰电话 là cuộc gọi làm phiền. 一张口 là vừa mở miệng. 报上你的姓氏 là nói ra đúng họ của bạn. Ba câu hỏi liên tiếp cho thấy thông tin của chúng ta đã lộ hết."]),
    ("身处互联网社会中的我们，很难像过去一样，把自己包裹起来，独善其身。网速升级短短几年，我们的个人信息就像洪水一样决堤而出，外卖网站、网购平台、社交软件……到处都是防不胜防的漏洞，单凭一己之力，永远不可能堵得上。",
     "Sống trong xã hội Internet, chúng ta khó có thể như ngày trước, bọc kín mình lại mà đứng ngoài mọi chuyện. Tốc độ mạng mới nâng cấp có mấy năm ngắn ngủi, thông tin cá nhân của chúng ta đã như nước lũ vỡ đê tuôn ra: trang giao đồ ăn, nền tảng mua sắm, ứng dụng mạng xã hội... đâu đâu cũng là lỗ hổng phòng không xuể, chỉ dựa vào sức một người thì mãi mãi không thể bịt kín.",
     ["身处 là đặt mình ở, sống trong. 包裹起来 là bọc kín lại. 独善其身 là thành ngữ, nghĩa gốc là tự giữ mình trong sạch, ở đây là chỉ lo cho riêng mình, đứng ngoài mọi chuyện.",
      "决堤而出 là vỡ đê tuôn ra, ví thông tin rò rỉ như lũ. 防不胜防 là phòng không xuể. 单凭一己之力 là chỉ dựa vào sức một người. 堵得上 là bịt được, bổ ngữ khả năng; 永远不可能堵得上 là mãi mãi không thể bịt kín."]),
    ("百度老总李彦宏其实说得没错，短短数年，我们已经适应了“互联网+”的生活，很多人为了便利，部分地让渡了自己的隐私权。",
     "Sếp tổng Baidu Lý Ngạn Hoằng thật ra nói không sai: chỉ trong mấy năm ngắn ngủi, chúng ta đã quen với cuộc sống 'Internet+', nhiều người vì tiện lợi mà đã nhường đi một phần quyền riêng tư của mình.",
     ["百度 là Baidu, công cụ tìm kiếm lớn nhất Trung Quốc, 老总 là sếp tổng. Năm hai nghìn không trăm mười tám, ông 李彦宏 từng gây tranh cãi khi nói rằng người Trung Quốc sẵn lòng đổi quyền riêng tư lấy sự tiện lợi.",
      "互联网加 là Internet cộng, chủ trương kết hợp Internet với mọi ngành nghề. 部分地让渡了自己的隐私权 là nhường đi một phần quyền riêng tư; 让渡 là chuyển nhượng, nhường lại."],
     "百度老总李彦宏其实说得没错，短短数年，我们已经适应了互联网加的生活，很多人为了便利，部分地让渡了自己的隐私权。"),
    ("【互联网授权协议成了“卖身契”】\n那些在屏幕上一闪而过的用户协议，会不会藏着什么陷阱呢？",
     "[Thỏa thuận cấp quyền trên mạng thành 'văn tự bán thân'] Những bản thỏa thuận người dùng lướt qua trong chớp mắt trên màn hình, liệu có giấu cạm bẫy nào không?",
     ["Đây là tiểu mục thứ hai. 授权协议 là thỏa thuận cấp quyền. 卖身契 là văn tự bán thân: sách chú thích, ở đây nó chỉ những thỏa thuận bắt người dùng bán đi quyền riêng tư với điều kiện vô lý.",
      "一闪而过 là vụt qua trong chớp mắt: ai cũng bấm đồng ý mà không đọc. 藏着什么陷阱 là giấu cạm bẫy gì đó. Câu hỏi này dẫn vào ví dụ ở đoạn sau."]),
    ("最典型的例子就是，很多应用让用户打勾授权，但授权明细后面只是含糊地写个“等”字，你以为你只是开了一条小缝，但其实推开的是一扇大门，可以让他人堂而皇之地收集你的个人信息。",
     "Ví dụ điển hình nhất là nhiều ứng dụng bắt người dùng đánh dấu tích để cấp quyền, nhưng cuối danh sách quyền chỉ viết mập mờ một chữ 'v.v.'. Bạn tưởng mình chỉ hé một khe cửa nhỏ, nhưng thật ra là đẩy toang cả một cánh cổng lớn, để người khác ngang nhiên thu thập thông tin cá nhân của bạn.",
     ["打勾授权 là đánh dấu tích để cấp quyền. 授权明细 là danh sách chi tiết các quyền. 含糊地写个等字 là viết mập mờ một chữ 等, vân vân: chữ này có thể bao gồm mọi thứ.",
      "开了一条小缝 là hé một khe nhỏ, 推开的是一扇大门 là đẩy toang một cánh cổng lớn: hình ảnh so sánh rất rõ. 堂而皇之 là thành ngữ, nghĩa là công khai, ngang nhiên, mang nghĩa chê."]),
    ("近日，一些居心不良者在网上发布有偿任务，如从各个角度自拍30张照片发给对方即可获得30元报酬，如果联系到最近大热的面部识别技术，不能不让人对其真实目的产生怀疑。",
     "Gần đây, một số kẻ có ý đồ xấu đăng nhiệm vụ có trả công trên mạng, chẳng hạn tự chụp 30 tấm ảnh từ các góc độ khác nhau gửi cho họ là nhận được 30 tệ tiền công. Nếu liên hệ với công nghệ nhận diện khuôn mặt đang rất thịnh hành gần đây, không thể không khiến người ta nghi ngờ mục đích thật sự của họ.",
     ["居心不良者 là kẻ có ý đồ xấu: 居心不良 là thành ngữ, 者 là người. 有偿任务 là nhiệm vụ có trả công. 即可 là thì có thể, văn viết, bằng 就可以.",
      "大热 là đang rất nóng, rất thịnh hành. 面部识别 là nhận diện khuôn mặt. 不能不让人怀疑 là phủ định kép: không thể không khiến người ta nghi ngờ, tức là chắc chắn đáng ngờ. 其 là của họ."],
     "近日，一些居心不良者在网上发布有偿任务，如从各个角度自拍三十张照片发给对方即可获得三十元报酬，如果联系到最近大热的面部识别技术，不能不让人对其真实目的产生怀疑。"),
    ("还有媒体报道过，一位女士因为给外卖骑手打了差评，遭到对方无休止的谩骂和恐吓。而对方正是根据外卖信息上的地址电话一路找来的。",
     "Còn có báo chí đưa tin, một phụ nữ vì đánh giá xấu một shipper giao đồ ăn mà bị người đó chửi bới, đe dọa không ngớt. Mà người đó chính là lần theo địa chỉ, số điện thoại trên đơn đồ ăn để tìm đến tận nơi.",
     ["打了差评 là cho đánh giá xấu. 遭到 là gặp phải, bị, luôn đi với điều không may. 无休止的谩骂和恐吓 là những lời chửi bới, đe dọa không dứt.",
      "正是 là chính là. 一路找来 là lần theo suốt dọc đường mà tìm đến. Ví dụ này cho thấy thông tin bị lộ có thể đe dọa cả sự an toàn của bản thân."]),
    ("这不禁让人担忧，大量的购物网站掌握了用户的私人信息，如何保证这些信息不被非法利用呢？有了这样的前车之鉴，用户在评价商品时，还能理直气壮地有一说一吗？",
     "Điều này không khỏi khiến người ta lo lắng: rất nhiều trang mua sắm nắm trong tay thông tin cá nhân của người dùng, làm sao bảo đảm những thông tin ấy không bị sử dụng trái phép? Đã có bài học nhãn tiền như vậy, khi đánh giá sản phẩm, người dùng còn dám đường hoàng có sao nói vậy nữa không?",
     ["不禁 là không kìm được, không khỏi. 担忧 là lo lắng. 非法利用 là sử dụng trái phép.",
      "前车之鉴 là xe trước đổ, xe sau lấy đó làm gương, tức là vết xe đổ, bài học nhãn tiền. 理直气壮 là lý lẽ vững vàng nên tự tin. 有一说一 là có sao nói vậy. Câu hỏi tu từ ngụ ý: người dùng sẽ không dám đánh giá thật lòng nữa."]),
    ("【别当了韭菜还不自知】\n根据对中国网络购物市场的预测，2018年网络购物用户数量将超过6亿。电商大佬们借着大数据的东风，可能比你更懂你自己。",
     "[Đừng làm 'rau hẹ' mà không hay biết] Theo dự báo về thị trường mua sắm trực tuyến Trung Quốc, năm 2018 số người mua sắm qua mạng sẽ vượt 600 triệu. Các ông lớn thương mại điện tử nhờ 'ngọn gió đông' của dữ liệu lớn, có khi còn hiểu bạn hơn chính bạn.",
     ["Đây là tiểu mục thứ ba. 当了韭菜 là làm rau hẹ: rau hẹ cắt rồi lại mọc, ví người bị bóc lột hết lần này đến lần khác. 不自知 là không tự biết.",
      "电商 là thương mại điện tử. 大佬 là ông lớn. 借着大数据的东风: sách chú thích, 借东风 là điển tích Gia Cát Lượng mượn gió đông trong Tam Quốc, nay chỉ tận dụng thời thế thuận lợi. 比你更懂你自己 là hiểu bạn hơn chính bạn."],
     "别当了韭菜还不自知。根据对中国网络购物市场的预测，二零一八年网络购物用户数量将超过六亿。电商大佬们借着大数据的东风，可能比你更懂你自己。"),
    ("当我们享受着线上购物的便利时，殊不知我们的生活方式、个人偏好乃至通讯地址都被大数据平台悉数掌握，无异于在各大平台上裸奔，毫无隐私可言。",
     "Khi chúng ta tận hưởng sự tiện lợi của mua sắm trực tuyến, nào ngờ lối sống, sở thích cá nhân, thậm chí cả địa chỉ liên lạc của mình đều đã bị các nền tảng dữ liệu lớn nắm trọn, chẳng khác gì 'khỏa thân chạy' trên các nền tảng lớn, chẳng còn chút riêng tư nào.",
     ["殊不知 là nào ngờ. 个人偏好 là sở thích cá nhân. 乃至 là thậm chí, cho đến cả. 悉数掌握 là nắm trọn toàn bộ. Chỉ một câu này đã chứa ba mẫu câu trọng điểm: 殊不知，无异于，毫无什么可言.",
      "裸奔: sách chú thích, nghĩa gốc là cởi hết quần áo mà chạy, ở đây ví thông tin cá nhân không được bảo vệ chút nào. 毫无隐私可言 là chẳng có chút riêng tư nào để mà nói."]),
    ("一些不良商家，仗着手握用户信息，不再下功夫提升服务水平，反正服务和产品再烂，都能赚得盆满钵满。",
     "Một số thương nhân bất lương, cậy mình nắm trong tay thông tin người dùng, không còn chịu bỏ công nâng cao chất lượng dịch vụ, dù sao thì dịch vụ và sản phẩm có tệ đến đâu cũng vẫn kiếm bộn tiền.",
     ["不良商家 là thương nhân làm ăn bất chính. 仗着手握用户信息 là cậy mình nắm thông tin người dùng; 仗着 là ỷ vào, mang nghĩa chê. 下功夫 là bỏ công sức.",
      "反正 là dù sao thì. 再烂，都能: mẫu 再 cộng tính từ cộng 都 nghĩa là dù có… đến đâu cũng…; 烂 là tệ, dở, khẩu ngữ. 赚得盆满钵满 là kiếm đầy chậu đầy bát, tức là kiếm bộn tiền."]),
    ("可悲的是，很多用户当了任人宰割的韭菜还不自知，这种唾手可得的“方便”让我们产生了“自由”的错觉，然而“方便”非但不是“自由”的替代品，反而可能带我们通往“自由”的反面，被消费主义绑架。",
     "Đáng buồn là nhiều người dùng đã làm 'rau hẹ' mặc người chém giết mà vẫn không hay biết. Thứ 'tiện lợi' dễ như trở bàn tay này khiến ta có ảo giác về 'tự do'; thế nhưng 'tiện lợi' chẳng những không phải là thứ thay thế cho 'tự do', mà ngược lại còn có thể dẫn ta tới mặt đối lập của 'tự do': bị chủ nghĩa tiêu dùng trói buộc.",
     ["任人宰割 là mặc người chém giết, không sức chống cự. 唾手可得 là dễ như trở bàn tay, nghĩa đen là nhổ nước bọt vào tay là có được. 错觉 là ảo giác, cảm nhận sai.",
      "非但不是，反而 là chẳng những không phải, mà ngược lại còn, mẫu câu trọng điểm thứ bảy. 被消费主义绑架 là bị chủ nghĩa tiêu dùng bắt cóc, tức là bị nó khống chế, điều khiển."]),
    ("连接世界的互联网，可能正在成为信息的一个大筛子。泥沙俱下之中，不乏海量的个人信息泄露。在它面前，任何个人的力量都是渺小的，对此制度的约束尤为必要。",
     "Mạng Internet kết nối thế giới có lẽ đang trở thành một cái sàng thông tin khổng lồ. Giữa cảnh bùn cát cùng trôi, không thiếu những vụ rò rỉ thông tin cá nhân với số lượng cực lớn. Trước nó, sức lực của bất kỳ cá nhân nào cũng thật nhỏ bé, vì vậy sự ràng buộc bằng chế độ, luật lệ càng đặc biệt cần thiết.",
     ["一个大筛子 là một cái sàng lớn: thông tin lọt qua vô số lỗ nhỏ. 泥沙俱下 là bùn cát cùng trôi xuống, ví tốt xấu lẫn lộn. 不乏 là không thiếu. 海量 là số lượng cực lớn.",
      "渺小 là nhỏ bé. 对此 là đối với việc này. 制度的约束 là sự ràng buộc của chế độ, quy định. 尤为必要 là đặc biệt cần thiết. Đây là giải pháp tác giả đề xuất: cá nhân không đủ sức, cần có luật pháp."]),
    ("而作为千百年来习惯了连“你吃了吗”都要问一问的普通中国人，实在应该重新审视个人隐私这个问题了。",
     "Còn với những người Trung Quốc bình thường, vốn quen từ hàng nghìn năm nay đến câu 'Ăn cơm chưa?' cũng phải hỏi một tiếng, thì thật sự nên nhìn nhận lại vấn đề quyền riêng tư cá nhân rồi.",
     ["作为 là với tư cách là. 千百年来 là từ hàng nghìn năm nay. 你吃了吗 là câu chào truyền thống của người Trung Quốc, giống câu Ăn cơm chưa của người Việt. Ý tác giả: người Trung Quốc vốn quen quan tâm chuyện của nhau, ít để ý ranh giới riêng tư.",
      "实在应该 là thật sự nên. 重新审视 là xem xét lại một cách kỹ lưỡng. Chữ 了 cuối câu nhấn mạnh: đã đến lúc phải làm việc này rồi."]),
    ("身处互联网时代的中国人，对每条个人信息都应当重视起来，切勿放弃这个权利，否则总有一天，你的隐私将连一分钱都不值。",
     "Người Trung Quốc sống trong thời đại Internet cần coi trọng từng mẩu thông tin cá nhân của mình, tuyệt đối đừng từ bỏ quyền lợi này; nếu không, sẽ có một ngày quyền riêng tư của bạn đến một xu cũng chẳng đáng.",
     ["应当重视起来 là cần bắt đầu coi trọng; 起来 chỉ sự bắt đầu một trạng thái. 切勿放弃这个权利 là tuyệt đối đừng từ bỏ quyền này, 切勿 là mẫu câu trọng điểm cuối cùng.",
      "否则 là nếu không thì. 总有一天 là rồi sẽ có một ngày. 连一分钱都不值 là đến một xu cũng không đáng: bài khép lại bằng chính hình ảnh một xu ở tên bài, rất chặt chẽ."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 真的，你的隐私只值一分钱！", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Bài có 3 tiểu mục (【……】), đọc kỹ để nắm lập luận",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa. Bài được cải biên từ một bài viết đăng tháng tư năm hai nghìn không trăm mười tám trên tài khoản chính thức của tạp chí 新周刊, Tân Chu San.",
         F(0, f"Thầy chia bài thành {len(P)} đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Bài bình luận này có ba tiểu mục, thầy đặt trong ngoặc vuông. Các bạn chú ý cách tác giả dẫn dắt: từ một cuộc triển lãm, đến thói quen của chúng ta, rồi đến các thỏa thuận cấp quyền, và cuối cùng là nền tảng thương mại điện tử."),
         F(3, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh
    spoken = spoken.replace("“", "").replace("”", "").replace("【", "").replace("】", "。").replace("\n", "")
    zsize = 54 if len(zh) <= 100 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Bố cục bài khóa", section="Bài khóa 课文", title="Bố cục và lập luận của bài", size=34,
    items=["## Mở bài: triển lãm 34,6 vạn mẩu thông tin – mỗi mẩu 一分钱",
           "Nêu hiện tượng gây sốc → 只用花一分钱，就能买到一个人这么多的秘密",
           "## Ba tiểu mục (thân bài)",
           "(1) 我们是不是对隐私太大方了？ – tin rác, cuộc gọi rác; 让渡了自己的隐私权",
           "(2) 互联网授权协议成了“卖身契” – chữ “等”, ảnh tự chụp, shipper đe dọa",
           "(3) 别当了韭菜还不自知 – nền tảng nắm hết thông tin, 被消费主义绑架",
           "## Kết bài: 制度的约束尤为必要 · 切勿放弃这个权利"],
    say=["Đọc xong bài khóa, chúng ta cùng nhìn lại bố cục. Đây là một bài bình luận điển hình, rất đáng học khi viết luận.",
         F(0, "Mở bài: một hiện tượng gây sốc, cuộc triển lãm ba mươi tư vạn sáu nghìn mẩu thông tin cá nhân mua từ chợ đen."),
         F(1, "Câu then chốt: 只用花一分钱，就能买到一个人这么多的秘密。 Chỉ cần một xu là mua được ngần ấy bí mật của một người. Con số một xu tạo ấn tượng rất mạnh."),
         F(2, "Thân bài gồm ba tiểu mục, mỗi tiểu mục là một câu hỏi hoặc một lời cảnh báo."),
         F(3, "Tiểu mục một tự vấn: phải chăng chúng ta quá hào phóng với quyền riêng tư? Dẫn chứng là tin nhắn rác, cuộc gọi rác; kết luận là nhiều người vì tiện lợi mà nhường đi quyền riêng tư."),
         F(4, "Tiểu mục hai chỉ ra cạm bẫy của thỏa thuận cấp quyền, với ba ví dụ: chữ 等 mập mờ, nhiệm vụ tự chụp ba mươi tấm ảnh, và chuyện shipper đe dọa khách hàng."),
         F(5, "Tiểu mục ba cảnh báo: đừng làm rau hẹ mà không biết. Các nền tảng nắm hết thông tin, thương nhân bất lương không cần nâng cao dịch vụ, và người dùng bị chủ nghĩa tiêu dùng trói buộc."),
         F(6, "Kết bài đưa ra giải pháp từ hai phía: xã hội cần sự ràng buộc của luật lệ, còn mỗi cá nhân tuyệt đối đừng từ bỏ quyền riêng tư. Cách viết này đi từ hiện tượng, đến phân tích, rồi đến giải pháp, các bạn có thể áp dụng khi viết bài nghị luận.")])

# ======================= MẪU CÂU TRỌNG ĐIỂM =======================
add("bullets", chapter="Mẫu câu: 到……地步 · 懒得", section="Mẫu câu 重点句型", title="1. V到……地步 – đến mức, đến nông nỗi", size=36,
    items=["Chỉ tình cảnh, mức độ đạt tới; thường là tình cảnh xấu, tiêu cực",
           "Hay gặp: 到……的地步 · 落到……地步 · 发展到……地步",
           "(1) 一些信息细化到令人瞠目结舌的地步。",
           "(2) 曾经的他多么风光，真没想到现在会落到现在这个地步。",
           "(3) 你们的关系发展到今天的地步，两个人都是有责任的。"],
    say=["Bây giờ chúng ta sang phần mẫu câu trọng điểm, tiếng Trung là 重点句型与词汇. Sách đưa ra chín mẫu câu, tất cả đều lấy từ bài khóa.",
         F(0, "Mẫu thứ nhất: động từ cộng 到什么地步. Nó chỉ một tình cảnh hay một mức độ đã đạt tới, phần lớn là tình cảnh xấu, tiêu cực. Tiếng Việt dịch là đến mức, đến nông nỗi."),
         F(1, "Hay gặp các cụm: 到什么的地步，落到什么地步，发展到什么地步. Riêng 落到这个地步 là sa sút đến nông nỗi này."),
         F(2, "Ví dụ một, lấy từ bài khóa: 一些信息细化到令人瞠目结舌的地步。 Có những thông tin chi tiết đến mức khiến người ta trợn mắt líu lưỡi."),
         F(3, "Ví dụ hai: 曾经的他多么风光，真没想到现在会落到现在这个地步。 Anh ta từng vẻ vang biết bao, thật không ngờ bây giờ lại sa sút đến nông nỗi này. 风光 ở đây là vẻ vang, oai phong."),
         F(4, "Ví dụ ba: 你们的关系发展到今天的地步，两个人都是有责任的。 Quan hệ của hai người đi đến tình cảnh như hôm nay, cả hai đều có trách nhiệm.")])

add("bullets", section="Mẫu câu 重点句型", title="2. (连)V都懒得V – (ngay cả) … cũng chẳng buồn …", size=36,
    items=["Khẩu ngữ: không muốn, chẳng buồn làm việc gì; lặp lại cùng một động từ",
           "Thường gặp: 多到 / ……得 + V都懒得V; 连 + V + 都懒得 + V",
           "(1) 打开邮箱，广告邮件是不是多到删都懒得删？",
           "(2) 到后来我们连吵都懒得吵了，干脆各过各的。",
           "(3) 他现在看都懒得看她一眼，觉得她已经没救了。"],
    say=[F(0, "Mẫu thứ hai: 连 cộng động từ, 都懒得, rồi lặp lại động từ đó. Đây là cách nói khẩu ngữ, nghĩa là ngay cả làm việc đó cũng chẳng buồn làm, thể hiện sự chán nản hoặc coi thường."),
         F(1, "Chữ 连 có thể lược bỏ. Phía trước thường có một nguyên nhân, như 多到, nhiều đến mức."),
         F(2, "Ví dụ một, lấy từ bài khóa: 打开邮箱，广告邮件是不是多到删都懒得删？ Mở hộp thư, có phải thư quảng cáo nhiều đến mức xóa cũng chẳng buồn xóa?"),
         F(3, "Ví dụ hai: 到后来我们连吵都懒得吵了，干脆各过各的。 Về sau chúng tôi đến cãi nhau cũng chẳng buồn cãi nữa, dứt khoát ai sống đời nấy. Các bạn thấy không, chẳng buồn cãi nhau còn đáng sợ hơn cãi nhau."),
         F(4, "Ví dụ ba: 他现在看都懒得看她一眼，觉得她已经没救了。 Bây giờ anh ta đến liếc cô ấy một cái cũng chẳng buồn, cho rằng cô ấy hết thuốc chữa rồi.")])

add("bullets", chapter="Mẫu câu: 殊不知 · 无异于 · 毫无……可言", section="Mẫu câu 重点句型", title="3. 殊不知 – nào ngờ, nào hay", size=34,
    items=["Biểu thị chuyển ý: sửa lại ý kiến của người khác (竟不知道), hoặc suy nghĩ ban đầu của chính mình (竟没有想到)",
           "Vế trước thường có 以为 / 认为 (tưởng rằng…)",
           "(1) 当我们享受着线上购物的便利时，殊不知我们的生活方式、个人偏好乃至通讯地址都被大数据平台悉数掌握……",
           "(2) 有人以为喝酒可以御寒，殊不知酒劲一过，更觉得冷。",
           "(3) 我以为他还在北京，殊不知上星期他就走了。"],
    say=[F(0, "Mẫu thứ ba: 殊不知. Nó biểu thị sự chuyển ý, có hai cách dùng. Một là dẫn lại ý kiến của người khác rồi sửa lại, nghĩa là họ đâu biết rằng. Hai là sửa lại suy nghĩ ban đầu của chính mình, nghĩa là nào ngờ."),
         F(1, "Vế trước thường có 以为 hoặc 认为, tưởng rằng, cho rằng. Vế sau dùng 殊不知 để nói ra sự thật."),
         F(2, "Ví dụ một, lấy từ bài khóa: 当我们享受着线上购物的便利时，殊不知我们的生活方式、个人偏好乃至通讯地址都被大数据平台悉数掌握。 Khi ta tận hưởng tiện lợi của mua sắm trực tuyến, nào ngờ lối sống, sở thích, thậm chí địa chỉ liên lạc đều đã bị nắm trọn."),
         F(3, "Ví dụ hai: 有人以为喝酒可以御寒，殊不知酒劲一过，更觉得冷。 Có người tưởng uống rượu thì chống được rét, đâu biết rằng hết hơi men lại càng thấy lạnh hơn. Đây là cách dùng thứ nhất: sửa ý kiến của người khác."),
         F(4, "Ví dụ ba: 我以为他还在北京，殊不知上星期他就走了。 Tôi tưởng anh ấy vẫn còn ở Bắc Kinh, nào ngờ tuần trước anh ấy đã đi rồi. Đây là cách dùng thứ hai: sửa suy nghĩ của chính mình.")])

add("bullets", section="Mẫu câu 重点句型", title="4. 无异于 – chẳng khác gì · 5. 毫无……可言 – chẳng có chút … nào", size=34,
    items=["## 无异于 + cụm từ: nhấn mạnh hai việc giống nhau, không khác biệt",
           "……悉数掌握，无异于在各大平台上裸奔……",
           "(2) 两个人吵架的时候翻旧账，无异于火上浇油。",
           "(3) 没有目标的努力无异于在茫茫黑暗中前行。",
           "## 毫无 + danh từ trừu tượng + 可言: hoàn toàn không có gì đáng gọi là …",
           "……无异于在各大平台上裸奔，毫无隐私可言。",
           "(2) 明明已经答应的事情，现在他又反悔了，真的是毫无信用可言。",
           "(3) 我每天都是家和公司两点一线，生活毫无乐趣可言。"],
    say=[F(0, "Mẫu thứ tư: 无异于. Nó đứng trước một cụm từ, nhấn mạnh việc này với việc kia không có gì khác nhau. Tiếng Việt dịch là chẳng khác gì, không khác nào. Thường dùng để phê phán, cảnh báo."),
         F(1, "Trong bài khóa: 悉数掌握，无异于在各大平台上裸奔。 Bị nắm trọn thông tin, chẳng khác gì khỏa thân chạy trên các nền tảng lớn."),
         F(2, "Ví dụ hai: 两个人吵架的时候翻旧账，无异于火上浇油。 Lúc hai người cãi nhau mà lôi chuyện cũ ra, chẳng khác gì đổ thêm dầu vào lửa. 翻旧账 là lật lại sổ cũ, tức là nhắc lại chuyện cũ."),
         F(3, "Ví dụ ba: 没有目标的努力无异于在茫茫黑暗中前行。 Nỗ lực mà không có mục tiêu chẳng khác gì đi trong bóng tối mênh mông."),
         F(4, "Mẫu thứ năm: 毫无 cộng một danh từ trừu tượng cộng 可言. Nghĩa là hoàn toàn không có chút gì đáng để nói đến. 毫无 là không hề có, còn 可言 là có thể nói đến."),
         F(5, "Trong bài khóa: 无异于在各大平台上裸奔，毫无隐私可言。 Chẳng còn chút riêng tư nào."),
         F(6, "Ví dụ hai: 明明已经答应的事情，现在他又反悔了，真的是毫无信用可言。 Việc rõ ràng đã nhận lời, giờ anh ta lại nuốt lời, đúng là chẳng có chút chữ tín nào."),
         F(7, "Ví dụ ba: 我每天都是家和公司两点一线，生活毫无乐趣可言。 Ngày nào tôi cũng chỉ đi về giữa hai điểm nhà và công ty, cuộc sống chẳng có chút niềm vui nào. 两点一线 là cuộc sống chỉ quanh quẩn hai điểm, rất đơn điệu.")])

add("bullets", chapter="Mẫu câu: 仗着 · 非但不……反而", section="Mẫu câu 重点句型", title="6. 仗着…… – cậy, ỷ vào (nghĩa chê)", size=36,
    items=["Khẩu ngữ: dựa vào, ỷ vào một điều kiện nào đó (tiền, quyền, đông người…) để làm việc không tốt",
           "Cấu trúc: (chủ ngữ +) 仗着 + điều kiện, + hành động",
           "(1) 一些不良商家，仗着手握用户信息，不再下功夫提升服务水平……",
           "(2) 这几年他仗着父亲有钱有势，消费大手大脚。",
           "(3) 他们仗着人多欺负弱小，应该受到惩罚。"],
    say=[F(0, "Mẫu thứ sáu: 仗着. Đây là cách nói khẩu ngữ, nghĩa là dựa vào, ỷ vào một điều kiện nào đó, như tiền bạc, quyền thế hay số đông, để làm việc không tốt. Vì vậy nó thường mang nghĩa chê."),
         F(1, "Cấu trúc: 仗着 cộng điều kiện, rồi đến hành động. Tiếng Việt có cách nói tương tự: cậy thế, ỷ thế."),
         F(2, "Ví dụ một, lấy từ bài khóa: 一些不良商家，仗着手握用户信息，不再下功夫提升服务水平。 Một số thương nhân bất lương cậy mình nắm thông tin người dùng, không chịu bỏ công nâng cao dịch vụ."),
         F(3, "Ví dụ hai: 这几年他仗着父亲有钱有势，消费大手大脚。 Mấy năm nay anh ta cậy bố có tiền có thế, tiêu xài vung tay quá trán. 大手大脚 là tiêu tiền phung phí."),
         F(4, "Ví dụ ba: 他们仗着人多欺负弱小，应该受到惩罚。 Bọn họ cậy đông người bắt nạt kẻ yếu, đáng bị trừng phạt.")])

add("bullets", section="Mẫu câu 重点句型", title="7. ……，然而……非但不/没有……，反而……", size=34,
    items=["Câu phức chuyển ý: kết quả trái hẳn với điều đáng lẽ phải xảy ra",
           "非但不 A，反而 B: chẳng những không A, mà ngược lại còn B",
           "(1) 然而“方便”非但不是“自由”的替代品，反而可能带我们通往“自由”的反面，被消费主义绑架。",
           "(2) 我帮了他的忙，然而我帮了他，他非但不感谢我，反而责怪起我。",
           "(3) 这件事明明是他的过错，然而他非但不认错，反而把责任推给别人。"],
    say=[F(0, "Mẫu thứ bảy là một câu phức chuyển ý: 然而，非但不，反而. Nó biểu thị kết quả thực tế trái ngược hẳn với điều đáng lẽ phải xảy ra."),
         F(1, "非但不 A，反而 B nghĩa là chẳng những không A, mà ngược lại còn B. 非但 là văn viết của 不但; còn 然而 là thế nhưng, mở đầu sự chuyển ý."),
         F(2, "Ví dụ một, lấy từ bài khóa: 然而方便非但不是自由的替代品，反而可能带我们通往自由的反面，被消费主义绑架。 Thế nhưng tiện lợi chẳng những không thay thế được tự do, mà ngược lại còn có thể dẫn ta tới mặt đối lập của tự do."),
         F(3, "Ví dụ hai: 我帮了他的忙，然而我帮了他，他非但不感谢我，反而责怪起我。 Tôi đã giúp anh ta, thế nhưng anh ta chẳng những không cảm ơn, mà ngược lại còn trách móc tôi."),
         F(4, "Ví dụ ba: 这件事明明是他的过错，然而他非但不认错，反而把责任推给别人。 Việc này rõ ràng là lỗi của anh ta, thế nhưng anh ta chẳng những không nhận lỗi, mà còn đổ trách nhiệm cho người khác.")])

add("bullets", chapter="Mẫu câu: 被……绑架 · 切勿", section="Mẫu câu 重点句型", title="8. 被……绑架 – bị … trói buộc · 9. 切勿 – tuyệt đối đừng", size=34,
    items=["## 被……绑架: nghĩa gốc là bị bắt cóc; nghĩa bóng là hành vi bị ép buộc, khống chế",
           "……反而可能带我们通往“自由”的反面，被消费主义绑架。",
           "(2) 不要让文学创作被资本绑架。",
           "(3) 外卖送餐员往往被速度绑架，导致交通事故率飙升。",
           "## 切勿 + động từ: phó từ, văn viết, tuyệt đối đừng, nhất thiết không được",
           "(1) ……对每条个人信息都应当重视起来，切勿放弃这个权利。",
           "(2) 年轻人切勿浪费时间，时间不等人。",
           "(3) 安全第一，请大家切勿酒后开车。"],
    say=[F(0, "Mẫu thứ tám: 被什么绑架. Nghĩa gốc của 绑架 là bắt cóc. Nghĩa bóng, dùng rất nhiều ngày nay, là hành vi của một người bị một thứ gì đó ép buộc, khống chế."),
         F(1, "Trong bài khóa: 被消费主义绑架, bị chủ nghĩa tiêu dùng trói buộc."),
         F(2, "Ví dụ hai: 不要让文学创作被资本绑架。 Đừng để sáng tác văn học bị đồng tiền chi phối. 资本 là tư bản, đồng vốn."),
         F(3, "Ví dụ ba: 外卖送餐员往往被速度绑架，导致交通事故率飙升。 Người giao đồ ăn thường bị tốc độ trói buộc, khiến tỷ lệ tai nạn giao thông tăng vọt. Ngoài ra còn có cụm rất hay gặp: 道德绑架, ép buộc người khác bằng đạo đức."),
         F(4, "Mẫu thứ chín: 切勿. Đây là phó từ văn viết, nghĩa là tuyệt đối đừng, nhất thiết không được, đứng trước động từ. Hay gặp trên biển báo, thông báo, lời khuyên."),
         F(5, "Ví dụ một, câu kết của bài khóa: 对每条个人信息都应当重视起来，切勿放弃这个权利。 Cần coi trọng từng mẩu thông tin cá nhân, tuyệt đối đừng từ bỏ quyền này."),
         F(6, "Ví dụ hai: 年轻人切勿浪费时间，时间不等人。 Người trẻ tuyệt đối đừng lãng phí thời gian, thời gian không chờ đợi ai."),
         F(7, "Ví dụ ba: 安全第一，请大家切勿酒后开车。 An toàn là trên hết, xin mọi người tuyệt đối đừng lái xe sau khi uống rượu. Câu này giống hệt khẩu hiệu đã uống rượu bia thì không lái xe ở Việt Nam.")])

# ======================= KẾT HỢP TỪ =======================
add("bullets", chapter="Kết hợp từ", section="Kết hợp từ 词语搭配", title="Kết hợp từ (1): 骚扰 · 一己 · 让渡 · 悉数", size=34,
    items=["## 骚扰: ～短信 · ～电话 · ～软件 · ～拦截",
           "许多人因为骚扰电话不断而不胜其烦。",
           "## 一己: ～之力 · ～之见 · ～之私 · ～之利",
           "以上只是我的一己之见，欢迎大家批评指正。",
           "## 让渡: ～主权 · ～权利 · ～利益 · ～资源",
           "全球化必然带来国际交往与合作，企业不可避免地需要让渡部分利益。",
           "## 悉数: ～掌握 · ～到场 · ～参加 · ～上涨",
           "六月的世界杯比赛，传统强队悉数参加，他们将为大家带来一场视觉盛宴。"],
    say=["Tiếp theo là phần kết hợp từ, tiếng Trung là 词语搭配. Học từ theo cụm sẽ giúp các bạn dùng từ tự nhiên như người bản ngữ.",
         F(0, "Từ thứ nhất: 骚扰. Hay gặp: 骚扰短信，骚扰电话，骚扰软件，骚扰拦截. Tức là tin nhắn rác, cuộc gọi làm phiền, phần mềm quấy rối, và chặn cuộc gọi rác."),
         F(1, "Ví dụ: 许多人因为骚扰电话不断而不胜其烦。 Nhiều người phiền không chịu nổi vì cuộc gọi làm phiền liên tục. 不胜其烦 là phiền không chịu nổi."),
         F(2, "Từ thứ hai: 一己. Hay gặp: 一己之力，一己之见，一己之私，一己之利. Tức là sức một người, ý kiến riêng, tư tâm, và lợi ích riêng."),
         F(3, "Ví dụ: 以上只是我的一己之见，欢迎大家批评指正。 Trên đây chỉ là ý kiến riêng của tôi, rất mong mọi người góp ý. Câu này rất hay dùng khi kết thúc bài phát biểu, các bạn nên nhớ."),
         F(4, "Từ thứ ba: 让渡. Hay gặp: 让渡主权，让渡权利，让渡利益，让渡资源. Tức là nhượng lại chủ quyền, quyền lợi, lợi ích, tài nguyên."),
         F(5, "Ví dụ: 全球化必然带来国际交往与合作，企业不可避免地需要让渡部分利益。 Toàn cầu hóa tất yếu mang đến giao lưu và hợp tác quốc tế, doanh nghiệp khó tránh khỏi phải nhường lại một phần lợi ích."),
         F(6, "Từ thứ tư: 悉数. Hay gặp: 悉数掌握，悉数到场，悉数参加，悉数上涨. Tức là nắm trọn, có mặt đầy đủ, tham gia đông đủ, và tăng giá đồng loạt."),
         F(7, "Ví dụ: 六月的世界杯比赛，传统强队悉数参加，他们将为大家带来一场视觉盛宴。 Kỳ World Cup tháng sáu, các đội mạnh truyền thống đều tham gia đầy đủ, họ sẽ mang đến một bữa tiệc thị giác cho mọi người.")])

add("bullets", section="Kết hợp từ 词语搭配", title="Kết hợp từ (2): 不乏 · 海量 · 渺小 · 尤为", size=34,
    items=["## 不乏: ～先例 · ～其人 · ～其例",
           "其实，实现区域合作的共同发展是不乏先例的。",
           "## 海量: ～信息 · ～数据 · ～空间 · ～存储",
           "面对海量的出版物，书店和读者都难免会迷失方向。",
           "## 渺小: 生命～ · 力量～ · 声音～",
           "微生物如此渺小，以致常被人们忽视。",
           "## 尤为: ～严重 · ～深刻 · ～重要 · ～引人注意",
           "今年中国遭遇了百年不遇的旱灾，西南地区尤为严重。"],
    say=[F(0, "Từ thứ năm: 不乏. Hay gặp: 不乏先例，不乏其人，不乏其例. Tức là không thiếu tiền lệ, không thiếu người như thế, không thiếu ví dụ như thế."),
         F(1, "Ví dụ: 其实，实现区域合作的共同发展是不乏先例的。 Thật ra, việc hợp tác khu vực để cùng phát triển không thiếu tiền lệ."),
         F(2, "Từ thứ sáu: 海量. Hay gặp: 海量信息，海量数据，海量空间，海量存储. Tức là thông tin khổng lồ, dữ liệu khổng lồ, dung lượng cực lớn, lưu trữ cực lớn."),
         F(3, "Ví dụ: 面对海量的出版物，书店和读者都难免会迷失方向。 Trước lượng ấn phẩm khổng lồ, cả hiệu sách lẫn độc giả đều khó tránh khỏi lạc hướng."),
         F(4, "Từ thứ bảy: 渺小. Hay gặp: 生命渺小，力量渺小，声音渺小. Tức là sinh mệnh nhỏ bé, sức lực nhỏ bé, tiếng nói nhỏ bé. Chú ý, 渺小 thường làm vị ngữ, đứng sau danh từ."),
         F(5, "Ví dụ: 微生物如此渺小，以致常被人们忽视。 Vi sinh vật nhỏ bé đến thế, đến nỗi thường bị con người bỏ qua. 以致 là đến nỗi, dẫn ra kết quả không mong muốn."),
         F(6, "Từ thứ tám: 尤为. Hay gặp: 尤为严重，尤为深刻，尤为重要，尤为引人注意. Tức là đặc biệt nghiêm trọng, đặc biệt sâu sắc, đặc biệt quan trọng, đặc biệt thu hút sự chú ý."),
         F(7, "Ví dụ: 今年中国遭遇了百年不遇的旱灾，西南地区尤为严重。 Năm nay Trung Quốc gặp phải trận hạn hán trăm năm có một, vùng Tây Nam đặc biệt nghiêm trọng. 百年不遇 là trăm năm chưa gặp.")])

# ======================= THÀNH NGỮ =======================
add("bullets", chapter="Thành ngữ (14 câu)", section="Thành ngữ 成语", title="Thành ngữ (1)", size=33,
    items=["## 瞠目结舌 chēngmù-jiéshé – trợn mắt líu lưỡi, sững sờ",
           "这场滑雪比赛十分惊险，看得观众瞠目结舌。",
           "## 小心翼翼 xiǎoxīn-yìyì – thận trọng từng li từng tí",
           "我站在悬崖边上有点头晕，只能小心翼翼地向前走。",
           "## 独善其身 dúshàn-qíshēn – chỉ lo cho riêng mình",
           "随着经济全球化进程的发展，一个国家很难脱离国际社会“独善其身”。",
           "## 决堤而出 juédī'érchū – vỡ đê tuôn ra",
           "记忆却像洪水一样，随时会决堤而出。"],
    say=["Bài này có rất nhiều thành ngữ, sách liệt kê mười bốn câu. Thầy chia thành bốn nhóm. Mỗi câu, thầy giải thích nghĩa và đọc thêm một ví dụ ngoài bài khóa.",
         F(0, "Câu thứ nhất: 瞠目结舌. 瞠目 là trợn mắt, 结舌 là líu lưỡi: trợn tròn mắt, không nói nên lời, chỉ sự sững sờ hoặc lúng túng. Trong bài: 细化到令人瞠目结舌的地步."),
         F(1, "Ví dụ: 这场滑雪比赛十分惊险，看得观众瞠目结舌。 Trận thi trượt tuyết này vô cùng gay cấn, khiến khán giả xem mà sững sờ."),
         F(2, "Câu thứ hai: 小心翼翼, thận trọng từng li từng tí, không dám sơ suất chút nào. Trong bài: 连问个生日、年龄、工作都得小心翼翼."),
         F(3, "Ví dụ: 我站在悬崖边上有点头晕，只能小心翼翼地向前走。 Tôi đứng bên vách núi thấy hơi chóng mặt, chỉ dám thận trọng từng bước tiến lên."),
         F(4, "Câu thứ ba: 独善其身. 独 là chỉ, 善 là làm cho tốt, giữ gìn. Sách giải thích: chỉ lo cho bản thân, không quan tâm người khác. Câu gốc trong sách Mạnh Tử là 穷则独善其身，达则兼济天下, nghèo thì giữ mình cho tốt, hiển đạt thì giúp cả thiên hạ."),
         F(5, "Ví dụ: 随着经济全球化进程的发展，一个国家很难脱离国际社会独善其身。 Cùng với tiến trình toàn cầu hóa kinh tế, một quốc gia rất khó tách khỏi cộng đồng quốc tế mà đứng riêng một mình."),
         F(6, "Câu thứ tư: 决堤而出, nước sông vỡ đê tuôn ra, thường dùng để so sánh nước mắt, ký ức, hay thông tin tuôn trào không ngăn được. Trong bài: 个人信息就像洪水一样决堤而出."),
         F(7, "Ví dụ: 记忆却像洪水一样，随时会决堤而出。 Thế nhưng ký ức lại như nước lũ, bất cứ lúc nào cũng có thể vỡ đê tuôn ra.")])

add("bullets", section="Thành ngữ 成语", title="Thành ngữ (2)", size=33,
    items=["## 防不胜防 fángbùshèngfáng – phòng không xuể",
           "我已经非常小心了，还是上了骗子的当，实在是防不胜防。",
           "## 一闪而过 yìshǎn'érguò – vụt qua trong chớp mắt",
           "时间像一闪而过的流星，总是在我们不经意间悄悄溜走。",
           "## 堂而皇之 táng'érhuángzhī – công khai, ngang nhiên (nghĩa chê)",
           "他抄袭了别人的文章，还堂而皇之地署上自己的名字拿去发表。",
           "## 居心不良 jūxīn-bùliáng – có ý đồ xấu, dụng tâm bất lương",
           "越是善良的人，越察觉不出别人的居心不良。"],
    say=[F(0, "Câu thứ năm: 防不胜防, việc cần đề phòng quá nhiều, phòng không xuể. Trong bài: 到处都是防不胜防的漏洞."),
         F(1, "Ví dụ: 我已经非常小心了，还是上了骗子的当，实在是防不胜防。 Tôi đã rất cẩn thận rồi mà vẫn mắc lừa kẻ lừa đảo, đúng là phòng không xuể."),
         F(2, "Câu thứ sáu: 一闪而过, vụt qua trong chớp mắt, rất nhanh, không để ý là đã qua. Trong bài: 那些在屏幕上一闪而过的用户协议."),
         F(3, "Ví dụ: 时间像一闪而过的流星，总是在我们不经意间悄悄溜走。 Thời gian như sao băng vụt qua, luôn lặng lẽ trôi đi khi ta không để ý."),
         F(4, "Câu thứ bảy: 堂而皇之. Nghĩa là công khai, không hề che giấu, hoặc có vẻ đường hoàng, bề thế; cả hai nghĩa đều thường mang sắc thái chê. Trong bài: 让他人堂而皇之地收集你的个人信息."),
         F(5, "Ví dụ: 他抄袭了别人的文章，还堂而皇之地署上自己的名字拿去发表。 Hắn đạo văn của người khác, còn ngang nhiên ký tên mình đem đi đăng."),
         F(6, "Câu thứ tám: 居心不良. 居心 là dụng tâm, 良 là tốt: lòng dạ không tốt, có ý đồ xấu. Trong bài: 一些居心不良者在网上发布有偿任务."),
         F(7, "Ví dụ: 越是善良的人，越察觉不出别人的居心不良。 Người càng lương thiện thì càng khó nhận ra ý đồ xấu của người khác.")])

add("bullets", section="Thành ngữ 成语", title="Thành ngữ (3)", size=34,
    items=["## 前车之鉴 qiánchēzhījiàn – vết xe đổ, bài học nhãn tiền",
           "有了他人的失败作为前车之鉴，我们可以少走很多弯路。",
           "## 有一说一 yǒuyī-shuōyī – có sao nói vậy",
           "有一说一，这件事确实是你考虑得不周全。",
           "## 盆满钵满 pénmǎn-bōmǎn – kiếm bộn tiền",
           "国庆黄金周一到，夫子庙商圈的商家都赚了个盆满钵满。"],
    say=[F(0, "Câu thứ chín: 前车之鉴. 鉴 là tấm gương, mở rộng ra là bài học. Xe đi trước bị lật, xe đi sau lấy đó làm gương: tiếng Việt nói là vết xe đổ, hay bài học nhãn tiền. Trong bài: 有了这样的前车之鉴."),
         F(1, "Ví dụ: 有了他人的失败作为前车之鉴，我们可以少走很多弯路。 Có thất bại của người khác làm bài học, chúng ta có thể bớt đi rất nhiều đường vòng."),
         F(2, "Câu thứ mười: 有一说一, có gì nói nấy, nói đúng sự thật. Trong khẩu ngữ hiện nay, nó còn hay đứng đầu câu, nghĩa là nói thật lòng thì."),
         F(3, "Ví dụ: 有一说一，这件事确实是你考虑得不周全。 Nói thật lòng nhé, chuyện này đúng là cậu suy nghĩ chưa chu đáo."),
         F(4, "Câu thứ mười một: 盆满钵满, chậu đầy bát đầy, chỉ kiếm được rất nhiều tiền. Thường dùng trong mẫu 赚得盆满钵满 hoặc 赚了个盆满钵满."),
         F(5, "Ví dụ: 国庆黄金周一到，夫子庙商圈的商家都赚了个盆满钵满。 Tuần lễ vàng Quốc khánh vừa đến, các cửa hàng ở khu thương mại Phu Tử Miếu đều kiếm bộn tiền. 夫子庙 là một khu phố cổ nổi tiếng ở Nam Kinh.")])

add("bullets", section="Thành ngữ 成语", title="Thành ngữ (4)", size=34,
    items=["## 任人宰割 rènrén-zǎigē – mặc người chém giết, không sức chống cự",
           "落后就要挨打，国家没有经济实力就要任人宰割。",
           "## 唾手可得 tuòshǒu-kědé – dễ như trở bàn tay",
           "科学上没有唾手可得的事，任何发现都需要经过艰苦的努力。",
           "## 泥沙俱下 níshā-jùxià – bùn cát cùng trôi, tốt xấu lẫn lộn",
           "近几年，网络文学日渐流行，作品数量众多，但由于创作者水平不一，所以难免泥沙俱下。"],
    say=[F(0, "Câu thứ mười hai: 任人宰割. 任 là mặc cho, 宰割 là giết mổ, cắt xẻ: mặc cho người khác chém giết, ức hiếp mà không có sức chống lại. Trong bài: 任人宰割的韭菜."),
         F(1, "Ví dụ: 落后就要挨打，国家没有经济实力就要任人宰割。 Lạc hậu thì sẽ bị đánh, đất nước không có thực lực kinh tế thì sẽ bị người ta chèn ép."),
         F(2, "Câu thứ mười ba: 唾手可得. 唾手 là nhổ nước bọt vào lòng bàn tay, chỉ một động tác rất dễ: tiếng Việt nói là dễ như trở bàn tay. Trong bài: 这种唾手可得的方便."),
         F(3, "Ví dụ: 科学上没有唾手可得的事，任何发现都需要经过艰苦的努力。 Trong khoa học không có gì dễ như trở bàn tay, mọi phát hiện đều phải trải qua nỗ lực gian khổ."),
         F(4, "Câu thứ mười bốn: 泥沙俱下. Bùn và cát cùng trôi theo dòng nước, ví người tốt kẻ xấu, thứ hay thứ dở lẫn lộn với nhau. Trong bài: 泥沙俱下之中，不乏海量的个人信息泄露."),
         F(5, "Ví dụ: 近几年，网络文学日渐流行，作品数量众多，但由于创作者水平不一，所以难免泥沙俱下。 Mấy năm gần đây, văn học mạng ngày càng thịnh hành, tác phẩm rất nhiều, nhưng vì trình độ người viết không đồng đều, nên khó tránh khỏi hay dở lẫn lộn.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 课后练习", title="Bài tập 1: Chọn từ thích hợp điền vào chỗ trống (1)", reveal=True, size=33,
    items=["## 细化 · 瞠目结舌 · 彼岸 · 让渡 · 小心翼翼 · 防不胜防 · 决堤而出 · 独善其身",
           "(1) 害怕吵醒入睡的孩子，张小海___地上了楼。",
           "Đáp án: 小心翼翼",
           "(2) 每当思念家乡时，我都会站在海边，想象着大洋___的家人正在做什么。",
           "Đáp án: 彼岸",
           "(3) 眼睁睁看到他居然把车开到人行道上，我们都___。",
           "Đáp án: 瞠目结舌",
           "(4) 所谓投资就是___资金使用权，从而获取利益的行为。",
           "Đáp án: 让渡"],
    say=["Bây giờ chúng ta sang phần luyện tập sau bài, sách gọi là 趁热打铁, rèn sắt khi còn nóng. Bài tập một: chọn từ thích hợp điền vào chỗ trống.",
         F(0, "Có tám từ: 细化，瞠目结舌，彼岸，让渡，小心翼翼，防不胜防，决堤而出，独善其身."),
         F(1, "Câu một: 害怕吵醒入睡的孩子，张小海什么地上了楼。 Sợ đánh thức đứa con đã ngủ, Trương Tiểu Hải lên lầu một cách thế nào? Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 小心翼翼. 张小海小心翼翼地上了楼。 Trương Tiểu Hải rón rén, thận trọng từng bước lên lầu."),
         F(3, "Câu hai: 每当思念家乡时，我都会站在海边，想象着大洋什么的家人正在做什么。 Mỗi khi nhớ quê, tôi lại đứng bên bờ biển, tưởng tượng người nhà ở đâu đang làm gì."),
         F(4, "Đáp án: 彼岸. 大洋彼岸的家人, người nhà ở bên kia đại dương. Cụm 大洋彼岸 vừa gặp trong bài khóa."),
         F(5, "Câu ba: 眼睁睁看到他居然把车开到人行道上，我们都什么。 Trơ mắt nhìn anh ta lái xe lên cả vỉa hè, chúng tôi đều thế nào?"),
         F(6, "Đáp án: 瞠目结舌. Chúng tôi đều sững sờ, trợn mắt không nói nên lời."),
         F(7, "Câu bốn: 所谓投资就是什么资金使用权，从而获取利益的行为。 Cái gọi là đầu tư, chính là hành vi làm gì với quyền sử dụng vốn, từ đó thu lợi?"),
         F(8, "Đáp án: 让渡. 让渡资金使用权, chuyển nhượng quyền sử dụng vốn. Đây là kết hợp 让渡权利 vừa học.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 1: Chọn từ thích hợp điền vào chỗ trống (2)", reveal=True, size=33,
    items=["(5) 目前的方案只是一个大概的设想，具体实施步骤还需要进一步___。",
           "Đáp án: 细化",
           "(6) 网络骗局不仅数量和种类众多，手段还越来越高明，有时候真是让人___。",
           "Đáp án: 防不胜防",
           "(7) 多年感情只因她的一句话就终结了，我的悲伤就如同海水一样___。",
           "Đáp án: 决堤而出",
           "(8) ___也好，兼济天下也好，除了做“愤怒青年”，还应当有“奋斗青年”的理想。",
           "Đáp án: 独善其身"],
    say=[F(0, "Câu năm: 目前的方案只是一个大概的设想，具体实施步骤还需要进一步什么。 Phương án hiện nay chỉ là một ý tưởng sơ bộ, các bước thực hiện cụ thể còn cần làm gì thêm?"),
         F(1, "Đáp án: 细化. 进一步细化, cụ thể hóa thêm một bước."),
         F(2, "Câu sáu: 网络骗局不仅数量和种类众多，手段还越来越高明，有时候真是让人什么。 Các trò lừa đảo trên mạng không chỉ nhiều về số lượng và chủng loại, thủ đoạn còn ngày càng tinh vi, có lúc thật khiến người ta thế nào?"),
         F(3, "Đáp án: 防不胜防. 让人防不胜防, khiến người ta phòng không xuể."),
         F(4, "Câu bảy: 多年感情只因她的一句话就终结了，我的悲伤就如同海水一样什么。 Tình cảm bao năm chỉ vì một câu nói của cô ấy mà chấm dứt, nỗi buồn của tôi như nước biển làm sao?"),
         F(5, "Đáp án: 决堤而出. 悲伤如同海水一样决堤而出, nỗi buồn như nước biển vỡ đê tuôn trào."),
         F(6, "Câu tám: 什么也好，兼济天下也好，除了做愤怒青年，还应当有奋斗青年的理想。 Dù là gì, hay là giúp đời, ngoài làm thanh niên phẫn nộ, còn nên có lý tưởng của thanh niên phấn đấu."),
         F(7, "Đáp án: 独善其身. 独善其身也好，兼济天下也好: đây chính là câu của Mạnh Tử mà thầy vừa nhắc, 穷则独善其身，达则兼济天下.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn đáp án đúng (1)", reveal=True, size=34,
    items=["(1) 他因这场网络暴力去世后，众多网友又对他的朋友开始了一场新的道德（  ）。 A.谩骂 B.绑架 C.恐吓 D.约束",
           "Đáp án: B. 绑架 – 道德绑架 (ép buộc bằng đạo đức)",
           "(2) 我们已经掌握了关键证据，所以说话才能（  ）。 A.堂而皇之 B.理直气壮 C.有一说一 D.直来直去",
           "Đáp án: B. 理直气壮 – có lý lẽ, chứng cứ nên nói năng tự tin",
           "(3) 失败并不可怕，我们应分析原因，吸取（  ），以免再犯同样的错误。 A.泥沙俱下 B.唾手可得 C.前车之鉴 D.防不胜防",
           "Đáp án: C. 前车之鉴 – 吸取前车之鉴 (rút bài học)"],
    say=["Bài tập hai: chọn đáp án đúng.",
         F(0, "Câu một: 他因这场网络暴力去世后，众多网友又对他的朋友开始了一场新的道德什么。 Sau khi anh ấy qua đời vì bạo lực mạng, nhiều cư dân mạng lại bắt đầu một cuộc gì đó về đạo đức nhằm vào bạn bè anh ấy. A, 谩骂; B, 绑架; C, 恐吓; D, 约束."),
         F(1, "Đáp án: B, 绑架. 道德绑架 là một cụm cố định, nghĩa là ép buộc, chèn ép người khác bằng đạo đức. 谩骂 và 恐吓 không đi với 道德."),
         F(2, "Câu hai: 我们已经掌握了关键证据，所以说话才能什么。 Chúng tôi đã nắm được chứng cứ then chốt, nên nói năng mới có thể thế nào? A, 堂而皇之; B, 理直气壮; C, 有一说一; D, 直来直去."),
         F(3, "Đáp án: B, 理直气壮. Có chứng cứ thì lý lẽ vững, nói năng tự tin. 堂而皇之 mang nghĩa chê; 有一说一 và 直来直去 là có sao nói vậy, thẳng thắn, không liên quan đến chứng cứ."),
         F(4, "Câu ba: 失败并不可怕，我们应分析原因，吸取什么，以免再犯同样的错误。 Thất bại không đáng sợ, ta nên phân tích nguyên nhân, rút ra gì đó, để khỏi phạm lại sai lầm cũ. A, 泥沙俱下; B, 唾手可得; C, 前车之鉴; D, 防不胜防."),
         F(5, "Đáp án: C, 前车之鉴. 吸取前车之鉴 là rút bài học từ vết xe đổ.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn đáp án đúng (2)", reveal=True, size=34,
    items=["(4) 在关键问题上，他总是说得（  ）不清，大家对此都很不满意。 A.含糊 B.模糊 C.糊涂 D.马虎",
           "Đáp án: A. 含糊 – 含糊不清 là cụm cố định chỉ lời nói mập mờ",
           "(5) 尽管他是这个时代的风云人物，但是从人类发展史上来看，仍然（  ）得很。 A.细微 B.渺茫 C.细小 D.渺小",
           "Đáp án: D. 渺小 – nhỏ bé, không đáng kể (nói về con người, sức lực)"],
    say=[F(0, "Câu bốn: 在关键问题上，他总是说得什么不清，大家对此都很不满意。 Ở những vấn đề then chốt, anh ta luôn nói năng gì đó không rõ, mọi người đều rất không hài lòng. A, 含糊; B, 模糊; C, 糊涂; D, 马虎."),
         F(1, "Đáp án: A, 含糊. 含糊不清 là cụm cố định chỉ lời nói mập mờ, úp mở. 模糊 thường nói về hình ảnh, ký ức mờ nhạt; 糊涂 là hồ đồ, lú lẫn; 马虎 là cẩu thả."),
         F(2, "Câu năm: 尽管他是这个时代的风云人物，但是从人类发展史上来看，仍然什么得很。 Tuy ông ấy là nhân vật lẫy lừng của thời đại này, nhưng xét trong lịch sử phát triển của loài người, vẫn rất thế nào? A, 细微; B, 渺茫; C, 细小; D, 渺小."),
         F(3, "Đáp án: D, 渺小. 渺小 nói về con người, sức lực nhỏ bé, không đáng kể. 渺茫 là mờ mịt, như 希望渺茫, hy vọng mong manh; 细微 và 细小 nói về vật thể nhỏ li ti.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ và mẫu câu cho sẵn trả lời câu hỏi", reveal=True, size=32,
    items=["(1) 邓玉峰从黑市购买的个人信息包括哪些内容？（……到……地步）",
           "Đáp án gợi ý: 包括姓名、电话、住址、银行存款等，有的信息甚至细化到网购记录、购票记录和家用车发动机号的地步。",
           "(2) 我们的个人信息如何泄露的？（殊不知）",
           "Đáp án gợi ý: 我们以为点一下“同意”没什么关系，殊不知各种应用、外卖网站和网购平台都在收集我们的信息。",
           "(3) 商家是如何利用个人信息的？（仗着……）",
           "Đáp án gợi ý: 一些不良商家仗着手握用户信息，不再下功夫提升服务，还向用户推送大量广告。",
           "(4) 让渡个人隐私真的让人们的生活更便利吗？（……，然而……非但不……，反而……）",
           "Đáp án gợi ý: 表面上生活更方便了，然而让渡隐私非但不能带来真正的自由，反而让我们被消费主义绑架。"],
    say=["Bài tập ba: dùng từ và mẫu câu cho sẵn để trả lời câu hỏi. Đây là câu hỏi mở, thầy đưa ra đáp án gợi ý, các bạn có thể trả lời theo cách của mình.",
         F(0, "Câu một: 邓玉峰从黑市购买的个人信息包括哪些内容？ Thông tin cá nhân mà Đặng Ngọc Phong mua từ chợ đen gồm những gì? Dùng mẫu 到什么地步."),
         F(1, "Đáp án gợi ý: 包括姓名、电话、住址、银行存款等，有的信息甚至细化到网购记录、购票记录和家用车发动机号的地步。 Gồm họ tên, điện thoại, địa chỉ, tiền gửi ngân hàng; có thông tin còn chi tiết đến mức cả lịch sử mua hàng, mua vé và số máy xe ô tô."),
         F(2, "Câu hai: 我们的个人信息如何泄露的？ Thông tin cá nhân của chúng ta bị rò rỉ như thế nào? Dùng 殊不知."),
         F(3, "Đáp án gợi ý: 我们以为点一下同意没什么关系，殊不知各种应用、外卖网站和网购平台都在收集我们的信息。 Chúng ta tưởng bấm đồng ý một cái chẳng sao, nào ngờ đủ loại ứng dụng, trang giao đồ ăn và nền tảng mua sắm đều đang thu thập thông tin của mình."),
         F(4, "Câu ba: 商家是如何利用个人信息的？ Thương nhân lợi dụng thông tin cá nhân như thế nào? Dùng 仗着."),
         F(5, "Đáp án gợi ý: 一些不良商家仗着手握用户信息，不再下功夫提升服务，还向用户推送大量广告。 Một số thương nhân bất lương cậy nắm thông tin người dùng, không chịu nâng cao dịch vụ, còn gửi hàng loạt quảng cáo cho người dùng."),
         F(6, "Câu bốn: 让渡个人隐私真的让人们的生活更便利吗？ Nhường đi quyền riêng tư có thật sự làm cuộc sống tiện lợi hơn không? Dùng mẫu 然而，非但不，反而."),
         F(7, "Đáp án gợi ý: 表面上生活更方便了，然而让渡隐私非但不能带来真正的自由，反而让我们被消费主义绑架。 Bề ngoài cuộc sống tiện hơn, thế nhưng nhường đi quyền riêng tư chẳng những không mang lại tự do thật sự, mà còn khiến ta bị chủ nghĩa tiêu dùng trói buộc.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Chọn từ điền vào đoạn văn", reveal=True, size=32,
    items=["## 任人宰割 · 泄露 · 别有用心 · 骚扰 · 堂而皇之 · 一己之力 · 陷阱",
           "大数据时代，没有人能凭借___来保全个人隐私。个人隐私数据一旦___，造成的危害往往难以想象，不可不防：当用户的隐私被让渡给___的商家，他们便会___地收集和传播用户信息，对用户进行有针对性的广告___；更可怕的是，诈骗分子非法获得隐私数据的成本越来越低，很多人因为一时疏忽，便落入诈骗分子的___，只能___。",
           "Đáp án: 一己之力 · 泄露 · 别有用心 · 堂而皇之 · 骚扰 · 陷阱 · 任人宰割"],
    say=[F(0, "Bài tập bốn: chọn từ điền vào đoạn văn. Có bảy từ: 任人宰割，泄露，别有用心，骚扰，堂而皇之，一己之力，陷阱. Trong đó 别有用心 là có dụng ý khác, có mưu đồ riêng, gần nghĩa với 居心不良."),
         F(1, "大数据时代，没有人能凭借什么来保全个人隐私。个人隐私数据一旦什么，造成的危害往往难以想象，不可不防：当用户的隐私被让渡给什么的商家，他们便会什么地收集和传播用户信息，对用户进行有针对性的广告什么；更可怕的是，诈骗分子非法获得隐私数据的成本越来越低，很多人因为一时疏忽，便落入诈骗分子的什么，只能什么。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 没有人能凭借一己之力来保全个人隐私；隐私数据一旦泄露；让渡给别有用心的商家；他们便会堂而皇之地收集和传播用户信息；进行有针对性的广告骚扰；落入诈骗分子的陷阱，只能任人宰割。 Thời đại dữ liệu lớn, không ai có thể dựa vào sức một mình để bảo vệ quyền riêng tư. Dữ liệu riêng tư một khi bị rò rỉ, tác hại thường khó lường: khi quyền riêng tư bị giao cho những thương nhân có mưu đồ, họ sẽ ngang nhiên thu thập, phát tán thông tin, quấy rối người dùng bằng quảng cáo nhắm đúng đối tượng; đáng sợ hơn, chi phí để kẻ lừa đảo có được dữ liệu ngày càng thấp, nhiều người chỉ sơ suất một chút là sa vào bẫy, đành mặc người chém giết.")])

# ======================= THẢO LUẬN =======================
add("bullets", chapter="Thảo luận: liên hệ Việt Nam", section="Thảo luận 讨论", title="Thảo luận: quyền riêng tư ở Việt Nam", reveal=True, size=33,
    items=["(1) 在越南，你遇到过骚扰电话或诈骗短信吗？对方是怎么知道你的信息的？",
           "Đáp án gợi ý: 遇到过。对方一张口就能报上我的姓名，可能是我在网上购物、填表或者注册应用时，个人信息被泄露了。",
           "(2) 为了保护自己的隐私，我们可以怎么做？",
           "Đáp án gợi ý: 安装应用时仔细阅读授权协议，切勿随便打勾；不在网上公开身份证和住址；收到可疑短信时不点链接。",
           "(3) 你同意“用隐私换便利”吗？",
           "Đáp án gợi ý: 可以部分地让渡，但要有底线；同时需要法律的约束，比如越南的《个人数据保护法》。"],
    say=["Cuối cùng, chúng ta cùng thảo luận, liên hệ với Việt Nam. Các bạn hãy thử trả lời bằng tiếng Trung, dùng các từ và mẫu câu vừa học.",
         F(0, "Câu một: 在越南，你遇到过骚扰电话或诈骗短信吗？对方是怎么知道你的信息的？ Ở Việt Nam, bạn đã từng gặp cuộc gọi làm phiền hay tin nhắn lừa đảo chưa? Đối phương làm sao biết thông tin của bạn?"),
         F(1, "Đáp án gợi ý: 遇到过。对方一张口就能报上我的姓名，可能是我在网上购物、填表或者注册应用时，个人信息被泄露了。 Từng gặp rồi. Đối phương vừa mở miệng đã gọi đúng tên tôi, có lẽ thông tin bị rò rỉ khi tôi mua hàng qua mạng, điền biểu mẫu hay đăng ký ứng dụng. Các bạn thấy không, câu 一张口就能报上 trong bài khóa dùng được ngay."),
         F(2, "Câu hai: 为了保护自己的隐私，我们可以怎么做？ Để bảo vệ quyền riêng tư của mình, chúng ta có thể làm gì?"),
         F(3, "Đáp án gợi ý: 安装应用时仔细阅读授权协议，切勿随便打勾；不在网上公开身份证和住址；收到可疑短信时不点链接。 Khi cài ứng dụng thì đọc kỹ thỏa thuận cấp quyền, tuyệt đối đừng tùy tiện đánh dấu tích; không công khai căn cước và địa chỉ trên mạng; nhận tin nhắn đáng ngờ thì không bấm vào đường link."),
         F(4, "Câu ba: 你同意用隐私换便利吗？ Bạn có đồng ý đổi quyền riêng tư lấy sự tiện lợi không?"),
         F(5, "Đáp án gợi ý: 可以部分地让渡，但要有底线；同时需要法律的约束，比如越南的个人数据保护法。 Có thể nhường lại một phần, nhưng phải có giới hạn; đồng thời cần sự ràng buộc của pháp luật. Ở Việt Nam, sau Nghị định mười ba năm hai nghìn không trăm hai mươi ba, Luật Bảo vệ dữ liệu cá nhân đã có hiệu lực từ năm hai nghìn không trăm hai mươi sáu. Đây đúng là điều mà bài khóa gọi là 制度的约束.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết", section="Tổng kết", title="Tổng kết bài 4.1", size=34,
    items=["Từ vựng trọng tâm: 细化 · 地步 · 骚扰 · 漏洞 · 让渡 · 授权 · 陷阱 · 含糊 · 殊不知 · 悉数 · 无异于 · 仗着 · 绑架 · 不乏 · 泄露 · 尤为 · 切勿",
           "Mẫu câu: V到……地步 · (连)V都懒得V · 殊不知 · 无异于 · 毫无……可言 · 仗着 · 非但不……反而…… · 被……绑架 · 切勿",
           "Thành ngữ: 瞠目结舌 · 防不胜防 · 堂而皇之 · 前车之鉴 · 盆满钵满 · 任人宰割 · 唾手可得 · 泥沙俱下……",
           "Bố cục bài nghị luận: hiện tượng → phân tích (3 tiểu mục) → giải pháp",
           "## Bài tập về nhà",
           "Viết một đoạn khoảng 300 chữ: 你愿意用隐私换便利吗？ (dùng ít nhất 4 mẫu câu của bài)"],
    say=["Chúng ta cùng tổng kết bài bốn chấm một.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 细化，地步，骚扰，漏洞，让渡，授权，陷阱，含糊，殊不知，悉数，无异于，仗着，绑架，不乏，泄露，尤为，切勿. Và đừng quên các từ dễ nhầm như 社交，含糊，反面."),
         F(1, "Về mẫu câu: 到什么地步 chỉ mức độ, thường là tình cảnh xấu; 连什么都懒得 là chẳng buồn làm; 殊不知 là nào ngờ; 无异于 là chẳng khác gì; 毫无什么可言 là chẳng có chút gì; 仗着 là cậy, ỷ vào; 非但不，反而 là chẳng những không, mà ngược lại còn; 被什么绑架 là bị trói buộc; và 切勿 là tuyệt đối đừng."),
         F(2, "Về thành ngữ, hãy ôn lại mười bốn câu, đặc biệt là 瞠目结舌，防不胜防，堂而皇之，前车之鉴，盆满钵满，任人宰割，唾手可得，泥沙俱下."),
         F(3, "Về cách viết, hãy nhớ bố cục của bài nghị luận này: nêu hiện tượng, phân tích qua ba tiểu mục, rồi đưa ra giải pháp."),
         F(5, "Bài tập về nhà: hãy viết một đoạn văn khoảng ba trăm chữ với đề 你愿意用隐私换便利吗？ Bạn có sẵn lòng đổi quyền riêng tư lấy sự tiện lợi không? Hãy dùng ít nhất bốn mẫu câu của bài, như 殊不知，无异于，非但不，反而，切勿."),
         "Cảm ơn các bạn đã theo dõi bài giảng. Ở bài sau, chúng ta sẽ gặp một nhân vật đặc biệt: bác sĩ robot Watson, chỉ mười giây đã đưa ra phác đồ điều trị ung thư. Hẹn gặp lại các bạn ở bài bốn chấm hai: 机器人医生，简直神了！ Bác sĩ robot, đúng là thần kỳ! Chúc các bạn học tốt!"])

lesson = {
    "title": "顶石中文 – Bài 4.1: 真的，你的隐私只值一分钱！ (Thật đấy, quyền riêng tư của bạn chỉ đáng một xu!)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"小缝": "小凤",            # xiǎo fèng
                    "门缝": "门凤",            # mén fèng
                    "差评": "岔评",            # chàpíng
                    "恐吓": "恐赫",            # kǒnghè
                    "偏好": "偏号",            # piānhào
                    "悉数": "悉树",            # xīshù
                    "数年": "树年",            # shùnián
                    "泄露": "泄漏",            # xièlòu
                    "尤为": "尤维",            # yóuwéi
                    "切勿": "怯勿",            # qièwù
                    "身处": "身楚"},           # shēnchǔ
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds41.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
