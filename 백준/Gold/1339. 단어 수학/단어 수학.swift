import Foundation
var n : Int!

n = Int(readLine()!)
let startingValue = Int(("A" as UnicodeScalar).value) // 65

var dict: [Character:Int] = [:]
for i in (65...90) {
    let tmp = Character(UnicodeScalar(i)!)
    dict[tmp] = 0
}

func myPow (_ radix: Int, _ power: Int) -> Int {
    return Int(pow(Double(radix), Double(power)))
}


for _ in (0..<n){
    let word = readLine()!
    let w = Array(word)
    for i in 0..<w.count {
        dict[w[i]] = dict[w[i]]! + myPow(10,(w.count - i - 1))
    }
}


let sorted = dict.sorted { $0.value > $1.value}
var ans = 0
var value = 9
for item in sorted {
    if item.value == 0 {
        break
    }
    
    ans += item.value * value
    value -= 1
}

print(ans)