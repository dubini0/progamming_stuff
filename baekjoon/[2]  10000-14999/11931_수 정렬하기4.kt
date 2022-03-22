import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    var sb = StringBuffer()
    val n = readLine().toInt()
    var arr = mutableListOf<Int>()

    for (i in 1..n){
        arr.add(readLine().toInt())
    }
    arr.sortDescending()

    arr.forEach{ sb.append("$it\n") }
    println(sb)
}
