import requests
from bs4 import BeautifulSoup

# pretty print lib
import pprint

response = requests.get("https://news.ycombinator.com/news")
# Parse this html string (response.text) into an object we could use (soup)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.a)

# Find the 1st HTML element and returns it
# print(soup.find("a"))

# Find and return all target HTML elements
# print(soup.find_all("a"))

# select.  Wraps a piece of data in CSS selector.
search = BeautifulSoup(response.text, "html.parser")

# return all elements with a score class
# print(search.select(".score"))

# returns element with a specific ID:
# print(search.select("#score_24615787"))

# returns all element with class storylink:
links = search.select(".storylink")

# returns all elements with class score:
votes = search.select(".score")
# print(votes)

# returns all elements with class score:
# votes = search.select(".score")[0]
# print(votes)

# return all elements with class subtext
subtext = search.select(".subtext")


# Sorting data function:
def sort_stories_by_votes(hnlist):
    # key are used to sort dictionaries. reverse=  higher to lower:
    return sorted(hnlist, key=lambda key: key["votes"], reverse=True)


# Filtering Data function:
def create_custom_hn(links, subtext):
    # Create empty hackernews list:
    hn = []
    # We only want the titles:
    for index, item in enumerate(links):
        # .getText() is a Beautifulsoup method that returns text inside an element.
        title = item.getText()

        # return "href" attribute, and in the 2nd param assign None as default in case "href" not found.
        href = item.get("href", None)
        vote = subtext[index].select(".score")
        if len(vote):
            # We want to return "points" as an int, and without the word "points"
            points = int(vote[0].getText().replace("points", ""))
            if points > 99:
                hn.append({
                    "title": title,
                    "link": href,
                    "votes": points
                })

    return sort_stories_by_votes(hn)


# print(create_custom_hn(link, subtext))
pprint.pprint(create_custom_hn(links, subtext))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
