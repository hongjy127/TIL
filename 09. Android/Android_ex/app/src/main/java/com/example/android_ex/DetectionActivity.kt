package com.example.android_ex

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.webkit.WebViewClient
import android.widget.SeekBar
import com.example.mylib.openapi.piapi.PiApi
import kotlinx.android.synthetic.main.activity_detection.*
import org.jetbrains.anko.startActivity

class DetectionActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_detection)

        seekAngle.setOnSeekBarChangeListener(object: SeekBar.OnSeekBarChangeListener {
            override fun onProgressChanged(seekBar: SeekBar?, progress: Int, fromUser: Boolean) {
                val value = progress - 90
                PiApi.controlServo("1", value) {
                    if (it.result == "OK") {
                        txtServo.text = "ServoMotor: $value"
                    }
                }
            }

            override fun onStartTrackingTouch(seekBar: SeekBar?) {
            }

            override fun onStopTrackingTouch(seekBar: SeekBar?) {
            }

        })

        webView.apply {
            settings.javaScriptEnabled = true
            webViewClient = WebViewClient()
        }

        // mjpeg-streamer 실행
        webView.loadUrl("http://172.30.1.57:8000/mjpeg/?mode=stream")

        btnBack.setOnClickListener {
            startActivity<MainActivity>(
            )
        }
    }
}