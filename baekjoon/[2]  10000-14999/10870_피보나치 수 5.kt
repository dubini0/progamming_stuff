import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    var n = readLine().toInt()

    val res = fibo(n)
    print(res)
}

fun fibo(num: Int): Int {
    return if (num == 0)
        0
    else if (num == 1 || num == 2)
        1
    else
        fibo(num-1)+fibo(num-2)
}
