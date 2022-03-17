import java.io.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()

    for (i in 1..n) {
        for (j in 1..i)  print("*")
        println()
    }
}
