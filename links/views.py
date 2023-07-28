from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from .models import Link


from django.http import JsonResponse

def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        while True:
            shortened_url = get_random_string(length=6)
            if not Link.objects.filter(shortened_url=shortened_url).exists():
                break
        try:
            link = Link.objects.create(original_url=original_url, shortened_url=shortened_url)
            return JsonResponse({'original_url': link.original_url, 'shortened_url': link.shortened_url})
        except Exception as e:
            print(f"An error occurred: {e}")
            return JsonResponse({'error': 'An error occurred. Please try again later.'}, status=500)

    # Получаем все укороченные ссылки из базы данных и передаем их в контекст для вывода на странице.
    links = Link.objects.all()
    return render(request, 'links/form.html', {'links': links})