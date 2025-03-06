list1 = [{"name": "john", "class": 12}, {"name": "anil", "class": 10}]
formatted_string = ", ".join([f"name: {item['name']}, class: {item['class']}" for item in list1])

print(formatted_string)
