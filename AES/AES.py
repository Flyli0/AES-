block_hex = input("Insert 16hex symbols")
block = bytes.fromhex(block_hex)

key = input("Insert hex key 16bytes")
secret = bytes.fromhex(block_hex)

state = bytes(p^k for p,k in zip(block,secret)) #Тут создаю массив стейт который хорит сразу инишл ки и наш блок




