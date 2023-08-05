import numpy as np

from . import channels

def get_info_length(code_length, channel, channelstate):
    rate = channel_capacity(channel, channelstate)
    info_length = int(np.floor(code_length*rate))
    return info_length


def channel_capacity(channel, channelstate=None):
    if isinstance(channel, channels.Channel):
        capacity = channel.capacity()
    elif channel == "BAWGN":
        capacity = _capacity_bawgn(channelstate)
    return capacity


def _phi(x, sigsq):
    return 1./(np.sqrt(8*np.pi*sigsq)) * (np.exp(-(x-1)**2/(2*sigsq))+np.exp(-(x+1)**2/(2*sigsq)))

def _integrand(x, sigsq):
    return _phi(x, sigsq)*np.log2(_phi(x, sigsq))

def _capacity_bawgn(snr):
    sigsq = 1./(10**(snr/10.))
    #integral = integrate.quad(lambda x: _integrand(x, sigsq), -np.inf, np.inf)
    x = np.linspace(-1-10*np.sqrt(sigsq), 1+10*np.sqrt(sigsq), num=4000)
    y = _integrand(x, sigsq)
    integral = np.trapz(y, x)
    capacity = -integral - .5*np.log2(2*np.pi*np.e*sigsq)
    return capacity


def entropy(prob):
    """Calculate the Shannon entropy of a discrete random variable.

    Parameters
    ----------
    prob : list (float)
        List of probabilities of the random variable.

    Returns
    -------
    entr : float
        Entropy in bits.
    """
    if not sum(prob) == 1:
        raise ValueError("The probabilities have to sum up to one")
    prob = np.array(prob)
    prob = prob[prob != 0]
    entr = -np.sum(prob * np.log2(prob))
    return entr


def binary_entropy(prob):
    """Calculate the Shannon entropy of a binary random variable.

    Parameters
    ----------
    prob : float
        Probability of one event.

    Returns
    -------
    entr : float
        Entropy in bits.
    """
    if prob == 0 or prob == 1:
        return 0.
    else:
        return -prob*np.log2(prob)-(1.-prob)*np.log2(1.-prob)
