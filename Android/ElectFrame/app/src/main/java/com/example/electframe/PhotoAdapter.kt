package com.example.basic_3_recyclerview

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.AdapterView
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.example.electframe.R
import kotlinx.android.synthetic.main.item_photo.view.*

class PhotoAdapter(val items: List<String>, val onItemClick: (Int)->Unit):
    RecyclerView.Adapter<PhotoAdapter.MainViewHolder>() {
    val TAG = javaClass.simpleName

    inner class MainViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val imgThumb = itemView.imgThumb

        init {
            itemView.setOnClickListener {
                val pos = adapterPosition   // 현재 ViewHolder가 몇번째 index인지 알 수 있는 속성
                if (pos != RecyclerView.NO_POSITION) {
                    onItemClick(pos)
                }
            }
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MainViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_photo, parent, false)
        return MainViewHolder(view)
    }

    // 데이터의 개수 리턴턴
    override fun getItemCount() = items.size

    override fun onBindViewHolder(holder: MainViewHolder, position: Int) {
        items[position].let {
            with(holder) {
                Glide.with(imgThumb)
                    .load(it)
                    .override(300, 300)
                    .into(imgThumb)
            }
        }
    }

}