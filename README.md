[![test](https://github.com/23C1049/ros2_mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/23C1049/ros2_mypkg/actions/workflows/test.yml)
# cigarettes_pub
## 概要
このリポジトリ内のROS2パッケージには、タバコを吸った本数によって減少する寿命をパブリッシュするノードが含まれています。
## ノード
### cigarettes_pub
このノードは吸ったタバコ１本あたり６分寿命が減る計算を２秒ごとに繰り返し行います。
### cigarettes_sub
このノードは計算結果をログに出力するためのテスト用です。
## トピック
### honsuu
吸ったタバコの合計本数をパブリッシュします。
### zyumyou
減った寿命の合計時間（分）をパブリッシュします。
## 実行例
以下は**ros2 launch**コマンドを入力し、１つの端末で**cigarettes_pub**と**cigarettes_sub**を同時に実行したときの結果です。

```bash
$ ros2 launch mypkg talk_listen.launch.py
```

```bash
[cigarettes_sub-2] [INFO] [1736499116.301584002] [listener]: タバコを1本吸いました
[cigarettes_sub-2] [INFO] [1736499116.304448559] [listener]: 寿命が6分減りました
[cigarettes_sub-2] [INFO] [1736499117.273485146] [listener]: タバコを2本吸いました
[cigarettes_sub-2] [INFO] [1736499117.274453836] [listener]: 寿命が12分減りました
[cigarettes_sub-2] [INFO] [1736499118.273813859] [listener]: タバコを3本吸いました
[cigarettes_sub-2] [INFO] [1736499118.274983160] [listener]: 寿命が18分減りました
[cigarettes_sub-2] [INFO] [1736499119.274042223] [listener]: タバコを4本吸いました
[cigarettes_sub-2] [INFO] [1736499119.275160349] [listener]: 寿命が24分減りました
[cigarettes_sub-2] [INFO] [1736499120.273457701] [listener]: タバコを5本吸いました
[cigarettes_sub-2] [INFO] [1736499120.274402474] [listener]: 寿命が30分減りました
[cigarettes_sub-2] [INFO] [1736499121.273170385] [listener]: タバコを6本吸いました
[cigarettes_sub-2] [INFO] [1736499121.274117441] [listener]: 寿命が36分減りました
```

## テスト環境
- ROS2 Foxy  
Ubuntu 20.04 LTS
- ROS2 Humble  
Ubuntu 22.04 LTS

## 参考資料
このプロジェクトを作成する上で参考にさせていただいたサイトを以下に記載します。
- [Qiita-Markdown記法チートシート](https://qiita.com/Qiita/items/c686397e4a0f4f11683d)  

## 著作権及びライセンス
- このソフトウェアパッケージは、３条項BSDライセンスの下、再頒布および使用が許可されます。  
- このパッケージに含まれるtest.ymlは、下記のコンテナ(by Ryuichi Ueda)から使用しています。  
    - https://hub.docker.com/repository/docker/ryuichiueda/ubuntu22.04-ros2  
- このパッケージに含まれるtalk_listen.launch.pyは、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを、本人の許可を得て自身の著作としたものです。  
    - https://ryuichiueda.github.io/slides_marp/robosys2024/lesson9.html  
- ©2025 Shizen Kotake
