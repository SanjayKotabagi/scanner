import streamlit as st
# from views import log

def load_view():
    # if lrobj.login_status != True:
    #     log.load_view(lrobj)
    st.title("URL Scanner")
    st.write("URL scanner app! Please select the number of URLs you want to scan.")
    st.write("Feel Free to contrubute in GitHub")
    st.write("---")
    st.write("Find me on social media:")
    st.write('<div class="cfooter">'
        #'<a href="https://twitter.com/SanjayKotabagi1"><img src="https://img.shields.io/twitter/follow/SanjayKotabagi1?style=social"></a>'
        #'&nbsp;&nbsp;&nbsp;'  # Inserting spaces between icons
        '<a href="https://www.linkedin.com/in/sanjaykotabagi/"><img src="https://img.shields.io/badge/LinkedIn-Connect-blue"></a>'
        '&nbsp;&nbsp;&nbsp;'  # Inserting spaces between icons
        '<a href="https://github.com/SanjayKotabagi"><img src="https://img.shields.io/github/followers/SanjayKotabagi?label=Follow&style=social"></a>''</div>',
        unsafe_allow_html=True
    )
