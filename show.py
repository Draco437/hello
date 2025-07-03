SHOWS = [
    "Arthur",
    "Kim Possible",
    "Jimmy Nelson",
    "Avatar: The last airbinder"
]

def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.title().strip())

        print('.'.join(cleaned_shows))

main()