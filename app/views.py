from collections import Counter
from django.http import HttpResponse

from django.shortcuts import render

class IncrementCounter:
    
    def __init__(self):
        self._value = 0
    
    def new_value(self):
        self._value += 1
        return self._value
    def print(self):
        return self._value


counter_show_original = IncrementCounter()
counter_show_test = IncrementCounter()
counter_click_original = IncrementCounter()
counter_click_test = IncrementCounter()



def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    conversion = request.GET['from-landing']
    if conversion == 'original':
        counter_click_original.new_value()
    elif conversion == 'test':
        counter_click_test.new_value()
    return render(request,'index.html')


def landing(request):
    ab = request.GET['ab-test']
    if ab== 'original':
        page = 'landing.html'
        counter_show_original.new_value()
    elif ab == 'test':
        page = 'landing_alternate.html'
        counter_show_test.new_value()

    return render(request,page)


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    if counter_click_test.print() != 0 and counter_show_test.print() != 0:
        test =  round((counter_click_test.print()  / counter_show_test.print()) * 100, 1)
    else:
        test = 'Мало данных для расчета'
    if counter_click_original.print() != 0 and counter_show_original.print() != 0:
        original =  round((counter_click_original.print()  / counter_show_original.print()) * 100, 1)
    else:
        original = 'Мало данных для расчета'
    return render(request,'stats.html', context={
        'test_conversion': f'{test} %',
        'original_conversion': f'{original} %',
    })
