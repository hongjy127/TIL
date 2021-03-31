data class Human(var name: String, var age: Int, var addr: String="서울"){
//    override fun equals(other: Any?): Boolean {
//        if(other is Human) {
//            val h = other as Human
//            return name == h.name && age == h.age && addr == h.addr
//        } else {
//            return false
//        }
//    }
//
//    override fun hashCode(): Int {
//        print("Hash Code called")
//        return super.hashCode()
//    }
//
//    override fun toString() = "$name $age $addr"
//    // python : __str__()
}


fun main() {
    var h1 = Human("홍길동", 20)
    var h2 = Human("고길동", 40, "수원")
    var h3 = Human("고길동", 40, "수원")

    println(h1)
    println(h2)
    println(h3)

    // 내용이 같냐?, 참조는 ===
    println(h1 == h2)
    println(h2 == h3)

    val h4 = h3 // 같은 참조를 가지는
    println(h3 === h4)
    val h5 = h3.copy(age=25)    // 복사본 생성
    println(h5)
    println(h3 === h5)
}