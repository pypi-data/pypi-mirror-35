import json

import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split

from finetune.classifier import Classifier
from finetune.regressor import Regressor
from finetune.base import BaseModel
from finetune.target_encoders import OneHotLabelEncoder, RegressionEncoder
from finetune.network_modules import classifier, regressor


class MultifieldClassifier(Classifier):
    """ 
    Classifies a set of documents into 1 of N classes.

    :param config: A :py:class:`finetune.config.Settings` object or None (for default config).
    :param \**kwargs: key-value pairs of config items to override.
    """
        
    def finetune(self, Xs, Y=None, batch_size=None):
        """
        :param \*Xs: lists of text inputs, shape [batch, n_fields]
        :param Y: integer or string-valued class labels. It is necessary for the items of Y to be sortable.
        :param batch_size: integer number of examples per batch. When N_GPUS > 1, this number
                           corresponds to the number of training examples provided to each GPU.
        """
        return BaseModel.finetune(self, Xs, Y=Y, batch_size=batch_size)

    def predict(self, Xs, max_length=None):
        """
        Produces list of most likely class labels as determined by the fine-tuned model.

        :param \*Xs: lists of text inputs, shape [batch, n_fields]
        :param max_length: the number of tokens to be included in the document representation.
                           Providing more than `max_length` tokens as input will result in truncation.
        :returns: list of class labels.
        """
        return BaseModel.predict(self, Xs, max_length=max_length)

    def predict_proba(self, Xs, max_length=None):
        """
        Produces probability distribution over classes for each example in X.

        :param \*Xs: lists of text inputs, shape [batch, n_fields]
        :param max_length: the number of tokens to be included in the document representation.
                           Providing more than `max_length` tokens as input will result in truncation.
        :returns: list of dictionaries.  Each dictionary maps from X2 class label to its assigned class probability.
        """
        return BaseModel.predict_proba(self, Xs, max_length=max_length)

    def featurize(self, Xs, max_length=None):
        """
        Embeds inputs in learned feature space. Can be called before or after calling :meth:`finetune`.

        :param \*Xs: lists of text inputs, shape [batch, n_fields]
        :param max_length: the number of tokens to be included in the document representation.
                           Providing more than `max_length` tokens as input will result in truncation.
        :returns: np.array of features of shape (n_examples, embedding_size).
        """
        return BaseModel.featurize(self, Xs, max_length=max_length)

    def get_eval_fn(cls):
        return lambda labels, targets: np.mean(np.asarray(labels) == np.asarray(targets))

    def _target_encoder(self):
        return OneHotLabelEncoder()

    def _target_model(self, featurizer_state, targets, n_outputs, train=False, reuse=None, **kwargs):
        return classifier(
            hidden=featurizer_state['features'], 
            targets=targets, 
            n_targets=n_outputs, 
            dropout_placeholder=self.do_dropout, 
            config=self.config,
            train=train,
            reuse=reuse,
            **kwargs
        )

    def _predict_op(self, logits, **kwargs):
        return tf.argmax(logits, -1)

    def _predict_proba_op(self, logits, **kwargs):
        return tf.nn.softmax(logits, -1)



class MultifieldRegressor(Regressor):
    """ 
    Regresses one or more floating point values given a set of documents per example.

    :param config: A :py:class:`finetune.config.Settings` object or None (for default config).
    :param \**kwargs: key-value pairs of config items to override.
    """
        
    def finetune(self, Xs, Y=None, batch_size=None):
        """
        :param \*Xs: lists of text inputs, shape [batch, n_fields]
        :param Y: floating point targets
        :param batch_size: integer number of examples per batch. When N_GPUS > 1, this number
                           corresponds to the number of training examples provided to each GPU.
        """
        return BaseModel.finetune(self, Xs, Y=Y, batch_size=batch_size)

    def predict(self, Xs, max_length=None):
        """
        Produces list of most likely class labels as determined by the fine-tuned model.

        :param \*Xs: lists of text inputs, shape [batch, n_fields]
        :param max_length: the number of tokens to be included in the document representation.
                           Providing more than `max_length` tokens as input will result in truncation.
        :returns: list of class labels.
        """
        return BaseModel.predict(self, Xs, max_length=max_length)

    def predict_proba(self, Xs, max_length=None):
        """
        Produces probability distribution over classes for each example in X.

        :param \*Xs: lists of text inputs, shape [batch, n_fields]
        :param max_length: the number of tokens to be included in the document representation.
                           Providing more than `max_length` tokens as input will result in truncation.
        :returns: list of dictionaries.  Each dictionary maps from X2 class label to its assigned class probability.
        """
        return BaseModel.predict_proba(self, Xs, max_length=max_length)

    def featurize(self, Xs, max_length=None):
        """
        Embeds inputs in learned feature space. Can be called before or after calling :meth:`finetune`.

        :param \*Xs: lists of text inputs, shape [batch, n_fields]
        :param max_length: the number of tokens to be included in the document representation.
                           Providing more than `max_length` tokens as input will result in truncation.
        :returns: np.array of features of shape (n_examples, embedding_size).
        """
        return BaseModel.featurize(self, Xs, max_length=max_length)

    def _target_encoder(self):
        return RegressionEncoder()

    def _target_model(self, featurizer_state, targets, n_outputs, train=False, reuse=None, **kwargs):
        return regressor(
            hidden=featurizer_state['features'],
            targets=targets, 
            n_targets=n_outputs,
            dropout_placeholder=self.do_dropout,
            config=self.config,
            train=train, 
            reuse=reuse, 
            **kwargs
        )

    def _predict_op(self, logits, **kwargs):
        return logits

    def _predict_proba_op(self, logits, **kwargs):
        return tf.no_op()


if __name__ == "__main__":

    with open("data/questions.json", "rt") as fp:
        data = json.load(fp)

    scores = []
    questions = []
    answers = []
    save_path = 'saved-models/cola'

    model = MultifieldClassifier()
    xs = []

    for item in data:
        row = data[item]
        scores.append(row["score"])
        xs.append([row["question"], row["answers"][0]["answer"]])

    scores_train, scores_test, xs_train, xs_test = train_test_split(
        scores, xs, test_size=0.33, random_state=5)

    model.finetune(xs_train, scores_train)

    model = MultifieldClassifier.load(save_path)

    print("TRAIN EVAL")
    predictions = model.predict(xs_train)
    print(predictions)

    from scipy.stats import spearmanr

    print(spearmanr(predictions, scores_train))

    print("TEST EVAL")
    predictions = model.predict(xs_test)
    print(predictions)
    print(spearmanr(predictions, scores_test))
