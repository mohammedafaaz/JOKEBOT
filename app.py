
from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Example jokes
jokes = [
{"joke": "Why don't skeletons fight each other? They don't have the guts."},
{"joke": "What do you call fake spaghetti? An impasta."},
{"joke": "Why don't some couples go to the gym? Because some relationships don't work out."},
{"joke": "Why was the math book sad? Because it had too many problems."},
{"joke": "I told my wife she was drawing her eyebrows too high. She looked surprised."},
{"joke": "Why do cows have hooves instead of feet? Because they lactose."},
{"joke": "I used to play piano by ear, but now I use my hands."},
{"joke": "What do you call cheese that isn't yours? Nacho cheese."},
{"joke": "Why couldn't the bicycle stand up by itself? It was two-tired."},
{"joke": "I asked the librarian if the library had any books on paranoia. She whispered, 'They're right behind you.'"},
{"joke": "I told my computer I needed a break, and now it won’t stop sending me KitKats."},
{"joke": "How does Moses make his coffee? Hebrews it."},
{"joke": "What’s orange and sounds like a parrot? A carrot."},
{"joke": "How do you organize a space party? You planet."},
{"joke": "Why do we tell actors to 'break a leg'? Because every play has a cast."},
{"joke": "Why don’t oysters donate to charity? Because they are shellfish."},
{"joke": "What did the fish say when it hit the wall? Dam."},
{"joke": "What’s a skeleton’s least favorite room in the house? The living room."},
{"joke": "What do you call an alligator in a vest? An investigator."},
{"joke": "What did the ocean say to the beach? Nothing, it just waved."},
{"joke": "I’m reading a book about anti-gravity. It’s impossible to put down."},
{"joke": "Why don’t seagulls fly over the bay? Because then they’d be called bagels."},
{"joke": "I used to be a baker, but I couldn’t make enough dough."},
{"joke": "What did the janitor say when he jumped out of the closet? Supplies!"}, 
{"joke": "Why can’t you give Elsa a balloon? Because she’ll let it go."},
{"joke": "Why did the chicken join a band? Because it had the drumsticks."},
{"joke": "What do you call a pile of cats? A meow-tain."},
{"joke": "I told my wife she was drawing her eyebrows too high. She looked surprised."},
{"joke": "Why don’t skeletons ever use cell phones? Because they don’t have the guts to pick up the phone."},
{"joke": "Why do elephants never use computers? They’re afraid of the mouse."},
{"joke": "What do you call an alligator in a vest? An investigator."},
{"joke": "Why was the broom late? It swept in."},
{"joke": "I wondered why the frisbee kept getting bigger, but then it hit me."},
{"joke": "What do you call a snowman with a six-pack? An abdominal snowman."},
{"joke": "I once got into a fight with a broken pencil... It was pointless."},
{"joke": "What’s a vampire’s favorite fruit? A nectarine."},
{"joke": "Why don’t skeletons ever fight each other? They don’t have the guts."},
{"joke": "Why don’t skeletons ever go trick or treating? Because they have no body to go with."},
{"joke": "What do you call a bear with no teeth? A gummy bear."},
{"joke": "How do you catch a squirrel? Climb up in a tree and act like a nut."},
{"joke": "Why don’t scientists trust atoms? Because they make up everything."},
{"joke": "What do you get when you cross a snowman and a vampire? Frostbite."},
{"joke": "Why can’t you hear a pterodactyl go to the bathroom? Because the P is silent."},
{"joke": "Why don’t some couples go to the gym? Because some relationships don’t work out."},
{"joke": "Why did the coffee file a police report? It got mugged."},
{"joke": "I told my wife she was drawing her eyebrows too high. She looked surprised."},
{"joke": "What do you call a fish wearing a bowtie? Sofishticated."},
{"joke": "What’s brown and sticky? A stick."},
{"joke": "I can’t believe I got fired from the calendar factory. All I did was take a day off."},
{"joke": "What did one ocean say to the other ocean? Nothing, they just waved."},
{"joke": "Why did the scarecrow win an award? Because he was outstanding in his field."},
{"joke": "What’s the best way to watch a fly fishing tournament? Live stream."},
{"joke": "What do you call a shoe made of a banana? A slipper."},
{"joke": "How does a penguin build its house? Igloos it together."},
{"joke": "Why did the tomato turn red? Because it saw the salad dressing."},
{"joke": "Why did the golfer bring two pairs of pants? In case he got a hole in one."},
{"joke": "What did one wall say to the other wall? I’ll meet you at the corner."},
{"joke": "Why do chicken coops only have two doors? Because if they had four, they’d be chicken sedans."},
{"joke": "Why did the belt get arrested? For holding up a pair of pants."},
{"joke": "What’s a skeleton’s least favorite room in the house? The living room."},
{"joke": "Why don’t you ever see any hippos hiding in trees? Because they’re really, really good at it."},
{"joke": "What’s brown and sounds like a bell? Dung."},
{"joke": "I couldn’t figure out why I haven’t been to the gym lately... Then I realized I’m out of shape!"}, 
{"joke": "What do you call a man who lost all of his intelligence? A widow."},
{"joke": "Why do elephants never use computers? They’re afraid of the mouse."},
{"joke": "Why don’t seagulls fly over the bay? Because then they’d be bagels."},
{"joke": "What did the grape do when it got stepped on? Nothing but let out a little wine."},
{"joke": "Why don’t eggs tell jokes? Because they might crack up."},
{"joke": "Why did the bicycle fall over? It was two-tired."},
{"joke": "Why are frogs so happy? Because they eat whatever bugs them."},
{"joke": "Why do cows wear bells? Because their horns don’t work."},
{"joke": "Why was the broom late? It swept in."},
{"joke": "What did the paper say to the pencil? Write on."},
{"joke": "What does a cloud wear under his raincoat? Thunderwear."},
{"joke": "Why don’t skeletons fight each other? They don’t have the guts."},
{"joke": "Why did the baker go to therapy? He kneaded it."},
{"joke": "Why don’t skeletons use smartphones? They don’t have the guts to answer calls."},
{"joke": "Why was the math book sad? Because it had too many problems."},
{"joke": "What’s a vampire’s least favorite food? A steak."},
{"joke": "What did the tree say to the wind? Leaf me alone."},
{"joke": "What do you call a factory that makes kids' toys? A toy factory."},
{"joke": "What’s red and smells like blue paint? Red paint."},
{"joke": "Why can’t you trust stairs? They’re always up to something."},
{"joke": "Why don’t some couples go to the gym? Because some relationships don’t work out."},
{"joke": "Why was the mushroom invited to the party? Because he was a fungi."},
{"joke": "What’s a skeleton’s least favorite instrument? The trombone."},
{"joke": "Why can’t you trust an atom? Because they make up everything."},
{"joke": "What did the ocean say to the beach? Nothing, it just waved."},
{"joke": "Why did the computer go to the doctor? Because it had a virus."},
{"joke": "What do you call a dinosaur with an extensive vocabulary? A thesaurus."},
{"joke": "Why was the math book sad? Because it had too many problems."},
{"joke": "What did the fish say when it hit the wall? Dam."}
]


# Keywords to detect reactions and control the flow
positive_reactions = ["haha", "good", "funny", "amazing", "wow", "lol", "lmao", "hahaha", "omg", "insane"]
negative_reactions = ["stop", "bye", "end", "enough", "boring", "sorry", "no", "go"]
yes_responses = ["yes", "yeah", "sure", "please", "yup", "okay", "ok", "why", "not","yaa","ya"]
end_dialogue = "Catch you later! Keep smiling!"

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
