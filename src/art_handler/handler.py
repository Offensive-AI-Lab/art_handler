import traceback
import json
import logging
from importlib import import_module
from .helpers import get_map_root
class ArtHandler:
    def __init__(self):
        with open(get_map_root() + "/attack_defense_map.json", 'r') as f:
            self.map = json.load(f)


    def get(self, defense_or_attack_str, specifics=None):
        """
        :param - defense_or_attack_str: either attack or defense as str
        :param(optional) - list of specific attacks or defenses in class path form.
         If specifics is None than all attacks or defenses will return
        :return: nested dict where each dict contains object and metadata

        Example:
        specifics = [ 'art.defences.postprocessor.class_labels.ClassLabels',
                    'art.defences.postprocessor.gaussian_noise.GaussianNoise']


        """
        if defense_or_attack_str == "attack":
            dicts = self.map['attacks'].values()

        elif defense_or_attack_str == "defense":
            dicts = self.map['defenses'].values()
        else:
            raise ValueError(f"Expected attack or defense, got: {defense_or_attack_str}")
        if specifics:
            specifics = list(specifics.values())[0]
            specific_dicts = []
            for d in dicts:
                if d['class_name'] in specifics:
                    specific_dicts.append(d)
            dicts = specific_dicts
        for d in dicts:
            try:
                path = d['class_name']
                split_idx = path.rfind(".")
                art_path = path[:split_idx]
                object = path[split_idx + 1:]
                d['obj'] = (getattr(import_module(art_path), object))

            except Exception as err:
                logging.error(f"{object} can not be imported!")
                logging.error(traceback.format_exc())
                d['obj'] = None

        return dicts

    def get_package_root(self):
        return get_map_root()

a =ArtHandler()
print(a.get(('defense')))