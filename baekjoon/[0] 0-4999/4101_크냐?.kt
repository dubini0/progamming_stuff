import java.io.*
import java.util.*

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    var arr = readLine().split(" ").map{it.toInt()}
    do{
        if(arr[0]==0 && arr[1]==0) break

        if(arr[0] > arr[1]){
            println("Yes")
        }
        else{
            println("No")
        }
        arr = readLine().split(" ").map{it.toInt()}
    }while(arr[0] != 0 && arr[1] != 0)
}
