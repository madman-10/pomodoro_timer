import streamlit as st
import time

base_template = '''<p style="text-align: center; font-size: 18px; font-style:sans-serif; color: white;">
The Pomodoro Timer is a method to increase productivity. The goal is to focus on task while the timer is running and take a short break between each session 3 times, followed by a long break, after completion of 4 session.
</p>'''
st.title(":orange[Pomodoro Timer]", text_alignment='center')
st.markdown(base_template, unsafe_allow_html=True)
st.divider()

WORK_TIME = 25 * 60
# WORK_TIME = 5  # Testing in small duration
POMODORO_COUNT = 0

if "is_running" not in st.session_state.keys():
    st.session_state["is_running"] = False
if "work" not in st.session_state.keys():
    st.session_state["work"] = WORK_TIME
if "button_disabled" not in st.session_state.keys():
    st.session_state["button_disabled"] = False
if "pomodoro_count" not in st.session_state.keys():
    st.session_state["pomodoro_count"] = POMODORO_COUNT
if "pomodoro_complete" not in st.session_state.keys():
    st.session_state["pomodoro_complete"] = False


# Start the timer here
def start_time():
    st.session_state["button_disabled"] = True
    st.session_state["is_running"] = True

# Function to pause the pomodoro timer (after start, during work or break time)
def pause_time():
    st.session_state["is_running"] = False
    st.session_state["button_disabled"] = False
    st.session_state["pomodoro_complete"] = False

# Function to reset the states (all states set to the original)
def reset_time():
    st.session_state["is_running"] = False
    st.session_state.work = WORK_TIME
    st.session_state["pomodoro_complete"] = False
    st.session_state["button_disabled"] = False

# Function to display the timer and counter
def display():
    minutes, seconds = divmod(st.session_state.work, 60)
    minutes = str(minutes).zfill(2)
    seconds = str(seconds).zfill(2)
    p_count = st.session_state["pomodoro_count"]
    timer_template = '''<p style="text-align: center; font-size: 55px; font-weight: bold; color: violet;">{minutes}:{seconds}</p>'''
    counter_template = '''<p style="text-align: center; font-family: serif; font-size: 42px; font-weight: light; color: yellow;">You've Completed {p_count} Pomodoros</p>'''
    with placeholder.container():
        st.markdown(timer_template.format(minutes=minutes, seconds=seconds), unsafe_allow_html=True)
        st.markdown(counter_template.format(p_count=p_count), unsafe_allow_html=True)

# Function called upon completion of each pomodoro
def success_message():
    if st.session_state.pomodoro_count % 4 == 0:
        st.success(''':material/star_shine: Congratulations, you have completed a complete Pomodoro Work Session! :material/star_shine:
                \n Take a long break now 😁
                \n Press "Reset" button to move on to the next session.''')
        st.snow()
    else:
        st.success(''':material/star_shine: Congratulations, you have completed a complete Pomodoro Work Session! :material/star_shine:
                \n Have a short break ⏱️
                \n Press "Reset" button to move on to the next session.''')
        st.snow()


placeholder = st.empty()

st.divider()

# Button column for "Start", "Pause" and "Reset" buttons
col1, col2, col3 = st.columns(3, gap='medium')
col1.button("Start Timer", on_click=start_time, use_container_width=True, type='primary', disabled=st.session_state.button_disabled)
col2.button("Pause Timer", on_click=pause_time, use_container_width=True, type='secondary')
col3.button("Reset Timer", on_click=reset_time, use_container_width=True, type='secondary')

# Logic implementation for the countdown and display
if st.session_state.is_running:
    display()
    milliseconds = 0
    while st.session_state.work != 0:
        time.sleep(0.1)
        milliseconds += 1
        if milliseconds % 10 == 0:
            st.session_state.work -= 1
        display()
    if st.session_state.work == 0:
        st.session_state.pomodoro_complete = True
        st.session_state.work = WORK_TIME
        st.session_state["pomodoro_count"] += 1
        display()
    if st.session_state.pomodoro_complete:
        success_message()
else:
    display()
