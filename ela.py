import streamlit as st

import pandas as pd

import numpy as np

import random

import sqlite3

profile = "hi"
if profile is not None:
    st.title("ELA")
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS profile (score LIST[INTEGER], day LIST[INTEGER])")
    connection.commit()
    hours = 0
    mins = 0
    secs = 0
    st.write(f"You have {hours} hours, {mins} minutes, and {secs} seconds until you can take the test again.")
    st.write(connection.total_changes)
    col1, col2 = st.columns(2)
    qa = dict()
    num = 0
    qlist = []
    score = dict()
    percentage = [5, 6, 3]
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

                Eliza had spent the last twenty years avoiding the cedar chest that rested in the corner of her attic.
            Within it lay letters—dozens of them—from her younger sister, Clara.
            They had parted ways long ago after an argument so fierce it turned love into silence.
            Eliza had never opened Clara's letters, convinced that the words within were filled with anger and blame.
            But now, as years stretched into decades and regret tightened its grip, she found herself drawn to the chest.
            With trembling hands, she lifted the lid and unfolded a yellowed envelope.
            "Eliza," the letter began, "I miss you. I'm sorry for everything."
            The words tumbled out like a flood, and by the last page, Eliza sat sobbing on the attic floor, overwhelmed by a love that had endured even when she thought it had been lost.
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
    answer_bank = {"1": 1, "2": 2}
    count = [1, 2, 3]
    chart_data = pd.DataFrame(
        {
            "Days": count,
            "Score (percentage)": [100, 30, 50],
            "Score": np.random.choice(["Your Score", 100, 30, 50], size=len(count)).tolist(),
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
            pass
        cursor.execute(f"INSERT INTO profile VALUES ({percentage}, {count})")
        connection.commit()
        connection.close()
elif profile is None:
    st.subheader("Sign in to take quizes")
    sign_in = st.button(label="Sign in", icon=":material/login:")
    if sign_in:
        st.switch_page("settings.py")
