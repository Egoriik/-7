import random

group1 = ["Иванов", "Петров", "Кузнецов", "Смирнов", "Попов",
          "Васильев", "Михайлов", "Новиков", "Сидоров", "Федоров"]
group2 = ["Иванов", "Волков", "Зайцев", "Морозов", "Соловьев",
          "Орлов", "Козлов", "Никитин", "Егоров", "Алексеев"]

team1 = random.sample(group1, 5)
team2 = random.sample(group2, 5)

team = tuple(team1 + team2)

print(f"Группа 1: {group1[:5]} \n          {group1[5:]} \n"
      f"Группа 2: {group2[:5]} \n          {group2[5:]} \n"
      f"Спортивная команда: {team[:5]} \n {" "*18} {team[5:]}")
print("-" * 60)
print(f"Длина кортежа: {len(team)}")
print("-" * 60)
print(f"Сортировка: {sorted(team)[:5]} \n {" " * 10} {sorted(team)[5:]}")
print("-" * 60)

cnt = 0

for _ in team:
    if _ == "Иванов":
        cnt += 1

if cnt >= 1:
    print(f"Студент Иванов встречается {cnt} раз(а) в команде ")
else:
    print("Иванов не входит в команду.")
