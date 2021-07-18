package com.example.mqtt_ex

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.SeekBar
import com.example.mylib.net.Mqtt
import kotlinx.android.synthetic.main.activity_main.*
import org.eclipse.paho.client.mqttv3.MqttMessage

const val SUB_TOPIC = "iot/monitor/#"
const val PUB_TOPIC = "iot/led"
const val SERVER_URI = "tcp://172.30.1.39:1883" // broker: pc

class MainActivity : AppCompatActivity() {
    val TAG = "MqttActivity"
    lateinit var mqttClient: Mqtt

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        mqttClient = Mqtt(this, SERVER_URI)
        try {
            mqttClient.setCallback(::onReceived)
            Log.d("Mqtt", "connect")
            mqttClient.connect(arrayOf<String>(SUB_TOPIC))
        } catch (e: Exception) {
            e.printStackTrace()
        }

        ledSwitch.setOnCheckedChangeListener { buttonView, isChecked ->
            val value = if(isChecked) "on" else "off"
            mqttClient.publish("iot/control/led", value)
        }

        seekAngle.setOnSeekBarChangeListener(object: SeekBar.OnSeekBarChangeListener {
            override fun onProgressChanged(seekBar: SeekBar?, progress: Int, fromUser: Boolean) {
                mqttClient.publish("iot/control/servo", progress.toString())
            }

            override fun onStartTrackingTouch(seekBar: SeekBar?) {
            }

            override fun onStopTrackingTouch(seekBar: SeekBar?) {
            }

        })
    }

    fun onReceived(topic: String, message: MqttMessage) {
        val msg = String(message.payload)
        Log.i(TAG, "$topic: $msg")
        // MqttService에서 runOnUIIThread()로 호출
        // 안전하게 UI작업을 해도 됨.
        txtWeatherInfo.text = "$topic: $msg"
    }

    fun publish() {
        mqttClient.publish(PUB_TOPIC, "1")
    }
}