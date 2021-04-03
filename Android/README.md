# Android



## 프로젝트 생성 시 항상 해야할 것

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



- 라이브러리 추가

settings.gradle

```android
include ':app', ':MyLib'
project(':MyLib').projectDir = new File('C:\\Users\\hongj\\TIL\\Android\\MyLibBase\\MyLib')
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