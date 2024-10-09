import yaml
from .kineva import *
import torch
import os
from loguru import logger
from ..utils import dictConfig

def load_model(cfg_file, nc=None) -> Model:

    def init_weight(M):
        from torch import nn
        for m in M.modules():
            if isinstance(m, nn.BatchNorm2d):
                m.eps = 1e-3
                m.momentum = 0.03

    

    my_model = Model(cfg_file, nc=nc, is_file=not (isinstance(cfg_file, dict) or not os.path.isfile(cfg_file)))
    my_model.apply(init_weight)
    return my_model

class Kineva:

    model = None
    cfg_d = None
    optimizer = None
    dataloader = None
    evaluator = None
    lr_scheduler = None
    loss = None
    start_epoch = 0
    now_epoch = 0
    input_size = [640, 640]
    class_names = []
    rank = 0
    is_match = True
    ckpt = {}
    is_pretrain_mode = False

    def __init__(self, cfg_file=None, weights=None, rank=0, write_cfg_to_weights=False, nc=None):
        self.rank = rank
        assert cfg_file is not None or weights is not None
        
       
        self.__weights = weights
        if weights is not None and os.path.isfile(weights):
            if not rank:
                logger.info(f"loading models from weight {os.path.abspath(weights)}")
            self.ckpt = torch.load(weights, map_location="cpu")
            if write_cfg_to_weights:
                if cfg_file is not None:
                    self.ckpt["cfg_data"] = open(cfg_file, "r", encoding="utf8").read()
                    if not rank:
                        logger.info(f"use cfg data {cfg_file}")
                        f = os.path.join(os.path.dirname(weights),
                                         os.path.basename(weights).split(".")[0] + "(cfg_change).pth")
                        torch.save(self.ckpt, f)


            if isinstance(self.ckpt["cfg_data"], str):
                try:
                    self.ckpt["cfg_data"] = yaml.load(self.ckpt["cfg_data"], yaml.SafeLoader)
                except:
                    pass
            
            if not self.ckpt["cfg_data"]["nc"] == len(self.ckpt["class_names"]):
                self.ckpt["cfg_data"]["nc"] = len(self.ckpt["class_names"])
                torch.save(self.ckpt, weights)

            restart = False
            if nc is not None:
                if not self.ckpt["cfg_data"]["nc"] == nc:
                    restart = True
                self.ckpt["cfg_data"]["nc"] = nc
            self.cfg_data = self.ckpt["cfg_data"]

            self.model = load_model(self.cfg_data, nc=self.ckpt["cfg_data"]["nc"])
            try:
                self.model.load_state_dict(self.ckpt["model"], strict=False)
            except Exception as e:
                logger.info(e)
                self.is_match = self.try_load_state_dict(self.ckpt["model"])
            if ("pretrain_epoch" if self.is_pretrain_mode else "epoch") in self.ckpt and not restart:
                self.start_epoch = self.ckpt["pretrain_epoch" if self.is_pretrain_mode else "epoch"] + 1
                self.now_epoch = max(0, self.start_epoch - 1)
            if "class_names" in self.ckpt:
                self.class_names = self.ckpt["class_names"]
                # print(self.ckpt["class_names"])
        elif isinstance(cfg_file, dict) or (cfg_file is not None and os.path.isfile(cfg_file)):
            if not isinstance(cfg_file, dict):
                if not rank:
                    logger.info(f"no weight file found, setup models from cfg file {os.path.abspath(cfg_file)}")
                self.cfg_data = open(cfg_file).read()
            else:
                if not rank:
                    logger.info("no weight file found, setup models from cfg dict")
                self.cfg_data = cfg_file

            self.model = load_model(cfg_file, nc=nc)

        else:
            logger.error("no weights and cfg found!")
            assert False



    def get_model_size(self, input_size=None):
        from ..utils import get_model_info
        return get_model_info(self.model, self.input_size if input_size is None else input_size)

    def info(self, info):
        if self.rank == 0:
            logger.info(info)

    def warning(self, warning):
        if self.rank == 0:
            logger.warning(warning)

    def error(self, err):
        if self.rank == 0:
            logger.error(err)
