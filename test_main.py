from main import on_message, Input, DummyContext

if __name__ == '__main__':
    # Create dummy context instance
    ctx = DummyContext()

    # Input prompt to generate the image and 3D model for
    input_data = Input(text=["A futuristic city skyline at sunset"])

    # Call the main on_message function
    result = on_message(ctx, input_data)

    # Print the output message
    print(result.text[0])
