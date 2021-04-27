# dummy base prediction classes
base_classes = ['fried_rice',
					'hamburger',
					'ice_cream',
					'pizza',
					'ramen']

# updated classes will add here
updated_classes = []

models = {
	# default version of model
	"model_1": {
		"classes": base_classes,
		# model name - type of model, number, number of classes included
		"model_name": "Model_name - model_number - number of clases"
	}
	# add newer versions of models
}

def load_and_prep_image(image):
	pass

def predict_json():
	pass

def get_classes_and_models(model_name):
	model_name = model_name.split(" :")[0].lower()

	CLASSSES = models[model_name]["classes"]
	MODEL = models[model_name]["model_name"]

	return CLASSSES, MODEL
