def solution(arrows):
    op=[[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
    n=0 
    e=0
    x,y=0,0
    node=dict()
    node[(0,0)]=0
    edge=dict()
    for i in arrows:
        nx=x+op[i][0]
        ny=y+op[i][1] 
        ni=(i+4)%8
        if (nx,ny,ni) not in edge and (x,y,i) not in edge:
            
            if i%2==1:   
                i1=(i-1)
                i2=(i+1)%8
                i3=(i1+3)%8
                i4=(i2+5)%8
                if (x+op[i1][0],y+op[i1][1],i3) in edge or (x+op[i2][0],y+op[i2][1],i4) in edge:
                    e+=2
                    n+=1

            node[(nx,ny)]=0
            edge[(x,y,i)]=0

        x+=op[i][0]
        y+=op[i][1]

    e+=len(edge)
    n+=len(node)
    return 1-n+e