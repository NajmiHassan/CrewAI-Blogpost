import streamlit as st
from crew import crew
import os

# Streamlit user interface
st.title("Crew AI System for Tech Blogging")

topic = st.text_input("Enter the topic you want to explore:", "AI in healthcare")

if st.button("Start Research and Writing"):
    result = crew.kickoff(inputs={'topic': topic})
    st.write("Task execution completed. Here are the results:")
    st.write(result)
    
    if os.path.exists('new-blog-post.md'):
        with open('new-blog-post.md', 'r') as file:
            blog_post = file.read()
        st.markdown(blog_post)
