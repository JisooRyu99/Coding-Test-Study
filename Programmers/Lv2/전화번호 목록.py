def solution(phone_book):

    phone_book = (sorted(phone_book))
    print(phone_book[0])
    
    answer = [word for word in phone_book if word.startswith(phone_book[0])]
    
    if len(answer)>1:
        return False
    else:
        return True
      

 # 처음 시도한 코드였으나 sort한 후 제일 짧은 원소랑만 비교했기 때문에 총 20개의 테스트에서 3개가 오류나고, 효율성 테스트에서도 4개 중 1개가 오류남
------------------------------------------------------------------------------------------------------------------------------------------

# 수정 코드

def solution(phone_book):

    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True


--------------------------------------------------------------------------------------------------------------------------------------------
# 비슷한 정답

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):        # zip 을 통해서 [i],[i+1]의 표현을 없앰
        if p2.startswith(p1):
            return False
    return True
