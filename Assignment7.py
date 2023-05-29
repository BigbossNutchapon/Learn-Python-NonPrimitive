
fruit = ["มะม่วงดอง","แตงโมปั่น","ฝรั่งแช่บ๋วย"]
price = [50,30,15]

for x,y in zip(fruit,price[::-1]):
    print(f"สินค้า = {x} ราคา = {y}")