# viewing-party

## Setup

Install dependencies once at the beginning of this project with

```
python3 -m pip install -r requirements.txt
```

## Run Tests

Run tests with

```
python3 -m pytest
```

If you want to see any `print` statements print to the console:

```
python3 -m pytest -s
```

## Project Write-Up

```
{
  watchlist:[]
  favorites:[]
  watched:[]
  friends: {
    watched:[]
    }
}
```

Creates a data structure from input:
Given some fields, creates a movie dict
Given some user data, adds a movie to the watched list
Given some user data, adds a movie to the watchlist

move a movie from watchlist to watched


One loop:
What is the average rating of the movies I've watched
What is the most common genre of the movies I've watched

Nested loops:
Between my friends, what is the average rating of the movies they've watched
Most common genre of movies my friends have watched

Nested loops + Compare with me (could be another loop):
What are all the movies I've seen that they haven't seen
What are all the movies they've seen that I haven't seen
What are all the movies they've seen that I haven't seen on a streaming service that I have

Intense logic that can rely on previous functions if useful, probably the most optional?:
Pick a movie for me; it should match my most common genre, a movie i haven't seen, but one of my friends has
Pick a movie for me; it should be in my favorites, and my friends haven't seen it
