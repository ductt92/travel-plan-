#!/usr/bin/env python3
"""Kịch bản bài giảng 顶石中文 – Bài 1.3 «“高考移民”动了谁的奶酪？» + ôn tập Đơn vị 1. Chạy để sinh ds13.json."""
import json
import os

TAG = "顶石中文 · Bài 1.3 · “高考移民”动了谁的奶酪？"
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
    zh="“高考移民”", py="动了谁的奶酪？",
    vi="Bài 1.3: “Di dân thi đại học” đụng đến phô mai của ai?",
    sub="“Gāokǎo yímín” dòng le shéi de nǎilào?\nBài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng giáo trình 顶石中文, Đỉnh cao tiếng Trung.",
         "Hôm nay chúng ta học bài một chấm ba, bài cuối cùng của Đơn vị một, 教育篇, chủ đề Giáo dục: 高考移民动了谁的奶酪？ Nghĩa là: Di dân thi đại học đụng đến miếng phô mai của ai?",
         "高考移民 là hiện tượng thí sinh chuyển trường, chuyển hộ khẩu sang tỉnh có điểm chuẩn thấp hơn, chỉ tiêu nhiều hơn để thi đại học. Còn 动了谁的奶酪 nghĩa bóng là đụng đến lợi ích của ai. Bài khóa được cải biên từ video 高考移民伤害了谁 của chương trình 飞碟说.",
         "Sau phần bài học, chúng ta sẽ có thêm một chương ôn tập toàn bộ Đơn vị một, gồm các đề báo cáo, tranh luận, và cách viết một bài văn so sánh bằng tiếng Trung."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài khóa: nguyên nhân, hình thức và hệ quả của “高考移民”",
           "Nắm vững 45 từ mới, kèm âm Hán Việt và ví dụ",
           "8 mẫu câu: 可谓是 · 由于……且……加上…… · 钻……的空子 · 意味着 · 何苦 · 无非 · 远高于 · 给……以",
           "Kết hợp từ (词语搭配) và 14 thành ngữ, quán ngữ",
           "Luyện tập, thảo luận và ôn tập Đơn vị 1 (báo cáo, tranh luận, viết bài so sánh)"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu bài khóa: vì sao có hiện tượng di dân thi đại học, nó có những hình thức nào, và vì sao nó không công bằng."),
         F(1, "Thứ hai, nắm vững bốn mươi lăm từ mới, kèm âm Hán Việt và ví dụ."),
         F(2, "Thứ ba, học tám mẫu câu, như 可谓是, có thể nói là; 钻……的空子, lách kẽ hở của…; 何苦, hà tất phải khổ thế; và 无非, chẳng qua là."),
         F(3, "Thứ tư, học các kết hợp từ và mười bốn thành ngữ, quán ngữ. Bài này có rất nhiều thành ngữ, như 前程似锦, 背井离乡, 治标不治本."),
         F(4, "Cuối cùng là luyện tập, thảo luận, và ôn tập cả Đơn vị một. Các bạn hãy chuẩn bị giấy bút nhé.")])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 课前思考", title="Khởi động: Suy nghĩ trước khi học (课前思考)", reveal=True, size=34,
    items=["(1) 什么是“高考移民”？",
           "Đáp án gợi ý: 指一些考生通过转学或迁移户口，到录取分数线较低、录取率较高的地区参加高考。",
           "(2) 在你们国家，地区之间的教育水平有很大差异吗？",
           "Đáp án gợi ý: 有。在越南，城市和农村、平原和山区之间的教育条件差别比较大。",
           "(3) 在大学招生中，存在哪些不公平的现象？",
           "Đáp án gợi ý: 比如各地区录取分数线不同、有人钻加分政策的空子、有钱人家的孩子能享受更好的教育资源等。"],
    say=["Chúng ta bắt đầu bằng phần 课前思考, suy nghĩ trước khi học. Các bạn hãy tạm dừng video, tự trả lời bằng tiếng Trung trước, rồi nghe đáp án gợi ý nhé.",
         F(0, "Câu một: 什么是高考移民？ Di dân thi đại học là gì?"),
         F(1, "Đáp án gợi ý: 指一些考生通过转学或迁移户口，到录取分数线较低、录取率较高的地区参加高考。 Là việc một số thí sinh chuyển trường hoặc chuyển hộ khẩu đến những vùng có điểm chuẩn thấp hơn, tỷ lệ trúng tuyển cao hơn để dự thi đại học. 录取分数线 là điểm chuẩn, 录取率 là tỷ lệ trúng tuyển."),
         F(2, "Câu hai: 在你们国家，地区之间的教育水平有很大差异吗？ Ở nước bạn, trình độ giáo dục giữa các vùng có chênh lệch lớn không?"),
         F(3, "Đáp án gợi ý: 有。在越南，城市和农村、平原和山区之间的教育条件差别比较大。 Có. Ở Việt Nam, điều kiện giáo dục giữa thành thị và nông thôn, giữa đồng bằng và miền núi chênh lệch khá lớn."),
         F(4, "Câu ba: 在大学招生中，存在哪些不公平的现象？ Trong tuyển sinh đại học có những hiện tượng không công bằng nào?"),
         F(5, "Đáp án gợi ý: 比如各地区录取分数线不同、有人钻加分政策的空子、有钱人家的孩子能享受更好的教育资源等。 Chẳng hạn điểm chuẩn mỗi vùng khác nhau, có người lách kẽ hở của chính sách cộng điểm, con nhà giàu được hưởng tài nguyên giáo dục tốt hơn, vân vân.")])

add("bullets", section="Khởi động 课前思考", title="Bối cảnh: các khái niệm cần biết (注释)", size=34,
    items=["动了谁的奶酪: từ truyện 《谁动了我的奶酪？》 (Spencer Johnson) → xâm phạm, đe dọa lợi ích của người khác",
           "“十年寒窗苦读，一朝金榜题名”: mười năm đèn sách gian khổ, một sớm đỗ đạt bảng vàng",
           "学霸 / 学渣: học sinh học giỏi xuất sắc / học sinh học kém (thường dùng để tự trào)",
           "“不患寡而患不均” (《论语》): không lo ít, chỉ lo chia không đều",
           "分省录取: đại học tuyển sinh theo chỉ tiêu riêng cho từng tỉnh → điểm chuẩn mỗi tỉnh khác nhau"],
    say=["Trước khi học từ mới, chúng ta tìm hiểu một số khái niệm qua phần chú thích, 注释, của sách.",
         F(0, "动了谁的奶酪 xuất phát từ câu chuyện ngụ ngôn của nhà văn Mỹ Spencer Johnson, bản tiếng Trung tên là 谁动了我的奶酪, ai đã lấy miếng phô mai của tôi. Từ đó, người ta dùng 动了奶酪 để chỉ việc xâm phạm hoặc đe dọa lợi ích của người khác."),
         F(1, "十年寒窗苦读，一朝金榜题名. Nghĩa gốc là thí sinh thời xưa học hành gian khổ suốt nhiều năm, rồi đỗ cao trong khoa cử, tên được ghi lên bảng vàng. Ngày nay chỉ học sinh khổ học nhiều năm và đạt kết quả như ý trong kỳ thi đại học. Tiếng Việt cũng có câu mười năm đèn sách."),
         F(2, "学霸 và 学渣 là hai từ mới xuất hiện khi cạnh tranh trong giáo dục ngày càng gay gắt. 学霸 chỉ người chăm chỉ, học rộng, thành tích nổi bật; 学渣 là học sinh học kém. Hai từ này thường không mang nghĩa xấu, hay được dùng để tự trào."),
         F(3, "不患寡而患不均 xuất phát từ sách Luận Ngữ: không lo của cải ít, chỉ lo phân chia không công bằng. Câu này mở đầu đoạn kết của bài khóa."),
         F(4, "Và một khái niệm quan trọng: 分省录取. Các trường đại học Trung Quốc phân chỉ tiêu tuyển sinh cho từng tỉnh, nên điểm chuẩn mỗi tỉnh mỗi khác. Đây chính là gốc rễ của hiện tượng di dân thi đại học.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("奶酪", "nǎilào", "nãi lạc", "danh từ", "phô mai; (nghĩa bóng) lợi ích, miếng bánh", "我早餐喜欢吃面包和奶酪。", "Bữa sáng tôi thích ăn bánh mì với phô mai.",
     "Danh từ, một loại chế phẩm từ sữa, tức phô mai, thường được dùng để chỉ một lợi ích nào đó. 动了谁的奶酪 là đụng đến lợi ích của ai, giống như tiếng Việt nói đụng đến miếng bánh của ai."),
    ("可谓", "kěwèi", "khả vị", "động từ", "có thể nói là", "他的一生可谓传奇。", "Cuộc đời ông ấy có thể nói là một huyền thoại.",
     "Động từ văn viết, nghĩa là có thể nói là, có thể gọi là. Mẫu hay gặp: 可谓是. Trong bài: 高考可谓是万千学子命运的转折点."),
    ("转折", "zhuǎnzhé", "chuyển chiết", "động từ", "chuyển biến, đổi hướng", "这次比赛是他人生的转折点。", "Cuộc thi này là bước ngoặt cuộc đời anh ấy.",
     "Động từ, nghĩa là thay đổi, chuyển hướng. 转折点 là bước ngoặt. Trong ngữ pháp, 转折 còn chỉ quan hệ chuyển ý, như 但是，然而."),
    ("歪", "wāi", "oai", "tính từ", "lệch; (nghĩa bóng) bất chính, không đứng đắn", "他总想用歪点子赚钱。", "Hắn lúc nào cũng muốn kiếm tiền bằng mánh khóe bất chính.",
     "Tính từ, nghĩa gốc là lệch, xiêu vẹo, như 画挂歪了, bức tranh treo lệch; nghĩa bóng là bất chính, không đứng đắn: 歪理, lý lẽ cong queo; 歪风, thói xấu; 歪点子, mánh khóe xấu. Trong bài: 动起了歪心思, nảy ra ý đồ bất chính."),
    ("心思", "xīnsī", "tâm tư", "danh từ", "ý nghĩ, tâm trí, tâm sức", "为了这件事，他花了不少心思。", "Vì việc này, anh ấy đã tốn không ít tâm sức.",
     "Danh từ, nghĩa là đầu óc, ý nghĩ, tâm sức. Hay gặp 花心思，费心思，用尽心思. Chú ý: tiếng Việt tâm tư là nỗi lòng; còn 心思 thường là ý định, tâm sức bỏ ra."),
    ("奇葩", "qípā", "kỳ ba", "danh từ", "kỳ hoa; người, việc quái gở, khó hiểu", "这种奇葩规定让大家都很无语。", "Quy định quái gở này khiến ai cũng cạn lời.",
     "Danh từ, nghĩa gốc là bông hoa lạ mà đẹp, ví người đặc biệt xuất sắc; ngày nay thường chỉ những hành vi khó hiểu, kỳ quặc, hơi mang nghĩa chê. Trong bài: 高考移民是中国应试教育制度下的奇葩现象."),
    ("幅员", "fúyuán", "bức viên", "danh từ", "diện tích lãnh thổ", "中国幅员辽阔，人口众多。", "Trung Quốc lãnh thổ rộng lớn, dân số đông đúc.",
     "Danh từ, chỉ diện tích lãnh thổ, gần như chỉ đi với 辽阔: 幅员辽阔."),
    ("辽阔", "liáokuò", "liêu khoát", "tính từ", "rộng lớn, bao la", "草原辽阔无边。", "Thảo nguyên bao la không bờ bến.",
     "Tính từ, nghĩa là rộng lớn, bao la. Hay gặp 幅员辽阔，辽阔的草原，辽阔的大海."),
    ("现行", "xiànxíng", "hiện hành", "tính từ", "hiện hành, đang có hiệu lực", "现行的规定还有不少问题。", "Quy định hiện hành vẫn còn không ít vấn đề.",
     "Tính từ, nghĩa là đang thực hiện, đang có hiệu lực. Hay gặp 现行标准，现行法规，现行制度. Trong bài: 现行高招制度的弊端; 高招 là viết tắt của 高校招生, tuyển sinh đại học."),
    ("弊端", "bìduān", "tệ đoan", "danh từ", "mặt trái, tệ hại, lỗ hổng (của chế độ)", "这种制度有不少弊端。", "Chế độ này có không ít mặt trái.",
     "Danh từ, chỉ lỗ hổng và sai sót trong công việc hay chế độ. Chú ý: tiếng Việt tệ đoan thường chỉ tệ nạn xã hội; còn 弊端 là mặt trái, khiếm khuyết của một chế độ hay cách làm."),
    ("转学", "zhuǎnxué", "chuyển học", "động từ", "chuyển trường", "他上个月转学到北京了。", "Tháng trước cậu ấy đã chuyển trường lên Bắc Kinh.",
     "Động từ, nghĩa là chuyển từ trường này sang trường khác học. Hay gặp 办理转学手续, làm thủ tục chuyển trường."),
    ("迁移", "qiānyí", "thiên di", "động từ", "di chuyển, chuyển (chỗ ở, hộ khẩu)", "每年冬天，这些鸟都会迁移到南方。", "Mỗi mùa đông, những con chim này đều di cư về phương nam.",
     "Động từ, nghĩa là rời nơi cũ đến nơi khác. Hay gặp 迁移户口, chuyển hộ khẩu. Hán Việt là thiên di, như sự thiên di của loài chim."),
    ("相对", "xiāngduì", "tương đối", "tính từ", "tương đối", "这里的房价相对便宜。", "Giá nhà ở đây tương đối rẻ.",
     "Tính từ, nghĩa là so sánh mà nói, tương đối. Hay gặp 相对稳定，相对优势. Trong bài: 高考分数线相对较低."),
    ("应考", "yìngkǎo", "ứng khảo", "động từ", "dự thi, đi thi", "他明天要去北京应考。", "Ngày mai cậu ấy phải lên Bắc Kinh dự thi.",
     "Động từ, nghĩa là tham gia kỳ thi. Chữ đầu đọc thanh bốn. 应考者 là thí sinh. Trong bài: 到……地区应考."),
    ("均衡", "jūnhéng", "quân hành", "tính từ", "cân đối, đồng đều", "孩子的营养要均衡。", "Dinh dưỡng của trẻ phải cân đối.",
     "Tính từ, nghĩa là đồng đều, cân bằng. Hay gặp 营养均衡，均衡发展. Trong bài: 教育资源不均衡显而易见."),
    ("地域", "dìyù", "địa vực", "danh từ", "vùng, khu vực (rộng lớn)", "中国地域辽阔，各地风俗不同。", "Trung Quốc rộng lớn, phong tục mỗi vùng mỗi khác.",
     "Danh từ, chỉ một vùng đất có diện tích khá lớn. Hay gặp 地域辽阔，地域差异. Trong bài: 这种地域性差异, sự chênh lệch mang tính vùng miền."),
    ("求学", "qiúxué", "cầu học", "động từ", "đi học, theo học", "他十八岁就到上海求学。", "Mười tám tuổi anh ấy đã đến Thượng Hải theo học.",
     "Động từ, nghĩa là đến trường học tập, thường là đi học xa. Hay gặp 到北京求学，海外求学. 求学者 là người đi học."),
    ("何苦", "hékǔ", "hà khổ", "phó từ", "hà tất phải khổ thế, cần gì phải", "为这点小事生气，何苦呢？", "Vì chuyện nhỏ này mà tức giận, cần gì phải khổ thế?",
     "Phó từ, dùng giọng hỏi vặn để biểu thị không đáng, cuối câu thường có 呢. Đây là mẫu câu trọng điểm của bài."),
    ("奔波", "bēnbō", "bôn ba", "động từ", "bôn ba, tất bật ngược xuôi", "他每天为工作四处奔波。", "Ngày nào anh ấy cũng bôn ba khắp nơi vì công việc.",
     "Động từ, nghĩa là vất vả chạy ngược chạy xuôi. Âm Hán Việt và nghĩa giống tiếng Việt. Trong bài: 背井离乡奔波到外省考试."),
    ("无非", "wúfēi", "vô phi", "phó từ", "chẳng qua, chỉ là", "他说这些，无非是想让你帮忙。", "Anh ta nói những điều này, chẳng qua là muốn cậu giúp.",
     "Phó từ, nghĩa là chỉ, không ngoài, thường dùng khi muốn nói giảm, nói nhẹ sự việc. Hay gặp 无非是."),
    ("大体", "dàtǐ", "đại thể", "phó từ", "nhìn chung, đại thể", "我们的看法大体相同。", "Quan điểm của chúng tôi nhìn chung là giống nhau.",
     "Phó từ, nghĩa là xét theo phần lớn trường hợp hoặc mặt chủ yếu. Trong bài: 高考移民大体分为两类."),
    ("总和", "zǒnghé", "tổng hòa", "danh từ", "tổng, tổng số cộng lại", "他的收入是我们两个人的总和。", "Thu nhập của anh ấy bằng tổng thu nhập của hai chúng tôi.",
     "Danh từ, nghĩa là toàn bộ số lượng hoặc nội dung cộng lại. Trong bài: 高于四川、江苏、安徽、湖北四个省的招生人数的总和."),
    ("欠", "qiàn", "khiếm", "tính từ", "thiếu, chưa đủ (văn viết)", "这件事你考虑得有点儿欠周到。", "Việc này cậu cân nhắc hơi thiếu chu đáo.",
     "Tính từ văn viết, nghĩa là thiếu, chưa đủ, đứng trước tính từ hoặc động từ hai chữ: 欠发达, kém phát triển; 欠考虑, thiếu cân nhắc; 欠妥, chưa thỏa đáng. Hán Việt là khiếm, như trong khiếm khuyết. Trong bài: 移民至欠发达地区. Ngoài ra động từ 欠 còn có nghĩa là nợ: 欠钱."),
    ("自治区", "zìzhìqū", "tự trị khu", "danh từ", "khu tự trị", "西藏是中国的一个自治区。", "Tây Tạng là một khu tự trị của Trung Quốc.",
     "Danh từ, đơn vị hành chính tự trị dân tộc ngang cấp tỉnh, như khu tự trị Nội Mông, khu tự trị Tân Cương Duy Ngô Nhĩ. Trung Quốc có năm khu tự trị."),
    ("优待", "yōudài", "ưu đãi", "động từ", "ưu đãi, đối đãi đặc biệt", "这家博物馆对老人有优待。", "Bảo tàng này có ưu đãi cho người cao tuổi.",
     "Động từ, nghĩa là dành cho sự đối đãi tốt hơn. Âm Hán Việt và nghĩa giống tiếng Việt. Trong bài: 民族优待政策, chính sách ưu đãi dân tộc."),
    ("本意", "běnyì", "bản ý", "danh từ", "ý định ban đầu, dụng ý vốn có", "他的本意是好的，只是话说重了。", "Ý anh ấy vốn là tốt, chỉ là nói hơi nặng lời.",
     "Danh từ, nghĩa là ý nghĩa hoặc ý định ban đầu. Trong bài: 这一制度的本意是避免……, mục đích ban đầu của chế độ này là tránh…."),
    ("匮乏", "kuìfá", "quỹ phạp", "tính từ", "thiếu thốn, khan hiếm", "那时候物资非常匮乏。", "Hồi đó vật tư vô cùng thiếu thốn.",
     "Tính từ văn viết, nghĩa là thiếu, không đủ. Hay gặp 资源匮乏，物资匮乏，人才匮乏."),
    ("捷径", "jiéjìng", "tiệp kính", "danh từ", "đường tắt", "学习语言没有捷径。", "Học ngoại ngữ không có đường tắt.",
     "Danh từ, nghĩa là con đường gần; nghĩa bóng là cách làm khéo để nhanh đạt mục đích. Hay gặp 走捷径，寻求捷径. Trong bài: 想走捷径的考生."),
    ("限度", "xiàndù", "hạn độ", "danh từ", "giới hạn, hạn mức", "我的耐心是有限度的。", "Sự kiên nhẫn của tôi là có giới hạn.",
     "Danh từ, nghĩa là giới hạn cao nhất hoặc thấp nhất. Hay gặp 最高限度，有限度. Trong bài: 每个城市的大学录取名额都有限度."),
    ("凭借", "píngjiè", "bằng tạ", "động từ", "dựa vào, nhờ vào", "他凭借自己的努力考上了大学。", "Anh ấy nhờ nỗ lực của bản thân mà đỗ đại học.",
     "Động từ, nghĩa là dựa vào, nương vào. Trong bài: 凭借自身优势, dựa vào ưu thế của bản thân."),
    ("挤占", "jǐzhàn", "tễ chiếm", "động từ", "chen vào chiếm chỗ, chiếm mất", "他的车挤占了别人的车位。", "Xe của anh ta chiếm mất chỗ đỗ của người khác.",
     "Động từ, nghĩa là chen vào đẩy cái cũ ra để chiếm lấy vị trí của nó. Hay gặp 挤占名额，挤占资源，挤占空间."),
    ("委屈", "wěiqū", "ủy khuất", "tính từ", "tủi thân, oan ức", "她觉得很委屈，哭了起来。", "Cô ấy thấy rất tủi thân, bật khóc.",
     "Tính từ, nghĩa là bị trách móc hoặc đối xử không đáng, trong lòng buồn tủi. Trong khẩu ngữ, chữ sau thường đọc thanh nhẹ. Trong bài: 当地人就真的该感觉委屈吗？"),
    ("命题", "mìngtí", "mệnh đề", "danh từ", "ra đề; đề bài", "这是一篇命题作文。", "Đây là một bài văn theo đề cho sẵn.",
     "Ở bài này nghĩa là ra đề thi, đề bài. Hay gặp 命题作文，统一命题，自主命题. Chú ý: tiếng Việt mệnh đề thường là thuật ngữ logic, ngữ pháp; còn ở đây 命题 là ra đề. Trong bài: 实行全国统一命题."),
    ("学渣", "xuézhā", "học tra", "danh từ", "học sinh kém (từ mạng)", "我上学的时候是个学渣。", "Hồi đi học tôi là một học sinh kém.",
     "Danh từ, từ mới trên mạng, chỉ học sinh học kém, đối lập với 学霸. Chữ 渣 là cặn bã. Thường không mang nghĩa xấu, hay dùng để tự trào."),
    ("学霸", "xuébà", "học bá", "danh từ", "học sinh xuất sắc, “thánh học”", "她是我们班的学霸。", "Cô ấy là “thánh học” của lớp chúng tôi.",
     "Danh từ, chỉ người chăm chỉ, học giỏi, thành tích xuất sắc. Chữ 霸 là bá chủ. Trong bài: 在山东是学渣，但在北京，就是学霸."),
    ("自主", "zìzhǔ", "tự chủ", "động từ", "tự chủ, tự quyết định", "这家公司坚持自主研发。", "Công ty này kiên trì tự nghiên cứu phát triển.",
     "Động từ, nghĩa là tự mình quyết định, tự mình hoàn thành. Hay gặp 自主招生，自主研发，自主命题."),
    ("效仿", "xiàofǎng", "hiệu phỏng", "động từ", "bắt chước, noi theo", "其他学校也纷纷效仿这种做法。", "Các trường khác cũng lần lượt làm theo cách này.",
     "Động từ, nghĩa là bắt chước, học theo. Trong bài: 北京等地区也纷纷效仿."),
    ("可比性", "kěbǐxìng", "khả tỉ tính", "danh từ", "tính có thể so sánh", "这两组数据没有可比性。", "Hai nhóm số liệu này không thể so sánh với nhau.",
     "Danh từ, chỉ tính chất có thể so sánh, đối chiếu. Trong bài: 录取分数线不再具有可比性."),
    ("掩盖", "yǎngài", "yểm cái", "động từ", "che giấu, che đậy", "谎言掩盖不了事实。", "Lời nói dối không che giấu được sự thật.",
     "Động từ, nghĩa là che đậy, giấu đi. Hay gặp 掩盖事实，掩盖真相，掩盖罪行."),
    ("永恒", "yǒnghéng", "vĩnh hằng", "tính từ", "vĩnh hằng, muôn thuở", "爱是一个永恒的话题。", "Tình yêu là một đề tài muôn thuở.",
     "Tính từ, nghĩa là mãi mãi không thay đổi, mãi mãi tồn tại. Trong bài: 公平是文明社会永恒的诉求."),
    ("诉求", "sùqiú", "tố cầu", "danh từ", "nguyện vọng, yêu cầu", "政府应该倾听市民的诉求。", "Chính quyền nên lắng nghe nguyện vọng của người dân.",
     "Danh từ, nghĩa là mong muốn, đòi hỏi. Hay gặp 利益诉求，倾听诉求."),
    ("诱因", "yòuyīn", "dụ nhân", "danh từ", "nguyên nhân gây ra, yếu tố dẫn tới", "压力是很多疾病的诱因。", "Áp lực là yếu tố dẫn tới nhiều bệnh tật.",
     "Danh từ, chỉ nguyên nhân dẫn đến một tình trạng nào đó. Trong bài: 这一现象背后的诱因是……"),
    ("眼下", "yǎnxià", "nhãn hạ", "danh từ", "trước mắt, hiện nay", "眼下最重要的是找工作。", "Trước mắt điều quan trọng nhất là tìm việc.",
     "Danh từ chỉ thời gian, nghĩa là hiện giờ, trước mắt. Trong bài: 眼下的当务之急."),
    ("有望", "yǒuwàng", "hữu vọng", "động từ", "có hy vọng", "这支球队有望获得冠军。", "Đội bóng này có hy vọng giành chức vô địch.",
     "Động từ, nghĩa là có hy vọng. Hay gặp 有望获胜，有望成功. Trong bài: 才有望终结高考移民的怪现象."),
    ("终结", "zhōngjié", "chung kết", "động từ", "kết thúc, chấm dứt", "他的运动生涯就此终结了。", "Sự nghiệp thi đấu của anh ấy kết thúc tại đây.",
     "Động từ, nghĩa là kết thúc hẳn. Chú ý: tiếng Việt chung kết là trận đấu cuối cùng, tiếng Trung là 决赛; còn 终结 là chấm dứt."),
]

add("bullets", chapter="Từ mới (45 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 1.3 có 45 từ mới, chia thành 15 nhóm",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 应考 (yìng) · 委屈 (wěiqu) · 欠 (欠发达 qiàn fādá)",
           "Từ dễ nhầm: 弊端 · 命题 · 终结 · 心思"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bài này có bốn mươi lăm từ, chia thành mười lăm nhóm, mỗi nhóm ba từ. Nhiều từ trong bài là từ văn viết dùng trong tin tức, bình luận xã hội.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe nhé."),
         F(3, "Chú ý âm đọc: chữ đầu trong 应考 đọc thanh bốn; chữ sau trong 委屈 trong khẩu ngữ đọc thanh nhẹ. Bảng từ của sách in nhầm phiên âm của chữ 欠 thành phiên âm của cả cụm 欠发达, các bạn lưu ý nhé."),
         F(4, "Có mấy từ Hán Việt dễ hiểu nhầm, như 弊端, không phải tệ nạn mà là mặt trái của chế độ; 命题, ở đây là ra đề thi; 终结, không phải trận chung kết mà là chấm dứt. Chúng ta bắt đầu.")])

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
    ("“十年寒窗苦读，一朝金榜题名”，在中国，高考可谓是万千学子命运的转折点。为了孩子的未来前程似锦，有些家长开始动起了“歪心思”，想方设法，甚至投机取巧给孩子搞起了“高考移民”。",
     "“Mười năm đèn sách gian khổ, một sớm đề tên bảng vàng”, ở Trung Quốc, thi đại học có thể nói là bước ngoặt số phận của hàng triệu sĩ tử. Để tương lai con cái rạng rỡ như gấm hoa, có những phụ huynh bắt đầu nảy ra “ý đồ bất chính”, tìm đủ mọi cách, thậm chí lợi dụng kẽ hở, làm cho con mình “di dân thi đại học”.",
     ["可谓是 là có thể nói là. 万千学子 là hàng nghìn hàng vạn sĩ tử. 转折点 là bước ngoặt. 前程似锦 là tiền đồ rực rỡ như gấm, thường dùng để chúc.",
      "动起了歪心思 là nảy ra ý đồ bất chính. 想方设法 là nghĩ đủ mọi cách. 投机取巧 là lợi dụng thời cơ, giở mánh khóe để kiếm lợi. 搞起了 là bày ra, làm ra, khẩu ngữ, ở đây hơi mang ý chê."]),
    ("“高考移民”是中国应试教育制度下的奇葩现象。由于中国幅员辽阔、考生众多，且各地区之间教育资源分配不均，加上现行高招制度的弊端，",
     "“Di dân thi đại học” là một hiện tượng quái gở dưới chế độ giáo dục chạy theo thi cử của Trung Quốc. Do Trung Quốc lãnh thổ rộng lớn, thí sinh đông đảo, hơn nữa tài nguyên giáo dục giữa các vùng phân bổ không đều, cộng thêm những mặt trái của chế độ tuyển sinh đại học hiện hành,",
     ["奇葩现象 là hiện tượng quái gở, khó hiểu. 幅员辽阔 là lãnh thổ rộng lớn. 考生众多 là thí sinh đông đảo.",
      "由于……，且……，加上……: do…, hơn nữa…, cộng thêm…, đây là mẫu câu chồng nhiều nguyên nhân. 分配不均 là phân bổ không đều. 高招 là tuyển sinh đại học."]),
    ("各省各地区的录取分数线、招生名额、竞争人数和考题难易程度等方面都存在差异。因此，部分考生通过转学或迁移户口到高考分数线相对较低、录取率较高的地区应考，钻高考政策的空子。",
     "nên điểm chuẩn, chỉ tiêu tuyển sinh, số người cạnh tranh và độ khó dễ của đề thi ở các tỉnh, các vùng đều có sự chênh lệch. Vì vậy, một số thí sinh chuyển trường hoặc chuyển hộ khẩu đến những vùng có điểm chuẩn tương đối thấp, tỷ lệ trúng tuyển khá cao để dự thi, lách kẽ hở của chính sách thi đại học.",
     ["录取分数线 là điểm chuẩn. 招生名额 là chỉ tiêu tuyển sinh. 难易程度 là mức độ khó dễ; chữ 易 ở đây là dễ, đọc thanh bốn.",
      "通过转学或迁移户口 là thông qua chuyển trường hoặc chuyển hộ khẩu. 录取率 là tỷ lệ trúng tuyển. 钻……的空子 là lách kẽ hở của…, 空子 là chỗ hở, sơ hở."]),
    ("教育资源不均衡显而易见，这种地域性差异主要由高考录取模式——分省录取来决定，有差异便意味着人员有流动的可能，",
     "Tài nguyên giáo dục không đồng đều là điều ai cũng thấy rõ. Sự chênh lệch mang tính vùng miền này chủ yếu do mô hình tuyển sinh đại học – tuyển sinh theo từng tỉnh – quyết định. Có chênh lệch thì có nghĩa là có khả năng người ta sẽ di chuyển,",
     ["显而易见 là rõ ràng dễ thấy. 地域性差异 là sự chênh lệch mang tính vùng miền. 由……来决定 là do… quyết định.",
      "分省录取 là tuyển sinh theo tỉnh, mỗi tỉnh một chỉ tiêu. 有差异便意味着…… là có chênh lệch thì có nghĩa là…; 便 là văn viết của 就. 流动 là di chuyển, lưu động."]),
    ("不然原本在家乡求学的考生，何苦舍近求远或背井离乡奔波到外省考试呢？利用区域分数差来增强高考竞争力，无非是为了考入更理想的大学。",
     "nếu không thì những thí sinh vốn đang học ở quê nhà, hà tất phải bỏ gần tìm xa, hay rời quê bôn ba sang tỉnh khác thi làm gì? Lợi dụng chênh lệch điểm giữa các vùng để tăng sức cạnh tranh trong kỳ thi, chẳng qua là để vào được trường đại học lý tưởng hơn.",
     ["不然 là nếu không thì. 何苦……呢 là hà tất phải khổ…, câu hỏi tu từ. 舍近求远 là bỏ gần tìm xa. 背井离乡 là rời bỏ quê hương. 奔波 là bôn ba.",
      "区域分数差 là chênh lệch điểm giữa các vùng. 增强竞争力 là tăng sức cạnh tranh. 无非是为了 là chẳng qua là để, cách nói giảm nhẹ."]),
    ("“高考移民”大体分为两类：一是移民到发达地区。多年来，北上广等大城市一直拥有更多的招生名额，",
     "“Di dân thi đại học” nhìn chung chia làm hai loại. Loại thứ nhất là di dân đến vùng phát triển. Nhiều năm nay, các thành phố lớn như Bắc Kinh, Thượng Hải, Quảng Châu luôn có nhiều chỉ tiêu tuyển sinh hơn,",
     ["大体分为两类 là nhìn chung chia làm hai loại. 一是……二是…… là một là…, hai là…, dùng để phân loại.",
      "北上广 là cách nói tắt của Bắc Kinh, Thượng Hải, Quảng Châu, ba thành phố lớn nhất Trung Quốc. 拥有更多的招生名额 là có nhiều chỉ tiêu tuyển sinh hơn."]),
    ("如清华大学在北京的招生人数高于四川、江苏、安徽、湖北四个省的招生人数的总和，而北京的人口却不到这四省总人口的1/20；",
     "chẳng hạn số học sinh Đại học Thanh Hoa tuyển ở Bắc Kinh còn cao hơn tổng số tuyển ở bốn tỉnh Tứ Xuyên, Giang Tô, An Huy, Hồ Bắc cộng lại, trong khi dân số Bắc Kinh chưa bằng một phần hai mươi tổng dân số bốn tỉnh này;",
     ["如 là ví dụ như. 高于……的总和 là cao hơn tổng số của…. 却 là lại, nhấn mạnh sự trái ngược.",
      "Cách đọc phân số: một phần hai mươi đọc là 二十分之一, mẫu số đọc trước, tử số đọc sau. Con số này cho thấy sự chênh lệch rất lớn về cơ hội giữa thí sinh Bắc Kinh và thí sinh các tỉnh đông dân."],
     "如清华大学在北京的招生人数高于四川、江苏、安徽、湖北四个省的招生人数的总和，而北京的人口却不到这四省总人口的二十分之一；"),
    ("二是移民至欠发达地区。由于自治区的民族优待政策，西藏、新疆、海南等地都拥有较多的招生名额，加之当地人口较少，这样一来，其高考实际录取率远高于河南、河北等人口大省，而竞争压力小得多。",
     "Loại thứ hai là di dân đến vùng kém phát triển. Do chính sách ưu đãi dân tộc của các khu tự trị, những nơi như Tây Tạng, Tân Cương, Hải Nam đều có khá nhiều chỉ tiêu tuyển sinh, cộng thêm dân số địa phương ít, như vậy tỷ lệ trúng tuyển thực tế ở đó cao hơn nhiều so với các tỉnh đông dân như Hà Nam, Hà Bắc, mà áp lực cạnh tranh lại nhỏ hơn nhiều.",
     ["移民至 là di dân đến; 至 là văn viết của 到. 欠发达地区 là vùng kém phát triển. 民族优待政策 là chính sách ưu đãi dân tộc thiểu số.",
      "加之 là cộng thêm, văn viết của 加上. 其 là của nó, chỉ những vùng này. 远高于 là cao hơn nhiều so với. 人口大省 là tỉnh đông dân."]),
    ("这一制度的本意是避免教育落后地区因教育资源匮乏，而导致学生受教育机会不平等，但它确实给想走捷径的考生以可乘之机。",
     "Mục đích ban đầu của chế độ này là tránh để những vùng giáo dục lạc hậu, vì thiếu thốn tài nguyên giáo dục, mà học sinh không được bình đẳng về cơ hội học tập; nhưng nó quả thực đã cho những thí sinh muốn đi đường tắt một cơ hội để lợi dụng.",
     ["本意 là ý định ban đầu. 因……而导致…… là vì… mà dẫn đến…. 匮乏 là thiếu thốn. 受教育机会 là cơ hội được học hành.",
      "给……以…… là đem lại cho ai cái gì, văn viết. 走捷径 là đi đường tắt. 可乘之机 là cơ hội có thể lợi dụng, sơ hở để chen vào."]),
    ("每个城市的大学录取名额都有限度，高考移民作为外来者，变更户籍后，凭借自身优势，插一脚进来抢饭吃，挤占当地人上大学的录取名额，对当地人来说相当不公平。话又说回来，当地人就真的该感觉委屈吗？",
     "Chỉ tiêu tuyển sinh đại học của mỗi thành phố đều có giới hạn. Người di dân thi đại học là người từ nơi khác đến, sau khi đổi hộ tịch, dựa vào ưu thế của mình mà chen chân vào tranh bát cơm, chiếm mất chỉ tiêu vào đại học của người địa phương, điều này đối với người địa phương là khá bất công. Nhưng nói đi cũng phải nói lại, người địa phương có thật sự nên thấy oan ức không?",
     ["有限度 là có giới hạn. 外来者 là người từ nơi khác đến. 变更户籍 là thay đổi hộ tịch. 凭借自身优势 là dựa vào ưu thế của mình.",
      "插一脚 là chen chân vào; 抢饭吃 là tranh bát cơm. 挤占 là chen vào chiếm chỗ. 话又说回来 là nói đi cũng phải nói lại, mẫu câu của bài trước. Câu hỏi cuối mở ra đoạn tiếp theo."]),
    ("1952年，中国有了“高考”这个词，实行全国统一命题。这种情况持续了42年。2001年，北京文科一本录取线只有454分，山东却高达580分。",
     "Năm 1952, Trung Quốc có từ “thi đại học”, áp dụng đề thi thống nhất toàn quốc. Tình trạng này kéo dài 42 năm. Năm 2001, điểm chuẩn vào các trường đại học nhóm một khối xã hội ở Bắc Kinh chỉ có 454 điểm, còn Sơn Đông lại cao tới 580 điểm.",
     ["统一命题 là ra đề thống nhất. 持续了四十二年 là kéo dài bốn mươi hai năm.",
      "一本录取线 là điểm chuẩn vào các trường đại học nhóm một, nhóm trường tốt nhất. Cùng một đề thi mà điểm chuẩn Sơn Đông cao hơn Bắc Kinh tới một trăm hai mươi sáu điểm. 高达 là cao tới."],
     "一九五二年，中国有了高考这个词，实行全国统一命题。这种情况持续了四十二年。二零零一年，北京文科一本录取线只有四百五十四分，山东却高达五百八十分。"),
    ("如果考生的分数是460分，在山东是学渣，但在北京，就是学霸。同样的试卷，同样的分数，只因户籍不同，上的大学便有天壤之别。",
     "Nếu một thí sinh được 460 điểm, thì ở Sơn Đông là học sinh kém, nhưng ở Bắc Kinh lại là “thánh học”. Cùng một đề thi, cùng một số điểm, chỉ vì hộ tịch khác nhau mà trường đại học được vào khác nhau một trời một vực.",
     ["学渣 là học sinh kém; 学霸 là học sinh xuất sắc. Bốn trăm sáu mươi điểm ở Sơn Đông chưa tới điểm chuẩn, nhưng ở Bắc Kinh đã vượt điểm chuẩn khá xa.",
      "只因 là chỉ vì. 天壤之别 là khác biệt như trời với đất, một trời một vực. 便 là liền, thì."],
     "如果考生的分数是四百六十分，在山东是学渣，但在北京，就是学霸。同样的试卷，同样的分数，只因户籍不同，上的大学便有天壤之别。"),
    ("当媒体和公众开始讨论并努力解决这一不公平的现象时，部分地区开始实行自主命题。1985年，上海率先拿到高考自主命题权，开始改革，随后，北京等地区也纷纷效仿，",
     "Khi truyền thông và công chúng bắt đầu bàn luận và nỗ lực giải quyết hiện tượng bất công này, một số địa phương bắt đầu tự ra đề. Năm 1985, Thượng Hải là nơi đầu tiên giành được quyền tự ra đề thi đại học, bắt đầu cải cách; sau đó, Bắc Kinh và các nơi khác cũng lần lượt làm theo,",
     ["当……时 là khi…. 媒体 là truyền thông, 公众 là công chúng. 自主命题 là tự ra đề.",
      "率先 là đi đầu, là người đầu tiên. 自主命题权 là quyền tự ra đề. 随后 là ngay sau đó. 纷纷效仿 là lần lượt bắt chước theo."],
     "当媒体和公众开始讨论并努力解决这一不公平的现象时，部分地区开始实行自主命题。一九八五年，上海率先拿到高考自主命题权，开始改革，随后，北京等地区也纷纷效仿，"),
    ("这让各地区之间的录取分数线不再具有可比性，因为考卷不一样，山东的460分不等于北京的460分，从而“巧妙”地掩盖了高考录取的不公平。可是独立命题了，教育资源不均衡的现实就改变了吗？",
     "điều này khiến điểm chuẩn giữa các vùng không còn so sánh được với nhau nữa, vì đề thi khác nhau, 460 điểm ở Sơn Đông không bằng 460 điểm ở Bắc Kinh, từ đó đã “khéo léo” che đậy sự bất công trong tuyển sinh đại học. Thế nhưng tự ra đề rồi, thực trạng tài nguyên giáo dục không đồng đều đã thay đổi chưa?",
     ["不再具有可比性 là không còn tính so sánh được nữa. 从而 là từ đó, nhờ đó, nối kết quả.",
      "巧妙 trong ngoặc kép là khéo léo, ở đây mang ý mỉa mai: không phải giải quyết bất công, mà chỉ là che giấu nó đi. 掩盖 là che đậy. Câu hỏi cuối dẫn vào đoạn kết."],
     "这让各地区之间的录取分数线不再具有可比性，因为考卷不一样，山东的四百六十分不等于北京的四百六十分，从而巧妙地掩盖了高考录取的不公平。可是独立命题了，教育资源不均衡的现实就改变了吗？"),
    ("“不患寡而患不均”，公平是文明社会永恒的诉求。虽然教育部明确表示加强资格审查，严厉打击“高考移民”的行为，但不能否认这一现象背后的诱因是各省份户籍福利差异和机会的不均等，",
     "“Không lo ít, chỉ lo không đều”, công bằng là đòi hỏi muôn thuở của xã hội văn minh. Tuy Bộ Giáo dục đã tuyên bố rõ sẽ tăng cường thẩm tra tư cách, nghiêm trị hành vi “di dân thi đại học”, nhưng không thể phủ nhận rằng nguyên nhân sâu xa đằng sau hiện tượng này là sự chênh lệch phúc lợi hộ tịch và sự bất bình đẳng về cơ hội giữa các tỉnh,",
     ["不患寡而患不均 là câu trong Luận Ngữ. 永恒的诉求 là đòi hỏi muôn thuở. 资格审查 là thẩm tra tư cách dự thi. 严厉打击 là nghiêm trị, trấn áp mạnh tay.",
      "不能否认 là không thể phủ nhận. 诱因 là nguyên nhân dẫn tới. 户籍福利差异 là chênh lệch về phúc lợi gắn với hộ tịch. 机会的不均等 là cơ hội không bình đẳng."]),
    ("有关部门不能只依靠户籍地来限制此类违规现象，围追堵截也只是治标不治本，那些在高考大省苦读的考生与在资源匮乏地区就读的考生并不会因此高枕无忧。",
     "các cơ quan hữu quan không thể chỉ dựa vào nơi đăng ký hộ tịch để hạn chế những hiện tượng vi phạm loại này; vây bắt chặn đường cũng chỉ là chữa ngọn không chữa gốc, những thí sinh khổ học ở các tỉnh đông thí sinh và những thí sinh học ở vùng thiếu thốn tài nguyên cũng không vì thế mà được kê cao gối ngủ yên.",
     ["有关部门 là cơ quan hữu quan. 户籍地 là nơi đăng ký hộ tịch. 此类违规现象 là những hiện tượng vi phạm loại này.",
      "围追堵截 là bao vây, truy đuổi, chặn đánh, ở đây là truy quét gắt gao. 治标不治本 là chữa ngọn không chữa gốc. 高枕无忧 là kê cao gối mà ngủ, yên tâm không lo gì."]),
    ("眼下的当务之急还是要尽快深化高考改革，同时缩小地域间教育资源的差距，只有对症下药从根本上解决问题，才有望终结“高考移民”的怪现象。",
     "Việc cấp bách trước mắt vẫn là phải nhanh chóng đẩy mạnh cải cách thi đại học, đồng thời thu hẹp khoảng cách về tài nguyên giáo dục giữa các vùng; chỉ có bốc đúng thuốc, giải quyết vấn đề từ gốc rễ, thì mới có hy vọng chấm dứt hiện tượng quái lạ “di dân thi đại học”.",
     ["眼下 là trước mắt. 当务之急 là việc cấp bách nhất hiện nay. 深化改革 là đẩy mạnh, đi sâu cải cách. 缩小差距 là thu hẹp khoảng cách.",
      "只有……才…… là chỉ có… mới…. 对症下药 là bốc thuốc đúng bệnh. 有望终结 là có hy vọng chấm dứt. Đoạn kết đưa ra giải pháp: không phải trấn áp, mà là giải quyết sự bất bình đẳng về giáo dục."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa “高考移民”动了谁的奶酪？", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa. Đây là một bài bình luận xã hội điển hình: nêu hiện tượng, phân tích nguyên nhân, đưa số liệu, rồi đề xuất giải pháp. Văn phong khá trang trọng, nhiều từ văn viết và thành ngữ.",
         F(0, "Bài có sáu đoạn, thầy chia thành mười bảy phần ngắn. Với mỗi phần, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
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
    items=["Đoạn 1: Thi đại học là bước ngoặt số phận → một số phụ huynh làm “高考移民”",
           "Đoạn 2: Định nghĩa và nguyên nhân: lãnh thổ rộng, thí sinh đông, tài nguyên không đều, chế độ có mặt trái",
           "Đoạn 3: Hai loại di dân: đến vùng phát triển (北上广) và đến vùng kém phát triển (西藏、新疆、海南)",
           "Đoạn 4–5: Bất công với người địa phương? – lịch sử đề thi thống nhất và tự ra đề (1952, 2001, 1985)",
           "Đoạn 6: Truy quét chỉ chữa ngọn; giải pháp là cải cách, thu hẹp khoảng cách giáo dục giữa các vùng"],
    say=["Chúng ta cùng nhìn lại bố cục của bài khóa. Đây là bố cục rất điển hình của một bài bình luận xã hội.",
         F(0, "Đoạn một: nêu hiện tượng. Thi đại học là bước ngoặt số phận, nên có phụ huynh tìm mọi cách cho con di dân thi đại học."),
         F(1, "Đoạn hai: định nghĩa và nguyên nhân: lãnh thổ rộng, thí sinh đông, tài nguyên giáo dục phân bổ không đều, chế độ tuyển sinh có mặt trái, nên điểm chuẩn và chỉ tiêu mỗi nơi một khác."),
         F(2, "Đoạn ba: hai loại di dân: đến các thành phố phát triển như Bắc Kinh, Thượng Hải, Quảng Châu, nơi có nhiều chỉ tiêu; và đến các vùng kém phát triển như Tây Tạng, Tân Cương, Hải Nam, nơi có chính sách ưu đãi."),
         F(3, "Đoạn bốn và năm: di dân thi đại học bất công với người địa phương, nhưng bản thân người địa phương có thật sự chịu thiệt? Tác giả dùng số liệu để chỉ ra sự bất công giữa các tỉnh, và việc tự ra đề chỉ che giấu nó."),
         F(4, "Đoạn sáu: kết luận. Truy quét chỉ là chữa ngọn; việc cấp bách là cải cách thi đại học, thu hẹp khoảng cách giáo dục giữa các vùng.")])

add("bullets", section="Đọc hiểu 课文理解", title="Câu hỏi đọc hiểu (1)", reveal=True, size=34,
    items=["(1) 为什么说高考是万千学子命运的转折点？",
           "Đáp án: 因为“十年寒窗苦读，一朝金榜题名”，考上理想的大学，就能改变人生的道路。",
           "(2) “高考移民”分为哪两类？",
           "Đáp án: 一是移民到北上广等发达地区；二是移民到西藏、新疆、海南等欠发达地区。",
           "(3) 为什么西藏、新疆等地的高考实际录取率高？",
           "Đáp án: 因为有民族优待政策，招生名额较多，加之当地人口较少。"],
    say=["Bây giờ chúng ta kiểm tra mức độ hiểu bài. Thầy đọc câu hỏi, các bạn tạm dừng, trả lời bằng tiếng Trung, rồi nghe đáp án.",
         F(0, "Câu một: 为什么说高考是万千学子命运的转折点？ Vì sao nói thi đại học là bước ngoặt số phận của hàng triệu sĩ tử?"),
         F(1, "Đáp án: 因为十年寒窗苦读，一朝金榜题名，考上理想的大学，就能改变人生的道路。 Vì sau mười năm đèn sách, thi đỗ trường đại học lý tưởng là có thể thay đổi con đường đời."),
         F(2, "Câu hai: 高考移民分为哪两类？ Di dân thi đại học chia làm hai loại nào?"),
         F(3, "Đáp án: 一是移民到北上广等发达地区；二是移民到西藏、新疆、海南等欠发达地区。 Một là đến vùng phát triển như Bắc Kinh, Thượng Hải, Quảng Châu; hai là đến vùng kém phát triển như Tây Tạng, Tân Cương, Hải Nam."),
         F(4, "Câu ba: 为什么西藏、新疆等地的高考实际录取率高？ Vì sao tỷ lệ trúng tuyển thực tế ở Tây Tạng, Tân Cương cao?"),
         F(5, "Đáp án: 因为有民族优待政策，招生名额较多，加之当地人口较少。 Vì có chính sách ưu đãi dân tộc, chỉ tiêu nhiều, cộng thêm dân số địa phương ít.")])

add("bullets", section="Đọc hiểu 课文理解", title="Câu hỏi đọc hiểu (2)", reveal=True, size=33,
    items=["(4) 2001年北京和山东的例子说明了什么？",
           "Đáp án: 同样的试卷、同样的分数，只因户籍不同，上的大学便有天壤之别，说明各地区之间存在不公平。",
           "(5) 作者为什么说自主命题“巧妙”地掩盖了不公平？",
           "Đáp án: 因为考卷不一样，各地分数线不再具有可比性，不公平看不出来了，但教育资源不均衡的现实并没有改变。",
           "(6) 作者认为应该怎样解决“高考移民”问题？",
           "Đáp án: 不能只靠围追堵截；当务之急是深化高考改革，缩小地域间教育资源的差距，对症下药。"],
    say=[F(0, "Câu bốn: 二零零一年北京和山东的例子说明了什么？ Ví dụ về Bắc Kinh và Sơn Đông năm hai nghìn lẻ một cho thấy điều gì?"),
         F(1, "Đáp án: 同样的试卷、同样的分数，只因户籍不同，上的大学便有天壤之别，说明各地区之间存在不公平。 Cùng đề thi, cùng điểm số, chỉ vì hộ tịch khác nhau mà trường đại học được vào khác nhau một trời một vực, cho thấy giữa các vùng tồn tại sự bất công."),
         F(2, "Câu năm: 作者为什么说自主命题巧妙地掩盖了不公平？ Vì sao tác giả nói việc tự ra đề đã khéo léo che giấu sự bất công?"),
         F(3, "Đáp án: 因为考卷不一样，各地分数线不再具有可比性，不公平看不出来了，但教育资源不均衡的现实并没有改变。 Vì đề thi khác nhau nên điểm chuẩn không còn so sánh được, sự bất công không còn nhìn thấy, nhưng thực trạng tài nguyên giáo dục không đồng đều vẫn không thay đổi."),
         F(4, "Câu sáu: 作者认为应该怎样解决高考移民问题？ Theo tác giả, nên giải quyết vấn đề này thế nào?"),
         F(5, "Đáp án: 不能只靠围追堵截；当务之急是深化高考改革，缩小地域间教育资源的差距，对症下药。 Không thể chỉ dựa vào truy quét; việc cấp bách là cải cách thi đại học, thu hẹp khoảng cách tài nguyên giáo dục giữa các vùng, bốc thuốc đúng bệnh.")])

# ======================= MẪU CÂU TRỌNG ĐIỂM =======================
add("bullets", chapter="Mẫu câu: 可谓是 · 由于…且…加上 · 钻…的空子 · 意味着", section="Mẫu câu 重点句型", title="1. 可谓是 – có thể nói là", size=34,
    items=["Văn viết: có thể nói là, có thể gọi là – đưa ra một đánh giá, thường là khen ngợi hoặc nhấn mạnh",
           "“十年寒窗苦读，一朝金榜题名”，在中国，高考可谓是万千学子命运的转折点。",
           "12月27日小米手机的发布，可谓是2011年手机领域的一大亮点。",
           "这款新车在9月份一共卖出去12600辆，在同类车当中可谓是一马当先。"],
    say=["Bây giờ chúng ta sang phần mẫu câu và từ trọng điểm. Bài này có tám điểm.",
         F(0, "Điểm thứ nhất: 可谓是, nghĩa là có thể nói là, có thể gọi là. Đây là cách nói văn viết, dùng để đưa ra một đánh giá, thường là khen ngợi hoặc nhấn mạnh tầm quan trọng."),
         F(1, "Ví dụ một, trong bài khóa: 十年寒窗苦读，一朝金榜题名，在中国，高考可谓是万千学子命运的转折点。 Ở Trung Quốc, thi đại học có thể nói là bước ngoặt số phận của hàng triệu sĩ tử."),
         F(2, "Ví dụ hai: 十二月二十七日小米手机的发布，可谓是二零一一年手机领域的一大亮点。 Sự kiện ra mắt điện thoại Xiaomi ngày hai mươi bảy tháng mười hai có thể nói là một điểm sáng lớn của ngành điện thoại năm hai nghìn không trăm mười một. 亮点 là điểm sáng."),
         F(3, "Ví dụ ba: 这款新车在九月份一共卖出去一万二千六百辆，在同类车当中可谓是一马当先。 Mẫu xe mới này trong tháng chín bán được tổng cộng mười hai nghìn sáu trăm chiếc, có thể nói là dẫn đầu trong các dòng xe cùng loại. 一马当先 là một ngựa phi trước, dẫn đầu.")])

add("bullets", section="Mẫu câu 重点句型", title="2. 由于……，且……，加上…… – do…, hơn nữa…, cộng thêm…", size=34,
    items=["Chồng chất nhiều nguyên nhân; vế kết quả thường có 因此 · 所以",
           "由于中国幅员辽阔、考生众多，且各地区之间教育资源分配不均，加上现行高招制度的弊端，各省各地区的……都存在差异。",
           "由于他成绩不好，且不喜欢读书，加上家里还有妹妹弟弟要上学，所以他辍学去打工了。",
           "由于他名校毕业，且做事努力，加上很会说话，因此晋升得很快。"],
    say=["Điểm thứ hai: mẫu câu 由于……，且……，加上…….",
         F(0, "Mẫu này dùng để chồng chất nhiều nguyên nhân: do…, hơn nữa…, cộng thêm…. 且 là văn viết, nghĩa là hơn nữa, và. Vế kết quả phía sau thường có 因此 hoặc 所以."),
         F(1, "Ví dụ một, trong bài khóa: 由于中国幅员辽阔、考生众多，且各地区之间教育资源分配不均，加上现行高招制度的弊端，各省各地区的录取分数线等方面都存在差异。 Ba nguyên nhân dẫn đến một kết quả."),
         F(2, "Ví dụ hai: 由于他成绩不好，且不喜欢读书，加上家里还有妹妹弟弟要上学，所以他辍学去打工了。 Vì học kém, lại không thích học, cộng thêm ở nhà còn các em phải đi học, nên cậu ấy bỏ học đi làm thuê. 辍学 là bỏ học giữa chừng."),
         F(3, "Ví dụ ba: 由于他名校毕业，且做事努力，加上很会说话，因此晋升得很快。 Vì anh ấy tốt nghiệp trường danh tiếng, làm việc chăm chỉ, lại khéo ăn nói, nên thăng tiến rất nhanh. 晋升 là thăng chức.")])

add("bullets", section="Mẫu câu 重点句型", title="3. 钻……的空子 – lách kẽ hở của…", size=34,
    items=["Lợi dụng lỗ hổng, sơ hở, cơ hội để hành động (mang nghĩa chê); 钻 đọc thanh một",
           "因此，部分考生通过转学或迁移户口到……地区应考，钻高考政策的空子。",
           "多家企业钻政策空子，这导致当地药品生产、经营混乱。",
           "一旦税收制度不健全，就会有人想尽办法钻法律空子。"],
    say=["Điểm thứ ba: 钻……的空子.",
         F(0, "钻 là chui, khoan; 空子 là chỗ hở. 钻空子 là lách kẽ hở, lợi dụng lỗ hổng, sơ hở để hành động, luôn mang nghĩa chê. Chữ 钻 ở đây đọc thanh một. Có thể bỏ chữ 的: 钻政策空子，钻法律空子."),
         F(1, "Ví dụ một, trong bài khóa: 部分考生通过转学或迁移户口到分数线相对较低的地区应考，钻高考政策的空子。"),
         F(2, "Ví dụ hai: 多家企业钻政策空子，这导致当地药品生产、经营混乱。 Nhiều doanh nghiệp lách kẽ hở chính sách, dẫn đến việc sản xuất, kinh doanh thuốc ở địa phương hỗn loạn."),
         F(3, "Ví dụ ba: 一旦税收制度不健全，就会有人想尽办法钻法律空子。 Một khi chế độ thuế không hoàn thiện, sẽ có người tìm mọi cách lách luật. Tiếng Việt có từ rất sát: lách luật.")])

add("bullets", section="Mẫu câu 重点句型", title="4. 意味着 yìwèizhe – có nghĩa là, đồng nghĩa với", size=36,
    items=["Động từ: biểu thị, báo hiệu, đồng nghĩa với (= 代表 · 标志着); phủ định: 并不意味着",
           "有差异便意味着人员有流动的可能。",
           "教育部表示，购买学区房并不意味着能进优质学校。",
           "努力可能失败，但放弃则意味着永远不可能成功。"],
    say=["Điểm thứ tư: động từ 意味着.",
         F(0, "意味着 nghĩa là có nghĩa là, đồng nghĩa với, báo hiệu điều gì. Nó gần với 代表 và 标志着. Phủ định thường dùng 并不意味着, không có nghĩa là."),
         F(1, "Ví dụ một, trong bài khóa: 有差异便意味着人员有流动的可能。 Có chênh lệch thì có nghĩa là có khả năng người ta sẽ di chuyển."),
         F(2, "Ví dụ hai: 教育部表示，购买学区房并不意味着能进优质学校。 Bộ Giáo dục cho biết, mua nhà khu trường tốt không có nghĩa là vào được trường chất lượng cao. Câu này nối lại với bài một chấm hai."),
         F(3, "Ví dụ ba: 努力可能失败，但放弃则意味着永远不可能成功。 Cố gắng có thể thất bại, nhưng từ bỏ thì đồng nghĩa với việc vĩnh viễn không thể thành công. 则 là văn viết, nghĩa là thì.")])

add("bullets", chapter="Mẫu câu: 何苦 · 无非 · 远高于 · 给…以", section="Mẫu câu 重点句型", title="5. 何苦 hékǔ – hà tất phải khổ thế", size=36,
    items=["Phó từ: hỏi vặn, biểu thị không đáng; cuối câu thường có 呢; cũng nói 何苦来",
           "不然原本在家乡求学的考生，何苦舍近求远或背井离乡奔波到外省考试呢？",
           "你何苦在这些小事上伤脑筋呢，让孩子们去做吧。",
           "冒着这么大的雨赶去看电影，何苦呢？"],
    say=["Điểm thứ năm: phó từ 何苦.",
         F(0, "何苦 dùng giọng hỏi vặn để biểu thị việc gì đó không đáng làm, tự chuốc khổ vào thân. Cuối câu thường có 呢, cũng có thể nói 何苦来. Ở bài trước chúng ta đã học 何必, cần gì phải; 何苦 nhấn mạnh thêm ý khổ sở, không đáng."),
         F(1, "Ví dụ một, trong bài khóa: 不然原本在家乡求学的考生，何苦舍近求远或背井离乡奔波到外省考试呢？ Nếu không thì thí sinh hà tất phải rời quê bôn ba sang tỉnh khác thi?"),
         F(2, "Ví dụ hai: 你何苦在这些小事上伤脑筋呢，让孩子们去做吧。 Cậu cần gì phải đau đầu vì mấy chuyện nhỏ này, cứ để bọn trẻ làm đi."),
         F(3, "Ví dụ ba: 冒着这么大的雨赶去看电影，何苦呢？ Đội mưa to thế này để vội đi xem phim, khổ thế làm gì?")])

add("bullets", section="Mẫu câu 重点句型", title="6. 无非 wúfēi – chẳng qua là, chỉ là", size=36,
    items=["Phó từ: chỉ, không ngoài (thường nói giảm, nói nhẹ sự việc); hay dùng 无非是",
           "利用区域分数差来增强高考竞争力，无非是为了考入更理想的大学。",
           "我无非是想给他提个醒，没有别的意思。",
           "他这一番话，无非是在炫耀自己雄厚的财力。"],
    say=["Điểm thứ sáu: phó từ 无非.",
         F(0, "无非 nghĩa là chỉ, không ngoài, chẳng qua là. Người nói dùng nó khi muốn nói giảm, nói nhẹ sự việc, hoặc vạch ra mục đích thật sự. Hay dùng 无非是."),
         F(1, "Ví dụ một, trong bài khóa: 利用区域分数差来增强高考竞争力，无非是为了考入更理想的大学。 Chẳng qua là để vào được trường đại học lý tưởng hơn."),
         F(2, "Ví dụ hai: 我无非是想给他提个醒，没有别的意思。 Tôi chẳng qua chỉ muốn nhắc anh ấy một chút, không có ý gì khác. 提个醒 là nhắc nhở."),
         F(3, "Ví dụ ba: 他这一番话，无非是在炫耀自己雄厚的财力。 Những lời anh ta nói chẳng qua là để khoe khoang tài lực hùng hậu của mình. 炫耀 là khoe khoang.")])

add("bullets", section="Mẫu câu 重点句型", title="7. 远高于 · 8. 给……以 – cao hơn nhiều so với · đem lại cho… cái…", size=33,
    items=["## 远高于: cao hơn nhiều so với (văn viết; trái nghĩa: 远低于)",
           "这样一来，其高考实际录取率远高于河南、河北等人口大省，而竞争压力小得多。",
           "非洲移动手机的普及率远高于互联网的普及率。",
           "## 给 + người + 以 + danh từ trừu tượng: đem lại, dành cho ai cái gì (văn viết)",
           "这一制度的本意是……，但它确实给想走捷径的考生以可乘之机。",
           "人非圣贤，谁都会犯错，要给孩子以改正的机会。"],
    say=["Hai điểm cuối cùng: 远高于 và 给……以.",
         F(0, "远高于 nghĩa là cao hơn nhiều so với. 远 là xa, chỉ mức chênh lệch lớn; 于 là so với, văn viết. Trái nghĩa là 远低于."),
         F(1, "Ví dụ một, trong bài khóa: 其高考实际录取率远高于河南、河北等人口大省，而竞争压力小得多。 Tỷ lệ trúng tuyển thực tế cao hơn nhiều so với Hà Nam, Hà Bắc."),
         F(2, "Ví dụ hai: 非洲移动手机的普及率远高于互联网的普及率。 Ở châu Phi, tỷ lệ phổ cập điện thoại di động cao hơn nhiều so với tỷ lệ phổ cập internet."),
         F(3, "给……以…… là văn viết: đem lại cho ai một điều gì đó. Sau 以 thường là danh từ trừu tượng, như 机会，帮助，鼓励，可乘之机."),
         F(4, "Ví dụ một, trong bài khóa: 但它确实给想走捷径的考生以可乘之机。 Nhưng nó quả thực đã cho những thí sinh muốn đi đường tắt cơ hội để lợi dụng."),
         F(5, "Ví dụ hai: 人非圣贤，谁都会犯错，要给孩子以改正的机会。 Người đâu phải thánh hiền, ai cũng có lúc mắc lỗi, phải cho trẻ cơ hội sửa sai. 人非圣贤 là con người không phải thánh nhân.")])

add("compare", section="Mẫu câu 重点句型", title="Phân biệt 均衡 và 平衡",
    common="Đều có nghĩa là cân bằng; bài tập 2 có câu chọn giữa 平衡 · 均衡 · 平均 · 均匀",
    cols=[{"head": "均衡",
           "lines": ["Tính từ: phân bố đồng đều giữa các phần, các vùng",
                     "Đúng: 教育资源分配不均衡。",
                     "Đúng: 保持健康要均衡饮食。"]},
          {"head": "平衡",
           "lines": ["Hai bên ngang nhau; còn làm động từ, mang tân ngữ",
                     "Đúng: 骑车时他失去了平衡。",
                     "Sai: 我很难均衡工作和家庭。 → 平衡"]}],
    say=["Bài tập hai của sách có một câu chọn giữa 平衡，均衡，平均，均匀. Vì vậy chúng ta phân biệt hai từ hay gặp nhất: 均衡 và 平衡.",
         F(0, "均衡 là tính từ, nhấn mạnh sự phân bố đồng đều giữa các phần, các vùng. Ví dụ: 教育资源分配不均衡, tài nguyên giáo dục phân bổ không đồng đều; 保持健康要均衡饮食, muốn giữ sức khỏe phải ăn uống cân đối, đủ các nhóm chất."),
         F(1, "Còn 平衡 nhấn mạnh hai bên ngang nhau, giữ được thăng bằng, và còn làm động từ mang tân ngữ. Ví dụ: 骑车时他失去了平衡, khi đạp xe anh ấy bị mất thăng bằng; 心理不平衡, trong lòng thấy không cân bằng, tức là ấm ức."),
         F(1, "Vì vậy câu 我很难均衡工作和家庭 là sai, phải nói 我很难平衡工作和家庭, tôi rất khó cân bằng công việc và gia đình. Ngoài ra, 平均 là bình quân, 均匀 là đều đặn, như 呼吸均匀, hơi thở đều.")])

# ======================= KẾT HỢP TỪ =======================
add("bullets", chapter="Kết hợp từ", section="Kết hợp từ 词语搭配", title="Kết hợp từ (1): 弊端 · 均衡 · 匮乏", size=34,
    items=["## 弊端: 经营～ · 揭露～ · 扫除～ · 政治～",
           "鲁迅以笔做刀枪，淋漓尽致地揭露了旧社会的弊端。",
           "## 均衡: 水平～ · 势力～ · 营养～ · 保持～",
           "在青少年长身体的阶段，最重要的是营养均衡、适度锻炼及充足的睡眠。",
           "## 匮乏: 资源～ · 物质～ · 精神～ · 人才～",
           "上个世纪七十年代的中国乡村，物资匮乏，很多人家吃不饱。"],
    say=["Tiếp theo là phần 词语搭配, kết hợp từ.",
         F(0, "弊端 đi với 经营，揭露，扫除，政治: mặt trái trong kinh doanh, vạch trần mặt trái, quét sạch tệ hại, tệ hại chính trị."),
         F(1, "Ví dụ: 鲁迅以笔做刀枪，淋漓尽致地揭露了旧社会的弊端。 Lỗ Tấn lấy ngòi bút làm gươm súng, vạch trần một cách sâu sắc những tệ hại của xã hội cũ. 淋漓尽致 là đầy đủ, triệt để."),
         F(2, "均衡 đi với 水平，势力，营养，保持: trình độ đồng đều, cân bằng thế lực, dinh dưỡng cân đối, giữ cân bằng."),
         F(3, "Ví dụ: 在青少年长身体的阶段，最重要的是营养均衡、适度锻炼及充足的睡眠。 Trong giai đoạn thanh thiếu niên đang lớn, quan trọng nhất là dinh dưỡng cân đối, tập luyện vừa phải và ngủ đủ giấc."),
         F(4, "匮乏 đi với 资源，物质，精神，人才: thiếu tài nguyên, thiếu vật chất, nghèo nàn về tinh thần, thiếu nhân tài."),
         F(5, "Ví dụ: 上个世纪七十年代的中国乡村，物资匮乏，很多人家吃不饱。 Nông thôn Trung Quốc những năm bảy mươi của thế kỷ trước vật tư thiếu thốn, nhiều nhà không đủ ăn.")])

add("bullets", section="Kết hợp từ 词语搭配", title="Kết hợp từ (2): 挤占 · 率先 · 掩盖", size=34,
    items=["## 挤占 + N: ～资源 · ～空间 · ～位置 · ～份额",
           "我开车进小区时，发现通道被其他车辆挤占，只好绕道而行。",
           "## 率先 + V: ～开启 · ～推出 · ～表态 · ～采用",
           "这家酒店由于率先推出微笑服务而走红。",
           "## 掩盖 + N: ～真相 · ～罪行 · ～目的 · ～面目",
           "他们千方百计做假材料，企图掩盖犯罪事实。"],
    say=[F(0, "挤占 đi với 资源，空间，位置，份额: chiếm mất tài nguyên, không gian, vị trí, thị phần."),
         F(1, "Ví dụ: 我开车进小区时，发现通道被其他车辆挤占，只好绕道而行。 Khi lái xe vào khu dân cư, tôi thấy lối đi bị xe khác chiếm mất, đành đi đường vòng."),
         F(2, "率先 đứng trước động từ: 率先开启，率先推出，率先表态，率先采用, đi đầu mở ra, đi đầu tung ra, là người đầu tiên bày tỏ thái độ, đi đầu áp dụng. Chữ đầu đọc là shuài."),
         F(3, "Ví dụ: 这家酒店由于率先推出微笑服务而走红。 Khách sạn này nổi tiếng nhờ đi đầu đưa ra dịch vụ nụ cười. 走红 là nổi tiếng, được ưa chuộng."),
         F(4, "掩盖 đi với 真相，罪行，目的，面目: che giấu sự thật, tội ác, mục đích, bộ mặt thật."),
         F(5, "Ví dụ: 他们千方百计做假材料，企图掩盖犯罪事实。 Bọn họ tìm mọi cách làm giả tài liệu, hòng che giấu hành vi phạm tội. 企图 là âm mưu, toan tính.")])

# ======================= THÀNH NGỮ =======================
add("bullets", chapter="Thành ngữ & quán ngữ", section="Thành ngữ 成语", title="Thành ngữ (1): 前程似锦 · 想方设法 · 投机取巧 · 显而易见", size=33,
    items=["## 前程似锦 – tiền đồ rực rỡ như gấm (thường dùng để chúc)",
           "衷心祝你金榜题名，前程似锦。",
           "## 想方设法 – nghĩ đủ mọi cách",
           "这件事太紧急了，他正在想方设法联络各个部门处理。",
           "## 投机取巧 – lợi dụng thời cơ, giở mánh khóe để kiếm lợi",
           "做学问需要扎扎实实下工夫，一步一个脚印，不允许投机取巧。",
           "## 显而易见 – rõ ràng, dễ thấy",
           "这个道理显而易见，谁都明白。"],
    say=["Bài này có mười bốn thành ngữ và quán ngữ, thầy chia thành bốn nhóm.",
         F(0, "前程似锦: tiền đồ như gấm hoa, tức tương lai rực rỡ. Thường dùng trong lời chúc."),
         F(1, "Ví dụ: 衷心祝你金榜题名，前程似锦。 Chân thành chúc bạn đỗ đạt, tiền đồ rộng mở."),
         F(2, "想方设法: nghĩ hết mọi cách, tìm đủ mọi cách."),
         F(3, "Ví dụ: 这件事太紧急了，他正在想方设法联络各个部门处理。 Việc này gấp quá, anh ấy đang tìm mọi cách liên hệ các bộ phận để xử lý."),
         F(4, "投机取巧: lợi dụng thời cơ, lách kẽ hở, giở mánh khóe để kiếm lợi; cũng chỉ dùng mẹo vặt để được lợi. Mang nghĩa chê."),
         F(5, "Ví dụ: 做学问需要扎扎实实下工夫，一步一个脚印，不允许投机取巧。 Làm học vấn cần bỏ công sức vững chắc, đi bước nào chắc bước ấy, không được phép mánh lới."),
         F(6, "显而易见: rõ ràng, nhìn là thấy ngay."),
         F(7, "Ví dụ: 这个道理显而易见，谁都明白。 Đạo lý này rõ như ban ngày, ai cũng hiểu.")])

add("bullets", section="Thành ngữ 成语", title="Thành ngữ (2): 舍近求远 · 背井离乡 · 可乘之机 · 插一脚", size=33,
    items=["## 舍近求远 – bỏ gần tìm xa",
           "这种东西我们本地也出产，无需舍近求远到外地去购买。",
           "## 背井离乡 – rời bỏ quê hương đến nơi khác",
           "他们中许多人因为贫穷，不得已背井离乡到城里打工谋生。",
           "## 可乘之机 – cơ hội, sơ hở có thể lợi dụng",
           "我们要提高警惕，不给坏人以可乘之机。",
           "## 插一脚 (tục ngữ) – chen chân vào, can dự vào việc người khác",
           "这是他们夫妻俩的私事，我们外人何必去插一脚呢？"],
    say=[F(0, "舍近求远: bỏ cái gần, tìm cái xa; ví làm việc đi đường vòng hoặc theo đuổi điều không thực tế."),
         F(1, "Ví dụ: 这种东西我们本地也出产，无需舍近求远到外地去购买。 Thứ này địa phương mình cũng sản xuất, không cần bỏ gần tìm xa, đi nơi khác mua."),
         F(2, "背井离乡: rời giếng làng, xa quê hương, tức là rời quê đến nơi khác sinh sống. Chữ đầu đọc thanh bốn."),
         F(3, "Ví dụ: 他们中许多人因为贫穷，不得已背井离乡到城里打工谋生。 Nhiều người trong số họ vì nghèo mà bất đắc dĩ phải rời quê lên thành phố làm thuê kiếm sống."),
         F(4, "可乘之机: cơ hội có thể lợi dụng. Hay dùng với 给……以: 给……以可乘之机, như trong bài khóa."),
         F(5, "Ví dụ: 我们要提高警惕，不给坏人以可乘之机。 Chúng ta phải nâng cao cảnh giác, không cho kẻ xấu cơ hội lợi dụng."),
         F(6, "插一脚: quán ngữ, nghĩa là chen một chân vào, tham gia hoặc can thiệp vào việc của người khác."),
         F(7, "Ví dụ: 这是他们夫妻俩的私事，我们外人何必去插一脚呢？ Đây là chuyện riêng của vợ chồng họ, người ngoài như chúng ta cần gì phải chen vào?")])

add("bullets", section="Thành ngữ 成语", title="Thành ngữ (3): 天壤之别 · 围追堵截 · 治标不治本", size=33,
    items=["## 天壤之别 – khác nhau như trời với đất",
           "自信和自负只差一个字，意思却有天壤之别。",
           "## 围追堵截 – bao vây, truy đuổi, chặn đánh; (nghĩa rộng) truy quét triệt để",
           "由于记者围追堵截，从下车到会场的短短几百米，他走了将近半小时。",
           "## 治标不治本 – chữa ngọn không chữa gốc (标: ngọn cây)",
           "只靠邮箱拦截垃圾邮件其实是治标不治本的。"],
    say=[F(0, "天壤之别: 天 là trời, 壤 là đất. Khác nhau như trời với đất, một trời một vực."),
         F(1, "Ví dụ: 自信和自负只差一个字，意思却有天壤之别。 Tự tin và tự phụ chỉ khác nhau một chữ, nhưng nghĩa thì khác một trời một vực."),
         F(2, "围追堵截: vốn là một cách tác chiến, bao vây, truy đuổi, chặn đánh kẻ địch; sau mở rộng chỉ việc tiêu diệt, ngăn chặn triệt để một người hay việc gì đó."),
         F(3, "Ví dụ: 由于记者围追堵截，从下车到会场的短短几百米，他走了将近半小时。 Vì phóng viên vây kín, quãng đường vài trăm mét từ xe đến hội trường mà anh ấy đi mất gần nửa tiếng."),
         F(4, "治标不治本: chữ 标 là ngọn cây, chỉ những chi tiết bề ngoài; 本 là gốc. Chỉ xử lý tạm thời phần lộ ra bên ngoài, không giải quyết từ gốc. Tiếng Việt nói y hệt: chữa ngọn không chữa gốc."),
         F(5, "Ví dụ: 只靠邮箱拦截垃圾邮件其实是治标不治本的。 Chỉ dựa vào hộp thư chặn thư rác thực ra là chữa ngọn không chữa gốc.")])

add("bullets", section="Thành ngữ 成语", title="Thành ngữ (4): 高枕无忧 · 当务之急 · 对症下药", size=33,
    items=["## 高枕无忧 – kê cao gối ngủ yên, không phải lo lắng gì",
           "你别以为得到金牌就可以高枕无忧了，未来的路很长，还需要继续努力啊！",
           "## 当务之急 – việc cấp bách nhất trước mắt",
           "事到如今，再去追究谁的责任已无太大意义，当务之急是找出解决的方法。",
           "## 对症下药 – bốc thuốc đúng bệnh: dùng biện pháp phù hợp với tình hình cụ thể",
           "只有摸清情况，对症下药，才能有效地解决问题。"],
    say=[F(0, "高枕无忧: gối đầu thật cao mà ngủ, không phải lo lắng gì; ví sự yên ổn, không có gì phải bận tâm."),
         F(1, "Ví dụ: 你别以为得到金牌就可以高枕无忧了，未来的路很长，还需要继续努力啊！ Đừng tưởng có huy chương vàng là có thể kê cao gối ngủ yên, con đường phía trước còn dài, phải tiếp tục cố gắng!"),
         F(2, "当务之急: trong những việc cần làm hiện nay, đây là việc gấp nhất. Chữ đầu đọc thanh một."),
         F(3, "Ví dụ: 事到如今，再去追究谁的责任已无太大意义，当务之急是找出解决的方法。 Sự đã đến nước này, truy cứu trách nhiệm của ai cũng chẳng còn mấy ý nghĩa, việc cấp bách là tìm ra cách giải quyết."),
         F(4, "对症下药: 症 là bệnh, 下药 là cho thuốc. Bốc thuốc đúng bệnh, tức là dùng biện pháp phù hợp với tình hình cụ thể."),
         F(5, "Ví dụ: 只有摸清情况，对症下药，才能有效地解决问题。 Chỉ có nắm rõ tình hình, bốc thuốc đúng bệnh, mới giải quyết vấn đề hiệu quả. Đoạn kết bài khóa dùng liền bốn thành ngữ: 围追堵截，治标不治本，高枕无忧，当务之急, rồi kết bằng 对症下药. Đây là đặc điểm của văn bình luận tiếng Trung.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 趁热打铁", title="Bài tập 1: Chọn từ điền vào chỗ trống (1)", reveal=True, size=34,
    items=["## Từ cho sẵn: 掩盖 · 奔波 · 插一脚 · 天壤之别 · 当务之急 · 背井离乡 · 想方设法",
           "(1) 年轻的时候，他常年在外___，退休之后终于可以过舒服日子了。",
           "Đáp án: 奔波",
           "(2) 我们兄弟俩的性格，简直是___，我胆小老实，他热情幽默。",
           "Đáp án: 天壤之别",
           "(3) 在记者们的努力下，大家终于了解到了被___的事件真相。",
           "Đáp án: 掩盖",
           "(4) 湖水达到了危险水位，政府正___降低湖水水位，不然后果将不堪设想。",
           "Đáp án: 想方设法"],
    say=["Bây giờ là phần luyện tập của sách, 趁热打铁. Bài tập một: chọn từ cho sẵn điền vào chỗ trống.",
         F(0, "Có bảy từ: 掩盖，奔波，插一脚，天壤之别，当务之急，背井离乡，想方设法."),
         F(1, "Câu một: 年轻的时候，他常年在外什么，退休之后终于可以过舒服日子了。 Hồi trẻ, ông ấy quanh năm… bên ngoài, nghỉ hưu rồi cuối cùng cũng được sống thoải mái. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 奔波. 常年在外奔波, quanh năm bôn ba xa nhà."),
         F(3, "Câu hai: 我们兄弟俩的性格，简直是什么，我胆小老实，他热情幽默。 Tính cách hai anh em tôi đúng là…, tôi nhút nhát thật thà, còn cậu ấy nhiệt tình hài hước."),
         F(4, "Đáp án: 天壤之别, khác nhau một trời một vực."),
         F(5, "Câu ba: 在记者们的努力下，大家终于了解到了被什么的事件真相。 Nhờ nỗ lực của các phóng viên, mọi người cuối cùng đã biết được sự thật bị… của sự việc."),
         F(6, "Đáp án: 掩盖. 被掩盖的真相, sự thật bị che giấu. Đây chính là kết hợp 掩盖真相."),
         F(7, "Câu bốn: 湖水达到了危险水位，政府正什么降低湖水水位，不然后果将不堪设想。 Nước hồ đã đến mức nguy hiểm, chính quyền đang… hạ mực nước, nếu không hậu quả sẽ khôn lường."),
         F(8, "Đáp án: 想方设法, tìm mọi cách. 不堪设想 là không dám tưởng tượng, khôn lường.")])

add("bullets", section="Luyện tập 趁热打铁", title="Bài tập 1: Chọn từ điền vào chỗ trống (2)", reveal=True, size=36,
    items=["## Từ cho sẵn: 掩盖 · 奔波 · 插一脚 · 天壤之别 · 当务之急 · 背井离乡 · 想方设法",
           "(5) 战争造成了多少人___，无家可归啊！",
           "Đáp án: 背井离乡",
           "(6) 普及九年义务教育，是发展中国教育事业的___。",
           "Đáp án: 当务之急",
           "(7) 这片空地各大公司早就盯上了，哪还轮得到我们___！",
           "Đáp án: 插一脚"],
    say=[F(1, "Câu năm: 战争造成了多少人什么，无家可归啊！ Chiến tranh đã khiến biết bao người…, không nhà để về!"),
         F(2, "Đáp án: 背井离乡, rời bỏ quê hương. 无家可归 là không nhà để về."),
         F(3, "Câu sáu: 普及九年义务教育，是发展中国教育事业的什么。 Phổ cập giáo dục bắt buộc chín năm là… của việc phát triển sự nghiệp giáo dục Trung Quốc."),
         F(4, "Đáp án: 当务之急, việc cấp bách nhất."),
         F(5, "Câu bảy: 这片空地各大公司早就盯上了，哪还轮得到我们什么！ Mảnh đất trống này các công ty lớn đã nhắm từ lâu, làm gì đến lượt chúng ta…!"),
         F(6, "Đáp án: 插一脚. 哪还轮得到我们插一脚, làm gì đến lượt chúng ta chen chân vào. 盯上 là nhắm vào, để mắt tới.")])

add("bullets", section="Luyện tập 趁热打铁", title="Bài tập 2: Chọn đáp án đúng (1)", reveal=True, size=33,
    items=["(1) 搬到新校区后，同学们的居住条件明显（ ）了，然而一些同学对老校区的那份感情却一时放不下。\nA.替换  B.改变  C.改善  D.变更",
           "Đáp án: C – 改善: cải thiện (条件 tốt lên)",
           "(2) 如今，互联网已经成为大众讨论公共事务、表达利益（ ）、进行舆论监督的重要平台。\nA.要求  B.渴求  C.诉求  D.请求",
           "Đáp án: C – 利益诉求: nguyện vọng về lợi ích",
           "(3) 应考者要如实填写各项信息，不得有任何虚假（ ），否则学校有权要求学生退学。\nA.掩饰  B.掩盖  C.隐藏  D.隐瞒",
           "Đáp án: D – 隐瞒: giấu giếm thông tin, sự thật"],
    say=["Bài tập hai: chọn một đáp án đúng.",
         F(0, "Câu một: 搬到新校区后，同学们的居住条件明显什么了，然而一些同学对老校区的那份感情却一时放不下。 Chuyển sang cơ sở mới, điều kiện ăn ở của các bạn rõ ràng đã…, nhưng một số bạn vẫn chưa nguôi tình cảm với cơ sở cũ. Lựa chọn: 替换，改变，改善，变更."),
         F(1, "Đáp án: C, 改善, cải thiện, tức là trở nên tốt hơn. 改变 chỉ là thay đổi, không nói rõ tốt hay xấu; 替换 là thay thế; 变更 là thay đổi kế hoạch, thủ tục."),
         F(2, "Câu hai: 如今，互联网已经成为大众讨论公共事务、表达利益什么、进行舆论监督的重要平台。 Ngày nay internet đã trở thành nền tảng quan trọng để công chúng bàn luận việc công, bày tỏ… về lợi ích, giám sát bằng dư luận. Lựa chọn: 要求，渴求，诉求，请求."),
         F(3, "Đáp án: C, 诉求. 利益诉求 là kết hợp cố định, nguyện vọng về lợi ích. 渴求 là khao khát; 请求 là thỉnh cầu."),
         F(4, "Câu ba: 应考者要如实填写各项信息，不得有任何虚假什么，否则学校有权要求学生退学。 Thí sinh phải điền trung thực các thông tin, không được có bất kỳ sự gian dối…, nếu không nhà trường có quyền buộc thôi học. Lựa chọn: 掩饰，掩盖，隐藏，隐瞒."),
         F(5, "Đáp án: D, 隐瞒, giấu giếm thông tin, sự thật không cho người khác biết. Cụm 虚假隐瞒 hay gặp trong các văn bản khai báo. 掩饰 thường là che giấu cảm xúc, khuyết điểm; 掩盖 là che đậy sự thật, tội lỗi; 隐藏 là cất giấu đồ vật, ẩn mình.")])

add("bullets", section="Luyện tập 趁热打铁", title="Bài tập 2: Chọn đáp án đúng (2)", reveal=True, size=34,
    items=["(4) 保持健康，很重要的一点是（ ）饮食，不能挑食，也不能暴饮暴食。\nA.平衡  B.均衡  C.平均  D.均匀",
           "Đáp án: B – 均衡饮食: ăn uống cân đối",
           "(5) 在几轮投票中，克拉克一路遥遥（ ）。\nA.首先  B.抢先  C.领先  D.率先",
           "Đáp án: C – 遥遥领先: bỏ xa đối thủ, dẫn trước rất xa"],
    say=[F(0, "Câu bốn: 保持健康，很重要的一点是什么饮食，不能挑食，也不能暴饮暴食。 Giữ gìn sức khỏe, một điều rất quan trọng là ăn uống…, không được kén ăn, cũng không được ăn uống vô độ. Lựa chọn: 平衡，均衡，平均，均匀."),
         F(1, "Đáp án: B, 均衡. 均衡饮食 là ăn uống cân đối, đủ các nhóm chất, đúng như chúng ta vừa phân biệt. 暴饮暴食 là ăn uống quá độ."),
         F(2, "Câu năm: 在几轮投票中，克拉克一路遥遥什么。 Qua mấy vòng bỏ phiếu, Clark luôn… rất xa. Lựa chọn: 首先，抢先，领先，率先."),
         F(3, "Đáp án: C, 领先. 遥遥领先 là kết hợp cố định, nghĩa là dẫn trước rất xa. 率先 là đi đầu làm việc gì, đứng trước động từ; 抢先 là tranh làm trước; 首先 là trước hết.")])

add("bullets", section="Luyện tập 趁热打铁", title="Bài tập 2: Chọn đáp án đúng (3)", reveal=True, size=34,
    items=["(6) 这是一个经济非常发达的国家，但是面临着资源（ ）的窘境。\nA.缺少  B.匮乏  C.欠缺  D.贫乏",
           "Đáp án: B – 资源匮乏: tài nguyên thiếu thốn",
           "(7) 我们看问题要全面，要一分为二，不要因为人家有（ ），就认为人家一无是处。\nA.弊端  B.缺点  C.缺陷  D.后端",
           "Đáp án: B – 缺点: khuyết điểm (của người)"],
    say=[F(0, "Câu sáu: 这是一个经济非常发达的国家，但是面临着资源什么的窘境。 Đây là một nước kinh tế rất phát triển, nhưng đang đối mặt với tình cảnh tài nguyên…. Lựa chọn: 缺少，匮乏，欠缺，贫乏."),
         F(1, "Đáp án: B, 匮乏. 资源匮乏 là kết hợp các bạn vừa học. 缺少 là động từ, thường cần tân ngữ phía sau, như 缺少资源; 欠缺 hay dùng cho kinh nghiệm, năng lực; 贫乏 hay dùng cho tri thức, ngôn ngữ, như 知识贫乏. 窘境 là tình cảnh khó khăn."),
         F(2, "Câu bảy: 我们看问题要全面，要一分为二，不要因为人家有什么，就认为人家一无是处。 Nhìn vấn đề phải toàn diện, phải thấy cả hai mặt, đừng vì người ta có… mà cho rằng người ta chẳng ra gì. Lựa chọn: 弊端，缺点，缺陷，后端."),
         F(3, "Đáp án: B, 缺点, khuyết điểm. Ở đây nói về con người, nên dùng 缺点. 弊端 dùng cho chế độ, cách làm; 缺陷 là khiếm khuyết của cơ thể hay sản phẩm; 后端 là phần phía sau, không hợp. 一无是处 là chẳng có điểm nào tốt.")])

add("bullets", section="Luyện tập 趁热打铁", title="Bài tập 3: Dùng từ cho sẵn trả lời câu hỏi (1)", reveal=True, size=33,
    items=["(1) “高考移民”现象出现的原因是什么？（由于……，且……，加上……，因此/所以……）",
           "Đáp án gợi ý: 由于中国考生众多，且各地区教育资源分配不均，加上各省录取分数线和招生名额不同，因此出现了“高考移民”。",
           "(2) “高考移民”的手段是什么？（钻……的空子）",
           "Đáp án gợi ý: 他们通过转学或迁移户口，到分数线较低、录取率较高的地区应考，钻高考政策的空子。"],
    say=["Bài tập ba: dùng từ và mẫu câu cho sẵn để trả lời câu hỏi. Các bạn hãy tự trả lời trước, rồi nghe đáp án gợi ý.",
         F(0, "Câu một, dùng mẫu 由于……，且……，加上……，因此: 高考移民现象出现的原因是什么？ Nguyên nhân của hiện tượng di dân thi đại học là gì?"),
         F(1, "Đáp án gợi ý: 由于中国考生众多，且各地区教育资源分配不均，加上各省录取分数线和招生名额不同，因此出现了高考移民。 Do thí sinh đông, tài nguyên giáo dục phân bổ không đều, cộng thêm điểm chuẩn và chỉ tiêu mỗi tỉnh khác nhau, nên mới có di dân thi đại học."),
         F(2, "Câu hai, dùng 钻……的空子: 高考移民的手段是什么？ Thủ đoạn của di dân thi đại học là gì?"),
         F(3, "Đáp án gợi ý: 他们通过转学或迁移户口，到分数线较低、录取率较高的地区应考，钻高考政策的空子。 Họ chuyển trường hoặc chuyển hộ khẩu đến vùng có điểm chuẩn thấp, tỷ lệ trúng tuyển cao để dự thi, lách kẽ hở của chính sách thi đại học.")])

add("bullets", section="Luyện tập 趁热打铁", title="Bài tập 3: Dùng từ cho sẵn trả lời câu hỏi (2)", reveal=True, size=32,
    items=["(3) 2001年，同样试卷、同样分数的北京考生和山东考生，考入的大学一样吗？（天壤之别）",
           "Đáp án gợi ý: 不一样，有天壤之别。北京文科一本线只有454分，山东却高达580分，同样考460分，在北京能上一本，在山东却上不了。",
           "(4) 为什么说高考移民者在当地参加高考，对当地人不公平？（插一脚）",
           "Đáp án gợi ý: 因为录取名额有限度，高考移民变更户籍后插一脚进来抢饭吃，挤占了当地人上大学的名额。",
           "(5) 高考移民学生为什么要千方百计地迁移户口，到异地求学应考？（无非）",
           "Đáp án gợi ý: 无非是为了利用区域分数差，增强竞争力，考入更理想的大学。"],
    say=[F(0, "Câu ba, dùng 天壤之别: 二零零一年，同样试卷、同样分数的北京考生和山东考生，考入的大学一样吗？ Năm hai nghìn lẻ một, thí sinh Bắc Kinh và Sơn Đông cùng đề thi, cùng điểm số, có vào cùng loại trường không?"),
         F(1, "Đáp án gợi ý: 不一样，有天壤之别。北京文科一本线只有四百五十四分，山东却高达五百八十分，同样考四百六十分，在北京能上一本，在山东却上不了。 Không giống, khác một trời một vực: cùng bốn trăm sáu mươi điểm, ở Bắc Kinh vào được trường nhóm một, ở Sơn Đông thì không."),
         F(2, "Câu bốn, dùng 插一脚: 为什么说高考移民者在当地参加高考，对当地人不公平？ Vì sao nói người di dân thi đại học dự thi ở địa phương là bất công với người địa phương?"),
         F(3, "Đáp án gợi ý: 因为录取名额有限度，高考移民变更户籍后插一脚进来抢饭吃，挤占了当地人上大学的名额。 Vì chỉ tiêu có hạn, người di dân đổi hộ tịch rồi chen chân vào tranh bát cơm, chiếm mất chỉ tiêu của người địa phương."),
         F(4, "Câu năm, dùng 无非: 高考移民学生为什么要千方百计地迁移户口，到异地求学应考？ Vì sao học sinh di dân thi đại học tìm mọi cách chuyển hộ khẩu, sang nơi khác học và thi?"),
         F(5, "Đáp án gợi ý: 无非是为了利用区域分数差，增强竞争力，考入更理想的大学。 Chẳng qua là để lợi dụng chênh lệch điểm giữa các vùng, tăng sức cạnh tranh, vào được trường đại học lý tưởng hơn.")])

add("bullets", section="Luyện tập 趁热打铁", title="Bài tập 4: Chọn từ điền vào đoạn văn", reveal=True, size=33,
    items=["## Từ cho sẵn: 如此一来 · 享有盛誉 · 砸锅卖铁 · 相差无几 · 雄厚 · 自然而然",
           "“再苦不能苦孩子，再穷不能穷教育”，在中国父母观念中，就算家里一贫如洗，___也会送孩子上学，中国人重视教育的程度可想而知。以前如果孩子能考上一所___的大学，毕业后就能改善生活，___地改变个人和家庭的命运。这其实与“书中自有黄金屋”的观念___。然而，当今社会，如果一个家庭没有较为___的财力，孩子根本不可能享受优质的教育资源，___，寒门再难出贵子。",
           "Đáp án: 砸锅卖铁 · 享有盛誉 · 自然而然 · 相差无几 · 雄厚 · 如此一来"],
    say=["Bài tập bốn: chọn từ cho sẵn điền vào đoạn văn. Các bạn để ý, tất cả các từ này đều học ở bài một chấm hai, đây là bài ôn tập rất tốt.",
         F(0, "Có sáu từ: 如此一来，享有盛誉，砸锅卖铁，相差无几，雄厚，自然而然."),
         F(1, "Đoạn văn như sau: 再苦不能苦孩子，再穷不能穷教育，在中国父母观念中，就算家里一贫如洗，什么也会送孩子上学，中国人重视教育的程度可想而知。以前如果孩子能考上一所什么的大学，毕业后就能改善生活，什么地改变个人和家庭的命运。这其实与书中自有黄金屋的观念什么。然而，当今社会，如果一个家庭没有较为什么的财力，孩子根本不可能享受优质的教育资源，什么，寒门再难出贵子。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 砸锅卖铁也会送孩子上学；一所享有盛誉的大学；自然而然地改变个人和家庭的命运；与书中自有黄金屋的观念相差无几；较为雄厚的财力；如此一来，寒门再难出贵子."),
         F(2, "Cả đoạn nghĩa là: Khổ mấy cũng không để con khổ, nghèo mấy cũng không để giáo dục nghèo. Trong quan niệm của cha mẹ Trung Quốc, dù nhà nghèo rớt mồng tơi, có bán cả gia tài cũng cho con đi học. Trước kia, con thi đỗ một trường đại học danh tiếng thì tốt nghiệp xong có thể cải thiện cuộc sống, tự nhiên thay đổi số phận bản thân và gia đình; điều này chẳng khác mấy với quan niệm trong sách có nhà vàng. Thế nhưng xã hội ngày nay, nếu gia đình không có tài lực khá hùng hậu, con cái hoàn toàn không thể hưởng tài nguyên giáo dục chất lượng cao; như vậy, nhà nghèo khó mà sinh con quý được nữa.")])

# ======================= THẢO LUẬN =======================
add("bullets", chapter="Thảo luận", section="Thảo luận 讨论", title="Thảo luận: Ai bị đụng đến “miếng phô mai”?", reveal=True, size=33,
    items=["(1) 你认为“高考移民”是钻空子，还是对教育不公平的反抗？",
           "Đáp án gợi ý: 高考移民确实钻了政策的空子，挤占了当地人的名额；但话又说回来，它背后的诱因是教育资源不均衡。只靠围追堵截是治标不治本的，当务之急是缩小地区差距。",
           "(2) 越南有没有类似的政策或现象？",
           "Đáp án gợi ý: 越南的大学招生对偏远地区、少数民族考生有优先加分政策，这和中国的民族优待政策有相似之处；怎样防止有人钻政策的空子，也是两国都要面对的问题。"],
    say=["Bây giờ chúng ta cùng thảo luận. Đây cũng chính là đề tranh luận số ba trong phần ôn tập đơn vị.",
         F(0, "Câu hỏi một: 你认为高考移民是钻空子，还是对教育不公平的反抗？ Bạn cho rằng di dân thi đại học là lách kẽ hở, hay là sự phản kháng trước bất công giáo dục?"),
         F(1, "Gợi ý: 高考移民确实钻了政策的空子，挤占了当地人的名额；但话又说回来，它背后的诱因是教育资源不均衡。只靠围追堵截是治标不治本的，当务之急是缩小地区差距。 Di dân thi đại học đúng là lách kẽ hở, chiếm chỉ tiêu của người địa phương; nhưng nói đi cũng phải nói lại, nguyên nhân sâu xa là tài nguyên giáo dục không đồng đều. Chỉ truy quét là chữa ngọn, việc cấp bách là thu hẹp khoảng cách giữa các vùng."),
         F(2, "Câu hỏi hai: 越南有没有类似的政策或现象？ Việt Nam có chính sách hay hiện tượng tương tự không?"),
         F(3, "Gợi ý: 越南的大学招生对偏远地区、少数民族考生有优先加分政策，这和中国的民族优待政策有相似之处；怎样防止有人钻政策的空子，也是两国都要面对的问题。 Tuyển sinh đại học ở Việt Nam có điểm ưu tiên cho thí sinh vùng sâu vùng xa và người dân tộc thiểu số, khá giống chính sách ưu đãi dân tộc của Trung Quốc; làm sao ngăn người khác lách kẽ hở chính sách cũng là vấn đề cả hai nước phải đối mặt.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết bài 1.3", section="Tổng kết", title="Tổng kết bài 1.3", size=34,
    items=["Từ vựng trọng tâm: 可谓 · 转折 · 弊端 · 迁移 · 均衡 · 何苦 · 奔波 · 无非 · 欠发达 · 匮乏 · 捷径 · 凭借 · 挤占 · 委屈 · 效仿 · 掩盖 · 诉求 · 诱因 · 有望 · 终结",
           "Mẫu câu: 可谓是 · 由于……，且……，加上…… · 钻……的空子 · 意味着",
           "何苦……呢 · 无非是 · 远高于 · 给……以…… · phân biệt 均衡 / 平衡",
           "Thành ngữ: 前程似锦 · 想方设法 · 投机取巧 · 显而易见 · 舍近求远 · 背井离乡 · 可乘之机 · 插一脚 · 天壤之别 · 围追堵截 · 治标不治本 · 高枕无忧 · 当务之急 · 对症下药"],
    say=["Chúng ta cùng tổng kết bài một chấm ba.",
         F(0, "Về từ vựng, các bạn cần đặc biệt nhớ: 可谓，转折，弊端，迁移，均衡，何苦，奔波，无非，欠发达，匮乏，捷径，凭借，挤占，委屈，效仿，掩盖，诉求，诱因，有望，终结. Và đừng quên những từ dễ nhầm: 弊端，命题，终结."),
         F(1, "Về mẫu câu: 可谓是, có thể nói là; 由于……，且……，加上……, chồng chất nguyên nhân; 钻……的空子, lách kẽ hở; 意味着, có nghĩa là."),
         F(2, "Tiếp theo: 何苦……呢, hà tất phải khổ thế; 无非是, chẳng qua là; 远高于, cao hơn nhiều so với; 给……以……, đem lại cho ai cái gì; và phân biệt 均衡 với 平衡."),
         F(3, "Và mười bốn thành ngữ, quán ngữ. Văn bình luận tiếng Trung dùng thành ngữ rất dày đặc, các bạn nên học thuộc cả câu ví dụ để dùng được trong bài viết của mình.")])

# ======================= ÔN TẬP ĐƠN VỊ 1 =======================
add("bullets", chapter="Ôn tập đơn vị 1", section="Ôn tập 单元练习", title="Ôn tập Đơn vị 1 (教育篇): ba bài, ba vấn đề", size=33,
    items=["## 1.1 没有高考，你怎么拼得过富二代？ – thi đại học và cơ hội đổi đời của con nhà nghèo",
           "按说 · 未免 · 换一个角度 · 不只是……更是…… · 历来 · 偏偏 · 反倒 · 并非 · 无论如何……都",
           "## 1.2 学区房情结怎么破？ – nhà gần trường tốt, so sánh Trung Quốc và nước ngoài",
           "不尽然 · 乃至 · 越发 · 何以见得 · 不妨 · 话又说回来 · 区别在于 · 一则……二则…… · 如此一来",
           "## 1.3 “高考移民”动了谁的奶酪？ – công bằng giáo dục giữa các vùng",
           "可谓是 · 由于……且……加上…… · 钻……的空子 · 意味着 · 何苦 · 无非 · 给……以"],
    say=["Chúng ta đã học xong ba bài của Đơn vị một. Bây giờ là chương ôn tập đơn vị, theo phần 单元练习, học để dùng, 学以致用, của sách.",
         F(0, "Bài một chấm một: thi đại học và cơ hội đổi đời của con nhà nghèo, qua lời kể của 白岩松."),
         F(1, "Các mẫu câu: 按说，未免，换一个角度，不只是……更是……，历来，偏偏，反倒，并非，无论如何……都."),
         F(2, "Bài một chấm hai: nhà gần trường tốt, so sánh Trung Quốc và nước ngoài."),
         F(3, "Các mẫu câu: 不尽然，乃至，越发，何以见得，不妨，话又说回来，区别在于，一则……二则……，如此一来."),
         F(4, "Bài một chấm ba: di dân thi đại học và vấn đề công bằng giáo dục giữa các vùng."),
         F(5, "Các mẫu câu: 可谓是，由于……且……加上……，钻……的空子，意味着，何苦，无非，给……以. Ba bài cùng xoay quanh một chữ: 公平, công bằng trong giáo dục.")])

add("bullets", section="Ôn tập 单元练习", title="Ôn tập nhanh: chọn từ đã học trong đơn vị (1)", reveal=True, size=34,
    items=["## Từ cho sẵn: 不尽然 · 偏偏 · 何苦 · 越发 · 无非 · 并非",
           "(1) 都说名校毕业就一定能找到好工作，其实___。",
           "Đáp án: 不尽然",
           "(2) 大家都劝他报考本地的大学，他___要去外省。",
           "Đáp án: 偏偏",
           "(3) 你成绩这么好，___为了几分去当“高考移民”呢？",
           "Đáp án: 何苦"],
    say=["Trước hết, chúng ta làm một bài ôn tập nhanh với sáu từ của cả ba bài: 不尽然，偏偏，何苦，越发，无非，并非. Các bạn tạm dừng sau mỗi câu nhé.",
         F(1, "Câu một: 都说名校毕业就一定能找到好工作，其实什么。 Ai cũng nói tốt nghiệp trường danh tiếng là nhất định tìm được việc tốt, thực ra…."),
         F(2, "Đáp án: 不尽然. 其实不尽然, thực ra không hẳn vậy."),
         F(3, "Câu hai: 大家都劝他报考本地的大学，他什么要去外省。 Mọi người đều khuyên cậu ấy thi trường ở quê, cậu ấy… muốn sang tỉnh khác."),
         F(4, "Đáp án: 偏偏, lại cứ."),
         F(5, "Câu ba: 你成绩这么好，什么为了几分去当高考移民呢？ Thành tích cậu tốt thế, … vì mấy điểm mà đi di dân thi đại học?"),
         F(6, "Đáp án: 何苦, hà tất phải khổ thế. Chữ 呢 ở cuối câu là gợi ý.")])

add("bullets", section="Ôn tập 单元练习", title="Ôn tập nhanh: chọn từ đã học trong đơn vị (2)", reveal=True, size=34,
    items=["## Từ cho sẵn: 不尽然 · 偏偏 · 何苦 · 越发 · 无非 · 并非",
           "(4) 学区房的价格越来越高，家长们的焦虑也___严重了。",
           "Đáp án: 越发",
           "(5) 他每天学到半夜，___是想考上一所理想的大学。",
           "Đáp án: 无非",
           "(6) 高考___改变命运的唯一途径。",
           "Đáp án: 并非"],
    say=[F(1, "Câu bốn: 学区房的价格越来越高，家长们的焦虑也什么严重了。 Giá nhà khu trường tốt ngày càng cao, nỗi lo của phụ huynh cũng… nặng nề."),
         F(2, "Đáp án: 越发, càng thêm."),
         F(3, "Câu năm: 他每天学到半夜，什么是想考上一所理想的大学。 Ngày nào cậu ấy cũng học đến nửa đêm, … là muốn đỗ một trường đại học lý tưởng."),
         F(4, "Đáp án: 无非. 无非是, chẳng qua là."),
         F(5, "Câu sáu: 高考什么改变命运的唯一途径。 Thi đại học… con đường duy nhất để thay đổi số phận."),
         F(6, "Đáp án: 并非, hoàn toàn không phải. 高考并非改变命运的唯一途径.")])

add("bullets", section="Ôn tập 单元练习", title="Báo cáo · Ý kiến · Tranh luận (明察暗访 · 众说纷纭 · 针锋相对)", size=32,
    items=["## 明察暗访 – tìm hiểu, báo cáo",
           "报告一 应试教育 vs 素质教育 · 报告二 填报高考志愿时的考虑因素 · 报告三 如何给学区房降温？",
           "## 众说纷纭 – mỗi người một ý",
           "“本科选学校，硕士选专业，博士选导师” · 寒门学子输在了教育起跑线上？ · 电影《学区房72小时》（孟母三迁）",
           "## 针锋相对 – tranh luận",
           "高考能不能改变命运？ · 砸锅卖铁买学区到底值不值得？ · 打击“高考移民”，能有效维护教育公平吗？"],
    say=["Phần 单元练习 của sách có năm dạng hoạt động. Ba dạng đầu là báo cáo, nêu ý kiến và tranh luận.",
         F(0, "明察暗访 là tìm hiểu cả công khai lẫn ngấm ngầm, tức là tra cứu tài liệu hoặc khảo sát, rồi báo cáo ở buổi học sau."),
         F(1, "Có ba đề: báo cáo một, 应试教育 và 素质教育, giáo dục chạy theo thi cử và giáo dục toàn diện; báo cáo hai, những yếu tố cần cân nhắc khi đăng ký nguyện vọng; báo cáo ba, làm sao hạ nhiệt cơn sốt nhà gần trường. Sách cho biết ở Anh, điểm thi của trường tiểu học cứ tăng mười điểm thì giá nhà xung quanh tăng ba phẩy ba phần trăm."),
         F(2, "众说纷纭 là mỗi người một ý, các bạn nêu quan điểm của mình."),
         F(3, "Có ba chủ đề: câu nói 本科选学校，硕士选专业，博士选导师, đại học chọn trường, thạc sĩ chọn ngành, tiến sĩ chọn thầy; con nhà nghèo có thua ngay từ vạch xuất phát không; và bộ phim 学区房七十二小时, kể về một phó giáo sư phải bán nhà, mua nhà gần trường trong bảy mươi hai giờ. Câu thành ngữ đi kèm là 孟母三迁, mẹ Mạnh Tử ba lần chuyển nhà để chọn môi trường tốt cho con."),
         F(4, "针锋相对 là mũi kim đối nhau, tức là tranh luận đối đầu."),
         F(5, "Ba đề tranh luận: thi đại học có thay đổi được số phận không; dốc hết gia tài mua nhà gần trường có đáng không; và trấn áp di dân thi đại học có bảo vệ được công bằng giáo dục không. Ba đề này ứng với ba bài khóa, các bạn hãy dùng các mẫu câu đã học để chuẩn bị lập luận.")])

add("bullets", section="Ôn tập 单元练习", title="Viết bài so sánh (1): mở bài và điểm khác nhau", size=34,
    items=["## Mở bài (中心句 / 领起句)",
           "A 和 B 的不同在以下几个方面 · A 和 B 截然相反 / 大相径庭 / 有天壤之别",
           "两者之间的差异何在？ · 一般认为……，具体分析如下",
           "## Điểm khác nhau – triển khai: 首先…… · 其次…… · 再者…… · 最后……",
           "A……，而 B 则…… · A……。相比之下，B 则…… · B 没有 A……",
           "在……方面，A 和 B 有所区别 · 与 A 形成对比的是 B · 比起 A，B 更/愈加…… · 反观 B，……"],
    say=["Dạng thứ tư là 妙笔生花, ngòi bút nở hoa, tức là luyện viết. Đề viết thứ hai dạy cách viết một bài so sánh, rất thiết thực. Thầy tóm tắt các cấu trúc của sách.",
         F(0, "Phần một là câu chủ đề, mở bài."),
         F(1, "Ví dụ: A 和 B 的不同在以下几个方面, A và B khác nhau ở mấy mặt sau. Hoặc: A 和 B 截然相反, hoàn toàn trái ngược; 大相径庭, khác nhau rất xa; 有天壤之别, khác một trời một vực."),
         F(2, "Cũng có thể mở bằng câu hỏi: 两者之间的差异何在？ Sự khác biệt giữa hai bên nằm ở đâu? Hoặc: 一般认为……，具体分析如下, người ta thường cho rằng…, cụ thể phân tích như sau."),
         F(3, "Phần hai là nội dung so sánh, triển khai theo trình tự 首先，其次，再者，最后, trước hết, tiếp theo, hơn nữa, cuối cùng."),
         F(4, "Để nêu điểm khác: A……，而 B 则……, A thì…, còn B thì…; 相比之下，B 则……, so ra thì B lại…; B 没有 A……, B không bằng A."),
         F(5, "Hoặc: 在……方面，A 和 B 有所区别, về mặt…, A và B có sự khác biệt; 与 A 形成对比的是 B, đối lập với A là B; 比起 A，B 更……, so với A, B càng…; 反观 B, nhìn lại B. Các bạn để ý, mẫu 区别在于 ở bài một chấm hai cũng dùng rất tốt ở đây.")])

add("bullets", section="Ôn tập 单元练习", title="Viết bài so sánh (2): điểm giống, số liệu, kết luận", size=34,
    items=["## Điểm giống nhau",
           "A 和 B 很接近 · 在……方面，A 和 B 差异不大 / 大同小异 · A 与 B 在某种程度上很相似",
           "A 与 B 并无区别 / 相差无几 / 并无二致 · 相同之处可以归纳为以下几个方面",
           "## Dẫn số liệu: A 大约是 B 的……倍 · 和 B 相比，A 增长/下降了……% · A 不足 B 的一半",
           "## Kết luận: 总之 · 总而言之 · 由此看来 · 综上所述",
           "Luyện tập: 请比较一下你们国家和中国大学教育制度的异同。"],
    say=[F(0, "Để nêu điểm giống nhau, sách đưa ra các cấu trúc sau."),
         F(1, "A 和 B 很接近, A và B rất gần nhau; 在……方面，A 和 B 差异不大, hoặc 大同小异, về mặt…, A và B khác nhau không nhiều, giống nhau là chính; A 与 B 在某种程度上很相似, ở một mức độ nào đó rất giống nhau."),
         F(2, "A 与 B 并无区别, 相差无几, hoặc 并无二致, đều là không có gì khác nhau. Và 相同之处可以归纳为以下几个方面, điểm giống nhau có thể quy về mấy mặt sau."),
         F(3, "Khi dẫn số liệu: A 大约是 B 的几倍, A gấp khoảng mấy lần B; 和 B 相比，A 增长了，或下降了百分之几, so với B, A tăng hoặc giảm bao nhiêu phần trăm; A 不足 B 的一半, A chưa bằng một nửa B. Bài một chấm ba có câu rất hay: 北京的人口却不到这四省总人口的二十分之一."),
         F(4, "Kết luận: 总之，总而言之，由此看来，综上所述, tóm lại, nói chung, từ đó có thể thấy, tổng hợp những điều trên."),
         F(5, "Bài luyện tập của sách: 请比较一下你们国家和中国大学教育制度的异同。 Hãy so sánh điểm giống và khác nhau giữa chế độ giáo dục đại học của nước bạn và Trung Quốc. Sách còn có một bài văn mẫu so sánh nhà gần trường ở Mỹ và Trung Quốc, yêu cầu tóm tắt lại trong bốn trăm đến năm trăm chữ.")])

add("bullets", section="Ôn tập 单元练习", title="Đề viết và bài tập quay video", size=34,
    items=["写作一：教育，是否能改变阶层固化？– phim tài liệu 《人生七年》, không dưới 800 chữ",
           "写作三：教育公平 – “不患寡而患不均”: 起点公平 · 过程公平 · 结果公平 (không dưới 800 chữ)",
           "录屏作业：名校面对面 – giới thiệu một trường của nước bạn cho học sinh Trung Quốc (PPT + video)",
           "Gợi ý: 学校历史、排名 · 校园和宿舍环境 · 特色专业、课程 · 师资情况 · 其他亮点"],
    say=["Cuối cùng là các đề viết và bài tập quay video.",
         F(0, "Đề viết một: 教育，是否能改变阶层固化？ Giáo dục có thể phá vỡ sự cố định giai tầng không? 阶层固化 là các tầng lớp xã hội bị đóng khung, con nhà nghèo khó vươn lên. Sách lấy ví dụ bộ phim tài liệu 人生七年 của Anh, quay suốt gần năm mươi lăm năm cuộc đời của mười bốn đứa trẻ thuộc các tầng lớp khác nhau. Bài viết không dưới tám trăm chữ."),
         F(1, "Đề viết ba: 教育公平, công bằng giáo dục, mở đầu bằng câu 不患寡而患不均 trong bài một chấm ba. Các bạn hãy bàn xem nên theo đuổi 起点公平, công bằng điểm xuất phát, 过程公平, công bằng quá trình, hay 结果公平, công bằng kết quả."),
         F(2, "Bài tập quay video: 名校面对面, gặp gỡ trường danh tiếng. Hãy chọn một trường cấp ba hoặc đại học của Việt Nam, làm slide và quay video giới thiệu trường cho học sinh Trung Quốc."),
         F(3, "Gợi ý nội dung: lịch sử và thứ hạng của trường, khuôn viên và ký túc xá, các ngành học đặc sắc, đội ngũ giáo viên, và những điểm nổi bật khác. Đây là cơ hội tuyệt vời để dùng lại toàn bộ từ vựng của Đơn vị một.")])

add("bullets", section="Ôn tập 单元练习", title="Hoàn thành Đơn vị 1 – bài tập về nhà", size=36,
    items=["Ôn lại 135 từ mới và khoảng 30 mẫu câu của ba bài",
           "Chọn một đề tranh luận, chuẩn bị 3 luận điểm bằng tiếng Trung",
           "Viết bài so sánh 400–500 chữ: giáo dục đại học ở Việt Nam và Trung Quốc",
           "Bài sau: Đơn vị 2 时代篇 – Bài 2.1 融不进的城市，回不去的农村"],
    say=["Như vậy là chúng ta đã hoàn thành Đơn vị một.",
         F(0, "Các bạn hãy ôn lại một trăm ba mươi lăm từ mới và khoảng ba mươi mẫu câu của ba bài."),
         F(1, "Chọn một trong ba đề tranh luận, chuẩn bị ba luận điểm bằng tiếng Trung, dùng các từ nối như 按说，换一个角度，话又说回来，一则……二则……."),
         F(2, "Và viết một bài so sánh từ bốn trăm đến năm trăm chữ về giáo dục đại học ở Việt Nam và Trung Quốc, dùng các cấu trúc so sánh vừa học."),
         F(3, "Cảm ơn các bạn đã theo dõi bài giảng. Bài sau, chúng ta bước sang Đơn vị hai, 时代篇, chủ đề Thời đại, với bài hai chấm một: 融不进的城市，回不去的农村, Thành phố không hòa nhập được, nông thôn không về được, nói về thế hệ lao động trẻ từ nông thôn lên thành phố. Hẹn gặp lại các bạn. Chúc các bạn học tốt!")])

lesson = {
    "title": "顶石中文 – Bài 1.3: “高考移民”动了谁的奶酪？ (Di dân thi đại học đụng đến phô mai của ai?)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"应考": "硬考",            # yìngkǎo
                    "应试": "硬试",            # yìngshì
                    "一朝": "一招",            # yīzhāo
                    "相差": "相岔",            # xiāngchà
                    "背井": "倍井",            # bèijǐng
                    "率先": "帅先",            # shuàixiān
                    "空子": "控子",            # kòngzi
                    "似锦": "四锦",            # sìjǐn
                    "长身体": "涨身体"},       # zhǎng
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds13.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
