# You want to implement a state machine or an object that operates in
# a number of different states, but don’t want to litter your code
# with a lot of conditionals.


# Instead of all this "ifs" we'll use delegation
class ConnectionOld:
    def __init__(self):
        self.state = "CLOSED"

    def open(self):
        if self.state == "OPENED":
            raise RuntimeError('Connection is already opened')
        # ....
        self.state = 'OPENED'

    def read(self):
        if self.state != 'OPENED':
            raise RuntimeError('Connection is not opened')
        # ....

    def close(self):
        if self.state != 'OPENED':
            raise RuntimeError('Connection is not opened')
        # ....
        self.state = 'CLOSED'


# using delegation
class StateConnection:
    @staticmethod
    def open(connection):
        raise NotImplementedError

    @staticmethod
    def read(connection):
        raise NotImplementedError

    @staticmethod
    def close(connection):
        raise NotImplementedError


class StateConnectionClosed(StateConnection):
    @staticmethod
    def open(connection):
        # ...
        connection.new_state(StateConnectionOpened)

    @staticmethod
    def read(connection):
        raise RuntimeError('Connection is not opened')

    @staticmethod
    def close(connection):
        raise RuntimeError('Connection is not opened')


class StateConnectionOpened(StateConnection):
    @staticmethod
    def open(connection):
        raise RuntimeError('Connection is already opened')

    @staticmethod
    def read(connection):
        pass

    @staticmethod
    def close(connection):
        # ...
        connection.new_state(StateConnectionClosed)


class Connection:
    def __init__(self):
        self.new_state(StateConnectionClosed)

    def new_state(self, new_state_cls):
        self.state = new_state_cls

    def open(self):
        self.state.open(self)

    def read(self):
        return self.state.read(self)

    def close(self):
        self.state.close(self)


# 2. Second variant - not very "object oriented"
# as the __class__ attribute of the instance is changed

class StateOld:
    def __init(self):
        self.state = 'A'

    def action(self):
        if self.state == 'A':
            # ...
            self.state = 'B'
        elif self.state == 'B':
            # ...
            self.state = 'C'
        elif self.state == 'C':
            # ...
            self.state = 'A'


#  changing the instance's __class__ attribute
class State:
    def _init(self):
        self._new_state(StateA)

    def _new_state(self, action_cls):
        self.__class__ = action_cls

    def action(self):
        raise NotImplementedError


class StateA(State):
    def action(self):
        # ...
        self._new_state(StateB)


class StateB(State):
    def action(self):
        # ...
        self._new_state(StateC)


class StateC(State):
    def action(self):
        # ...
        self._new_state(StateA)
