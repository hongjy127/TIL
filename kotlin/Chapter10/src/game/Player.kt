class Player {
    var name = "nadrigal"   // 멤버변수는 반드시 초기화
        get() = field.capitalize()
        set(value) {
            field = value.trim()
        }
    fun castFireball(numFireballs: Int = 2) =
        println("한 덩어리의 파이어볼이 나타난다. (X$numFireballs)")
}