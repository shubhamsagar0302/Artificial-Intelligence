pip install fuzzywuzzy
from fuzzywuzzy import fuzz
import random
# Define movie recommendations for each genre
movie_recommendations = {
    "action": ["Bade Miyan Chote Miyan", "Yodha", "Fighter", "HanuMan", "Captain Miller"],
    "adventure": ["Shivaay", "Bholaa", "Kartikeya", "Kartikeya 2", "Uunchai"],
    "comedy": ["Teri Baaton Mein Aisa Uljha Jiya", "Housefull 4", "Phir Hera Pheri", "Hungama 2", "Dhol"],
    "drama": ["Kantara: A Legend", "Crew", "Maidaan", "Main Atal Hoon", "Madgaon Express"],
    "fantasy": ["OMG2", "Angel", "BRO", "Avengers Endgame", "Godzilla x Kong: The New Empire"],
    "sci-fi": ["Mr. X", "Yashoda", "Ismart Shankar", "Black Adam", "Captain"],
    "suspense": ["Drishyam 2", "Mission Majnu", "HIT: The Second Case", "Freddy", "118"]
}
casual={'how are you?':'I am working fine, so I guess I am alright! How about you?',
        'i am ok,fine': 'Thats nice to know',
        'what is your name?': 'My name is Teja',
        'who are you': 'I am Teja. I am an movie suggesting chatbot',
        'what can you do?': 'I am an movie suggesting chatbot. I can recommend you movies based on your favourite genres.'}

# Function to find the closest match for genres
def find_closest_genre(user_input):
    matches = []
    for genre in movie_recommendations.keys():
        ratio = fuzz.ratio(user_input, genre)
        if ratio > 70:  # Adjust threshold as needed
            matches.append((genre, ratio))
    if matches:
        closest_match = max(matches, key=lambda x: x[1])[0]
        return closest_match
    else:
        return None

def suggest_movie(genres):
    recommendations = []
    for genre in genres:
        closest_genre = find_closest_genre(genre)
        if closest_genre:
            recommendations.extend(movie_recommendations[closest_genre])
    return recommendations


def suggest():
    while True:
        print('Teja: Enter your preferred genres (comma-separated): ')
        user_input = input("You: ").lower()
        user_genres = [genre.strip() for genre in user_input.split(",")]
       
        recommendations = suggest_movie(user_genres)
        if recommendations:
            print("\nTeja: Here are some movie recommendations for you:")
            for recommendation in random.sample(recommendations, min(len(recommendations), 5)):
                print("-", recommendation)
        else:
            print("\nTeja: Sorry, I couldn't find any recommendations for the specified genres.")
       
        continue_chat = input("\nTeja: Would you like more recommendations? \nYou: (yes/no)").lower()
        while continue_chat not in ('y','n','no','yes'):
            continue_chat = input("\nTeja: Could'nt understand you. \n Would you like more recommendations? \nYou: (yes/no)").lower()
        if continue_chat not in ('y','yes'):
            print("Teja: Have a nice day! See you again later!")
            break
    return 

def chating(inp):
    if 'recom' in inp or 'sug' in inp:
        print("Teja: SURE!!")
        suggest()
        return True
    
    if 'hi' in inp or 'hey' in inp or 'hello' in inp:
        print('Teja: ',random.choice(["Hello!", "Hi there!", "Hey!", "how you doin?", "Howdy!"]))
        return False
        
    matches = []
    for chat in casual.keys():
        ratio = fuzz.ratio(inp, chat)
        if ratio > 50:  # Adjust threshold as needed
            matches.append((chat, ratio))
    if matches:
        closest_match = max(matches, key=lambda x: x[1])[0]
        print('Teja: ',casual[closest_match])
        return False
    else: 
        print("Teja: I could'nt quite undersand you. Can you rephrase the sentence")
    
while True:
    inp=input('You: ').lower()
    if chating(inp): break