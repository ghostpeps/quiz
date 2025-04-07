import streamlit as st

import pandas as pd

import numpy as np

import random

from settings import grade, user

def login_screen():
    st.title("Go to Settings to Login")
    settings = st.button("Go to Settings", icon=":material/settings:")
    if settings:
        st.switch_page("settings.py")
if user.is_logged_in:
    st.title("ELA")
    hours = 0
    mins = 0
    secs = 0
    st.write(f"You have {hours} hours, {mins} minutes, and {secs} seconds until you can take the test again.")
    col1, col2 = st.columns(2)
    qa = dict()
    num = 0
    qlist = []
    score = dict()
    score = 0
    days = 0
    if grade == 1:
        question_bank = [
                    [
                "",
                "",
                "",
                "",
                ""
                ],
                    ["""
                """,
                "",
                "",
                "",
                ""
                ]
        ]
        #answer_bank = {"": , "": }
    elif grade == 2:
        question_bank = [
                    [
                "He **acquiesced** in his decision. What is the definition of the bolded word?",
                "accepted something reluctantly but without protesting",
                "thought about something",
                "to be happy about a choice",
                "None of the above"
                ],
                    ["""
                "The Last Letter"
    
                    Eliza had spent the last twenty years avoiding the cedar chest in the corner of her attic.
                Within it lay letters—dozens of them—from her younger sister, Clara.
                They had parted ways long ago after an argument so fierce it turned love into silence.
                Eliza had never opened Clara's letters, convinced that the words within were filled with anger and blame.
                But now, as years stretched into decades and regret tightened, she found herself drawn to the chest.
                With trembling hands, she lifted the lid and unfolded a yellowed envelope.
                "Eliza," the letter began, "I miss you. I'm sorry for everything."
                The words tumbled like a flood, and by the last page, Eliza sat sobbing on the attic floor, overwhelmed by a love that had endured even when she thought it had been lost.
                In that moment, forgiveness felt like sunlight breaking through an old, stubborn storm.
                She picked up her pen and began to write a letter of her own—one she should have written long ago.
                    
                What is the theme?
                """,
                "hope",
                "forgiveness",
                "betrayal",
                "good vs. evil"
                ]
        ]
        answer_bank = {"0": 1, "1": 2}
    elif grade == 3:
        question_bank = [
                    [
                "",
                "",
                "",
                "",
                ""
                ],
                    ["""
                """,
                "",
                "",
                "",
                ""
                ]
        ]
        #answer_bank = {"": , "": }
    elif grade == 4:
        question_bank = [
                    [
                "",
                "",
                "",
                "",
                ""
                ],
                    ["""
                """,
                "",
                "",
                "",
                ""
                ]
        ]
        #answer_bank = {"": , "": }
    elif grade == 5:
        question_bank = [
                    [
                "",
                "",
                "",
                "",
                ""
                ],
                    ["""
                """,
                "",
                "",
                "",
                ""
                ]
        ]
        #answer_bank = {"": , "": }
    count = []
    axes_three = ["Your Score"]
    chart_data = pd.DataFrame(
        {
            "Days": count,
            "Score (percentage)": [x for x in axes_three if x != "Your Score"],
            "Score": np.random.choice(axes_three, size=len(count)).tolist(),
        }
    )
    with col1:
        st.line_chart(data=chart_data, x="Days", y="Score (percentage)")
    with col2:
        with st.form("ela-form", enter_to_submit=False):
            for i in range(1, 3):
                q = random.randint(0, 1)
                if i > 1:
                    while q in qlist:
                        q = random.randint(0, 1)
                qlist.append(q)
                question = question_bank[q]
                st.write(f"{i}. {question[0]}")
                choice = st.radio(label="", options=[question[1], question[2], question[3], question[4]], index=None, label_visibility="collapsed")
            if question[1] is choice:
                num = 1
            elif question[2] is choice:
                num = 2
            elif question[3] is choice:
                num = 3
            elif question[4] is choice:
                num = 4
            qa.update({str(q): num})
            if len(qa) != 2:
                submit = st.form_submit_button(label="Submit", icon=":material/check:", disabled=True)
            elif len(qa) == 2:
                submit = st.form_submit_button(label="Submit", icon=":material/check:", disabled=False)
        if submit:
            count.append(count[-1]+1)
            for key in qa:
                if qa[key] == answer_bank[key]:
                    score += 1
            score = score/20
            score = score * 100
            axes_three.append(score)
            days += 1
elif not user.is_logged_in:
    login_screen()
