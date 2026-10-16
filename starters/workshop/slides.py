# Workshop starter (Thinc. look). One concept, broken into beats. Read METHOD.md first.
# Same fields as the Thinc. template, plus:
#   min     minutes on this slide (feeds out/runsheet.md, the running clock)
#   say     one line for the presenter: what to say / ask / what the room does
#   reveal  True with builds=N: parts appear one by one (later groups hidden) instead of dimming
# Example content = Seven's E+R=O module (WS101). Replace with the new concept.
BRAND = "Thinc."
TRACKER = 0

S = [
 dict(n="01", kind="divider", title="E + R = O", sub="ทำไมผลลัพธ์ไม่เป็นอย่างที่หวัง", min=1,
      say="เปิด module: วันนี้จะตอบ 2 คำถาม เราจัดการกับเหตุการณ์ยังไง และทางเลือกอื่นมีอะไรบ้าง"),
 dict(n="02", title="มาช่วยน้อง Miss กันเถอะ", sub="Ice-breaking", builds=3, reveal=True, min=4,
      say="เล่าทีละ beat: น้อง Miss เจอลูกค้า → ลูกค้าหนาว → ให้ห้องช่วยคิด แล้วค่อยโชว์ไอเดีย",
      brief="Story beat. Left: simple character (pink). Right: speech card 1, speech card 2, then 3 sticky-note ideas (reveal 1-2-3)."),
 dict(n="03", title="Key Question", min=1, say="ถามแล้วเงียบ ให้คิดในใจ 30 วิ ยังไม่ต้องตอบ",
      brief="One big question in a card, centred. Chip: think 30 s."),
 dict(n="04", title="เรื่องของพี่เอง", sub="ฝึกงานที่ใหม่ กับงานที่ไม่เคยทำ", builds=3, reveal=True, min=6,
      say="เล่าเรื่องจริงของตัวเอง: สถานการณ์ → ความคิดโทษคนอื่น → ทางเลือกที่เจอ",
      brief="Reveal: situation card left; 3 red blame thoughts; 3 green options."),
 dict(n="05", title="At Effect กับ At Cause", min=3, say="ตั้งชื่อให้สิ่งที่เพิ่งเห็นในเรื่อง",
      brief="Two lanes: At Effect red crossed out, At Cause green check. Bulb line under."),
 dict(n="06", title="Workshop", time="10 นาที", out="ทุกคนมี 5 ทางเลือกที่เราคุมได้", min=10,
      say="อธิบายทีละข้อ แล้วกดเวลา 10:00",
      brief="Activity: 3 numbered steps with minutes + who; big timer disc right."),
 dict(n="07", title="Half-way check point", min=1, say="สรุปสิ่งที่รู้แล้ว 2 ข้อ แล้วบอกว่าต่อไปเรียนอะไร",
      brief="Check point: 2 green-check lines, next-up chip dashed."),
 dict(n="08", title="The success formula", sub="เหตุการณ์ + การตอบสนอง = ผลลัพธ์", builds=2, min=3,
      say="หน้าแรกชี้ E กับ O, หน้าสองชี้ R: นี่คือส่วนที่เราคุมได้",
      brief="Formula E + R = O as 3 big discs. Build 1 focus E and O, build 2 focus R."),
 dict(n="09", title="Let's Try!", sub="Response ใหม่ที่เป็นไปได้มีอะไรบ้าง?", builds=2, reveal=True, min=4,
      say="ให้ห้องตอบก่อน แล้วค่อยเฉลย",
      brief="Formula slots: E card, O card, R column with 3 ??? chips; build 2 = answers cover the ???."),
 dict(n="10", title="Key Takeaway", min=2, say="3 มุม: ต่อตัวเอง ต่อโค้ชชี ต่อการโค้ช",
      brief="3 lens cards with icon discs and one line each."),
 dict(n="11", title="Check-out", min=5, say="ทีละคน คนละ 30 วิ",
      brief="One big check-out question; chips: one by one, 30 s each."),
]
