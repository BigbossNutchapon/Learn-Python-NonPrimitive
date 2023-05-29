#หาเลขคู่ คี่

number = []
odd = []
even = []
while True:
    x = int(input("ป้อนตัวเลขของคุณ: "))
    if x < 0:
        break
    if x%2 == 0:
        even.append(x)
    else:
        odd.append(x)
    number.append(x)
print(f"ตัวเลขทั้งหมด : {number}")
print(f"เลขคู่ : {even}")
print(f"เลขคี่ : {odd}")