from flask import Flask, render_template, jsonify, request
import requests
import random

app = Flask(__name__)

# URL for the Official Joke API
JOKE_API_URL = "https://official-joke-api.appspot.com/random_joke"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_joke", methods=["GET"])
def get_joke():
    try: 
        response = requests.get(JOKE_API_URL)
        if response.status_code == 200:
            joke = response.json()
            return jsonify({
                "setup": joke.get("setup", ""),
                "punchline": joke.get("punchline", "")
            })
        else:
            return jsonify({"error": "Failed to fetch joke"}), 500
    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

def generate_automated_response(user_message):
    """
    Generate an automated response based on rule‑based keyword matching with random selection.
    This function is used to process feedback after a joke.
    """
    message = user_message.lower()
    
    # Define response lists
    positive_responses = [
        "I'm glad you enjoyed it! Would you like another joke?",
        "Awesome, happy to hear you liked it! Want another one?",
        "Great to know you found it funny! Shall I tell another joke?",
        "I'm thrilled you enjoyed that one! Would you like to hear another joke?",
        "Awesome, your laugh just made my day! Ready for another round of humor?",
        "Great to hear it hit the mark! How about another joke to keep the fun going?",
        "I'm so glad that brought a smile to your face! Want to try another joke?",
        "Yay! I’m delighted you liked that one. Care for another burst of laughter?",
        "Your positive vibes mean a lot! Would you like to hear another joke?",
        "Fantastic! Nothing beats a good laugh—want to hear another joke?",
        "That’s music to my ears! Shall I share another joke?",
        "Hooray, your feedback makes my day! Ready for another joke?",
        "I'm happy you enjoyed it! How about another joke to keep the fun rolling?"
    ]
    negative_responses = [
        "I'm sorry that one didn't land. Would you like to try another joke?",
        "I understand – humor can be hit or miss. Want to give another joke a try?",
        "Sorry, I know that one missed the mark. Would you like another joke?",
        "I'm sorry that one didn't hit the mark. Would you like to try another joke?",
        "Oops, looks like that joke fell flat. Want to give another one a shot?",
        "I appreciate your honesty—sorry if that one missed the mark. Shall I try a different joke?",
        "My apologies if that joke wasn’t your style. Would you like to hear another one?",
        "I’m sorry that didn’t land as intended. Want me to try another joke?",
        "I appreciate your feedback. Let’s see if another joke suits your taste better—interested?",
        "Sorry about that one! How about I try a different joke to see if it hits the spot?",
        "I understand that didn’t work for you. Would you like to hear a different joke?",
        "My apologies if that joke wasn't funny for you. Can I offer you another one?",
        "Thanks for the candid feedback. Want to give another joke a try and see if it works better?"
    ]
    default_responses = [
        "Would you like another joke?, if yes type (joke) if not type (no) ",
        "Should I tell you another joke? if yes type (joke) if not type (no)",
        "How about another joke? if yes type (joke) if not type (no)"
    ]
    
    # Check for negative compound phrases first
    if "not funny" in message:
        return random.choice(negative_responses)
    elif any(word in message for word in ["boring", "bad", "waste", "meh","not funny","understand","what","understood","didnt","didn't"]):
        return random.choice(negative_responses)
    # Then check for positive feedback
    elif any(word in message for word in ["funny", "great", "awesome", "hilarious", "loved","haha","lol","lmao"]):
        return random.choice(positive_responses)
    else:
        return random.choice(default_responses)

@app.route("/generate_response", methods=["POST"])
def generate_response_endpoint():
    data = request.get_json()
    user_message = data.get("message", "")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    response_text = generate_automated_response(user_message)
    return jsonify({"response": response_text})

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5000)