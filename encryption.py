def encipher(p):
    a = ord(p)
    if a == 32: a = 96 #띄어쓰기 문자 32를 영어 문자 내에서 돌리기 위해 임의로 a 바로 앞의 문자로 변경해줌
    t = a + k
    if t > 122: t %= 122 # z보다 큰 아스키 값을 가지면 돌려줌
    if t < 27: t += 95 # a보다 작은 아스키 값이면 문자범위로 돌려줌
    if t == 96: t = 32 # 암호화 종료 후 96인 값이 있으면 이를 띄어쓰기 문자로 변경해줌
    return chr(t)


def decipher(c):
    a = ord(c)
    if a == 32: a = 96 #복호화할 문자가 띄어쓰기면 96으로 조정해줌
    t = a - k  # k 값 돌리기
    if t < 96: 
        '''
        여기 조건 뭐 써야 할지 모르겠다
        
        '''
    if t == 96: t = 32
    return chr(t)

p = input('평문입력 : ')
k = int(input('K값 입력(1~26) : '))
while k < 1 or k > 26:
    k = int(input('K값 입력(1~26) : '))
n = len(p)
c = ''
for i in range(n):
    ch = encipher(p[i])
    c += ch
print('암호문 출력 : [', end = '')
print(c, end='')
print(']')
q = ''
for i in range(n):
    ch = decipher(c[i])
    q += ch
print('복호화된 평문 : [', end='')
print(q, end='')
print(']')