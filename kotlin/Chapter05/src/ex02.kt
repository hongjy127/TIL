fun main(args: Array<String>) {

//    val greetingFunction = {playName: String, numBuildings: Int ->
//        val currentYear = 2021
//        println("$numBuildings 채의 건물이 추가됨")
//        "SimVillage 방문을 환영합니다. $playName!(copyright $currentYear)"
//    }
//
//    runSimulation("홍이", greetingFunction)

    runSimulation("홍이") { playName: String, numBuildings: Int ->
        val currentYear = 2021
        println("$numBuildings 채의 건물이 추가됨")
        "SimVillage 방문을 환영합니다. $playName!(copyright $currentYear)"
    }
}

fun runSimulation(playerName: String,
                  greetingFunction: (String, Int) -> String) {
    val numBuildings = (1..3).shuffled().last()
    println(greetingFunction(playerName, numBuildings))
}