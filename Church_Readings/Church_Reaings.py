import requests
from bs4 import BeautifulSoup


def get_url():
    #this will get the date from the user, and will enable us to find the right html (no error handling yet)
    print("Input a date that is a sunday")
    day = input("Day: ")
    month = input("Month: ")
    year = input("Year: ")

    #exmaple: https://www.vaticannews.va/en/word-of-the-day/2024/10/13.html
    url = "https://www.vaticannews.va/en/word-of-the-day/"
    new_url = url + year + "/" + month + "/" + day + ".html"
    return new_url

def print_choices(readings):
    for i, reading in enumerate(readings):
        number = i + 1
        print(f"[{number}] {reading}")

def print_all_paragraphs(paragraphs): #for testing
    for i, paragraph in enumerate(paragraphs):
        number = i + 1
        print(f"[{number}] {paragraph.text}")
        print("\n\n")

def find_reading_by_heading(paragraphs, heading, add):
    #find the key word and return the corresponding paragraphs
    for i, paragraph in enumerate(paragraphs):
        if heading.lower() in paragraph.text.lower():
            return "\n\n".join([p.text for p in paragraphs[i:i+add]])  # Return the next few paragraphs after the heading
    return "Not found"

def find_learnings_by_heading(paragraphs):
    for i, paragraph in enumerate(paragraphs):
        if "gospel" in paragraph.text.lower():
            return paragraphs[i+3].text 
    return "Not found"

# start of the code 
#
#
link = get_url()
html = requests.get(link)
soup = BeautifulSoup(html.content, "html.parser")

#find the tags that have the paragraph tag
paragraphs = soup.find_all('p')

#ask user what they want to read
readings = ["First Reading", "Second Reading", "Gospel", "Learnings"]
print("What do you want to read?")
print() #new line 
print_choices(readings)

print()
selected = int(input("select (number): "))
print() #new line

#print out what they asked for
print(readings[selected-1])
print()

if selected == 1:  # First Reading
    first_reading = find_reading_by_heading(paragraphs, "First Reading", 3)
    print(first_reading)
elif selected == 2:  # Second Reading
    second_reading = find_reading_by_heading(paragraphs, "Second Reading", 3)
    print(second_reading)
elif selected == 3:  # Gospel
    gospel = find_reading_by_heading(paragraphs, "Gospel", 3)
    print(gospel)
elif selected == 4:  # Learnings (you might need a different heading for this)
    learnings = find_learnings_by_heading(paragraphs)
    print()
    print(learnings)

print()
print()


