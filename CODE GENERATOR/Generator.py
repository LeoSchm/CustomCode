from encrypt import *

HTML_FORMAT = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ENCRYPTION</title>
        <link rel="stylesheet" href="main.css">
    </head>
    <body>
    """
    

def encrypt(message):
    Info = []
    length = len(message)
    if length > 80:
        DisplayError("Your Message is too long. the Maximum is 80 Characters.")
        return
    length = TextToBinary(str(length))
    Info.insert(0, length)
    EncryptedMessage = TextToBinary(message)
    Info.append(EncryptedMessage)
    return Info

def DisplayInformation(List):
    TotalBits = len(List[0]) + len(List[1])
    RemaindingBits = 800 - TotalBits - 4
    output = HTML_FORMAT + '<div class="Frame">'
    for i in List[0]:
        if i == "0":
            output += '<div class="Tile Black"></div>'
        if i == "1": 
            output += '<div class="Tile White"></div>'
    
    for i in range(4):
        output += '<div class="Tile Black"></div>'

    for i in List[1]:
        if i == "0":
            output += '<div class="Tile Black"></div>'
        if i == "1": 
            output += '<div class="Tile White"></div>'
    
    for i in range(RemaindingBits):
        output += '<div class="Tile Black"></div>'
    
    output += """</div>
    </body>
    </html>"""

    f = open("WEB/Generator.html", "w")
    f.write(output)
    f.close()

        

def DisplayError(Message):
    f = open("Generator.html", "w")
    html_template = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <link rel="stylesheet" href="main.css">
    </head>
    <body>

        <p id="Label">{Message}</p>

    </body>
    </html>"""
    f.write(html_template)

    f.close()
