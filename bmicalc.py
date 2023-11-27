import streamlit as st 

st.title("BMI Calculator")

img = "images/BMI.jpg"
img2="images/Success.jpg"
img3="images/Failure.jpg"
st.image(img, width=500)

st.subheader("Introduction")

st.text("""
BMI is a person’s weight in kilograms divided by the square of height in meters. 
A high BMI can indicate high body fatness.

If your BMI is less than 18.5, it falls within the underweight range.
If your BMI is 18.5 to <25, it falls within the healthy weight range.
If your BMI is 25.0 to <30, it falls within the overweight range.
If your BMI is 30.0 or higher, it falls within the obesity range.

Obesity is frequently subdivided into categories:

Class 1: BMI of 30 to < 35
Class 2: BMI of 35 to < 40
Class 3: BMI of 40 or higher. 
Class 3 obesity is sometimes categorized as “severe” obesity.
	""")


weight = st.slider("Enter your Weight in KG", 0, 200) #new


if 'button' not in st.session_state:
    st.session_state.button = False
if 'button2' not in st.session_state:
    st.session_state.button2 = False
def click_button():
        st.session_state.button = not st.session_state.button
def click_button2():
        st.session_state.button2 = not st.session_state.button2

st.button("Meters", on_click=click_button) #new
if st.session_state.button: #new
    height = st.number_input("Enter your Height in Meters", 0.1) #new
    bmi = weight/(height)**2
    st.write(f"Your BMI is {bmi}")
    if bmi>=18.5 and bmi<25:
         st.image(img2, width=200)
    else:
         st.image(img3, width=200)
st.button("Feet and Inches", on_click=click_button2)
if st.session_state.button2: 
    Feet = st.selectbox("Enter the feet", (1,2,3,4,5,6,7,8)) #new
    Inches = st.selectbox("Enter the inches", (0,1,2,3,4,5,6,7,8,9,10,11))
    height=(Feet*30.48+Inches*2.54)/100
    bmi = weight/(height)**2
    st.write(f"Your BMI is {bmi}") 
    if bmi>=18.5 and bmi<25:
         st.image(img2)
    else:
         st.image(img3)

