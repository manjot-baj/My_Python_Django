from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='62df77bec0cf4a1ebe659d1a84a2140d')
sources = newsapi.get_sources()

user_decision = input('Choose any one option what you want Query or Source : ')
if user_decision == 'Query':
    user_query = input('Enter Query : ')
    top_headlines_query = newsapi.get_top_headlines(q=user_query, page_size=10)
    if top_headlines_query == {'status': 'ok', 'totalResults': 0, 'articles': []}:
        print('Sorry the information related to this is not available')
    else:
        print(top_headlines_query)
elif user_decision == 'Source':
    user_source = input('Enter Source : ')
    try:
        top_headlines_source = newsapi.get_top_headlines(sources=user_source, page_size=10)
        print(top_headlines_source)
    except:
        print('Sorry the information related to this is not available')
else:
    print('Your entry is invalid')
