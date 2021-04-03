package com.example.bmicalc

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_result.*
import org.jetbrains.anko.longToast

class ResultActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_result)

        val height = intent.getIntExtra("height", 0)
        val weight = intent.getIntExtra("weight", 0)

        val bmi = weight / Math.pow(height / 100.0, 2.0)

        resultTextView.apply {
            text = when {
                bmi >= 35 -> "고도 비만"
                bmi >= 30 -> "2단계 비만"
                bmi >= 25 -> "1단계 비만"
                bmi >= 23 -> "과체중"
                bmi >= 18.5 -> "정상"
                else -> "저체중"
            }
        }

        imageView.apply {
            when {
                bmi >= 23 -> setImageResource(
                    R.drawable.ic_baseline_sentiment_very_dissatisfied_24
                )
                bmi >= 18.5 -> setImageResource(
                    R.drawable.ic_baseline_sentiment_satisfied_alt_24
                )
                else -> setImageResource(
                    R.drawable.ic_baseline_sentiment_dissatisfied_24
                )

            }
        }

        longToast("키: $height, 체중: $weight, bmi: $bmi")
    }
}