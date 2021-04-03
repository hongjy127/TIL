open class TownSquare: Room("Town Square") {
    override val dangerLevel = super.dangerLevel-3
    private val bellsound = "댕댕"

    override fun load() = "당신의 참여를 주민들이 다 함께 환영합니다.\r\n" +
                            ringBell()
    private fun ringBell() = "당신의 도착을 종탑에서 알립니다. $bellsound"
}

fun printRoomInfo(room: Room) {
    println(room.description())
    println(room.load())
}

fun main() {
    val test = object: TownSquare() {
        override fun load() = "새로운 로드입니다"
    }
    println(test.load())
    println(test.description())
}