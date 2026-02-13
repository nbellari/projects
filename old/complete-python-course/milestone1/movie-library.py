import sys

# A list of movies maintained in-memory
# Each movie stored has the following attributes:
# 1. Movie Name (title)
# 2. Movie Release Year (year)
# 3. Movie Hero (main_cast)
# 4. IMDB Rating (imdb_score)
movie_library = []

menu = """
Movie Library:
--------------

1. [A]dd a movie to library
2. [L]ist all the movies in the library
3. [F]ind a movie in the library
4. [Q]uit
"""

ADD_MOVIE_OPTION = 0
LIST_MOVIES_OPTION = 1
FIND_MOVIE_OPTION = 2
QUIT_OPTION = 3

# A dictionary that maps the input option to an index
input_options_dict = {
    "A": ADD_MOVIE_OPTION,
    "a": ADD_MOVIE_OPTION,
    "L": LIST_MOVIES_OPTION,
    "l": LIST_MOVIES_OPTION,
    "F": FIND_MOVIE_OPTION,
    "f": FIND_MOVIE_OPTION,
    "Q": QUIT_OPTION,
    "q": QUIT_OPTION,
    "1": ADD_MOVIE_OPTION,
    "2": LIST_MOVIES_OPTION,
    "3": FIND_MOVIE_OPTION,
    "4": QUIT_OPTION
}

def display_menu():
    print(menu)

def input_option_is_valid(option):
    # Check if the entered option is a single character
    if len(option) != 1:
        return False
    
    if option in input_options_dict:
        return True
    
    return False

# input_option_is_valid() - should be called before this
def get_input_option_index(option):
    return input_options_dict[option]

def get_input_option():
    display_string = """
    Enter an option to continue
    (option number or first character [case insensitive]): 
    """
    return input(display_string)

def display_movie(movie):
    print(f"Movie: {movie['title']}, Release Year: {movie['year']}, IMDB Rating: {movie['imdb_score']}")

def validate_year(input_string):
    if not input_string.isdigit():
        return False
    
    # Year should be only 4 digits
    if len(input_string) != 4:
        return False

    return True

def get_year(input_string):
    return int(input_string)

def validate_imdb_score(input_string):
    # Best way is to utilize the float() in a try catch
    try:
        score = float(input_string)
        if score > 10.0:
            return False
        else:
            return True
    except:
        return False
    
def get_imdb_score(input_string):
    return float(input_string)    

def get_input(message,
              validate_string,
              get_data,
              is_empty_allowed=True):
    while (True):
        input_string = input(f"{message}: ")
        if not is_empty_allowed and len(input_string) == 0:
            print("Please enter a valid input!")
            continue
        if not validate_string(input_string):
            print("Please enter a valid input!")
            continue
        break

    return get_data(input_string)

def get_movie_details():
    movie = {}
    movie['title'] = get_input("Enter Movie Title",
                                      lambda x: True,
                                      lambda x: x,
                                      is_empty_allowed=False)

    movie['year'] = get_input("Enter the year of release (XXXX)",
                                     validate_year,
                                     get_year,
                                     is_empty_allowed=False)

    movie['imdb_score'] = get_input("Enter IMDB score (between 0 and 10)",
                                           validate_imdb_score,
                                           get_imdb_score,
                                           is_empty_allowed=False)

    movie['main_cast'] = get_input("Enter main cast",
                                          lambda x: True,
                                          lambda x: x,
                                          is_empty_allowed=True)
    
    return movie

def add_movie():
    movie = get_movie_details()
    movie_library.append(movie)

def list_movies():
    if len(movie_library) > 0:
        print("Movie List:")
        print("-----------")
    for movie in movie_library:
        display_movie(movie)

def find_movie():
    movie_name = get_input("Enter Movie Title",
                            lambda x: True,
                            lambda x: x,
                            is_empty_allowed=False)
    # Search for the movie in the library
    for movie in movie_library:
        if movie_name.lower() in movie['title'].lower():
            display_movie(movie)
            break
    else:
        print(f"Movie {movie_name} not found")

def quit_menu():
    sys.exit(0)

menu_actions = []
menu_actions.insert(ADD_MOVIE_OPTION, add_movie)
menu_actions.insert(LIST_MOVIES_OPTION, list_movies)
menu_actions.insert(FIND_MOVIE_OPTION, find_movie)
menu_actions.insert(QUIT_OPTION, quit_menu)

def get_menu_action():
    action = get_input_option()
    while not input_option_is_valid(action):
        action = get_input_option()
    return get_input_option_index(action)  

while (True):
    display_menu()
    action = get_menu_action()
    menu_actions[action]()

