import java.util.*
import java.io.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var tokenizer = StringTokenizer(readLine())
    val n = tokenizer.nextToken().toInt()
    val x = tokenizer.nextToken().toInt()

    tokenizer = StringTokenizer(readLine())
    for(i in 1..n){
        var m = tokenizer.nextToken().toInt()
        if (m < x) print("$m ")
    }

}
