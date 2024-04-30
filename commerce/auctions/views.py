from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import AuctionList
from .forms import CreateListingForm

from .models import User



def index(request):
    return render(request, "auctions/index.html",{
        "objects":AuctionList.objects.all()
    })


def show_product_details(request,product_id):
    product_details=AuctionList.objects.get(pk=product_id)
    return render(request,"auctions/details.html",{
        "details":product_details
    })


def image(request,product_id):
    image_details=AuctionList.objects.get(pk=product_id)
    image_url=image_details.product_image.url
    name=image_details.product_name
    return render(request,"auctions/image.html",{
        "image":image_url,"name":name
    })


def Categories(request):
    return render(request,"auctions/index.html",{
        "tag":"Categories"
    })
    

def WatchList(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request,"auctions/index.html",{
        "tag":"Watch List"
    })


def CreateListing(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request,"auctions/index.html",{
        "tag":"Create Listing",
        "form": CreateListingForm()
    })


def AddCreateListing(request):
     if request.method=="POST":
        product_name=request.POST["product_name"]
        product_image=request.POST["product_image"]
        product_price=request.POST["product_price"]
        product_date_joined=request.POST["product_date_joined"]
        product_bid_closing_time=request.POST["product_bid_closing_time"]
        product_description=request.POST["product_description"]
        product_category=request.POST["product_category"]
        f=AuctionList(product_name=product_name,product_image=product_image,product_price=product_price,product_date_joined=product_date_joined,product_bid_closing_time=product_bid_closing_time,product_description=product_description,product_user_created=True,product_category=product_category)
        f.save()
        product=AuctionList.objects.get(pk=f.id)
        return HttpResponseRedirect(reverse('product_details',args=[product.id]))


def Comment(request,product_id):
    return 


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message":"Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
