from django.contrib import admin
from .models import User,AuctionList,Bids,WinningBid,WatchList
# Register your models here.

class AuctionListStyle(admin.ModelAdmin):
    list_display=('product_name','product_image','product_price','product_date_joined')    
admin.site.register(User)
admin.site.register(AuctionList,AuctionListStyle)
admin.site.register(Bids)
admin.site.register(WinningBid)
admin.site.register(WatchList)

