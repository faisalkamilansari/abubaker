from django.urls import path


from . import views
from . import NewViews

urlpatterns = [
    path("", views.index, name="index"),
    # path("login", views.login_view, name="login"),
    # path("logout", views.logout_view, name="logout"),
    # path("register", views.register, name="register"),
    # path("<int:product_id>",views.show_product_details, name="product_details"),
    # path("/media/Images/<int:product_id>",views.image,name="image"),
    # path("categories",views.Categories,name="categories"),
    # path("watch_list",views.WatchList,name="watch_list"),
    # path("create_listing",views.CreateListing,name="create_listing"),
    # path("add_create_listing",views.AddCreateListing,name="add_create_listing"),
    # path("<int:product_id>",NewViews.AddToWatchList,name="add_to_watch_list"),
]


 