from django.contrib import admin

from .models import Date,Shift,Vessel,Slot

class ShiftInline(admin.StackedInline):
    model = Shift


class SlotInline(admin.StackedInline):
    model = Slot

class ShiftAdmin(admin.ModelAdmin):
    inlines = [SlotInline]

class DateAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date information', {'fields': ['date']}),]
    inlines = [ShiftInline]

admin.site.register(Date,DateAdmin)

admin.site.register(Shift,ShiftAdmin)
# admin.site.register(Shift)
# admin.site.register(Vessel)
# admin.site.register(Slot)
