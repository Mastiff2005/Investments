from django.shortcuts import render

def index(request):
    title = 'Финансовые рынки и инвестиции'
    body = 'Котировки основных индексов, валют и акций'
    context = {'title': title, 'body': body}
    return render(request, "index.html", context)