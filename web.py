import streamlit as st
import functions

todos = functions.get_todos()       # importing the todos list from todos.txt
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    print(todo)
    todos.append(todo)
    functions.write_todos(todos)



st.title("MY To-Do App")        # for heading/title of the web app
st.subheader("Designed by - Ashutosh Roy.")     # for sub_heading
st.write("This app is to increase your productivity.") # For writting simple text in the app


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)        # to create a check boxes
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=" ", placeholder="Add a new Todo...",
              on_change=add_todo, key= 'new_todo')
