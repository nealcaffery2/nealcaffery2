from flask import Flask, request, jsonify
from flask_cors import CORS
from zillow_api import get_zillow_data
from chatgpt_api import call_chat_gpt_api
import openai

app = Flask(__name__)
CORS(app)

# Replace 'YOUR_API_KEY_HERE' with your actual OpenAI API key
openai.api_key = "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"

@app.route('/search', methods=['GET', 'POST'])
def search_properties():
    if request.method == 'GET':
        # Handle the GET request here (optional)
        return "This is the GET request for searching properties."

    elif request.method == 'POST':
        # Handle the POST request here
        data = request.json
        location = data.get('location')

        # Fetch data from Zillow API
        zillow_data = get_zillow_data(location)

        # Generate a prompt for ChatGPT based on Zillow data
        prompt = create_prompt(zillow_data)

        # Analyze with ChatGPT
        gpt_response = call_chat_gpt_api(prompt, openai.api_key)

        # Return the response in a JSON format
        return jsonify({"result": gpt_response})

def create_prompt(zillow_data):
    """
    Transforms Zillow data into a prompt for ChatGPT analysis.
    """
    prompt = "You are a real estate expert analyzing a list of properties. Your goal is to find the best real estate deals using two methods: the Wholesale Deal Finder (WDF) and the Underpriced Market Spotter (UMS).\n\n"

    # Loop through the properties in the Zillow data and add property details to the prompt
    for property_info in zillow_data['properties']:
        prompt += f"\n{property_info['address']}\n"
        prompt += f"- Listed Price: ${property_info['price']}\n"
        prompt += f"- Zestimate (as-is value): ${property_info['zestimate']}\n"

    prompt += "\n1. Wholesale Deal Finder (WDF):\n"
    prompt += "   - Calculate the Maximum Allowable Offer (MAO) for each property.\n"
    prompt += "   - Use the formula: (Zestimate × 0.7) - $10,000 for repairs - $10,000 for wholesale fee.\n"
    prompt += "   - Identify properties where the listed price is equal to or lower than the MAO.\n\n"

    prompt += "2. Underpriced Market Spotter (UMS):\n"
    prompt += "   - Identify properties where the Zestimate (as-is value) is higher than the asking price.\n"
    prompt += "   - Ensure that the property also fits within or better than the MAO criteria calculated in the WDF step.\n\n"

    prompt += "Please provide a list of properties that meet or are better than the criteria for a good real estate investment according to the WDF and UMS methods. If a property doesn't meet the criteria, exclude it from the list."

    return prompt

if __name__ == '__main__':
    # Set debug=False in a production environment
    app.run(debug=True, port=5000)
