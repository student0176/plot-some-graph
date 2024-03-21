所謂*數據可視化*就是將數據弄成更加直觀的圖，*數據挖掘*就是用代碼來探索數據的規律。數據可以説一個小型數字列表，也可以是多字節的數據。
用到的東西有：python, matplotlib庫, Pygal庫

之前chatgpt幫了不少忙，這次卻一再幫倒忙。畢竟這種‘早年項目’大家都做過，直接csdn反而應有盡有，比方説json文件、bmp圖片（skr~），以及這次import報紅，原因很簡單：包已經廢棄或更新。chatgpt的回答是`pip upgrade`。我當然不能對一個語言模型過分苛責，這是自己考慮的情況不夠多，也太過於依賴chatgpt，合該有此情況。

## 牛刀小試
* 快速的華個折綫圖：

![a.jpg](image_rw/a.jpg)

再慢慢引入新東西

![aline.jpg](image_rw%2Faline.jpg)

爲什麽4對應25呢？大概是從0開始索引的吧，那就把x和y兩個list都傳進去：

![aline_add_xaixs.jpg](image_rw%2Faline_add_xaixs.jpg)


* 然後是scatter：

![scatter.jpg](image_rw%2Fscatter.jpg)

一個很重要的color_map，即用不同顔色來區分某種量。思路是將color參數c弄成列表，與值域相同，指定cmap

![scatter_colormap.jpg](image_rw%2Fscatter_colormap.jpg)

## 隨機漫步
*按：圖可能有點多，可以看一下圖的名稱，基本意思都在裏面*
這裏代碼很好理解，就是每次該變量加上原來數組的位置，主要是要理解代碼對解決數學問題的幫助。

![rw.jpg](image_rw%2Frw.jpg)

爲了表達出運動痕跡，巧妙地用顔色的濃淡變化來顯示，厲害！

![rw_color.jpg](image_rw%2Frw_color.jpg)
![rw_color_+2.jpg](image_rw%2Frw_color_%2B2.jpg)
![rw_color_+2axis.jpg](image_rw%2Frw_color_%2B2axis.jpg)
![rw_1w_point.jpg](image_rw%2Frw_1w_point.jpg)
![rw_1w_point_figsize.jpg](image_rw%2Frw_1w_point_figsize.jpg)

## 擲骰子
用pygal包生成可縮放的矢量圖，這個好處就是能夠自如地scale以適應屏幕，所以適合放在online的網頁上。

![die_visual.svg](image_die%2Fdie_visual.svg)

這個圖片在瀏覽器中打開個空白頁，將它拖進去，然後鼠標懸停后會顯示相應的信息，真個不錯！

![die_visual_2.svg](image_die%2Fdie_visual_2.svg)
![die_visual_6+12.svg](image_die%2Fdie_visual_6%2B12.svg)
![die_visual_6+10.svg](image_die%2Fdie_visual_6%2B10.svg)

既然程序生成隨機數這麽容易又快速，自然也可以來求pi的近似值，這就是蒙特卡洛思想的核心。

## 下載數據，然後可視化
主要集中於csv與json文件。
所謂csv文件，無他，就是以逗號分隔的一些數值，如2022-5-31,61,-5,,,,10,4,,195,,

![01.jpg](image_tempreture%2F01.jpg)
![full_year.jpg](image_tempreture%2Ffull_year.jpg)
![full_year_add_low.jpg](image_tempreture%2Ffull_year_add_low.jpg)
![full_year_fill.jpg](image_tempreture%2Ffull_year_fill.jpg)
![death_valley.jpg](image_tempreture%2Fdeath_valley.jpg)

可以發現後者晝夜溫差大。

## json的世界人口地圖
剛開始的COUNTRIES弄國別碼費了不少時間,原來是`from pygal.i18n import COUNTRIES`早就廢棄了,安裝`from pygal_maps_world.i18n import COUNTRIES`來代替.

有了國別碼后,製作地圖易如反掌,用pygal提供的Worldmap.不過這裏`wm = pygal.Worldmap()`也會報錯,用
```javascript
import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm.title = 'North, Central, and South America'
wm.add('North America',['ca','mx','us'])
--snip--

wm.render_to_file('./image_map/americas.svg')
```

![americas.svg](image_map%2Famericas.svg)

傳入列表就是為不同縮寫著色,傳入dict進一步調節顔色深淺

![americas_population.svg](image_map%2Famericas_population.svg)
![population_notonly_us.svg](image_map%2Fpopulation_notonly_us.svg)

我好像看到了一個遙遙領先的國度,然後有的人便玩不起了,轉換思路掩耳盜鈴:

![population_3groups.svg](image_map%2Fpopulation_3groups.svg)
![population_change_style.svg](image_map%2Fpopulation_change_style.svg)

## 使用API
`pip requests`來向網站請求信息、檢查返回值。
即用Web應用編程接口自動請求網頁的特定信息而不是整個網頁,再可視化.這個方法具有實時性,因爲采集的都是最新信息.
將使用github的api來請求該網站中py項目的有關信息,可視化其受歡迎程度.
既然通過api調用來請求各種信息,那何爲api調用?輸入
`https://api.github.com/search/repositories?q=language:python&sort=stars`
后回車
```javascript
{
  "total_count": 13874844,
  "incomplete_results": true,
  "items": [
    {
      "id": 54346799,
      "node_id": "MDEwOlJlcG9zaXRvcnk1NDM0Njc5OQ==",
      "name": "public-apis",
       --snip--
```
true説明請求確實不完整,github無法全面處理該api
查看搜索api的速率限制：
`https://api.github.com/rate_limit`
由`"search":{"limit":10,`可知極限為每分鐘10個請求，當前分鐘内還剩下9個請求

![python_repos.svg](image_map%2Fpython_repos.svg)

將格式參數等都打包成my_config，然後跟原來差不多：

![python_repos_finetune.svg](image_map%2Fpython_repos_finetune1.svg)
![python_repos_finetune.svg](image_map%2Fpython_repos_finetune2.svg)

這二者區別顯而易見。

## hacker news api
`https://hacker-news.firebaseio.com/v0/topstories.json`
