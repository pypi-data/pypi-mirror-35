from keras import models
from keras.layers import Input, Dense, LSTM
from keras import layers

from ..model import Model

from ...lib.text_lib import *

from ...lib.general_lib import *

import numpy as np

import random



class Translation_Model(Model):
    def __init__(self, input_shape = None, model_path = None, output_dictionary_path = None):
        """Initializes a model.
        
        Arguments:
            Model {class} -- A super class of neural network models.
        
        Keyword Arguments:
            input_shape {tuple} -- An input shape of the neural network. (default: {None})
            model_path {str} -- A path of model file. (default: {None})
            output_dictionary_path {str or None} -- A path of output_dictionary file. (default: {None})
        """
        if type(model_path) != type(None):
            Model.__init__(self, model_path, output_dictionary_path)
            return
        if type(input_shape) == type(None):
            Model.__init__(self)
        else:
            Model.__init__(self)
            self.input_shape = input_shape

    def prepare_train_data(self, train_text, max_sentence_size, sentences, next_characters):
        if hasattr(self, 'output_dictionary') == False:
            sorted_unique_characters = get_unique_characters(train_text)
            char_index_dict = dict((c, i) for i, c in enumerate(sorted_unique_characters))
            self.output_dictionary = reverse_dict(char_index_dict)
        else:
            try:
                char_index_dict = reverse_dict(self.output_dictionary)
            except:
                raise TypeError('invalid output_dictionary')
        
        input_token_index = dict( [(char, i) for i, char in enumerate(input_characters)] )
        target_token_index = dict( [(char, i) for i, char in enumerate(target_characters)] )

        encoder_input_data = np.zeros( (len(input_texts), max_encoder_seq_length, num_encoder_tokens), dtype='float32')
        decoder_input_data = np.zeros( (len(input_texts), max_decoder_seq_length, num_decoder_tokens), dtype='float32')
        decoder_target_data = np.zeros( (len(input_texts), max_decoder_seq_length, num_decoder_tokens), dtype='float32')

        for i, (input_text, target_text) in enumerate(zip(input_texts, target_texts)):
            for t, char in enumerate(input_text):
                encoder_input_data[i, t, input_token_index[char]] = 1.
            for t, char in enumerate(target_text):
                # decoder_target_data is ahead of decoder_input_data by one timestep
                decoder_input_data[i, t, target_token_index[char]] = 1.
                if t > 0:
                    # decoder_target_data will be ahead by one timestep
                    # and will not include the start character.
                    decoder_target_data[i, t - 1, target_token_index[char]] = 1.
    
    def create_model(self):
        encoder_inputs = Input(shape=(None, num_encoder_tokens))
        encoder = LSTM(latent_dim, return_state=True)
        encoder_outputs, state_h, state_c = encoder(encoder_inputs)
        # We discard `encoder_outputs` and only keep the states.
        encoder_states = [state_h, state_c]

        # Set up the decoder, using `encoder_states` as initial state.
        decoder_inputs = Input(shape=(None, num_decoder_tokens))
        # We set up our decoder to return full output sequences,
        # and to return internal states as well. We don't use the
        # return states in the training model, but we will use them in inference.
        decoder_lstm = LSTM(256, return_sequences=True, return_state=True)
        decoder_outputs, _, _ = decoder_lstm(decoder_inputs, initial_state=encoder_states)
        decoder_dense = Dense(num_decoder_tokens, activation='softmax')
        decoder_outputs = decoder_dense(decoder_outputs)
        model = models.Model([encoder_inputs, decoder_inputs], decoder_outputs)
        return model

    def train(self,
            batch_size = None,
            steps_per_epoch = None,
            epochs = 1,
            verbose = 1,
            callbacks = None,
            shuffle = True):
            self.model = self.create_model()
            self.compile_model(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
            model.fit([encoder_input_data, decoder_input_data], decoder_target_data, batch_size=batch_size, epochs=epochs, validation_split=0.2)
            self.model.fit(self.x, self.y, batch_size=batch_size, steps_per_epoch=steps_per_epoch, epochs = epochs, verbose = verbose, callbacks = callbacks, shuffle = shuffle)

    def created_encoder_and_decoder_model(self):
        encoder_model = Model(encoder_inputs, encoder_states)

        decoder_state_input_h = Input(shape=(latent_dim,))
        decoder_state_input_c = Input(shape=(latent_dim,))
        decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]
        decoder_outputs, state_h, state_c = decoder_lstm(decoder_inputs, initial_state=decoder_states_inputs)
        decoder_states = [state_h, state_c]
        decoder_outputs = decoder_dense(decoder_outputs)
        decoder_model = Model( [[decoder_inputs] + decoder_states_inputs, decoder_outputs] + decoder_states )

    def translate_text(self, starting_sentence, generated_text_size):
        for seq_index in range(100):
            # Take one sequence (part of the training test)
            # for trying out decoding.
            input_seq = encoder_input_data[seq_index: seq_index + 1]
            decoded_sentence = decode_sequence(encoder_model, decoder_model, input_seq, num_decoder_tokens, target_token_index, reverse_target_char_index, max_decoder_seq_length)
            print('-')
            print('Input sentence:', input_texts[seq_index])
        return decoded_sentence

    def decode_sequence(self, encoder_model, decoder_model, input_seq, num_decoder_tokens, target_token_index, reverse_target_char_index, max_decoder_seq_length):
        # Encode the input as state vectors.
        states_value = encoder_model.predict(input_seq)
        # Generate empty target sequence of length 1.
        target_seq = np.zeros((1, 1, num_decoder_tokens))
        # Populate the first character of target sequence with the start character.
        target_seq[0, 0, target_token_index['\t']] = 1.
        # Sampling loop for a batch of sequences
        # (to simplify, here we assume a batch of size 1).
        stop_condition = False
        decoded_sentence = ''
        while not stop_condition:
            output_tokens, h, c = decoder_model.predict([target_seq] + states_value)
            # Sample a token
            sampled_token_index = np.argmax(output_tokens[0, -1, :])
            sampled_char = reverse_target_char_index[sampled_token_index]
            decoded_sentence += sampled_char
            # Exit condition: either hit max length
            # or find stop character.
            if (sampled_char == '\n' or len(decoded_sentence) > max_decoder_seq_length):
                stop_condition = True
            # Update the target sequence (of length 1).
            target_seq = np.zeros((1, 1, num_decoder_tokens))
            target_seq[0, 0, sampled_token_index] = 1.
            # Update states
            states_value = [h, c]
        return decoded_sentence





# Next: inference mode (sampling).
# Here's the drill:
# 1) encode input and retrieve initial decoder state
# 2) run one step of decoder with this initial state
# and a "start of sequence" token as target.
# Output will be the next target token
# 3) Repeat with the current target token and current states

# Define sampling models

# Reverse-lookup token index to decode sequences back to
# something readable.
reverse_input_char_index = dict( (i, char) for char, i in input_token_index.items() )
reverse_target_char_index = dict( (i, char) for char, i in target_token_index.items() )


