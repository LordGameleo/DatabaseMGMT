import datetime, operator
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from report.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



@login_required(login_url = '/account/login/')
def main(request):
    return render(request, 'main.html',)

def add_options(request):
    return render(request, 'add_options.html',)

def report_options(request):
    return render(request, 'report_options.html')

@login_required(login_url = '/account/login/')
def add(request):
    if request.user.has_perm('MPT.add_date'):
        form1 = DateForm(request.POST)
        form2 = ShiftForm(request.POST)
        form3 = VesselForm(request.POST)
        form4 = SlotForm(request.POST)

        if request.method == 'POST' :
            if  form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
                date = form1.cleaned_data['date']

                hmc_number = form2.cleaned_data['hmc_number']
                shift = form2.cleaned_data['shift']
                vessel_name = form3.cleaned_data['vessel_name']
                vessel_cargo = form3.cleaned_data['vessel_cargo']

                time_slot_start = form4.cleaned_data['time_slot_start']
                time_slot_stop = form4.cleaned_data['time_slot_stop']
                reason = form4.cleaned_data['reason']
                remark = form4.cleaned_data['remark']

                if Date.objects.filter(date = date):       #if list is non empty it will proceed
                    date_data = Date.objects.filter(date = date)[0]
                else:
                    date_data = Date(
                        date = date
                        )
                    date_data.save()

                if Shift.objects.filter(date__date = date).filter(shift = shift).filter(hmc_number = hmc_number):
                    shift_data = Shift.objects.filter(date__date = date).filter(shift =shift).filter(hmc_number = hmc_number)[0]
                else:
                    shift_data = Shift(date = date_data, shift = shift, hmc_number = hmc_number, user = request.user)
                    shift_data.save()

                if shift_data.shift_end_flag == 0:
                    slot_data = Slot(shift = shift_data, time_slot_start = time_slot_start, time_slot_stop = time_slot_stop,
                    reason = reason, remark = remark)
                    slot_data.save()
                    vessel_data = Vessel(
                                    slot = slot_data,
                                    vessel_name = vessel_name,
                                    vessel_cargo = vessel_cargo
                                  )
                    vessel_data.save()
                    return render(request,'message.html',{'message':"Entry Saved!!!  **or Shift already existed"})
                else:
                    return render(request,'message.html',{'message':"Shift has already been ended.You can't add data again now."})

        else:

            form1 = DateForm()
            form2 = ShiftForm()
            form3 = VesselForm()
            form4 = SlotForm()

        dates = Date.objects.all().order_by('-date')[:2]
        return render(request, 'add.html', { 'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4,'dates':dates})
    else:
        return render(request,'message.html',{'message':"You don't have permison to add data."})


@login_required(login_url = '/account/login/')
def add_shift_end(request):
    form = ShiftEndForm(request.POST)
    if request.method == "POST":

        if form.is_valid():
            date = form.cleaned_data['date']
            shift = form.cleaned_data['shift']
            hmc_number = form.cleaned_data['hmc_number']
            diesel_end_hours = form.cleaned_data['diesel_end_hours']
            diesel_start_hours = form.cleaned_data['diesel_start_hours']
            diesel_start_percentage = form.cleaned_data['diesel_end_percentage']
            diesel_end_percentage = form.cleaned_data['diesel_end_percentage']
            total_tonnage_or_boxes = form.cleaned_data['total_tonnage_or_boxes']
            cycles = form.cleaned_data['cycles']
            shift_objects = Shift.objects.filter(date__date = date, shift = shift, hmc_number = hmc_number)
            if shift_objects:
                shift_object = shift_objects[0]
                if shift_object.shift_end_flag == 0:
                    shift_object.diesel_start_hours = diesel_start_hours
                    shift_object.diesel_end_hours = diesel_end_hours
                    shift_object.diesel_start_percentage = diesel_start_percentage
                    shift_object.diesel_end_percentage = diesel_end_percentage
                    shift_object.total_tonnage_or_boxes = total_tonnage_or_boxes
                    shift_object.cycles = cycles
                    shift_object.user = request.user
                    shift_object.shift_end_flag = 1
                    shift_object.save()
                    return render(request,'message.html',{'message':"Shift has been ended successfully."})
                else:
                    return render(request,'message.html',{'message':"Shift has already been ended.You can't end it again."})
            else:
                return render(request,'message.html',{'message':"Shift doesn't exist."})
        else:
            form = ShiftEndForm()
    return render(request, 'add_shift_end.html', { 'form': form})


@login_required(login_url = '/account/login/')
def delete_view(request):
    if request.user.has_perm('MPT.delete_date'):
        form = SearchForm(request.POST)
        if request.method == 'POST' :
            date_search = request.POST['date_search']
            month_search = request.POST['month_search']
            year_search = request.POST['year_search']
            hmc_search = request.POST['hmc_search']

            if date_search != "" and month_search != "" and year_search != "":
                search_results = Shift.objects.filter(date__date__day = date_search).filter(date__date__month = month_search).filter(date__date__year = year_search).filter(hmc_number = hmc_search).order_by('date__date', 'shift')
            elif date_search != "" and month_search != "" and year_search == "":
                search_results = Shift.objects.filter(date__date__day = date_search).filter(date__date__month = month_search).filter(hmc_number = hmc_search).order_by('date__date', 'shift')
            elif date_search != "" and month_search == "" and year_search != "":
                search_results = Shift.objects.filter(date__date__day = date_search).filter(date__date__year = year_search).filter(hmc_number = hmc_search).order_by('date__date', 'shift')
            elif date_search != "" and month_search == "" and year_search == "":
                search_results = Shift.objects.filter(date__date__day = date_search).filter(hmc_number = hmc_search).order_by('date__date', 'shift')
            elif date_search == "" and month_search != "" and year_search != "":
                search_results = Shift.objects.filter(date__date__month = month_search).filter(date__date__year = year_search).filter(hmc_number = hmc_search).order_by('date__date', 'shift')
            elif date_search == "" and month_search != "" and year_search == "":
                search_results = Shift.objects.filter(date__date__month = month_search).filter(hmc_number = hmc_search).order_by('date__date', 'shift')
            elif date_search == "" and month_search == "" and year_search != "":
                search_results = Shift.objects.filter(date__date__year = year_search).filter(hmc_number = hmc_search).order_by('date__date', 'shift')
            else:
                search_results = []
            if search_results:
                context = {'search_results': search_results}
                return render(request, 'delete_result.html', context)
            else:
                return render(request,'message.html',{'message':"No data for given parameters exists."})
        else:
            form = SearchForm()

        return render(request, 'delete.html', {'form': form})

    else:
        return render(request,'message.html',{'message':"You don't have permission to delete data."})


@login_required(login_url = '/account/login/')
def delete_date_entry(request, date_id):
    date = Date.objects.filter(id = date_id).delete()
    return render(request,'message.html',{'message':"Data has been deleted successfully."})


@login_required(login_url = '/account/login/')
def delete_shift_entry(request, shift_id):
    to_be_deleted = Shift.objects.filter(id = shift_id)
    if to_be_deleted:
        date_id = to_be_deleted[0].date.id
    else:
        return render(request,'message.html',{'message':"Either Date doesn't exist or has been deleted."})
    to_be_deleted.delete()
    check_empty_date = Shift.objects.filter(date__id = date_id)
    if check_empty_date:
        pass
    else:
        Date.objects.filter(id = date_id).delete()
    return render(request,'message.html',{'message':"Shift has been deleted successfully."})

@login_required(login_url = '/account/login/')
def delete_slot_entry(request, slot_id):
    Slot.objects.filter(id = slot_id).delete()
    return render(request,'message.html',{'message':"Slot has been deleted successfully."})

# finish the searching code
@login_required(login_url = '/account/login/')
def search(request):
    form = SearchForm(request.POST)
    if request.method == 'POST' :
        date_search = request.POST['date_search']
        month_search = request.POST['month_search']
        year_search = request.POST['year_search']
        hmc_search = request.POST['hmc_search']

        if date_search != "" and month_search != "" and year_search != "":
            search_results = Shift.objects.filter(date__date__day = date_search).filter(date__date__month = month_search).filter(date__date__year = year_search).filter(hmc_number = hmc_search).order_by('date__date','shift')
        elif date_search != "" and month_search != "" and year_search == "":
            search_results = Shift.objects.filter(date__date__day = date_search).filter(date__date__month = month_search).filter(hmc_number = hmc_search).order_by('date__date','shift')
        elif date_search != "" and month_search == "" and year_search != "":
            search_results = Shift.objects.filter(date__date__day = date_search).filter(date__date__year = year_search).filter(hmc_number = hmc_search).order_by('date__date','shift')
        elif date_search != "" and month_search == "" and year_search == "":
            search_results = Shift.objects.filter(date__date__day = date_search).filter(hmc_number = hmc_search).order_by('date__date','shift')
        elif date_search == "" and month_search != "" and year_search != "":
            search_results = Shift.objects.filter(date__date__month = month_search).filter(date__date__year = year_search).filter(hmc_number = hmc_search).order_by('date__date','shift')
        elif date_search == "" and month_search != "" and year_search == "":
            search_results = Shift.objects.filter(date__date__month = month_search).filter(hmc_number = hmc_search).order_by('date__date','shift')
        elif date_search == "" and month_search == "" and year_search != "":
            search_results = Shift.objects.filter(date__date__year = year_search).filter(hmc_number = hmc_search).order_by('date__date','shift')
        else:
            search_results = []
        if search_results:
            context = {'search_results': search_results}
            return render(request, 'search_result.html', context)
        else:
            return render(request,'message.html',{'message':"No data for given parameters exists."})
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form})

@login_required(login_url = '/account/login/')
def generate_report(request):
    form = ReportGenerationForm(request.POST)
    if request.method == 'POST':
        month_search = request.POST['month_search']
        reason_search = request.POST['reason_search']
        year_search = request.POST['year_search']
        hmc_search = request.POST['hmc_search']

        if month_search == "":
            search_results = Slot.objects.filter(reason = reason_search).filter(shift__date__date__year=year_search).filter(shift__hmc_number = hmc_search)
        else:
            search_results = Slot.objects.filter(reason = reason_search).filter(shift__date__date__year = year_search).filter(shift__hmc_number = hmc_search)
            search_results = search_results.filter(shift__date__date__month = month_search).order_by('shift__date__date')

        res = []
        for slot in search_results:
            data = [slot.shift.date.date.strftime("%d.%m.%Y"), slot.time_slot_start.strftime("%H:%M"), slot.time_slot_stop.strftime("%H:%M"), round(slot.total_time(), 2), slot.reason, slot.remark]
            res.append(data)
        if res:
            context = {'res': res}
            return render(request, 'report_generation_result.html', context)
        else:
            return render(request,'message.html',{'message':"No data for given parameters exists."})
    else:
        form = ReportGenerationForm()

    return render(request, 'report_generation.html', {'form': form})

# Make sure that there is only one vessel in a single shift
@login_required(login_url = '/account/login/')
def vesselwise_tonnage(request):
    form = VesselwiseTonnageForm(request.POST)

    if request.method == 'POST':
        year_search = request.POST['year_search']
        hmc_search = request.POST['hmc_search']
        month_search = request.POST['month_search']

        shifts = Shift.objects.filter(date__date__year = year_search).filter(date__date__month = month_search).filter(hmc_number = hmc_search).order_by('date__date')

        res = []
        vessels = set()
        last_date = dict()

        for shift in shifts:
            if shift.slot_set.all():
                slot = shift.slot_set.all()[0]
                if slot.vessel_set.all():
                    vessel = slot.vessel_set.all()[0]
                    vessels.add(vessel.vessel_name)

        for vessel_name in vessels:
            # data = [trip, vessel_name, tonnage, cargo, diesel_consumed, diesel_hours]
            trip = 1
            tonnage = 0
            cargo = 0
            diesel_consumed = 0
            diesel_hours = 0
            for i in range(len(shifts)):
                if shifts[i].slot_set.all():
                    slot = shifts[i].slot_set.all()[0]
                    if slot.vessel_set.all():
                        vessel = slot.vessel_set.all()[0]
                        if vessel.vessel_name == vessel_name:
                            if vessel_name in last_date and shifts[i].date.date - last_date[vessel_name] > datetime.timedelta(7):
                                data = [trip, vessel_name, tonnage, cargo, diesel_consumed, diesel_hours]
                                res.append(data)
                                trip += 1
                                tonnage = 0
                                cargo = 0
                                diesel_consumed = 0
                                diesel_hours = 0
                            tonnage += shifts[i].total_tonnage_or_boxes
                            cargo = shifts[i].slot_set.all()[0].vessel_set.all()[0].vessel_cargo
                            diesel_consumed += shifts[i].diesel_consumed()
                            diesel_hours += shifts[i].diesel_hours()
                            last_date[vessel_name] = shifts[i].date.date
            data = [trip, vessel_name, tonnage, cargo, diesel_consumed, diesel_hours]
            res.append(data)
        res.sort(key = operator.itemgetter(0))
        if res:
            context = {'res': res}
            return render(request, 'vesselwise_tonnage_result.html', context)
        else:
            return render(request,'message.html',{'message':"No data for given parameters exists."})
    else:
        form = ReportGenerationForm()

    return render(request, 'vesselwise_tonnage.html', {'form': form})
