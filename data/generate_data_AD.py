from itertools import chain

import pickle

from argparse import ArgumentParser

import random

def main(args):
    partition = {"separation": None, "data_indices": None}
    video_num_partition = {"video_num" : None}

    train_list = list(open('C:/Users/User/PycharmProjects/FL_AD/UCF_Train_ten_crop_i3d_complete_V1.txt'))
    test_list = list(open('C:/Users/User/PycharmProjects/FL_AD/UCF_Test_ten_crop_i3d_complete_V1.txt'))

    clients_num = args.client_num
    clients_4_train = list(range(clients_num))
    clients_4_test = list(range(clients_num))

    partition["separation"] = {
        "train": clients_4_train,
        "test": clients_4_test,
        "total": clients_num,
    }
    data_indices = [[] for _ in range(clients_num)]
    data_indices1 = [[] for _ in range(clients_num)]
    partition["data_indices"] = data_indices
 

    video_num_partition["data_indices"] = data_indices1

    train_videos_num = args.train_vid_num
    test_videos_num = args.test_vid_num


    # Create an array of 1610 numbers (replace this with your actual array)
    all_numbers_train = list(range(train_videos_num))

    # Define the number of agents and calculate the chunk size
    num_agents = clients_num
    chunk_size = len(all_numbers_train) // num_agents

    # Shuffle the array randomly to ensure IID distribution
    random.shuffle(all_numbers_train)

    # Divide the shuffled array into chunks for each agent
    agents_data_train = [all_numbers_train[i * chunk_size:(i + 1) * chunk_size] for i in range(num_agents)]

    # If there's any remaining data, distribute it evenly among the agents
    remaining_data = all_numbers_train[num_agents * chunk_size:]
    for i, num in enumerate(remaining_data):
        agents_data_train[i % num_agents].append(num)


    all_numbers_test = list(range(test_videos_num))

    # Define the number of agents and calculate the chunk size
    num_agents = clients_num
    chunk_size = len(all_numbers_test) // num_agents

    # Shuffle the array randomly to ensure IID distribution
    random.shuffle(all_numbers_test)

    # Divide the shuffled array into chunks for each agent
    agents_data_test = [all_numbers_test[i * chunk_size:(i + 1) * chunk_size] for i in range(num_agents)]

    # If there's any remaining data, distribute it evenly among the agents
    remaining_data = all_numbers_test[num_agents * chunk_size:]
    for i, num in enumerate(remaining_data):
        agents_data_test[i % num_agents].append(num)


    # for i in range(clients_num):
    #     partition["data_indices"][i] = {"train": agents_data_train[i], "test": agents_data_test[i]}

    for i in range(clients_num):
        partition["data_indices"][i] = {"train": agents_data_train[i], "test": None}
        video_num_partition["data_indices"][i] = {"train": agents_data_train[i]}
        # break


    with open(f"C:/Users/User/PycharmProjects/FL_AD/data/ucf/video_num_partition_{clients_num}_V3.pkl", "wb") as f:
        pickle.dump(video_num_partition, f)


   
    for i in range(clients_num):

        for k,v in enumerate(partition["data_indices"][i]["train"]):
            from_id = train_list[v].split('\n')[0].split(',')[1]
            to_id = train_list[v].split('\n')[0].split(',')[2]
            partition["data_indices"][i]["train"][k] = list(range(int(from_id), int(to_id))) 
            
        # break
        partition["data_indices"][i]["train"]= list(chain(*partition["data_indices"][i]["train"]))

    


    # for i in range(clients_num):

    #     for k,v in enumerate(partition_features["data_indices"][i]['test']):
    #         from_id = test_list[v].split('\n')[0].split(',')[1]
    #         to_id = test_list[v].split('\n')[0].split(',')[2]
    #         partition_features["data_indices"][i]['test'][k] = list(range(int(from_id), int(to_id))) 
            
    #     # break
    #     partition_features["data_indices"][i]['test']= list(chain(*partition_features["data_indices"][i]['test']))
    test_set_all_indices = 69634
    for i in range(clients_num):

            
        # break
        partition["data_indices"][i]['test']= list(range(test_set_all_indices))





    


    with open(f"C:/Users/User/PycharmProjects/FL_AD/data/ucf/partition_{clients_num}_V3.pkl", "wb") as f:
        pickle.dump(partition, f)




if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-d",
        "--dataset",
        type=str,
        choices=[
            "mnist",
            "cifar10",
            "cifar100",
            "synthetic",
            "femnist",
            "emnist",
            "fmnist",
            "celeba",
            "medmnistS",
            "medmnistA",
            "medmnistC",
            "covid19",
            "svhn",
            "usps",
            "tiny_imagenet",
            "cinic10",
            "ucf",
        ],
        default="ucf",
    )
    # parser.add_argument("--iid", type=int, default=0)
    parser.add_argument("-cn", "--client_num", type=int, default=25)
    parser.add_argument("-trv", "--train_vid_num", type=int, default=1608)
    parser.add_argument("-tev", "--test_vid_num", type=int, default=290)
    # parser.add_argument("--seed", type=int, default=42)
    # parser.add_argument(
    #     "--split", type=str, choices=["sample", "user"], default="sample"
    # )
    # parser.add_argument("-f", "--fraction", type=float, default=0.5)
    # parser.add_argument("-c", "--classes", type=int, default=0)
    # parser.add_argument("-s", "--shards", type=int, default=0)
    # parser.add_argument("-a", "--alpha", type=float, default=0)
    # parser.add_argument("-ls", "--least_samples", type=int, default=40)

    # # For synthetic data only
    # parser.add_argument("--gamma", type=float, default=0.5)
    # parser.add_argument("--beta", type=float, default=0.5)
    # parser.add_argument("--dimension", type=int, default=60)

    # # For CIFAR-100 only
    # parser.add_argument("--super_class", type=int, default=0)

    # # For EMNIST only
    # parser.add_argument(
    #     "--emnist_split",
    #     type=str,
    #     choices=["byclass", "bymerge", "letters", "balanced", "digits", "mnist"],
    #     default="byclass",
    # )

    # # For semantic partition only
    # parser.add_argument("-sm", "--semantic", type=int, default=0)
    # parser.add_argument("--efficient_net_type", type=int, default=0)
    # parser.add_argument("--gmm_max_iter", type=int, default=100)
    # parser.add_argument(
    #     "--gmm_init_params", type=str, choices=["random", "kmeans"], default="kmeans"
    # )
    # parser.add_argument("--pca_components", type=int, default=256)
    # parser.add_argument("--use_cuda", type=int, default=1)
    args = parser.parse_args()
    main(args)