import matplotlib.pyplot as plt

# Данные для Customer Journey Map
steps = ["Регистрация", "Настройка профиля", "Поиск сотрудников", "Просмотр деталей", "Создание заявки", "Завершение найма"]
durations = [3, 5, 8, 4, 3, 2]  # Длительность в минутах

# Создание диаграммы
plt.figure(figsize=(10, 6))
plt.plot(steps, durations, marker='o', color='blue', label='Продолжительность (мин)')
plt.title("Customer Journey Map")
plt.xlabel("Этапы пользовательского пути")
plt.ylabel("Продолжительность (минуты)")
plt.grid(True)
plt.legend()
plt.show()
