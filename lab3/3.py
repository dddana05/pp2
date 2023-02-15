def solve(heads,legs):
    error="No solution"
    chicken_cnt=0
    rabbit_cnt=0
    
    if(heads>=legs):
        print(error)
    elif(legs%2!=0):
        print(error)
    else:
        rabbit_cnt=(legs-2*heads)/2
        chicken_cnt=heads-rabbit_cnt
        print(int(chicken_cnt),int(rabbit_cnt))