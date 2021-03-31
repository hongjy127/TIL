package com.example.basic_2_activitylife

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log

class MainActivity : AppCompatActivity() {
    val TAG = javaClass.simpleName
    var nLineNumber = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        Log.d(TAG, String.format("\n%d: onCreate", nLineNumber++))
    }

    override fun onRestart() {
        super.onRestart()
        Log.d(TAG, String.format("\n%d: onRestart", nLineNumber++))
    }

    override fun onResume() {
        super.onResume()
        Log.d(TAG, String.format("\n%d: onResume", nLineNumber++))
    }

    override fun onPause() {
        super.onStop()
        Log.d(TAG, String.format("\n%d: onPause", nLineNumber++))
    }

    override fun onStop() {
        super.onStop()
        Log.d(TAG, String.format("\n%d: onStop", nLineNumber++))
    }

    override fun onDestroy() {
        super.onDestroy()
        Log.d(TAG, String.format("\n%d: onDestroy", nLineNumber++))
    }
}