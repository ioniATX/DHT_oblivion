from secret_sharing_modif import secret_sharing
from secret_sharing_c_modif import secret_sharing_c

S = secret_sharing("The quick brown fox jumps over the lazy dog", 100, 15)

s = secret_sharing_c()
print S.share_random()
s.add_share(S.share_random())
s.add_share(S.share_random())
s.add_share(S.share_random())
s.add_share(S.share_random())
s.add_share(S.share_random())
s.add_share(S.share_random())
s.add_share(S.share_random())
s.add_share(S.share_random())
s.add_share(S.share_random())
s.add_share(S.share_random())
s.add_share(S.share_random())
s.add_share(S.share_random())
s.add_share(S.share_random())
s.add_share(S.share_random())
s.add_share(S.share_random())
print S


print s.reconstruct()
