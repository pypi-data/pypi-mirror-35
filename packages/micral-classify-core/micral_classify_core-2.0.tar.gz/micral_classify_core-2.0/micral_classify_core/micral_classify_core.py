import numpy as np
from keras.models import load_model
import micral_utils
import os, traceback

def split(t,size):
    splitted = np.empty(((t.shape[0]//size)*(t.shape[1]//size),size,size), dtype=np.float32)
    numSplit = 0
    for y in range(t.shape[0]//size):
        for x in range(t.shape[1]//size):
            img = t[y*size:(y+1)*size,x*size:(x+1)*size]
            img = img.astype('float32') / 255.
            img = img-img.mean()
            if img.std() > 0.0:
                img = img/img.std()
            splitted[numSplit,:,:] = img
            numSplit += 1
    return np.expand_dims(splitted, axis=3)
    
def classifyImageProcessor(image, plot, model):
    image_dict = dict()
    imageSize = 32
    categories = ["Martensite", "Spheroidite", "Pearlite"]
    splitted = split(image, imageSize)
    pred = np.sum(model.predict_on_batch(splitted), axis=0)/len(splitted) * 100.0
    catPred = np.argmax(pred)
    
    image_dict['category'] = categories[catPred]
    if plot :
        image_dict['category_number'] = catPred
        image_dict['prediction_histogram'] = pred
    
    return image_dict

def classifyImageCore(images, plot):
    output = dict()
    images = micral_utils.formatInput(images)
    model = load_model(os.path.dirname(os.path.realpath(__file__)) + '/CrystNet1.2.hdf5')
    for numImage in range(len(images)):
        try:
            data, name = micral_utils.loadData(images[numImage], numImage)
            output[name] = classifyImageProcessor(data, name, model)
        except Exception as e:
            print("image " + str(numImage) + " raise : " + str(e.__doc__))
            traceback.print_exc()
            pass
    return micral_utils.removeEmptyDict(output)