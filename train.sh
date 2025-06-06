    python ./src/server/fedavg.py \
        -d ucf \
        -m c2fpl_ucf \
        --train_mode US \
        --global_testset 0 \
        -bs 128 \
        --global_epoch 1 \
        --local_epoch 10 \
        --partition scene_partition_11_V3.pkl \
        --partition_chain scene_partition_chain_11_V3.pkl \
        --video_num_partition scene_video_num_partition_11_V3.pkl \
        --datasplit scene \
        --test_gap 1 \
        --join_ratio 1 \
        --gmm_pl 1 \
        --eta_clustering 0 \
        --load 0 \
        --seed 42\

