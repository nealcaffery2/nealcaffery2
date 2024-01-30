from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Replace 'YOUR_API_KEY_HERE' with your actual OpenAI API key
openai.api_key = "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"

@app.route('/process_data', methods=['POST'])
def process_data():
    # Extract data from the request
    data = request.json
    zillow_data = data['zillowData']

    # Make a call to the ChatGPT API with the Zillow data
    chat_gpt_response = call_chat_gpt_api(zillow_data)

    # Send the processed data back to the extension
    return jsonify(chat_gpt_response)

def call_chat_gpt_api(zillow_data):
    # Here you'll create your prompt using Zillow data and your formulas
    prompt = create_prompt(zillow_data)

    try:
        # Call the ChatGPT API with your prompt
        response = openai.Completion.create(
            engine="text-davinci-004",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return str(e)  # You should handle errors appropriately in production

def create_prompt(zillow_data):
    # Create and return a prompt based on the property data from Zillow
    # and your investment formulas.
    # This is a placeholder function; you need to implement it based on your data and formulas.
    return "Based on the following property details ... Is this a good investment?"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
