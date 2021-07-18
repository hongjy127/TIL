package com.example.android_ex

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.SeekBar
import com.example.mylib.Notification
import com.example.mylib.net.Mqtt
import com.example.mylib.openapi.piapi.PiApi
import kotlinx.android.synthetic.main.activity_main.*
import org.eclipse.paho.client.mqttv3.MqttMessage

const val SUB_TOPIC = "iot/pir"
const val SERVER_URI = "tcp://172.30.1.39:1883"

class MainActivity : AppCompatActivity() {
    companion object {
        const val CHANNEL_ID = "com.example.Android_ex"
        const val CHANNEL_NAME = "My Channel"
        const val CHANNEL_DESCRIPTION = "Channel Test"
        const val NOTIFICATION_REQUEST = 0
        const val NOTIFICATION_ID = 100
    }

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



    }

    fun onReceived(topic: String, message: MqttMessage) {
        val msg = String(message.payload)
        Log.i(TAG, "$topic: $msg")

        if (msg == "on") {
            txtMqtt.text = "$topic: $msg"
            val noti = Notification(this)
            noti.createNotificationChannel(CHANNEL_ID, CHANNEL_NAME, CHANNEL_DESCRIPTION)
            val pendingIntent = noti.getPendingIntent(
                    DetectionActivity::class.java,
                    NOTIFICATION_REQUEST)
            noti.notifyBasic(CHANNEL_ID, NOTIFICATION_ID,
                    "Alarm", "동작 감지",
                    R.drawable.ic_launcher_foreground, pendingIntent)
        }
    }

}