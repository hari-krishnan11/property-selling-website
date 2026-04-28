from django.http import JsonResponse
from django.shortcuts import redirect, render
from Admin.models import *
from Guest.models import *
from User.models import *

# Create your views here.
def District(request):
    districtData=tbl_district.objects.all()
    if request.method == "POST":
        name = request.POST.get("Districtname")
        tbl_district.objects.create(district_name=name)
        return render(request,'Admin/District.html')
    else:
        return render(request,'Admin/District.html',{'districtData':districtData})
    
def deleteDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return render(request,'Admin/District.html',{'msg':"Deleted"})

def EditDistrict(request,did):
    EditData=tbl_district.objects.get(id=did)
    districtData=tbl_district.objects.all()

    if request.method == "POST":
        name = request.POST.get("Districtname")
        EditData.district_name=name
        EditData.save()
        return render(request,'Admin/District.html',{"msg":"Updated"})

    else:
        return render(request,'Admin/District.html',{'EditData':EditData,'districtData':districtData})


def Category(request):
    CategoryData=tbl_category.objects.all()
    if request.method =="POST":
        name = request.POST.get("Category")
        tbl_category.objects.create(category_name=name)
        return render(request,'Admin/Category.html')
    else:
        return render(request,'Admin/Category.html',{'CategoryData':CategoryData})
    

def deleteCategory(request,did):
    tbl_category.objects.get(id=did).delete()
    return render(request,'Admin/Category.html',{"msg":"Deleted"})

def EditCategory(request,did):
    EditData=tbl_category.objects.get(id=did)
    CategoryData=tbl_category.objects.all()

    if request.method == "POST":
        name = request.POST.get("Category")
        EditData.category_name=name
        EditData.save()
        return render(request,'Admin/Category.html',{"msg":"Updated"})

    else:
        return render(request,'Admin/Category.html',{'EditData':EditData,'CategoryData':CategoryData})


def AdminReg(request):
    AdminData=tbl_adminreg.objects.all()
    if request.method =="POST":
        name = request.POST.get("name")
        email=request.POST.get("Email")
        password=request.POST.get("Password")
        tbl_adminreg.objects.create(adminReg_name=name,adminReg_Email=email,adminReg_password=password)
        return render(request,'Admin/AdminReg.html',{'msg':"Inserted"})
    else:
        return render(request,'Admin/AdminReg.html',{'AdminData':AdminData})
    

def deleteAdmin(request,did):
    tbl_adminreg.objects.get(id=did).delete()
    return render(request,'Admin/AdminReg.html',{"msg":"Deleted"})

def EditAdmin(request,eid):
    EditData=tbl_adminreg.objects.get(id=eid)
    AdminData=tbl_adminreg.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("Email")
        password = request.POST.get("password")
        EditData.adminReg_name=name
        EditData.adminReg_name=email
        EditData.adminReg_name=password
        EditData.save()
        return render(request,'Admin/AdminReg.html',{"msg":"Updated"})
    else:
        return render(request,'Admin/AdminReg.html',{'EditData':EditData,'AdminData':AdminData})
    

def place(request):
    districtData=tbl_district.objects.all()
    placeData=tbl_place.objects.all()
    if request.method == "POST":
        place=request.POST.get('txt_place')
        district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(place_name=place,district=district)
        return render(request,'Admin/Place.html',{"msg":"Inserted"})
    else:
        return render(request,'Admin/Place.html',{'districtData':districtData,'placeData':placeData})
    

def deleteplace(request,did):
    tbl_place.objects.get(id=did).delete()
    return render(request,'Admin/place.html',{"msg":"Deleted"})

def Editplace(request,did):
    EditData=tbl_place.objects.get(id=did)
    placeData=tbl_place.objects.all()
    districtData=tbl_district.objects.all()
    if request.method == "POST":
        place=request.POST.get('txt_place')
        district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        EditData.place_name=place
        EditData.district=district
        EditData.save()
        return render(request,'Admin/Place.html',{"msg":"Updated"})
    else:
        return render(request,'Admin/Place.html',{'placeData':placeData,'EditData':EditData,'districtData':districtData})

def SubCategory(request):
    CategoryData=tbl_category.objects.all()
    SubCategoryData=tbl_subcategory.objects.all()
    if request.method == "POST":
        SubCategory=request.POST.get('txt_SubCategory')
        Category=tbl_category.objects.get(id=request.POST.get('sel_Category'))
        tbl_subcategory.objects.create(subcategory_name=SubCategory,Category=Category)
        return render(request,'Admin/SubCategory.html',{"msg":"Inserted"})
    else:
        return render(request,'Admin/SubCategory.html',{'CategoryData':CategoryData,'SubCategory':SubCategoryData})
    

def EditSubcategory(request,did):
    EditData=tbl_subcategory.objects.get(id=did)
    SubCategoryData=tbl_subcategory.objects.all()
    CategoryData=tbl_category.objects.all()
    if request.method == "POST":
        SubCategory=request.POST.get('txt_SubCategory')
        Category=tbl_category.objects.get(id=request.POST.get('sel_Category'))
        EditData.subcategory_name=SubCategory
        EditData.Category=Category
        EditData.save()
        return render(request,'Admin/SubCategory.html',{"msg":"Updated"})
    else:
        return render(request,'Admin/SubCategory.html',{'CategoryeData':SubCategoryData,'EditData':EditData,'CategoryData':CategoryData})

def deletesubcategroy(request,did):
    tbl_subcategory.objects.get(id=did).delete()
    return render(request,'Admin/SubCategory.html',{"msg":"Deleted"})


from django.db.models import Q

def HomePage(request):

    users = tbl_user.objects.count()
    sellers = tbl_seller.objects.count()
    complaints = tbl_complaint.objects.count()
    feedbacks = tbl_feedback.objects.count()

    complaints_list = tbl_complaint.objects.filter(seller__isnull=False).order_by('-complaint_date')[:5]
    user_complaints_list = tbl_complaint.objects.filter(user__isnull=False).order_by('-complaint_date')[:5]

    # Booking / Payment report data
    reportData = tbl_booking.objects.filter(booking_status=4)

    if request.method == "POST":

        username = request.POST.get("username")
        sellername = request.POST.get("sellername")
        place = request.POST.get("place")
        fdate = request.POST.get("fdate")
        tdate = request.POST.get("tdate")

        if username:
            reportData = reportData.filter(user__user_name__icontains=username)

        if sellername:
            reportData = reportData.filter(property__seller__seller_name__icontains=sellername)

        if place:
            reportData = reportData.filter(property__place__place_name__icontains=place)

        if fdate and tdate:
            reportData = reportData.filter(booking_date__range=[fdate, tdate])

    context = {
        "users": users,
        "sellers": sellers,
        "complaints": complaints,
        "feedbacks": feedbacks,
        "complaints_list": complaints_list,
        "reportData": reportData,
        "user_complaints_list": user_complaints_list,

    }

    return render(request, "Admin/HomePage.html", context)

def verifyseller(request):
    sellerData=tbl_seller.objects.filter(seller_status=0)
    sellerDataAccpeted=tbl_seller.objects.filter(seller_status=1)
    sellerDataRejected=tbl_seller.objects.filter(seller_status=2)

    return render(request,'Admin/verifyseller.html',{'sellerData':sellerData,'sellerDataAccpeted':sellerDataAccpeted,'sellerDataRejected':sellerDataRejected})
    
def AccpetSeller(request,sid):
    seller=tbl_seller.objects.get(id=sid)
    seller.seller_status=1
    seller.save()
    return render(request,'Admin/verifyseller.html',{'msg':"Seller Accepted"})

def rejectSeller(request,sid):
    seller=tbl_seller.objects.get(id=sid)
    seller.seller_status=2
    seller.save()
    return render(request,'Admin/verifyseller.html',{'msg':"Seller Rejected"})

def verifyuser(request):
    userData=tbl_user.objects.filter(user_status=0)
    userDataAccpeted=tbl_user.objects.filter(user_status=1)
    userDataRejected=tbl_user.objects.filter(user_status=2)

    return render(request,'Admin/verifyUser.html',{'userData':userData,'userDataAccpeted':userDataAccpeted,'userDataRejected':userDataRejected})


def AccpetUser(request,uid):
    user=tbl_user.objects.get(id=uid)
    user.user_status=1
    user.save()
    return render(request,'Admin/verifyUser.html',{'msg':"User Accepted"})

def rejectUser(request,uid):
    user=tbl_user.objects.get(id=uid)
    user.user_status=2
    user.save()
    return render(request,'Admin/verifyUser.html',{'msg':"User Rejected"})


def Sellercomplaints(request):
    complaintData = tbl_complaint.objects.filter(seller__isnull=False)
    return render(request,'Admin/Sellercomplaints.html',{'complaintData':complaintData})

def Usercomplaints(request):
    complaintData=tbl_complaint.objects.filter(user__isnull=False)
    return render(request,'Admin/UserComplaints.html',{'complaintData':complaintData})

def reply(request,cid):
    replyData=tbl_complaint.objects.get(id=cid)
    if request.method == "POST":
        reply=request.POST.get("txt_reply")
        replyData.complaint_reply=reply
        replyData.save()
        return render(request,'Admin/Reply.html',{'msg':"Reply Updated"})
    return render(request,'Admin/Reply.html')


def feedback(request):
    feedbackData=tbl_feedback.objects.filter(seller__isnull=False)
    feedbackDatas=tbl_feedback.objects.filter(user__isnull=False)

    return render(request,'Admin/Feedback.html',{'feedbackData':feedbackData, 'feedbackDatas':feedbackDatas})

def ViewProperty(request):
    propertyData=tbl_property.objects.all()
    districtData = tbl_district.objects.all()
    return render(request,'Admin/View Property.html',{'propertyData':propertyData, 'districtData':districtData})

def logout(request):
    return redirect('Guest:Login')