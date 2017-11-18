from django.shortcuts import render

# Create your views here.
def post_list(request):
    zmones = [{'vardas': 'tadas', 'amzius': 26}, {'vardas': 'mindaugas', 'amzius': 40}, {'vardas': 'gedas', 'amzius': 19}]
    return render(request, 'blog/post_list.html', {'zmones': zmones})
