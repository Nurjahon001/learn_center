from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import CustomUser
from users.serializers import CustomUserSerializer
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserCreateForm,CustomUserUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CustomUserListUpdateDelateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user=CustomUser.objects.all()
        serializer=CustomUserSerializer(user,many=True)
        return Response(data=serializer.data)

    def delete(self,request,pk):
        user=CustomUser.objects.get(pk=pk)
        user.delete()
        return Response(status=204)

    def put(self,request,pk):
        user=CustomUser.objects.get(pk=pk)
        serializer=CustomUserSerializer( instance=user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        user=CustomUser.objects.get(pk=pk)
        serializer=CustomUserSerializer( instance=user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CustomUserDetailUpdateDelateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        user=CustomUser.objects.get(pk=pk)
        serializer=CustomUserSerializer(user)
        return Response(data=serializer.data)

    def delete(self,request,pk):
        user=CustomUser.objects.get(pk=pk)
        user.delete()
        return Response(status=204)

    def put(self,request,pk):
        user=CustomUser.objects.get(pk=pk)
        serializer=CustomUserSerializer( instance=user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        user=CustomUser.objects.get(pk=pk)
        serializer=CustomUserSerializer( instance=user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)














class UserRegisterView(View):
    def get(self,request):
        create_form=CustomUserCreateForm()
        context={
            'form':create_form
        }
        return render(request,'users/register.html',context)

    def post(self,request):
        create_form=CustomUserCreateForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('users:login')
        else:
            context = {
                'form': create_form
            }
            return render(request, 'users/register.html',context=context)

        # print(request.POST['username'])
        # username=request.POST['username']
        # first_name=request.POST['first_name']
        # last_name=request.POST['last_name']
        # email=request.POST['email']
        # password=request.POST['password']
        #
        # user=CustomUser.objects.create(
        #     username=username,
        #     first_name=first_name,
        #     last_name=last_name,
        #     email=email
        # )
        # user.set_password(password)
        # user.save()

class CustomUserLogin(View):
    def get(self,request):
        login_form=AuthenticationForm
        context = {
            'form': login_form
        }
        return render(request, 'users/login.html', context)

    def post(self,request):
        login_form=AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user=login_form.get_user()
            login(request,user)
            return redirect('home')
        else:
            context = {
                'form': login_form
            }
            return render(request, 'users/login.html', context)


class LogoutView(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        return render(request,'home.html')

class ProfileView(LoginRequiredMixin,View):
    def get(self,request):
        context={
            'user': request.user
        }
        return  render(request,'users/profile.html',context=context)

class ProfileUpdateView(LoginRequiredMixin,View):
    def get(self,request):
        update_form=CustomUserUpdateForm(instance=request.user)
        context={
            'update_form':update_form
        }
        return render(request,'users/profile_update.html',context=context)

    def post(self,request):
        update_form=CustomUserUpdateForm(instance=request.user, data=request.POST, files=request.FILES)
        # update_form.is_valid()
        # user=update_form.save()
        # return redirect('users:profile')
        if update_form.is_valid():
            update_form.save()
            return redirect('users:profile')
        else:
            return render(request,'users/profile_update.html',{'update_form':update_form})