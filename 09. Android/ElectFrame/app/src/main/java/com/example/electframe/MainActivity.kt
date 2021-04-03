package com.example.electframe

import android.Manifest
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.mylib.MediaImage
import com.example.mylib.PermissionChecker
import kotlinx.android.synthetic.main.activity_main.*
import org.jetbrains.anko.longToast
import kotlin.concurrent.timer


class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val pos = intent.getIntExtra(PhotoGridActivity.KEY_PHOTO_INDEX, 0)
        val mediaImage = MediaImage(this)
        val adapter = PhotoPagerAdapter(
            this,
            mediaImage.getAllPhotos()
        )
        viewPager.adapter = adapter
        viewPager.currentItem = pos

        timer(period = 3000) {
            runOnUiThread {
                if (viewPager.currentItem < adapter.itemCount - 1) {
                    viewPager.currentItem++
                } else {
                    viewPager.currentItem = 0
                }
            }
        }
    }
}

//        val permissionChecker by lazy {
//            val permissions = arrayOf(Manifest.permission.READ_EXTERNAL_STORAGE)
//            PermissionChecker(this, permissions)
//        }

//        if (permissionChecker.check()) {
//            // 이전에 승인 받음
////            longToast("권한 획득 했었음")
//            init()
//        }
//    }

//    override fun onRequestPermissionsResult(
//        requestCode: Int,
//        permissions: Array<out String>,
//        grantResults: IntArray) {
//        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
//        if(permissionChecker.checkGranted(requestCode, permissions, grantResults)) {
//            // 최초 승인 성공
////            longToast("권한 획득 성공")
//            init()
//        } else {
//            longToast("앱을 실행하려면 권한 승인이 필요합니다.")
//            // 종료
//            finish()
//        }
//    }

//    private fun init() {
////        longToast("액티비티 초기화")
//        // 갤러리로부터 이미지 목록을 얻는 것
//        // PhotoPagerAdapter 생성
//        // Pager에 등록
//
//        val mediaImage = MediaImage(this)
//        val adapter = PhotoPagerAdapter(this, mediaImage.getAllPhotos())
//        viewPager.adapter = adapter
//        viewPager.currentItem = pos
//
//        timer(period = 3000) {
//            runOnUiThread {
//                if (viewPager.currentItem < adapter.itemCount -1) {
//                    viewPager.currentItem++
//                } else {
//                    viewPager.currentItem = 0
//                }
//            }
//        }
//    }
