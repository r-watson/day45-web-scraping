from bs4 import BeautifulSoup


# use https://news.ycombinator.com/robots.txt to see what a site allows you to scrape

with open("website.html", encoding='utf-8') as website:
    contents = website.read()


soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title.string)
# print with indentations:
# print(soup.prettify())
# show first anchor tag:
# print(soup.a)

all_anchor_tags = soup.find_all(name="p")
print(soup.find_all("p"))
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     # print(tag.get("href"))

heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_='heading')
# print(section_heading)

# can use CSS selectors to search for objects. Use multiple elements e.g. 'p a' for paragrah and anchor. Or # for IDs. Or . for class.
name = soup.select_one(selector='#name')
print(name)

headings = soup.select('.heading')
print(headings)

