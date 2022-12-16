# Functions for tipout calculator
def total(a, b, c, d):
    total = a + b + c + d
    return total

# calculates barback tips
def barback_tips_2(total_tips, bar_back_tip_percent,
                 total_hours, emp_1_hours, emp_2_hours):

    barback = round(total_tips * bar_back_tip_percent/100, 2)

    barback_total_tipout = round(barback, 2)

    bartender1_tipout_barback = round((barback / total_hours) * emp_1_hours, 2)
    bartender2_tipout_barback = round((barback / total_hours) * emp_2_hours, 2)

    return [barback_total_tipout, bartender1_tipout_barback, bartender2_tipout_barback]

def barback_tips_3(total_tips, bar_back_tip_percent,
                 total_hours, emp_1_hours, emp_2_hours, emp_3_hours):

    barback = round(total_tips * bar_back_tip_percent / 100, 2)

    barback_total_tipout = round(barback, 2)

    bartender1_tipout_barback = round((barback / total_hours) * emp_1_hours, 2)
    bartender2_tipout_barback = round((barback / total_hours) * emp_2_hours, 2)
    bartender3_tipout_barback = round((barback / total_hours) * emp_3_hours, 2)
    return [barback_total_tipout, bartender1_tipout_barback,
            bartender2_tipout_barback, bartender3_tipout_barback]

def barback_tips_4(total_tips, bar_back_tip_percent,
                 total_hours, emp_1_hours, emp_2_hours, emp_3_hours, emp_4_hours):

    barback = round(total_tips * bar_back_tip_percent / 100, 2)

    barback_total_tipout = round(barback, 2)

    bartender1_tipout_barback = round((barback / total_hours) * emp_1_hours, 2)
    bartender2_tipout_barback = round((barback / total_hours) * emp_2_hours, 2)
    bartender3_tipout_barback = round((barback / total_hours) * emp_3_hours, 2)
    bartender4_tipout_barback = round((barback / total_hours) * emp_4_hours, 2)
    return [barback_total_tipout, bartender1_tipout_barback,
            bartender2_tipout_barback, bartender3_tipout_barback,
            bartender4_tipout_barback]


# calculates foodrunner tips
def foodrunner(runner, food_sales, runner_percentage):
    food_runner = 0
    if runner.startswith("y") or runner.startswith("Y"):
        food_runner = food_runner + (food_sales * runner_percentage / 100)
        return food_runner
    else:
        return food_runner

# calculates hourly rate
def hourly_rate(total_money, total_hours, emp_1_hours, emp_2_hours, emp_3_hours,
                emp_4_hours):
    hourly = total_money / total_hours
    emp_1_hourly = hourly * emp_1_hours
    emp_2_hourly = hourly * emp_2_hours
    emp_3_hourly = hourly * emp_3_hours
    emp_4_hourly = hourly * emp_4_hours
    return [hourly, emp_1_hourly, emp_2_hourly, emp_3_hourly, emp_4_hourly]

# calculates if Bartenders need to tip each other so taxation is equal
def bartender_tipout(cc_tips, emp_total_tips):
    if cc_tips - emp_total_tips > 0:
        return f"Tip out {cc_tips - emp_total_tips}"
    else:
        return f"Receive {emp_total_tips - cc_tips}"





























