from collections import Counter

counter = Counter()

a = {'a':[1,2,3,5,4],'b':[3,2,1,5], 'c':[4,3,6],'d':[7,5,43,6,7]}

for user, items in a.items() :
    counter.update(items)

print(counter)
print(counter.most_common(10000))

from collections import Counter

import json
import numpy as np
import torch
import os
import time
from model import Encoder
from data_utils import melData


def cosine_similarity(x1, x2):
    return (x1 * x2).sum() / ((x1**2).sum()**.5 * (x2**2).sum()**.5)

def get_recommends(user, items,item_id, top=100) :
    similarities = []

    for item in items :
        similarities.append(cosine_similarity(user,item))

    item_similar_map = list(zip(item_id, similarities))

    similarities = sorted(item_similar_map, key=lambda x :(-x[1],x[0]))

    recommends =  [id for id,sim in similarities[:top]]

    return recommends


os.environ["CUDA_VISIBLE_DEVICES"] = "3"

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


start_time = time.time()

predictions = json.load(open("../CF/NCF/preds/pred_5.txt"))
data_set = melData("/root/data/arena_mel/", is_training=False)

print("START")
zx=time.time()
# imageset = set()
# for user,item in predictions.items() :
#     imageset.add(user)
#     imageset = imageset | set(item[0])
counter = Counter()

for user, items in predictions.items() :
    counter.update(items)

data_set.load_all_image(counter.most_common(40000))
print("END : ",time.time()-zx)


encoder = Encoder().cuda()
encoder.load_state_dict(torch.load('./models/encoder_9.pth'))
answer = {}
cnt = 0
for user_id, item_ids in predictions.items() :
    cnt+=1
    item_ids = item_ids[0]
    user = data_set.make_user(user_id)
    data_set.make_batch(item_ids, batch_size=64)

    user = encoder(user.cuda())
    items = torch.tensor([]).cuda()
    for X in data_set :
        items = torch.cat([items, encoder(X.to(device))])
    recommends= get_recommends(user,items,item_ids,top=75)
    #print(recommends[:10])
    answer[user] = recommends

elapsed_time = time.time() - start_time
print("The time elapse is {}".format(time.strftime("%H: %M: %S", time.gmtime(elapsed_time))))


with open(os.path.join("./pred_top75_.txt"), "w") as fp :
    fp.write(json.dumps(answer))
