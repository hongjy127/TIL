fun main(args: Array<String>) {
    val numLetters = "Mississippi".count({letter->letter=='s'})
    println(numLetters)

//    val greetingFunction: () -> String = {
//        val currentYear = 2021
//        "SimVillage 방문을 환영합니다. 촌장님!(copyright $currentYear)"
//    }

//    val greetingFunction: (String) -> String = {playerName ->
//        val currentYear = 2021
//        "SimVillage 방문을 환영합니다. $playerName!(copyright $currentYear)"
//    }

//    val greetingFunction: (String) -> String = {
//        val currentYear = 2021
//        "SimVillage 방문을 환영합니다. $it!(copyright $currentYear)"
//    }

//    val greetingFunction: (String, Int) -> String = {playName, numBuildings ->
//        val currentYear = 2021
//        println("$numBuildings 채의 건물이 추가됨")
//        "SimVillage 방문을 환영합니다. $playName!(copyright $currentYear)"
//    }

    val greetingFunction = {playName: String, numBuildings: Int ->
        val currentYear = 2021
        println("$numBuildings 채의 건물이 추가됨")
        "SimVillage 방문을 환영합니다. $playName!(copyright $currentYear)"
    }

    println(greetingFunction("홍이", 2))
}

