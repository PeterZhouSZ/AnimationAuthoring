import numpy as np
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from MANN import MANN


num_joints  = 27
num_styles  = 9
datapath    = './data'
savepath    = './training'
num_experts = 8
index_gatingIn = [321, 322, 323,
                  381, 382, 383,
                  429, 430, 431,
                  477, 478, 479,
                  102,  103,  104, 105, 106, 107, 108, 109, 110, 111]
def main():
    rng  = np.random.RandomState(23456)
    sess = tf.Session()
    mann = MANN(num_joints,
                num_styles,
                rng,
                sess,
                datapath, savepath,
                num_experts,
                hidden_size = 512,
                hidden_size_gt = 32,
                index_gating = index_gatingIn,
                batch_size = 32 , epoch = 150, Te = 10, Tmult =2,
                learning_rate_ini = 0.0001, weightDecay_ini = 0.0025, keep_prob_ini = 0.7)

    mann.build_model()
    mann.train()


if __name__ =='__main__':
    main()
