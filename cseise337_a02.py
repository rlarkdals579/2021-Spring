# Name : Kangmin Kim
# NetID : KangKim
# SBUID : 111329652

import re


# Problem 1.

def highlight(pattern, string):
    matches = re.findall(pattern, string)

    if matches.__len__() > 0:
        result = string
        for m in matches:
            result = result.replace(m, "<" + m + ">")
    else:
        result = None
    return result

pattern = r'\bbook\B'
strings = ["bookstore", "booking", "textbooks", "returned books", "audiobook"]
new_strings = []

for string in strings:
    if string == strings[0] or highlight(pattern, string) is None:
        new_strings.append(highlight(pattern, string))
    else:
        new_strings.append(string)

print(new_strings)


# Problem 2.


def highlight_all(pattern, string):
    matches = re.findall(pattern, string)

    if matches.__len__() > 0:
        result = string
        for m in matches:
            result = result.replace(m, "<" + m + ">")
    else:
        result = None
    return result


pattern = r'o\w+'
string = "I'm Commander Shepard and this is my favorite store on the Citadel."
result = highlight_all(pattern, string)

print()
print(result)

#Problem 3.

def ruin_a_webpage(filename):
    new_line = ""
    open_paragraph = '<p>'
    close_paragraph = '</p>'
    open_span = '<span>'
    close_span = '</span>'

    line_breaks = '<br><br>'
    flag = True

    if re.search(".html|.htm", filename):
        file = open(filename)

    for line in file:
        if re.search(open_paragraph, line):
            if re.search(close_paragraph, line):
                if re.search(open_span, line):
                    no_close_span = re.sub(close_span, "", line)
                    no_open_span = re.sub(open_span, "", no_close_span)
                    new_line = new_line + re.sub('<p>|</p>\n', "", no_open_span)
                    new_line = new_line + line_breaks
                    new_line = new_line + '\n'
                    flag = False
                else:
                    new_line += re.sub('<p>|</p>\n', "", line)
                    new_line += line_breaks
                    new_line += '\n'
                    flag = False
            else:
                if (re.search(open_span, line)):
                    if (re.search(close_span, line)):
                        no_close_span = re.sub('</span>|\n', "", line)
                        no_open_span = re.sub(open_span, "", no_close_span)
                        new_line = new_line +  re.sub(open_paragraph, "", no_open_span)
                        flag = False

        elif(re.search(close_paragraph, line)):
            if (re.search(close_span, line)):
                no_close_span = re.sub(close_span, " ", line)
            new_line = new_line + re.sub('</p>\n', "", no_close_span)
            new_line += line_breaks
            new_line += '\n'
            flag = False
        if (flag):
            new_line = new_line + line
        flag = True
        output_file = open("ruined.html", "w+")
        output_file.write(new_line)
    else:
        return None


ruin_a_webpage("correct.html") # replce the name of the html file to your inputted file name
# and located in a same directory



#Problem 4.

def decompose_path(path):
    result = re.split(':',path)
    return result

path = "/usr/openwin/bin:/usr/ucb:/usr/bin:/bin:/etc:/usr/local/bin:/usr/local/lib:/usr/shareware/bin:/usr/shareware/lib:."
print()
print(decompose_path(path))


# Problem 5

# I don't the format of inputs when you are grading, so I just made sample html file.
# If you
# this html file should located in a same directory with this .py file and you need to change the file name in line #155
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
# </head>
# <body>
# <a href="https://www.google.com">Search at Google</a>
# <a href="https://www.naver.com">Search at naver</a>
#
# </body>
# </html>


def link_mapper(filename):
    if re.search(".html" or ".htm", filename):
        file = open(filename)
        dict = {"filename": []}

        for line in file:
            url = re.findall(r'<a[^>]* href="([^"]*)"', line)
            text = re.findall(r'>(.*?)</a>', line)
            if url:
                dict["filename"].append((text[0], url[0]))

        return dict

    else:
        return None

print()
print(link_mapper("input_filename.html")) #change the name of the file you want to run here.
# Place it in the same directory with this .py file and then run it.



# Problem 6

print()
text = input("Enter string: ")
newtext = ""


def grammarly(text):
    lst = text.split()
    i = 0
    new_txts = ""

    while i < len(lst):
        if lst[i] == "i":  # Capitalized i
            lst[i] = "I"

        if lst[i] == "an" or lst[i] == "An" or lst[i] == "AN" or lst[i] == "aN" and i != len(lst) - 1:  # an + non (a,i,e,o,u) -> a
            if not (lst[i + 1][0].lower() == "a" or lst[i + 1][0].lower() == "u" or
                    lst[i + 1][0].lower == "o" or lst[i + 1][0].lower() == "i" or lst[i + 1][0].lower() == "e"):
                lst[i] = "a"


        elif (lst[i] == "a" or lst[i] == "A") and i != len(lst) - 1:
            if lst[i + 1][0].lower() == "a" or lst[i + 1][0].lower() == "e" or lst[i + 1][0].lower() =="i" or \
                    lst[i + 1][0].lower() =="o" or lst[i + 1][0].lower() =="u":  # a + a,i,e,o,u -> an
                lst[i] = "an"

            elif (lst[i + 1][0] == "A" or lst[i + 1][0] == "E" or lst[i + 1][0] == "I" or lst[i + 1][0] == "O" or
                    lst[i + 1][0] == "U"):
                lst[i] = "an"

        if (lst[i] == "and" or lst[i] == "AND" or lst[i] == "aND" or lst[i] == "anD" or lst[i] == "AnD"\
                or lst[i] == "ANd") and lst[i-1][-1] != ",":  # add comma before and
            lst[i - 1] = lst[i - 1] + ","

        if i != (lst.__len__() - 1):
            if lst[i + 1] == lst[i]:
                del lst[i + 1]
        i += 1

    lst[0] = lst[0][0].upper() + lst[0][1:]

    newtext = ' '.join([str(item) for item in lst])
    new_txts = re.sub(r'(\([^()]*\))|[()]', lambda x: x.group(1) or "", newtext)
    print(new_txts)


grammarly(text)
