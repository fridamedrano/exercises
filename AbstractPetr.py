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
# NEWW, H = pt(inch(9)), pt(inch(12)) # Document size
W, H = inch(9, 12) # Document size
PADDING = pt(mm(13))  # Page padding on all sides
G = mm(4) # 2 Pica gutter
PW = W - 2*PADDING # Usable padded page width
PH = H - 2*PADDING # Usable padded page height
CW = (PW - (G*2)) # Column width
CH = PH
# Hard coded grid, will be automatic in later examples.
GRIDX = ((CW, G), (CW, 0))
GRIDY = ((CH, 0),)

# Abstract Paragraph
text = """Roanne Adams launched RoAndCo in 2006 after being recognized as one of Print magazine’s “New Visual Artist (20 under 30).” In 2010, she was named one of the city’s most “outstanding up-and-coming design professionals” by T: The New York Times Style Magazine and she received an Art Director’s Club Young Guns 9 award in 2011. Roanne currently serves on the Board of Directors for AIGA’s New York Chapter. With her keen eye for style and a skill for visually embodying brands’ personalities, Roanne has earned the trust and respect of clients and collaborators alike.

Photography by James Chorous"""
font = findFont('Roboto')
style = dict(font=font, fontSize=16, leading=em(1.4), textFill=0, hyphenation=True)
t = context.newString(text, style=style)

# Title / Name
text2 = """Roanne Adams"""
text2 = text2.upper()
font2 = findFont('Druk Cond Super')
style2 = dict(font=font2, fontSize=222, leading=em(0.8), textFill=0, hyphenation=True)
t2 = context.newString(text2, style=style2)

# Create a new document with 1 page. Set overall size and padding.
doc = Document(w=W, h=H, padding=PADDING, gridX=GRIDX, gridY=GRIDY, context=context)
# Get the default page view of the document and set viewing parameters
view = doc.view
# Get the page
page = doc[1]

# New text box for the Title
newTextBox(t2, w=W, h=(PH/2), parent=page, xAlign=CENTER, conditions=(Left2Left(), Bottom2Bottom()))

# One column Page
# NEW: (No need to keep as variable). No need to define name, unless linking overflow to or export to CSS
# newTextBox(t, w=CW, name='c1', parent=page, conditions=[Left2Left(), Top2Top(), Fit2Height()])
newTextBox(t, w=CW, parent=page, conditions=[Left2Left(), Top2Top(), Fit2Height()])
# Solve the page/element conditions
doc.solve()

# Export the document to this PDF file.
doc.export('_export/Abstract.jpg')
