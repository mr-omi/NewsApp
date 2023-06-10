from django.shortcuts import render
from newsapi import NewsApiClient


def index(response):
    if response.method == "POST":
        country = response.POST.get("country")
        newsapi = NewsApiClient(api_key='*****************')
        try:
            top_headlines = newsapi.get_top_headlines(language='en', country=country)
        except:
            error = "Invalid Country Code !! Please try again"
            return render(response, "newsapp/index.html", {"error": error})
        else:
            articles = top_headlines["articles"]
            title = []
            desc = []
            url = []
            img_url = []
            publishedAt = []
            for article in articles:
                title.append(article["title"])
                desc.append(article["description"])
                url.append(article["url"])
                img_url.append(article["urlToImage"])
                publishedAt.append(article["publishedAt"])

            data = zip(title, desc, url, img_url, publishedAt)
            print(data)
            return render(response, "newsapp/index.html", {"data": data})

    else:
        return render(response, "newsapp/index.html", {})
