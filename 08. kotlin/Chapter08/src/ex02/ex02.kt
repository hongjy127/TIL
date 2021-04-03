val patronList2 = mutableListOf<String>("Eli", "Mordoc", "Sophie")

fun main(args: Array<String>) {
//    println(patronList2)
//    patronList2.remove("Eli")
//    patronList2.add("Alex")
//    patronList2.add(0,"Alex")
//    patronList2[0] = "Alexis"
//    println(patronList2)

//    for(patron in patronList2) {
//        println("좋은 밤입니다. $patron 님")
//    }
//    patronList2.forEach { patron ->
//        println("좋은 밤입니다. $patron 님")
//    }
//
//    patronList2.forEach { println("좋은 밤입니다. $it 님") }

    patronList2.forEachIndexed { index, patron ->
        println("좋은 밤입니다. $patron 님 - 당신은 ${index+1} 번째 입니다.")
    }
}