from db import get_products

def smart_search(query, category=None):
    query = query.lower()
    products = get_products()
    results = []
    for p in products:
        if query in p["name"].lower():
            if category and category != p["category"]:
                continue
            results.append(p)
    return results
