import webbrowser

user_term = input("Enter your search term : ").replace(' ', '+')

webbrowser.open("https://www.youtube.com/search?q=" + user_term)
