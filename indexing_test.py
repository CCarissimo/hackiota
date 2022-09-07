import iota_client
import os
LOCAL_NODE_URL = "https://api.lb-0.h.chrysalis-devnet.iota.cafe/:443"

# NOTE! Load the seed from your env path instead
# NEVER assign the seed directly in your codes!
# DO NOT USE THIS!!:
SEED = "256a818b2aac458941f7274985a410e57fb750f3a3a67969ece5bd9ae7eef5b2"

# USE THIS INSTEAD
#SEED = os.getenv('MY_IOTA_SEED')

EMPTY_ADDRESS = "atoi1qzt0nhsf38nh6rs4p6zs5knqp6psgha9wsv74uajqgjmwc75ugupx3y7x0r"
client = iota_client.Client(
    nodes_name_password=[[LOCAL_NODE_URL]], node_sync_disabled=True)
    

def main():
    ind = "jiosdjfiojdasiofjoisdshdaifhsdifanhivbdsafojdsof"
    # Get the (address, changed ) for the first found address
    message_id_indexation = client.message(
        index=ind, data_str="hello there")
    #print(f'Indexation sent with message_id: {message_id_indexation}')

    messages = client.find_messages(indexation_keys=[ind])
    #print(f'Messages: {messages}')

    for msg in messages:
        print(msg['payload']['indexation'][0]['data'])


if __name__ == "__main__":
    main()
