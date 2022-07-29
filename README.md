# 项目名称
Implement a PGP scheme with SM2
# 项目简介
PGP-Pretty Good Privacy，是一个基于RSA公钥和对称加密相结合的邮件加密软件。该系统能为电子邮件和文件存储应用过程提供认证业务和保密业务。
PGP是一个混合加密算法。
# 完成人
何静
# 项目流程
## 加密
1、首先设定好会话密钥，使用会话密钥对消息进行加密；这里选取的对称加密算法为sm4（des已逐步淘汰，刚好gmssl库中可直接调用sm4）
2、使用规定的非对称加密算法sm2对会话密钥进行加密
![image](https://user-images.githubusercontent.com/104714591/181781283-ffb85c5c-9f7a-49a4-85c4-0c4c0962bf20.png)
## 解密
3、先解得会话密钥（sm2解密）
4、使用解得的会话密钥对加密的消息进行解密即可
![image](https://user-images.githubusercontent.com/104714591/181781364-ecc0db31-cd7d-47b8-8433-f3aca78a1549.png)

# 部分代码说明
代码注释十分详尽，详见代码注释
# 运行过程截图
![image](https://user-images.githubusercontent.com/104714591/181779427-ca83fb01-ad36-4310-bb40-82660aa9b1ca.png)
#引用参考
[1]https://blog.csdn.net/qq_42248536/article/details/105805078?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-2-105805078-blog-83047309.pc_relevant_vip_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-2-105805078-blog-83047309.pc_relevant_vip_default&utm_relevant_index=3
[2]https://www.cnblogs.com/rocedu/p/15518988.html

