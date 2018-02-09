# -*- coding:utf-8 -*-
import md5
text='需要加密的文字'
md5_obje=md5.new()
md5_obje.update(text)
print md5_obje.hexdigest() # 生成十六进制
print md5_obje.digest() # 生成二进制
56563edf23b9d717dc63981b8836fc60  1
6e564b206a0fd5ebdd045261694d6c71  2  a92bbcbefad8259055217dc15d9bd73b
848ce59e93a757af6c238eec6d7996dc  3