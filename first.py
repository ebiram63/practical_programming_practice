"""It is a kind of test that is desinged by CTF """
"""توی این قسمت با یه پیام یه جورهایی رمز شده طرفیم. البته رمزی که هر کس با یه نگاه می‌تونه بگه چطوری باید رمزگشایی بشه ولی جالبیش اینه که هر کسی نمی‌تونه سریع رمزگشاییش کنه، چون باید رشته‌ها و کار با اونها رو در زبانتون بلد باشین که بتونین به خوبی حلش کنین. بیاین با هم پیام زیر رو رمزگشایی کنیم:"""
string = "T4 l16 _36 510 _27 s26 _11 320 414 {6 }39 C2 T0 m28 317 y35 d31 F1 m22 g19 d38 z34 423 l15 329 c12 ;37 19 h13 _30 F5 t7 C3 325 z33 _21 h8 n18 132 k24"


string_chunked = string.split(" ")
#print(c)


answer = []
for i in range(100):
    answer.append("*")
    #print(answer)
def print_answer_from_the_list(s):
    print (''.join(s))
for p in string_chunked:
    part1 =p[0]
    part2 = int(p[1:])
    #print(part1,part2)
    answer[part2] = part1 
    print_answer_from_the_list(answer)

print_answer_from_the_list(answer)