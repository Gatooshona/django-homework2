from django.shortcuts import render

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


def dish(request):
    dish_name = request.path.replace('/', '')
    servings = int(request.GET.get('servings', 1))

    def get_servings(name, persons=1):
        serve_dish = {}

        for ingredient, amount in DATA[name].items():
            serve_dish[ingredient] = round(amount * persons, 2)

        return serve_dish

    context = {
      'recipe': {
        'servings': servings,
        'ingredients': get_servings(dish_name, servings)
      }
    }
    return render(request, 'calculator/index.html', context)
