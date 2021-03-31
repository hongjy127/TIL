fun main() {
    val player = Player("Madrigal", 89, true, false)
    println(player)
    println(player.name)
    println(player.healthPoints)
    println(player.isBlessed)
//    println(player.isImmortal)

    val player2 = Player("Hong")
    println(player2)
    player2.apply { println("$name $healthPoints $isBlessed") }

    println(player2.hometown)
}