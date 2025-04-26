from django.http import HttpResponse

def health_check(request):
    """
    Простая функция для проверки здоровья приложения.
    Railway использует это для определения, работает ли приложение.
    """
    return HttpResponse("OK")