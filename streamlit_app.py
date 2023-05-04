
import streamlit as st

# set the app's title
st.title("Text Elements")
 
# header
st.header("Header in Streamlit")
 
# subheader
st.subheader("Subheader in Streamlit")
 
# markdown
# display text in bold formatting
st.markdown("**AskPython** is an awesome website!")
# display text in italic formatting
st.markdown("Visit _askpython.com_ to learn from various Python tutorials.")
 
# code block
code = '''
def add(a, b):
    print("a+b = ", a+b)
'''
st.code(code, language='python')
 
# latex
st.latex('''
(a+b)^2 = a^2 + b^2 + 2*a*b
''')
