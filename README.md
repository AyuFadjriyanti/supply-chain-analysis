# Supply Chain Operations Analysis & Dashboard

## Project Overview

This project analyzes a simulated supply chain dataset to identify inefficiencies across **supplier performance, logistics strategy, and inventory management**.

The project combines **Exploratory Data Analysis (EDA)** and an **Interactive Streamlit Dashboard** to translate raw operational data into actionable business insights.

## Business Context

In supply chain operations, inefficiencies in delivery, supplier reliability, and inventory planning can lead to:

- High late delivery rates
- Stockouts and lost sales
- Inefficient logistics costs

This project aims to diagnose these issues and provide **data-driven optimization strategies**.

## Objectives

- Evaluate supplier reliability and late delivery patterns
- Analyze transportation performance vs cost
- Identify high-risk inventory (stockout & overstock)
- Measure operational efficiency using unit economics

## Tools & Technologies

- Python (Pandas, NumPy)
- Data Visualization (Matplotlib, Plotly)
- Streamlit (Interactive Dashboard)
- Jupyter Notebook (EDA)

## Key Metrics

- Late Delivery Rate (~47%)
- Average Shipping Time (~5.7 days)
- Total Lead Time (~36 days)
- Stock Gap (inventory vs demand imbalance)
- Revenue per Unit & Cost per Unit

## Key Insights

- **High Late Delivery Rate (~47%)**
  → Indicates systemic inefficiency in supplier and logistics performance

- **No strong correlation between cost and shipping time**
  → Higher cost does not guarantee faster delivery → potential cost inefficiency

- **Severe Stockout Risk (~900–1000 units)**
  → Inventory planning is misaligned with demand

- **Transport Mode Trade-off**
  → Sea is cheapest but slowest  
  → Road is the fastest and most balanced option

- **Supplier Performance Variability (40%–52% late rate)**
  → Significant inconsistency → opportunity for supplier optimization

## 👉 [View Interactive Dashboard](https://supply-chain-analysis-drvawxydyr5mmjsywgevak.streamlit.app/)

This project includes an interactive dashboard to explore:

- Supplier performance comparison
- Transport mode efficiency
- Inventory risk analysis
- Cost vs performance relationship
- Demand segmentation

### Run Locally

```bash
streamlit run analysis_02.py
