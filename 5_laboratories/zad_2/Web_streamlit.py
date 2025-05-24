import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Połączenie z bazą SQLite
conn = sqlite3.connect('sales.db', check_same_thread=False)
c = conn.cursor()

# Funkcja do pobrania danych z bazy
def get_data(product_filter=None):
    if product_filter and product_filter != "Wszystkie":
        query = "SELECT * FROM sales WHERE product = ?"
        df = pd.read_sql_query(query, conn, params=(product_filter,))
    else:
        query = "SELECT * FROM sales"
        df = pd.read_sql_query(query, conn)
    return df

# Funkcja do dodania nowego rekordu
def add_sale(product, quantity, price, date):
    c.execute(
        "INSERT INTO sales (product, quantity, price, date) VALUES (?, ?, ?, ?)",
        (product, quantity, price, date)
    )
    conn.commit()

# Tytuł aplikacji
st.title("Aplikacja sprzedażowa")

# Pobranie unikalnych produktów dla filtra i selectboxa
all_products = pd.read_sql_query("SELECT DISTINCT product FROM sales", conn)['product'].tolist()
all_products = ["Wszystkie"] + all_products

# Sekcja dodawania nowego rekordu
st.header("Dodaj nową sprzedaż")

with st.form("form_add_sale"):
    product = st.text_input("Produkt")
    quantity = st.number_input("Ilość", min_value=1, step=1)
    price = st.number_input("Cena", min_value=0.0, format="%.2f")
    date = st.date_input("Data")
    submitted = st.form_submit_button("Dodaj")

    if submitted:
        if product and quantity > 0 and price >= 0:
            add_sale(product, quantity, price, date.strftime("%Y-%m-%d"))
            st.success("Dodano nową sprzedaż!")
            st.balloons()
        else:
            st.error("Wprowadź poprawne dane")

# Filtr po produkcie
st.header("Tabela sprzedaży")
product_filter = st.selectbox("Filtruj po produkcie:", all_products)

df = get_data(product_filter)
st.dataframe(df)

# Wykresy
st.header("Wykresy sprzedaży")

if not df.empty:
    # Sprzedaż dzienna (ilość × cena)
    df['date'] = pd.to_datetime(df['date'])
    df['value'] = df['quantity'] * df['price']
    daily_sales = df.groupby('date')['value'].sum()

    fig1, ax1 = plt.subplots()
    daily_sales.plot(kind='bar', ax=ax1)
    ax1.set_title("Sprzedaż dzienna")
    ax1.set_ylabel("Wartość sprzedaży")
    ax1.set_xlabel("Data")
    plt.xticks(rotation=45)
    st.pyplot(fig1)

    # Suma sprzedanych produktów wg typu
    product_sum = df.groupby('product')['quantity'].sum()

    fig2, ax2 = plt.subplots()
    product_sum.plot(kind='bar', ax=ax2, color='orange')
    ax2.set_title("Suma sprzedanych produktów wg typu")
    ax2.set_ylabel("Ilość")
    ax2.set_xlabel("Produkt")
    plt.xticks(rotation=45)
    st.pyplot(fig2)
else:
    st.info("Brak danych do wyświetlenia wykresów.")

# Uruchomienie apliakcji:
# W terminalu w PyCharm wpisujemy:
# streamlit run Nazwa_pliku_z_projektem.py
