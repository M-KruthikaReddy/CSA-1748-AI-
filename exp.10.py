from queue import PriorityQueue
goal_state=(1,2,3,4,5,6,7,8,0)
def heuristic(state):
    d=0
    for i in range(3):
        for j in range(3):
            t=state[i*3+j]
            if t!=0:
                x,y=(t-1)//3,(t-1)%3
                d+=abs(x-i)+abs(y-j)
    return d
def successors(state):
    s=[];i=state.index(0)
    if i%3!=0:
        n=list(state);n[i],n[i-1]=n[i-1],n[i];s.append(tuple(n))
    if i%3!=2:
        n=list(state);n[i],n[i+1]=n[i+1],n[i];s.append(tuple(n))
    if i//3!=0:
        n=list(state);n[i],n[i-3]=n[i-3],n[i];s.append(tuple(n))
    if i//3!=2:
        n=list(state);n[i],n[i+3]=n[i+3],n[i];s.append(tuple(n))
    return s
def solve(initial):
    f=PriorityQueue()
    f.put((heuristic(initial),initial))
    explored=set()
    g={initial:0}
    while not f.empty():
        _,state=f.get()
        if state==goal_state:return True
        explored.add(state)
        for nxt in successors(state):
            if nxt not in explored:
                g[nxt]=g[state]+1
                f.put((g[nxt]+heuristic(nxt),nxt))
    return False
initial_state=(2,8,3,1,6,4,7,0,5)
print("The puzzle is solvable!" if solve(initial_state) else "The puzzle is unsolvable.")
