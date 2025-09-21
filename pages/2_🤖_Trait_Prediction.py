import streamlit as st
import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import graphviz
from sklearn.tree import export_graphviz
from utils.pdf_export import add_pdf_export

st.set_page_config(page_title="Trait Prediction", page_icon="🤖", layout="wide")
st.title("🤖 Trait Prediction using a Machine Learning Model")
st.markdown("This page showcases a predictive model built to guess a person's handedness based on their other genetic traits. This is a classic example of a **classification problem** in machine learning.")

@st.cache_data
def generate_data():
    names = [
        "Shreyas", "Arnab", "Aditya", "Arjun", "Krishna", "Rohan", "Ishaan", "Kunal",
        "Sanya", "Ananya", "Priya", "Kavya", "Ritika", "Nisha", "Meera", "Divya",
        "Rahul", "Amit", "Sneha", "Pooja", "Varun", "Neha", "Shreya", "Manish",
        "Akash", "Vikram", "Sunita", "Lakshmi", "Ramesh", "Deepak", "Geeta", "Ajay",
        "Suresh", "Anjali", "Swati"
    ]
    data = []
    for i, name in enumerate(names, 1):
        data.append([
            i, name, random.randint(18, 25), random.choice(["Brown", "Black"]),
            random.choice(["Yes", "No"]), random.choice(["Free", "Attached"]),
            random.choice(["Yes", "No"]),
            random.choices(["Right", "Left", "Mixed"], weights=[0.89, 0.10, 0.01])[0]
        ])
    fields = ["S.No", "Name", "Age", "Eye Colour", "Dimples", "Earlobe", "Tongue Roll", "Handedness"]
    return pd.DataFrame(data, columns=fields)

df = generate_data()
df_ml = df.drop(columns=['S.No', 'Name'])
encoders = {}
for column in df_ml.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df_ml[column] = le.fit_transform(df_ml[column])
    encoders[column] = le

X = df_ml.drop('Handedness', axis=1)
y = df_ml['Handedness']
feature_names = X.columns.tolist()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

st.markdown("---")
st.header("🔮 Make a Prediction")
st.write("Select the traits of an individual to predict their handedness.")

col1, col2, col3 = st.columns(3)
with col1:
    eye_colour = st.selectbox("Eye Colour:", encoders['Eye Colour'].classes_)
    dimples = st.selectbox("Dimples:", encoders['Dimples'].classes_)
with col2:
    earlobe = st.selectbox("Earlobe:", encoders['Earlobe'].classes_)
    tongue_roll = st.selectbox("Tongue Roll:", encoders['Tongue Roll'].classes_)
with col3:
    age = st.slider("Age:", 18, 25, 22)

if st.button("Predict Handedness", type="primary"):
    input_data = pd.DataFrame({
        'Age': [age],
        'Eye Colour': [encoders['Eye Colour'].transform([eye_colour])[0]],
        'Dimples': [encoders['Dimples'].transform([dimples])[0]],
        'Earlobe': [encoders['Earlobe'].transform([earlobe])[0]],
        'Tongue Roll': [encoders['Tongue Roll'].transform([tongue_roll])[0]]
    })
    prediction_encoded = model.predict(input_data)[0]
    prediction_decoded = encoders['Handedness'].inverse_transform([prediction_encoded])[0]
    st.success(f"**Predicted Handedness:** {prediction_decoded}")

st.markdown("---")
st.header("🧠 How the Model Works")
st.info(f"We trained a **Decision Tree Classifier** on the dataset. It achieved an accuracy of **{accuracy:.2f}%** on the test data.", icon="💡")
st.subheader("Visualizing the Decision Tree")
st.markdown("The diagram below shows the 'questions' the model asks to make a prediction. It moves down the tree based on an individual's traits until it reaches a final decision.")

dot_data = export_graphviz(model, out_file=None, feature_names=feature_names, class_names=encoders['Handedness'].classes_, filled=True, rounded=True, special_characters=True)
st.graphviz_chart(dot_data)

st.warning("Note: Since the dataset is small and randomly generated, the model's 'logic' might not reflect real-world biology, but it demonstrates the machine learning process effectively.", icon="⚠️")
add_pdf_export()
