from django.shortcuts import render

def menu_list(request):
    items = [
        {"name": "Burger", "category": "Main", "price": 120, "available": True},
        {"name": "Orange Juice", "category": "Drinks", "price": 45, "available": True},
        {"name": "Caesar Salad", "category": "Appetizer", "price": 75, "available": False},
        {"name": "Chocolate Cake", "category": "Dessert", "price": 60, "available": True},
        {"name": "Grilled Chicken", "category": "Main", "price": 150, "available": True},
    ]

    query = request.GET.get('q')
    category = request.GET.get('category')

    categories = list(set(item["category"] for item in items))
    categories.sort()

    if query:
        items = [i for i in items if query.lower() in i["name"].lower()]

    if category:
        items = [i for i in items if i["category"] == category]

    context = {
        'items': items,
        'categories': categories,
        'query': query,
        'current_category': category,
    }

    return render(request, 'list.html', context)