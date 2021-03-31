fun printConstructionCost(numBuildings: Int) {
    val cost = 500
    println("건축비용: ${cost * numBuildings}")
}

inline fun runSimulation(playerName: String,
                         costPrinter: (Int) -> Unit,
                         greetingFunction: (String, Int) -> String) {
        val numBuildings = (1..3).shuffled().last()
        costPrinter(numBuildings)
        println(greetingFunction(playerName, numBuildings))
    }


fun main(args: Array<String>) {
    runSimulation("홍이", ::printConstructionCost) {
            playerName, numBuildings ->
        val currentYear = 2021
        println("$numBuildings 채의 건물이 추가됨")
        "SimVillage 방문을 환영합니다. $playerName!(copyright $currentYear)"
    }
}