from django.contrib import admin

from .models import Flat, Complaint, Owner

class OwnedFlatsInline(admin.TabularInline):
    model = Owner.have_flats.through
    raw_id_fields = ['owner']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'owner', 'address']
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ['new_building']
    list_filter = ('new_building', 'town', 'has_balcony', 'rooms_number')
    raw_id_fields = ['liked_by']
    inlines = [
        OwnedFlatsInline,
    ]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['complain_flat']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['have_flats']
    inlines = [
        OwnedFlatsInline,
    ]

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)