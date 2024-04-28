from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import WatchList,AuctionList

def AddToWatchList(request,product_id):
    product=AuctionList.objects.get(pk=product_id)
    user=request.user
    item=WatchList(product=product,watchlist=user)
    item.save()
    return HttpResponseRedirect(reverse("watch_list"))