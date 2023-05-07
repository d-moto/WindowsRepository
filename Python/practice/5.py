sentence = 'I love Python programming.'


print('sentence[0] : ', sentence[0])
print('sentence[-1] : ', sentence[-1])
print('sentence[2] : ', sentence[2])
print('sentence[6:13] : ', sentence[6:13])
print('sentence[::-1] : ', sentence[::-1])

print(
    """
     - スライスの使い方
     sequence[start:stop:step]

     startはスライスの開始位置を表し、省略すると先頭からスライスが開始されます。
     stopはスライスの終了位置を表し、省略すると末尾でスライスが終了されます。
     stepはスライスのステップ（増分）を表し、省略すると1となります。
     したがって、sentence[::-1]というスライスは次のような意味を持ちます：

     startは省略されているため、スライスは先頭から始まります。
     stopも省略されているため、スライスは末尾まで行われます。
     stepは-1と指定されており、逆順でスライスすることを意味します。
     したがって、sentence[::-1]は文字列 sentence を逆順にした結果を返します。
    """
)
