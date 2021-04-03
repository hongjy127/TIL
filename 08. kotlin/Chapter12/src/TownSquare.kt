class TownSquare: Room("Town Square") {
    override val dangerLevel = super.dangerLevel-3
    private val bellsound = "댕댕"

    final override fun load() = "당신의 참여를 주민들이 다 함께 환영합니다.\r\n" +
                            ringBell()
    private fun ringBell() = "당신의 도착을 종탑에서 알립니다. $bellsound"
}

fun printRoomInfo(room: Room) {
    println(room.description())
    println(room.load())
}

fun main() {
    val ts = TownSquare()
//    val ts: TownSquare = Room("Foyer") // 자식 타입 변수 참조 불가
    println(ts.description())
    println(ts.load())
    printRoomInfo(ts)
//    print(ts.dangerLevel)

    var room: Room
    room = ts
    println(room.description())
    println(room.load())
    printRoomInfo(room)
}