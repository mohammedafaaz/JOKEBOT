from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Example jokes
jokes = [
  {"joke": "Why did the computer go to the doctor? It had a virus."},
  {"joke": "Why don't skeletons fight each other? They don’t have the guts."},
  {"joke": "Why don’t programmers like nature? It has too many bugs."},
  {"joke": "What do you call fake spaghetti? An impasta."},
  {"joke": "Why don't some couples go to the gym? Because some relationships don't work out."},
  {"joke": "Why did the bicycle fall over? It was two-tired."},
  {"joke": "Why did the tomato turn red? Because it saw the salad dressing."},
  {"joke": "Why did the mushroom go to the party? Because he was a fungi."},
  {"joke": "Why can't you trust an atom? Because they make up everything."},
  {"joke": "Why did the math book look sad? Because it had too many problems."},
  {"joke": "Why don't eggs tell jokes? Because they might crack up."},
  {"joke": "Why was the math lecture so long? Because it went on for pi."},
  {"joke": "What’s orange and sounds like a parrot? A carrot."},
  {"joke": "Why can't you play hide and seek with mountains? Because they always peak."},
  {"joke": "What did one Indian plate say to the other? Keep calm and curry on."},
  {"joke": "Why did the software developer go broke? Because he used up all his cache."},
  {"joke": "What do you call a fake noodle? An impasta."},
  {"joke": "What’s the best way to watch a fly fishing tournament? Live stream."},
  {"joke": "Why are ghosts bad at lying? Because they are too transparent."},
  {"joke": "What’s a skeleton’s least favorite room? The living room."},
  {"joke": "What do you call cheese that isn't yours? Nacho cheese."},
  {"joke": "Why did the coffee file a police report? It got mugged."},
  {"joke": "What do you call a bear with no teeth? A gummy bear."},
  {"joke": "Why did the student eat his homework? Because his teacher told him it was a piece of cake."},
  {"joke": "Why are frogs so happy? They eat whatever bugs them."},
  {"joke": "Why don't skeletons fight each other? They don’t have the stomach for it."},
  {"joke": "What do you call a snowman in the summer? A puddle."},
  {"joke": "What’s a skeleton’s least favorite instrument? The trombone."},
  {"joke": "Why don’t ants get sick? Because they have tiny ant-bodies."},
  {"joke": "Why did the orange stop? Because it ran out of juice."},
  {"joke": "Why do cows have hooves instead of feet? Because they lactose."},
  {"joke": "What do you call a can opener that doesn’t work? A can’t opener."},
  {"joke": "Why can’t a nose be 12 inches long? Because then it would be a foot."},
  {"joke": "What do you call a sleeping bull? A bulldozer."},
  {"joke": "Why did the chicken join a band? Because it had the drumsticks."},
  {"joke": "What do you call a cow that plays a musical instrument? A moo-sician."},
  {"joke": "Why did the banana go to the doctor? Because it wasn’t peeling well."},
  {"joke": "Why do bicycles fall over? Because they are two-tired."},
  {"joke": "What’s a skeleton’s favorite instrument? The trombone."},
  {"joke": "Why don’t skeletons ever fight each other? They don’t have the guts."},
  {"joke": "Why don’t some couples go to the gym? Because some relationships don’t work out."},
  {"joke": "What do you call a dog magician? A labracadabrador."},
  {"joke": "Why did the grape stop in the middle of the road? It ran out of juice."},
  {"joke": "Why did the football player go to jail? Because he got caught holding."},
  {"joke": "What’s a frog’s favorite candy? Lollihops."},
  {"joke": "Why did the scarecrow win an award? Because he was outstanding in his field."},
  {"joke": "What’s big, grey, and doesn’t matter? An irrelephant."},
  {"joke": "Why was the broom late? It swept in."},
  {"joke": "Why don't oysters donate to charity? Because they are shellfish."},
  {"joke": "Why don't skeletons ever fight? They don't have the guts."}
]


# Keywords to detect reactions and control the flow
positive_reactions = ["haha", "good", "funny", "amazing", "wow", "lol", "lmao", "hahaha", "omg", "insane"]
negative_reactions = ["stop", "bye", "end", "enough", "boring", "sorry", "no", "go"]
yes_responses = ["yes", "yeah", "sure", "please", "yup", "okay", "ok", "why", "not"]
end_dialogue = "Thanks for chatting! See you next time!"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_joke', methods=['GET'])
def get_joke():
    joke = random.choice(jokes)
    return jsonify(joke)

@app.route('/get_feedback', methods=['POST'])
def get_feedback():
    user_input = request.json.get("reaction").lower()

    # Check for positive feedback to ask if user wants to hear another joke
    if any(react in user_input for react in positive_reactions):
        return jsonify({"next_action": "ask_for_another"})
    
    # Check if user wants to end the session
    elif any(react in user_input for react in negative_reactions):
        return jsonify({"next_action": "end_session", "end_dialogue": end_dialogue})

    # Otherwise, continue waiting for feedback
    return jsonify({"next_action": "wait_for_feedback"})

@app.route('/get_next_action', methods=['POST'])
def get_next_action():
    user_input = request.json.get("reaction").lower()

    # Check for "yes" or "sure" responses for another joke
    if any(react in user_input for react in yes_responses):
        return jsonify({"next_action": "tell_another_joke"})
    elif any(react in user_input for react in negative_reactions):
        return jsonify({"next_action": "end_session", "end_dialogue": end_dialogue})

    # Continue waiting for next feedback or action
    return jsonify({"next_action": "wait_for_feedback"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

