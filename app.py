import streamlit as st
import tensorflow as tf
from utils import load_and_prep_image, predict, get_classes_and_models, update_logger
import SessionState
 
st.title("Streamlit Web App for Image classification")
st.header("Identify what's in your food photo!")

@st.cache
def make_prediction(image, model, class_name):		
	image = load_and_prep_image(image, 224)
	image = tf.cast(tf.expand_dims(image, axis=0), tf.int16)
	preds = predict(image)

	pred_class = class_name[tf.argmax(preds[0])]
	pred_conf = tf.reduce_max(preds[0])

	return image, pred_class, pred_conf

# Pick the model version
choose_model = st.sidebar.selectbox(
	"Pick model to use",
	# model name writing style - 'Model_number :' - after this can add discription. 
	("Model_1 : EfficientNet - 10 classes",
	 "Model_2 : Not available",
	 "Model_3 : Not available")
)

# Model choice logic
try:
	CLASSES, MODEL = get_classes_and_models(choose_model)
except KeyError:
	pass

# Display info about model and classes
if st.checkbox("Show classes"):
	st.write(f"You chose {MODEL}, these are the classes of food it can identify:\n", CLASSES)

# File uploader allows user to add their own image
uploaded_file = st.file_uploader(label="Upload an image of food", type=["png", "jpeg", "jpg"])

# Session State kinda like instance
session_state = SessionState.get(pred_button=False)

# Logical flow of app
if not uploaded_file:
	st.warning("Please upload an image.")
	st.stop()
else:
	session_state.uploaded_image = uploaded_file.read()
	st.image(session_state.uploaded_image, use_column_width=True)
	pred_button = st.button("Predict")

# If button is press?
if pred_button:
	session_state.pred_button = True

# If pressed
if session_state.pred_button:
	session_state.image, session_state.pred_class, session_state.pred_conf = make_prediction(session_state.uploaded_image, model=MODEL, class_name=CLASSES)
	st.write("Prediction : {},\nConfidance : {}".format(session_state.pred_class, session_state.pred_conf))

	# Feedback loop
	session_state.feedback = st.selectbox("Correct?", ("Select an option", "Yes", "No"))

	if session_state.feedback == "Yes":
		st.write("Thanks you for feedback!")
		#TODO - code written to simply print log. update using logger.
		update_logger(img=session_state.image, model_used=MODEL, pred_class=session_state.pred_class, pred_conf=session_state.pred_conf, correct=True)
	elif session_state.feedback == "No":
		session_state.correct_class = st.text_input("Select correct label for it.")
		if session_state.correct_class:
			st.write("Thank you for that, we'll use your help to make our model better!")
			update_logger(img=session_state.image, model_used=MODEL, pred_class=session_state.pred_class, pred_conf=session_state.pred_conf, correct=False, user_label=session_state.correct_class)