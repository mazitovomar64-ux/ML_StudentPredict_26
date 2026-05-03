import streamlit as st
import requests

api_url = 'http://127.0.0.1:8000/predict'

st.title('Student Predict')

gen_student = st.selectbox('Пол', ['male', 'female'])
race_student = st.selectbox('Этническая раса', ['group A', 'group B', 'group C', 'group D', 'group E'])
parent_student = st.selectbox('Обучение Родителей', ["associate's degree", "bachelor's degree", 'high school', "master's degree", 'some college', 'some high school'])
lunch_student = st.selectbox('Обед', ['standard', 'free/reduced'])
test_student = st.selectbox('Допольнительные занятия', ['completed', 'none'])
math_student = st.number_input('баллы по матиматике', min_value=0)
read_student = st.number_input('баллы по чтению', min_value=0)


student_data = {
    'gender': gen_student,
    'race_ethnicity': race_student,
    'parent_education': parent_student,
    'lunch': lunch_student,
    'test_preparation': test_student,
    'math_score': math_student,
    'reading_score': read_student
}

if st.button('Предсказать'):
    try:
        answer = requests.post(api_url, json=student_data, timeout=10)
        if answer.status_code == 200:
            result = answer.json()
            st.success(f'Result {result.get('predict')}')
        else:
            st.error(f'Ошибка: {answer.status_code}')

    except requests.exceptions.RequestException:
        st.error(f'Не удалось соединиться с API')


