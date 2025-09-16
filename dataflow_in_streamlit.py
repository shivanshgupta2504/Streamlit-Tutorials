import streamlit as st

pressed1 = st.button("Button 1")
print(f"Button 1 state: {pressed1}")

st.write(
    "Every time any event occurs like `pressing a button` in our App, there is a change in state, which"
    " reruns the entire script again"
)
st.write("In case of this button, initially it is returning `False` or say it was in `False state`, but"
         " after pressing the button, on next `Rerun` it's state changes to `True`"
)

# Let's say I have second button
pressed2 = st.button("Button 2")
print(f"Button 2 state: {pressed2}")

st.write("In case of two buttons, they work like a Toggle switch. "
         "So initially both are `False`, but when I pressed `Button 1`, it's state will be `True` on next `Rerun` "
         "and on the other hand since I didn't pressed `Button 2`, it's state will remain `False` on next Rerun. "
         "Same thing will happen if I preesed `Button 2` next time, there values will toggle untill I refresh the app"
)
