import streamlit as st



# Define pages
dashboard = st.Page("report/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True)
sales = st.Page("report/sales.py", title="Sales & Revenue", icon=":material/euro:")
customer = st.Page("report/customer.py", title="Customer", icon=":material/group:")
product = st.Page("report/product.py", title="Product", icon=":material/category:")


# Navigation
pg = st.navigation(
    {
        "Reports": [dashboard, sales, customer, product],
    }
)

pg.run()
