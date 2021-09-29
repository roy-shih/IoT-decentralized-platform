# IOT Kit

## 架構

1. 伺服器系統
    1. 跨平台LAN伺服器，能運行在Windows、MacOS電腦與Raspberry PI
2. 網頁應用程式系統
    1. 跨平台控制介面，能適應各種大小的Windows、MacOS、Android、iOS等
3. 物聯網終端系統
    1. 電器：以ESP32+繼電器為核心作為終端，每秒GET一次設備狀態進行IO設置
    2. 感測器：以ESP32+各類感測器為核心作為終端，每秒POST一次感測器數值進行更新，或與電器連動（詳見自動化）

## 安裝並運行伺服器

1. 環境
    1. Python 3.7 以上 
    2. 需要安裝 "virtualenv" Python套件
        
        ```bash
        pip install virtualenv
        ```
        
2. 進入 IOT 資料夾，開啟虛擬環境
    
    ```bash
    #Terminal
    source bin/activate
    ```
    
    ```bash
    #Powershell
    bin\activate.ps1
    ```
    
3. 進入 IOT/src 資料夾，運行伺服器
    
    ```bash
    python manage.py runserver 127.0.0.1:8000
    ```
    
    - 查看伺服器的IP位置
        
        ```bash
        #Terminal
        ifconfig
        ```
        
        ```bash
        #CMD
        ipconfig
        ```
        

## 設備韌體

### POST 方法

```arduino
#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "SSID";     // Same AP as the server
const char* pwd = "password";
const String server_ip = xxx.xxx.xx.x:xxxx

const String Device_ID="temp"; //Custom sensor ID
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  WiFi.begin(ssid,pwd);
  while(WiFi.status() != WL_CONNECTED){
    delay(100);
    Serial.println("Connecting to wifi...");
  }
  Serial.println("Done");
 }

void loop() {

	String T=String(random(10)+20);  //sensor value

  if((WiFi.status() == WL_CONNECTED)){
    HTTPClient http;
    http.begin("http://192.168.0.113:5000/sensorapi/");
    http.addHeader("Content-Type","application/json");
    int httpResponseCode = http.POST("{\"DEVICE_ID\":\""+Device_ID+"\",\"VALUE\":\""+T+"\"}");
    if(httpResponseCode>0){
      Serial.println(httpResponseCode);
			/* 
				if return 200, means upload successful, happy hacking
				500 means upload unsuccessful, Json string may have some wrong
				404 means URL may have some wrong 
			*/
    }else{
      Serial.println("Error on sending POST");
    }
    http.end();
    delay(1000);
  }
}
```

 

### GET方法

```arduino
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

const char* ssid = "SSID";     // Same AP as the server
const char* pwd = "password";
const String server_ip = xxx.xxx.xx.x:xxxx
const String Device_ID="fan1"; //Custom device ID
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  WiFi.begin(ssid,pwd);
  while(WiFi.status() != WL_CONNECTED){
    delay(100);
    Serial.println("Connecting to wifi...");
  }
  Serial.println("Done");
 }

void loop() {
  if((WiFi.status() == WL_CONNECTED)){
    HTTPClient http;
    http.begin("http://"+server_ip+"/io/"+Device_ID); 
    int httpCode = http.GET();
    if(httpCode>0){
      String payload = http.getString();
      StaticJsonDocument<200> doc;
      deserializeJson(doc, payload);
      const char* id=doc["Device_ID"];
      int st=doc["state"];
      Serial.print(id);
      Serial.print(",");
      Serial.println(st);   //Use variable "st" to do everything, happy hacking
    }
  }
}
```

## 註冊設備

1. 以127.0.0.1:8000為例，進入時會發現什麼設備都沒有
    
    ![Export-82d63faa-6e03-4c42-84aa-32bf264ce14d/IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.34.01.png](IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.34.01.png)
    
2. 用瀏覽器到伺服器後台：[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin/#/admin/device/device/)
    1. 登入後台：預設帳號為admin、密碼為admin
        
        ![IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.20.40.png](IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.20.40.png)
        
    2. 後台畫面
        
        ![IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.20.18.png](IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.20.18.png)
        
    3. 進入Device中
        
        ![IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.28.43.png](IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.28.43.png)
        
    4. 按Add
        
        ![IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.25.22.png](IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.25.22.png)
        
    5. 填寫Device ID、名稱(Name)、初始狀態(state)、icon (Fig，放網址)，接著按右下角儲存
        
        ![IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.32.03.png](IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.32.03.png)
        
    6. 完成註冊，並在[http://127.0.0.1:8000](http://127.0.0.1:8000/admin/#/admin/device/device/) 中可以看到生成一個按鈕，同理，註冊感測器也是一樣的流程，只是c.進入Device改成Sensor
        
        ![IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.35.26.png](IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.35.26.png)
        
        ![IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.36.03.png](IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.36.03.png)
        

## 設定場景

1. 在主頁的場景按鈕中，預設有全開和全關兩個場景
    
    ![IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.51.15.png](IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.51.15.png)
    
2. 要增加其他場景，如睡眠模式：開啟冷氣1、關閉所有燈
    1. 進入後台的Scenes，按Add
        
        ![IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.48.32.png](IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.48.32.png)
        
    2. 輸入場景名稱（中英文都可以）、在這個場景下想要開的物件ID(OpenDevice ID)和想要關的物件ID(closeDevice ID)，以逗號隔開，不要有空白鍵。若沒有要開啟或是關閉時，在欄位中填入“none“（小寫）。
        
        ![IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.54.02.png](IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.54.02.png)
        
    
    c. 儲存後，可以看到多了一種模式
    
    ![IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.55.19.png](IOT%20Kit%206a91c733c17847dea9ffa22cd2e208c9/%E6%88%AA%E5%9C%96_2021-08-02_%E4%B8%8B%E5%8D%881.55.19.png)
    

## 設定自動化

開發中。

## 設定定時器

開發中。
