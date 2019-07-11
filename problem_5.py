import hashlib
from datetime import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.previous_block = None

    def calc_hash(self):
      sha = hashlib.sha256()
      tmp_str = "%s%s%s" % (self.timestamp, self.data, self.previous_hash)
      hash_str = tmp_str.encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()

    def get_hash(self):
        return self.hash

    def has_previous_hash(self):
        return self.previous_hash is not None

    def add_previous_hash(self, previous_hash):
        self.previous_hash = previous_hash

    def set_previous_block(self, block):
        self.previous_block = block

    def has_previous_block(self):
        return self.previous_block is not None

    def get_previous_block(self):
        return self.previous_block


class BlockChain(object):
    def __init__(self, timestamp, data, previous_hash):
        self.block = Block(timestamp, data, previous_hash)

    def add_block(self, timestamp, data):
        previous_hash = self.block.get_hash()
        newBlock = Block(timestamp, data, previous_hash)
        newBlock.set_previous_block(self.block)
        self.block = newBlock

    def print_block_chain(self):

        temp_block = self.block
        while temp_block.has_previous_block():
            print("Block's current hash:", temp_block.get_hash(), "Previous Hash", temp_block.previous_hash)
            temp_block = temp_block.get_previous_block()
        # should print None for previous hash in the below line because we reached first block that has no previous hash
        print("Block's current hash:", temp_block.get_hash(), "Previous Hash", temp_block.previous_hash)


#Test case 1
bc = BlockChain(datetime.utcnow(),
                "Super Sensitive2", None)

bc.add_block(datetime.utcnow(),
             "Super Sensitive3")

bc.add_block(datetime.utcnow(),
             "Super Sensitive4")

#Block's current hash: b4c86a102db11d541ba9376e346d0f63ba822b33653fef1e8b64050bd595cd2c Previous Hash 9a5280780db83f7b81ed52d950837c34922cd7b57bbd6a7fbc8977963ac0ab38
#Block's current hash: 9a5280780db83f7b81ed52d950837c34922cd7b57bbd6a7fbc8977963ac0ab38 Previous Hash 2de8646b617a26642a016e45c7b247425a83e41040ad5d58b9dfebc833adc152
#c7b247425a83e41040ad5d58b9dfebc833adc152
bc.print_block_chain()

#Test case 2
bc = BlockChain(datetime.utcnow(),
                "", None)

bc.add_block(datetime.utcnow(),
             "Hello")

bc.add_block(datetime.utcnow(),
             "Super Sensitive5")

#Block's current hash: 299c4edd36d5138942cdffd0c7d82926990e02048d218e39d042388f0123adea Previous Hash d5ed355dc10f97849f89732f0ba83c9d315c241b87ea290bee1223083a134f81
#Block's current hash: d5ed355dc10f97849f89732f0ba83c9d315c241b87ea290bee1223083a134f81 Previous Hash 4e730cd00912e34d395e21c81b57baaf98fc63683712fa8d3efd5f2ec7d57f76
#Block's current hash: 4e730cd00912e34d395e21c81b57baaf98fc63683712fa8d3efd5f2ec7d57f76 Previous Hash None
bc.print_block_chain()

#Test case 3
bc = BlockChain(datetime.utcnow(),   #Edge case
                "Super Sensitive6", None)
bc.print_block_chain()  #Block's current hash: 8a9ec45b578bec55a8ca70aa579bca7778f7c492e4652672df63501a94e25f7c Previous Hash None









