import streamlit as st
import tensorflow as tf
from utils import load_and_prep_image, predict_json, classes_and_models
 
st.title("My first App in Streamlit.")
st.header("Identify what's in your food photo!")

@st.cache
def makePrediction(image, model, class_name):		
	image = load_and_prep_image(image)
	image = tf.cast(tf.expand_dims(image, axis=0), tf.int16)
	preds = predict_json()

	pred_class = class_name[tf.argmax(preds[0])]
	pred_conf = tf.reduce_max(preds[0])

	return image, pred_class, pred_conf

# Pick the model version
choose_model = st.sidebar.selectbox(
	"Pick model to use",
	("Model 1 : ",
	 "Model 2 : ",
	 "Model 3 : ")
)

# Model choice logic
if choose_model == "Model 1 : ":
	CLASSES = classes_and_models
	MODEL = classes_and_models
elif choose_model == "Model 2 : s":
	CLASSES = classes_and_models
	MODEL = classes_and_models
else:
	CLASSES = classes_and_models
	MODEL = classes_and_models

# Display info about model and classes
if st.checkbox("Show classes"):
	st.write(f"You chose {MODEL}, these are the classes of food it can identify:\n", CLASSES)

# File uploader allows user to add their own image
uploaded_file = st.file_uploader(label="Upload an image of food", type=["png", "jpeg", "jpg"])


#logical flow of app
if not uploaded_file:
	st.warning("Please upload an image.")
	st.stop
