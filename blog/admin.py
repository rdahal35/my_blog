from django.contrib import admin
from django.contrib import messages

from .models import Post
from django import forms

from ckeditor.widgets import CKEditorWidget

# admin.site.register(Post)


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = Post
        fields = "__all__"


# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created_date')
#     list_filter = ('created_date',)
#     search_fields = ("title", )
#     form = PostAdminForm

#     class Meta:
#         ordering = ('title')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date',
                    'published_date', 'author', 'is_active')
    list_filter = ('title', 'created_date', 'published_date', 'is_active')
    search_fields = ('title',)
    form = PostAdminForm

    # def active(self, obj):
    #     return obj.is_active == True
    # active.boolean = True

    def make_active(modeladmin, request, queryset):
        queryset.update(is_active=True)
        messages.success(
            request, "Selected Record(s) Marked as Active Successfully !!"
        )

    def make_inactive(modeladmin, request, queryset):
        queryset.update(is_active=False)
        messages.success(
            request, "Selected Record(s) Marked as Inactive Successfully !!")

    def has_delete_permission(self, request, obj=None):
        return False

    admin.site.add_action(make_active, "Make Active")
    admin.site.add_action(make_inactive, "Make Inactive")
