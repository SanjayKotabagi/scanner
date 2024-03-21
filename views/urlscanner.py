import streamlit as st
from logic import urlscan

def load_view():
    st.header("URL Scanner")
    num_urls = st.number_input("Enter the number of URLs", min_value=1, step=1)
    
    urls = []
    for i in range(num_urls):
        urls.append(st.text_input(f"Enter URL {i+1}"))
    
    if st.button("Scan URLs"):
        st.write("Wait While Fetching Result")
        res = urlscan.get_reports(urls)
        for r in res:
            display_info(r)
            st.write("✔-------------------------------------✔")

def display_info(data):
    print(data)
    for d in data:
        if d[0] == 'Screenshot':
            st.write("Screenshot")
            st.image(d[1], width=500)
            st.write("SS URL : ", d[1])
            continue
        # elif d == 'Scan prevented ...':
        #     st.write("Scan Prevented in URL Scan")
        #     continue
        st.write(d[0], " : " ,d[1])