import random

def compphrase(phrase, order):
    nphrase = ""
    n = 0
    for i in phrase:
        if i == "_":
            inp = order[n]
            n+=1
        else:
            inp = i
        nphrase = nphrase + inp
    return nphrase

def Order(order):
    ans_lst = []
    for word in order:
        ans = input(f"Enter a {word}: ")
        ans_lst.append(ans)
    return ans_lst

def One():
    order = ["Adjective","Noun","Plural Noun","Person in room female","Adjective","Article of clothing","Noun","A City","Plural Noun","Adjective","Part of body","Letter of Alphabet","Celebrity","Plural Noun","Adjective","A Place","Part of The Body","Adjective","Adjective","Verb","Plural Noun","Number"]
    ordering = Order(order)
    phrase = f"""\n
    There are many _ ways to choose a/an _ to read.\n
    First you could ask for recommendations from your friends and _.\n
    Just don't ask Aunt _-she only reads _ books with _-ripping goddesses on the cover.\n
    If your friends and family are no help, try checking out the _ Review in The _ Times.\n
    If the _ featured there are too _ for your taste, try something a little more low-_,\n
    like _: The _ Magazine, or _ Magazine. You could also choose a book the _-fashioned way.\n
    Head to your local library or _ and browse the shelves until something catches your _.\n
    Or, you could save yourself a whole lot of _ trouble and log on to www.bookish.com, the _\n
    new website to _ for books! With all the time you'll save not having to search for _, you can read _ more books!"""
    print(compphrase(phrase,ordering))

def Two():
    order = ["Noun","Person in Room","Verb","Part of body(Plural)","Adjective","Noun","Noun","Plural Noun","Type of Liquid","Adjective","Noun","Noun","Noun","Plural Noun","Person in Room(Female)","Noun","Part of body(Plural)"]
    ordering = Order(order)
    phrase = f"""\n
    It was Thanksgiving, and the scent of succulent roast _ wafted through my house.\n
    '_, it's time to _!' my mother called. I couldn't wait to get my _ on that _ Thanksgivingmeal.\n
    My family sat around the dining-room _. The table was laid out with every kind of _ imaginable.\n
    There was a basket of hot buttered _ and glasses of sparkling _. The _ turkey sat, steaming, next to a tureen of _ gravy.\n
    A bowl of ruby-red _ sauce, a sweet-_ casserole, and a dish of mashed _ tempted my taste buds Bud the dish I looked forward\n
    to most was Grandma _'s famous _ pie. Thanksgiving is my favourite holiday, _ down."""
    print(compphrase(phrase,ordering))

def Three():
    sorder = "Plural Noun,Adjective,Plural Noun,animals,Plural Noun, Adjective,Color,Adjective,Noun,Plural Noun,Adjective,Verb,Plural Noun, Verb-ed,Verb,Noun,Adjective"
    order = list(sorder.split(","))
    ordering = Order(order)
    phrase = f"""\n
    Unicorns aren't like other _; They're _. They look like _, with _ for feet and a _ mane of hair.\n
    But unicorns are _ and have a _ _ on their heads. Some _ don't believe unicorns are _ but I believe in them.\n
    I would love to _ a unicorn to faraway _. One thing I've always _ about is whether unicorns _ rainbows, or is their\n
    _ _ like any other animal's?
    """
    print(compphrase(phrase,ordering))


def Four():
    sorder = "Adjective,Adjective,type of bird,room in a house,verb(past tense),verb,relative's name,noun,a liquid,verb ending in -ing,part of body(plural),plural noun,verb ending in -ing,Noun"
    order = list(sorder.split(","))
    ordering = Order(order)
    phrase = f"""\n
    It was a _, cold November day. I woke up to the _ smell of _ roasting in the _ downstairs.\n
    I _ down the stairs to see if I could help _ the dinner. My mom said, "See if _ needs a fresh _." \n
    So I carried a tray of glasses full of _ into the _ room. When I got there, I couldn't believe my _!\n
    There were _ _ on the _!
    """
    print(compphrase(phrase,ordering))

madlibno = random.randint(1,4)
if madlibno == 1:
    One()
elif madlibno == 2:
    Two()
elif madlibno == 3:
    Three()
elif madlibno == 4:
    Four()
