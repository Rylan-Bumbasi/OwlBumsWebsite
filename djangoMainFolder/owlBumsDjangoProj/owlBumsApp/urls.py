
from django.urls import path, include
#from .import views
from .views import HomeView, ReviewDetailView, CreateReviewView, UpdateReviewView, DeleteReviewView, CreateCategoryView, CategoryView, CategoryListView, LikeView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('review/<int:pk>', ReviewDetailView.as_view(), name='review-detail'),
    path('add_post/', CreateReviewView.as_view(), name='create-review' ),
    path('add_category/', CreateCategoryView.as_view(), name='create-category' ),
    path('review/edit/<int:pk>', UpdateReviewView.as_view(), name='update-review'),
    path('review/<int:pk>/delete', DeleteReviewView.as_view(), name='delete-review'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name ="like_review"),
]

