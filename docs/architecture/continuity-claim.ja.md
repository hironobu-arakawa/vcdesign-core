# Continuity Claim Layer (継続主張層)

VCDesign は、システムを直接制御する機能ではありません。
この層は、システムが「価値が継続している（Value Continuous）」と主張できる**状態（Status）**を定義するためのプロトコルです。

## The Final Guard (最終防衛線)

> **This structure never improves value.**
> **It only prevents claiming continuity when value has already drifted.**
>
> （この構造は、決して価値を向上させない。）
> （これは、価値がすでに漂流しているにも関わらず『継続している』と主張することを防ぐだけである。）

この層にいかなる「生産性向上」「効率化」の期待も持ち込んではなりません。
これは、システムが VCDesign 準拠であるという看板（Claim）を、いつ剥奪すべきかを定義するものです。

## The Claim (主張の要件)

システムが「VCDesign 準拠である」と主張できるのは、以下の3つの要素がすべて機能している間だけです。

1.  **The Core (守るべき論理)**
    * 設計内価値（憲法、BOA、責任の閉包）が守られていること。
2.  **The Sensor (文脈乖離センサー)**
    * 前提の変化や文脈のズレ（Drift）を検知するセンサーが稼働しており、無視されていないこと。
3.  **The Loop (判断返却サイクル)**
    * 検知時に、システムを停止または設計へ差し戻すサイクルが機能していること。

これらが一つでも欠けた時、システムは動き続けるかもしれませんが、**「継続性（Continuity）」の主張は直ちに失効 (INVALID)** します。

## The Mechanism (判定ロジック)

この層は、以下のシグナル遷移を監視し、ステータスを決定します。

| Sensor State | Loop Action | **Claim Status** | Description |
| :--- | :--- | :--- | :--- |
| Normal | (Monitoring) | **VALID** | 正常稼働中。 |
| **Drift Detected** | **No Action / Ignored** | **INVALID** | 警告が無視された。もはやVCDesignではない。 |
| **Drift Detected** | **Returned / Stopped** | **VALID (Maintaining)** | 価値を守るために停止・返却したため、VCDesignの状態は維持されている。 |

「止まること」は失敗ではありません。
「止まらずに暴走すること」だけが、Claim の喪失を意味します。