import java.io.*

fun main() {
    val br :BufferedReader = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()

    for (i in 1..9){
        println("$n * $i = ${n*i}")
    }
}
