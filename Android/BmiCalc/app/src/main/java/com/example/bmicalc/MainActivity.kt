package com.example.bmicalc

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.preference.PreferenceManager
import kotlinx.android.synthetic.main.activity_main.*
import org.jetbrains.anko.startActivity
import org.jetbrains.anko.toast

class MainActivity : AppCompatActivity() {
    companion object {
        val KEY_WEIGHT = "KEY_WEIGHT"
        val KEY_HEIGHT = "KEY_HEIGHT"
    }
    private fun saveData(height: Int, weight: Int) {
        val pref = PreferenceManager.getDefaultSharedPreferences(this)
        val editor = pref.edit()
        editor.putInt(KEY_HEIGHT, height).putInt(KEY_WEIGHT, weight).apply()
    }

    private fun loadData() {
        val pref = PreferenceManager.getDefaultSharedPreferences(this)
        val height = pref.getInt(MainActivity.KEY_HEIGHT, 0)
        val weight = pref.getInt(MainActivity.KEY_WEIGHT, 0)

        if (height != 0 && weight != 0) {
            heightEditText.setText(height.toString())
            weightEditText.setText(weight.toString())
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        loadData()
        resultButton.setOnClickListener {
            val height = heightEditText.text.toString().toInt()
            val weight = weightEditText.text.toString().toInt()

//            toast("키: $height, 체중: $weight")
            saveData(height, weight)
            startActivity<ResultActivity>(
                KEY_HEIGHT to height,
                KEY_WEIGHT to weight
            )
        }
    }
}