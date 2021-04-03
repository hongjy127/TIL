package com.example.mylib.openapi.openweather

import android.util.Log
import com.example.mylib.openapi.OpenApi
import com.example.mylib.openapi.openweather.data.WeatherCast
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.GET
import retrofit2.http.Query

const val API_KEY = "d475fa2dadfba600248573dd893d7824"

interface OpenWeatherService {
    // http://api.openweathermap.org/data/2.5/weather?q=Seoul&APPID=d475fa2dadfba600248573dd893d7824&lang=kr
    @GET("/data/2.5/weather")
    fun getWeatherCast(
        @Query("q") city: String,
        @Query("APPID") apiKey: String = API_KEY,
        @Query("lang") lang: String = "kr"
    ): Call<WeatherCast>
}

object OpenWeather: OpenApi() {
    override val TAG = javaClass.simpleName
    override val BASE_URL = "http://api.openweathermap.org"

    private val service = retrofit.create(OpenWeatherService::class.java)

    fun getWeatherCast(city: String, callback: (WeatherCast)->Unit) {
        service.getWeatherCast(city)
                .enqueue(ApiCallback<WeatherCast>(callback))
    }
}


//object OpenWeather {
//    val TAG = javaClass.simpleName
//    private val retrofit = Retrofit.Builder()
//        .baseUrl("http://api.openweathermap.org")
//        .addConverterFactory(GsonConverterFactory.create())
//        .build()
//
//    fun getService(): OpenWeatherService = retrofit.create(
//        OpenWeatherService::class.java)
//
//    fun getWeatherCast(city: String, callback: (WeatherCast)->Unit) {
//        getService()
//            .getWeatherCast(city)
//            .enqueue(object: Callback<WeatherCast> {
//                override fun onFailure(call: Call<WeatherCast>, t: Throwable) {
//                    Log.e(TAG, t.toString())
//                }
//
//                override fun onResponse(
//                    call: Call<WeatherCast>,
//                    response: Response<WeatherCast>
//                ) {
//                    if (response.isSuccessful) {
//                        val result = response.body()
//                        callback(result!!)
//
//                    } else {
//                        Log.w(TAG, "${response.code()}, ${response.message()}")
//                        Log.w(TAG, "${response.toString()}")
//                    }
//                }
//            })
//    }
//}