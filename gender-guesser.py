from genderize import Genderize

def predict_gender(first_name):
    genders = Genderize().get([first_name])
    gender = genders[0]['gender']
    probability = genders[0]['probability'] * 100
    
    if gender == 'unknown':
        return "Gender unknown"
    else:
        return f"Predicted gender: {gender} (Probability: {probability:.2f}%)"

# Example usage
first_name = input("Enter the first name: ")
result = predict_gender(first_name)
print(result)
