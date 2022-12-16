# Functions for tipout calculator
def total(a, b, c, d):
    total = a + b + c + d
    return total

# calculates barback tips
def barback_tips(total_tips, bar_back_tip_percent):
    barback = round(total_tips * bar_back_tip_percent / 100, 2)
    return barback



# calculates foodrunner tips
def foodrunner(food_sales, runner_percentage):
    food_runner = 0
    food_runner = food_runner + (food_sales * runner_percentage / 100)
    return food_runner


# calculates hourly rate
def hourly_rate(total_money, total_hours):

    hourly = float(round(total_money / total_hours, 2))
    return hourly


# calculates if Bartenders need to tip each other so taxation is equal
def bartender_tipout(cc_tips, emp_total_tips):
    if cc_tips - emp_total_tips > 0:
        return f"Tip out {cc_tips - emp_total_tips}"
    else:
        return f"Receive {emp_total_tips - cc_tips}"





























