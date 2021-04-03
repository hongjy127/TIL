import jdk.incubator.vector.DoubleVector

fun main() {
//    val map = mapOf<String, Double>(
//        "Eli" to 10.5,
//        "Sophie" to 5.5
//    )

    val map = mutableMapOf<String, Double>(
        Pair("Eli", 10.5),
        Pair("Sophie", 5.5)
    )
    println(map)

    map += "Sophie" to 6.0
    println(map)

    map["Sophie2"] = 8.0
    println(map)
    println(map["Sophie2"])
    println(map["test"])    // null

    //    value = map["Sophie2"]  // map[]의 리턴타입은 Double?
    var value : Double = map.getOrElse("Sophie2") { 0.0 }
    println(value)
    var value2 : Double = map.getOrDefault("test", 0.0)
    println(value2)

    // forEach로 map 순회하면서 출력
    map.forEach { key, value ->
        println("$key : $value")
    }
}