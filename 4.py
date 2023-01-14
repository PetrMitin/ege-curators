for i in range(1, 10000):
    st = '0' + '1'*i + '2'*i + '0'
    while st.find('00') < 0:
        st = st.replace('011', '20', 1)
        st = st.replace('022', '10', 1)
        st = st.replace('01', '220', 1)
        st = st.replace('02', '110', 1)

    if st.count('1') == 40 and st.count('2') > 50:
        print(i)
        break
