from django.contrib.auth.models import AbstractUser
from django.db import models
#) #%-> means I am nearly sure
#) #%&&-> means I am doubtful or wrong  

class User(AbstractUser):
    pass


class AuctionList(models.Model):
    product_name=models.CharField(max_length=64)
    product_image=models.ImageField(upload_to='Images/')
    product_price=models.DecimalField(max_digits=5,decimal_places=2)
    product_date_joined=models.DateTimeField()
    product_bid_closing_time=models.DateTimeField(default=None)
    product_description=models.CharField(max_length=100,default=None)
    product_user_created=models.BooleanField(default=False)
    product_quantity=models.SmallIntegerField(default=1)
    product_watchlisted_on=models.ForeignKey(User,blank=True,on_delete=models.CASCADE,name="on_watchlists")
    product_category=models.CharField()


 
    def __str__(self):
        return f"({self.id} : [{self.product_name}] : {self.product_date_joined} : {self.product_bid_closing_time} : {self.product_price} : [User created :]{self.product_user_created})"
    

class Profile(models.Model):
    user_associated=models.OneToOneField(User,on_delete=models.CASCADE,related_name="user_associated")
    user_watchlist=models.ForeignKey(AuctionList,blank=True,on_delete=models.CASCADE,related_name="users_watchlist")
    user_profile_pic=models.ImageField(upload_to="ProfilePics/",blank=True,null=True,on_delete=models.CASCADE)
    user_phone_number=models.BigIntegerField(default="")
    

# For User
class Bids(models.Model):   
    auction=models.ForeignKey(AuctionList,on_delete=models.CASCADE,related_name="product")
    bidder=models.ManyToManyField(User,blank=True,related_name="bidder")
    bid_product_quantity=models.IntegerField(default=1)
    bid_price=models.DecimalField(max_digits=10,decimal_places=2)

    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['auction', 'bidder'], name='unique_bid_per_user'),
        ]
    def __str__(self):
        return f"( {self.auction} : {self.bidder} : {self.bid_product_quantity} : {self.bid_price} )"
    
class WinningBid(models.Model):    
    winning_bidder=models.OneToOneField(User,on_delete=models.CASCADE,related_name="winning_bidder")
    winning_product=models.OneToOneField(AuctionList,on_delete=models.CASCADE,related_name="winning_product")
    winning_bid_price=models.DecimalField(max_digits=10,decimal_places=2)
    winning_bid_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"[ {self.winning_bidder} : {self.winning_product} : {self.winning_bid_price} : {self.winning_bid_time} ]"
    



