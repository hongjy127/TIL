package com.example.basic_3_recyclerview

import java.io.Serializable

// Serializable: 인터페이스(생성자 호출 안함)
data class MainData(val title: String, val content: String) : Serializable