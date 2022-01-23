from django.contrib import admin
from .models import sendOtp,Profile,Blog,Categories
# Register your models here.



@admin.register(Profile)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["phone"]
    def queryset(self, request):
        qs = super(Profile, self).queryset(request)
        return qs.filter(is_deleted=True)
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_deleted=False)

    def delete_model(self, request, object):
        print(self,object.id)
        Profile.objects.filter(pk=object.id).update(is_deleted=True)
        # self.is_deleted = True

        pass

admin.site.register(sendOtp)
admin.site.register(Categories)
admin.site.register(Blog)