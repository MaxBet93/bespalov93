import random
list_length = random.randint(3, 10)
source_list = [random.randint(1, 100) for _ in range(list_length)]
print(f"Початковий список (довжина {list_length}): {source_list}")

final_list = [source_list[0], source_list[2], source_list[-2]]

print(f"Фінальний список: {final_list}")