from googlesearch import search
from bs4 import BeautifulSoup
from bs4 import NavigableString
from bs4 import Tag
from bs4 import Comment
import requests
import os
# md_yaml = "---\n" + \
#           "layout: page\n" + \
#           "title: AWWW task 1\n" + \
#           "---\n\n"

words_to_skip = [ \
        "header", \
        "navigation", \
        "bar", \
        "banner", \
        "button", \
        "lang" \
    ]

def is_printable(tag):
    return any(c.isalpha() for c in tag.get_text())

# table[is_table, rows, colums]
def process_tag(tag, url, output, table, do_strip=False, search_for=[0]):
    if (not isinstance(tag, NavigableString) and \
        not isinstance(tag, Tag)) or \
       isinstance(tag, Comment):
        return None

    if tag.get_text().isspace():
        return None

    if isinstance(tag, NavigableString):
        if table[0] == 1 and table[1] >= 2 and is_printable(tag) and search_for[0] > 0:
            search_for[0] = search_for[0] - 1
            file = str(tag.strip()) + ".md"
            print("searching for: ", tag.strip())
            url_2 = next(search(f"{tag.strip()} description"), None)
            print("Found: " + url_2)
            process_website(file, url_2)
            output.append("[" + tag.strip() + "]({% link " + tag.strip() + ".md %})")
        elif do_strip:
            output.append(tag.strip().replace("\n", ""))
        else:
            output.append(tag)
        return None

    for key, value in tag.attrs.items():
        for word in words_to_skip:
            if word in value:
                return None

    match tag.name:
        # Assuming these tags does not have any children tags.
        case "b" | "strong":
            output.append("**" + tag.get_text().strip().replace('\n', '') + "** ")
        case "i" | "cite" | "address" | "em":
            output.append("*" + tag.get_text().strip().replace('\n', '') + "* ")
        case "h1" | "h2" | "h3" | "h4" | "h5" | "h6":
            output.append("\n")
            output.append("#" * int(tag.name[1]) + " " + tag.get_text().strip().replace("\n", ""))
            output.append("\n")
        case "img":
            image = tag.get("src", "")
            if  not image.startswith("http"):
                image = url.split(".com/")[0] + ".com/" + image
            output.append(f"![Image is supposed to be here!]({image}) ")
        case "a":
            link = tag.get("href", "")
            if  not link.startswith("http"):
                link = url.split(".com/")[0] + ".com/" + link
            output.append(" [" + tag.get_text().strip().replace('\n', '') + "](" + link + ") ")
        # These tags can have children tag.
        case "p":
            output.append("\n")
            output.append("\n")
            for x in tag.children:
                process_tag(x, url, output, table, do_strip=do_strip, search_for=search_for)
        case "table":
            output.append("\n")
            output.append("\n")
            table = [1,0,0]
            for x in tag.children:
                process_tag(x, url, output, table, do_strip=do_strip, search_for=search_for)
            table = [0,0,0]
        case "tr":
            if output[-1][-1] != "\n":
                output.append(" |")
                output.append("\n")

            if table[0] == 1:
                table[1] = table[1] + 1

            if table[0] == 1 and table[1] == 2:
                output.append("| :---: " * table[2])
                output.append(" |")
                output.append("\n")


            for x in tag.children:
                process_tag(x, url, output, table, do_strip=True, search_for=search_for)

            if output[-1][-1] != "\n":
                output.append(" |")
                output.append("\n")
        case "th" | "td":
            cols = int(tag.attrs.get("colspan", "1"))
            output.append("| " * cols)
            if table[0] == 1 and table[1] == 1:
                table[2] += cols

            for x in tag.children:
                process_tag(x, url, output, table, do_strip=do_strip, search_for=search_for)
        case "li":
            if output[-1][-1] != "\n":
                output.append("\n")
            output.append("- ")
            for x in tag.children:
                process_tag(x, url, output, table, do_strip=True, search_for=search_for)
            output.append("\n")
        case "ul" | "ol":
            output.append("\n")
            output.append("\n")
            for x in tag.children:
                process_tag(x, url, output, table, do_strip=do_strip, search_for=search_for)
        case "style" | "script" | "noscript" | "caption":
            return None
        case "br":
            if table[0] == 0:
                output.append("\n")
                output.append("\n")
            else:
                output.append(" ")
        case default:
            for x in tag.children:
                process_tag(x, url, output, table, do_strip=do_strip, search_for=search_for)


def process_website(file, website, search_for=[0]):
    print(website)
    file_w = open(file, "w")
    data = requests.get(website)
    # main_file_site.write(data.text)
    os.makedirs("data_scraps", exist_ok=True)
    open("data_scraps/" + file.split(".md")[0] + ".html", "w").write(data.text) # source code for debug
    main_soup = BeautifulSoup(data.text, 'html.parser')
    output = [" "]
    process_tag(main_soup.body, website, output, [0,0,0], search_for=search_for)
    # file_w.write(md_yaml)
    file_w.write("---\n")
    file_w.write("layout: page\n")
    file_w.write("title: " + file.split(".md")[0] + "\n")
    file_w.write("---\n")
    for text in output:
        file_w.write(text)


main_file = "index.md"
default_website = "https://www.tiobe.com/tiobe-index/"
process_website(main_file, default_website, search_for=[10])
