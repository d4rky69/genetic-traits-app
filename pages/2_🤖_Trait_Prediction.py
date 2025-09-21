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

# --- DATA LOADING (Mirrors the logic from Home.py) ---
@st.cache_data
def generate_demo_data():
    names = [
        "Shreyas", "Arnab", "Aditya", "Arjun", "Krishna", "Rohan", "Ishaan", "Kunal", "Sanya", "Ananya",
        "Priya", "Kavya", "Ritika", "Nisha", "Meera", "Divya", "Rahul", "Amit", "Sneha", "Pooja",
        "Varun", "Neha", "Shreya", "Manish", "Akash", "Vikram", "Sunita", "Lakshmi", "Ramesh",
        "Deepak", "Geeta", "Ajay", "Suresh", "Anjali", "Swati"
    ]
    data = [[i, name, random.randint(18, 25), random.choice(["Brown", "Black"]), random.choice(["Yes", "No"]),
             random.choice(["Free", "Attached"]), random.choice(["Yes", "No"]),
             random.choices(["Right", "Left", "Mixed"], weights=[0.89, 0.10, 0.01])[0]]
            for i, name in enumerate(names, 1)]
    fields = ["S.No", "Name", "Age", "Eye Colour", "Dimples", "Earlobe", "Tongue Roll", "Handedness"]
    return pd.DataFrame(data, columns=fields)

REQUIRED_COLS = {"Name", "Age", "Eye Colour", "Dimples", "Earlobe", "Tongue Roll", "Handedness"}

uploaded_file = st.sidebar.file_uploader("📂 Upload your own CSV data", type="csv")
if uploaded_file is not None:
    st.sidebar.success("Custom data loaded!")
    df = pd.read_csv(uploaded_file)
    if not REQUIRED_COLS.issubset(df.columns):
        st.error(f"Error: The uploaded CSV must contain the following columns: {', '.join(REQUIRED_COLS)}")
        st.stop()
else:
    st.sidebar.info("Using demo data. Upload a CSV to analyze your own!")
    df = generate_demo_data()

# --- MODEL TRAINING ---
st.markdown("This model trains on the currently loaded data (either the demo set or your uploaded file) to predict handedness.")
df_ml = df.drop(columns=['S.No', 'Name'])
encoders = {}
for column in df_ml.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df_ml[column] = le.fit_transform(df_ml[column])
    encoders[column] = le

X = df_ml.drop('Handedness', axis=1)
y = df_ml['Handedness']
feature_names = X.columns.tolist()
if len(df) > 10: # Ensure enough data to split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = DecisionTreeClassifier(max_depth=4, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
else:
    accuracy = "N/A (Dataset too small)"

# --- INTERACTIVE PREDICTION & MODEL EXPLANATION ---
# (The rest of the code for this page is the same as before)
st.markdown("---")
st.header("🔮 Make a Prediction")
# ... (Prediction UI code) ...
col1, col2, col3 = st.columns(3)
with col1:
    eye_colour = st.selectbox("Eye Colour:", encoders['Eye Colour'].classes_)
    dimples = st.selectbox("Dimples:", encoders['Dimples'].classes_)
with col2:
    earlobe = st.selectbox("Earlobe:", encoders['Earlobe'].classes_)
    tongue_roll = st.selectbox("Tongue Roll:", encoders['Tongue Roll'].classes_)
with col3:
    age = st.slider("Age:", int(df['Age'].min()), int(df['Age'].max()), int(df['Age'].mean()))

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
if isinstance(accuracy, float):
    st.info(f"The Decision Tree Classifier achieved an accuracy of **{accuracy:.2f}%** on the test portion of the loaded data.", icon="💡")
else:
    st.info(f"Accuracy: **{accuracy}**", icon="💡")

st.subheader("Visualizing the Decision Tree")
dot_data = export_graphviz(model, out_file=None, feature_names=feature_names, class_names=encoders['Handedness'].classes_, filled=True, rounded=True, special_characters=True)
st.graphviz_chart(dot_data)

add_pdf_export()
