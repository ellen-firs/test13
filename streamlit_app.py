import streamlit as st

# Заголовок
st.title("Прототип интерфейса AgroHunters")

# Блок регистрации
st.header("Регистрация")
with st.form("register_form"):
    name = st.text_input("Имя пользователя")
    email = st.text_input("E-mail")
    password = st.text_input("Пароль", type="password")
    submitted = st.form_submit_button("Зарегистрироваться")
    if submitted:
        st.success(f"Пользователь {name} успешно зарегистрирован!")

# Блок поиска
st.header("Поиск сотрудников/вакансий")
role = st.selectbox("Выберите роль", ["Агроном", "Механик", "Прораб"])
location = st.text_input("Город")
st.button("Искать")

# Список результатов
st.subheader("Результаты поиска")
st.write("1. Иван Иванов - Агроном, Москва")
st.write("2. Ольга Смирнова - Механик, Краснодар")
