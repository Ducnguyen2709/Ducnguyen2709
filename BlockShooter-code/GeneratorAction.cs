using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public class GeneratorAction : MonoBehaviour {
    public float Interval = 1.0f; //発生間隔（秒）
    public GameObject BlueBoxPrefab; //青箱のプレハブ
    public GameObject RedBoxPrefab; //赤箱のプレハブ
    public GameObject GreenBoxPrefab; //赤箱のプレハブ
    public GameObject SpawnBox;
    int count = 1;
    float Elapsed; //経過時間
    void GameStart() {
        enabled = true; //スクリプトを稼働させる
    }
    void Start() {
        Elapsed = 0.0f;
    }
    void Update() {
        Elapsed -= Time.deltaTime;
        if (Elapsed <= 0.0f) { //発生までの時間がゼロになったら
            Vector3 Pos = new Vector3( 0, 10.0f, 0 ); //箱を生成するランダム位置Pos
            Pos.x = Random.Range( -8.0f, 8.0f );
            Pos.z = Random.Range( -4.0f, 4.0f );
            //生成するプレハブを割り当てる


            if (count % 3 ==1){
                SpawnBox = RedBoxPrefab;
            }
            else
                if (count % 3 == 2) {
                    SpawnBox = BlueBoxPrefab;                  
                 } else {
                        SpawnBox = GreenBoxPrefab;     
                      }
            //箱のプレハブをインスタンス生成する
            Instantiate(SpawnBox, Pos, Random.rotation );
            Elapsed = Interval; //次の発生までの時間を設定
            count += 1;

           

        }
    }
}