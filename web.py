import streamlit as st
import functions as fn

st.subheader("Ensure everyone gets paid and taxed properly based on hours worked")

# Bartender inputs
bt1_cc_tips = st.number_input(label="Bartender 1 credit tips")
bt1_hours_worked = st.number_input(label="Bartender 1 hours worked")

bt2_cc_tips = st.number_input(label="Bartender 2 credit tips")
bt2_hours_worked = st.number_input(label="Bartender 2 hours worked")

bt3_cc_tips = st.number_input(label="Bartender 3 credit tips")
bt3_hours_worked = st.number_input(label="Bartender 3 hours worked")

bt4_cc_tips = st.number_input(label="Bartender 4 credit tips")
bt4_hours_worked = st.number_input(label="Bartender 4 hours worked")

# Bar back inputs

bar_back_percentage = st.number_input(
    label="Enter barback tip percentage (leave as 0 if no barback)")

# Food runner inputs

food_sales = st.number_input(label="Enter food sales")
food_runner_percentage = st.number_input(
    label="Enter food runner tip percentage (leave as 0 if no food runner)")

# Totals
total_cc_tips = fn.total(bt1_cc_tips, bt2_cc_tips, bt3_cc_tips, bt4_cc_tips)
total_hours = fn.total(bt1_hours_worked, bt2_hours_worked, bt3_hours_worked,
                       bt4_hours_worked)
total_tips = st.number_input(label="Total tips (charge + cash)")

if st.button(label="Calculate Tipout"):
    # Barback Payout

    bar_back_payout = float(round(fn.barback_tips(total_tips, bar_back_percentage), 2))
    bar_back_hourly = float(round(bar_back_payout / total_hours, 2))

    bar1_to_barback = float(round(bar_back_hourly * bt1_hours_worked, 2))
    if bar1_to_barback > 0:
        st.write(f"Barback receives ${bar1_to_barback} from Bartender 1")

    bar2_to_barback = float(round(bar_back_hourly * bt2_hours_worked, 2))
    if bar2_to_barback > 0:
        st.write(f"Barback receives ${bar2_to_barback} from Bartender 2")

    bar3_to_barback = float(round(bar_back_hourly * bt3_hours_worked, 2))
    if bar3_to_barback > 0:
        st.write(f"Barback receives ${bar3_to_barback} from Bartender 3")

    bar4_to_barback = float(round(bar_back_hourly * bt4_hours_worked, 2))
    if bar4_to_barback > 0:
        st.write(f"Barback receives ${bar4_to_barback} from Bartender 4")

    if bar_back_payout > 0:
        st.write(f"Barback receives a total of ${bar_back_payout}")

    # Food Runner Pay
    food_runner_payout = float(fn.foodrunner(food_sales, food_runner_percentage))
    if food_runner_payout > 0:
        st.write(f"Food runner receives ${food_runner_payout}")



    # Bartenders Hourly rate
    total_after_tipouts = float(total_tips - food_runner_payout - bar_back_payout)
    try:
        cc_hourly = fn.hourly_rate(total_cc_tips, total_hours)
    except ZeroDivisionError:
        st.write("Please enter employee hours")

    try:
        hourly_rate = fn.hourly_rate(total_after_tipouts, total_hours)
    except ZeroDivisionError:
        st.write("for at least bartenders 1 and 2")
    # Bartender take home

    try:
        bt1_take_home = float(round(hourly_rate * bt1_hours_worked, 2))
        st.write(f"Bartender 1 takes home ${bt1_take_home}")

        bt2_take_home = float(round(hourly_rate * bt2_hours_worked, 2))
        st.write(f"Bartender 2 takes home ${bt2_take_home}")

        bt3_take_home = float(round(hourly_rate * bt3_hours_worked, 2))
        if bt3_take_home > 0:
            st.write(f"Bartender 3 takes home ${bt3_take_home}")

        bt4_take_home = float(round(hourly_rate * bt4_hours_worked, 2))
        if bt4_take_home > 0:
            st.write(f"Bartender 4 takes home ${bt4_take_home}")
    except NameError:
        st.write("or the calculator will not work for you")



