import interactions
from interactions.ext.paginator import Page, Paginator

import requests
from decouple import config
import datetime

URL = "https://openlibrary.org/"
TOKEN = config("TOKEN")

bot = interactions.Client(token=TOKEN, presence=interactions.ClientPresence(
        status=interactions.StatusType.IDLE,
        activities=[
            interactions.PresenceActivity(name="you vibing", type=interactions.PresenceActivityType.WATCHING)
        ]
    ))

print("Bot is on.")


@bot.command(name="search", description="Searches query", scope=905301278647783424)
@interactions.option("query")
@interactions.option(choices=[interactions.Choice(name="query", value="q"), interactions.Choice(name="title", value="title"), interactions.Choice(name="author", value="author")])
async def search_command(ctx: interactions.CommandContext, query: str, choice: str):
    await ctx.defer()
    response = requests.get(URL + "search.json?" + choice + "=" + query.replace(" ", "+")).json()

    book = requests.get(URL + response["docs"][0]["key"] + ".json").json()

    authors = []
    for i in book["authors"]:
        try:
            author = requests.get(URL + i["author"]["key"] + ".json").json()
            authors.append(author["name"])
        except:
            pass


    if choice == "q":
        embed1 = interactions.Embed(
            title="Search results",
            fields=[
                interactions.EmbedField(
                    name=book["title"],
                    value=", ".join(authors)
                ),
                interactions.EmbedField(
                    name="More info",
                    value="""If this is a book, search with the book tag. If author, search with author tag.
                    `/search book_title title` or `/search author_name author`"""
                )
            ],
            timestamp=datetime.datetime.utcnow()
        ).set_footer("https://openlibrary.org")
        await ctx.send(embeds=embed1)

    elif choice == "title":
        try:
            description = book["description"]
        except:
            description = "None"
        embed1 = interactions.Embed(
            title="Search results",
            fields=[
                interactions.EmbedField(
                    name=book["title"],
                    value=", ".join(authors)
                ),
                interactions.EmbedField(
                    name="Description",
                    value=description
                )
            ],
            timestamp=datetime.datetime.utcnow()
        ).set_footer("https://openlibrary.org").set_image(
            url="https://covers.openlibrary.org/b/id/" + str(book["covers"][0]) + "-L.jpg")
        try:
            subjects = book["subjects"]
        except:
            subjects = "None"
        embed2 = interactions.Embed(
            title="Search results",
            fields=[
                interactions.EmbedField(
                    name="Subjects",
                    value=", ".join(subjects)
                )
            ],
            timestamp=datetime.datetime.utcnow()
        ).set_footer("https://openlibrary.org")
        try:
            people = book["subject_people"]
        except:
            people = "None"
        embed3 = interactions.Embed(
            title="Search results",
            fields=[
                interactions.EmbedField(
                    name="People",
                    value=", ".join(people)
                )
            ],
            timestamp=datetime.datetime.utcnow()
        ).set_footer("https://openlibrary.org")
        embed4 = interactions.Embed(
            title="Search results",
            fields=[
                interactions.EmbedField(
                    name="More info",
                    value=f"""ID : {book['key'].split("/")[-1]}
                    Book link: https://openlibrary.org/works/{book['key']}
                    Website revisions: {str(book["revision"])}
                    """
                )
            ],
            timestamp=datetime.datetime.utcnow()
        ).set_footer("https://openlibrary.org")

        await Paginator(
            client=bot,
            ctx=ctx,
            pages=[
                Page("", title="Main", embeds=embed1),
                Page("", title="Subjects", embeds=embed2),
                Page("", title="People", embeds=embed3),
                Page("", title="More info", embeds=embed4),
            ],
        ).run()

    elif choice == "author":
        authorID = requests.get(URL + "search/authors.json?q=" + query.replace(" ", "+")).json()["docs"][0]["key"]
        author = requests.get(URL + "/authors/" + authorID + ".json").json()

        try:
            deathdate = author["death_date"]
        except:
            deathdate = "Present"
        try:
            birthdate = author["birth_date"]
        except:
            birthdate = "Unknown"
            deathdate = "Unknown"
        embed1 = interactions.Embed(
            title="Search results",
            fields=[
                interactions.EmbedField(
                    name=author["name"],
                    value=f"{birthdate} - {deathdate}"
                )
            ],
            timestamp=datetime.datetime.utcnow()
        ).set_footer("https://openlibrary.org")
        try:
            bio = author["bio"]["value"]
        except:
            try:
                bio = author["bio"]
            except:
                bio = "None"
        embed2 = interactions.Embed(
            title="Search results",
            fields=[
                interactions.EmbedField(
                    name="Biography",
                    value=bio
                )
            ],
            timestamp=datetime.datetime.utcnow()
        ).set_footer("https://openlibrary.org")
        embed3 = interactions.Embed(
            title="Search results",
            fields=[
                interactions.EmbedField(
                    name="More info",
                    value=f"""ISBN : {authorID}
                    Author link: https://openlibrary.org/authors/{authorID}
                    Website revisions: {str(author["revision"])}
                    """
                )
            ],
            timestamp=datetime.datetime.utcnow()
        ).set_footer("https://openlibrary.org")

        await Paginator(
            client=bot,
            ctx=ctx,
            pages=[
                Page("", title="Main", embeds=embed1),
                Page("", title="Biography", embeds=embed2),
                Page("", title="More info", embeds=embed3),
            ],
        ).run()


@bot.command(name="book", description="Searches information about a book", scope=905301278647783424)
@interactions.option("id")
async def book_command(ctx: interactions.CommandContext, book_id: str):
    await ctx.defer()
    book = requests.get(URL + "works/" + book_id + ".json").json()
    rating = requests.get(URL + "works/" + book_id + "/ratings.json").json()
    bookshelves = requests.get(URL + "works/" + book_id + "/bookshelves.json").json()

    authors = []
    for i in book["authors"]:
        try:
            author = requests.get(URL + i["author"]["key"] + ".json").json()
            authors.append(author["name"])
        except:
            pass

    try:
        description = book["description"]
    except:
        description = "None"
    embed1 = interactions.Embed(
        title="Search results",
        fields=[
            interactions.EmbedField(
                name=book["title"],
                value=", ".join(authors)
            ),
            interactions.EmbedField(
                name="Description",
                value=description
            )
        ],
        timestamp=datetime.datetime.utcnow()
    ).set_footer("https://openlibrary.org").set_image(
        url="https://covers.openlibrary.org/b/id/" + str(book["covers"][0]) + "-L.jpg")
    try:
        subjects = book["subjects"]
    except:
        subjects = "None"
    embed2 = interactions.Embed(
        title="Search results",
        fields=[
            interactions.EmbedField(
                name="Subjects",
                value=", ".join(subjects)
            )
        ],
        timestamp=datetime.datetime.utcnow()
    ).set_footer("https://openlibrary.org")
    try:
        people = book["subject_people"]
    except:
        people = "None"
    embed3 = interactions.Embed(
        title="Search results",
        fields=[
            interactions.EmbedField(
                name="People",
                value=", ".join(people)
            )
        ],
        timestamp=datetime.datetime.utcnow()
    ).set_footer("https://openlibrary.org")
    embed4 = interactions.Embed(
        title="Search results",
        fields=[
            interactions.EmbedField(
                name="Ratings",
                value=f"""Average: {rating['summary']['average']}
                Count: {rating['summary']['count']}"""
            )
        ],
        timestamp=datetime.datetime.utcnow()
    ).set_footer("https://openlibrary.org")
    embed5 = interactions.Embed(
        title="Search results",
        fields=[
            interactions.EmbedField(
                name="More info",
                value=f"""Want to read: {str(bookshelves['counts']['want_to_read'])}
                Currently reading: {str(bookshelves['counts']['currently_reading'])}
                Already read: {str(bookshelves['counts']['already_read'])}
                Book link: https://openlibrary.org/works/{book['key']}
                Website revisions: {str(book["revision"])}
                """
            )
        ],
        timestamp=datetime.datetime.utcnow()
    ).set_footer("https://openlibrary.org")

    await Paginator(
        client=bot,
        ctx=ctx,
        pages=[
            Page("", title="Main", embeds=embed1),
            Page("", title="Subjects", embeds=embed2),
            Page("", title="People", embeds=embed3),
            Page("", title="Ratings", embeds=embed4),
            Page("", title="More info", embeds=embed5),
        ],
    ).run()


@bot.command(name="author", description="Searches information about an author", scope=905301278647783424)
@interactions.option("id")
async def author_command(ctx: interactions.CommandContext, author_id: str):
    await ctx.defer()
    author = requests.get(URL + "/authors/" + author_id + ".json").json()

    try:
        deathdate = author["death_date"]
    except:
        deathdate = "Present"
    try:
        birthdate = author["birth_date"]
    except:
        birthdate = "Unknown"
        deathdate = "Unknown"
    embed1 = interactions.Embed(
        title="Search results",
        fields=[
            interactions.EmbedField(
                name=author["name"],
                value=f"{birthdate} - {deathdate}"
            )
        ],
        timestamp=datetime.datetime.utcnow()
    ).set_footer("https://openlibrary.org")
    try:
        bio = author["bio"]["value"]
    except:
        try:
            bio = author["bio"]
        except:
            bio = "None"
    embed2 = interactions.Embed(
        title="Search results",
        fields=[
            interactions.EmbedField(
                name="Biography",
                value=bio
            )
        ],
        timestamp=datetime.datetime.utcnow()
    ).set_footer("https://openlibrary.org")
    embed3 = interactions.Embed(
        title="Search results",
        fields=[
            interactions.EmbedField(
                name="More info",
                value=f"""ID : {author_id}
                        Author link: https://openlibrary.org/authors/{author_id}
                        Website revisions: {str(author["revision"])}
                        """
            )
        ],
        timestamp=datetime.datetime.utcnow()
    ).set_footer("https://openlibrary.org")

    await Paginator(
        client=bot,
        ctx=ctx,
        pages=[
            Page("", title="Main", embeds=embed1),
            Page("", title="Biography", embeds=embed2),
            Page("", title="More info", embeds=embed3),
        ],
    ).run()

bot.start()
