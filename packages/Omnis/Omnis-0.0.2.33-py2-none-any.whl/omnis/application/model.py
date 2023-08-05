from keras.models import load_model

import pickle

import numpy


class Model:
    def __init__(self, model_path = None, output_dictionary_path = None):
        """Initializes a neural network model.

        If you want to load a model you've already trained, just give a path of model file and it's output_dictionary path.
        
        Keyword Arguments:
            model_path {str} -- A path of model file. (default: {None})
            output_dictionary_path {str or None} -- A path of output_dictionary file. (default: {None})
        
        Raises:
            e -- Raises error when loading a model is failed.
        """
        if type(model_path) == type(None):
            self.model = None
        else:
            try:
                self.model = self.load(model_path, output_dictionary_path)
                if type(self.model) == type(None):
                    print('Nothing loaded')
            except Exception as e:
                print('Model loading failed')
                raise e

    def load(self, model_path, output_dictionary_path):
        """Loads a model and a output_dictionary from a file system.
        
        Arguments:
            model_path {str} -- Path of saved model.
            output_dictionary_path {str} -- Path of saved output_dictionary
        
        Returns:
           [keras model instance] -- Functional model will be returned.
        """
        model = load_model(model_path)
        self.output_dictionary = self.load_output_dictionary(output_dictionary_path)
        self.input_shape = model.input_shape[1:]
        return model

    def load_output_dictionary(self, output_dictionary_path):
        try:
            with open(output_dictionary_path, 'r') as f:
                data = pickle.load(f)
            return data
        except Exception as e:
            raise e

    def save(self, model_path, output_dictionary_path):
        """Saves a model as h5 format and a output_dictionary as pickle format.
        
        Arguments:
            model_path {str} -- Path to save model.
            output_dictionary_path {str} -- Path to save output_dictionary.
                
        Raises:
            TypeError -- Raises error if self.model is not created.
            e -- Raises error if a path is wrong.
        """
        try:
            if type(self.model) == type(None):
                raise TypeError('you should create a model before save it')
            self.model.save(model_path)
            self.save_output_dictionary(output_dictionary_path)  
        except Exception as e:
            raise e

    def save_output_dictionary(self, output_dictionary_path):
        if type(self.output_dictionary) == type({}): # check output_dictionary type
            if type(output_dictionary_path) == type(''): # check output_dictionary_path type
                with open(output_dictionary_path, 'w') as f:
                    pickle.dump(self.output_dictionary, f)
            elif type(output_dictionary_path) != type(None):
                raise TypeError('a type of output_dictionary_path should be str')
        else:
            if type(output_dictionary_path) == type(''):
                raise TypeError('wrong output_dictionary type')

    def set_output_dictionary(self, output_dictionary):
        self.output_dictionary = output_dictionary

    def compile_model(self, optimizer, loss=None, metrics=['accuracy']):
        """This function compiles self.model according to arguments.
        
        Arguments:
            optimizer {str or keras optimizer instance} -- See https://keras.io/optimizers/ for more information about optimizers.
        
        Keyword Arguments:
            loss {str or objective function} -- See https://keras.io/losses/ for more information about loss. (default: {None})
            metrics {list} -- List of metrics to be evaluated by the model during training and evaluating(testing). (default: {['accuracy']})
        """
        self.model.compile(optimizer, loss=loss, metrics=metrics)    

    def predict(self, data_array, predict_classes = True):
        """Generates output of predictions for the input samples.
        
        Arguments:
            data_array {ndarray} -- The input data like x_test of keras.
        
        Keyword Arguments:
            predict_classes {bool} --
                Decides a prediction result's type.
                By default, a return value of prediction result is an array of classes.
                If you set predict_classes as False, you can get a raw output array as a prediction result.
                (default: {True})

        Raises:
            e -- Raise exception when prediction failed.
        
        Returns:
            [ndarray] -- Predicted classes(labels) of input data
        """
        try:
            probs = self.model.predict(data_array)
            if predict_classes == False:
                return probs
            predicted_classes = probs.argmax(axis=-1)
            try:
                for i in range(predicted_classes.shape[0]):
                    if i == 0:
                        return_list = [ self.output_dictionary[predicted_classes[i]] ]
                    else:
                        return_list.append( self.output_dictionary[predicted_classes[i]] )
                return numpy.asarray(return_list)
            except:
                return predicted_classes
        except Exception as e:
            # Prediction failed
            raise e

    def print_summary(self):
        self.model.summary()