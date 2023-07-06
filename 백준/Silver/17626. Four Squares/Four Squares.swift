import Foundation

let idx = Int(readLine()!)!
var dp = Array.init(repeating: idx, count: idx+1)

for i in 1...idx {
    if i*i > idx{
        break
    }
    dp[i*i] = 1
}

for i in 1...idx {
    for j in 1..<i {
        if j*j > i {
            break
        }
        dp[i] = min(dp[i-j*j] + dp[j*j], dp[i])
//        print(i,j)
    }
}
print(dp[idx])