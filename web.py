import streamlit as st
import modules


def add_task():
    if len(st.session_state['new_task']) > 0:
        modules.add_task(st.session_state['new_task'])
    st.session_state['new_task'] = ''


st.title('My todo app')
st.text(body=f'Last update: {modules.get_human_readable_time(modules.get_dictionary()["last_update"])}')

for task in modules.get_task_list():
    ch = st.checkbox(label=task, key=task)
    if ch:
        modules.remove_task(task)
        del st.session_state[task]
        st.experimental_rerun()


st.text_input(placeholder='Enter a task: ', key='new_task', on_change=add_task, label='')
