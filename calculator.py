import streamlit as st

# Set the title of the app
st.title("Simple Calculator")

# Input fields for the numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Select box for the operation
operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate the result based on the selected operation
result = None
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        st.error("Cannot divide by zero!")

# Display the result
if result is not None:
    st.write(f"The result of {operation.lower()}ing {num1} and {num2} is: {result}")
