<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif&family=Noto+Serif+SC:wght@500&family=Shippori+Mincho+B1:wght@500&display=swap');
body{
font-family: 'Shippori Mincho B1', 'Noto Serif SC','Noto Serif', serif;
}
rt{font-size:0.85rem}</style>
# RIME 標準吳語方案

![](https://img.shields.io/github/license/saeziae/rime_nguphing?style=flat-square)
![](https://img.shields.io/github/v/release/saeziae/rime_nguphing?style=flat-square)
[![Download](https://img.shields.io/github/downloads/saeziae/rime_nguphing/total?style=flat-square)](https://github.com/saeziae/rime_nguphing/releases/latest)

用扗 [RIME](https://rime.im/) 上頭个吳語輸入法。用个是標準吳語。

适用于 [RIME](https://rime.im/) 的吴语输入法。采用标准化的吴语音系。

A Standardized Shanghainese (Wu Language) Input Method for [RIME](https://rime.im/) engine.

測試反饋群：[![QQ群833433703](https://img.shields.io/static/v1?color=blue&label=QQ群&logo=Tencent+QQ&message=833433703&style=flat-square)](https://jq.qq.com/?_wv=1027&k=TP5MKGCC)

裏向包括：

- nguphing 標準吳語
- nguphing-soochow 標準吳語 蘇州音系
- nguphing-shanghai 標準吳語 上海音系

## 安裝

### Linux & MacOS

首先確保安裝着 `fcitx5-rime` `ibus-rime` `fcitx-rime` 任何之一，MacOS 則是 [鼠鬚管](https://github.com/rime/squirrel/releases/latest)

[迭隻是詳細指南](https://github.com/rime/home/wiki/CustomizationGuide)

安裝方案：

```sh
git clone git@github.com:saeziae/rime_nguphing.git
cd rime_nguphing && ./linux_setup.sh
```

倘使尔是頭一届安裝，會自動用 vim 調出`default.yaml`方便尔添加方案，添加着之後請部署(Deploy)（一般在狀態欄个「ㄓ」个右擊菜單裏）。

### Windows

安裝[小狼毫](https://github.com/rime/weasel/releases/latest)

下載[方案](https://github.com/saeziae/rime_nguphing/releases/latest)，選擇`bin`或`yaml`版本全可以个。

打開【開始菜單】>【小狼毫輸入法】>【用戶文件夾】

將`nguphing-xxxxxxxx.zip`解壓到尔打開个【用戶文件夾】。（如果是`bin`版本，尔應該看不見多出啥文件，箇是正常个）

打開【開始菜單】>【小狼毫輸入法】>【輸入法設定】，勾選伲个輸入法。

### 下載方案

[![Download](https://img.shields.io/github/downloads/saeziae/rime_nguphing/total?style=flat-square)](https://github.com/saeziae/rime_nguphing/releases/latest)

## [>用字標準](standard.md)

## [>拼音體系](romanization.md)

## 畀眼銅鈿鼓勵鼓勵

<span background style="background-color:lightgrey;color: black;">
<img style="height:1em;vertical-align:baseline;" src="https://simpleicons.org/icons/ethereum.svg"/>ETH </span>
<span style="background-color:black;color:white">0x888117715a884a7F84B88CBBBF7998745A5FF96D</span>

<a href="https://liberapay.com/estela/donate"><img alt="Donate using Liberapay" src="https://liberapay.com/assets/widgets/donate.svg"></a>
[![Buy me a coffee](https://img.shields.io/static/v1?label=Ko-fi&message=Buy+me+a+coffee&color=FF5E5B&logo=Ko-fi&style=flat-square)](https://ko-fi.com/saeziae)

## 感謝

- [RIME 輸入法引擎](https://rime.im/)
- [韻典網](https://ytenx.org/)
- [字海](http://zisea.com/)
- [Wiktionary](https://en.wiktionary.org/)
- <u>汪平</u>老師對吳語个研究
- 幫助調試个朋友道裏
- 每一位傳承與保護吳語个人
