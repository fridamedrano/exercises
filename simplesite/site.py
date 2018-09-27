#!/usr/bin/env python
# -*- coding: UTF-8 -*-
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
#     site.py
import os
import webbrowser

from pagebot.publications.publication import Publication
from pagebot.constants import URL_JQUERY, URL_MEDIA
from pagebot.composer import Composer
from pagebot.typesetter import Typesetter
from pagebot.elements import *
from pagebot.conditions import *
from pagebot.toolbox.color import color, whiteColor, blackColor
from pagebot.toolbox.units import em, pt
from pagebot.elements.web.simplesite.siteelements import *

SITE_NAME = 'SimpleSite'

MD_PATH = 'content.md'
EXPORT_PATH = '_export/' + SITE_NAME

USE_SCSS = True

DO_PDF = 'Pdf' # Save as PDF representation of the site.
DO_FILE = 'File' # Generate website output in _export/SimpleSite and open browser on file index.html
DO_MAMP = 'Mamp' # Generate website in /Applications/Mamp/htdocs/SimpleSite and open a localhost
DO_GIT = 'Git' # Generate website and commit to git (so site is published in git docs folder.
EXPORT_TYPE = DO_FILE

blueColor = color(rgb='#2A8BB8')

headerBackgroundColor = color(1) #whiteColor
heroBackgroundColor = whiteColor
bannerBackgroundColor = color(0, 1, 0) #whiteColor
navigationBackgroundColor = blackColor
coloredSectionBackgroundColor = whiteColor
logoColor = blueColor
logoBackgroundColor = color(1, 1, 0)
coloredSectionColor = color(0.4)
footerBackgroundColor = color(1)
footerColor = blackColor
CurrentMenu = color(0, 0, 255)

siteDescription = [
    ('index', 'PageBot Responsive Home'),
    ('content', 'PageBot Responsive Content'),
    ('page3', 'PageBot Responsive Page 3'),
    ('page4', 'PageBot Responsive Page 4'),
    ('page5', 'PageBot Responsive Page 5'),
]
styles = dict(
    body=dict(
        fill=whiteColor,
        margin=em(0),
        padding=em(3),
        fontSize=pt(12),
        leading=em(1.4),
    ),
    br=dict(leading=em(1.4)
    ),
)


# class SecondSection(Element):
#     def __init__(self, **kwargs):
#         Element.__init__(self, **kwargs)
#         newTextBox('', parent=self, cssId='columns')

#     def build(self, view, path):
#         pass

#     def build_html(self, view, path):
#         b = self.context.b
#         b.comment('Start '+self.__class__.__name__)
#         b.section(cssId='section1', cssClass='clearFix')
#         b.div(cssClass='wrapper')
#         b.div(cssClass='row')

#         b.div(cssClass='grid_4')
#         self.deepFind('TextIntroduction').build_html(view, path)
#         b._div()
#         b.comment('End .grid_4')

#         b.div(cssClass="grid_8", cssId='vis')
#         self.deepFind('NextImage').build_html(view, path)
#         b._div()
#         b.comment('End .grid_8')

#         b._div() # end .row
#         b.comment('End .row')
#         b._div() # end .wrapper
#         b._section()
#         b.comment('End .wrapper')
#         b.comment('End '+self.__class__.__name__)


def makeNavigation(header, currentPage):
    navigation = Navigation(parent=header, fill=navigationBackgroundColor)
    # TODO: Build this automatic from the content of the pages table.
    menu = TopMenu(parent=navigation)
    menuItem1 = MenuItem(parent=menu, href='index.html', label='Home', current=currentPage=='index.html')
    menuItem2 = MenuItem(parent=menu, href='content.html', label='Section', current=currentPage=='content.html')
    menuItem3 = MenuItem(parent=menu, href='page3.html', label='About', current=currentPage=='page3.html')
    menuItem4 = MenuItem(parent=menu, href='page4.html', label='Contact', current=currentPage=='page4.html')
    
    return navigation

def makePages(doc, siteDescription):

    for pn, (name, title) in enumerate(siteDescription):
        pn += 1 # Page numbers start at 1
        page = doc[pn]
        page.name, page.title = name, title
        page.description = 'PageBot SimpleSite is a basic generated template for responsive web design'
        page.keyWords = 'PageBot Python Scripting Simple Demo Site Design Design Space'
        page.viewPort = 'width=device-width, initial-scale=1.0, user-scalable=yes'
        page.style = styles['body']

        currentPage = name + '.html'
        # Add neste content elements for this page.
        conditions = (Left2Left(), Float2Top(), Fit2Width())
        # comlpete header
        header = Header(parent=page, fill=headerBackgroundColor, conditions=conditions)
        banner = Banner(parent=header, fill=bannerBackgroundColor, conditions=conditions)
        logos = Logo(parent=banner, name=name, textFill=logoColor, fill=logoBackgroundColor,
            conditions=(Left2Left(), Float2Top()))
        navigation = makeNavigation(header, currentPage)
        #section = ColoredSection(parent=page ,fill=headerBackgroundColor)

        if pn == 1:
            #section for the 1st image slider
            #1st section content
            content = Content(parent=page, cssID='vis', conditions=(Fit2LeftSide()) )
            #content = SecondSection(parent=page, cssID='vis')
            #hero = Hero(parent=page, fontSize=em(1.1), fill=heroBackgroundColor) 
            #section for the 3 column layout
            #3rth section content repeat
            content = Content(parent=page)
            content = Content(parent=page, contentId='Content2') #  fill=(0.7, 0.7, 0.9)
            section = ColoredSection(parent=content, fill=coloredSectionBackgroundColor, cssClass='paddingcolor')

        elif pn == 2:
            hero = Hero(parent=page, fontSize=em(1.1), fill=heroBackgroundColor)    
            section = ColoredSection(parent=page, fill=coloredSectionBackgroundColor)
        elif pn == 3:
            hero = Hero(parent=page, fontSize=em(1.1), fill=heroBackgroundColor)    
            section = ColoredSection(parent=page, fill=coloredSectionBackgroundColor)
        elif pn == 4:
            content = Content(parent=page, cssID='vis', conditions=(Fit2LeftSide()) )
        elif pn == 5:
            content = Content(parent=page, conditions=(Fit2LeftSide()) )
        footer = Footer(parent=page, fill=footerBackgroundColor, textFill=footerColor)


def makeSite(siteDescription, styles, viewId):
    doc = Site(viewId=viewId, autoPages=len(siteDescription), styles=styles)
    view = doc.view
    view.resourcePaths = ('css','fonts','images','js')
    view.jsUrls = (URL_JQUERY, URL_MEDIA, 'js/d3.js', 'js/main.js')
    # SiteView will automatic generate css/style.scss.css from assumed css/style.scss
    if USE_SCSS:
        view.cssUrls = ('fonts/webfonts.css', 'css/normalize.css', 'css/style.scss.css')
    else:
        view.cssUrls = ('fonts/webfonts.css', 'css/normalize.css', 'css/style-org.css')

    # Make the all pages and elements of the site as empty containers
    makePages(doc, siteDescription)    
    # By default, the typesetter produces a single Galley with content and code blocks.
    
    t = Typesetter(doc.context)
    galley = t.typesetFile(MD_PATH)
    # Create a Composer for this document, then create pages and fill content. 
    composer = Composer(doc)
    # The composer executes the embedded Python code blocks that direct where context should go.
    # by the HtmlContext.
    composer.compose(galley)
    
    doc.solve() # Solve all layout and float conditions for pages and elements.

    return doc
    

if EXPORT_TYPE == DO_PDF: # PDF representation of the site
    doc = makeSite(siteDescription, styles=styles, viewId='Page')
    doc.export(EXPORT_PATH + '.pdf')

elif EXPORT_TYPE == DO_FILE:
    doc = makeSite(siteDescription, styles=styles, viewId='Site')
    siteView = doc.view
    siteView.useScss = USE_SCSS
    doc.export(EXPORT_PATH)
    #print('Site file path: %s' % EXPORT_PATH)
    os.system(u'/usr/bin/open "%s"' % ('%s/index.html' % EXPORT_PATH))

elif EXPORT_TYPE == DO_MAMP:
    # Internal CSS file may be switched off for development.
    doc = makeSite(siteDescription, styles=styles, viewId='Mamp')
    mampView.useScss = USE_SCSS
    mampView.resourcePaths = view.resourcePaths
    mampView.jsUrls = view.jsUrls
    mampView.cssUrls = view.cssUrls
    print('View.jsUrls: %s' % view.jsUrls)
    print('View.cssUrls: %s' % view.cssUrls)

    MAMP_PATH = '/Applications/MAMP/htdocs/' + SITE_NAME 
    print('Site path: %s' % MAMP_PATH)
    doc.export(MAMP_PATH)

    if not os.path.exists(MAMP_PATH):
        print('The local MAMP server application does not exist. Download and in stall from %s.' % view.MAMP_SHOP_URL)
        os.system(u'/usr/bin/open %s' % view.MAMP_SHOP_URL)
    else:
        #t.doc.export('_export/%s.pdf' % NAME, multiPages=True)
        os.system(u'/usr/bin/open "%s"' % mampView.getUrl(SITE_NAME))

elif EXPORT_TYPE == DO_GIT and False: # Not supported for SimpleSite, only one per repository?
    # Make sure outside always has the right generated CSS
    doc = makeSite(siteDescription, styles=styles, viewId='Git')
    doc.export(EXPORT_PATH)
    # Open the css file in the default editor of your local system.
    os.system('git pull; git add *;git commit -m "Updating website changes.";git pull; git push')
    os.system(u'/usr/bin/open "%s"' % view.getUrl(DOMAIN))

else: # No output view defined
    print('Set EXPORTTYPE to DO_FILE or DO_MAMP or DO_GIT')