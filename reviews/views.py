from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from reviews.models import Review

# Create your views here.

class AppDevClubReviewsView(APIView):
    def get(self, requests):
        reviews = []
        for review in Review.objects.filter():
            review_data = {'review_text': review.review_text,
                           'name': review.name,
                           'email': review.email,
                           'phone': review.phone,
                           }
            reviews.append(review_data)
        return Response({'reviews': reviews})
    
class CreateAppDevClubReview(APIView):
    def post(self, request):
        review = request.data.get('review_text', '')
        name = request.data.get('name', '')
        email = request.data.get('email', '')
        phone = request.data.get('phone', '')

        if review == '':
            return Response({'message': 'failure'})
        else:
            new_database_entry = Review(review_text=review, 
                                        name=name, 
                                        email=email, 
                                        phone=phone)
            new_database_entry.save()
            return Response({'message': 'success'})