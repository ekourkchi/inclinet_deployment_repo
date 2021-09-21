import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten
from tensorflow.keras.utils import to_categorical

class Models:

    def __init__(self, input_shape=(128, 128, 3), n_classes = None):
        
        self.input_shape = input_shape
        self.n_classes   = n_classes

    def getModel(self, model_name):

        if model_name == 'model4':
            return self.model4
        if model_name == 'model5':
            return self.model5
        if model_name == 'model6':
            return self.model6

    ## n_classes is None if the network is used for regression
    def model4(self):

        model = tf.keras.models.Sequential()
        model.add(tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=self.input_shape, name='conv1'))
        model.add(tf.keras.layers.Conv2D(16, (3, 3), activation='relu', name='conv2'))
        model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
        model.add(tf.keras.layers.Dropout(0.25))

        model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', name='conv3'))
        model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', name='conv4'))
        model.add(tf.keras.layers.BatchNormalization(axis = 3, name = 'bn_2'))
        model.add(tf.keras.layers.MaxPooling2D(pool_size=(4, 4)))
        model.add(tf.keras.layers.Dropout(0.25))

        ## Fully connected layers
        model.add(tf.keras.layers.Flatten())
        model.add(tf.keras.layers.Dense(256, activation='relu', name='fc_2'))
        model.add(tf.keras.layers.Dense(32, activation='relu', name='fc_4'))
        model.add(tf.keras.layers.Dense(8, activation='relu', name='fc_5'))

        # output layer
        if self.n_classes is None:
            model.add(tf.keras.layers.Dense(1, activation='tanh', name='fc_out2'))
        else:
            model.add(tf.keras.layers.Dense(self.n_classes, activation='softmax'))

        return model

    #################################################################################################################

    ## n_classes is None if the network is used for regression
    def model5(self):

        model = tf.keras.models.Sequential()

        model.add(tf.keras.layers.Conv2D(128, (3, 3), activation='relu', input_shape=self.input_shape, name='conv1'))
        model.add(tf.keras.layers.Conv2D(128, (3, 3), activation='relu', name='conv2'))
        model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
        model.add(tf.keras.layers.Dropout(0.25))

        model.add(tf.keras.layers.Conv2D(256, (3, 3), activation='relu', name='conv3'))
        model.add(tf.keras.layers.Conv2D(256, (3, 3), activation='relu', name='conv4'))
        model.add(tf.keras.layers.BatchNormalization(axis = 3, name = 'bn_2'))
        model.add(tf.keras.layers.MaxPooling2D(pool_size=(4, 4)))
        model.add(tf.keras.layers.Dropout(0.25))
        
        model.add(tf.keras.layers.Conv2D(256, (3, 3), activation='relu', name='conv5'))
        model.add(tf.keras.layers.Conv2D(256, (3, 3), activation='relu', name='conv6'))
        model.add(tf.keras.layers.BatchNormalization(axis = 3, name = 'bn_3'))
        model.add(tf.keras.layers.MaxPooling2D(pool_size=(4, 4)))

        ## Fully connected layers
        model.add(tf.keras.layers.Flatten())
        model.add(tf.keras.layers.Dense(256, activation='relu', name='fc_2'))
        model.add(tf.keras.layers.Dense(128, activation='relu', name='fc_3')) 
        model.add(tf.keras.layers.Dense(64, activation='relu', name='fc_4'))
        model.add(tf.keras.layers.Dense(8, activation='relu', name='fc_5'))
        
        # output layer
        if self.n_classes is None:
            model.add(tf.keras.layers.Dense(1, activation='tanh', name='fc_out2'))
        else:
            model.add(tf.keras.layers.Dense(self.n_classes, activation='softmax'))

        return model

    #################################################################################################################

    ## n_classes is None if the network is used for regression
    def model6(self):

        model = tf.keras.models.Sequential()

        model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=self.input_shape, name='conv1'))
        model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', name='conv2'))
        model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
        model.add(tf.keras.layers.Dropout(0.25))

        model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu', name='conv3'))
        model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu', name='conv4'))
        model.add(tf.keras.layers.BatchNormalization(axis = 3, name = 'bn_2'))
        model.add(tf.keras.layers.MaxPooling2D(pool_size=(4, 4)))
        model.add(tf.keras.layers.Dropout(0.25))

        ## Fully connected layers
        model.add(tf.keras.layers.Flatten())
        model.add(tf.keras.layers.Dense(128, activation='relu', name='fc_3'))
        model.add(tf.keras.layers.Dense(64, activation='relu', name='fc_4'))
        model.add(tf.keras.layers.Dense(8, activation='relu', name='fc_5'))

        # output layer
        # output layer
        if self.n_classes is None:
            model.add(tf.keras.layers.Dense(1, activation='tanh', name='fc_out2'))
        else:
            model.add(tf.keras.layers.Dense(self.n_classes, activation='softmax'))

        return model

    #################################################################################################################