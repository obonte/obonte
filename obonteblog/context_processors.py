from . models import Category

def category(request):
    categorys = Category.objects.all().order_by('-created')

    return {
        'categorys':categorys
    }
