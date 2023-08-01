    using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI; //uGUIを用いるのに必要
public class ScoreAction : MonoBehaviour
{
    float Elapsed; //経過時間
    public int count; //ターゲットは赤か？
    public int Score; //スコア
    public int Reward = 100; //加点ポイント
    public int Penalty = -25; //減点ポイント
    public float Interval = 10.0f; //赤青の切り替え間隔（既定値10秒）
    public Text txtMessage; //メッセージ表示
    public Text txtScore;
    void GameStart()
    {
        enabled = true; //スクリプトを稼働させる
    }
    void Start()
    {
        count = 1;
        txtScore.text = "SCORE : 0";
        Score = 0; //スコア
    }
    void OnDestroyBox(string boxColorName)
    {
        //破壊された箱の色名を元に判定して得点計算・表示する

        Score += (boxColorName == GetTargetColorName()) ? Reward : Penalty;
        txtScore.text = "SCORE : " + Score;
    }
    static string GetTargetColorName(string kara)
    { //真偽値をもとに文字列を返す関数
        if (count % 3 == 1)
        {
            kara = "Red";
        }
        else
            if (count % 3 == 2)
        {
            kara = "Blue";
        }
        else
        {
            kara = "Green";
        }
        return kara;
    }

    void Update()
    {
        Elapsed += Time.deltaTime;
        if (Elapsed > Interval)
        {
            count += 1; //赤青切り替え
            Elapsed = 0.0f;
        }
        //ターゲットを字と色で指示
        txtMessage.text = "Shoot " + GetTargetColorName() + " Boxes";

        if (count % 3 == 1)
        {
            txtMessage.color = Color.red;
        }
        else
            if (count % 3 == 2)
        {
            txtMessage.color = Color.blue;
        }
        else
        {
            txtMessage.color = Color.green;
        }
        count += 1;
    }
}
