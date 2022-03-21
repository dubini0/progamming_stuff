import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    var a = readLine().toInt()
    var b = readLine().toInt()
    var c = readLine().toInt()
    var resArr = IntArray(10, {0})

    var res = a*b*c
    for (i in res.toString()){
        val idx = i.code - 48
        resArr[idx]++
    }

    resArr.forEach { println(it) }
}
