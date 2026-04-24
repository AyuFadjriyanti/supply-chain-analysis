# Supply Chain Operations Analysis

## Overview

This project analyzes supply chain operations data to identify inefficiencies in **delivery performance, supplier reliability, transportation strategy, and inventory management**.

The analysis focuses on uncovering key operational bottlenecks and providing **data-driven recommendations** to improve overall efficiency and reduce risk.

## Objectives

* Evaluate supplier performance and delivery reliability
* Analyze the impact of transportation modes on shipping time
* Identify inventory risks (stockout & overstock)
* Assess cost efficiency in relation to operational performance

## Tools & Technologies

* Python (Pandas, NumPy)
* Data Visualization (Matplotlib)
* Jupyter Notebook / Google Colab

## Key Metrics

* **Late Delivery Rate (~50%)**
* **Average Shipping Time (1–10 days range)**
* **Total Lead Time (end-to-end process)**
* **Stock Gap (inventory vs demand)**
* **Cost per Unit & Revenue per Unit**

## Key Insights

* **No significant correlation between cost and delivery speed**, indicating inefficient logistics spending
* **Severe stockout risk (~1000 unit shortages)** across top SKUs, highlighting poor inventory planning
* **Transport mode significantly impacts delivery time**, with sea being ~50% slower than road
* **Supplier performance varies (40%–52% late rate)**, indicating inconsistency in reliability
* **High variability in lead time**, suggesting unstable supply chain performance

## Recommendations

### 1. Optimize Supplier Strategy

Rebalance supplier allocation by reducing reliance on high-delay vendors (>50% late rate) and shifting volume to more reliable suppliers

### 2. Strengthen Inventory Planning (High Priority)

Implement safety stock for high-demand SKUs and address critical stockout risks (up to ~1000 unit shortages)

### 3. Enhance Transport Strategy

Adopt a priority-based model: Road as default, Air for urgent deliveries, and Sea for low-priority shipments

### 4. Improve Cost Efficiency

Eliminate high-cost, low-performance shipments and optimize decisions based on cost-to-performance effectiveness

## Expected Impact

* Reduce late delivery rate to **<45%**
* Decrease stockout risk by **>70%**
* Improve delivery time by **1–2 days**
* Increase overall cost efficiency
