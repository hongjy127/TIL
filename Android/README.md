# Android



## 프로젝트 생성 시 항상 해야할 것

build.gradle (:app) 파일

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





플러그인 설치

File > Settings > Plugins > JSON To Kotlin Class