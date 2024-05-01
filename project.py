import random

# Dictionary of symptoms and corresponding possible diagnoses and prescriptions
symptoms = {
    "fever": {
        "diagnosis": "You may have a viral or bacterial infection. Please rest and drink plenty of fluids.",
        "prescription": "Take acetaminophen or ibuprofen for fever and body aches. If symptoms persist, see a doctor."
    },
    "stomach pain": {
        "diagnosis": "Stomach pain can have various causes, such as indigestion or gastritis.",
        "prescription": "Avoid spicy and fatty foods. Consider taking antacids for relief."
    },
    "headache": {
        "diagnosis": "Headaches can be caused by tension, dehydration, or migraines.",
        "prescription": "Rest in a quiet, dark room. Stay hydrated and consider taking pain relievers."
    },
    "cough": {
        "diagnosis": "A cough could be due to a respiratory infection, allergies, or irritation.",
        "prescription": "Stay hydrated and consider using cough drops. If cough persists, consult a doctor."
    },
    "sore throat": {
        "diagnosis": "Sore throat can be caused by viruses, bacteria, or allergies.",
        "prescription": "Gargle with warm salt water and stay hydrated. Consider using throat lozenges."
    },
    "fatigue": {
        "diagnosis": "Fatigue can result from lack of sleep, stress, or medical conditions.",
        "prescription": "Ensure you get enough rest and maintain a healthy lifestyle. If fatigue persists, consult a doctor."
    }
}

# ANSI escape codes for colored text
color_red = "\033[91m"
color_green = "\033[92m"
color_yellow = "\033[93m"
color_blue = "\033[94m"
color_purple = "\033[95m"
color_cyan = "\033[96m"
color_reset = "\033[0m"

def doctor():
    print("Welcome! I am your virtual doctor. How can I assist you today?")
    while True:
        user_input = input("Please describe your symptoms (type 'quit' to exit): ").lower()
        
        if user_input == 'quit':
            print("Thank you for consulting. Take care!")
            break
        
        response = ""
        for symptom in symptoms:
            if symptom in user_input:
                response += color_cyan + symptoms[symptom]["diagnosis"] + color_reset + "\n"
                response += color_green + symptoms[symptom]["prescription"] + color_reset + "\n"
        
        if response:
            print(response)
        else:
            print(color_red + "I'm sorry, I couldn't understand your symptoms. Please provide more details or try different wording." + color_reset)

# Run the virtual doctor program
doctor()
