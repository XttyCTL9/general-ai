import json
import os

from models.model import Model
from reinforcement.ddpg.ddpg_reinforcement import DDPGReinforcement
from reinforcement.reinforcement_parameters import DDPGParameters


class LearnedDDPG(Model):
    def __init__(self, logdir):
        self.metadata = None
        for file in os.listdir(logdir):
            if file.endswith(".json"):
                with open(os.path.join(logdir, file), "r") as f:
                    self.metadata = json.load(f)
                    break

        self.game = self.metadata["game"]
        self.parameters = DDPGParameters.from_dict(self.metadata["parameters"])
        self.ddpg = DDPGReinforcement(self.game, self.parameters)
        self.ddpg.load_checkpoint(logdir)

    def get_new_instance(self, weights, game_config):
        raise NotImplementedError

    def evaluate(self, input, current_phase):
        action = self.ddpg.agent.play(input, None)
        action_string = ""
        for a in action:
            action_string += str(a) + " "
        return action_string

    def get_name(self):
        return "Learned DDPG Agent (Reinforcement Learning)"

    def get_class_name(self):
        return "LearnedDDPG"
