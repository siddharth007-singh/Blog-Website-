from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.


def get_user(r):
    if r.session.has_key('logins'):
        return NewUser.objects.get(nu_name=r.session['logins'])


def get_admin(r):
    if r.session.has_key('add_log'):
        return Admin_login.objects.get(name=r.session['add_log'])


def home(r):
    return render(r, "public/home.html", {
        "cat": Category.objects.all(),
        "top": Topic.objects.all(),
        "home_post": Posts.objects.filter(post_status=0),
        "postcount": Posts.objects.all().count(),
        "usercount": NewUser.objects.all().count(),
        "topiccount": Topic.objects.all().count(),
        "user": get_user(r)
    })


def category_filter(r, cat_id):
    data = {
        "home_post": Posts.objects.filter(post_category__cat_id=cat_id),
        "cat": Category.objects.all(),
        "top": Topic.objects.all(),
    }
    return render(r, "public/home.html", data)


def searchbar(r):
    if r.method == "GET":
        search_data = r.GET.get('search')
        data = {
            "home_post": Posts.objects.filter(post_category__cat_title__icontains=search_data),
            "cat": Category.objects.all(),
            "top": Topic.objects.all(),
        }
        return render(r, "public/home.html", data)
    else:
        return redirect(home)


def detail(r,post_id):
    data = {
        "posts": Posts.objects.filter(post_id=post_id),
        "topics": Topic.objects.all(),
        "cat": Category.objects.all(),
    }
    return render(r, "public/details.html", data)


def meet_author(r):
    return render(r, "public/meet_author.html", {
        "newauthor": NewUser.objects.all(),
        "cat": Category.objects.all(),
    })


def login(r):
    form = NewUserForm(r.POST or None, r.FILES or None)
    if r.method=="POST":
        if form.is_valid():
            n = NewUser()
            n.nu_name = r.POST.get('nu_name')
            n.nu_city = r.POST.get('nu_city')
            n.nu_state = r.POST.get('nu_state')
            n.nu_image = r.FILES.get('nu_image')
            n.nu_doc = r.POST.get('nu_doc')
            n.nu_address = r.POST.get('nu_address')
            n.nu_phone = r.POST.get('nu_phone')
            n.nu_email = r.POST.get('nu_email')
            n.nu_password = r.POST.get('nu_password')
            n.nu_myself = r.POST.get('nu_myself')
            n.save()
            return redirect(signin)
    return render(r, "public/login.html")


def signin(r):
    if r.method == "POST":
        nu_name = r.POST.get('nu_name')
        nu_password = r.POST.get('nu_password')
        cond = (Q(nu_name=nu_name) & Q(nu_password=nu_password))
        check = NewUser.objects.get(cond)
        if(check):
            r.session['logins'] = nu_name
            return redirect(home)
        else:
            return redirect(signin)
    return render(r, "public/signin.html")


def user_dashboard(r):
    log = get_user(r)
    return render(r, "user/dashboard.html", {
        "postcount": Posts.objects.filter(post_user__nu_name=log).count(),
        "categorycount": Category.objects.filter().count(),
        "topiccount": Topic.objects.all().count(),
        'user': log,
    })


def user_profile(r):
    log = get_user(r)
    return render(r, "user/profile.html", {
        "user": log,
    })


def user_edit_info(r, nu_id):
    log = get_user(r)
    get_id = NewUser.objects.get(nu_id=nu_id)
    edit = UserProfileEditForms(r.POST or None, instance=get_id)
    if r.method=="POST":
        if edit.is_valid():
            edit.save()
            return redirect(user_profile)
    return render(r, "user/edit_user_info.html", {
        "edit":edit,
        'user': log,
    })


def user_edit_image(r, nu_id):
    log = get_user(r)
    get_id = NewUser.objects.get(nu_id=nu_id)
    editform = UserImageEditForms(r.FILES or None, instance=get_id)
    if r.method == "POST":
        if editform.is_valid():
            editform.save()
            return redirect(user_profile)
    return render(r, "user/edit_image_info.html", {
        "editform": editform,
        'user': log,
    })


def user_view_post(r, post_id):
    log = get_user(r)
    return render(r, "user/view_post.html", {
        "view": Posts.objects.filter(post_id=post_id),
        "user": log,
    })


def user_edit_post(r, post_id):
    log = get_user(r)
    get_id = Posts.objects.get(post_id=post_id)
    editform = PostForms(r.POST or None, r.FILES or None, instance=get_id)
    if r.method == "POST":
        if editform.is_valid():
            editform.save()
            return redirect(user_manage_post)
    return render(r, "user/user_post_edit.html",  {
        "edit": editform,
        "user": log,
    })


def user_insert_post(r):
    log = r.session['logins']
    form = PostForms(r.POST or None, r.FILES or None)
    if r.method == "POST":
        if form.is_valid():
            id = NewUser.objects.get(nu_name=log).nu_id
            p = Posts()
            p.post_user = NewUser(id)
            p.post_name = r.POST.get('post_name')
            p.post_category = Category(r.POST.get('post_category'))
            p.post_topic = Topic(r.POST.get('post_topic'))
            p.post_image = r.FILES.get('post_image')
            p.post_description = r.POST.get('post_description')
            p.post_doc = r.POST.get('post_doc')
            p.save()
            return redirect(user_manage_post)
    return render(r, "user/insert_post.html", {
        "cat": Category.objects.all(),
        "topic": Topic.objects.all(),
        "user": log,
    })


def user_manage_post(r):
    log = get_user(r)
    return render(r, "user/manage_post.html", {
        "posts": Posts.objects.filter(post_user__nu_name=log),
        "user": log,
    })


def user_insert_cat(r):
    log = get_user(r)
    form = CategoryForms(r.POST or None)
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(user_insert_cat)
    return render(r, "user/insert_category.html", {
        "form": form,
        "cat": Category.objects.all(),
        "user": log,
    })


def user_insert_topic(r):
    log = get_user(r)
    form = TopicForms(r.POST or None)
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(user_insert_topic)
    return render(r, "user/insert_topic.html", {
        "form": form,
        "topic": Topic.objects.all(),
        "user":log,
    })


def user_report(r):
    log = get_user(r)
    if r.method == "GET":
        q1 = r.GET.get("q1")
        q2 = r.GET.get("q2")
        data = {"se": Posts.objects.filter(post_doc__range=[q1, q2])}
        return render(r, "user/report.html", {
            "n": data,
            "user": log,
        })


def admin_login(r):
    form = AdminLoginForm(r.POST or None)
    if r.method == "POST":
        if form.is_valid():
            name = r.POST.get("name")
            password = r.POST.get("password")
            cond = (Q(name=name) & Q(password=password))
            check = Admin_login.objects.get(cond)
            if check:
                r.session['add_log'] = name
                return redirect(secure_dashboard)
            else:
                return redirect(admin_login)
    return render(r, "secure/addlog.html", {
        "form": form,
    })


def secure_dashboard(r):
    if r.session.has_key('add_log'):
        return render(r, "secure/dashboard.html", {
            "topiccount": Topic.objects.all().count(),
            "categorycount": Category.objects.all().count(),
            "postcount": Posts.objects.all().count(),
            "usercount": NewUser.objects.all().count(),
            "likecount": Likes.objects.all().count(),
        })
    else:
        return redirect(admin_login)


def secure_manage_post(r):
    return render(r, "secure/manage_post.html", {
        "sec_post": Posts.objects.all(),
    })


def secure_manage_user(r):
    return render(r, "secure/manage_user.html", {
        "users": NewUser.objects.all()
    })


def secure_manage_report(r):
    return render(r, "secure/manage_report.html")


def secure_manage_profile(r):
    pass


def secure_viewpost(r, post_id):
    data = {
        "view": Posts.objects.filter(post_id=post_id)
    }
    return render(r, "secure/view_post.html",data)


def delete_post(r, post_id):
    get_id = Posts.objects.get(post_id=post_id)
    get_id.delete()
    return redirect(user_manage_post)


def secure_edit(r, post_id):
    get_id = Posts.objects.get(post_id=post_id)
    editform = PostAdminForms(r.POST or None, r.FILES or None, instance=get_id)
    if r.method == "POST":
        if editform.is_valid():
            editform.save()
            return redirect(secure_manage_post)
    return render(r, "secure/edit.html", {"edit": editform})


def like_dislike(r, id):
    if r.session.has_key('logins'):
        like = Likes.objects.filter(post_like__post_id=id, user_like__nu_name=r.session['logins']).count()
        if like > 0:
            like = Likes.objects.filter(post_like__post_id=id, user_like__nu_name=r.session['logins'])
            like.delete()
            print("disliked")
            return redirect(home)
        else:
            like = Likes()
            like.post_like = Posts(id)
            like.user_like = NewUser(NewUser.objects.get(nu_name=r.session['logins']).nu_id)
            like.save()
            print("Liked")
            return redirect(home)
    else:
        return redirect(signin)


def comment(r):
    pass


def logout(r):
    if r.session.has_key('logins'):
        del r.session['logins']
        return redirect(home)