import Foundation

struct Truck{
    var cap : Int
    var dcnt : Int = 0
    var pcnt : Int = 0
}
func solution(_ cap:Int, _ n:Int, _ deliveries:[Int], _ pickups:[Int]) -> Int64 {
    var answer = 0
    var nextD = [Int]()
    var nextP = [Int]()
    var darr = deliveries
    var parr = pickups

    for i in 0..<deliveries.count{
        if deliveries[i] != 0 {
            nextD.append(i)
        }
        if pickups[i] != 0{
            nextP.append(i)
        }
    }
    
    var truck = Truck(cap: cap)
    while true{
        //print(nextD, nextP)
        truck.cap = cap
        if nextP.isEmpty && nextD.isEmpty {
            break
        }
        answer += max(nextD.last ?? 0, nextP.last ?? 0)*2+2
        
        while !nextD.isEmpty{
            //print(nextD)
            let i = nextD.popLast()!
            if truck.cap >= darr[i]{
                truck.cap -= darr[i]
            }else{
                darr[i] -= truck.cap
                nextD.append(i)
                break
            }
        }
        truck.cap = cap
        while !nextP.isEmpty{
            //print(nextP)
            let i = nextP.popLast()!
            if truck.cap >= parr[i]{
                truck.cap -= parr[i]
            }else{
                parr[i] -= truck.cap
                nextP.append(i)
                break
            }
        }
        
    }
    return Int64(answer)
}