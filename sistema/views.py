from django.shortcuts import render

# Aqui irão ficar todas as views ( controladores ) ref ao app sistema
# A Funçaõ index informa o que vai acontecer 
def index(request):
    return render(
        request,
        'sistema/index.html',
    )


