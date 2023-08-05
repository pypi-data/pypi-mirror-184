from typing import Dict

try:
    import tensorflow as tf
except ImportError:
    raise ImportError('tensorflow package is required')

import copy

import deepdriver
from deepdriver import logger


class MLCallback(tf.keras.callbacks.Callback):

    def __init__(self):
        pass

    def on_epoch_end(self, epoch: int, logs: Dict = {}):
        logger.debug(f"logs:{logs}")
        logger.debug(f"epoch:{epoch}")

        to_send_log = copy.deepcopy(logs)
        if "accuracy" in logs:
            to_send_log["acc"] = logs["accuracy"]

        if "val_accuracy" in logs:
            to_send_log["val_acc"] = logs["val_accuracy"]

        logger.debug(f"to_send_logs:{to_send_log}")
        deepdriver.log(to_send_log)
