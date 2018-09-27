# -----------------------------------------------------------------------------
#
#     P A G E B O T
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     010_DoubleColumnOverflow.py
#
#     Draw a two columns with a single text, showing overflow from one column
#     into the other. Use some view.showGridBackground options to show the grid.
#     Use view.showTextBoxBaselines = True to show the baselines of the text.

#from pagebot.contexts.flatcontext import FlatContext
from pagebot.contexts.platform import getContext

from pagebot.fonttoolbox.objects.font import findFont
from pagebot.document import Document
from pagebot.elements import * # Import all types of page-child elements for convenience
from pagebot.toolbox.color import color
from pagebot.toolbox.units import em, p, pt, mm, inch
from pagebot.style import CENTER
from pagebot.toolbox.color import blueColor, darkGrayColor, redColor, Color, noColor, color
from pagebot.conditions import * # Import all conditions for convenience.
from pagebot.constants import GRID_COL, GRID_ROW, GRID_SQR

#context = FlatContext()
context = getContext()

W, H = pt(inch(9)), pt(inch(12)) # Document size
PADDING = pt(mm(13))  # Page padding on all sides
G = mm(4) # 2 Pica gutter
PW = W - 2*PADDING # Usable padded page width
PH = H - 2*PADDING # Usable padded page height
CW = (PW - (G*2))/3 # Column width
CH = PH
# Hard coded grid, will be automatic in later examples.
GRIDX = ((CW, G), (CW, 0))
GRIDY = ((CH, 0),)


text = """the moment when I realized that people were actually looking at my website. People thought I was good at what I did, and they were pushing me to do more of it. I began doing more freelance projects on the side, and that’s what eventually motivated me to freelance full-time.

Going freelance and deciding to start your own studio are pretty big risks. Have you taken any other risks to move forward? 
I’ve taken a lot of risks, but I haven’t done anything so bold as risking my life or anything! If you have an appetite for it, take big risks when you’re young and have less responsibility—and before you have kids. Risk-taking is a good thing, but it does evolve into more risks. The longer I run my studio and the larger it grows, the risk of something going wrong or falling apart becomes greater. But your threshold for those scenarios becomes greater over the years.

Earlier you mentioned talking to your mom about going out on your own. Have your family and friends been supportive of what you do? 
My mom’s a worrywart and she’s instilled that trait in me, too. When she told me, “I’m worried about you quitting your job. It’s crazy,” I reminded her that she said the same thing when I decided to move to New York and when I wanted to go to Parsons. She would joke about those decisions and try to offer a more practical route. I had to take everything she said with a grain of salt and believe in myself. If you think you can do something, go for it. I’ve always imagined myself in a role like this. I don’t know what my exact vision was, but I saw myself living in New York City and being successful in whatever creative industry I chose. I wanted that for myself, and I was willing to work hard and do whatever it took to make it happen. 
Now that everything has worked out, my mom doesn’t question my decisions or tell me I’m crazy anymore. (laughing) It’s nice, and I’m proud of that. At the end of the day, that’s what you want from your parents: you want them to trust you and your instincts and the decisions you make.

Parents want us to live an amazing, safe life. But if you want to do anything worthwhile, there’s a little risk involved. You just have to chase that, and hopefully the people around you will be supportive. 
Exactly. I do have supportive people in my life, and I’m incredibly thankful for that. My husband has been a huge supporter of mine since I was 16. My family, his family, and all of our siblings have been equally supportive. Everyone who has worked at RoAndCo has also helped to push me along and make decisions that I never would have made on my own.

They’re looking to you to lead. 
Yeah! They’re not only looking to me, but some of them are also helping me lead and telling me what we should do and what the next step is. Sometimes I’m risk-averse or not ready to move on, but they’re there to say, “No, you’re ready. Let’s do it!”

Do you feel a responsibility to contribute to something bigger than yourself, or outside of yourself? 
Definitely. As I’ve gotten older, I’ve embraced that I’m part of a larger graphic design community, and I get satisfaction from being involved in it. I’m on the board of directors for the AIGA/NY chapter and it’s amazing to sit around a table with other designers and business owners who’ve experienced similar challenges, successes, and situations. I’m so excited to be a part of that. Aside from serving on the board, I also like giving back to the community by hosting events and moderating panels with other designers.
With age and perspective—and since having my daughter—I’ve grown to look at the world differently. My very selfish world has been turned on its head. I no longer think about my personal achievements. Instead, I think about the success of my business and the employees who work at RoAndCo. I’m working on helping them evolve as individuals and grow into their roles, beyond their initial expectations. That has been a wonderful experience.

What have you learned over the years that you would want to share with your younger self? There’s a lot of advice I would give to my younger self. Thinking about it now, I should have taken stock and appreciated what I had along the way. I was constantly concerned with wanting more. I had an inherent determination to keep going forward, to keep trying to succeed and quickly move on. I didn’t take a step back to think, “I’m so grateful for what I currently have.” I also didn’t take the time to thank the people who helped me as often as I should have. I guess we take a lot for granted when we’re young."""


font = findFont('Georgia')
style = dict(font=font, fontSize=9.4, leading=em(1.4), textFill=0.2, hyphenation=True)
t = context.newString(text, style=style)

# Quote Style
text2 = """I want to be a good role model for her. It’s important that she can look back at what I’ve done and feel empowered to do whatever she wants to do. I want my daughter to dream big and achieve each and every goal. """
text2 = text2.upper()
font2 = findFont('Druk Medium')
style2 = dict(font=font2, fontSize=23, leading=em(1), textFill=0.3, hyphenation=True)
t2 = context.newString(text2, style=style2)

# Create a new document with 1 page. Set overall size and padding.
doc = Document(w=W, h=H, padding=PADDING, gridX=GRIDX, gridY=GRIDY, context=context)
# Get the default page view of the document and set viewing parameters
view = doc.view
# Get the page
page = doc[1]

# Background color rectangle
newRect(w=W/5, h=H, stroke=noColor, parent=doc[1], xAlign=CENTER, conditions=(Center2Center(), Right2Right()), fill=(253/255,239/255,239/255))

# Vertical Lines in between the paragraphs
lineh = 35
linew = 0
parah = PH
strokew = 0.5
strokec = (0, 0, 0,0.5)
newLine(x=30, y=lineh, w=linew, h=parah, stroke=strokec, strokeWidth=strokew, parent=page)
newLine(x=225, y=lineh, w=linew, h=parah, stroke=strokec, strokeWidth=strokew, parent=page)
newLine(x=422, y=lineh, w=linew, h=parah, stroke=strokec, strokeWidth=strokew, parent=page)

# Text Box for the Quote style
newTextBox(t2, w=W/4, h=H/3, parent=page, xAlign=CENTER, conditions=(Right2Right(), Middle2Middle()))
# Lines for Quote 
linew2= PW/10
linep= w=PW-125
newLine(x=linep, y=265, w=linew2, h=linew, stroke=(0, 0, 0,0.5), strokeWidth=3, parent=page)
newLine(x=linep, y=525, w=linew2, h=linew, stroke=(0, 0, 0,0.5), strokeWidth=3, parent=page)

# Make text box as child element of the page and set its layout conditions
# to fit the padding of the page and the condition that checks on text overflow.
c1 = newTextBox(t, w=CW, name='c1', parent=page, nextElementName='c2', conditions=[Left2Left(), Top2Top(), Fit2Height(), Overflow2Next()])
# Text without initial content, will be filled by overflow of c1.
c2 = newTextBox(w=CW, name='c2', parent=page, conditions=[Center2Center(), Top2Top(), Fit2Height()])

# Solve the page/element conditions
doc.solve()

# Export the document to this PDF file.
doc.export('_export/Article.jpg')

