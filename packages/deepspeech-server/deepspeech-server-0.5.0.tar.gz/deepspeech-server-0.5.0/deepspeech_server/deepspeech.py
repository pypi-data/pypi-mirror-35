import io
from collections import namedtuple
import scipy.io.wavfile as wav

from rx import Observable
from cyclotron import Component
from deepspeech.model import Model

# Number of MFCC features to use
N_FEATURES = 26

# Size of the context window used for producing timesteps in the input vector
N_CONTEXT = 9

# Beam width used in the CTC decoder when building candidate transcriptions
BEAM_WIDTH = 500

# The alpha hyperparameter of the CTC decoder. Language Model weight
LM_WEIGHT = 1.75

# The beta hyperparameter of the CTC decoder. Word insertion weight (penalty)
WORD_COUNT_WEIGHT = 1.00

# Valid word insertion weight. This is used to lessen the word insertion
# penalty when the inserted word is part of the vocabulary
VALID_WORD_COUNT_WEIGHT = 1.00

Sink = namedtuple('Sink', ['speech'])
Source = namedtuple('Source', ['text'])

# Sink events
Initialize = namedtuple('Initialize', ['model', 'alphabet', 'lm', 'trie'])
Initialize.__new__.__defaults__ = (None, None, None,)

SpeechToText = namedtuple('SpeechToText', ['data', 'context'])

# Sourc eevents
TextResult = namedtuple('TextResult', ['text', 'context'])
TextError = namedtuple('TextError', ['error', 'context'])


def make_driver(loop=None):
    def driver(sink):
        ds_model = None

        def setup_model(model_path, alphabet, lm, trie):
                print("creating model {} {}...".format(model_path, alphabet))
                ds_model = Model(
                    model_path,
                    N_FEATURES, N_CONTEXT, alphabet, BEAM_WIDTH)

                if lm and trie:
                    ds_model.enableDecoderWithLM(
                        alphabet, lm, trie,
                        LM_WEIGHT, WORD_COUNT_WEIGHT, VALID_WORD_COUNT_WEIGHT)
                print("model is ready.")
                return ds_model

        def subscribe(observer):
            def on_deepspeech_request(item):
                nonlocal ds_model

                if type(item) is SpeechToText:
                    if ds_model is not None:
                        try:
                            fs, audio = wav.read(io.BytesIO(item.data))
                            # convert to mono.
                            # todo: move to a component or just a function here
                            if len(audio.shape) > 1:
                                audio = audio[:, 0]
                            text = ds_model.stt(audio, fs)
                            observer.on_next(Observable.just(TextResult(
                                text=text,
                                context=item.context,
                            )))
                        except Exception as e:
                            observer.on_next(Observable.throw(TextError(
                                error=e,
                                context=item.context,
                            )))
                elif type(item) is Initialize:
                    ds_model = setup_model(
                        item.model, item.alphabet, item.lm, item.trie)
                else:
                    observer.on_error(
                        "Unknown item type: {}".format(type(item)))

            sink.speech.subscribe(lambda item: on_deepspeech_request(item))

        return Source(
            text=Observable.create(subscribe)
        )

    return Component(call=driver, input=Sink)
