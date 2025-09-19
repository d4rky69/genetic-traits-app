import pandas as pd
import random
import streamlit as st
import matplotlib.pyplot as plt

# ------------------------------
# Generate Random Data
# ------------------------------
names = [
    "Aarav", "Vihaan", "Aditya", "Arjun", "Krishna", "Rohan", "Ishaan", "Kunal",
    "Sanya", "Ananya", "Priya", "Kavya", "Ritika", "Nisha", "Meera", "Divya",
    "Rahul", "Amit", "Sneha", "Pooja", "Varun", "Neha", "Shreya", "Manish",
    "Akash", "Vikram", "Sunita", "Lakshmi", "Ramesh", "Deepak", "Geeta", "Ajay",
    "Suresh", "Anjali", "Swati"
]

eye_colours = ["Brown", "Black"]
dimples = ["Yes", "No"]
earlobes = ["Free", "Attached"]
tongue_roll = ["Yes", "No"]
right_handed = ["Yes", "No"]

data = []
for i in range(1, 36):
    name = names[i-1]
    age = random.randint(18, 25)
    eye = random.choice(eye_colours)
    dimple = random.choice(dimples)
    ear = random.choice(earlobes)
    tongue = random.choice(tongue_roll)
    handed = random.choices(right_handed, weights=[0.9, 0.1])[0]
    data.append([i, name, age, eye, dimple, ear, tongue, handed])

fields = ["S.No", "Name", "Age", "Eye Colour", "Dimples", "Earlobe", "Tongue Roll", "Right Handed"]
df = pd.DataFrame(data, columns=fields)

# ------------------------------
# Streamlit App
# ------------------------------
st.set_page_config(page_title="Genetic Traits Database", layout="wide")

st.title("🧬 Genetic Traits Database")
st.write("Interactive dataset of 35 individuals with genetic traits.")

# Show full dataset
st.subheader("📋 Full Dataset")
st.dataframe(df, use_container_width=True)

# Search by Name
st.subheader("🔍 Search by Name")
search_name = st.text_input("Enter a name:")
if search_name:
    results = df[df["Name"].str.contains(search_name, case=False, na=False)]
    if not results.empty:
        st.success(f"Found {len(results)} record(s)")
        st.dataframe(results, use_container_width=True)
    else:
        st.warning("No match found.")

# Filter by Trait
st.subheader("🎯 Filter by Trait")
trait = st.selectbox("Choose a trait to filter:", ["Eye Colour", "Dimples", "Earlobe", "Tongue Roll", "Right Handed"])
value = st.selectbox("Choose value:", df[trait].unique())

filtered = df[df[trait] == value]
st.write(f"Showing individuals with **{trait} = {value}**:")
st.dataframe(filtered, use_container_width=True)

# Summary Section
st.subheader("📊 Trait Summary & Visualizations")

def show_trait_summary(column, title):
    counts = df[column].value_counts()
    percentages = round((counts / len(df)) * 100, 2)

    # Table
    st.write(f"**{title} Distribution**")
    summary = pd.DataFrame({"Value": counts.index, "Count": counts.values, "Percentage": percentages.values})
    st.dataframe(summary)

    # Charts
    col1, col2 = st.columns(2)
    with col1:
        st.write("Bar Chart")
        fig, ax = plt.subplots()
        ax.bar(counts.index, counts.values, color="skyblue", edgecolor="black")
        ax.set_ylabel("Count")
        ax.set_title(f"{title} - Bar Chart")
        st.pyplot(fig)

    with col2:
        st.write("Pie Chart")
        fig, ax = plt.subplots()
        ax.pie(counts.values, labels=counts.index, autopct='%1.1f%%', startangle=90,
               colors=["#66b3ff","#ff9999","#99ff99","#ffcc99"])
        ax.set_title(f"{title} - Pie Chart")
        st.pyplot(fig)

# Show for all traits
show_trait_summary("Eye Colour", "Eye Colour")
show_trait_summary("Dimples", "Dimples")
show_trait_summary("Earlobe", "Earlobe")
show_trait_summary("Tongue Roll", "Tongue Roll")
show_trait_summary("Right Handed", "Handedness")
st.markdown("---")
st.markdown("👨‍💻 Created by **Shreyas Sahoo**")

