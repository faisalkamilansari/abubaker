from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
#) #%-> means I am nearly sure
#) #%&&-> means I am doubtful or wrong  

class User(AbstractUser):
    pass

class Category(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    def __str__(self):
        return f"{self.id} : {self.category_name}"    

class AuctionList(models.Model):
    CHOICES=[
        ("Mg","Magical"),
        ("Ec","Electronics"),
        ("Cl","Clothing"),
        ("Fs","Fashion"),
        ("Sp","Sports")
    ]
    product_name=models.CharField(max_length=64)
    product_image=models.ImageField(upload_to='Images/')
    product_price=models.DecimalField(max_digits=5,decimal_places=2)
    product_date_joined=models.DateTimeField()
    product_bid_closing_time=models.DateTimeField(default=None)
    product_description=models.CharField(max_length=100,default=None)
    product_user_created=models.BooleanField(default=False)
    product_quantity=models.SmallIntegerField(default=1)
    product_watchlisted_on=models.ManyToManyField(User,blank=True,name="watchlist")   ##
    product_category=models.CharField(max_length=3,choices=CHOICES)  #@


 
    def __str__(self):
        return f"({self.id} : [{self.product_name}] : {self.product_date_joined} : {self.product_bid_closing_time} : {self.product_price} : [User created :]{self.product_user_created})"    

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    user_profile_pic=models.ImageField(upload_to="ProfilePics/",blank=True,null=True)
    user_phone_number=models.CharField(max_length=15)
    
class WatchList(models.Model):
    watchlist=models.OneToOneField(User,on_delete=models.CASCADE,related_name="watchlist")
    product=models.ManyToManyField(AuctionList,blank=True,related_name="user_watchlist")
# For User

class Bids(models.Model):   
    auction=models.ForeignKey(AuctionList,on_delete=models.CASCADE,related_name="product")
    bidder=models.ManyToManyField(User,blank=True,related_name="bidder")
    bid_product_quantity=models.IntegerField(default=1)
    bid_price=models.DecimalField(max_digits=10,decimal_places=2)

    def clean(self):
        existing_bids = Bids.objects.filter(auction=self.auction, bidder__in=self.bidder.all()).exclude(pk=self.pk)
        if existing_bids.exists():
            raise ValidationError('A user can only have one bid per auction.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['auction', 'bidder'], name='unique_bid_per_user'),
    #     ]
    def __str__(self):
        return f"( {self.auction} : {self.bidder} : {self.bid_product_quantity} : {self.bid_price} )"


@receiver(post_save, sender=Bids)
def check_unique_bid(sender, instance, created, **kwargs):
    if created:
        auction = instance.auction
        bidder = instance.bidder
        existing_bid = Bids.objects.filter(auction=auction, bidder=bidder).exclude(pk=instance.pk).exists()
        if existing_bid:
            raise ValidationError('A user can only have one bid per auction.')




class WinningBid(models.Model):    
    winning_bidder=models.OneToOneField(User,on_delete=models.CASCADE,related_name="winning_bidder")
    winning_product=models.OneToOneField(AuctionList,on_delete=models.CASCADE,related_name="winning_product")
    winning_bid_price=models.DecimalField(max_digits=10,decimal_places=2)
    winning_bid_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"[ {self.winning_bidder} : {self.winning_product} : {self.winning_bid_price} : {self.winning_bid_time} ]"
    



