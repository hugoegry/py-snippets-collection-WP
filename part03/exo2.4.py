p = "abcdefghij"
print(p[::-2][:5][::-1][3:]) 
#[::-2] on parcour a lenver en prenent un char sur 2
# = jhfdb
# [ :5] on garde que les 5 premier
# = jhfdb
# [::-1] on remet a l endroit
# = bdfhj
# [3 : ] on prend les caracter apres le 3eme 
# = hj