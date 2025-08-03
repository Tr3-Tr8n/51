import streamlit as st
st.title('Dien tin thong tin gioi thieu ban than em')
my_bar = st.progress(0)
quiz =  ['Ho va ten:', 'Ngay thang nam sinh:', 'so thich:']
answers = []
len_quiz = len(quiz)
for i in range(len_quiz):
  answer = st.text_input(quiz[i], '')
  if answer != '':
    answers.append(answer)
if st.button('Confirm'):
  if len(answers) == len_quiz:
    my_bar.progress(100)
    st.write('Ban da hoan thanh day du thong tin!')
    st.ballons()
  else:
    my_bar.progress(len(answers)/len_quiz)
  for i in range(len(answers)):
    st.write(quiz[i], answers[i])
