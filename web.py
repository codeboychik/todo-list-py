import streamlit as st
import modules


def add_task():
    modules.add_task(st.session_state['new_task'])
    st.write(st.session_state)


def remove_task():
    return None
    # st.write(st.session_state)


st.title('My todo app')
st.text(body=f'Last update: {modules.get_human_readable_time(modules.get_dictionary()["last_update"])}')

for task in modules.get_task_list():
    st.checkbox(label=task, value=False, key=id(task), on_change=remove_task())
    print(id(task))


st.text_input(placeholder='Enter a task: ', key='new_task', on_change=add_task, label='')
