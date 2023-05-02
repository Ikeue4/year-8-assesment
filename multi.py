import difflib

def match_input(possible_inputs):
    user_input = input("Enter your input: ")
    while user_input not in possible_inputs:
        closest_match = difflib.get_close_matches(user_input, possible_inputs, n=1)
        if closest_match:
            suggestion = closest_match[0]
            confirm_suggestion = input(f"Did you mean '{suggestion}' instead? [y/n] ")
            if confirm_suggestion.lower() == "y":
                return suggestion
        user_input = input("Invalid input. Please try again: ")
    return user_input

possible_inputs = ["apple", "banana", "orange"]
matched_input = match_input(possible_inputs)
print("Your input matched:", matched_input)