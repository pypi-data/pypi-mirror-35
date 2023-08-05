import logging
import time
from datetime import datetime
from itertools import product

import numpy as np
from sklearn.metrics import accuracy_score

from .modulators import IdentityModulator
from .messages import generate_data, unpack_to_bits, pack_to_dec, _generate_data_generator


def create_simulation_var_combinations(sim_var_params):
    """Generate a simulation variable dictionary for a CustomSimulation

    Parameters
    ----------
    sim_var_params : dict
        Dict containing the different variable names as keys and their values
        as values in a list.

    Returns
    -------
    sim_var : list
        List of all different simulation parameters.
    """
    sim_var = []
    for _val_tuple in product(*sim_var_params.values()):
        sim_var.append({k: v for k, v in zip(sim_var_params.keys(), _val_tuple)})
    return sim_var


def single_simulation(encoder, decoder, channel, modulator=IdentityModulator,
                      demodulator=IdentityModulator,
                      test_size=1e6, batch_size=50000, metric=['ber']):
    """Run a single simulation with fixed parameters.

    Parameters
    ----------
    encoder : Encoder
        Encoder instance which is used for encoding messages.

    decoder : Decoder
        Decoder instance which is used for decoding messages.

    channel : Channel
        Channel instance which is used for corrupting the transmitted messages.

    modulator : Modulator, optional
        Modulator instance which is used for modulating the codewords before
        transmission. The default is no modulation.

    demodulator : Demodulator, optional
        Demodulator instance which is used for demodulating the channel output
        before decoding. The default is no demodulation.

    test_size : int, optional
        Number of messages to be tested.

    batch_size : int, optional
        The number of messages which are processed within one batch. Increasing
        this number may cause memory issues.

    metric : list, optional
        List of metrics which are calculated and returned.
    

    Returns
    -------
    results : dict
        Dict containing all simulation results. The keys are the metrics and
        the values are the corresponding metric value.
    """
    test_size = int(test_size)
    code_length = encoder.code_length
    info_length = encoder.info_length

    errors = {k: 0 for k in metric}
    tx_messages_gen = _generate_data_generator(
        batch_size=batch_size, info_length=info_length,
        number=test_size)
    for tx_messages in tx_messages_gen:
        tx_messages_bit = unpack_to_bits(tx_messages, info_length)
        tx_codewords = encoder.encode_messages(tx_messages_bit)
        tx_modulated = modulator.modulate_symbols(tx_codewords)
        rx_modulated = channel.transmit_data(tx_modulated)
        rx_codewords = demodulator.demodulate_symbols(rx_modulated)
        rx_messages_bit = decoder.decode_messages(rx_codewords, channel)

        if 'ber' in metric:
            errors['ber'] += np.count_nonzero(tx_messages_bit != rx_messages_bit)/info_length
        if 'bler' in metric:
            rx_messages = pack_to_dec(rx_messages_bit)
            errors['bler'] += np.count_nonzero(np.ravel(tx_messages) != np.ravel(rx_messages))
    results = {k: v/test_size for k, v in errors.items()}
    return results


class TransmissionSimulation(object):
    """Generic class for transmission simulations"""
    def __init__(self, encoder, decoder, channel, modulator=None,
                 demodulator=None, logger=None):
        self.encoder = encoder
        self.modulator = IdentityModulator if modulator is None else modulator
        self.channel = channel
        self.demodulator = IdentityModulator if demodulator is None else demodulator
        self.decoder = decoder
        self.logger = logger

    def simulate(self, sim_var, test_size=1e6, metric=['bler', 'ber']):
        """Run a simulation with provided options.

        Parameters
        ----------
        sim_var : dict
            Dict of simulation variables and all their combinations.

        test_size : int, optional
            Number of test messages.

        metric : list (str), optional
            List of metrics that are calculated. Possible choices are "ber" for
            the bit error rate and "bler" for the block error rate.

        Returns
        -------
        results : dict
            Dict including all the results (metrics) for the evaluated
            simulation variables.
        """
        test_size = int(test_size)
        code_length = self.encoder.code_length
        info_length = self.encoder.info_length

        tx_messages = generate_data(info_length, number=test_size)
        tx_messages_bit = unpack_to_bits(tx_messages, info_length)
        tx_codewords = self.encoder.encode_messages(tx_messages_bit)
        tx_modulated = self.modulator.modulate_symbols(tx_codewords)
        results = {}
        for _options in channel_options:
            _options = tuple(_options)
            _channel = self.channel(*_options)
            rx_modulated = _channel.transmit_data(tx_modulated)
            rx_codewords = self.demodulator.demodulate_symbols(rx_modulated)
            rx_messages_bit = self.decoder.decode_messages(rx_codewords)

            result_metrics = {}
            if 'ber' in metric:
                result_metrics['ber'] = 1.-accuracy_score(
                    np.ravel(tx_messages_bit), np.ravel(rx_messages_bit))
            if 'bler' in metric:
                rx_messages = pack_to_dec(rx_messages_bit)
                result_metrics['bler'] = 1.-accuracy_score(tx_messages, rx_messages)

            results[_options] = result_metrics
        return results


class CustomSimulation(object):
    """Fully customizable tranmission simulation.
    
    Parameters
    ----------
    encoder : Encoder
        Class object of Encoder like class

    decoder : Decoder
        Class object of Decoder like class

    channel : Channel
        Class object of Channel like class

    modulator : Modulator, optional
        Class object of Modulator like class

    demodulator : Demodulator, optional
        Class object of Demodulator like class

    logger : Logger, optional
        Logger object from logging package
    """
    def __init__(self, encoder, decoder, channel, modulator=None,
                 demodulator=None, logger=None):
        self.encoder = encoder
        self.modulator = IdentityModulator if modulator is None else modulator
        self.channel = channel
        self.demodulator = IdentityModulator if demodulator is None else demodulator
        self.decoder = decoder
        self.logger = self._create_logger() if logger is None else logger
        #self.logger.info(self.__dict__)

    def _create_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        _log_date = datetime.fromtimestamp(time.time())
        log_date = datetime.strftime(_log_date, "%Y-%m-%d-%H-%M-%S")
        # Only log results (INFO) and WARN/ERR in file
        fh = logging.FileHandler('{}.dat'.format(log_date))
        fh.setLevel(logging.INFO)
        # Stream shows everything
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        file_form = logging.Formatter('%(message)s')  #.500s for truncating str
        con_form = logging.Formatter('%(asctime)s - %(levelname)8s - %(message)s')
        fh.setFormatter(file_form)
        ch.setFormatter(con_form)
        logger.addHandler(fh)
        logger.addHandler(ch)
        return logger#, log_date

    @staticmethod
    def _default_empty_if_none(x):
        return {} if x is None else x

    def simulate(self, simulation_parameters, channel_options,
                 enc_opt=None, dec_opt=None,
                 mod_opt=None, demod_opt=None, training_opt=None, **kwargs):
        self.logger.info(self.__dict__)
        enc_opt = self._default_empty_if_none(enc_opt)
        dec_opt = self._default_empty_if_none(dec_opt)
        mod_opt = self._default_empty_if_none(mod_opt)
        demod_opt = self._default_empty_if_none(demod_opt)
        self.logger.info(enc_opt)
        self.logger.info({k: v for k, v in dec_opt.items() if k != "training_data"})
        self.logger.info(mod_opt)
        self.logger.info(demod_opt)
        self.logger.info(kwargs)

        self.logger.debug("Start simulation...")
        results = {}
        for idx, parameters in enumerate(simulation_parameters):
            #self.logger.info("{}|{}".format(idx, parameters))
            _key = tuple([(k, v) for k, v in parameters.items()])
            self.logger.info(_key)
            results[_key] = {}
            self.logger.debug("Creating encoder...")
            encoder = self.encoder(**{**enc_opt, **parameters})
            modulator = self.modulator(**{**mod_opt, **parameters})
            demodulator = self.demodulator(**{**demod_opt, **parameters})
            self.logger.debug("Creating decoder...")
            decoder = self.decoder(**{**dec_opt, **parameters})
            if training_opt is not None:
                self.logger.debug("Start training...")
                decoder.train_system((encoder, modulator), **training_opt)
                self.logger.debug("...Training finished")
            for _channel_options in channel_options:
                try:
                    _channel_options = tuple(_channel_options)
                except TypeError:
                    _channel_options = (_channel_options,)
                channel = self.channel(*_channel_options)
                results[_key][_channel_options] = single_simulation(
                    encoder=encoder, decoder=decoder, modulator=modulator,
                    demodulator=demodulator, channel=channel, **kwargs)
                self.logger.debug("{}: {}".format(_channel_options, results[_key][_channel_options]))
            self.logger.info(results[_key])
        return results


class WiretapSimulation(CustomSimulation):
    """Simulation class for wiretap channel simulations."""
    def simulate(self, **kwargs):
        pass
