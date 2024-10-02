import requests


def query_wikipedia(term, lang, limit=100):
    url = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        'action': 'query',
        'list': 'search',
        'srsearch': term,
        'srlimit': limit,
        'format': 'json'
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def get_page_sizes(pages, lang):
    page_sizes = []
    for page in pages:
        page_title = page['title']
        page_id = page['pageid']

        page_info_url = f"https://{lang}.wikipedia.org/w/api.php"
        page_info_params = {
            'action': 'query',
            'prop': 'pageprops',
            'pageids': page_id,
            'format': 'json'
        }
        page_info_response = requests.get(page_info_url, params=page_info_params)
        page_info_response.raise_for_status()
        page_info_data = page_info_response.json()

        page_size = len(page_info_data['query']['pages'][str(page_id)]['pageprops'])

        page_sizes.append({
            'title': page_title,
            'size': page_size,
            'language': lang
        })
    return page_sizes


def main():
    term = "絵文字"
    languages = ['en', 'ja']
    all_results = []

    for lang in languages:
        search_results = query_wikipedia(term, lang)
        page_sizes = get_page_sizes(search_results['query']['search'], lang)
        all_results.extend(page_sizes)

    sorted_results = sorted(all_results, key=lambda x: x['size'], reverse=True)

    for result in sorted_results[:20]:
        print(f"Title: {result['title']}, Size: {result['size']}, Language: {result['language']}")


if __name__ == "__main__":
    main()
