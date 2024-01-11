# RIME 標準吳語方案

![License](https://img.shields.io/github/license/saeziae/rime_nguphing?style=for-the-badge)
[![Welcome to contribute](https://img.shields.io/badge/%E6%AD%A1%E8%BF%8E-%E5%8F%83%E8%88%87%E8%B2%A2%E7%8D%BB-1dd3b0?style=for-the-badge&logo=github)](https://github.com/saeziae/rime_nguphing/issues)
[![GitHub Workflow](https://img.shields.io/github/actions/workflow/status/saeziae/rime_nguphing/pack-trime.yml?label=%E5%B0%81%E8%A3%9D%E7%A8%8B%E5%BC%8F&logo=github&style=for-the-badge)](https://kawaii.estela.moe/a52f87782e563a4e5e915220603ede08)

用扗 [RIME](https://rime.im/) 上頭个吳語輸入法。用个是所謂个標準吳語。

适用于 [RIME](https://rime.im/) 的吴语输入法。采用标准化的吴语音系。

A Standardized Shanghainese (Wu Language) Input Method for [RIME](https://rime.im/) engine.

測試反饋：[![Telegram群@nguphing](https://img.shields.io/static/v1?color=blue&label=Telegram群&logo=Telegram&message=@nguphing&style=flat-square)](https://t.me/nguphing)

裏向包括：

- nguphing 標準吳語
- nguphin-yaehwei 標準吳語 吳語協會式拼寫
- nguphing-soochow 標準吳語 蘇州音系 （弗建議）
- nguphing-shanghai 標準吳語 上海音系 （弗建議）

## 安裝

### Windows

- 在扗開始菜單裏丄或者狀態欄个「ㄓ」圖標个右擊菜單裏丄揀「輸入法設定」
- 在彈出个窗口裏撳 「獲取更多輸入方案…」
- 然後在彈出个界面，輸入 `saeziae/rime_nguphing`，然後撳 Enter
- 關脫「Rime package installer」个窗口，回到「輸入法設定」個版面，勾選「吳語拼音」，然後撳「中」
- 修改或者弗修改配色，再撳「中」完成設定
- 在扗開始菜單裏丄或者狀態欄个「ㄓ」圖標个右擊菜單裏丄撳「重新部署」
- 撳 <kbd>Ctrl</kbd> 対 <kbd>`</kbd>，就可以見到「吳語拼音」哉

### MacOS, ibus on Linux

頭一次使用請先運行迭隻命令來獲取依賴文件：

```bash
curl -fsSL https://git.io/rime-install | bash -s -- :preset
```

運行下頭个命令來安裝或更新：

```bash
curl -fsSL https://git.io/rime-install | bash -s -- saeziae/rime_nguphing
```

請在 `default.yaml` 中增加輸入法；或者如果尔弗懂並且只需要使用吳語，請使用以下个自動命令：

```bash
curl -fsSL https://git.io/rime-install | bash -s -- custom:clear_schema_list custom:schema=nguphing custom:schema=nguphin-yaehwei custom:schema=luna_pinyin
```

- 其中 MacOS 可能會彈出叫尔安裝 git，要撳允許。Linux 一般有 git，如果嘸沒，請按照尔發行版个說明安裝。
- 運行着之後重新部署。
- 撳 <kbd>Ctrl/Control</kbd> 対 <kbd>`</kbd>，就可以見到「吳語拼音」哉

### fcitx5 on Linux

頭一次使用請先運行迭隻命令來獲取依賴文件：

```bash
curl -fsSL https://git.io/rime-install | rime_frontend=fcitx5-rime bash -s -- :preset
```

運行下頭个命令來安裝或更新：

```bash
curl -fsSL https://git.io/rime-install | rime_frontend=fcitx5-rime bash -s -- saeziae/rime_nguphing
```

請在 `default.yaml` 中增加輸入法；或者如果尔弗懂並且只需要使用吳語，請使用以下个自動命令：

```bash
curl -fsSL https://git.io/rime-install | rime_frontend=fcitx5-rime bash -s -- custom:clear_schema_list custom:schema=nguphing custom:schema=nguphin-yaehwei custom:schema=luna_pinyin
```

- 運行着之後重新部署。
- 撳 <kbd>Ctrl</kbd> 対 <kbd>`</kbd>，就可以見到「吳語拼音」哉

### fcitx on Linux

頭一次使用請先運行迭隻命令來獲取依賴文件：

```bash
curl -fsSL https://git.io/rime-install | rime_frontend=fcitx-rime bash -s -- :preset
```

運行下頭个命令來安裝或更新：

```bash
curl -fsSL https://git.io/rime-install | rime_frontend=fcitx-rime bash -s -- saeziae/rime_nguphing
```

請在 `default.yaml` 中增加輸入法；或者如果尔弗懂並且只需要使用吳語，請使用以下个自動命令：

```bash
curl -fsSL https://git.io/rime-install | rime_frontend=fcitx-rime bash -s -- custom:clear_schema_list custom:schema=nguphing custom:schema=nguphin-yaehwei custom:schema=luna_pinyin
```

- 運行着之後重新部署。
- 撳 <kbd>Ctrl </kbd> 対 <kbd>`</kbd>，就可以見到「吳語拼音」哉

### TRIME (Android)

從該許下載數據包，解壓到手機內部存儲空間个 `rime` 目錄。

[![GitHub Workflow](https://img.shields.io/github/actions/workflow/status/saeziae/rime_nguphing/pack-trime.yml?label=%E5%B0%81%E8%A3%9D%E7%A8%8B%E5%BC%8F&logo=github&style=for-the-badge)](https://kawaii.estela.moe/a52f87782e563a4e5e915220603ede08)

## [>用字標準](standard.md)

## [>拼音體系](romanization.md)

## 詞彙庫

- [x] 自編詞彙（標吳形式）
- [x] 蘇州詞庫《蘇州方言研究》（汪平）
- [x] 地名詞庫（上海、蘇南、浙江）
- [x] 《明清吴语词典》（石汝杰、宮田一郎）
- [ ] （計畫）《寧波方言字語彙解》（睦禮遜 Morrison）
- [ ] （計畫）《上海话大辞典》（錢乃榮等）
- [ ] （計畫）《寧波方言詞典》（湯珍珠等）
- [ ] （計畫）《無錫方言詞典》（項行）

## 感謝

- [RIME 輸入法引擎](https://rime.im/)
- [韻典網](https://ytenx.org/)
- [字海](http://zisea.com/)
- [Wiktionary](https://en.wiktionary.org/)
- 優秀个先生対前輩對吳語个研究
- 幫助調試个朋友道裏
- 每一位傳承與保護吳語个人

## [捐助](https://github.com/saeziae/rime_nguphing)
