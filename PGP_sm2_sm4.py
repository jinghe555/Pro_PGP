#PGP使用对称加密算法和非对称加密算法混合加密；
#我采用sm4作为对称加密算法加密消息，sm2作为非对称加密算法加密会话密钥
import base64
import binascii
from gmssl import sm2,func
from gmssl.sm4 import CryptSM4,SM4_ENCRYPT,SM4_DECRYPT

'''加密部分'''
#初始化会话密钥k
k=b'315butlj26hvv313'
#M：消息
M=b'bbbu77b'
crypt_sm4=CryptSM4()
#ECB模式使用会话密钥加密消息M，加密的结果为encrypt_value
crypt_sm4.set_key(k,SM4_ENCRYPT)
encrypt_value=crypt_sm4.crypt_ecb(M)
print("加密消息结果:",encrypt_value)

#SM2加密会话密钥k
#设立公私钥对 pk:公钥  sk:私钥
sk='00B9AB0B828FF68872F21A837FC303668428DEA11DCD1B24429D0C99E24EED83D5'
pk='B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207'
#初始化
sm2_crypt=sm2.CryptSM2(public_key=pk,private_key=sk)
#加密会话密钥k
enc_k=sm2_crypt.encrypt(k)
print("加密的会话密钥结果:",enc_k)

'''解密部分'''
#SM2解密获得会话密钥k
dec_k=sm2_crypt.decrypt(enc_k)
print("解得的会话密钥k:",dec_k)

#ECB模式使用解得的会话密钥dec_k解密得到消息M
crypt_sm4.set_key(dec_k,SM4_DECRYPT)
decrypt_value=crypt_sm4.crypt_ecb(encrypt_value)
print("解得的消息M：",decrypt_value)

