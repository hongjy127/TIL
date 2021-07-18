# Android



## 설치

https://developer.android.com/studio





## 환경설정



- 장치

  설정 > 시스템 > 테블릿 정보 7번 누르기 > 개발자 옵션 > USB 설정 선택: MTP
  
- 가상 디바이스

  



## 프로젝트 만들기

Package name: 전세계적으로 유일해야함



manifests > AndroidManifest.xml : 권한 등록

java > com.example.~ > kotlin 파일

res > layout > xml 파일

Gradle Scripts > build.gradle : 프로젝트 설정, 외부 라이브러리



### 프로젝트 생성 시 항상 해야할 것

build.gradle (Module:app) 파일

```android
plugins {
    id 'kotlin-android-extensions'
}
dependencies {
	// Anko library
	implementation "org.jetbrains.anko:anko-commons:0.10.5"
	
	// Glide library
	implementation 'com.github.bumptech.glide:glide:4.9.0'
	annotationProcessor 'com.github.bumptech.glide:compiler:4.9.0'	
	
	//retrofit
	implementation 'com.google.code.gson:gson:2.8.5'
 	implementation 'com.squareup.retrofit2:retrofit:2.6.0'
 	implementation 'com.squareup.retrofit2:converter-gson:2.6.0'
 	
 	//mqtt
 	implementation 'androidx.localbroadcastmanager:localbroadcastmanager:1.0.0'
	implementation 'org.eclipse.paho:org.eclipse.paho.client.mqttv3:1.2.0'
	implementation 'org.eclipse.paho:org.eclipse.paho.android.service:1.1.1'
}

```



- 내 라이브러리 추가

settings.gradle

```android
include ':app', ':MyLib'
project(':MyLib').projectDir = new File('C:\\Users\\hongj\\TIL\\09. Android\\MyLibBase\\MyLib')
```

build.gradle

```
implementation project(':MyLib')
```



- 권한

AndroidManifest.xml

```android
// 인터넷 사용 권한
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.WAKE_LOCK" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

```



- 위험권한

AndroidManifest.xml

```android
// Storage 권한 설정
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
```



- http 허용

AndroidManifest.xml

```
<application
	android:usesCleartextTraffic="true"
/application>
```



- mqtt 사용시

AndroidManifest.xml

```
<?xml version="1.0" encoding="utf-8"?>
<manifest ...> 
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WAKE_LOCK" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<application ...>
 :
<service android:name="org.eclipse.paho.android.service.MqttService" />
```





플러그인 설치

File > Settings > Plugins > JSON To Kotlin Class



## 안드로이드

Activity: 화면 처리

Service: 백그라운드 작업

BroadCastreceiver: 시스템이벤트 수신

Content provider: DB 연계

-> AndroidManifest에 등록하고 사용



- Activity Life Cycle
  - onCreate: 생성될 때 최초 1번 실행
  - onStart: Activity가 최초 실행될 때
  - onResume
  - onStop: 화면 일부가 보이지 않을 때 실행
  - onDestroy: 앱이 종료될 때 실행



### 화면 디자인

#### TextView

```kotlin
// View에 대한 참조
// findViewById<뷰클래스>(뷰 ID) 이거 안쓰고
// View id와 동일한 이름의 변수 사용

// View ID 지정방식
R.<리소스유형>.<뷰 ID>

// View 속성 변경
// View참조.속성 = 속성값
txtView.text
txtview.textSize
txtview.setOnClickListener {
    txtview.apply {
    	// 텍스트 클릭 시 실행할 코드 작성
    }
}
```



#### EditText

```kotlin
edtTxt.setOnFocusChangeListener() { v, hasFocus ->
	// v: 이벤트를 발생한 뷰
    // hasFocus: 포커스를 얻었는지 잃었는지              
}

edtTxt.addTextChangedListener(object: TextWatcher) { 
    // Ctrl + O로 필요한 함수 자동완성
}
```



#### Button

```kotlin
btn.setOnClickListener {
    btn.apply {
    	// 버튼 클릭 시 실행할 코드 작성
    }
}
```



- activity_main.xml

  imeOptions에 따라 키보드 모양이 달라짐

  `android:imeOptions='actionDone'`: 체크모양



### Error

#### LogCat

```kotlin
val TAG = javaClass.name
val TAG = javaClass.simpleName

Log.d(TAG, "출력할 내용")	// 변수 출력
Log.e(TAG, "출력할 내용")	// error 출력
```



### Intent

- 컴포넌트 간 정보 전달을 위해 사용

```kotlin
// SMS
var uri = Uri.parse("smsto:" + "번호010----")
var intent = Intent(Intent.ACTION_SENDTO, uri)
intent.putExtra("sms_body", "문자 내용")

// email
var uri = Uri.parse("mailto:email@email.com")
var intent = Intent(Intent.ACTION_SENDTO, uri)
intent.putExtra(Intent.EXTRA_EMAIL, "email@email.com")
intent.putExtra(Intent.EXTRA_SUBJECT, "test email")

val uri = Uri.parse("https://www.naver.com")
val intent = Intent(Intent.ACTION_VIEW, uri)
startActivity(intent)
```

- Activity 호출

```kotlin
// val intent = Intent(호출자, 피호출자)
val intent = Intent(this, Main2Activity::class.java)
intent.putExtra("key", value)
startActivity(intent)

// 받을 때
intent = getIntent()
var v = intent.getStringExtra("key")
```



### Toast

문자열 짧게 보여주기

```kotlin
Toast.makeText(Content, String, duration).show()
// duration
Toast.LENGTH_LONG
Toast.LENGTH_SHORT
```

```kotlin
// 사용자 정의 Toast
val layoutInflater = getSystemService(Context.LAYOUT_INFLATER_SERVICE) as LayoutInflater
// layout.xml을 코드로 객체화(inflate)
val layout = layoutInflater.inflate(R.layout.custom_toast, null)

layout.txtMessage.text = s

Toast(applicationContext).apply {
    setGravity(Gravity.CENTER, 0, 0)
    duration = Toast.LENGTH_LONG
    view = layout
    show()
}
```

#### Anko 라이브러리

```
toast(" ")
longToast(" ")
```







### Notification

- Android 0(API 26, Android 8)에서 Channel 추가

  - Channel Id: 앱마다 unique한 ID 생성 -> package full name 사용
  - Channel Name: 사용자에게 보여지는 채널의 이름(String)
  - Channel Importance: 채널의 중요도

  ```
  companion object {
      const val CHANNEL_ID = "com.example.basic_3_noti"
      const val CHANNEL_NAME = "My Channel"
      const val CHANNEL_DESCRIPTION = "Channel Test"
      const val NOTIFICATION_REQUEST = 0
      const val NOTIFICATION_ID = 100
  }
  ```



### RecyclerView

- 목록을 보여줄 때 사용

- data class

- Adapter

  RecyclerView.Adapter<T> 상속

  

### Retrofit

- REST API를 이용할 수 있도록 지원



- Weather 작동

  - 어플 실행

  - 라즈베리파이 기동

    ```
    $ sudo pigpiod	// 지터링 방지 기동
    $ cd mjpeg/iot/api
    $ python manage.py runserver 0.0.0.0:8000	// 웹서버 기동
    ```

    

### Mqtt

- mqtt_ex 작동

  - cmd에서 pub, sub

    - ```
      mosquitto_sub -v -h localhost -t iot/#
      mosquitto_pub -h localhost -t iot/monitor/led -m on
      ```

  - 안드로이드에서 스위치로 제어 가능 -> sub 구독






