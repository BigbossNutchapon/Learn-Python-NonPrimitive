#การค้นหาและนับจำนวนตัวอักษรในสมาชิก

message = ["aa","aab","cba","bba","aba","cca","aab","aaa"]
#อยากจะนับว่าแต่ละช่องมี a กี่ตัว
result = []

for item in message:
    result.append(item.count("a"))
print(result)
