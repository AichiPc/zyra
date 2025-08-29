from transformers import pipeline

# Load pre-trained model
chatbot = pipeline("text-generation", model="gpt2")

# Personality definition
zyra_persona = """
You are Zyra, a friendly bee mentor who loves teaching students.
You explain things clearly, give examples, and encourage learning.
Keep responses kind, engaging, and slightly playful like a bee buzzing.
"""

def get_response(user_input):
    prompt = f"{zyra_persona}\nStudent: {user_input}\nZyra:"
    response = chatbot(prompt, max_length=150, do_sample=True, temperature=0.7)[0]['generated_text']
    return response.split("Zyra:")[-1].strip()

if __name__ == "__main__":
    print("🐝 Zyra the Bee Mentor is ready! Type 'quit' to exit.")
    while True:
        user_input = input("Student: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        print("Zyra:", get_response(user_input))
