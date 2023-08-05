# -*- coding:utf-8 -*-
"""
Created on the 05/01/18
@author: Nicolas Thiebaut
@email: nkthiebaut@gmail.com
"""
from typing import List

import gensim.downloader as api
from gensim.models.keyedvectors import Word2VecKeyedVectors
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

from zeugma.logger import package_logger as logger
from zeugma.conf import DEFAULT_PRETRAINED_EMBEDDINGS


class EmbeddingTransformer(BaseEstimator, TransformerMixin):
    """ Text vectorizer class """

    def __init__(self, model: str ='glove', aggregation: str ='average'):
        if isinstance(model, str):
            model = model.lower()
            if model in DEFAULT_PRETRAINED_EMBEDDINGS.keys():
                model_gensim_name = DEFAULT_PRETRAINED_EMBEDDINGS[model]
                self.model = api.load(model_gensim_name)
            elif model in api.info()['models'].keys():
                self.model = api.load(model)
            else:
                raise KeyError('Unknown pretrained model name:' + model + '. Available models are: ' +
                               ", ".join(api.info()['models'].keys()))
            logger.info('Loaded model keyed vectors: ' + model)
        elif isinstance(model, Word2VecKeyedVectors):
            self.model = model
            logger.info('Loaded model keyed vectors.')
        else:
            raise TypeError('Input pre-trained model should be a string or a gensim Word2VecKeyedVectors object')
        self.aggregation = aggregation

    def transform_sentence(self, text):
        """ Compute an aggregate embedding vector for the input text """
        def preprocess_text(raw_text: str) -> List[str]:
            """ Prepare text for Gensim model, excluding unknown words"""
            if not isinstance(raw_text, list):
                if not isinstance(raw_text, str):
                    raise TypeError
                raw_text = raw_text.split()
            return list(filter(lambda x: x in self.model.vocab, raw_text))
        tokens = preprocess_text(text)

        if not tokens:
            return np.zeros(self.model.vector_size)

        if self.aggregation == 'average':
            text_vector = np.mean(self.model[tokens], axis=0)
        elif self.aggregation == 'sum':
            text_vector = np.sum(self.model[tokens], axis=0)
        elif self.aggregation == 'minmax':
            maxi = np.max(self.model[tokens], axis=0)
            mini = np.min(self.model[tokens], axis=0)
            text_vector = np.concatenate([maxi, mini])
        else:
            raise ValueError('Unknown embeddings aggregation mode: ' + self.aggregation)
        return text_vector

    def fit(self, x, y=None):
        """ Has to define fit method to conform scikit-learn Transformer
        definition and integrate a sklearn.Pipeline object """
        return self

    def transform(self, texts):
        """ Transform corpus from single text transformation method """
        # TODO: parallelize this method with multiprocessing
        return np.array([self.transform_sentence(t) for t in texts])
