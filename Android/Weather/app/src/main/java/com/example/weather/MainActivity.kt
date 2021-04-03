package com.example.weather

import android.content.res.ColorStateList
import android.graphics.Color
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.SeekBar
import com.bumptech.glide.Glide
import com.example.mylib.openapi.openweather.OpenWeather
import com.example.mylib.openapi.piapi.PiApi
import kotlinx.android.synthetic.main.activity_main.*
import kotlin.math.roundToInt

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        OpenWeather.getWeatherCast("Seoul") {
//            Log.d("Weather", it.toString())
            txtDescription.text = it.weather[0].description
            val icon = it.weather[0].icon
            val iconPath = "https://openweathermap.org/img/w/${icon}.png"
            Glide.with(this).load(iconPath).into(imageWeather)
            // 온도(섭씨)를 포함해서 기타 정보 출력...
//            val temp = ((it.main.temp - 273.15)*10).roundToInt() / 10f
            val temp = it.main.temp - 273.15
            val humidity = it.main.humidity
            txtWeatherInfo.text = "온도: ${"%.1f".format(temp)} ℃, 습도: $humidity"
        }

        ledSwitch.setOnCheckedChangeListener { buttonView, isChecked ->
            if(isChecked) { // switch on
                PiApi.controlLed("1", "on") {
                    if(it.result == "OK") {
                        imageLight.imageTintList = ColorStateList.valueOf(Color.YELLOW)
                    }
                }
            } else {        // switch off
                PiApi.controlLed("1", "off") {
                    if(it.result == "OK") {
                        imageLight.imageTintList = ColorStateList.valueOf(Color.DKGRAY)
                    }
                }
            }
        }

        seekAngle.setOnSeekBarChangeListener(object: SeekBar.OnSeekBarChangeListener {
            override fun onProgressChanged(seekBar: SeekBar?, progress: Int, fromUser: Boolean) {
                val value = progress - 90
                PiApi.controlServo("1", value) {
                    if (it.result == "OK") {
                        txtServo.text = "서보 모터: $value"
                    }
                }
            }

            override fun onStartTrackingTouch(seekBar: SeekBar?) {

            }

            override fun onStopTrackingTouch(seekBar: SeekBar?) {

            }
        })

    }
}