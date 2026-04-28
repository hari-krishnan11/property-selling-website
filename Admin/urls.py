from django.urls import path
from Admin import views
app_name="Admin"
urlpatterns = [
path('District/',views.District,name="District"),
path('deleteDistrict/<int:did>',views.deleteDistrict,name="deleteDistrict"),
path('EditDistrict/<int:did>',views.EditDistrict,name="EditDistrict"),

path('Category/',views.Category,name="Category"),
path('deleteCategory/<int:did>',views.deleteCategory,name="deleteCategory"),
path('EditCategory/<int:did>',views.EditCategory,name="EditCategory"),

path('AdminReg/',views.AdminReg,name="AdminReg"),
path('deleteAdmin/<int:did>',views.deleteAdmin,name="deleteAdminReg"),
path('EditAdmin/<int:did>',views.EditAdmin,name="EditAdmin"),

path('place/',views.place,name="place"),
path('deleteplace/<int:did>',views.deleteplace,name="deleteplace"),
path('Editplace/<int:did>',views.Editplace,name="Editplace"),

path('SubCategory/',views.SubCategory,name="SubCategory"),
path('EditSubcategory/<int:did>',views.EditSubcategory,name="EditSubcategory"),
path('deletesubcategroy/<int:did>',views.deletesubcategroy,name="deletesubcategroy"),


path('HomePage/',views.HomePage,name="HomePage"),

path('verifyseller/',views.verifyseller,name="verifyseller"),

path('AccpetSeller/<int:sid>',views.AccpetSeller,name="AccpetSeller"),
path('rejectSeller/<int:sid>',views.rejectSeller,name="rejectSeller"),

path('verifyUser/',views.verifyuser,name="verifyUser"),

path('AccpetUser/<int:uid>',views.AccpetUser,name="AccpetUser"),
path('rejectUser/<int:uid>',views.rejectUser,name="rejectUser"),

path('Sellercomplaints/',views.Sellercomplaints,name="Sellercomplaints"),

path('usercomplaints/',views.Usercomplaints,name="usercomplaints"),

path('reply/<int:cid>/',views.reply,name="reply"),


path('feedback/',views.feedback,name="feedback"),

path('ViewProperty/',views.ViewProperty,name="ViewProperty"),

path('logout/',views.logout,name="logout"),
]