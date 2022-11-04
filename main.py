# Importing the panda package and assigning pd to it
import hashlib
import json

import pandas as pd

askCsv = input('Enter csv path: ')
print('Loading ...')
# reading the csv files -> df(data frame)
df = pd.read_csv(askCsv)  # passing the file path of the csv file
df = df.ffill()

# hng9nft_teams.csv
# Hashing the JSON file -> declaring a function to do the hashing
def sha256digest(filename):
    return hashlib.sha256(open(filename, 'rb').read()).hexdigest()


# Create an empty list
listHash = []
# Going over or Iterating the csv line by line for the JSON file
for a, b in df.iterrows():
    attributes_list = []
    attributes = b[6]
    attributes = attributes.split(";")
    if attributes[-1] == '':
        attributes.remove('')
    for attr in attributes:
        attr_map = attr.split(":")
        attr_name = attr_map[0].strip()
        attr_value = attr_map[1].strip()
        attributes_list.append({"trait_type": attr_name, "value": attr_value})

    '''
    Dictionaries in python
    '''
    chip = {}
    chip['format'] = 'CHIP-0007'
    chip['name'] = b[3]
    chip['description'] = b[4]
    chip['minting_tool'] = b[0]  # adding minting_tool
    chip['sensitive_content'] = False
    chip['seriesNumber'] = b[1]
    chip['series_total'] = 420
    chip['attributes'] = attributes_list

    # Creating another dictionary for attribute
    chip_attributes = {}
    chip_attributes['type'] = 'Zuri NFT Tickets for Free Lunch'
    chip_attributes['value'] = 'Rewards for accomplishments'
    # Creating another dictionary for collection
    chip_collection = {}
    chip_collection['name'] = 'Zuri NFT Tickets for Free Lunch'
    chip_collection['id'] = 'b774f676-c1d5-422e-beed-00ef5510c64d'

    # adding the attributes to collection
    chip_collection['attributes'] = chip_attributes

    # adding the collection to chip
    chip['collection'] = chip_collection

    # Serializing json
    with open(b[2] + ".json", "w") as outfile:  # writing a dictionary into the json file
        json.dump(chip, outfile, indent=4)
        # print(chip)
    hashJs = sha256digest(b[2] + ".json")
    # print(hashJs)
    # append hashJs into the empty list
    listHash.append(hashJs)

# added a new hash column to the csv
df['Hashes'] = listHash

# creating a new csv file
df.to_csv("hng9nft_teams.output.csv", index=False)

print('Done!! The final csv file is found in the hng9nft_teams.output.csv')