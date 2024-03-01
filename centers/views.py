from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CenterReviewSerializer,CenterSerializer
from .models import CenterReview , Center
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class CenterReviewDetailUpdateDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        center_reviews = CenterReview.objects.all()
        paginator=PageNumberPagination()
        page_obj=paginator.paginate_queryset(center_reviews,request)
        serializer=CenterReviewSerializer(page_obj,many=True)
        return paginator.get_paginated_response(data=serializer.data)

    def delete(self,request,pk):
        center_review=CenterReview.objects.get(pk=pk)
        center_review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self,request,pk):
        center_review = CenterReview.objects.get(pk=pk)
        serializer=CenterReviewSerializer(instance=center_review,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        center_review = CenterReview.objects.get(pk=pk)
        serializer=CenterReviewSerializer(instance=center_review,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CenterListDetailUpdateDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        centers = CenterSerializer.objects.all()
        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(centers, request)
        serializer = CenterSerializer(page_obj, many=True)
        return paginator.get_paginated_response(data=serializer.data)

    def delete(self,request,pk):
        center=Center.objects.get(pk=pk)
        center.delete()
        return Response(status=204)

    def put(self,request,pk):
        center=Center.objects.get(pk=pk)
        serializer=CenterSerializer( instance=center,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        center=Center.objects.get(pk=pk)
        serializer=CenterSerializer( instance=center,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class CenterList(LoginRequiredMixin,View):
    def get(self,request):
        centers=Center.objects.order_by('create_at')
        search_query=request.GET.get('q')
        if search_query:
            centers=centers.filter(title__icontains=search_query)
        # context={
        #     'books':books
        # }

        paginator = Paginator(centers, 2)
        page = request.GET.get('page')
        try:
            centers = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            centers = paginator.page(paginator.num_pages)

        return render(request,'centers/center_list.html',{'centers':centers})


class CenterDetailView(LoginRequiredMixin,View):
    def get(self,request,pk):
        # book = get_object_or_404(Books, pk=pk)
        center=Center.objects.get(pk=pk)
        # book_review=BookReview.objects.all()
        context = {
            'centers': center,
            # 'book_review':book_review
        }
        return render(request,'centers/center_detail.html',context=context)