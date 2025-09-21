import streamlit as st
import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import graphviz
from sklearn.tree import export_graphviz
from utils.pdf_export import add_pdf_export, load_css

st.set_page_config(page_title="Trait Prediction", page_icon="🤖", layout="wide")
load_css()

# (The rest of this file's code is the same as the previous correct version)
# Data loading, model training, prediction UI, etc.

add_pdf_export()
