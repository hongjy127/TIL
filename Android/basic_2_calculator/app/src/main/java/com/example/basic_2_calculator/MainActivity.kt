package com.example.basic_2_calculator

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    private fun subNumber(i: Int, i1: Int): Int {
        return i - i1
    }

    private fun addNumber(i: Int, i1: Int): Int {
        return i + i1
    }

    private fun calculate(pFunc: (Int, Int)->Int,
                  num1: Int, num2: Int): Int {
        return pFunc(num1, num2)
    }

    private fun calculate(pFunc: (Int, Int)->Int) {
        if(firstNumber.text == null || secondNumber.text == null) {
            return
        }

        if(firstNumber.text.length == 0 || secondNumber.text.length == 0) {
            return
        }

        var first = firstNumber.text.toString()
        var second = secondNumber.text.toString()

        var result = pFunc(first.toInt(), second.toInt())
        txtResult.text = "$result"
    }


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        btnPlus.setOnClickListener {
            calculate(::addNumber)
        }

        btnMinus.setOnClickListener {
            calculate(::subNumber)
        }

    }
}