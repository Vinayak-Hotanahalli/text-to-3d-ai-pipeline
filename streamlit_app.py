# Import necessary modules
import streamlit as st
from main import on_message
from openfabric_sdk.context import OpenfabricExecutionContext
from openfabric_pysdk.utility import Input

# Initialize the execution context
ctx = OpenfabricExecutionContext()

# Set the app title
st.title(" AI Creative 3D Generator")

# User input for creative prompt
user_prompt = st.text_input("Enter your creative idea:")

# Generate button triggers AI pipeline
if st.button("Generate"):
    input = Input(text=[user_prompt])              # Prepare input
    output = on_message(ctx, input)                # Call main processing
    st.success(output.text[0])                     # Show success message
    st.image("generated_image.png")                # Display the generated image
