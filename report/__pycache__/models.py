import datetime
from django.db import models
from django.contrib.auth.models import User

# EPS is the epsilon value to check if two float values are equal or not
EPS = pow(10, -9)

# Returns (boolean). Checks whether two float values are equal or not. If the absolute value of their difference is less than EPS (declared at top) then they are equal
def is_equal(a, b):
    return abs(a - b) < EPS

class Date(models.Model):
    date = models.DateField('Date', null = True)

    def __str__(self):
        date = str(self.date)
        return date

    # For HMC 1 ****************************************************************************************

    # Returns (float) the holiday (H) time (in hrs) for the day
    def H_1(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 1:
                for slot in shift.slot_set.all():
                    if slot.reason == "H":
                        res += slot.total_time()
        return res

    # Returns (float) the strike (S) time (in hrs) for the day
    def S_1(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 1:
                for slot in shift.slot_set.all():
                    if slot.reason == "S":
                        res += slot.total_time()
        return res

    # Returns (float) the no-vehicle (NV) time (in hrs) for the day
    def NV_1(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 1:
                for slot in shift.slot_set.all():
                    if slot.reason == "NV":
                        res += slot.total_time()
        return res

    # Returns (float) the no-booking (NB) time (in hrs) for the day
    def NB_1(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 1:
                for slot in shift.slot_set.all():
                    if slot.reason == "NB":
                        res += slot.total_time()
        return res

    # Returns (float) the no-cargo (NC) time (in hrs) for the day
    def NC_1(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 1:
                for slot in shift.slot_set.all():
                    if slot.reason == "NC":
                        res += slot.total_time()
        return res

    # Returns (float) the travelling (TR) time (in hrs) for the day
    def TR_1(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 1:
                for slot in shift.slot_set.all():
                    if slot.reason == "TR":
                        res += slot.total_time()
        return res

    # Returns (float) the fixing-hatch (FH) time (in hrs) for the day
    def FH_1(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 1:
                for slot in shift.slot_set.all():
                    if slot.reason == "FH":
                        res += slot.total_time()
        return res

    # Returns (float) the remove-hatch (RH) time (in hrs) for the day
    def RH_1(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 1:
                for slot in shift.slot_set.all():
                    if slot.reason == "RH":
                        res += slot.total_time()
        return res

    # Returns (float) the no-trailer (NT) time (in hrs) for the day
    def NT_1(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 1:
                for slot in shift.slot_set.all():
                    if slot.reason == "NT":
                        res += slot.total_time()
        return res

    # Returns (float) the no-operation (NO) time (in hrs) for the day
    def NO_1(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 1:
                for slot in shift.slot_set.all():
                    if slot.reason == "NO":
                        res += slot.total_time()
        return res

    # Returns (float) the miscellaneous (MISC) time (in hrs) for the day
    def MISC_1(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 1:
                for slot in shift.slot_set.all():
                    if slot.reason == "MISC":
                        res += slot.total_time()
        return res

    # Returns (float) the breakdown (BD) time (in hrs) for the day
    def BD_1(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 1:
                for slot in shift.slot_set.all():
                    if slot.reason == "BD":
                        res += slot.total_time()
        return res

    # Returns (float) the maintenance (M) time (in hrs) for the day
    def M_1(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 1:
                for slot in shift.slot_set.all():
                    if slot.reason == "M":
                        res += slot.total_time()
        return res

    # Returns (int) the total available time (in hours) for the day
    def hours_available_for_the_day_1(self):
        return 24

    # Returns (float) the holiday and off time (in hours) for the day
    def holiday_and_off_1(self):
        return self.H_1()

    # Returns (float) the strike time (in hours) for the day
    def strike_1(self):
        return self.S_1()

    # Returns (float) the other time (in hours) for the day
    def other_1(self):
        return 0

    # Returns (float) the total of holiday, strike, and other time (in hours) for the day
    def total_3_to_5_1(self):
        return self.holiday_and_off_1() + self.strike_1() + self.other_1()

    # Returns (float) the total time (in hours) available for working for the day
    def hours_available_for_working_1(self):
        return self.hours_available_for_the_day_1() - self.total_3_to_5_1()

    # Returns (float) the no-vessel time (in hours) for the day
    def no_vessel_1(self):
        return self.NV_1()

    # Returns (float) the no-booking time (in hours) for the day
    def no_booking_1(self):
        return self.NB_1()

    # Returns (float) the no-cargo time (in hours) for the day
    def no_cargo_1(self):
        return self.NC_1()

    # Returns (float) the total of travelling, fixing-hatch, removing-hatch, no-trailer, no-operation, and miscellaneous time (in hours) for the day
    def others_port_users_account_1(self):
        return self.TR_1() + self.FH_1() + self.RH_1() + self.NT_1() + self.NO_1() + self.MISC_1()

    # Returns (float) the total time due to all reasons (in hours) for the day
    def total_8_to_11_1(self):
        return self.no_vessel_1() + self.no_booking_1() + self.no_cargo_1() + self.others_port_users_account_1()

    # Returns (float) the breakdown time (in hours) for the day
    def actual_available_working_hours_1(self):
        return self.hours_available_for_working_1() - self.total_8_to_11_1()

    # Returns (float) the breakdown time (in hours) for the day
    def breakdown_repairs_1(self):
        return self.BD_1()

    # Returns (float) the maintenance time (in hours) for the day
    def maintenance_1(self):
        return self.M_1()

    # Returns (float) the total of breakdown time (in hours) for the day
    def total_13_to_14_1(self):
        return self.breakdown_repairs_1() + self.maintenance_1()

    def HMC_availability_hours_1(self):
        return self.hours_available_for_the_day_1() - self.total_13_to_14_1()

    def effective_working_hours_1(self):
        return self.actual_available_working_hours_1() - self.total_13_to_14_1()

    def HMC_availability_percentage_1(self):
        return 100 * self.HMC_availability_hours_1() / self.hours_available_for_the_day_1()

    def operational_utilization_percentage_1(self):
        return 100 * self.effective_working_hours_1() / self.actual_available_working_hours_1()

    # Returns (float) the cumulative breakdown time for the month
    def cumulative_breakdown_monthwise_1(self):
        dates = Date.objects.filter(date__month = self.date.month).filter(date__day__lte = self.date.day).order_by('date')
        return sum([date.BD_1() for date in dates])

    def cumulative_available_hours_1(self):
        dates = Date.objects.filter(date__month = self.date.month).filter(date__day__lte = self.date.day).order_by('date')
        return sum([date.hours_available_for_the_day_1() for date in dates])

    def cumulative_ewt_1(self):
        dates = Date.objects.filter(date__month = self.date.month).filter(date__day__lte = self.date.day).order_by('date')
        return sum([date.effective_working_hours_1() for date in dates])

    def cumulative_percentage_utilization_1(self):
        return 100 * self.cumulative_ewt_1() / self.cumulative_available_hours_1()

    def cumulative_HMC_availability_hours_1(self):
        dates = Date.objects.filter(date__month = self.date.month).filter(date__day__lte = self.date.day).order_by('date')
        return sum([date.HMC_availability_hours_1() for date in dates])

    def cumulative_percentage_availability_1(self):
        return 100 * self.cumulative_HMC_availability_hours_1() / self.cumulative_available_hours_1()

    def cumulative_actual_available_working_time_1(self):
        dates = Date.objects.filter(date__month = self.date.month).filter(date__day__lte = self.date.day).order_by('date')
        return sum([date.actual_available_working_hours_1() for date in dates])

    def cumulative_percentage_opt_utilization_1(self):
        return 100 * self.cumulative_ewt_1() / self.cumulative_actual_available_working_time_1()

    # For HMC 2 ****************************************************************************************

    # Returns (float) the holiday (H) time (in hrs) for the day
    def H_2(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 2:
                for slot in shift.slot_set.all():
                    if slot.reason == "H":
                        res += slot.total_time()
        return res

    # Returns (float) the strike (S) time (in hrs) for the day
    def S_2(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 2:
                for slot in shift.slot_set.all():
                    if slot.reason == "S":
                        res += slot.total_time()
        return res

    # Returns (float) the no-vehicle (NV) time (in hrs) for the day
    def NV_2(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 2:
                for slot in shift.slot_set.all():
                    if slot.reason == "NV":
                        res += slot.total_time()
        return res

    # Returns (float) the no-booking (NB) time (in hrs) for the day
    def NB_2(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 2:
                for slot in shift.slot_set.all():
                    if slot.reason == "NB":
                        res += slot.total_time()
        return res

    # Returns (float) the no-cargo (NC) time (in hrs) for the day
    def NC_2(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 2:
                for slot in shift.slot_set.all():
                    if slot.reason == "NC":
                        res += slot.total_time()
        return res

    # Returns (float) the travelling (TR) time (in hrs) for the day
    def TR_2(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 2:
                for slot in shift.slot_set.all():
                    if slot.reason == "TR":
                        res += slot.total_time()
        return res

    # Returns (float) the fixing-hatch (FH) time (in hrs) for the day
    def FH_2(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 2:
                for slot in shift.slot_set.all():
                    if slot.reason == "FH":
                        res += slot.total_time()
        return res

    # Returns (float) the remove-hatch (RH) time (in hrs) for the day
    def RH_2(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 2:
                for slot in shift.slot_set.all():
                    if slot.reason == "RH":
                        res += slot.total_time()
        return res

    # Returns (float) the no-trailer (NT) time (in hrs) for the day
    def NT_2(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 2:
                for slot in shift.slot_set.all():
                    if slot.reason == "NT":
                        res += slot.total_time()
        return res

    # Returns (float) the no-operation (NO) time (in hrs) for the day
    def NO_2(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 2:
                for slot in shift.slot_set.all():
                    if slot.reason == "NO":
                        res += slot.total_time()
        return res

    # Returns (float) the miscellaneous (MISC) time (in hrs) for the day
    def MISC_2(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 2:
                for slot in shift.slot_set.all():
                    if slot.reason == "MISC":
                        res += slot.total_time()
        return res

    # Returns (float) the breakdown (BD) time (in hrs) for the day
    def BD_2(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 2:
                for slot in shift.slot_set.all():
                    if slot.reason == "BD":
                        res += slot.total_time()
        return res

    # Returns (float) the maintenance (M) time (in hrs) for the day
    def M_2(self):
        res = 0
        for shift in self.shift_set.all():
            if shift.hmc_number == 2:
                for slot in shift.slot_set.all():
                    if slot.reason == "M":
                        res += slot.total_time()
        return res

    # Returns (int) the total available time (in hours) for the day
    def hours_available_for_the_day_2(self):
        return 24

    # Returns (float) the holiday and off time (in hours) for the day
    def holiday_and_off_2(self):
        return self.H_2()

    # Returns (float) the strike time (in hours) for the day
    def strike_2(self):
        return self.S_2()

    # Returns (float) the other time (in hours) for the day
    def other_2(self):
        return 0

    # Returns (float) the total of holiday, strike, and other time (in hours) for the day
    def total_3_to_5_2(self):
        return self.holiday_and_off_2() + self.strike_2() + self.other_2()

    # Returns (float) the total time (in hours) available for working for the day
    def hours_available_for_working_2(self):
        return self.hours_available_for_the_day_2() - self.total_3_to_5_2()

    # Returns (float) the no-vessel time (in hours) for the day
    def no_vessel_2(self):
        return self.NV_2()

    # Returns (float) the no-booking time (in hours) for the day
    def no_booking_2(self):
        return self.NB_2()

    # Returns (float) the no-cargo time (in hours) for the day
    def no_cargo_2(self):
        return self.NC_2()

    # Returns (float) the total of travelling, fixing-hatch, removing-hatch, no-trailer, no-operation, and miscellaneous time (in hours) for the day
    def others_port_users_account_2(self):
        return self.TR_2() + self.FH_2() + self.RH_2() + self.NT_2() + self.NO_2() + self.MISC_2()

    # Returns (float) the total time due to all reasons (in hours) for the day
    def total_8_to_11_2(self):
        return self.no_vessel_2() + self.no_booking_2() + self.no_cargo_2() + self.others_port_users_account_2()

    # Returns (float) the breakdown time (in hours) for the day
    def actual_available_working_hours_2(self):
        return self.hours_available_for_working_2() - self.total_8_to_11_2()

    # Returns (float) the breakdown time (in hours) for the day
    def breakdown_repairs_2(self):
        return self.BD_2()

    # Returns (float) the maintenance time (in hours) for the day
    def maintenance_2(self):
        return self.M_2()

    # Returns (float) the total of breakdown time (in hours) for the day
    def total_13_to_14_2(self):
        return self.breakdown_repairs_2() + self.maintenance_2()

    def HMC_availability_hours_2(self):
        return self.hours_available_for_the_day_2() - self.total_13_to_14_2()

    def effective_working_hours_2(self):
        return self.actual_available_working_hours_2() - self.total_13_to_14_2()

    def HMC_availability_percentage_2(self):
        return 100 * self.HMC_availability_hours_2() / self.hours_available_for_the_day_2()

    def operational_utilization_percentage_2(self):
        return 100 * self.effective_working_hours_2() / self.actual_available_working_hours_2()

    # Returns (float) the cumulative breakdown time for the month
    def cumulative_breakdown_monthwise_2(self):
        dates = Date.objects.filter(date__month = self.date.month).filter(date__day__lte = self.date.day).order_by('date')
        return sum([date.BD_2() for date in dates])

    def cumulative_available_hours_2(self):
        dates = Date.objects.filter(date__month = self.date.month).filter(date__day__lte = self.date.day).order_by('date')
        return sum([date.hours_available_for_the_day_2() for date in dates])

    def cumulative_ewt_2(self):
        dates = Date.objects.filter(date__month = self.date.month).filter(date__day__lte = self.date.day).order_by('date')
        return sum([date.effective_working_hours_2() for date in dates])

    def cumulative_percentage_utilization_2(self):
        return 100 * self.cumulative_ewt_2() / self.cumulative_available_hours_2()

    def cumulative_HMC_availability_hours_2(self):
        dates = Date.objects.filter(date__month = self.date.month).filter(date__day__lte = self.date.day).order_by('date')
        return sum([date.HMC_availability_hours_2() for date in dates])

    def cumulative_percentage_availability_2(self):
        return 100 * self.cumulative_HMC_availability_hours_2() / self.cumulative_available_hours_2()

    def cumulative_actual_available_working_time_2(self):
        dates = Date.objects.filter(date__month = self.date.month).filter(date__day__lte = self.date.day).order_by('date')
        return sum([date.actual_available_working_hours_2() for date in dates])

    def cumulative_percentage_opt_utilization_2(self):
        return 100 * self.cumulative_ewt_2() / self.cumulative_actual_available_working_time_2()



class Shift(models.Model):
    date = models.ForeignKey(Date, on_delete = models.CASCADE)
    hmc_number = models.IntegerField(default = 1)
    shift = models.FloatField(default = 1)
    diesel_start_percentage = models.FloatField(default = 100)
    diesel_end_percentage = models.FloatField(default = 0)
    diesel_start_hours = models.FloatField(default = 0)
    diesel_end_hours = models.FloatField(default = 0)
    total_tonnage_or_boxes = models.FloatField(default = 0)
    cycles = models.FloatField(default = 0)
    user =  models.ForeignKey(User , on_delete= models.CASCADE)
    shift_end_flag = models.IntegerField(default = 0)

    def __str__(self):
        shift = str(self.shift)
        return shift

    # Returns the total diesel consumed
    def diesel_consumed(self):
        if self.hmc_number == 1:
            return (self.diesel_start_percentage - self.diesel_end_percentage) * 110
        else:
            return (self.diesel_start_percentage - self.diesel_end_percentage) * 130

    # Returns the diesel hours spent
    def diesel_hours(self):
        return self.diesel_end_hours - self.diesel_start_hours

    # Returns (float) the summation of total times for the shift
    def total_idle_time(self):
        return sum([slot.total_time() for slot in self.slot_set.all()])

    # Returns (float) the effective working time for the shift (out of total of 8 hrs)
    def ewt(self):
        return 8 - self.total_idle_time()

    # Returns (float) the tonnage (or boxes) per hour for the shift
    def tonnage_per_hour(self):
        # Checks division by 0
        if is_equal(self.ewt(), 0):
            return 0
        return self.total_tonnage_or_boxes / self.ewt()

    # Returns (float) the number of cyles / hour for the shift
    def cycles_per_hour(self):
        # Checks division by 0
        if is_equal(self.ewt(), 0):
            return 0
        return self.cycles / self.ewt();


class Slot(models.Model):
    shift = models.ForeignKey(Shift, on_delete = models.CASCADE)
    time_slot_start = models.TimeField('Time of start')
    time_slot_stop = models.TimeField('Time of stop')
    reason = models.CharField(default ='NO', max_length = 10)
    remark = models.CharField(default ='Nothing', max_length = 200)

    def __str__(self):
        time_start = str(self.time_slot_start)
        return time_start

    def get_time_slot_start(self):
        return self.time_slot_start.strftime("%H:%M")

    def get_time_slot_stop(self):
        return self.time_slot_stop.strftime("%H:%M")

    # Returns (float) total time for the slot
    def total_time(self):
        t_start = datetime.timedelta(hours = self.time_slot_start.hour, minutes = self.time_slot_start.minute)
        t_stop = datetime.timedelta(hours = self.time_slot_stop.hour, minutes = self.time_slot_stop.minute)
        h = (t_stop - t_start).total_seconds() / 3600
        return h


class Vessel(models.Model):
    slot = models.ForeignKey(Slot, on_delete = models.CASCADE)
    vessel_name = models.CharField(default = 'None', max_length = 100)
    vessel_cargo = models.CharField(default = 'None', max_length = 100)
    berth_number = models.IntegerField(default = 1)

    def __str__(self):
        return self.vessel_name
