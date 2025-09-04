#####solution.py
class RESULT:
    def __init__(self, cnt, IDs):
        self.cnt = cnt
        self.IDs = IDs  # [int] * 5

def init() -> None:
    pass

def sell(mID : int, mCategory : int, mCompany : int, mPrice : int) -> int:
    """
    ID가 mID이고 품목이 mCategory이고 제조사가 mCompany이고 가격이 mPrice인 상품을 판매 시작한다.
    판매 시작한 후 품목이 mCategory이고 제조사가 mCompany인 판매 중인 상품의 개수를 반환한다.
    함수가 호출 시 전달되는 mID 값은 이전 호출에서 이미 전달된 값이 아님을 보장한다.

    Parameters
        mID : 추가할 자료의 ID (1 ≤ mID ≤ 1,000,000,000)
        mCategory : 상품의 품목 (1 ≤ mCategory ≤ 5)
        mCompany : 상품의 제조사 (1 ≤ mCompany ≤ 5)
        mPrice : 상품의 가격 (1 ≤ mPrice ≤ 1,000,000)

    Return Value
        같은 품목과 제조사를 가진 판매 중인 상품의 개수 
    """
    # add / append
    return -1

def closeSale(mID : int) -> int:
    """
    ID가 mID인 상품을 판매 종료한다.
    판매를 종료할 때 상품의 가격을 반환한다. 만약, 판매하고 있지 않은 상품이거나 판매가 종료된 상품인 경우 -1을 반환한다.

    Parameters
        mID : 판매를 종료할 상품의 ID (1 ≤ mID ≤ 1,000,000,000)

    Return Value
        판매를 종료할 때 상품의 가격을 반환하고 상품을 판매하지 않는 경우 -1
    """
    # get(default=-1)
    # remove / pop
    return -1

def discount(mCategory : int, mCompany : int, mAmount : int) -> int:
    """
    품목이 mCategory이고 제조사 mCompany인 모든 상품의 가격을 mAmount 만큼 낮춘다.
    만약, 낮춘 가격이 0이거나 음수가 되면 해당 상품은 판매 종료한다.
    가격을 낮춘 후 품목이 mCategory이고 제조사가 mCompany인 판매되고 있는 상품의 개수를 반환한다.

    Parameters
        mCategory : 할인하고자 하는 상품의 품목 (1 ≤ mCategory ≤ 5)
        mCompany : 할인하고자 하는 상품의 제조사 (1 ≤ mCompany ≤ 5)
        mAmount : 할인되는 금액 (1 ≤ mAmount ≤ 1,000,000)

    Return Value
        품목과 제조사가 mCategory, mCompany인 판매 중인 상품 개수    
    """
    return -1

def show(mHow : int, mCode : int) -> RESULT:
    """
    mHow에 따라 조건을 만족하는 상품 중 가격이 낮은 순서로 최대 5개의 상품을 RESULT 구조체에 저장하고 반환한다. 
    만약 가격이 같은 경우 상품 ID가 더 적은 값을 가진 상품이 우선한다.
        ① mHow = 0인 경우 모든 상품에 대해서
            mHow = 0일 때 mCode는 0인 값이 들어오지만 의미가 없다.  
        ② mHow = 1인 경우 품목이 mCode인 모든 상품에 대해서
        ③ mHow = 2인 경우 제조사가 mCode인 모든 상품에 대해서
            mHow = 1 또는 2일 때 mCode는 1 이상 5 이하의 정수 값이다.
    판매 종료된 상품은 제외한다.

    반환할 때 저장된 상품의 개수를 RESULT.cnt에 저장하고 i번째 상품의 ID를 RESULT.IDs[i – 1]에 저장한다. 
    (1 ≤ i ≤ RESULT.cnt)
    조건에 만족하는 상품이 없는 경우 RESULT.cnt에 0을 저장한다.

    Parameters
        mHow : 검색 조건 (0 ≤ mHow ≤ 2)
        mCode : 검색 값 (0 ≤ mCode ≤ 5)

    Return Value
        검색 조건에 만족하는 상품 중 가격이 낮은 순서로 최대 5개의 상품    
    """
    return RESULT(-1, [0, 0, 0, 0, 0])
