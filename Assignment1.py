


number = []
while True:
    x = int(input("กรอกตัวเลข: "))
    if x < 0:
        break
    number.append(x)

print(f"ผล = {number}")
number.sort()
print(f"หลัง = {number}")
number.reverse()
print(f"หลัง2 = {number}")

print("จบโปรแกรม")

