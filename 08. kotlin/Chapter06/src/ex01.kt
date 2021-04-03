public fun readLine(): String ? {
    return "hello world"
//    return ""
//    return null
}

//fun main(args: Array<String>) {
//    var beverage = readLine()
//    println(beverage)
//    beverage = null
//    println(beverage)
//}

//fun main(args: Array<String>) {
//    var beverage = readLine()?.capitalize()
//    println(beverage)
//}

fun main(args: Array<String>) {
//    var beverage = readLine()?.let {
//        if(it.isNotBlank()) {
//            it.capitalize()
//        } else {
//            "맥주"
//        }
//    }

    var beverage = readLine()!!.capitalize()
    println(beverage)
}