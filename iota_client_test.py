import iota_client

# create a client with a node
client = iota_client.Client(
    nodes_name_password=[['https://api.thin-hornet-0.h.chrysalis-devnet.iota.cafe/']])

print(client.get_info())

message = client.message(index="0", data_str="test")
print(message)


message = client.get_message_data(message["message_id"])
message_meta = client.get_message_metadata(message["message_id"])

print("Message meta data:")
print(message_meta)
print("Message data:")
print(message)

