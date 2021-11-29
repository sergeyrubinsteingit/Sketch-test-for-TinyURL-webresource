###################################################
# A script to generate random hash
import random


gener_hash_: str
def generate_hash():
    global gener_hash_
    #  md5-hash is just a 128-bit value;
    gener_hash_ = str(random.getrandbits(128))[:10] #  stringed to let limitate a number of digits to 10
    print(gener_hash_)

if __name__ == '__main__':
    generate_hash()