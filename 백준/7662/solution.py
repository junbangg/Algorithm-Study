import sys, heapq, collections
input = sys.stdin.readline
tc = int(input())

for _ in range(tc):
    N = int(input())
    maxq, minq, dic = [], [], collections.defaultdict(int)
    for _ in range(N):
        cmd, num = input().split()
        # push 작업
        if cmd == 'I':  
            heapq.heappush(minq, int(num))
            heapq.heappush(maxq, -int(num))
            dic[int(num)] += 1
        # pop 작업
        else:
            # 최소값
            if num == '-1':
                # 해시값이 0인 최소값 건너뛰기
                while minq and dic[minq[0]] == 0:
                    heapq.heappop(minq)
                # 최소값 뽑기
                if minq:
                    minVal = heapq.heappop(minq)
                    dic[minVal] -= 1
            # 최대값
            elif num == '1':
                # 해시값이 0인 최대값 건너뛰기
                while maxq and dic[-maxq[0]] == 0:
                    heapq.heappop(maxq)
                # 최대값 뽑기
                if maxq:
                    maxVal = -heapq.heappop(maxq)
                    dic[maxVal] -= 1
    # 해시값이 0 인 최대값 건너뛰기
    while maxq and dic[-maxq[0]] == 0:
        heapq.heappop(maxq)
    # 해시값이 0인 최소값 건너뛰기
    while minq and dic[minq[0]] == 0:
        heapq.heappop(minq)
    #출력
    if not minq or not maxq:
        print('EMPTY')
    else:
        print(-heapq.heappop(maxq), heapq.heappop(minq))
