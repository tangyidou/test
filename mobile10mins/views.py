from django.shortcuts import render
from mobile10mins.models import UserInfo
from mobile10mins.form import UserInfoForm

# Create your views here.
def userlistpanel(request):
    return render(request, 'userListPanel.html', {})

def userlistpanel_login(request):
    return render(request, 'userListPanelLogin.html', {})

def userdetail(request, id):
    if request.method == 'GET':
        form = UserInfoForm
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            c = UserInfo(name=name, password=password)
            c.save()
            return redirect(to='datail')

    context = {}
    userinfo_list = UserInfo.objects.all()
    userinfo = UserInfo.objects.get(id=id)
    context['userinfo'] = userinfo
    context['userinfo_list'] = userinfo_list
    context['form'] = form
    return render(request, 'userDetail.html', context)
