# Personal Movie Tracker

A simple Python script to manage your personal movie collection. Store movie details like **title**, **genre**, and **rating**, and search your collection by title or genre.

## Features
- Add movies with name, genre, and rating.
- Search movies by **title** or **genre**.
- View all movies in your collection.
- Saves data in a **JSON file** for persistence.

## Usage
1. Run the script:
python personal_movie_tracker.py

## Example

==== MyMovieDB ====
1. Add Movie
2. View All Movies
3. Search Movie
4. Exit
Choose an option (1-4): 1
Enter the movie name: Inception
Genre: Sci-Fi
Enter rating (0-10): 9
✅ Movie added

 ==== MyMovieDB ====
1. Add Movie
2. View All Movies
3. Search Movie
4. Exit
Choose an option (1-4): 1
Enter the movie name: Titanic
Genre: Romance
Enter rating (0-10): 8
✅ Movie added

 ==== MyMovieDB ====
1. Add Movie
2. View All Movies
3. Search Movie
4. Exit
Choose an option (1-4): 4
Exiting Database.

[
  {
    "title": "Inception",
    "genre": "Sci-Fi",
    "rating": 9
  },
  {
    "title": "Titanic",
    "genre": "Romance",
    "rating": 8
  }
]