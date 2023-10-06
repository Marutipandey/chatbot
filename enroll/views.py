from django.shortcuts import render

# Define a list to store the chat history
chat_history = []

qna = {
    "hi": "Hey",
    "how are you": "I am fine",
    "what is your name": "My name is Priyanka",
}

def chatbot_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '').strip()

        if user_input.lower() == "quit":
            response = "Goodbye!"
        elif user_input in qna:
            response = qna[user_input]
        else:
            response = "I don't know the answer to that question."

        # Append the user's input and chatbot's response to the chat history
        chat_history.append(f'You: {user_input}')
        chat_history.append(f'Bot: {response}')

        return render(request, 'enroll/home.html', {'chat_history': chat_history})

    return render(request, 'enroll/home.html', {'chat_history': chat_history})
