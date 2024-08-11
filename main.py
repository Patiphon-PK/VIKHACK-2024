from openai import OpenAI
client = OpenAI()

while (True):
    user_input = input("Enter prompt: ")
    if user_input == "exit":
        print("exiting")
        break
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", 
            "content": "You're my math tutor"},
            {"role": "user", 
            "content": user_input}
        ]
    )
    print(completion.choices[0].message)