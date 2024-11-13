from django.shortcuts import render , redirect
from .forms import KeywordForm
from .models import Keyword , Trend
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import matplotlib.pyplot as plt
import io
import urllib, base64
# Create your views here.
def index(request):
    return render(request, 'trends/index.html')

def keyword(request):
    keywords = Keyword.objects.all()
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trends:keyword')
    else:
        form = KeywordForm()
    context = {
        'form': form,
        'keywords': keywords,
    }
    return render(request, 'trends/keyword.html', context)

def delete(request , pk):
    keywords = Keyword.objects.get(pk=pk)
    if request.method == 'POST':
        keywords.delete()
        return redirect('trends:keyword')
    return redirect('trends:index')




def get_google_data(keyword,sorted):
    if not sorted:
        url = f"https://www.google.com/search?q={keyword}"
    elif sorted:
        url = f"https://www.google.com/search?q={keyword}&tbs=qdr:{sorted}"
    # &tbs=qdr:m
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source 
    soup = BeautifulSoup(html, "html.parser")
    result_stats = soup.select_one("div#result-stats")


    if result_stats:
        # 텍스트에서 숫자만 추출
        result_text = result_stats.get_text()
        match = re.search(r'약 ([\d,]+)개', result_text)
        if match:
            return int(match.group(1).replace(',', ''))  # 숫자를 정수로 변환
    return None




def crawling(request):
    keywoods = Keyword.objects.all()

    for key_name in keywoods:
        stat = get_google_data(key_name.name,"")
        Trend.objects.get_or_create(name=key_name.name , result=stat , search_period="all")

    keywords = Trend.objects.all()
    context ={
        'keywords' : keywords,
    }
    return render(request, 'trends/crawling.html', context )





def clearTrend(request):
    Trend.objects.all().delete()
    return redirect('trends:keyword')




def crawling_histograms(request):
    trends = Trend.objects.all()

    # Extracting data for the graph
    names = [trend.name for trend in trends]
    results = [trend.result for trend in trends]

    fig, ax = plt.subplots()
    ax.bar(names, results, color='skyblue')
    ax.set_xlabel('Name')
    ax.set_ylabel('Result')
    ax.set_title('Trend Results')

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    
    # Encode image to base64 string
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
    
    # Send the graphic in the context
    context = {'graphic': graphic}
    return render(request, 'trends/crawling_histograms.html', context)


def crawling_advanced(request):
    keywoods = Keyword.objects.all()
    my_search_period = "y"
    for key_name in keywoods:
        stat = get_google_data(key_name.name,my_search_period)
        Trend.objects.get_or_create(name=key_name.name , result=stat , search_period=my_search_period)

    keywords = Trend.objects.all()
    names = [keyword.name for keyword in keywords]
    results = [keyword.result for keyword in keywords]
    fig, ax = plt.subplots()
    ax.bar(names, results, color='skyblue')
    ax.set_xlabel('Name')
    ax.set_ylabel('Result')
    ax.set_title('Trend Results')

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    
    # Encode image to base64 string
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
    
    # Send the graphic in the context
    context = {'graphic': graphic}
    return render(request, 'trends/crawling_histograms.html', context)

