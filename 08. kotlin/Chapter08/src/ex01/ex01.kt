const val TAVERN_NAME = "Taernyl's Folly"

var playerGold = 10
var playerSilver = 10
val patronList = listOf<String>("Eli", "Mordoc", "Sophie")

fun main(args: Array<String>) {
    println(patronList)
    println(patronList[0])
    println(patronList.first())
    println(patronList.last())
    println()
    patronList.apply {
        println(first())
        println(last())
    }

    println(patronList.getOrElse(4) {"unknown Patron"})
}