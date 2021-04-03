package com.example.basic_1_edittext

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_result.*


class ResultActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_result)

        btnClose.setOnClickListener {
            val i = Intent()
            i.putExtra(MainActivity.RESULT, txtMessage.text.toString())
            setResult(RESULT_OK, i)
            finish()
        }
    }

    override fun onStart() {
        super.onStart()

        val i = intent ?: return

        val sID = i.getStringExtra(MainActivity.ID)
        val sPasswd = i.getStringExtra(MainActivity.PASSWD)

        txtMessage.text = "ID: ${sID}\nPassword: ${sPasswd}"
        i.putExtra(MainActivity.RESULT, txtMessage.text.toString())
    }
}