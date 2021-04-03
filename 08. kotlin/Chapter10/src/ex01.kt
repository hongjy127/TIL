import game.Dice
import game.Player

fun main() {
    val player = Player()
    player.castFireball()
    player.name = "estragon"
    print(player.name + "TheBrave")

    val my06 = Dice()
    println(my06.rolledValue)
    println(my06.rolledValue)
    println(my06.rolledValue)

    my06.apply {
        println(rolledValue)
        println(rolledValue)
        println(rolledValue)
    }
}