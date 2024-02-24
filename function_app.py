import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

data = {

    "books": [

        {
            "title":"12 Rules of Life",
            "Author": "Jordan Peterson",
            "year": 2018,
            "category": "Self-help",
            "bookcoverUrl":"https://myblob.com/12rulesoflife.jpg"
        },

        {
            "title":"The Invisible Man",
            "Author": "H. G. Wells",
            "year": 1988,
            "category": "Mystery",
            "bookcoverUrl":"https://myblob.com/theinvisibleman.jpg"
        },

        {
            "title":"Harry Potter and the Philosopher's Stone",
            "Author": "J. K. Rowling",
            "year": 1998,
            "category": "fantasy",
            "bookcoverUrl":"https://myblob.com/harrypotter.jpg"
        },

        {
            "title":"We who Wrestle with god",
            "Author": "Jordan Peterson",
            "year": 2018,
            "category": "Self-help",
            "bookcoverUrl":"https://myblob.com/12rulesoflife.jpg"
        }

    ]

}

@app.route(route="allbooks")
def all_books(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python all_books HTTPtrigger function processed a request.')

    return func.HttpResponse(json.dumps(data,indent=True),
                             mimetype="application/json",
                             status_code=200)

@app.route(route="getbooksbyyear/{year}")
def getbooksbyyear(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getbooksbyyear HTTPtrigger function processed a request.')

    year = req.route_params.get('year')

    filtered_books = []

    for book in data['books']:
        if book['year'] == int(year):
            filtered_books.append(book)

    return func.HttpResponse(json.dumps(filtered_books,indent=True),
                            mimetype="application/json",
                            status_code=200)
    #return func.HttpResponse(books_json)



