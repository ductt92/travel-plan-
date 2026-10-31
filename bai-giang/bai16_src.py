#!/usr/bin/env python3
"""Kịch bản bài giảng HSK 6 (Thượng) – Bài 16 «徐健和他的野生动物摄影师们». Chạy để sinh bai16.json."""
import json
import os

TAG = "HSK 6 (Thượng) · Bài 16 · 徐健和他的野生动物摄影师们"
slides = []


def add(type_, chapter=None, section="", **kw):
    s = {"type": type_, "section": section, **kw}
    if chapter:
        s["chapter"] = chapter
    slides.append(s)


def F(i, t, **kw):
    return {"t": t, "f": i, **kw}


# ======================= MỞ ĐẦU =======================
# Tên bài có 13 chữ, quá dài cho một dòng chữ cỡ lớn (170px), nên tách làm hai dòng: zh + py
add("title", chapter="Mở đầu",
    top="Giáo trình chuẩn HSK 6 – Quyển Thượng",
    zh="徐健和他的", py="野生动物摄影师们",
    vi="Bài 16: Từ Kiện và các nhà nhiếp ảnh động vật hoang dã",
    sub="Xú Jiàn hé tā de yěshēng dòngwù shèyǐngshīmen\nBài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng Giáo trình chuẩn HSK 6, quyển Thượng.",
         "Hôm nay chúng ta học bài mười sáu: 徐健和他的野生动物摄影师们。 Nghĩa là: Từ Kiện và các nhà nhiếp ảnh động vật hoang dã của anh ấy.",
         "Đây là bài cuối cùng của Chủ đề bốn, 走遍天下, Đi khắp thiên hạ. Nhân vật chính là anh Từ Kiện, người sáng lập IBE, một nhóm nhiếp ảnh gia chuyên chụp ảnh động vật và thực vật hoang dã ở Trung Quốc. Họ băng rừng, vượt núi, ăn gió nằm sương, không phải để bán ảnh kiếm tiền, mà để ghi lại và bảo vệ sự đa dạng sinh học của đất nước mình.",
         "Việt Nam chúng ta cũng có rất nhiều loài động vật quý hiếm như sao la, voọc, hổ Đông Dương. Trong lúc học, các bạn hãy thử nghĩ xem: những hình ảnh đẹp có thể giúp gì cho việc bảo vệ chúng nhé."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài khóa: Từ Kiện và nhóm IBE chụp ảnh động vật hoang dã để bảo vệ đa dạng sinh học",
           "Nắm vững 45 từ mới, kèm âm Hán Việt và ví dụ",
           "Ngữ pháp: thành phần chen 换句话说, cấu trúc 为……所……, động từ 足以",
           "Phân biệt 以便 và 便于",
           "Mở rộng: thành phần chen (插入语) và các cặp từ gần nghĩa"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu nội dung bài khóa: công việc của Từ Kiện và các nhiếp ảnh gia nhóm IBE, những khó khăn họ gặp phải, và cách họ làm việc."),
         F(1, "Thứ hai, nắm vững bốn mươi lăm từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học ba điểm ngữ pháp: thành phần chen 换句话说, nghĩa là nói cách khác; cấu trúc bị động văn viết 为所; và động từ 足以, nghĩa là đủ để."),
         F(3, "Thứ tư, phân biệt hai từ rất dễ nhầm: 以便 và 便于."),
         F(4, "Thứ năm, phần mở rộng: tìm hiểu các loại thành phần chen trong câu, tiếng Trung gọi là 插入语, và làm quen với mười bốn cặp từ gần nghĩa."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 热身", title="Khởi động: Tên các loài động vật", size=40,
    items=["雪豹 xuěbào – báo tuyết · 赤斑羚 chìbānlíng – sơn dương đỏ",
           "喜马拉雅旱獭 Xǐmǎlāyǎ hàntǎ – macmot Himalaya",
           "藏狐 zànghú – cáo Tây Tạng · 大熊猫 dàxióngmāo – gấu trúc lớn",
           "大紫胸鹦鹉 dàzǐxiōngyīngwǔ – vẹt ngực tím lớn",
           "藏羚羊 zànglíngyáng – linh dương Tây Tạng · 牦牛 máoniú – bò Tây Tạng (yak)"],
    say=["Chúng ta bắt đầu bằng phần khởi động. Sách cho tám bức ảnh, yêu cầu các bạn làm quen với tên của các loài động vật. Cả tám loài này đều xuất hiện trong bài khóa.",
         F(0, "雪豹, báo tuyết, loài báo sống trên núi tuyết, bộ lông có nhiều đốm. 赤斑羚, sơn dương đỏ, chữ 赤 là màu đỏ."),
         F(1, "喜马拉雅旱獭, macmot Himalaya, một loài sóc đất to, sống trong hang trên cao nguyên. 旱 là khô hạn, vì chúng sống ở nơi khô ráo."),
         F(2, "藏狐, cáo Tây Tạng. Chú ý: chữ đầu ở đây đọc là zàng, thanh bốn, chỉ Tây Tạng. 大熊猫, gấu trúc lớn, loài vật tượng trưng của Trung Quốc."),
         F(3, "大紫胸鹦鹉, vẹt ngực tím lớn. 紫 là màu tím, 胸 là ngực, 鹦鹉 là con vẹt."),
         F(4, "藏羚羊, linh dương Tây Tạng. Và 牦牛, bò Tây Tạng, còn gọi là bò yak, lông dài, sống ở vùng núi cao lạnh giá. Các bạn hãy tạm dừng video và đọc to tên tám loài vật này nhé.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 野 và 亡", size=38,
    items=["## 野 (dã): ngoài đồng, hoang dã, không do người nuôi trồng",
           "野生 hoang dã · 野外 ngoài trời · 野地 bãi hoang · 野餐 dã ngoại · 野花 hoa dại · 野草 cỏ dại · 野菜 rau dại",
           "野马 ngựa hoang · 野牛 bò rừng · 野狗 chó hoang · 野猫 mèo hoang · 野兽 dã thú · 山野 núi rừng · 田野 đồng ruộng",
           "## 亡 (vong): mất, chết, diệt vong",
           "消亡 tiêu vong · 死亡 tử vong · 灭亡 diệt vong · 危亡 nguy vong · 兴亡 hưng vong",
           "存亡 tồn vong · 伤亡 thương vong · 亡国 mất nước · 亡故 qua đời · 亡友 người bạn đã mất"],
    say=["Phần khởi động thứ hai yêu cầu: hãy nghĩ xem các từ sau có liên hệ gì với nhau. Đây là cách học từ theo yếu tố cấu tạo, rất có lợi cho người Việt vì hầu hết các chữ đều có âm Hán Việt quen thuộc.",
         F(0, "Nhóm thứ nhất có chữ 野, Hán Việt là dã, như trong dã ngoại, dã thú. Nghĩa là ngoài đồng, hoang dã, không do con người nuôi trồng."),
         F(1, "野生，野外，野地，野餐，野花，野草，野菜。 Tức là: hoang dã, ngoài trời, bãi đất hoang, đi dã ngoại ăn uống, hoa dại, cỏ dại, rau dại. Từ 野生 chính là từ mới đầu tiên của bài, và có ngay trong tên bài."),
         F(2, "野马，野牛，野狗，野猫，野兽，山野，田野。 Tức là: ngựa hoang, bò rừng, chó hoang, mèo hoang, dã thú, núi rừng, đồng ruộng. Bài khóa có câu 长期风餐露宿在山野, lâu ngày ăn gió nằm sương nơi núi rừng."),
         F(3, "Nhóm thứ hai có chữ 亡, Hán Việt là vong, nghĩa là mất, chết, diệt vong."),
         F(4, "消亡，死亡，灭亡，危亡，兴亡。 Tức là: tiêu vong, tử vong, diệt vong, nguy vong, và hưng vong. Bài khóa nói loài báo tuyết 正濒临消亡, đang đứng trước nguy cơ biến mất."),
         F(5, "存亡，伤亡，亡国，亡故，亡友。 Tức là: tồn vong, thương vong, mất nước, qua đời, và người bạn đã khuất.")])

add("bullets", section="Khởi động 热身", title="Học từ theo yếu tố cấu tạo: 露 và 严", size=38,
    items=["## 露 (lộ): để lộ ra, bày ra ngoài; sương",
           "暴露 bộc lộ, phơi bày · 表露 biểu lộ · 透露 tiết lộ · 流露 bộc lộ (tình cảm) · 吐露心声 thổ lộ nỗi lòng",
           "原形毕露 lộ nguyên hình · 露头 (lòu) ló đầu ra · 出头露面 (lòu) ra mặt · 风餐露宿 ăn gió nằm sương",
           "## 严 (nghiêm): chặt chẽ, nghiêm khắc; mức độ sâu",
           "严峻 nghiêm trọng · 严厉 nghiêm khắc · 严格 nghiêm ngặt · 严寒 giá rét · 严肃 nghiêm túc",
           "严正 nghiêm chỉnh · 严办 xử lý nghiêm · 严明 nghiêm minh · 严冬 mùa đông giá rét · 严重 nghiêm trọng"],
    say=[F(0, "Nhóm thứ ba có chữ Hán Việt là lộ, nghĩa là để lộ ra, bày ra bên ngoài; ngoài ra còn có nghĩa là sương, như trong 风餐露宿. Chữ này có hai cách đọc, các bạn chú ý nghe nhé."),
         F(1, "暴露，表露，透露，流露，吐露心声。 Tức là: phơi bày, biểu lộ, tiết lộ, bộc lộ tình cảm, và thổ lộ nỗi lòng. Trong các từ này, chữ lộ đọc là lù, thanh bốn."),
         F(2, "原形毕露，露头，出头露面，风餐露宿。 Tức là: lộ nguyên hình, ló đầu ra, ra mặt, và ăn gió nằm sương. Chú ý: trong 露头 và 出头露面, chữ lộ đọc là lòu, đây là cách đọc khẩu ngữ. Thành ngữ 风餐露宿 có trong bài khóa."),
         F(3, "Nhóm cuối cùng có chữ 严, Hán Việt là nghiêm, nghĩa là chặt chẽ, nghiêm khắc, hoặc chỉ mức độ rất sâu, rất nặng."),
         F(4, "严峻，严厉，严格，严寒，严肃。 Tức là: nghiêm trọng, nghiêm khắc, nghiêm ngặt, giá rét, nghiêm túc. Từ 严峻 là từ mới của bài: 更严峻的是, điều nghiêm trọng hơn là."),
         F(5, "严正，严办，严明，严冬，严重。 Tức là: nghiêm chỉnh, xử lý nghiêm, nghiêm minh, mùa đông giá rét, và nghiêm trọng."),
         "Các bạn thấy không, chỉ cần nắm nghĩa của một chữ gốc, ta có thể đoán được nghĩa của cả một nhóm từ. Hãy áp dụng cách này khi học từ mới nhé."])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("野生", "yěshēng", "dã sinh", "tính từ", "hoang dã, hoang dại", "野生动物需要我们的保护。", "Động vật hoang dã cần được chúng ta bảo vệ.",
     "Tính từ, nghĩa là hoang dã, sống hoặc mọc tự nhiên, không do con người nuôi trồng. Hay gặp: 野生动物，野生植物. Trái nghĩa là 家养, nuôi trong nhà, hoặc 人工种的, do người trồng."),
    ("压抑", "yāyì", "áp ức", "động từ", "kiềm chế, kìm nén", "他压抑住内心的激动，平静地说完了话。", "Anh ấy kìm nén xúc động trong lòng, bình tĩnh nói hết câu.",
     "Động từ, nghĩa là kìm nén cảm xúc, không để lộ ra ngoài. Trong bài: 压抑住兴奋, kìm nén sự phấn khích. Ngoài ra, 压抑 còn là tính từ, chỉ cảm giác ngột ngạt, nặng nề: 心情很压抑, lòng rất nặng nề."),
    ("完毕", "wánbì", "hoàn tất", "động từ", "hoàn tất, xong", "准备完毕，我们出发吧！", "Chuẩn bị xong rồi, chúng ta xuất phát thôi!",
     "Động từ, nghĩa là hoàn tất, kết thúc, mang màu sắc trang trọng. Thường đứng sau một động từ khác: 拍摄完毕，检查完毕，准备完毕."),
    ("瞪", "dèng", "trừng", "động từ", "nhìn trừng trừng, trợn (mắt)", "她生气地瞪了我一眼。", "Cô ấy tức giận lườm tôi một cái.",
     "Động từ, nghĩa là mở to mắt mà nhìn, trợn mắt, lườm. Có thể vì ngạc nhiên, như 瞪着眼睛 trong bài, cũng có thể vì tức giận, như 瞪了我一眼, lườm tôi một cái. Hán Việt là trừng, như trong trừng mắt."),
    ("注视", "zhùshì", "chú thị", "động từ", "nhìn chăm chú", "全场观众都注视着舞台。", "Cả khán phòng đều chăm chú nhìn lên sân khấu.",
     "Động từ, nghĩa là nhìn chăm chú, dồn ánh mắt vào một chỗ. 注 là dồn vào, 视 là nhìn. Trong bài: 正瞪着眼睛注视着自己, đang trợn tròn mắt chăm chú nhìn mình."),
    ("斑", "bān", "ban", "danh từ", "vằn, đốm, vết lốm đốm", "这种鸟的羽毛上有白色的斑点。", "Lông của loài chim này có những đốm trắng.",
     "Danh từ, chỉ vằn, đốm, vết lốm đốm khác màu trên bề mặt. Hay gặp: 斑点, đốm; 花斑, đốm hoa; 斑马, ngựa vằn. Trong bài: 皮毛上带着美丽花斑, bộ lông mang những đốm hoa tuyệt đẹp."),
    ("濒临", "bīnlín", "tần lâm", "động từ", "kề sát; đứng trước bờ (tình trạng xấu)", "这种植物已经濒临灭绝。", "Loài thực vật này đã đứng trước bờ tuyệt chủng.",
     "Động từ. Nghĩa gốc là kề sát, giáp với sông biển; nghĩa bóng là sắp rơi vào một tình trạng xấu. Hay gặp: 濒临灭绝，濒临消亡，濒临破产. Chú ý: chữ đầu đọc thanh một."),
    ("致力", "zhìlì", "trí lực", "động từ", "dốc sức, tận tụy với", "他一生致力于教育事业。", "Cả đời ông ấy dốc sức cho sự nghiệp giáo dục.",
     "Động từ, nghĩa là dồn hết sức vào một việc. Mẫu cố định là 致力于, cộng danh từ hoặc động từ. Cẩn thận: đừng nhầm với 智力, là trí tuệ, trí thông minh; còn 致力 là đem sức ra cống hiến."),
    ("领袖", "lǐngxiù", "lãnh tụ", "danh từ", "lãnh tụ, người dẫn đầu", "他是这个团队的精神领袖。", "Anh ấy là thủ lĩnh tinh thần của nhóm này.",
     "Danh từ, nghĩa là lãnh tụ, người đứng đầu. Ngày nay còn chỉ người dẫn đầu trong một lĩnh vực: 领袖人物, như Từ Kiện trong bài. Chữ 领 là cổ áo, 袖 là tay áo, là những chỗ nổi bật nhất của chiếc áo."),
    ("辨认", "biànrèn", "biện nhận", "động từ", "nhận ra, nhận biết", "照片太模糊了，我辨认不出这是谁。", "Tấm ảnh mờ quá, tôi không nhận ra đây là ai.",
     "Động từ, nghĩa là dựa vào đặc điểm để nhận ra một đối tượng. Thường dùng 辨认不出, không nhận ra được, như trong bài: 另外四种辨认不出."),
    ("现状", "xiànzhuàng", "hiện trạng", "danh từ", "tình trạng hiện nay", "我们不能满足于现状。", "Chúng ta không thể bằng lòng với hiện trạng.",
     "Danh từ, nghĩa là hiện trạng, tình trạng hiện nay, âm Hán Việt và nghĩa giống hệt tiếng Việt."),
    ("识别", "shíbié", "thức biệt", "động từ", "phân biệt, nhận diện", "这台机器能自动识别人脸。", "Chiếc máy này có thể tự động nhận diện khuôn mặt.",
     "Động từ, nghĩa là phân biệt, nhận diện, biết được cái này khác cái kia. Hay gặp trong công nghệ: 人脸识别, nhận diện khuôn mặt; 语音识别, nhận dạng giọng nói."),
    ("来历", "láilì", "lai lịch", "danh từ", "lai lịch, nguồn gốc", "这件古董的来历很不简单。", "Lai lịch của món đồ cổ này không hề đơn giản.",
     "Danh từ, nghĩa là lai lịch, nguồn gốc, quá trình hình thành của một người hay một vật."),
    ("苦涩", "kǔsè", "khổ sáp", "tính từ", "đắng chát; đau khổ, cay đắng", "他脸上带着苦涩的笑容。", "Trên mặt anh ấy là một nụ cười cay đắng.",
     "Tính từ. Nghĩa gốc là vừa đắng vừa chát, nói về vị; nghĩa bóng là đau khổ, cay đắng trong lòng. Trong bài: 面带苦涩, mặt lộ vẻ cay đắng."),
    ("指望", "zhǐwàng", "chỉ vọng", "động từ", "trông chờ, mong đợi", "你不能什么事都指望别人帮忙。", "Bạn không thể việc gì cũng trông chờ người khác giúp.",
     "Động từ, nghĩa là trông chờ, trông cậy vào. Trong bài: 怎么指望保护？ Làm sao mà trông mong bảo vệ được? Cũng có thể làm danh từ: 没指望了, hết hy vọng rồi."),
    ("严峻", "yánjùn", "nghiêm tuấn", "tính từ", "nghiêm trọng, gay gắt", "我们面临着严峻的考验。", "Chúng ta đang đối mặt với thử thách gay gắt.",
     "Tính từ, chỉ tình hình, thử thách nghiêm trọng, khắc nghiệt. Hay đi với 形势，考验，挑战. Trong bài: 更严峻的是, điều nghiêm trọng hơn là."),
    ("空白", "kòngbái", "không bạch", "danh từ", "chỗ trống; lĩnh vực còn bỏ trống", "请在空白处写上你的名字。", "Hãy viết tên bạn vào chỗ trống.",
     "Danh từ, nghĩa là chỗ trống chưa viết, chưa vẽ gì; nghĩa bóng là lĩnh vực chưa ai làm, chưa có gì: 填补空白, lấp chỗ trống. Trong bài: 影像空白, chưa hề có hình ảnh. Chú ý: chữ đầu đọc thanh bốn."),
    ("琢磨", "zuómo", "trác ma", "động từ", "suy nghĩ, cân nhắc, nghiền ngẫm", "这个问题我琢磨了好几天。", "Vấn đề này tôi nghiền ngẫm mấy ngày liền.",
     "Động từ khẩu ngữ, nghĩa là suy đi tính lại, nghiền ngẫm. Chú ý cách đọc: âm tiết đầu thanh hai, âm tiết sau đọc nhẹ. Cùng cách viết này còn một cách đọc khác, nghĩa là mài giũa ngọc, gọt giũa câu văn; nhưng trong bài, chúng ta đọc như thầy vừa đọc."),
    ("昼夜", "zhòuyè", "trú dạ", "danh từ", "ngày đêm", "医院昼夜都有医生值班。", "Bệnh viện ngày đêm đều có bác sĩ trực.",
     "Danh từ, nghĩa là ngày và đêm, mang màu sắc văn viết. 昼 là ban ngày. Mẫu thường gặp: 不分昼夜, không kể ngày đêm, như trong bài."),
    ("奔波", "bēnbō", "bôn ba", "động từ", "bôn ba, chạy vạy", "为了生活，他每天四处奔波。", "Vì cuộc sống, ngày nào anh ấy cũng bôn ba khắp nơi.",
     "Động từ, nghĩa là bôn ba, chạy vạy vất vả khắp nơi, âm Hán Việt và nghĩa giống tiếng Việt."),
    ("渴望", "kěwàng", "khát vọng", "động từ", "khát khao, ao ước", "孩子们渴望得到父母的理解。", "Bọn trẻ khao khát được cha mẹ thấu hiểu.",
     "Động từ, nghĩa là khát khao, mong mỏi tha thiết. Chú ý: khát vọng trong tiếng Việt là danh từ, còn 渴望 thường là động từ, phía sau có động từ hoặc danh từ: 渴望拍出好照片."),
    ("足以", "zúyǐ", "túc dĩ", "động từ", "đủ để", "这些证据足以证明他是清白的。", "Những bằng chứng này đủ để chứng minh anh ấy trong sạch.",
     "Động từ, nghĩa là hoàn toàn đủ để. Đây là điểm ngữ pháp thứ ba của bài."),
    ("心甘情愿", "xīngān-qíngyuàn", "tâm cam tình nguyện", "thành ngữ", "cam tâm tình nguyện, cam lòng", "为了孩子，她心甘情愿地付出一切。", "Vì con, cô ấy cam lòng hy sinh tất cả.",
     "Thành ngữ, nghĩa là hoàn toàn tự nguyện, vui lòng, không hề miễn cưỡng. Cẩn thận: cam tâm trong tiếng Việt đôi khi mang nghĩa chịu nhục, như cam tâm làm tay sai; còn 心甘情愿 mang nghĩa tích cực: vui lòng làm."),
    ("以便", "yǐbiàn", "dĩ tiện", "liên từ", "để, nhằm (cho dễ…)", "请留下电话号码，以便我们联系你。", "Xin để lại số điện thoại để chúng tôi tiện liên lạc với bạn.",
     "Liên từ, đứng đầu vế câu sau, chỉ mục đích: để cho việc phía sau dễ thực hiện. Lát nữa chúng ta sẽ so sánh kỹ với 便于."),
    ("支撑", "zhīchēng", "chi xanh", "động từ", "chống đỡ; gánh vác, chu cấp", "几根柱子支撑着整个屋顶。", "Mấy cây cột chống đỡ cả mái nhà.",
     "Động từ. Nghĩa gốc là chống đỡ vật nặng; nghĩa bóng là gồng gánh, duy trì: 支撑家庭, gánh vác gia đình. Trong bài: 支撑他们深入野外的巨大开支, gánh được khoản chi phí khổng lồ khi đi sâu vào vùng hoang dã."),
    ("畅销", "chàngxiāo", "sướng tiêu", "động từ", "bán chạy", "这本小说非常畅销。", "Cuốn tiểu thuyết này bán rất chạy.",
     "Động từ, nghĩa là bán chạy. 畅 là thông suốt, 销 là bán. 畅销书 là sách bán chạy. Trái nghĩa là 滞销, bán ế."),
    ("报酬", "bàochou", "báo thù", "danh từ", "thù lao", "这份工作的报酬很高。", "Thù lao của công việc này rất cao.",
     "Danh từ, nghĩa là tiền thù lao, tiền công. Cẩn thận: âm Hán Việt là báo thù, nghe như trả thù, nhưng chữ 酬 ở đây là đền đáp, trả công; chữ thù trong trả thù là một chữ khác: 报仇. Âm tiết thứ hai đọc nhẹ."),
    ("童话", "tónghuà", "đồng thoại", "danh từ", "truyện cổ tích, truyện thiếu nhi", "小时候，妈妈常给我讲童话故事。", "Hồi nhỏ, mẹ thường kể chuyện cổ tích cho tôi nghe.",
     "Danh từ, nghĩa là truyện cổ tích, truyện viết cho trẻ em. Trong bài: 这样的想法，几近童话, ý tưởng ấy gần như chuyện cổ tích, tức là không thực tế."),
    ("课题", "kètí", "khóa đề", "danh từ", "đề tài, vấn đề (nghiên cứu)", "这个研究课题需要两年时间完成。", "Đề tài nghiên cứu này cần hai năm để hoàn thành.",
     "Danh từ, nghĩa là đề tài nghiên cứu, hoặc vấn đề quan trọng cần giải quyết. Trong bài: 为保护区、政府等各类课题提供服务, cung cấp dịch vụ cho các loại đề tài của khu bảo tồn, chính phủ."),
    ("立体", "lìtǐ", "lập thể", "tính từ", "lập thể, ba chiều; nhiều mặt", "这是一部立体电影，要戴眼镜看。", "Đây là phim ba chiều, phải đeo kính để xem.",
     "Tính từ, nghĩa là ba chiều, nổi: 立体电影, phim ba chiều; 立体声, âm thanh nổi. Nghĩa bóng là nhiều mặt, toàn diện: 立体还原, tái hiện một cách toàn diện. Chú ý: lập thể trong tiếng Việt hay dùng cho trường phái hội họa."),
    ("还原", "huányuán", "hoàn nguyên", "động từ", "khôi phục trạng thái, hình dạng ban đầu", "警方还原了事故发生的经过。", "Cảnh sát đã dựng lại diễn biến của vụ tai nạn.",
     "Động từ, nghĩa là khôi phục lại trạng thái hoặc hình dạng ban đầu, tái hiện lại. Chú ý: chữ đầu ở đây đọc là huán, thanh hai, nghĩa là quay về, chứ không đọc như phó từ còn, vẫn."),
    ("名副其实", "míngfùqíshí", "danh phó kỳ thực", "thành ngữ", "danh xứng với thực", "他是一位名副其实的专家。", "Ông ấy là một chuyên gia đúng với danh xưng.",
     "Thành ngữ, nghĩa là danh xứng với thực, tên gọi đúng với thực chất. 副 ở đây là phù hợp. Trái nghĩa là 名不副实, hữu danh vô thực."),
    ("高超", "gāochāo", "cao siêu", "tính từ", "giỏi, điêu luyện, tuyệt vời", "他的厨艺非常高超。", "Tay nghề nấu ăn của anh ấy cực kỳ điêu luyện.",
     "Tính từ, chỉ kỹ thuật, tay nghề giỏi hơn hẳn người thường: 技术高超，医术高超. Cẩn thận: cao siêu trong tiếng Việt thường là khó hiểu, xa vời; còn 高超 là giỏi, điêu luyện."),
    ("素质", "sùzhì", "tố chất", "danh từ", "tố chất, phẩm chất, năng lực", "我们要不断提高自己的专业素质。", "Chúng ta phải không ngừng nâng cao năng lực chuyên môn của mình.",
     "Danh từ, chỉ phẩm chất, trình độ, năng lực. Hay gặp: 专业素质，心理素质，身体素质. Chú ý: tố chất trong tiếng Việt thiên về năng khiếu bẩm sinh; còn 素质 rộng hơn, gồm cả văn hóa, ý thức: 素质很高 là người có văn hóa, có ý thức."),
    ("号召", "hàozhào", "hiệu triệu", "động từ", "kêu gọi, hiệu triệu", "学校号召同学们节约用水。", "Nhà trường kêu gọi học sinh tiết kiệm nước.",
     "Động từ, nghĩa là kêu gọi đông người cùng làm một việc. Cũng làm danh từ: 发出号召, phát lời kêu gọi, như trong bài."),
    ("证实", "zhèngshí", "chứng thực", "động từ", "chứng thực, xác nhận", "这个消息已经得到了证实。", "Tin này đã được xác nhận.",
     "Động từ, nghĩa là chứng minh là đúng, xác nhận. Trong bài: 实践证实, thực tế đã chứng minh."),
    ("成效", "chéngxiào", "thành hiệu", "danh từ", "hiệu quả, kết quả", "经过半年的努力，工作终于有了成效。", "Sau nửa năm nỗ lực, công việc cuối cùng đã có kết quả.",
     "Danh từ, nghĩa là kết quả, hiệu quả đạt được. Hay đi với 显著: 成效显著, hiệu quả rõ rệt, như trong bài."),
    ("显著", "xiǎnzhù", "hiển trứ", "tính từ", "rõ rệt, nổi bật", "他的成绩有了显著的提高。", "Thành tích của cậu ấy tiến bộ rõ rệt.",
     "Tính từ, nghĩa là rõ rệt, dễ thấy. Hay đi với 成效，变化，提高，效果."),
    ("用户", "yònghù", "dụng hộ", "danh từ", "người dùng", "这款手机很受用户欢迎。", "Mẫu điện thoại này rất được người dùng ưa chuộng.",
     "Danh từ, nghĩa là người sử dụng một sản phẩm hay dịch vụ. Chữ 户 là hộ, như hộ gia đình."),
    ("浓厚", "nónghòu", "nùng hậu", "tính từ", "đậm đặc; sâu đậm, đậm đà", "他对中国文化有浓厚的兴趣。", "Anh ấy có hứng thú sâu đậm với văn hóa Trung Quốc.",
     "Tính từ. Nghĩa gốc là khói, mây dày đặc; nghĩa bóng là hứng thú, không khí, màu sắc đậm đà: 浓厚的兴趣，浓厚的节日气氛. Trong bài: 浓厚的科考性质, đậm tính chất khảo sát khoa học."),
    ("统计", "tǒngjì", "thống kê", "động từ", "thống kê", "请统计一下参加会议的人数。", "Hãy thống kê số người tham dự cuộc họp.",
     "Động từ, nghĩa là thống kê, âm Hán Việt và nghĩa giống hệt tiếng Việt."),
    ("权威", "quánwēi", "quyền uy", "tính từ", "có uy tín, có thẩm quyền", "他是这个领域的权威专家。", "Ông ấy là chuyên gia có uy tín nhất trong lĩnh vực này.",
     "Tính từ, nghĩa là có uy tín, có thẩm quyền, đáng tin cậy nhất. Cũng làm danh từ: 医学权威, người có uy tín trong ngành y. Chú ý: quyền uy tiếng Việt thiên về quyền lực; còn 权威 thường là uy tín chuyên môn."),
    ("鉴别", "jiànbié", "giám biệt", "động từ", "phân biệt, giám định", "专家正在鉴别这幅画的真假。", "Chuyên gia đang giám định thật giả của bức tranh này.",
     "Động từ, nghĩa là xem xét kỹ để phân biệt thật giả, tốt xấu, hoặc xác định chủng loại. Trong bài: 物种鉴别, xác định loài."),
    ("评估", "pínggū", "bình cổ", "động từ", "đánh giá", "我们需要对这个项目进行风险评估。", "Chúng ta cần tiến hành đánh giá rủi ro cho dự án này.",
     "Động từ, nghĩa là đánh giá, thẩm định giá trị hoặc mức độ. Trong bài: 环境评估调查报告, báo cáo điều tra đánh giá môi trường."),
    ("队伍", "duìwu", "đội ngũ", "danh từ", "đội ngũ, hàng ngũ", "我们的研究队伍越来越大了。", "Đội ngũ nghiên cứu của chúng tôi ngày càng lớn mạnh.",
     "Danh từ, nghĩa là đội ngũ, tập thể người cùng làm một việc; cũng chỉ hàng người xếp nối nhau. Âm tiết thứ hai đọc nhẹ."),
]

add("bullets", chapter="Từ mới (45 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 16 có 45 từ mới, chia thành 15 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 空白 (kòng) · 琢磨 (zuómo) · 还原 (huán) · 报酬 (chou)",
           "Từ dễ nhầm: 报酬 · 高超 · 素质 · 心甘情愿 · 权威"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có bốn mươi lăm từ, thầy chia thành mười lăm nhóm nhỏ, mỗi nhóm ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Một số từ có âm đọc cần chú ý, như 空白，琢磨，还原，报酬. Thầy sẽ nhắc khi gặp."),
         F(4, "Ngoài ra, có mấy từ Hán Việt rất dễ hiểu nhầm, như 报酬，高超，素质，心甘情愿，权威. Nghĩa của chúng trong tiếng Trung khác với tiếng Việt, các bạn nhớ nghe kỹ phần giải thích nhé. Chúng ta bắt đầu.")])

sizes = [3] * 15
assert sum(sizes) == len(V)
g = 0
for gs in sizes:
    group = V[g:g + gs]
    words, say = [], []
    for i, item in enumerate(group):
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
    ("中国青海，海拔4500米的山上，3头雪豹正在玩耍。野生动植物摄影师们压抑住兴奋，憋住气，全力拍摄雪豹。",
     "Thanh Hải, Trung Quốc, trên ngọn núi cao bốn nghìn năm trăm mét so với mực nước biển, ba con báo tuyết đang nô đùa. Các nhiếp ảnh gia động thực vật hoang dã kìm nén sự phấn khích, nín thở, dồn hết sức chụp những con báo tuyết.",
     ["青海 là tỉnh Thanh Hải, nằm trên cao nguyên Thanh Tạng; theo chú thích của sách, sông Trường Giang và Hoàng Hà đều bắt nguồn từ đây. 海拔 là độ cao so với mực nước biển. 头 là lượng từ cho con vật lớn: 三头雪豹.",
      "憋住气 là nín thở. 压抑住 và 憋住 đều dùng bổ ngữ 住, chỉ giữ chặt, kìm lại. 全力 là dốc toàn lực."],
     "中国青海，海拔四千五百米的山上，三头雪豹正在玩耍。野生动植物摄影师们压抑住兴奋，憋住气，全力拍摄雪豹。"),
    ("拍摄完毕，一回头，发现两只藏在山头的雪豹正瞪着眼睛注视着自己，大家相视而笑。",
     "Chụp xong, vừa quay đầu lại, họ phát hiện hai con báo tuyết nấp trên đỉnh núi đang trợn tròn mắt chăm chú nhìn mình, mọi người nhìn nhau mà cười.",
     ["藏在山头 là nấp trên đỉnh núi; ở đây chữ tàng đọc là cáng, nghĩa là ẩn nấp. 一回头 là vừa quay đầu lại, 一 cộng động từ chỉ hành động vừa xảy ra thì có ngay kết quả.",
      "相视而笑 là nhìn nhau mà cười. Đoạn mở đầu rất sinh động: người chụp ảnh báo tuyết, hóa ra lại bị báo tuyết quan sát."]),
    ("雪豹，这种皮毛上带着美丽花斑的大型猫科动物正濒临消亡，换句话说，在不久的将来我们很可能再也见不到这种动物。",
     "Báo tuyết, loài động vật họ mèo cỡ lớn mang những đốm hoa tuyệt đẹp trên bộ lông, đang đứng trước nguy cơ biến mất; nói cách khác, trong tương lai không xa, rất có thể chúng ta sẽ không bao giờ được nhìn thấy loài vật này nữa.",
     ["Câu có định ngữ dài: 这种皮毛上带着美丽花斑的大型猫科动物, trung tâm là 动物. 猫科 là họ mèo. 濒临消亡 là sắp bị tiêu vong.",
      "换句话说 là nói cách khác, dùng để giải thích lại vế trước cho dễ hiểu hơn. Đây là điểm ngữ pháp thứ nhất của bài."]),
    ("而这些摄影师们是致力于保护野生物种，记录和展示中国生物多样性的“博物学家”。长期风餐露宿在山野，他们不但不觉得苦，反而感到无比的快乐。",
     "Còn những nhiếp ảnh gia này là những nhà tự nhiên học dốc sức bảo vệ các loài hoang dã, ghi lại và giới thiệu sự đa dạng sinh học của Trung Quốc. Lâu ngày ăn gió nằm sương nơi núi rừng, họ không những không thấy khổ, mà còn cảm thấy vô cùng vui sướng.",
     ["致力于 là dốc sức vào. 物种 là loài, giống loài. 生物多样性 là đa dạng sinh học. 博物学家 là nhà tự nhiên học, người nghiên cứu động vật, thực vật, khoáng vật trong tự nhiên.",
      "风餐露宿 là ăn gió nằm sương. Mẫu 不但不……，反而…… nghĩa là không những không…, mà ngược lại còn…, dùng để nhấn mạnh kết quả trái với dự đoán."]),
    ("徐健是摄影师中的领袖人物，IBE的创始人，他拿出8张照片，我认识大熊猫、金丝猴、牦牛和雪豹，另外4种辨认不出，据说，它们是藏狐、赤斑羚、藏羚羊和喜马拉雅旱獭。",
     "Từ Kiện là nhân vật dẫn đầu trong số các nhiếp ảnh gia, là người sáng lập IBE. Anh ấy lấy ra tám tấm ảnh, tôi nhận ra gấu trúc lớn, khỉ lông vàng, bò Tây Tạng và báo tuyết, còn bốn loài kia thì không nhận ra; nghe nói, chúng là cáo Tây Tạng, sơn dương đỏ, linh dương Tây Tạng và macmot Himalaya.",
     ["Theo chú thích của sách, IBE là viết tắt của Imaging Biodiversity Expedition, tiếng Trung là 影像生物多样性调查所, tức là nhóm khảo sát đa dạng sinh học bằng hình ảnh. 创始人 là người sáng lập. 金丝猴 là khỉ lông vàng.",
      "辨认不出 là không nhận ra được. 据说 là nghe nói, cũng là một thành phần chen, cho biết nguồn tin. Chúng ta sẽ học kỹ ở phần mở rộng."],
     "徐健是摄影师中的领袖人物，IBE的创始人，他拿出八张照片，我认识大熊猫、金丝猴、牦牛和雪豹，另外四种辨认不出，据说，它们是藏狐、赤斑羚、藏羚羊和喜马拉雅旱獭。"),
    ("徐健说：“我们的现状是，人们能识别长颈鹿、大猩猩、河马，知道它们的来历，却不认识藏羚羊，大家对非洲的动物好像比对我们自己国家的动物更为熟悉。”",
     "Từ Kiện nói: Hiện trạng của chúng ta là, mọi người có thể nhận ra hươu cao cổ, khỉ đột, hà mã, biết nguồn gốc của chúng, nhưng lại không biết linh dương Tây Tạng; mọi người dường như quen thuộc với động vật châu Phi hơn là với động vật của chính đất nước mình.",
     ["长颈鹿 là hươu cao cổ, 大猩猩 là khỉ đột, 河马 là hà mã, đều là động vật châu Phi. 却 là nhưng lại, biểu thị chuyển ý.",
      "Câu so sánh 对A比对B更为熟悉 nghĩa là quen thuộc với A hơn với B. 更为 là càng, hơn, mang màu sắc văn viết, giống 更加."]),
    ("徐健面带苦涩地说：“许多动植物，连一张清楚的照片都没有，大家不认识，怎么指望保护？更严峻的是自然保护区的影像空白，很多特有物种，还没来得及为我们所了解，就消失了。”",
     "Từ Kiện mặt lộ vẻ cay đắng nói: Rất nhiều loài động thực vật, đến một tấm ảnh rõ ràng cũng không có, mọi người không biết chúng, thì làm sao trông mong bảo vệ? Nghiêm trọng hơn là khu bảo tồn thiên nhiên còn trống trơn về hình ảnh, rất nhiều loài đặc hữu chưa kịp được chúng ta biết đến thì đã biến mất rồi.",
     ["连……都…… là ngay cả… cũng…. 怎么指望保护？ là câu hỏi tu từ, nghĩa là không thể trông mong bảo vệ được. 特有物种 là loài đặc hữu, chỉ có ở một vùng.",
      "还没来得及……就…… là chưa kịp… thì đã…. 为我们所了解 là được chúng ta biết đến; đây là cấu trúc bị động văn viết 为所, điểm ngữ pháp thứ hai của bài."]),
    ("徐健和他的朋友曾苦苦琢磨，怎样为野生动物保护尽一份责任。",
     "Từ Kiện và những người bạn của anh ấy từng trăn trở suy nghĩ, làm thế nào để góp một phần trách nhiệm cho việc bảo vệ động vật hoang dã.",
     ["曾 là đã từng, văn viết, giống 曾经. 苦苦琢磨 là trăn trở, vắt óc suy nghĩ; 苦苦 là lặp lại để nhấn mạnh sự vất vả.",
      "尽一份责任 là góp một phần trách nhiệm; chữ 尽 ở đây đọc thanh bốn, nghĩa là làm hết sức. Ở đây 为 đọc thanh bốn, nghĩa là vì, cho."]),
    ("他们不分昼夜地奔波，渴望拍出足以使人疯狂的照片，吸引大家心甘情愿地去购买，以便支撑他们深入野外的巨大开支，但摄影作品不是畅销书，摄影师报酬很低，这样的想法，几近童话。",
     "Họ bôn ba không kể ngày đêm, khao khát chụp được những bức ảnh đủ để khiến người ta phát cuồng, thu hút mọi người vui lòng bỏ tiền ra mua, để gánh được khoản chi phí khổng lồ cho những chuyến đi sâu vào vùng hoang dã. Nhưng tác phẩm nhiếp ảnh không phải sách bán chạy, thù lao của nhiếp ảnh gia rất thấp, ý tưởng ấy gần như chuyện cổ tích.",
     ["Câu này có hai điểm quan trọng: 足以使人疯狂, đủ để khiến người ta phát cuồng, là điểm ngữ pháp 足以; còn 以便支撑……开支, để gánh được chi phí, là từ 以便 trong phần phân biệt từ.",
      "几近 là gần như, văn viết; ở đây chữ đầu đọc là jī, thanh một. 几近童话 nghĩa là ý tưởng ấy đẹp nhưng không thực tế."]),
    ("于是徐健成立了社会企业IBE，为保护区、政府等各类课题提供服务，他们的工作是建立野生动植物影像库，立体还原一个地区的生态多样性。",
     "Thế là Từ Kiện thành lập doanh nghiệp xã hội IBE, cung cấp dịch vụ cho các loại đề tài của khu bảo tồn, chính phủ…; công việc của họ là xây dựng kho hình ảnh động thực vật hoang dã, tái hiện một cách toàn diện sự đa dạng sinh thái của một vùng.",
     ["社会企业 là doanh nghiệp xã hội, tức doanh nghiệp hoạt động vì mục tiêu xã hội chứ không chỉ vì lợi nhuận. 为……提供服务 là cung cấp dịch vụ cho….",
      "影像库 là kho hình ảnh. 立体还原 là tái hiện lại một cách nhiều chiều, toàn diện. 生态 là sinh thái."]),
    ("IBE的摄影师个个是名副其实的博物学家，不但有高超的摄影技术，还有非同一般的专业素质。",
     "Các nhiếp ảnh gia của IBE ai cũng là nhà tự nhiên học đúng nghĩa, không những có kỹ thuật chụp ảnh điêu luyện, mà còn có năng lực chuyên môn khác thường.",
     ["个个 là người nào cũng, ai ai cũng; lượng từ lặp lại chỉ toàn bộ. 名副其实 là danh xứng với thực.",
      "非同一般 là khác hẳn bình thường, không tầm thường. Mẫu 不但……，还…… là không những…, mà còn…."]),
    ("他们分散在全国各地，徐健一发出号召，大家立刻聚在一起。实践证实，这种集合式工作成效显著，用户也很喜欢他们的作品。",
     "Họ phân tán khắp nơi trên cả nước, Từ Kiện vừa phát lời kêu gọi, mọi người lập tức tụ họp lại. Thực tế đã chứng minh, cách làm việc tập hợp này đạt hiệu quả rõ rệt, người dùng cũng rất thích tác phẩm của họ.",
     ["一……，就…… là vừa… thì…; ở đây vế sau dùng 立刻, lập tức: 一发出号召，大家立刻聚在一起. 分散 là phân tán, trái nghĩa với 聚 là tụ họp.",
      "实践证实 là thực tế chứng minh. 集合式工作 là cách làm việc tập hợp lại khi có nhiệm vụ. 成效显著 là hiệu quả rõ rệt."]),
    ("IBE的作品带有浓厚的科考性质，每张照片都有详细的数据可供使用，比如精确统计的动物数量。",
     "Tác phẩm của IBE mang đậm tính chất khảo sát khoa học, mỗi tấm ảnh đều có số liệu chi tiết để sử dụng, ví dụ như số lượng động vật được thống kê chính xác.",
     ["科考 là khảo sát khoa học, viết tắt của 科学考察. 带有……性质 là mang tính chất….",
      "可供使用 là có thể dùng được; chữ 供 ở đây đọc thanh một, nghĩa là cung cấp. 精确 là chính xác."]),
    ("一次在梅里雪山遇见大紫胸鹦鹉群，摄影师在Photoshop上一个一个地数，统计出1500只的精确数据，之后权威专家表示，这是有记录以来，近30年此地区出现的最大规模鹦鹉越冬群。",
     "Có một lần ở núi tuyết Mai Lý, họ gặp một đàn vẹt ngực tím lớn. Nhiếp ảnh gia đếm từng con một trên Photoshop, thống kê được số liệu chính xác là một nghìn năm trăm con. Sau đó các chuyên gia có uy tín cho biết, đây là đàn vẹt trú đông quy mô lớn nhất xuất hiện ở vùng này trong gần ba mươi năm, kể từ khi có ghi chép.",
     ["梅里雪山 là núi tuyết Mai Lý, ở giáp ranh Vân Nam và Tây Tạng. 一个一个地数 là đếm từng con một; chữ 数 ở đây đọc thanh ba, là động từ đếm.",
      "有记录以来 là kể từ khi có ghi chép. 越冬 là trú đông, qua mùa đông. Con số chính xác này cho thấy tính khoa học của ảnh IBE."],
     "一次在梅里雪山遇见大紫胸鹦鹉群，摄影师在Photoshop上一个一个地数，统计出一千五百只的精确数据，之后权威专家表示，这是有记录以来，近三十年此地区出现的最大规模鹦鹉越冬群。"),
    ("拍摄同时，他们还进行物种鉴别、动物行为分析等。项目结束后，他们还会向当地保护区提交一份环境评估调查报告。如今，徐健和他的队伍天天在路上忙碌着。",
     "Cùng lúc chụp ảnh, họ còn tiến hành xác định loài, phân tích hành vi động vật… Sau khi dự án kết thúc, họ còn nộp cho khu bảo tồn địa phương một bản báo cáo điều tra đánh giá môi trường. Ngày nay, Từ Kiện và đội ngũ của anh ấy ngày ngày bận rộn trên đường.",
     ["进行 cộng danh từ hai âm tiết là tiến hành việc gì: 进行物种鉴别，进行分析. 向……提交 là nộp cho…. 一份报告 là một bản báo cáo.",
      "忙碌 là bận rộn. Câu kết ngắn gọn, cho thấy công việc của họ vẫn đang tiếp tục. Bài được cải biên từ một bài báo trên tạp chí 人物, tức tạp chí Nhân vật."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 徐健和他的野生动物摄影师们", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa 徐健和他的野生动物摄影师们, dài tám trăm chín mươi tám chữ. Bài được cải biên từ một bài báo trên tạp chí 人物, tức tạp chí Nhân vật, viết về tiêu chuẩn chọn nhiếp ảnh gia của nhóm IBE.",
         F(0, "Thầy chia bài thành mười lăm đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh
    spoken = spoken.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 100 else 50
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Tóm tắt nội dung", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5) – phần 1", size=34,
    items=["## 1. 徐健他们的工作是什么？",
           "野生动植物摄影师 · 博物学家：致力于保护野生物种，记录和展示中国生物多样性",
           "## 2. 为什么大家对非洲生物的熟悉程度远远大于自己的国家？",
           "影像空白：许多动植物连一张清楚的照片都没有，大家不认识",
           "## 3. 徐健他们以前希望照片可以怎样？结果呢？",
           "吸引大家心甘情愿地去购买，支撑深入野外的巨大开支 · 但不是畅销书，报酬很低，几近童话"],
    say=["Bài tập năm của sách yêu cầu dựa vào gợi ý để trả lời câu hỏi về nội dung bài khóa. Chúng ta cùng làm luôn nhé, đây cũng là bố cục của bài.",
         F(0, "Câu hỏi một: công việc của Từ Kiện và các bạn là gì?"),
         F(1, "Trả lời: họ là 野生动植物摄影师, nhiếp ảnh gia động thực vật hoang dã, đồng thời là 博物学家, những nhà tự nhiên học dốc sức bảo vệ các loài hoang dã, ghi lại và giới thiệu sự đa dạng sinh học của Trung Quốc."),
         F(2, "Câu hỏi hai: vì sao mọi người quen thuộc với sinh vật châu Phi hơn nhiều so với sinh vật của chính nước mình?"),
         F(3, "Trả lời: vì 影像空白, chưa có hình ảnh. 许多动植物连一张清楚的照片都没有，大家不认识。 Nhiều loài đến một tấm ảnh rõ ràng cũng không có, nên mọi người không biết đến chúng."),
         F(4, "Câu hỏi ba: trước đây, Từ Kiện và các bạn mong những bức ảnh mình chụp có thể thế nào? Kết quả ra sao?"),
         F(5, "Trả lời: họ mong ảnh 吸引大家心甘情愿地去购买, thu hút mọi người vui lòng mua, để 支撑深入野外的巨大开支, gánh được chi phí đi vào vùng hoang dã. Nhưng ảnh không phải sách bán chạy, thù lao rất thấp, nên ý tưởng ấy 几近童话, gần như chuyện cổ tích.")])

add("bullets", section="Bài khóa 课文", title="Bố cục bài khóa (theo bài tập 5) – phần 2", size=34,
    items=["## 4. IBE的工作内容和工作方式分别是什么？",
           "内容：为保护区、政府等提供服务，建立野生动植物影像库，立体还原一个地区的生态多样性",
           "方式：摄影师分散在全国各地，徐健一号召，就聚在一起，集合式工作",
           "## 5. 为什么说IBE的作品带有浓厚的科考性质？",
           "每张照片都有详细的数据可供使用 · 精确统计动物数量 · 物种鉴别、动物行为分析 · 提交环境评估调查报告"],
    say=[F(0, "Câu hỏi bốn: nội dung công việc và cách làm việc của IBE lần lượt là gì?"),
         F(1, "Trả lời: về nội dung, họ cung cấp dịch vụ cho các đề tài của khu bảo tồn, chính phủ; xây dựng kho hình ảnh động thực vật hoang dã, và tái hiện toàn diện sự đa dạng sinh thái của một vùng."),
         F(2, "Về cách làm việc: các nhiếp ảnh gia phân tán khắp cả nước, Từ Kiện vừa kêu gọi là mọi người tụ họp lại, làm việc theo kiểu tập hợp."),
         F(3, "Câu hỏi năm: vì sao nói tác phẩm của IBE mang đậm tính chất khảo sát khoa học?"),
         F(4, "Trả lời: vì mỗi tấm ảnh đều có số liệu chi tiết để sử dụng, như số lượng động vật được thống kê chính xác; họ còn xác định loài, phân tích hành vi động vật, và nộp báo cáo điều tra đánh giá môi trường cho khu bảo tồn. Bố cục này rất có ích khi các bạn tự kể lại bài khóa.")])

# ======================= NGỮ PHÁP =======================
add("bullets", chapter="Ngữ pháp: 换句话说", section="Ngữ pháp 注释", title="1. 换句话说 – nói cách khác", size=34,
    items=["Thành phần chen (插入语), dùng để giải thích, nói rõ thêm ý vừa nêu",
           "雪豹，这种皮毛上带着美丽花斑的大型猫科动物正濒临消亡，换句话说，在不久的将来我们很可能再也见不到这种动物。",
           "推销产品靠的是广告，但是做广告需要高额资金，这笔广告费最终还是会转嫁到产品上。换句话说，一个产品的广告越多，它的零售价格也会越高。",
           "## Cùng loại còn có: 也就是说 · 就是说",
           "科学教育多了，人文教育就得少一些……也就是说，加强了科学教育就等于挖了人文教育的墙角……",
           "每个国家都应与他国和睦相处，尽其该尽的国际义务。就是说，国家拥有主权，但并不是可以为所欲为的。"],
    say=["Bây giờ chúng ta sang phần ngữ pháp. Điểm thứ nhất là 换句话说.",
         F(0, "换句话说 là một thành phần chen, tiếng Trung gọi là 插入语. Nghĩa đen là đổi một câu khác mà nói, tức là nói cách khác. Nó dùng để giải thích, nói rõ thêm ý của vế trước bằng một cách dễ hiểu hơn, cụ thể hơn."),
         F(1, "Ví dụ một, lấy từ bài khóa: 雪豹，这种皮毛上带着美丽花斑的大型猫科动物正濒临消亡，换句话说，在不久的将来我们很可能再也见不到这种动物。 Báo tuyết đang đứng trước nguy cơ biến mất, nói cách khác, trong tương lai không xa, có thể ta sẽ không bao giờ được thấy chúng nữa. Vế sau nói lại ý濒临消亡 một cách cụ thể hơn."),
         F(2, "Ví dụ hai: 推销产品靠的是广告，但是做广告需要高额资金，这笔广告费最终还是会转嫁到产品上。换句话说，一个产品的广告越多，它的零售价格也会越高。 Quảng bá sản phẩm dựa vào quảng cáo, nhưng quảng cáo cần rất nhiều tiền, khoản phí này cuối cùng sẽ bị đẩy vào giá sản phẩm. Nói cách khác, sản phẩm càng quảng cáo nhiều thì giá bán lẻ càng cao."),
         F(3, "Những thành phần chen cùng loại thường dùng còn có 也就是说 và 就是说, nghĩa là tức là, cũng có nghĩa là."),
         F(4, "Ví dụ ba: 科学教育多了，人文教育就要少一些；人文教育多了，科学教育就要少一些。也就是说，加强了科学教育就等于挖了人文教育的墙角。 Giáo dục khoa học nhiều thì giáo dục nhân văn phải ít đi, và ngược lại. Tức là, tăng cường giáo dục khoa học cũng bằng như đào chân tường của giáo dục nhân văn. 挖墙角 là đào chân tường, nghĩa bóng là làm hại, làm suy yếu bên kia.",
           cap="Ví dụ ba: 科学教育多了，人文教育就得少一些；人文教育多了，科学教育就得少一些。也就是说，加强了科学教育就等于挖了人文教育的墙角。 Giáo dục khoa học nhiều thì giáo dục nhân văn phải ít đi, và ngược lại. Tức là, tăng cường giáo dục khoa học cũng bằng như đào chân tường của giáo dục nhân văn. 挖墙角 là đào chân tường, nghĩa bóng là làm hại, làm suy yếu bên kia."),
         F(5, "Ví dụ bốn: 每个国家都应与他国和睦相处，尽其该尽的国际义务。就是说，国家拥有主权，但并不是可以为所欲为的。 Mỗi quốc gia đều nên chung sống hòa thuận với nước khác, làm tròn nghĩa vụ quốc tế của mình. Tức là, quốc gia có chủ quyền, nhưng không phải muốn làm gì thì làm.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: nối hai câu bằng 换句话说", reveal=True, size=34,
    items=["A. 结婚前要睁大眼睛仔细瞧，结婚后就要睁一只眼闭一只眼 · B. 武松赤手空拳打死了老虎 · C. 世界上每小时就有五千个孩子出生",
           "D. 武松什么武器都没用，就用拳头打死了老虎 · E. 婚前要多看看对方的短处，婚后要多想想对方的长处 · F. 每天地球上就要多出十二万人",
           "(1) 有人这样说，结婚前要睁大眼睛仔细瞧，结婚后就要睁一只眼闭一只眼……",
           "Đáp án: A + E: ……，换句话说，婚前要多看看对方的短处，婚后要多想想对方的长处。",
           "(2) 中国古典小说《水浒传》中的武松赤手空拳打死了老虎……",
           "Đáp án: B + D: ……，换句话说，武松什么武器都没用，就用拳头打死了老虎。",
           "(3) 现在，世界上每小时就有五千个孩子出生……",
           "Đáp án: C + F: ……，换句话说，每天地球上就要多出十二万人。"],
    say=[F(0, "Luyện tập: sách cho sáu câu nhỏ, từng cặp câu nói về cùng một sự việc. Hãy dùng 换句话说 để nối chúng thành câu dài có ý giải thích. A: 结婚前要睁大眼睛仔细瞧，结婚后就要睁一只眼闭一只眼. Trước khi cưới phải mở to mắt mà nhìn kỹ, sau khi cưới thì nên nhắm một mắt mở một mắt. B: 武松赤手空拳打死了老虎. Võ Tòng tay không đánh chết hổ. C: 世界上每小时就有五千个孩子出生. Trên thế giới mỗi giờ có năm nghìn đứa trẻ ra đời."),
         F(1, "D: 武松什么武器都没用，就用拳头打死了老虎. Võ Tòng không dùng vũ khí gì cả, chỉ dùng nắm đấm đánh chết hổ. E: 婚前要多看看对方的短处，婚后要多想想对方的长处. Trước khi cưới nên nhìn nhiều vào khuyết điểm của đối phương, sau khi cưới nên nghĩ nhiều đến ưu điểm của họ. F: 每天地球上就要多出十二万人. Mỗi ngày trái đất lại có thêm mười hai vạn người. Các bạn tạm dừng và ghép cặp thử nhé."),
         F(2, "Câu một: 有人这样说，结婚前要睁大眼睛仔细瞧，结婚后就要睁一只眼闭一只眼。 Câu này đi với câu nào?"),
         F(3, "Đáp án: A đi với E. 换句话说，婚前要多看看对方的短处，婚后要多想想对方的长处。 Vế sau giải thích ý của câu nói hình ảnh ở vế trước."),
         F(4, "Câu hai: 中国古典小说水浒传中的武松赤手空拳打死了老虎。 Trong tiểu thuyết cổ điển Thủy Hử, Võ Tòng tay không đánh chết hổ."),
         F(5, "Đáp án: B đi với D. 换句话说，武松什么武器都没用，就用拳头打死了老虎。 Vế sau giải thích thành ngữ 赤手空拳, tay không."),
         F(6, "Câu ba: 现在，世界上每小时就有五千个孩子出生。"),
         F(7, "Đáp án: C đi với F. 换句话说，每天地球上就要多出十二万人。 Năm nghìn nhân hai mươi bốn giờ là mười hai vạn, nên vế sau nói lại cùng một sự thật bằng một con số khác.")])

add("bullets", chapter="Ngữ pháp: 为……所……", section="Ngữ pháp 注释", title="2. 为……所…… wéi…suǒ… – bị, được (bị động)", size=34,
    items=["Giới thiệu chủ thể hành động, tạo câu bị động; dùng trong văn viết",
           "## Khẳng định: 为 + danh từ / cụm danh từ + 所 + động từ",
           "更严峻的是自然保护区的影像空白，很多特有物种，还没来得及为我们所了解，就消失了。",
           "我们要通过教育，使原来为少数人所掌握的科学知识，在较短的时间内为更多的人所掌握，并不断扩大其传播范围。",
           "## Phủ định: 不 + 为 + danh từ / cụm danh từ + 所 + động từ",
           "他是个有原则的人，绝不会为金钱所惑。",
           "说到那个电影，没有一个人不喜欢，没有一个人不为电影中的人物所感动。"],
    say=["Điểm ngữ pháp thứ hai là cấu trúc 为所. Chú ý: trong cấu trúc này, chữ 为 đọc là wéi, thanh hai.",
         F(0, "Cấu trúc này dùng để giới thiệu chủ thể của hành động, tạo thành câu bị động, giống 被, nhưng mang màu sắc văn viết, trang trọng. Tiếng Việt dịch là bị, được."),
         F(1, "Dạng khẳng định: 为, cộng danh từ hoặc cụm danh từ, cộng 所, cộng động từ. Danh từ ở giữa chính là người thực hiện hành động."),
         F(2, "Ví dụ một, lấy từ bài khóa: 更严峻的是自然保护区的影像空白，很多特有物种，还没来得及为我们所了解，就消失了。 Nhiều loài đặc hữu chưa kịp được chúng ta biết đến thì đã biến mất. 为我们所了解 tức là 被我们了解."),
         F(3, "Ví dụ hai: 我们要通过教育，使原来为少数人所掌握的科学知识，在较短的时间内为更多的人所掌握，并不断扩大其传播范围。 Chúng ta phải thông qua giáo dục, làm cho tri thức khoa học vốn chỉ một số ít người nắm được, trong thời gian ngắn được nhiều người hơn nắm vững, và không ngừng mở rộng phạm vi lan truyền của nó."),
         F(4, "Dạng phủ định: thêm 不 vào trước 为: 不, cộng 为, cộng danh từ, cộng 所, cộng động từ."),
         F(5, "Ví dụ ba: 他是个有原则的人，绝不会为金钱所惑。 Anh ấy là người có nguyên tắc, tuyệt đối không bị đồng tiền mê hoặc."),
         F(6, "Ví dụ bốn: 说到那个电影，没有一个人不喜欢，没有一个人不为电影中的人物所感动。 Nói đến bộ phim đó, không ai là không thích, không ai là không bị các nhân vật trong phim làm cho cảm động.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: hoàn thành câu với 为……所……", reveal=True, size=36,
    items=["(1) 京酱肉丝这道菜______。（很多人，称道）",
           "Đáp án: 京酱肉丝这道菜为很多人所称道。",
           "(2) 连日大雪，部分牧民______，日前，救助他们的队伍已经出发，会给他们带去食品和衣物。（大雪，困）",
           "Đáp án: 连日大雪，部分牧民为大雪所困，……",
           "(3) 废气、废水有望真正变废为宝，______。（人们，利用）",
           "Đáp án: 废气、废水有望真正变废为宝，为人们所利用。"],
    say=[F(0, "Luyện tập: tham khảo từ gợi ý, dùng cấu trúc 为所 để hoàn thành câu. Câu một: 京酱肉丝这道菜什么。 Gợi ý: 很多人，称道. Món thịt xào tương Bắc Kinh thế nào? 称道 là khen ngợi. Các bạn tạm dừng và thử hoàn thành câu nhé."),
         F(1, "Đáp án: 京酱肉丝这道菜为很多人所称道。 Món thịt xào tương Bắc Kinh được rất nhiều người khen ngợi."),
         F(2, "Câu hai: 连日大雪，部分牧民什么，日前，救助他们的队伍已经出发，会给他们带去食品和衣物。 Gợi ý: 大雪，困. Tuyết rơi nhiều ngày liền, một số người chăn nuôi thế nào; mấy hôm trước, đội cứu trợ đã xuất phát, sẽ mang thức ăn và quần áo đến cho họ."),
         F(3, "Đáp án: 部分牧民为大雪所困。 Một số người chăn nuôi bị tuyết lớn vây hãm. 困 là vây khốn, mắc kẹt."),
         F(4, "Câu ba: 废气、废水有望真正变废为宝，什么。 Gợi ý: 人们，利用. Khí thải, nước thải có triển vọng thật sự biến phế liệu thành của quý, và thế nào?"),
         F(5, "Đáp án: 为人们所利用。 Được con người tận dụng. Chú ý thành ngữ 变废为宝, biến phế thành bảo, cũng đọc là wéi, nghĩa là trở thành.")])

add("bullets", chapter="Ngữ pháp: 足以", section="Ngữ pháp 注释", title="3. 足以 zúyǐ – đủ để", size=36,
    items=["Động từ: hoàn toàn có thể, hoàn toàn đủ để",
           "Phía sau là cụm động từ · phủ định: 不足以",
           "他们不分昼夜地奔波，渴望拍出足以使人疯狂的照片，吸引大家心甘情愿地去购买……",
           "对这样的坏人不严惩就不足以平民愤。",
           "跟儿童谈话很讲究技巧，必须随机应变，要能够随时提出足以了解儿童心理状态而又不会引起儿童反感的问题。"],
    say=["Điểm ngữ pháp thứ ba là động từ 足以.",
         F(0, "足以 là động từ, biểu thị hoàn toàn có thể, hoàn toàn đủ để làm được việc gì. 足 là đủ, 以 là để. Mang màu sắc văn viết."),
         F(1, "Phía sau 足以 là một cụm động từ. Dạng phủ định là 不足以, không đủ để."),
         F(2, "Ví dụ một, lấy từ bài khóa: 他们不分昼夜地奔波，渴望拍出足以使人疯狂的照片，吸引大家心甘情愿地去购买。 Họ bôn ba ngày đêm, khao khát chụp được những bức ảnh đủ để khiến người ta phát cuồng, thu hút mọi người vui lòng mua."),
         F(3, "Ví dụ hai: 对这样的坏人不严惩就不足以平民愤。 Với kẻ xấu như vậy, không trừng trị nghiêm thì không đủ để xoa dịu lòng căm phẫn của dân chúng. 平民愤 là làm dịu cơn phẫn nộ của dân."),
         F(4, "Ví dụ ba: 跟儿童谈话很讲究技巧，必须随机应变，要能够随时提出足以了解儿童心理状态而又不会引起儿童反感的问题。 Nói chuyện với trẻ em rất cần kỹ năng, phải tùy cơ ứng biến, luôn đặt ra được những câu hỏi đủ để hiểu tâm lý trẻ mà lại không khiến trẻ khó chịu.")])

add("bullets", section="Ngữ pháp 注释", title="Luyện tập: dùng 足以 viết lại câu", reveal=True, size=34,
    items=["(1) 听说我们一年浪费掉的粮食够50万人吃一天了。",
           "Đáp án: 听说我们一年浪费掉的粮食足以让50万人吃一天。",
           "(2) 这些材料完全能够说明问题了。",
           "Đáp án: 这些材料足以说明问题了。",
           "(3) 哪怕在知识或信息方面只领先或落后几个星期、几天，甚至几个小时，就完全能够使一个企业利润剧增或面临破产。",
           "Đáp án: ……，就足以使一个企业利润剧增或面临破产。"],
    say=[F(0, "Luyện tập: dùng 足以 viết lại câu. Câu một: 听说我们一年浪费掉的粮食够五十万人吃一天了。 Nghe nói lương thực chúng ta lãng phí trong một năm đủ cho năm mươi vạn người ăn một ngày. Các bạn thử viết lại nhé."),
         F(1, "Đáp án: 听说我们一年浪费掉的粮食足以让五十万人吃一天。 Thay 够 bằng 足以让."),
         F(2, "Câu hai: 这些材料完全能够说明问题了。 Những tài liệu này hoàn toàn có thể nói rõ vấn đề rồi."),
         F(3, "Đáp án: 这些材料足以说明问题了。 Cụm 完全能够 chính là nghĩa của 足以."),
         F(4, "Câu ba: 哪怕在知识或信息方面只领先或落后几个星期、几天，甚至几个小时，就完全能够使一个企业利润剧增或面临破产。 Dù chỉ đi trước hay tụt hậu vài tuần, vài ngày, thậm chí vài giờ về tri thức hay thông tin, cũng hoàn toàn có thể khiến một doanh nghiệp lợi nhuận tăng vọt hoặc đứng trước nguy cơ phá sản."),
         F(5, "Đáp án: 就足以使一个企业利润剧增或面临破产。 Thay 完全能够 bằng 足以.")])

# ======================= PHÂN BIỆT TỪ =======================
add("compare", chapter="Phân biệt 以便 – 便于", section="Phân biệt từ 词语辨析", title="Phân biệt 以便 và 便于",
    common="Giống nhau: đều có ý làm cho mục đích phía sau dễ thực hiện. Ví dụ: 大家现在要努力掌握各种相关知识，以便/便于将来更好地工作。",
    cols=[{"head": "以便",
           "lines": ["(1) Liên từ, chỉ đứng đầu vế câu sau",
                     "Đúng: 你先把材料准备好，以便小组开会研究。",
                     "(2) Không có nghĩa nhờ có điều kiện nào đó mà đạt kết quả",
                     "Sai: 这种电脑体积小，以便大家携带。"]},
          {"head": "便于",
           "lines": ["(1) Động từ, có thể đứng ở vế câu trước",
                     "Đúng: 为了便于管理，我们制定了一些规章制度。",
                     "(2) Vì bản thân có điều kiện nào đó nên dễ đạt kết quả",
                     "Đúng: 这种新型电脑体积小，便于大家携带。"]}],
    say=["Tiếp theo là phần phân biệt từ: 以便 và 便于. Hai từ này đều có chữ 便, nghĩa là tiện, dễ dàng, nên người học rất hay dùng lẫn lộn.",
         "Điểm giống nhau: cả hai đều có ý làm cho mục đích nói ở phía sau dễ thực hiện. Ví dụ: 大家现在要努力掌握各种相关知识，以便将来更好地工作, hoặc 便于将来更好地工作, đều đúng. Bây giờ mọi người phải cố gắng nắm vững các kiến thức liên quan, để sau này làm việc tốt hơn.",
         F(0, "Điểm khác thứ nhất. 以便 là liên từ, chỉ có thể đứng ở đầu vế câu sau. Ví dụ: 你先把材料准备好，以便小组开会研究。 Bạn chuẩn bị tài liệu trước, để nhóm họp nghiên cứu."),
         F(1, "Còn 便于 là động từ, nghĩa là tiện cho, dễ cho; nó có thể đứng ở vế câu trước. Ví dụ: 为了便于管理，我们制定了一些规章制度。 Để tiện quản lý, chúng tôi đã đặt ra một số quy chế. Ở đây không thể nói 为了以便, vì 以便 là liên từ, không đứng sau 为了 được."),
         F(1, "Điểm khác thứ hai. 便于 còn biểu thị: vì bản thân sự vật có một điều kiện nào đó, nên dễ đạt được kết quả hay hiệu quả phía sau. Ví dụ: 这种新型电脑体积小，便于大家携带。 Loại máy tính kiểu mới này nhỏ gọn, tiện cho mọi người mang theo."),
         F(0, "以便 không có nghĩa này. Vì vậy câu 这种电脑体积小，以便大家携带 là sai. Vế sau của 以便 phải là mục đích mà người nói chủ động hướng tới, chứ không phải là kết quả của một đặc điểm có sẵn."),
         "Mẹo nhớ: 以便 là để, đứng đầu vế sau, nối với một hành động có chủ đích ở vế trước; còn 便于 là tiện cho, là động từ, dùng được ở nhiều vị trí, và hay đi sau một đặc điểm như nhỏ, nhẹ, rộng, đơn giản."])

add("bullets", section="Phân biệt từ 词语辨析", title="Làm thử: Đúng hay sai?", reveal=True, size=36,
    items=["(1) 为了以便联系，老师把所有学生的电话制成了一张表。",
           "Đáp án: Sai – 以便 là liên từ, không đứng sau 为了. Sửa: 为了便于联系……",
           "(2) 你把需要用到的各种食材都准备好，这样便于制作。",
           "Đáp án: Đúng – 便于 là động từ, nghĩa là tiện cho.",
           "(3) 请参加此次活动的人员报一下名，以便我们统计人数。",
           "Đáp án: Đúng – 以便 đứng đầu vế sau, chỉ mục đích.",
           "(4) 场地很大，以便大家开展活动。",
           "Đáp án: Sai – điều kiện có sẵn dẫn đến kết quả. Sửa: 场地很大，便于大家开展活动。"],
    say=[F(0, "Bây giờ chúng ta làm thử: phán đoán đúng sai. Câu một: 为了以便联系，老师把所有学生的电话制成了一张表。 Để tiện liên lạc, thầy giáo làm số điện thoại của tất cả học sinh thành một bảng. Đúng hay sai? Các bạn suy nghĩ nhé."),
         F(1, "Đáp án: sai. 以便 là liên từ, không thể đứng sau 为了. Phải sửa thành 为了便于联系。"),
         F(2, "Câu hai: 你把需要用到的各种食材都准备好，这样便于制作。 Bạn chuẩn bị sẵn các loại nguyên liệu cần dùng, như vậy sẽ tiện cho việc chế biến."),
         F(3, "Đáp án: đúng. 便于 là động từ, 便于制作 là tiện cho việc chế biến."),
         F(4, "Câu ba: 请参加此次活动的人员报一下名，以便我们统计人数。 Mời những người tham gia hoạt động lần này đăng ký tên, để chúng tôi thống kê số người."),
         F(5, "Đáp án: đúng. 以便 đứng đầu vế câu sau, chỉ mục đích của hành động đăng ký."),
         F(6, "Câu bốn: 场地很大，以便大家开展活动。 Sân bãi rất rộng, để mọi người triển khai hoạt động."),
         F(7, "Đáp án: sai. Sân rộng là điều kiện có sẵn, dẫn đến kết quả là tiện cho hoạt động, nên phải dùng 便于: 场地很大，便于大家开展活动。")])

# ======================= MỞ RỘNG: THÀNH PHẦN CHEN =======================
add("bullets", chapter="Mở rộng: thành phần chen 插入语", section="Mở rộng 扩展", title="Thành phần chen (插入语) là gì?", size=36,
    items=["Từ hoặc cụm từ chen vào câu, không làm chủ ngữ, vị ngữ, tân ngữ…",
           "Bỏ đi, câu vẫn đúng ngữ pháp; nhưng mất sắc thái giải thích, nguồn tin, thái độ…",
           "Thường đứng đầu câu hoặc giữa câu, tách ra bằng dấu phẩy",
           "据说，它们是藏狐、赤斑羚、藏羚羊和喜马拉雅旱獭。",
           "→ 它们是藏狐、赤斑羚、藏羚羊和喜马拉雅旱獭。 (vẫn đúng, nhưng thành khẳng định chắc chắn)"],
    say=["Bây giờ chúng ta sang phần mở rộng. Quyển này không có mục tu từ riêng. Bài tập bốn của sách yêu cầu chúng ta nối câu với lời giải thích, và thể hội cách dùng thành phần chen, tiếng Trung gọi là 插入语. Vì vậy hôm nay thầy dành riêng một phần để học kỹ kỹ năng này.",
         F(0, "插入语 là từ hoặc cụm từ được chen vào trong câu. Nó không làm chủ ngữ, vị ngữ, tân ngữ hay bất kỳ thành phần nào của câu, cũng không có quan hệ cấu trúc với các thành phần khác."),
         F(1, "Vì vậy, nếu bỏ thành phần chen đi, câu vẫn đúng ngữ pháp. Nhưng câu sẽ mất đi sắc thái mà nó mang lại, như giải thích, cho biết nguồn tin, hay thể hiện thái độ của người nói."),
         F(2, "Thành phần chen thường đứng ở đầu câu hoặc giữa câu, và được tách ra bằng dấu phẩy."),
         F(3, "Ví dụ trong bài khóa: 据说，它们是藏狐、赤斑羚、藏羚羊和喜马拉雅旱獭。 Nghe nói, chúng là cáo Tây Tạng, sơn dương đỏ, linh dương Tây Tạng và macmot Himalaya."),
         F(4, "Nếu bỏ 据说 đi, câu vẫn đúng. Nhưng khi đó tác giả khẳng định chắc chắn, trong khi thật ra tác giả không nhận ra bốn loài này, chỉ là nghe người khác nói lại. Các bạn thấy không, thành phần chen tuy nhỏ, nhưng giúp lời nói chính xác hơn rất nhiều.")])

add("bullets", section="Mở rộng 扩展", title="Các loại thành phần chen thường gặp (1)", size=34,
    items=["## (1) Giải thích, nói lại: 换句话说 · 也就是说 · 就是说",
           "他一个月的工资是我的三倍，也就是说，他一个月的工资相当于我三个月的。",
           "## (2) Nguồn tin: 据说 · 听说 · 据报道 · 据统计",
           "据报道，梅里雪山出现了近三十年来最大规模的鹦鹉越冬群。",
           "## (3) Phỏng đoán, nhận định: 看来 · 看样子 · 说不定",
           "看来，这种集合式工作的成效十分显著。"],
    say=[F(0, "Loại thứ nhất: thành phần chen dùng để giải thích, nói lại cho rõ, như 换句话说，也就是说，就是说. Đây chính là điểm ngữ pháp thứ nhất chúng ta vừa học."),
         F(1, "Ví dụ: 他一个月的工资是我的三倍，也就是说，他一个月的工资相当于我三个月的。 Lương một tháng của anh ấy gấp ba lần tôi, tức là, lương một tháng của anh ấy bằng ba tháng lương của tôi."),
         F(2, "Loại thứ hai: thành phần chen cho biết nguồn tin, như 据说，听说，据报道，据统计, tức là nghe nói, nghe đâu, theo tin đưa, theo thống kê."),
         F(3, "Ví dụ: 据报道，梅里雪山出现了近三十年来最大规模的鹦鹉越冬群。 Theo tin đưa, ở núi tuyết Mai Lý đã xuất hiện đàn vẹt trú đông lớn nhất trong gần ba mươi năm qua."),
         F(4, "Loại thứ ba: thành phần chen thể hiện sự phỏng đoán, nhận định, như 看来，看样子，说不定, tức là xem ra, trông có vẻ, không chừng."),
         F(5, "Ví dụ: 看来，这种集合式工作的成效十分显著。 Xem ra, cách làm việc tập hợp này có hiệu quả rất rõ rệt.")])

add("bullets", section="Mở rộng 扩展", title="Các loại thành phần chen thường gặp (2)", size=34,
    items=["## (4) Thái độ của người nói: 说实在的 · 说真的 · 毫无疑问 · 不瞒你说",
           "说实在的，靠卖照片来支撑巨大的开支，几近童话。",
           "## (5) Tổng kết: 总之 · 总而言之 · 一句话",
           "总而言之，保护野生动物是我们每个人的责任。",
           "## (6) Gây chú ý: 你看 · 要知道 · 你想想",
           "要知道，很多物种还没来得及为我们所了解，就消失了。"],
    say=[F(0, "Loại thứ tư: thành phần chen thể hiện thái độ của người nói, như 说实在的，说真的，毫无疑问，不瞒你说, tức là nói thật lòng, nói thật, không còn nghi ngờ gì, nói thật với bạn."),
         F(1, "Ví dụ: 说实在的，靠卖照片来支撑巨大的开支，几近童话。 Nói thật lòng, dựa vào bán ảnh để gánh khoản chi phí khổng lồ thì gần như chuyện cổ tích."),
         F(2, "Loại thứ năm: thành phần chen dùng để tổng kết, như 总之，总而言之，一句话, tức là tóm lại, nói tóm lại, nói một câu thôi."),
         F(3, "Ví dụ: 总而言之，保护野生动物是我们每个人的责任。 Tóm lại, bảo vệ động vật hoang dã là trách nhiệm của mỗi chúng ta."),
         F(4, "Loại thứ sáu: thành phần chen dùng để gây sự chú ý của người nghe, như 你看，要知道，你想想, tức là bạn xem, phải biết rằng, bạn thử nghĩ xem."),
         F(5, "Ví dụ: 要知道，很多物种还没来得及为我们所了解，就消失了。 Phải biết rằng, rất nhiều loài còn chưa kịp được chúng ta biết đến thì đã biến mất rồi. Khi nói và viết, dùng đúng thành phần chen sẽ làm cho lời văn mạch lạc và tự nhiên hơn nhiều.")])

add("bullets", section="Mở rộng 扩展", title="Bài tập 4: Nối câu với lời giải thích", reveal=True, size=36,
    items=["(1) 他一个月的工资是我的三倍，也就是说，……",
           "Đáp án: B. 他一个月的工资相当于我三个月的。",
           "(2) 他所有的辛劳都是心甘情愿的，换句话说，……",
           "Đáp án: C. 没有人强迫他。",
           "(3) 他非名牌不穿，就是说，……",
           "Đáp án: D. 他只穿名牌，不是名牌不穿。",
           "(4) 现在很多年轻人都是“月光族”，也就是说，……",
           "Đáp án: A. 到了月底，钱就都花光了。"],
    say=[F(0, "Bài tập bốn của sách: nối các câu sau với lời giải thích của chúng, và thể hội cách dùng thành phần chen. Bốn lời giải thích là: A, 到了月底，钱就都花光了; B, 他一个月的工资相当于我三个月的; C, 没有人强迫他; D, 他只穿名牌，不是名牌不穿. Câu một: 他一个月的工资是我的三倍，也就是说。 Các bạn tạm dừng và chọn nhé."),
         F(1, "Đáp án: B. 他一个月的工资相当于我三个月的。 Lương một tháng của anh ấy bằng ba tháng lương của tôi."),
         F(2, "Câu hai: 他所有的辛劳都是心甘情愿的，换句话说。 Mọi vất vả của anh ấy đều là tự nguyện, nói cách khác thì sao?"),
         F(3, "Đáp án: C. 没有人强迫他。 Không ai ép buộc anh ấy cả. Tự nguyện tức là không bị ai ép."),
         F(4, "Câu ba: 他非名牌不穿，就是说。 Mẫu 非……不…… nghĩa là không phải… thì không…."),
         F(5, "Đáp án: D. 他只穿名牌，不是名牌不穿。 Anh ấy chỉ mặc hàng hiệu, không phải hàng hiệu thì không mặc."),
         F(6, "Câu bốn: 现在很多年轻人都是月光族，也就是说。 月光族 là gì?"),
         F(7, "Đáp án: A. 到了月底，钱就都花光了。 Đến cuối tháng là tiêu sạch tiền. 月光族 là cách nói vui: 月 là tháng, 光 là sạch, hết; tức là những người tháng nào cũng tiêu hết sạch lương.")])

add("bullets", section="Mở rộng 扩展", title="Luyện tập: chọn thành phần chen thích hợp", reveal=True, size=36,
    items=["## 据说 · 看来 · 换句话说 · 说实在的 · 总而言之",
           "(1) ______，梅里雪山上又发现了一大群鹦鹉。",
           "Đáp án: 据说 – cho biết nguồn tin",
           "(2) 天这么黑，风这么大，______，今天要下大雨了。",
           "Đáp án: 看来 – phỏng đoán",
           "(3) 他每天工作十二个小时，周末也不休息，______，他几乎没有自己的时间。",
           "Đáp án: 换句话说 – nói lại, giải thích",
           "(4) ______，这部电影我一点儿也没看懂。",
           "Đáp án: 说实在的 – thái độ thật lòng"],
    say=[F(0, "Luyện tập thêm: chọn thành phần chen thích hợp điền vào chỗ trống. Có năm lựa chọn: 据说，看来，换句话说，说实在的，总而言之."),
         F(1, "Câu một: 什么，梅里雪山上又发现了一大群鹦鹉。 Ở núi tuyết Mai Lý lại phát hiện một đàn vẹt lớn. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 据说. 据说，梅里雪山上又发现了一大群鹦鹉。 Người nói không tận mắt thấy, nên dùng 据说 cho biết nguồn tin."),
         F(3, "Câu hai: 天这么黑，风这么大，什么，今天要下大雨了。 Trời tối thế này, gió to thế này, hôm nay sắp mưa to rồi."),
         F(4, "Đáp án: 看来. Dựa vào trời tối, gió to để phỏng đoán."),
         F(5, "Câu ba: 他每天工作十二个小时，周末也不休息，什么，他几乎没有自己的时间。 Mỗi ngày anh ấy làm mười hai tiếng, cuối tuần cũng không nghỉ."),
         F(6, "Đáp án: 换句话说. Vế sau nói lại ý của vế trước: anh ấy gần như không có thời gian riêng."),
         F(7, "Câu bốn: 什么，这部电影我一点儿也没看懂。 Bộ phim này tôi chẳng hiểu gì cả."),
         F(8, "Đáp án: 说实在的. Người nói thú nhận thật lòng. Còn 总而言之 thì dùng để tổng kết một đoạn dài, ở đây không có chỗ phù hợp.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 练习", title="Bài tập 1: Mở rộng từ theo chữ có dấu chấm", size=40,
    items=["来历 (历) → 经历 · 历史 · 简历 · 学历",
           "濒临 (临) → 面临 · 来临 · 光临 · 临时",
           "领袖 (袖) → 袖子 · 袖口 · 长袖 · 短袖",
           "识别 (识) → 知识 · 认识 · 常识 · 见识",
           "报酬 (酬) → 薪酬 · 酬金 · 酬谢 · 酬劳"],
    say=["Phần luyện tập. Bài tập một: mô phỏng ví dụ, viết thêm các từ có chứa chữ được đánh dấu chấm.",
         F(0, "Ví dụ mẫu: 来历, chữ được đánh dấu là chữ thứ hai, Hán Việt là lịch. Ta có 经历，历史，简历，学历. Tức là trải nghiệm, lịch sử, sơ yếu lý lịch, và học lực, bằng cấp."),
         F(1, "濒临, chữ được đánh dấu là chữ thứ hai, Hán Việt là lâm, nghĩa là đến gần, sắp tới. Ta có 面临，来临，光临，临时. Tức là đối mặt, đến, quang lâm, và tạm thời."),
         F(2, "领袖, chữ được đánh dấu là chữ thứ hai, nghĩa là tay áo. Ta có 袖子，袖口，长袖，短袖. Tức là tay áo, cổ tay áo, áo dài tay, và áo ngắn tay."),
         F(3, "识别, chữ được đánh dấu là chữ đầu, Hán Việt là thức, nghĩa là biết. Ta có 知识，认识，常识，见识. Tức là tri thức, quen biết, thường thức, và hiểu biết."),
         F(4, "报酬, chữ được đánh dấu là chữ thứ hai, Hán Việt là thù, nghĩa là trả công, đền đáp. Ta có 薪酬，酬金，酬谢，酬劳. Tức là lương bổng, tiền thù lao, đền đáp cảm ơn, và tiền công.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Dùng từ cho sẵn hoàn thành câu (1)", reveal=True, size=36,
    items=["(1) 请在信封上写清地址，______。（以便）",
           "Đáp án: ……，以便邮递员准确地投递。",
           "(2) 他对中国非常了解，是个______。（名副其实）",
           "Đáp án: ……，是个名副其实的中国通。",
           "(3) 很多年轻人都______。（渴望）",
           "Đáp án: 很多年轻人都渴望找到一份自己喜欢的工作。"],
    say=[F(0, "Bài tập hai: dùng từ cho sẵn để hoàn thành câu. Câu một, dùng 以便: 请在信封上写清地址，什么。 Xin hãy ghi rõ địa chỉ trên phong bì, để làm gì? Các bạn tạm dừng và thử hoàn thành nhé."),
         F(1, "Đáp án gợi ý: 请在信封上写清地址，以便邮递员准确地投递。 Xin ghi rõ địa chỉ trên phong bì, để người đưa thư giao đúng nơi. 以便 đứng đầu vế sau, chỉ mục đích."),
         F(2, "Câu hai, dùng 名副其实: 他对中国非常了解，是个什么。 Anh ấy rất hiểu Trung Quốc, là một người thế nào?"),
         F(3, "Đáp án gợi ý: 是个名副其实的中国通。 Là một người thông thạo Trung Quốc đúng nghĩa. 中国通 là người am hiểu Trung Quốc."),
         F(4, "Câu ba, dùng 渴望: 很多年轻人都什么。 Rất nhiều người trẻ đều thế nào?"),
         F(5, "Đáp án gợi ý: 很多年轻人都渴望找到一份自己喜欢的工作。 Rất nhiều người trẻ đều khao khát tìm được một công việc mình yêu thích.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 2: Dùng từ cho sẵn hoàn thành câu (2)", reveal=True, size=36,
    items=["(4) 这些事实______。（足以）",
           "Đáp án: 这些事实足以说明他是无辜的。",
           "(5) 他从小就爱好写作，几十年来他一直______。（致力于）",
           "Đáp án: ……，几十年来他一直致力于文学创作。",
           "(6) 孩子长大后都忙于自己的工作，父母______。（指望）",
           "Đáp án: ……，父母不能指望他们天天陪在身边。"],
    say=[F(0, "Câu bốn, dùng 足以: 这些事实什么。 Những sự thật này thế nào?"),
         F(1, "Đáp án gợi ý: 这些事实足以说明他是无辜的。 Những sự thật này đủ để chứng minh anh ấy vô tội. 无辜 là vô tội."),
         F(2, "Câu năm, dùng 致力于: 他从小就爱好写作，几十年来他一直什么。 Anh ấy từ nhỏ đã yêu thích viết lách, mấy chục năm nay anh ấy luôn thế nào?"),
         F(3, "Đáp án gợi ý: 几十年来他一直致力于文学创作。 Mấy chục năm nay anh ấy luôn dốc sức cho sáng tác văn học."),
         F(4, "Câu sáu, dùng 指望: 孩子长大后都忙于自己的工作，父母什么。 Con cái lớn lên đều bận rộn với công việc của mình, cha mẹ thì sao?"),
         F(5, "Đáp án gợi ý: 父母不能指望他们天天陪在身边。 Cha mẹ không thể trông chờ con cái ngày ngày ở bên cạnh.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (1)", reveal=True, size=34,
    items=["## Từ cho sẵn: 渴望 · 高超 · 昼夜 · 完毕 · 浓厚",
           "一天的工作处理___，她终于可以休息一下了。在不分___的忙碌之外，她非常___拥有一段属于自己的时间。安静地读点儿书，去旅行，或者做自己喜欢做的事情。她对摄影有___的兴趣，而且拍摄技术___，如果有时间，她很想约上几个朋友，一起去野外拍些照片。",
           "Đáp án: 完毕 · 昼夜 · 渴望 · 浓厚 · 高超"],
    say=[F(0, "Bài tập ba: chọn từ thích hợp điền vào chỗ trống. Đoạn một có năm từ: 渴望，高超，昼夜，完毕，浓厚."),
         F(1, "一天的工作处理什么，她终于可以休息一下了。在不分什么的忙碌之外，她非常什么拥有一段属于自己的时间。安静地读点儿书，去旅行，或者做自己喜欢做的事情。她对摄影有什么的兴趣，而且拍摄技术什么，如果有时间，她很想约上几个朋友，一起去野外拍些照片。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 处理完毕，不分昼夜，非常渴望，浓厚的兴趣，拍摄技术高超。 Công việc trong ngày đã xử lý xong, cuối cùng cô ấy cũng được nghỉ ngơi một chút. Ngoài những bận rộn không kể ngày đêm, cô ấy rất khao khát có một khoảng thời gian của riêng mình. Cô ấy rất hứng thú với nhiếp ảnh, kỹ thuật chụp lại điêu luyện; nếu có thời gian, cô ấy rất muốn hẹn vài người bạn cùng ra ngoài trời chụp ảnh.")])

add("bullets", section="Luyện tập 练习", title="Bài tập 3: Chọn từ thích hợp điền vào chỗ trống (2)", reveal=True, size=34,
    items=["## Từ cho sẵn: 童话 · 畅销 · 足以 · 报酬 · 心甘情愿",
           "我的朋友是个作家，他写的书很___，自然他得到的___也不少。年轻女孩子喜欢他写的___式的爱情故事，虽然不真实，但___带给人幻想和安慰。所以，每当他的新书出版，他的书迷们都会___起大早排队去购买。",
           "Đáp án: 畅销 · 报酬 · 童话 · 足以 · 心甘情愿"],
    say=[F(0, "Đoạn hai có năm từ: 童话，畅销，足以，报酬，心甘情愿."),
         F(1, "我的朋友是个作家，他写的书很什么，自然他得到的什么也不少。年轻女孩子喜欢他写的什么式的爱情故事，虽然不真实，但什么带给人幻想和安慰。所以，每当他的新书出版，他的书迷们都会什么起大早排队去购买。 Các bạn điền thử nhé."),
         F(2, "Đáp án: 书很畅销，得到的报酬，童话式的爱情故事，足以带给人幻想和安慰，心甘情愿起大早排队去购买。 Bạn tôi là nhà văn, sách anh ấy viết bán rất chạy, tất nhiên thù lao nhận được cũng không ít. Các cô gái trẻ thích những câu chuyện tình yêu kiểu cổ tích của anh ấy; tuy không thật, nhưng đủ để mang lại cho người ta mộng tưởng và sự an ủi. Vì vậy, mỗi khi sách mới của anh ấy ra mắt, những người hâm mộ đều vui lòng dậy sớm xếp hàng đi mua."),
         "Các bạn để ý: trong bài khóa, ảnh của Từ Kiện 不是畅销书, không phải sách bán chạy, nên 报酬很低. Còn nhà văn trong đoạn này thì ngược lại. Cùng một nhóm từ, nhưng hai câu chuyện trái ngược nhau."])

add("bullets", section="Luyện tập 练习", title="Mở rộng 扩展: các cặp từ gần nghĩa", size=36,
    items=["布告 – 公告 thông cáo, bố cáo · 诞辰 – 生日 ngày sinh · 发布 – 公布 công bố",
           "范畴 – 范围 phạm trù, phạm vi · 挥霍 – 浪费 phung phí, lãng phí",
           "坚固 – 牢固 vững chắc · 奖赏 – 奖励 khen thưởng · 恐吓 – 威胁 đe dọa",
           "谅解 – 原谅 thông cảm, tha thứ · 勉励 – 鼓励 khích lệ, động viên",
           "藐视 – 蔑视 coi thường, khinh miệt · 洽谈 – 协商 đàm phán, bàn bạc",
           "谦逊 – 谦虚 khiêm tốn · 区分 – 区别 phân biệt"],
    say=["Phần mở rộng của sách giới thiệu mười bốn cặp từ gần nghĩa. Thầy đọc qua để các bạn làm quen; khi gặp trong bài đọc, các bạn sẽ nhận ra ngay.",
         F(0, "布告，公告: thông cáo, bố cáo dán nơi công cộng. 诞辰，生日: ngày sinh; 诞辰 trang trọng hơn, thường dùng cho người nổi tiếng, vĩ nhân. 发布，公布: công bố."),
         F(1, "范畴，范围: phạm trù, phạm vi. 挥霍，浪费: phung phí, lãng phí; 挥霍 thường dùng cho tiền bạc, của cải."),
         F(2, "坚固，牢固: vững chắc. 奖赏，奖励: khen thưởng. 恐吓，威胁: đe dọa, uy hiếp."),
         F(3, "谅解，原谅: thông cảm, tha thứ. 勉励，鼓励: khích lệ, động viên."),
         F(4, "藐视，蔑视: coi thường, khinh miệt. 洽谈，协商: đàm phán, bàn bạc; 洽谈 hay dùng trong kinh doanh."),
         F(5, "谦逊，谦虚: khiêm tốn. 区分，区别: phân biệt. Các cặp từ này nghĩa gần nhau nhưng mức độ và cách kết hợp có khác biệt, các bạn hãy tra từ điển và đặt câu với từng từ nhé.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết & bài tập về nhà", section="Tổng kết", title="Tổng kết bài 16", size=34,
    items=["Từ vựng trọng tâm: 野生 · 濒临 · 致力 · 辨认 · 识别 · 严峻 · 空白 · 琢磨 · 渴望 · 足以 · 以便 · 名副其实 · 显著 · 浓厚",
           "Ngữ pháp: 换句话说 (nói cách khác) · 为……所…… (bị, được – văn viết) · 足以 (đủ để)",
           "Phân biệt: 以便 (liên từ, đầu vế sau) ≠ 便于 (động từ; điều kiện có sẵn → tiện cho)",
           "Mở rộng: thành phần chen – giải thích, nguồn tin, phỏng đoán, thái độ, tổng kết, gây chú ý",
           "## Bài tập về nhà (运用)",
           "Tham khảo bài tập 5, viết tóm tắt bài khóa thành một bài khoảng 400 chữ"],
    say=["Chúng ta cùng tổng kết bài mười sáu.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 野生，濒临，致力，辨认，识别，严峻，空白，琢磨，渴望，足以，以便，名副其实，显著，浓厚. Và đừng quên những từ dễ nhầm như 报酬，高超，素质，权威."),
         F(1, "Về ngữ pháp: 换句话说 là thành phần chen, dùng để giải thích, nói lại cho rõ. Cấu trúc 为所 là câu bị động văn viết, nhớ đọc là wéi, dạng phủ định thêm 不 vào trước. 足以 là đủ để, phía sau là cụm động từ, phủ định là 不足以."),
         F(2, "Về phân biệt từ: 以便 là liên từ, chỉ đứng đầu vế câu sau; còn 便于 là động từ, đứng được ở vế trước, và còn chỉ nhờ có điều kiện sẵn có mà tiện cho việc gì."),
         F(3, "Về phần mở rộng: thành phần chen không làm thành phần câu, bỏ đi câu vẫn đúng, nhưng giúp giải thích, cho biết nguồn tin, phỏng đoán, thể hiện thái độ, tổng kết, hoặc gây chú ý."),
         F(5, "Bài tập về nhà, theo phần vận dụng của sách: để bảo vệ và tuyên truyền về động vật hoang dã, Từ Kiện đã thành lập IBE, chuyên chụp ảnh động vật hoang dã; tác phẩm của họ không những có kỹ thuật điêu luyện, mà còn mang đậm tính khảo sát khoa học. Hãy tham khảo bài tập năm, tóm tắt bài khóa thành một bài viết ngắn khoảng bốn trăm chữ. Nhớ thử dùng 换句话说，为所，足以 và 以便 trong bài viết nhé."),
         "Với bài này, chúng ta cũng khép lại Chủ đề bốn, 走遍天下, Đi khắp thiên hạ. Cảm ơn các bạn đã theo dõi bài giảng. Mong rằng mỗi khi nhìn thấy một bức ảnh đẹp về thiên nhiên, các bạn sẽ nhớ đến những người đã ăn gió nằm sương để có được nó. Hẹn gặp lại các bạn ở bài mười bảy: 小动物眼中的慢世界, Thế giới chậm trong mắt động vật nhỏ. Chúc các bạn học tốt!"])

lesson = {
    "title": "HSK 6 (Thượng) – Bài 16: 徐健和他的野生动物摄影师们 (Từ Kiện và các nhà nhiếp ảnh động vật hoang dã)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    # Thứ tự có ý nghĩa: khóa dài phải đứng trước khóa ngắn nằm bên trong nó.
    "tts_replace": {"藏狐": "葬狐",                    # zànghú
                    "藏羚羊": "葬羚羊",                # zànglíngyáng
                    "兴亡": "星亡",                    # xīngwáng
                    "吐露": "土露",                    # tǔlù
                    "露头": "漏头",                    # lòutóu
                    "露面": "漏面",                    # lòumiàn
                    "空白": "控白",                    # kòngbái
                    "琢磨": "昨磨",                    # zuómo
                    "几近": "机近",                    # jījìn
                    "还原": "环原",                    # huányuán
                    "可供": "可工",                    # kěgōng
                    "地数": "地属",                    # yí ge yí ge de shǔ
                    "更为": "更维",                    # gèngwéi
                    "尽一份": "进一份",                # jìn yí fèn
                    "尽其该尽": "进其该进",            # jìn qí gāi jìn
                    "相处": "相楚",                    # xiāngchǔ
                    "处理": "楚理",                    # chǔlǐ
                    "为所欲为": "维所欲维",            # wéisuǒyùwéi
                    "为我们所": "维我们所",            # wéi…suǒ
                    "为少数人所": "维少数人所",        # wéi…suǒ
                    "为更多的人所": "维更多的人所",    # wéi…suǒ
                    "为金钱所": "维金钱所",            # wéi…suǒ
                    "为电影中的人物所": "维电影中的人物所",  # wéi…suǒ
                    "为很多人所": "维很多人所",        # wéi…suǒ
                    "为大雪所": "维大雪所",            # wéi…suǒ
                    "为人们所": "维人们所",            # wéi…suǒ
                    "变废为宝": "变废维宝",            # biàn fèi wéi bǎo
                    "为所": "维所",                    # tên cấu trúc wéi…suǒ trong lời giảng
                    "为野生动物": "位野生动物",        # wèi (vì, cho)
                    "为保护区": "位保护区",            # wèi (cho)
                    "水浒传": "水浒撰",                # Shuǐhǔ Zhuàn
                    "强迫": "抢迫",                    # qiǎngpò
                    "恐吓": "恐赫"},                   # kǒnghè
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bai16.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
