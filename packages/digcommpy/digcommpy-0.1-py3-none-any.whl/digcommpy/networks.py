from abc import ABC, abstractmethod

class Network(object):
    """Basic class for communications network"""
    def __init__(self, *args):
        self.users = list(args)
        self.connections = {}

    def add_user(self, user):
        """Add a user to the network.

        Parameters
        ----------
        user : User
            New user to be added.
        """
        self.users.append(user)

    def add_connection(self, src, dst, channel, symm=True):
        """Add a connection between two users.

        Parameters
        ----------
        src : User
            Source user

        dst : User
            Destination user

        channel : Channel
            Noise distribution on the channel between `src` and `dest`

        symm : bool, optional
            If True, the connection is added symmetrically
        """
        if src not in self.users:
            raise ArgumentError("The source user is not in the network!")
        elif dst not in self.users:
            raise ArgumentError("The destination user is not in the network!")
        if (src, dst) not in self.connections:
            self.connections[(src, dst)] = channel
        if symm:
            self.add_connection(dst, src, channel, symm=False)


class PointToPoint(Network):
    """Point to Point transmission network between two users"""
    def __init__(self, *args):
        if len(args) >=2:
            self.users = [args[0], args[1]]
        if len(args) == 3:
            self.add_connection(args[0], args[1], args[2], symm=True)
