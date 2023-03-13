let nk = readLine()!.split(separator: " ").map{Int($0)!}

var pn = Array.init(repeating: 1, count: nk[0]+1)
var cnt = 0
pn[1]=0
for num in 1...nk[0]{
    if pn[num] != 1{
        continue
    }
    for k in 1...nk[0]{
        if num*k>nk[0]{
            break
        }
        if pn[num*k] != 0{
            pn[num*k]=0
            cnt+=1
            
        }
        //print(num*k,cnt)
        if cnt == nk[1]{
            print(num*k)
            break
        }
    }
}
