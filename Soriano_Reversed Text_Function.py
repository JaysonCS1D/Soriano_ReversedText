# Keep asking the user until a valid text is entered
while True:
    # Get user input
    user_input = input("Type something: ")

    # Check if the input contains only alphabetic characters
    if user_input.isalpha():
        # Reverse the text
        reversed_text = user_input[::-1]

        # Display the reversed text
        print(f"Here is your text in reverse: {reversed_text}")

        # Exit the loop since a valid text was provided
        break
    else:
        # Inform the user about the error
        print("Error: Please enter text without numbers or special characters.")
