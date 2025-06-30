from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView,CreateView
from .models import Review


# class ReviewView(View):
#     def get(self,request):
#         form = ReviewForm()
#         return render(request,"reviews/review.html",{"form":form})
    
#     def post(self,request):
#         form=ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#         return render(request,"reviews/review.html",{"form":form})
    
    
class ReviewView(CreateView):
    model=Review
    form_class=ReviewForm
    template_name="reviews/review.html"
    success_url="/thank-you"

# class ThankYouView(View):
#     def get(self,request):
#         return render(request,'reviews/thank-you.html')

class ThankYouView(TemplateView):
    template_name='reviews/thank-you.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['message']='this works!'
        return context

# class ReviewsListView(TemplateView):
#     template_name="reviews/review_list.html"
#     def get_context_data(self, **kwargs):
#         context= super().get_context_data(**kwargs)
#         reviews=Review.objects.all()
#         context['reviews']=reviews
#         return context
    
class ReviewsListView(ListView):
    template_name="reviews/review_list.html"
    model=Review
    context_object_name='reviews'
    
    #loc du lieu
    
    # def get_queryset(self):
    #     base_querry= super().get_queryset()
    #     data = base_querry.filter(rating__gt=4)
    #     return data
    
 
   
# class SingleReviewView(TemplateView):
#     template_name='reviews/single_review.html'
#     def get_context_data(self, **kwargs):
#         context= super().get_context_data(**kwargs)
#         review_id=kwargs['id']
#         selected_review=Review.objects.get(pk=review_id)
#         context['review']=selected_review
#         return context
        

class SingleReviewView(DetailView):
    template_name='reviews/single_review.html'
    model=Review
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        loader_review=self.object
        request=self.request
        favorite_id=request.session.get('favorite_review')
        context['is_favorite']=favorite_id==str(loader_review.id)
        return context

class AddFavoriteView(View):
    def post(self,request):
        review_id=request.POST['review_id']
        print(review_id)
        request.session['favorite_review']=review_id
        return HttpResponseRedirect("/reviews/"+review_id)