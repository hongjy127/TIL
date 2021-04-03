//class Player(_name: String,
//            _healthPoints: Int,
//            _isBlessed: Boolean,
//            _isImmortal: Boolean) {
//    var name = _name
//        get() = field.capitalize()
//        set(value) {
//            field = value.trim()
//        }
//    val healthPoints = _healthPoints
//    val isBlessed = _isBlessed
//    private val isImmoral = _isImmortal
//
//    fun castFireball(numFireballs: Int = 2) =
//        println("한 덩어리의 파이어볼이 나타난다. (X$numFireballs)")
//}

class Player(_name: String,
             var healthPoints: Int,
             var isBlessed: Boolean,
             private var isImmortal: Boolean) {
    var name = _name
        get() = field.capitalize()
        set(value) {
            field = value.trim()
        }

    val hometown by lazy {
        selectHometown()
    }

    fun selectHometown(): String  {
        return "Seoul"
    }

    init {
        println("initbolck")
        require(healthPoints > 0, {"healthPoints는 0보다 커야합니다"})
        require(name.isNotBlank(), {"플레이어는 이름이 있어야합니다."})
    }

    constructor(name: String): this(name,
                healthPoints = 100,
                isBlessed = true,
                isImmortal = false) {
        if(name.toLowerCase() == "kar") healthPoints = 45
        println("보조생성자")
    }

    fun castFireball(numFireballs: Int = 2) =
        println("한 덩어리의 파이어볼이 나타난다. (X$numFireballs)")
}