from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

# Load Flan-T5
model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

chatbot = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

print("🐝 Zyra the Bee Mentor is ready! Type 'quit' to exit.")

# Define Zyra's role (used as context, not literal text)
system_prompt = (
    "You are Zyra, a friendly bee mentor who helps students learn. "
    "Always answer clearly, encourage students, and keep responses short and factual."
)

def get_response(user_input):
    # With Flan-T5 we frame it as an instruction
    full_prompt = f"Answer as Zyra, a friendly bee mentor who helps students learn.\n\nQuestion: {user_input}\nAnswer:"
    
    response = chatbot(
        full_prompt,
        max_new_tokens=150,
    )[0]['generated_text']

    return response.strip()


# Main loop
while True:
    user_input = input("Student: ")
    if user_input.lower() == "quit":
        break
    print("Zyra:", get_response(user_input))
