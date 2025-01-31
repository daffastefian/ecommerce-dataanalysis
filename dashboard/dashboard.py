import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

merged_df = pd.read_csv('merged_data.csv')

st.title('E-commerce Data Analysis')

st.header('1. Sebaran Status Order')

order_status_counts = merged_df['order_status'].value_counts()

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=order_status_counts.index, y=order_status_counts.values, palette='pastel', ax=ax)
ax.set_title("Sebaran Status Order")
ax.set_xlabel("Status Order")
ax.set_ylabel("Jumlah Pesanan")
for i, value in enumerate(order_status_counts.values):
    ax.text(i, value + 0.1, str(value), ha='center', fontsize=12)
st.pyplot(fig)

st.header('2. Produk yang Paling Banyak Terjual')

top_products = merged_df['product_category'].value_counts().head(5)

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=top_products.values, y=top_products.index, palette='coolwarm', ax=ax)
ax.set_title("Produk yang Paling Banyak Terjual")
ax.set_xlabel("Jumlah Terjual")
ax.set_ylabel("Nama Produk")
st.pyplot(fig)

st.header('3. Produk dengan Revenue Tertinggi')

product_revenue = merged_df.groupby('product_category')['price'].sum().sort_values(ascending=False).head(5)

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=product_revenue.values, y=product_revenue.index, palette='Blues_r', ax=ax)
ax.set_title("Top 5 Produk dengan Revenue Tertinggi")
ax.set_xlabel("Total Revenue")
ax.set_ylabel("Nama Produk")
st.pyplot(fig)

st.header('4. Negara Bagian dengan Pelanggan Terbanyak')

top_states = merged_df['customer_state'].value_counts().head(5)

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=top_states.values, y=top_states.index, palette='viridis', ax=ax)
ax.set_title("Negara Bagian dengan Pelanggan Terbanyak")
ax.set_xlabel("Jumlah Pelanggan")
ax.set_ylabel("Negara Bagian")
st.pyplot(fig)