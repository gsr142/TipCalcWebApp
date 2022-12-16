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
bar_back_present = st.text_input(label="Was there a barback? Enter y or n")
bar_back_percentage = st.number_input(label="Enter barback tip percentage")

# Food runner inputs
food_runner_present = st.text_input(label="Was there a food runner? Enter y or n")
food_sales = st.number_input(label="Enter food sales")
food_runner_percentage = st.number_input(label="Enter food runner tip percentage")

# Totals
total_cc_tips = fn.total(bt1_cc_tips, bt2_cc_tips, bt3_cc_tips, bt4_cc_tips)
total_hours = fn.total(bt1_hours_worked, bt2_hours_worked, bt3_hours_worked,
                       bt4_hours_worked)
total_tips = st.number_input(label="Total tips")

if st.button(label="Calculate Tipout"):
    # Barback Payout
    bar_back_payout = []
    bar_back_tips = bar_back_payout
    if bar_back_present.startswith("y") or bar_back_present.startswith("Y"):
        if bt3_hours_worked == 0 and bt4_hours_worked == 0:
            bar_back_payout = fn.barback_tips_2(total_tips, bar_back_percentage,
                                                     total_hours, bt1_hours_worked,
                                                     bt2_hours_worked)
        elif bt4_hours_worked == 0:
            bar_back_payout = fn.barback_tips_3(total_tips, bar_back_percentage,
                                                     total_hours, bt1_hours_worked,
                                                     bt2_hours_worked, bt3_hours_worked)
        else:
            bar_back_payout = fn.barback_tips_4(total_tips, bar_back_percentage,
                                                     total_hours, bt1_hours_worked,
                                                     bt2_hours_worked, bt3_hours_worked,
                                                     bt4_hours_worked)

    # Food Runner Pay
    food_runner_payout = fn.foodrunner(food_runner_present, food_sales,
                                       food_runner_percentage)

    # Bartenders Hourly rate
    total_after_tipouts = total_tips - food_runner_payout - bar_back_tips
    hourly_rate = fn.hourly_rate(total_after_tipouts, total_hours, bt1_hours_worked,
                                 bt2_hours_worked, bt3_hours_worked,
                                 bt4_hours_worked)







