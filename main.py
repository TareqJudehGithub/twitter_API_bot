import requests
from bs4 import BeautifulSoup

# pretty print lib
import pprint

response = requests.get("https://news.ycombinator.com/news")


search = BeautifulSoup(response.text, "html.parser")
links = search.select(".storylink")
votes = search.select(".score")
# return all elements with class subtext
subtext = search.select(".subtext")


# Sorting data function:
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda key: key["votes"], reverse=True)


# Filtering Data function:
def create_custom_hn(links, subtext):
    # Create empty hackernews list:
    hn = []
    # We only want the titles:
    for index, item in enumerate(links):
        title = item.getText()

        # Return "href" attribute:
        href = item.get("href", None)
        vote = subtext[index].select(".score")
        if len(vote):
            # Return "points" as an int, and without the word "points"
            points = int(vote[0].getText().replace("points", ""))
            if points > 99:
                hn.append({
                    "title": title,
                    "link": href,
                    "votes": points
                })

    return sort_stories_by_votes(hn)


if __name__ == '__main__':
    pprint.pprint(create_custom_hn(links, subtext))



