""" เขียน function ชื่อ analyze_scores ที่มีคุณสมบัติดังนี้:

รับ list ของคะแนน (ตัวเลข)
return dictionary ที่มี:

total: ผลรวมของคะแนนทั้งหมด
average: คะแนนเฉลี่ย (ปัดเศษ 1 ตำแหน่งหลังจุดทศนิยม)
highest: คะแนนสูงสุด
lowest: คะแนนต่ำสุด
passed: จำนวนคะแนนที่ >= 70 """

def analyze_scores(scores):
    total = sum(scores)
    count = len(scores)
    average = total / count
    lowest = min(scores)
    highest = max(scores)
    passed = 0

    for score in scores:
        if score >=70:
            passed+=1
    
    return {
        'sum': total,
        'count': count,
        'average': round(average, 2),
        'lowest': lowest,
        'highest': highest,
        'passed': passed
    }