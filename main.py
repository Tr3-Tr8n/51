import streamlit as st

st.title('Điền thông tin để đăng ký tài khoản')
my_bar = st.progress(0)

# Danh sách các trường cần nhập
form_fields = [
    'Tài khoản:',
    'Mật khẩu:',
    'Nhập lại mật khẩu:',
    'Tên người dùng:',
    'Email:'
]

answers = []
total_fields = len(form_fields)

# Vòng lặp để hiển thị từng trường nhập
for field in form_fields:
    if 'Mật khẩu' in field:
        response = st.text_input(field, type='password')
    else:
        response = st.text_input(field)
    if response != '':
        answers.append(response)

# Nút xác nhận
if st.button('Xác nhận'):
    if len(answers) == total_fields:
        if answers[1] != answers[2]:  # Kiểm tra mật khẩu và nhập lại mật khẩu
            my_bar.progress(int((len(answers) / total_fields) * 100))
            st.error("Mật khẩu không khớp!")
        else:
            my_bar.progress(100)
            st.success('Bạn đã hoàn thành đầy đủ thông tin!')
            st.balloons()
            for i in range(total_fields):
                if 'Mật khẩu' not in form_fields[i]:
                    st.write(form_fields[i], answers[i])
    else:
        my_bar.progress(int((len(answers) / total_fields) * 100))
        st.warning("Vui lòng điền đầy đủ thông tin!")
