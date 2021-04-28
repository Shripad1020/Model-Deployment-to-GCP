import tensorflow as tf
import googleapiclient.discovery
from google.api_core.client_options import ClientOptions

# dummy base prediction classes
base_classes = ['chicken_curry',
				 'chicken_wings',
				 'fried_rice',
				 'grilled_salmon',
				 'hamburger',
				 'ice_cream',
				 'pizza',
				 'ramen',
				 'steak',
				 'sushi']

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

def load_and_prep_image(image, img_shape, rescale=False):
	img = tf.io.decode_image(image, channels=3)
	# Resize the image
	img = tf.image.resize(img, [img_shape, img_shape])
	# Rescale the image
	if rescale:
		return img/255.
	else:
		return img

def predict_json(project, region, model, instances, version=None):
    """Send json data to a deployed model for prediction.
    Args:
        project (str): project where the Cloud ML Engine Model is deployed.
        model (str): model name.
        instances ([Mapping[str: Any]]): Keys should be the names of Tensors
            your deployed model expects as inputs. Values should be datatypes
            convertible to Tensors, or (potentially nested) lists of datatypes
            convertible to Tensors.
        version (str): version of the model to target.
    Returns:
        Mapping[str: any]: dictionary of prediction results defined by the 
            model.
    """
    # Create the ML Engine service object
    prefix = "{}-ml".format(region) if region else "ml"
    api_endpoint = "https://{}.googleapis.com".format(prefix)
    client_options = ClientOptions(api_endpoint=api_endpoint)

    # Setup model path
    model_path = "projects/{}/models/{}".format(project, model)
    if version is not None:
        model_path += "/versions/{}".format(version)

    # Create ML engine resource endpoint and input data
    ml_resource = googleapiclient.discovery.build(
        "ml", "v1", cache_discovery=False, client_options=client_options).projects()
    instances_list = instances.numpy().tolist() # turn input into list (ML Engine wants JSON)
    
    input_data_json = {"signature_name": "serving_default",
                       "instances": instances_list} 

    request = ml_resource.predict(name=model_path, body=input_data_json)
    response = request.execute()
    
    # # ALT: Create model api
    # model_api = api_endpoint + model_path + ":predict"
    # headers = {"Authorization": "Bearer " + token}
    # response = requests.post(model_api, json=input_data_json, headers=headers)

    if "error" in response:
        raise RuntimeError(response["error"])

    return response["predictions"]

def get_classes_and_models(model_name):
	model_name = model_name.split(" : ")[0].lower()

	CLASSSES = models[model_name]["classes"]
	MODEL = models[model_name]["model_name"]

	return CLASSSES, MODEL

def update_logger(img, model_used, pred_class, pred_conf, correct=False, user_label=None):
	logger = {
		"image": img,
		"model_used": model_used,
		"pred_class": pred_class,
		"pred_conf": pred_conf,
		"correct": correct,
		"user_label": user_label
	}   
	#return logger