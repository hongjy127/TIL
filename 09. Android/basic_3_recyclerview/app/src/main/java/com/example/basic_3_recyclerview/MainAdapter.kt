package com.example.basic_3_recyclerview

import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.AdapterView
import androidx.recyclerview.widget.RecyclerView
import kotlinx.android.synthetic.main.item_main.view.*

class MainAdapter(val items: List<MainData>, val onItemClick: (Int)->Unit): RecyclerView.Adapter<MainAdapter.MainViewHolder>() {
    val TAG = javaClass.simpleName

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MainViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.item_main, parent, false)
        return MainViewHolder(view)
    }

    // 데이터의 개수 리턴
   override fun getItemCount() = items.size

    override fun onBindViewHolder(holder: MainViewHolder, position: Int) {
        items[position].let { it ->
            with(holder) {
                tvTitle.text = it.title
                tvContent.text = it.content
            }
        }
    }

    inner class MainViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val tvTitle = itemView.tv_main_title    // 타이틀 뷰 참조
        val tvContent = itemView.tv_main_content    // 컨텐츠 뷰 참조

        init {
            itemView.setOnClickListener {
                val pos = adapterPosition   // 현재 ViewHolder가 몇번째 index인지 알 수 있는 속성
                if (pos != RecyclerView.NO_POSITION) {
                    Log.d(TAG, "Item Clicked!! - $pos")
                    // Activity의 OnItemClick() 호출
                    onItemClick(pos)
                }
            }
        }
    }
}