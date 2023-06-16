from flask import Flask, render_template, request
import openai

# Set up your OpenAI API credentials
openai.api_key = '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'

app = Flask(__name__)

def generate_response(prompt):
    # Generate a response from ChatGPT
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract and return the generated reply
    reply = response.choices[0].text.strip()
    return reply

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']

    # Generate a response based on user input
    chatbot_response = generate_response(user_input)

    return {'response': chatbot_response}

if __name__ == '__main__':
    app.run(debug=True)
