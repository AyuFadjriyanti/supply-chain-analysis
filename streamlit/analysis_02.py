import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

# ======================
# CONFIG
# ======================
st.set_page_config(page_title="Supply Chain Dashboard", layout="wide")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

px.defaults.template = "plotly_white"
px.defaults.color_discrete_sequence = px.colors.qualitative.Set2

# ======================
# LOAD DATA
# ======================
df = pd.read_csv("clean_supply_chain.csv")

# ======================
# FEATURE ENGINEERING
# ======================
df['total_lead_time'] = (
    df['order_lead_time'] +
    df['shipping_times'] +
    df['manufacturing_lead_time']
)

df['is_late'] = (df['shipping_times'] > df['shipping_times'].median()).astype(int)

df['stock_gap'] = df['stock_levels'] - df['number_of_products_sold']

df['revenue_per_unit'] = df['revenue_generated'] / df['number_of_products_sold']
df['cost_per_unit'] = df['total_cost'] / df['number_of_products_sold']

df['demand_segment'] = pd.qcut(
    df['number_of_products_sold'],
    3,
    labels=['Low','Medium','High']
)

df['daily_demand'] = df['number_of_products_sold'] / 30
df['stock_aging_days'] = df['stock_levels'] / df['daily_demand']

# ======================
# HEADER
# ======================
col1, col2 = st.columns([0.1, 0.9])

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3082/3082031.png", width=80)

with col2:
    st.markdown("""
        <h1>Supply Chain Analytics Dashboard</h1>
        <p>Lead Time • Inventory • Supplier Performance</p>
    """, unsafe_allow_html=True)

st.write(f"Last Updated: {datetime.datetime.now().strftime('%d %B %Y')}")

# ======================
# FILTER
# ======================
st.subheader("Filter Data")

f1, f2, f3, f4 = st.columns(4)

with f1:
    supplier_options = ["Select All"] + sorted(df['supplier_name'].unique())
    selected_supplier = st.multiselect("Supplier", supplier_options, default=["Select All"])

    if "Select All" in selected_supplier:
        supplier_filter = df['supplier_name'].unique()
    else:
        supplier_filter = selected_supplier

with f2:
    transport_filter = st.multiselect(
        "Transport Mode",
        df['transportation_modes'].unique(),
        default=df['transportation_modes'].unique()
    )

with f3:
    inspection_filter = st.multiselect(
        "Inspection",
        df['inspection_results'].unique(),
        default=df['inspection_results'].unique()
    )

with f4:
    segment_filter = st.multiselect(
        "Demand Segment",
        df['demand_segment'].unique(),
        default=df['demand_segment'].unique()
    )

filtered_df = df[
    (df['supplier_name'].isin(supplier_filter)) &
    (df['transportation_modes'].isin(transport_filter)) &
    (df['inspection_results'].isin(inspection_filter)) &
    (df['demand_segment'].isin(segment_filter))
]

# ======================
# KPI
# ======================
st.subheader("Key Metrics")

k1, k2, k3, k4, k5, k6, k7 = st.columns(7)

k1.metric("Revenue", f"{filtered_df['revenue_generated'].sum():,.0f}")
k2.metric("Cost", f"{filtered_df['total_cost'].sum():,.0f}")
k3.metric("Late Rate", f"{filtered_df['is_late'].mean()*100:.1f}%")
k4.metric("Avg Lead Time", f"{filtered_df['total_lead_time'].mean():.1f}")
k5.metric("Avg Shipping", f"{filtered_df['shipping_times'].mean():.1f}")
k6.metric("Rev/Unit", f"{filtered_df['revenue_per_unit'].mean():.2f}")
k7.metric("Cost/Unit", f"{filtered_df['cost_per_unit'].mean():.2f}")

st.divider()

# ======================
# SUPPLIER PERFORMANCE
# ======================
supplier_perf = filtered_df.groupby('supplier_name').agg({
    'is_late':'mean',
    'shipping_times':'mean',
    'total_cost':'mean'
}).reset_index()

color_map_supplier = {
    s: px.colors.qualitative.Set2[i % 8]
    for i, s in enumerate(supplier_perf['supplier_name'])
}

c1, c2, c3 = st.columns(3)

with c1:
    st.plotly_chart(
        px.bar(supplier_perf, x='supplier_name', y='is_late',
               color='supplier_name', color_discrete_map=color_map_supplier,
               title="Late Rate by Supplier"),
        use_container_width=True
    )

with c2:
    st.plotly_chart(
        px.bar(supplier_perf, x='supplier_name', y='shipping_times',
               color='supplier_name', color_discrete_map=color_map_supplier,
               title="Shipping Time by Supplier"),
        use_container_width=True
    )

with c3:
    st.plotly_chart(
        px.bar(supplier_perf, x='supplier_name', y='total_cost',
               color='supplier_name', color_discrete_map=color_map_supplier,
               title="Cost by Supplier"),
        use_container_width=True
    )

# ======================
# TRANSPORT
# ======================
transport_perf = filtered_df.groupby('transportation_modes').agg({
    'shipping_times':'mean',
    'total_cost':'mean'
}).reset_index()

c1, c2 = st.columns(2)

with c1:
    st.plotly_chart(
        px.bar(transport_perf, x='transportation_modes', y='shipping_times',
               color='transportation_modes',
               title="Shipping Time by Mode"),
        use_container_width=True
    )

with c2:
    st.plotly_chart(
        px.bar(transport_perf, x='transportation_modes', y='total_cost',
               color='transportation_modes',
               title="Cost by Mode"),
        use_container_width=True
    )

# ======================
# INVENTORY
# ======================
top_risk = filtered_df.nsmallest(10, 'stock_gap')

c1, c2 = st.columns(2)

with c1:
    st.plotly_chart(
        px.bar(top_risk, x='sku', y='stock_gap',
               color='sku',
               title="Top Stockout Risk"),
        use_container_width=True
    )

with c2:
    st.dataframe(top_risk[['sku','stock_gap','stock_aging_days']])

st.divider()

# ======================
# COST vs PERFORMANCE
# ======================
c1, c2 = st.columns(2)

with c1:
    st.plotly_chart(
        px.scatter(filtered_df,
                   x='total_cost',
                   y='shipping_times',
                   color='defect_rates',
                   color_continuous_scale='Viridis',
                   title="Cost vs Shipping"),
        use_container_width=True
    )

with c2:
    st.plotly_chart(
        px.histogram(filtered_df,
                     x='total_lead_time',
                     color='demand_segment',
                     title="Lead Time Distribution"),
        use_container_width=True
    )

st.divider()

# ======================
# QUALITY
# ======================
quality = filtered_df.groupby('inspection_results').agg({
    'defect_rates':'mean',
    'total_cost':'mean'
}).reset_index()

st.plotly_chart(
    px.bar(quality,
           x='inspection_results',
           y='defect_rates',
           color='defect_rates',
           color_continuous_scale='Reds',
           title="Defect Rate"),
    use_container_width=True
)

# ======================
# CORRELATION
# ======================
st.subheader("Correlation Analysis")

corr = filtered_df[['shipping_times','total_cost','defect_rates','total_lead_time']].corr()

st.plotly_chart(px.imshow(corr, text_auto=True),
                use_container_width=True)

# ======================
# SEGMENTATION
# ======================
st.subheader("Demand Segment Analysis")

seg = filtered_df.groupby('demand_segment')['revenue_generated'].sum().reset_index()

st.plotly_chart(
    px.bar(seg,
           x='demand_segment',
           y='revenue_generated',
           color='demand_segment',
           title="Revenue by Segment"),
    use_container_width=True
)

# ======================
# RAW DATA
# ======================
with st.expander("View Raw Data"):
    st.dataframe(filtered_df)

csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("Download Data", csv, "supply_chain.csv", "text/csv")