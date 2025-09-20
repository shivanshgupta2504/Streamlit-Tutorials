import streamlit as st
import datetime

st.title("User Information Form")

form_values = {
    "name": None,
    "age": None,
    "height": None,
    "gender": None,
    "dob": None,
    "location": None
}

# Untill we press the submit button, any change in the form
# like writing the name, entering the age, will not rerun the app
with st.form(key="user_info_form"):
    form_values["name"] = st.text_input("Enter your Name:")
    form_values['age'] = st.number_input("Enter your Age:")
    form_values['height'] = st.number_input("Enter your Height (cm):")
    form_values['gender'] = st.selectbox(label="Gender", options=["Male", "Female", "Other"])
    form_values['dob'] = st.date_input(
        label="Enter your Birthdate:",
        min_value=datetime.date(year=1900, month=1, day=1),
    )
    form_values['location'] = st.text_area("Enter your Location:")

    submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        if not all(form_values.values()):
            st.warning("All fields are required")
        else:
            st.balloons()
            st.write("### User Information")
            for key, value in form_values.items():
                st.write(f"- `{key}`: {value}")
