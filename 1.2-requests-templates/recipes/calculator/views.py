from django.http import HttpResponse
from django.shortcuts import render

def recipes():
    DATA = {
        'omlet': {
            'яйца, шт': 2,
            'молоко, л': 0.1,
            'соль, ч.л.': 0.5,
        },
        'pasta': {
            'макароны, г': 0.3,
            'сыр, г': 0.05,
        },
        'buter': {
            'хлеб, ломтик': 1,
            'колбаса, ломтик': 1,
            'сыр, ломтик': 1,
            'помидор, ломтик': 1,
        },
    }
    return DATA

def omlet(request):
    data = recipes()
    recipe = data['omlet']
    servings = int(request.GET.get('servings', 1))
    for key, value in recipe.items():
        recipe[key] = value * servings
    context = {'recipe': recipe}
    return render(request, 'calculator/index.html', context)

def pasta(request):
    data = recipes()
    recipe = data['pasta']
    servings = int(request.GET.get('servings', 1))
    for key, value in recipe.items():
        recipe[key] = value * servings
    context = {'recipe': recipe}
    return render(request, 'calculator/index.html', context)

def buter(request):
    data = recipes()
    recipe = data['buter']
    servings = int(request.GET.get('servings', 1))
    for key, value in recipe.items():
        recipe[key] = value * servings
    context = {'recipe': recipe}
    return render(request, 'calculator/index.html', context)