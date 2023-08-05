import numpy as np

from .messages import generate_data
from .encoders import IdentityEncoder
from .decoders import IdentityDecoder
from .modulators import IdentityModulator


class User(object):
    """Regular user in communication scenario
    
    Parameters
    ----------
    encoder : Encoder, optional
        Encoder class which will be used to encode messages. If `None`, the
        identity coder will be used.

    decoder : Decoder, optional
        Decoder class which will be used to decode the channel output. If
        `None`, the identity decoder will be used.

    modulator : Modulator, optional
        Modulator class which will be used to modulate the encoded symbols.
        If `None`, the identity modulator will be used.

    messages : array, optional
        This can be set to be an array of fixed messages which will be 
        transmitted in every transmission. Set it to `None` if messages should
        be generated randomly.

    name : str, optional
        Name of the user which is used for printing the object.
    """
    def __init__(self, encoder=None, decoder=None, modulator=None,
                 messages=None, name="User"):
        self.name = name
        self.messages = messages
        if not encoder:
            self.encoder = IdentityEncoder
        else:
            self.encoder = encoder
        if not decoder:
            self.decoder = IdentityDecoder
        else:
            self.decoder = decoder
        if not modulator:
            self.modulator = IdentityModulator
        else:
            self.modulator = modulator
        self.received = []
        self.estimated = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def _generate_messages(self, **kwargs):
        self.messages = generate_data(**kwargs)

    def _encode_messages(self):
        return self.encoder.encode_messages(self.messages)

    def _modulate_codewords(self, codewords):
        return self.modulator.modulate_symbols(codewords)

    def _decode_messages(self):
        return self.decoder.decode_messages(self.receive_messages)

    def generate_channel_input(self, generate_messages=False):
        """Generate channel input data
        
        Parameters
        ----------
        generate_messages : dict, optional
            Dict with options to generate new data. If empty, the previously
            generated messages will be used. Options are input of function
            `.message.generate_data`.

        Returns
        -------
        channel_input : array
            Array of the channel inputs (encoded and modulated messages)
        """
        if self.messages is None or generate_messages:
            self._generate_messages(**generate_messages)

        codewords = self._encode_messages()
        modulated = self._modulate_codewords(codewords)
        return modulated

    def receive_messages(self, channel_output):
        self.received = channel_output
        self.estimated = self._decode_messages()
