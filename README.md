# RIME 標準吳語方案

適用於 [RIME](https://rime.im/) 的吳語輸入法。採用標準化的吳語音系。

A Standardized Shanghainese (Wu Language) Input Method for [RIME](https://rime.im/) engine.

測試反饋群：[![QQ群833433703](https://img.shields.io/static/v1?color=blue&label=QQ群&logo=Tencent+QQ&message=833433703&style=flat-square)](https://jq.qq.com/?_wv=1027&k=TP5MKGCC)

內包含：

- nguphing 標準吳語
- nguphing-soochow 標準吳語 蘇州音系
- nguphing-shanghai 標準吳語 上海音系

## 安裝

### Linux

```sh
git clone git@github.com:saeziae/rime_nguphing.git
cd rime_nguphing && ./linux_setup.sh
```

如果術初次安裝，會自動用 vim 調出`default.yaml`以便添加方案，添加之後請部署(Deploy)。

### 下載安裝

[![Download](https://img.shields.io/github/downloads/saeziae/rime_nguphing/total?style=for-the-badge)](https://github.com/saeziae/rime_nguphing/releases)

## 拼音體系

Romanization system

| 聲母 |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- |
| p    | ph  | b   | m   | f   | v   |
| t    | th  | d   | n   | l   |     |
| k    | kh  | g   | ng  | h   | gh  |
| c    | ch  | j   |     | sh  | zh  |
| tz   | ts  | dz  |     | s   | z   |

| 韻母 |      |      |
| ---- | ---- | ---- |
| y    | i    | u    |
|      | ui   | iu   |
| a    | ia   | ua   |
| ai   |      | uai  |
| ei   |      | uei  |
| o    | io   |      |
| ou   |      |      |
| eu   | ieu  |      |
| ae   | iae  | uae  |
| aeh  | iaeh | uaeh |
| oe   | ioe  | uoe  |
| oh   | ioh  | uoh  |
| e    | ie   | ue   |
| en   | in   | un   |
|      |      | iun  |
| eh   | ih   | ueh  |
|      |      | iuh  |
| ang  | iang | uang |
| ak   | iak  | uak  |
| ong  | iong | uong |
| ok   | iok  | uok  |
| eng  | ing  | ueng |
| ek   | ik   | uek  |
| ung  | iung |      |
| uk   | iuk  |      |

1. ghi/ghi(n/ng/h/k) ghu 寫作 yi wu，如 胡 wu，形 ying，紅 ghung
1. ghi- ghu- 寫作 y- w-，如 黃 wong
1. ie(h) iae(h) 實際可不做區分，輸入法中也模糊
1. ui iu 實際可不做區分，輸入法中也模糊
1. eng(/k) en(/h) 實際可不做區分，輸入法中也模糊
