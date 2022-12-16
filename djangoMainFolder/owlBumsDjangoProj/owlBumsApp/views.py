from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Review, Category
from .forms import ReviewForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

#def home(request):
#    return render(request, 'home.html', {})

def LikeView(request, pk):
    review = get_object_or_404(Review, id=request.POST.get('review_id'))
    liked = False
    if review.likes.filter(id=request.user.id).exists():
        review.likes.remove(request.user)
        liked = False
    else: 
        review.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('review-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Review
    template_name = 'home.html' 
    ordering = ['review_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})

def CategoryView(request, cats):
    category_reviews = Review.objects.filter(category=cats.replace('-',' '))
    return render(request, 'categories.html', {'cats': cats, 'category_reviews': category_reviews})


class ReviewDetailView(DetailView): 
    model = Review
    template_name = 'review_details.html'
    def get_context_data(self, *args, **kwargs):
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Review, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class CreateReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'create_review.html'
   # fields = ('title','albumScore','body')

class CreateCategoryView(CreateView):
    model = Category
    # form_class = ReviewForm
    template_name = 'add_category.html'
    fields = '__all__'


class UpdateReviewView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'update_review.html'
   # fields = ['title', 'albumScore', 'body']

class DeleteReviewView(DeleteView):
    model = Review
    template_name = 'delete_review.html'
    success_url = reverse_lazy('home')

    
