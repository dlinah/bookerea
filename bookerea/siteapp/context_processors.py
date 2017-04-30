from .models import Category

def categories_context_processor(request):
    urls='/login/ /logout/ /register/ /signup/ '
    if request.path not in urls:
        cats=Category.objects.all()
        return {'categories':cats}
    return {}