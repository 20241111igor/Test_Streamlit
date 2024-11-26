import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Заголовок приложения
st.title('Мой первый дашборд')

# Загрузка данных
data = {
    'Фрукты': ['Яблоко', 'Банан', 'Апельсин'],
    'Количество': [10, 20, 30]
}
df = pd.DataFrame(data)

# Отображение таблицы
st.write(df)

# Построение графика
fig, ax = plt.subplots()
ax.bar(df['Фрукты'], df['Количество'])
plt.xlabel('Фрукты')
plt.ylabel('Количество')
plt.title('График количества фруктов')
st.pyplot(fig)

# Интерактивный элемент
fruit = st.selectbox('Выберите фрукт:', df['Фрукты'])
st.write(f'Вы выбрали {fruit}')
