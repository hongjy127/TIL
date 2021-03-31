package com.example.basic_3_recyclerview

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.recyclerview.widget.GridLayoutManager
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import kotlinx.android.synthetic.main.activity_main.*
import org.jetbrains.anko.longToast
import org.jetbrains.anko.startActivity

class MainActivity : AppCompatActivity() {
    companion object {
        val KEY_DATA = "DATA"
    }
    var items = mutableListOf<MainData>()
    init {
        for(i in 1..70) {
            items.plusAssign(MainData("Title$i", "Content$i"))
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        rv_main_list.adapter = MainAdapter(items, ::onItemClick)
//        rv_main_list.layoutManager = LinearLayoutManager(this)
        rv_main_list.layoutManager = GridLayoutManager(this,2)

        btnAdd.setOnClickListener {
            val data = MainData(txtTitle.text.toString(), txtContent.text.toString())
            items.add(0, data)
            longToast(data.toString())
            // List가 수정된 사실을 adapter는 모름 --> 자동으로 갱신되지 않음
            // adapter에게 데이터가 수정된 사실을 통지하고, 화면 갱신을 유도해야함
            rv_main_list.adapter?.notifyDataSetChanged()
        }
    }

    fun onItemClick(pos: Int) {
        val data = items[pos]
//        longToast(data.toString())
        startActivity<DetailActivity>(
            "DATA" to data
        )
    }

}