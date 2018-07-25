from django.db import models
from .models import *
from django import forms


class SearchForm(forms.Form):
    hmc_search = forms.IntegerField(label = "HMC to search for", required = True)
    date_search = forms.IntegerField(label = "Date to search for")
    month_search = forms.IntegerField(label = "Month to search for")
    year_search = forms.IntegerField(label = "Year to search for")

    date_check = forms.BooleanField()
    month_check = forms.BooleanField()
    year_check = forms.BooleanField()


class DeleteForm(forms.Form):
    hmc_search = forms.IntegerField(label = "HMC to search for")
    date_search = forms.IntegerField(label = "Date to search for")
    month_search = forms.IntegerField(label = "Month to search for")
    year_search = forms.IntegerField(label = "Year to search for")

    date_check = forms.BooleanField()
    month_check = forms.BooleanField()
    year_check = forms.BooleanField()


class ReportGenerationForm(forms.Form):
    month_search = forms.IntegerField(label = "Month to search for", required = True)
    year_search = forms.IntegerField(label = "Year to search for", required = True)
    hmc_search = forms.IntegerField(label = "HMC to search for", required = True)
    reason_search = forms.CharField(label = "Reason to search for", required = True)


class VesselwiseTonnageForm(forms.Form):
    hmc_search = forms.IntegerField(label = "HMC to search for", required = True)
    month_search = forms.IntegerField(label = "Month to search for", required = True)
    year_search = forms.IntegerField(label = "Year to search for", required = True)


class DateForm(forms.Form):
    date = forms.DateField(label = "Date", required = True)


class ShiftForm(forms.Form):
    hmc_number = forms.IntegerField(label = "HMC Number", required = True)
    shift = forms.IntegerField(label = "Shift Number", required = True)


class ShiftEndForm(forms.Form):
    date = forms.DateField(label = "Date", required = True)
    hmc_number = forms.IntegerField(label = "HMC Number", required = True)
    shift = forms.IntegerField(label = "Shift Number", required = True)
    diesel_start_percentage = forms.FloatField(label = "Diesel Start Percentage", required = True)
    diesel_end_percentage = forms.FloatField(label = "Diesel End Percentage", required = True)
    diesel_start_hours = forms.FloatField(label = "Diesel Start Hour", required = True)
    diesel_end_hours = forms.FloatField(label = "Diesel End Hour", required = True)
    total_tonnage_or_boxes = forms.IntegerField(label = "Total Tonnage/Boxes ", required = True)
    cycles = forms.IntegerField(label = "Cycles", required = True)


class VesselForm(forms.Form):
    vessel_name = forms.CharField(label = "Vessel Name", required = True)
    vessel_cargo = forms.CharField(label = "Vessel Cargo", required = True)
    berth_number = forms.IntegerField(label = "Berth Number", required = True)


class SlotForm(forms.Form):
    time_slot_start = forms.TimeField(label = "Time Slot Start", required = True);
    time_slot_stop = forms.TimeField(label = "Time Slot Stop", required = True);
    reason = forms.CharField(label = "Reason", required = True);
    remark = forms.CharField(label = "Remark", required = False);
