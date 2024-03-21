import streamlit as st
import utils as utl
from views import urlscanner, home



st.set_page_config(layout="wide")
utl.inject_custom_css()
utl.navbar_component()


def navigation():
    route = utl.get_current_route()
    if route == "home":
        home.load_view()
    elif route == "urlscanner":
        urlscanner.load_view()
    elif route == None:
        home.load_view()
        
navigation()