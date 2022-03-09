import java.util.*
import java.io.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var n = readLine().toInt()
    for (i in 1..n){
        var tokenizer = StringTokenizer(readLine())
        var m = tokenizer.nextToken().toInt()
        var intarr = IntArray(m, {0})
        var sum = 0
        var cnt = 0

        for (j in 1..m){
            var a = tokenizer.nextToken().toInt()
            sum += a
            intarr[j-1] = a
        }
        var avg = sum / m.toDouble()
        intarr.forEach{
            if(it.toDouble() > avg) cnt += 1
        }
        println("${String.format("%.3f", (cnt/m.toDouble())*100)}%")
    }
}
