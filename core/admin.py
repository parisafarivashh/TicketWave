from django.contrib import admin

from core.models import Hall


class HallAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_by', 'title')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Hall, HallAdmin)

