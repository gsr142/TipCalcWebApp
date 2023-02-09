import streamlit as st
import functions as fn

st.subheader("Ensure everyone gets paid and taxed properly based on hours worked")

# Columned Inputs


col1, col2 = st.columns(2)
with col1:
    bt1_cc_tips = st.number_input(label="Bartender 1 credit tips")
    bt2_cc_tips = st.number_input(label="Bartender 2 credit tips")
    bt3_cc_tips = st.number_input(label="Bartender 3 credit tips")
    bt4_cc_tips = st.number_input(label="Bartender 4 credit tips")
    food_sales = st.number_input(label="Enter food sales")
    total_tips = st.number_input(label="Total tips (charge + cash)")
with col2:
    bt1_hours_worked = st.number_input(label="Bartender 1 hours worked")
    bt2_hours_worked = st.number_input(label="Bartender 2 hours worked")
    bt3_hours_worked = st.number_input(label="Bartender 3 hours worked")
    bt4_hours_worked = st.number_input(label="Bartender 4 hours worked")
    food_runner_percentage = st.number_input(
        label="Enter food runner tip percentage (0 if no food runner)")
    bar_back_percentage = st.number_input(
        label="Enter barback tip percentage (0 if no barback)")

# Totals
total_cc_tips = fn.total(bt1_cc_tips, bt2_cc_tips, bt3_cc_tips, bt4_cc_tips)
total_hours = fn.total(bt1_hours_worked, bt2_hours_worked, bt3_hours_worked,
                       bt4_hours_worked)

# Calculate button runs code for calculations
if st.button(label="Calculate Tipout"):
    # Barback Payout
    if total_hours <= 0 or bt1_hours_worked <= 0 or bt2_hours_worked <= 0:
        st.write("Please complete the form for at least 2 bartenders")
        exit()
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
    cc_total_after_tipout = float(total_cc_tips - food_runner_payout - bar_back_payout)
    st.write(f"cc tips after support tipout are ${cc_total_after_tipout}")
    cc_hourly = float(total_cc_tips / total_hours)
    st.write(f"cc hourly rate is ${cc_hourly.round(2)}")

    hourly_rate = float(fn.hourly_rate(total_after_tipouts, total_hours))
    st.write(f"actual hourly rate is ${hourly_rate}")
    # Bartender take home

    try:
        bt1_take_home = float(hourly_rate * bt1_hours_worked)
        bt1_cc_hourly = float(bt1_hours_worked * cc_hourly)
        st.write(f"Bartender 1 takes home ${bt1_take_home}")

        bt2_take_home = float(hourly_rate * bt2_hours_worked)
        bt2_cc_hourly = float(bt2_hours_worked * cc_hourly)
        st.write(f"Bartender 2 takes home ${bt2_take_home}")

        bt3_take_home = float(hourly_rate * bt3_hours_worked)
        bt3_cc_hourly = float(bt3_hours_worked * cc_hourly)
        if bt3_take_home > 0:
            st.write(f"Bartender 3 takes home ${bt3_take_home}")

        bt4_take_home = float(hourly_rate * bt4_hours_worked)
        bt4_cc_hourly = float(bt4_hours_worked * cc_hourly)
        if bt4_take_home > 0:
            st.write(f"Bartender 4 takes home ${bt4_take_home}")
    except NameError:
        st.write("Please complete the form for at least 2 bartenders")
        exit()

    # Bartender tipout to each other


    if bt1_cc_hourly <= bt1_cc_tips:
        st.write(f"Bartender 1 tips out ${round(bt1_cc_tips - bt1_cc_hourly, 2)}")
    elif bt1_cc_hourly > bt1_cc_tips:
        st.write(f"Bartender 1 receives ${round(bt1_cc_hourly - bt1_cc_tips, 2)}")


    if bt2_cc_hourly <= bt2_cc_tips:
        st.write(f"Bartender 2 tips out ${round(bt2_cc_tips - bt2_cc_hourly, 2)}")
    elif bt2_cc_hourly > bt2_cc_tips:
        st.write(f"Bartender 2 receives ${round(bt2_cc_hourly - bt2_cc_tips, 2)}")


    if bt3_cc_hourly > 0:
        if bt3_cc_hourly <= bt3_cc_tips:
            st.write(f"Bartender 3 tips out ${round(bt3_cc_tips - bt3_cc_hourly, 2)}")
        elif bt3_cc_hourly > bt3_cc_tips:
            st.write(f"Bartender 3 receives ${round(bt3_cc_hourly - bt3_cc_tips, 2)}")


    if bt4_cc_hourly > 0:
        if bt4_cc_hourly <= bt4_cc_tips:
            st.write(f"Bartender 4 tips out ${round(bt4_cc_tips - bt4_cc_hourly, 2)}")
        elif bt4_cc_hourly > bt4_cc_tips:
            st.write(f"Bartender 4 receives ${round(bt4_cc_hourly - bt4_cc_tips, 2)}")