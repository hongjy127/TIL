package com.example.mylib

import android.provider.MediaStore
import android.util.Log
import androidx.appcompat.app.AppCompatActivity

class MediaImage(val ctx: AppCompatActivity) {
    fun getAllPhotos(): ArrayList<String> {
        val cursor = ctx.contentResolver.query(
            MediaStore.Images.Media.EXTERNAL_CONTENT_URI,
            null,
            null,
            null,
            MediaStore.Images.ImageColumns.DATE_TAKEN + " DESC"
        )
        val imageUris = ArrayList<String>()

        cursor?.use {
            while (it.moveToNext()) {
                val uri = it.getString(it.getColumnIndexOrThrow(
                    MediaStore.Images.Media.DATA))
                Log.d("MainActivity", uri)
                imageUris.add(uri)
            }
        }
        return imageUris
    }
}