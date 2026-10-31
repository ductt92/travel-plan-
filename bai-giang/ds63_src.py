#!/usr/bin/env python3
"""Kịch bản bài giảng 顶石中文 – Bài 6.3 «30 岁的职场姐姐如何乘风破浪？». Chạy để sinh ds63.json."""
import json
import os

TAG = "顶石中文 · Bài 6.3 · 30 岁的职场姐姐如何乘风破浪？"
slides = []


def add(type_, chapter=None, section="", **kw):
    s = {"type": type_, "section": section, **kw}
    if chapter:
        s["chapter"] = chapter
    slides.append(s)


def F(i, t, **kw):
    return {"t": t, "f": i, **kw}


# ======================= MỞ ĐẦU =======================
# Tên bài dài, tách làm hai dòng (giống Bài 40): zh + py; dòng đầu của "sub" là pinyin đầy đủ
add("title", chapter="Mở đầu",
    top="顶石中文 – Đỉnh cao tiếng Trung",
    zh="30 岁的职场姐姐", py="如何乘风破浪？",
    vi="Bài 6.3: Các chị 30 tuổi nơi công sở vượt sóng thế nào?",
    sub="Sānshí suì de zhíchǎng jiějie rúhé chéngfēng-pòlàng?\nBài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng giáo trình 顶石中文, Đỉnh cao tiếng Trung.",
         {"t": "Hôm nay chúng ta học bài cuối cùng của Đơn vị sáu, chủ đề Nơi làm việc: bài sáu chấm ba, 三十岁的职场姐姐如何乘风破浪？ Nghĩa là: Các chị ba mươi tuổi nơi công sở đạp gió rẽ sóng thế nào?",
          "cap": "Hôm nay chúng ta học bài cuối cùng của Đơn vị 6, chủ đề Nơi làm việc: bài 6.3, 30 岁的职场姐姐如何乘风破浪？ Nghĩa là: Các chị 30 tuổi nơi công sở đạp gió rẽ sóng thế nào?"},
         "Tên bài lấy cảm hứng từ chương trình truyền hình nổi tiếng 乘风破浪的姐姐, ở Việt Nam quen gọi là Chị đẹp đạp gió rẽ sóng. Bài khóa là một bài báo của trang 网易数读, phân tích những khó khăn của phụ nữ ngoài ba mươi tuổi nơi công sở: bị hỏi chuyện kết hôn sinh con khi phỏng vấn, bị phân biệt giới tính, bị điều chuyển, giảm lương, và phải gánh gần hết việc nhà.",
         "Cuối bài, chúng ta sẽ có thêm một chương ôn tập cả Đơn vị sáu, với các hoạt động của sách như phản bác bằng phương pháp phản chứng, và các đề tranh luận về công việc. Chúng ta bắt đầu nhé."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài báo về phụ nữ đi làm ngoài 30 tuổi: khó khăn và nguyên nhân",
           "Nắm vững 45 từ mới, kèm âm Hán Việt và ví dụ",
           "8 mẫu câu: 令人……的是 · 即便是……也…… · 当着 · 凡 · 唯独 · 谈不上 · 哪怕……也…… · 别的不说",
           "Kết hợp từ (庞大 · 同等 · 轮流 · 缴纳 · 塑造) và 21 thành ngữ",
           "Luyện tập, thảo luận; ôn tập Đơn vị 6: phản bác bằng 反证法, tranh luận"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu bài báo về phụ nữ đi làm ngoài ba mươi tuổi ở Trung Quốc: họ gặp những khó khăn gì, và vì sao lại như vậy."),
         F(1, "Thứ hai, nắm vững bốn mươi lăm từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học tám mẫu câu trọng điểm: 令人的是，即便是也，当着，凡，唯独，谈不上，哪怕也, và 别的不说."),
         F(3, "Thứ tư, học năm kết hợp từ và hai mươi mốt thành ngữ. Bài này có rất nhiều thành ngữ, như 风口浪尖，雪上加霜，焦头烂额，鸡毛蒜皮，披荆斩棘."),
         F(4, "Thứ năm, làm bài luyện tập, thảo luận liên hệ Việt Nam, rồi ôn tập cả Đơn vị sáu: học cách phản bác một quan điểm bằng phương pháp phản chứng, và làm quen với các đề tranh luận về công việc."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 课前思考", title="Câu hỏi trước bài học 课前思考", reveal=True, size=36,
    items=["(1) 你同意“男主外女主内”这种说法吗？",
           "Đáp án gợi ý: 我不太同意。现在男女平等，家务和育儿应该由夫妻共同承担。",
           "(2) 你愿意选择当全职主妇吗？/让太太成为全职主妇吗？",
           "Đáp án gợi ý: 我不太愿意，因为我希望有自己的事业和收入。不过，这应该是个人的自由选择。",
           "(3) 如果你工作繁忙，愿意把孩子交给父母照顾吗？",
           "Đáp án gợi ý: 愿意。在越南，很多年轻父母工作忙，常常请爷爷奶奶或外公外婆帮忙带孩子。"],
    say=["Chúng ta bắt đầu bằng ba câu hỏi trước bài học, 课前思考. Thầy đọc câu hỏi, các bạn tạm dừng để tự trả lời bằng tiếng Trung, rồi nghe câu trả lời gợi ý nhé.",
         F(0, "Câu một: 你同意男主外女主内这种说法吗？ Bạn có đồng ý với quan niệm đàn ông lo việc ngoài, đàn bà lo việc trong không? 主 ở đây là chủ trì, lo liệu."),
         F(1, "Gợi ý: 我不太同意。现在男女平等，家务和育儿应该由夫妻共同承担。 Tôi không đồng ý lắm. Bây giờ nam nữ bình đẳng, việc nhà và nuôi con nên do cả hai vợ chồng cùng gánh vác."),
         F(2, "Câu hai: 你愿意选择当全职主妇吗？或者，让太太成为全职主妇吗？ Bạn có muốn làm nội trợ toàn thời gian không? Hoặc, bạn có muốn để vợ làm nội trợ toàn thời gian không?"),
         F(3, "Gợi ý: 我不太愿意，因为我希望有自己的事业和收入。不过，这应该是个人的自由选择。 Tôi không muốn lắm, vì tôi mong có sự nghiệp và thu nhập của riêng mình. Tuy nhiên, đây nên là lựa chọn tự do của mỗi người."),
         F(4, "Câu ba: 如果你工作繁忙，愿意把孩子交给父母照顾吗？ Nếu công việc bận rộn, bạn có sẵn lòng giao con cho bố mẹ chăm không?"),
         F(5, "Gợi ý: 愿意。在越南，很多年轻父母工作忙，常常请爷爷奶奶或外公外婆帮忙带孩子。 Có. Ở Việt Nam, nhiều bố mẹ trẻ bận việc, thường nhờ ông bà nội hoặc ông bà ngoại trông con giúp. Ở Trung Quốc cũng vậy đấy.")])

add("bullets", section="Khởi động 课前思考", title="Khởi động: từ khóa về phụ nữ và công việc", size=35,
    items=["职场女性 phụ nữ đi làm · 婚育 kết hôn và sinh con · 产假 chǎnjià nghỉ thai sản",
           "全职主妇 / 全职妈妈 nội trợ toàn thời gian · 双职工家庭 gia đình cả vợ cả chồng đi làm",
           "性别歧视 phân biệt giới tính · 男主外女主内 nam lo việc ngoài, nữ lo việc trong",
           "家庭煮夫 “ông chồng nội trợ” (煮 nấu ≈ 主) · 超级奶爸 ông bố bỉm sữa siêu đẳng",
           "《乘风破浪的姐姐》 “Chị đẹp đạp gió rẽ sóng” – show của các nữ nghệ sĩ trên 30 tuổi"],
    say=["Trước khi vào bài, chúng ta làm quen với một số từ khóa về phụ nữ và công việc.",
         F(0, "职场女性, phụ nữ đi làm. 婚育, kết hôn và sinh con, một từ rất hay gặp trong bài. 产假, chữ thứ hai đọc thanh bốn, là nghỉ thai sản."),
         F(1, "全职主妇 hay 全职妈妈 là người nội trợ toàn thời gian, bà mẹ ở nhà chăm con. 双职工家庭 là gia đình mà cả vợ và chồng đều đi làm."),
         F(2, "性别歧视, phân biệt đối xử về giới tính. 男主外女主内, đàn ông lo việc bên ngoài, đàn bà lo việc trong nhà, một quan niệm truyền thống."),
         F(3, "Hai từ vui: 家庭煮夫 là ông chồng nội trợ; chữ 煮 là nấu, đồng âm với chữ 主 trong 家庭主妇, bà nội trợ. Còn 超级奶爸 là ông bố siêu đẳng, chăm con khéo như mẹ, gần giống bố bỉm sữa trong tiếng Việt. Hai từ này sẽ xuất hiện trong phần ôn tập đơn vị."),
         F(4, "Cuối cùng là chương trình 乘风破浪的姐姐, Chị đẹp đạp gió rẽ sóng, nơi các nữ nghệ sĩ trên ba mươi tuổi chứng minh tuổi tác không phải là giới hạn. Tên bài khóa chính là lấy từ đây.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("综艺", "zōngyì", "tổng nghệ", "danh từ", "văn nghệ tổng hợp; (chương trình) giải trí", "这是一档很火的综艺节目。", "Đây là một chương trình giải trí rất hot.",
     "Danh từ, nói gọn của 综合文艺, văn nghệ tổng hợp. 综艺节目 là chương trình giải trí tạp kỹ, gameshow, truyền hình thực tế. Lượng từ của chương trình là 档. Trong bài: 综艺节目《乘风破浪的姐姐》."),
    ("聚焦", "jùjiāo", "tụ tiêu", "động từ", "tập trung, hội tụ (sự chú ý)", "这次会议聚焦环境问题。", "Hội nghị lần này tập trung vào vấn đề môi trường.",
     "Động từ, nghĩa gốc là hội tụ ánh sáng vào một điểm, nghĩa bóng là tập trung sự chú ý. Trong bài: 重回大众聚焦的风口浪尖, trở lại tâm điểm chú ý của công chúng."),
    ("窘境", "jiǒngjìng", "quẫn cảnh", "danh từ", "tình cảnh khó xử, cảnh khốn quẫn", "他的公司陷入了窘境。", "Công ty của anh ấy rơi vào cảnh khốn quẫn.",
     "Danh từ, nghĩa là hoàn cảnh hết sức khó xử, bế tắc. Chữ 窘 là quẫn, như trong quẫn bách. Kết hợp: 陷入窘境, rơi vào cảnh khốn quẫn; 摆脱窘境, thoát khỏi cảnh khó khăn."),
    ("转型", "zhuǎnxíng", "chuyển hình", "động từ", "chuyển đổi, chuyển hướng (mô hình, nghề nghiệp)", "很多传统企业正在转型。", "Nhiều doanh nghiệp truyền thống đang chuyển đổi.",
     "Động từ, nghĩa là thay đổi mô hình, cơ cấu hay hướng đi. 数字化转型 là chuyển đổi số. Trong bài, các nữ diễn viên trên ba mươi tuổi 需要转型, phải chuyển hướng sự nghiệp vì không còn vai diễn. Đây là từ thầy bổ sung từ bài khóa."),
    ("缩影", "suōyǐng", "súc ảnh", "danh từ", "hình ảnh thu nhỏ", "这个小村庄是中国农村的缩影。", "Ngôi làng nhỏ này là hình ảnh thu nhỏ của nông thôn Trung Quốc.",
     "Danh từ, chỉ người hay sự vật cụ thể, nhỏ bé nhưng đại diện được cho cả một loại. 缩 là co lại, 影 là hình bóng. Trong bài: 正是无数在职场拼搏的中国女性的缩影."),
    ("勤劳", "qínláo", "cần lao", "tính từ", "cần cù, chăm chỉ", "中国人民勤劳勇敢。", "Nhân dân Trung Quốc cần cù dũng cảm.",
     "Tính từ, nghĩa là chăm chỉ lao động, không ngại vất vả, âm Hán Việt là cần lao. Trong bài: 中国人的勤劳远近闻名, sự cần cù của người Trung Quốc nổi tiếng khắp nơi."),
    ("庞大", "pángdà", "bàng đại", "tính từ", "to lớn, đồ sộ, khổng lồ", "这个项目需要庞大的资金。", "Dự án này cần nguồn vốn khổng lồ.",
     "Tính từ, nghĩa là hình thể, tổ chức, số lượng lớn vượt mức bình thường, có khi hàm ý cồng kềnh. Kết hợp: 规模庞大，数量庞大. Trong bài: 庞大的人口基数, cơ số dân số khổng lồ."),
    ("体量", "tǐliàng", "thể lượng", "danh từ", "quy mô, khối lượng", "这座建筑的体量很大。", "Tòa nhà này có quy mô rất lớn.",
     "Danh từ, vốn chỉ quy mô của công trình kiến trúc, nay mở rộng chỉ quy mô nói chung: 经济体量, quy mô kinh tế. Sách ghi âm thứ hai là liáng, nhưng theo từ điển thì đọc là tǐliàng. Trong bài: 职业女性群体体量相对也很大."),
    ("备孕", "bèiyùn", "bị dựng", "động từ", "chuẩn bị mang thai", "她最近在备孕，不喝咖啡了。", "Dạo này cô ấy đang chuẩn bị mang thai, không uống cà phê nữa.",
     "Động từ, nghĩa là chuẩn bị cho việc mang thai, như khám sức khỏe, bổ sung dinh dưỡng. 备 là chuẩn bị, 孕 là thai. Trong bài: 婚后备孕先要拿号排队."),
    ("调离", "diàolí", "điều ly", "động từ", "điều chuyển đi nơi khác", "他被调离了原来的岗位。", "Anh ấy bị điều chuyển khỏi vị trí cũ.",
     "Động từ, nghĩa là điều động ra khỏi vị trí, nơi làm việc cũ. Chú ý chữ đầu đọc thanh bốn, diào, như trong 调动. Trong bài: 生娃后被调离原岗位, sinh con xong bị điều khỏi vị trí cũ."),
    ("凡", "fán", "phàm", "phó từ", "phàm, hễ là, tất cả", "凡年满十八岁的公民都有选举权。", "Phàm là công dân đủ mười tám tuổi đều có quyền bầu cử.",
     "Phó từ, nghĩa là phàm là, hễ là, tất cả những gì trong phạm vi được nói đến, không có ngoại lệ; giống 凡是. Cụm hay gặp: 凡此种种, tất cả những điều kể trên; 凡事, mọi việc. Trong bài: 凡此种种不友好."),
    ("倒逼", "dàobī", "đảo bức", "động từ", "ép ngược, buộc phải thay đổi", "环保压力倒逼企业转型。", "Áp lực bảo vệ môi trường buộc doanh nghiệp phải chuyển đổi.",
     "Động từ, nghĩa gốc là thúc ép theo chiều ngược lại; nay chỉ áp lực từ dưới lên, từ kết quả, buộc phải thay đổi. Chú ý chữ đầu đọc thanh bốn. Bài sáu chấm một có 倒逼机制; bài này có 倒逼女性婚育后主动离职."),
    ("调和", "tiáohé", "điều hòa", "động từ", "điều hòa, dung hòa, hòa giải", "他们的矛盾很难调和。", "Mâu thuẫn của họ rất khó dung hòa.",
     "Động từ, nghĩa là phối hợp cho hài hòa, hoặc hòa giải mâu thuẫn. Chú ý chữ đầu ở đây đọc thanh hai, tiáo, khác với diào trong 调离. Trong bài: 家庭与工作这对难以调和的矛盾."),
    ("着实", "zhuóshí", "trước thực", "phó từ", "thật sự, quả thật", "这件事着实让人头疼。", "Chuyện này quả thật khiến người ta đau đầu.",
     "Phó từ, nghĩa là thật sự, quả thật, giống 实在 và 确实. Chú ý chữ đầu đọc zhuó, thanh hai, như trong 着手. Trong bài: 着实让不少职场女性分身乏术."),
    ("追问", "zhuīwèn", "truy vấn", "động từ", "hỏi dồn, gặng hỏi", "在妈妈的追问下，他说出了真相。", "Trước sự gặng hỏi của mẹ, cậu ấy đã nói ra sự thật.",
     "Động từ, nghĩa là hỏi đến tận cùng, hỏi dồn. Âm Hán Việt là truy vấn, nhưng nghĩa gần với gặng hỏi hơn. Trong bài: 被追问到如何平衡家庭和事业, bị hỏi dồn về chuyện cân bằng gia đình và sự nghiệp."),
    ("尚", "shàng", "thượng", "phó từ", "còn, vẫn còn", "这个问题尚待研究。", "Vấn đề này vẫn còn chờ nghiên cứu.",
     "Phó từ văn viết, nghĩa là còn, vẫn còn, giống 还. Hay gặp 尚未, vẫn chưa; 尚可, còn tạm được. Trong bài: 三十加尚处于职业发展的黄金阶段, ngoài ba mươi vẫn đang ở giai đoạn vàng của sự nghiệp."),
    ("应聘", "yìngpìn", "ứng sính", "động từ", "ứng tuyển, dự tuyển", "她去一家外企应聘。", "Cô ấy đi ứng tuyển vào một công ty nước ngoài.",
     "Động từ, nghĩa là nhận lời mời tuyển dụng, đi ứng tuyển; đối lập với 招聘, tuyển dụng. Chữ đầu đọc thanh bốn, yìng. 应聘者 là ứng viên."),
    ("歧视", "qíshì", "kỳ thị", "động từ", "phân biệt đối xử, kỳ thị", "我们反对任何形式的性别歧视。", "Chúng tôi phản đối mọi hình thức phân biệt giới tính.",
     "Động từ, cũng làm danh từ, nghĩa là đối xử bất bình đẳng, coi thường. Âm Hán Việt là kỳ thị. Kết hợp: 性别歧视, phân biệt giới tính; 就业歧视, phân biệt đối xử trong việc làm. Đây là từ thầy bổ sung từ bài khóa."),
    ("隐性", "yǐnxìng", "ẩn tính", "tính từ", "ngầm, tiềm ẩn, không lộ ra", "隐性歧视更难发现。", "Phân biệt đối xử ngầm còn khó phát hiện hơn.",
     "Tính từ thuộc tính, nghĩa là không biểu hiện ra ngoài, đối lập với 显性 mà chúng ta đã học ở bài sáu chấm một. Trong bài: 除了显性歧视外，还有不少招聘方会采用隐性的方式."),
    ("初审", "chūshěn", "sơ thẩm", "động từ", "xét duyệt vòng đầu", "他的简历通过了初审。", "Hồ sơ của anh ấy đã qua vòng xét duyệt đầu.",
     "Động từ, nghĩa là thẩm tra lần đầu; trong tuyển dụng là vòng lọc hồ sơ. Chú ý: tiếng Việt sơ thẩm thường là phiên tòa cấp thứ nhất, tiếng Trung gọi là 一审; còn 初审 dùng rộng hơn."),
    ("同等", "tóngděng", "đồng đẳng", "tính từ", "ngang nhau, cùng mức", "男女应该享有同等的权利。", "Nam và nữ nên được hưởng quyền như nhau.",
     "Tính từ, nghĩa là cùng cấp bậc, cùng địa vị, ngang nhau. Kết hợp: 同等权利，同等待遇，同等学力. Trong bài: 同等优秀条件下, trong điều kiện xuất sắc như nhau."),
    ("唯独", "wéidú", "duy độc", "phó từ", "chỉ riêng, duy chỉ", "大家都来了，唯独他没来。", "Mọi người đều đến cả, chỉ riêng anh ấy không đến.",
     "Phó từ, nghĩa là chỉ riêng, loại trừ mọi người, mọi vật khác. Đây cũng là một mẫu câu trọng điểm. Trong bài: 唯独筛除女性的简历, chỉ riêng loại bỏ hồ sơ của nữ."),
    ("筛除", "shāichú", "si trừ", "động từ", "sàng lọc loại bỏ", "系统自动筛除了不合格的简历。", "Hệ thống tự động lọc bỏ những hồ sơ không đạt.",
     "Động từ, nghĩa là sàng lọc rồi loại bỏ. Chữ 筛 là cái sàng, như 筛子; 筛选 là sàng lọc, tuyển chọn."),
    ("谈不上", "tánbushàng", "đàm bất thượng", "cụm động từ", "không đến mức, chưa thể gọi là", "我们只是认识，谈不上朋友。", "Chúng tôi chỉ quen biết, chưa thể gọi là bạn bè.",
     "Cụm động từ, nghĩa là chưa đạt tới mức độ hay tiêu chuẩn nào đó, chưa thể nói là. Trái nghĩa: 谈得上. Trong bài: 连笔试和面试的机会都谈不上, đến cơ hội thi viết và phỏng vấn cũng chẳng có."),
    ("性骚扰", "xìngsāorǎo", "tính tao nhiễu", "danh từ", "quấy rối tình dục", "公司必须防止职场性骚扰。", "Công ty phải ngăn chặn quấy rối tình dục nơi làm việc.",
     "Danh từ, chỉ hành vi dùng lời nói hay hành động mang tính tình dục để quấy rối người khác. 骚扰 là quấy rối, như 电话骚扰, gọi điện quấy rối."),
    ("轮流", "lúnliú", "luân lưu", "phó từ", "lần lượt, thay phiên nhau", "我们轮流做饭。", "Chúng tôi thay phiên nhau nấu cơm.",
     "Phó từ, nghĩa là theo thứ tự lần lượt, hết vòng lại bắt đầu lại. Kết hợp: 轮流值班, thay phiên trực. Trong bài có một chi tiết rất xót xa: 女同事间需要排好计划表轮流怀孕."),
    ("直至", "zhízhì", "trực chí", "động từ", "cho đến, mãi đến", "他一直工作，直至深夜。", "Anh ấy làm việc liên tục cho đến khuya.",
     "Động từ văn viết, nghĩa là cho đến, giống 直到. Trong bài: 直至为照顾孩子和家庭而不得不放弃事业发展."),
    ("已然", "yǐrán", "dĩ nhiên", "phó từ", "đã, đã là (sự thật)", "事情已然如此，后悔也没用。", "Sự việc đã như vậy rồi, hối hận cũng vô ích.",
     "Phó từ văn viết, nghĩa là đã, đã thành sự thật, giống 已经. Cẩn thận, đây là từ rất dễ nhầm: tiếng Việt dĩ nhiên nghĩa là đương nhiên, còn 已然 lại là đã. Trong bài: 这些问题已然司空见惯."),
    ("晋升", "jìnshēng", "tấn thăng", "động từ", "thăng chức, đề bạt", "他去年晋升为部门经理。", "Năm ngoái anh ấy được thăng chức trưởng phòng.",
     "Động từ, nghĩa là được nâng lên chức vụ, cấp bậc cao hơn, âm Hán Việt là tấn thăng. Mẫu hay gặp: 晋升为, thăng lên làm; 晋升机会, cơ hội thăng tiến."),
    ("均等", "jūnděng", "quân đẳng", "tính từ", "đồng đều, ngang bằng", "每个人都应该有均等的机会。", "Ai cũng nên có cơ hội ngang bằng nhau.",
     "Tính từ, nghĩa là bình quân, ngang bằng. Trong bài: 晋升机会的不均等问题, vấn đề cơ hội thăng tiến không đồng đều."),
    ("生理", "shēnglǐ", "sinh lý", "danh từ", "sinh lý", "男女在生理上有差别。", "Nam và nữ có sự khác biệt về sinh lý.",
     "Danh từ, chỉ hoạt động sống và chức năng các cơ quan của cơ thể, âm Hán Việt là sinh lý. Trong bài: 由于生理结构的特殊性，女性的生育是不可避免的话题."),
    ("裁员", "cáiyuán", "tài viên", "động từ", "cắt giảm nhân sự", "公司今年裁员百分之十。", "Năm nay công ty cắt giảm mười phần trăm nhân sự.",
     "Động từ li hợp, nghĩa là cắt giảm nhân viên. Chữ 裁 là cắt, như 裁缝, thợ may. Luật Trung Quốc không cho phép doanh nghiệp cắt giảm hay giảm lương lao động nữ trong thời gian nghỉ thai sản."),
    ("缴纳", "jiǎonà", "chước nạp", "động từ", "nộp, đóng (tiền, thuế)", "公民有缴纳税款的义务。", "Công dân có nghĩa vụ nộp thuế.",
     "Động từ, nghĩa là nộp tiền hoặc hiện vật theo quy định cho nhà nước, cơ quan. Kết hợp: 缴纳学费，缴纳税费，缴纳社保."),
    ("社保", "shèbǎo", "xã bảo", "danh từ", "bảo hiểm xã hội", "公司每月为员工缴纳社保。", "Hằng tháng công ty đóng bảo hiểm xã hội cho nhân viên.",
     "Danh từ, nói gọn của 社会保障 hoặc 社会保险, bảo hiểm xã hội. Ở Trung Quốc thường gọi gộp là 五险一金, năm loại bảo hiểm và một quỹ nhà ở."),
    ("育龄", "yùlíng", "dục linh", "danh từ", "độ tuổi sinh đẻ", "她们都是育龄女性。", "Họ đều là phụ nữ trong độ tuổi sinh đẻ.",
     "Danh từ, chỉ độ tuổi thích hợp để sinh con. 育 là sinh nở, nuôi dưỡng. Trong bài: 不愿意招聘三十岁左右的育龄女性."),
    ("产假", "chǎnjià", "sản giá", "danh từ", "nghỉ thai sản", "她休了半年产假。", "Cô ấy nghỉ thai sản nửa năm.",
     "Danh từ, chỉ kỳ nghỉ của lao động nữ trước và sau khi sinh con. Chú ý chữ thứ hai đọc thanh bốn, jià. Luật Lao động Trung Quốc quy định nghỉ thai sản không ít hơn chín mươi ngày; ở Việt Nam là sáu tháng. Đây là từ thầy bổ sung từ bài khóa."),
    ("配偶", "pèi'ǒu", "phối ngẫu", "danh từ", "vợ hoặc chồng, người phối ngẫu", "表格上要填写配偶的姓名。", "Trên tờ khai phải điền họ tên vợ hoặc chồng.",
     "Danh từ, chỉ vợ hoặc chồng, thường dùng trong văn bản pháp luật. Trong bài: 配偶陪产假, kỳ nghỉ của người chồng để chăm vợ sinh."),
    ("重担", "zhòngdàn", "trọng đảm", "danh từ", "gánh nặng, trách nhiệm nặng nề", "他一个人挑起了养家的重担。", "Một mình anh ấy gánh vác trách nhiệm nuôi cả nhà.",
     "Danh từ, nghĩa đen là gánh nặng, nghĩa bóng là trách nhiệm nặng nề. Chữ thứ hai đọc thanh bốn, dàn, chỉ cái gánh. Trong bài: 早期的大部分育儿重担仍要女性承担."),
    ("陪伴", "péibàn", "bồi bạn", "động từ", "ở bên, bầu bạn, đồng hành", "父母要多陪伴孩子。", "Bố mẹ nên dành nhiều thời gian ở bên con.",
     "Động từ, nghĩa là ở bên cạnh làm bạn, đồng hành. Trong bài: 陪伴孩子和接送孩子, ở bên con và đưa đón con."),
    ("琐事", "suǒshì", "tỏa sự", "danh từ", "việc vặt, chuyện lặt vặt", "每天都有很多家庭琐事要处理。", "Ngày nào cũng có nhiều việc vặt trong nhà phải lo.",
     "Danh từ, nghĩa là việc nhỏ nhặt, lặt vặt. Chữ 琐 là vụn vặt, như 琐碎. Trong bài: 家庭琐事, việc vặt trong gia đình."),
    ("塑造", "sùzào", "tố tạo", "động từ", "nặn, tạc; xây dựng (hình tượng)", "这部小说塑造了一个勇敢的女孩。", "Cuốn tiểu thuyết này xây dựng hình tượng một cô gái dũng cảm.",
     "Động từ, nghĩa gốc là nặn tượng, tạc tượng; nghĩa bóng là dùng ngôn ngữ, nghệ thuật để xây dựng hình tượng. Kết hợp: 塑造形象，塑造人物，塑造品牌. Chú ý chữ đầu đọc sù."),
    ("一把手", "yībǎshǒu", "nhất bả thủ", "danh từ", "người đứng đầu; tay giỏi việc", "他是这个单位的一把手。", "Ông ấy là người đứng đầu đơn vị này.",
     "Danh từ, chỉ lãnh đạo cao nhất trong một tổ chức, đơn vị; cũng chỉ người làm giỏi. Cụm 里里外外一把手 là việc trong việc ngoài đều một tay đảm đương, rất giống câu giỏi việc nước, đảm việc nhà."),
    ("险峻", "xiǎnjùn", "hiểm tuấn", "tính từ", "hiểm trở; hiểm ác, khắc nghiệt", "这座山非常险峻。", "Ngọn núi này vô cùng hiểm trở.",
     "Tính từ, nghĩa gốc là núi cao và hiểm trở; trong bài dùng nghĩa bóng là nguy hiểm, khắc nghiệt: 险峻的职场环境, môi trường công sở khắc nghiệt."),
    ("夹缝", "jiāfèng", "giáp phùng", "danh từ", "khe hở, kẽ hẹp", "小草从石头的夹缝中长出来。", "Ngọn cỏ mọc lên từ kẽ đá.",
     "Danh từ, chỉ khe hẹp giữa hai vật sát nhau. Chú ý chữ thứ hai đọc thanh bốn, fèng. 在夹缝中生存 là sống trong khe hẹp, tức là sống chật vật giữa hai áp lực. Trong bài: 女性在家庭和职场的夹缝中生存."),
    ("洒脱", "sǎtuō", "sái thoát", "tính từ", "phóng khoáng, ung dung, không gò bó", "他的性格很洒脱。", "Tính cách anh ấy rất phóng khoáng.",
     "Tính từ, nghĩa là lời nói, cử chỉ, phong cách tự nhiên, thoải mái, không câu nệ. Trong bài: 远不能洒脱地乘风破浪, còn lâu mới có thể ung dung đạp gió rẽ sóng."),
]

add("bullets", chapter="Từ mới (45 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 6.3 có 45 từ mới, chia thành 15 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 调离 (diào) ≠ 调和 (tiáo) · 着实 (zhuó) · 应聘 (yìng) · 夹缝 (fèng) · 产假 (jià)",
           "Từ dễ nhầm: 已然 = đã (không phải “dĩ nhiên”!) · 初审 · 追问"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bảng từ của sách có bốn mươi bốn từ. Hai từ 拼搏 và 显性 chúng ta đã học ở bài sáu chấm một, nên thầy thay bằng ba từ quan trọng trong bài khóa: 转型，歧视 và 产假. Tổng cộng bốn mươi lăm từ, chia thành mười lăm nhóm.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Chú ý cách đọc: 调离 đọc diàolí, còn 调和 đọc tiáohé, cùng một chữ mà hai cách đọc. 着实 đọc zhuóshí, 应聘 đọc yìngpìn, 夹缝 đọc jiāfèng, 产假 đọc chǎnjià."),
         F(4, "Đặc biệt cẩn thận với từ 已然: âm Hán Việt là dĩ nhiên, nhưng nghĩa lại là đã, chứ không phải đương nhiên. Chúng ta bắt đầu.")])

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
# (chữ Hán hiển thị, dịch, ghi chú[, lời đọc tiếng Trung: số viết bằng chữ Hán, bỏ ngoặc kép])
P = [
    ("综艺节目《乘风破浪的姐姐》让一群年龄“30+”的姐姐们重回大众聚焦的风口浪尖。但令人无可奈何的事实是，即便是功成名就、自认为正处于“黄金年龄”的女演员、女歌手，也要面临“没有戏演”、需要转型的职场窘境。",
     "Chương trình giải trí “Chị đẹp đạp gió rẽ sóng” đã đưa một nhóm các chị ngoài “30” trở lại tâm điểm chú ý của công chúng. Nhưng sự thật khiến người ta bất lực là: ngay cả những nữ diễn viên, nữ ca sĩ đã thành danh, tự cho rằng mình đang ở “độ tuổi vàng”, cũng phải đối mặt với cảnh “không có vai để đóng”, phải chuyển hướng sự nghiệp.",
     ["《乘风破浪的姐姐》 là chương trình của Mango TV năm hai nghìn không trăm hai mươi: ba mươi nữ nghệ sĩ sinh trước năm một nghìn chín trăm chín mươi cùng luyện tập, thi đấu để chọn ra bảy người lập nhóm nhạc. 三十加 là ngoài ba mươi. 风口浪尖 là đầu sóng ngọn gió, tâm điểm chú ý.",
      "令人无可奈何的是 là điều khiến người ta bất lực là; mẫu 令人什么的是 là mẫu câu trọng điểm. 即便是，也 là cho dù là, cũng. 功成名就 là công thành danh toại. 没有戏演 là không có vai diễn. 窘境 là cảnh khốn quẫn."],
     "综艺节目《乘风破浪的姐姐》让一群年龄三十加的姐姐们重回大众聚焦的风口浪尖。但令人无可奈何的事实是，即便是功成名就、自认为正处于黄金年龄的女演员、女歌手，也要面临没有戏演、需要转型的职场窘境。"),
    ("而这些“30+”姐姐们的遭遇，正是无数在职场拼搏的中国女性的缩影。女性想要在职场上乘风破浪，绝非轻而易举。",
     "Mà cảnh ngộ của những chị em ngoài “30” này chính là hình ảnh thu nhỏ của vô số phụ nữ Trung Quốc đang bươn chải nơi công sở. Phụ nữ muốn đạp gió rẽ sóng nơi công sở tuyệt đối không phải chuyện dễ dàng.",
     ["遭遇 là cảnh ngộ, những gì gặp phải, thường là điều không may. 缩影 là hình ảnh thu nhỏ. 拼搏 là dốc sức phấn đấu, chúng ta đã học ở bài sáu chấm một.",
      "乘风破浪 là thành ngữ: thuyền thuận gió rẽ sóng tiến lên, ví với vượt qua khó khăn, dũng cảm tiến lên. 绝非 là tuyệt đối không phải. 轻而易举 là nhẹ nhàng dễ dàng, chẳng tốn sức."],
     "而这些三十加姐姐们的遭遇，正是无数在职场拼搏的中国女性的缩影。女性想要在职场上乘风破浪，绝非轻而易举。"),
    ("中国人的勤劳远近闻名，中国女性的劳动参与率在全球位居前列。尽管这一数据近年来呈现下降趋势，但在世界范围内依旧遥遥领先。",
     "Sự cần cù của người Trung Quốc nổi tiếng khắp nơi, tỉ lệ tham gia lao động của phụ nữ Trung Quốc đứng hàng đầu thế giới. Dù những năm gần đây con số này có xu hướng giảm, nhưng trên phạm vi thế giới vẫn bỏ xa nhiều nước khác.",
     ["Tiêu đề nhỏ của phần này là 职场女性腹背受敌, phụ nữ đi làm bị đánh cả trước lẫn sau. 腹背受敌 là thành ngữ: bụng và lưng đều gặp địch, tức bị kẹp giữa hai mặt tấn công. 远近闻名 là xa gần đều biết tiếng.",
      "劳动参与率 là tỉ lệ tham gia lực lượng lao động. 位居前列 là đứng ở hàng đầu. 呈现下降趋势 là có xu hướng giảm, giống mẫu 呈现态势 ở bài trước. 遥遥领先 là dẫn đầu cách biệt."]),
    ("在中国庞大的人口基数下，中国职业女性群体体量相对也很大。招聘时当着众人被问及是否婚育；婚后备孕先要“拿号”排队；生娃后被调离原岗位……凡此种种“不友好”都是在倒逼女性婚育后主动离职。",
     "Với cơ số dân số khổng lồ của Trung Quốc, quy mô nhóm phụ nữ đi làm cũng tương đối lớn. Tuyển dụng thì bị hỏi trước mặt mọi người đã kết hôn, sinh con chưa; cưới rồi muốn chuẩn bị mang thai phải “lấy số” xếp hàng; sinh con xong bị điều khỏi vị trí cũ… Tất cả những điều “không thân thiện” ấy đều đang ép phụ nữ phải tự nghỉ việc sau khi kết hôn, sinh con.",
     ["基数 là cơ số, con số làm gốc. 当着众人 là trước mặt mọi người; 当着 là mẫu câu trọng điểm. 被问及 là bị hỏi đến, văn viết. 婚育 là kết hôn và sinh con. 拿号排队 là lấy số xếp hàng: ở một số đơn vị, nữ nhân viên phải đăng ký lượt mới được mang thai.",
      "生娃 là sinh con; 娃 là khẩu ngữ, nghĩa là đứa bé. 凡此种种 là tất cả những điều kể trên. 倒逼 là ép ngược. 主动离职 là tự xin nghỉ việc: công ty không sa thải, nhưng khiến người ta không thể ở lại."]),
    ("而家庭与工作这对难以调和的矛盾，着实让不少职场女性分身乏术。对许多职业女性来说，被追问到“如何平衡家庭和事业”这一问题是家常便饭。“30+”尚处于职业发展的黄金阶段，也恰好撞上女性的婚育高峰期。",
     "Còn mâu thuẫn khó dung hòa giữa gia đình và công việc thật sự khiến không ít phụ nữ đi làm không thể phân thân. Với nhiều phụ nữ đi làm, bị gặng hỏi “cân bằng gia đình và sự nghiệp thế nào” là chuyện cơm bữa. Tuổi ngoài “30” vẫn đang là giai đoạn vàng để phát triển sự nghiệp, lại đúng vào cao điểm kết hôn, sinh con của phụ nữ.",
     ["这对矛盾 là cặp mâu thuẫn này, 对 là lượng từ chỉ cặp. 调和 đọc tiáohé, là dung hòa. 着实 là thật sự. 分身乏术 là thành ngữ: không có phép phân thân, ý nói quá bận, không thể cùng lúc lo nhiều việc.",
      "家常便饭 là cơm nhà bữa thường, ví với chuyện xảy ra thường xuyên, chuyện cơm bữa. 尚 là vẫn còn. 撞上 là đâm sầm vào, trùng đúng vào. 高峰期 là thời kỳ cao điểm."],
     "而家庭与工作这对难以调和的矛盾，着实让不少职场女性分身乏术。对许多职业女性来说，被追问到如何平衡家庭和事业这一问题是家常便饭。三十加尚处于职业发展的黄金阶段，也恰好撞上女性的婚育高峰期。"),
    ("当职业发展撞上适婚年龄，是否生育就成了无法回避的问题。未婚的女性求职者也会被刨根问底“是否有男朋友”、“几年内会不会考虑结婚”，而已婚的女性求职者则会被问到“是否有生育一胎二胎的计划”。",
     "Khi phát triển sự nghiệp trùng với tuổi kết hôn, có sinh con hay không trở thành câu hỏi không thể né tránh. Ứng viên nữ chưa kết hôn cũng bị hỏi cặn kẽ “có bạn trai chưa”, “trong mấy năm tới có tính chuyện kết hôn không”; còn ứng viên nữ đã kết hôn thì bị hỏi “có kế hoạch sinh con thứ nhất, con thứ hai không”.",
     ["适婚年龄 là tuổi thích hợp để kết hôn. 无法回避 là không thể né tránh. 求职者 là người tìm việc.",
      "刨根问底 là thành ngữ: đào tận gốc, hỏi tận đáy, tức là hỏi cặn kẽ đến cùng; chữ đầu đọc páo, nghĩa là đào bới. 一胎二胎 là con thứ nhất, con thứ hai."]),
    ("除此之外，用人单位招聘时限制性别，使得女性在职场应聘中雪上加霜。比如，一些公司在招聘广告中会写明“男士优先”或“只招男性”。",
     "Ngoài ra, việc đơn vị tuyển dụng giới hạn giới tính khiến phụ nữ đi xin việc càng thêm khó khăn chồng chất. Ví dụ, một số công ty ghi rõ trong quảng cáo tuyển dụng “ưu tiên nam giới” hoặc “chỉ tuyển nam”.",
     ["除此之外 là ngoài ra. 用人单位 là đơn vị sử dụng lao động. 使得 là khiến cho. 雪上加霜 là thành ngữ: trên tuyết lại thêm sương, tức là họa vô đơn chí, khó khăn chồng chất.",
      "写明 là ghi rõ. 男士优先 là ưu tiên nam giới; 只招男性 là chỉ tuyển nam. Đây là phân biệt đối xử công khai, mà bài gọi là 显性歧视."]),
    ("除了显性歧视外，还有不少招聘方会采用隐性的方式，例如初审时同等优秀条件下唯独筛除女性的简历，连笔试和面试的机会都谈不上。",
     "Ngoài phân biệt đối xử công khai, không ít bên tuyển dụng còn dùng cách ngầm, chẳng hạn khi xét duyệt hồ sơ vòng đầu, trong điều kiện xuất sắc như nhau thì chỉ riêng loại bỏ hồ sơ của nữ, khiến họ đến cơ hội thi viết và phỏng vấn cũng không có.",
     ["显性歧视 là phân biệt công khai; 隐性 là ngầm, tiềm ẩn: hai từ trái nghĩa. 招聘方 là bên tuyển dụng. 初审 là xét duyệt vòng đầu.",
      "唯独 là chỉ riêng, một mẫu câu trọng điểm. 筛除 là sàng lọc loại bỏ. 连，都谈不上 là ngay cả, cũng chẳng có; 谈不上 là chưa đến mức, không thể nói tới."]),
    ("哪怕成功入职，女性也被职场性骚扰等问题所困扰。同样让人难以接受的是，她们在婚育阶段就被迫调岗减薪，女同事间则需要排好计划表“轮流”怀孕，直至为照顾孩子和家庭而不得不放弃事业发展。",
     "Cho dù vào làm thành công, phụ nữ vẫn bị những vấn đề như quấy rối tình dục nơi công sở làm phiền. Điều cũng khó chấp nhận không kém là, đến giai đoạn kết hôn sinh con họ liền bị ép chuyển vị trí, giảm lương; các đồng nghiệp nữ còn phải xếp lịch để “thay phiên” mang thai, cho đến khi vì chăm con, lo cho gia đình mà buộc phải từ bỏ sự nghiệp.",
     ["哪怕，也 là cho dù, cũng: mẫu câu trọng điểm. 入职 là vào làm. 被，所困扰 là bị làm phiền bởi, cấu trúc bị động văn viết.",
      "让人难以接受的是 là điều khó chấp nhận là, lại là mẫu 让人什么的是. 调岗减薪 là chuyển vị trí, giảm lương. 轮流怀孕 là thay phiên nhau mang thai, để đơn vị không bị thiếu người cùng lúc. 直至 là cho đến khi."]),
    ("这些问题已然“司空见惯”，直接造成晋升机会的不均等问题。长此以往，女性在职场就只能担任普通职位或辅助工作，进入管理层的比例也必然大大低于男性。",
     "Những vấn đề này đã trở nên “quá quen thuộc”, trực tiếp gây ra sự bất bình đẳng về cơ hội thăng tiến. Cứ kéo dài như vậy, phụ nữ nơi công sở chỉ có thể đảm nhận những vị trí bình thường hoặc công việc hỗ trợ, tỉ lệ vào tầng lớp quản lý chắc chắn cũng thấp hơn nam giới rất nhiều.",
     ["已然 là đã, cẩn thận đừng nhầm với dĩ nhiên trong tiếng Việt. 司空见惯 là thành ngữ: 司空 là một chức quan thời xưa, ông ấy thấy mãi thành quen; ý nói chuyện thường thấy, chẳng có gì lạ. 晋升 là thăng tiến.",
      "长此以往 là cứ kéo dài mãi như thế. 担任 là đảm nhận. 辅助工作 là công việc phụ trợ. 管理层 là tầng lớp quản lý. 必然 là tất yếu, chắc chắn."]),
    ("毋庸置疑，女性在职场中遇到的一些问题仅仅因为她们是女性。由于生理结构的特殊性，女性的生育是不可避免的话题。",
     "Không cần phải nghi ngờ, một số vấn đề phụ nữ gặp phải nơi công sở chỉ đơn giản vì họ là phụ nữ. Do đặc thù về cấu tạo sinh lý, chuyện sinh con của phụ nữ là đề tài không thể tránh khỏi.",
     ["Tiêu đề nhỏ của phần này là 三十加的她们为什么这么难？ Vì sao các chị ngoài ba mươi lại khó khăn đến thế? Phần này phân tích nguyên nhân. 毋庸置疑 là thành ngữ: không cần nghi ngờ; 毋庸 là không cần, văn viết.",
      "仅仅因为 là chỉ vì. 生理结构 là cấu tạo sinh lý. 不可避免 là không thể tránh khỏi."]),
    ("产假本意上是为了保护女性的合法权益，但在实际操作中，由于产假期间企业不得裁员、减薪，而且得继续缴纳社保，许多公司为了减少成本，反而不愿意招聘30岁左右的育龄女性。",
     "Nghỉ thai sản vốn là để bảo vệ quyền lợi hợp pháp của phụ nữ, nhưng trong thực tế, vì trong thời gian nghỉ thai sản doanh nghiệp không được cắt giảm, giảm lương, lại phải tiếp tục đóng bảo hiểm xã hội, nên nhiều công ty để giảm chi phí, ngược lại không muốn tuyển phụ nữ trong độ tuổi sinh đẻ khoảng 30 tuổi.",
     ["本意上 là về ý định ban đầu. 合法权益 là quyền lợi hợp pháp. 实际操作 là khi thực hiện trên thực tế. 不得 là không được phép, văn viết.",
      "而且得继续缴纳社保: chữ 得 ở đây đọc děi, nghĩa là phải. 反而 là ngược lại: chính sách bảo vệ phụ nữ lại khiến công ty ngại tuyển phụ nữ. Luật Lao động Trung Quốc quy định lao động nữ được nghỉ thai sản không ít hơn chín mươi ngày."],
     "产假本意上是为了保护女性的合法权益，但在实际操作中，由于产假期间企业不得裁员、减薪，而且得继续缴纳社保，许多公司为了减少成本，反而不愿意招聘三十岁左右的育龄女性。"),
    ("随着“全面二孩”政策落地，全国大部分地区延长了产假时间，在产假最长的西藏，女性可以休假一年。但配偶陪产假最长不过30天，早期的大部分育儿重担仍要女性承担。",
     "Cùng với việc chính sách “toàn diện hai con” đi vào thực tế, phần lớn các địa phương đã kéo dài thời gian nghỉ thai sản; ở Tây Tạng, nơi có thời gian nghỉ thai sản dài nhất, phụ nữ có thể nghỉ một năm. Nhưng kỳ nghỉ chăm vợ sinh của người chồng dài nhất cũng không quá 30 ngày, phần lớn gánh nặng nuôi con thời kỳ đầu vẫn do phụ nữ gánh vác.",
     ["全面二孩 là chính sách mọi cặp vợ chồng được sinh hai con, áp dụng từ năm hai nghìn không trăm mười sáu; đến năm hai nghìn không trăm hai mươi mốt, Trung Quốc tiếp tục cho phép sinh ba con. 落地 là đi vào thực tế.",
      "陪产假 là kỳ nghỉ của người chồng để chăm vợ sinh. 不过 ở đây là không quá. 育儿重担 là gánh nặng nuôi dạy con. 承担 là gánh vác."],
     "随着全面二孩政策落地，全国大部分地区延长了产假时间，在产假最长的西藏，女性可以休假一年。但配偶陪产假最长不过三十天，早期的大部分育儿重担仍要女性承担。"),
    ("在传统社会男女分工影响下，男性更多地承担养家的责任，而女性则更多地承担顾家的责任，即所谓“男主外女主内”。当今社会男女平等，双职工家庭的女性不仅要面临职场的焦头烂额，还要承担家庭的鸡毛蒜皮。",
     "Dưới ảnh hưởng của sự phân công nam nữ trong xã hội truyền thống, đàn ông gánh trách nhiệm kiếm tiền nuôi nhà nhiều hơn, còn phụ nữ gánh trách nhiệm chăm lo gia đình nhiều hơn, tức là “nam lo việc ngoài, nữ lo việc trong”. Xã hội ngày nay nam nữ bình đẳng, phụ nữ trong gia đình cả vợ cả chồng đi làm không chỉ phải đối mặt với cảnh rối bời nơi công sở, mà còn phải gánh cả những chuyện lặt vặt trong nhà.",
     ["养家 là kiếm tiền nuôi gia đình, 顾家 là chăm lo việc nhà. 即所谓 là tức là cái gọi là. 男主外女主内 rất giống quan niệm đàn ông xây nhà, đàn bà xây tổ ấm ở Việt Nam.",
      "双职工家庭 là gia đình cả hai vợ chồng đều đi làm. 焦头烂额 là thành ngữ: cháy đầu bỏng trán, chỉ bận rộn rối bời. 鸡毛蒜皮 là lông gà vỏ tỏi, chỉ những chuyện vụn vặt không đáng kể."]),
    ("别的不说，在打扫做饭、陪伴孩子和接送孩子辅导学习这些所谓家庭琐事上，女性平均投入了男性两倍或以上的时长。可见不少女性努力地平衡着事业和家庭，两手都要抓，被塑造成了里里外外一把手的“超人”妈妈。",
     "Chưa nói gì khác, chỉ riêng những việc vặt trong nhà như dọn dẹp nấu cơm, ở bên con, đưa đón con và kèm con học, phụ nữ trung bình đã bỏ ra thời gian gấp đôi nam giới hoặc hơn. Có thể thấy không ít phụ nữ đang cố gắng cân bằng sự nghiệp và gia đình, việc nào cũng phải nắm, bị khắc họa thành những bà mẹ “siêu nhân” việc trong việc ngoài đều đảm đương.",
     ["别的不说 là chưa nói gì khác, chỉ nói một việc thôi: mẫu câu trọng điểm. 接送 là đưa đón. 辅导学习 là kèm học. 两倍或以上 là gấp đôi hoặc hơn.",
      "可见 là có thể thấy. 两手都要抓 là hai tay đều phải nắm, tức việc nào cũng phải lo. 塑造成 là bị nhào nặn, khắc họa thành. 里里外外一把手 là việc trong việc ngoài đều một tay đảm đương."]),
    ("在外，她们面临险峻的职场环境。在家，她们仍需要“相夫教子”做家务。总之，女性在家庭和职场的夹缝中生存，她们的生活，远不能洒脱地“乘风破浪”，倒蛮像是艰难地“披荆斩棘”。",
     "Ở ngoài, họ đối mặt với môi trường công sở khắc nghiệt. Ở nhà, họ vẫn phải “giúp chồng dạy con”, làm việc nhà. Tóm lại, phụ nữ sống trong khe hẹp giữa gia đình và công sở; cuộc sống của họ còn lâu mới được ung dung “đạp gió rẽ sóng”, mà trái lại khá giống như đang chật vật “vạch gai mở lối”.",
     ["相夫教子 là giúp chồng, dạy con; chữ đầu đọc xiàng, nghĩa là giúp đỡ. 夹缝 là khe hẹp. 远不能 là còn lâu mới có thể. 洒脱 là ung dung, phóng khoáng.",
      "倒蛮像是 là trái lại khá giống như; 倒 là trái lại, 蛮 là khá, khẩu ngữ. 披荆斩棘 là thành ngữ: vạch bụi gai, chặt cây gai, ví với vượt qua muôn vàn trở ngại. Câu kết đối lập hai thành ngữ: không phải đạp gió rẽ sóng hào hùng, mà là vạch gai mở lối đầy gian nan."]),
]
# tiêu đề nhỏ của bài khóa: đoạn bắt đầu phần đó
HEAD = {3: "职场女性“腹背受敌”", 11: "30+的她们为什么这么难？"}

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 30 岁的职场姐姐如何乘风破浪？", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa. Bài được cải biên từ bài báo 三十岁的职场女人，无法乘风破浪, Phụ nữ ba mươi tuổi nơi công sở không thể đạp gió rẽ sóng, của tác giả 潘子怡, đăng trên chuyên mục 网易数读 ngày hai mươi sáu tháng sáu năm hai nghìn không trăm hai mươi. Bài dài khoảng một nghìn ba trăm chữ, có hai tiêu đề nhỏ.",
         F(0, "Thầy chia bài thành mười sáu đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Bài này có rất nhiều thành ngữ, nên nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 90 else 50 if len(zh) <= 115 else 46
    title = f"Bài khóa – đoạn {i}/{len(P)}" + (f" · {HEAD[i]}" if i in HEAD else "")
    add("passage", section="Bài khóa 课文", title=title, zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Bố cục & ghi chú", section="Bài khóa 课文", title="Bố cục bài khóa", size=34,
    items=["## 1. Mở đầu (đoạn 1–2)",
           "《乘风破浪的姐姐》 → các chị “30+” cũng phải 转型 → 中国职场女性的缩影",
           "## 2. 职场女性“腹背受敌” (đoạn 3–10)",
           "Bị hỏi chuyện 婚育 · 男士优先 / 只招男性 · 隐性歧视 · 调岗减薪 · “轮流”怀孕 · 晋升机会不均等",
           "## 3. 30+的她们为什么这么难？ (đoạn 11–15)",
           "生理特殊性 + chi phí 产假 · 陪产假 quá ngắn · 男主外女主内 · việc nhà gấp đôi nam giới",
           "## 4. Kết luận (đoạn 16)",
           "在家庭和职场的夹缝中生存：不是“乘风破浪”，而是“披荆斩棘”"],
    say=["Trước khi sang phần mẫu câu, chúng ta cùng nhìn lại bố cục bài khóa. Bài có bốn phần: dẫn đề, thực trạng, nguyên nhân và kết luận.",
         F(1, "Phần một, dẫn đề: từ chương trình Chị đẹp đạp gió rẽ sóng, tác giả chỉ ra rằng ngay cả nữ nghệ sĩ nổi tiếng ngoài ba mươi tuổi cũng phải chuyển hướng; họ là hình ảnh thu nhỏ của phụ nữ đi làm ở Trung Quốc."),
         F(3, "Phần hai, thực trạng: phụ nữ đi làm bị đánh từ cả hai phía. Họ bị hỏi chuyện kết hôn sinh con, bị giới hạn giới tính công khai lẫn ngầm, bị điều chuyển, giảm lương, thậm chí phải thay phiên mang thai, nên cơ hội thăng tiến không bình đẳng."),
         F(5, "Phần ba, nguyên nhân: vì đặc thù sinh lý và chi phí nghỉ thai sản mà doanh nghiệp ngại tuyển; kỳ nghỉ của người chồng quá ngắn; và quan niệm nam lo việc ngoài, nữ lo việc trong khiến phụ nữ làm việc nhà gấp đôi nam giới."),
         F(7, "Phần bốn, kết luận: phụ nữ sống trong khe hẹp giữa gia đình và công sở; cuộc sống của họ không phải là đạp gió rẽ sóng, mà là vạch gai mở lối. Câu kết này trả lời trực tiếp cho câu hỏi ở tên bài.")])

add("bullets", section="Bài khóa 课文", title="Ghi chú 注释: hiểu thêm về bối cảnh", size=33,
    items=["《乘风破浪的姐姐》: show của Mango TV (2020) – 30 nữ nghệ sĩ sinh trước 1990 luyện tập, thi đấu, chọn ra 7 người lập nhóm nhạc",
           "全面二孩: 1982 kế hoạch hóa gia đình là quốc sách (mỗi cặp 1 con) → 2013 单独二孩 → 2016 全面二孩 → 2021 cho phép sinh 3 con",
           "产假: 《劳动法》 – lao động nữ sinh con được nghỉ thai sản không ít hơn 90 ngày",
           "《妇女权益保障法》: không đơn vị nào được vì kết hôn, mang thai, nghỉ thai sản, cho con bú mà giảm lương, sa thải lao động nữ"],
    say=["Sách có ba ghi chú giúp hiểu thêm bối cảnh bài khóa.",
         F(0, "Một: 乘风破浪的姐姐, chương trình giải trí của Mango TV, thuộc đài truyền hình Hồ Nam, ra mắt năm hai nghìn không trăm hai mươi. Ba mươi nữ nghệ sĩ sinh trước năm một nghìn chín trăm chín mươi cùng luyện tập, thi thố để chọn ra bảy người lập nhóm nhạc. Họ đều đã thành danh, nhưng ngoài ba mươi tuổi thì ít nhiều đều gặp cảnh bị lãng quên, buộc phải chuyển hướng."),
         F(1, "Hai: chính sách sinh con của Trung Quốc. Năm một nghìn chín trăm tám mươi hai, kế hoạch hóa gia đình trở thành quốc sách, mỗi cặp vợ chồng một con. Năm hai nghìn không trăm mười ba có chính sách 单独二孩: nếu một trong hai vợ chồng là con một thì được sinh hai con. Từ ngày một tháng một năm hai nghìn không trăm mười sáu là 全面二孩, mọi cặp vợ chồng được sinh hai con. Năm hai nghìn không trăm hai mươi mốt, Trung Quốc cho phép sinh ba con."),
         F(2, "Ba: 产假, nghỉ thai sản. Luật Lao động Trung Quốc quy định lao động nữ sinh con được nghỉ thai sản không ít hơn chín mươi ngày."),
         F(3, "Luật Bảo đảm quyền lợi phụ nữ còn quy định: không đơn vị nào được vì lý do kết hôn, mang thai, nghỉ thai sản, cho con bú mà giảm lương, sa thải lao động nữ hay đơn phương chấm dứt hợp đồng. Luật là vậy, nhưng như bài khóa cho thấy, trên thực tế phụ nữ vẫn gặp rất nhiều khó khăn.")])

# ======================= MẪU CÂU =======================
add("bullets", chapter="Mẫu câu: 令人…的是 · 即便是 · 当着 · 凡", section="Mẫu câu 重点句型", title="1. 令人/让人……的是 · 2. 即便是……也（不）要……", size=33,
    items=["## 令人……的是 / 让人……的是: điều khiến người ta… là… (giữa thường là động từ, tính từ chỉ cảm xúc)",
           "但令人无可奈何的事实是，即便是功成名就……的女演员、女歌手，也要面临“没有戏演”、需要转型的职场窘境。",
           "让人难忘的是毕业十周年的那次聚会。",
           "令人遗憾的是，他虽然闯进了淘汰赛，但是因为两年前的旧伤复发而止步于四强。",
           "## 即便是……也（不）要……: cho dù là… cũng (đừng)… – nhấn mạnh giả thiết",
           "努力奋斗吧！即便是遇到挫折也不要让生活失去色彩。",
           "即便是一粒尘埃，也要发出自己的光芒。"],
    say=["Bây giờ chúng ta sang phần mẫu câu và từ ngữ trọng điểm. Bài này có tám điểm, thầy gộp mỗi slide hai điểm. Đầu tiên là 令人的是 và 即便是也.",
         F(0, "令人什么的是, hay 让人什么的是, nghĩa là điều khiến người ta thế nào là. Ở giữa thường là động từ hay tính từ chỉ cảm xúc: 遗憾，难忘，惊讶，无可奈何. Mẫu này giúp đưa ra đánh giá trước, rồi mới nêu sự việc, rất hay dùng trong văn nghị luận."),
         F(1, "Ví dụ từ bài khóa: 但令人无可奈何的事实是，即便是功成名就的女演员、女歌手，也要面临没有戏演、需要转型的职场窘境。"),
         F(2, "让人难忘的是毕业十周年的那次聚会。 Điều khiến tôi khó quên là buổi họp mặt kỷ niệm mười năm tốt nghiệp."),
         F(3, "令人遗憾的是，他虽然闯进了淘汰赛，但是因为两年前的旧伤复发而止步于四强。 Điều đáng tiếc là, tuy anh ấy lọt vào vòng loại trực tiếp, nhưng vì chấn thương cũ hai năm trước tái phát nên dừng bước ở bán kết."),
         F(4, "即便是，也 nghĩa là cho dù là, cũng; dạng phủ định 也不要 là cũng đừng. 即便 giống 即使, nhưng mang màu văn viết hơn. Mẫu này nêu một giả thiết, thường là trường hợp cực đoan, để nhấn mạnh kết quả không đổi."),
         F(5, "努力奋斗吧！即便是遇到挫折也不要让生活失去色彩。 Hãy cố gắng phấn đấu! Cho dù gặp thất bại cũng đừng để cuộc sống mất đi màu sắc."),
         F(6, "即便是一粒尘埃，也要发出自己的光芒。 Cho dù chỉ là một hạt bụi, cũng phải tỏa ra ánh sáng của riêng mình.")])

add("bullets", section="Mẫu câu 重点句型", title="3. 当着…… · 4. 凡……", size=34,
    items=["## 当着: trước mặt ai, khi có ai ở đó (当着 + người + 的面)",
           "招聘时当着众人被问及是否婚育。",
           "当着我的面，你有什么想说的就都说出来吧。",
           "我当着大家的面把礼物拆开了。",
           "## 凡: phàm, hễ là – tất cả trong phạm vi đó, không có ngoại lệ (= 凡是)",
           "……凡此种种“不友好”都是在倒逼女性婚育后主动离职。",
           "凡事自己努力去做就好。 · 凡年龄满十八岁的公民都有选举与被选举的权利。"],
    say=["Tiếp theo là 当着 và 凡.",
         F(0, "当着 nghĩa là trước mặt ai, khi có người đó ở đó. Mẫu thường gặp: 当着谁的面, trước mặt ai. Chữ đầu đọc thanh một."),
         F(1, "Ví dụ từ bài khóa: 招聘时当着众人被问及是否婚育。 Khi tuyển dụng bị hỏi trước mặt mọi người có kết hôn, sinh con chưa: vừa riêng tư, vừa khó xử."),
         F(2, "当着我的面，你有什么想说的就都说出来吧。 Trước mặt tôi đây, cậu có gì muốn nói thì cứ nói hết ra đi."),
         F(3, "我当着大家的面把礼物拆开了。 Tôi mở quà ngay trước mặt mọi người."),
         F(4, "凡 nghĩa là phàm, hễ là, chỉ tất cả trong phạm vi được nói đến, không có ngoại lệ, giống 凡是. Phía sau thường có 都 hô ứng."),
         F(5, "Ví dụ từ bài khóa: 凡此种种不友好都是在倒逼女性婚育后主动离职。 Tất cả những điều không thân thiện ấy đều đang ép phụ nữ tự nghỉ việc. 凡此种种 là một cụm cố định rất hay gặp."),
         F(6, "凡事自己努力去做就好。 Việc gì cũng vậy, cứ tự mình cố gắng làm là được. Và: 凡年龄满十八岁的公民都有选举与被选举的权利。 Phàm công dân đủ mười tám tuổi đều có quyền bầu cử và ứng cử.")])

add("bullets", chapter="Mẫu câu: 唯独 · 谈不上 · 哪怕 · 别的不说", section="Mẫu câu 重点句型", title="5. 唯独…… · 6. 谈不上……", size=34,
    items=["## 唯独: chỉ riêng, duy chỉ – loại trừ mọi người, mọi vật khác",
           "初审时同等优秀条件下唯独筛除女性的简历，连笔试和面试的机会都谈不上。",
           "全班同学都在认真听讲，唯独他在睡觉。",
           "他什么都不在乎，唯独受不了家人的误解。",
           "## 谈不上: chưa đạt đến mức (cao, tốt, sâu như vậy), chưa thể gọi là",
           "他只是一个普普通通的足球爱好者而已，还谈不上是专业球迷。",
           "我和他只是萍水相逢，谈不上感情深厚。"],
    say=["Tiếp theo là 唯独 và 谈不上.",
         F(0, "唯独 là phó từ, nghĩa là chỉ riêng, duy chỉ, loại trừ mọi người, mọi vật khác. Thường dùng sau một vế nói về tất cả, để nêu ra một trường hợp khác biệt."),
         F(1, "Ví dụ từ bài khóa: 初审时同等优秀条件下唯独筛除女性的简历，连笔试和面试的机会都谈不上。"),
         F(2, "全班同学都在认真听讲，唯独他在睡觉。 Cả lớp đều chăm chú nghe giảng, chỉ riêng cậu ấy đang ngủ."),
         F(3, "他什么都不在乎，唯独受不了家人的误解。 Anh ấy chẳng bận tâm điều gì, chỉ riêng không chịu nổi sự hiểu lầm của gia đình."),
         F(4, "谈不上 nghĩa là chưa đạt tới mức độ nào đó, chưa thể nói là, thường dùng để nói khiêm tốn hoặc phủ nhận nhẹ nhàng. Câu trong bài khóa vừa rồi cũng có 谈不上."),
         F(5, "他只是一个普普通通的足球爱好者而已，还谈不上是专业球迷。 Anh ấy chỉ là một người yêu bóng đá bình thường mà thôi, còn chưa thể gọi là cổ động viên chuyên nghiệp."),
         F(6, "我和他只是萍水相逢，谈不上感情深厚。 Tôi với anh ấy chỉ là bèo nước gặp nhau, chưa thể nói là tình cảm sâu đậm. 萍水相逢 là bèo nước gặp nhau, tình cờ quen biết.")])

add("bullets", section="Mẫu câu 重点句型", title="7. 哪怕……也…… · 8. 别的不说……", size=34,
    items=["## 哪怕……也……: cho dù… cũng… (nhượng bộ, = 即使 / 就算)",
           "哪怕成功入职，女性也被职场性骚扰等问题所困扰。",
           "如果我下定决心，哪怕困难重重，也要坚持到底。",
           "哪怕他有再大的本事，一个人也完成不了这个项目。",
           "## 别的不说: chưa nói gì khác – gạt các việc khác sang bên, chỉ nêu một việc tiêu biểu",
           "我在你们家干的活也太多了，别的不说，光买菜做饭就够忙一阵儿的了。",
           "他准是一位资深厨师，别的不说，光看他切菜的熟练程度就知道了。"],
    say=["Hai điểm cuối là 哪怕也 và 别的不说.",
         F(0, "哪怕，也 nghĩa là cho dù, cũng, là liên từ nhượng bộ, giống 即使 và 就算, mang màu khẩu ngữ hơn."),
         F(1, "Ví dụ từ bài khóa: 哪怕成功入职，女性也被职场性骚扰等问题所困扰。 Cho dù vào làm thành công, phụ nữ vẫn bị những vấn đề như quấy rối tình dục làm phiền."),
         F(2, "如果我下定决心，哪怕困难重重，也要坚持到底。 Nếu tôi đã quyết tâm, thì cho dù khó khăn chồng chất, cũng phải kiên trì đến cùng."),
         F(3, "哪怕他有再大的本事，一个人也完成不了这个项目。 Cho dù anh ấy có giỏi đến mấy, một mình cũng không hoàn thành nổi dự án này."),
         F(4, "别的不说 nghĩa là chưa nói gì khác, gạt mọi chuyện khác sang một bên, chỉ nêu một việc tiêu biểu để chứng minh. Phía sau thường có 光 hoặc 单是, nghĩa là chỉ riêng."),
         F(5, "Ví dụ: 我在你们家干的活也太多了，别的不说，光买菜做饭就够忙一阵儿的了。 Việc tôi làm ở nhà các người nhiều quá rồi, chưa nói gì khác, chỉ riêng đi chợ nấu cơm đã đủ bận một hồi."),
         F(6, "他准是一位资深厨师，别的不说，光看他切菜的熟练程度就知道了。 Ông ấy chắc chắn là một đầu bếp lâu năm, chưa nói gì khác, chỉ cần nhìn độ thành thạo khi thái rau là biết. Trong bài khóa: 别的不说，在打扫做饭这些家庭琐事上，女性平均投入了男性两倍或以上的时长.")])

# ======================= KẾT HỢP TỪ & THÀNH NGỮ =======================
add("bullets", chapter="Kết hợp từ 词语搭配", section="Kết hợp từ 词语搭配", title="Kết hợp từ: 庞大 · 同等 · 轮流 · 缴纳 · 塑造", size=32,
    items=["## 庞大: 规模～ · 数量～ · 队伍～ · 体型～ · 显得～",
           "在这部科幻电影中，人类面对数量庞大的机器人，显得渺小而无力。",
           "## 同等: ～权利 · ～待遇 · ～学力",
           "根据《民法典》，非婚生子女与婚生子女享有同等的权利。",
           "## 轮流: ～值班 · ～陪伴 · ～上阵 · ～看守",
           "他生病住院时，同学们轮流帮他补课。",
           "## 缴纳: 按时～ · 延期～ · ～学费 · ～税费 · ～保证金",
           "学校要求学生按时缴纳学费。",
           "## 塑造: ～形象 · ～人物 · ～品牌 · 精心～ · 大力～",
           "朋友圈成了一些人塑造个人形象的舞台。"],
    say=["Tiếp theo là phần kết hợp từ, gồm năm từ.",
         F(0, "庞大 đi với 规模，数量，队伍，体型: quy mô khổng lồ, số lượng khổng lồ, đội ngũ đông đảo, thân hình đồ sộ; và 显得庞大, trông đồ sộ."),
         F(1, "Ví dụ: 在这部科幻电影中，人类面对数量庞大的机器人，显得渺小而无力。 Trong bộ phim khoa học viễn tưởng này, con người trước số lượng robot khổng lồ trở nên nhỏ bé và bất lực."),
         F(2, "同等 đi với 权利，待遇，学力: quyền lợi ngang nhau, đãi ngộ ngang nhau, và 同等学力, trình độ tương đương, tức là chưa học đại học nhưng có trình độ tương đương tốt nghiệp đại học."),
         F(3, "Ví dụ: 根据民法典，非婚生子女与婚生子女享有同等的权利。 Theo Bộ luật Dân sự, con ngoài giá thú và con trong giá thú có quyền như nhau."),
         F(4, "轮流 đi với 值班, trực ban; 陪伴, ở bên; 上阵, ra trận; 看守, canh giữ. Ví dụ: 他生病住院时，同学们轮流帮他补课。 Khi cậu ấy ốm nằm viện, các bạn thay phiên nhau giảng bài bù cho cậu ấy."),
         F(6, "缴纳 đi với 按时缴纳, nộp đúng hạn; 延期缴纳, nộp chậm; và 学费，税费，保证金: học phí, thuế phí, tiền đặt cọc bảo đảm. Ví dụ: 学校要求学生按时缴纳学费。 Nhà trường yêu cầu học sinh nộp học phí đúng hạn."),
         F(8, "塑造 đi với 形象，人物，品牌: xây dựng hình tượng, nhân vật, thương hiệu; và 精心塑造, dày công xây dựng; 大力塑造, ra sức xây dựng."),
         F(9, "Ví dụ: 朋友圈成了一些人塑造个人形象的舞台。 Vòng bạn bè WeChat đã trở thành sân khấu để một số người xây dựng hình ảnh cá nhân. Giống như Facebook ở Việt Nam vậy.")])

add("bullets", chapter="Thành ngữ (21 thành ngữ)", section="Thành ngữ 成语与惯用语", title="Thành ngữ (1): 风口浪尖 · 无可奈何 · 功成名就 · 乘风破浪", size=33,
    items=["## 风口浪尖 fēngkǒu-làngjiān – đầu sóng ngọn gió: tâm điểm tranh cãi, chú ý",
           "他在舆论的风口浪尖上能够如此镇定，让人十分钦佩。",
           "## 无可奈何 wúkěnàihé – đành chịu, không còn cách nào",
           "她争执一番后，无可奈何地缴纳了罚金。",
           "## 功成名就 gōngchéng-míngjiù – công thành danh toại",
           "他苦干了几十年，终于功成名就。",
           "## 乘风破浪 chéngfēng-pòlàng – thuận gió rẽ sóng: vượt khó, dũng cảm tiến lên",
           "愿您毕业后乘风破浪，干出一番事业，对社会有所贡献。"],
    say=["Bài này có hai mươi mốt thành ngữ và quán dụng ngữ, nhiều nhất trong cả đơn vị. Chúng ta học mỗi lần ba đến bốn thành ngữ.",
         F(0, "风口浪尖: chỗ gió to sóng lớn, nghĩa gốc ví với nơi tiền tuyến của cuộc đấu tranh gay gắt; nay hay dùng để chỉ tâm điểm của dư luận, của tranh cãi. Tiếng Việt có câu tương tự: đầu sóng ngọn gió."),
         F(1, "Ví dụ: 他在舆论的风口浪尖上能够如此镇定，让人十分钦佩。 Đứng giữa tâm bão dư luận mà anh ấy vẫn bình tĩnh như vậy, khiến người ta rất khâm phục."),
         F(2, "无可奈何: không có cách nào khác, đành chịu vậy."),
         F(3, "Ví dụ: 她争执一番后，无可奈何地缴纳了罚金。 Sau một hồi tranh cãi, cô ấy đành ngậm ngùi nộp tiền phạt."),
         F(4, "功成名就: 功 là công trạng, 就 là đạt được. Công trạng đã có, danh tiếng cũng có, giống câu công thành danh toại của tiếng Việt."),
         F(5, "Ví dụ: 他苦干了几十年，终于功成名就。 Ông ấy làm lụng vất vả mấy chục năm, cuối cùng đã công thành danh toại."),
         F(6, "乘风破浪: thuyền thuận theo sức gió mà rẽ sóng tiến lên, ví với vượt qua khó khăn, hăng hái tiến lên. Đây chính là thành ngữ trong tên bài."),
         F(7, "Ví dụ: 愿您毕业后乘风破浪，干出一番事业，对社会有所贡献。 Chúc bạn sau khi tốt nghiệp sẽ vượt sóng tiến lên, làm nên sự nghiệp, có đóng góp cho xã hội.")])

add("bullets", section="Thành ngữ 成语与惯用语", title="Thành ngữ (2): 轻而易举 · 腹背受敌 · 远近闻名 · 位居前列", size=33,
    items=["## 轻而易举 qīng'éryìjǔ – nhẹ nhàng dễ dàng, chẳng tốn sức",
           "他真是个大力士，轻而易举地搬走了一块巨大的石头。",
           "## 腹背受敌 fùbèi-shòudí – bị đánh cả trước lẫn sau",
           "前有围堵，后有追兵，我们已经腹背受敌，该如何是好？",
           "## 远近闻名 yuǎnjìn-wénmíng – xa gần đều biết tiếng, rất nổi tiếng",
           "以前，我的家乡没通水、没通电，而如今已发展成远近闻名的富裕村了。",
           "## 位居前列 wèijū-qiánliè – đứng ở hàng đầu, dẫn đầu",
           "本季度，该省份的GDP增速在全国范围内位居前列。"],
    say=[F(0, "轻而易举: 举 là nhấc lên. Nhẹ đến mức dễ dàng nhấc lên được, ý nói việc rất dễ làm, chẳng tốn sức."),
         F(1, "Ví dụ: 他真是个大力士，轻而易举地搬走了一块巨大的石头。 Anh ấy đúng là lực sĩ, dễ dàng bê đi một tảng đá khổng lồ."),
         F(2, "腹背受敌: 腹 là bụng, chỉ phía trước; 背 là lưng, chỉ phía sau. Phía trước, phía sau đều bị kẻ địch tấn công."),
         F(3, "Ví dụ: 前有围堵，后有追兵，我们已经腹背受敌，该如何是好？ Phía trước bị chặn, phía sau có quân đuổi, chúng ta đã bị kẹp cả hai đầu, biết làm sao bây giờ?"),
         F(4, "远近闻名: dù ở xa hay ở gần đều nghe tiếng, ý nói rất nổi tiếng."),
         F(5, "Ví dụ: 以前，我的家乡没通水、没通电，而如今已发展成远近闻名的富裕村了。 Trước kia quê tôi không có nước máy, không có điện, mà nay đã thành ngôi làng giàu có nổi tiếng khắp vùng."),
         F(6, "位居前列: thứ hạng ở hàng đầu, ví với vị trí dẫn đầu."),
         F(7, "Ví dụ: 本季度，该省份的GDP增速在全国范围内位居前列。 Quý này, tốc độ tăng trưởng GDP của tỉnh đó đứng hàng đầu cả nước.")])

add("bullets", section="Thành ngữ 成语与惯用语", title="Thành ngữ (3): 遥遥领先 · 分身乏术 · 家常便饭 · 刨根问底", size=33,
    items=["## 遥遥领先 yáoyáo-lǐngxiān – bỏ xa phía sau, dẫn đầu cách biệt",
           "他不愧是我们团队中最有能力的人，这个月的销售业绩遥遥领先。",
           "## 分身乏术 fēnshēn-fáshù – không có phép phân thân: bận đến mức không lo xuể",
           "为了能兼顾功课和社团活动，现在的我已是分身乏术了。",
           "## 家常便饭 jiācháng-biànfàn – cơm nhà bữa thường: chuyện thường ngày, cơm bữa",
           "他工作太忙了，加班熬夜是家常便饭。",
           "## 刨根问底 páogēn-wèndǐ – đào tận gốc, hỏi tận đáy: truy hỏi đến cùng",
           "对于不懂的问题，我们一定要刨根问底搞清楚。"],
    say=[F(0, "遥遥领先: 遥遥 là xa tít. Đi trước rất xa, dẫn đầu cách biệt."),
         F(1, "Ví dụ: 他不愧是我们团队中最有能力的人，这个月的销售业绩遥遥领先。 Anh ấy không hổ là người giỏi nhất nhóm chúng tôi, doanh số tháng này dẫn đầu cách biệt."),
         F(2, "分身乏术: 分身 là phân thân, 乏术 là không có cách. Không có phép phân thân, ý nói quá bận, không thể cùng lúc làm nhiều việc."),
         F(3, "Ví dụ: 为了能兼顾功课和社团活动，现在的我已是分身乏术了。 Để lo được cả bài vở lẫn hoạt động câu lạc bộ, giờ tôi bận đến mức không xoay xở nổi."),
         F(4, "家常便饭: bữa cơm thường ngày trong nhà, ví với chuyện xảy ra thường xuyên, rất bình thường, giống câu chuyện cơm bữa của tiếng Việt."),
         F(5, "Ví dụ: 他工作太忙了，加班熬夜是家常便饭。 Anh ấy bận việc quá, tăng ca thức khuya là chuyện cơm bữa. Câu này nhắc lại chủ đề bài sáu chấm một."),
         F(6, "刨根问底: chữ đầu đọc páo, là đào bới. Đào đến tận gốc, hỏi đến tận đáy, tức là truy hỏi cho đến cùng."),
         F(7, "Ví dụ: 对于不懂的问题，我们一定要刨根问底搞清楚。 Với những vấn đề chưa hiểu, chúng ta nhất định phải hỏi cho ra lẽ.")])

add("bullets", section="Thành ngữ 成语与惯用语", title="Thành ngữ (4): 雪上加霜 · 司空见惯 · 长此以往", size=34,
    items=["## 雪上加霜 xuěshàng-jiāshuāng – trên tuyết thêm sương: họa vô đơn chí",
           "今年收成本来就不好，又遇到蝗灾，这无疑是雪上加霜。",
           "## 司空见惯 sīkōng-jiànguàn – quá quen thuộc, chẳng có gì lạ",
           "对现在的年轻人，失恋分手已是司空见惯的事情。",
           "## 长此以往 chángcǐ-yǐwǎng – cứ kéo dài mãi như thế",
           "有的孩子不吃早饭，长此以往，有损身体健康。",
           "这样近距离地看书，长此以往，非成近视眼不可。"],
    say=[F(0, "雪上加霜: trên tuyết lại phủ thêm sương giá, ví với liên tiếp gặp tai họa, thiệt hại càng thêm nặng nề. Giống câu họa vô đơn chí, hay đã nghèo lại gặp cái eo."),
         F(1, "Ví dụ: 今年收成本来就不好，又遇到蝗灾，这无疑是雪上加霜。 Năm nay mùa màng vốn đã kém, lại gặp nạn châu chấu, đúng là họa vô đơn chí."),
         F(2, "司空见惯: 司空 là một chức quan thời xưa. Tương truyền nhà thơ Lưu Vũ Tích được một vị quan tư không mời dự tiệc có ca kỹ, ông thấy lạ, nhưng vị quan thì đã thấy mãi thành quen. Nay chỉ chuyện thường thấy, chẳng có gì lạ."),
         F(3, "Ví dụ: 对现在的年轻人，失恋分手已是司空见惯的事情。 Với giới trẻ bây giờ, thất tình chia tay đã là chuyện quá bình thường."),
         F(4, "长此以往: chữ đầu đọc cháng. Cứ lâu dài như thế mãi, thường dẫn ra một hậu quả xấu."),
         F(5, "Ví dụ: 有的孩子不吃早饭，长此以往，有损身体健康。 Có những đứa trẻ không ăn sáng, cứ kéo dài như vậy sẽ hại sức khỏe."),
         F(6, "Và: 这样近距离地看书，长此以往，非成近视眼不可。 Đọc sách gần thế này, cứ mãi như vậy thì không cận thị mới lạ. 非，不可 là nhất định sẽ.")])

add("bullets", section="Thành ngữ 成语与惯用语", title="Thành ngữ (5): 毋庸置疑 · 焦头烂额 · 鸡毛蒜皮", size=34,
    items=["## 毋庸置疑 wúyōng-zhìyí – không cần nghi ngờ, chắc chắn",
           "毋庸置疑，抽烟喝酒有害健康。",
           "想要学好一门语言，一定要勤学苦练，这是毋庸置疑的。",
           "## 焦头烂额 jiāotóu-làn'é – cháy đầu bỏng trán: bận rộn, rối bời",
           "最近为了搬家的事，忙得我焦头烂额。",
           "## 鸡毛蒜皮 jīmáo-suànpí – lông gà vỏ tỏi: chuyện vụn vặt không đáng kể",
           "这种鸡毛蒜皮的小事，我们最好不要斤斤计较。"],
    say=[F(0, "毋庸置疑: 毋庸 là không cần, 置疑 là đặt nghi vấn. Không cần phải nghi ngờ, điều hiển nhiên."),
         F(1, "Ví dụ: 毋庸置疑，抽烟喝酒有害健康。 Không cần bàn cãi, hút thuốc uống rượu có hại cho sức khỏe."),
         F(2, "Và: 想要学好一门语言，一定要勤学苦练，这是毋庸置疑的。 Muốn học giỏi một ngoại ngữ thì nhất định phải chăm học khổ luyện, điều này là chắc chắn."),
         F(3, "焦头烂额: đầu cháy, trán bỏng, vốn chỉ người bị thương khi chữa cháy; nay ví với công việc, cuộc sống bận rộn, rối như canh hẹ."),
         F(4, "Ví dụ: 最近为了搬家的事，忙得我焦头烂额。 Dạo này vì chuyện chuyển nhà mà tôi bận tối mắt tối mũi."),
         F(5, "鸡毛蒜皮: lông gà và vỏ tỏi, ví với những chuyện vụn vặt không quan trọng."),
         F(6, "Ví dụ: 这种鸡毛蒜皮的小事，我们最好不要斤斤计较。 Những chuyện vặt vãnh như thế này, chúng ta tốt nhất đừng so đo tính toán. 斤斤计较 là so đo từng li từng tí.")])

add("bullets", section="Thành ngữ 成语与惯用语", title="Thành ngữ (6): 里里外外一把手 · 相夫教子 · 披荆斩棘", size=34,
    items=["## 里里外外一把手 – việc trong việc ngoài đều một tay đảm đương",
           "二嫂生意做得好，又把生病多年的母亲照顾得很周到，真是里里外外一把手。",
           "## 相夫教子 xiàngfū-jiàozǐ – giúp chồng, dạy con",
           "多年在家相夫教子的全职妈妈要重返职场不是一件容易的事儿。",
           "## 披荆斩棘 pījīng-zhǎnjí – vạch gai mở lối: vượt qua muôn vàn trở ngại",
           "他白手起家，多年来在商场上披荆斩棘，终于有了今日的成就。"],
    say=[F(0, "里里外外一把手: việc trong nhà lẫn việc bên ngoài đều do một người lo liệu giỏi giang, rất giống câu giỏi việc nước, đảm việc nhà của Việt Nam."),
         F(1, "Ví dụ: 二嫂生意做得好，又把生病多年的母亲照顾得很周到，真是里里外外一把手。 Chị dâu thứ hai buôn bán giỏi, lại chăm sóc người mẹ ốm nhiều năm rất chu đáo, đúng là giỏi việc ngoài, đảm việc trong."),
         F(2, "相夫教子: chữ đầu đọc xiàng, nghĩa là giúp đỡ; 教子 là dạy con. Nghĩa là ở nhà giúp chồng, dạy con, hình mẫu người phụ nữ truyền thống."),
         F(3, "Ví dụ: 多年在家相夫教子的全职妈妈要重返职场不是一件容易的事儿。 Một bà mẹ nội trợ nhiều năm ở nhà chăm chồng dạy con muốn quay lại công sở không phải chuyện dễ."),
         F(4, "披荆斩棘: 披 là vạch ra, 荆 là bụi gai, 斩 là chặt, 棘 là cây có gai. Vạch bụi gai, chặt cây gai mà đi, ví với vượt qua muôn vàn khó khăn trên con đường lập nghiệp."),
         F(5, "Ví dụ: 他白手起家，多年来在商场上披荆斩棘，终于有了今日的成就。 Anh ấy tay trắng lập nghiệp, nhiều năm vượt qua bao chông gai trên thương trường, cuối cùng có được thành tựu ngày hôm nay. 白手起家 là tay trắng làm nên.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 课后练习", title="Bài tập 1: Chọn từ điền vào chỗ trống (1)", reveal=True, size=34,
    items=["## 刨根问底 · 缩影 · 风口浪尖 · 毋庸置疑 · 功成名就 · 雪上加霜 · 承担",
           "(1) 科学频道的电视就是以___的方式来解读世界上奇异现象的奥秘。",
           "Đáp án: 刨根问底",
           "(2) 对于___的人，我们应该看到他们在成功背后的付出。",
           "Đáp án: 功成名就",
           "(3) 他提出了这么敏感的问题，相当于把自己推到了舆论场的___。",
           "Đáp án: 风口浪尖",
           "(4) 《红楼梦》中的贾府是日趋没落的中国封建社会的___。",
           "Đáp án: 缩影"],
    say=["Bây giờ chúng ta sang phần luyện tập của sách. Bài tập một: chọn từ thích hợp điền vào chỗ trống. Có bảy lựa chọn: 刨根问底，缩影，风口浪尖，毋庸置疑，功成名就，雪上加霜，承担.",
         F(1, "Câu một: 科学频道的电视就是以什么的方式来解读世界上奇异现象的奥秘。 Kênh truyền hình khoa học dùng cách thế nào để giải mã bí ẩn của những hiện tượng kỳ lạ trên thế giới? Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 刨根问底. 以刨根问底的方式, bằng cách truy hỏi đến tận cùng."),
         F(3, "Câu hai: 对于什么的人，我们应该看到他们在成功背后的付出。 Với những người thế nào, chúng ta nên thấy sự hy sinh đằng sau thành công của họ?"),
         F(4, "Đáp án: 功成名就. Người công thành danh toại."),
         F(5, "Câu ba: 他提出了这么敏感的问题，相当于把自己推到了舆论场的什么。 Anh ta nêu ra vấn đề nhạy cảm như vậy, chẳng khác nào tự đẩy mình ra đâu của dư luận?"),
         F(6, "Đáp án: 风口浪尖. 推到风口浪尖, đẩy ra đầu sóng ngọn gió."),
         F(7, "Câu bốn: 红楼梦中的贾府是日趋没落的中国封建社会的什么。 Phủ họ Giả trong Hồng lâu mộng là gì của xã hội phong kiến Trung Quốc đang ngày càng suy tàn?"),
         F(8, "Đáp án: 缩影, hình ảnh thu nhỏ. Cả một xã hội được thu nhỏ trong một gia tộc.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 1: Chọn từ điền vào chỗ trống (2)", reveal=True, size=34,
    items=["(5) 洪灾刚过又发生了地震，对于这个国家来说，无异于___。",
           "Đáp án: 雪上加霜",
           "(6) 这件事的责任应该是由你___，可是你却嫁祸于人，这样做是多么的可耻。",
           "Đáp án: 承担",
           "(7) 人生成败取决于发奋与否，这点___，但所谓“谋事在人成事在天”，也不无道理。",
           "Đáp án: 毋庸置疑"],
    say=[F(0, "Câu năm: 洪灾刚过又发生了地震，对于这个国家来说，无异于什么。 Lũ lụt vừa qua lại xảy ra động đất, đối với đất nước này chẳng khác gì cái gì?"),
         F(1, "Đáp án: 雪上加霜. Thiên tai nối tiếp thiên tai, đúng là họa vô đơn chí. 无异于 là chẳng khác gì."),
         F(2, "Câu sáu: 这件事的责任应该是由你什么，可是你却嫁祸于人，这样做是多么的可耻。 Trách nhiệm việc này lẽ ra do cậu làm gì, vậy mà cậu lại đổ vạ cho người khác, thật đáng xấu hổ."),
         F(3, "Đáp án: 承担. 承担责任, gánh vác trách nhiệm. 嫁祸于人 là đổ vạ cho người khác."),
         F(4, "Câu bảy: 人生成败取决于发奋与否，这点什么，但所谓谋事在人成事在天，也不无道理。 Thành bại của đời người phụ thuộc vào việc có nỗ lực hay không, điểm này thế nào; nhưng câu mưu sự tại nhân, thành sự tại thiên cũng không phải không có lý."),
         F(5, "Đáp án: 毋庸置疑. Điểm này không cần nghi ngờ. Các bạn chú ý, ở câu năm, sách in là 这个的国家, thầy đã bỏ chữ 的 thừa cho đúng ngữ pháp.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn từ đúng hoàn thành câu (1)", reveal=True, size=34,
    items=["(1) 他家因父亲失业，生活已陷入___。 A.窘态 B.窘境 C.窘迫 D.窘相",
           "Đáp án: B 窘境 – 陷入窘境: rơi vào cảnh khốn quẫn",
           "(2) 要赶超世界___水平，我们还得快马加鞭。 A.遥遥领先 B.一马当先 C.先进 D.抢先",
           "Đáp án: C 先进 – 世界先进水平: trình độ tiên tiến thế giới",
           "(3) 我今天非要___，把这件事弄他个一清二楚。 A.刨根问底 B.知根知底 C.问长问短 D.归根结底",
           "Đáp án: A 刨根问底 – truy hỏi đến cùng"],
    say=["Bài tập hai: chọn từ đúng để hoàn thành câu.",
         F(0, "Câu một: 他家因父亲失业，生活已陷入什么。 Vì bố mất việc, cuộc sống nhà anh ấy đã rơi vào gì? A, 窘态; B, 窘境; C, 窘迫; D, 窘相."),
         F(1, "Đáp án: B, 窘境. 陷入 phải đi với danh từ chỉ hoàn cảnh: 陷入窘境. 窘态 và 窘相 là dáng vẻ lúng túng; 窘迫 là tính từ, khốn quẫn, không làm tân ngữ của 陷入 được."),
         F(2, "Câu hai: 要赶超世界什么水平，我们还得快马加鞭。 Muốn đuổi kịp và vượt trình độ gì của thế giới, chúng ta còn phải tăng tốc. A, 遥遥领先; B, 一马当先; C, 先进; D, 抢先."),
         F(3, "Đáp án: C, 先进. 世界先进水平 là trình độ tiên tiến thế giới, cụm cố định. Đã muốn đuổi kịp thì trình độ ấy không thể là của mình đang dẫn đầu. 快马加鞭 là ngựa nhanh còn quất thêm roi, tức tăng tốc hơn nữa."),
         F(4, "Câu ba: 我今天非要什么，把这件事弄他个一清二楚。 Hôm nay tôi nhất định phải làm gì, làm cho việc này rõ ràng ra lẽ. A, 刨根问底; B, 知根知底; C, 问长问短; D, 归根结底."),
         F(5, "Đáp án: A, 刨根问底, truy hỏi đến cùng. 知根知底 là biết rõ gốc gác; 问长问短 là hỏi han đủ thứ, tỏ ý quan tâm; 归根结底 là suy cho cùng.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn từ đúng hoàn thành câu (2)", reveal=True, size=34,
    items=["(4) 他从小就不是一个安份守己的人，从小学开始，逃课打架那是___。 A.不以为然 B.家常炒菜 C.少见多怪 D.家常便饭",
           "Đáp án: D 家常便饭 – chuyện cơm bữa",
           "(5) 对于他的人品操守，___，绝对信得过。 A.难以置信 B.半信半疑 C.毋庸置疑 D.深信不疑",
           "Đáp án: C 毋庸置疑 – không cần nghi ngờ"],
    say=[F(0, "Câu bốn: 他从小就不是一个安份守己的人，从小学开始，逃课打架那是什么。 Từ nhỏ cậu ta đã không phải người an phận, từ tiểu học đã trốn học đánh nhau như là gì? A, 不以为然; B, 家常炒菜; C, 少见多怪; D, 家常便饭."),
         F(1, "Đáp án: D, 家常便饭, chuyện cơm bữa. 家常炒菜 là món xào thường ngày, là đáp án gây nhiễu; 不以为然 là không cho là đúng; 少见多怪 là ít thấy nên lấy làm lạ."),
         F(2, "Câu năm: 对于他的人品操守，什么，绝对信得过。 Về nhân cách và phẩm hạnh của anh ấy thì thế nào, hoàn toàn có thể tin được. A, 难以置信; B, 半信半疑; C, 毋庸置疑; D, 深信不疑."),
         F(3, "Đáp án: C, 毋庸置疑, không cần nghi ngờ. 难以置信 là khó tin, 半信半疑 là bán tín bán nghi, đều trái với 绝对信得过. Còn 深信不疑 cần có chủ ngữ là người tin, như 我对他深信不疑.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ ngữ, mẫu câu cho sẵn trả lời câu hỏi", reveal=True, size=32,
    items=["(1) 在你看来，30+的职场女性所面临的困境是什么？（令人……的是/让人……的是）",
           "Đáp án gợi ý: 令人无奈的是，30+的女性正处于事业的黄金阶段，却恰好撞上婚育高峰期，常常要在家庭和事业之间艰难地平衡。",
           "(2) 对职场女性来说，为什么家庭和工作的矛盾是难以调和的？（即便是……也……）",
           "Đáp án gợi ý: 因为即便是在双职工家庭，女性也要承担大部分家务和育儿重担，很难兼顾事业。",
           "(3) 刚入职场之时，对于女性是否公平？（谈不上……）",
           "Đáp án gợi ý: 谈不上公平。有的公司只招男性，有的在初审时唯独筛除女性的简历，女性连面试的机会都没有。",
           "(4) 男性和女性在家庭中的分工是怎样的？（别的不说……）",
           "Đáp án gợi ý: 传统上是“男主外女主内”。别的不说，光是做饭、接送孩子，女性投入的时间就是男性的两倍以上。"],
    say=["Bài tập ba: dùng từ ngữ và mẫu câu cho sẵn để trả lời câu hỏi. Đây là câu hỏi mở, thầy đưa ra đáp án gợi ý dựa theo bài khóa.",
         F(0, "Câu một: 在你看来，三十加的职场女性所面临的困境是什么？ Theo bạn, phụ nữ đi làm ngoài ba mươi tuổi đang đối mặt với khó khăn gì? Dùng 令人的是."),
         F(1, "Gợi ý: 令人无奈的是，三十加的女性正处于事业的黄金阶段，却恰好撞上婚育高峰期，常常要在家庭和事业之间艰难地平衡。"),
         F(2, "Câu hai: 对职场女性来说，为什么家庭和工作的矛盾是难以调和的？ Với phụ nữ đi làm, vì sao mâu thuẫn giữa gia đình và công việc lại khó dung hòa? Dùng 即便是也."),
         F(3, "Gợi ý: 因为即便是在双职工家庭，女性也要承担大部分家务和育儿重担，很难兼顾事业。 Vì cho dù trong gia đình cả hai vợ chồng đi làm, phụ nữ vẫn phải gánh phần lớn việc nhà và nuôi con, rất khó lo trọn sự nghiệp."),
         F(4, "Câu ba: 刚入职场之时，对于女性是否公平？ Khi mới bước vào công sở, có công bằng với phụ nữ không? Dùng 谈不上."),
         F(5, "Gợi ý: 谈不上公平。有的公司只招男性，有的在初审时唯独筛除女性的简历，女性连面试的机会都没有。"),
         F(6, "Câu bốn: 男性和女性在家庭中的分工是怎样的？ Nam và nữ phân công việc nhà như thế nào? Dùng 别的不说."),
         F(7, "Gợi ý: 传统上是男主外女主内。别的不说，光是做饭、接送孩子，女性投入的时间就是男性的两倍以上。")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Chọn từ ngữ, thành ngữ điền vào đoạn văn", reveal=True, size=32,
    items=["## 披荆斩棘 · 调和 · 轮流 · 夹缝 · 焦头烂额 · 着实 · 洒脱 · 琐事 · 鸡毛蒜皮",
           "对于中国职场女性而言，工作与家庭这对难以___的矛盾，让她们有些分身乏术。职场中，她们在婚育阶段常常被迫调岗减薪，女同事间则需要排好计划表“___”怀孕，直至为照顾孩子和家庭而不得不放弃事业发展。家庭中，在“男主外女主内”的传统思想影响下，双职工家庭的女性不仅要面临职场的___，还要承担家庭的___。在打扫做饭、陪伴孩子和接送孩子辅导学习这些所谓家庭___上，女性平均投入了男性两倍或以上的时长。总之，女性在家庭和职场的___中生存，她们的生活，远不能___地“乘风破浪”，倒蛮像是艰难地“___”。",
           "Đáp án: 调和 · 轮流 · 焦头烂额 · 鸡毛蒜皮 · 琐事 · 夹缝 · 洒脱 · 披荆斩棘 (thừa: 着实)"],
    say=["Bài tập bốn: chọn từ ngữ, thành ngữ điền vào đoạn văn. Có chín lựa chọn cho tám chỗ trống: 披荆斩棘，调和，轮流，夹缝，焦头烂额，着实，洒脱，琐事，鸡毛蒜皮.",
         F(1, "对于中国职场女性而言，工作与家庭这对难以什么的矛盾，让她们有些分身乏术。职场中，她们在婚育阶段常常被迫调岗减薪，女同事间则需要排好计划表什么怀孕，直至为照顾孩子和家庭而不得不放弃事业发展。"),
         F(1, "家庭中，在男主外女主内的传统思想影响下，双职工家庭的女性不仅要面临职场的什么，还要承担家庭的什么。在打扫做饭、陪伴孩子和接送孩子辅导学习这些所谓家庭什么上，女性平均投入了男性两倍或以上的时长。总之，女性在家庭和职场的什么中生存，她们的生活，远不能什么地乘风破浪，倒蛮像是艰难地什么。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 难以调和；轮流怀孕；职场的焦头烂额；家庭的鸡毛蒜皮；家庭琐事；夹缝中生存；洒脱地乘风破浪；艰难地披荆斩棘. Từ thừa là 着实."),
         F(2, "Mẹo: 焦头烂额 và 鸡毛蒜皮 đi thành cặp, một bên là công sở rối bời, một bên là việc nhà vụn vặt. Còn 琐事 đứng sau 家庭 tạo thành 家庭琐事. Đoạn văn này chính là bản tóm tắt nửa sau của bài khóa, hãy đọc to vài lần nhé.")])

# ======================= THẢO LUẬN =======================
add("bullets", chapter="Thảo luận: phụ nữ đi làm ở Việt Nam", section="Thảo luận 讨论", title="Thảo luận: phụ nữ đi làm ở Việt Nam", reveal=True, size=33,
    items=["(1) 越南职场女性也会遇到文中提到的问题吗？",
           "Đáp án gợi ý: 也会遇到。比如面试时被问到结婚和生孩子的计划。不过，越南法律规定产假为六个月，也禁止性别歧视。",
           "(2) 越南有没有类似“里里外外一把手”的说法？",
           "Đáp án gợi ý: 有。越南人常说女性要“giỏi việc nước, đảm việc nhà”，意思是工作出色，家务也做得好。",
           "(3) 你认为怎样才能帮助职场女性“乘风破浪”？",
           "Đáp án gợi ý: 我认为丈夫要分担家务和育儿，企业不能歧视女性，国家也应该延长男性的陪产假。"],
    say=["Chúng ta cùng thảo luận, liên hệ với thực tế Việt Nam. Các bạn hãy thử trả lời bằng tiếng Trung trước khi nghe gợi ý.",
         F(0, "Câu một: 越南职场女性也会遇到文中提到的问题吗？ Phụ nữ đi làm ở Việt Nam có gặp những vấn đề như trong bài không?"),
         F(1, "Gợi ý: 也会遇到。比如面试时被问到结婚和生孩子的计划。不过，越南法律规定产假为六个月，也禁止性别歧视。 Cũng có. Ví dụ khi phỏng vấn bị hỏi về kế hoạch kết hôn, sinh con. Tuy nhiên, luật Việt Nam quy định nghỉ thai sản sáu tháng, và cấm phân biệt đối xử về giới. Tỉ lệ phụ nữ Việt Nam tham gia lao động cũng thuộc hàng cao trên thế giới."),
         F(2, "Câu hai: 越南有没有类似里里外外一把手的说法？ Việt Nam có cách nói nào giống 里里外外一把手 không?"),
         F(3, "Gợi ý: 有。越南人常说女性要giỏi việc nước, đảm việc nhà，意思是工作出色，家务也做得好。 Có. Người Việt hay nói phụ nữ phải giỏi việc nước, đảm việc nhà, nghĩa là làm việc xuất sắc, việc nhà cũng chu toàn. Lời khen này cũng chính là áp lực, giống như hình ảnh bà mẹ siêu nhân trong bài."),
         F(4, "Câu ba: 你认为怎样才能帮助职场女性乘风破浪？ Theo bạn, làm thế nào mới giúp được phụ nữ đi làm đạp gió rẽ sóng?"),
         F(5, "Gợi ý: 我认为丈夫要分担家务和育儿，企业不能歧视女性，国家也应该延长男性的陪产假。 Tôi cho rằng người chồng phải chia sẻ việc nhà và nuôi con, doanh nghiệp không được phân biệt đối xử với phụ nữ, nhà nước cũng nên kéo dài kỳ nghỉ chăm vợ sinh của nam giới. Ở Việt Nam, người chồng hiện được nghỉ từ năm đến mười bốn ngày làm việc khi vợ sinh con.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết bài 6.3", section="Tổng kết", title="Tổng kết bài 6.3", size=34,
    items=["Từ vựng trọng tâm: 窘境 · 缩影 · 庞大 · 倒逼 · 调和 · 着实 · 尚 · 应聘 · 歧视 · 隐性 · 唯独 · 谈不上 · 已然 · 晋升 · 裁员 · 缴纳 · 重担 · 琐事 · 塑造 · 夹缝 · 洒脱",
           "Mẫu câu: 令人/让人……的是 · 即便是……也（不）要…… · 当着 · 凡 · 唯独 · 谈不上 · 哪怕……也…… · 别的不说",
           "Thành ngữ: 风口浪尖 · 乘风破浪 · 腹背受敌 · 分身乏术 · 家常便饭 · 刨根问底 · 雪上加霜 · 司空见惯 · 焦头烂额 · 鸡毛蒜皮 · 披荆斩棘",
           "## Bài tập về nhà",
           "Viết đoạn văn khoảng 300 chữ: 越南的职场女性 – dùng ít nhất 3 mẫu câu và 3 thành ngữ của bài"],
    say=["Chúng ta cùng tổng kết bài sáu chấm ba.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 窘境，缩影，庞大，倒逼，调和，着实，尚，应聘，歧视，隐性，唯独，谈不上，已然，晋升，裁员，缴纳，重担，琐事，塑造，夹缝，洒脱. Nhớ cách đọc của 调和，着实，夹缝, và đừng nhầm 已然 với dĩ nhiên."),
         F(1, "Về mẫu câu: 令人的是 để đưa đánh giá lên trước; 即便是也 là cho dù cũng; 当着 là trước mặt; 凡 là phàm là; 唯独 là chỉ riêng; 谈不上 là chưa thể gọi là; 哪怕也 là cho dù cũng; và 别的不说 là chưa nói gì khác."),
         F(2, "Về thành ngữ: 风口浪尖，乘风破浪，腹背受敌，分身乏术，家常便饭，刨根问底，雪上加霜，司空见惯，焦头烂额，鸡毛蒜皮，披荆斩棘. Hãy tập dùng chúng thành từng cặp, như 焦头烂额 với 鸡毛蒜皮, hay 乘风破浪 với 披荆斩棘."),
         F(4, "Bài tập về nhà: hãy viết một đoạn văn khoảng ba trăm chữ về chủ đề 越南的职场女性, phụ nữ đi làm ở Việt Nam. Dùng ít nhất ba mẫu câu và ba thành ngữ của bài. Sau đây, chúng ta cùng ôn tập cả Đơn vị sáu.",
           cap="Bài tập về nhà: hãy viết một đoạn văn khoảng 300 chữ về chủ đề 越南的职场女性, phụ nữ đi làm ở Việt Nam. Dùng ít nhất 3 mẫu câu và 3 thành ngữ của bài. Sau đây, chúng ta cùng ôn tập cả Đơn vị 6.")])

# ======================= ÔN TẬP ĐƠN VỊ =======================
add("bullets", chapter="Ôn tập đơn vị 6", section="Ôn tập đơn vị 单元练习", title="Ôn tập Đơn vị 6 职场篇: nhìn lại ba bài", size=33,
    items=["## 6.1 职场 996: 两个症结 – 法律责任的缺位 · 文化价值的错位",
           "所谓……是指…… · 披着……的外衣 · 固然……但是…… · ……与……是两码事",
           "## 6.2 谁能站在新职业风口？: 新职业应运而生 · 以兴趣为导向",
           "一时间 · 渐成风气 · 呈现……态势 · 和……相去甚远 · 尤以……为最",
           "## 6.3 30 岁的职场姐姐: 腹背受敌 · 在家庭和职场的夹缝中生存",
           "令人……的是 · 即便是……也…… · 唯独 · 谈不上 · 别的不说"],
    say=["Bây giờ là chương ôn tập Đơn vị sáu. Phần này dựa theo mục 单元练习, với tiêu đề 学以致用, học để dùng, ở cuối đơn vị trong sách. Trước hết, chúng ta nhìn lại ba bài.",
         F(0, "Bài sáu chấm một, 职场九九六: chế độ làm việc chín giờ sáng đến chín giờ tối, sáu ngày một tuần ngày càng lan rộng vì hai nút thắt: pháp luật thiếu vắng trách nhiệm, và giá trị văn hóa lệch lạc.",
           cap="Bài 6.1, 职场 996: chế độ làm việc 9 giờ sáng đến 9 giờ tối, 6 ngày một tuần ngày càng lan rộng vì hai nút thắt: pháp luật thiếu vắng trách nhiệm, và giá trị văn hóa lệch lạc."),
         F(1, "Các mẫu câu tiêu biểu: 所谓是指，披着的外衣，固然但是, và 两码事."),
         F(2, "Bài sáu chấm hai: internet sinh ra hàng loạt nghề mới, giới trẻ lấy sở thích làm định hướng, nhưng vẫn phải vượt qua cửa ải bát cơm sắt của bố mẹ.",
           cap="Bài 6.2: internet sinh ra hàng loạt nghề mới, giới trẻ lấy sở thích làm định hướng, nhưng vẫn phải vượt qua cửa ải “bát cơm sắt” của bố mẹ."),
         F(3, "Các mẫu câu tiêu biểu: 一时间，渐成风气，呈现态势，相去甚远，尤以为最."),
         F(4, "Bài sáu chấm ba: phụ nữ ngoài ba mươi tuổi bị kẹp giữa công việc và gia đình, cuộc sống của họ là vạch gai mở lối chứ không phải đạp gió rẽ sóng.",
           cap="Bài 6.3: phụ nữ ngoài 30 tuổi bị kẹp giữa công việc và gia đình, cuộc sống của họ là “vạch gai mở lối” chứ không phải “đạp gió rẽ sóng”."),
         F(5, "Các mẫu câu tiêu biểu: 令人的是，即便是也，唯独，谈不上，别的不说. Ba bài cùng một chủ đề: con người và công việc trong xã hội hiện đại.")])

add("bullets", section="Ôn tập đơn vị 单元练习", title="众说纷纭: 千奇百怪新职业 – đoán xem nghề này làm gì?", reveal=True, size=32,
    items=["(1) 闻香师 · 幸运饼干作家 · 地铁“推手” · 职业“美人鱼”",
           "Đáp án gợi ý: người ngửi thử mùi hương (nước hoa, thực phẩm) · người viết lời chúc trong bánh may mắn · người đẩy hành khách vào toa tàu điện ngầm giờ cao điểm · người biểu diễn làm nàng tiên cá dưới nước",
           "(2) 数鱼师 · 夜班护送师 · 送葬者 · 鸡性别判定工作者",
           "Đáp án gợi ý: người đếm cá (đếm cá di cư qua đập, cá trong trại nuôi) · người hộ tống ban đêm, đưa người về nhà an toàn · người đưa tang thuê · người phân biệt trống mái cho gà con mới nở",
           "(3) 合法“抢银行”职业 · 天鹅守望者 · 僵尸装扮者",
           "Đáp án gợi ý: người được ngân hàng thuê để thử đột nhập, tìm lỗ hổng an ninh · người trông coi, bảo vệ đàn thiên nga · người hóa trang thành xác sống trong công viên giải trí, nhà ma"],
    say=["Hoạt động đầu tiên của phần ôn tập là 众说纷纭, mỗi người một ý. Đề tài một: 千奇百怪新职业, những nghề mới muôn hình vạn trạng. Sách cho mười một tên nghề, yêu cầu đoán xem nghề đó làm gì, nghề nào kỳ quặc nhất, nghề nào thú vị nhất. Câu tục ngữ mở đầu là 世界之大，无奇不有, thế giới rộng lớn, chuyện lạ gì cũng có.",
         F(0, "Nhóm một: 闻香师，幸运饼干作家，地铁推手，职业美人鱼. Các bạn đoán thử nhé."),
         F(1, "Gợi ý: 闻香师 là người ngửi thử mùi hương, làm việc ở các hãng nước hoa, thực phẩm. 幸运饼干作家 là người viết những câu chúc, câu tiên tri trong bánh quy may mắn. 地铁推手 là người đẩy hành khách vào toa tàu điện ngầm giờ cao điểm, nổi tiếng ở Tokyo. 职业美人鱼 là người biểu diễn hóa thân nàng tiên cá dưới nước ở thủy cung."),
         F(2, "Nhóm hai: 数鱼师，夜班护送师，送葬者，鸡性别判定工作者."),
         F(3, "Gợi ý: 数鱼师 là người đếm cá, ví dụ đếm cá hồi di cư qua đập nước. 夜班护送师 là người hộ tống ban đêm, đưa người về nhà an toàn. 送葬者 là người đưa tang thuê. 鸡性别判定工作者 là người phân biệt trống mái cho gà con mới nở, một nghề đòi hỏi tay nghề rất cao."),
         F(4, "Nhóm ba: 合法抢银行职业，天鹅守望者，僵尸装扮者."),
         F(5, "Gợi ý: nghề cướp ngân hàng hợp pháp là người được ngân hàng thuê để thử đột nhập, tìm ra lỗ hổng an ninh. 天鹅守望者 là người trông coi, bảo vệ đàn thiên nga, như ở nước Anh. 僵尸装扮者 là người hóa trang thành xác sống trong công viên giải trí, nhà ma. Đề tài hai của mục này là 家庭煮夫 và 超级奶爸: các bạn nghĩ gì về những ông chồng làm nội trợ, ông bố ở nhà chăm con?")])

add("bullets", section="Ôn tập đơn vị 单元练习", title="从句段到篇章: phản bác bằng “phản chứng” 反证法", size=32,
    items=["## Ba bước: (1) nêu quan điểm đối phương, tỏ thái độ → (2) phân tích, nêu phản ví dụ → (3) nêu quan điểm của mình",
           "(1) ……的观点有一定的道理，然而…… · 我承认……但是…… · 这只是问题的一个侧面，并不全面 · ……缺乏说服力",
           "(2) 按照这种逻辑，我们设想一下，…… · 我们可以举出……的反例 · ……是以偏概全 · 事实胜于雄辩 · ……的例子不胜枚举",
           "(3) ……不是……，而是…… · 在我看来，…… · 由此可见，…… · 问题的实质是…… · 既然……的说法不成立，那么正确的观点是……"],
    say=["Hoạt động tiếp theo là 从句段到篇章, từ câu đoạn đến bài văn. Sách dạy cách phản bác quan điểm của người khác bằng 反证法, phương pháp phản chứng: muốn chứng minh luận điểm của mình đúng, trước hết chứng minh luận điểm ngược lại là sai.",
         F(0, "Có ba bước. Một, nêu quan điểm của đối phương và tỏ thái độ của mình. Hai, phân tích quan điểm ấy, đưa ra phản ví dụ. Ba, nêu quan điểm của mình."),
         F(1, "Bước một, tỏ thái độ khác: 的观点有一定的道理，然而, quan điểm ấy có lý ở một mức độ nào đó, tuy nhiên. 我承认，但是, tôi thừa nhận, nhưng. 这只是问题的一个侧面，并不全面, đây chỉ là một mặt của vấn đề, chưa toàn diện. 缺乏说服力, thiếu sức thuyết phục."),
         F(2, "Bước hai, nêu phản ví dụ: 按照这种逻辑，我们设想一下, theo logic này, chúng ta thử hình dung xem. 我们可以举出的反例, ta có thể nêu ra phản ví dụ. 是以偏概全, là lấy một phần để khái quát toàn bộ, vơ đũa cả nắm. 事实胜于雄辩, sự thật hơn mọi lời hùng biện. 的例子不胜枚举, ví dụ nhiều không kể xiết."),
         F(3, "Bước ba, nêu quan điểm của mình: 不是，而是, không phải, mà là. 在我看来, theo tôi. 由此可见, từ đó có thể thấy. 问题的实质是, thực chất của vấn đề là. 既然的说法不成立，那么正确的观点是, đã là cách nói ấy không đứng vững, thì quan điểm đúng là. Sách còn có một hoạt động viết khác: thiết kế phiếu khảo sát về nghề mới ở nước mình rồi viết báo cáo điều tra.")])

add("bullets", section="Ôn tập đơn vị 单元练习", title="Luyện tập: dùng 反证法 phản bác quan điểm về “996”", reveal=True, size=33,
    items=["Quan điểm: “我个人认为，能做996是一种巨大的福气，很多公司、很多人想996都没有机会。如果你年轻的时候不996，你什么时候可以996？”",
           "Đáp án gợi ý: 这个观点有一定的道理，年轻人确实应该努力奋斗。然而，按照这种逻辑，如果每个年轻人都长期996，他们的健康和家庭怎么办？事实上，因过度加班而亚健康甚至猝死的例子不胜枚举。由此可见，自觉拼搏与被迫996是两码事。问题的实质是，企业应该依法保障员工的休息权，而不是把加班说成福气。"],
    say=["Bây giờ chúng ta luyện tập: dùng phương pháp phản chứng để phản bác quan điểm sau đây. Đây là phát biểu của doanh nhân Mã Vân, nhà sáng lập Alibaba, năm hai nghìn không trăm mười chín, từng gây tranh cãi rất lớn.",
         F(0, "我个人认为，能做九九六是一种巨大的福气，很多公司、很多人想九九六都没有机会。如果你年轻的时候不九九六，你什么时候可以九九六？ Cá nhân tôi cho rằng, được làm 九九六 là một phúc lớn, rất nhiều công ty, rất nhiều người muốn làm 九九六 cũng không có cơ hội. Nếu lúc còn trẻ bạn không làm 九九六, thì bao giờ bạn mới làm được? Các bạn tạm dừng, thử viết một đoạn phản bác theo ba bước nhé.",
           cap="Quan điểm: 我个人认为，能做996是一种巨大的福气……如果你年轻的时候不996，你什么时候可以996？ Các bạn tạm dừng, thử viết một đoạn phản bác theo ba bước nhé."),
         F(1, "Đáp án gợi ý. Bước một: 这个观点有一定的道理，年轻人确实应该努力奋斗。然而，"),
         F(1, "Bước hai: 按照这种逻辑，如果每个年轻人都长期九九六，他们的健康和家庭怎么办？事实上，因过度加班而亚健康甚至猝死的例子不胜枚举。"),
         F(1, "Bước ba: 由此可见，自觉拼搏与被迫九九六是两码事。问题的实质是，企业应该依法保障员工的休息权，而不是把加班说成福气。 Các bạn thấy không, đoạn văn này dùng lại rất nhiều từ ngữ của bài sáu chấm một: 亚健康，猝死，两码事.")])

add("bullets", section="Ôn tập đơn vị 单元练习", title="Hoạt động khác & tranh luận 针锋相对", size=33,
    items=["明察暗访: khảo sát 5 người về “996” · về phụ nữ đi làm · về tiêu chuẩn chọn nghề (金饭碗 · 铁饭碗 · 泥饭碗)",
           "设计新职业 – tự thiết kế một nghề mới · 模拟校园招聘会 – mô phỏng hội chợ tuyển giáo viên tiếng Trung",
           "## Đề tranh luận 辩题",
           "(1) 奋斗与拼搏才是人生的主旋律，你同意吗？ · (2) 下班后收到工作消息，该不该回？",
           "(3) 让兴趣成为自己的职业还是业余爱好？ · (4) “女士优先”算不算性别歧视？",
           "(5) 事业上升期的职场女性，工作重要还是家庭重要呢？"],
    say=["Phần ôn tập của sách còn nhiều hoạt động thực hành.",
         F(0, "Mục 明察暗访, điều tra tìm hiểu: thiết kế phiếu hỏi năm người xung quanh về chế độ 九九六, về tình hình phụ nữ đi làm, và về tiêu chuẩn chọn nghề. Người Trung Quốc gọi việc làm ổn định là 铁饭碗, việc vừa ổn định vừa lương cao là 金饭碗, còn việc bấp bênh là 泥饭碗, bát cơm bằng đất, rơi là vỡ."),
         F(1, "Mục 设计新职业: tự thiết kế một nghề mới, đặt tên thật kêu, giải thích vì sao cần nghề đó và cần kỹ năng gì. Mục 模拟校园招聘会: mô phỏng một hội chợ việc làm, một nhóm làm nhà tuyển dụng giáo viên tiếng Trung, một nhóm làm ứng viên."),
         F(2, "Cuối cùng là mục 针锋相对, mũi kim đối mũi kim, tức là tranh luận. Sách đưa ra năm đề."),
         F(3, "Đề một: 奋斗与拼搏才是人生的主旋律，你同意吗？ Phấn đấu và cống hiến mới là giai điệu chính của đời người, bạn có đồng ý không? Đề hai: 下班后收到工作消息，该不该回？ Tan làm rồi nhận tin nhắn công việc, có nên trả lời không?"),
         F(4, "Đề ba: 让兴趣成为自己的职业还是业余爱好？ Nên biến sở thích thành nghề nghiệp, hay chỉ giữ làm thú vui lúc rảnh? Đề bốn: 女士优先算不算性别歧视？ Ưu tiên phụ nữ có phải là phân biệt giới tính không?"),
         F(5, "Đề năm: 事业上升期的职场女性，工作重要还是家庭重要呢？ Với phụ nữ đang trong giai đoạn thăng tiến sự nghiệp, công việc quan trọng hay gia đình quan trọng? Sách kể trường hợp một chị hai mươi chín tuổi làm quản lý ở công ty khởi nghiệp, phải đi công tác dài ngày một hai năm, trong khi gia đình giục sinh con. Các bạn chọn một đề, tự lập luận bằng tiếng Trung, nhớ dùng 反证法 và các mẫu câu của đơn vị này nhé."),
         {"t": "Cảm ơn các bạn đã theo dõi bài giảng. Như vậy là chúng ta đã hoàn thành Đơn vị sáu, chủ đề Nơi làm việc. Bài sau, chúng ta bước sang Đơn vị bảy: 经济篇, chủ đề Kinh tế, với bài bảy chấm một: 闲置经济是真正的共享经济, Kinh tế đồ cũ mới là kinh tế chia sẻ thực sự. Chúng ta sẽ bàn về chuyện mua bán đồ cũ, chiếc điện thoại cũ trong ngăn kéo, và những huy chương Olympic làm từ điện thoại cũ. Hẹn gặp lại các bạn. Chúc các bạn học tốt!",
          "cap": "Cảm ơn các bạn đã theo dõi bài giảng. Như vậy là chúng ta đã hoàn thành Đơn vị 6, chủ đề Nơi làm việc. Bài sau, chúng ta bước sang Đơn vị 7: 经济篇, chủ đề Kinh tế, với bài 7.1: 闲置经济是真正的共享经济, Kinh tế đồ cũ mới là kinh tế chia sẻ thực sự. Hẹn gặp lại các bạn!"}])

lesson = {
    "title": "顶石中文 – Bài 6.3: 30 岁的职场姐姐如何乘风破浪？ (Các chị 30 tuổi nơi công sở vượt sóng thế nào?)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"调离": "掉离",              # diàolí
                    "调岗": "掉岗",              # diàogǎng
                    "调动": "掉动",              # diàodòng
                    "调和": "条和",              # tiáohé
                    "着实": "酌实",              # zhuóshí
                    "着手": "酌手",              # zhuóshǒu
                    "应聘": "映聘",              # yìngpìn
                    "倒逼": "到逼",              # dàobī
                    "倒蛮": "到蛮",              # dào mán
                    "重担": "众担",              # zhòngdàn
                    "重回": "虫回",              # chónghuí
                    "重返": "虫返",              # chóngfǎn
                    "困难重重": "困难虫虫",      # chóngchóng
                    "夹缝": "家凤",              # jiāfèng
                    "产假": "产驾",              # chǎnjià (cả 陪产假)
                    "休假": "休驾",              # xiūjià
                    "为六个月": "维六个月",      # wéi
                    "相夫": "象夫",              # xiàngfū
                    "教子": "叫子",              # jiàozǐ
                    "刨根": "袍根",              # páogēn
                    "长此": "常此",              # chángcǐ
                    "长期": "常期",              # chángqī
                    "最长": "最常",              # zuì cháng
                    "问长问短": "问常问短",      # wèn cháng wèn duǎn
                    "长出": "涨出",              # zhǎngchū
                    "西藏": "西葬",              # Xīzàng
                    "参与率": "参预律",          # cānyùlǜ
                    "基数": "基树",              # jīshù
                    "体量": "体亮",              # tǐliàng
                    "看守": "刊守",              # kānshǒu
                    "为照顾": "位照顾",          # wèi
                    "为员工": "位员工",          # wèi
                    "晋升为": "晋升维",          # wéi
                    "处于": "楚于",              # chǔyú
                    "处理": "楚理",              # chǔlǐ
                    "差别": "插别",              # chābié
                    "睡觉": "睡叫",              # shuìjiào
                    "真相": "真象",              # zhēnxiàng
                    "没落": "末落",              # mòluò
                    "窘相": "窘象",              # jiǒngxiàng
                    "熬": "敖",                  # áo (熬夜)
                    "干出": "赣出",              # gànchū
                    "苦干": "苦赣",              # kǔgàn
                    "干的活": "赣的活",          # gàn de huó
                    "数鱼": "属鱼"},             # shǔ yú
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds63.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
