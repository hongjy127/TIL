package com.example.basic_3_usingintent

import android.content.Intent
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        setUpUI()
    }

    private fun setUpUI() {
        // 암묵적 인텐트 호출 <--> 명시적 인텐트 호출
        btnSMS.setOnClickListener {
//        var uri = Uri.parse("smsto:" + "01000000000")
//        var intent = Intent(Intent.ACTION_SENDTO, uri)
//        intent.putExtra("sms_body", "여기가 문자!!")

            // email
            var uri = Uri.parse("mailto:hongjy127@naver.com")
            var intent = Intent(Intent.ACTION_SENDTO, uri)
            intent.putExtra(Intent.EXTRA_EMAIL, "hongjy127@naver.com")
            intent.putExtra(Intent.EXTRA_SUBJECT, "test email")

            startActivity(intent)
        }

        btnInternet.setOnClickListener {
            val uri = Uri.parse("https://blog.naver.com/hongjy127/")
            val intent = Intent(Intent.ACTION_VIEW, uri)
            startActivity(intent)
        }

        btnMap.setOnClickListener {
            val uri = Uri.parse("geo: 37.5310091, 127.0261659")
            val intent = Intent(Intent.ACTION_VIEW, uri)
            startActivity(intent)
        }

        btnMarket.setOnClickListener {
            val uri = Uri.parse("market://detail?id=com.psw.moringcall")
            val intent = Intent(Intent.ACTION_VIEW, uri)
            startActivity(intent)
        }

    }
}