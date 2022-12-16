import docx
import time

def parse_script(inputDoc):
    # inputDoc = input("Enter the announcements document to teleprompt (include the file extension '.docx'). >>")
    doc = docx.Document(inputDoc)

    paragraphs = doc.paragraphs
    content = ""
    for i in range(len(paragraphs)):
        for g in range(len(paragraphs[i].text)):
            if paragraphs[i].text[g] != "’" and paragraphs[i].text[g] != ":" and paragraphs[i].text[g] != "�":
                content+= paragraphs[i].text[g]

    word_splits = []
    dialogue = ""
    anchors = []
    flag = False
    tempDialogue = ""
    tempTag = ""
    for i in range(len(content)):
        if content[i] == "[":
            flag = True
            dialogue += tempDialogue
            tempDialogue = ""
        elif content[i] == "]":
            flag = False
            dialogue += " @ "
            anchors.append(tempTag)
            tempTag = ""
        if flag and content[i] != "[" and content[i] != "]":
            tempTag += content[i]
        elif content[i] != "[" and content[i] != "]":
            tempDialogue += content[i]
    dialogue += tempDialogue

    # print(dialogue)
    # print(anchors)

    anchorIndex = 0
    splitLogue = dialogue.split(" ")
    msg = ""
    for i in range(len(splitLogue)):
        if splitLogue[i] != "@" :
            msg += splitLogue[i] + " "
        if i%5==0 and i != 0:
            word_splits.append(msg)
            msg = ""
        if splitLogue[i] == "@":
            word_splits.append(msg)
            msg = ""
            if i != 0:
                word_splits.append(anchors[anchorIndex]+":")
            else:
                word_splits.append(anchors[anchorIndex]+":")
            anchorIndex+=1
        if i == len(splitLogue)-1:
            word_splits.append(msg)
            msg = ""


    f = open("WordFives.txt","w+")
    for i in range(len(word_splits)):
        f.write(word_splits[i]+"\n")
    f.close()

