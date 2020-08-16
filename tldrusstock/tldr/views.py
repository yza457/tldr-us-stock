from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .stockData.getData import getStockData
from .sentiment.sentiment import getSentiment
import json
import time

# Create your views here.
@csrf_exempt
def submit(request):
  try:
    req = json.loads(request.body)
  except Exception:
    return JsonResponse({'error': 'Bad Request: {0}'.format(str(Exception))})
  # print(req['input'])
  # print(type(req['input']))
  
  comps = req['input'].split(",")
  # print(comps)
  # remove whitespace
  comps = [s.strip() for s in comps if s]
  # print(comps)

  # get stock name and price
  resInBytes = getStockData(comps)
  # print(resInBytes)
  res = json.loads(resInBytes.decode('utf-8').replace("'", '"'))

  # do sentiment analysis on valid stocks
  error = [ s['error'] for s in res]
  sentiment = getSentiment(comps, error)

  for i in range(len(res)):
    res[i]["positive"] = sentiment[i][0]
    res[i]["negative"] = sentiment[i][1]

  # print(res)

  return JsonResponse(res, safe=False)


  

  # res = []
  # for comp in comps:
  #   curr = {}
  #   curr['name'] = comp
  #   curr['ticker'] = "test"
  #   curr['price'] = 1
  #   curr['percent'] = 0.05
  #   curr['positive'] = 0.21
  #   curr['negative'] = 0.18
  #   res.append(curr)
  # res = [
  #   {
  #     'name' : 'Apple',
  #     'ticker' : 'aapl',
  #     'price' : 10.5,
  #     'change' : 0.05,
  #     'positive' : 0.01,
  #     'negative' : 0.02,
  #     'error' : False
  #   },
  #   {
  #     'name' : 'Tesla Motors',
  #     'ticker' : 'tsla',
  #     'price' : 20.5,
  #     'percent' : 0.07,
  #     'positive' : 0.01,
  #     'negative' : 0.02,
  #     'error' : True,
  #   },
  #   {
  #     'name' : 'Microsoft',
  #     'ticker' : 'msft',
  #     'price' : 20.5,
  #     'percent' : 0.07,
  #     'positive' : 0.01,
  #     'negative' : 0.02,
  #     'error' : False
  #   },
  #   {
  #     'name' : 'Apple',
  #     'ticker' : 'aapl',
  #     'price' : 10.5,
  #     'percent' : 0.05,
  #     'positive' : 0.01,
  #     'negative' : 0.02,
  #     'error' : False
  #   },
  #   {
  #     'name' : 'Tesla Motors',
  #     'ticker' : 'tsla',
  #     'price' : 20.5,
  #     'percent' : 0.07,
  #     'positive' : 0.01,
  #     'negative' : 0.02,
  #     'error' : True
  #   },
  #   {
  #     'name' : 'Microsoft',
  #     'ticker' : 'msft',
  #     'price' : 20.5,
  #     'percent' : 0.07,
  #     'positive' : 0.01,
  #     'negative' : 0.02,
  #     'error' : False
  #   },
  #   {
  #     'name' : 'Apple',
  #     'ticker' : 'aapl',
  #     'price' : 10.5,
  #     'percent' : 0.05,
  #     'positive' : 0.01,
  #     'negative' : 0.02,
  #     'error' : False
  #   },
  #   {
  #     'name' : 'Tesla Motors',
  #     'ticker' : 'tsla',
  #     'price' : 20.5,
  #     'percent' : 0.07,
  #     'positive' : 0.01,
  #     'negative' : 0.02,
  #     'error' : True
  #   },
  #   {
  #     'name' : 'Microsoft',
  #     'ticker' : 'msft',
  #     'price' : 20.5,
  #     'percent' : 0.07,
  #     'positive' : 0.01,
  #     'negative' : 0.02,
  #     'error' : False
  #   }
  # ]