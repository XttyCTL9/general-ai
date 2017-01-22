class ReinforcementParameters():
    """
    Encapsulates parameters of for reinforcement learning.
    """

    @staticmethod
    def get_empty_params():
        return ReinforcementParameters(
            batch_size=None,
            epochs=None,
            penalty=None,
            gamma=None,
            base_reward=None,
            dropout=None,
            optimizer=None)

    @staticmethod
    def from_dict(data):
        params = ReinforcementParameters(
            data["batch_size"],
            data["epochs"],
            data["penalty"],
            data["gamma"],
            data["base_reward"],
            data["dropout"],
            data["optimizer"],
            data["learning_rate"])
        return params

    def __init__(self,
                 batch_size,
                 epochs,
                 penalty,
                 gamma,
                 base_reward,
                 dropout,
                 optimizer,
                 learning_rate=0.001):
        self.batch_size = batch_size
        self.epochs = epochs
        self.penalty = penalty
        self.gamma = gamma
        self.base_reward = base_reward
        self.dropout = dropout
        self.optimizer = optimizer
        self.learning_rate = learning_rate

    def to_dictionary(self):
        data = {}
        data["batch_size"] = self.batch_size
        data["epochs"] = self.epochs
        data["penalty"] = self.penalty
        data["gamma"] = self.gamma
        data["base_reward"] = self.base_reward
        data["dropout"] = self.dropout
        data["optimizer"] = self.optimizer
        data["learning_rate"] = self.learning_rate
        return data

    def to_string(self):
        return "penalty: {}, gamma: {}, base_reward: {}, dropout: {}, optimizer: {}, lr: {}, batch_size: {}, epochs: {}".format(
            self.penalty, self.gamma, self.base_reward, self.dropout, self.optimizer, self.learning_rate,
            self.base_reward, self.epochs)
