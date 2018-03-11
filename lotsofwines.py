from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category, Wine

engine = create_engine('sqlite:///winelistwithusers.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create dummy user
User1 = User(username="wineMaker", email="wine@maker.co",
             picture="/static/blankUser.jpg")
session.add(User1)
session.commit()

# List for White wines
category1 = Category(user_id=1, name="White wines", description="""White wine 
    is a wine whose colour can be straw-yellow, yellow-green, or yellow-gold. 
    It is produced by the alcoholic fermentation of the non-coloured pulp of 
    grapes, which may have a skin of any colour. White wine has existed for at
     least 2500 years. The wide variety of white wines comes from the large 
     number of varieties, methods of winemaking, and ratios of residual sugar. 
     White wine is mainly from "white" grapes, which are green or yellow in 
     colour, such as the Chardonnay, Sauvignon, and Riesling. Some white wine
      is also made from grapes with coloured skin, provided that the obtained 
      wort is not stained. Pinot noir, for example, is commonly used to 
      produce champagne.""")

session.add(category1)
session.commit()

wineItem1 = Wine(user_id=1, name="2013 Chardonnay Stainless", origin= "Central Coast - USA",
    description="""(aged 4 months in stainless steel) is crisp and clean, with lively
     green herbs, citrus blossom and hints of saltiness all emerging from the glass. 
     Its medium-bodied and balanced, and although slightly straightforward, is certainly a delicious drink. 
     Enjoy bottles over the coming handful of years. Coming from the Edna Valley and leaning heavily toward the fresher, 
     elegant and lightly textured end of the spectrum, these are all noteworthy wines from Chamisal Vineyards.""",
     price="$60", category=category1)

session.add(wineItem1)
session.commit()

wineItem2 = Wine(user_id=1, name="2013 Sauvignon Blanc", origin= "Marlborough - New Zealand",
    description=""" aromas of lime leaves, lemon juice, 
    gooseberries and fresh thyme with underlying mown grass hints. Light-bodied, 
    it's a little dilute in the mid-palate with vague herbal notes and a clipped, tart finish.""",
                     price="$60", category=category1)

session.add(wineItem2)
session.commit()

wineItem3 = Wine(user_id=1, name="Vignes de la Garenne", origin="Bordeaux AOC - France",
    description=""" WHITE - RICH - Buttery vanilla honey wood creamy rounds""",
                     price="$60", category=category1)

session.add(wineItem3)
session.commit()

# List for Red wines
category2 = Category(user_id=1, name="Red wines", description="""Red wine is a 
    type of wine made from dark-colored (black) grape varieties. The actual 
    color of the wine can range from intense violet, typical of young wines, 
    through to brick red for mature wines and brown for older red wines. The 
    juice from most purple grapes is greenish-white; the red color comes from 
    anthocyan pigments (also called anthocyanins) present in the skin of the 
    grape; exceptions are the relatively uncommon teinturier varieties, which 
    produce a red colored juice. Much of the red-wine production process 
    therefore involves extraction of color and flavor components from the grape 
    skin.""")

session.add(category2)
session.commit()

wineItem1 = Wine(user_id=1, name="2013 Shiraz", origin="McLaren Vale - Australia", 
    description="""Deep garnet colored, the 2013 Shiraz has notes of baked blueberries, 
    blackcurrant cordial and dried Provence herbs with a aniseed and black earth undercurrent. 
    Soft, rounded and open-for-business, it delivers plenty of fruit and spice with good length.""",
                     price="$58", category=category2)

session.add(wineItem1)
session.commit()

wineItem2 = Wine(user_id=1, name="2011 Merlot Napa", origin="Napa Valley - USA", 
    description="""blend of 82.2% Merlot and the rest Cabernet Sauvignon, Petit Verdot 
    and Cabernet Franc aged 14 months in 25% new oak. A solid, competent effort 
    for the vintage, it offers up notes of herbs, white chocolate, espresso, clove 
    and sweet cherries. Medium-bodied and somewhat short, it needs to be drunk over 
    the next 4-6 years.""",
                     price="$70", category=category2)

session.add(wineItem2)
session.commit()

# List for Rose wines
category3 = Category(user_id=1, name="Rose wines", description="""A rose (
    from French rose; also known as rosado in Portugal and Spanish-speaking 
    countries and rosato in Italy) is a type of wine that incorporates some 
    of the color from the grape skins, but not enough to qualify it as a red 
    wine. It may be the oldest known type of wine, as it is the most 
    straightforward to make with the skin contact method. The pink color can 
    range from a pale "onion-skin" orange to a vivid near-purple, depending 
    on the varietals used and winemaking techniques. There are three major 
    ways to produce rose wine: skin contact, saignee, and blending. Rose wines 
    can be made still, semi-sparkling or sparkling and with a wide range of 
    sweetness levels from highly dry Provencal rose to sweet White Zinfandels 
    and blushes. Rose wines are made from a wide variety of grapes and can be 
    found all around the globe.""")

session.add(category3)
session.commit()

wineItem1 = Wine(user_id=1, name="Champagne Veuve Clicquot", 
    origin="Champagne AOC - France", description="""The rich, salmon-colored 
    NV Brut Rose (base 2012 with a dosage of nine grams) was launched ten 
    years ago for the first time. Based on the Yellow Label cuvee, but 
    colored with red wine, the newest edition offers intense and ripe red 
    fruit aromas on the clear nose. Fresh, elegant and finesse-full on the 
    palate, this is a warm and lush character with ripe cherry flavors, fine 
    tannins, some leather aromas and a serious finish. This is a serious 
    expression of easy-drinking Pinot Noir.""", price="$80", 
    category=category3)

session.add(wineItem1)
session.commit()

print "added wine items!"

