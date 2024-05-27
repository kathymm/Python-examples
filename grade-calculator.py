# Get the user's grade score
while True:
    try:
        grade = int(input("Please enter your grade score (between 0 and 100): "))
        if 0 <= grade <= 100:
            break  # Exit the loop if valid input is received
        else:
            print("You have entered a wrong input. Please enter a grade between 0 to 100")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Assign grade and response based on the score
if 0 <= grade <= 39:
    response = "You are below the pass mark. You can do better!"
elif 40 <= grade <= 55:
    response = "You have a 'Pass' in this course"
elif 56 <= grade <= 69:
    response = "You have a 'Lower Credit' in this course"
elif 70 <= grade <= 80:
    response = "You have an 'Upper Credit' in this course"
else:
    response = "You have Scored 'Excellent' in this course"

# Print the response
print(response)
