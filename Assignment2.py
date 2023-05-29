

number = []
while True:
    x = int(input("กรอกตัวเลข: "))
    if x < 0:
        break
    number.append(x)

print(number)
print(f"ค่าที่น้อยที่สุดคือ : {min(number)}")
print(f"ค่าที่มากที่สุดคือ : {max(number)}")
print(f"ผลรวม : {sum(number)}")

print("จบโปรแกรม")

