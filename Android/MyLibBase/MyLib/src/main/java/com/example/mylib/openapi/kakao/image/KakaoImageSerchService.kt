package com.example.imagesearch

import com.example.imagesearch.data.kakaoimage.ImageSearchResult
import retrofit2.Call
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.GET
import retrofit2.http.Headers
import retrofit2.http.Query

interface KakaoImageSerchService {
    @Headers("Authorization: KakaoAK 4cf5f301c1c62029f447bb1326dea702")
    @GET("/v2/search/image")
    fun requestSearchImage(
        @Query("query") keyword: String,
        @Query("sort") sort: String = "recency",
        @Query("page") page: Int,
        @Query("size") size: Int = 10
    ): Call<ImageSearchResult>
}

// 싱글톤: 오직 한개의 인스턴스만 존재
// 인스턴스가 알아서 만들어짐
object KakaoImageSearch {
    private val retrofit = Retrofit.Builder()
        .baseUrl("https://dapi.kakao.com")
        .addConverterFactory(GsonConverterFactory.create())
        .build()

    fun getService(): KakaoImageSerchService = retrofit.create(KakaoImageSerchService::class.java)
}