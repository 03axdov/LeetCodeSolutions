import scala.collection.mutable.Map
import scala.collection.mutable.ListBuffer

def twoSum(li: List[Int], target: Int): ListBuffer[Int] =
    var map = Map[Int, Int]()
    val output = new ListBuffer[Int]()
    for (i <- 0 to li.length - 1) {
        println(s"map: $map")
        if ( map.get(target - li(i)) != None ) {
            output.append(map.get(target-li(i)).get)
            output.append(i)
        } else {
            map += (li(i) -> i)
        }
    }
    output

@main def main(): Unit =
    val res = twoSum(List(1,2,3,2,4,7), 10)
    println(res)