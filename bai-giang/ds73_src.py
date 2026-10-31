#!/usr/bin/env python3
"""Kịch bản bài giảng 顶石中文 – Bài 7.3 «中国扶贫的道路选择». Chạy để sinh ds73.json."""
import json
import os

TAG = "顶石中文 · Bài 7.3 · 中国扶贫的道路选择"
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
    zh="中国扶贫的", py="道路选择",
    vi="Bài 7.3: Con đường xóa đói giảm nghèo của Trung Quốc",
    sub="Zhōngguó fúpín de dàolù xuǎnzé\nBài giảng chi tiết bằng tiếng Việt",
    say=["Xin chào các bạn! Chào mừng các bạn đến với bài giảng giáo trình 顶石中文, Đỉnh cao tiếng Trung.",
         {"t": "Hôm nay chúng ta học bài cuối của Đơn vị bảy, chủ đề Kinh tế: bài bảy chấm ba, 中国扶贫的道路选择。 Nghĩa là: Con đường xóa đói giảm nghèo mà Trung Quốc lựa chọn.",
          "cap": "Hôm nay chúng ta học bài cuối của Đơn vị 7, chủ đề Kinh tế: bài 7.3, 中国扶贫的道路选择。 Nghĩa là: Con đường xóa đói giảm nghèo mà Trung Quốc lựa chọn."},
         "Bài khóa là một bài bình luận trên tuần san Tam Liên Sinh Hoạt. Cuối năm hai nghìn không trăm hai mươi, Trung Quốc tuyên bố đã xóa bỏ nghèo tuyệt đối. Tác giả giải thích: gốc rễ của nghèo đói là thể chế kinh tế kế hoạch, và lời giải nằm ở cải cách: khoán ruộng đến hộ gia đình, doanh nghiệp hương trấn, và chính sách nâng giá nông sản.",
         "Câu chuyện này rất gần gũi với Việt Nam: từ thời bao cấp, Khoán mười, đến Đổi mới. Cuối bài, chúng ta còn có chương ôn tập toàn bộ Đơn vị bảy. Chúng ta bắt đầu nhé."])

add("bullets", section="Mở đầu", title="Mục tiêu bài học",
    items=["Hiểu bài bình luận: nguồn gốc nghèo đói và ba động lực giảm nghèo của Trung Quốc",
           "Nắm vững 45 từ mới, kèm âm Hán Việt và ví dụ",
           "6 mẫu câu: 载入……史册 · 归根到底 · 意想不到的是 · 事关 · 继……之后 · 打破……的束缚",
           "6 kết hợp từ: 寥寥 · 蓬勃 · 空前 · 高涨 · 大幅 · 激发 và 13 thành ngữ, quán ngữ",
           "Luyện tập theo sách; liên hệ Việt Nam; Ôn tập Đơn vị 7"],
    say=["Bài học hôm nay có năm mục tiêu.",
         F(0, "Thứ nhất, hiểu bài bình luận: vì sao nông thôn Trung Quốc từng nghèo, và ba động lực đã giúp hàng trăm triệu người thoát nghèo."),
         F(1, "Thứ hai, nắm vững bốn mươi lăm từ mới. Với mỗi từ, thầy sẽ đọc mẫu, cho các bạn âm Hán Việt để dễ nhớ, giải thích nghĩa và đưa ví dụ."),
         F(2, "Thứ ba, học sáu mẫu câu trọng điểm: 载入史册，归根到底，意想不到的是，事关，继之后, và 打破的束缚."),
         F(3, "Thứ tư, học sáu kết hợp từ và mười ba thành ngữ, quán ngữ, nhiều nhất trong đơn vị này, như 雨后春笋，立竿见影，天时地利人和."),
         F(4, "Thứ năm, làm bài luyện tập của sách, liên hệ với con đường thoát nghèo của Việt Nam, và cuối cùng là ôn tập toàn bộ Đơn vị bảy."),
         "Các bạn hãy chuẩn bị giấy bút, và đừng ngại tạm dừng video để ghi chép hoặc đọc theo nhé."])

# ======================= KHỞI ĐỘNG =======================
add("bullets", chapter="Khởi động", section="Khởi động 课前思考", title="Câu hỏi trước bài học 课前思考", reveal=True, size=34,
    items=["(1) 你们国家存在贫困人口吗？",
           "Đáp án gợi ý: 存在。越南经过几十年的革新开放，贫困率大幅下降，但是在山区和少数民族地区还有一部分贫困人口。",
           "(2) 你觉得造成贫困的原因有哪些？",
           "Đáp án gợi ý: 原因有很多，比如自然条件差、交通不便、教育水平低、缺少资金和技术，还有不合理的制度。",
           "(3) 你们国家的政府有哪些针对贫困人口的扶持政策？",
           "Đáp án gợi ý: 越南政府为贫困地区修建道路和学校，为贫困户提供优惠贷款和医疗保险，还开展职业培训。"],
    say=["Chúng ta bắt đầu bằng ba câu hỏi trước bài học, 课前思考. Thầy đọc câu hỏi, các bạn tạm dừng để tự trả lời bằng tiếng Trung, rồi nghe câu trả lời gợi ý nhé.",
         F(0, "Câu một: 你们国家存在贫困人口吗？ Ở nước bạn có người nghèo không? 贫困人口 là dân số nghèo, người nghèo."),
         F(1, "Gợi ý: 存在。越南经过几十年的革新开放，贫困率大幅下降，但是在山区和少数民族地区还有一部分贫困人口。 Có. Qua mấy chục năm Đổi mới, tỷ lệ nghèo của Việt Nam giảm mạnh, nhưng ở miền núi và vùng đồng bào dân tộc thiểu số vẫn còn một bộ phận người nghèo. Người Trung Quốc gọi công cuộc Đổi mới của Việt Nam là 革新开放."),
         F(2, "Câu hai: 你觉得造成贫困的原因有哪些？ Theo bạn, những nguyên nhân nào gây ra nghèo đói?"),
         F(3, "Gợi ý: 原因有很多，比如自然条件差、交通不便、教育水平低、缺少资金和技术，还有不合理的制度。 Có nhiều nguyên nhân: điều kiện tự nhiên khắc nghiệt, giao thông không thuận tiện, trình độ giáo dục thấp, thiếu vốn và kỹ thuật, và cả chế độ bất hợp lý. Nguyên nhân cuối cùng chính là luận điểm của bài khóa."),
         F(4, "Câu ba: 你们国家的政府有哪些针对贫困人口的扶持政策？ Chính phủ nước bạn có những chính sách hỗ trợ nào dành cho người nghèo? 扶持 là nâng đỡ, hỗ trợ."),
         F(5, "Gợi ý: 越南政府为贫困地区修建道路和学校，为贫困户提供优惠贷款和医疗保险，还开展职业培训。 Chính phủ Việt Nam xây đường, trường học cho vùng nghèo, cho hộ nghèo vay vốn ưu đãi, cấp bảo hiểm y tế, và mở các lớp dạy nghề.")])

add("bullets", section="Khởi động 课前思考", title="Khởi động: từ ngữ về xóa đói giảm nghèo", size=34,
    items=["贫困 nghèo khó · 贫困人口 người nghèo · 贫困户 hộ nghèo · 贫困县 huyện nghèo",
           "扶贫 xóa đói giảm nghèo, giúp người nghèo · 脱贫 thoát nghèo · 摘帽 “bỏ mũ” = thoát danh hiệu huyện nghèo",
           "精准扶贫 xóa nghèo “chính xác” (đến từng hộ, từ 2013) · 小康社会 xã hội khá giả",
           "三农 “tam nông”: 农业 · 农村 · 农民 (Việt Nam cũng nói “tam nông”)",
           "扶贫先扶智 giúp nghèo trước hết giúp trí · 授人以鱼不如授人以渔 cho cá không bằng cho cần câu"],
    say=["Trước khi học từ mới, chúng ta làm quen với một số từ ngữ về xóa đói giảm nghèo, rất hay gặp trong báo chí Trung Quốc.",
         F(0, "贫困 là nghèo khó; 贫困人口 là người nghèo; 贫困户 là hộ nghèo; 贫困县 là huyện nghèo."),
         F(1, "扶贫, chữ đầu là phù, nâng đỡ: nâng đỡ người nghèo, tức là xóa đói giảm nghèo. 脱贫 là thoát nghèo. 摘帽 là bỏ mũ: huyện nghèo đạt chuẩn thì được bỏ cái mũ huyện nghèo."),
         F(2, "精准扶贫 là xóa nghèo chính xác, chính sách từ năm hai nghìn không trăm mười ba: xác định đúng từng hộ nghèo, nghèo vì sao, giúp bằng cách nào. 小康社会 là xã hội khá giả, mục tiêu Trung Quốc đặt ra cho năm hai nghìn không trăm hai mươi."),
         F(3, "三农 là ba vấn đề nông: 农业, nông nghiệp; 农村, nông thôn; 农民, nông dân. Việt Nam cũng dùng chính khái niệm tam nông này."),
         F(4, "Và hai câu rất hay: 扶贫先扶智, giúp người nghèo trước hết phải giúp về trí tuệ; 授人以鱼不如授人以渔, cho người con cá không bằng dạy người cách câu cá. Phần ôn tập đơn vị sẽ có một đề tranh biện về điều này.")])

# ======================= TỪ MỚI =======================
# (chữ Hán, pinyin, Hán Việt, từ loại, nghĩa hiển thị, ví dụ, dịch ví dụ, lời giảng[, chữ đọc thay])
V = [
    ("扶贫", "fúpín", "phù bần", "động từ", "xóa đói giảm nghèo, giúp đỡ người nghèo", "政府派了很多干部到农村扶贫。", "Chính phủ cử rất nhiều cán bộ về nông thôn giúp dân thoát nghèo.",
     "Động từ, nghĩa là giúp hộ nghèo phát triển sản xuất, thay đổi cảnh nghèo khó. 扶 là phù, nâng đỡ, như trong 扶持; 贫 là bần, nghèo. Hay gặp: 扶贫工作，扶贫政策，扶贫干部."),
    ("清零", "qīnglíng", "thanh linh", "động từ", "đưa về số không, xóa sạch", "这个县的贫困人口已经清零了。", "Số người nghèo của huyện này đã về không.",
     "Động từ, nghĩa là đưa con số về không. 清 là làm sạch, 零 là số không. Trong bài: 实现了数亿贫困人口清零, đưa mấy trăm triệu người nghèo về con số không."),
    ("奇迹", "qíjì", "kỳ tích", "danh từ", "kỳ tích, điều kỳ diệu", "他们创造了一个医学奇迹。", "Họ đã tạo nên một kỳ tích y học.",
     "Danh từ, nghĩa là việc phi thường ngoài sức tưởng tượng. Động từ hay đi kèm là 创造: 创造奇迹, tạo nên kỳ tích. Âm Hán Việt kỳ tích giống tiếng Việt."),
    ("载入", "zǎirù", "tải nhập", "động từ", "ghi vào, ghi vào sử sách", "他的名字将载入史册。", "Tên tuổi của ông ấy sẽ được ghi vào sử sách.",
     "Động từ, nghĩa là ghi vào. Chú ý chữ đầu ở đây đọc thanh ba, zǎi, như trong 记载, ghi chép; khác với zài trong 载人, chở người. Gần như luôn đi với 史册: 载入史册, mẫu câu thứ nhất."),
    ("史册", "shǐcè", "sử sách", "danh từ", "sử sách", "这场战役被写进了史册。", "Trận đánh này đã được ghi vào sử sách.",
     "Danh từ, nghĩa là sách ghi chép lịch sử. 册 Hán Việt là sách, như trong 手册, sổ tay. Hay gặp: 载入史册, 名垂史册, tên tuổi lưu danh sử sách."),
    ("借鉴", "jièjiàn", "tá giám", "động từ", "tham khảo, học hỏi (kinh nghiệm)", "我们可以借鉴别国的成功经验。", "Chúng ta có thể học hỏi kinh nghiệm thành công của nước khác.",
     "Động từ, nghĩa là lấy người khác làm gương để học hỏi, tham khảo. 借 là mượn, 鉴 là tấm gương. Từ này không có trong bảng từ của sách nhưng xuất hiện ở đầu và cuối bài: 借鉴意义, giá trị tham khảo; 为很多贫困地区所借鉴."),
    ("归根到底", "guīgēn-dàodǐ", "quy căn đáo để", "thành ngữ", "suy cho cùng, xét đến cùng", "归根到底，这是一个钱的问题。", "Suy cho cùng, đây là vấn đề tiền bạc.",
     "Thành ngữ, nghĩa là trở về đến tận gốc, tức là suy cho cùng. Còn nói là 归根结底. 归 là trở về, 根 là gốc rễ, 到底 là đến cùng. Đây là mẫu câu thứ hai."),
    ("弊端", "bìduān", "tệ đoan", "danh từ", "tệ hại, mặt trái, khuyết điểm (của chế độ)", "这种管理制度有很多弊端。", "Chế độ quản lý này có rất nhiều mặt trái.",
     "Danh từ, chỉ những điều tệ hại, sai sót do chế độ hay cách làm gây ra. Cẩn thận, từ dễ nhầm: tiếng Việt tệ đoan thường là tệ nạn xã hội; còn 弊端 là mặt trái, khuyết điểm của một chế độ. Trong bài: 计划经济时代的种种弊端."),
    ("加剧", "jiājù", "gia kịch", "động từ", "làm trầm trọng thêm, ngày càng gay gắt", "人口老龄化问题正在加剧。", "Vấn đề già hóa dân số đang ngày càng trầm trọng.",
     "Động từ, nghĩa là làm mức độ nghiêm trọng tăng thêm. Chữ 剧 ở đây là mãnh liệt, dữ dội, không phải kịch. Trong bài: 加剧了农村人口的贫困程度."),
    ("帷幕", "wéimù", "duy mạc", "danh từ", "màn (sân khấu), tấm màn", "演出即将开始，帷幕慢慢拉开了。", "Buổi diễn sắp bắt đầu, tấm màn từ từ kéo ra.",
     "Danh từ, nghĩa là tấm màn treo trên sân khấu. Cụm cố định: 拉开帷幕, kéo màn, tức là mở màn, bắt đầu; 落下帷幕, hạ màn, kết thúc. Trong bài: 中国的市场经济改革就此拉开帷幕."),
    ("寥寥", "liáoliáo", "liêu liêu", "tính từ", "rất ít, lèo tèo", "会场上的观众寥寥无几。", "Khán giả trong hội trường lèo tèo chẳng mấy người.",
     "Tính từ, nghĩa là rất ít. Hay gặp: 寥寥无几, ít ỏi chẳng được mấy; 寥寥数语, vài ba câu. Trong bài: 那一轮国企改革成效寥寥, hiệu quả ít ỏi. Đây là một kết hợp từ trọng điểm."),
    ("凸显", "tūxiǎn", "đột hiển", "động từ", "nổi bật lên, lộ rõ", "这个问题日益凸显出来。", "Vấn đề này ngày càng lộ rõ.",
     "Động từ, nghĩa là hiện ra rõ ràng. 凸 là lồi lên, 显 là hiện. Trong bài: 改革的成就却最终在农村凸显出来, thành tựu cải cách cuối cùng lại nổi bật ở nông thôn."),
    ("联产", "liánchǎn", "liên sản", "động từ", "gắn với sản lượng", "联产承包大大提高了农民的积极性。", "Khoán gắn với sản lượng đã nâng cao rất nhiều tính tích cực của nông dân.",
     "Động từ, nghĩa là gắn với sản lượng. 联 là liên kết, 产 là sản lượng. Thu nhập của nông dân gắn với sản lượng họ làm ra, làm nhiều hưởng nhiều. Trong bài: 家庭联产承包责任制."),
    ("承包", "chéngbāo", "thừa bao", "động từ", "nhận khoán, nhận thầu", "他承包了村里的五十亩果园。", "Anh ấy nhận khoán năm mươi mẫu vườn cây ăn quả của làng.",
     "Động từ, nghĩa là nhận làm và chịu trách nhiệm hoàn thành một công trình, một việc sản xuất kinh doanh. Tiếng Việt nói khoán, thầu: 承包制 là chế độ khoán; 承包商 là nhà thầu."),
    ("乡镇", "xiāngzhèn", "hương trấn", "danh từ", "xã và thị trấn; thị trấn nhỏ", "这个乡镇的经济发展得很快。", "Kinh tế của thị trấn này phát triển rất nhanh.",
     "Danh từ, 乡 là xã, 镇 là thị trấn, hai cấp hành chính cơ sở của Trung Quốc; cũng chỉ chung các thị trấn nhỏ. 乡镇企业 là doanh nghiệp hương trấn, nhân vật chính của bài."),
    ("蓬勃", "péngbó", "bồng bột", "tính từ", "sôi nổi, mạnh mẽ, phát triển mạnh", "近年来，电子商务蓬勃发展。", "Mấy năm gần đây, thương mại điện tử phát triển mạnh mẽ.",
     "Tính từ, nghĩa là phồn vinh, tràn đầy sức sống. Cẩn thận, từ dễ nhầm: tiếng Việt bồng bột là nông nổi, hấp tấp; còn 蓬勃 là phát triển mạnh mẽ, mang nghĩa tốt. Hay gặp: 蓬勃发展，朝气蓬勃. Đây là một kết hợp từ trọng điểm."),
    ("抛弃", "pāoqì", "phao khí", "động từ", "vứt bỏ, ruồng bỏ", "我们要抛弃旧观念。", "Chúng ta phải vứt bỏ quan niệm cũ.",
     "Động từ, nghĩa là ném đi không cần nữa. Dùng cho đồ vật, quan niệm, cũng dùng cho người: 抛弃家人, ruồng bỏ gia đình. Trong bài: 抛弃了以前的大锅饭体制."),
    ("大锅饭", "dàguōfàn", "đại oa phạn", "danh từ", "“nồi cơm chung”, chế độ cào bằng", "吃大锅饭的时代已经过去了。", "Thời ăn chung một nồi cơm đã qua rồi.",
     "Danh từ, nghĩa đen là cơm nấu chung một nồi to. Nghĩa bóng: làm tốt hay dở, đóng góp nhiều hay ít, đãi ngộ đều như nhau, tức là chế độ cào bằng. Thời công xã nhân dân, các đội sản xuất ăn ở nhà ăn tập thể, nên có tên gọi này. Hay nói: 吃大锅饭."),
    ("激励", "jīlì", "kích lệ", "động từ", "khích lệ, khuyến khích", "公司用奖金激励员工。", "Công ty dùng tiền thưởng để khích lệ nhân viên.",
     "Động từ, nghĩa là khích lệ, cổ vũ cho hăng hái lên. Hay gặp: 激励机制, cơ chế khuyến khích, như trong bài: 交够了国家的，留足了集体的，剩下的全是自己的的激励机制."),
    ("空前", "kōngqián", "không tiền", "động từ", "chưa từng có", "这次展览取得了空前的成功。", "Cuộc triển lãm này đã thành công chưa từng có.",
     "Bảng từ ghi là động từ, thường dùng như tính từ, nghĩa là trước đây chưa từng có. Tiếng Việt có thành ngữ không tiền khoáng hậu, trước chưa từng có, sau cũng không có. Hay gặp: 空前高涨，空前成功，盛况空前."),
    ("高涨", "gāozhǎng", "cao trướng", "động từ", "dâng cao, tăng vọt", "大家的热情十分高涨。", "Nhiệt tình của mọi người dâng rất cao.",
     "Động từ, nghĩa là mực nước, giá cả tăng vọt; cũng dùng cho tinh thần, cảm xúc dâng cao. Chú ý chữ sau đọc thanh ba, zhǎng. Trong bài: 农民的生产积极性空前高涨."),
    ("大幅", "dàfú", "đại phúc", "tính từ", "(với) biên độ lớn, mạnh", "今年的产量大幅提高。", "Sản lượng năm nay tăng mạnh.",
     "Tính từ, đứng trước động từ, nghĩa là với biên độ lớn. 幅 là bề rộng, biên độ. Hay gặp: 大幅提高，大幅上涨，大幅下降. Còn nói là 大幅度. Đây là một kết hợp từ trọng điểm."),
    ("事关", "shìguān", "sự quan", "động từ", "liên quan đến (việc hệ trọng)", "这件事关系重大，事关全厂工人的利益。", "Việc này hệ trọng, liên quan đến lợi ích của toàn thể công nhân nhà máy.",
     "Động từ, nghĩa là việc này liên quan đến…, thường là chuyện hệ trọng như an toàn, trách nhiệm, lợi ích. Hay gặp: 事关重大, 事关全局. Đây là mẫu câu thứ tư."),
    ("切身", "qièshēn", "thiết thân", "tính từ", "thiết thân, sát sườn; tự thân", "这项政策关系到每个人的切身利益。", "Chính sách này liên quan đến lợi ích thiết thân của mỗi người.",
     "Tính từ, nghĩa là liên quan mật thiết đến bản thân; cũng có nghĩa là tự mình trải qua: 切身体会, cảm nhận của chính mình. Chú ý chữ đầu đọc thanh bốn, qiè. Âm Hán Việt thiết thân giống tiếng Việt."),
    ("连锁反应", "liánsuǒ fǎnyìng", "liên tỏa phản ứng", "danh từ", "phản ứng dây chuyền", "两国的贸易冲突引发了一系列连锁反应。", "Xung đột thương mại giữa hai nước đã gây ra một loạt phản ứng dây chuyền.",
     "Danh từ, ví với việc nhiều sự vật liên quan với nhau, chỉ cần một cái thay đổi là những cái khác thay đổi theo. 连锁 là xích nối liền nhau, như 连锁店, chuỗi cửa hàng."),
    ("释放", "shìfàng", "thích phóng", "động từ", "giải phóng, tỏa ra; phóng thích", "运动可以帮助人们释放压力。", "Vận động có thể giúp con người giải tỏa áp lực.",
     "Động từ, nghĩa là giải phóng vật chất hay năng lượng chứa bên trong; cũng có nghĩa là thả người bị giam. Hay gặp: 释放压力，释放潜力，释放能量. Trong bài: 释放出更多的剩余劳动力."),
    ("剩余", "shèngyú", "thặng dư", "động từ", "thừa ra, còn dư", "我把剩余的钱存进了银行。", "Tôi gửi số tiền còn dư vào ngân hàng.",
     "Động từ, cũng dùng như tính từ, nghĩa là phần còn lại sau khi đã trừ đi. 剩余劳动力 là lao động dư thừa. Âm Hán Việt thặng dư, như giá trị thặng dư."),
    ("民营", "mínyíng", "dân doanh", "tính từ", "tư nhân, do dân kinh doanh", "民营企业是国民经济的重要力量。", "Doanh nghiệp tư nhân là lực lượng quan trọng của nền kinh tế quốc dân.",
     "Tính từ, nghĩa là do nhân dân kinh doanh, đối lập với 国营, quốc doanh. 民营企业 là doanh nghiệp tư nhân; 民营经济 là kinh tế tư nhân."),
    ("启蒙", "qǐméng", "khải mông", "động từ", "khai sáng; vỡ lòng", "母亲是我的启蒙老师。", "Mẹ là người thầy vỡ lòng của tôi.",
     "Động từ, nghĩa là phổ biến tri thức mới, giúp con người thoát khỏi ngu muội; cũng là dạy vỡ lòng. 启蒙运动 là phong trào Khai sáng ở châu Âu. Trong bài: 对中国民营经济的发展起到了明显的启蒙作用."),
    ("崛起", "juéqǐ", "quật khởi", "động từ", "trỗi dậy, vươn lên", "一座新城市在这里崛起。", "Một thành phố mới đã vươn lên ở nơi này.",
     "Động từ, nghĩa là nổi lên, trỗi dậy mạnh mẽ. Hay gặp: 大国崛起, sự trỗi dậy của nước lớn. Âm Hán Việt quật khởi giống tiếng Việt. Trong bài: 乡镇企业的崛起."),
    ("重工业", "zhònggōngyè", "trọng công nghiệp", "danh từ", "công nghiệp nặng", "这座城市以重工业为主。", "Thành phố này lấy công nghiệp nặng làm chủ đạo.",
     "Danh từ, gồm luyện kim, cơ khí, năng lượng như điện, dầu mỏ, than đá, khí thiên nhiên, hóa chất, vật liệu. Trái nghĩa là 轻工业, công nghiệp nhẹ. Chữ đầu đọc là zhòng."),
    ("人为", "rénwéi", "nhân vi", "động từ", "do con người làm ra, nhân tạo", "这场火灾是人为造成的。", "Vụ cháy này là do con người gây ra.",
     "Bảng từ ghi là động từ, thường dùng như tính từ, nghĩa là do con người làm, không tự nhiên. Trái nghĩa là 天然，自然. Chú ý chữ sau đọc thanh hai, wéi. Trong bài: 农产品价格被人为压低."),
    ("剪刀差", "jiǎndāochā", "tiễn đao sai", "danh từ", "cánh kéo giá (chênh lệch giá công – nông)", "工农业产品价格存在剪刀差。", "Giá sản phẩm công nghiệp và nông nghiệp tồn tại cánh kéo chênh lệch.",
     "Danh từ, chỉ việc khi trao đổi, hàng công nghiệp có giá cao hơn giá trị, nông sản có giá thấp hơn giá trị; vẽ lên biểu đồ thì hai đường mở ra như cái kéo. Tiếng Việt gọi là cánh kéo giá. Chữ cuối đọc là chā."),
    ("压低", "yādī", "áp đê", "động từ", "ép xuống, hạ thấp", "他怕别人听见，便压低声音说话。", "Anh ấy sợ người khác nghe thấy nên hạ giọng nói nhỏ.",
     "Động từ, nghĩa là ép cho thấp xuống: 压低价格, ép giá; 压低声音, hạ giọng. Trong bài: 农产品价格在很长时间内被人为压低."),
    ("萧条", "xiāotiáo", "tiêu điều", "tính từ", "tiêu điều, vắng vẻ; suy thoái (kinh tế)", "经济萧条，很多工厂都倒闭了。", "Kinh tế suy thoái, rất nhiều nhà máy đóng cửa.",
     "Tính từ, nghĩa là vắng vẻ, không có sức sống; trong kinh tế là suy thoái. Âm Hán Việt tiêu điều giống tiếng Việt. Trong bài: 农村经济一片萧条."),
    ("症结", "zhēngjié", "chứng kết", "danh từ", "mấu chốt, căn nguyên (của vấn đề)", "遇到困难，一定要找准症结。", "Gặp khó khăn, nhất định phải tìm đúng căn nguyên.",
     "Danh từ, vốn là khối cứng trong bụng theo Đông y, nghĩa bóng là chỗ mấu chốt của vấn đề. Chú ý chữ đầu ở đây đọc thanh một, zhēng; khác với 症状, zhèngzhuàng. Trong bài: 找准体制的症结，对症下药."),
    ("压抑", "yāyì", "áp ức", "động từ", "kìm nén, đè nén", "他压抑不住内心的激动。", "Anh ấy không kìm nén được sự xúc động trong lòng.",
     "Động từ, nghĩa là hạn chế tình cảm, sức lực, không cho bộc lộ hay phát huy hết. Cũng dùng như tính từ: 心情很压抑, tâm trạng rất ngột ngạt. Trong bài: 长期被压抑的积极性得以激发."),
    ("激发", "jīfā", "kích phát", "động từ", "khơi dậy, kích thích", "老师的话激发了学生的学习兴趣。", "Lời thầy giáo đã khơi dậy hứng thú học tập của học sinh.",
     "Động từ, nghĩa là kích thích cho hăng hái lên. Hay gặp: 激发热情，激发斗志，激发兴趣. Đây là một kết hợp từ trọng điểm."),
    ("生产力", "shēngchǎnlì", "sinh sản lực", "danh từ", "sức sản xuất, lực lượng sản xuất", "科学技术是第一生产力。", "Khoa học kỹ thuật là lực lượng sản xuất hàng đầu.",
     "Danh từ, thuật ngữ kinh tế, chỉ năng lực sản xuất, hiệu suất sản xuất. Tiếng Việt gọi là lực lượng sản xuất. Trong bài: 生产力得到极大解放, sức sản xuất được giải phóng mạnh mẽ."),
    ("能动性", "néngdòngxìng", "năng động tính", "danh từ", "tính năng động, tính chủ động", "要充分发挥学生的主观能动性。", "Phải phát huy đầy đủ tính năng động chủ quan của học sinh.",
     "Danh từ, chỉ đặc tính tự giác nỗ lực, tích cực hoạt động của con người. Gần như luôn đi trong cụm 主观能动性, tính năng động chủ quan, như trong bài."),
    ("脱贫", "tuōpín", "thoát bần", "động từ", "thoát nghèo", "这个村子已经全部脱贫。", "Ngôi làng này đã thoát nghèo hoàn toàn.",
     "Động từ, nghĩa là thoát khỏi cảnh nghèo. 脱 là thoát, 贫 là nghèo. Hay gặp: 脱贫致富, thoát nghèo làm giàu; 脱贫攻坚, cuộc chiến thoát nghèo."),
    ("致富", "zhìfù", "trí phú", "động từ", "làm giàu", "他靠种水果致富了。", "Anh ấy làm giàu nhờ trồng cây ăn quả.",
     "Động từ, nghĩa là trở nên giàu có. Hay gặp: 勤劳致富, làm giàu bằng sự cần cù; 致富之路, con đường làm giàu. Chữ 致 là đạt tới, như trong 致力于."),
    ("辛勤", "xīnqín", "tân cần", "tính từ", "cần cù vất vả, chăm chỉ", "感谢老师们的辛勤付出。", "Cảm ơn sự vất vả tận tụy của các thầy cô.",
     "Tính từ, nghĩa là vất vả và cần cù. Hay gặp: 辛勤劳动，辛勤工作，辛勤付出. Trong bài: 脱贫致富终究要靠群众的智慧和辛勤付出."),
    ("红利", "hónglì", "hồng lợi", "danh từ", "lợi tức, cổ tức; (nghĩa bóng) lợi ích", "改革开放的红利惠及了千家万户。", "Lợi ích của cải cách mở cửa đã đến với muôn nhà.",
     "Danh từ, nghĩa gốc là phần lợi nhuận chia thêm cho cổ đông, nhân viên; nghĩa bóng là lợi ích do một điều kiện nào đó mang lại, như 人口红利, lợi tức dân số. Từ này có trong bài khóa và bài tập bốn."),
    ("束缚", "shùfù", "thúc phược", "động từ", "trói buộc, ràng buộc", "不要被旧观念束缚住手脚。", "Đừng để quan niệm cũ trói buộc chân tay.",
     "Động từ, cũng dùng như danh từ, nghĩa là trói buộc, hạn chế. Mẫu hay gặp: 打破……的束缚, phá bỏ sự trói buộc của…, mẫu câu thứ sáu; 挣脱束缚, vùng thoát khỏi xiềng xích."),
]

add("bullets", chapter="Từ mới (45 từ)", section="Từ mới 生词", title="Phần 1: Từ mới",
    items=["Bài 7.3 có 45 từ mới, chia thành 15 nhóm nhỏ",
           "Mỗi từ: nghe đọc mẫu 2 lần → âm Hán Việt → nghĩa → ví dụ",
           "Hãy đọc to theo sau mỗi lần nghe",
           "Chú ý âm đọc: 载入 (zǎi) · 症结 (zhēng) · 人为 (wéi) · 切身 (qiè) · 剪刀差 (chā)",
           "Từ dễ nhầm: 弊端 · 蓬勃 · 空前 · 加剧"],
    say=["Bây giờ chúng ta sang phần một: từ mới. Bảng từ của sách có bốn mươi từ; thầy thêm năm từ có trong bài khóa và bài tập là 借鉴，弊端，切身，红利，束缚, thành bốn mươi lăm từ, chia thành mười lăm nhóm nhỏ, mỗi nhóm ba từ.",
         F(1, "Với mỗi từ, các bạn sẽ nghe đọc mẫu hai lần, sau đó là âm Hán Việt, nghĩa, và một ví dụ."),
         F(2, "Hãy đọc to theo sau mỗi lần nghe, vì đọc thành tiếng giúp nhớ từ lâu hơn rất nhiều."),
         F(3, "Bài này có nhiều chữ đa âm: 载入 đọc là zǎirù; 症结 đọc là zhēngjié; 人为 đọc là rénwéi; 切身 đọc là qièshēn; và chữ cuối của 剪刀差 đọc là chā."),
         F(4, "Ngoài ra, có mấy từ Hán Việt dễ hiểu nhầm như 弊端, tệ đoan, hay 蓬勃, bồng bột. Nghĩa của chúng trong tiếng Trung khác hẳn tiếng Việt, các bạn nhớ nghe kỹ nhé. Chúng ta bắt đầu.")])

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
    ("中国在2020年底实现了数亿贫困人口“清零”。这一成就被称为奇迹当之无愧，足以载入人类社会发展的史册。那么中国到底是如何在短短几十年时间里消除了绝对贫困的呢？这样的道路选择对于全球扶贫是否具有借鉴意义呢？",
     "Cuối năm 2020, Trung Quốc đã đưa số người nghèo lên tới hàng trăm triệu về con số không. Thành tựu này được gọi là kỳ tích thì hoàn toàn xứng đáng, đủ để ghi vào sử sách phát triển của xã hội loài người. Vậy rốt cuộc Trung Quốc đã làm thế nào để xóa bỏ nghèo tuyệt đối chỉ trong vài chục năm ngắn ngủi? Con đường mà Trung Quốc lựa chọn có giá trị tham khảo đối với công cuộc xóa nghèo toàn cầu hay không?",
     ["数亿 là mấy trăm triệu: 亿 là một trăm triệu. 清零 là đưa về số không. 当之无愧 là thành ngữ: xứng đáng, không hổ thẹn. 足以载入史册 là đủ để ghi vào sử sách, mẫu câu thứ nhất.",
      "绝对贫困 là nghèo tuyệt đối, tức là không đủ cái ăn cái mặc tối thiểu. 那么 là vậy thì; 到底 là rốt cuộc. 借鉴意义 là giá trị tham khảo. Bài mở đầu bằng hai câu hỏi, phần còn lại sẽ lần lượt trả lời."],
     "中国在二零二零年底实现了数亿贫困人口清零。这一成就被称为奇迹当之无愧，足以载入人类社会发展的史册。那么中国到底是如何在短短几十年时间里消除了绝对贫困的呢？这样的道路选择对于全球扶贫是否具有借鉴意义呢？"),
    ("贫困问题归根到底是由于不合理的计划经济体制造成的。在改革开放之前，计划经济时代的种种弊端给农村经济带来了巨大伤害，加剧了农村人口的贫困程度。这也就意味着，只有对当时落后的制度作出彻底的改革，才能从根本上改变农村面貌，进而大规模消除贫困现象。",
     "Vấn đề nghèo đói suy cho cùng là do thể chế kinh tế kế hoạch bất hợp lý gây ra. Trước cải cách mở cửa, đủ thứ tệ hại của thời kinh tế kế hoạch đã gây tổn hại to lớn cho kinh tế nông thôn, làm trầm trọng thêm mức độ nghèo của dân cư nông thôn. Điều đó cũng có nghĩa là, chỉ có cải cách triệt để chế độ lạc hậu lúc bấy giờ thì mới có thể thay đổi bộ mặt nông thôn từ gốc rễ, rồi từ đó xóa bỏ nghèo đói trên quy mô lớn.",
     ["归根到底 là suy cho cùng, mẫu câu thứ hai. 由于……造成的 là do… gây ra. 计划经济体制 là thể chế kinh tế kế hoạch: nhà nước quyết định sản xuất cái gì, bao nhiêu, phân phối thế nào; Việt Nam gọi là thời bao cấp. 种种弊端 là đủ thứ tệ hại.",
      "加剧 là làm trầm trọng thêm. 只有……才…… là chỉ có… mới…. 从根本上 là từ gốc rễ. 进而 là rồi tiến thêm một bước. Luận điểm của tác giả rất rõ: nghèo là do chế độ, nên phải cải cách chế độ."]),
    ("1978年，中共中央召开了十一届三中全会，中国的市场经济改革就此拉开帷幕。当时改革的重点聚焦于国有企业，但“有心栽花花不开”，那一轮国企改革成效寥寥，意想不到的是，“无心插柳柳成荫”，改革的成就却最终在农村凸显出来。",
     "Năm 1978, Trung ương Đảng Cộng sản Trung Quốc triệu tập Hội nghị Trung ương 3 khóa XI, công cuộc cải cách kinh tế thị trường của Trung Quốc từ đó mở màn. Trọng điểm cải cách lúc ấy tập trung vào doanh nghiệp nhà nước, nhưng “cố công trồng hoa hoa chẳng nở”, đợt cải cách doanh nghiệp nhà nước ấy hiệu quả chẳng được bao nhiêu; điều không ngờ là, “vô tình cắm liễu liễu lại xanh”, thành tựu của cải cách cuối cùng lại nổi bật ở nông thôn.",
     ["中共中央 là Trung ương Đảng Cộng sản Trung Quốc. 十一届三中全会 là Hội nghị toàn thể lần thứ ba Ban Chấp hành Trung ương khóa mười một, tháng mười hai năm 1978, mốc mở đầu cải cách mở cửa. 拉开帷幕 là kéo màn, tức mở màn. 国有企业 là doanh nghiệp nhà nước, nói tắt là 国企.",
      "有心栽花花不开，无心插柳柳成荫 là cặp tục ngữ: cố công trồng hoa thì hoa chẳng nở, vô tình cắm cành liễu thì liễu lại xanh um. 成效寥寥 là hiệu quả ít ỏi. 意想不到的是 là điều không ngờ là, mẫu câu thứ ba. 凸显 là nổi bật lên."],
     "一九七八年，中共中央召开了十一届三中全会，中国的市场经济改革就此拉开帷幕。当时改革的重点聚焦于国有企业，但有心栽花花不开，那一轮国企改革成效寥寥，意想不到的是，无心插柳柳成荫，改革的成就却最终在农村凸显出来。"),
    ("1980年，中央正式批准实行家庭联产承包责任制，趁着改革的东风，乡镇企业随之蓬勃兴起。",
     "Năm 1980, Trung ương chính thức phê chuẩn thực hiện chế độ trách nhiệm khoán sản lượng đến hộ gia đình; nhân luồng gió đông của cải cách, doanh nghiệp hương trấn cũng theo đó mà nở rộ.",
     ["家庭联产承包责任制 là chế độ trách nhiệm khoán gắn với sản lượng theo hộ gia đình: ruộng đất vẫn thuộc tập thể, nhưng giao cho từng hộ canh tác, nộp đủ phần quy định thì phần còn lại thuộc về hộ. Việt Nam cũng có chính sách khoán rất giống, như Khoán mười năm 1988.",
      "趁着改革的东风 là nhân luồng gió đông của cải cách; 东风 là gió xuân, ví với điều kiện thuận lợi. 乡镇企业 là doanh nghiệp hương trấn, do xã, thị trấn hoặc nông dân lập ra. 随之 là theo đó. 蓬勃兴起 là nổi lên mạnh mẽ."],
     "一九八零年，中央正式批准实行家庭联产承包责任制，趁着改革的东风，乡镇企业随之蓬勃兴起。"),
    ("家庭联产承包制度取代了人民公社，对农民而言，最大的意义在于抛弃了以前的“大锅饭”体制，取而代之的是“交够了国家的，留足了集体的，剩下的全是自己的”的激励机制。",
     "Chế độ khoán sản lượng đến hộ gia đình đã thay thế công xã nhân dân. Đối với nông dân, ý nghĩa lớn nhất là vứt bỏ được thể chế “nồi cơm chung” trước kia, thay vào đó là cơ chế khuyến khích “nộp đủ cho nhà nước, để đủ cho tập thể, phần còn lại hoàn toàn là của mình”.",
     ["人民公社 là công xã nhân dân, tồn tại từ năm 1958 đến 1983, đặc điểm là quy mô lớn và mức độ công hữu cao. 对……而言 là đối với… mà nói. 大锅饭 là nồi cơm chung: làm nhiều làm ít, làm tốt làm dở đều hưởng như nhau, tức là cào bằng.",
      "取而代之的是 là thứ thay thế nó là. 交够了国家的，留足了集体的，剩下的全是自己的 là khẩu hiệu nổi tiếng của chế độ khoán; chữ 的 cuối mỗi vế tạo cụm danh từ: phần của nhà nước, phần của tập thể. 激励机制 là cơ chế khuyến khích."]),
    ("农民的生产积极性空前高涨，农业生产效率显著提高，主要农产品的产量大幅提升，农民生活有了明显改善。",
     "Tính tích cực sản xuất của nông dân dâng cao chưa từng thấy, hiệu suất sản xuất nông nghiệp tăng rõ rệt, sản lượng các nông sản chủ yếu tăng mạnh, đời sống nông dân được cải thiện rõ ràng.",
     ["空前高涨 là dâng cao chưa từng có, hai kết hợp từ trọng điểm đi liền nhau. 积极性 là tính tích cực, sự hăng hái. 显著 là rõ rệt.",
      "大幅提升 là tăng mạnh; 大幅 là biên độ lớn. Bốn vế câu nối tiếp nhau như một chuỗi phản ứng: nông dân hăng hái, năng suất tăng, sản lượng tăng, đời sống khá lên."]),
    ("家庭联产承包制度的推进事关农民的切身利益，给农村带来了一系列连锁反应，最大的效应就是刺激了乡镇企业的发展。“说一千、道一万，增加农民收入是关键”。",
     "Việc đẩy mạnh chế độ khoán sản lượng đến hộ gia đình liên quan đến lợi ích thiết thân của nông dân, mang lại cho nông thôn một loạt phản ứng dây chuyền, mà hiệu ứng lớn nhất là thúc đẩy sự phát triển của doanh nghiệp hương trấn. “Nói nghìn câu vạn lời, tăng thu nhập cho nông dân mới là then chốt.”",
     ["事关 là liên quan đến việc hệ trọng, mẫu câu thứ tư. 切身利益 là lợi ích thiết thân. 一系列连锁反应 là một loạt phản ứng dây chuyền. 效应 là hiệu ứng. 刺激 là kích thích, thúc đẩy.",
      "说一千、道一万 là quán ngữ: nói nghìn câu, bàn vạn lời, tức là dù nói gì đi nữa thì điều cốt lõi vẫn là…. Câu này nhấn mạnh: tăng thu nhập cho nông dân là mấu chốt."]),
    ("农民收入提高之后，消费需求随之上升，同时，土地制度改革提高了农业生产效率，释放出更多的剩余劳动力，乡镇企业经济如雨后春笋般在农村发展起来，成为当时中国经济最有活力的部分，对中国民营经济的发展起到了明显的启蒙作用。",
     "Sau khi thu nhập của nông dân tăng lên, nhu cầu tiêu dùng cũng theo đó tăng; đồng thời, cải cách chế độ ruộng đất nâng cao hiệu suất sản xuất nông nghiệp, giải phóng thêm nhiều lao động dư thừa. Kinh tế doanh nghiệp hương trấn phát triển ở nông thôn như nấm mọc sau mưa, trở thành bộ phận năng động nhất của kinh tế Trung Quốc lúc bấy giờ, có tác dụng khai sáng rõ rệt đối với sự phát triển của kinh tế tư nhân Trung Quốc.",
     ["随之上升 là theo đó mà tăng. 释放出剩余劳动力: mỗi hộ không còn cần nhiều người làm ruộng như trước, người thừa ra có thể vào làm ở doanh nghiệp hương trấn. 释放 là giải phóng.",
      "如雨后春笋般 là như măng xuân sau mưa, tiếng Việt nói như nấm mọc sau mưa. 民营经济 là kinh tế tư nhân. 起到了启蒙作用 là có tác dụng khai sáng, mở đường: doanh nghiệp hương trấn là bài học vỡ lòng cho kinh tế tư nhân."]),
    ("乡镇企业的崛起，成为继家庭联产承包责任制之后，农村减贫的第二大推动力。",
     "Sự trỗi dậy của doanh nghiệp hương trấn đã trở thành động lực giảm nghèo nông thôn lớn thứ hai, tiếp sau chế độ trách nhiệm khoán sản lượng đến hộ gia đình.",
     ["崛起 là trỗi dậy, vươn lên. 继……之后 là tiếp sau…, mẫu câu thứ năm. 减贫 là giảm nghèo. 推动力 là động lực thúc đẩy.",
      "Đến đây tác giả đã nêu hai động lực giảm nghèo: thứ nhất là chế độ khoán, thứ hai là doanh nghiệp hương trấn. Đoạn sau nói đến yếu tố thứ ba: chính sách hỗ trợ của nhà nước."]),
    ("当时农民收入的提高，除了轰轰烈烈的制度改革之外，国家政策扶持也是至关重要的。从新中国成立之初到改革开放之前，中国经济的重点是发展城市工业，为了扶持工业尤其是重工业发展，农产品价格在很长时间内被人为压低，工农业产品价格的巨大剪刀差大大伤害了农民的利益。",
     "Thu nhập của nông dân lúc ấy tăng lên, ngoài cuộc cải cách chế độ rầm rộ, sự hỗ trợ bằng chính sách của nhà nước cũng vô cùng quan trọng. Từ khi nước Trung Hoa mới thành lập đến trước cải cách mở cửa, trọng điểm của kinh tế Trung Quốc là phát triển công nghiệp đô thị; để hỗ trợ công nghiệp, nhất là công nghiệp nặng, giá nông sản trong thời gian dài bị ép thấp một cách nhân tạo, cánh kéo chênh lệch khổng lồ giữa giá hàng công nghiệp và nông sản đã gây tổn hại lớn cho lợi ích của nông dân.",
     ["除了……之外 là ngoài… ra. 轰轰烈烈 là rầm rộ, sôi nổi. 扶持 là nâng đỡ, hỗ trợ. 至关重要 là vô cùng quan trọng. 新中国成立 là nước Cộng hòa Nhân dân Trung Hoa thành lập, năm 1949.",
      "尤其是 là nhất là. 被人为压低 là bị ép thấp một cách nhân tạo. 剪刀差 là cánh kéo giá: hàng công nghiệp bán đắt hơn giá trị, nông sản bán rẻ hơn giá trị. Nông dân đã phải gánh chi phí cho công cuộc công nghiệp hóa."]),
    ("改革开放之后，从1979年开始，政府大幅度提高农产品的采购价格，农民收入随之提高，可谓“立竿见影”。",
     "Sau cải cách mở cửa, từ năm 1979, chính phủ tăng mạnh giá thu mua nông sản, thu nhập của nông dân cũng theo đó tăng lên, có thể nói là “dựng sào thấy bóng”, hiệu quả tức thì.",
     ["大幅度 là với biên độ lớn, giống 大幅. 采购价格 là giá thu mua. 随之提高 là theo đó tăng lên.",
      "可谓 là có thể nói là. 立竿见影 là thành ngữ: dựng cây sào dưới nắng là thấy ngay bóng, tức là có hiệu quả ngay. Chú ý: phần giải nghĩa thành ngữ này trong sách bị in nhầm thành nghĩa của 当仁不让; nghĩa đúng là hiệu quả tức thì."],
     "改革开放之后，从一九七九年开始，政府大幅度提高农产品的采购价格，农民收入随之提高，可谓立竿见影。"),
    ("改革开放之前的大量贫困人口，可以视为一种制度性贫困。农民在大锅饭体制下毫无生产积极性，加之农业为工业输血作出巨大牺牲，农村经济一片萧条。",
     "Số lượng lớn người nghèo trước cải cách mở cửa có thể coi là một kiểu nghèo do chế độ. Dưới thể chế nồi cơm chung, nông dân hoàn toàn không có tính tích cực sản xuất, thêm vào đó nông nghiệp phải hy sinh to lớn để truyền máu cho công nghiệp, nên kinh tế nông thôn tiêu điều xơ xác.",
     ["视为 là coi là. 制度性贫困 là nghèo do chế độ, khái niệm then chốt của bài. 毫无 là hoàn toàn không có. 加之 là thêm vào đó, văn viết.",
      "为工业输血 là truyền máu cho công nghiệp, tức là chuyển của cải từ nông nghiệp sang công nghiệp qua cánh kéo giá. 作出巨大牺牲 là hy sinh to lớn. 一片萧条 là tiêu điều xơ xác."]),
    ("改革开放之后，找准体制的症结，对症下药，长期被压抑的积极性得以激发，生产力得到极大解放，如此一来，不需要政府给予太多的扶持，农民自己就会成为减贫的最大推动力，他们发挥主观能动性，致力于脱贫，当仁不让。",
     "Sau cải cách mở cửa, tìm đúng căn bệnh của thể chế, bốc thuốc đúng bệnh, tính tích cực bị kìm nén bấy lâu được khơi dậy, sức sản xuất được giải phóng mạnh mẽ. Như vậy, không cần chính phủ hỗ trợ quá nhiều, bản thân nông dân sẽ trở thành động lực lớn nhất của giảm nghèo; họ phát huy tính năng động chủ quan, dốc sức thoát nghèo, không chút chối từ.",
     ["找准症结 là tìm đúng mấu chốt. 对症下药 là bốc thuốc đúng bệnh, thành ngữ có trong bài tập một; ở đây chữ 症 đọc thanh bốn. 得以激发 là được khơi dậy. 解放生产力 là giải phóng sức sản xuất.",
      "如此一来 là như vậy thì, kết quả là. 给予 đọc là jǐyǔ, nghĩa là dành cho. 主观能动性 là tính năng động chủ quan. 致力于 là dốc sức vào. 当仁不让 là thành ngữ: gặp việc nên làm thì chủ động làm, không nhường ai."]),
    ("“没有比人更高的山，没有比脚更长的路”，脱贫致富终究要靠群众的智慧和辛勤付出才能得以实现。",
     "“Không có ngọn núi nào cao hơn con người, không có con đường nào dài hơn đôi chân”, thoát nghèo làm giàu rốt cuộc phải dựa vào trí tuệ và sự lao động cần cù của quần chúng mới có thể thực hiện được.",
     ["没有比人更高的山，没有比脚更长的路 là một câu nói rất đẹp: núi cao mấy cũng không cao bằng ý chí con người, đường dài mấy cũng bị đôi chân đi hết. Tiếng Việt có câu: đường đi khó, không khó vì ngăn sông cách núi, mà khó vì lòng người ngại núi e sông.",
      "脱贫致富 là thoát nghèo làm giàu. 终究 là rốt cuộc. 辛勤付出 là sự bỏ công sức cần cù. 靠……才能得以实现 là phải dựa vào… mới thực hiện được. Thông điệp: chính sách chỉ mở đường, người dân mới là chủ thể."]),
    ("当前全球还有很多地区的贫困属于制度性贫困，而中国在改革开放之初用制度改革的红利消除贫困的经验，其实可以为很多贫困地区所借鉴。",
     "Hiện nay, nghèo đói ở nhiều khu vực trên thế giới vẫn thuộc loại nghèo do chế độ, mà kinh nghiệm của Trung Quốc dùng lợi ích từ cải cách chế độ để xóa nghèo hồi đầu cải cách mở cửa, thực ra có thể được nhiều vùng nghèo tham khảo.",
     ["当前 là hiện nay. 属于 là thuộc về. 红利 vốn là cổ tức, lợi tức; 制度改革的红利 là lợi ích do cải cách chế độ mang lại.",
      "为……所借鉴 là câu bị động văn viết theo mẫu 为A所B, được A làm B; chữ 为 ở đây đọc là wéi. 可以为很多贫困地区所借鉴 là có thể được nhiều vùng nghèo tham khảo. Đây là câu trả lời cho câu hỏi thứ hai ở đầu bài."]),
    ("不过，最大的难点在于，当年中国有足够的勇气解放思想，打破不合理体制的束缚，推进浩浩荡荡的改革开放，这样的改革开放需要“天时、地利、人和”的配合。而对于全球多数长期难以摆脱贫困的地区而言，“抄作业”并非易事。",
     "Tuy nhiên, khó khăn lớn nhất nằm ở chỗ: năm ấy Trung Quốc có đủ dũng khí giải phóng tư tưởng, phá bỏ sự trói buộc của thể chế bất hợp lý, đẩy mạnh công cuộc cải cách mở cửa rầm rộ, mà một cuộc cải cách mở cửa như thế cần sự phối hợp của “thiên thời, địa lợi, nhân hòa”. Còn đối với phần lớn các khu vực trên thế giới lâu nay khó thoát nghèo, “chép bài” không phải là chuyện dễ.",
     ["难点在于 là chỗ khó nằm ở. 解放思想 là giải phóng tư tưởng. 打破……的束缚 là phá bỏ sự trói buộc của…, mẫu câu thứ sáu. 浩浩荡荡 là cuồn cuộn, rầm rộ, vốn tả nước sông mênh mông.",
      "天时、地利、人和 là thiên thời, địa lợi, nhân hòa, giống hệt tiếng Việt. 抄作业 là chép bài tập, từ lóng mạng: rập khuôn kinh nghiệm của người khác. 并非易事 là hoàn toàn không phải chuyện dễ. Bài kết thúc khách quan: có kinh nghiệm, nhưng không dễ sao chép."]),
]

add("bullets", chapter="Bài khóa", section="Bài khóa 课文", title="Phần 2: Bài khóa 中国扶贫的道路选择", size=42,
    items=["Đọc từng đoạn: nghe tiếng Trung trước (chưa hiện bản dịch)",
           "Sau đó: bản dịch tiếng Việt + giải thích từ ngữ, cấu trúc",
           "Mẹo: tạm dừng, đọc to đoạn văn trước khi nghe giảng"],
    say=["Tiếp theo là phần hai: bài khóa. Bài lấy từ bài viết cùng tên 中国扶贫的道路选择 của tác giả 谢九, đăng trên tuần san 三联生活周刊, Tam Liên Sinh Hoạt Chu San, số bốn mươi, ngày ba mươi tháng chín năm hai nghìn không trăm hai mươi.",
         F(0, "Bài gốc có chín đoạn khá dài; thầy chia thành mười sáu đoạn ngắn. Với mỗi đoạn, các bạn nghe đọc tiếng Trung trước, cố gắng hiểu bằng các từ mới vừa học."),
         F(1, "Sau đó bản dịch tiếng Việt sẽ hiện ra, và thầy giải thích các từ ngữ, cấu trúc quan trọng."),
         F(2, "Bài có nhiều thuật ngữ chính trị, kinh tế và rất nhiều thành ngữ. Nếu muốn luyện đọc, các bạn hãy tạm dừng và tự đọc to đoạn văn trước khi nghe giảng nhé.")])

for i, item in enumerate(P, 1):
    zh, vi, notes = item[:3]
    spoken = item[3] if len(item) > 3 else zh.replace("“", "").replace("”", "")
    zsize = 54 if len(zh) <= 90 else 50 if len(zh) <= 115 else 46
    add("passage", section="Bài khóa 课文", title=f"Bài khóa – đoạn {i}/{len(P)}", zh=zh, vi=vi, zsize=zsize,
        say=[F(0, spoken, cap="(Nghe đọc đoạn văn tiếng Trung)", zr=150),
             F(1, "Dịch nghĩa: " + vi.replace("“", "").replace("”", ""), cap="")] + [F(1, n) for n in notes])

add("bullets", chapter="Bố cục & ghi chú", section="Bài khóa 课文", title="Bố cục bài khóa", size=33,
    items=["## 1. Nêu vấn đề (đoạn 1): 数亿贫困人口清零 → 如何做到？能否借鉴？",
           "## 2. Gốc rễ của nghèo (đoạn 2): 不合理的计划经济体制 → 必须彻底改革制度",
           "## 3. Ba động lực giảm nghèo (đoạn 3–11)",
           "① 家庭联产承包责任制: 取代人民公社，抛弃大锅饭 · ② 乡镇企业: 如雨后春笋",
           "③ 国家政策扶持: 消除剪刀差，提高农产品采购价格 → 立竿见影",
           "## 4. Tổng kết (đoạn 12–14): 制度性贫困 → 改革激发积极性，农民是减贫的最大推动力",
           "## 5. Giá trị tham khảo và khó khăn (đoạn 15–16): 天时、地利、人和 · “抄作业”并非易事"],
    say=["Trước khi sang phần mẫu câu, chúng ta cùng nhìn lại bố cục bài khóa. Bài có năm phần, lập luận theo kiểu nêu vấn đề, phân tích nguyên nhân, đưa ra lời giải.",
         F(0, "Phần một, nêu vấn đề: Trung Quốc đã đưa mấy trăm triệu người nghèo về không. Vậy làm thế nào, và kinh nghiệm ấy có tham khảo được không?"),
         F(1, "Phần hai, gốc rễ của nghèo đói: thể chế kinh tế kế hoạch bất hợp lý; vì thế phải cải cách triệt để chế độ."),
         F(2, "Phần ba, ba động lực giảm nghèo."),
         F(3, "Thứ nhất là chế độ khoán sản lượng đến hộ gia đình, thay thế công xã nhân dân, xóa bỏ nồi cơm chung. Thứ hai là doanh nghiệp hương trấn, mọc lên như nấm sau mưa."),
         F(4, "Thứ ba là chính sách hỗ trợ của nhà nước: thu hẹp cánh kéo giá, nâng giá thu mua nông sản, hiệu quả thấy ngay."),
         F(5, "Phần bốn, tổng kết: nghèo trước kia là nghèo do chế độ; cải cách đã khơi dậy tính tích cực, và chính nông dân là động lực lớn nhất của giảm nghèo."),
         F(6, "Phần năm, giá trị tham khảo và khó khăn: kinh nghiệm Trung Quốc có thể tham khảo, nhưng cần thiên thời, địa lợi, nhân hòa, nên chép bài không phải chuyện dễ.")])

add("bullets", section="Bài khóa 课文", title="Ghi chú 注释: hiểu thêm về bối cảnh", size=30,
    items=["十一届三中全会 (18–22/12/1978): chuyển trọng tâm sang xây dựng hiện đại hóa → mở ra thời kỳ cải cách mở cửa, “bước ngoặt vĩ đại”",
           "家庭联产承包责任制: hộ nông dân nhận khoán ruộng đất từ tập thể · Văn kiện số 1 (1/1/1982) khẳng định 包产到户、包干到户 · “7% đất đai thế giới nuôi 22% dân số thế giới”",
           "乡镇企业: doanh nghiệp tập thể, hợp tác, cá thể ở xã, thị trấn · 1987: giá trị sản lượng lần đầu vượt nông nghiệp · 2008: chiếm 71,21% giá trị gia tăng nông thôn",
           "人民公社 (1958–1983): “一大二公” – quy mô lớn, công hữu cao · đội sản xuất lập nhà ăn công cộng → “大锅饭”",
           "剪刀差: hàng công nghiệp giá cao hơn giá trị, nông sản giá thấp hơn giá trị; biểu đồ hình cái kéo mở"],
    say=["Sách có năm ghi chú giúp hiểu thêm bối cảnh bài khóa.",
         F(0, "Một: 十一届三中全会, họp từ ngày mười tám đến hai mươi hai tháng mười hai năm một nghìn chín trăm bảy mươi tám tại Bắc Kinh. Hội nghị quyết định chuyển trọng tâm công tác sang xây dựng hiện đại hóa, đánh dấu Trung Quốc bước vào thời kỳ cải cách mở cửa; sách gọi đây là một bước ngoặt vĩ đại trong lịch sử Trung Quốc."),
         F(1, "Hai: 家庭联产承包责任制. Nông dân lấy hộ gia đình làm đơn vị, nhận khoán ruộng đất và nhiệm vụ sản xuất từ tổ chức kinh tế tập thể là thôn, tổ. Ngày một tháng một năm một nghìn chín trăm tám mươi hai, Văn kiện số một đầu tiên về nông thôn khẳng định khoán sản lượng đến hộ và khoán gọn đến hộ đều là chế độ trách nhiệm của kinh tế tập thể. Nhờ đó Trung Quốc tạo ra kỳ tích dùng bảy phần trăm đất đai của thế giới nuôi hai mươi hai phần trăm dân số thế giới."),
         F(2, "Ba: 乡镇企业, tên gọi chung các doanh nghiệp tập thể, hợp tác và cá thể do tổ chức kinh tế ở xã, thị trấn, thôn hoặc nông dân lập ra. Năm một nghìn chín trăm tám mươi bảy, giá trị sản lượng của chúng lần đầu vượt tổng giá trị sản lượng nông nghiệp; đến năm hai nghìn không trăm lẻ tám, chúng chiếm bảy mươi mốt phẩy hai mốt phần trăm giá trị gia tăng của xã hội nông thôn."),
         F(3, "Bốn: 人民公社, công xã nhân dân, tồn tại từ năm một nghìn chín trăm năm mươi tám đến năm một nghìn chín trăm tám mươi ba, đặc điểm được tóm tắt là 一大二公: một là lớn, quy mô lớn; hai là công, mức độ công hữu tư liệu sản xuất cao. Các đội sản xuất khắp nơi đều lập nhà ăn công cộng, nên còn gọi là 大锅饭."),
         F(4, "Năm: 剪刀差. Khi trao đổi hàng công nghiệp và nông sản, giá hàng công nghiệp cao hơn giá trị, giá nông sản thấp hơn giá trị; vẽ lên biểu đồ thì hai đường mở ra như lưỡi kéo, nên gọi là cánh kéo giá.")])

add("bullets", section="Bài khóa 课文", title="Phim gợi ý 推荐电视剧: 《大江大河》(2018)", size=33,
    items=["Bối cảnh: nông thôn và nhà máy Trung Quốc từ năm 1978, thời cải cách mở cửa",
           "宋运辉: xuất thân bị kỳ thị, nắm lấy kỳ thi đại học 1978 → kỹ sư doanh nghiệp nhà nước → 国营经济",
           "雷东宝: anh rể của Vận Huy, “大老粗” hành động mạnh, dẫn dân làng cải cách → 集体经济",
           "杨巡: hộ kinh doanh cá thể, xoay xở giữa cơ hội và cạm bẫy → 个体经济",
           "Từ đáng học: 抓住机遇 · 勤学苦干 · 紧跟政策 · 走在时代的前沿 · 日新月异 · 几经波折"],
    say=["Sách giới thiệu một bộ phim truyền hình rất nổi tiếng, giúp hiểu thêm bối cảnh bài khóa: 大江大河, Sông lớn, chiếu năm hai nghìn không trăm mười tám.",
         F(0, "Phim kể chuyện những con người ở nông thôn và nhà máy Trung Quốc từ năm một nghìn chín trăm bảy mươi tám, đúng thời điểm cải cách mở cửa bắt đầu."),
         F(1, "Nhân vật thứ nhất, 宋运辉, thông minh nhưng xuất thân không tốt nên luôn bị kỳ thị. Anh nắm lấy cơ hội khôi phục kỳ thi đại học năm một nghìn chín trăm bảy mươi tám, chăm học chăm làm, trở thành kỹ sư của doanh nghiệp nhà nước, đại diện cho kinh tế quốc doanh."),
         F(2, "Nhân vật thứ hai, 雷东宝, anh rể của Vận Huy, xuất thân nghèo khó, là một 大老粗, người thô kệch ít học nhưng dám nghĩ dám làm. Anh dẫn dân làng theo sát chính sách, luôn đi đầu thời đại, nhưng vì trình độ văn hóa có hạn mà cuối cùng vấp ngã trước cái mới. Anh đại diện cho kinh tế tập thể."),
         F(3, "Nhân vật thứ ba, 杨巡, hộ kinh doanh cá thể. Giữa thời đại thay đổi từng ngày, anh luống cuống nắm lấy cơ hội, cũng từng sa vào cạm bẫy, trải qua bao sóng gió rồi mới có cơ nghiệp riêng. Anh đại diện cho kinh tế cá thể."),
         F(4, "Những cụm từ đáng học trong phần giới thiệu phim: 抓住机遇, nắm bắt cơ hội; 勤学苦干, chăm học chịu khó; 紧跟政策, theo sát chính sách; 走在时代的前沿, đi đầu thời đại; 日新月异, thay đổi từng ngày; 几经波折, trải qua nhiều trắc trở. Phần viết của ôn tập đơn vị cũng có một đề về nhân vật 杨巡.")])

# ======================= MẪU CÂU =======================
add("bullets", chapter="Mẫu câu: 载入史册 · 归根到底 · 意想不到的是", section="Mẫu câu 重点句型", title="1. 载入……（的）史册 · 2. 归根到底", size=32,
    items=["## 载入……（的）史册: ghi vào sử sách (thành tựu, sự kiện có ý nghĩa lịch sử)",
           "这一成就被称为奇迹当之无愧，足以载入人类社会发展的史册。",
           "《流浪地球》是一部非常优秀的国产硬科幻大作，可以载入中国电影史册。",
           "2008年8月8日注定是载入史册的一天，这一天，第二十九届夏季奥运会在北京拉开帷幕。",
           "## 归根到底 (= 归根结底): suy cho cùng, xét đến cùng",
           "贫困问题归根到底是由于不合理的计划经济体制造成的。",
           "任何重大的成功，归根到底都是用人的成功。同理，任何重大的失败，说到底都是用人的失败。"],
    say=["Bây giờ chúng ta sang phần mẫu câu trọng điểm. Bài có sáu mẫu, thầy chia thành ba slide.",
         F(0, "Mẫu thứ nhất: 载入史册, ghi vào sử sách. Ở giữa có thể thêm định ngữ: 载入人类社会发展的史册, 载入中国电影史册. Dùng cho thành tựu hay sự kiện có ý nghĩa lịch sử. Chữ 载 đọc là zǎi."),
         F(1, "Ví dụ một, lấy từ bài khóa: 这一成就被称为奇迹当之无愧，足以载入人类社会发展的史册。"),
         F(2, "Ví dụ hai: 流浪地球是一部非常优秀的国产硬科幻大作，可以载入中国电影史册。 Lưu lạc Địa Cầu là một bom tấn khoa học viễn tưởng nội địa rất xuất sắc, có thể ghi vào lịch sử điện ảnh Trung Quốc."),
         F(3, "Ví dụ ba: 二零零八年八月八日注定是载入史册的一天，这一天，第二十九届夏季奥运会在北京拉开帷幕。 Ngày tám tháng tám năm hai nghìn không trăm lẻ tám chắc chắn là ngày đi vào lịch sử: Thế vận hội mùa hè lần thứ hai mươi chín khai mạc tại Bắc Kinh. Ở đây lại gặp 拉开帷幕."),
         F(4, "Mẫu thứ hai: 归根到底, còn nói là 归根结底, nghĩa là suy cho cùng. Thường đứng trước vị ngữ, dẫn ra nguyên nhân hay bản chất sâu xa nhất."),
         F(5, "Ví dụ một, lấy từ bài khóa: 贫困问题归根到底是由于不合理的计划经济体制造成的。 Sách còn có ví dụ: 当今社会的所有竞争归根到底是人才的竞争, mọi cạnh tranh trong xã hội ngày nay suy cho cùng là cạnh tranh nhân tài."),
         F(6, "Ví dụ ba: 任何重大的成功，归根到底都是用人的成功。同理，任何重大的失败，说到底都是用人的失败。 Mọi thành công lớn suy cho cùng đều là thành công trong việc dùng người; cũng vậy, mọi thất bại lớn nói cho cùng đều là thất bại trong việc dùng người. 说到底 là cách nói khẩu ngữ hơn.")])

add("bullets", section="Mẫu câu 重点句型", title="3. （让人/令人）意想不到的是 · 4. 事关……", size=32,
    items=["## （让人/令人）意想不到的是，……: điều không ngờ là… (kết quả hoàn toàn bất ngờ)",
           "意想不到的是，“无心插柳柳成荫”，改革的成就却最终在农村凸显出来。",
           "让人意想不到的是，这支实力不错的球队居然大败而归。",
           "评奖结果终于公布，意想不到的是，今年这部低成本电影获得了评委们的一致好评。",
           "## 事关……: việc này liên quan đến… (điều hệ trọng)",
           "家庭联产承包制度的推进事关农民的切身利益……",
           "事关大众权益，我们绝不能冷眼旁观，袖手不管。 · ……主权问题事关重大，处理不当甚至会引发冲突。"],
    say=[F(0, "Mẫu thứ ba: 意想不到的是, điều không ngờ là. Phía trước có thể thêm 让人 hoặc 令人: 让人意想不到的是. Vế sau nêu một kết quả hoàn toàn bất ngờ, thường đi với 却，居然，竟然."),
         F(1, "Ví dụ một, lấy từ bài khóa: 意想不到的是，无心插柳柳成荫，改革的成就却最终在农村凸显出来。"),
         F(2, "Ví dụ hai: 让人意想不到的是，这支实力不错的球队居然大败而归。 Điều không ai ngờ là đội bóng có thực lực khá này lại thua đậm trở về."),
         F(3, "Ví dụ ba: 评奖结果终于公布，意想不到的是，今年这部低成本电影获得了评委们的一致好评。 Kết quả giải thưởng cuối cùng cũng công bố; điều không ngờ là bộ phim kinh phí thấp năm nay lại được ban giám khảo nhất trí khen ngợi."),
         F(4, "Mẫu thứ tư: 事关, nghĩa là việc này liên quan đến. Phía sau thường là những điều hệ trọng: 事关安全，事关责任，事关利益. Cụm cố định 事关重大 là việc hệ trọng."),
         F(5, "Ví dụ một, lấy từ bài khóa: 家庭联产承包制度的推进事关农民的切身利益。"),
         F(6, "Ví dụ hai: 事关大众权益，我们绝不能冷眼旁观，袖手不管。 Việc liên quan đến quyền lợi của đại chúng, chúng ta tuyệt đối không thể lạnh lùng đứng nhìn, khoanh tay mặc kệ. Và: 在国际关系的现实世界中，主权问题事关重大，处理不当甚至会引发冲突。 Trong quan hệ quốc tế, vấn đề chủ quyền là hệ trọng, xử lý không khéo thậm chí có thể gây xung đột.")])

add("bullets", chapter="Mẫu câu: 继…之后 · 打破…的束缚", section="Mẫu câu 重点句型", title="5. 继……之后 · 6. 打破……（的）束缚", size=32,
    items=["## 继……之后: tiếp sau… (một sự việc tiếp nối sự việc trước)",
           "乡镇企业的崛起，成为继家庭联产承包责任制之后，农村减贫的第二大推动力。",
           "继这起案件之后，国家又陆续出台了更详尽的法律法规。",
           "继那次火灾之后，邻居们的安全防范意识都有所增强。",
           "## 打破……（的）束缚: phá bỏ sự trói buộc, hạn chế của…",
           "当年中国有足够的勇气解放思想，打破不合理体制的束缚……",
           "新型企业管理必须打破旧观念的束缚，建立一种全新的用人制度。",
           "她们打破了传统观念的束缚，成为中国第一批飞上蓝天的女性。"],
    say=[F(0, "Mẫu thứ năm: 继之后, tiếp sau. 继 là tiếp nối. Mẫu này văn viết, nối hai sự việc theo thứ tự: sau sự việc thứ nhất, lại có sự việc thứ hai, thường kèm 又，也，第二."),
         F(1, "Ví dụ một, lấy từ bài khóa: 乡镇企业的崛起，成为继家庭联产承包责任制之后，农村减贫的第二大推动力。 Chữ 第二 cho thấy rõ thứ tự."),
         F(2, "Ví dụ hai: 继这起案件之后，国家又陆续出台了更详尽的法律法规。 Tiếp sau vụ án này, nhà nước lại lần lượt ban hành những luật lệ chi tiết hơn."),
         F(3, "Ví dụ ba: 继那次火灾之后，邻居们的安全防范意识都有所增强。 Sau vụ hỏa hoạn ấy, ý thức phòng ngừa an toàn của hàng xóm đều được nâng lên. 有所 cộng động từ là có phần, ít nhiều."),
         F(4, "Mẫu thứ sáu: 打破的束缚, phá bỏ sự trói buộc của một thứ gì đó. Ở giữa thường là 体制，观念，传统: 打破旧观念的束缚, 打破传统观念的束缚."),
         F(5, "Ví dụ một, lấy từ bài khóa: 当年中国有足够的勇气解放思想，打破不合理体制的束缚。"),
         F(6, "Ví dụ hai: 新型企业管理必须打破旧观念的束缚，建立一种全新的用人制度。 Quản lý doanh nghiệp kiểu mới phải phá bỏ sự trói buộc của quan niệm cũ, xây dựng một chế độ dùng người hoàn toàn mới."),
         F(7, "Ví dụ ba: 她们打破了传统观念的束缚，成为中国第一批飞上蓝天的女性。 Họ đã phá bỏ sự trói buộc của quan niệm truyền thống, trở thành lớp phụ nữ đầu tiên của Trung Quốc bay lên bầu trời, tức là những nữ phi công đầu tiên.")])

add("bullets", section="Mẫu câu 重点句型", title="Luyện tập (1): điền mẫu câu thích hợp", reveal=True, size=35,
    items=["(1) 这场比赛的胜利将___中国体育___。",
           "Đáp án: 载入……史册 → 将载入中国体育史册",
           "(2) 他成绩不好，___还是因为不够努力。",
           "Đáp án: 归根到底",
           "(3) 大家都以为他会输，___，他最后得了冠军。",
           "Đáp án: 意想不到的是"],
    say=["Bây giờ chúng ta luyện tập nhanh sáu mẫu câu vừa học. Thầy đọc câu, các bạn tạm dừng chọn mẫu, rồi nghe đáp án nhé.",
         F(0, "Câu một: 这场比赛的胜利将什么中国体育什么。 Chiến thắng của trận đấu này sẽ được ghi vào lịch sử thể thao Trung Quốc."),
         F(1, "Đáp án: 载入史册. 这场比赛的胜利将载入中国体育史册。"),
         F(2, "Câu hai: 他成绩不好，什么还是因为不够努力。 Thành tích của cậu ấy kém, suy cho cùng vẫn là do chưa đủ cố gắng."),
         F(3, "Đáp án: 归根到底. Dẫn ra nguyên nhân sâu xa nhất."),
         F(4, "Câu ba: 大家都以为他会输，什么，他最后得了冠军。 Ai cũng tưởng anh ấy sẽ thua; điều không ngờ là cuối cùng anh ấy lại vô địch."),
         F(5, "Đáp án: 意想不到的是. Kết quả trái ngược hẳn với dự đoán.")])

add("bullets", section="Mẫu câu 重点句型", title="Luyện tập (2): điền mẫu câu thích hợp", reveal=True, size=35,
    items=["(4) 食品安全___每个人的健康，必须高度重视。",
           "Đáp án: 事关",
           "(5) ___北京___，上海也出台了类似的政策。",
           "Đáp án: 继……之后 → 继北京之后",
           "(6) 年轻人要敢于___传统观念的___，勇于创新。",
           "Đáp án: 打破……束缚"],
    say=[F(0, "Câu bốn: 食品安全什么每个人的健康，必须高度重视。 An toàn thực phẩm liên quan đến sức khỏe của mỗi người, phải hết sức coi trọng."),
         F(1, "Đáp án: 事关. 食品安全事关每个人的健康。"),
         F(2, "Câu năm: 什么北京什么，上海也出台了类似的政策。 Tiếp sau Bắc Kinh, Thượng Hải cũng ban hành chính sách tương tự."),
         F(3, "Đáp án: 继北京之后. Chữ 也 ở vế sau là gợi ý."),
         F(4, "Câu sáu: 年轻人要敢于什么传统观念的什么，勇于创新。 Người trẻ phải dám phá bỏ sự trói buộc của quan niệm truyền thống, mạnh dạn đổi mới."),
         F(5, "Đáp án: 打破传统观念的束缚.")])

# ======================= KẾT HỢP TỪ =======================
add("bullets", chapter="Kết hợp từ (6 từ)", section="Kết hợp từ 词语搭配", title="Kết hợp từ (1): 寥寥 · 蓬勃 · 空前", size=32,
    items=["## 寥寥: ～无几 · ～数语 · ～几笔 · ～几字",
           "初冬时节，树上寥寥无几的叶子，在寒风中瑟瑟发抖。 · 老师的评语虽只寥寥数语，却是入木三分。",
           "## 蓬勃: ～发展 · 朝气～ · ～生长 · ～气象",
           "看着自己几年来的事业蓬勃发展起来了，他感到无比欣慰。",
           "我们青少年应该精神饱满，朝气蓬勃。",
           "## 空前: ～高涨 · ～成功 · ～发展 · 盛况～",
           "这部电视剧的空前成功，让市场的目光再次聚焦到职业女性题材。"],
    say=["Tiếp theo là phần kết hợp từ, 词语搭配. Bài này có sáu từ, thầy chia thành hai slide.",
         F(0, "Từ thứ nhất: 寥寥, rất ít. Đi với 无几，数语，几笔，几字: 寥寥无几, chẳng được mấy; 寥寥数语, vài ba câu; 寥寥几笔, vài nét vẽ. Trong bài: 成效寥寥."),
         F(1, "Ví dụ: 初冬时节，树上寥寥无几的叶子，在寒风中瑟瑟发抖。 Đầu đông, mấy chiếc lá thưa thớt trên cây run rẩy trong gió lạnh. Và: 老师的评语虽只寥寥数语，却是入木三分。 Lời phê của thầy tuy chỉ vài câu, nhưng sâu sắc thấu đáo. 入木三分 là ăn sâu vào gỗ ba phân, chỉ sự sâu sắc."),
         F(2, "Từ thứ hai: 蓬勃, mạnh mẽ, tràn đầy sức sống. Đi với 发展，生长，气象, và cụm 朝气蓬勃, tràn đầy sức sống, chữ 朝 ở đây đọc là zhāo. Trong bài: 乡镇企业随之蓬勃兴起."),
         F(3, "Ví dụ: 看着自己几年来的事业蓬勃发展起来了，他感到无比欣慰。 Nhìn sự nghiệp mấy năm nay của mình phát triển mạnh mẽ, anh ấy vô cùng mãn nguyện."),
         F(4, "Và: 我们青少年应该精神饱满，朝气蓬勃。 Thanh thiếu niên chúng ta phải tinh thần phấn chấn, tràn đầy sức sống."),
         F(5, "Từ thứ ba: 空前, chưa từng có. Đi với 高涨，成功，发展, và cụm 盛况空前, cảnh tượng sôi động chưa từng thấy."),
         F(6, "Ví dụ: 这部电视剧的空前成功，让市场的目光再次聚焦到职业女性题材。 Thành công chưa từng có của bộ phim truyền hình này khiến thị trường lại tập trung vào đề tài phụ nữ đi làm. Và: 改革开放以来，我国各个领域都得到了空前的发展。 Từ khi cải cách mở cửa, mọi lĩnh vực của nước ta đều phát triển chưa từng có.")])

add("bullets", section="Kết hợp từ 词语搭配", title="Kết hợp từ (2): 高涨 · 大幅 · 激发", size=32,
    items=["## 高涨: 热情～ · 空前～ · 情绪～ · 日益～",
           "2008年奥运会之后，群众对体育运动的热情日益高涨。",
           "## 大幅: ～提高 · ～上涨 · ～下降 · ～反弹",
           "为抑制投资炒房和房价大幅上涨，金融政策收紧已是大势所趋。",
           "商品价格的大幅下降，大大地刺激了顾客的购买力。",
           "## 激发: ～热情 · ～斗志 · ～激情 · ～兴趣",
           "落后两球的险恶形势，反而激发起队员们的斗志，使他们在补时阶段连进三球，反败为胜。"],
    say=[F(0, "Từ thứ tư: 高涨, dâng cao. Đi với 热情高涨，空前高涨，情绪高涨，日益高涨. Trong bài: 农民的生产积极性空前高涨."),
         F(1, "Ví dụ: 二零零八年奥运会之后，群众对体育运动的热情日益高涨。 Sau Olympic năm hai nghìn không trăm lẻ tám, nhiệt tình của quần chúng với thể thao ngày càng dâng cao. Sách còn có: 农民们学科学、用科学的积极性空前高涨."),
         F(2, "Từ thứ năm: 大幅, biên độ lớn. Đi với 提高，上涨，下降，反弹. 反弹 là bật tăng trở lại. Trong bài: 主要农产品的产量大幅提升."),
         F(3, "Ví dụ: 为抑制投资炒房和房价大幅上涨，金融政策收紧已是大势所趋。 Để kiềm chế đầu cơ nhà đất và giá nhà tăng mạnh, thắt chặt chính sách tài chính đã là xu thế tất yếu. 炒房 là đầu cơ nhà đất."),
         F(4, "Và: 商品价格的大幅下降，大大地刺激了顾客的购买力。 Giá hàng giảm mạnh đã kích thích rất lớn sức mua của khách hàng."),
         F(5, "Từ thứ sáu: 激发, khơi dậy. Đi với 热情，斗志，激情，兴趣. Trong bài: 长期被压抑的积极性得以激发."),
         F(6, "Ví dụ: 落后两球的险恶形势，反而激发起队员们的斗志，使他们在补时阶段连进三球，反败为胜。 Tình thế hiểm nghèo bị dẫn hai bàn lại khơi dậy ý chí chiến đấu của các cầu thủ, giúp họ ghi liền ba bàn trong thời gian bù giờ, lội ngược dòng giành chiến thắng. 反败为胜 là chuyển bại thành thắng.")])

# ======================= THÀNH NGỮ =======================
add("bullets", chapter="Thành ngữ (13)", section="Thành ngữ 成语和惯用语", title="Thành ngữ (1): 当之无愧 · 有心栽花花不开 · 无心插柳柳成荫", size=32,
    items=["## 当之无愧 dāngzhīwúkuì: xứng đáng, nhận danh hiệu mà không hổ thẹn",
           "感谢新冠疫情期间奋战在第一线的医护人员，他们是当之无愧的白衣天使。",
           "## 有心栽花花不开: cố công trồng hoa hoa chẳng nở – dốc sức mà không như ý",
           "人人都愿美梦成真，但有心栽花花不开，很多时候总是事与愿违。",
           "## 无心插柳柳成荫: vô tình cắm liễu liễu lại xanh – không cố ý mà thành công",
           "想不到我举手之劳，竟使众人受惠，真是无心插柳柳成荫。"],
    say=["Bây giờ là phần thành ngữ và quán ngữ. Bài có mười ba cụm, nhiều nhất trong đơn vị; thầy chia thành bốn slide.",
         F(0, "Thành ngữ thứ nhất: 当之无愧. 当 đọc là dāng, là nhận lấy, đảm đương; 无愧 là không hổ thẹn. Nhận danh hiệu hay vinh dự ấy hoàn toàn xứng đáng. Trong bài: 这一成就被称为奇迹当之无愧."),
         F(1, "Ví dụ: 感谢新冠疫情期间奋战在第一线的医护人员，他们是当之无愧的白衣天使。 Cảm ơn các y bác sĩ chiến đấu ở tuyến đầu trong dịch Covid, họ xứng đáng là những thiên thần áo trắng."),
         F(2, "Tục ngữ thứ hai: 有心栽花花不开. Cố công trồng hoa, hoa lại không nở: dồn nhiều tâm sức làm một việc mà kết quả không như ý. Trong bài: 有心栽花花不开，那一轮国企改革成效寥寥."),
         F(3, "Ví dụ: 人人都愿美梦成真，但有心栽花花不开，很多时候总是事与愿违。 Ai cũng mong giấc mơ đẹp thành hiện thực, nhưng cố trồng hoa hoa chẳng nở, nhiều khi sự việc lại trái với mong muốn. 事与愿违 là việc trái với ý nguyện."),
         F(4, "Tục ngữ thứ ba: 无心插柳柳成荫. Tiện tay cắm cành liễu xuống đất, không ngờ thành cây liễu xanh um: việc làm không cố ý lại thu được kết quả tốt. Câu này thường đi đôi với câu trước, như trong bài khóa. Chữ cuối đọc là yīn."),
         F(5, "Ví dụ: 想不到我举手之劳，竟使众人受惠，真是无心插柳柳成荫。 Không ngờ việc nhỏ như nhấc tay của tôi lại khiến bao người được lợi, đúng là vô tình cắm liễu liễu lại xanh. 举手之劳 là việc dễ như nhấc tay.")])

add("bullets", section="Thành ngữ 成语和惯用语", title="Thành ngữ (2): 说一千道一万 · 雨后春笋 · 轰轰烈烈", size=32,
    items=["## 说一千道一万: nói nghìn câu vạn lời (thì điều cốt lõi vẫn là…)",
           "他们一直坚信，实践才是硬道理，说一千道一万，还不如好好干一场。",
           "## 雨后春笋 yǔhòu-chūnsǔn: măng xuân sau mưa – như nấm mọc sau mưa",
           "深圳当年是个小渔村，在改革开放成为特区之后，高楼大厦如雨后春笋般拔地而起。",
           "## 轰轰烈烈 hōnghōng-lièliè: rầm rộ, sôi nổi, khí thế lớn",
           "得到了全家人的支持后，他准备去上海轰轰烈烈地干一番事业。"],
    say=[F(0, "Quán ngữ thứ tư: 说一千道一万, còn nói là 说千道万: nói nghìn câu, bàn vạn lời. Ý là dù nói bao nhiêu đi nữa thì điều cốt lõi vẫn là cái sắp nói ra. Trong bài: 说一千、道一万，增加农民收入是关键."),
         F(1, "Ví dụ: 他们一直坚信，实践才是硬道理，说一千道一万，还不如好好干一场。 Họ luôn tin rằng thực tiễn mới là chân lý, nói nghìn câu vạn lời chẳng bằng bắt tay làm cho tử tế. 硬道理 là đạo lý cứng, chân lý không thể bác bỏ."),
         F(2, "Thành ngữ thứ năm: 雨后春笋. Sau cơn mưa xuân, măng tre mọc lên hàng loạt: ví với sự vật mới xuất hiện nhanh và nhiều. Thường dùng 如雨后春笋般 cộng động từ. Tiếng Việt nói như nấm mọc sau mưa."),
         F(3, "Ví dụ: 深圳当年是个小渔村，在改革开放成为特区之后，高楼大厦如雨后春笋般拔地而起。 Thâm Quyến năm xưa là một làng chài nhỏ; sau khi thành đặc khu thời cải cách mở cửa, nhà cao tầng mọc lên như nấm sau mưa. 拔地而起 là vươn lên từ mặt đất."),
         F(4, "Thành ngữ thứ sáu: 轰轰烈烈. 轰轰 là tiếng nổ vang, 烈烈 là lửa cháy rừng rực: tả sự nghiệp hưng thịnh, khí thế lớn lao, rầm rộ. Trong bài: 轰轰烈烈的制度改革."),
         F(5, "Ví dụ: 得到了全家人的支持后，他准备去上海轰轰烈烈地干一番事业。 Được cả nhà ủng hộ, anh ấy chuẩn bị lên Thượng Hải làm nên một sự nghiệp lừng lẫy. Sách còn có câu: 谈一场轰轰烈烈的恋爱, yêu một cuộc tình nồng nhiệt, cháy bỏng.")])

add("bullets", section="Thành ngữ 成语和惯用语", title="Thành ngữ (3): 至关重要 · 立竿见影 · 当仁不让", size=32,
    items=["## 至关重要 zhìguān-zhòngyào: vô cùng quan trọng",
           "这件事情至关重要，我们不能贸然作出决定。",
           "## 立竿见影 lìgān-jiànyǐng: dựng sào thấy bóng – hiệu quả tức thì",
           "新厂长采取的新管理方法产生了立竿见影的效果。",
           "## 当仁不让 dāngrén-bùràng: gặp việc nên làm thì chủ động làm, không chối từ",
           "社会各界发起的“希望工程”捐款活动，我当仁不让，把这个月的工资全部捐献了出去。"],
    say=[F(0, "Thành ngữ thứ bảy: 至关重要, vô cùng quan trọng. 至 là cực kỳ, 关 là liên quan. Hay gặp: 起到了至关重要的作用, có tác dụng vô cùng quan trọng."),
         F(1, "Ví dụ: 这件事情至关重要，我们不能贸然作出决定。 Việc này vô cùng quan trọng, chúng ta không thể vội vàng quyết định. Sách còn có: 他演讲中的这番话，起到了至关重要的作用，堪称画龙点睛之笔, câu nói ấy trong bài diễn thuyết có tác dụng then chốt, đúng là nét vẽ điểm mắt cho rồng."),
         F(2, "Thành ngữ thứ tám: 立竿见影. Dựng cây sào dưới nắng là thấy ngay bóng: ví với việc có hiệu quả ngay lập tức. Lưu ý: sách in nhầm phần giải nghĩa thành ẩn ý của 当仁不让; nghĩa đúng là hiệu quả tức thì, như các ví dụ của chính sách đều cho thấy."),
         F(3, "Ví dụ: 新厂长采取的新管理方法产生了立竿见影的效果。 Phương pháp quản lý mới của giám đốc nhà máy mới đã mang lại hiệu quả tức thì. Sách còn có câu đùa: 一到夏天，她就恨不得找个立竿见影的减肥方法, cứ đến mùa hè là cô ấy chỉ mong tìm được cách giảm cân thấy hiệu quả ngay."),
         F(4, "Thành ngữ thứ chín: 当仁不让. Gặp việc nhân nghĩa thì không nhường ai, tức là gặp việc nên làm thì chủ động gánh vác, không chối từ. Chữ đầu đọc là dāng."),
         F(5, "Ví dụ: 社会各界发起的希望工程捐款活动，我当仁不让，把这个月的工资全部捐献了出去。 Trong đợt quyên góp cho Công trình Hy vọng do các giới phát động, tôi không chút chối từ, quyên góp toàn bộ lương tháng này. 希望工程 là chương trình giúp trẻ em nghèo được đi học.")])

add("bullets", section="Thành ngữ 成语和惯用语", title="Thành ngữ (4): 浩浩荡荡 · 天时地利人和 · 抄作业 · 日新月异", size=31,
    items=["## 浩浩荡荡 hàohào-dàngdàng: cuồn cuộn mênh mông; (đoàn người) rầm rộ, hùng hậu",
           "军队浩浩荡荡地向远方行进着，场面十分壮观。",
           "## 天时地利人和: thiên thời, địa lợi, nhân hòa – mọi điều kiện đều thuận lợi",
           "这支球队有着天时地利人和的主场优势，是夺冠的热门球队。",
           "## 抄作业 chāo zuòyè: (từ lóng) chép bài – rập khuôn kinh nghiệm người khác",
           "在培养孩子的过程中，家长不要一味地“抄作业”，应该根据孩子的实际情况来选择合适的教育方式。",
           "## 日新月异 rìxīn-yuèyì: ngày một mới, tháng một khác – thay đổi từng ngày",
           "微电子技术的发展日新月异，给我们的生活和工作带来了巨大的变化。"],
    say=[F(0, "Thành ngữ thứ mười: 浩浩荡荡. Vốn tả dòng nước mênh mông cuồn cuộn, sau tả sự vật rộng lớn, hoặc đoàn người tiến lên rầm rộ, hùng hậu. Trong bài: 推进浩浩荡荡的改革开放."),
         F(1, "Ví dụ: 军队浩浩荡荡地向远方行进着，场面十分壮观。 Đoàn quân rầm rộ tiến về phía xa, cảnh tượng vô cùng hùng tráng. Sách còn có câu: 望着长江的水浩浩荡荡地向东流去, nhìn nước Trường Giang cuồn cuộn chảy về đông."),
         F(2, "Thành ngữ thứ mười một: 天时地利人和, thiên thời, địa lợi, nhân hòa. Vốn nói về điều kiện khi đánh trận: khí hậu, địa thế, lòng người; ở đây chỉ mọi điều kiện đều thuận lợi. Tiếng Việt dùng y hệt."),
         F(3, "Ví dụ: 这支球队有着天时地利人和的主场优势，是夺冠的热门球队。 Đội bóng này có lợi thế sân nhà hội đủ thiên thời địa lợi nhân hòa, là ứng viên nặng ký cho chức vô địch."),
         F(4, "Quán ngữ thứ mười hai: 抄作业, chép bài tập. Từ lóng trên mạng, chỉ việc rập khuôn kinh nghiệm của người khác. Trong bài: 抄作业并非易事."),
         F(5, "Ví dụ: 在培养孩子的过程中，家长不要一味地抄作业，应该根据孩子的实际情况来选择合适的教育方式。 Khi nuôi dạy con, cha mẹ đừng chỉ biết rập khuôn người khác, mà nên chọn cách giáo dục phù hợp với thực tế của con mình."),
         F(6, "Thành ngữ thứ mười ba: 日新月异, ngày một mới, tháng một khác: tiến bộ, phát triển rất nhanh. Thành ngữ này có trong phần giới thiệu phim 大江大河."),
         F(7, "Ví dụ: 微电子技术的发展日新月异，给我们的生活和工作带来了巨大的变化。 Công nghệ vi điện tử phát triển từng ngày, mang lại thay đổi to lớn cho cuộc sống và công việc của chúng ta.")])

# ======================= LUYỆN TẬP =======================
add("bullets", chapter="Luyện tập", section="Luyện tập 课后练习", title="Bài tập 1: Chọn thành ngữ điền vào chỗ trống (1)", reveal=True, size=31,
    items=["## 当仁不让 · 对症下药 · 当之无愧 · 轰轰烈烈 · 无心插柳柳成荫 · 雨后春笋 · 立竿见影 · 浩浩荡荡",
           "(1) 当年一支建筑工程队___地开进这个山村，没想到过了短短几年，这里已旧貌变新颜。",
           "Đáp án: 浩浩荡荡",
           "(2) 科学史上有很多的重大研究突破都是___，比如青霉素的发现，就是因为弗莱明做完实验忘记洗盘子发现的。",
           "Đáp án: 无心插柳柳成荫",
           "(3) 既然你们这么信任我，那带领大家探索致富之路我就___了。",
           "Đáp án: 当仁不让",
           "(4) 经过不懈的努力，科学家们终于攻克了这个难题，他们是___的英雄。",
           "Đáp án: 当之无愧"],
    say=["Phần luyện tập 趁热打铁. Bài tập một: chọn thành ngữ điền vào chỗ trống. Có tám cụm: 当仁不让，对症下药，当之无愧，轰轰烈烈，无心插柳柳成荫，雨后春笋，立竿见影，浩浩荡荡.",
         F(1, "Câu một: 当年一支建筑工程队什么地开进这个山村，没想到过了短短几年，这里已旧貌变新颜。 Năm ấy một đội công trình xây dựng tiến vào ngôi làng miền núi này một cách thế nào; không ngờ chỉ mấy năm ngắn ngủi, nơi đây đã thay da đổi thịt. Các bạn tạm dừng và chọn nhé."),
         F(2, "Đáp án: 浩浩荡荡. Một đội công trình rầm rộ tiến vào làng."),
         F(3, "Câu hai: 科学史上有很多的重大研究突破都是什么，比如青霉素的发现，就是因为弗莱明做完实验忘记洗盘子发现的。 Nhiều đột phá lớn trong lịch sử khoa học đều là gì đó, ví dụ penicillin được phát hiện vì Fleming làm thí nghiệm xong quên rửa đĩa."),
         F(4, "Đáp án: 无心插柳柳成荫. Không cố ý mà lại có phát minh vĩ đại."),
         F(5, "Câu ba: 既然你们这么信任我，那带领大家探索致富之路我就什么了。 Các bạn đã tin tưởng tôi như vậy, thì việc dẫn dắt mọi người tìm đường làm giàu, tôi xin thế nào?"),
         F(6, "Đáp án: 当仁不让. Việc nên làm thì không chối từ."),
         F(7, "Câu bốn: 经过不懈的努力，科学家们终于攻克了这个难题，他们是什么的英雄。 Sau nỗ lực không ngừng, các nhà khoa học cuối cùng đã giải được bài toán khó này, họ là những anh hùng thế nào?"),
         F(8, "Đáp án: 当之无愧. 当之无愧的英雄, những anh hùng xứng đáng.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 1: Chọn thành ngữ điền vào chỗ trống (2)", reveal=True, size=32,
    items=["(5) 这个年纪的年轻人，没人甘于平淡，谁都想___地过一生。",
           "Đáp án: 轰轰烈烈",
           "(6) 遇到困难，只要找准症结，___，就一定可以解决问题，克服困难。",
           "Đáp án: 对症下药",
           "(7) 没多久的时间，这条街道上的各种快餐店便犹如___，一家接着一家地开张了。",
           "Đáp án: 雨后春笋",
           "(8) 只要掌握了正确的学习方法，便可收到___的效果。",
           "Đáp án: 立竿见影"],
    say=[F(0, "Câu năm: 这个年纪的年轻人，没人甘于平淡，谁都想什么地过一生。 Thanh niên ở tuổi này, không ai cam chịu bình lặng, ai cũng muốn sống một đời thế nào?"),
         F(1, "Đáp án: 轰轰烈烈. 轰轰烈烈地过一生, sống một đời sôi nổi, oanh liệt."),
         F(2, "Câu sáu: 遇到困难，只要找准症结，什么，就一定可以解决问题，克服困难。 Gặp khó khăn, chỉ cần tìm đúng căn nguyên, rồi làm gì, thì nhất định giải quyết được vấn đề."),
         F(3, "Đáp án: 对症下药. 找准症结，对症下药, đúng như câu trong bài khóa. Chữ 症 trong 对症下药 đọc thanh bốn."),
         F(4, "Câu bảy: 没多久的时间，这条街道上的各种快餐店便犹如什么，一家接着一家地开张了。 Chẳng bao lâu, các quán ăn nhanh trên con phố này giống như gì đó, lần lượt khai trương."),
         F(5, "Đáp án: 雨后春笋. 犹如雨后春笋, như nấm mọc sau mưa."),
         F(6, "Câu tám: 只要掌握了正确的学习方法，便可收到什么的效果。 Chỉ cần nắm được phương pháp học đúng đắn, là có thể thu được hiệu quả thế nào?"),
         F(7, "Đáp án: 立竿见影. 收到立竿见影的效果, thu được hiệu quả tức thì.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn đáp án đúng (1)", reveal=True, size=33,
    items=["(1) 九十年代中国的市场经济呈现出一派（  ）的生命力。 A.昌盛 B.旺盛 C.繁荣 D.兴旺",
           "Đáp án: B 旺盛 – 旺盛的生命力 sức sống dồi dào (cố định)",
           "(2) ……为了让他们拥有更精彩的人生，家长一定要多（  ）孩子的创造力。 A.激励 B.激化 C.激发 D.刺激",
           "Đáp án: C 激发 – 激发创造力 khơi dậy sức sáng tạo",
           "(3) 这几年，我们公司经营状况越来越好，（  ）调整了员工的工资。 A.大量 B.大力 C.大幅 D.大致",
           "Đáp án: C 大幅 – 大幅调整 điều chỉnh mạnh (biên độ lớn)"],
    say=["Bài tập hai: chọn đáp án đúng. Bài này luyện phân biệt các từ gần nghĩa.",
         F(0, "Câu một: 九十年代中国的市场经济呈现出一派什么的生命力。 Kinh tế thị trường Trung Quốc những năm chín mươi thể hiện một sức sống thế nào? Bốn lựa chọn: 昌盛，旺盛，繁荣，兴旺."),
         F(1, "Đáp án: B, 旺盛. 旺盛的生命力, sức sống dồi dào, là kết hợp cố định. 昌盛 hay đi với 国家, 繁荣昌盛; 繁荣 đi với 经济，市场; 兴旺 đi với 家业，事业."),
         F(2, "Câu hai: 优秀的创造力，会让孩子的未来有很多种可能，为了让他们拥有更精彩的人生，家长一定要多什么孩子的创造力。 Để con có cuộc đời đặc sắc hơn, cha mẹ nhất định phải làm gì với sức sáng tạo của con? Bốn lựa chọn: 激励，激化，激发，刺激."),
         F(3, "Đáp án: C, 激发. 激发创造力, khơi dậy sức sáng tạo. 激励 thường có tân ngữ chỉ người, như 激励孩子; 激化 là làm gay gắt thêm, như 激化矛盾; 刺激 thường đi với 消费，经济, hoặc mang nghĩa kích động."),
         F(4, "Câu ba: 这几年，我们公司经营状况越来越好，什么调整了员工的工资。 Mấy năm nay tình hình kinh doanh của công ty ngày càng tốt, nên đã điều chỉnh lương nhân viên thế nào? Bốn lựa chọn: 大量，大力，大幅，大致."),
         F(5, "Đáp án: C, 大幅. 大幅调整工资, điều chỉnh lương với biên độ lớn. 大量 đi với danh từ chỉ số lượng; 大力 là ra sức, như 大力支持; 大致 là đại khái.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 2: Chọn đáp án đúng (2)", reveal=True, size=33,
    items=["(4) 图书馆的门口立着一块“（  ）大声喧哗”的提示牌。 A.压抑 B.抑制 C.制止 D.禁止",
           "Đáp án: D 禁止 – 禁止大声喧哗 cấm làm ồn (biển báo)",
           "(5) 由于过度劳累，他的病情复发，（  ）恶化。 A.加大 B.加剧 C.加重 D.加强",
           "Đáp án: B 加剧 – 加剧恶化 xấu đi nhanh, trầm trọng thêm",
           "(6) 原子核裂变会（  ）出巨大的能量。 A.释放 B.解放 C.解除 D.发放",
           "Đáp án: A 释放 – 释放能量 giải phóng năng lượng"],
    say=[F(0, "Câu bốn: 图书馆的门口立着一块什么大声喧哗的提示牌。 Trước cửa thư viện dựng một tấm biển gì đó làm ồn. Bốn lựa chọn: 压抑，抑制，制止，禁止."),
         F(1, "Đáp án: D, 禁止. 禁止大声喧哗, cấm làm ồn, là lời biển báo quen thuộc. 制止 là ngăn chặn một hành vi đang xảy ra, như 制止打架; 抑制 là kìm hãm; 压抑 là kìm nén tình cảm."),
         F(2, "Câu năm: 由于过度劳累，他的病情复发，什么恶化。 Do làm việc quá sức, bệnh của anh ấy tái phát, xấu đi thế nào? Bốn lựa chọn: 加大，加剧，加重，加强."),
         F(3, "Đáp án: B, 加剧, từ mới của bài: 加剧恶化, trầm trọng thêm, xấu đi nhanh hơn. 加大 đi với 力度，难度; 加强 đi với 管理，锻炼; còn 加重 thường đứng một mình, như 病情加重, không đi với 恶化."),
         F(4, "Câu sáu: 原子核裂变会什么出巨大的能量。 Phản ứng phân hạch hạt nhân sẽ làm gì ra năng lượng khổng lồ? Bốn lựa chọn: 释放，解放，解除，发放."),
         F(5, "Đáp án: A, 释放. 释放能量, giải phóng năng lượng. 解放 đi với 思想，生产力, như 解放思想 trong bài; 解除 đi với 合同，警报; 发放 là phát, cấp, như 发放工资.")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 3: Dùng từ ngữ, mẫu câu cho sẵn trả lời câu hỏi", reveal=True, size=30,
    items=["(1) 改革开放之前为何农村经济困难？（归根到底）",
           "Đáp án gợi ý: 归根到底是由于不合理的计划经济体制造成的，计划经济的种种弊端加剧了农村人口的贫困程度。",
           "(2) 中国的市场经济改革有何成果？（意想不到的是……）",
           "Đáp án gợi ý: 改革原本聚焦于国有企业，但成效寥寥。意想不到的是，改革的成就最终在农村凸显出来，大量农民摆脱了贫困。",
           "(3) 家庭联产承包制度在农村带来了哪些连锁反应？（继……之后）",
           "Đáp án gợi ý: 它提高了农民收入和生产效率，释放出剩余劳动力，刺激了乡镇企业的发展。乡镇企业成为继家庭联产承包责任制之后，农村减贫的第二大推动力。",
           "(4) 农民的生产积极性是如何被激发的？（如此一来……，致力于……）",
           "Đáp án gợi ý: 改革开放后，政府找准体制的症结，对症下药。如此一来，农民自己成为减贫的最大推动力，致力于脱贫致富。"],
    say=["Bài tập ba: dùng từ ngữ và mẫu câu cho sẵn để trả lời câu hỏi về bài khóa. Đây là câu hỏi mở, thầy đưa ra đáp án gợi ý.",
         F(0, "Câu một: 改革开放之前为何农村经济困难？ Vì sao trước cải cách mở cửa kinh tế nông thôn khó khăn? 为何 là vì sao, văn viết. Dùng 归根到底."),
         F(1, "Gợi ý: 归根到底是由于不合理的计划经济体制造成的，计划经济的种种弊端加剧了农村人口的贫困程度。"),
         F(2, "Câu hai: 中国的市场经济改革有何成果？ Cải cách kinh tế thị trường của Trung Quốc có thành quả gì? Dùng 意想不到的是."),
         F(3, "Gợi ý: 改革原本聚焦于国有企业，但成效寥寥。意想不到的是，改革的成就最终在农村凸显出来，大量农民摆脱了贫困。"),
         F(4, "Câu ba: 家庭联产承包制度在农村带来了哪些连锁反应？ Chế độ khoán mang lại những phản ứng dây chuyền nào ở nông thôn? Dùng 继之后."),
         F(5, "Gợi ý: 它提高了农民收入和生产效率，释放出剩余劳动力，刺激了乡镇企业的发展。乡镇企业成为继家庭联产承包责任制之后，农村减贫的第二大推动力。"),
         F(6, "Câu bốn: 农民的生产积极性是如何被激发的？ Tính tích cực sản xuất của nông dân đã được khơi dậy thế nào? Dùng 如此一来 và 致力于."),
         F(7, "Gợi ý: 改革开放后，政府找准体制的症结，对症下药。如此一来，农民自己成为减贫的最大推动力，致力于脱贫致富。")])

add("bullets", section="Luyện tập 课后练习", title="Bài tập 4: Chọn từ điền vào đoạn văn", reveal=True, size=31,
    items=["## 天时地利人和 · 如此一来 · 辛勤 · 红利 · 空前 · 大幅 · 致富 · 束缚 · 事关",
           "全面实施乡村振兴战略，使乡村取得___发展，让___的老百姓切实享受改革开放的___，需要___。乡村振兴___全面建成小康社会宏伟目标。只要我们抓住……“天时”，用好……“地利”，培育……“人和”，就能打赢乡村振兴攻坚战，___，就能___提高农民的收入，使乡村逐渐走向___之路，挣脱贫困的___。",
           "Đáp án: 空前 · 辛勤 · 红利 · 天时地利人和 · 事关 · 如此一来 · 大幅 · 致富 · 束缚"],
    say=["Bài tập bốn: chọn từ điền vào đoạn văn về chiến lược chấn hưng nông thôn. Có chín từ: 天时地利人和，如此一来，辛勤，红利，空前，大幅，致富，束缚，事关.",
         F(1, "全面实施乡村振兴战略，使乡村取得什么发展，让什么的老百姓切实享受改革开放的什么，需要什么。乡村振兴什么全面建成小康社会宏伟目标。只要我们抓住中央全面铺开乡村振兴战略蓝图的天时，用好深厚乡土情怀、美丽乡村风貌的地利，培育三农人才、职业农民的人和，就能打赢乡村振兴攻坚战，什么，就能什么提高农民的收入，使乡村逐渐走向什么之路，挣脱贫困的什么。 Các bạn tạm dừng và điền thử nhé."),
         F(2, "Đáp án: 取得空前发展；辛勤的老百姓；改革开放的红利；需要天时地利人和；乡村振兴事关全面建成小康社会宏伟目标；如此一来；大幅提高农民的收入；走向致富之路；挣脱贫困的束缚。"),
         F(2, "Gợi ý: phía sau đoạn văn tách thiên thời, địa lợi, nhân hòa ra giải thích từng cái, nên chỗ trống trước đó phải là cả cụm 天时地利人和. 大幅 đứng trước động từ 提高; 挣脱束缚 là vùng thoát khỏi sự trói buộc. Đoạn văn dùng gần hết các từ trọng điểm của bài, các bạn hãy đọc to vài lần nhé.")])

# ======================= LIÊN HỆ =======================
add("bullets", chapter="Liên hệ: con đường thoát nghèo của Việt Nam", section="Thảo luận 讨论", title="Liên hệ Việt Nam: Khoán 10, Đổi mới và xóa đói giảm nghèo", size=33,
    items=["Thời bao cấp, hợp tác xã “làm chung, ăn chung” ≈ 计划经济 · 人民公社 · 大锅饭",
           "Khoán 100 (1981), Khoán 10 (1988): giao ruộng cho hộ nông dân ≈ 家庭联产承包责任制",
           "Đổi mới (1986) ≈ 改革开放 (1978) → từ thiếu lương thực thành nước xuất khẩu gạo hàng đầu",
           "Chương trình 135, Nghị quyết 30a, vay vốn ưu đãi, bảo hiểm y tế cho hộ nghèo ≈ 国家政策扶持",
           "Câu hỏi (对比研究): 越南和中国的扶贫道路有哪些相同点和不同点？"],
    say=["Trước khi ôn tập đơn vị, chúng ta cùng liên hệ với Việt Nam. Đây cũng là đề bài của phần nghiên cứu so sánh, 对比研究, trong ôn tập đơn vị: so sánh con đường xóa nghèo của nước bạn và Trung Quốc.",
         F(0, "Thời bao cấp ở Việt Nam, hợp tác xã nông nghiệp làm chung, chia chung, cũng giống 计划经济，人民公社 và 大锅饭 trong bài: làm nhiều làm ít đều như nhau, nên nông dân không hăng hái."),
         F(1, "Rồi Việt Nam có Khoán một trăm năm một nghìn chín trăm tám mươi mốt, và đặc biệt là Khoán mười năm một nghìn chín trăm tám mươi tám, giao ruộng đất cho hộ nông dân, rất giống 家庭联产承包责任制."),
         F(2, "Công cuộc Đổi mới năm một nghìn chín trăm tám mươi sáu tương tự 改革开放 năm một nghìn chín trăm bảy mươi tám. Chỉ vài năm sau Khoán mười, Việt Nam từ một nước thiếu lương thực đã trở thành một trong những nước xuất khẩu gạo hàng đầu thế giới. Đúng là 立竿见影!"),
         F(3, "Về chính sách hỗ trợ, Việt Nam có Chương trình một trăm ba mươi lăm cho các xã đặc biệt khó khăn, Nghị quyết ba mươi a cho các huyện nghèo, cùng chính sách cho hộ nghèo vay vốn ưu đãi và cấp bảo hiểm y tế, giống 国家政策扶持 trong bài."),
         F(4, "Câu hỏi cho các bạn: 越南和中国的扶贫道路有哪些相同点和不同点？ Câu mẫu: 越南和中国的扶贫道路在很多方面大同小异，都是从农村改革开始的。中国实行家庭联产承包责任制，而越南则推行了“十号决议”，把土地交给农户经营。 Con đường xóa nghèo của Việt Nam và Trung Quốc về nhiều mặt là giống nhau, đều bắt đầu từ cải cách nông thôn. Trung Quốc thực hiện khoán đến hộ, còn Việt Nam thì thực hiện Nghị quyết mười, giao đất cho hộ nông dân. Các bạn hãy tạm dừng và nói thêm điểm khác nhau nhé.")])

# ======================= ÔN TẬP ĐƠN VỊ =======================
add("bullets", chapter="Ôn tập đơn vị 7", section="Ôn tập đơn vị 单元练习", title="Ôn tập Đơn vị 7: 单元练习 “学以致用”", size=31,
    items=["一、从句段到篇章: dùng từ chỉ thời gian, trình tự để kể quá trình phát triển của sự việc",
           "二、明察暗访: lập phiếu điều tra – 二手货，你愿意买单吗？ · 免费变付费，你会买单吗？",
           "三、对簿公堂: “小法庭” của 闲鱼 – 17 cư dân mạng làm “quan tòa” xử tranh chấp đồ cũ",
           "四、众说纷纭: 男性 vs 女性消费 · 从“她经济”到“他经济” · 付费时代是退步吗？ · “戴穷帽”的怪相",
           "五、研究报告: ưu nhược điểm của mô hình trả phí · 聚焦“三农”   六、对比研究: xóa nghèo nước bạn và Trung Quốc",
           "七、针锋相对: 知识付费 · 扶贫与扶智 · 帮扶“懒汉”   八、畅所欲言: phim tài liệu《走进大凉山》   九、妙笔生花: 2 bài viết ≥ 800 chữ"],
    say=["Bây giờ chúng ta sang chương ôn tập Đơn vị bảy. Sách có một phần bài tập tổng hợp mang tên 学以致用, học để vận dụng, gồm chín phần, nối kết cả ba bài: kinh tế đồ cũ, thời đại miễn phí kết thúc, và xóa đói giảm nghèo.",
         F(0, "Phần một, 从句段到篇章, từ câu đoạn đến bài văn: học cách dùng từ chỉ thời gian và trình tự để kể quá trình phát triển của một sự việc. Lát nữa chúng ta sẽ làm phần này."),
         F(1, "Phần hai, 明察暗访, điều tra công khai và bí mật: lập phiếu hỏi ba đến năm người xung quanh xem họ có chấp nhận đồ cũ không, và họ có sẵn lòng trả phí cho dịch vụ internet không. Đây chính là hai đề bài tập về nhà của bài bảy chấm một và bảy chấm hai."),
         F(2, "Phần ba, 对簿公堂, ra tòa đối chất: tìm hiểu tòa án nhỏ của Xianyu, nơi mười bảy cư dân mạng được chọn ngẫu nhiên làm quan tòa, xử tranh chấp mua bán đồ cũ."),
         F(3, "Phần bốn, 众说纷纭, mỗi người một ý: vì sao trên các ứng dụng đồ cũ nam nhiều hơn nữ; từ nền kinh tế của phái nữ đến nền kinh tế của phái nam; internet bước vào thời trả phí có phải là thụt lùi không; và hiện tượng lạ: huyện nghèo không muốn bỏ mũ nghèo."),
         F(4, "Phần năm, 研究报告, báo cáo nghiên cứu: ưu nhược điểm của mô hình trả phí, và vấn đề tam nông. Phần sáu, 对比研究, nghiên cứu so sánh: so sánh con đường xóa nghèo của nước bạn và Trung Quốc, như chúng ta vừa làm."),
         F(5, "Phần bảy, 针锋相对, tranh biện đối đầu, với ba đề: trả phí cho tri thức là cái hố hay kho báu; giúp nghèo về vật chất hay giúp về trí tuệ quan trọng hơn; và có nên trợ giúp người lười. Phần tám, 畅所欲言, nói thỏa thích: xem phim tài liệu 走进大凉山 của đạo diễn Nhật Bản 竹内亮 rồi nêu cảm nghĩ. Phần chín, 妙笔生花: hai đề viết, mỗi bài ít nhất tám trăm chữ. Thầy chọn những phần tiêu biểu để chúng ta cùng làm.")])

add("bullets", section="Ôn tập đơn vị 单元练习", title="从句段到篇章: kể quá trình phát triển của sự việc", reveal=True, size=31,
    items=["Thời gian: 一年前 · 当时 · 此时 · 若干年前   Bắt đầu: 一开始 · 最初 · 起初 · 起先",
           "Trình tự: 以后 · 自此以后 · 此后 · 随后 · 后来 · 于是 · 接着 · 最后 · 终于 · 最终   Tức thì: 一……就…… · 不久 · 随即",
           "Đề: 1978年—1992年 计划经济体制向市场经济体制转变（最初……；之后……；不久……；……；最终……）",
           "Đáp án gợi ý: 最初，1978年十一届三中全会意识到计划经济的弊端；之后，1982年党的十二大提出了“计划经济为主，市场调节为辅”的原则；不久，1984年十二届三中全会第一次明确了社会主义经济是有计划的商品经济；1987年十三大进一步指出“国家调节市场，市场引导企业”的机制；最终，1992年十四大把建立社会主义市场经济体制作为我国经济体制改革的目标。"],
    say=["Phần một của ôn tập: 从句段到篇章. Khi dùng tiếng Trung kể lại quá trình xảy ra và phát triển của một sự việc, ta dùng các từ chỉ thời gian và trình tự để nối các câu.",
         F(0, "Từ chỉ thời gian: 一年前，当时，此时，若干年前. Từ chỉ sự bắt đầu: 一开始，最初，起初，起先."),
         F(1, "Từ chỉ trình tự trước sau: 以后，自此以后，此后，随后，后来，于是，接着，最后，终于，最终. Và từ chỉ việc sau xảy ra ngay sau việc trước: 一……就……，不久，随即."),
         F(2, "Bài tập của sách: tra cứu quá trình cải cách thể chế kinh tế của Trung Quốc và giới thiệu cho cả lớp. Sách cho sẵn khung giai đoạn một nghìn chín trăm bảy mươi tám đến một nghìn chín trăm chín mươi hai: chuyển từ kinh tế kế hoạch sang kinh tế thị trường, với các từ nối 最初，之后，不久，最终. Các bạn thử điền vào nhé."),
         F(3, "Đáp án gợi ý: 最初，一九七八年十一届三中全会意识到计划经济的弊端；之后，一九八二年党的十二大提出了计划经济为主，市场调节为辅的原则；不久，一九八四年十二届三中全会第一次明确了社会主义经济是有计划的商品经济；一九八七年十三大进一步指出国家调节市场，市场引导企业的机制；最终，一九九二年十四大把建立社会主义市场经济体制作为我国经济体制改革的目标。",
           cap="Đáp án gợi ý: 最初，1978 年十一届三中全会……；之后，1982 年十二大……；不久，1984 年十二届三中全会……；1987 年十三大……；最终，1992 年十四大把建立社会主义市场经济体制作为经济体制改革的目标。"),
         F(3, "Các bạn có thể dùng đúng khung này để kể về công cuộc Đổi mới của Việt Nam: 最初……意识到……；一九八六年……；此后……；最终…… Hãy thử viết một đoạn khoảng hai trăm chữ nhé.")])

add("bullets", section="Ôn tập đơn vị 单元练习", title="对簿公堂: 闲鱼“小法庭” – nếu bạn là quan tòa?", reveal=True, size=31,
    items=["Cách xử: hệ thống chọn ngẫu nhiên 17 người dùng làm “小法官” → hai bên nộp ảnh, chứng cứ → bên nào được 9 phiếu trước thì thắng, thường chưa đến 24 giờ",
           "Vụ 3: 鱿鱿 bán áo len mohair 70 tệ, ghi rõ “不退换”; người mua chê rụng lông, đòi trả hàng → “小法官” xử người mua thắng",
           "鱿鱿 không phục: “世界上所有的马海毛毛衣都会掉毛……我觉得闲鱼小法庭是不是应该在评审人群方面筛选再严格一点。”",
           "如果你是小法官，你会如何处理以上案例？请说明理由。",
           "Đáp án gợi ý: 我会支持鱿鱿。卖家已经注明“不退换”，而且马海毛掉毛是这种材料的正常特点，不属于质量问题。不过卖家最好在商品描述中提前说明，这样可以减少纠纷。"],
    say=["Phần ba của ôn tập: 对簿公堂, ra tòa đối chất. Trên ứng dụng Xianyu có một tòa án nhỏ trên mạng, mỗi ngày xử hàng nghìn vụ tranh chấp mua bán; người cầm cân nảy mực không phải thẩm phán, mà là mười bảy cư dân mạng bình thường.",
         F(0, "Cách xử như sau: khi một vụ tranh chấp được gửi lên, hệ thống chọn ngẫu nhiên mười bảy người dùng đủ điều kiện làm quan tòa nhỏ. Hai bên nộp ảnh, chứng cứ giao dịch; các quan tòa bỏ phiếu theo chứng cứ, bên nào được chín phiếu trước thì thắng, thường chưa đến hai mươi bốn giờ là có kết quả."),
         F(1, "Sách đưa ra ba vụ việc; thầy chọn vụ thứ ba. 鱿鱿, một cô gái hai mươi lăm tuổi mê truyện tranh, bán trên Xianyu một chiếc áo len mohair giá bảy mươi tệ, ghi rõ không đổi trả. Người mua nhận hàng thấy áo rụng lông nên đòi trả, 鱿鱿 từ chối. Hai bên ra tòa nhỏ, và 鱿鱿 không được các quan tòa ủng hộ."),
         F(2, "鱿鱿 không phục, cô nói với phóng viên: 世界上所有的马海毛毛衣都会掉毛，就算你去专柜买了件五百块钱的，依然会掉。我觉得闲鱼小法庭是不是应该在评审人群方面筛选再严格一点。 Mọi chiếc áo len mohair trên đời đều rụng lông, kể cả mua ở quầy chính hãng năm trăm tệ cũng vẫn rụng. Tôi nghĩ tòa án nhỏ của Xianyu có nên chọn người xét xử chặt chẽ hơn không."),
         F(3, "Câu hỏi: 如果你是小法官，你会如何处理以上案例？请说明理由。 Nếu bạn là quan tòa nhỏ, bạn sẽ xử vụ này thế nào? Hãy nêu lý do. Các bạn tạm dừng và suy nghĩ nhé."),
         F(4, "Đáp án gợi ý: 我会支持鱿鱿。卖家已经注明不退换，而且马海毛掉毛是这种材料的正常特点，不属于质量问题。不过卖家最好在商品描述中提前说明，这样可以减少纠纷。 Tôi sẽ ủng hộ 鱿鱿: người bán đã ghi rõ không đổi trả, mà rụng lông là đặc điểm bình thường của chất liệu mohair, không phải lỗi chất lượng. Có điều người bán nên nói rõ trước trong phần mô tả để giảm tranh chấp. Đây là câu hỏi mở, các bạn hoàn toàn có thể đứng về phía người mua, miễn là giải thích được. Vụ việc này cũng nhắc lại bài bảy chấm một: lòng tin là chìa khóa của giao dịch đồ cũ.")])

add("bullets", section="Ôn tập đơn vị 单元练习", title="众说纷纭 · 针锋相对: “戴穷帽”的怪相 và 扶贫还是扶智？", reveal=True, size=30,
    items=["## 讨论四: “戴穷帽”的怪相 – có huyện đã đủ chuẩn nhưng không muốn “摘帽”, vì 贫困县 được ưu tiên về tài chính, dự án, hạ tầng",
           "你如何看待以上现象？你认为应该如何杜绝上述怪相的发生？",
           "Đáp án gợi ý: 这是利益驱动在作怪。应该实行“摘帽不摘政策”，让脱贫县不必担心失去扶持；同时加强监督，对弄虚作假的干部严肃问责。",
           "## 辩论题: 扶贫与扶智哪个更重要？ “仓廪实而知礼节，衣食足而知荣辱” ↔ “授人以鱼不如授人以渔”",
           "Đáp án gợi ý: 两者缺一不可。扶贫能解燃眉之急，扶智才能拔掉穷根。扶贫先扶智，脱贫先立志；扶贫不扶懒，救急不救穷。"],
    say=["Phần tiếp theo của ôn tập: thảo luận và tranh biện, nối với bài bảy chấm ba.",
         F(0, "Đề thảo luận thứ tư: 戴穷帽的怪相, hiện tượng lạ đội mũ nghèo. Nhà nước đầu tư rất nhiều nhân lực, vật lực, tài lực để các huyện nghèo sớm thoát nghèo. Thế nhưng có huyện đã đạt chuẩn bỏ mũ mà vẫn chần chừ không muốn bỏ. Lý do là lợi ích: huyện nghèo được ưu tiên về chuyển giao ngân sách, vốn dự án, xây dựng hạ tầng, nên đội mũ nghèo là được nhiều lợi."),
         F(1, "Câu hỏi: 你如何看待以上现象？你认为应该如何杜绝上述怪相的发生？ Bạn nhìn nhận hiện tượng trên thế nào? Nên làm gì để chấm dứt hiện tượng lạ ấy? 杜绝 là ngăn chặn tận gốc."),
         F(2, "Đáp án gợi ý: 这是利益驱动在作怪。应该实行摘帽不摘政策，让脱贫县不必担心失去扶持；同时加强监督，对弄虚作假的干部严肃问责。 Đây là do lợi ích chi phối. Nên thực hiện bỏ mũ nhưng không bỏ chính sách, để huyện đã thoát nghèo không lo mất hỗ trợ; đồng thời tăng cường giám sát, nghiêm khắc truy cứu trách nhiệm cán bộ gian dối. Thực tế, Trung Quốc đã áp dụng nguyên tắc 摘帽不摘政策 như vậy."),
         F(3, "Đề tranh biện: 扶贫与扶智哪个更重要？ Giúp nghèo về vật chất hay giúp về trí tuệ quan trọng hơn? Một bên dẫn câu của sách Quản Tử: 仓廪实而知礼节，衣食足而知荣辱, kho lẫm đầy thì biết lễ tiết, cơm áo đủ thì biết vinh nhục. Bên kia dẫn câu: 授人以鱼不如授人以渔, cho cá không bằng dạy cách câu cá."),
         F(4, "Đáp án gợi ý: 两者缺一不可。扶贫能解燃眉之急，扶智才能拔掉穷根。扶贫先扶智，脱贫先立志；扶贫不扶懒，救急不救穷。 Hai thứ không thể thiếu một. Giúp vật chất giải quyết cái khó trước mắt, giúp trí tuệ mới nhổ được gốc nghèo. 燃眉之急 là lửa cháy đến lông mày, việc cấp bách. 扶贫不扶懒，救急不救穷 là giúp người nghèo chứ không giúp kẻ lười, cứu lúc nguy cấp chứ không nuôi cái nghèo mãi. Đây cũng là câu trả lời cho đề tranh biện thứ ba của sách: có nên giúp người lười thu nhập thấp không.")])

# ======================= TỔNG KẾT =======================
add("bullets", chapter="Tổng kết", section="Tổng kết", title="Tổng kết bài 7.3 và Đơn vị 7", size=31,
    items=["Từ vựng bài 7.3: 扶贫 · 载入 · 借鉴 · 归根到底 · 弊端 · 加剧 · 凸显 · 承包 · 蓬勃 · 抛弃 · 激励 · 事关 · 释放 · 崛起 · 人为 · 萧条 · 症结 · 压抑 · 激发 · 脱贫 · 致富 · 束缚",
           "Mẫu câu: 载入……史册 · 归根到底 · 意想不到的是 · 事关 · 继……之后 · 打破……的束缚",
           "Thành ngữ: 当之无愧 · 有心栽花花不开 · 无心插柳柳成荫 · 说一千道一万 · 雨后春笋 · 轰轰烈烈 · 至关重要 · 立竿见影 · 当仁不让 · 浩浩荡荡 · 天时地利人和 · 抄作业 · 日新月异",
           "## Đơn vị 7 · 经济篇: 7.1 物品的使用比占有更具价值 · 7.2 天下没有永远免费的午餐 · 7.3 脱贫致富靠制度改革和辛勤付出",
           "Bài tập về nhà (妙笔生花): 如何激发群众的主观能动性，通过勤劳的双手脱贫致富？ (≈ 500 chữ)"],
    say=["Chúng ta cùng tổng kết bài bảy chấm ba, và cũng là tổng kết Đơn vị bảy.",
         F(0, "Về từ vựng bài bảy chấm ba, các bạn cần đặc biệt nhớ: 扶贫，载入，借鉴，归根到底，弊端，加剧，凸显，承包，蓬勃，抛弃，激励，事关，释放，崛起，人为，萧条，症结，压抑，激发，脱贫，致富，束缚. Nhớ cách đọc 载入，人为，症结 và những từ dễ nhầm như 弊端，蓬勃."),
         F(1, "Về mẫu câu: 载入史册 là ghi vào sử sách; 归根到底 là suy cho cùng; 意想不到的是 là điều không ngờ là; 事关 là liên quan đến việc hệ trọng; 继之后 là tiếp sau; và 打破的束缚 là phá bỏ sự trói buộc."),
         F(2, "Về thành ngữ, mười ba cụm, nhiều nhất trong đơn vị. Hãy ôn kỹ những cặp hay đi cùng nhau như 有心栽花花不开 và 无心插柳柳成荫, 找准症结 và 对症下药, cùng 天时地利人和 mà tiếng Việt dùng y hệt."),
         F(3, "Nhìn lại cả Đơn vị bảy, chủ đề Kinh tế: bài bảy chấm một nói rằng sử dụng đồ vật có giá trị hơn sở hữu nó; bài bảy chấm hai nói rằng trên đời không có bữa trưa nào miễn phí mãi; và bài bảy chấm ba nói rằng thoát nghèo làm giàu phải dựa vào cải cách chế độ và sự lao động cần cù của chính người dân. Cả ba bài đều nhắc chúng ta nhìn kinh tế một cách tỉnh táo, tôn trọng quy luật."),
         F(4, "Bài tập về nhà, theo phần 妙笔生花 của ôn tập đơn vị: hãy tự đặt đầu đề, bàn về việc làm thế nào khơi dậy tính năng động chủ quan của quần chúng, để họ thoát nghèo làm giàu bằng đôi tay cần cù. Sách yêu cầu ít nhất tám trăm chữ; các bạn có thể bắt đầu với khoảng năm trăm chữ, dùng ít nhất năm thành ngữ và ba mẫu câu của đơn vị. Nếu có thời gian, hãy xem phim 大江大河 và viết về nhân vật 杨巡 nhé."),
         {"t": "Cảm ơn các bạn đã theo dõi bài giảng. Chúc mừng các bạn đã hoàn thành Đơn vị bảy! Ở bài sau, chúng ta bước sang Đơn vị tám, 法律篇, chủ đề Pháp luật, với bài tám chấm một: 大头条对簿小油条, Đại Đầu Điều ra tòa với Tiểu Du Điều. Đó là câu chuyện ứng dụng tin tức Kim Nhật Đầu Điều kiện một tiệm bán quẩy tên Kim Nhật Du Điều vì nhái thương hiệu. Hẹn gặp lại các bạn. Chúc các bạn học tốt!",
          "cap": "Cảm ơn các bạn đã theo dõi bài giảng. Chúc mừng các bạn đã hoàn thành Đơn vị 7! Bài sau, Đơn vị 8 · 法律篇, bài 8.1: “大头条”对簿“小油条”, Đại Đầu Điều ra tòa với Tiểu Du Điều. Hẹn gặp lại các bạn. Chúc các bạn học tốt!"}])

lesson = {
    "title": "顶石中文 – Bài 7.3: 中国扶贫的道路选择 (Con đường xóa đói giảm nghèo của Trung Quốc)",
    "tag": TAG,
    "vi_voice": "Linh", "zh_voice": "Tingting", "vi_rate": 175, "zh_rate": 145,
    # sửa âm đọc của giọng máy cho các chữ đa âm (thay bằng chữ cùng âm, cùng thanh)
    "tts_replace": {"载入": "宰入",              # zǎirù
                    "重工业": "众工业",          # zhònggōngyè
                    "人为": "人维",              # rénwéi
                    "剪刀差": "剪刀叉",          # jiǎndāochā
                    "症结": "征结",              # zhēngjié
                    "高涨": "高掌",              # gāozhǎng
                    "切身": "窃身",              # qièshēn
                    "给予": "挤予",              # jǐyǔ
                    "数亿": "树亿",              # shùyì
                    "视为": "视维",              # shìwéi
                    "称为": "称维",              # chēngwéi
                    "可以为很多": "可以维很多",  # wéi … suǒ
                    "朝气": "招气",              # zhāoqì
                    "斗志": "豆志",              # dòuzhì
                    "冠军": "贯军",              # guànjūn
                    "夺冠": "夺贯",              # duóguàn
                    "干一番": "赣一番",          # gàn
                    "处理": "楚理",              # chǔlǐ
                    "增长": "增涨",              # zēngzhǎng
                    "新冠": "新官",              # xīnguān
                    "当之无愧": "铛之无愧",      # dāng
                    "当仁不让": "铛仁不让"},     # dāng
    "slides": slides,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds73.json")
json.dump(lesson, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{out}: {len(slides)} slide, {sum(len(s['say']) for s in slides)} câu giảng")
