from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import WatchList,AuctionList

def AddToWatchList(request,product_id):
    product=AuctionList.objects.get(pk=product_id)
    watchlist=request.user

    item=WatchList(product=product,watchlist=watchlist,quantity=1)
    item.objects.add(item)
    return HttpResponseRedirect(reverse("watch_list"))
    # if request.user.is_authenticated:
    #     product = AuctionList.objects.get(pk=product_id)

    #     # Handle potential exceptions (e.g., ObjectDoesNotExist)
    #     try:
    #         watchlist, created = WatchList.objects.get_or_create(user=request.user)
    #         watchlist.item.add(product)

    #         message = 'Successfully added to your watchlist!' if created else 'Already in your watchlist.'
    #         messages.success(request, message)  # Use Django's message framework
    #     except AuctionList.DoesNotExist:
    #         messages.warning(request, 'Product not found.')

    #     return redirect('watch_list')

    # else:
    #     messages.warning(request.user, 'You need to be logged in to add products to your watchlist.')
    #     return redirect('login')  # Redirect to login page if not authenticated