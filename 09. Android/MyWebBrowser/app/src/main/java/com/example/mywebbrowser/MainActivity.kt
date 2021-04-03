package com.example.mywebbrowser

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.view.ContextMenu
import com.google.android.material.floatingactionbutton.FloatingActionButton
import com.google.android.material.snackbar.Snackbar
import androidx.appcompat.app.AppCompatActivity
import android.view.Menu
import android.view.MenuItem
import android.view.View
import android.view.inputmethod.EditorInfo
import android.webkit.WebViewClient
import kotlinx.android.synthetic.main.content_main.*
import org.jetbrains.anko.browse
import org.jetbrains.anko.email
import org.jetbrains.anko.sendSMS
import org.jetbrains.anko.share

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        setSupportActionBar(findViewById(R.id.toolbar))

        registerForContextMenu(webView)

        webView.apply {
            settings.javaScriptEnabled = true
            webViewClient = WebViewClient()
        }

        webView.loadUrl("http://www.google.com")

        urlEditText.setOnEditorActionListener { _, actionId, _ ->
            if (actionId == EditorInfo.IME_ACTION_SEARCH) {
                var url = urlEditText.text.toString()
                if (!url.startsWith("http://") && ! url.startsWith("https://")) {
                    url = "http://$url"
                }
                webView.loadUrl(url)
                true
            } else {
                false
            }
        }
    }

    override fun onBackPressed() {
        if (webView.canGoBack()) {
            webView.goBack()
        } else {
            super.onBackPressed()
        }
    }

    // OptionsMenu, ContextMenu, PopupMenu
    // 메뉴 설정
    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_main, menu)
        return true
    }

    // 메뉴 아이템이 선택 됐을 때 호출
    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            R.id.action_google, R.id.action_home -> {
                webView.loadUrl("http://www.google.com")
                true
            }
            R.id.action_naver -> {
                webView.loadUrl("http://www.naver.com")
                true
            }
            R.id.action_daum -> {
                webView.loadUrl("http://www.daum.net")
                true
            }
            R.id.action_call -> {
                val intent = Intent(Intent.ACTION_DIAL)
                intent.data = Uri.parse("tel: 031-123-4567")
                if (intent.resolveActivity(packageManager) != null) {
                    startActivity(intent)
                }
                true
            }
            R.id.action_send_text -> {
                webView.url?.let { sendSMS("031-123-4567", it) }
                true
            }
            R.id.action_email -> {
                webView.url?.let { email("test@example", "좋은사이트", it) }
                true
            }

            else -> super.onOptionsItemSelected(item)
        }
    }

    // 컨텍스트 메뉴 작성
    override fun onCreateContextMenu(menu: ContextMenu?, v: View?,
                                     menuInfo: ContextMenu.ContextMenuInfo?) {
        // Inflate the menu; this adds items to the action bar if it is present.
        super.onCreateContextMenu(menu, v, menuInfo)
        menuInflater.inflate(R.menu.menu_main, menu)
    }

    override fun onContextItemSelected(item: MenuItem): Boolean {
        return when(item?.itemId) {
            R.id.action_share -> {
                webView.url?.let { share(it) }
                true
            }
            R.id.action_browser -> {
                webView.url?.let { browse(it) }
                true
            }
            else -> super.onContextItemSelected(item)
        }
    }
}