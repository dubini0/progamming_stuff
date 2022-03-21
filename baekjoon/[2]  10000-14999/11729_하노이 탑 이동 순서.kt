import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.StringBuilder
import java.util.*

val sb = StringBuilder()
var cnt = 0

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    var n = readLine().toInt()

    hanoi(n, 1, 2, 3)
    println(cnt)
    print(sb)
}

fun hanoi(num: Int, start: Int, sub: Int, to: Int){
    if (num == 0) return
    cnt += 1
    hanoi(num-1, start, to, sub)
    sb.append("$start $to\n")
    hanoi(num-1, sub, start, to)
}
